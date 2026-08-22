#!/usr/bin/env python3
"""INQUISITIO-1492 — AUDYTOR KANONU 4P (Canonical Anchor-Based Balance Optimizer).

Autonomiczny optymalizator balansu skupiony w 100% na doprowadzeniu Kanonu 4-osobowego (4P)
do absolutnego optimum (99–100 pkt), bez kompromisów pod 3p i 5p.

Główne założenia metodologiczne:
  1. Kanon 4P jako Kotwica (Anchor):
     Format 4-osobowy jest sercem mechaniki gry INQUISITIO-1492. Wszystkie karty i reguły
     muszą w pierwszej kolejności działać w sposób idealny i elegancki na 5 setupach 4p:
       - 4p-core
       - 4p-no-cienie
       - 4p-no-kabala
       - 4p-no-korona
       - 4p-no-oficjum
  2. Błyskawiczny 3-Stopniowy Lejek na 5 setupach 4P:
     - Etap 1 (Szybki Przesiew): 200 gier/setup × 5 setupów (~1.5 min) -> TOP 48 półfinalistów
     - Etap 2 (Głęboki Przesiew): 1000 gier/setup × 5 setupów (~3.5 min) -> TOP 24 finalistów
     - Etap 3 (Weryfikacja Ultra): 5000 gier/setup × 5 setupów (~7.5 min) -> Zwycięski Patch
  3. Diagnostyka Wpływu Kolateralnego (Cross-Impact Telemetry):
     Po znalezieniu najlepszej zmiany 4P, skrypt mierzy jej wpływ na 3p i 5p, raportując:
     jakie realne anomalie geometryczne stołu zostały obnażone.
  4. Pełna automatyzacja dokumentacji:
     - playtesting/sim-reports/canon_4p_log.md
     - playtesting/sim-reports/raport_optymalizacji_4p.md (oraz archiwum)
     - playtesting/balance-notes.md
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
from inquisitio.runner.balance import faction_shares as win_shares
from inquisitio.runner.canon_accept import (
    TARGET_BAND_PCT,
    accept_candidate,
    canon_should_stop,
    rank_key,
    setup_shares_in_range,
    table_has_share_foundation,
)
from inquisitio.runner.scoring import (
    calculate_balance_score,
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
from audytor_4p import is_ablation_off, is_frozen_identity_knob
from manual_ablation_hints import (
    collect_manual_ablation_candidates,
    format_manual_ablation_report,
    print_manual_ablation_summary,
)

REPORTS_DIR = Path(__file__).resolve().parent.parent.parent / "playtesting" / "sim-reports"
BALANCE_NOTES_PATH = Path(__file__).resolve().parent.parent.parent / "playtesting" / "balance-notes.md"
LIVE_LOG_PATH = REPORTS_DIR / "audytor_live.log"

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


def _run_single_test_task_4p(task_args: tuple[tuple[str, str, dict], int, int, list[str]]) -> dict:
    """Execute a single candidate rule across the 5 canonical 4P setups."""
    (rule_id, rule_name, rule_params), games_per_setup, seed, setups = task_args
    t_rule = time.time()

    summaries = []
    setup_scores = {}
    setup_scores_balance = {}
    setup_shares: dict[str, dict[str, float]] = {}
    vitality_penalties = []
    vitality_warnings: list[str] = []
    for idx_s, sname in enumerate(setups):
        summary = run_batch(
            games=games_per_setup,
            setup=sname,
            seed=seed,
            layer="C",
            win_overrides=rule_params,
        )
        summaries.append(summary)
        setup_scores[sname] = calculate_setup_score(summary)
        setup_scores_balance[sname] = calculate_balance_score(summary)
        setup_shares[sname] = {
            fid: round(pct * 100.0, 1) for fid, pct in win_shares(summary).items()
        }
        vit = evaluate_vitality(summary)
        vitality_penalties.append(vit.vitality_penalty)
        for msg in vit.warnings:
            vitality_warnings.append(f"{sname}: {msg}")

        # Wczesne odrzucanie w Etapie 1 (gdy po 2 setupach wariant jest skrajnie nieoptymalny < 30 pkt)
        if games_per_setup <= 200 and idx_s == 1:
            if (sum(setup_scores_balance.values()) / 2.0) < 30.0:
                for rem_sname in setups[2:]:
                    setup_scores[rem_sname] = 0.0
                    setup_scores_balance[rem_sname] = 0.0
                break


    score_4p = round(sum(setup_scores.values()) / len(setup_scores), 1) if setup_scores else 0.0
    score_4p_balance = (
        round(sum(setup_scores_balance.values()) / len(setup_scores_balance), 1)
        if setup_scores_balance
        else 0.0
    )
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
    min_balance_name = min(setup_scores_balance, key=lambda k: setup_scores_balance[k])
    min_balance = setup_scores_balance[min_balance_name]
    vitality_penalty = max(vitality_penalties) if vitality_penalties else 0.0

    return {
        "id": rule_id,
        "name": rule_name,
        "params": rule_params,
        "score_4p": score_4p,
        "score_4p_balance": score_4p_balance,
        "setup_scores": setup_scores,
        "setup_scores_balance": setup_scores_balance,
        "setup_shares": setup_shares,
        "min_setup": (min_setup_name, min_setup_score),
        "min_balance": min_balance,
        "min_balance_setup": min_balance_name,
        "vitality_penalty": vitality_penalty,
        "vitality_warnings": vitality_warnings,
        "dt": dt,
        "eras_avg": eras_avg, "eras_min": eras_min, "eras_max": eras_max,
        "deadlock_pct": deadlock_pct,
        "poverty_pct": poverty_pct,
        "autodafe_avg": autodafe_avg,
        "acc_avg": acc_avg,
        "gold_avg": gold_avg,
    }


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


def generate_antagonistic_and_hybrid_candidates(
    base_res: dict, atomic_pool: list[tuple[str, str, dict]]
) -> list[tuple[str, str, dict]]:
    """Generates targeted 2D candidates (Antagonistic pairs, Hybrids, Intra-faction shifts)
    focused on directly solving the weakest setups in the 4P canon.
    """
    setup_scores = base_res.get("setup_scores", {})
    setup_shares = base_res.get("setup_shares", {})
    out: list[tuple[str, str, dict]] = []

    for sname in sorted(setup_scores.keys(), key=lambda k: setup_scores[k]):
        score = setup_scores[sname]
        shares = setup_shares.get(sname, {})
        if not shares:
            continue

        ideal_share = 25.0
        dominant_prefixes = []
        struggling_prefixes = []

        for f_code, pct in shares.items():
            dev = pct - ideal_share
            if dev >= 1.5:
                dominant_prefixes.append((f_code, dev))
            elif dev <= -1.5:
                struggling_prefixes.append((f_code, dev))

        if not dominant_prefixes or not struggling_prefixes:
            sorted_f = sorted(shares.items(), key=lambda x: x[1])
            struggling_prefixes = [(sorted_f[0][0], sorted_f[0][1] - ideal_share)]
            dominant_prefixes = [(sorted_f[-1][0], sorted_f[-1][1] - ideal_share)]

        # 1. Antagonistic Pairs: Nerf Dominant + Buff Deficit
        for dom_f, _ in dominant_prefixes:
            dom_nerfs = [
                m for m in atomic_pool
                if get_mutation_faction(m) == dom_f and classify_card_mutation_intent(m) == "NERF"
            ]
            for strug_f, _ in struggling_prefixes:
                strug_buffs = [
                    m for m in atomic_pool
                    if get_mutation_faction(m) == strug_f and classify_card_mutation_intent(m) == "BUFF"
                ]

                for m_nerf in dom_nerfs:
                    for m_buff in strug_buffs:
                        merged = merge_mutations(m_nerf, m_buff)
                        if merged:
                            out.append(merged)

        # 2. Hybrids: L3 Buff/Nerf + L1/L2 System Rules
        sys_rules = [
            m for m in atomic_pool
            if classify_card_mutation_intent(m) == "SYSTEM" and not m[0].startswith("L4_")
        ]
        for strug_f, _ in struggling_prefixes:
            strug_buffs = [
                m for m in atomic_pool
                if get_mutation_faction(m) == strug_f and classify_card_mutation_intent(m) == "BUFF"
            ]
            for m_buff in strug_buffs:
                for s_rule in sys_rules:
                    merged = merge_mutations(m_buff, s_rule)
                    if merged:
                        out.append(merged)

        # 3. Intra-faction Rebalance
        for strug_f, _ in struggling_prefixes:
            f_buffs = [
                m for m in atomic_pool
                if get_mutation_faction(m) == strug_f and classify_card_mutation_intent(m) == "BUFF"
            ]
            f_nerfs = [
                m for m in atomic_pool
                if get_mutation_faction(m) == strug_f and classify_card_mutation_intent(m) == "NERF"
            ]
            for mb in f_buffs:
                for mn in f_nerfs:
                    merged = merge_mutations(mb, mn)
                    if merged:
                        out.append(merged)

    seen = set()
    unique_out = []
    for c in out:
        if c[0] not in seen:
            seen.add(c[0])
            unique_out.append(c)
    return unique_out


def cheap_funnel_flags(n: int, top_semifinalists: int, top_k: int) -> tuple[bool, bool]:

    """Skip cheap screens when they wouldn't cut the pool. Confirm always runs.

    Returns (run_fast, run_screen). If n ≤ top_k both are False — jump straight to ultra.
    """
    run_fast = n > top_semifinalists
    after_fast = min(n, top_semifinalists) if run_fast else n
    run_screen = after_fast > top_k
    return run_fast, run_screen


def merge_mutations(m1: tuple[str, str, dict], m2: tuple[str, str, dict]) -> tuple[str, str, dict] | None:
    """Merges two mutations into a composite mutation (e.g. 2D pair or 3D triple)."""
    id1, name1, p1 = m1
    id2, name2, p2 = m2

    # Check for direct conflicts on atomic keys
    keys1 = set(p1.keys()) - {"card_overrides"}
    keys2 = set(p2.keys()) - {"card_overrides"}
    if keys1 & keys2:
        return None

    # Check for conflicts on same card parameters
    cards1 = p1.get("card_overrides", {})
    cards2 = p2.get("card_overrides", {})
    for cid, c_dict in cards2.items():
        if cid in cards1:
            if set(c_dict.keys()) & set(cards1[cid].keys()):
                return None

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


def select_diverse_survivors(results: list[dict], cand_dict: dict, target_count: int) -> list[tuple[str, str, dict]]:
    """Select a diverse set of candidates: global leaders + maximin leaders + setup champions."""
    if len(results) <= target_count:
        return [cand_dict[r["id"]] for r in results]

    selected_ids = []

    # 1. Top by global score_4p_balance (50% quota)
    by_score = sorted(results, key=lambda r: -r.get("score_4p_balance", 0))
    quota_global = max(1, target_count // 2)
    for r in by_score:
        if r["id"] not in selected_ids and len(selected_ids) < quota_global:
            selected_ids.append(r["id"])

    # 2. Top by weakest setup improvement (min_balance) (30% quota)
    by_min = sorted(results, key=lambda r: -r.get("min_balance", 0))
    quota_min = quota_global + max(1, int(target_count * 0.3))
    for r in by_min:
        if r["id"] not in selected_ids and len(selected_ids) < quota_min:
            selected_ids.append(r["id"])

    # 3. Setup champions for struggling setups (4p-core, 4p-no-kabala, 4p-no-oficjum)
    for sname in ["4p-no-kabala", "4p-core", "4p-no-oficjum"]:
        by_setup = sorted(results, key=lambda r: -r.get("setup_scores_balance", {}).get(sname, 0))
        for r in by_setup[:2]:
            if r["id"] not in selected_ids and len(selected_ids) < target_count:
                selected_ids.append(r["id"])

    # 4. Fill remaining slots from global sort
    for r in by_score:
        if r["id"] not in selected_ids and len(selected_ids) < target_count:
            selected_ids.append(r["id"])

    return [cand_dict[cid] for cid in selected_ids]


def generate_and_save_telemetry_report(version: str, games_per_setup: int = 1000, seed: int = 42) -> tuple[Path, Path | None]:
    """Generates and archives raport_telemetrii.md for the given version across all 16 setups."""
    setups = sorted(SETUP_PRESETS.keys())
    t0 = time.time()
    setup_data = []

    for sname in setups:
        summary = run_batch(games=games_per_setup, setup=sname, seed=seed, layer="C", threshold=8)
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
        acc_opt = "🟢" if 2.0 <= accusations_avg <= 4.5 else ("🟡" if 1.5 <= accusations_avg <= 5.0 else "🔴")

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

    report_lines = [
        f"# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: {version}",
        "",
        f"**Wersja Balansu:** `{version}` | **Data:** {datetime.now().strftime('%Y-%m-%d %H:%M')} | **Wielkość Próby:** {games_per_setup} gier/setup ({games_per_setup * 16} gier łącznie) | **Czas Symulacji:** {elapsed}s",
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

        eval_str = "🟢 ZBALANSOWANY" if d['score'] >= 90.0 else ("🟡 AKCEPTOWALNY" if d['score'] >= 75.0 else ("🟠 WYMAGA UWAGI" if d['score'] >= 60.0 else "🔴 ODCHYLONY"))
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
        f"- **Wynik Kanonu 4P Balance:** {score_pair(base_res_4p['score_4p_balance'], best_res_4p['score_4p_balance'], colored=True)} pkt",
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
        "| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |",
        "| :---: | :---: | :--- | :---: | :---: | :---: | :---: |",
    ])

    for idx, c in enumerate(all_ranked_candidates, 1):
        d_diff = c["score_4p_balance"] - base_res_4p["score_4p_balance"]
        status = "🌟 ZWYCIĘZCA" if c["id"] == best_res_4p["id"] else ("🟢 ZYSK" if d_diff > 0.0 else "⚪ STRATA/NEUTRALNY")
        lines.append(
            f"| #{idx} | `{c['id']}` | {c['name']} | {score_pair(base_res_4p['score_4p_balance'], c['score_4p_balance'], colored=True)} | "
            f"{c['deadlock_pct']:.1f}% | {c['poverty_pct']:.1f}% | {status} |"
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
    """Automatically update playtesting/balance-notes.md with the new measured scores and patch note entry."""
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

    history_heading = "## 📜 Chronologiczna Historia Zmian Balansu (Faza Prototypowa — Patch Notes)\n\n"
    if history_heading in content:
        content = content.replace(history_heading, history_heading + patch_note_block, 1)

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
        self._base_in_band = False
        self._last_base_res: dict | None = None
        signal.signal(signal.SIGINT, self._handle_sigint)

    def _accept_mode(self) -> str:
        return getattr(self.args, "accept_mode", "legacy")

    def _rank(self, res: dict) -> tuple:
        return rank_key(res, mode=self._accept_mode(), base_in_band=self._base_in_band)

    def _handle_sigint(self, signum, frame):
        print("\n\n⚠️ Otrzymano sygnał przerwania (Ctrl+C). Bezpiecznie kończę bieżącą iterację...")
        self.stop_requested = True

    def _emit_manual_ablation_review(self) -> None:
        if self._last_base_res is None:
            return
        candidates = collect_manual_ablation_candidates(self._last_base_res)
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

    def _execute_pool(self, task_func, task_list: list, label: str = "Testy 4P") -> list[dict]:
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
                if best_so_far is None or self._rank(res) < self._rank(best_so_far):
                    best_so_far = res

                elapsed = time.time() - t0
                rate = idx / elapsed if elapsed > 0 else 0
                eta_s = (total - idx) / rate if rate > 0 else 0
                eta_str = f"{int(eta_s // 60)}m {int(eta_s % 60):02d}s" if eta_s >= 60 else f"{int(eta_s)}s"
                lead_id = best_so_far['id'][:26] if best_so_far else "-"
                lead_sc = f"{best_so_far['score_4p_balance']:.1f}" if best_so_far else "-"
                sys.stdout.write(f"\r⏳ [{label}] [{idx:4d}/{total:4d}] ({idx*100.0/total:5.1f}%) | {rate:4.1f} zad/s | ETA: {eta_str:<7s} | Lider 4P: {lead_id} ({lead_sc} pkt)  ")
                sys.stdout.flush()

        sys.stdout.write(f"\n   ✔ Ukończono {total} zadań w {round(time.time() - t0, 1)}s.\n")
        return results

    def run(self):
        print("═══════════════════════════════════════════════════════════════════════")
        print("   INQUISITIO-1492 — AUDYTOR KANONU 4P (Anchor-Based 4P Optimizer)     ")
        print("  Doprowadzanie Kanonu 4P do 100% z diagnostyką wpływu na 3p i 5p      ")
        print("═══════════════════════════════════════════════════════════════════════")
        print(f"Bieżąca wersja bazowa:      {CONFIG.version}")
        print(f"Maksymalny czas sesji:      {self.args.hours if self.args.hours else 'Brak limitu (do optimum)'} godz.")
        print(f"Maksymalnie patchów:        {self.args.max_iters if self.args.max_iters else 'Brak (do optimum)'}")
        print(f"Kanon Setupy:               {', '.join(CANONICAL_4P_SETUPS)}")
        print(f"Etap 1 (Szybki przesiew):   {self.args.fast_games} gier/setup ({len(CANONICAL_4P_SETUPS)} setupów 4p)")
        print(f"Etap 2 (Głęboki przesiew):  {self.args.screen_games} gier/setup (TOP {self.args.top_semifinalists} półfinalistów)")
        print(f"Etap 3 (Weryfikacja Ultra): {self.args.confirm_games} gier/setup (TOP {self.args.top_k} finalistów)")
        print(f"Wątki procesora:            {self.args.workers}")
        print(f"Tryb przyjęcia patcha:      {self._accept_mode()}")
        print(f"Archiwizacja raportów:     {REPORTS_DIR}/archive/<wersja>/")
        print("═══════════════════════════════════════════════════════════════════════\n")

        setups = CANONICAL_4P_SETUPS
        time_limit_sec = (self.args.hours * 3600) if self.args.hours else None

        current_phase = 1
        beam_seeds: list[tuple[str, str, dict]] = []

        while not self.stop_requested:
            if time_limit_sec and (time.time() - self.start_time) >= time_limit_sec:
                print(f"\n⏱️ Osiągnięto limit czasu sesji ({self.args.hours}h). Kończę pracę.")
                break

            if self.args.max_iters and self.total_iterations >= self.args.max_iters:
                print(f"\n🔢 Osiągnięto maksymalną liczbę udanych patchów ({self.args.max_iters}). Kończę pracę.")
                break

            iter_start = time.time()

            # 1. Measure 4P Baseline
            print(f"\n{'='*71}")
            print(f"🔍 [POMIAR BAZOWY KANONU 4P] Diagnoza 5 setupów 4p (Próba: {self.args.confirm_games} gier/setup)...")
            base_task = ((("BASE", "Bieżący stan Kanonu 4P", {}), self.args.confirm_games, self.args.seed, setups),)
            base_res = self._execute_pool(_run_single_test_task_4p, [base_task[0]], label="Baza 4P")[0]
            self._last_base_res = base_res

            print(f"   🎯 Wynik Kanonu 4P Balance: {color_score(base_res['score_4p_balance'], bold=True)} pkt")
            print(
                f"   📐 Balance (win share): {color_score(base_res['score_4p_balance'])} pkt | "
                f"min `{base_res['min_balance_setup']}` {color_score(base_res['min_balance'])} | "
                f"witalność kara {base_res['vitality_penalty']:.3f}"
            )
            self._base_in_band = setup_shares_in_range(base_res.get("setup_shares") or {}, *TARGET_BAND_PCT)
            band_label = "w paśmie 20–30% → higiena" if self._base_in_band else "poza pasmem 20–30% → wspinaczka maximin"
            print(f"   🎚️ Pasmo 4P: {band_label}")
            warns = base_res.get("vitality_warnings") or []
            if warns:
                print("   💤 Witalność — martwe / kastracja (audytor ma to leczyć, nie zatrzymywać się na win share):")
                for w in warns:
                    print(f"      • {w}")
            if self._accept_mode() == "band" and not table_has_share_foundation(base_res):
                print(
                    "\n🧱 Fundament: 4P poza czerwoną linią 15–35%. "
                    "Wspinaczka aktywna — akceptuję kandydatów poprawiających rozkład frakcji."
                )
            if canon_should_stop(base_res, mode=self._accept_mode()):
                print(f"\n🏁 Kanon 4P: {base_res['score_4p_balance']:.1f} pkt — optimum osiągnięte.")
                break
            for sname, sc in sorted(base_res["setup_scores"].items()):
                bal = base_res["setup_scores_balance"].get(sname, sc)
                print(f"      • `{sname}`: {color_score(sc, bold=True)} pkt (balance {color_score(bal)})")
            print(f"   ⏱️ Średnia Er: {base_res['eras_avg']:.2f} | Deadlocks: {base_res['deadlock_pct']:.1f}% | Pas Biedy: {base_res['poverty_pct']:.1f}%")

            # 2. Candidate Pool
            atomic_pool = generate_all_atomic_candidates()

            if current_phase == 1 or not beam_seeds:
                print(f"\n🌐 [FAZA 1D — KANON 4P] Pełna pula atomowa L1–L4...")
                candidate_pool = atomic_pool
            else:
                print(f"\n🌐 [FAZA {current_phase}D — KANON 4P] Celowane pary antagonistyczne (Nerf Dominanta + Buff Deficytu) i komplementarne wiązki...")
                composite_pool = []

                # 1. Celowane pary antagonistyczne i hybrydowe
                antag_pairs = generate_antagonistic_and_hybrid_candidates(base_res, atomic_pool)
                composite_pool.extend(antag_pairs)

                # 2. Komplementarne łączenie nasion wiązki z regułami L1/L2 i kartami deficytowych frakcji
                for seed_mut in beam_seeds:
                    # Łączymy nasiona z kartami INNYCH frakcji (L3) oraz reprezentacją reguł systemowych (L1/L2)
                    seed_f = get_mutation_faction(seed_mut)
                    other_cards = [
                        m for m in atomic_pool
                        if get_mutation_faction(m) is not None and get_mutation_faction(m) != seed_f
                    ]
                    sys_muts = [
                        m for m in atomic_pool
                        if classify_card_mutation_intent(m) == "SYSTEM"
                    ]
                    # Bierzemy próbkę kart innych frakcji + reguły systemowe
                    selected_atomic = other_cards[:100] + sys_muts[:10]
                    for atomic_mut in selected_atomic:
                        merged = merge_mutations(seed_mut, atomic_mut)
                        if merged:
                            composite_pool.append(merged)

                seen_ids = set()
                candidate_pool = []
                for c in composite_pool:
                    if c[0] not in seen_ids:
                        seen_ids.add(c[0])
                        candidate_pool.append(c)

                # Zachowujemy pełną pulę celowanych wariantów złożonych dla Etapu 1
                if len(candidate_pool) > 1500:
                    candidate_pool = candidate_pool[:1500]

            print(f"   🧬 Wygenerowano {len(candidate_pool)} unikalnych kandydatów dla Kanonu 4P.")
            cand_dict = {c[0]: c for c in candidate_pool}

            run_fast, run_screen = cheap_funnel_flags(
                len(candidate_pool), self.args.top_semifinalists, self.args.top_k
            )
            survivors = list(candidate_pool)

            # 3. ETAP 1/3: Szybki Przesiew (tylko jeśli pula > top_semifinalists)
            if run_fast:
                print(f"\n--- [ETAP 1/3: SZYBKI PRZESIEW 4P] Testuję {len(survivors)} kandydatów ({self.args.fast_games} gier/setup × 5 setupów) ---")
                stage1_tasks = [((c[0], c[1], c[2]), self.args.fast_games, self.args.seed, setups) for c in survivors]
                stage1_results = self._execute_pool(_run_single_test_task_4p, stage1_tasks, label="Przesiew 4P 1/3")
                stage1_results.sort(key=self._rank)
                n_semifinalists = min(self.args.top_semifinalists, len(stage1_results))
                survivors = select_diverse_survivors(stage1_results, cand_dict, n_semifinalists)
            else:
                print(f"\n⏭️ Pomijam etap 1 ({self.args.fast_games} g): {len(survivors)} ≤ TOP {self.args.top_semifinalists} — przesiew nic nie tnie.")

            # 4. ETAP 2/3: Głęboki Przesiew (tylko jeśli pula po etapie 1 > top_k)
            if run_screen:
                print(f"\n--- [ETAP 2/3: GŁĘBOKI PRZESIEW 4P] Badam {len(survivors)} półfinalistów ({self.args.screen_games} gier/setup × 5 setupów) ---")
                stage2_tasks = [((c[0], c[1], c[2]), self.args.screen_games, self.args.seed, setups) for c in survivors]
                stage2_results = self._execute_pool(_run_single_test_task_4p, stage2_tasks, label="Przesiew 4P 2/3")
                stage2_results.sort(key=self._rank)
                n_finalists = min(self.args.top_k, len(stage2_results))
                survivors = select_diverse_survivors(stage2_results, cand_dict, n_finalists)
            else:
                print(f"\n⏭️ Pomijam etap 2 ({self.args.screen_games} g): {len(survivors)} ≤ TOP {self.args.top_k} — idę na ultra.")

            # 5. ETAP 3/3: Weryfikacja Ultra 4P
            print(f"\n--- [ETAP 3/3: WERYFIKACJA ULTRA 4P] Weryfikuję {len(survivors)} finalistów ({self.args.confirm_games} gier/setup × 5 setupów) ---")
            stage3_tasks = [((c[0], c[1], c[2]), self.args.confirm_games, self.args.seed, setups) for c in survivors]
            stage3_results = self._execute_pool(_run_single_test_task_4p, stage3_tasks, label="Weryfikacja 4P 3/3")

            stage3_results.sort(key=self._rank)

            print(f"\n📊 [WYNIKI WERYFIKACJI FINALISTÓW KANONU 4P] tryb={self._accept_mode()}")
            for idx, r in enumerate(stage3_results, 1):
                decision = accept_candidate(
                    base_res, r, mode=self._accept_mode(), min_delta=self.args.min_delta
                )
                d_4 = r["score_4p_balance"] - base_res["score_4p_balance"]
                sign = f"+{d_4:.2f}" if d_4 > 0 else f"{d_4:.2f}"
                mark = "✔" if decision.accepted else "✖"
                print(
                    f"   #{idx:2d} {mark} [{r['id'][:42]}...] 4P {base_res['score_4p_balance']:.1f} → {r['score_4p_balance']:.1f} "
                    f"(Δ {sign}) min {r['min_balance']:.1f} | {decision.reason}"
                )

            # Wybieramy najlepszego zaakceptowanego finalistę (według rankingu score_4p / witalności)
            accepted_candidate = None
            best_ver_res = None

            for ver_res in stage3_results:
                decision = accept_candidate(
                    base_res, ver_res, mode=self._accept_mode(), min_delta=self.args.min_delta
                )
                if decision.accepted:
                    accepted_candidate = cand_dict[ver_res["id"]]
                    best_ver_res = ver_res
                    break

            if best_ver_res is not None:
                d_lead = best_ver_res['score_4p_balance'] - base_res['score_4p_balance']
                print(f"\n   → Wybrano `{best_ver_res['id']}` (zysk 4P Δ {d_lead:+.2f} pkt, min {best_ver_res.get('min_balance', 0):.1f})")


            # 5b. WALIDACJA KRZYŻOWA — potwierdzenie na niezależnym seedzie
            if accepted_candidate and best_ver_res is not None:
                cross_seed = self.args.seed + 9999  # Niezależne ziarno losowości
                print(f"\n🔀 [WALIDACJA KRZYŻOWA] Potwierdzam zwycięzcę na niezależnym seedzie ({cross_seed})...")
                print(f"   Testuję bazę i kandydata na {self.args.confirm_games} gier/setup × 5 setupów...")

                cross_base_task = (("CROSS_BASE", "Baza krzyżowa", {}), self.args.confirm_games, cross_seed, setups)
                cross_cand_task = (accepted_candidate, self.args.confirm_games, cross_seed, setups)
                cross_results = self._execute_pool(
                    _run_single_test_task_4p,
                    [cross_base_task, cross_cand_task],
                    label="Walidacja krzyżowa"
                )

                cross_base_res = None
                cross_cand_res = None
                for cr in cross_results:
                    if cr["id"] == "CROSS_BASE":
                        cross_base_res = cr
                    else:
                        cross_cand_res = cr

                if cross_base_res and cross_cand_res:
                    cross_decision = accept_candidate(
                        cross_base_res, cross_cand_res,
                        mode=self._accept_mode(), min_delta=self.args.min_delta
                    )
                    cross_d = cross_cand_res['score_4p_balance'] - cross_base_res['score_4p_balance']
                    cross_dmin = float(cross_cand_res.get('min_balance', 0)) - float(cross_base_res.get('min_balance', 0))
                    print(f"   🔀 Wynik krzyżowy: Δscore {cross_d:+.2f} pkt, Δmin {cross_dmin:+.2f} pkt")
                    print(f"   🔀 Decyzja krzyżowa: {'✔ POTWIERDZONE' if cross_decision.accepted else '✖ ODRZUCONE'} — {cross_decision.reason}")

                    if not cross_decision.accepted:
                        print(f"\n   ⛔ ODRZUCONO PATCH — walidacja krzyżowa na seedzie {cross_seed} nie potwierdziła zysku.")
                        print(f"      Kandydat `{best_ver_res['id']}` to szum statystyczny, a nie realna poprawa.")
                        accepted_candidate = None
                        best_ver_res = None
                else:
                    print(f"\n   ⛔ ODRZUCONO PATCH — błąd walidacji krzyżowej.")
                    accepted_candidate = None
                    best_ver_res = None

            # 6. Apply Patch & Measure Collateral Impact
            if accepted_candidate and best_ver_res is not None:
                self.total_iterations += 1
                rule_id, rule_name, rule_params = accepted_candidate

                with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
                    raw_cfg = yaml.safe_load(f)

                old_version = raw_cfg.get("version", "v0.51")
                mod_cfg, change_desc = apply_mutation_to_config(raw_cfg, rule_id, rule_params)

                # Cross-impact diagnosis (all 16 setups before vs after)
                print(f"\n🔬 [DIAGNOZA WPŁYWU NA POZOSTAŁE TRYBY (3P / 5P)]...")
                diag_before = _run_full_diagnostic({}, games_per_setup=1000, seed=self.args.seed)
                diag_after = _run_full_diagnostic(rule_params, games_per_setup=1000, seed=self.args.seed)

                d_3 = diag_after["cat_scores"].get("3p", 0) - diag_before["cat_scores"].get("3p", 0)
                d_5 = diag_after["cat_scores"].get("5p", 0) - diag_before["cat_scores"].get("5p", 0)
                d_g = diag_after["global_score"] - diag_before["global_score"]

                d3_sign = f"+{d_3:.1f}" if d_3 > 0 else f"{d_3:.1f}"
                d5_sign = f"+{d_5:.1f}" if d_5 > 0 else f"{d_5:.1f}"
                dg_sign = f"+{d_g:.1f}" if d_g > 0 else f"{d_g:.1f}"

                print(f"   🎯 4P Kanon:  {base_res['score_4p_balance']:.1f} → **{best_ver_res['score_4p_balance']:.1f} pkt** (Δ {best_ver_res['score_4p_balance'] - base_res['score_4p_balance']:+.2f} pkt)")
                print(f"   👥 Wpływ 3p:  {diag_before['cat_scores'].get('3p',0):.1f} → {diag_after['cat_scores'].get('3p',0):.1f} pkt (`{d3_sign} pkt`)")
                print(f"   👥 Wpływ 5p:  {diag_before['cat_scores'].get('5p',0):.1f} → {diag_after['cat_scores'].get('5p',0):.1f} pkt (`{d5_sign} pkt`)")
                print(f"   🌐 Globalny:  {diag_before['global_score']:.1f} → {diag_after['global_score']:.1f} pkt (`{dg_sign} pkt`)")

                if self.args.dry_run:
                    print(f"\n[DRY RUN] Zaakceptowano by modyfikację Kanonu 4P: {change_desc}")
                    current_phase += 1
                else:
                    new_version, saved_path = save_config_and_bump_version(mod_cfg, _CONFIG_PATH, bump_version=True)
                    iter_elapsed = round(time.time() - iter_start, 2)

                    print(f"\n🎉 [ZAAKCEPTOWANO PATCH KANONU 4P #{self.total_iterations} — FAZA {current_phase}D]")
                    print(f"   Wersja:        `{old_version}` → **`{new_version}`**")
                    print(f"   Modyfikacja:   {change_desc}")

                    version_archive_dir = REPORTS_DIR / "archive" / new_version
                    version_archive_dir.mkdir(parents=True, exist_ok=True)
                    log_path = version_archive_dir / "canon_4p_log.md"

                    log_canon_iteration(
                        log_path,
                        self.total_iterations,
                        current_phase,
                        old_version,
                        new_version,
                        change_desc,
                        rule_id,
                        base_res,
                        best_ver_res,
                        diag_before,
                        diag_after,
                        iter_elapsed,
                    )

                    # Snapshot game_config.yaml in version archive
                    shutil.copy2(_CONFIG_PATH, version_archive_dir / "game_config.yaml")

                    print("   📊 Generuję pełny raport telemetrii 16 setupów i archiwum...")
                    generate_and_save_telemetry_report(new_version, games_per_setup=1000, seed=self.args.seed)

                    print("   📝 Generuję szczegółowy raport optymalizacji Kanonu 4P...")
                    generate_and_save_canon_optimization_report(
                        old_version,
                        new_version,
                        self.total_iterations,
                        current_phase,
                        base_res,
                        best_ver_res,
                        diag_before,
                        diag_after,
                        stage3_results,
                        change_desc,
                        rule_id,
                        iter_elapsed,
                    )

                    print("   📑 Aktualizuję playtesting/balance-notes.md...")
                    update_balance_notes(
                        old_version,
                        new_version,
                        change_desc,
                        rule_id,
                        base_res,
                        best_ver_res,
                        diag_before,
                        diag_after,
                    )

                    print("   🔄 Synchronizuję dokumentację kart i reguł...")
                    subprocess.run([sys.executable, str(TOOLS_SIM_DIR.parent / "sync_config.py")])
                    print("   ✔ Zaktualizowano katalog kart, opisy markdown, HTML i card-editor.")

                    current_phase = 1
                    beam_seeds.clear()

            else:
                print(
                    f"\n⚪ Brak bezpośredniego zwycięzcy w Fazie {current_phase}D. "
                    f"Buduję zaawansowane wiązki synergii dla słabych setupów..."
                )
                diverse_seeds = []
                by_score = sorted(stage3_results, key=lambda r: -r.get("score_4p_balance", 0))
                for r in by_score[:4]:
                    diverse_seeds.append(cand_dict[r["id"]])
                by_min = sorted(stage3_results, key=lambda r: -r.get("min_balance", 0))
                for r in by_min[:4]:
                    if cand_dict[r["id"]] not in diverse_seeds:
                        diverse_seeds.append(cand_dict[r["id"]])
                for sname in ["4p-no-kabala", "4p-core", "4p-no-oficjum"]:
                    by_s = sorted(stage3_results, key=lambda r: -r.get("setup_scores_balance", {}).get(sname, 0))
                    for r in by_s[:2]:
                        if cand_dict[r["id"]] not in diverse_seeds:
                            diverse_seeds.append(cand_dict[r["id"]])

                beam_seeds = diverse_seeds[: self.args.beam_width]
                current_phase += 1
                print(f"🔄 Zakwalifikowano {len(beam_seeds)} nasion synergii i ESKALUJĘ DO FAZY {current_phase}D...\n")

        self._emit_manual_ablation_review()
        print(f"\n═══════════════════════════════════════════════════════════════════════")
        print(f"   AUDYTOR KANONU 4P ZAKOŃCZYŁ SESJĘ. ŁĄCZNIE WPROWADZONO {self.total_iterations} PATCHY.")
        print(f"═══════════════════════════════════════════════════════════════════════\n")


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 Audytor Kanonu 4P (Anchor-Based 4P Optimizer)")
    parser.add_argument("--hours", type=float, default=None, help="Maksymalny czas działania w godzinach (np. 4.0)")
    parser.add_argument("--max-iters", type=int, default=None, help="Maksymalna liczba udanych patchów przed zatrzymaniem")
    parser.add_argument("--fast-games", type=int, default=300, help="Liczba gier w Etapie 1 na 5 setupach 4p (domyślnie: 300)")
    parser.add_argument("--screen-games", type=int, default=1500, help="Liczba gier w Etapie 2 na 5 setupach 4p (domyślnie: 1500)")
    parser.add_argument("--confirm-games", type=int, default=5000, help="Liczba gier w Etapie 3 na 5 setupach 4p (domyślnie: 5000)")
    parser.add_argument("--top-semifinalists", type=int, default=24, help="Liczba półfinalistów sprawdzanych w Etapie 2 (domyślnie: 24)")
    parser.add_argument("--top-k", type=int, default=12, help="Liczba finalistów sprawdzanych w Etapie 3 (domyślnie: 12)")
    parser.add_argument("--beam-width", type=int, default=8, help="Liczba najlepszych kandydatów kwalifikowanych do nasion kolejnej fazy wiązek (domyślnie: 8)")
    parser.add_argument("--max-depth", type=int, default=3, help="Maksymalna głębokość wiązek kombinacji n-D (domyślnie: 3)")
    parser.add_argument("--min-delta", type=float, default=0.50, help="Minimalny zysk punktowy dla 4P wymagany do wdrożenia patcha (pkt, domyślnie: 0.50)")

    parser.add_argument("--workers", type=int, default=min(os.cpu_count() or 4, 10), help="Liczba procesów równoległych")
    parser.add_argument("--seed", type=int, default=42, help="Ziarno generatora liczb losowych")
    parser.add_argument("--dry-run", action="store_true", help="Tryb symulacji bez zapisywania zmian do game_config.yaml")
    parser.add_argument(
        "--accept-mode",
        choices=("legacy", "band"),
        default="legacy",
        help=(
            "legacy (domyślnie): max średniej balansu 4P jak dawny auto_balancer (czysty gradient). "
            "band: wspinaczka maximin poza pasmem 20–30%%, higiena zdrowia w paśmie."
        ),
    )

    args = parser.parse_args()

    if args.fast_games < 100:
        args.fast_games = 100
    if args.screen_games < 500:
        args.screen_games = 500
    if args.confirm_games < 3000:
        args.confirm_games = 3000

    auditor = Canon4PAutoBalancer(args)
    auditor.run()


if __name__ == "__main__":
    import multiprocessing
    try:
        multiprocessing.set_start_method("fork")
    except RuntimeError:
        pass
    main()
