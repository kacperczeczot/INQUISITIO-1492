# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.5 (Iteracja #2, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.4` (4P: `75.9 pkt`) → **Nowa Wersja:** `v1.0-alpha.5` (4P: `76.2 pkt`)
**Data:** 2026-08-18 23:57 | **Czas Trwania Iteracji:** 453.9s | **Zysk 4P:** `+0.3 pkt` | **Zysk Global:** `+0.2 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_GC-07_COST_MINUS1` — **GC-07 (Skrytobójstwo): cost 2 → 1**
- **Opis Modyfikacji:** Karta `gc-07` (Skrytobójstwo): `cost` → `1`
- **Wynik Kanonu 4P Score:** 75.9 → 🟡 ** 76.2** (`⬆️ +0.3`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 68.0 pkt
  - `4p-no-cienie`: 86.9 → 87.0 (`⬆️ +0.1`) pkt
  - `4p-no-kabala`: 62.4 → 61.0 (`-1.4`) pkt
  - `4p-no-korona`: 89.3 → 91.2 (`⬆️ +1.9`) pkt
  - `4p-no-oficjum`: 73.1 → 74.0 (`⬆️ +0.9`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 21.0 → 20.8 (`-0.2`) pkt
- **Tryb 4-osobowy (4p Avg):** 77.7 → 79.3 (`⬆️ +1.6`) pkt
- **Tryb 5-osobowy (5p Avg):** 40.5 → 39.6 (`-0.9`) pkt
- **Global Game Balance Score:** 46.4 → 🔴 ** 46.6** (`⬆️ +0.2`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.21 Er`
  - **Deadlocki (Limit Er):** `0.5%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.6%` (norma: <30%)
  - **Autodafé / partię:** `2.22`
  - **Oskarżenia / partię:** `4.16`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-07_COST_MINUS1` | GC-07 (Skrytobójstwo): cost 2 → 1 | 75.9 → 🟡 ** 76.2** (`⬆️ +0.3`) | 0.5% | 1.6% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-02_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): heresy 0 → 1 | 75.9 → 🟡 ** 76.1** (`⬆️ +0.2`) | 0.6% | 1.6% | 🟢 ZYSK |
| #3 | `L1_MAX_ERAS_PLUS1` | Limit Er: 13 → 14 | 75.9 → 🟡 ** 76.0** (`⬆️ +0.1`) | 0.3% | 1.6% | 🟢 ZYSK |
| #4 | `L3_KT-07_COST_MINUS1` | KT-07 (Archiwum Ukryte): cost 1 → 0 | 75.9 → 🟡 ** 76.0** (`⬆️ +0.1`) | 0.5% | 1.6% | 🟢 ZYSK |
| #5 | `L3_SO-11_HERESY_PLUS1` | SO-11 (Dekret Czystości Wiary): heresy 1 → 2 | 75.9 → 🟡 ** 76.0** (`⬆️ +0.1`) | 0.5% | 1.6% | 🟢 ZYSK |
| #6 | `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 75.9 → 🟡 ** 76.0** (`⬆️ +0.1`) | 0.5% | 1.6% | 🟢 ZYSK |
| #7 | `L3_KT-11_COST_MINUS1` | KT-11 (Medytacja Sefirot): cost 1 → 0 | 75.9 → 🟡 ** 76.0** (`⬆️ +0.1`) | 0.5% | 1.6% | 🟢 ZYSK |
| #8 | `L3_GC-12_COST_PLUS1` | GC-12 (Złodziejski Zwiad): cost 0 → 1 | 🟡 ** 75.9** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #9 | `L2_CAA_ERA_MINUS1` | Cienie Era ścieżki: 1 → 0 | 🟡 ** 75.9** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #10 | `L2_CAA_ERA_PLUS1` | Cienie Era ścieżki: 1 → 2 | 🟡 ** 75.9** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #11 | `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 7 → 8 | 🟡 ** 75.9** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-01_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 🟡 ** 75.9** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 0 → 1 | 🟡 ** 75.9** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 0 → 1 | 🟡 ** 75.9** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_CAA-07_HERESY_PLUS1` | CAA-07 (Szantaż Bractwa): heresy 0 → 1 | 🟡 ** 75.9** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_CAA-09_COST_PLUS1` | CAA-09 (Kurier Relikwii): cost 0 → 1 | 🟡 ** 75.9** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_CAA-09_GOLD_PLUS1` | CAA-09 (Kurier Relikwii): gold 0 → 1 | 🟡 ** 75.9** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 🟡 ** 75.9** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_SO-02_GOLD_MINUS1` | SO-02 (Skarbiec Trybunału): gold 3 → 2 | 🟡 ** 75.9** | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_SO-10_HERESY_MINUS1` | SO-10 (Oczyść Miasto): heresy 2 → 1 | 75.9 → 🟡 ** 75.8** (`-0.1`) | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 0 → 1 | 75.9 → 🟡 ** 75.8** (`-0.1`) | 0.6% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_CAA-02_GOLD_MINUS1` | CAA-02 (Złoto z Kryjówki): gold 3 → 2 | 75.9 → 🟡 ** 75.8** (`-0.1`) | 0.6% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 1 → 2 | 75.9 → 🟡 ** 75.7** (`-0.2`) | 0.5% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 2 → 3 | 75.9 → 🟡 ** 75.2** (`-0.7`) | 0.6% | 1.6% | ⚪ STRATA/NEUTRALNY |