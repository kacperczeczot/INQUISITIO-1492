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
            # Kabała nie ma pasma wygranej — Herezja to ten sam sąd co u reszty.
            post_h = pl.heresy + c.heresy
            if post_h >= threshold:
                u -= c.heresy * 4.0  # Walking into Court execution
            elif post_h >= threshold - 1:
                u -= c.heresy * 2.0  # Observed danger
            else:
                u -= c.heresy * 0.4  # Minor stain

            # ── C. Target Heresy & Table Politics (Anti-Snowballing) ──
            if c.target_heresy > 0:
                u += c.target_heresy * 1.5
                so = state.players.get(FactionId.SWIETE_OFICJUM)
                if so and faction != FactionId.SWIETE_OFICJUM and oficjum_snowball_threat(state):
                    # Oficjum 1 shy of win — don't spend heresy framing random rivals
                    u -= c.target_heresy * 1.2
                # If Kabała is near win with 2+ fragments:
                kt = state.players.get(FactionId.KABALA_TOLEDO)
                if kt and faction != FactionId.KABALA_TOLEDO and kt.fragments >= 2:
                    # Near Codex: push them into Court range
                    u += c.target_heresy * 1.8

            # ── D. Board Presence & Agent Movement ──
            if c.agents > 0:
                u += c.agents * 0.8
                # Cienie Al-Andalus: prioritize moving toward relics or harbor
                if faction == FactionId.CIENIE_AL_ANDALUS:
                    u += c.agents * 1.2

            # ── E. Control & Extortion (Arrests, Interrogations, Hooks) ──
            if c.arrest:
                u += 2.0
            if "interrogation" in c.tags:
                u += 2.2
            if c.creates_hook:
                if faction == FactionId.GILDIA_CIENI:
                    u += 3.5  # Upadki often need a Hak
                else:
                    u += 2.0

            # ── F. Faction-Specific Win Proximity ──
            if faction == FactionId.SWIETE_OFICJUM:
                if "autodafe" in c.tags:
                    if state.eras_since_autodafe >= state.autodafe_cooldown:
                        u += 6.0 if pl.gold >= eff_cost else 1.0
                    else:
                        u += 1.0
                if "inquisitor" in c.tags and not pl.used_inquisitor_send:
                    u += 2.5

            elif faction == FactionId.CIENIE_AL_ANDALUS:
                if "relic" in c.tags:
                    u += 4.0
                    if pl.relics_evacuated >= 1:
                        u += 3.5
                    if state.sea_route_open and pl.relics_evacuated < 2:
                        u += 2.0
                if c.id == "caa-03":
                    on_relic = any(
                        state.relics_on_board.get(ag.location, 0) > 0 and not ag.arrested
                        for ag in pl.agents
                    )
                    if on_relic:
                        u += 4.0
                if c.id == "caa-09" and pl.relics_evacuated < 2:
                    u += 3.0
                if c.id == "caa-10":
                    if card_condition_met(state, faction, c) or state.sea_route_open:
                        u += 9.0 if pl.relics_evacuated >= 1 else 6.0
                    else:
                        u -= 18.0
                if c.id == "caa-05":  # Odnalezienie Relikwii
                    if not pl.used_kurier and pl.relics_evacuated < 2:
                        on_relic = any(
                            state.relics_on_board.get(ag.location, 0) > 0 and not ag.arrested
                            for ag in pl.agents
                        )
                        u += 6.0 if on_relic else 4.0
                if c.id == "caa-06":  # Bunt
                    arrested_cnt = sum(1 for ag in pl.agents if ag.arrested)
                    if arrested_cnt > 0:
                        u += 3.0

            elif faction == FactionId.KORONA_BORGIOWIE:
                from inquisitio.engine.hooks import distinct_hook_victims

                active_hooks = distinct_hook_victims(state, faction)
                if "decree" in c.tags:
                    u += 4.0
                    if pl.decrees_played < 2:
                        u += 2.0
                if c.id == "kb-10":
                    if active_hooks >= 2:
                        u += 6.0
                    else:
                        u -= 20.0
                if c.creates_hook:
                    if active_hooks < 2:
                        u += 3.5
                    elif len(pl.hook_victims_ever) < 2:
                        u += 2.0

            elif faction == FactionId.KABALA_TOLEDO:
                if "fragment" in c.tags:
                    u += 4.5
                    if pl.fragments >= 2 and c.id == "kt-10":
                        u += 6.0  # Decisive Finisher

            elif faction == FactionId.GILDIA_CIENI:
                if "fall" in c.tags or c.id == "gc-10":
                    u += 4.5
                if c.creates_hook or c.id in ("gc-04", "gc-06", "gc-09"):
                    u += 3.0

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

