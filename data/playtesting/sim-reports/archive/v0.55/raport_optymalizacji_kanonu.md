# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.55 (Iteracja #3, Faza 1D)

**Wersja Poprzednia:** `v0.54` (4P: `99.7 pkt`) → **Nowa Wersja:** `v0.55` (4P: `99.8 pkt`)
**Data:** 2026-08-16 14:03 | **Czas Trwania Iteracji:** 237.4s | **Zysk 4P:** `+0.1 pkt` | **Zysk Global:** `+1.7 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_CAA-07_COST_MINUS1` — **CAA-07 (Szantaż Bractwa): cost 2 → 1**
- **Opis Modyfikacji:** Karta `caa-07` (Szantaż Bractwa): `cost` → `1`
- **Wynik Kanonu 4P Score:** 99.7 → 🟢 ** 99.8** (`⬆️ +0.1`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 99.9 → 100.0 (`⬆️ +0.1`) pkt
  - `4p-no-cienie`: 99.5 pkt
  - `4p-no-kabala`: 99.8 → 99.9 (`⬆️ +0.1`) pkt
  - `4p-no-korona`: 99.5 pkt
  - `4p-no-oficjum`: 99.8 → 100.0 (`⬆️ +0.2`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 65.9 → 59.6 (`-6.3`) pkt
- **Tryb 4-osobowy (4p Avg):** 99.6 → 99.7 (`⬆️ +0.1`) pkt
- **Tryb 5-osobowy (5p Avg):** 86.0 → 97.1 (`⬆️ +11.1`) pkt
- **Global Game Balance Score:** 83.8 → 🟡 ** 85.5** (`⬆️ +1.7`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.48 Er`
  - **Deadlocki (Limit Er):** `0.4%` (norma: <5%)
  - **Pas Biedy (Złoto):** `25.3%` (norma: <30%)
  - **Autodafé / partię:** `0.45`
  - **Oskarżenia / partię:** `3.17`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-07_COST_MINUS1` | CAA-07 (Szantaż Bractwa): cost 2 → 1 | 99.7 → 🟢 ** 99.8** (`⬆️ +0.1`) | 0.4% | 25.3% | 🌟 ZWYCIĘZCA |
| #2 | `L3_CAA-09_COST_MINUS1` | CAA-09 (Kurier Relikwii): cost 2 → 1 | 99.7 → 🟢 ** 99.8** (`⬆️ +0.1`) | 0.4% | 25.3% | 🟢 ZYSK |
| #3 | `L3_CAA-05_GOLD_PLUS1` | CAA-05 (Ukryty Kurier): gold 0 → 1 | 99.7 → 🟢 ** 99.8** (`⬆️ +0.1`) | 0.4% | 25.3% | 🟢 ZYSK |
| #4 | `L3_CAA-05_COST_MINUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 | 99.7 → 🟢 ** 99.8** (`⬆️ +0.1`) | 0.4% | 25.3% | 🟢 ZYSK |
| #5 | `L3_CAA-04_COST_MINUS1` | CAA-04 (Fałszywy Trop): cost 1 → 0 | 99.7 → 🟢 ** 99.8** (`⬆️ +0.1`) | 0.4% | 25.3% | 🟢 ZYSK |
| #6 | `L3_CAA-08_COST_MINUS1` | CAA-08 (Kaptur Nocy): cost 2 → 1 | 99.7 → 🟢 ** 99.8** (`⬆️ +0.1`) | 0.5% | 25.3% | 🟢 ZYSK |
| #7 | `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 🟢 ** 99.7** | 0.5% | 25.4% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_KT-09_GOLD_PLUS1` | KT-09 (Fragment Kodeksu): gold 1 → 2 | 🟢 ** 99.7** | 0.4% | 25.4% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_KT-09_GOLD_MINUS1` | KT-09 (Fragment Kodeksu): gold 1 → 0 | 🟢 ** 99.7** | 0.5% | 25.4% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_KT-10_COST_PLUS1` | KT-10 (Pieczęć Salomona): cost 2 → 3 | 🟢 ** 99.7** | 0.4% | 25.1% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_CAA-07_GOLD_PLUS1` | CAA-07 (Szantaż Bractwa): gold 0 → 1 | 🟢 ** 99.7** | 0.4% | 25.4% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 0 → 1 | 🟢 ** 99.7** | 0.5% | 25.6% | ⚪ STRATA/NEUTRALNY |
| #13 | `L2_CAA_ERA_MINUS1` | Cienie Era: 5 → 4 | 🟢 ** 99.7** | 0.5% | 25.4% | ⚪ STRATA/NEUTRALNY |
| #14 | `L1_MAX_ERAS_PLUS1` | Limit Er: 11 → 12 | 🟢 ** 99.7** | 0.1% | 25.4% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 1 → 2 | 🟢 ** 99.7** | 0.5% | 25.4% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_KT-10_GOLD_PLUS1` | KT-10 (Pieczęć Salomona): gold 1 → 2 | 🟢 ** 99.7** | 0.5% | 25.4% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_KT-03_GOLD_MINUS1` | KT-03 (Zakazana Wiedza): gold 1 → 0 | 🟢 ** 99.7** | 0.4% | 25.4% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_GC-01_COST_PLUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 2 | 🟢 ** 99.7** | 0.6% | 26.1% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_SO-01_HERESY_PLUS1` | SO-01 (Patrol Familiariuszy): heresy 0 → 1 | 🟢 ** 99.7** | 0.4% | 25.3% | ⚪ STRATA/NEUTRALNY |
| #20 | `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 🟢 ** 99.7** | 0.5% | 25.4% | ⚪ STRATA/NEUTRALNY |
| #21 | `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 🟢 ** 99.7** | 0.5% | 25.4% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_KB-08_TARGET_HERESY_PLUS1` | KB-08 (Przekupstwo Sędziego): target_heresy 0 → 1 | 🟢 ** 99.7** | 0.5% | 25.4% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_GC-05_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): heresy 0 → 1 | 🟢 ** 99.7** | 0.5% | 25.4% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_GC-01_GOLD_PLUS1` | GC-01 (Przekupiony Strażnik): gold 0 → 1 | 99.7 → 🟢 ** 99.6** (`-0.1`) | 0.3% | 24.5% | ⚪ STRATA/NEUTRALNY |