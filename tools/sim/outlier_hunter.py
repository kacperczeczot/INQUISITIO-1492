#!/usr/bin/env python3
"""INQUISITIO-1492 — OUTLIER HUNTER (Optymalizator Wielowymiarowy 2D/3D).

Specjalistyczny optymalizator balansu stworzony do przełamywania plateau.
Zamiast pojedynczych mutacji (1D), generuje i testuje:
  1. Antagonistyczne Pary 2D (Nerf Dominanta + Buff Frakcji Deficytowej w danym setupie)
  2. Wewnątrzfrakcyjne Pary Przesunięć (Rebalans talii frakcji)
  3. Hybrydy Karta + Reguła Systemowa (L3 + L1/L2)
  4. Wiązki Sukcesywne 3D (Top 2D + Mikro-korekta systemowa)

Algorytm działa w 2-etapowym sicie:
  Etap 1: Przesiew na zapalnym setupie (min. 1000 gier)
  Etap 2: Weryfikacja Ultra na wszystkich 16 setupach (min. 5000 gier, CRN)

Przystosowany do wielogodzinnej pracy ciągłej (np. na noc).
"""
from __future__ import annotations

import argparse
import copy
import itertools
import os
import re
import shutil
import signal
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
from inquisitio.runner.audit_facts import score_pair, save_and_archive_report
from inquisitio.runner.batch import run_batch
from inquisitio.runner.scoring import (
    calculate_category_scores,
    calculate_global_score,
    calculate_setup_score,
    color_score,
)

# Test builders for hybrid combinations
import audit_level1
import audit_level2

REPORTS_DIR = Path(__file__).resolve().parent.parent.parent / "playtesting" / "sim-reports"
LOG_FILE_PATH = REPORTS_DIR / "outlier_hunter_log.md"
BALANCE_NOTES_PATH = Path(__file__).resolve().parent.parent.parent / "playtesting" / "balance-notes.md"

FACTION_NAMES = {
    FactionId.SWIETE_OFICJUM: "SO",
    FactionId.CIENIE_AL_ANDALUS: "CAA",
    FactionId.KORONA_BORGIOWIE: "KB",
    FactionId.KABALA_TOLEDO: "KT",
    FactionId.GILDIA_CIENI: "GC",
}

PREFIX_TO_FACTION_ID = {
    "so": FactionId.SWIETE_OFICJUM,
    "caa": FactionId.CIENIE_AL_ANDALUS,
    "kb": FactionId.KORONA_BORGIOWIE,
    "kt": FactionId.KABALA_TOLEDO,
    "gc": FactionId.GILDIA_CIENI,
}

FACTION_ID_TO_PREFIX = {v: k for k, v in PREFIX_TO_FACTION_ID.items()}


def passes_telemetry_safety(res: dict) -> tuple[bool, str]:
    """Verify that candidate results stay within safety margins."""
    if res.get("deadlock_pct", 0) > 5.0:
        return False, f"Deadlock {res['deadlock_pct']:.1f}% > 5.0%"
    if res.get("poverty_pct", 0) > 30.0:
        return False, f"Pas Biedy {res['poverty_pct']:.1f}% > 30.0%"
    eras = res.get("eras_avg", 5.5)
    if eras < 4.5 or eras > 7.0:
        return False, f"Śr. Er {eras:.2f} poza zakresem [4.5, 7.0]"
    return True, "OK"


def _run_single_setup_task(task_args: tuple[tuple[str, str, dict], int, int, str]) -> dict:
    """Execute a candidate on a single targeted setup."""
    (rule_id, rule_name, rule_params), games, seed, setup_name = task_args
    t0 = time.time()

    summary = run_batch(
        games=games,
        setup=setup_name,
        seed=seed,
        layer="C",
        win_overrides=rule_params,
    )
    score = calculate_setup_score(summary)
    dt = round(time.time() - t0, 2)

    factions = SETUP_PRESETS[setup_name]
    shares = {}
    for fid in factions:
        fname = FACTION_NAMES[fid]
        w_count = summary.wins.get(fid, 0)
        shares[fname] = round((w_count / summary.games) * 100.0, 1)

    deadlock_pct = summary.eras_limit_pct * 100.0
    poverty_pct = summary.passes_forced_pct * 100.0
    eras_avg = summary.eras_avg

    return {
        "id": rule_id,
        "name": rule_name,
        "params": rule_params,
        "setup": setup_name,
        "setup_score": score,
        "shares": shares,
        "deadlock_pct": deadlock_pct,
        "poverty_pct": poverty_pct,
        "eras_avg": eras_avg,
        "dt": dt,
    }


