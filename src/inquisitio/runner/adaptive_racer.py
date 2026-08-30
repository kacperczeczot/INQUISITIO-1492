"""INQUISITIO-1492 — Generic Adaptive Sequential Racer Core Module.

Provides high-performance Multi-Fidelity Monte Carlo racing with:
  1. Multi-fidelity geometric ladder (rungs: 400 -> 1600 -> 6400).
  2. Pure Statistical Confidence Interval (95% CI) pruning without arbitrary capacity cuts.
  3. Delta-Method Standard Error for win-share balance scores.
  4. Parallel execution of flattened setup tasks across native C++20 workers.
  5. Multi-dimensional mutation merging for combinatorial beam search (1D -> 2D -> 3D -> 4D).
"""
from __future__ import annotations

import copy
import math
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass, field
from typing import Any

from inquisitio.runner.balance import faction_shares as win_shares
from inquisitio.runner.batch import BatchSummary, merge_batch_summaries, run_batch
from inquisitio.runner.canon_accept import rank_key
from inquisitio.runner.scoring import (
    calculate_balance_stats,
    calculate_setup_score,
    evaluate_vitality,
)


def _run_single_batch_task(task_args: tuple[int, str, int, int, str, dict | None, int]) -> tuple[int, BatchSummary]:
    """Runs a single micro-batch on a specific setup in a worker process."""
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
    delta_tuple: tuple[str, str, dict] | None = None
    total_games_per_setup: int = 0
    summaries_per_setup: dict[str, list[BatchSummary]] = field(default_factory=dict)
    combined_summary_per_setup: dict[str, BatchSummary] = field(default_factory=dict)
    setup_scores: dict[str, float] = field(default_factory=dict)
    setup_scores_balance: dict[str, float] = field(default_factory=dict)
    setup_shares: dict[str, dict[str, float]] = field(default_factory=dict)
    score_4p: float = 0.0
    score_4p_balance: float = 0.0
    score_global: float = 0.0
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
        
        # Obliczenia stare dla zgodności
        self.score_4p = round(sum(setup_scores.values()) / n_s, 1) if n_s else 0.0
        self.score_4p_balance = (
            round(sum(setup_scores_balance.values()) / n_s, 1) if n_s else 0.0
        )
        self.score_se = round((math.sqrt(sum(s ** 2 for s in setup_ses)) / n_s), 3) if n_s else 0.0

        # Nowe obliczenia globalne
        from inquisitio.runner.scoring import calculate_category_scores, calculate_global_score
        cat_scores = calculate_category_scores(summaries)
        self.score_global = calculate_global_score(cat_scores)

        min_sname = min(setup_scores_balance, key=lambda k: setup_scores_balance[k]) if setup_scores_balance else ""
        self.min_balance_setup = min_sname
        self.min_balance = setup_scores_balance.get(min_sname, 0.0)
        self.vitality_penalty = max(vitality_penalties) if vitality_penalties else 0.0
        self.vitality_warnings = vitality_warnings

        n_sum = len(summaries)
        if n_sum:
            self.eras_avg = sum(s.eras_avg for s in summaries) / n_sum
            self.eras_min = min(s.eras_min for s in summaries)
            self.eras_max = max(s.eras_max for s in summaries)
            self.deadlock_pct = (sum(s.eras_limit_pct for s in summaries) / n_sum) * 100.0
            self.poverty_pct = (sum(s.passes_forced_pct for s in summaries) / n_sum) * 100.0
            self.autodafe_avg = sum(s.autodafe_avg for s in summaries) / n_sum
            self.acc_avg = sum(s.accusations_avg for s in summaries) / n_sum
            self.gold_avg = sum(s.avg_gold_end for s in summaries) / n_sum

    def to_result_dict(self) -> dict:
        """Converts stats to the standard dictionary schema."""
        min_setup_name = min(self.setup_scores, key=lambda k: self.setup_scores[k]) if self.setup_scores else ""
        min_setup_score = self.setup_scores.get(min_setup_name, 0.0)
        return {
            "id": self.id,
            "name": self.name,
            "params": self.params,
            "score_global": getattr(self, "score_global", 0.0),
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
    label: str = "Testy Symulacji",
) -> list[tuple[int, BatchSummary]]:
    """Executes a flat list of setup micro-batches in parallel across all CPU cores."""
    total = len(task_list)
    if total == 0:
        return []

    if workers <= 1 or total < 50:
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
    chunk_size = max(50, min(2000, total // (workers * 8)))
    step_freq = max(100, total // 100)
    with ProcessPoolExecutor(max_workers=workers) as executor:
        for idx, res in enumerate(executor.map(_run_single_batch_task, task_list, chunksize=chunk_size), 1):
            results.append(res)
            if idx % step_freq == 0 or idx == total:
                elapsed = time.time() - t0
                rate = idx / elapsed if elapsed > 0 else 0
                eta_s = (total - idx) / rate if rate > 0 else 0
                eta_str = f"{int(eta_s // 60)}m {int(eta_s % 60):02d}s" if eta_s >= 60 else f"{int(eta_s)}s"
                sys.stdout.write(f"\r⏳ [{label}] [{idx:7d}/{total:7d}] ({idx*100.0/total:5.1f}%) | {rate:5.1f} bat/s | ETA: {eta_str:<8s}")
                sys.stdout.flush()

    sys.stdout.write(f"\n   ✔ Ukończono {total} zadań mikro-batchy w {round(time.time() - t0, 1)}s.\n")
    return results


class AdaptiveSequentialRacer:
    """Adaptive Multi-Fidelity Racing optimizer with Delta-Method SE and Pure Statistical CI Pruning."""

    def __init__(
        self,
        setups: list[str],
        batch_step: int = 400,
        min_games: int = 400,
        max_games: int = 6400,
        epsilon_indiff: float = 0.15,
        workers: int = 10,
        min_delta: float = 0.05,
    ):
        self.setups = setups
        self.batch_step = batch_step
        self.min_games = min_games
        self.max_games = max_games
        self.epsilon_indiff = epsilon_indiff
        self.workers = workers
        self.min_delta = min_delta

    def run_race(
        self,
        base_cand: tuple[str, str, dict],
        candidate_pool: list[tuple[str, str, dict]],
        seed: int,
        delta_pool: list[tuple[str, str, dict]] | None = None,
        label_prefix: str = "WYŚCIG ADAPTACYJNY",
        base_stats_cache: CandidateStats | None = None,
        target_floor_score: float | None = None,
    ) -> tuple[CandidateStats, list[CandidateStats]]:
        """Conducts iterative micro-batch racing with pure statistical 95% CI pruning."""
        base_stats = copy.deepcopy(base_stats_cache) if base_stats_cache is not None else CandidateStats(base_cand, delta_tuple=base_cand)
        if delta_pool and len(delta_pool) == len(candidate_pool):
            active_candidates = [
                CandidateStats(cand_tuple=c, delta_tuple=d)
                for c, d in zip(candidate_pool, delta_pool)
            ]
        else:
            active_candidates = [CandidateStats(c, delta_tuple=c) for c in candidate_pool]
        all_candidates = list(active_candidates)

        # ─── Optimal 3-Rung Geometry (x4 scale: [400, 1600, 6400]) ──────────
        rungs = []
        r = max(400, self.min_games)
        while r < self.max_games:
            rungs.append(r)
            r *= 4
        if not rungs or rungs[-1] < self.max_games:
            rungs.append(self.max_games)

        curr_games = 0
        t_start = time.time()

        print(
            f"\n🏁 [{label_prefix}] Pula: {len(active_candidates)} kandydatów | "
            f"Szczeble: {rungs} gier/setup (95% CI Statistical Pruning)"
        )

        for step_idx, target_games in enumerate(rungs, 1):
            delta_games = target_games - curr_games
            if delta_games <= 0:
                continue

            survivors = [c for c in active_candidates if not c.is_pruned]
            if not survivors:
                print(f"   🛑 Wszyscy kandydaci zostali statystycznie wyeliminowani (N={curr_games} gier/setup).")
                break

            need_simulate_base = base_stats.total_games_per_setup < target_games
            current_pool = ([base_stats] if need_simulate_base else []) + survivors

            task_list = []
            task_map = []
            task_idx = 0

            for cand_idx, cand_obj in enumerate(current_pool):
                for sname in self.setups:
                    task_seed = seed + step_idx * 10007 + (hash(cand_obj.id) % 5003)
                    task_args = (task_idx, sname, task_seed, 8, "C", cand_obj.params, delta_games)
                    task_list.append(task_args)
                    task_map.append((cand_idx, sname))
                    task_idx += 1

            step_label = f"Szczebel #{step_idx}/{len(rungs)} (N={target_games} gier) [{len(survivors)} kand]"
            batch_results = _simulate_flat_tasks_pool(task_list, self.workers, label=step_label)

            for t_id, summary in batch_results:
                cand_idx, sname = task_map[t_id]
                current_pool[cand_idx].summaries_per_setup.setdefault(sname, []).append(summary)

            curr_games = target_games
            for cand_obj in current_pool:
                cand_obj.total_games_per_setup = curr_games
                for sname, s_list in cand_obj.summaries_per_setup.items():
                    cand_obj.combined_summary_per_setup[sname] = merge_batch_summaries(s_list)
                cand_obj.update_metrics()
                cand_obj.dt = round(time.time() - t_start, 2)

            base_lb, base_ub = base_stats.ci_95

            # 4. Pure Statistical CI Pruning
            active_survivors = [c for c in active_candidates if not c.is_pruned]
            if active_survivors:
                best_score = max(c.score_4p_balance for c in active_survivors)
                floor_lb = (target_floor_score + self.min_delta - 2.5 * base_stats.score_se) if target_floor_score is not None else (base_lb + self.min_delta)
                ref_lb = max(base_lb + self.min_delta, floor_lb, best_score - 2.5 * base_stats.score_se)

                for c in active_survivors:
                    c_lb, c_ub = c.ci_95

                    # A. Telemetry & Vitality hard vetoes
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

                    # B. Pure Statistical Upper-Bound Pruning vs Base & Leader (95% CI)
                    if curr_games >= 200:
                        if c_ub < ref_lb - 0.05:
                            c.is_pruned = True
                            c.prune_reason = f"Brak statystycznych szans na zysk (UB {c_ub:.2f} < Wymagany LB {ref_lb:.2f})"
                            continue

            active_survivors = [c for c in active_candidates if not c.is_pruned]
            pruned_count = len(all_candidates) - len(active_survivors)
            print(
                f"   📊 [Status N={curr_games}] Baza: {base_stats.score_4p_balance:.1f} pkt (±{base_stats.score_se:.2f}) | "
                f"Aktywnych: {len(active_survivors)}/{len(all_candidates)} (Odrzucono: {pruned_count})"
            )

            # 5. Convergence & Early Stop Check
            if curr_games >= self.min_games and active_survivors:
                active_survivors.sort(key=lambda x: rank_key(x.to_result_dict()))
                leader = active_survivors[0]
                l_lb, l_ub = leader.ci_95

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

                    if l_lb > r_ub and l_lb > base_ub:
                        print(
                            f"   🏆 Wyłoniono bezdyskusyjnego lidera: {leader.id} (LB {l_lb:.2f} > Drugi UB {r_ub:.2f}) "
                            f"po {curr_games} grach/setup."
                        )
                        break

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


def merge_mutations(m1: tuple[str, str, dict], m2: tuple[str, str, dict]) -> tuple[str, str, dict] | None:
    """Merges two mutations into a composite mutation (2D, 3D, 4D)."""
    id1, name1, p1 = m1
    id2, name2, p2 = m2

    parts1 = id1.split("__")
    parts2 = id2.split("__")
    if set(parts1) & set(parts2):
        return None

    cards1 = p1.get("card_overrides", {})
    cards2 = p2.get("card_overrides", {})
    for cid, c_dict in cards2.items():
        if cid in cards1:
            if set(c_dict.keys()) & set(cards1[cid].keys()):
                return None

    # Canonical sorting of atomic mutation parts eliminates commutative duplicates (A+B == B+A)
    all_parts = sorted(parts1 + parts2)
    combined_id = "__".join(all_parts)

    names1 = [n.strip() for n in name1.split("+")]
    names2 = [n.strip() for n in name2.split("+")]
    combined_name = " + ".join(sorted(names1 + names2))

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


def merge_override_dicts(base_dict: dict, delta_dict: dict) -> dict:
    """Deep merges delta_dict on top of base_dict."""
    out = copy.deepcopy(base_dict)
    for k, v in delta_dict.items():
        if k == "card_overrides":
            if "card_overrides" not in out:
                out["card_overrides"] = {}
            for cid, c_dict in v.items():
                if cid not in out["card_overrides"]:
                    out["card_overrides"][cid] = {}
                out["card_overrides"][cid].update(c_dict)
        else:
            if k.endswith("_offset") and k in out:
                out[k] += v
            else:
                out[k] = v
    return out


def extract_config_overrides(cfg: dict, setup_type: str = "4p") -> dict:
    """Extracts all card and victory rule deviations in cfg relative to the C++ hardcoded baseline snapshot."""
    ov = {}
    cards = cfg.get("cards", {})
    card_ov = {}
    for cid, cdata in cards.items():
        diff = {}
        for k in ["cost", "heresy", "target_heresy", "gold"]:
            if k in cdata:
                diff[k] = cdata[k]
        if diff:
            card_ov[cid] = diff
    if card_ov:
        ov["card_overrides"] = card_ov

    def _get_val(val, stype):
        if isinstance(val, dict):
            return val.get(stype, val.get("4p", 0))
        return val

    sys = cfg.get("system", {})
    if "accusation_threshold" in sys:
        ov["threshold_offset"] = _get_val(sys["accusation_threshold"], setup_type) - 7
    if "start_gold" in sys:
        ov["start_gold_offset"] = _get_val(sys["start_gold"], setup_type) - 4
    if "hand_limit" in sys:
        ov["hand_limit_offset"] = _get_val(sys["hand_limit"], setup_type) - 5
    if "max_eras" in sys:
        ov["max_eras_offset"] = _get_val(sys["max_eras"], setup_type) - 15
    if "cards_per_era" in sys:
        ov["cards_per_era_offset"] = _get_val(sys["cards_per_era"], setup_type) - 2
    if "intrigue_gold" in sys:
        ov["intrigue_gold_offset"] = _get_val(sys["intrigue_gold"], setup_type) - 1
    if "observed_threshold" in sys:
        ov["observed_threshold_offset"] = _get_val(sys["observed_threshold"], setup_type) - 3
    if "autodafe_cooldown" in sys:
        ov["cooldown_offset"] = _get_val(sys["autodafe_cooldown"], setup_type) - 3

    vic = cfg.get("victory", {})
    if "swiete_oficjum" in vic and "stacks" in vic["swiete_oficjum"]:
        ov["so_stacks_offset"] = _get_val(vic["swiete_oficjum"]["stacks"], setup_type) - 7
    if "korona_borgiowie" in vic and "decrees" in vic["korona_borgiowie"]:
        ov["kb_decrees_offset"] = _get_val(vic["korona_borgiowie"]["decrees"], setup_type) - 2
    if "cienie_al_andalus" in vic and "relics" in vic["cienie_al_andalus"]:
        ov["caa_relics_offset"] = _get_val(vic["cienie_al_andalus"]["relics"], setup_type) - 2
    if "kabala_toledo" in vic and "fragments" in vic["kabala_toledo"]:
        ov["kt_frags_offset"] = _get_val(vic["kabala_toledo"]["fragments"], setup_type) - 3
    if "gildia_cieni" in vic and "falls" in vic["gildia_cieni"]:
        ov["gc_falls_offset"] = _get_val(vic["gildia_cieni"]["falls"], setup_type) - 9
    return ov
