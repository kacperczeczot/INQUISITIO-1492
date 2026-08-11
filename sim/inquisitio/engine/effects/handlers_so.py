"""Święte Oficjum card handlers."""

from __future__ import annotations

from inquisitio.engine.effects.registry import effect
from inquisitio.engine.state import GameState, PlayedCard
from inquisitio.model import Card, FactionId, LocationId


def _rival_high_heresy(state: GameState, owner: FactionId, min_h: int = 4):
    rivals = [f for f in state.rivals(owner) if state.player(f).heresy >= min_h]
    if not rivals:
        return None
    return max(rivals, key=lambda f: state.player(f).heresy)


@effect("so-01")
def proces_pokazowy(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    target = _rival_high_heresy(state, played.owner, 4)
    if target:
        for a in state.player(target).agents_on_board():
            a.in_dungeon = True
            a.location = None
            break
        if state.player(target).heresy >= 5:
            state.player(target).add_heresy(1)
        owner.influence_tribunal += 1


@effect("so-02")
def oblawa(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    for loc in (LocationId.RYNEK, LocationId.GILDIA):
        for rival in state.rivals(played.owner):
            agents = state.player(rival).agents_in(loc)
            if agents:
                agents[0].in_dungeon = True
                agents[0].location = None
                if state.player(rival).heresy >= 4:
                    owner.influence_tribunal += 1
                return


@effect("so-03")
def wymuszenie(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    owner.gold += 1
    for rival in state.rivals(played.owner):
        rp = state.player(rival)
        if rp.dungeon_agents():
            if rp.hand:
                rp.discard.append(rp.hand.pop())
            else:
                # target_heresy applied by registry
                state.era_modifiers[f"blame:{played.owner.value}"] = rival
            return


@effect("so-04")
def autodafe(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    for rival in state.rivals(played.owner):
        rp = state.player(rival)
        # dungeon + heresy >= threshold-1
        if rp.dungeon_agents() and rp.heresy >= max(4, state.threshold - 1):
            rp.dungeon_agents()[0].burned = True
            owner.stakes += 1
            state.metrics.stakes_total += 1
            state.metrics.verdicts += 1
            return
    # soft: jeśli ktoś w kryytcznej bez lochów — aresztuj i +presja
    target = _rival_high_heresy(state, played.owner, state.threshold)
    if target:
        rp = state.player(target)
        board = rp.agents_on_board()
        if board:
            board[0].in_dungeon = True
            board[0].location = None
        rp.add_heresy(1)


@effect("so-05")
def konfiskata(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    target = _rival_high_heresy(state, played.owner, 0) or (state.rivals(played.owner) or [None])[0]
    if not target:
        return
    rp = state.player(target)
    take = min(2, rp.gold)
    rp.gold -= take
    owner.gold += take
    if rp.heresy >= 4 and rp.relics > 0:
        rp.relics -= 1
        state.relics_on_board[LocationId.TRYBUNAL] += 1


@effect("so-06")
def edykt_czystosci(state: GameState, played: PlayedCard, card: Card) -> None:
    state.era_modifiers["extra_heresy_on_2plus"] = 1
    state.player(played.owner).influence_tribunal += 1


@effect("so-07")
def familiariusz(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    if owner.deck:
        owner.hand.append(owner.deck.pop(0))
    elif owner.discard:
        owner.deck = list(owner.discard)
        owner.discard.clear()
        import random

        random.Random(state.rng_seed + state.era).shuffle(owner.deck)
        if owner.deck:
            owner.hand.append(owner.deck.pop(0))
    agents = owner.living_agents()
    free = [a for a in agents if a.location is None and not a.in_dungeon and not a.burned]
    if free:
        free[0].location = LocationId.TRYBUNAL
    elif owner.agents_on_board():
        a = owner.agents_on_board()[0]
        # move toward tribunal/lochy
        a.location = LocationId.LOCHY if a.location != LocationId.LOCHY else LocationId.TRYBUNAL


@effect("so-08")
def swiadek_koronny(state: GameState, played: PlayedCard, card: Card) -> None:
    # reaction: blame handled via target_heresy; mark process win
    state.era_modifiers["oficjum_wins_bid"] = True
    target = _rival_high_heresy(state, played.owner, 0)
    if target:
        state.era_modifiers[f"blame:{played.owner.value}"] = target


@effect("so-09")
def relikwiarz(state: GameState, played: PlayedCard, card: Card) -> None:
    # move any board relic to tribunal
    for loc, n in list(state.relics_on_board.items()):
        if n > 0 and loc != LocationId.TRYBUNAL:
            state.relics_on_board[loc] -= 1
            state.relics_on_board[LocationId.TRYBUNAL] += 1
            return
    for rival in state.rivals(played.owner):
        rp = state.player(rival)
        if rp.relics > 0:
            rp.relics -= 1
            state.relics_on_board[LocationId.TRYBUNAL] += 1
            rp.add_heresy(1)
            return


@effect("so-10")
def oczysc_miasto(state: GameState, played: PlayedCard, card: Card) -> None:
    loc = played.location
    for rival in state.rivals(played.owner):
        if state.player(rival).heresy < 4:
            continue
        for a in list(state.player(rival).agents_in(loc)):
            a.in_dungeon = True
            a.location = None
    # if >=2 dungeon agents among rivals, mark auto-process candidate
    dungeon_rivals = [
        f for f in state.rivals(played.owner) if state.player(f).dungeon_agents()
    ]
    if len(dungeon_rivals) >= 1:
        worst = max(dungeon_rivals, key=lambda f: state.player(f).heresy)
        state.era_modifiers["pending_process"] = worst
