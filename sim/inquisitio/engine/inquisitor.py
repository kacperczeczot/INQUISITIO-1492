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
    sys = state.sys_overrides or {}
    speed = sys.get("inquisitor_speed", 1)
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
    return state.eras_since_autodafe >= state.autodafe_cooldown


def resolve_autodafe(
    state: GameState, force: bool = False, award_stack: bool = True
) -> bool:
    if not force and not can_autodafe(state):
        return False
    loc = state.inquisitor_location
    state.inquisitor_mode = InquisitorMode.AUTODAFE
    state.metrics.autodafe_count += 1
    state.eras_since_autodafe = 0
    hit_rival_dirty = False
    so = None
    for fid, pl in state.players.items():
        if fid.value == "swiete-oficjum":
            so = fid
        for ag in pl.agents:
            if ag.location == loc and not ag.arrested:
                add_heresy(state, fid, 1, reason=f"autodafe:{loc}")
                ag.arrested = True
                ag.location = "lochy"
                if pl.heresy <= 3:
                    state.add_log(f"Autodafé (Czysta <=3): {fid.value} agent arrested -> Lochy")
                else:
                    if so and fid != so:
                        hit_rival_dirty = True
                    state.add_log(f"Autodafé (Obserwowana/Krytyczna >=4): {fid.value} agent burned -> Lochy")
                    # Gildia Cieni: Upadek if burned rival had hook from Gildia
                    if FactionId.GILDIA_CIENI in state.players:
                        gc_pl = state.players[FactionId.GILDIA_CIENI]
                        if fid != FactionId.GILDIA_CIENI and fid in gc_pl.hook_victims_ever:
                            gc_pl.falls += 1
                            state.add_log(f"Gildia Cieni: Upadek from Autodafé on hooked rival {fid.value} (total={gc_pl.falls})")

    # Relikwia w lokacji Autodafé wraca do puli (zgodnie z Księgą Zasad)
    if state.relics_on_board.get(loc, 0) > 0:
        relic_cnt = state.relics_on_board[loc]
        state.relics_on_board[loc] = 0
        state.add_log(f"Autodafé: {relic_cnt} Relic(s) at {loc} returned to pool")

    if award_stack and so and hit_rival_dirty:
        so_pl = state.players[so]
        so_pl.stacks += 1
        state.add_log(f"Autodafé stack -> {so_pl.stacks}")
    elif so and hit_rival_dirty and not award_stack:
        state.add_log("Autodafé: pressure only (no Oficjum stack)")
    state.inquisitor_mode = InquisitorMode.PATROL
    state.add_log(f"Autodafé at {loc}")
    return True


def era_start_inquisitor(state: GameState, rng: random.Random) -> None:
    move_inquisitor(state, rng)
    has_agents = any(
        ag.location == state.inquisitor_location and not ag.arrested
        for pl in state.players.values()
        for ag in pl.agents
    )
    if has_agents and can_autodafe(state):
        resolve_autodafe(state)
