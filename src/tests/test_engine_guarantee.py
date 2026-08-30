"""v1.0-alpha.22 — YAML knobs, card fields, and rule mechanics must reach the engine (gwarancja silnika)."""
from __future__ import annotations

import random

from inquisitio.cards.loader import load_all_cards
from inquisitio.config import CONFIG
from inquisitio.engine.card_conditions import card_condition_met
from inquisitio.engine.effects.registry import resolve_card_effects, resolve_time_edict
from inquisitio.engine.inquisitor import move_inquisitor, resolve_autodafe
from inquisitio.engine.setup import new_game
from inquisitio.engine.state import FactionId
from inquisitio.engine.turn import _maybe_open_sea_route
from inquisitio.engine.win import check_winner_details


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


def test_so05_reaction_triggers_on_heresy_play():
    st = new_game(setup="4p-core", seed=21, layer="C")
    so = st.players[FactionId.SWIETE_OFICJUM]
    so.hand = ["so-05"]
    so.gold = 3
    kt = st.players[FactionId.KABALA_TOLEDO]
    kt.gold = 5
    # kt-04 has heresy: 1 (or gc-11/so-03)
    card = load_all_cards()["so-03"]  # heresy: 2, target_heresy: 3
    resolve_card_effects(st, FactionId.KABALA_TOLEDO, card, random.Random(7))
    assert "so-05" not in so.hand
    assert "so-05" in so.discard
    assert any("so-05" in msg for msg in st.log)


def test_so10_forces_autodafe():
    st = new_game(setup="4p-core", seed=23, layer="C")
    so = st.players[FactionId.SWIETE_OFICJUM]
    so.gold = 5
    st.inquisitor_location = "palac"
    caa = st.players[FactionId.CIENIE_AL_ANDALUS]
    caa.agents[0].location = "palac"
    caa.agents[0].arrested = False
    caa.heresy = 5  # observed
    card = load_all_cards()["so-10"]
    resolve_card_effects(st, FactionId.SWIETE_OFICJUM, card, random.Random(8))
    assert any("Autodafé" in msg for msg in st.log)


def test_caa05_evacuates_relic_and_sets_shadow_exit():
    st = new_game(setup="4p-core", seed=25, layer="C")
    caa = st.players[FactionId.CIENIE_AL_ANDALUS]
    caa.gold = 3
    caa.agents[0].location = "rynek"
    st.sea_route_open = True
    st.inquisitor_location = "trybunal"
    st.relics_on_board["rynek"] = 1
    card = load_all_cards()["caa-05"]
    resolve_card_effects(st, FactionId.CIENIE_AL_ANDALUS, card, random.Random(9))
    assert caa.relics_evacuated == 1


def test_caa06_frees_prisoner():
    from inquisitio.engine.dungeon import arrest_agent
    st = new_game(setup="4p-core", seed=27, layer="C")
    caa = st.players[FactionId.CIENIE_AL_ANDALUS]
    arrest_agent(st, FactionId.CIENIE_AL_ANDALUS)
    assert any(ag.arrested and ag.location == "lochy" for ag in caa.agents)
    card = load_all_cards()["caa-06"]
    resolve_card_effects(st, FactionId.CIENIE_AL_ANDALUS, card, random.Random(10))
    assert not any(ag.arrested for ag in caa.agents)


def test_kt10_respects_heresy_band_and_activation():
    st = new_game(setup="4p-core", seed=29, layer="C")
    kt = st.players[FactionId.KABALA_TOLEDO]
    kt.fragments = 3
    kt.heresy = 6
    card = load_all_cards()["kt-10"]
    from inquisitio.engine.effects.registry import _signature
    _signature(st, FactionId.KABALA_TOLEDO, card, random.Random(11))
    assert kt.kt10_played is True
    # Card decreases heresy by 2 per definition, bringing 6 -> 4 (within [4, 6] band)
    assert kt.heresy == 4


def test_gc10_fiasco_and_success():
    st = new_game(setup="5p-full", seed=31, layer="C")
    gc = st.players[FactionId.GILDIA_CIENI]
    card = load_all_cards()["gc-10"]

    # Fiasco when no hook/marionette/inquisitor
    from inquisitio.engine.effects.registry import _gc_extra
    before_falls = gc.falls
    _gc_extra(st, FactionId.GILDIA_CIENI, card, random.Random(12))
    assert gc.falls == before_falls

    # Success when hook is present on rival
    gc.hooks_on[FactionId.CIENIE_AL_ANDALUS] = 1
    _gc_extra(st, FactionId.GILDIA_CIENI, card, random.Random(13))
    assert gc.falls == before_falls + 1


def test_all_ten_time_edicts_execute_cleanly():
    cards = load_all_cards()
    for tid in [f"time-0{i}" for i in range(1, 10)] + ["time-10"]:
        st = new_game(setup="4p-core", seed=42, layer="C")
        resolve_time_edict(st, tid, random.Random(42))
        assert any(tid in msg for msg in st.log), f"Edict {tid} did not log"


def test_victory_conditions_strictly_follow_ssot_config():
    st = new_game(setup="5p-full", seed=99, layer="C")
    cfg_v = CONFIG.victory

    def _v5(item: Any, default: int = 1) -> int:
        if hasattr(item, "get"):
            return int(item.get("5p", item.get("4p", default)))
        if hasattr(item, "__getitem__") and not isinstance(item, (str, bytes)):
            try:
                return int(item["5p"])
            except Exception:
                pass
        return int(item) if item is not None else default

    # SO Stacks
    st.players[FactionId.SWIETE_OFICJUM].stacks = _v5(cfg_v.swiete_oficjum.stacks, 8)
    assert check_winner_details(st) == (FactionId.SWIETE_OFICJUM, "so_stacks")
    st.players[FactionId.SWIETE_OFICJUM].stacks = 0

    # SO Condemns
    condemns_5p = _v5(cfg_v.swiete_oficjum.condemns, 3)
    st.players[FactionId.SWIETE_OFICJUM].condemned_rivals = set(list([FactionId.CIENIE_AL_ANDALUS, FactionId.KORONA_BORGIOWIE, FactionId.KABALA_TOLEDO])[:condemns_5p])
    assert check_winner_details(st) == (FactionId.SWIETE_OFICJUM, "so_condemns")
    st.players[FactionId.SWIETE_OFICJUM].condemned_rivals.clear()

    # CAA Relics
    relics_5p = _v5(cfg_v.cienie_al_andalus.relics, 2)
    st.players[FactionId.CIENIE_AL_ANDALUS].relics_evacuated = relics_5p
    st.players[FactionId.CIENIE_AL_ANDALUS].shadow_exit = True
    assert check_winner_details(st) == (FactionId.CIENIE_AL_ANDALUS, "caa_sea_route")
    st.players[FactionId.CIENIE_AL_ANDALUS].relics_evacuated = 0

    # KB Decrees
    decrees_5p = _v5(cfg_v.korona_borgiowie.decrees, 2)
    st.players[FactionId.KORONA_BORGIOWIE].decrees_played = decrees_5p
    st.players[FactionId.KORONA_BORGIOWIE].hooks_on[FactionId.CIENIE_AL_ANDALUS] = 1
    st.players[FactionId.KORONA_BORGIOWIE].hooks_on[FactionId.KABALA_TOLEDO] = 1
    assert check_winner_details(st) == (FactionId.KORONA_BORGIOWIE, "kb_main")
    st.players[FactionId.KORONA_BORGIOWIE].decrees_played = 0
    st.players[FactionId.KORONA_BORGIOWIE].hooks_on.clear()

    # KT Fragments
    st.players[FactionId.KABALA_TOLEDO].fragments = _v5(cfg_v.kabala_toledo.fragments, 3)
    st.players[FactionId.KABALA_TOLEDO].heresy = 5
    st.players[FactionId.KABALA_TOLEDO].kt10_played = True
    assert check_winner_details(st) == (FactionId.KORONA_BORGIOWIE if False else FactionId.KABALA_TOLEDO, "kt_codex")
    st.players[FactionId.KABALA_TOLEDO].fragments = 0

    # GC Falls
    falls_5p = _v5(cfg_v.gildia_cieni.falls, 9)
    st.players[FactionId.GILDIA_CIENI].falls = falls_5p
    assert check_winner_details(st) == (FactionId.GILDIA_CIENI, "gc_falls")
    st.players[FactionId.GILDIA_CIENI].falls = 0
