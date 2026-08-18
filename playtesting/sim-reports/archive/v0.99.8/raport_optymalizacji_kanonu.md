# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.99.8 (Iteracja #2, Faza 1D)

**Wersja Poprzednia:** `v0.99.7` (4P: `62.7 pkt`) → **Nowa Wersja:** `v0.99.8` (4P: `63.1 pkt`)
**Data:** 2026-08-18 02:48 | **Czas Trwania Iteracji:** 579.7s | **Zysk 4P:** `+0.4 pkt` | **Zysk Global:** `-0.4 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_CAA-08_HERESY_MINUS1` — **CAA-08 (Kaptur Nocy): heresy 1 → 0**
- **Opis Modyfikacji:** Karta `caa-08` (Kaptur Nocy): `heresy` → `0`
- **Wynik Kanonu 4P Score:** 62.7 → 🟠 ** 63.1** (`⬆️ +0.4`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 49.3 → 50.1 (`⬆️ +0.8`) pkt
  - `4p-no-cienie`: 63.1 pkt
  - `4p-no-kabala`: 59.7 pkt
  - `4p-no-korona`: 82.9 → 82.1 (`-0.8`) pkt
  - `4p-no-oficjum`: 58.6 → 60.5 (`⬆️ +1.9`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 14.5 pkt
- **Tryb 4-osobowy (4p Avg):** 64.0 → 64.6 (`⬆️ +0.6`) pkt
- **Tryb 5-osobowy (5p Avg):** 38.7 → 37.0 (`-1.7`) pkt
- **Global Game Balance Score:** 39.1 → 🔴 ** 38.7** (`-0.4`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.18 Er`
  - **Deadlocki (Limit Er):** `2.1%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.4%` (norma: <30%)
  - **Autodafé / partię:** `2.11`
  - **Oskarżenia / partię:** `4.69`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 62.7 → 🟠 ** 63.4** (`⬆️ +0.7`) | 2.4% | 1.4% | 🟢 ZYSK |
| #2 | `L3_CAA-12_HERESY_MINUS1` | CAA-12 (Skrytka w Murach): heresy 1 → 0 | 62.7 → 🟠 ** 63.4** (`⬆️ +0.7`) | 2.3% | 1.4% | 🟢 ZYSK |
| #3 | `L3_CAA-08_HERESY_MINUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 0 | 62.7 → 🟠 ** 63.1** (`⬆️ +0.4`) | 2.1% | 1.4% | 🌟 ZWYCIĘZCA |
| #4 | `L3_CAA-06_COST_MINUS1` | CAA-06 (Ucieczka z Lochów): cost 1 → 0 | 62.7 → 🟠 ** 63.2** (`⬆️ +0.5`) | 2.1% | 1.4% | 🟢 ZYSK |
| #5 | `L3_CAA-06_GOLD_PLUS1` | CAA-06 (Ucieczka z Lochów): gold 0 → 1 | 62.7 → 🟠 ** 63.2** (`⬆️ +0.5`) | 2.1% | 1.4% | 🟢 ZYSK |
| #6 | `L4_SEA_ROUTE_ERA_MINUS1` | Szlak Morski: Era 4 → 3 | 62.7 → 🟠 ** 62.9** (`⬆️ +0.2`) | 2.1% | 1.4% | 🟢 ZYSK |
| #7 | `L3_GC-09_TARGET_HERESY_PLUS1` | GC-09 (Lista Dłużników): target_heresy 0 → 1 | 62.7 → 🟠 ** 63.1** (`⬆️ +0.4`) | 2.1% | 1.4% | 🟢 ZYSK |
| #8 | `L3_KT-11_COST_MINUS1` | KT-11 (Medytacja Sefirot): cost 1 → 0 | 62.7 → 🟠 ** 62.9** (`⬆️ +0.2`) | 2.1% | 1.3% | 🟢 ZYSK |
| #9 | `L3_GC-12_COST_PLUS1` | GC-12 (Złodziejski Zwiad): cost 0 → 1 | 62.7 → 🟠 ** 62.8** (`⬆️ +0.1`) | 2.1% | 1.4% | 🟢 ZYSK |
| #10 | `L3_KT-04_COST_MINUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 0 | 62.7 → 🟠 ** 62.8** (`⬆️ +0.1`) | 2.1% | 1.3% | 🟢 ZYSK |
| #11 | `L3_SO-02_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): heresy 0 → 1 | 62.7 → 🟠 ** 62.8** (`⬆️ +0.1`) | 2.2% | 1.4% | 🟢 ZYSK |
| #12 | `L3_SO-06_TARGET_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): target_heresy 0 → 1 | 62.7 → 🟠 ** 63.1** (`⬆️ +0.4`) | 2.1% | 1.4% | 🟢 ZYSK |
| #13 | `L3_SO-08_GOLD_PLUS1` | SO-08 (Nasłanie Inkwizytora): gold 0 → 1 | 62.7 → 🟠 ** 62.6** (`-0.1`) | 2.0% | 1.4% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_SO-08_COST_MINUS1` | SO-08 (Nasłanie Inkwizytora): cost 1 → 0 | 62.7 → 🟠 ** 62.6** (`-0.1`) | 2.0% | 1.4% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_KB-01_TARGET_HERESY_PLUS1` | KB-01 (Rozkaz Dworu): target_heresy 0 → 1 | 62.7 → 🟠 ** 64.6** (`⬆️ +1.9`) | 2.1% | 1.4% | 🟢 ZYSK |
| #16 | `L3_GC-03_COST_MINUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 0 | 62.7 → 🟠 ** 63.2** (`⬆️ +0.5`) | 2.1% | 1.3% | 🟢 ZYSK |
| #17 | `L3_GC-09_COST_PLUS1` | GC-09 (Lista Dłużników): cost 3 → 4 | 62.7 → 🟠 ** 62.0** (`-0.7`) | 2.1% | 1.8% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_KB-03_COST_MINUS1` | KB-03 (Plotka Dworska): cost 1 → 0 | 62.7 → 🟠 ** 64.7** (`⬆️ +2.0`) | 2.0% | 0.7% | 🟢 ZYSK |
| #19 | `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 2 → 3 | 62.7 → 🟠 ** 62.1** (`-0.6`) | 2.1% | 1.4% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_KB-03_GOLD_PLUS1` | KB-03 (Plotka Dworska): gold 0 → 1 | 62.7 → 🟠 ** 64.1** (`⬆️ +1.4`) | 2.1% | 1.4% | 🟢 ZYSK |
| #21 | `L3_GC-08_COST_MINUS1` | GC-08 (Zatrute Złoto): cost 2 → 1 | 62.7 → 🟠 ** 62.8** (`⬆️ +0.1`) | 2.1% | 1.4% | 🟢 ZYSK |
| #22 | `L3_KB-11_TARGET_HERESY_PLUS1` | KB-11 (Tajny Emisariusz): target_heresy 0 → 1 | 62.7 → 🟠 ** 64.1** (`⬆️ +1.4`) | 2.1% | 1.4% | 🟢 ZYSK |
| #23 | `L3_KB-10_COST_MINUS1` | KB-10 (Pieczęć Korony): cost 3 → 2 | 62.7 → 🟠 ** 61.6** (`-1.1`) | 2.0% | 1.3% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_KB-03_TARGET_HERESY_PLUS1` | KB-03 (Plotka Dworska): target_heresy 1 → 2 | 62.7 → 🟠 ** 64.3** (`⬆️ +1.6`) | 2.1% | 1.4% | 🟢 ZYSK |