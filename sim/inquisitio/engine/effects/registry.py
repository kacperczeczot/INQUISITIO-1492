"""Effect registry — resolve card plays."""
from __future__ import annotations

import random
from typing import Callable

from inquisitio.cards.loader import Card, load_all_cards
from inquisitio.config import CONFIG
from inquisitio.engine.card_conditions import card_condition_met
from inquisitio.engine.dungeon import arrest_agent, interrogate
from inquisitio.engine.heresy import add_heresy
from inquisitio.engine.hooks import (
    distinct_hook_victims_ever,
    force_hook,
    grant_hook,
)
from inquisitio.engine.inquisitor import neighbors, resolve_autodafe, send_inquisitor
from inquisitio.engine.state import (
    LOCATIONS,
    FactionId,
    GameState,
    StagedPlay,
    heresy_zone,
)
from inquisitio.engine.table_ai import card_fiasco, choose_optional_agent_dest, choose_play_location

Handler = Callable[[GameState, FactionId, Card, random.Random], None]


def _neighbors(loc: str) -> list[str]:
    return neighbors(loc)


def optional_agent_step(state: GameState, fid: FactionId, rng: random.Random) -> None:
    """Księga: przy Opcji A/B opcjonalnie 1 Agent o max 1 lokację."""
    choice = choose_optional_agent_dest(state, fid)
    if not choice:
        return
    idx, dest = choice
    pl = state.players[fid]
    if idx >= len(pl.agents):
        return
    ag = pl.agents[idx]
    if ag.arrested:
        return
    prev = ag.location
    if dest not in _neighbors(prev) and dest != prev:
        return
    ag.location = dest
    if prev != dest:
        state.add_log(f"{fid.value} agent {prev}→{dest}")


def _play_location(state: GameState, fid: FactionId, card: Card) -> str:
    return choose_play_location(state, fid, card)


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
    raw = card.raw if isinstance(card.raw, dict) else {}
    dec = int(raw.get("heresy_decrease", 0) or 0)
    if dec > 0 and pl.heresy > 0:
        pl.heresy = max(0, pl.heresy - dec)
        state.add_log(f"{fid.value} heresy -{dec} -> {pl.heresy} ({card.id})")
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


def _drag_relic_toward_harbor(
    state: GameState, fid: FactionId, loc: str, rng: random.Random
) -> None:
    if state.relics_on_board.get(loc, 0) <= 0:
        return
    neigh = _neighbors(loc)
    if not neigh:
        return
    harbors = [d for d in neigh if d in ("rynek", "gildia")]
    dest = rng.choice(harbors) if harbors and rng.random() < 0.7 else rng.choice(neigh)
    state.relics_on_board[loc] -= 1
    state.relics_on_board[dest] = state.relics_on_board.get(dest, 0) + 1
    state.add_log(f"{fid.value} relic {loc}→{dest}")


def _mark_gc10_fall_if_legal(state: GameState, fid: FactionId) -> None:
    """Upadek Domu: rywal z Hakiem Gildii, Marionetką lub pod Inkwizytorem."""
    pl_gc = state.players[fid]
    for rival in state.turn_order:
        if rival == fid:
            continue
        rp = state.players[rival]
        hooked = pl_gc.hooks_on.get(rival, 0) > 0 or rival in pl_gc.hook_victims_ever
        marionette = any(ag.double_agent for ag in rp.agents)
        at_inquisitor = (
            rival != FactionId.SWIETE_OFICJUM
            and any(ag.location == state.inquisitor_location and not ag.arrested for ag in rp.agents)
        )
        if hooked or marionette or at_inquisitor:
            pl_gc.falls += 1
            state.add_log(f"{fid.value} fall on {rival.value} (total={pl_gc.falls})")
            break


def _staged_condition_ok(state: GameState, fid: FactionId, card_id: str) -> bool | None:
    for sp in state.pending_plays:
        if sp.owner == fid and sp.card_id == card_id:
            return sp.cond_ok
    return None


