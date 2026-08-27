# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.68 (Iteracja #2, Faza 2D)

**Wersja Poprzednia:** `v1.0-alpha.67` (4P: `72.3 pkt`) → **Nowa Wersja:** `v1.0-alpha.68` (4P: `74.4 pkt`)
**Data:** 2026-08-24 07:44 | **Czas Trwania Iteracji:** 613.0s | **Zysk 4P:** `+2.1 pkt` | **Zysk Global:** `+9.1 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (2D):** `L3_SO-08_GOLD_SET3__L3_CAA-08_TARGET_HERESY_MINUS1` — **SO-08 (Nasłanie Inkwizytora): dodaj gold = 3 + CAA-08 (Kaptur Nocy): target_heresy 2 → 1**
- **Opis Modyfikacji:** Karta `so-08` (Nasłanie Inkwizytora): `gold` → `3` + Karta `caa-08` (Kaptur Nocy): `target_heresy` → `1`
- **Wynik Kanonu 4P Balance:** 72.3 → 🟠 ** 74.4** (`⬆️ +2.1`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 75.7 → 83.0 (`⬆️ +7.3`) pkt
  - `4p-no-cienie`: 63.6 → 69.1 (`⬆️ +5.5`) pkt
  - `4p-no-kabala`: 68.5 → 66.2 (`-2.3`) pkt
  - `4p-no-korona`: 96.2 → 90.9 (`-5.3`) pkt
  - `4p-no-oficjum`: 57.5 → 62.8 (`⬆️ +5.3`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 31.9 pkt
- **Tryb 4-osobowy (4p Avg):** 61.3 → 65.9 (`⬆️ +4.6`) pkt
- **Tryb 5-osobowy (5p Avg):** 3.2 → 25.7 (`⬆️ +22.5`) pkt
- **Global Game Balance Score:** 32.1 → 🔴 ** 41.2** (`⬆️ +9.1`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.80 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.4%` (norma: <30%)
  - **Autodafé / partię:** `1.54`
  - **Oskarżenia / partię:** `6.75`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-08_GOLD_SET3__L3_CAA-08_TARGET_HERESY_MINUS1` | SO-08 (Nasłanie Inkwizytora): dodaj gold = 3 + CAA-08 (Kaptur Nocy): target_heresy 2 → 1 | 72.3 → 🟠 ** 74.4** (`⬆️ +2.1`) | 0.0% | 4.4% | 🌟 ZWYCIĘZCA |
| #2 | `L3_CAA-04_TARGET_HERESY_PLUS1__L3_GC-07_HERESY_SET2` | CAA-04 (Fałszywy Trop): target_heresy 1 → 2 + GC-07 (Skrytobójstwo): dodaj heresy = 2 | 72.3 → 🟠 ** 74.1** (`⬆️ +1.8`) | 0.0% | 5.0% | 🟢 ZYSK |
| #3 | `L3_CAA-04_TARGET_HERESY_PLUS1__L3_GC-08_HERESY_PLUS1` | CAA-04 (Fałszywy Trop): target_heresy 1 → 2 + GC-08 (Zatrute Złoto): heresy 2 → 3 | 72.3 → 🟠 ** 73.0** (`⬆️ +0.7`) | 0.0% | 5.1% | 🟢 ZYSK |
| #4 | `L3_SO-08_GOLD_SET3__L1_OBSERVED_MINUS1` | SO-08 (Nasłanie Inkwizytora): dodaj gold = 3 + Próg Obserwowanej: 5 → 4 | 72.3 → 🟠 ** 73.0** (`⬆️ +0.7`) | 0.0% | 4.4% | 🟢 ZYSK |
| #5 | `L3_KB-07_HERESY_SET2__L3_CAA-09_COST_PLUS1` | KB-07 (Szantaż Pieczęcią): dodaj heresy = 2 + CAA-09 (Kurier Relikwii): cost 0 → 1 | 72.3 → 🟠 ** 72.7** (`⬆️ +0.4`) | 0.0% | 5.1% | 🟢 ZYSK |
| #6 | `L3_SO-08_GOLD_SET3__L3_CAA-03_GOLD_MINUS1` | SO-08 (Nasłanie Inkwizytora): dodaj gold = 3 + CAA-03 (Cień na Rynku): gold 2 → 1 | 72.3 → 🟠 ** 72.1** (`-0.2`) | 0.0% | 4.4% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_CAA-04_GOLD_MINUS1__L3_GC-08_HERESY_PLUS1` | CAA-04 (Fałszywy Trop): gold 3 → 2 + GC-08 (Zatrute Złoto): heresy 2 → 3 | 72.3 → 🟠 ** 71.9** (`-0.4`) | 0.0% | 5.1% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_CAA-04_COST_PLUS1__L3_GC-08_HERESY_PLUS1` | CAA-04 (Fałszywy Trop): cost 0 → 1 + GC-08 (Zatrute Złoto): heresy 2 → 3 | 72.3 → 🟠 ** 71.9** (`-0.4`) | 0.0% | 5.1% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_CAA-04_COST_PLUS1__L3_GC-03_HERESY_SET2` | CAA-04 (Fałszywy Trop): cost 0 → 1 + GC-03 (Podrzucenie Księgi): dodaj heresy = 2 | 72.3 → 🟠 ** 71.8** (`-0.5`) | 0.0% | 5.1% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_CAA-04_GOLD_MINUS1__L3_GC-03_HERESY_SET2` | CAA-04 (Fałszywy Trop): gold 3 → 2 + GC-03 (Podrzucenie Księgi): dodaj heresy = 2 | 72.3 → 🟠 ** 71.8** (`-0.5`) | 0.0% | 5.1% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_CAA-04_GOLD_MINUS1__L3_GC-07_HERESY_SET2` | CAA-04 (Fałszywy Trop): gold 3 → 2 + GC-07 (Skrytobójstwo): dodaj heresy = 2 | 72.3 → 🟠 ** 71.7** (`-0.6`) | 0.0% | 5.0% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-04_COST_PLUS1__L3_GC-07_HERESY_SET2` | CAA-04 (Fałszywy Trop): cost 0 → 1 + GC-07 (Skrytobójstwo): dodaj heresy = 2 | 72.3 → 🟠 ** 71.7** (`-0.6`) | 0.0% | 5.0% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_CAA-04_COST_PLUS1__L3_GC-05_HERESY_SET1` | CAA-04 (Fałszywy Trop): cost 0 → 1 + GC-05 (Fałszywy Świadek): dodaj heresy = 1 | 72.3 → 🟠 ** 71.5** (`-0.8`) | 0.0% | 5.1% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_CAA-04_COST_PLUS1__L3_GC-05_TARGET_HERESY_PLUS1` | CAA-04 (Fałszywy Trop): cost 0 → 1 + GC-05 (Fałszywy Świadek): target_heresy 0 → 1 | 72.3 → 🟠 ** 71.5** (`-0.8`) | 0.0% | 5.1% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_CAA-04_COST_PLUS1__L3_GC-05_HERESY_SET2` | CAA-04 (Fałszywy Trop): cost 0 → 1 + GC-05 (Fałszywy Świadek): dodaj heresy = 2 | 72.3 → 🟠 ** 71.5** (`-0.8`) | 0.0% | 5.1% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_CAA-04_COST_PLUS1__L3_GC-05_HERESY_PLUS1` | CAA-04 (Fałszywy Trop): cost 0 → 1 + GC-05 (Fałszywy Świadek): heresy 0 → 1 | 72.3 → 🟠 ** 71.5** (`-0.8`) | 0.0% | 5.1% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_CAA-04_COST_PLUS1__L3_GC-05_TARGET_HERESY_SET1` | CAA-04 (Fałszywy Trop): cost 0 → 1 + GC-05 (Fałszywy Świadek): dodaj target_heresy = 1 | 72.3 → 🟠 ** 71.5** (`-0.8`) | 0.0% | 5.1% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_KB-07_HERESY_SET2__L3_CAA-01_GOLD_SET3` | KB-07 (Szantaż Pieczęcią): dodaj heresy = 2 + CAA-01 (Przejście Podziemiami): dodaj gold = 3 | 72.3 → 🟠 ** 70.8** (`-1.5`) | 0.0% | 5.1% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_CAA-04_COST_PLUS1__L3_GC-03_HERESY_PLUS1` | CAA-04 (Fałszywy Trop): cost 0 → 1 + GC-03 (Podrzucenie Księgi): heresy 0 → 1 | 72.3 → 🟠 ** 69.3** (`-3.0`) | 0.0% | 5.1% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_CAA-04_COST_PLUS1__L3_GC-03_HERESY_SET1` | CAA-04 (Fałszywy Trop): cost 0 → 1 + GC-03 (Podrzucenie Księgi): dodaj heresy = 1 | 72.3 → 🟠 ** 69.3** (`-3.0`) | 0.0% | 5.1% | ⚪ STRATA/NEUTRALNY |