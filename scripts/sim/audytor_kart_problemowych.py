#!/usr/bin/env python3
"""INQUISITIO-1492 — AUDYTOR KART PROBLEMOWYCH 4P (Per-Card Sequential Deep Dive Optimizer).

Autonomiczny optymalizator balansu badający karty problematyczne KARTA PO KARCIE.
Dla każdej karty generuje pełną, wielowymiarową siatkę kombinacji (1D, 2D, 3D, 4D):
  • Koszt (cost: 0, 1, 2, -1, -2)
  • Złoto (gold: 1, 2, 3, +1)
  • Herezja własna (heresy: 0, -1)
  • Oczyszczenie z herezji (heresy_decrease: 1, 2)
  • Wrabianie w herezję (target_heresy: 1, 2, +1)
  • Mobilność agentów (agents: 1, 2)
  • Haki polityczne (creates_hook: True)
  • Kontrola stołu (arrest: True)
  • Pakiety złożone łączące gospodarkę, tempo, planszę i politykę.

Każda zmiana przechodzi 2-etapowy lejek z walidacją krzyżową na 2 seedach (eliminacja szumu).
Po zatwierdzeniu patcha optymalizator podbija wersję, synchronizuje repozytorium
i przechodzi do kolejnej karty na zaktualizowanym stanie gry.

Uruchamianie:
  python3 tools/sim/audytor_kart_problemowych.py --apply
  python3 tools/sim/audytor_kart_problemowych.py --dry-run
  python3 tools/sim/audytor_kart_problemowych.py --apply --card kt-04
  python3 tools/sim/audytor_kart_problemowych.py --apply --min-delta 0.15
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
import multiprocessing
try:
    multiprocessing.set_start_method("fork")
except RuntimeError:
    pass
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from pathlib import Path
from typing import Any

# Ensure sim and tools/sim directories are on path
TOOLS_SRC_DIR = Path(__file__).resolve().parent
SRC_DIR = TOOLS_SRC_DIR.parent.parent / "src"

for p in (TOOLS_SRC_DIR, SRC_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(line_buffering=True)
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(line_buffering=True)

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
        "seed": seed,
    }


def parse_or_detect_problematic_cards(games_screen: int = 1000, seed: int = 42) -> dict[str, dict[str, Any]]:
    """Identifies problematic cards from existing ablation report or quick baseline screening."""
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
                # If the card has healthy play-rate (>=0.30), it's a tempo filler, not a severe problem
                severity = 3 if play_rate >= 0.30 else 1
                problem_cards[cid] = {"id": cid, "name": name, "category": "SELF_HARM", "role": role, "card": c, "faction": pref, "severity": severity, "play_rate": play_rate}
            elif "DISRUPTOR" in role or "TOKSYCZNY" in role or "SZUM" in role:
                problem_cards[cid] = {"id": cid, "name": name, "category": "DISRUPTOR", "role": role, "card": c, "faction": pref, "severity": 2, "play_rate": play_rate}
            elif "DEAD" in role or "NISKIEGO WPŁYWU" in role or "Pasywna" in role or "NIEZAGRYWANA" in role:
                problem_cards[cid] = {"id": cid, "name": name, "category": "DEAD_WEIGHT", "role": role, "card": c, "faction": pref, "severity": 3, "play_rate": play_rate}

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
                sev = 1 if group == "SELF_HARM" else (2 if group == "DISRUPTOR" else 3)
                problem_cards[cid] = {"id": cid, "name": cards[cid].name, "category": group, "role": role_name, "card": cards[cid], "faction": pref, "severity": sev}

    return problem_cards


def generate_deep_reworks_for_single_card(
    cid: str,
    info: dict[str, Any],
    base_res: dict[str, Any] | None = None,
) -> list[tuple[str, str, dict]]:
    """Generates an extensive combinatorial grid (1D, 2D, 3D, 4D) of mechanical reworks for a single card."""
    c = info["card"]
    cat = info["category"]
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

    # --- 1. WYMIAR KOSZTU ---
    if c.cost > 0:
        _add_cand("COST_MINUS1", f"Koszt {c.cost}→{c.cost-1}", {"cost": c.cost - 1})
        _add_cand("COST_ZERO", f"Koszt darmowy {c.cost}→0", {"cost": 0})
    if c.cost >= 2:
        _add_cand("COST_MINUS2", f"Koszt głęboki {c.cost}→{c.cost-2}", {"cost": c.cost - 2})

    # --- 2. WYMIAR HEREZJI WŁASNEJ ---
    if c.heresy > 0:
        _add_cand("HERESY_ZERO", f"Usunięcie kary herezji {c.heresy}→0", {"heresy": 0})
        if c.heresy >= 2:
            _add_cand("HERESY_MINUS1", f"Zmniejszenie herezji {c.heresy}→{c.heresy-1}", {"heresy": c.heresy - 1})

    # --- 3. WYMIAR OCZYSZCZANIA (heresy_decrease) ---
    _add_cand("DEC_HERESY_1", "Oczyszczenie z herezji: -1", {"heresy_decrease": 1})
    _add_cand("DEC_HERESY_2", "Oczyszczenie głębokie: -2", {"heresy_decrease": 2})
    if c.heresy > 0:
        _add_cand("HERESY_0_AND_DEC_1", "Herezja 0 + Oczyszczenie -1", {"heresy": 0, "heresy_decrease": 1})

    # --- 4. WYMIAR GOSPODARCZY (gold) ---
    if c.gold == 0:
        _add_cand("GOLD_1", "Zastrzyk złota +1", {"gold": 1})
        _add_cand("GOLD_2", "Silnik złota +2", {"gold": 2})
        _add_cand("GOLD_3", "Skarbiec +3", {"gold": 3})
    else:
        _add_cand("GOLD_PLUS1", f"Złoto {c.gold}→{c.gold+1}", {"gold": c.gold + 1})
        _add_cand("GOLD_PLUS2", f"Złoto {c.gold}→{c.gold+2}", {"gold": c.gold + 2})

    # --- 5. WYMIAR WRABIANIA / AGRESJI (target_heresy) ---
    if c.target_heresy == 0:
        _add_cand("TARGET_HERESY_1", "Wrabianie rywala: 1", {"target_heresy": 1})
        _add_cand("TARGET_HERESY_2", "Wrabianie rywala: 2", {"target_heresy": 2})
    else:
        _add_cand("TARGET_HERESY_PLUS1", f"Wrabianie {c.target_heresy}→{c.target_heresy+1}", {"target_heresy": c.target_heresy + 1})

    # --- 6. WYMIAR MOBILNOŚCI I PLANSZY (agents) ---
    if c.agents == 0:
        _add_cand("AGENTS_1", "Ruch agenta: 1", {"agents": 1})
        _add_cand("AGENTS_2", "Mobilność agentów: 2", {"agents": 2})
    else:
        _add_cand("AGENTS_PLUS1", f"Agenci {c.agents}→{c.agents+1}", {"agents": c.agents + 1})

    # --- 7. WYMIAR POLITYCZNY I KONTROLI (creates_hook, arrest) ---
    if not c.creates_hook:
        _add_cand("HOOK_TRUE", "Dźwignia polityczna: tworzy hak", {"creates_hook": True})
    if not c.arrest:
        _add_cand("ARREST_TRUE", "Kontrola stołu: aresztuje wroga", {"arrest": True})

    # --- 8. ZŁOŻONE KOMBINACJE 2D (Multi-Parameter Compound) ---
    # Koszt + Herezja
    if c.cost > 0 and c.heresy > 0:
        _add_cand("COMPOUND_COST_HERESY", f"Koszt {c.cost-1} + Herezja 0", {"cost": c.cost - 1, "heresy": 0})
        _add_cand("COMPOUND_COST0_HERESY0", "Koszt 0 + Herezja 0", {"cost": 0, "heresy": 0})
    # Koszt + Złoto
    if c.cost > 0:
        _add_cand("COMPOUND_COST_GOLD1", f"Koszt {c.cost-1} + Złoto 1", {"cost": c.cost - 1, "gold": max(1, c.gold + 1)})
        _add_cand("COMPOUND_COST0_GOLD1", "Koszt 0 + Złoto 1", {"cost": 0, "gold": max(1, c.gold + 1)})
        _add_cand("COMPOUND_COST0_GOLD2", "Koszt 0 + Złoto 2", {"cost": 0, "gold": max(2, c.gold + 2)})
    # Koszt + Wrabianie
    if c.cost > 0:
        _add_cand("COMPOUND_COST_TARGET", f"Koszt {c.cost-1} + Wrabianie 1", {"cost": c.cost - 1, "target_heresy": max(1, c.target_heresy + 1)})
        _add_cand("COMPOUND_COST0_TARGET1", "Koszt 0 + Wrabianie 1", {"cost": 0, "target_heresy": max(1, c.target_heresy + 1)})
    # Koszt + Haki
    if c.cost > 0 and not c.creates_hook:
        _add_cand("COMPOUND_COST_HOOK", f"Koszt {c.cost-1} + Tworzy Hak", {"cost": c.cost - 1, "creates_hook": True})
        _add_cand("COMPOUND_COST0_HOOK", "Koszt 0 + Tworzy Hak", {"cost": 0, "creates_hook": True})
    # Koszt + Agenci
    if c.cost > 0 and c.agents == 0:
        _add_cand("COMPOUND_COST_AGENTS", f"Koszt {c.cost-1} + Ruch Agenta 1", {"cost": c.cost - 1, "agents": 1})
        _add_cand("COMPOUND_COST0_AGENTS", "Koszt 0 + Ruch Agenta 1", {"cost": 0, "agents": 1})

    # Herezja + Złoto
    if c.heresy > 0:
        _add_cand("COMPOUND_HERESY0_GOLD1", "Herezja 0 + Złoto 1", {"heresy": 0, "gold": max(1, c.gold + 1)})
        _add_cand("COMPOUND_HERESY0_GOLD2", "Herezja 0 + Złoto 2", {"heresy": 0, "gold": max(2, c.gold + 2)})
        _add_cand("COMPOUND_HERESY0_TARGET1", "Herezja 0 + Wrabianie 1", {"heresy": 0, "target_heresy": max(1, c.target_heresy + 1)})
        _add_cand("COMPOUND_HERESY0_HOOK", "Herezja 0 + Tworzy Hak", {"heresy": 0, "creates_hook": True})
        _add_cand("COMPOUND_HERESY0_AGENTS", "Herezja 0 + Ruch Agenta 1", {"heresy": 0, "agents": 1})
        _add_cand("COMPOUND_HERESY0_ARREST", "Herezja 0 + Areszt", {"heresy": 0, "arrest": True})

    # Złoto + Wrabianie / Haki / Agenci
    _add_cand("COMPOUND_GOLD1_TARGET1", "Złoto 1 + Wrabianie 1", {"gold": max(1, c.gold + 1), "target_heresy": max(1, c.target_heresy + 1)})
    _add_cand("COMPOUND_GOLD1_HOOK", "Złoto 1 + Tworzy Hak", {"gold": max(1, c.gold + 1), "creates_hook": True})
    _add_cand("COMPOUND_GOLD1_AGENTS", "Złoto 1 + Ruch Agenta 1", {"gold": max(1, c.gold + 1), "agents": 1})
    _add_cand("COMPOUND_TARGET1_HOOK", "Wrabianie 1 + Tworzy Hak", {"target_heresy": max(1, c.target_heresy + 1), "creates_hook": True})
    _add_cand("COMPOUND_TARGET1_AGENTS", "Wrabianie 1 + Ruch Agenta 1", {"target_heresy": max(1, c.target_heresy + 1), "agents": 1})
    _add_cand("COMPOUND_DEC_HERESY_AGENTS", "Oczyszczenie -1 + Ruch Agenta 1", {"heresy_decrease": 1, "agents": 1})
    _add_cand("COMPOUND_DEC_HERESY_GOLD1", "Oczyszczenie -1 + Złoto 1", {"heresy_decrease": 1, "gold": max(1, c.gold + 1)})

    # --- 9. ZAAWANSOWANE PAKIETY 3D i 4D ---
    # Pakiet Przełamania Biedy
    _add_cand("TRIO_POVERTY_BREAKER", "Pakiet Przełamania Biedy (Koszt 0, Złoto 2, Herezja 0)", {"cost": 0, "gold": max(2, c.gold + 2), "heresy": 0})
    # Pakiet Mobilności i Wrabiania
    _add_cand("TRIO_MOBILITY_FRAME", "Pakiet Mobilności i Wrabiania (Koszt 0, Agenci 1, Wrabianie 1)", {"cost": 0, "agents": 1, "target_heresy": max(1, c.target_heresy + 1)})
    # Pakiet Polityczny
    _add_cand("TRIO_POLITICAL_ENGINE", "Pakiet Polityczny (Koszt 0, Złoto 1, Hak True)", {"cost": 0, "gold": max(1, c.gold + 1), "creates_hook": True})
    # Pakiet Oczyszczenia Stołu
    _add_cand("TRIO_PURIFICATION_SUITE", "Pakiet Oczyszczenia (Herezja 0, Oczyszczenie -1, Złoto 1)", {"heresy": 0, "heresy_decrease": 1, "gold": max(1, c.gold + 1)})
    # Pakiet Kontroli i Aresztu
    _add_cand("TRIO_CONTROL_ARREST", "Pakiet Kontroli Stołu (Koszt 1, Herezja 0, Areszt True)", {"cost": max(1, c.cost), "heresy": 0, "arrest": True})
    # Pakiet Pełnej Mocy (Quad)
    _add_cand("QUAD_SUPREME_TEMPO", "Pakiet Najwyższego Tempa (Koszt 0, Złoto 1, Agenci 1, Hak True)", {"cost": 0, "gold": max(1, c.gold + 1), "agents": 1, "creates_hook": True})
    _add_cand("QUAD_PURIFIED_FRAME", "Pakiet Agresji Czystości (Koszt 0, Herezja 0, Oczyszczenie -1, Wrabianie 1)", {"cost": 0, "heresy": 0, "heresy_decrease": 1, "target_heresy": max(1, c.target_heresy + 1)})

    # Align candidate count to a multiple of 10 for 100% CPU thread efficiency
    remainder = len(candidates) % 10
    if remainder != 0:
        needed = 10 - remainder
        for g_amt in (4, 5, 6, 7, 8, 9, 10):
            p_tag = f"PAD_GOLD_{g_amt}"
            _add_cand(p_tag, f"Dopełnienie Ekonomiczne: Złoto {g_amt}", {"gold": g_amt})
            if len(candidates) % 10 == 0:
                break

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
    """Adds entry to data/playtesting/balance-notes.md."""
    if not BALANCE_NOTES_PATH.exists():
        return
    content = BALANCE_NOTES_PATH.read_text(encoding="utf-8")
    today = datetime.now().strftime("%Y-%m-%d")
    d_4p = best_score - base_score
    delta_str = f"+{d_4p:.2f}" if d_4p > 0 else f"{d_4p:.2f}"

    block = (
        f"### 🟢 Patch {new_version} ({today}) — Celowany Rework Karty: {change_desc} (Zysk 4P Δ {delta_str} pkt)\n"
        f"- **Wynik 4P (win share):** **`{best_score:.1f} pkt`** (baza `{base_score:.1f} pkt`)\n"
        f"- **Modyfikacja (`{rule_id}`):** {change_desc}.\n"
        f"- **Efekt:** Likwidacja autopodatku i naprawa mechaniki karty. "
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
        print(f"      Wersja: {CONFIG.version} | Ziarno: {self.args.seed}      ")
        print("═══════════════════════════════════════════════════════════════\n")

        # 1. Detect and Sort Problematic Cards
        all_problem_cards = parse_or_detect_problematic_cards(games_screen=1000, seed=self.args.seed)
        
        # Filter if single card requested
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

        print(f"🎯 Zidentyfikowano {len(all_problem_cards)} kart poddanych sekwencyjnemu badaniu:")
        # Sort by severity (Self-harm first, then Disruptors, then Dead Weight)
        sorted_cards = sorted(all_problem_cards.items(), key=lambda x: (x[1]["severity"], x[0]))
        for cid, info in sorted_cards:
            print(f"   • {cid:<7s} ({info['name']:<25s}): {info['role']}")
        print()

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

            # 1. Measure Current Base Score on primary and cross seeds
            print("📊 Mierzę aktualny stan bazowy Kanonu 4P (3000 gier/setup)...")
            base_res = _run_single_task(("BASE", "Baza", {}, 3000, self.args.seed, CANONICAL_4P_SETUPS))
            base_score = base_res["score"]
            print(f"   🎯 Bieżący 4P Score (Seed {self.args.seed}): {color_score(base_score, bold=True)} pkt")
            print(f"   📊 Udziały: {', '.join(f'{k}: {v:.1f}%' for k, v in sorted(base_res['faction_shares'].items()))}\n")

            # 2. Generate 40-60 multi-parameter reworks for this single card
            candidates = generate_deep_reworks_for_single_card(cid, info, base_res)
            print(f"🔧 Wygenerowano {len(candidates)} wielowymiarowych wariantów kombinatorycznych dla `{cid}`.\n")

            # 3. Stage 1: Fast Screening (1000 games/setup across 10 parallel processes)
            print(f"⏳ [Etap 1/2: Przesiew Siatki] Testuję {len(candidates)} kombinacji (1000 gier/setup)...")
            tasks_stage1 = [(c[0], c[1], c[2], 1000, self.args.seed, CANONICAL_4P_SETUPS) for c in candidates]
            with ProcessPoolExecutor(max_workers=min(10, len(tasks_stage1), os.cpu_count() or 4)) as ex:
                res_stage1 = list(ex.map(_run_single_task, tasks_stage1))

            res_stage1.sort(key=lambda r: r["score"], reverse=True)
            top_n = min(5, len(res_stage1))
            top_candidates = res_stage1[:top_n]

            print(f"✔ Wyłoniono TOP {top_n} finalistów dla `{cid}`:")
            for rank, r in enumerate(top_candidates, 1):
                d = r["score"] - base_score
                print(f"   {rank:2d}. Score: {color_score(r['score'])} pkt (Δ {d:+5.2f} pkt) | {r['name']}")
            print()

            # 4. Stage 2: Ultra Verification + Cross-Validation (3000 games on Seed 1 AND Seed 2 in 1 parallel pass)
            cross_seed = self.args.seed + 9999
            print(f"⏳ [Etap 2/2: Weryfikacja Ultra & Cross-Validation] Badam TOP {top_n} finalistów na 2 seedach równolegle (3000 gier/setup)...")
            
            tasks_stage2 = []
            for r in top_candidates:
                tasks_stage2.append((f"{r['id']}__S1", r["name"], r["overrides"], 3000, self.args.seed, CANONICAL_4P_SETUPS))
                tasks_stage2.append((f"{r['id']}__S2", r["name"], r["overrides"], 3000, cross_seed, CANONICAL_4P_SETUPS))
            
            # Base cross measurement
            tasks_stage2.append(("BASE__S2", "Baza Cross", {}, 3000, cross_seed, CANONICAL_4P_SETUPS))

            with ProcessPoolExecutor(max_workers=min(11, len(tasks_stage2), os.cpu_count() or 4)) as ex:
                res_all_stage2 = list(ex.map(_run_single_task, tasks_stage2))

            stage2_map = {r["id"]: r for r in res_all_stage2}
            base_cross_score = stage2_map.get("BASE__S2", {}).get("score", base_score)

            evaluated = []
            for r in top_candidates:
                r1 = stage2_map.get(f"{r['id']}__S1")
                r2 = stage2_map.get(f"{r['id']}__S2")
                if not r1 or not r2:
                    continue
                d1 = r1["score"] - base_score
                d2 = r2["score"] - base_cross_score
                avg_score = (r1["score"] + r2["score"]) / 2.0
                avg_delta = (d1 + d2) / 2.0
                evaluated.append({
                    "id": r["id"],
                    "name": r["name"],
                    "overrides": r["overrides"],
                    "score_primary": r1["score"],
                    "score_cross": r2["score"],
                    "score_avg": avg_score,
                    "delta_primary": d1,
                    "delta_cross": d2,
                    "delta_avg": avg_delta,
                    "res_primary": r1,
                    "res_cross": r2,
                })

            evaluated.sort(key=lambda x: x["delta_avg"], reverse=True)
            best = evaluated[0]

            print("\n═══════════════════════════════════════════════════════════════")
            print(f"🏆 NAJLEPSZY REWORK DLA KARTY `{cid.upper()}`:")
            print(f"   ID:       {best['id']}")
            print(f"   Opis:     {best['name']}")
            print(f"   Wynik S1 (Seed {self.args.seed}):      {base_score:.2f} → {best['score_primary']:.2f} pkt (Δ {best['delta_primary']:+5.2f} pkt)")
            print(f"   Wynik S2 (Seed {cross_seed}):  {base_cross_score:.2f} → {best['score_cross']:.2f} pkt (Δ {best['delta_cross']:+5.2f} pkt)")
            print(f"   Średni Zysk Balansu 4P: {color_score(best['score_avg'], bold=True)} pkt (Δ Średnia: {best['delta_avg']:+5.2f} pkt)")
            p_res = best["res_primary"]
            print(f"   Rozkład 4P: {', '.join(f'{k}: {v:.1f}%' for k, v in sorted(p_res['faction_shares'].items()))}")
            print(f"   Telemetria: Śr. Er {p_res['eras_avg']:.2f} | Deadlocks: {p_res['deadlock_pct']:.1f}% | Pas Biedy: {p_res['poverty_pct']:.1f}%")
            print("═══════════════════════════════════════════════════════════════\n")

            # Check acceptance threshold (Cross-Validated)
            is_valid_gain = (best["delta_avg"] >= self.args.min_delta) and (best["delta_primary"] > 0) and (best["delta_cross"] > 0)

            if is_valid_gain:
                if self.args.apply:
                    with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
                        raw_cfg = yaml.safe_load(f)
                    old_ver = raw_cfg.get("version", "v1.0")
                    mod_cfg, change_desc = apply_mutation_to_config(raw_cfg, best["id"], best["overrides"])
                    new_ver, _ = save_config_and_bump_version(mod_cfg, _CONFIG_PATH, bump_version=True)

                    # Update balance notes and sync
                    update_balance_notes_entry(old_ver, new_ver, change_desc, best["id"], base_score, best["score_avg"], p_res)
                    subprocess.run([sys.executable, str(TOOLS_SRC_DIR.parent / "sync_config.py")])
                    print(f"🎉 [ZAAKCEPTOWANO PATCH KARTY #{self.total_patches_applied + 1}] `{old_ver}` → **`{new_ver}`** ({change_desc})")
                    self.total_patches_applied += 1
                else:
                    print(f"[DRY RUN] Zaakceptowano by mutację {best['id']} (Zysk Δ {best['delta_avg']:+5.2f} pkt).")
                    self.total_patches_applied += 1
            else:
                print(f"⚪ Karta `{cid}` nie uzyskała stabilnego zysku ≥ {self.args.min_delta:.2f} pkt na obu seedach. Pozostawiam bez zmian.")

        total_elapsed = round(time.time() - self.start_time, 1)
        print(f"\n═══════════════════════════════════════════════════════════════")
        print(f"   AUDYTOR KART PROBLEMOWYCH ZAKOŃCZYŁ SESJĘ.")
        print(f"   Wprowadzono łącznie {self.total_patches_applied} udanych patchów w {total_elapsed}s ({round(total_elapsed/60, 1)} min).")
        print(f"═══════════════════════════════════════════════════════════════\n")


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 — Audytor Kart Problemowych 4P (Per-Card Sequential Deep Dive)")
    parser.add_argument("--dry-run", action="store_true", help="Tylko symulacja bez zapisu zmian do game_config.yaml")
    parser.add_argument("--apply", action="store_true", help="Automatycznie aplikuj każdy udany patch do game_config.yaml i kontynuuj sekwencję")
    parser.add_argument("--card", type=str, default=None, help="Poddaj badaniu wyłącznie jedną konkretną kartę (np. kt-04, caa-01)")
    parser.add_argument("--max-iters", type=int, default=None, help="Maksymalna liczba udanych patchów")
    parser.add_argument("--hours", type=float, default=None, help="Maksymalny czas działania w godzinach")
    parser.add_argument("--min-delta", type=float, default=0.10, help="Minimalny średni zysk 4P Score wymagany do zatwierdzenia patcha (pkt, domyślnie: 0.10)")
    parser.add_argument("--seed", type=int, default=42, help="RNG seed")
    args = parser.parse_args()

    optimizer = ProblemCardOptimizer(args)
    optimizer.run()


if __name__ == "__main__":
    main()
