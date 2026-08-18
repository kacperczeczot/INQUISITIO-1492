# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.99.24 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v0.99.23` (4P: `75.5 pkt`) → **Nowa Wersja:** `v0.99.24` (4P: `76.2 pkt`)
**Data:** 2026-08-18 16:19 | **Czas Trwania Iteracji:** 780.9s | **Zysk 4P:** `+0.7 pkt` | **Zysk Global:** `+0.5 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_GC-04_TARGET_HERESY_PLUS1` — **GC-04 (Informator): target_heresy 0 → 1**
- **Opis Modyfikacji:** Karta `gc-04` (Informator): `target_heresy` → `1`
- **Wynik Kanonu 4P Score:** 75.5 → 🟡 ** 76.2** (`⬆️ +0.7`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 67.0 pkt
  - `4p-no-cienie`: 82.7 → 89.5 (`⬆️ +6.8`) pkt
  - `4p-no-kabala`: 65.7 → 61.9 (`-3.8`) pkt
  - `4p-no-korona`: 86.7 → 89.3 (`⬆️ +2.6`) pkt
  - `4p-no-oficjum`: 75.4 → 73.1 (`-2.3`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 21.2 pkt
- **Tryb 4-osobowy (4p Avg):** 76.5 → 77.3 (`⬆️ +0.8`) pkt
- **Tryb 5-osobowy (5p Avg):** 37.1 → 37.6 (`⬆️ +0.5`) pkt
- **Global Game Balance Score:** 44.9 → 🔴 ** 45.4** (`⬆️ +0.5`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.23 Er`
  - **Deadlocki (Limit Er):** `0.6%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.5%` (norma: <30%)
  - **Autodafé / partię:** `2.23`
  - **Oskarżenia / partię:** `4.09`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-04_TARGET_HERESY_PLUS1` | GC-04 (Informator): target_heresy 0 → 1 | 75.5 → 🟡 ** 76.2** (`⬆️ +0.7`) | 0.6% | 1.5% | 🌟 ZWYCIĘZCA |
| #2 | `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 7 → 8 | 🟡 ** 75.5** | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #3 | `L1_MAX_ERAS_PLUS1` | Limit Er: 13 → 14 | 🟡 ** 75.5** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #4 | `L3_GC-05_COST_PLUS1` | GC-05 (Fałszywy Świadek): cost 0 → 1 | 🟡 ** 75.5** | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #5 | `L2_CAA_ERA_MINUS1` | Cienie Era ścieżki: 1 → 0 | 🟡 ** 75.5** | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #6 | `L2_CAA_ERA_PLUS1` | Cienie Era ścieżki: 1 → 2 | 🟡 ** 75.5** | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_SO-01_TARGET_HERESY_PLUS1` | SO-01 (Patrol Familiariuszy): target_heresy 0 → 1 | 🟡 ** 75.5** | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_GC-03_GOLD_PLUS1` | GC-03 (Podrzucenie Księgi): gold 0 → 1 | 75.5 → 🟡 ** 75.4** (`-0.1`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 1 → 2 | 75.5 → 🟡 ** 75.4** (`-0.1`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_KT-11_COST_MINUS1` | KT-11 (Medytacja Sefirot): cost 1 → 0 | 75.5 → 🟡 ** 75.4** (`-0.1`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_KT-03_GOLD_PLUS1` | KT-03 (Zakazana Wiedza): gold 0 → 1 | 75.5 → 🟡 ** 75.4** (`-0.1`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 75.5 → 🟡 ** 75.4** (`-0.1`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_GC-03_COST_MINUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 0 | 75.5 → 🟡 ** 75.4** (`-0.1`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_SO-02_GOLD_MINUS1` | SO-02 (Skarbiec Trybunału): gold 3 → 2 | 75.5 → 🟡 ** 75.4** (`-0.1`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_CAA-12_GOLD_MINUS1` | CAA-12 (Skrytka w Murach): gold 3 → 2 | 75.5 → 🟡 ** 75.4** (`-0.1`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_CAA-12_COST_PLUS1` | CAA-12 (Skrytka w Murach): cost 0 → 1 | 75.5 → 🟡 ** 75.4** (`-0.1`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 75.5 → 🟡 ** 75.3** (`-0.2`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_CAA-02_GOLD_MINUS1` | CAA-02 (Złoto z Kryjówki): gold 3 → 2 | 75.5 → 🟡 ** 75.3** (`-0.2`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 0 → 1 | 75.5 → 🟡 ** 75.3** (`-0.2`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_KB-11_GOLD_MINUS1` | KB-11 (Tajny Emisariusz): gold 1 → 0 | 75.5 → 🟡 ** 75.2** (`-0.3`) | 0.6% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_GC-03_TARGET_HERESY_PLUS1` | GC-03 (Podrzucenie Księgi): target_heresy 1 → 2 | 75.5 → 🟡 ** 75.2** (`-0.3`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 2 → 3 | 75.5 → 🟡 ** 75.0** (`-0.5`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_GC-07_COST_MINUS1` | GC-07 (Skrytobójstwo): cost 2 → 1 | 75.5 → 🟡 ** 75.0** (`-0.5`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_KB-04_TARGET_HERESY_PLUS1` | KB-04 (Faworyt Dworu): target_heresy 0 → 1 | 75.5 → 🟠 ** 73.4** (`-2.1`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |