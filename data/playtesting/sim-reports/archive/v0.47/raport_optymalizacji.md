[Strona główna](../../../../../README.md) > [v0.47](README.md) > [raport_optymalizacji](raport_optymalizacji.md)

---

# Raport Optymalizacji Balansu (Szalony Audytor — Progressive Beam) — Wersja v0.47 (Iteracja #5, Faza 1D)

**Wersja Poprzednia:** `v0.46` (`82.8 pkt`) → **Nowa Wersja:** `v0.47` (`85.2 pkt`)
**Data:** 2026-08-16 03:19 | **Czas Trwania Iteracji:** 1384.4s | **Zysk Global:** `+2.4 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu
- **Wybrany Wariant (1D):** `L3_GC-08_COST_PLUS1` — **GC-08 (Zatrute Złoto): cost 1 → 2**
- **Opis Modyfikacji:** Karta `gc-08` (Zatrute Złoto): `cost` → `2`
- **Global Game Balance Score:** 82.8 → 🟡 ** 85.2** (`⬆️ +2.4`) pkt
- **Rozbicie Składów Graczy:**
  - **3p:** 85.2 → 82.6 (`-2.6`) pkt
  - **4p:** 80.3 → 87.8 (`⬆️ +7.5`) pkt
  - **5p:** 0.0 pkt
- **Kluczowa Telemetria Silnika:**
  - **Średnia Długość Gry:** `5.80 Er`
  - **Deadlocki (Limit Er):** `1.6%` (norma: <5%)
  - **Pas Biedy (Złoto):** `27.4%` (norma: <30%)
  - **Autodafé / partię:** `0.56`
  - **Oskarżenia / partię:** `3.73`

## 2. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści)

| Poz. | ID Wariantu | Nazwa / Opis | Global (baza → test) | 3p | 4p | 5p | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 1 → 2 | 82.8 → 🟡 ** 85.2** (`⬆️ +2.4`) | 82.6 | 87.8 | 0.0 | 1.6% | 27.4% | 🌟 ZWYCIĘZCA |
| #2 | `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 1 → 2 | 🟡 ** 82.8** | 85.6 | 80.0 | 0.0 | 1.4% | 26.4% | ⚪ STRATA/NEUTRALNY |
| #3 | `L3_KT-08_GOLD_PLUS1` | KT-08 (Areszt Wiedzy): gold 0 → 1 | 82.8 → 🟡 ** 82.2** (`-0.6`) | 84.8 | 79.7 | 0.0 | 1.4% | 26.2% | ⚪ STRATA/NEUTRALNY |
| #4 | `L3_KT-06_GOLD_PLUS1` | KT-06 (Przesłuchanie Imienia): gold 0 → 1 | 82.8 → 🟡 ** 82.2** (`-0.6`) | 85.5 | 78.8 | 0.0 | 1.3% | 26.2% | ⚪ STRATA/NEUTRALNY |
| #5 | `L3_KT-06_COST_MINUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 1 | 82.8 → 🟡 ** 82.0** (`-0.8`) | 85.4 | 78.6 | 0.0 | 1.3% | 26.2% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_SO-09_COST_PLUS1` | SO-09 (Świadek Koronny): cost 2 → 3 | 82.8 → 🟡 ** 81.6** (`-1.2`) | 84.0 | 79.2 | 0.0 | 1.3% | 26.5% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_SO-03_TARGET_HERESY_MINUS1` | SO-03 (Podejrzenie): target_heresy 1 → 0 | 82.8 → 🟡 ** 81.6** (`-1.2`) | 75.6 | 87.6 | 0.0 | 1.4% | 26.2% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_CAA-06_HERESY_MINUS1` | CAA-06 (Ucieczka z Lochów): heresy 1 → 0 | 82.8 → 🟡 ** 81.3** (`-1.5`) | 77.8 | 84.8 | 0.0 | 1.4% | 26.3% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_SO-04_COST_PLUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 2 | 82.8 → 🟡 ** 81.2** (`-1.6`) | 82.7 | 79.8 | 0.0 | 1.4% | 27.0% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_GC-07_COST_MINUS1` | GC-07 (Skrytobójstwo): cost 2 → 1 | 82.8 → 🟡 ** 80.0** (`-2.8`) | 86.6 | 73.4 | 0.0 | 1.3% | 25.6% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_GC-09_COST_PLUS1` | GC-09 (Lista Dłużników): cost 2 → 3 | 82.8 → 🟡 ** 77.8** (`-5.0`) | 83.5 | 72.0 | 0.0 | 1.6% | 26.7% | ⚪ STRATA/NEUTRALNY |
| #12 | `L4_INQUISITOR_SPEED0` | Inkwizytor Patrol: ruch 1 → 0 | 82.8 → 🟠 ** 60.0** (`-22.8`) | 83.5 | 84.3 | 12.3 | 1.4% | 26.1% | ⚪ STRATA/NEUTRALNY |