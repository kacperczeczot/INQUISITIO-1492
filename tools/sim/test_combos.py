import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'sim'))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from inquisitio.runner.batch import run_batch
from inquisitio.runner.scoring import calculate_balance_score, evaluate_vitality
from inquisitio.runner.balance import faction_shares

CANON_4P = ['4p-core', '4p-no-cienie', '4p-no-kabala', '4p-no-korona', '4p-no-oficjum']

def eval_combo(item):
    name, ov = item
    scores = []
    shares_map = {}
    vitalities = []
    for s in CANON_4P:
        res = run_batch(games=3000, setup=s, seed=42, layer='C', win_overrides=ov)
        sc = calculate_balance_score(res)
        scores.append(sc)
        shares_map[s] = {k: round(v*100, 1) for k, v in faction_shares(res).items()}
        vit = evaluate_vitality(res)
        vitalities.append(vit.vitality_penalty)
    mean_s = sum(scores)/len(scores)
    min_s = min(scores)
    max_vit = max(vitalities)
    return name, mean_s, min_s, scores, shares_map, max_vit

if __name__ == '__main__':
    combos = [
        ('BAZA v1.0-alpha.22', {}),
        ('1. SO-03 heresy 2->1 + KB-01 cost 1->0', {
            'card_overrides': {'so-03': {'heresy': 1}, 'kb-01': {'cost': 0}}
        }),
        ('2. SO-03 th 3->2 + KB-01 cost 1->0', {
            'card_overrides': {'so-03': {'target_heresy': 2}, 'kb-01': {'cost': 0}}
        }),
        ('3. SO-03 th 3->2 + GC-04 cost 1->2 + KB-01 cost 1->0', {
            'card_overrides': {'so-03': {'target_heresy': 2}, 'gc-04': {'cost': 2}, 'kb-01': {'cost': 0}}
        }),
        ('4. SO-03 th 3->2 + GC-04 cost 1->2 + CAA-05 cost 1->0 + KB-01 cost 1->0', {
            'card_overrides': {
                'so-03': {'target_heresy': 2},
                'gc-04': {'cost': 2},
                'caa-05': {'cost': 0},
                'kb-01': {'cost': 0}
            }
        }),
        ('5. SO-03 th 3->2 + GC-11 cost 0->1 + CAA-08 cost 2->1 + KB-01 cost 1->0', {
            'card_overrides': {
                'so-03': {'target_heresy': 2},
                'gc-11': {'cost': 1},
                'caa-08': {'cost': 1},
                'kb-01': {'cost': 0}
            }
        }),
    ]

    for c in combos:
        name, mean_s, min_s, scores, shares, vit = eval_combo(c)
        print(f'=== {name} === Mean 4P: {mean_s:5.1f} | Min: {min_s:5.1f} | Vit: {vit:.2f}')
        print(f'   Scores: {[round(x,1) for x in scores]}')
        for s in CANON_4P:
            print(f'     {s:<14}: {shares[s]}')
        print()
