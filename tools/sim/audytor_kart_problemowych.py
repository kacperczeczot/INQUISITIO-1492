#!/usr/bin/env python3
"""INQUISITIO-1492 — AUDYTOR KART PROBLEMOWYCH 4P (Targeted Problem Card Optimizer).

Autonomiczny optymalizator balansu skupiony w 100% na kartach problematycznych
zidentyfikowanych w badaniu użyteczności i wpływu (Ablation Matrix 4P):
  1. 🩸 AUTOPODATKI (Self-Harm Tax): Karty, których wyłączenie podnosi winrate ich frakcji
     (karta jest obciążeniem/haraczem dla gracza) -> generuje mutacje buffujące (cost -1, heresy -1, gold +1).
  2. ⚠️ DESTABILIZATORY (Disruptors / Toxic Promoters): Karty, których wyłączenie podnosi 4P Score
     (karta zaburza symetrię stołu) -> generuje mutacje łagodzące / nerfujące (cost +1, heresy +1).
  3. 💤 KARTY MARTWE (Dead Weight / Low Impact): Karty o znikomym wpływie na grę
     (karta nie uczestniczy w ekosystemie) -> generuje mutacje aktywujące.

Karty z grup FILAR (Core Keystone), KOTWICA (Balance Anchor) i NARZĘDZIE (Utility) są w 100% bezpieczne i pomijane.

Działa w ciągłej pętli iteracyjnej (1D i 2D composite pairs), dopóki istnieją poprawki zwiększające 4P Score.

Uruchamianie:
  python3 tools/sim/audytor_kart_problemowych.py --apply
  python3 tools/sim/audytor_kart_problemowych.py --dry-run
  python3 tools/sim/audytor_kart_problemowych.py --apply --max-iters 5
"""
from __future__ import annotations

import argparse
import copy
import os
import re
import shutil
import subprocess
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

import yaml
from inquisitio.cards.loader import load_all_cards
from inquisitio.config import CONFIG, _CONFIG_PATH
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
BALANCE_NOTES_PATH = Path(__file__).resolve().parent.parent.parent / "playtesting" / "balance-notes.md"

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
        content = ablation_report.read_text(encoding="utf-8")
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
            elif "DISRUPTOR" in role or "TOKSYCZNY" in role or "SZUM" in role:
                problem_cards[cid] = {"id": cid, "name": name, "category": "DISRUPTOR", "role": role, "card": c, "faction": pref}
            elif "DEAD" in role or "NISKIEGO WPŁYWU" in role or "Pasywna" in role:
                problem_cards[cid] = {"id": cid, "name": name, "category": "DEAD_WEIGHT", "role": role, "card": c, "faction": pref}

    if not problem_cards:
        print("⚡ Przeprowadzam szybki screening ablacyjny 60 kart...")
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


def generate_targeted_candidate_mutations(
    problem_cards: dict[str, dict[str, Any]],
    include_2d_combos: bool = False,
    base_res: dict[str, Any] | None = None,
) -> list[tuple[str, str, dict]]:
    """Generates focused mutations strictly for problematic cards."""
    candidates: list[tuple[str, str, dict]] = []

    for cid, info in sorted(problem_cards.items()):
        c = info["card"]
        cat = info["category"]

        if cat == "SELF_HARM":
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

    # 2D Combos between problematic cards
    if include_2d_combos and len(candidates) >= 2:
        combos = []
        for i in range(min(15, len(candidates))):
            for j in range(i + 1, min(20, len(candidates))):
                m1 = candidates[i]
                m2 = candidates[j]
                c1_id = list(m1[2]["card_overrides"].keys())[0]
                c2_id = list(m2[2]["card_overrides"].keys())[0]
                if c1_id != c2_id:
                    comb_id = f"{m1[0]}__{m2[0]}"
                    comb_name = f"{m1[1]} + {m2[1]}"
                    comb_ov = {
                        "card_overrides": {
                            **m1[2]["card_overrides"],
                            **m2[2]["card_overrides"],
                        }
                    }
                    combos.append((comb_id, comb_name, comb_ov))
        candidates.extend(combos)

    # Align candidate count to a multiple of 10 for 100% CPU thread efficiency
    remainder = len(candidates) % 10
    if remainder != 0:
        needed = 10 - remainder
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


