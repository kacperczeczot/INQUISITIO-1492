# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.86 (Iteracja #9, Faza 2D)

**Wersja Poprzednia:** `v0.85` (4P: `94.5 pkt`) → **Nowa Wersja:** `v0.86` (4P: `94.6 pkt`)
**Data:** 2026-08-17 07:07 | **Czas Trwania Iteracji:** 5905.9s | **Zysk 4P:** `+0.1 pkt` | **Zysk Global:** `-0.8 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (2D):** `L3_CAA-05_COST_MINUS1__L3_CAA-03_GOLD_PLUS1` — **CAA-05 (Ukryty Kurier): cost 1 → 0 + CAA-03 (Cień na Rynku): gold 0 → 1**
- **Opis Modyfikacji:** Karta `caa-05` (Ukryty Kurier): `cost` → `0` + Karta `caa-03` (Cień na Rynku): `gold` → `1`
- **Wynik Kanonu 4P Score:** 94.5 → 🟢 ** 94.6** (`⬆️ +0.1`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 96.7 → 97.6 (`⬆️ +0.9`) pkt
  - `4p-no-cienie`: 88.9 pkt
  - `4p-no-kabala`: 98.6 → 98.5 (`-0.1`) pkt
  - `4p-no-korona`: 96.3 → 96.4 (`⬆️ +0.1`) pkt
  - `4p-no-oficjum`: 92.2 → 91.6 (`-0.6`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 46.2 → 45.7 (`-0.5`) pkt
- **Tryb 4-osobowy (4p Avg):** 91.4 → 91.6 (`⬆️ +0.2`) pkt
- **Tryb 5-osobowy (5p Avg):** 67.0 → 65.0 (`-2.0`) pkt
- **Global Game Balance Score:** 68.2 → 🟠 ** 67.4** (`-0.8`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.94 Er`
  - **Deadlocki (Limit Er):** `1.1%` (norma: <5%)
  - **Pas Biedy (Złoto):** `5.6%` (norma: <30%)
  - **Autodafé / partię:** `1.53`
  - **Oskarżenia / partię:** `3.63`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-05_COST_MINUS1__L3_CAA-03_GOLD_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 + CAA-03 (Cień na Rynku): gold 0 → 1 | 94.5 → 🟢 ** 94.6** (`⬆️ +0.1`) | 1.1% | 5.6% | 🌟 ZWYCIĘZCA |
| #2 | `L3_CAA-05_GOLD_PLUS1__L3_CAA-03_GOLD_PLUS1` | CAA-05 (Ukryty Kurier): gold 0 → 1 + CAA-03 (Cień na Rynku): gold 0 → 1 | 94.5 → 🟢 ** 94.6** (`⬆️ +0.1`) | 1.1% | 5.6% | 🟢 ZYSK |
| #3 | `L2_SO_CONDEMNS_PLUS1__L3_CAA-05_COST_MINUS1` | Oficjum Skazania: 3 → 4 + CAA-05 (Ukryty Kurier): cost 1 → 0 | 🟢 ** 94.5** | 1.1% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #4 | `L2_SO_CONDEMNS_PLUS1__L3_CAA-05_GOLD_PLUS1` | Oficjum Skazania: 3 → 4 + CAA-05 (Ukryty Kurier): gold 0 → 1 | 🟢 ** 94.5** | 1.1% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #5 | `L3_CAA-05_COST_MINUS1__L2_SO_CONDEMNS_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 + Oficjum Skazania: 3 → 4 | 🟢 ** 94.5** | 1.1% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_CAA-05_GOLD_PLUS1__L2_SO_CONDEMNS_PLUS1` | CAA-05 (Ukryty Kurier): gold 0 → 1 + Oficjum Skazania: 3 → 4 | 🟢 ** 94.5** | 1.1% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_CAA-05_COST_MINUS1__L2_KT_HERESY_LOW_MINUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 + Kabała Pasmo: 3–9 → 2–9 | 🟢 ** 94.5** | 1.1% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_CAA-05_COST_MINUS1__L2_KT_HERESY_LOW_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 + Kabała Pasmo: 3–9 → 4–9 | 🟢 ** 94.5** | 1.1% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_CAA-05_COST_MINUS1__L3_GC-05_HERESY_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 + GC-05 (Fałszywy Świadek): heresy 0 → 1 | 🟢 ** 94.5** | 1.1% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_CAA-05_COST_MINUS1__L3_GC-05_GOLD_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 + GC-05 (Fałszywy Świadek): gold 0 → 1 | 🟢 ** 94.5** | 1.1% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_CAA-05_COST_MINUS1__L3_KB-01_HERESY_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 + KB-01 (Rozkaz Dworu): heresy 1 → 2 | 🟢 ** 94.5** | 1.1% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-05_GOLD_PLUS1__L3_CAA-08_HERESY_PLUS1` | CAA-05 (Ukryty Kurier): gold 0 → 1 + CAA-08 (Kaptur Nocy): heresy 1 → 2 | 94.5 → 🟢 ** 94.4** (`-0.1`) | 1.1% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_CAA-05_COST_MINUS1__L3_CAA-08_HERESY_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 + CAA-08 (Kaptur Nocy): heresy 1 → 2 | 94.5 → 🟢 ** 94.4** (`-0.1`) | 1.1% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_CAA-05_COST_MINUS1__L3_CAA-06_GOLD_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 + CAA-06 (Ucieczka z Lochów): gold 0 → 1 | 94.5 → 🟢 ** 94.4** (`-0.1`) | 1.1% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_CAA-05_COST_MINUS1__L3_CAA-05_GOLD_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 + CAA-05 (Ukryty Kurier): gold 0 → 1 | 94.5 → 🟢 ** 94.4** (`-0.1`) | 1.1% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_CAA-05_GOLD_PLUS1__L3_CAA-05_COST_MINUS1` | CAA-05 (Ukryty Kurier): gold 0 → 1 + CAA-05 (Ukryty Kurier): cost 1 → 0 | 94.5 → 🟢 ** 94.4** (`-0.1`) | 1.1% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_CAA-06_GOLD_PLUS1__L3_CAA-05_COST_MINUS1` | CAA-06 (Ucieczka z Lochów): gold 0 → 1 + CAA-05 (Ukryty Kurier): cost 1 → 0 | 94.5 → 🟢 ** 94.4** (`-0.1`) | 1.1% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_CAA-06_GOLD_PLUS1__L3_CAA-05_GOLD_PLUS1` | CAA-06 (Ucieczka z Lochów): gold 0 → 1 + CAA-05 (Ukryty Kurier): gold 0 → 1 | 94.5 → 🟢 ** 94.4** (`-0.1`) | 1.1% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_CAA-05_GOLD_PLUS1__L3_CAA-06_GOLD_PLUS1` | CAA-05 (Ukryty Kurier): gold 0 → 1 + CAA-06 (Ucieczka z Lochów): gold 0 → 1 | 94.5 → 🟢 ** 94.4** (`-0.1`) | 1.1% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #20 | `L2_SO_CONDEMNS_PLUS1__L3_CAA-10_COST_MINUS1` | Oficjum Skazania: 3 → 4 + CAA-10 (Echo Alhambry): cost 1 → 0 | 94.5 → 🟢 ** 94.3** (`-0.2`) | 1.2% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_CAA-05_COST_MINUS1__L3_KB-01_TARGET_HERESY_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 + KB-01 (Rozkaz Dworu): target_heresy 0 → 1 | 94.5 → 🟢 ** 94.3** (`-0.2`) | 1.2% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_CAA-05_GOLD_PLUS1__L3_KB-01_TARGET_HERESY_PLUS1` | CAA-05 (Ukryty Kurier): gold 0 → 1 + KB-01 (Rozkaz Dworu): target_heresy 0 → 1 | 94.5 → 🟢 ** 94.2** (`-0.3`) | 1.2% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_CAA-05_COST_MINUS1__L3_CAA-10_COST_MINUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 + CAA-10 (Echo Alhambry): cost 1 → 0 | 94.5 → 🟢 ** 93.9** (`-0.6`) | 1.2% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_CAA-05_GOLD_PLUS1__L3_CAA-10_COST_MINUS1` | CAA-05 (Ukryty Kurier): gold 0 → 1 + CAA-10 (Echo Alhambry): cost 1 → 0 | 94.5 → 🟢 ** 93.9** (`-0.6`) | 1.2% | 5.5% | ⚪ STRATA/NEUTRALNY |