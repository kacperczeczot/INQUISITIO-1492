#!/usr/bin/env python3
import math
import sys
from inquisitio.runner.batch import run_batch
from inquisitio.runner.scoring import calculate_balance_stats

setups = ['4p-core', '4p-no-cienie', '4p-no-kabala', '4p-no-korona', '4p-no-oficjum']
sample_sizes = [50, 100, 200, 400, 800, 1600, 3200, 6400, 10000]
n_trials = 25

print('=== EMPIRYCZNY POMIAR BŁĘDU STANDARDOWEGO I ROZSTĘPU BALANSU (25 prób per N) ===', flush=True)
print(f'{"N":>6} | {"Śr. Score":>10} | {"Emp. Std (σ)":>12} | {"Analityczny SE":>14} | {"95% CI (±)":>11} | {"Rozstęp [Min-Max]":>18}', flush=True)
print('-' * 85, flush=True)

for N in sample_sizes:
    scores = []
    ana_ses = []
    for trial in range(n_trials):
        trial_scores = []
        trial_ses = []
        for sname in setups:
            summary = run_batch(games=N, setup=sname, seed=10000 + trial * 31 + N * 7, threshold=7, layer='C')
            sc, se = calculate_balance_stats(summary)
            trial_scores.append(sc)
            trial_ses.append(se)
        avg_score = sum(trial_scores) / len(trial_scores)
        avg_se = math.sqrt(sum(s**2 for s in trial_ses)) / len(setups)
        scores.append(avg_score)
        ana_ses.append(avg_se)
    
    mean_score = sum(scores) / len(scores)
    emp_std = math.sqrt(sum((s - mean_score)**2 for s in scores) / (len(scores) - 1))
    mean_ana_se = sum(ana_ses) / len(ana_ses)
    ci95 = 1.96 * emp_std
    min_sc, max_sc = min(scores), max(scores)
    row = f'{N:6d} | {mean_score:10.2f} | {emp_std:12.3f} | {mean_ana_se:14.3f} | {ci95:11.2f} | [{min_sc:5.1f} - {max_sc:5.1f}] ({max_sc-min_sc:4.1f} pkt)'
    print(row, flush=True)

print('\n=== ZAKOŃCZONO POMIAR EMPIRYCZNY ===', flush=True)
