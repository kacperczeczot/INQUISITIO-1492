#!/usr/bin/env python3
"""INQUISITIO-1492 — SZALONY AUDYTOR / AUTONOMOUS BALANCE OPTIMIZER.

Autonomously explores the parameter space (Levels 1–4), finds the single best
balance improvement (highest delta global), applies the change to game_config.yaml,
bumps the version, archives snapshots, and repeats in a continuous hill-climbing loop
until a global optimum is reached or time limit expires.
"""
from __future__ import annotations

import argparse
import copy
import os
import signal
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
from inquisitio.engine.setup import SETUP_PRESETS
from inquisitio.runner.audit_facts import score_pair
from inquisitio.runner.batch import run_batch
from inquisitio.runner.scoring import (
    calculate_category_scores,
    calculate_global_score,
    color_score,
)

# Import test builders
import audit_level1
import audit_level2
import audit_level3
import audit_level4

LOG_FILE_PATH = Path(__file__).resolve().parent.parent.parent / "playtesting" / "sim-reports" / "auto_balancer_log.md"


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
        print("═══════════════════════════════════════════════════════════════════════\n")

        setups = sorted(SETUP_PRESETS.keys())
        time_limit_sec = (self.args.hours * 3600) if self.args.hours else None

        while not self.stop_requested:
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
            print(f"▶ ITERACJA #{self.total_iterations} — Wersja: {CONFIG.version} | Czas łączny: {round((time.time() - self.start_time)/60, 1)} min")
            print(f"{'='*71}")

            # 1. Generate all candidate tests for current config
            candidate_tests = generate_candidate_tests(
                level_filter=self.args.level,
                param_filter=self.args.param,
                card_filter=self.args.card,
            )
            print(f"Wygenerowano {len(candidate_tests)} wariantów testowych (Poziomy: {self.args.level}).")

            # 2. Strategy Execution (Two-Stage or Direct)
            if self.args.mode == "two-stage":
                best_candidate, base_res, best_res = self._run_two_stage(candidate_tests, setups)
            else:
                games_per_setup = (
                    3000 if self.args.mode == "grand"
                    else (500 if self.args.mode == "standard" else 250)
                )
                best_candidate, base_res, best_res = self._run_direct_stage(candidate_tests, setups, games_per_setup)

            if self.stop_requested:
                break

            if not best_candidate or best_res is None or base_res is None:
                print("\n🏁 Brak kandydatów lub błąd ewaluacji. Kończę.")
                break

            delta_global = best_res["global_score"] - base_res["global_score"]
            print(f"\n📊 Wynik Bazy: {color_score(base_res['global_score'], bold=True)} pkt")
            print(f"🌟 Najlepszy kandydat: [{best_res['id']}] {best_res['name']}")
            print(f"   Nowy Global Score:  {color_score(best_res['global_score'], bold=True)} pkt (Δ {delta_global:+5.2f} pkt)")

            # Check if improvement exceeds threshold
            if delta_global < self.args.min_delta:
                print(f"\n🏆 OSIĄGNIĘTO LOKALNE OPTIMUM GLOBALNE!")
                print(f"Żadna z {len(candidate_tests)} modyfikacji nie przynosi zysku >= +{self.args.min_delta} pkt.")
                print(f"Najwyższy dostępny zysk: {delta_global:+5.2f} pkt.")
                break

            # 3. Apply modification to game_config.yaml
            rule_id, rule_name, rule_params = best_candidate
            with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
                raw_cfg = yaml.safe_load(f)

            old_version = raw_cfg.get("version", "v0.19")
            mod_cfg, change_desc = apply_mutation_to_config(raw_cfg, rule_id, rule_params)

            if self.args.dry_run:
                print(f"\n[DRY RUN] Zastosowano by zmianę: {change_desc}")
                print(f"[DRY RUN] Podbito by wersję z {old_version} do nowej.")
                break
            else:
                new_version, saved_path = save_config_and_bump_version(mod_cfg, _CONFIG_PATH, bump_version=True)
                iter_elapsed = round(time.time() - iter_start, 2)
                print(f"\n✅ ZAPISANO ZMIANĘ DO: {saved_path.name}")
                print(f"   Opis zmiany:  {change_desc}")
                print(f"   Wersja:       {old_version} → {new_version}")
                print(f"   Zysk Balansu: {score_pair(base_res['global_score'], best_res['global_score'], colored=True)}")

                # Log to auto_balancer_log.md
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

        self._print_final_summary()

    def _run_two_stage(self, tests: list[tuple[str, str, dict]], setups: list[str]):
        """Stage 1: Fast screening (e.g. 250 games). Stage 2: Deep verification (1500 games) for top 5."""
        stage1_games = self.args.fast_games
        stage2_games = self.args.confirm_games

        print(f"\n--- [KROK 1/2: SZYBKI PRZESIEW] Próba: {stage1_games} gier/setup ({len(tests)} wariantów) ---")
        task_list = [(t, stage1_games, self.args.seed, setups) for t in tests]
        results = self._execute_pool(task_list)

        base_s1 = results[0]
        # Filter strictly positive delta and safety
        positives = []
        for r in results[1:]:
            delta = r["global_score"] - base_s1["global_score"]
            is_safe, _ = passes_telemetry_safety(r)
            if delta > 0.05 and is_safe:
                positives.append(r)

        positives.sort(key=lambda x: x["global_score"] - base_s1["global_score"], reverse=True)

        if not positives:
            print("Brak kandydatów przynoszących poprawę w przesiewie.")
            return None, base_s1, None

        top_k = positives[: self.args.top_k]
        print(f"\n--- [KROK 2/2: PRECYZYJNA WERYFIKACJA] Badam TOP {len(top_k)} liderów na próbie {stage2_games} gier/setup ---")

        # Map back to test tuples
        test_dict = {t[0]: t for t in tests}
        verify_tests = [tests[0]] + [test_dict[r["id"]] for r in top_k]

        verify_tasks = [(t, stage2_games, self.args.seed + 999, setups) for t in verify_tests]
        verified_results = self._execute_pool(verify_tasks)

        base_s2 = verified_results[0]
        verified_candidates = []

        for r in verified_results[1:]:
            delta = r["global_score"] - base_s2["global_score"]
            is_safe, safe_msg = passes_telemetry_safety(r)
            if is_safe:
                verified_candidates.append(r)
            else:
                print(f"⚠️ Odrzucono kandydata [{r['id']}] z powodu telemetrii: {safe_msg}")

        if not verified_candidates:
            print("Żaden z liderów nie przeszedł pomyślnie weryfikacji i testów bezpieczeństwa.")
            return None, base_s2, None

        verified_candidates.sort(key=lambda x: x["global_score"] - base_s2["global_score"], reverse=True)
        best_res = verified_candidates[0]
        best_tuple = test_dict[best_res["id"]]

        return best_tuple, base_s2, best_res

    def _run_direct_stage(self, tests: list[tuple[str, str, dict]], setups: list[str], games_per_setup: int):
        """Single stage full evaluation."""
        print(f"\n--- [PEŁNA EWALUACJA] Próba: {games_per_setup} gier/setup ({len(tests)} wariantów) ---")
        task_list = [(t, games_per_setup, self.args.seed, setups) for t in tests]
        results = self._execute_pool(task_list)

        base_res = results[0]
        candidates = []
        for r in results[1:]:
            is_safe, _ = passes_telemetry_safety(r)
            if is_safe:
                candidates.append(r)

        if not candidates:
            return None, base_res, None

        candidates.sort(key=lambda x: x["global_score"] - base_res["global_score"], reverse=True)
        best_res = candidates[0]
        test_dict = {t[0]: t for t in tests}
        best_tuple = test_dict[best_res["id"]]

        return best_tuple, base_res, best_res

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
        print("═" * 71)


