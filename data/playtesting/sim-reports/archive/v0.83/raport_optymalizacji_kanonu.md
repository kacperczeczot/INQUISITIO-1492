[Strona główna](../../../../../README.md) > [v0.83](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.83 (Iteracja #6, Faza 1D)

**Wersja Poprzednia:** `v0.82` (4P: `92.5 pkt`) → **Nowa Wersja:** `v0.83` (4P: `92.9 pkt`)
**Data:** 2026-08-17 03:34 | **Czas Trwania Iteracji:** 730.1s | **Zysk 4P:** `+0.4 pkt` | **Zysk Global:** `+0.7 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_GC-12_HERESY_PLUS1` — **GC-12 (Złodziejski Zwiad): heresy 1 → 2**
- **Opis Modyfikacji:** Karta `gc-12` (Złodziejski Zwiad): `heresy` → `2`
- **Wynik Kanonu 4P Score:** 92.5 → 🟢 ** 92.9** (`⬆️ +0.4`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 95.3 pkt
  - `4p-no-cienie`: 83.4 → 86.8 (`⬆️ +3.4`) pkt
  - `4p-no-kabala`: 97.2 → 98.6 (`⬆️ +1.4`) pkt
  - `4p-no-korona`: 93.3 → 92.6 (`-0.7`) pkt
  - `4p-no-oficjum`: 93.3 → 91.1 (`-2.2`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 47.4 → 47.2 (`-0.2`) pkt
- **Tryb 4-osobowy (4p Avg):** 88.6 → 90.3 (`⬆️ +1.7`) pkt
- **Tryb 5-osobowy (5p Avg):** 66.8 → 67.3 (`⬆️ +0.5`) pkt
- **Global Game Balance Score:** 67.6 → 🟠 ** 68.3** (`⬆️ +0.7`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.95 Er`
  - **Deadlocki (Limit Er):** `1.2%` (norma: <5%)
  - **Pas Biedy (Złoto):** `5.5%` (norma: <30%)
  - **Autodafé / partię:** `1.54`
  - **Oskarżenia / partię:** `3.63`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-12_HERESY_PLUS1` | GC-12 (Złodziejski Zwiad): heresy 1 → 2 | 92.5 → 🟢 ** 92.9** (`⬆️ +0.4`) | 1.2% | 5.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KB-01_TARGET_HERESY_PLUS1` | KB-01 (Rozkaz Dworu): target_heresy 0 → 1 | 92.5 → 🟢 ** 92.6** (`⬆️ +0.1`) | 1.3% | 5.8% | 🟢 ZYSK |
| #3 | `L3_CAA-04_COST_MINUS1` | CAA-04 (Fałszywy Trop): cost 1 → 0 | 🟢 ** 92.5** | 1.2% | 5.7% | ⚪ STRATA/NEUTRALNY |
| #4 | `L3_CAA-04_GOLD_PLUS1` | CAA-04 (Fałszywy Trop): gold 0 → 1 | 🟢 ** 92.5** | 1.2% | 5.7% | ⚪ STRATA/NEUTRALNY |
| #5 | `L3_GC-02_HERESY_PLUS1` | GC-02 (Czarny Rynek): heresy 1 → 2 | 🟢 ** 92.5** | 1.3% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 1 → 2 | 92.5 → 🟢 ** 92.3** (`-0.2`) | 1.2% | 5.9% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_CAA-05_COST_MINUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 | 92.5 → 🟢 ** 92.3** (`-0.2`) | 1.2% | 5.7% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_CAA-05_GOLD_PLUS1` | CAA-05 (Ukryty Kurier): gold 0 → 1 | 92.5 → 🟢 ** 92.3** (`-0.2`) | 1.2% | 5.7% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_CAA-08_TARGET_HERESY_PLUS1` | CAA-08 (Kaptur Nocy): target_heresy 0 → 1 | 92.5 → 🟢 ** 92.3** (`-0.2`) | 1.3% | 5.8% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_CAA-09_GOLD_PLUS1` | CAA-09 (Kurier Relikwii): gold 0 → 1 | 92.5 → 🟢 ** 92.2** (`-0.3`) | 1.2% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_CAA-07_COST_MINUS1` | CAA-07 (Szantaż Bractwa): cost 1 → 0 | 92.5 → 🟢 ** 92.1** (`-0.4`) | 1.3% | 5.7% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-07_GOLD_PLUS1` | CAA-07 (Szantaż Bractwa): gold 0 → 1 | 92.5 → 🟢 ** 92.1** (`-0.4`) | 1.3% | 5.7% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_CAA-10_COST_MINUS1` | CAA-10 (Echo Alhambry): cost 1 → 0 | 92.5 → 🟢 ** 92.0** (`-0.5`) | 1.3% | 5.7% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 2 → 3 | 92.5 → 🟢 ** 92.0** (`-0.5`) | 1.1% | 5.7% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_CAA-10_GOLD_PLUS1` | CAA-10 (Echo Alhambry): gold 0 → 1 | 92.5 → 🟢 ** 92.0** (`-0.5`) | 1.3% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_CAA-03_COST_PLUS1` | CAA-03 (Cień na Rynku): cost 0 → 1 | 92.5 → 🟢 ** 91.9** (`-0.6`) | 1.2% | 5.8% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_CAA-04_HERESY_PLUS1` | CAA-04 (Fałszywy Trop): heresy 0 → 1 | 92.5 → 🟢 ** 91.6** (`-0.9`) | 1.2% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_KB-03_HERESY_PLUS1` | KB-03 (Plotka Dworska): heresy 1 → 2 | 92.5 → 🟢 ** 91.6** (`-0.9`) | 1.2% | 5.7% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_KB-01_COST_MINUS1` | KB-01 (Rozkaz Dworu): cost 1 → 0 | 92.5 → 🟢 ** 91.3** (`-1.2`) | 1.3% | 4.1% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_CAA-04_COST_PLUS1` | CAA-04 (Fałszywy Trop): cost 1 → 2 | 92.5 → 🟢 ** 90.7** (`-1.8`) | 1.2% | 5.7% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_KT-05_COST_PLUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 2 | 92.5 → 🟢 ** 90.7** (`-1.8`) | 1.3% | 5.8% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_GC-12_COST_PLUS1` | GC-12 (Złodziejski Zwiad): cost 0 → 1 | 92.5 → 🟢 ** 90.4** (`-2.1`) | 1.2% | 5.9% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_GC-12_GOLD_MINUS1` | GC-12 (Złodziejski Zwiad): gold 1 → 0 | 92.5 → 🟡 ** 89.9** (`-2.6`) | 1.2% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_CAA-03_HERESY_PLUS1` | CAA-03 (Cień na Rynku): heresy 1 → 2 | 92.5 → 🟡 ** 89.2** (`-3.3`) | 1.2% | 5.7% | ⚪ STRATA/NEUTRALNY |