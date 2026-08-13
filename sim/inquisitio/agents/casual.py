"""CasualAgent (Nowicjusz / Gracz Początkujący) — Zachłanny, brak planowania oszczędności."""
from __future__ import annotations
import random
from inquisitio.cards.loader import load_all_cards
from inquisitio.engine.state import FactionId, GameState

class CasualAgent:
    def __init__(self, rng: random.Random):
        self.rng = rng

    def choose_card(self, state: GameState, faction: FactionId, legal: list[str]) -> str | None:
        if not legal:
            return None
        cards = load_all_cards()
        pl = state.players[faction]

        # Greedy choice: pick card with highest immediate raw stats, spend gold immediately
        scored = []
        for cid in legal:
            c = cards[cid]
            score = 0.0
            score += c.gold * 1.5
            score += c.agents * 1.2
            score += c.target_heresy * 1.0
            # Casual fears heresy too much
            if c.heresy > 0:
                score -= c.heresy * 2.5
            scored.append((score, cid))

        scored.sort(reverse=True)
        return scored[0][1]
