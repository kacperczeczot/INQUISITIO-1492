[Strona główna](../../../../../README.md) > [v0.32](README.md) > [raport_optymalizacji](raport_optymalizacji.md)

---

# Raport Optymalizacji Balansu (Outlier Hunter) — Wersja v0.32 (Iteracja #2)

**Wersja Poprzednia:** `v0.31` (`96.3 pkt`) → **Nowa Wersja:** `v0.32` (`96.7 pkt`)
**Data:** 2026-08-15 07:53 | **Czas Trwania Iteracji:** 173.9s | **Zysk Global:** `+0.4 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu
- **Wybrany Wariant:** `PAIR_gc-02_heresy+1__so-08_heresy-1` — **GC-02 herezja 0→1 + SO-08 herezja 1→0**
- **Opis Modyfikacji:** Karta `gc-02` (Czarny Rynek): `heresy` → `1` + Karta `so-08` (Nasłanie Inkwizytora): `heresy` → `0`
- **Global Game Balance Score:** 96.3 → 🟢 ** 96.7** (`⬆️ +0.4`) pkt
- **Rozbicie Składów Graczy:**
  - **3p:** 94.3 → 91.9 (`-2.4`) pkt
  - **4p:** 95.1 → 98.8 (`⬆️ +3.7`) pkt
  - **5p:** 99.6 → 99.5 (`-0.1`) pkt
- **Kluczowa Telemetria Silnika:**
  - **Średnia Długość Gry:** `5.55 Er`
  - **Deadlocki (Limit Er):** `1.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `26.2%` (norma: <30%)
  - **Autodafé / partię:** `1.03`
  - **Oskarżenia / partię:** `3.65`

## 2. Ranking Przebadanych Kandydatów w tej Iteracji

| Poz. | ID Wariantu | Nazwa / Opis | Global (baza → test) | 3p | 4p | 5p | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| #1 | `PAIR_gc-02_cost+1__so-01_cost-1` | GC-02 koszt 1→2 + SO-01 koszt 1→0 | 96.3 → 🟢 ** 93.5** (`-2.8`) | 83.2 | 98.6 | 98.8 | 1.1% | 26.8% | ⚪ STRATA/NEUTRALNY |
| #2 | `PAIR_gc-02_cost+1__so-10_cost-1` | GC-02 koszt 1→2 + SO-10 koszt 4→3 | 96.3 → 🟡 ** 88.2** (`-8.1`) | 77.5 | 98.9 | 88.3 | 0.9% | 26.6% | ⚪ STRATA/NEUTRALNY |
| #3 | `PAIR_gc-10_heresy+1__so-10_heresy-1` | GC-10 herezja 2→3 + SO-10 herezja 2→1 | 96.3 → 🟡 ** 85.8** (`-10.5`) | 79.6 | 87.9 | 89.8 | 1.1% | 26.2% | ⚪ STRATA/NEUTRALNY |
| #4 | `PAIR_gc-02_heresy+1__so-08_heresy-1` | GC-02 herezja 0→1 + SO-08 herezja 1→0 | 96.3 → 🟢 ** 96.7** (`⬆️ +0.4`) | 91.9 | 98.8 | 99.5 | 1.3% | 26.2% | 🌟 ZWYCIĘZCA |
| #5 | `PAIR_gc-02_gold-1__so-04_cost-1` | GC-02 złoto 2→1 + SO-04 koszt 1→0 | 96.3 → 🟢 ** 93.3** (`-3.0`) | 82.0 | 98.8 | 99.2 | 1.1% | 25.7% | ⚪ STRATA/NEUTRALNY |
| #6 | `PAIR_gc-04_heresy+1__so-05_tgheresy+1` | GC-04 herezja 1→2 + SO-05 wrobienie 2→3 | 96.3 → 🟢 ** 93.2** (`-3.1`) | 85.1 | 95.2 | 99.3 | 1.0% | 26.0% | ⚪ STRATA/NEUTRALNY |
| #7 | `PAIR_gc-06_cost+1__so-06_cost-1` | GC-06 koszt 2→3 + SO-06 koszt 2→1 | 96.3 → 🟢 ** 96.2** (`-0.1`) | 92.1 | 97.1 | 99.5 | 1.3% | 25.7% | ⚪ STRATA/NEUTRALNY |
| #8 | `PAIR_gc-06_heresy+1__so-05_tgheresy+1` | GC-06 herezja 0→1 + SO-05 wrobienie 2→3 | 🟢 ** 96.3** | 93.6 | 95.7 | 99.7 | 1.0% | 26.0% | ⚪ STRATA/NEUTRALNY |