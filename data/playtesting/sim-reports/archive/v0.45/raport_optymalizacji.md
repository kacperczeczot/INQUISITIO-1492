[Strona główna](../../../../../README.md) > [v0.45](README.md) > [raport_optymalizacji](raport_optymalizacji.md)

---

# Raport Optymalizacji Balansu (Szalony Audytor — Progressive Beam) — Wersja v0.45 (Iteracja #3, Faza 1D)

**Wersja Poprzednia:** `v0.44` (`73.8 pkt`) → **Nowa Wersja:** `v0.45` (`79.3 pkt`)
**Data:** 2026-08-16 02:30 | **Czas Trwania Iteracji:** 1573.2s | **Zysk Global:** `+5.5 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu
- **Wybrany Wariant (1D):** `L3_GC-02_COST_PLUS1` — **GC-02 (Czarny Rynek): cost 1 → 2**
- **Opis Modyfikacji:** Karta `gc-02` (Czarny Rynek): `cost` → `2`
- **Global Game Balance Score:** 73.8 → 🟡 ** 79.3** (`⬆️ +5.5`) pkt
- **Rozbicie Składów Graczy:**
  - **3p:** 72.5 → 71.3 (`-1.2`) pkt
  - **4p:** 75.1 → 87.3 (`⬆️ +12.2`) pkt
  - **5p:** 0.0 pkt
- **Kluczowa Telemetria Silnika:**
  - **Średnia Długość Gry:** `5.72 Er`
  - **Deadlocki (Limit Er):** `1.2%` (norma: <5%)
  - **Pas Biedy (Złoto):** `26.2%` (norma: <30%)
  - **Autodafé / partię:** `0.55`
  - **Oskarżenia / partię:** `3.62`

## 2. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści)

| Poz. | ID Wariantu | Nazwa / Opis | Global (baza → test) | 3p | 4p | 5p | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-02_COST_PLUS1` | GC-02 (Czarny Rynek): cost 1 → 2 | 73.8 → 🟡 ** 79.3** (`⬆️ +5.5`) | 71.3 | 87.3 | 0.0 | 1.2% | 26.2% | 🌟 ZWYCIĘZCA |
| #2 | `L3_GC-02_GOLD_MINUS1` | GC-02 (Czarny Rynek): gold 2 → 1 | 73.8 → 🟡 ** 79.0** (`⬆️ +5.2`) | 73.2 | 84.8 | 0.0 | 1.3% | 25.5% | 🟢 ZYSK |
| #3 | `L3_GC-06_COST_PLUS1` | GC-06 (Szantaż): cost 2 → 3 | 73.8 → 🟡 ** 76.8** (`⬆️ +3.0`) | 72.2 | 81.4 | 0.0 | 1.3% | 25.4% | 🟢 ZYSK |
| #4 | `L3_KB-08_GOLD_PLUS1` | KB-08 (Przekupstwo Sędziego): gold 0 → 1 | 73.8 → 🟡 ** 75.2** (`⬆️ +1.4`) | 70.1 | 80.4 | 0.0 | 1.0% | 24.7% | 🟢 ZYSK |
| #5 | `L3_CAA-03_COST_PLUS1` | CAA-03 (Cień na Rynku): cost 0 → 1 | 73.8 → 🟠 ** 74.9** (`⬆️ +1.1`) | 72.9 | 76.9 | 0.0 | 1.1% | 25.0% | 🟢 ZYSK |
| #6 | `L3_KB-08_COST_MINUS1` | KB-08 (Przekupstwo Sędziego): cost 3 → 2 | 73.8 → 🟠 ** 74.8** (`⬆️ +1.0`) | 69.9 | 79.6 | 0.0 | 1.1% | 24.7% | 🟢 ZYSK |
| #7 | `L3_KT-10_GOLD_PLUS1` | KT-10 (Pieczęć Salomona): gold 0 → 1 | 73.8 → 🟠 ** 74.2** (`⬆️ +0.4`) | 72.5 | 75.9 | 0.0 | 1.1% | 24.9% | 🟢 ZYSK |
| #8 | `L3_KT-10_COST_MINUS1` | KT-10 (Pieczęć Salomona): cost 1 → 0 | 73.8 → 🟠 ** 74.1** (`⬆️ +0.3`) | 72.4 | 75.7 | 0.0 | 1.1% | 24.9% | 🟢 ZYSK |
| #9 | `L3_CAA-08_COST_PLUS1` | CAA-08 (Kaptur Nocy): cost 2 → 3 | 73.8 → 🟠 ** 73.5** (`-0.3`) | 71.5 | 75.5 | 0.0 | 1.1% | 25.0% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_KT-08_COST_MINUS1` | KT-08 (Areszt Wiedzy): cost 2 → 1 | 73.8 → 🟠 ** 73.5** (`-0.3`) | 72.4 | 74.6 | 0.0 | 1.1% | 24.9% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_CAA-09_COST_PLUS1` | CAA-09 (Kurier Relikwii): cost 2 → 3 | 73.8 → 🟠 ** 72.2** (`-1.6`) | 67.3 | 77.0 | 0.0 | 1.1% | 25.1% | ⚪ STRATA/NEUTRALNY |
| #12 | `L2_KB_ERA_MINUS1` | Korona Era: 5/5/5 → 4/4/4 | 73.8 → 🔴 ** 53.1** (`-20.7`) | 71.0 | 86.0 | 2.4 | 1.1% | 24.7% | ⚪ STRATA/NEUTRALNY |