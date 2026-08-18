# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.3 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.2` (4P: `75.2 pkt`) → **Nowa Wersja:** `v1.0-alpha.3` (4P: `76.5 pkt`)
**Data:** 2026-08-18 23:23 | **Czas Trwania Iteracji:** 229.0s | **Zysk 4P:** `+1.3 pkt` | **Zysk Global:** `+1.8 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L1_MAX_ERAS_PLUS1` — **Limit Er: 11 → 12**
- **Opis Modyfikacji:** Limit Er: offset +1 (nowy: 12)
- **Wynik Kanonu 4P Score:** 75.2 → 🟡 ** 76.5** (`⬆️ +1.3`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 54.5 → 60.6 (`⬆️ +6.1`) pkt
  - `4p-no-cienie`: 87.9 → 87.8 (`-0.1`) pkt
  - `4p-no-kabala`: 65.7 → 65.9 (`⬆️ +0.2`) pkt
  - `4p-no-korona`: 91.2 → 91.5 (`⬆️ +0.3`) pkt
  - `4p-no-oficjum`: 76.8 pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 15.0 → 18.6 (`⬆️ +3.6`) pkt
- **Tryb 4-osobowy (4p Avg):** 75.5 → 77.5 (`⬆️ +2.0`) pkt
- **Tryb 5-osobowy (5p Avg):** 40.5 pkt
- **Global Game Balance Score:** 43.7 → 🔴 ** 45.5** (`⬆️ +1.8`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.20 Er`
  - **Deadlocki (Limit Er):** `1.9%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.6%` (norma: <30%)
  - **Autodafé / partię:** `2.21`
  - **Oskarżenia / partię:** `4.14`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L1_MAX_ERAS_PLUS1` | Limit Er: 11 → 12 | 75.2 → 🟡 ** 76.5** (`⬆️ +1.3`) | 1.9% | 1.6% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 75.2 → 🟡 ** 75.6** (`⬆️ +0.4`) | 2.7% | 1.6% | 🟢 ZYSK |
| #3 | `L3_GC-12_COST_PLUS1` | GC-12 (Złodziejski Zwiad): cost 0 → 1 | 🟡 ** 75.2** | 2.7% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #4 | `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 7 → 8 | 🟡 ** 75.2** | 2.7% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #5 | `L2_CAA_ERA_PLUS1` | Cienie Era ścieżki: 1 → 2 | 🟡 ** 75.2** | 2.7% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #6 | `L2_CAA_ERA_MINUS1` | Cienie Era ścieżki: 1 → 0 | 🟡 ** 75.2** | 2.7% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 0 → 1 | 🟡 ** 75.2** | 2.7% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_CAA-09_COST_PLUS1` | CAA-09 (Kurier Relikwii): cost 0 → 1 | 🟡 ** 75.2** | 2.7% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_CAA-01_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 🟡 ** 75.2** | 2.7% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 0 → 1 | 🟡 ** 75.2** | 2.7% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_CAA-09_GOLD_PLUS1` | CAA-09 (Kurier Relikwii): gold 0 → 1 | 🟡 ** 75.2** | 2.7% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-07_HERESY_PLUS1` | CAA-07 (Szantaż Bractwa): heresy 0 → 1 | 🟡 ** 75.2** | 2.7% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_CAA-10_COST_PLUS1` | CAA-10 (Echo Alhambry): cost 0 → 1 | 🟡 ** 75.2** | 2.7% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_CAA-11_COST_PLUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 2 | 🟡 ** 75.2** | 2.7% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_CAA-11_HERESY_PLUS1` | CAA-11 (Nocna Zmiana Warty): heresy 0 → 1 | 🟡 ** 75.2** | 2.7% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_CAA-11_COST_MINUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 0 | 🟡 ** 75.2** | 2.7% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_KT-11_COST_PLUS1` | KT-11 (Medytacja Sefirot): cost 1 → 2 | 75.2 → 🟡 ** 75.1** (`-0.1`) | 2.7% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_KT-03_GOLD_PLUS1` | KT-03 (Zakazana Wiedza): gold 0 → 1 | 75.2 → 🟡 ** 75.1** (`-0.1`) | 2.7% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_CAA-12_GOLD_MINUS1` | CAA-12 (Skrytka w Murach): gold 3 → 2 | 75.2 → 🟡 ** 75.1** (`-0.1`) | 2.8% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_CAA-12_COST_PLUS1` | CAA-12 (Skrytka w Murach): cost 0 → 1 | 75.2 → 🟡 ** 75.1** (`-0.1`) | 2.8% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 0 → 1 | 75.2 → 🟡 ** 75.0** (`-0.2`) | 2.8% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_CAA-02_GOLD_MINUS1` | CAA-02 (Złoto z Kryjówki): gold 3 → 2 | 75.2 → 🟡 ** 75.0** (`-0.2`) | 2.8% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_CAA-06_TARGET_HERESY_PLUS1` | CAA-06 (Ucieczka z Lochów): target_heresy 0 → 1 | 75.2 → 🟡 ** 75.0** (`-0.2`) | 2.4% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_KT-07_COST_PLUS1` | KT-07 (Archiwum Ukryte): cost 1 → 2 | 75.2 → 🟠 ** 74.9** (`-0.3`) | 2.7% | 1.6% | ⚪ STRATA/NEUTRALNY |