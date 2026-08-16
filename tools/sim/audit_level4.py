#!/usr/bin/env python3
"""Script to run a +-1 Niche Variants & Modifiers (Level 4) parameter audit with full telemetry (Min/Avg/Max) & Deltas."""
import argparse
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from pathlib import Path

# Fix path to include sim directory
SIM_DIR = Path(__file__).resolve().parent.parent.parent / "sim"
sys.path.insert(0, str(SIM_DIR))

from inquisitio.config import CONFIG
from inquisitio.engine.setup import SETUP_PRESETS
from inquisitio.runner.batch import run_batch
from inquisitio.runner.scoring import (
    calculate_category_scores,
    calculate_global_score,
    color_score,
)
from inquisitio.runner.audit_facts import (
    delta_status,
    score_pair,
    save_and_archive_report,
    split_and_sort_audit_results,
)

def build_level4_tests():
    nv = CONFIG.variants
    tests = [
        ("L4_BAZA", "Baza (Bieżące warianty niszowe i zasady edyktów)", {}),
        ("L4_NO_TIME_DECK", "Kronika Dziejów: Całkowite wyłączenie edyktów", {"no_time_deck": True}),
        ("L4_VERDICT_SECRET", "Werdykt: jawny → tajny (brak koordynacji anty-snowball)", {"verdict_secret": True}),
    ]
    cur_freq = getattr(nv, "time_deck_freq", 1)
    if cur_freq != 1:
        tests.append(("L4_TIME_DECK_EVERY_ERA", f"Edykty Czasu: co {cur_freq} Erę → co 1 Erę", {"time_deck_freq": 1}))
    if cur_freq != 2:
        tests.append(("L4_TIME_DECK_EVERY_2ERAS", f"Edykty Czasu: co {cur_freq} Erę → co 2 Ery", {"time_deck_freq": 2}))

    cur_sea = getattr(nv, "sea_route_era", 5)
    if cur_sea != 4:
        tests.append(("L4_SEA_ROUTE_ERA4", f"Szlak Morski: Era {cur_sea} → Era 4", {"sea_route_era": 4}))
    if cur_sea != 5:
        tests.append(("L4_SEA_ROUTE_ERA5", f"Szlak Morski: Era {cur_sea} → Era 5", {"sea_route_era": 5}))
    if cur_sea != 6:
        tests.append(("L4_SEA_ROUTE_ERA6", f"Szlak Morski: Era {cur_sea} → Era 6", {"sea_route_era": 6}))

    cur_inq = getattr(nv, "inquisitor_speed", 1)
    if cur_inq != 2:
        tests.append(("L4_INQUISITOR_SPEED2", f"Inkwizytor Patrol: ruch {cur_inq} → 2", {"inquisitor_speed": 2}))
    if cur_inq != 0:
        tests.append(("L4_INQUISITOR_SPEED0", f"Inkwizytor Patrol: ruch {cur_inq} → 0", {"inquisitor_speed": 0}))

    return tests


LEVEL4_TESTS = build_level4_tests()

def _run_single_test_task(task_args: tuple[tuple[str, str, dict], int, int, list[str]]) -> dict:
    (rule_id, rule_name, rule_params), games_per_setup, seed, setups = task_args
    t_rule = time.time()

    summaries = []
    for sname in setups:
        summary = run_batch(
            games=games_per_setup,
            setup=sname,
            seed=seed,
            layer="C",
            win_overrides=rule_params,
        )
        summaries.append(summary)

    cat_scores = calculate_category_scores(summaries)
    global_score = calculate_global_score(cat_scores)
    dt = round(time.time() - t_rule, 2)

    # Aggregate telemetry across all setups for this test
    n_sum = len(summaries)
    eras_avg = sum(s.eras_avg for s in summaries) / n_sum
    eras_min = min(s.eras_min for s in summaries)
    eras_max = max(s.eras_max for s in summaries)

    deadlock_pct = (sum(s.eras_limit_pct for s in summaries) / n_sum) * 100.0
    poverty_pct = (sum(s.passes_forced_pct for s in summaries) / n_sum) * 100.0

    autodafe_avg = sum(s.autodafe_avg for s in summaries) / n_sum
    autodafe_min = min(s.autodafe_min for s in summaries)
    autodafe_max = max(s.autodafe_max for s in summaries)

    acc_avg = sum(s.accusations_avg for s in summaries) / n_sum
    acc_min = min(s.accusations_min for s in summaries)
    acc_max = max(s.accusations_max for s in summaries)

    gold_avg = sum(s.avg_gold_end for s in summaries) / n_sum
    gold_min = min(s.gold_min for s in summaries)
    gold_max = max(s.gold_max for s in summaries)

    heresy_avg = sum(s.avg_heresy_end for s in summaries) / n_sum
    heresy_min = min(s.heresy_min for s in summaries)
    heresy_max = max(s.heresy_max for s in summaries)

    return {
        "id": rule_id,
        "name": rule_name,
        "global_score": global_score,
        "cat_scores": cat_scores,
        "dt": dt,
        "eras_avg": eras_avg, "eras_min": eras_min, "eras_max": eras_max,
        "deadlock_pct": deadlock_pct,
        "poverty_pct": poverty_pct,
        "autodafe_avg": autodafe_avg, "autodafe_min": autodafe_min, "autodafe_max": autodafe_max,
        "acc_avg": acc_avg, "acc_min": acc_min, "acc_max": acc_max,
        "gold_avg": gold_avg, "gold_min": gold_min, "gold_max": gold_max,
        "heresy_avg": heresy_avg, "heresy_min": heresy_min, "heresy_max": heresy_max,
    }

