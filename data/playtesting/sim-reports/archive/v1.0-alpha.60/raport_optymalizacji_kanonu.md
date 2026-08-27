# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.60 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.59` (4P: `56.0 pkt`) → **Nowa Wersja:** `v1.0-alpha.60` (4P: `60.4 pkt`)
**Data:** 2026-08-23 22:43 | **Czas Trwania Iteracji:** 899.3s | **Zysk 4P:** `+4.4 pkt` | **Zysk Global:** `+2.5 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L2_GC_FALLS_PLUS1` — **Gildia Upadki: 8 → 9**
- **Opis Modyfikacji:** Gildia Cieni: Upadki offset +1
- **Wynik Kanonu 4P Balance:** 56.0 → 🟠 ** 60.4** (`⬆️ +4.4`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 67.1 pkt
  - `4p-no-cienie`: 57.3 → 45.5 (`-11.8`) pkt
  - `4p-no-kabala`: 48.1 → 69.8 (`⬆️ +21.7`) pkt
  - `4p-no-korona`: 69.8 → 62.4 (`-7.4`) pkt
  - `4p-no-oficjum`: 37.8 → 57.3 (`⬆️ +19.5`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 17.9 → 21.4 (`⬆️ +3.5`) pkt
- **Tryb 4-osobowy (4p Avg):** 48.3 → 54.4 (`⬆️ +6.1`) pkt
- **Tryb 5-osobowy (5p Avg):** 9.4 → 7.3 (`-2.1`) pkt
- **Global Game Balance Score:** 25.2 → 🔴 ** 27.7** (`⬆️ +2.5`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.82 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `5.6%` (norma: <30%)
  - **Autodafé / partię:** `1.36`
  - **Oskarżenia / partię:** `6.72`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_KT-09_GOLD_SET3` | KT-09 (Fragment Kodeksu): dodaj gold = 3 | 56.0 → 🔴 ** 55.3** (`-0.7`) | 0.0% | 5.4% | ⚪ STRATA/NEUTRALNY |
| #2 | `L2_GC_FALLS_PLUS2` | Gildia Upadki: 8 → 10 | 56.0 → 🔴 ** 54.9** (`-1.1`) | 0.0% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #3 | `L2_GC_FALLS_PLUS1` | Gildia Upadki: 8 → 9 | 56.0 → 🟠 ** 60.4** (`⬆️ +4.4`) | 0.0% | 5.6% | 🌟 ZWYCIĘZCA |
| #4 | `L3_GC-11_GOLD_SET2` | GC-11 (Fałszywe Świadectwo Cechu): dodaj gold = 2 | 56.0 → 🔴 ** 56.3** (`⬆️ +0.3`) | 0.0% | 5.5% | 🟢 ZYSK |
| #5 | `L3_CAA-05_TARGET_HERESY_SET2` | CAA-05 (Ukryty Kurier): dodaj target_heresy = 2 | 56.0 → 🔴 ** 58.9** (`⬆️ +2.9`) | 0.0% | 5.5% | 🟢 ZYSK |
| #6 | `L3_GC-10_HERESY_PLUS1` | GC-10 (Upadek Domu): heresy 2 → 3 | 56.0 → 🔴 ** 59.1** (`⬆️ +3.1`) | 0.0% | 5.5% | 🟢 ZYSK |
| #7 | `L3_GC-10_GOLD_PLUS1` | GC-10 (Upadek Domu): gold 0 → 1 | 56.0 → 🔴 ** 59.1** (`⬆️ +3.1`) | 0.0% | 5.5% | 🟢 ZYSK |
| #8 | `L3_GC-10_GOLD_SET1` | GC-10 (Upadek Domu): dodaj gold = 1 | 56.0 → 🔴 ** 59.1** (`⬆️ +3.1`) | 0.0% | 5.5% | 🟢 ZYSK |
| #9 | `L3_KB-03_COST_MINUS1` | KB-03 (Plotka Dworska): cost 1 → 0 | 56.0 → 🔴 ** 57.3** (`⬆️ +1.3`) | 0.0% | 4.7% | 🟢 ZYSK |
| #10 | `L3_GC-01_TARGET_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): target_heresy 0 → 1 | 56.0 → 🔴 ** 57.5** (`⬆️ +1.5`) | 0.0% | 5.5% | 🟢 ZYSK |
| #11 | `L3_GC-09_HERESY_SET2` | GC-09 (Lista Dłużników): dodaj heresy = 2 | 56.0 → 🔴 ** 59.1** (`⬆️ +3.1`) | 0.0% | 5.4% | 🟢 ZYSK |
| #12 | `L4_SEA_ROUTE_ERA_MINUS1` | Szlak Morski: Era 4 → 3 | 56.0 → 🟠 ** 61.8** (`⬆️ +5.8`) | 0.0% | 5.4% | 🟢 ZYSK |
| #13 | `L3_CAA-10_COST_MINUS1` | CAA-10 (Echo Alhambry): cost 3 → 2 | 56.0 → 🟠 ** 67.8** (`⬆️ +11.8`) | 0.0% | 5.4% | 🟢 ZYSK |
| #14 | `L3_CAA-10_GOLD_SET2` | CAA-10 (Echo Alhambry): dodaj gold = 2 | 56.0 → 🟠 ** 67.8** (`⬆️ +11.8`) | 0.0% | 5.4% | 🟢 ZYSK |
| #15 | `L3_CAA-10_GOLD_SET3` | CAA-10 (Echo Alhambry): dodaj gold = 3 | 56.0 → 🟠 ** 70.9** (`⬆️ +14.9`) | 0.0% | 5.4% | 🟢 ZYSK |
| #16 | `L3_CAA-10_TARGET_HERESY_SET1` | CAA-10 (Echo Alhambry): dodaj target_heresy = 1 | 56.0 → 🟠 ** 68.3** (`⬆️ +12.3`) | 0.0% | 5.4% | 🟢 ZYSK |
| #17 | `L3_CAA-10_TARGET_HERESY_PLUS1` | CAA-10 (Echo Alhambry): target_heresy 0 → 1 | 56.0 → 🟠 ** 68.3** (`⬆️ +12.3`) | 0.0% | 5.4% | 🟢 ZYSK |
| #18 | `L3_CAA-10_TARGET_HERESY_SET2` | CAA-10 (Echo Alhambry): dodaj target_heresy = 2 | 56.0 → 🟠 ** 66.4** (`⬆️ +10.4`) | 0.0% | 5.5% | 🟢 ZYSK |
| #19 | `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 4 → 5 Ery | 56.0 → 🟠 ** 63.9** (`⬆️ +7.9`) | 0.0% | 5.4% | 🟢 ZYSK |
| #20 | `L1_CARDS_PER_ERA_PLUS1` | Karty/Erę: 2 → 3 | 56.0 → 🔴 ** 52.0** (`-4.0`) | 0.0% | 14.3% | ⚪ STRATA/NEUTRALNY |