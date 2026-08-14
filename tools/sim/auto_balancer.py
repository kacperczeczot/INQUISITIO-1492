#!/usr/bin/env python3
"""INQUISITIO-1492 — SZALONY AUDYTOR / AUTONOMOUS BALANCE OPTIMIZER.

Autonomously explores the parameter space (Levels 1–4), finds the single best
balance improvement (highest delta global), applies the change to game_config.yaml,
bumps the version, archives snapshots, generates full reports & documentation,
updates playtesting/balance-notes.md and repeats in a continuous hill-climbing loop
until a global optimum is reached or time limit expires.
"""
from __future__ import annotations

import argparse
import copy
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

# Import test builders
import audit_level1
import audit_level2
import audit_level3
import audit_level4

REPORTS_DIR = Path(__file__).resolve().parent.parent.parent / "playtesting" / "sim-reports"
LOG_FILE_PATH = REPORTS_DIR / "auto_balancer_log.md"
BALANCE_NOTES_PATH = Path(__file__).resolve().parent.parent.parent / "playtesting" / "balance-notes.md"

FACTION_NAMES = {
    FactionId.SWIETE_OFICJUM: "SO",
    FactionId.CIENIE_AL_ANDALUS: "CAA",
    FactionId.KORONA_BORGIOWIE: "KB",
    FactionId.KABALA_TOLEDO: "KT",
    FactionId.GILDIA_CIENI: "GC",
}


def _run_single_test_task(task_args: tuple[tuple[str, str, dict], int, int, list[str]]) -> dict:
    """Execute a single candidate rule across all setups."""
    (rule_id, rule_name, rule_params), games_per_setup, seed, setups = task_args
    t_rule = time.time()

    summaries = []
    for sname in setups:
        summary = run_batch(
            games=games_per_setup,
            setup=sname,
            seed=seed,
            layer="C",
            win_overrides=rule_params,
        )
        summaries.append(summary)

    cat_scores = calculate_category_scores(summaries)
    global_score = calculate_global_score(cat_scores)
    dt = round(time.time() - t_rule, 2)

    n_sum = len(summaries)
    eras_avg = sum(s.eras_avg for s in summaries) / n_sum
    eras_min = min(s.eras_min for s in summaries)
    eras_max = max(s.eras_max for s in summaries)

    deadlock_pct = (sum(s.eras_limit_pct for s in summaries) / n_sum) * 100.0
    poverty_pct = (sum(s.passes_forced_pct for s in summaries) / n_sum) * 100.0

    autodafe_avg = sum(s.autodafe_avg for s in summaries) / n_sum
    autodafe_min = min(s.autodafe_min for s in summaries)
    autodafe_max = max(s.autodafe_max for s in summaries)

    acc_avg = sum(s.accusations_avg for s in summaries) / n_sum
    acc_min = min(s.accusations_min for s in summaries)
    acc_max = max(s.accusations_max for s in summaries)

    gold_avg = sum(s.avg_gold_end for s in summaries) / n_sum
    gold_min = min(s.gold_min for s in summaries)
    gold_max = max(s.gold_max for s in summaries)

    heresy_avg = sum(s.avg_heresy_end for s in summaries) / n_sum
    heresy_min = min(s.heresy_min for s in summaries)
    heresy_max = max(s.heresy_max for s in summaries)

    return {
        "id": rule_id,
        "name": rule_name,
        "params": rule_params,
        "global_score": global_score,
        "cat_scores": cat_scores,
        "dt": dt,
        "eras_avg": eras_avg, "eras_min": eras_min, "eras_max": eras_max,
        "deadlock_pct": deadlock_pct,
        "poverty_pct": poverty_pct,
        "autodafe_avg": autodafe_avg, "autodafe_min": autodafe_min, "autodafe_max": autodafe_max,
        "acc_avg": acc_avg, "acc_min": acc_min, "acc_max": acc_max,
        "gold_avg": gold_avg, "gold_min": gold_min, "gold_max": gold_max,
        "heresy_avg": heresy_avg, "heresy_min": heresy_min, "heresy_max": heresy_max,
    }


