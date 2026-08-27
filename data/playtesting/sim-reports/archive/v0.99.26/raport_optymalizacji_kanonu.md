# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.99.26 (Iteracja #3, Faza 1D)

**Wersja Poprzednia:** `v0.99.25` (4P: `75.8 pkt`) → **Nowa Wersja:** `v0.99.26` (4P: `75.8 pkt`)
**Data:** 2026-08-18 16:44 | **Czas Trwania Iteracji:** 727.9s | **Zysk 4P:** `0.0 pkt` | **Zysk Global:** `+0.6 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L1_MAX_ERAS_PLUS1` — **Limit Er: 13 → 14**
- **Opis Modyfikacji:** Limit Er: offset +1 (nowy: 14)
- **Wynik Kanonu 4P Score:** 🟡 ** 75.8** pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 67.3 pkt
  - `4p-no-cienie`: 88.4 pkt
  - `4p-no-kabala`: 62.4 → 62.5 (`⬆️ +0.1`) pkt
  - `4p-no-korona`: 89.3 pkt
  - `4p-no-oficjum`: 71.4 pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 21.0 → 22.8 (`⬆️ +1.8`) pkt
- **Tryb 4-osobowy (4p Avg):** 77.2 pkt
- **Tryb 5-osobowy (5p Avg):** 38.4 pkt
- **Global Game Balance Score:** 45.5 → 🔴 ** 46.1** (`⬆️ +0.6`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.21 Er`
  - **Deadlocki (Limit Er):** `0.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.5%` (norma: <30%)
  - **Autodafé / partię:** `2.21`
  - **Oskarżenia / partię:** `4.16`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-09_GOLD_PLUS1` | GC-09 (Lista Dłużników): gold 0 → 1 | 75.8 → 🟡 ** 76.1** (`⬆️ +0.3`) | 0.5% | 1.5% | 🟢 ZYSK |
| #2 | `L3_KB-11_GOLD_MINUS1` | KB-11 (Tajny Emisariusz): gold 1 → 0 | 75.8 → 🟡 ** 75.9** (`⬆️ +0.1`) | 0.5% | 1.6% | 🟢 ZYSK |
| #3 | `L3_CAA-12_GOLD_MINUS1` | CAA-12 (Skrytka w Murach): gold 3 → 2 | 75.8 → 🟡 ** 75.9** (`⬆️ +0.1`) | 0.6% | 1.5% | 🟢 ZYSK |
| #4 | `L3_CAA-12_COST_PLUS1` | CAA-12 (Skrytka w Murach): cost 0 → 1 | 75.8 → 🟡 ** 75.9** (`⬆️ +0.1`) | 0.6% | 1.5% | 🟢 ZYSK |
| #5 | `L1_MAX_ERAS_PLUS1` | Limit Er: 13 → 14 | 🟡 ** 75.8** | 0.3% | 1.5% | 🌟 ZWYCIĘZCA |
| #6 | `L3_KT-11_COST_MINUS1` | KT-11 (Medytacja Sefirot): cost 1 → 0 | 🟡 ** 75.8** | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 🟡 ** 75.8** | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #8 | `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 7 → 8 | 🟡 ** 75.8** | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #9 | `L2_CAA_ERA_PLUS1` | Cienie Era ścieżki: 1 → 2 | 🟡 ** 75.8** | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #10 | `L2_CAA_ERA_MINUS1` | Cienie Era ścieżki: 1 → 0 | 🟡 ** 75.8** | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_CAA-01_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 🟡 ** 75.8** | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_KT-11_COST_PLUS1` | KT-11 (Medytacja Sefirot): cost 1 → 2 | 🟡 ** 75.8** | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_KT-08_COST_MINUS1` | KT-08 (Areszt Wiedzy): cost 1 → 0 | 🟡 ** 75.8** | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 0 → 1 | 🟡 ** 75.8** | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_CAA-07_HERESY_PLUS1` | CAA-07 (Szantaż Bractwa): heresy 0 → 1 | 🟡 ** 75.8** | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 0 → 1 | 🟡 ** 75.8** | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_CAA-09_GOLD_PLUS1` | CAA-09 (Kurier Relikwii): gold 0 → 1 | 🟡 ** 75.8** | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_CAA-10_COST_PLUS1` | CAA-10 (Echo Alhambry): cost 0 → 1 | 🟡 ** 75.8** | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 🟡 ** 75.8** | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_GC-07_COST_MINUS1` | GC-07 (Skrytobójstwo): cost 2 → 1 | 🟡 ** 75.8** | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_GC-12_COST_PLUS1` | GC-12 (Złodziejski Zwiad): cost 0 → 1 | 75.8 → 🟡 ** 75.7** (`-0.1`) | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_SO-02_GOLD_MINUS1` | SO-02 (Skarbiec Trybunału): gold 3 → 2 | 75.8 → 🟡 ** 75.7** (`-0.1`) | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 1 → 2 | 75.8 → 🟡 ** 75.3** (`-0.5`) | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_KT-05_HERESY_PLUS1` | KT-05 (Wskazówka Cyklu): heresy 1 → 2 | 75.8 → 🟡 ** 75.1** (`-0.7`) | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |