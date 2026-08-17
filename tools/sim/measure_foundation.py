#!/usr/bin/env python3
"""Szybki pomiar bazy 4P: HUD, udziały, czy przechodzi bramkę fundamentu 15–35%."""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from types import SimpleNamespace

TOOLS_SIM_DIR = Path(__file__).resolve().parent
SIM_DIR = TOOLS_SIM_DIR.parent.parent / "sim"
for p in (TOOLS_SIM_DIR, SIM_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

import audytor_kanonu as k
from inquisitio.config import CONFIG
from inquisitio.runner.canon_accept import (
    RED_LINE_PCT,
    TARGET_BAND_PCT,
    setup_shares_in_range,
    table_has_share_foundation,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--games", type=int, default=3000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--workers", type=int, default=min(os.cpu_count() or 4, 10))
    args = parser.parse_args()
    games = max(args.games, 500)

    auditor = k.Canon4PAutoBalancer(
        SimpleNamespace(
            hours=None,
            max_iters=0,
            fast_games=200,
            screen_games=1000,
            confirm_games=games,
            top_semifinalists=48,
            top_k=24,
            beam_width=8,
            min_delta=0.05,
            workers=args.workers,
            seed=args.seed,
            dry_run=True,
            accept_mode="band",
        )
    )
    setups = k.CANONICAL_4P_SETUPS
    base = auditor._execute_pool(
        k._run_single_test_task_4p,
        [(("BASE", "Baza", {}), games, args.seed, setups)],
        label="Baza",
    )[0]

    fund = table_has_share_foundation(base)
    band = setup_shares_in_range(base.get("setup_shares") or {}, *TARGET_BAND_PCT)
    print(f"VERSION={CONFIG.version}")
    print(f"SCORE_4P={base['score_4p']:.1f} MIN={base['min_balance']:.1f} ({base['min_balance_setup']})")
    print(f"FOUNDATION={fund} BAND_20_30={band} VIT={base['vitality_penalty']:.3f}")
    print(f"ER={base['eras_avg']:.2f} DL={base['deadlock_pct']:.1f}%")
    lo, hi = RED_LINE_PCT
    for sname in sorted(base["setup_shares"]):
        sh = base["setup_shares"][sname]
        parts = " ".join(f"{fk}={fv:.1f}%" for fk, fv in sorted(sh.items()))
        out = [f for f, v in sh.items() if v < lo or v > hi]
        flag = f" OUT:{','.join(out)}" if out else ""
        print(f"  {sname}: bal={base['setup_scores_balance'].get(sname, 0):.1f} {parts}{flag}")


if __name__ == "__main__":
    main()
