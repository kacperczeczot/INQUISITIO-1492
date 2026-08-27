[Strona główna](../../../../../README.md) > [v1.0-alpha.22](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.22 (Iteracja #12, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.21` (4P: `80.1 pkt`) → **Nowa Wersja:** `v1.0-alpha.22` (4P: `80.3 pkt`)
**Data:** 2026-08-21 07:53 | **Czas Trwania Iteracji:** 745.9s | **Zysk 4P:** `+0.2 pkt` | **Zysk Global:** `-0.4 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_SO-10_HERESY_MINUS1` — **SO-10 (Oczyść Miasto): heresy 2 → 1**
- **Opis Modyfikacji:** Karta `so-10` (Oczyść Miasto): `heresy` → `1`
- **Wynik Kanonu 4P Balance:** 80.1 → 🟡 ** 80.3** (`⬆️ +0.2`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 67.3 pkt
  - `4p-no-cienie`: 93.8 → 93.7 (`-0.1`) pkt
  - `4p-no-kabala`: 61.3 → 61.2 (`-0.1`) pkt
  - `4p-no-korona`: 98.5 → 99.5 (`⬆️ +1.0`) pkt
  - `4p-no-oficjum`: 79.6 pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 24.4 → 24.3 (`-0.1`) pkt
- **Tryb 4-osobowy (4p Avg):** 83.3 → 83.5 (`⬆️ +0.2`) pkt
- **Tryb 5-osobowy (5p Avg):** 30.5 → 29.2 (`-1.3`) pkt
- **Global Game Balance Score:** 46.1 → 🔴 ** 45.7** (`-0.4`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.24 Er`
  - **Deadlocki (Limit Er):** `0.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.5%` (norma: <30%)
  - **Autodafé / partię:** `2.25`
  - **Oskarżenia / partię:** `4.26`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-10_HERESY_MINUS1` | SO-10 (Oczyść Miasto): heresy 2 → 1 | 80.1 → 🟡 ** 80.3** (`⬆️ +0.2`) | 0.3% | 1.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-03_HERESY_MINUS1` | SO-03 (Podejrzenie): heresy 2 → 1 | 80.1 → 🟡 ** 80.2** (`⬆️ +0.1`) | 0.3% | 1.5% | 🟢 ZYSK |
| #3 | `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 7 → 8 | 🟡 ** 80.1** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #4 | `L3_CAA-01_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 🟡 ** 80.1** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #5 | `L3_CAA-09_COST_PLUS1` | CAA-09 (Kurier Relikwii): cost 0 → 1 | 🟡 ** 80.1** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 0 → 1 | 🟡 ** 80.1** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_CAA-09_GOLD_PLUS1` | CAA-09 (Kurier Relikwii): gold 0 → 1 | 🟡 ** 80.1** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_CAA-07_HERESY_PLUS1` | CAA-07 (Szantaż Bractwa): heresy 0 → 1 | 🟡 ** 80.1** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 0 → 1 | 🟡 ** 80.1** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_SO-11_HERESY_MINUS1` | SO-11 (Dekret Czystości Wiary): heresy 1 → 0 | 80.1 → 🟡 ** 80.0** (`-0.1`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_CAA-02_GOLD_MINUS1` | CAA-02 (Złoto z Kryjówki): gold 3 → 2 | 80.1 → 🟡 ** 79.9** (`-0.2`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 0 → 1 | 80.1 → 🟡 ** 79.9** (`-0.2`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |