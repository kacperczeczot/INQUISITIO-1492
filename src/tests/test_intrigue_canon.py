"""Faza I/II canon: Gospodarcza, zakrycie, dobór do limitu, 1. gracz."""
from __future__ import annotations

import random

from inquisitio.engine.effects.registry import play_card, resolve_pending_plays
from inquisitio.engine.setup import new_game
from inquisitio.engine.state import FactionId
from inquisitio.engine.turn import play_era, take_economic_action


def test_economic_action_pays_intrigue_gold():
    st = new_game(setup="4p-core", seed=1, layer="C")
    fid = FactionId.SWIETE_OFICJUM
    before = st.players[fid].gold
    rng = random.Random(1)
    take_economic_action(st, fid, rng, move_agent=False)
    assert st.players[fid].gold == before + 1
    assert any("economic action +1" in line for line in st.log)


def test_jarmark_pays_two_on_rynek():
    st = new_game(setup="4p-core", seed=1, layer="C")
    fid = FactionId.KORONA_BORGIOWIE
    st.active_time_edict = "time-09"
    st.players[fid].agents[0].location = "rynek"
    st.players[fid].agents[0].arrested = False
    before = st.players[fid].gold
    take_economic_action(st, fid, random.Random(1), move_agent=False)
    assert st.players[fid].gold == before + 2


def test_jarmark_without_rynek_stays_plus_one():
    st = new_game(setup="4p-core", seed=1, layer="C")
    fid = FactionId.KORONA_BORGIOWIE
    st.active_time_edict = "time-09"
    for ag in st.players[fid].agents:
        ag.location = "trybunal"
        ag.arrested = False
    before = st.players[fid].gold
    take_economic_action(st, fid, random.Random(1), move_agent=False)
    assert st.players[fid].gold == before + 1


def test_broke_turn_still_takes_economic_not_empty_pass():
    st = new_game(setup="4p-core", seed=7, layer="C")
    gold0 = {fid: st.players[fid].gold for fid in st.turn_order}
    for pl in st.players.values():
        pl.gold = 0
    first = list(st.turn_order)
    play_era(st, random.Random(7), lambda _s, _f, _legal: None)
    for fid in first:
        # 2× Gospodarcza; +dochód Fazy III unless someone already won
        assert st.players[fid].gold >= 2
        if st.winner is None:
            assert st.players[fid].gold == 3
    assert all("pass (savings)" not in line for line in st.log)
    assert all("pass (no legal cards)" not in line for line in st.log)
    assert gold0  # sanity: setup had gold


def test_stage_does_not_apply_effect_until_reveal():
    st = new_game(setup="4p-core", seed=42, layer="C")
    caa = st.players[FactionId.CIENIE_AL_ANDALUS]
    caa.hand = ["caa-03"]
    caa.gold = 5
    h0 = caa.heresy
    rng = random.Random(42)
    assert play_card(st, FactionId.CIENIE_AL_ANDALUS, "caa-03", rng, resolve=False)
    assert caa.heresy == h0
    assert "caa-03" not in caa.hand
    assert "caa-03" not in caa.discard
    assert st.pending_plays
    resolve_pending_plays(st, rng)
    assert caa.heresy == h0 + 1
    assert "caa-03" in caa.discard


def test_draw_up_to_hand_limit():
    st = new_game(setup="4p-core", seed=3, layer="C")
    fid = st.turn_order[0]
    pl = st.players[fid]
    pl.hand = pl.hand[:3]
    play_era(st, random.Random(3), lambda _s, _f, _legal: None)
    assert len(st.players[fid].hand) == 5


def test_first_player_rotates_after_era():
    st = new_game(setup="4p-core", seed=3, layer="C")
    first = st.turn_order[0]
    play_era(st, random.Random(3), lambda _s, _f, _legal: None)
    if st.winner:
        return
    assert st.turn_order[0] != first
    assert st.turn_order[-1] == first


def test_autodafe_skips_oficjum_agents():
    from inquisitio.engine.inquisitor import resolve_autodafe

    st = new_game(setup="4p-core", seed=1, layer="C")
    loc = "trybunal"
    st.inquisitor_location = loc
    so = st.players[FactionId.SWIETE_OFICJUM]
    caa = st.players[FactionId.CIENIE_AL_ANDALUS]
    for ag in so.agents:
        ag.location = loc
        ag.arrested = False
    for ag in caa.agents:
        ag.location = "gildia"
        ag.arrested = False
    so.heresy = 8
    resolve_autodafe(st, force=True)
    assert all(not ag.arrested and ag.location == loc for ag in so.agents)


def test_autodafe_stack_per_burned_rival_agent():
    from inquisitio.engine.inquisitor import resolve_autodafe

    st = new_game(setup="4p-core", seed=1, layer="C")
    loc = "trybunal"
    st.inquisitor_location = loc
    so = st.players[FactionId.SWIETE_OFICJUM]
    caa = st.players[FactionId.CIENIE_AL_ANDALUS]
    kb = st.players[FactionId.KORONA_BORGIOWIE]
    so.stacks = 0
    for ag in so.agents:
        ag.location = "palac"
    caa.heresy = 8
    kb.heresy = 8
    caa.agents[0].location = loc
    caa.agents[0].arrested = False
    kb.agents[0].location = loc
    kb.agents[0].arrested = False
    resolve_autodafe(st, force=True)
    assert so.stacks == 2


def test_no_free_caa_evacuate():
    st = new_game(setup="4p-core", seed=3, layer="C")
    play_era(st, random.Random(3), lambda _s, _f, _legal: None)
    assert all("quiet harbor" not in line for line in st.log)
    assert all("sea evacuate" not in line for line in st.log)


def test_fiasco_without_dungeon_presence():
    st = new_game(setup="4p-core", seed=1, layer="C")
    so = st.players[FactionId.SWIETE_OFICJUM]
    for ag in so.agents:
        ag.location = "trybunal"
        ag.arrested = False
    so.hand = ["so-07"]
    so.gold = 5
    play_card(st, FactionId.SWIETE_OFICJUM, "so-07", random.Random(1))
    assert any("fiasko" in line for line in st.log)
    assert not so.used_interrogation


def test_hook_force_when_legal():
    from inquisitio.engine.hooks import grant_hook

    st = new_game(setup="4p-core", seed=3, layer="C")
    grant_hook(st, FactionId.KORONA_BORGIOWIE, FactionId.CIENIE_AL_ANDALUS)
    play_era(st, random.Random(3), lambda _s, _f, _legal: None)
    assert st.metrics.hooks_forced >= 1


def test_naslanie_oficjum_wins_conflict():
    from inquisitio.engine.table_ai import resolve_naslanie_winner

    st = new_game(setup="4p-core", seed=1, layer="C")
    decls = {
        FactionId.CIENIE_AL_ANDALUS: "gildia",
        FactionId.SWIETE_OFICJUM: "trybunal",
    }
    win = resolve_naslanie_winner(st, decls)
    assert win == (FactionId.SWIETE_OFICJUM, "trybunal")


def test_verdict_once_per_target_per_era():
    from inquisitio.engine.verdict import run_verdict

    st = new_game(setup="4p-core", seed=1, layer="C")
    caa = st.players[FactionId.CIENIE_AL_ANDALUS]
    caa.heresy = 10
    rng = random.Random(0)
    assert run_verdict(st, FactionId.SWIETE_OFICJUM, FactionId.CIENIE_AL_ANDALUS, rng)
    assert run_verdict(st, FactionId.KORONA_BORGIOWIE, FactionId.CIENIE_AL_ANDALUS, rng) is False


def test_marionette_detected_at_inquisitor():
    from inquisitio.engine.dungeon import detect_marionettes_at

    st = new_game(setup="4p-core", seed=1, layer="C")
    caa = st.players[FactionId.CIENIE_AL_ANDALUS]
    ag = caa.agents[0]
    ag.location = "trybunal"
    ag.double_agent = True
    ag.controller = FactionId.SWIETE_OFICJUM
    h0 = caa.heresy
    detect_marionettes_at(st, "trybunal")
    assert caa.heresy == h0 + 2
    assert not ag.double_agent

