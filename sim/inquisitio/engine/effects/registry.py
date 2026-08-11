from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from inquisitio.engine.state import GameState, PlayedCard
    from inquisitio.model import Card

EffectFn = Callable[["GameState", "PlayedCard", "Card"], None]

_REGISTRY: dict[str, EffectFn] = {}
_LOADED = False


def effect(card_id: str) -> Callable[[EffectFn], EffectFn]:
    def deco(fn: EffectFn) -> EffectFn:
        _REGISTRY[card_id] = fn
        return fn

    return deco


def get_handler(card_id: str) -> EffectFn | None:
    return _REGISTRY.get(card_id)


def register_defaults() -> None:
    global _LOADED
    if _LOADED:
        return
    from inquisitio.engine.effects import (  # noqa: F401
        handlers_caa,
        handlers_gc,
        handlers_kb,
        handlers_kt,
        handlers_so,
        handlers_time,
    )

    _LOADED = True


def apply_card_effect(state: GameState, played: PlayedCard, card: Card) -> None:
    register_defaults()
    from inquisitio.engine.effects import generic
    from inquisitio.model import FactionId

    handler = get_handler(card.id)
    if handler:
        handler(state, played, card)
    else:
        generic.apply_generic(state, played, card)

    # Time events: do not apply owner heresy to a player seat
    if card.faction.value == "time":
        return

    owner = state.player(played.owner)
    before = owner.heresy
    # Mirror permanent: redirect incoming heresy next — applied here as self heresy
    if card.heresy:
        if state.era_modifiers.get(f"mirror:{played.owner.value}") and card.heresy > 0:
            # spend mirror on self-damage from own card? no — mirror is for incoming
            owner.add_heresy(card.heresy)
        else:
            owner.add_heresy(card.heresy)
        if state.era_modifiers.get("extra_heresy_on_2plus") and card.heresy >= 2:
            owner.add_heresy(1)
    if owner.heresy >= state.threshold > before:
        state.metrics.critical_entries += 1
    state.metrics.max_heresy_seen[played.owner.value] = max(
        state.metrics.max_heresy_seen.get(played.owner.value, 0),
        owner.heresy,
    )

    if card.target_heresy:
        target = state.era_modifiers.get(f"blame:{played.owner.value}")
        if target is None:
            rivals = state.rivals(played.owner)
            if rivals:
                target = max(rivals, key=lambda f: state.player(f).heresy)
        if target is not None:
            if isinstance(target, str):
                target = FactionId(target)
            # mirror redirect
            if state.era_modifiers.get(f"mirror:{target.value}"):
                # redirect to another rival
                others = [f for f in state.rivals(target) if f != played.owner]
                if others:
                    target = others[0]
                state.era_modifiers.pop(f"mirror:{target.value}", None)
            tp = state.player(target)
            tb = tp.heresy
            amount = card.target_heresy
            # observed zone boost for podrzucenie-style already in handler
            if state.player(target).zone() == "obserwowana" and card.id == "gc-02":
                amount = max(amount, 2)
            tp.add_heresy(amount)
            if tp.heresy >= state.threshold > tb:
                state.metrics.critical_entries += 1
