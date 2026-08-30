#!/usr/bin/env python3
"""INQUISITIO-1492 — Narzędzie Porównania Bieżącego Stanu Kart z Punktami Odniesienia Genezy."""

import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
GENESIS_PATH = ROOT / "data" / "playtesting" / "baseline_deck_genesis.yaml"
CURRENT_PATH = ROOT / "data" / "game_config.yaml"


def main():
    if not GENESIS_PATH.exists():
        print(f"❌ Brak pliku genezy: {GENESIS_PATH}")
        sys.exit(1)

    with open(GENESIS_PATH, encoding="utf-8") as f:
        gen_data = yaml.safe_load(f)
    gen_cards = gen_data.get("cards", {})

    with open(CURRENT_PATH, encoding="utf-8") as f:
        cur_data = yaml.safe_load(f)
    cur_cards = cur_data.get("cards", {})

    print("═════════════════════════════════════════════════════════════════════════")
    print(f"🏛️  RAPORT ODCHYLEŃ KART OD KANONICZNEJ GENEZY (Wersja: {cur_data.get('version', 'vSSOT')})")
    print("═════════════════════════════════════════════════════════════════════════\n")

    diffs = []
    identical = 0

    all_keys = sorted(set(gen_cards.keys()) | set(cur_cards.keys()))

    for cid in all_keys:
        if cid.startswith("time-"):
            continue
        g = gen_cards.get(cid, {})
        c = cur_cards.get(cid, {})

        if not g:
            diffs.append((cid, c.get("name", cid), ["Karta NOWA (brak w bazie genezy)"]))
            continue
        if not c:
            diffs.append((cid, g.get("name", cid), ["Karta USUNIĘTA z bieżącego SSOT"]))
            continue

        card_diffs = []
        name = c.get("name", g.get("name", cid))

        fields_to_check = ["cost", "gold", "heresy", "target_heresy", "action"]
        for f in fields_to_check:
            gv = g.get(f, 0 if f in ("cost", "gold", "heresy", "target_heresy") else "")
            cv = c.get(f, 0 if f in ("cost", "gold", "heresy", "target_heresy") else "")
            if gv != cv:
                card_diffs.append(f"{f}: {gv} → {cv}")

        if card_diffs:
            diffs.append((cid, name, card_diffs))
        else:
            identical += 1

    print(f"📊 Karty identyczne z bazą genezy: {identical} / {len(all_keys)}")
    print(f"🔄 Karty z modyfikacjami balansu: {len(diffs)} / {len(all_keys)}\n")

    if diffs:
        print("─────────────────────────────────────────────────────────────────────────")
        print("ZMODYFIKOWANE KARTY (Bieżący SSOT vs Geneza Utworzenia):")
        print("─────────────────────────────────────────────────────────────────────────")
        for cid, name, changes in diffs:
            print(f"  • [{cid}] {name}:")
            for ch in changes:
                print(f"      - {ch}")
        print()
    else:
        print("✅ Wszystkie karty są w 100% zgodne ze swoją bazową genezą!")


if __name__ == "__main__":
    main()
