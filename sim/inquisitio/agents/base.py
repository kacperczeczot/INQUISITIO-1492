"""Agent interface."""
from __future__ import annotations

import random
from typing import Protocol

from inquisitio.engine.state import FactionId, GameState


class Agent(Protocol):
    def choose_card(self, state: GameState, faction: FactionId, legal: list[str]) -> str | None:
        ...


class RandomAgent:
    def __init__(self, rng: random.Random):
        self.rng = rng

    def choose_card(self, state: GameState, faction: FactionId, legal: list[str]) -> str | None:
        if not legal:
            return None
        return self.rng.choice(legal)
