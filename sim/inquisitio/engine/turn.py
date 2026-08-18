"""Turn / era loop."""
from __future__ import annotations

import random

from inquisitio.cards.loader import load_all_cards
from inquisitio.config import CONFIG
from inquisitio.engine.variants import variant_bool, variant_int
from inquisitio.engine.card_conditions import card_condition_met
from inquisitio.engine.dungeon import interrogate, move_controlled_marionette
from inquisitio.engine.effects.registry import (
    optional_agent_step,
    play_card,
    resolve_pending_plays,
    resolve_time_edict,
)
from inquisitio.engine.hooks import active_hook_targets, distinct_hook_victims, force_hook
from inquisitio.engine.inquisitor import can_autodafe, era_start_inquisitor
from inquisitio.engine.state import FactionId, GameState
from inquisitio.engine.table_ai import (
    choose_naslanie_target,
    choose_patrol_dest,
    interrogate_prefer,
    is_naslanie_card,
    lowest_heresy_chooser,
    resolve_naslanie_winner,
    should_accuse,
    should_announce_autodafe,
    victim_complies_hook,
)
from inquisitio.engine.verdict import eligible_accused, oficjum_snowball_threat, run_verdict
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


def _sea_route_era_threshold(state: GameState) -> int:
    if "sea_route_era" in (state.sys_overrides or {}):
        return max(1, variant_int(state, "sea_route_era", 4))
    off = (state.sys_overrides or {}).get("sea_route_era_offset")
    base = int(getattr(CONFIG.variants, "sea_route_era", 4))
    if off is not None:
        return max(1, base + int(off))
    return max(1, base)


def _maybe_open_sea_route(state: GameState) -> None:
    """SSOT variants.sea_route_era — scheduled opening (Kronika time-03 still stacks)."""
    if state.sea_route_open:
        return
    threshold = _sea_route_era_threshold(state)
    if threshold >= 90:
        return
    if state.era >= threshold:
        state.sea_route_open = True
        state.add_log(f"Sea route open (era {state.era} ≥ {threshold})")


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
        pl.used_puppet_move = False
    state.pending_plays.clear()
    state.accused_this_era.clear()


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
        curfew_cost = 1 if (state.active_time_edict == "time-02" and c.location in ("rynek", "gildia")) else 0
        cost = max(0, c.cost + card_cost_offset + sig_offset + curfew_cost)
        if pl.gold >= cost:
            raw = c.raw if isinstance(c.raw, dict) else {}
            if cid == "kb-10" and raw.get("condition") and not card_condition_met(state, fid, c):
                continue
            legal.append(cid)
    return legal


def intrigue_gold_amount(state: GameState, fid: FactionId) -> int:
    """Akcja Gospodarcza: YAML intrigue_gold; Jarmark (time-09) na Rynku = 2."""
    sys = state.sys_overrides or {}
    if "intrigue_gold_offset" in sys:
        base = max(0, CONFIG.intrigue_gold() + int(sys["intrigue_gold_offset"]))
    else:
        base = int(sys.get("intrigue_gold", CONFIG.intrigue_gold()))
    pl = state.players[fid]
    on_rynek = any(ag.location == "rynek" and not ag.arrested for ag in pl.agents)
    if state.active_time_edict == "time-09" and on_rynek:
        return max(base, 2)
    return base


def take_economic_action(
    state: GameState,
    fid: FactionId,
    rng: random.Random,
    *,
    move_agent: bool = True,
) -> int:
    """Opcja B: opcjonalny ruch Agenta, potem złoto z banku."""
    if move_agent:
        optional_agent_step(state, fid, rng)
    amt = intrigue_gold_amount(state, fid)
    pl = state.players[fid]
    pl.gold += amt
    state.add_log(f"{fid.value} economic action +{amt} gold (now {pl.gold})")
    return amt


