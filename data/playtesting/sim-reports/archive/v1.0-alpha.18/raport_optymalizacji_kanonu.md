# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.18 (Iteracja #8, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.17` (4P: `79.4 pkt`) → **Nowa Wersja:** `v1.0-alpha.18` (4P: `79.7 pkt`)
**Data:** 2026-08-21 00:17 | **Czas Trwania Iteracji:** 772.4s | **Zysk 4P:** `+0.3 pkt` | **Zysk Global:** `-1.0 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_GC-11_HERESY_PLUS1` — **GC-11 (Fałszywe Świadectwo Cechu): heresy 0 → 1**
- **Opis Modyfikacji:** Karta `gc-11` (Fałszywe Świadectwo Cechu): `heresy` → `1`
- **Wynik Kanonu 4P Balance:** 79.4 → 🟡 ** 79.7** (`⬆️ +0.3`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 67.2 pkt
  - `4p-no-cienie`: 92.9 → 92.6 (`-0.3`) pkt
  - `4p-no-kabala`: 61.3 pkt
  - `4p-no-korona`: 96.7 → 97.9 (`⬆️ +1.2`) pkt
  - `4p-no-oficjum`: 78.8 → 79.6 (`⬆️ +0.8`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 23.9 → 24.4 (`⬆️ +0.5`) pkt
- **Tryb 4-osobowy (4p Avg):** 81.2 → 81.4 (`⬆️ +0.2`) pkt
- **Tryb 5-osobowy (5p Avg):** 32.5 → 29.0 (`-3.5`) pkt
- **Global Game Balance Score:** 45.9 → 🔴 ** 44.9** (`-1.0`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.23 Er`
  - **Deadlocki (Limit Er):** `0.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.5%` (norma: <30%)
  - **Autodafé / partię:** `2.22`
  - **Oskarżenia / partię:** `4.24`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-11_HERESY_PLUS1` | GC-11 (Fałszywe Świadectwo Cechu): heresy 0 → 1 | 79.4 → 🟡 ** 79.7** (`⬆️ +0.3`) | 0.3% | 1.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-12_COST_PLUS1` | SO-12 (Straż Trybunalska): cost 1 → 2 | 🟡 ** 79.4** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #3 | `L3_SO-02_GOLD_PLUS1` | SO-02 (Skarbiec Trybunału): gold 3 → 4 | 🟡 ** 79.4** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #4 | `L1_MAX_ERAS_PLUS1` | Limit Er: 14 → 15 | 79.4 → 🟡 ** 79.3** (`-0.1`) | 0.2% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #5 | `L3_SO-03_COST_PLUS1` | SO-03 (Podejrzenie): cost 2 → 3 | 79.4 → 🟡 ** 79.3** (`-0.1`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_SO-02_GOLD_MINUS1` | SO-02 (Skarbiec Trybunału): gold 3 → 2 | 79.4 → 🟡 ** 79.3** (`-0.1`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 0 → 1 | 79.4 → 🟡 ** 79.2** (`-0.2`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_CAA-02_GOLD_MINUS1` | CAA-02 (Złoto z Kryjówki): gold 3 → 2 | 79.4 → 🟡 ** 79.2** (`-0.2`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_SO-06_TARGET_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): target_heresy 0 → 1 | 79.4 → 🟡 ** 79.1** (`-0.3`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 79.4 → 🟡 ** 79.1** (`-0.3`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 79.4 → 🟡 ** 79.0** (`-0.4`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_GC-04_GOLD_PLUS1` | GC-04 (Informator): gold 0 → 1 | 79.4 → 🟡 ** 78.9** (`-0.5`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |