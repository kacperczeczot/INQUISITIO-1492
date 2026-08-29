# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.93 (Iteracja #1, Faza 3D)

**Wersja Poprzednia:** `v1.0-alpha.92` (4P: `93.8 pkt`) → **Nowa Wersja:** `v1.0-alpha.93` (4P: `94.0 pkt`)
**Data:** 2026-08-29 11:19 | **Czas Trwania Iteracji:** 390.9s | **Zysk 4P:** `+0.2 pkt` | **Zysk Global:** `+0.1 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (3D):** `L3_CAA-12_COST_PLUS1__L3_GC-05_C1_H0__L3_GC-07_GOLD_MINUS2` — **CAA-12 (Skrytka w Murach): cost 0 → 1 + GC-05 (Fałszywy Świadek): koszt 0→1, herezja 0→0 + GC-07 (Skrytobójstwo): gold 2 → 0**
- **Opis Modyfikacji:** Karta `gc-05` (Fałszywy Świadek): `cost` → `1` + Karta `gc-05` (Fałszywy Świadek): `heresy` → `0` + Karta `gc-07` (Skrytobójstwo): `gold` → `0` + Karta `caa-12` (Skrytka w Murach): `cost` → `1`
- **Wynik Kanonu 4P Balance:** 93.8 → 🟢 ** 94.0** (`⬆️ +0.2`) pkt (±0.80)
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 92.1 → 92.6 (`⬆️ +0.5`) pkt
  - `4p-no-cienie`: 86.7 → 86.9 (`⬆️ +0.2`) pkt
  - `4p-no-kabala`: 95.4 → 97.0 (`⬆️ +1.6`) pkt
  - `4p-no-korona`: 96.1 → 96.4 (`⬆️ +0.3`) pkt
  - `4p-no-oficjum`: 98.5 → 97.2 (`🔻 -1.3`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 33.1 → 33.1 (`= 0.0`) pkt
- **Tryb 4-osobowy (4p Avg):** 93.8 → 94.0 (`⬆️ +0.2`) pkt
- **Tryb 5-osobowy (5p Avg):** 25.7 → 25.8 (`⬆️ +0.1`) pkt
- **Global Game Balance Score:** 50.9 → 🔴 ** 51.0** (`⬆️ +0.1`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.77 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.9%` (norma: <30%)
  - **Autodafé / partię:** `1.53`
  - **Oskarżenia / partię:** `7.65`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | CI 95% | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| #1 | `L1_AUTODAFE_COOLDOWN_PLUS1__L3_GC-08_G0_H3__L3_SO-02_GOLD_MINUS1__L3_SO-05_HERESY_MINUS1` | Cooldown Autodafé: 3 → 4 Ery + GC-08 (Zatrute Złoto): złoto 1→0, herezja 2→3 + SO-02 (Skarbiec Trybunału): gold 2 → 1 + SO-05 (Wezwanie do Trybunału): heresy 1 → 0 | 93.8 → 🟢 ** 96.9** (`⬆️ +3.1`) | `[95.3, 98.5]` | 0.0% | 4.9% | 🟢 ZYSK |
| #2 | `L3_CAA-03_C1_G4__L3_CAA-12_G3_H0__L3_GC-08_HERESY_PLUS2__L4_TIME_DECK_EVERY_2ERAS` | CAA-03 (Cień na Rynku): koszt 0→1, złoto 2→4 + CAA-12 (Skrytka w Murach): złoto 4→3, herezja 0→0 + Edykty Czasu: co 1 Erę → co 2 Ery + GC-08 (Zatrute Złoto): heresy 2 → 4 | 93.8 → 🟢 ** 96.9** (`⬆️ +3.1`) | `[95.3, 98.5]` | 0.0% | 4.9% | 🟢 ZYSK |
| #3 | `L1_AUTODAFE_COOLDOWN_PLUS1__L1_START_GOLD_MINUS1__L3_GC-07_GOLD_MINUS2__L3_SO-05_HERESY_MINUS1` | Cooldown Autodafé: 3 → 4 Ery + GC-07 (Skrytobójstwo): gold 2 → 0 + SO-05 (Wezwanie do Trybunału): heresy 1 → 0 + Złoto startowe: 4zł → 3zł | 93.8 → 🟢 ** 96.9** (`⬆️ +3.1`) | `[95.3, 98.5]` | 0.0% | 4.9% | 🟢 ZYSK |
| #4 | `L3_CAA-02_C1_G4__L3_CAA-05_C0_H0__L3_GC-04_GOLD_SET3__L3_SO-05_TARGET_HERESY_PLUS2` | CAA-02 (Złoto z Kryjówki): koszt 0→1, złoto 3→4 + CAA-05 (Ukryty Kurier): koszt 1→0, herezja 0→0 + GC-04 (Informator): dodaj gold = 3 + SO-05 (Wezwanie do Trybunału): target_heresy 1 → 3 | 93.8 → 🟢 ** 96.8** (`⬆️ +3.0`) | `[95.2, 98.4]` | 0.0% | 4.9% | 🟢 ZYSK |
| #5 | `L3_CAA-12_G3_H0__L3_GC-07_GOLD_MINUS2__L4_SEA_ROUTE_ERA_PLUS1__L4_TIME_DECK_EVERY_2ERAS` | CAA-12 (Skrytka w Murach): złoto 4→3, herezja 0→0 + Edykty Czasu: co 1 Erę → co 2 Ery + GC-07 (Skrytobójstwo): gold 2 → 0 + Szlak Morski: Era 4 → 5 | 93.8 → 🟢 ** 96.8** (`⬆️ +3.0`) | `[95.2, 98.4]` | 0.0% | 4.9% | 🟢 ZYSK |
| #6 | `L1_AUTODAFE_COOLDOWN_PLUS1__L3_CAA-05_GOLD_PLUS1__L3_GC-08_G0_H3__L3_SO-05_HERESY_MINUS1` | CAA-05 (Ukryty Kurier): gold 3 → 4 + Cooldown Autodafé: 3 → 4 Ery + GC-08 (Zatrute Złoto): złoto 1→0, herezja 2→3 + SO-05 (Wezwanie do Trybunału): heresy 1 → 0 | 93.8 → 🟢 ** 96.8** (`⬆️ +3.0`) | `[95.2, 98.4]` | 0.0% | 4.9% | 🟢 ZYSK |
| #7 | `L3_CAA-01_G1_H3__L3_CAA-12_G3_H0__L4_SEA_ROUTE_ERA_PLUS1__L4_TIME_DECK_EVERY_2ERAS` | CAA-01 (Przejście Podziemiami): złoto 0→1, herezja 2→3 + CAA-12 (Skrytka w Murach): złoto 4→3, herezja 0→0 + Edykty Czasu: co 1 Erę → co 2 Ery + Szlak Morski: Era 4 → 5 | 93.8 → 🟢 ** 96.8** (`⬆️ +3.0`) | `[95.2, 98.4]` | 0.0% | 4.9% | 🟢 ZYSK |
| #8 | `L3_CAA-05_C0_G5__L3_CAA-12_G3_H0__L4_SEA_ROUTE_ERA_PLUS1__L4_TIME_DECK_EVERY_2ERAS` | CAA-05 (Ukryty Kurier): koszt 1→0, złoto 3→5 + CAA-12 (Skrytka w Murach): złoto 4→3, herezja 0→0 + Edykty Czasu: co 1 Erę → co 2 Ery + Szlak Morski: Era 4 → 5 | 93.8 → 🟢 ** 96.8** (`⬆️ +3.0`) | `[95.2, 98.4]` | 0.0% | 4.9% | 🟢 ZYSK |
| #9 | `L1_AUTODAFE_COOLDOWN_PLUS1__L1_MAX_ERAS_MINUS1__L3_GC-08_G0_H3__L3_SO-05_HERESY_MINUS1` | Cooldown Autodafé: 3 → 4 Ery + GC-08 (Zatrute Złoto): złoto 1→0, herezja 2→3 + Limit Er: 15 → 14 + SO-05 (Wezwanie do Trybunału): heresy 1 → 0 | 93.8 → 🟢 ** 96.7** (`⬆️ +2.9`) | `[95.1, 98.3]` | 0.0% | 4.9% | 🟢 ZYSK |
| #10 | `L3_CAA-05_GOLD_PLUS2__L3_GC-05_C1_H0__L3_GC-07_GOLD_MINUS2__L3_GC-09_C0_H0` | CAA-05 (Ukryty Kurier): gold 3 → 5 + GC-05 (Fałszywy Świadek): koszt 0→1, herezja 0→0 + GC-07 (Skrytobójstwo): gold 2 → 0 + GC-09 (Lista Dłużników): koszt 1→0, herezja 0→0 | 93.8 → 🟢 ** 96.7** (`⬆️ +2.9`) | `[95.1, 98.3]` | 0.0% | 4.9% | 🟢 ZYSK |
| #11 | `L1_AUTODAFE_COOLDOWN_PLUS1__L3_GC-03_C2_G1__L3_SO-05_HERESY_MINUS1__L3_SO-07_G3_H0` | Cooldown Autodafé: 3 → 4 Ery + GC-03 (Podrzucenie Księgi): koszt 1→2, złoto 0→1 + SO-05 (Wezwanie do Trybunału): heresy 1 → 0 + SO-07 (Przesłuchanie Oficjum): złoto 2→3, herezja 0→0 | 93.8 → 🟢 ** 96.7** (`⬆️ +2.9`) | `[95.1, 98.3]` | 0.0% | 4.8% | 🟢 ZYSK |
| #12 | `L3_CAA-03_C1_G4__L3_CAA-12_G3_H0__L3_SO-02_G1_H3__L4_TIME_DECK_EVERY_2ERAS` | CAA-03 (Cień na Rynku): koszt 0→1, złoto 2→4 + CAA-12 (Skrytka w Murach): złoto 4→3, herezja 0→0 + Edykty Czasu: co 1 Erę → co 2 Ery + SO-02 (Skarbiec Trybunału): złoto 2→1, herezja 2→3 | 93.8 → 🟢 ** 96.6** (`⬆️ +2.8`) | `[95.0, 98.2]` | 0.0% | 4.9% | 🟢 ZYSK |
| #13 | `L3_CAA-03_C1_G4__L3_CAA-12_G3_H0__L3_GC-04_GOLD_PLUS1__L4_TIME_DECK_EVERY_2ERAS` | CAA-03 (Cień na Rynku): koszt 0→1, złoto 2→4 + CAA-12 (Skrytka w Murach): złoto 4→3, herezja 0→0 + Edykty Czasu: co 1 Erę → co 2 Ery + GC-04 (Informator): gold 0 → 1 | 93.8 → 🟢 ** 96.6** (`⬆️ +2.8`) | `[94.9, 98.3]` | 0.0% | 4.9% | 🟢 ZYSK |
| #14 | `L3_CAA-03_C1_G4__L3_CAA-12_G3_H0__L3_GC-05_C1_G2__L4_TIME_DECK_EVERY_2ERAS` | CAA-03 (Cień na Rynku): koszt 0→1, złoto 2→4 + CAA-12 (Skrytka w Murach): złoto 4→3, herezja 0→0 + Edykty Czasu: co 1 Erę → co 2 Ery + GC-05 (Fałszywy Świadek): koszt 0→1, złoto 0→2 | 93.8 → 🟢 ** 96.6** (`⬆️ +2.8`) | `[95.0, 98.2]` | 0.0% | 4.9% | 🟢 ZYSK |
| #15 | `L3_CAA-12_G3_H0__L3_SO-08_C1_G4__L4_SEA_ROUTE_ERA_PLUS1__L4_TIME_DECK_EVERY_2ERAS` | CAA-12 (Skrytka w Murach): złoto 4→3, herezja 0→0 + Edykty Czasu: co 1 Erę → co 2 Ery + SO-08 (Nasłanie Inkwizytora): koszt 0→1, złoto 3→4 + Szlak Morski: Era 4 → 5 | 93.8 → 🟢 ** 96.6** (`⬆️ +2.8`) | `[95.0, 98.2]` | 0.0% | 5.1% | 🟢 ZYSK |
| #16 | `L3_CAA-11_C2_G2__L3_GC-09_C0_H0__L3_SO-05_G0_H0__L4_TIME_DECK_EVERY_2ERAS` | CAA-11 (Nocna Zmiana Warty): koszt 1→2, złoto 1→2 + Edykty Czasu: co 1 Erę → co 2 Ery + GC-09 (Lista Dłużników): koszt 1→0, herezja 0→0 + SO-05 (Wezwanie do Trybunału): złoto 0→0, herezja 1→0 | 93.8 → 🟢 ** 96.6** (`⬆️ +2.8`) | `[95.0, 98.2]` | 0.0% | 4.9% | 🟢 ZYSK |
| #17 | `L3_CAA-12_G3_H0__L3_GC-05_HERESY_PLUS1__L4_SEA_ROUTE_ERA_PLUS1__L4_TIME_DECK_EVERY_2ERAS` | CAA-12 (Skrytka w Murach): złoto 4→3, herezja 0→0 + Edykty Czasu: co 1 Erę → co 2 Ery + GC-05 (Fałszywy Świadek): heresy 0 → 1 + Szlak Morski: Era 4 → 5 | 93.8 → 🟢 ** 96.5** (`⬆️ +2.7`) | `[94.8, 98.2]` | 0.0% | 4.9% | 🟢 ZYSK |
| #18 | `L3_CAA-03_C1_G4__L3_CAA-12_G3_H0__L3_GC-04_C0_G2__L4_TIME_DECK_EVERY_2ERAS` | CAA-03 (Cień na Rynku): koszt 0→1, złoto 2→4 + CAA-12 (Skrytka w Murach): złoto 4→3, herezja 0→0 + Edykty Czasu: co 1 Erę → co 2 Ery + GC-04 (Informator): koszt 1→0, złoto 0→2 | 93.8 → 🟢 ** 96.5** (`⬆️ +2.7`) | `[94.8, 98.2]` | 0.0% | 4.9% | 🟢 ZYSK |
| #19 | `L1_START_GOLD_PLUS1__L3_CAA-12_COST_PLUS1__L3_GC-05_C1_H0__L3_GC-07_GOLD_MINUS2` | CAA-12 (Skrytka w Murach): cost 0 → 1 + GC-05 (Fałszywy Świadek): koszt 0→1, herezja 0→0 + GC-07 (Skrytobójstwo): gold 2 → 0 + Złoto startowe: 4zł → 5zł | 93.8 → 🟢 ** 96.5** (`⬆️ +2.7`) | `[94.8, 98.2]` | 0.0% | 4.9% | 🟢 ZYSK |
| #20 | `L1_AUTODAFE_COOLDOWN_PLUS1__L3_CAA-10_GOLD_PLUS2__L3_GC-03_C2_G1__L3_SO-05_HERESY_MINUS1` | CAA-10 (Echo Alhambry): gold 0 → 2 + Cooldown Autodafé: 3 → 4 Ery + GC-03 (Podrzucenie Księgi): koszt 1→2, złoto 0→1 + SO-05 (Wezwanie do Trybunału): heresy 1 → 0 | 93.8 → 🟢 ** 96.5** (`⬆️ +2.7`) | `[94.9, 98.1]` | 0.0% | 4.9% | 🟢 ZYSK |
| #21 | `L3_CAA-11_C2_G2__L3_KT-01_HERESY_PLUS1__L3_SO-05_G0_H0__L4_TIME_DECK_EVERY_2ERAS` | CAA-11 (Nocna Zmiana Warty): koszt 1→2, złoto 1→2 + Edykty Czasu: co 1 Erę → co 2 Ery + KT-01 (Rytuał Przejścia): heresy 1 → 2 + SO-05 (Wezwanie do Trybunału): złoto 0→0, herezja 1→0 | 93.8 → 🟢 ** 96.4** (`⬆️ +2.6`) | `[94.7, 98.1]` | 0.0% | 4.9% | 🟢 ZYSK |
| #22 | `L1_THRESHOLD_PLUS1__L3_CAA-01_HERESY_PLUS1__L3_CAA-05_C0_H0__L3_GC-08_GOLD_MINUS1` | CAA-01 (Przejście Podziemiami): heresy 2 → 3 + CAA-05 (Ukryty Kurier): koszt 1→0, herezja 0→0 + GC-08 (Zatrute Złoto): gold 1 → 0 + Próg Oskarżenia: 7 → 8 | 93.8 → 🟢 ** 96.4** (`⬆️ +2.6`) | `[94.7, 98.1]` | 0.0% | 4.9% | 🟢 ZYSK |
| #23 | `L3_CAA-11_C2_G2__L3_SO-05_G0_H0__L4_TIME_DECK_EVERY_2ERAS__L4_TIME_DECK_EVERY_3ERAS` | CAA-11 (Nocna Zmiana Warty): koszt 1→2, złoto 1→2 + Edykty Czasu: co 1 Erę → co 2 Ery + Edykty Czasu: co 1 Erę → co 3 Ery + SO-05 (Wezwanie do Trybunału): złoto 0→0, herezja 1→0 | 93.8 → 🟢 ** 96.4** (`⬆️ +2.6`) | `[94.7, 98.1]` | 0.0% | 4.9% | 🟢 ZYSK |
| #24 | `L1_AUTODAFE_COOLDOWN_PLUS1__L3_GC-08_G0_H3__L3_SO-05_HERESY_MINUS1__L4_SEA_ROUTE_ERA_PLUS2` | Cooldown Autodafé: 3 → 4 Ery + GC-08 (Zatrute Złoto): złoto 1→0, herezja 2→3 + SO-05 (Wezwanie do Trybunału): heresy 1 → 0 + Szlak Morski: Era 4 → 6 | 93.8 → 🟢 ** 96.4** (`⬆️ +2.6`) | `[94.8, 98.0]` | 0.0% | 4.9% | 🟢 ZYSK |
| #25 | `L3_CAA-12_G3_H0__L3_SO-05_G0_H2__L4_SEA_ROUTE_ERA_PLUS1__L4_TIME_DECK_EVERY_2ERAS` | CAA-12 (Skrytka w Murach): złoto 4→3, herezja 0→0 + Edykty Czasu: co 1 Erę → co 2 Ery + SO-05 (Wezwanie do Trybunału): złoto 0→0, herezja 1→2 + Szlak Morski: Era 4 → 5 | 93.8 → 🟢 ** 96.4** (`⬆️ +2.6`) | `[94.7, 98.1]` | 0.0% | 4.9% | 🟢 ZYSK |
| #26 | `L3_CAA-12_COST_PLUS1__L3_CAA-12_G5_H0__L3_GC-05_C1_H0__L3_GC-07_GOLD_MINUS2` | CAA-12 (Skrytka w Murach): cost 0 → 1 + CAA-12 (Skrytka w Murach): złoto 4→5, herezja 0→0 + GC-05 (Fałszywy Świadek): koszt 0→1, herezja 0→0 + GC-07 (Skrytobójstwo): gold 2 → 0 | 93.8 → 🟢 ** 96.4** (`⬆️ +2.6`) | `[94.7, 98.1]` | 0.0% | 4.9% | 🟢 ZYSK |
| #27 | `L3_CAA-12_G3_H0__L3_GC-05_GOLD_SET3__L4_SEA_ROUTE_ERA_PLUS1__L4_TIME_DECK_EVERY_2ERAS` | CAA-12 (Skrytka w Murach): złoto 4→3, herezja 0→0 + Edykty Czasu: co 1 Erę → co 2 Ery + GC-05 (Fałszywy Świadek): dodaj gold = 3 + Szlak Morski: Era 4 → 5 | 93.8 → 🟢 ** 96.4** (`⬆️ +2.6`) | `[94.7, 98.1]` | 0.0% | 4.9% | 🟢 ZYSK |
| #28 | `L1_AGENTS_PLUS1__L3_CAA-12_G3_H0__L4_SEA_ROUTE_ERA_PLUS1__L4_TIME_DECK_EVERY_2ERAS` | Agenci: 3 → 4 + CAA-12 (Skrytka w Murach): złoto 4→3, herezja 0→0 + Edykty Czasu: co 1 Erę → co 2 Ery + Szlak Morski: Era 4 → 5 | 93.8 → 🟢 ** 96.4** (`⬆️ +2.6`) | `[94.7, 98.1]` | 0.0% | 4.9% | 🟢 ZYSK |
| #29 | `L3_CAA-01_HERESY_MINUS1__L3_GC-05_C1_H0__L3_GC-07_GOLD_MINUS2__L3_GC-09_C0_H0` | CAA-01 (Przejście Podziemiami): heresy 2 → 1 + GC-05 (Fałszywy Świadek): koszt 0→1, herezja 0→0 + GC-07 (Skrytobójstwo): gold 2 → 0 + GC-09 (Lista Dłużników): koszt 1→0, herezja 0→0 | 93.8 → 🟢 ** 96.4** (`⬆️ +2.6`) | `[94.8, 98.0]` | 0.0% | 4.9% | 🟢 ZYSK |
| #30 | `L3_CAA-12_COST_PLUS1__L3_GC-04_C2_G2__L3_GC-05_C1_H0__L3_GC-07_GOLD_MINUS2` | CAA-12 (Skrytka w Murach): cost 0 → 1 + GC-04 (Informator): koszt 1→2, złoto 0→2 + GC-05 (Fałszywy Świadek): koszt 0→1, herezja 0→0 + GC-07 (Skrytobójstwo): gold 2 → 0 | 93.8 → 🟢 ** 96.3** (`⬆️ +2.5`) | `[94.6, 98.0]` | 0.0% | 4.9% | 🟢 ZYSK |