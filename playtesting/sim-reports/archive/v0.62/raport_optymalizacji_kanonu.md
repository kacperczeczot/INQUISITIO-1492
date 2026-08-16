# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.62 (Iteracja #4, Faza 1D)

**Wersja Poprzednia:** `v0.61` (4P: `92.1 pkt`) → **Nowa Wersja:** `v0.62` (4P: `93.4 pkt`)
**Data:** 2026-08-16 16:50 | **Czas Trwania Iteracji:** 296.1s | **Zysk 4P:** `+1.3 pkt` | **Zysk Global:** `+3.8 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_CAA-04_GOLD_PLUS1` — **CAA-04 (Fałszywy Trop): gold 0 → 1**
- **Opis Modyfikacji:** Karta `caa-04` (Fałszywy Trop): `gold` → `1`
- **Wynik Kanonu 4P Score:** 92.1 → 🟢 ** 93.4** (`⬆️ +1.3`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 93.3 → 92.2 (`-1.1`) pkt
  - `4p-no-cienie`: 89.7 pkt
  - `4p-no-kabala`: 98.3 → 99.1 (`⬆️ +0.8`) pkt
  - `4p-no-korona`: 91.1 → 93.6 (`⬆️ +2.5`) pkt
  - `4p-no-oficjum`: 88.1 → 92.5 (`⬆️ +4.4`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 68.4 → 67.8 (`-0.6`) pkt
- **Tryb 4-osobowy (4p Avg):** 87.7 → 90.1 (`⬆️ +2.4`) pkt
- **Tryb 5-osobowy (5p Avg):** 62.0 → 71.6 (`⬆️ +9.6`) pkt
- **Global Game Balance Score:** 72.7 → 🟡 ** 76.5** (`⬆️ +3.8`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.47 Er`
  - **Deadlocki (Limit Er):** `0.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `24.4%` (norma: <30%)
  - **Autodafé / partię:** `1.44`
  - **Oskarżenia / partię:** `3.06`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-04_GOLD_PLUS1` | CAA-04 (Fałszywy Trop): gold 0 → 1 | 92.1 → 🟢 ** 93.4** (`⬆️ +1.3`) | 0.3% | 24.4% | 🌟 ZWYCIĘZCA |
| #2 | `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 1 → 2 | 92.1 → 🟢 ** 92.8** (`⬆️ +0.7`) | 0.3% | 24.5% | 🟢 ZYSK |
| #3 | `L3_CAA-05_COST_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 2 | 92.1 → 🟢 ** 92.4** (`⬆️ +0.3`) | 0.3% | 24.5% | 🟢 ZYSK |
| #4 | `L3_SO-09_COST_PLUS1` | SO-09 (Świadek Koronny): cost 2 → 3 | 92.1 → 🟢 ** 92.3** (`⬆️ +0.2`) | 0.3% | 24.9% | 🟢 ZYSK |
| #5 | `L3_CAA-07_COST_MINUS1` | CAA-07 (Szantaż Bractwa): cost 1 → 0 | 92.1 → 🟢 ** 92.2** (`⬆️ +0.1`) | 0.3% | 24.4% | 🟢 ZYSK |
| #6 | `L3_GC-07_HERESY_PLUS1` | GC-07 (Skrytobójstwo): heresy 0 → 1 | 92.1 → 🟢 ** 92.2** (`⬆️ +0.1`) | 0.3% | 24.4% | 🟢 ZYSK |
| #7 | `L3_CAA-08_GOLD_PLUS1` | CAA-08 (Kaptur Nocy): gold 0 → 1 | 🟢 ** 92.1** | 0.3% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_CAA-09_COST_MINUS1` | CAA-09 (Kurier Relikwii): cost 2 → 1 | 🟢 ** 92.1** | 0.3% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_CAA-07_GOLD_PLUS1` | CAA-07 (Szantaż Bractwa): gold 0 → 1 | 🟢 ** 92.1** | 0.3% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_CAA-03_GOLD_PLUS1` | CAA-03 (Cień na Rynku): gold 0 → 1 | 🟢 ** 92.1** | 0.3% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_GC-04_HERESY_PLUS1` | GC-04 (Informator): heresy 1 → 2 | 92.1 → 🟢 ** 91.8** (`-0.3`) | 0.3% | 24.3% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_KT-04_GOLD_PLUS1` | KT-04 (Zwierciadło Herezji): gold 0 → 1 | 92.1 → 🟢 ** 91.8** (`-0.3`) | 0.3% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_GC-06_HERESY_PLUS1` | GC-06 (Szantaż): heresy 0 → 1 | 92.1 → 🟢 ** 91.8** (`-0.3`) | 0.4% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_SO-03_COST_PLUS1` | SO-03 (Podejrzenie): cost 2 → 3 | 92.1 → 🟢 ** 91.7** (`-0.4`) | 0.3% | 24.8% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_SO-02_GOLD_PLUS1` | SO-02 (Skarbiec Trybunału): gold 2 → 3 | 92.1 → 🟢 ** 91.5** (`-0.6`) | 0.3% | 24.0% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_SO-06_GOLD_PLUS1` | SO-06 (Areszt Trybunalski): gold 0 → 1 | 92.1 → 🟢 ** 91.4** (`-0.7`) | 0.3% | 23.8% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_SO-10_COST_PLUS1` | SO-10 (Oczyść Miasto): cost 5 → 6 | 92.1 → 🟢 ** 91.4** (`-0.7`) | 0.3% | 24.8% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_CAA-02_GOLD_PLUS1` | CAA-02 (Złoto z Kryjówki): gold 2 → 3 | 92.1 → 🟢 ** 91.3** (`-0.8`) | 0.3% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_CAA-06_HERESY_MINUS1` | CAA-06 (Ucieczka z Lochów): heresy 1 → 0 | 92.1 → 🟢 ** 91.3** (`-0.8`) | 0.4% | 24.5% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_CAA-08_HERESY_MINUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 0 | 92.1 → 🟢 ** 91.2** (`-0.9`) | 0.4% | 24.5% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_KT-04_TARGET_HERESY_MINUS1` | KT-04 (Zwierciadło Herezji): target_heresy 1 → 0 | 92.1 → 🟢 ** 91.1** (`-1.0`) | 0.3% | 24.6% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_SO-04_GOLD_PLUS1` | SO-04 (Publiczne Ostrzeżenie): gold 0 → 1 | 92.1 → 🟢 ** 90.6** (`-1.5`) | 0.4% | 23.8% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_GC-02_COST_MINUS1` | GC-02 (Czarny Rynek): cost 2 → 1 | 92.1 → 🟢 ** 90.1** (`-2.0`) | 0.3% | 23.0% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_KT-08_TARGET_HERESY_PLUS1` | KT-08 (Areszt Wiedzy): target_heresy 0 → 1 | 92.1 → 🟡 ** 88.4** (`-3.7`) | 0.2% | 24.1% | ⚪ STRATA/NEUTRALNY |