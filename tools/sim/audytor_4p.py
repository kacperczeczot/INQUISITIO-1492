#!/usr/bin/env python3
"""INQUISITIO-1492 — AUDYTOR 4P MAKRO (4-Player Autonomous Macro-Balance Optimizer).

Bliźniaczy, autonomiczny optymalizator balansu dla Kanonu 4P oparty na architekturze
Audytora Kanonu, zoptymalizowany pod kątem parametrów makro (L1, L2, L4) bez kart (L3).

Główne założenia metodologiczne:
  1. Kanon 4P (5 setupów 4-osobowych):
     - 4p-core
     - 4p-no-cienie
     - 4p-no-kabala
     - 4p-no-korona
     - 4p-no-oficjum
  2. Błyskawiczny 3-Stopniowy Lejek Sukcesywnej Selekcji (L1 + L2 + L4):
     - Etap 1 (Szybki Przesiew): 200 gier/setup × 5 setupów -> TOP 24 półfinalistów
     - Etap 2 (Głęboki Przesiew): 1000 gier/setup × 5 setupów -> TOP 12 finalistów
     - Etap 3 (Weryfikacja Ultra): 5000 gier/setup × 5 setupów -> Zwycięski Patch
  3. Ciągła Pętla Progresywna (Progressive Beam Search 1D -> 2D -> 3D -> ...):
     - Jeśli w danej fazie (np. 1D) żaden wariant nie daje zysku, skrypt automatycznie
       kwalifikuje TOP nasiona i eskaluje do kolejnej fazy (2D, 3D itd.), działając
       w pętli ciągłej aż do osiągnięcia optimum lub przerwania (Ctrl+C / limit czasu).
  4. Pełna automatyzacja dokumentacji i SSOT:
     - Aktualizacja game_config.yaml (z podbiciem wersji)
     - playtesting/sim-reports/logs/audytor_4p_log.md
     - playtesting/balance-notes.md
     - Pełna synchronizacja kart, katalogu i zasad (sync_config.py)
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

# Import test builders (L1, L2, L4 only - no cards L3)
import audit_level1
import audit_level2
import audit_level4

REPORTS_DIR = Path(__file__).resolve().parent.parent.parent / "playtesting" / "sim-reports"
BALANCE_NOTES_PATH = Path(__file__).resolve().parent.parent.parent / "playtesting" / "balance-notes.md"

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


def passes_telemetry_safety(res: dict) -> tuple[bool, str]:
    """Verify that candidate results stay within safety margins."""
    if res.get("deadlock_pct", 0) > 5.0:
        return False, f"Deadlock {res['deadlock_pct']:.1f}% > 5.0%"
    if res.get("poverty_pct", 0) > 30.0:
        return False, f"Pas Biedy {res['poverty_pct']:.1f}% > 30.0%"
    eras = res.get("eras_avg", 5.5)
    if eras < 4.0 or eras > 8.0:
        return False, f"Średnia Er {eras:.2f} poza zakresem [4.0, 8.0]"
    return True, "OK"


def _run_single_test_task_4p(args_tuple: tuple) -> dict:
    """Worker task evaluating a single candidate mutation across 4P setups."""
    (cand_id, cand_name, rule_params), games_per_setup, seed, setups = args_tuple

    summaries = []
    setup_scores = {}
    fshares = {fid: [] for fid in FACTION_NAMES.keys()}

    for sname in setups:
        s = run_batch(games=games_per_setup, setup=sname, seed=seed, layer="C", win_overrides=rule_params)
        summaries.append(s)
        sc = calculate_setup_score(s)
        setup_scores[sname] = sc
        for fid, wins in s.wins.items():
            if s.games > 0:
                fid_enum = FactionId(fid) if not isinstance(fid, FactionId) else fid
                if fid_enum in fshares:
                    fshares[fid_enum].append(wins / s.games)

    score_4p = round(sum(setup_scores.values()) / len(setup_scores), 1) if setup_scores else 0.0
    n_sum = len(summaries) if summaries else 1
    eras_avg = sum(s.eras_avg for s in summaries) / n_sum
    eras_min = min(s.eras_min for s in summaries) if summaries else 0
    eras_max = max(s.eras_max for s in summaries) if summaries else 0
    deadlock_pct = (sum(s.eras_limit_pct for s in summaries) / n_sum) * 100.0
    poverty_pct = (sum(s.passes_forced_pct for s in summaries) / n_sum) * 100.0
    autodafe_avg = sum(s.autodafe_avg for s in summaries) / n_sum
    acc_avg = sum(s.accusations_avg for s in summaries) / n_sum
    gold_avg = sum(s.avg_gold_end for s in summaries) / n_sum

    return {
        "id": cand_id,
        "name": cand_name,
        "params": rule_params,
        "score_4p": score_4p,
        "setup_scores": setup_scores,
        "fshares": {FACTION_NAMES[k]: round(sum(v)/len(v)*100, 1) for k, v in fshares.items() if v},
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


def generate_all_atomic_candidates_macro() -> list[tuple[str, str, dict]]:
    """Builds atomic candidate pool for macro parameters (L1, L2, L4) excluding cards (L3)."""
    tests = []
    # Level 1 (Core System Parameters)
    tests.extend([t for t in audit_level1.build_level1_tests() if t[0] != "L1_BAZA"])
    # Level 2 (Faction Victory Conditions)
    tests.extend([t for t in audit_level2.build_level2_tests() if t[0] != "L2_BAZA"])
    # Level 4 (Niche Variants & Edicts)
    tests.extend([t for t in audit_level4.build_level4_tests() if t[0] != "L4_BAZA"])
    return tests


def merge_mutations(m1: tuple[str, str, dict], m2: tuple[str, str, dict]) -> tuple[str, str, dict] | None:
    """Merges two mutations into a composite mutation (e.g. 2D pair or 3D triple)."""
    id1, name1, p1 = m1
    id2, name2, p2 = m2

    keys1 = set(p1.keys())
    keys2 = set(p2.keys())
    if keys1 & keys2:
        return None

    combined_id = f"{id1}__{id2}"
    combined_name = f"{name1} + {name2}"
    merged_params = copy.deepcopy(p1)
    merged_params.update(p2)
    return (combined_id, combined_name, merged_params)


def update_balance_notes_4p(
    old_version: str,
    new_version: str,
    change_desc: str,
    rule_id: str,
    base_res_4p: dict,
    best_res_4p: dict,
    diag_before: dict,
    diag_after: dict,
):
    """Automatically update playtesting/balance-notes.md with patch note entry."""
    if not BALANCE_NOTES_PATH.exists():
        return

    content = BALANCE_NOTES_PATH.read_text(encoding="utf-8")
    today = datetime.now().strftime("%Y-%m-%d")
    d_4p = best_res_4p["score_4p"] - base_res_4p["score_4p"]
    delta_4p_str = f"+{d_4p:.1f}" if d_4p > 0 else f"{d_4p:.1f}"

    patch_note_block = (
        f"### 🟢 Patch {new_version} ({today}) — Kanon 4P Makro: {change_desc} (Zysk 4P Δ {delta_4p_str} pkt)\n"
        f"- **Wynik 4P:** Kanon **`{base_res_4p['score_4p']:.1f}`** → **`{best_res_4p['score_4p']:.1f} pkt`** | Global **`{diag_after['global_score']:.1f}`** | 3p **`{diag_after['cat_scores'].get('3p',0.0):.1f}`** | 5p **`{diag_after['cat_scores'].get('5p',0.0):.1f}`**\n"
        f"- **Modyfikacja (`{rule_id}`):** {change_desc}.\n"
        f"- **Efekt:** Optymalizacja parametrów makro 4P. Telemetria: Średnia Er {best_res_4p['eras_avg']:.2f}, Deadlocks {best_res_4p['deadlock_pct']:.1f}%, Pas Biedy {best_res_4p['poverty_pct']:.1f}%.\n\n"
    )

    history_heading = "## 📜 Chronologiczna Historia Zmian Balansu (Faza Prototypowa — Patch Notes)\n\n"
    if history_heading in content:
        content = content.replace(history_heading, history_heading + patch_note_block, 1)

    BALANCE_NOTES_PATH.write_text(content, encoding="utf-8")


def log_4p_iteration(
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
    """Appends an iteration entry to audytor_4p_log.md."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    if not log_path.exists():
        headers = [
            "# Dziennik Optymalizacji Kanonu 4P Makro (Audytor 4P)",
            "",
            "Rejestr wdrożonych patchów makro (L1, L2, L4) dla Kanonu 4-osobowego.",
            "",
            "| Iteracja | Faza | Data i Czas | Wersja | Modyfikacja 4P | 4P Score | Wpływ na 3p | Wpływ na 5p | Global Score | Deadlocks % | Pas Biedy % | Czas |",
            "| :---: | :---: | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
        ]
        log_path.write_text("\n".join(headers) + "\n", encoding="utf-8")

    d_4p = best_res_4p["score_4p"] - base_res_4p["score_4p"]
    d4_str = f"+{d_4p:.1f}" if d_4p > 0 else f"{d_4p:.1f}"

    d_3p = diag_after["cat_scores"].get("3p", 0) - diag_before["cat_scores"].get("3p", 0)
    d3_str = f"+{d_3p:.1f}" if d_3p > 0 else f"{d_3p:.1f}"

    d_5p = diag_after["cat_scores"].get("5p", 0) - diag_before["cat_scores"].get("5p", 0)
    d5_str = f"+{d_5p:.1f}" if d_5p > 0 else f"{d_5p:.1f}"

    d_glob = diag_after["global_score"] - diag_before["global_score"]
    dg_str = f"+{d_glob:.1f}" if d_glob > 0 else f"{d_glob:.1f}"

    score_4p_col = f"{base_res_4p['score_4p']:.1f} → **{best_res_4p['score_4p']:.1f}** (`{d4_str}`)"
    p3_col = f"{diag_before['cat_scores'].get('3p',0):.1f} → {diag_after['cat_scores'].get('3p',0):.1f} (`{d3_str}`)"
    p5_col = f"{diag_before['cat_scores'].get('5p',0):.1f} → {diag_after['cat_scores'].get('5p',0):.1f} (`{d5_str}`)"
    glob_col = f"{diag_before['global_score']:.1f} → **{diag_after['global_score']:.1f}** (`{dg_str}`)"

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    row = (
        f"| #{iteration} | {phase}D | {now_str} | `{new_version}` | {desc} | "
        f"{score_4p_col} | {p3_col} | {p5_col} | {glob_col} | "
        f"{best_res_4p['deadlock_pct']:.1f}% | {best_res_4p['poverty_pct']:.1f}% | {elapsed_iter:.1f}s |"
    )
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(row + "\n")


