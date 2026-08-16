#!/usr/bin/env python3
"""INQUISITIO-1492 — AUDYTOR 3P (3-Player Adaptive Depth Lookahead Optimizer).

Autonomiczny optymalizator balansu dedykowany dla 10 setupów 3-osobowych (3P).
Zasady działania:
  1. Kanon 4P i talia 50 kart (L3) są w 100% NIENARUSZALNE.
  2. Optymalizacja operuje wyłącznie na parametrach formatu 3P (L1, L2, L4):
     - L1: start_gold (3p), accusation_threshold (3p)
     - L2: warunki zwycięstwa frakcji specyficzne dla 3P (so_stacks, kb_era, kt_frags, kt_era, gc_falls itp.)
     - L4: szlak morski (3p)
  3. Adaptacyjny Algorytm Wybiegający w Przód (Adaptive Lookahead +1D):
     - Zawsze bada poziom k-D oraz sprawdza poziom (k+1)-D.
     - Dopóki głębszy poziom przynosi zysk (Δ > 0), schodzi głębiej (1D -> 2D -> 3D -> 4D).
     - Zatrzymuje się w punkcie nasycenia, aplikując optymalny wektor zmian w jednym przebiegu.
  4. Bezpieczeństwo i SSOT:
     - Zapisuje wyjątki 3p bezpośrednio pod kluczami '3p:' w game_config.yaml.
"""
from __future__ import annotations

import argparse
import copy
import os
import shutil
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
)

import audit_level1
import audit_level2
import audit_level4

REPORTS_DIR = Path(__file__).resolve().parent.parent.parent / "playtesting" / "sim-reports"
LOG_FILE_PATH = REPORTS_DIR / "logs" / "audytor_3p_log.md"
BALANCE_NOTES_PATH = Path(__file__).resolve().parent.parent.parent / "playtesting" / "balance-notes.md"

SETUPS_3P = [s for s, pl in SETUP_PRESETS.items() if len(pl) == 3]

FACTION_NAMES = {
    FactionId.SWIETE_OFICJUM: "SO",
    FactionId.CIENIE_AL_ANDALUS: "CAA",
    FactionId.KORONA_BORGIOWIE: "KB",
    FactionId.KABALA_TOLEDO: "KT",
    FactionId.GILDIA_CIENI: "GC",
}


def log_msg(msg: str, echo: bool = True) -> None:
    """Logs message to console and audytor_3p_log.md."""
    if echo:
        print(msg)
    LOG_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}\n")


def evaluate_candidate_3p(
    candidate: tuple[str, str, dict],
    games_per_setup: int = 1000,
    seed: int = 42,
) -> dict:
    """Evaluates candidate mutation across all 10 3P setups."""
    cid, name, params = candidate
    summaries = []
    setup_scores = {}

    for sname in SETUPS_3P:
        s = run_batch(games=games_per_setup, setup=sname, seed=seed, layer="C", win_overrides=params)
        summaries.append(s)
        sc = calculate_setup_score(s)
        setup_scores[sname] = sc

    score_3p = round(sum(setup_scores.values()) / len(setup_scores), 1) if setup_scores else 0.0
    eras_avg = round(sum(s.eras_avg for s in summaries) / len(summaries), 2)
    deadlock_pct = round(sum(s.eras_limit_pct for s in summaries) / len(summaries), 2)
    poverty_pct = round(sum(s.passes_forced_pct for s in summaries) / len(summaries), 2)
    autodafe_avg = round(sum(s.autodafe_avg for s in summaries) / len(summaries), 2)

    return {
        "id": cid,
        "name": name,
        "params": params,
        "score_3p": score_3p,
        "setup_scores": setup_scores,
        "eras_avg": eras_avg,
        "deadlock_pct": deadlock_pct,
        "poverty_pct": poverty_pct,
        "autodafe_avg": autodafe_avg,
    }


def generate_atomic_candidates_3p() -> list[tuple[str, str, dict]]:
    """Builds atomic mutations for 3P format across L1, L2, and L4 (strictly excluding L3 cards)."""
    tests = []

    # L1: System parameters for 3P
    tests.extend([t for t in audit_level1.build_level1_tests() if t[0] != "L1_BAZA" and "HAND_LIMIT" not in t[0]])

    # L2: Faction victory conditions for 3P
    tests.extend([t for t in audit_level2.build_level2_tests() if t[0] != "L2_BAZA"])

    # L4: Niche variants & Edicts
    tests.extend([t for t in audit_level4.build_level4_tests() if t[0] != "L4_BAZA"])

    return tests


