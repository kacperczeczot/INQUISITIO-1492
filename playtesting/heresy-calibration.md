# Kalibracja kosztów Herezji kart

Macierz startowa (Faza 1, `status: draft`). Po sesji uzupełnij kolumny **Ocena** i **Propozycja**.

Konwencja ze [`../game/cards/SCHEMA.md`](../game/cards/SCHEMA.md):

| `heresy` | Siła efektu (orientacyjnie) |
| ---: | :--- |
| 0 | Bezpieczna, słaba / utility |
| +1 | Solidna akcja |
| +2 | Silna / kluczowa |
| +3 | Niszczycielska / signature |

Wrabianie: niski `heresy` u siebie, wysoki `target_heresy`.

## Rozkład startowy (50 kart)

| heresy | Liczba kart |
| ---: | ---: |
| 0 | 26 |
| 1 | 13 |
| 2 | 9 |
| 3 | 2 |

Ocena: `słabe` · `OK` · `mocne` (względem konwencji i stołu). Propozycja: np. `heresy: 1→2` lub `—`.

## Święte Oficjum

| ID | Nazwa | Tier | heresy | target_heresy | Ocena | Propozycja |
| :--- | :--- | :--- | ---: | ---: | :--- | :--- |
| `so-01` | Proces Pokazowy | basic | 0 | 0 |  |  |
| `so-02` | Obława | basic | 0 | 0 |  |  |
| `so-03` | Wymuszenie Zeznania | basic | 1 | 1 |  |  |
| `so-04` | Autodafé | signature | 0 | 0 |  |  |
| `so-05` | Konfiskata | basic | 0 | 0 |  |  |
| `so-06` | Edykt Czystości | advanced | 0 | 0 |  |  |
| `so-07` | Familiariusz | basic | 0 | 0 |  |  |
| `so-08` | Świadek Koronny | advanced | 1 | 2 |  |  |
| `so-09` | Relikwiarz | advanced | 1 | 0 |  |  |
| `so-10` | Oczyść Miasto | signature | 2 | 0 |  |  |

## Cienie Al-Andalus

| ID | Nazwa | Tier | heresy | target_heresy | Ocena | Propozycja |
| :--- | :--- | :--- | ---: | ---: | :--- | :--- |
| `caa-01` | Zamach w Cieniu | signature | 2 | 0 |  |  |
| `caa-02` | Przejście Podziemiami | basic | 0 | 0 |  |  |
| `caa-03` | Fałszywy Trop | basic | 0 | 1 |  |  |
| `caa-04` | Przysięga Bractwa | basic | 0 | 0 |  |  |
| `caa-05` | Kurier Relikwii | advanced | 1 | 0 |  |  |
| `caa-06` | Szlak Morski | advanced | 1 | 0 |  |  |
| `caa-07` | Kaptur Nocy | basic | 0 | 0 |  |  |
| `caa-08` | Poświęcenie | signature | 3 | 0 |  |  |
| `caa-09` | Ukryta Kryjówka | basic | 0 | 0 |  |  |
| `caa-10` | Echo Alhambry | advanced | 2 | 0 |  |  |

## Korona & Borgiowie

| ID | Nazwa | Tier | heresy | target_heresy | Ocena | Propozycja |
| :--- | :--- | :--- | ---: | ---: | :--- | :--- |
| `kb-01` | Dekret Królewski | basic | 0 | 0 |  |  |
| `kb-02` | Przekupstwo Sędziego | advanced | 1 | 0 |  |  |
| `kb-03` | Pobór Podatków | basic | 0 | 0 |  |  |
| `kb-04` | List Żelazny | basic | 0 | 0 |  |  |
| `kb-05` | Faworyt Dworu | basic | 0 | 0 |  |  |
| `kb-06` | Fałszywe Akta | advanced | 1 | 1 |  |  |
| `kb-07` | Kontrola Rynku | advanced | 0 | 0 |  |  |
| `kb-08` | Sojusz Dynastyczny | basic | 0 | 0 |  |  |
| `kb-09` | Kapitan Straży | advanced | 1 | 0 |  |  |
| `kb-10` | Pieczęć Korony | signature | 2 | 0 |  |  |

## Kabała z Toledo

| ID | Nazwa | Tier | heresy | target_heresy | Ocena | Propozycja |
| :--- | :--- | :--- | ---: | ---: | :--- | :--- |
| `kt-01` | Zakazana Alchemia | advanced | 2 | 0 |  |  |
| `kt-02` | Fragment Kodeksu | advanced | 1 | 0 |  |  |
| `kt-03` | Użycie Artefaktu | signature | 3 | 0 |  |  |
| `kt-04` | Rytuał Gwiazd | advanced | 2 | 0 |  |  |
| `kt-05` | Przepis na Płomień | basic | 1 | 0 |  |  |
| `kt-06` | Archiwum Ukryte | basic | 0 | 0 |  |  |
| `kt-07` | Transmutacja Winy | advanced | 0 | 2 |  |  |
| `kt-08` | Wskazówka (Cykl) | basic | 1 | 0 |  |  |
| `kt-09` | Zwierciadło Herezji | advanced | 0 | 0 |  |  |
| `kt-10` | Pieczęć Salomona | signature | 2 | 0 |  |  |

## Gildia Cieni

| ID | Nazwa | Tier | heresy | target_heresy | Ocena | Propozycja |
| :--- | :--- | :--- | ---: | ---: | :--- | :--- |
| `gc-01` | Fabrykowanie Dowodów | basic | 0 | 2 |  |  |
| `gc-02` | Podrzucenie Księgi | basic | 0 | 1 |  |  |
| `gc-03` | Szantaż | advanced | 0 | 0 |  |  |
| `gc-04` | Skrytobójstwo | signature | 2 | 0 |  |  |
| `gc-05` | Fałszywy Świadek | basic | 0 | 1 |  |  |
| `gc-06` | Przekupiony Strażnik | basic | 0 | 0 |  |  |
| `gc-07` | Czarny Rynek | basic | 1 | 0 |  |  |
| `gc-08` | Lista Dłużników | basic | 0 | 0 |  |  |
| `gc-09` | Zatrute Złoto | advanced | 1 | 2 |  |  |
| `gc-10` | Upadek Domu | signature | 2 | 0 |  |  |

## Po sesji

1. Wpisz oceny w tej tabeli.

2. Zaloguj zatwierdzone zmiany w [`balance-notes.md`](balance-notes.md) (Log zmian).

3. Zaktualizuj frontmatter karty i ustaw `status: playtest` gdy efekt uznany za OK.
