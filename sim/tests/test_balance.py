"""Balance matrix — all setups × layers (not just two rigid configs)."""
from __future__ import annotations

import pytest

from inquisitio.engine.setup import SETUP_PRESETS
from inquisitio.runner.balance import evaluate, faction_shares, gate_for, run_matrix
from inquisitio.runner.batch import run_batch

ALL_SETUPS = sorted(SETUP_PRESETS.keys())
PRODUCT_LAYERS = ("B", "C")


@pytest.mark.parametrize("setup", ALL_SETUPS)
def test_setup_preset_size(setup: str):
    n = len(SETUP_PRESETS[setup])
    assert 3 <= n <= 5
    assert len(set(SETUP_PRESETS[setup])) == n


@pytest.mark.parametrize("setup", ALL_SETUPS)
@pytest.mark.parametrize("layer", PRODUCT_LAYERS)
def test_balance_matrix_product(setup: str, layer: str):
    """Every documented composition must pass win-share + health gates."""
    games = 300
    summary = run_batch(
        games=games, setup=setup, seed=42, layer=layer, threshold=7
    )
    ok, errors = evaluate(summary)
    shares = faction_shares(summary)
    gate = gate_for(setup, layer)
    assert ok, (
        f"{setup} L{layer} gate={gate} "
        f"shares={{{', '.join(f'{k}:{v:.0%}' for k, v in shares.items())}}} "
        f"dead={summary.deadlocks_avg:.2f} acc={summary.accusations_avg:.2f} :: {errors}"
    )


@pytest.mark.parametrize("setup", ALL_SETUPS)
def test_deadlocks_all_setups_layer_c(setup: str):
    summary = run_batch(games=40, setup=setup, seed=7, layer="C", threshold=7)
    assert summary.deadlocks_avg < 1.0, (
        f"{setup} deadlocks={summary.deadlocks_avg} wins={summary.wins}"
    )


@pytest.mark.parametrize("setup", ALL_SETUPS)
def test_smoke_game_completes_all_setups(setup: str):
    """One full C game per setup — winner in turn order, eras >= 1."""
    import random

    from inquisitio.agents.politics import PoliticsAgent
    from inquisitio.engine.setup import new_game
    from inquisitio.engine.turn import play_game

    rng = random.Random(hash(setup) % 10_000)
    state = new_game(setup=setup, seed=99, layer="C")
    agent = PoliticsAgent(rng)
    winner = play_game(
        state, rng, lambda st, fid, legal: agent.choose_card(st, fid, legal)
    )
    assert winner in state.turn_order
    assert state.metrics.eras >= 1


def test_matrix_cli_helper_covers_all_presets():
    rows = run_matrix(games=5, seed=1, layers=("C",))
    assert len(rows) == len(SETUP_PRESETS)
    assert all(s.games == 5 for s, _, _ in rows)


@pytest.mark.parametrize("seed", [42, 99, 123])
@pytest.mark.parametrize(
    "setup",
    [
        "3p-oficjum-alandalus-korona",
        "3p-oficjum-kabala-gildia",
        "3p-cienie-korona-gildia",
        "3p-oficjum-alandalus-gildia",
        "4p-core",
        "5p-full",
    ],
)
def test_balance_c_multi_seed_core_setups(setup: str, seed: int):
    """Core compositions must hold across seeds on layer C (no seed-42 overfitting)."""
    summary = run_batch(
        games=300, setup=setup, seed=seed, layer="C", threshold=7
    )
    ok, errors = evaluate(summary)
    assert ok, f"{setup} seed={seed} {errors} wins={summary.wins}"
