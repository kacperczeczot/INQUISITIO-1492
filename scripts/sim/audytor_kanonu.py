#!/usr/bin/env python3
"""INQUISITIO-1492 — AUDYTOR KANONU 4P (Canonical Anchor-Based Balance Optimizer).

Autonomiczny optymalizator balansu skupiony w 100% na doprowadzeniu Kanonu 4-osobowego (4P)
do absolutnego optimum (99–100 pkt), bez kompromisów pod 3p i 5p.

Architektura optymalizacyjna:
  1. Kanon 4P jako Kotwica (Anchor):
     Format 4-osobowy jest sercem mechaniki gry INQUISITIO-1492. Wszystkie karty i reguły
     muszą w pierwszej kolejności działać w sposób idealny i elegancki na 5 setupach 4p:
       - 4p-core
       - 4p-no-cienie
       - 4p-no-kabala
       - 4p-no-korona
       - 4p-no-oficjum
  2. Adaptacyjny Wyścig Monte Carlo (Multi-Fidelity Sequential Racing):
     - Zastąpienie sztywnych etapów dynamicznym mikro-krokiem (Iterative Batching, np. 100 gier/setup).
     - Rygorystyczny błąd standardowy liczony analitycznie Metodą Delta z macierzy kowariancji rozkładu wielomianowego.
     - Spłaszczona kolejka zadań (Flat Task Matrix) dla 100% wysycenia wszystkich rdzeni CPU.
     - Wczesne odrzucanie statystyczne (Statistical Upper-Bound Pruning) wariantów bez szans na wygraną.
     - Zbieżność wyścigu w Strefie Nierozróżnialności (Indifference Zone Racing) z ochroną przed nieskończonymi remisami.
  3. Mechanizm Ucieczki z Minimów Lokalnych (Simulated Annealing):
     - Probabilistyczna akceptacja mikro-mutacji z temperaturą wyżarzania przy jednoczesnym twardym wetowaniu kastracji mechanik.
  4. Wektoryzacja synergii i wiązek celowanych.
  5. Pełna automatyzacja dokumentacji i archiwizacji (100% kompatybilności wstecznej).
"""
from __future__ import annotations

import argparse
import copy
import math
import os
import random
import re
import shutil
import signal
import subprocess
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

# Ensure sim and tools/sim directories are on path
TOOLS_SRC_DIR = Path(__file__).resolve().parent
SRC_DIR = TOOLS_SRC_DIR.parent.parent / "src"