def merge_mutations(m1: tuple[str, str, dict], m2: tuple[str, str, dict]) -> tuple[str, str, dict] | None:
    """Merges two non-conflicting mutations."""
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


def run_lookahead_beam_search_3p(
    baseline_score: float,
    workers: int = 10,
    max_depth: int = 5,
) -> dict | None:
    """Adaptive Lookahead +1D Optimizer for 3P."""
    atomic = generate_atomic_candidates_3p()
    log_msg(f"Pula kandydatów atomowych 1D: {len(atomic)} wariantów")

    current_best_candidate = ("BASE_3P", "Baza 3P", {})
    current_best_res = evaluate_candidate_3p(current_best_candidate, games_per_setup=2000)
    current_best_score = current_best_res["score_3p"]
    baseline_score = current_best_score

    log_msg(f"Stan początkowy 3P: {color_score(current_best_score, bold=True)} pkt")

    current_level_candidates = atomic

    for depth in range(1, max_depth + 1):
        log_msg(f"\n{'='*60}\n🔍 BADANIE GŁĘBOKOŚCI {depth}D (Kandydatów do zbadania: {len(current_level_candidates)})\n{'='*60}")
        
        t0 = time.time()
        results = []
        with ProcessPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(evaluate_candidate_3p, c, 500) for c in current_level_candidates]
            for fut in futures:
                results.append(fut.result())

        results.sort(key=lambda x: x["score_3p"], reverse=True)
        top_candidates = results[:min(30, len(results))]
        best_of_depth = top_candidates[0]

        log_msg(f"Najlepszy wstępny na głębokości {depth}D: {best_of_depth['name']} -> {best_of_depth['score_3p']:.1f} pkt (Czas: {time.time()-t0:.1f}s)")

        # Verify TOP 8 on high sample
        verified_top = []
        for cand in top_candidates[:8]:
            c_tuple = (cand["id"], cand["name"], cand["params"])
            ver_res = evaluate_candidate_3p(c_tuple, games_per_setup=2500)
            verified_top.append(ver_res)

        verified_top.sort(key=lambda x: x["score_3p"], reverse=True)
        best_verified = verified_top[0]

        log_msg(f"Zweryfikowany lider {depth}D: {best_verified['name']} -> {color_score(best_verified['score_3p'], bold=True)} pkt")

        improved = False
        if best_verified["score_3p"] > current_best_score + 0.05:
            gain = best_verified["score_3p"] - current_best_score
            log_msg(f"✨ Nowe optimum na głębokości {depth}D: +{gain:.2f} pkt ({current_best_score:.1f} -> {best_verified['score_3p']:.1f} pkt)")
            current_best_score = best_verified["score_3p"]
            current_best_candidate = (best_verified["id"], best_verified["name"], best_verified["params"])
            current_best_res = best_verified
            improved = True

        # Lookahead rule: ALWAYS explore 2D, and for depth >= 2 continue as long as score improved
        if depth == 1 or improved:
            next_level = []
            seen_ids = set()
            expansion_pool = top_candidates[:20] if improved else top_candidates[:25]
            for cand in expansion_pool:
                c_tuple = (cand["id"], cand["name"], cand["params"])
                for atom in atomic:
                    merged = merge_mutations(c_tuple, atom)
                    if merged:
                        norm_id = "__".join(sorted(merged[0].split("__")))
                        if norm_id not in seen_ids:
                            seen_ids.add(norm_id)
                            next_level.append(merged)

            if not next_level:
                log_msg(f"Brak dalszych niekolidujących kombinacji dla poziomu {depth+1}D.")
                break
            log_msg(f"🚀 Przechodzę do lookahead {depth+1}D: wygenerowano {len(next_level)} kombinacji.")
            current_level_candidates = next_level
        else:
            log_msg(f"🛑 Poziom {depth}D nie przyniósł dalszej poprawy ponad dotychczasowe optimum ({current_best_score:.1f} pkt). Zatrzymuję ekspansję.")
            break

    if current_best_score > baseline_score + 0.05:
        return current_best_res
    return None


