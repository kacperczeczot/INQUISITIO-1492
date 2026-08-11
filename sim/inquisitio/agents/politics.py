from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from inquisitio.model import FactionId, LocationId


@dataclass
class PlayDecision:
    card_id: str
    location: LocationId
    move_agent: bool = True
    agent_dest: LocationId | None = None
    intent: str = ""
    feint: bool = False
    blame_target: FactionId | None = None


@dataclass
class AccuseDecision:
    accuse: bool
    target: FactionId | None = None
    strategic: bool = False
    reason: str = ""


@dataclass
class BeliefState:
    """Simple belief: likely focus locations per rival."""

    focus: dict[FactionId, dict[LocationId, float]] = field(default_factory=dict)
    seen_plays: dict[FactionId, list[str]] = field(default_factory=dict)

    def observe_play(self, faction: FactionId, location: LocationId, card_id: str) -> None:
        bucket = self.focus.setdefault(faction, {})
        for loc in list(bucket.keys()):
            bucket[loc] *= 0.85
        bucket[location] = bucket.get(location, 0.1) + 0.4
        self.seen_plays.setdefault(faction, []).append(card_id)

    def likely_location(self, faction: FactionId) -> LocationId | None:
        bucket = self.focus.get(faction) or {}
        if not bucket:
            return None
        return max(bucket.items(), key=lambda kv: kv[1])[0]


@dataclass
class PoliticsState:
    alliances: dict[FactionId, FactionId] = field(default_factory=dict)  # me -> ally
    threats: dict[FactionId, float] = field(default_factory=dict)

    def set_ally(self, me: FactionId, ally: FactionId) -> None:
        self.alliances[me] = ally

    def decay(self) -> None:
        # alliances last one era unless refreshed
        self.alliances.clear()


def intrigue_progress(state, faction: FactionId) -> float:
    p = state.player(faction)
    mapping = {
        FactionId.SWIETE_OFICJUM: min(1.0, (p.stakes * 2 + p.influence_tribunal / 4.0) / 2.0),
        FactionId.CIENIE_AL_ANDALUS: (p.evacuated_relics * 2 + p.relics) / 4.0,
        FactionId.KORONA_BORGIOWIE: (p.control_palace + p.control_market) / 4.0,
        FactionId.KABALA_TOLEDO: p.clues / 4.0,
        FactionId.GILDIA_CIENI: len(set(p.collapses)) / 2.0,
    }
    return float(mapping.get(faction, 0.0))


def build_threat_map(state, me: FactionId) -> dict[FactionId, float]:
    threats: dict[FactionId, float] = {}
    for f in state.rivals(me):
        t = intrigue_progress(state, f)
        # critical heresy is opportunity for oficjum / gildia
        if state.player(f).heresy >= state.threshold:
            t += 0.35
        threats[f] = t
    return threats
