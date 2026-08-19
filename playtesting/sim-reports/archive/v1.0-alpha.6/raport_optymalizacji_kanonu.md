# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.6 (Iteracja #3, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.5` (4P: `76.2 pkt`) → **Nowa Wersja:** `v1.0-alpha.6` (4P: `76.4 pkt`)
**Data:** 2026-08-19 00:04 | **Czas Trwania Iteracji:** 452.5s | **Zysk 4P:** `+0.2 pkt` | **Zysk Global:** `-0.3 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_KT-11_COST_PLUS1` — **KT-11 (Medytacja Sefirot): cost 1 → 2**
- **Opis Modyfikacji:** Karta `kt-11` (Medytacja Sefirot): `cost` → `2`
- **Wynik Kanonu 4P Score:** 76.2 → 🟡 ** 76.4** (`⬆️ +0.2`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 68.0 → 67.9 (`-0.1`) pkt
  - `4p-no-cienie`: 87.0 pkt
  - `4p-no-kabala`: 61.0 pkt
  - `4p-no-korona`: 91.2 → 91.6 (`⬆️ +0.4`) pkt
  - `4p-no-oficjum`: 74.0 → 74.6 (`⬆️ +0.6`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 20.8 → 20.6 (`-0.2`) pkt
- **Tryb 4-osobowy (4p Avg):** 79.3 → 79.7 (`⬆️ +0.4`) pkt
- **Tryb 5-osobowy (5p Avg):** 39.6 → 38.7 (`-0.9`) pkt
- **Global Game Balance Score:** 46.6 → 🔴 ** 46.3** (`-0.3`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.21 Er`
  - **Deadlocki (Limit Er):** `0.5%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.6%` (norma: <30%)
  - **Autodafé / partię:** `2.22`
  - **Oskarżenia / partię:** `4.15`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_KT-11_COST_PLUS1` | KT-11 (Medytacja Sefirot): cost 1 → 2 | 76.2 → 🟡 ** 76.4** (`⬆️ +0.2`) | 0.5% | 1.6% | 🌟 ZWYCIĘZCA |
| #2 | `L1_MAX_ERAS_PLUS1` | Limit Er: 13 → 14 | 76.2 → 🟡 ** 76.3** (`⬆️ +0.1`) | 0.3% | 1.6% | 🟢 ZYSK |
| #3 | `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 76.2 → 🟡 ** 76.3** (`⬆️ +0.1`) | 0.5% | 1.6% | 🟢 ZYSK |
| #4 | `L3_KT-11_COST_MINUS1` | KT-11 (Medytacja Sefirot): cost 1 → 0 | 76.2 → 🟡 ** 76.3** (`⬆️ +0.1`) | 0.5% | 1.5% | 🟢 ZYSK |
| #5 | `L3_CAA-10_COST_PLUS1` | CAA-10 (Echo Alhambry): cost 0 → 1 | 76.2 → 🟡 ** 76.3** (`⬆️ +0.1`) | 0.5% | 1.6% | 🟢 ZYSK |
| #6 | `L3_GC-05_COST_PLUS1` | GC-05 (Fałszywy Świadek): cost 0 → 1 | 76.2 → 🟡 ** 76.3** (`⬆️ +0.1`) | 0.5% | 1.6% | 🟢 ZYSK |
| #7 | `L3_GC-12_COST_PLUS1` | GC-12 (Złodziejski Zwiad): cost 0 → 1 | 🟡 ** 76.2** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #8 | `L2_CAA_ERA_MINUS1` | Cienie Era ścieżki: 1 → 0 | 🟡 ** 76.2** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #9 | `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 7 → 8 | 🟡 ** 76.2** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #10 | `L2_CAA_ERA_PLUS1` | Cienie Era ścieżki: 1 → 2 | 🟡 ** 76.2** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 0 → 1 | 🟡 ** 76.2** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 0 → 1 | 🟡 ** 76.2** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_CAA-07_HERESY_PLUS1` | CAA-07 (Szantaż Bractwa): heresy 0 → 1 | 🟡 ** 76.2** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_CAA-09_GOLD_PLUS1` | CAA-09 (Kurier Relikwii): gold 0 → 1 | 🟡 ** 76.2** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_CAA-09_COST_PLUS1` | CAA-09 (Kurier Relikwii): cost 0 → 1 | 🟡 ** 76.2** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_CAA-11_COST_PLUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 2 | 🟡 ** 76.2** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_CAA-01_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 🟡 ** 76.2** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_CAA-11_HERESY_PLUS1` | CAA-11 (Nocna Zmiana Warty): heresy 0 → 1 | 🟡 ** 76.2** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_CAA-11_COST_MINUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 0 | 🟡 ** 76.2** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_CAA-11_GOLD_PLUS1` | CAA-11 (Nocna Zmiana Warty): gold 0 → 1 | 🟡 ** 76.2** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_GC-01_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): heresy 1 → 2 | 🟡 ** 76.2** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_GC-01_HERESY_MINUS1` | GC-01 (Przekupiony Strażnik): heresy 1 → 0 | 🟡 ** 76.2** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_SO-10_HERESY_MINUS1` | SO-10 (Oczyść Miasto): heresy 2 → 1 | 🟡 ** 76.2** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 2 → 3 | 76.2 → 🟡 ** 75.6** (`-0.6`) | 0.6% | 1.6% | ⚪ STRATA/NEUTRALNY |