# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.61 (Iteracja #3, Faza 1D)

**Wersja Poprzednia:** `v0.60` (4P: `89.8 pkt`) → **Nowa Wersja:** `v0.61` (4P: `92.1 pkt`)
**Data:** 2026-08-16 16:45 | **Czas Trwania Iteracji:** 303.5s | **Zysk 4P:** `+2.3 pkt` | **Zysk Global:** `+1.4 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_GC-10_HERESY_MINUS1` — **GC-10 (Upadek Domu): heresy 2 → 1**
- **Opis Modyfikacji:** Karta `gc-10` (Upadek Domu): `heresy` → `1`
- **Wynik Kanonu 4P Score:** 89.8 → 🟢 ** 92.1** (`⬆️ +2.3`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 93.3 pkt
  - `4p-no-cienie`: 89.6 → 89.7 (`⬆️ +0.1`) pkt
  - `4p-no-kabala`: 90.7 → 98.3 (`⬆️ +7.6`) pkt
  - `4p-no-korona`: 83.8 → 91.1 (`⬆️ +7.3`) pkt
  - `4p-no-oficjum`: 91.4 → 88.1 (`-3.3`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 74.5 → 68.4 (`-6.1`) pkt
- **Tryb 4-osobowy (4p Avg):** 87.7 pkt
- **Tryb 5-osobowy (5p Avg):** 51.8 → 62.0 (`⬆️ +10.2`) pkt
- **Global Game Balance Score:** 71.3 → 🟠 ** 72.7** (`⬆️ +1.4`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.46 Er`
  - **Deadlocki (Limit Er):** `0.4%` (norma: <5%)
  - **Pas Biedy (Złoto):** `24.4%` (norma: <30%)
  - **Autodafé / partię:** `1.44`
  - **Oskarżenia / partię:** `3.06`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-10_HERESY_MINUS1` | GC-10 (Upadek Domu): heresy 2 → 1 | 89.8 → 🟢 ** 92.1** (`⬆️ +2.3`) | 0.4% | 24.4% | 🌟 ZWYCIĘZCA |
| #2 | `L3_GC-07_GOLD_PLUS1` | GC-07 (Skrytobójstwo): gold 0 → 1 | 89.8 → 🟢 ** 91.9** (`⬆️ +2.1`) | 0.2% | 24.1% | 🟢 ZYSK |
| #3 | `L3_CAA-06_HERESY_MINUS1` | CAA-06 (Ucieczka z Lochów): heresy 1 → 0 | 89.8 → 🟢 ** 91.5** (`⬆️ +1.7`) | 0.3% | 24.4% | 🟢 ZYSK |
| #4 | `L3_SO-08_TARGET_HERESY_MINUS1` | SO-08 (Nasłanie Inkwizytora): target_heresy 1 → 0 | 89.8 → 🟢 ** 90.3** (`⬆️ +0.5`) | 0.3% | 24.6% | 🟢 ZYSK |
| #5 | `L3_GC-07_COST_MINUS1` | GC-07 (Skrytobójstwo): cost 2 → 1 | 89.8 → 🟢 ** 90.3** (`⬆️ +0.5`) | 0.3% | 23.8% | 🟢 ZYSK |
| #6 | `L3_SO-02_GOLD_MINUS1` | SO-02 (Skarbiec Trybunału): gold 2 → 1 | 89.8 → 🟢 ** 90.2** (`⬆️ +0.4`) | 0.3% | 25.0% | 🟢 ZYSK |
| #7 | `L3_KT-06_COST_PLUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 3 | 89.8 → 🟢 ** 90.2** (`⬆️ +0.4`) | 0.3% | 24.0% | 🟢 ZYSK |
| #8 | `L3_CAA-08_GOLD_PLUS1` | CAA-08 (Kaptur Nocy): gold 0 → 1 | 89.8 → 🟡 ** 89.9** (`⬆️ +0.1`) | 0.2% | 24.3% | 🟢 ZYSK |
| #9 | `L3_SO-03_HERESY_PLUS1` | SO-03 (Podejrzenie): heresy 0 → 1 | 89.8 → 🟡 ** 89.9** (`⬆️ +0.1`) | 0.2% | 24.2% | 🟢 ZYSK |
| #10 | `L3_CAA-02_GOLD_PLUS1` | CAA-02 (Złoto z Kryjówki): gold 2 → 3 | 🟡 ** 89.8** | 0.2% | 24.3% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_GC-02_GOLD_PLUS1` | GC-02 (Czarny Rynek): gold 2 → 3 | 🟡 ** 89.8** | 0.3% | 24.2% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-07_COST_MINUS1` | CAA-07 (Szantaż Bractwa): cost 1 → 0 | 89.8 → 🟡 ** 89.5** (`-0.3`) | 0.2% | 24.3% | ⚪ STRATA/NEUTRALNY |
| #13 | `L2_KB_ERA_MINUS1` | Korona Era: 4 → 3 | 89.8 → 🟡 ** 89.3** (`-0.5`) | 0.3% | 24.3% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_CAA-07_GOLD_PLUS1` | CAA-07 (Szantaż Bractwa): gold 0 → 1 | 89.8 → 🟡 ** 89.3** (`-0.5`) | 0.2% | 24.3% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_SO-03_COST_PLUS1` | SO-03 (Podejrzenie): cost 2 → 3 | 89.8 → 🟡 ** 89.2** (`-0.6`) | 0.3% | 24.7% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_CAA-01_GOLD_PLUS1` | CAA-01 (Przejście Podziemiami): gold 1 → 2 | 89.8 → 🟡 ** 89.0** (`-0.8`) | 0.3% | 24.2% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 1 → 2 | 89.8 → 🟡 ** 88.9** (`-0.9`) | 0.2% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_KT-04_TARGET_HERESY_MINUS1` | KT-04 (Zwierciadło Herezji): target_heresy 1 → 0 | 89.8 → 🟡 ** 88.9** (`-0.9`) | 0.3% | 24.5% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_SO-04_COST_MINUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 0 | 89.8 → 🟡 ** 88.5** (`-1.3`) | 0.3% | 23.7% | ⚪ STRATA/NEUTRALNY |
| #20 | `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–8 → 3–9 | 89.8 → 🟡 ** 88.5** (`-1.3`) | 0.2% | 24.2% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_SO-04_GOLD_PLUS1` | SO-04 (Publiczne Ostrzeżenie): gold 0 → 1 | 89.8 → 🟡 ** 88.3** (`-1.5`) | 0.3% | 23.7% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_SO-09_COST_PLUS1` | SO-09 (Świadek Koronny): cost 2 → 3 | 89.8 → 🟡 ** 87.7** (`-2.1`) | 0.3% | 24.8% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_KB-03_TARGET_HERESY_MINUS1` | KB-03 (Plotka Dworska): target_heresy 1 → 0 | 89.8 → 🟡 ** 87.5** (`-2.3`) | 0.3% | 24.3% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_SO-03_COST_MINUS1` | SO-03 (Podejrzenie): cost 2 → 1 | 89.8 → 🟡 ** 87.3** (`-2.5`) | 0.3% | 23.7% | ⚪ STRATA/NEUTRALNY |