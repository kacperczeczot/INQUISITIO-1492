"""Effect registry — resolve card plays."""
from __future__ import annotations

import random
from typing import Callable

from inquisitio.cards.loader import Card, load_all_cards
from inquisitio.engine.dungeon import arrest_agent, interrogate
from inquisitio.engine.heresy import add_heresy
from inquisitio.engine.hooks import (
    distinct_hook_victims_ever,
    force_hook,
    grant_hook,
)
from inquisitio.engine.inquisitor import neighbors, resolve_autodafe, send_inquisitor
from inquisitio.engine.state import FactionId, GameState

Handler = Callable[[GameState, FactionId, Card, random.Random], None]


def _neighbors(loc: str) -> list[str]:
    return neighbors(loc)


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
            prev = ag.location
            ag.location = dest
            if prev != dest:
                state.add_log(f"{fid.value} agent {prev}→{dest}")
                # Cienie: agent may drag a Relic toward harbors (A teach needs drag for 2nd)
                if (
                    fid == FactionId.CIENIE_AL_ANDALUS
                    and state.relics_on_board.get(prev, 0) > 0
                    and rng.random()
                    < {"A": 0.55, "B": 0.70, "C": 0.55}.get(state.layer, 0.55)
                ):
                    state.relics_on_board[prev] -= 1
                    state.relics_on_board[dest] = state.relics_on_board.get(dest, 0) + 1
                    state.add_log(f"{fid.value} dragged relic {prev}→{dest}")


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
        before = pl.gold
        pl.gold = max(0, pl.gold + card.gold)
        if pl.gold != before:
            state.add_log(f"{fid.value} gold {before}→{pl.gold} ({card.id})")
    if card.heresy:
        add_heresy(state, fid, card.heresy, reason=card.id)
    if card.target_heresy:
        rival = _pick_rival(state, fid, rng)
        if rival:
            amt = card.target_heresy
            # A teach: Gildia Podrzucenie hits harder without breaking B/C
            if state.layer == "A" and card.id == "gc-03":
                amt = max(amt, 2)
            add_heresy(state, rival, amt, reason=f"{card.id}:frame")
            pl.frames_dealt += amt
    if card.agents:
        _move_agent(state, fid, rng, card.agents)
    if card.arrest and state.layer in ("B", "C"):
        rival = _pick_rival(state, fid, rng)
        if rival:
            arrest_agent(state, rival)
    # Hooks: A-layer teach cards only when playing layer A; B/C cards on B/C
    if card.creates_hook:
        card_layer = (card.layer or "A").upper()
        allowed = (state.layer == "A" and card_layer == "A") or (
            state.layer in ("B", "C") and card_layer in ("B", "C")
        )
        # A: Faworyt Haki dopiero od Ery 4 (Korona nie domyka stołu za wcześnie)
        if (
            allowed
            and state.layer == "A"
            and card.id == "kb-04"
            and state.era < 4
        ):
            allowed = False
        if allowed:
            rival = _pick_rival(state, fid, rng)
            if rival:
                grant_hook(state, fid, rival)


