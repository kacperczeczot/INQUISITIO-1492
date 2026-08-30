"""Victory checks — faction political goals with parameterized overrides."""
from __future__ import annotations
from typing import Any

from inquisitio.config import CONFIG
from inquisitio.engine.hooks import distinct_hook_victims, distinct_hook_victims_ever
from inquisitio.engine.state import FactionId, GameState


def _pc(n: int) -> str:
    """Player count key for CONFIG lookups."""
    return f"{n}p"


def _val(item: Any, pc: str) -> int:
    """Return integer value whether item is scalar or per-player-count dict."""
    if hasattr(item, "__getitem__") and not isinstance(item, (str, bytes)):
        try:
            return int(item[pc])
        except (KeyError, TypeError):
            pass
    return int(item)


def _gc_falls_need(falls: Any, ov: dict, *, no_oficjum: bool, layer: str = "C", pc: str = "4p") -> int:
    """One table-wide number or per-player-count dict. Legacy default/no_oficjum dict still reads for old YAML."""
    unified = int(ov.get("gc_falls_offset", 0) or 0)
    split_default = int(ov.get("gc_falls_default_offset", 0) or 0)
    split_noso = int(ov.get("gc_falls_no_oficjum_offset", 0) or 0)
    if hasattr(falls, "default"):
        raw = falls.no_oficjum if no_oficjum else falls.default
        split = split_noso if no_oficjum else split_default
        return max(1, int(raw) + split + unified)
    if isinstance(falls, dict):
        if "default" in falls or "no_oficjum" in falls:
            raw = falls["no_oficjum"] if no_oficjum else falls["default"]
            split = split_noso if no_oficjum else split_default
            return max(1, int(raw) + split + unified)
        raw = falls.get(pc, falls.get("4p", 9))
        return max(1, int(raw) + unified)
    if hasattr(falls, "__getitem__") and not isinstance(falls, (str, bytes)):
        try:
            return max(1, int(falls[pc]) + unified)
        except Exception:
            pass
    return max(1, int(falls) + unified + split_default + split_noso)


_VICTORY_CACHE: dict[str, dict[str, Any]] = {}


def _get_victory_base(pc: str) -> dict[str, Any]:
    global _VICTORY_CACHE
    if pc in _VICTORY_CACHE:
        return _VICTORY_CACHE[pc]
    cfg_v = CONFIG.victory
    data = {
        "so_stacks": _val(cfg_v.swiete_oficjum.stacks, pc),
        "so_condemns": _val(cfg_v.swiete_oficjum.condemns, pc),
        "caa_relics": _val(cfg_v.cienie_al_andalus.relics, pc),
        "kb_decrees": _val(cfg_v.korona_borgiowie.decrees, pc),
        "kb_hooks": _val(cfg_v.korona_borgiowie.get("hooks", 0), pc),
        "kt_frags": _val(cfg_v.kabala_toledo.fragments, pc),
        "kt_band": cfg_v.kabala_toledo.get("heresy_band") or [4, 6],
        "gc_falls_raw": cfg_v.gildia_cieni.falls,
    }
    _VICTORY_CACHE[pc] = data
    return data


def clear_victory_cache() -> None:
    _VICTORY_CACHE.clear()


def check_winner_details(state: GameState, win_overrides: dict | None = None) -> tuple[FactionId, str] | None:
    """Returns tuple of (winner_faction, win_path_id) or None."""
    ov = win_overrides or {}
    n_players = len(state.turn_order)
    pc = _pc(n_players)
    base = _get_victory_base(pc)

    for fid in state.turn_order:
        pl = state.players[fid]

        if fid == FactionId.SWIETE_OFICJUM:
            stack_need = max(1, base["so_stacks"] + ov.get("so_stacks_offset", 0))
            condemn_need = max(1, base["so_condemns"] + ov.get("so_condemns_offset", 0))
            condemn_ok = len(pl.condemned_rivals) >= condemn_need

            if condemn_ok:
                return (fid, "so_condemns")
            if pl.stacks >= stack_need:
                return (fid, "so_stacks")

        elif fid == FactionId.CIENIE_AL_ANDALUS:
            if "caa_relics" in ov:
                relic_need = ov["caa_relics"]
            elif "caa_relics_5p" in ov and n_players >= 5:
                relic_need = ov["caa_relics_5p"]
            else:
                relic_need = max(1, base["caa_relics"] + ov.get("caa_relics_offset", 0))

            if pl.relics_evacuated >= relic_need:
                if (
                    state.sea_route_open
                    or pl.path_via_double
                    or pl.avoided_autodafe
                    or pl.shadow_exit
                ):
                    return (fid, "caa_sea_route")

        elif fid == FactionId.KORONA_BORGIOWIE:
            hooks_active = distinct_hook_victims(state, fid)
            if "kb_decrees_3p" in ov and n_players <= 3:
                decrees_need = ov["kb_decrees_3p"]
            else:
                decrees_need = max(1, base["kb_decrees"] + ov.get("kb_decrees_offset", 0))
            if "kb_hooks" in ov:
                hooks_need = _val(ov["kb_hooks"], pc)
            else:
                hooks_need = max(0, base["kb_hooks"] + ov.get("kb_hooks_offset", 0))

            if (
                pl.decrees_played >= decrees_need
                and hooks_active >= hooks_need
            ):
                return (fid, "kb_main")

        elif fid == FactionId.KABALA_TOLEDO:
            if "kt_fragments" in ov:
                frag_need = _val(ov["kt_fragments"], pc)
            elif "kt_fragments_5p" in ov and n_players >= 5:
                frag_need = _val(ov["kt_fragments_5p"], pc)
            else:
                frag_need = max(1, base["kt_frags"] + ov.get("kt_frags_offset", 0))

            band = ov.get("kt_heresy_band", base["kt_band"])
            if band:
                h_low, h_high = int(band[0]), int(band[1])
                heresy_ok = h_low <= pl.heresy <= h_high
            else:
                heresy_ok = True

            if (
                getattr(pl, "kt10_played", False)
                and pl.fragments >= frag_need
                and heresy_ok
            ):
                return (fid, "kt_codex")

        elif fid == FactionId.GILDIA_CIENI:
            no_oficjum = FactionId.SWIETE_OFICJUM not in state.players
            falls_need = _gc_falls_need(
                base["gc_falls_raw"], ov, no_oficjum=no_oficjum, layer=getattr(state, "layer", "C"), pc=pc
            )

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
            progress = pl.decrees_played + distinct_hook_victims(state, fid)
        elif fid == FactionId.KABALA_TOLEDO:
            progress = pl.fragments
        else:
            progress = pl.falls
        scores.append((progress, -pl.heresy, fid))
    scores.sort(reverse=True)
    return scores[0][2]
