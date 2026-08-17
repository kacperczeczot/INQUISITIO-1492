"""4P impact audit: headline score is win share; identity knobs are not ablated."""
import sys
from pathlib import Path

TOOLS_SIM = Path(__file__).resolve().parents[2] / "tools" / "sim"
if str(TOOLS_SIM) not in sys.path:
    sys.path.insert(0, str(TOOLS_SIM))

from feature_impact_4p import (  # noqa: E402
    CANONICAL_4P_SETUPS,
    REPORT_GAMES_MIN,
    assert_report_sample_size,
    build_all_mechanic_tasks,
)


def test_removed_or_identity_knobs_are_not_ablated():
    ids = {t[0] for t in build_all_mechanic_tasks(1, 1, CANONICAL_4P_SETUPS)}
    assert "L2_CAA_ERA_EARLY" not in ids
    assert "L2_CAA_ERA_LATE" not in ids
    assert "L2_KB_ERA_EARLY" not in ids
    assert "L2_KB_ERA_LATE" not in ids
    assert "L2_KB_HOOKS_REQ_0" not in ids
    assert "L4_SEA_ROUTE_ERA4" not in ids
    assert "L2_KT_HERESY_BAND_WIDE" not in ids
    assert "L2_KT_HERESY_LOW_UP" not in ids
    assert "L4_SEA_ROUTE_ERA6" not in ids
    assert "L4_INQUISITOR_SPEED2" not in ids
    assert "L1_MAX_ERAS_16" not in ids
    assert "L2_SO_CONDEMNS_REQ_PLUS2" not in ids
    assert "L4_INQUISITOR_SPEED0" in ids
    assert "L1_MAX_ERAS_8" in ids
    assert "L2_SO_CONDEMNS_REQ_MINUS1" in ids
    assert "L2_KB_HOOKS_REQ_PLUS2" in ids


def test_archive_report_rejects_screen_sized_samples():
    assert REPORT_GAMES_MIN == 5000
    assert_report_sample_size(5000, screen=False)
    assert_report_sample_size(400, screen=True)
    try:
        assert_report_sample_size(400, screen=False)
    except SystemExit as exc:
        assert "5000" in str(exc)
    else:
        raise AssertionError("400 gier nie może iść do archiwum")