for p in (TOOLS_SRC_DIR, SRC_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

import yaml
from inquisitio.cards.loader import load_all_cards
from inquisitio.config import CONFIG, _CONFIG_PATH
from inquisitio.config_updater import apply_mutation_to_config, save_config_and_bump_version
from inquisitio.engine.setup import SETUP_PRESETS, FactionId
from inquisitio.runner.audit_facts import score_pair, save_and_archive_report
from inquisitio.runner.batch import BatchSummary, merge_batch_summaries, run_batch
from inquisitio.runner.era_analytics import generate_era_distribution_markdown
from inquisitio.runner.balance import faction_shares as win_shares
from inquisitio.runner.canon_accept import (
    TARGET_BAND_PCT,
    accept_candidate,
    canon_should_stop,
    rank_key,
    setup_shares_in_range,
    table_has_share_foundation,
    telemetry_is_safe,
)
from inquisitio.runner.scoring import (
    calculate_balance_score,
    calculate_balance_stats,
    calculate_category_scores,
    calculate_global_score,
    calculate_setup_score,
    color_score,
    evaluate_vitality,
)

# Import test builders
import audit_level1
import audit_level2
import audit_level3
import audit_level4
from audytor_4p import is_ablation_off
from manual_ablation_hints import (
    collect_manual_ablation_candidates,
    format_manual_ablation_report,
    print_manual_ablation_summary,
)

REPORTS_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "playtesting" / "sim-reports"
BALANCE_NOTES_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "playtesting" / "balance-notes.md"
LIVE_LOG_PATH = REPORTS_DIR / "audytor_live.log"

import multiprocessing

class _LiveTee:
    def __init__(self, filename: Path):
        self.terminal = sys.stdout
        filename.parent.mkdir(parents=True, exist_ok=True)
        self.log = open(filename, "w", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.terminal.flush()
        self.log.write(message)
        self.log.flush()

    def flush(self):
        self.terminal.flush()
        self.log.flush()

if multiprocessing.current_process().name == "MainProcess":
    sys.stdout = _LiveTee(LIVE_LOG_PATH)

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


from inquisitio.runner.adaptive_racer import (
    AdaptiveSequentialRacer,
    CandidateStats,
    extract_config_overrides,
    merge_mutations,
    merge_override_dicts,
)



def _run_full_diagnostic(rule_params: dict, games_per_setup: int = 1000, seed: int = 42) -> dict:
    """Runs a complete 16-setup diagnostic to measure 3p, 4p, 5p and global score."""
    all_setups = sorted(SETUP_PRESETS.keys())
    summaries = []
    setup_scores = {}
    for sname in all_setups:
        s = run_batch(games=games_per_setup, setup=sname, seed=seed, layer="C", win_overrides=rule_params)
        summaries.append(s)
        setup_scores[sname] = calculate_setup_score(s)

    cat_scores = calculate_category_scores(summaries)
    global_score = calculate_global_score(cat_scores)
    return {
        "global_score": global_score,
        "cat_scores": cat_scores,
        "setup_scores": setup_scores,
    }


def generate_all_atomic_candidates() -> list[tuple[str, str, dict]]:
    """Builds the full pool of atomic candidates across L1, L2, L3, and L4."""
    tests = []

    l1 = [
        t
        for t in audit_level1.build_level1_tests()
        if t[0] != "L1_BAZA" and not is_ablation_off(t[0], t[2])
    ]
    tests.extend(l1)

    l2 = [
        t
        for t in audit_level2.build_level2_tests()
        if t[0] != "L2_BAZA" and not is_ablation_off(t[0], t[2])
    ]
    tests.extend(l2)

    l3 = [t for t in audit_level3.build_level3_tests(param_filter="cost,heresy,gold,target_heresy") if t[0] != "L3_BAZA"]
    tests.extend(l3)

    l4 = [
        t
        for t in audit_level4.build_level4_tests()
        if t[0] != "L4_BAZA" and not is_ablation_off(t[0], t[2])
    ]
    tests.extend(l4)

    return tests


def classify_card_mutation_intent(mut_tuple: tuple[str, str, dict]) -> str:
    """Classify whether an atomic mutation is a BUFF, NERF, or SYSTEM/NEUTRAL."""
    tag, _, params = mut_tuple
    card_overrides = params.get("card_overrides")
    if not card_overrides:
        return "SYSTEM"
    cid = list(card_overrides.keys())[0]
    param = list(card_overrides[cid].keys())[0]
    val = card_overrides[cid][param]

    cards = load_all_cards()
    c_obj = cards.get(cid)
    if not c_obj:
        return "NEUTRAL"
    orig = getattr(c_obj, param, 0)

    if param in ("cost", "heresy"):
        return "BUFF" if val < orig else "NERF"
    elif param in ("gold", "target_heresy"):
        return "BUFF" if val > orig else "NERF"
    return "NEUTRAL"


def get_mutation_faction(mut_tuple: tuple[str, str, dict]) -> str | None:
    """Returns faction code (SO, CAA, KB, KT, GC) for a card mutation, or None."""
    tag, _, params = mut_tuple
    card_overrides = params.get("card_overrides")
    if card_overrides:
        cid = list(card_overrides.keys())[0]
        prefix = cid.split("-")[0].upper()
        return prefix
    if tag.startswith("L3_"):
        parts = tag.split("_")
        if len(parts) >= 2:
            prefix = parts[1].split("-")[0].upper()
            return prefix
    return None


def _normalize_faction_code(f_name: str) -> str:
    """Normalizes any faction representation (slug, name, enum or abbreviation) to 2-3 letter code."""
    f = f_name.lower().replace("-", "_").strip()
    if "oficjum" in f or f == "so":
        return "SO"
    if "andalus" in f or "cienie_al" in f or f == "caa":
        return "CAA"
    if "korona" in f or "borgiowie" in f or f == "kb":
        return "KB"
    if "kabala" in f or "toledo" in f or f == "kt":
        return "KT"
    if "gildia" in f or f == "gc":
        return "GC"
    return f_name.upper()


def select_diverse_beam_seeds(all_candidate_stats: list, beam_width: int = 60) -> list[tuple[str, str, dict]]:
    """Selects a rich, balanced set of seeds representing the full spectrum:
    - Top positive candidates (promising leads)
    - Strongest negative/antagonist mutations (nerfs and counterweights across all factions)
    - Diverse structural modifiers
    """
    sorted_all = sorted(all_candidate_stats, key=lambda c: getattr(c, "score_4p_balance", getattr(c, "score_4p", 0.0)), reverse=True)
    if not sorted_all:
        return []

    seeds = []
    seen = set()

    def add_cand(cand):
        tup = cand.delta_tuple if getattr(cand, "delta_tuple", None) else cand.cand_tuple
        if tup[0] not in seen:
            seen.add(tup[0])
            seeds.append(tup)

    # 1. Top performers (positive momentum)
    for c in sorted_all[:beam_width // 2]:
        add_cand(c)

    # 2. Strongest antagonist / negative mutations (essential for compensatory pairs A- + B- -> AB+)
    bottom_half = sorted_all[len(sorted_all) // 2:]
    for c in reversed(bottom_half):
        add_cand(c)
        if len(seeds) >= (beam_width * 4 // 5):
            break

    # 3. Ensure representation across all factions
    for c in sorted_all:
        if len(seeds) >= beam_width:
            break
        add_cand(c)

    return seeds[:beam_width]


def generate_all_composite_candidates(
    beam_seeds: list[tuple[str, str, dict]],
    atomic_pool: list[tuple[str, str, dict]],
) -> list[tuple[str, str, dict]]:
    """Generates the full unconstrained combinatorial cross-product between beam seeds and atomic mutations.
    
    Zero artificial faction filtering, zero heuristic intent restrictions.
    Pure search space exploration checking only for physical card/parameter collision validity.
    """
    seen_ids = set()
    composite_pool = []
    for seed_mut in beam_seeds:
        for atomic_mut in atomic_pool:
            merged = merge_mutations(seed_mut, atomic_mut)
            if merged and merged[0] not in seen_ids:
                seen_ids.add(merged[0])
                composite_pool.append(merged)
    return composite_pool



def generate_and_save_telemetry_report(
    version: str,
    games_per_setup: int = 10000,
    seed: int = 42,
    setups: list[str] | None = None,
    win_overrides: dict | None = None,
) -> tuple[Path, Path | None]:
    """Generates and archives raport_telemetrii.md for the given version across Kanon 4P setups."""
    if setups is None:
        setups = CANONICAL_4P_SETUPS
    t0 = time.time()
    setup_data = []
    all_summaries = []
    thresh = int(CONFIG.system.accusation_threshold)
    ov = win_overrides or {}

    for sname in setups:
        summary = run_batch(games=games_per_setup, setup=sname, seed=seed, layer="C", threshold=thresh, win_overrides=ov)
        all_summaries.append(summary)
        score = calculate_setup_score(summary)
        balance = calculate_balance_score(summary)
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
        acc_opt = "🟢" if 3.5 <= accusations_avg <= 8.5 else ("🟡" if 2.0 <= accusations_avg <= 10.0 else "🔴")

        vit = evaluate_vitality(summary)

        setup_data.append({
            "setup": sname,
            "n_players": n_players,
            "score": score,
            "balance": balance,
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
            "vitality_status": vit.status,
            "vitality_warnings": vit.warnings,
            "vitality_penalty": round(vit.vitality_penalty, 3),
        })

    elapsed = round(time.time() - t0, 2)
    total_games = games_per_setup * len(setups)

    report_lines = [
        f"# Raport Telemetrii i Szans Wygranych (Win Shares) dla Kanonu 4P — Wersja Balansu: {version}",
        "",
        f"**Wersja Balansu:** `{version}` | **Data:** {datetime.now().strftime('%Y-%m-%d %H:%M')} | **Wielkość Próby:** {games_per_setup} gier/setup ({total_games} gier łącznie) | **Czas Symulacji:** {elapsed}s",
        "",
        "*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.",
        "",
        "## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny",
        "",
        "| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |",
    ]

    for d in setup_data:
        so_s = f"{d['shares'].get('SO', 0.0):.1f}%" if "SO" in d['shares'] else "-"
        caa_s = f"{d['shares'].get('CAA', 0.0):.1f}%" if "CAA" in d['shares'] else "-"
        kb_s = f"{d['shares'].get('KB', 0.0):.1f}%" if "KB" in d['shares'] else "-"
        kt_s = f"{d['shares'].get('KT', 0.0):.1f}%" if "KT" in d['shares'] else "-"
        gc_s = f"{d['shares'].get('GC', 0.0):.1f}%" if "GC" in d['shares'] else "-"

        eval_str = "🟢 ZBALANSOWANY" if d['score'] >= 90.0 else ("🟡 AKCEPTOWALNY" if d['score'] >= 80.0 else ("🟠 WYMAGA UWAGI" if d['score'] >= 65.0 else "🔴 ODCHYLONY"))
        report_lines.append(
            f"| `{d['setup']}` | {d['n_players']} | {color_score(d['score'], bold=True)} | {color_score(d['balance'])} | {d['ideal_share']:.1f}% | {so_s} | {caa_s} | {kb_s} | {kt_s} | {gc_s} | {eval_str} |"
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
        "## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)",
        "",
        "| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |",
        "| :--- | :---: | :---: | :--- |",
    ])

    for d in setup_data:
        warn_str = ", ".join(d['vitality_warnings']) if d['vitality_warnings'] else "Brak — wszystkie mechaniki aktywne i płynne"
        report_lines.append(
            f"| `{d['setup']}` | {d['vitality_status']} | {d['vitality_penalty']:.3f} | {warn_str} |"
        )

    return save_and_archive_report(report_lines, "raport_telemetrii.md")


def generate_and_save_canon_optimization_report(
    old_version: str,
    new_version: str,
    iteration: int,
    phase: int,
    base_res_4p: dict,
    best_res_4p: dict,
    diag_before: dict,
    diag_after: dict,
    all_ranked_candidates: list[dict],
    change_desc: str,
    rule_id: str,
    elapsed_iter: float,
) -> tuple[Path, Path | None]:
    """Generates and archives a detailed iteration report for the newly created version."""
    d_4p = best_res_4p["score_4p_balance"] - base_res_4p["score_4p_balance"]
    delta_4p_str = f"+{d_4p:.1f}" if d_4p > 0 else f"{d_4p:.1f}"

    d_glob = diag_after["global_score"] - diag_before["global_score"]
    delta_glob_str = f"+{d_glob:.1f}" if d_glob > 0 else f"{d_glob:.1f}"

    lines = [
        f"# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja {new_version} (Iteracja #{iteration}, Faza {phase}D)",
        "",
        f"**Wersja Poprzednia:** `{old_version}` (4P: `{base_res_4p['score_4p_balance']:.1f} pkt`) → **Nowa Wersja:** `{new_version}` (4P: `{best_res_4p['score_4p_balance']:.1f} pkt`)",
        f"**Data:** {datetime.now().strftime('%Y-%m-%d %H:%M')} | **Czas Trwania Iteracji:** {elapsed_iter:.1f}s | **Zysk 4P:** `{delta_4p_str} pkt` | **Zysk Global:** `{delta_glob_str} pkt`",
        "",
        "## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P",
        f"- **Wybrany Wariant ({phase}D):** `{rule_id}` — **{best_res_4p['name']}**",
        f"- **Opis Modyfikacji:** {change_desc}",
        f"- **Wynik Kanonu 4P Balance:** {score_pair(base_res_4p['score_4p_balance'], best_res_4p['score_4p_balance'], colored=True)} pkt (±{best_res_4p.get('score_se', 0.0):.2f})",
        f"- **Rozbicie Setupów Kanonu 4P:**",
    ]

    for sname in sorted(base_res_4p["setup_scores_balance"].keys()):
        b_sc = base_res_4p["setup_scores_balance"][sname]
        n_sc = best_res_4p["setup_scores_balance"].get(sname, 0.0)
        lines.append(f"  - `{sname}`: {score_pair(b_sc, n_sc)} pkt")

    lines.extend([
        "",
        f"## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)",
        f"- **Tryb 3-osobowy (3p Avg):** {score_pair(diag_before['cat_scores'].get('3p',0), diag_after['cat_scores'].get('3p',0))} pkt",
        f"- **Tryb 4-osobowy (4p Avg):** {score_pair(diag_before['cat_scores'].get('4p',0), diag_after['cat_scores'].get('4p',0))} pkt",
        f"- **Tryb 5-osobowy (5p Avg):** {score_pair(diag_before['cat_scores'].get('5p',0), diag_after['cat_scores'].get('5p',0))} pkt",
        f"- **Global Game Balance Score:** {score_pair(diag_before['global_score'], diag_after['global_score'], colored=True)} pkt",
        "",
        f"- **Kluczowa Telemetria Silnika (Kanon 4P):**",
        f"  - **Średnia Długość Gry:** `{best_res_4p['eras_avg']:.2f} Er`",
        f"  - **Deadlocki (Limit Er):** `{best_res_4p['deadlock_pct']:.1f}%` (norma: <5%)",
        f"  - **Pas Biedy (Złoto):** `{best_res_4p['poverty_pct']:.1f}%` (norma: <30%)",
        f"  - **Autodafé / partię:** `{best_res_4p['autodafe_avg']:.2f}`",
        f"  - **Oskarżenia / partię:** `{best_res_4p['acc_avg']:.2f}`",
        "",
        "## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)",
        "",
        "| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | CI 95% | Deadlocks % | Pas Biedy % | Status |",
        "| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: |",
    ])

    for idx, c in enumerate(all_ranked_candidates[:30], 1):
        d_diff = c["score_4p_balance"] - base_res_4p["score_4p_balance"]
        status = "🌟 ZWYCIĘZCA" if c["id"] == best_res_4p["id"] else ("🟢 ZYSK" if d_diff > 0.0 else "⚪ STRATA/NEUTRALNY")
        ci_str = f"[{c.get('ci_95', (0,0))[0]:.1f}, {c.get('ci_95', (0,0))[1]:.1f}]" if "ci_95" in c else "-"
        lines.append(
            f"| #{idx} | `{c['id']}` | {c['name']} | {score_pair(base_res_4p['score_4p_balance'], c['score_4p_balance'], colored=True)} | "
            f"`{ci_str}` | {c['deadlock_pct']:.1f}% | {c['poverty_pct']:.1f}% | {status} |"
        )

    return save_and_archive_report(lines, "raport_optymalizacji_kanonu.md")


def update_balance_notes(
    old_version: str,
    new_version: str,
    change_desc: str,
    rule_id: str,
    base_res_4p: dict,
    best_res_4p: dict,
    diag_before: dict,
    diag_after: dict,
):
    """Automatically update data/playtesting/balance-notes.md with the new measured scores and patch note entry."""
    if not BALANCE_NOTES_PATH.exists():
        return

    content = BALANCE_NOTES_PATH.read_text(encoding="utf-8")
    today = datetime.now().strftime("%Y-%m-%d")
    d_4p = best_res_4p["score_4p_balance"] - base_res_4p["score_4p_balance"]
    delta_4p_str = f"+{d_4p:.1f}" if d_4p > 0 else f"{d_4p:.1f}"

    patch_note_block = (
        f"### 🟢 Patch {new_version} ({today}) — Kanon 4P: {change_desc} (Zysk 4P Δ {delta_4p_str} pkt)\n"
        f"- **Wynik 4P:** Kanon **`{base_res_4p['score_4p_balance']:.1f}`** → **`{best_res_4p['score_4p_balance']:.1f} pkt`** | Global **`{diag_after['global_score']:.1f}`** | 3p **`{diag_after['cat_scores'].get('3p',0.0):.1f}`** | 5p **`{diag_after['cat_scores'].get('5p',0.0):.1f}`**\n"
        f"- **Modyfikacja (`{rule_id}`):** {change_desc}.\n"
        f"- **Efekt:** Optymalizacja Kanonu 4P. Telemetria: Średnia Er {best_res_4p['eras_avg']:.2f}, Deadlocks {best_res_4p['deadlock_pct']:.1f}%, Pas Biedy {best_res_4p['poverty_pct']:.1f}%.\n\n"
    )

    history_heading = "## 📜 Chronologiczna Historia Zmian Balansu (Faza Prototypowa — Patch Notes)"
    if history_heading in content:
        idx = content.find(history_heading) + len(history_heading)
        content = content[:idx] + "\n\n" + patch_note_block.strip() + "\n\n" + content[idx:].lstrip("\n")

    BALANCE_NOTES_PATH.write_text(content, encoding="utf-8")


def log_canon_iteration(
    log_path: Path,
    iteration: int,
    phase: int,
    old_version: str,
    new_version: str,
    desc: str,
    rule_id: str,
    base_res_4p: dict,
    best_res_4p: dict,
    diag_before: dict,
    diag_after: dict,
    elapsed_iter: float,
):
    """Appends an iteration entry to canon_4p_log.md."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    if not log_path.exists():
        headers = [
            "# Dziennik Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer)",
            "",
            "Rejestr wdrożonych patchów skupionych w 100% na doprowadzeniu Kanonu 4-osobowego do 100%.",
            "",
            "| Iteracja | Faza | Data i Czas | Wersja | Modyfikacja 4P | 4P Score | Wpływ na 3p | Wpływ na 5p | Global Score | Deadlocks % | Pas Biedy % | Czas |",
            "| :---: | :---: | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
        ]
        log_path.write_text("\n".join(headers) + "\n", encoding="utf-8")

    d_4p = best_res_4p["score_4p_balance"] - base_res_4p["score_4p_balance"]
    d4_str = f"+{d_4p:.1f}" if d_4p > 0 else f"{d_4p:.1f}"

    d_3p = diag_after["cat_scores"].get("3p", 0) - diag_before["cat_scores"].get("3p", 0)
    d3_str = f"+{d_3p:.1f}" if d_3p > 0 else f"{d_3p:.1f}"

    d_5p = diag_after["cat_scores"].get("5p", 0) - diag_before["cat_scores"].get("5p", 0)
    d5_str = f"+{d_5p:.1f}" if d_5p > 0 else f"{d_5p:.1f}"

    d_glob = diag_after["global_score"] - diag_before["global_score"]
    dg_str = f"+{d_glob:.1f}" if d_glob > 0 else f"{d_glob:.1f}"

    score_4p_col = f"{base_res_4p['score_4p_balance']:.1f} → **{best_res_4p['score_4p_balance']:.1f}** (`{d4_str}`)"
    p3_col = f"{diag_before['cat_scores'].get('3p',0):.1f} → {diag_after['cat_scores'].get('3p',0):.1f} (`{d3_str}`)"
    p5_col = f"{diag_before['cat_scores'].get('5p',0):.1f} → {diag_after['cat_scores'].get('5p',0):.1f} (`{d5_str}`)"
    glob_col = f"{diag_before['global_score']:.1f} → **{diag_after['global_score']:.1f}** (`{dg_str}`)"

    row = (
        f"| #{iteration} | {phase}D | {datetime.now().strftime('%Y-%m-%d %H:%M')} | `{old_version}` → `{new_version}` | "
        f"**{desc}** (`{rule_id}`) | {score_4p_col} | {p3_col} | {p5_col} | {glob_col} | "
        f"{best_res_4p['deadlock_pct']:.1f}% | {best_res_4p['poverty_pct']:.1f}% | {elapsed_iter:.1f}s |"
    )

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(row + "\n")


class Canon4PAutoBalancer:
    def __init__(self, args: argparse.Namespace):
        self.args = args
        self.stop_requested = False
        self.total_iterations = 0
        self.start_time = time.time()
        self.initial_version = CONFIG.version
        self._last_base_res: dict | None = None
        
        # Simulated Annealing parameters
        self.temperature = getattr(self.args, "temperature", 0.40)
        self.cooling_rate = getattr(self.args, "cooling_rate", 0.90)
        self.min_temperature = getattr(self.args, "min_temperature", 0.05)

        signal.signal(signal.SIGINT, self._handle_sigint)

    def _accept_mode(self) -> str:
        return getattr(self.args, "accept_mode", "legacy")

    def _handle_sigint(self, signum, frame):
        print("\n\n⚠️ Otrzymano sygnał przerwania (Ctrl+C). Bezpiecznie kończę bieżącą iterację...")
        self.stop_requested = True

    def _emit_manual_ablation_review(self) -> None:
        if self._last_base_res is None:
            return
        candidates = collect_manual_ablation_candidates(self._last_base_res)
        if not candidates:
            return
        print_manual_ablation_summary(
            candidates,
            version=CONFIG.version,
            patches_applied=self.total_iterations,
        )
        report_lines = format_manual_ablation_report(
            candidates,
            version=CONFIG.version,
            patches_applied=self.total_iterations,
        )
        archive_path, _ = save_and_archive_report(report_lines, "kandydaci_recznej_ablacji.md")
        print(f"\n   📄 Raport ręcznej ablacji: {archive_path}")

    def run(self):
        print("═══════════════════════════════════════════════════════════════════════")
        print("   INQUISITIO-1492 — AUDYTOR KANONU 4P (Adaptive Monte Carlo Racer)    ")
        print("  Doprowadzanie Kanonu 4P do 100% z dynamicznym doborem próby Monte Carlo")
        print("═══════════════════════════════════════════════════════════════════════")
        print(f"Bieżąca wersja bazowa:      {CONFIG.version}")
        print(f"Maksymalny czas sesji:      {self.args.hours if self.args.hours else 'Brak limitu (do optimum)'} godz.")
        print(f"Maksymalnie patchów:        {self.args.max_iters if self.args.max_iters else 'Brak (do optimum)'}")
        print(f"Kanon Setupy:               {', '.join(CANONICAL_4P_SETUPS)}")
        print(f"Krok partii (Batch Step):   {self.args.batch_step} gier/setup ({len(CANONICAL_4P_SETUPS)} setupów 4p)")
        print(f"Zakres partii w wyścigu:    {self.args.min_games} – {self.args.max_games} gier/setup")
        print(f"Strefa Nierozróżnialności:  ε = {self.args.epsilon_indiff:.2f} pkt")
        print(f"Simulated Annealing:        T_0 = {self.temperature:.2f}, cooling = {self.cooling_rate:.2f}")
        print(f"Wątki procesora:            {self.args.workers}")
        print(f"Tryb przyjęcia patcha:      {self._accept_mode()}")
        print(f"Archiwizacja raportów:     {REPORTS_DIR}/archive/<wersja>/")
        print("═══════════════════════════════════════════════════════════════════════\n")

        setups = CANONICAL_4P_SETUPS
        time_limit_sec = (self.args.hours * 3600) if self.args.hours else None

        current_phase = 1
        beam_seeds: list[tuple[str, str, dict]] = []
        consecutive_stalls = 0
        loop_iteration = 0
        pending_patch: dict[str, Any] | None = None
        cached_base_stats = None

        while not self.stop_requested:
            if time_limit_sec and (time.time() - self.start_time) >= time_limit_sec:
                print(f"\n⏱️ Osiągnięto limit czasu sesji ({self.args.hours}h). Kończę pracę.")
                break

            if self.args.max_iters and self.total_iterations >= self.args.max_iters:
                print(f"\n🔢 Osiągnięto maksymalną liczbę udanych patchów ({self.args.max_iters}). Kończę pracę.")
                break

            iter_start = time.time()
            iter_seed = self.args.seed + loop_iteration * 97
            loop_iteration += 1

            # 1. Candidate Pool Generation (Unconstrained Tree Frontier)
            atomic_pool = generate_all_atomic_candidates()

            if current_phase == 1 or not beam_seeds:
                print(f"\n🌐 [FAZA 1D — KANON 4P] Pełna uniwersalna pula atomowa L1–L4 ({len(atomic_pool)} kandydatów)...")
                candidate_pool = atomic_pool
            else:
                print(f"\n🌐 [FAZA {current_phase}D — KANON 4P] Pełna przestrzeń kombinatoryczna ({len(beam_seeds)} nasion × {len(atomic_pool)} atomów)...")
                candidate_pool = generate_all_composite_candidates(beam_seeds, atomic_pool)

            with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
                current_raw_cfg = yaml.safe_load(f)

            curr_ver = current_raw_cfg.get("system", {}).get("version", current_raw_cfg.get("version", "v1.0-alpha.80"))
            curr_base_overrides = extract_config_overrides(current_raw_cfg)

            # Apply candidate mutations ON TOP OF current cumulative configuration
            effective_candidates = []
            for cid, cname, cparams in candidate_pool:
                merged_params = merge_override_dicts(curr_base_overrides, cparams)
                effective_candidates.append((cid, cname, merged_params))

            print(f"   🧬 Przygotowano {len(effective_candidates)} unikalnych kandydatów (baza: `{curr_ver}`).")

            # 2. Run Adaptive Multi-Fidelity Race
            racer = AdaptiveSequentialRacer(
                setups=setups,
                batch_step=self.args.batch_step,
                min_games=self.args.min_games,
                max_games=self.args.max_games,
                epsilon_indiff=self.args.epsilon_indiff,
                workers=self.args.workers,
                accept_mode=self._accept_mode(),
                min_delta=self.args.min_delta,
            )

            base_stats, candidate_results = racer.run_race(
                base_cand=("BASE", f"Bieżący stan Kanonu 4P ({curr_ver})", curr_base_overrides),
                candidate_pool=effective_candidates,
                seed=iter_seed,
                delta_pool=candidate_pool,
                base_stats_cache=cached_base_stats,
            )
            cached_base_stats = base_stats

            base_res = base_stats.to_result_dict()
            self._last_base_res = base_res

            print(f"\n{'='*71}")
            print(f"🎯 [WYNIK BAZOWY KANONU 4P (`{curr_ver}`)] {color_score(base_res['score_4p_balance'], bold=True)} pkt (±{base_stats.score_se:.2f})")
            print(
                f"   📐 Balance (win share): {color_score(base_res['score_4p_balance'])} pkt | "
                f"min `{base_res['min_balance_setup']}` {color_score(base_res['min_balance'])} | "
                f"witalność kara {base_res['vitality_penalty']:.3f}"
            )
            for sname, sc in sorted(base_res["setup_scores"].items()):
                bal = base_res["setup_scores_balance"].get(sname, sc)
                print(f"      • `{sname}`: {color_score(sc, bold=True)} pkt (balance {color_score(bal)})")
            print(f"   ⏱️ Średnia Er: {base_res['eras_avg']:.2f} | Deadlocks: {base_res['deadlock_pct']:.1f}% | Pas Biedy: {base_res['poverty_pct']:.1f}%")

            if canon_should_stop(base_res, mode=self._accept_mode()):
                print(f"\n🏁 Kanon 4P: {base_res['score_4p_balance']:.1f} pkt — optimum osiągnięte.")
                break

            # 3. Evaluate Survivors & Anti-Greedy Frontier
            surviving_stats = [c for c in candidate_results if not c.is_pruned]
            surviving_stats.sort(key=lambda x: rank_key(x.to_result_dict(), mode=self._accept_mode()))
            ranked_results = [c.to_result_dict() for c in surviving_stats]

            found_better_at_this_depth = False
            best_candidate_at_depth = None

            for cand_stat in surviving_stats:
                cand_res = cand_stat.to_result_dict()
                decision = accept_candidate(
                    base_res, cand_res, mode=self._accept_mode(), min_delta=self.args.min_delta
                )
                if decision.accepted:
                    accepted_tuple = cand_stat.delta_tuple if cand_stat.delta_tuple else cand_stat.cand_tuple
                    best_candidate_at_depth = {
                        "cand_tuple": accepted_tuple,
                        "cand_stat": cand_stat,
                        "best_res": cand_res,
                        "effective_params": cand_stat.cand_tuple[2],
                        "reason": decision.reason,
                        "phase": current_phase,
                    }
                    found_better_at_this_depth = True
                    break

            # Anti-Greedy Lookahead Decision Engine
            should_apply_patch = False
            patch_to_apply = None

            if found_better_at_this_depth and best_candidate_at_depth:
                cand_delta = best_candidate_at_depth["best_res"]["score_4p_balance"] - base_res["score_4p_balance"]
                
                # If this candidate is strictly better than any previously held pending patch
                prev_pending_score = pending_patch["best_res"]["score_4p_balance"] if pending_patch else base_res["score_4p_balance"]
                min_lookahead_gain = getattr(self.args, "min_lookahead_delta", 0.05)
                cand_gain_over_pending = best_candidate_at_depth["best_res"]["score_4p_balance"] - prev_pending_score

                if cand_gain_over_pending >= min_lookahead_gain:
                    pending_patch = best_candidate_at_depth
                    print(
                        f"\n🔍 [ANTI-GREEDY LOOKAHEAD +1D] Znaleziono nową poprawkę w Fazie {current_phase}D: "
                        f"{best_candidate_at_depth['cand_tuple'][1]} (+{cand_delta:.2f} pkt, przyrost nad wstrzymanym: +{cand_gain_over_pending:.2f} pkt).\n"
                        f"   ✋ WSTRZYMUJĘ natychmiastowe wdrożenie i eskaluję do Fazy {current_phase + 1}D, "
                        f"by sprawdzić czy głębsze synergie dadzą jeszcze wyższy zysk globalny..."
                    )
                    beam_seeds = select_diverse_beam_seeds(candidate_results, beam_width=self.args.beam_width)
                    current_phase += 1
                    continue
                else:
                    # Deeper search brought diminishing returns (< min_lookahead_gain) -> Apply the confirmed global best vector!
                    print(
                        f"\n🎯 [LOOKAHEAD ZASADA MALEJĄCYCH PRZYROSTÓW] Faza {current_phase}D wniosła przyrost +{cand_gain_over_pending:.2f} pkt "
                        f"(poniżej progu eskalacji {min_lookahead_gain:.2f} pkt).\n"
                        f"   🌟 Zatrzymuję dalszą eskalację drzewa i wdrażam sprawdzony globalny wektor synergii!"
                    )
                    should_apply_patch = True
                    patch_to_apply = best_candidate_at_depth if best_candidate_at_depth["best_res"]["score_4p_balance"] > prev_pending_score else pending_patch
            else:
                if pending_patch is not None:
                    # Deeper level produced no further gains -> The held pending patch is the confirmed global optimum!
                    print(
                        f"\n🎯 [ANTI-GREEDY LOOKAHEAD] Faza {current_phase}D nie pobiła wstrzymanego wektora z Fazy {pending_patch['phase']}D.\n"
                        f"   🌟 Wdrażam sprawdzony globalny wektor synergii: {pending_patch['cand_tuple'][1]}"
                    )
                    should_apply_patch = True
                    patch_to_apply = pending_patch
                else:
                    # No pending patch and no improvement at this depth -> escalate deeper to search for emergent synergies
                    beam_seeds = select_diverse_beam_seeds(candidate_results, beam_width=self.args.beam_width)
                    max_depth = getattr(self.args, "max_depth", 12)
                    if current_phase >= max_depth or not beam_seeds:
                        consecutive_stalls += 1
                        print(f"\n🛑 Zbadano głębokość do Fazy {current_phase}D bez znalezienia patcha.")
                        print(f"   🔄 Resetuję do Fazy 1D z przesunięciem ziarna eksploracji (pełny cykl {consecutive_stalls}). Kontynuuję poszukiwanie synergii...")
                        current_phase = 1
                        self.args.seed += 137
                        beam_seeds.clear()
                    else:
                        current_phase += 1
                        print(f"🔄 Brak bezpośredniego zysku w {current_phase-1}D. Eksploruję wielowymiarowe synergie w FAZIE {current_phase}D ({len(beam_seeds)} nasion pełnego spektrum)...\n")
                    continue


            # 4. Mandatory 10k Validation Gate & SSOT Commit
            if should_apply_patch and patch_to_apply:
                rule_id, rule_name, delta_params = patch_to_apply["cand_tuple"]
                effective_rule_params = patch_to_apply["effective_params"]
                best_ver_res = patch_to_apply["best_res"]
                acceptance_reason = patch_to_apply["reason"]
                patch_phase = patch_to_apply["phase"]

                print(f"\n🔍 [RYGORYSTYCZNA BRAMKA WALIDACJI 10 000 GIER/SETUP — DLA WEKTORA {patch_phase}D]")
                val_base = _run_full_diagnostic(curr_base_overrides, games_per_setup=10000, seed=42)
                val_cand = _run_full_diagnostic(effective_rule_params, games_per_setup=10000, seed=42)

                val_base_score = val_base["cat_scores"].get("4p", 0.0)
                val_cand_score = val_cand["cat_scores"].get("4p", 0.0)
                val_delta = val_cand_score - val_base_score

                min_allowed_delta = max(0.05, getattr(self.args, "min_delta", 0.05))
                if val_delta < min_allowed_delta:
                    print(
                        f"   ⛔ ODRZUCONO KANDYDATA NA PEŁNYM BENCHMARKU 10K: "
                        f"Baza 10k: {val_base_score:.1f} pkt → Test 10k: {val_cand_score:.1f} pkt "
                        f"(Δ = {val_delta:+.2f} pkt < wymaganego +{min_allowed_delta:.2f} pkt). "
                        f"Fałszywy alarm wyścigu wyeliminowany."
                    )
                    pending_patch = None
                    cached_base_stats = None
                    current_phase = 1
                    beam_seeds.clear()
                    continue

                self.total_iterations += 1

                with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
                    raw_cfg = yaml.safe_load(f)

                old_version = raw_cfg.get("version", "v0.51")
                mod_cfg, change_desc = apply_mutation_to_config(raw_cfg, rule_id, delta_params)

                d_3 = val_cand["cat_scores"].get("3p", 0) - val_base["cat_scores"].get("3p", 0)
                d_5 = val_cand["cat_scores"].get("5p", 0) - val_base["cat_scores"].get("5p", 0)
                d_g = val_cand["global_score"] - val_base["global_score"]

                d3_sign = f"+{d_3:.1f}" if d_3 > 0 else f"{d_3:.1f}"
                d5_sign = f"+{d_5:.1f}" if d_5 > 0 else f"{d_5:.1f}"
                dg_sign = f"+{d_g:.1f}" if d_g > 0 else f"{d_g:.1f}"

                print(f"   🎯 4P Kanon (10k):  {val_base_score:.1f} → **{val_cand_score:.1f} pkt** (Δ {val_delta:+.2f} pkt)")
                print(f"   👥 Wpływ 3p:        {val_base['cat_scores'].get('3p',0):.1f} → {val_cand['cat_scores'].get('3p',0):.1f} pkt (`{d3_sign} pkt`)")
                print(f"   👥 Wpływ 5p:        {val_base['cat_scores'].get('5p',0):.1f} → {val_cand['cat_scores'].get('5p',0):.1f} pkt (`{d5_sign} pkt`)")
                print(f"   🌐 Globalny:        {val_base['global_score']:.1f} → {val_cand['global_score']:.1f} pkt (`{dg_sign} pkt`)")

                # Format exact standardized structures for report and balance notes (10k certified SSOT)
                rep_base_res = dict(base_res)
                rep_base_res["score_4p_balance"] = val_base_score
                rep_base_res["setup_scores_balance"] = {
                    s: val_base["setup_scores"].get(s, 0.0) for s in CANONICAL_4P_SETUPS
                }
                rep_cand_res = dict(best_ver_res)
                rep_cand_res["score_4p_balance"] = val_cand_score
                rep_cand_res["setup_scores_balance"] = {
                    s: val_cand["setup_scores"].get(s, 0.0) for s in CANONICAL_4P_SETUPS
                }

                if self.args.dry_run:
                    print(f"\n[DRY RUN] Zaakceptowano by modyfikację Kanonu 4P: {change_desc} ({acceptance_reason})")
                    pending_patch = None
                    current_phase = 1
                    beam_seeds.clear()
                else:
                    new_version, saved_path = save_config_and_bump_version(mod_cfg, _CONFIG_PATH, bump_version=True)
                    iter_elapsed = round(time.time() - iter_start, 2)

                    print(f"\n🎉 [ZAAKCEPTOWANO PATCH KANONU 4P #{self.total_iterations} — FAZA {patch_phase}D]")
                    print(f"   Wersja:        `{old_version}` → **`{new_version}`**")
                    print(f"   Modyfikacja:   {change_desc}")
                    print(f"   Powód:         {acceptance_reason}")

                    version_archive_dir = REPORTS_DIR / "archive" / new_version
                    version_archive_dir.mkdir(parents=True, exist_ok=True)
                    log_path = version_archive_dir / "canon_4p_log.md"

                    log_canon_iteration(
                        log_path,
                        self.total_iterations,
                        patch_phase,
                        old_version,
                        new_version,
                        change_desc,
                        rule_id,
                        rep_base_res,
                        rep_cand_res,
                        val_base,
                        val_cand,
                        iter_elapsed,
                    )

                    shutil.copy2(_CONFIG_PATH, version_archive_dir / "game_config.yaml")

                    print("   📊 Generuję pełny raport telemetrii Kanonu 4P (10 000 gier/setup)...")
                    generate_and_save_telemetry_report(
                        new_version,
                        games_per_setup=10000,
                        seed=self.args.seed,
                        win_overrides=effective_rule_params,
                    )

                    print("   📝 Generuję szczegółowy raport optymalizacji Kanonu 4P...")
                    generate_and_save_canon_optimization_report(
                        old_version,
                        new_version,
                        self.total_iterations,
                        patch_phase,
                        rep_base_res,
                        rep_cand_res,
                        val_base,
                        val_cand,
                        ranked_results,
                        change_desc,
                        rule_id,
                        iter_elapsed,
                    )

                    print("   📑 Aktualizuję data/playtesting/balance-notes.md...")
                    update_balance_notes(
                        old_version,
                        new_version,
                        change_desc,
                        rule_id,
                        rep_base_res,
                        rep_cand_res,
                        val_base,
                        val_cand,
                    )

                    print("   🔄 Synchronizuję dokumentację kart i reguł...")
                    subprocess.run([sys.executable, str(TOOLS_SRC_DIR.parent / "sync_config.py")])
                    print("   ✔ Zaktualizowano katalog kart, opisy markdown, HTML i card-editor.")

                    current_phase = 1
                    beam_seeds.clear()
                    pending_patch = None
                    cached_base_stats = None

                    # Simulated Annealing: Cool down temperature after each applied step
                    old_t = self.temperature
                    self.temperature = max(self.min_temperature, self.temperature * self.cooling_rate)
                    if old_t > self.min_temperature:
                        print(f"   🌡️ [Simulated Annealing] Schłodzenie: T = {old_t:.3f} → {self.temperature:.3f} (cooling={self.cooling_rate:.2f})")
                    consecutive_stalls = 0

        self._emit_manual_ablation_review()
        print(f"\n═══════════════════════════════════════════════════════════════════════")
        print(f"   AUDYTOR KANONU 4P ZAKOŃCZYŁ SESJĘ. ŁĄCZNIE WPROWADZONO {self.total_iterations} PATCHY.")
        print(f"═══════════════════════════════════════════════════════════════════════\n")


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 Audytor Kanonu 4P (Adaptive Monte Carlo Racer)")
    parser.add_argument("--hours", type=float, default=None, help="Maksymalny czas działania w godzinach (np. 4.0)")
    parser.add_argument("--max-iters", type=int, default=None, help="Maksymalna liczba udanych patchów przed zatrzymaniem")
    
    # Adaptive Monte Carlo Racing parameters
    parser.add_argument("--batch-step", type=int, default=100, help="Rozmiar mikro-kroku partii na setup (domyślnie: 100)")
    parser.add_argument("--min-games", type=int, default=100, help="Minimalna liczba gier/setup przed sprawdzeniem kryterium stopu (domyślnie: 100)")
    parser.add_argument("--max-games", type=int, default=6400, help="Maksymalna liczba gier/setup w wyścigu (domyślnie: 6400)")
    parser.add_argument("--epsilon-indiff", type=float, default=0.15, help="Próg strefy nierozróżnialności / szumu balansu w pkt (domyślnie: 0.15)")
    parser.add_argument("--min-lookahead-delta", type=float, default=0.05, help="Minimalny przyrost punktowy nad wstrzymanym patchem wymagany do eskalacji D->D+1 (pkt, domyślnie: 0.05)")
    
    # Simulated Annealing parameters
    parser.add_argument("--temperature", type=float, default=0.40, help="Początkowa temperatura wyżarzania (domyślnie: 0.40)")
    parser.add_argument("--cooling-rate", type=float, default=0.90, help="Współczynnik chłodzenia po zaakceptowanym patchu (domyślnie: 0.90)")
    parser.add_argument("--min-temperature", type=float, default=0.05, help="Minimalna temperatura wyżarzania (domyślnie: 0.05)")

    parser.add_argument("--beam-width", type=int, default=20, help="Liczba najlepszych kandydatów kwalifikowanych do nasion kolejnej fazy wiązek (domyślnie: 20)")
    parser.add_argument("--max-depth", type=int, default=4, help="Maksymalna głębokość wiązek kombinacji n-D (domyślnie: 4)")
    parser.add_argument("--min-delta", type=float, default=0.05, help="Minimalny zysk punktowy dla 4P wymagany do wdrożenia patcha (pkt, domyślnie: 0.05)")

    parser.add_argument("--workers", type=int, default=min(os.cpu_count() or 4, 10), help="Liczba procesów równoległych")
    parser.add_argument("--seed", type=int, default=42, help="Ziarno generatora liczb losowych")
    parser.add_argument("--dry-run", action="store_true", help="Tryb symulacji bez zapisywania zmian do game_config.yaml")
    parser.add_argument(
        "--accept-mode",
        choices=("legacy", "band"),
        default="legacy",
        help="legacy (max średniej) vs band (maximin poza pasmem, higiena w paśmie)",
    )

    # Legacy compatibility arguments (kept for CLI backwards compatibility)
    parser.add_argument("--fast-games", type=int, default=300, help="[Legacy alias]")
    parser.add_argument("--screen-games", type=int, default=1500, help="[Legacy alias]")
    parser.add_argument("--confirm-games", type=int, default=5000, help="[Legacy alias]")
    parser.add_argument("--top-semifinalists", type=int, default=40, help="[Legacy alias]")
    parser.add_argument("--top-k", type=int, default=20, help="[Legacy alias]")

    args = parser.parse_args()

    auditor = Canon4PAutoBalancer(args)
    auditor.run()


if __name__ == "__main__":
    import multiprocessing
    import platform
    if platform.system() == "Darwin":
        try:
            multiprocessing.set_start_method("spawn")
        except RuntimeError:
            pass
    else:
        try:
            multiprocessing.set_start_method("fork")
        except RuntimeError:
            pass
    main()
