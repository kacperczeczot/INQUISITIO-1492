#!/usr/bin/env python3
"""INQUISITIO-1492 — AUDYTOR KART PROBLEMOWYCH 4P (Per-Card Multi-D Deep Dive Optimizer).

Autonomous optimizer for targeted problematic cards:
  1. Multi-dimensional combinatorial grid per card (cost, gold, heresy, target_heresy).
  2. Multi-Fidelity Adaptive Sequential Racer with Delta-Method SE and 95% CI statistical pruning.
  3. Mandatory 10,000 games/setup validation gate on standard seed.
  4. Automatic version bump, reports, and sync.

Usage:
  python3 scripts/sim/audytor_kart_problemowych.py --card kt-04
  python3 scripts/sim/audytor_kart_problemowych.py --apply
  python3 scripts/sim/audytor_kart_problemowych.py --dry-run
"""
from __future__ import annotations

import argparse
import copy
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any

TOOLS_SRC_DIR = Path(__file__).resolve().parent
SRC_DIR = TOOLS_SRC_DIR.parent.parent / "src"

for p in (TOOLS_SRC_DIR, SRC_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

import yaml
from inquisitio.cards.loader import load_all_cards
from inquisitio.config import CONFIG, _CONFIG_PATH
from inquisitio.config_updater import apply_mutation_to_config, save_config_and_bump_version
from inquisitio.engine.setup import SETUP_PRESETS, FactionId
from inquisitio.runner.adaptive_racer import (
    AdaptiveSequentialRacer,
    CandidateStats,
    extract_config_overrides,
    merge_override_dicts,
)
from inquisitio.runner.batch import run_batch
from inquisitio.runner.canon_accept import accept_candidate, rank_key
from inquisitio.runner.impact_taxonomy import classify_card_impact_4p
from inquisitio.runner.scoring import (
    calculate_category_scores,
    calculate_global_score,
    calculate_setup_score,
    color_score,
)

REPORTS_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "playtesting" / "sim-reports"
BALANCE_NOTES_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "playtesting" / "balance-notes.md"

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


def _run_full_diagnostic(rule_params: dict, games_per_setup: int = 1000, seed: int = 42) -> dict:
    """Runs a complete 16-setup diagnostic to measure 3p, 4p, 5p and global score."""
    all_setups = sorted(SETUP_PRESETS.keys())
    summaries = []
    setup_scores = {}
    for sname in all_setups:
        s = run_batch(games=games_per_setup, setup=sname, seed=seed, layer="C", win_overrides=rule_params)
        summaries.append(s)
        setup_scores[sname] = calculate_setup_score(s)

    cat_scores = calculate_category_scores(summaries)
    global_score = calculate_global_score(cat_scores)
    return {
        "global_score": global_score,
        "cat_scores": cat_scores,
        "setup_scores": setup_scores,
    }


def parse_or_detect_problematic_cards(games_screen: int = 500, seed: int = 42) -> dict[str, dict[str, Any]]:
    """Identifies problematic cards from ablation report or quick baseline screening."""
    ablation_report = REPORTS_DIR / "archive" / CONFIG.version / "raport_uzytecznosci_i_wplywu_4p.md"
    if not ablation_report.exists():
        ablation_report = REPORTS_DIR / "current" / "raport_uzytecznosci_i_wplywu_4p.md"
    if not ablation_report.exists():
        archives = sorted((REPORTS_DIR / "archive").glob("v1.0-alpha.*"), reverse=True)
        for arc in archives:
            candidate = arc / "raport_uzytecznosci_i_wplywu_4p.md"
            if candidate.exists():
                ablation_report = candidate
                break

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
            play_rate = 0.0
            try:
                play_rate = float(parts[5])
            except (ValueError, IndexError):
                pass
            role = parts[-1].strip()

            if cid not in cards:
                continue

            c = cards[cid]
            pref = cid.split("-")[0]

            if "AUTOPODATEK" in role:
                severity = 3 if play_rate >= 0.30 else 1
                problem_cards[cid] = {"id": cid, "name": name, "category": "SELF_HARM", "role": role, "card": c, "faction": pref, "severity": severity, "play_rate": play_rate}
            elif "DISRUPTOR" in role or "TOKSYCZNY" in role or "SZUM" in role:
                problem_cards[cid] = {"id": cid, "name": name, "category": "DISRUPTOR", "role": role, "card": c, "faction": pref, "severity": 2, "play_rate": play_rate}
            elif "DEAD" in role or "NISKIEGO WPŁYWU" in role or "Pasywna" in role or "NIEZAGRYWANA" in role:
                problem_cards[cid] = {"id": cid, "name": name, "category": "DEAD_WEIGHT", "role": role, "card": c, "faction": pref, "severity": 3, "play_rate": play_rate}

    if not problem_cards:
        for cid, card in sorted(cards.items()):
            pref = cid.split("-")[0]
            if pref in PREFIX_TO_FACTION_ID:
                problem_cards[cid] = {"id": cid, "name": card.name, "category": "GENERAL", "role": "Badanie ogólne", "card": card, "faction": pref, "severity": 2}

    return problem_cards


def generate_deep_reworks_for_single_card(
    cid: str,
    info: dict[str, Any],
) -> list[tuple[str, str, dict]]:
    """Generates an extensive combinatorial grid of mechanical reworks for a single card."""
    c = info["card"]
    cname = c.name
    candidates: list[tuple[str, str, dict]] = []
    seen_overrides: set[tuple[tuple[str, Any], ...]] = set()

    def _add_cand(tag: str, desc: str, card_dict: dict[str, Any]):
        sig = tuple(sorted(card_dict.items()))
        if sig in seen_overrides:
            return
        seen_overrides.add(sig)
        cid_up = cid.upper()
        candidates.append((
            f"MUT_{cid_up}_{tag}",
            f"{cid_up} ({cname}) [{desc}]",
            {"card_overrides": {cid: card_dict}},
        ))

    # Cost adjustments
    for delta in (-2, -1, 1, 2):
        new_cost = max(0, c.cost + delta)
        if new_cost != c.cost:
            _add_cand(f"COST_{new_cost}", f"koszt: {c.cost} -> {new_cost}", {"cost": new_cost})

    # Gold adjustments
    for delta in (-2, -1, 1, 2):
        new_gold = max(0, c.gold + delta)
        if new_gold != c.gold:
            _add_cand(f"GOLD_{new_gold}", f"złoto: {c.gold} -> {new_gold}", {"gold": new_gold})

    # Heresy adjustments
    for delta in (-2, -1, 1, 2):
        new_heresy = max(0, c.heresy + delta)
        if new_heresy != c.heresy:
            _add_cand(f"HERESY_{new_heresy}", f"herezja: {c.heresy} -> {new_heresy}", {"heresy": new_heresy})

    # Target heresy adjustments
    for delta in (-2, -1, 1, 2):
        new_th = max(0, c.target_heresy + delta)
        if new_th != c.target_heresy:
            _add_cand(f"TARGET_HERESY_{new_th}", f"cel herezji: {c.target_heresy} -> {new_th}", {"target_heresy": new_th})

    # 2D pairs for this card (e.g. cost + heresy, gold + cost)
    for cost_d in (-1, 0, 1):
        for heresy_d in (-1, 0, 1):
            if cost_d == 0 and heresy_d == 0:
                continue
            nc = max(0, c.cost + cost_d)
            nh = max(0, c.heresy + heresy_d)
            if nc != c.cost or nh != c.heresy:
                _add_cand(f"C{nc}_H{nh}", f"koszt: {nc}, herezja: {nh}", {"cost": nc, "heresy": nh})

    return candidates


def update_balance_notes_problem_card(
    old_version: str,
    new_version: str,
    change_desc: str,
    rule_id: str,
    base_res: dict,
    best_res: dict,
):
    """Automatically update data/playtesting/balance-notes.md with patch note entry."""
    if not BALANCE_NOTES_PATH.exists():
        return

    content = BALANCE_NOTES_PATH.read_text(encoding="utf-8")
    today = datetime.now().strftime("%Y-%m-%d")
    d_4p = best_res["score_4p_balance"] - base_res["score_4p_balance"]
    delta_str = f"+{d_4p:.2f}" if d_4p > 0 else f"{d_4p:.2f}"

    block = (
        f"### 🟢 Patch {new_version} ({today}) — Celowany Rework Karty: {change_desc} (Zysk 4P Δ {delta_str} pkt)\n"
        f"- **Wynik 4P (win share):** **`{best_res['score_4p_balance']:.1f} pkt`** (baza `{base_res['score_4p_balance']:.1f} pkt`)\n"
        f"- **Modyfikacja (`{rule_id}`):** {change_desc}.\n"
        f"- **Efekt:** Optymalizacja karty problemowej. "
        f"Telemetria: Średnia Er {best_res['eras_avg']:.2f}, Deadlocks {best_res['deadlock_pct']:.1f}%, Pas Biedy {best_res['poverty_pct']:.1f}%.\n\n"
    )

    history_heading = "## 📜 Chronologiczna Historia Zmian Balansu (Faza Prototypowa — Patch Notes)\n\n"
    if history_heading in content:
        content = content.replace(history_heading, history_heading + block, 1)
    BALANCE_NOTES_PATH.write_text(content, encoding="utf-8")


class ProblemCardOptimizer:
    def __init__(self, args: argparse.Namespace):
        self.args = args
        self.total_patches_applied = 0
        self.start_time = time.time()

    def run(self):
        print("═══════════════════════════════════════════════════════════════")
        print("   INQUISITIO-1492 — AUDYTOR KART PROBLEMOWYCH W KANONIE 4P    ")
        print("     Tryb Sekwencyjny Karta-po-Karcie (Multi-D Deep Dive)      ")
        print("═══════════════════════════════════════════════════════════════\n")

        all_problem_cards = parse_or_detect_problematic_cards(games_screen=500, seed=self.args.seed)

        if getattr(self.args, "card", None):
            req_cid = self.args.card.lower()
            if req_cid in all_problem_cards:
                all_problem_cards = {req_cid: all_problem_cards[req_cid]}
            else:
                cards = load_all_cards()
                if req_cid in cards:
                    all_problem_cards = {
                        req_cid: {
                            "id": req_cid,
                            "name": cards[req_cid].name,
                            "category": "SELF_HARM",
                            "role": "Wymuszone badanie karty",
                            "card": cards[req_cid],
                            "faction": req_cid.split("-")[0],
                            "severity": 1,
                        }
                    }

        sorted_cards = sorted(all_problem_cards.items(), key=lambda x: (x[1]["severity"], x[0]))
        print(f"🎯 Zidentyfikowano {len(sorted_cards)} kart poddanych sekwencyjnemu badaniu:\n")

        racer = AdaptiveSequentialRacer(
            setups=CANONICAL_4P_SETUPS,
            batch_step=100,
            min_games=400,
            max_games=8000,
            epsilon_indiff=0.15,
            workers=self.args.workers,
            accept_mode="legacy",
            min_delta=self.args.min_delta,
        )

        card_idx = 0
        for cid, info in sorted_cards:
            card_idx += 1
            if self.args.hours and (time.time() - self.start_time) >= self.args.hours * 3600:
                print(f"⏱️ Osiągnięto limit czasu ({self.args.hours}h). Kończę sesję.")
                break

            if self.args.max_iters and self.total_patches_applied >= self.args.max_iters:
                print(f"🛑 Osiągnięto maksymalną liczbę zatwierdzonych patchów ({self.args.max_iters}). Kończę sesję.")
                break

            print(f"\n───────────────────────────────────────────────────────────────")
            print(f"🔬 [KARTA {card_idx}/{len(sorted_cards)}] BADAM: {cid.upper()} ({info['name']})")
            print(f"   Frakcja: {FACTION_FULL_NAMES.get(info['faction'], info['faction'])} | Rola: {info['role']}")
            print(f"───────────────────────────────────────────────────────────────")

            with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
                current_raw_cfg = yaml.safe_load(f)

            curr_ver = current_raw_cfg.get("system", {}).get("version", current_raw_cfg.get("version", "v1.0-alpha.90"))
            curr_base_overrides = extract_config_overrides(current_raw_cfg)

            candidates = generate_deep_reworks_for_single_card(cid, info)
            print(f"🔧 Wygenerowano {len(candidates)} wielowymiarowych wariantów kombinatorycznych dla `{cid}`.\n")

            effective_candidates = []
            for c in candidates:
                eff_p = merge_override_dicts(curr_base_overrides, c[2])
                effective_candidates.append((c[0], c[1], eff_p))

            base_cand = ("BASE", f"Baza {curr_ver}", curr_base_overrides)
            base_stats, ranked_stats = racer.run_race(
                base_cand=base_cand,
                candidate_pool=effective_candidates,
                seed=self.args.seed,
                delta_pool=candidates,
                label_prefix=f"WYŚCIG KARTY {cid.upper()}",
            )

            surviving_stats = [c for c in ranked_stats if not c.is_pruned]
            surviving_stats.sort(key=lambda x: rank_key(x.to_result_dict(), mode="legacy"))

            base_res = base_stats.to_result_dict()
            accepted_candidate = None
            effective_rule_params = None
            best_ver_res = None

            for cand_stat in surviving_stats:
                cand_res = cand_stat.to_result_dict()
                decision = accept_candidate(
                    base_res,
                    cand_res,
                    mode="legacy",
                    min_delta=self.args.min_delta,
                )
                if decision.accepted:
                    accepted_candidate = cand_stat.delta_tuple if cand_stat.delta_tuple else cand_stat.cand_tuple
                    effective_rule_params = cand_stat.cand_tuple[2]
                    best_ver_res = cand_res
                    break

            if accepted_candidate and best_ver_res is not None and effective_rule_params is not None:
                rule_id, rule_name, delta_params = accepted_candidate

                print(f"\n🔍 [RYGORYSTYCZNA BRAMKA WALIDACJI 10 000 GIER/SETUP]")
                val_base = _run_full_diagnostic(curr_base_overrides, games_per_setup=10000, seed=42)
                val_cand = _run_full_diagnostic(effective_rule_params, games_per_setup=10000, seed=42)

                val_base_4p = val_base["cat_scores"].get("4p", 0.0)
                val_cand_4p = val_cand["cat_scores"].get("4p", 0.0)
                val_delta_4p = val_cand_4p - val_base_4p

                min_allowed_delta = max(0.05, getattr(self.args, "min_delta", 0.05))
                if val_delta_4p < min_allowed_delta:
                    print(f"   ⛔ ODRZUCONO: Zysk 4P ({val_delta_4p:+.2f} pkt) < wymaganego +{min_allowed_delta:.2f} pkt.")
                    continue

                self.total_patches_applied += 1

                with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
                    raw_cfg = yaml.safe_load(f)

                old_version = raw_cfg.get("version", "v1.0-alpha.90")
                mod_cfg, change_desc = apply_mutation_to_config(raw_cfg, rule_id, delta_params)

                if self.args.dry_run:
                    print(f"\n[DRY RUN] Zaakceptowano by modyfikację karty: {change_desc}")
                else:
                    new_version, saved_path = save_config_and_bump_version(mod_cfg, _CONFIG_PATH, bump_version=True)
                    print(f"\n🎉 [ZAAKCEPTOWANO PATCH KARTY #{self.total_patches_applied}]")
                    print(f"   Wersja:      `{old_version}` → **`{new_version}`**")
                    print(f"   Modyfikacja: {change_desc}")

                    update_balance_notes_problem_card(
                        old_version,
                        new_version,
                        change_desc,
                        rule_id,
                        base_res,
                        best_ver_res,
                    )

                    subprocess.run([sys.executable, str(TOOLS_SRC_DIR.parent / "sync_config.py")])
                    print("   ✔ Zaktualizowano konfigurację i dokumentację.")


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 — Audytor Kart Problemowych")
    parser.add_argument("--card", type=str, default=None, help="Identyfikator konkretnej karty do zbadania (np. kt-04)")
    parser.add_argument("--hours", type=float, default=None, help="Maksymalny czas sesji w godzinach")
    parser.add_argument("--max-iters", type=int, default=None, help="Maksymalna liczba udanych patchów")
    parser.add_argument("--min-delta", type=float, default=0.05, help="Minimalny zysk punktowy dla 4P (domyślnie: 0.05)")
    parser.add_argument("--workers", type=int, default=min(os.cpu_count() or 4, 10), help="Liczba procesów równoległych")
    parser.add_argument("--seed", type=int, default=42, help="Ziarno generatora liczb losowych")
    parser.add_argument("--apply", action="store_true", help="Automatycznie wdrażaj zmiany do game_config.yaml")
    parser.add_argument("--dry-run", action="store_true", help="Tryb symulacji bez zapisu")

    args = parser.parse_args()
    optimizer = ProblemCardOptimizer(args)
    optimizer.run()


if __name__ == "__main__":
    main()
