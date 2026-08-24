# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.38 (Iteracja #3, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.37` (4P: `62.4 pkt`) → **Nowa Wersja:** `v1.0-alpha.38` (4P: `66.4 pkt`)
**Data:** 2026-08-23 04:09 | **Czas Trwania Iteracji:** 615.3s | **Zysk 4P:** `+4.0 pkt` | **Zysk Global:** `+2.8 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_GC-04_HERESY_MINUS1` — **GC-04 (Informator): heresy 1 → 0**
- **Opis Modyfikacji:** Karta `gc-04` (Informator): `heresy` → `0`
- **Wynik Kanonu 4P Balance:** 62.4 → 🟠 ** 66.4** (`⬆️ +4.0`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 61.0 pkt
  - `4p-no-cienie`: 42.8 → 53.9 (`⬆️ +11.1`) pkt
  - `4p-no-kabala`: 76.1 → 78.3 (`⬆️ +2.2`) pkt
  - `4p-no-korona`: 52.3 → 59.8 (`⬆️ +7.5`) pkt
  - `4p-no-oficjum`: 79.8 → 79.1 (`-0.7`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 24.7 → 25.5 (`⬆️ +0.8`) pkt
- **Tryb 4-osobowy (4p Avg):** 63.4 → 67.3 (`⬆️ +3.9`) pkt
- **Tryb 5-osobowy (5p Avg):** 13.6 → 17.4 (`⬆️ +3.8`) pkt
- **Global Game Balance Score:** 33.9 → 🔴 ** 36.7** (`⬆️ +2.8`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `4.78 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `3.4%` (norma: <30%)
  - **Autodafé / partię:** `1.58`
  - **Oskarżenia / partię:** `4.73`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-04_HERESY_MINUS1` | GC-04 (Informator): heresy 1 → 0 | 62.4 → 🟠 ** 66.4** (`⬆️ +4.0`) | 0.0% | 3.4% | 🌟 ZWYCIĘZCA |
| #2 | `L3_GC-09_HERESY_MINUS1` | GC-09 (Lista Dłużników): heresy 1 → 0 | 62.4 → 🟠 ** 66.2** (`⬆️ +3.8`) | 0.0% | 3.4% | 🟢 ZYSK |
| #3 | `L3_GC-06_HERESY_MINUS1` | GC-06 (Szantaż): heresy 1 → 0 | 62.4 → 🟠 ** 65.8** (`⬆️ +3.4`) | 0.0% | 3.4% | 🟢 ZYSK |
| #4 | `L3_GC-08_HERESY_MINUS1` | GC-08 (Zatrute Złoto): heresy 1 → 0 | 62.4 → 🟠 ** 65.8** (`⬆️ +3.4`) | 0.0% | 3.4% | 🟢 ZYSK |
| #5 | `L1_OBSERVED_PLUS1` | Próg Obserwowanej: 5 → 6 | 62.4 → 🟠 ** 65.6** (`⬆️ +3.2`) | 0.0% | 3.4% | 🟢 ZYSK |
| #6 | `L3_KT-09_HERESY_MINUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 0 | 62.4 → 🟠 ** 65.0** (`⬆️ +2.6`) | 0.0% | 3.5% | 🟢 ZYSK |
| #7 | `L4_TIME_DECK_EVERY_3ERAS` | Edykty Czasu: co 1 Erę → co 3 Ery | 62.4 → 🟠 ** 64.5** (`⬆️ +2.1`) | 0.0% | 3.8% | 🟢 ZYSK |
| #8 | `L3_GC-01_COST_MINUS1` | GC-01 (Przekupiony Strażnik): cost 2 → 1 | 62.4 → 🟠 ** 64.5** (`⬆️ +2.1`) | 0.0% | 3.4% | 🟢 ZYSK |
| #9 | `L3_GC-01_GOLD_PLUS1` | GC-01 (Przekupiony Strażnik): gold 1 → 2 | 62.4 → 🟠 ** 64.4** (`⬆️ +2.0`) | 0.0% | 3.4% | 🟢 ZYSK |
| #10 | `L3_KB-06_COST_MINUS1` | KB-06 (Areszt Królewski): cost 2 → 1 | 62.4 → 🟠 ** 64.1** (`⬆️ +1.7`) | 0.0% | 3.1% | 🟢 ZYSK |
| #11 | `L3_CAA-06_TARGET_HERESY_SET2` | CAA-06 (Ucieczka z Lochów): dodaj target_heresy = 2 | 62.4 → 🟠 ** 64.1** (`⬆️ +1.7`) | 0.0% | 3.4% | 🟢 ZYSK |
| #12 | `L3_KT-10_COST_PLUS1` | KT-10 (Pieczęć Salomona): cost 2 → 3 | 62.4 → 🟠 ** 63.8** (`⬆️ +1.4`) | 0.0% | 3.5% | 🟢 ZYSK |
| #13 | `L3_GC-11_TARGET_HERESY_MINUS1` | GC-11 (Fałszywe Świadectwo Cechu): target_heresy 1 → 0 | 62.4 → 🟠 ** 63.8** (`⬆️ +1.4`) | 0.0% | 3.4% | 🟢 ZYSK |
| #14 | `L3_SO-02_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): heresy 0 → 1 | 62.4 → 🟠 ** 63.6** (`⬆️ +1.2`) | 0.0% | 3.5% | 🟢 ZYSK |
| #15 | `L3_SO-02_HERESY_SET1` | SO-02 (Skarbiec Trybunału): dodaj heresy = 1 | 62.4 → 🟠 ** 63.6** (`⬆️ +1.2`) | 0.0% | 3.5% | 🟢 ZYSK |
| #16 | `L3_SO-09_HERESY_PLUS1` | SO-09 (Świadek Koronny): heresy 0 → 1 | 62.4 → 🟠 ** 63.4** (`⬆️ +1.0`) | 0.0% | 3.5% | 🟢 ZYSK |
| #17 | `L3_CAA-05_HERESY_PLUS2` | CAA-05 (Ukryty Kurier): heresy 0 → 2 (+2) | 62.4 → 🟠 ** 60.2** (`-2.2`) | 0.0% | 3.3% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_CAA-05_HERESY_SET2` | CAA-05 (Ukryty Kurier): dodaj heresy = 2 | 62.4 → 🟠 ** 60.2** (`-2.2`) | 0.0% | 3.3% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_KB-11_GOLD_SET1` | KB-11 (Tajny Emisariusz): dodaj gold = 1 | 62.4 → 🟠 ** 60.1** (`-2.3`) | 0.0% | 3.0% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_KB-10_HERESY_PLUS1` | KB-10 (Pieczęć Korony): heresy 2 → 3 | 62.4 → 🔴 ** 55.7** (`-6.7`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |