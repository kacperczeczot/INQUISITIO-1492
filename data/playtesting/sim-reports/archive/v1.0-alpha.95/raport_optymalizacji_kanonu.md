# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.95 (Iteracja #2, Faza 2D)

**Wersja Poprzednia:** `v1.0-alpha.94` (4P: `94.1 pkt`) → **Nowa Wersja:** `v1.0-alpha.95` (4P: `94.2 pkt`)
**Data:** 2026-08-29 16:09 | **Czas Trwania Iteracji:** 444.5s | **Zysk 4P:** `+0.1 pkt` | **Zysk Global:** `0.0 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (2D):** `L3_GC-07_GOLD_SET2__L3_SO-05_TARGET_HERESY_PLUS2` — **GC-07 (Skrytobójstwo): dodaj gold = 2 + SO-05 (Wezwanie do Trybunału): target_heresy 1 → 3**
- **Opis Modyfikacji:** Karta `so-05` (Wezwanie do Trybunału): `target_heresy` → `3` + Karta `gc-07` (Skrytobójstwo): `gold` → `2`
- **Wynik Kanonu 4P Balance:** 94.1 → 🟢 ** 94.2** (`⬆️ +0.1`) pkt (±0.80)
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 92.6 → 92.6 (`= 0.0`) pkt
  - `4p-no-cienie`: 86.9 → 86.7 (`🔻 -0.2`) pkt
  - `4p-no-kabala`: 97.2 → 96.5 (`🔻 -0.7`) pkt
  - `4p-no-korona`: 96.5 → 97.7 (`⬆️ +1.2`) pkt
  - `4p-no-oficjum`: 97.1 → 97.4 (`⬆️ +0.3`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 33.1 → 33.1 (`= 0.0`) pkt
- **Tryb 4-osobowy (4p Avg):** 94.1 → 94.2 (`⬆️ +0.1`) pkt
- **Tryb 5-osobowy (5p Avg):** 25.8 → 25.8 (`= 0.0`) pkt
- **Global Game Balance Score:** 51.0 → 🔴 ** 51.0** (`= 0.0`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.77 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.9%` (norma: <30%)
  - **Autodafé / partię:** `1.53`
  - **Oskarżenia / partię:** `7.64`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | CI 95% | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| #1 | `L1_START_GOLD_PLUS1__L3_CAA-09_C1_G1__L3_GC-08_G0_H1` | CAA-09 (Kurier Relikwii): koszt 0→1, złoto 0→1 + GC-08 (Zatrute Złoto): złoto 1→0, herezja 2→1 + Złoto startowe: 4zł → 5zł | 94.1 → 🟢 ** 97.1** (`⬆️ +3.0`) | `[95.5, 98.7]` | 0.0% | 4.9% | 🟢 ZYSK |
| #2 | `L3_CAA-09_C1_G1__L3_GC-05_GOLD_SET2__L3_GC-08_G0_H1` | CAA-09 (Kurier Relikwii): koszt 0→1, złoto 0→1 + GC-05 (Fałszywy Świadek): dodaj gold = 2 + GC-08 (Zatrute Złoto): złoto 1→0, herezja 2→1 | 94.1 → 🟢 ** 97.1** (`⬆️ +3.0`) | `[95.5, 98.7]` | 0.0% | 4.9% | 🟢 ZYSK |
| #3 | `L3_CAA-01_G0_H1__L3_CAA-03_C1_G3__L3_SO-05_GOLD_MINUS2` | CAA-01 (Przejście Podziemiami): złoto 0→0, herezja 2→1 + CAA-03 (Cień na Rynku): koszt 0→1, złoto 2→3 + SO-05 (Wezwanie do Trybunału): gold 2 → 0 | 94.1 → 🟢 ** 97.1** (`⬆️ +3.0`) | `[95.6, 98.6]` | 0.0% | 4.9% | 🟢 ZYSK |
| #4 | `L3_CAA-01_HERESY_PLUS1__L3_GC-05_C0_H0__L3_GC-08_G0_H1` | CAA-01 (Przejście Podziemiami): heresy 2 → 3 + GC-05 (Fałszywy Świadek): koszt 1→0, herezja 0→0 + GC-08 (Zatrute Złoto): złoto 1→0, herezja 2→1 | 94.1 → 🟢 ** 97.0** (`⬆️ +2.9`) | `[95.5, 98.5]` | 0.0% | 4.9% | 🟢 ZYSK |
| #5 | `L3_GC-05_C0_H0__L3_GC-05_TARGET_HERESY_SET1__L3_GC-08_G0_H1` | GC-05 (Fałszywy Świadek): dodaj target_heresy = 1 + GC-05 (Fałszywy Świadek): koszt 1→0, herezja 0→0 + GC-08 (Zatrute Złoto): złoto 1→0, herezja 2→1 | 94.1 → 🟢 ** 97.0** (`⬆️ +2.9`) | `[95.4, 98.6]` | 0.0% | 4.9% | 🟢 ZYSK |
| #6 | `L3_CAA-08_GOLD_MINUS1__L3_GC-07_GOLD_SET2__L3_SO-05_TARGET_HERESY_PLUS2` | CAA-08 (Kaptur Nocy): gold 3 → 2 + GC-07 (Skrytobójstwo): dodaj gold = 2 + SO-05 (Wezwanie do Trybunału): target_heresy 1 → 3 | 94.1 → 🟢 ** 96.9** (`⬆️ +2.8`) | `[95.3, 98.5]` | 0.0% | 5.0% | 🟢 ZYSK |
| #7 | `L3_GC-05_HERESY_SET2__L3_GC-07_GOLD_SET2__L3_SO-05_TARGET_HERESY_PLUS2` | GC-05 (Fałszywy Świadek): dodaj heresy = 2 + GC-07 (Skrytobójstwo): dodaj gold = 2 + SO-05 (Wezwanie do Trybunału): target_heresy 1 → 3 | 94.1 → 🟢 ** 96.9** (`⬆️ +2.8`) | `[95.3, 98.5]` | 0.0% | 4.9% | 🟢 ZYSK |
| #8 | `L3_CAA-03_C1_G3__L3_GC-05_HERESY_PLUS1__L3_SO-05_G3_H4` | CAA-03 (Cień na Rynku): koszt 0→1, złoto 2→3 + GC-05 (Fałszywy Świadek): heresy 0 → 1 + SO-05 (Wezwanie do Trybunału): złoto 2→3, herezja 3→4 | 94.1 → 🟢 ** 96.9** (`⬆️ +2.8`) | `[95.3, 98.5]` | 0.0% | 4.9% | 🟢 ZYSK |
| #9 | `L3_CAA-03_C1_G3__L3_GC-05_HERESY_SET2__L3_SO-05_GOLD_MINUS1` | CAA-03 (Cień na Rynku): koszt 0→1, złoto 2→3 + GC-05 (Fałszywy Świadek): dodaj heresy = 2 + SO-05 (Wezwanie do Trybunału): gold 2 → 1 | 94.1 → 🟢 ** 96.8** (`⬆️ +2.7`) | `[95.2, 98.4]` | 0.0% | 4.9% | 🟢 ZYSK |
| #10 | `L3_GC-08_GOLD_MINUS1__L3_SO-05_GOLD_MINUS1__L4_SEA_ROUTE_ERA_MINUS1` | GC-08 (Zatrute Złoto): gold 1 → 0 + SO-05 (Wezwanie do Trybunału): gold 2 → 1 + Szlak Morski: Era 4 → 3 | 94.1 → 🟢 ** 96.8** (`⬆️ +2.7`) | `[95.2, 98.4]` | 0.0% | 4.9% | 🟢 ZYSK |
| #11 | `L3_CAA-01_G0_H1__L3_CAA-03_C1_G3__L3_GC-05_C0_G1` | CAA-01 (Przejście Podziemiami): złoto 0→0, herezja 2→1 + CAA-03 (Cień na Rynku): koszt 0→1, złoto 2→3 + GC-05 (Fałszywy Świadek): koszt 1→0, złoto 0→1 | 94.1 → 🟢 ** 96.8** (`⬆️ +2.7`) | `[95.2, 98.4]` | 0.0% | 4.9% | 🟢 ZYSK |
| #12 | `L3_CAA-01_C3_H1__L3_GC-05_C0_H1__L3_KB-12_HERESY_MINUS2` | CAA-01 (Przejście Podziemiami): koszt 2→3, herezja 2→1 + GC-05 (Fałszywy Świadek): koszt 1→0, herezja 0→1 + KB-12 (Szantaż Salonowy): heresy 2 → 0 | 94.1 → 🟢 ** 96.8** (`⬆️ +2.7`) | `[95.2, 98.4]` | 0.0% | 4.9% | 🟢 ZYSK |
| #13 | `L3_CAA-03_C0_G3__L3_GC-03_C2_G1__L3_SO-05_G1_H4` | CAA-03 (Cień na Rynku): koszt 0→0, złoto 2→3 + GC-03 (Podrzucenie Księgi): koszt 1→2, złoto 0→1 + SO-05 (Wezwanie do Trybunału): złoto 2→1, herezja 3→4 | 94.1 → 🟢 ** 96.8** (`⬆️ +2.7`) | `[95.2, 98.4]` | 0.0% | 4.9% | 🟢 ZYSK |
| #14 | `L3_GC-05_C0_H0__L3_GC-08_G0_H1__L3_GC-09_GOLD_SET3` | GC-05 (Fałszywy Świadek): koszt 1→0, herezja 0→0 + GC-08 (Zatrute Złoto): złoto 1→0, herezja 2→1 + GC-09 (Lista Dłużników): dodaj gold = 3 | 94.1 → 🟢 ** 96.8** (`⬆️ +2.7`) | `[95.2, 98.4]` | 0.0% | 4.9% | 🟢 ZYSK |
| #15 | `L3_CAA-09_C1_G1__L3_GC-08_G0_H1__L3_SO-05_HERESY_MINUS1` | CAA-09 (Kurier Relikwii): koszt 0→1, złoto 0→1 + GC-08 (Zatrute Złoto): złoto 1→0, herezja 2→1 + SO-05 (Wezwanie do Trybunału): heresy 3 → 2 | 94.1 → 🟢 ** 96.7** (`⬆️ +2.6`) | `[95.1, 98.3]` | 0.0% | 4.9% | 🟢 ZYSK |
| #16 | `L3_GC-07_GOLD_SET2__L3_GC-09_GOLD_PLUS1__L3_SO-05_TARGET_HERESY_PLUS2` | GC-07 (Skrytobójstwo): dodaj gold = 2 + GC-09 (Lista Dłużników): gold 0 → 1 + SO-05 (Wezwanie do Trybunału): target_heresy 1 → 3 | 94.1 → 🟢 ** 96.7** (`⬆️ +2.6`) | `[95.1, 98.3]` | 0.0% | 4.9% | 🟢 ZYSK |
| #17 | `L3_CAA-01_C1_H3__L3_GC-05_C0_H1__L3_KB-08_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): koszt 2→1, herezja 2→3 + GC-05 (Fałszywy Świadek): koszt 1→0, herezja 0→1 + KB-08 (Przekupstwo Sędziego): heresy 2 → 3 | 94.1 → 🟢 ** 96.7** (`⬆️ +2.6`) | `[95.1, 98.3]` | 0.0% | 4.9% | 🟢 ZYSK |
| #18 | `L3_CAA-03_C1_G3__L3_GC-05_HERESY_PLUS1__L3_KT-01_GOLD_MINUS1` | CAA-03 (Cień na Rynku): koszt 0→1, złoto 2→3 + GC-05 (Fałszywy Świadek): heresy 0 → 1 + KT-01 (Rytuał Przejścia): gold 1 → 0 | 94.1 → 🟢 ** 96.7** (`⬆️ +2.6`) | `[95.1, 98.3]` | 0.0% | 4.9% | 🟢 ZYSK |
| #19 | `L3_CAA-01_TARGET_HERESY_MINUS1__L3_GC-05_HERESY_PLUS1__L3_GC-09_GOLD_PLUS2` | CAA-01 (Przejście Podziemiami): target_heresy 1 → 0 + GC-05 (Fałszywy Świadek): heresy 0 → 1 + GC-09 (Lista Dłużników): gold 0 → 2 | 94.1 → 🟢 ** 96.7** (`⬆️ +2.6`) | `[95.1, 98.3]` | 0.0% | 4.9% | 🟢 ZYSK |
| #20 | `L3_GC-07_GOLD_SET2__L3_SO-05_GOLD_MINUS1__L4_SEA_ROUTE_ERA_MINUS1` | GC-07 (Skrytobójstwo): dodaj gold = 2 + SO-05 (Wezwanie do Trybunału): gold 2 → 1 + Szlak Morski: Era 4 → 3 | 94.1 → 🟢 ** 96.6** (`⬆️ +2.5`) | `[95.0, 98.2]` | 0.0% | 4.9% | 🟢 ZYSK |
| #21 | `L3_GC-08_HERESY_PLUS2__L3_SO-05_GOLD_MINUS1__L4_SEA_ROUTE_ERA_MINUS1` | GC-08 (Zatrute Złoto): heresy 2 → 4 + SO-05 (Wezwanie do Trybunału): gold 2 → 1 + Szlak Morski: Era 4 → 3 | 94.1 → 🟢 ** 96.6** (`⬆️ +2.5`) | `[95.0, 98.2]` | 0.0% | 4.9% | 🟢 ZYSK |
| #22 | `L3_CAA-01_C3_H3__L3_CAA-09_C1_G1__L3_GC-08_G0_H1` | CAA-01 (Przejście Podziemiami): koszt 2→3, herezja 2→3 + CAA-09 (Kurier Relikwii): koszt 0→1, złoto 0→1 + GC-08 (Zatrute Złoto): złoto 1→0, herezja 2→1 | 94.1 → 🟢 ** 96.6** (`⬆️ +2.5`) | `[95.0, 98.2]` | 0.0% | 4.9% | 🟢 ZYSK |
| #23 | `L1_THRESHOLD_MINUS1__L3_GC-05_C0_H1__L3_KB-12_HERESY_MINUS2` | GC-05 (Fałszywy Świadek): koszt 1→0, herezja 0→1 + KB-12 (Szantaż Salonowy): heresy 2 → 0 + Próg Oskarżenia: 7 → 6 | 94.1 → 🟢 ** 96.6** (`⬆️ +2.5`) | `[95.0, 98.2]` | 0.0% | 4.9% | 🟢 ZYSK |
| #24 | `L3_GC-04_GOLD_SET2__L3_GC-05_TARGET_HERESY_PLUS1__L3_SO-05_GOLD_MINUS1` | GC-04 (Informator): dodaj gold = 2 + GC-05 (Fałszywy Świadek): target_heresy 0 → 1 + SO-05 (Wezwanie do Trybunału): gold 2 → 1 | 94.1 → 🟢 ** 96.6** (`⬆️ +2.5`) | `[95.0, 98.2]` | 0.0% | 4.9% | 🟢 ZYSK |
| #25 | `L3_CAA-03_C1_G3__L3_GC-05_HERESY_SET2__L3_GC-10_GOLD_PLUS2` | CAA-03 (Cień na Rynku): koszt 0→1, złoto 2→3 + GC-05 (Fałszywy Świadek): dodaj heresy = 2 + GC-10 (Upadek Domu): gold 0 → 2 | 94.1 → 🟢 ** 96.6** (`⬆️ +2.5`) | `[95.0, 98.2]` | 0.0% | 4.9% | 🟢 ZYSK |
| #26 | `L3_GC-05_C0_H0__L3_GC-07_GOLD_SET3__L3_GC-08_G0_H1` | GC-05 (Fałszywy Świadek): koszt 1→0, herezja 0→0 + GC-07 (Skrytobójstwo): dodaj gold = 3 + GC-08 (Zatrute Złoto): złoto 1→0, herezja 2→1 | 94.1 → 🟢 ** 96.6** (`⬆️ +2.5`) | `[95.0, 98.2]` | 0.0% | 4.9% | 🟢 ZYSK |
| #27 | `L1_THRESHOLD_MINUS1__L3_CAA-03_GOLD_PLUS1__L3_KB-05_G0_H0` | CAA-03 (Cień na Rynku): gold 2 → 3 + KB-05 (List Żelazny): złoto 0→0, herezja 1→0 + Próg Oskarżenia: 7 → 6 | 94.1 → 🟢 ** 96.6** (`⬆️ +2.5`) | `[95.0, 98.2]` | 0.0% | 4.9% | 🟢 ZYSK |
| #28 | `L3_CAA-03_C0_G3__L3_CAA-09_C1_G1__L3_GC-03_C2_G1` | CAA-03 (Cień na Rynku): koszt 0→0, złoto 2→3 + CAA-09 (Kurier Relikwii): koszt 0→1, złoto 0→1 + GC-03 (Podrzucenie Księgi): koszt 1→2, złoto 0→1 | 94.1 → 🟢 ** 96.6** (`⬆️ +2.5`) | `[95.0, 98.2]` | 0.0% | 4.9% | 🟢 ZYSK |
| #29 | `L3_CAA-03_C0_G3__L3_GC-03_C2_G1__L3_SO-05_C0_H2` | CAA-03 (Cień na Rynku): koszt 0→0, złoto 2→3 + GC-03 (Podrzucenie Księgi): koszt 1→2, złoto 0→1 + SO-05 (Wezwanie do Trybunału): koszt 0→0, herezja 3→2 | 94.1 → 🟢 ** 96.6** (`⬆️ +2.5`) | `[95.0, 98.2]` | 0.0% | 4.9% | 🟢 ZYSK |
| #30 | `L3_CAA-03_C1_G3__L3_GC-05_HERESY_PLUS1__L3_GC-12_C1_G2` | CAA-03 (Cień na Rynku): koszt 0→1, złoto 2→3 + GC-05 (Fałszywy Świadek): heresy 0 → 1 + GC-12 (Złodziejski Zwiad): koszt 0→1, złoto 1→2 | 94.1 → 🟢 ** 96.6** (`⬆️ +2.5`) | `[95.0, 98.2]` | 0.0% | 5.0% | 🟢 ZYSK |