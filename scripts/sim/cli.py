#!/usr/bin/env python3
"""INQUISITIO-1492 — Zunifikowane Narzędzie Balansu i Symulacji (CLI).

Komendy:
  1. audit:    python tools/sim/cli.py audit [--setup canon-4p|4p-core|all] [--games 2000] [--layer C]
  2. solve:    python tools/sim/cli.py solve [--games 1500] [--workers 10]
  3. test:     python tools/sim/cli.py test --override "so-02:target_heresy=0,caa-06:gold=1" [--games 2000]
  4. baseline: python tools/sim/cli.py baseline [--games 5000]
"""

import argparse
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, List

TOOLS_SIM_DIR = Path(__file__).resolve().parent
SIM_DIR = TOOLS_SIM_DIR.parent.parent / "sim"

for p in (TOOLS_SIM_DIR, SIM_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from inquisitio.runner.batch import run_batch
from inquisitio.runner.scoring import calculate_balance_score
from inquisitio.runner.balance import faction_shares

CANON_4P = ['4p-core', '4p-no-cienie', '4p-no-kabala', '4p-no-korona', '4p-no-oficjum']
SETUPS_3P = ['3p-core', '3p-no-cienie', '3p-no-kabala', '3p-no-korona', '3p-no-oficjum']
SETUPS_5P = ['5p-full']

def parse_overrides_str(override_str: str) -> Dict[str, Dict[str, Any]]:
    """Parsuje ciąg typu 'so-02:target_heresy=0,caa-06:gold=1,kt-09:cost=2'."""
    card_overrides: Dict[str, Dict[str, Any]] = {}
    if not override_str:
        return card_overrides
    
    pairs = [p.strip() for p in override_str.split(',') if p.strip()]
    for pair in pairs:
        if ':' not in pair or '=' not in pair:
            print(f"⚠️ Niepoprawny format nadpisania '{pair}'. Oczekiwano 'karta:pole=wartość'.")
            continue
        card_id, param_val = pair.split(':', 1)
        card_id = card_id.strip()
        field, val_s = param_val.split('=', 1)
        field = field.strip()
        val_s = val_s.strip()
        
        # Konwersja typu (int, bool, str)
        if val_s.lower() in ('true', 'yes'):
            val: Any = True
        elif val_s.lower() in ('false', 'no'):
            val = False
        elif val_s.isdigit() or (val_s.startswith('-') and val_s[1:].isdigit()):
            val = int(val_s)
        else:
            try:
                val = float(val_s)
            except ValueError:
                val = val_s
                
        if card_id not in card_overrides:
            card_overrides[card_id] = {}
        card_overrides[card_id][field] = val
        
    return card_overrides

def cmd_audit(args: argparse.Namespace) -> None:
    setups: List[str]
    if args.setup == 'canon-4p':
        setups = CANON_4P
    elif args.setup == 'all-3p':
        setups = SETUPS_3P
    elif args.setup == 'all-5p':
        setups = SETUPS_5P
    elif args.setup == 'all':
        setups = CANON_4P + SETUPS_3P + SETUPS_5P
    else:
        setups = [args.setup]
        
    print("=" * 80)
    print(f"🏆 AUDYT BALANSU (Próba: {args.games} gier/setup | Warstwa: {args.layer} | Rdzenie: {args.workers})")
    print("=" * 80)
    
    scores = {}
    shares = {}
    for s in setups:
        res = run_batch(games=args.games, setup=s, seed=args.seed, layer=args.layer)
        sc = calculate_balance_score(res)
        sh = faction_shares(res)
        scores[s] = sc
        shares[s] = {k: round(v * 100, 1) for k, v in sh.items()}
        col = "🟢" if sc >= 80.0 else ("🟡" if sc >= 70.0 else "🔴")
        print(f"  {col} {s:<15}: {sc:>5.1f} pkt | Udziały: {shares[s]}")
        sys.stdout.flush()
        
    mean_s = sum(scores.values()) / len(scores)
    min_s = min(scores.values())
    all_green = all(sc >= 80.0 for sc in scores.values())
    icon = "🟢" if all_green else ("🟡" if min_s >= 70.0 else "🔴")
    print("=" * 80)
    print(f"{icon} ŚREDNIA: {mean_s:.2f} pkt | NAJNIŻSZY SETUP: {min_s:.2f} pkt")
    print("=" * 80)

def cmd_test(args: argparse.Namespace) -> None:
    overrides = parse_overrides_str(args.override)
    print("=" * 80)
    print(f"🧪 TEST NACPISANIA KART (Próba: {args.games} gier/setup | Nadpisania: {overrides})")
    print("=" * 80)
    
    setups = CANON_4P if args.setup == 'canon-4p' else [args.setup]
    scores = {}
    shares = {}
    for s in setups:
        res = run_batch(games=args.games, setup=s, seed=args.seed, layer=args.layer,
                        win_overrides={'card_overrides': overrides} if overrides else None)
        sc = calculate_balance_score(res)
        sh = faction_shares(res)
        scores[s] = sc
        shares[s] = {k: round(v * 100, 1) for k, v in sh.items()}
        col = "🟢" if sc >= 80.0 else ("🟡" if sc >= 70.0 else "🔴")
        print(f"  {col} {s:<15}: {sc:>5.1f} pkt | Udziały: {shares[s]}")
        sys.stdout.flush()
        
    mean_s = sum(scores.values()) / len(scores)
    min_s = min(scores.values())
    print("=" * 80)
    print(f"👉 ŚREDNIA: {mean_s:.2f} pkt | NAJNIŻSZY SETUP: {min_s:.2f} pkt")
    print("=" * 80)

def _eval_solver_task(task):
    name, overrides, games, seed, layer = task
    scores = {}
    shares = {}
    for s in CANON_4P:
        res = run_batch(games=games, setup=s, seed=seed, layer=layer, win_overrides={'card_overrides': overrides})
        sc = calculate_balance_score(res)
        scores[s] = round(sc, 1)
        shares[s] = {k: round(v * 100, 1) for k, v in faction_shares(res).items()}
    
    mean_s = sum(scores.values()) / len(scores)
    min_s = min(scores.values())
    return {
        "name": name,
        "overrides": overrides,
        "mean": mean_s,
        "min": min_s,
        "scores": scores,
        "shares": shares,
    }

def cmd_solve(args: argparse.Namespace) -> None:
    so_options = [
        ("so-02 th:0", {"so-02": {"target_heresy": 0}}),
        ("so-03 th:2", {"so-03": {"target_heresy": 2}}),
        ("so-base", {}),
    ]
    caa_options = [
        ("caa-06 gold:1", {"caa-06": {"gold": 1}}),
        ("caa-03 gold:3", {"caa-03": {"gold": 3}}),
        ("caa-07 heresy:2", {"caa-07": {"heresy": 2}}),
        ("caa-base", {}),
    ]
    gc_options = [
        ("gc-04 gold:1", {"gc-04": {"gold": 1}}),
        ("gc-08 heresy:0", {"gc-08": {"heresy": 0}}),
        ("gc-base", {}),
    ]
    
    tasks = []
    for s_name, s_ov in so_options:
        for c_name, c_ov in caa_options:
            for g_name, g_ov in gc_options:
                full_name = f"{s_name} + {c_name} + {g_name}"
                merged = {}
                merged.update(s_ov)
                merged.update(c_ov)
                merged.update(g_ov)
                tasks.append((full_name, merged, args.games, args.seed, args.layer))
                
    print("=" * 80)
    print(f"🚀 WIELOFRAKCYJNY SOLVER KANONU 4P ({len(tasks)} kombinacji | {args.games} gier/setup | {args.workers} rdzeni)")
    print("=" * 80)
    
    results = []
    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(_eval_solver_task, t): t for t in tasks}
        for f in as_completed(futures):
            results.append(f.result())
            
    results.sort(key=lambda x: (x["min"], x["mean"]), reverse=True)
    print("\n🏆 TOP 10 NAJWYŻSZYCH WYNIKÓW:")
    print("-" * 80)
    for r in results[:10]:
        all_green = all(sc >= 80.0 for sc in r["scores"].values())
        icon = "🟢🟢🟢 [5/5 ZIELONE]" if all_green else ("🟢 [Wysoki Balans]" if r["min"] >= 75.0 else ("🟡" if r["min"] >= 65.0 else "🔴"))
        print(f"\n{icon} {r['name']}")
        print(f"   ŚREDNIA: {r['mean']:.2f} pkt | MIN: {r['min']:.2f} pkt")
        for s in CANON_4P:
            col = "🟢" if r['scores'][s] >= 80.0 else ("🟡" if r['scores'][s] >= 70.0 else "🔴")
            print(f"     {col} {s:<15}: {r['scores'][s]:>5.1f} pkt | Udziały: {r['shares'][s]}")

def main() -> None:
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 Simulator & Balance CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Audit
    p_audit = subparsers.add_parser("audit", help="Uruchamia audyt balansu")
    p_audit.add_argument("--setup", default="canon-4p", help="canon-4p | all-3p | all-5p | all | nazwa setupu")
    p_audit.add_argument("--games", type=int, default=5000, help="Liczba gier na setup (domyślnie 5000)")
    p_audit.add_argument("--layer", default="C", help="Warstwa kart (A, B, C)")
    p_audit.add_argument("--seed", type=int, default=42, help="Seed generatora")
    p_audit.add_argument("--workers", type=int, default=10, help="Wątki CPU")
    p_audit.set_defaults(func=cmd_audit)
    
    # Test
    p_test = subparsers.add_parser("test", help="Szybki test nadpisania kart w locie")
    p_test.add_argument("--override", required=True, help="np. 'so-02:target_heresy=0,caa-06:gold=1'")
    p_test.add_argument("--setup", default="canon-4p", help="canon-4p lub nazwa setupu")
    p_test.add_argument("--games", type=int, default=2000, help="Liczba gier na setup")
    p_test.add_argument("--layer", default="C", help="Warstwa kart")
    p_test.add_argument("--seed", type=int, default=42, help="Seed generatora")
    p_test.set_defaults(func=cmd_test)
    
    # Solve
    p_solve = subparsers.add_parser("solve", help="Wielofrakcyjny solver optymalizacji")
    p_solve.add_argument("--games", type=int, default=2000, help="Liczba gier na setup dla każdej kombinacji")
    p_solve.add_argument("--layer", default="C", help="Warstwa kart")
    p_solve.add_argument("--seed", type=int, default=42, help="Seed generatora")
    p_solve.add_argument("--workers", type=int, default=10, help="Wątki CPU")
    p_solve.set_defaults(func=cmd_solve)
    
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
