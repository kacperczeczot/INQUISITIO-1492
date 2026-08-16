# Raport Optymalizacji Balansu (Szalony Audytor — Progressive Beam) — Wersja v0.50 (Iteracja #8, Faza 1D)

**Wersja Poprzednia:** `v0.49` (`86.8 pkt`) → **Nowa Wersja:** `v0.50` (`86.9 pkt`)
**Data:** 2026-08-16 04:22 | **Czas Trwania Iteracji:** 1237.8s | **Zysk Global:** `+0.1 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu
- **Wybrany Wariant (1D):** `L3_KT-10_COST_PLUS1` — **KT-10 (Pieczęć Salomona): cost 1 → 2**
- **Opis Modyfikacji:** Karta `kt-10` (Pieczęć Salomona): `cost` → `2`
- **Global Game Balance Score:** 86.8 → 🟡 ** 86.9** (`⬆️ +0.1`) pkt
- **Rozbicie Składów Graczy:**
  - **3p:** 82.6 → 82.7 (`⬆️ +0.1`) pkt
  - **4p:** 91.1 pkt
  - **5p:** 0.0 pkt
- **Kluczowa Telemetria Silnika:**
  - **Średnia Długość Gry:** `5.80 Er`
  - **Deadlocki (Limit Er):** `1.5%` (norma: <5%)
  - **Pas Biedy (Złoto):** `27.4%` (norma: <30%)
  - **Autodafé / partię:** `0.56`
  - **Oskarżenia / partię:** `3.72`

## 2. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści)

| Poz. | ID Wariantu | Nazwa / Opis | Global (baza → test) | 3p | 4p | 5p | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_KT-10_COST_PLUS1` | KT-10 (Pieczęć Salomona): cost 1 → 2 | 86.8 → 🟡 ** 86.9** (`⬆️ +0.1`) | 82.7 | 91.1 | 0.0 | 1.5% | 27.4% | 🌟 ZWYCIĘZCA |
| #2 | `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 🟡 ** 86.8** | 82.6 | 91.1 | 0.0 | 1.5% | 27.4% | ⚪ STRATA/NEUTRALNY |
| #3 | `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 1 → 2 | 86.8 → 🟡 ** 86.7** (`-0.1`) | 83.6 | 89.8 | 0.0 | 1.5% | 27.4% | ⚪ STRATA/NEUTRALNY |
| #4 | `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 0 → 1 | 86.8 → 🟡 ** 86.3** (`-0.5`) | 83.4 | 89.2 | 0.0 | 1.5% | 27.4% | ⚪ STRATA/NEUTRALNY |
| #5 | `L3_KT-06_GOLD_PLUS1` | KT-06 (Przesłuchanie Imienia): gold 0 → 1 | 86.8 → 🟡 ** 86.1** (`-0.7`) | 82.7 | 89.5 | 0.0 | 1.5% | 27.4% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_GC-02_HERESY_PLUS1` | GC-02 (Czarny Rynek): heresy 1 → 2 | 86.8 → 🟡 ** 86.0** (`-0.8`) | 83.4 | 88.5 | 0.0 | 1.5% | 27.4% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_KB-08_HERESY_PLUS1` | KB-08 (Przekupstwo Sędziego): heresy 0 → 1 | 86.8 → 🟡 ** 85.8** (`-1.0`) | 83.8 | 87.8 | 0.0 | 1.6% | 27.4% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_KT-09_GOLD_PLUS1` | KT-09 (Fragment Kodeksu): gold 1 → 2 | 86.8 → 🟡 ** 85.6** (`-1.2`) | 82.2 | 88.9 | 0.0 | 1.5% | 27.4% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_KT-05_COST_PLUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 2 | 86.8 → 🟠 ** 65.9** (`-20.9`) | 83.4 | 91.4 | 22.9 | 1.5% | 27.4% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_KT-06_COST_PLUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 3 | 86.8 → 🟠 ** 64.7** (`-22.1`) | 83.0 | 90.4 | 20.6 | 1.5% | 27.4% | ⚪ STRATA/NEUTRALNY |
| #11 | `L2_CAA_ERA_MINUS1` | Cienie Era: 5 → 4 | 86.8 → 🟠 ** 64.6** (`-22.2`) | 82.6 | 91.4 | 19.9 | 1.5% | 27.4% | ⚪ STRATA/NEUTRALNY |
| #12 | `L4_SEA_ROUTE_ERA4` | Szlak Morski: Era 5 → Era 4 | 86.8 → 🟠 ** 63.2** (`-23.6`) | 82.5 | 88.9 | 18.3 | 1.5% | 27.4% | ⚪ STRATA/NEUTRALNY |