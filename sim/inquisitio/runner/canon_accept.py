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
    """Autonomous halt: shares in band and the table is already healthy."""
    if mode != "band":
        return False
    shares = base.get("setup_shares") or {}
    if not setup_shares_in_range(shares, *TARGET_BAND_PCT):
        return False
    return table_is_healthy(base)


def rank_key(res: dict, *, mode: str, base_in_band: bool) -> tuple:
    """Sort key (lower is better) for the 4P funnel.

    Hygiene must not promote wrecked tables just because deadlock/accusations
    look slightly 'healthier' — stay in band and keep 4p-core ≥ 90 first.
    """
    if mode != "band":
        return (-float(res.get("score_4p", 0.0)),)
    min_b = float(res.get("min_balance", res.get("score_4p_balance", 0.0)))
    mean_b = float(res.get("score_4p_balance", res.get("score_4p", 0.0)))
    if not base_in_band:
        return (-min_b, -mean_b)
    in_band = setup_shares_in_range(res.get("setup_shares") or {}, *TARGET_BAND_PCT)
    core = float((res.get("setup_scores_balance") or {}).get(CORE_SETUP, 0.0))
    return (
        0 if in_band else 1,
        0 if core >= CORE_SCORE_FLOOR else 1,
        float(res.get("vitality_penalty", 0.0)),
        telemetry_distance(res),
        -min_b,
    )


def accept_candidate(
    base: dict,
    cand: dict,
    *,
    mode: str = "legacy",
    min_delta: float = 0.05,
) -> AcceptDecision:
    """Decide whether a verified 4P candidate may be applied."""
    if mode == "legacy":
        safe, msg = telemetry_is_safe(cand)
        if not safe:
            return AcceptDecision(False, msg, "legacy")
        d = float(cand.get("score_4p", 0.0)) - float(base.get("score_4p", 0.0))
        if d >= min_delta:
            return AcceptDecision(True, f"legacy Δ {d:+.2f} ≥ {min_delta}", "legacy")
        return AcceptDecision(False, f"legacy Δ {d:+.2f} < {min_delta}", "legacy")

    if mode != "band":
        raise ValueError(f"Unknown accept mode: {mode!r}")

    base_shares = base.get("setup_shares") or {}
    cand_shares = cand.get("setup_shares") or {}
    climbing = not setup_shares_in_range(base_shares, *TARGET_BAND_PCT)

    if not table_has_share_foundation(base):
        return AcceptDecision(
            False,
            "fundament: 4P poza czerwoną linią 15–35%, nie wdrażaj z dołu",
            "foundation",
        )

    safe, msg = telemetry_is_safe(cand, relax_era=climbing)
    if not safe:
        return AcceptDecision(False, msg, "climb")

    if canon_should_stop(base, mode="band"):
        return AcceptDecision(False, "higiena: stół zdrowy, nie ruszaj mechaniki", "hygiene")

    if cand.get("vitality_penalty", 0.0) > base.get("vitality_penalty", 0.0) + 1e-9:
        return AcceptDecision(False, "witalność gorsza niż baza", "climb")

    if not setup_shares_in_range(cand_shares, *RED_LINE_PCT):
        return AcceptDecision(False, "frakcja poza czerwoną linią 15–35%", "climb")

    base_scores = base.get("setup_scores_balance") or {}
    cand_scores = cand.get("setup_scores_balance") or {}
    base_core = float(base_scores.get(CORE_SETUP, 0.0))
    cand_core = float(cand_scores.get(CORE_SETUP, 0.0))
    if base_core >= CORE_SCORE_FLOOR and cand_core < CORE_SCORE_FLOOR:
        return AcceptDecision(
            False,
            f"{CORE_SETUP} spadł poniżej {CORE_SCORE_FLOOR:.0f} pkt",
            "hygiene",
        )

    base_in_band = setup_shares_in_range(base_shares, *TARGET_BAND_PCT)
    cand_in_band = setup_shares_in_range(cand_shares, *TARGET_BAND_PCT)

    if not base_in_band:
        dmin = float(cand.get("min_balance", 0.0)) - float(base.get("min_balance", 0.0))
        dscore = float(cand.get("score_4p", 0.0)) - float(base.get("score_4p", 0.0))
        if dscore < -1e-9:
            return AcceptDecision(
                False,
                f"wspinaczka: Δscore_4p {dscore:+.2f} ujemny — odrzucam regresję",
                "climb",
            )
        if dmin >= min_delta:
            return AcceptDecision(True, f"wspinaczka maximin Δmin {dmin:+.2f}", "climb")
        return AcceptDecision(
            False,
            f"wspinaczka maximin Δmin {dmin:+.2f} < {min_delta}",
            "climb",
        )

    if not cand_in_band:
        return AcceptDecision(False, "higiena: wyszedł z pasma 20–30%", "hygiene")
    if health_improved(cand, base):
        return AcceptDecision(True, "higiena: poprawa zdrowia, pasmo utrzymane", "hygiene")
    return AcceptDecision(
        False,
        "higiena: brak poprawy zdrowia (kosmetyka score odrzucona)",
        "hygiene",
    )
