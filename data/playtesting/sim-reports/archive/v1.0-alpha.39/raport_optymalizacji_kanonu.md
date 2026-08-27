[Strona główna](../../../../../README.md) > [v1.0-alpha.39](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.39 (Iteracja #4, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.38` (4P: `65.2 pkt`) → **Nowa Wersja:** `v1.0-alpha.39` (4P: `68.9 pkt`)
**Data:** 2026-08-23 04:20 | **Czas Trwania Iteracji:** 613.5s | **Zysk 4P:** `+3.7 pkt` | **Zysk Global:** `+2.1 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_GC-09_HERESY_MINUS1` — **GC-09 (Lista Dłużników): heresy 1 → 0**
- **Opis Modyfikacji:** Karta `gc-09` (Lista Dłużników): `heresy` → `0`
- **Wynik Kanonu 4P Balance:** 65.2 → 🟠 ** 68.9** (`⬆️ +3.7`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 59.9 pkt
  - `4p-no-cienie`: 57.9 → 71.3 (`⬆️ +13.4`) pkt
  - `4p-no-kabala`: 76.6 → 74.4 (`-2.2`) pkt
  - `4p-no-korona`: 59.3 → 67.5 (`⬆️ +8.2`) pkt
  - `4p-no-oficjum`: 72.5 → 71.6 (`-0.9`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 25.5 → 27.4 (`⬆️ +1.9`) pkt
- **Tryb 4-osobowy (4p Avg):** 67.3 → 69.9 (`⬆️ +2.6`) pkt
- **Tryb 5-osobowy (5p Avg):** 17.4 → 19.0 (`⬆️ +1.6`) pkt
- **Global Game Balance Score:** 36.7 → 🔴 ** 38.8** (`⬆️ +2.1`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `4.78 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `3.4%` (norma: <30%)
  - **Autodafé / partię:** `1.57`
  - **Oskarżenia / partię:** `4.66`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-09_HERESY_MINUS1` | GC-09 (Lista Dłużników): heresy 1 → 0 | 65.2 → 🟠 ** 68.9** (`⬆️ +3.7`) | 0.0% | 3.4% | 🌟 ZWYCIĘZCA |
| #2 | `L3_GC-08_HERESY_MINUS1` | GC-08 (Zatrute Złoto): heresy 1 → 0 | 65.2 → 🟠 ** 68.7** (`⬆️ +3.5`) | 0.0% | 3.4% | 🟢 ZYSK |
| #3 | `L3_KT-05_HERESY_MINUS1` | KT-05 (Wskazówka Cyklu): heresy 1 → 0 | 65.2 → 🟠 ** 67.7** (`⬆️ +2.5`) | 0.0% | 3.4% | 🟢 ZYSK |
| #4 | `L3_CAA-06_GOLD_SET3` | CAA-06 (Ucieczka z Lochów): dodaj gold = 3 | 65.2 → 🟠 ** 67.7** (`⬆️ +2.5`) | 0.0% | 3.4% | 🟢 ZYSK |
| #5 | `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 1 → 2 | 65.2 → 🟠 ** 67.6** (`⬆️ +2.4`) | 0.0% | 3.4% | 🟢 ZYSK |
| #6 | `L3_GC-10_COST_PLUS1` | GC-10 (Upadek Domu): cost 4 → 5 | 65.2 → 🟠 ** 67.3** (`⬆️ +2.1`) | 0.0% | 3.4% | 🟢 ZYSK |
| #7 | `L3_CAA-03_TARGET_HERESY_SET2` | CAA-03 (Cień na Rynku): dodaj target_heresy = 2 | 65.2 → 🟠 ** 66.3** (`⬆️ +1.1`) | 0.0% | 3.4% | 🟢 ZYSK |
| #8 | `L3_CAA-03_TARGET_HERESY_PLUS1` | CAA-03 (Cień na Rynku): target_heresy 0 → 1 | 65.2 → 🟠 ** 66.0** (`⬆️ +0.8`) | 0.0% | 3.4% | 🟢 ZYSK |
| #9 | `L3_KT-12_GOLD_SET3` | KT-12 (Strażnik Archiwum): dodaj gold = 3 | 65.2 → 🟠 ** 65.9** (`⬆️ +0.7`) | 0.0% | 3.3% | 🟢 ZYSK |
| #10 | `L3_GC-07_GOLD_SET3` | GC-07 (Skrytobójstwo): dodaj gold = 3 | 65.2 → 🟠 ** 65.8** (`⬆️ +0.6`) | 0.0% | 3.4% | 🟢 ZYSK |
| #11 | `L3_GC-04_GOLD_SET3` | GC-04 (Informator): dodaj gold = 3 | 65.2 → 🟠 ** 65.6** (`⬆️ +0.4`) | 0.0% | 3.4% | 🟢 ZYSK |
| #12 | `L3_SO-07_COST_MINUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 1 | 65.2 → 🟠 ** 65.6** (`⬆️ +0.4`) | 0.0% | 3.4% | 🟢 ZYSK |
| #13 | `L3_KT-03_GOLD_SET1` | KT-03 (Zakazana Wiedza): dodaj gold = 1 | 65.2 → 🟠 ** 65.4** (`⬆️ +0.2`) | 0.0% | 3.3% | 🟢 ZYSK |
| #14 | `L3_KT-03_GOLD_PLUS1` | KT-03 (Zakazana Wiedza): gold 0 → 1 | 65.2 → 🟠 ** 65.4** (`⬆️ +0.2`) | 0.0% | 3.3% | 🟢 ZYSK |
| #15 | `L3_KB-11_TARGET_HERESY_MINUS1` | KB-11 (Tajny Emisariusz): target_heresy 1 → 0 | 65.2 → 🟠 ** 65.4** (`⬆️ +0.2`) | 0.0% | 3.4% | 🟢 ZYSK |
| #16 | `L3_KT-06_GOLD_SET3` | KT-06 (Przesłuchanie Imienia): dodaj gold = 3 | 65.2 → 🟠 ** 65.0** (`-0.2`) | 0.0% | 3.3% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_KT-06_GOLD_SET2` | KT-06 (Przesłuchanie Imienia): dodaj gold = 2 | 65.2 → 🟠 ** 64.9** (`-0.3`) | 0.0% | 3.3% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_SO-02_COST_MINUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 0 | 65.2 → 🟠 ** 63.3** (`-1.9`) | 0.0% | 2.9% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_CAA-12_HERESY_SET2` | CAA-12 (Skrytka w Murach): dodaj heresy = 2 | 65.2 → 🟠 ** 62.1** (`-3.1`) | 0.0% | 3.3% | ⚪ STRATA/NEUTRALNY |
| #20 | `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 7 → 6 | 65.2 → 🟠 ** 61.2** (`-4.0`) | 0.0% | 3.1% | ⚪ STRATA/NEUTRALNY |