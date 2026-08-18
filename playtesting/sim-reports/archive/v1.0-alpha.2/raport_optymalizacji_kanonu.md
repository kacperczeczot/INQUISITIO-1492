# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.2 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.1` (4P: `74.8 pkt`) → **Nowa Wersja:** `v1.0-alpha.2` (4P: `75.2 pkt`)
**Data:** 2026-08-18 23:14 | **Czas Trwania Iteracji:** 230.2s | **Zysk 4P:** `+0.4 pkt` | **Zysk Global:** `+0.9 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_KB-11_GOLD_MINUS1` — **KB-11 (Tajny Emisariusz): gold 1 → 0**
- **Opis Modyfikacji:** Karta `kb-11` (Tajny Emisariusz): `gold` → `0`
- **Wynik Kanonu 4P Score:** 74.8 → 🟡 ** 75.2** (`⬆️ +0.4`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 53.2 → 54.5 (`⬆️ +1.3`) pkt
  - `4p-no-cienie`: 89.9 → 87.9 (`-2.0`) pkt
  - `4p-no-kabala`: 65.7 pkt
  - `4p-no-korona`: 91.2 pkt
  - `4p-no-oficjum`: 74.0 → 76.8 (`⬆️ +2.8`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 15.1 → 15.0 (`-0.1`) pkt
- **Tryb 4-osobowy (4p Avg):** 75.0 → 75.5 (`⬆️ +0.5`) pkt
- **Tryb 5-osobowy (5p Avg):** 38.4 → 40.5 (`⬆️ +2.1`) pkt
- **Global Game Balance Score:** 42.8 → 🔴 ** 43.7** (`⬆️ +0.9`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.18 Er`
  - **Deadlocki (Limit Er):** `2.7%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.6%` (norma: <30%)
  - **Autodafé / partię:** `2.20`
  - **Oskarżenia / partię:** `4.11`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_KB-11_GOLD_MINUS1` | KB-11 (Tajny Emisariusz): gold 1 → 0 | 74.8 → 🟡 ** 75.2** (`⬆️ +0.4`) | 2.7% | 1.6% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KB-03_GOLD_PLUS1` | KB-03 (Plotka Dworska): gold 0 → 1 | 74.8 → 🟡 ** 75.1** (`⬆️ +0.3`) | 2.7% | 1.6% | 🟢 ZYSK |
| #3 | `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 74.8 → 🟡 ** 75.1** (`⬆️ +0.3`) | 2.7% | 1.5% | 🟢 ZYSK |
| #4 | `L3_CAA-12_COST_PLUS1` | CAA-12 (Skrytka w Murach): cost 0 → 1 | 🟠 ** 74.8** | 2.8% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #5 | `L3_CAA-12_GOLD_MINUS1` | CAA-12 (Skrytka w Murach): gold 3 → 2 | 🟠 ** 74.8** | 2.8% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_GC-12_COST_PLUS1` | GC-12 (Złodziejski Zwiad): cost 0 → 1 | 🟠 ** 74.8** | 2.7% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_KT-11_COST_MINUS1` | KT-11 (Medytacja Sefirot): cost 1 → 0 | 74.8 → 🟠 ** 74.9** (`⬆️ +0.1`) | 2.7% | 1.5% | 🟢 ZYSK |
| #8 | `L2_CAA_ERA_PLUS1` | Cienie Era ścieżki: 1 → 2 | 🟠 ** 74.8** | 2.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_GC-09_GOLD_PLUS1` | GC-09 (Lista Dłużników): gold 0 → 1 | 🟠 ** 74.8** | 2.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #10 | `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 7 → 8 | 🟠 ** 74.8** | 2.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #11 | `L2_CAA_ERA_MINUS1` | Cienie Era ścieżki: 1 → 0 | 🟠 ** 74.8** | 2.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 0 → 1 | 🟠 ** 74.8** | 2.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_CAA-07_HERESY_PLUS1` | CAA-07 (Szantaż Bractwa): heresy 0 → 1 | 🟠 ** 74.8** | 2.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_CAA-10_COST_PLUS1` | CAA-10 (Echo Alhambry): cost 0 → 1 | 🟠 ** 74.8** | 2.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_CAA-09_GOLD_PLUS1` | CAA-09 (Kurier Relikwii): gold 0 → 1 | 🟠 ** 74.8** | 2.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_CAA-01_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 🟠 ** 74.8** | 2.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 0 → 1 | 🟠 ** 74.8** | 2.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_CAA-09_COST_PLUS1` | CAA-09 (Kurier Relikwii): cost 0 → 1 | 🟠 ** 74.8** | 2.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_CAA-11_COST_PLUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 2 | 🟠 ** 74.8** | 2.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_CAA-11_COST_MINUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 0 | 🟠 ** 74.8** | 2.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_KT-11_COST_PLUS1` | KT-11 (Medytacja Sefirot): cost 1 → 2 | 74.8 → 🟠 ** 74.7** (`-0.1`) | 2.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_GC-03_COST_MINUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 0 | 74.8 → 🟠 ** 74.7** (`-0.1`) | 2.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_KT-07_COST_PLUS1` | KT-07 (Archiwum Ukryte): cost 1 → 2 | 74.8 → 🟠 ** 74.4** (`-0.4`) | 2.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_KT-05_HERESY_PLUS1` | KT-05 (Wskazówka Cyklu): heresy 1 → 2 | 74.8 → 🟠 ** 74.6** (`-0.2`) | 2.6% | 1.5% | ⚪ STRATA/NEUTRALNY |