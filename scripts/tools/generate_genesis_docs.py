#!/usr/bin/env python3
"""Generator kanonicznej dokumentacji punktów odniesienia i genezy talii."""

import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
GENESIS_PATH = ROOT / "data" / "playtesting" / "baseline_deck_genesis.yaml"
OUTPUT_PATH = ROOT / "docs" / "game" / "cards" / "PUNKTY_ODNIESIENIA_GENEZY_TALII.md"

with open(GENESIS_PATH, encoding="utf-8") as f:
    genesis = yaml.safe_load(f)

cards = genesis.get("cards", {})

faction_names = {
    "so": ("Święte Oficjum", "⛪"),
    "caa": ("Cienie Al-Andalus", "🕌"),
    "kb": ("Korona Borgiowie", "👑"),
    "kt": ("Kabała z Toledo", "📜"),
    "gc": ("Gildia Cieni", "🗡️"),
}

doc = [
    "# 🏛️ Punkty Odniesienia i Geneza Talii (Kanon Kart w Momencie Utworzenia)",
    "",
    "> **Cel Dokumentu:** Trwały punkt odniesienia dla projektanta gry, audytora i systemu balansu.",
    "> Pozwala w ułamku sekundy zweryfikować, jak dana karta została pierwotnie zaprojektowana w momencie jej powstania oraz jakie odchylenia wprowadzono w trakcie strojenia parametrów.",
    "",
    "## 📜 Kamienie Milowe Powstania Talii:",
    "1. **Wersja `v0.0` (13 sierpnia 2026):** Powstanie bazowych kart **`01 .. 10`** dla 5 frakcji (50 kart).",
    "2. **Wersja `v0.40` (15 sierpnia 2026):** Refaktor i wdrożenie 10 kart Edyktów Ery Kroniki Dziejów (`time-01 .. 10`).",
    "3. **Wersja `v0.76` (17 sierpnia 2026):** Wprowadzenie kart **`11` i `12`** dla 5 frakcji (rozszerzenie talii do 70 kart).",
    "",
    "---",
    "",
]

for fac_code, (fac_name, icon) in faction_names.items():
    doc.append(f"## {icon} {fac_name} (`{fac_code}`)")
    doc.append("")
    doc.append("| ID | Nazwa | Typ / Rola | Koszt | Złoto | Herezja | Rywal H | Działanie Bazowe | Geneza |")
    doc.append("| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :---: |")

    for i in range(1, 13):
        cid = f"{fac_code}-{i:02d}"
        c = cards.get(cid, {})
        name = c.get("name", "—")
        ctype = c.get("type", "akcja")
        cost = c.get("cost", 0)
        gold = c.get("gold", "—")
        heresy = c.get("heresy", 0)
        theresy = c.get("target_heresy", "—")
        act = c.get("action", "—")
        genesis_ver = "`v0.76`" if i in (11, 12) else "`v0.0`"

        doc.append(
            f"| `{cid}` | **{name}** | {ctype} | {cost} zł | {gold} | +{heresy}H | {theresy} | `{act}` | {genesis_ver} |"
        )
    doc.append("")

doc.extend(
    [
        "---",
        "",
        "## 🛠️ Jak korzystać z Punktów Odniesienia przy Edycji Kart?",
        "",
        "1. **Porównanie z bazą:** Przed każdą modyfikacją karty w `game_config.yaml` uruchom skrypt:",
        "   ```bash",
        "   python3 scripts/sim/compare_with_genesis.py",
        "   ```",
        "2. **Tożsamość karty:** Jeśli karta taktyczna oddala się zbyt daleko od swojej roli bazowej (np. dostaje złoto lub traci swój unikalny mechanizm), należy zweryfikować, czy zmiana nie niszczy zamysłu Game Designu.",
        "3. **Twarde granice:** Wszelkie zmiany muszą mieścić się w limitach: `cost: 0..5`, `gold: 0..3`, `heresy: 0..3`, `target_heresy: 0..2`.",
    ]
)

OUTPUT_PATH.write_text("\n".join(doc) + "\n", encoding="utf-8")
print(f"Wygenerowano poprawnie {OUTPUT_PATH}")
