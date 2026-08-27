[Strona główna](../../../../../README.md) > [v0.60](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.60 (Iteracja #2, Faza 1D)

**Wersja Poprzednia:** `v0.59` (4P: `84.5 pkt`) → **Nowa Wersja:** `v0.60` (4P: `89.8 pkt`)
**Data:** 2026-08-16 16:40 | **Czas Trwania Iteracji:** 316.8s | **Zysk 4P:** `+5.3 pkt` | **Zysk Global:** `+1.3 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_KB-08_COST_MINUS1` — **KB-08 (Przekupstwo Sędziego): cost 3 → 2**
- **Opis Modyfikacji:** Karta `kb-08` (Przekupstwo Sędziego): `cost` → `2`
- **Wynik Kanonu 4P Score:** 84.5 → 🟡 ** 89.8** (`⬆️ +5.3`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 82.4 → 93.3 (`⬆️ +10.9`) pkt
  - `4p-no-cienie`: 79.3 → 89.6 (`⬆️ +10.3`) pkt
  - `4p-no-kabala`: 83.8 → 90.7 (`⬆️ +6.9`) pkt
  - `4p-no-korona`: 83.8 pkt
  - `4p-no-oficjum`: 93.0 → 91.4 (`-1.6`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 76.8 → 74.5 (`-2.3`) pkt
- **Tryb 4-osobowy (4p Avg):** 83.9 → 87.7 (`⬆️ +3.8`) pkt
- **Tryb 5-osobowy (5p Avg):** 49.3 → 51.8 (`⬆️ +2.5`) pkt
- **Global Game Balance Score:** 70.0 → 🟠 ** 71.3** (`⬆️ +1.3`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.42 Er`
  - **Deadlocki (Limit Er):** `0.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `24.3%` (norma: <30%)
  - **Autodafé / partię:** `1.43`
  - **Oskarżenia / partię:** `3.21`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_KB-08_COST_MINUS1` | KB-08 (Przekupstwo Sędziego): cost 3 → 2 | 84.5 → 🟡 ** 89.8** (`⬆️ +5.3`) | 0.3% | 24.3% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KB-03_COST_PLUS1` | KB-03 (Plotka Dworska): cost 1 → 2 | 84.5 → 🟡 ** 89.0** (`⬆️ +4.5`) | 0.2% | 25.2% | 🟢 ZYSK |
| #3 | `L3_GC-04_HERESY_MINUS1` | GC-04 (Informator): heresy 1 → 0 | 84.5 → 🟡 ** 87.3** (`⬆️ +2.8`) | 0.3% | 24.6% | 🟢 ZYSK |
| #4 | `L3_CAA-06_HERESY_MINUS1` | CAA-06 (Ucieczka z Lochów): heresy 1 → 0 | 84.5 → 🟡 ** 86.4** (`⬆️ +1.9`) | 0.3% | 24.7% | 🟢 ZYSK |
| #5 | `L3_SO-03_COST_PLUS1` | SO-03 (Podejrzenie): cost 2 → 3 | 84.5 → 🟡 ** 86.2** (`⬆️ +1.7`) | 0.3% | 25.0% | 🟢 ZYSK |
| #6 | `L3_GC-07_GOLD_PLUS1` | GC-07 (Skrytobójstwo): gold 0 → 1 | 84.5 → 🟡 ** 85.5** (`⬆️ +1.0`) | 0.2% | 24.3% | 🟢 ZYSK |
| #7 | `L3_KB-06_COST_PLUS1` | KB-06 (Areszt Królewski): cost 1 → 2 | 84.5 → 🟡 ** 85.4** (`⬆️ +0.9`) | 0.2% | 25.1% | 🟢 ZYSK |
| #8 | `L3_SO-01_GOLD_PLUS1` | SO-01 (Patrol Familiariuszy): gold 0 → 1 | 84.5 → 🟡 ** 85.2** (`⬆️ +0.7`) | 0.3% | 24.1% | 🟢 ZYSK |
| #9 | `L3_KT-08_COST_PLUS1` | KT-08 (Areszt Wiedzy): cost 2 → 3 | 84.5 → 🟡 ** 85.0** (`⬆️ +0.5`) | 0.3% | 24.6% | 🟢 ZYSK |
| #10 | `L3_SO-02_GOLD_MINUS1` | SO-02 (Skarbiec Trybunału): gold 2 → 1 | 84.5 → 🟡 ** 84.8** (`⬆️ +0.3`) | 0.3% | 25.3% | 🟢 ZYSK |
| #11 | `L3_KT-09_GOLD_MINUS1` | KT-09 (Fragment Kodeksu): gold 1 → 0 | 84.5 → 🟡 ** 84.7** (`⬆️ +0.2`) | 0.3% | 24.5% | 🟢 ZYSK |
| #12 | `L3_SO-02_GOLD_PLUS1` | SO-02 (Skarbiec Trybunału): gold 2 → 3 | 84.5 → 🟡 ** 84.6** (`⬆️ +0.1`) | 0.4% | 24.2% | 🟢 ZYSK |
| #13 | `L3_CAA-07_GOLD_PLUS1` | CAA-07 (Szantaż Bractwa): gold 0 → 1 | 84.5 → 🟡 ** 84.6** (`⬆️ +0.1`) | 0.3% | 24.6% | 🟢 ZYSK |
| #14 | `L3_KT-06_COST_PLUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 3 | 🟡 ** 84.5** | 0.3% | 24.3% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_CAA-08_COST_PLUS1` | CAA-08 (Kaptur Nocy): cost 2 → 3 | 84.5 → 🟡 ** 84.3** (`-0.2`) | 0.3% | 24.7% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_KB-01_COST_PLUS1` | KB-01 (Rozkaz Dworu): cost 1 → 2 | 84.5 → 🟡 ** 84.2** (`-0.3`) | 0.2% | 25.1% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_SO-02_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): heresy 0 → 1 | 84.5 → 🟡 ** 84.1** (`-0.4`) | 0.3% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 2 → 3 | 84.5 → 🟡 ** 84.0** (`-0.5`) | 0.3% | 24.9% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_SO-07_COST_PLUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 3 | 84.5 → 🟡 ** 83.8** (`-0.7`) | 0.3% | 25.0% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_KB-03_TARGET_HERESY_MINUS1` | KB-03 (Plotka Dworska): target_heresy 1 → 0 | 84.5 → 🟡 ** 83.7** (`-0.8`) | 0.3% | 24.6% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_GC-07_HERESY_PLUS1` | GC-07 (Skrytobójstwo): heresy 0 → 1 | 84.5 → 🟡 ** 83.4** (`-1.1`) | 0.3% | 24.5% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_KB-10_HERESY_MINUS1` | KB-10 (Pieczęć Korony): heresy 2 → 1 | 84.5 → 🟡 ** 83.2** (`-1.3`) | 0.4% | 25.0% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_KB-06_HERESY_PLUS1` | KB-06 (Areszt Królewski): heresy 0 → 1 | 84.5 → 🟡 ** 83.1** (`-1.4`) | 0.3% | 24.4% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_SO-06_COST_MINUS1` | SO-06 (Areszt Trybunalski): cost 2 → 1 | 84.5 → 🟡 ** 82.6** (`-1.9`) | 0.3% | 24.0% | ⚪ STRATA/NEUTRALNY |