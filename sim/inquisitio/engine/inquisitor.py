"""Grand Inquisitor — Patrol / Autodafé."""
from __future__ import annotations

import random
from collections import deque

from inquisitio.engine.heresy import add_heresy
from inquisitio.engine.state import (
    LOCATION_INDEX,
    NEIGHBORS,
    FactionId,
    GameState,
    InquisitorMode,
)


def neighbors(loc: str) -> list[str]:
    return list(NEIGHBORS.get(loc, ()))


def shortest_path(src: str, dst: str) -> list[str]:
    """BFS path including src and dst. Empty if unreachable."""
    if src == dst:
        return [src]
    if src not in NEIGHBORS or dst not in NEIGHBORS:
        return []
    prev: dict[str, str | None] = {src: None}
    q: deque[str] = deque([src])
    while q:
        cur = q.popleft()
        for nxt in NEIGHBORS[cur]:
            if nxt in prev:
                continue
            prev[nxt] = cur
            if nxt == dst:
                path = [dst]
                while path[-1] != src:
                    parent = prev[path[-1]]
                    assert parent is not None
                    path.append(parent)
                path.reverse()
                return path
            q.append(nxt)
    return []


def step_toward(src: str, dst: str) -> str:
    """One edge along a shortest path toward dst; stay if already there / unreachable."""
    path = shortest_path(src, dst)
    if len(path) >= 2:
        return path[1]
    return src


def move_inquisitor(state: GameState, rng: random.Random, toward: str | None = None) -> None:
    cur = state.inquisitor_location
    if toward and toward in LOCATION_INDEX:
        state.inquisitor_location = step_toward(cur, toward)
    else:
        opts = [cur, *neighbors(cur)]
        state.inquisitor_location = rng.choice(opts)
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


def resolve_autodafe(
    state: GameState, force: bool = False, award_stack: bool = True
) -> bool:
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
    if award_stack and so and hit_rival:
        so_pl = state.players[so]
        # C: dampen free Stosy once Oficjum is already at 2 (anti 5p snowball)
        if state.layer == "C" and so_pl.stacks >= 2 and not force:
            state.add_log("Autodafé: pressure only (Oficjum at 2+ Stosy)")
        else:
            so_pl.stacks += 1
            state.add_log(f"Autodafé stack -> {so_pl.stacks}")
    elif so and hit_rival and not award_stack:
        state.add_log("Autodafé: pressure only (no Oficjum stack)")
    state.inquisitor_mode = InquisitorMode.PATROL
    state.add_log(f"Autodafé at {loc}")
    return True


def era_start_inquisitor(state: GameState, rng: random.Random) -> None:
    move_inquisitor(state, rng)
    crowd = sum(
        1
        for pl in state.players.values()
        for ag in pl.agents
        if ag.location == state.inquisitor_location and not ag.arrested
    )
    # Lower crowd ignition — Oficjum snowballed when Autodafé was too frequent
    if crowd >= 3 and can_autodafe(state) and rng.random() < 0.18:
        resolve_autodafe(state)
