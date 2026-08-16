#!/usr/bin/env python3
"""INQUISITIO-1492 — BADANIE UŻYTECZNOŚCI I WPŁYWU ELEMENTÓW W KANONIE 4P (Ablation & Impact Audit 4P).

Specjalistyczne narzędzie analityczne do badania wkładu każdego pojedynczego elementu gry w Kanon 4-osobowy (4P):
  1. Ablacja Kart (Per-Card Ablation w 4P): Wyłącza każdą z 50 kart z osobna na 5 setupach 4p:
     - Wpływ na Win Share frakcji w 4P (Kanon: idealne 25.0%)
     - Wpływ na 4P Balance Score (czy karta stabilizuje kanon 4p, czy go destabilizuje)
     - Wpływ na tempo partii (Średnia Er) i wskaźnik deadlocków w 4P
  2. Klasyfikacja Kart w Kanonie 4P (Matryca 2D):
     - 👑 FILAR FRAKCJI W 4P (Core Keystone): Kluczowy motor napędowy wygranych frakcji
     - ⚓ KOTWICA KANONU 4P (Balance Anchor): Bezpiecznik chroniący przed dominacją frakcji
     - ⚠️ KARTA TOKSYCZNA W 4P (Disruptor): Karta, której usunięcie podnosi 4P Score
     - 💤 MARTWA KARTA W 4P (Dead Weight): Znikomy wpływ na grę 4-osobową
     - ⚖️ ZBALANSOWANE NARZĘDZIE 4P (Utility): Zdrowe, elastyczne narzędzie taktyczne
  3. Ablacja Mechanik Systemowych i Ścieżek Zwycięstwa w 4P:
     - Wpływ Kroniki Dziejów (Talia Czasu), Cooldownu Autodafé, Bramki Haka, Fragmentów itp.

Generuje raport w: playtesting/sim-reports/raport_uzytecznosci_i_wplywu_4p.md oraz archiwizuje w archive/{version}/.
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
    calculate_setup_score,
    color_score,
)

REPORTS_DIR = Path(__file__).resolve().parent.parent.parent / "playtesting" / "sim-reports"
OUTPUT_REPORT_PATH = REPORTS_DIR / "current" / "raport_uzytecznosci_i_wplywu_4p.md"

CANONICAL_4P_SETUPS = [
    "4p-core",
    "4p-no-cienie",
    "4p-no-kabala",
    "4p-no-korona",
    "4p-no-oficjum",
]

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


def _run_ablation_task_4p(task_args: tuple[str, str, dict, int, int, list[str]]) -> dict:
    """Simulates the 5 canonical 4P setups under a specific ablation / modification."""
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

    score_4p = round(sum(setup_scores.values()) / len(setup_scores), 1) if setup_scores else 0.0
    dt = round(time.time() - t0, 2)

    n_sum = len(summaries)
    eras_avg = sum(s.eras_avg for s in summaries) / n_sum
    deadlock_pct = (sum(s.eras_limit_pct for s in summaries) / n_sum) * 100.0
    poverty_pct = (sum(s.passes_forced_pct for s in summaries) / n_sum) * 100.0
    autodafe_avg = sum(s.autodafe_avg for s in summaries) / n_sum
    acc_avg = sum(s.accusations_avg for s in summaries) / n_sum

    faction_shares = {}
    for fname, wins in faction_wins.items():
        tot = faction_total_games.get(fname, 1)
        faction_shares[fname] = round((wins / tot) * 100.0, 1)

    return {
        "id": element_id,
        "name": element_name,
        "score_4p": score_4p,
        "setup_scores": setup_scores,
        "faction_shares": faction_shares,
        "eras_avg": eras_avg,
        "deadlock_pct": deadlock_pct,
        "poverty_pct": poverty_pct,
        "autodafe_avg": autodafe_avg,
        "acc_avg": acc_avg,
        "dt": dt,
    }


def classify_card_impact_4p(d_share: float, d_4p: float) -> tuple[str, str, str]:
    """Classifies card impact into 3x3 quadrant matrix for Kanon 4P."""
    if d_4p >= 1.2:
        if d_share > 0.8:
            return "TOXIC_CARRIER", "⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver)", "DISRUPTOR"
        elif d_share < -0.8:
            return "TOXIC_BRAKE", "⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm)", "DISRUPTOR"
        else:
            return "TOXIC_NOISE", "⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor)", "DISRUPTOR"

    if d_4p <= -2.0 or d_share >= 2.5:
        if d_share >= 2.5:
            return "PILLAR", "👑 FILAR KANONU (Core Keystone)", "STABILIZER"
        elif d_share <= -2.5:
            return "SHIELD", "🛡️ TARCZA DEFENSYWNA (Faction Shield)", "STABILIZER"
        else:
            return "ANCHOR", "⚓ KOTWICA KANONU (Balance Anchor)", "STABILIZER"

    if abs(d_share) <= 0.4 and abs(d_4p) <= 0.4:
        return "DEAD_WEIGHT", "💤 KARTA NISKIEGO WPŁYWU (Passive)", "DEAD_WEIGHT"

    if d_share >= 1.0:
        return "ENGINE", "⚡ MOTOR FRAKCJI (Offensive Engine)", "BALANCED"
    elif d_share <= -1.0:
        return "BRAKE", "🛑 HAMULEC FRAKCJI (Control Tool)", "BALANCED"
    else:
        return "UTILITY", "⚖️ ZBALANSOWANE NARZĘDZIE (Utility)", "BALANCED"


def run_full_ablation_audit_4p(games_per_setup: int = 5000, seed: int = 42, workers: int = 10) -> Path:
    """Executes the complete 4P ablation study across all 50 faction cards, time deck, and system mechanics."""
    t_start = time.time()
    setups = CANONICAL_4P_SETUPS
    all_cards = load_all_cards()

    print("═══════════════════════════════════════════════════════════════════════")
    print("   INQUISITIO-1492 — BADANIE UŻYTECZNOŚCI I WPŁYWU W KANONIE 4P        ")
    print("   Analiza ablacyjna (Leave-One-Out) dla 50 kart i mechanik w 4P       ")
    print("═══════════════════════════════════════════════════════════════════════")
    print(f"Bieżąca wersja:            {CONFIG.version}")
    print(f"Kanon Setupy:              {', '.join(setups)}")
    print(f"Wielkość próby:            {games_per_setup} gier/setup × {len(setups)} setupów 4P ({games_per_setup * len(setups)} gier per wariant)")
    print(f"Liczba kart do zbadania:   50 kart frakcji + 8 kart czasu + 8 podsystemów")
    print(f"Wątki procesora:           {workers}")
    print("═══════════════════════════════════════════════════════════════════════\n")

    # 1. Baseline 4P Measurement
    print(f"🔍 [1/4] POMIAR BAZOWY KANONU 4P (Wszystkie karty aktywne)...")
    base_task = ("BASE_4P", "Kanon 4P — Wszystkie Elementy Aktywne", {}, games_per_setup, seed, setups)
    base_res = _run_ablation_task_4p(base_task)

    print(f"   🎯 Wynik Kanonu 4P Score: {color_score(base_res['score_4p'], bold=True)} pkt")
    for sname, sc in sorted(base_res["setup_scores"].items()):
        print(f"      • `{sname}`: {color_score(sc, bold=True)} pkt")
    print(f"   📊 Udziały Frakcji w 4P (Kanon: idealne 25.0%):")
    for fname, sh in sorted(base_res["faction_shares"].items()):
        print(f"      • {fname:<4s}: {sh:5.1f}%")
    print(f"   ⏱️ Średnia Er: {base_res['eras_avg']:.2f} | Deadlocks: {base_res['deadlock_pct']:.1f}% | Pas Biedy: {base_res['poverty_pct']:.1f}%\n")

    # 2. Build Card Ablation Tasks (50 faction cards)
    card_tasks = []
    card_meta = {}
    for cid, card in sorted(all_cards.items()):
        pref = cid.split("-")[0]
        if pref not in PREFIX_TO_FACTION_ID:
            continue
        fname = FACTION_FULL_NAMES.get(pref, pref)
        card_name = card.name
        card_tasks.append((
            f"ABLATION_{cid.upper()}",
            f"Brak karty {cid} ({card_name})",
            {"disabled_cards": [cid]},
            games_per_setup,
            seed,
            setups,
        ))
        card_meta[f"ABLATION_{cid.upper()}"] = {
            "id": cid,
            "name": card_name,
            "faction_code": pref,
            "faction_name": fname,
            "cost": card.cost,
            "heresy": card.heresy,
            "type": card.type,
            "layer": card.layer,
        }

    # 3. Build Time Deck Ablation Tasks (8 cards)
    time_cards = [
        ("tc-01", "Kres Średniowiecza"),
        ("tc-02", "Płonący Stos"),
        ("tc-03", "Królewski Podatek"),
        ("tc-04", "Spisek w Cieniu"),
        ("tc-05", "Złoty Wiek"),
        ("tc-06", "Czystka w Mieście"),
        ("tc-07", "Druga Szansa"),
        ("tc-08", "Zaćmienie Słońca"),
    ]
    time_tasks = []
    for t_id, t_name in time_cards:
        time_tasks.append((
            f"TIME_{t_id.upper()}",
            f"Brak wydarzenia {t_id} ({t_name})",
            {"disabled_cards": [t_id]},
            games_per_setup,
            seed,
            setups,
        ))

    # 4. Build System & Victory Path Ablation Tasks
    sys_tasks = [
        ("SYS_NO_TIME_DECK", "Wyłączona Kronika Dziejów (Talia Czasu)", {"no_time_deck": True}, games_per_setup, seed, setups),
        ("SYS_AUTODAFE_CD_2", "Autodafé Cooldown = 2 Ery (Agresywna czystka)", {"autodafe_cooldown": 2}, games_per_setup, seed, setups),
        ("SYS_AUTODAFE_CD_4", "Autodafé Cooldown = 4 Ery (Rzadka czystka)", {"autodafe_cooldown": 4}, games_per_setup, seed, setups),
        ("VP_SO_STACKS_REQ_PLUS2", "Święte Oficjum: Wymóg 6 Stosów (Zamiast 4)", {"so_stacks_offset": 2}, games_per_setup, seed, setups),
        ("VP_SO_CONDEMNS_PLUS2", "Święte Oficjum: Wymóg 4 Skazań (Zamiast 2)", {"so_condemns_offset": 2}, games_per_setup, seed, setups),
        ("VP_CAA_RELICS_PLUS2", "Cienie: Wymóg 4 Relikwii (Zamiast 2)", {"caa_relics_offset": 2}, games_per_setup, seed, setups),
        ("VP_CAA_LATE_ERA", "Cienie: Wymóg Ery 8 (Zamiast 5)", {"caa_era_offset": 3}, games_per_setup, seed, setups),
        ("VP_KB_DECREES_PLUS1", "Korona: Wymóg 3 Dekretów (Zamiast 2)", {"kb_decrees_offset": 1}, games_per_setup, seed, setups),
        ("VP_KT_FRAGS_PLUS1", "Kabała: Wymóg 4 Fragmentów (Zamiast 3)", {"kt_frags_offset": 1}, games_per_setup, seed, setups),
    ]

    all_tasks = card_tasks + time_tasks + sys_tasks
    total_tasks = len(all_tasks)

    print(f"⏳ [2/4] URUCHAMIAM {total_tasks} ZADAŃ ABLACYJNYCH DLA KANONU 4P...")
    results_map = {}

    t_pool = time.time()
    with ProcessPoolExecutor(max_workers=workers) as executor:
        from concurrent.futures import as_completed
        future_to_id = {executor.submit(_run_ablation_task_4p, t): t[0] for t in all_tasks}

        for idx, future in enumerate(as_completed(future_to_id), 1):
            res = future.result()
            results_map[res["id"]] = res

            elapsed = time.time() - t_pool
            rate = idx / elapsed if elapsed > 0 else 0
            eta_s = (total_tasks - idx) / rate if rate > 0 else 0
            eta_str = f"{int(eta_s // 60)}m {int(eta_s % 60):02d}s" if eta_s >= 60 else f"{int(eta_s)}s"

            sys.stdout.write(f"\r⏳ [Ablacja 4P] [{idx:3d}/{total_tasks:3d}] ({idx*100.0/total_tasks:5.1f}%) | {rate:4.1f} zad/s | ETA: {eta_str:<8s} | Ostatni: {res['id'][:24]:<24s}  ")
            sys.stdout.flush()

    sys.stdout.write(f"\n   ✔ Ukończono wszystkie {total_tasks} zadań ablacyjnych 4P w {round(time.time() - t_pool, 1)}s.\n\n")

    # 5. Process & Classify Card Results
    print("🔬 [3/4] ANALIZUJĘ I KLASYFIKUJĘ KARTY W MATRYCY 3x3 DLA KANONU 4P...")
    analyzed_cards = []

    for task in card_tasks:
        t_id = task[0]
        res = results_map[t_id]
        meta = card_meta[t_id]
        pref = meta["faction_code"]
        fid_obj = PREFIX_TO_FACTION_ID[pref]
        f_short = FACTION_NAMES[fid_obj]

        base_f_share = base_res["faction_shares"].get(f_short, 25.0)
        ablated_f_share = res["faction_shares"].get(f_short, 25.0)

        # d_share > 0 means removing card decreased winrate (card was driving wins)
        d_share = round(base_f_share - ablated_f_share, 1)

        # d_4p > 0 means removing card increased 4P score (card was destabilizing 4P)
        d_4p = round(res["score_4p"] - base_res["score_4p"], 1)

        sub_id, role_name, group_id = classify_card_impact_4p(d_share, d_4p)

        analyzed_cards.append({
            "id": meta["id"],
            "name": meta["name"],
            "faction_code": pref,
            "faction_name": meta["faction_name"],
            "f_short": f_short,
            "cost": meta["cost"],
            "heresy": meta["heresy"],
            "type": meta["type"],
            "layer": meta["layer"],
            "base_share": base_f_share,
            "ablated_share": ablated_f_share,
            "d_share": d_share,
            "score_4p": res["score_4p"],
            "d_4p": d_4p,
            "sub_id": sub_id,
            "role_name": role_name,
            "group_id": group_id,
            "eras_avg": res["eras_avg"],
            "deadlock_pct": res["deadlock_pct"],
            "poverty_pct": res["poverty_pct"],
        })

    # Sort cards by faction, then layer/cost
    analyzed_cards.sort(key=lambda c: (c["faction_code"], c["layer"], c["cost"]))

    # 6. Process Time Cards
    analyzed_time_cards = []
    for t_id, t_name in time_cards:
        t_key = f"TIME_{t_id.upper()}"
        res = results_map[t_key]
        d_4p = round(res["score_4p"] - base_res["score_4p"], 1)
        status = "🟢 Stabilizator tempa" if d_4p <= -1.0 else ("⚠️ Spowalniacz" if d_4p >= 1.0 else "⚖️ Neutralna Kronika")
        analyzed_time_cards.append({
            "id": t_id,
            "name": t_name,
            "score_4p": res["score_4p"],
            "d_4p": d_4p,
            "eras_avg": res["eras_avg"],
            "deadlock_pct": res["deadlock_pct"],
            "status": status,
        })

    # 7. Process System Tasks
    sys_results = []
    sys_categories = {
        "SYS_NO_AUTODAFE": "Globalne Podsystemy",
        "SYS_NO_TRIBUNAL": "Globalne Podsystemy",
        "SYS_NO_TIME_DECK": "Globalne Podsystemy",
        "SYS_AUTODAFE_CD_2": "Globalne Podsystemy",
        "SYS_AUTODAFE_CD_4": "Globalne Podsystemy",
        "VP_SO_NO_STACKS": "Ścieżki Zwycięstwa",
        "VP_SO_NO_CONDEMNS": "Ścieżki Zwycięstwa",
        "VP_CAA_NO_MARIONETTE": "Ścieżki Zwycięstwa",
        "VP_CAA_NO_PATH": "Ścieżki Zwycięstwa",
        "VP_KB_NO_HOOKS_WIN": "Ścieżki Zwycięstwa",
    }
    for t in sys_tasks:
        s_id = t[0]
        s_name = t[1]
        res = results_map[s_id]
        sys_results.append({
            "id": s_id,
            "name": s_name,
            "score_4p": res["score_4p"],
            "setup_scores": res["setup_scores"],
            "faction_shares": res["faction_shares"],
            "eras_avg": res["eras_avg"],
            "deadlock_pct": res["deadlock_pct"],
            "poverty_pct": res["poverty_pct"],
        })

    # 8. Build Comprehensive Markdown Report
    print("📝 [4/4] GENERUJĘ PEŁNY RAPORT UŻYTECZNOŚCI I WPŁYWU DLA KANONU 4P...")

    lines = [
        f"# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja {CONFIG.version}",
        "",
        f"**Wersja Gry:** `{CONFIG.version}` | **Data Badania:** {datetime.now().strftime('%Y-%m-%d %H:%M')} | **Próba:** {games_per_setup} gier/setup ({games_per_setup * len(setups)} gier na wariant) | **Ziarno:** {seed}",
        f"**Wynik Bazowy Kanonu 4P:** {color_score(base_res['score_4p'], bold=True)} pkt | **Średnia Długość Partii:** `{base_res['eras_avg']:.2f} Er` | **Deadlocki:** `{base_res['deadlock_pct']:.1f}%` | **Pas Biedy:** `{base_res['poverty_pct']:.1f}%`",
        "",
        "---",
        "",
        "## 1. 🗺️ Podsumowanie Ekosystemu Kanonu 4P (Matryca Wpływu Kart 3x3)",
        "",
        "Rozkład wszystkich 50 kart frakcyjnych w matrycy **Wpływ na Frakcję ($\\Delta \\text{Share}$)** vs **Wpływ na Kanon 4P ($\\Delta \\text{4P Score}$)**:",
        "",
        "| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |",
        "| :--- | :---: | :---: | :--- | :--- |",
    ]

    group_counts = {
        "STABILIZER": len([c for c in analyzed_cards if c["group_id"] == "STABILIZER"]),
        "DISRUPTOR": len([c for c in analyzed_cards if c["group_id"] == "DISRUPTOR"]),
        "DEAD_WEIGHT": len([c for c in analyzed_cards if c["group_id"] == "DEAD_WEIGHT"]),
        "BALANCED": len([c for c in analyzed_cards if c["group_id"] == "BALANCED"]),
    }

    lines.extend([
        f"| 👑 / ⚓ **Filar / Kotwica Kanonu** | **{group_counts['STABILIZER']}** | {group_counts['STABILIZER']*2}% | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |",
        f"| ⚖️ **Zbalansowane Narzędzie** | **{group_counts['BALANCED']}** | {group_counts['BALANCED']*2}% | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Optymalne** |",
        f"| 💤 **Karta Pasywna (Dead Weight)** | **{group_counts['DEAD_WEIGHT']}** | {group_counts['DEAD_WEIGHT']*2}% | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia** |",
        f"| ⚠️ **Karta Destabilizująca (Disruptor)** | **{group_counts['DISRUPTOR']}** | {group_counts['DISRUPTOR']*2}% | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |",
        "",
        "---",
        "",
        "## 2. 🃏 Warstwa I — Szczegółowa Analiza 50 Kart Frakcji w Kanonie 4P",
        "",
        "### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)",
        "Karty, których brak powoduje spadek wyniku Kanonu 4P o $\\ge 4.0$ pkt lub załamanie winrate frakcji o $\\ge 4.0\\%$:",
        "",
        "| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\\Delta$ Frakcji | 4P Score po Wyłączeniu |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: |",
    ])

    stabilizers = sorted([c for c in analyzed_cards if c["group_id"] == "STABILIZER"], key=lambda x: x["d_4p"])
    for c in stabilizers:
        ds_sign = f"-{c['d_share']:.1f}%" if c['d_share'] > 0 else f"+{abs(c['d_share']):.1f}%"
        lines.append(
            f"| `{c['id']}` **{c['name']}** | {c['faction_name']} | {c['cost']}zł / {c['heresy']}☣ | "
            f"{c['role_name']} | {c['base_share']:.1f}% → **{c['ablated_share']:.1f}%** | "
            f"**`{ds_sign}`** | {base_res['score_4p']:.1f} → **{c['score_4p']:.1f} pkt** (`{c['d_4p']:.1f}`) |"
        )

    lines.extend([
        "",
        "### 2.2. ⚠️ Karty Destabilizujące Kanon 4P (Disruptors)",
        "Karty, których wyłączenie podnosi 4P Score ($\\Delta \\text{4P} \\ge +1.5$ pkt):",
        "",
        "| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\\Delta$ Frakcji | 4P Score po Wyłączeniu |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: |",
    ])

    disruptors = sorted([c for c in analyzed_cards if c["group_id"] == "DISRUPTOR"], key=lambda x: x["d_4p"], reverse=True)
    if not disruptors:
        lines.append("| *Brak kart destabilizujących* | - | - | - | - | - | - |")
    for c in disruptors:
        ds_sign = f"-{c['d_share']:.1f}%" if c['d_share'] > 0 else f"+{abs(c['d_share']):.1f}%"
        lines.append(
            f"| `{c['id']}` **{c['name']}** | {c['faction_name']} | {c['cost']}zł / {c['heresy']}☣ | "
            f"{c['role_name']} | {c['base_share']:.1f}% → **{c['ablated_share']:.1f}%** | "
            f"`{ds_sign}` | {base_res['score_4p']:.1f} → **{c['score_4p']:.1f} pkt** (`{c['d_4p']:+.1f}`) |"
        )

    lines.extend([
        "",
        "### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich 50 Kart Frakcji w Kanonie 4P",
        "",
        "| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Faction Win Share 4P | $\\Delta$ Frakcji | 4P Score | $\\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |",
        "| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |",
    ])

    for c in analyzed_cards:
        ds_sign = f"-{c['d_share']:.1f}%" if c['d_share'] > 0 else f"+{abs(c['d_share']):.1f}%"
        d4_sign = f"+{c['d_4p']:.1f}" if c['d_4p'] > 0 else f"{c['d_4p']:.1f}"
        lines.append(
            f"| `{c['id']}` | **{c['name']}** | {c['faction_name']} | {c['cost']} | {c['heresy']} | "
            f"{c['base_share']:.1f}% → {c['ablated_share']:.1f}% | `{ds_sign}` | "
            f"{c['score_4p']:.1f} | `{d4_sign}` | {c['eras_avg']:.2f} | {c['deadlock_pct']:.1f}% | {c['role_name']} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 3. ⏳ Warstwa II — Kronika Dziejów w 4P (Ablacja 8 Kart Wydarzeń Czasu)",
        "",
        "Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans w 4P:",
        "",
        "| ID | Karta Wydarzenia | 4P Score | $\\Delta$ 4P | Średnia Er | Deadlock % | Status Roli w Kronice |",
        "| :--- | :--- | :---: | :---: | :---: | :---: | :--- |",
    ])

    for tc in analyzed_time_cards:
        d4_str = f"+{tc['d_4p']:.1f}" if tc['d_4p'] > 0 else f"{tc['d_4p']:.1f}"
        lines.append(
            f"| `{tc['id']}` | **{tc['name']}** | {score_pair(base_res['score_4p'], tc['score_4p'], colored=True)} | "
            f"`{d4_str} pkt` | {tc['eras_avg']:.2f} Er | {tc['deadlock_pct']:.1f}% | {tc['status']} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 4. ⚙️ Warstwa III — Globalne Mechaniki i Parametry Silnika w 4P",
        "",
        "Badanie odporności Kanonu 4P na wyłączenie lub skrajne przestawienie bazowych parametrów silnika:",
        "",
        "| Badany Podsystem / Parametr | 4P Score | $\\Delta$ 4P | Średnia Er | Deadlocks % | Pas Biedy % | Diagnoza i Wpływ na Silnik |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :--- |",
    ])

    global_sys_results = [r for r in sys_results if sys_categories.get(r["id"]) == "Globalne Podsystemy"]
    for r in global_sys_results:
        d4 = r["score_4p"] - base_res["score_4p"]
        d4_str = f"+{d4:.1f}" if d4 > 0 else f"{d4:.1f}"
        if d4 >= 1.5:
            diag = "🟢 Zysk balansu — mechanika w obecnej formie obciąża Kanon 4P"
        elif d4 <= -15.0:
            diag = "🔴 Katastrofa ekosystemu — filar bezwzględnie krytyczny dla Kanonu 4P"
        elif d4 <= -5.0:
            diag = "🟠 Poważna destabilizacja — silnik traci płynność lub różnorodność w 4P"
        else:
            diag = "⚪ Wpływ neutralny / mechanika stabilna"

        lines.append(
            f"| **{r['name']}** | {score_pair(base_res['score_4p'], r['score_4p'], colored=True)} | "
            f"`{d4_str} pkt` | {r['eras_avg']:.2f} Er | {r['deadlock_pct']:.1f}% | {r['poverty_pct']:.1f}% | {diag} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 5. ⚔️ Warstwa IV — Asymetryczne Ścieżki Zwycięstwa w 4P (Victory Paths)",
        "",
        "Badanie krytyczności i elastyczności unikalnych bramek zwycięstwa dla każdej frakcji w Kanonie 4P:",
        "",
        "| Badana Ścieżka / Bramka Wygranej | 4P Score | $\\Delta$ 4P | Średnia Er | Deadlocks % | Pas Biedy % | Diagnoza Ścieżki Zwycięstwa |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :--- |",
    ])

    vp_results = [r for r in sys_results if sys_categories.get(r["id"]) == "Ścieżki Zwycięstwa"]
    for r in vp_results:
        d4 = r["score_4p"] - base_res["score_4p"]
        d4_str = f"+{d4:.1f}" if d4 > 0 else f"{d4:.1f}"
        if d4 >= 1.5:
            diag = "🟢 Zysk balansu — ścieżka w obecnej formie zaburza równowagę w 4P"
        elif d4 <= -15.0:
            diag = "🔴 Krytyczna ścieżka — frakcja nie posiada alternatywnego motoru w 4P"
        elif d4 <= -5.0:
            diag = "🟠 Istotna ścieżka — jej brak zauważalnie ubożeje przestrzeń decyzyjną"
        else:
            diag = "⚪ Ścieżka alternatywna / opcjonalna"

        lines.append(
            f"| **{r['name']}** | {score_pair(base_res['score_4p'], r['score_4p'], colored=True)} | "
            f"`{d4_str} pkt` | {r['eras_avg']:.2f} Er | {r['deadlock_pct']:.1f}% | {r['poverty_pct']:.1f}% | {diag} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 6. 👥 Warstwa V — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji",
        "",
        "Zestawienie stabilności 5 wariantów 4-osobowych w Kanonie 4P:",
        "",
        "| Nieobecna Frakcja | Setup Testowy | 4P Score Setupu | Diagnoza Wpływu Braku Frakcji na Stół 4P |",
        "| :--- | :--- | :---: | :--- |",
        f"| **Bez Gildii Cieni** | `4p-core` | **`{base_res['setup_scores'].get('4p-core', 0.0):.1f} pkt`** | Stół klasyczny (czysta walka religijno-polityczna) |",
        f"| **Bez Kabały z Toledo** | `4p-no-kabala` | **`{base_res['setup_scores'].get('4p-no-kabala', 0.0):.1f} pkt`** | Brak presji okultystycznej i manipulacji czasem |",
        f"| **Bez Korony i Borgiów** | `4p-no-korona` | **`{base_res['setup_scores'].get('4p-no-korona', 0.0):.1f} pkt`** | Brak presji podatkowej i aresztów królewskich |",
        f"| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`{base_res['setup_scores'].get('4p-no-cienie', 0.0):.1f} pkt`** | Brak szlaków morskich i ucieczek podziemiami |",
        f"| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`{base_res['setup_scores'].get('4p-no-oficjum', 0.0):.1f} pkt`** | Brak presji stosów i bezpośredniego Inkwizytora |",
    ])

    report_path, arch_path = save_and_archive_report(lines, "raport_uzytecznosci_i_wplywu_4p.md")
    print(f"\n✅ 5-WARSTWOWY RAPORT KANONU 4P WYGENEROWANY POMYŚLNIE!")
    print(f"   Raport:    {report_path}")
    print(f"   Archiwum:  {arch_path}\n")
    return report_path


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 Feature & Card Impact Audit for Kanon 4P (Ablation Study 4P)")
    parser.add_argument("--games", type=int, default=5000, help="Liczba gier na setup (domyślnie: 5000, min. 1000)")
    parser.add_argument("--workers", type=int, default=min(os.cpu_count() or 4, 10), help="Liczba wątków równoległych")
    parser.add_argument("--seed", type=int, default=42, help="Ziarno losowe (CRN)")

    args = parser.parse_args()
    if args.games < 1000:
        print("⚠️ Podwyższam próbę do wymaganego minimum 1000 gier.")
        args.games = 1000

    run_full_ablation_audit_4p(games_per_setup=args.games, seed=args.seed, workers=args.workers)


if __name__ == "__main__":
    main()
