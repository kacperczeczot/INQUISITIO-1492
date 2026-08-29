#!/usr/bin/env python3
"""INQUISITIO-1492 — AUDYTOR 3P (3-Player Autonomous Balance Optimizer).

Autonomous optimizer for 3-player format exceptions, powered by:
  1. Native C++20 simulation core.
  2. Multi-Fidelity Adaptive Sequential Racer (10 3P setups, 95% CI statistical pruning).
  3. Multi-dimensional Combinatorial Beam Search (1D -> 2D -> 3D -> 4D).
  4. Mandatory 10,000 games/setup validation gate with 4P Canon Collateral Guard.
  5. Strict SSOT automation (game_config.yaml '3p:' exceptions, sync_config, balance-notes.md).
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

SETUPS_3P = sorted([s for s, pl in SETUP_PRESETS.items() if len(pl) == 3])

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


def generate_all_atomic_candidates_3p() -> list[tuple[str, str, dict]]:
    """L1/L2/L4 for 3P exceptions (table-wide L3 cards are fixed by 4P canon)."""
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


def apply_mutation_to_3p_config(raw_cfg: dict[str, Any], rule_params: dict[str, Any]) -> tuple[dict[str, Any], str]:
    """Applies parameter overrides directly to 3p sections in config dict."""
    cfg = copy.deepcopy(raw_cfg)
    rule_params = strip_table_wide_canon_params(rule_params)
    descs = []

    def _set_3p(section_dict: dict, key: str, default_val: Any, offset: Any, desc_name: str):
        if offset is None:
            return
        off = int(offset)
        cur = section_dict.get(key, default_val)
        if isinstance(cur, dict):
            val_cand = cur.get("3p", cur.get("4p", default_val))
            base_v = int(val_cand) if val_cand is not None else int(default_val)
            new_v = max(1, base_v + off)
            cur["3p"] = new_v
        else:
            base_v = int(cur) if cur is not None else int(default_val)
            new_v = max(1, base_v + off)
            section_dict[key] = {"3p": new_v, "4p": cur, "5p": cur}
        descs.append(f"{desc_name} (3p): {new_v}")

    # L1
    if "start_gold_offset" in rule_params:
        _set_3p(cfg.setdefault("system", {}), "start_gold", 4, rule_params["start_gold_offset"], "Złoto startowe")
    if "threshold_offset" in rule_params:
        _set_3p(cfg.setdefault("system", {}), "accusation_threshold", 6, rule_params["threshold_offset"], "Próg oskarżenia")

    # L2
    vic = cfg.setdefault("victory", {})
    if "so_stacks_offset" in rule_params:
        _set_3p(vic.setdefault("swiete_oficjum", {}), "stacks", 5, rule_params["so_stacks_offset"], "SO Stosy")
    if "so_condemns_offset" in rule_params:
        _set_3p(vic.setdefault("swiete_oficjum", {}), "condemns", 2, rule_params["so_condemns_offset"], "SO Skazania")
    if "caa_relics_offset" in rule_params:
        _set_3p(vic.setdefault("cienie_al_andalus", {}), "relics", 2, rule_params["caa_relics_offset"], "CAA Relikwie")
    if "kb_decrees_offset" in rule_params:
        _set_3p(vic.setdefault("korona_borgiowie", {}), "decrees", 2, rule_params["kb_decrees_offset"], "KB Dekrety")
    if "kt_frags_offset" in rule_params:
        _set_3p(vic.setdefault("kabala_toledo", {}), "fragments", 3, rule_params["kt_frags_offset"], "KT Fragmenty")
    if "kt_era_offset" in rule_params:
        _set_3p(vic.setdefault("kabala_toledo", {}), "era", 6, rule_params["kt_era_offset"], "KT Era")
    if "gc_falls_default_offset" in rule_params or "gc_falls_offset" in rule_params:
        off = rule_params.get("gc_falls_offset", rule_params.get("gc_falls_default_offset", 0))
        _set_3p(vic.setdefault("gildia_cieni", {}), "falls", 4, off, "GC Upadki")

    desc = ", ".join(descs) if descs else "Modyfikacja parametrów 3P"
    return cfg, desc


def update_balance_notes_3p(
    old_version: str,
    new_version: str,
    change_desc: str,
    rule_id: str,
    base_res_3p: dict,
    best_res_3p: dict,
    diag_before: dict,
    diag_after: dict,
):
    """Automatically update data/playtesting/balance-notes.md with patch note entry."""
    if not BALANCE_NOTES_PATH.exists():
        return

    content = BALANCE_NOTES_PATH.read_text(encoding="utf-8")
    today = datetime.now().strftime("%Y-%m-%d")
    d_3p = best_res_3p["score_4p_balance"] - base_res_3p["score_4p_balance"]
    delta_3p_str = f"+{d_3p:.1f}" if d_3p > 0 else f"{d_3p:.1f}"

    patch_note_block = (
        f"### 🟢 Patch {new_version} ({today}) — Format 3P: {change_desc} (Zysk 3P Δ {delta_3p_str} pkt)\n"
        f"- **Wynik 3P:** 3p **`{base_res_3p['score_4p_balance']:.1f}`** → **`{best_res_3p['score_4p_balance']:.1f} pkt`** | Kanon 4P **`{diag_after['cat_scores'].get('4p',0.0):.1f}`** | 5p **`{diag_after['cat_scores'].get('5p',0.0):.1f}`** | Global **`{diag_after['global_score']:.1f}`**\n"
        f"- **Modyfikacja (`{rule_id}`):** {change_desc}.\n"
        f"- **Efekt:** Optymalizacja Formatu 3P (wyjątki `3p:`). Telemetria: Średnia Er {best_res_3p['eras_avg']:.2f}, Deadlocks {best_res_3p['deadlock_pct']:.1f}%, Pas Biedy {best_res_3p['poverty_pct']:.1f}%.\n\n"
    )

    history_heading = "## 📜 Chronologiczna Historia Zmian Balansu (Faza Prototypowa — Patch Notes)\n\n"
    if history_heading in content:
        content = content.replace(history_heading, history_heading + patch_note_block, 1)

    BALANCE_NOTES_PATH.write_text(content, encoding="utf-8")


def log_3p_iteration(
    log_path: Path,
    iteration: int,
    phase: int,
    old_version: str,
    new_version: str,
    desc: str,
    rule_id: str,
    base_res_3p: dict,
    best_res_3p: dict,
    diag_before: dict,
    diag_after: dict,
    elapsed_iter: float,
):
    """Appends an iteration entry to audytor_3p_log.md."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    if not log_path.exists():
        headers = [
            "# Dziennik Optymalizacji Formatu 3P (Audytor 3P)",
            "",
            "Rejestr wdrożonych patchów wyjątków formatu 3-osobowego.",
            "",
            "| Iteracja | Faza | Data i Czas | Wersja | Modyfikacja 3P | 3P Score | Wpływ na 4p | Wpływ na 5p | Global Score | Deadlocks % | Pas Biedy % | Czas |",
            "| :---: | :---: | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
        ]
        log_path.write_text("\n".join(headers) + "\n", encoding="utf-8")

    d_3p = best_res_3p["score_4p_balance"] - base_res_3p["score_4p_balance"]
    d3_str = f"+{d_3p:.1f}" if d_3p > 0 else f"{d_3p:.1f}"

    d_4p = diag_after["cat_scores"].get("4p", 0) - diag_before["cat_scores"].get("4p", 0)
    d4_str = f"+{d_4p:.1f}" if d_4p > 0 else f"{d_4p:.1f}"

    d_5p = diag_after["cat_scores"].get("5p", 0) - diag_before["cat_scores"].get("5p", 0)
    d5_str = f"+{d_5p:.1f}" if d_5p > 0 else f"{d_5p:.1f}"

    d_glob = diag_after["global_score"] - diag_before["global_score"]
    dg_str = f"+{d_glob:.1f}" if d_glob > 0 else f"{d_glob:.1f}"

    score_3p_col = f"{base_res_3p['score_4p_balance']:.1f} → **{best_res_3p['score_4p_balance']:.1f}** (`{d3_str}`)"
    p4_col = f"{diag_before['cat_scores'].get('4p',0):.1f} → {diag_after['cat_scores'].get('4p',0):.1f} (`{d4_str}`)"
    p5_col = f"{diag_before['cat_scores'].get('5p',0):.1f} → {diag_after['cat_scores'].get('5p',0):.1f} (`{d5_str}`)"
    glob_col = f"{diag_before['global_score']:.1f} → **{diag_after['global_score']:.1f}** (`{dg_str}`)"

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    row = (
        f"| #{iteration} | {phase}D | {now_str} | `{new_version}` | {desc} | "
        f"{score_3p_col} | {p4_col} | {p5_col} | {glob_col} | "
        f"{best_res_3p['deadlock_pct']:.1f}% | {best_res_3p['poverty_pct']:.1f}% | {elapsed_iter:.1f}s |"
    )
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(row + "\n")


