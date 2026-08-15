#!/usr/bin/env python3
"""INQUISITIO-1492 — BADANIE UŻYTECZNOŚCI I WPŁYWU ELEMENTÓW (Ablation & Impact Audit).

Narzędzie analityczne do badania wkładu każdego pojedynczego elementu gry w balans:
  1. Ablacja Kart (Per-Card Ablation): Wyłącza każdą z 50 kart z osobna i bada:
     - Wpływ na Win Share frakcji (czy frakcja bez niej wygrywa, czy przegrywa)
     - Wpływ na Global Balance Score (czy karta destabilizuje stół, czy stabilizuje)
     - Wpływ na tempo partii (Średnia Er) i wskaźnik deadlocków
  2. Klasyfikacja Kart:
     - 👑 FILAR FRAKCJI (Core Keystone): Kluczowy motor napędowy wygranych frakcji
     - ⚖️ ZBALANSOWANE NARZĘDZIE (Utility): Zdrowe, elastyczne narzędzie taktyczne
     - 💤 MARTWA KARTA (Dead Weight): Zerowy wpływ na grę (kandydat do wzmocnienia/reworku)
     - ⚠️ KARTA TOKSYCZNA (Disruptor): Karta, której usunięcie poprawia balans stołu
  3. Ablacja Mechanik Systemowych (System Ablation):
     - Wpływ Kroniki Dziejów (Talia Czasu), Cooldownu Autodafé, Złota Startowego itp.

Generuje pełny raport w: playtesting/sim-reports/raport_uzytecznosci_i_wplywu.md
"""
from __future__ import annotations

import argparse
import copy
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from pathlib import Path
from typing import Any

# Ensure sim and tools/sim directories are on path
TOOLS_SIM_DIR = Path(__file__).resolve().parent
SIM_DIR = TOOLS_SIM_DIR.parent.parent / "sim"

for p in (TOOLS_SIM_DIR, SIM_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from inquisitio.cards.loader import load_all_cards
from inquisitio.config import CONFIG
from inquisitio.engine.setup import SETUP_PRESETS, FactionId
from inquisitio.runner.audit_facts import score_pair, save_and_archive_report
from inquisitio.runner.batch import run_batch
from inquisitio.runner.scoring import (
    calculate_category_scores,
    calculate_global_score,
    calculate_setup_score,
    color_score,
)

REPORTS_DIR = Path(__file__).resolve().parent.parent.parent / "playtesting" / "sim-reports"
OUTPUT_REPORT_PATH = REPORTS_DIR / "raport_uzytecznosci_i_wplywu.md"

FACTION_NAMES = {
    FactionId.SWIETE_OFICJUM: "SO",
    FactionId.CIENIE_AL_ANDALUS: "CAA",
    FactionId.KORONA_BORGIOWIE: "KB",
    FactionId.KABALA_TOLEDO: "KT",
    FactionId.GILDIA_CIENI: "GC",
}

PREFIX_TO_FACTION_ID = {
    "so": FactionId.SWIETE_OFICJUM,
    "caa": FactionId.CIENIE_AL_ANDALUS,
    "kb": FactionId.KORONA_BORGIOWIE,
    "kt": FactionId.KABALA_TOLEDO,
    "gc": FactionId.GILDIA_CIENI,
}

FACTION_ID_TO_PREFIX = {v: k for k, v in PREFIX_TO_FACTION_ID.items()}

FACTION_FULL_NAMES = {
    "so": "Święte Oficjum",
    "caa": "Cienie Al-Andalus",
    "kb": "Korona & Borgiowie",
    "kt": "Kabała z Toledo",
    "gc": "Gildia Cieni",
}


def _run_ablation_task(task_args: tuple[str, str, dict, int, int, list[str]]) -> dict:
    """Simulates the full 16-setup suite under a specific ablation / modification."""
    element_id, element_name, sys_overrides, games_per_setup, seed, setups = task_args
    t0 = time.time()

    summaries = []
    setup_scores = {}
    faction_wins: dict[str, int] = {}
    faction_total_games: dict[str, int] = {}

    for sname in setups:
        summary = run_batch(
            games=games_per_setup,
            setup=sname,
            seed=seed,
            layer="C",
            win_overrides=sys_overrides,
        )
        summaries.append(summary)
        setup_scores[sname] = calculate_setup_score(summary)

        factions = SETUP_PRESETS[sname]
        for fid in factions:
            fname = FACTION_NAMES[fid]
            w_count = summary.wins.get(fid, 0)
            faction_wins[fname] = faction_wins.get(fname, 0) + w_count
            faction_total_games[fname] = faction_total_games.get(fname, 0) + summary.games

    cat_scores = calculate_category_scores(summaries)
    global_score = calculate_global_score(cat_scores)
    dt = round(time.time() - t0, 2)

    n_sum = len(summaries)
    eras_avg = sum(s.eras_avg for s in summaries) / n_sum
    deadlock_pct = (sum(s.eras_limit_pct for s in summaries) / n_sum) * 100.0
    poverty_pct = (sum(s.passes_forced_pct for s in summaries) / n_sum) * 100.0
    autodafe_avg = sum(s.autodafe_avg for s in summaries) / n_sum
    acc_avg = sum(s.accusations_avg for s in summaries) / n_sum

    faction_win_shares = {}
    for fname, total_g in faction_total_games.items():
        if total_g > 0:
            faction_win_shares[fname] = round((faction_wins.get(fname, 0) / total_g) * 100.0, 2)

    return {
        "id": element_id,
        "name": element_name,
        "overrides": sys_overrides,
        "global_score": global_score,
        "cat_scores": cat_scores,
        "setup_scores": setup_scores,
        "faction_win_shares": faction_win_shares,
        "eras_avg": eras_avg,
        "deadlock_pct": deadlock_pct,
        "poverty_pct": poverty_pct,
        "autodafe_avg": autodafe_avg,
        "acc_avg": acc_avg,
        "dt": dt,
    }


def classify_card_impact(
    delta_faction_share: float,
    delta_global_score: float,
    card_id: str,
) -> tuple[str, str]:
    """Classifies a card's strategic role in the game based on ablation deltas.
    Note: delta_faction_share = (base_share - ablated_share).
    If positive -> removing card hurt the faction -> card was a driver of victory.
    """
    if delta_faction_share >= 3.0:
        return "👑 FILAR FRAKCJI", "Kluczowa dla wygranej; usunięcie drastycznie osłabia frakcję."
    elif delta_global_score >= 1.5 or delta_faction_share <= -2.5:
        return "⚠️ TOKSYCZNA / DESTABILIZUJĄCA", "Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację."
    elif abs(delta_faction_share) <= 0.6 and abs(delta_global_score) <= 0.5:
        return "💤 MARTWA KARTA", "Zerowy wpływ na wynik; grana bardzo rzadko (kandydat do wzmocnienia)."
    else:
        return "⚖️ ZBALANSOWANE NARZĘDZIE", "Zdrowe narzędzie sytuacyjne o umiarkowanym wpływie."


def run_full_ablation_audit(games_per_setup: int = 5000, seed: int = 42, workers: int = 8) -> Path:
    """Executes the complete ablation & impact audit suite across cards and system mechanics."""
    t_start = time.time()
    setups = sorted(SETUP_PRESETS.keys())
    cards = load_all_cards()

    print("═══════════════════════════════════════════════════════════════════════")
    print("   INQUISITIO-1492 — BADANIE UŻYTECZNOŚCI I WPŁYWU ELEMENTÓW GRY       ")
    print("   Testy Ablacyjne (Ablation Study) 50 Kart & Mechanik Systemowych     ")
    print("═══════════════════════════════════════════════════════════════════════")
    print(f"Bieżąca wersja gry:     {CONFIG.version}")
    print(f"Próba na element:       {games_per_setup} gier / setup ({games_per_setup * 16} gier łącznie)")
    print(f"Liczba procesów CPU:    {workers}")
    print(f"Ziarno generatora:      {seed}")
    print("═══════════════════════════════════════════════════════════════════════\n")

    # 1. BASELINE RUN
    print("🔍 [1/3] Pomiar Bazy Referencyjnej (Pełny stan gry)...")
    base_task = ("BASE", "Pełna gra (Stan bieżący)", {}, games_per_setup, seed, setups)
    base_res = _run_ablation_task(base_task)
    print(f"   ✔ Baza Global Score: {color_score(base_res['global_score'], bold=True)} pkt")
    print(f"   ✔ Win Shares Frakcji: " + " | ".join([f"{f}: {s:.1f}%" for f, s in sorted(base_res['faction_win_shares'].items())]))
    print(f"   ✔ Telemetria: Średnia Er {base_res['eras_avg']:.2f}, Deadlocki {base_res['deadlock_pct']:.1f}%, Pas Biedy {base_res['poverty_pct']:.1f}%\n")

    # 2. PER-CARD ABLATION TASKS
    print(f"🧬 [2/3] Generowanie i badanie ablacyjne 50 kart frakcji...")
    card_tasks = []
    for cid, c in sorted(cards.items()):
        if cid.startswith("time-"):
            continue
        task_name = f"BEZ {cid.upper()} ({c.name})"
        sys_overrides = {"disabled_cards": [cid]}
        card_tasks.append((cid, task_name, sys_overrides, games_per_setup, seed, setups))

    with ProcessPoolExecutor(max_workers=min(workers, len(card_tasks))) as executor:
        card_results = list(executor.map(_run_ablation_task, card_tasks))

    print(f"   ✔ Zbadano ablacyjnie {len(card_results)} kart.\n")

    # 3. SYSTEM MECHANICS & VICTORY PATH ABLATION (Turning complete subsystems ON/OFF)
    print("⚙️ [3/3] Badanie czysto ablacyjne podsystemów i ścieżek zwycięstwa (Ablation Scenarios)...")

    ablation_scenarios = [
        # --- PODSYSTEMY GLOBALNE ---
        ("ABL_TIME_DECK_OFF", "Talia Czasu (Kronika Dziejów): Całkowite WYŁĄCZENIE", {"no_time_deck": True}, "Globalne Podsystemy"),
        ("ABL_AUTODAFE_OFF", "Autodafé: Całkowite WYŁĄCZENIE (brak kary śmierci)", {"so_stacks_offset": 99, "cooldown_offset": 99}, "Globalne Podsystemy"),
        ("ABL_AUTODAFE_NO_COOLDOWN", "Cooldown Autodafé: WYŁĄCZENIE (Autodafé co turę)", {"cooldown_offset": -3}, "Globalne Podsystemy"),
        ("ABL_INQUISITOR_FREEZE", "Ruch Inkwizytora: WYŁĄCZENIE (Inkwizytor stoi w miejscu)", {"inquisitor_speed": 0}, "Globalne Podsystemy"),
        ("ABL_START_GOLD_ZERO", "Złoto Startowe: WYŁĄCZENIE (Start z 0 zł)", {"start_gold_offset": -3}, "Globalne Podsystemy"),
        ("ABL_HAND_LIMIT_LOW", "Limit Ręki: Redukcja do 4 kart (Presja dociągu)", {"hand_limit_offset": -1}, "Globalne Podsystemy"),

        # --- ABLACJA ŚCIEŻEK ZWYCIĘSTWA (VICTORY PATHS) ---
        ("ABL_SO_ONLY_STACKS", "Święte Oficjum: Wyłączenie Skazań (Wygrana TYLKO przez Stosy)", {"so_condemns_offset": 99}, "Ścieżki Zwycięstwa"),
        ("ABL_SO_ONLY_CONDEMNS", "Święte Oficjum: Wyłączenie Stosów (Wygrana TYLKO przez Skazania)", {"so_stacks_offset": 99}, "Ścieżki Zwycięstwa"),
        ("ABL_CAA_NO_SEA_ROUTE", "Cienie Al-Andalus: Wyłączenie Szlaku Morskiego (Tylko Ląd)", {"sea_route_era": 99}, "Ścieżki Zwycięstwa"),
        ("ABL_CAA_EARLY_SEA_ROUTE", "Cienie Al-Andalus: Szlak Morski Otwarty od Ery 1", {"sea_route_era": 1}, "Ścieżki Zwycięstwa"),
        ("ABL_KB_NO_HOOK_GATE", "Korona & Borgiowie: Wyłączenie Wymogu Haków (Tylko Dekrety)", {"kb_hooks": 0}, "Ścieżki Zwycięstwa"),
        ("ABL_KT_NO_HERESY_GATE", "Kabała z Toledo: Wyłączenie Pasma Herezji (Bezpieczna Iluminacja)", {"kt_heresy_band": (0, 99)}, "Ścieżki Zwycięstwa"),
        ("ABL_GC_STATIC_FALLS", "Gildia Cieni: Wyłączenie Modyfikatora 'Bez Oficjum' (Stały próg upadków)", {"gc_falls_no_oficjum_offset": -1}, "Ścieżki Zwycięstwa"),
    ]

    sys_tasks = []
    sys_categories: dict[str, str] = {}

    for s_id, s_name, s_params, s_cat in ablation_scenarios:
        sys_tasks.append((s_id, s_name, s_params, games_per_setup, seed, setups))
        sys_categories[s_id] = s_cat

    with ProcessPoolExecutor(max_workers=min(workers, len(sys_tasks))) as executor:
        sys_results = list(executor.map(_run_ablation_task, sys_tasks))

    print(f"   ✔ Zbadano ablacyjnie {len(sys_results)} kluczowych podsystemów i ścieżek gry.\n")

    # 4. ANALYZE AND FORMAT REPORT
    print("📄 Generowanie i formatowanie raportu użyteczności...")
    total_elapsed = round(time.time() - t_start, 1)

    analyzed_cards = []
    for r in card_results:
        cid = r["id"]
        c = cards.get(cid)
        pref = cid.split("-")[0]
        fname = FACTION_NAMES.get(PREFIX_TO_FACTION_ID.get(pref))
        
        base_share = base_res["faction_win_shares"].get(fname, 0.0)
        ablated_share = r["faction_win_shares"].get(fname, 0.0)
        
        # Delta: positive means faction LOST win share without this card -> card contributes to win
        d_share = round(base_share - ablated_share, 2)
        d_global = round(r["global_score"] - base_res["global_score"], 2)
        d_eras = round(r["eras_avg"] - base_res["eras_avg"], 2)
        
        category, desc = classify_card_impact(d_share, d_global, cid)

        analyzed_cards.append({
            "id": cid,
            "name": c.name if c else cid,
            "faction_pref": pref,
            "faction_name": fname,
            "cost": c.cost if c else 0,
            "heresy": c.heresy if c else 0,
            "base_share": base_share,
            "ablated_share": ablated_share,
            "d_share": d_share,
            "global_score": r["global_score"],
            "d_global": d_global,
            "eras_avg": r["eras_avg"],
            "d_eras": d_eras,
            "deadlock_pct": r["deadlock_pct"],
            "category": category,
            "desc": desc,
        })

    # Sortings for special categories
    core_cards = sorted([c for c in analyzed_cards if "FILAR" in c["category"]], key=lambda x: x["d_share"], reverse=True)
    dead_cards = sorted([c for c in analyzed_cards if "MARTWA" in c["category"]], key=lambda x: abs(x["d_share"]))
    disruptive_cards = sorted([c for c in analyzed_cards if "TOKSYCZNA" in c["category"]], key=lambda x: x["d_global"], reverse=True)

    today_str = datetime.now().strftime("%Y-%m-%d %H:%M")

    lines = [
        f"# Raport Użyteczności i Wpływu Elementów Gry (Ablation & Impact Audit) — Wersja: {CONFIG.version}",
        "",
        f"**Wersja Gry:** `{CONFIG.version}` | **Data:** {today_str} | **Próba:** {games_per_setup} gier/setup ({games_per_setup * 16} gier/test) | **Czas Analizy:** {total_elapsed}s",
        "",
        "Raport przedstawia wyniki badania ablacyjnego (**Feature Importance / Ablation Study**).",
        "Dla każdego elementu zbadano zachowanie ekosystemu gry **po jego całkowitym wyłączeniu**.",
        "",
        "---",
        "",
        "## 1. Podsumowanie Wniosków Strategicznych",
        "",
        f"- **👑 Liczba Filarów Frakcji (Kluczowe Karty Wygranych):** `{len(core_cards)}` kart",
        f"- **💤 Liczba Martwych Kart (Kandydaci do Wzmocnienia / Reworku):** `{len(dead_cards)}` kart",
        f"- **⚠️ Liczba Kart Destabilizujących (Kandydaci do Osłabienia):** `{len(disruptive_cards)}` kart",
        f"- **⚖️ Liczba Zbalansowanych Narzędzi Taktycznych:** `{len(analyzed_cards) - len(core_cards) - len(dead_cards) - len(disruptive_cards)}` kart",
        "",
        "---",
        "",
        "## 2. 👑 Filary Frakcji (Najważniejsze Karty Napędzające Wygraną)",
        "",
        "Karty, których wyłączenie drastycznie obniża szanse na zwycięstwo danej frakcji ($\Delta \text{Win Share} \ge +3.0\%$):",
        "",
        "| Karta | Frakcja | Koszt / Herezja | Win Share (Baza → Bez Karty) | Spadek Szans ($\Delta$) | Global Score po Usunięciu | Rola i Diagnoza |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :--- |",
    ]

    for c in core_cards:
        ds_str = f"-{c['d_share']:.1f}%" if c['d_share'] > 0 else f"+{abs(c['d_share']):.1f}%"
        lines.append(
            f"| `{c['id']}` **{c['name']}** | {c['faction_name']} | {c['cost']}zł / {c['heresy']}☣ | "
            f"{c['base_share']:.1f}% → **{c['ablated_share']:.1f}%** | **`{ds_str}`** 🔻 | {c['global_score']:.1f} pkt | {c['desc']} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 3. 💤 Martwe Karty (Kandydaci do Wzmocnienia lub Reworku)",
        "",
        "Karty, których usunięcie z gry nie wywołuje niemal żadnego mierzalnego efektu ($|\Delta \text{Win Share}| \le 0.6\%$). Są rzadko zagrywane lub ich efekt jest zbyt słaby:",
        "",
        "| Karta | Frakcja | Koszt / Herezja | Win Share (Baza → Bez Karty) | Wpływ ($\Delta$) | Status Rekomendacji |",
        "| :--- | :---: | :---: | :---: | :---: | :--- |",
    ])

    if dead_cards:
        for c in dead_cards:
            lines.append(
                f"| `{c['id']}` **{c['name']}** | {c['faction_name']} | {c['cost']}zł / {c['heresy']}☣ | "
                f"{c['base_share']:.1f}% → {c['ablated_share']:.1f}% | `{c['d_share']:+.1f}%` | ⚠️ Wymaga obniżenia kosztu, dodania złota lub wzmocnienia efektu |"
            )
    else:
        lines.append("| — | — | — | — | — | ✅ Brak całkowicie martwych kart w talii! |")

    lines.extend([
        "",
        "---",
        "",
        "## 4. ⚠️ Karty Destabilizujące / Toksyczne",
        "",
        "Karty, których wyłączenie z talii **podnosi ogólny wynik zbalansowania gry** ($\Delta \text{Global} > +1.0$ pkt):",
        "",
        "| Karta | Frakcja | Koszt / Herezja | Global Score (Baza → Bez Karty) | Zysk Balansu ($\Delta$) | Diagnoza |",
        "| :--- | :---: | :---: | :---: | :---: | :--- |",
    ])

    if disruptive_cards:
        for c in disruptive_cards:
            lines.append(
                f"| `{c['id']}` **{c['name']}** | {c['faction_name']} | {c['cost']}zł / {c['heresy']}☣ | "
                f"{base_res['global_score']:.1f} → **{c['global_score']:.1f} pkt** | **`{c['d_global']:+.1f} pkt`** 🟢 | {c['desc']} |"
            )
    else:
        lines.append("| — | — | — | — | — | ✅ Brak toksycznych kart psujących balans stołu! |")

    lines.extend([
        "",
        "---",
        "",
        "## 5. 📋 Pełna Tabela Ablacji Wszystkich 50 Kart Frakcji",
        "",
        "| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Faction Win Share | $\Delta$ Frakcji | Global Score | $\Delta$ Global | Śr. Er | Deadlock % | Kategoria Roli |",
        "| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |",
    ])

    for c in analyzed_cards:
        ds_sign = f"-{c['d_share']:.1f}%" if c['d_share'] > 0 else f"+{abs(c['d_share']):.1f}%"
        dg_sign = f"+{c['d_global']:.1f}" if c['d_global'] > 0 else f"{c['d_global']:.1f}"
        lines.append(
            f"| `{c['id']}` | **{c['name']}** | {c['faction_name']} | {c['cost']} | {c['heresy']} | "
            f"{c['base_share']:.1f}% → {c['ablated_share']:.1f}% | `{ds_sign}` | "
            f"{c['global_score']:.1f} | `{dg_sign}` | {c['eras_avg']:.2f} | {c['deadlock_pct']:.1f}% | {c['category']} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 6. ⚙️ Ablacja Podsystemów i Ścieżek Zwycięstwa (Mechanics Ablation)",
        "",
        "Badanie odporności gry na całkowite wyłączenie poszczególnych podsystemów, zasad lub ścieżek wygranej.",
    ])

    for cat_name in ["Globalne Podsystemy", "Ścieżki Zwycięstwa"]:
        cat_results = [r for r in sys_results if sys_categories.get(r["id"]) == cat_name]
        if not cat_results:
            continue

        lines.extend([
            "",
            f"### {cat_name}",
            "",
            "| Badany Scenariusz Ablacji | Global Score | $\Delta$ Global | Średnia Er | Deadlocks % | Pas Biedy % | Diagnoza i Wpływ na Ekosystem Gry |",
            "| :--- | :---: | :---: | :---: | :---: | :---: | :--- |",
        ])

        for r in cat_results:
            dg = r["global_score"] - base_res["global_score"]
            dg_str = f"+{dg:.1f}" if dg > 0 else f"{dg:.1f}"
            
            if dg >= 1.0:
                diag = "🟢 Zysk balansu — mechanika w obecnej formie obciążała stół"
            elif dg <= -15.0:
                diag = "🔴 Katastrofa ekosystemu — filar bezwzględnie krytyczny dla gry"
            elif dg <= -5.0:
                diag = "🟠 Poważna destabilizacja — silnik traci płynność lub różnorodność"
            else:
                diag = "⚪ Wpływ neutralny / mechanika opcjonalna"

            lines.append(
                f"| **{r['name']}** | {score_pair(base_res['global_score'], r['global_score'], colored=True)} | "
                f"`{dg_str} pkt` | {r['eras_avg']:.2f} Er | {r['deadlock_pct']:.1f}% | {r['poverty_pct']:.1f}% | {diag} |"
            )

    lines.extend([
        "",
        "---",
        "",
        "## 7. Metodologia Badania",
        "",
        "- **Ablacja Pojedynczego Elementu (Leave-One-Out):** Każdy test usuwa dokładnie 1 kartę lub zmienia 1 mechanikę bazową.",
        "- **Wpływ na Frakcję ($\Delta$ Win Share):** Różnica $WS_{\text{baza}} - WS_{\text{bez\_karty}}$. Dodatnia wartość oznacza, że karta napędzała wygrane frakcji.",
        "- **Wpływ na Balans Gry ($\Delta$ Global):** Zmiana wyniku globalnego po usunięciu elementu.",
        "- **Rygor Próby:** Każdy wariant jest testowany na pełnym pakiecie 16 setupów (min. 1000 gier/setup = 16 000 partii na kartę).",
    ])

    report_path, arch_path = save_and_archive_report(lines, "raport_uzytecznosci_i_wplywu.md")
    print(f"\n✅ RAPORT WYGENEROWANY POMYŚLNIE!")
    print(f"   Raport:    {report_path}")
    print(f"   Archiwum:  {arch_path}\n")
    return report_path


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 Feature & Card Impact Audit (Ablation Study)")
    parser.add_argument("--games", type=int, default=5000, help="Liczba gier na setup (domyślnie: 5000, min. 1000)")
    parser.add_argument("--workers", type=int, default=min(os.cpu_count() or 4, 10), help="Liczba wątków równoległych")
    parser.add_argument("--seed", type=int, default=42, help="Ziarno losowe (CRN)")

    args = parser.parse_args()
    if args.games < 1000:
        print("⚠️ Podwyższam próbę do wymaganego minimum 1000 gier.")
        args.games = 1000

    run_full_ablation_audit(games_per_setup=args.games, seed=args.seed, workers=args.workers)


if __name__ == "__main__":
    main()
