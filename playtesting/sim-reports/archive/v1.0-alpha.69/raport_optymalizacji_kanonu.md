# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.69 (Iteracja #3, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.68` (4P: `69.8 pkt`) → **Nowa Wersja:** `v1.0-alpha.69` (4P: `73.1 pkt`)
**Data:** 2026-08-24 07:51 | **Czas Trwania Iteracji:** 433.1s | **Zysk 4P:** `+3.3 pkt` | **Zysk Global:** `-0.7 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_SO-04_TARGET_HERESY_PLUS1` — **SO-04 (Publiczne Ostrzeżenie): target_heresy 0 → 1**
- **Opis Modyfikacji:** Karta `so-04` (Publiczne Ostrzeżenie): `target_heresy` → `1`
- **Wynik Kanonu 4P Balance:** 69.8 → 🟠 ** 73.1** (`⬆️ +3.3`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 74.0 → 74.3 (`⬆️ +0.3`) pkt
  - `4p-no-cienie`: 63.7 → 64.0 (`⬆️ +0.3`) pkt
  - `4p-no-kabala`: 64.3 → 75.1 (`⬆️ +10.8`) pkt
  - `4p-no-korona`: 82.1 → 87.4 (`⬆️ +5.3`) pkt
  - `4p-no-oficjum`: 64.9 pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 31.9 → 30.6 (`-1.3`) pkt
- **Tryb 4-osobowy (4p Avg):** 65.9 → 63.7 (`-2.2`) pkt
- **Tryb 5-osobowy (5p Avg):** 25.7 → 27.2 (`⬆️ +1.5`) pkt
- **Global Game Balance Score:** 41.2 → 🔴 ** 40.5** (`-0.7`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.82 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.3%` (norma: <30%)
  - **Autodafé / partię:** `1.55`
  - **Oskarżenia / partię:** `6.83`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-04_TARGET_HERESY_PLUS1` | SO-04 (Publiczne Ostrzeżenie): target_heresy 0 → 1 | 69.8 → 🟠 ** 73.1** (`⬆️ +3.3`) | 0.0% | 4.3% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-04_TARGET_HERESY_SET1` | SO-04 (Publiczne Ostrzeżenie): dodaj target_heresy = 1 | 69.8 → 🟠 ** 73.1** (`⬆️ +3.3`) | 0.0% | 4.3% | 🟢 ZYSK |
| #3 | `L3_GC-06_HERESY_MINUS1` | GC-06 (Szantaż): heresy 1 → 0 | 69.8 → 🟠 ** 72.5** (`⬆️ +2.7`) | 0.0% | 4.5% | 🟢 ZYSK |
| #4 | `L3_GC-03_HERESY_SET2` | GC-03 (Podrzucenie Księgi): dodaj heresy = 2 | 69.8 → 🟠 ** 72.1** (`⬆️ +2.3`) | 0.0% | 4.4% | 🟢 ZYSK |
| #5 | `L3_SO-04_COST_PLUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 2 | 69.8 → 🟠 ** 72.1** (`⬆️ +2.3`) | 0.0% | 4.6% | 🟢 ZYSK |
| #6 | `L3_SO-11_TARGET_HERESY_MINUS1` | SO-11 (Dekret Czystości Wiary): target_heresy 1 → 0 | 69.8 → 🟠 ** 71.9** (`⬆️ +2.1`) | 0.0% | 4.4% | 🟢 ZYSK |
| #7 | `L3_SO-04_HERESY_SET1` | SO-04 (Publiczne Ostrzeżenie): dodaj heresy = 1 | 69.8 → 🟠 ** 71.9** (`⬆️ +2.1`) | 0.0% | 4.5% | 🟢 ZYSK |
| #8 | `L3_SO-04_HERESY_PLUS1` | SO-04 (Publiczne Ostrzeżenie): heresy 0 → 1 | 69.8 → 🟠 ** 71.9** (`⬆️ +2.1`) | 0.0% | 4.5% | 🟢 ZYSK |
| #9 | `L3_SO-12_COST_PLUS1` | SO-12 (Straż Trybunalska): cost 1 → 2 | 69.8 → 🟠 ** 71.8** (`⬆️ +2.0`) | 0.0% | 4.7% | 🟢 ZYSK |
| #10 | `L3_CAA-05_TARGET_HERESY_PLUS2` | CAA-05 (Ukryty Kurier): target_heresy 2 → 4 (+2) | 69.8 → 🟠 ** 71.2** (`⬆️ +1.4`) | 0.0% | 4.5% | 🟢 ZYSK |
| #11 | `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 69.8 → 🟠 ** 70.9** (`⬆️ +1.1`) | 0.0% | 4.5% | 🟢 ZYSK |
| #12 | `L3_GC-02_GOLD_MINUS1` | GC-02 (Czarny Rynek): gold 2 → 1 | 69.8 → 🟠 ** 70.3** (`⬆️ +0.5`) | 0.0% | 4.4% | 🟢 ZYSK |
| #13 | `L3_GC-02_HERESY_SET2` | GC-02 (Czarny Rynek): dodaj heresy = 2 | 69.8 → 🟠 ** 70.1** (`⬆️ +0.3`) | 0.0% | 4.4% | 🟢 ZYSK |
| #14 | `L3_GC-02_COST_PLUS1` | GC-02 (Czarny Rynek): cost 0 → 1 | 69.8 → 🟠 ** 70.1** (`⬆️ +0.3`) | 0.0% | 4.5% | 🟢 ZYSK |
| #15 | `L3_GC-02_GOLD_PLUS1` | GC-02 (Czarny Rynek): gold 2 → 3 | 69.8 → 🟠 ** 70.1** (`⬆️ +0.3`) | 0.0% | 4.5% | 🟢 ZYSK |
| #16 | `L3_GC-02_HERESY_SET1` | GC-02 (Czarny Rynek): dodaj heresy = 1 | 69.8 → 🟠 ** 69.6** (`-0.2`) | 0.0% | 4.4% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_GC-02_HERESY_PLUS1` | GC-02 (Czarny Rynek): heresy 0 → 1 | 69.8 → 🟠 ** 69.6** (`-0.2`) | 0.0% | 4.4% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_SO-06_COST_MINUS1` | SO-06 (Areszt Trybunalski): cost 2 → 1 | 69.8 → 🟠 ** 71.3** (`⬆️ +1.5`) | 0.0% | 4.2% | 🟢 ZYSK |
| #19 | `L3_KT-03_COST_PLUS1` | KT-03 (Zakazana Wiedza): cost 0 → 1 | 69.8 → 🟠 ** 68.7** (`-1.1`) | 0.0% | 4.6% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_SO-12_TARGET_HERESY_SET2` | SO-12 (Straż Trybunalska): dodaj target_heresy = 2 | 69.8 → 🟠 ** 66.1** (`-3.7`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |