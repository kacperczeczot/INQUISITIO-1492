#!/usr/bin/env python3
"""INQUISITIO-1492 — AUDYTOR KART PROBLEMOWYCH 4P (Targeted Problem Card Optimizer).

Wyszukuje i optymalizuje WYŁĄCZNIE karty zaklasyfikowane jako problematyczne na podstawie
Badania Użyteczności i Wpływu (Ablation Matrix 4P):
  1. 🩸 AUTOPODATKI (Self-Harm Tax): Karty, których wyłączenie podnosi winrate ich frakcji
     (karta jest obciążeniem/haraczem dla gracza) -> generuje mutacje buffujące (cost -1, heresy -1, gold +1).
  2. ⚠️ DESTABILIZATORY (Disruptors / Toxic Promoters): Karty, których wyłączenie podnosi 4P Score
     (karta zaburza symetrię stołu) -> generuje mutacje łagodzące / nerfujące (cost +1, heresy +1).
  3. 💤 KARTY MARTWE (Dead Weight / Low Impact): Karty o znikomym wpływie na grę
     (karta nie uczestniczy w ekosystemie) -> generuje mutacje aktywujące.

Karty z grup FILAR (Core Keystone), KOTWICA (Balance Anchor) i NARZĘDZIE (Utility) są w 100% bezpieczne i pomijane.

Uruchamianie:
  python3 tools/sim/audytor_kart_problemowych.py --dry-run
  python3 tools/sim/audytor_kart_problemowych.py --apply
"""
from __future__ import annotations

import argparse
import copy
import os
import re
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from pathlib import Path
from typing import Any

# Ensure sim and tools/sim directories are on path
TOOLS_SIM_DIR = Path(__file__).resolve().parent
SIM_DIR = TOOLS_SIM_DIR.parent.parent / "sim"

for p in (TOOLS_SIM_DIR, SIM_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from inquisitio.cards.loader import load_all_cards
from inquisitio.config import CONFIG
from inquisitio.config_updater import apply_mutation_to_config, save_config_and_bump_version
from inquisitio.engine.setup import SETUP_PRESETS, FactionId
from inquisitio.runner.audit_facts import save_and_archive_report, score_pair
from inquisitio.runner.batch import run_batch
from inquisitio.runner.impact_taxonomy import classify_card_impact_4p
from inquisitio.runner.scoring import (
    calculate_balance_score,
    calculate_category_scores,
    calculate_global_score,
    calculate_setup_score,
    color_score,
)

REPORTS_DIR = Path(__file__).resolve().parent.parent.parent / "playtesting" / "sim-reports"
CANONICAL_4P_SETUPS = [
    "4p-core",
    "4p-no-cienie",
    "4p-no-kabala",
    "4p-no-korona",
    "4p-no-oficjum",
]

PREFIX_TO_FACTION_ID = {
    "so": FactionId.SWIETE_OFICJUM,
    "caa": FactionId.CIENIE_AL_ANDALUS,
    "kb": FactionId.KORONA_BORGIOWIE,
    "kt": FactionId.KABALA_TOLEDO,
    "gc": FactionId.GILDIA_CIENI,
}

FACTION_FULL_NAMES = {
    "so": "Święte Oficjum",
    "caa": "Cienie Al-Andalus",
    "kb": "Korona & Borgiowie",
    "kt": "Kabała z Toledo",
    "gc": "Gildia Cieni",
}


def _run_single_task(task_args: tuple[str, str, dict, int, int, list[str]]) -> dict:
    """Executes an evaluation batch across the 5 canonical 4P setups."""
    tid, name, overrides, games_per_setup, seed, setups = task_args
    t_start = time.time()
    summaries = []
    for sname in setups:
        s = run_batch(
            games=games_per_setup,
            setup=sname,
            seed=seed,
            layer="C",
            win_overrides=overrides,
        )
        summaries.append(s)

    f_shares: dict[str, float] = {}
    total_wins = 0
    for s in summaries:
        for f_name, win_cnt in s.wins.items():
            f_shares[f_name] = f_shares.get(f_name, 0.0) + win_cnt
            total_wins += win_cnt

    tot = total_wins or 1
    agg_shares = {k: (v / tot) * 100.0 for k, v in f_shares.items()}
    cat_scores = calculate_category_scores(summaries)
    score = calculate_global_score(cat_scores)

    n_sum = len(summaries)
    eras_avg = sum(s.eras_avg for s in summaries) / n_sum
    deadlock_pct = (sum(s.eras_limit_pct for s in summaries) / n_sum) * 100.0
    poverty_pct = (sum(s.passes_forced_pct for s in summaries) / n_sum) * 100.0
    dt = round(time.time() - t_start, 2)

    return {
        "id": tid,
        "name": name,
        "overrides": overrides,
        "score": score,
        "faction_shares": agg_shares,
        "eras_avg": eras_avg,
        "deadlock_pct": deadlock_pct,
        "poverty_pct": poverty_pct,
        "duration": dt,
    }


def parse_or_detect_problematic_cards(games_screen: int = 1000, seed: int = 42) -> dict[str, dict[str, Any]]:
    """Identifies problematic cards from existing ablation report or quick baseline screening."""
    ablation_report = REPORTS_DIR / "archive" / CONFIG.version / "raport_uzytecznosci_i_wplywu_4p.md"
    if not ablation_report.exists():
        ablation_report = REPORTS_DIR / "current" / "raport_uzytecznosci_i_wplywu_4p.md"

    cards = load_all_cards()
    problem_cards: dict[str, dict[str, Any]] = {}

    if ablation_report.exists():
        print(f"📖 Wczytuję klasyfikację kart z raportu ablacji: {ablation_report.name}")
        content = ablation_report.read_text(encoding="utf-8")
        # Parse table lines: | `cid` | **Name** | Faction | Cost | Heresy | ... | Rola |
        for line in content.splitlines():
            if not line.startswith("| `") or "` | **" not in line:
                continue
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) < 12:
                continue
            cid = parts[0].replace("`", "").strip()
            name = parts[1].replace("*", "").strip()
            role = parts[11]

            if cid not in cards:
                continue

            c = cards[cid]
            pref = cid.split("-")[0]

            if "AUTOPODATEK" in role:
                problem_cards[cid] = {"id": cid, "name": name, "category": "SELF_HARM", "role": role, "card": c, "faction": pref}
            elif "DISRUPTOR" in role or "TOKSYCZNY" in role:
                problem_cards[cid] = {"id": cid, "name": name, "category": "DISRUPTOR", "role": role, "card": c, "faction": pref}
            elif "DEAD" in role or "NISKIEGO WPŁYWU" in role or "Pasywna" in role:
                problem_cards[cid] = {"id": cid, "name": name, "category": "DEAD_WEIGHT", "role": role, "card": c, "faction": pref}

    if not problem_cards:
        print("⚡ Brak gotowego raportu — przeprowadzam szybki screening ablacyjny 60 kart...")
        # Run quick ablation baseline
        base_res = _run_single_task(("BASE", "Baza", {}, games_screen, seed, CANONICAL_4P_SETUPS))
        base_score = base_res["score"]
        base_shares = base_res["faction_shares"]

        tasks = []
        for cid, card in sorted(cards.items()):
            if cid.split("-")[0] not in PREFIX_TO_FACTION_ID:
                continue
            tasks.append((f"ABL_{cid}", f"Bez {cid}", {"disabled_cards": [cid]}, games_screen, seed, CANONICAL_4P_SETUPS))

        with ProcessPoolExecutor(max_workers=min(10, len(tasks), os.cpu_count() or 4)) as ex:
            results = list(ex.map(_run_single_task, tasks))

        for r in results:
            cid = r["id"].replace("ABL_", "")
            pref = cid.split("-")[0]
            fname = PREFIX_TO_FACTION_ID[pref].value
            d_share = base_shares.get(fname, 25.0) - r["faction_shares"].get(fname, 25.0)
            d_4p = r["score"] - base_score
            cat_code, role_name, group = classify_card_impact_4p(d_share, d_4p)
            if group in ("SELF_HARM", "DISRUPTOR", "DEAD_WEIGHT"):
                problem_cards[cid] = {"id": cid, "name": cards[cid].name, "category": group, "role": role_name, "card": cards[cid], "faction": pref}

    return problem_cards


