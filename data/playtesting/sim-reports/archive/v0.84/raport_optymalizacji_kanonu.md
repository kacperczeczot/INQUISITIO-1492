# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.84 (Iteracja #7, Faza 1D)

**Wersja Poprzednia:** `v0.83` (4P: `92.9 pkt`) → **Nowa Wersja:** `v0.84` (4P: `94.2 pkt`)
**Data:** 2026-08-17 04:07 | **Czas Trwania Iteracji:** 1947.7s | **Zysk 4P:** `+1.3 pkt` | **Zysk Global:** `+1.3 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L2_KT_HERESY_HIGH_PLUS1` — **Kabała Pasmo: 3–8 → 3–9**
- **Opis Modyfikacji:** Kabała Toledo: Pasmo Herezji 3–9
- **Wynik Kanonu 4P Score:** 92.9 → 🟢 ** 94.2** (`⬆️ +1.3`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 95.3 → 95.1 (`-0.2`) pkt
  - `4p-no-cienie`: 86.8 → 88.9 (`⬆️ +2.1`) pkt
  - `4p-no-kabala`: 98.6 pkt
  - `4p-no-korona`: 92.6 → 96.2 (`⬆️ +3.6`) pkt
  - `4p-no-oficjum`: 91.1 → 92.2 (`⬆️ +1.1`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 47.2 → 45.9 (`-1.3`) pkt
- **Tryb 4-osobowy (4p Avg):** 90.3 → 91.1 (`⬆️ +0.8`) pkt
- **Tryb 5-osobowy (5p Avg):** 67.3 → 71.7 (`⬆️ +4.4`) pkt
- **Global Game Balance Score:** 68.3 → 🟠 ** 69.6** (`⬆️ +1.3`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.93 Er`
  - **Deadlocki (Limit Er):** `1.1%` (norma: <5%)
  - **Pas Biedy (Złoto):** `5.5%` (norma: <30%)
  - **Autodafé / partię:** `1.53`
  - **Oskarżenia / partię:** `3.61`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–8 → 3–9 | 92.9 → 🟢 ** 94.2** (`⬆️ +1.3`) | 1.1% | 5.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_CAA-04_HERESY_PLUS1` | CAA-04 (Fałszywy Trop): heresy 0 → 1 | 92.9 → 🟢 ** 93.3** (`⬆️ +0.4`) | 1.1% | 5.4% | 🟢 ZYSK |
| #3 | `L3_CAA-10_COST_MINUS1` | CAA-10 (Echo Alhambry): cost 1 → 0 | 92.9 → 🟢 ** 93.1** (`⬆️ +0.2`) | 1.2% | 5.5% | 🟢 ZYSK |
| #4 | `L3_CAA-10_GOLD_PLUS1` | CAA-10 (Echo Alhambry): gold 0 → 1 | 🟢 ** 92.9** | 1.3% | 5.4% | ⚪ STRATA/NEUTRALNY |
| #5 | `L3_CAA-05_COST_MINUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 | 🟢 ** 92.9** | 1.2% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_CAA-05_GOLD_PLUS1` | CAA-05 (Ukryty Kurier): gold 0 → 1 | 🟢 ** 92.9** | 1.2% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #7 | `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 3 → 4 | 🟢 ** 92.9** | 1.2% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #8 | `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 🟢 ** 92.9** | 1.2% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_CAA-06_GOLD_PLUS1` | CAA-06 (Ucieczka z Lochów): gold 0 → 1 | 🟢 ** 92.9** | 1.2% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_CAA-08_HERESY_MINUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 0 | 🟢 ** 92.9** | 1.2% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_CAA-08_HERESY_PLUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 2 | 🟢 ** 92.9** | 1.2% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-08_GOLD_PLUS1` | CAA-08 (Kaptur Nocy): gold 0 → 1 | 🟢 ** 92.9** | 1.2% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_GC-05_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): heresy 0 → 1 | 🟢 ** 92.9** | 1.2% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_GC-05_GOLD_PLUS1` | GC-05 (Fałszywy Świadek): gold 0 → 1 | 🟢 ** 92.9** | 1.2% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_KB-01_HERESY_PLUS1` | KB-01 (Rozkaz Dworu): heresy 1 → 2 | 🟢 ** 92.9** | 1.2% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_GC-05_TARGET_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): target_heresy 0 → 1 | 🟢 ** 92.9** | 1.2% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_KB-01_HERESY_MINUS1` | KB-01 (Rozkaz Dworu): heresy 1 → 0 | 🟢 ** 92.9** | 1.2% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_CAA-09_GOLD_PLUS1` | CAA-09 (Kurier Relikwii): gold 0 → 1 | 92.9 → 🟢 ** 92.7** (`-0.2`) | 1.2% | 5.4% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_CAA-04_GOLD_PLUS1` | CAA-04 (Fałszywy Trop): gold 0 → 1 | 92.9 → 🟢 ** 92.6** (`-0.3`) | 1.2% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_CAA-04_COST_MINUS1` | CAA-04 (Fałszywy Trop): cost 1 → 0 | 92.9 → 🟢 ** 92.6** (`-0.3`) | 1.2% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_CAA-07_HERESY_PLUS1` | CAA-07 (Szantaż Bractwa): heresy 0 → 1 | 92.9 → 🟢 ** 92.0** (`-0.9`) | 1.2% | 5.4% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_KT-05_COST_PLUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 2 | 92.9 → 🟢 ** 92.0** (`-0.9`) | 1.3% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_CAA-04_COST_PLUS1` | CAA-04 (Fałszywy Trop): cost 1 → 2 | 92.9 → 🟢 ** 92.0** (`-0.9`) | 1.2% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_KB-03_HERESY_PLUS1` | KB-03 (Plotka Dworska): heresy 1 → 2 | 92.9 → 🟢 ** 91.9** (`-1.0`) | 1.2% | 5.5% | ⚪ STRATA/NEUTRALNY |