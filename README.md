# INQUISITIO 1492: Cienie Toledo

Karcianka z planszą (**3–5 graczy**, 60–90+ min) osadzona w XV-wiecznej Hiszpanii. Ciężka **intryga polityczna**: Herezja, Wielki Inkwizytor, Lochy/Podwójni, Haki, karty signature — w estetyce mrocznego pixel artu.

> Oficjalna historia 1492 roku to zasłona. Pod Toledo i Alhambrą leżą *Fragmenty Przedwiecznego Kodeksu*. Inkwizycja nie poluje na heretyków — poluje na Relikwie.

## Status

**Prototyp** w przebudowie warstwowej **A → B → C**.

| Warstwa | Slice |
| :--- | :--- |
| **A** | Herezja + Inkwizytor + Werdykt + 5 prostych kart/frakcję |
| **B** | Lochy / Podwójni + Haki + karty narzędziowe |
| **C** | 10 kart/frakcję (signature) + Talia Czasu |

GDD: [`docs/gdd/Inquisitio_1492_GDD.md`](docs/gdd/Inquisitio_1492_GDD.md)  
Zasady: [`docs/rules/README.md`](docs/rules/README.md)  
Setupy: [`playtesting/setups.md`](playtesting/setups.md)  
Sim: [`sim/README.md`](sim/README.md)

## Struktura

```
docs/           # GDD, zasady, lore
game/           # Frakcje, karty, plansza, mechaniki, komponenty
sim/            # Silnik + agenci + metryki dramatu
assets/         # Pixel art scaffolding
playtesting/    # Sesje, balans dramatyczny, raporty sim
```

## Frakcje

| Frakcja | Cel |
| :--- | :--- |
| **Święte Oficjum** | 2 Stosy (Autodafé/Werdykt) lub 2 skazania z Krytycznej |
| **Cienie Al-Andalus** | 2 Relikwie ewakuowane (+ ścieżka Podwójny/unik Autodafé) |
| **Korona & Borgiowie** | 2 Dekrety signature + Haki na 2 graczach |
| **Kabała z Toledo** | 3 Fragmenty; Herezja 4–6 przy wygranej |
| **Gildia Cieni** | 2 upadki (Hak / Podwójny / spalona lokacja) |

## Roadmap

Warstwy danych **A→B→C** są w repo; otwarty jest **cykl stołu**: Solo Dev-Play → PnP → UX ludzkie → rulebook.  
Szczegóły: [`docs/roadmap.md`](docs/roadmap.md)

## Szybki start

1. GDD → `docs/gdd/`
2. Zasady → `docs/rules/`
3. Setup → `playtesting/setups.md`
4. Frakcja → `game/factions/`
5. SCHEMA → `game/cards/SCHEMA.md`
6. Sim / feel: `cd sim && python -m inquisitio run --games 50`
7. PnP → `assets/prototypes/` (gdy generator gotowy)
8. Po sesji ludzkiej → `playtesting/sessions/_TEMPLATE.md` (UX: downtime, AP, emocja Werdyktu)
