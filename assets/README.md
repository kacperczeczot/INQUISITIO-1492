[Strona główna](../README.md) > [Zasoby](README.md)

---


# Assets

## Architektura PnP (obowiązująca)

```
[ Schemat mechaniki ]  ← tools/pnp/generate.py: węzły + ulice = graf NEIGHBORS + sloty
```

UI (sloty kart, Agenci, Inkwizytor, Tor Herezji, żetony) żyje **w kodzie**. Prototyp drukuje się UI-only (pergamin + etykiety tekstowe) — bez grafik w repo.

## Kolejność

1. Heavy sim + feel C — done (+1 złoto / turę)
2. PnP Layout C (UI) — struktura gotowa
3. Sesja ludzka C
4. Freeze → final art (poza repo do czasu freeze)

## Katalogi

| Ścieżka | Rola |
| :--- | :--- |
| `icons/` | Placeholder (`.gitkeep`) — na przyszłe symbole |
| `prototypes/` | **Jedyny** PnP HTML (warstwa C) |

## Generator

```bash
cd sim && source .venv/bin/activate && cd ..
python tools/pnp/generate.py
# → assets/prototypes/index.html
```

Paleta UI: czerwień / złoto / czerń / pergamin.
