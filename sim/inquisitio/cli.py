from __future__ import annotations

import argparse
import sys

from inquisitio.engine.setup import SETUP_PRESETS
from inquisitio.runner.balance import faction_shares, run_matrix
from inquisitio.runner.batch import compare_thresholds, run_batch
from inquisitio.runner.feel import render_feel, run_feel
from inquisitio.runner.report import write_compare_report, write_report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="inquisitio", description="INQUISITIO 1492 intrigue simulation")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_run = sub.add_parser("run", help="Run a batch of games (drama metrics)")
    p_run.add_argument("--games", type=int, default=100)
    p_run.add_argument("--players", type=int, default=None, choices=[3, 4, 5])
    p_run.add_argument("--setup", type=str, default=None, choices=sorted(SETUP_PRESETS.keys()))
    p_run.add_argument("--threshold", type=int, default=7)
    p_run.add_argument("--seed", type=int, default=42)
    p_run.add_argument("--layer", type=str, default="C", choices=["A", "B", "C"])

    p_cmp = sub.add_parser("compare", help="Compare accusation thresholds (drama experiment)")
    p_cmp.add_argument("--games", type=int, default=100)
    p_cmp.add_argument("--thresholds", type=str, default="7,8")
    p_cmp.add_argument("--setup", type=str, default="3p-oficjum-alandalus-korona")
    p_cmp.add_argument("--seed", type=int, default=42)
    p_cmp.add_argument("--layer", type=str, default="C", choices=["A", "B", "C"])

    p_feel = sub.add_parser("feel", help="Solo Dev-Play: narrative log of one game")
    p_feel.add_argument(
        "--setup",
        type=str,
        default="3p-oficjum-alandalus-korona",
        choices=sorted(SETUP_PRESETS.keys()),
    )
    p_feel.add_argument("--seed", type=int, default=42)
    p_feel.add_argument("--layer", type=str, default="A", choices=["A", "B", "C"])
    p_feel.add_argument("--threshold", type=int, default=7)
    p_feel.add_argument("--max-eras", type=int, default=None)

    p_mtx = sub.add_parser("matrix", help="Balance matrix: all setups × layers")
    p_mtx.add_argument("--games", type=int, default=80)
    p_mtx.add_argument("--seed", type=int, default=42)
    p_mtx.add_argument("--layers", type=str, default="B,C", help="Comma list A,B,C")
    p_mtx.add_argument("--setup", type=str, default=None, help="Single setup (default: all)")
    p_mtx.add_argument("--threshold", type=int, default=7)

    sub.add_parser("setups", help="List setup presets (3–5p)")

    args = parser.parse_args(argv)

    if args.cmd == "setups":
        for name, factions in SETUP_PRESETS.items():
            print(f"{name}: {', '.join(f.value for f in factions)}")
        return 0

    if args.cmd == "feel":
        result = run_feel(
            setup=args.setup,
            seed=args.seed,
            layer=args.layer,
            threshold=args.threshold,
            max_eras=args.max_eras,
        )
        print(render_feel(result), end="")
        return 0

    if args.cmd == "run":
        summary = run_batch(
            games=args.games,
            threshold=args.threshold,
            players=args.players,
            setup=args.setup,
            seed=args.seed,
            layer=args.layer,
        )
        jp, mp = write_report(summary)
        print(f"Wrote {jp}")
        print(f"Wrote {mp}")
        print(f"Wins (info): {summary.wins}")
        print(
            f"Drama: autodafe={summary.autodafe_avg:.2f} "
            f"acc={summary.accusations_avg:.2f} hooks={summary.hooks_avg:.2f} "
            f"doubles={summary.doubles_avg:.2f} deadlocks={summary.deadlocks_avg:.2f}"
        )
        return 0

    if args.cmd == "compare":
        th = [int(x.strip()) for x in args.thresholds.split(",") if x.strip()]
        results = compare_thresholds(
            games=args.games, thresholds=th, setup=args.setup, seed=args.seed, layer=args.layer
        )
        jp, mp = write_compare_report(results)
        print(f"Wrote {jp}")
        print(f"Wrote {mp}")
        for k, s in results.items():
            print(
                f"t={k} accusations/game={s.accusations_avg:.2f} "
                f"deadlocks={s.deadlocks_avg:.2f} wins={s.wins}"
            )
        return 0

    if args.cmd == "matrix":
        layers = tuple(x.strip() for x in args.layers.split(",") if x.strip())
        setups = [args.setup] if args.setup else None
        rows = run_matrix(
            games=args.games,
            seed=args.seed,
            layers=layers,
            setups=setups,
            threshold=args.threshold,
        )
        failed = 0
        for summary, ok, errors in rows:
            shares = faction_shares(summary)
            mark = "OK" if ok else "FAIL"
            share_s = " ".join(f"{k}:{v:.0%}" for k, v in shares.items())
            print(
                f"[{mark}] {summary.setup} L{summary.layer} "
                f"dead={summary.deadlocks_avg:.2f} acc={summary.accusations_avg:.2f} | {share_s}"
            )
            if not ok:
                failed += 1
                for e in errors:
                    print(f"       ! {e}")
        print(f"\n{len(rows) - failed}/{len(rows)} passed")
        return 1 if failed else 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
