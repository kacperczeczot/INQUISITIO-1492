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
    TIME = "time"


class LocationId(str, Enum):
    TRYBUNAL = "trybunal"
    PALAC = "palac"
    LOCHY = "lochy"
    RYNEK = "rynek"
    GILDIA = "gildia"
    ANY = "any"


LOCATION_ORDER: list[LocationId] = [
    LocationId.TRYBUNAL,
    LocationId.PALAC,
    LocationId.LOCHY,
    LocationId.RYNEK,
    LocationId.GILDIA,
]

NEIGHBORS: dict[LocationId, list[LocationId]] = {
    LocationId.TRYBUNAL: [LocationId.PALAC],
    LocationId.PALAC: [LocationId.TRYBUNAL, LocationId.LOCHY],
    LocationId.LOCHY: [LocationId.PALAC, LocationId.RYNEK],
    LocationId.RYNEK: [LocationId.LOCHY, LocationId.GILDIA],
    LocationId.GILDIA: [LocationId.RYNEK],
}


class CardType(str, Enum):
    AKCJA = "akcja"
    REAKCJA = "reakcja"
    PERMANENT = "permanent"
    WYDARZENIE = "wydarzenie"


class CardTier(str, Enum):
    BASIC = "basic"
    ADVANCED = "advanced"
    SIGNATURE = "signature"


@dataclass(frozen=True)
class Card:
    id: str
    name: str
    faction: FactionId
    type: CardType
    tier: CardTier
    cost: int
    heresy: int
    target_heresy: int
    location: LocationId
    agents: int
    tags: tuple[str, ...] = ()
    status: str = "draft"
    effect_text: str = ""
    raw: dict[str, Any] = field(default_factory=dict, compare=False, hash=False)

    @property
    def is_reaction(self) -> bool:
        return self.type == CardType.REAKCJA

    @property
    def is_permanent(self) -> bool:
        return self.type == CardType.PERMANENT


def heresy_zone(value: int) -> str:
    if value <= 3:
        return "czysta"
    if value <= 6:
        return "obserwowana"
    return "krytyczna"