def _card_condition_satisfied(
    state: GameState, fid: FactionId, card: Card, *, staged: bool = False
) -> bool:
    raw = card.raw if isinstance(card.raw, dict) else {}
    if not raw.get("condition"):
        return True
    snap = _staged_condition_ok(state, fid, card.id) if staged else None
    if snap is not None:
        return snap
    return card_condition_met(state, fid, card)


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
        if not _card_condition_satisfied(state, fid, card, staged=True):
            state.add_log(f"{fid.value} {card.id} fiasko (condition unmet)")
            return
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
                # BUG-1 FIX: only set avoided_autodafe when Inquisitor was
                # actually nearby (at location or neighboring), meaning genuine
                # danger was dodged. Sea route is its own bypass path.
                if not quiet:
                    # Inquisitor IS at this location — agent survived Autodafé
                    pl.avoided_autodafe = True
                elif loc in neighbors(state.inquisitor_location):
                    # Inquisitor is one step away — narrow escape
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
                    # Sea route bypass — no need to set avoided_autodafe
                    evacuated_n += 1
        if evacuated_n:
            state.add_log(
                f"{fid.value} evacuated {evacuated_n} relic(s) (total={pl.relics_evacuated})"
            )
    elif card.id == "kb-09":
        pl.decrees_played += 1
        state.add_log(f"{fid.value} decree played (total={pl.decrees_played})")
        targets = [t for t, n in pl.hooks_on.items() if n > 0]
        if targets:
            force_hook(state, fid, targets[0], comply=rng.random() < 0.5)
        else:
            rival = _pick_rival(state, fid, rng)
            # Plant only if Korona already held a Hak on someone ever
            if rival and distinct_hook_victims_ever(state, fid) >= 1:
                grant_hook(state, fid, rival)
    elif card.id == "kb-10":
        if not _card_condition_satisfied(state, fid, card, staged=True):
            state.add_log(f"{fid.value} {card.id} fiasko (condition unmet)")
            return
        pl.decrees_played += 1
        state.add_log(f"{fid.value} decree played (total={pl.decrees_played})")
    elif card.id == "kt-10":
        # Finisher assist: +1 Fragment only when already on the path (≥1)
        if pl.fragments >= 1:
            pl.fragments += 1
        raw = card.raw if isinstance(card.raw, dict) else {}
        band = raw.get("target_heresy_band", [4, 6])
        fallback = raw.get("fallback_heresy", 5)
        if pl.fragments >= 3 and not (band[0] <= pl.heresy <= band[1]):
            pl.heresy = fallback
        state.add_log(f"{fid.value} fragments={pl.fragments} heresy={pl.heresy}")


def _so_extra(state: GameState, fid: FactionId, card: Card, rng: random.Random) -> None:
    apply_generic(state, fid, card, rng)
    if card.id == "so-07":
        rival = _pick_rival(state, fid, rng)
        if rival:
            interrogate(state, fid, rival, rng)
    elif card.id in ("so-04", "so-08"):
        pl = state.players[fid]
        if pl.used_inquisitor_send:
            return
        locs = [ag.location for ag in pl.agents if not ag.arrested]
        if locs:
            send_inquisitor(state, fid, rng.choice(locs))
    elif card.id == "so-10":
        # apply_generic already paid heresy cost; now fire the Autodafé.
        resolve_autodafe(state, force=True)