def main():
    parser = argparse.ArgumentParser(
        description="INQUISITIO-1492 — Szalony Audytor / Autonomous Balance Optimizer",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--mode", type=str, choices=["two-stage", "grand", "standard", "fast"], default="two-stage",
                        help="Tryb ewaluacji: two-stage (rekomendowany szybki przesiew + weryfikacja), grand (3k gier), standard (500), fast (250)")
    parser.add_argument("--fast-games", type=int, default=250, help="Liczba gier/setup w kroku 1 przesiewu (dla two-stage)")
    parser.add_argument("--confirm-games", type=int, default=1500, help="Liczba gier/setup w kroku 2 weryfikacji (dla two-stage)")
    parser.add_argument("--top-k", type=int, default=5, help="Liczba liderów weryfikowanych w kroku 2")
    parser.add_argument("--hours", type=float, default=None, help="Maksymalny czas działania w godzinach (np. 4.0)")
    parser.add_argument("--max-iters", type=int, default=None, help="Maksymalna liczba iteracji optymalizatora")
    parser.add_argument("--min-delta", type=float, default=0.1, help="Minimalny zysk punktowy (delta global) wymagany do zapisu")
    parser.add_argument("--level", type=str, choices=["all", "1", "2", "3", "4"], default="all", help="Filtruj poziomy testów")
    parser.add_argument("--param", type=str, default="cost,heresy", help="Parametry kart dla Poziomu 3 (cost, heresy, target_heresy, gold, all)")
    parser.add_argument("--card", type=str, default=None, help="Ogranicz poziom 3 do konkretnej karty (np. so-04)")
    parser.add_argument("--seed", type=int, default=42, help="Początkowe ziarno RNG")
    parser.add_argument("--workers", type=int, default=os.cpu_count() or 4, help="Liczba równoległych procesów CPU")
    parser.add_argument("--dry-run", action="store_true", help="Tryb symulacji bez zapisu zmian do game_config.yaml")

    args = parser.parse_args()
    auditor = AutoBalancer(args)
    auditor.run()


if __name__ == "__main__":
    main()