def update_balance_notes_entry(
    old_version: str,
    new_version: str,
    change_desc: str,
    rule_id: str,
    base_score: float,
    best_score: float,
    best_res: dict[str, Any],
):
    """Adds entry to playtesting/balance-notes.md."""
    if not BALANCE_NOTES_PATH.exists():
        return
    content = BALANCE_NOTES_PATH.read_text(encoding="utf-8")
    today = datetime.now().strftime("%Y-%m-%d")
    d_4p = best_score - base_score
    delta_str = f"+{d_4p:.2f}" if d_4p > 0 else f"{d_4p:.2f}"

    block = (
        f"### 🟢 Patch {new_version} ({today}) — Celowany Rework Kart Problemowych: {change_desc} (Zysk 4P Δ {delta_str} pkt)\n"
        f"- **Wynik 4P (win share):** **`{best_score:.1f} pkt`** (baza `{base_score:.1f} pkt`)\n"
        f"- **Modyfikacja (`{rule_id}`):** {change_desc}.\n"
        f"- **Efekt:** Naprawa zidentyfikowanych kart problematycznych (Autopodatki / Disruptory). "
        f"Telemetria: Średnia Er {best_res['eras_avg']:.2f}, Deadlocks {best_res['deadlock_pct']:.1f}%, Pas Biedy {best_res['poverty_pct']:.1f}%.\n\n"
    )

    history_heading = "## 📜 Chronologiczna Historia Zmian Balansu (Faza Prototypowa — Patch Notes)\n\n"
    if history_heading in content:
        content = content.replace(history_heading, history_heading + block, 1)
    BALANCE_NOTES_PATH.write_text(content, encoding="utf-8")


class ProblemCardOptimizer:
    def __init__(self, args: argparse.Namespace):
        self.args = args
        self.total_iterations = 0
        self.start_time = time.time()

    def run(self):
        print("═══════════════════════════════════════════════════════════════")
        print("   INQUISITIO-1492 — AUDYTOR KART PROBLEMOWYCH W KANONIE 4P    ")
        print("      Autonomiczna Pętla Optymalizacji Autopodatków i Wad      ")
        print(f"      Wersja: {CONFIG.version} | Ziarno: {self.args.seed}      ")
        print("═══════════════════════════════════════════════════════════════\n")

        current_phase = 1

        while True:
            if self.args.hours and (time.time() - self.start_time) >= self.args.hours * 3600:
                print(f"⏱️ Osiągnięto limit czasu ({self.args.hours}h). Kończę sesję.")
                break

            if self.args.max_iters and self.total_iterations >= self.args.max_iters:
                print(f"🛑 Osiągnięto maksymalną liczbę iteracji ({self.args.max_iters}). Kończę sesję.")
                break

            iter_start = time.time()
            print(f"\n───────────────────────────────────────────────────────────────")
            print(f"🔄 [ITERACJA #{self.total_iterations + 1} — FAZA {current_phase}D] Badam karty problematyczne...")
            print(f"───────────────────────────────────────────────────────────────")

            # 1. Detect Problematic Cards for current version
            problem_cards = parse_or_detect_problematic_cards(games_screen=1000, seed=self.args.seed)
            print(f"🎯 Zidentyfikowano {len(problem_cards)} problematycznych kart w wersji {CONFIG.version}:")
            for cid, info in sorted(problem_cards.items()):
                print(f"   • {cid:<7s} ({info['name']:<25s}): {info['role']}")
            print()

            if not problem_cards:
                print("🎉 Wszystkie karty w Kanonie 4P są zbalansowane i zdrowe! Brak problematycznych kart.")
                break

            # 2. Measure Base Score
            print("📊 Mierzę stan bazowy Kanonu 4P (3000 gier/setup)...")
            base_res = _run_single_task(("BASE", "Baza", {}, 3000, self.args.seed, CANONICAL_4P_SETUPS))
            base_score = base_res["score"]
            print(f"   🎯 Bieżący 4P Score: {color_score(base_score, bold=True)} pkt")
            print(f"   📊 Udziały: {', '.join(f'{k}: {v:.1f}%' for k, v in sorted(base_res['faction_shares'].items()))}\n")

            if base_score >= 100.0:
                print(f"🏆 Wynik Kanonu 4P osiągnął absolutne 100.0 pkt! Balans doskonały.")
                break

            # 3. Generate Candidate Mutations
            include_2d = (current_phase >= 2)
            candidates = generate_targeted_candidate_mutations(
                problem_cards,
                include_2d_combos=include_2d,
                base_res=base_res,
            )
            print(f"🔧 Pula kandydatów: {len(candidates)} mutacji (Faza {current_phase}D, mod 10: {len(candidates)%10 == 0})\n")

            # 4. Lejek Selekcyjny
            # Etap 1: Szybki Przesiew (1000 gier/setup)
            print(f"⏳ [Etap 1/2: Przesiew] Testuję {len(candidates)} kandydatów (1000 gier/setup)...")
            tasks_stage1 = [(c[0], c[1], c[2], 1000, self.args.seed, CANONICAL_4P_SETUPS) for c in candidates]
            with ProcessPoolExecutor(max_workers=min(10, len(tasks_stage1), os.cpu_count() or 4)) as ex:
                res_stage1 = list(ex.map(_run_single_task, tasks_stage1))

            res_stage1.sort(key=lambda r: r["score"], reverse=True)
            top_n = min(20, (len(res_stage1) // 10) * 10 or 10)
            top_candidates = res_stage1[:top_n]

            print(f"✔ Wyłoniono TOP {top_n} finalistów do Etapu 2:")
            for idx, r in enumerate(top_candidates[:5], 1):
                delta = r["score"] - base_score
                print(f"   {idx:2d}. {r['id']:<32s} Score: {color_score(r['score'])} pkt (Δ {delta:+5.2f} pkt) | {r['name']}")
            print()

            # Etap 2: Głęboka Weryfikacja (5000 gier/setup)
            print(f"⏳ [Etap 2/2: Weryfikacja Ultra] Badam TOP {top_n} finalistów (5000 gier/setup)...")
            tasks_stage2 = [(r["id"], r["name"], r["overrides"], 5000, self.args.seed, CANONICAL_4P_SETUPS) for r in top_candidates]
            with ProcessPoolExecutor(max_workers=min(10, len(tasks_stage2), os.cpu_count() or 4)) as ex:
                res_stage2 = list(ex.map(_run_single_task, tasks_stage2))

            res_stage2.sort(key=lambda r: r["score"], reverse=True)
            best = res_stage2[0]
            best_delta = best["score"] - base_score

            print("\n═══════════════════════════════════════════════════════════════")
            print(f"🏆 LIDER ITERACJI #{self.total_iterations + 1}:")
            print(f"   ID:       {best['id']}")
            print(f"   Opis:     {best['name']}")
            print(f"   4P Score: {color_score(base_score)} → {color_score(best['score'], bold=True)} pkt (Zysk: {best_delta:+5.2f} pkt)")
            print(f"   Rozkład:  {', '.join(f'{k}: {v:.1f}%' for k, v in sorted(best['faction_shares'].items()))}")
            print(f"   Telemetria: Śr. Er {best['eras_avg']:.2f} | Deadlocks: {best['deadlock_pct']:.1f}% | Pas Biedy: {best['poverty_pct']:.1f}%")
            print("═══════════════════════════════════════════════════════════════\n")

            # 5. Generowanie i Zapis Raportu
            report_lines = [
                f"# Raport Audytora Kart Problemowych 4P — Wersja Balansu: {CONFIG.version}",
                "",
                f"**Wersja:** `{CONFIG.version}` | **Data:** {datetime.now().strftime('%Y-%m-%d %H:%M')} | **Próba:** 5000 gier/setup | **Ziarno:** {self.args.seed}",
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

            # 6. Apply or Loop Decision
            if best_delta >= self.args.min_delta:
                if self.args.apply:
                    with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
                        raw_cfg = yaml.safe_load(f)
                    old_ver = raw_cfg.get("version", "v1.0")
                    mod_cfg, change_desc = apply_mutation_to_config(raw_cfg, best["id"], best["overrides"])
                    new_ver, _ = save_config_and_bump_version(mod_cfg, _CONFIG_PATH, bump_version=True)

                    # Update balance notes and sync
                    update_balance_notes_entry(old_ver, new_ver, change_desc, best["id"], base_score, best["score"], best)
                    subprocess.run([sys.executable, str(TOOLS_SIM_DIR.parent / "sync_config.py")])
                    print(f"\n🎉 [ZAAKCEPTOWANO PATCH KART #{self.total_iterations + 1}] `{old_ver}` → **`{new_ver}`** ({change_desc})")
                    self.total_iterations += 1
                    current_phase = 1
                else:
                    print(f"\n[DRY RUN] Zaakceptowano by mutację {best['id']}. Przechodzę do kolejnej iteracji.")
                    self.total_iterations += 1
                    current_phase = 1
            else:
                if current_phase == 1:
                    print(f"\n⚪ Brak pojedynczej mutacji 1D dającej zysk ≥ {self.args.min_delta:.2f} pkt. ESKALUJĘ DO KOMBINACJI 2D...")
                    current_phase = 2
                else:
                    print(f"\n🛑 Przestrzeń mutacji kart problematycznych wyczerpana (brak dalszego zysku w 1D i 2D).")
                    break

        total_elapsed = round(time.time() - self.start_time, 1)
        print(f"\n═══════════════════════════════════════════════════════════════")
        print(f"   AUDYTOR KART PROBLEMOWYCH ZAKOŃCZYŁ SESJĘ.")
        print(f"   Wprowadzono łącznie {self.total_iterations} udanych patchów w {total_elapsed}s ({round(total_elapsed/60, 1)} min).")
        print(f"═══════════════════════════════════════════════════════════════\n")


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 — Audytor Kart Problemowych 4P (Continuous Optimizer)")
    parser.add_argument("--dry-run", action="store_true", help="Tylko symulacja bez zapisu zmian do game_config.yaml")
    parser.add_argument("--apply", action="store_true", help="Automatycznie aplikuj każdy udany patch do game_config.yaml i zapętlaj")
    parser.add_argument("--max-iters", type=int, default=None, help="Maksymalna liczba udanych patchów")
    parser.add_argument("--hours", type=float, default=None, help="Maksymalny czas działania w godzinach")
    parser.add_argument("--min-delta", type=float, default=0.10, help="Minimalny zysk 4P Score wymagany do zatwierdzenia patcha (pkt, domyślnie: 0.10)")
    parser.add_argument("--seed", type=int, default=42, help="RNG seed")
    args = parser.parse_args()

    optimizer = ProblemCardOptimizer(args)
    optimizer.run()


if __name__ == "__main__":
    main()
