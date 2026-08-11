from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from inquisitio.model import LOCATION_ORDER, FactionId, LocationId, heresy_zone


@dataclass
class AgentToken:
    owner: FactionId
    location: LocationId | None = None  # None = off board (reserve)
    in_dungeon: bool = False
    burned: bool = False


@dataclass
class PlayedCard:
    card_id: str
    owner: FactionId
    location: LocationId
    face_down: bool = True


@dataclass
class PlayerState:
    faction: FactionId
    heresy: int = 0
    gold: int = 2
    hand: list[str] = field(default_factory=list)
    deck: list[str] = field(default_factory=list)
    discard: list[str] = field(default_factory=list)
    permanents: list[str] = field(default_factory=list)
    agents: list[AgentToken] = field(default_factory=list)
    relics: int = 0
    evacuated_relics: int = 0
    clues: int = 0
    control_palace: int = 0
    control_market: int = 0
    influence_tribunal: int = 0
    stakes: int = 0  # Oficjum stosy
    collapses: list[FactionId] = field(default_factory=list)  # Gildia upadki
    accused_this_era: bool = False
    played_shadow_locs: set[LocationId] = field(default_factory=set)
    cards_played_this_era: int = 0

    def living_agents(self) -> list[AgentToken]:
        return [a for a in self.agents if not a.burned]

    def agents_on_board(self) -> list[AgentToken]:
        return [a for a in self.living_agents() if a.location is not None and not a.in_dungeon]

    def agents_in(self, loc: LocationId) -> list[AgentToken]:
        return [a for a in self.agents_on_board() if a.location == loc]

    def dungeon_agents(self) -> list[AgentToken]:
        return [a for a in self.living_agents() if a.in_dungeon]

    def add_heresy(self, amount: int) -> None:
        self.heresy = max(0, min(10, self.heresy + amount))

    def zone(self) -> str:
        return heresy_zone(self.heresy)


@dataclass
class GameMetrics:
    critical_entries: int = 0
    accusations: int = 0
    verdicts: int = 0
    stakes_total: int = 0
    feints: int = 0
    plays: int = 0
    strategic_accusations: int = 0
    max_heresy_seen: dict[str, int] = field(default_factory=dict)
    intrigue_log: list[dict[str, Any]] = field(default_factory=list)

    def log(self, **kwargs: Any) -> None:
        self.intrigue_log.append(kwargs)


@dataclass
class GameState:
    players: dict[FactionId, PlayerState]
    order: list[FactionId]
    cards: dict[str, Any]  # card_id -> Card
    threshold: int = 7
    era: int = 0
    max_eras: int = 6
    first_player_idx: int = 0
    sea_route_open: bool = False
    relic_pool: int = 5
    relics_on_board: dict[LocationId, int] = field(default_factory=dict)
    clue_pool: int = 6
    time_deck: list[str] = field(default_factory=list)
    time_discard: list[str] = field(default_factory=list)
    current_time: str | None = None
    slots: dict[LocationId, list[PlayedCard]] = field(default_factory=dict)
    winner: FactionId | None = None
    win_reason: str = ""
    metrics: GameMetrics = field(default_factory=GameMetrics)
    rng_seed: int = 0
    era_modifiers: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.slots:
            self.slots = {loc: [] for loc in LOCATION_ORDER}
        if not self.relics_on_board:
            self.relics_on_board = {loc: 0 for loc in LOCATION_ORDER}

    def player(self, faction: FactionId) -> PlayerState:
        return self.players[faction]

    def rivals(self, faction: FactionId) -> list[FactionId]:
        return [f for f in self.order if f != faction]

    def turn_order(self) -> list[FactionId]:
        n = len(self.order)
        start = self.first_player_idx % n
        return [self.order[(start + i) % n] for i in range(n)]

    def clear_era_slots(self) -> None:
        for loc in LOCATION_ORDER:
            self.slots[loc].clear()
        for p in self.players.values():
            p.accused_this_era = False
            p.played_shadow_locs.clear()
            p.cards_played_this_era = 0
        self.era_modifiers.clear()
        self.current_time = None
