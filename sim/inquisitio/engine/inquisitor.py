"""Grand Inquisitor — Patrol / Autodafé."""
from __future__ import annotations

import random
from collections import deque

from inquisitio.config import CONFIG
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
    sys = state.sys_overrides or {}
    speed = sys.get("inquisitor_speed", CONFIG.variants.inquisitor_speed)
    if speed == 0:
        state.inquisitor_mode = InquisitorMode.PATROL
        return
    for _ in range(speed):
        cur = state.inquisitor_location
        if toward and toward in LOCATION_INDEX:
            state.inquisitor_location = step_toward(cur, toward)
        else:
            opts = [cur, *neighbors(cur)]
            state.inquisitor_location = rng.choice(opts)
    state.inquisitor_mode = InquisitorMode.PATROL
    state.add_log(f"Inquisitor patrol -> {state.inquisitor_location}")


def send_inquisitor(state: GameState, sender: FactionId, location: str) -> bool:
    """Nasłanie already spent this era → no extra teleport on reveal."""
    p = state.players[sender]
    if p.used_inquisitor_send:
        return False
    if location not in LOCATION_INDEX:
        return False
    p.used_inquisitor_send = True
    p.inquisitor_send_count += 1
    nxt = step_toward(state.inquisitor_location, location)
    state.inquisitor_location = nxt
    state.add_log(f"{sender.value} sent Inquisitor toward {location} -> {nxt}")
    return True


def can_autodafe(state: GameState) -> bool:
    return state.eras_since_autodafe >= state.autodafe_cooldown


def resolve_autodafe(
    state: GameState, force: bool = False, award_stack: bool = True
) -> bool:
    if not force and not can_autodafe(state):
        return False
    loc = state.inquisitor_location
    from inquisitio.engine.dungeon import detect_marionettes_at

    detect_marionettes_at(state, loc)
    state.inquisitor_mode = InquisitorMode.AUTODAFE
    state.metrics.autodafe_count += 1
    state.eras_since_autodafe = 0
    burned_rival_agents = 0
    so = FactionId.SWIETE_OFICJUM if FactionId.SWIETE_OFICJUM in state.players else None
    for fid, pl in state.players.items():
        if so and fid == so:
            continue
        for ag in pl.agents:
            if ag.location != loc or ag.arrested:
                continue
            add_heresy(state, fid, 1, reason=f"autodafe:{loc}")
            ag.arrested = True
            ag.location = "lochy"
            if pl.heresy < state.observed_threshold:
                state.add_log(
                    f"Autodafé (Czysta <{state.observed_threshold}): {fid.value} agent arrested -> Lochy"
                )
            else:
                burned_rival_agents += 1
                state.add_log(
                    f"Autodafé (Obserwowana/Krytyczna >={state.observed_threshold}): {fid.value} agent burned -> Lochy"
                )
                if FactionId.GILDIA_CIENI in state.players:
                    gc_pl = state.players[FactionId.GILDIA_CIENI]
                    if fid != FactionId.GILDIA_CIENI and fid in gc_pl.hook_victims_ever:
                        gc_pl.falls += 1
                        state.add_log(
                            f"Gildia Cieni: Upadek from Autodafé on hooked rival {fid.value} (total={gc_pl.falls})"
                        )

    if state.relics_on_board.get(loc, 0) > 0:
        relic_cnt = state.relics_on_board[loc]
        state.relics_on_board[loc] = 0
        state.add_log(f"Autodafé: {relic_cnt} Relic(s) at {loc} returned to pool")

    if award_stack and so and burned_rival_agents:
        so_pl = state.players[so]
        so_pl.stacks += burned_rival_agents
        state.add_log(f"Autodafé stack +{burned_rival_agents} -> {so_pl.stacks}")
    elif so and burned_rival_agents and not award_stack:
        state.add_log("Autodafé: pressure only (no Oficjum stack)")
    state.inquisitor_mode = InquisitorMode.PATROL
    state.add_log(f"Autodafé at {loc}")
    return True


def era_start_inquisitor(
    state: GameState,
    rng: random.Random,
    *,
    toward: str | None = None,
    dest: str | None = None,
    announce_autodafe: bool | None = None,
) -> None:
    """Patrol 0 or 1 (speed override for L4), then optional Autodafé."""
    sys = state.sys_overrides or {}
    speed = sys.get("inquisitor_speed", CONFIG.variants.inquisitor_speed)
    cur = state.inquisitor_location
    if int(speed) == 0:
        state.inquisitor_mode = InquisitorMode.PATROL
        state.add_log("Inquisitor patrol skipped (speed 0)")
    elif dest is not None:
        if dest == cur or dest in neighbors(cur):
            state.inquisitor_location = dest
        state.inquisitor_mode = InquisitorMode.PATROL
        state.add_log(f"Inquisitor patrol -> {state.inquisitor_location}")
    elif toward and toward in LOCATION_INDEX:
        steps = max(1, int(speed))
        for _ in range(steps):
            state.inquisitor_location = step_toward(state.inquisitor_location, toward)
        state.inquisitor_mode = InquisitorMode.PATROL
        state.add_log(f"Inquisitor patrol toward {toward} -> {state.inquisitor_location}")
    else:
        state.inquisitor_mode = InquisitorMode.PATROL
        state.add_log(f"Inquisitor holds at {cur}")

    from inquisitio.engine.dungeon import detect_marionettes_at

    detect_marionettes_at(state, state.inquisitor_location)

    has_agents = any(
        ag.location == state.inquisitor_location and not ag.arrested
        for fid, pl in state.players.items()
        if not (FactionId.SWIETE_OFICJUM in state.players and fid == FactionId.SWIETE_OFICJUM)
        for ag in pl.agents
    )
    do_auto = announce_autodafe if announce_autodafe is not None else has_agents
    if do_auto and can_autodafe(state):
        resolve_autodafe(state)
