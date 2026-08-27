[Strona główna](../../../../../README.md) > [v1.0-alpha.32](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.32 (Iteracja #2, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.31` (4P: `62.2 pkt`) → **Nowa Wersja:** `v1.0-alpha.32` (4P: `70.3 pkt`)
**Data:** 2026-08-22 23:35 | **Czas Trwania Iteracji:** 620.9s | **Zysk 4P:** `+8.1 pkt` | **Zysk Global:** `+1.9 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_KB-09_HERESY_MINUS1` — **KB-09 (Dekret Królewski): heresy 1 → 0**
- **Opis Modyfikacji:** Karta `kb-09` (Dekret Królewski): `heresy` → `0`
- **Wynik Kanonu 4P Balance:** 62.2 → 🟠 ** 70.3** (`⬆️ +8.1`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 30.9 → 32.7 (`⬆️ +1.8`) pkt
  - `4p-no-cienie`: 51.3 → 71.0 (`⬆️ +19.7`) pkt
  - `4p-no-kabala`: 59.5 → 81.6 (`⬆️ +22.1`) pkt
  - `4p-no-korona`: 83.6 pkt
  - `4p-no-oficjum`: 85.7 → 82.7 (`-3.0`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 16.4 → 19.9 (`⬆️ +3.5`) pkt
- **Tryb 4-osobowy (4p Avg):** 33.0 → 30.8 (`-2.2`) pkt
- **Tryb 5-osobowy (5p Avg):** 19.0 → 23.5 (`⬆️ +4.5`) pkt
- **Global Game Balance Score:** 22.8 → 🔴 ** 24.7** (`⬆️ +1.9`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `4.79 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `3.4%` (norma: <30%)
  - **Autodafé / partię:** `1.72`
  - **Oskarżenia / partię:** `4.96`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_KB-09_HERESY_MINUS1` | KB-09 (Dekret Królewski): heresy 1 → 0 | 62.2 → 🟠 ** 70.3** (`⬆️ +8.1`) | 0.0% | 3.4% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KB-12_COST_MINUS1` | KB-12 (Szantaż Salonowy): cost 1 → 0 | 62.2 → 🟠 ** 68.1** (`⬆️ +5.9`) | 0.0% | 2.8% | 🟢 ZYSK |
| #3 | `L3_KB-12_GOLD_SET1` | KB-12 (Szantaż Salonowy): dodaj gold = 1 | 62.2 → 🟠 ** 67.8** (`⬆️ +5.6`) | 0.0% | 2.9% | 🟢 ZYSK |
| #4 | `L3_KB-12_GOLD_PLUS1` | KB-12 (Szantaż Salonowy): gold 0 → 1 | 62.2 → 🟠 ** 67.8** (`⬆️ +5.6`) | 0.0% | 2.9% | 🟢 ZYSK |
| #5 | `L3_KB-08_GOLD_SET1` | KB-08 (Przekupstwo Sędziego): dodaj gold = 1 | 62.2 → 🟠 ** 67.8** (`⬆️ +5.6`) | 0.0% | 3.0% | 🟢 ZYSK |
| #6 | `L3_KB-08_GOLD_PLUS1` | KB-08 (Przekupstwo Sędziego): gold 0 → 1 | 62.2 → 🟠 ** 67.8** (`⬆️ +5.6`) | 0.0% | 3.0% | 🟢 ZYSK |
| #7 | `L1_START_GOLD_PLUS1` | Złoto startowe: 5zł → 6zł | 62.2 → 🟠 ** 67.7** (`⬆️ +5.5`) | 0.0% | 2.2% | 🟢 ZYSK |
| #8 | `L3_KB-05_COST_MINUS1` | KB-05 (List Żelazny): cost 2 → 1 | 62.2 → 🟠 ** 67.6** (`⬆️ +5.4`) | 0.0% | 2.7% | 🟢 ZYSK |
| #9 | `L3_KB-06_GOLD_SET2` | KB-06 (Areszt Królewski): dodaj gold = 2 | 62.2 → 🟠 ** 67.4** (`⬆️ +5.2`) | 0.0% | 3.1% | 🟢 ZYSK |
| #10 | `L3_KB-11_COST_MINUS1` | KB-11 (Tajny Emisariusz): cost 1 → 0 | 62.2 → 🟠 ** 67.3** (`⬆️ +5.1`) | 0.0% | 2.8% | 🟢 ZYSK |
| #11 | `L3_KB-07_GOLD_SET1` | KB-07 (Szantaż Pieczęcią): dodaj gold = 1 | 62.2 → 🟠 ** 66.9** (`⬆️ +4.7`) | 0.0% | 3.0% | 🟢 ZYSK |
| #12 | `L3_KB-07_GOLD_PLUS1` | KB-07 (Szantaż Pieczęcią): gold 0 → 1 | 62.2 → 🟠 ** 66.9** (`⬆️ +4.7`) | 0.0% | 3.0% | 🟢 ZYSK |
| #13 | `L3_KB-02_GOLD_PLUS1` | KB-02 (Pobór Podatków): gold 2 → 3 | 62.2 → 🟠 ** 66.1** (`⬆️ +3.9`) | 0.0% | 2.8% | 🟢 ZYSK |
| #14 | `L3_KB-04_GOLD_SET2` | KB-04 (Faworyt Dworu): dodaj gold = 2 | 62.2 → 🟠 ** 65.8** (`⬆️ +3.6`) | 0.0% | 2.7% | 🟢 ZYSK |
| #15 | `L3_KB-01_GOLD_SET2` | KB-01 (Rozkaz Dworu): dodaj gold = 2 | 62.2 → 🟠 ** 65.3** (`⬆️ +3.1`) | 0.0% | 2.5% | 🟢 ZYSK |
| #16 | `L3_KB-01_TARGET_HERESY_MINUS1` | KB-01 (Rozkaz Dworu): target_heresy 1 → 0 | 62.2 → 🟠 ** 64.9** (`⬆️ +2.7`) | 0.0% | 3.2% | 🟢 ZYSK |
| #17 | `L3_KB-03_GOLD_SET2` | KB-03 (Plotka Dworska): dodaj gold = 2 | 62.2 → 🟠 ** 64.3** (`⬆️ +2.1`) | 0.0% | 2.8% | 🟢 ZYSK |
| #18 | `L3_KB-12_TARGET_HERESY_SET2` | KB-12 (Szantaż Salonowy): dodaj target_heresy = 2 | 62.2 → 🟠 ** 62.5** (`⬆️ +0.3`) | 0.0% | 3.3% | 🟢 ZYSK |
| #19 | `L2_KT_ERA_PLUS1` | Kabała Era: 6 → 7 | 62.2 → 🔴 ** 40.1** (`-22.1`) | 0.0% | 3.5% | ⚪ STRATA/NEUTRALNY |
| #20 | `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 62.2 → 🔴 ** 28.4** (`-33.8`) | 0.0% | 3.1% | ⚪ STRATA/NEUTRALNY |