"""Effect registry — resolve card plays."""
from __future__ import annotations

import random
from typing import Callable

from inquisitio.cards.loader import Card, load_all_cards
from inquisitio.engine.dungeon import arrest_agent, interrogate
from inquisitio.engine.heresy import add_heresy
from inquisitio.engine.hooks import force_hook, grant_hook
from inquisitio.engine.inquisitor import resolve_autodafe, send_inquisitor
from inquisitio.engine.state import LOCATIONS, LOCATION_INDEX, FactionId, GameState

Handler = Callable[[GameState, FactionId, Card, random.Random], None]


def _neighbors(loc: str) -> list[str]:
    i = LOCATION_INDEX[loc]
    out = []
    if i > 0:
        out.append(LOCATIONS[i - 1])
    if i < len(LOCATIONS) - 1:
        out.append(LOCATIONS[i + 1])
    return out


def _move_agent(state: GameState, fid: FactionId, rng: random.Random, n: int = 1) -> None:
    pl = state.players[fid]
    free = [ag for ag in pl.agents if not ag.arrested]
    for _ in range(n):
        if not free:
            return
        ag = rng.choice(free)
        opts = _neighbors(ag.location)
        if opts:
            dest = rng.choice(opts)
            # avoid autodafé location slightly
            if dest == state.inquisitor_location and len(opts) > 1 and rng.random() < 0.5:
                dest = [o for o in opts if o != state.inquisitor_location][0]
            ag.location = dest


def _pick_rival(state: GameState, fid: FactionId, rng: random.Random) -> FactionId | None:
    rivals = [x for x in state.turn_order if x != fid]
    if not rivals:
        return None
    # prefer higher heresy for framing, but not always
    rivals.sort(key=lambda r: state.players[r].heresy, reverse=True)
    if rng.random() < 0.7:
        return rivals[0]
    return rng.choice(rivals)


def apply_generic(state: GameState, fid: FactionId, card: Card, rng: random.Random) -> None:
    pl = state.players[fid]
    if card.gold:
        pl.gold = max(0, pl.gold + card.gold)
    if card.heresy:
        add_heresy(state, fid, card.heresy, reason=card.id)
    if card.target_heresy:
        rival = _pick_rival(state, fid, rng)
        if rival:
            add_heresy(state, rival, card.target_heresy, reason=f"{card.id}:frame")
    if card.agents:
        _move_agent(state, fid, rng, card.agents)
    if card.arrest and state.layer in ("B", "C"):
        rival = _pick_rival(state, fid, rng)
        if rival:
            arrest_agent(state, rival)
    if card.creates_hook and state.layer in ("B", "C"):
        rival = _pick_rival(state, fid, rng)
        if rival:
            grant_hook(state, fid, rival)


def _signature(state: GameState, fid: FactionId, card: Card, rng: random.Random) -> None:
    apply_generic(state, fid, card, rng)
    pl = state.players[fid]
    if card.id == "so-10":
        resolve_autodafe(state, force=True)
    elif card.id == "caa-09":
        # move relic along agent
        for ag in pl.agents:
            if not ag.arrested and state.relics_on_board.get(ag.location, 0) > 0:
                state.relics_on_board[ag.location] -= 1
                neigh = _neighbors(ag.location)
                if neigh:
                    dest = rng.choice(neigh)
                    state.relics_on_board[dest] = state.relics_on_board.get(dest, 0) + 1
                break
    elif card.id == "caa-10":
        for ag in pl.agents:
            if ag.arrested:
                continue
            loc = ag.location
            if state.relics_on_board.get(loc, 0) > 0 and (
                pl.path_via_double or pl.avoided_autodafe or ag.double_agent
            ):
                state.relics_on_board[loc] -= 1
                pl.relics_evacuated += 1
                if ag.double_agent or ag.controller:
                    pl.path_via_double = True
                break
        # also try sea route
        if state.sea_route_open:
            for loc in ("rynek", "gildia"):
                if state.relics_on_board.get(loc, 0) > 0:
                    for ag in pl.agents:
                        if ag.location == loc and not ag.arrested:
                            state.relics_on_board[loc] -= 1
                            pl.relics_evacuated += 1
                            pl.avoided_autodafe = True
                            break
    elif card.id in ("kb-09", "kb-10"):
        pl.decrees_played += 1
        if card.id == "kb-09":
            targets = [t for t, n in pl.hooks_on.items() if n > 0]
            if targets:
                force_hook(state, fid, targets[0], comply=rng.random() < 0.5)
    elif card.id == "kt-10":
        if pl.fragments >= 3 and not (4 <= pl.heresy <= 6):
            pl.heresy = 5
        if pl.fragments < 3:
            pl.fragments = max(pl.fragments, 3)
    elif card.id == "gc-10":
        # mark fall if any rival critical or hooked
        for rival in state.turn_order:
            if rival == fid:
                continue
            rp = state.players[rival]
            if rp.heresy >= state.accusation_threshold or any(
                ag.double_agent for ag in rp.agents
            ):
                pl.falls += 1
                break


