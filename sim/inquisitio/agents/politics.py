"""Politics agent — fear Critical / Inquisitor, value Hooks."""
from __future__ import annotations

import random

from inquisitio.cards.loader import load_all_cards
from inquisitio.engine.state import FactionId, GameState


class PoliticsAgent:
    def __init__(self, rng: random.Random):
        self.rng = rng

    def choose_card(self, state: GameState, faction: FactionId, legal: list[str]) -> str | None:
        if not legal:
            return None
        cards = load_all_cards()
        pl = state.players[faction]
        scored: list[tuple[float, str]] = []
        for cid in legal:
            c = cards[cid]
            score = 0.0
            # fear critical: avoid self heresy when high
            if pl.heresy >= 6:
                score -= c.heresy * 3
            else:
                score += c.heresy * 0.2  # power edge
            score += c.target_heresy * 1.5
            score += c.gold * 0.8
            score += c.agents * 0.5
            if c.creates_hook:
                score += 2.0
            if c.arrest:
                score += 1.5
            if "interrogation" in c.tags:
                score += 1.8
            if c.type == "signature":
                score += 3.0
            # Oficjum likes stacks path — but so-10 is expensive; don't force-dump gold
            if faction == FactionId.SWIETE_OFICJUM and "autodafe" in c.tags:
                score += 2.5 if pl.gold >= c.cost_gold + 1 else 0.5
            # Anti-snowball: rivals deprioritize framing when Oficjum near win
            so = state.players.get(FactionId.SWIETE_OFICJUM)
            if (
                so
                and faction != FactionId.SWIETE_OFICJUM
                and (so.stacks >= 2 or len(so.condemned_rivals) >= 1)
                and c.target_heresy
            ):
                score -= c.target_heresy * 1.2
            # Anti-snowball: push Kabala out of sweet spot when close
            kt = state.players.get(FactionId.KABALA_TOLEDO)
            if (
                kt
                and faction != FactionId.KABALA_TOLEDO
                and kt.fragments >= 2
                and c.target_heresy
            ):
                score += c.target_heresy * 1.5
            if faction == FactionId.SWIETE_OFICJUM and "inquisitor" in c.tags:
                score += 2.5 if not pl.used_inquisitor_send else 0.2
            if faction == FactionId.CIENIE_AL_ANDALUS and "relic" in c.tags:
                score += 2.5
                # Push hard when a second relic would win
                if pl.relics_evacuated >= 1 or c.id in ("caa-05", "caa-10"):
                    score += 2.0
                if c.id in ("caa-05", "caa-10") and pl.gold >= c.cost_gold:
                    score += 3.0
            if faction == FactionId.KORONA_BORGIOWIE and "decree" in c.tags:
                score += 3.0
                if state.layer == "A":
                    if state.era < 4:
                        score -= 1.5
                    if pl.decrees_played < 1:
                        score += 2.0
                elif state.layer == "C":
                    # Need 2 decrees; hooks are the other half
                    hooks = len(pl.hook_victims_ever)
                    if pl.decrees_played < 2:
                        score += 3.5
                    if hooks < 1:
                        score += 1.5
                    if hooks >= 1 and pl.decrees_played >= 1 and pl.gold >= c.cost_gold:
                        score += 3.0
                if len(pl.hook_victims_ever) >= 1 and pl.gold >= c.cost_gold:
                    score += 2.0
            if faction == FactionId.CIENIE_AL_ANDALUS and state.layer == "A":
                on_relic = any(
                    state.relics_on_board.get(ag.location, 0) > 0 and not ag.arrested
                    for ag in pl.agents
                )
                if c.id == "caa-05":
                    if pl.used_kurier or pl.relics_evacuated >= 2:
                        score -= 5.0
                    elif on_relic:
                        score += 5.0
                    else:
                        score -= 2.0
                elif c.agents and pl.relics_evacuated < 2:
                    score += 2.0 if not on_relic else 0.5
            if (
                faction == FactionId.KORONA_BORGIOWIE
                and state.layer == "A"
                and "decree" in c.tags
            ):
                if pl.decrees_played < 1:
                    score += 3.0
                if state.era < 3:
                    score -= 1.0
            if faction == FactionId.KORONA_BORGIOWIE and c.creates_hook:
                score += 3.0
                need_hooks = 1 if state.layer == "A" else 2
                if len(pl.hook_victims_ever) < need_hooks:
                    score += 2.5
            if faction == FactionId.GILDIA_CIENI and c.creates_hook:
                score += 2.5
            if faction == FactionId.KABALA_TOLEDO and "fragment" in c.tags:
                score += 3.0
                if c.id in ("kt-03", "kt-05", "kt-06", "kt-09"):
                    score += 2.0
                if c.id == "kt-10":
                    if pl.fragments >= 2 and pl.gold >= c.cost_gold:
                        score += 4.0
                    elif pl.fragments < 1:
                        score -= 3.0
                if pl.fragments >= 2 or state.layer == "A":
                    if pl.heresy < 4:
                        score += max(0, c.heresy) * 2.0
                    elif pl.heresy > 6:
                        score -= c.heresy * 2
            if faction == FactionId.GILDIA_CIENI and "fall" in c.tags:
                need = 3 if state.layer == "B" else 2
                score += 2.5
                if pl.falls >= need - 1:
                    score += 3.0
            # avoid inquisitor tile overcrowding via move when heresy high
            if pl.heresy >= 5 and c.agents:
                score += 0.5
            score += self.rng.random() * 0.3
            scored.append((score, cid))
        scored.sort(reverse=True)
        return scored[0][1]
