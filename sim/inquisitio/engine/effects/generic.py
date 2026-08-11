"""Fallback semantics from tags / frontmatter when no specific handler."""

from __future__ import annotations

from inquisitio.engine.state import GameState, PlayedCard
from inquisitio.model import Card, FactionId, LocationId


def apply_generic(state: GameState, played: PlayedCard, card: Card) -> None:
    owner = state.player(played.owner)
    tags = set(card.tags)

    if "kontrola" in tags or "dekret" in tags:
        # nie dawaj darmowego 1/1 — tylko +1 do jednej lokacji
        if played.location == LocationId.PALAC:
            owner.control_palace = min(3, owner.control_palace + 1)
        elif played.location == LocationId.RYNEK:
            owner.control_market = min(3, owner.control_market + 1)
        elif owner.control_palace <= owner.control_market:
            owner.control_palace = min(3, owner.control_palace + 1)
        else:
            owner.control_market = min(3, owner.control_market + 1)

    if "wskazowka" in tags or "kodeks" in tags:
        if state.clue_pool > 0:
            state.clue_pool -= 1
            owner.clues += 1

    if "relikwia" in tags or "transport" in tags or "ewakuacja" in tags:
        if state.relics_on_board.get(played.location, 0) > 0:
            state.relics_on_board[played.location] -= 1
            owner.relics += 1
        elif "ewakuacja" in tags and owner.relics > 0 and (
            state.sea_route_open or played.location in (LocationId.RYNEK, LocationId.GILDIA)
        ):
            owner.relics -= 1
            owner.evacuated_relics += 1

    if "proces" in tags or "oblawa" in tags:
        # soft arrest: move rival agent from this loc to dungeon if heresy>=4
        for rival in state.rivals(played.owner):
            rp = state.player(rival)
            if rp.heresy < 4:
                continue
            here = rp.agents_in(played.location)
            if here:
                here[0].in_dungeon = True
                here[0].location = None
                break

    if "skrytobojstwo" in tags or "eliminacja" in tags:
        for rival in state.rivals(played.owner):
            here = state.player(rival).agents_in(played.location)
            if here:
                here[0].burned = True
                break

    if "ekonomia" in tags or "zloto" in tags:
        owner.gold += 1

    if "upadek" in tags:
        # mark weakest rival as collapsed candidate
        rivals = state.rivals(played.owner)
        if rivals and played.owner == FactionId.GILDIA_CIENI:
            target = min(rivals, key=lambda f: (
                state.player(f).gold
                + state.player(f).clues
                + state.player(f).relics
                + state.player(f).control_palace
                + state.player(f).control_market
            ))
            g = state.player(FactionId.GILDIA_CIENI)
            if state.player(target).heresy >= 7 and target not in g.collapses:
                g.collapses.append(target)

    if card.type.value == "permanent":
        if card.id not in owner.permanents:
            owner.permanents.append(card.id)
