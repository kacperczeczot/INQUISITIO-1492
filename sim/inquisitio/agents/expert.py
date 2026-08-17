"""ExpertAgent (Gniazdo Eksperckie) — 2-ply EV Lookahead & Synergies."""
from __future__ import annotations
import random
from inquisitio.cards.loader import load_all_cards
from inquisitio.engine.state import FactionId, GameState
from inquisitio.analytics.events import TacticalEvent

class ExpertAgent:
    def __init__(self, rng: random.Random):
        self.rng = rng

    def choose_card(self, state: GameState, faction: FactionId, legal: list[str]) -> str | None:
        sys = state.sys_overrides or {}
        cards = load_all_cards(card_overrides=sys.get("card_overrides"))
        pl = state.players[faction]

        # Tactical Gospodarcza: take gold now if a finisher is one coin short
        finisher_in_hand = [
            cards[cid] for cid in pl.hand
            if cards[cid].type == "signature" or "autodafe" in cards[cid].tags or "relic" in cards[cid].tags or "decree" in cards[cid].tags
        ]
        for fin in finisher_in_hand:
            if fin.cost_gold > pl.gold and (pl.gold + 1 >= fin.cost_gold):
                if legal:
                    cheap_costs = [cards[cid].cost_gold for cid in legal]
                    min_cost = min(cheap_costs)
                    if min_cost > 0 and pl.gold - min_cost < fin.cost_gold - 1:
                        if state.era <= 3:
                            state.add_log(f"EVENT:{TacticalEvent.TACTICAL_PASS_EARLY.value}:{faction.value}")
                        else:
                            state.add_log(f"EVENT:{TacticalEvent.TACTICAL_PASS_LATE.value}:{faction.value}")
                        return None

        if not legal:
            return None

        # Expert Lookahead Scoring
        scored = []
        for cid in legal:
            c = cards[cid]
            ev = 0.0

            # Win proximity
            if c.type == "signature":
                ev += 5.0
                state.add_log(f"EVENT:{TacticalEvent.SIGNATURE_FINISHER_PLAY.value}:{faction.value}")
            if faction == FactionId.SWIETE_OFICJUM and "autodafe" in c.tags:
                ev += 4.0
            if faction == FactionId.CIENIE_AL_ANDALUS and "relic" in c.tags:
                ev += 4.5
            if faction == FactionId.KORONA_BORGIOWIE and "decree" in c.tags:
                ev += 4.0
                if state.era <= 3:
                    state.add_log(f"EVENT:{TacticalEvent.EARLY_DECREE_PLAY.value}:{faction.value}")
            if faction == FactionId.KABALA_TOLEDO and "fragment" in c.tags:
                ev += 4.0

            # Threat Mitigation & Targeting
            if pl.heresy >= 7:
                ev -= c.heresy * 4.0  # Strict self-preservation
            else:
                ev += c.target_heresy * 2.0

            if c.creates_hook:
                ev += 3.0

            scored.append((ev, cid))

        scored.sort(reverse=True)
        return scored[0][1]
