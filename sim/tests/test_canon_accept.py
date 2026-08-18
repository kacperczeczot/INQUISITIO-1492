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
    gain = _snap(score_4p=90.2)
    loss = _snap(score_4p=89.9)
    assert accept_candidate(base, gain, mode="legacy").accepted
    assert not accept_candidate(base, loss, mode="legacy").accepted


def test_legacy_telemetry_veto_beats_score_gain():
    base = _snap(score_4p=90.0)
    cand = _snap(score_4p=95.0, deadlock=8.0)
    d = accept_candidate(base, cand, mode="legacy")
    assert not d.accepted
    assert "Deadlock" in d.reason


def test_foundation_allows_climb_from_wrecked_shares():
    """Wrecked shares allow climbing candidates that improve min_balance/score."""
    wreck = _shares_ok()
    wreck["4p-core"] = {"SO": 55.0, "CAA": 15.0, "KB": 15.0, "KT": 15.0}
    wreck["4p-no-korona"] = {"SO": 70.0, "CAA": 10.0, "KT": 10.0, "GC": 10.0}
    base = _snap(
        score_4p=8.5,
        min_balance=2.7,
        core=5.7,
        weak=2.7,
        shares=wreck,
        eras=4.49,
        vitality=1.2,
    )
    even = _shares_ok()
    cand = _snap(
        score_4p=16.9,
        min_balance=16.9,
        core=18.0,
        weak=16.9,
        shares=even,
        eras=5.5,
        vitality=1.2,
    )
    assert not table_has_share_foundation(base)
    d = accept_candidate(base, cand, mode="band", min_delta=0.05)
    assert d.accepted
    assert d.phase == "foundation"


def test_in_band_still_vetoes_short_games():
    base = _snap()
    cand = _snap(score_4p=95.0, min_balance=90.0, weak=90.0, eras=3.98)
    d = accept_candidate(base, cand, mode="band")
    assert not d.accepted
    assert "Er" in d.reason


def test_climb_still_runs_inside_red_line_outside_target_band():
    """16–34% is a ridge the auditor may climb; 10% / 55% is not."""
    shares = _shares_ok()
    shares["4p-no-oficjum"]["KB"] = 34.0
    shares["4p-no-oficjum"]["GC"] = 16.0
    base = _snap(min_balance=83.0, shares=shares, score_4p=91.0)
    still_out = dict(shares)
    still_out["4p-no-oficjum"] = {"CAA": 25.0, "KB": 36.0, "KT": 25.0, "GC": 14.0}
    cand = _snap(min_balance=85.0, weak=85.0, shares=still_out, score_4p=90.5)
    d = accept_candidate(base, cand, mode="band", min_delta=0.05)
    assert not d.accepted
    assert "czerwoną" in d.reason


def test_band_climb_uses_min_not_mean():
    shares = _shares_ok()
    shares["4p-no-oficjum"]["KB"] = 34.0
    shares["4p-no-oficjum"]["GC"] = 16.0
    base = _snap(min_balance=83.0, shares=shares, score_4p=91.0)
    # Mean up, weakest down — reject
    worse_min = _snap(min_balance=80.0, weak=80.0, shares=shares, score_4p=93.0)
    assert not accept_candidate(base, worse_min, mode="band").accepted
    better_min = _snap(min_balance=85.0, weak=85.0, shares=shares, score_4p=91.2)
    d = accept_candidate(base, better_min, mode="band")
    assert d.accepted
    assert d.phase == "climb"


def test_band_hygiene_accepts_health_fix_with_lower_score():
    base = _snap(score_4p=91.5, min_balance=88.0, weak=88.0, acc=5.2)
    cand = _snap(score_4p=89.0, min_balance=86.0, weak=86.0, acc=4.0, core=93.0)
    d = accept_candidate(base, cand, mode="band")
    assert d.accepted
    assert d.phase == "hygiene"


def test_band_hygiene_accepts_score_gain_in_band():
    base = _snap(score_4p=91.5, min_balance=88.0, weak=88.0)
    cand = _snap(score_4p=91.8, min_balance=88.2, weak=88.2)
    d = accept_candidate(base, cand, mode="band")
    assert d.accepted
    assert d.phase == "hygiene"


def test_band_veto_core_below_90_and_red_line():
    base = _snap(core=96.0, min_balance=88.0, weak=88.0, acc=5.2)
    drop_core = _snap(core=89.0, min_balance=88.0, weak=88.0, acc=4.0)
    d = accept_candidate(base, drop_core, mode="band")
    assert not d.accepted

    bad_shares = _shares_ok()
    bad_shares["4p-no-oficjum"]["GC"] = 36.0
    bad_shares["4p-no-oficjum"]["KB"] = 14.0
    red = _snap(shares=bad_shares, acc=4.0)
    d2 = accept_candidate(base, red, mode="band")
    assert not d2.accepted
    assert "czerwoną" in d2.reason


def test_no_cienie_88_with_shares_in_band_optimizes_score():
    """Score optimization from 88 to 92 continues pushing to optimum."""
    shares = _shares_ok()
    shares["4p-no-cienie"] = {"SO": 27.2, "KB": 22.1, "KT": 24.7, "GC": 26.0}
    assert setup_shares_in_range(shares, 20.0, 30.0)
    base = _snap(min_balance=88.1, weak=88.1, shares=shares)
    gain = _snap(score_4p=92.0, min_balance=88.4, weak=88.4, shares=shares)
    d = accept_candidate(base, gain, mode="band")
    assert d.accepted
    assert d.phase == "hygiene"


def test_rank_key_band_climb_prefers_higher_min():
    low = {"min_balance": 80.0, "score_4p_balance": 92.0, "score_4p": 92.0}
    high = {"min_balance": 85.0, "score_4p_balance": 88.0, "score_4p": 88.0}
    assert rank_key(high, mode="band", base_in_band=False) < rank_key(
        low, mode="band", base_in_band=False
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
    assert rank_key(healthy, mode="band", base_in_band=True) < rank_key(
        wreck, mode="band", base_in_band=True
    )
    assert not accept_candidate(healthy, wreck, mode="band").accepted


def test_healthy_v086_table_rejects_insufficient_gain():
    """Noise with delta < min_delta and no health improvement is rejected."""
    base = _snap(min_balance=91.5, core=95.8, weak=91.5, acc=3.64, deadlock=1.0, eras=5.93)
    cand = _snap(score_4p=base["score_4p"] + 0.01, min_balance=91.51, core=95.8, weak=91.51, acc=3.64, deadlock=0.98, eras=5.93)
    assert not canon_should_stop(base, mode="band")
    d = accept_candidate(base, cand, mode="band", min_delta=0.05)
    assert not d.accepted
    assert "brak poprawy zdrowia" in d.reason or "min_delta" in d.reason


def test_dead_win_path_keeps_hygiene_open():
    """Equal 20–30% shares must not halt while a victory clause is unused."""
    base = _snap(min_balance=91.5, core=95.8, weak=91.5, vitality=1.2)
    cand = _snap(score_4p=90.0, min_balance=90.5, core=94.0, weak=90.5, vitality=0.0)
    assert not canon_should_stop(base, mode="band")
    d = accept_candidate(base, cand, mode="band")
    assert d.accepted
    assert d.phase == "hygiene"


def test_hygiene_still_fixes_accusations_out_of_window():
    base = _snap(score_4p=91.5, min_balance=88.0, weak=88.0, acc=5.2)
    cand = _snap(score_4p=89.0, min_balance=86.0, weak=86.0, acc=4.0, core=93.0)
    assert not canon_should_stop(base, mode="band")
    d = accept_candidate(base, cand, mode="band")
    assert d.accepted
    assert d.phase == "hygiene"
