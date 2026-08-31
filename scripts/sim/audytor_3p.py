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


def _run_full_diagnostic(raw_cfg: dict, delta_params: dict | None = None, games_per_setup: int = 1000, seed: int = 42) -> dict:
    """Runs a complete 16-setup diagnostic to measure 3p, 4p, 5p and global score."""
    from inquisitio.runner.adaptive_racer import extract_config_overrides, merge_override_dicts
    all_setups = sorted(SETUP_PRESETS.keys())
    summaries = []
    setup_scores = {}
    for sname in all_setups:
        pc = len(SETUP_PRESETS[sname])
        stype = "5p" if pc == 5 else ("3p" if pc == 3 else "4p")
        base_params = extract_config_overrides(raw_cfg, setup_type=stype)

        if pc == 3 and delta_params:
            eff_params = merge_override_dicts(base_params, delta_params)
        else:
            eff_params = base_params

        s = run_batch(games=games_per_setup, setup=sname, seed=seed, layer="C", win_overrides=eff_params)
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
    """L1/L2/L4 for 3P exceptions + Contextual L2 rules per missing faction."""
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

    # Contextual L2 rules per missing faction AND per present faction (all except missing) in 3P
    CONTEXTUAL_MODES = [
        ("no_so", "Brak Świętego Oficjum (setupy bez SO)"),
        ("no_kb", "Brak Korony Borgiów (setupy bez KB)"),
        ("no_gc", "Brak Gildii Cieni (setupy bez GC)"),
        ("no_caa", "Brak Cieni Al-Andalus (setupy bez CAA)"),
        ("no_kt", "Brak Kabały Toledo (setupy bez KT)"),
        ("with_so", "Obecność Świętego Oficjum (wszystkie oprócz braku SO)"),
        ("with_kb", "Obecność Korony Borgiów (wszystkie oprócz braku KB)"),
        ("with_gc", "Obecność Gildii Cieni (wszystkie oprócz braku GC)"),
        ("with_caa", "Obecność Cieni Al-Andalus (wszystkie oprócz braku CAA)"),
        ("with_kt", "Obecność Kabały Toledo (wszystkie oprócz braku KT)"),
    ]

    L2_KNOBS = [
        ("threshold_offset", "Próg oskarżenia", [-1, 1]),
        ("start_gold_offset", "Złoto startowe", [-1, 1]),
        ("so_stacks_offset", "SO Stosy", [-1, 1, 2]),
        ("so_condemns_offset", "SO Skazania", [-1]),
        ("gc_falls_offset", "GC Upadki", [-2, -1, 1, 2]),
        ("kb_decrees_offset", "KB Dekrety", [-1, 1]),
        ("kt_frags_offset", "KT Fragmenty", [-1, 1]),
        ("caa_relics_offset", "CAA Relikwie", [-1, 1]),
        ("cooldown_offset", "Autodafe Cooldown", [-1, 1]),
    ]

    for tag, tag_name in CONTEXTUAL_MODES:
        for knob_key, knob_name, deltas in L2_KNOBS:
            for d in deltas:
                c_key = f"{tag}_{knob_key}"
                sign = f"+{d}" if d > 0 else f"{d}"
                tid = f"3P_CTX_{tag.upper()}_{knob_key.upper()}_{sign}"
                tname = f"[3P Reguła 1D: {tag_name}] {knob_name} {sign}"
                tests.append((tid, tname, {c_key: d}))

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

    def _set_3p(section_dict: dict, key: str, default_val: Any, offset: Any, desc_name: str, ctx_tag: str | None = None):
        if offset is None:
            return
        off = int(offset)
        cur = section_dict.get(key, default_val)
        
        # Mapping from with_ tag to canonical no_ tag
        WITH_TO_NO = {
            "with_so": "no_so", "has_so": "no_so",
            "with_caa": "no_caa", "has_caa": "no_caa",
            "with_kb": "no_kb", "has_kb": "no_kb",
            "with_kt": "no_kt", "has_kt": "no_kt",
            "with_gc": "no_gc", "has_gc": "no_gc",
        }
        
        is_with = ctx_tag in WITH_TO_NO if ctx_tag else False
        canonical_no_tag = WITH_TO_NO.get(ctx_tag) if is_with else ctx_tag

        if isinstance(cur, dict):
            val_cand = cur.get("3p", cur.get("4p", default_val))
            if isinstance(val_cand, dict):
                base_v = int(val_cand.get("default", default_val))
                if is_with:
                    # with_X: new default is base_v + off, and no_X retains base_v
                    val_cand["default"] = max(1, base_v + off)
                    val_cand[canonical_no_tag] = base_v
                elif ctx_tag:
                    val_cand[ctx_tag] = max(1, base_v + off)
                else:
                    val_cand["default"] = max(1, base_v + off)
            else:
                base_v = int(val_cand) if val_cand is not None else int(default_val)
                new_v = max(1, base_v + off)
                if is_with:
                    cur["3p"] = {"default": new_v, canonical_no_tag: base_v}
                elif ctx_tag:
                    cur["3p"] = {"default": base_v, ctx_tag: new_v}
                else:
                    cur["3p"] = new_v
        else:
            base_v = int(cur) if cur is not None else int(default_val)
            new_v = max(1, base_v + off)
            if is_with:
                section_dict[key] = {"3p": {"default": new_v, canonical_no_tag: base_v}, "4p": cur, "5p": cur}
            elif ctx_tag:
                section_dict[key] = {"3p": {"default": base_v, ctx_tag: new_v}, "4p": cur, "5p": cur}
            else:
                section_dict[key] = {"3p": new_v, "4p": cur, "5p": cur}
        ctx_info = f" ({canonical_no_tag})" if canonical_no_tag else ""
        descs.append(f"{desc_name} (3p{ctx_info}): {new_v}")

    for k, v in rule_params.items():
        ctx_tag = None
        for tag in [
            "no_so", "no_oficjum", "no_caa", "no_cienie", "no_kb", "no_korona", "no_kt", "no_kabala", "no_gc", "no_gildia",
            "with_so", "has_so", "with_caa", "has_caa", "with_kb", "has_kb", "with_kt", "has_kt", "with_gc", "has_gc"
        ]:
            if tag in k:
                ctx_tag = tag
                break
        
        base_k = k.replace(f"{ctx_tag}_", "") if ctx_tag else k

        if base_k == "start_gold_offset":
            _set_3p(cfg.setdefault("system", {}), "start_gold", 4, v, "Złoto startowe", ctx_tag)
        elif base_k == "threshold_offset":
            _set_3p(cfg.setdefault("system", {}), "accusation_threshold", 6, v, "Próg oskarżenia", ctx_tag)
        elif base_k == "so_stacks_offset":
            _set_3p(cfg.setdefault("victory", {}).setdefault("swiete_oficjum", {}), "stacks", 6, v, "SO Stosy", ctx_tag)
        elif base_k == "so_condemns_offset":
            _set_3p(cfg.setdefault("victory", {}).setdefault("swiete_oficjum", {}), "condemns", 2, v, "SO Skazania", ctx_tag)
        elif base_k == "caa_relics_offset":
            _set_3p(cfg.setdefault("victory", {}).setdefault("cienie_al_andalus", {}), "relics", 2, v, "CAA Relikwie", ctx_tag)
        elif base_k == "kb_decrees_offset":
            _set_3p(cfg.setdefault("victory", {}).setdefault("korona_borgiowie", {}), "decrees", 2, v, "KB Dekrety", ctx_tag)
        elif base_k == "kb_hooks_offset":
            _set_3p(cfg.setdefault("victory", {}).setdefault("korona_borgiowie", {}), "hooks", 2, v, "KB Haki", ctx_tag)
        elif base_k == "kt_frags_offset":
            _set_3p(cfg.setdefault("victory", {}).setdefault("kabala_toledo", {}), "fragments", 3, v, "KT Fragmenty", ctx_tag)
        elif base_k in ("gc_falls_offset", "gc_falls_default_offset"):
            _set_3p(cfg.setdefault("victory", {}).setdefault("gildia_cieni", {}), "falls", 8, v, "GC Upadki", ctx_tag)

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
            curr_base_overrides = extract_config_overrides(current_raw_cfg, setup_type="3p")

            atomic_pool = drop_dead_path_crutches({}, generate_all_atomic_candidates_3p())

            if current_phase == 1:
                print(f"\n🌐 [FAZA 1D — MAKRO 3P] 100% Pełna uniwersalna pula atomowa ({len(atomic_pool)} modyfikacji)...")
                candidate_pool = atomic_pool
            elif current_phase == 2:
                print(f"\n🌐 [FAZA 2D — MAKRO 3P] 100% PEŁNE PRZESZUKANIE WSZYSTKICH PAR (bez nasion)...")
                candidate_pool = generate_all_macro_pairwise_candidates(atomic_pool)
            elif current_phase == 3:
                print(f"\n🌐 [FAZA 3D — MAKRO 3P] 100% PEŁNE PRZESZUKANIE WSZYSTKICH TRÓJEK...")
                candidate_pool = generate_all_macro_3d_candidates(atomic_pool)
            else:
                print(f"\n🌐 [FAZA 4D — MAKRO 3P] 100% PEŁNE PRZESZUKANIE WSZYSTKICH CZWÓREK...")
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
                label_prefix=f"WYŚCIG 3P — FAZA {current_phase}D",
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

            best_rejection = ""
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
                else:
                    if not best_rejection:
                        best_rejection = f"Odpadł najlepszy kandydat: {decision.reason}"

            # Validation Gate with 4P Canon Collateral Guard
            if accepted_candidate and best_ver_res is not None and effective_rule_params is not None:
                rule_id, rule_name, delta_params = accepted_candidate

                print(f"\n🔍 [RYGORYSTYCZNA BRAMKA WALIDACJI 10 000 GIER/SETUP — FORMAT 3P (ALL)]")
                val_base = _run_full_diagnostic(current_raw_cfg, delta_params=None, games_per_setup=self.args.confirm_games, seed=42)
                val_cand = _run_full_diagnostic(current_raw_cfg, delta_params=delta_params, games_per_setup=self.args.confirm_games, seed=42)

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
                    CONFIG.reload()
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
                    cached_base_stats = None
                    consecutive_stalls = 0
            else:
                if current_phase >= self.args.max_depth:
                    print(
                        f"\n🏁 Brak zmian makro przynoszących zysk w 3P na {current_phase}D "
                        f"(lookahead wyczerpany). Bieżący stan jest lokalnym optimum puli."
                    )
                    break
                else:
                    if best_rejection:
                        print(f"   ⛔ {best_rejection}")
                    print(f"🔄 [ŚLEPY ZAUŁEK {current_phase}D] Brak zysku w {current_phase}D. Przechodzę do 100% wyczerpującej FAZY {current_phase + 1}D...\n\n")
                    current_phase += 1


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 — Audytor 3P (Adaptive Monte Carlo Racer)")
    parser.add_argument("--hours", type=float, default=None, help="Maksymalny czas sesji w godzinach")
    parser.add_argument("--max-iters", type=int, default=None, help="Maksymalna liczba udanych patchów")
    
    # Adaptive Monte Carlo Racing parameters
    parser.add_argument("--batch-step", type=int, default=400, help="Rozmiar mikro-kroku partii na setup (domyślnie: 400)")
    parser.add_argument("--min-games", type=int, default=400, help="Minimalna liczba gier/setup przed sprawdzeniem kryterium stopu (domyślnie: 400)")
    parser.add_argument("--max-games", type=int, default=6400, help="Maksymalna liczba gier/setup w wyścigu (domyślnie: 6400)")
    parser.add_argument("--epsilon-indiff", type=float, default=0.15, help="Próg strefy nierozróżnialności / szumu balansu w pkt (domyślnie: 0.15)")
    parser.add_argument("--confirm-games", type=int, default=10000, help="Liczba gier weryfikujących SSOT (domyślnie: 10000)")
    
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
