# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.99.15 (Iteracja #2, Faza 1D)

**Wersja Poprzednia:** `v0.99.14` (4P: `68.6 pkt`) → **Nowa Wersja:** `v0.99.15` (4P: `69.3 pkt`)
**Data:** 2026-08-18 13:08 | **Czas Trwania Iteracji:** 659.0s | **Zysk 4P:** `+0.7 pkt` | **Zysk Global:** `+2.7 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_GC-08_COST_MINUS1` — **GC-08 (Zatrute Złoto): cost 2 → 1**
- **Opis Modyfikacji:** Karta `gc-08` (Zatrute Złoto): `cost` → `1`
- **Wynik Kanonu 4P Score:** 68.6 → 🟠 ** 69.3** (`⬆️ +0.7`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 71.8 pkt
  - `4p-no-cienie`: 63.7 → 65.9 (`⬆️ +2.2`) pkt
  - `4p-no-kabala`: 59.7 → 61.0 (`⬆️ +1.3`) pkt
  - `4p-no-korona`: 84.6 → 84.9 (`⬆️ +0.3`) pkt
  - `4p-no-oficjum`: 63.4 → 62.9 (`-0.5`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 14.3 → 14.2 (`-0.1`) pkt
- **Tryb 4-osobowy (4p Avg):** 63.2 → 71.5 (`⬆️ +8.3`) pkt
- **Tryb 5-osobowy (5p Avg):** 36.7 → 36.8 (`⬆️ +0.1`) pkt
- **Global Game Balance Score:** 38.1 → 🔴 ** 40.8** (`⬆️ +2.7`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.14 Er`
  - **Deadlocki (Limit Er):** `0.6%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.5%` (norma: <30%)
  - **Autodafé / partię:** `2.17`
  - **Oskarżenia / partię:** `3.80`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-04_COST_MINUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 0 | 68.6 → 🟠 ** 68.3** (`-0.3`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #2 | `L3_SO-04_GOLD_PLUS1` | SO-04 (Publiczne Ostrzeżenie): gold 0 → 1 | 68.6 → 🟠 ** 68.3** (`-0.3`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #3 | `L3_GC-08_COST_MINUS1` | GC-08 (Zatrute Złoto): cost 2 → 1 | 68.6 → 🟠 ** 69.3** (`⬆️ +0.7`) | 0.6% | 1.5% | 🌟 ZWYCIĘZCA |
| #4 | `L3_KB-05_HERESY_PLUS1` | KB-05 (List Żelazny): heresy 0 → 1 | 68.6 → 🟠 ** 68.7** (`⬆️ +0.1`) | 0.6% | 1.5% | 🟢 ZYSK |
| #5 | `L3_CAA-12_HERESY_MINUS1` | CAA-12 (Skrytka w Murach): heresy 1 → 0 | 68.6 → 🟠 ** 69.2** (`⬆️ +0.6`) | 0.7% | 1.5% | 🟢 ZYSK |
| #6 | `L3_GC-07_COST_PLUS1` | GC-07 (Skrytobójstwo): cost 2 → 3 | 68.6 → 🟠 ** 68.9** (`⬆️ +0.3`) | 0.6% | 1.5% | 🟢 ZYSK |
| #7 | `L3_SO-10_HERESY_MINUS1` | SO-10 (Oczyść Miasto): heresy 2 → 1 | 🟠 ** 68.6** | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 68.6 → 🟠 ** 68.7** (`⬆️ +0.1`) | 0.6% | 1.5% | 🟢 ZYSK |
| #9 | `L3_GC-01_TARGET_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): target_heresy 0 → 1 | 68.6 → 🟠 ** 69.9** (`⬆️ +1.3`) | 0.6% | 1.5% | 🟢 ZYSK |
| #10 | `L3_SO-03_TARGET_HERESY_PLUS1` | SO-03 (Podejrzenie): target_heresy 1 → 2 | 68.6 → 🟠 ** 69.6** (`⬆️ +1.0`) | 0.6% | 1.5% | 🟢 ZYSK |
| #11 | `L3_SO-09_TARGET_HERESY_PLUS1` | SO-09 (Świadek Koronny): target_heresy 0 → 1 | 68.6 → 🟠 ** 69.4** (`⬆️ +0.8`) | 0.6% | 1.5% | 🟢 ZYSK |
| #12 | `L3_SO-12_TARGET_HERESY_PLUS1` | SO-12 (Straż Trybunalska): target_heresy 0 → 1 | 68.6 → 🟠 ** 69.3** (`⬆️ +0.7`) | 0.6% | 1.5% | 🟢 ZYSK |
| #13 | `L3_GC-11_GOLD_PLUS1` | GC-11 (Fałszywe Świadectwo Cechu): gold 0 → 1 | 68.6 → 🟠 ** 69.3** (`⬆️ +0.7`) | 0.6% | 1.5% | 🟢 ZYSK |
| #14 | `L3_KT-05_COST_PLUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 2 | 68.6 → 🟠 ** 69.2** (`⬆️ +0.6`) | 0.6% | 1.5% | 🟢 ZYSK |
| #15 | `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 68.6 → 🟠 ** 68.9** (`⬆️ +0.3`) | 0.6% | 1.5% | 🟢 ZYSK |
| #16 | `L3_KT-03_GOLD_PLUS1` | KT-03 (Zakazana Wiedza): gold 0 → 1 | 68.6 → 🟠 ** 68.9** (`⬆️ +0.3`) | 0.6% | 1.5% | 🟢 ZYSK |
| #17 | `L3_KB-01_HERESY_MINUS1` | KB-01 (Rozkaz Dworu): heresy 1 → 0 | 68.6 → 🟠 ** 68.8** (`⬆️ +0.2`) | 0.6% | 1.6% | 🟢 ZYSK |
| #18 | `L3_GC-07_COST_MINUS1` | GC-07 (Skrytobójstwo): cost 2 → 1 | 68.6 → 🟠 ** 68.8** (`⬆️ +0.2`) | 0.6% | 1.5% | 🟢 ZYSK |
| #19 | `L3_SO-02_GOLD_MINUS1` | SO-02 (Skarbiec Trybunału): gold 3 → 2 | 68.6 → 🟠 ** 68.7** (`⬆️ +0.1`) | 0.6% | 1.5% | 🟢 ZYSK |
| #20 | `L3_SO-07_TARGET_HERESY_PLUS1` | SO-07 (Przesłuchanie Oficjum): target_heresy 0 → 1 | 68.6 → 🟠 ** 68.7** (`⬆️ +0.1`) | 0.6% | 1.5% | 🟢 ZYSK |
| #21 | `L3_SO-02_TARGET_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): target_heresy 1 → 2 | 68.6 → 🟠 ** 69.1** (`⬆️ +0.5`) | 0.5% | 1.5% | 🟢 ZYSK |
| #22 | `L3_KB-04_HERESY_PLUS1` | KB-04 (Faworyt Dworu): heresy 1 → 2 | 68.6 → 🟠 ** 66.4** (`-2.2`) | 0.4% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_CAA-03_HERESY_PLUS1` | CAA-03 (Cień na Rynku): heresy 1 → 2 | 68.6 → 🟠 ** 66.0** (`-2.6`) | 0.4% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_KB-10_TARGET_HERESY_PLUS1` | KB-10 (Pieczęć Korony): target_heresy 0 → 1 | 68.6 → 🟠 ** 68.4** (`-0.2`) | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |