from __future__ import annotations

from inquisitio.agents.base import IntrigueAgent
from inquisitio.engine.state import GameState
from inquisitio.model import FactionId


class OficjumAgent(IntrigueAgent):
    feint_bias = 0.1

    def era_intent(self, state: GameState) -> str:
        return "hunt_critical_for_stakes"

    def faction_card_bias(self, state: GameState, card_id: str) -> float:
        tags = set(state.cards[card_id].tags)
        bonus = 0.0
        if "proces" in tags or "oblawa" in tags or "stos" in tags:
            bonus += 1.4
        critical = any(state.player(f).heresy >= state.threshold - 1 for f in state.rivals(self.faction))
        if critical and ("proces" in tags or card_id in ("so-04", "so-10", "so-01", "so-02")):
            bonus += 2.0
        # buduj Wpływ → Stosy
        if card_id in ("so-01", "so-06", "so-05", "so-02"):
            bonus += 0.8
        return bonus

    def accuse_threshold(self) -> float:
        return 0.2  # eager to accuse


class AlAndalusAgent(IntrigueAgent):
    feint_bias = 0.35  # blef świadomy; mniej czystego RNG

    def era_intent(self, state: GameState) -> str:
        p = state.player(self.faction)
        if p.relics > 0 or state.sea_route_open:
            return "evacuate_relic"
        return "acquire_and_feint_transport"

    def faction_card_bias(self, state: GameState, card_id: str) -> float:
        tags = set(state.cards[card_id].tags)
        bonus = 0.0
        if "relikwia" in tags or "ewakuacja" in tags or "stealth" in tags:
            bonus += 1.3
        p = state.player(self.faction)
        if p.heresy >= 5 and state.cards[card_id].heresy == 0:
            bonus += 0.8
        if card_id in ("caa-06", "caa-08", "caa-05"):
            bonus += 1.0
        return bonus


class KoronaAgent(IntrigueAgent):
    feint_bias = 0.15

    def era_intent(self, state: GameState) -> str:
        p = state.player(self.faction)
        if p.control_palace < 2:
            return "secure_palace"
        if p.control_market < 2:
            return "secure_market"
        return "defend_monopoly"

    def faction_card_bias(self, state: GameState, card_id: str) -> float:
        tags = set(state.cards[card_id].tags)
        bonus = 0.0
        p = state.player(self.faction)
        if "kontrola" in tags or "dekret" in tags:
            bonus += 0.9
        if "zloto" in tags:
            bonus += 0.4
        # nie faworyzuj signature instant-win tak mocno
        if card_id == "kb-10":
            bonus += 0.5 if p.control_palace >= 1 and p.control_market >= 1 else 0.2
        if card_id in ("kb-01", "kb-07", "kb-05") and (
            (p.control_palace < 2) or (p.control_market < 2)
        ):
            bonus += 1.0
        return bonus


class KabalaAgent(IntrigueAgent):
    feint_bias = 0.3

    def era_intent(self, state: GameState) -> str:
        p = state.player(self.faction)
        if p.heresy < 4:
            return "enter_observed_zone"
        if p.heresy > 6:
            return "dump_heresy_and_survive"
        return "farm_clues_in_sweet_spot"

    def faction_card_bias(self, state: GameState, card_id: str) -> float:
        tags = set(state.cards[card_id].tags)
        bonus = 0.0
        if "wskazowka" in tags or "kodeks" in tags or "alchemia" in tags:
            bonus += 1.3
        p = state.player(self.faction)
        if p.heresy >= 6 and state.cards[card_id].target_heresy > 0:
            bonus += 1.5  # dump blame
        if p.heresy <= 3 and state.cards[card_id].heresy >= 1:
            bonus += 0.6
        return bonus


class GildiaAgent(IntrigueAgent):
    feint_bias = 0.35

    def era_intent(self, state: GameState) -> str:
        return "frame_rivals_for_collapse"

    def faction_card_bias(self, state: GameState, card_id: str) -> float:
        tags = set(state.cards[card_id].tags)
        bonus = 0.0
        if "wrabianie" in tags or "szantaz" in tags or "upadek" in tags:
            bonus += 1.5
        if state.cards[card_id].target_heresy > 0:
            bonus += 0.7 * state.cards[card_id].target_heresy
        return bonus

    def accuse_threshold(self) -> float:
        return 0.25


AGENT_MAP = {
    FactionId.SWIETE_OFICJUM: OficjumAgent,
    FactionId.CIENIE_AL_ANDALUS: AlAndalusAgent,
    FactionId.KORONA_BORGIOWIE: KoronaAgent,
    FactionId.KABALA_TOLEDO: KabalaAgent,
    FactionId.GILDIA_CIENI: GildiaAgent,
}
