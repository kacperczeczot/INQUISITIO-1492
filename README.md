# INQUISITIO 1492: Cienie Toledo

Karcianka z planszą (2–5 graczy, 60–90+ min) osadzona w XV-wiecznej Hiszpanii epoki Reconquisty. Budowanie intrygi, ukryta tożsamość, pozycjonowanie agentów i asymetryczna walka o wpływy — w estetyce mrocznego pixel artu.

> Oficjalna historia 1492 roku to zasłona. Pod Toledo i Alhambrą leżą *Fragmenty Przedwiecznego Kodeksu*. Inkwizycja nie poluje na heretyków — poluje na Relikwie.

## Status

Faza 2 w toku — prototyp papierowy + infrastruktura playtest + **silnik symulacji intryg** (`sim/`).

Pełny dokument koncepcyjny: [`docs/gdd/Inquisitio_1492_GDD.md`](docs/gdd/Inquisitio_1492_GDD.md)  
Szkic zasad: [`docs/rules/README.md`](docs/rules/README.md)  
Setupy / protokół balansu: [`playtesting/setups.md`](playtesting/setups.md), [`playtesting/balance-notes.md`](playtesting/balance-notes.md)  
Symulacja: [`sim/README.md`](sim/README.md)

## Struktura repozytorium

```
docs/           # GDD, zasady, lore
game/           # Dane gry: frakcje, karty, plansza, mechaniki
sim/            # Silnik symulacji + agenci intrygi
assets/         # Grafiki, ikony, prototypy wizualne
playtesting/    # Notatki z testów, raporty sim
```

| Ścieżka | Zawartość |
| :--- | :--- |
| `docs/gdd/` | Dokument koncepcyjny (GDD) |
| `docs/rules/` | Zasady gry (rulebook) |
| `docs/lore/` | Świat i fabuła |
| `game/factions/` | Opisy 5 asymetrycznych frakcji |
| `game/cards/` | Karty frakcji + Talia Czasu |
| `game/board/` | Lokacje i mechanika podwójnego dna |
| `game/mechanics/` | Poziom Herezji i inne systemy |
| `game/components/` | Lista komponentów fizycznych |
| `playtesting/` | Sesje testowe i notatki balansu |
| `sim/` | Silnik symulacji (agenci intrygi, batch A/B) |

## Frakcje

| Frakcja | Cel zwycięstwa |
| :--- | :--- |
| **Święte Oficjum** | Skazać 2 Agentów na stos |
| **Cienie Al-Andalus** | Ewakuować 2 Relikwie poza planszę |
| **Korona & Borgiowie** | Kontrola Pałacu **2** + Rynku **2** |
| **Kabała z Toledo** | Zebrać 4 Wskazówki Kodeksu |
| **Gildia Cieni** | Doprowadzić do upadku 2 frakcji |

## Roadmap

1. ~~Prototyp 10 kart startowych na każdą frakcję~~ ✅
2. Testy balansu Toru Herezji (próg oskarżenia 7 vs 8)
3. Ikonografia pixel art (intrygi, skrytobójstwo, relikwie)

Szczegóły: [`docs/roadmap.md`](docs/roadmap.md)

## Szybki start (projektanci)

1. Przeczytaj GDD → `docs/gdd/`
2. Szkic zasad prototypu → `docs/rules/`
3. Wybierz setup sesji → `playtesting/setups.md`
4. Sprawdź frakcję → `game/factions/`
5. Karty według schematu → `game/cards/SCHEMA.md`
6. Plansza / planszetka → `game/board/`
7. Po grze: notatka z `playtesting/sessions/_TEMPLATE.md`
8. Batch symulacji: `cd sim && python -m inquisitio compare --games 200`
