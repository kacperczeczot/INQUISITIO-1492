# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.67 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.66` (4P: `72.5 pkt`) → **Nowa Wersja:** `v1.0-alpha.67` (4P: `73.5 pkt`)
**Data:** 2026-08-24 07:26 | **Czas Trwania Iteracji:** 435.7s | **Zysk 4P:** `+1.0 pkt` | **Zysk Global:** `-3.9 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_KB-01_TARGET_HERESY_MINUS1` — **KB-01 (Rozkaz Dworu): target_heresy 1 → 0**
- **Opis Modyfikacji:** Karta `kb-01` (Rozkaz Dworu): `target_heresy` → `0`
- **Wynik Kanonu 4P Balance:** 72.5 → 🟠 ** 73.5** (`⬆️ +1.0`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 83.6 → 76.4 (`-7.2`) pkt
  - `4p-no-cienie`: 55.8 → 65.6 (`⬆️ +9.8`) pkt
  - `4p-no-kabala`: 69.2 → 67.7 (`-1.5`) pkt
  - `4p-no-korona`: 96.3 pkt
  - `4p-no-oficjum`: 57.8 → 61.3 (`⬆️ +3.5`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 32.5 → 31.9 (`-0.6`) pkt
- **Tryb 4-osobowy (4p Avg):** 72.7 → 61.3 (`-11.4`) pkt
- **Tryb 5-osobowy (5p Avg):** 2.8 → 3.2 (`⬆️ +0.4`) pkt
- **Global Game Balance Score:** 36.0 → 🔴 ** 32.1** (`-3.9`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.84 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `5.1%` (norma: <30%)
  - **Autodafé / partię:** `1.40`
  - **Oskarżenia / partię:** `6.88`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_KB-01_TARGET_HERESY_MINUS1` | KB-01 (Rozkaz Dworu): target_heresy 1 → 0 | 72.5 → 🟠 ** 73.5** (`⬆️ +1.0`) | 0.0% | 5.1% | 🌟 ZWYCIĘZCA |
| #2 | `L3_GC-08_TARGET_HERESY_MINUS1` | GC-08 (Zatrute Złoto): target_heresy 1 → 0 | 72.5 → 🟠 ** 73.4** (`⬆️ +0.9`) | 0.0% | 5.3% | 🟢 ZYSK |
| #3 | `L3_GC-07_COST_PLUS1` | GC-07 (Skrytobójstwo): cost 0 → 1 | 72.5 → 🟠 ** 73.4** (`⬆️ +0.9`) | 0.0% | 5.3% | 🟢 ZYSK |
| #4 | `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 1 → 2 | 72.5 → 🟠 ** 73.2** (`⬆️ +0.7`) | 0.0% | 5.3% | 🟢 ZYSK |
| #5 | `L3_KB-03_HERESY_PLUS1` | KB-03 (Plotka Dworska): heresy 1 → 2 | 72.5 → 🟠 ** 73.1** (`⬆️ +0.6`) | 0.0% | 5.0% | 🟢 ZYSK |
| #6 | `L3_KB-03_TARGET_HERESY_MINUS1` | KB-03 (Plotka Dworska): target_heresy 1 → 0 | 72.5 → 🟠 ** 72.9** (`⬆️ +0.4`) | 0.0% | 4.9% | 🟢 ZYSK |
| #7 | `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 72.5 → 🟠 ** 72.7** (`⬆️ +0.2`) | 0.0% | 5.3% | 🟢 ZYSK |
| #8 | `L3_KB-07_COST_MINUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 1 | 72.5 → 🟠 ** 72.2** (`-0.3`) | 0.0% | 4.7% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_KB-10_HERESY_MINUS1` | KB-10 (Pieczęć Korony): heresy 1 → 0 | 72.5 → 🟠 ** 71.7** (`-0.8`) | 0.0% | 5.3% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_GC-07_GOLD_SET2` | GC-07 (Skrytobójstwo): dodaj gold = 2 | 72.5 → 🟠 ** 72.8** (`⬆️ +0.3`) | 0.0% | 5.2% | 🟢 ZYSK |
| #11 | `L3_SO-01_TARGET_HERESY_PLUS1` | SO-01 (Patrol Familiariuszy): target_heresy 0 → 1 | 72.5 → 🟠 ** 67.9** (`-4.6`) | 0.0% | 5.2% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_SO-06_GOLD_SET3` | SO-06 (Areszt Trybunalski): dodaj gold = 3 | 72.5 → 🟠 ** 66.6** (`-5.9`) | 0.0% | 4.7% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_KB-07_COST_PLUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 3 | 72.5 → 🟠 ** 73.6** (`⬆️ +1.1`) | 0.0% | 5.4% | 🟢 ZYSK |
| #14 | `L3_KB-04_TARGET_HERESY_SET2` | KB-04 (Faworyt Dworu): dodaj target_heresy = 2 | 72.5 → 🟠 ** 72.9** (`⬆️ +0.4`) | 0.0% | 5.3% | 🟢 ZYSK |
| #15 | `L3_KB-04_TARGET_HERESY_SET1` | KB-04 (Faworyt Dworu): dodaj target_heresy = 1 | 72.5 → 🟠 ** 72.6** (`⬆️ +0.1`) | 0.0% | 5.3% | 🟢 ZYSK |
| #16 | `L3_KB-04_TARGET_HERESY_PLUS1` | KB-04 (Faworyt Dworu): target_heresy 0 → 1 | 72.5 → 🟠 ** 72.6** (`⬆️ +0.1`) | 0.0% | 5.3% | 🟢 ZYSK |
| #17 | `L3_CAA-12_TARGET_HERESY_PLUS1` | CAA-12 (Skrytka w Murach): target_heresy 0 → 1 | 72.5 → 🟠 ** 72.4** (`-0.1`) | 0.0% | 5.3% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_CAA-12_TARGET_HERESY_SET1` | CAA-12 (Skrytka w Murach): dodaj target_heresy = 1 | 72.5 → 🟠 ** 72.4** (`-0.1`) | 0.0% | 5.3% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_KB-07_GOLD_PLUS1` | KB-07 (Szantaż Pieczęcią): gold 0 → 1 | 72.5 → 🟠 ** 70.0** (`-2.5`) | 0.0% | 4.9% | ⚪ STRATA/NEUTRALNY |
| #20 | `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 7 → 6 | 72.5 → 🟠 ** 68.1** (`-4.4`) | 0.0% | 5.0% | ⚪ STRATA/NEUTRALNY |