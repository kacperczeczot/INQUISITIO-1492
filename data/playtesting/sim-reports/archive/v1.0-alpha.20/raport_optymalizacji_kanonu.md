[Strona główna](../../../../../README.md) > [v1.0-alpha.20](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.20 (Iteracja #10, Faza 2D)

**Wersja Poprzednia:** `v1.0-alpha.19` (4P: `79.9 pkt`) → **Nowa Wersja:** `v1.0-alpha.20` (4P: `80.0 pkt`)
**Data:** 2026-08-21 06:28 | **Czas Trwania Iteracji:** 20733.2s | **Zysk 4P:** `+0.1 pkt` | **Zysk Global:** `+1.1 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (2D):** `L3_SO-06_TARGET_HERESY_PLUS1__L3_GC-11_HERESY_PLUS1` — **SO-06 (Areszt Trybunalski): target_heresy 0 → 1 + GC-11 (Fałszywe Świadectwo Cechu): heresy 1 → 2**
- **Opis Modyfikacji:** Karta `so-06` (Areszt Trybunalski): `target_heresy` → `1` + Karta `gc-11` (Fałszywe Świadectwo Cechu): `heresy` → `2`
- **Wynik Kanonu 4P Balance:** 79.9 → 🟡 ** 80.0** (`⬆️ +0.1`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 67.6 → 67.2 (`-0.4`) pkt
  - `4p-no-cienie`: 93.2 → 93.7 (`⬆️ +0.5`) pkt
  - `4p-no-kabala`: 61.3 pkt
  - `4p-no-korona`: 97.9 → 98.2 (`⬆️ +0.3`) pkt
  - `4p-no-oficjum`: 79.6 pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 24.1 → 24.4 (`⬆️ +0.3`) pkt
- **Tryb 4-osobowy (4p Avg):** 81.5 → 83.2 (`⬆️ +1.7`) pkt
- **Tryb 5-osobowy (5p Avg):** 28.9 → 30.2 (`⬆️ +1.3`) pkt
- **Global Game Balance Score:** 44.8 → 🔴 ** 45.9** (`⬆️ +1.1`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.23 Er`
  - **Deadlocki (Limit Er):** `0.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.5%` (norma: <30%)
  - **Autodafé / partię:** `2.20`
  - **Oskarżenia / partię:** `4.27`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-06_TARGET_HERESY_PLUS1__L3_GC-11_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): target_heresy 0 → 1 + GC-11 (Fałszywe Świadectwo Cechu): heresy 1 → 2 | 79.9 → 🟡 ** 80.0** (`⬆️ +0.1`) | 0.3% | 1.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-06_TARGET_HERESY_PLUS1__L3_SO-06_GOLD_PLUS1` | SO-06 (Areszt Trybunalski): target_heresy 0 → 1 + SO-06 (Areszt Trybunalski): gold 0 → 1 | 🟡 ** 79.9** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #3 | `L3_SO-06_TARGET_HERESY_PLUS1__L3_SO-03_GOLD_PLUS1` | SO-06 (Areszt Trybunalski): target_heresy 0 → 1 + SO-03 (Podejrzenie): gold 0 → 1 | 🟡 ** 79.9** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #4 | `L3_SO-06_TARGET_HERESY_PLUS1__L3_SO-07_COST_MINUS1` | SO-06 (Areszt Trybunalski): target_heresy 0 → 1 + SO-07 (Przesłuchanie Oficjum): cost 2 → 1 | 🟡 ** 79.9** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #5 | `L3_SO-06_TARGET_HERESY_PLUS1__L3_CAA-03_GOLD_PLUS1` | SO-06 (Areszt Trybunalski): target_heresy 0 → 1 + CAA-03 (Cień na Rynku): gold 2 → 3 | 🟡 ** 79.9** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_SO-06_TARGET_HERESY_PLUS1__L3_SO-09_COST_MINUS1` | SO-06 (Areszt Trybunalski): target_heresy 0 → 1 + SO-09 (Świadek Koronny): cost 2 → 1 | 🟡 ** 79.9** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_SO-06_TARGET_HERESY_PLUS1__L3_SO-02_GOLD_PLUS1` | SO-06 (Areszt Trybunalski): target_heresy 0 → 1 + SO-02 (Skarbiec Trybunału): gold 3 → 4 | 79.9 → 🟡 ** 79.8** (`-0.1`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_SO-06_TARGET_HERESY_PLUS1__L1_THRESHOLD_PLUS1` | SO-06 (Areszt Trybunalski): target_heresy 0 → 1 + Próg Oskarżenia: 7 → 8 | 79.9 → 🟡 ** 79.7** (`-0.2`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #9 | `L1_THRESHOLD_PLUS1__L3_SO-06_TARGET_HERESY_PLUS1` | Próg Oskarżenia: 7 → 8 + SO-06 (Areszt Trybunalski): target_heresy 0 → 1 | 79.9 → 🟡 ** 79.7** (`-0.2`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_SO-06_TARGET_HERESY_PLUS1__L3_SO-03_HERESY_MINUS1` | SO-06 (Areszt Trybunalski): target_heresy 0 → 1 + SO-03 (Podejrzenie): heresy 2 → 1 | 79.9 → 🟡 ** 79.7** (`-0.2`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_SO-02_GOLD_MINUS1__L3_SO-06_TARGET_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): gold 3 → 2 + SO-06 (Areszt Trybunalski): target_heresy 0 → 1 | 79.9 → 🟡 ** 79.6** (`-0.3`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_SO-06_TARGET_HERESY_PLUS1__L3_SO-02_GOLD_MINUS1` | SO-06 (Areszt Trybunalski): target_heresy 0 → 1 + SO-02 (Skarbiec Trybunału): gold 3 → 2 | 79.9 → 🟡 ** 79.6** (`-0.3`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |