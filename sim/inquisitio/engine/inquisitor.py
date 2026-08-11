"""Grand Inquisitor — Patrol / Autodafé."""
from __future__ import annotations

import random

from inquisitio.engine.heresy import add_heresy
from inquisitio.engine.state import (
    LOCATIONS,
    LOCATION_INDEX,
    FactionId,
    GameState,
    InquisitorMode,
)


def move_inquisitor(state: GameState, rng: random.Random, toward: str | None = None) -> None:
    idx = LOCATION_INDEX[state.inquisitor_location]
    if toward and toward in LOCATION_INDEX:
        target = LOCATION_INDEX[toward]
        if target > idx:
            idx = min(idx + 1, len(LOCATIONS) - 1)
        elif target < idx:
            idx = max(idx - 1, 0)
        # else stay
    else:
        # default patrol: random stay / +1 / -1
        step = rng.choice([-1, 0, 1])
        idx = max(0, min(len(LOCATIONS) - 1, idx + step))
    state.inquisitor_location = LOCATIONS[idx]
    state.inquisitor_mode = InquisitorMode.PATROL
    state.add_log(f"Inquisitor patrol -> {state.inquisitor_location}")


def send_inquisitor(state: GameState, sender: FactionId, location: str) -> bool:
    """Player send (1/era). Oficjum preferred via agent heuristics."""
    p = state.players[sender]
    if p.used_inquisitor_send:
        return False
    if location not in LOCATION_INDEX:
        return False
    p.used_inquisitor_send = True
    state.inquisitor_location = location
    state.add_log(f"{sender.value} sent Inquisitor to {location}")
    return True


def can_autodafe(state: GameState) -> bool:
    return state.eras_since_autodafe >= 2


def resolve_autodafe(state: GameState, force: bool = False) -> bool:
    if not force and not can_autodafe(state):
        return False
    loc = state.inquisitor_location
    state.inquisitor_mode = InquisitorMode.AUTODAFE
    state.metrics.autodafe_count += 1
    state.eras_since_autodafe = 0
    hit_rival = False
    so = None
    for fid, pl in state.players.items():
        if fid.value == "swiete-oficjum":
            so = fid
        for ag in pl.agents:
            if ag.location == loc and not ag.arrested:
                add_heresy(state, fid, 1, reason=f"autodafe:{loc}")
                if so and fid != so:
                    hit_rival = True
                # survivors may mark avoidance if they leave later
    if so and hit_rival:
        state.players[so].stacks += 1
        state.add_log(f"Autodafé stack -> {state.players[so].stacks}")
    state.inquisitor_mode = InquisitorMode.PATROL
    state.add_log(f"Autodafé at {loc}")
    return True


def era_start_inquisitor(state: GameState, rng: random.Random) -> None:
    move_inquisitor(state, rng)
    # opportunistic autodafé if crowded and allowed
    crowd = sum(
        1
        for pl in state.players.values()
        for ag in pl.agents
        if ag.location == state.inquisitor_location and not ag.arrested
    )
    if crowd >= 3 and can_autodafe(state) and rng.random() < 0.35:
        resolve_autodafe(state)
