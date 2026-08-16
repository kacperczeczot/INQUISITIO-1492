#!/usr/bin/env python3
"""INQUISITIO-1492 — SZALONY AUDYTOR / PROGRESSIVE BEAM BALANCE OPTIMIZER.

Autonomiczny optymalizator balansu oparty na Progresywnym Przeszukiwaniu Wiązkowym (Progressive Beam Search).
Działa jednocześnie na wszystkich poziomach gry (L1 Rdzeń + L2 Zwycięstwa + L3 Karty + L4 Warianty):
  1. Faza 1 (1D): Przesiew wszystkich atomowych modyfikacji L1–L4 (min. 1000 gier) -> TOP 12 Finalistów (min. 5000 gier CRN).
  2. Jeśli brak dodatniej delty -> wybiera TOP 8 kandydatów i wchodzi w Fazę 2 (Wiązki 2D: TOP 8 x Wszystkie mechaniki L1-L4).
  3. Jeśli brak dodatniej delty w Fazie 2 -> wybiera TOP 8 par i wchodzi w Fazę 3 (Wiązki 3D / Trójki).
  4. Schodzi rekurencyjnie bez limitu faz, dopóki nie przełamie plateau.
  5. Po znalezieniu zyskownej kombinacji (1D, 2D, 3D...) wdraża Patch, aktualizuje raporty i resetuje wiązkę do Fazy 1.

Pełna automatyzacja dokumentacji:
  - raport_telemetrii.md (oraz archiwum wersji)
  - raport_optymalizacji.md (oraz archiwum wersji)
  - playtesting/balance-notes.md (wpisy Patch Notes + Stan Zmierzony)
  - auto_balancer_log.md
  - Pełna synchronizacja kart, katalogu i księgi zasad (sync_config.py)
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

# Import test builders
import audit_level1
import audit_level2
import audit_level3
import audit_level4

REPORTS_DIR = Path(__file__).resolve().parent.parent.parent / "playtesting" / "sim-reports"
LOG_FILE_PATH = REPORTS_DIR / "logs" / "auto_balancer_log.md"
BALANCE_NOTES_PATH = Path(__file__).resolve().parent.parent.parent / "playtesting" / "balance-notes.md"

FACTION_NAMES = {
    FactionId.SWIETE_OFICJUM: "SO",
    FactionId.CIENIE_AL_ANDALUS: "CAA",
    FactionId.KORONA_BORGIOWIE: "KB",
    FactionId.KABALA_TOLEDO: "KT",
    FactionId.GILDIA_CIENI: "GC",
}


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


def _run_single_test_task(task_args: tuple[tuple[str, str, dict], int, int, list[str]]) -> dict:
    """Execute a single candidate rule across all setups."""
    (rule_id, rule_name, rule_params), games_per_setup, seed, setups = task_args
    t_rule = time.time()

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
    dt = round(time.time() - t_rule, 2)

    n_sum = len(summaries)
    eras_avg = sum(s.eras_avg for s in summaries) / n_sum
    eras_min = min(s.eras_min for s in summaries)
    eras_max = max(s.eras_max for s in summaries)

    deadlock_pct = (sum(s.eras_limit_pct for s in summaries) / n_sum) * 100.0
    poverty_pct = (sum(s.passes_forced_pct for s in summaries) / n_sum) * 100.0

    autodafe_avg = sum(s.autodafe_avg for s in summaries) / n_sum
    acc_avg = sum(s.accusations_avg for s in summaries) / n_sum
    gold_avg = sum(s.avg_gold_end for s in summaries) / n_sum

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
        "eras_avg": eras_avg, "eras_min": eras_min, "eras_max": eras_max,
        "deadlock_pct": deadlock_pct,
        "poverty_pct": poverty_pct,
        "autodafe_avg": autodafe_avg,
        "acc_avg": acc_avg,
        "gold_avg": gold_avg,
    }


def generate_all_atomic_candidates() -> list[tuple[str, str, dict]]:
    """Builds the full pool of atomic candidates across L1, L2, L3, and L4."""
    tests = []

    # Level 1 (Core System Parameters)
    l1 = [t for t in audit_level1.build_level1_tests() if t[0] != "L1_BAZA"]
    tests.extend(l1)

    # Level 2 (Faction Victory Conditions)
    l2 = [t for t in audit_level2.build_level2_tests() if t[0] != "L2_BAZA"]
    tests.extend(l2)

    # Level 3 (Card Parameters: cost, heresy, gold, target_heresy)
    l3 = [t for t in audit_level3.build_level3_tests(param_filter="cost,heresy,gold,target_heresy") if t[0] != "L3_BAZA"]
    tests.extend(l3)

    # Level 4 (Niche Variants & Edicts)
    l4 = [t for t in audit_level4.build_level4_tests() if t[0] != "L4_BAZA"]
    tests.extend(l4)

    return tests


def merge_mutations(m1: tuple[str, str, dict], m2: tuple[str, str, dict]) -> tuple[str, str, dict] | None:
    """Merges two mutations into a composite mutation (e.g. 2D pair or 3D triple)."""
    id1, name1, p1 = m1
    id2, name2, p2 = m2

    # Check for direct conflicts on atomic keys
    keys1 = set(p1.keys()) - {"card_overrides"}
    keys2 = set(p2.keys()) - {"card_overrides"}
    if keys1 & keys2:
        return None  # Direct conflict on same system parameter

    # Check for conflicts on same card parameters
    cards1 = p1.get("card_overrides", {})
    cards2 = p2.get("card_overrides", {})
    for cid, c_dict in cards2.items():
        if cid in cards1:
            if set(c_dict.keys()) & set(cards1[cid].keys()):
                return None  # Conflict on same card parameter

    combined_id = f"{id1}__{id2}"
    combined_name = f"{name1} + {name2}"

    merged_params = copy.deepcopy(p1)
    for k, v in p2.items():
        if k != "card_overrides":
            merged_params[k] = v
        else:
            if "card_overrides" not in merged_params:
                merged_params["card_overrides"] = {}
            for cid, c_dict in v.items():
                if cid in merged_params["card_overrides"]:
                    merged_params["card_overrides"][cid].update(c_dict)
                else:
                    merged_params["card_overrides"][cid] = copy.deepcopy(c_dict)

    return (combined_id, combined_name, merged_params)


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

        eras_opt = "🟢" if 5.0 <= avg_eras <= 6.5 else ("🟡" if 4.5 <= avg_eras <= 7.0 else "🔴")
        deadlock_opt = "🟢" if deadlock_pct <= 5.0 else ("🟡" if deadlock_pct <= 10.0 else "🔴")
        poverty_opt = "🟢" if poverty_pct <= 28.0 else ("🟡" if poverty_pct <= 32.0 else "🔴")
        autodafe_opt = "🟢" if 0.7 <= autodafe_avg <= 1.8 else ("🟡" if 0.5 <= autodafe_avg <= 2.0 else "🔴")
        acc_opt = "🟢" if 2.0 <= accusations_avg <= 4.5 else ("🟡" if 1.5 <= accusations_avg <= 5.0 else "🔴")

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

        eval_str = "🟢 ZBALANSOWANY" if d['score'] >= 90.0 else ("🟡 AKCEPTOWALNY" if d['score'] >= 75.0 else ("🟠 WYMAGA UWAGI" if d['score'] >= 60.0 else "🔴 ODCHYLONY"))
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

    return save_and_archive_report(report_lines, "raport_telemetrii.md")


def generate_and_save_optimization_report(
    old_version: str,
    new_version: str,
    iteration: int,
    phase: int,
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
        f"# Raport Optymalizacji Balansu (Szalony Audytor — Progressive Beam) — Wersja {new_version} (Iteracja #{iteration}, Faza {phase}D)",
        "",
        f"**Wersja Poprzednia:** `{old_version}` (`{base_res['global_score']:.1f} pkt`) → **Nowa Wersja:** `{new_version}` (`{best_res['global_score']:.1f} pkt`)",
        f"**Data:** {datetime.now().strftime('%Y-%m-%d %H:%M')} | **Czas Trwania Iteracji:** {elapsed_iter:.1f}s | **Zysk Global:** `{delta_str} pkt`",
        "",
        "## 1. Wprowadzona Zmiana i Wynik Balansu",
        f"- **Wybrany Wariant ({phase}D):** `{rule_id}` — **{best_res['name']}**",
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
        "## 2. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści)",
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
        f"## 📊 Stan zmierzony — {today} (Szalony Audytor Progressive Beam, seed 42, warstwa C)\n\n"
        f"YAML po Patch {new_version} ({change_desc}).\n\n"
        f"- **Global Game Balance Score:** **`{best_res['global_score']:.1f} / 100.0 pkt` 🟢 (Auto-Optimizer Optimum)**\n"
        f"- **3p Avg Score:** **`{best_res['cat_scores'].get('3p',0.0):.1f} / 100.0 pkt` 🟢**\n"
        f"- **4p Avg Score:** **`{best_res['cat_scores'].get('4p',0.0):.1f} / 100.0 pkt` 🟢**\n"
        f"- **5p Avg Score:** **`{best_res['cat_scores'].get('5p',0.0):.1f} / 100.0 pkt` 🟢**"
    )
    if re.search(measured_pattern, content):
        content = re.sub(measured_pattern, new_measured_block, content, count=1)

    BALANCE_NOTES_PATH.write_text(content, encoding="utf-8")


def log_auto_balancer_iteration(
    log_path: Path,
    iteration: int,
    phase: int,
    old_version: str,
    new_version: str,
    desc: str,
    rule_id: str,
    base_res: dict,
    best_res: dict,
    elapsed_iter: float,
):
    """Appends an iteration entry to auto_balancer_log.md."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    if not log_path.exists():
        headers = [
            "# Dziennik Optymalizacji Szalony Audytor (Progressive Beam Search)",
            "",
            "Rejestr wdrożonych patchów i postępów w kierunku globalnego optimum 100%.",
            "",
            "| Iteracja | Faza | Data i Czas | Wersja | Wprowadzona Zmiana / Wiązka | Global Score | 3p | 4p | 5p | Deadlocks % | Pas Biedy % | Czas |",
            "| :---: | :---: | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
        ]
        log_path.write_text("\n".join(headers) + "\n", encoding="utf-8")

    d_glob = best_res["global_score"] - base_res["global_score"]
    delta_str = f"+{d_glob:.1f}" if d_glob > 0 else f"{d_glob:.1f}"

    score_col = f"{base_res['global_score']:.1f} → **{best_res['global_score']:.1f}** (`{delta_str}`)"
    p3_col = f"{base_res['cat_scores'].get('3p',0):.1f} → {best_res['cat_scores'].get('3p',0):.1f}"
    p4_col = f"{base_res['cat_scores'].get('4p',0):.1f} → {best_res['cat_scores'].get('4p',0):.1f}"
    p5_col = f"{base_res['cat_scores'].get('5p',0):.1f} → {best_res['cat_scores'].get('5p',0):.1f}"

    row = (
        f"| #{iteration} | {phase}D | {datetime.now().strftime('%Y-%m-%d %H:%M')} | `{old_version}` → `{new_version}` | "
        f"**{desc}** (`{rule_id}`) | {score_col} | {p3_col} | {p4_col} | {p5_col} | "
        f"{best_res['deadlock_pct']:.1f}% | {best_res['poverty_pct']:.1f}% | {elapsed_iter:.1f}s |"
    )

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(row + "\n")