def _signature(state: GameState, fid: FactionId, card: Card, rng: random.Random) -> None:
    apply_generic(state, fid, card, rng)
    pl = state.players[fid]
    if card.id == "so-10":
        resolve_autodafe(state, force=True)
    elif card.id == "caa-09":
        # move relic along agent — prefer harbor (rynek/gildia)
        for ag in pl.agents:
            if not ag.arrested and state.relics_on_board.get(ag.location, 0) > 0:
                state.relics_on_board[ag.location] -= 1
                neigh = _neighbors(ag.location)
                if neigh:
                    harbors = [d for d in neigh if d in ("rynek", "gildia")]
                    dest = rng.choice(harbors) if harbors and rng.random() < 0.7 else rng.choice(neigh)
                    state.relics_on_board[dest] = state.relics_on_board.get(dest, 0) + 1
                    state.add_log(f"{fid.value} relic {ag.location}→{dest}")
                break
    elif card.id == "caa-10":
        evacuated_n = 0
        for ag in pl.agents:
            if evacuated_n >= 2:
                break
            if ag.arrested:
                continue
            loc = ag.location
            if state.relics_on_board.get(loc, 0) <= 0:
                continue
            via_double = bool(ag.double_agent or ag.controller or pl.path_via_double)
            quiet = state.inquisitor_location != loc
            if via_double or pl.avoided_autodafe or quiet or state.sea_route_open:
                state.relics_on_board[loc] -= 1
                pl.relics_evacuated += 1
                evacuated_n += 1
                if via_double:
                    pl.path_via_double = True
                if quiet or state.sea_route_open:
                    pl.avoided_autodafe = True
        if state.sea_route_open and evacuated_n < 2:
            for loc in ("rynek", "gildia"):
                if evacuated_n >= 2:
                    break
                while state.relics_on_board.get(loc, 0) > 0 and evacuated_n < 2:
                    if not any(ag.location == loc and not ag.arrested for ag in pl.agents):
                        break
                    state.relics_on_board[loc] -= 1
                    pl.relics_evacuated += 1
                    pl.avoided_autodafe = True
                    evacuated_n += 1
        if evacuated_n:
            state.add_log(
                f"{fid.value} evacuated {evacuated_n} relic(s) (total={pl.relics_evacuated})"
            )
    elif card.id in ("kb-09", "kb-10"):
        pl.decrees_played += 1
        state.add_log(f"{fid.value} decree played (total={pl.decrees_played})")
        if card.id == "kb-09":
            targets = [t for t, n in pl.hooks_on.items() if n > 0]
            if targets:
                force_hook(state, fid, targets[0], comply=rng.random() < 0.5)
            else:
                rival = _pick_rival(state, fid, rng)
                # 5p: soft plant (floor); ≤4p: plant only if already had a Hak ever
                if rival and (
                    len(state.turn_order) >= 5
                    or distinct_hook_victims_ever(state, fid) >= 1
                ):
                    grant_hook(state, fid, rival)
    elif card.id == "kt-10":
        # Finisher assist: +1 Fragment only when already on the path (≥1)
        if pl.fragments >= 1:
            pl.fragments += 1
        if pl.fragments >= 3 and not (4 <= pl.heresy <= 6):
            pl.heresy = 5
        state.add_log(f"{fid.value} fragments={pl.fragments} heresy={pl.heresy}")
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
                state.add_log(f"{fid.value} fall on {rival.value} (total={pl.falls})")
                break


def _so_extra(state: GameState, fid: FactionId, card: Card, rng: random.Random) -> None:
    apply_generic(state, fid, card, rng)
    if card.id == "so-07":
        rival = _pick_rival(state, fid, rng)
        if rival:
            interrogate(state, fid, rival, rng)
    elif card.id in ("so-04", "so-08"):
        pl = state.players[fid]
        # so-04 is A teach nasłanie; on B/C it's just a move (so-08 is the real nasłanie)
        if card.id == "so-04" and state.layer != "A":
            _move_agent(state, fid, rng, 1)
            return
        if pl.used_inquisitor_send:
            return
        locs = [ag.location for ag in pl.agents if not ag.arrested]
        if locs:
            send_inquisitor(state, fid, rng.choice(locs))
            pl.used_inquisitor_send = True
    elif card.id == "so-10":
        # Signature already paid generic costs above; do not re-apply (double heresy).
        resolve_autodafe(state, force=True)


def _caa_extra(state: GameState, fid: FactionId, card: Card, rng: random.Random) -> None:
    apply_generic(state, fid, card, rng)
    pl = state.players[fid]
    if card.id == "caa-05":
        if state.layer != "A":
            _move_agent(state, fid, rng, 1)
            return
        # A teach: Kurier once — second Relic via quiet harbor / drag
        if pl.used_kurier:
            return
        for ag in pl.agents:
            if ag.arrested:
                continue
            loc = ag.location
            if state.relics_on_board.get(loc, 0) <= 0:
                continue
            state.relics_on_board[loc] -= 1
            pl.relics_evacuated += 1
            pl.used_kurier = True
            state.add_log(
                f"{fid.value} evacuated relic from {loc} (total={pl.relics_evacuated})"
            )
            break
    elif card.id == "caa-06":
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
    pl = state.players[fid]
    if card.id == "kb-05":
        if state.layer == "A":
            # One Dekret credit from List (repeat plays don't stack)
            if pl.decrees_played < 1:
                pl.decrees_played += 1
                state.add_log(f"{fid.value} decree played (total={pl.decrees_played})")
        else:
            if pl.heresy > 0:
                pl.heresy -= 1
                state.add_log(f"{fid.value} list-zelazny heresy→{pl.heresy}")
    elif card.id in ("kb-09", "kb-10"):
        _signature(state, fid, card, rng)


