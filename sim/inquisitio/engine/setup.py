from __future__ import annotations

import random
from dataclasses import dataclass

from inquisitio.cards.loader import CardLoader
from inquisitio.engine.state import AgentToken, GameState, PlayerState
from inquisitio.model import LOCATION_ORDER, FactionId, LocationId


SETUP_PRESETS: dict[str, list[FactionId]] = {
    "2p-oficjum-alandalus": [
        FactionId.SWIETE_OFICJUM,
        FactionId.CIENIE_AL_ANDALUS,
    ],
    "2p-oficjum-kabala": [
        FactionId.SWIETE_OFICJUM,
        FactionId.KABALA_TOLEDO,
    ],
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
    "4p-no-gildia": [
        FactionId.SWIETE_OFICJUM,
        FactionId.CIENIE_AL_ANDALUS,
        FactionId.KORONA_BORGIOWIE,
        FactionId.KABALA_TOLEDO,
    ],
    "5p-full": [
        FactionId.SWIETE_OFICJUM,
        FactionId.CIENIE_AL_ANDALUS,
        FactionId.KORONA_BORGIOWIE,
        FactionId.KABALA_TOLEDO,
        FactionId.GILDIA_CIENI,
    ],
}


@dataclass
class SetupConfig:
    factions: list[FactionId]
    threshold: int = 7
    max_eras: int = 6
    starting_gold: int = 2
    hand_size: int = 5
    agents_per_player: int = 3
    seed: int = 0
    simplified: bool = False  # 2-3p: fewer relics, shorter eras


def resolve_setup(
    setup_name: str | None = None,
    players: int | None = None,
    threshold: int = 7,
    seed: int = 0,
) -> SetupConfig:
    if setup_name and setup_name in SETUP_PRESETS:
        factions = list(SETUP_PRESETS[setup_name])
    elif players == 2:
        factions = list(SETUP_PRESETS["2p-oficjum-alandalus"])
    elif players == 3:
        factions = list(SETUP_PRESETS["3p-oficjum-alandalus-korona"])
    elif players == 4:
        factions = list(SETUP_PRESETS["4p-no-gildia"])
    else:
        factions = list(SETUP_PRESETS["5p-full"])
    simplified = len(factions) <= 3
    return SetupConfig(
        factions=factions,
        threshold=threshold,
        max_eras=5 if simplified else 6,
        seed=seed,
        simplified=simplified,
    )


def create_game(config: SetupConfig, loader: CardLoader | None = None) -> GameState:
    loader = loader or CardLoader()
    all_cards = loader.load_all()
    rng = random.Random(config.seed)

    players: dict[FactionId, PlayerState] = {}
    for faction in config.factions:
        deck_cards = [c.id for c in loader.by_faction(faction)]
        rng.shuffle(deck_cards)
        hand = deck_cards[: config.hand_size]
        rest = deck_cards[config.hand_size :]
        # Start agents on preferred locations (spread)
        prefs = {
            FactionId.SWIETE_OFICJUM: [LocationId.TRYBUNAL, LocationId.LOCHY, LocationId.RYNEK],
            FactionId.CIENIE_AL_ANDALUS: [LocationId.GILDIA, LocationId.LOCHY, LocationId.RYNEK],
            FactionId.KORONA_BORGIOWIE: [LocationId.PALAC, LocationId.RYNEK, LocationId.TRYBUNAL],
            FactionId.KABALA_TOLEDO: [LocationId.GILDIA, LocationId.TRYBUNAL, LocationId.LOCHY],
            FactionId.GILDIA_CIENI: [LocationId.GILDIA, LocationId.RYNEK, LocationId.LOCHY],
        }
        locs = prefs.get(faction, list(LOCATION_ORDER)[:3])
        agents = [
            AgentToken(owner=faction, location=locs[i % len(locs)])
            for i in range(config.agents_per_player)
        ]
        players[faction] = PlayerState(
            faction=faction,
            gold=config.starting_gold,
            hand=hand,
            deck=rest,
            agents=agents,
        )

    time_ids = [c.id for c in loader.by_faction(FactionId.TIME)]
    rng.shuffle(time_ids)
    # Bez sztucznego „dokładania” Floty — wybór 2 kart w Fazie I to skill

    relics_on_board = {loc: 0 for loc in LOCATION_ORDER}
    relics_on_board[LocationId.LOCHY] = 1
    pool = 4 if config.simplified else 5
    open_count = 1 if config.simplified else 2

    # Pierwszy gracz: stały względem kolejności frakcji (nie RNG) —
    # przy stole: ustalacie sami; remis skillowy, nie kostka.
    state = GameState(
        players=players,
        order=list(config.factions),
        cards=all_cards,
        threshold=config.threshold,
        max_eras=config.max_eras,
        first_player_idx=0,
        relic_pool=pool,
        relics_on_board=relics_on_board,
        clue_pool=4 if config.simplified else 6,
        time_deck=time_ids,
        rng_seed=config.seed,
    )
    for i in range(open_count):
        loc = LocationId.GILDIA if i % 2 == 0 else LocationId.RYNEK
        if state.relic_pool > 0:
            state.relics_on_board[loc] += 1
            state.relic_pool -= 1

    # Mulligan skillowy: każdy może wymienić do 2 najsłabszych kart (1×)
    _opening_mulligan(state, rng)
    return state


def _opening_mulligan(state: GameState, rng: random.Random) -> None:
    """Wymiana do 2 kart o najniższym score (deterministyczny względem seed)."""
    for faction in state.order:
        p = state.player(faction)
        if len(p.hand) < 2 or not p.deck:
            continue

        def rough_score(cid: str) -> float:
            c = state.cards[cid]
            s = 1.0 - 0.15 * c.cost
            if c.heresy >= 2:
                s -= 0.3
            if c.target_heresy > 0:
                s += 0.5
            # frakcyjne preferencje
            tags = set(c.tags)
            if faction == FactionId.CIENIE_AL_ANDALUS and ("relikwia" in tags or "ewakuacja" in tags):
                s += 1.0
            if faction == FactionId.KORONA_BORGIOWIE and ("kontrola" in tags or "dekret" in tags):
                s += 1.0
            if faction == FactionId.SWIETE_OFICJUM and ("proces" in tags or "oblawa" in tags):
                s += 1.0
            if faction == FactionId.KABALA_TOLEDO and ("wskazowka" in tags or "kodeks" in tags):
                s += 1.0
            if faction == FactionId.GILDIA_CIENI and ("wrabianie" in tags or c.target_heresy > 0):
                s += 1.0
            return s

        ranked = sorted(p.hand, key=rough_score)
        to_mull = [cid for cid in ranked[:2] if rough_score(cid) < 1.0]
        for cid in to_mull:
            if not p.deck:
                break
            p.hand.remove(cid)
            p.deck.append(cid)
            # dobierz wierzch (bez pełnego shuffle mid-mulligan — skill/determinism)
            p.hand.append(p.deck.pop(0))
        if to_mull:
            rng.shuffle(p.deck)
