"""Victory checks — faction political goals."""
from __future__ import annotations

from inquisitio.engine.hooks import distinct_hook_victims, distinct_hook_victims_ever
from inquisitio.engine.state import FactionId, GameState, heresy_zone


def check_winner(state: GameState) -> FactionId | None:
    for fid in state.turn_order:
        pl = state.players[fid]
        if fid == FactionId.SWIETE_OFICJUM:
            # C: 4 Stosy dla 4-5p, 3 dla <=3p (zbięcie dominacji Oficjum)
            if state.layer == "C":
                stack_need = 5 if len(state.turn_order) >= 5 else (4 if len(state.turn_order) == 4 else 3)
            else:
                stack_need = 3 if state.layer == "A" else (
                    2 if len(state.turn_order) <= 3 else 3
                )
            condemn_need = 4 if len(state.turn_order) >= 5 else (3 if len(state.turn_order) == 4 else 2)
            condemn_ok = (
                state.layer != "B" and len(pl.condemned_rivals) >= condemn_need
            )
            if pl.stacks >= stack_need or condemn_ok:
                return fid
        elif fid == FactionId.CIENIE_AL_ANDALUS:
            path_ok = (
                pl.path_via_double
                or pl.avoided_autodafe
                or state.sea_route_open
                or (len(state.turn_order) >= 4 and state.era >= 6)
            )
            if state.layer == "A":
                if pl.relics_evacuated >= 2 and state.era >= 5:
                    return fid
            elif pl.relics_evacuated >= 2 and (path_ok or len(state.turn_order) >= 5):
                return fid
        elif fid == FactionId.KORONA_BORGIOWIE:
            hooks_ever = distinct_hook_victims_ever(state, fid)
            era_need = 7 if len(state.turn_order) <= 3 else 6
            if (
                state.layer == "C"
                and pl.decrees_played >= 2
                and hooks_ever >= 1
                and state.era >= era_need
            ):
                return fid
            if (
                state.layer == "C"
                and len(state.turn_order) >= 4
                and pl.decrees_played >= 1
                and hooks_ever >= 2
                and state.era >= 6
            ):
                return fid
        elif fid == FactionId.KABALA_TOLEDO:
            if state.layer == "A":
                pass
            elif state.layer == "B":
                if (
                    pl.fragments >= 3
                    and heresy_zone(pl.heresy) == "obserwowana"
                    and state.era >= 6
                ):
                    return fid
            elif (
                pl.fragments >= 3
                and heresy_zone(pl.heresy) == "obserwowana"
                and state.era >= (6 if len(state.turn_order) >= 4 else 7)
            ):
                return fid
        elif fid == FactionId.GILDIA_CIENI:
            no_oficjum = FactionId.SWIETE_OFICJUM not in state.players
            falls_need = 3 if state.layer == "B" or no_oficjum or len(state.turn_order) >= 5 else 2
            if pl.falls >= falls_need:
                return fid
    return None


def end_game_tiebreak(state: GameState) -> FactionId:
    """After max eras: closest to goal, then lowest heresy."""
    scores: list[tuple[int, int, FactionId]] = []
    for fid in state.turn_order:
        pl = state.players[fid]
        if fid == FactionId.SWIETE_OFICJUM:
            progress = max(pl.stacks, len(pl.condemned_rivals))
        elif fid == FactionId.CIENIE_AL_ANDALUS:
            progress = pl.relics_evacuated
        elif fid == FactionId.KORONA_BORGIOWIE:
            if state.layer == "A":
                progress = min(pl.decrees_played, 1) + min(
                    distinct_hook_victims_ever(state, fid), 1
                )
            elif state.layer == "B":
                progress = min(distinct_hook_victims(state, fid), 2)
            else:
                progress = pl.decrees_played + distinct_hook_victims_ever(state, fid)
        elif fid == FactionId.KABALA_TOLEDO:
            progress = pl.fragments
        else:
            if state.layer == "B":
                progress = min(pl.falls, 2)
            else:
                progress = pl.falls
        scores.append((progress, -pl.heresy, fid))
    scores.sort(reverse=True)
    return scores[0][2]
