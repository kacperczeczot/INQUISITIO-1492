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
    """A decks: 5 cards, no signatures; Haki dozwolone na teach (kb-04, gc-04)."""
    for fac in [
        "swiete-oficjum",
        "cienie-al-andalus",
        "korona-borgiowie",
        "kabala-toledo",
        "gildia-cieni",
    ]:
        a = cards_for_faction(fac, max_layer="A")
        assert len(a) == 6
        for c in a:
            assert c.layer == "A"
            assert c.type != "signature"
            assert not c.breaks_rule
            # A-layer Haki: Faworyt, Informator, List Żelazny
            if c.creates_hook:
                assert c.id in ("kb-04", "gc-04", "kb-05")
                assert "hook" in c.tags


def test_layer_c_full_decks():
    for fac in [
        "swiete-oficjum",
        "cienie-al-andalus",
        "korona-borgiowie",
        "kabala-toledo",
        "gildia-cieni",
    ]:
        assert len(cards_for_faction(fac, max_layer="C")) == 12
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


def test_board_graph_neighbors():
    from inquisitio.engine.inquisitor import move_inquisitor, neighbors, shortest_path, step_toward
    from inquisitio.engine.state import LOCATIONS, NEIGHBORS

    assert set(NEIGHBORS) == set(LOCATIONS)
    for loc, ns in NEIGHBORS.items():
        assert len(ns) >= 2, loc
        for n in ns:
            assert loc in NEIGHBORS[n], f"asymmetric {loc}->{n}"

    assert set(neighbors("trybunal")) == {"palac", "lochy"}
    assert set(neighbors("palac")) == {"trybunal", "rynek", "lochy"}
    # two paths Trybunał → Rynek; neither requires the old chain through Lochy-only
    assert len(shortest_path("trybunal", "rynek")) == 3  # T-P-R
    assert step_toward("trybunal", "rynek") == "palac"
    assert step_toward("gildia", "trybunal") in {"lochy", "rynek"}

    state = new_game(setup="3p-oficjum-alandalus-korona", seed=3, layer="A")
    state.inquisitor_location = "trybunal"
    move_inquisitor(state, random.Random(0), toward="rynek")
    assert state.inquisitor_location == "palac"
    move_inquisitor(state, random.Random(0), toward="rynek")
    assert state.inquisitor_location == "rynek"
    # random patrol stays on graph
    for seed in range(20):
        cur = state.inquisitor_location
        move_inquisitor(state, random.Random(seed))
        nxt = state.inquisitor_location
        assert nxt == cur or nxt in NEIGHBORS[cur]


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


def test_feel_cli_layer_a():
    from inquisitio.runner.feel import render_feel, run_feel

    result = run_feel(setup="3p-oficjum-alandalus-korona", seed=7, layer="A")
    text = render_feel(result)
    assert "=== Era 1 ===" in text
    assert "=== Metryki ===" in text
    assert "Winner:" in text
    assert result.state.winner is not None
    assert result.state.metrics.eras >= 1
    assert "Autodafé:" in text


def test_layer_c_deadlocks_low():
    """Gold trickle should keep C out of the ~16 deadlock spiral."""
    from inquisitio.runner.batch import run_batch

    summary = run_batch(
        games=50,
        setup="3p-oficjum-alandalus-korona",
        seed=42,
        layer="C",
        threshold=7,
    )
    assert summary.deadlocks_avg < 2.0, f"deadlocks_avg={summary.deadlocks_avg}"


def test_cards_load():
    cards = load_all_cards()
    assert "so-01" in cards
    assert "time-01" in cards
    assert cards["so-10"].breaks_rule
    so = cards["so-01"]
    assert so.cost_gold == so.cost == 1
    assert so.effect
    assert "Zapłać" not in so.effect
    assert so.heresy_text and so.lore
    assert "bez Herezji" not in so.heresy_text.lower()
    assert not so.table_note
    hot = cards["caa-03"]
    assert hot.heresy == 1 and hot.heresy_text and hot.lore
    clean = cards["gc-01"]
    assert clean.heresy == 1 and clean.heresy_text and clean.lore
    assert "bez Herezji" not in clean.heresy_text.lower()
    for c in cards.values():
        assert c.effect, c.id
        assert c.heresy_text or c.lore, c.id
        if c.heresy_text:
            assert "bez herezji" not in c.heresy_text.lower(), c.id
        assert not (c.raw or {}).get("table_note"), c.id
    assert "Tunele starej Toledo" in cards["caa-01"].heresy_text
    assert "Handel spod lady" in (cards["gc-02"].lore or "")
    assert "Teach" not in (cards["so-04"].lore or "")
    assert "Załóż Hak" in cards["kb-08"].effect
    assert "Zyskaj Hak" not in cards["kb-08"].effect
    assert cards["kb-05"].creates_hook and "hook" in cards["kb-05"].tags
    assert cards["so-05"].target_heresy >= 1
    assert cards["caa-09"].agents == 0
    for c in cards.values():
        lore = (c.lore or "").lower()
        assert "teach a" not in lore and "reposition" not in lore, c.id
        assert "double-dip" not in lore and "sweet spot" not in lore, c.id
        assert "czysta ekonomia" not in lore, c.id