def _maybe_force_hook(state: GameState, fid: FactionId, rng: random.Random) -> None:
    if state.players[fid].used_hook:
        return
    pl = state.players[fid]
    if any(sp.owner == fid and sp.card_id == "kb-10" for sp in state.pending_plays):
        return
    if (
        fid == FactionId.KORONA_BORGIOWIE
        and "kb-10" in pl.hand
        and distinct_hook_victims(state, fid) >= 2
    ):
        return
    targets = active_hook_targets(state, fid)
    if not targets:
        return
    t = targets[0]
    force_hook(state, fid, t, comply=victim_complies_hook(state, t))


def _phase_ii_interrogations(state: GameState, rng: random.Random) -> None:
    """1 przesłuchanie / gracza / erę, gdy masz Agenta w Lochach i areszt rywala."""
    for fid in state.turn_order:
        pl = state.players[fid]
        if pl.used_interrogation:
            continue
        if not any(ag.location == "lochy" for ag in pl.agents):
            continue
        victims = [
            x
            for x in state.turn_order
            if x != fid and any(ag.arrested for ag in state.players[x].agents)
        ]
        if not victims:
            continue
        interrogate(state, fid, victims[0], rng, prefer=interrogate_prefer(fid))


def _phase_ii_inquisitor(state: GameState, rng: random.Random) -> None:
    sys = state.sys_overrides or {}
    cards = load_all_cards(card_overrides=sys.get("card_overrides"))
    declarations: dict[FactionId, str] = {}
    for sp in state.pending_plays:
        card = cards.get(sp.card_id)
        if not card or not is_naslanie_card(card):
            continue
        pl = state.players[sp.owner]
        if pl.used_inquisitor_send:
            continue
        declarations[sp.owner] = sp.location
        pl.used_inquisitor_send = True
        pl.inquisitor_send_count += 1
        state.add_log(f"{sp.owner.value} nasłanie (karta) → {sp.location}")
    for fid in state.turn_order:
        if state.players[fid].used_inquisitor_send:
            continue
        t = choose_naslanie_target(state, fid)
        if not t:
            continue
        declarations[fid] = t
        state.players[fid].used_inquisitor_send = True
        state.players[fid].inquisitor_send_count += 1
        state.add_log(f"{fid.value} nasłanie → {t}")
    win = resolve_naslanie_winner(state, declarations)
    toward = None
    dest = None
    if win:
        toward = win[1]
        state.add_log(f"nasłanie wins: {win[0].value} → {win[1]}")
    else:
        chooser = lowest_heresy_chooser(state)
        dest = choose_patrol_dest(state, chooser)
        state.add_log(f"patrol choice ({chooser.value}, lowest heresy) → {dest}")
    era_start_inquisitor(
        state,
        rng,
        toward=toward,
        dest=dest,
        announce_autodafe=False,
    )
    if should_announce_autodafe(state) and can_autodafe(state):
        from inquisitio.engine.inquisitor import resolve_autodafe
        resolve_autodafe(state)


def play_era(
    state: GameState,
    rng: random.Random,
    agent_choose,
    win_overrides: dict | None = None,
) -> FactionId | None:
    """One era — 3 Phases: I Intryga, II Sąd, III Kronika."""
    sys = state.sys_overrides or {}
    state.metrics.eras += 1
    state.eras_since_autodafe += 1
    _maybe_open_sea_route(state)
    _reset_era_flags(state)

    # ══════════════════════════════════════════════════════════════
    # FAZA I: INTRYGA (zakryta karta LUB Akcja Gospodarcza)
    # ══════════════════════════════════════════════════════════════
    if "cards_per_era_offset" in sys:
        n_rounds = max(1, int(CONFIG.system.cards_per_era) + int(sys["cards_per_era_offset"]))
    else:
        n_rounds = max(1, int(sys.get("cards_per_era", CONFIG.system.cards_per_era)))
    for round_num in range(n_rounds):
        for fid in state.turn_order:
            legal = _legal_card_ids(state, fid)
            state.metrics.legal_moves_sampled += len(legal)
            if not legal:
                state.metrics.forced_passes += 1
                take_economic_action(state, fid, rng)
            else:
                choice = agent_choose(state, fid, legal)
                if choice:
                    play_card(state, fid, choice, rng, resolve=False)
                    optional_agent_step(state, fid, rng)
                else:
                    take_economic_action(state, fid, rng)
            move_controlled_marionette(state, fid)
            _maybe_force_hook(state, fid, rng)

    # ══════════════════════════════════════════════════════════════
    # FAZA II: SĄD (Inkwizytor → Odkrycie → Lochy → Dwór)
    # ══════════════════════════════════════════════════════════════
    _phase_ii_inquisitor(state, rng)
    resolve_pending_plays(state, rng)
    _phase_ii_interrogations(state, rng)

    for fid in state.turn_order:
        accused_list = [a for a in eligible_accused(state) if a != fid]
        if accused_list and should_accuse(state, fid, accused_list):
            so = state.players.get(FactionId.SWIETE_OFICJUM)
            so_near = oficjum_snowball_threat(state)
            condemned = so.condemned_rivals if so else set()
            fresh = [a for a in accused_list if a not in condemned]
            if so_near and FactionId.SWIETE_OFICJUM in accused_list:
                target = FactionId.SWIETE_OFICJUM
            elif fid == FactionId.SWIETE_OFICJUM and fresh:
                target = fresh[0]
            else:
                pool = fresh or accused_list
                target = pool[0]
            run_verdict(state, fid, target, rng)
        w = check_winner(state, win_overrides)
        if w:
            state.winner = w
            state.add_log(f"WINNER {w.value}")
            return w

    # ══════════════════════════════════════════════════════════════
    # FAZA III: KRONIKA & CZYSTKA (Cele, Uzupełnienie, Edykt Czasu)
    # ══════════════════════════════════════════════════════════════
    res = check_winner_details(state, win_overrides)
    if res:
        state.winner = res[0]
        state.win_path = res[1]
        state.add_log(f"WINNER {res[0].value} via {res[1]}")
        return res[0]

    # 1. Dobierz do limitu ręki + dochód fazy III
    if "era_income_offset" in sys:
        income = max(0, CONFIG.era_income() + int(sys["era_income_offset"]))
    else:
        income = int(sys.get("era_income", CONFIG.era_income()))
    n_players = len(state.turn_order)
    hl = sys.get("hand_limit", CONFIG.hand_limit_for(n_players))
    if "hand_limit_offset" in sys:
        hl = max(1, CONFIG.hand_limit_for(n_players) + int(sys["hand_limit_offset"]))
    for fid in state.turn_order:
        pl = state.players[fid]
        need = max(0, int(hl) - len(pl.hand))
        if need:
            _draw(state, fid, need)
        while len(pl.hand) > hl:
            pl.discard.append(pl.hand.pop(0))
        pl.gold += income
        state.add_log(f"{fid.value} end of era upkeep: +{income} gold (now {pl.gold})")

    # 2. Odkrycie Edyktu Kroniki Dziejów (obowiązującego w nadchodzącej Erze)
    freq = variant_int(state, "time_deck_freq", int(CONFIG.variants.time_deck_freq))
    if (
        state.layer == "C"
        and state.time_deck
        and (state.era % freq == 0)
        and not variant_bool(state, "no_time_deck", False)
    ):
        state.active_time_edict = None
        edict = state.time_deck.pop()
        resolve_time_edict(state, edict, rng)
        state.time_discard.append(edict)

    # 3. Przesuń 1. gracza
    if len(state.turn_order) > 1:
        state.turn_order = state.turn_order[1:] + state.turn_order[:1]
        state.add_log(f"first player → {state.turn_order[0].value}")

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
