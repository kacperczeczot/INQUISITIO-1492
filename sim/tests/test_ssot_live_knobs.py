"""YAML knobs that used to be dead must reach the engine and the macro pool."""
from __future__ import annotations

from inquisitio.config import CONFIG
from inquisitio.config_updater import apply_mutation_to_config
from inquisitio.engine.inquisitor import resolve_autodafe
from inquisitio.engine.setup import new_game
from inquisitio.engine.state import FactionId, heresy_zone
from inquisitio.engine.win import check_winner_details


def test_yaml_exposes_observed_and_income_and_no_split_zones():
    assert CONFIG.observed_threshold() == 5
    assert CONFIG.era_income() == 1
    assert CONFIG.intrigue_gold() == 1
    assert int(CONFIG.system.cards_per_era) == 2
    assert "heresy_zones" not in CONFIG.raw()


def test_observed_override_changes_autodafe_burn():
    st = new_game(setup="4p-core", seed=1, layer="C", sys_overrides={"observed_threshold": 5})
    assert st.observed_threshold == 5
    so = st.players[FactionId.SWIETE_OFICJUM]
    caa = st.players[FactionId.CIENIE_AL_ANDALUS]
    loc = st.inquisitor_location
    caa.heresy = 3
    caa.agents[0].location = loc
    caa.agents[0].arrested = False
    so.agents[0].location = "palac"
    st.eras_since_autodafe = 5
    resolve_autodafe(st, force=True)
    burned = any("burned" in line for line in st.log)
    arrested_clean = any("Czysta" in line for line in st.log)
    assert arrested_clean
    assert not burned


def test_apply_mutation_writes_observed_and_cards_per_era():
    raw = {
        "system": {"observed_threshold": 4, "cards_per_era": 2, "era_income": 1, "intrigue_gold": 1},
        "victory": {},
        "variants": {"sea_route_era": 4},
        "cards": {},
    }
    cfg, _ = apply_mutation_to_config(raw, "L1_OBSERVED_PLUS1", {"observed_threshold_offset": 1})
    assert cfg["system"]["observed_threshold"] == 5
    cfg, _ = apply_mutation_to_config(raw, "L1_CARDS_PER_ERA_MINUS1", {"cards_per_era_offset": -1})
    assert cfg["system"]["cards_per_era"] == 1
    cfg, _ = apply_mutation_to_config(raw, "L1_INTRIGUE_GOLD_PLUS1", {"intrigue_gold_offset": 1})
    assert cfg["system"]["intrigue_gold"] == 2
    cfg, _ = apply_mutation_to_config(raw, "L4_SEA_ROUTE_ERA_PLUS1", {"sea_route_era_offset": 1})
    assert cfg["variants"]["sea_route_era"] == 5


def test_path_era_offset_blocks_early_caa():
    st = new_game(setup="3p-cienie-korona-kabala", seed=1, layer="C")
    caa = st.players[FactionId.CIENIE_AL_ANDALUS]
    caa.relics_evacuated = 2
    caa.path_via_double = True
    st.era = 4
    assert check_winner_details(st) == (FactionId.CIENIE_AL_ANDALUS, "caa_sea_route")
    assert check_winner_details(st, {"caa_era_offset": 1}) is None or (
        check_winner_details(st, {"caa_era_offset": 1})[0] != FactionId.CIENIE_AL_ANDALUS
    )
    st.era = 5
    assert check_winner_details(st, {"caa_era_offset": 1}) == (FactionId.CIENIE_AL_ANDALUS, "caa_sea_route")


def test_heresy_zone_observed_min_moves():
    assert heresy_zone(4, critical_min=7, observed_min=5) == "czysta"
    assert heresy_zone(5, critical_min=7, observed_min=5) == "obserwowana"
