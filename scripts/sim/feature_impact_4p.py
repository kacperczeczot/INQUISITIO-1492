#!/usr/bin/env python3
"""INQUISITIO-1492 — BADANIE UŻYTECZNOŚCI I WPŁYWU ELEMENTÓW W KANONIE 4P (Ablation & Impact Audit 4P).

Specjalistyczne narzędzie analityczne do badania wkładu każdego pojedynczego elementu gry w Kanon 4-osobowy (4P):
  1. Ablacja Kart (Per-Card Ablation w 4P): Wyłącza każdą z 50 kart z osobna na 5 setupach 4p:
     - Wpływ na Win Share frakcji w 4P (Kanon: idealne 25.0%)
     - Wpływ na 4P Score = win share (`calculate_balance_score`); witalność osobno, nie w tej liczbie
     - Wpływ na tempo partii (Średnia Er) i wskaźnik deadlocków w 4P
  2. Klasyfikacja Kart w Kanonie 4P (Matryca 2D):
     - 👑 FILAR FRAKCJI W 4P (Core Keystone): Kluczowy motor napędowy wygranych frakcji
     - ⚓ KOTWICA KANONU 4P (Balance Anchor): Bezpiecznik chroniący przed dominacją frakcji
     - ⚠️ KARTA TOKSYCZNA W 4P (Disruptor): Karta, której usunięcie podnosi 4P Score
     - 💤 MARTWA KARTA W 4P (Dead Weight): Znikomy wpływ na grę 4-osobową
     - ⚖️ ZBALANSOWANE NARZĘDZIE 4P (Utility): Zdrowe, elastyczne narzędzie taktyczne
  3. Mechaniki L1/L2/L4: **skrajna wartość albo wyłączenie** (połowa / podwojenie / off).
     Nudges ±1 są w `audit_level1.py` / `audit_level2.py` / `audit_level4.py`, nie tutaj.

Generuje raport w: data/playtesting/sim-reports/raport_uzytecznosci_i_wplywu_4p.md oraz archiwizuje w archive/{version}/.
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
TOOLS_SRC_DIR = Path(__file__).resolve().parent
SRC_DIR = TOOLS_SRC_DIR.parent.parent / "src"

for p in (TOOLS_SRC_DIR, SRC_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

import yaml
from inquisitio.cards.loader import load_all_cards
from inquisitio.config import CONFIG, _CONFIG_PATH
from inquisitio.engine.setup import SETUP_PRESETS, FactionId
from inquisitio.runner.adaptive_racer import extract_config_overrides, merge_override_dicts
from inquisitio.runner.audit_facts import score_pair, save_and_archive_report
from inquisitio.runner.batch import run_batch
from inquisitio.runner.impact_taxonomy import (
    classify_card_impact_4p,
    classify_mechanic_impact_4p,
)
from inquisitio.runner.scoring import (
    calculate_balance_score,
    calculate_setup_score,
    color_score,
    evaluate_vitality,
)

REPORTS_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "playtesting" / "sim-reports"
OUTPUT_REPORT_PATH = REPORTS_DIR / "current" / "raport_uzytecznosci_i_wplywu_4p.md"
REPORT_GAMES_MIN = 5000

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

_DEAD_PATH_ROLE = "💤 UŚPIONA ŚCIEŻKA ZWYCIĘSTWA"
_DEAD_PATH_WARN_RE = re.compile(
    r"Martwa ścieżka (?P<path>\S+) \((?P<fid>[^)]+)\): "
    r"(?P<n>\d+)/(?P<total>\d+) wygranych.*?gra tylko (?P<alive>\S+)"
)
SHARE_GAP_PP = 2.5
TIME_CARD_DEAD_D4P = 0.8
TAX_LIFTS_TABLE_D4P = 1.2


def vitality_dead_path_mechanics(base_res: dict) -> list[dict]:
    """Rows for 4.0 from `evaluate_vitality` warnings (any dual-path label)."""
    warns = base_res.get("vitality_warnings") or []
    score = float(base_res.get("score_4p") or 0.0)
    penalty = float(base_res.get("vitality_penalty") or 0.0)
    worst: dict[tuple[str, str], dict] = {}

    for w in warns:
        m = _DEAD_PATH_WARN_RE.search(w)
        if not m:
            continue
        n = int(m.group("n"))
        total = int(m.group("total"))
        share = n / total if total else 0.0
        key = (m.group("fid"), m.group("path"))
        prev = worst.get(key)
        if prev is None or share < prev["share"]:
            worst[key] = {
                "fid": m.group("fid"),
                "path": m.group("path"),
                "n": n,
                "total": total,
                "alive": m.group("alive"),
                "share": share,
            }

    rows: list[dict] = []
    for item in worst.values():
        slug = re.sub(r"[^a-z0-9]+", "_", f"{item['fid']}_{item['path']}")
        rows.append({
            "id": f"VITALITY_{slug}",
            "name": (
                f"{item['fid']}: ścieżka {item['path']} uśpiona "
                f"({item['n']}/{item['total']}; gra tylko {item['alive']})"
            ),
            "category": "Poziom 2: Warunki Zwycięstwa",
            "score_4p": score,
            "d_4p": 0.0,
            "max_d_share": 0.0,
            "sub_id": "M_DEAD_PATH",
            "role_name": _DEAD_PATH_ROLE,
            "group_id": "DEAD",
            "eras_avg": float(base_res.get("eras_avg") or 0.0),
            "deadlock_pct": float(base_res.get("deadlock_pct") or 0.0),
            "poverty_pct": float(base_res.get("poverty_pct") or 0.0),
            "vitality_penalty": penalty,
        })
    return rows


def format_canon_debt(
    base_res: dict,
    analyzed_cards: list[dict],
    analyzed_time_cards: list[dict],
    analyzed_mechanics: list[dict],
) -> list[str]:
    """Section 0: classifier buckets and vitality rows from this run only."""
    bullets: list[str] = []

    for m in analyzed_mechanics:
        if str(m.get("id", "")).startswith("VITALITY_"):
            bullets.append(
                f"**{m['name']}** — kara witalności `{base_res.get('vitality_penalty', 0):.3f}`"
            )

    shares = base_res.get("faction_shares") or {}
    if shares:
        target = 100.0 / 4
        weak_factions = [
            (fn, sh) for fn, sh in sorted(shares.items(), key=lambda x: x[1])
            if abs(sh - target) >= SHARE_GAP_PP
        ]
        if weak_factions:
            bits = ", ".join(f"{fn} {sh:.1f}%" for fn, sh in weak_factions)
            bullets.append(
                f"**Share |Δ| ≥ {SHARE_GAP_PP:g} pp od {target:.0f}%:** {bits}"
            )

    tax = [c for c in analyzed_cards if c.get("group_id") == "SELF_HARM"]
    tax_lifts_table = [c for c in tax if c.get("d_4p", 0) >= TAX_LIFTS_TABLE_D4P]
    if analyzed_cards and tax:
        bullets.append(f"**Autopodatek (SELF_HARM):** {len(tax)}/{len(analyzed_cards)}")
    if tax_lifts_table:
        names = ", ".join(
            f"`{c['id']}` Δ4P {c['d_4p']:+.1f}"
            for c in sorted(tax_lifts_table, key=lambda x: -x["d_4p"])
        )
        bullets.append(
            f"**SELF_HARM z Δ4P ≥ {TAX_LIFTS_TABLE_D4P:g}:** {names}"
        )

    dead_cards = [c for c in analyzed_cards if c.get("group_id") == "DEAD_WEIGHT"]
    if dead_cards:
        bullets.append(
            "**DEAD_WEIGHT:** "
            + ", ".join(f"`{c['id']}` {c['name']}" for c in dead_cards)
        )

    if analyzed_time_cards:
        dead_tc = [
            t for t in analyzed_time_cards
            if abs(t.get("d_4p") or 0) <= TIME_CARD_DEAD_D4P
        ]
        if dead_tc:
            bullets.append(
                f"**Karty Kroniki |Δ4P| ≤ {TIME_CARD_DEAD_D4P:g}:** "
                f"{len(dead_tc)}/{len(analyzed_time_cards)}"
            )
        deck = next((m for m in analyzed_mechanics if m.get("id") == "L4_NO_TIME_DECK"), None)
        if deck is not None:
            bullets.append(
                f"**Ablacja całej Kroniki (`L4_NO_TIME_DECK`):** "
                f"Δ4P {deck['d_4p']:+.1f} ({deck.get('group_id', '?')})"
            )

    for label, groups in (
        ("WEAK/NEUTRAL", ("WEAK", "NEUTRAL")),
        ("DEAD", ("DEAD",)),
        ("DISRUPTOR", ("DISRUPTOR",)),
    ):
        ms = [
            m for m in analyzed_mechanics
            if m.get("group_id") in groups and not str(m.get("id", "")).startswith("VITALITY_")
        ]
        if ms:
            bullets.append(
                f"**Mechaniki {label}:** " + "; ".join(m["name"] for m in ms)
            )

    if not bullets:
        return []

    return [
        "## 0. Wady z tej próby (nie HUD win share)",
        "",
        "Kubełki klasyfikatora i ostrzeżenia witalności z bieżącego runu.",
        "",
        *[f"- {b}" for b in bullets],
        "",
        "---",
        "",
    ]


def _run_ablation_task_4p(task_args: tuple[str, str, dict, int, int, list[str]]) -> dict:
    """Simulates the 5 canonical 4P setups under a specific ablation / modification."""
    element_id, element_name, sys_overrides, games_per_setup, seed, setups = task_args
    t0 = time.time()

    summaries = []
    setup_scores = {}
    setup_scores_vitality = {}
    faction_wins: dict[str, int] = {}
    faction_total_games: dict[str, int] = {}
    vitality_penalties: list[float] = []
    vitality_warnings: list[str] = []
    card_plays_agg: dict[str, int] = {}
    total_games_all_setups = 0

    for sname in setups:
        summary = run_batch(
            games=games_per_setup,
            setup=sname,
            seed=seed,
            layer="C",
            win_overrides=sys_overrides,
        )
        summaries.append(summary)
        setup_scores[sname] = calculate_balance_score(summary)
        setup_scores_vitality[sname] = calculate_setup_score(summary)
        vit = evaluate_vitality(summary)
        vitality_penalties.append(vit.vitality_penalty)
        for msg in vit.warnings:
            vitality_warnings.append(f"{sname}: {msg}")
        total_games_all_setups += summary.games
        for cid, cnt in summary.card_plays_total.items():
            card_plays_agg[cid] = card_plays_agg.get(cid, 0) + cnt

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
        "setup_scores_vitality": setup_scores_vitality,
        "vitality_penalty": max(vitality_penalties) if vitality_penalties else 0.0,
        "vitality_warnings": vitality_warnings,
        "faction_shares": faction_shares,
        "card_plays_total": card_plays_agg,
        "total_games": total_games_all_setups,
        "eras_avg": eras_avg,
        "deadlock_pct": deadlock_pct,
        "poverty_pct": poverty_pct,
        "autodafe_avg": autodafe_avg,
        "acc_avg": acc_avg,
        "dt": dt,
    }


def _n4(item: Any) -> int:
    if hasattr(item, "raw"):
        item = item.raw()
    if isinstance(item, dict):
        val = item.get("4p", next(iter(item.values()), 0))
        return int(val) if val is not None else 0
    return int(item) if item is not None else 0


def _falls_n(falls: Any) -> int:
    if hasattr(falls, "default"):
        return int(falls.default)
    if isinstance(falls, dict):
        val = falls.get("default", falls.get("no_oficjum", 4))
        return int(val) if val is not None else 4
    return int(falls) if falls is not None else 4


def _win_extremes(cur: int, min_val: int = 1) -> list[tuple[str, int, int]]:
    """Offsets that are not ±1: floor (if |Δ|≥2), double (if |Δ|≥2), or 0→2 / 1→3."""
    rows: list[tuple[str, int, int]] = []
    lo_off = min_val - cur
    if abs(lo_off) >= 2:
        rows.append(("LO", lo_off, min_val))
    if cur == 0:
        rows.append(("HI", 2, 2))
    elif cur == 1:
        rows.append(("HI", 2, 3))
    else:
        hi_val = cur * 2
        hi_off = hi_val - cur
        if abs(hi_off) >= 2:
            rows.append(("HI", hi_off, hi_val))
    return rows


def build_all_mechanic_tasks(games_per_setup: int, seed: int, setups: list[str]) -> list[tuple[str, str, str, dict, int, int, list[str]]]:
    """Extreme / off ablations for L1, L2, L4. ±1 lives in audit_level1/2/4.

    Measurement only. Auditors must not import this catalog into apply-pool.
    """
    v = CONFIG.victory
    sys_cfg = CONFIG.system
    nv = CONFIG.variants
    cat1 = "Poziom 1: System Core"
    cat2 = "Poziom 2: Warunki Zwycięstwa"
    cat4 = "Poziom 4: Warianty i Modyfikatory"
    tasks: list[tuple[str, str, str, dict]] = []

    def add(tid: str, name: str, cat: str, ov: dict) -> None:
        tasks.append((tid, name, cat, ov))

    max_eras = int(sys_cfg.max_eras)
    half_eras = max(1, max_eras // 2)
    if abs(half_eras - max_eras) >= 2:
        add("L1_MAX_ERAS_HALF", f"Limit Er: {max_eras} → {half_eras} (skrajna presja)", cat1, {"max_eras": half_eras})

    th = CONFIG.threshold_for(4)
    for tag, off, new in _win_extremes(th, min_val=1):
        add(f"L1_THRESHOLD_{tag}", f"Próg Oskarżenia: {th} → {new}", cat1, {"threshold_offset": off})

    gold = CONFIG.start_gold_for(4)
    if gold != 0:
        add("L1_START_GOLD_0", f"Złoto startowe: {gold}zł → 0zł (wyłączenie)", cat1, {"start_gold": 0})
    if gold >= 2:
        add("L1_START_GOLD_DOUBLE", f"Złoto startowe: {gold}zł → {gold * 2}zł", cat1, {"start_gold": gold * 2})

    agents = int(sys_cfg.agents_per_player)
    for tag, off, new in _win_extremes(agents, min_val=1):
        add(f"L1_AGENTS_{tag}", f"Liczba Agentów: {agents} → {new}", cat1, {"agents_offset": off})

    hand = CONFIG.hand_limit_for(4)
    for tag, off, new in _win_extremes(hand, min_val=1):
        add(f"L1_HAND_{tag}", f"Limit kart na ręce: {hand} → {new}", cat1, {"hand_limit_offset": off})

    cd = int(sys_cfg.autodafe_cooldown)
    if cd != 0:
        add("L1_AUTODAFE_CD_0", f"Autodafé: cooldown {cd} → 0 (co erę)", cat1, {"autodafe_cooldown": 0})
    add("L1_AUTODAFE_DISABLED", "Autodafé: całkowite wyłączenie", cat1, {"autodafe_cooldown": 99})

    so, caa, kb, kt, gc = v.swiete_oficjum, v.cienie_al_andalus, v.korona_borgiowie, v.kabala_toledo, v.gildia_cieni

    for tag, off, new in _win_extremes(_n4(so.stacks)):
        add(f"L2_SO_STACKS_{tag}", f"Święte Oficjum: stosy {_n4(so.stacks)} → {new}", cat2, {"so_stacks_offset": off})
    for tag, off, new in _win_extremes(_n4(so.condemns)):
        add(f"L2_SO_CONDEMNS_{tag}", f"Święte Oficjum: skazania {_n4(so.condemns)} → {new}", cat2, {"so_condemns_offset": off})
    for tag, off, new in _win_extremes(_n4(caa.relics)):
        add(f"L2_CAA_RELICS_{tag}", f"Cienie: relikwie {_n4(caa.relics)} → {new}", cat2, {"caa_relics_offset": off})
    for tag, off, new in _win_extremes(_n4(kb.decrees)):
        add(f"L2_KB_DECREES_{tag}", f"Korona: dekrety {_n4(kb.decrees)} → {new}", cat2, {"kb_decrees_offset": off})
    kb_hooks_val = int(kb.get("hooks", 0))
    if kb_hooks_val > 0:
        for tag, off, new in _win_extremes(kb_hooks_val, min_val=0):
            add(f"L2_KB_HOOKS_{tag}", f"Korona: wymóg haków {kb_hooks_val} → {new}", cat2, {"kb_hooks_offset": off})
    for tag, off, new in _win_extremes(_n4(kt.fragments)):
        add(f"L2_KT_FRAGS_{tag}", f"Kabała: fragmenty {_n4(kt.fragments)} → {new}", cat2, {"kt_frags_offset": off})
    if hasattr(kt, "era"):
        for tag, off, new in _win_extremes(_n4(kt.era)):
            add(f"L2_KT_ERA_{tag}", f"Kabała: era {_n4(kt.era)} → {new}", cat2, {"kt_era_offset": off})

    hb = kt.get("heresy_band")
    if hb:
        lo_b, hi_b = int(hb[0]), int(hb[1])
        if hi_b - lo_b >= 4:
            mid = (lo_b + hi_b) // 2
            tight = (max(0, mid - 1), mid + 1)
            if tight != (lo_b, hi_b):
                add("L2_KT_HERESY_TIGHT", f"Kabała: pasmo {lo_b}–{hi_b} → {tight[0]}–{tight[1]}", cat2, {"kt_heresy_band": tight})

    for tag, off, new in _win_extremes(_falls_n(gc.falls)):
        add(
            f"L2_GC_FALLS_{tag}",
            f"Gildia: upadki {_falls_n(gc.falls)} → {new}",
            cat2,
            {"gc_falls_offset": off},
        )

    add("L1_INTRIGUE_GOLD_0", "Akcja Gospodarcza: 0zł (brak zysku złota)", cat1, {"intrigue_gold": 0})
    add("L1_INTRIGUE_GOLD_DOUBLE", f"Akcja Gospodarcza: {sys_cfg.intrigue_gold} → {sys_cfg.intrigue_gold * 2} (podwojenie)", cat1, {"intrigue_gold": sys_cfg.intrigue_gold * 2})
    add("L1_OBSERVED_LO", f"Próg Obserwowanej: {sys_cfg.observed_threshold} → 2 (skrajna presja)", cat1, {"observed_threshold": 2})

    add("L4_NO_TIME_DECK", "Kronika Dziejów: całkowite wyłączenie", cat4, {"no_time_deck": True})
    add("L4_TIME_DECK_EVERY_3ERAS", "Kronika Dziejów: co 3 Ery (spowolniony zegar)", cat4, {"time_deck_freq": 3})
    inq = int(getattr(nv, "inquisitor_speed", 1))
    if inq != 0:
        add("L4_INQUISITOR_SPEED0", f"Inkwizytor Patrol: ruch {inq} → 0 (wyłączenie)", cat4, {"inquisitor_speed": 0})
    add("L4_INQUISITOR_SPEED_DOUBLE", "Inkwizytor Patrol: ruch x2 (podwojona prędkość)", cat4, {"inquisitor_speed": 2})
    sea = int(nv.sea_route_era)
    if sea < 90:
        add("L4_SEA_ROUTE_OFF", f"Szlak Morski: era {sea} → nigdy (99)", cat4, {"sea_route_era": 99})

    return [(t[0], t[1], t[2], t[3], games_per_setup, seed, setups) for t in tasks]


def assert_report_sample_size(games_per_setup: int, *, screen: bool) -> None:
    """Archive reports need 5000 games/setup. Smaller N is screen-only."""
    if screen:
        return
    if games_per_setup < REPORT_GAMES_MIN:
        raise SystemExit(
            f"Raport archiwalny wymaga ≥{REPORT_GAMES_MIN} gier/setup "
            f"(dostałem {games_per_setup}). Przesiew: --screen --games N."
        )


def run_full_ablation_audit_4p(
    games_per_setup: int = 5000,
    seed: int = 42,
    workers: int = 10,
    skip_cards: bool = False,
    screen: bool = False,
) -> Path | None:
    """4P ablation: L1/L2/L4 mechanics always; faction + time cards unless skip_cards."""
    assert_report_sample_size(games_per_setup, screen=screen)
    t_start = time.time()
    setups = CANONICAL_4P_SETUPS
    all_cards = load_all_cards() if not skip_cards else {}

    mode = "L1/L2/L4 (bez kart)" if skip_cards else "karty + mechaniki"
    print("═══════════════════════════════════════════════════════════════════════")
    print("   INQUISITIO-1492 — BADANIE UŻYTECZNOŚCI I WPŁYWU W KANONIE 4P        ")
    print(f"   Ablacja 4P — {mode}")
    print("═══════════════════════════════════════════════════════════════════════")
    print(f"Bieżąca wersja:            {CONFIG.version}")
    print(f"Kanon Setupy:              {', '.join(setups)}")
    print(f"Wielkość próby:            {games_per_setup} gier/setup × {len(setups)} setupów 4P ({games_per_setup * len(setups)} gier per wariant)")
    print(f"Wątki procesora:           {workers}")
    if screen:
        print("TRYB:                      PRZESIEW (--screen) — bez archiwum")
    print("═══════════════════════════════════════════════════════════════════════\n")

    # Load active cumulative config overrides
    with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
        raw_cfg = yaml.safe_load(f)
    curr_base_overrides = extract_config_overrides(raw_cfg)

    # 1. Baseline 4P Measurement
    print(f"🔍 [1/4] POMIAR BAZOWY KANONU 4P (Wszystkie elementy aktywne)...")
    base_task = ("BASE_4P", "Kanon 4P — Wszystkie Elementy Aktywne", curr_base_overrides, games_per_setup, seed, setups)
    base_res = _run_ablation_task_4p(base_task)

    print(
        f"   🎯 4P Score (win share): {color_score(base_res['score_4p'], bold=True)} pkt | "
        f"witalność kara {base_res['vitality_penalty']:.3f}"
    )
    for sname, sc in sorted(base_res["setup_scores"].items()):
        vit_sc = base_res["setup_scores_vitality"].get(sname, sc)
        print(f"      • `{sname}`: {color_score(sc, bold=True)} pkt (setup+witalność {color_score(vit_sc)})")
    print("   📊 Udziały Frakcji w 4P (Kanon: idealne 25.0%):")
    for fname, sh in sorted(base_res["faction_shares"].items()):
        print(f"      • {fname:<4s}: {sh:5.1f}%")
    print(
        f"   ⏱️ Średnia Er: {base_res['eras_avg']:.2f} | Deadlocks: {base_res['deadlock_pct']:.1f}% | "
        f"Pas Biedy: {base_res['poverty_pct']:.1f}%"
    )
    warns = base_res.get("vitality_warnings") or []
    if warns:
        print("   💤 Witalność:")
        for w in warns:
            print(f"      • {w}")
    print()

    # 2. Build Card Ablation Tasks (faction cards) — optional
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
            merge_override_dicts(curr_base_overrides, {"disabled_cards": [cid]}),
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

    # 3. Build Time Deck Ablation Tasks (dynamic from docs/game/cards/time-deck)
    from inquisitio.cards.loader import time_cards as get_time_cards
    actual_time_cards = get_time_cards(max_layer="C")
    time_cards = [(tc.id, tc.name) for tc in actual_time_cards]
    time_tasks = []
    for t_id, t_name in time_cards:
        time_tasks.append((
            f"TIME_{t_id.upper().replace('-', '_')}",
            f"Brak wydarzenia {t_id} ({t_name})",
            merge_override_dicts(curr_base_overrides, {"disabled_cards": [t_id]}),
            games_per_setup,
            seed,
            setups,
        ))

    # 4. Build Full System & Victory Path Ablation Tasks
    mech_tasks_raw = build_all_mechanic_tasks(games_per_setup, seed, setups)
    mech_tasks = [(t[0], t[1], merge_override_dicts(curr_base_overrides, t[3]), t[4], t[5], t[6]) for t in mech_tasks_raw]
    mech_meta = {t[0]: {"id": t[0], "name": t[1], "category": t[2], "overrides": t[3]} for t in mech_tasks_raw}

    if skip_cards:
        time_tasks = []
        time_cards = []
        card_tasks = []
        card_meta = {}

    all_tasks = card_tasks + time_tasks + mech_tasks
    total_tasks = len(all_tasks)

    print(f"⏳ [2/4] URUCHAMIAM {total_tasks} ZADAŃ ABLACYJNYCH DLA KANONU 4P...")
    if skip_cards:
        print(f"   (pominięto karty frakcji i kroniki — {len(mech_tasks)} mechanik L1/L2/L4)")
    else:
        print(f"   ({len(card_tasks)} kart frakcji + {len(time_tasks)} kart czasu + {len(mech_tasks)} mechanik L1/L2/L4)")
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

        # Compute play_rate: total plays of this card / total games across all setups
        base_card_plays = base_res.get("card_plays_total", {})
        base_total_games = base_res.get("total_games", 1)
        card_play_count = base_card_plays.get(meta["id"], 0)
        play_rate = round(card_play_count / max(base_total_games, 1), 3)

        sub_id, role_name, group_id = classify_card_impact_4p(d_share, d_4p, play_rate=play_rate)

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
            "play_rate": play_rate,
            "play_count": card_play_count,
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
        t_key = f"TIME_{t_id.upper().replace('-', '_')}"
        res = results_map[t_key]
        d_4p = round(res["score_4p"] - base_res["score_4p"], 1)
        if abs(d_4p) <= 0.4:
            status = "💤 Martwa karta kroniki (Δ≈0)"
        elif d_4p <= -1.0:
            status = "🟢 Stabilizator tempa"
        elif d_4p >= 1.0:
            status = "⚠️ Spowalniacz"
        else:
            status = "⚖️ Neutralna Kronika"
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

    analyzed_mechanics = vitality_dead_path_mechanics(base_res) + analyzed_mechanics

    # 8. Build Comprehensive Markdown Report
    print("📝 [4/4] GENERUJĘ PEŁNY RAPORT UŻYTECZNOŚCI I WPŁYWU DLA KANONU 4P...")

    n_cards = len(analyzed_cards)
    deck_pct = (100.0 / n_cards) if n_cards else 0.0

    def _deck_share(n: int) -> str:
        return f"{n * deck_pct:.1f}%"

    lines = [
        f"# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja {CONFIG.version}",
        "",
        f"**Wersja Gry:** `{CONFIG.version}` | **Data Badania:** {datetime.now().strftime('%Y-%m-%d %H:%M')} | **Próba:** {games_per_setup} gier/setup ({games_per_setup * len(setups)} gier na wariant) | **Ziarno:** {seed}",
        f"**4P Score (win share):** {color_score(base_res['score_4p'], bold=True)} pkt | **Witalność (osobna kara):** `{base_res['vitality_penalty']:.3f}` | **Śr. Er:** `{base_res['eras_avg']:.2f}` | **Deadlocki:** `{base_res['deadlock_pct']:.1f}%` | **Pas Biedy:** `{base_res['poverty_pct']:.1f}%`",
        f"**Udziały 4P:** " + " · ".join(f"{fn} {sh:.1f}%" for fn, sh in sorted(base_res["faction_shares"].items())),
        "",
        "Klasyfikacja L1/L2/L4 i Δ 4P liczą wyłącznie równość win share (`calculate_balance_score`). Kara witalności jest osobno.",
    ]
    if skip_cards:
        lines.extend([
            "",
            "**Tryb:** `--no-cards` — raport bez ablacji kart frakcji i kroniki (tylko L1/L2/L4 i stoły 4P).",
        ])
    warns = base_res.get("vitality_warnings") or []
    if warns:
        lines.extend(["", "**Ostrzeżenia witalności (nie w 4P Score):**"])
        for w in warns:
            lines.append(f"- {w}")
    lines.extend(["", "---", ""])
    lines.extend(format_canon_debt(base_res, analyzed_cards, analyzed_time_cards, analyzed_mechanics))
    if not skip_cards:
        lines.extend([
            f"## 1. 🗺️ Podsumowanie Ekosystemu Kart Kanonu 4P (Matryca Wpływu Kart, {n_cards} kart)",
            "",
            f"Rozkład wszystkich {n_cards} kart frakcyjnych w matrycy **Wpływ na Frakcję ($\\Delta \\text{{Share}}$)** vs **Wpływ na Kanon 4P ($\\Delta \\text{{4P Score}}$)**:",
            "",
            "| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |",
            "| :--- | :---: | :---: | :--- | :--- |",
        ])

        group_counts = {
            "STABILIZER": len([c for c in analyzed_cards if c["group_id"] == "STABILIZER"]),
            "DISRUPTOR": len([c for c in analyzed_cards if c["group_id"] == "DISRUPTOR"]),
            "DEAD_WEIGHT": len([c for c in analyzed_cards if c["group_id"] == "DEAD_WEIGHT"]),
            "SELF_HARM": len([c for c in analyzed_cards if c["group_id"] == "SELF_HARM"]),
            "TEMPO_FILLER": len([c for c in analyzed_cards if c["group_id"] == "TEMPO_FILLER"]),
            "BALANCED": len([c for c in analyzed_cards if c["group_id"] == "BALANCED"]),
        }

        lines.extend([
            f"| 🩸 **Autopodatek (Self-Harm)** | **{group_counts['SELF_HARM']}** | {_deck_share(group_counts['SELF_HARM'])} | Wyłączenie **podnosi** win share własnej frakcji — karta jest haraczem, nie silnikiem | **Rework / osłabienie kosztu, nie filar** |",
            f"| 🔄 **Rozcieńczalnik Talii (Tempo Filler)** | **{group_counts['TEMPO_FILLER']}** | {_deck_share(group_counts['TEMPO_FILLER'])} | Normalna karta tempa — ablacja fałszywie flaguje ją jako autopodatek z powodu odchudzenia talii | **Normalny element deckbuildingu** |",
            f"| 💤 **Karta Pasywna (Dead Weight)** | **{group_counts['DEAD_WEIGHT']}** | {_deck_share(group_counts['DEAD_WEIGHT'])} | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia lub wycięcia** |",
            f"| ⚠️ **Karta Destabilizująca (Disruptor)** | **{group_counts['DISRUPTOR']}** | {_deck_share(group_counts['DISRUPTOR'])} | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |",
            f"| ⚖️ **Zbalansowane Narzędzie** | **{group_counts['BALANCED']}** | {_deck_share(group_counts['BALANCED'])} | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Narzędzie, nie złoty środek całego kanonu** |",
            f"| 👑 / ⚓ **Filar / Kotwica Kanonu** | **{group_counts['STABILIZER']}** | {_deck_share(group_counts['STABILIZER'])} | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |",
            "",
            "---",
            "",
            f"## 2. 🃏 Warstwa I — Szczegółowa Analiza {n_cards} Kart Frakcji w Kanonie 4P",
            "",
            "### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)",
            "Karty, których brak powoduje spadek wyniku Kanonu 4P o $\\ge 4.0$ pkt lub załamanie winrate frakcji o $\\ge 4.0\\%$ — **bez** autopodatków (te są w 2.1b):",
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

        self_harm = sorted([c for c in analyzed_cards if c["group_id"] == "SELF_HARM"], key=lambda x: x["d_share"])
        lines.extend([
            "",
            "### 2.1b. 🩸 Autopodatek Frakcji (Self-Harm)",
            "Karty, których wyłączenie **podnosi** win share własnej frakcji. Gracz zauważy je jako haracz, nawet gdy stół 4P jest równy dzięki temu haraczowi.",
            "",
            "| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\\Delta$ Frakcji | 4P Score po Wyłączeniu |",
            "| :--- | :---: | :---: | :---: | :---: | :---: | :---: |",
        ])
        if not self_harm:
            lines.append("| *Brak kart-autopodatków* | - | - | - | - | - | - |")
        for c in self_harm:
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
            f"### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich {n_cards} Kart Frakcji w Kanonie 4P",
            "",
            "| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Play-Rate | Faction Win Share 4P | $\\Delta$ Frakcji | 4P Score | $\\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |",
            "| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |",
        ])

        for c in analyzed_cards:
            ds_sign = f"-{c['d_share']:.1f}%" if c['d_share'] > 0 else f"+{abs(c['d_share']):.1f}%"
            d4_sign = f"+{c['d_4p']:.1f}" if c['d_4p'] > 0 else f"{c['d_4p']:.1f}"
            pr = c.get('play_rate', 0.0)
            pr_str = f"{pr:.2f}"
            lines.append(
                f"| `{c['id']}` | **{c['name']}** | {c['faction_name']} | {c['cost']} | {c['heresy']} | "
                f"{pr_str} | "
                f"{c['base_share']:.1f}% → {c['ablated_share']:.1f}% | `{ds_sign}` | "
                f"{c['score_4p']:.1f} | `{d4_sign}` | {c['eras_avg']:.2f} | {c['deadlock_pct']:.1f}% | {c['role_name']} |"
            )

        # --- Sekcja Monokultury Talii (Deck Concentration Index) ---
        lines.extend([
            "",
            f"### 2.4. 🎯 Monokultura Talii (Deck Concentration Index)",
            "",
            "Jak mocno skoncentrowane jest zagrywanie kart w obrębie każdej frakcji.",
            "Wskaźnik HHI (Herfindahl–Hirschman Index) mierzy koncentrację: HHI = 1.0 oznacza, że 100% zagrań to 1 karta; HHI ≈ 1/N oznacza idealnie równomierny rozkład.",
            "",
            "| Frakcja | Kart w Talii | Top Karta (Play-Rate) | Top 2 (%) | HHI | Ocena |",
            "| :--- | :---: | :--- | :---: | :---: | :--- |",
        ])
        faction_cards: dict[str, list[dict]] = {}
        for c in analyzed_cards:
            fc = c["faction_code"]
            faction_cards.setdefault(fc, []).append(c)
        for fc in sorted(faction_cards.keys()):
            cards_in_faction = faction_cards[fc]
            total_plays = sum(c.get("play_count", 0) for c in cards_in_faction)
            if total_plays == 0:
                lines.append(f"| {FACTION_FULL_NAMES.get(fc, fc)} | {len(cards_in_faction)} | — | — | — | 💤 Brak danych |") 
                continue
            sorted_by_plays = sorted(cards_in_faction, key=lambda x: x.get("play_count", 0), reverse=True)
            top1 = sorted_by_plays[0]
            top1_pct = (top1.get("play_count", 0) / total_plays * 100.0) if total_plays else 0.0
            top2_pct = top1_pct
            if len(sorted_by_plays) > 1:
                top2_pct += (sorted_by_plays[1].get("play_count", 0) / total_plays * 100.0)
            # HHI = sum of squared shares
            hhi = sum((c.get("play_count", 0) / total_plays) ** 2 for c in cards_in_faction) if total_plays else 0.0
            n_cards_faction = len(cards_in_faction)
            ideal_hhi = 1.0 / n_cards_faction if n_cards_faction else 1.0
            if hhi >= 0.25:
                verdict = "⚠️ Monokultura (>25% HHI)"
            elif hhi >= 0.18:
                verdict = "🟡 Nierównomierny"
            else:
                verdict = "🟢 Zdrowy rozkład"
            lines.append(
                f"| {FACTION_FULL_NAMES.get(fc, fc)} | {n_cards_faction} | "
                f"`{top1['id']}` ({top1.get('play_rate', 0.0):.2f}) | {top2_pct:.1f}% | {hhi:.3f} | {verdict} |"
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
        "Mechaniki w tym raporcie: **skraj albo wyłączenie**. Testy ±1 są w `audit_level1` / `audit_level2` / `audit_level4`. **Δ≈0 nie jest harmonią.**",
        "",
        "| Kategoria Mechaniki | Liczba Testów | Rola w Ekosystemie Kanonu 4P | Rekomendacja Balansowa |",
        "| :--- | :---: | :--- | :--- |",
    ])

    mech_groups = {
        "STABILIZER": len([m for m in analyzed_mechanics if m["group_id"] == "STABILIZER"]),
        "WEAK": len([m for m in analyzed_mechanics if m["group_id"] in ("WEAK", "NEUTRAL")]),
        "DEAD": len([m for m in analyzed_mechanics if m["group_id"] == "DEAD"]),
        "DISRUPTOR": len([m for m in analyzed_mechanics if m["group_id"] == "DISRUPTOR"]),
    }

    lines.extend([
        f"| 👑 / 🛡️ **Filary i Bezpieczniki** | **{mech_groups['STABILIZER']}** | Ablacja wali w stół — gracze czują tę gałkę | **Cel kanonu** |",
        f"| ⚠️ **Za słabe dźwignie** | **{mech_groups['WEAK']}** | Rusza share, nie trzyma stołu — nie jest „zbalansowana” | **Wzmocnić aż będzie filarem** |",
        f"| 💤 **Martwe / uśpione ścieżki** | **{mech_groups['DEAD']}** | Dual-win z witalności albo ablacja Δ≈0 | Wada pomiaru, nie harmonia |",
        f"| ⚠️ / 💡 **Wady bieżącej wartości** | **{mech_groups['DISRUPTOR']}** | Inna wartość gałki **podnosi** 4P — obecny setting szkodzi | **Przekręcić albo rework** |",
        "",
        "### 4.0. ⚠️ Problematyczne mechaniki (osobny wykaz)",
        "Wszystkie mechaniki z grup **DEAD**, **WEAK/NEUTRAL** i **DISRUPTOR**: ścieżki dual-win z `evaluate_vitality`, testy z $|\\Delta\\text{4P}| \\le 0.8$ i ruchem share $\\le 1.5$ pp (DEAD), za słabe dźwignie (WEAK) oraz wady bieżącej wartości (DISRUPTOR).",
        "",
        "| Badany Podsystem | Kategoria | 4P Score | $\\Delta$ 4P | Klasyfikacja |",
        "| :--- | :--- | :---: | :---: | :--- |",
    ])

    problem_mechs = sorted(
        [m for m in analyzed_mechanics if m["group_id"] in ("DEAD", "WEAK", "NEUTRAL", "DISRUPTOR")],
        key=lambda x: ({"DEAD": 0, "WEAK": 1, "NEUTRAL": 1, "DISRUPTOR": 2}.get(x["group_id"], 3), abs(x["d_4p"]), x["name"]),
    )
    if not problem_mechs:
        lines.append("| *Brak problematycznych mechanik w tej próbie* | - | - | - | - |")
    for m in problem_mechs:
        d4_str = f"+{m['d_4p']:.1f}" if m['d_4p'] > 0 else f"{m['d_4p']:.1f}"
        lines.append(
            f"| **{m['name']}** | {m['category']} | {score_pair(base_res['score_4p'], m['score_4p'], colored=True)} | "
            f"`{d4_str} pkt` | {m['role_name']} |"
        )

    lines.extend([
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
        "Zestawienie stabilności 5 wariantów 4-osobowych. Kolumna win share to HUD kanonu; setup+witalność to stary blend (kara martwej ścieżki).",
        "",
        "| Nieobecna Frakcja | Setup Testowy | Win share | Setup+witalność | Diagnoza |",
        "| :--- | :--- | :---: | :---: | :--- |",
        f"| **Bez Gildii Cieni** | `4p-core` | **`{base_res['setup_scores'].get('4p-core', 0.0):.1f}`** | `{base_res['setup_scores_vitality'].get('4p-core', 0.0):.1f}` | Stół klasyczny (czysta walka religijno-polityczna) |",
        f"| **Bez Kabały z Toledo** | `4p-no-kabala` | **`{base_res['setup_scores'].get('4p-no-kabala', 0.0):.1f}`** | `{base_res['setup_scores_vitality'].get('4p-no-kabala', 0.0):.1f}` | Brak presji okultystycznej i manipulacji czasem |",
        f"| **Bez Korony i Borgiów** | `4p-no-korona` | **`{base_res['setup_scores'].get('4p-no-korona', 0.0):.1f}`** | `{base_res['setup_scores_vitality'].get('4p-no-korona', 0.0):.1f}` | Brak presji podatkowej i aresztów królewskich |",
        f"| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`{base_res['setup_scores'].get('4p-no-cienie', 0.0):.1f}`** | `{base_res['setup_scores_vitality'].get('4p-no-cienie', 0.0):.1f}` | Brak szlaków morskich i ucieczek podziemiami |",
        f"| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`{base_res['setup_scores'].get('4p-no-oficjum', 0.0):.1f}`** | `{base_res['setup_scores_vitality'].get('4p-no-oficjum', 0.0):.1f}` | Brak presji stosów i bezpośredniego Inkwizytora |",
    ])

    if screen:
        print("\n⚠️ PRZESIEW — wynik tylko na konsoli, archiwum nie ruszane.")
        return None

    report_path, arch_path = save_and_archive_report(lines, "raport_uzytecznosci_i_wplywu_4p.md")
    print(f"\n✅ PEŁNY RAPORT UŻYTECZNOŚCI I WPŁYWU 4P WYGENEROWANY POMYŚLNIE!")
    print(f"   Raport:    {report_path}")
    print(f"   Archiwum:  {arch_path}\n")
    return report_path


def main():
    parser = argparse.ArgumentParser(description="INQUISITIO-1492 Feature & Card Impact Audit for Kanon 4P (Ablation Study 4P)")
    parser.add_argument(
        "--games",
        type=int,
        default=REPORT_GAMES_MIN,
        help=f"Gier na setup (raport: ≥{REPORT_GAMES_MIN}; mniej tylko z --screen)",
    )
    parser.add_argument("--workers", type=int, default=min(os.cpu_count() or 4, 10), help="Liczba wątków równoległych")
    parser.add_argument("--seed", type=int, default=42, help="Ziarno losowe (CRN)")
    parser.add_argument(
        "--no-cards",
        action="store_true",
        help="Pomiń ablację kart frakcji i kroniki; tylko L1/L2/L4 i odporność stołu 4P",
    )
    parser.add_argument(
        "--screen",
        action="store_true",
        help="Przesiew: wolno <5000 gier/setup, nie zapisuje raportu do archive/",
    )

    args = parser.parse_args()
    run_full_ablation_audit_4p(
        games_per_setup=args.games,
        seed=args.seed,
        workers=args.workers,
        skip_cards=args.no_cards,
        screen=args.screen,
    )


if __name__ == "__main__":
    main()
