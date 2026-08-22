# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.25 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.24` (4P: `11.9 pkt`) → **Nowa Wersja:** `v1.0-alpha.25` (4P: `27.2 pkt`)
**Data:** 2026-08-22 22:21 | **Czas Trwania Iteracji:** 292.5s | **Zysk 4P:** `+15.3 pkt` | **Zysk Global:** `+9.0 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_KB-09_GOLD_SET3` — **KB-09 (Dekret Królewski): dodaj gold = 3**
- **Opis Modyfikacji:** Karta `kb-09` (Dekret Królewski): `gold` → `3`
- **Wynik Kanonu 4P Balance:** 11.9 → 🔴 ** 27.2** (`⬆️ +15.3`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 20.1 → 64.5 (`⬆️ +44.4`) pkt
  - `4p-no-cienie`: 4.2 → 6.6 (`⬆️ +2.4`) pkt
  - `4p-no-kabala`: 7.6 → 14.3 (`⬆️ +6.7`) pkt
  - `4p-no-korona`: 18.2 pkt
  - `4p-no-oficjum`: 9.3 → 32.3 (`⬆️ +23.0`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 12.5 → 24.2 (`⬆️ +11.7`) pkt
- **Tryb 4-osobowy (4p Avg):** 11.9 → 26.8 (`⬆️ +14.9`) pkt
- **Tryb 5-osobowy (5p Avg):** 1.4 → 1.9 (`⬆️ +0.5`) pkt
- **Global Game Balance Score:** 8.6 → 🔴 ** 17.6** (`⬆️ +9.0`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `4.81 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `3.5%` (norma: <30%)
  - **Autodafé / partię:** `1.77`
  - **Oskarżenia / partię:** `5.07`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 11.9 → 🔴 ** 28.4** (`⬆️ +16.5`) | 0.0% | 3.8% | 🟢 ZYSK |
| #2 | `L3_KB-09_GOLD_SET3` | KB-09 (Dekret Królewski): dodaj gold = 3 | 11.9 → 🔴 ** 27.2** (`⬆️ +15.3`) | 0.0% | 3.5% | 🌟 ZWYCIĘZCA |
| #3 | `L3_KB-05_GOLD_SET3` | KB-05 (List Żelazny): dodaj gold = 3 | 11.9 → 🔴 ** 23.6** (`⬆️ +11.7`) | 0.0% | 3.3% | 🟢 ZYSK |
| #4 | `L3_KB-12_GOLD_SET3` | KB-12 (Szantaż Salonowy): dodaj gold = 3 | 11.9 → 🔴 ** 21.2** (`⬆️ +9.3`) | 0.0% | 3.1% | 🟢 ZYSK |
| #5 | `L3_KB-11_GOLD_SET3` | KB-11 (Tajny Emisariusz): dodaj gold = 3 | 11.9 → 🔴 ** 21.0** (`⬆️ +9.1`) | 0.0% | 3.1% | 🟢 ZYSK |
| #6 | `L3_KB-01_GOLD_SET3` | KB-01 (Rozkaz Dworu): dodaj gold = 3 | 11.9 → 🔴 ** 20.8** (`⬆️ +8.9`) | 0.0% | 3.2% | 🟢 ZYSK |
| #7 | `L3_KB-08_GOLD_SET3` | KB-08 (Przekupstwo Sędziego): dodaj gold = 3 | 11.9 → 🔴 ** 20.4** (`⬆️ +8.5`) | 0.0% | 3.3% | 🟢 ZYSK |
| #8 | `L3_KB-07_GOLD_SET3` | KB-07 (Szantaż Pieczęcią): dodaj gold = 3 | 11.9 → 🔴 ** 20.2** (`⬆️ +8.3`) | 0.0% | 3.3% | 🟢 ZYSK |
| #9 | `L3_KB-05_GOLD_SET2` | KB-05 (List Żelazny): dodaj gold = 2 | 11.9 → 🔴 ** 19.5** (`⬆️ +7.6`) | 0.0% | 3.7% | 🟢 ZYSK |
| #10 | `L3_KB-04_GOLD_SET3` | KB-04 (Faworyt Dworu): dodaj gold = 3 | 11.9 → 🔴 ** 19.0** (`⬆️ +7.1`) | 0.0% | 3.4% | 🟢 ZYSK |
| #11 | `L3_KB-03_GOLD_SET3` | KB-03 (Plotka Dworska): dodaj gold = 3 | 11.9 → 🔴 ** 18.7** (`⬆️ +6.8`) | 0.0% | 3.4% | 🟢 ZYSK |
| #12 | `L1_INTRIGUE_GOLD_DOUBLE` | Akcja Gospodarcza: 1 → 2 (podwojenie) | 11.9 → 🔴 ** 18.4** (`⬆️ +6.5`) | 0.0% | 3.5% | 🟢 ZYSK |
| #13 | `L1_INTRIGUE_GOLD_PLUS1` | Akcja Gospodarcza: 1 → 2 | 11.9 → 🔴 ** 18.4** (`⬆️ +6.5`) | 0.0% | 3.5% | 🟢 ZYSK |
| #14 | `L3_KB-09_GOLD_SET2` | KB-09 (Dekret Królewski): dodaj gold = 2 | 11.9 → 🔴 ** 17.9** (`⬆️ +6.0`) | 0.0% | 3.7% | 🟢 ZYSK |
| #15 | `L3_KB-09_COST_MINUS1` | KB-09 (Dekret Królewski): cost 4 → 3 | 11.9 → 🔴 ** 17.6** (`⬆️ +5.7`) | 0.0% | 4.7% | 🟢 ZYSK |
| #16 | `L3_KB-07_GOLD_SET2` | KB-07 (Szantaż Pieczęcią): dodaj gold = 2 | 11.9 → 🔴 ** 16.7** (`⬆️ +4.8`) | 0.0% | 3.7% | 🟢 ZYSK |
| #17 | `L1_START_GOLD_PLUS2` | Złoto startowe: offset +2 | 11.9 → 🔴 ** 16.5** (`⬆️ +4.6`) | 0.0% | 3.0% | 🟢 ZYSK |
| #18 | `L3_KB-10_COST_MINUS1` | KB-10 (Pieczęć Korony): cost 3 → 2 | 11.9 → 🔴 ** 16.2** (`⬆️ +4.3`) | 0.0% | 4.0% | 🟢 ZYSK |
| #19 | `L3_KB-02_GOLD_PLUS1` | KB-02 (Pobór Podatków): gold 2 → 3 | 11.9 → 🔴 ** 13.5** (`⬆️ +1.6`) | 0.0% | 4.1% | 🟢 ZYSK |
| #20 | `L3_KB-01_COST_PLUS1` | KB-01 (Rozkaz Dworu): cost 1 → 2 | 11.9 → 🔴 ** 12.9** (`⬆️ +1.0`) | 0.0% | 5.0% | 🟢 ZYSK |