class ProgressiveBeamAutoBalancer:
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

    def _execute_pool(self, task_func, task_list: list, label: str = "Testy") -> list[dict]:
        total = len(task_list)
        if total == 0:
            return []

        workers = min(self.args.workers, total)
        if workers <= 1:
            results = []
            t0 = time.time()
            for idx, t in enumerate(task_list, 1):
                res = task_func(t)
                results.append(res)
                elapsed = time.time() - t0
                rate = idx / elapsed if elapsed > 0 else 0
                eta_s = (total - idx) / rate if rate > 0 else 0
                eta_str = f"{int(eta_s // 60)}m {int(eta_s % 60):02d}s" if eta_s >= 60 else f"{int(eta_s)}s"
                sys.stdout.write(f"\r⏳ [{label}] [{idx:4d}/{total:4d}] ({idx*100.0/total:5.1f}%) | {rate:4.1f} zad/s | ETA: {eta_str:<8s}")
                sys.stdout.flush()
            sys.stdout.write("\n")
            return results

        results = []
        t0 = time.time()
        with ProcessPoolExecutor(max_workers=workers) as executor:
            from concurrent.futures import as_completed
            future_to_task = {executor.submit(task_func, t): t for t in task_list}
            best_so_far = None

            for idx, future in enumerate(as_completed(future_to_task), 1):
                res = future.result()
                results.append(res)
                if best_so_far is None or res["global_score"] > best_so_far["global_score"]:
                    best_so_far = res

                elapsed = time.time() - t0
                rate = idx / elapsed if elapsed > 0 else 0
                eta_s = (total - idx) / rate if rate > 0 else 0
                eta_str = f"{int(eta_s // 60)}m {int(eta_s % 60):02d}s" if eta_s >= 60 else f"{int(eta_s)}s"
                lead_id = best_so_far['id'][:26] if best_so_far else "-"
                lead_sc = f"{best_so_far['global_score']:.1f}" if best_so_far else "-"
                sys.stdout.write(f"\r⏳ [{label}] [{idx:4d}/{total:4d}] ({idx*100.0/total:5.1f}%) | {rate:4.1f} zad/s | ETA: {eta_str:<7s} | Lider: {lead_id} ({lead_sc} pkt)  ")
                sys.stdout.flush()

        sys.stdout.write(f"\n   ✔ Ukończono {total} zadań w {round(time.time() - t0, 1)}s.\n")
        return results

    def run(self):
        print("═══════════════════════════════════════════════════════════════════════")
        print("  INQUISITIO-1492 — SZALONY AUDYTOR (Progressive Beam Search 1D/2D/3D)  ")
        print("  3-Stopniowy Lejek Sukcesywnej Selekcji (Coarse → Deep → Ultra)        ")
        print("═══════════════════════════════════════════════════════════════════════")
        print(f"Bieżąca wersja bazowa:      {CONFIG.version}")
        print(f"Maksymalny czas sesji:      {self.args.hours if self.args.hours else 'Brak limitu (do optimum)'} godz.")
        print(f"Maksymalnie patchów:        {self.args.max_iters if self.args.max_iters else 'Brak (do optimum)'}")
        print(f"Etap 1 (Szybki przesiew):   {self.args.fast_games} gier/setup (wszyscy kandydaci)")
        print(f"Etap 2 (Głęboki przesiew):  {self.args.screen_games} gier/setup (TOP {self.args.top_semifinalists} półfinalistów)")
        print(f"Etap 3 (Weryfikacja Ultra): {self.args.confirm_games} gier/setup (TOP {self.args.top_k} finalistów)")
        print(f"Szerokość Wiązki:           K = {self.args.beam_width} (nasiona do wyższej fazy)")
        print(f"Wątki procesora:            {self.args.workers}")
        print(f"Dziennik operacji:          {LOG_FILE_PATH}")
        print("═══════════════════════════════════════════════════════════════════════\n")

        setups = sorted(SETUP_PRESETS.keys())
        time_limit_sec = (self.args.hours * 3600) if self.args.hours else None

        current_phase = 1
        beam_seeds: list[tuple[str, str, dict]] = []

        while not self.stop_requested:
            # 1. Check time / iteration limit
            if time_limit_sec and (time.time() - self.start_time) >= time_limit_sec:
                print(f"\n⏱️ Osiągnięto limit czasu sesji ({self.args.hours}h). Kończę pracę.")
                break

            if self.args.max_iters and self.total_iterations >= self.args.max_iters:
                print(f"\n🔢 Osiągnięto maksymalną liczbę udanych patchów ({self.args.max_iters}). Kończę pracę.")
                break

            iter_start = time.time()

            # 2. Run current 16-setup baseline measurement
            print(f"\n{'='*71}")
            print(f"🔍 [POMIAR BAZOWY] Diagnoza 16 setupów (Próba: {self.args.confirm_games} gier/setup)...")
            base_task = ((("BASE", "Bieżący stan gry", {}), self.args.confirm_games, self.args.seed, setups),)
            base_res = self._execute_pool(_run_single_test_task, [base_task[0]], label="Baza 16 Setupów")[0]

            print(f"   📊 Global Balance Score: {color_score(base_res['global_score'], bold=True)} pkt")
            print(f"   🎯 3p: {base_res['cat_scores'].get('3p',0):.1f} | 4p: {base_res['cat_scores'].get('4p',0):.1f} | 5p: {base_res['cat_scores'].get('5p',0):.1f} pkt")
            print(f"   ⏱️ Średnia Er: {base_res['eras_avg']:.2f} | Deadlocks: {base_res['deadlock_pct']:.1f}% | Pas Biedy: {base_res['poverty_pct']:.1f}%")

            # 3. Generate candidate pool for current phase
            atomic_pool = generate_all_atomic_candidates()

            if current_phase == 1 or not beam_seeds:
                print(f"\n🌐 [FAZA 1D] Generuję pełną pulę atomową wszystkich poziomów L1–L4...")
                candidate_pool = atomic_pool
            else:
                print(f"\n🌐 [FAZA {current_phase}D] Generuję wiązki {current_phase}D (TOP {len(beam_seeds)} nasion × {len(atomic_pool)} atomowych mechanik)...")
                composite_pool = []
                for seed_mut in beam_seeds:
                    for atomic_mut in atomic_pool:
                        merged = merge_mutations(seed_mut, atomic_mut)
                        if merged:
                            composite_pool.append(merged)

                # Deduplicate by ID
                seen_ids = set()
                candidate_pool = []
                for c in composite_pool:
                    if c[0] not in seen_ids:
                        seen_ids.add(c[0])
                        candidate_pool.append(c)

            print(f"   🧬 Wygenerowano {len(candidate_pool)} unikalnych kandydatów w Fazie {current_phase}D.")
            cand_dict = {c[0]: c for c in candidate_pool}

            # 4. ETAP 1/3: SZYBKI PRZESIEW ZGRUBNY (Coarse Screen)
            print(f"\n--- [ETAP 1/3: SZYBKI PRZESIEW ZGRUBNY] Testuję {len(candidate_pool)} kandydatów ({self.args.fast_games} gier/setup) ---")
            stage1_tasks = [((c[0], c[1], c[2]), self.args.fast_games, self.args.seed, setups) for c in candidate_pool]
            stage1_results = self._execute_pool(_run_single_test_task, stage1_tasks, label=f"Przesiew 1/3 ({current_phase}D)")

            # Sort by global score descending
            stage1_results.sort(key=lambda r: r["global_score"], reverse=True)

            # Pick TOP semifinalists for Stage 2
            n_semifinalists = min(self.args.top_semifinalists, len(stage1_results))
            semifinalist_results = stage1_results[:n_semifinalists]
            semifinalist_candidates = [cand_dict[r["id"]] for r in semifinalist_results]

            # 5. ETAP 2/3: GŁĘBOKI PRZESIEW I KONSOLIDACJA (Refined Screen)
            print(f"\n--- [ETAP 2/3: GŁĘBOKI PRZESIEW] Badam TOP {len(semifinalist_candidates)} półfinalistów ({self.args.screen_games} gier/setup) ---")
            stage2_tasks = [((c[0], c[1], c[2]), self.args.screen_games, self.args.seed, setups) for c in semifinalist_candidates]
            stage2_results = self._execute_pool(_run_single_test_task, stage2_tasks, label=f"Przesiew 2/3 ({current_phase}D)")

            # Sort by global score descending
            stage2_results.sort(key=lambda r: r["global_score"], reverse=True)

            # Pick TOP finalists for Stage 3
            n_finalists = min(self.args.top_k, len(stage2_results))
            finalist_results = stage2_results[:n_finalists]
            finalist_candidates = [cand_dict[r["id"]] for r in finalist_results]

            # 6. ETAP 3/3: WERYFIKACJA ULTRA (Ultra Verification)
            print(f"\n--- [ETAP 3/3: WERYFIKACJA ULTRA] Weryfikuję TOP {len(finalist_candidates)} finalistów ({self.args.confirm_games} gier/setup) ---")
            stage3_tasks = [((c[0], c[1], c[2]), self.args.confirm_games, self.args.seed, setups) for c in finalist_candidates]
            stage3_results = self._execute_pool(_run_single_test_task, stage3_tasks, label=f"Weryfikacja 3/3 ({current_phase}D)")

            # Rank verified finalists
            stage3_results.sort(key=lambda r: r["global_score"], reverse=True)

            print(f"\n📊 [WYNIKI WERYFIKACJI FINALISTÓW]")
            for idx, r in enumerate(stage3_results, 1):
                d_g = r["global_score"] - base_res["global_score"]
                is_safe, msg = passes_telemetry_safety(r)
                sign = f"+{d_g:.2f}" if d_g > 0 else f"{d_g:.2f}"
                print(f"   #{idx:2d} [{r['id'][:42]}...] Global: {base_res['global_score']:.1f} → {r['global_score']:.1f} (Δ {sign}) | {msg}")

            # Check if any finalist has real positive gain
            accepted_candidate = None
            best_ver_res = None

            for ver_res in stage3_results:
                d_global = ver_res["global_score"] - base_res["global_score"]
                is_safe, safe_msg = passes_telemetry_safety(ver_res)

                if is_safe and d_global >= self.args.min_delta:
                    accepted_candidate = cand_dict[ver_res["id"]]
                    best_ver_res = ver_res
                    break

            # 7. Handle Outcome
            if accepted_candidate and best_ver_res is not None:
                # SUCCESS: Apply Patch!
                self.total_iterations += 1
                rule_id, rule_name, rule_params = accepted_candidate

                with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
                    raw_cfg = yaml.safe_load(f)

                old_version = raw_cfg.get("version", "v0.32")
                mod_cfg, change_desc = apply_mutation_to_config(raw_cfg, rule_id, rule_params)

                if self.args.dry_run:
                    print(f"\n[DRY RUN] Zaakceptowano by modyfikację {current_phase}D: {change_desc}")
                    current_phase += 1
                else:
                    new_version, saved_path = save_config_and_bump_version(mod_cfg, _CONFIG_PATH, bump_version=True)
                    iter_elapsed = round(time.time() - iter_start, 2)

                    print(f"\n🎉 [ZAAKCEPTOWANO PATCH #{self.total_iterations} — FAZA {current_phase}D]")
                    print(f"   Wersja:        `{old_version}` → **`{new_version}`**")
                    print(f"   Modyfikacja:   {change_desc}")
                    print(f"   Global Score:  {base_res['global_score']:.1f} → **{best_ver_res['global_score']:.1f} pkt** (Δ {best_ver_res['global_score'] - base_res['global_score']:+.2f} pkt)")

                    # Full Documentation Suite
                    print(f"\n📄 [DOKUMENTACJA] Generuję raporty i archiwum wersji {new_version}...")

                    log_auto_balancer_iteration(
                        LOG_FILE_PATH,
                        self.total_iterations,
                        current_phase,
                        old_version,
                        new_version,
                        change_desc,
                        rule_id,
                        base_res,
                        best_ver_res,
                        iter_elapsed,
                    )

                    opt_out, opt_arch = generate_and_save_optimization_report(
                        old_version,
                        new_version,
                        self.total_iterations,
                        current_phase,
                        base_res,
                        best_ver_res,
                        stage3_results,
                        change_desc,
                        rule_id,
                        iter_elapsed,
                    )
                    print(f"   ✔ Zapisano raport optymalizacji: {opt_out.name} (archiwum: {opt_arch})")

                    telem_out, telem_arch = generate_and_save_telemetry_report(
                        new_version,
                        games_per_setup=self.args.screen_games,
                        seed=self.args.seed,
                    )
                    print(f"   ✔ Zaktualizowano raport telemetrii: {telem_out.name} (archiwum: {telem_arch})")

                    update_balance_notes(old_version, new_version, change_desc, rule_id, base_res, best_ver_res)
                    print(f"   ✔ Zaktualizowano notatki balansu: {BALANCE_NOTES_PATH.name}")

                    print("   🔄 Synchronizuję dokumentację kart i reguł...")
                    subprocess.run([sys.executable, str(TOOLS_SIM_DIR.parent / "sync_config.py")])
                    print("   ✔ Zaktualizowano katalog kart, opisy markdown i card-editor.")

                    # RESET BEAM TO PHASE 1 AFTER SUCCESS
                    current_phase = 1
                    beam_seeds.clear()

            else:
                # NO POSITIVE GAIN IN CURRENT PHASE -> ESCALATE TO PHASE D+1!
                print(f"\n⚪ Brak wariantu z dodatnim zyskiem (Δ ≥ +{self.args.min_delta} pkt) w Fazie {current_phase}D.")
                
                # Pick TOP K beam seeds from Stage 3 results to expand in next phase
                top_beam_results = stage3_results[: self.args.beam_width]
                beam_seeds = [cand_dict[r["id"]] for r in top_beam_results]

                current_phase += 1
                print(f"🔄 Kwalifikuję TOP {len(beam_seeds)} nasion wiązki i ESKALUJĘ DO FAZY {current_phase}D...\n")

        print(f"\n═══════════════════════════════════════════════════════════════════════")
        print(f"   SZALONY AUDYTOR ZAKOŃCZYŁ SESJĘ. ŁĄCZNIE WPROWADZONO {self.total_iterations} PATCHY.")
        print(f"═══════════════════════════════════════════════════════════════════════\n")


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 Szalony Audytor — Progressive Beam Search Optimizer (3-Stage Funnel)")
    parser.add_argument("--hours", type=float, default=None, help="Maksymalny czas działania w godzinach (np. 8.0 na noc)")
    parser.add_argument("--max-iters", type=int, default=None, help="Maksymalna liczba udanych patchów przed zatrzymaniem")
    parser.add_argument("--fast-games", type=int, default=200, help="Liczba gier w Etapie 1 (szybki przesiew, min. 100, domyślnie: 200)")
    parser.add_argument("--screen-games", type=int, default=1000, help="Liczba gier w Etapie 2 (głęboki przesiew, min. 500, domyślnie: 1000)")
    parser.add_argument("--confirm-games", type=int, default=5000, help="Liczba gier w Etapie 3 (weryfikacja ultra, min. 3000, domyślnie: 5000)")
    parser.add_argument("--top-semifinalists", type=int, default=48, help="Liczba półfinalistów sprawdzanych w Etapie 2 (domyślnie: 48)")
    parser.add_argument("--top-k", type=int, default=24, help="Liczba finalistów sprawdzanych w Etapie 3 (domyślnie: 24)")
    parser.add_argument("--beam-width", type=int, default=8, help="Liczba najlepszych kandydatów kwalifikowanych do nasion kolejnej fazy wiązek (domyślnie: 8)")
    parser.add_argument("--min-delta", type=float, default=0.05, help="Minimalny zysk globalny wymagany do wdrożenia patcha (pkt, domyślnie: 0.05)")
    parser.add_argument("--workers", type=int, default=min(os.cpu_count() or 4, 10), help="Liczba procesów równoległych")
    parser.add_argument("--seed", type=int, default=42, help="Ziarno generatora liczb losowych")
    parser.add_argument("--dry-run", action="store_true", help="Tryb symulacji bez zapisywania zmian do game_config.yaml")

    args = parser.parse_args()

    if args.fast_games < 100:
        print("⚠️ Podwyższam fast-games do wymaganego minimum 100 gier.")
        args.fast_games = 100
    if args.screen_games < 500:
        print("⚠️ Podwyższam screen-games do wymaganego minimum 500 gier.")
        args.screen_games = 500
    if args.confirm_games < 3000:
        print("⚠️ Podwyższam confirm-games do wymaganego minimum 3000 gier.")
        args.confirm_games = 3000

    auditor = ProgressiveBeamAutoBalancer(args)
    auditor.run()


if __name__ == "__main__":
    main()
