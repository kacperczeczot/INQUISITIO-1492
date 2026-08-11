from __future__ import annotations

import random
from typing import TYPE_CHECKING

from inquisitio.engine.effects.registry import apply_card_effect
from inquisitio.engine.process import run_process
from inquisitio.engine.state import PlayedCard
from inquisitio.engine.win import check_winner, end_game_by_eras
from inquisitio.model import LOCATION_ORDER, CardType, FactionId, LocationId

if TYPE_CHECKING:
    from inquisitio.agents.base import IntrigueAgent
    from inquisitio.engine.state import GameState


def _draw_to(state: GameState, faction: FactionId, hand_limit: int = 5) -> None:
    p = state.player(faction)
    rng = random.Random(state.rng_seed + state.era + hash(faction.value) % 997)
    while len(p.hand) < hand_limit:
        if not p.deck:
            if not p.discard:
                break
            p.deck = list(p.discard)
            p.discard.clear()
            rng.shuffle(p.deck)
        if p.deck:
            p.hand.append(p.deck.pop(0))


def _pay_cost(state: GameState, faction: FactionId, cost: int) -> bool:
    p = state.player(faction)
    rebate = int(state.era_modifiers.get(f"cost_rebate:{faction.value}", 0))
    cost = max(0, cost - rebate)
    if p.gold < cost:
        return False
    p.gold -= cost
    return True


def phase_i_time(state: GameState, agents: dict[FactionId, IntrigueAgent] | None = None) -> None:
    """Skill > luck: odkryj 2, wybiera gracz z najniższym postępem Intrygi."""
    from inquisitio.agents.politics import intrigue_progress

    if not state.time_deck:
        state.time_deck = list(state.time_discard)
        state.time_discard.clear()
        # Przetasuj deterministycznie (seed), nie „świeży chaos”
        random.Random(state.rng_seed + 1000 + state.era).shuffle(state.time_deck)
    if not state.time_deck:
        return

    options: list[str] = []
    while len(options) < 2 and state.time_deck:
        options.append(state.time_deck.pop(0))
    if not options:
        return

    # Chooser: najniższy postęp (dogrywka) — świadoma decyzja polityczna
    chooser = min(state.order, key=lambda f: (intrigue_progress(state, f), state.order.index(f)))
    chosen = options[0]
    if len(options) == 2 and agents and chooser in agents:
        chosen = agents[chooser].choose_time_event(state, options)
    elif len(options) == 2:
        # fallback bez agentów: preferuj Flotę jeśli ktoś ma Relikwie
        has_relics = any(state.player(f).relics > 0 for f in state.order)
        if has_relics and "time-03" in options:
            chosen = "time-03"
        else:
            chosen = options[0]

    for cid in options:
        if cid != chosen:
            # odrzucona na spód talii (wraca później — mniej swing)
            state.time_deck.append(cid)

    state.current_time = chosen
    state.time_discard.append(chosen)
    card = state.cards[chosen]
    played = PlayedCard(card_id=chosen, owner=chooser, location=LocationId.TRYBUNAL, face_down=False)
    apply_card_effect(state, played, card)
    state.metrics.log(
        event="time_choice",
        era=state.era,
        chooser=chooser.value,
        chosen=chosen,
        options=options,
    )


def phase_ii_planning(state: GameState, agents: dict[FactionId, IntrigueAgent]) -> None:
    cards_per = 3 if len(state.order) == 2 else 2
    order = state.turn_order()
    # Round-robin plays
    for _ in range(cards_per):
        for faction in order:
            if state.winner:
                return
            agent = agents[faction]
            decision = agent.choose_play(state)
            if not decision:
                continue
            p = state.player(faction)
            if decision.card_id not in p.hand:
                continue
            card = state.cards[decision.card_id]
            if not _pay_cost(state, faction, card.cost):
                # try next best: skip
                continue
            p.hand.remove(decision.card_id)
            p.cards_played_this_era += 1
            state.metrics.plays += 1
            if decision.feint:
                state.metrics.feints += 1
            if decision.blame_target:
                state.era_modifiers[f"blame:{faction.value}"] = decision.blame_target

            if card.type == CardType.PERMANENT:
                played = PlayedCard(decision.card_id, faction, decision.location, face_down=False)
                apply_card_effect(state, played, card)
                p.discard.append(decision.card_id)
            else:
                state.slots[decision.location].append(
                    PlayedCard(decision.card_id, faction, decision.location, face_down=True)
                )
                # shadow play tracking
                if card.heresy > 0 or "cien" in card.tags or card.location != LocationId.ANY:
                    p.played_shadow_locs.add(decision.location)

            if decision.move_agent and decision.agent_dest and p.agents_on_board():
                a = p.agents_on_board()[0]
                a.location = decision.agent_dest

            state.metrics.log(
                event="play",
                era=state.era,
                faction=faction.value,
                card=decision.card_id,
                location=decision.location.value,
                intent=decision.intent,
                feint=decision.feint,
                blame=decision.blame_target.value if decision.blame_target else None,
            )


