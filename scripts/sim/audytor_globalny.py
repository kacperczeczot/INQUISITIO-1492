#!/usr/bin/env python3
"""INQUISITIO-1492 — GRAND COMBO AUDITOR (Global Greedy Optimizer)."""

import argparse
import copy
import sys
import time
from pathlib import Path
from typing import Any

# Ścieżki
TOOLS_SRC_DIR = Path(__file__).resolve().parent
SRC_DIR = TOOLS_SRC_DIR.parent.parent / "src"
for p in (TOOLS_SRC_DIR, SRC_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

import yaml
from inquisitio.config import _CONFIG_PATH
from inquisitio.engine.setup import SETUP_PRESETS
from inquisitio.runner.adaptive_racer import AdaptiveSequentialRacer, merge_mutations
from inquisitio.runner.canon_accept import accept_global_candidate

import audit_level1
import audit_level2
import audit_level3

def generate_global_pool():
    pool = []
    def _add_split(tests):
        for tid, tname, tdict in tests:
            if tid.endswith("BAZA") or not tdict: continue
            pool.append((tid, tname, tdict))
            
    # L1 & L2 rules for 3P, 4P, 5P
    _add_split(audit_level1.build_level1_tests())
    _add_split(audit_level2.build_level2_tests())
    
    # L3 cards (global)
    for tid, tname, tdict in audit_level3.build_level3_tests(param_filter="cost,heresy"):
        if tid.endswith("BAZA") or not tdict: continue
        pool.append((tid, f"[L3] {tname}", tdict))
    return pool

def main():
    print("═══════════════════════════════════════════════════════════════════════")
    print("   INQUISITIO-1492 — GRAND COMBO AUDITOR (Global Greedy Optimizer)    ")
    print("═══════════════════════════════════════════════════════════════════════")
    
    atomic_pool = generate_global_pool()
    setups_to_run = list(SETUP_PRESETS.keys())
    
    racer = AdaptiveSequentialRacer(
        setups=setups_to_run,
        batch_step=400,
        min_games=400,
        max_games=6400,
        epsilon_indiff=0.15,
        workers=10,
        min_delta=0.2,
    )
    
    base_cand = ("BAZA", "Konfiguracja Startowa", {})
    cached_base_stats = None
    iteration = 1
    
    while True:
        print(f"\n🌀 --- ITERACJA #{iteration} ---")
        print(f"🏁 [START] Pula: {len(atomic_pool)} atomów (na bazie {base_cand[0]})")
        
        # Apply the accumulated base mutations to all atomic candidates
        delta_pool = []
        effective_candidates = []
        for tid, tname, tdict in atomic_pool:
            merged = merge_mutations(base_cand, (tid, tname, tdict))
            if merged:
                effective_candidates.append(merged)
                delta_pool.append((tid, tname, tdict))
                
        if not effective_candidates:
            print("🛑 Brak prawidłowych mutacji do nałożenia.")
            break
            
        base_stats, ranked_stats = racer.run_race(
            base_cand=base_cand,
            candidate_pool=effective_candidates,
            seed=42 + iteration,
            delta_pool=delta_pool,
            label_prefix=f"ITERACJA {iteration}",
            base_stats_cache=cached_base_stats,
        )
        cached_base_stats = base_stats
        
        base_dict = base_stats.to_result_dict()
        print(f"\n   Baza Global Score: {base_dict['score_global']:.2f} | 4P: {base_dict['score_4p']:.2f}")
        
        surviving = [c for c in ranked_stats if not c.is_pruned]
        if not surviving:
            print("\n🛑 LOKALNE OPTIMUM OSIĄGNIĘTE. Brak zyskownych atomów.")
            break
            
        # Sort by global score
        surviving.sort(key=lambda c: c.to_result_dict()['score_global'], reverse=True)
        best = surviving[0]
        cand_dict = best.to_result_dict()
        
        decision = accept_global_candidate(base_dict, cand_dict)
        print(f"\n🏆 Najlepszy z puli: {best.name}")
        print(f"   Decyzja: {decision.accepted} - {decision.reason}")
        
        if decision.accepted:
            print(f"✅ ZNALEZIONO POPRAWKĘ! Aktualizuję bazę i idę dalej (Kombos stacking)!")
            # Update base cand with the new best candidate
            base_cand = (best.cand_tuple[0], best.cand_tuple[1], best.cand_tuple[2])
            cached_base_stats = best
            iteration += 1
        else:
            print("\n🛑 Brak akceptowalnego kandydata. Koniec optymalizacji.")
            break

if __name__ == "__main__":
    main()
