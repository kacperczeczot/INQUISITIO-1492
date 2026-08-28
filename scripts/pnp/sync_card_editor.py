#!/usr/bin/env python3
"""
Embeds all 50 cards from game_config.yaml into assets/prototypes/card-editor.html as CARDS_DATABASE JS object.
Allows the HTML PnP Card Editor to load, edit, preview, and export any card from the game.
"""
from __future__ import annotations
import json
import re
from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
CONFIG_PATH = REPO_ROOT / "data/game_config.yaml"
EDITOR_PATH = REPO_ROOT / "assets" / "prototypes" / "card-editor.html"
CARDS_DIR = REPO_ROOT / "docs" / "game" / "cards"


def load_md_extras():
    """Load lore & heresy_text from card markdown files."""
    extras = {}
    for path in CARDS_DIR.rglob("*.md"):
        if path.name.upper() in ("SCHEMA.MD", "KATALOG.MD", "README.MD"):
            continue
        content = path.read_text(encoding="utf-8")
        parts = content.split("---")
        if len(parts) >= 2:
            try:
                meta = yaml.safe_load(parts[1])
                if isinstance(meta, dict) and "id" in meta:
                    cid = str(meta["id"])
                    extras[cid] = {}
                    if "heresy_text" in meta:
                        extras[cid]["heresy_text"] = meta["heresy_text"]
                    if "lore" in meta:
                        extras[cid]["lore"] = meta["lore"]
            except Exception:
                pass
    return extras


def main():
    if not CONFIG_PATH.exists() or not EDITOR_PATH.exists():
        print("Missing CONFIG_PATH or EDITOR_PATH")
        return

    with open(CONFIG_PATH, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    cards = cfg.get("cards", {})
    extras = load_md_extras()

    # Merge extras into cards
    full_db = {}
    for cid, data in cards.items():
        card_entry = dict(data)
        if cid in extras:
            if "heresy_text" in extras[cid]:
                card_entry["heresy_text"] = extras[cid]["heresy_text"]
            if "lore" in extras[cid]:
                card_entry["lore"] = extras[cid]["lore"]
        full_db[cid] = card_entry

    js_db = json.dumps(full_db, ensure_ascii=False, indent=2)

    html = EDITOR_PATH.read_text(encoding="utf-8")

    # Replace CARDS_DATABASE definition
    pattern = re.compile(r"const CARDS_DATABASE = \{.*?\};", re.DOTALL)
    new_code = f"const CARDS_DATABASE = {js_db};"

    if pattern.search(html):
        html = pattern.sub(new_code, html)
    else:
        # Insert before AVAILABLE_TAGS
        html = html.replace("const AVAILABLE_TAGS =", f"{new_code}\n\nconst AVAILABLE_TAGS =")

    ver = cfg.get("version", "v1.0-alpha.1")
    html = re.sub(r'<span id="prev-meta-ver">.*?</span>', f'<span id="prev-meta-ver">{ver}</span>', html)
    html = re.sub(r"document\.getElementById\('prev-meta-ver'\)\.textContent = '.*?';", f"document.getElementById('prev-meta-ver').textContent = '{ver}';", html)

    EDITOR_PATH.write_text(html, encoding="utf-8")
    print(f"✅ Zsynchronizowano {len(full_db)} kart z `game_config.yaml` do `assets/prototypes/card-editor.html`!")


if __name__ == "__main__":
    main()