def _caa_extra(state: GameState, fid: FactionId, card: Card, rng: random.Random) -> None:
    apply_generic(state, fid, card, rng)
    pl = state.players[fid]
    if card.id == "caa-05":
        # caa-05 Odnalezienie Relikwii: If agent at location with relic, evacuate 1 relic. Otherwise discover relic at agent's location.
        limit = card.raw.get("kurier_limit", 1) if isinstance(card.raw, dict) else 1
        if pl.kurier_count >= limit:
            return
        evacuated = False
        for ag in pl.agents:
            if ag.arrested:
                continue
            loc = ag.location
            if state.relics_on_board.get(loc, 0) > 0:
                state.relics_on_board[loc] -= 1
                pl.relics_evacuated += 1
                pl.kurier_count += 1
                pl.used_kurier = True
                state.add_log(
                    f"{fid.value} caa-05 evacuated relic from {loc} (total={pl.relics_evacuated})"
                )
                if state.inquisitor_location != loc:
                    pl.shadow_exit = True
                evacuated = True
                break
        if not evacuated:
            for ag in pl.agents:
                if not ag.arrested:
                    loc = ag.location
                    state.relics_on_board[loc] = state.relics_on_board.get(loc, 0) + 1
                    pl.kurier_count += 1
                    pl.used_kurier = True
                    state.add_log(f"{fid.value} caa-05 discovered relic at {loc}")
                    break
    elif card.id == "caa-03":
        for ag in pl.agents:
            if not ag.arrested and state.relics_on_board.get(ag.location, 0) > 0:
                _drag_relic_toward_harbor(state, fid, ag.location, rng)
                break
    elif card.id == "caa-06":
        for ag in pl.agents:
            if ag.arrested:
                ag.arrested = False
                _move_agent(state, fid, rng, 1)
                break
    elif card.id == "caa-08":
        if not card_condition_met(state, fid, card):
            state.add_log(f"{fid.value} {card.id} fiasko (condition unmet)")
            return
        moved = False
        for other in state.players.values():
            if moved:
                break
            for ag in other.agents:
                if ag.double_agent and ag.controller == fid:
                    opts = _neighbors(ag.location)
                    if opts:
                        ag.location = rng.choice(opts)
                    moved = True
                    break
    elif card.id in ("caa-09", "caa-10"):
        _signature(state, fid, card, rng)
    elif card.id == "caa-11":
        raw = card.raw if isinstance(card.raw, dict) else {}
        if raw.get("move_inquisitor"):
            for ag in pl.agents:
                if not ag.arrested:
                    send_inquisitor(state, fid, ag.location)
                    break


def _kb_extra(state: GameState, fid: FactionId, card: Card, rng: random.Random) -> None:
    apply_generic(state, fid, card, rng)
    pl = state.players[fid]
    if card.id == "kb-05":
        if state.layer == "A":
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
        # Zakazana Wiedza: zawsze startuje tor fragmentów (nie tylko przy herezji 4–6).
        if pl.fragments < 3:
            pl.fragments += 1
            state.add_log(f"{fid.value} fragment from kt-03 (total={pl.fragments})")
        else:
            pl.gold += 1
            state.add_log(f"{fid.value} kt-03 overflow +1 gold")
    elif card.id == "kt-05":
        # kt-05 Wskazówka Cyklu: If agent at Lochy or Trybunał, gain 1 Fragment
        if any(ag.location in ("lochy", "trybunal") for ag in pl.agents) and pl.fragments < 3:
            pl.fragments += 1
            state.add_log(f"{fid.value} fragment from kt-05 (total={pl.fragments})")
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
        if not card_condition_met(state, fid, card):
            state.add_log(f"{fid.value} {card.id} fiasko (condition unmet)")
            return
        _mark_gc10_fall_if_legal(state, fid)


FACTION_HANDLERS: dict[str, Handler] = {
    "swiete-oficjum": _so_extra,
    "cienie-al-andalus": _caa_extra,
    "korona-borgiowie": _kb_extra,
    "kabala-toledo": _kt_extra,
    "gildia-cieni": _gc_extra,
}


def _card_cost(state: GameState, card: Card) -> int:
    sys = state.sys_overrides or {}
    card_cost_offset = sys.get("card_cost_offset", CONFIG.economy.card_cost_offset)
    sig_offset = sys.get("sig_cost_offset", CONFIG.economy.sig_cost_offset) if (card.breaks_rule or card.type == "signature") else 0
    curfew_cost = 1 if (state.active_time_edict == "time-02" and card.location in ("rynek", "gildia")) else 0
    return max(0, card.cost + card_cost_offset + sig_offset + curfew_cost)


def resolve_card_effects(
    state: GameState,
    fid: FactionId,
    card: Card,
    rng: random.Random,
    *,
    staged_loc: str | None = None,
) -> None:
    loc = staged_loc or _play_location(state, fid, card)
    if card_fiasco(state, fid, card, loc):
        state.add_log(f"{fid.value} {card.id} fiasko at {loc} (no heresy)")
        state.metrics.cards_played += 1
        return
    sys = state.sys_overrides or {}
    cards = load_all_cards(card_overrides=sys.get("card_overrides"))
    handler = FACTION_HANDLERS.get(card.faction, apply_generic)
    handler(state, fid, card, rng)
    state.metrics.cards_played += 1
    if ((card.heresy and card.heresy >= 1) or (card.target_heresy and card.target_heresy >= 1)):
        if FactionId.SWIETE_OFICJUM in state.players and fid != FactionId.SWIETE_OFICJUM:
            so_pl = state.players[FactionId.SWIETE_OFICJUM]
            if "so-05" in so_pl.hand:
                so_card = cards.get("so-05")
                so_cost = max(0, so_card.cost + sys.get("card_cost_offset", CONFIG.economy.card_cost_offset)) if so_card else 0
                if so_pl.gold >= so_cost:
                    so_pl.gold -= so_cost
                    so_pl.hand.remove("so-05")
                    so_pl.discard.append("so-05")
                    state.metrics.card_plays["so-05"] = state.metrics.card_plays.get("so-05", 0) + 1
                    target_h = so_card.target_heresy if so_card else 2
                    add_heresy(state, fid, target_h, reason="so-05:reaction")
                    so_pl.frames_dealt += target_h
                    state.add_log(
                        f"swiete-oficjum reaction so-05 (Wezwanie do Trybunału) on {fid.value} (+{target_h} heresy)"
                    )


def play_card(
    state: GameState,
    fid: FactionId,
    card_id: str,
    rng: random.Random,
    *,
    resolve: bool = True,
) -> bool:
    sys = state.sys_overrides or {}
    cards = load_all_cards(card_overrides=sys.get("card_overrides"))
    card = cards.get(card_id)
    if not card:
        return False
    pl = state.players[fid]
    if card_id not in pl.hand:
        return False
    cost = _card_cost(state, card)
    if pl.gold < cost:
        return False
    gold_before = pl.gold
    pl.gold -= cost
    pl.hand.remove(card_id)
    state.metrics.card_plays[card_id] = state.metrics.card_plays.get(card_id, 0) + 1
    loc = _play_location(state, fid, card)
    name = card.name
    suffix = " [signature]" if card.breaks_rule or card.type == "signature" else ""
    paid = f" paid {cost}" if cost else ""
    if not resolve:
        raw = card.raw if isinstance(card.raw, dict) else {}
        cond_ok = card_condition_met(state, fid, card) if raw.get("condition") else None
        state.pending_plays.append(
            StagedPlay(
                owner=fid,
                card_id=card_id,
                location=loc,
                seq=len(state.pending_plays),
                cond_ok=cond_ok,
            )
        )
        state.add_log(f"{fid.value} staged {card_id} ({name}) under {loc}{suffix}{paid}")
        if cost and pl.gold != gold_before:
            state.add_log(f"{fid.value} gold after cost {gold_before}→{pl.gold}")
        return True
    pl.discard.append(card_id)
    state.add_log(f"{fid.value} played {card_id} ({name}){suffix}{paid}")
    if cost and pl.gold != gold_before:
        state.add_log(f"{fid.value} gold after cost {gold_before}→{pl.gold}")
    resolve_card_effects(state, fid, card, rng, staged_loc=loc)
    return True


def resolve_pending_plays(state: GameState, rng: random.Random) -> None:
    """Faza II krok 2: odkrycie lokacje 1→5, w każdej od 1. gracza."""
    sys = state.sys_overrides or {}
    cards = load_all_cards(card_overrides=sys.get("card_overrides"))
    pending = list(state.pending_plays)
    state.pending_plays.clear()
    for loc in LOCATIONS:
        for fid in state.turn_order:
            for sp in pending:
                if sp.location != loc or sp.owner != fid:
                    continue
                card = cards.get(sp.card_id)
                pl = state.players[fid]
                if card is None:
                    continue
                pl.discard.append(sp.card_id)
                state.add_log(f"{fid.value} revealed {sp.card_id} ({card.name}) at {loc}")
                resolve_card_effects(state, fid, card, rng, staged_loc=loc)


