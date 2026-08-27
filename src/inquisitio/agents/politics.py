"""Politics agent — Intelligent Utility AI with Economic ROI, Heresy Risk, and Strategic Passing."""
from __future__ import annotations

import random

from inquisitio.cards.loader import Card, load_all_cards
from inquisitio.config import CONFIG
from inquisitio.engine.card_conditions import card_condition_met
from inquisitio.engine.hooks import distinct_hook_victims
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

        # ── 1. Calibrated Value of Akcja Gospodarcza (+gold / pass option) ──
        if "intrigue_gold_offset" in sys:
            econ_gold = max(0, CONFIG.intrigue_gold() + int(sys["intrigue_gold_offset"]))
        else:
            econ_gold = int(sys.get("intrigue_gold", CONFIG.intrigue_gold()))
        on_rynek = any(ag.location == "rynek" and not ag.arrested for ag in pl.agents)
        if state.active_time_edict == "time-09" and on_rynek:
            econ_gold = max(econ_gold, 2)

        # Base value of taking simple economic pass
        v_econ = econ_gold * 0.9 + 0.3  # ~1.2 base

        # Finisher one gold short: Gospodarcza this round funds it (same era or next)
        finishers = [
            cards[cid] for cid in pl.hand
            if cards.get(cid) and (
                cards[cid].type == "signature"
                or "autodafe" in cards[cid].tags
                or "relic" in cards[cid].tags
                or "decree" in cards[cid].tags
                or "fragment" in cards[cid].tags
                or "fall" in cards[cid].tags
            )
        ]
        for fin in finishers:
            fin_cost = _effective_cost(fin)
            if fin_cost > pl.gold and (pl.gold + econ_gold >= fin_cost):
                v_econ = max(v_econ, 2.8)
                break

        if pl.gold == 0:
            v_econ = max(v_econ, 1.8)

        # ── 2. Threat Assessment for Tactical Targeting ──
        threats: dict[FactionId, float] = {}
        for r_fid, r_pl in state.players.items():
            if r_fid == faction:
                continue
            th = 0.0
            if r_fid == FactionId.SWIETE_OFICJUM:
                condemns = len(r_pl.condemned_rivals)
                if condemns >= 2:
                    th += 0.85
                elif condemns == 1:
                    th += 0.4
                if r_pl.stacks >= 5:
                    th += 0.75
            elif r_fid == FactionId.CIENIE_AL_ANDALUS:
                if r_pl.relics_evacuated >= 1:
                    th += 0.85
                    if state.sea_route_open:
                        th += 0.25
                elif any(state.relics_on_board.get(ag.location, 0) > 0 and not ag.arrested for ag in r_pl.agents):
                    th += 0.35
            elif r_fid == FactionId.KORONA_BORGIOWIE:
                r_hooks = distinct_hook_victims(state, r_fid)
                if r_hooks >= 2:
                    th += 0.85
                elif r_hooks == 1:
                    th += 0.35
                if r_pl.decrees_played >= 1:
                    th += 0.3
            elif r_fid == FactionId.KABALA_TOLEDO:
                if r_pl.fragments >= 2:
                    th += 0.75
                elif r_pl.fragments == 1 and state.era >= 4:
                    th += 0.30
            elif r_fid == FactionId.GILDIA_CIENI:
                if r_pl.falls >= 7:
                    th += 0.85
                elif r_pl.falls >= 5:
                    th += 0.45

            threats[r_fid] = th

        max_threat = max(threats.values()) if threats else 0.0
        has_so = FactionId.SWIETE_OFICJUM in state.players and faction != FactionId.SWIETE_OFICJUM
        autodafe_near = has_so and state.eras_since_autodafe >= (state.autodafe_cooldown - 1)

        # ── 3. Utility Evaluation for Each Legal Card ──
        scored: list[tuple[float, str]] = []

        for cid in legal:
            c = cards.get(cid)
            if not c:
                continue

            eff_cost = _effective_cost(c)
            # Base tempo score of putting card into play (cycles hand + performs action)
            u = 1.8

            # ── A. Economic Utility (Net ROI) ──
            if c.gold > 0:
                net_gold = c.gold - eff_cost
                u += net_gold * 1.5
            else:
                u -= eff_cost * 0.8
                if pl.gold <= eff_cost and eff_cost > 0:
                    u -= 0.4  # friction for spending last coin

            # ── B. Heresy Decrease / Cleanse Utility ──
            raw = c.raw if isinstance(c.raw, dict) else {}
            heresy_dec = int(raw.get("heresy_decrease", 0) or 0)
            if heresy_dec > 0 and pl.heresy > 0:
                u += min(pl.heresy, heresy_dec) * 2.0

            # ── C. Heresy Risk & Zone Dynamics ──
            post_h = pl.heresy + c.heresy
            if post_h >= threshold:
                u -= c.heresy * 4.5  # Critical execution danger
            elif post_h >= threshold - 1:
                u -= c.heresy * 2.5
            elif has_so and post_h >= state.observed_threshold:
                if autodafe_near:
                    u -= c.heresy * 3.0
                else:
                    u -= c.heresy * 1.2
            else:
                u -= c.heresy * 0.3  # Safe zone heresy

            # ── D. Board Presence & Agent Mobility ──
            if c.agents > 0:
                u += c.agents * 1.2
                if faction == FactionId.CIENIE_AL_ANDALUS:
                    u += c.agents * 1.0  # Crucial for repositioning on relics
                elif faction == FactionId.SWIETE_OFICJUM:
                    u += c.agents * 0.8

            # ── E. Control, Hooks, Arrests, Framing ──
            if c.target_heresy > 0:
                u += c.target_heresy * 1.4
                if max_threat >= 0.4:
                    u += c.target_heresy * 1.8 * max_threat

            if c.creates_hook:
                if faction == FactionId.GILDIA_CIENI:
                    u += 3.6  # Upadki engine
                elif faction == FactionId.KORONA_BORGIOWIE:
                    u += 3.2  # Pieczęć Korony prerequisite
                else:
                    u += 2.2

            if c.arrest:
                u += 2.5
                if max_threat >= 0.4:
                    u += 2.0 * max_threat

            if "interrogation" in c.tags:
                u += 2.4

            # ── F. Faction-Specific Strategic Synergies ──
            if faction == FactionId.CIENIE_AL_ANDALUS:
                relics_left = max(0, 2 - pl.relics_evacuated)
                if "relic" in c.tags:
                    u += 3.5
                    if pl.relics_evacuated >= 1:
                        u += 2.5
                    if state.sea_route_open and pl.relics_evacuated < 2:
                        u += 1.8
                if c.id == "caa-01":  # Przejście Podziemiami
                    # Agent relocation: highly valuable if any agent is far from port/relic
                    u += 3.2
                if c.id == "caa-02":  # Złoto z Kryjówki
                    # Gold liquidity: valuable if poor or preparing for caa-10/caa-05
                    u += 3.6 if pl.gold < 3 else 1.8
                if c.id == "caa-03":
                    on_relic = any(state.relics_on_board.get(ag.location, 0) > 0 and not ag.arrested for ag in pl.agents)
                    if on_relic:
                        u += 3.5
                if c.id == "caa-04":  # Fałszywy Trop
                    u += 1.6  # Free 0-cost disruption
                if c.id == "caa-05":  # Ukryty Kurier
                    if not pl.used_kurier and pl.relics_evacuated < 2:
                        on_relic = any(state.relics_on_board.get(ag.location, 0) > 0 and not ag.arrested for ag in pl.agents)
                        u += 5.5 if on_relic else 3.5
                if c.id == "caa-06":  # Ucieczka z Lochów
                    arrested_cnt = sum(1 for ag in pl.agents if ag.arrested)
                    if arrested_cnt >= 2:
                        u += 5.5
                    elif arrested_cnt == 1:
                        u += 3.8
                    else:
                        u += 1.2
                if c.id == "caa-08":  # Kaptur Nocy
                    u += 2.0
                if c.id == "caa-09":  # Kurier Relikwii
                    u += 3.0 if pl.relics_evacuated < 2 else 1.0
                if c.id == "caa-10":  # Echo Alhambry
                    if card_condition_met(state, faction, c) or state.sea_route_open:
                        u += 7.0 if pl.relics_evacuated >= 1 else 4.0
                    else:
                        u -= 18.0
                if c.id == "caa-11":  # Nocna Zmiana Warty
                    u += 2.2
                if c.id == "caa-12":  # Skrytka w Murach
                    u += 3.5

            elif faction == FactionId.KORONA_BORGIOWIE:
                active_hooks = distinct_hook_victims(state, faction)
                decrees_left = max(0, 2 - pl.decrees_played)

                if "decree" in c.tags:
                    u += 3.8
                    if decrees_left == 1 and active_hooks >= 2:
                        u += 4.5
                    elif decrees_left == 1:
                        u += 2.5

                if c.id == "kb-10":  # Pieczęć Korony
                    if active_hooks >= 2:
                        u += 7.5 if pl.decrees_played >= 1 else 4.5
                    else:
                        u -= 20.0  # Need hooks first

                if c.id == "kb-09":  # Dekret Królewski
                    if pl.decrees_played < 2:
                        u += 3.5

                if c.id in ("kb-01", "kb-03", "kb-11"):
                    u += 1.6  # Solid court maneuvers

                if c.creates_hook:
                    if active_hooks < 2:
                        u += 3.5 if active_hooks == 0 else 2.5
                    elif len(pl.hook_victims_ever) < 2:
                        u += 2.0

            elif faction == FactionId.KABALA_TOLEDO:
                frags_left = max(0, 3 - pl.fragments)
                if "fragment" in c.tags:
                    u += 4.5
                    if frags_left <= 1:
                        u += 3.0

                if c.id == "kt-03":  # Zakazana Wiedza
                    u += 5.5
                if c.id == "kt-05":  # Wskazówka Cyklu
                    u += 5.0
                if c.id == "kt-06":  # Przesłuchanie Imienia
                    u += 5.0
                if c.id == "kt-09":  # Fragment Kodeksu
                    u += 5.0
                if c.id == "kt-10":  # Pieczęć Salomona
                    if pl.fragments >= 3:
                        u += 12.0
                    else:
                        u -= 20.0  # Cannot complete rite without 3 fragments
                if c.id in ("kt-01", "kt-02", "kt-04", "kt-07", "kt-08", "kt-11", "kt-12"):
                    u += 2.0  # Tactical Kabala tools

            elif faction == FactionId.GILDIA_CIENI:
                falls_left = max(0, 8 - pl.falls)
                if c.id == "gc-10":  # Upadek Domu
                    if card_condition_met(state, faction, c):
                        u += 9.5 if falls_left <= 2 else 6.5
                    else:
                        u -= 15.0
                elif "fall" in c.tags:
                    u += 4.8
                    if falls_left <= 2:
                        u += 4.0
                    elif falls_left <= 4:
                        u += 2.0
                if c.id in ("gc-01", "gc-03", "gc-04", "gc-06", "gc-07", "gc-08", "gc-09", "gc-11", "gc-12"):
                    u += 2.2  # Guild subversive tools

            elif faction == FactionId.SWIETE_OFICJUM:
                if "autodafe" in c.tags:
                    if state.eras_since_autodafe >= state.autodafe_cooldown:
                        condemnable = sum(1 for f_id, p in state.players.items() if f_id != faction and p.heresy >= state.observed_threshold)
                        if condemnable >= 1:
                            u += 5.0 if pl.gold >= eff_cost else 2.0
                        else:
                            u += 2.5
                    else:
                        u += 0.8
                if "inquisitor" in c.tags and not pl.used_inquisitor_send:
                    u += 2.5
                if c.id == "so-03":  # Podejrzenie (+3 frame)
                    u += 3.5
                if c.id == "so-10":  # Oczyść Miasto (Stos)
                    condemnable = sum(1 for f_id, p in state.players.items() if f_id != faction and p.heresy >= state.observed_threshold)
                    u += 6.5 if condemnable >= 1 else 3.0
                if c.id in ("so-01", "so-04", "so-06", "so-07", "so-08", "so-09", "so-11", "so-12"):
                    u += 1.8  # Solid inquisitorial tools

            if c.type == "signature":
                u += 2.0

            # Tie-breaking slight entropy
            u += self.rng.random() * 0.2
            scored.append((u, cid))

        scored.sort(reverse=True)

        # ── 4. Play card vs Akcja Gospodarcza ──
        best_u, best_cid = scored[0]
        if best_u < v_econ:
            return None

        return best_cid

