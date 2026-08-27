# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.19 (Iteracja #9, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.18` (4P: `79.7 pkt`) → **Nowa Wersja:** `v1.0-alpha.19` (4P: `79.9 pkt`)
**Data:** 2026-08-21 00:30 | **Czas Trwania Iteracji:** 767.0s | **Zysk 4P:** `+0.2 pkt` | **Zysk Global:** `-0.1 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_SO-03_HERESY_PLUS1` — **SO-03 (Podejrzenie): heresy 1 → 2**
- **Opis Modyfikacji:** Karta `so-03` (Podejrzenie): `heresy` → `2`
- **Wynik Kanonu 4P Balance:** 79.7 → 🟡 ** 79.9** (`⬆️ +0.2`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 67.2 → 67.6 (`⬆️ +0.4`) pkt
  - `4p-no-cienie`: 92.6 → 93.2 (`⬆️ +0.6`) pkt
  - `4p-no-kabala`: 61.3 pkt
  - `4p-no-korona`: 97.9 pkt
  - `4p-no-oficjum`: 79.6 pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 24.4 → 24.1 (`-0.3`) pkt
- **Tryb 4-osobowy (4p Avg):** 81.4 → 81.5 (`⬆️ +0.1`) pkt
- **Tryb 5-osobowy (5p Avg):** 29.0 → 28.9 (`-0.1`) pkt
- **Global Game Balance Score:** 44.9 → 🔴 ** 44.8** (`-0.1`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.23 Er`
  - **Deadlocki (Limit Er):** `0.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.5%` (norma: <30%)
  - **Autodafé / partię:** `2.21`
  - **Oskarżenia / partię:** `4.25`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-03_HERESY_PLUS1` | SO-03 (Podejrzenie): heresy 1 → 2 | 79.7 → 🟡 ** 79.9** (`⬆️ +0.2`) | 0.3% | 1.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-09_COST_PLUS1` | SO-09 (Świadek Koronny): cost 2 → 3 | 79.7 → 🟡 ** 79.8** (`⬆️ +0.1`) | 0.3% | 1.5% | 🟢 ZYSK |
| #3 | `L3_SO-01_COST_PLUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 2 | 🟡 ** 79.7** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #4 | `L3_SO-06_TARGET_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): target_heresy 0 → 1 | 🟡 ** 79.7** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #5 | `L3_SO-02_GOLD_PLUS1` | SO-02 (Skarbiec Trybunału): gold 3 → 4 | 79.7 → 🟡 ** 79.6** (`-0.1`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_GC-11_HERESY_PLUS1` | GC-11 (Fałszywe Świadectwo Cechu): heresy 1 → 2 | 79.7 → 🟡 ** 79.6** (`-0.1`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_SO-03_GOLD_PLUS1` | SO-03 (Podejrzenie): gold 0 → 1 | 79.7 → 🟡 ** 79.6** (`-0.1`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_KT-01_COST_MINUS1` | KT-01 (Rytuał Przejścia): cost 1 → 0 | 79.7 → 🟡 ** 79.6** (`-0.1`) | 0.3% | 1.4% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_SO-11_HERESY_PLUS1` | SO-11 (Dekret Czystości Wiary): heresy 1 → 2 | 79.7 → 🟡 ** 79.5** (`-0.2`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 0 → 1 | 79.7 → 🟡 ** 79.5** (`-0.2`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_CAA-02_GOLD_MINUS1` | CAA-02 (Złoto z Kryjówki): gold 3 → 2 | 79.7 → 🟡 ** 79.5** (`-0.2`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 79.7 → 🟡 ** 79.2** (`-0.5`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |