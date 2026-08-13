#!/usr/bin/env python3
"""Script to run a +-1 Niche Variants & Modifiers (Level 4) parameter audit with full telemetry (Min/Avg/Max) & Deltas."""
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
    calculate_category_scores,
    calculate_global_score,
    color_score,
)

LEVEL4_TESTS = [
    ("L4_BAZA", "Baza (Bieżące warianty niszowe i zasady edyktów)", {}),

    # 1. Częstotliwość odkrywania Edyktów Czasu
    ("L4_TIME_DECK_EVERY_ERA", "Edykty Czasu: Odkrywane co 1 Erę (+1 powszechność)", {"time_deck_freq": 1}),
    ("L4_TIME_DECK_EVERY_2ERAS", "Edykty Czasu: Odkrywane co 2 Ery (-1 powszechność)", {"time_deck_freq": 2}),

    # 2. Otwarcie Szlaku Morskiego dla Cieni
    ("L4_SEA_ROUTE_ERA4", "Szlak Morski Cieni: Otwarcie w Erze 4 (-1 Era)", {"sea_route_era": 4}),
    ("L4_SEA_ROUTE_ERA6", "Szlak Morski Cieni: Otwarcie w Erze 6 (+1 Era)", {"sea_route_era": 6}),

    # 3. Ruch Inkwizytora (Patrol)
    ("L4_INQUISITOR_SPEED2", "Inkwizytor Patrol: Ruch o 2 pola (+1 ruch)", {"inquisitor_speed": 2}),
    ("L4_INQUISITOR_SPEED0", "Inkwizytor Patrol: Ruch o 0 pól (Stacjonarny)", {"inquisitor_speed": 0}),

    # 4. Werdykt Stołu (Głosowanie tajne vs jawne)
    ("L4_VERDICT_SECRET", "Werdykt Stołu: Wariant z tajnymi kartami głosów", {"verdict_secret": True}),
]

def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 - Audit Level 4 Niche Variants")
    parser.add_argument("--games", type=int, default=300, help="Number of games per setup")
    parser.add_argument("--seed", type=int, default=42, help="RNG seed")
    parser.add_argument("--output", type=str, default=None, help="Output markdown path")
    args = parser.parse_args()

    games_per_setup = args.games
    setups = sorted(SETUP_PRESETS.keys())

    print("========================================================")
    print("ROZPOCZYNAM PEŁNY AUDYT POZIOMU 4: WARIANTY NISZOWE I MODYFIKATORY")
    print(f"Próba: {games_per_setup} gier × 16 setupów | Ziarno: {args.seed}")
    print("========================================================\n")

    t0 = time.time()
    results = []

    for rule_id, rule_name, rule_params in LEVEL4_TESTS:
        t_rule = time.time()

        summaries = []
        for sname in setups:
            summary = run_batch(
                games=games_per_setup,
                setup=sname,
                seed=args.seed,
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

        results.append({
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
        })

        print(f"[{rule_id}] Global Score: {global_score:5.1f} pkt | Czas: {dt}s")

    elapsed = round(time.time() - t0, 2)
    base = results[0]

    # Markdown Report Generation
    report_lines = [
        "# Raport Audytu Poziomu 4 (Warianty Niszowe i Modyfikatory)",
        "",
        f"**Przeanalizowano Wariantów:** {len(LEVEL4_TESTS)} | **Próba:** {games_per_setup} gier/setup | **Czas:** {elapsed}s",
        f"**Wynik Bazy Poziomu 4 (Global):** `{color_score(base['global_score'])} pkt` | 3p: `{base['cat_scores'].get('3p',0.0):.1f} pkt` | 4p: `{base['cat_scores'].get('4p',0.0):.1f} pkt` | 5p: `{base['cat_scores'].get('5p',0.0):.1f} pkt`",
        "",
        "## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy",
        "",
        "| ID | Wariant Niszowy Poziomu 4 | Global Score | Delta Global | 3p Score | Delta 3p | 4p Score | Delta 4p | 5p Score | Delta 5p | Status Balansu |",
        "| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
    ]

    for r in results:
        g_diff = r['global_score'] - base['global_score']
        g_diff_str = f"+{g_diff:.1f}" if g_diff > 0 else f"{g_diff:.1f}"

        s3 = r['cat_scores'].get('3p', 0.0)
        b3 = base['cat_scores'].get('3p', 0.0)
        d3 = s3 - b3
        d3_str = f"+{d3:.1f}" if d3 > 0 else f"{d3:.1f}"
        s3_fmt = f"⬆️ {s3:.1f}" if d3 > 0 else f"{s3:.1f}"

        s4 = r['cat_scores'].get('4p', 0.0)
        b4 = base['cat_scores'].get('4p', 0.0)
        d4 = s4 - b4
        d4_str = f"+{d4:.1f}" if d4 > 0 else f"{d4:.1f}"
        s4_fmt = f"⬆️ {s4:.1f}" if d4 > 0 else f"{d4:.1f}"

        s5 = r['cat_scores'].get('5p', 0.0)
        b5 = base['cat_scores'].get('5p', 0.0)
        d5 = s5 - b5
        d5_str = f"+{d5:.1f}" if d5 > 0 else f"{d5:.1f}"
        s5_fmt = f"⬆️ {s5:.1f}" if d5 > 0 else f"{s5:.1f}"

        if g_diff > 0.5:
            status = "🟢 POPRAWIA GLOBALNIE"
        elif g_diff < -0.5:
            status = "🔴 POGARSZA GLOBALNIE"
        else:
            status = "⚪ OPTYMALNY"

        report_lines.append(
            f"| `{r['id']}` | {r['name']} | {color_score(r['global_score'], bold=True)} | `{g_diff_str}` | {s3_fmt} | `{d3_str}` | {s4_fmt} | `{d4_str}` | {s5_fmt} | `{d5_str}` | {status} |"
        )



    report_lines.extend([
        "",
        "## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm",
        "",
        "| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |",
        "| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
    ])

    for r in results:
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

        report_lines.append(
            f"| `{r['id']}` | {eras_str} | {r['deadlock_pct']:.1f}% | {r['poverty_pct']:.1f}% | {autodafe_str} | {acc_str} | {gold_str} | {heresy_str} | {norm_status} |"
        )

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

    out_path = args.output
    if not out_path:
        out_path = Path(__file__).resolve().parent.parent.parent / "playtesting" / "sim-reports" / "audyt_level4_raport.md"
    else:
        out_path = Path(out_path)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(report_lines), encoding="utf-8")

    print("========================================================")
    print(f"AUDYT POZIOMU 4 ZAKOŃCZONY W {elapsed}s!")
    print(f"Raport zapisano w: {out_path}")
    print("========================================================")

if __name__ == "__main__":
    main()
