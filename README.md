[Strona główna](README.md)


# INQUISITIO 1492: Cienie Toledo

Karcianka z planszą (**3–5 graczy**, 60–90+ min) osadzona w XV-wiecznej Hiszpanii. Ciężka **intryga polityczna**: Herezja, Wielki Inkwizytor, Lochy/Podwójni, Haki, karty signature.

> Oficjalna historia 1492 roku to zasłona. Pod Toledo i Alhambrą leżą *Fragmenty Przedwiecznego Kodeksu*. Inkwizycja nie poluje na heretyków — poluje na Relikwie.

## Status

**Prototyp warstwy C** (pełne mechaniki) — gotowy do pierwszej sesji ludzkiej.  
A/B w sim = teach / izolacja talii, nie osobny PnP.

| | |
| :--- | :--- |
| GDD | [`docs/gdd/Inquisitio_1492_GDD.md`](docs/gdd/Inquisitio_1492_GDD.md) |
| Zasady (hub) | [`docs/rules/README.md`](docs/rules/README.md) |
| Teach / księga / słownik | [`docs/rules/teach-sheet.md`](docs/rules/teach-sheet.md) · [`ksiega.md`](docs/rules/ksiega.md) · [`slownik.md`](docs/rules/slownik.md) |
| Setupy | [`playtesting/setups.md`](playtesting/setups.md) |
| Balans | [`playtesting/balance-notes.md`](playtesting/balance-notes.md) |
| Sim | [`sim/README.md`](sim/README.md) |
| Roadmap | [`docs/roadmap.md`](docs/roadmap.md) |

## Struktura

```
docs/           # GDD, zasady, lore, roadmap
game/           # Frakcje, karty, plansza, mechaniki, komponenty
sim/            # Silnik + agenci + metryki
assets/         # PnP HTML (UI-only)
playtesting/    # Setupy, balans, sesje
tools/          # Generator PnP, katalog kart
```

## Frakcje (cele C)

| Frakcja | Cel |
| :--- | :--- |
| **Święte Oficjum** | 3 Stosy **lub** skazania Werdyktem (2@3p / 3@4p / 4@5p) |
| **Cienie Al-Andalus** | 2 Relikwie + ścieżka (Podwójny / cichy exit / szlak / Era 6@3p / 5@4–5p) |
| **Korona & Borgiowie** | 2 Dekrety + ≥0 Haków (Era 5); ≥1 Hak (4–5p); 4p+ też 1 Dekret+2 Haki od Ery 6 |
| **Kabała z Toledo** | 3 Fragmenty + Herezja 3–8 (Era 7@3p / 6@4–5p) |
| **Gildia Cieni** | 2 upadki (3 bez Oficjum) |

Szczegóły: [`game/factions/`](game/factions/) · [`docs/rules/ksiega.md`](docs/rules/ksiega.md).

## Szybki start

1. Nauka → `docs/rules/teach-sheet.md` · lookup → `docs/rules/slownik.md` · księga → `docs/rules/ksiega.md`
2. Setup → `playtesting/setups.md`
3. Karty → `game/cards/` · zbiorczo: `game/cards/KATALOG.md`
4. Feel: `cd sim && python -m inquisitio feel --setup 3p-oficjum-alandalus-korona --seed 42 --layer C`
5. Matryca: `python -m inquisitio matrix --games 100 --layers C --seed 42`
6. PnP: `python tools/pnp/generate.py` → `assets/prototypes/`
7. Po sesji → `playtesting/sessions/_TEMPLATE.md`
