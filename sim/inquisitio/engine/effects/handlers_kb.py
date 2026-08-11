"""Korona & Borgiowie handlers — skalisowane: kontrola budowana żetonami (cel 2+2)."""

from __future__ import annotations

from inquisitio.engine.effects.registry import effect
from inquisitio.engine.state import GameState, PlayedCard
from inquisitio.model import Card, LocationId


def _add_control(owner, which: str, amount: int = 1, cap: int = 3) -> None:
    if which == "palace":
        owner.control_palace = min(cap, owner.control_palace + amount)
    else:
        owner.control_market = min(cap, owner.control_market + amount)


@effect("kb-01")
def dekret(state: GameState, played: PlayedCard, card: Card) -> None:
    """+1 Kontrola w słabszej lokacji (nie obie naraz)."""
    owner = state.player(played.owner)
    if owner.control_palace <= owner.control_market:
        _add_control(owner, "palace", 1)
    else:
        _add_control(owner, "market", 1)
    state.era_modifiers["shadow_tax_loc"] = played.location.value


@effect("kb-02")
def przekupstwo(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    if owner.gold >= 2:
        owner.gold -= 2
        state.era_modifiers["korona_controls_process"] = True
        # bez darmowej kontroli Pałacu


@effect("kb-03")
def pobor(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    owner.gold += 3  # buff lekki vs Al-Andalus tempo
    for rival in state.rivals(played.owner):
        rp = state.player(rival)
        if rp.agents_in(LocationId.PALAC) or rp.agents_in(LocationId.RYNEK):
            if rp.gold > 0:
                rp.gold -= 1
                owner.gold += 1


@effect("kb-04")
def list_zelazny(state: GameState, played: PlayedCard, card: Card) -> None:
    state.era_modifiers[f"shield:{played.owner.value}"] = True
    owner = state.player(played.owner)
    if owner.agents_on_board():
        owner.agents_on_board()[0].location = LocationId.PALAC


@effect("kb-05")
def faworyt(state: GameState, played: PlayedCard, card: Card) -> None:
    """Draw + gold; kontrola tylko jeśli już masz obecność (agent w Pałacu)."""
    owner = state.player(played.owner)
    if owner.deck:
        owner.hand.append(owner.deck.pop(0))
    owner.gold += 1
    if owner.agents_in(LocationId.PALAC):
        _add_control(owner, "palace", 1)


@effect("kb-06")
def falszywe_akta(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    for rival in state.rivals(played.owner):
        rp = state.player(rival)
        if rp.control_palace > 0:
            rp.control_palace -= 1
            _add_control(owner, "palace", 1)
            return
        if rp.control_market > 0:
            rp.control_market -= 1
            _add_control(owner, "market", 1)
            return
    rivals = state.rivals(played.owner)
    if rivals:
        state.era_modifiers[f"blame:{played.owner.value}"] = rivals[0]


@effect("kb-07")
def kontrola_rynku(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    _add_control(owner, "market", 1)


@effect("kb-08")
def sojusz(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    rivals = state.rivals(played.owner)
    if rivals:
        from inquisitio.agents.politics import intrigue_progress

        ally = min(rivals, key=lambda f: intrigue_progress(state, f))
        state.player(ally).gold += 1
        owner.gold += 1
        state.era_modifiers[f"ally:{played.owner.value}"] = ally
        state.era_modifiers[f"ally:{ally.value}"] = played.owner


@effect("kb-09")
def kapitan(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    for loc in (LocationId.RYNEK, LocationId.PALAC):
        for rival in state.rivals(played.owner):
            agents = state.player(rival).agents_in(loc)
            if agents:
                agents[0].in_dungeon = True
                agents[0].location = None
                # bez darmowej kontroli — tylko czyszczenie przestrzeni
                return


@effect("kb-10")
def pieczec(state: GameState, played: PlayedCard, card: Card) -> None:
    """+1 do słabszej kontroli (nie obie naraz)."""
    owner = state.player(played.owner)
    if owner.control_palace <= owner.control_market:
        _add_control(owner, "palace", 1)
    else:
        _add_control(owner, "market", 1)
    for rival in state.rivals(played.owner):
        rp = state.player(rival)
        if rp.control_palace > owner.control_palace and rp.control_palace > 0:
            rp.control_palace -= 1
            break
        if rp.control_market > owner.control_market and rp.control_market > 0:
            rp.control_market -= 1
            break
    state.era_modifiers["shadow_needs_korona"] = True
