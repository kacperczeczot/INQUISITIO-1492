# Raport Optymalizacji Balansu (Outlier Hunter) — Wersja v0.31 (Iteracja #1)

**Wersja Poprzednia:** `v0.30` (`94.8 pkt`) → **Nowa Wersja:** `v0.31` (`96.3 pkt`)
**Data:** 2026-08-15 07:18 | **Czas Trwania Iteracji:** 1144.0s | **Zysk Global:** `+1.5 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu
- **Wybrany Wariant:** `PAIR_kb-04_cost+1__kb-06_cost-1` — **KB-04 koszt 1→2 + KB-06 koszt 2→1**
- **Opis Modyfikacji:** Karta `kb-04` (Faworyt Dworu): `cost` → `2` + Karta `kb-06` (Areszt Królewski): `cost` → `1`
- **Global Game Balance Score:** 94.8 → 🟢 ** 96.3** (`⬆️ +1.5`) pkt
- **Rozbicie Składów Graczy:**
  - **3p:** 92.1 → 94.3 (`⬆️ +2.2`) pkt
  - **4p:** 93.5 → 95.1 (`⬆️ +1.6`) pkt
  - **5p:** 98.7 → 99.6 (`⬆️ +0.9`) pkt
- **Kluczowa Telemetria Silnika:**
  - **Średnia Długość Gry:** `5.53 Er`
  - **Deadlocki (Limit Er):** `1.1%` (norma: <5%)
  - **Pas Biedy (Złoto):** `26.1%` (norma: <30%)
  - **Autodafé / partię:** `1.02`
  - **Oskarżenia / partię:** `3.62`

## 2. Ranking Przebadanych Kandydatów w tej Iteracji

| Poz. | ID Wariantu | Nazwa / Opis | Global (baza → test) | 3p | 4p | 5p | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| #1 | `PAIR_kb-02_heresy+1__kb-06_cost-1` | KB-02 herezja 0→1 + KB-06 koszt 2→1 | 94.8 → 🟡 ** 83.7** (`-11.1`) | 82.0 | 85.3 | 0.0 | 1.0% | 25.8% | ⚪ STRATA/NEUTRALNY |
| #2 | `PAIR_kb-02_gold-1__kb-10_heresy-1` | KB-02 złoto 2→1 + KB-10 herezja 2→1 | 94.8 → 🟢 ** 91.0** (`-3.8`) | 90.7 | 91.3 | 0.0 | 1.2% | 27.2% | ⚪ STRATA/NEUTRALNY |
| #3 | `PAIR_kb-05_cost+1__kb-08_cost-1` | KB-05 koszt 2→3 + KB-08 koszt 3→2 | 94.8 → 🟡 ** 85.8** (`-9.0`) | 82.2 | 89.5 | 0.0 | 1.3% | 26.8% | ⚪ STRATA/NEUTRALNY |
| #4 | `PAIR_kb-10_cost+1__kb-01_cost-1` | KB-10 koszt 2→3 + KB-01 koszt 1→0 | 94.8 → 🟡 ** 88.8** (`-6.0`) | 89.2 | 88.4 | 0.0 | 1.2% | 26.1% | ⚪ STRATA/NEUTRALNY |
| #5 | `PAIR_kb-02_cost+1__kb-10_heresy-1` | KB-02 koszt 1→2 + KB-10 herezja 2→1 | 94.8 → 🟢 ** 91.2** (`-3.6`) | 89.5 | 92.8 | 0.0 | 1.3% | 28.7% | ⚪ STRATA/NEUTRALNY |
| #6 | `PAIR_kb-04_cost+1__kb-06_cost-1` | KB-04 koszt 1→2 + KB-06 koszt 2→1 | 94.8 → 🟢 ** 96.3** (`⬆️ +1.5`) | 94.3 | 95.1 | 99.6 | 1.1% | 26.1% | 🌟 ZWYCIĘZCA |
| #7 | `PAIR_kb-10_cost+1__kb-03_cost-1` | KB-10 koszt 2→3 + KB-03 koszt 1→0 | 94.8 → 🟡 ** 77.5** (`-17.3`) | 80.1 | 74.9 | 0.0 | 1.3% | 26.1% | ⚪ STRATA/NEUTRALNY |
| #8 | `PAIR_kb-10_cost+1__kb-05_cost-1` | KB-10 koszt 2→3 + KB-05 koszt 2→1 | 94.8 → 🟡 ** 87.0** (`-7.8`) | 89.6 | 82.6 | 88.7 | 0.9% | 27.3% | ⚪ STRATA/NEUTRALNY |