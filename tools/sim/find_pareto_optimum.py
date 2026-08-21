import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'sim'))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from inquisitio.runner.batch import run_batch
from inquisitio.runner.scoring import calculate_balance_score, evaluate_vitality
from inquisitio.runner.balance import faction_shares

CANON_4P = ['4p-core', '4p-no-cienie', '4p-no-kabala', '4p-no-korona', '4p-no-oficjum']

def eval_candidate(name, ov, games=3000):
    scores = []
    shares_map = {}
    vitalities = []
    deadlocks = []
    eras = []
    for s in CANON_4P:
        res = run_batch(games=games, setup=s, seed=42, layer='C', win_overrides=ov)
        sc = calculate_balance_score(res)
        scores.append(sc)
        shares_map[s] = {k: round(v*100, 1) for k, v in faction_shares(res).items()}
        vit = evaluate_vitality(res)
        vitalities.append(vit.vitality_penalty)
        deadlocks.append(res.eras_limit_pct)
        eras.append(res.eras_avg)
    mean_s = sum(scores)/len(scores)
    min_s = min(scores)
    max_vit = max(vitalities)
    max_dl = max(deadlocks)
    avg_eras = sum(eras)/len(eras)
    return {
        'name': name,
        'mean': mean_s,
        'min': min_s,
        'scores': scores,
        'shares': shares_map,
        'max_vit': max_vit,
        'max_dl': max_dl,
        'avg_eras': avg_eras,
        'overrides': ov
    }

if __name__ == '__main__':
    print('--- EVALUATING PARETO CANDIDATES ---')
    base = eval_candidate('BAZA (v1.0-alpha.22)', {})
    print(f"BAZA: Mean: {base['mean']:.2f} | Min: {base['min']:.2f} | Scores: {[round(x,1) for x in base['scores']]}")
    print()

    candidates = [
        # Przetestujmy kombinacje drobnych korekt, które wspierają Cienie w obecności Gildii i Koronę w 4p-core
        ('C1: CAA-05 cost 0 + CAA-06 cost 0', {
            'card_overrides': {'caa-05': {'cost': 0}, 'caa-06': {'cost': 0}}
        }),
        ('C2: CAA-05 cost 0 + CAA-08 condition bypass', {
            'card_overrides': {'caa-05': {'cost': 0}, 'caa-08': {'cost': 0}}
        }),
        ('C3: CAA-05 cost 0 + CAA-09 cost 0', {
            'card_overrides': {'caa-05': {'cost': 0}, 'caa-09': {'cost': 0}}
        }),
        ('C4: CAA-05 cost 0 + KB-06 gold 3', {
            'card_overrides': {'caa-05': {'cost': 0}, 'kb-06': {'gold': 3}}
        }),
        ('C5: CAA-05 cost 0 + KB-08 cost 0', {
            'card_overrides': {'caa-05': {'cost': 0}, 'kb-08': {'cost': 0}}
        }),
        ('C6: CAA-05 cost 0 + GC-06 cost 2', {
            'card_overrides': {'caa-05': {'cost': 0}, 'gc-06': {'cost': 2}}
        }),
        ('C7: CAA-05 cost 0 + GC-07 cost 2', {
            'card_overrides': {'caa-05': {'cost': 0}, 'gc-07': {'cost': 2}}
        }),
        ('C8: CAA-05 cost 0 + SO-04 cost 2', {
            'card_overrides': {'caa-05': {'cost': 0}, 'so-04': {'cost': 2}}
        }),
        ('C9: CAA-05 cost 0 + SO-08 cost 2', {
            'card_overrides': {'caa-05': {'cost': 0}, 'so-08': {'cost': 2}}
        }),
        ('C10: CAA-05 cost 0 + KT-06 cost 1', {
            'card_overrides': {'caa-05': {'cost': 0}, 'kt-06': {'cost': 1}}
        }),
    ]

    results = []
    for name, ov in candidates:
        res = eval_candidate(name, ov)
        d_mean = res['mean'] - base['mean']
        d_min = res['min'] - base['min']
        print(f"{name:<45} -> Mean: {res['mean']:5.2f} (Δ {d_mean:+5.2f}) | Min: {res['min']:5.2f} (Δ {d_min:+5.2f}) | Scores: {[round(x,1) for x in res['scores']]}")
        if d_mean >= -0.1 and d_min > 0.05:
            results.append(res)

    print()
    print(f"=== ZNALEZIONO {len(results)} KANDYDATÓW PARETO-LEPSZYCH ===")
    for r in sorted(results, key=lambda x: -x['mean']):
        print(f"-> {r['name']}: Mean: {r['mean']:.2f}, Min: {r['min']:.2f}")
