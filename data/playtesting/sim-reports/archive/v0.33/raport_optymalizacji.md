[Strona główna](../../../../../README.md) > [v0.33](README.md) > [raport_optymalizacji](raport_optymalizacji.md)

---

# Raport Optymalizacji Balansu (Outlier Hunter) — Wersja v0.33 (Iteracja #1)

**Wersja Poprzednia:** `v0.32` (`96.7 pkt`) → **Nowa Wersja:** `v0.33` (`97.2 pkt`)
**Data:** 2026-08-15 08:47 | **Czas Trwania Iteracji:** 157.9s | **Zysk Global:** `+0.5 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu
- **Wybrany Wariant:** `PAIR_so-03_cost+1__so-08_cost-1` — **SO-03 koszt 1→2 + SO-08 koszt 2→1**
- **Opis Modyfikacji:** Karta `so-03` (Podejrzenie): `cost` → `2` + Karta `so-08` (Nasłanie Inkwizytora): `cost` → `1`
- **Global Game Balance Score:** 96.7 → 🟢 ** 97.2** (`⬆️ +0.5`) pkt
- **Rozbicie Składów Graczy:**
  - **3p:** 91.9 → 93.4 (`⬆️ +1.5`) pkt
  - **4p:** 98.8 → 98.9 (`⬆️ +0.1`) pkt
  - **5p:** 99.5 → 99.4 (`-0.1`) pkt
- **Kluczowa Telemetria Silnika:**
  - **Średnia Długość Gry:** `5.56 Er`
  - **Deadlocki (Limit Er):** `1.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `26.2%` (norma: <30%)
  - **Autodafé / partię:** `1.04`
  - **Oskarżenia / partię:** `3.64`

## 2. Ranking Przebadanych Kandydatów w tej Iteracji

| Poz. | ID Wariantu | Nazwa / Opis | Global (baza → test) | 3p | 4p | 5p | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| #1 | `PAIR_so-03_cost+1__so-01_cost-1` | SO-03 koszt 1→2 + SO-01 koszt 1→0 | 96.7 → 🟢 ** 95.7** (`-1.0`) | 91.7 | 95.8 | 99.7 | 1.3% | 26.2% | ⚪ STRATA/NEUTRALNY |
| #2 | `PAIR_so-07_cost+1__so-10_heresy-1` | SO-07 koszt 2→3 + SO-10 herezja 2→1 | 96.7 → 🟢 ** 90.8** (`-5.9`) | 84.3 | 88.9 | 99.2 | 1.4% | 26.5% | ⚪ STRATA/NEUTRALNY |
| #3 | `PAIR_so-02_gold-1__so-09_cost-1` | SO-02 złoto 2→1 + SO-09 koszt 2→1 | 96.7 → 🟢 ** 97.2** (`⬆️ +0.5`) | 93.3 | 98.6 | 99.7 | 1.2% | 26.4% | 🟢 ZYSK |
| #4 | `PAIR_so-02_gold-1__so-08_cost-1` | SO-02 złoto 2→1 + SO-08 koszt 2→1 | 96.7 → 🟢 ** 96.2** (`-0.5`) | 91.6 | 97.3 | 99.6 | 1.3% | 26.3% | ⚪ STRATA/NEUTRALNY |
| #5 | `PAIR_so-03_cost+1__so-04_cost-1` | SO-03 koszt 1→2 + SO-04 koszt 1→0 | 🟢 ** 96.7** | 91.8 | 99.0 | 99.3 | 1.2% | 26.0% | ⚪ STRATA/NEUTRALNY |
| #6 | `PAIR_so-08_cost+1__so-10_heresy-1` | SO-08 koszt 2→3 + SO-10 herezja 2→1 | 96.7 → 🟢 ** 91.9** (`-4.8`) | 86.2 | 90.0 | 99.5 | 1.4% | 26.7% | ⚪ STRATA/NEUTRALNY |
| #7 | `PAIR_so-04_cost+1__so-09_cost-1` | SO-04 koszt 1→2 + SO-09 koszt 2→1 | 96.7 → 🟢 ** 96.9** (`⬆️ +0.2`) | 94.6 | 97.0 | 99.1 | 1.3% | 26.2% | 🟢 ZYSK |
| #8 | `PAIR_so-03_cost+1__so-08_cost-1` | SO-03 koszt 1→2 + SO-08 koszt 2→1 | 96.7 → 🟢 ** 97.2** (`⬆️ +0.5`) | 93.4 | 98.9 | 99.4 | 1.3% | 26.2% | 🌟 ZWYCIĘZCA |