def generate_candidate_tests(
    level_filter: str = "all",
    param_filter: str = "cost,heresy",
    card_filter: str | None = None,
) -> list[tuple[str, str, dict]]:
    """Build all candidate tests from levels 1 to 4."""
    tests = [("BAZA", "Baza (Bieżący stan gry)", {})]

    if level_filter in ("all", "1"):
        l1 = audit_level1.build_level1_tests()
        tests.extend([t for t in l1 if t[0] != "L1_BAZA"])

    if level_filter in ("all", "2"):
        l2 = audit_level2.build_level2_tests()
        tests.extend([t for t in l2 if t[0] != "L2_BAZA"])

    if level_filter in ("all", "3"):
        l3 = audit_level3.build_level3_tests(param_filter=param_filter, card_filter=card_filter)
        tests.extend([t for t in l3 if t[0] != "L3_BAZA"])

    if level_filter in ("all", "4"):
        l4 = audit_level4.build_level4_tests()
        tests.extend([t for t in l4 if t[0] != "L4_BAZA"])

    return tests


def passes_telemetry_safety(res: dict) -> tuple[bool, str]:
    """Verify that a candidate does not violate critical telemetry norms."""
    if res["deadlock_pct"] > 16.0:
        return False, f"Deadlock {res['deadlock_pct']:.1f}% > 16%"
    if res["poverty_pct"] > 35.0:
        return False, f"Pas Biedy {res['poverty_pct']:.1f}% > 35%"
    if res["eras_avg"] < 4.2 or res["eras_avg"] > 7.8:
        return False, f"Śr. Er {res['eras_avg']:.2f} poza zakresem [4.2, 7.8]"
    return True, "OK"


def generate_and_save_telemetry_report(version: str, games_per_setup: int = 500, seed: int = 42) -> tuple[Path, Path | None]:
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

        eras_opt = "🟢" if (5.0 <= avg_eras <= 7.0) else "🔴"
        deadlock_opt = "🟢" if (deadlock_pct <= 15.0) else "🔴"
        poverty_opt = "🟢" if (poverty_pct <= 30.0) else "🔴"
        autodafe_opt = "🟢" if (0.5 <= autodafe_avg <= 2.0) else "⚪"
        acc_opt = "🟢" if (1.5 <= accusations_avg <= 4.5) else "⚪"

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

        eval_str = "🟢 ZBALANSOWANY" if d['score'] >= 50.0 else ("🟡 AKCEPTOWALNY" if d['score'] >= 25.0 else "🔴 ODCHYLONY")
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

    report_lines.extend([
        "",
        "## 3. Legenda Wskaźników Telemetrii i Norm Balansowych",
        "",
        "- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p",
        "- **⏱️ Średnia Er (Tempo Gry):** Normatyw: **5.0 – 7.0 Er** (oznaczono 🟢 / 🔴)",
        "- **🔒 Remisy po 8 Erach (Deadlock %):** Dopuszczalne: **< 15.0%** (oznaczono 🟢 / 🔴)",
        "- **💰 Pas Biedy (Poverty Rate %):** Dopuszczalne: **< 30.0%** tur spasionych z braku monety (oznaczono 🟢 / 🔴)",
        "- **🔥 Autodafé / Partię (Aktywność Inkwizycji):** Optymalne: **0.5 – 2.0** na grę (oznaczono 🟢 / ⚪)",
        "- **⚖️ Oskarżenia na Dworze / Partię:** Optymalne: **1.5 – 4.5** na grę (oznaczono 🟢 / ⚪)",
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
        f"# Raport Optymalizacji Balansu (Szalony Audytor) — Wersja {new_version} (Iteracja #{iteration})",
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
        f"  - **Średnia Długość Gry:** `{best_res['eras_avg']:.2f} Er` (zakres: {best_res['eras_min']}–{best_res['eras_max']})",
        f"  - **Deadlocki (Limit 8/9 Er):** `{best_res['deadlock_pct']:.1f}%` (norma: <15%)",
        f"  - **Pas Biedy (Wymuszony brak monety):** `{best_res['poverty_pct']:.1f}%` (norma: <30%)",
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

    # Build new patch note block
    patch_note_block = (
        f"### 🟢 Patch {new_version} ({today}) — {change_desc} (Zysk Δ {delta_str} pkt)\n"
        f"- **Wynik:** Global **`{best_res['global_score']:.1f}`** | 3p **`{best_res['cat_scores'].get('3p',0.0):.1f}`** | 4p **`{best_res['cat_scores'].get('4p',0.0):.1f}`** | 5p **`{best_res['cat_scores'].get('5p',0.0):.1f}`**\n"
        f"- **Modyfikacja (`{rule_id}`):** {change_desc}.\n"
        f"- **Efekt:** Wzrost wyniku globalnego z {base_res['global_score']:.1f} do **`{best_res['global_score']:.1f} pkt`** ({delta_str} pkt). Telemetria: Średnia Er {best_res['eras_avg']:.2f}, Deadlocks {best_res['deadlock_pct']:.1f}%, Pas Biedy {best_res['poverty_pct']:.1f}%.\n\n"
    )

    # Insert below heading: ## 📜 Chronologiczna Historia Zmian Balansu (Faza Prototypowa — Patch Notes)
    history_heading = "## 📜 Chronologiczna Historia Zmian Balansu (Faza Prototypowa — Patch Notes)\n\n"
    if history_heading in content:
        content = content.replace(history_heading, history_heading + patch_note_block, 1)

    # Update ## 📊 Stan zmierzony block
    measured_pattern = r"(## 📊 Stan zmierzony — [^\n]+\n\nYAML po Patch [^\n]+\n\n- \*\*Global Game Balance Score:\*\* [^\n]+\n- \*\*3p Avg Score:\*\* [^\n]+\n- \*\*4p Avg Score:\*\* [^\n]+\n- \*\*5p Avg Score:\*\* [^\n]+)"
    new_measured_block = (
        f"## 📊 Stan zmierzony — {today} (Szalony Audytor, seed 42, warstwa C)\n\n"
        f"YAML po Patch {new_version} ({change_desc}).\n\n"
        f"- **Global Game Balance Score:** **`{best_res['global_score']:.1f} / 100.0 pkt` 🟢 (Auto-Optimizer Optimum)**\n"
        f"- **3p Avg Score:** **`{best_res['cat_scores'].get('3p',0.0):.1f} / 100.0 pkt` 🟢**\n"
        f"- **4p Avg Score:** **`{best_res['cat_scores'].get('4p',0.0):.1f} / 100.0 pkt` 🟢**\n"
        f"- **5p Avg Score:** **`{best_res['cat_scores'].get('5p',0.0):.1f} / 100.0 pkt` 🟢**"
    )
    if re.search(measured_pattern, content):
        content = re.sub(measured_pattern, new_measured_block, content, count=1)

    BALANCE_NOTES_PATH.write_text(content, encoding="utf-8")


def log_iteration_to_markdown(
    log_path: Path,
    iteration: int,
    old_version: str,
    new_version: str,
    desc: str,
    rule_id: str,
    base_res: dict,
    best_res: dict,
    elapsed_iter: float,
):
    """Appends an iteration record to auto_balancer_log.md."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    if not log_path.exists():
        header = [
            "# Dziennik Ewolucji Balansu — Szalony Audytor (Auto-Balancer)",
            "",
            "Automatyczny rejestr wprowadzonych zmian balansu, podbić wersji i ewolucji punktacji globalnej.",
            "",
            "| Iteracja | Data i Czas | Wersja | Modyfikacja | Global Score | 3p | 4p | 5p | Deadlock % | Pas Biedy % | Czas |",
            "| :---: | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
        ]
        log_path.write_text("\n".join(header) + "\n", encoding="utf-8")

    d_glob = best_res["global_score"] - base_res["global_score"]
    delta_str = f"+{d_glob:.1f}" if d_glob > 0 else f"{d_glob:.1f}"

    score_col = f"{base_res['global_score']:.1f} → **{best_res['global_score']:.1f}** (`{delta_str}`)"
    p3_col = f"{base_res['cat_scores'].get('3p',0):.1f} → {best_res['cat_scores'].get('3p',0):.1f}"
    p4_col = f"{base_res['cat_scores'].get('4p',0):.1f} → {best_res['cat_scores'].get('4p',0):.1f}"
    p5_col = f"{base_res['cat_scores'].get('5p',0):.1f} → {best_res['cat_scores'].get('5p',0):.1f}"

    row = (
        f"| #{iteration} | {datetime.now().strftime('%Y-%m-%d %H:%M')} | `{old_version}` → `{new_version}` | "
        f"**{desc}** (`{rule_id}`) | {score_col} | {p3_col} | {p4_col} | {p5_col} | "
        f"{best_res['deadlock_pct']:.1f}% | {best_res['poverty_pct']:.1f}% | {elapsed_iter:.1f}s |"
    )

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(row + "\n")


def run_full_suite_audit(games: int = 500, seed: int = 42):
    """Runs all audit levels and saves full suite reports for the final optimum version."""
    print("\n═══════════════════════════════════════════════════════════════════════")
    print(f"  GENEROWANIE PEŁNEGO PAKIETU 6 RAPORTÓW AUDYTU DLA WERSJI {CONFIG.version}  ")
    print("═══════════════════════════════════════════════════════════════════════")
    pipeline = [
        ("Telemetria i Win Shares", TOOLS_SIM_DIR / "generate_report.py", ["--games", str(games), "--seed", str(seed)]),
        ("Poziom 1 (Mechaniki Systemowe)", TOOLS_SIM_DIR / "audit_level1.py", ["--games", str(games), "--seed", str(seed)]),
        ("Poziom 2 (Warunki Zwycięstwa)", TOOLS_SIM_DIR / "audit_level2.py", ["--games", str(games), "--seed", str(seed)]),
        ("Poziom 3 (Parametry Kart)", TOOLS_SIM_DIR / "audit_level3.py", ["--games", str(max(150, games // 2)), "--param", "cost,heresy", "--seed", str(seed)]),
        ("Poziom 4 (Warianty Niszowe)", TOOLS_SIM_DIR / "audit_level4.py", ["--games", str(games), "--seed", str(seed)]),
        ("Testy Stresu Ekonomicznego", TOOLS_SIM_DIR / "audit_stress_tests.py", ["--games", str(games), "--seed", str(seed)]),
    ]
    for idx, (name, script_path, default_args) in enumerate(pipeline, 1):
        print(f"▶ [{idx}/{len(pipeline)}] Generuję: {name}...")
        subprocess.run([sys.executable, str(script_path)] + default_args)


class AutoBalancer:
    def __init__(self, args: argparse.Namespace):
        self.args = args
        self.stop_requested = False
        self.total_iterations = 0
        self.start_time = time.time()
        self.initial_version = CONFIG.version
        self.initial_score = 0.0

        # Handle SIGINT (Ctrl+C) gracefully
        signal.signal(signal.SIGINT, self._handle_sigint)

    def _handle_sigint(self, signum, frame):
        print("\n\n⚠️ Otrzymano sygnał przerwania (Ctrl+C). Bezpiecznie kończę bieżącą iterację...")
        self.stop_requested = True

    def run(self):
        print("═══════════════════════════════════════════════════════════════════════")
        print("    INQUISITIO-1492 — SZALONY AUDYTOR / AUTONOMOUS BALANCE OPTIMIZER   ")
        print("    Wielopoziomowa pętla optymalizacji balansu (Greedy Hill-Climbing)  ")
        print("═══════════════════════════════════════════════════════════════════════")
        print(f"Bieżąca wersja bazowa: {CONFIG.version}")
        print(f"Tryb działania:        {self.args.mode.upper()}")
        print(f"Maksymalny czas:       {self.args.hours if self.args.hours else 'Brak (do odwołania)'} godz.")
        print(f"Maksymalnie iteracji:  {self.args.max_iters if self.args.max_iters else 'Brak (do optimum)'}")
        print(f"Minimalna delta zysku: +{self.args.min_delta} pkt")
        print(f"Poziomy testowe:       {self.args.level.upper()}")
        print(f"Wątki procesora:       {self.args.workers}")
        print(f"Lokalizacja logów:     {LOG_FILE_PATH}")
        print("═══════════════════════════════════════════════════════════════════════\n")

        setups = sorted(SETUP_PRESETS.keys())
        time_limit_sec = (self.args.hours * 3600) if self.args.hours else None

        if self.args.level == "all":
            tiers = ["1", "2", "3", "4"]
        else:
            tiers = [self.args.level]

        tier_names = {
            "1": "POZIOM 1 (Główne Mechaniki Systemowe)",
            "2": "POZIOM 2 (Warunki Zwycięstwa i Skalowanie)",
            "3": "POZIOM 3 (Parametry Kart: Koszt, Herezja, Złoto)",
            "4": "POZIOM 4 (Warianty Niszowe i Edykty)",
        }

        tier_idx = 0

        while not self.stop_requested and tier_idx < len(tiers):
            current_tier = tiers[tier_idx]
            current_tier_name = tier_names.get(current_tier, f"POZIOM {current_tier}")

            self.total_iterations += 1
            iter_start = time.time()

            # Check time limit
            if time_limit_sec and (time.time() - self.start_time) >= time_limit_sec:
                print(f"\n⏱️ Osiągnięto limit czasu ({self.args.hours}h). Zatrzymuję pętlę.")
                break

            # Check iteration limit
            if self.args.max_iters and self.total_iterations > self.args.max_iters:
                print(f"\n🔢 Osiągnięto maksymalną liczbę iteracji ({self.args.max_iters}). Zatrzymuję pętlę.")
                break

            print(f"\n{'='*71}")
            print(f"▶ ITERACJA #{self.total_iterations} — Wersja: {CONFIG.version} | {current_tier_name}")
            print(f"  Czas łączny sesji: {round((time.time() - self.start_time)/60, 1)} min")
            print(f"{'='*71}")

            # 1. Generate all candidate tests for current level
            candidate_tests = generate_candidate_tests(
                level_filter=current_tier,
                param_filter=self.args.param,
                card_filter=self.args.card,
            )
            print(f"Wygenerowano {len(candidate_tests)} wariantów testowych dla {current_tier_name}.")

            # 2. Strategy Execution:
            # - For small tiers (L1: ~12, L2: ~28, L4: ~8 tests): Direct Ultra evaluation on confirm_games (no screening needed!)
            # - For large tiers (L3: ~200+ card tests): Two-stage screening (1000 games -> TOP 20 -> confirm_games)
            if current_tier in ("1", "2", "4") or len(candidate_tests) <= self.args.top_k or self.args.mode != "two-stage":
                games_per_setup = self.args.confirm_games if self.args.mode == "two-stage" else (
                    3000 if self.args.mode == "grand" else (500 if self.args.mode == "standard" else 250)
                )
                best_candidate, base_res, best_res, ranked_candidates = self._run_direct_stage(candidate_tests, setups, games_per_setup)
            else:
                best_candidate, base_res, best_res, ranked_candidates = self._run_two_stage(candidate_tests, setups)

            if self.stop_requested:
                break

            delta_global = (best_res["global_score"] - base_res["global_score"]) if (best_res and base_res) else 0.0

            # 3. Check if improvement found in this tier
            if not best_candidate or best_res is None or base_res is None or delta_global < self.args.min_delta:
                print(f"\n⚪ {current_tier_name} optymalny — brak modyfikacji przynoszącej zysk >= +{self.args.min_delta} pkt.")
                tier_idx += 1
                if tier_idx < len(tiers):
                    next_tier_name = tier_names.get(tiers[tier_idx], f"Poziom {tiers[tier_idx]}")
                    print(f"➡️ Przechodzę kaskadowo do: {next_tier_name}...\n")
                else:
                    print(f"\n🏆 OSIĄGNIĘTO PEŁNE LOKALNE OPTIMUM GLOBALNE WE WSZYSTKICH POZIOMACH (L1 → L2 → L3 → L4)!")
                continue

            print(f"\n📊 Wynik Bazy: {color_score(base_res['global_score'], bold=True)} pkt")
            print(f"🌟 Najlepszy kandydat: [{best_res['id']}] {best_res['name']}")
            print(f"   Nowy Global Score:  {color_score(best_res['global_score'], bold=True)} pkt (Δ {delta_global:+5.2f} pkt)")

            # 4. Apply modification to game_config.yaml
            rule_id, rule_name, rule_params = best_candidate
            with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
                raw_cfg = yaml.safe_load(f)

            old_version = raw_cfg.get("version", "v0.19")
            mod_cfg, change_desc = apply_mutation_to_config(raw_cfg, rule_id, rule_params)

            if self.args.dry_run:
                print(f"\n[DRY RUN] Zastosowano by zmianę: {change_desc}")
                print(f"[DRY RUN] Podbito by wersję z {old_version} do nowej.")
                tier_idx += 1
            else:
                new_version, saved_path = save_config_and_bump_version(mod_cfg, _CONFIG_PATH, bump_version=True)
                iter_elapsed = round(time.time() - iter_start, 2)
                print(f"\n✅ ZAPISANO ZMIANĘ DO: {saved_path.name}")
                print(f"   Opis zmiany:  {change_desc}")
                print(f"   Wersja:       {old_version} → {new_version}")
                print(f"   Zysk Balansu: {score_pair(base_res['global_score'], best_res['global_score'], colored=True)}")

                # 5. Generate Reports & Documentation Automatically
                print(f"\n📄 [DOKUMENTACJA] Generuję raporty i archiwum wersji {new_version}...")
                
                # A. Log entry in auto_balancer_log.md
                log_iteration_to_markdown(
                    LOG_FILE_PATH,
                    self.total_iterations,
                    old_version,
                    new_version,
                    change_desc,
                    rule_id,
                    base_res,
                    best_res,
                    iter_elapsed,
                )

                # B. Save detailed optimization report for this iteration
                opt_out, opt_arch = generate_and_save_optimization_report(
                    old_version,
                    new_version,
                    self.total_iterations,
                    base_res,
                    best_res,
                    ranked_candidates,
                    change_desc,
                    rule_id,
                    iter_elapsed,
                )
                print(f"   ✔ Zapisano raport optymalizacji: {opt_out.name} (archiwum: {opt_arch})")

                # C. Generate full telemetry & win shares report for new version
                telem_out, telem_arch = generate_and_save_telemetry_report(new_version, games_per_setup=self.args.fast_games * 2, seed=self.args.seed)
                print(f"   ✔ Zaktualizowano raport telemetrii: {telem_out.name} (archiwum: {telem_arch})")

                # D. Update playtesting/balance-notes.md
                update_balance_notes(old_version, new_version, change_desc, rule_id, base_res, best_res)
                print(f"   ✔ Zaktualizowano notatki balansu: {BALANCE_NOTES_PATH.name}")

                # CASCADE RESET: Always reset back to Level 1 after a successful change!
                if tier_idx > 0:
                    print(f"\n🔄 Zmiana wprowadzona na {current_tier_name}! Resetuję kaskadę i wracam do POZIOMU 1...\n")
                tier_idx = 0

        # Optional full audit suite on finish
        if not self.args.dry_run and self.args.full_audit_on_finish and self.total_iterations > 0:
            run_full_suite_audit(games=self.args.confirm_games, seed=self.args.seed)

        self._print_final_summary()

    def _run_two_stage(self, tests: list[tuple[str, str, dict]], setups: list[str]):
        """Stage 1: Fast screening (e.g. 250 games). Stage 2: Deep verification (1500 games) for top 5."""
        stage1_games = self.args.fast_games
        stage2_games = self.args.confirm_games

        print(f"\n--- [KROK 1/2: SZYBKI PRZESIEW] Próba: {stage1_games} gier/setup ({len(tests)} wariantów) ---")
        task_list = [(t, stage1_games, self.args.seed, setups) for t in tests]
        results = self._execute_pool(task_list)

        base_s1 = results[0]
        # Collect all candidates that pass telemetry safety, sorted by delta in screening
        safe_candidates = []
        for r in results[1:]:
            delta = r["global_score"] - base_s1["global_score"]
            is_safe, _ = passes_telemetry_safety(r)
            if is_safe:
                safe_candidates.append(r)

        safe_candidates.sort(key=lambda x: x["global_score"] - base_s1["global_score"], reverse=True)

        if not safe_candidates:
            print("Brak bezpiecznych kandydatów w przesiewie.")
            return None, base_s1, None, results

        top_k = safe_candidates[: self.args.top_k]
        print(f"\n--- [KROK 2/2: PRECYZYJNA WERYFIKACJA] Badam TOP {len(top_k)} liderów na próbie {stage2_games} gier/setup ---")

        # Map back to test tuples
        test_dict = {t[0]: t for t in tests}
        verify_tests = [tests[0]] + [test_dict[r["id"]] for r in top_k]

        # Use Common Random Numbers (CRN) paired seed to eliminate external variance
        verify_tasks = [(t, stage2_games, self.args.seed, setups) for t in verify_tests]
        verified_results = self._execute_pool(verify_tasks)

        base_s2 = verified_results[0]
        verified_candidates = []

        for r in verified_results[1:]:
            delta = r["global_score"] - base_s2["global_score"]
            is_safe, safe_msg = passes_telemetry_safety(r)
            if is_safe and delta >= self.args.min_delta:
                verified_candidates.append(r)
            elif not is_safe:
                print(f"⚠️ Odrzucono kandydata [{r['id']}] z powodu telemetrii: {safe_msg}")
            else:
                print(f"⚪ Odrzucono kandydata [{r['id']}] po weryfikacji: brak zysku na dużej próbie (Δ {delta:+5.2f} pkt)")

        if not verified_candidates:
            print("Żaden z liderów nie przeszedł pomyślnie weryfikacji i testów bezpieczeństwa.")
            return None, base_s2, None, verified_results

        verified_candidates.sort(key=lambda x: x["global_score"] - base_s2["global_score"], reverse=True)
        best_res = verified_candidates[0]
        best_tuple = test_dict[best_res["id"]]

        return best_tuple, base_s2, best_res, verified_candidates

    def _run_direct_stage(self, tests: list[tuple[str, str, dict]], setups: list[str], games_per_setup: int):
        """Single stage full evaluation on full sample size (used for L1, L2, L4)."""
        print(f"\n--- [BEZPOŚREDNIA EWALUACJA ULTRA] Próba: {games_per_setup} gier/setup ({len(tests)} wariantów) ---")
        task_list = [(t, games_per_setup, self.args.seed, setups) for t in tests]
        results = self._execute_pool(task_list)

        base_res = results[0]
        candidates = []
        for r in results[1:]:
            delta = r["global_score"] - base_res["global_score"]
            is_safe, safe_msg = passes_telemetry_safety(r)
            if is_safe and delta >= self.args.min_delta:
                candidates.append(r)
            elif not is_safe:
                print(f"⚠️ Odrzucono kandydata [{r['id']}] z powodu telemetrii: {safe_msg}")
            else:
                print(f"⚪ Odrzucono kandydata [{r['id']}]: brak zysku na próbie {games_per_setup} gier (Δ {delta:+5.2f} pkt)")

        if not candidates:
            return None, base_res, None, results

        candidates.sort(key=lambda x: x["global_score"] - base_res["global_score"], reverse=True)
        best_res = candidates[0]
        test_dict = {t[0]: t for t in tests}
        best_tuple = test_dict[best_res["id"]]

        return best_tuple, base_res, best_res, candidates

    def _execute_pool(self, task_list: list) -> list[dict]:
        """Execute tasks using ProcessPoolExecutor with live counter."""
        results = []
        n_tasks = len(task_list)
        workers = min(self.args.workers, n_tasks)

        if workers > 1:
            with ProcessPoolExecutor(max_workers=workers) as executor:
                for idx, res in enumerate(executor.map(_run_single_test_task, task_list), 1):
                    results.append(res)
                    if idx % 10 == 0 or idx == n_tasks or idx == 1:
                        print(f"[{idx:3d}/{n_tasks:3d}] Postęp | Ostatni: {res['id']:<28} Score: {res['global_score']:5.1f} pkt", flush=True)
        else:
            for idx, task in enumerate(task_list, 1):
                res = _run_single_test_task(task)
                results.append(res)
                if idx % 10 == 0 or idx == n_tasks or idx == 1:
                    print(f"[{idx:3d}/{n_tasks:3d}] Postęp | Ostatni: {res['id']:<28} Score: {res['global_score']:5.1f} pkt", flush=True)

        return results

    def _print_final_summary(self):
        total_time = round((time.time() - self.start_time) / 60, 1)
        print("\n" + "═" * 71)
        print("        PODSUMOWANIE DZIAŁANIA SZALONEGO AUDYTORA")
        print("═" * 71)
        print(f"Łączny czas sesji:    {total_time} min ({round(total_time/60, 2)} h)")
        print(f"Wykonanych iteracji:  {self.total_iterations}")
        print(f"Wersja początkowa:    {self.initial_version}")
        print(f"Wersja końcowa:       {CONFIG.version}")
        print(f"Dziennik ewolucji:    {LOG_FILE_PATH}")
        print(f"Notatki balansu:      {BALANCE_NOTES_PATH}")
        print(f"Katalog archiwum:     {REPORTS_DIR / 'archive' / CONFIG.version}")
        print("═" * 71)


def main():
    parser = argparse.ArgumentParser(
        description="INQUISITIO-1492 — Szalony Audytor / Autonomous Balance Optimizer",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--mode", type=str, choices=["two-stage", "grand", "standard", "fast"], default="two-stage",
                        help="Tryb ewaluacji: two-stage (rekomendowany szybki przesiew + weryfikacja), grand (3k gier), standard (500), fast (250)")
    parser.add_argument("--fast-games", type=int, default=1000, help="Liczba gier/setup w kroku 1 przesiewu (dla two-stage)")
    parser.add_argument("--confirm-games", type=int, default=5000, help="Liczba gier/setup w kroku 2 weryfikacji (dla two-stage)")
    parser.add_argument("--top-k", type=int, default=20, help="Liczba liderów weryfikowanych w kroku 2")
    parser.add_argument("--hours", type=float, default=None, help="Maksymalny czas działania w godzinach (np. 4.0)")
    parser.add_argument("--max-iters", type=int, default=None, help="Maksymalna liczba iteracji optymalizatora")
    parser.add_argument("--min-delta", type=float, default=0.05, help="Minimalny zysk punktowy (delta global) wymagany do zapisu (domyślnie >= 0.05)")
    parser.add_argument("--level", type=str, choices=["all", "1", "2", "3", "4"], default="all", help="Filtruj poziomy testów")
    parser.add_argument("--param", type=str, default="all", help="Parametry kart dla Poziomu 3 (cost, heresy, target_heresy, gold, all)")
    parser.add_argument("--card", type=str, default=None, help="Ogranicz poziom 3 do konkretnej karty (np. so-04)")
    parser.add_argument("--seed", type=int, default=42, help="Początkowe ziarno RNG")
    parser.add_argument("--workers", type=int, default=os.cpu_count() or 4, help="Liczba równoległych procesów CPU")
    parser.add_argument("--dry-run", action="store_true", help="Tryb symulacji bez zapisu zmian do game_config.yaml")
    parser.add_argument("--full-audit-on-finish", action="store_true", help="Uruchom pełny pakiet 6 raportów po zakończeniu pracy optymalizatora")

    args = parser.parse_args()
    auditor = AutoBalancer(args)
    auditor.run()


if __name__ == "__main__":
    main()
