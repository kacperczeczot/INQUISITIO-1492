#!/usr/bin/env python3
"""INQUISITIO-1492 — BADANIE UŻYTECZNOŚCI I WPŁYWU ELEMENTÓW W KANONIE 4P (Ablation & Impact Audit 4P).

Specjalistyczne narzędzie analityczne do badania wkładu każdego pojedynczego elementu gry w Kanon 4-osobowy (4P):
  1. Ablacja Kart (Per-Card Ablation w 4P): Wyłącza każdą z 50 kart z osobna na 5 setupach 4p:
     - Wpływ na Win Share frakcji w 4P (Kanon: idealne 25.0%)
     - Wpływ na 4P Balance Score (czy karta stabilizuje kanon 4p, czy go destabilizuje)
     - Wpływ na tempo partii (Średnia Er) i wskaźnik deadlocków w 4P
  2. Klasyfikacja Kart w Kanonie 4P (Matryca 2D):
     - 👑 FILAR FRAKCJI W 4P (Core Keystone): Kluczowy motor napędowy wygranych frakcji
     - ⚓ KOTWICA KANONU 4P (Balance Anchor): Bezpiecznik chroniący przed dominacją frakcji
     - ⚠️ KARTA TOKSYCZNA W 4P (Disruptor): Karta, której usunięcie podnosi 4P Score
     - 💤 MARTWA KARTA W 4P (Dead Weight): Znikomy wpływ na grę 4-osobową
     - ⚖️ ZBALANSOWANE NARZĘDZIE 4P (Utility): Zdrowe, elastyczne narzędzie taktyczne
  3. Ablacja Mechanik Systemowych i Ścieżek Zwycięstwa w 4P:
     - Wpływ Kroniki Dziejów (Talia Czasu), Cooldownu Autodafé, Bramki Haka, Fragmentów itp.

Generuje raport w: playtesting/sim-reports/raport_uzytecznosci_i_wplywu_4p.md oraz archiwizuje w archive/{version}/.
"""
from __future__ import annotations

import argparse
import copy
import os
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
from inquisitio.engine.setup import SETUP_PRESETS, FactionId
from inquisitio.runner.audit_facts import score_pair, save_and_archive_report
from inquisitio.runner.batch import run_batch
from inquisitio.runner.scoring import (
    calculate_setup_score,
    color_score,
)

REPORTS_DIR = Path(__file__).resolve().parent.parent.parent / "playtesting" / "sim-reports"
OUTPUT_REPORT_PATH = REPORTS_DIR / "current" / "raport_uzytecznosci_i_wplywu_4p.md"

CANONICAL_4P_SETUPS = [
    "4p-core",
    "4p-no-cienie",
    "4p-no-kabala",
    "4p-no-korona",
    "4p-no-oficjum",
]

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

FACTION_FULL_NAMES = {
    "so": "Święte Oficjum",
    "caa": "Cienie Al-Andalus",
    "kb": "Korona & Borgiowie",
    "kt": "Kabała z Toledo",
    "gc": "Gildia Cieni",
}


def _run_ablation_task_4p(task_args: tuple[str, str, dict, int, int, list[str]]) -> dict:
    """Simulates the 5 canonical 4P setups under a specific ablation / modification."""
    element_id, element_name, sys_overrides, games_per_setup, seed, setups = task_args
    t0 = time.time()

    summaries = []
    setup_scores = {}
    faction_wins: dict[str, int] = {}
    faction_total_games: dict[str, int] = {}

    for sname in setups:
        summary = run_batch(
            games=games_per_setup,
            setup=sname,
            seed=seed,
            layer="C",
            win_overrides=sys_overrides,
        )
        summaries.append(summary)
        setup_scores[sname] = calculate_setup_score(summary)

        factions = SETUP_PRESETS[sname]
        for fid in factions:
            fname = FACTION_NAMES[fid]
            w_count = summary.wins.get(fid, 0)
            faction_wins[fname] = faction_wins.get(fname, 0) + w_count
            faction_total_games[fname] = faction_total_games.get(fname, 0) + summary.games

    score_4p = round(sum(setup_scores.values()) / len(setup_scores), 1) if setup_scores else 0.0
    dt = round(time.time() - t0, 2)

    n_sum = len(summaries)
    eras_avg = sum(s.eras_avg for s in summaries) / n_sum
    deadlock_pct = (sum(s.eras_limit_pct for s in summaries) / n_sum) * 100.0
    poverty_pct = (sum(s.passes_forced_pct for s in summaries) / n_sum) * 100.0
    autodafe_avg = sum(s.autodafe_avg for s in summaries) / n_sum
    acc_avg = sum(s.accusations_avg for s in summaries) / n_sum

    faction_shares = {}
    for fname, wins in faction_wins.items():
        tot = faction_total_games.get(fname, 1)
        faction_shares[fname] = round((wins / tot) * 100.0, 1)

    return {
        "id": element_id,
        "name": element_name,
        "score_4p": score_4p,
        "setup_scores": setup_scores,
        "faction_shares": faction_shares,
        "eras_avg": eras_avg,
        "deadlock_pct": deadlock_pct,
        "poverty_pct": poverty_pct,
        "autodafe_avg": autodafe_avg,
        "acc_avg": acc_avg,
        "dt": dt,
    }


def classify_card_impact_4p(d_share: float, d_4p: float) -> tuple[str, str, str]:
    """Classifies card impact into 3x3 quadrant matrix for Kanon 4P."""
    if d_4p >= 1.2:
        if d_share > 0.8:
            return "TOXIC_CARRIER", "⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver)", "DISRUPTOR"
        elif d_share < -0.8:
            return "TOXIC_BRAKE", "⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm)", "DISRUPTOR"
        else:
            return "TOXIC_NOISE", "⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor)", "DISRUPTOR"

    if d_4p <= -2.0 or d_share >= 2.5:
        if d_share >= 2.5:
            return "PILLAR", "👑 FILAR KANONU (Core Keystone)", "STABILIZER"
        elif d_share <= -2.5:
            return "SHIELD", "🛡️ TARCZA DEFENSYWNA (Faction Shield)", "STABILIZER"
        else:
            return "ANCHOR", "⚓ KOTWICA KANONU (Balance Anchor)", "STABILIZER"

    if abs(d_share) <= 0.4 and abs(d_4p) <= 0.4:
        return "DEAD_WEIGHT", "💤 KARTA NISKIEGO WPŁYWU (Passive)", "DEAD_WEIGHT"

    if d_share >= 1.0:
        return "ENGINE", "⚡ MOTOR FRAKCJI (Offensive Engine)", "BALANCED"
    elif d_share <= -1.0:
        return "BRAKE", "🛑 HAMULEC FRAKCJI (Control Tool)", "BALANCED"
    else:
        return "UTILITY", "⚖️ ZBALANSOWANE NARZĘDZIE (Utility)", "BALANCED"


def classify_mechanic_impact_4p(d_4p: float, max_d_share: float) -> tuple[str, str, str]:
    """Classifies system/victory mechanic impact into 3x3 (9 areas) matrix.
    
    Y: Severity / Importance (Critical, Moderate, Low)
    X: Effect Direction (Worsens Balance, Neutral, Improves Balance)
    """
    # 1. Determine Severity
    if abs(d_4p) >= 15.0 or max_d_share >= 10.0:
        severity = "CRITICAL"
    elif abs(d_4p) >= 4.0 or max_d_share >= 4.0:
        severity = "MODERATE"
    else:
        severity = "LOW"

    # 2. Determine Effect Direction
    if d_4p <= -4.0:
        direction = "STABILIZER"
    elif d_4p >= 1.5:
        direction = "DISRUPTOR"
    else:
        direction = "NEUTRAL"

    # 3. 3x3 Matrix mapping (9 Areas)
    mapping = {
        ("CRITICAL", "STABILIZER"): ("M_CRIT_STAB", "👑 KRYTYCZNY FILAR (Core Engine Pillar)", "STABILIZER"),
        ("CRITICAL", "NEUTRAL"):    ("M_CRIT_NEUT", "⚓ KLUCZOWY STABILIZATOR (Key Anchor)", "NEUTRAL"),
        ("CRITICAL", "DISRUPTOR"):   ("M_CRIT_DISR", "⚠️ KRYTYCZNA WADA (Critical Flaw)", "DISRUPTOR"),
        ("MODERATE", "STABILIZER"): ("M_MOD_STAB",  "🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard)", "STABILIZER"),
        ("MODERATE", "NEUTRAL"):    ("M_MOD_NEUT",  "⚖️ ZBALANSOWANY REGULATOR (Balanced Regulator)", "NEUTRAL"),
        ("MODERATE", "DISRUPTOR"):  ("M_MOD_DISR",  "⚠️ UMIARKOWANE OBCIĄŻENIE (Moderate Drag)", "DISRUPTOR"),
        ("LOW", "STABILIZER"):      ("M_LOW_STAB",  "🛑 DROBNY REGULATOR (Minor Buffer)", "STABILIZER"),
        ("LOW", "NEUTRAL"):         ("M_LOW_NEUT",  "💤 MECHANIKA PASYWNA (Low Impact)", "NEUTRAL"),
        ("LOW", "DISRUPTOR"):       ("M_LOW_DISR",  "💡 KANDYDAT DO UPROSZCZENIA (Simplification)", "DISRUPTOR"),
    }
    return mapping.get((severity, direction), ("M_GENERIC", "⚖️ REGULATOR", "NEUTRAL"))


