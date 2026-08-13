"""Turn / era loop."""
from __future__ import annotations

import random

from inquisitio.cards.loader import load_all_cards
from inquisitio.config import CONFIG
from inquisitio.engine.effects.registry import play_card, resolve_time_edict
from inquisitio.engine.heresy import is_critical
from inquisitio.engine.hooks import active_hook_targets, force_hook
from inquisitio.engine.inquisitor import era_start_inquisitor
from inquisitio.engine.state import FactionId, GameState
from inquisitio.engine.verdict import eligible_accused, run_verdict
from inquisitio.engine.win import check_winner, check_winner_details, end_game_tiebreak



def _draw(state: GameState, fid: FactionId, n: int = 1) -> None:
    pl = state.players[fid]
    for _ in range(n):
        if not pl.deck:
            pl.deck = list(pl.discard)
            pl.discard.clear()
            if not pl.deck:
                return
            # reshuffle handled by caller rng externally — simple reverse
            pl.deck = pl.deck[::-1]
        pl.hand.append(pl.deck.pop())


def _reset_era_flags(state: GameState) -> None:
    for pl in state.players.values():
        pl.used_hook = False
        pl.used_interrogation = False
        pl.used_inquisitor_send = False
        pl.used_kurier = False
        pl.inquisitor_send_count = 0
        pl.interrogate_count = 0
        pl.kurier_count = 0
        pl.vote_change_count = 0


def _legal_card_ids(state: GameState, fid: FactionId) -> list[str]:
    sys = state.sys_overrides or {}
    cards = load_all_cards(card_overrides=sys.get("card_overrides"))
    pl = state.players[fid]
    legal = []
    card_cost_offset = sys.get("card_cost_offset", CONFIG.economy.card_cost_offset)
    for cid in pl.hand:
        c = cards.get(cid)
        if not c:
            continue
        if c.type == "reakcja":
            continue
        sig_offset = sys.get("sig_cost_offset", CONFIG.economy.sig_cost_offset) if (c.breaks_rule or c.type == "signature") else 0
        cost = max(0, c.cost + card_cost_offset + sig_offset)
        if pl.gold >= cost:
            legal.append(cid)
    return legal


