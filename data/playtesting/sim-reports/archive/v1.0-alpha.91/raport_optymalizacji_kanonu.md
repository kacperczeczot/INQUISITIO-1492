# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.91 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.90` (4P: `92.0 pkt`) → **Nowa Wersja:** `v1.0-alpha.91` (4P: `92.1 pkt`)
**Data:** 2026-08-29 02:58 | **Czas Trwania Iteracji:** 129.0s | **Zysk 4P:** `+0.1 pkt` | **Zysk Global:** `+0.1 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_GC-07_GOLD_SET2` — **GC-07 (Skrytobójstwo): dodaj gold = 2**
- **Opis Modyfikacji:** Karta `gc-07` (Skrytobójstwo): `gold` → `2`
- **Wynik Kanonu 4P Balance:** 92.0 → 🟢 ** 92.1** (`⬆️ +0.1`) pkt (±0.94)
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 85.0 → 85.0 (`= 0.0`) pkt
  - `4p-no-cienie`: 84.3 → 84.8 (`⬆️ +0.5`) pkt
  - `4p-no-kabala`: 97.5 → 96.5 (`🔻 -1.0`) pkt
  - `4p-no-korona`: 94.1 → 94.4 (`⬆️ +0.3`) pkt
  - `4p-no-oficjum`: 98.9 → 99.8 (`⬆️ +0.9`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 32.7 → 32.7 (`= 0.0`) pkt
- **Tryb 4-osobowy (4p Avg):** 92.0 → 92.1 (`⬆️ +0.1`) pkt
- **Tryb 5-osobowy (5p Avg):** 25.1 → 25.1 (`= 0.0`) pkt
- **Global Game Balance Score:** 49.9 → 🔴 ** 50.0** (`⬆️ +0.1`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.75 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.9%` (norma: <30%)
  - **Autodafé / partię:** `1.52`
  - **Oskarżenia / partię:** `7.56`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | CI 95% | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-06_TARGET_HERESY_MINUS1` | CAA-06 (Ucieczka z Lochów): target_heresy 2 → 1 | 92.0 → 🟢 ** 93.0** (`⬆️ +1.0`) | `[91.2, 94.8]` | 0.0% | 4.9% | 🟢 ZYSK |
| #2 | `L3_GC-07_GOLD_SET2` | GC-07 (Skrytobójstwo): dodaj gold = 2 | 92.0 → 🟢 ** 92.7** (`⬆️ +0.7`) | `[90.8, 94.5]` | 0.0% | 4.9% | 🌟 ZWYCIĘZCA |
| #3 | `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 92.0 → 🟢 ** 92.6** (`⬆️ +0.6`) | `[90.8, 94.4]` | 0.0% | 4.9% | 🟢 ZYSK |
| #4 | `L3_GC-09_COST_MINUS1` | GC-09 (Lista Dłużników): cost 1 → 0 | 92.0 → 🟢 ** 92.3** (`⬆️ +0.3`) | `[90.5, 94.1]` | 0.0% | 4.9% | 🟢 ZYSK |
| #5 | `L3_CAA-07_HERESY_SET1` | CAA-07 (Szantaż Bractwa): dodaj heresy = 1 | 92.0 → 🟢 ** 92.1** (`⬆️ +0.1`) | `[90.3, 93.9]` | 0.0% | 4.8% | 🟢 ZYSK |
| #6 | `L3_KT-01_HERESY_PLUS1` | KT-01 (Rytuał Przejścia): heresy 0 → 1 | 92.0 → 🟢 ** 92.1** (`⬆️ +0.1`) | `[90.2, 94.0]` | 0.0% | 4.9% | 🟢 ZYSK |
| #7 | `L3_GC-10_GOLD_SET1` | GC-10 (Upadek Domu): dodaj gold = 1 | 92.0 → 🟢 ** 92.0** (`= 0.0`) | `[90.1, 93.9]` | 0.0% | 4.8% | ⚪ STRATA/NEUTRALNY |
| #8 | `L1_OBSERVED_PLUS1` | Próg Obserwowanej: 4 → 5 | 92.0 → 🟢 ** 92.0** (`= 0.0`) | `[90.1, 93.9]` | 0.0% | 4.9% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_CAA-11_COST_PLUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 2 | 92.0 → 🟢 ** 92.0** (`= 0.0`) | `[90.1, 93.9]` | 0.0% | 4.8% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 0 → 1 | 92.0 → 🟢 ** 92.0** (`= 0.0`) | `[90.2, 93.8]` | 0.0% | 4.9% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_KB-11_TARGET_HERESY_PLUS1` | KB-11 (Tajny Emisariusz): target_heresy 1 → 2 | 92.0 → 🟢 ** 91.9** (`🔻 -0.1`) | `[90.0, 93.8]` | 0.0% | 4.8% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-05_GOLD_PLUS1` | CAA-05 (Ukryty Kurier): gold 3 → 4 | 92.0 → 🟢 ** 91.9** (`🔻 -0.1`) | `[90.0, 93.8]` | 0.0% | 4.9% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_GC-02_COST_PLUS1` | GC-02 (Czarny Rynek): cost 0 → 1 | 92.0 → 🟢 ** 91.9** (`🔻 -0.1`) | `[90.0, 93.8]` | 0.0% | 4.9% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_GC-09_GOLD_SET3` | GC-09 (Lista Dłużników): dodaj gold = 3 | 92.0 → 🟢 ** 91.9** (`🔻 -0.1`) | `[90.0, 93.8]` | 0.0% | 4.8% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_GC-05_GOLD_PLUS1` | GC-05 (Fałszywy Świadek): gold 0 → 1 | 92.0 → 🟢 ** 91.9** (`🔻 -0.1`) | `[90.0, 93.8]` | 0.0% | 4.8% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_GC-03_GOLD_PLUS1` | GC-03 (Podrzucenie Księgi): gold 0 → 1 | 92.0 → 🟢 ** 91.9** (`🔻 -0.1`) | `[90.0, 93.8]` | 0.0% | 4.8% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_SO-07_HERESY_SET1` | SO-07 (Przesłuchanie Oficjum): dodaj heresy = 1 | 92.0 → 🟢 ** 91.9** (`🔻 -0.1`) | `[90.0, 93.8]` | 0.0% | 4.9% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_GC-01_COST_PLUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 2 | 92.0 → 🟢 ** 91.8** (`🔻 -0.2`) | `[89.9, 93.7]` | 0.0% | 4.9% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_SO-02_COST_MINUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 0 | 92.0 → 🟢 ** 91.8** (`🔻 -0.2`) | `[89.9, 93.7]` | 0.0% | 3.7% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_SO-05_GOLD_PLUS1` | SO-05 (Wezwanie do Trybunału): gold 0 → 1 | 92.0 → 🟢 ** 91.8** (`🔻 -0.2`) | `[89.9, 93.7]` | 0.0% | 4.8% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_SO-05_TARGET_HERESY_PLUS1` | SO-05 (Wezwanie do Trybunału): target_heresy 1 → 2 | 92.0 → 🟢 ** 91.8** (`🔻 -0.2`) | `[90.0, 93.7]` | 0.0% | 4.9% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_SO-12_HERESY_PLUS1` | SO-12 (Straż Trybunalska): heresy 2 → 3 | 92.0 → 🟢 ** 91.8** (`🔻 -0.2`) | `[89.9, 93.7]` | 0.0% | 4.8% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_GC-03_COST_PLUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 2 | 92.0 → 🟢 ** 91.7** (`🔻 -0.3`) | `[89.8, 93.6]` | 0.0% | 4.9% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_GC-04_GOLD_SET3` | GC-04 (Informator): dodaj gold = 3 | 92.0 → 🟢 ** 91.7** (`🔻 -0.3`) | `[89.8, 93.6]` | 0.0% | 4.8% | ⚪ STRATA/NEUTRALNY |
| #25 | `L3_KB-01_HERESY_PLUS1` | KB-01 (Rozkaz Dworu): heresy 1 → 2 | 92.0 → 🟢 ** 91.7** (`🔻 -0.3`) | `[89.8, 93.6]` | 0.0% | 4.7% | ⚪ STRATA/NEUTRALNY |
| #26 | `L3_KT-10_GOLD_SET1` | KT-10 (Pieczęć Salomona): dodaj gold = 1 | 92.0 → 🟢 ** 91.7** (`🔻 -0.3`) | `[89.8, 93.6]` | 0.0% | 4.8% | ⚪ STRATA/NEUTRALNY |
| #27 | `L3_CAA-09_TARGET_HERESY_SET1` | CAA-09 (Kurier Relikwii): dodaj target_heresy = 1 | 92.0 → 🟢 ** 91.7** (`🔻 -0.3`) | `[89.8, 93.6]` | 0.0% | 4.8% | ⚪ STRATA/NEUTRALNY |
| #28 | `L3_GC-05_GOLD_SET2` | GC-05 (Fałszywy Świadek): dodaj gold = 2 | 92.0 → 🟢 ** 91.7** (`🔻 -0.3`) | `[89.8, 93.6]` | 0.0% | 4.9% | ⚪ STRATA/NEUTRALNY |
| #29 | `L3_KT-10_TARGET_HERESY_SET1` | KT-10 (Pieczęć Salomona): dodaj target_heresy = 1 | 92.0 → 🟢 ** 91.7** (`🔻 -0.3`) | `[89.8, 93.5]` | 0.0% | 4.9% | ⚪ STRATA/NEUTRALNY |
| #30 | `L3_SO-11_GOLD_PLUS1` | SO-11 (Dekret Czystości Wiary): gold 1 → 2 | 92.0 → 🟢 ** 91.7** (`🔻 -0.3`) | `[89.8, 93.6]` | 0.0% | 4.6% | ⚪ STRATA/NEUTRALNY |