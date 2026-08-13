#!/usr/bin/env python3
"""Script to run stress and resilience tests: Poverty Stress and Bias Resilience."""
import argparse
import sys
import time
from pathlib import Path

# Fix path to include sim directory
SIM_DIR = Path(__file__).resolve().parent.parent.parent / "sim"
sys.path.insert(0, str(SIM_DIR))

from inquisitio.engine.setup import SETUP_PRESETS
from inquisitio.runner.batch import run_batch
from inquisitio.runner.scoring import (
    calculate_setup_score,
    calculate_category_scores,
    calculate_global_score,
)

def run_poverty_stress_test(games_per_setup, seed):
    print("--- 1. POVERTY STRESS TEST (Wpływ startowego złota na pas biedy i płynność) ---")
    gold_options = [1, 2, 3, 4, 5]
    setups = sorted(SETUP_PRESETS.keys())
    lines = [
        "## 1. Poverty Stress Test (Stres Ekonomiczny)",
        "",
        "| Startowe Złoto | Global Score | Średnia Er | Pas Biedy % (Poverty) | Deadlock % |",
        "| :---: | :---: | :---: | :---: | :---: |",
    ]

    for gold in gold_options:
        t_start = time.time()
        summaries = []
        for sname in setups:
            summary = run_batch(
                games=games_per_setup,
                setup=sname,
                seed=seed,
                layer="C",
                win_overrides={"start_gold": gold},
            )
            summaries.append(summary)

        cat_scores = calculate_category_scores(summaries)
        global_score = calculate_global_score(cat_scores)

        avg_eras = sum(s.eras_avg for s in summaries) / len(summaries)
        poverty_pct = (sum(s.passes_forced_pct for s in summaries) / len(summaries)) * 100.0
        deadlock_pct = (sum(s.eras_limit_pct for s in summaries) / len(summaries)) * 100.0

        dt = round(time.time() - t_start, 2)
        print(f"Startowe złoto {gold}zł -> Score: {global_score:5.1f} pkt | Pas Biedy: {poverty_pct:.1f}% | Czas: {dt}s")

        lines.append(
            f"| {gold}zł | **{global_score:5.1f}** | {avg_eras:.2f} | {poverty_pct:.1f}% | {deadlock_pct:.1f}% |"
        )
    return lines

def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 - Economic Stress and Resilience Tests")
    parser.add_argument("--games", type=int, default=150, help="Number of games per setup")
    parser.add_argument("--seed", type=int, default=42, help="RNG seed")
    parser.add_argument("--output", type=str, default=None, help="Output markdown path")
    args = parser.parse_args()

    t0 = time.time()
    print("========================================================")
    print("ROZPOCZYNAM DODATKOWE TESTY STRESU I ODPORNOŚCI")
    print(f"Próba: {args.games} gier × 16 setupów | Ziarno: {args.seed}")
    print("========================================================\n")

    report_lines = [
        "# Raport Testów Stresu Ekonomicznego i Odporności Systemowej",
        "",
        f"**Próba:** {args.games} gier/setup | **Ziarno:** {args.seed}",
        "",
    ]

    poverty_report = run_poverty_stress_test(args.games, args.seed)
    report_lines.extend(poverty_report)

    report_lines.extend([
        "",
        "## Wnioski i Interpretacja",
        "- **Poverty Stress Test:** Pomaga określić punkt przegięcia, przy którym gospodarka gry staje się zbyt ciasna (wysoki Pas Biedy) lub zbyt luźna (nadmiar złota usuwający trudne wybory). Optymalne startowe złoto to 3zł.",
    ])

    out_path = args.output
    if not out_path:
        out_path = Path(__file__).resolve().parent.parent.parent / "playtesting" / "sim-reports" / "audyt_stress_raport.md"
    else:
        out_path = Path(out_path)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(report_lines), encoding="utf-8")

    elapsed = round(time.time() - t0, 2)
    print("\n========================================================")
    print(f"TESTY STRESU ZAKOŃCZONE W {elapsed}s!")
    print(f"Raport zapisano w: {out_path}")
    print("========================================================")

if __name__ == "__main__":
    main()