def build_all_mechanic_tasks(games_per_setup: int, seed: int, setups: list[str]) -> list[tuple[str, str, str, dict, int, int, list[str]]]:
    """Generates comprehensive ablation & extreme-parameter tasks for ALL Level 1, Level 2, and Level 4 mechanics."""
    v = CONFIG.victory
    s = CONFIG.system
    nv = CONFIG.variants

    so = v.swiete_oficjum
    caa = v.cienie_al_andalus
    kb = v.korona_borgiowie
    kt = v.kabala_toledo
    gc = v.gildia_cieni
    hb = kt.heresy_band

    tasks = [
        # ══════════════════════════════════════════════════════════════
        # POZIOM 1: GŁÓWNE MECHANIKI SYSTEMOWE (GLOBAL SYSTEM CORE)
        # ══════════════════════════════════════════════════════════════
        ("L1_MAX_ERAS_8", "Limit Er: 12 → 8 Er (Presja czasu)", "Poziom 1: System Core", {"max_eras": 8}),
        ("L1_MAX_ERAS_16", "Limit Er: 12 → 16 Er (Wydłużony silnik)", "Poziom 1: System Core", {"max_eras": 16}),
        ("L1_THRESHOLD_MINUS1", "Próg Oskarżenia na Dworze: -1 (Agresywny Dwór)", "Poziom 1: System Core", {"threshold_offset": -1}),
        ("L1_THRESHOLD_PLUS1", "Próg Oskarżenia na Dworze: +1 (Pasywny Dwór)", "Poziom 1: System Core", {"threshold_offset": 1}),
        ("L1_START_GOLD_0", "Złoto startowe: 4zł → 0zł (Skrajne ubóstwo)", "Poziom 1: System Core", {"start_gold": 0}),
        ("L1_START_GOLD_6", "Złoto startowe: 4zł → 6zł (Bogaty start)", "Poziom 1: System Core", {"start_gold": 6}),
        ("L1_AGENTS_2", "Liczba Agentów: 3 → 2 Agentów (Ograniczony zasięg)", "Poziom 1: System Core", {"agents_offset": -1}),
        ("L1_AGENTS_4", "Liczba Agentów: 3 → 4 Agentów (Gęsta plansza)", "Poziom 1: System Core", {"agents_offset": 1}),
        ("L1_HAND_LIMIT_3", "Limit kart na ręce: 5 → 3 karty (Zmniejszona elastyczność)", "Poziom 1: System Core", {"hand_limit_offset": -2}),
        ("L1_HAND_LIMIT_7", "Limit kart na ręce: 5 → 7 kart (Pełna swoboda)", "Poziom 1: System Core", {"hand_limit_offset": 2}),
        ("L1_AUTODAFE_CD_2", "Autodafé Inkwizytora: Cooldown 2 Ery (Częsta czystka)", "Poziom 1: System Core", {"autodafe_cooldown": 2}),
        ("L1_AUTODAFE_CD_4", "Autodafé Inkwizytora: Cooldown 4 Ery (Rzadka czystka)", "Poziom 1: System Core", {"autodafe_cooldown": 4}),
        ("L1_AUTODAFE_DISABLED", "Autodafé Inkwizytora: Całkowity brak czystki", "Poziom 1: System Core", {"autodafe_cooldown": 99}),

        # ══════════════════════════════════════════════════════════════
        # POZIOM 2: FRAKCYJNE WARUNKI ZWYCIĘSTWA (VICTORY PATHS)
        # ══════════════════════════════════════════════════════════════
        # Święte Oficjum
        ("L2_SO_STACKS_REQ_PLUS2", "Święte Oficjum: Wymóg Stosów +2", "Poziom 2: Warunki Zwycięstwa", {"so_stacks_offset": 2}),
        ("L2_SO_STACKS_REQ_MINUS1", "Święte Oficjum: Wymóg Stosów -1", "Poziom 2: Warunki Zwycięstwa", {"so_stacks_offset": -1}),
        ("L2_SO_CONDEMNS_REQ_PLUS2", "Święte Oficjum: Wymóg Skazań +2 (Zamiast 2-3)", "Poziom 2: Warunki Zwycięstwa", {"so_condemns_offset": 2}),
        ("L2_SO_CONDEMNS_REQ_MINUS1", "Święte Oficjum: Wymóg Skazań -1", "Poziom 2: Warunki Zwycięstwa", {"so_condemns_offset": -1}),

        # Cienie Al-Andalus
        ("L2_CAA_RELICS_REQ_PLUS2", "Cienie: Wymóg Relikwii 2 → 4", "Poziom 2: Warunki Zwycięstwa", {"caa_relics_offset": 2}),
        ("L2_CAA_RELICS_REQ_MINUS1", "Cienie: Wymóg Relikwii 2 → 1", "Poziom 2: Warunki Zwycięstwa", {"caa_relics_offset": -1}),
        ("L2_CAA_ERA_EARLY", "Cienie: Wymóg Ery 5 → Era 3 (Wczesna ucieczka)", "Poziom 2: Warunki Zwycięstwa", {"caa_era_offset": -2}),
        ("L2_CAA_ERA_LATE", "Cienie: Wymóg Ery 5 → Era 8 (Późna ucieczka)", "Poziom 2: Warunki Zwycięstwa", {"caa_era_offset": 3}),

        # Korona & Borgiowie
        ("L2_KB_DECREES_REQ_PLUS1", "Korona: Wymóg Dekretów 2 → 3", "Poziom 2: Warunki Zwycięstwa", {"kb_decrees_offset": 1}),
        ("L2_KB_DECREES_REQ_MINUS1", "Korona: Wymóg Dekretów 2 → 1", "Poziom 2: Warunki Zwycięstwa", {"kb_decrees_offset": -1}),
        ("L2_KB_HOOKS_REQ_0", "Korona: Brak wymogu Haków (0 Haków)", "Poziom 2: Warunki Zwycięstwa", {"kb_hooks_offset": -1}),
        ("L2_KB_HOOKS_REQ_PLUS2", "Korona: Wymóg Haków +2", "Poziom 2: Warunki Zwycięstwa", {"kb_hooks_offset": 2}),
        ("L2_KB_ERA_EARLY", "Korona: Wymóg Ery 5 → Era 3", "Poziom 2: Warunki Zwycięstwa", {"kb_era_offset": -2}),
        ("L2_KB_ERA_LATE", "Korona: Wymóg Ery 5 → Era 7", "Poziom 2: Warunki Zwycięstwa", {"kb_era_offset": 2}),

        # Kabała z Toledo
        ("L2_KT_FRAGS_REQ_PLUS1", "Kabała: Wymóg Fragmentów 3 → 4", "Poziom 2: Warunki Zwycięstwa", {"kt_frags_offset": 1}),
        ("L2_KT_FRAGS_REQ_MINUS1", "Kabała: Wymóg Fragmentów 3 → 2", "Poziom 2: Warunki Zwycięstwa", {"kt_frags_offset": -1}),
        ("L2_KT_ERA_EARLY", "Kabała: Wymóg Ery 6 → Era 4", "Poziom 2: Warunki Zwycięstwa", {"kt_era_offset": -2}),
        ("L2_KT_ERA_LATE", "Kabała: Wymóg Ery 6 → Era 8", "Poziom 2: Warunki Zwycięstwa", {"kt_era_offset": 2}),
        ("L2_KT_HERESY_LOW_UP", f"Kabała: Próg Dolny Pasma {hb[0]} → {hb[0]+2} (Zawężenie od dołu)", "Poziom 2: Warunki Zwycięstwa", {"kt_heresy_band": (hb[0]+2, hb[1])}),
        ("L2_KT_HERESY_LOW_DOWN", f"Kabała: Próg Dolny Pasma {hb[0]} → {max(0, hb[0]-2)} (Rozszerzenie w dół)", "Poziom 2: Warunki Zwycięstwa", {"kt_heresy_band": (max(0, hb[0]-2), hb[1])}),
        ("L2_KT_HERESY_HIGH_DOWN", f"Kabała: Próg Górny Pasma {hb[1]} → {hb[1]-2} (Zawężenie od góry)", "Poziom 2: Warunki Zwycięstwa", {"kt_heresy_band": (hb[0], hb[1]-2)}),
        ("L2_KT_HERESY_HIGH_UP", f"Kabała: Próg Górny Pasma {hb[1]} → {hb[1]+2} (Rozszerzenie w górę)", "Poziom 2: Warunki Zwycięstwa", {"kt_heresy_band": (hb[0], hb[1]+2)}),
        ("L2_KT_HERESY_BAND_NARROW", "Kabała: Całe Pasmo Wąskie (4–6)", "Poziom 2: Warunki Zwycięstwa", {"kt_heresy_band": (4, 6)}),
        ("L2_KT_HERESY_BAND_WIDE", "Kabała: Całe Pasmo Szerokie (2–9)", "Poziom 2: Warunki Zwycięstwa", {"kt_heresy_band": (2, 9)}),

        # Gildia Cieni
        ("L2_GC_FALLS_DEFAULT_PLUS1", "Gildia: Wymóg Upadków (z Oficjum) 2 → 3", "Poziom 2: Warunki Zwycięstwa", {"gc_falls_default_offset": 1}),
        ("L2_GC_FALLS_DEFAULT_MINUS1", "Gildia: Wymóg Upadków (z Oficjum) 2 → 1", "Poziom 2: Warunki Zwycięstwa", {"gc_falls_default_offset": -1}),
        ("L2_GC_FALLS_NO_SO_PLUS1", "Gildia: Wymóg Upadków (bez Oficjum) 3 → 4", "Poziom 2: Warunki Zwycięstwa", {"gc_falls_no_oficjum_offset": 1}),
        ("L2_GC_FALLS_NO_SO_MINUS1", "Gildia: Wymóg Upadków (bez Oficjum) 3 → 2", "Poziom 2: Warunki Zwycięstwa", {"gc_falls_no_oficjum_offset": -1}),

        # ══════════════════════════════════════════════════════════════
        # POZIOM 4: WARIANTY NISZOWE I MODYFIKATORY GLOBALNE
        # ══════════════════════════════════════════════════════════════
        ("L4_NO_TIME_DECK", "Kronika Dziejów: Całkowite wyłączenie edyktów czasu", "Poziom 4: Warianty i Modyfikatory", {"no_time_deck": True}),
        ("L4_TIME_DECK_EVERY_2ERAS", "Kronika Dziejów: Częstotliwość co 2 Ery", "Poziom 4: Warianty i Modyfikatory", {"time_deck_freq": 2}),
        ("L4_VERDICT_SECRET", "Werdykt Sądu: Tajny (brak koordynacji anty-snowball)", "Poziom 4: Warianty i Modyfikatory", {"verdict_secret": True}),
        ("L4_SEA_ROUTE_ERA4", "Szlak Morski: Odblokowanie w Erze 4 (Wczesne)", "Poziom 4: Warianty i Modyfikatory", {"sea_route_era": 4}),
        ("L4_SEA_ROUTE_ERA6", "Szlak Morski: Odblokowanie w Erze 6 (Późne)", "Poziom 4: Warianty i Modyfikatory", {"sea_route_era": 6}),
        ("L4_INQUISITOR_SPEED0", "Inkwizytor Patrol: Ruch 0 pól (Stacjonarny)", "Poziom 4: Warianty i Modyfikatory", {"inquisitor_speed": 0}),
        ("L4_INQUISITOR_SPEED2", "Inkwizytor Patrol: Ruch 2 pola (Szybki patrol)", "Poziom 4: Warianty i Modyfikatory", {"inquisitor_speed": 2}),
    ]

    return [(t[0], t[1], t[2], t[3], games_per_setup, seed, setups) for t in tasks]


