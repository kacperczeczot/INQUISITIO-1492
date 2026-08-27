# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.27 (Iteracja #2, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.26` (4P: `35.3 pkt`) → **Nowa Wersja:** `v1.0-alpha.27` (4P: `48.7 pkt`)
**Data:** 2026-08-22 22:45 | **Czas Trwania Iteracji:** 641.0s | **Zysk 4P:** `+13.4 pkt` | **Zysk Global:** `+3.5 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L2_GC_FALLS_MINUS1` — **Gildia Upadki: 7 → 6**
- **Opis Modyfikacji:** Gildia Cieni: Upadki offset -1
- **Wynik Kanonu 4P Balance:** 35.3 → 🔴 ** 48.7** (`⬆️ +13.4`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 63.4 pkt
  - `4p-no-cienie`: 8.2 → 13.6 (`⬆️ +5.4`) pkt
  - `4p-no-kabala`: 24.7 → 39.7 (`⬆️ +15.0`) pkt
  - `4p-no-korona`: 23.7 → 40.9 (`⬆️ +17.2`) pkt
  - `4p-no-oficjum`: 56.4 → 85.7 (`⬆️ +29.3`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 25.8 → 16.9 (`-8.9`) pkt
- **Tryb 4-osobowy (4p Avg):** 34.0 → 50.2 (`⬆️ +16.2`) pkt
- **Tryb 5-osobowy (5p Avg):** 2.9 → 6.1 (`⬆️ +3.2`) pkt
- **Global Game Balance Score:** 20.9 → 🔴 ** 24.4** (`⬆️ +3.5`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `4.68 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `3.4%` (norma: <30%)
  - **Autodafé / partię:** `1.71`
  - **Oskarżenia / partię:** `4.78`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L2_GC_FALLS_MINUS1` | Gildia Upadki: 7 → 6 | 35.3 → 🔴 ** 48.7** (`⬆️ +13.4`) | 0.0% | 3.4% | 🌟 ZWYCIĘZCA |
| #2 | `L3_GC-10_HERESY_MINUS1` | GC-10 (Upadek Domu): heresy 2 → 1 | 35.3 → 🔴 ** 46.0** (`⬆️ +10.7`) | 0.0% | 3.4% | 🟢 ZYSK |
| #3 | `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2/3/3 → 3/4/4 | 35.3 → 🔴 ** 45.9** (`⬆️ +10.6`) | 0.0% | 3.5% | 🟢 ZYSK |
| #4 | `L2_SO_CONDEMNS_PLUS2` | Oficjum Skazania: 2/3/3 → 4/5/5 | 35.3 → 🔴 ** 45.9** (`⬆️ +10.6`) | 0.0% | 3.5% | 🟢 ZYSK |
| #5 | `L2_SO_STACKS_PLUS2` | Oficjum Stosy: 6 → 8 | 35.3 → 🔴 ** 45.7** (`⬆️ +10.4`) | 0.0% | 3.5% | 🟢 ZYSK |
| #6 | `L3_GC-10_TARGET_HERESY_SET2` | GC-10 (Upadek Domu): dodaj target_heresy = 2 | 35.3 → 🔴 ** 44.0** (`⬆️ +8.7`) | 0.0% | 3.5% | 🟢 ZYSK |
| #7 | `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 6 → 7 | 35.3 → 🔴 ** 42.7** (`⬆️ +7.4`) | 0.0% | 3.5% | 🟢 ZYSK |
| #8 | `L3_GC-06_GOLD_SET3` | GC-06 (Szantaż): dodaj gold = 3 | 35.3 → 🔴 ** 42.0** (`⬆️ +6.7`) | 0.0% | 3.4% | 🟢 ZYSK |
| #9 | `L3_GC-06_GOLD_SET2` | GC-06 (Szantaż): dodaj gold = 2 | 35.3 → 🔴 ** 41.9** (`⬆️ +6.6`) | 0.0% | 3.4% | 🟢 ZYSK |
| #10 | `L3_GC-06_TARGET_HERESY_PLUS1` | GC-06 (Szantaż): target_heresy 0 → 1 | 35.3 → 🔴 ** 41.1** (`⬆️ +5.8`) | 0.0% | 3.5% | 🟢 ZYSK |
| #11 | `L1_INTRIGUE_GOLD_DOUBLE` | Akcja Gospodarcza: 1 → 2 (podwojenie) | 35.3 → 🔴 ** 40.9** (`⬆️ +5.6`) | 0.0% | 2.8% | 🟢 ZYSK |
| #12 | `L1_INTRIGUE_GOLD_PLUS1` | Akcja Gospodarcza: 1 → 2 | 35.3 → 🔴 ** 40.9** (`⬆️ +5.6`) | 0.0% | 2.8% | 🟢 ZYSK |
| #13 | `L3_KB-09_HERESY_MINUS1` | KB-09 (Dekret Królewski): heresy 1 → 0 | 35.3 → 🔴 ** 40.7** (`⬆️ +5.4`) | 0.0% | 3.4% | 🟢 ZYSK |
| #14 | `L3_KB-02_COST_MINUS1` | KB-02 (Pobór Podatków): cost 1 → 0 | 35.3 → 🔴 ** 40.7** (`⬆️ +5.4`) | 0.0% | 2.6% | 🟢 ZYSK |
| #15 | `L1_START_GOLD_PLUS1` | Złoto startowe: 5zł → 6zł | 35.3 → 🔴 ** 39.0** (`⬆️ +3.7`) | 0.0% | 2.2% | 🟢 ZYSK |
| #16 | `L3_KB-04_HERESY_MINUS1` | KB-04 (Faworyt Dworu): heresy 1 → 0 | 35.3 → 🔴 ** 36.3** (`⬆️ +1.0`) | 0.0% | 3.4% | 🟢 ZYSK |
| #17 | `L3_SO-10_GOLD_PLUS1` | SO-10 (Oczyść Miasto): gold 0 → 1 | 🔴 ** 35.3** | 0.0% | 3.0% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_SO-10_GOLD_SET1` | SO-10 (Oczyść Miasto): dodaj gold = 1 | 🔴 ** 35.3** | 0.0% | 3.0% | ⚪ STRATA/NEUTRALNY |
| #19 | `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 35.3 → 🔴 ** 26.8** (`-8.5`) | 0.0% | 4.0% | ⚪ STRATA/NEUTRALNY |
| #20 | `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 35.3 → 🔴 ** 20.5** (`-14.8`) | 0.0% | 3.7% | ⚪ STRATA/NEUTRALNY |