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


def rank_key(res: dict, *, mode: str = "band", base_in_band: bool = False) -> tuple:
    """Sort key (lower is better) for the 4P funnel.

    Ranks by pure win-share balance descending,
    then min_balance descending, then vitality penalty ascending.
    Vitality is a veto gate, not part of the ranking number.
    """
    score_4p = _score(res)
    min_b = float(res.get("min_balance") or score_4p)
    vit = float(res.get("vitality_penalty") or 0.0)
    return (-score_4p, -min_b, vit)



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
        d = _score(cand) - _score(base)
        dmin = float(cand.get("min_balance", 0.0)) - float(base.get("min_balance", 0.0))
        # Akceptujemy zysk w globalnym score LUB istotną poprawę najsłabszego setupu (Maximin) bez zapaści średniej
        if d >= min_delta:
            return AcceptDecision(True, f"legacy Δscore {d:+.2f} ≥ {min_delta}", "legacy")
        if dmin >= 0.5 and d >= -0.1:
            return AcceptDecision(True, f"legacy Maximin Δmin {dmin:+.2f} (Δscore {d:+.2f})", "legacy")
        return AcceptDecision(False, f"legacy Δscore {d:+.2f} i Δmin {dmin:+.2f} < {min_delta}", "legacy")

    if mode != "band":
        raise ValueError(f"Unknown accept mode: {mode!r}")

    base_shares = base.get("setup_shares") or {}
    cand_shares = cand.get("setup_shares") or {}
    climbing = not setup_shares_in_range(base_shares, *TARGET_BAND_PCT)

    if not table_has_share_foundation(base):
        # Base is outside 15–35% red line. Accept any candidate that doesn't
        # regress — when deep in the red zone, every small step counts.
        safe_f, msg_f = telemetry_is_safe(cand, relax_era=True)
        if not safe_f:
            return AcceptDecision(False, f"fundament: {msg_f}", "foundation")
        if cand.get("vitality_penalty", 0.0) > base.get("vitality_penalty", 0.0) + 1e-9:
            return AcceptDecision(False, "fundament: witalność gorsza niż baza", "foundation")
        if table_has_share_foundation(cand):
            return AcceptDecision(True, "fundament: kandydat wciąga frakcje w 15–35%", "foundation")
        dmin = float(cand.get("min_balance", 0.0)) - float(base.get("min_balance", 0.0))
        dscore = _score(cand) - _score(base)
        if dscore < -1e-9 and dmin < -1e-9:
            return AcceptDecision(
                False,
                f"fundament: Δscore {dscore:+.2f} i Δmin {dmin:+.2f} oba ujemne",
                "foundation",
            )
        return AcceptDecision(True, f"fundament: wspinaczka Δmin {dmin:+.2f} Δscore {dscore:+.2f}", "foundation")

    safe, msg = telemetry_is_safe(cand, relax_era=climbing)
    if not safe:
        return AcceptDecision(False, msg, "climb" if climbing else "hygiene")

    if cand.get("vitality_penalty", 0.0) > base.get("vitality_penalty", 0.0) + 1e-9:
        return AcceptDecision(False, "witalność gorsza niż baza", "climb")

    if not setup_shares_in_range(cand_shares, *RED_LINE_PCT):
        return AcceptDecision(False, "frakcja poza czerwoną linią 15–35%", "climb")

    base_scores = base.get("setup_scores_balance") or base.get("setup_scores") or {}
    cand_scores = cand.get("setup_scores_balance") or cand.get("setup_scores") or {}
    raw_base_core = base.get("core") if base.get("core") is not None else base_scores.get(CORE_SETUP, 0.0)
    raw_cand_core = cand.get("core") if cand.get("core") is not None else cand_scores.get(CORE_SETUP, 0.0)
    base_core = float(raw_base_core or 0.0)
    cand_core = float(raw_cand_core or 0.0)

    if base_core >= CORE_SCORE_FLOOR and cand_core < CORE_SCORE_FLOOR:
        return AcceptDecision(
            False,
            f"{CORE_SETUP} spadł poniżej {CORE_SCORE_FLOOR:.0f} pkt",
            "hygiene",
        )


    dscore = _score(cand) - _score(base)
    dmin = float(cand.get("min_balance", 0.0)) - float(base.get("min_balance", 0.0))

    base_in_band = setup_shares_in_range(base_shares, *TARGET_BAND_PCT)
    cand_in_band = setup_shares_in_range(cand_shares, *TARGET_BAND_PCT)

    if not base_in_band:
        # Wspinaczka: stół poza pasmem 20-30%
        if dscore >= min_delta or (dmin >= min_delta and dscore >= 0.0):
            return AcceptDecision(True, f"wspinaczka: Δscore {dscore:+.2f} Δmin {dmin:+.2f}", "climb")
        return AcceptDecision(
            False,
            f"wspinaczka: Δscore {dscore:+.2f} Δmin {dmin:+.2f} < {min_delta}",
            "climb",
        )

    # Baza jest w paśmie 20-30% (Higiena i dopracowanie optimum)
    if not cand_in_band and dscore < min_delta:
        return AcceptDecision(False, "higiena: wyszedł z pasma 20–30%", "hygiene")
    if health_improved(cand, base):
        return AcceptDecision(True, "higiena: poprawa zdrowia, pasmo utrzymane", "hygiene")
    if dscore >= min_delta or dmin >= min_delta:
        return AcceptDecision(True, f"higiena: Δscore {dscore:+.2f} Δmin {dmin:+.2f} w paśmie", "hygiene")
    return AcceptDecision(
        False,
        f"higiena: Δscore {dscore:+.2f} Δmin {dmin:+.2f} < {min_delta} i brak poprawy zdrowia",
        "hygiene",
    )


