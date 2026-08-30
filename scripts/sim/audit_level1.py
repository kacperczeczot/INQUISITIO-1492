#!/usr/bin/env python3
"""Script to run a +-1 System Core (Level 1) parameter audit with full telemetry (Min/Avg/Max) & Deltas."""
import argparse
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from pathlib import Path

# Fix path to include sim directory
SRC_DIR = Path(__file__).resolve().parent.parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

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


def _pc(sec, delta: int = 0) -> str:
    """3p/4p/5p snapshot or scalar, optional ±delta on each."""
    if hasattr(sec, "__getitem__") and not isinstance(sec, (str, bytes)):
        try:
            return f"{sec['3p'] + delta}/{sec['4p'] + delta}/{sec['5p'] + delta}"
        except (KeyError, TypeError):
            pass
    return str(int(sec) + delta)


def build_level1_tests():
    """Generate ±1 tests dynamically as relative offsets from current CONFIG values.
    Includes independent format-specific tests (3p, 4p, 5p) and table-wide rules.
    """
    s = CONFIG.system
    t, g, h = s.accusation_threshold, s.start_gold, s.hand_limit

    tests = [
        ("L1_BAZA", "Baza (Bieżące parametry systemowe)", {}),
    ]

    # --- 1. Format-specific Accusation Thresholds (3p, 4p, 5p) ---
    for p_key in ("3p", "4p", "5p"):
        cur_t = t[p_key] if isinstance(t, dict) or hasattr(t, "__getitem__") else int(t)
        for d in (1, 2):
            tests.append((f"L1_THRESHOLD_{p_key.upper()}_PLUS{d}", f"Próg Oskarżenia ({p_key}): {cur_t} → {cur_t + d}", {f"threshold_{p_key}_offset": d}))
            if cur_t - d >= 1:
                tests.append((f"L1_THRESHOLD_{p_key.upper()}_MINUS{d}", f"Próg Oskarżenia ({p_key}): {cur_t} → {cur_t - d}", {f"threshold_{p_key}_offset": -d}))

    # --- 2. Format-specific Starting Gold (3p, 4p, 5p) ---
    for p_key in ("3p", "4p", "5p"):
        cur_g = g[p_key] if isinstance(g, dict) or hasattr(g, "__getitem__") else int(g)
        for d in (1, 2):
            tests.append((f"L1_START_GOLD_{p_key.upper()}_PLUS{d}", f"Złoto startowe ({p_key}): {cur_g}zł → {cur_g + d}zł", {f"start_gold_{p_key}_offset": d}))
            if cur_g - d >= 0:
                tests.append((f"L1_START_GOLD_{p_key.upper()}_MINUS{d}", f"Złoto startowe ({p_key}): {cur_g}zł → {cur_g - d}zł", {f"start_gold_{p_key}_offset": -d}))

    # --- 3. Format-specific Hand Limit (3p, 4p, 5p) ---
    for p_key in ("3p", "4p", "5p"):
        cur_h = h[p_key] if isinstance(h, dict) or hasattr(h, "__getitem__") else int(h)
        tests.append((f"L1_HAND_LIMIT_{p_key.upper()}_PLUS1", f"Limit ręki ({p_key}): {cur_h} → {cur_h + 1}", {f"hand_limit_{p_key}_offset": 1}))
        if cur_h - 1 >= 2:
            tests.append((f"L1_HAND_LIMIT_{p_key.upper()}_MINUS1", f"Limit ręki ({p_key}): {cur_h} → {cur_h - 1}", {f"hand_limit_{p_key}_offset": -1}))

    # --- 4. Global System Rules ---
    tests.extend([
        ("L1_THRESHOLD_PLUS1", f"Próg Oskarżenia (global): {_pc(t)} → {_pc(t, 1)}", {"threshold_offset": 1}),
        ("L1_THRESHOLD_MINUS1", f"Próg Oskarżenia (global): {_pc(t)} → {_pc(t, -1)}", {"threshold_offset": -1}),
        ("L1_OBSERVED_PLUS1", f"Próg Obserwowanej: {s.observed_threshold} → {s.observed_threshold + 1}", {"observed_threshold_offset": 1}),
        ("L1_OBSERVED_MINUS1", f"Próg Obserwowanej: {s.observed_threshold} → {s.observed_threshold - 1}", {"observed_threshold_offset": -1}),
        ("L1_CARDS_PER_ERA_PLUS1", f"Karty/Erę: {s.cards_per_era} → {s.cards_per_era + 1}", {"cards_per_era_offset": 1}),
        ("L1_CARDS_PER_ERA_MINUS1", f"Karty/Erę: {s.cards_per_era} → {s.cards_per_era - 1}", {"cards_per_era_offset": -1}),
        ("L1_INTRIGUE_GOLD_PLUS1", f"Akcja Gospodarcza: {s.intrigue_gold} → {s.intrigue_gold + 1}", {"intrigue_gold_offset": 1}),
        ("L1_INTRIGUE_GOLD_MINUS1", f"Akcja Gospodarcza: {s.intrigue_gold} → {s.intrigue_gold - 1}", {"intrigue_gold_offset": -1}),
        ("L1_MAX_ERAS_PLUS1", f"Limit Er: {s.max_eras} → {s.max_eras + 1}", {"max_eras_offset": 1}),
        ("L1_MAX_ERAS_MINUS1", f"Limit Er: {s.max_eras} → {s.max_eras - 1}", {"max_eras_offset": -1}),
        ("L1_AGENTS_PLUS1", f"Agenci: {s.agents_per_player} → {s.agents_per_player + 1}", {"agents_offset": 1}),
        ("L1_AGENTS_MINUS1", f"Agenci: {s.agents_per_player} → {s.agents_per_player - 1}", {"agents_offset": -1}),
        ("L1_AUTODAFE_COOLDOWN_PLUS1", f"Cooldown Autodafé: {s.autodafe_cooldown} → {s.autodafe_cooldown + 1} Ery", {"cooldown_offset": 1}),
        ("L1_AUTODAFE_COOLDOWN_MINUS1", f"Cooldown Autodafé: {s.autodafe_cooldown} → {s.autodafe_cooldown - 1} Ery", {"cooldown_offset": -1}),
    ])

    return tests


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
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 - Audit Level 1 System Parameters")
    parser.add_argument("--games", type=int, default=10000, help="Number of games per setup (ADR-0014: >= 10000)")
    parser.add_argument("--seed", type=int, default=42, help="RNG seed")
    parser.add_argument("--workers", type=int, default=os.cpu_count() or 4, help="Number of parallel worker processes")
    parser.add_argument("--players", type=int, default=None, choices=[3, 4, 5], help="Filter setups by player count")
    parser.add_argument("--output", type=str, default=None, help="Output markdown path")
    parser.add_argument("--force", action="store_true", help="Zezwól na nadpisanie istniejącego raportu w archiwum")
    args = parser.parse_args()

    games_per_setup = args.games
    if args.players:
        setups = [s for s in sorted(SETUP_PRESETS.keys()) if len(SETUP_PRESETS[s]) == args.players]
        setup_tag = f"{len(setups)} setupów ({args.players}P)"
    else:
        setups = sorted(SETUP_PRESETS.keys())
        setup_tag = "16 setupów"
    level1_tests = build_level1_tests()

    print("========================================================")
    print("ROZPOCZYNAM PEŁNY AUDYT POZIOMU 1: GŁÓWNE MECHANIKI SYSTEMOWE")
    print(f"Próba: {games_per_setup} gier × {setup_tag} | Ziarno: {args.seed}")
    print(f"Równoległe procesy: {args.workers}")
    print("========================================================\n", flush=True)

    t0 = time.time()
    task_list = [(test, games_per_setup, args.seed, setups) for test in level1_tests]
    results = []

    workers = min(args.workers, len(level1_tests))
    if workers > 1:
        with ProcessPoolExecutor(max_workers=workers) as executor:
            for idx, res in enumerate(executor.map(_run_single_test_task, task_list), 1):
                results.append(res)
                print(f"[{res['id']}] Global Score: {res['global_score']:5.1f} pkt | Czas: {res['dt']}s", flush=True)
    else:
        for idx, task in enumerate(task_list, 1):
            res = _run_single_test_task(task)
            results.append(res)
            print(f"[{res['id']}] Global Score: {res['global_score']:5.1f} pkt | Czas: {res['dt']}s", flush=True)

    elapsed = round(time.time() - t0, 2)
    base = results[0]
    positives, negatives = split_and_sort_audit_results(results, base)

    # Markdown Report Generation
    report_lines = [
        f"# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: {CONFIG.version}",
        "",
        f"**Wersja Balansu:** `{CONFIG.version}` | **Data:** {datetime.now().strftime('%Y-%m-%d %H:%M')} | **Przeanalizowano Wariantów:** {len(level1_tests)} | **Próba:** {games_per_setup} gier/setup | **Czas:** {elapsed}s",
        f"**Wynik Bazy Poziomu 1 (Global):** `{color_score(base['global_score'])} pkt` | 3p: `{base['cat_scores'].get('3p',0.0):.1f} pkt` | 4p: `{base['cat_scores'].get('4p',0.0):.1f} pkt` | 5p: `{base['cat_scores'].get('5p',0.0):.1f} pkt`",
        "",
        "## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy",
        "",
        f"### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta ({len(positives)})",
        "",
        "| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |",
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
            "| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |",
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

    default_report_name = f"audyt_level1_raport_{args.players}p.md" if args.players else "audyt_level1_raport.md"
    out_path, archive_path = save_and_archive_report(report_lines, default_report_name, args.output, allow_overwrite=args.force)

    print("========================================================")
    print(f"AUDYT POZIOMU 1 ZAKOŃCZONY W {elapsed}s!")
    print(f"Raport zapisano w: {out_path}")
    if archive_path:
        print(f"Zarchiwizowano w: {archive_path}")
        print(f"Snapshot configu w: {archive_path.parent / 'game_config.yaml'}")
    print("========================================================")

if __name__ == "__main__":
    main()
