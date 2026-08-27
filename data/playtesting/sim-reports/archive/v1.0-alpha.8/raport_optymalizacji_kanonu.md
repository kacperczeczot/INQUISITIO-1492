[Strona główna](../../../../../README.md) > [v1.0-alpha.8](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.8 (Iteracja #5, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.7` (4P: `76.4 pkt`) → **Nowa Wersja:** `v1.0-alpha.8` (4P: `76.5 pkt`)
**Data:** 2026-08-19 00:20 | **Czas Trwania Iteracji:** 454.7s | **Zysk 4P:** `+0.1 pkt` | **Zysk Global:** `0.0 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_CAA-10_COST_PLUS1` — **CAA-10 (Echo Alhambry): cost 0 → 1**
- **Opis Modyfikacji:** Karta `caa-10` (Echo Alhambry): `cost` → `1`
- **Wynik Kanonu 4P Score:** 76.4 → 🟡 ** 76.5** (`⬆️ +0.1`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 67.9 pkt
  - `4p-no-cienie`: 87.0 pkt
  - `4p-no-kabala`: 61.1 pkt
  - `4p-no-korona`: 91.6 → 91.7 (`⬆️ +0.1`) pkt
  - `4p-no-oficjum`: 74.6 pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 22.3 pkt
- **Tryb 4-osobowy (4p Avg):** 79.7 pkt
- **Tryb 5-osobowy (5p Avg):** 38.7 pkt
- **Global Game Balance Score:** 🔴 ** 46.9** pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.21 Er`
  - **Deadlocki (Limit Er):** `0.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.6%` (norma: <30%)
  - **Autodafé / partię:** `2.22`
  - **Oskarżenia / partię:** `4.16`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-10_COST_PLUS1` | CAA-10 (Echo Alhambry): cost 0 → 1 | 76.4 → 🟡 ** 76.5** (`⬆️ +0.1`) | 0.3% | 1.6% | 🌟 ZWYCIĘZCA |
| #2 | `L3_GC-12_COST_PLUS1` | GC-12 (Złodziejski Zwiad): cost 0 → 1 | 🟡 ** 76.4** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #3 | `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 7 → 8 | 🟡 ** 76.4** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #4 | `L2_CAA_ERA_MINUS1` | Cienie Era ścieżki: 1 → 0 | 🟡 ** 76.4** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #5 | `L2_CAA_ERA_PLUS1` | Cienie Era ścieżki: 1 → 2 | 🟡 ** 76.4** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #6 | `L1_MAX_ERAS_PLUS1` | Limit Er: 14 → 15 | 🟡 ** 76.4** | 0.2% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 0 → 1 | 🟡 ** 76.4** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_CAA-07_HERESY_PLUS1` | CAA-07 (Szantaż Bractwa): heresy 0 → 1 | 🟡 ** 76.4** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_CAA-09_COST_PLUS1` | CAA-09 (Kurier Relikwii): cost 0 → 1 | 🟡 ** 76.4** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_CAA-01_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 🟡 ** 76.4** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 0 → 1 | 🟡 ** 76.4** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-11_HERESY_PLUS1` | CAA-11 (Nocna Zmiana Warty): heresy 0 → 1 | 🟡 ** 76.4** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_CAA-09_GOLD_PLUS1` | CAA-09 (Kurier Relikwii): gold 0 → 1 | 🟡 ** 76.4** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_CAA-11_COST_PLUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 2 | 🟡 ** 76.4** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_CAA-11_COST_MINUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 0 | 🟡 ** 76.4** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_CAA-11_GOLD_PLUS1` | CAA-11 (Nocna Zmiana Warty): gold 0 → 1 | 🟡 ** 76.4** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_GC-01_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): heresy 1 → 2 | 🟡 ** 76.4** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_GC-01_TARGET_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): target_heresy 0 → 1 | 🟡 ** 76.4** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_GC-01_GOLD_PLUS1` | GC-01 (Przekupiony Strażnik): gold 1 → 2 | 🟡 ** 76.4** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_GC-01_HERESY_MINUS1` | GC-01 (Przekupiony Strażnik): heresy 1 → 0 | 🟡 ** 76.4** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_SO-10_HERESY_MINUS1` | SO-10 (Oczyść Miasto): heresy 2 → 1 | 76.4 → 🟡 ** 76.3** (`-0.1`) | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 0 → 1 | 76.4 → 🟡 ** 76.3** (`-0.1`) | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_CAA-02_GOLD_MINUS1` | CAA-02 (Złoto z Kryjówki): gold 3 → 2 | 76.4 → 🟡 ** 76.3** (`-0.1`) | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 2 → 3 | 76.4 → 🟡 ** 75.9** (`-0.5`) | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |