[Strona główna](../../../../../README.md) > [v0.67](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.67 (Iteracja #9, Faza 1D)

**Wersja Poprzednia:** `v0.66` (4P: `95.0 pkt`) → **Nowa Wersja:** `v0.67` (4P: `95.1 pkt`)
**Data:** 2026-08-16 17:16 | **Czas Trwania Iteracji:** 289.4s | **Zysk 4P:** `+0.1 pkt` | **Zysk Global:** `-0.1 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_KB-01_HERESY_PLUS1` — **KB-01 (Rozkaz Dworu): heresy 0 → 1**
- **Opis Modyfikacji:** Karta `kb-01` (Rozkaz Dworu): `heresy` → `1`
- **Wynik Kanonu 4P Score:** 95.0 → 🟢 ** 95.1** (`⬆️ +0.1`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 92.0 → 90.7 (`-1.3`) pkt
  - `4p-no-cienie`: 93.0 → 94.2 (`⬆️ +1.2`) pkt
  - `4p-no-kabala`: 97.9 → 98.5 (`⬆️ +0.6`) pkt
  - `4p-no-korona`: 96.4 pkt
  - `4p-no-oficjum`: 95.8 → 95.9 (`⬆️ +0.1`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 68.5 → 69.9 (`⬆️ +1.4`) pkt
- **Tryb 4-osobowy (4p Avg):** 91.7 → 92.5 (`⬆️ +0.8`) pkt
- **Tryb 5-osobowy (5p Avg):** 64.5 → 61.9 (`-2.6`) pkt
- **Global Game Balance Score:** 74.9 → 🟠 ** 74.8** (`-0.1`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.42 Er`
  - **Deadlocki (Limit Er):** `0.4%` (norma: <5%)
  - **Pas Biedy (Złoto):** `23.9%` (norma: <30%)
  - **Autodafé / partię:** `1.49`
  - **Oskarżenia / partię:** `3.08`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_KB-01_HERESY_PLUS1` | KB-01 (Rozkaz Dworu): heresy 0 → 1 | 95.0 → 🟢 ** 95.1** (`⬆️ +0.1`) | 0.4% | 23.9% | 🌟 ZWYCIĘZCA |
| #2 | `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 🟢 ** 95.0** | 0.3% | 23.9% | ⚪ STRATA/NEUTRALNY |
| #3 | `L1_MAX_ERAS_PLUS1` | Limit Er: 11 → 12 | 🟢 ** 95.0** | 0.1% | 23.9% | ⚪ STRATA/NEUTRALNY |
| #4 | `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 🟢 ** 95.0** | 0.3% | 23.9% | ⚪ STRATA/NEUTRALNY |
| #5 | `L4_TIME_DECK_EVERY_ERA` | Edykty Czasu: co 1 Erę → co 1 Erę | 🟢 ** 95.0** | 0.3% | 23.9% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_GC-05_COST_PLUS1` | GC-05 (Fałszywy Świadek): cost 0 → 1 | 🟢 ** 95.0** | 0.3% | 23.9% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_GC-05_GOLD_PLUS1` | GC-05 (Fałszywy Świadek): gold 0 → 1 | 🟢 ** 95.0** | 0.3% | 23.9% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_GC-05_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): heresy 0 → 1 | 🟢 ** 95.0** | 0.3% | 23.9% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_SO-05_TARGET_HERESY_MINUS1` | SO-05 (Wezwanie do Trybunału): target_heresy 2 → 1 | 🟢 ** 95.0** | 0.3% | 23.9% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_SO-05_COST_PLUS1` | SO-05 (Wezwanie do Trybunału): cost 0 → 1 | 🟢 ** 95.0** | 0.3% | 23.9% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_GC-05_TARGET_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): target_heresy 0 → 1 | 🟢 ** 95.0** | 0.3% | 23.9% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_SO-05_TARGET_HERESY_PLUS1` | SO-05 (Wezwanie do Trybunału): target_heresy 2 → 3 | 🟢 ** 95.0** | 0.3% | 23.9% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_SO-05_GOLD_PLUS1` | SO-05 (Wezwanie do Trybunału): gold 0 → 1 | 🟢 ** 95.0** | 0.3% | 23.9% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_SO-05_HERESY_PLUS1` | SO-05 (Wezwanie do Trybunału): heresy 0 → 1 | 🟢 ** 95.0** | 0.3% | 23.9% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 0 → 1 | 95.0 → 🟢 ** 94.5** (`-0.5`) | 0.3% | 24.0% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_SO-04_COST_MINUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 0 | 95.0 → 🟢 ** 94.2** (`-0.8`) | 0.3% | 23.4% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_CAA-05_COST_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 2 | 95.0 → 🟢 ** 94.2** (`-0.8`) | 0.3% | 24.1% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_GC-02_HERESY_PLUS1` | GC-02 (Czarny Rynek): heresy 1 → 2 | 95.0 → 🟢 ** 94.2** (`-0.8`) | 0.3% | 23.9% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_CAA-08_GOLD_PLUS1` | CAA-08 (Kaptur Nocy): gold 0 → 1 | 95.0 → 🟢 ** 93.9** (`-1.1`) | 0.3% | 23.9% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_SO-04_GOLD_PLUS1` | SO-04 (Publiczne Ostrzeżenie): gold 0 → 1 | 95.0 → 🟢 ** 93.8** (`-1.2`) | 0.3% | 23.4% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_SO-02_GOLD_PLUS1` | SO-02 (Skarbiec Trybunału): gold 3 → 4 | 95.0 → 🟢 ** 93.6** (`-1.4`) | 0.3% | 23.5% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_SO-08_COST_MINUS1` | SO-08 (Nasłanie Inkwizytora): cost 1 → 0 | 95.0 → 🟢 ** 93.0** (`-2.0`) | 0.3% | 23.5% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 95.0 → 🟢 ** 92.8** (`-2.2`) | 0.5% | 24.1% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_CAA-07_GOLD_PLUS1` | CAA-07 (Szantaż Bractwa): gold 0 → 1 | 95.0 → 🟢 ** 92.7** (`-2.3`) | 0.3% | 23.9% | ⚪ STRATA/NEUTRALNY |