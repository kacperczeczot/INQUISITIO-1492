#!/usr/bin/env python3
"""INQUISITIO-1492 — OUTLIER HUNTER (Optymalizator Wielowymiarowy 2D/3D).

Specjalistyczny, odporny na zakleszczenia optymalizator balansu dla fazy post-plateau.
Wielopoziomowa strategia poszukiwań:
  Poziom 1: Antagonistyczne Pary 2D (Nerf Dominanta + Buff Frakcji Deficytowej)
  Poziom 2: Hybrydy Karta + Reguła Systemowa (L3 + L1/L2)
  Poziom 3: Wewnątrzfrakcyjne Przesunięcia (Rebalans talii wewnątrz frakcji)
  Poziom 4: Wiązki Sukcesywne 3D (Top 2D + Mikro-korekta systemowa)
  Poziom 5: Globalny Skaner Wariancji (Wielofrakcyjne pary kompensacyjne)

Algorytm 2-etapowego sita z adaptacyjną kolejką setupów:
  - Jeśli zapalny setup A nie ma dopuszczalnej pary w Poziomie 1, automatycznie przechodzi
    do setupu B, C, D lub rozszerza przestrzeń do Poziomów 2-5 (nigdy nie zatrzymuje się przedwcześnie).
  - Etap 1: Przesiew lokalny (min. 1000 gier)
  - Etap 2: Weryfikacja Ultra na wszystkich 16 setupach (min. 5000 gier, CRN)

Pełna automatyzacja dokumentacji (identyczna jak w Szalonym Audytorze):
  - raport_telemetrii.md (oraz archiwum wersji)
  - raport_optymalizacji.md (oraz archiwum wersji)
  - playtesting/balance-notes.md (wpisy Patch Notes + Stan Zmierzony)
  - outlier_hunter_log.md
  - Pełna synchronizacja kart, katalogu i księgi zasad (sync_config.py)
"""
from __future__ import annotations

import argparse
import copy
import itertools
import os
import re
import shutil
import signal
import subprocess
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

import yaml
from inquisitio.cards.loader import load_all_cards
from inquisitio.config import CONFIG, _CONFIG_PATH
from inquisitio.config_updater import apply_mutation_to_config, save_config_and_bump_version
from inquisitio.engine.setup import SETUP_PRESETS, FactionId
from inquisitio.runner.audit_facts import score_pair, save_and_archive_report
from inquisitio.runner.batch import run_batch
from inquisitio.runner.scoring import (
    calculate_category_scores,
    calculate_global_score,
    calculate_setup_score,
    color_score,
)

# Test builders for hybrid combinations
import audit_level1
import audit_level2

REPORTS_DIR = Path(__file__).resolve().parent.parent.parent / "playtesting" / "sim-reports"
LOG_FILE_PATH = REPORTS_DIR / "outlier_hunter_log.md"
BALANCE_NOTES_PATH = Path(__file__).resolve().parent.parent.parent / "playtesting" / "balance-notes.md"

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


def passes_telemetry_safety(res: dict) -> tuple[bool, str]:
    """Verify that candidate results stay within safety margins."""
    if res.get("deadlock_pct", 0) > 5.0:
        return False, f"Deadlock {res['deadlock_pct']:.1f}% > 5.0%"
    if res.get("poverty_pct", 0) > 30.0:
        return False, f"Pas Biedy {res['poverty_pct']:.1f}% > 30.0%"
    eras = res.get("eras_avg", 5.5)
    if eras < 4.5 or eras > 7.0:
        return False, f"Śr. Er {eras:.2f} poza zakresem [4.5, 7.0]"
    return True, "OK"


def _run_single_setup_task(task_args: tuple[tuple[str, str, dict], int, int, str]) -> dict:
    """Execute a candidate on a single targeted setup."""
    (rule_id, rule_name, rule_params), games, seed, setup_name = task_args
    t0 = time.time()

    summary = run_batch(
        games=games,
        setup=setup_name,
        seed=seed,
        layer="C",
        win_overrides=rule_params,
    )
    score = calculate_setup_score(summary)
    dt = round(time.time() - t0, 2)

    factions = SETUP_PRESETS[setup_name]
    shares = {}
    for fid in factions:
        fname = FACTION_NAMES[fid]
        w_count = summary.wins.get(fid, 0)
        shares[fname] = round((w_count / summary.games) * 100.0, 1)

    deadlock_pct = summary.eras_limit_pct * 100.0
    poverty_pct = summary.passes_forced_pct * 100.0
    eras_avg = summary.eras_avg

    return {
        "id": rule_id,
        "name": rule_name,
        "params": rule_params,
        "setup": setup_name,
        "setup_score": score,
        "shares": shares,
        "deadlock_pct": deadlock_pct,
        "poverty_pct": poverty_pct,
        "eras_avg": eras_avg,
        "dt": dt,
    }


def _run_full_16_setups_task(task_args: tuple[tuple[str, str, dict], int, int, list[str]]) -> dict:
    """Execute a candidate on all 16 setups."""
    (rule_id, rule_name, rule_params), games_per_setup, seed, setups = task_args
    t_start = time.time()

    summaries = []
    setup_scores = {}
    for sname in setups:
        summary = run_batch(
            games=games_per_setup,
            setup=sname,
            seed=seed,
            layer="C",
            win_overrides=rule_params,
        )
        summaries.append(summary)
        setup_scores[sname] = calculate_setup_score(summary)

    cat_scores = calculate_category_scores(summaries)
    global_score = calculate_global_score(cat_scores)
    dt = round(time.time() - t_start, 2)

    n_sum = len(summaries)
    eras_avg = sum(s.eras_avg for s in summaries) / n_sum
    deadlock_pct = (sum(s.eras_limit_pct for s in summaries) / n_sum) * 100.0
    poverty_pct = (sum(s.passes_forced_pct for s in summaries) / n_sum) * 100.0
    autodafe_avg = sum(s.autodafe_avg for s in summaries) / n_sum
    acc_avg = sum(s.accusations_avg for s in summaries) / n_sum

    min_setup_name = min(setup_scores, key=lambda k: setup_scores[k])
    min_setup_score = setup_scores[min_setup_name]

    return {
        "id": rule_id,
        "name": rule_name,
        "params": rule_params,
        "global_score": global_score,
        "cat_scores": cat_scores,
        "setup_scores": setup_scores,
        "min_setup": (min_setup_name, min_setup_score),
        "dt": dt,
        "eras_avg": eras_avg,
        "deadlock_pct": deadlock_pct,
        "poverty_pct": poverty_pct,
        "autodafe_avg": autodafe_avg,
        "acc_avg": acc_avg,
    }


def generate_and_save_telemetry_report(version: str, games_per_setup: int = 1000, seed: int = 42) -> tuple[Path, Path | None]:
    """Generates and archives raport_telemetrii.md for the given version."""
    setups = sorted(SETUP_PRESETS.keys())
    t0 = time.time()
    setup_data = []

    for sname in setups:
        summary = run_batch(games=games_per_setup, setup=sname, seed=seed, layer="C", threshold=8)
        score = calculate_setup_score(summary)
        factions = SETUP_PRESETS[sname]
        n_players = len(factions)
        ideal_share = round(100.0 / n_players, 1)

        faction_shares = {}
        for fid in factions:
            fname = FACTION_NAMES[fid]
            w_count = summary.wins.get(fid, 0)
            share = round((w_count / summary.games) * 100.0, 1)
            faction_shares[fname] = share

        avg_eras = round(summary.eras_avg, 2)
        deadlock_pct = round(summary.eras_limit_pct * 100.0, 1)
        poverty_pct = round(summary.passes_forced_pct * 100.0, 1)
        autodafe_avg = round(summary.autodafe_avg, 2)
        accusations_avg = round(summary.accusations_avg, 2)

        if 5.0 <= avg_eras <= 6.5:
            eras_opt = "🟢"
        elif 4.5 <= avg_eras <= 7.0:
            eras_opt = "🟡"
        else:
            eras_opt = "🔴"

        if deadlock_pct <= 5.0:
            deadlock_opt = "🟢"
        elif deadlock_pct <= 10.0:
            deadlock_opt = "🟡"
        else:
            deadlock_opt = "🔴"

        if poverty_pct <= 28.0:
            poverty_opt = "🟢"
        elif poverty_pct <= 32.0:
            poverty_opt = "🟡"
        else:
            poverty_opt = "🔴"

        if 0.7 <= autodafe_avg <= 1.8:
            autodafe_opt = "🟢"
        elif 0.5 <= autodafe_avg <= 2.0:
            autodafe_opt = "🟡"
        else:
            autodafe_opt = "🔴"

        if 2.0 <= accusations_avg <= 4.5:
            acc_opt = "🟢"
        elif 1.5 <= accusations_avg <= 5.0:
            acc_opt = "🟡"
        else:
            acc_opt = "🔴"

        setup_data.append({
            "setup": sname,
            "n_players": n_players,
            "score": score,
            "ideal_share": ideal_share,
            "shares": faction_shares,
            "avg_eras": avg_eras,
            "eras_opt": eras_opt,
            "deadlock_pct": deadlock_pct,
            "deadlock_opt": deadlock_opt,
            "poverty_pct": poverty_pct,
            "poverty_opt": poverty_opt,
            "autodafe_avg": autodafe_avg,
            "autodafe_opt": autodafe_opt,
            "accusations_avg": accusations_avg,
            "acc_opt": acc_opt,
            "end_gold": round(summary.avg_gold_end, 2),
            "end_heresy": round(summary.avg_heresy_end, 2),
        })

    elapsed = round(time.time() - t0, 2)

    report_lines = [
        f"# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: {version}",
        "",
        f"**Wersja Balansu:** `{version}` | **Data:** {datetime.now().strftime('%Y-%m-%d %H:%M')} | **Wielkość Próby:** {games_per_setup} gier/setup ({games_per_setup * 16} gier łącznie) | **Czas Symulacji:** {elapsed}s",
        "",
        "## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny",
        "",
        "| Setup | Gr. | Score | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |",
    ]

    for d in setup_data:
        so_s = f"{d['shares'].get('SO', 0.0):.1f}%" if "SO" in d['shares'] else "-"
        caa_s = f"{d['shares'].get('CAA', 0.0):.1f}%" if "CAA" in d['shares'] else "-"
        kb_s = f"{d['shares'].get('KB', 0.0):.1f}%" if "KB" in d['shares'] else "-"
        kt_s = f"{d['shares'].get('KT', 0.0):.1f}%" if "KT" in d['shares'] else "-"
        gc_s = f"{d['shares'].get('GC', 0.0):.1f}%" if "GC" in d['shares'] else "-"

        if d['score'] >= 90.0:
            eval_str = "🟢 ZBALANSOWANY"
        elif d['score'] >= 75.0:
            eval_str = "🟡 AKCEPTOWALNY"
        elif d['score'] >= 60.0:
            eval_str = "🟠 WYMAGA UWAGI"
        else:
            eval_str = "🔴 ODCHYLONY"
        report_lines.append(
            f"| `{d['setup']}` | {d['n_players']} | {color_score(d['score'], bold=True)} | {d['ideal_share']:.1f}% | {so_s} | {caa_s} | {kb_s} | {kt_s} | {gc_s} | {eval_str} |"
        )

    report_lines.extend([
        "",
        "## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności",
        "",
        "| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |",
    ])

    for d in setup_data:
        all_ok = (d['eras_opt'] == "🟢" and d['deadlock_opt'] == "🟢" and d['poverty_opt'] == "🟢")
        status_icon = "🟢 OPTYMALNA" if all_ok else "⚠️ WARTOŚCI BRZEGOWE"

        report_lines.append(
            f"| `{d['setup']}` | {d['avg_eras']} {d['eras_opt']} | {d['deadlock_pct']}% {d['deadlock_opt']} | {d['poverty_pct']}% {d['poverty_opt']} | {d['autodafe_avg']} {d['autodafe_opt']} | {d['accusations_avg']} {d['acc_opt']} | {d['end_gold']}zł | {d['end_heresy']} | {status_icon} |"
        )

    faction_stats: dict[str, list[tuple[str, float, float]]] = {}
    for d in setup_data:
        ideal = d['ideal_share'] / 100.0
        for fname, share_pct in d['shares'].items():
            share = share_pct / 100.0
            faction_stats.setdefault(fname, []).append((d['setup'], share, ideal))

    report_lines.extend([
        "",
        "## 3. Frakcje Wymagające Uwagi",
        "",
    ])

    faction_summary = []
    for fname, entries in sorted(faction_stats.items()):
        avg_share = sum(s for _, s, _ in entries) / len(entries)
        worst_setup = max(entries, key=lambda e: abs(e[1] - e[2]))
        worst_dev = worst_setup[1] - worst_setup[2]
        worst_dev_pct = worst_dev * 100.0
        if abs(worst_dev_pct) > 5.0:
            status = "🟡 DOMINUJE" if worst_dev > 0 else "🟡 SŁABA"
        elif abs(worst_dev_pct) > 8.0:
            status = "🔴 SILNIE ZABURZONA"
        else:
            status = "🟢 OK"
        faction_summary.append((fname, avg_share * 100, worst_setup[0], worst_dev_pct, status))

    report_lines.append("| Frakcja | Śr. Win Share (wszystkie setupy) | Najgorszy Setup | Max Odchylenie od Ideału | Status |")
    report_lines.append("| :--- | :---: | :--- | :---: | :--- |")
    for fname, avg_s, ws_name, ws_dev, ws_status in sorted(faction_summary, key=lambda x: abs(x[3]), reverse=True):
        dev_sign = f"+{ws_dev:.1f}%" if ws_dev > 0 else f"{ws_dev:.1f}%"
        report_lines.append(f"| **{fname}** | {avg_s:.1f}% | `{ws_name}` | {dev_sign} | {ws_status} |")

    weak_setups = [(d['setup'], d['score'], d['shares'], d['ideal_share']) for d in setup_data if d['score'] < 90.0]
    if weak_setups:
        report_lines.extend([
            "",
            "### Setupy poniżej Score 90 (wymagające poprawy):",
            "",
            "| Setup | Score | Główny problem |",
            "| :--- | :---: | :--- |",
        ])
        for sname, score, shares, ideal in sorted(weak_setups, key=lambda x: x[1]):
            max_dev_fname = max(shares, key=lambda f: abs(shares[f] - ideal))
            dev = shares[max_dev_fname] - ideal
            problem = f"{max_dev_fname} {'dominuje' if dev > 0 else 'za słaba'} ({shares[max_dev_fname]:.1f}% vs ideal {ideal:.1f}%)"
            report_lines.append(f"| `{sname}` | {color_score(score, bold=True)} | {problem} |")
    else:
        report_lines.extend(["", "### ✅ Wszystkie setupy mają Score ≥ 90 — brak setupów wymagających poprawy."])

    report_lines.extend([
        "",
        "## 4. Legenda Wskaźników Telemetrii i Norm Balansowych",
        "",
        "- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p",
        "- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem",
        "- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%",
        "- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%",
        "- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem",
        "- **⚖️ Oskarżenia / Partię:** 🟢 **2.0 – 4.5** | 🟡 1.5–2.0 / 4.5–5.0 | 🔴 poza zakresem",
        "- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 75 | 🟠 ≥ 60 | 🔴 < 60",
    ])

    return save_and_archive_report(report_lines, "raport_telemetrii.md")


def generate_and_save_optimization_report(
    old_version: str,
    new_version: str,
    iteration: int,
    base_res: dict,
    best_res: dict,
    all_ranked_candidates: list[dict],
    change_desc: str,
    rule_id: str,
    elapsed_iter: float,
) -> tuple[Path, Path | None]:
    """Generates and archives a detailed iteration report for the newly created version."""
    d_glob = best_res["global_score"] - base_res["global_score"]
    delta_str = f"+{d_glob:.1f}" if d_glob > 0 else f"{d_glob:.1f}"

    lines = [
        f"# Raport Optymalizacji Balansu (Outlier Hunter) — Wersja {new_version} (Iteracja #{iteration})",
        "",
        f"**Wersja Poprzednia:** `{old_version}` (`{base_res['global_score']:.1f} pkt`) → **Nowa Wersja:** `{new_version}` (`{best_res['global_score']:.1f} pkt`)",
        f"**Data:** {datetime.now().strftime('%Y-%m-%d %H:%M')} | **Czas Trwania Iteracji:** {elapsed_iter:.1f}s | **Zysk Global:** `{delta_str} pkt`",
        "",
        "## 1. Wprowadzona Zmiana i Wynik Balansu",
        f"- **Wybrany Wariant:** `{rule_id}` — **{best_res['name']}**",
        f"- **Opis Modyfikacji:** {change_desc}",
        f"- **Global Game Balance Score:** {score_pair(base_res['global_score'], best_res['global_score'], colored=True)} pkt",
        f"- **Rozbicie Składów Graczy:**",
        f"  - **3p:** {score_pair(base_res['cat_scores'].get('3p',0), best_res['cat_scores'].get('3p',0))} pkt",
        f"  - **4p:** {score_pair(base_res['cat_scores'].get('4p',0), best_res['cat_scores'].get('4p',0))} pkt",
        f"  - **5p:** {score_pair(base_res['cat_scores'].get('5p',0), best_res['cat_scores'].get('5p',0))} pkt",
        f"- **Kluczowa Telemetria Silnika:**",
        f"  - **Średnia Długość Gry:** `{best_res['eras_avg']:.2f} Er`",
        f"  - **Deadlocki (Limit Er):** `{best_res['deadlock_pct']:.1f}%` (norma: <5%)",
        f"  - **Pas Biedy (Złoto):** `{best_res['poverty_pct']:.1f}%` (norma: <30%)",
        f"  - **Autodafé / partię:** `{best_res['autodafe_avg']:.2f}`",
        f"  - **Oskarżenia / partię:** `{best_res['acc_avg']:.2f}`",
        "",
        "## 2. Ranking Przebadanych Kandydatów w tej Iteracji",
        "",
        "| Poz. | ID Wariantu | Nazwa / Opis | Global (baza → test) | 3p | 4p | 5p | Deadlocks % | Pas Biedy % | Status |",
        "| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
    ]

    for idx, c in enumerate(all_ranked_candidates, 1):
        g_diff = c["global_score"] - base_res["global_score"]
        status = "🌟 ZWYCIĘZCA" if c["id"] == best_res["id"] else ("🟢 ZYSK" if g_diff > 0.0 else "⚪ STRATA/NEUTRALNY")
        lines.append(
            f"| #{idx} | `{c['id']}` | {c['name']} | {score_pair(base_res['global_score'], c['global_score'], colored=True)} | "
            f"{c['cat_scores'].get('3p',0):.1f} | {c['cat_scores'].get('4p',0):.1f} | {c['cat_scores'].get('5p',0):.1f} | "
            f"{c['deadlock_pct']:.1f}% | {c['poverty_pct']:.1f}% | {status} |"
        )

    return save_and_archive_report(lines, "raport_optymalizacji.md")


