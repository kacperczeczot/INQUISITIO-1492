[Strona główna](../../../../../README.md) > [v0.73](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.73 (Iteracja #3, Faza 1D)

**Wersja Poprzednia:** `v0.72` (4P: `93.7 pkt`) → **Nowa Wersja:** `v0.73` (4P: `95.9 pkt`)
**Data:** 2026-08-16 23:21 | **Czas Trwania Iteracji:** 547.8s | **Zysk 4P:** `+2.2 pkt` | **Zysk Global:** `+2.2 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_GC-02_GOLD_MINUS1` — **GC-02 (Czarny Rynek): gold 2 → 1**
- **Opis Modyfikacji:** Karta `gc-02` (Czarny Rynek): `gold` → `1`
- **Wynik Kanonu 4P Score:** 93.7 → 🟢 ** 95.9** (`⬆️ +2.2`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 97.7 pkt
  - `4p-no-cienie`: 94.0 → 96.8 (`⬆️ +2.8`) pkt
  - `4p-no-kabala`: 92.7 → 97.8 (`⬆️ +5.1`) pkt
  - `4p-no-korona`: 90.3 → 93.9 (`⬆️ +3.6`) pkt
  - `4p-no-oficjum`: 93.8 → 93.4 (`-0.4`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 64.4 → 65.8 (`⬆️ +1.4`) pkt
- **Tryb 4-osobowy (4p Avg):** 91.2 → 92.7 (`⬆️ +1.5`) pkt
- **Tryb 5-osobowy (5p Avg):** 67.8 → 71.6 (`⬆️ +3.8`) pkt
- **Global Game Balance Score:** 74.5 → 🟡 ** 76.7** (`⬆️ +2.2`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.48 Er`
  - **Deadlocki (Limit Er):** `0.1%` (norma: <5%)
  - **Pas Biedy (Złoto):** `24.6%` (norma: <30%)
  - **Autodafé / partię:** `1.51`
  - **Oskarżenia / partię:** `3.21`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-02_GOLD_MINUS1` | GC-02 (Czarny Rynek): gold 2 → 1 | 93.7 → 🟢 ** 95.9** (`⬆️ +2.2`) | 0.1% | 24.6% | 🌟 ZWYCIĘZCA |
| #2 | `L3_GC-05_COST_PLUS1` | GC-05 (Fałszywy Świadek): cost 0 → 1 | 93.7 → 🟢 ** 95.0** (`⬆️ +1.3`) | 0.1% | 24.2% | 🟢 ZYSK |
| #3 | `L3_GC-03_HERESY_PLUS1` | GC-03 (Podrzucenie Księgi): heresy 0 → 1 | 93.7 → 🟢 ** 94.9** (`⬆️ +1.2`) | 0.1% | 24.1% | 🟢 ZYSK |
| #4 | `L3_GC-02_COST_PLUS1` | GC-02 (Czarny Rynek): cost 2 → 3 | 93.7 → 🟢 ** 94.7** (`⬆️ +1.0`) | 0.1% | 24.6% | 🟢 ZYSK |
| #5 | `L3_GC-01_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): heresy 1 → 2 | 93.7 → 🟢 ** 94.6** (`⬆️ +0.9`) | 0.1% | 24.0% | 🟢 ZYSK |
| #6 | `L3_SO-07_COST_MINUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 1 | 93.7 → 🟢 ** 94.4** (`⬆️ +0.7`) | 0.1% | 23.5% | 🟢 ZYSK |
| #7 | `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 0 → 1 | 93.7 → 🟢 ** 94.1** (`⬆️ +0.4`) | 0.1% | 24.1% | 🟢 ZYSK |
| #8 | `L3_SO-03_COST_MINUS1` | SO-03 (Podejrzenie): cost 2 → 1 | 93.7 → 🟢 ** 94.0** (`⬆️ +0.3`) | 0.1% | 23.4% | 🟢 ZYSK |
| #9 | `L4_SEA_ROUTE_ERA5` | Szlak Morski: Era 6 → Era 5 | 93.7 → 🟢 ** 93.6** (`-0.1`) | 0.1% | 24.0% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_KT-04_COST_PLUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 2 | 93.7 → 🟢 ** 93.6** (`-0.1`) | 0.1% | 24.1% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_KT-01_GOLD_PLUS1` | KT-01 (Rytuał Przejścia): gold 0 → 1 | 93.7 → 🟢 ** 93.2** (`-0.5`) | 0.1% | 24.1% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_SO-02_COST_MINUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 0 | 93.7 → 🟢 ** 93.1** (`-0.6`) | 0.1% | 23.5% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 93.7 → 🟢 ** 93.1** (`-0.6`) | 0.1% | 24.2% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_GC-07_TARGET_HERESY_PLUS1` | GC-07 (Skrytobójstwo): target_heresy 0 → 1 | 93.7 → 🟢 ** 93.1** (`-0.6`) | 0.1% | 24.3% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_KT-05_GOLD_PLUS1` | KT-05 (Wskazówka Cyklu): gold 0 → 1 | 93.7 → 🟢 ** 93.1** (`-0.6`) | 0.1% | 24.1% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_SO-06_GOLD_PLUS1` | SO-06 (Areszt Trybunalski): gold 0 → 1 | 93.7 → 🟢 ** 93.0** (`-0.7`) | 0.1% | 23.6% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_SO-08_GOLD_PLUS1` | SO-08 (Nasłanie Inkwizytora): gold 0 → 1 | 93.7 → 🟢 ** 92.7** (`-1.0`) | 0.1% | 23.5% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_KB-06_HERESY_PLUS1` | KB-06 (Areszt Królewski): heresy 0 → 1 | 93.7 → 🟢 ** 92.6** (`-1.1`) | 0.1% | 23.9% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_KT-05_COST_PLUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 2 | 93.7 → 🟢 ** 92.5** (`-1.2`) | 0.1% | 24.0% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_KB-05_HERESY_PLUS1` | KB-05 (List Żelazny): heresy 0 → 1 | 93.7 → 🟢 ** 92.3** (`-1.4`) | 0.1% | 23.9% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 93.7 → 🟢 ** 91.7** (`-2.0`) | 0.1% | 25.1% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_KT-05_TARGET_HERESY_PLUS1` | KT-05 (Wskazówka Cyklu): target_heresy 0 → 1 | 93.7 → 🟡 ** 89.6** (`-4.1`) | 0.1% | 23.7% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_GC-08_TARGET_HERESY_PLUS1` | GC-08 (Zatrute Złoto): target_heresy 1 → 2 | 93.7 → 🟡 ** 89.6** (`-4.1`) | 0.1% | 23.9% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_KB-08_COST_PLUS1` | KB-08 (Przekupstwo Sędziego): cost 2 → 3 | 93.7 → 🟡 ** 89.1** (`-4.6`) | 0.1% | 24.3% | ⚪ STRATA/NEUTRALNY |