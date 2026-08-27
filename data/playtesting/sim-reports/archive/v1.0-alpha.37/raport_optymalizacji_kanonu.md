# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.37 (Iteracja #2, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.36` (4P: `62.0 pkt`) → **Nowa Wersja:** `v1.0-alpha.37` (4P: `65.7 pkt`)
**Data:** 2026-08-23 03:59 | **Czas Trwania Iteracji:** 614.6s | **Zysk 4P:** `+3.7 pkt` | **Zysk Global:** `-1.1 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_CAA-07_GOLD_SET3` — **CAA-07 (Szantaż Bractwa): dodaj gold = 3**
- **Opis Modyfikacji:** Karta `caa-07` (Szantaż Bractwa): `gold` → `3`
- **Wynik Kanonu 4P Balance:** 62.0 → 🟠 ** 65.7** (`⬆️ +3.7`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 58.4 → 61.9 (`⬆️ +3.5`) pkt
  - `4p-no-cienie`: 52.5 pkt
  - `4p-no-kabala`: 71.5 → 79.8 (`⬆️ +8.3`) pkt
  - `4p-no-korona`: 50.6 → 53.7 (`⬆️ +3.1`) pkt
  - `4p-no-oficjum`: 76.9 → 80.6 (`⬆️ +3.7`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 27.2 → 24.7 (`-2.5`) pkt
- **Tryb 4-osobowy (4p Avg):** 60.9 → 63.4 (`⬆️ +2.5`) pkt
- **Tryb 5-osobowy (5p Avg):** 16.9 → 13.6 (`-3.3`) pkt
- **Global Game Balance Score:** 35.0 → 🔴 ** 33.9** (`-1.1`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `4.77 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `3.4%` (norma: <30%)
  - **Autodafé / partię:** `1.59`
  - **Oskarżenia / partię:** `4.80`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-07_GOLD_SET3` | CAA-07 (Szantaż Bractwa): dodaj gold = 3 | 62.0 → 🟠 ** 65.7** (`⬆️ +3.7`) | 0.0% | 3.4% | 🌟 ZWYCIĘZCA |
| #2 | `L3_CAA-09_TARGET_HERESY_SET2` | CAA-09 (Kurier Relikwii): dodaj target_heresy = 2 | 62.0 → 🟠 ** 65.7** (`⬆️ +3.7`) | 0.0% | 3.3% | 🟢 ZYSK |
| #3 | `L3_CAA-07_GOLD_SET2` | CAA-07 (Szantaż Bractwa): dodaj gold = 2 | 62.0 → 🟠 ** 65.6** (`⬆️ +3.6`) | 0.0% | 3.4% | 🟢 ZYSK |
| #4 | `L3_GC-09_HERESY_MINUS1` | GC-09 (Lista Dłużników): heresy 1 → 0 | 62.0 → 🟠 ** 65.3** (`⬆️ +3.3`) | 0.0% | 3.3% | 🟢 ZYSK |
| #5 | `L3_CAA-02_TARGET_HERESY_SET1` | CAA-02 (Złoto z Kryjówki): dodaj target_heresy = 1 | 62.0 → 🟠 ** 65.0** (`⬆️ +3.0`) | 0.0% | 3.3% | 🟢 ZYSK |
| #6 | `L3_CAA-02_TARGET_HERESY_PLUS1` | CAA-02 (Złoto z Kryjówki): target_heresy 0 → 1 | 62.0 → 🟠 ** 65.0** (`⬆️ +3.0`) | 0.0% | 3.3% | 🟢 ZYSK |
| #7 | `L3_SO-05_TARGET_HERESY_MINUS1` | SO-05 (Wezwanie do Trybunału): target_heresy 1 → 0 | 62.0 → 🟠 ** 64.9** (`⬆️ +2.9`) | 0.0% | 3.3% | 🟢 ZYSK |
| #8 | `L3_CAA-07_TARGET_HERESY_SET2` | CAA-07 (Szantaż Bractwa): dodaj target_heresy = 2 | 62.0 → 🟠 ** 64.1** (`⬆️ +2.1`) | 0.0% | 3.4% | 🟢 ZYSK |
| #9 | `L3_GC-10_COST_MINUS1` | GC-10 (Upadek Domu): cost 4 → 3 | 62.0 → 🟠 ** 63.2** (`⬆️ +1.2`) | 0.0% | 3.3% | 🟢 ZYSK |
| #10 | `L3_SO-07_COST_MINUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 1 | 62.0 → 🟠 ** 63.2** (`⬆️ +1.2`) | 0.0% | 3.3% | 🟢 ZYSK |
| #11 | `L3_GC-12_HERESY_MINUS1` | GC-12 (Złodziejski Zwiad): heresy 2 → 1 | 62.0 → 🟠 ** 63.1** (`⬆️ +1.1`) | 0.0% | 3.3% | 🟢 ZYSK |
| #12 | `L3_GC-07_GOLD_SET3` | GC-07 (Skrytobójstwo): dodaj gold = 3 | 62.0 → 🟠 ** 63.0** (`⬆️ +1.0`) | 0.0% | 3.3% | 🟢 ZYSK |
| #13 | `L3_SO-07_GOLD_SET3` | SO-07 (Przesłuchanie Oficjum): dodaj gold = 3 | 62.0 → 🟠 ** 62.8** (`⬆️ +0.8`) | 0.0% | 3.3% | 🟢 ZYSK |
| #14 | `L3_GC-07_GOLD_SET2` | GC-07 (Skrytobójstwo): dodaj gold = 2 | 62.0 → 🟠 ** 62.5** (`⬆️ +0.5`) | 0.0% | 3.3% | 🟢 ZYSK |
| #15 | `L3_SO-07_GOLD_SET2` | SO-07 (Przesłuchanie Oficjum): dodaj gold = 2 | 62.0 → 🟠 ** 62.4** (`⬆️ +0.4`) | 0.0% | 3.3% | 🟢 ZYSK |
| #16 | `L3_SO-11_TARGET_HERESY_PLUS1` | SO-11 (Dekret Czystości Wiary): target_heresy 1 → 2 | 62.0 → 🟠 ** 62.2** (`⬆️ +0.2`) | 0.0% | 3.2% | 🟢 ZYSK |
| #17 | `L3_SO-09_GOLD_PLUS1` | SO-09 (Świadek Koronny): gold 0 → 1 | 62.0 → 🟠 ** 62.1** (`⬆️ +0.1`) | 0.0% | 3.2% | 🟢 ZYSK |
| #18 | `L3_GC-02_TARGET_HERESY_PLUS1` | GC-02 (Czarny Rynek): target_heresy 0 → 1 | 62.0 → 🟠 ** 61.0** (`-1.0`) | 0.0% | 3.3% | ⚪ STRATA/NEUTRALNY |
| #19 | `L4_TIME_DECK_EVERY_2ERAS` | Edykty Czasu: co 1 Erę → co 2 Ery | 62.0 → 🟠 ** 60.5** (`-1.5`) | 0.0% | 3.6% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_SO-06_HERESY_SET2` | SO-06 (Areszt Trybunalski): dodaj heresy = 2 | 62.0 → 🟠 ** 60.4** (`-1.6`) | 0.0% | 3.1% | ⚪ STRATA/NEUTRALNY |