def apply_and_document_winner_3p(winner: dict) -> None:
    """Applies the winning 3P exception to game_config.yaml under 3p: sections and updates docs."""
    log_msg(f"\n🏆 APLIKOWANIE ZWYCIĘSKIEGO WEKTORA ZMIAN 3P: {winner['name']} ({winner['score_3p']:.1f} pkt)")
    
    with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    # Apply parameter overrides to 3p sections in config
    p = winner["params"]
    
    # 1. SO Stacks
    if "so_stacks_offset" in p:
        cur = cfg.get("victory", {}).get("swiete_oficjum", {}).get("stacks", 5)
        val = (cur.get("3p", cur) if isinstance(cur, dict) else cur) + p["so_stacks_offset"]
        if not isinstance(cfg["victory"]["swiete_oficjum"]["stacks"], dict):
            cfg["victory"]["swiete_oficjum"]["stacks"] = {"3p": val, "4p": cur, "5p": cur}
        else:
            cfg["victory"]["swiete_oficjum"]["stacks"]["3p"] = val

    # 2. KB Era
    if "kb_era_offset" in p:
        cur = cfg.get("victory", {}).get("korona_borgiowie", {}).get("era", 4)
        val = (cur.get("3p", cur) if isinstance(cur, dict) else cur) + p["kb_era_offset"]
        if not isinstance(cfg["victory"]["korona_borgiowie"]["era"], dict):
            cfg["victory"]["korona_borgiowie"]["era"] = {"3p": val, "4p": cur, "5p": cur}
        else:
            cfg["victory"]["korona_borgiowie"]["era"]["3p"] = val

    # 3. KT Era
    if "kt_era_offset" in p:
        cur = cfg.get("victory", {}).get("kabala_toledo", {}).get("era", 6)
        val = (cur.get("3p", cur) if isinstance(cur, dict) else cur) + p["kt_era_offset"]
        if not isinstance(cfg["victory"]["kabala_toledo"]["era"], dict):
            cfg["victory"]["kabala_toledo"]["era"] = {"3p": val, "4p": cur, "5p": cur}
        else:
            cfg["victory"]["kabala_toledo"]["era"]["3p"] = val

    # 4. GC Falls Default
    if "gc_falls_default_offset" in p or "gc_falls_offset" in p:
        off = p.get("gc_falls_default_offset", p.get("gc_falls_offset", 0))
        cur = cfg.get("victory", {}).get("gildia_cieni", {}).get("falls", {}).get("default", 3)
        val = (cur.get("3p", cur) if isinstance(cur, dict) else cur) + off
        if not isinstance(cfg["victory"]["gildia_cieni"]["falls"]["default"], dict):
            cfg["victory"]["gildia_cieni"]["falls"]["default"] = {"3p": val, "4p": cur, "5p": cur}
        else:
            cfg["victory"]["gildia_cieni"]["falls"]["default"]["3p"] = val

    # 5. Start Gold
    if "start_gold_offset" in p:
        cur = cfg.get("system", {}).get("start_gold", 4)
        val = (cur.get("3p", cur) if isinstance(cur, dict) else cur) + p["start_gold_offset"]
        if not isinstance(cfg["system"]["start_gold"], dict):
            cfg["system"]["start_gold"] = {"3p": val, "4p": cur, "5p": cur}
        else:
            cfg["system"]["start_gold"]["3p"] = val

    new_ver = save_config_and_bump_version(cfg)
    log_msg(f"✅ Zapisano wyjątki 3P do game_config.yaml! Nowa wersja: {new_ver}")

    # Synchronize rules
    subprocess.run(["python3", str(TOOLS_SIM_DIR / "sync_config.py")], check=True)
    log_msg("✅ Zsynchronizowano reguły gry i katalog kart (sync_config.py).")


def main() -> None:
    parser = argparse.ArgumentParser(description="Audytor 3P — Adaptive Lookahead Optimizer")
    parser.add_argument("--workers", type=int, default=10, help="Liczba procesów równoległych")
    parser.add_argument("--max-depth", type=int, default=4, help="Maksymalna głębokość przeszukiwania Lookahead")
    args = parser.parse_args()

    log_msg("═══════════════════════════════════════════════════════════")
    log_msg("🚀 START AUDYTOR 3P (ADAPTIVE LOOKAHEAD +1D OPTIMIZER)")
    log_msg("═══════════════════════════════════════════════════════════")

    CONFIG.reload()
    base_res = evaluate_candidate_3p(("BASE", "Baza 3P", {}), games_per_setup=2000)
    log_msg(f"Bieżący wynik 3P: {color_score(base_res['score_3p'], bold=True)} pkt")

    winner = run_lookahead_beam_search_3p(base_res["score_3p"], workers=args.workers, max_depth=args.max_depth)
    if winner:
        apply_and_document_winner_3p(winner)
    else:
        log_msg("🏁 Brak zmian przynoszących zysk w 3P. Bieżący stan jest optymalny.")


if __name__ == "__main__":
    main()
