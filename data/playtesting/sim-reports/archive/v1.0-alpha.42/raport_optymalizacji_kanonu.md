[Strona główna](../../../../../README.md) > [v1.0-alpha.42](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.42 (Iteracja #7, Faza 2D)

**Wersja Poprzednia:** `v1.0-alpha.41` (4P: `72.1 pkt`) → **Nowa Wersja:** `v1.0-alpha.42` (4P: `75.5 pkt`)
**Data:** 2026-08-23 08:17 | **Czas Trwania Iteracji:** 1117.0s | **Zysk 4P:** `+3.4 pkt` | **Zysk Global:** `+0.6 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (2D):** `L3_CAA-11_GOLD_SET3__L3_GC-09_GOLD_MINUS1` — **CAA-11 (Nocna Zmiana Warty): dodaj gold = 3 + GC-09 (Lista Dłużników): gold 1 → 0**
- **Opis Modyfikacji:** Karta `caa-11` (Nocna Zmiana Warty): `gold` → `3` + Karta `gc-09` (Lista Dłużników): `gold` → `0`
- **Wynik Kanonu 4P Balance:** 72.1 → 🟡 ** 75.5** (`⬆️ +3.4`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 60.1 → 62.0 (`⬆️ +1.9`) pkt
  - `4p-no-cienie`: 77.1 → 75.5 (`-1.6`) pkt
  - `4p-no-kabala`: 72.0 → 77.9 (`⬆️ +5.9`) pkt
  - `4p-no-korona`: 79.8 → 82.6 (`⬆️ +2.8`) pkt
  - `4p-no-oficjum`: 71.6 → 79.3 (`⬆️ +7.7`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 22.8 → 25.9 (`⬆️ +3.1`) pkt
- **Tryb 4-osobowy (4p Avg):** 72.4 → 72.1 (`-0.3`) pkt
- **Tryb 5-osobowy (5p Avg):** 22.6 → 21.6 (`-1.0`) pkt
- **Global Game Balance Score:** 39.3 → 🔴 ** 39.9** (`⬆️ +0.6`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `4.79 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `3.5%` (norma: <30%)
  - **Autodafé / partię:** `1.58`
  - **Oskarżenia / partię:** `4.58`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-11_GOLD_SET3__L3_GC-09_GOLD_MINUS1` | CAA-11 (Nocna Zmiana Warty): dodaj gold = 3 + GC-09 (Lista Dłużników): gold 1 → 0 | 72.1 → 🟡 ** 75.5** (`⬆️ +3.4`) | 0.0% | 3.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_CAA-11_GOLD_SET3__L3_GC-01_HERESY_PLUS1` | CAA-11 (Nocna Zmiana Warty): dodaj gold = 3 + GC-01 (Przekupiony Strażnik): heresy 1 → 2 | 72.1 → 🟡 ** 75.2** (`⬆️ +3.1`) | 0.0% | 3.4% | 🟢 ZYSK |
| #3 | `L3_CAA-11_GOLD_SET3__L3_GC-10_GOLD_SET1` | CAA-11 (Nocna Zmiana Warty): dodaj gold = 3 + GC-10 (Upadek Domu): dodaj gold = 1 | 72.1 → 🟠 ** 74.7** (`⬆️ +2.6`) | 0.0% | 3.5% | 🟢 ZYSK |
| #4 | `L3_CAA-11_GOLD_SET3__L3_GC-10_GOLD_PLUS1` | CAA-11 (Nocna Zmiana Warty): dodaj gold = 3 + GC-10 (Upadek Domu): gold 0 → 1 | 72.1 → 🟠 ** 74.7** (`⬆️ +2.6`) | 0.0% | 3.5% | 🟢 ZYSK |
| #5 | `L3_CAA-11_GOLD_SET3__L3_GC-10_HERESY_PLUS1` | CAA-11 (Nocna Zmiana Warty): dodaj gold = 3 + GC-10 (Upadek Domu): heresy 2 → 3 | 72.1 → 🟠 ** 74.6** (`⬆️ +2.5`) | 0.0% | 3.5% | 🟢 ZYSK |
| #6 | `L3_CAA-11_GOLD_SET3__L1_THRESHOLD_PLUS1` | CAA-11 (Nocna Zmiana Warty): dodaj gold = 3 + Próg Oskarżenia: 7 → 8 | 72.1 → 🟠 ** 74.4** (`⬆️ +2.3`) | 0.0% | 3.4% | 🟢 ZYSK |
| #7 | `L3_CAA-11_GOLD_SET3__L3_GC-05_HERESY_PLUS1` | CAA-11 (Nocna Zmiana Warty): dodaj gold = 3 + GC-05 (Fałszywy Świadek): heresy 0 → 1 | 72.1 → 🟠 ** 74.4** (`⬆️ +2.3`) | 0.0% | 3.4% | 🟢 ZYSK |
| #8 | `L3_CAA-11_GOLD_SET3__L3_GC-05_HERESY_SET2` | CAA-11 (Nocna Zmiana Warty): dodaj gold = 3 + GC-05 (Fałszywy Świadek): dodaj heresy = 2 | 72.1 → 🟠 ** 74.4** (`⬆️ +2.3`) | 0.0% | 3.4% | 🟢 ZYSK |
| #9 | `L3_CAA-11_GOLD_SET3__L3_GC-05_TARGET_HERESY_SET1` | CAA-11 (Nocna Zmiana Warty): dodaj gold = 3 + GC-05 (Fałszywy Świadek): dodaj target_heresy = 1 | 72.1 → 🟠 ** 74.4** (`⬆️ +2.3`) | 0.0% | 3.4% | 🟢 ZYSK |
| #10 | `L3_CAA-11_GOLD_SET3__L3_GC-06_COST_PLUS1` | CAA-11 (Nocna Zmiana Warty): dodaj gold = 3 + GC-06 (Szantaż): cost 2 → 3 | 72.1 → 🟠 ** 74.0** (`⬆️ +1.9`) | 0.0% | 3.5% | 🟢 ZYSK |
| #11 | `L3_CAA-11_GOLD_SET3__L3_GC-09_GOLD_PLUS1` | CAA-11 (Nocna Zmiana Warty): dodaj gold = 3 + GC-09 (Lista Dłużników): gold 1 → 2 | 72.1 → 🟠 ** 73.7** (`⬆️ +1.6`) | 0.0% | 3.4% | 🟢 ZYSK |
| #12 | `L3_SO-03_COST_MINUS1__L3_CAA-01_TARGET_HERESY_SET1` | SO-03 (Podejrzenie): cost 2 → 1 + CAA-01 (Przejście Podziemiami): dodaj target_heresy = 1 | 72.1 → 🟠 ** 71.1** (`-1.0`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_SO-03_COST_MINUS1__L3_CAA-01_TARGET_HERESY_PLUS1` | SO-03 (Podejrzenie): cost 2 → 1 + CAA-01 (Przejście Podziemiami): target_heresy 0 → 1 | 72.1 → 🟠 ** 71.1** (`-1.0`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_SO-03_COST_MINUS1__L3_CAA-07_TARGET_HERESY_SET2` | SO-03 (Podejrzenie): cost 2 → 1 + CAA-07 (Szantaż Bractwa): dodaj target_heresy = 2 | 72.1 → 🟠 ** 71.0** (`-1.1`) | 0.0% | 3.5% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_SO-03_COST_MINUS1__L3_CAA-03_TARGET_HERESY_SET2` | SO-03 (Podejrzenie): cost 2 → 1 + CAA-03 (Cień na Rynku): dodaj target_heresy = 2 | 72.1 → 🟠 ** 70.6** (`-1.5`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_CAA-11_GOLD_SET3__L1_THRESHOLD_MINUS1` | CAA-11 (Nocna Zmiana Warty): dodaj gold = 3 + Próg Oskarżenia: 7 → 6 | 72.1 → 🟠 ** 69.6** (`-2.5`) | 0.0% | 3.1% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_SO-06_TARGET_HERESY_PLUS1__L3_CAA-07_COST_PLUS1` | SO-06 (Areszt Trybunalski): target_heresy 1 → 2 + CAA-07 (Szantaż Bractwa): cost 0 → 1 | 72.1 → 🟠 ** 67.1** (`-5.0`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_SO-06_TARGET_HERESY_PLUS1__L3_CAA-07_GOLD_MINUS1` | SO-06 (Areszt Trybunalski): target_heresy 1 → 2 + CAA-07 (Szantaż Bractwa): gold 3 → 2 | 72.1 → 🟠 ** 67.1** (`-5.0`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_SO-03_COST_MINUS1__L3_CAA-04_HERESY_SET2` | SO-03 (Podejrzenie): cost 2 → 1 + CAA-04 (Fałszywy Trop): dodaj heresy = 2 | 72.1 → 🟠 ** 66.8** (`-5.3`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #20 | `L2_GC_FALLS_PLUS1__L3_CAA-04_TARGET_HERESY_MINUS1` | Gildia Upadki: 6 → 7 + CAA-04 (Fałszywy Trop): target_heresy 1 → 0 | 72.1 → 🔴 ** 55.2** (`-16.9`) | 0.0% | 3.6% | ⚪ STRATA/NEUTRALNY |