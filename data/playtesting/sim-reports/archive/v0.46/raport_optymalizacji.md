# Raport Optymalizacji Balansu (Szalony Audytor — Progressive Beam) — Wersja v0.46 (Iteracja #4, Faza 1D)

**Wersja Poprzednia:** `v0.45` (`79.3 pkt`) → **Nowa Wersja:** `v0.46` (`82.8 pkt`)
**Data:** 2026-08-16 02:56 | **Czas Trwania Iteracji:** 1568.4s | **Zysk Global:** `+3.5 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu
- **Wybrany Wariant (1D):** `L3_KT-07_HERESY_PLUS1` — **KT-07 (Archiwum Ukryte): heresy 0 → 1**
- **Opis Modyfikacji:** Karta `kt-07` (Archiwum Ukryte): `heresy` → `1`
- **Global Game Balance Score:** 79.3 → 🟡 ** 82.8** (`⬆️ +3.5`) pkt
- **Rozbicie Składów Graczy:**
  - **3p:** 71.3 → 85.2 (`⬆️ +13.9`) pkt
  - **4p:** 87.3 → 80.3 (`-7.0`) pkt
  - **5p:** 0.0 pkt
- **Kluczowa Telemetria Silnika:**
  - **Średnia Długość Gry:** `5.74 Er`
  - **Deadlocki (Limit Er):** `1.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `26.2%` (norma: <30%)
  - **Autodafé / partię:** `0.55`
  - **Oskarżenia / partię:** `3.76`

## 2. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści)

| Poz. | ID Wariantu | Nazwa / Opis | Global (baza → test) | 3p | 4p | 5p | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_KT-07_HERESY_PLUS1` | KT-07 (Archiwum Ukryte): heresy 0 → 1 | 79.3 → 🟡 ** 82.8** (`⬆️ +3.5`) | 85.2 | 80.3 | 0.0 | 1.3% | 26.2% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KT-05_HERESY_PLUS1` | KT-05 (Wskazówka Cyklu): heresy 0 → 1 | 79.3 → 🟡 ** 82.0** (`⬆️ +2.7`) | 83.0 | 81.0 | 0.0 | 1.2% | 26.1% | 🟢 ZYSK |
| #3 | `L3_KT-01_HERESY_PLUS1` | KT-01 (Rytuał Przejścia): heresy 0 → 1 | 79.3 → 🟡 ** 81.9** (`⬆️ +2.6`) | 84.9 | 78.9 | 0.0 | 1.3% | 26.2% | 🟢 ZYSK |
| #4 | `L3_SO-09_COST_PLUS1` | SO-09 (Świadek Koronny): cost 2 → 3 | 79.3 → 🟡 ** 81.8** (`⬆️ +2.5`) | 69.8 | 93.9 | 0.0 | 1.2% | 26.5% | 🟢 ZYSK |
| #5 | `L3_KT-04_COST_PLUS1` | KT-04 (Zwierciadło Herezji): cost 0 → 1 | 79.3 → 🟡 ** 80.7** (`⬆️ +1.4`) | 71.4 | 89.9 | 0.0 | 1.2% | 26.2% | 🟢 ZYSK |
| #6 | `L3_GC-04_COST_PLUS1` | GC-04 (Informator): cost 0 → 1 | 79.3 → 🟡 ** 80.3** (`⬆️ +1.0`) | 67.5 | 93.1 | 0.0 | 1.5% | 27.2% | 🟢 ZYSK |
| #7 | `L3_KB-08_GOLD_PLUS1` | KB-08 (Przekupstwo Sędziego): gold 0 → 1 | 79.3 → 🟡 ** 80.2** (`⬆️ +0.9`) | 68.7 | 91.6 | 0.0 | 1.1% | 26.0% | 🟢 ZYSK |
| #8 | `L3_KB-03_HERESY_PLUS1` | KB-03 (Plotka Dworska): heresy 0 → 1 | 79.3 → 🟡 ** 79.7** (`⬆️ +0.4`) | 74.0 | 85.3 | 0.0 | 1.1% | 26.0% | 🟢 ZYSK |
| #9 | `L3_GC-06_HERESY_PLUS1` | GC-06 (Szantaż): heresy 0 → 1 | 79.3 → 🟡 ** 79.6** (`⬆️ +0.3`) | 74.4 | 84.7 | 0.0 | 1.1% | 26.1% | 🟢 ZYSK |
| #10 | `L3_SO-04_COST_PLUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 2 | 79.3 → 🟡 ** 79.5** (`⬆️ +0.2`) | 69.1 | 89.9 | 0.0 | 1.3% | 27.0% | 🟢 ZYSK |
| #11 | `L3_GC-07_COST_MINUS1` | GC-07 (Skrytobójstwo): cost 2 → 1 | 79.3 → 🟡 ** 78.0** (`-1.3`) | 71.7 | 84.2 | 0.0 | 1.2% | 25.6% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 1 → 2 | 79.3 → 🟠 ** 64.4** (`-14.9`) | 62.3 | 95.5 | 35.3 | 1.4% | 27.4% | ⚪ STRATA/NEUTRALNY |