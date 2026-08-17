#!/usr/bin/env python3
"""INQUISITIO-1492 — AUDYTOR 4P MAKRO (4-Player Autonomous Macro-Balance Optimizer).

Bliźniaczy, autonomiczny optymalizator balansu dla Kanonu 4P oparty na architekturze
Audytora Kanonu, zoptymalizowany pod kątem parametrów makro (L1, L2, L4) bez kart (L3).

Główne założenia metodologiczne:
  1. Kanon 4P (5 setupów 4-osobowych) — ten sam lejek co Audytor Kanonu, **bez L3 / kart**.
  2. Pula: ±1 z audit_level1/2/4 **oraz** skraj/off z raportu użyteczności.
  3. **Lookahead +1D:** nie wdraża poprawy na głębokości, na której ją znalazł — zawsze
     zagląda jedną warstwę głębiej (1D→2D zawsze, dalej tylko gdy nowa głębokość bije held).
     Jeśli głębiej nic lepszego, wdraża wcześniejszy wektor. 1D bez zysku i tak idzie w 2D.
  4. HUD = win share (`calculate_balance_score`). Witalność / martwe dual-win są **veto i ranking**,
     nie składnikiem 4P Score. Obniżenie progu uśpionej ścieżki to proteza — odrzucane.
  5. Przyjęcie patcha: `canon_accept` tryb `band` (jak kanon).
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
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from pathlib import Path

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
from inquisitio.runner.batch import run_batch
from inquisitio.runner.balance import faction_shares as win_shares
from inquisitio.runner.canon_accept import (
    TARGET_BAND_PCT,
    AcceptDecision,
    accept_candidate,
    canon_should_stop,
    rank_key,
    setup_shares_in_range,
)
from inquisitio.runner.scoring import (
    calculate_balance_score,
    calculate_category_scores,
    calculate_global_score,
    calculate_setup_score,
    color_score,
    evaluate_vitality,
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


def _run_single_test_task_4p(args_tuple: tuple) -> dict:
    """Worker: 5 canonical 4P setups. Win-share HUD + vitality (użyteczność), no cards."""
    (cand_id, cand_name, rule_params), games_per_setup, seed, setups = args_tuple

    summaries = []
    setup_scores = {}
    setup_scores_balance = {}
    setup_shares: dict[str, dict[str, float]] = {}
    vitality_penalties = []
    vitality_warnings: list[str] = []
    fshares = {fid: [] for fid in FACTION_NAMES.keys()}

    for sname in setups:
        s = run_batch(games=games_per_setup, setup=sname, seed=seed, layer="C", win_overrides=rule_params)
        summaries.append(s)
        setup_scores[sname] = calculate_setup_score(s)
        setup_scores_balance[sname] = calculate_balance_score(s)
        setup_shares[sname] = {
            fid: round(pct * 100.0, 1) for fid, pct in win_shares(s).items()
        }
        vit = evaluate_vitality(s)
        vitality_penalties.append(vit.vitality_penalty)
        for msg in vit.warnings:
            vitality_warnings.append(f"{sname}: {msg}")
        for fid, wins in s.wins.items():
            if s.games > 0:
                fid_enum = FactionId(fid) if not isinstance(fid, FactionId) else fid
                if fid_enum in fshares:
                    fshares[fid_enum].append(wins / s.games)

    score_4p = round(sum(setup_scores.values()) / len(setup_scores), 1) if setup_scores else 0.0
    score_4p_balance = (
        round(sum(setup_scores_balance.values()) / len(setup_scores_balance), 1)
        if setup_scores_balance
        else 0.0
    )
    n_sum = len(summaries) if summaries else 1
    min_balance_name = min(setup_scores_balance, key=lambda k: setup_scores_balance[k]) if setup_scores_balance else ""
    min_balance = setup_scores_balance[min_balance_name] if min_balance_name else 0.0

    return {
        "id": cand_id,
        "name": cand_name,
        "params": rule_params,
        "score_4p": score_4p,
        "score_4p_balance": score_4p_balance,
        "setup_scores": setup_scores,
        "setup_scores_balance": setup_scores_balance,
        "setup_shares": setup_shares,
        "min_balance": min_balance,
        "min_balance_setup": min_balance_name,
        "vitality_penalty": max(vitality_penalties) if vitality_penalties else 0.0,
        "vitality_warnings": vitality_warnings,
        "fshares": {FACTION_NAMES[k]: round(sum(v) / len(v) * 100, 1) for k, v in fshares.items() if v},
        "eras_avg": sum(s.eras_avg for s in summaries) / n_sum,
        "eras_min": min(s.eras_min for s in summaries) if summaries else 0,
        "eras_max": max(s.eras_max for s in summaries) if summaries else 0,
        "deadlock_pct": (sum(s.eras_limit_pct for s in summaries) / n_sum) * 100.0,
        "poverty_pct": (sum(s.passes_forced_pct for s in summaries) / n_sum) * 100.0,
        "autodafe_avg": sum(s.autodafe_avg for s in summaries) / n_sum,
        "acc_avg": sum(s.accusations_avg for s in summaries) / n_sum,
        "gold_avg": sum(s.avg_gold_end for s in summaries) / n_sum,
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
    """L1/L2/L4 ±1 plus extreme/off from feature_impact. No L3 / no card_overrides."""
    tests: list[tuple[str, str, dict]] = []
    tests.extend(
        [
            t
            for t in audit_level1.build_level1_tests()
            if t[0] != "L1_BAZA"
            and "HAND_LIMIT" not in t[0]
            and "AUTODAFE" not in t[0]
        ]
    )
    tests.extend([t for t in audit_level2.build_level2_tests() if t[0] != "L2_BAZA"])
    tests.extend([t for t in audit_level4.build_level4_tests() if t[0] != "L4_BAZA"])

    from feature_impact_4p import CANONICAL_4P_SETUPS as IMPACT_SETUPS
    from feature_impact_4p import build_all_mechanic_tasks

    for t in build_all_mechanic_tasks(1, 1, IMPACT_SETUPS):
        tests.append((t[0], t[1], t[3]))

    seen: set[str] = set()
    out: list[tuple[str, str, dict]] = []
    for tid, name, params in tests:
        if tid.startswith("L3_") or "card_overrides" in params or "disabled_cards" in params:
            continue
        if "AUTODAFE" in tid or "cooldown_offset" in params or "autodafe_cooldown" in params:
            continue
        if "GC_FALLS_DEFAULT" in tid or "GC_FALLS_NO_SO" in tid:
            continue
        if "gc_falls_default_offset" in params or "gc_falls_no_oficjum_offset" in params:
            continue
        if tid in seen:
            continue
        seen.add(tid)
        out.append((tid, name, params))
    return out


_DEAD_PATH_CRUTCH = (
    ("skazania", "so_condemns_offset"),
    ("stosy", "so_stacks_offset"),
)


def is_dead_path_crutch(base: dict, params: dict) -> bool:
    """True if params lower a dual-win threshold that vitality already flags as dead."""
    warns = " ".join(base.get("vitality_warnings") or [])
    for label, key in _DEAD_PATH_CRUTCH:
        if f"Martwa ścieżka {label}" in warns and int(params.get(key, 0) or 0) < 0:
            return True
    return False


def drop_dead_path_crutches(
    base: dict, candidates: list[tuple[str, str, dict]]
) -> list[tuple[str, str, dict]]:
    """Keep crutches out of the 1D pool and 2D/3D beam (not just the accept gate)."""
    return [c for c in candidates if not is_dead_path_crutch(base, c[2])]


def accept_macro_candidate(base: dict, cand: dict, **kwargs) -> AcceptDecision:
    """Same gates as kanon, plus: don't 'heal' a dead dual-path by lowering its threshold."""
    params = cand.get("params") or {}
    if is_dead_path_crutch(base, params):
        warns = " ".join(base.get("vitality_warnings") or [])
        for label, key in _DEAD_PATH_CRUTCH:
            if f"Martwa ścieżka {label}" in warns and int(params.get(key, 0) or 0) < 0:
                return AcceptDecision(
                    False,
                    f"użyteczność: obniżenie {key} przy martwej ścieżce {label} to proteza",
                    "hygiene",
                )
    return accept_candidate(base, cand, **kwargs)


