#!/usr/bin/env python3
"""Calibrate PoliticsAgent utility weights for optimal 4P balance."""

import sys, time
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
TOOLS_DIR = Path(__file__).resolve().parent
for p in (str(SRC_DIR), str(TOOLS_DIR)):
    if p not in sys.path:
        sys.path.insert(0, p)

from inquisitio.runner.batch import run_batch
from inquisitio.runner.scoring import calculate_balance_score
from inquisitio.runner.balance import faction_shares

CANON_4P = ['4p-core', '4p-no-cienie', '4p-no-kabala', '4p-no-korona', '4p-no-oficjum']
GAMES = 3000
SEEDS = [42, 10041]

def evaluate_current():
    seed_scores = []
    setup_details = {}
    for seed in SEEDS:
        total = 0
        setup_details[seed] = {}
        for setup in CANON_4P:
            s = run_batch(games=GAMES, setup=setup, seed=seed)
            sc = calculate_balance_score(s)
            sh = faction_shares(s)
            setup_details[seed][setup] = (sc, sh)
            total += sc
        seed_scores.append(total / len(CANON_4P))
    
    cross_avg = sum(seed_scores) / len(seed_scores)
    min_score = min(setup_details[s][setup][0] for s in SEEDS for setup in CANON_4P)
    
    print(f"\n{'='*70}")
    print(f"📊 ŚREDNIA CROSS-SEED: {cross_avg:.2f} pkt | MIN SETUP: {min_score:.2f} pkt")
    print(f"{'='*70}")
    for setup in CANON_4P:
        s42 = setup_details[42][setup]
        s10 = setup_details[10041][setup]
        avg_s = (s42[0] + s10[0]) / 2
        sh_str = " | ".join(f"{k.split('-')[0][:3].upper()}: {s42[1].get(k, 0)*100:.1f}%" for k in sorted(s42[1].keys()))
        status = "🟢" if avg_s >= 85 else ("🟡" if avg_s >= 75 else "🔴")
        print(f"  {status} {setup:<18} avg={avg_s:5.1f} (s42={s42[0]:4.1f}, s10={s10[0]:4.1f}) | {sh_str}")
    return cross_avg, min_score

if __name__ == "__main__":
    evaluate_current()
