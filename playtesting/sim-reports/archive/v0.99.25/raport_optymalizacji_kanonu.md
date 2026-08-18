# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.99.25 (Iteracja #2, Faza 1D)

**Wersja Poprzednia:** `v0.99.24` (4P: `76.2 pkt`) → **Nowa Wersja:** `v0.99.25` (4P: `75.8 pkt`)
**Data:** 2026-08-18 16:32 | **Czas Trwania Iteracji:** 733.8s | **Zysk 4P:** `-0.4 pkt` | **Zysk Global:** `+0.1 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_KB-10_TARGET_HERESY_PLUS1` — **KB-10 (Pieczęć Korony): target_heresy 0 → 1**
- **Opis Modyfikacji:** Karta `kb-10` (Pieczęć Korony): `target_heresy` → `1`
- **Wynik Kanonu 4P Score:** 76.2 → 🟡 ** 75.8** (`-0.4`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 67.0 → 67.3 (`⬆️ +0.3`) pkt
  - `4p-no-cienie`: 89.5 → 88.4 (`-1.1`) pkt
  - `4p-no-kabala`: 61.9 → 62.4 (`⬆️ +0.5`) pkt
  - `4p-no-korona`: 89.3 pkt
  - `4p-no-oficjum`: 73.1 → 71.4 (`-1.7`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 21.2 → 21.0 (`-0.2`) pkt
- **Tryb 4-osobowy (4p Avg):** 77.3 → 77.2 (`-0.1`) pkt
- **Tryb 5-osobowy (5p Avg):** 37.6 → 38.4 (`⬆️ +0.8`) pkt
- **Global Game Balance Score:** 45.4 → 🔴 ** 45.5** (`⬆️ +0.1`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.20 Er`
  - **Deadlocki (Limit Er):** `0.5%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.5%` (norma: <30%)
  - **Autodafé / partię:** `2.21`
  - **Oskarżenia / partię:** `4.16`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-12_COST_PLUS1` | CAA-12 (Skrytka w Murach): cost 0 → 1 | 76.2 → 🟡 ** 76.3** (`⬆️ +0.1`) | 0.6% | 1.5% | 🟢 ZYSK |
| #2 | `L3_CAA-12_GOLD_MINUS1` | CAA-12 (Skrytka w Murach): gold 3 → 2 | 76.2 → 🟡 ** 76.3** (`⬆️ +0.1`) | 0.6% | 1.5% | 🟢 ZYSK |
| #3 | `L3_GC-09_GOLD_PLUS1` | GC-09 (Lista Dłużników): gold 0 → 1 | 76.2 → 🟡 ** 76.3** (`⬆️ +0.1`) | 0.6% | 1.5% | 🟢 ZYSK |
| #4 | `L3_GC-12_COST_PLUS1` | GC-12 (Złodziejski Zwiad): cost 0 → 1 | 🟡 ** 76.2** | 0.6% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #5 | `L1_MAX_ERAS_PLUS1` | Limit Er: 13 → 14 | 🟡 ** 76.2** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_KB-11_GOLD_MINUS1` | KB-11 (Tajny Emisariusz): gold 1 → 0 | 🟡 ** 76.2** | 0.6% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 🟡 ** 76.2** | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_KT-11_COST_MINUS1` | KT-11 (Medytacja Sefirot): cost 1 → 0 | 🟡 ** 76.2** | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #9 | `L2_CAA_ERA_PLUS1` | Cienie Era ścieżki: 1 → 2 | 🟡 ** 76.2** | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #10 | `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 7 → 8 | 🟡 ** 76.2** | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #11 | `L2_CAA_ERA_MINUS1` | Cienie Era ścieżki: 1 → 0 | 🟡 ** 76.2** | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 0 → 1 | 🟡 ** 76.2** | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_CAA-01_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 🟡 ** 76.2** | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_KT-11_COST_PLUS1` | KT-11 (Medytacja Sefirot): cost 1 → 2 | 🟡 ** 76.2** | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_SO-02_GOLD_MINUS1` | SO-02 (Skarbiec Trybunału): gold 3 → 2 | 🟡 ** 76.2** | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 🟡 ** 76.2** | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_SO-10_HERESY_MINUS1` | SO-10 (Oczyść Miasto): heresy 2 → 1 | 76.2 → 🟡 ** 76.1** (`-0.1`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_KT-08_COST_MINUS1` | KT-08 (Areszt Wiedzy): cost 1 → 0 | 76.2 → 🟡 ** 76.1** (`-0.1`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_CAA-04_HERESY_PLUS1` | CAA-04 (Fałszywy Trop): heresy 0 → 1 | 76.2 → 🟡 ** 76.0** (`-0.2`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_KT-04_COST_MINUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 0 | 76.2 → 🟡 ** 76.0** (`-0.2`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_GC-07_COST_MINUS1` | GC-07 (Skrytobójstwo): cost 2 → 1 | 76.2 → 🟡 ** 76.0** (`-0.2`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_KB-10_TARGET_HERESY_PLUS1` | KB-10 (Pieczęć Korony): target_heresy 0 → 1 | 76.2 → 🟡 ** 75.8** (`-0.4`) | 0.5% | 1.5% | 🌟 ZWYCIĘZCA |
| #23 | `L3_KB-03_GOLD_PLUS1` | KB-03 (Plotka Dworska): gold 0 → 1 | 76.2 → 🟡 ** 75.8** (`-0.4`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 1 → 2 | 76.2 → 🟡 ** 75.7** (`-0.5`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |