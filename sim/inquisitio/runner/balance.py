"""Balance gates — shared criteria for matrix tests and CLI."""
from __future__ import annotations

from dataclasses import dataclass

from inquisitio.engine.setup import SETUP_PRESETS
from inquisitio.runner.batch import BatchSummary, run_batch

LAYERS = ("A", "B", "C")


@dataclass(frozen=True)
class BalanceGate:
    max_share: float
    min_share: float
    max_deadlocks: float
    min_accusations: float = 0.0


def gate_for(setup: str, layer: str) -> BalanceGate:
    """Gates: C live-ready; B mid; A teach. Bounds allow ~80-game sampling noise."""
    n = len(SETUP_PRESETS[setup])
    if layer == "C":
        if n <= 3:
            return BalanceGate(0.52, 0.14, 0.5, min_accusations=1.0)
        if n == 4:
            return BalanceGate(0.50, 0.06, 0.5, min_accusations=1.0)
        return BalanceGate(0.48, 0.05, 0.5, min_accusations=1.2)
    if layer == "B":
        if n <= 3:
            return BalanceGate(0.55, 0.10, 0.5)
        return BalanceGate(0.52, 0.03, 0.5)
    # A teach
    if n <= 3:
        return BalanceGate(0.72, 0.05, 0.5)
    return BalanceGate(0.65, 0.0, 0.5)


def faction_shares(summary: BatchSummary) -> dict[str, float]:
    factions = [f.value for f in SETUP_PRESETS[summary.setup]]
    n = summary.games
    return {fid: summary.wins.get(fid, 0) / n for fid in factions}


def evaluate(summary: BatchSummary) -> tuple[bool, list[str]]:
    gate = gate_for(summary.setup, summary.layer)
    shares = faction_shares(summary)
    vals = list(shares.values())
    errors: list[str] = []
    mx, mn = max(vals), min(vals)
    if mx > gate.max_share:
        errors.append(f"max_share={mx:.2f}>{gate.max_share} wins={summary.wins}")
    if mn < gate.min_share:
        errors.append(f"min_share={mn:.2f}<{gate.min_share} wins={summary.wins}")
    if summary.deadlocks_avg > gate.max_deadlocks:
        errors.append(f"deadlocks={summary.deadlocks_avg:.2f}>{gate.max_deadlocks}")
    if summary.accusations_avg < gate.min_accusations:
        errors.append(
            f"accusations={summary.accusations_avg:.2f}<{gate.min_accusations}"
        )
    return not errors, errors


def run_matrix(
    *,
    games: int = 80,
    seed: int = 42,
    layers: tuple[str, ...] = LAYERS,
    setups: list[str] | None = None,
    threshold: int = 7,
) -> list[tuple[BatchSummary, bool, list[str]]]:
    names = setups or sorted(SETUP_PRESETS.keys())
    out: list[tuple[BatchSummary, bool, list[str]]] = []
    for setup in names:
        for layer in layers:
            summary = run_batch(
                games=games,
                setup=setup,
                seed=seed,
                layer=layer,
                threshold=threshold,
            )
            ok, errors = evaluate(summary)
            out.append((summary, ok, errors))
    return out