def resolve_time_edict(state: GameState, card_id: str, rng: random.Random) -> None:
    cards = load_all_cards()
    card = cards.get(card_id)
    if not card:
        return
    state.add_log(f"Time edict {card_id} ({card.name})")
    
    if card.id == "time-01":
        # Kapitulacja Grenady: +1 gold for agents in palac, Inquisitor moves toward trybunal
        for fid, pl in state.players.items():
            if any(ag.location == "palac" and not ag.arrested for ag in pl.agents):
                pl.gold += 1
                state.add_log(f"{fid.value} +1 gold from palac celebration")
        from inquisitio.engine.inquisitor import move_inquisitor
        move_inquisitor(state, rng, toward="trybunal")
        
    elif card.id == "time-02":
        # Godzina Policyjna: curfew active for this era (+1 gold under rynek & gildia)
        state.active_time_edict = "time-02"
        state.add_log("Edict: Curfew active (+1 gold for cards under Rynek/Gildia this era)")
        
    elif card.id == "time-03":
        # Flota Odkrywców: opens sea route + +1 gold for agents in rynek or gildia
        state.sea_route_open = True
        state.add_log("Sea route open")
        for fid, pl in state.players.items():
            if any(ag.location in ("rynek", "gildia") and not ag.arrested for ag in pl.agents):
                pl.gold += 1
                state.add_log(f"{fid.value} +1 gold from harbor trade")
                
    elif card.id == "time-04":
        # Rewizja w Dzielnicach: highest heresy +1 heresy, lowest heresy +1 gold
        if state.players:
            max_h = max(pl.heresy for pl in state.players.values())
            min_h = min(pl.heresy for pl in state.players.values())
            for fid, pl in state.players.items():
                if pl.heresy == max_h:
                    add_heresy(state, fid, 1, reason="time-04 (highest heresy)")
                if pl.heresy == min_h:
                    pl.gold += 1
                    state.add_log(f"{fid.value} +1 gold from time-04 (lowest heresy)")
                    
    elif card.id == "time-05":
        # Gorączka Donosów: threshold -1 for this era
        state.active_time_edict = "time-05"
        state.add_log("Edict: Denunciation fever active (accusation threshold -1 this era)")
        
    elif card.id == "time-06":
        # Nocna Obława: move Inquisitor to location with most agents
        loc_counts: dict[str, int] = {}
        for pl in state.players.values():
            for ag in pl.agents:
                if not ag.arrested and ag.location:
                    loc_counts[ag.location] = loc_counts.get(ag.location, 0) + 1
        if loc_counts:
            max_c = max(loc_counts.values())
            top_locs = [l for l, c in loc_counts.items() if c == max_c]
            chosen_loc = top_locs[0] if len(top_locs) == 1 else rng.choice(top_locs)
            from inquisitio.engine.inquisitor import move_inquisitor
            move_inquisitor(state, rng, toward=chosen_loc)
            state.add_log(f"Night raid: Inquisitor moved toward {chosen_loc}")
            
    elif card.id == "time-07":
        # Bunt w Lochach: free 1 prisoner to gildia, or place relic if empty
        arrested_agents = []
        for fid, pl in state.players.items():
            for ag in pl.agents:
                if ag.arrested or ag.location == "lochy":
                    arrested_agents.append((fid, ag))
        if arrested_agents:
            fid, ag = rng.choice(arrested_agents)
            ag.arrested = False
            ag.location = "gildia"
            state.add_log(f"{fid.value} agent freed from lochy to gildia")
        else:
            state.relics_on_board["lochy"] = state.relics_on_board.get("lochy", 0) + 1
            state.add_log("Relic placed in lochy (empty dungeon)")
            
    elif card.id == "time-08":
        # Święte Przymierze: verdicts suspended for this era
        state.active_time_edict = "time-08"
        state.add_log("Edict: Holy Alliance active (Verdicts suspended this era)")
        
    elif card.id == "time-09":
        # Jarmark Królewski: market bonus for this era
        state.active_time_edict = "time-09"
        state.add_log("Edict: Royal Market active (economic action on Rynek +2 gold)")
        
    elif card.id == "time-10":
        # Amnestia Biskupia: −1 Herezja w Obserwowanej (SSOT: observed_threshold … T−1)
        for fid, pl in state.players.items():
            if heresy_zone(pl.heresy, state.accusation_threshold, state.observed_threshold) == "obserwowana":
                add_heresy(state, fid, -1, reason="time-10 (episcopal amnesty)")

