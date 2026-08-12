#!/usr/bin/env python3
"""Zbuduj zbiorczy katalog kart → game/cards/KATALOG.md (źródło: pliki YAML)."""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "sim"))

from inquisitio.cards.loader import Card, load_all_cards  # noqa: E402

OUT = REPO / "game" / "cards" / "KATALOG.md"

FACTION_ORDER = [
    ("swiete-oficjum", "Święte Oficjum"),
    ("cienie-al-andalus", "Cienie Al-Andalus"),
    ("korona-borgiowie", "Korona & Borgiowie"),
    ("kabala-toledo", "Kabała z Toledo"),
    ("gildia-cieni", "Gildia Cieni"),
    ("time", "Talia Czasu"),
]

DISPLAY_FIELDS = [
    "id",
    "name",
    "faction",
    "type",
    "layer",
    "cost_gold",
    "heresy",
    "heresy_text",
    "effect",
    "lore",
    "tags",
    "status",
]


def _esc_cell(s: str) -> str:
    return (s or "").replace("|", "\\|").replace("\n", " ").strip()


def _field_value(c: Card, key: str) -> str:
    if key == "tags":
        return ", ".join(c.tags) if c.tags else "—"
    if key == "cost_gold":
        return str(c.cost_gold if c.cost_gold else c.cost)
    if key == "heresy_text":
        return _esc_cell(c.heresy_text) or "—"
    if key == "effect":
        return _esc_cell(c.effect) or "—"
    if key == "lore":
        return _esc_cell(c.lore) or "—"
    raw = c.raw
    v = raw.get(key, getattr(c, key, None))
    if v is None or v == "":
        return "—"
    if isinstance(v, list):
        return ", ".join(str(x) for x in v) or "—"
    return _esc_cell(str(v))


def _section(title: str, cards: list[Card]) -> str:
    lines = [f"## {title}", "", f"Kart: **{len(cards)}**", ""]
    for c in sorted(cards, key=lambda x: x.id):
        lines.append(f"### `{c.id}` — {c.name}")
        lines.append("")
        lines.append("| Pole | Wartość |")
        lines.append("| :--- | :--- |")
        for key in DISPLAY_FIELDS:
            lines.append(f"| `{key}` | {_field_value(c, key)} |")
        lines.append("")
    return "\n".join(lines)


def build() -> str:
    cards = load_all_cards(force=True)
    by_faction: dict[str, list[Card]] = {}
    for c in cards.values():
        by_faction.setdefault(c.faction, []).append(c)

    parts = [
        "# Katalog kart — INQUISITIO 1492",
        "",
        "> **Auto-generowane.** Nie edytuj ręcznie.",
        "> Źródło: pojedyncze pliki w `game/cards/factions/` i `game/cards/time-deck/`.",
        "> Odśwież: `python3 tools/cards/build_catalog.py`",
        "",
        f"Łącznie kart: **{len(cards)}**",
        "",
        "Schemat pól: [`SCHEMA.md`](SCHEMA.md). "
        "Słownictwo `effect`: [`../mechanics/leksykon.md`](../mechanics/leksykon.md).",
        "",
        "## Spis",
        "",
    ]
    for fid, label in FACTION_ORDER:
        n = len(by_faction.get(fid, []))
        parts.append(f"- [{label}](#{fid}) ({n})")
    parts.append("")

    known = {fid for fid, _ in FACTION_ORDER}
    for fid, label in FACTION_ORDER:
        group = by_faction.get(fid, [])
        if not group:
            continue
        parts.append(f'<a id="{fid}"></a>')
        parts.append("")
        parts.append(_section(label, group))

    for fid in sorted(set(by_faction) - known):
        parts.append(f'<a id="{fid}"></a>')
        parts.append("")
        parts.append(_section(fid, by_faction[fid]))

    return "\n".join(parts).rstrip() + "\n"


def main() -> None:
    text = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text, encoding="utf-8")
    print(f"Wrote {OUT.relative_to(REPO)} ({len(text.splitlines())} lines)")


if __name__ == "__main__":
    main()
