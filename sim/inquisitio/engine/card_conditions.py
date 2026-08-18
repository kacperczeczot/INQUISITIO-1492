"""YAML `condition` fields — fiasko when unmet (Suplement I)."""
from __future__ import annotations

from inquisitio.cards.loader import Card
from inquisitio.engine.hooks import distinct_hook_victims
from inquisitio.engine.state import FactionId, GameState


def card_condition_met(state: GameState, fid: FactionId, card: Card) -> bool:
    raw = card.raw if isinstance(card.raw, dict) else {}
    cond = raw.get("condition")
    if not cond:
        return True
    pl = state.players[fid]

    if cond == "relic_present":
        return any(
            not ag.arrested and state.relics_on_board.get(ag.location, 0) > 0
            for ag in pl.agents
        )
    if cond == "has_double_agent":
        return any(ag.double_agent and ag.controller == fid for ag in pl.agents)
    if cond == "agent_in_dungeon_or_tribunal":
        return any(ag.location in ("lochy", "trybunal") and not ag.arrested for ag in pl.agents)
    if cond == "fragments_eq_3":
        return pl.fragments == 3
    if cond == "active_hooks_gte_2":
        return distinct_hook_victims(state, fid) >= 2
    if cond == "heresy_gte_4":
        return pl.heresy >= 4
    if cond == "has_fragment_and_agent_in_dungeon_or_tribunal":
        return pl.fragments >= 1 and any(
            ag.location in ("lochy", "trybunal") and not ag.arrested for ag in pl.agents
        )
    if cond == "no_inquisitor_or_double_or_sea_route":
        locs = {ag.location for ag in pl.agents if not ag.arrested}
        quiet = state.inquisitor_location not in locs
        via_double = any(ag.double_agent and ag.controller == fid for ag in pl.agents)
        return quiet or via_double or state.sea_route_open
    if cond == "rival_has_hook_or_double_or_autodafe":
        for rival in state.turn_order:
            if rival == fid:
                continue
            rp = state.players[rival]
            if pl.hooks_on.get(rival, 0) > 0 or rival in pl.hook_victims_ever:
                return True
            if any(ag.double_agent for ag in rp.agents):
                return True
            if rival != FactionId.SWIETE_OFICJUM:
                for ag in rp.agents:
                    if ag.location == state.inquisitor_location and not ag.arrested:
                        return True
        return False
    if cond == "rival_in_dungeon_or_inquisitor":
        for rival in state.turn_order:
            if rival == fid:
                continue
            rp = state.players[rival]
            if any(ag.location == "lochy" or ag.arrested for ag in rp.agents):
                return True
            if any(
                ag.location == state.inquisitor_location and not ag.arrested for ag in rp.agents
            ):
                return True
        return False
    return True
