# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.99.6 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v0.99.5` (4P: `56.2 pkt`) → **Nowa Wersja:** `v0.99.6` (4P: `61.4 pkt`)
**Data:** 2026-08-18 02:13 | **Czas Trwania Iteracji:** 384.4s | **Zysk 4P:** `+5.2 pkt` | **Zysk Global:** `-1.0 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_CAA-08_TARGET_HERESY_PLUS1` — **CAA-08 (Kaptur Nocy): target_heresy 1 → 2**
- **Opis Modyfikacji:** Karta `caa-08` (Kaptur Nocy): `target_heresy` → `2`
- **Wynik Kanonu 4P Score:** 56.2 → 🟠 ** 61.4** (`⬆️ +5.2`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 37.9 → 41.5 (`⬆️ +3.6`) pkt
  - `4p-no-cienie`: 59.7 pkt
  - `4p-no-kabala`: 60.2 pkt
  - `4p-no-korona`: 69.8 → 89.0 (`⬆️ +19.2`) pkt
  - `4p-no-oficjum`: 53.2 → 56.4 (`⬆️ +3.2`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 12.8 → 12.9 (`⬆️ +0.1`) pkt
- **Tryb 4-osobowy (4p Avg):** 59.2 → 63.1 (`⬆️ +3.9`) pkt
- **Tryb 5-osobowy (5p Avg):** 48.2 → 41.2 (`-7.0`) pkt
- **Global Game Balance Score:** 40.1 → 🔴 ** 39.1** (`-1.0`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.21 Er`
  - **Deadlocki (Limit Er):** `2.5%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.4%` (norma: <30%)
  - **Autodafé / partię:** `2.12`
  - **Oskarżenia / partię:** `4.59`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-08_TARGET_HERESY_PLUS1` | CAA-08 (Kaptur Nocy): target_heresy 1 → 2 | 56.2 → 🟠 ** 61.4** (`⬆️ +5.2`) | 2.5% | 1.4% | 🌟 ZWYCIĘZCA |
| #2 | `L3_CAA-08_COST_MINUS1` | CAA-08 (Kaptur Nocy): cost 1 → 0 | 56.2 → 🟠 ** 60.9** (`⬆️ +4.7`) | 2.5% | 1.4% | 🟢 ZYSK |
| #3 | `L3_CAA-08_GOLD_PLUS1` | CAA-08 (Kaptur Nocy): gold 0 → 1 | 56.2 → 🟠 ** 60.9** (`⬆️ +4.7`) | 2.5% | 1.4% | 🟢 ZYSK |
| #4 | `L3_KT-05_TARGET_HERESY_PLUS1` | KT-05 (Wskazówka Cyklu): target_heresy 0 → 1 | 56.2 → 🔴 ** 55.3** (`-0.9`) | 2.1% | 1.4% | ⚪ STRATA/NEUTRALNY |
| #5 | `L3_KT-06_COST_PLUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 3 | 56.2 → 🔴 ** 56.5** (`⬆️ +0.3`) | 2.3% | 1.4% | 🟢 ZYSK |
| #6 | `L3_CAA-06_COST_MINUS1` | CAA-06 (Ucieczka z Lochów): cost 1 → 0 | 56.2 → 🔴 ** 57.1** (`⬆️ +0.9`) | 2.5% | 1.4% | 🟢 ZYSK |
| #7 | `L3_CAA-06_GOLD_PLUS1` | CAA-06 (Ucieczka z Lochów): gold 0 → 1 | 56.2 → 🔴 ** 57.1** (`⬆️ +0.9`) | 2.5% | 1.4% | 🟢 ZYSK |
| #8 | `L3_KB-06_COST_MINUS1` | KB-06 (Areszt Królewski): cost 1 → 0 | 56.2 → 🔴 ** 56.8** (`⬆️ +0.6`) | 2.4% | 0.6% | 🟢 ZYSK |
| #9 | `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 56.2 → 🔴 ** 56.1** (`-0.1`) | 2.4% | 1.4% | ⚪ STRATA/NEUTRALNY |
| #10 | `L4_SEA_ROUTE_ERA_MINUS1` | Szlak Morski: Era 4 → 3 | 56.2 → 🔴 ** 56.4** (`⬆️ +0.2`) | 2.4% | 1.4% | 🟢 ZYSK |
| #11 | `L3_KT-07_COST_PLUS1` | KT-07 (Archiwum Ukryte): cost 1 → 2 | 56.2 → 🔴 ** 56.0** (`-0.2`) | 2.5% | 1.4% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_SO-09_TARGET_HERESY_PLUS1` | SO-09 (Świadek Koronny): target_heresy 0 → 1 | 56.2 → 🔴 ** 56.9** (`⬆️ +0.7`) | 2.5% | 1.4% | 🟢 ZYSK |
| #13 | `L1_MAX_ERAS_MINUS1` | Limit Er: 12 → 11 | 56.2 → 🔴 ** 55.1** (`-1.1`) | 3.5% | 1.4% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_SO-07_TARGET_HERESY_PLUS1` | SO-07 (Przesłuchanie Oficjum): target_heresy 0 → 1 | 56.2 → 🔴 ** 56.6** (`⬆️ +0.4`) | 2.5% | 1.4% | 🟢 ZYSK |
| #15 | `L3_SO-08_COST_MINUS1` | SO-08 (Nasłanie Inkwizytora): cost 1 → 0 | 56.2 → 🔴 ** 57.0** (`⬆️ +0.8`) | 2.3% | 1.4% | 🟢 ZYSK |
| #16 | `L3_SO-08_GOLD_PLUS1` | SO-08 (Nasłanie Inkwizytora): gold 0 → 1 | 56.2 → 🔴 ** 57.0** (`⬆️ +0.8`) | 2.3% | 1.4% | 🟢 ZYSK |
| #17 | `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 56.2 → 🔴 ** 56.5** (`⬆️ +0.3`) | 2.4% | 1.4% | 🟢 ZYSK |
| #18 | `L3_SO-02_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): heresy 0 → 1 | 56.2 → 🔴 ** 55.8** (`-0.4`) | 2.6% | 1.4% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_SO-04_COST_MINUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 0 | 56.2 → 🔴 ** 56.6** (`⬆️ +0.4`) | 2.3% | 1.4% | 🟢 ZYSK |
| #20 | `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 3 → 4 | 56.2 → 🔴 ** 23.7** (`-32.5`) | 2.7% | 1.4% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_KT-07_COST_MINUS1` | KT-07 (Archiwum Ukryte): cost 1 → 0 | 🔴 ** 56.2** | 2.5% | 1.4% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_KT-05_GOLD_PLUS1` | KT-05 (Wskazówka Cyklu): gold 0 → 1 | 56.2 → 🔴 ** 53.1** (`-3.1`) | 2.3% | 1.4% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_KT-05_COST_MINUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 0 | 56.2 → 🔴 ** 53.2** (`-3.0`) | 2.3% | 1.4% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_KT-10_HERESY_PLUS1` | KT-10 (Pieczęć Salomona): heresy 1 → 2 | 56.2 → 🔴 ** 56.6** (`⬆️ +0.4`) | 2.1% | 1.4% | 🟢 ZYSK |