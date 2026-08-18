# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.99.19 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v0.99.18` (4P: `71.2 pkt`) → **Nowa Wersja:** `v0.99.19` (4P: `73.1 pkt`)
**Data:** 2026-08-18 14:16 | **Czas Trwania Iteracji:** 660.4s | **Zysk 4P:** `+1.9 pkt` | **Zysk Global:** `-1.0 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_KB-11_TARGET_HERESY_PLUS1` — **KB-11 (Tajny Emisariusz): target_heresy 0 → 1**
- **Opis Modyfikacji:** Karta `kb-11` (Tajny Emisariusz): `target_heresy` → `1`
- **Wynik Kanonu 4P Score:** 71.2 → 🟠 ** 73.1** (`⬆️ +1.9`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 73.0 → 70.6 (`-2.4`) pkt
  - `4p-no-cienie`: 69.4 → 69.0 (`-0.4`) pkt
  - `4p-no-kabala`: 65.7 pkt
  - `4p-no-korona`: 81.5 pkt
  - `4p-no-oficjum`: 66.5 → 78.5 (`⬆️ +12.0`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 14.6 → 14.2 (`-0.4`) pkt
- **Tryb 4-osobowy (4p Avg):** 71.6 → 73.4 (`⬆️ +1.8`) pkt
- **Tryb 5-osobowy (5p Avg):** 40.7 → 36.4 (`-4.3`) pkt
- **Global Game Balance Score:** 42.3 → 🔴 ** 41.3** (`-1.0`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.22 Er`
  - **Deadlocki (Limit Er):** `0.7%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.5%` (norma: <30%)
  - **Autodafé / partię:** `2.23`
  - **Oskarżenia / partię:** `3.87`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_KB-11_TARGET_HERESY_PLUS1` | KB-11 (Tajny Emisariusz): target_heresy 0 → 1 | 71.2 → 🟠 ** 73.1** (`⬆️ +1.9`) | 0.7% | 1.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_GC-11_GOLD_PLUS1` | GC-11 (Fałszywe Świadectwo Cechu): gold 0 → 1 | 71.2 → 🟠 ** 72.0** (`⬆️ +0.8`) | 0.7% | 1.5% | 🟢 ZYSK |
| #3 | `L3_SO-01_TARGET_HERESY_PLUS1` | SO-01 (Patrol Familiariuszy): target_heresy 0 → 1 | 71.2 → 🟠 ** 71.8** (`⬆️ +0.6`) | 0.7% | 1.5% | 🟢 ZYSK |
| #4 | `L3_SO-11_HERESY_PLUS1` | SO-11 (Dekret Czystości Wiary): heresy 0 → 1 | 71.2 → 🟠 ** 71.5** (`⬆️ +0.3`) | 0.7% | 1.5% | 🟢 ZYSK |
| #5 | `L3_SO-06_TARGET_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): target_heresy 0 → 1 | 71.2 → 🟠 ** 71.5** (`⬆️ +0.3`) | 0.7% | 1.5% | 🟢 ZYSK |
| #6 | `L3_GC-03_GOLD_PLUS1` | GC-03 (Podrzucenie Księgi): gold 0 → 1 | 71.2 → 🟠 ** 71.4** (`⬆️ +0.2`) | 0.7% | 1.5% | 🟢 ZYSK |
| #7 | `L3_KB-01_HERESY_MINUS1` | KB-01 (Rozkaz Dworu): heresy 1 → 0 | 71.2 → 🟠 ** 71.4** (`⬆️ +0.2`) | 0.7% | 1.6% | 🟢 ZYSK |
| #8 | `L1_MAX_ERAS_MINUS1` | Limit Er: 13 → 12 | 71.2 → 🟠 ** 69.1** (`-2.1`) | 2.1% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 71.2 → 🟠 ** 71.4** (`⬆️ +0.2`) | 0.7% | 1.5% | 🟢 ZYSK |
| #10 | `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 2 → 3 | 71.2 → 🟠 ** 71.3** (`⬆️ +0.1`) | 0.7% | 1.5% | 🟢 ZYSK |
| #11 | `L3_KT-07_COST_MINUS1` | KT-07 (Archiwum Ukryte): cost 1 → 0 | 71.2 → 🟠 ** 71.3** (`⬆️ +0.1`) | 0.7% | 1.5% | 🟢 ZYSK |
| #12 | `L3_GC-12_COST_PLUS1` | GC-12 (Złodziejski Zwiad): cost 0 → 1 | 🟠 ** 71.2** | 0.7% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_SO-10_HERESY_MINUS1` | SO-10 (Oczyść Miasto): heresy 2 → 1 | 71.2 → 🟠 ** 71.0** (`-0.2`) | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_GC-03_COST_MINUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 0 | 71.2 → 🟠 ** 71.4** (`⬆️ +0.2`) | 0.7% | 1.5% | 🟢 ZYSK |
| #15 | `L3_SO-05_COST_PLUS1` | SO-05 (Wezwanie do Trybunału): cost 0 → 1 | 71.2 → 🟠 ** 71.3** (`⬆️ +0.1`) | 0.7% | 1.5% | 🟢 ZYSK |
| #16 | `L3_GC-11_COST_MINUS1` | GC-11 (Fałszywe Świadectwo Cechu): cost 1 → 0 | 71.2 → 🟠 ** 71.7** (`⬆️ +0.5`) | 0.7% | 1.5% | 🟢 ZYSK |
| #17 | `L3_CAA-12_COST_PLUS1` | CAA-12 (Skrytka w Murach): cost 0 → 1 | 71.2 → 🟠 ** 70.9** (`-0.3`) | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_CAA-12_GOLD_MINUS1` | CAA-12 (Skrytka w Murach): gold 3 → 2 | 71.2 → 🟠 ** 70.9** (`-0.3`) | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_KB-06_COST_MINUS1` | KB-06 (Areszt Królewski): cost 2 → 1 | 71.2 → 🟠 ** 70.5** (`-0.7`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_KB-01_TARGET_HERESY_PLUS1` | KB-01 (Rozkaz Dworu): target_heresy 1 → 2 | 71.2 → 🟠 ** 72.2** (`⬆️ +1.0`) | 0.5% | 1.6% | 🟢 ZYSK |
| #21 | `L3_GC-08_COST_MINUS1` | GC-08 (Zatrute Złoto): cost 1 → 0 | 🟠 ** 71.2** | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_GC-08_GOLD_PLUS1` | GC-08 (Zatrute Złoto): gold 1 → 2 | 71.2 → 🟠 ** 70.9** (`-0.3`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_GC-07_TARGET_HERESY_PLUS1` | GC-07 (Skrytobójstwo): target_heresy 0 → 1 | 71.2 → 🟠 ** 71.5** (`⬆️ +0.3`) | 0.7% | 1.5% | 🟢 ZYSK |
| #24 | `L3_SO-08_TARGET_HERESY_PLUS1` | SO-08 (Nasłanie Inkwizytora): target_heresy 0 → 1 | 71.2 → 🟠 ** 72.0** (`⬆️ +0.8`) | 0.5% | 1.5% | 🟢 ZYSK |