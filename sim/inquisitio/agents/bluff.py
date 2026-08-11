from __future__ import annotations

import random

from inquisitio.agents.politics import BeliefState
from inquisitio.model import LOCATION_ORDER, FactionId, LocationId


PREFERRED: dict[FactionId, list[LocationId]] = {
    FactionId.SWIETE_OFICJUM: [LocationId.TRYBUNAL, LocationId.LOCHY, LocationId.RYNEK],
    FactionId.CIENIE_AL_ANDALUS: [LocationId.GILDIA, LocationId.LOCHY, LocationId.RYNEK],
    FactionId.KORONA_BORGIOWIE: [LocationId.PALAC, LocationId.RYNEK, LocationId.TRYBUNAL],
    FactionId.KABALA_TOLEDO: [LocationId.GILDIA, LocationId.TRYBUNAL, LocationId.LOCHY],
    FactionId.GILDIA_CIENI: [LocationId.GILDIA, LocationId.RYNEK, LocationId.LOCHY],
}


def choose_location(
    *,
    faction: FactionId,
    true_intent_loc: LocationId,
    belief: BeliefState,
    rivals: list[FactionId],
    rng: random.Random,
    feint_bias: float,
) -> tuple[LocationId, bool]:
    """Return (location, is_feint). Feint misdirects Oficjum/Gildia watchers."""
    watchers = [f for f in rivals if f in (FactionId.SWIETE_OFICJUM, FactionId.GILDIA_CIENI)]
    should_feint = bool(watchers) and rng.random() < feint_bias
    if not should_feint:
        return true_intent_loc, False
    # Feint: play away from true intent, preferably where a watcher expects us
    decoys = [loc for loc in LOCATION_ORDER if loc != true_intent_loc]
    for w in watchers:
        guessed = belief.likely_location(faction)
        if guessed and guessed in decoys:
            # avoid playing exactly where they already track us hard — go elsewhere
            decoys = [d for d in decoys if d != guessed] or decoys
    return rng.choice(decoys), True


def true_intent_location(faction: FactionId, state, card_location: LocationId) -> LocationId:
    if card_location != LocationId.ANY:
        return card_location
    prefs = PREFERRED.get(faction, list(LOCATION_ORDER))
    # Bias toward board presence
    p = state.player(faction)
    for loc in prefs:
        if p.agents_in(loc):
            return loc
    # relics / control bias
    if faction == FactionId.CIENIE_AL_ANDALUS:
        for loc in LOCATION_ORDER:
            if state.relics_on_board.get(loc, 0) > 0:
                return loc
    if faction == FactionId.KORONA_BORGIOWIE:
        if p.control_palace < 2:
            return LocationId.PALAC
        if p.control_market < 2:
            return LocationId.RYNEK
        return LocationId.PALAC
    return prefs[0]
