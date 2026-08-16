"""Game state for political intrigue prototype (layers A–C)."""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class FactionId(str, Enum):
    SWIETE_OFICJUM = "swiete-oficjum"
    CIENIE_AL_ANDALUS = "cienie-al-andalus"
    KORONA_BORGIOWIE = "korona-borgiowie"
    KABALA_TOLEDO = "kabala-toledo"
    GILDIA_CIENI = "gildia-cieni"


LOCATIONS = [
    "trybunal",
    "palac",
    "lochy",
    "rynek",
    "gildia",
]

LOCATION_INDEX = {name: i for i, name in enumerate(LOCATIONS)}

# Cycle + Lochy–Pałac chord (see game/board/locations.md). Phase III order ≠ graph.
NEIGHBORS: dict[str, tuple[str, ...]] = {
    "trybunal": ("palac", "lochy"),
    "palac": ("trybunal", "rynek", "lochy"),
    "lochy": ("trybunal", "palac", "gildia"),
    "rynek": ("palac", "gildia"),
    "gildia": ("rynek", "lochy"),
}


class InquisitorMode(str, Enum):
    PATROL = "patrol"
    AUTODAFE = "autodafe"


@dataclass
class AgentToken:
    owner: FactionId
    location: str
    arrested: bool = False
    double_agent: bool = False  # controlled by another
    controller: FactionId | None = None


@dataclass
class PlayerState:
    faction: FactionId
    heresy: int = 0
    gold: int = 3
    hand: list[str] = field(default_factory=list)
    deck: list[str] = field(default_factory=list)
    discard: list[str] = field(default_factory=list)
    agents: list[AgentToken] = field(default_factory=list)
    # victory trackers
    stacks: int = 0  # Oficjum (Autodafé / Werdykt)
    condemned_rivals: set[FactionId] = field(default_factory=set)  # Oficjum alternate
    relics_evacuated: int = 0  # Cienie
    decrees_played: int = 0  # Korona
    fragments: int = 0  # Kabala
    falls: int = 0  # Gildia
    # hooks this player HOLDS on others: target faction -> count
    hooks_on: dict[FactionId, int] = field(default_factory=dict)
    # lifetime distinct hook victims (survives force/consume — Korona win path)
    hook_victims_ever: set[FactionId] = field(default_factory=set)
    # anti-AP per era
    used_hook: bool = False
    used_interrogation: bool = False
    used_inquisitor_send: bool = False
    avoided_autodafe: bool = False
    path_via_double: bool = False
    # A teach / shared pressure metric
    frames_dealt: int = 0
    used_kurier: bool = False  # A: caa-05 once
    inquisitor_send_count: int = 0
    interrogate_count: int = 0
    kurier_count: int = 0
    vote_change_count: int = 0


@dataclass
class DramaMetrics:
    autodafe_count: int = 0
    accusations: int = 0
    convictions: int = 0
    hooks_created: int = 0
    hooks_forced: int = 0
    doubles_created: int = 0
    cards_played: int = 0
    legal_moves_sampled: int = 0
    deadlocks: int = 0  # eras where a player had zero legal plays
    forced_passes: int = 0  # turns where player had no affordable cards
    eras: int = 0


@dataclass
class GameState:
    players: dict[FactionId, PlayerState]
    turn_order: list[FactionId]
    era: int = 1
    max_eras: int = 8
    accusation_threshold: int = 7
    inquisitor_location: str = "trybunal"
    inquisitor_mode: InquisitorMode = InquisitorMode.PATROL
    eras_since_autodafe: int = 0
    autodafe_cooldown: int = 3
    sea_route_open: bool = False
    relics_on_board: dict[str, int] = field(default_factory=dict)
    time_deck: list[str] = field(default_factory=list)
    time_discard: list[str] = field(default_factory=list)
    active_time_edict: str | None = None
    winner: FactionId | None = None
    win_path: str | None = None
    metrics: DramaMetrics = field(default_factory=DramaMetrics)
    log: list[str] = field(default_factory=list)
    rng_seed: int = 0
    layer: str = "C"  # A, B, or C content enabled
    sys_overrides: dict = field(default_factory=dict)

    def alive_factions(self) -> list[FactionId]:
        return list(self.turn_order)

    def add_log(self, msg: str) -> None:
        self.log.append(f"E{self.era}: {msg}")


def heresy_zone(value: int, critical_min: int = 7) -> str:
    """Clean 0–3; observed until accusation threshold; critical at threshold+."""
    if value <= 3:
        return "czysta"
    if value < critical_min:
        return "obserwowana"
    return "krytyczna"


def clamp_heresy(v: int) -> int:
    return max(0, min(10, v))
