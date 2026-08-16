#!/usr/bin/env python3
"""INQUISITIO-1492 — AUDYTOR 4P MAKRO (4-Player Adaptive Lookahead Optimizer without Cards).

Autonomiczny optymalizator balansu dedykowany dla 5 setupów Kanonu 4-osobowego (4P),
skupiony wyłącznie na parametrach systemowych i celach frakcji (L1, L2, L4),
całkowicie pomijający talię kart (L3).

Zasady działania:
  1. Działa na 5 setupach Kanonu 4P:
     - 4p-core
     - 4p-no-cienie
     - 4p-no-kabala
     - 4p-no-korona
     - 4p-no-oficjum
  2. Optymalizuje parametry makro (L1, L2, L4):
     - L1: start_gold, accusation_threshold (4p), max_eras, hand_limit, autodafe_cooldown
     - L2: warunki zwycięstwa frakcji (so_stacks, so_condemns, caa_relics, caa_era, kb_decrees, kb_era, kt_frags, kt_era, gc_falls itp.)
     - L4: szlak morski (sea_route_era), ruch patrolu inkwizytora
  3. Adaptacyjny Algorytm Wybiegający w Przód (Adaptive Lookahead +1D):
     - Bada przestrzeń wielowymiarową (1D -> 2D -> 3D -> 4D).
     - Dopóki (k+1)D przynosi zysk (Δ > 0.1 pkt), schodzi głębiej, gromadząc sprzężenia wieloparametrowe.
     - Zatrzymuje się w punkcie nasycenia, aplikując optymalny wielowymiarowy wektor zmian w jednym przebiegu.
  4. Zapis do SSOT:
     - Zapisuje globalne parametry bazowe bezpośrednio do game_config.yaml i synchronizuje reguły.
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
LOG_FILE_PATH = REPORTS_DIR / "logs" / "audytor_4p_log.md"
BALANCE_NOTES_PATH = Path(__file__).resolve().parent.parent.parent / "playtesting" / "balance-notes.md"

SETUPS_4P = [
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


def log_msg(msg: str, echo: bool = True) -> None:
    """Logs message to console and audytor_4p_log.md."""
    if echo:
        print(msg)
    LOG_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}\n")


def evaluate_candidate_4p(
    candidate: tuple[str, str, dict],
    games_per_setup: int = 1000,
    seed: int = 42,
) -> dict:
    """Evaluates candidate mutation across all 5 Canonical 4P setups."""
    cid, name, params = candidate
    summaries = []
    setup_scores = {}

    for sname in SETUPS_4P:
        s = run_batch(games=games_per_setup, setup=sname, seed=seed, layer="C", win_overrides=params)
        summaries.append(s)
        sc = calculate_setup_score(s)
        setup_scores[sname] = sc

    score_4p = round(sum(setup_scores.values()) / len(setup_scores), 1) if setup_scores else 0.0
    eras_avg = round(sum(s.eras_avg for s in summaries) / len(summaries), 2)
    deadlock_pct = round(sum(s.eras_limit_pct for s in summaries) / len(summaries), 2)
    poverty_pct = round(sum(s.passes_forced_pct for s in summaries) / len(summaries), 2)
    autodafe_avg = round(sum(s.autodafe_avg for s in summaries) / len(summaries), 2)

    return {
        "id": cid,
        "name": name,
        "params": params,
        "score_4p": score_4p,
        "setup_scores": setup_scores,
        "eras_avg": eras_avg,
        "deadlock_pct": deadlock_pct,
        "poverty_pct": poverty_pct,
        "autodafe_avg": autodafe_avg,
    }


def generate_atomic_candidates_4p() -> list[tuple[str, str, dict]]:
    """Builds atomic mutations for 4P format across L1, L2, and L4 (strictly excluding L3 cards)."""
    tests = []

    # L1: System parameters
    tests.extend([t for t in audit_level1.build_level1_tests() if t[0] != "L1_BAZA"])

    # L2: Faction victory conditions
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


def run_lookahead_beam_search_4p(
    baseline_score: float,
    workers: int = 10,
    max_depth: int = 5,
) -> dict | None:
    """Adaptive Lookahead +1D Optimizer for 4P."""
    atomic = generate_atomic_candidates_4p()
    log_msg(f"Pula kandydatów atomowych 1D: {len(atomic)} wariantów")

    current_best_candidate = ("BASE_4P", "Baza 4P", {})
    current_best_res = evaluate_candidate_4p(current_best_candidate, games_per_setup=2500)
    current_best_score = current_best_res["score_4p"]
    baseline_score = current_best_score

    log_msg(f"Stan początkowy Kanonu 4P: {color_score(current_best_score, bold=True)} pkt")

    current_level_candidates = atomic

    for depth in range(1, max_depth + 1):
        log_msg(f"\n{'='*60}\n🔍 BADANIE GŁĘBOKOŚCI {depth}D (Kandydatów do zbadania: {len(current_level_candidates)})\n{'='*60}")
        
        t0 = time.time()
        results = []
        with ProcessPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(evaluate_candidate_4p, c, 600) for c in current_level_candidates]
            for fut in futures:
                results.append(fut.result())

        results.sort(key=lambda x: x["score_4p"], reverse=True)
        top_candidates = results[:min(30, len(results))]
        best_of_depth = top_candidates[0]

        log_msg(f"Najlepszy wstępny na głębokości {depth}D: {best_of_depth['name']} -> {best_of_depth['score_4p']:.1f} pkt (Czas: {time.time()-t0:.1f}s)")

        # Verify TOP 8 on high sample (3000 games)
        verified_top = []
        for cand in top_candidates[:8]:
            c_tuple = (cand["id"], cand["name"], cand["params"])
            ver_res = evaluate_candidate_4p(c_tuple, games_per_setup=3000)
            verified_top.append(ver_res)

        verified_top.sort(key=lambda x: x["score_4p"], reverse=True)
        best_verified = verified_top[0]

        log_msg(f"Zweryfikowany lider {depth}D: {best_verified['name']} -> {color_score(best_verified['score_4p'], bold=True)} pkt")

        improved = False
        if best_verified["score_4p"] > current_best_score + 0.05:
            gain = best_verified["score_4p"] - current_best_score
            log_msg(f"✨ Nowe optimum na głębokości {depth}D: +{gain:.2f} pkt ({current_best_score:.1f} -> {best_verified['score_4p']:.1f} pkt)")
            current_best_score = best_verified["score_4p"]
            current_best_candidate = (best_verified["id"], best_verified["name"], best_verified["params"])
            current_best_res = best_verified
            improved = True

        # Lookahead rule: ALWAYS explore 2D (depth 1 -> 2), and for depth >= 2 continue as long as score improved
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


def apply_and_document_winner_4p(winner: dict) -> None:
    """Applies the winning 4P mutation to game_config.yaml as global base and updates docs."""
    log_msg(f"\n🏆 APLIKOWANIE ZWYCIĘSKIEGO WEKTORA ZMIAN 4P: {winner['name']} ({winner['score_4p']:.1f} pkt)")
    
    with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    p = winner["params"]

    # 1. SO Stacks
    if "so_stacks_offset" in p:
        cur = cfg.get("victory", {}).get("swiete_oficjum", {}).get("stacks", 5)
        val = (cur.get("4p", 5) if isinstance(cur, dict) else cur) + p["so_stacks_offset"]
        cfg["victory"]["swiete_oficjum"]["stacks"] = val

    # 2. SO Condemns
    if "so_condemns_offset" in p:
        cur = cfg.get("victory", {}).get("swiete_oficjum", {}).get("condemns", 2)
        val = (cur.get("4p", 2) if isinstance(cur, dict) else cur) + p["so_condemns_offset"]
        cfg["victory"]["swiete_oficjum"]["condemns"] = val

    # 3. KB Era
    if "kb_era_offset" in p:
        cur = cfg.get("victory", {}).get("korona_borgiowie", {}).get("era", 4)
        val = (cur.get("4p", 4) if isinstance(cur, dict) else cur) + p["kb_era_offset"]
        cfg["victory"]["korona_borgiowie"]["era"] = val

    # 4. KT Era
    if "kt_era_offset" in p:
        cur = cfg.get("victory", {}).get("kabala_toledo", {}).get("era", 6)
        val = (cur.get("4p", 6) if isinstance(cur, dict) else cur) + p["kt_era_offset"]
        cfg["victory"]["kabala_toledo"]["era"] = val

    # 5. GC Falls Default
    if "gc_falls_default_offset" in p or "gc_falls_offset" in p:
        off = p.get("gc_falls_default_offset", p.get("gc_falls_offset", 0))
        cur = cfg.get("victory", {}).get("gildia_cieni", {}).get("falls", {}).get("default", 3)
        val = (cur.get("4p", 3) if isinstance(cur, dict) else cur) + off
        cfg["victory"]["gildia_cieni"]["falls"]["default"] = val

    # 6. GC Falls No SO
    if "gc_falls_no_so_offset" in p:
        cur = cfg.get("victory", {}).get("gildia_cieni", {}).get("falls", {}).get("no_oficjum", 4)
        val = (cur.get("4p", 4) if isinstance(cur, dict) else cur) + p["gc_falls_no_so_offset"]
        cfg["victory"]["gildia_cieni"]["falls"]["no_oficjum"] = val

    # 7. Start Gold
    if "start_gold_offset" in p:
        cur = cfg.get("system", {}).get("start_gold", 4)
        val = (cur.get("4p", 4) if isinstance(cur, dict) else cur) + p["start_gold_offset"]
        cfg["system"]["start_gold"] = val

    # 8. Max Eras
    if "max_eras_offset" in p:
        cur = cfg.get("system", {}).get("max_eras", 11)
        cfg["system"]["max_eras"] = cur + p["max_eras_offset"]

    # 9. Hand Limit
    if "hand_limit_offset" in p:
        cur = cfg.get("system", {}).get("hand_limit", 5)
        cfg["system"]["hand_limit"] = cur + p["hand_limit_offset"]

    new_ver = save_config_and_bump_version(cfg)
    log_msg(f"✅ Zapisano globalne zmiany 4P do game_config.yaml! Nowa wersja: {new_ver}")

    # Synchronize rules
    subprocess.run(["python3", str(TOOLS_SIM_DIR / "sync_config.py")], check=True)
    log_msg("✅ Zsynchronizowano reguły gry i katalog kart (sync_config.py).")


def main() -> None:
    parser = argparse.ArgumentParser(description="Audytor 4P Makro — Adaptive Lookahead Optimizer (without cards)")
    parser.add_argument("--workers", type=int, default=10, help="Liczba procesów równoległych")
    parser.add_argument("--max-depth", type=int, default=4, help="Maksymalna głębokość przeszukiwania Lookahead")
    args = parser.parse_args()

    log_msg("═══════════════════════════════════════════════════════════")
    log_msg("🚀 START AUDYTOR 4P MAKRO (ADAPTIVE LOOKAHEAD +1D)")
    log_msg("═══════════════════════════════════════════════════════════")

    CONFIG.reload()
    base_res = evaluate_candidate_4p(("BASE", "Baza 4P", {}), games_per_setup=2000)
    log_msg(f"Bieżący wynik Kanonu 4P: {color_score(base_res['score_4p'], bold=True)} pkt")

    winner = run_lookahead_beam_search_4p(base_res["score_4p"], workers=args.workers, max_depth=args.max_depth)
    if winner:
        apply_and_document_winner_4p(winner)
    else:
        log_msg("🏁 Brak zmian makro przynoszących zysk w 4P. Bieżący stan jest optymalny.")


if __name__ == "__main__":
    main()