def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 - Audit Level 4 Niche Variants")
    parser.add_argument("--games", type=int, default=300, help="Number of games per setup")
    parser.add_argument("--seed", type=int, default=42, help="RNG seed")
    parser.add_argument("--workers", type=int, default=os.cpu_count() or 4, help="Number of parallel worker processes")
    parser.add_argument("--output", type=str, default=None, help="Output markdown path")
    args = parser.parse_args()

    games_per_setup = args.games
    setups = sorted(SETUP_PRESETS.keys())

    print("========================================================")
    print("ROZPOCZYNAM PEŁNY AUDYT POZIOMU 4: WARIANTY NISZOWE I MODYFIKATORY")
    print(f"Próba: {games_per_setup} gier × 16 setupów | Ziarno: {args.seed}")
    print(f"Równoległe procesy: {args.workers}")
    print("========================================================\n", flush=True)

    t0 = time.time()
    task_list = [(test, games_per_setup, args.seed, setups) for test in LEVEL4_TESTS]
    results = []

    workers = min(args.workers, len(LEVEL4_TESTS))
    if workers > 1:
        with ProcessPoolExecutor(max_workers=workers) as executor:
            for res in executor.map(_run_single_test_task, task_list):
                results.append(res)
                print(f"[{res['id']}] Global Score: {res['global_score']:5.1f} pkt | Czas: {res['dt']}s", flush=True)
    else:
        for task in task_list:
            res = _run_single_test_task(task)
            results.append(res)
            print(f"[{res['id']}] Global Score: {res['global_score']:5.1f} pkt | Czas: {res['dt']}s", flush=True)

    elapsed = round(time.time() - t0, 2)
    base = results[0]
    positives, negatives = split_and_sort_audit_results(results, base)

    # Markdown Report Generation
    report_lines = [
        f"# Raport Audytu Poziomu 4 (Warianty Niszowe i Edykty) — Wersja Balansu: {CONFIG.version}",
        "",
        f"**Wersja Balansu:** `{CONFIG.version}` | **Data:** {datetime.now().strftime('%Y-%m-%d %H:%M')} | **Przeanalizowano Wariantów:** {len(LEVEL4_TESTS)} | **Próba:** {games_per_setup} gier/setup | **Czas:** {elapsed}s",
        f"**Wynik Bazy Poziomu 4 (Global):** `{color_score(base['global_score'])} pkt` | 3p: `{base['cat_scores'].get('3p',0.0):.1f} pkt` | 4p: `{base['cat_scores'].get('4p',0.0):.1f} pkt` | 5p: `{base['cat_scores'].get('5p',0.0):.1f} pkt`",
        "",
        "## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy",
        "",
        f"### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta ({len(positives)})",
        "",
        "| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |",
        "| :---: | :--- | :---: | :---: | :---: | :---: | :---: |",
    ]

    for r in positives:
        g_diff = r['global_score'] - base['global_score']
        report_lines.append(
            f"| `{r['id']}` | {r['name']} | {score_pair(base['global_score'], r['global_score'], colored=True)} | "
            f"{score_pair(base['cat_scores'].get('3p', 0.0), r['cat_scores'].get('3p', 0.0))} | "
            f"{score_pair(base['cat_scores'].get('4p', 0.0), r['cat_scores'].get('4p', 0.0))} | "
            f"{score_pair(base['cat_scores'].get('5p', 0.0), r['cat_scores'].get('5p', 0.0))} | "
            f"{delta_status(g_diff)} |"
        )

    if negatives:
        report_lines.extend([
            "",
            f"<details>",
            f"<summary><b>🔻 Pokaż pozostałe {len(negatives)} wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>",
            "",
            "| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |",
            "| :---: | :--- | :---: | :---: | :---: | :---: | :---: |",
        ])
        for r in negatives:
            g_diff = r['global_score'] - base['global_score']
            report_lines.append(
                f"| `{r['id']}` | {r['name']} | {score_pair(base['global_score'], r['global_score'], colored=True)} | "
                f"{score_pair(base['cat_scores'].get('3p', 0.0), r['cat_scores'].get('3p', 0.0))} | "
                f"{score_pair(base['cat_scores'].get('4p', 0.0), r['cat_scores'].get('4p', 0.0))} | "
                f"{score_pair(base['cat_scores'].get('5p', 0.0), r['cat_scores'].get('5p', 0.0))} | "
                f"{delta_status(g_diff)} |"
            )
        report_lines.extend([
            "",
            "</details>",
        ])

    def _telemetry_row(r):
        eras_str = f"{r['eras_avg']:.2f} Er ({r['eras_min']}–{r['eras_max']})"
        autodafe_str = f"{r['autodafe_avg']:.2f} ({r['autodafe_min']}–{r['autodafe_max']})"
        acc_str = f"{r['acc_avg']:.2f} ({r['acc_min']}–{r['acc_max']})"
        gold_str = f"{r['gold_avg']:.2f}zł ({r['gold_min']:.1f}–{r['gold_max']:.1f})"
        heresy_str = f"{r['heresy_avg']:.2f} ({r['heresy_min']:.1f}–{r['heresy_max']:.1f})"

        eras_ok = (5.0 <= r['eras_avg'] <= 7.0)
        deadlock_ok = (r['deadlock_pct'] <= 15.0)
        poverty_ok = (r['poverty_pct'] <= 30.0)

        if eras_ok and deadlock_ok and poverty_ok:
            norm_status = "🟢 W NORMIE"
        elif deadlock_ok and poverty_ok:
            norm_status = "⚠️ WARTOŚCI BRZEGOWE"
        else:
            norm_status = "🔴 PRZEKROCZONE NORMY"

        return f"| `{r['id']}` | {eras_str} | {r['deadlock_pct']:.1f}% | {r['poverty_pct']:.1f}% | {autodafe_str} | {acc_str} | {gold_str} | {heresy_str} | {norm_status} |"

    report_lines.extend([
        "",
        "## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm",
        "",
        f"### 🌟 Telemetria Wariantów z Zyskiem ({len(positives)})",
        "",
        "| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |",
        "| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
    ])

    for r in positives:
        report_lines.append(_telemetry_row(r))

    if negatives:
        report_lines.extend([
            "",
            f"<details>",
            f"<summary><b>🔻 Pokaż telemetrię pozostałych {len(negatives)} wariantów bez zysku...</b></summary>",
            "",
            "| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |",
            "| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
        ])
        for r in negatives:
            report_lines.append(_telemetry_row(r))
        report_lines.extend([
            "",
            "</details>",
        ])

    report_lines.extend([
        "",
        "## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry",
        "",
        "- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.",
        "- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.",
        "- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.",
        "- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.",
        "- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.",
    ])

    out_path, archive_path = save_and_archive_report(report_lines, "audyt_level4_raport.md", args.output)

    print("========================================================")
    print(f"AUDYT POZIOMU 4 ZAKOŃCZONY W {elapsed}s!")
    print(f"Raport zapisano w: {out_path}")
    if archive_path:
        print(f"Zarchiwizowano w: {archive_path}")
        print(f"Snapshot configu w: {archive_path.parent / 'game_config.yaml'}")
    print("========================================================")

if __name__ == "__main__":
    main()
