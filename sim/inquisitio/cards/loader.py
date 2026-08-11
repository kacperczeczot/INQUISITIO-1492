"""Card loader — markdown YAML frontmatter from game/cards."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

# repo: sim/inquisitio/cards/loader.py -> parents[3] = repo root
REPO_ROOT = Path(__file__).resolve().parents[3]
CARDS_ROOT = REPO_ROOT / "game" / "cards"


@dataclass
class Card:
    id: str
    name: str
    faction: str
    type: str = "akcja"
    cost: int = 0
    heresy: int = 0
    target_heresy: int = 0
    location: str | None = None
    agents: int = 0
    tags: list[str] = field(default_factory=list)
    creates_hook: bool = False
    breaks_rule: bool = False
    gold: int = 0
    arrest: bool = False
    layer: str = "A"
    status: str = "prototyp"
    text: str = ""
    raw: dict[str, Any] = field(default_factory=dict)


_CACHE: dict[str, Card] | None = None


def _parse_md(path: Path) -> Card | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    meta = yaml.safe_load(parts[1]) or {}
    body = parts[2].strip()
    if "id" not in meta:
        return None
    return Card(
        id=str(meta["id"]),
        name=str(meta.get("name", meta["id"])),
        faction=str(meta.get("faction", "")),
        type=str(meta.get("type", "akcja")),
        cost=int(meta.get("cost") or 0),
        heresy=int(meta.get("heresy") or 0),
        target_heresy=int(meta.get("target_heresy") or 0),
        location=meta.get("location"),
        agents=int(meta.get("agents") or 0),
        tags=list(meta.get("tags") or []),
        creates_hook=bool(meta.get("creates_hook")),
        breaks_rule=bool(meta.get("breaks_rule")),
        gold=int(meta.get("gold") or 0),
        arrest=bool(meta.get("arrest")),
        layer=str(meta.get("layer") or "A"),
        status=str(meta.get("status") or "prototyp"),
        text=body,
        raw=meta,
    )


def load_all_cards(force: bool = False) -> dict[str, Card]:
    global _CACHE
    if _CACHE is not None and not force:
        return _CACHE
    cards: dict[str, Card] = {}
    for path in CARDS_ROOT.rglob("*.md"):
        if path.name.upper() == "SCHEMA.MD" or path.name == "SCHEMA.md":
            continue
        c = _parse_md(path)
        if c:
            cards[c.id] = c
    _CACHE = cards
    return cards


def cards_for_faction(faction: str, max_layer: str = "C") -> list[Card]:
    order = {"A": 0, "B": 1, "C": 2}
    cap = order.get(max_layer, 2)
    all_c = load_all_cards()
    out = [
        c
        for c in all_c.values()
        if c.faction == faction and order.get(c.layer, 2) <= cap
    ]
    out.sort(key=lambda c: c.id)
    return out


def time_cards(max_layer: str = "C") -> list[Card]:
    return cards_for_faction("time", max_layer=max_layer)
