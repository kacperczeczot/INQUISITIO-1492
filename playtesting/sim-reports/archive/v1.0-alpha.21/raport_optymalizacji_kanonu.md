# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.21 (Iteracja #11, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.20` (4P: `80.0 pkt`) → **Nowa Wersja:** `v1.0-alpha.21` (4P: `80.1 pkt`)
**Data:** 2026-08-21 07:41 | **Czas Trwania Iteracji:** 4329.2s | **Zysk 4P:** `+0.1 pkt` | **Zysk Global:** `+0.2 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_SO-09_COST_MINUS1` — **SO-09 (Świadek Koronny): cost 2 → 1**
- **Opis Modyfikacji:** Karta `so-09` (Świadek Koronny): `cost` → `1`
- **Wynik Kanonu 4P Balance:** 80.0 → 🟡 ** 80.1** (`⬆️ +0.1`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 67.2 → 67.3 (`⬆️ +0.1`) pkt
  - `4p-no-cienie`: 93.7 → 93.8 (`⬆️ +0.1`) pkt
  - `4p-no-kabala`: 61.3 pkt
  - `4p-no-korona`: 98.2 → 98.5 (`⬆️ +0.3`) pkt
  - `4p-no-oficjum`: 79.6 pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 24.4 pkt
- **Tryb 4-osobowy (4p Avg):** 83.2 → 83.3 (`⬆️ +0.1`) pkt
- **Tryb 5-osobowy (5p Avg):** 30.2 → 30.5 (`⬆️ +0.3`) pkt
- **Global Game Balance Score:** 45.9 → 🔴 ** 46.1** (`⬆️ +0.2`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.23 Er`
  - **Deadlocki (Limit Er):** `0.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.5%` (norma: <30%)
  - **Autodafé / partię:** `2.20`
  - **Oskarżenia / partię:** `4.27`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-09_COST_MINUS1` | SO-09 (Świadek Koronny): cost 2 → 1 | 80.0 → 🟡 ** 80.1** (`⬆️ +0.1`) | 0.3% | 1.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-09_COST_PLUS1` | SO-09 (Świadek Koronny): cost 2 → 3 | 80.0 → 🟡 ** 80.1** (`⬆️ +0.1`) | 0.3% | 1.5% | 🟢 ZYSK |
| #3 | `L3_SO-03_HERESY_MINUS1` | SO-03 (Podejrzenie): heresy 2 → 1 | 80.0 → 🟡 ** 80.1** (`⬆️ +0.1`) | 0.3% | 1.5% | 🟢 ZYSK |
| #4 | `L3_SO-07_COST_MINUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 1 | 80.0 → 🟡 ** 80.1** (`⬆️ +0.1`) | 0.3% | 1.5% | 🟢 ZYSK |
| #5 | `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 7 → 8 | 🟡 ** 80.0** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_SO-03_GOLD_PLUS1` | SO-03 (Podejrzenie): gold 0 → 1 | 🟡 ** 80.0** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_SO-06_GOLD_PLUS1` | SO-06 (Areszt Trybunalski): gold 0 → 1 | 🟡 ** 80.0** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_CAA-01_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 🟡 ** 80.0** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_SO-11_HERESY_MINUS1` | SO-11 (Dekret Czystości Wiary): heresy 1 → 0 | 80.0 → 🟡 ** 79.9** (`-0.1`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 80.0 → 🟡 ** 79.8** (`-0.2`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 0 → 1 | 80.0 → 🟡 ** 79.8** (`-0.2`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-02_GOLD_MINUS1` | CAA-02 (Złoto z Kryjówki): gold 3 → 2 | 80.0 → 🟡 ** 79.8** (`-0.2`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |