"""Cienie Al-Andalus handlers."""

from __future__ import annotations

from inquisitio.engine.effects.registry import effect
from inquisitio.engine.state import GameState, PlayedCard
from inquisitio.model import Card, LocationId


@effect("caa-01")
def zamach(state: GameState, played: PlayedCard, card: Card) -> None:
    for rival in state.rivals(played.owner):
        agents = state.player(rival).agents_in(played.location)
        if agents:
            agents[0].burned = True
            break
    if state.relics_on_board.get(played.location, 0) > 0:
        state.relics_on_board[played.location] -= 1
        state.player(played.owner).relics += 1


@effect("caa-02")
def przejscie(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    for a in owner.dungeon_agents() + owner.agents_in(LocationId.LOCHY):
        a.in_dungeon = False
        a.location = LocationId.GILDIA
        # transport Relikwii tylko jeśli już w Lochach na planszy (nie auto-loot)
        if state.relics_on_board.get(LocationId.LOCHY, 0) > 0 and owner.agents_in(LocationId.LOCHY):
            pass  # agent was in lochy
        if state.relics_on_board.get(LocationId.LOCHY, 0) > 0:
            state.relics_on_board[LocationId.LOCHY] -= 1
            owner.relics += 1
        return
    if owner.agents_on_board():
        owner.agents_on_board()[0].location = LocationId.GILDIA


@effect("caa-03")
def falszywy_trop(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    if owner.agents_on_board():
        a = owner.agents_on_board()[0]
        from inquisitio.model import NEIGHBORS

        if a.location and NEIGHBORS.get(a.location):
            a.location = NEIGHBORS[a.location][0]
    rivals = state.rivals(played.owner)
    if rivals:
        state.era_modifiers[f"blame:{played.owner.value}"] = rivals[0]


@effect("caa-04")
def przysiega(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    for _ in range(2):
        if owner.deck:
            owner.hand.append(owner.deck.pop(0))
    if len(owner.hand) > 5:
        owner.discard.append(owner.hand.pop())
    owner.add_heresy(-1)


@effect("caa-05")
def kurier(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    # tylko z planszy — nie z puli (balans)
    if state.relics_on_board.get(played.location, 0) > 0:
        state.relics_on_board[played.location] -= 1
        owner.relics += 1


@effect("caa-06")
def szlak(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    if owner.relics <= 0:
        return
    on_port = played.location in (LocationId.RYNEK, LocationId.GILDIA)
    if not on_port:
        return
    if state.sea_route_open:
        owner.relics -= 1
        owner.evacuated_relics += 1
    else:
        # bez Floty: +1 Herezji ekstra (zgodnie z kartą; nie +2)
        owner.add_heresy(1)
        owner.relics -= 1
        owner.evacuated_relics += 1


@effect("caa-07")
def kaptur(state: GameState, played: PlayedCard, card: Card) -> None:
    state.era_modifiers[f"shield:{played.owner.value}"] = True
    # nie free escape z lochów — tylko shield na Erę


@effect("caa-08")
def poswiecenie(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    board = owner.agents_on_board()
    if board:
        board[0].burned = True
    # ewakuacja 1 Relikwii tylko jeśli już w schowku; bez grabienia puli
    if owner.relics > 0:
        owner.relics -= 1
        owner.evacuated_relics += 1
    elif state.relics_on_board.get(played.location, 0) > 0:
        state.relics_on_board[played.location] -= 1
        owner.evacuated_relics += 1


@effect("caa-09")
def kryjowka(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    if card.id not in owner.permanents:
        owner.permanents.append(card.id)
    state.era_modifiers[f"relic_safe:{played.owner.value}"] = True


@effect("caa-10")
def echo(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    if state.relic_pool > 0:
        state.relic_pool -= 1
        state.relics_on_board[LocationId.LOCHY] += 1
    if state.relics_on_board.get(LocationId.LOCHY, 0) > 0:
        state.relics_on_board[LocationId.LOCHY] -= 1
        owner.relics += 1
    for a in owner.agents_in(LocationId.LOCHY) or owner.agents_on_board():
        a.location = LocationId.GILDIA
        break
    for rival in state.rivals(played.owner):
        if state.player(rival).agents_in(LocationId.LOCHY) or state.player(rival).dungeon_agents():
            state.player(rival).add_heresy(1)
