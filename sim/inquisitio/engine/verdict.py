"""Table verdict when heresy is critical."""
from __future__ import annotations

import random

from inquisitio.engine.heresy import add_heresy, is_critical
from inquisitio.engine.state import FactionId, GameState


def eligible_accused(state: GameState) -> list[FactionId]:
    return [
        fid
        for fid, pl in state.players.items()
        if is_critical(pl, state.accusation_threshold)
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
    for fid in state.turn_order:
        if fid == accused:
            continue
        # politics: spare self-allies with low heresy; burn high threats
        accused_h = state.players[accused].heresy
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
            state.players[FactionId.SWIETE_OFICJUM].stacks += 1
        # mark fall for gildia tracking if hook/double context — handled elsewhere
    else:
        add_heresy(state, accuser, 1, reason="failed_accusation")
    return convicted
