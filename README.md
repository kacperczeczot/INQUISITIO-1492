# INQUISITIO 1492: Cienie Toledo

Karcianka z planszą (**3–5 graczy**, 60–90+ min) osadzona w XV-wiecznej Hiszpanii. Ciężka **intryga polityczna**: Herezja, Wielki Inkwizytor, Lochy/Marionetki, Haki, karty signature.

> Oficjalna historia 1492 roku to zasłona. Pod Toledo i Alhambrą leżą *Fragmenty Przedwiecznego Kodeksu*. Inkwizycja nie poluje na heretyków — poluje na Relikwie.

## Status

**Prototyp warstwy C** (pełne mechaniki) — gotowy do pierwszej sesji ludzkiej.  
A/B w sim = teach / izolacja talii, nie osobny PnP.

| | |
| :--- | :--- |
| GDD | [`docs/gdd/Inquisitio_1492_GDD.md`](docs/gdd/Inquisitio_1492_GDD.md) |
| Zasady (hub) | [`docs/rules/README.md`](docs/rules/README.md) |
| Księga zasad / słownik | [`docs/rules/ksiega.md`](docs/rules/ksiega.md) · [`docs/rules/slownik.md`](docs/rules/slownik.md) |
| Setupy | [`data/playtesting/setups.md`](data/playtesting/setups.md) |
| Balans | [`data/playtesting/balance-notes.md`](data/playtesting/balance-notes.md) |
| Sim | [`sim/README.md`](sim/README.md) |
| Roadmap | [`docs/roadmap.md`](docs/roadmap.md) |

## Struktura

```
docs/           # GDD, zasady, lore, roadmap
game/           # Frakcje, karty, plansza, mechaniki, komponenty
sim/            # Silnik + agenci + metryki
assets/         # PnP HTML (UI-only)
data/playtesting/    # Setupy, balans, sesje
tools/          # Generator PnP, katalog kart
```

## Frakcje i Cele Zwycięstwa (Kanon 4p)

| Frakcja | Cel (Kanon 4p) |
| :--- | :--- |
| **Święte Oficjum** | **7 Stosy** (spaleni agenci) **lub 3 Skazania** Werdyktem |
| **Cienie Al-Andalus** | **2 Relikwie** + ścieżka |
| **Korona & Borgiowie** | **2 Dekrety** |
| **Kabała z Toledo** | **3 Fragmenty** (od Ery 6) |
| **Gildia Cieni** | **9 Upadki** |

Szczegóły: [`game/factions/`](game/factions/) · [`docs/rules/ksiega.md`](docs/rules/ksiega.md).

## Szybki start

1. Zasady → `docs/rules/ksiega.md` · lookup → `docs/rules/slownik.md`
2. Setup → `data/playtesting/setups.md`
3. Karty → `game/cards/` · zbiorczo: `game/cards/KATALOG.md`
4. Feel: `cd sim && python -m inquisitio feel --setup 3p-oficjum-alandalus-korona --seed 42 --layer C`
5. Matryca: `python -m inquisitio matrix --games 100 --layers C --seed 42`
6. PnP: `python tools/pnp/generate.py` → `assets/prototypes/`
7. Po sesji → `data/playtesting/sessions/_TEMPLATE.md`
