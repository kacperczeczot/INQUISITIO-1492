"""4P canon accept-mode: legacy vs band (climb / hygiene)."""
from __future__ import annotations

from inquisitio.runner.canon_accept import (
    accept_candidate,
    canon_should_stop,
    rank_key,
    setup_shares_in_range,
    table_has_share_foundation,
)


def _shares_ok() -> dict[str, dict[str, float]]:
    even = {"SO": 25.0, "CAA": 25.0, "KB": 25.0, "KT": 25.0}
    return {
        "4p-core": dict(even),
        "4p-no-cienie": {"SO": 25.0, "KB": 25.0, "KT": 25.0, "GC": 25.0},
        "4p-no-kabala": {"SO": 25.0, "CAA": 25.0, "KB": 25.0, "GC": 25.0},
        "4p-no-korona": {"SO": 25.0, "CAA": 25.0, "KT": 25.0, "GC": 25.0},
        "4p-no-oficjum": {"CAA": 25.0, "KB": 25.0, "KT": 25.0, "GC": 25.0},
    }


def _scores(core: float = 96.0, weak: float = 88.0) -> dict[str, float]:
    return {
        "4p-core": core,
        "4p-no-cienie": weak,
        "4p-no-kabala": 95.0,
        "4p-no-korona": 95.0,
        "4p-no-oficjum": weak,
    }


def _snap(
    *,
    score_4p: float = 90.0,
    min_balance: float = 83.0,
    core: float = 96.0,
    weak: float = 83.0,
    shares: dict | None = None,
    vitality: float = 0.0,
    deadlock: float = 1.0,
    poverty: float = 6.0,
    eras: float = 5.9,
    acc: float = 3.0,
) -> dict:
    scores = _scores(core, weak)
    return {
        "score_4p": score_4p,
        "score_4p_balance": sum(scores.values()) / len(scores),
        "min_balance": min_balance,
        "setup_scores_balance": scores,
        "setup_shares": shares if shares is not None else _shares_ok(),
        "vitality_penalty": vitality,
        "deadlock_pct": deadlock,
        "poverty_pct": poverty,
        "eras_avg": eras,
        "acc_avg": acc,
    }


def test_legacy_accepts_mean_gain_rejects_small_loss():
    base = _snap(score_4p=90.0)
    gain = _snap(score_4p=90.2, core=97.0, weak=84.0)  # balance ≈ 91.0 vs base 90.4
    loss = _snap(score_4p=89.9, core=95.0, weak=82.0)  # balance ≈ 89.8 vs base 90.4
    assert accept_candidate(base, gain).accepted
    assert not accept_candidate(base, loss).accepted


def test_legacy_telemetry_veto_beats_score_gain():
    base = _snap(score_4p=90.0)
    cand = _snap(score_4p=95.0, deadlock=8.0)
    d = accept_candidate(base, cand)
    assert not d.accepted
    assert "Deadlock" in d.reason



def test_in_band_still_vetoes_short_games():
    base = _snap()
    cand = _snap(score_4p=95.0, min_balance=90.0, weak=90.0, eras=3.98)
    d = accept_candidate(base, cand)
    assert not d.accepted
    assert "Er" in d.reason








def test_rank_key_prefers_higher_score():
    low = {"min_balance": 85.0, "score_4p_balance": 88.0, "score_4p": 88.0}
    high = {"min_balance": 80.0, "score_4p_balance": 92.0, "score_4p": 92.0}
    assert rank_key(high) < rank_key(
        low
    )


def test_hygiene_rank_does_not_promote_wrecked_table():
    """v0.86 leak: band funnel ranked L3_KB-10_GOLD_PLUS1 (~41 pkt) first."""
    healthy = _snap(min_balance=91.5, core=95.8, weak=91.5, acc=3.64, deadlock=1.0)
    wreck_shares = _shares_ok()
    wreck_shares["4p-core"] = {"SO": 10.0, "CAA": 40.0, "KB": 40.0, "KT": 10.0}
    wreck = _snap(
        score_4p=41.0,
        min_balance=41.0,
        core=41.0,
        weak=41.0,
        shares=wreck_shares,
        acc=2.5,
        deadlock=0.2,
    )
    assert rank_key(healthy) < rank_key(
        wreck
    )
    assert not accept_candidate(healthy, wreck).accepted




