"""v0.99.4 — YAML knobs and card fields must reach the engine (gwarancja silnika)."""
from __future__ import annotations

import random

from inquisitio.cards.loader import load_all_cards
from inquisitio.engine.effects.registry import resolve_card_effects
from inquisitio.engine.inquisitor import era_start_inquisitor, move_inquisitor
from inquisitio.engine.setup import new_game
from inquisitio.engine.state import FactionId
from inquisitio.engine.turn import _maybe_open_sea_route
from inquisitio.engine.verdict import run_verdict


def test_kt11_heresy_decrease_from_yaml():
    st = new_game(setup="4p-no-cienie", seed=3, layer="C")
    kt = st.players[FactionId.KABALA_TOLEDO]
    kt.heresy = 4
    kt.gold = 5
    card = load_all_cards()["kt-11"]
    resolve_card_effects(st, FactionId.KABALA_TOLEDO, card, random.Random(1))
    assert kt.heresy == 3


def test_caa03_drags_relic_toward_harbor():
    st = new_game(setup="4p-core", seed=5, layer="C")
    caa = st.players[FactionId.CIENIE_AL_ANDALUS]
    caa.gold = 3
    loc = caa.agents[0].location
    st.relics_on_board[loc] = 1
    before = dict(st.relics_on_board)
    card = load_all_cards()["caa-03"]
    resolve_card_effects(st, FactionId.CIENIE_AL_ANDALUS, card, random.Random(2))
    assert sum(st.relics_on_board.values()) == sum(before.values())
    assert st.relics_on_board.get(loc, 0) <= before.get(loc, 0)


def test_caa11_sends_inquisitor_after_agent_move():
    st = new_game(setup="4p-core", seed=7, layer="C")
    caa = st.players[FactionId.CIENIE_AL_ANDALUS]
    caa.gold = 5
    before = st.inquisitor_location
    card = load_all_cards()["caa-11"]
    resolve_card_effects(st, FactionId.CIENIE_AL_ANDALUS, card, random.Random(3))
    assert caa.inquisitor_send_count == 1
    assert st.inquisitor_location != before or before in ("rynek", "gildia", "lochy", "palac", "trybunal")


def test_inquisitor_speed_two_steps_on_patrol():
    st = new_game(setup="4p-core", seed=11, layer="C", sys_overrides={"inquisitor_speed": 2})
    st.inquisitor_location = "trybunal"
    move_inquisitor(st, random.Random(4), toward="gildia")
    assert st.inquisitor_location != "trybunal"


def test_sea_route_scheduled_without_time_deck():
    st = new_game(setup="4p-core", seed=1, layer="C", sys_overrides={"no_time_deck": True})
    st.era = 4
    _maybe_open_sea_route(st)
    assert st.sea_route_open


def test_caa10_fiasco_when_inquisitor_present():
    st = new_game(setup="4p-core", seed=19, layer="C")
    caa = st.players[FactionId.CIENIE_AL_ANDALUS]
    caa.gold = 5
    loc = caa.agents[0].location
    st.inquisitor_location = loc
    st.relics_on_board[loc] = 2
    before = caa.relics_evacuated
    card = load_all_cards()["caa-10"]
    from inquisitio.engine.effects.registry import _signature

    _signature(st, FactionId.CIENIE_AL_ANDALUS, card, random.Random(6))
    assert caa.relics_evacuated == before
    assert any("fiasko" in msg for msg in st.log)


def test_kb10_fiasco_without_two_hooks():
    st = new_game(setup="4p-core", seed=17, layer="C")
    kb = st.players[FactionId.KORONA_BORGIOWIE]
    kb.gold = 10
    kb.hooks_on.clear()
    card = load_all_cards()["kb-10"]
    before_decrees = kb.decrees_played
    from inquisitio.engine.effects.registry import _signature

    _signature(st, FactionId.KORONA_BORGIOWIE, card, random.Random(5))
    assert kb.decrees_played == before_decrees
    assert any("fiasko" in msg for msg in st.log)
