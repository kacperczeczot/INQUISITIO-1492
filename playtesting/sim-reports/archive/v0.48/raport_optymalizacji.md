# Raport Optymalizacji Balansu (Szalony Audytor — Progressive Beam) — Wersja v0.48 (Iteracja #6, Faza 1D)

**Wersja Poprzednia:** `v0.47` (`85.2 pkt`) → **Nowa Wersja:** `v0.48` (`86.5 pkt`)
**Data:** 2026-08-16 03:40 | **Czas Trwania Iteracji:** 1266.1s | **Zysk Global:** `+1.3 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu
- **Wybrany Wariant (1D):** `L3_KT-09_GOLD_PLUS1` — **KT-09 (Fragment Kodeksu): gold 0 → 1**
- **Opis Modyfikacji:** Karta `kt-09` (Fragment Kodeksu): `gold` → `1`
- **Global Game Balance Score:** 85.2 → 🟡 ** 86.5** (`⬆️ +1.3`) pkt
- **Rozbicie Składów Graczy:**
  - **3p:** 82.6 → 82.9 (`⬆️ +0.3`) pkt
  - **4p:** 87.8 → 90.0 (`⬆️ +2.2`) pkt
  - **5p:** 0.0 pkt
- **Kluczowa Telemetria Silnika:**
  - **Średnia Długość Gry:** `5.80 Er`
  - **Deadlocki (Limit Er):** `1.5%` (norma: <5%)
  - **Pas Biedy (Złoto):** `27.4%` (norma: <30%)
  - **Autodafé / partię:** `0.56`
  - **Oskarżenia / partię:** `3.73`

## 2. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści)

| Poz. | ID Wariantu | Nazwa / Opis | Global (baza → test) | 3p | 4p | 5p | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_KT-09_GOLD_PLUS1` | KT-09 (Fragment Kodeksu): gold 0 → 1 | 85.2 → 🟡 ** 86.5** (`⬆️ +1.3`) | 82.9 | 90.0 | 0.0 | 1.5% | 27.4% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KT-02_GOLD_PLUS1` | KT-02 (Transmutacja Złota): gold 2 → 3 | 85.2 → 🟡 ** 86.3** (`⬆️ +1.1`) | 81.1 | 91.6 | 0.0 | 1.6% | 27.4% | 🟢 ZYSK |
| #3 | `L3_KT-10_GOLD_PLUS1` | KT-10 (Pieczęć Salomona): gold 0 → 1 | 85.2 → 🟡 ** 86.2** (`⬆️ +1.0`) | 82.9 | 89.5 | 0.0 | 1.5% | 27.4% | 🟢 ZYSK |
| #4 | `L3_SO-09_COST_PLUS1` | SO-09 (Świadek Koronny): cost 2 → 3 | 85.2 → 🟡 ** 85.9** (`⬆️ +0.7`) | 82.0 | 89.8 | 0.0 | 1.6% | 27.8% | 🟢 ZYSK |
| #5 | `L3_KT-10_COST_MINUS1` | KT-10 (Pieczęć Salomona): cost 1 → 0 | 85.2 → 🟡 ** 85.5** (`⬆️ +0.3`) | 82.7 | 88.2 | 0.0 | 1.5% | 27.4% | 🟢 ZYSK |
| #6 | `L3_KT-01_COST_MINUS1` | KT-01 (Rytuał Przejścia): cost 1 → 0 | 85.2 → 🟡 ** 85.5** (`⬆️ +0.3`) | 82.7 | 88.2 | 0.0 | 1.6% | 27.4% | 🟢 ZYSK |
| #7 | `L3_KT-09_COST_MINUS1` | KT-09 (Fragment Kodeksu): cost 1 → 0 | 85.2 → 🟡 ** 85.5** (`⬆️ +0.3`) | 82.5 | 88.4 | 0.0 | 1.6% | 27.4% | 🟢 ZYSK |
| #8 | `L3_KT-06_GOLD_PLUS1` | KT-06 (Przesłuchanie Imienia): gold 0 → 1 | 85.2 → 🟡 ** 85.4** (`⬆️ +0.2`) | 82.7 | 88.1 | 0.0 | 1.5% | 27.4% | 🟢 ZYSK |
| #9 | `L3_KT-06_COST_MINUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 1 | 85.2 → 🟡 ** 85.3** (`⬆️ +0.1`) | 82.6 | 88.1 | 0.0 | 1.5% | 27.4% | 🟢 ZYSK |
| #10 | `L3_KT-03_COST_PLUS1` | KT-03 (Zakazana Wiedza): cost 0 → 1 | 🟡 ** 85.2** | 82.4 | 88.0 | 0.0 | 1.6% | 27.4% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_KT-08_COST_MINUS1` | KT-08 (Areszt Wiedzy): cost 2 → 1 | 85.2 → 🟡 ** 81.2** (`-4.0`) | 82.7 | 79.6 | 0.0 | 1.5% | 27.4% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-04_COST_PLUS1` | CAA-04 (Fałszywy Trop): cost 1 → 2 | 85.2 → 🟠 ** 65.0** (`-20.2`) | 82.3 | 88.3 | 24.3 | 1.5% | 27.6% | ⚪ STRATA/NEUTRALNY |