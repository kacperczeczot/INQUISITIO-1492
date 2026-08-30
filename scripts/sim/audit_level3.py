#!/usr/bin/env python3
"""Script to run a granular per-card +-1 parameter audit (Level 3: Card Economy & Parameters) with full telemetry & deltas."""
from __future__ import annotations
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

from inquisitio.cards.loader import load_all_cards
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

FACTION_NAMES = {
    "so": ("Święte Oficjum", "swiete-oficjum"),
    "caa": ("Cienie Al-Andalus", "cienie-al-andalus"),
    "kb": ("Korona Borgiowie", "korona-borgiowie"),
    "kt": ("Kabała Toledo", "kabala-toledo"),
    "gc": ("Gildia Cieni", "gildia-cieni"),
}


def build_level3_tests(param_filter: str = "all", faction_filter: str = "all", card_filter: str | None = None):
    """Generate comprehensive card parameter and intra-card multi-param tests without arbitrary limits."""
    cards = load_all_cards()
    tests = [
        ("L3_BAZA", "Baza (Bieżące parametry wszystkich kart)", {})
    ]

    params_to_test = ["cost", "heresy", "target_heresy", "gold"]
    if param_filter != "all":
        selected_params = [p.strip() for p in param_filter.split(",")]
        params_to_test = [p for p in params_to_test if p in selected_params]

    sorted_card_ids = sorted(cards.keys())

    PARAM_HARD_BOUNDS = {
        "cost": (0, 5),
        "gold": (0, 3),
        "heresy": (0, 3),
        "target_heresy": (0, 2),
        "agents": (0, 2),
    }

    for cid in sorted_card_ids:
        if cid.startswith("time-"):
            continue

        c = cards[cid]
        faction_prefix = cid.split("-")[0]

        if faction_filter != "all" and faction_prefix != faction_filter:
            continue

        if card_filter and cid.lower() != card_filter.lower():
            continue

        # 1. Granular +/-1 and +/-2 shifts within hard bounds
        for p in params_to_test:
            curr_val = getattr(c, p, 0)
            min_bound, max_bound = PARAM_HARD_BOUNDS.get(p, (0, 10))

            # Delta +1, +2
            for d in (1, 2):
                new_v = curr_val + d
                if min_bound <= new_v <= max_bound:
                    test_id_p = f"L3_{cid.upper()}_{p.upper()}_PLUS{d}"
                    name_p = f"{cid.upper()} ({c.name}): {p} {curr_val} → {new_v}"
                    tests.append((test_id_p, name_p, {"card_overrides": {cid: {p: new_v}}}))

            # Delta -1, -2 (if within valid range)
            for d in (1, 2):
                new_v = curr_val - d
                if min_bound <= new_v <= max_bound and curr_val >= d:
                    test_id_m = f"L3_{cid.upper()}_{p.upper()}_MINUS{d}"
                    name_m = f"{cid.upper()} ({c.name}): {p} {curr_val} → {new_v}"
                    tests.append((test_id_m, name_m, {"card_overrides": {cid: {p: new_v}}}))

            # Extended absolute set values when base is 0
            if curr_val == 0:
                if p == "gold":
                    for ext_val in [1, 2, 3]:
                        if min_bound <= ext_val <= max_bound:
                            test_id_ext = f"L3_{cid.upper()}_{p.upper()}_SET{ext_val}"
                            name_ext = f"{cid.upper()} ({c.name}): dodaj {p} = {ext_val}"
                            tests.append((test_id_ext, name_ext, {"card_overrides": {cid: {p: ext_val}}}))
                elif p in ("target_heresy", "heresy"):
                    for ext_val in [1, 2]:
                        if min_bound <= ext_val <= max_bound:
                            test_id_ext = f"L3_{cid.upper()}_{p.upper()}_SET{ext_val}"
                            name_ext = f"{cid.upper()} ({c.name}): dodaj {p} = {ext_val}"
                            tests.append((test_id_ext, name_ext, {"card_overrides": {cid: {p: ext_val}}}))

        # 2. Single-card Intra-card Multi-dimensional Pairs within Hard Bounds
        curr_cost = getattr(c, "cost", 0)
        curr_gold = getattr(c, "gold", 0)
        curr_heresy = getattr(c, "heresy", 0)
        curr_th = getattr(c, "target_heresy", 0)

        # Cost + Heresy trade-offs (cost 0..5, heresy 0..3)
        for d_c in (-1, 1):
            for d_h in (-1, 1):
                nc = max(0, min(5, curr_cost + d_c))
                nh = max(0, min(3, curr_heresy + d_h))
                if (nc != curr_cost or nh != curr_heresy):
                    tid = f"L3_{cid.upper()}_C{nc}_H{nh}"
                    tname = f"{cid.upper()} ({c.name}): koszt {curr_cost}→{nc}, herezja {curr_heresy}→{nh}"
                    tests.append((tid, tname, {"card_overrides": {cid: {"cost": nc, "heresy": nh}}}))

        # Cost + Gold trade-offs (cost 0..5, gold 0..3)
        for d_c in (-1, 1):
            for d_g in (1, 2):
                nc = max(0, min(5, curr_cost + d_c))
                ng = max(0, min(3, curr_gold + d_g))
                if (nc != curr_cost or ng != curr_gold):
                    tid = f"L3_{cid.upper()}_C{nc}_G{ng}"
                    tname = f"{cid.upper()} ({c.name}): koszt {curr_cost}→{nc}, złoto {curr_gold}→{ng}"
                    tests.append((tid, tname, {"card_overrides": {cid: {"cost": nc, "gold": ng}}}))

        # Gold + Heresy trade-offs (gold 0..3, heresy 0..3)
        for d_g in (-1, 1):
            for d_h in (-1, 1):
                ng = max(0, min(3, curr_gold + d_g))
                nh = max(0, min(3, curr_heresy + d_h))
                if (ng != curr_gold or nh != curr_heresy):
                    tid = f"L3_{cid.upper()}_G{ng}_H{nh}"
                    tname = f"{cid.upper()} ({c.name}): złoto {curr_gold}→{ng}, herezja {curr_heresy}→{nh}"
                    tests.append((tid, tname, {"card_overrides": {cid: {"gold": ng, "heresy": nh}}}))

    # Deduplicate tests
    seen = set()
    unique_tests = []
    for t in tests:
        if t[0] not in seen:
            seen.add(t[0])
            unique_tests.append(t)

    return unique_tests


def _run_single_test_task(task_args: tuple[tuple[str, str, dict], int, int, list[str]]) -> dict:
    """Execute a single audit test rule across all setups."""
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

    # Aggregate telemetry across all setups
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
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 - Granular Level 3 Card Parameter Audit")
    parser.add_argument("--games", type=int, default=10000, help="Number of games per setup (ADR-0014: >= 10000)")
    parser.add_argument("--seed", type=int, default=42, help="RNG seed")
    parser.add_argument("--param", type=str, default="cost,heresy", help="Filter params: cost, heresy, target_heresy, gold, or all")
    parser.add_argument("--faction", type=str, default="all", help="Filter faction: so, caa, kb, kt, gc, or all")
    parser.add_argument("--card", type=str, default=None, help="Filter specific card ID, e.g. so-04")
    parser.add_argument("--workers", type=int, default=os.cpu_count() or 4, help="Number of parallel worker processes")
    parser.add_argument("--players", type=int, default=None, choices=[3, 4, 5], help="Filter setups by player count")
    parser.add_argument("--output", type=str, default=None, help="Output markdown path")
    args = parser.parse_args()

    games_per_setup = args.games
    if args.players:
        setups = [s for s in sorted(SETUP_PRESETS.keys()) if len(SETUP_PRESETS[s]) == args.players]
        setup_tag = f"{len(setups)} setupów ({args.players}P)"
    else:
        setups = sorted(SETUP_PRESETS.keys())
        setup_tag = "16 setupów"
    tests = build_level3_tests(param_filter=args.param, faction_filter=args.faction, card_filter=args.card)

    print("========================================================")
    print("ROZPOCZYNAM PRECYZYJNY AUDYT POZIOMU 3: EKONOMIA I PARAMETRY KART")
    print(f"Testów w serii: {len(tests)} | Próba: {games_per_setup} gier × {setup_tag} | Ziarno: {args.seed}")
    print(f"Filtry: parametry={args.param} | frakcja={args.faction} | karta={args.card or 'wszystkie'}")
    print(f"Równoległe procesy: {args.workers}")
    print("========================================================\n", flush=True)

    t0 = time.time()
    task_list = [(test, games_per_setup, args.seed, setups) for test in tests]
    results = []

    workers = min(args.workers, len(tests))
    if workers > 1:
        with ProcessPoolExecutor(max_workers=workers) as executor:
            for idx, res in enumerate(executor.map(_run_single_test_task, task_list), 1):
                results.append(res)
                print(f"[{idx}/{len(tests)}] [{res['id']}] Global Score: {res['global_score']:5.1f} pkt | Czas: {res['dt']}s", flush=True)
    else:
        for idx, task in enumerate(task_list, 1):
            res = _run_single_test_task(task)
            results.append(res)
            print(f"[{idx}/{len(tests)}] [{res['id']}] Global Score: {res['global_score']:5.1f} pkt | Czas: {res['dt']}s", flush=True)

    elapsed = round(time.time() - t0, 2)
    base = results[0]
    positives, negatives = split_and_sort_audit_results(results, base)

    # Markdown Report Generation
    report_lines = [
        f"# Raport Precyzyjnego Audytu Poziomu 3 (Parametry Pojedynczych Kart) — Wersja Balansu: {CONFIG.version}",
        "",
        f"**Wersja Balansu:** `{CONFIG.version}` | **Data:** {datetime.now().strftime('%Y-%m-%d %H:%M')} | **Przeanalizowano Wariantów Kart:** {len(tests)} | **Próba:** {games_per_setup} gier/setup | **Czas:** {elapsed}s",
        f"**Filtry:** Parametry: `{args.param}` | Frakcja: `{args.faction}` | Karta: `{args.card or 'Wszystkie'}`",
        f"**Wynik Bazy Poziomu 3 (Global):** `{color_score(base['global_score'])} pkt` | 3p: `{base['cat_scores'].get('3p',0.0):.1f} pkt` | 4p: `{base['cat_scores'].get('4p',0.0):.1f} pkt` | 5p: `{base['cat_scores'].get('5p',0.0):.1f} pkt`",
        "",
        "## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy",
        "",
        f"### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta ({len(positives)})",
        "",
        "| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |",
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
            "| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |",
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

    default_report_name = f"audyt_level3_raport_{args.players}p.md" if args.players else "audyt_level3_raport.md"
    out_path, archive_path = save_and_archive_report(report_lines, default_report_name, args.output)

    print("========================================================")
    print(f"PRECYZYJNY AUDYT POZIOMU 3 ZAKOŃCZONY W {elapsed}s!")
    print(f"Raport zapisano w: {out_path}")
    if archive_path:
        print(f"Zarchiwizowano w: {archive_path}")
        print(f"Snapshot configu w: {archive_path.parent / 'game_config.yaml'}")
    print("========================================================")

if __name__ == "__main__":
    main()
