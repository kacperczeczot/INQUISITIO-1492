[Strona główna](../../README.md) > [Narzędzia](../README.md) > [PnP](README.md)

---


# tools/pnp

Generator Print & Play (HTML) — **UI-only** (SVG/CSS, bez grafik w repo).

```bash
cd sim && source .venv/bin/activate && cd ..
python tools/pnp/generate.py
# opcjonalnie: --bw (grayscale pod Xerox), --layer A|B
```

Karty czytają schemat z `game/cards/` (`effect`, `heresy`/`heresy_text`, `lore`, `cost_gold`).  
Layout PnP: HDR → slot art → EFFECT (banery) → lore — [`game/cards/SCHEMA.md`](../../game/cards/SCHEMA.md).  
Leksykon komend: [`game/mechanics/leksykon.md`](../../game/mechanics/leksykon.md).

Output: **`assets/prototypes/`** — jedna aktualna wersja (warstwa C).  
`--layer A|B` tylko do lokalnych eksperymentów (nadpisuje ten sam katalog).
