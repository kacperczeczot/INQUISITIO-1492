#!/usr/bin/env python3
"""INQUISITIO-1492 — AUDYTOR 5P (5-Player Autonomous Balance Optimizer).

Autonomous optimizer for 5-player format exceptions (5p-full), powered by:
  1. Native C++20 simulation core.
  2. Multi-Fidelity Adaptive Sequential Racer (5p-full, 95% CI statistical pruning).
  3. Multi-dimensional Combinatorial Beam Search (1D -> 2D -> 3D -> 4D).
  4. Mandatory 10,000 games/setup validation gate with 4P Canon Collateral Guard.
  5. Strict SSOT automation (game_config.yaml '5p:' exceptions, sync_config, balance-notes.md).
"""
from __future__ import annotations

import argparse
import copy
import os
import shutil
import signal
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any

TOOLS_SRC_DIR = Path(__file__).resolve().parent
SRC_DIR = TOOLS_SRC_DIR.parent.parent / "src"

for p in (TOOLS_SRC_DIR, SRC_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

import yaml
from inquisitio.config import CONFIG, _CONFIG_PATH
from inquisitio.config_updater import save_config_and_bump_version
from inquisitio.engine.setup import SETUP_PRESETS, FactionId
from inquisitio.runner.adaptive_racer import (
    AdaptiveSequentialRacer,
    CandidateStats,
    extract_config_overrides,
    merge_mutations,
    merge_override_dicts,
)
from inquisitio.runner.batch import run_batch
from inquisitio.runner.canon_accept import accept_candidate, rank_key
from inquisitio.runner.scoring import (
    calculate_category_scores,
    calculate_global_score,
    calculate_setup_score,
    color_score,
    evaluate_vitality,
)

import audit_level1
import audit_level2
import audit_level4
from audytor_4p import (
    accept_format_exception,
    drop_dead_path_crutches,
    is_ablation_off,
    is_frozen_identity_knob,
    strip_table_wide_canon_params,
)

REPORTS_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "playtesting" / "sim-reports"
BALANCE_NOTES_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "playtesting" / "balance-notes.md"

SETUPS_5P = ["5p-full"]

FACTION_NAMES = {
    FactionId.SWIETE_OFICJUM: "SO",
    FactionId.CIENIE_AL_ANDALUS: "CAA",
    FactionId.KORONA_BORGIOWIE: "KB",
    FactionId.KABALA_TOLEDO: "KT",
    FactionId.GILDIA_CIENI: "GC",
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


def generate_all_atomic_candidates_5p() -> list[tuple[str, str, dict]]:
    """L1/L2/L4 for 5P exceptions (table-wide L3 cards are fixed by 4P canon)."""
    tests = []
    for builder, baza in (
        (audit_level1.build_level1_tests, "L1_BAZA"),
        (audit_level2.build_level2_tests, "L2_BAZA"),
        (audit_level4.build_level4_tests, "L4_BAZA"),
    ):
        for tid, tname, p in builder():
            if is_frozen_identity_knob(tid, p) or is_ablation_off(tid, p):
                continue
            cleaned = strip_table_wide_canon_params(p)
            if cleaned:
                tests.append((tid, tname, cleaned))

    seen = set()
    out = []
    for t in tests:
        if t[0] not in seen:
            seen.add(t[0])
            out.append(t)
    return out


def apply_mutation_to_5p_config(raw_cfg: dict[str, Any], rule_params: dict[str, Any]) -> tuple[dict[str, Any], str]:
    """Applies parameter overrides directly to 5p sections in config dict."""
    cfg = copy.deepcopy(raw_cfg)
    rule_params = strip_table_wide_canon_params(rule_params)
    descs = []

    def _set_5p(section_dict: dict, key: str, default_val: Any, offset: Any, desc_name: str):
        if offset is None:
            return
        off = int(offset)
        cur = section_dict.get(key, default_val)
        if isinstance(cur, dict):
            val_cand = cur.get("5p", cur.get("4p", default_val))
            base_v = int(val_cand) if val_cand is not None else int(default_val)
            new_v = max(1, base_v + off)
            cur["5p"] = new_v
        else:
            base_v = int(cur) if cur is not None else int(default_val)
            new_v = max(1, base_v + off)
            section_dict[key] = {"3p": cur, "4p": cur, "5p": new_v}
        descs.append(f"{desc_name} (5p): {new_v}")

    # L1
    if "start_gold_offset" in rule_params:
        _set_5p(cfg.setdefault("system", {}), "start_gold", 4, rule_params["start_gold_offset"], "Złoto startowe")
    if "threshold_offset" in rule_params:
        _set_5p(cfg.setdefault("system", {}), "accusation_threshold", 7, rule_params["threshold_offset"], "Próg oskarżenia")

    # L2
    vic = cfg.setdefault("victory", {})
    if "so_stacks_offset" in rule_params:
        _set_5p(vic.setdefault("swiete_oficjum", {}), "stacks", 7, rule_params["so_stacks_offset"], "SO Stosy")
    if "so_condemns_offset" in rule_params:
        _set_5p(vic.setdefault("swiete_oficjum", {}), "condemns", 3, rule_params["so_condemns_offset"], "SO Skazania")
    if "caa_relics_offset" in rule_params:
        _set_5p(vic.setdefault("cienie_al_andalus", {}), "relics", 2, rule_params["caa_relics_offset"], "CAA Relikwie")
    if "kb_decrees_offset" in rule_params:
        _set_5p(vic.setdefault("korona_borgiowie", {}), "decrees", 2, rule_params["kb_decrees_offset"], "KB Dekrety")
    if "kt_frags_offset" in rule_params:
        _set_5p(vic.setdefault("kabala_toledo", {}), "fragments", 3, rule_params["kt_frags_offset"], "KT Fragmenty")
    if "kt_era_offset" in rule_params:
        _set_5p(vic.setdefault("kabala_toledo", {}), "era", 6, rule_params["kt_era_offset"], "KT Era")
    if "gc_falls_default_offset" in rule_params or "gc_falls_offset" in rule_params:
        off = rule_params.get("gc_falls_offset", rule_params.get("gc_falls_default_offset", 0))
        _set_5p(vic.setdefault("gildia_cieni", {}), "falls", 9, off, "GC Upadki")

    desc = ", ".join(descs) if descs else "Modyfikacja parametrów 5P"
    return cfg, desc


def update_balance_notes_5p(
    old_version: str,
    new_version: str,
    change_desc: str,
    rule_id: str,
    base_res_5p: dict,
    best_res_5p: dict,
    diag_before: dict,
    diag_after: dict,
):
    """Automatically update data/playtesting/balance-notes.md with patch note entry."""
    if not BALANCE_NOTES_PATH.exists():
        return

    content = BALANCE_NOTES_PATH.read_text(encoding="utf-8")
    today = datetime.now().strftime("%Y-%m-%d")
    d_5p = best_res_5p["score_4p_balance"] - base_res_5p["score_4p_balance"]
    delta_5p_str = f"+{d_5p:.1f}" if d_5p > 0 else f"{d_5p:.1f}"

    patch_note_block = (
        f"### 🟢 Patch {new_version} ({today}) — Format 5P Full: {change_desc} (Zysk 5P Δ {delta_5p_str} pkt)\n"
        f"- **Wynik 5P:** 5p **`{base_res_5p['score_4p_balance']:.1f}`** → **`{best_res_5p['score_4p_balance']:.1f} pkt`** | Kanon 4P **`{diag_after['cat_scores'].get('4p',0.0):.1f}`** | 3p **`{diag_after['cat_scores'].get('3p',0.0):.1f}`** | Global **`{diag_after['global_score']:.1f}`**\n"
        f"- **Modyfikacja (`{rule_id}`):** {change_desc}.\n"
        f"- **Efekt:** Optymalizacja Formatu 5P Full (wyjątki `5p:`). Telemetria: Średnia Er {best_res_5p['eras_avg']:.2f}, Deadlocks {best_res_5p['deadlock_pct']:.1f}%, Pas Biedy {best_res_5p['poverty_pct']:.1f}%.\n\n"
    )

    history_heading = "## 📜 Chronologiczna Historia Zmian Balansu (Faza Prototypowa — Patch Notes)\n\n"
    if history_heading in content:
        content = content.replace(history_heading, history_heading + patch_note_block, 1)

    BALANCE_NOTES_PATH.write_text(content, encoding="utf-8")


def log_5p_iteration(
    log_path: Path,
    iteration: int,
    phase: int,
    old_version: str,
    new_version: str,
    desc: str,
    rule_id: str,
    base_res_5p: dict,
    best_res_5p: dict,
    diag_before: dict,
    diag_after: dict,
    elapsed_iter: float,
):
    """Appends an iteration entry to audytor_5p_log.md."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    if not log_path.exists():
        headers = [
            "# Dziennik Optymalizacji Formatu 5P Full (Audytor 5P)",
            "",
            "Rejestr wdrożonych patchów wyjątków formatu 5-osobowego.",
            "",
            "| Iteracja | Faza | Data i Czas | Wersja | Modyfikacja 5P | 5P Score | Wpływ na 4p | Wpływ na 3p | Global Score | Deadlocks % | Pas Biedy % | Czas |",
            "| :---: | :---: | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
        ]
        log_path.write_text("\n".join(headers) + "\n", encoding="utf-8")

    d_5p = best_res_5p["score_4p_balance"] - base_res_5p["score_4p_balance"]
    d5_str = f"+{d_5p:.1f}" if d_5p > 0 else f"{d_5p:.1f}"

    d_4p = diag_after["cat_scores"].get("4p", 0) - diag_before["cat_scores"].get("4p", 0)
    d4_str = f"+{d_4p:.1f}" if d_4p > 0 else f"{d_4p:.1f}"

    d_3p = diag_after["cat_scores"].get("3p", 0) - diag_before["cat_scores"].get("3p", 0)
    d3_str = f"+{d_3p:.1f}" if d_3p > 0 else f"{d_3p:.1f}"

    d_glob = diag_after["global_score"] - diag_before["global_score"]
    dg_str = f"+{d_glob:.1f}" if d_glob > 0 else f"{d_glob:.1f}"

    score_5p_col = f"{base_res_5p['score_4p_balance']:.1f} → **{best_res_5p['score_4p_balance']:.1f}** (`{d5_str}`)"
    p4_col = f"{diag_before['cat_scores'].get('4p',0):.1f} → {diag_after['cat_scores'].get('4p',0):.1f} (`{d4_str}`)"
    p3_col = f"{diag_before['cat_scores'].get('3p',0):.1f} → {diag_after['cat_scores'].get('3p',0):.1f} (`{d3_str}`)"
    glob_col = f"{diag_before['global_score']:.1f} → **{diag_after['global_score']:.1f}** (`{dg_str}`)"

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    row = (
        f"| #{iteration} | {phase}D | {now_str} | `{new_version}` | {desc} | "
        f"{score_5p_col} | {p4_col} | {p3_col} | {glob_col} | "
        f"{best_res_5p['deadlock_pct']:.1f}% | {best_res_5p['poverty_pct']:.1f}% | {elapsed_iter:.1f}s |"
    )
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(row + "\n")


def generate_all_macro_pairwise_candidates(atomic_pool: list[tuple[str, str, dict]]) -> list[tuple[str, str, dict]]:
    """Generates 100% full unconstrained pairwise combinations of macro rules (N*(N-1)/2)."""
    seen_ids = set()
    pairs = []
    n = len(atomic_pool)
    for i in range(n):
        for j in range(i + 1, n):
            merged = merge_mutations(atomic_pool[i], atomic_pool[j])
            if merged and merged[0] not in seen_ids:
                seen_ids.add(merged[0])
                pairs.append(merged)
    return pairs


def generate_all_macro_3d_candidates(atomic_pool: list[tuple[str, str, dict]]) -> list[tuple[str, str, dict]]:
    """Generates 100% full unconstrained 3-way combinations of macro rules (N*(N-1)*(N-2)/6)."""
    seen_ids = set()
    trios = []
    n = len(atomic_pool)
    for i in range(n):
        for j in range(i + 1, n):
            pair = merge_mutations(atomic_pool[i], atomic_pool[j])
            if not pair:
                continue
            for k in range(j + 1, n):
                trio = merge_mutations(pair, atomic_pool[k])
                if trio and trio[0] not in seen_ids:
                    seen_ids.add(trio[0])
                    trios.append(trio)
    return trios


def generate_all_macro_4d_candidates(atomic_pool: list[tuple[str, str, dict]]) -> list[tuple[str, str, dict]]:
    """Generates 100% full unconstrained 4-way combinations of macro rules."""
    seen_ids = set()
    quads = []
    n = len(atomic_pool)
    for i in range(n):
        for j in range(i + 1, n):
            pair = merge_mutations(atomic_pool[i], atomic_pool[j])
            if not pair:
                continue
            for k in range(j + 1, n):
                trio = merge_mutations(pair, atomic_pool[k])
                if not trio:
                    continue
                for l in range(k + 1, n):
                    quad = merge_mutations(trio, atomic_pool[l])
                    if quad and quad[0] not in seen_ids:
                        seen_ids.add(quad[0])
                        quads.append(quad)
    return quads


class AutoBalancer5P:
    """Autonomous continuous balancer for 5-player format exceptions."""

    def __init__(self, args: argparse.Namespace):
        self.args = args
        self.stop_requested = False
        self.total_iterations = 0
        self.start_time = time.time()

        signal.signal(signal.SIGINT, self._handle_signal)
        signal.signal(signal.SIGTERM, self._handle_signal)

    def _handle_signal(self, signum, frame):
        print("\n\n🛑 Otrzymano sygnał przerwania (Ctrl+C). Bezpiecznie kończę po bieżącym kroku...")
        self.stop_requested = True

    def run(self):
        setups = SETUPS_5P
        racer = AdaptiveSequentialRacer(
            setups=setups,
            batch_step=self.args.batch_step,
            min_games=self.args.min_games,
            max_games=self.args.max_games,
            epsilon_indiff=self.args.epsilon_indiff,
            workers=self.args.workers,
            min_delta=self.args.min_delta,
        )

        time_limit_sec = (self.args.hours * 3600) if self.args.hours else None
        current_phase = 1
        beam_seeds = []
        consecutive_stalls = 0
        cached_base_stats = None

        print("═══════════════════════════════════════════════════════════════════════")
        print("   INQUISITIO-1492 — AUDYTOR 5P (Adaptive Monte Carlo Racer)          ")
        print("  Doprowadzanie Formatu 5P do 100% z zachowaniem nienaruszonego Kanonu 4P")
        print("═══════════════════════════════════════════════════════════════════════")

        while not self.stop_requested:
            if time_limit_sec and (time.time() - self.start_time) >= time_limit_sec:
                print(f"\n⏱️ Osiągnięto limit czasu sesji ({self.args.hours}h). Kończę pracę.")
                break

            if self.args.max_iters and self.total_iterations >= self.args.max_iters:
                print(f"\n🔢 Osiągnięto maksymalną liczbę udanych patchów ({self.args.max_iters}). Kończę pracę.")
                break

            iter_start = time.time()
            iter_seed = self.args.seed + self.total_iterations * 10007 + current_phase * 997

            with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
                current_raw_cfg = yaml.safe_load(f)

            curr_ver = current_raw_cfg.get("system", {}).get("version", current_raw_cfg.get("version", "v1.0-alpha.90"))
            curr_base_overrides = extract_config_overrides(current_raw_cfg)

            atomic_pool = drop_dead_path_crutches({}, generate_all_atomic_candidates_5p())

            if current_phase == 1:
                print(f"\n🌐 [FAZA 1D — MAKRO 5P] 100% Pełna uniwersalna pula atomowa ({len(atomic_pool)} modyfikacji)...")
                candidate_pool = atomic_pool
            elif current_phase == 2:
                print(f"\n🌐 [FAZA 2D — MAKRO 5P] 100% PEŁNE PRZESZUKANIE WSZYSTKICH PAR (bez nasion)...")
                candidate_pool = generate_all_macro_pairwise_candidates(atomic_pool)
            elif current_phase == 3:
                print(f"\n🌐 [FAZA 3D — MAKRO 5P] 100% PEŁNE PRZESZUKANIE WSZYSTKICH TRÓJEK...")
                candidate_pool = generate_all_macro_3d_candidates(atomic_pool)
            else:
                print(f"\n🌐 [FAZA 4D — MAKRO 5P] 100% PEŁNE PRZESZUKANIE WSZYSTKICH CZWÓREK...")
                candidate_pool = generate_all_macro_4d_candidates(atomic_pool)
            delta_pool = list(candidate_pool)

            # Apply candidate mutations ON TOP OF base overrides
            effective_candidates = []
            for c in candidate_pool:
                eff_p = merge_override_dicts(curr_base_overrides, c[2])
                effective_candidates.append((c[0], c[1], eff_p))

            base_cand = ("BASE", f"Baza {curr_ver}", curr_base_overrides)
            base_stats, ranked_stats = racer.run_race(
                base_cand=base_cand,
                candidate_pool=effective_candidates,
                seed=iter_seed,
                delta_pool=delta_pool,
                label_prefix=f"WYŚCIG 5P — FAZA {current_phase}D",
                base_stats_cache=cached_base_stats,
            )
            cached_base_stats = base_stats

            surviving_stats = [c for c in ranked_stats if not c.is_pruned]
            surviving_stats.sort(key=lambda x: rank_key(x.to_result_dict()))

            base_res = base_stats.to_result_dict()
            accepted_candidate = None
            effective_rule_params = None
            best_ver_res = None
            acceptance_reason = ""

            for cand_stat in surviving_stats:
                cand_res = cand_stat.to_result_dict()
                decision = accept_candidate(
                    base_res,
                    cand_res,
                    min_delta=self.args.min_delta,
                )
                if decision.accepted:
                    accepted_candidate = cand_stat.delta_tuple if cand_stat.delta_tuple else cand_stat.cand_tuple
                    effective_rule_params = cand_stat.cand_tuple[2]
                    best_ver_res = cand_res
                    acceptance_reason = decision.reason
                    break

            # Validation Gate with 4P Canon Collateral Guard
            if accepted_candidate and best_ver_res is not None and effective_rule_params is not None:
                rule_id, rule_name, delta_params = accepted_candidate

                print(f"\n🔍 [RYGORYSTYCZNA BRAMKA WALIDACJI 10 000 GIER/SETUP — FORMAT 5P FULL]")
                val_base = _run_full_diagnostic(curr_base_overrides, games_per_setup=self.args.confirm_games, seed=42)
                val_cand = _run_full_diagnostic(effective_rule_params, games_per_setup=self.args.confirm_games, seed=42)

                val_base_5p = val_base["cat_scores"].get("5p", 0.0)
                val_cand_5p = val_cand["cat_scores"].get("5p", 0.0)
                val_delta_5p = val_cand_5p - val_base_5p

                val_base_4p = val_base["cat_scores"].get("4p", 0.0)
                val_cand_4p = val_cand["cat_scores"].get("4p", 0.0)
                val_delta_4p = val_cand_4p - val_base_4p

                min_allowed_delta = max(0.05, getattr(self.args, "min_delta", 0.05))

                if val_delta_5p < min_allowed_delta:
                    print(f"   ⛔ ODRZUCONO: Zysk 5P ({val_delta_5p:+.2f} pkt) < wymaganego +{min_allowed_delta:.2f} pkt.")
                    accepted_candidate = None
                    best_ver_res = None
                elif val_delta_4p < -0.30:
                    print(f"   ⛔ COLLATERAL VETO: Zmiana narusza Kanon 4P (Δ4P = {val_delta_4p:+.2f} pkt < -0.30 pkt)!")
                    accepted_candidate = None
                    best_ver_res = None

            if accepted_candidate and best_ver_res is not None and effective_rule_params is not None:
                self.total_iterations += 1

                with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
                    raw_cfg = yaml.safe_load(f)

                old_version = raw_cfg.get("version", "v1.0-alpha.90")
                mod_cfg, change_desc = apply_mutation_to_5p_config(raw_cfg, delta_params)

                if self.args.dry_run:
                    print(f"\n[DRY RUN] Zaakceptowano by modyfikację 5P: {change_desc}")
                    current_phase += 1
                else:
                    new_version, saved_path = save_config_and_bump_version(mod_cfg, _CONFIG_PATH, bump_version=True)
                    CONFIG.reload()
                    iter_elapsed = round(time.time() - iter_start, 2)

                    print(f"\n🎉 [ZAAKCEPTOWANO PATCH 5P #{self.total_iterations} — FAZA {current_phase}D]")
                    print(f"   Wersja:        `{old_version}` → **`{new_version}`**")
                    print(f"   Modyfikacja:   {change_desc}")

                    version_archive_dir = REPORTS_DIR / "archive" / new_version
                    version_archive_dir.mkdir(parents=True, exist_ok=True)
                    log_path = version_archive_dir / "audytor_5p_log.md"

                    log_5p_iteration(
                        log_path,
                        self.total_iterations,
                        current_phase,
                        old_version,
                        new_version,
                        change_desc,
                        rule_id,
                        base_res,
                        best_ver_res,
                        val_base,
                        val_cand,
                        iter_elapsed,
                    )

                    shutil.copy2(_CONFIG_PATH, version_archive_dir / "game_config.yaml")

                    print("   📑 Aktualizuję data/playtesting/balance-notes.md...")
                    update_balance_notes_5p(
                        old_version,
                        new_version,
                        change_desc,
                        rule_id,
                        base_res,
                        best_ver_res,
                        val_base,
                        val_cand,
                    )

                    print("   🔄 Synchronizuję dokumentację kart i reguł...")
                    subprocess.run([sys.executable, str(TOOLS_SRC_DIR.parent / "sync_config.py")])
                    print("   ✔ Zaktualizowano konfigurację.")

                    current_phase = 1
                    cached_base_stats = None
                    consecutive_stalls = 0
            else:
                if current_phase >= self.args.max_depth:
                    consecutive_stalls += 1
                    print(f"\n🛑 Zbadano pełną głębokość do Fazy {current_phase}D bez znalezienia patcha.")
                    print(f"   🔄 Resetuję do Fazy 1D z nowym ziarnem rozdań (cykl {consecutive_stalls})...")
                    current_phase = 1
                    self.args.seed += 137
                else:
                    current_phase += 1
                    print(f"🔄 [ŚLEPY ZAUŁEK {current_phase-1}D] Brak zysku w {current_phase-1}D. Przechodzę do 100% wyczerpującej FAZY {current_phase}D...\n")


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 — Audytor 5P (Adaptive Monte Carlo Racer)")
    parser.add_argument("--hours", type=float, default=None, help="Maksymalny czas sesji w godzinach")
    parser.add_argument("--max-iters", type=int, default=None, help="Maksymalna liczba udanych patchów")
    
    # Adaptive Monte Carlo Racing parameters
    parser.add_argument("--batch-step", type=int, default=400, help="Rozmiar mikro-kroku partii na setup (domyślnie: 400)")
    parser.add_argument("--min-games", type=int, default=400, help="Minimalna liczba gier/setup przed sprawdzeniem kryterium stopu (domyślnie: 400)")
    parser.add_argument("--max-games", type=int, default=6400, help="Maksymalna liczba gier/setup w wyścigu (domyślnie: 6400)")
    parser.add_argument("--epsilon-indiff", type=float, default=0.15, help="Próg strefy nierozróżnialności / szumu balansu w pkt (domyślnie: 0.15)")
    parser.add_argument("--confirm-games", type=int, default=10000, help="Liczba gier weryfikujących SSOT (domyślnie: 10000)")
    
    parser.add_argument("--min-delta", type=float, default=0.05, help="Minimalny zysk punktowy dla 5P (domyślnie: 0.05)")
    parser.add_argument("--beam-width", type=int, default=20, help="Szerokość wiązki synergii (domyślnie: 20)")
    parser.add_argument("--max-depth", type=int, default=4, help="Maksymalna głębokość wiązek kombinacji (domyślnie: 4)")
    parser.add_argument("--workers", type=int, default=min(os.cpu_count() or 4, 10), help="Liczba procesów równoległych")
    parser.add_argument("--seed", type=int, default=42, help="Ziarno generatora liczb losowych")
    parser.add_argument("--dry-run", action="store_true", help="Tryb symulacji bez zapisu do game_config.yaml")

    args = parser.parse_args()
    auditor = AutoBalancer5P(args)
    auditor.run()


if __name__ == "__main__":
    main()
