[Strona główna](../../../../../README.md) > [v1.0-alpha.65](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.65 (Iteracja #4, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.64` (4P: `69.6 pkt`) → **Nowa Wersja:** `v1.0-alpha.65` (4P: `71.5 pkt`)
**Data:** 2026-08-24 07:16 | **Czas Trwania Iteracji:** 429.6s | **Zysk 4P:** `+1.9 pkt` | **Zysk Global:** `-9.9 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L4_INQUISITOR_SPEED2` — **Inkwizytor Patrol: ruch 1 → 2 (podwojenie)**
- **Opis Modyfikacji:** Wariant: Prędkość Ruchu Inkwizytora = 2
- **Wynik Kanonu 4P Balance:** 69.6 → 🟠 ** 71.5** (`⬆️ +1.9`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 74.2 → 82.0 (`⬆️ +7.8`) pkt
  - `4p-no-cienie`: 51.7 → 53.4 (`⬆️ +1.7`) pkt
  - `4p-no-kabala`: 67.0 → 77.1 (`⬆️ +10.1`) pkt
  - `4p-no-korona`: 97.0 → 90.0 (`-7.0`) pkt
  - `4p-no-oficjum`: 58.1 → 55.1 (`-3.0`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 32.5 → 28.9 (`-3.6`) pkt
- **Tryb 4-osobowy (4p Avg):** 72.7 → 47.2 (`-25.5`) pkt
- **Tryb 5-osobowy (5p Avg):** 2.8 → 2.2 (`-0.6`) pkt
- **Global Game Balance Score:** 36.0 → 🔴 ** 26.1** (`-9.9`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.78 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `5.3%` (norma: <30%)
  - **Autodafé / partię:** `1.39`
  - **Oskarżenia / partię:** `6.83`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L4_INQUISITOR_SPEED2` | Inkwizytor Patrol: ruch 1 → 2 (podwojenie) | 69.6 → 🟠 ** 71.5** (`⬆️ +1.9`) | 0.0% | 5.3% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-09_HERESY_SET2` | SO-09 (Świadek Koronny): dodaj heresy = 2 | 69.6 → 🟠 ** 71.4** (`⬆️ +1.8`) | 0.0% | 5.3% | 🟢 ZYSK |
| #3 | `L3_KB-11_COST_PLUS1` | KB-11 (Tajny Emisariusz): cost 1 → 2 | 69.6 → 🟠 ** 71.2** (`⬆️ +1.6`) | 0.0% | 5.9% | 🟢 ZYSK |
| #4 | `L3_SO-09_HERESY_PLUS1` | SO-09 (Świadek Koronny): heresy 0 → 1 | 69.6 → 🟠 ** 71.1** (`⬆️ +1.5`) | 0.0% | 5.3% | 🟢 ZYSK |
| #5 | `L3_SO-09_HERESY_SET1` | SO-09 (Świadek Koronny): dodaj heresy = 1 | 69.6 → 🟠 ** 71.1** (`⬆️ +1.5`) | 0.0% | 5.3% | 🟢 ZYSK |
| #6 | `L3_KB-08_COST_MINUS1` | KB-08 (Przekupstwo Sędziego): cost 3 → 2 | 69.6 → 🟠 ** 70.8** (`⬆️ +1.2`) | 0.0% | 5.3% | 🟢 ZYSK |
| #7 | `L3_KT-04_TARGET_HERESY_MINUS1` | KT-04 (Zwierciadło Herezji): target_heresy 1 → 0 | 69.6 → 🟠 ** 70.5** (`⬆️ +0.9`) | 0.0% | 5.3% | 🟢 ZYSK |
| #8 | `L3_KT-04_COST_PLUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 2 | 69.6 → 🟠 ** 69.8** (`⬆️ +0.2`) | 0.0% | 5.3% | 🟢 ZYSK |
| #9 | `L3_KT-11_COST_PLUS1` | KT-11 (Medytacja Sefirot): cost 2 → 3 | 69.6 → 🟠 ** 68.9** (`-0.7`) | 0.0% | 5.2% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_CAA-08_TARGET_HERESY_MINUS1` | CAA-08 (Kaptur Nocy): target_heresy 2 → 1 | 69.6 → 🟠 ** 67.6** (`-2.0`) | 0.0% | 5.2% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_KB-02_COST_PLUS1` | KB-02 (Pobór Podatków): cost 1 → 2 | 69.6 → 🟠 ** 71.4** (`⬆️ +1.8`) | 0.0% | 6.5% | 🟢 ZYSK |
| #12 | `L3_KB-01_HERESY_MINUS1` | KB-01 (Rozkaz Dworu): heresy 1 → 0 | 69.6 → 🟠 ** 70.4** (`⬆️ +0.8`) | 0.0% | 5.3% | 🟢 ZYSK |
| #13 | `L3_KB-04_HERESY_SET2` | KB-04 (Faworyt Dworu): dodaj heresy = 2 | 69.6 → 🟠 ** 69.9** (`⬆️ +0.3`) | 0.0% | 5.5% | 🟢 ZYSK |
| #14 | `L3_CAA-10_GOLD_SET2` | CAA-10 (Echo Alhambry): dodaj gold = 2 | 69.6 → 🟠 ** 66.1** (`-3.5`) | 0.0% | 5.2% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_KB-04_TARGET_HERESY_SET1` | KB-04 (Faworyt Dworu): dodaj target_heresy = 1 | 69.6 → 🟠 ** 72.6** (`⬆️ +3.0`) | 0.0% | 5.3% | 🟢 ZYSK |
| #16 | `L3_KB-04_TARGET_HERESY_PLUS1` | KB-04 (Faworyt Dworu): target_heresy 0 → 1 | 69.6 → 🟠 ** 72.6** (`⬆️ +3.0`) | 0.0% | 5.3% | 🟢 ZYSK |
| #17 | `L4_TIME_DECK_EVERY_2ERAS` | Edykty Czasu: co 1 Erę → co 2 Ery | 69.6 → 🟠 ** 71.3** (`⬆️ +1.7`) | 0.0% | 5.7% | 🟢 ZYSK |
| #18 | `L3_KB-07_TARGET_HERESY_SET2` | KB-07 (Szantaż Pieczęcią): dodaj target_heresy = 2 | 69.6 → 🟠 ** 70.1** (`⬆️ +0.5`) | 0.0% | 5.3% | 🟢 ZYSK |
| #19 | `L3_CAA-04_TARGET_HERESY_PLUS1` | CAA-04 (Fałszywy Trop): target_heresy 1 → 2 | 69.6 → 🟠 ** 69.2** (`-0.4`) | 0.0% | 5.3% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_GC-02_TARGET_HERESY_SET2` | GC-02 (Czarny Rynek): dodaj target_heresy = 2 | 69.6 → 🟠 ** 68.0** (`-1.6`) | 0.0% | 5.3% | ⚪ STRATA/NEUTRALNY |