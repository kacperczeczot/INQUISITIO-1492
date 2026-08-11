"""Heresy track helpers."""
from __future__ import annotations

from inquisitio.engine.state import FactionId, GameState, PlayerState, clamp_heresy, heresy_zone


def add_heresy(state: GameState, faction: FactionId, amount: int, reason: str = "") -> None:
    if amount == 0:
        return
    p = state.players[faction]
    before = p.heresy
    p.heresy = clamp_heresy(p.heresy + amount)
    state.add_log(
        f"{faction.value} heresy {before}->{p.heresy} ({heresy_zone(p.heresy)})"
        + (f" [{reason}]" if reason else "")
    )


def is_critical(player: PlayerState, threshold: int = 7) -> bool:
    return player.heresy >= threshold
