[Strona główna](../../../../../README.md) > [v0.66](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.66 (Iteracja #8, Faza 1D)

**Wersja Poprzednia:** `v0.65` (4P: `94.5 pkt`) → **Nowa Wersja:** `v0.66` (4P: `95.0 pkt`)
**Data:** 2026-08-16 17:11 | **Czas Trwania Iteracji:** 325.1s | **Zysk 4P:** `+0.5 pkt` | **Zysk Global:** `-1.8 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_SO-02_GOLD_PLUS1` — **SO-02 (Skarbiec Trybunału): gold 2 → 3**
- **Opis Modyfikacji:** Karta `so-02` (Skarbiec Trybunału): `gold` → `3`
- **Wynik Kanonu 4P Score:** 94.5 → 🟢 ** 95.0** (`⬆️ +0.5`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 91.0 → 92.0 (`⬆️ +1.0`) pkt
  - `4p-no-cienie`: 90.7 → 93.0 (`⬆️ +2.3`) pkt
  - `4p-no-kabala`: 99.5 → 97.9 (`-1.6`) pkt
  - `4p-no-korona`: 95.4 → 96.4 (`⬆️ +1.0`) pkt
  - `4p-no-oficjum`: 95.8 pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 67.4 → 68.5 (`⬆️ +1.1`) pkt
- **Tryb 4-osobowy (4p Avg):** 91.8 → 91.7 (`-0.1`) pkt
- **Tryb 5-osobowy (5p Avg):** 70.9 → 64.5 (`-6.4`) pkt
- **Global Game Balance Score:** 76.7 → 🟠 ** 74.9** (`-1.8`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.44 Er`
  - **Deadlocki (Limit Er):** `0.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `23.9%` (norma: <30%)
  - **Autodafé / partię:** `1.49`
  - **Oskarżenia / partię:** `3.07`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-02_GOLD_PLUS1` | SO-02 (Skarbiec Trybunału): gold 2 → 3 | 94.5 → 🟢 ** 95.0** (`⬆️ +0.5`) | 0.3% | 23.9% | 🌟 ZWYCIĘZCA |
| #2 | `L4_SEA_ROUTE_ERA6` | Szlak Morski: Era 5 → Era 6 | 🟢 ** 94.5** | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #3 | `L1_MAX_ERAS_PLUS1` | Limit Er: 11 → 12 | 🟢 ** 94.5** | 0.1% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #4 | `L3_CAA-04_GOLD_PLUS1` | CAA-04 (Fałszywy Trop): gold 1 → 2 | 🟢 ** 94.5** | 0.4% | 24.3% | ⚪ STRATA/NEUTRALNY |
| #5 | `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 🟢 ** 94.5** | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #6 | `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 🟢 ** 94.5** | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #7 | `L4_TIME_DECK_EVERY_ERA` | Edykty Czasu: co 1 Erę → co 1 Erę | 🟢 ** 94.5** | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_GC-05_TARGET_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): target_heresy 0 → 1 | 🟢 ** 94.5** | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_GC-05_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): heresy 0 → 1 | 🟢 ** 94.5** | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_GC-05_GOLD_PLUS1` | GC-05 (Fałszywy Świadek): gold 0 → 1 | 🟢 ** 94.5** | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_SO-05_TARGET_HERESY_PLUS1` | SO-05 (Wezwanie do Trybunału): target_heresy 2 → 3 | 🟢 ** 94.5** | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_SO-05_COST_PLUS1` | SO-05 (Wezwanie do Trybunału): cost 0 → 1 | 🟢 ** 94.5** | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_GC-05_COST_PLUS1` | GC-05 (Fałszywy Świadek): cost 0 → 1 | 🟢 ** 94.5** | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_SO-05_HERESY_PLUS1` | SO-05 (Wezwanie do Trybunału): heresy 0 → 1 | 🟢 ** 94.5** | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_SO-05_GOLD_PLUS1` | SO-05 (Wezwanie do Trybunału): gold 0 → 1 | 🟢 ** 94.5** | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_SO-05_TARGET_HERESY_MINUS1` | SO-05 (Wezwanie do Trybunału): target_heresy 2 → 1 | 🟢 ** 94.5** | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_GC-02_HERESY_PLUS1` | GC-02 (Czarny Rynek): heresy 1 → 2 | 94.5 → 🟢 ** 94.2** (`-0.3`) | 0.4% | 24.3% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_GC-07_HERESY_PLUS1` | GC-07 (Skrytobójstwo): heresy 0 → 1 | 94.5 → 🟢 ** 94.1** (`-0.4`) | 0.3% | 24.3% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_SO-06_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): heresy 0 → 1 | 94.5 → 🟢 ** 93.9** (`-0.6`) | 0.3% | 24.3% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 0 → 1 | 94.5 → 🟢 ** 93.8** (`-0.7`) | 0.4% | 24.3% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_GC-06_GOLD_PLUS1` | GC-06 (Szantaż): gold 0 → 1 | 94.5 → 🟢 ** 93.8** (`-0.7`) | 0.3% | 23.7% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_GC-09_HERESY_PLUS1` | GC-09 (Lista Dłużników): heresy 0 → 1 | 94.5 → 🟢 ** 93.5** (`-1.0`) | 0.3% | 24.3% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_GC-02_GOLD_PLUS1` | GC-02 (Czarny Rynek): gold 2 → 3 | 94.5 → 🟢 ** 93.1** (`-1.4`) | 0.3% | 24.2% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_CAA-07_GOLD_PLUS1` | CAA-07 (Szantaż Bractwa): gold 0 → 1 | 94.5 → 🟢 ** 92.8** (`-1.7`) | 0.4% | 24.3% | ⚪ STRATA/NEUTRALNY |