def update_balance_notes(
    old_version: str,
    new_version: str,
    change_desc: str,
    rule_id: str,
    base_res: dict,
    best_res: dict,
):
    """Automatically update playtesting/balance-notes.md with the new measured scores and patch note entry."""
    if not BALANCE_NOTES_PATH.exists():
        return

    content = BALANCE_NOTES_PATH.read_text(encoding="utf-8")
    today = datetime.now().strftime("%Y-%m-%d")
    d_glob = best_res["global_score"] - base_res["global_score"]
    delta_str = f"+{d_glob:.1f}" if d_glob > 0 else f"{d_glob:.1f}"

    patch_note_block = (
        f"### 🟢 Patch {new_version} ({today}) — {change_desc} (Zysk Δ {delta_str} pkt)\n"
        f"- **Wynik:** Global **`{best_res['global_score']:.1f}`** | 3p **`{best_res['cat_scores'].get('3p',0.0):.1f}`** | 4p **`{best_res['cat_scores'].get('4p',0.0):.1f}`** | 5p **`{best_res['cat_scores'].get('5p',0.0):.1f}`**\n"
        f"- **Modyfikacja (`{rule_id}`):** {change_desc}.\n"
        f"- **Efekt:** Wzrost wyniku globalnego z {base_res['global_score']:.1f} do **`{best_res['global_score']:.1f} pkt`** ({delta_str} pkt). Telemetria: Średnia Er {best_res['eras_avg']:.2f}, Deadlocks {best_res['deadlock_pct']:.1f}%, Pas Biedy {best_res['poverty_pct']:.1f}%.\n\n"
    )

    history_heading = "## 📜 Chronologiczna Historia Zmian Balansu (Faza Prototypowa — Patch Notes)\n\n"
    if history_heading in content:
        content = content.replace(history_heading, history_heading + patch_note_block, 1)

    measured_pattern = r"(## 📊 Stan zmierzony — [^\n]+\n\nYAML po Patch [^\n]+\n\n- \*\*Global Game Balance Score:\*\* [^\n]+\n- \*\*3p Avg Score:\*\* [^\n]+\n- \*\*4p Avg Score:\*\* [^\n]+\n- \*\*5p Avg Score:\*\* [^\n]+)"
    new_measured_block = (
        f"## 📊 Stan zmierzony — {today} (Outlier Hunter 2D/3D, seed 42, warstwa C)\n\n"
        f"YAML po Patch {new_version} ({change_desc}).\n\n"
        f"- **Global Game Balance Score:** **`{best_res['global_score']:.1f} / 100.0 pkt` 🟢 (Auto-Optimizer Optimum)**\n"
        f"- **3p Avg Score:** **`{best_res['cat_scores'].get('3p',0.0):.1f} / 100.0 pkt` 🟢**\n"
        f"- **4p Avg Score:** **`{best_res['cat_scores'].get('4p',0.0):.1f} / 100.0 pkt` 🟢**\n"
        f"- **5p Avg Score:** **`{best_res['cat_scores'].get('5p',0.0):.1f} / 100.0 pkt` 🟢**"
    )
    if re.search(measured_pattern, content):
        content = re.sub(measured_pattern, new_measured_block, content, count=1)

    BALANCE_NOTES_PATH.write_text(content, encoding="utf-8")


def generate_atomic_card_mutations(faction_prefix: str) -> list[tuple[str, str, dict]]:
    """Build all atomic card mutations (+-1 cost, +-1 heresy, +-1 gold, +-1 target_heresy) for a faction."""
    cards = load_all_cards()
    mutations = []

    for cid, c in sorted(cards.items()):
        if not cid.startswith(f"{faction_prefix}-"):
            continue

        cost = getattr(c, "cost", 0)
        mutations.append((f"{cid}_cost+1", f"{cid.upper()} koszt {cost}→{cost+1}", {cid: {"cost": cost + 1}}))
        if cost > 0:
            mutations.append((f"{cid}_cost-1", f"{cid.upper()} koszt {cost}→{cost-1}", {cid: {"cost": cost - 1}}))

        heresy = getattr(c, "heresy", 0)
        mutations.append((f"{cid}_heresy+1", f"{cid.upper()} herezja {heresy}→{heresy+1}", {cid: {"heresy": heresy + 1}}))
        if heresy > 0:
            mutations.append((f"{cid}_heresy-1", f"{cid.upper()} herezja {heresy}→{heresy-1}", {cid: {"heresy": heresy - 1}}))

        gold = getattr(c, "gold", 0)
        if gold > 0:
            mutations.append((f"{cid}_gold+1", f"{cid.upper()} złoto {gold}→{gold+1}", {cid: {"gold": gold + 1}}))
            if gold > 1:
                mutations.append((f"{cid}_gold-1", f"{cid.upper()} złoto {gold}→{gold-1}", {cid: {"gold": gold - 1}}))

        target_heresy = getattr(c, "target_heresy", 0)
        if target_heresy > 0:
            mutations.append((f"{cid}_tgheresy+1", f"{cid.upper()} wrobienie {target_heresy}→{target_heresy+1}", {cid: {"target_heresy": target_heresy + 1}}))
            if target_heresy > 1:
                mutations.append((f"{cid}_tgheresy-1", f"{cid.upper()} wrobienie {target_heresy}→{target_heresy-1}", {cid: {"target_heresy": target_heresy - 1}}))

    return mutations


def classify_card_mutation_intent(mut_tuple: tuple[str, str, dict]) -> str:
    """Classify whether an atomic mutation is a BUFF, NERF, or SHIFT."""
    tag, _, pdict = mut_tuple
    cid = list(pdict.keys())[0]
    param = list(pdict[cid].keys())[0]
    val = pdict[cid][param]
    
    cards = load_all_cards()
    orig = getattr(cards.get(cid), param, 0)

    if param == "cost":
        return "BUFF" if val < orig else "NERF"
    elif param == "heresy":
        return "BUFF" if val < orig else "NERF"
    elif param in ("gold", "target_heresy"):
        return "BUFF" if val > orig else "NERF"
    return "NEUTRAL"


def merge_card_mutations(m1: tuple[str, str, dict], m2: tuple[str, str, dict]) -> tuple[str, str, dict]:
    """Merge two atomic card mutations into a single 2D composite candidate."""
    id1, name1, pdict1 = m1
    id2, name2, pdict2 = m2

    combined_id = f"PAIR_{id1}__{id2}"
    combined_name = f"{name1} + {name2}"

    merged_overrides = copy.deepcopy(pdict1)
    for cid, params in pdict2.items():
        if cid in merged_overrides:
            merged_overrides[cid].update(params)
        else:
            merged_overrides[cid] = copy.deepcopy(params)

    return (combined_id, combined_name, {"card_overrides": merged_overrides})


def generate_candidate_pool_for_strategy(
    strategy_level: int,
    setup_name: str,
    shares: dict[str, float],
    ideal_share: float,
) -> list[tuple[str, str, dict]]:
    """Generates focused candidate pools based on search strategy level."""
    factions = SETUP_PRESETS[setup_name]
    pairs: list[tuple[str, str, dict]] = []

    dominant_prefixes = []
    struggling_prefixes = []

    for fid in factions:
        fname = FACTION_NAMES[fid]
        pref = FACTION_ID_TO_PREFIX[fid]
        share = shares.get(fname, ideal_share)
        dev = share - ideal_share
        if dev >= 1.5:
            dominant_prefixes.append((pref, dev))
        elif dev <= -1.5:
            struggling_prefixes.append((pref, dev))

    dominant_prefixes.sort(key=lambda x: x[1], reverse=True)
    struggling_prefixes.sort(key=lambda x: x[1])

    if not dominant_prefixes or not struggling_prefixes:
        all_sorted = sorted([(FACTION_ID_TO_PREFIX[fid], shares.get(FACTION_NAMES[fid], ideal_share) - ideal_share) for fid in factions], key=lambda x: x[1])
        struggling_prefixes = [all_sorted[0]]
        dominant_prefixes = [all_sorted[-1]]

    # LEVEL 1: Antagonist 2D Pairs (Nerf Dominant + Buff Deficit)
    if strategy_level == 1:
        for dom_pref, _ in dominant_prefixes:
            dom_muts = generate_atomic_card_mutations(dom_pref)
            dom_nerfs = [m for m in dom_muts if classify_card_mutation_intent(m) == "NERF"]

            for strug_pref, _ in struggling_prefixes:
                strug_muts = generate_atomic_card_mutations(strug_pref)
                strug_buffs = [m for m in strug_muts if classify_card_mutation_intent(m) == "BUFF"]

                for m_nerf in dom_nerfs:
                    for m_buff in strug_buffs:
                        pairs.append(merge_card_mutations(m_nerf, m_buff))

    # LEVEL 2: Hybrid L3 Card + L1/L2 Rule Tweaks (Targeting ~400-500 focused combinations for 15-min budget)
    elif strategy_level == 2:
        l1_rules = [t for t in audit_level1.build_level1_tests() if t[0] != "L1_BAZA"]
        l2_rules = [t for t in audit_level2.build_level2_tests() if t[0] != "L2_BAZA"]

        # Filter L2 victory rules only for factions present in this setup
        setup_prefixes = set(FACTION_ID_TO_PREFIX[fid] for fid in factions)
        relevant_l2 = []
        for r in l2_rules:
            r_id = r[0].lower()
            if any(pref in r_id for pref in setup_prefixes):
                relevant_l2.append(r)

        sys_rules = l1_rules + relevant_l2

        for dom_pref, _ in dominant_prefixes:
            dom_nerfs = [m for m in generate_atomic_card_mutations(dom_pref) if classify_card_mutation_intent(m) == "NERF"]
            for m_nerf in dom_nerfs:
                for s_rule in sys_rules:
                    s_id, s_name, s_params = s_rule
                    combined_id = f"HYBRID_{m_nerf[0]}__{s_id}"
                    combined_name = f"{m_nerf[1]} + {s_name}"
                    merged_params = copy.deepcopy(s_params)
                    merged_params["card_overrides"] = copy.deepcopy(m_nerf[2])
                    pairs.append((combined_id, combined_name, merged_params))

        for strug_pref, _ in struggling_prefixes:
            strug_buffs = [m for m in generate_atomic_card_mutations(strug_pref) if classify_card_mutation_intent(m) == "BUFF"]
            for m_buff in strug_buffs:
                for s_rule in sys_rules:
                    s_id, s_name, s_params = s_rule
                    combined_id = f"HYBRID_{m_buff[0]}__{s_id}"
                    combined_name = f"{m_buff[1]} + {s_name}"
                    merged_params = copy.deepcopy(s_params)
                    merged_params["card_overrides"] = copy.deepcopy(m_buff[2])
                    pairs.append((combined_id, combined_name, merged_params))

    # LEVEL 3: Intra-Faction Shift Pairs (1 Buff + 1 Nerf in same faction)
    elif strategy_level == 3:
        for dom_pref, _ in dominant_prefixes:
            dom_muts = generate_atomic_card_mutations(dom_pref)
            dom_nerfs = [m for m in dom_muts if classify_card_mutation_intent(m) == "NERF"]
            dom_buffs = [m for m in dom_muts if classify_card_mutation_intent(m) == "BUFF"]

            for m_nerf in dom_nerfs:
                for m_buff in dom_buffs:
                    cid1 = list(m_nerf[2].keys())[0]
                    cid2 = list(m_buff[2].keys())[0]
                    if cid1 != cid2:
                        pairs.append(merge_card_mutations(m_nerf, m_buff))

    # LEVEL 4: Global Multi-Faction Variance Sweeper
    elif strategy_level >= 4:
        all_factions_in_setup = [FACTION_ID_TO_PREFIX[fid] for fid in factions]
        all_muts = []
        for pref in all_factions_in_setup:
            all_muts.extend(generate_atomic_card_mutations(pref))

        for i in range(len(all_muts)):
            for j in range(i + 1, min(len(all_muts), i + 25)):
                cid1 = list(all_muts[i][2].keys())[0]
                cid2 = list(all_muts[j][2].keys())[0]
                if cid1 != cid2:
                    pairs.append(merge_card_mutations(all_muts[i], all_muts[j]))

    seen = set()
    unique_pairs = []
    for p in pairs:
        if p[0] not in seen:
            seen.add(p[0])
            unique_pairs.append(p)

    return unique_pairs


def log_outlier_iteration(
    log_path: Path,
    iteration: int,
    old_ver: str,
    new_ver: str,
    target_setup: str,
    old_setup_score: float,
    new_setup_score: float,
    old_glob: float,
    new_glob: float,
    desc: str,
    rule_id: str,
    elapsed: float,
):
    """Appends an iteration log entry to outlier_hunter_log.md."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    if not log_path.exists():
        headers = [
            "# Dziennik Optymalizacji Outlier Hunter (2D/3D Multi-Mutation)",
            "",
            "Rejestr naprawionych setupów odstających i postępów w kierunku równomiernego balansu 100%.",
            "",
            "| Iteracja | Data i Czas | Wersja | Celowany Setup | Wynik Setupu | Global Score | Wprowadzona Para / Trójka | Czas |",
            "| :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: |",
        ]
        log_path.write_text("\n".join(headers) + "\n", encoding="utf-8")

    d_setup = new_setup_score - old_setup_score
    d_glob = new_glob - old_glob
    ds_str = f"+{d_setup:.1f}" if d_setup > 0 else f"{d_setup:.1f}"
    dg_str = f"+{d_glob:.1f}" if d_glob > 0 else f"{d_glob:.1f}"

    setup_col = f"{old_setup_score:.1f} → **{new_setup_score:.1f}** (`{ds_str}`)"
    glob_col = f"{old_glob:.1f} → **{new_glob:.1f}** (`{dg_str}`)"

    row = (
        f"| #{iteration} | {datetime.now().strftime('%Y-%m-%d %H:%M')} | `{old_ver}` → `{new_ver}` | "
        f"`{target_setup}` | {setup_col} | {glob_col} | **{desc}** (`{rule_id}`) | {elapsed:.1f}s |"
    )

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(row + "\n")


class OutlierHunter:
    def __init__(self, args: argparse.Namespace):
        self.args = args
        self.stop_requested = False
        self.total_iterations = 0
        self.start_time = time.time()
        self.initial_version = CONFIG.version
        signal.signal(signal.SIGINT, self._handle_sigint)

    def _handle_sigint(self, signum, frame):
        print("\n\n⚠️ Otrzymano sygnał przerwania (Ctrl+C). Bezpiecznie kończę bieżącą iterację...")
        self.stop_requested = True

    def _execute_pool(self, task_func, task_list: list) -> list[dict]:
        workers = min(self.args.workers, len(task_list))
        if workers <= 1:
            return [task_func(t) for t in task_list]
        with ProcessPoolExecutor(max_workers=workers) as executor:
            return list(executor.map(task_func, task_list))

    def run(self):
        print("═══════════════════════════════════════════════════════════════════════")
        print("     INQUISITIO-1492 — OUTLIER HUNTER (2D/3D Multi-Mutation Search)    ")
        print("  Celowana optymalizacja zapalnych setupów z globalną ochroną balansu  ")
        print("═══════════════════════════════════════════════════════════════════════")
        print(f"Bieżąca wersja bazowa:  {CONFIG.version}")
        print(f"Maksymalny czas sesji:  {self.args.hours if self.args.hours else 'Brak limitu (do optimum)'} godz.")
        print(f"Maksymalnie iteracji:   {self.args.max_iters if self.args.max_iters else 'Brak (do optimum)'}")
        print(f"Przesiew setupu (Etap1): {self.args.fast_games} gier (min. 1000)")
        print(f"Weryfikacja 16s (Etap2): {self.args.confirm_games} gier/setup ({self.args.confirm_games * 16} gier/kandydat)")
        print(f"Wątki procesora:        {self.args.workers}")
        print(f"Dziennik operacji:      {LOG_FILE_PATH}")
        print("═══════════════════════════════════════════════════════════════════════\n")

        setups = sorted(SETUP_PRESETS.keys())
        time_limit_sec = (self.args.hours * 3600) if self.args.hours else None

        current_strategy_level = 1
        attempted_setups_in_epoch: set[str] = set()

        while not self.stop_requested:
            # 1. Check time / iteration limit
            if time_limit_sec and (time.time() - self.start_time) >= time_limit_sec:
                print(f"\n⏱️ Osiągnięto limit czasu sesji ({self.args.hours}h). Kończę pracę.")
                break

            if self.args.max_iters and self.total_iterations >= self.args.max_iters:
                print(f"\n🔢 Osiągnięto maksymalną liczbę udanych iteracji ({self.args.max_iters}). Kończę pracę.")
                break

            iter_start = time.time()

            # 2. Run current 16-setup baseline measurement
            print(f"\n{'='*71}")
            print(f"🔍 [POMIAR BAZOWY] Diagnoza wszystkich 16 setupów (Próba: {self.args.confirm_games} gier/setup)...")
            base_task = ((("BASE", "Bieżący stan gry", {}), self.args.confirm_games, self.args.seed, setups),)
            base_res = self._execute_pool(_run_full_16_setups_task, [base_task[0]])[0]

            print(f"   📊 Global Balance Score: {color_score(base_res['global_score'], bold=True)} pkt")
            print(f"   🎯 3p: {base_res['cat_scores'].get('3p',0):.1f} | 4p: {base_res['cat_scores'].get('4p',0):.1f} | 5p: {base_res['cat_scores'].get('5p',0):.1f} pkt")

            # 3. Find and rank outlier setups (< 90 pts are strict blockers)
            sorted_setups = sorted(base_res["setup_scores"].items(), key=lambda x: x[1])
            weak_setups = [s for s in sorted_setups if s[1] < 90.0]

            print(f"\n📋 Status Setupów:")
            for sname, score in sorted_setups[:5]:
                print(f"   • `{sname}`: {color_score(score, bold=True)} pkt")

            if not weak_setups:
                print(f"🌟 Wszystkie 16 setupów ma Score ≥ 90 (Global: {base_res['global_score']:.1f} pkt)! Kontynuuję mikrostrojenie TOP {self.args.top_worst} najsłabszych układów ku 99+...")

            # STRICT OUTLIER FILTER: ONLY ever focus on the TOP N worst setups in the game.
            # Never waste time testing setups outside the top-worst window.
            candidate_queue = sorted_setups[: self.args.top_worst]
            available_setups = [s for s in candidate_queue if s[0] not in attempted_setups_in_epoch]

            if not available_setups:
                # All target setups failed at current strategy level -> escalate strategy depth-first!
                current_strategy_level += 1
                attempted_setups_in_epoch.clear()
                if current_strategy_level > 4:
                    print("\n🏁 Sprawdzono wszystkie poziomy strategii (1-4) dla zapalnych setupów. Resetuję cykl...")
                    current_strategy_level = 1
                strategy_names = {
                    1: "Poziom 1: Antagonistyczne Pary 2D (Nerf Dominanta + Buff Deficytu)",
                    2: "Poziom 2: Hybrydy Karta + Reguła Systemowa (L3 + L1/L2)",
                    3: "Poziom 3: Wewnątrzfrakcyjne Przesunięcia Stylu Gry",
                    4: "Poziom 4: Globalny Skaner Wariancji",
                }
                print(f"\n🔄 ESKALACJA STRATEGII DLA OUTLIERÓW → {strategy_names.get(current_strategy_level, f'Poziom {current_strategy_level}')}...\n")
                continue

            # Pick target setup (lowest scoring available setup)
            target_setup_name, target_setup_score = available_setups[0]
            factions = SETUP_PRESETS[target_setup_name]
            n_players = len(factions)
            ideal_share = 100.0 / n_players

            # Quick measure of shares in target setup
            s_task = (("BASE", "Base", {}), self.args.fast_games, self.args.seed, target_setup_name)
            s_diag = _run_single_setup_task(s_task)

            print(f"\n🎯 [CEL OPTYMALIZACJI] Zapalny setup: `{target_setup_name}` (Score: {color_score(target_setup_score, bold=True)} pkt)")
            shares_str = " | ".join([f"{f}: {s_diag['shares'].get(f, 0)}% (ideal {ideal_share:.1f}%)" for f in [FACTION_NAMES[fid] for fid in factions]])
            print(f"   Rozkład szans: {shares_str}")
            print(f"   Aktywna strategia: Poziom {current_strategy_level}")

            # 4. Generate candidate pool for current strategy level
            candidate_pairs = generate_candidate_pool_for_strategy(current_strategy_level, target_setup_name, s_diag["shares"], ideal_share)
            print(f"   🧬 Wygenerowano {len(candidate_pairs)} kandydatów.")

            if not candidate_pairs:
                print(f"⚠️ Brak kandydatów dla `{target_setup_name}` w strategii #{current_strategy_level}. Przechodzę do kolejnego setupu...")
                attempted_setups_in_epoch.add(target_setup_name)
                continue

            # 5. ETAP 1: Szybki Przesiew na Target Setupie (min. 1000 gier)
            print(f"\n--- [ETAP 1/2: PRZESIEW LOKALNY] Testuję {len(candidate_pairs)} par na `{target_setup_name}` ({self.args.fast_games} gier) ---")
            stage1_tasks = [(p, self.args.fast_games, self.args.seed, target_setup_name) for p in candidate_pairs]
            stage1_results = self._execute_pool(_run_single_setup_task, stage1_tasks)

            promising_candidates = []
            for r in stage1_results:
                d_setup = r["setup_score"] - target_setup_score
                is_safe, safe_msg = passes_telemetry_safety(r)
                if is_safe and d_setup >= self.args.min_worst_delta:
                    promising_candidates.append((r, d_setup))

            promising_candidates.sort(key=lambda x: x[1], reverse=True)

            if not promising_candidates:
                print(f"⚪ Żaden wariant nie przyniósł zysku na setupie `{target_setup_name}` w strategii #{current_strategy_level}. Przechodzę do kolejnego zapalnego setupu...")
                attempted_setups_in_epoch.add(target_setup_name)
                continue

            top_candidates = promising_candidates[: self.args.top_k]
            print(f"\n--- [ETAP 2/2: WERYFIKACJA ULTRA (16 SETUPÓW)] Sprawdzam TOP {len(top_candidates)} liderów na pełnej próbie {self.args.confirm_games} gier/setup ---")

            pair_dict = {p[0]: p for p in candidate_pairs}
            verify_tests = [pair_dict[c[0]["id"]] for c in top_candidates]

            verify_tasks = [(t, self.args.confirm_games, self.args.seed, setups) for t in verify_tests]
            verified_results = self._execute_pool(_run_full_16_setups_task, verify_tasks)

            accepted_candidate = None
            best_ver_res = None
            best_composite_gain = -999.0

            for ver_res in verified_results:
                new_target_score = ver_res["setup_scores"].get(target_setup_name, 0.0)
                d_target = new_target_score - target_setup_score
                d_global = ver_res["global_score"] - base_res["global_score"]
                is_safe, safe_msg = passes_telemetry_safety(ver_res)

                composite_gain = d_target + (d_global * 2.0)

                print(f"   ▶ [{ver_res['id'][:38]}...] Target: {target_setup_score:.1f} → {new_target_score:.1f} (Δ {d_target:+5.1f}) | Global: {base_res['global_score']:.1f} → {ver_res['global_score']:.1f} (Δ {d_global:+5.2f}) | {safe_msg}")

                if is_safe and d_target >= self.args.min_worst_delta and d_global >= self.args.min_global_delta:
                    if composite_gain > best_composite_gain:
                        best_composite_gain = composite_gain
                        accepted_candidate = pair_dict[ver_res["id"]]
                        best_ver_res = ver_res

            if not accepted_candidate or best_ver_res is None:
                print(f"\n⚪ Brak wariantu dla `{target_setup_name}` bez regresji w innych setupach w strategii #{current_strategy_level}. Przechodzę do kolejnego setupu...")
                attempted_setups_in_epoch.add(target_setup_name)
                continue

            # 6. Apply Accepted Modification to game_config.yaml
            self.total_iterations += 1
            rule_id, rule_name, rule_params = accepted_candidate

            with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
                raw_cfg = yaml.safe_load(f)

            old_version = raw_cfg.get("version", "v0.30")
            mod_cfg, change_desc = apply_mutation_to_config(raw_cfg, rule_id, rule_params)

            if self.args.dry_run:
                print(f"\n[DRY RUN] Zaakceptowano by modyfikację: {change_desc}")
                print(f"[DRY RUN] Nowy wynik setupu: {best_ver_res['setup_scores'][target_setup_name]:.1f} | Nowy Global: {best_ver_res['global_score']:.1f}")
                attempted_setups_in_epoch.add(target_setup_name)
            else:
                new_version, saved_path = save_config_and_bump_version(mod_cfg, _CONFIG_PATH, bump_version=True)
                iter_elapsed = round(time.time() - iter_start, 2)

                print(f"\n🎉 [ZAAKCEPTOWANO PATCH #{self.total_iterations}]")
                print(f"   Wersja:        `{old_version}` → **`{new_version}`**")
                print(f"   Modyfikacja:   {change_desc}")
                print(f"   Setup `{target_setup_name}`: {target_setup_score:.1f} → **{best_ver_res['setup_scores'][target_setup_name]:.1f} pkt** (Δ {best_ver_res['setup_scores'][target_setup_name] - target_setup_score:+.1f} pkt)")
                print(f"   Global Score:  {base_res['global_score']:.1f} → **{best_ver_res['global_score']:.1f} pkt** (Δ {best_ver_res['global_score'] - base_res['global_score']:+.2f} pkt)")

                # 7. GENERATE COMPLETE DOCUMENTATION SUITE
                print(f"\n📄 [DOKUMENTACJA] Generuję pełny pakiet raportów i archiwum wersji {new_version}...")

                log_outlier_iteration(
                    LOG_FILE_PATH,
                    self.total_iterations,
                    old_version,
                    new_version,
                    target_setup_name,
                    target_setup_score,
                    best_ver_res["setup_scores"][target_setup_name],
                    base_res["global_score"],
                    best_ver_res["global_score"],
                    change_desc,
                    rule_id,
                    iter_elapsed,
                )

                opt_out, opt_arch = generate_and_save_optimization_report(
                    old_version,
                    new_version,
                    self.total_iterations,
                    base_res,
                    best_ver_res,
                    verified_results,
                    change_desc,
                    rule_id,
                    iter_elapsed,
                )
                print(f"   ✔ Zapisano raport optymalizacji: {opt_out.name} (archiwum: {opt_arch})")

                telem_out, telem_arch = generate_and_save_telemetry_report(
                    new_version,
                    games_per_setup=self.args.fast_games,
                    seed=self.args.seed,
                )
                print(f"   ✔ Zaktualizowano raport telemetrii: {telem_out.name} (archiwum: {telem_arch})")

                update_balance_notes(old_version, new_version, change_desc, rule_id, base_res, best_ver_res)
                print(f"   ✔ Zaktualizowano notatki balansu: {BALANCE_NOTES_PATH.name}")

                print("   🔄 Synchronizuję dokumentację kart i reguł...")
                subprocess.run([sys.executable, str(TOOLS_SIM_DIR.parent / "sync_config.py")])
                print("   ✔ Zaktualizowano katalog kart, opisy markdown i card-editor.")

                # Reset state after successful patch
                attempted_setups_in_epoch.clear()
                current_strategy_level = 1

        print(f"\n═══════════════════════════════════════════════════════════════════════")
        print(f"   OUTLIER HUNTER ZAKOŃCZYŁ SESJĘ. ŁĄCZNIE WPROWADZONO {self.total_iterations} PATCHY.")
        print(f"═══════════════════════════════════════════════════════════════════════\n")


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 Outlier Hunter — 2D/3D Multi-Mutation Balance Optimizer")
    parser.add_argument("--hours", type=float, default=None, help="Maksymalny czas działania w godzinach (np. 8.0 na noc)")
    parser.add_argument("--max-iters", type=int, default=None, help="Maksymalna liczba udanych patchów przed zatrzymaniem")
    parser.add_argument("--fast-games", type=int, default=1000, help="Liczba gier w Etapie 1 (przesiew na 1 setupie, min. 1000)")
    parser.add_argument("--confirm-games", type=int, default=5000, help="Liczba gier w Etapie 2 (weryfikacja 16 setupów, min. 5000)")
    parser.add_argument("--workers", type=int, default=min(os.cpu_count() or 4, 10), help="Liczba procesów równoległych")
    parser.add_argument("--seed", type=int, default=42, help="Ziarno generatora liczb losowych")
    parser.add_argument("--min-worst-delta", type=float, default=1.0, help="Minimalny zysk na zapalnym setupie (pkt)")
    parser.add_argument("--min-global-delta", type=float, default=-0.1, help="Maksymalny dopuszczalny spadek globalny (zabezpieczenie przed regresją)")
    parser.add_argument("--top-k", type=int, default=8, help="Liczba najlepszych par sprawdzanych w Etapie 2")
    parser.add_argument("--top-worst", type=int, default=3, help="Liczba najsłabszych setupów, na których wyłącznie skupia się optymalizator (domyślnie: 3)")
    parser.add_argument("--dry-run", action="store_true", help="Tryb symulacji bez zapisywania zmian do game_config.yaml")

    args = parser.parse_args()

    if args.fast_games < 1000:
        print("⚠️ Podwyższam fast-games do wymaganego minimum 1000 gier.")
        args.fast_games = 1000
    if args.confirm_games < 5000:
        print("⚠️ Podwyższam confirm-games do wymaganego minimum 5000 gier.")
        args.confirm_games = 5000

    hunter = OutlierHunter(args)
    hunter.run()


if __name__ == "__main__":
    main()
