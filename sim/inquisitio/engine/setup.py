"""Game setup — 3–5 players only."""
from __future__ import annotations

import random
from typing import Iterable

from inquisitio.cards.loader import cards_for_faction, time_cards
from inquisitio.config import CONFIG
from inquisitio.engine.state import (
    LOCATIONS,
    AgentToken,
    FactionId,
    GameState,
    PlayerState,
)

SETUP_PRESETS: dict[str, list[FactionId]] = {
    # --- 3p (wszystkie 10 kombinacji) ---
    "3p-oficjum-alandalus-korona": [
        FactionId.SWIETE_OFICJUM,
        FactionId.CIENIE_AL_ANDALUS,
        FactionId.KORONA_BORGIOWIE,
    ],
    "3p-oficjum-kabala-gildia": [
        FactionId.SWIETE_OFICJUM,
        FactionId.KABALA_TOLEDO,
        FactionId.GILDIA_CIENI,
    ],
    "3p-cienie-korona-gildia": [
        FactionId.CIENIE_AL_ANDALUS,
        FactionId.KORONA_BORGIOWIE,
        FactionId.GILDIA_CIENI,
    ],
    "3p-oficjum-alandalus-gildia": [
        FactionId.SWIETE_OFICJUM,
        FactionId.CIENIE_AL_ANDALUS,
        FactionId.GILDIA_CIENI,
    ],
    "3p-oficjum-alandalus-kabala": [
        FactionId.SWIETE_OFICJUM,
        FactionId.CIENIE_AL_ANDALUS,
        FactionId.KABALA_TOLEDO,
    ],
    "3p-oficjum-korona-gildia": [
        FactionId.SWIETE_OFICJUM,
        FactionId.KORONA_BORGIOWIE,
        FactionId.GILDIA_CIENI,
    ],
    "3p-oficjum-korona-kabala": [
        FactionId.SWIETE_OFICJUM,
        FactionId.KORONA_BORGIOWIE,
        FactionId.KABALA_TOLEDO,
    ],
    "3p-cienie-korona-kabala": [
        FactionId.CIENIE_AL_ANDALUS,
        FactionId.KORONA_BORGIOWIE,
        FactionId.KABALA_TOLEDO,
    ],
    "3p-cienie-kabala-gildia": [
        FactionId.CIENIE_AL_ANDALUS,
        FactionId.KABALA_TOLEDO,
        FactionId.GILDIA_CIENI,
    ],
    "3p-korona-kabala-gildia": [
        FactionId.KORONA_BORGIOWIE,
        FactionId.KABALA_TOLEDO,
        FactionId.GILDIA_CIENI,
    ],
    # --- 4p (wszystkie 5 kombinacji) ---
    "4p-core": [  # no Gildia
        FactionId.SWIETE_OFICJUM,
        FactionId.CIENIE_AL_ANDALUS,
        FactionId.KORONA_BORGIOWIE,
        FactionId.KABALA_TOLEDO,
    ],
    "4p-no-kabala": [
        FactionId.SWIETE_OFICJUM,
        FactionId.CIENIE_AL_ANDALUS,
        FactionId.KORONA_BORGIOWIE,
        FactionId.GILDIA_CIENI,
    ],
    "4p-no-korona": [
        FactionId.SWIETE_OFICJUM,
        FactionId.CIENIE_AL_ANDALUS,
        FactionId.KABALA_TOLEDO,
        FactionId.GILDIA_CIENI,
    ],
    "4p-no-cienie": [
        FactionId.SWIETE_OFICJUM,
        FactionId.KORONA_BORGIOWIE,
        FactionId.KABALA_TOLEDO,
        FactionId.GILDIA_CIENI,
    ],
    "4p-no-oficjum": [
        FactionId.CIENIE_AL_ANDALUS,
        FactionId.KORONA_BORGIOWIE,
        FactionId.KABALA_TOLEDO,
        FactionId.GILDIA_CIENI,
    ],
    # --- 5p (wszystkie 5 frakcji) ---
    "5p-full": [
        FactionId.SWIETE_OFICJUM,
        FactionId.CIENIE_AL_ANDALUS,
        FactionId.KORONA_BORGIOWIE,
        FactionId.KABALA_TOLEDO,
        FactionId.GILDIA_CIENI,
    ],
}


def _start_agents(faction: FactionId, count: int = 3) -> list[AgentToken]:
    homes = {
        FactionId.SWIETE_OFICJUM: "trybunal",
        FactionId.CIENIE_AL_ANDALUS: "gildia",
        FactionId.KORONA_BORGIOWIE: "palac",
        FactionId.KABALA_TOLEDO: "lochy",
        FactionId.GILDIA_CIENI: "rynek",
    }
    home = homes[faction]
    tokens = []
    for i in range(count):
        loc = home if i < 2 else "rynek"
        tokens.append(AgentToken(owner=faction, location=loc))
    return tokens


def new_game(
    factions: Iterable[FactionId] | None = None,
    *,
    setup: str | None = None,
    players: int | None = None,
    seed: int = 42,
    threshold: int = 8,
    layer: str = "C",
    max_eras: int = 8,
    sys_overrides: dict | None = None,
) -> GameState:
    if setup:
        factions = SETUP_PRESETS[setup]
    elif factions is None:
        if players == 4:
            factions = SETUP_PRESETS["4p-core"]
        elif players == 5:
            factions = SETUP_PRESETS["5p-full"]
        else:
            factions = SETUP_PRESETS["3p-oficjum-alandalus-korona"]
    faction_list = list(factions)
    if len(faction_list) < 3 or len(faction_list) > 5:
        raise ValueError("Players must be 3–5 (no 2p mode)")

    n_players = len(faction_list)
    sys = sys_overrides or {}

    if "start_gold" in sys:
        start_gold = sys["start_gold"]
    else:
        start_gold = CONFIG.start_gold_for(n_players)
    agents_count = sys.get("agents_per_player", CONFIG.system.agents_per_player)
    hand_limit = sys.get("hand_limit", CONFIG.system.hand_limit)
    max_eras = sys.get("max_eras", CONFIG.system.max_eras)

    # Threshold: sys_overrides > explicit param > CONFIG per player count
    if "threshold" in sys:
        final_threshold = sys["threshold"]
    elif threshold != 8:
        final_threshold = threshold
    else:
        final_threshold = CONFIG.threshold_for(n_players)

    rng = random.Random(seed)
    players_map: dict[FactionId, PlayerState] = {}
    for fid in faction_list:
        deck_cards = cards_for_faction(fid.value, max_layer=layer)
        ids = [c.id for c in deck_cards]
        rng.shuffle(ids)
        hand = ids[:hand_limit]
        deck = ids[hand_limit:]
        players_map[fid] = PlayerState(
            faction=fid,
            hand=hand,
            deck=deck,
            agents=_start_agents(fid, agents_count),
            gold=start_gold,
        )

    relics = {loc: 0 for loc in LOCATIONS}
    relics["lochy"] = 1
    relics["gildia"] = 1
    relics["trybunal"] = 1

    tdeck = [c.id for c in time_cards(max_layer=layer)]
    rng.shuffle(tdeck)

    state = GameState(
        players=players_map,
        turn_order=faction_list,
        accusation_threshold=final_threshold,
        relics_on_board=relics,
        time_deck=tdeck,
        rng_seed=seed,
        layer=layer,
        max_eras=max_eras,
        autodafe_cooldown=sys.get("autodafe_cooldown", CONFIG.system.autodafe_cooldown),
        sys_overrides=sys,
    )
    return state
