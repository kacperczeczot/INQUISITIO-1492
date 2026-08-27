[Strona główna](../../../../../README.md) > [v0.99.16](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.99.16 (Iteracja #3, Faza 1D)

**Wersja Poprzednia:** `v0.99.15` (4P: `69.3 pkt`) → **Nowa Wersja:** `v0.99.16` (4P: `69.3 pkt`)
**Data:** 2026-08-18 13:19 | **Czas Trwania Iteracji:** 656.4s | **Zysk 4P:** `0.0 pkt` | **Zysk Global:** `-0.1 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_SO-04_GOLD_PLUS1` — **SO-04 (Publiczne Ostrzeżenie): gold 0 → 1**
- **Opis Modyfikacji:** Karta `so-04` (Publiczne Ostrzeżenie): `gold` → `1`
- **Wynik Kanonu 4P Score:** 🟠 ** 69.3** pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 71.8 → 69.2 (`-2.6`) pkt
  - `4p-no-cienie`: 65.9 → 68.7 (`⬆️ +2.8`) pkt
  - `4p-no-kabala`: 61.0 → 62.9 (`⬆️ +1.9`) pkt
  - `4p-no-korona`: 84.9 → 82.7 (`-2.2`) pkt
  - `4p-no-oficjum`: 62.9 pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 14.2 → 14.5 (`⬆️ +0.3`) pkt
- **Tryb 4-osobowy (4p Avg):** 71.5 → 70.2 (`-1.3`) pkt
- **Tryb 5-osobowy (5p Avg):** 36.8 → 37.3 (`⬆️ +0.5`) pkt
- **Global Game Balance Score:** 40.8 → 🔴 ** 40.7** (`-0.1`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.15 Er`
  - **Deadlocki (Limit Er):** `0.6%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.5%` (norma: <30%)
  - **Autodafé / partię:** `2.21`
  - **Oskarżenia / partię:** `3.82`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-04_GOLD_PLUS1` | SO-04 (Publiczne Ostrzeżenie): gold 0 → 1 | 🟠 ** 69.3** | 0.6% | 1.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-04_COST_MINUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 0 | 🟠 ** 69.3** | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #3 | `L3_SO-02_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): heresy 0 → 1 | 69.3 → 🟠 ** 69.7** (`⬆️ +0.4`) | 0.6% | 1.5% | 🟢 ZYSK |
| #4 | `L3_KB-05_HERESY_PLUS1` | KB-05 (List Żelazny): heresy 0 → 1 | 69.3 → 🟠 ** 69.6** (`⬆️ +0.3`) | 0.5% | 1.5% | 🟢 ZYSK |
| #5 | `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 69.3 → 🟠 ** 69.4** (`⬆️ +0.1`) | 0.6% | 1.5% | 🟢 ZYSK |
| #6 | `L3_SO-02_GOLD_MINUS1` | SO-02 (Skarbiec Trybunału): gold 3 → 2 | 69.3 → 🟠 ** 69.4** (`⬆️ +0.1`) | 0.6% | 1.5% | 🟢 ZYSK |
| #7 | `L3_KB-03_GOLD_PLUS1` | KB-03 (Plotka Dworska): gold 0 → 1 | 69.3 → 🟠 ** 70.9** (`⬆️ +1.6`) | 0.6% | 1.6% | 🟢 ZYSK |
| #8 | `L3_GC-01_TARGET_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): target_heresy 0 → 1 | 69.3 → 🟠 ** 70.9** (`⬆️ +1.6`) | 0.6% | 1.5% | 🟢 ZYSK |
| #9 | `L3_GC-11_TARGET_HERESY_PLUS1` | GC-11 (Fałszywe Świadectwo Cechu): target_heresy 1 → 2 | 69.3 → 🟠 ** 70.5** (`⬆️ +1.2`) | 0.6% | 1.5% | 🟢 ZYSK |
| #10 | `L3_GC-11_GOLD_PLUS1` | GC-11 (Fałszywe Świadectwo Cechu): gold 0 → 1 | 69.3 → 🟠 ** 70.3** (`⬆️ +1.0`) | 0.6% | 1.5% | 🟢 ZYSK |
| #11 | `L3_SO-12_TARGET_HERESY_PLUS1` | SO-12 (Straż Trybunalska): target_heresy 0 → 1 | 69.3 → 🟠 ** 70.0** (`⬆️ +0.7`) | 0.6% | 1.5% | 🟢 ZYSK |
| #12 | `L3_KT-04_COST_PLUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 2 | 69.3 → 🟠 ** 69.7** (`⬆️ +0.4`) | 0.6% | 1.5% | 🟢 ZYSK |
| #13 | `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 69.3 → 🟠 ** 69.6** (`⬆️ +0.3`) | 0.6% | 1.5% | 🟢 ZYSK |
| #14 | `L3_KT-07_COST_MINUS1` | KT-07 (Archiwum Ukryte): cost 1 → 0 | 69.3 → 🟠 ** 69.5** (`⬆️ +0.2`) | 0.6% | 1.5% | 🟢 ZYSK |
| #15 | `L3_KT-03_HERESY_PLUS1` | KT-03 (Zakazana Wiedza): heresy 0 → 1 | 69.3 → 🟠 ** 69.4** (`⬆️ +0.1`) | 0.5% | 1.5% | 🟢 ZYSK |
| #16 | `L3_KT-07_COST_PLUS1` | KT-07 (Archiwum Ukryte): cost 1 → 2 | 69.3 → 🟠 ** 69.4** (`⬆️ +0.1`) | 0.6% | 1.5% | 🟢 ZYSK |
| #17 | `L3_KT-06_COST_PLUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 3 | 69.3 → 🟠 ** 69.1** (`-0.2`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_SO-02_TARGET_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): target_heresy 1 → 2 | 69.3 → 🟠 ** 69.9** (`⬆️ +0.6`) | 0.5% | 1.5% | 🟢 ZYSK |
| #19 | `L3_GC-02_GOLD_PLUS1` | GC-02 (Czarny Rynek): gold 3 → 4 | 69.3 → 🟠 ** 69.4** (`⬆️ +0.1`) | 0.6% | 1.5% | 🟢 ZYSK |
| #20 | `L3_GC-12_COST_PLUS1` | GC-12 (Złodziejski Zwiad): cost 0 → 1 | 69.3 → 🟠 ** 69.2** (`-0.1`) | 0.6% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_KB-10_TARGET_HERESY_PLUS1` | KB-10 (Pieczęć Korony): target_heresy 0 → 1 | 69.3 → 🟠 ** 69.2** (`-0.1`) | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_GC-11_COST_MINUS1` | GC-11 (Fałszywe Świadectwo Cechu): cost 1 → 0 | 69.3 → 🟠 ** 70.3** (`⬆️ +1.0`) | 0.6% | 1.5% | 🟢 ZYSK |
| #23 | `L3_KT-06_COST_MINUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 1 | 69.3 → 🟠 ** 69.6** (`⬆️ +0.3`) | 0.6% | 1.5% | 🟢 ZYSK |
| #24 | `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 69.3 → 🟠 ** 69.1** (`-0.2`) | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |