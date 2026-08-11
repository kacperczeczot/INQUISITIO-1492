"""Politics agent — fear Critical / Inquisitor, value Hooks."""
from __future__ import annotations

import random

from inquisitio.cards.loader import load_all_cards
from inquisitio.engine.state import FactionId, GameState


class PoliticsAgent:
    def __init__(self, rng: random.Random):
        self.rng = rng

    def choose_card(self, state: GameState, faction: FactionId, legal: list[str]) -> str | None:
        if not legal:
            return None
        cards = load_all_cards()
        pl = state.players[faction]
        scored: list[tuple[float, str]] = []
        for cid in legal:
            c = cards[cid]
            score = 0.0
            # fear critical: avoid self heresy when high
            if pl.heresy >= 6:
                score -= c.heresy * 3
            else:
                score += c.heresy * 0.2  # power edge
            score += c.target_heresy * 1.5
            score += c.gold * 0.8
            score += c.agents * 0.5
            if c.creates_hook:
                score += 2.0
            if c.arrest:
                score += 1.5
            if "interrogation" in c.tags:
                score += 1.8
            if c.type == "signature":
                score += 3.0
            # Oficjum likes stacks path
            if faction == FactionId.SWIETE_OFICJUM and "autodafe" in c.tags:
                score += 2.5
            if faction == FactionId.CIENIE_AL_ANDALUS and "relic" in c.tags:
                score += 2.5
            if faction == FactionId.KORONA_BORGIOWIE and "decree" in c.tags:
                score += 3.0
            if faction == FactionId.KABALA_TOLEDO and "fragment" in c.tags:
                score += 2.5
            if faction == FactionId.GILDIA_CIENI and "fall" in c.tags:
                score += 2.5
            # avoid inquisitor tile overcrowding via move when heresy high
            if pl.heresy >= 5 and c.agents:
                score += 0.5
            score += self.rng.random() * 0.3
            scored.append((score, cid))
        scored.sort(reverse=True)
        return scored[0][1]
