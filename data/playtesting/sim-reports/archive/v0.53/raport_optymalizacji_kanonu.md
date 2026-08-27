# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.53 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v0.52` (4P: `99.5 pkt`) → **Nowa Wersja:** `v0.53` (4P: `99.6 pkt`)
**Data:** 2026-08-16 13:55 | **Czas Trwania Iteracji:** 259.1s | **Zysk 4P:** `+0.1 pkt` | **Zysk Global:** `-1.3 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_GC-07_HERESY_MINUS1` — **GC-07 (Skrytobójstwo): heresy 1 → 0**
- **Opis Modyfikacji:** Karta `gc-07` (Skrytobójstwo): `heresy` → `0`
- **Wynik Kanonu 4P Score:** 99.5 → 🟢 ** 99.6** (`⬆️ +0.1`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 99.8 pkt
  - `4p-no-cienie`: 99.2 pkt
  - `4p-no-kabala`: 99.5 → 99.7 (`⬆️ +0.2`) pkt
  - `4p-no-korona`: 99.4 → 99.5 (`⬆️ +0.1`) pkt
  - `4p-no-oficjum`: 99.8 → 99.6 (`-0.2`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 74.9 → 73.2 (`-1.7`) pkt
- **Tryb 4-osobowy (4p Avg):** 99.5 pkt
- **Tryb 5-osobowy (5p Avg):** 85.7 → 83.4 (`-2.3`) pkt
- **Global Game Balance Score:** 86.7 → 🟡 ** 85.4** (`-1.3`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.53 Er`
  - **Deadlocki (Limit Er):** `0.5%` (norma: <5%)
  - **Pas Biedy (Złoto):** `25.6%` (norma: <30%)
  - **Autodafé / partię:** `0.46`
  - **Oskarżenia / partię:** `3.21`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-07_HERESY_MINUS1` | GC-07 (Skrytobójstwo): heresy 1 → 0 | 99.5 → 🟢 ** 99.6** (`⬆️ +0.1`) | 0.5% | 25.6% | 🌟 ZWYCIĘZCA |
| #2 | `L3_CAA-06_COST_MINUS1` | CAA-06 (Ucieczka z Lochów): cost 2 → 1 | 99.5 → 🟢 ** 99.6** (`⬆️ +0.1`) | 0.5% | 25.6% | 🟢 ZYSK |
| #3 | `L2_CAA_ERA_MINUS1` | Cienie Era: 5 → 4 | 99.5 → 🟢 ** 99.6** (`⬆️ +0.1`) | 0.5% | 25.6% | 🟢 ZYSK |
| #4 | `L3_KT-09_GOLD_MINUS1` | KT-09 (Fragment Kodeksu): gold 1 → 0 | 99.5 → 🟢 ** 99.6** (`⬆️ +0.1`) | 0.5% | 25.7% | 🟢 ZYSK |
| #5 | `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 99.5 → 🟢 ** 99.6** (`⬆️ +0.1`) | 0.5% | 25.7% | 🟢 ZYSK |
| #6 | `L1_MAX_ERAS_MINUS1` | Limit Er: 11 → 10 | 🟢 ** 99.5** | 1.5% | 25.7% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_CAA-02_COST_MINUS1` | CAA-02 (Złoto z Kryjówki): cost 1 → 0 | 🟢 ** 99.5** | 0.5% | 25.6% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_CAA-05_GOLD_PLUS1` | CAA-05 (Ukryty Kurier): gold 0 → 1 | 🟢 ** 99.5** | 0.5% | 25.6% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_KT-10_GOLD_PLUS1` | KT-10 (Pieczęć Salomona): gold 1 → 2 | 🟢 ** 99.5** | 0.5% | 25.7% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_CAA-05_COST_MINUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 | 🟢 ** 99.5** | 0.5% | 25.6% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_KT-05_COST_PLUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 2 | 🟢 ** 99.5** | 0.5% | 25.6% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_GC-07_COST_PLUS1` | GC-07 (Skrytobójstwo): cost 2 → 3 | 🟢 ** 99.5** | 0.4% | 25.6% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_CAA-07_GOLD_PLUS1` | CAA-07 (Szantaż Bractwa): gold 0 → 1 | 🟢 ** 99.5** | 0.4% | 25.6% | ⚪ STRATA/NEUTRALNY |
| #14 | `L1_MAX_ERAS_PLUS1` | Limit Er: 11 → 12 | 🟢 ** 99.5** | 0.1% | 25.7% | ⚪ STRATA/NEUTRALNY |
| #15 | `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 🟢 ** 99.5** | 0.5% | 25.7% | ⚪ STRATA/NEUTRALNY |
| #16 | `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 🟢 ** 99.5** | 0.5% | 25.7% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_GC-05_GOLD_PLUS1` | GC-05 (Fałszywy Świadek): gold 0 → 1 | 🟢 ** 99.5** | 0.5% | 25.7% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_KT-05_GOLD_PLUS1` | KT-05 (Wskazówka Cyklu): gold 0 → 1 | 🟢 ** 99.5** | 0.5% | 25.7% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_GC-05_COST_PLUS1` | GC-05 (Fałszywy Świadek): cost 0 → 1 | 🟢 ** 99.5** | 0.5% | 25.7% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_GC-05_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): heresy 0 → 1 | 🟢 ** 99.5** | 0.5% | 25.7% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_GC-05_TARGET_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): target_heresy 0 → 1 | 🟢 ** 99.5** | 0.5% | 25.7% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_KT-02_COST_MINUS1` | KT-02 (Transmutacja Złota): cost 1 → 0 | 🟢 ** 99.5** | 0.5% | 25.7% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_KT-07_COST_MINUS1` | KT-07 (Archiwum Ukryte): cost 1 → 0 | 🟢 ** 99.5** | 0.5% | 25.7% | ⚪ STRATA/NEUTRALNY |
| #24 | `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 99.5 → 🟢 ** 99.4** (`-0.1`) | 0.5% | 25.7% | ⚪ STRATA/NEUTRALNY |