[Strona główna](../../../../../README.md) > [v1.0-alpha.76](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.76 (Iteracja #10, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.75` (4P: `80.2 pkt`) → **Nowa Wersja:** `v1.0-alpha.76` (4P: `82.3 pkt`)
**Data:** 2026-08-24 16:19 | **Czas Trwania Iteracji:** 3153.8s | **Zysk 4P:** `+2.1 pkt` | **Zysk Global:** `+0.6 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_GC-06_COST_PLUS1` — **GC-06 (Szantaż): cost 2 → 3**
- **Opis Modyfikacji:** Karta `gc-06` (Szantaż): `cost` → `3`
- **Wynik Kanonu 4P Balance:** 80.2 → 🟡 ** 82.3** (`⬆️ +2.1`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 92.1 pkt
  - `4p-no-cienie`: 68.3 → 72.1 (`⬆️ +3.8`) pkt
  - `4p-no-kabala`: 93.9 → 94.1 (`⬆️ +0.2`) pkt
  - `4p-no-korona`: 84.9 → 87.3 (`⬆️ +2.4`) pkt
  - `4p-no-oficjum`: 61.6 → 65.9 (`⬆️ +4.3`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 28.1 pkt
- **Tryb 4-osobowy (4p Avg):** 76.6 → 78.7 (`⬆️ +2.1`) pkt
- **Tryb 5-osobowy (5p Avg):** 17.8 → 17.3 (`-0.5`) pkt
- **Global Game Balance Score:** 40.8 → 🔴 ** 41.4** (`⬆️ +0.6`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.75 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.2%` (norma: <30%)
  - **Autodafé / partię:** `1.51`
  - **Oskarżenia / partię:** `6.94`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_KB-03_COST_PLUS1` | KB-03 (Plotka Dworska): cost 1 → 2 | 80.2 → 🟡 ** 82.6** (`⬆️ +2.4`) | 0.0% | 4.9% | 🟢 ZYSK |
| #2 | `L3_GC-06_COST_PLUS1` | GC-06 (Szantaż): cost 2 → 3 | 80.2 → 🟡 ** 82.3** (`⬆️ +2.1`) | 0.0% | 4.2% | 🌟 ZWYCIĘZCA |
| #3 | `L3_KB-04_COST_MINUS1` | KB-04 (Faworyt Dworu): cost 2 → 1 | 80.2 → 🟡 ** 82.0** (`⬆️ +1.8`) | 0.0% | 3.7% | 🟢 ZYSK |
| #4 | `L3_GC-06_HERESY_MINUS1` | GC-06 (Szantaż): heresy 1 → 0 | 80.2 → 🟡 ** 82.0** (`⬆️ +1.8`) | 0.0% | 4.3% | 🟢 ZYSK |
| #5 | `L3_KB-06_COST_PLUS1` | KB-06 (Areszt Królewski): cost 2 → 3 | 80.2 → 🟡 ** 81.8** (`⬆️ +1.6`) | 0.0% | 4.3% | 🟢 ZYSK |
| #6 | `L3_SO-03_HERESY_PLUS1` | SO-03 (Podejrzenie): heresy 3 → 4 | 80.2 → 🟡 ** 81.7** (`⬆️ +1.5`) | 0.0% | 4.2% | 🟢 ZYSK |
| #7 | `L3_KT-08_TARGET_HERESY_SET1` | KT-08 (Areszt Wiedzy): dodaj target_heresy = 1 | 80.2 → 🟡 ** 81.5** (`⬆️ +1.3`) | 0.0% | 4.2% | 🟢 ZYSK |
| #8 | `L3_KT-08_TARGET_HERESY_PLUS1` | KT-08 (Areszt Wiedzy): target_heresy 0 → 1 | 80.2 → 🟡 ** 81.5** (`⬆️ +1.3`) | 0.0% | 4.2% | 🟢 ZYSK |
| #9 | `L3_SO-02_HERESY_SET2` | SO-02 (Skarbiec Trybunału): dodaj heresy = 2 | 80.2 → 🟡 ** 81.2** (`⬆️ +1.0`) | 0.0% | 4.5% | 🟢 ZYSK |
| #10 | `L3_GC-03_COST_PLUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 2 | 80.2 → 🟡 ** 80.9** (`⬆️ +0.7`) | 0.0% | 4.2% | 🟢 ZYSK |
| #11 | `L3_GC-09_COST_PLUS1` | GC-09 (Lista Dłużników): cost 1 → 2 | 80.2 → 🟡 ** 80.5** (`⬆️ +0.3`) | 0.0% | 4.3% | 🟢 ZYSK |
| #12 | `L3_GC-02_GOLD_MINUS1` | GC-02 (Czarny Rynek): gold 2 → 1 | 80.2 → 🟡 ** 80.3** (`⬆️ +0.1`) | 0.0% | 4.2% | 🟢 ZYSK |
| #13 | `L3_KT-06_COST_MINUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 1 | 80.2 → 🟡 ** 80.1** (`-0.1`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_GC-07_GOLD_PLUS1` | GC-07 (Skrytobójstwo): gold 0 → 1 | 80.2 → 🟡 ** 79.9** (`-0.3`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_GC-07_GOLD_SET1` | GC-07 (Skrytobójstwo): dodaj gold = 1 | 80.2 → 🟡 ** 79.9** (`-0.3`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_CAA-05_COST_PLUS2` | CAA-05 (Ukryty Kurier): cost 1 → 3 (+2) | 80.2 → 🟡 ** 79.4** (`-0.8`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_KB-07_TARGET_HERESY_PLUS1` | KB-07 (Szantaż Pieczęcią): target_heresy 0 → 1 | 80.2 → 🟡 ** 78.2** (`-2.0`) | 0.0% | 4.3% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_CAA-03_HERESY_PLUS1` | CAA-03 (Cień na Rynku): heresy 1 → 2 | 80.2 → 🟡 ** 77.4** (`-2.8`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_KB-11_HERESY_PLUS1` | KB-11 (Tajny Emisariusz): heresy 0 → 1 | 80.2 → 🟠 ** 74.0** (`-6.2`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #20 | `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 4 → 5 Ery | 80.2 → 🟡 ** 81.1** (`⬆️ +0.9`) | 0.0% | 4.1% | 🟢 ZYSK |