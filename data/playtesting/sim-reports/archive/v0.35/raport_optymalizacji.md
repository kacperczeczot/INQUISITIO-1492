[Strona główna](../../../../../README.md) > [v0.35](README.md) > [raport_optymalizacji](raport_optymalizacji.md)

---

# Raport Optymalizacji Balansu (Szalony Audytor — Progressive Beam) — Wersja v0.35 (Iteracja #2, Faza 1D)

**Wersja Poprzednia:** `v0.34` (`97.5 pkt`) → **Nowa Wersja:** `v0.35` (`97.7 pkt`)
**Data:** 2026-08-15 11:12 | **Czas Trwania Iteracji:** 1197.0s | **Zysk Global:** `+0.2 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu
- **Wybrany Wariant (1D):** `L3_CAA-08_COST_PLUS1` — **CAA-08 (Kaptur Nocy): cost 1 → 2**
- **Opis Modyfikacji:** Karta `caa-08` (Kaptur Nocy): `cost` → `2`
- **Global Game Balance Score:** 97.5 → 🟢 ** 97.7** (`⬆️ +0.2`) pkt
- **Rozbicie Składów Graczy:**
  - **3p:** 93.8 → 94.5 (`⬆️ +0.7`) pkt
  - **4p:** 99.1 → 99.0 (`-0.1`) pkt
  - **5p:** 99.6 → 99.5 (`-0.1`) pkt
- **Kluczowa Telemetria Silnika:**
  - **Średnia Długość Gry:** `5.56 Er`
  - **Deadlocki (Limit Er):** `1.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `26.2%` (norma: <30%)
  - **Autodafé / partię:** `1.04`
  - **Oskarżenia / partię:** `3.62`

## 2. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści)

| Poz. | ID Wariantu | Nazwa / Opis | Global (baza → test) | 3p | 4p | 5p | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-08_COST_PLUS1` | CAA-08 (Kaptur Nocy): cost 1 → 2 | 97.5 → 🟢 ** 97.7** (`⬆️ +0.2`) | 94.5 | 99.0 | 99.5 | 1.3% | 26.2% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KT-05_COST_MINUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 0 | 🟢 ** 97.5** | 93.7 | 99.1 | 99.6 | 1.3% | 26.1% | ⚪ STRATA/NEUTRALNY |
| #3 | `L3_CAA-05_COST_MINUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 | 🟢 ** 97.5** | 93.9 | 99.1 | 99.6 | 1.3% | 26.0% | ⚪ STRATA/NEUTRALNY |
| #4 | `L3_CAA-05_GOLD_PLUS1` | CAA-05 (Ukryty Kurier): gold 0 → 1 | 🟢 ** 97.5** | 93.9 | 99.1 | 99.6 | 1.3% | 26.0% | ⚪ STRATA/NEUTRALNY |
| #5 | `L3_SO-01_COST_MINUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 0 | 97.5 → 🟢 ** 97.4** (`-0.1`) | 93.7 | 99.0 | 99.5 | 1.2% | 25.0% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 97.5 → 🟢 ** 97.3** (`-0.2`) | 93.2 | 99.1 | 99.6 | 1.3% | 26.2% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_KT-04_HERESY_PLUS1` | KT-04 (Zwierciadło Herezji): heresy 0 → 1 | 97.5 → 🟢 ** 97.3** (`-0.2`) | 93.1 | 99.2 | 99.5 | 1.5% | 26.1% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_CAA-02_GOLD_MINUS1` | CAA-02 (Złoto z Kryjówki): gold 2 → 1 | 97.5 → 🟢 ** 97.2** (`-0.3`) | 93.5 | 99.0 | 99.2 | 1.2% | 26.2% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_KT-02_GOLD_MINUS1` | KT-02 (Transmutacja Złota): gold 2 → 1 | 97.5 → 🟢 ** 97.1** (`-0.4`) | 92.6 | 99.1 | 99.6 | 1.2% | 26.1% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_KT-08_COST_MINUS1` | KT-08 (Areszt Wiedzy): cost 2 → 1 | 97.5 → 🟢 ** 97.1** (`-0.4`) | 92.5 | 99.1 | 99.6 | 1.3% | 26.1% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_GC-09_GOLD_PLUS1` | GC-09 (Lista Dłużników): gold 0 → 1 | 97.5 → 🟢 ** 97.0** (`-0.5`) | 92.5 | 99.2 | 99.3 | 1.1% | 25.9% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 1 → 2 | 97.5 → 🟢 ** 96.4** (`-1.1`) | 91.4 | 98.8 | 99.0 | 1.3% | 27.2% | ⚪ STRATA/NEUTRALNY |