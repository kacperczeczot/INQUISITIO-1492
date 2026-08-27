[Strona główna](../../../../../README.md) > [v0.99.7](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.99.7 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v0.99.6` (4P: `61.8 pkt`) → **Nowa Wersja:** `v0.99.7` (4P: `62.7 pkt`)
**Data:** 2026-08-18 02:38 | **Czas Trwania Iteracji:** 634.9s | **Zysk 4P:** `+0.9 pkt` | **Zysk Global:** `0.0 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_KT-10_HERESY_PLUS1` — **KT-10 (Pieczęć Salomona): heresy 1 → 2**
- **Opis Modyfikacji:** Karta `kt-10` (Pieczęć Salomona): `heresy` → `2`
- **Wynik Kanonu 4P Score:** 61.8 → 🟠 ** 62.7** (`⬆️ +0.9`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 43.6 → 49.3 (`⬆️ +5.7`) pkt
  - `4p-no-cienie`: 59.6 → 63.1 (`⬆️ +3.5`) pkt
  - `4p-no-kabala`: 59.7 pkt
  - `4p-no-korona`: 90.8 → 82.9 (`-7.9`) pkt
  - `4p-no-oficjum`: 55.5 → 58.6 (`⬆️ +3.1`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 12.9 → 14.5 (`⬆️ +1.6`) pkt
- **Tryb 4-osobowy (4p Avg):** 63.1 → 64.0 (`⬆️ +0.9`) pkt
- **Tryb 5-osobowy (5p Avg):** 41.2 → 38.7 (`-2.5`) pkt
- **Global Game Balance Score:** 🔴 ** 39.1** pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.18 Er`
  - **Deadlocki (Limit Er):** `2.1%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.4%` (norma: <30%)
  - **Autodafé / partię:** `2.11`
  - **Oskarżenia / partię:** `4.72`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-12_HERESY_MINUS1` | CAA-12 (Skrytka w Murach): heresy 1 → 0 | 61.8 → 🟠 ** 62.8** (`⬆️ +1.0`) | 2.7% | 1.4% | 🟢 ZYSK |
| #2 | `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 61.8 → 🟠 ** 62.5** (`⬆️ +0.7`) | 2.7% | 1.4% | 🟢 ZYSK |
| #3 | `L3_KT-10_HERESY_PLUS1` | KT-10 (Pieczęć Salomona): heresy 1 → 2 | 61.8 → 🟠 ** 62.7** (`⬆️ +0.9`) | 2.1% | 1.4% | 🌟 ZWYCIĘZCA |
| #4 | `L3_KT-06_COST_PLUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 3 | 61.8 → 🟠 ** 62.8** (`⬆️ +1.0`) | 2.3% | 1.4% | 🟢 ZYSK |
| #5 | `L3_GC-09_TARGET_HERESY_PLUS1` | GC-09 (Lista Dłużników): target_heresy 0 → 1 | 61.8 → 🟠 ** 62.1** (`⬆️ +0.3`) | 2.4% | 1.4% | 🟢 ZYSK |
| #6 | `L3_KT-05_COST_PLUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 2 | 61.8 → 🟠 ** 62.0** (`⬆️ +0.2`) | 2.4% | 1.4% | 🟢 ZYSK |
| #7 | `L3_GC-09_COST_MINUS1` | GC-09 (Lista Dłużników): cost 3 → 2 | 61.8 → 🟠 ** 62.3** (`⬆️ +0.5`) | 2.4% | 1.5% | 🟢 ZYSK |
| #8 | `L3_GC-08_COST_MINUS1` | GC-08 (Zatrute Złoto): cost 2 → 1 | 61.8 → 🟠 ** 62.1** (`⬆️ +0.3`) | 2.4% | 1.4% | 🟢 ZYSK |
| #9 | `L4_SEA_ROUTE_ERA_MINUS1` | Szlak Morski: Era 4 → 3 | 61.8 → 🟠 ** 61.9** (`⬆️ +0.1`) | 2.4% | 1.4% | 🟢 ZYSK |
| #10 | `L3_KT-06_GOLD_PLUS1` | KT-06 (Przesłuchanie Imienia): gold 0 → 1 | 61.8 → 🟠 ** 62.1** (`⬆️ +0.3`) | 2.4% | 1.4% | 🟢 ZYSK |
| #11 | `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 61.8 → 🟠 ** 61.9** (`⬆️ +0.1`) | 2.4% | 1.4% | 🟢 ZYSK |
| #12 | `L3_KT-07_COST_MINUS1` | KT-07 (Archiwum Ukryte): cost 1 → 0 | 61.8 → 🟠 ** 62.0** (`⬆️ +0.2`) | 2.4% | 1.4% | 🟢 ZYSK |
| #13 | `L3_CAA-08_COST_PLUS1` | CAA-08 (Kaptur Nocy): cost 1 → 2 | 61.8 → 🟠 ** 61.9** (`⬆️ +0.1`) | 2.4% | 1.4% | 🟢 ZYSK |
| #14 | `L1_MAX_ERAS_MINUS1` | Limit Er: 12 → 11 | 61.8 → 🟠 ** 60.5** (`-1.3`) | 3.5% | 1.4% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_SO-08_COST_MINUS1` | SO-08 (Nasłanie Inkwizytora): cost 1 → 0 | 61.8 → 🟠 ** 62.1** (`⬆️ +0.3`) | 2.3% | 1.4% | 🟢 ZYSK |
| #16 | `L3_SO-08_GOLD_PLUS1` | SO-08 (Nasłanie Inkwizytora): gold 0 → 1 | 61.8 → 🟠 ** 62.1** (`⬆️ +0.3`) | 2.3% | 1.4% | 🟢 ZYSK |
| #17 | `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 61.8 → 🟠 ** 62.0** (`⬆️ +0.2`) | 2.3% | 1.4% | 🟢 ZYSK |
| #18 | `L3_SO-02_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): heresy 0 → 1 | 61.8 → 🟠 ** 61.1** (`-0.7`) | 2.5% | 1.4% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_GC-01_COST_MINUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 0 | 🟠 ** 61.8** | 2.4% | 1.4% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_KT-07_COST_PLUS1` | KT-07 (Archiwum Ukryte): cost 1 → 2 | 61.8 → 🟠 ** 61.9** (`⬆️ +0.1`) | 2.4% | 1.4% | 🟢 ZYSK |
| #21 | `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 2 → 3 | 61.8 → 🟠 ** 61.5** (`-0.3`) | 2.4% | 1.4% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_GC-09_COST_PLUS1` | GC-09 (Lista Dłużników): cost 3 → 4 | 61.8 → 🟠 ** 61.2** (`-0.6`) | 2.4% | 1.9% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_GC-03_GOLD_PLUS1` | GC-03 (Podrzucenie Księgi): gold 0 → 1 | 61.8 → 🟠 ** 62.1** (`⬆️ +0.3`) | 2.4% | 1.4% | 🟢 ZYSK |
| #24 | `L3_GC-01_TARGET_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): target_heresy 0 → 1 | 61.8 → 🟠 ** 62.2** (`⬆️ +0.4`) | 2.4% | 1.4% | 🟢 ZYSK |