"""Table-legal choices (heuristics, not coin-flip skip of a legal window)."""
from __future__ import annotations

from inquisitio.cards.loader import Card
from inquisitio.engine.inquisitor import neighbors
from inquisitio.engine.state import LOCATIONS, FactionId, GameState
from inquisitio.engine.verdict import oficjum_snowball_threat


def _rival_agent_counts(state: GameState, fid: FactionId) -> dict[str, int]:
    counts = {loc: 0 for loc in LOCATIONS}
    for other, pl in state.players.items():
        if other == fid:
            continue
        for ag in pl.agents:
            if not ag.arrested and ag.location in counts:
                counts[ag.location] += 1
    return counts


def is_naslanie_card(card: Card) -> bool:
    tags = card.tags or []
    if "autodafe" in tags:
        return False
    action = (card.raw or {}).get("action") if isinstance(card.raw, dict) else None
    return "inquisitor" in tags or action == "send_inquisitor"


def choose_play_location(state: GameState, fid: FactionId, card: Card) -> str:
    if card.location in LOCATIONS:
        return str(card.location)
    raw = card.raw if isinstance(card.raw, dict) else {}
    tloc = raw.get("target_loc")
    if tloc == "dungeon":
        return "lochy"
    pl = state.players[fid]
    own = [ag.location for ag in pl.agents if not ag.arrested and ag.location in LOCATIONS]
    if is_naslanie_card(card):
        counts = _rival_agent_counts(state, fid)
        best = max(LOCATIONS, key=lambda loc: (counts[loc], loc == state.inquisitor_location))
        return best
    if "relic" in (card.tags or []):
        for loc in ("rynek", "gildia", "lochy", "trybunal", "palac"):
            if state.relics_on_board.get(loc, 0) > 0:
                return loc
    if tloc in ("same_location", "agent_location") and own:
        return own[0]
    if own:
        return own[0]
    return "trybunal"


def card_fiasco(state: GameState, fid: FactionId, card: Card, staged_loc: str) -> bool:
    """Suplement I: brak lokacji/agenta przy rozpatrzeniu → fiasko bez Herezji."""
    raw = card.raw if isinstance(card.raw, dict) else {}
    tloc = raw.get("target_loc")
    pl = state.players[fid]
    free_here = [
        ag for ag in pl.agents if not ag.arrested and ag.location == staged_loc
    ]
    if card.location in LOCATIONS and not any(
        ag.location == card.location and not ag.arrested for ag in pl.agents
    ):
        return True
    if tloc == "dungeon" and not any(ag.location == "lochy" for ag in pl.agents):
        return True
    if tloc in ("same_location", "agent_location") and not free_here:
        return True
    return False


def choose_optional_agent_dest(state: GameState, fid: FactionId) -> tuple[int, str] | None:
    """None = skip; else (agent_index, dest)."""
    pl = state.players[fid]
    inq = state.inquisitor_location
    for i, ag in enumerate(pl.agents):
        if ag.arrested:
            continue
        opts = neighbors(ag.location)
        if not opts:
            continue
        if ag.location == inq:
            safe = [o for o in opts if o != inq]
            return (i, safe[0] if safe else opts[0])
        if fid == FactionId.CIENIE_AL_ANDALUS:
            if state.relics_on_board.get(ag.location, 0) > 0:
                harbors = [o for o in opts if o in ("rynek", "gildia")]
                if harbors:
                    return (i, harbors[0])
            for o in opts:
                if state.relics_on_board.get(o, 0) > 0 or o in ("rynek", "gildia"):
                    return (i, o)
        if fid == FactionId.SWIETE_OFICJUM:
            counts = _rival_agent_counts(state, fid)
            best = max(opts, key=lambda loc: counts.get(loc, 0))
            if counts.get(best, 0) > counts.get(ag.location, 0):
                return (i, best)
    return None


def choose_naslanie_target(state: GameState, fid: FactionId) -> str | None:
    counts = _rival_agent_counts(state, fid)
    if fid == FactionId.SWIETE_OFICJUM:
        best = max(LOCATIONS, key=lambda loc: counts[loc])
        return best if counts[best] > 0 else None
    if fid == FactionId.CIENIE_AL_ANDALUS:
        pl = state.players[fid]
        relic_locs = {
            ag.location
            for ag in pl.agents
            if not ag.arrested and state.relics_on_board.get(ag.location, 0) > 0
        }
        away = [loc for loc in LOCATIONS if loc not in relic_locs and counts[loc] > 0]
        if away:
            return max(away, key=lambda loc: counts[loc])
        return None
    best = max(LOCATIONS, key=lambda loc: counts[loc])
    return best if counts[best] > 0 else None


def resolve_naslanie_winner(
    state: GameState, declarations: dict[FactionId, str]
) -> tuple[FactionId, str] | None:
    if not declarations:
        return None
    if FactionId.SWIETE_OFICJUM in declarations:
        fid = FactionId.SWIETE_OFICJUM
        return fid, declarations[fid]
    first = state.turn_order[0]
    if first in declarations:
        return first, declarations[first]
    best_fid = min(
        declarations,
        key=lambda f: (state.players[f].heresy, state.turn_order.index(f)),
    )
    return best_fid, declarations[best_fid]


def lowest_heresy_chooser(state: GameState) -> FactionId:
    min_h = min(state.players[f].heresy for f in state.turn_order)
    for f in state.turn_order:
        if state.players[f].heresy == min_h:
            return f
    return state.turn_order[0]


def choose_patrol_dest(state: GameState, chooser: FactionId) -> str:
    cur = state.inquisitor_location
    opts = [cur, *neighbors(cur)]
    counts = _rival_agent_counts(state, chooser)
    if chooser == FactionId.CIENIE_AL_ANDALUS:
        pl = state.players[chooser]
        danger = {
            ag.location
            for ag in pl.agents
            if not ag.arrested and state.relics_on_board.get(ag.location, 0) > 0
        }
        safe = [o for o in opts if o not in danger]
        pool = safe or opts
        return max(pool, key=lambda loc: counts.get(loc, 0) if loc != cur else -1)
    return max(opts, key=lambda loc: (counts.get(loc, 0), loc == cur))


def should_announce_autodafe(state: GameState) -> bool:
    loc = state.inquisitor_location
    so = FactionId.SWIETE_OFICJUM
    for fid, pl in state.players.items():
        if so in state.players and fid == so:
            continue
        if any(ag.location == loc and not ag.arrested for ag in pl.agents):
            return True
    return False


def should_accuse(state: GameState, fid: FactionId, accused_list: list[FactionId]) -> bool:
    if not accused_list:
        return False
    if fid == FactionId.SWIETE_OFICJUM:
        return True
    if FactionId.SWIETE_OFICJUM in accused_list and oficjum_snowball_threat(state):
        return True
    return True


def interrogate_prefer(fid: FactionId) -> str:
    if fid == FactionId.CIENIE_AL_ANDALUS:
        return "double"
    if fid == FactionId.GILDIA_CIENI:
        return "hook"
    if fid == FactionId.SWIETE_OFICJUM:
        return "heresy"
    return "hook"


def victim_complies_hook(state: GameState, victim: FactionId) -> bool:
    """Comply if refusal would put you in Court range."""
    pl = state.players[victim]
    return pl.heresy + 2 >= state.accusation_threshold
