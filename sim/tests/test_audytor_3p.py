"""Audytor 3P/5P: lookahead +1D shared with 4P; vitality crutch veto; frozen identity."""
from __future__ import annotations

import sys
from pathlib import Path

TOOLS_SIM = Path(__file__).resolve().parents[2] / "tools" / "sim"
if str(TOOLS_SIM) not in sys.path:
    sys.path.insert(0, str(TOOLS_SIM))

from audytor_3p import generate_all_atomic_candidates_3p  # noqa: E402
from audytor_4p import (  # noqa: E402
    accept_format_exception,
    drop_dead_path_crutches,
    is_dead_path_crutch,
    lookahead_next_action,
)
from audytor_5p import generate_all_atomic_candidates_5p  # noqa: E402


def _dead_skazania_base(score_key: str = "score_3p") -> dict:
    return {
        score_key: 40.0,
        "vitality_penalty": 1.2,
        "vitality_warnings": [
            "3p-so-caa-kb: Martwa ścieżka skazania (swiete-oficjum): 19/400 wygranych (<8%) — gra tylko stosy",
        ],
        "deadlock_pct": 1.1,
        "poverty_pct": 5.5,
        "eras_avg": 5.5,
        "params": {},
    }


def test_format_pool_skips_frozen_identity():
    for gen in (generate_all_atomic_candidates_3p, generate_all_atomic_candidates_5p):
        ids = [c[0] for c in gen()]
        assert ids
        assert all("HAND_LIMIT" not in tid for tid in ids)
        assert all("AUTODAFE" not in tid for tid in ids)
        assert all("AGENTS" not in tid for tid in ids)
        assert all("VERDICT_SECRET" not in tid for tid in ids)
        assert all("KB_HOOKS" not in tid for tid in ids)
        for _tid, _name, params in gen():
            assert "kb_hooks_offset" not in params
            assert "kb_era_offset" not in params
            assert "verdict_secret" not in params
            assert "no_time_deck" not in params
            assert "time_deck_freq" not in params
            assert int(params.get("sea_route_era") or 0) < 90
            assert params.get("inquisitor_speed") != 0
        assert all("TIME_DECK" not in tid for tid in ids)
        assert all("SEA_ROUTE_OFF" not in tid for tid in ids)
        assert all("INQUISITOR_SPEED0" not in tid for tid in ids)


def test_format_exception_rejects_dead_condemns_crutch():
    base = _dead_skazania_base()
    cand = {
        **base,
        "id": "L2_SO_CONDEMNS_MINUS1",
        "params": {"so_condemns_offset": -1},
        "score_3p": 55.0,
        "deadlock_pct": 1.0,
        "poverty_pct": 5.0,
        "eras_avg": 5.5,
    }
    d = accept_format_exception(
        base,
        cand,
        score_key="score_3p",
        min_delta=0.05,
        telemetry_ok=(True, "OK"),
    )
    assert not d.accepted
    assert "proteza" in d.reason
    assert is_dead_path_crutch(base, cand["params"])


def test_format_exception_accepts_safe_delta():
    base = _dead_skazania_base()
    base["vitality_warnings"] = []
    base["vitality_penalty"] = 0.0
    cand = {
        **base,
        "id": "L1_THRESHOLD_PLUS1",
        "params": {"threshold_offset": 1},
        "score_3p": 50.0,
        "deadlock_pct": 1.0,
        "poverty_pct": 5.0,
        "eras_avg": 5.5,
    }
    d = accept_format_exception(
        base,
        cand,
        score_key="score_3p",
        min_delta=0.05,
        telemetry_ok=(True, "OK"),
    )
    assert d.accepted


def test_format_drop_crutches_from_beam():
    base = _dead_skazania_base()
    pool = [
        ("L2_SO_CONDEMNS_MINUS1", "skazania −1", {"so_condemns_offset": -1}),
        ("L1_THRESHOLD_PLUS1", "próg +1", {"threshold_offset": 1}),
    ]
    kept = drop_dead_path_crutches(base, pool)
    assert [c[0] for c in kept] == ["L1_THRESHOLD_PLUS1"]


def test_lookahead_shared_with_4p():
    assert lookahead_next_action(depth=1, max_depth=4, has_pending=False, found_better=False) == "deeper_empty"
    assert lookahead_next_action(depth=1, max_depth=4, has_pending=False, found_better=True) == "hold_and_deeper"
    assert lookahead_next_action(depth=2, max_depth=4, has_pending=True, found_better=False) == "apply_pending"
