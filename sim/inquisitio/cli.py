from __future__ import annotations

import argparse
import sys

from inquisitio.engine.setup import SETUP_PRESETS
from inquisitio.runner.batch import compare_thresholds, run_batch
from inquisitio.runner.report import write_compare_report, write_report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="inquisitio", description="INQUISITIO 1492 simulation engine")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_run = sub.add_parser("run", help="Run a batch of games")
    p_run.add_argument("--games", type=int, default=100)
    p_run.add_argument("--players", type=int, default=None)
    p_run.add_argument("--setup", type=str, default=None, choices=sorted(SETUP_PRESETS.keys()))
    p_run.add_argument("--threshold", type=int, default=7)
    p_run.add_argument("--seed", type=int, default=42)

    p_cmp = sub.add_parser("compare", help="Compare accusation thresholds")
    p_cmp.add_argument("--games", type=int, default=100)
    p_cmp.add_argument("--thresholds", type=str, default="7,8")
    p_cmp.add_argument("--setup", type=str, default="3p-oficjum-alandalus-korona")
    p_cmp.add_argument("--seed", type=int, default=42)

    p_list = sub.add_parser("setups", help="List setup presets")

    args = parser.parse_args(argv)

    if args.cmd == "setups":
        for name, factions in SETUP_PRESETS.items():
            print(f"{name}: {', '.join(f.value for f in factions)}")
        return 0

    if args.cmd == "run":
        summary = run_batch(
            games=args.games,
            threshold=args.threshold,
            players=args.players,
            setup=args.setup,
            seed=args.seed,
        )
        jp, mp = write_report(summary)
        print(f"Wrote {jp}")
        print(f"Wrote {mp}")
        print(f"Wins: {summary.wins}")
        return 0

    if args.cmd == "compare":
        th = [int(x.strip()) for x in args.thresholds.split(",") if x.strip()]
        results = compare_thresholds(games=args.games, thresholds=th, setup=args.setup, seed=args.seed)
        jp, mp = write_compare_report(results)
        print(f"Wrote {jp}")
        print(f"Wrote {mp}")
        for k, s in results.items():
            print(f"t={k} wins={s.wins} accusations/game={s.accusations:.2f}")
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
