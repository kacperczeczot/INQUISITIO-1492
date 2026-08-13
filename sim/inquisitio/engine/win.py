"""Victory checks — faction political goals with parameterized overrides."""
from __future__ import annotations

from inquisitio.engine.hooks import distinct_hook_victims, distinct_hook_victims_ever
from inquisitio.engine.state import FactionId, GameState, heresy_zone


def check_winner(state: GameState, win_overrides: dict | None = None) -> FactionId | None:
    ov = win_overrides or {}
    n_players = len(state.turn_order)

    for fid in state.turn_order:
        pl = state.players[fid]

        if fid == FactionId.SWIETE_OFICJUM:
            if state.layer == "C":
                base_stack = 5 if n_players >= 5 else 3
            else:
                base_stack = 3 if state.layer == "A" else (2 if n_players <= 3 else 3)
            stack_need = max(1, base_stack + ov.get("so_stacks_offset", 0))

            base_condemn = 4 if n_players >= 5 else (3 if n_players == 4 else 2)
            condemn_need = max(1, base_condemn + ov.get("so_condemns_offset", 0))
            condemn_ok = (state.layer != "B" and len(pl.condemned_rivals) >= condemn_need)

            if pl.stacks >= stack_need or condemn_ok:
                return fid

        elif fid == FactionId.CIENIE_AL_ANDALUS:
            base_era = (5 if n_players >= 4 else 6) + ov.get("caa_era_offset", 0)
            path_ok = (
                pl.path_via_double
                or pl.avoided_autodafe
                or state.sea_route_open
                or (n_players >= 4 and state.era >= base_era)
            )
            relic_need = 2
            if "caa_relics" in ov:
                relic_need = ov["caa_relics"]
            elif "caa_relics_5p" in ov and n_players >= 5:
                relic_need = ov["caa_relics_5p"]

            if state.layer == "A":
                if pl.relics_evacuated >= relic_need and state.era >= 5:
                    return fid
            elif pl.relics_evacuated >= relic_need and (path_ok or n_players >= 5):
                return fid

        elif fid == FactionId.KORONA_BORGIOWIE:
            hooks_ever = distinct_hook_victims_ever(state, fid)
            base_era = (6 if n_players <= 3 else 5) + ov.get("kb_era_offset", 0)
            decrees_need = ov.get("kb_decrees_3p", 2) if n_players <= 3 else 2
            hooks_need = ov.get("kb_hooks", 1)

            if (
                state.layer == "C"
                and pl.decrees_played >= decrees_need
                and hooks_ever >= hooks_need
                and state.era >= base_era
            ):
                return fid
            if (
                state.layer == "C"
                and n_players >= 4
                and pl.decrees_played >= 1
                and hooks_ever >= max(2, hooks_need)
                and state.era >= (6 + ov.get("kb_era_offset", 0))
            ):
                return fid

        elif fid == FactionId.KABALA_TOLEDO:
            frag_need = 2 if n_players >= 5 else 3
            if "kt_fragments" in ov:
                frag_need = ov["kt_fragments"]
            elif "kt_fragments_5p" in ov and n_players >= 5:
                frag_need = ov["kt_fragments_5p"]

            h_low, h_high = ov.get("kt_heresy_band", (3, 7))
            heresy_ok = (h_low <= pl.heresy <= h_high)
            base_era = (6 if n_players >= 4 else 7) + ov.get("kt_era_offset", 0)

            if state.layer == "A":
                pass
            elif state.layer == "B":
                if pl.fragments >= frag_need and heresy_ok and state.era >= max(1, base_era):
                    return fid
            elif pl.fragments >= frag_need and heresy_ok and state.era >= max(1, base_era):
                return fid

        elif fid == FactionId.GILDIA_CIENI:
            no_oficjum = FactionId.SWIETE_OFICJUM not in state.players
            base_falls = 3 if state.layer == "B" or no_oficjum or n_players >= 5 else 2
            falls_need = max(1, base_falls + ov.get("gc_falls_offset", 0))

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
