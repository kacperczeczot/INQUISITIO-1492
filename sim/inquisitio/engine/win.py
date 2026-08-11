"""Victory checks — faction political goals."""
from __future__ import annotations

from inquisitio.engine.hooks import distinct_hook_victims
from inquisitio.engine.state import FactionId, GameState, heresy_zone


def check_winner(state: GameState) -> FactionId | None:
    for fid in state.turn_order:
        pl = state.players[fid]
        if fid == FactionId.SWIETE_OFICJUM:
            if pl.stacks >= 2:
                return fid
            # alternate: 2 rivals condemned counted via stacks already
        elif fid == FactionId.CIENIE_AL_ANDALUS:
            if pl.relics_evacuated >= 2 and (pl.path_via_double or pl.avoided_autodafe):
                return fid
            # Layer A softening: 2 relics enough if layer A
            if state.layer == "A" and pl.relics_evacuated >= 2:
                return fid
        elif fid == FactionId.KORONA_BORGIOWIE:
            if pl.decrees_played >= 2 and distinct_hook_victims(state, fid) >= 2:
                return fid
            if state.layer == "A" and pl.decrees_played >= 2:
                return fid
        elif fid == FactionId.KABALA_TOLEDO:
            if pl.fragments >= 3 and heresy_zone(pl.heresy) == "obserwowana":
                return fid
            if state.layer == "A" and pl.fragments >= 3:
                return fid
        elif fid == FactionId.GILDIA_CIENI:
            if pl.falls >= 2:
                return fid
    return None


def end_game_tiebreak(state: GameState) -> FactionId:
    """After max eras: closest to goal, then lowest heresy."""
    scores: list[tuple[int, int, FactionId]] = []
    for fid in state.turn_order:
        pl = state.players[fid]
        if fid == FactionId.SWIETE_OFICJUM:
            progress = pl.stacks
        elif fid == FactionId.CIENIE_AL_ANDALUS:
            progress = pl.relics_evacuated
        elif fid == FactionId.KORONA_BORGIOWIE:
            progress = pl.decrees_played + distinct_hook_victims(state, fid)
        elif fid == FactionId.KABALA_TOLEDO:
            progress = pl.fragments
        else:
            progress = pl.falls
        scores.append((progress, -pl.heresy, fid))
    scores.sort(reverse=True)
    return scores[0][2]
