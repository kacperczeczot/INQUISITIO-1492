# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.99.20 (Iteracja #2, Faza 1D)

**Wersja Poprzednia:** `v0.99.19` (4P: `73.1 pkt`) → **Nowa Wersja:** `v0.99.20` (4P: `73.5 pkt`)
**Data:** 2026-08-18 14:27 | **Czas Trwania Iteracji:** 651.7s | **Zysk 4P:** `+0.4 pkt` | **Zysk Global:** `-0.6 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_GC-08_HERESY_PLUS1` — **GC-08 (Zatrute Złoto): heresy 0 → 1**
- **Opis Modyfikacji:** Karta `gc-08` (Zatrute Złoto): `heresy` → `1`
- **Wynik Kanonu 4P Score:** 73.1 → 🟠 ** 73.5** (`⬆️ +0.4`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 70.6 pkt
  - `4p-no-cienie`: 69.0 → 70.8 (`⬆️ +1.8`) pkt
  - `4p-no-kabala`: 65.7 pkt
  - `4p-no-korona`: 81.5 → 82.3 (`⬆️ +0.8`) pkt
  - `4p-no-oficjum`: 78.5 → 78.3 (`-0.2`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 14.2 → 14.5 (`⬆️ +0.3`) pkt
- **Tryb 4-osobowy (4p Avg):** 73.4 → 74.2 (`⬆️ +0.8`) pkt
- **Tryb 5-osobowy (5p Avg):** 36.4 → 33.5 (`-2.9`) pkt
- **Global Game Balance Score:** 41.3 → 🔴 ** 40.7** (`-0.6`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.22 Er`
  - **Deadlocki (Limit Er):** `0.7%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.5%` (norma: <30%)
  - **Autodafé / partię:** `2.23`
  - **Oskarżenia / partię:** `3.89`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 0 → 1 | 73.1 → 🟠 ** 73.5** (`⬆️ +0.4`) | 0.7% | 1.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_GC-03_GOLD_PLUS1` | GC-03 (Podrzucenie Księgi): gold 0 → 1 | 73.1 → 🟠 ** 73.3** (`⬆️ +0.2`) | 0.7% | 1.5% | 🟢 ZYSK |
| #3 | `L1_MAX_ERAS_MINUS1` | Limit Er: 13 → 12 | 73.1 → 🟠 ** 71.1** (`-2.0`) | 2.1% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #4 | `L3_KT-12_COST_PLUS1` | KT-12 (Strażnik Archiwum): cost 0 → 1 | 🟠 ** 73.1** | 0.7% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #5 | `L3_KT-01_COST_MINUS1` | KT-01 (Rytuał Przejścia): cost 1 → 0 | 🟠 ** 73.1** | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #6 | `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 7 → 8 | 🟠 ** 73.1** | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #7 | `L2_CAA_ERA_MINUS1` | Cienie Era ścieżki: 1 → 0 | 🟠 ** 73.1** | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #8 | `L1_MAX_ERAS_PLUS1` | Limit Er: 13 → 14 | 🟠 ** 73.1** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #9 | `L2_CAA_ERA_PLUS1` | Cienie Era ścieżki: 1 → 2 | 🟠 ** 73.1** | 0.7% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 0 → 1 | 🟠 ** 73.1** | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_CAA-07_HERESY_PLUS1` | CAA-07 (Szantaż Bractwa): heresy 0 → 1 | 🟠 ** 73.1** | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 0 → 1 | 🟠 ** 73.1** | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_CAA-01_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 🟠 ** 73.1** | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_CAA-09_COST_PLUS1` | CAA-09 (Kurier Relikwii): cost 0 → 1 | 🟠 ** 73.1** | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_CAA-11_COST_PLUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 2 | 🟠 ** 73.1** | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_CAA-09_GOLD_PLUS1` | CAA-09 (Kurier Relikwii): gold 0 → 1 | 🟠 ** 73.1** | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_CAA-11_COST_MINUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 0 | 🟠 ** 73.1** | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_KT-03_GOLD_PLUS1` | KT-03 (Zakazana Wiedza): gold 0 → 1 | 73.1 → 🟠 ** 73.0** (`-0.1`) | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_KT-07_COST_MINUS1` | KT-07 (Archiwum Ukryte): cost 1 → 0 | 73.1 → 🟠 ** 73.0** (`-0.1`) | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_KT-11_COST_PLUS1` | KT-11 (Medytacja Sefirot): cost 1 → 2 | 73.1 → 🟠 ** 73.0** (`-0.1`) | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_GC-05_COST_PLUS1` | GC-05 (Fałszywy Świadek): cost 0 → 1 | 73.1 → 🟠 ** 73.0** (`-0.1`) | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_KT-03_HERESY_PLUS1` | KT-03 (Zakazana Wiedza): heresy 0 → 1 | 73.1 → 🟠 ** 72.7** (`-0.4`) | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_KT-06_HERESY_PLUS1` | KT-06 (Przesłuchanie Imienia): heresy 0 → 1 | 73.1 → 🟠 ** 72.4** (`-0.7`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_SO-02_GOLD_MINUS1` | SO-02 (Skarbiec Trybunału): gold 3 → 2 | 73.1 → 🟠 ** 73.0** (`-0.1`) | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |