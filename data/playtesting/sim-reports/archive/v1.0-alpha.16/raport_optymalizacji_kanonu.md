# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.16 (Iteracja #6, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.15` (4P: `78.6 pkt`) → **Nowa Wersja:** `v1.0-alpha.16` (4P: `78.8 pkt`)
**Data:** 2026-08-20 23:51 | **Czas Trwania Iteracji:** 789.1s | **Zysk 4P:** `+0.2 pkt` | **Zysk Global:** `+0.1 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_SO-03_TARGET_HERESY_PLUS1` — **SO-03 (Podejrzenie): target_heresy 2 → 3**
- **Opis Modyfikacji:** Karta `so-03` (Podejrzenie): `target_heresy` → `3`
- **Wynik Kanonu 4P Balance:** 78.6 → 🟡 ** 78.8** (`⬆️ +0.2`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 67.4 → 67.2 (`-0.2`) pkt
  - `4p-no-cienie`: 93.8 → 94.6 (`⬆️ +0.8`) pkt
  - `4p-no-kabala`: 60.2 pkt
  - `4p-no-korona`: 95.5 → 95.9 (`⬆️ +0.4`) pkt
  - `4p-no-oficjum`: 76.2 pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 22.8 → 23.1 (`⬆️ +0.3`) pkt
- **Tryb 4-osobowy (4p Avg):** 80.8 → 81.1 (`⬆️ +0.3`) pkt
- **Tryb 5-osobowy (5p Avg):** 34.7 → 34.3 (`-0.4`) pkt
- **Global Game Balance Score:** 46.1 → 🔴 ** 46.2** (`⬆️ +0.1`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.23 Er`
  - **Deadlocki (Limit Er):** `0.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.5%` (norma: <30%)
  - **Autodafé / partię:** `2.22`
  - **Oskarżenia / partię:** `4.21`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-03_TARGET_HERESY_PLUS1` | SO-03 (Podejrzenie): target_heresy 2 → 3 | 78.6 → 🟡 ** 78.8** (`⬆️ +0.2`) | 0.3% | 1.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_CAA-08_COST_PLUS1` | CAA-08 (Kaptur Nocy): cost 1 → 2 | 78.6 → 🟡 ** 78.7** (`⬆️ +0.1`) | 0.3% | 1.5% | 🟢 ZYSK |
| #3 | `L3_CAA-03_GOLD_PLUS1` | CAA-03 (Cień na Rynku): gold 2 → 3 | 78.6 → 🟡 ** 78.7** (`⬆️ +0.1`) | 0.3% | 1.5% | 🟢 ZYSK |
| #4 | `L3_GC-05_COST_PLUS1` | GC-05 (Fałszywy Świadek): cost 0 → 1 | 🟡 ** 78.6** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #5 | `L3_SO-03_COST_PLUS1` | SO-03 (Podejrzenie): cost 2 → 3 | 78.6 → 🟡 ** 78.5** (`-0.1`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_SO-02_GOLD_MINUS1` | SO-02 (Skarbiec Trybunału): gold 3 → 2 | 78.6 → 🟡 ** 78.5** (`-0.1`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 78.6 → 🟡 ** 78.4** (`-0.2`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_GC-04_GOLD_PLUS1` | GC-04 (Informator): gold 0 → 1 | 78.6 → 🟡 ** 78.4** (`-0.2`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 0 → 1 | 78.6 → 🟡 ** 78.4** (`-0.2`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_CAA-02_GOLD_MINUS1` | CAA-02 (Złoto z Kryjówki): gold 3 → 2 | 78.6 → 🟡 ** 78.4** (`-0.2`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 78.6 → 🟡 ** 78.3** (`-0.3`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_SO-06_TARGET_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): target_heresy 0 → 1 | 78.6 → 🟡 ** 78.3** (`-0.3`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |