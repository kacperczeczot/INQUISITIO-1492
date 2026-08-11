from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import asdict, dataclass, field
from typing import Any

from inquisitio.cards.loader import CardLoader
from inquisitio.engine.setup import SetupConfig, create_game, resolve_setup
from inquisitio.engine.turn import play_game


@dataclass
class BatchSummary:
    games: int
    threshold: int
    setup: str
    wins: dict[str, int] = field(default_factory=dict)
    win_reasons: dict[str, int] = field(default_factory=dict)
    avg_eras: float = 0.0
    critical_entries: float = 0.0
    accusations: float = 0.0
    verdicts: float = 0.0
    stakes: float = 0.0
    feint_rate: float = 0.0
    strategic_accusation_rate: float = 0.0
    max_heresy_avg: dict[str, float] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def run_batch(
    *,
    games: int = 100,
    threshold: int = 7,
    players: int | None = 3,
    setup: str | None = None,
    seed: int = 42,
) -> BatchSummary:
    loader = CardLoader()
    loader.load_all()
    cfg0 = resolve_setup(setup_name=setup, players=players, threshold=threshold, seed=seed)
    setup_label = setup or f"{len(cfg0.factions)}p"

    wins: Counter[str] = Counter()
    reasons: Counter[str] = Counter()
    sum_eras = 0
    sum_crit = 0
    sum_acc = 0
    sum_verd = 0
    sum_stakes = 0
    sum_feints = 0
    sum_plays = 0
    sum_strat = 0
    heresy_sums: dict[str, float] = defaultdict(float)
    heresy_counts: dict[str, int] = defaultdict(int)

    for i in range(games):
        cfg = SetupConfig(
            factions=list(cfg0.factions),
            threshold=threshold,
            max_eras=cfg0.max_eras,
            seed=seed + i,
            simplified=cfg0.simplified,
        )
        state = create_game(cfg, loader=loader)
        play_game(state)
        assert state.winner is not None
        wins[state.winner.value] += 1
        reasons[state.win_reason] += 1
        sum_eras += state.era
        m = state.metrics
        sum_crit += m.critical_entries
        sum_acc += m.accusations
        sum_verd += m.verdicts
        sum_stakes += m.stakes_total
        sum_feints += m.feints
        sum_plays += max(1, m.plays)
        sum_strat += m.strategic_accusations
        for fac, val in m.max_heresy_seen.items():
            heresy_sums[fac] += val
            heresy_counts[fac] += 1

    n = max(1, games)
    return BatchSummary(
        games=games,
        threshold=threshold,
        setup=setup_label,
        wins=dict(wins),
        win_reasons=dict(reasons),
        avg_eras=sum_eras / n,
        critical_entries=sum_crit / n,
        accusations=sum_acc / n,
        verdicts=sum_verd / n,
        stakes=sum_stakes / n,
        feint_rate=sum_feints / max(1, sum_plays),
        strategic_accusation_rate=(sum_strat / max(1, sum_acc)) if sum_acc else 0.0,
        max_heresy_avg={
            k: heresy_sums[k] / max(1, heresy_counts[k]) for k in heresy_sums
        },
    )


def compare_thresholds(
    *,
    games: int = 100,
    thresholds: list[int] | None = None,
    setup: str | None = "3p-oficjum-alandalus-korona",
    seed: int = 42,
) -> dict[str, BatchSummary]:
    thresholds = thresholds or [7, 8]
    return {
        str(t): run_batch(games=games, threshold=t, setup=setup, seed=seed)
        for t in thresholds
    }
