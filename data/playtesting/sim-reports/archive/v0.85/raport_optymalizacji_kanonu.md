# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.85 (Iteracja #8, Faza 1D)

**Wersja Poprzednia:** `v0.84` (4P: `94.2 pkt`) → **Nowa Wersja:** `v0.85` (4P: `94.5 pkt`)
**Data:** 2026-08-17 04:34 | **Czas Trwania Iteracji:** 1545.3s | **Zysk 4P:** `+0.3 pkt` | **Zysk Global:** `-1.4 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_CAA-08_TARGET_HERESY_PLUS1` — **CAA-08 (Kaptur Nocy): target_heresy 0 → 1**
- **Opis Modyfikacji:** Karta `caa-08` (Kaptur Nocy): `target_heresy` → `1`
- **Wynik Kanonu 4P Score:** 94.2 → 🟢 ** 94.5** (`⬆️ +0.3`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 95.1 → 96.7 (`⬆️ +1.6`) pkt
  - `4p-no-cienie`: 88.9 pkt
  - `4p-no-kabala`: 98.6 pkt
  - `4p-no-korona`: 96.2 → 96.3 (`⬆️ +0.1`) pkt
  - `4p-no-oficjum`: 92.2 pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 45.9 → 46.2 (`⬆️ +0.3`) pkt
- **Tryb 4-osobowy (4p Avg):** 91.1 → 91.4 (`⬆️ +0.3`) pkt
- **Tryb 5-osobowy (5p Avg):** 71.7 → 67.0 (`-4.7`) pkt
- **Global Game Balance Score:** 69.6 → 🟠 ** 68.2** (`-1.4`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.93 Er`
  - **Deadlocki (Limit Er):** `1.1%` (norma: <5%)
  - **Pas Biedy (Złoto):** `5.6%` (norma: <30%)
  - **Autodafé / partię:** `1.53`
  - **Oskarżenia / partię:** `3.62`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-08_TARGET_HERESY_PLUS1` | CAA-08 (Kaptur Nocy): target_heresy 0 → 1 | 94.2 → 🟢 ** 94.5** (`⬆️ +0.3`) | 1.1% | 5.6% | 🌟 ZWYCIĘZCA |
| #2 | `L3_CAA-10_COST_MINUS1` | CAA-10 (Echo Alhambry): cost 1 → 0 | 94.2 → 🟢 ** 94.3** (`⬆️ +0.1`) | 1.2% | 5.5% | 🟢 ZYSK |
| #3 | `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 3 → 4 | 🟢 ** 94.2** | 1.1% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #4 | `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–9 → 2–9 | 🟢 ** 94.2** | 1.1% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #5 | `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–9 → 4–9 | 🟢 ** 94.2** | 1.1% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_CAA-05_COST_MINUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 | 🟢 ** 94.2** | 1.1% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_CAA-05_GOLD_PLUS1` | CAA-05 (Ukryty Kurier): gold 0 → 1 | 🟢 ** 94.2** | 1.1% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_CAA-08_HERESY_PLUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 2 | 🟢 ** 94.2** | 1.1% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_CAA-08_HERESY_MINUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 0 | 🟢 ** 94.2** | 1.1% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_CAA-08_GOLD_PLUS1` | CAA-08 (Kaptur Nocy): gold 0 → 1 | 🟢 ** 94.2** | 1.1% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_GC-05_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): heresy 0 → 1 | 🟢 ** 94.2** | 1.1% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_GC-05_TARGET_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): target_heresy 0 → 1 | 🟢 ** 94.2** | 1.1% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_GC-05_GOLD_PLUS1` | GC-05 (Fałszywy Świadek): gold 0 → 1 | 🟢 ** 94.2** | 1.1% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_KB-01_HERESY_MINUS1` | KB-01 (Rozkaz Dworu): heresy 1 → 0 | 🟢 ** 94.2** | 1.1% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_CAA-09_GOLD_PLUS1` | CAA-09 (Kurier Relikwii): gold 0 → 1 | 94.2 → 🟢 ** 94.1** (`-0.1`) | 1.2% | 5.4% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_CAA-10_GOLD_PLUS1` | CAA-10 (Echo Alhambry): gold 0 → 1 | 94.2 → 🟢 ** 94.1** (`-0.1`) | 1.2% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_CAA-06_GOLD_PLUS1` | CAA-06 (Ucieczka z Lochów): gold 0 → 1 | 94.2 → 🟢 ** 94.1** (`-0.1`) | 1.1% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 1 → 2 | 94.2 → 🟢 ** 93.9** (`-0.3`) | 1.0% | 5.7% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_CAA-05_COST_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 2 | 94.2 → 🟢 ** 93.6** (`-0.6`) | 1.1% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_KB-03_HERESY_PLUS1` | KB-03 (Plotka Dworska): heresy 1 → 2 | 94.2 → 🟢 ** 93.1** (`-1.1`) | 1.1% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_CAA-04_COST_MINUS1` | CAA-04 (Fałszywy Trop): cost 1 → 0 | 94.2 → 🟢 ** 93.0** (`-1.2`) | 1.1% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_CAA-04_GOLD_PLUS1` | CAA-04 (Fałszywy Trop): gold 0 → 1 | 94.2 → 🟢 ** 93.0** (`-1.2`) | 1.1% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_SO-01_GOLD_PLUS1` | SO-01 (Patrol Familiariuszy): gold 0 → 1 | 94.2 → 🟢 ** 92.9** (`-1.3`) | 1.2% | 6.9% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_CAA-04_COST_PLUS1` | CAA-04 (Fałszywy Trop): cost 1 → 2 | 94.2 → 🟢 ** 92.7** (`-1.5`) | 1.1% | 5.5% | ⚪ STRATA/NEUTRALNY |