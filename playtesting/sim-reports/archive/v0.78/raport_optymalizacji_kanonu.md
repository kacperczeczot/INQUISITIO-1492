# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.78 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v0.77` (4P: `76.2 pkt`) → **Nowa Wersja:** `v0.78` (4P: `81.3 pkt`)
**Data:** 2026-08-17 02:33 | **Czas Trwania Iteracji:** 688.5s | **Zysk 4P:** `+5.1 pkt` | **Zysk Global:** `+0.2 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L2_GC_FALLS_NO_SO_PLUS1` — **Gildia Upadki (bez Oficjum): 4 → 5**
- **Opis Modyfikacji:** Gildia Cieni: Upadki (bez Oficjum) offset +1
- **Wynik Kanonu 4P Score:** 76.2 → 🟡 ** 81.3** (`⬆️ +5.1`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 79.6 pkt
  - `4p-no-cienie`: 71.2 pkt
  - `4p-no-kabala`: 83.5 pkt
  - `4p-no-korona`: 81.5 pkt
  - `4p-no-oficjum`: 65.2 → 90.8 (`⬆️ +25.6`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 41.0 → 37.7 (`-3.3`) pkt
- **Tryb 4-osobowy (4p Avg):** 77.9 → 81.8 (`⬆️ +3.9`) pkt
- **Tryb 5-osobowy (5p Avg):** 69.2 pkt
- **Global Game Balance Score:** 62.7 → 🟠 ** 62.9** (`⬆️ +0.2`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.03 Er`
  - **Deadlocki (Limit Er):** `1.6%` (norma: <5%)
  - **Pas Biedy (Złoto):** `5.5%` (norma: <30%)
  - **Autodafé / partię:** `1.56`
  - **Oskarżenia / partię:** `3.46`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 4 → 5 | 76.2 → 🟡 ** 81.3** (`⬆️ +5.1`) | 1.6% | 5.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-02_TARGET_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): target_heresy 0 → 1 | 76.2 → 🟡 ** 80.9** (`⬆️ +4.7`) | 1.3% | 5.5% | 🟢 ZYSK |
| #3 | `L3_GC-01_TARGET_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): target_heresy 0 → 1 | 76.2 → 🟡 ** 80.3** (`⬆️ +4.1`) | 1.4% | 6.1% | 🟢 ZYSK |
| #4 | `L3_GC-09_HERESY_PLUS1` | GC-09 (Lista Dłużników): heresy 0 → 1 | 76.2 → 🟡 ** 80.0** (`⬆️ +3.8`) | 1.4% | 5.4% | 🟢 ZYSK |
| #5 | `L3_GC-01_GOLD_PLUS1` | GC-01 (Przekupiony Strażnik): gold 0 → 1 | 76.2 → 🟡 ** 79.4** (`⬆️ +3.2`) | 1.4% | 5.9% | 🟢 ZYSK |
| #6 | `L3_GC-02_HERESY_PLUS1` | GC-02 (Czarny Rynek): heresy 1 → 2 | 76.2 → 🟡 ** 78.6** (`⬆️ +2.4`) | 1.4% | 5.5% | 🟢 ZYSK |
| #7 | `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 76.2 → 🟡 ** 78.6** (`⬆️ +2.4`) | 1.4% | 5.7% | 🟢 ZYSK |
| #8 | `L3_KT-11_GOLD_PLUS1` | KT-11 (Medytacja Sefirot): gold 1 → 2 | 76.2 → 🟡 ** 78.4** (`⬆️ +2.2`) | 1.5% | 5.5% | 🟢 ZYSK |
| #9 | `L3_GC-11_HERESY_PLUS1` | GC-11 (Fałszywe Świadectwo Cechu): heresy 0 → 1 | 76.2 → 🟡 ** 78.4** (`⬆️ +2.2`) | 1.4% | 5.4% | 🟢 ZYSK |
| #10 | `L3_SO-10_TARGET_HERESY_PLUS1` | SO-10 (Oczyść Miasto): target_heresy 0 → 1 | 76.2 → 🟡 ** 78.2** (`⬆️ +2.0`) | 1.3% | 5.6% | 🟢 ZYSK |
| #11 | `L3_SO-06_TARGET_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): target_heresy 0 → 1 | 76.2 → 🟡 ** 78.2** (`⬆️ +2.0`) | 1.2% | 5.7% | 🟢 ZYSK |
| #12 | `L3_KT-02_GOLD_MINUS1` | KT-02 (Transmutacja Złota): gold 2 → 1 | 76.2 → 🟡 ** 77.8** (`⬆️ +1.6`) | 1.4% | 5.7% | 🟢 ZYSK |
| #13 | `L3_SO-09_TARGET_HERESY_PLUS1` | SO-09 (Świadek Koronny): target_heresy 0 → 1 | 76.2 → 🟡 ** 77.6** (`⬆️ +1.4`) | 1.3% | 5.6% | 🟢 ZYSK |
| #14 | `L3_SO-02_GOLD_PLUS1` | SO-02 (Skarbiec Trybunału): gold 3 → 4 | 76.2 → 🟡 ** 77.6** (`⬆️ +1.4`) | 1.4% | 5.3% | 🟢 ZYSK |
| #15 | `L3_SO-02_COST_MINUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 0 | 76.2 → 🟡 ** 77.6** (`⬆️ +1.4`) | 1.4% | 5.3% | 🟢 ZYSK |
| #16 | `L3_SO-12_HERESY_PLUS1` | SO-12 (Straż Trybunalska): heresy 0 → 1 | 76.2 → 🟡 ** 77.5** (`⬆️ +1.3`) | 1.2% | 5.5% | 🟢 ZYSK |
| #17 | `L3_SO-08_HERESY_PLUS1` | SO-08 (Nasłanie Inkwizytora): heresy 0 → 1 | 76.2 → 🟡 ** 77.3** (`⬆️ +1.1`) | 1.1% | 5.5% | 🟢 ZYSK |
| #18 | `L3_SO-09_GOLD_PLUS1` | SO-09 (Świadek Koronny): gold 0 → 1 | 76.2 → 🟡 ** 77.2** (`⬆️ +1.0`) | 1.5% | 5.5% | 🟢 ZYSK |
| #19 | `L3_SO-07_HERESY_PLUS1` | SO-07 (Przesłuchanie Oficjum): heresy 0 → 1 | 76.2 → 🟡 ** 76.6** (`⬆️ +0.4`) | 1.5% | 5.2% | 🟢 ZYSK |
| #20 | `L3_GC-02_COST_MINUS1` | GC-02 (Czarny Rynek): cost 1 → 0 | 76.2 → 🟡 ** 76.6** (`⬆️ +0.4`) | 1.4% | 5.4% | 🟢 ZYSK |
| #21 | `L3_GC-02_GOLD_PLUS1` | GC-02 (Czarny Rynek): gold 3 → 4 | 76.2 → 🟡 ** 76.6** (`⬆️ +0.4`) | 1.4% | 5.4% | 🟢 ZYSK |
| #22 | `L3_SO-03_COST_PLUS1` | SO-03 (Podejrzenie): cost 2 → 3 | 76.2 → 🟡 ** 76.3** (`⬆️ +0.1`) | 1.5% | 5.5% | 🟢 ZYSK |
| #23 | `L3_KT-07_HERESY_PLUS1` | KT-07 (Archiwum Ukryte): heresy 1 → 2 | 76.2 → 🟡 ** 75.7** (`-0.5`) | 1.5% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_CAA-09_COST_PLUS1` | CAA-09 (Kurier Relikwii): cost 2 → 3 | 76.2 → 🟡 ** 75.6** (`-0.6`) | 1.5% | 5.6% | ⚪ STRATA/NEUTRALNY |