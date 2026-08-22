"""Politics agent — Intelligent Utility AI with Economic ROI, Heresy Risk, and Strategic Passing."""
from __future__ import annotations

import random

from inquisitio.cards.loader import Card, load_all_cards
from inquisitio.config import CONFIG
from inquisitio.engine.card_conditions import card_condition_met
from inquisitio.engine.state import FactionId, GameState
from inquisitio.engine.verdict import oficjum_snowball_threat


class PoliticsAgent:
    def __init__(self, rng: random.Random):
        self.rng = rng

    def choose_card(self, state: GameState, faction: FactionId, legal: list[str]) -> str | None:
        if not legal:
            return None

        sys = state.sys_overrides or {}
        cards = load_all_cards(card_overrides=sys.get("card_overrides"))
        pl = state.players[faction]

        card_cost_offset = sys.get("card_cost_offset", CONFIG.economy.card_cost_offset)
        sig_offset_val = sys.get("sig_cost_offset", CONFIG.economy.sig_cost_offset)
        threshold = state.accusation_threshold

        def _effective_cost(c: Card) -> int:
            s_off = sig_offset_val if (c.breaks_rule or c.type == "signature") else 0
            curfew_cost = 1 if (state.active_time_edict == "time-02" and c.location in ("rynek", "gildia")) else 0
            return max(0, c.cost + card_cost_offset + s_off + curfew_cost)

        # ── 1. Value of Akcja Gospodarcza (always legal; pays gold now) ──
        v_econ = 0.35
        if "intrigue_gold_offset" in sys:
            econ_gold = max(0, CONFIG.intrigue_gold() + int(sys["intrigue_gold_offset"]))
        else:
            econ_gold = int(sys.get("intrigue_gold", CONFIG.intrigue_gold()))
        on_rynek = any(ag.location == "rynek" and not ag.arrested for ag in pl.agents)
        if state.active_time_edict == "time-09" and on_rynek:
            econ_gold = max(econ_gold, 2)
        v_econ = econ_gold * 1.8 + 0.8  # gold now + optional agent step

        # Finisher one gold short: Gospodarcza this round funds it (same era or next)
        finishers = [
            cards[cid] for cid in pl.hand
            if cards.get(cid) and (
                cards[cid].type == "signature"
                or "autodafe" in cards[cid].tags
                or "relic" in cards[cid].tags
                or "decree" in cards[cid].tags
                or "fragment" in cards[cid].tags
            )
        ]
        for fin in finishers:
            fin_cost = _effective_cost(fin)
            if fin_cost > pl.gold and (pl.gold + econ_gold >= fin_cost):
                v_econ = max(v_econ, 2.5)
                break

        if pl.gold <= 1:
            v_econ = max(v_econ, 0.8 + econ_gold * 1.8)

        # ── 2. Utility Evaluation for Each Legal Card ──
        scored: list[tuple[float, str]] = []

        for cid in legal:
            c = cards.get(cid)
            if not c:
                continue

            eff_cost = _effective_cost(c)
            u = 0.0

            # ── A. Economic Utility (Net ROI) ──
            if c.gold > 0:
                net_gold = c.gold - eff_cost
                # If a card yields net negative gold and provides NO other tangible mechanical effect:
                has_other_effects = bool(
                    c.agents > 0 or c.creates_hook or c.arrest or c.target_heresy > 0
                    or "interrogation" in c.tags or "relic" in c.tags or "decree" in c.tags
                    or "fragment" in c.tags or "fall" in c.tags or "inquisitor" in c.tags
                    or c.type == "signature" or c.breaks_rule
                )
                if net_gold < 0 and not has_other_effects:
                    # Strictly irrational self-harm (e.g. paying 2g for 1g)
                    u -= 15.0
                else:
                    u += net_gold * 1.8
            else:
                # Paying gold for effects: deduct gold opportunity cost
                u -= eff_cost * 0.9
                if pl.gold <= eff_cost and eff_cost > 0:
                    u -= 0.5  # Emptying vault carries friction

            # ── B. Heresy Risk & Zone Dynamics ──
            post_h = pl.heresy + c.heresy
            has_so = FactionId.SWIETE_OFICJUM in state.players and faction != FactionId.SWIETE_OFICJUM
            autodafe_near = has_so and state.eras_since_autodafe >= (state.autodafe_cooldown - 1)

            if post_h >= threshold:
                u -= c.heresy * 4.5  # Direct Court Execution
            elif post_h >= threshold - 1:
                u -= c.heresy * 2.5  # Critical 1 step from execution
            elif has_so and post_h >= state.observed_threshold:
                # Danger of Autodafe burning & condemnation
                if autodafe_near:
                    u -= c.heresy * 3.0  # Autodafe is ready — do not enter observed zone!
                else:
                    u -= c.heresy * 1.2  # Monitored by Inquisition
            else:
                u -= c.heresy * 0.35  # Safe zone heresy

            # ── C. Dynamic Threat Assessment & Table Politics (Anti-Leader Defense) ──
            threats: dict[FactionId, float] = {}
            for r_fid, r_pl in state.players.items():
                if r_fid == faction:
                    continue
                th = 0.0
                if r_fid == FactionId.SWIETE_OFICJUM:
                    condemns = len(r_pl.condemned_rivals)
                    if condemns >= 2:
                        th += 0.85  # 1 condemnation from victory
                    elif condemns == 1:
                        th += 0.4
                    if r_pl.stacks >= 5:
                        th += 0.75
                elif r_fid == FactionId.CIENIE_AL_ANDALUS:
                    if r_pl.relics_evacuated >= 1:
                        th += 0.85  # 1 relic from victory
                        if state.sea_route_open:
                            th += 0.25
                    elif any(state.relics_on_board.get(ag.location, 0) > 0 and not ag.arrested for ag in r_pl.agents):
                        th += 0.35
                elif r_fid == FactionId.KORONA_BORGIOWIE:
                    from inquisitio.engine.hooks import distinct_hook_victims
                    r_hooks = distinct_hook_victims(state, r_fid)
                    if r_hooks >= 2:
                        th += 0.85  # Threat of Pieczęć Korony (kb-10)
                    elif r_hooks == 1:
                        th += 0.35
                    if r_pl.decrees_played >= 1:
                        th += 0.3
                elif r_fid == FactionId.KABALA_TOLEDO:
                    if r_pl.fragments >= 2:
                        th += 0.75  # Full Codex held — impending Era 6 check
                    elif r_pl.fragments == 1 and state.era >= 4:
                        th += 0.30
                elif r_fid == FactionId.GILDIA_CIENI:
                    if r_pl.falls >= 7:
                        th += 0.85  # 1 fall from victory
                    elif r_pl.falls >= 5:
                        th += 0.45

                threats[r_fid] = th

            max_threat = max(threats.values()) if threats else 0.0

            # Table reacts against threatening leaders:
            if max_threat >= 0.5:
                # Confront leader via arrests, framing, and disruption
                if has_so:
                    # Inquisitor is present — heresy framing pushes leader into burning range
                    if c.target_heresy > 0:
                        u += 1.8 * max_threat
                    if c.arrest:
                        u += 2.2 * max_threat
                else:
                    # No Inquisition — physical arrests & interrogation are the true stop to leaders
                    if c.arrest:
                        u += 3.5 * max_threat
                    if "interrogation" in c.tags or c.creates_hook:
                        u += 2.2 * max_threat

                if "interrogation" in c.tags or c.creates_hook:
                    u += 1.2 * max_threat

            # Anti-snowball: If Oficjum is threatening, do not feed heresy
            so_threat = threats.get(FactionId.SWIETE_OFICJUM, 0.0)
            if so_threat >= 0.5 and c.target_heresy > 0:
                u -= c.target_heresy * 1.5

            # ── D. Board Presence & Agent Movement ──
            if c.agents > 0:
                u += c.agents * 0.8
                if faction == FactionId.CIENIE_AL_ANDALUS:
                    u += c.agents * 1.2

            # ── E. Control & Extortion (Arrests, Interrogations, Hooks) ──
            if c.arrest:
                u += 2.0
            if "interrogation" in c.tags:
                u += 2.2
            if c.creates_hook:
                if faction == FactionId.GILDIA_CIENI:
                    u += 3.8  # Upadki engine
                else:
                    u += 2.0

            # ── F. Faction-Specific Win Proximity (Pure Self-Pacing) ──
            if faction == FactionId.SWIETE_OFICJUM:
                if "autodafe" in c.tags:
                    if state.eras_since_autodafe >= state.autodafe_cooldown:
                        condemnable = sum(1 for f_id, p in state.players.items() if f_id != faction and p.heresy >= state.observed_threshold)
                        if condemnable >= 1:
                            u += 4.2 if pl.gold >= eff_cost else 1.5
                        else:
                            u += 2.2 if pl.gold >= eff_cost else 0.5
                    else:
                        u += 0.5
                if "inquisitor" in c.tags and not pl.used_inquisitor_send:
                    u += 2.0
                    # Inquisitor urgency scales if clandestine rivals (CAA, KT) threaten victory
                    clandestine_threat = max(threats.get(FactionId.CIENIE_AL_ANDALUS, 0.0), threats.get(FactionId.KABALA_TOLEDO, 0.0))
                    if clandestine_threat >= 0.5:
                        u += 1.2 * clandestine_threat

            elif faction == FactionId.CIENIE_AL_ANDALUS:
                relics_left = max(0, 2 - pl.relics_evacuated)
                if "relic" in c.tags:
                    u += 3.5
                    if pl.relics_evacuated >= 1:
                        u += 2.2
                    if state.sea_route_open and pl.relics_evacuated < 2:
                        u += 1.5
                if c.id == "caa-03":
                    on_relic = any(
                        state.relics_on_board.get(ag.location, 0) > 0 and not ag.arrested
                        for ag in pl.agents
                    )
                    if on_relic:
                        u += 3.5
                if c.id == "caa-09" and pl.relics_evacuated < 2:
                    u += 2.5
                if c.id == "caa-10":
                    if card_condition_met(state, faction, c) or state.sea_route_open:
                        u += 6.2 if pl.relics_evacuated >= 1 else 3.8
                    else:
                        u -= 18.0
                if c.id == "caa-05":  # Odnalezienie Relikwii
                    if not pl.used_kurier and pl.relics_evacuated < 2:
                        on_relic = any(
                            state.relics_on_board.get(ag.location, 0) > 0 and not ag.arrested
                            for ag in pl.agents
                        )
                        u += 4.5 if on_relic else 3.0
                if c.id == "caa-06":  # Bunt / Ucieczka z lochów
                    arrested_cnt = sum(1 for ag in pl.agents if ag.arrested)
                    if arrested_cnt >= 2:
                        u += 5.0
                    elif arrested_cnt == 1:
                        u += 3.5
                if c.id == "caa-02" and pl.gold <= 2:
                    u += 2.5  # Critical economic injection

            elif faction == FactionId.KORONA_BORGIOWIE:
                from inquisitio.engine.hooks import distinct_hook_victims

                active_hooks = distinct_hook_victims(state, faction)
                decrees_left = max(0, 2 - pl.decrees_played)

                if "decree" in c.tags:
                    u += 3.8
                    if decrees_left == 1 and active_hooks >= 2:
                        u += 3.5  # Decisive decree to win
                    elif decrees_left == 1:
                        u += 2.0

                if c.id == "kb-10":
                    if active_hooks >= 2:
                        u += 6.5 if pl.decrees_played >= 1 else 4.0
                    else:
                        u -= 20.0  # Need hooks first

                if c.id == "kb-09":
                    if pl.decrees_played < 2:
                        u += 2.5

                if c.creates_hook:
                    if active_hooks < 2:
                        u += 3.8 if active_hooks == 0 else 2.5
                    elif len(pl.hook_victims_ever) < 2:
                        u += 1.8

            elif faction == FactionId.KABALA_TOLEDO:
                frags_left = max(0, 2 - pl.fragments)
                if "fragment" in c.tags:
                    u += 3.8
                    if frags_left == 1:
                        u += 1.8

                if c.id == "kt-10":
                    if pl.fragments >= 2:
                        u += 6.2 if state.era >= 6 else 3.2
                    else:
                        u += 1.0

            elif faction == FactionId.GILDIA_CIENI:
                falls_left = max(0, 8 - pl.falls)
                if "fall" in c.tags or c.id == "gc-10":
                    u += 4.8
                    if falls_left <= 2:
                        u += 3.5  # Near victory (match point)
                    elif falls_left <= 4:
                        u += 1.5
                if c.creates_hook or c.id in ("gc-04", "gc-06", "gc-09"):
                    u += 3.5
                if c.id == "gc-07":
                    u += 1.5
                if c.id == "gc-02" and pl.gold <= 2:
                    u += 2.5  # Fund expensive falls

            if c.type == "signature":
                u += 2.0

            # Tie-breaking slight entropy
            u += self.rng.random() * 0.2
            scored.append((u, cid))

        scored.sort(reverse=True)

        # ── 3. Play card vs Akcja Gospodarcza (None → +gold, not a skip) ──
        best_u, best_cid = scored[0]
        if best_u < v_econ:
            return None

        return best_cid