class AutoBalancer3P:
    """Autonomous continuous balancer for 3-player format exceptions."""

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
        setups = SETUPS_3P
        racer = AdaptiveSequentialRacer(
            setups=setups,
            batch_step=400,
            min_games=400,
            max_games=6400,
            epsilon_indiff=0.15,
            workers=self.args.workers,
            accept_mode="legacy",
            min_delta=self.args.min_delta,
        )

        time_limit_sec = (self.args.hours * 3600) if self.args.hours else None
        current_phase = 1
        beam_seeds = []
        consecutive_stalls = 0
        cached_base_stats = None

        print("═══════════════════════════════════════════════════════════════════════")
        print("   INQUISITIO-1492 — AUDYTOR 3P (Adaptive Monte Carlo Racer)          ")
        print("  Doprowadzanie Formatu 3P do 100% z zachowaniem nienaruszonego Kanonu 4P")
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

            atomic_pool = drop_dead_path_crutches({}, generate_all_atomic_candidates_3p())

            if current_phase == 1 or not beam_seeds:
                candidate_pool = atomic_pool
                delta_pool = list(atomic_pool)
            else:
                composite_pool = []
                for seed_mut in beam_seeds:
                    for atomic_mut in atomic_pool:
                        merged = merge_mutations(seed_mut, atomic_mut)
                        if merged:
                            composite_pool.append(merged)
                seen_ids = set()
                candidate_pool = []
                for c in composite_pool:
                    if c[0] not in seen_ids:
                        seen_ids.add(c[0])
                        candidate_pool.append(c)
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
                label_prefix=f"WYŚCIG 3P — FAZA {current_phase}D",
                base_stats_cache=cached_base_stats,
            )
            cached_base_stats = base_stats

            surviving_stats = [c for c in ranked_stats if not c.is_pruned]
            surviving_stats.sort(key=lambda x: rank_key(x.to_result_dict(), mode="legacy"))

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
                    mode="legacy",
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

                print(f"\n🔍 [RYGORYSTYCZNA BRAMKA WALIDACJI 10 000 GIER/SETUP — FORMAT 3P]")
                val_base = _run_full_diagnostic(curr_base_overrides, games_per_setup=10000, seed=42)
                val_cand = _run_full_diagnostic(effective_rule_params, games_per_setup=10000, seed=42)

                val_base_3p = val_base["cat_scores"].get("3p", 0.0)
                val_cand_3p = val_cand["cat_scores"].get("3p", 0.0)
                val_delta_3p = val_cand_3p - val_base_3p

                val_base_4p = val_base["cat_scores"].get("4p", 0.0)
                val_cand_4p = val_cand["cat_scores"].get("4p", 0.0)
                val_delta_4p = val_cand_4p - val_base_4p

                min_allowed_delta = max(0.05, getattr(self.args, "min_delta", 0.05))

                # Guard 1: 3P improvement
                # Guard 2: 4P Canon must NOT be broken (delta 4P >= -0.30 pkt)
                if val_delta_3p < min_allowed_delta:
                    print(f"   ⛔ ODRZUCONO: Zysk 3P ({val_delta_3p:+.2f} pkt) < wymaganego +{min_allowed_delta:.2f} pkt.")
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
                mod_cfg, change_desc = apply_mutation_to_3p_config(raw_cfg, delta_params)

                if self.args.dry_run:
                    print(f"\n[DRY RUN] Zaakceptowano by modyfikację 3P: {change_desc}")
                    current_phase += 1
                else:
                    new_version, saved_path = save_config_and_bump_version(mod_cfg, _CONFIG_PATH, bump_version=True)
                    iter_elapsed = round(time.time() - iter_start, 2)

                    print(f"\n🎉 [ZAAKCEPTOWANO PATCH 3P #{self.total_iterations} — FAZA {current_phase}D]")
                    print(f"   Wersja:        `{old_version}` → **`{new_version}`**")
                    print(f"   Modyfikacja:   {change_desc}")

                    version_archive_dir = REPORTS_DIR / "archive" / new_version
                    version_archive_dir.mkdir(parents=True, exist_ok=True)
                    log_path = version_archive_dir / "audytor_3p_log.md"

                    log_3p_iteration(
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
                    update_balance_notes_3p(
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
                    beam_seeds.clear()
                    cached_base_stats = None
                    consecutive_stalls = 0
            else:
                diverse_seeds = [r.cand_tuple for r in surviving_stats]
                if current_phase >= self.args.max_depth:
                    consecutive_stalls += 1
                    print(f"\n🛑 Osiągnięto maksymalną głębokość wiązek 3P ({self.args.max_depth}D).")
                    print(f"   🔄 Resetuję do Fazy 1D z przesunięciem ziarna (cykl {consecutive_stalls})...")
                    current_phase = 1
                    self.args.seed += 137
                    beam_seeds.clear()
                else:
                    beam_seeds = diverse_seeds[:self.args.beam_width]
                    current_phase += 1
                    print(f"🔄 Zakwalifikowano {len(beam_seeds)} nasion 3P i ESKALUJĘ DO FAZY {current_phase}D...\n")


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 — Audytor 3P (Adaptive Monte Carlo Racer)")
    parser.add_argument("--hours", type=float, default=None, help="Maksymalny czas sesji w godzinach")
    parser.add_argument("--max-iters", type=int, default=None, help="Maksymalna liczba udanych patchów")
    parser.add_argument("--min-delta", type=float, default=0.05, help="Minimalny zysk punktowy dla 3P (domyślnie: 0.05)")
    parser.add_argument("--beam-width", type=int, default=20, help="Szerokość wiązki synergii (domyślnie: 20)")
    parser.add_argument("--max-depth", type=int, default=4, help="Maksymalna głębokość wiązek kombinacji (domyślnie: 4)")
    parser.add_argument("--workers", type=int, default=min(os.cpu_count() or 4, 10), help="Liczba procesów równoległych")
    parser.add_argument("--seed", type=int, default=42, help="Ziarno generatora liczb losowych")
    parser.add_argument("--dry-run", action="store_true", help="Tryb symulacji bez zapisu do game_config.yaml")

    args = parser.parse_args()
    auditor = AutoBalancer3P(args)
    auditor.run()


if __name__ == "__main__":
    main()
