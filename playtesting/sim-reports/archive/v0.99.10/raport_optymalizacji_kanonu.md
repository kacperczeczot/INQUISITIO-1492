# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.99.10 (Iteracja #4, Faza 1D)

**Wersja Poprzednia:** `v0.99.9` (4P: `63.7 pkt`) → **Nowa Wersja:** `v0.99.10` (4P: `63.2 pkt`)
**Data:** 2026-08-18 03:07 | **Czas Trwania Iteracji:** 545.2s | **Zysk 4P:** `-0.5 pkt` | **Zysk Global:** `-0.1 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_SO-08_COST_MINUS1` — **SO-08 (Nasłanie Inkwizytora): cost 1 → 0**
- **Opis Modyfikacji:** Karta `so-08` (Nasłanie Inkwizytora): `cost` → `0`
- **Wynik Kanonu 4P Score:** 63.7 → 🟠 ** 63.2** (`-0.5`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 51.1 → 51.6 (`⬆️ +0.5`) pkt
  - `4p-no-cienie`: 63.1 → 64.5 (`⬆️ +1.4`) pkt
  - `4p-no-kabala`: 60.4 → 60.5 (`⬆️ +0.1`) pkt
  - `4p-no-korona`: 82.1 → 78.0 (`-4.1`) pkt
  - `4p-no-oficjum`: 61.6 pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 14.6 → 14.7 (`⬆️ +0.1`) pkt
- **Tryb 4-osobowy (4p Avg):** 65.3 → 64.7 (`-0.6`) pkt
- **Tryb 5-osobowy (5p Avg):** 37.5 → 37.7 (`⬆️ +0.2`) pkt
- **Global Game Balance Score:** 39.1 → 🔴 ** 39.0** (`-0.1`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.19 Er`
  - **Deadlocki (Limit Er):** `2.1%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.4%` (norma: <30%)
  - **Autodafé / partię:** `2.15`
  - **Oskarżenia / partię:** `4.69`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 63.7 → 🟠 ** 63.8** (`⬆️ +0.1`) | 2.4% | 1.4% | 🟢 ZYSK |
| #2 | `L3_CAA-12_HERESY_MINUS1` | CAA-12 (Skrytka w Murach): heresy 1 → 0 | 63.7 → 🟠 ** 63.9** (`⬆️ +0.2`) | 2.3% | 1.4% | 🟢 ZYSK |
| #3 | `L3_KB-01_COST_MINUS1` | KB-01 (Rozkaz Dworu): cost 1 → 0 | 63.7 → 🟠 ** 64.1** (`⬆️ +0.4`) | 2.1% | 0.6% | 🟢 ZYSK |
| #4 | `L3_SO-08_COST_MINUS1` | SO-08 (Nasłanie Inkwizytora): cost 1 → 0 | 63.7 → 🟠 ** 63.2** (`-0.5`) | 2.1% | 1.4% | 🌟 ZWYCIĘZCA |
| #5 | `L3_SO-08_GOLD_PLUS1` | SO-08 (Nasłanie Inkwizytora): gold 0 → 1 | 63.7 → 🟠 ** 63.2** (`-0.5`) | 2.1% | 1.4% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_GC-03_COST_MINUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 0 | 63.7 → 🟠 ** 64.3** (`⬆️ +0.6`) | 2.1% | 1.3% | 🟢 ZYSK |
| #7 | `L3_SO-06_TARGET_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): target_heresy 0 → 1 | 63.7 → 🟠 ** 64.0** (`⬆️ +0.3`) | 2.1% | 1.4% | 🟢 ZYSK |
| #8 | `L3_GC-12_COST_PLUS1` | GC-12 (Złodziejski Zwiad): cost 0 → 1 | 63.7 → 🟠 ** 63.8** (`⬆️ +0.1`) | 2.1% | 1.4% | 🟢 ZYSK |
| #9 | `L3_KT-11_COST_MINUS1` | KT-11 (Medytacja Sefirot): cost 1 → 0 | 63.7 → 🟠 ** 63.8** (`⬆️ +0.1`) | 2.1% | 1.3% | 🟢 ZYSK |
| #10 | `L3_KT-04_COST_MINUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 0 | 🟠 ** 63.7** | 2.1% | 1.3% | ⚪ STRATA/NEUTRALNY |
| #11 | `L4_SEA_ROUTE_ERA_MINUS1` | Szlak Morski: Era 4 → 3 | 63.7 → 🟠 ** 63.8** (`⬆️ +0.1`) | 2.1% | 1.4% | 🟢 ZYSK |
| #12 | `L1_MAX_ERAS_PLUS1` | Limit Er: 12 → 13 | 63.7 → 🟠 ** 65.7** (`⬆️ +2.0`) | 0.6% | 1.4% | 🟢 ZYSK |
| #13 | `L3_KT-11_COST_PLUS1` | KT-11 (Medytacja Sefirot): cost 1 → 2 | 63.7 → 🟠 ** 63.2** (`-0.5`) | 2.1% | 1.4% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_SO-01_TARGET_HERESY_PLUS1` | SO-01 (Patrol Familiariuszy): target_heresy 0 → 1 | 63.7 → 🟠 ** 64.3** (`⬆️ +0.6`) | 2.1% | 1.4% | 🟢 ZYSK |
| #15 | `L3_KB-01_TARGET_HERESY_PLUS1` | KB-01 (Rozkaz Dworu): target_heresy 0 → 1 | 63.7 → 🟠 ** 65.7** (`⬆️ +2.0`) | 2.1% | 1.4% | 🟢 ZYSK |
| #16 | `L3_KB-10_TARGET_HERESY_PLUS1` | KB-10 (Pieczęć Korony): target_heresy 0 → 1 | 63.7 → 🟠 ** 64.8** (`⬆️ +1.1`) | 1.7% | 1.4% | 🟢 ZYSK |
| #17 | `L3_SO-02_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): heresy 0 → 1 | 63.7 → 🟠 ** 63.5** (`-0.2`) | 2.2% | 1.4% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_GC-08_COST_MINUS1` | GC-08 (Zatrute Złoto): cost 2 → 1 | 🟠 ** 63.7** | 2.1% | 1.4% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_GC-09_TARGET_HERESY_PLUS1` | GC-09 (Lista Dłużników): target_heresy 0 → 1 | 63.7 → 🟠 ** 63.6** (`-0.1`) | 2.1% | 1.4% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_KB-03_GOLD_PLUS1` | KB-03 (Plotka Dworska): gold 0 → 1 | 63.7 → 🟠 ** 65.2** (`⬆️ +1.5`) | 2.1% | 1.5% | 🟢 ZYSK |
| #21 | `L3_KB-03_COST_MINUS1` | KB-03 (Plotka Dworska): cost 1 → 0 | 63.7 → 🟠 ** 65.7** (`⬆️ +2.0`) | 2.0% | 0.7% | 🟢 ZYSK |
| #22 | `L3_KB-11_TARGET_HERESY_PLUS1` | KB-11 (Tajny Emisariusz): target_heresy 0 → 1 | 63.7 → 🟠 ** 65.2** (`⬆️ +1.5`) | 2.1% | 1.4% | 🟢 ZYSK |
| #23 | `L3_KB-10_COST_MINUS1` | KB-10 (Pieczęć Korony): cost 3 → 2 | 63.7 → 🟠 ** 62.4** (`-1.3`) | 2.0% | 1.3% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_KB-03_TARGET_HERESY_PLUS1` | KB-03 (Plotka Dworska): target_heresy 1 → 2 | 63.7 → 🟠 ** 65.5** (`⬆️ +1.8`) | 2.1% | 1.4% | 🟢 ZYSK |