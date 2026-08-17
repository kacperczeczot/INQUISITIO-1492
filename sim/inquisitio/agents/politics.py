"""Politics agent — Intelligent Utility AI with Economic ROI, Heresy Risk, and Strategic Passing."""
from __future__ import annotations

import random

from inquisitio.cards.loader import Card, load_all_cards
from inquisitio.config import CONFIG
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

        # ── 1. Tactical Reservation Value of Passing (V_pass) ──
        # In a board game, passing to conserve gold and avoid unnecessary heresy is a fundamental tactical option.
        v_pass = 0.2

        # Check if holding a critical finisher or signature card that we cannot yet afford but could afford next era (+1 gold):
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
            if fin_cost > pl.gold and (pl.gold + 1 >= fin_cost):
                # If saving our gold allows firing the finisher next era:
                v_pass = max(v_pass, 2.5)
                break

        # If low on gold (1g) and no urgent threat, conserve gold for next era's card draw:
        if pl.gold <= 1:
            v_pass = max(v_pass, 0.8)

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
            if faction == FactionId.KABALA_TOLEDO:
                # Kabała needs heresy in the sweet spot [3, 8] (target 4–6)
                if pl.heresy < 3:
                    u += max(0, c.heresy) * 1.6
                elif 3 <= pl.heresy <= 6:
                    if c.heresy > 0:
                        u -= c.heresy * 1.2
                    elif c.heresy < 0:
                        u += 0.5  # slight stabilization
                else:  # >= 7 (Critical danger of Court Werdykt)
                    u -= c.heresy * 4.0
            else:
                # Standard factions fear Critical Heresy (Court accusation threshold)
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
                    # Push Kabała out of sweet spot into Critical
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
                if faction in (FactionId.KORONA_BORGIOWIE, FactionId.GILDIA_CIENI):
                    u += 3.5  # Core win condition prerequisite
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
                    u += 3.5
                    if pl.relics_evacuated >= 1:
                        u += 2.5
                if c.id == "caa-05":  # Ukryty Kurier
                    on_relic = any(
                        state.relics_on_board.get(ag.location, 0) > 0 and not ag.arrested
                        for ag in pl.agents
                    )
                    if on_relic and not pl.used_kurier and pl.relics_evacuated < 2:
                        u += 5.5
                    else:
                        u -= 2.5
                if c.id == "caa-06":  # Bunt
                    arrested_cnt = sum(1 for ag in pl.agents if ag.arrested)
                    if arrested_cnt > 0:
                        u += 3.0

            elif faction == FactionId.KORONA_BORGIOWIE:
                if "decree" in c.tags:
                    u += 4.0
                    if pl.decrees_played < 2:
                        u += 2.0
                if c.creates_hook and len(pl.hook_victims_ever) < 2:
                    u += 2.5

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

        # ── 3. Rational Decision Gate (Play vs Tactical Pass) ──
        best_u, best_cid = scored[0]
        if best_u < v_pass:
            # All available plays have lower expected utility than keeping resources / passing
            return None

        return best_cid

