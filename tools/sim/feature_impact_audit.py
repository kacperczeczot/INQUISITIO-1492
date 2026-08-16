#!/usr/bin/env python3
"""INQUISITIO-1492 — BADANIE UŻYTECZNOŚCI I WPŁYWU ELEMENTÓW (Ablation & Impact Audit).

Narzędzie analityczne do badania wkładu każdego pojedynczego elementu gry w balans:
  1. Ablacja Kart (Per-Card Ablation): Wyłącza każdą z 50 kart z osobna i bada:
     - Wpływ na Win Share frakcji (czy frakcja bez niej wygrywa, czy przegrywa)
     - Wpływ na Global Balance Score (czy karta destabilizuje stół, czy stabilizuje)
     - Wpływ na tempo partii (Średnia Er) i wskaźnik deadlocków
  2. Klasyfikacja Kart (Matryca 2D):
     - 👑 FILAR FRAKCJI (Core Keystone): Kluczowy motor napędowy wygranych frakcji
     - ⚓ KOTWICA STOŁU (Balance Anchor): Bezpiecznik chroniący przed dominacją frakcji
     - ⚠️ KARTA TOKSYCZNA (Disruptor): Karta, której usunięcie poprawia balans stołu
     - 💤 MARTWA KARTA (Dead Weight): Zerowy wpływ na grę (kandydat do wzmocnienia/reworku)
     - ⚖️ ZBALANSOWANE NARZĘDZIE (Utility): Zdrowe, elastyczne narzędzie taktyczne
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
OUTPUT_REPORT_PATH = REPORTS_DIR / "current" / "raport_uzytecznosci_i_wplywu.md"

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
) -> dict[str, str]:
    """Classifies a card's strategic role using a symmetrical 3x3 matrix.
    
    Axes:
      1. Global Ecosystem Axis (Δ Global Score = ablated_score - base_score):
         - DESTABILIZER (Δ ≥ +1.0 pkt): Card presence harms table balance; removal improves it.
         - BALANCED     (-5.0 < Δ < +1.0 pkt): Card has moderate/healthy impact on table balance.
         - CRITICAL     (Δ ≤ -5.0 pkt): Card is foundational; removal collapses table balance.
         
      2. Local Faction Axis (Δ Faction Share = base_share - ablated_share):
         - BRAKE        (Δ ≤ -2.0%): Defensive/diluting card; removal increases faction winrate.
         - TACTICAL     (-2.0% < Δ < +2.5%): Neutral/situational tactical tool.
         - KEYSTONE     (Δ ≥ +2.5%): Victory engine; removal drops faction winrate.
    """
    # 1. Faction Axis (Subgroup)
    if delta_faction_share <= -2.0:
        sub_id = "BRAKE"
        sub_tag = "🛑 Hamulec Tempa"
    elif delta_faction_share >= 2.5:
        sub_id = "KEYSTONE"
        sub_tag = "👑 Motor Wygranych"
    else:
        sub_id = "TACTICAL"
        sub_tag = "⚪ Narzędzie Taktyczne"

    # 2. Ecosystem Axis (Main Group)
    if delta_global_score >= 1.0:
        group_id = "DESTABILIZER"
        group_name = "⚠️ I. Destabilizatory Stołu"
        if sub_id == "BRAKE":
            role_name = "⚠️🛑 Toksyczny Balast"
        elif sub_id == "KEYSTONE":
            role_name = "⚠️👑 Toksyczny Dominator"
        else:
            role_name = "⚠️⚪ Toksyczny Zgrzyt"
    elif delta_global_score <= -5.0:
        group_id = "CRITICAL"
        group_name = "⚓ III. Krytyczne dla Balansu Stołu"
        if sub_id == "BRAKE":
            role_name = "⚓🛑 Kotwica Stołu (Bezpiecznik)"
        elif sub_id == "KEYSTONE":
            role_name = "⚓👑 Filar Frakcji i Stołu"
        else:
            role_name = "⚓⚪ Zwornik Różnorodności"
    else:
        group_id = "BALANCED"
        group_name = "⚖️ II. Neutralne / Zbalansowane"
        if sub_id == "BRAKE":
            role_name = "⚖️🛑 Zdrowy Hamulec"
        elif sub_id == "KEYSTONE":
            role_name = "⚖️👑 Lokalny Silnik Frakcji"
        else:
            role_name = "⚖️⚪ Zrównoważone Narzędzie"

    return {
        "group_id": group_id,
        "group_name": group_name,
        "sub_id": sub_id,
        "sub_tag": sub_tag,
        "role_name": role_name,
    }


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

    # 2. PER-CARD ABLATION TASKS (FACTION CARDS)
    print(f"🧬 [2/4] Generowanie i badanie ablacyjne 50 kart frakcji...")
    card_tasks = []
    time_card_tasks = []
    
    for cid, c in sorted(cards.items()):
        if cid.startswith("time-"):
            task_name = f"BEZ {cid.upper()} ({c.name})"
            sys_overrides = {"disabled_cards": [cid]}
            time_card_tasks.append((cid, task_name, sys_overrides, games_per_setup, seed, setups))
        else:
            task_name = f"BEZ {cid.upper()} ({c.name})"
            sys_overrides = {"disabled_cards": [cid]}
            card_tasks.append((cid, task_name, sys_overrides, games_per_setup, seed, setups))

    with ProcessPoolExecutor(max_workers=min(workers, len(card_tasks))) as executor:
        card_results = list(executor.map(_run_ablation_task, card_tasks))

    print(f"   ✔ Zbadano ablacyjnie {len(card_results)} kart frakcji.")

    # 3. TIME DECK PER-EVENT ABLATION TASKS
    print(f"⏳ [3/4] Generowanie i badanie ablacyjne {len(time_card_tasks)} kart Talii Czasu (Kroniki Dziejów)...")
    with ProcessPoolExecutor(max_workers=min(workers, len(time_card_tasks))) as executor:
        time_card_results = list(executor.map(_run_ablation_task, time_card_tasks))

    print(f"   ✔ Zbadano ablacyjnie {len(time_card_results)} kart Talii Czasu.\n")

    # 4. SYSTEM MECHANICS & VICTORY PATH ABLATION (Turning complete subsystems ON/OFF)
    print("⚙️ [4/4] Badanie czysto ablacyjne podsystemów i ścieżek zwycięstwa (Ablation Scenarios)...")

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

    # 5. ANALYZE AND FORMAT REPORT
    print("📄 Generowanie i formatowanie 5-warstwowego raportu użyteczności...")
    total_elapsed = round(time.time() - t_start, 1)

    analyzed_cards = []
    for r in card_results:
        cid = r["id"]
        c = cards.get(cid)
        pref = cid.split("-")[0].lower()
        fid = PREFIX_TO_FACTION_ID.get(pref)
        fname = FACTION_NAMES.get(fid, pref.upper()) if fid else pref.upper()
        
        base_share = base_res["faction_win_shares"].get(fname, 0.0)
        ablated_share = r["faction_win_shares"].get(fname, 0.0)
        
        # Delta: positive means faction LOST win share without this card -> card contributes to win
        d_share = round(base_share - ablated_share, 2)
        d_global = round(r["global_score"] - base_res["global_score"], 2)
        d_eras = round(r["eras_avg"] - base_res["eras_avg"], 2)
        
        cinfo = classify_card_impact(d_share, d_global, cid)

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
            "group_id": cinfo["group_id"],
            "group_name": cinfo["group_name"],
            "sub_id": cinfo["sub_id"],
            "sub_tag": cinfo["sub_tag"],
            "role_name": cinfo["role_name"],
        })

    # Analyzed Time Cards
    analyzed_time_cards = []
    for r in time_card_results:
        cid = r["id"]
        c = cards.get(cid)
        d_global = round(r["global_score"] - base_res["global_score"], 2)
        d_eras = round(r["eras_avg"] - base_res["eras_avg"], 2)
        
        if d_global >= 1.0:
            t_status = "⚠️ Destabilizuje (usunięcie poprawia stół)"
        elif d_global <= -3.0:
            t_status = "⚓ Filar stabilności (niezbędna w Kronice)"
        else:
            t_status = "⚖️ Zrównoważone wydarzenie"

        analyzed_time_cards.append({
            "id": cid,
            "name": c.name if c else cid,
            "effect": c.effect if c else "",
            "global_score": r["global_score"],
            "d_global": d_global,
            "eras_avg": r["eras_avg"],
            "d_eras": d_eras,
            "deadlock_pct": r["deadlock_pct"],
            "status": t_status,
        })

    # Group counts for 3x3 Matrix
    matrix_counts: dict[tuple[str, str], int] = {}
    for g_id in ["DESTABILIZER", "BALANCED", "CRITICAL"]:
        for s_id in ["BRAKE", "TACTICAL", "KEYSTONE"]:
            matrix_counts[(g_id, s_id)] = sum(1 for c in analyzed_cards if c["group_id"] == g_id and c["sub_id"] == s_id)

    # Topology Analysis from Baseline
    setups_3p = [s for s in setups if s.startswith("3p-")]
    setups_4p = [s for s in setups if s.startswith("4p-")]
    setups_5p = [s for s in setups if s.startswith("5p-")]

    score_3p = sum(base_res["setup_scores"][s] for s in setups_3p) / len(setups_3p) if setups_3p else 0
    score_4p = sum(base_res["setup_scores"][s] for s in setups_4p) / len(setups_4p) if setups_4p else 0
    score_5p = sum(base_res["setup_scores"][s] for s in setups_5p) / len(setups_5p) if setups_5p else 0

    today_str = datetime.now().strftime("%Y-%m-%d %H:%M")

    lines = [
        f"# Raport Użyteczności i Wpływu Elementów Gry (5-Warstwowy Audyt Ablacyjny) — Wersja: {CONFIG.version}",
        "",
        f"**Wersja Gry:** `{CONFIG.version}` | **Data:** {today_str} | **Próba:** {games_per_setup} gier/setup ({games_per_setup * 16} gier/test) | **Czas Analizy:** {total_elapsed}s",
        "",
        "Kompleksowy audyt badania wkładu poszczególnych elementów gry w balans ekosystemu (**Leave-One-Out Feature Importance**).",
        "Analiza obejmuje 5 komplementarnych warstw architektury mechanicznej *INQUISITIO-1492*.",
        "",
        "---",
        "",
        "## 1. 🏛️ Architektura 5 Warstw Badania Ablacyjnego",
        "",
        "| Warstwa Architektury | Badany Zakres Elementów | Liczba Testów | Kluczowy Wskaźnik |",
        "| :--- | :--- | :---: | :--- |",
        "| **Warstwa I: Karty Frakcyjne** | 50 kart akcji, reakcji i permanentów (po 10 na frakcję) | `50` | Matryca 3x3 (Filar vs Kotwica vs Destabilizator) |",
        "| **Warstwa II: Kronika Dziejów** | 8 kart wydarzeń z Talii Czasu | `8` | Wpływ na tempo partii i stabilność metagry |",
        "| **Warstwa III: Mechaniki Silnika** | Inkwizytor, Autodafé, Limit ręki, Złoto startowe | `6` | Odporność rdzenia na skrajne modyfikatory |",
        "| **Warstwa IV: Ścieżki Zwycięstwa** | Bramki frakcyjne (Haki KB, Pasmo KT, Szlak CAA, Stosy SO) | `7` | Krytyczność asymetrycznych warunków wygranej |",
        "| **Warstwa V: Skalowanie Stołu** | Formaty 3-osobowe, 4-osobowe i 5-osobowe (16 setupów) | `16` | Symetria i brak dominacji przy różnej liczbie graczy |",
        "",
        "---",
        "",
        "## 2. 🃏 Warstwa I — Karty Frakcyjne (Symetryczna Matryca 3x3)",
        "",
        "Wszystkie 50 kart frakcji sklasyfikowano na przecięciu dwóch ortogonalnych osi:",
        "- **Oś Globalna (Stół):** Wpływ wyłączenia karty na ogólny stan balansu gry ($\\Delta \\text{Global Score}$).",
        "- **Oś Lokalna (Frakcja):** Wpływ wyłączenia karty na szanse zwycięstwa danej frakcji ($\\Delta \\text{Faction Share}$).",
        "",
        "| Grupa Ekosystemu \\ Profil Frakcji | 🛑 Hamulec Tempa (Δ ≤ -2.0%) | ⚪ Narzędzie Taktyczne (Neutralne) | 👑 Motor Wygranych (Δ ≥ +2.5%) | ŁĄCZNIE |",
        "| :--- | :---: | :---: | :---: | :---: |",
        f"| **⚠️ I. Destabilizatory Stołu** (Δ Global ≥ +1.0 pkt) | `{matrix_counts[('DESTABILIZER', 'BRAKE')]}` *(Toksyczny Balast)* | `{matrix_counts[('DESTABILIZER', 'TACTICAL')]}` *(Toksyczny Zgrzyt)* | `{matrix_counts[('DESTABILIZER', 'KEYSTONE')]}` *(Toksyczny Dominator)* | **`{sum(matrix_counts[('DESTABILIZER', s)] for s in ['BRAKE', 'TACTICAL', 'KEYSTONE'])}`** |",
        f"| **⚖️ II. Zbalansowane dla Stołu** (-5.0 < Δ < +1.0 pkt) | `{matrix_counts[('BALANCED', 'BRAKE')]}` *(Zdrowy Hamulec)* | `{matrix_counts[('BALANCED', 'TACTICAL')]}` *(Zrównoważone Narzędzie)* | `{matrix_counts[('BALANCED', 'KEYSTONE')]}` *(Lokalny Silnik)* | **`{sum(matrix_counts[('BALANCED', s)] for s in ['BRAKE', 'TACTICAL', 'KEYSTONE'])}`** |",
        f"| **⚓ III. Krytyczne dla Balansu** (Δ Global ≤ -5.0 pkt) | `{matrix_counts[('CRITICAL', 'BRAKE')]}` *(Kotwica Stołu)* | `{matrix_counts[('CRITICAL', 'TACTICAL')]}` *(Zwornik Różnorodności)* | `{matrix_counts[('CRITICAL', 'KEYSTONE')]}` *(Filar Frakcji i Stołu)* | **`{sum(matrix_counts[('CRITICAL', s)] for s in ['BRAKE', 'TACTICAL', 'KEYSTONE'])}`** |",
        f"| **ŁĄCZNIE** | **`{sum(matrix_counts[(g, 'BRAKE')] for g in ['DESTABILIZER', 'BALANCED', 'CRITICAL'])}`** | **`{sum(matrix_counts[(g, 'TACTICAL')] for g in ['DESTABILIZER', 'BALANCED', 'CRITICAL'])}`** | **`{sum(matrix_counts[(g, 'KEYSTONE')] for g in ['DESTABILIZER', 'BALANCED', 'CRITICAL'])}`** | **50 kart** |",
        "",
        "### 2.1. ⚠️ Destabilizatory Ekosystemu (Kandydaci do Osłabienia / Reworku)",
        "Karty, których wyłączenie **podnosi** ogólny wynik balansu gry ($\\Delta \\text{Global} \\ge +1.0$ pkt):",
        "",
        "| Karta | Frakcja | Koszt / Herezja | Podgrupa 3x3 | Global Score (Baza → Bez) | Zysk Balansu ($\\Delta$) | Win Share Frakcji |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: |",
    ]

    destab_cards = sorted([c for c in analyzed_cards if c["group_id"] == "DESTABILIZER"], key=lambda x: x["d_global"], reverse=True)
    if destab_cards:
        for c in destab_cards:
            lines.append(
                f"| `{c['id']}` **{c['name']}** | {c['faction_name']} | {c['cost']}zł / {c['heresy']}☣ | "
                f"{c['role_name']} | {base_res['global_score']:.1f} → **{c['global_score']:.1f} pkt** | "
                f"**`+{c['d_global']:.1f} pkt`** 🟢 | {c['base_share']:.1f}% → {c['ablated_share']:.1f}% (`{c['d_share']:+.1f}%`) |"
            )
    else:
        lines.append("| — | — | — | — | — | — | — |")
        lines.append("| *Brak kart destabilizujących ekosystem.* |")

    lines.extend([
        "",
        "### 2.2. ⚓ Karty Krytyczne dla Balansu Stołu (Filary i Kotwice)",
        "Karty, których wyłączenie **drastycznie załamuje** równowagę gry ($\\Delta \\text{Global} \\le -5.0$ pkt):",
        "",
        "| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 3x3 | Win Share Frakcji (Baza → Bez) | Wpływ na Frakcję ($\\Delta$) | Global Score po Wyłączeniu |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: |",
    ])

    crit_cards = sorted([c for c in analyzed_cards if c["group_id"] == "CRITICAL"], key=lambda x: (x["sub_id"] != "KEYSTONE", x["sub_id"] != "BRAKE", x["d_global"]))
    for c in crit_cards:
        if c["sub_id"] == "KEYSTONE":
            ds_fmt = f"**`-{c['d_share']:.1f}%`** 🔻"
        elif c["sub_id"] == "BRAKE":
            ds_fmt = f"**`+{abs(c['d_share']):.1f}%`** 🚀"
        else:
            ds_fmt = f"`{c['d_share']:+.1f}%`"

        lines.append(
            f"| `{c['id']}` **{c['name']}** | {c['faction_name']} | {c['cost']}zł / {c['heresy']}☣ | "
            f"{c['role_name']} | {c['base_share']:.1f}% → **{c['ablated_share']:.1f}%** | "
            f"{ds_fmt} | {base_res['global_score']:.1f} → **{c['global_score']:.1f} pkt** (`{c['d_global']:.1f}`) |"
        )

    lines.extend([
        "",
        "### 2.3. ⚖️ Karty Zbalansowane i Narzędzia Taktyczne",
        "Karty o stabilnym, neutralnym wpływie na stół ($-5.0 < \\Delta \\text{Global} < +1.0$ pkt):",
        "",
        "| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 3x3 | Win Share Frakcji (Baza → Bez) | $\\Delta$ Frakcji | Global Score po Wyłączeniu |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: |",
    ])

    bal_cards = sorted([c for c in analyzed_cards if c["group_id"] == "BALANCED"], key=lambda x: abs(x["d_share"]), reverse=True)
    for c in bal_cards:
        lines.append(
            f"| `{c['id']}` **{c['name']}** | {c['faction_name']} | {c['cost']}zł / {c['heresy']}☣ | "
            f"{c['role_name']} | {c['base_share']:.1f}% → {c['ablated_share']:.1f}% | "
            f"`{c['d_share']:+.1f}%` | {c['global_score']:.1f} pkt (`{c['d_global']:+.1f}`) |"
        )

    lines.extend([
        "",
        "### 2.4. 📋 Pełny Wykaz Ablacji Wszystkich 50 Kart Frakcji",
        "",
        "| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Faction Win Share | $\\Delta$ Frakcji | Global Score | $\\Delta$ Global | Śr. Er | Deadlock % | Rola w Matrycy 3x3 |",
        "| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |",
    ])

    for c in analyzed_cards:
        ds_sign = f"-{c['d_share']:.1f}%" if c['d_share'] > 0 else f"+{abs(c['d_share']):.1f}%"
        dg_sign = f"+{c['d_global']:.1f}" if c['d_global'] > 0 else f"{c['d_global']:.1f}"
        lines.append(
            f"| `{c['id']}` | **{c['name']}** | {c['faction_name']} | {c['cost']} | {c['heresy']} | "
            f"{c['base_share']:.1f}% → {c['ablated_share']:.1f}% | `{ds_sign}` | "
            f"{c['global_score']:.1f} | `{dg_sign}` | {c['eras_avg']:.2f} | {c['deadlock_pct']:.1f}% | {c['role_name']} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 3. ⏳ Warstwa II — Kronika Dziejów (Ablacja 8 Kart Wydarzeń Czasu)",
        "",
        "Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans:",
        "",
        "| ID | Karta Wydarzenia | Global Score | $\\Delta$ Global | Średnia Er | Deadlock % | Status Roli w Kronice |",
        "| :--- | :--- | :---: | :---: | :---: | :---: | :--- |",
    ])

    for tc in analyzed_time_cards:
        dg_str = f"+{tc['d_global']:.1f}" if tc['d_global'] > 0 else f"{tc['d_global']:.1f}"
        lines.append(
            f"| `{tc['id']}` | **{tc['name']}** | {score_pair(base_res['global_score'], tc['global_score'], colored=True)} | "
            f"`{dg_str} pkt` | {tc['eras_avg']:.2f} Er | {tc['deadlock_pct']:.1f}% | {tc['status']} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 4. ⚙️ Warstwa III — Globalne Mechaniki i Parametry Silnika",
        "",
        "Badanie odporności gry na wyłączenie lub skrajne przestawienie bazowych parametrów silnika:",
        "",
        "| Badany Podsystem / Parametr | Global Score | $\\Delta$ Global | Średnia Er | Deadlocks % | Pas Biedy % | Diagnoza i Wpływ na Silnik |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :--- |",
    ])

    global_sys_results = [r for r in sys_results if sys_categories.get(r["id"]) == "Globalne Podsystemy"]
    for r in global_sys_results:
        dg = r["global_score"] - base_res["global_score"]
        dg_str = f"+{dg:.1f}" if dg > 0 else f"{dg:.1f}"
        if dg >= 1.0:
            diag = "🟢 Zysk balansu — mechanika w obecnej formie obciąża stół"
        elif dg <= -15.0:
            diag = "🔴 Katastrofa ekosystemu — filar bezwzględnie krytyczny dla gry"
        elif dg <= -5.0:
            diag = "🟠 Poważna destabilizacja — silnik traci płynność lub różnorodność"
        else:
            diag = "⚪ Wpływ neutralny / mechanika stabilna"

        lines.append(
            f"| **{r['name']}** | {score_pair(base_res['global_score'], r['global_score'], colored=True)} | "
            f"`{dg_str} pkt` | {r['eras_avg']:.2f} Er | {r['deadlock_pct']:.1f}% | {r['poverty_pct']:.1f}% | {diag} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 5. ⚔️ Warstwa IV — Asymetryczne Ścieżki Zwycięstwa (Victory Paths)",
        "",
        "Badanie krytyczności i elastyczności unikalnych bramek zwycięstwa (*Victory Gating*) dla każdej frakcji:",
        "",
        "| Badana Ścieżka / Bramka Wygranej | Global Score | $\\Delta$ Global | Średnia Er | Deadlocks % | Pas Biedy % | Diagnoza Ścieżki Zwycięstwa |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :--- |",
    ])

    vp_results = [r for r in sys_results if sys_categories.get(r["id"]) == "Ścieżki Zwycięstwa"]
    for r in vp_results:
        dg = r["global_score"] - base_res["global_score"]
        dg_str = f"+{dg:.1f}" if dg > 0 else f"{dg:.1f}"
        if dg >= 1.0:
            diag = "🟢 Zysk balansu — ścieżka w obecnej formie zaburza równowagę"
        elif dg <= -15.0:
            diag = "🔴 Krytyczna ścieżka — frakcja nie posiada alternatywnego motoru"
        elif dg <= -5.0:
            diag = "🟠 Istotna ścieżka — jej brak zauważalnie ubożeje przestrzeń decyzyjną"
        else:
            diag = "⚪ Ścieżka alternatywna / opcjonalna"

        lines.append(
            f"| **{r['name']}** | {score_pair(base_res['global_score'], r['global_score'], colored=True)} | "
            f"`{dg_str} pkt` | {r['eras_avg']:.2f} Er | {r['deadlock_pct']:.1f}% | {r['poverty_pct']:.1f}% | {diag} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 6. 👥 Warstwa V — Skalowalność i Odporność Topologii Stołu (3P / 4P / 5P)",
        "",
        "Zestawienie stabilności ekosystemu gry w zależności od formatu liczby graczy i obecności poszczególnych frakcji:",
        "",
        "### 6.1. Balans w Podziale na Formaty Liczby Graczy",
        "",
        "| Format Gry | Liczba Badanych Setupów | Średni Global Score | Średnia Długość (Er) | Stan Balansu Formatu |",
        "| :--- | :---: | :---: | :---: | :--- |",
        f"| **Format 3-osobowy (3P)** | 10 setupów | **`{score_3p:.1f} pkt`** | {base_res['eras_avg']:.2f} Er | {'🟢 Bardzo wysoki' if score_3p >= 90 else '🟡 Umiarkowany'} |",
        f"| **Format 4-osobowy (4P)** | 5 setupów | **`{score_4p:.1f} pkt`** | {base_res['eras_avg']:.2f} Er | {'🟢 Bardzo wysoki' if score_4p >= 90 else '🟡 Umiarkowany'} |",
        f"| **Format 5-osobowy (5P - Pełny Stół)** | 1 setup (`5p-full`) | **`{score_5p:.1f} pkt`** | {base_res['eras_avg']:.2f} Er | {'🟢 Bardzo wysoki' if score_5p >= 90 else '🟡 Umiarkowany'} |",
        "",
        "### 6.2. Odporność Stołu na Nieobecność Konkretnej Frakcji (Formaty 4P)",
        "",
        "| Nieobecna Frakcja | Setup Testowy | Global Score | Diagnoza Wpływu Braku Frakcji na Stół |",
        "| :--- | :--- | :---: | :--- |",
        f"| **Bez Gildii Cieni** | `4p-core` | **`{base_res['setup_scores'].get('4p-core', 0.0):.1f} pkt`** | Stół klasyczny (czysta walka religijno-polityczna) |",
        f"| **Bez Kabały z Toledo** | `4p-no-kabala` | **`{base_res['setup_scores'].get('4p-no-kabala', 0.0):.1f} pkt`** | Brak presji okultystycznej i manipulacji czasem |",
        f"| **Bez Korony i Borgiów** | `4p-no-korona` | **`{base_res['setup_scores'].get('4p-no-korona', 0.0):.1f} pkt`** | Brak presji podatkowej i aresztów królewskich |",
        f"| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`{base_res['setup_scores'].get('4p-no-cienie', 0.0):.1f} pkt`** | Brak szlaków morskich i ucieczek podziemiami |",
        f"| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`{base_res['setup_scores'].get('4p-no-oficjum', 0.0):.1f} pkt`** | Brak presji stosów i bezpośredniego Inkwizytora |",
        "",
        "---",
        "",
        "## 7. 📐 Metodologia Badania i Matryca Klasyfikacji 3x3",
        "",
        "Raport opiera się na **dwuwymiarowej przestrzeni metryk ablacyjnych (Leave-One-Out)**:",
        "",
        "1. **OŚ LOKALNA — Wpływ na Frakcję ($\\Delta \\text{Faction Share} = WS_{\\text{baza}} - WS_{\\text{bez\\_karty}}$):**",
        "   - Wartość dodatnia ($> 0$): Usunięcie karty osłabia frakcję $\\rightarrow$ Karta jest **motorem zwycięstwa (Filar)**.",
        "   - Wartość ujemna ($< 0$): Usunięcie karty podnosi winrate frakcji $\\rightarrow$ Karta jest **hamulcem tempa / kartą defensywną**.",
        "2. **OŚ GLOBALNA — Wpływ na Ekosystem ($\\Delta \\text{Global Score} = GS_{\\text{bez\\_karty}} - GS_{\\text{baza}}$):**",
        "   - Wartość dodatnia ($> 0$): Usunięcie karty poprawia balans stołu $\\rightarrow$ Karta była **toksyczna / destabilizująca**.",
        "   - Wartość ujemna ($< 0$): Usunięcie karty załamuje balans stołu $\\rightarrow$ Karta jest **stabilizatorem / kotwicą stołu**.",
        "",
        "- **Rygor Próby:** Każdy element badany jest na pełnym pakiecie 16 setupów (min. 1000 partii / setup = min. 16 000 partii na wariant).",
    ])

    report_path, arch_path = save_and_archive_report(lines, "raport_uzytecznosci_i_wplywu.md")
    print(f"\n✅ 5-WARSTWOWY RAPORT WYGENEROWANY POMYŚLNIE!")
    print(f"   Raport:    {report_path}")
    print(f"   Archiwum:  {arch_path}\n")
    return report_path


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 Feature & Card Impact Audit (Ablation Study)")
    parser.add_argument("--games", type=int, default=5000, help="Liczba gier na setup (domyślnie: 5000, min. 1000)")
    parser.add_argument("--workers", type=int, default=min(os.cpu_count() or 4, 10), help="Liczba wątków równoległych")
    parser.add_argument("--seed", type=int, default=42, help="Ziarno losowe (CRN)")
    parser.add_argument("--canon-4p", action="store_true", help="Tryb Kanonu 4P: bada wyłącznie 5 setupów 4-osobowych (3.2x szybciej)")

    args = parser.parse_args()
    if args.games < 1000:
        print("⚠️ Podwyższam próbę do wymaganego minimum 1000 gier.")
        args.games = 1000

    if args.canon_4p:
        from feature_impact_4p import run_full_ablation_audit_4p
        run_full_ablation_audit_4p(games_per_setup=args.games, seed=args.seed, workers=args.workers)
    else:
        run_full_ablation_audit(games_per_setup=args.games, seed=args.seed, workers=args.workers)


if __name__ == "__main__":
    main()


