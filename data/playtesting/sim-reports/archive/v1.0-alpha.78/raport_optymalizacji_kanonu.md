[Strona główna](../../../../../README.md) > [v1.0-alpha.78](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.78 (Iteracja #12, Faza 2D)

**Wersja Poprzednia:** `v1.0-alpha.77` (4P: `83.3 pkt`) → **Nowa Wersja:** `v1.0-alpha.78` (4P: `84.9 pkt`)
**Data:** 2026-08-24 18:13 | **Czas Trwania Iteracji:** 1156.3s | **Zysk 4P:** `+1.6 pkt` | **Zysk Global:** `-0.2 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (2D):** `L3_GC-04_TARGET_HERESY_MINUS1__L3_CAA-05_TARGET_HERESY_PLUS1` — **GC-04 (Informator): target_heresy 1 → 0 + CAA-05 (Ukryty Kurier): target_heresy 2 → 3**
- **Opis Modyfikacji:** Karta `gc-04` (Informator): `target_heresy` → `0` + Karta `caa-05` (Ukryty Kurier): `target_heresy` → `3`
- **Wynik Kanonu 4P Balance:** 83.3 → 🟡 ** 84.9** (`⬆️ +1.6`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 93.7 → 94.9 (`⬆️ +1.2`) pkt
  - `4p-no-cienie`: 69.1 → 72.8 (`⬆️ +3.7`) pkt
  - `4p-no-kabala`: 98.7 → 97.5 (`-1.2`) pkt
  - `4p-no-korona`: 89.0 → 88.2 (`-0.8`) pkt
  - `4p-no-oficjum`: 65.8 → 71.3 (`⬆️ +5.5`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 30.2 → 29.1 (`-1.1`) pkt
- **Tryb 4-osobowy (4p Avg):** 80.9 → 79.1 (`-1.8`) pkt
- **Tryb 5-osobowy (5p Avg):** 13.9 → 16.3 (`⬆️ +2.4`) pkt
- **Global Game Balance Score:** 41.7 → 🔴 ** 41.5** (`-0.2`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.78 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.2%` (norma: <30%)
  - **Autodafé / partię:** `1.54`
  - **Oskarżenia / partię:** `6.92`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-04_TARGET_HERESY_MINUS1__L3_CAA-05_TARGET_HERESY_PLUS1` | GC-04 (Informator): target_heresy 1 → 0 + CAA-05 (Ukryty Kurier): target_heresy 2 → 3 | 83.3 → 🟡 ** 84.9** (`⬆️ +1.6`) | 0.0% | 4.2% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KB-03_COST_MINUS1__L3_CAA-04_TARGET_HERESY_PLUS1` | KB-03 (Plotka Dworska): cost 1 → 0 + CAA-04 (Fałszywy Trop): target_heresy 1 → 2 | 83.3 → 🟡 ** 84.5** (`⬆️ +1.2`) | 0.0% | 3.4% | 🟢 ZYSK |
| #3 | `L3_SO-12_HERESY_SET2__L3_CAA-08_TARGET_HERESY_MINUS1` | SO-12 (Straż Trybunalska): dodaj heresy = 2 + CAA-08 (Kaptur Nocy): target_heresy 2 → 1 | 83.3 → 🟡 ** 84.3** (`⬆️ +1.0`) | 0.0% | 4.5% | 🟢 ZYSK |
| #4 | `L3_SO-12_HERESY_SET2__L3_CAA-06_TARGET_HERESY_MINUS1` | SO-12 (Straż Trybunalska): dodaj heresy = 2 + CAA-06 (Ucieczka z Lochów): target_heresy 2 → 1 | 83.3 → 🟡 ** 83.7** (`⬆️ +0.4`) | 0.0% | 4.4% | 🟢 ZYSK |
| #5 | `L3_GC-07_HERESY_SET1__L3_CAA-05_TARGET_HERESY_PLUS1` | GC-07 (Skrytobójstwo): dodaj heresy = 1 + CAA-05 (Ukryty Kurier): target_heresy 2 → 3 | 83.3 → 🟡 ** 83.4** (`⬆️ +0.1`) | 0.0% | 4.2% | 🟢 ZYSK |
| #6 | `L3_GC-07_HERESY_PLUS1__L3_CAA-05_TARGET_HERESY_PLUS1` | GC-07 (Skrytobójstwo): heresy 0 → 1 + CAA-05 (Ukryty Kurier): target_heresy 2 → 3 | 83.3 → 🟡 ** 83.4** (`⬆️ +0.1`) | 0.0% | 4.2% | 🟢 ZYSK |
| #7 | `L3_KB-03_COST_MINUS1__L3_CAA-05_TARGET_HERESY_PLUS1` | KB-03 (Plotka Dworska): cost 1 → 0 + CAA-05 (Ukryty Kurier): target_heresy 2 → 3 | 83.3 → 🟡 ** 82.7** (`-0.6`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_SO-12_HERESY_SET2__L3_CAA-09_TARGET_HERESY_SET1` | SO-12 (Straż Trybunalska): dodaj heresy = 2 + CAA-09 (Kurier Relikwii): dodaj target_heresy = 1 | 83.3 → 🟡 ** 82.1** (`-1.2`) | 0.0% | 4.4% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_GC-02_TARGET_HERESY_SET1__L3_CAA-10_GOLD_SET2` | GC-02 (Czarny Rynek): dodaj target_heresy = 1 + CAA-10 (Echo Alhambry): dodaj gold = 2 | 83.3 → 🟡 ** 81.9** (`-1.4`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_GC-02_TARGET_HERESY_PLUS1__L3_CAA-10_GOLD_SET2` | GC-02 (Czarny Rynek): target_heresy 0 → 1 + CAA-10 (Echo Alhambry): dodaj gold = 2 | 83.3 → 🟡 ** 81.9** (`-1.4`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_GC-02_TARGET_HERESY_SET1__L3_CAA-10_COST_MINUS1` | GC-02 (Czarny Rynek): dodaj target_heresy = 1 + CAA-10 (Echo Alhambry): cost 3 → 2 | 83.3 → 🟡 ** 81.6** (`-1.7`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_GC-02_TARGET_HERESY_PLUS1__L3_CAA-10_COST_MINUS1` | GC-02 (Czarny Rynek): target_heresy 0 → 1 + CAA-10 (Echo Alhambry): cost 3 → 2 | 83.3 → 🟡 ** 81.6** (`-1.7`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_GC-02_TARGET_HERESY_PLUS1__L3_CAA-03_HERESY_MINUS1` | GC-02 (Czarny Rynek): target_heresy 0 → 1 + CAA-03 (Cień na Rynku): heresy 1 → 0 | 83.3 → 🟡 ** 80.3** (`-3.0`) | 0.0% | 4.3% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_KB-03_COST_MINUS1__L3_CAA-10_TARGET_HERESY_SET1` | KB-03 (Plotka Dworska): cost 1 → 0 + CAA-10 (Echo Alhambry): dodaj target_heresy = 1 | 83.3 → 🟡 ** 79.9** (`-3.4`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_KB-03_COST_MINUS1__L3_CAA-10_TARGET_HERESY_PLUS1` | KB-03 (Plotka Dworska): cost 1 → 0 + CAA-10 (Echo Alhambry): target_heresy 0 → 1 | 83.3 → 🟡 ** 79.9** (`-3.4`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_KB-08_GOLD_SET2__L3_CAA-10_TARGET_HERESY_PLUS1` | KB-08 (Przekupstwo Sędziego): dodaj gold = 2 + CAA-10 (Echo Alhambry): target_heresy 0 → 1 | 83.3 → 🟡 ** 79.5** (`-3.8`) | 0.0% | 4.0% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_SO-12_HERESY_SET2__L3_CAA-09_TARGET_HERESY_SET2` | SO-12 (Straż Trybunalska): dodaj heresy = 2 + CAA-09 (Kurier Relikwii): dodaj target_heresy = 2 | 83.3 → 🟡 ** 78.6** (`-4.7`) | 0.0% | 4.4% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_GC-02_TARGET_HERESY_SET1__L3_CAA-10_GOLD_SET3` | GC-02 (Czarny Rynek): dodaj target_heresy = 1 + CAA-10 (Echo Alhambry): dodaj gold = 3 | 83.3 → 🟡 ** 77.8** (`-5.5`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_GC-02_TARGET_HERESY_PLUS1__L3_CAA-10_GOLD_SET3` | GC-02 (Czarny Rynek): target_heresy 0 → 1 + CAA-10 (Echo Alhambry): dodaj gold = 3 | 83.3 → 🟡 ** 77.8** (`-5.5`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_SO-06_TARGET_HERESY_PLUS1__L1_START_GOLD_PLUS1` | SO-06 (Areszt Trybunalski): target_heresy 1 → 2 + Złoto startowe: 4zł → 5zł | 83.3 → 🟡 ** 84.5** (`⬆️ +1.2`) | 0.0% | 3.3% | 🟢 ZYSK |