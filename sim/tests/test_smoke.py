import pytest

from inquisitio.cards.loader import CardLoader
from inquisitio.engine.setup import create_game, resolve_setup
from inquisitio.engine.turn import play_game
from inquisitio.engine.win import check_winner
from inquisitio.engine.effects.registry import register_defaults, get_handler, _REGISTRY
from inquisitio.model import FactionId
from inquisitio.runner.batch import run_batch


def test_loader_counts():
    cards = CardLoader().load_all()
    assert len(cards) == 58
    assert sum(1 for c in cards.values() if c.faction == FactionId.TIME) == 8
    assert sum(1 for c in cards.values() if c.faction == FactionId.SWIETE_OFICJUM) == 10


def test_all_handlers_registered():
    register_defaults()
    cards = CardLoader().load_all()
    missing = [cid for cid in cards if get_handler(cid) is None]
    assert not missing, f"missing handlers: {missing}"
    assert len(_REGISTRY) >= 58


def test_smoke_game_completes():
    cfg = resolve_setup(players=3, seed=7)
    state = create_game(cfg)
    play_game(state)
    assert state.winner is not None
    assert state.era >= 1
    assert state.metrics.plays > 0


def test_win_stakes():
    cfg = resolve_setup(setup_name="3p-oficjum-alandalus-korona", seed=0)
    state = create_game(cfg)
    state.player(FactionId.SWIETE_OFICJUM).stakes = 2
    assert check_winner(state) == FactionId.SWIETE_OFICJUM


def test_win_korona_needs_two_each():
    cfg = resolve_setup(setup_name="3p-oficjum-alandalus-korona", seed=0)
    state = create_game(cfg)
    k = state.player(FactionId.KORONA_BORGIOWIE)
    k.control_palace = 1
    k.control_market = 1
    assert check_winner(state) is None
    k.control_palace = 2
    k.control_market = 2
    assert check_winner(state) == FactionId.KORONA_BORGIOWIE


def test_batch_deterministic():
    a = run_batch(games=5, setup="3p-oficjum-alandalus-korona", seed=99, threshold=7)
    b = run_batch(games=5, setup="3p-oficjum-alandalus-korona", seed=99, threshold=7)
    assert a.wins == b.wins
    assert a.avg_eras == b.avg_eras
