[Strona główna](../../../../../README.md) > [v0.63](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.63 (Iteracja #5, Faza 1D)

**Wersja Poprzednia:** `v0.62` (4P: `93.4 pkt`) → **Nowa Wersja:** `v0.63` (4P: `93.9 pkt`)
**Data:** 2026-08-16 16:55 | **Czas Trwania Iteracji:** 296.3s | **Zysk 4P:** `+0.5 pkt` | **Zysk Global:** `-0.4 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_CAA-10_COST_PLUS1` — **CAA-10 (Echo Alhambry): cost 0 → 1**
- **Opis Modyfikacji:** Karta `caa-10` (Echo Alhambry): `cost` → `1`
- **Wynik Kanonu 4P Score:** 93.4 → 🟢 ** 93.9** (`⬆️ +0.5`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 92.2 → 91.2 (`-1.0`) pkt
  - `4p-no-cienie`: 89.7 pkt
  - `4p-no-kabala`: 99.1 → 99.5 (`⬆️ +0.4`) pkt
  - `4p-no-korona`: 93.6 → 94.8 (`⬆️ +1.2`) pkt
  - `4p-no-oficjum`: 92.5 → 94.4 (`⬆️ +1.9`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 67.8 → 67.3 (`-0.5`) pkt
- **Tryb 4-osobowy (4p Avg):** 90.1 → 90.9 (`⬆️ +0.8`) pkt
- **Tryb 5-osobowy (5p Avg):** 71.6 → 70.1 (`-1.5`) pkt
- **Global Game Balance Score:** 76.5 → 🟡 ** 76.1** (`-0.4`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.46 Er`
  - **Deadlocki (Limit Er):** `0.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `24.4%` (norma: <30%)
  - **Autodafé / partię:** `1.44`
  - **Oskarżenia / partię:** `3.06`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-10_COST_PLUS1` | CAA-10 (Echo Alhambry): cost 0 → 1 | 93.4 → 🟢 ** 93.9** (`⬆️ +0.5`) | 0.3% | 24.4% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 93.4 → 🟢 ** 93.7** (`⬆️ +0.3`) | 0.4% | 24.4% | 🟢 ZYSK |
| #3 | `L3_CAA-09_COST_PLUS1` | CAA-09 (Kurier Relikwii): cost 2 → 3 | 93.4 → 🟢 ** 93.7** (`⬆️ +0.3`) | 0.3% | 24.4% | 🟢 ZYSK |
| #4 | `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 93.4 → 🟢 ** 93.6** (`⬆️ +0.2`) | 0.4% | 24.4% | 🟢 ZYSK |
| #5 | `L3_CAA-05_COST_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 2 | 93.4 → 🟢 ** 93.6** (`⬆️ +0.2`) | 0.3% | 24.4% | 🟢 ZYSK |
| #6 | `L3_GC-07_HERESY_PLUS1` | GC-07 (Skrytobójstwo): heresy 0 → 1 | 93.4 → 🟢 ** 93.5** (`⬆️ +0.1`) | 0.3% | 24.4% | 🟢 ZYSK |
| #7 | `L3_GC-07_COST_PLUS1` | GC-07 (Skrytobójstwo): cost 2 → 3 | 93.4 → 🟢 ** 93.5** (`⬆️ +0.1`) | 0.3% | 24.4% | 🟢 ZYSK |
| #8 | `L3_KT-04_COST_PLUS1` | KT-04 (Zwierciadło Herezji): cost 0 → 1 | 93.4 → 🟢 ** 93.5** (`⬆️ +0.1`) | 0.4% | 24.4% | 🟢 ZYSK |
| #9 | `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 0 → 1 | 🟢 ** 93.4** | 0.3% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_GC-02_HERESY_MINUS1` | GC-02 (Czarny Rynek): heresy 1 → 0 | 🟢 ** 93.4** | 0.3% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #11 | `L4_SEA_ROUTE_ERA6` | Szlak Morski: Era 5 → Era 6 | 93.4 → 🟢 ** 93.3** (`-0.1`) | 0.3% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-04_GOLD_PLUS1` | CAA-04 (Fałszywy Trop): gold 1 → 2 | 93.4 → 🟢 ** 93.2** (`-0.2`) | 0.3% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_CAA-05_COST_MINUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 | 93.4 → 🟢 ** 93.2** (`-0.2`) | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_CAA-07_COST_MINUS1` | CAA-07 (Szantaż Bractwa): cost 1 → 0 | 93.4 → 🟢 ** 93.2** (`-0.2`) | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_CAA-05_GOLD_PLUS1` | CAA-05 (Ukryty Kurier): gold 0 → 1 | 93.4 → 🟢 ** 93.2** (`-0.2`) | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_CAA-09_COST_MINUS1` | CAA-09 (Kurier Relikwii): cost 2 → 1 | 93.4 → 🟢 ** 93.2** (`-0.2`) | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_GC-09_HERESY_PLUS1` | GC-09 (Lista Dłużników): heresy 0 → 1 | 93.4 → 🟢 ** 93.1** (`-0.3`) | 0.3% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_CAA-06_COST_PLUS1` | CAA-06 (Ucieczka z Lochów): cost 2 → 3 | 93.4 → 🟢 ** 93.0** (`-0.4`) | 0.3% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_KT-04_GOLD_PLUS1` | KT-04 (Zwierciadło Herezji): gold 0 → 1 | 93.4 → 🟢 ** 92.7** (`-0.7`) | 0.3% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_GC-03_HERESY_PLUS1` | GC-03 (Podrzucenie Księgi): heresy 0 → 1 | 93.4 → 🟢 ** 92.7** (`-0.7`) | 0.3% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_KB-03_HERESY_PLUS1` | KB-03 (Plotka Dworska): heresy 0 → 1 | 93.4 → 🟢 ** 92.5** (`-0.9`) | 0.3% | 24.2% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_SO-10_COST_PLUS1` | SO-10 (Oczyść Miasto): cost 5 → 6 | 93.4 → 🟢 ** 92.4** (`-1.0`) | 0.3% | 24.8% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_CAA-08_GOLD_PLUS1` | CAA-08 (Kaptur Nocy): gold 0 → 1 | 93.4 → 🟢 ** 92.3** (`-1.1`) | 0.3% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_CAA-07_GOLD_PLUS1` | CAA-07 (Szantaż Bractwa): gold 0 → 1 | 93.4 → 🟢 ** 92.1** (`-1.3`) | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |