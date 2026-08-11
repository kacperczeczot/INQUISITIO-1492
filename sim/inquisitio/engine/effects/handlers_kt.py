"""Kabała z Toledo handlers — wolniejszy farm Wskazówek."""

from __future__ import annotations

from inquisitio.engine.effects.registry import effect
from inquisitio.engine.state import GameState, PlayedCard
from inquisitio.model import Card


def _gain_clue(state: GameState, owner_faction, *, require_observed: bool = True) -> bool:
    owner = state.player(owner_faction)
    if require_observed and owner.zone() == "czysta":
        # wejdź w strefę albo nic — sweet spot jest obowiązkowy
        owner.add_heresy(1)
        if owner.zone() == "czysta":
            return False
    if state.clue_pool <= 0:
        return False
    key = f"clues_gained:{owner_faction.value}"
    if int(state.era_modifiers.get(key, 0)) >= 1:
        return False
    state.clue_pool -= 1
    owner.clues += 1
    state.era_modifiers[key] = int(state.era_modifiers.get(key, 0)) + 1
    return True


def _gain_clue_force(state: GameState, owner_faction) -> bool:
    """Signature: ignore per-era cap once."""
    owner = state.player(owner_faction)
    if state.clue_pool <= 0:
        return False
    state.clue_pool -= 1
    owner.clues += 1
    return True


@effect("kt-01")
def alchemia(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    owner.gold += 1
    if owner.zone() == "obserwowana":
        _gain_clue(state, played.owner)
    else:
        # poza sweet spotem: dump winy zamiast darmowej wskazówki
        owner.add_heresy(-1) if owner.heresy > 0 else None
        rivals = state.rivals(played.owner)
        if rivals:
            state.era_modifiers[f"blame:{played.owner.value}"] = max(
                rivals, key=lambda f: state.player(f).heresy
            )


@effect("kt-02")
def fragment(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    _gain_clue(state, played.owner, require_observed=(owner.zone() == "czysta"))
    if 4 <= owner.heresy <= 6 and owner.deck:
        owner.hand.append(owner.deck.pop(0))


@effect("kt-03")
def artefakt(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    spent = False
    if owner.relics > 0:
        owner.relics -= 1
        state.relic_pool += 1
        spent = True
    # 1 clue (force), nie 2; bez free heresy=5 jackpot
    if spent:
        _gain_clue_force(state, played.owner)
        owner.gold += 1
    else:
        _gain_clue(state, played.owner)


@effect("kt-04")
def rytual(state: GameState, played: PlayedCard, card: Card) -> None:
    _gain_clue(state, played.owner)
    for p in state.players.values():
        if p.heresy >= 4:
            p.add_heresy(1)


@effect("kt-05")
def przepis(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    owner.gold += 2
    state.era_modifiers[f"cost_rebate:{played.owner.value}"] = 1


@effect("kt-06")
def archiwum(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    # czysta strefa: tylko draw, nie clue (tempo)
    if owner.heresy <= 3:
        if owner.deck:
            owner.hand.append(owner.deck.pop(0))
    else:
        _gain_clue(state, played.owner)
    if state.time_deck:
        state.era_modifiers["peek_time"] = state.time_deck[0]


@effect("kt-07")
def transmutacja(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    owner.add_heresy(-2)
    rivals = state.rivals(played.owner)
    if rivals:
        target = max(
            rivals,
            key=lambda f: state.player(f).stakes
            + state.player(f).evacuated_relics * 2
            + state.player(f).clues
            + state.player(f).control_palace
            + state.player(f).control_market,
        )
        state.era_modifiers[f"blame:{played.owner.value}"] = target


@effect("kt-08")
def wskazowka_cykl(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    _gain_clue(state, played.owner)
    # bez drugiego clue w tej samej erze
    if owner.clues >= 2 and owner.zone() == "obserwowana":
        owner.add_heresy(1)


@effect("kt-09")
def zwierciadlo(state: GameState, played: PlayedCard, card: Card) -> None:
    state.era_modifiers[f"mirror:{played.owner.value}"] = True
    state.player(played.owner).gold += 1


@effect("kt-10")
def pieczec_salomona(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    if owner.clues >= 3:
        _gain_clue_force(state, played.owner)
        owner.heresy = min(10, max(owner.heresy, 6))
    else:
        _gain_clue(state, played.owner)
        owner.add_heresy(1)
