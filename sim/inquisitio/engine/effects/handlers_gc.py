"""Gildia Cieni handlers."""

from __future__ import annotations

from inquisitio.engine.effects.registry import effect
from inquisitio.engine.state import GameState, PlayedCard
from inquisitio.model import Card, FactionId, LocationId


def _blame_best(state: GameState, owner) -> None:
    rivals = state.rivals(owner)
    if not rivals:
        return
    # Prefer near-critical who blocks gildia
    target = max(rivals, key=lambda f: (state.player(f).heresy, state.player(f).gold))
    state.era_modifiers[f"blame:{owner.value}"] = target


@effect("gc-01")
def fabrykowanie(state: GameState, played: PlayedCard, card: Card) -> None:
    _blame_best(state, played.owner)
    owner = state.player(played.owner)
    target = state.era_modifiers.get(f"blame:{played.owner.value}")
    if target and state.player(target).heresy + card.target_heresy >= state.threshold:
        if owner.gold >= 1:
            owner.gold -= 1
            state.era_modifiers["pending_process"] = target
            state.era_modifiers["pending_strategic"] = True


@effect("gc-02")
def podrzucenie(state: GameState, played: PlayedCard, card: Card) -> None:
    rivals = state.rivals(played.owner)
    if not rivals:
        return
    from inquisitio.agents.politics import intrigue_progress

    target = max(rivals, key=lambda f: (intrigue_progress(state, f), state.player(f).heresy))
    state.era_modifiers[f"blame:{played.owner.value}"] = target
    # zawsze + draw; observed zone dostaje mocniejszy target via registry/gc
    owner = state.player(played.owner)
    if owner.deck:
        owner.hand.append(owner.deck.pop(0))
    if state.player(target).zone() == "obserwowana":
        state.player(target).add_heresy(1)  # extra beyond target_heresy 1 → effectively 2+


@effect("gc-03")
def szantaz(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    rivals = state.rivals(played.owner)
    if not rivals:
        return
    target = max(rivals, key=lambda f: state.player(f).gold)
    rp = state.player(target)
    if rp.gold >= 2:
        rp.gold -= 2
        owner.gold += 2
    else:
        state.era_modifiers[f"blame:{played.owner.value}"] = target
        # apply +2 via modifier since target_heresy is 0 on card
        rp.add_heresy(2)


@effect("gc-04")
def skrytobojstwo(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    for loc in (LocationId.GILDIA, LocationId.RYNEK, played.location):
        for rival in state.rivals(played.owner):
            agents = state.player(rival).agents_in(loc)
            if agents:
                agents[0].burned = True
                if state.player(rival).heresy >= state.threshold:
                    # tylko kradzież postępu — Upadek dopiero przez gc-10 / proces
                    rp = state.player(rival)
                    if rp.control_palace > 0:
                        rp.control_palace -= 1
                    elif rp.clues > 0:
                        rp.clues -= 1
                        state.clue_pool += 1
                return


@effect("gc-05")
def falszywy_swiadek(state: GameState, played: PlayedCard, card: Card) -> None:
    state.era_modifiers["gildia_redirect_process"] = True
    state.player(played.owner).gold += 1
    _blame_best(state, played.owner)


@effect("gc-06")
def straznik(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    if owner.gold >= 1:
        owner.gold -= 1
    if owner.dungeon_agents():
        a = owner.dungeon_agents()[0]
        a.in_dungeon = False
        a.location = LocationId.GILDIA
    else:
        for rival in state.rivals(played.owner):
            if state.player(rival).dungeon_agents():
                state.era_modifiers[f"extra_jail:{rival.value}"] = True
                break


@effect("gc-07")
def czarny_rynek(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    owner.gold += 2
    if owner.gold >= 3 and state.relics_on_board.get(played.location, 0) > 0:
        owner.gold -= 3
        state.relics_on_board[played.location] -= 1
        owner.relics += 1
    elif owner.relics > 0:
        owner.relics -= 1
        owner.gold += 3
        state.relic_pool += 1


@effect("gc-08")
def lista_dluznikow(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    if card.id not in owner.permanents:
        owner.permanents.append(card.id)
    for rival in state.rivals(played.owner):
        rp = state.player(rival)
        if rp.heresy >= 4:
            if rp.gold > 0:
                rp.gold -= 1
                owner.gold += 1
            else:
                rp.add_heresy(1)


@effect("gc-09")
def zatrute_zloto(state: GameState, played: PlayedCard, card: Card) -> None:
    rivals = state.rivals(played.owner)
    if not rivals:
        return
    target = max(rivals, key=lambda f: -state.player(f).heresy)  # cleanest gets poisoned
    state.player(target).gold += 1
    state.era_modifiers[f"blame:{played.owner.value}"] = target
    state.era_modifiers[f"no_cleanse:{target.value}"] = True


@effect("gc-10")
def upadek_domu(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    for rival in state.rivals(played.owner):
        rp = state.player(rival)
        burned = any(a.burned for a in rp.agents)
        # wymagaj spalenia LUB (herezja krytyczna + bankructwo)
        broke = rp.heresy >= state.threshold and rp.gold == 0 and rp.relics == 0 and rp.clues == 0
        if burned or broke:
            if rival not in owner.collapses:
                owner.collapses.append(rival)
