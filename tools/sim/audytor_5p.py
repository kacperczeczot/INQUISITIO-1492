#!/usr/bin/env python3
"""INQUISITIO-1492 — AUDYTOR 5P (5-Player Autonomous Balance Optimizer).

Bliźniaczy, autonomiczny optymalizator balansu dla formatu 5-osobowego (5P Full),
oparty na identycznej architekturze jak Audytor Kanonu 4P.

Główne założenia metodologiczne:
  1. Setup 5-osobowy: 5p-full (12 obcych agentów przy stole).
  2. Talia kart (L3), Kanon 4P i gałki całego stołu (Obserwowana, karty/erę,
     Gospodarcza, Er, CD Autodafé, szlak) są NIENARUSZALNE — zapis tylko `5p:`.
  3. Błyskawiczny 3-Stopniowy Lejek Sukcesywnej Selekcji (L1 + L2 + L4):
     - Etap 1 (Szybki Przesiew): 500 gier -> TOP 24 półfinalistów (~1.5s)
     - Etap 2 (Głęboki Przesiew): 1500 gier -> TOP 12 finalistów (~3s)
     - Etap 3 (Weryfikacja Ultra): 5000 gier -> Zwycięski Patch (~6s)
  4. **Lookahead +1D** (jak Audytor 4P): nie wdraża poprawy na głębokości, na której ją
     znalazł — 1D zawsze zagląda w 2D; dalej tylko gdy nowa głębokość bije held.
     Zapis idzie w wyjątki `5p:` (Kanon 4P i L3 nietknięte). Ranking: blended setup_score.
     Bramka witalności: proteza skazań/stosów −1 przy martwej ścieżce jest odrzucana.
  5. Pełna automatyzacja dokumentacji i SSOT:
     - Zapisuje wyjątki per-5p pod sekcjami '5p:' w game_config.yaml (z podbiciem wersji)
     - playtesting/sim-reports/archive/<wersja>/audytor_5p_log.md
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
from inquisitio.config_updater import save_config_and_bump_version
from inquisitio.engine.setup import SETUP_PRESETS, FactionId
from inquisitio.runner.audit_facts import score_pair, save_and_archive_report
from inquisitio.runner.batch import run_batch
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
    cheap_funnel_flags,
    drop_dead_path_crutches,
    is_ablation_off,
    is_frozen_identity_knob,
    is_table_wide_canon_knob,
    strip_table_wide_canon_params,
    lookahead_next_action,
)

REPORTS_DIR = Path(__file__).resolve().parent.parent.parent / "playtesting" / "sim-reports"
BALANCE_NOTES_PATH = Path(__file__).resolve().parent.parent.parent / "playtesting" / "balance-notes.md"

SETUPS_5P = ["5p-full"]

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


def _run_single_test_task_5p(args_tuple: tuple) -> dict:
    """Worker task evaluating a single candidate mutation on 5P setup."""
    (cand_id, cand_name, rule_params), games_per_setup, seed, setups = args_tuple

    summaries = []
    setup_scores = {}
    vitality_penalties = []
    vitality_warnings: list[str] = []
    fshares = {fid: [] for fid in FACTION_NAMES.keys()}

    for sname in setups:
        s = run_batch(games=games_per_setup, setup=sname, seed=seed, layer="C", win_overrides=rule_params)
        summaries.append(s)
        sc = calculate_setup_score(s)
        setup_scores[sname] = sc
        vit = evaluate_vitality(s)
        vitality_penalties.append(vit.vitality_penalty)
        for msg in vit.warnings:
            vitality_warnings.append(f"{sname}: {msg}")
        for fid, wins in s.wins.items():
            if s.games > 0:
                fid_enum = FactionId(fid) if not isinstance(fid, FactionId) else fid
                if fid_enum in fshares:
                    fshares[fid_enum].append(wins / s.games)

    score_5p = round(sum(setup_scores.values()) / len(setup_scores), 1) if setup_scores else 0.0
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
        "score_5p": score_5p,
        "setup_scores": setup_scores,
        "fshares": {FACTION_NAMES[k]: round(sum(v)/len(v)*100, 1) for k, v in fshares.items() if v},
        "eras_avg": eras_avg, "eras_min": eras_min, "eras_max": eras_max,
        "deadlock_pct": deadlock_pct,
        "poverty_pct": poverty_pct,
        "autodafe_avg": autodafe_avg,
        "acc_avg": acc_avg,
        "gold_avg": gold_avg,
        "vitality_penalty": max(vitality_penalties) if vitality_penalties else 0.0,
        "vitality_warnings": vitality_warnings,
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
    """L1/L2/L4 for 5P exceptions. No L3; SKU/ablation/Kronika stay out of the pool."""
    tests = []
    for builder, baza in (
        (audit_level1.build_level1_tests, "L1_BAZA"),
        (audit_level2.build_level2_tests, "L2_BAZA"),
        (audit_level4.build_level4_tests, "L4_BAZA"),
    ):
        for t in builder():
            if t[0] == baza or is_frozen_identity_knob(t[0], t[2]) or is_ablation_off(t[0], t[2]):
                continue
            if is_table_wide_canon_knob(t[0], t[2]):
                continue
            tests.append(t)
    return tests


def merge_mutations(m1: tuple[str, str, dict], m2: tuple[str, str, dict]) -> tuple[str, str, dict] | None:
    """Merges two mutations into a composite mutation."""
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
        _set_5p(cfg.setdefault("system", {}), "accusation_threshold", 8, rule_params["threshold_offset"], "Próg oskarżenia")

    # L2
    vic = cfg.setdefault("victory", {})
    if "so_stacks_offset" in rule_params:
        _set_5p(vic.setdefault("swiete_oficjum", {}), "stacks", 5, rule_params["so_stacks_offset"], "SO Stosy")
    if "so_condemns_offset" in rule_params:
        _set_5p(vic.setdefault("swiete_oficjum", {}), "condemns", 2, rule_params["so_condemns_offset"], "SO Skazania")
    if "caa_relics_offset" in rule_params:
        _set_5p(vic.setdefault("cienie_al_andalus", {}), "relics", 2, rule_params["caa_relics_offset"], "CAA Relikwie")
    if "caa_era_offset" in rule_params:
        _set_5p(vic.setdefault("cienie_al_andalus", {}), "path_era", 5, rule_params["caa_era_offset"], "CAA Era")
    if "kb_decrees_offset" in rule_params:
        _set_5p(vic.setdefault("korona_borgiowie", {}), "decrees", 2, rule_params["kb_decrees_offset"], "KB Dekrety")
    if "kt_frags_offset" in rule_params:
        _set_5p(vic.setdefault("kabala_toledo", {}), "fragments", 3, rule_params["kt_frags_offset"], "KT Fragmenty")
    if "kt_era_offset" in rule_params:
        _set_5p(vic.setdefault("kabala_toledo", {}), "era", 6, rule_params["kt_era_offset"], "KT Era")
    if "gc_falls_default_offset" in rule_params or "gc_falls_offset" in rule_params:
        off = rule_params.get("gc_falls_offset", rule_params.get("gc_falls_default_offset", 0))
        _set_5p(vic.setdefault("gildia_cieni", {}), "falls", 4, off, "GC Upadki")

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
    """Automatically update playtesting/balance-notes.md with patch note entry."""
    if not BALANCE_NOTES_PATH.exists():
        return

    content = BALANCE_NOTES_PATH.read_text(encoding="utf-8")
    today = datetime.now().strftime("%Y-%m-%d")
    d_5p = best_res_5p["score_5p"] - base_res_5p["score_5p"]
    delta_5p_str = f"+{d_5p:.1f}" if d_5p > 0 else f"{d_5p:.1f}"

    patch_note_block = (
        f"### 🟢 Patch {new_version} ({today}) — Format 5P: {change_desc} (Zysk 5P Δ {delta_5p_str} pkt)\n"
        f"- **Wynik 5P:** 5p **`{base_res_5p['score_5p']:.1f}`** → **`{best_res_5p['score_5p']:.1f} pkt`** | Kanon 4P **`{diag_after['cat_scores'].get('4p',0.0):.1f}`** | 3p **`{diag_after['cat_scores'].get('3p',0.0):.1f}`** | Global **`{diag_after['global_score']:.1f}`**\n"
        f"- **Modyfikacja (`{rule_id}`):** {change_desc}.\n"
        f"- **Efekt:** Optymalizacja formatu 5P. Telemetria: Średnia Er {best_res_5p['eras_avg']:.2f}, Deadlocks {best_res_5p['deadlock_pct']:.1f}%, Pas Biedy {best_res_5p['poverty_pct']:.1f}%.\n\n"
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
            "# Dziennik Optymalizacji Formatu 5P (Audytor 5P)",
            "",
            "Rejestr wdrożonych patchów wyjątków formatu 5-osobowego.",
            "",
            "| Iteracja | Faza | Data i Czas | Wersja | Modyfikacja 5P | 5P Score | Wpływ na 4p | Wpływ na 3p | Global Score | Deadlocks % | Pas Biedy % | Czas |",
            "| :---: | :---: | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
        ]
        log_path.write_text("\n".join(headers) + "\n", encoding="utf-8")

    d_5p = best_res_5p["score_5p"] - base_res_5p["score_5p"]
    d5_str = f"+{d_5p:.1f}" if d_5p > 0 else f"{d_5p:.1f}"

    d_4p = diag_after["cat_scores"].get("4p", 0) - diag_before["cat_scores"].get("4p", 0)
    d4_str = f"+{d_4p:.1f}" if d_4p > 0 else f"{d_4p:.1f}"

    d_3p = diag_after["cat_scores"].get("3p", 0) - diag_before["cat_scores"].get("3p", 0)
    d3_str = f"+{d_3p:.1f}" if d_3p > 0 else f"{d_3p:.1f}"

    d_glob = diag_after["global_score"] - diag_before["global_score"]
    dg_str = f"+{d_glob:.1f}" if d_glob > 0 else f"{d_glob:.1f}"

    score_5p_col = f"{base_res_5p['score_5p']:.1f} → **{best_res_5p['score_5p']:.1f}** (`{d5_str}`)"
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


class AutoBalancer5P:
    """Autonomous continuous balancer for 5-player format exceptions."""

    def __init__(self, args: argparse.Namespace):
        self.args = args
        self.total_iterations = 0
        self.start_time = time.time()
        self.stop_requested = False
        signal.signal(signal.SIGINT, self._handle_sigint)

    def _handle_sigint(self, signum, frame):
        print("\n\n⚠️ Otrzymano sygnał przerwania (Ctrl+C). Bezpiecznie kończę bieżącą iterację...")
        self.stop_requested = True

    def _execute_pool(self, task_func, task_list: list, label: str = "Testy 5P") -> list[dict]:
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
                if best_so_far is None or res["score_5p"] > best_so_far["score_5p"]:
                    best_so_far = res

                elapsed = time.time() - t0
                rate = idx / elapsed if elapsed > 0 else 0
                eta_s = (total - idx) / rate if rate > 0 else 0
                eta_str = f"{int(eta_s // 60)}m {int(eta_s % 60):02d}s" if eta_s >= 60 else f"{int(eta_s)}s"
                lead_id = best_so_far['id'][:26] if best_so_far else "-"
                lead_sc = (
                    f"{best_so_far['score_5p']:.1f} vit {best_so_far.get('vitality_penalty', 0):.2f}"
                    if best_so_far
                    else "-"
                )
                sys.stdout.write(f"\r⏳ [{label}] [{idx:4d}/{total:4d}] ({idx*100.0/total:5.1f}%) | {rate:4.1f} zad/s | ETA: {eta_str:<7s} | Lider 5P: {lead_id} ({lead_sc})  ")
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
        """Write an accepted lookahead vector to 5p: YAML exceptions (or print dry-run)."""
        self.total_iterations += 1
        rule_id, _rule_name, rule_params = accepted_candidate

        with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
            raw_cfg = yaml.safe_load(f)

        old_version = raw_cfg.get("version", "v0.51")
        mod_cfg, change_desc = apply_mutation_to_5p_config(raw_cfg, rule_params)

        print("\n🔬 [DIAGNOZA WPŁYWU NA POZOSTAŁE TRYBY (4P / 3P)]...")
        diag_before = _run_full_diagnostic({}, games_per_setup=1000, seed=self.args.seed)
        diag_after = _run_full_diagnostic(rule_params, games_per_setup=1000, seed=self.args.seed)

        d_4 = diag_after["cat_scores"].get("4p", 0) - diag_before["cat_scores"].get("4p", 0)
        d_3 = diag_after["cat_scores"].get("3p", 0) - diag_before["cat_scores"].get("3p", 0)
        d_g = diag_after["global_score"] - diag_before["global_score"]
        d4_sign = f"+{d_4:.1f}" if d_4 > 0 else f"{d_4:.1f}"
        d3_sign = f"+{d_3:.1f}" if d_3 > 0 else f"{d_3:.1f}"
        dg_sign = f"+{d_g:.1f}" if d_g > 0 else f"{d_g:.1f}"
        print(
            f"   🎯 5P Format: {base_res['score_5p']:.1f} → **{best_ver_res['score_5p']:.1f} pkt** "
            f"(Δ {best_ver_res['score_5p'] - base_res['score_5p']:+.2f} pkt)"
        )
        print(
            f"   💤 Witalność:   {base_res.get('vitality_penalty', 0):.3f} → "
            f"{best_ver_res.get('vitality_penalty', 0):.3f}"
        )
        print(f"   👥 Kanon 4P:  {diag_before['cat_scores'].get('4p',0):.1f} → {diag_after['cat_scores'].get('4p',0):.1f} pkt (`{d4_sign} pkt`)")
        print(f"   👥 Wpływ 3p:  {diag_before['cat_scores'].get('3p',0):.1f} → {diag_after['cat_scores'].get('3p',0):.1f} pkt (`{d3_sign} pkt`)")
        print(f"   🌐 Globalny:  {diag_before['global_score']:.1f} → {diag_after['global_score']:.1f} pkt (`{dg_sign} pkt`)")

        if self.args.dry_run:
            print(f"\n[DRY RUN] Zaakceptowano by wektor {phase}D (wyjątek 5p:): {change_desc}")
            return

        new_version, _saved_path = save_config_and_bump_version(mod_cfg, _CONFIG_PATH, bump_version=True)
        iter_elapsed = round(time.time() - iter_start, 2)
        print(f"\n🎉 [ZAAKCEPTOWANO PATCH FORMATU 5P #{self.total_iterations} — FAZA {phase}D]")
        print(f"   Wersja:        `{old_version}` → **`{new_version}`**")
        print(f"   Modyfikacja:   {change_desc}")

        version_archive_dir = REPORTS_DIR / "archive" / new_version
        version_archive_dir.mkdir(parents=True, exist_ok=True)
        log_5p_iteration(
            version_archive_dir / "audytor_5p_log.md",
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
        update_balance_notes_5p(
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

    def run(self):
        print("═══════════════════════════════════════════════════════════════════════")
        print("   INQUISITIO-1492 — AUDYTOR 5P (Adaptive Lookahead +1D)                ")
        print("   Wyjątki 5p: — bez ruszania kanonu 4P i kart (L3)                     ")
        print("═══════════════════════════════════════════════════════════════════════")
        print(f"Bieżąca wersja bazowa:      {CONFIG.version}")
        print(f"Maksymalny czas sesji:      {self.args.hours if self.args.hours else 'Brak limitu (do optimum)'} godz.")
        print(f"Maksymalnie patchów:        {self.args.max_iters if self.args.max_iters else 'Brak (do optimum)'}")
        print(f"Setup 5P:                   5p-full")
        print(f"Etap 1 (Szybki przesiew):   {self.args.fast_games} gier (5p-full)")
        print(f"Etap 2 (Głęboki przesiew):  {self.args.screen_games} gier (TOP {self.args.top_semifinalists} półfinalistów)")
        print(f"Etap 3 (Weryfikacja Ultra): {self.args.confirm_games} gier (TOP {self.args.top_k} finalistów)")
        print(f"Lookahead +1D:              max głębokość {self.args.max_depth}D (1D zawsze zagląda w 2D)")
        print(f"Wątki procesora:            {self.args.workers}")
        print(f"Ranking:                    blended setup_score (bez pasma 4P); witalność = veto protezy")
        print(f"Archiwizacja raportów:     {REPORTS_DIR}/archive/<wersja>/")
        print("═══════════════════════════════════════════════════════════════════════\n")

        setups = SETUPS_5P
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

            print(f"\n{'='*71}")
            print(f"🔍 [POMIAR BAZOWY FORMATU 5P] Diagnoza 5p-full (Próba: {self.args.confirm_games} gier)...")
            base_task = ((("BASE", "Bieżący stan 5P", {}), self.args.confirm_games, self.args.seed, setups),)
            base_res = self._execute_pool(_run_single_test_task_5p, [base_task[0]], label="Baza 5P")[0]

            print(f"   🎯 Wynik 5P Score: {color_score(base_res['score_5p'], bold=True)} pkt")
            print(f"   💤 Witalność kara: {base_res.get('vitality_penalty', 0):.3f}")
            warns = base_res.get("vitality_warnings") or []
            if warns:
                print("   💤 Witalność — audytor nie leczy obniżeniem progu dual-win:")
                for w in warns:
                    print(f"      • {w}")
            for sname, sc in sorted(base_res["setup_scores"].items()):
                print(f"      • `{sname}`: {color_score(sc, bold=True)} pkt")
            print(f"   ⏱️ Średnia Er: {base_res['eras_avg']:.2f} | Deadlocks: {base_res['deadlock_pct']:.1f}% | Pas Biedy: {base_res['poverty_pct']:.1f}%")

            atomic_pool = drop_dead_path_crutches(base_res, generate_all_atomic_candidates_5p())
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
                    print(f"\n🌐 [FAZA 1D — FORMAT 5P] Pula L1/L2/L4, bez kart ({len(atomic_pool)} wariantów)...")
                    candidate_pool = atomic_pool
                else:
                    print(f"\n🌐 [FAZA {current_phase}D — FORMAT 5P] Wiązki 5P (TOP {len(beam_seeds)} nasion × {len(atomic_pool)} mechanik)...")
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

                print(f"   🧬 Wygenerowano {len(candidate_pool)} unikalnych kandydatów dla Formatu 5P.")
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
                run_fast, run_screen = cheap_funnel_flags(
                    len(candidate_pool), self.args.top_semifinalists, self.args.top_k
                )
                survivors = list(candidate_pool)

                if run_fast:
                    print(f"\n--- [ETAP 1/3: SZYBKI PRZESIEW 5P] Testuję {len(survivors)} kandydatów ({self.args.fast_games} gier (5p-full)) ---")
                    stage1_tasks = [((c[0], c[1], c[2]), self.args.fast_games, self.args.seed, setups) for c in survivors]
                    stage1_results = self._execute_pool(_run_single_test_task_5p, stage1_tasks, label="Przesiew 5P 1/3")
                    stage1_results.sort(key=lambda r: r["score_5p"], reverse=True)
                    n_semifinalists = min(self.args.top_semifinalists, len(stage1_results))
                    survivors = [cand_dict[r["id"]] for r in stage1_results[:n_semifinalists]]
                else:
                    print(
                        f"\n⏭️ Pomijam etap 1 ({self.args.fast_games} g): "
                        f"{len(survivors)} ≤ TOP {self.args.top_semifinalists} — przesiew nic nie tnie."
                    )

                if run_screen:
                    print(f"\n--- [ETAP 2/3: GŁĘBOKI PRZESIEW 5P] Badam {len(survivors)} ({self.args.screen_games} gier (5p-full)) ---")
                    stage2_tasks = [((c[0], c[1], c[2]), self.args.screen_games, self.args.seed, setups) for c in survivors]
                    stage2_results = self._execute_pool(_run_single_test_task_5p, stage2_tasks, label="Przesiew 5P 2/3")
                    stage2_results.sort(key=lambda r: r["score_5p"], reverse=True)
                    n_finalists = min(self.args.top_k, len(stage2_results))
                    survivors = [cand_dict[r["id"]] for r in stage2_results[:n_finalists]]
                else:
                    print(
                        f"\n⏭️ Pomijam etap 2 ({self.args.screen_games} g): "
                        f"{len(survivors)} ≤ TOP {self.args.top_k} — idę na ultra."
                    )

                print(f"\n--- [ETAP 3/3: WERYFIKACJA ULTRA 5P] Weryfikuję {len(survivors)} ({self.args.confirm_games} gier (5p-full)) ---")
                stage3_tasks = [((c[0], c[1], c[2]), self.args.confirm_games, self.args.seed, setups) for c in survivors]
                stage3_results = self._execute_pool(_run_single_test_task_5p, stage3_tasks, label="Weryfikacja 5P 3/3")
                stage3_results.sort(key=lambda r: r["score_5p"], reverse=True)

                print(f"\n📊 [WYNIKI WERYFIKACJI FINALISTÓW FORMATU 5P] {current_phase}D")
                for idx, r in enumerate(stage3_results, 1):
                    decision = accept_format_exception(
                        base_res,
                        r,
                        score_key="score_5p",
                        min_delta=self.args.min_delta,
                        telemetry_ok=passes_telemetry_safety(r),
                    )
                    print(
                        f"   #{idx:2d} [{r['id'][:42]}...] 5P {r['score_5p']:.1f} | "
                        f"witalność {r.get('vitality_penalty', 0):.3f} | {decision.reason}"
                    )

                accepted_candidate = None
                best_ver_res = None
                for ver_res in stage3_results:
                    decision = accept_format_exception(
                        base_res,
                        ver_res,
                        score_key="score_5p",
                        min_delta=self.args.min_delta,
                        telemetry_ok=passes_telemetry_safety(ver_res),
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
                    found_better = best_ver_res["score_5p"] > pending_res["score_5p"]

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
                        f"(`{pending_cand[0]}`) — wdrażam wcześniejszy wektor (wyjątek 5p:)."
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
                    f"\n🏁 Brak zmian 5P przynoszących zysk na {current_phase}D "
                    f"(lookahead +1D wyczerpany). Bieżący stan jest lokalnym optimum puli."
                )
                search_exhausted = True
                break

            if self.args.dry_run and applied:
                break
            if search_exhausted:
                break

        print(f"\n═══════════════════════════════════════════════════════════════════════")
        print(f"   AUDYTOR 5P ZAKOŃCZYŁ SESJĘ. ŁĄCZNIE WPROWADZONO {self.total_iterations} PATCHY.")
        print(f"═══════════════════════════════════════════════════════════════════════\n")


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 Audytor 5P (Adaptive Lookahead +1D)")
    parser.add_argument("--hours", type=float, default=None, help="Maksymalny czas działania w godzinach (np. 4.0)")
    parser.add_argument("--max-iters", type=int, default=None, help="Maksymalna liczba udanych patchów przed zatrzymaniem")
    parser.add_argument("--fast-games", type=int, default=500, help="Liczba gier w Etapie 1 na 5p-full (domyślnie: 500)")
    parser.add_argument("--screen-games", type=int, default=1500, help="Liczba gier w Etapie 2 na 5p-full (domyślnie: 1500)")
    parser.add_argument("--confirm-games", type=int, default=5000, help="Liczba gier w Etapie 3 na 5p-full (domyślnie: 5000)")
    parser.add_argument("--top-semifinalists", type=int, default=24, help="Liczba półfinalistów sprawdzanych w Etapie 2 (domyślnie: 24)")
    parser.add_argument("--top-k", type=int, default=12, help="Liczba finalistów sprawdzanych w Etapie 3 (domyślnie: 12)")
    parser.add_argument("--beam-width", type=int, default=8, help="Liczba najlepszych kandydatów kwalifikowanych do nasion kolejnej fazy wiązek (domyślnie: 8)")
    parser.add_argument("--max-depth", type=int, default=4, help="Maksymalna głębokość Lookahead +1D (domyślnie: 4)")
    parser.add_argument("--min-delta", type=float, default=0.05, help="Minimalny zysk punktowy dla 5P wymagany do wdrożenia patcha (pkt, domyślnie: 0.05)")
    parser.add_argument("--workers", type=int, default=min(os.cpu_count() or 4, 10), help="Liczba procesów równoległych")
    parser.add_argument("--seed", type=int, default=42, help="Ziarno generatora liczb losowych")
    parser.add_argument("--dry-run", action="store_true", help="Tryb symulacji bez zapisywania zmian do game_config.yaml")

    args = parser.parse_args()

    if args.fast_games < 200:
        args.fast_games = 200
    if args.screen_games < 800:
        args.screen_games = 800
    if args.confirm_games < 3000:
        args.confirm_games = 3000
    if args.max_depth < 2:
        args.max_depth = 2

    auditor = AutoBalancer5P(args)
    auditor.run()


if __name__ == "__main__":
    main()