def phase_iii_reveal(state: GameState, agents: dict[FactionId, IntrigueAgent]) -> None:
    order = state.turn_order()
    for loc in LOCATION_ORDER:
        plays = list(state.slots[loc])
        # sort by turn order
        plays.sort(key=lambda pc: order.index(pc.owner) if pc.owner in order else 99)
        for played in plays:
            played.face_down = False
            card = state.cards[played.card_id]
            # Agent requirement soft-check: if needs agents and none, still resolve with penalty
            owner = state.player(played.owner)
            if card.agents > 0 and not owner.agents_in(loc) and not owner.agents_on_board():
                owner.add_heresy(1)
            apply_card_effect(state, played, card)
            for ag in agents.values():
                ag.observe_reveal(state, played.owner, loc, played.card_id)
            owner.discard.append(played.card_id)
            if check_winner(state):
                return
        # market end heresy from time-07
        if state.era_modifiers.get("market_agent_heresy") and loc == LocationId.RYNEK:
            for faction in state.order:
                if state.player(faction).agents_in(LocationId.RYNEK):
                    state.player(faction).add_heresy(1)
    for loc in LOCATION_ORDER:
        state.slots[loc].clear()


def phase_iv_court(state: GameState, agents: dict[FactionId, IntrigueAgent]) -> None:
    from inquisitio.agents.politics import intrigue_progress

    # Public scrutiny: lider wyścigu Intrygi dostaje +1 Herezji (napięcie stołu)
    if state.order:
        leader = max(state.order, key=lambda f: intrigue_progress(state, f))
        if intrigue_progress(state, leader) >= 0.35:
            before = state.player(leader).heresy
            state.player(leader).add_heresy(1)
            if state.player(leader).heresy >= state.threshold > before:
                state.metrics.critical_entries += 1
            state.metrics.log(event="scrutiny", era=state.era, faction=leader.value)

    # Sync temporary alliances from card era mods
    for faction in state.order:
        ally = state.era_modifiers.get(f"ally:{faction.value}")
        if ally:
            if isinstance(ally, str):
                ally = FactionId(ally)
            agents[faction].politics.set_ally(faction, ally)

    # Pending process from cards
    pending = state.era_modifiers.get("pending_process")
    if pending:
        if isinstance(pending, str):
            pending = FactionId(pending)
        accuser = FactionId.GILDIA_CIENI if FactionId.GILDIA_CIENI in state.players else state.order[0]
        strategic = bool(state.era_modifiers.get("pending_strategic"))
        if state.player(pending).heresy >= state.threshold:
            run_process(state, pending, accuser, strategic=strategic)
            if check_winner(state):
                return

    # Accusations — each player once
    accused_set: set[FactionId] = set()
    for faction in state.turn_order():
        if state.winner:
            return
        decision = agents[faction].choose_accusation(state)
        if not decision.accuse or not decision.target:
            continue
        if decision.target in accused_set:
            continue
        if state.player(decision.target).heresy < state.threshold:
            continue
        # alliance block
        ally = agents[faction].politics.alliances.get(faction)
        if ally and ally == decision.target:
            continue
        run_process(state, decision.target, faction, strategic=decision.strategic)
        accused_set.add(decision.target)
        state.metrics.log(
            event="accuse_decision",
            era=state.era,
            faction=faction.value,
            target=decision.target.value,
            reason=decision.reason,
            strategic=decision.strategic,
        )
        if check_winner(state):
            return

    # Free dungeon costs 3 gold
    for faction in state.order:
        p = state.player(faction)
        if p.dungeon_agents() and p.gold >= 3 and not state.era_modifiers.get(f"extra_jail:{faction.value}"):
            # shield blocks free escape? if shield, still pay
            if state.era_modifiers.get(f"shield:{faction.value}"):
                continue
            p.gold -= 3
            a = p.dungeon_agents()[0]
            a.in_dungeon = False
            a.location = LocationId.GILDIA

    # Passive income
    for faction in state.order:
        p = state.player(faction)
        if p.agents_in(LocationId.PALAC) and LocationId.PALAC not in p.played_shadow_locs:
            p.gold += 1
        if p.agents_in(LocationId.RYNEK) and LocationId.RYNEK not in p.played_shadow_locs:
            p.gold += 1 + int(state.era_modifiers.get("market_trade_bonus", 0))

    # Lista dłużników permanent upkeep
    if FactionId.GILDIA_CIENI in state.players:
        g = state.player(FactionId.GILDIA_CIENI)
        if "gc-08" in g.permanents:
            for rival in state.rivals(FactionId.GILDIA_CIENI):
                rp = state.player(rival)
                if rp.heresy >= 4:
                    if rp.gold > 0:
                        rp.gold -= 1
                        g.gold += 1
                    else:
                        rp.add_heresy(1)

    for faction in state.order:
        _draw_to(state, faction, 5)

    for ag in agents.values():
        ag.end_era()

    state.first_player_idx = (state.first_player_idx + 1) % len(state.order)
    # reset era flags on players
    for p in state.players.values():
        p.accused_this_era = False
        p.played_shadow_locs.clear()
        p.cards_played_this_era = 0
    state.era_modifiers.clear()
    state.current_time = None


def play_era(state: GameState, agents: dict[FactionId, IntrigueAgent]) -> None:
    state.era += 1
    phase_i_time(state, agents)
    if check_winner(state):
        return
    phase_ii_planning(state, agents)
    if check_winner(state):
        return
    phase_iii_reveal(state, agents)
    if check_winner(state):
        return
    phase_iv_court(state, agents)


def play_game(state: GameState, agents: dict[FactionId, IntrigueAgent] | None = None) -> GameState:
    from inquisitio.agents.base import make_agent

    if agents is None:
        agents = {f: make_agent(f, seed=state.rng_seed) for f in state.order}
    while state.era < state.max_eras and state.winner is None:
        play_era(state, agents)
        if check_winner(state):
            break
    if state.winner is None:
        end_game_by_eras(state)
    return state
