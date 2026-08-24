#!/usr/bin/env python3
"""One-shot baseline: 16 setups × N games, print category + global scores."""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

SIM_DIR = Path(__file__).resolve().parent.parent.parent / "sim"
sys.path.insert(0, str(SIM_DIR))

from inquisitio.engine.setup import SETUP_PRESETS
from inquisitio.runner.batch import run_batch
from inquisitio.runner.scoring import (
    calculate_category_scores,
    calculate_global_score,
    calculate_setup_score,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--games", type=int, default=5000, help="Number of games per setup (ADR-0014: >= 5000)")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    t0 = time.time()
    summaries = []
    for sname in sorted(SETUP_PRESETS):
        t = time.time()
        summary = run_batch(games=args.games, setup=sname, seed=args.seed, layer="C")
        summaries.append(summary)
        print(
            f"  {sname:32s} score={calculate_setup_score(summary):5.1f}  "
            f"eras={summary.eras_avg:.2f}  dead={summary.eras_limit_pct * 100:.1f}%  "
            f"({time.time() - t:.1f}s)",
            flush=True,
        )

    cats = calculate_category_scores(summaries)
    glob = calculate_global_score(cats)
    print()
    print(
        f"GLOBAL {glob:.1f} | 3p {cats['3p']:.1f} | 4p {cats['4p']:.1f} | "
        f"5p {cats['5p']:.1f} | {time.time() - t0:.1f}s"
    )


if __name__ == "__main__":
    main()
