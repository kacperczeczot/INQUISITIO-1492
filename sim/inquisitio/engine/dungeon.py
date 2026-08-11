"""Dungeons — interrogation → double or hook (Layer B)."""
from __future__ import annotations

import random

from inquisitio.engine.heresy import add_heresy
from inquisitio.engine.hooks import grant_hook
from inquisitio.engine.state import FactionId, GameState


def arrest_agent(state: GameState, owner: FactionId, location: str | None = None) -> bool:
    pl = state.players[owner]
    for ag in pl.agents:
        if ag.arrested:
            continue
        if location and ag.location != location:
            continue
        ag.arrested = True
        ag.location = "lochy"
        state.add_log(f"Arrest {owner.value} agent -> lochy")
        return True
    return False


def interrogate(
    state: GameState,
    interrogator: FactionId,
    victim: FactionId,
    rng: random.Random,
    prefer: str | None = None,
) -> str | None:
    """prefer: 'double' | 'hook' | 'heresy'. Returns outcome or None."""
    iq = state.players[interrogator]
    if iq.used_interrogation:
        return None
    victim_pl = state.players[victim]
    arrested = [ag for ag in victim_pl.agents if ag.arrested]
    if not arrested:
        return None
    iq.used_interrogation = True
    choice = prefer or rng.choice(["double", "hook", "heresy"])
    if choice == "double":
        ag = arrested[0]
        ag.double_agent = True
        ag.controller = interrogator
        state.metrics.doubles_created += 1
        if interrogator == FactionId.CIENIE_AL_ANDALUS:
            iq.path_via_double = True
        state.add_log(f"Double agent: {victim.value} controlled by {interrogator.value}")
        return "double"
    if choice == "hook":
        grant_hook(state, interrogator, victim)
        return "hook"
    add_heresy(state, victim, 2, reason="interrogation")
    if interrogator == FactionId.KABALA_TOLEDO:
        iq.fragments += 1
    return "heresy"