def _kt_extra(state: GameState, fid: FactionId, card: Card, rng: random.Random) -> None:
    apply_generic(state, fid, card, rng)
    pl = state.players[fid]
    if card.id == "kt-03":
        if state.layer == "A":
            # Cap: only +1 Fragment if still below 2 AND already in/near sweet path
            if pl.fragments < 2 and pl.heresy >= 3:
                pl.fragments += 1
                state.add_log(f"{fid.value} fragment (total={pl.fragments})")
        else:
            pl.gold += 1
    elif card.id == "kt-05":
        if state.layer == "A":
            if (
                pl.fragments >= 1
                and any(ag.location in ("lochy", "trybunal") for ag in pl.agents)
            ):
                pl.fragments += 1
                state.add_log(f"{fid.value} fragment (total={pl.fragments})")
        elif state.layer == "C":
            # Cap 2 on ≤4p; 5p may finish path via kt-05 (crowded table)
            cap = 3 if len(state.turn_order) >= 5 else 2
            if pl.fragments < cap and any(
                ag.location in ("lochy", "trybunal") for ag in pl.agents
            ):
                pl.fragments += 1
                state.add_log(f"{fid.value} fragment (total={pl.fragments})")
            else:
                pl.gold += 1
        else:
            pl.gold += 1
    elif card.id == "kt-06":
        rival = _pick_rival(state, fid, rng)
        if rival:
            out = interrogate(state, fid, rival, rng, prefer=rng.choice(["hook", "heresy"]))
            # Fragment on successful rite only (no fizzle credit — Kabala 3p C)
            if out:
                pl.fragments += 1
                state.add_log(f"{fid.value} fragment (total={pl.fragments})")
    elif card.id == "kt-09":
        # Third fragment gate: need path already started
        if pl.fragments >= 1 and any(
            ag.location in ("lochy", "trybunal") for ag in pl.agents
        ):
            pl.fragments += 1
            state.add_log(f"{fid.value} fragment (total={pl.fragments})")
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
    gold_before = pl.gold
    pl.gold -= cost
    pl.hand.remove(card_id)
    pl.discard.append(card_id)
    handler = FACTION_HANDLERS.get(card.faction, apply_generic)
    handler(state, fid, card, rng)
    state.metrics.cards_played += 1
    name = card.name
    suffix = " [signature]" if card.breaks_rule or card.type == "signature" else ""
    paid = f" paid {cost}" if cost else ""
    state.add_log(f"{fid.value} played {card_id} ({name}){suffix}{paid}")
    if cost and pl.gold != gold_before:
        state.add_log(f"{fid.value} gold after cost {gold_before}→{pl.gold}")
    return True


def resolve_time_edict(state: GameState, card_id: str, rng: random.Random) -> None:
    cards = load_all_cards()
    card = cards.get(card_id)
    if not card:
        return
    state.add_log(f"Time edict {card_id} ({card.name})")
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
        state.add_log("Sea route open")
    elif card.id == "time-04":
        if FactionId.KABALA_TOLEDO in state.players:
            pl = state.players[FactionId.KABALA_TOLEDO]
            if any(ag.location in ("trybunal", "lochy") for ag in pl.agents):
                pl.fragments += 1
                state.add_log(f"kabala-toledo fragment (total={pl.fragments})")
    elif card.id == "time-05":
        # Drama fire without free Oficjum Stos (stack still via so-10 / claimed Autodafé)
        resolve_autodafe(state, force=True, award_stack=False)
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
        state.add_log("Relic placed in lochy")
