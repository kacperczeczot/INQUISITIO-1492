# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.72 (Iteracja #6, Faza 3D)

**Wersja Poprzednia:** `v1.0-alpha.71` (4P: `76.6 pkt`) → **Nowa Wersja:** `v1.0-alpha.72` (4P: `80.0 pkt`)
**Data:** 2026-08-24 09:52 | **Czas Trwania Iteracji:** 3276.1s | **Zysk 4P:** `+3.4 pkt` | **Zysk Global:** `-4.8 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (3D):** `L3_SO-01_HERESY_SET2__L3_CAA-08_COST_PLUS1__L3_CAA-05_GOLD_SET3` — **SO-01 (Patrol Familiariuszy): dodaj heresy = 2 + CAA-08 (Kaptur Nocy): cost 1 → 2 + CAA-05 (Ukryty Kurier): dodaj gold = 3**
- **Opis Modyfikacji:** Karta `so-01` (Patrol Familiariuszy): `heresy` → `2` + Karta `caa-08` (Kaptur Nocy): `cost` → `2` + Karta `caa-05` (Ukryty Kurier): `gold` → `3`
- **Wynik Kanonu 4P Balance:** 76.6 → 🟡 ** 80.0** (`⬆️ +3.4`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 83.2 → 82.8 (`-0.4`) pkt
  - `4p-no-cienie`: 63.5 → 66.4 (`⬆️ +2.9`) pkt
  - `4p-no-kabala`: 88.7 → 90.7 (`⬆️ +2.0`) pkt
  - `4p-no-korona`: 91.3 → 97.0 (`⬆️ +5.7`) pkt
  - `4p-no-oficjum`: 56.2 → 63.0 (`⬆️ +6.8`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 32.0 → 34.5 (`⬆️ +2.5`) pkt
- **Tryb 4-osobowy (4p Avg):** 70.2 → 72.2 (`⬆️ +2.0`) pkt
- **Tryb 5-osobowy (5p Avg):** 22.1 → 3.2 (`-18.9`) pkt
- **Global Game Balance Score:** 41.4 → 🔴 ** 36.6** (`-4.8`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.73 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.6%` (norma: <30%)
  - **Autodafé / partię:** `1.47`
  - **Oskarżenia / partię:** `6.75`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-01_HERESY_SET2__L3_CAA-08_COST_PLUS1__L3_CAA-05_GOLD_SET3` | SO-01 (Patrol Familiariuszy): dodaj heresy = 2 + CAA-08 (Kaptur Nocy): cost 1 → 2 + CAA-05 (Ukryty Kurier): dodaj gold = 3 | 76.6 → 🟡 ** 80.0** (`⬆️ +3.4`) | 0.0% | 4.6% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-01_HERESY_SET2__L3_CAA-08_COST_PLUS1__L3_CAA-05_GOLD_SET2` | SO-01 (Patrol Familiariuszy): dodaj heresy = 2 + CAA-08 (Kaptur Nocy): cost 1 → 2 + CAA-05 (Ukryty Kurier): dodaj gold = 2 | 76.6 → 🟡 ** 80.0** (`⬆️ +3.4`) | 0.0% | 4.6% | 🟢 ZYSK |
