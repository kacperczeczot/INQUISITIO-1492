# INQUISITIO 1492: Cienie Toledo

Karcianka z planszą (2–5 graczy, 60–90+ min) osadzona w XV-wiecznej Hiszpanii epoki Reconquisty. Budowanie intrygi, ukryta tożsamość, pozycjonowanie agentów i asymetryczna walka o wpływy — w estetyce mrocznego pixel artu.

> Oficjalna historia 1492 roku to zasłona. Pod Toledo i Alhambrą leżą *Fragmenty Przedwiecznego Kodeksu*. Inkwizycja nie poluje na heretyków — poluje na Relikwie.

## Status

Faza koncepcyjna → prototyp talii startowych.

Pełny dokument koncepcyjny: [`docs/gdd/Inquisitio_1492_GDD.md`](docs/gdd/Inquisitio_1492_GDD.md)

## Struktura repozytorium

```
docs/           # GDD, zasady, lore
game/           # Dane gry: frakcje, karty, plansza, mechaniki
assets/         # Grafiki, ikony, prototypy wizualne
playtesting/    # Notatki z testów i balansu
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

## Frakcje

| Frakcja | Cel zwycięstwa |
| :--- | :--- |
| **Święte Oficjum** | Skazać 3 Agentów na stos |
| **Cienie Al-Andalus** | Ewakuować 2 Relikwie poza planszę |
| **Korona & Borgiowie** | Pełna kontrola Pałacu i Rynku |
| **Kabała z Toledo** | Zebrać 4 Wskazówki Kodeksu |
| **Gildia Cieni** | Doprowadzić do upadku 2 frakcji |

## Roadmap

1. Prototyp 10 kart startowych na każdą frakcję
2. Testy balansu Toru Herezji (próg oskarżenia 7 vs 8)
3. Ikonografia pixel art (intrygi, skrytobójstwo, relikwie)

Szczegóły: [`docs/roadmap.md`](docs/roadmap.md)

## Szybki start (projektanci)

1. Przeczytaj GDD → `docs/gdd/`
2. Sprawdź frakcję → `game/factions/`
3. Dodawaj karty według schematu → `game/cards/SCHEMA.md`
4. Notuj wyniki testów → `playtesting/`
