#!/usr/bin/env python3
"""Script to run a +-1 Faction Victory Condition (Level 2) parameter audit with full telemetry (Min/Avg/Max) & Deltas."""
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


def _pc(sec, delta: int = 0) -> str:
    """3p/4p/5p snapshot or scalar, optional ±delta on each."""
    if hasattr(sec, "__getitem__") and not isinstance(sec, (str, bytes)):
        try:
            return f"{sec['3p'] + delta}/{sec['4p'] + delta}/{sec['5p'] + delta}"
        except (KeyError, TypeError):
            pass
    return str(int(sec) + delta)


def _gc_falls_n(gc) -> int:
    f = gc.falls
    if hasattr(f, "default"):
        return int(f.default)
    return int(f)


def build_level2_tests():
    """Generate ±1 tests dynamically from current CONFIG victory conditions."""
    v = CONFIG.victory
    so = v.swiete_oficjum
    caa = v.cienie_al_andalus
    kb = v.korona_borgiowie
    kt = v.kabala_toledo
    gc = v.gildia_cieni
    hb = kt.heresy_band
    return [
        ("L2_BAZA", "Baza (Bieżące warunki zwycięstwa)", {}),
        ("L2_SO_STACKS_PLUS1", f"Oficjum Stosy: {_pc(so.stacks)} → {_pc(so.stacks, 1)}", {"so_stacks_offset": 1}),
        ("L2_SO_STACKS_MINUS1", f"Oficjum Stosy: {_pc(so.stacks)} → {_pc(so.stacks, -1)}", {"so_stacks_offset": -1}),
        ("L2_SO_CONDEMNS_MINUS1", f"Oficjum Skazania: {_pc(so.condemns)} → {_pc(so.condemns, -1)}", {"so_condemns_offset": -1}),
        ("L2_CAA_RELICS_PLUS1", f"Cienie Relikwie: {caa.relics} → {caa.relics + 1}", {"caa_relics_offset": 1}),
        ("L2_CAA_RELICS_MINUS1", f"Cienie Relikwie: {caa.relics} → {caa.relics - 1}", {"caa_relics_offset": -1}),
        ("L2_KB_DECREES_PLUS1", f"Korona Dekrety: {_pc(kb.decrees)} → {_pc(kb.decrees, 1)}", {"kb_decrees_offset": 1}),
        ("L2_KB_DECREES_MINUS1", f"Korona Dekrety: {_pc(kb.decrees)} → {_pc(kb.decrees, -1)}", {"kb_decrees_offset": -1}),
        ("L2_KB_HOOKS_PLUS1", f"Korona Haki: {_pc(kb.hooks)} → {_pc(kb.hooks, 1)}", {"kb_hooks_offset": 1}),
        ("L2_KT_FRAGS_PLUS1", f"Kabała Fragmenty: {_pc(kt.fragments)} → {_pc(kt.fragments, 1)}", {"kt_frags_offset": 1}),
        ("L2_KT_FRAGS_MINUS1", f"Kabała Fragmenty: {_pc(kt.fragments)} → {_pc(kt.fragments, -1)}", {"kt_frags_offset": -1}),
        ("L2_KT_ERA_PLUS1", f"Kabała Era: {_pc(kt.era)} → {_pc(kt.era, 1)}", {"kt_era_offset": 1}),
        ("L2_KT_ERA_MINUS1", f"Kabała Era: {_pc(kt.era)} → {_pc(kt.era, -1)}", {"kt_era_offset": -1}),
        ("L2_KT_HERESY_LOW_PLUS1", f"Kabała Pasmo: {hb[0]}–{hb[1]} → {hb[0] + 1}–{hb[1]}", {"kt_heresy_band": (hb[0] + 1, hb[1])}),
        ("L2_KT_HERESY_HIGH_PLUS1", f"Kabała Pasmo: {hb[0]}–{hb[1]} → {hb[0]}–{hb[1] + 1}", {"kt_heresy_band": (hb[0], hb[1] + 1)}),
        ("L2_KT_HERESY_HIGH_MINUS1", f"Kabała Pasmo: {hb[0]}–{hb[1]} → {hb[0]}–{hb[1] - 1}", {"kt_heresy_band": (hb[0], hb[1] - 1)}),
        ("L2_GC_FALLS_PLUS1", f"Gildia Upadki: {_gc_falls_n(gc)} → {_gc_falls_n(gc) + 1}", {"gc_falls_offset": 1}),
        ("L2_GC_FALLS_MINUS1", f"Gildia Upadki: {_gc_falls_n(gc)} → {_gc_falls_n(gc) - 1}", {"gc_falls_offset": -1}),
    ]


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
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 - Audit Level 2 Victory Conditions")
    parser.add_argument("--games", type=int, default=300, help="Number of games per setup")
    parser.add_argument("--seed", type=int, default=42, help="RNG seed")
    parser.add_argument("--workers", type=int, default=os.cpu_count() or 4, help="Number of parallel worker processes")
    parser.add_argument("--output", type=str, default=None, help="Output markdown path")
    args = parser.parse_args()

    games_per_setup = args.games
    setups = sorted(SETUP_PRESETS.keys())

    print("========================================================")
    print("ROZPOCZYNAM PEŁNY AUDYT POZIOMU 2: WARUNKI ZWYCIĘSTWA I SKALOWANIE")
    print(f"Próba: {games_per_setup} gier × 16 setupów | Ziarno: {args.seed}")
    print(f"Równoległe procesy: {args.workers}")
    print("========================================================\n", flush=True)

    t0 = time.time()
    level2_tests = build_level2_tests()
    task_list = [(test, games_per_setup, args.seed, setups) for test in level2_tests]
    results = []

    workers = min(args.workers, len(level2_tests))
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
        f"# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: {CONFIG.version}",
        "",
        f"**Wersja Balansu:** `{CONFIG.version}` | **Data:** {datetime.now().strftime('%Y-%m-%d %H:%M')} | **Przeanalizowano Wariantów:** {len(level2_tests)} | **Próba:** {games_per_setup} gier/setup | **Czas:** {elapsed}s",
        f"**Wynik Bazy Poziomu 2 (Global):** `{color_score(base['global_score'])} pkt` | 3p: `{base['cat_scores'].get('3p',0.0):.1f} pkt` | 4p: `{base['cat_scores'].get('4p',0.0):.1f} pkt` | 5p: `{base['cat_scores'].get('5p',0.0):.1f} pkt`",
        "",
        "## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy",
        "",
        f"### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta ({len(positives)})",
        "",
        "| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |",
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
            "| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |",
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

    out_path, archive_path = save_and_archive_report(report_lines, "audyt_level2_raport.md", args.output)

    print("========================================================")
    print(f"AUDYT POZIOMU 2 ZAKOŃCZONY W {elapsed}s!")
    print(f"Raport zapisano w: {out_path}")
    if archive_path:
        print(f"Zarchiwizowano w: {archive_path}")
        print(f"Snapshot configu w: {archive_path.parent / 'game_config.yaml'}")
    print("========================================================")

if __name__ == "__main__":
    main()