def lookahead_next_action(
    *,
    depth: int,
    max_depth: int,
    has_pending: bool,
    found_better: bool,
) -> str:
    """Lookahead +1D (aa230d1 / 9d303fa): never apply on the depth that first improved.

    1D always peeks 2D even with no gain. After a new best, peek one layer deeper.
    If the deeper layer does not beat the held vector, apply the held (shallower) one.
    """
    can_go_deeper = depth < max_depth
    if found_better:
        return "hold_and_deeper" if can_go_deeper else "apply_current"
    if has_pending:
        return "apply_pending"
    if depth == 1 and can_go_deeper:
        return "deeper_empty"
    return "stop"


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
    d_4p = best_res_4p.get("score_4p_balance", best_res_4p["score_4p"]) - base_res_4p.get(
        "score_4p_balance", base_res_4p["score_4p"]
    )
    delta_4p_str = f"+{d_4p:.1f}" if d_4p > 0 else f"{d_4p:.1f}"

    patch_note_block = (
        f"### 🟢 Patch {new_version} ({today}) — Kanon 4P Makro: {change_desc} (Zysk 4P Δ {delta_4p_str} pkt)\n"
        f"- **Wynik 4P (win share):** **`{best_res_4p.get('score_4p_balance', best_res_4p['score_4p']):.1f} pkt`** "
        f"(baza `{base_res_4p.get('score_4p_balance', base_res_4p['score_4p']):.1f}`) | "
        f"blended `{base_res_4p['score_4p']:.1f}` → `{best_res_4p['score_4p']:.1f}` | "
        f"Global **`{diag_after['global_score']:.1f}`** | 3p **`{diag_after['cat_scores'].get('3p',0.0):.1f}`** | 5p **`{diag_after['cat_scores'].get('5p',0.0):.1f}`**\n"
        f"- **Modyfikacja (`{rule_id}`):** {change_desc}.\n"
        f"- **Efekt:** Makro L1/L2/L4. Telemetria: Średnia Er {best_res_4p['eras_avg']:.2f}, "
        f"Deadlocks {best_res_4p['deadlock_pct']:.1f}%, Pas Biedy {best_res_4p['poverty_pct']:.1f}%. "
        f"Witalność `{base_res_4p.get('vitality_penalty', 0):.3f}` → `{best_res_4p.get('vitality_penalty', 0):.3f}`.\n\n"
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

    d_4p = best_res_4p.get("score_4p_balance", best_res_4p["score_4p"]) - base_res_4p.get(
        "score_4p_balance", base_res_4p["score_4p"]
    )
    d4_str = f"+{d_4p:.1f}" if d_4p > 0 else f"{d_4p:.1f}"

    d_3p = diag_after["cat_scores"].get("3p", 0) - diag_before["cat_scores"].get("3p", 0)
    d3_str = f"+{d_3p:.1f}" if d_3p > 0 else f"{d_3p:.1f}"

    d_5p = diag_after["cat_scores"].get("5p", 0) - diag_before["cat_scores"].get("5p", 0)
    d5_str = f"+{d_5p:.1f}" if d_5p > 0 else f"{d_5p:.1f}"

    d_glob = diag_after["global_score"] - diag_before["global_score"]
    dg_str = f"+{d_glob:.1f}" if d_glob > 0 else f"{d_glob:.1f}"

    score_4p_col = (
        f"{base_res_4p.get('score_4p_balance', base_res_4p['score_4p']):.1f} → "
        f"**{best_res_4p.get('score_4p_balance', best_res_4p['score_4p']):.1f}** (`{d4_str}`) "
        f"vit {base_res_4p.get('vitality_penalty', 0):.2f}→{best_res_4p.get('vitality_penalty', 0):.2f}"
    )
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
    """Autonomous continuous balancer for Canonical 4P macro parameters (no cards)."""

    def __init__(self, args: argparse.Namespace):
        self.args = args
        self.total_iterations = 0
        self.start_time = time.time()
        self.stop_requested = False
        self._base_in_band = False
        signal.signal(signal.SIGINT, self._handle_sigint)

    def _accept_mode(self) -> str:
        return getattr(self.args, "accept_mode", "band")

    def _rank(self, res: dict) -> tuple:
        return rank_key(res, mode=self._accept_mode(), base_in_band=self._base_in_band)

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
                if best_so_far is None or self._rank(res) < self._rank(best_so_far):
                    best_so_far = res

                elapsed = time.time() - t0
                rate = idx / elapsed if elapsed > 0 else 0
                eta_s = (total - idx) / rate if rate > 0 else 0
                eta_str = f"{int(eta_s // 60)}m {int(eta_s % 60):02d}s" if eta_s >= 60 else f"{int(eta_s)}s"
                lead_id = best_so_far['id'][:26] if best_so_far else "-"
                if best_so_far:
                    lead_sc = (
                        f"{best_so_far.get('score_4p_balance', best_so_far['score_4p']):.1f}"
                        f" vit {best_so_far.get('vitality_penalty', 0):.2f}"
                    )
                else:
                    lead_sc = "-"
                sys.stdout.write(f"\r⏳ [{label}] [{idx:4d}/{total:4d}] ({idx*100.0/total:5.1f}%) | {rate:4.1f} zad/s | ETA: {eta_str:<7s} | Lider 4P: {lead_id} ({lead_sc})  ")
                sys.stdout.flush()

        sys.stdout.write(f"\n   ✔ Ukończono {total} zadań w {round(time.time() - t0, 1)}s.\n")
        return results

    def _commit_patch(
        self,
        *,
        accepted_candidate: tuple[str, str, dict],
        best_ver_res: dict,
        base_res: dict,
        phase: int,
        iter_start: float,
    ) -> None:
        """Write an accepted lookahead vector to SSOT (or print dry-run)."""
        self.total_iterations += 1
        rule_id, _rule_name, rule_params = accepted_candidate

        with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
            raw_cfg = yaml.safe_load(f)

        old_version = raw_cfg.get("version", "v0.51")
        mod_cfg, change_desc = apply_mutation_to_config(raw_cfg, rule_id, rule_params)

        print("\n🔬 [DIAGNOZA WPŁYWU NA POZOSTAŁE TRYBY (3P / 5P)]...")
        diag_before = _run_full_diagnostic({}, games_per_setup=1000, seed=self.args.seed)
        diag_after = _run_full_diagnostic(rule_params, games_per_setup=1000, seed=self.args.seed)

        d_3 = diag_after["cat_scores"].get("3p", 0) - diag_before["cat_scores"].get("3p", 0)
        d_5 = diag_after["cat_scores"].get("5p", 0) - diag_before["cat_scores"].get("5p", 0)
        d_g = diag_after["global_score"] - diag_before["global_score"]
        d3_sign = f"+{d_3:.1f}" if d_3 > 0 else f"{d_3:.1f}"
        d5_sign = f"+{d_5:.1f}" if d_5 > 0 else f"{d_5:.1f}"
        dg_sign = f"+{d_g:.1f}" if d_g > 0 else f"{d_g:.1f}"
        d_ws = best_ver_res.get("score_4p_balance", best_ver_res["score_4p"]) - base_res.get(
            "score_4p_balance", base_res["score_4p"]
        )
        print(
            f"   🎯 4P win share: {base_res.get('score_4p_balance', base_res['score_4p']):.1f} → "
            f"**{best_ver_res.get('score_4p_balance', best_ver_res['score_4p']):.1f} pkt** (Δ {d_ws:+.2f})"
        )
        print(
            f"   💤 Witalność:   {base_res.get('vitality_penalty', 0):.3f} → "
            f"{best_ver_res.get('vitality_penalty', 0):.3f}"
        )
        print(f"   👥 Wpływ 3p:  {diag_before['cat_scores'].get('3p',0):.1f} → {diag_after['cat_scores'].get('3p',0):.1f} pkt (`{d3_sign} pkt`)")
        print(f"   👥 Wpływ 5p:  {diag_before['cat_scores'].get('5p',0):.1f} → {diag_after['cat_scores'].get('5p',0):.1f} pkt (`{d5_sign} pkt`)")
        print(f"   🌐 Globalny:  {diag_before['global_score']:.1f} → {diag_after['global_score']:.1f} pkt (`{dg_sign} pkt`)")

        if self.args.dry_run:
            print(f"\n[DRY RUN] Zaakceptowano by wektor {phase}D: {change_desc}")
            return

        new_version, _saved_path = save_config_and_bump_version(mod_cfg, _CONFIG_PATH, bump_version=True)
        iter_elapsed = round(time.time() - iter_start, 2)
        print(f"\n🎉 [ZAAKCEPTOWANO PATCH KANONU 4P MAKRO #{self.total_iterations} — FAZA {phase}D]")
        print(f"   Wersja:        `{old_version}` → **`{new_version}`**")
        print(f"   Modyfikacja:   {change_desc}")

        version_archive_dir = REPORTS_DIR / "archive" / new_version
        version_archive_dir.mkdir(parents=True, exist_ok=True)
        log_4p_iteration(
            version_archive_dir / "audytor_4p_log.md",
            self.total_iterations,
            phase,
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
        print("   🔄 Synchronizuję SSOT (zasady / YAML — bez talii kart)...")
        subprocess.run([sys.executable, str(TOOLS_SIM_DIR.parent / "sync_config.py")])
        print("   ✔ Zsynchronizowano config i księgę.")

    def run(self):
        print("═══════════════════════════════════════════════════════════════════════")
        print("   INQUISITIO-1492 — AUDYTOR 4P MAKRO (Adaptive Lookahead +1D) ")
        print("   Optymalizacja parametrów makro L1, L2, L4 dla 5 setupów Kanonu 4P   ")
        print("═══════════════════════════════════════════════════════════════════════")
        print(f"Bieżąca wersja bazowa:      {CONFIG.version}")
        print(f"Maksymalny czas sesji:      {self.args.hours if self.args.hours else 'Brak limitu (do optimum)'} godz.")
        print(f"Maksymalnie patchów:        {self.args.max_iters if self.args.max_iters else 'Brak (do optimum)'}")
        print(f"Kanon Setupy:               {', '.join(CANONICAL_4P_SETUPS)}")
        print(f"Etap 1 (Szybki przesiew):   {self.args.fast_games} gier/setup ({len(CANONICAL_4P_SETUPS)} setupów 4p)")
        print(f"Etap 2 (Głęboki przesiew):  {self.args.screen_games} gier/setup (TOP {self.args.top_semifinalists} półfinalistów)")
        print(f"Etap 3 (Weryfikacja Ultra): {self.args.confirm_games} gier/setup (TOP {self.args.top_k} finalistów)")
        print(f"Lookahead +1D:              max głębokość {self.args.max_depth}D (1D zawsze zagląda w 2D)")
        print(f"Wątki procesora:            {self.args.workers}")
        print(f"Tryb przyjęcia patcha:      {self._accept_mode()} (witalność w rankingu; bez kart L3)")
        print(f"Archiwizacja raportów:     {REPORTS_DIR}/archive/<wersja>/")
        print("═══════════════════════════════════════════════════════════════════════\n")

        setups = CANONICAL_4P_SETUPS
        time_limit_sec = (self.args.hours * 3600) if self.args.hours else None
        max_depth = int(getattr(self.args, "max_depth", 4))

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

            print(f"   🎯 Wynik Kanonu 4P (win share): {color_score(base_res['score_4p_balance'], bold=True)} pkt")
            print(
                f"   📐 Blended (legacy): {color_score(base_res['score_4p'])} pkt | "
                f"min `{base_res['min_balance_setup']}` {color_score(base_res['min_balance'])} | "
                f"witalność kara {base_res['vitality_penalty']:.3f}"
            )
            self._base_in_band = setup_shares_in_range(base_res.get("setup_shares") or {}, *TARGET_BAND_PCT)
            band_label = "w paśmie 20–30% → higiena" if self._base_in_band else "poza pasmem 20–30% → wspinaczka maximin"
            print(f"   🎚️ Pasmo 4P: {band_label}")
            warns = base_res.get("vitality_warnings") or []
            if warns:
                print("   💤 Witalność (użyteczność dual-win) — audytor leczy to makro, nie obniżeniem progu:")
                for w in warns:
                    print(f"      • {w}")
            if canon_should_stop(base_res, mode=self._accept_mode()):
                print("\n🏁 Kanon 4P w paśmie i mechaniki żywe — stop.")
                break
            for sname, bal in sorted(base_res["setup_scores_balance"].items()):
                blended = base_res["setup_scores"].get(sname, bal)
                print(f"      • `{sname}`: {color_score(bal, bold=True)} pkt (blended {color_score(blended)})")
            print(f"   ⏱️ Średnia Er: {base_res['eras_avg']:.2f} | Deadlocks: {base_res['deadlock_pct']:.1f}% | Pas Biedy: {base_res['poverty_pct']:.1f}%")

            # 2. Lookahead +1D: hold improvements, peek one layer deeper, then apply the held vector.
            atomic_pool = drop_dead_path_crutches(base_res, generate_all_atomic_candidates_macro())
            pending_cand: tuple[str, str, dict] | None = None
            pending_res: dict | None = None
            pending_phase: int | None = None
            current_phase = 1
            beam_seeds: list[tuple[str, str, dict]] = []
            applied = False
            search_exhausted = False

            while not self.stop_requested and current_phase <= max_depth:
                if time_limit_sec and (time.time() - self.start_time) >= time_limit_sec:
                    print(f"\n⏱️ Osiągnięto limit czasu sesji ({self.args.hours}h). Kończę pracę.")
                    search_exhausted = True
                    break

                if current_phase == 1 or not beam_seeds:
                    print(f"\n🌐 [FAZA 1D — MAKRO 4P] Pula L1/L2/L4 ±1 + skraj/off, bez kart ({len(atomic_pool)} wariantów)...")
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
                if not candidate_pool:
                    action = lookahead_next_action(
                        depth=current_phase,
                        max_depth=max_depth,
                        has_pending=pending_cand is not None,
                        found_better=False,
                    )
                    if action == "apply_pending" and pending_cand is not None and pending_res is not None:
                        print(f"\n🛑 Brak kombinacji {current_phase}D — wdrażam held {pending_phase}D.")
                        self._commit_patch(
                            accepted_candidate=pending_cand,
                            best_ver_res=pending_res,
                            base_res=base_res,
                            phase=pending_phase or current_phase,
                            iter_start=iter_start,
                        )
                        applied = True
                    else:
                        print(f"\n🏁 Brak dalszych niekolidujących kombinacji na {current_phase}D.")
                        search_exhausted = True
                    break
                cand_dict = {c[0]: c for c in candidate_pool}

                # 3. ETAP 1/3: Szybki Przesiew na 5 setupach 4P
                print(f"\n--- [ETAP 1/3: SZYBKI PRZESIEW 4P] Testuję {len(candidate_pool)} kandydatów ({self.args.fast_games} gier/setup × 5 setupów) ---")
                stage1_tasks = [((c[0], c[1], c[2]), self.args.fast_games, self.args.seed, setups) for c in candidate_pool]
                stage1_results = self._execute_pool(_run_single_test_task_4p, stage1_tasks, label=f"Przesiew 4P 1/3")

                stage1_results.sort(key=self._rank)

                n_semifinalists = min(self.args.top_semifinalists, len(stage1_results))
                semifinalist_results = stage1_results[:n_semifinalists]
                semifinalist_candidates = [cand_dict[r["id"]] for r in semifinalist_results]

                # 4. ETAP 2/3: Głęboki Przesiew 4P
                print(f"\n--- [ETAP 2/3: GŁĘBOKI PRZESIEW 4P] Badam TOP {len(semifinalist_candidates)} półfinalistów ({self.args.screen_games} gier/setup × 5 setupów) ---")
                stage2_tasks = [((c[0], c[1], c[2]), self.args.screen_games, self.args.seed, setups) for c in semifinalist_candidates]
                stage2_results = self._execute_pool(_run_single_test_task_4p, stage2_tasks, label=f"Przesiew 4P 2/3")

                stage2_results.sort(key=self._rank)

                n_finalists = min(self.args.top_k, len(stage2_results))
                finalist_results = stage2_results[:n_finalists]
                finalist_candidates = [cand_dict[r["id"]] for r in finalist_results]

                # 5. ETAP 3/3: Weryfikacja Ultra 4P
                print(f"\n--- [ETAP 3/3: WERYFIKACJA ULTRA 4P] Weryfikuję TOP {len(finalist_candidates)} finalistów ({self.args.confirm_games} gier/setup × 5 setupów) ---")
                stage3_tasks = [((c[0], c[1], c[2]), self.args.confirm_games, self.args.seed, setups) for c in finalist_candidates]
                stage3_results = self._execute_pool(_run_single_test_task_4p, stage3_tasks, label=f"Weryfikacja 4P 3/3")

                stage3_results.sort(key=self._rank)

                print(f"\n📊 [WYNIKI WERYFIKACJI FINALISTÓW KANONU 4P] {current_phase}D")
                for idx, r in enumerate(stage3_results, 1):
                    decision = accept_macro_candidate(
                        base_res, r, mode=self._accept_mode(), min_delta=self.args.min_delta
                    )
                    print(
                        f"   #{idx:2d} [{r['id'][:42]}...] win share {r.get('score_4p_balance', r['score_4p']):.1f} | "
                        f"witalność {r.get('vitality_penalty', 0):.3f} | {decision.reason}"
                    )

                accepted_candidate = None
                best_ver_res = None
                for ver_res in stage3_results:
                    decision = accept_macro_candidate(
                        base_res, ver_res, mode=self._accept_mode(), min_delta=self.args.min_delta
                    )
                    if decision.accepted:
                        accepted_candidate = cand_dict[ver_res["id"]]
                        best_ver_res = ver_res
                        break

                if accepted_candidate is None or best_ver_res is None:
                    found_better = False
                elif pending_res is None:
                    found_better = True
                else:
                    found_better = self._rank(best_ver_res) < self._rank(pending_res)

                action = lookahead_next_action(
                    depth=current_phase,
                    max_depth=max_depth,
                    has_pending=pending_cand is not None,
                    found_better=found_better,
                )
                top_beam = drop_dead_path_crutches(
                    base_res,
                    [cand_dict[r["id"]] for r in stage3_results[: self.args.beam_width] if r["id"] in cand_dict],
                )

                if action == "hold_and_deeper":
                    pending_cand = accepted_candidate
                    pending_res = best_ver_res
                    pending_phase = current_phase
                    beam_seeds = top_beam
                    print(
                        f"\n✨ Nowe optimum na {current_phase}D (`{pending_cand[0]}`) — "
                        f"NIE wdrażam, lookahead {current_phase + 1}D ({len(beam_seeds)} nasion)."
                    )
                    current_phase += 1
                    continue

                if action == "deeper_empty":
                    beam_seeds = top_beam
                    print(
                        f"\n⚪ Brak wariantu do przyjęcia w 1D — i tak sprawdzam 2D "
                        f"(lookahead +1D, {len(beam_seeds)} nasion)."
                    )
                    current_phase += 1
                    continue

                if action == "apply_pending" and pending_cand is not None and pending_res is not None:
                    print(
                        f"\n🛑 {current_phase}D nie przebiło held {pending_phase}D "
                        f"(`{pending_cand[0]}`) — wdrażam wcześniejszy wektor."
                    )
                    self._commit_patch(
                        accepted_candidate=pending_cand,
                        best_ver_res=pending_res,
                        base_res=base_res,
                        phase=pending_phase or current_phase,
                        iter_start=iter_start,
                    )
                    applied = True
                    break

                if action == "apply_current" and accepted_candidate is not None and best_ver_res is not None:
                    print(f"\n🏁 Max głębokość {max_depth}D — wdrażam bieżący wektor (`{accepted_candidate[0]}`).")
                    self._commit_patch(
                        accepted_candidate=accepted_candidate,
                        best_ver_res=best_ver_res,
                        base_res=base_res,
                        phase=current_phase,
                        iter_start=iter_start,
                    )
                    applied = True
                    break

                print(
                    f"\n🏁 Brak zmian makro przynoszących zysk w 4P na {current_phase}D "
                    f"(lookahead +1D wyczerpany). Bieżący stan jest lokalnym optimum puli."
                )
                search_exhausted = True
                break

            if self.args.dry_run and applied:
                break
            if search_exhausted:
                break

        print(f"\n═══════════════════════════════════════════════════════════════════════")
        print(f"   AUDYTOR 4P MAKRO ZAKOŃCZYŁ SESJĘ. ŁĄCZNIE WPROWADZONO {self.total_iterations} PATCHY.")
        print(f"═══════════════════════════════════════════════════════════════════════\n")


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 Audytor 4P Makro (Adaptive Lookahead +1D)")
    parser.add_argument("--hours", type=float, default=None, help="Maksymalny czas działania w godzinach (np. 4.0)")
    parser.add_argument("--max-iters", type=int, default=None, help="Maksymalna liczba udanych patchów przed zatrzymaniem")
    parser.add_argument("--fast-games", type=int, default=200, help="Liczba gier w Etapie 1 na 5 setupach 4p (domyślnie: 200)")
    parser.add_argument("--screen-games", type=int, default=1000, help="Liczba gier w Etapie 2 na 5 setupach 4p (domyślnie: 1000)")
    parser.add_argument("--confirm-games", type=int, default=5000, help="Liczba gier w Etapie 3 na 5 setupach 4p (domyślnie: 5000)")
    parser.add_argument("--top-semifinalists", type=int, default=48, help="Liczba półfinalistów sprawdzanych w Etapie 2 (domyślnie: 48)")
    parser.add_argument("--top-k", type=int, default=24, help="Liczba finalistów sprawdzanych w Etapie 3 (domyślnie: 24)")
    parser.add_argument("--beam-width", type=int, default=12, help="Nasiona wiązki 2D/3D (domyślnie: 12)")
    parser.add_argument("--max-depth", type=int, default=4, help="Maksymalna głębokość Lookahead +1D (domyślnie: 4)")
    parser.add_argument("--min-delta", type=float, default=0.05, help="Minimalny zysk punktowy dla 4P wymagany do wdrożenia patcha (pkt, domyślnie: 0.05)")
    parser.add_argument("--workers", type=int, default=min(os.cpu_count() or 4, 10), help="Liczba procesów równoległych")
    parser.add_argument("--seed", type=int, default=42, help="Ziarno generatora liczb losowych")
    parser.add_argument("--dry-run", action="store_true", help="Tryb symulacji bez zapisywania zmian do game_config.yaml")
    parser.add_argument(
        "--accept-mode",
        choices=("legacy", "band"),
        default="band",
        help=(
            "band (domyślnie): win share + witalność jak kanon — maximin poza pasmem 20–30%%, "
            "higiena w paśmie, stop gdy stół żywy. Bez kart L3. "
            "legacy: max blended 4P (kosmetyka +0.1)."
        ),
    )

    args = parser.parse_args()

    if args.fast_games < 100:
        args.fast_games = 100
    if args.screen_games < 500:
        args.screen_games = 500
    if args.confirm_games < 3000:
        args.confirm_games = 3000
    if args.max_depth < 2:
        args.max_depth = 2

    auditor = Macro4PAutoBalancer(args)
    auditor.run()


if __name__ == "__main__":
    main()
