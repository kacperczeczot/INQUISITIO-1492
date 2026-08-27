[Strona główna](../../../../../README.md) > [v0.34](README.md) > [raport_optymalizacji](raport_optymalizacji.md)

---

# Raport Optymalizacji Balansu (Szalony Audytor — Progressive Beam) — Wersja v0.34 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v0.33` (`97.2 pkt`) → **Nowa Wersja:** `v0.34` (`97.5 pkt`)
**Data:** 2026-08-15 10:52 | **Czas Trwania Iteracji:** 1997.9s | **Zysk Global:** `+0.3 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu
- **Wybrany Wariant (1D):** `L3_CAA-01_GOLD_PLUS1` — **CAA-01 (Przejście Podziemiami): gold 0 → 1**
- **Opis Modyfikacji:** Karta `caa-01` (Przejście Podziemiami): `gold` → `1`
- **Global Game Balance Score:** 97.2 → 🟢 ** 97.5** (`⬆️ +0.3`) pkt
- **Rozbicie Składów Graczy:**
  - **3p:** 93.4 → 93.8 (`⬆️ +0.4`) pkt
  - **4p:** 98.9 → 99.1 (`⬆️ +0.2`) pkt
  - **5p:** 99.4 → 99.6 (`⬆️ +0.2`) pkt
- **Kluczowa Telemetria Silnika:**
  - **Średnia Długość Gry:** `5.55 Er`
  - **Deadlocki (Limit Er):** `1.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `26.1%` (norma: <30%)
  - **Autodafé / partię:** `1.04`
  - **Oskarżenia / partię:** `3.62`

## 2. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści)

| Poz. | ID Wariantu | Nazwa / Opis | Global (baza → test) | 3p | 4p | 5p | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-01_GOLD_PLUS1` | CAA-01 (Przejście Podziemiami): gold 0 → 1 | 97.2 → 🟢 ** 97.5** (`⬆️ +0.3`) | 93.8 | 99.1 | 99.6 | 1.3% | 26.1% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-10_GOLD_PLUS1` | SO-10 (Oczyść Miasto): gold 0 → 1 | 97.2 → 🟢 ** 97.4** (`⬆️ +0.2`) | 94.0 | 99.0 | 99.3 | 1.2% | 25.6% | 🟢 ZYSK |
| #3 | `L3_KT-09_GOLD_PLUS1` | KT-09 (Fragment Kodeksu): gold 0 → 1 | 97.2 → 🟢 ** 97.3** (`⬆️ +0.1`) | 93.5 | 99.0 | 99.3 | 1.3% | 26.2% | 🟢 ZYSK |
| #4 | `L3_KT-08_COST_MINUS1` | KT-08 (Areszt Wiedzy): cost 2 → 1 | 97.2 → 🟢 ** 97.1** (`-0.1`) | 92.9 | 98.9 | 99.5 | 1.3% | 26.2% | ⚪ STRATA/NEUTRALNY |
| #5 | `L3_CAA-03_GOLD_PLUS1` | CAA-03 (Cień na Rynku): gold 0 → 1 | 97.2 → 🟢 ** 97.0** (`-0.2`) | 93.8 | 97.7 | 99.5 | 1.3% | 26.1% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_SO-07_GOLD_PLUS1` | SO-07 (Przesłuchanie Oficjum): gold 0 → 1 | 97.2 → 🟢 ** 97.0** (`-0.2`) | 92.7 | 99.0 | 99.2 | 1.2% | 25.4% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_CAA-05_COST_MINUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 | 97.2 → 🟢 ** 96.9** (`-0.3`) | 93.6 | 97.6 | 99.5 | 1.3% | 26.1% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_CAA-05_GOLD_PLUS1` | CAA-05 (Ukryty Kurier): gold 0 → 1 | 97.2 → 🟢 ** 96.9** (`-0.3`) | 93.6 | 97.6 | 99.5 | 1.3% | 26.1% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_CAA-08_GOLD_PLUS1` | CAA-08 (Kaptur Nocy): gold 0 → 1 | 97.2 → 🟢 ** 96.7** (`-0.5`) | 93.2 | 97.2 | 99.6 | 1.3% | 26.1% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_KT-08_COST_PLUS1` | KT-08 (Areszt Wiedzy): cost 2 → 3 | 97.2 → 🟢 ** 96.7** (`-0.5`) | 93.7 | 96.8 | 99.6 | 1.3% | 26.2% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 97.2 → 🟢 ** 96.5** (`-0.7`) | 93.0 | 97.6 | 98.9 | 1.3% | 26.3% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_SO-01_COST_MINUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 0 | 97.2 → 🟢 ** 96.2** (`-1.0`) | 93.0 | 95.9 | 99.6 | 1.2% | 25.2% | ⚪ STRATA/NEUTRALNY |