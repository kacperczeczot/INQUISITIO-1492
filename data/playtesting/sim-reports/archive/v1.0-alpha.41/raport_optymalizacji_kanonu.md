[Strona główna](../../../../../README.md) > [v1.0-alpha.41](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.41 (Iteracja #6, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.40` (4P: `73.7 pkt`) → **Nowa Wersja:** `v1.0-alpha.41` (4P: `75.0 pkt`)
**Data:** 2026-08-23 07:25 | **Czas Trwania Iteracji:** 9717.4s | **Zysk 4P:** `+1.3 pkt` | **Zysk Global:** `-0.6 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_KT-11_TARGET_HERESY_PLUS1` — **KT-11 (Medytacja Sefirot): target_heresy 0 → 1**
- **Opis Modyfikacji:** Karta `kt-11` (Medytacja Sefirot): `target_heresy` → `1`
- **Wynik Kanonu 4P Balance:** 73.7 → 🟡 ** 75.0** (`⬆️ +1.3`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 58.6 → 63.7 (`⬆️ +5.1`) pkt
  - `4p-no-cienie`: 79.2 → 80.4 (`⬆️ +1.2`) pkt
  - `4p-no-kabala`: 73.6 pkt
  - `4p-no-korona`: 83.1 → 80.3 (`-2.8`) pkt
  - `4p-no-oficjum`: 74.0 → 76.8 (`⬆️ +2.8`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 23.6 → 22.8 (`-0.8`) pkt
- **Tryb 4-osobowy (4p Avg):** 73.8 → 72.4 (`-1.4`) pkt
- **Tryb 5-osobowy (5p Avg):** 22.4 → 22.6 (`⬆️ +0.2`) pkt
- **Global Game Balance Score:** 39.9 → 🔴 ** 39.3** (`-0.6`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `4.83 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `3.5%` (norma: <30%)
  - **Autodafé / partię:** `1.59`
  - **Oskarżenia / partię:** `4.68`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_KT-11_TARGET_HERESY_PLUS1` | KT-11 (Medytacja Sefirot): target_heresy 0 → 1 | 73.7 → 🟡 ** 75.0** (`⬆️ +1.3`) | 0.0% | 3.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KT-11_TARGET_HERESY_SET1` | KT-11 (Medytacja Sefirot): dodaj target_heresy = 1 | 73.7 → 🟡 ** 75.0** (`⬆️ +1.3`) | 0.0% | 3.5% | 🟢 ZYSK |
| #3 | `L3_GC-11_HERESY_MINUS1` | GC-11 (Fałszywe Świadectwo Cechu): heresy 2 → 1 | 73.7 → 🟠 ** 74.8** (`⬆️ +1.1`) | 0.0% | 3.5% | 🟢 ZYSK |
| #4 | `L3_SO-09_COST_PLUS1` | SO-09 (Świadek Koronny): cost 1 → 2 | 73.7 → 🟠 ** 74.8** (`⬆️ +1.1`) | 0.0% | 3.7% | 🟢 ZYSK |
| #5 | `L3_KT-04_HERESY_SET2` | KT-04 (Zwierciadło Herezji): dodaj heresy = 2 | 73.7 → 🟠 ** 74.8** (`⬆️ +1.1`) | 0.0% | 3.5% | 🟢 ZYSK |
| #6 | `L3_GC-04_COST_PLUS1` | GC-04 (Informator): cost 1 → 2 | 73.7 → 🟠 ** 74.6** (`⬆️ +0.9`) | 0.0% | 3.5% | 🟢 ZYSK |
| #7 | `L3_KB-10_TARGET_HERESY_SET2` | KB-10 (Pieczęć Korony): dodaj target_heresy = 2 | 73.7 → 🟠 ** 74.3** (`⬆️ +0.6`) | 0.0% | 3.5% | 🟢 ZYSK |
| #8 | `L3_GC-01_HERESY_MINUS1` | GC-01 (Przekupiony Strażnik): heresy 1 → 0 | 73.7 → 🟠 ** 74.3** (`⬆️ +0.6`) | 0.0% | 3.5% | 🟢 ZYSK |
| #9 | `L3_GC-03_TARGET_HERESY_PLUS1` | GC-03 (Podrzucenie Księgi): target_heresy 1 → 2 | 73.7 → 🟠 ** 74.1** (`⬆️ +0.4`) | 0.0% | 3.5% | 🟢 ZYSK |
| #10 | `L3_KT-12_COST_PLUS1` | KT-12 (Strażnik Archiwum): cost 0 → 1 | 73.7 → 🟠 ** 73.4** (`-0.3`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_KT-03_HERESY_PLUS1` | KT-03 (Zakazana Wiedza): heresy 0 → 1 | 73.7 → 🟠 ** 73.1** (`-0.6`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_KT-03_HERESY_SET1` | KT-03 (Zakazana Wiedza): dodaj heresy = 1 | 73.7 → 🟠 ** 73.1** (`-0.6`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #13 | `L1_START_GOLD_MINUS1` | Złoto startowe: 5zł → 4zł | 73.7 → 🟠 ** 72.5** (`-1.2`) | 0.0% | 4.8% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_CAA-07_HERESY_PLUS1` | CAA-07 (Szantaż Bractwa): heresy 0 → 1 | 73.7 → 🟠 ** 72.2** (`-1.5`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_CAA-07_HERESY_SET1` | CAA-07 (Szantaż Bractwa): dodaj heresy = 1 | 73.7 → 🟠 ** 72.2** (`-1.5`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_CAA-07_HERESY_SET2` | CAA-07 (Szantaż Bractwa): dodaj heresy = 2 | 73.7 → 🟠 ** 71.9** (`-1.8`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_KT-05_TARGET_HERESY_PLUS1` | KT-05 (Wskazówka Cyklu): target_heresy 0 → 1 | 73.7 → 🟠 ** 71.3** (`-2.4`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_SO-09_TARGET_HERESY_SET2` | SO-09 (Świadek Koronny): dodaj target_heresy = 2 | 73.7 → 🟠 ** 66.9** (`-6.8`) | 0.0% | 3.2% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_GC-09_HERESY_SET2` | GC-09 (Lista Dłużników): dodaj heresy = 2 | 73.7 → 🟠 ** 66.4** (`-7.3`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #20 | `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 6 → 5 | 73.7 → 🔴 ** 56.8** (`-16.9`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |