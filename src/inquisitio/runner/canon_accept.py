"""4P canon accept rules — legacy (max mean score) vs band (maximin / hygiene).

Vitality is a veto, not part of the 4P balance number.
"""
from __future__ import annotations

from dataclasses import dataclass

TARGET_BAND_PCT = (20.0, 30.0)
RED_LINE_PCT = (15.0, 35.0)
CORE_SCORE_FLOOR = 90.0
CORE_SETUP = "4p-core"


@dataclass(frozen=True)
class AcceptDecision:
    accepted: bool
    reason: str
    phase: str  # legacy | climb | hygiene


def telemetry_is_safe(res: dict, *, relax_era: bool = False) -> tuple[bool, str]:
    """Hard telemetry veto. Era window is hygiene for a table already in band.

    Climb (wrecked 4P, shares outside 20–30%): do not freeze apply because the
    base is already under 4.5 Er — that is how v0.96 sat at 8.5 pkt with 0 patches.
    Deadlock / poverty stay hard. Blowout length (<3 or >9 Er) still vetoes.
    """
    if res.get("deadlock_pct", 0) > 5.0:
        return False, f"Deadlock {res['deadlock_pct']:.1f}% > 5.0%"
    if res.get("poverty_pct", 0) > 30.0:
        return False, f"Pas Biedy {res['poverty_pct']:.1f}% > 30.0%"
    eras = res.get("eras_avg", 5.5)
    if relax_era:
        if eras < 3.0 or eras > 9.0:
            return False, f"Śr. Er {eras:.2f} poza zakresem wspinaczki [3.0, 9.0]"
        return True, "OK"
    if eras < 4.5 or eras > 7.0:
        return False, f"Śr. Er {eras:.2f} poza zakresem [4.5, 7.0]"
    return True, "OK"


def setup_shares_in_range(
    setup_shares: dict[str, dict[str, float]],
    lo: float,
    hi: float,
) -> bool:
    """True if every faction share in every setup is inside [lo, hi] percent."""
    if not setup_shares:
        return False
    for shares in setup_shares.values():
        if not shares:
            return False
        for pct in shares.values():
            if pct < lo or pct > hi:
                return False
    return True


def telemetry_distance(res: dict) -> float:
    """Lower is healthier. Deadlock, poverty, era window, accusation window."""
    deadlock = max(0.0, float(res.get("deadlock_pct", 0.0)))
    poverty = max(0.0, float(res.get("poverty_pct", 0.0)))
    eras = float(res.get("eras_avg", 5.5))
    if eras < 5.0:
        eras_pen = 5.0 - eras
    elif eras > 6.5:
        eras_pen = eras - 6.5
    else:
        eras_pen = 0.0
    acc = float(res.get("acc_avg", 3.0))
    if acc < 2.0:
        acc_pen = 2.0 - acc
    elif acc > 4.5:
        acc_pen = acc - 4.5
    else:
        acc_pen = 0.0
    return deadlock / 5.0 + poverty / 30.0 + eras_pen + acc_pen


# Minimalny spadek telemetry_distance, żeby nie brać szumu (np. deadlock 1.0% → 0.8%).
HEALTH_DISTANCE_MIN = 0.25


def table_is_healthy(res: dict) -> bool:
    """Mechanics a player would notice in a few games: flow + signature vitality."""
    if float(res.get("vitality_penalty", 0.0)) > 1e-9:
        return False
    if float(res.get("deadlock_pct", 0.0)) > 5.0:
        return False
    if float(res.get("poverty_pct", 0.0)) > 15.0:
        return False
    eras = float(res.get("eras_avg", 5.5))
    if eras < 4.5 or eras > 7.0:
        return False
    acc = float(res.get("acc_avg", 3.0))
    if acc < 2.0 or acc > 4.5:
        return False
    return True


def health_improved(cand: dict, base: dict) -> bool:
    if cand.get("vitality_penalty", 0.0) < base.get("vitality_penalty", 0.0) - 1e-9:
        return True
    drop = telemetry_distance(base) - telemetry_distance(cand)
    return drop >= HEALTH_DISTANCE_MIN


def table_has_share_foundation(res: dict) -> bool:
    """True when every 4P setup is already inside the 15–35% red line.

    Below that, ±1 points at crutches (lower live goals) and climbing from the
    pit would lock a bad local optimum. L2 / hand SSOT first; auditor protects
    a ridge (breaking it lowers score).
    """
    return setup_shares_in_range(res.get("setup_shares") or {}, *RED_LINE_PCT)


def canon_should_stop(base: dict, *, mode: str) -> bool:
    """Always False — auditor runs until no candidate improves the score."""
    return False


def _score(res: dict) -> float:
    """4P canon score: pure win-share balance. Vitality is a separate veto."""
    return float(res.get("score_4p_balance") or res.get("score_4p") or 0.0)


def rank_key(res: dict) -> tuple:
    """Sort key (lower is better) for the 4P funnel.

    Prioritizes vitality compliance (vit penalty == 0), then win-share balance descending,
    then min_balance descending.
    """
    score_4p = _score(res)
    min_b = float(res.get("min_balance") or score_4p)
    vit = float(res.get("vitality_penalty") or 0.0)
    vit_flag = 1 if vit > 1e-9 else 0
    return (vit_flag, vit, -score_4p, -min_b)




def accept_candidate(
    base: dict,
    cand: dict,
    *,
    min_delta: float = 0.05,
) -> AcceptDecision:
    """Decide whether a verified 4P candidate may be applied."""
    safe, msg = telemetry_is_safe(cand)
    if not safe:
        return AcceptDecision(False, msg, "legacy")
    # Hard Vitality Gate: Do not accept any patch that carries vitality penalty > 0.10
    cand_vit = cand.get("vitality_penalty", 0.0)
    base_vit = base.get("vitality_penalty", 0.0)
    if cand_vit > 0.10:
        return AcceptDecision(False, f"legacy: naruszenie witalności (kara {cand_vit:.3f} > 0.10)", "legacy")
    if cand_vit > base_vit + 1e-9:
        return AcceptDecision(False, f"legacy: witalność gorsza niż baza (kara {cand_vit:.2f} > {base_vit:.2f})", "legacy")
    d = _score(cand) - _score(base)
    dmin = float(cand.get("min_balance", 0.0)) - float(base.get("min_balance", 0.0))
    # 1. Zysk ogólny bez istotnego psucia podłogi
    if d >= min_delta and dmin >= -0.50:
        return AcceptDecision(True, f"legacy Δscore {d:+.2f} ≥ {min_delta} (dmin {dmin:+.2f})", "legacy")
    # 2. Jednoczesna poprawa średniej i podłogi (Pareto improvement)
    if d >= 0.15 and dmin >= 0.15:
        return AcceptDecision(True, f"legacy Pareto Δscore {d:+.2f} & Δmin {dmin:+.2f}", "legacy")
    # 3. Bardzo duży zysk ogólny dopuszczający lekki trade-off
    if d >= 1.50 and dmin >= -0.75:
        return AcceptDecision(True, f"legacy Duży skok Δscore {d:+.2f} (dmin {dmin:+.2f})", "legacy")
    # 4. Istotna poprawa podłogi (Maximin)
    if dmin >= 0.50 and d >= 0.0:
        return AcceptDecision(True, f"legacy Maximin Δmin {dmin:+.2f} (Δscore {d:+.2f})", "legacy")
    return AcceptDecision(False, f"legacy Δscore {d:+.2f} i Δmin {dmin:+.2f} nie spełniają kryteriów bezpieczeństwa", "legacy")
