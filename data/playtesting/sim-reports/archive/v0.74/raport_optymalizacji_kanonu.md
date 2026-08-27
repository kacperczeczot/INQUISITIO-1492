[Strona główna](../../../../../README.md) > [v0.74](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.74 (Iteracja #4, Faza 1D)

**Wersja Poprzednia:** `v0.73` (4P: `95.9 pkt`) → **Nowa Wersja:** `v0.74` (4P: `96.3 pkt`)
**Data:** 2026-08-16 23:30 | **Czas Trwania Iteracji:** 570.4s | **Zysk 4P:** `+0.4 pkt` | **Zysk Global:** `-0.3 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_KT-08_COST_MINUS1` — **KT-08 (Areszt Wiedzy): cost 2 → 1**
- **Opis Modyfikacji:** Karta `kt-08` (Areszt Wiedzy): `cost` → `1`
- **Wynik Kanonu 4P Score:** 95.9 → 🟢 ** 96.3** (`⬆️ +0.4`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 97.7 → 98.2 (`⬆️ +0.5`) pkt
  - `4p-no-cienie`: 96.8 → 96.4 (`-0.4`) pkt
  - `4p-no-kabala`: 97.8 pkt
  - `4p-no-korona`: 93.9 → 95.0 (`⬆️ +1.1`) pkt
  - `4p-no-oficjum`: 93.4 → 94.2 (`⬆️ +0.8`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 65.8 → 65.3 (`-0.5`) pkt
- **Tryb 4-osobowy (4p Avg):** 92.7 → 93.2 (`⬆️ +0.5`) pkt
- **Tryb 5-osobowy (5p Avg):** 71.6 → 70.7 (`-0.9`) pkt
- **Global Game Balance Score:** 76.7 → 🟡 ** 76.4** (`-0.3`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.48 Er`
  - **Deadlocki (Limit Er):** `0.1%` (norma: <5%)
  - **Pas Biedy (Złoto):** `24.6%` (norma: <30%)
  - **Autodafé / partię:** `1.52`
  - **Oskarżenia / partię:** `3.21`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_KT-08_COST_MINUS1` | KT-08 (Areszt Wiedzy): cost 2 → 1 | 95.9 → 🟢 ** 96.3** (`⬆️ +0.4`) | 0.1% | 24.6% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KT-09_COST_MINUS1` | KT-09 (Fragment Kodeksu): cost 2 → 1 | 95.9 → 🟢 ** 96.3** (`⬆️ +0.4`) | 0.1% | 24.6% | 🟢 ZYSK |
| #3 | `L3_CAA-08_GOLD_PLUS1` | CAA-08 (Kaptur Nocy): gold 0 → 1 | 95.9 → 🟢 ** 96.3** (`⬆️ +0.4`) | 0.1% | 24.5% | 🟢 ZYSK |
| #4 | `L3_KT-06_GOLD_PLUS1` | KT-06 (Przesłuchanie Imienia): gold 0 → 1 | 95.9 → 🟢 ** 96.2** (`⬆️ +0.3`) | 0.1% | 24.6% | 🟢 ZYSK |
| #5 | `L4_SEA_ROUTE_ERA5` | Szlak Morski: Era 6 → Era 5 | 95.9 → 🟢 ** 96.2** (`⬆️ +0.3`) | 0.1% | 24.5% | 🟢 ZYSK |
| #6 | `L3_KT-01_GOLD_PLUS1` | KT-01 (Rytuał Przejścia): gold 0 → 1 | 95.9 → 🟢 ** 96.1** (`⬆️ +0.2`) | 0.1% | 24.6% | 🟢 ZYSK |
| #7 | `L3_KT-05_GOLD_PLUS1` | KT-05 (Wskazówka Cyklu): gold 0 → 1 | 95.9 → 🟢 ** 96.0** (`⬆️ +0.1`) | 0.1% | 24.6% | 🟢 ZYSK |
| #8 | `L3_KT-04_COST_PLUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 2 | 🟢 ** 95.9** | 0.1% | 24.6% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 95.9 → 🟢 ** 95.8** (`-0.1`) | 0.1% | 24.7% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_CAA-07_COST_MINUS1` | CAA-07 (Szantaż Bractwa): cost 1 → 0 | 95.9 → 🟢 ** 95.8** (`-0.1`) | 0.1% | 24.5% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 0 → 1 | 95.9 → 🟢 ** 95.7** (`-0.2`) | 0.1% | 24.6% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-04_COST_MINUS1` | CAA-04 (Fałszywy Trop): cost 1 → 0 | 95.9 → 🟢 ** 95.7** (`-0.2`) | 0.1% | 24.5% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_GC-03_HERESY_PLUS1` | GC-03 (Podrzucenie Księgi): heresy 0 → 1 | 95.9 → 🟢 ** 95.6** (`-0.3`) | 0.1% | 24.5% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_CAA-08_COST_MINUS1` | CAA-08 (Kaptur Nocy): cost 2 → 1 | 95.9 → 🟢 ** 95.6** (`-0.3`) | 0.1% | 24.5% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_CAA-09_COST_MINUS1` | CAA-09 (Kurier Relikwii): cost 2 → 1 | 95.9 → 🟢 ** 95.3** (`-0.6`) | 0.1% | 24.5% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_CAA-05_COST_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 2 | 95.9 → 🟢 ** 95.2** (`-0.7`) | 0.1% | 24.7% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_SO-02_COST_MINUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 0 | 95.9 → 🟢 ** 95.0** (`-0.9`) | 0.1% | 24.0% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_SO-07_COST_MINUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 1 | 95.9 → 🟢 ** 95.0** (`-0.9`) | 0.1% | 24.0% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_GC-01_HERESY_MINUS1` | GC-01 (Przekupiony Strażnik): heresy 1 → 0 | 95.9 → 🟢 ** 95.0** (`-0.9`) | 0.1% | 24.5% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_GC-10_HERESY_MINUS1` | GC-10 (Upadek Domu): heresy 1 → 0 | 95.9 → 🟢 ** 94.9** (`-1.0`) | 0.1% | 24.5% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_KB-06_HERESY_PLUS1` | KB-06 (Areszt Królewski): heresy 0 → 1 | 95.9 → 🟢 ** 94.9** (`-1.0`) | 0.1% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_SO-09_COST_MINUS1` | SO-09 (Świadek Koronny): cost 2 → 1 | 95.9 → 🟢 ** 94.9** (`-1.0`) | 0.1% | 24.0% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_CAA-01_GOLD_MINUS1` | CAA-01 (Przejście Podziemiami): gold 1 → 0 | 95.9 → 🟢 ** 94.5** (`-1.4`) | 0.1% | 24.6% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_KT-08_TARGET_HERESY_PLUS1` | KT-08 (Areszt Wiedzy): target_heresy 0 → 1 | 95.9 → 🟢 ** 94.0** (`-1.9`) | 0.1% | 24.3% | ⚪ STRATA/NEUTRALNY |