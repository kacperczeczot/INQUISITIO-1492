[Strona główna](../../../../../README.md) > [v0.54](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.54 (Iteracja #2, Faza 1D)

**Wersja Poprzednia:** `v0.53` (4P: `99.6 pkt`) → **Nowa Wersja:** `v0.54` (4P: `99.7 pkt`)
**Data:** 2026-08-16 13:59 | **Czas Trwania Iteracji:** 252.9s | **Zysk 4P:** `+0.1 pkt` | **Zysk Global:** `-1.6 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L2_KB_ERA_MINUS1` — **Korona Era: 5/5/5 → 4/4/4**
- **Opis Modyfikacji:** Korona Borgiowie: Era zwycięstwa offset -1
- **Wynik Kanonu 4P Score:** 99.6 → 🟢 ** 99.7** (`⬆️ +0.1`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 99.8 → 99.9 (`⬆️ +0.1`) pkt
  - `4p-no-cienie`: 99.2 → 99.5 (`⬆️ +0.3`) pkt
  - `4p-no-kabala`: 99.7 → 99.8 (`⬆️ +0.1`) pkt
  - `4p-no-korona`: 99.5 pkt
  - `4p-no-oficjum`: 99.6 → 99.8 (`⬆️ +0.2`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 73.2 → 65.9 (`-7.3`) pkt
- **Tryb 4-osobowy (4p Avg):** 99.5 → 99.6 (`⬆️ +0.1`) pkt
- **Tryb 5-osobowy (5p Avg):** 83.4 → 86.0 (`⬆️ +2.6`) pkt
- **Global Game Balance Score:** 85.4 → 🟡 ** 83.8** (`-1.6`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.48 Er`
  - **Deadlocki (Limit Er):** `0.5%` (norma: <5%)
  - **Pas Biedy (Złoto):** `25.4%` (norma: <30%)
  - **Autodafé / partię:** `0.45`
  - **Oskarżenia / partię:** `3.15`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L2_KB_ERA_MINUS1` | Korona Era: 5/5/5 → 4/4/4 | 99.6 → 🟢 ** 99.7** (`⬆️ +0.1`) | 0.5% | 25.4% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KT-10_GOLD_PLUS1` | KT-10 (Pieczęć Salomona): gold 1 → 2 | 🟢 ** 99.6** | 0.5% | 25.6% | ⚪ STRATA/NEUTRALNY |
| #3 | `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 1 → 2 | 🟢 ** 99.6** | 0.5% | 25.6% | ⚪ STRATA/NEUTRALNY |
| #4 | `L3_KT-10_COST_PLUS1` | KT-10 (Pieczęć Salomona): cost 2 → 3 | 🟢 ** 99.6** | 0.4% | 25.3% | ⚪ STRATA/NEUTRALNY |
| #5 | `L3_CAA-04_COST_MINUS1` | CAA-04 (Fałszywy Trop): cost 1 → 0 | 🟢 ** 99.6** | 0.4% | 25.5% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_CAA-07_GOLD_PLUS1` | CAA-07 (Szantaż Bractwa): gold 0 → 1 | 🟢 ** 99.6** | 0.4% | 25.6% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_CAA-07_COST_MINUS1` | CAA-07 (Szantaż Bractwa): cost 2 → 1 | 🟢 ** 99.6** | 0.4% | 25.5% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_CAA-09_COST_MINUS1` | CAA-09 (Kurier Relikwii): cost 2 → 1 | 🟢 ** 99.6** | 0.4% | 25.5% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_KT-09_GOLD_MINUS1` | KT-09 (Fragment Kodeksu): gold 1 → 0 | 🟢 ** 99.6** | 0.5% | 25.6% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 0 → 1 | 🟢 ** 99.6** | 0.5% | 25.8% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_KT-02_COST_MINUS1` | KT-02 (Transmutacja Złota): cost 1 → 0 | 🟢 ** 99.6** | 0.5% | 25.6% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-05_COST_MINUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 | 🟢 ** 99.6** | 0.4% | 25.5% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_KT-09_COST_MINUS1` | KT-09 (Fragment Kodeksu): cost 1 → 0 | 🟢 ** 99.6** | 0.5% | 25.6% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_CAA-05_GOLD_PLUS1` | CAA-05 (Ukryty Kurier): gold 0 → 1 | 🟢 ** 99.6** | 0.4% | 25.5% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_KT-05_COST_PLUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 2 | 🟢 ** 99.6** | 0.4% | 25.5% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_CAA-03_GOLD_PLUS1` | CAA-03 (Cień na Rynku): gold 0 → 1 | 🟢 ** 99.6** | 0.4% | 25.6% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_KT-03_GOLD_MINUS1` | KT-03 (Zakazana Wiedza): gold 1 → 0 | 🟢 ** 99.6** | 0.4% | 25.6% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_CAA-08_COST_MINUS1` | CAA-08 (Kaptur Nocy): cost 2 → 1 | 🟢 ** 99.6** | 0.5% | 25.6% | ⚪ STRATA/NEUTRALNY |
| #19 | `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 99.6 → 🟢 ** 99.5** (`-0.1`) | 0.5% | 25.6% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_CAA-02_COST_MINUS1` | CAA-02 (Złoto z Kryjówki): cost 1 → 0 | 99.6 → 🟢 ** 99.5** (`-0.1`) | 0.5% | 25.6% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_SO-01_HERESY_PLUS1` | SO-01 (Patrol Familiariuszy): heresy 0 → 1 | 99.6 → 🟢 ** 99.5** (`-0.1`) | 0.4% | 25.5% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_KT-09_GOLD_PLUS1` | KT-09 (Fragment Kodeksu): gold 1 → 2 | 99.6 → 🟢 ** 99.5** (`-0.1`) | 0.4% | 25.6% | ⚪ STRATA/NEUTRALNY |
| #23 | `L1_MAX_ERAS_PLUS1` | Limit Er: 11 → 12 | 99.6 → 🟢 ** 99.5** (`-0.1`) | 0.1% | 25.6% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_KB-08_TARGET_HERESY_PLUS1` | KB-08 (Przekupstwo Sędziego): target_heresy 0 → 1 | 99.6 → 🟢 ** 99.4** (`-0.2`) | 0.5% | 25.6% | ⚪ STRATA/NEUTRALNY |