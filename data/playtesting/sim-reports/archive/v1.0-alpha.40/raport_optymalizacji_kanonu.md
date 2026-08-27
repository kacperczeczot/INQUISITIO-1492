[Strona główna](../../../../../README.md) > [v1.0-alpha.40](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.40 (Iteracja #5, Faza 2D)

**Wersja Poprzednia:** `v1.0-alpha.39` (4P: `69.1 pkt`) → **Nowa Wersja:** `v1.0-alpha.40` (4P: `71.3 pkt`)
**Data:** 2026-08-23 04:43 | **Czas Trwania Iteracji:** 831.3s | **Zysk 4P:** `+2.2 pkt` | **Zysk Global:** `+1.1 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (2D):** `L3_CAA-04_GOLD_SET3__L3_GC-02_HERESY_MINUS1` — **CAA-04 (Fałszywy Trop): dodaj gold = 3 + GC-02 (Czarny Rynek): heresy 1 → 0**
- **Opis Modyfikacji:** Karta `caa-04` (Fałszywy Trop): `gold` → `3` + Karta `gc-02` (Czarny Rynek): `heresy` → `0`
- **Wynik Kanonu 4P Balance:** 69.1 → 🟠 ** 71.3** (`⬆️ +2.2`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 56.3 pkt
  - `4p-no-cienie`: 68.0 → 76.3 (`⬆️ +8.3`) pkt
  - `4p-no-kabala`: 69.9 → 72.1 (`⬆️ +2.2`) pkt
  - `4p-no-korona`: 73.4 → 78.9 (`⬆️ +5.5`) pkt
  - `4p-no-oficjum`: 78.1 → 73.1 (`-5.0`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 27.4 → 23.6 (`-3.8`) pkt
- **Tryb 4-osobowy (4p Avg):** 69.9 → 73.8 (`⬆️ +3.9`) pkt
- **Tryb 5-osobowy (5p Avg):** 19.0 → 22.4 (`⬆️ +3.4`) pkt
- **Global Game Balance Score:** 38.8 → 🔴 ** 39.9** (`⬆️ +1.1`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `4.83 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `3.5%` (norma: <30%)
  - **Autodafé / partię:** `1.59`
  - **Oskarżenia / partię:** `4.69`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-04_GOLD_SET3__L3_GC-02_HERESY_MINUS1` | CAA-04 (Fałszywy Trop): dodaj gold = 3 + GC-02 (Czarny Rynek): heresy 1 → 0 | 69.1 → 🟠 ** 71.3** (`⬆️ +2.2`) | 0.0% | 3.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KT-04_GOLD_SET1__L3_CAA-07_TARGET_HERESY_PLUS1` | KT-04 (Zwierciadło Herezji): dodaj gold = 1 + CAA-07 (Szantaż Bractwa): target_heresy 0 → 1 | 69.1 → 🟠 ** 70.1** (`⬆️ +1.0`) | 0.0% | 3.4% | 🟢 ZYSK |
| #3 | `L3_KT-04_GOLD_SET1__L3_CAA-07_TARGET_HERESY_SET1` | KT-04 (Zwierciadło Herezji): dodaj gold = 1 + CAA-07 (Szantaż Bractwa): dodaj target_heresy = 1 | 69.1 → 🟠 ** 70.1** (`⬆️ +1.0`) | 0.0% | 3.4% | 🟢 ZYSK |
| #4 | `L3_KT-11_TARGET_HERESY_SET2__L3_CAA-09_GOLD_PLUS1` | KT-11 (Medytacja Sefirot): dodaj target_heresy = 2 + CAA-09 (Kurier Relikwii): gold 0 → 1 | 69.1 → 🟠 ** 69.8** (`⬆️ +0.7`) | 0.0% | 3.4% | 🟢 ZYSK |
| #5 | `L3_KT-11_TARGET_HERESY_SET2__L3_CAA-09_GOLD_SET1` | KT-11 (Medytacja Sefirot): dodaj target_heresy = 2 + CAA-09 (Kurier Relikwii): dodaj gold = 1 | 69.1 → 🟠 ** 69.8** (`⬆️ +0.7`) | 0.0% | 3.4% | 🟢 ZYSK |
| #6 | `L3_CAA-04_GOLD_SET3__L3_GC-06_COST_PLUS1` | CAA-04 (Fałszywy Trop): dodaj gold = 3 + GC-06 (Szantaż): cost 2 → 3 | 69.1 → 🟠 ** 69.2** (`⬆️ +0.1`) | 0.0% | 3.5% | 🟢 ZYSK |
| #7 | `L3_KT-11_TARGET_HERESY_SET2__L3_CAA-07_TARGET_HERESY_SET1` | KT-11 (Medytacja Sefirot): dodaj target_heresy = 2 + CAA-07 (Szantaż Bractwa): dodaj target_heresy = 1 | 🟠 ** 69.1** | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_KT-11_TARGET_HERESY_SET2__L3_CAA-07_TARGET_HERESY_PLUS1` | KT-11 (Medytacja Sefirot): dodaj target_heresy = 2 + CAA-07 (Szantaż Bractwa): target_heresy 0 → 1 | 🟠 ** 69.1** | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_KT-11_TARGET_HERESY_SET2__L3_CAA-08_TARGET_HERESY_MINUS1` | KT-11 (Medytacja Sefirot): dodaj target_heresy = 2 + CAA-08 (Kaptur Nocy): target_heresy 2 → 1 | 69.1 → 🟠 ** 69.0** (`-0.1`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_KT-11_TARGET_HERESY_SET2__L3_CAA-01_HERESY_PLUS1` | KT-11 (Medytacja Sefirot): dodaj target_heresy = 2 + CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 69.1 → 🟠 ** 68.7** (`-0.4`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_KT-11_TARGET_HERESY_SET2__L3_CAA-01_HERESY_SET1` | KT-11 (Medytacja Sefirot): dodaj target_heresy = 2 + CAA-01 (Przejście Podziemiami): dodaj heresy = 1 | 69.1 → 🟠 ** 68.7** (`-0.4`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_KT-11_TARGET_HERESY_SET2__L3_CAA-02_TARGET_HERESY_SET1` | KT-11 (Medytacja Sefirot): dodaj target_heresy = 2 + CAA-02 (Złoto z Kryjówki): dodaj target_heresy = 1 | 69.1 → 🟠 ** 68.1** (`-1.0`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_KT-11_TARGET_HERESY_SET2__L3_CAA-02_TARGET_HERESY_PLUS1` | KT-11 (Medytacja Sefirot): dodaj target_heresy = 2 + CAA-02 (Złoto z Kryjówki): target_heresy 0 → 1 | 69.1 → 🟠 ** 68.1** (`-1.0`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_KT-11_TARGET_HERESY_SET2__L3_CAA-08_HERESY_PLUS1` | KT-11 (Medytacja Sefirot): dodaj target_heresy = 2 + CAA-08 (Kaptur Nocy): heresy 0 → 1 | 69.1 → 🟠 ** 67.7** (`-1.4`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_KT-11_TARGET_HERESY_SET2__L3_CAA-08_HERESY_SET1` | KT-11 (Medytacja Sefirot): dodaj target_heresy = 2 + CAA-08 (Kaptur Nocy): dodaj heresy = 1 | 69.1 → 🟠 ** 67.7** (`-1.4`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_KT-11_TARGET_HERESY_SET2__L3_CAA-06_GOLD_SET3` | KT-11 (Medytacja Sefirot): dodaj target_heresy = 2 + CAA-06 (Ucieczka z Lochów): dodaj gold = 3 | 69.1 → 🟠 ** 67.4** (`-1.7`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_KT-11_TARGET_HERESY_SET2__L3_CAA-09_TARGET_HERESY_PLUS1` | KT-11 (Medytacja Sefirot): dodaj target_heresy = 2 + CAA-09 (Kurier Relikwii): target_heresy 0 → 1 | 69.1 → 🟠 ** 67.1** (`-2.0`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_CAA-04_GOLD_SET3__L1_THRESHOLD_MINUS1` | CAA-04 (Fałszywy Trop): dodaj gold = 3 + Próg Oskarżenia: 7 → 6 | 69.1 → 🟠 ** 66.2** (`-2.9`) | 0.0% | 3.1% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_KT-04_GOLD_SET1__L3_CAA-09_HERESY_SET2` | KT-04 (Zwierciadło Herezji): dodaj gold = 1 + CAA-09 (Kurier Relikwii): dodaj heresy = 2 | 69.1 → 🔴 ** 59.5** (`-9.6`) | 0.0% | 3.2% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_KT-11_TARGET_HERESY_SET2__L3_CAA-09_HERESY_SET2` | KT-11 (Medytacja Sefirot): dodaj target_heresy = 2 + CAA-09 (Kurier Relikwii): dodaj heresy = 2 | 69.1 → 🔴 ** 57.5** (`-11.6`) | 0.0% | 3.3% | ⚪ STRATA/NEUTRALNY |