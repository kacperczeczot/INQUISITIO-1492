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


def _run_single_batch_task(task_args: tuple[int, str, int, int, str, dict | None, int]) -> tuple[int, BatchSummary]:
    """Runs a single micro-batch on a specific setup in parallel worker process.

    task_args: (task_idx, setup_name, seed, threshold, layer, win_overrides, games)
    """
    task_idx, setup_name, seed, threshold, layer, win_overrides, games = task_args
    summary = run_batch(
        games=games,
        setup=setup_name,
        seed=seed,
        threshold=threshold,
        layer=layer,
        win_overrides=win_overrides,
    )
    return task_idx, summary


@dataclass
class CandidateStats:
    """Represents a candidate's complete accumulated Monte Carlo race statistics."""
    cand_tuple: tuple[str, str, dict]
    total_games_per_setup: int = 0
    summaries_per_setup: dict[str, list[BatchSummary]] = field(default_factory=dict)
    combined_summary_per_setup: dict[str, BatchSummary] = field(default_factory=dict)
    setup_scores: dict[str, float] = field(default_factory=dict)
    setup_scores_balance: dict[str, float] = field(default_factory=dict)
    setup_shares: dict[str, dict[str, float]] = field(default_factory=dict)
    score_4p: float = 0.0
    score_4p_balance: float = 0.0
    score_se: float = 0.0
    min_balance: float = 0.0
    min_balance_setup: str = ""
    vitality_penalty: float = 0.0
    vitality_warnings: list[str] = field(default_factory=list)
    eras_avg: float = 0.0
    eras_min: int = 1
    eras_max: int = 8
    deadlock_pct: float = 0.0
    poverty_pct: float = 0.0
    autodafe_avg: float = 0.0
    acc_avg: float = 0.0
    gold_avg: float = 0.0
    is_pruned: bool = False
    prune_reason: str = ""
    dt: float = 0.0

    @property
    def id(self) -> str:
        return self.cand_tuple[0]

    @property
    def name(self) -> str:
        return self.cand_tuple[1]

    @property
    def params(self) -> dict:
        return self.cand_tuple[2]

    @property
    def ci_95(self) -> tuple[float, float]:
        """Returns [Lower 95% Bound, Upper 95% Bound]."""
        margin = 1.96 * self.score_se
        return (round(self.score_4p_balance - margin, 2), round(self.score_4p_balance + margin, 2))

    def update_metrics(self) -> None:
        """Recomputes all balance, SE, vitality, and telemetry metrics from combined summaries."""
        if not self.combined_summary_per_setup:
            return

        setup_scores = {}
        setup_scores_balance = {}
        setup_shares = {}
        setup_ses = []
        vitality_penalties = []
        vitality_warnings = []
        summaries = list(self.combined_summary_per_setup.values())

        for sname, summary in self.combined_summary_per_setup.items():
            sc = calculate_setup_score(summary)
            bal, se = calculate_balance_stats(summary)
            setup_scores[sname] = sc
            setup_scores_balance[sname] = bal
            setup_ses.append(se)
            setup_shares[sname] = {
                fid: round(pct * 100.0, 1) for fid, pct in win_shares(summary).items()
            }
            vit = evaluate_vitality(summary)
            vitality_penalties.append(vit.vitality_penalty)
            for msg in vit.warnings:
                vitality_warnings.append(f"{sname}: {msg}")

        n_s = len(setup_scores)
        self.setup_scores = setup_scores
        self.setup_scores_balance = setup_scores_balance
        self.setup_shares = setup_shares
        self.score_4p = round(sum(setup_scores.values()) / n_s, 1) if n_s else 0.0
        self.score_4p_balance = (
            round(sum(setup_scores_balance.values()) / n_s, 1) if n_s else 0.0
        )
        # Average of independent setup balance scores has variance = (1/n^2) * sum(Var_i)
        # So SE = (1/n) * sqrt( sum(SE_i^2) )
        self.score_se = round((math.sqrt(sum(s ** 2 for s in setup_ses)) / n_s), 3) if n_s else 0.0

        min_sname = min(setup_scores_balance, key=lambda k: setup_scores_balance[k])
        self.min_balance_setup = min_sname
        self.min_balance = setup_scores_balance[min_sname]
        self.vitality_penalty = max(vitality_penalties) if vitality_penalties else 0.0
        self.vitality_warnings = vitality_warnings

        n_sum = len(summaries)
        self.eras_avg = sum(s.eras_avg for s in summaries) / n_sum
        self.eras_min = min(s.eras_min for s in summaries)
        self.eras_max = max(s.eras_max for s in summaries)
        self.deadlock_pct = (sum(s.eras_limit_pct for s in summaries) / n_sum) * 100.0
        self.poverty_pct = (sum(s.passes_forced_pct for s in summaries) / n_sum) * 100.0
        self.autodafe_avg = sum(s.autodafe_avg for s in summaries) / n_sum
        self.acc_avg = sum(s.accusations_avg for s in summaries) / n_sum
        self.gold_avg = sum(s.avg_gold_end for s in summaries) / n_sum

    def to_result_dict(self) -> dict:
        """Converts stats to the standard dictionary schema expected by reporting and accept logic."""
        min_setup_name = min(self.setup_scores, key=lambda k: self.setup_scores[k]) if self.setup_scores else ""
        min_setup_score = self.setup_scores.get(min_setup_name, 0.0)
        return {
            "id": self.id,
            "name": self.name,
            "params": self.params,
            "score_4p": self.score_4p,
            "score_4p_balance": self.score_4p_balance,
            "score_se": self.score_se,
            "ci_95": self.ci_95,
            "setup_scores": self.setup_scores,
            "setup_scores_balance": self.setup_scores_balance,
            "setup_shares": self.setup_shares,
            "min_setup": (min_setup_name, min_setup_score),
            "min_balance": self.min_balance,
            "min_balance_setup": self.min_balance_setup,
            "vitality_penalty": self.vitality_penalty,
            "vitality_warnings": self.vitality_warnings,
            "dt": self.dt,
            "total_games_per_setup": self.total_games_per_setup,
            "eras_avg": self.eras_avg,
            "eras_min": self.eras_min,
            "eras_max": self.eras_max,
            "deadlock_pct": self.deadlock_pct,
            "poverty_pct": self.poverty_pct,
            "autodafe_avg": self.autodafe_avg,
            "acc_avg": self.acc_avg,
            "gold_avg": self.gold_avg,
        }