def play_era(
    state: GameState,
    rng: random.Random,
    agent_choose,
    win_overrides: dict | None = None,
) -> FactionId | None:
    """One era. agent_choose(state, fid, legal_ids) -> card_id | None."""
    sys = state.sys_overrides or {}
    state.metrics.eras += 1
    state.eras_since_autodafe += 1
    _reset_era_flags(state)
    era_start_inquisitor(state, rng)

    # Phase E.II — Plan / Intryga (2 rounds of card play or pass)
    for round_num in range(2):
        for fid in state.turn_order:
            pl = state.players[fid]
            if round_num == 0:
                pl.gold += 1
                state.add_log(f"{fid.value} gold trickle +1 (now {pl.gold})")
            legal = _legal_card_ids(state, fid)
            state.metrics.legal_moves_sampled += len(legal)
            if not legal:
                state.metrics.forced_passes += 1
                state.add_log(f"{fid.value} pass (no legal cards)")
            else:
                choice = agent_choose(state, fid, legal)
                if choice:
                    play_card(state, fid, choice, rng)
                else:
                    state.add_log(f"{fid.value} pass (savings)")

    for fid in state.turn_order:
        # optional hook force (A teach has Haki on kb/gc cards)
        if state.layer in ("A", "B", "C"):
            targets = active_hook_targets(state, fid)
            force_p = 0.35 if state.layer == "A" else 0.4
            if targets and not state.players[fid].used_hook and rng.random() < force_p:
                t = targets[0]
                # victim complies if heresy would hurt more
                comply = state.players[t].heresy >= 6 or rng.random() < 0.55
                force_hook(state, fid, t, comply=comply)
        # accusation — table politics vs Oficjum snowball
        accused_list = [a for a in eligible_accused(state) if a != fid]
        if accused_list:
            so = state.players.get(FactionId.SWIETE_OFICJUM)
            so_near = bool(
                so and (so.stacks >= 2 or len(so.condemned_rivals) >= 1)
            )
            # Prefer accusing Oficjum when they lead; otherwise random critical
            if so_near and FactionId.SWIETE_OFICJUM in accused_list:
                target = FactionId.SWIETE_OFICJUM
                p_acc = 0.7
            elif so_near:
                target = accused_list[0]
                p_acc = 0.25  # avoid feeding free Stosy
            else:
                target = accused_list[0]
                p_acc = 0.5
            if rng.random() < p_acc:
                run_verdict(state, fid, target, rng)
        w = check_winner(state)
        if w:
            state.winner = w
            state.add_log(f"WINNER {w.value}")
            return w
        _draw(state, fid, 1)
        # hand size soft cap
        pl = state.players[fid]
        while len(pl.hand) > 6:
            pl.discard.append(pl.hand.pop(0))

    # Cienie evacuate (B/C passive; A: second Relic after Kurier)
    if FactionId.CIENIE_AL_ANDALUS in state.players:
        pl = state.players[FactionId.CIENIE_AL_ANDALUS]
        evacuated = False
        harbor = ("rynek", "gildia")
        sea_era = sys.get("sea_route_era", CONFIG.variants.sea_route_era)
        if state.layer == "C" and (state.sea_route_open or state.era >= sea_era):
            for loc in harbor:
                if state.relics_on_board.get(loc, 0) > 0 and any(
                    ag.location == loc and not ag.arrested for ag in pl.agents
                ):
                    state.relics_on_board[loc] -= 1
                    pl.relics_evacuated += 1
                    pl.avoided_autodafe = True
                    evacuated = True
                    state.add_log(
                        f"cienie-al-andalus sea evacuate from {loc} "
                        f"(total={pl.relics_evacuated})"
                    )
                    break
        if not evacuated and state.layer in ("A", "B", "C"):
            if state.layer == "A" and pl.relics_evacuated < 1:
                chance = 0.0  # A: first Relic must be Kurier
            elif state.layer == "A":
                chance = 0.70  # second Relic after Kurier
            elif state.layer == "B":
                chance = 0.15
            else:
                chance = 0.32  # C: Cienie ~50% w Oficjum–Cienie–Gildia / multi-seed
            for loc in harbor:
                if chance <= 0:
                    break
                if state.relics_on_board.get(loc, 0) <= 0:
                    continue
                if state.inquisitor_location == loc:
                    continue
                if not any(ag.location == loc and not ag.arrested for ag in pl.agents):
                    continue
                if rng.random() >= chance:
                    break
                state.relics_on_board[loc] -= 1
                pl.relics_evacuated += 1
                pl.avoided_autodafe = True
                state.add_log(
                    f"cienie-al-andalus quiet harbor evacuate from {loc} "
                    f"(total={pl.relics_evacuated})"
                )
                break

    # time edict layer C
    freq = sys.get("time_deck_freq", CONFIG.variants.time_deck_freq)
    if state.layer == "C" and state.time_deck and (state.era % freq == 0):
        edict = state.time_deck.pop()
        resolve_time_edict(state, edict, rng)
        state.time_discard.append(edict)

    res = check_winner_details(state, win_overrides)
    if res:
        state.winner = res[0]
        state.win_path = res[1]
        state.add_log(f"WINNER {res[0].value} via {res[1]}")
        return res[0]
    return None


def play_game(
    state: GameState,
    rng: random.Random,
    agent_choose,
    win_overrides: dict | None = None,
) -> FactionId:
    while state.era <= state.max_eras and state.winner is None:
        play_era(state, rng, agent_choose, win_overrides=win_overrides)
        if state.winner:
            return state.winner
        if state.era >= state.max_eras:
            break
        state.era += 1
    if state.winner:
        return state.winner
    state.winner = end_game_tiebreak(state)
    state.win_path = "tiebreak"
    state.add_log(f"TIEBREAK WINNER {state.winner.value}")
    return state.winner