def generate_targeted_candidate_mutations(problem_cards: dict[str, dict[str, Any]]) -> list[tuple[str, str, dict]]:
    """Generates focused mutations strictly for problematic cards based on their issue."""
    candidates: list[tuple[str, str, dict]] = []

    for cid, info in sorted(problem_cards.items()):
        c = info["card"]
        cat = info["category"]

        if cat == "SELF_HARM":
            # Autopodatek: buff cost, heresy, or add gold
            if c.cost > 0:
                candidates.append((
                    f"MUT_{cid.upper()}_COST_MINUS1",
                    f"{cid.upper()} ({c.name}) [Buff Autopodatku]: koszt {c.cost} → {c.cost - 1}",
                    {"card_overrides": {cid: {"cost": c.cost - 1}}},
                ))
            if c.heresy > 0:
                candidates.append((
                    f"MUT_{cid.upper()}_HERESY_MINUS1",
                    f"{cid.upper()} ({c.name}) [Buff Autopodatku]: herezja {c.heresy} → {c.heresy - 1}",
                    {"card_overrides": {cid: {"heresy": c.heresy - 1}}},
                ))
            if c.gold == 0 and c.cost >= 1:
                candidates.append((
                    f"MUT_{cid.upper()}_GOLD_SET1",
                    f"{cid.upper()} ({c.name}) [Buff Autopodatku]: dodaj złoto = 1",
                    {"card_overrides": {cid: {"gold": 1}}},
                ))
            if c.gold > 0:
                candidates.append((
                    f"MUT_{cid.upper()}_GOLD_PLUS1",
                    f"{cid.upper()} ({c.name}) [Buff Autopodatku]: złoto {c.gold} → {c.gold + 1}",
                    {"card_overrides": {cid: {"gold": c.gold + 1}}},
                ))

        elif cat == "DISRUPTOR":
            # Disruptor: nerf cost or heresy
            candidates.append((
                f"MUT_{cid.upper()}_COST_PLUS1",
                f"{cid.upper()} ({c.name}) [Nerf Disruptora]: koszt {c.cost} → {c.cost + 1}",
                {"card_overrides": {cid: {"cost": c.cost + 1}}},
            ))
            candidates.append((
                f"MUT_{cid.upper()}_HERESY_PLUS1",
                f"{cid.upper()} ({c.name}) [Nerf Disruptora]: herezja {c.heresy} → {c.heresy + 1}",
                {"card_overrides": {cid: {"heresy": c.heresy + 1}}},
            ))
            if c.gold > 0:
                candidates.append((
                    f"MUT_{cid.upper()}_GOLD_MINUS1",
                    f"{cid.upper()} ({c.name}) [Nerf Disruptora]: złoto {c.gold} → {c.gold - 1}",
                    {"card_overrides": {cid: {"gold": c.gold - 1}}},
                ))

        elif cat == "DEAD_WEIGHT":
            # Dead weight: activate via cost 0, heresy 0, or gold injection
            if c.cost > 0:
                candidates.append((
                    f"MUT_{cid.upper()}_COST_MINUS1",
                    f"{cid.upper()} ({c.name}) [Aktywacja Dead Weight]: koszt {c.cost} → {c.cost - 1}",
                    {"card_overrides": {cid: {"cost": c.cost - 1}}},
                ))
            if c.heresy > 0:
                candidates.append((
                    f"MUT_{cid.upper()}_HERESY_MINUS1",
                    f"{cid.upper()} ({c.name}) [Aktywacja Dead Weight]: herezja {c.heresy} → {c.heresy - 1}",
                    {"card_overrides": {cid: {"heresy": c.heresy - 1}}},
                ))
            if c.gold == 0:
                candidates.append((
                    f"MUT_{cid.upper()}_GOLD_SET1",
                    f"{cid.upper()} ({c.name}) [Aktywacja Dead Weight]: dodaj złoto = 1",
                    {"card_overrides": {cid: {"gold": 1}}},
                ))

    # Align candidate count to a multiple of 10 for 100% CPU thread efficiency
    remainder = len(candidates) % 10
    if remainder != 0:
        needed = 10 - remainder
        # Add secondary fine-tuners on problem cards
        extra = []
        for cid, info in sorted(problem_cards.items()):
            c = info["card"]
            p2 = f"MUT_{cid.upper()}_COST_PLUS2"
            if not any(t[0] == p2 for t in candidates) and not any(t[0] == p2 for t in extra):
                extra.append((p2, f"{cid.upper()} ({c.name}) [Tuning]: koszt {c.cost} → {c.cost + 2}", {"card_overrides": {cid: {"cost": c.cost + 2}}}))
                if len(extra) == needed:
                    break
        candidates.extend(extra)

    return candidates


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 — Audytor Kart Problemowych 4P")
    parser.add_argument("--dry-run", action="store_true", help="Tylko analiza i ranking mutacji bez zapisu do SSOT")
    parser.add_argument("--apply", action="store_true", help="Zastosuj najlepszą mutację do game_config.yaml")
    parser.add_argument("--seed", type=int, default=42, help="RNG seed")
    args = parser.parse_args()

    print("═══════════════════════════════════════════════════════════════")
    print("   INQUISITIO-1492 — AUDYTOR KART PROBLEMOWYCH W KANONIE 4P    ")
    print("      Celowana optymalizacja Autopodatków, Disruptorów i Dead Weight")
    print(f"      Wersja: {CONFIG.version} | Ziarno: {args.seed}           ")
    print("═══════════════════════════════════════════════════════════════\n")

    t_start = time.time()

    # 1. Detect Problematic Cards
    problem_cards = parse_or_detect_problematic_cards(games_screen=1000, seed=args.seed)
    print(f"🎯 Zidentyfikowano {len(problem_cards)} problematycznych kart w Kanonie 4P:")
    for cid, info in sorted(problem_cards.items()):
        print(f"   • {cid:<7s} ({info['name']:<25s}): {info['role']}")
    print()

    # 2. Generate Candidate Mutations
    candidates = generate_targeted_candidate_mutations(problem_cards)
    print(f"🔧 Wygenerowano {len(candidates)} ukierunkowanych mutacji (wielokrotność 10: {len(candidates)%10 == 0})\n")

    # 3. Measure Base Score
    print("📊 Mierzę stan bazowy Kanonu 4P...")
    base_res = _run_single_task(("BASE", "Baza", {}, 3000, args.seed, CANONICAL_4P_SETUPS))
    base_score = base_res["score"]
    print(f"   🎯 Bieżący 4P Score: {color_score(base_score, bold=True)} pkt")
    print(f"   📊 Udziały bazowe: {', '.join(f'{k}: {v:.1f}%' for k, v in sorted(base_res['faction_shares'].items()))}\n")

    # 4. Lejek Selekcyjny
    # Etap 1: Szybki Przesiew (1000 gier/setup)
    print(f"⏳ [Etap 1/2] Przesiew {len(candidates)} kandydatów (1000 gier/setup)...")
    tasks_stage1 = [(c[0], c[1], c[2], 1000, args.seed, CANONICAL_4P_SETUPS) for c in candidates]
    with ProcessPoolExecutor(max_workers=min(10, len(tasks_stage1), os.cpu_count() or 4)) as ex:
        res_stage1 = list(ex.map(_run_single_task, tasks_stage1))

    res_stage1.sort(key=lambda r: r["score"], reverse=True)
    top_n = min(20, (len(res_stage1) // 10) * 10 or 10)
    top_candidates = res_stage1[:top_n]

    print(f"✔ Wyłoniono TOP {top_n} finalistów do Etapu 2:")
    for idx, r in enumerate(top_candidates[:5], 1):
        delta = r["score"] - base_score
        print(f"   {idx:2d}. {r['id']:<28s} Score: {color_score(r['score'])} pkt (Δ {delta:+5.1f} pkt) | {r['name']}")
    print()

    # Etap 2: Głęboka Weryfikacja (5000 gier/setup)
    print(f"⏳ [Etap 2/2] Głęboka weryfikacja TOP {top_n} finalistów (5000 gier/setup)...")
    tasks_stage2 = [(r["id"], r["name"], r["overrides"], 5000, args.seed, CANONICAL_4P_SETUPS) for r in top_candidates]
    with ProcessPoolExecutor(max_workers=min(10, len(tasks_stage2), os.cpu_count() or 4)) as ex:
        res_stage2 = list(ex.map(_run_single_task, tasks_stage2))

    res_stage2.sort(key=lambda r: r["score"], reverse=True)
    best = res_stage2[0]
    best_delta = best["score"] - base_score

    print("\n═══════════════════════════════════════════════════════════════")
    print(f"🏆 NAJLEPSZA MUTACJA DLA KART PROBLEMOWYCH:")
    print(f"   ID:       {best['id']}")
    print(f"   Opis:     {best['name']}")
    print(f"   4P Score: {color_score(base_score)} → {color_score(best['score'], bold=True)} pkt (Zysk: {best_delta:+5.2f} pkt)")
    print(f"   Rozkład:  {', '.join(f'{k}: {v:.1f}%' for k, v in sorted(best['faction_shares'].items()))}")
    print(f"   Telemetria: Śr. Er {best['eras_avg']:.2f} | Deadlocks: {best['deadlock_pct']:.1f}% | Pas Biedy: {best['poverty_pct']:.1f}%")
    print("═══════════════════════════════════════════════════════════════\n")

    # 5. Generowanie Raportu
    report_lines = [
        f"# Raport Audytora Kart Problemowych 4P — Wersja Balansu: {CONFIG.version}",
        "",
        f"**Wersja:** `{CONFIG.version}` | **Data:** {datetime.now().strftime('%Y-%m-%d %H:%M')} | **Próba:** 5000 gier/setup | **Ziarno:** {args.seed}",
        f"**Baza 4P Score:** {base_score:.2f} pkt | **Najlepsza Mutacja:** {best['score']:.2f} pkt (Δ {best_delta:+5.2f} pkt)",
        "",
        "## 1. Zidentyfikowane Karty Problematyczne",
        "",
        "| ID Karty | Nazwa Karty | Frakcja | Klasyfikacja w Matrycy 4P | Rola Projektowa |",
        "| :--- | :--- | :--- | :--- | :--- |",
    ]
    for cid, info in sorted(problem_cards.items()):
        report_lines.append(f"| `{cid}` | **{info['name']}** | {FACTION_FULL_NAMES.get(info['faction'], info['faction'])} | {info['role']} | {info['category']} |")

    report_lines.extend([
        "",
        "## 2. Wyniki Testów Celowanych (TOP Finaliści)",
        "",
        "| ID Mutacji | Modyfikacja Karty | 4P Score | Δ 4P | Średnia Er | Pas Biedy % | Deadlock % |",
        "| :--- | :--- | :---: | :---: | :---: | :---: | :---: |",
    ])
    for r in res_stage2:
        d = r["score"] - base_score
        report_lines.append(
            f"| `{r['id']}` | {r['name']} | {color_score(r['score'], bold=True)} | `{d:+5.2f} pkt` | {r['eras_avg']:.2f} | {r['poverty_pct']:.1f}% | {r['deadlock_pct']:.1f}% |"
        )

    out_path, arc_path = save_and_archive_report(report_lines, "audyt_kart_problemowych_4p.md")
    print(f"📝 Raport zapisano w: {out_path}")
    if arc_path:
        print(f"📦 Archiwum w: {arc_path}")

    # 6. Apply if requested
    if args.apply and best_delta > 0.0:
        print(f"\n🚀 Aplikuję najlepszą mutację {best['id']} do game_config.yaml...")
        apply_mutation_to_config(best["overrides"])
        new_ver = save_config_and_bump_version()
        print(f"✅ Zapisano nową wersję konfiguracji: {new_ver}")
    elif args.apply:
        print("\nℹ️ Żadna mutacja nie przyniosła zysku balansu — config bez zmian.")
    else:
        print("\n💡 Tryb DRY-RUN — config nie został zmodyfikowany. Użyj `--apply` aby wdrożyć zmianę.")

    elapsed = round(time.time() - t_start, 1)
    print(f"⏱️ Całkowity czas audytu: {elapsed}s ({round(elapsed/60, 1)} min)")


if __name__ == "__main__":
    main()
