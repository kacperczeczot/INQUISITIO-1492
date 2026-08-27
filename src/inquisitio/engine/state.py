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


class AgentToken:
    __slots__ = ("owner", "location", "arrested", "double_agent", "controller")

    def __init__(
        self,
        owner: FactionId,
        location: str,
        arrested: bool = False,
        double_agent: bool = False,
        controller: FactionId | None = None,
    ):
        self.owner = owner
        self.location = location
        self.arrested = arrested
        self.double_agent = double_agent
        self.controller = controller


class PlayerState:
    __slots__ = (
        "faction", "heresy", "gold", "hand", "deck", "discard", "agents",
        "stacks", "condemned_rivals", "relics_evacuated", "decrees_played",
        "fragments", "kt10_played", "falls", "hooks_on", "hook_victims_ever",
        "used_hook", "used_interrogation", "used_inquisitor_send",
        "avoided_autodafe", "path_via_double", "shadow_exit", "frames_dealt",
        "used_kurier", "inquisitor_send_count", "interrogate_count",
        "kurier_count", "vote_change_count", "used_puppet_move",
    )

    def __init__(
        self,
        faction: FactionId,
        heresy: int = 0,
        gold: int = 4,
        hand: list[str] | None = None,
        deck: list[str] | None = None,
        discard: list[str] | None = None,
        agents: list[AgentToken] | None = None,
        stacks: int = 0,
        condemned_rivals: set[FactionId] | None = None,
        relics_evacuated: int = 0,
        decrees_played: int = 0,
        fragments: int = 0,
        kt10_played: bool = False,
        falls: int = 0,
        hooks_on: dict[FactionId, int] | None = None,
        hook_victims_ever: set[FactionId] | None = None,
        used_hook: bool = False,
        used_interrogation: bool = False,
        used_inquisitor_send: bool = False,
        avoided_autodafe: bool = False,
        path_via_double: bool = False,
        shadow_exit: bool = False,
        frames_dealt: int = 0,
        used_kurier: bool = False,
        inquisitor_send_count: int = 0,
        interrogate_count: int = 0,
        kurier_count: int = 0,
        vote_change_count: int = 0,
        used_puppet_move: bool = False,
    ):
        self.faction = faction
        self.heresy = heresy
        self.gold = gold
        self.hand = hand if hand is not None else []
        self.deck = deck if deck is not None else []
        self.discard = discard if discard is not None else []
        self.agents = agents if agents is not None else []
        self.stacks = stacks
        self.condemned_rivals = condemned_rivals if condemned_rivals is not None else set()
        self.relics_evacuated = relics_evacuated
        self.decrees_played = decrees_played
        self.fragments = fragments
        self.kt10_played = kt10_played
        self.falls = falls
        self.hooks_on = hooks_on if hooks_on is not None else {}
        self.hook_victims_ever = hook_victims_ever if hook_victims_ever is not None else set()
        self.used_hook = used_hook
        self.used_interrogation = used_interrogation
        self.used_inquisitor_send = used_inquisitor_send
        self.avoided_autodafe = avoided_autodafe
        self.path_via_double = path_via_double
        self.shadow_exit = shadow_exit
        self.frames_dealt = frames_dealt
        self.used_kurier = used_kurier
        self.inquisitor_send_count = inquisitor_send_count
        self.interrogate_count = interrogate_count
        self.kurier_count = kurier_count
        self.vote_change_count = vote_change_count
        self.used_puppet_move = used_puppet_move


class StagedPlay:
    """Face-down intrigue card; effect resolves in Faza II (odkrycie)."""
    __slots__ = ("owner", "card_id", "location", "seq", "cond_ok")

    def __init__(
        self,
        owner: FactionId,
        card_id: str,
        location: str,
        seq: int = 0,
        cond_ok: bool | None = None,
    ):
        self.owner = owner
        self.card_id = card_id
        self.location = location
        self.seq = seq
        self.cond_ok = cond_ok


class DramaMetrics:
    __slots__ = (
        "autodafe_count", "accusations", "convictions", "hooks_created",
        "hooks_forced", "doubles_created", "cards_played", "card_plays",
        "legal_moves_sampled", "deadlocks", "forced_passes", "eras",
    )

    def __init__(
        self,
        autodafe_count: int = 0,
        accusations: int = 0,
        convictions: int = 0,
        hooks_created: int = 0,
        hooks_forced: int = 0,
        doubles_created: int = 0,
        cards_played: int = 0,
        card_plays: dict[str, int] | None = None,
        legal_moves_sampled: int = 0,
        deadlocks: int = 0,
        forced_passes: int = 0,
        eras: int = 0,
    ):
        self.autodafe_count = autodafe_count
        self.accusations = accusations
        self.convictions = convictions
        self.hooks_created = hooks_created
        self.hooks_forced = hooks_forced
        self.doubles_created = doubles_created
        self.cards_played = cards_played
        self.card_plays = card_plays if card_plays is not None else {}
        self.legal_moves_sampled = legal_moves_sampled
        self.deadlocks = deadlocks
        self.forced_passes = forced_passes
        self.eras = eras


class GameState:
    __slots__ = (
        "players", "turn_order", "era", "max_eras", "accusation_threshold",
        "observed_threshold", "inquisitor_location", "inquisitor_mode",
        "eras_since_autodafe", "autodafe_cooldown", "sea_route_open",
        "relics_on_board", "time_deck", "time_discard", "active_time_edict",
        "winner", "win_path", "metrics", "log", "rng_seed", "layer",
        "sys_overrides", "pending_plays", "accused_this_era",
    )

    def __init__(
        self,
        players: dict[FactionId, PlayerState],
        turn_order: list[FactionId],
        era: int = 1,
        max_eras: int = 12,
        accusation_threshold: int = 7,
        observed_threshold: int = 5,
        inquisitor_location: str = "trybunal",
        inquisitor_mode: InquisitorMode = InquisitorMode.PATROL,
        eras_since_autodafe: int = 0,
        autodafe_cooldown: int = 3,
        sea_route_open: bool = False,
        relics_on_board: dict[str, int] | None = None,
        time_deck: list[str] | None = None,
        time_discard: list[str] | None = None,
        active_time_edict: str | None = None,
        winner: FactionId | None = None,
        win_path: str | None = None,
        metrics: DramaMetrics | None = None,
        log: list[str] | None = None,
        rng_seed: int = 0,
        layer: str = "C",
        sys_overrides: dict | None = None,
        pending_plays: list[StagedPlay] | None = None,
        accused_this_era: set[FactionId] | None = None,
    ):
        self.players = players
        self.turn_order = turn_order
        self.era = era
        self.max_eras = max_eras
        self.accusation_threshold = accusation_threshold
        self.observed_threshold = observed_threshold
        self.inquisitor_location = inquisitor_location
        self.inquisitor_mode = inquisitor_mode
        self.eras_since_autodafe = eras_since_autodafe
        self.autodafe_cooldown = autodafe_cooldown
        self.sea_route_open = sea_route_open
        self.relics_on_board = relics_on_board if relics_on_board is not None else {}
        self.time_deck = time_deck if time_deck is not None else []
        self.time_discard = time_discard if time_discard is not None else []
        self.active_time_edict = active_time_edict
        self.winner = winner
        self.win_path = win_path
        self.metrics = metrics if metrics is not None else DramaMetrics()
        self.log = log
        self.rng_seed = rng_seed
        self.layer = layer
        self.sys_overrides = sys_overrides if sys_overrides is not None else {}
        self.pending_plays = pending_plays if pending_plays is not None else []
        self.accused_this_era = accused_this_era if accused_this_era is not None else set()

    def alive_factions(self) -> list[FactionId]:
        return list(self.turn_order)

    def add_log(self, msg: str) -> None:
        if self.log is not None:
            self.log.append(f"E{self.era}: {msg}")


def heresy_zone(value: int, critical_min: int = 7, observed_min: int = 5) -> str:
    """Czysta < observed_min; Obserwowana until accusation; Krytyczna at threshold+."""
    if value < observed_min:
        return "czysta"
    if value < critical_min:
        return "obserwowana"
    return "krytyczna"


def clamp_heresy(v: int) -> int:
    return max(0, min(10, v))
