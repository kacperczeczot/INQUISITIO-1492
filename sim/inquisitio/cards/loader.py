"""Card loader — markdown YAML frontmatter from game/cards."""
from __future__ import annotations

import re
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
    cost: int = 0  # alias of cost_gold (sim engine)
    cost_gold: int = 0
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
    effect: str = ""
    heresy_text: str = ""
    lore: str = ""
    table_note: str = ""  # deprecated; kept for compat, unused
    text: str = ""
    raw: dict[str, Any] = field(default_factory=dict)

    @property
    def type_label(self) -> str:
        """Human label for PnP, e.g. Akcja."""
        labels = {
            "akcja": "Akcja",
            "reakcja": "Reakcja",
            "permanent": "Permanent",
            "signature": "Specjalna",
            "wydarzenie": "Wydarzenie",
        }
        return labels.get(self.type, self.type.title())


_CACHE: dict[str, Card] | None = None


def _parse_md(path: Path) -> Card | None:
    if path.name.upper() in ("SCHEMA.MD", "KATALOG.MD", "README.MD"):
        return None
    text = path.read_text(encoding="utf-8")
    parts = text.split("---")
    for i in range(len(parts) - 1):
        try:
            meta = yaml.safe_load(parts[i])
            if isinstance(meta, dict) and "id" in meta and "faction" in meta:
                body = "---".join(parts[i + 1 :]).strip()
                cost_gold = int(meta.get("cost_gold", meta.get("cost") or 0))
                effect = str(meta.get("effect") or "").strip()
                heresy_text = str(meta.get("heresy_text") or "").strip()
                lore = str(meta.get("lore") or "").strip()
                legacy_note = str(meta.get("table_note") or "").strip()
                if legacy_note and legacy_note not in lore:
                    lore = f"{lore} {legacy_note}".strip() if lore else legacy_note

                if not effect and body:
                    m = re.search(
                        r"\*\*Efekt:\*\*\s*(.+?)(?:\n\n|\*\*[A-ZĄĆĘŁŃÓŚŹŻ]|\Z)",
                        body,
                        re.S,
                    )
                    if m:
                        effect = re.sub(r"\s+", " ", m.group(1)).strip()
                    m2 = re.search(
                        r"\*\*Przy stole:\*\*\s*(.+?)(?:\n\n|\*\*[A-ZĄĆĘŁŃÓŚŹŻ]|\Z)",
                        body,
                        re.S,
                    )
                    if m2:
                        przy = re.sub(r"\s+", " ", m2.group(1)).strip()
                        if przy and przy not in lore:
                            lore = f"{lore} {przy}".strip() if lore else przy

                return Card(
                    id=str(meta["id"]),
                    name=str(meta.get("name", meta["id"])),
                    faction=str(meta.get("faction", "")),
                    type=str(meta.get("type", "akcja")),
                    cost=cost_gold,
                    cost_gold=cost_gold,
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
                    effect=effect,
                    heresy_text=heresy_text,
                    lore=lore,
                    table_note="",
                    text=body,
                    raw=meta,
                )
        except Exception:
            continue
    return None


def load_all_cards(force: bool = False, card_overrides: dict | None = None) -> dict[str, Card]:
    global _CACHE
    if _CACHE is None or force:
        cards: dict[str, Card] = {}
        for path in CARDS_ROOT.rglob("*.md"):
            if path.name.upper() == "SCHEMA.MD" or path.name == "SCHEMA.md":
                continue
            c = _parse_md(path)
            if c:
                cards[c.id] = c
        _CACHE = cards

    if not card_overrides:
        return _CACHE

    # Return deep copies with applied overrides
    import copy
    modified_cards = copy.deepcopy(_CACHE)
    for cid, ov in card_overrides.items():
        if cid in modified_cards:
            card = modified_cards[cid]
            for field_name, val in ov.items():
                if hasattr(card, field_name):
                    setattr(card, field_name, val)
                    if field_name == "cost":
                        card.cost_gold = val
                    elif field_name == "cost_gold":
                        card.cost = val
    return modified_cards


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