def run_full_ablation_audit_4p(games_per_setup: int = 5000, seed: int = 42, workers: int = 10) -> Path:
    """Executes the complete 4P ablation study across all 50 faction cards, time deck, and system mechanics."""
    t_start = time.time()
    setups = CANONICAL_4P_SETUPS
    all_cards = load_all_cards()

    print("═══════════════════════════════════════════════════════════════════════")
    print("   INQUISITIO-1492 — BADANIE UŻYTECZNOŚCI I WPŁYWU W KANONIE 4P        ")
    print("   Analiza ablacyjna (Leave-One-Out) dla 50 kart i mechanik w 4P       ")
    print("═══════════════════════════════════════════════════════════════════════")
    print(f"Bieżąca wersja:            {CONFIG.version}")
    print(f"Kanon Setupy:              {', '.join(setups)}")
    print(f"Wielkość próby:            {games_per_setup} gier/setup × {len(setups)} setupów 4P ({games_per_setup * len(setups)} gier per wariant)")
    print(f"Wątki procesora:           {workers}")
    print("═══════════════════════════════════════════════════════════════════════\n")

    # 1. Baseline 4P Measurement
    print(f"🔍 [1/4] POMIAR BAZOWY KANONU 4P (Wszystkie elementy aktywne)...")
    base_task = ("BASE_4P", "Kanon 4P — Wszystkie Elementy Aktywne", {}, games_per_setup, seed, setups)
    base_res = _run_ablation_task_4p(base_task)

    print(f"   🎯 Wynik Kanonu 4P Score: {color_score(base_res['score_4p'], bold=True)} pkt")
    for sname, sc in sorted(base_res["setup_scores"].items()):
        print(f"      • `{sname}`: {color_score(sc, bold=True)} pkt")
    print(f"   📊 Udziały Frakcji w 4P (Kanon: idealne 25.0%):")
    for fname, sh in sorted(base_res["faction_shares"].items()):
        print(f"      • {fname:<4s}: {sh:5.1f}%")
    print(f"   ⏱️ Średnia Er: {base_res['eras_avg']:.2f} | Deadlocks: {base_res['deadlock_pct']:.1f}% | Pas Biedy: {base_res['poverty_pct']:.1f}%\n")

    # 2. Build Card Ablation Tasks (50 faction cards)
    card_tasks = []
    card_meta = {}
    for cid, card in sorted(all_cards.items()):
        pref = cid.split("-")[0]
        if pref not in PREFIX_TO_FACTION_ID:
            continue
        fname = FACTION_FULL_NAMES.get(pref, pref)
        card_name = card.name
        card_tasks.append((
            f"ABLATION_{cid.upper()}",
            f"Brak karty {cid} ({card_name})",
            {"disabled_cards": [cid]},
            games_per_setup,
            seed,
            setups,
        ))
        card_meta[f"ABLATION_{cid.upper()}"] = {
            "id": cid,
            "name": card_name,
            "faction_code": pref,
            "faction_name": fname,
            "cost": card.cost,
            "heresy": card.heresy,
            "type": card.type,
            "layer": card.layer,
        }

    # 3. Build Time Deck Ablation Tasks (8 cards)
    time_cards = [
        ("tc-01", "Kres Średniowiecza"),
        ("tc-02", "Płonący Stos"),
        ("tc-03", "Królewski Podatek"),
        ("tc-04", "Spisek w Cieniu"),
        ("tc-05", "Złoty Wiek"),
        ("tc-06", "Czystka w Mieście"),
        ("tc-07", "Druga Szansa"),
        ("tc-08", "Zaćmienie Słońca"),
    ]
    time_tasks = []
    for t_id, t_name in time_cards:
        time_tasks.append((
            f"TIME_{t_id.upper()}",
            f"Brak wydarzenia {t_id} ({t_name})",
            {"disabled_cards": [t_id]},
            games_per_setup,
            seed,
            setups,
        ))

    # 4. Build Full System & Victory Path Ablation Tasks
    mech_tasks_raw = build_all_mechanic_tasks(games_per_setup, seed, setups)
    mech_tasks = [(t[0], t[1], t[3], t[4], t[5], t[6]) for t in mech_tasks_raw]
    mech_meta = {t[0]: {"id": t[0], "name": t[1], "category": t[2], "overrides": t[3]} for t in mech_tasks_raw}

    all_tasks = card_tasks + time_tasks + mech_tasks
    total_tasks = len(all_tasks)

    print(f"⏳ [2/4] URUCHAMIAM {total_tasks} ZADAŃ ABLACYJNYCH DLA KANONU 4P...")
    print(f"   (50 Kart Frakcji + 8 Kart Czasu + {len(mech_tasks)} Mechanik Systemowych L1/L2/L4)")
    results_map = {}

    t_pool = time.time()
    with ProcessPoolExecutor(max_workers=workers) as executor:
        from concurrent.futures import as_completed
        future_to_id = {executor.submit(_run_ablation_task_4p, t): t[0] for t in all_tasks}

        for idx, future in enumerate(as_completed(future_to_id), 1):
            res = future.result()
            results_map[res["id"]] = res

            elapsed = time.time() - t_pool
            rate = idx / elapsed if elapsed > 0 else 0
            eta_s = (total_tasks - idx) / rate if rate > 0 else 0
            eta_str = f"{int(eta_s // 60)}m {int(eta_s % 60):02d}s" if eta_s >= 60 else f"{int(eta_s)}s"

            sys.stdout.write(f"\r⏳ [Ablacja 4P] [{idx:3d}/{total_tasks:3d}] ({idx*100.0/total_tasks:5.1f}%) | {rate:4.1f} zad/s | ETA: {eta_str:<8s} | Ostatni: {res['id'][:24]:<24s}  ")
            sys.stdout.flush()

    sys.stdout.write(f"\n   ✔ Ukończono wszystkie {total_tasks} zadań ablacyjnych 4P w {round(time.time() - t_pool, 1)}s.\n\n")

    # 5. Process & Classify Card Results
    print("🔬 [3/4] ANALIZUJĘ I KLASYFIKUJĘ KARTY ORAZ MECHANIKI W MATRYCY 3x3 DLA KANONU 4P...")
    analyzed_cards = []

    for task in card_tasks:
        t_id = task[0]
        res = results_map[t_id]
        meta = card_meta[t_id]
        pref = meta["faction_code"]
        fid_obj = PREFIX_TO_FACTION_ID[pref]
        f_short = FACTION_NAMES[fid_obj]

        base_f_share = base_res["faction_shares"].get(f_short, 25.0)
        ablated_f_share = res["faction_shares"].get(f_short, 25.0)

        # d_share > 0 means removing card decreased winrate (card was driving wins)
        d_share = round(base_f_share - ablated_f_share, 1)

        # d_4p > 0 means removing card increased 4P score (card was destabilizing 4P)
        d_4p = round(res["score_4p"] - base_res["score_4p"], 1)

        sub_id, role_name, group_id = classify_card_impact_4p(d_share, d_4p)

        analyzed_cards.append({
            "id": meta["id"],
            "name": meta["name"],
            "faction_code": pref,
            "faction_name": meta["faction_name"],
            "f_short": f_short,
            "cost": meta["cost"],
            "heresy": meta["heresy"],
            "type": meta["type"],
            "layer": meta["layer"],
            "base_share": base_f_share,
            "ablated_share": ablated_f_share,
            "d_share": d_share,
            "score_4p": res["score_4p"],
            "d_4p": d_4p,
            "sub_id": sub_id,
            "role_name": role_name,
            "group_id": group_id,
            "eras_avg": res["eras_avg"],
            "deadlock_pct": res["deadlock_pct"],
            "poverty_pct": res["poverty_pct"],
        })

    analyzed_cards.sort(key=lambda c: (c["faction_code"], c["layer"], c["cost"]))

    # 6. Process Time Cards
    analyzed_time_cards = []
    for t_id, t_name in time_cards:
        t_key = f"TIME_{t_id.upper()}"
        res = results_map[t_key]
        d_4p = round(res["score_4p"] - base_res["score_4p"], 1)
        status = "🟢 Stabilizator tempa" if d_4p <= -1.0 else ("⚠️ Spowalniacz" if d_4p >= 1.0 else "⚖️ Neutralna Kronika")
        analyzed_time_cards.append({
            "id": t_id,
            "name": t_name,
            "score_4p": res["score_4p"],
            "d_4p": d_4p,
            "eras_avg": res["eras_avg"],
            "deadlock_pct": res["deadlock_pct"],
            "status": status,
        })

    # 7. Process Mechanics in 9-Area Matrix
    analyzed_mechanics = []
    for task in mech_tasks:
        m_id = task[0]
        res = results_map[m_id]
        meta = mech_meta[m_id]

        d_4p = round(res["score_4p"] - base_res["score_4p"], 1)
        max_d_share = max([abs(base_res["faction_shares"].get(fn, 25.0) - res["faction_shares"].get(fn, 25.0)) for fn in base_res["faction_shares"]] or [0.0])

        sub_id, role_name, group_id = classify_mechanic_impact_4p(d_4p, max_d_share)

        analyzed_mechanics.append({
            "id": m_id,
            "name": meta["name"],
            "category": meta["category"],
            "score_4p": res["score_4p"],
            "d_4p": d_4p,
            "max_d_share": max_d_share,
            "sub_id": sub_id,
            "role_name": role_name,
            "group_id": group_id,
            "eras_avg": res["eras_avg"],
            "deadlock_pct": res["deadlock_pct"],
            "poverty_pct": res["poverty_pct"],
        })

    # 8. Build Comprehensive Markdown Report
    print("📝 [4/4] GENERUJĘ PEŁNY RAPORT UŻYTECZNOŚCI I WPŁYWU DLA KANONU 4P...")

    lines = [
        f"# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja {CONFIG.version}",
        "",
        f"**Wersja Gry:** `{CONFIG.version}` | **Data Badania:** {datetime.now().strftime('%Y-%m-%d %H:%M')} | **Próba:** {games_per_setup} gier/setup ({games_per_setup * len(setups)} gier na wariant) | **Ziarno:** {seed}",
        f"**Wynik Bazowy Kanonu 4P:** {color_score(base_res['score_4p'], bold=True)} pkt | **Średnia Długość Partii:** `{base_res['eras_avg']:.2f} Er` | **Deadlocki:** `{base_res['deadlock_pct']:.1f}%` | **Pas Biedy:** `{base_res['poverty_pct']:.1f}%`",
        "",
        "---",
        "",
        "## 1. 🗺️ Podsumowanie Ekosystemu Kart Kanonu 4P (Matryca Wpływu Kart 3x3)",
        "",
        "Rozkład wszystkich 50 kart frakcyjnych w matrycy **Wpływ na Frakcję ($\\Delta \\text{Share}$)** vs **Wpływ na Kanon 4P ($\\Delta \\text{4P Score}$)**:",
        "",
        "| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |",
        "| :--- | :---: | :---: | :--- | :--- |",
    ]

    group_counts = {
        "STABILIZER": len([c for c in analyzed_cards if c["group_id"] == "STABILIZER"]),
        "DISRUPTOR": len([c for c in analyzed_cards if c["group_id"] == "DISRUPTOR"]),
        "DEAD_WEIGHT": len([c for c in analyzed_cards if c["group_id"] == "DEAD_WEIGHT"]),
        "BALANCED": len([c for c in analyzed_cards if c["group_id"] == "BALANCED"]),
    }

    lines.extend([
        f"| 👑 / ⚓ **Filar / Kotwica Kanonu** | **{group_counts['STABILIZER']}** | {group_counts['STABILIZER']*2}% | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |",
        f"| ⚖️ **Zbalansowane Narzędzie** | **{group_counts['BALANCED']}** | {group_counts['BALANCED']*2}% | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Optymalne** |",
        f"| 💤 **Karta Pasywna (Dead Weight)** | **{group_counts['DEAD_WEIGHT']}** | {group_counts['DEAD_WEIGHT']*2}% | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia** |",
        f"| ⚠️ **Karta Destabilizująca (Disruptor)** | **{group_counts['DISRUPTOR']}** | {group_counts['DISRUPTOR']*2}% | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |",
        "",
        "---",
        "",
        "## 2. 🃏 Warstwa I — Szczegółowa Analiza 50 Kart Frakcji w Kanonie 4P",
        "",
        "### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)",
        "Karty, których brak powoduje spadek wyniku Kanonu 4P o $\\ge 4.0$ pkt lub załamanie winrate frakcji o $\\ge 4.0\\%$:",
        "",
        "| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\\Delta$ Frakcji | 4P Score po Wyłączeniu |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: |",
    ])

    stabilizers = sorted([c for c in analyzed_cards if c["group_id"] == "STABILIZER"], key=lambda x: x["d_4p"])
    for c in stabilizers:
        ds_sign = f"-{c['d_share']:.1f}%" if c['d_share'] > 0 else f"+{abs(c['d_share']):.1f}%"
        lines.append(
            f"| `{c['id']}` **{c['name']}** | {c['faction_name']} | {c['cost']}zł / {c['heresy']}☣ | "
            f"{c['role_name']} | {c['base_share']:.1f}% → **{c['ablated_share']:.1f}%** | "
            f"**`{ds_sign}`** | {base_res['score_4p']:.1f} → **{c['score_4p']:.1f} pkt** (`{c['d_4p']:.1f}`) |"
        )

    lines.extend([
        "",
        "### 2.2. ⚠️ Karty Destabilizujące Kanon 4P (Disruptors)",
        "Karty, których wyłączenie podnosi 4P Score ($\\Delta \\text{4P} \\ge +1.5$ pkt):",
        "",
        "| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\\Delta$ Frakcji | 4P Score po Wyłączeniu |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: |",
    ])

    disruptors = sorted([c for c in analyzed_cards if c["group_id"] == "DISRUPTOR"], key=lambda x: x["d_4p"], reverse=True)
    if not disruptors:
        lines.append("| *Brak kart destabilizujących* | - | - | - | - | - | - |")
    for c in disruptors:
        ds_sign = f"-{c['d_share']:.1f}%" if c['d_share'] > 0 else f"+{abs(c['d_share']):.1f}%"
        lines.append(
            f"| `{c['id']}` **{c['name']}** | {c['faction_name']} | {c['cost']}zł / {c['heresy']}☣ | "
            f"{c['role_name']} | {c['base_share']:.1f}% → **{c['ablated_share']:.1f}%** | "
            f"`{ds_sign}` | {base_res['score_4p']:.1f} → **{c['score_4p']:.1f} pkt** (`{c['d_4p']:+.1f}`) |"
        )

    lines.extend([
        "",
        "### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich 50 Kart Frakcji w Kanonie 4P",
        "",
        "| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Faction Win Share 4P | $\\Delta$ Frakcji | 4P Score | $\\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |",
        "| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |",
    ])

    for c in analyzed_cards:
        ds_sign = f"-{c['d_share']:.1f}%" if c['d_share'] > 0 else f"+{abs(c['d_share']):.1f}%"
        d4_sign = f"+{c['d_4p']:.1f}" if c['d_4p'] > 0 else f"{c['d_4p']:.1f}"
        lines.append(
            f"| `{c['id']}` | **{c['name']}** | {c['faction_name']} | {c['cost']} | {c['heresy']} | "
            f"{c['base_share']:.1f}% → {c['ablated_share']:.1f}% | `{ds_sign}` | "
            f"{c['score_4p']:.1f} | `{d4_sign}` | {c['eras_avg']:.2f} | {c['deadlock_pct']:.1f}% | {c['role_name']} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 3. ⏳ Warstwa II — Kronika Dziejów w 4P (Ablacja 8 Kart Wydarzeń Czasu)",
        "",
        "Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans w 4P:",
        "",
        "| ID | Karta Wydarzenia | 4P Score | $\\Delta$ 4P | Średnia Er | Deadlock % | Status Roli w Kronice |",
        "| :--- | :--- | :---: | :---: | :---: | :---: | :--- |",
    ])

    for tc in analyzed_time_cards:
        d4_str = f"+{tc['d_4p']:.1f}" if tc['d_4p'] > 0 else f"{tc['d_4p']:.1f}"
        lines.append(
            f"| `{tc['id']}` | **{tc['name']}** | {score_pair(base_res['score_4p'], tc['score_4p'], colored=True)} | "
            f"`{d4_str} pkt` | {tc['eras_avg']:.2f} Er | {tc['deadlock_pct']:.1f}% | {tc['status']} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 4. ⚙️ Warstwa III — Matryca 9 Obszarów Wpływu Mechanik Gry (L1, L2, L4)",
        "",
        "Zestawienie odporności Kanonu 4P na modyfikacje i ablację poszczególnych podsystemów według 9 obszarów istotności i efektu:",
        "",
        "| Kategoria Mechaniki | Liczba Testów | Rola w Ekosystemie Kanonu 4P | Rekomendacja Balansowa |",
        "| :--- | :---: | :--- | :--- |",
    ])

    mech_groups = {
        "STABILIZER": len([m for m in analyzed_mechanics if m["group_id"] == "STABILIZER"]),
        "NEUTRAL": len([m for m in analyzed_mechanics if m["group_id"] == "NEUTRAL"]),
        "DISRUPTOR": len([m for m in analyzed_mechanics if m["group_id"] == "DISRUPTOR"]),
    }

    lines.extend([
        f"| 👑 / 🛡️ **Filary i Bezpieczniki Stabilizujące** | **{mech_groups['STABILIZER']}** | Mechaniki krytyczne — ich brak lub rozregulowanie niszczy balans | **Nienaruszalny Kanon** |",
        f"| ⚖️ **Zbalansowane Regulatory / Pasywne** | **{mech_groups['NEUTRAL']}** | Mechaniki harmonijnie wpisane w dynamikę rozgrywki | **Optymalne w Kanonie** |",
        f"| ⚠️ / 💡 **Obciążenia i Kandydaci do Uproszczenia** | **{mech_groups['DISRUPTOR']}** | Mechaniki, których modyfikacja lub redukcja podnosi wynik 4P | **Kandydaci do optymalizacji** |",
        "",
        "### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)",
        "",
        "| Badany Podsystem / Modyfikator L1 | 4P Score | $\\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :--- |",
    ])

    for m in [m for m in analyzed_mechanics if m["category"] == "Poziom 1: System Core"]:
        d4_str = f"+{m['d_4p']:.1f}" if m['d_4p'] > 0 else f"{m['d_4p']:.1f}"
        lines.append(
            f"| **{m['name']}** | {score_pair(base_res['score_4p'], m['score_4p'], colored=True)} | "
            f"`{d4_str} pkt` | {m['eras_avg']:.2f} Er | {m['deadlock_pct']:.1f}% | {m['poverty_pct']:.1f}% | {m['role_name']} |"
        )

    lines.extend([
        "",
        "### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)",
        "",
        "| Badany Warunek Zwycięstwa L2 | 4P Score | $\\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :--- |",
    ])

    for m in [m for m in analyzed_mechanics if m["category"] == "Poziom 2: Warunki Zwycięstwa"]:
        d4_str = f"+{m['d_4p']:.1f}" if m['d_4p'] > 0 else f"{m['d_4p']:.1f}"
        lines.append(
            f"| **{m['name']}** | {score_pair(base_res['score_4p'], m['score_4p'], colored=True)} | "
            f"`{d4_str} pkt` | {m['eras_avg']:.2f} Er | {m['deadlock_pct']:.1f}% | {m['poverty_pct']:.1f}% | {m['role_name']} |"
        )

    lines.extend([
        "",
        "### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)",
        "",
        "| Badany Wariant / Modyfikator L4 | 4P Score | $\\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :--- |",
    ])

    for m in [m for m in analyzed_mechanics if m["category"] == "Poziom 4: Warianty i Modyfikatory"]:
        d4_str = f"+{m['d_4p']:.1f}" if m['d_4p'] > 0 else f"{m['d_4p']:.1f}"
        lines.append(
            f"| **{m['name']}** | {score_pair(base_res['score_4p'], m['score_4p'], colored=True)} | "
            f"`{d4_str} pkt` | {m['eras_avg']:.2f} Er | {m['deadlock_pct']:.1f}% | {m['poverty_pct']:.1f}% | {m['role_name']} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 5. 👥 Warstwa IV — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji",
        "",
        "Zestawienie stabilności 5 wariantów 4-osobowych w Kanonie 4P:",
        "",
        "| Nieobecna Frakcja | Setup Testowy | 4P Score Setupu | Diagnoza Wpływu Braku Frakcji na Stół 4P |",
        "| :--- | :--- | :---: | :--- |",
        f"| **Bez Gildii Cieni** | `4p-core` | **`{base_res['setup_scores'].get('4p-core', 0.0):.1f} pkt`** | Stół klasyczny (czysta walka religijno-polityczna) |",
        f"| **Bez Kabały z Toledo** | `4p-no-kabala` | **`{base_res['setup_scores'].get('4p-no-kabala', 0.0):.1f} pkt`** | Brak presji okultystycznej i manipulacji czasem |",
        f"| **Bez Korony i Borgiów** | `4p-no-korona` | **`{base_res['setup_scores'].get('4p-no-korona', 0.0):.1f} pkt`** | Brak presji podatkowej i aresztów królewskich |",
        f"| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`{base_res['setup_scores'].get('4p-no-cienie', 0.0):.1f} pkt`** | Brak szlaków morskich i ucieczek podziemiami |",
        f"| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`{base_res['setup_scores'].get('4p-no-oficjum', 0.0):.1f} pkt`** | Brak presji stosów i bezpośredniego Inkwizytora |",
    ])

    report_path, arch_path = save_and_archive_report(lines, "raport_uzytecznosci_i_wplywu_4p.md")
    print(f"\n✅ PEŁNY RAPORT UŻYTECZNOŚCI I WPŁYWU 4P WYGENEROWANY POMYŚLNIE!")
    print(f"   Raport:    {report_path}")
    print(f"   Archiwum:  {arch_path}\n")
    return report_path


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 Feature & Card Impact Audit for Kanon 4P (Ablation Study 4P)")
    parser.add_argument("--games", type=int, default=5000, help="Liczba gier na setup (domyślnie: 5000, min. 1000)")
    parser.add_argument("--workers", type=int, default=min(os.cpu_count() or 4, 10), help="Liczba wątków równoległych")
    parser.add_argument("--seed", type=int, default=42, help="Ziarno losowe (CRN)")

    args = parser.parse_args()
    run_full_ablation_audit_4p(games_per_setup=args.games, seed=args.seed, workers=args.workers)


if __name__ == "__main__":
    main()