def _so_extra(state: GameState, fid: FactionId, card: Card, rng: random.Random) -> None:
    apply_generic(state, fid, card, rng)
    if card.id == "so-07":
        rival = _pick_rival(state, fid, rng)
        if rival:
            interrogate(state, fid, rival, rng)
    elif card.id == "so-08":
        # send to location with own agent
        locs = [ag.location for ag in state.players[fid].agents if not ag.arrested]
        if locs:
            send_inquisitor(state, fid, rng.choice(locs))
    elif card.id == "so-10":
        _signature(state, fid, card, rng)


def _caa_extra(state: GameState, fid: FactionId, card: Card, rng: random.Random) -> None:
    apply_generic(state, fid, card, rng)
    pl = state.players[fid]
    if card.id == "caa-06":
        for ag in pl.agents:
            if ag.arrested:
                ag.arrested = False
                _move_agent(state, fid, rng, 1)
                break
    elif card.id == "caa-08":
        for ag in pl.agents:
            if ag.double_agent and ag.controller == fid:
                opts = _neighbors(ag.location)
                if opts:
                    ag.location = rng.choice(opts)
                break
    elif card.id in ("caa-09", "caa-10"):
        _signature(state, fid, card, rng)


def _kb_extra(state: GameState, fid: FactionId, card: Card, rng: random.Random) -> None:
    apply_generic(state, fid, card, rng)
    if card.id in ("kb-09", "kb-10"):
        _signature(state, fid, card, rng)


def _kt_extra(state: GameState, fid: FactionId, card: Card, rng: random.Random) -> None:
    apply_generic(state, fid, card, rng)
    pl = state.players[fid]
    if card.id == "kt-06":
        rival = _pick_rival(state, fid, rng)
        if rival:
            out = interrogate(state, fid, rival, rng, prefer=rng.choice(["hook", "heresy"]))
            if out:
                pl.fragments += 1
    elif card.id == "kt-09":
        if any(ag.location in ("lochy", "trybunal") for ag in pl.agents):
            pl.fragments += 1
    elif card.id == "kt-10":
        _signature(state, fid, card, rng)


def _gc_extra(state: GameState, fid: FactionId, card: Card, rng: random.Random) -> None:
    apply_generic(state, fid, card, rng)
    if card.id == "gc-09":
        # already creates_hook via generic; refusal path in politics
        pass
    elif card.id == "gc-10":
        _signature(state, fid, card, rng)


FACTION_HANDLERS: dict[str, Handler] = {
    "swiete-oficjum": _so_extra,
    "cienie-al-andalus": _caa_extra,
    "korona-borgiowie": _kb_extra,
    "kabala-toledo": _kt_extra,
    "gildia-cieni": _gc_extra,
}


def play_card(state: GameState, fid: FactionId, card_id: str, rng: random.Random) -> bool:
    cards = load_all_cards()
    card = cards.get(card_id)
    if not card:
        return False
    pl = state.players[fid]
    if card_id not in pl.hand:
        return False
    cost = max(0, card.cost)
    if pl.gold < cost:
        return False
    pl.gold -= cost
    pl.hand.remove(card_id)
    pl.discard.append(card_id)
    handler = FACTION_HANDLERS.get(card.faction, apply_generic)
    handler(state, fid, card, rng)
    state.metrics.cards_played += 1
    state.add_log(f"{fid.value} played {card_id}")
    return True


def resolve_time_edict(state: GameState, card_id: str, rng: random.Random) -> None:
    cards = load_all_cards()
    card = cards.get(card_id)
    if not card:
        return
    state.add_log(f"Time edict {card_id}")
    if card.id == "time-01":
        for fid, pl in state.players.items():
            if any(ag.location == "rynek" for ag in pl.agents):
                add_heresy(state, fid, 1, reason="time-01")
    elif card.id == "time-02":
        if FactionId.CIENIE_AL_ANDALUS in state.players:
            _move_agent(state, FactionId.CIENIE_AL_ANDALUS, rng, 1)
        for fid, pl in state.players.items():
            if fid == FactionId.CIENIE_AL_ANDALUS:
                continue
            if any(ag.location == "gildia" for ag in pl.agents):
                add_heresy(state, fid, 1, reason="time-02")
    elif card.id == "time-03":
        state.sea_route_open = True
    elif card.id == "time-04":
        if FactionId.KABALA_TOLEDO in state.players:
            pl = state.players[FactionId.KABALA_TOLEDO]
            if any(ag.location in ("trybunal", "lochy") for ag in pl.agents):
                pl.fragments += 1
    elif card.id == "time-05":
        resolve_autodafe(state, force=True)
    elif card.id == "time-06":
        candidates = [
            f
            for f in (FactionId.KORONA_BORGIOWIE, FactionId.GILDIA_CIENI)
            if f in state.players
        ]
        if candidates:
            candidates.sort(key=lambda f: state.players[f].heresy)
            holder = candidates[0]
            rivals = [x for x in state.turn_order if x != holder]
            if rivals:
                grant_hook(state, holder, rng.choice(rivals))
    elif card.id == "time-07":
        # move toward rynek
        from inquisitio.engine.inquisitor import move_inquisitor

        move_inquisitor(state, rng, toward="rynek")
    elif card.id == "time-08":
        state.relics_on_board["lochy"] = state.relics_on_board.get("lochy", 0) + 1