| #3 | `L3_SO-01_HERESY_SET2__L3_CAA-08_COST_PLUS1__L3_CAA-03_COST_PLUS1` | SO-01 (Patrol Familiariuszy): dodaj heresy = 2 + CAA-08 (Kaptur Nocy): cost 1 → 2 + CAA-03 (Cień na Rynku): cost 0 → 1 | 76.6 → 🟡 ** 79.2** (`⬆️ +2.6`) | 0.0% | 4.6% | 🟢 ZYSK |
| #4 | `L3_SO-01_HERESY_SET2__L3_CAA-08_COST_PLUS1__L3_CAA-05_TARGET_HERESY_PLUS1` | SO-01 (Patrol Familiariuszy): dodaj heresy = 2 + CAA-08 (Kaptur Nocy): cost 1 → 2 + CAA-05 (Ukryty Kurier): target_heresy 2 → 3 | 76.6 → 🟡 ** 79.2** (`⬆️ +2.6`) | 0.0% | 4.6% | 🟢 ZYSK |
| #5 | `L3_SO-01_HERESY_SET2__L3_CAA-08_COST_PLUS1__L3_CAA-05_COST_MINUS1` | SO-01 (Patrol Familiariuszy): dodaj heresy = 2 + CAA-08 (Kaptur Nocy): cost 1 → 2 + CAA-05 (Ukryty Kurier): cost 1 → 0 | 76.6 → 🟡 ** 79.1** (`⬆️ +2.5`) | 0.0% | 4.6% | 🟢 ZYSK |
| #6 | `L3_KT-03_HERESY_MINUS1__L3_CAA-10_COST_MINUS1__L3_CAA-09_HERESY_SET1` | KT-03 (Zakazana Wiedza): heresy 2 → 1 + CAA-10 (Echo Alhambry): cost 3 → 2 + CAA-09 (Kurier Relikwii): dodaj heresy = 1 | 76.6 → 🟡 ** 78.8** (`⬆️ +2.2`) | 0.0% | 4.3% | 🟢 ZYSK |
| #7 | `L3_KT-03_HERESY_MINUS1__L3_CAA-10_COST_MINUS1__L3_CAA-09_HERESY_PLUS1` | KT-03 (Zakazana Wiedza): heresy 2 → 1 + CAA-10 (Echo Alhambry): cost 3 → 2 + CAA-09 (Kurier Relikwii): heresy 0 → 1 | 76.6 → 🟡 ** 78.8** (`⬆️ +2.2`) | 0.0% | 4.3% | 🟢 ZYSK |
| #8 | `L3_SO-01_HERESY_SET2__L3_CAA-07_HERESY_SET1__L3_CAA-05_GOLD_SET3` | SO-01 (Patrol Familiariuszy): dodaj heresy = 2 + CAA-07 (Szantaż Bractwa): dodaj heresy = 1 + CAA-05 (Ukryty Kurier): dodaj gold = 3 | 76.6 → 🟡 ** 77.8** (`⬆️ +1.2`) | 0.0% | 4.6% | 🟢 ZYSK |
| #9 | `L3_SO-01_HERESY_SET2__L3_CAA-07_HERESY_PLUS1__L3_CAA-05_GOLD_SET3` | SO-01 (Patrol Familiariuszy): dodaj heresy = 2 + CAA-07 (Szantaż Bractwa): heresy 0 → 1 + CAA-05 (Ukryty Kurier): dodaj gold = 3 | 76.6 → 🟡 ** 77.8** (`⬆️ +1.2`) | 0.0% | 4.6% | 🟢 ZYSK |
| #10 | `L3_SO-01_HERESY_SET2__L3_CAA-07_HERESY_PLUS1__L3_CAA-05_GOLD_SET2` | SO-01 (Patrol Familiariuszy): dodaj heresy = 2 + CAA-07 (Szantaż Bractwa): heresy 0 → 1 + CAA-05 (Ukryty Kurier): dodaj gold = 2 | 76.6 → 🟡 ** 77.7** (`⬆️ +1.1`) | 0.0% | 4.6% | 🟢 ZYSK |
| #11 | `L3_SO-01_HERESY_SET2__L3_CAA-07_HERESY_SET1__L3_CAA-05_GOLD_SET2` | SO-01 (Patrol Familiariuszy): dodaj heresy = 2 + CAA-07 (Szantaż Bractwa): dodaj heresy = 1 + CAA-05 (Ukryty Kurier): dodaj gold = 2 | 76.6 → 🟡 ** 77.7** (`⬆️ +1.1`) | 0.0% | 4.6% | 🟢 ZYSK |
| #12 | `L3_KT-03_HERESY_MINUS1__L3_CAA-10_COST_MINUS1__L3_CAA-05_TARGET_HERESY_MINUS1` | KT-03 (Zakazana Wiedza): heresy 2 → 1 + CAA-10 (Echo Alhambry): cost 3 → 2 + CAA-05 (Ukryty Kurier): target_heresy 2 → 1 | 76.6 → 🟡 ** 76.7** (`⬆️ +0.1`) | 0.0% | 4.3% | 🟢 ZYSK |
| #13 | `L3_SO-01_HERESY_SET2__L3_CAA-08_COST_PLUS1__L3_CAA-09_TARGET_HERESY_SET2` | SO-01 (Patrol Familiariuszy): dodaj heresy = 2 + CAA-08 (Kaptur Nocy): cost 1 → 2 + CAA-09 (Kurier Relikwii): dodaj target_heresy = 2 | 76.6 → 🟡 ** 76.3** (`-0.3`) | 0.0% | 4.7% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_KT-03_HERESY_MINUS1__L3_CAA-10_COST_MINUS1__L3_CAA-04_TARGET_HERESY_PLUS1` | KT-03 (Zakazana Wiedza): heresy 2 → 1 + CAA-10 (Echo Alhambry): cost 3 → 2 + CAA-04 (Fałszywy Trop): target_heresy 1 → 2 | 76.6 → 🟡 ** 75.9** (`-0.7`) | 0.0% | 4.4% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_KT-03_HERESY_MINUS1__L3_CAA-10_COST_MINUS1__L3_CAA-01_GOLD_SET3` | KT-03 (Zakazana Wiedza): heresy 2 → 1 + CAA-10 (Echo Alhambry): cost 3 → 2 + CAA-01 (Przejście Podziemiami): dodaj gold = 3 | 76.6 → 🟡 ** 75.7** (`-0.9`) | 0.0% | 4.3% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_KT-03_HERESY_MINUS1__L3_CAA-10_COST_MINUS1__L3_CAA-11_COST_MINUS1` | KT-03 (Zakazana Wiedza): heresy 2 → 1 + CAA-10 (Echo Alhambry): cost 3 → 2 + CAA-11 (Nocna Zmiana Warty): cost 1 → 0 | 76.6 → 🟡 ** 75.6** (`-1.0`) | 0.0% | 4.3% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_KT-03_HERESY_MINUS1__L3_CAA-10_COST_MINUS1__L1_THRESHOLD_MINUS1` | KT-03 (Zakazana Wiedza): heresy 2 → 1 + CAA-10 (Echo Alhambry): cost 3 → 2 + Próg Oskarżenia: 7 → 6 | 76.6 → 🟡 ** 75.2** (`-1.4`) | 0.0% | 4.1% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_KT-03_HERESY_MINUS1__L3_CAA-10_COST_MINUS1__L3_CAA-06_HERESY_PLUS1` | KT-03 (Zakazana Wiedza): heresy 2 → 1 + CAA-10 (Echo Alhambry): cost 3 → 2 + CAA-06 (Ucieczka z Lochów): heresy 0 → 1 | 76.6 → 🟠 ** 74.0** (`-2.6`) | 0.0% | 4.3% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_KT-03_HERESY_MINUS1__L3_CAA-10_COST_MINUS1__L3_CAA-06_HERESY_SET1` | KT-03 (Zakazana Wiedza): heresy 2 → 1 + CAA-10 (Echo Alhambry): cost 3 → 2 + CAA-06 (Ucieczka z Lochów): dodaj heresy = 1 | 76.6 → 🟠 ** 74.0** (`-2.6`) | 0.0% | 4.3% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_SO-01_HERESY_SET2__L3_CAA-08_COST_PLUS1__L3_CAA-03_HERESY_MINUS1` | SO-01 (Patrol Familiariuszy): dodaj heresy = 2 + CAA-08 (Kaptur Nocy): cost 1 → 2 + CAA-03 (Cień na Rynku): heresy 1 → 0 | 76.6 → 🟠 ** 71.5** (`-5.1`) | 0.0% | 4.7% | ⚪ STRATA/NEUTRALNY |