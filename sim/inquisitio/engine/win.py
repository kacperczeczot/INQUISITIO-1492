"""Victory checks — faction political goals with parameterized overrides."""
from __future__ import annotations

from inquisitio.config import CONFIG
from inquisitio.engine.hooks import distinct_hook_victims, distinct_hook_victims_ever
from inquisitio.engine.state import FactionId, GameState


def _pc(n: int) -> str:
    """Player count key for CONFIG lookups."""
    return f"{n}p"


def check_winner_details(state: GameState, win_overrides: dict | None = None) -> tuple[FactionId, str] | None:
    """Returns tuple of (winner_faction, win_path_id) or None."""
    ov = win_overrides or {}
    n_players = len(state.turn_order)
    pc = _pc(n_players)
    cfg_v = CONFIG.victory

    for fid in state.turn_order:
        pl = state.players[fid]

        if fid == FactionId.SWIETE_OFICJUM:
            if state.layer == "C":
                base_stack = cfg_v.swiete_oficjum.stacks[pc]
            else:
                base_stack = 3 if state.layer == "A" else (2 if n_players <= 3 else 3)
            stack_need = max(1, base_stack + ov.get("so_stacks_offset", 0))

            if state.layer == "C":
                base_condemn = cfg_v.swiete_oficjum.condemns[pc]
            else:
                base_condemn = 4 if n_players >= 5 else (3 if n_players == 4 else 2)
            condemn_need = max(1, base_condemn + ov.get("so_condemns_offset", 0))
            condemn_ok = (state.layer != "B" and len(pl.condemned_rivals) >= condemn_need)

            if pl.stacks >= stack_need:
                return (fid, "so_stacks")
            elif condemn_ok:
                return (fid, "so_condemns")

        elif fid == FactionId.CIENIE_AL_ANDALUS:
            cfg_caa = cfg_v.cienie_al_andalus
            base_era = cfg_caa.path_era[pc] + ov.get("caa_era_offset", 0)
            relic_need = max(1, cfg_caa.relics + ov.get("caa_relics_offset", 0))
            if "caa_relics" in ov:
                relic_need = ov["caa_relics"]
            elif "caa_relics_5p" in ov and n_players >= 5:
                relic_need = ov["caa_relics_5p"]

            if pl.relics_evacuated >= relic_need:
                if state.sea_route_open or pl.path_via_double or pl.avoided_autodafe:
                    return (fid, "caa_sea_route")
                elif state.era >= base_era:
                    return (fid, "caa_era")

        elif fid == FactionId.KORONA_BORGIOWIE:
            cfg_kb = cfg_v.korona_borgiowie
            hooks_ever = distinct_hook_victims_ever(state, fid)
            base_era = cfg_kb.era[pc] + ov.get("kb_era_offset", 0)
            if "kb_decrees_3p" in ov and n_players <= 3:
                decrees_need = ov["kb_decrees_3p"]
            else:
                decrees_need = max(1, int(cfg_kb.decrees[pc]) + ov.get("kb_decrees_offset", 0))
            if "kb_hooks" in ov:
                hooks_need = ov["kb_hooks"]
            else:
                hooks_need = max(0, int(cfg_kb.hooks[pc]) + ov.get("kb_hooks_offset", 0))

            if (
                state.layer == "C"
                and pl.decrees_played >= decrees_need
                and hooks_ever >= hooks_need
                and state.era >= base_era
            ):
                return (fid, "kb_main")

            # Alternative path (4p+)
            alt = cfg_kb.alt_path
            alt_min = alt.min_players + ov.get("kb_alt_min_players_offset", 0)
            alt_decrees = max(1, alt.decrees + ov.get("kb_alt_decrees_offset", 0))
            alt_hooks = max(0, alt.hooks + ov.get("kb_alt_hooks_offset", 0))
            alt_era = alt.era + ov.get("kb_alt_era_offset", ov.get("kb_era_offset", 0))
            if (
                state.layer == "C"
                and n_players >= alt_min
                and pl.decrees_played >= alt_decrees
                and hooks_ever >= max(alt_hooks, hooks_need)
                and state.era >= alt_era
            ):
                return (fid, "kb_alt")

        elif fid == FactionId.KABALA_TOLEDO:
            cfg_kt = cfg_v.kabala_toledo
            frag_need = max(1, cfg_kt.fragments[pc] + ov.get("kt_frags_offset", 0))
            if "kt_fragments" in ov:
                frag_need = ov["kt_fragments"]
            elif "kt_fragments_5p" in ov and n_players >= 5:
                frag_need = ov["kt_fragments_5p"]

            band = ov.get("kt_heresy_band", cfg_kt.heresy_band)
            h_low, h_high = band[0], band[1]
            heresy_ok = (h_low <= pl.heresy <= h_high)
            base_era = cfg_kt.era[pc] + ov.get("kt_era_offset", 0)

            if pl.fragments >= frag_need and heresy_ok and state.era >= max(1, base_era):
                return (fid, "kt_codex")

        elif fid == FactionId.GILDIA_CIENI:
            cfg_gc = cfg_v.gildia_cieni
            no_oficjum = FactionId.SWIETE_OFICJUM not in state.players
            if state.layer == "B" or no_oficjum:
                base_falls = cfg_gc.falls.no_oficjum + ov.get("gc_falls_no_oficjum_offset", 0)
            else:
                base_falls = cfg_gc.falls.default + ov.get("gc_falls_default_offset", 0)
            falls_need = max(1, base_falls + ov.get("gc_falls_offset", 0))

            if pl.falls >= falls_need:
                return (fid, "gc_falls")

    return None


def check_winner(state: GameState, win_overrides: dict | None = None) -> FactionId | None:
    res = check_winner_details(state, win_overrides)
    if res:
        state.winner = res[0]
        state.win_path = res[1]
        return res[0]
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
