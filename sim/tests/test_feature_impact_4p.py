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
    format_canon_debt,
    vitality_dead_path_mechanics,
)


def test_impact_skips_plusminus1_and_identity():
    ids = {t[0] for t in build_all_mechanic_tasks(1, 1, CANONICAL_4P_SETUPS)}
    for nid in (
        "L1_THRESHOLD_MINUS1",
        "L1_THRESHOLD_PLUS1",
        "L1_AGENTS_2",
        "L1_AGENTS_4",
        "L1_AUTODAFE_CD_2",
        "L1_AUTODAFE_CD_4",
        "L1_START_GOLD_6",
        "L1_MAX_ERAS_8",
        "L1_MAX_ERAS_16",
        "L2_SO_CONDEMNS_REQ_MINUS1",
        "L2_SO_STACKS_REQ_MINUS1",
        "L2_CAA_RELICS_REQ_MINUS1",
        "L2_KB_DECREES_REQ_PLUS1",
        "L2_KB_DECREES_REQ_MINUS1",
        "L2_KT_FRAGS_REQ_PLUS1",
        "L2_KT_FRAGS_REQ_MINUS1",
        "L2_KT_ERA_EARLY",
        "L2_GC_FALLS_PLUS1",
        "L2_GC_FALLS_MINUS1",
        "L2_GC_FALLS_DEFAULT_PLUS1",
        "L2_GC_FALLS_DEFAULT_MINUS1",
        "L2_GC_FALLS_NO_SO_PLUS1",
        "L2_GC_FALLS_NO_SO_MINUS1",
        "L4_TIME_DECK_EVERY_2ERAS",
        "L4_SEA_ROUTE_ERA4",
        "L2_CAA_ERA_EARLY",
        "L2_KB_ERA_EARLY",
        "L2_KB_HOOKS_REQ_0",
        "L4_INQUISITOR_SPEED2",
    ):
        assert nid not in ids, nid


def test_impact_uses_extreme_or_off():
    ids = {t[0] for t in build_all_mechanic_tasks(1, 1, CANONICAL_4P_SETUPS)}
    for eid in (
        "L1_START_GOLD_0",
        "L1_AUTODAFE_DISABLED",
        "L1_AUTODAFE_CD_0",
        "L4_NO_TIME_DECK",
        "L4_INQUISITOR_SPEED0",
        "L4_SEA_ROUTE_OFF",
        "L2_SO_CONDEMNS_LO",
        "L2_SO_CONDEMNS_HI",
        "L2_CAA_RELICS_HI",
        "L2_KB_HOOKS_HI",
    ):
        assert eid in ids, eid
    assert "L2_CAA_RELICS_LO" not in ids  # 2→1 is ±1, L2 audit
    offs = {t[0]: t[3] for t in build_all_mechanic_tasks(1, 1, CANONICAL_4P_SETUPS)}
    assert abs(offs["L2_SO_CONDEMNS_LO"]["so_condemns_offset"]) >= 2
    assert abs(offs["L2_SO_CONDEMNS_HI"]["so_condemns_offset"]) >= 2


def test_dormant_condemns_are_listed_as_dead_from_vitality():
    rows = vitality_dead_path_mechanics({
        "score_4p": 86.6,
        "vitality_penalty": 1.2,
        "eras_avg": 5.96,
        "deadlock_pct": 1.1,
        "poverty_pct": 5.5,
        "vitality_warnings": [
            "4p-core: Martwa ścieżka skazania (swiete-oficjum): 19/1264 wygranych (<8%) — gra tylko stosy",
        ],
    })
    assert len(rows) == 1
    assert rows[0]["group_id"] == "DEAD"
    assert "skazania" in rows[0]["name"]
    assert "próg 3" not in rows[0]["name"]
    assert rows[0]["id"].startswith("VITALITY_")


def test_canon_debt_is_data_only():
    text = "\n".join(format_canon_debt(
        {
            "score_4p": 86.6,
            "vitality_penalty": 1.2,
            "faction_shares": {"CAA": 21.3, "GC": 25.4, "KB": 26.5, "KT": 25.8, "SO": 25.9},
        },
        [{"id": "caa-09", "name": "Kurier", "group_id": "SELF_HARM", "d_4p": 6.5}],
        [{"d_4p": 0.0}] * 8,
        [
            {"id": "VITALITY_x", "name": "skazania uśpione", "group_id": "DEAD"},
            {"id": "L4_NO_TIME_DECK", "name": "Kronika off", "group_id": "STABILIZER", "d_4p": -42.4},
        ],
    ))
    assert "skazania uśpione" in text
    assert "CAA 21.3%" in text
    assert "caa-09" in text
    assert "path_era" not in text
    assert "Nie spuszczać" not in text
    assert "win.py" not in text
    assert "ożywić przy 3" not in text
    assert "L4_NO_TIME_DECK" in text


def test_canon_debt_empty_when_no_flags():
    assert format_canon_debt({"faction_shares": {"A": 25.0}}, [], [], []) == []


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
