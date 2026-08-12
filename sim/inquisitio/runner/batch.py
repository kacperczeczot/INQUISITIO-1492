"""Batch runner — drama / deadlock metrics."""
from __future__ import annotations

import random
from collections import Counter
from dataclasses import dataclass, field

from inquisitio.agents.politics import PoliticsAgent
from inquisitio.engine.setup import SETUP_PRESETS, new_game
from inquisitio.engine.state import FactionId, GameState
from inquisitio.engine.turn import play_game


@dataclass
class BatchSummary:
    games: int
    setup: str
    threshold: int
    layer: str = "C"
    wins: dict[str, int] = field(default_factory=dict)
    autodafe_avg: float = 0.0
    accusations_avg: float = 0.0
    convictions_avg: float = 0.0
    hooks_avg: float = 0.0
    hooks_forced_avg: float = 0.0
    doubles_avg: float = 0.0
    deadlocks_avg: float = 0.0
    legal_moves_avg: float = 0.0
    eras_avg: float = 0.0
    cards_played_avg: float = 0.0


def run_batch(
    games: int = 100,
    *,
    threshold: int = 7,
    players: int | None = None,
    setup: str | None = None,
    seed: int = 42,
    layer: str = "C",
) -> BatchSummary:
    setup_name = setup or (
        "5p-full"
        if players == 5
        else "4p-core"
        if players == 4
        else "3p-oficjum-alandalus-korona"
    )
    if setup_name not in SETUP_PRESETS:
        setup_name = "3p-oficjum-alandalus-korona"

    wins: Counter[str] = Counter()
    totals = dict(
        autodafe=0,
        accusations=0,
        convictions=0,
        hooks=0,
        hooks_forced=0,
        doubles=0,
        deadlocks=0,
        legal=0,
        eras=0,
        cards=0,
    )

    for i in range(games):
        gseed = seed + i * 17
        rng = random.Random(gseed)
        state = new_game(setup=setup_name, seed=gseed, threshold=threshold, layer=layer)
        agent = PoliticsAgent(rng)

        def choose(st: GameState, fid: FactionId, legal: list[str]):
            return agent.choose_card(st, fid, legal)

        winner = play_game(state, rng, choose)
        wins[winner.value] += 1
        m = state.metrics
        totals["autodafe"] += m.autodafe_count
        totals["accusations"] += m.accusations
        totals["convictions"] += m.convictions
        totals["hooks"] += m.hooks_created
        totals["hooks_forced"] += m.hooks_forced
        totals["doubles"] += m.doubles_created
        totals["deadlocks"] += m.deadlocks
        totals["legal"] += m.legal_moves_sampled
        totals["eras"] += m.eras
        totals["cards"] += m.cards_played

    n = max(games, 1)
    return BatchSummary(
        games=games,
        setup=setup_name,
        threshold=threshold,
        layer=layer,
        wins=dict(wins),
        autodafe_avg=totals["autodafe"] / n,
        accusations_avg=totals["accusations"] / n,
        convictions_avg=totals["convictions"] / n,
        hooks_avg=totals["hooks"] / n,
        hooks_forced_avg=totals["hooks_forced"] / n,
        doubles_avg=totals["doubles"] / n,
        deadlocks_avg=totals["deadlocks"] / n,
        legal_moves_avg=totals["legal"] / n,
        eras_avg=totals["eras"] / n,
        cards_played_avg=totals["cards"] / n,
    )


def compare_thresholds(
    games: int = 100,
    thresholds: list[int] | None = None,
    setup: str = "3p-oficjum-alandalus-korona",
    seed: int = 42,
    layer: str = "C",
) -> dict[int, BatchSummary]:
    thresholds = thresholds or [7, 8]
    return {
        t: run_batch(games=games, threshold=t, setup=setup, seed=seed, layer=layer)
        for t in thresholds
    }