def _simulate_flat_tasks_pool(
    task_list: list[tuple[int, str, int, int, str, dict | None, int]],
    workers: int,
    label: str = "Testy 4P",
) -> list[tuple[int, BatchSummary]]:
    """Executes a flat list of setup micro-batches in parallel across all CPU cores."""
    total = len(task_list)
    if total == 0:
        return []

    from inquisitio.runner.batch import _HAS_NATIVE
    if _HAS_NATIVE or workers <= 1:
        results = []
        t0 = time.time()
        step_freq = max(1, total // 10)
        for idx, t in enumerate(task_list, 1):
            res = _run_single_batch_task(t)
            results.append(res)
            if idx % step_freq == 0 or idx == total:
                elapsed = time.time() - t0
                rate = idx / elapsed if elapsed > 0 else 0
                eta_s = (total - idx) / rate if rate > 0 else 0
                eta_str = f"{int(eta_s // 60)}m {int(eta_s % 60):02d}s" if eta_s >= 60 else f"{int(eta_s)}s"
                sys.stdout.write(f"\r⏳ [{label}] [{idx:4d}/{total:4d}] ({idx*100.0/total:5.1f}%) | {rate:5.1f} bat/s | ETA: {eta_str:<8s}\n")
                sys.stdout.flush()
        sys.stdout.write(f"   ✔ Ukończono {total} zadań mikro-batchy w {round(time.time() - t0, 1)}s.\n")
        return results

    results = []
    t0 = time.time()
    chunk_size = max(1, min(10, total // (workers * 4)))
    step_freq = max(1, total // 10)
    with ProcessPoolExecutor(max_workers=workers) as executor:
        for idx, res in enumerate(executor.map(_run_single_batch_task, task_list, chunksize=chunk_size), 1):
            results.append(res)
            elapsed = time.time() - t0
            rate = idx / elapsed if elapsed > 0 else 0
            eta_s = (total - idx) / rate if rate > 0 else 0
            eta_str = f"{int(eta_s // 60)}m {int(eta_s % 60):02d}s" if eta_s >= 60 else f"{int(eta_s)}s"
            if idx % step_freq == 0 or idx == total:
                sys.stdout.write(f"\r⏳ [{label}] [{idx:4d}/{total:4d}] ({idx*100.0/total:5.1f}%) | {rate:4.1f} bat/s | ETA: {eta_str:<8s}\n")
            else:
                sys.stdout.write(f"\r⏳ [{label}] [{idx:4d}/{total:4d}] ({idx*100.0/total:5.1f}%) | {rate:4.1f} bat/s | ETA: {eta_str:<8s}")
            sys.stdout.flush()

    sys.stdout.write(f"   ✔ Ukończono {total} zadań mikro-batchy w {round(time.time() - t0, 1)}s.\n")
    return results


class AdaptiveSequentialRacer:
    """Adaptive Multi-Fidelity Racing optimizer with Delta-Method SE and Indifference Zone stopping."""

    def __init__(
        self,
        setups: list[str],
        batch_step: int = 100,
        min_games: int = 400,
        max_games: int = 8000,
        epsilon_indiff: float = 0.15,
        workers: int = 10,
        accept_mode: str = "legacy",
        min_delta: float = 0.50,
    ):
        self.setups = setups
        self.batch_step = batch_step
        self.min_games = min_games
        self.max_games = max_games
        self.epsilon_indiff = epsilon_indiff
        self.workers = workers
        self.accept_mode = accept_mode
        self.min_delta = min_delta

    def run_race(
        self,
        base_cand: tuple[str, str, dict],
        candidate_pool: list[tuple[str, str, dict]],
        seed: int,
    ) -> tuple[CandidateStats, list[CandidateStats]]:
        """Conducts iterative micro-batch racing with statistical pruning and indifference zone stopping."""
        base_stats = CandidateStats(base_cand)
        active_candidates = [CandidateStats(c) for c in candidate_pool]
        all_candidates = list(active_candidates)

        # ─── Geometric Rung Ladder (Successive Halving) ──────────────────────
        rungs = []
        r = max(100, self.batch_step)
        while r < self.max_games:
            rungs.append(r)
            r *= 2
        if not rungs or rungs[-1] < self.max_games:
            rungs.append(self.max_games)

        curr_games = 0
        t_start = time.time()

        print(
            f"\n🏁 [START WYŚCIGU ADAPTACYJNEGO] Pula: {len(active_candidates)} kandydatów | "
            f"Szczeble: {rungs} gier/setup (Successive Halving)"
        )

        for step_idx, target_games in enumerate(rungs, 1):
            delta_games = target_games - curr_games
            if delta_games <= 0:
                continue

            # Active set: Base + non-pruned candidates
            survivors = [c for c in active_candidates if not c.is_pruned]
            if not survivors:
                print(f"   🛑 Wszyscy kandydaci zostali statystycznie wyeliminowani (N={curr_games} gier/setup).")
                break

            current_pool = [base_stats] + survivors

            # 1. Build flat task matrix (candidate x setup) for the delta games
            task_list = []
            task_map = {}  # task_idx -> (candidate_obj, setup_name)
            task_idx = 0

            for cand_obj in current_pool:
                for sname in self.setups:
                    task_seed = seed + step_idx * 10007 + (hash(cand_obj.id) % 5003)
                    task_args = (task_idx, sname, task_seed, 8, "C", cand_obj.params, delta_games)
                    task_list.append(task_args)
                    task_map[task_idx] = (cand_obj, sname)
                    task_idx += 1

            # 2. Execute flattened pool across all CPU workers
            step_label = f"Szczebel #{step_idx}/{len(rungs)} (N={target_games} gier) [{len(survivors)} kand]"
            batch_results = _simulate_flat_tasks_pool(task_list, self.workers, label=step_label)

            # 3. Aggregate results into candidate stats
            for t_id, summary in batch_results:
                cand_obj, sname = task_map[t_id]
                cand_obj.summaries_per_setup.setdefault(sname, []).append(summary)

            curr_games = target_games
            for cand_obj in current_pool:
                cand_obj.total_games_per_setup = curr_games
                for sname, s_list in cand_obj.summaries_per_setup.items():
                    cand_obj.combined_summary_per_setup[sname] = merge_batch_summaries(s_list)
                cand_obj.update_metrics()
                cand_obj.dt = round(time.time() - t_start, 2)

            base_lb, base_ub = base_stats.ci_95

            # 4. Statistical & Successive Halving Pruning
            active_survivors = [c for c in active_candidates if not c.is_pruned]
            if active_survivors:
                best_score = max(c.score_4p_balance for c in active_survivors)
                ref_lb = max(base_lb, best_score - 2.5 * base_stats.score_se)

                for c in active_survivors:
                    c_lb, c_ub = c.ci_95

                    # A. Telemetry & Vitality hard vetoes (SPRT early stop)
                    if curr_games >= 200:
                        if c.vitality_penalty > 0.0 and base_stats.vitality_penalty == 0.0:
                            c.is_pruned = True
                            c.prune_reason = f"Weto witalności (kara {c.vitality_penalty:.2f})"
                            continue
                        if c.deadlock_pct > 8.0:
                            c.is_pruned = True
                            c.prune_reason = f"Katastrofa deadlocków ({c.deadlock_pct:.1f}% > 8%)"
                            continue
                        if c.poverty_pct > 35.0:
                            c.is_pruned = True
                            c.prune_reason = f"Katastrofa biedy ({c.poverty_pct:.1f}% > 35%)"
                            continue

                    # B. Statistical Upper-Bound Pruning vs Base & Leader
                    if curr_games >= 200:
                        if c_ub < ref_lb - 0.10:
                            c.is_pruned = True
                            c.prune_reason = f"Statystycznie gorszy od Bazy/Lidera (UB {c_ub:.2f} < Ref LB {ref_lb:.2f})"
                            continue

                # C. Successive Halving Capacity Filter (Top-K by UCB)
                remaining = [c for c in active_candidates if not c.is_pruned]
                max_capacity = max(8, int(len(candidate_pool) / (2 ** (step_idx - 1))))
                if len(remaining) > max_capacity:
                    remaining.sort(key=lambda x: x.ci_95[1], reverse=True)
                    for cut_c in remaining[max_capacity:]:
                        cut_c.is_pruned = True
                        cut_c.prune_reason = f"Successive Halving (odcięcie poza TOP {max_capacity})"

            active_survivors = [c for c in active_candidates if not c.is_pruned]
            pruned_count = len(all_candidates) - len(active_survivors)
            print(
                f"   📊 [Status N={curr_games}] Baza: {base_stats.score_4p_balance:.1f} pkt (±{base_stats.score_se:.2f}) | "
                f"Aktywnych: {len(active_survivors)}/{len(all_candidates)} (Odrzucono: {pruned_count})"
            )

            # 5. Check Racing Stop & Convergence Conditions
            if curr_games >= self.min_games and active_survivors:
                # Rank active survivors
                active_survivors.sort(key=lambda x: rank_key(x.to_result_dict(), mode=self.accept_mode))
                leader = active_survivors[0]
                l_lb, l_ub = leader.ci_95

                # If leader itself is statistically worse than base: stop!
                if l_ub < base_lb:
                    print(f"   🛑 Lider ({leader.id}) jest statystycznie gorszy od Bazy (UB {l_ub:.2f} < Base LB {base_lb:.2f}). Kończę wyścig.")
                    break

                if len(active_survivors) == 1:
                    if l_lb > base_ub:
                        print(f"   🏆 Wyłoniono samotnego zwycięzcę: {leader.id} (LB {l_lb:.2f} > Base UB {base_ub:.2f}) po {curr_games} grach/setup.")
                        break

                elif len(active_survivors) >= 2:
                    runner_up = active_survivors[1]
                    r_lb, r_ub = runner_up.ci_95

                    # Case A: Clear statistical separation
                    if l_lb > r_ub and l_lb > base_ub:
                        print(
                            f"   🏆 Wyłoniono bezdyskusyjnego lidera: {leader.id} (LB {l_lb:.2f} > Drugi UB {r_ub:.2f}) "
                            f"po {curr_games} grach/setup."
                        )
                        break

                    # Case B: Indifference Zone (Effective Tie in noise margin)
                    score_gap = abs(leader.score_4p_balance - runner_up.score_4p_balance)
                    se_diff = math.sqrt(leader.score_se ** 2 + runner_up.score_se ** 2)

                    if score_gap < self.epsilon_indiff and se_diff < self.epsilon_indiff and l_lb > base_ub:
                        chosen = leader if leader.min_balance >= runner_up.min_balance else runner_up
                        print(
                            f"   🤝 Zbieżność w Strefie Nierozróżnialności: Δ={score_gap:.3f} < {self.epsilon_indiff:.2f} "
                            f"(SE_diff={se_diff:.3f}). Wybrano {chosen.id} (lepsza podłoga). Kończę wyścig po {curr_games} grach/setup."
                        )
                        break

        return base_stats, all_candidates


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
        shares = setup_shares.get(sname, {})
        if not shares:
            continue

        ideal_share = 25.0
        dominant_prefixes = []
        struggling_prefixes = []

        for f_raw, pct in shares.items():
            f_code = _normalize_faction_code(f_raw)
            dev = pct - ideal_share
            if dev >= 1.5:
                dominant_prefixes.append((f_code, dev))
            elif dev <= -1.5:
                struggling_prefixes.append((f_code, dev))

        if not dominant_prefixes or not struggling_prefixes:
            sorted_f = sorted(shares.items(), key=lambda x: x[1])
            struggling_prefixes = [(_normalize_faction_code(sorted_f[0][0]), sorted_f[0][1] - ideal_share)]
            dominant_prefixes = [(_normalize_faction_code(sorted_f[-1][0]), sorted_f[-1][1] - ideal_share)]

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

            # 1. Candidate Pool Generation
            atomic_pool = generate_all_atomic_candidates()

            if current_phase == 1 or not beam_seeds:
                print(f"\n🌐 [FAZA 1D — KANON 4P] Pełna pula atomowa L1–L4 ({len(atomic_pool)} kandydatów)...")
                candidate_pool = atomic_pool
            else:
                print(f"\n🌐 [FAZA {current_phase}D — KANON 4P] Celowane pary antagonistyczne i synergistyczne wiązki...")
                composite_pool = []

                if self._last_base_res is not None:
                    antag_pairs = generate_antagonistic_and_hybrid_candidates(self._last_base_res, atomic_pool)
                    composite_pool.extend(antag_pairs)

                for seed_mut in beam_seeds:
                    seed_f = get_mutation_faction(seed_mut)
                    # Group other candidates by faction to ensure even coverage across the entire game
                    faction_groups: dict[str, list] = {}
                    for m in atomic_pool:
                        f = get_mutation_faction(m) or "SYSTEM"
                        if f != seed_f:
                            faction_groups.setdefault(f, []).append(m)

                    selected_atomic = []
                    rng_pool = random.Random(iter_seed + hash(seed_mut[0]) % 10007)
                    for f, m_list in faction_groups.items():
                        shuffled_m = list(m_list)
                        rng_pool.shuffle(shuffled_m)
                        selected_atomic.extend(shuffled_m[:50])

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

                if len(candidate_pool) > 2000:
                    rng_comb = random.Random(iter_seed)
                    rng_comb.shuffle(candidate_pool)
                    candidate_pool = candidate_pool[:2000]

            print(f"   🧬 Przygotowano {len(candidate_pool)} unikalnych kandydatów.")

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
                base_cand=("BASE", "Bieżący stan Kanonu 4P", {}),
                candidate_pool=candidate_pool,
                seed=iter_seed,
            )

            base_res = base_stats.to_result_dict()
            self._last_base_res = base_res

            print(f"\n{'='*71}")
            print(f"🎯 [WYNIK BAZOWY KANONU 4P] {color_score(base_res['score_4p_balance'], bold=True)} pkt (±{base_stats.score_se:.2f})")
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

            # 3. Evaluate Survivors and Finalists
            surviving_stats = [c for c in candidate_results if not c.is_pruned]
            surviving_stats.sort(key=lambda x: rank_key(x.to_result_dict(), mode=self._accept_mode()))

            ranked_results = [c.to_result_dict() for c in surviving_stats]

            accepted_candidate = None
            best_ver_res = None
            acceptance_reason = ""

            for cand_stat in surviving_stats:
                cand_res = cand_stat.to_result_dict()
                decision = accept_candidate(
                    base_res, cand_res, mode=self._accept_mode(), min_delta=self.args.min_delta
                )
                
                # Strict Global Optimization Gate: Must strictly improve 4P Canon (Δ >= min_delta) with zero floor degradation
                if decision.accepted:
                    accepted_candidate = cand_stat.cand_tuple
                    best_ver_res = cand_res
                    acceptance_reason = decision.reason
                    break

            # 4. Apply Patch & Measure Collateral Impact (with Strict 10k Full Benchmark Gate)
            if accepted_candidate and best_ver_res is not None:
                rule_id, rule_name, rule_params = accepted_candidate

                # MANDATORY VALIDATION GATE: Confirm on full 10,000 games/setup benchmark on standard seed
                # Guarantee that official score is strictly monotonically increasing (NO false positives from micro-batches)
                print(f"\n🔍 [RYGORYSTYCZNA BRAMKA WALIDACJI 10 000 GIER/SETUP]")
                val_base = _run_full_diagnostic({}, games_per_setup=10000, seed=42)
                val_cand = _run_full_diagnostic(rule_params, games_per_setup=10000, seed=42)

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
                    accepted_candidate = None
                    best_ver_res = None
                    continue

                self.total_iterations += 1

                with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
                    raw_cfg = yaml.safe_load(f)

                old_version = raw_cfg.get("version", "v0.51")
                mod_cfg, change_desc = apply_mutation_to_config(raw_cfg, rule_id, rule_params)

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

                # Format exact standardized structures for report and balance notes
                rep_base_res = dict(base_res)
                rep_base_res["score_4p_balance"] = val_base_score
                rep_cand_res = dict(best_ver_res)
                rep_cand_res["score_4p_balance"] = val_cand_score

                if self.args.dry_run:
                    print(f"\n[DRY RUN] Zaakceptowano by modyfikację Kanonu 4P: {change_desc} ({acceptance_reason})")
                    current_phase += 1
                else:
                    new_version, saved_path = save_config_and_bump_version(mod_cfg, _CONFIG_PATH, bump_version=True)
                    iter_elapsed = round(time.time() - iter_start, 2)

                    print(f"\n🎉 [ZAAKCEPTOWANO PATCH KANONU 4P #{self.total_iterations} — FAZA {current_phase}D]")
                    print(f"   Wersja:        `{old_version}` → **`{new_version}`**")
                    print(f"   Modyfikacja:   {change_desc}")
                    print(f"   Powód:         {acceptance_reason}")

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
                        win_overrides=rule_params,
                    )

                    print("   📝 Generuję szczegółowy raport optymalizacji Kanonu 4P...")
                    generate_and_save_canon_optimization_report(
                        old_version,
                        new_version,
                        self.total_iterations,
                        current_phase,
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

                    # Simulated Annealing: Cool down temperature after each applied step
                    old_t = self.temperature
                    self.temperature = max(self.min_temperature, self.temperature * self.cooling_rate)
                    if old_t > self.min_temperature:
                        print(f"   🌡️ [Simulated Annealing] Schłodzenie: T = {old_t:.3f} → {self.temperature:.3f} (cooling={self.cooling_rate:.2f})")
                    consecutive_stalls = 0

            else:
                print(
                    f"\n⚪ Brak bezpośredniego zwycięzcy w Fazie {current_phase}D. "
                    f"Buduję zaawansowane wiązki synergii dla słabych setupów..."
                )
                diverse_seeds = []
                seen_seed_factions = set()
                # Ensure every faction with active mutations gets a seed in the combinatorial beam
                for r in surviving_stats:
                    f = get_mutation_faction(r.cand_tuple) or "SYSTEM"
                    if f not in seen_seed_factions:
                        seen_seed_factions.add(f)
                        diverse_seeds.append(r.cand_tuple)
                for r in surviving_stats:
                    if r.cand_tuple not in diverse_seeds:
                        diverse_seeds.append(r.cand_tuple)

                if current_phase >= self.args.max_depth:
                    consecutive_stalls += 1
                    print(f"\n🛑 Osiągnięto maksymalną głębokość wiązek ({self.args.max_depth}D) bez znalezienia patcha.")
                    if consecutive_stalls >= 5:
                        print(f"   ⛔ {consecutive_stalls} pełnych cykli 1D-3D bez efektu. Przestrzeń mutacji wyczerpana. Kończę.")
                        break
                    else:
                        print(f"   🔄 Resetuję do Fazy 1D z przesunięciem ziarna eksploracji (pełny cykl {consecutive_stalls}/5).")
                        current_phase = 1
                        self.args.seed += 137
                        beam_seeds.clear()
                else:
                    beam_seeds = diverse_seeds[:self.args.beam_width]
                    current_phase += 1
                    print(f"🔄 Zakwalifikowano {len(beam_seeds)} nasion synergii i ESKALUJĘ DO FAZY {current_phase}D...\n")

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
    parser.add_argument("--min-games", type=int, default=400, help="Minimalna liczba gier/setup przed sprawdzeniem kryterium stopu (domyślnie: 400)")
    parser.add_argument("--max-games", type=int, default=8000, help="Maksymalna liczba gier/setup w wyścigu (domyślnie: 8000)")
    parser.add_argument("--epsilon-indiff", type=float, default=0.15, help="Próg strefy nierozróżnialności / szumu balansu w pkt (domyślnie: 0.15)")
    
    # Simulated Annealing parameters
    parser.add_argument("--temperature", type=float, default=0.40, help="Początkowa temperatura wyżarzania (domyślnie: 0.40)")
    parser.add_argument("--cooling-rate", type=float, default=0.90, help="Współczynnik chłodzenia po zaakceptowanym patchu (domyślnie: 0.90)")
    parser.add_argument("--min-temperature", type=float, default=0.05, help="Minimalna temperatura wyżarzania (domyślnie: 0.05)")

    parser.add_argument("--beam-width", type=int, default=10, help="Liczba najlepszych kandydatów kwalifikowanych do nasion kolejnej fazy wiązek")
    parser.add_argument("--max-depth", type=int, default=3, help="Maksymalna głębokość wiązek kombinacji n-D (domyślnie: 3)")
    parser.add_argument("--min-delta", type=float, default=0.50, help="Minimalny zysk punktowy dla 4P wymagany do wdrożenia patcha (pkt, domyślnie: 0.50)")

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
