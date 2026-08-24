# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.79 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.78` (4P: `83.2 pkt`) → **Nowa Wersja:** `v1.0-alpha.79` (4P: `85.3 pkt`)
**Data:** 2026-08-24 20:27 | **Czas Trwania Iteracji:** 669.0s | **Zysk 4P:** `+2.1 pkt` | **Zysk Global:** `+2.5 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_KT-07_HERESY_MINUS1` — **KT-07 (Archiwum Ukryte): heresy 1 → 0**
- **Opis Modyfikacji:** Karta `kt-07` (Archiwum Ukryte): `heresy` → `0`
- **Wynik Kanonu 4P Balance:** 83.2 → 🟡 ** 85.3** (`⬆️ +2.1`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 91.1 → 91.4 (`⬆️ +0.3`) pkt
  - `4p-no-cienie`: 74.5 → 80.8 (`⬆️ +6.3`) pkt
  - `4p-no-kabala`: 93.0 pkt
  - `4p-no-korona`: 85.5 → 88.5 (`⬆️ +3.0`) pkt
  - `4p-no-oficjum`: 71.8 → 72.9 (`⬆️ +1.1`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 29.1 → 31.0 (`⬆️ +1.9`) pkt
- **Tryb 4-osobowy (4p Avg):** 79.1 → 84.5 (`⬆️ +5.4`) pkt
- **Tryb 5-osobowy (5p Avg):** 16.3 → 16.6 (`⬆️ +0.3`) pkt
- **Global Game Balance Score:** 41.5 → 🔴 ** 44.0** (`⬆️ +2.5`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.78 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.2%` (norma: <30%)
  - **Autodafé / partię:** `1.52`
  - **Oskarżenia / partię:** `6.89`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_KT-07_HERESY_MINUS1` | KT-07 (Archiwum Ukryte): heresy 1 → 0 | 83.2 → 🟡 ** 85.3** (`⬆️ +2.1`) | 0.0% | 4.2% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KT-03_HERESY_MINUS1` | KT-03 (Zakazana Wiedza): heresy 2 → 1 | 83.2 → 🟡 ** 85.0** (`⬆️ +1.8`) | 0.0% | 4.3% | 🟢 ZYSK |
| #3 | `L3_KT-12_COST_PLUS1` | KT-12 (Strażnik Archiwum): cost 0 → 1 | 83.2 → 🟡 ** 84.3** (`⬆️ +1.1`) | 0.0% | 4.7% | 🟢 ZYSK |
| #4 | `L3_GC-09_GOLD_SET2` | GC-09 (Lista Dłużników): dodaj gold = 2 | 83.2 → 🟡 ** 83.8** (`⬆️ +0.6`) | 0.0% | 4.2% | 🟢 ZYSK |
| #5 | `L3_GC-09_GOLD_SET3` | GC-09 (Lista Dłużników): dodaj gold = 3 | 83.2 → 🟡 ** 83.8** (`⬆️ +0.6`) | 0.0% | 4.2% | 🟢 ZYSK |
| #6 | `L3_KB-10_GOLD_SET3` | KB-10 (Pieczęć Korony): dodaj gold = 3 | 83.2 → 🟡 ** 83.5** (`⬆️ +0.3`) | 0.0% | 4.2% | 🟢 ZYSK |
| #7 | `L3_GC-02_TARGET_HERESY_PLUS1` | GC-02 (Czarny Rynek): target_heresy 0 → 1 | 83.2 → 🟡 ** 83.4** (`⬆️ +0.2`) | 0.0% | 4.2% | 🟢 ZYSK |
| #8 | `L3_GC-02_TARGET_HERESY_SET1` | GC-02 (Czarny Rynek): dodaj target_heresy = 1 | 83.2 → 🟡 ** 83.4** (`⬆️ +0.2`) | 0.0% | 4.2% | 🟢 ZYSK |
| #9 | `L3_GC-09_GOLD_SET1` | GC-09 (Lista Dłużników): dodaj gold = 1 | 83.2 → 🟡 ** 83.3** (`⬆️ +0.1`) | 0.0% | 4.2% | 🟢 ZYSK |
| #10 | `L3_GC-09_GOLD_PLUS1` | GC-09 (Lista Dłużników): gold 0 → 1 | 83.2 → 🟡 ** 83.3** (`⬆️ +0.1`) | 0.0% | 4.2% | 🟢 ZYSK |
| #11 | `L3_KB-04_COST_MINUS1` | KB-04 (Faworyt Dworu): cost 2 → 1 | 🟡 ** 83.2** | 0.0% | 3.7% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_KB-10_TARGET_HERESY_PLUS1` | KB-10 (Pieczęć Korony): target_heresy 0 → 1 | 83.2 → 🟡 ** 83.1** (`-0.1`) | 0.0% | 4.3% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_KB-10_TARGET_HERESY_SET1` | KB-10 (Pieczęć Korony): dodaj target_heresy = 1 | 83.2 → 🟡 ** 83.1** (`-0.1`) | 0.0% | 4.3% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_GC-09_COST_PLUS1` | GC-09 (Lista Dłużników): cost 1 → 2 | 83.2 → 🟡 ** 82.9** (`-0.3`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_KB-10_TARGET_HERESY_SET2` | KB-10 (Pieczęć Korony): dodaj target_heresy = 2 | 83.2 → 🟡 ** 82.4** (`-0.8`) | 0.0% | 4.3% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_KB-08_GOLD_SET2` | KB-08 (Przekupstwo Sędziego): dodaj gold = 2 | 83.2 → 🟡 ** 82.0** (`-1.2`) | 0.0% | 4.0% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_KB-06_COST_PLUS1` | KB-06 (Areszt Królewski): cost 2 → 3 | 83.2 → 🟡 ** 82.0** (`-1.2`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_KB-07_COST_PLUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 3 | 83.2 → 🟡 ** 81.4** (`-1.8`) | 0.0% | 4.3% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_KT-08_GOLD_PLUS1` | KT-08 (Areszt Wiedzy): gold 0 → 1 | 83.2 → 🟡 ** 80.8** (`-2.4`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_KT-08_GOLD_SET1` | KT-08 (Areszt Wiedzy): dodaj gold = 1 | 83.2 → 🟡 ** 80.8** (`-2.4`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |