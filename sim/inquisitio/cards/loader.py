from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

from inquisitio.model import Card, CardTier, CardType, FactionId, LocationId

_FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)


def _repo_root() -> Path:
    # sim/inquisitio/cards/loader.py -> repo root
    return Path(__file__).resolve().parents[3]


def default_cards_root() -> Path:
    return _repo_root() / "game" / "cards"


def _parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    m = _FRONTMATTER.match(text.strip())
    if not m:
        raise ValueError("missing YAML frontmatter")
    data = yaml.safe_load(m.group(1)) or {}
    body = m.group(2).strip()
    return data, body


def _as_location(value: str) -> LocationId:
    value = (value or "any").strip().lower()
    try:
        return LocationId(value)
    except ValueError:
        return LocationId.ANY


def _as_faction(value: str) -> FactionId:
    return FactionId(value.strip().lower())


def _as_type(value: str) -> CardType:
    return CardType(value.strip().lower())


def _as_tier(value: str) -> CardTier:
    return CardTier((value or "basic").strip().lower())


def card_from_dict(data: dict[str, Any], body: str = "") -> Card:
    tags = data.get("tags") or []
    if isinstance(tags, str):
        tags = [tags]
    return Card(
        id=str(data["id"]),
        name=str(data["name"]),
        faction=_as_faction(str(data["faction"])),
        type=_as_type(str(data.get("type", "akcja"))),
        tier=_as_tier(str(data.get("tier", "basic"))),
        cost=int(data.get("cost", 0)),
        heresy=int(data.get("heresy", 0)),
        target_heresy=int(data.get("target_heresy", 0)),
        location=_as_location(str(data.get("location", "any"))),
        agents=int(data.get("agents", 0)),
        tags=tuple(str(t) for t in tags),
        status=str(data.get("status", "draft")),
        effect_text=body,
        raw=dict(data),
    )


def load_card_file(path: Path) -> Card:
    text = path.read_text(encoding="utf-8")
    data, body = _parse_frontmatter(text)
    return card_from_dict(data, body)


class CardLoader:
    def __init__(self, cards_root: Path | None = None) -> None:
        self.cards_root = cards_root or default_cards_root()
        self._by_id: dict[str, Card] = {}

    def load_all(self) -> dict[str, Card]:
        self._by_id.clear()
        files: list[Path] = []
        faction_dir = self.cards_root / "factions"
        if faction_dir.exists():
            files.extend(sorted(faction_dir.glob("*/*.md")))
        time_dir = self.cards_root / "time-deck"
        if time_dir.exists():
            files.extend(sorted(time_dir.glob("*.md")))
        for path in files:
            if path.name == "SCHEMA.md":
                continue
            card = load_card_file(path)
            if card.id in self._by_id:
                raise ValueError(f"duplicate card id: {card.id}")
            self._by_id[card.id] = card
        return dict(self._by_id)

    def get(self, card_id: str) -> Card:
        if not self._by_id:
            self.load_all()
        return self._by_id[card_id]

    def by_faction(self, faction: FactionId) -> list[Card]:
        if not self._by_id:
            self.load_all()
        return sorted(
            (c for c in self._by_id.values() if c.faction == faction),
            key=lambda c: c.id,
        )

    @property
    def all_cards(self) -> dict[str, Card]:
        if not self._by_id:
            self.load_all()
        return dict(self._by_id)
