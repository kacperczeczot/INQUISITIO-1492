"""Table verdict when heresy is critical."""
from __future__ import annotations

import random

from inquisitio.engine.heresy import add_heresy, is_critical
from inquisitio.engine.state import FactionId, GameState


def eligible_accused(state: GameState) -> list[FactionId]:
    if state.active_time_edict == "time-08":
        return []
    threshold = state.accusation_threshold
    if state.active_time_edict == "time-05":
        threshold = max(1, threshold - 1)
    return [
        fid
        for fid, pl in state.players.items()
        if is_critical(pl, threshold)
    ]


def run_verdict(
    state: GameState,
    accuser: FactionId,
    accused: FactionId,
    rng: random.Random,
    double_vote: FactionId | None = None,
) -> bool:
    """Returns True if convicted."""
    if accused not in eligible_accused(state):
        return False
    if accuser == accused:
        return False
    state.metrics.accusations += 1
    votes_burn = 0
    votes_spare = 0
    so = state.players.get(FactionId.SWIETE_OFICJUM)
    so_near_win = bool(
        so and (so.stacks >= 2 or len(so.condemned_rivals) >= 1)
    )
    sys = state.sys_overrides or {}
    secret_verdict = sys.get("verdict_secret", False)
    for fid in state.turn_order:
        if fid == accused:
            continue
        accused_h = state.players[accused].heresy
        # Table politics: cut Oficjum snowball; pile on Oficjum when they lead
        if secret_verdict:
            prefer_burn = accused_h >= 7 or rng.random() < 0.40
        elif accused == FactionId.SWIETE_OFICJUM and so_near_win:
            prefer_burn = accused_h >= 7 or rng.random() < 0.65
        elif so_near_win and accused != FactionId.SWIETE_OFICJUM:
            prefer_burn = accused_h >= 9 or rng.random() < 0.22
        else:
            prefer_burn = accused_h >= 8 or rng.random() < 0.45
        weight = 2 if double_vote == fid else 1
        if prefer_burn:
            votes_burn += weight
        else:
            votes_spare += weight
    convicted = votes_burn > votes_spare
    state.add_log(
        f"Verdict {accuser.value}->{accused.value}: "
        f"burn={votes_burn} spare={votes_spare} => {'CONVICT' if convicted else 'SPARE'}"
    )
    if convicted:
        state.metrics.convictions += 1
        pl = state.players[accused]
        # remove one free agent to stack
        for ag in list(pl.agents):
            if not ag.arrested:
                pl.agents.remove(ag)
                break
        if FactionId.SWIETE_OFICJUM in state.players:
            so_pl = state.players[FactionId.SWIETE_OFICJUM]
            # B teach: Stos from Werdykt only if Oficjum oskarża (cuts 5p snowball)
            if state.layer != "B" or accuser == FactionId.SWIETE_OFICJUM:
                so_pl.stacks += 1
            if accused != FactionId.SWIETE_OFICJUM:
                so_pl.condemned_rivals.add(accused)
        # Gildia fall: accuse with leverage, or 40% if your Hak-victim is condemned by anyone
        if FactionId.GILDIA_CIENI in state.players and accused != FactionId.GILDIA_CIENI:
            gp = state.players[FactionId.GILDIA_CIENI]
            leveraged = accused in gp.hook_victims_ever
            p_fall = 0.25 if state.layer == "B" else 0.4
            if leveraged and (
                accuser == FactionId.GILDIA_CIENI or rng.random() < p_fall
            ):
                gp.falls += 1
                state.add_log(f"gildia-cieni fall via hooked verdict (total={gp.falls})")
        # mark fall for gildia tracking if hook/double context — handled elsewhere
    else:
        add_heresy(state, accuser, 1, reason="failed_accusation")
    return convicted
