#!/usr/bin/env python3
"""Compare audytor_kanonu accept-mode=legacy vs band on one shared 4P funnel (dry, no SSOT writes)."""
from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path
from types import SimpleNamespace

TOOLS_SIM_DIR = Path(__file__).resolve().parent
SIM_DIR = TOOLS_SIM_DIR.parent.parent / "sim"
for p in (TOOLS_SIM_DIR, SIM_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from inquisitio.config import CONFIG
from inquisitio.runner.canon_accept import (
    TARGET_BAND_PCT,
    accept_candidate,
    setup_shares_in_range,
)

import audytor_kanonu as kanon


def _ns(**kwargs):
    defaults = dict(
        hours=None,
        max_iters=1,
        fast_games=200,
        screen_games=1000,
        confirm_games=3000,
        top_semifinalists=48,
        top_k=24,
        beam_width=8,
        min_delta=0.05,
        workers=min(os.cpu_count() or 4, 10),
        seed=42,
        dry_run=True,
        accept_mode="legacy",
    )
    defaults.update(kwargs)
    return SimpleNamespace(**defaults)


def _tasks(cands: list[tuple[str, str, dict]], games: int, seed: int, setups: list[str]):
    return [((c[0], c[1], c[2]), games, seed, setups) for c in cands]


def _print_baseline(base: dict, in_band: bool) -> None:
    print(f"\n=== BAZA {CONFIG.version} ===")
    print(
        f"legacy score_4p={base['score_4p']:.1f}  balance={base['score_4p_balance']:.1f}  "
        f"min={base['min_balance']:.1f} ({base['min_balance_setup']})  "
        f"vitality={base['vitality_penalty']:.3f}  in_band_20_30={in_band}"
    )
    print(
        f"eras={base['eras_avg']:.2f}  deadlock={base['deadlock_pct']:.1f}%  "
        f"poverty={base['poverty_pct']:.1f}%  acc={base['acc_avg']:.2f}"
    )
    for sname, sc in sorted(base["setup_scores_balance"].items()):
        shares = base["setup_shares"].get(sname, {})
        share_s = " ".join(f"{k}={v:.1f}%" for k, v in shares.items())
        print(f"  {sname:16s} balance={sc:5.1f}  {share_s}")


def _run_mode(auditor, cand_dict, stage1, base, mode: str, args) -> dict:
    auditor.args.accept_mode = mode
    auditor._base_in_band = setup_shares_in_range(base.get("setup_shares") or {}, *TARGET_BAND_PCT)
    setups = kanon.CANONICAL_4P_SETUPS

    s1 = sorted(stage1, key=auditor._rank)
    semi_ids = [r["id"] for r in s1[: args.top_semifinalists]]
    semi_cands = [cand_dict[i] for i in semi_ids if i in cand_dict]
    print(f"\n--- {mode}: etap 2 ({args.screen_games} gier/setup) TOP {len(semi_cands)} ---")
    stage2 = auditor._execute_pool(
        kanon._run_single_test_task_4p,
        _tasks(semi_cands, args.screen_games, args.seed, setups),
        label=f"{mode} 2/3",
    )
    s2 = sorted(stage2, key=auditor._rank)
    fin_ids = [r["id"] for r in s2[: args.top_k]]
    fin_cands = [cand_dict[i] for i in fin_ids if i in cand_dict]
    print(f"--- {mode}: etap 3 ({args.confirm_games} gier/setup) TOP {len(fin_cands)} ---")
    stage3 = auditor._execute_pool(
        kanon._run_single_test_task_4p,
        _tasks(fin_cands, args.confirm_games, args.seed, setups),
        label=f"{mode} 3/3",
    )
    s3 = sorted(stage3, key=auditor._rank)

    print(f"\n[{mode}] finaliści")
    picked = None
    for i, r in enumerate(s3, 1):
        d = accept_candidate(base, r, mode=mode, min_delta=args.min_delta)
        mark = "✔" if d.accepted else "✖"
        print(
            f"  #{i:2d} {mark} {r['id'][:48]:48s}  "
            f"Δleg {r['score_4p']-base['score_4p']:+.2f}  "
            f"min {r['min_balance']:.1f}  vit {r['vitality_penalty']:.3f}  | {d.reason}"
        )
        if picked is None and d.accepted:
            picked = (r, d)
    return {"mode": mode, "picked": picked, "finalists": s3, "in_band": auditor._base_in_band}


def main() -> None:
    parser = argparse.ArgumentParser(description="Porównanie legacy vs band (dry-run, bez zapisu SSOT)")
    parser.add_argument("--fast-games", type=int, default=200)
    parser.add_argument("--screen-games", type=int, default=1000)
    parser.add_argument("--confirm-games", type=int, default=3000)
    parser.add_argument("--top-semifinalists", type=int, default=48)
    parser.add_argument("--top-k", type=int, default=24)
    parser.add_argument("--workers", type=int, default=min(os.cpu_count() or 4, 10))
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--min-delta", type=float, default=0.05)
    args = parser.parse_args()

    t0 = time.time()
    ns = _ns(
        fast_games=max(args.fast_games, 100),
        screen_games=max(args.screen_games, 500),
        confirm_games=max(args.confirm_games, 3000),
        top_semifinalists=args.top_semifinalists,
        top_k=args.top_k,
        workers=args.workers,
        seed=args.seed,
        min_delta=args.min_delta,
    )
    auditor = kanon.Canon4PAutoBalancer(ns)
    setups = kanon.CANONICAL_4P_SETUPS

    print(f"Wersja SSOT: {CONFIG.version}  workers={ns.workers}")
    print("🔍 baza (confirm)...")
    base = auditor._execute_pool(
        kanon._run_single_test_task_4p,
        [(("BASE", "Baza 4P", {}), ns.confirm_games, ns.seed, setups)],
        label="Baza",
    )[0]
    in_band = setup_shares_in_range(base.get("setup_shares") or {}, *TARGET_BAND_PCT)
    auditor._base_in_band = in_band
    _print_baseline(base, in_band)

    pool = kanon.generate_all_atomic_candidates()
    cand_dict = {c[0]: c for c in pool}
    print(f"\n🧬 pula atomowa: {len(pool)}  etap 1 @ {ns.fast_games} gier/setup")
    stage1 = auditor._execute_pool(
        kanon._run_single_test_task_4p,
        _tasks(pool, ns.fast_games, ns.seed, setups),
        label="Etap 1 wspólny",
    )

    results = []
    for mode in ("legacy", "band"):
        results.append(_run_mode(auditor, cand_dict, stage1, base, mode, ns))

    print("\n=== WERDYKT ===")
    for row in results:
        picked = row["picked"]
        if not picked:
            print(f"  {row['mode']}: BRAK patcha")
            continue
        r, d = picked
        print(
            f"  {row['mode']}: {r['id']}  ({d.phase}) {d.reason}  "
            f"legacy {base['score_4p']:.1f}→{r['score_4p']:.1f}  "
            f"min {base['min_balance']:.1f}→{r['min_balance']:.1f}"
        )

    ids = [(row["picked"][0]["id"] if row["picked"] else None) for row in results]
    if ids[0] == ids[1]:
        print("  zgoda: oba tryby biorą ten sam kandydat")
    elif ids[0] and ids[1]:
        print("  rozjazd: legacy i band biorą różnych kandydatów")
    print(f"\nczas {round(time.time() - t0, 1)}s")


if __name__ == "__main__":
    main()
