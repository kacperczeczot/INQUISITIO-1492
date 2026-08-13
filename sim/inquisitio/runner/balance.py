"""Balance gates — shared criteria for matrix tests and CLI."""
from __future__ import annotations

from dataclasses import dataclass

from inquisitio.engine.setup import SETUP_PRESETS
from inquisitio.runner.batch import BatchSummary, run_batch

LAYERS = ("A", "B", "C")


@dataclass(frozen=True)
class BalanceGate:
    # Cel Ścisły (Target Band)
    target_max: float
    target_min: float
    # Zakres Krytyczny (Red Line Boundary)
    critical_max: float
    critical_min: float
    max_deadlocks: float = 0.5
    min_accusations: float = 1.0

    @property
    def max_share(self) -> float:
        return self.critical_max

    @property
    def min_share(self) -> float:
        return self.critical_min


def gate_for(setup: str, layer: str) -> BalanceGate:
    """Gates: C live-ready; B mid; A teach. Strict evaluation of Red Line critical bounds."""
    n = len(SETUP_PRESETS[setup])
    if layer == "C":
        if n <= 3:
            return BalanceGate(
                target_max=0.38, target_min=0.28,
                critical_max=0.45, critical_min=0.20,
                max_deadlocks=0.5, min_accusations=1.0
            )
        if n == 4:
            return BalanceGate(
                target_max=0.30, target_min=0.20,
                critical_max=0.35, critical_min=0.15,
                max_deadlocks=0.5, min_accusations=1.0
            )
        return BalanceGate(
            target_max=0.24, target_min=0.16,
            critical_max=0.30, critical_min=0.10,
            max_deadlocks=0.5, min_accusations=1.2
        )
    if layer == "B":
        if n <= 3:
            return BalanceGate(
                target_max=0.40, target_min=0.25,
                critical_max=0.48, critical_min=0.15,
                max_deadlocks=0.5, min_accusations=0.0
            )
        if n == 4:
            return BalanceGate(
                target_max=0.32, target_min=0.18,
                critical_max=0.40, critical_min=0.10,
                max_deadlocks=0.5, min_accusations=0.0
            )
        return BalanceGate(
            target_max=0.26, target_min=0.14,
            critical_max=0.32, critical_min=0.08,
            max_deadlocks=0.5, min_accusations=0.0
        )
    # A teach
    if n <= 3:
        return BalanceGate(
            target_max=0.45, target_min=0.20,
            critical_max=0.55, critical_min=0.10,
            max_deadlocks=0.5, min_accusations=0.0
        )
    return BalanceGate(
        target_max=0.35, target_min=0.12,
        critical_max=0.45, critical_min=0.05,
        max_deadlocks=0.5, min_accusations=0.0
    )


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

    # Red line checks (Critical Failure)
    if mx > gate.critical_max:
        errors.append(f"CRITICAL OVERPOWER: max_share={mx:.2f}>{gate.critical_max} wins={summary.wins}")
    if mn < gate.critical_min:
        errors.append(f"CRITICAL UNDERPOWER: min_share={mn:.2f}<{gate.critical_min} wins={summary.wins}")

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
