"""Smoke tests — layers A/B/C, setups 3–5p."""
from __future__ import annotations

import random
from pathlib import Path

import pytest

from inquisitio.agents.politics import PoliticsAgent
from inquisitio.cards.loader import cards_for_faction, load_all_cards, time_cards
from inquisitio.engine.dungeon import arrest_agent, interrogate
from inquisitio.engine.heresy import add_heresy, is_critical
from inquisitio.engine.hooks import force_hook, grant_hook
from inquisitio.engine.inquisitor import can_autodafe, resolve_autodafe
from inquisitio.engine.setup import SETUP_PRESETS, new_game
from inquisitio.engine.state import FactionId
from inquisitio.engine.turn import play_game
from inquisitio.engine.verdict import run_verdict


def test_no_2p_setup():
    assert all(len(v) >= 3 for v in SETUP_PRESETS.values())
    with pytest.raises(ValueError):
        new_game(factions=[FactionId.SWIETE_OFICJUM, FactionId.CIENIE_AL_ANDALUS])


def test_layer_a_cards_simple():
    for fac in [
        "swiete-oficjum",
        "cienie-al-andalus",
        "korona-borgiowie",
        "kabala-toledo",
        "gildia-cieni",
    ]:
        a = cards_for_faction(fac, max_layer="A")
        assert len(a) == 5
        for c in a:
            assert c.layer == "A"
            assert c.type != "signature"
            assert not c.breaks_rule
            assert not c.creates_hook


def test_layer_c_full_decks():
    for fac in [
        "swiete-oficjum",
        "cienie-al-andalus",
        "korona-borgiowie",
        "kabala-toledo",
        "gildia-cieni",
    ]:
        assert len(cards_for_faction(fac, max_layer="C")) == 10
    assert len(time_cards("C")) >= 8


def test_heresy_and_verdict_layer_a():
    rng = random.Random(1)
    state = new_game(setup="3p-oficjum-alandalus-korona", seed=1, layer="A")
    accused = FactionId.CIENIE_AL_ANDALUS
    add_heresy(state, accused, 8)
    assert is_critical(state.players[accused], state.accusation_threshold)
    state.eras_since_autodafe = 5
    assert can_autodafe(state)
    resolve_autodafe(state)
    run_verdict(state, FactionId.SWIETE_OFICJUM, accused, rng)
    assert state.metrics.accusations >= 1


def test_dungeon_and_hooks_layer_b():
    rng = random.Random(2)
    state = new_game(setup="3p-oficjum-alandalus-korona", seed=2, layer="B")
    victim = FactionId.CIENIE_AL_ANDALUS
    assert arrest_agent(state, victim)
    out = interrogate(state, FactionId.SWIETE_OFICJUM, victim, rng, prefer="double")
    assert out == "double"
    assert state.metrics.doubles_created >= 1
    grant_hook(state, FactionId.KORONA_BORGIOWIE, victim)
    assert force_hook(state, FactionId.KORONA_BORGIOWIE, victim, comply=False)
    assert state.metrics.hooks_forced >= 1
    assert state.players[victim].heresy >= 2


def test_smoke_full_game_layer_c():
    rng = random.Random(42)
    state = new_game(setup="3p-oficjum-alandalus-korona", seed=42, layer="C")
    agent = PoliticsAgent(rng)

    def choose(st, fid, legal):
        return agent.choose_card(st, fid, legal)

    winner = play_game(state, rng, choose)
    assert winner in state.turn_order
    assert state.metrics.eras >= 1
    proc = Path(__file__).resolve().parents[1] / "inquisitio" / "engine" / "process.py"
    assert not proc.exists()


def test_cards_load():
    cards = load_all_cards()
    assert "so-01" in cards
    assert "time-01" in cards
    assert cards["so-10"].breaks_rule
