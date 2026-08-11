"""Talia Czasu handlers."""

from __future__ import annotations

from inquisitio.engine.effects.registry import effect
from inquisitio.engine.state import GameState, PlayedCard
from inquisitio.model import Card, FactionId, LocationId


@effect("time-01")
def upadek_grenady(state: GameState, played: PlayedCard, card: Card) -> None:
    state.era_modifiers["shadow_heresy_palac"] = 1
    if state.relic_pool > 0:
        state.relic_pool -= 1
        state.relics_on_board[LocationId.LOCHY] += 1


@effect("time-02")
def edykt_alhambra(state: GameState, played: PlayedCard, card: Card) -> None:
    for p in state.players.values():
        if p.heresy >= 4:
            p.add_heresy(1)
    if FactionId.SWIETE_OFICJUM in state.players:
        state.player(FactionId.SWIETE_OFICJUM).influence_tribunal += 1
    if FactionId.CIENIE_AL_ANDALUS in state.players:
        caa = state.player(FactionId.CIENIE_AL_ANDALUS)
        if caa.agents_on_board():
            caa.agents_on_board()[0].location = LocationId.GILDIA


@effect("time-03")
def flota(state: GameState, played: PlayedCard, card: Card) -> None:
    state.sea_route_open = True


@effect("time-04")
def archiwa(state: GameState, played: PlayedCard, card: Card) -> None:
    if state.relic_pool > 0:
        state.relic_pool -= 1
        state.relics_on_board[LocationId.GILDIA] += 1
    state.era_modifiers["lochy_shadow_gold"] = 1
    state.era_modifiers["lochy_shadow_heresy"] = 1


@effect("time-05")
def auto_de_fe(state: GameState, played: PlayedCard, card: Card) -> None:
    for p in state.players.values():
        if p.heresy >= state.threshold and p.agents_on_board():
            a = p.agents_on_board()[0]
            a.in_dungeon = True
            a.location = None
    state.era_modifiers["free_accuse"] = True


@effect("time-06")
def spisek(state: GameState, played: PlayedCard, card: Card) -> None:
    for p in state.players.values():
        p.control_palace = 0
    state.era_modifiers["palac_discount"] = 1
    state.era_modifiers["first_shadow_palac_heresy"] = 1


@effect("time-07")
def niepokoj(state: GameState, played: PlayedCard, card: Card) -> None:
    state.era_modifiers["market_trade_bonus"] = 1
    state.era_modifiers["market_agent_heresy"] = 1
    if state.relic_pool > 0:
        state.relic_pool -= 1
        state.relics_on_board[LocationId.RYNEK] += 1


@effect("time-08")
def krypta(state: GameState, played: PlayedCard, card: Card) -> None:
    if state.relic_pool > 0:
        state.relic_pool -= 1
        state.relics_on_board[LocationId.LOCHY] += 1
    if state.clue_pool > 0:
        state.era_modifiers["clue_on_tribunal"] = True
