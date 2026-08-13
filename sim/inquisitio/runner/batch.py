"""Batch runner — multi-threaded parallel execution across all CPU cores."""
from __future__ import annotations

import os
import random
from collections import Counter
from dataclasses import dataclass, field
from concurrent.futures import ProcessPoolExecutor

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
    eras_min: int = 8
    eras_max: int = 1
    eras_limit_pct: float = 0.0
    cards_played_avg: float = 0.0
    avg_gold_end: float = 0.0
    avg_heresy_end: float = 0.0
    passes_forced_pct: float = 0.0

def _run_single_game_tuple(args: tuple[str, int, int, str]) -> dict:
    setup_name, gseed, threshold, layer = args
    rng = random.Random(gseed)
    state = new_game(setup=setup_name, seed=gseed, threshold=threshold, layer=layer)
    agent = PoliticsAgent(rng)

    def choose(st: GameState, fid: FactionId, legal: list[str]):
        return agent.choose_card(st, fid, legal)

    winner = play_game(state, rng, choose)
    m = state.metrics

    gold_sum = sum(pl.gold for pl in state.players.values())
    heresy_sum = sum(pl.heresy for pl in state.players.values())

    return {
        "winner": winner.value,
        "eras": m.eras,
        "is_limit": m.eras >= state.max_eras,
        "autodafe": m.autodafe_count,
        "accusations": m.accusations,
        "convictions": m.convictions,
        "hooks": m.hooks_created,
        "hooks_forced": m.hooks_forced,
        "doubles": m.doubles_created,
        "deadlocks": m.deadlocks,
        "legal": m.legal_moves_sampled,
        "cards": m.cards_played,
        "forced_passes": m.forced_passes,
        "gold_sum": gold_sum,
        "heresy_sum": heresy_sum,
    }

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
        gold_end=0,
        heresy_end=0,
        forced_passes=0,
        limit_games=0,
    )
    eras_list = []

    # Parallel Execution via ProcessPoolExecutor if games >= 100
    if games >= 100:
        max_workers = min(os.cpu_count() or 4, 16)
        task_args = [
            (setup_name, seed + i * 17, threshold, layer)
            for i in range(games)
        ]
        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            game_results = list(executor.map(_run_single_game_tuple, task_args, chunksize=max(10, games // (max_workers * 4))))

        for res in game_results:
            wins[res["winner"]] += 1
            eras_list.append(res["eras"])
            if res["is_limit"]:
                totals["limit_games"] += 1

            totals["autodafe"] += res["autodafe"]
            totals["accusations"] += res["accusations"]
            totals["convictions"] += res["convictions"]
            totals["hooks"] += res["hooks"]
            totals["hooks_forced"] += res["hooks_forced"]
            totals["doubles"] += res["doubles"]
            totals["deadlocks"] += res["deadlocks"]
            totals["legal"] += res["legal"]
            totals["eras"] += res["eras"]
            totals["cards"] += res["cards"]
            totals["forced_passes"] += res["forced_passes"]
            totals["gold_end"] += res["gold_sum"]
            totals["heresy_end"] += res["heresy_sum"]
    else:
        for i in range(games):
            res = _run_single_game_tuple((setup_name, seed + i * 17, threshold, layer))
            wins[res["winner"]] += 1
            eras_list.append(res["eras"])
            if res["is_limit"]:
                totals["limit_games"] += 1

            totals["autodafe"] += res["autodafe"]
            totals["accusations"] += res["accusations"]
            totals["convictions"] += res["convictions"]
            totals["hooks"] += res["hooks"]
            totals["hooks_forced"] += res["hooks_forced"]
            totals["doubles"] += res["doubles"]
            totals["deadlocks"] += res["deadlocks"]
            totals["legal"] += res["legal"]
            totals["eras"] += res["eras"]
            totals["cards"] += res["cards"]
            totals["forced_passes"] += res["forced_passes"]
            totals["gold_end"] += res["gold_sum"]
            totals["heresy_end"] += res["heresy_sum"]

    n = max(games, 1)
    tot_players = sum(len(SETUP_PRESETS[setup_name]) for _ in range(games))
    tot_turns = totals["eras"] * 2 * len(SETUP_PRESETS[setup_name])

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
        eras_min=min(eras_list) if eras_list else 1,
        eras_max=max(eras_list) if eras_list else 8,
        eras_limit_pct=totals["limit_games"] / n,
        cards_played_avg=totals["cards"] / n,
        avg_gold_end=totals["gold_end"] / tot_players if tot_players else 0.0,
        avg_heresy_end=totals["heresy_end"] / tot_players if tot_players else 0.0,
        passes_forced_pct=totals["forced_passes"] / tot_turns if tot_turns else 0.0,
    )


def compare_thresholds(
    games: int = 100,
    thresholds: list[int] | None = None,
    setup: str | None = None,
    seed: int = 42,
    layer: str = "C",
) -> list[BatchSummary]:
    if thresholds is None:
        thresholds = [6, 7, 8]
    return [
        run_batch(games, threshold=t, setup=setup, seed=seed, layer=layer)
        for t in thresholds
    ]

