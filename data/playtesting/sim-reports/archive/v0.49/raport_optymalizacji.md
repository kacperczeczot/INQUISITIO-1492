[Strona główna](../../../../../README.md) > [v0.49](README.md) > [raport_optymalizacji](raport_optymalizacji.md)

---

# Raport Optymalizacji Balansu (Szalony Audytor — Progressive Beam) — Wersja v0.49 (Iteracja #7, Faza 1D)

**Wersja Poprzednia:** `v0.48` (`86.5 pkt`) → **Nowa Wersja:** `v0.49` (`86.8 pkt`)
**Data:** 2026-08-16 04:01 | **Czas Trwania Iteracji:** 1243.5s | **Zysk Global:** `+0.3 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu
- **Wybrany Wariant (1D):** `L3_KT-10_GOLD_PLUS1` — **KT-10 (Pieczęć Salomona): gold 0 → 1**
- **Opis Modyfikacji:** Karta `kt-10` (Pieczęć Salomona): `gold` → `1`
- **Global Game Balance Score:** 86.5 → 🟡 ** 86.8** (`⬆️ +0.3`) pkt
- **Rozbicie Składów Graczy:**
  - **3p:** 82.9 → 82.6 (`-0.3`) pkt
  - **4p:** 90.0 → 91.1 (`⬆️ +1.1`) pkt
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
| #1 | `L3_KT-10_GOLD_PLUS1` | KT-10 (Pieczęć Salomona): gold 0 → 1 | 86.5 → 🟡 ** 86.8** (`⬆️ +0.3`) | 82.6 | 91.1 | 0.0 | 1.5% | 27.4% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KT-01_COST_MINUS1` | KT-01 (Rytuał Przejścia): cost 1 → 0 | 86.5 → 🟡 ** 86.4** (`-0.1`) | 82.9 | 89.9 | 0.0 | 1.5% | 27.4% | ⚪ STRATA/NEUTRALNY |
| #3 | `L3_GC-02_GOLD_MINUS1` | GC-02 (Czarny Rynek): gold 2 → 1 | 86.5 → 🟡 ** 86.1** (`-0.4`) | 81.4 | 90.8 | 0.0 | 1.7% | 28.0% | ⚪ STRATA/NEUTRALNY |
| #4 | `L3_KB-08_HERESY_PLUS1` | KB-08 (Przekupstwo Sędziego): heresy 0 → 1 | 86.5 → 🟡 ** 85.9** (`-0.6`) | 83.8 | 88.0 | 0.0 | 1.6% | 27.4% | ⚪ STRATA/NEUTRALNY |
| #5 | `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 0 → 1 | 86.5 → 🟡 ** 85.8** (`-0.7`) | 83.7 | 87.9 | 0.0 | 1.5% | 27.4% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_KT-09_GOLD_PLUS1` | KT-09 (Fragment Kodeksu): gold 1 → 2 | 86.5 → 🟡 ** 85.5** (`-1.0`) | 82.3 | 88.7 | 0.0 | 1.5% | 27.4% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_GC-02_HERESY_PLUS1` | GC-02 (Czarny Rynek): heresy 1 → 2 | 86.5 → 🟡 ** 85.5** (`-1.0`) | 83.8 | 87.2 | 0.0 | 1.6% | 27.4% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_GC-07_GOLD_PLUS1` | GC-07 (Skrytobójstwo): gold 0 → 1 | 86.5 → 🟡 ** 84.8** (`-1.7`) | 81.6 | 88.1 | 0.0 | 1.5% | 27.1% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_CAA-04_COST_PLUS1` | CAA-04 (Fałszywy Trop): cost 1 → 2 | 86.5 → 🟠 ** 65.6** (`-20.9`) | 82.9 | 90.1 | 23.8 | 1.5% | 27.6% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_GC-07_HERESY_MINUS1` | GC-07 (Skrytobójstwo): heresy 1 → 0 | 86.5 → 🟠 ** 65.5** (`-21.0`) | 81.2 | 91.6 | 23.6 | 1.6% | 27.4% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_KT-06_COST_PLUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 3 | 86.5 → 🟠 ** 64.6** (`-21.9`) | 82.6 | 89.7 | 21.6 | 1.5% | 27.4% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 86.5 → 🟠 ** 64.0** (`-22.5`) | 82.4 | 89.8 | 19.9 | 1.5% | 27.4% | ⚪ STRATA/NEUTRALNY |