class Macro4PAutoBalancer:
    """Autonomous continuous balancer for Canonical 4P macro parameters."""

    def __init__(self, args: argparse.Namespace):
        self.args = args
        self.total_iterations = 0
        self.start_time = time.time()
        self.stop_requested = False
        signal.signal(signal.SIGINT, self._handle_sigint)

    def _handle_sigint(self, signum, frame):
        print("\n\n⚠️ Otrzymano sygnał przerwania (Ctrl+C). Bezpiecznie kończę bieżącą iterację...")
        self.stop_requested = True

    def _execute_pool(self, task_func, task_list: list, label: str = "Testy 4P") -> list[dict]:
        total = len(task_list)
        if total == 0:
            return []

        workers = min(self.args.workers, total)
        results = []
        t0 = time.time()
        with ProcessPoolExecutor(max_workers=workers) as executor:
            from concurrent.futures import as_completed
            future_to_task = {executor.submit(task_func, t): t for t in task_list}
            best_so_far = None

            for idx, future in enumerate(as_completed(future_to_task), 1):
                res = future.result()
                results.append(res)
                if best_so_far is None or res["score_4p"] > best_so_far["score_4p"]:
                    best_so_far = res

                elapsed = time.time() - t0
                rate = idx / elapsed if elapsed > 0 else 0
                eta_s = (total - idx) / rate if rate > 0 else 0
                eta_str = f"{int(eta_s // 60)}m {int(eta_s % 60):02d}s" if eta_s >= 60 else f"{int(eta_s)}s"
                lead_id = best_so_far['id'][:26] if best_so_far else "-"
                lead_sc = f"{best_so_far['score_4p']:.1f}" if best_so_far else "-"
                sys.stdout.write(f"\r⏳ [{label}] [{idx:4d}/{total:4d}] ({idx*100.0/total:5.1f}%) | {rate:4.1f} zad/s | ETA: {eta_str:<7s} | Lider 4P: {lead_id} ({lead_sc} pkt)  ")
                sys.stdout.flush()

        sys.stdout.write(f"\n   ✔ Ukończono {total} zadań w {round(time.time() - t0, 1)}s.\n")
        return results

    def run(self):
        print("═══════════════════════════════════════════════════════════════════════")
        print("   INQUISITIO-1492 — AUDYTOR 4P MAKRO (Continuous Lookahead Optimizer) ")
        print("   Optymalizacja parametrów makro L1, L2, L4 dla 5 setupów Kanonu 4P   ")
        print("═══════════════════════════════════════════════════════════════════════")
        print(f"Bieżąca wersja bazowa:      {CONFIG.version}")
        print(f"Maksymalny czas sesji:      {self.args.hours if self.args.hours else 'Brak limitu (do optimum)'} godz.")
        print(f"Maksymalnie patchów:        {self.args.max_iters if self.args.max_iters else 'Brak (do optimum)'}")
        print(f"Kanon Setupy:               {', '.join(CANONICAL_4P_SETUPS)}")
        print(f"Etap 1 (Szybki przesiew):   {self.args.fast_games} gier/setup ({len(CANONICAL_4P_SETUPS)} setupów 4p)")
        print(f"Etap 2 (Głęboki przesiew):  {self.args.screen_games} gier/setup (TOP {self.args.top_semifinalists} półfinalistów)")
        print(f"Etap 3 (Weryfikacja Ultra): {self.args.confirm_games} gier/setup (TOP {self.args.top_k} finalistów)")
        print(f"Wątki procesora:            {self.args.workers}")
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

            print(f"   🎯 Wynik Kanonu 4P Score: {color_score(base_res['score_4p'], bold=True)} pkt")
            for sname, sc in sorted(base_res["setup_scores"].items()):
                print(f"      • `{sname}`: {color_score(sc, bold=True)} pkt")
            print(f"   ⏱️ Średnia Er: {base_res['eras_avg']:.2f} | Deadlocks: {base_res['deadlock_pct']:.1f}% | Pas Biedy: {base_res['poverty_pct']:.1f}%")

            # 2. Candidate Pool
            atomic_pool = generate_all_atomic_candidates_macro()

            if current_phase == 1 or not beam_seeds:
                print(f"\n🌐 [FAZA 1D — MAKRO 4P] Pełna pula atomowa L1, L2, L4 ({len(atomic_pool)} wariantów)...")
                candidate_pool = atomic_pool
            else:
                print(f"\n🌐 [FAZA {current_phase}D — MAKRO 4P] Wiązki 4P (TOP {len(beam_seeds)} nasion × {len(atomic_pool)} mechanik)...")
                composite_pool = []
                for seed_mut in beam_seeds:
                    for atomic_mut in atomic_pool:
                        merged = merge_mutations(seed_mut, atomic_mut)
                        if merged:
                            composite_pool.append(merged)

                seen_ids = set()
                candidate_pool = []
                for c in composite_pool:
                    norm_id = "__".join(sorted(c[0].split("__")))
                    if norm_id not in seen_ids:
                        seen_ids.add(norm_id)
                        candidate_pool.append(c)

            print(f"   🧬 Wygenerowano {len(candidate_pool)} unikalnych kandydatów dla Kanonu 4P.")
            cand_dict = {c[0]: c for c in candidate_pool}

            # 3. ETAP 1/3: Szybki Przesiew na 5 setupach 4P
            print(f"\n--- [ETAP 1/3: SZYBKI PRZESIEW 4P] Testuję {len(candidate_pool)} kandydatów ({self.args.fast_games} gier/setup × 5 setupów) ---")
            stage1_tasks = [((c[0], c[1], c[2]), self.args.fast_games, self.args.seed, setups) for c in candidate_pool]
            stage1_results = self._execute_pool(_run_single_test_task_4p, stage1_tasks, label=f"Przesiew 4P 1/3")

            stage1_results.sort(key=lambda r: r["score_4p"], reverse=True)

            n_semifinalists = min(self.args.top_semifinalists, len(stage1_results))
            semifinalist_results = stage1_results[:n_semifinalists]
            semifinalist_candidates = [cand_dict[r["id"]] for r in semifinalist_results]

            # 4. ETAP 2/3: Głęboki Przesiew 4P
            print(f"\n--- [ETAP 2/3: GŁĘBOKI PRZESIEW 4P] Badam TOP {len(semifinalist_candidates)} półfinalistów ({self.args.screen_games} gier/setup × 5 setupów) ---")
            stage2_tasks = [((c[0], c[1], c[2]), self.args.screen_games, self.args.seed, setups) for c in semifinalist_candidates]
            stage2_results = self._execute_pool(_run_single_test_task_4p, stage2_tasks, label=f"Przesiew 4P 2/3")

            stage2_results.sort(key=lambda r: r["score_4p"], reverse=True)

            n_finalists = min(self.args.top_k, len(stage2_results))
            finalist_results = stage2_results[:n_finalists]
            finalist_candidates = [cand_dict[r["id"]] for r in finalist_results]

            # 5. ETAP 3/3: Weryfikacja Ultra 4P
            print(f"\n--- [ETAP 3/3: WERYFIKACJA ULTRA 4P] Weryfikuję TOP {len(finalist_candidates)} finalistów ({self.args.confirm_games} gier/setup × 5 setupów) ---")
            stage3_tasks = [((c[0], c[1], c[2]), self.args.confirm_games, self.args.seed, setups) for c in finalist_candidates]
            stage3_results = self._execute_pool(_run_single_test_task_4p, stage3_tasks, label=f"Weryfikacja 4P 3/3")

            stage3_results.sort(key=lambda r: r["score_4p"], reverse=True)

            print(f"\n📊 [WYNIKI WERYFIKACJI FINALISTÓW KANONU 4P]")
            for idx, r in enumerate(stage3_results, 1):
                d_4 = r["score_4p"] - base_res["score_4p"]
                is_safe, msg = passes_telemetry_safety(r)
                sign = f"+{d_4:.2f}" if d_4 > 0 else f"{d_4:.2f}"
                print(f"   #{idx:2d} [{r['id'][:42]}...] 4P Score: {base_res['score_4p']:.1f} → {r['score_4p']:.1f} (Δ {sign}) | {msg}")

            accepted_candidate = None
            best_ver_res = None

            for ver_res in stage3_results:
                d_4p = ver_res["score_4p"] - base_res["score_4p"]
                is_safe, safe_msg = passes_telemetry_safety(ver_res)

                if is_safe and d_4p >= self.args.min_delta:
                    accepted_candidate = cand_dict[ver_res["id"]]
                    best_ver_res = ver_res
                    break

            # 6. Apply Patch & Measure Collateral Impact
            if accepted_candidate and best_ver_res is not None:
                self.total_iterations += 1
                rule_id, rule_name, rule_params = accepted_candidate

                with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
                    raw_cfg = yaml.safe_load(f)

                old_version = raw_cfg.get("version", "v0.51")
                mod_cfg, change_desc = apply_mutation_to_config(raw_cfg, rule_id, rule_params)

                # Cross-impact diagnosis
                print(f"\n🔬 [DIAGNOZA WPŁYWU NA POZOSTAŁE TRYBY (3P / 5P)]...")
                diag_before = _run_full_diagnostic({}, games_per_setup=1000, seed=self.args.seed)
                diag_after = _run_full_diagnostic(rule_params, games_per_setup=1000, seed=self.args.seed)

                d_3 = diag_after["cat_scores"].get("3p", 0) - diag_before["cat_scores"].get("3p", 0)
                d_5 = diag_after["cat_scores"].get("5p", 0) - diag_before["cat_scores"].get("5p", 0)
                d_g = diag_after["global_score"] - diag_before["global_score"]

                d3_sign = f"+{d_3:.1f}" if d_3 > 0 else f"{d_3:.1f}"
                d5_sign = f"+{d_5:.1f}" if d_5 > 0 else f"{d_5:.1f}"
                dg_sign = f"+{d_g:.1f}" if d_g > 0 else f"{d_g:.1f}"

                print(f"   🎯 4P Kanon:  {base_res['score_4p']:.1f} → **{best_ver_res['score_4p']:.1f} pkt** (Δ {best_ver_res['score_4p'] - base_res['score_4p']:+.2f} pkt)")
                print(f"   👥 Wpływ 3p:  {diag_before['cat_scores'].get('3p',0):.1f} → {diag_after['cat_scores'].get('3p',0):.1f} pkt (`{d3_sign} pkt`)")
                print(f"   👥 Wpływ 5p:  {diag_before['cat_scores'].get('5p',0):.1f} → {diag_after['cat_scores'].get('5p',0):.1f} pkt (`{d5_sign} pkt`)")
                print(f"   🌐 Globalny:  {diag_before['global_score']:.1f} → {diag_after['global_score']:.1f} pkt (`{dg_sign} pkt`)")

                if self.args.dry_run:
                    print(f"\n[DRY RUN] Zaakceptowano by modyfikację Kanonu 4P: {change_desc}")
                    current_phase += 1
                else:
                    new_version, saved_path = save_config_and_bump_version(mod_cfg, _CONFIG_PATH, bump_version=True)
                    iter_elapsed = round(time.time() - iter_start, 2)

                    print(f"\n🎉 [ZAAKCEPTOWANO PATCH KANONU 4P MAKRO #{self.total_iterations} — FAZA {current_phase}D]")
                    print(f"   Wersja:        `{old_version}` → **`{new_version}`**")
                    print(f"   Modyfikacja:   {change_desc}")

                    version_archive_dir = REPORTS_DIR / "archive" / new_version
                    version_archive_dir.mkdir(parents=True, exist_ok=True)
                    log_path = version_archive_dir / "audytor_4p_log.md"

                    log_4p_iteration(
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

                    print("   📑 Aktualizuję playtesting/balance-notes.md...")
                    update_balance_notes_4p(
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
                print(f"\n⚪ Brak wariantu z dodatnim zyskiem dla Kanonu 4P (Δ ≥ +{self.args.min_delta} pkt) w Fazie {current_phase}D.")
                top_beam_results = stage3_results[: self.args.beam_width]
                beam_seeds = [cand_dict[r["id"]] for r in top_beam_results]
                current_phase += 1
                print(f"🔄 Kwalifikuję TOP {len(beam_seeds)} nasion wiązki i ESKALUJĘ DO FAZY {current_phase}D...\n")

        print(f"\n═══════════════════════════════════════════════════════════════════════")
        print(f"   AUDYTOR 4P MAKRO ZAKOŃCZYŁ SESJĘ. ŁĄCZNIE WPROWADZONO {self.total_iterations} PATCHY.")
        print(f"═══════════════════════════════════════════════════════════════════════\n")


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 Audytor 4P Makro (Continuous Macro Optimizer)")
    parser.add_argument("--hours", type=float, default=None, help="Maksymalny czas działania w godzinach (np. 4.0)")
    parser.add_argument("--max-iters", type=int, default=None, help="Maksymalna liczba udanych patchów przed zatrzymaniem")
    parser.add_argument("--fast-games", type=int, default=200, help="Liczba gier w Etapie 1 na 5 setupach 4p (domyślnie: 200)")
    parser.add_argument("--screen-games", type=int, default=1000, help="Liczba gier w Etapie 2 na 5 setupach 4p (domyślnie: 1000)")
    parser.add_argument("--confirm-games", type=int, default=5000, help="Liczba gier w Etapie 3 na 5 setupach 4p (domyślnie: 5000)")
    parser.add_argument("--top-semifinalists", type=int, default=30, help="Liczba półfinalistów sprawdzanych w Etapie 2 (domyślnie: 30)")
    parser.add_argument("--top-k", type=int, default=15, help="Liczba finalistów sprawdzanych w Etapie 3 (domyślnie: 15)")
    parser.add_argument("--beam-width", type=int, default=8, help="Liczba najlepszych kandydatów kwalifikowanych do nasion kolejnej fazy wiązek (domyślnie: 8)")
    parser.add_argument("--min-delta", type=float, default=0.05, help="Minimalny zysk punktowy dla 4P wymagany do wdrożenia patcha (pkt, domyślnie: 0.05)")
    parser.add_argument("--workers", type=int, default=min(os.cpu_count() or 4, 10), help="Liczba procesów równoległych")
    parser.add_argument("--seed", type=int, default=42, help="Ziarno generatora liczb losowych")
    parser.add_argument("--dry-run", action="store_true", help="Tryb symulacji bez zapisywania zmian do game_config.yaml")

    args = parser.parse_args()

    if args.fast_games < 100:
        args.fast_games = 100
    if args.screen_games < 500:
        args.screen_games = 500
    if args.confirm_games < 2500:
        args.confirm_games = 2500

    auditor = Macro4PAutoBalancer(args)
    auditor.run()


if __name__ == "__main__":
    main()