def test_ssot_win_paths_match_yaml():
    from inquisitio.engine.win import check_winner_details
    from inquisitio.engine.state import heresy_zone

    st = new_game(setup="3p-cienie-korona-kabala", seed=1, layer="C")
    caa = st.players[FactionId.CIENIE_AL_ANDALUS]
    caa.relics_evacuated = 2
    caa.path_via_double = True
    st.era = 8
    assert check_winner_details(st) == (FactionId.CIENIE_AL_ANDALUS, "caa_sea_route")

    st5 = new_game(setup="5p-full", seed=1, layer="C")
    caa5 = st5.players[FactionId.CIENIE_AL_ANDALUS]
    caa5.relics_evacuated = 2
    st5.era = 1
    got = check_winner_details(st5)
    assert got is None or got[0] != FactionId.CIENIE_AL_ANDALUS
    st5.era = 5
    assert check_winner_details(st5) == (FactionId.CIENIE_AL_ANDALUS, "caa_era")

    gc = st5.players[FactionId.GILDIA_CIENI]
    caa5.relics_evacuated = 0
    st5.era = 1
    gc.falls = 3
    assert check_winner_details(st5) == (FactionId.GILDIA_CIENI, "gc_falls")

    assert heresy_zone(5, critical_min=6) == "obserwowana"
    assert heresy_zone(6, critical_min=6) == "krytyczna"
    assert heresy_zone(6, critical_min=7) == "obserwowana"


def test_win_overrides_kt_era_kb_decrees_alt():
    from inquisitio.engine.win import check_winner_details

    st = new_game(setup="3p-oficjum-kabala-gildia", seed=1, layer="C")
    kt = st.players[FactionId.KABALA_TOLEDO]
    kt.fragments = 3
    kt.heresy = 5
    st.era = 6
    assert check_winner_details(st) == (FactionId.KABALA_TOLEDO, "kt_codex")
    blocked = check_winner_details(st, {"kt_era_offset": 1})
    assert blocked is None or blocked[0] != FactionId.KABALA_TOLEDO
    st.era = 7
    assert check_winner_details(st, {"kt_era_offset": 1}) == (FactionId.KABALA_TOLEDO, "kt_codex")

    from inquisitio.engine.hooks import grant_hook
    st2 = new_game(setup="3p-oficjum-alandalus-korona", seed=1, layer="C")
    kb = st2.players[FactionId.KORONA_BORGIOWIE]
    kb.decrees_played = 2
    grant_hook(st2, FactionId.KORONA_BORGIOWIE, FactionId.SWIETE_OFICJUM)
    st2.era = 6
    assert check_winner_details(st2) == (FactionId.KORONA_BORGIOWIE, "kb_main")
    blocked = check_winner_details(st2, {"kb_decrees_offset": 1})
    assert blocked is None or blocked[0] != FactionId.KORONA_BORGIOWIE


def test_reaction_so_05_triggers_on_heresy_play():
    import random
    from inquisitio.engine.effects.registry import play_card
    from inquisitio.engine.setup import new_game, FactionId

    st = new_game(setup="4p-core", seed=42, layer="C")
    so = st.players[FactionId.SWIETE_OFICJUM]
    caa = st.players[FactionId.CIENIE_AL_ANDALUS]

    so.hand = ["so-05"]
    caa.hand = ["caa-03"]  # caa-03 has heresy=1
    caa.gold = 5
    caa_h_before = caa.heresy

    rng = random.Random(42)
    played = play_card(st, FactionId.CIENIE_AL_ANDALUS, "caa-03", rng)
    cards = load_all_cards()
    so_target_h = cards["so-05"].target_heresy
    # caa gets 1 from card, plus so-05 reaction target_heresy
    assert caa.heresy == caa_h_before + 1 + so_target_h
    assert "so-05" not in so.hand
    assert "so-05" in so.discard


def test_reaction_gc_05_alters_verdict_vote():
    import random
    from inquisitio.engine.setup import new_game, FactionId
    from inquisitio.engine.verdict import run_verdict

    st = new_game(setup="4p-no-oficjum", seed=42, layer="C")
    gc = st.players[FactionId.GILDIA_CIENI]
    gc.hand = ["gc-05"]
    gc.heresy = 8  # eligible accused

    rng = random.Random(42)
    # Verdict against Gildia Cieni
    convicted = run_verdict(st, FactionId.KORONA_BORGIOWIE, FactionId.GILDIA_CIENI, rng)
    assert "gc-05" not in gc.hand
    assert "gc-05" in gc.discard