def _run_full_16_setups_task(task_args: tuple[tuple[str, str, dict], int, int, list[str]]) -> dict:
    """Execute a candidate on all 16 setups."""
    (rule_id, rule_name, rule_params), games_per_setup, seed, setups = task_args
    t_start = time.time()

    summaries = []
    setup_scores = {}
    for sname in setups:
        summary = run_batch(
            games=games_per_setup,
            setup=sname,
            seed=seed,
            layer="C",
            win_overrides=rule_params,
        )
        summaries.append(summary)
        setup_scores[sname] = calculate_setup_score(summary)

    cat_scores = calculate_category_scores(summaries)
    global_score = calculate_global_score(cat_scores)
    dt = round(time.time() - t_start, 2)

    n_sum = len(summaries)
    eras_avg = sum(s.eras_avg for s in summaries) / n_sum
    deadlock_pct = (sum(s.eras_limit_pct for s in summaries) / n_sum) * 100.0
    poverty_pct = (sum(s.passes_forced_pct for s in summaries) / n_sum) * 100.0
    autodafe_avg = sum(s.autodafe_avg for s in summaries) / n_sum
    acc_avg = sum(s.accusations_avg for s in summaries) / n_sum

    min_setup_name = min(setup_scores, key=setup_scores.get)
    min_setup_score = setup_scores[min_setup_name]

    return {
        "id": rule_id,
        "name": rule_name,
        "params": rule_params,
        "global_score": global_score,
        "cat_scores": cat_scores,
        "setup_scores": setup_scores,
        "min_setup": (min_setup_name, min_setup_score),
        "dt": dt,
        "eras_avg": eras_avg,
        "deadlock_pct": deadlock_pct,
        "poverty_pct": poverty_pct,
        "autodafe_avg": autodafe_avg,
        "acc_avg": acc_avg,
    }


def generate_atomic_card_mutations(faction_prefix: str) -> list[tuple[str, str, dict]]:
    """Build all atomic card mutations (+-1 cost, +-1 heresy, +-1 gold, +-1 target_heresy) for a faction."""
    cards = load_all_cards()
    mutations = []

    for cid, c in sorted(cards.items()):
        if not cid.startswith(f"{faction_prefix}-"):
            continue

        # 1. Cost (+1 / -1)
        cost = getattr(c, "cost", 0)
        mutations.append((f"{cid}_cost+1", f"{cid.upper()} koszt {cost}→{cost+1}", {cid: {"cost": cost + 1}}))
        if cost > 0:
            mutations.append((f"{cid}_cost-1", f"{cid.upper()} koszt {cost}→{cost-1}", {cid: {"cost": cost - 1}}))

        # 2. Heresy (+1 / -1)
        heresy = getattr(c, "heresy", 0)
        mutations.append((f"{cid}_heresy+1", f"{cid.upper()} herezja {heresy}→{heresy+1}", {cid: {"heresy": heresy + 1}}))
        if heresy > 0:
            mutations.append((f"{cid}_heresy-1", f"{cid.upper()} herezja {heresy}→{heresy-1}", {cid: {"heresy": heresy - 1}}))

        # 3. Gold (+1 / -1) if card has gold property
        gold = getattr(c, "gold", 0)
        if gold > 0:
            mutations.append((f"{cid}_gold+1", f"{cid.upper()} złoto {gold}→{gold+1}", {cid: {"gold": gold + 1}}))
            if gold > 1:
                mutations.append((f"{cid}_gold-1", f"{cid.upper()} złoto {gold}→{gold-1}", {cid: {"gold": gold - 1}}))

        # 4. Target Heresy (+1 / -1) if card has target_heresy property
        target_heresy = getattr(c, "target_heresy", 0)
        if target_heresy > 0:
            mutations.append((f"{cid}_tgheresy+1", f"{cid.upper()} wrobienie {target_heresy}→{target_heresy+1}", {cid: {"target_heresy": target_heresy + 1}}))
            if target_heresy > 1:
                mutations.append((f"{cid}_tgheresy-1", f"{cid.upper()} wrobienie {target_heresy}→{target_heresy-1}", {cid: {"target_heresy": target_heresy - 1}}))

    return mutations


def classify_card_mutation_intent(mut_tuple: tuple[str, str, dict]) -> str:
    """Classify whether an atomic mutation is a BUFF, NERF, or SHIFT."""
    tag, _, pdict = mut_tuple
    cid = list(pdict.keys())[0]
    param = list(pdict[cid].keys())[0]
    val = pdict[cid][param]
    
    cards = load_all_cards()
    orig = getattr(cards.get(cid), param, 0)

    if param == "cost":
        return "BUFF" if val < orig else "NERF"
    elif param == "heresy":
        return "BUFF" if val < orig else "NERF"
    elif param in ("gold", "target_heresy"):
        return "BUFF" if val > orig else "NERF"
    return "NEUTRAL"


def merge_card_mutations(m1: tuple[str, str, dict], m2: tuple[str, str, dict]) -> tuple[str, str, dict]:
    """Merge two atomic card mutations into a single 2D composite candidate."""
    id1, name1, pdict1 = m1
    id2, name2, pdict2 = m2

    combined_id = f"PAIR_{id1}__{id2}"
    combined_name = f"{name1} + {name2}"

    merged_overrides = copy.deepcopy(pdict1)
    for cid, params in pdict2.items():
        if cid in merged_overrides:
            merged_overrides[cid].update(params)
        else:
            merged_overrides[cid] = copy.deepcopy(params)

    return (combined_id, combined_name, {"card_overrides": merged_overrides})


def generate_antagonist_and_synergy_pairs(
    setup_name: str,
    shares: dict[str, float],
    ideal_share: float,
) -> list[tuple[str, str, dict]]:
    """Generates focused 2D pairs based on the deviations of factions in this setup."""
    factions = SETUP_PRESETS[setup_name]
    pairs: list[tuple[str, str, dict]] = []

    dominant_prefixes = []
    struggling_prefixes = []

    for fid in factions:
        fname = FACTION_NAMES[fid]
        pref = FACTION_ID_TO_PREFIX[fid]
        share = shares.get(fname, ideal_share)
        dev = share - ideal_share
        if dev >= 1.5:
            dominant_prefixes.append((pref, dev))
        elif dev <= -1.5:
            struggling_prefixes.append((pref, dev))

    dominant_prefixes.sort(key=lambda x: x[1], reverse=True)
    struggling_prefixes.sort(key=lambda x: x[1])

    # If no clear dominant/struggling split, pick top and bottom faction
    if not dominant_prefixes or not struggling_prefixes:
        all_sorted = sorted([(FACTION_ID_TO_PREFIX[fid], shares.get(FACTION_NAMES[fid], ideal_share) - ideal_share) for fid in factions], key=lambda x: x[1])
        struggling_prefixes = [all_sorted[0]]
        dominant_prefixes = [all_sorted[-1]]

    # 1. Antagonist Pairs: Nerf Dominant + Buff Struggling
    for dom_pref, _ in dominant_prefixes:
        dom_muts = generate_atomic_card_mutations(dom_pref)
        dom_nerfs = [m for m in dom_muts if classify_card_mutation_intent(m) == "NERF"]

        for strug_pref, _ in struggling_prefixes:
            strug_muts = generate_atomic_card_mutations(strug_pref)
            strug_buffs = [m for m in strug_muts if classify_card_mutation_intent(m) == "BUFF"]

            for m_nerf in dom_nerfs:
                for m_buff in strug_buffs:
                    pairs.append(merge_card_mutations(m_nerf, m_buff))

    # 2. Intra-Faction Shift Pairs: 1 Buff + 1 Nerf in Dominant faction
    for dom_pref, _ in dominant_prefixes:
        dom_muts = generate_atomic_card_mutations(dom_pref)
        dom_nerfs = [m for m in dom_muts if classify_card_mutation_intent(m) == "NERF"]
        dom_buffs = [m for m in dom_muts if classify_card_mutation_intent(m) == "BUFF"]

        for m_nerf in dom_nerfs:
            for m_buff in dom_buffs:
                # Ensure different cards
                cid1 = list(m_nerf[2].keys())[0]
                cid2 = list(m_buff[2].keys())[0]
                if cid1 != cid2:
                    pairs.append(merge_card_mutations(m_nerf, m_buff))

    # 3. Hybrid Pairs: Card Nerf/Buff + System Rule (Level 1 / Level 2 tweaks)
    l1_rules = [t for t in audit_level1.build_level1_tests() if t[0] != "L1_BAZA"]
    l2_rules = [t for t in audit_level2.build_level2_tests() if t[0] != "L2_BAZA"]
    sys_rules = l1_rules + l2_rules

    # Add a selected subset of high-impact hybrid pairs
    for dom_pref, _ in dominant_prefixes:
        dom_nerfs = [m for m in generate_atomic_card_mutations(dom_pref) if classify_card_mutation_intent(m) == "NERF"]
        for m_nerf in dom_nerfs[:5]:  # Top 5 representative nerfs
            for s_rule in sys_rules[:6]:  # Top 6 system rules
                s_id, s_name, s_params = s_rule
                cid = list(m_nerf[2].keys())[0]
                combined_id = f"HYBRID_{m_nerf[0]}__{s_id}"
                combined_name = f"{m_nerf[1]} + {s_name}"
                merged_params = copy.deepcopy(s_params)
                merged_params["card_overrides"] = copy.deepcopy(m_nerf[2])
                pairs.append((combined_id, combined_name, merged_params))

    # Deduplicate by rule_id
    seen = set()
    unique_pairs = []
    for p in pairs:
        if p[0] not in seen:
            seen.add(p[0])
            unique_pairs.append(p)

    return unique_pairs


def log_outlier_iteration(
    log_path: Path,
    iteration: int,
    old_ver: str,
    new_ver: str,
    target_setup: str,
    old_setup_score: float,
    new_setup_score: float,
    old_glob: float,
    new_glob: float,
    desc: str,
    rule_id: str,
    elapsed: float,
):
    """Appends an iteration log entry to outlier_hunter_log.md."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    if not log_path.exists():
        headers = [
            "# Dziennik Optymalizacji Outlier Hunter (2D/3D Multi-Mutation)",
            "",
            "Rejestr naprawionych setupów odstających i postępów w kierunku równomiernego balansu 100%.",
            "",
            "| Iteracja | Data i Czas | Wersja | Celowany Setup | Wynik Setupu | Global Score | Wprowadzona Para / Trójka | Czas |",
            "| :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: |",
        ]
        log_path.write_text("\n".join(headers) + "\n", encoding="utf-8")

    d_setup = new_setup_score - old_setup_score
    d_glob = new_glob - old_glob
    ds_str = f"+{d_setup:.1f}" if d_setup > 0 else f"{d_setup:.1f}"
    dg_str = f"+{d_glob:.1f}" if d_glob > 0 else f"{d_glob:.1f}"

    setup_col = f"{old_setup_score:.1f} → **{new_setup_score:.1f}** (`{ds_str}`)"
    glob_col = f"{old_glob:.1f} → **{new_glob:.1f}** (`{dg_str}`)"

    row = (
        f"| #{iteration} | {datetime.now().strftime('%Y-%m-%d %H:%M')} | `{old_ver}` → `{new_ver}` | "
        f"`{target_setup}` | {setup_col} | {glob_col} | **{desc}** (`{rule_id}`) | {elapsed:.1f}s |"
    )

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(row + "\n")


class OutlierHunter:
    def __init__(self, args: argparse.Namespace):
        self.args = args
        self.stop_requested = False
        self.total_iterations = 0
        self.start_time = time.time()
        self.initial_version = CONFIG.version
        signal.signal(signal.SIGINT, self._handle_sigint)

    def _handle_sigint(self, signum, frame):
        print("\n\n⚠️ Otrzymano sygnał przerwania (Ctrl+C). Bezpiecznie kończę bieżącą iterację...")
        self.stop_requested = True

    def _execute_pool(self, task_func, task_list: list) -> list[dict]:
        workers = min(self.args.workers, len(task_list))
        if workers <= 1:
            return [task_func(t) for t in task_list]
        with ProcessPoolExecutor(max_workers=workers) as executor:
            return list(executor.map(task_func, task_list))

    def run(self):
        print("═══════════════════════════════════════════════════════════════════════")
        print("     INQUISITIO-1492 — OUTLIER HUNTER (2D/3D Multi-Mutation Search)    ")
        print("  Celowana optymalizacja zapalnych setupów z globalną ochroną balansu  ")
        print("═══════════════════════════════════════════════════════════════════════")
        print(f"Bieżąca wersja bazowa:  {CONFIG.version}")
        print(f"Maksymalny czas sesji:  {self.args.hours if self.args.hours else 'Brak limitu (do optimum)'} godz.")
        print(f"Maksymalnie iteracji:   {self.args.max_iters if self.args.max_iters else 'Brak (do optimum)'}")
        print(f"Przesiew setupu (Etap1): {self.args.fast_games} gier (min. 1000)")
        print(f"Weryfikacja 16s (Etap2): {self.args.confirm_games} gier/setup ({self.args.confirm_games * 16} gier/kandydat)")
        print(f"Wątki procesora:        {self.args.workers}")
        print(f"Dziennik operacji:      {LOG_FILE_PATH}")
        print("═══════════════════════════════════════════════════════════════════════\n")

        setups = sorted(SETUP_PRESETS.keys())
        time_limit_sec = (self.args.hours * 3600) if self.args.hours else None

        while not self.stop_requested:
            # 1. Check time / iteration limit
            if time_limit_sec and (time.time() - self.start_time) >= time_limit_sec:
                print(f"\n⏱️ Osiągnięto limit czasu sesji ({self.args.hours}h). Kończę pracę.")
                break

            if self.args.max_iters and self.total_iterations >= self.args.max_iters:
                print(f"\n🔢 Osiągnięto maksymalną liczbę udanych iteracji ({self.args.max_iters}). Kończę pracę.")
                break

            # 2. Run initial/current 16-setup baseline measurement
            print(f"\n{'='*71}")
            print(f"🔍 [POMIAR BAZOWY] Diagnoza wszystkich 16 setupów (Próba: {self.args.confirm_games} gier/setup)...")
            base_task = ((("BASE", "Bieżący stan gry", {}), self.args.confirm_games, self.args.seed, setups),)
            base_res = self._execute_pool(_run_full_16_setups_task, [base_task[0]])[0]

            print(f"   📊 Global Balance Score: {color_score(base_res['global_score'], bold=True)} pkt")
            print(f"   🎯 3p: {base_res['cat_scores'].get('3p',0):.1f} | 4p: {base_res['cat_scores'].get('4p',0):.1f} | 5p: {base_res['cat_scores'].get('5p',0):.1f} pkt")

            # 3. Find and rank outlier setups
            sorted_setups = sorted(base_res["setup_scores"].items(), key=lambda x: x[1])
            weak_setups = [s for s in sorted_setups if s[1] < 90.0]

            print(f"\n📋 Status Setupów:")
            for sname, score in sorted_setups[:5]:
                print(f"   • `{sname}`: {color_score(score, bold=True)} pkt")

            if not weak_setups and base_res["global_score"] >= 98.0:
                print(f"\n🏆 WSZYSTKIE 16 SETUPÓW OSIĄGNĘŁY SCORE ≥ 90, A GLOBAL WYNOSI {base_res['global_score']:.1f} pkt!")
                print("   Osiągnięto idealny stan balansu gry. Gratulacje!")
                break

            # Pick target setup (lowest scoring setup)
            target_setup_name, target_setup_score = sorted_setups[0]
            factions = SETUP_PRESETS[target_setup_name]
            n_players = len(factions)
            ideal_share = 100.0 / n_players

            # Quick measure of shares in target setup
            s_task = (("BASE", "Base", {}), self.args.fast_games, self.args.seed, target_setup_name)
            s_diag = _run_single_setup_task(s_task)

            print(f"\n🎯 [CEL OPTYMALIZACJI] Zapalny setup: `{target_setup_name}` (Score: {color_score(target_setup_score, bold=True)} pkt)")
            shares_str = " | ".join([f"{f}: {s_diag['shares'].get(f, 0)}% (ideal {ideal_share:.1f}%)" for f in [FACTION_NAMES[fid] for fid in factions]])
            print(f"   Rozkład szans: {shares_str}")

            # 4. Generate Antagonist 2D & Hybrid Pairs for target setup
            candidate_pairs = generate_antagonist_and_synergy_pairs(target_setup_name, s_diag["shares"], ideal_share)
            print(f"   🧬 Wygenerowano {len(candidate_pairs)} ukierunkowanych par antagonistycznych/hybrydowych.")

            # 5. ETAP 1: Szybki Przesiew na Target Setupie (min. 1000 gier)
            print(f"\n--- [ETAP 1/2: PRZESIEW LOKALNY] Testuję {len(candidate_pairs)} par na `{target_setup_name}` ({self.args.fast_games} gier) ---")
            stage1_tasks = [(p, self.args.fast_games, self.args.seed, target_setup_name) for p in candidate_pairs]
            stage1_results = self._execute_pool(_run_single_setup_task, stage1_tasks)

            # Filter candidates that improve target setup and are telemetry safe
            promising_candidates = []
            for r in stage1_results:
                d_setup = r["setup_score"] - target_setup_score
                is_safe, safe_msg = passes_telemetry_safety(r)
                if is_safe and d_setup >= self.args.min_worst_delta:
                    promising_candidates.append((r, d_setup))

            promising_candidates.sort(key=lambda x: x[1], reverse=True)

            if not promising_candidates:
                print(f"⚠️ Żadna para 2D nie przyniosła zysku na setupie `{target_setup_name}`. Sprawdzam kolejny setup...")
                if len(sorted_setups) > 1 and sorted_setups[1][1] < 90.0:
                    # Move to second worst setup
                    target_setup_name, target_setup_score = sorted_setups[1]
                    continue
                else:
                    print("Brak dalszych kandydatów do poprawy w tej iteracji.")
                    break

            top_candidates = promising_candidates[: self.args.top_k]
            print(f"\n--- [ETAP 2/2: WERYFIKACJA ULTRA (16 SETUPÓW)] Sprawdzam TOP {len(top_candidates)} liderów na pełnej próbie {self.args.confirm_games} gier/setup ---")

            pair_dict = {p[0]: p for p in candidate_pairs}
            verify_tests = [pair_dict[c[0]["id"]] for c in top_candidates]

            verify_tasks = [(t, self.args.confirm_games, self.args.seed, setups) for t in verify_tests]
            verified_results = self._execute_pool(_run_full_16_setups_task, verify_tasks)

            # Evaluate against baseline
            accepted_candidate = None
            best_ver_res = None
            best_composite_gain = -999.0

            for ver_res in verified_results:
                new_target_score = ver_res["setup_scores"].get(target_setup_name, 0.0)
                d_target = new_target_score - target_setup_score
                d_global = ver_res["global_score"] - base_res["global_score"]
                is_safe, safe_msg = passes_telemetry_safety(ver_res)

                # Composite score: target improvement + global gain
                composite_gain = d_target + (d_global * 2.0)

                print(f"   ▶ [{ver_res['id'][:35]}...] Target: {target_setup_score:.1f} → {new_target_score:.1f} (Δ {d_target:+5.1f}) | Global: {base_res['global_score']:.1f} → {ver_res['global_score']:.1f} (Δ {d_global:+5.2f}) | {safe_msg}")

                if is_safe and d_target >= self.args.min_worst_delta and d_global >= self.args.min_global_delta:
                    if composite_gain > best_composite_gain:
                        best_composite_gain = composite_gain
                        accepted_candidate = pair_dict[ver_res["id"]]
                        best_ver_res = ver_res

            if not accepted_candidate or best_ver_res is None:
                print(f"\n⚪ Brak pary, która poprawiłaby setup `{target_setup_name}` bez regresji w pozostałych setupach.")
                break

            # 6. Apply Accepted Modification to game_config.yaml
            self.total_iterations += 1
            rule_id, rule_name, rule_params = accepted_candidate

            with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
                raw_cfg = yaml.safe_load(f)

            old_version = raw_cfg.get("version", "v0.29")
            mod_cfg, change_desc = apply_mutation_to_config(raw_cfg, rule_id, rule_params)

            if self.args.dry_run:
                print(f"\n[DRY RUN] Zaakceptowano by modyfikację: {change_desc}")
                print(f"[DRY RUN] Nowy wynik setupu: {best_ver_res['setup_scores'][target_setup_name]:.1f} | Nowy Global: {best_ver_res['global_score']:.1f}")
                break
            else:
                new_version, saved_path = save_config_and_bump_version(mod_cfg, _CONFIG_PATH, bump_version=True)
                iter_time = round(time.time() - self.start_time, 1)

                print(f"\n🎉 [ZAAKCEPTOWANO PATCH #{self.total_iterations}]")
                print(f"   Wersja:        `{old_version}` → **`{new_version}`**")
                print(f"   Modyfikacja:   {change_desc}")
                print(f"   Setup `{target_setup_name}`: {target_setup_score:.1f} → **{best_ver_res['setup_scores'][target_setup_name]:.1f} pkt** (Δ {best_ver_res['setup_scores'][target_setup_name] - target_setup_score:+.1f} pkt)")
                print(f"   Global Score:  {base_res['global_score']:.1f} → **{best_ver_res['global_score']:.1f} pkt** (Δ {best_ver_res['global_score'] - base_res['global_score']:+.2f} pkt)")

                # Log to outlier_hunter_log.md
                log_outlier_iteration(
                    LOG_FILE_PATH,
                    self.total_iterations,
                    old_version,
                    new_version,
                    target_setup_name,
                    target_setup_score,
                    best_ver_res["setup_scores"][target_setup_name],
                    base_res["global_score"],
                    best_ver_res["global_score"],
                    change_desc,
                    rule_id,
                    iter_time,
                )

                # Synchronize documentation and cards
                print("   🔄 Synchronizuję dokumentację kart i reguł...")
                subprocess.run([sys.executable, str(TOOLS_SIM_DIR.parent / "sync_config.py")], stdout=subprocess.DEVNULL)
                print("   ✔ Zaktualizowano katalog kart, opisy markdown i card-editor.")

        print(f"\n═══════════════════════════════════════════════════════════════════════")
        print(f"   OUTLIER HUNTER ZAKOŃCZYŁ SESJĘ. ŁĄCZNIE WPROWADZONO {self.total_iterations} PATCHY.")
        print(f"═══════════════════════════════════════════════════════════════════════\n")


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 Outlier Hunter — 2D/3D Multi-Mutation Balance Optimizer")
    parser.add_argument("--hours", type=float, default=None, help="Maksymalny czas działania w godzinach (np. 8.0 na noc)")
    parser.add_argument("--max-iters", type=int, default=None, help="Maksymalna liczba udanych patchów przed zatrzymaniem")
    parser.add_argument("--fast-games", type=int, default=1000, help="Liczba gier w Etapie 1 (przesiew na 1 setupie, min. 1000)")
    parser.add_argument("--confirm-games", type=int, default=5000, help="Liczba gier w Etapie 2 (weryfikacja 16 setupów, min. 5000)")
    parser.add_argument("--workers", type=int, default=min(os.cpu_count() or 4, 10), help="Liczba procesów równoległych")
    parser.add_argument("--seed", type=int, default=42, help="Ziarno generatora liczb losowych")
    parser.add_argument("--min-worst-delta", type=float, default=1.0, help="Minimalny zysk na zapalnym setupie (pkt)")
    parser.add_argument("--min-global-delta", type=float, default=-0.1, help="Maksymalny dopuszczalny spadek globalny (zabezpieczenie przed regresją)")
    parser.add_argument("--top-k", type=int, default=8, help="Liczba najlepszych par sprawdzanych w Etapie 2")
    parser.add_argument("--dry-run", action="store_true", help="Tryb symulacji bez zapisywania zmian do game_config.yaml")

    args = parser.parse_args()

    # Enforce user requirements: no tests below 1000 games, final tests minimum 5000
    if args.fast_games < 1000:
        print("⚠️ Podwyższam fast-games do wymaganego minimum 1000 gier.")
        args.fast_games = 1000
    if args.confirm_games < 5000:
        print("⚠️ Podwyższam confirm-games do wymaganego minimum 5000 gier.")
        args.confirm_games = 5000

    hunter = OutlierHunter(args)
    hunter.run()


if __name__ == "__main__":
    main()
