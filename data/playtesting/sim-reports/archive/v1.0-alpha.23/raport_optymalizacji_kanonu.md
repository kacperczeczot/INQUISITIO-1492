# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.23 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.22` (4P: `77.0 pkt`) → **Nowa Wersja:** `v1.0-alpha.23` (4P: `77.5 pkt`)
**Data:** 2026-08-22 13:17 | **Czas Trwania Iteracji:** 516.0s | **Zysk 4P:** `+0.5 pkt` | **Zysk Global:** `+0.1 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_CAA-12_GOLD_PLUS1` — **CAA-12 (Skrytka w Murach): gold 3 → 4**
- **Opis Modyfikacji:** Karta `caa-12` (Skrytka w Murach): `gold` → `4`
- **Wynik Kanonu 4P Balance:** 77.0 → 🟡 ** 77.5** (`⬆️ +0.5`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 61.4 → 62.5 (`⬆️ +1.1`) pkt
  - `4p-no-cienie`: 93.7 pkt
  - `4p-no-kabala`: 66.2 → 66.0 (`-0.2`) pkt
  - `4p-no-korona`: 79.3 → 81.0 (`⬆️ +1.7`) pkt
  - `4p-no-oficjum`: 84.4 → 84.1 (`-0.3`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 25.4 → 25.0 (`-0.4`) pkt
- **Tryb 4-osobowy (4p Avg):** 77.8 → 78.3 (`⬆️ +0.5`) pkt
- **Tryb 5-osobowy (5p Avg):** 28.3 → 28.4 (`⬆️ +0.1`) pkt
- **Global Game Balance Score:** 43.8 → 🔴 ** 43.9** (`⬆️ +0.1`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.18 Er`
  - **Deadlocki (Limit Er):** `0.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.5%` (norma: <30%)
  - **Autodafé / partię:** `2.22`
  - **Oskarżenia / partię:** `4.20`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-12_GOLD_PLUS1` | CAA-12 (Skrytka w Murach): gold 3 → 4 | 77.0 → 🟡 ** 77.5** (`⬆️ +0.5`) | 0.3% | 1.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 0 → 1 | 77.0 → 🟡 ** 77.2** (`⬆️ +0.2`) | 0.3% | 1.5% | 🟢 ZYSK |
| #3 | `L3_CAA-02_GOLD_MINUS1` | CAA-02 (Złoto z Kryjówki): gold 3 → 2 | 77.0 → 🟡 ** 77.2** (`⬆️ +0.2`) | 0.3% | 1.5% | 🟢 ZYSK |
| #4 | `L3_GC-03_COST_PLUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 2 | 77.0 → 🟡 ** 76.4** (`-0.6`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #5 | `L3_GC-04_GOLD_PLUS1` | GC-04 (Informator): gold 0 → 1 | 77.0 → 🟡 ** 76.3** (`-0.7`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_GC-04_GOLD_SET1` | GC-04 (Informator): dodaj gold = 1 | 77.0 → 🟡 ** 76.3** (`-0.7`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_SO-01_GOLD_SET3` | SO-01 (Patrol Familiariuszy): dodaj gold = 3 | 77.0 → 🟡 ** 76.1** (`-0.9`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_SO-01_GOLD_SET2` | SO-01 (Patrol Familiariuszy): dodaj gold = 2 | 77.0 → 🟡 ** 76.1** (`-0.9`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_GC-04_COST_MINUS1` | GC-04 (Informator): cost 1 → 0 | 77.0 → 🟡 ** 76.0** (`-1.0`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_KB-04_HERESY_MINUS1` | KB-04 (Faworyt Dworu): heresy 1 → 0 | 77.0 → 🟠 ** 74.6** (`-2.4`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_SO-05_TARGET_HERESY_PLUS1` | SO-05 (Wezwanie do Trybunału): target_heresy 1 → 2 | 77.0 → 🟠 ** 74.3** (`-2.7`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_KB-11_GOLD_SET3` | KB-11 (Tajny Emisariusz): dodaj gold = 3 | 77.0 → 🟠 ** 66.1** (`-10.9`) | 0.2% | 1.2% | ⚪ STRATA/NEUTRALNY |