"""Batch runner — multi-threaded parallel execution across all CPU cores."""
from __future__ import annotations

import gc
import os
import random
import multiprocessing
from collections import Counter
from dataclasses import dataclass, field
from concurrent.futures import ProcessPoolExecutor

from inquisitio.agents.politics import PoliticsAgent
from inquisitio.engine.setup import SETUP_PRESETS, new_game
from inquisitio.engine.state import FactionId, GameState
from inquisitio.engine.turn import play_game

# Use Python SSOT engine for complete mathematical fidelity and valid scores
_HAS_NATIVE = False

@dataclass
class BatchSummary:
    games: int
    setup: str
    threshold: int
    layer: str = "C"
    wins: dict[str, int] = field(default_factory=dict)
    win_paths: dict[str, int] = field(default_factory=dict)
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
    autodafe_min: int = 0
    autodafe_max: int = 0
    accusations_min: int = 0
    accusations_max: int = 0
    gold_min: float = 0.0
    gold_max: float = 0.0
    heresy_min: float = 0.0
    heresy_max: float = 0.0
    eras_limit_pct: float = 0.0
    cards_played_avg: float = 0.0
    avg_gold_end: float = 0.0
    avg_heresy_end: float = 0.0
    passes_forced_pct: float = 0.0
    card_plays_total: dict[str, int] = field(default_factory=dict)
    era_hist: dict[int, int] = field(default_factory=dict)
    era_faction_wins: dict[int, dict[str, int]] = field(default_factory=dict)

def _run_single_game_tuple(args: tuple[str, int, int, str, dict | None]) -> dict:
    setup_name, gseed, threshold, layer, win_overrides = args
    rng = random.Random(gseed)
    state = new_game(setup=setup_name, seed=gseed, threshold=threshold, layer=layer, sys_overrides=win_overrides, enable_log=False)
    agent = PoliticsAgent(rng)

    def choose(st: GameState, fid: FactionId, legal: list[str]):
        return agent.choose_card(st, fid, legal)

    winner = play_game(state, rng, choose, win_overrides=win_overrides)
    m = state.metrics

    gold_sum = sum(pl.gold for pl in state.players.values())
    heresy_sum = sum(pl.heresy for pl in state.players.values())

    return {
        "winner": winner.value,
        "win_path": getattr(state, "win_path", "unknown"),
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
        "card_plays": dict(m.card_plays),
        "forced_passes": m.forced_passes,
        "gold_sum": gold_sum,
        "heresy_sum": heresy_sum,
    }

def run_batch(
    games: int = 100,
    *,
    threshold: int = 8,
    players: int | None = None,
    setup: str | None = None,
    seed: int = 42,
    layer: str = "C",
    win_overrides: dict | None = None,
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

    if _HAS_NATIVE:
        res = inquisitio_native.run_batch(
            games=games,
            setup=setup_name,
            seed=seed,
            threshold=threshold,
            layer=layer,
            win_overrides=win_overrides or {},
        )
        return BatchSummary(
            games=games,
            setup=setup_name,
            threshold=threshold,
            layer=layer,
            wins=res["wins"],
            win_paths=res["win_paths"],
            era_hist=res["era_hist"],
            eras_avg=res.get("eras_avg", 0.0),
            autodafe_avg=res.get("autodafe_avg", 0.0),
            accusations_avg=res.get("accusations_avg", 0.0),
            convictions_avg=res.get("convictions_avg", 0.0),
            deadlocks_avg=res.get("deadlocks_avg", 0.0),
            eras_limit_pct=res.get("eras_limit_pct", 0.0),
            avg_gold_end=res.get("avg_gold_end", 0.0),
            avg_heresy_end=res.get("avg_heresy_end", 0.0),
            passes_forced_pct=res.get("passes_forced_pct", 0.0),
        )

    wins: Counter[str] = Counter()
    win_paths: Counter[str] = Counter()
    card_plays_agg = Counter()
    era_hist = Counter()
    era_faction_wins: dict[int, Counter] = {}
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
    autodafe_list = []
    accusations_list = []
    gold_list = []
    heresy_list = []

    # Parallel Execution via ProcessPoolExecutor if games >= 100 and in MainProcess
    if games >= 100 and multiprocessing.current_process().name == "MainProcess":
        max_workers = min(os.cpu_count() or 4, 16)
        task_args = [
            (setup_name, seed + i * 17, threshold, layer, win_overrides)
            for i in range(games)
        ]
        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            game_results = list(executor.map(_run_single_game_tuple, task_args, chunksize=max(10, games // (max_workers * 4))))

        for res in game_results:
            winner = res["winner"]
            era = res["eras"]
            wins[winner] += 1
            win_paths[res["win_path"]] += 1
            era_hist[era] += 1
            if era not in era_faction_wins:
                era_faction_wins[era] = Counter()
            era_faction_wins[era][winner] += 1

            eras_list.append(era)

            autodafe_list.append(res["autodafe"])
            accusations_list.append(res["accusations"])
            n_pl = len(SETUP_PRESETS[setup_name])
            gold_list.append(res["gold_sum"] / n_pl)
            heresy_list.append(res["heresy_sum"] / n_pl)

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
            totals["eras"] += era
            totals["cards"] += res["cards"]
            totals["forced_passes"] += res["forced_passes"]
            totals["gold_end"] += res["gold_sum"]
            totals["heresy_end"] += res["heresy_sum"]
            for cid, cnt in res.get("card_plays", {}).items():
                card_plays_agg[cid] += cnt
    else:
        gc_was_enabled = gc.isenabled()
        if gc_was_enabled:
            gc.disable()
        try:
            for i in range(games):
                res = _run_single_game_tuple((setup_name, seed + i * 17, threshold, layer, win_overrides))
                winner = res["winner"]
                era = res["eras"]
                wins[winner] += 1
                win_paths[res["win_path"]] += 1
                era_hist[era] += 1
                if era not in era_faction_wins:
                    era_faction_wins[era] = Counter()
                era_faction_wins[era][winner] += 1

                eras_list.append(era)
                autodafe_list.append(res["autodafe"])
                accusations_list.append(res["accusations"])
                n_pl = len(SETUP_PRESETS[setup_name])
                gold_list.append(res["gold_sum"] / n_pl)
                heresy_list.append(res["heresy_sum"] / n_pl)

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
                totals["eras"] += era
                totals["cards"] += res["cards"]
                totals["forced_passes"] += res["forced_passes"]
                totals["gold_end"] += res["gold_sum"]
                totals["heresy_end"] += res["heresy_sum"]
                for cid, cnt in res.get("card_plays", {}).items():
                    card_plays_agg[cid] += cnt
        finally:
            if gc_was_enabled:
                gc.enable()


    n = max(games, 1)
    tot_players = sum(len(SETUP_PRESETS[setup_name]) for _ in range(games))
    tot_turns = totals["eras"] * 2 * len(SETUP_PRESETS[setup_name])

    return BatchSummary(
        games=games,
        setup=setup_name,
        threshold=threshold,
        layer=layer,
        wins=dict(wins),
        win_paths=dict(win_paths),
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
        autodafe_min=min(autodafe_list) if autodafe_list else 0,
        autodafe_max=max(autodafe_list) if autodafe_list else 0,
        accusations_min=min(accusations_list) if accusations_list else 0,
        accusations_max=max(accusations_list) if accusations_list else 0,
        gold_min=min(gold_list) if gold_list else 0.0,
        gold_max=max(gold_list) if gold_list else 0.0,
        heresy_min=min(heresy_list) if heresy_list else 0.0,
        heresy_max=max(heresy_list) if heresy_list else 0.0,
        eras_limit_pct=totals["limit_games"] / n,
        cards_played_avg=totals["cards"] / n,
        avg_gold_end=totals["gold_end"] / tot_players if tot_players else 0.0,
        avg_heresy_end=totals["heresy_end"] / tot_players if tot_players else 0.0,
        passes_forced_pct=totals["forced_passes"] / tot_turns if tot_turns else 0.0,
        card_plays_total=dict(card_plays_agg),
        era_hist={k: era_hist[k] for k in sorted(era_hist.keys())},
        era_faction_wins={k: dict(v) for k, v in sorted(era_faction_wins.items())},
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


def merge_batch_summaries(summaries: list[BatchSummary]) -> BatchSummary:
    """Merges multiple BatchSummary objects (e.g. from incremental micro-batches) into a single aggregated summary."""
    if not summaries:
        raise ValueError("Cannot merge empty list of BatchSummary")
    if len(summaries) == 1:
        return summaries[0]

    first = summaries[0]
    setup_name = first.setup
    threshold = first.threshold
    layer = first.layer

    total_games = sum(s.games for s in summaries)
    if total_games == 0:
        return first

    merged_wins: Counter[str] = Counter()
    merged_win_paths: Counter[str] = Counter()
    merged_card_plays: Counter[str] = Counter()
    merged_era_hist: Counter[int] = Counter()
    merged_era_faction_wins: dict[int, Counter] = {}

    weighted_autodafe = 0.0
    weighted_accusations = 0.0
    weighted_convictions = 0.0
    weighted_hooks = 0.0
    weighted_hooks_forced = 0.0
    weighted_doubles = 0.0
    weighted_deadlocks = 0.0
    weighted_legal_moves = 0.0
    weighted_eras = 0.0
    weighted_eras_limit_pct = 0.0
    weighted_cards_played = 0.0
    weighted_avg_gold_end = 0.0
    weighted_avg_heresy_end = 0.0
    weighted_passes_forced_pct = 0.0

    eras_min_val = min(s.eras_min for s in summaries)
    eras_max_val = max(s.eras_max for s in summaries)
    autodafe_min_val = min(s.autodafe_min for s in summaries)
    autodafe_max_val = max(s.autodafe_max for s in summaries)
    accusations_min_val = min(s.accusations_min for s in summaries)
    accusations_max_val = max(s.accusations_max for s in summaries)
    gold_min_val = min(s.gold_min for s in summaries)
    gold_max_val = max(s.gold_max for s in summaries)
    heresy_min_val = min(s.heresy_min for s in summaries)
    heresy_max_val = max(s.heresy_max for s in summaries)

    for s in summaries:
        w = s.games
        for fid, count in s.wins.items():
            merged_wins[fid] += count
        for wp, count in s.win_paths.items():
            merged_win_paths[wp] += count
        for cid, count in s.card_plays_total.items():
            merged_card_plays[cid] += count
        for era, count in s.era_hist.items():
            merged_era_hist[era] += count
        for era, f_dict in s.era_faction_wins.items():
            if era not in merged_era_faction_wins:
                merged_era_faction_wins[era] = Counter()
            for fid, count in f_dict.items():
                merged_era_faction_wins[era][fid] += count

        weighted_autodafe += s.autodafe_avg * w
        weighted_accusations += s.accusations_avg * w
        weighted_convictions += s.convictions_avg * w
        weighted_hooks += s.hooks_avg * w
        weighted_hooks_forced += s.hooks_forced_avg * w
        weighted_doubles += s.doubles_avg * w
        weighted_deadlocks += s.deadlocks_avg * w
        weighted_legal_moves += s.legal_moves_avg * w
        weighted_eras += s.eras_avg * w
        weighted_eras_limit_pct += s.eras_limit_pct * w
        weighted_cards_played += s.cards_played_avg * w
        weighted_avg_gold_end += s.avg_gold_end * w
        weighted_avg_heresy_end += s.avg_heresy_end * w
        weighted_passes_forced_pct += s.passes_forced_pct * w

    return BatchSummary(
        games=total_games,
        setup=setup_name,
        threshold=threshold,
        layer=layer,
        wins=dict(merged_wins),
        win_paths=dict(merged_win_paths),
        autodafe_avg=weighted_autodafe / total_games,
        accusations_avg=weighted_accusations / total_games,
        convictions_avg=weighted_convictions / total_games,
        hooks_avg=weighted_hooks / total_games,
        hooks_forced_avg=weighted_hooks_forced / total_games,
        doubles_avg=weighted_doubles / total_games,
        deadlocks_avg=weighted_deadlocks / total_games,
        legal_moves_avg=weighted_legal_moves / total_games,
        eras_avg=weighted_eras / total_games,
        eras_min=eras_min_val,
        eras_max=eras_max_val,
        autodafe_min=autodafe_min_val,
        autodafe_max=autodafe_max_val,
        accusations_min=accusations_min_val,
        accusations_max=accusations_max_val,
        gold_min=gold_min_val,
        gold_max=gold_max_val,
        heresy_min=heresy_min_val,
        heresy_max=heresy_max_val,
        eras_limit_pct=weighted_eras_limit_pct / total_games,
        cards_played_avg=weighted_cards_played / total_games,
        avg_gold_end=weighted_avg_gold_end / total_games,
        avg_heresy_end=weighted_avg_heresy_end / total_games,
        passes_forced_pct=weighted_passes_forced_pct / total_games,
        card_plays_total=dict(merged_card_plays),
        era_hist={k: merged_era_hist[k] for k in sorted(merged_era_hist.keys())},
        era_faction_wins={k: dict(v) for k, v in sorted(merged_era_faction_wins.items())},
    )


