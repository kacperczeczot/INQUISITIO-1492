"""Table verdict when heresy is critical."""
from __future__ import annotations

import random
from typing import Any

from inquisitio.config import CONFIG
from inquisitio.engine.heresy import add_heresy, is_critical
from inquisitio.engine.state import FactionId, GameState


def _cfg_int(item: Any, pc: str) -> int:
    if hasattr(item, "__getitem__") and not isinstance(item, (str, bytes)):
        try:
            return int(item[pc])
        except (KeyError, TypeError):
            pass
    return int(item)


def oficjum_snowball_threat(state: GameState) -> bool:
    """True when Oficjum is 1 shy of a dual-win — table may pile on.

    Early 2 stacks / 1 unique name is *not* a snowball: that was starving
    the condemns path so stacks from repeat verdicts finished first.
    """
    so = state.players.get(FactionId.SWIETE_OFICJUM)
    if not so:
        return False
    pc = f"{len(state.turn_order)}p"
    stacks_need = _cfg_int(CONFIG.victory.swiete_oficjum.stacks, pc)
    condemns_need = _cfg_int(CONFIG.victory.swiete_oficjum.condemns, pc)
    return so.stacks >= max(1, stacks_need - 1) or len(so.condemned_rivals) >= max(
        1, condemns_need - 1
    )


def eligible_accused(state: GameState) -> list[FactionId]:
    if state.active_time_edict == "time-08":
        return []
    threshold = state.accusation_threshold
    if state.active_time_edict == "time-05":
        threshold = max(1, threshold - 1)
    return [
        fid
        for fid, pl in state.players.items()
        if is_critical(pl, threshold) and fid not in state.accused_this_era
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
    if accused in state.accused_this_era:
        return False
    state.accused_this_era.add(accused)
    state.metrics.accusations += 1
    votes_burn = 0
    votes_spare = 0
    so_near_win = oficjum_snowball_threat(state)
    sys = state.sys_overrides or {}
    for fid in state.turn_order:
        if fid == accused:
            continue
        accused_h = state.players[accused].heresy
        # Table politics: cut Oficjum snowball; pile on Oficjum when they lead
        if accused == FactionId.SWIETE_OFICJUM and so_near_win:
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

    # ── Reaction: gc-05 (Fałszywy Świadek) ──
    # Trigger: after_verdict_majority_revealed (Gildia Cieni alters 1 vote)
    if FactionId.GILDIA_CIENI in state.players:
        gc_pl = state.players[FactionId.GILDIA_CIENI]
        if "gc-05" in gc_pl.hand:
            from inquisitio.cards.loader import load_all_cards
            cards = load_all_cards(card_overrides=sys.get("card_overrides"))
            gc_card = cards.get("gc-05")
            gc_cost = max(0, gc_card.cost + sys.get("card_cost_offset", 0)) if gc_card else 0
            if gc_pl.gold >= gc_cost:
                # Case 1: Accused is Gildia Cieni and would be convicted -> save own agent
                if accused == FactionId.GILDIA_CIENI and votes_burn > votes_spare:
                    gc_pl.gold -= gc_cost
                    gc_pl.hand.remove("gc-05")
                    gc_pl.discard.append("gc-05")
                    state.metrics.card_plays["gc-05"] = state.metrics.card_plays.get("gc-05", 0) + 1
                    votes_burn -= 1
                    votes_spare += 1
                    state.add_log(
                        f"gildia-cieni reaction gc-05 (Fałszywy Świadek) changed vote to spare: burn={votes_burn} spare={votes_spare}"
                    )
                # Case 2: Accused is a rival with Hook and 1 vote is needed to convict
                elif accused != FactionId.GILDIA_CIENI and accused in gc_pl.hook_victims_ever and votes_burn <= votes_spare:
                    gc_pl.gold -= gc_cost
                    gc_pl.hand.remove("gc-05")
                    gc_pl.discard.append("gc-05")
                    state.metrics.card_plays["gc-05"] = state.metrics.card_plays.get("gc-05", 0) + 1
                    votes_spare -= 1
                    votes_burn += 1
                    state.add_log(
                        f"gildia-cieni reaction gc-05 (Fałszywy Świadek) changed vote to burn: burn={votes_burn} spare={votes_spare}"
                    )

    convicted = votes_burn > votes_spare
    state.add_log(
        f"Verdict {accuser.value}->{accused.value}: "
        f"burn={votes_burn} spare={votes_spare} => {'CONVICT' if convicted else 'SPARE'}"
    )
    if convicted:
        state.metrics.convictions += 1
        add_heresy(state, accused, 1, reason="verdict_convict")
        from inquisitio.engine.dungeon import arrest_agent

        arrest_agent(state, accused)
        if FactionId.SWIETE_OFICJUM in state.players:
            so_pl = state.players[FactionId.SWIETE_OFICJUM]
            # Unikalne skazania: każdy Werdykt na rywalu (stół może karmić 3 Skazania).
            # Stos z Werdyktu: tylko oskarżenie Oficjum (powtórka też) — stół nie
            # dobija 5 stosów przy okazji.
            if accused != FactionId.SWIETE_OFICJUM:
                so_pl.condemned_rivals.add(accused)
            if accuser == FactionId.SWIETE_OFICJUM and accused != FactionId.SWIETE_OFICJUM:
                so_pl.stacks += 1
        # Gildia fall: Hak-victim convicted → Upadek
        if FactionId.GILDIA_CIENI in state.players and accused != FactionId.GILDIA_CIENI:
            gp = state.players[FactionId.GILDIA_CIENI]
            leveraged = accused in gp.hook_victims_ever
            if leveraged:
                gp.falls += 1
                state.add_log(f"gildia-cieni fall via hooked verdict (total={gp.falls})")
        # mark fall for gildia tracking if hook/double context — handled elsewhere
    else:
        add_heresy(state, accuser, 1, reason="failed_accusation")
    return convicted
