from __future__ import annotations

import os
import random
from abc import ABC, abstractmethod

from inquisitio.agents.bluff import choose_location, true_intent_location
from inquisitio.agents.politics import (
    AccuseDecision,
    BeliefState,
    PlayDecision,
    PoliticsState,
    build_threat_map,
    intrigue_progress,
)
from inquisitio.engine.state import GameState
from inquisitio.llm.adapter import LLMAdapter, get_adapter
from inquisitio.model import LOCATION_ORDER, CardType, FactionId, LocationId, NEIGHBORS


class IntrigueAgent(ABC):
    faction: FactionId
    feint_bias: float = 0.25

    def __init__(self, faction: FactionId, seed: int = 0) -> None:
        self.faction = faction
        self.rng = random.Random(seed + hash(faction.value) % 10000)
        self.belief = BeliefState()
        self.politics = PoliticsState()
        self.llm: LLMAdapter = get_adapter()

    @abstractmethod
    def era_intent(self, state: GameState) -> str:
        ...

    def score_card(self, state: GameState, card_id: str) -> float:
        card = state.cards[card_id]
        p = state.player(self.faction)
        score = 1.0
        # Prefer affordable
        if card.cost > p.gold:
            score -= 2.0
        # Unikaj tylko twardego wejścia w Krytyczną; mid-heresy jest OK (intryga)
        projected = p.heresy + card.heresy
        if projected >= state.threshold and card.heresy > 0:
            score -= 0.9
        elif projected >= state.threshold - 1 and card.heresy >= 2:
            score -= 0.35
        if card.target_heresy > 0:
            score += 1.1 * card.target_heresy
            # bonus vs race leader
            rivals = state.rivals(self.faction)
            if rivals:
                leader = max(rivals, key=lambda f: intrigue_progress(state, f))
                if intrigue_progress(state, leader) >= 0.35:
                    score += 0.6
        if card.type == CardType.REAKCJA:
            score -= 0.3  # keep for later unless nothing else
        return score + self.faction_card_bias(state, card_id)

    def faction_card_bias(self, state: GameState, card_id: str) -> float:
        return 0.0

    def choose_play(self, state: GameState) -> PlayDecision | None:
        # Skill: Al-Andalus może otworzyć Szlak za złoto zamiast czekać na Flotę
        if self.faction == FactionId.CIENIE_AL_ANDALUS and not state.sea_route_open:
            p = state.player(self.faction)
            if p.relics > 0 and p.gold >= 3 and (
                p.agents_in(LocationId.RYNEK) or p.agents_in(LocationId.GILDIA)
            ):
                p.gold -= 3
                state.sea_route_open = True
                state.metrics.log(event="open_sea_route", faction=self.faction.value, era=state.era)

        p = state.player(self.faction)
        actions = [cid for cid in p.hand if state.cards[cid].type in (CardType.AKCJA, CardType.PERMANENT)]
        pool = actions or list(p.hand)
        if not pool:
            return None
        scored = sorted(pool, key=lambda c: self.score_card(state, c), reverse=True)
        card_id = scored[0]
        # Mniej losu: exploration 5% (było 15%)
        if len(scored) > 1 and self.rng.random() < 0.05:
            card_id = scored[1]
        card = state.cards[card_id]
        intent = self.era_intent(state)
        true_loc = true_intent_location(self.faction, state, card.location)
        loc, feint = choose_location(
            faction=self.faction,
            true_intent_loc=true_loc,
            belief=self.belief,
            rivals=state.rivals(self.faction),
            rng=self.rng,
            feint_bias=self.feint_bias,
        )
        llm_choice = self.llm.maybe_choose_location(state, self.faction, true_loc, intent)
        if llm_choice is not None:
            loc, feint = llm_choice, llm_choice != true_loc

        blame = None
        if card.target_heresy > 0:
            threats = build_threat_map(state, self.faction)
            ally = self.politics.alliances.get(self.faction)
            candidates = [f for f in state.rivals(self.faction) if f != ally]
            if candidates:
                blame = max(candidates, key=lambda f: threats.get(f, 0) + state.player(f).heresy * 0.1)

        agent_dest = None
        move = False
        if p.agents_on_board():
            move = True
            cur = p.agents_on_board()[0]
            if cur.location == loc:
                agent_dest = loc
            elif cur.location and loc in NEIGHBORS.get(cur.location, []):
                agent_dest = loc
            elif cur.location and NEIGHBORS.get(cur.location):
                agent_dest = NEIGHBORS[cur.location][0]
            else:
                agent_dest = loc

        return PlayDecision(
            card_id=card_id,
            location=loc,
            move_agent=move,
            agent_dest=agent_dest,
            intent=intent,
            feint=feint,
            blame_target=blame,
        )

    def choose_time_event(self, state: GameState, options: list[str]) -> str:
        """Wybór wydarzenia: maksymalizuj własny EV, minimalizuj lidera rywala."""
        from inquisitio.agents.politics import intrigue_progress

        def score_event(card_id: str) -> float:
            tags = set(state.cards[card_id].tags)
            s = 0.0
            my = intrigue_progress(state, self.faction)
            rivals = state.rivals(self.faction)
            leader = max(rivals, key=lambda f: intrigue_progress(state, f)) if rivals else None
            if card_id == "time-03":  # Flota
                if self.faction == FactionId.CIENIE_AL_ANDALUS:
                    s += 3.0 + state.player(self.faction).relics
                elif leader == FactionId.CIENIE_AL_ANDALUS:
                    s -= 2.0
                else:
                    s += 0.2
            if card_id == "time-05":  # Auto de Fe — pomaga Oficjum / szkodzi Krytycznym
                if self.faction == FactionId.SWIETE_OFICJUM:
                    s += 2.5
                if state.player(self.faction).heresy >= state.threshold:
                    s -= 2.0
                elif leader and state.player(leader).heresy >= 4:
                    s += 1.0
            if card_id == "time-02":  # Edykt — herezja globalna
                if self.faction == FactionId.GILDIA_CIENI:
                    s += 1.5
                if self.faction == FactionId.KABALA_TOLEDO and state.player(self.faction).zone() == "czysta":
                    s += 1.0
                if state.player(self.faction).heresy >= 6:
                    s -= 1.5
            if card_id == "time-06":  # Spisek — reset Pałacu
                if self.faction == FactionId.KORONA_BORGIOWIE and state.player(self.faction).control_palace >= 2:
                    s -= 2.5
                elif leader == FactionId.KORONA_BORGIOWIE:
                    s += 2.0
                elif self.faction == FactionId.KORONA_BORGIOWIE:
                    s += 0.5
            if "relikwia" in tags or card_id in ("time-01", "time-04", "time-08"):
                if self.faction == FactionId.CIENIE_AL_ANDALUS:
                    s += 1.2
                if self.faction == FactionId.KABALA_TOLEDO:
                    s += 0.8
            if my < 0.25:
                s += 0.3  # dogrywający bierze ryzyko
            return s

        return max(options, key=score_event)

    def choose_accusation(self, state: GameState) -> AccuseDecision:
        p = state.player(self.faction)
        if p.accused_this_era and not state.era_modifiers.get("free_accuse"):
            # already used? per rules once per player per era as accuser — track separately
            pass
        critical = [
            f
            for f in state.rivals(self.faction)
            if state.player(f).heresy >= state.threshold and not state.player(f).accused_this_era
        ]
        if not critical:
            return AccuseDecision(False)
        ally = self.politics.alliances.get(self.faction)
        era_ally = state.era_modifiers.get(f"ally:{self.faction.value}")
        if era_ally:
            ally = FactionId(era_ally) if isinstance(era_ally, str) else era_ally
        critical = [f for f in critical if f != ally]
        if not critical:
            return AccuseDecision(False)

        threats = build_threat_map(state, self.faction)
        target = max(critical, key=lambda f: threats.get(f, 0))
        my_prog = intrigue_progress(state, self.faction)
        their = threats[target]
        strategic = their >= 0.4 or state.player(target).heresy >= state.threshold + 1
        # Oficjum / Gildia: extra push to accuse
        role = 0.25 if self.faction in (FactionId.SWIETE_OFICJUM, FactionId.GILDIA_CIENI) else 0.0
        base = their + (0.45 if strategic else 0.1) + role - 0.1 * my_prog

        llm = self.llm.maybe_accuse(state, self.faction, target, base)
        if llm is not None:
            return AccuseDecision(llm, target if llm else None, strategic, "llm")

        if base < self.accuse_threshold():
            return AccuseDecision(False, reason="ev_low")
        return AccuseDecision(True, target, strategic, "threat_ev")

    def accuse_threshold(self) -> float:
        return 0.28

    def observe_reveal(self, state: GameState, faction: FactionId, location: LocationId, card_id: str) -> None:
        self.belief.observe_play(faction, location, card_id)

    def end_era(self) -> None:
        self.politics.decay()


def make_agent(faction: FactionId, seed: int = 0) -> IntrigueAgent:
    from inquisitio.agents.factions import AGENT_MAP

    cls = AGENT_MAP[faction]
    return cls(faction, seed=seed)
