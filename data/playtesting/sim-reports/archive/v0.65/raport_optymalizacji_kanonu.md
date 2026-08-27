# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.65 (Iteracja #7, Faza 1D)

**Wersja Poprzednia:** `v0.64` (4P: `94.0 pkt`) → **Nowa Wersja:** `v0.65` (4P: `94.5 pkt`)
**Data:** 2026-08-16 17:05 | **Czas Trwania Iteracji:** 296.5s | **Zysk 4P:** `+0.5 pkt` | **Zysk Global:** `0.0 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_KT-09_COST_PLUS1` — **KT-09 (Fragment Kodeksu): cost 1 → 2**
- **Opis Modyfikacji:** Karta `kt-09` (Fragment Kodeksu): `cost` → `2`
- **Wynik Kanonu 4P Score:** 94.0 → 🟢 ** 94.5** (`⬆️ +0.5`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 91.6 → 91.0 (`-0.6`) pkt
  - `4p-no-cienie`: 89.2 → 90.7 (`⬆️ +1.5`) pkt
  - `4p-no-kabala`: 99.5 pkt
  - `4p-no-korona`: 94.6 → 95.4 (`⬆️ +0.8`) pkt
  - `4p-no-oficjum`: 95.0 → 95.8 (`⬆️ +0.8`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 67.2 → 67.4 (`⬆️ +0.2`) pkt
- **Tryb 4-osobowy (4p Avg):** 91.1 → 91.8 (`⬆️ +0.7`) pkt
- **Tryb 5-osobowy (5p Avg):** 71.9 → 70.9 (`-1.0`) pkt
- **Global Game Balance Score:** 🟡 ** 76.7** pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.46 Er`
  - **Deadlocki (Limit Er):** `0.4%` (norma: <5%)
  - **Pas Biedy (Złoto):** `24.4%` (norma: <30%)
  - **Autodafé / partię:** `1.44`
  - **Oskarżenia / partię:** `3.05`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 1 → 2 | 94.0 → 🟢 ** 94.5** (`⬆️ +0.5`) | 0.4% | 24.4% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KT-09_GOLD_MINUS1` | KT-09 (Fragment Kodeksu): gold 1 → 0 | 94.0 → 🟢 ** 94.4** (`⬆️ +0.4`) | 0.4% | 24.4% | 🟢 ZYSK |
| #3 | `L3_KT-09_COST_MINUS1` | KT-09 (Fragment Kodeksu): cost 1 → 0 | 94.0 → 🟢 ** 94.1** (`⬆️ +0.1`) | 0.4% | 24.4% | 🟢 ZYSK |
| #4 | `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 🟢 ** 94.0** | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #5 | `L1_MAX_ERAS_PLUS1` | Limit Er: 11 → 12 | 🟢 ** 94.0** | 0.1% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #6 | `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 🟢 ** 94.0** | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_GC-05_TARGET_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): target_heresy 0 → 1 | 🟢 ** 94.0** | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_GC-05_COST_PLUS1` | GC-05 (Fałszywy Świadek): cost 0 → 1 | 🟢 ** 94.0** | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_GC-05_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): heresy 0 → 1 | 🟢 ** 94.0** | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #10 | `L4_SEA_ROUTE_ERA4` | Szlak Morski: Era 5 → Era 4 | 🟢 ** 94.0** | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_GC-05_GOLD_PLUS1` | GC-05 (Fałszywy Świadek): gold 0 → 1 | 🟢 ** 94.0** | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #12 | `L4_SEA_ROUTE_ERA6` | Szlak Morski: Era 5 → Era 6 | 94.0 → 🟢 ** 93.9** (`-0.1`) | 0.4% | 24.5% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_GC-07_HERESY_PLUS1` | GC-07 (Skrytobójstwo): heresy 0 → 1 | 94.0 → 🟢 ** 93.9** (`-0.1`) | 0.3% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_GC-06_GOLD_PLUS1` | GC-06 (Szantaż): gold 0 → 1 | 94.0 → 🟢 ** 93.9** (`-0.1`) | 0.3% | 23.8% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_KT-03_COST_PLUS1` | KT-03 (Zakazana Wiedza): cost 0 → 1 | 94.0 → 🟢 ** 93.9** (`-0.1`) | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_KT-07_COST_MINUS1` | KT-07 (Archiwum Ukryte): cost 1 → 0 | 94.0 → 🟢 ** 93.9** (`-0.1`) | 0.3% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_GC-02_HERESY_MINUS1` | GC-02 (Czarny Rynek): heresy 1 → 0 | 94.0 → 🟢 ** 93.8** (`-0.2`) | 0.3% | 24.5% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_KT-03_GOLD_MINUS1` | KT-03 (Zakazana Wiedza): gold 1 → 0 | 94.0 → 🟢 ** 93.7** (`-0.3`) | 0.3% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_SO-04_HERESY_PLUS1` | SO-04 (Publiczne Ostrzeżenie): heresy 0 → 1 | 94.0 → 🟢 ** 93.6** (`-0.4`) | 0.3% | 24.3% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_GC-02_HERESY_PLUS1` | GC-02 (Czarny Rynek): heresy 1 → 2 | 94.0 → 🟢 ** 93.6** (`-0.4`) | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 0 → 1 | 94.0 → 🟢 ** 93.2** (`-0.8`) | 0.3% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_SO-10_COST_PLUS1` | SO-10 (Oczyść Miasto): cost 5 → 6 | 94.0 → 🟢 ** 93.1** (`-0.9`) | 0.4% | 24.9% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_CAA-05_COST_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 2 | 94.0 → 🟢 ** 93.1** (`-0.9`) | 0.3% | 24.6% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_GC-09_HERESY_PLUS1` | GC-09 (Lista Dłużników): heresy 0 → 1 | 94.0 → 🟢 ** 92.9** (`-1.1`) | 0.3% | 24.4% | ⚪ STRATA/NEUTRALNY |