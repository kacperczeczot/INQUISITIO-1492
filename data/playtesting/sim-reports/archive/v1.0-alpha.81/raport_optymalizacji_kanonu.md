# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.81 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.80` (4P: `75.7 pkt`) → **Nowa Wersja:** `v1.0-alpha.81` (4P: `80.0 pkt`)
**Data:** 2026-08-29 01:28 | **Czas Trwania Iteracji:** 42.7s | **Zysk 4P:** `+4.3 pkt` | **Zysk Global:** `+2.1 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_SO-01_GOLD_PLUS1` — **SO-01 (Patrol Familiariuszy): gold 2 → 3**
- **Opis Modyfikacji:** Karta `so-01` (Patrol Familiariuszy): `gold` → `3`
- **Wynik Kanonu 4P Balance:** 75.7 → 🟡 ** 80.0** (`⬆️ +4.3`) pkt (±0.91)
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 75.2 → 79.4 (`⬆️ +4.2`) pkt
  - `4p-no-cienie`: 64.8 → 66.9 (`⬆️ +2.1`) pkt
  - `4p-no-kabala`: 89.9 → 95.3 (`⬆️ +5.4`) pkt
  - `4p-no-korona`: 65.6 → 78.8 (`⬆️ +13.2`) pkt
  - `4p-no-oficjum`: 83.7 → 85.0 (`⬆️ +1.3`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 31.5 → 32.3 (`⬆️ +0.8`) pkt
- **Tryb 4-osobowy (4p Avg):** 75.7 → 80.0 (`⬆️ +4.3`) pkt
- **Tryb 5-osobowy (5p Avg):** 23.3 → 24.5 (`⬆️ +1.2`) pkt
- **Global Game Balance Score:** 43.5 → 🔴 ** 45.6** (`⬆️ +2.1`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.81 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.5%` (norma: <30%)
  - **Autodafé / partię:** `1.53`
  - **Oskarżenia / partię:** `7.68`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | CI 95% | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-01_GOLD_PLUS1` | SO-01 (Patrol Familiariuszy): gold 2 → 3 | 75.7 → 🟡 ** 81.1** (`⬆️ +5.4`) | `[79.3, 82.9]` | 0.0% | 4.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-12_HERESY_PLUS1` | SO-12 (Straż Trybunalska): heresy 1 → 2 | 75.7 → 🟡 ** 80.0** (`⬆️ +4.3`) | `[78.2, 81.8]` | 0.0% | 4.8% | 🟢 ZYSK |
| #3 | `L3_KB-03_COST_PLUS1` | KB-03 (Plotka Dworska): cost 1 → 2 | 75.7 → 🟠 ** 79.9** (`⬆️ +4.2`) | `[78.2, 81.6]` | 0.0% | 5.3% | 🟢 ZYSK |
| #4 | `L3_SO-01_COST_MINUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 0 | 75.7 → 🟠 ** 79.8** (`⬆️ +4.1`) | `[78.0, 81.6]` | 0.0% | 3.9% | 🟢 ZYSK |
| #5 | `L3_KB-06_GOLD_SET1` | KB-06 (Areszt Królewski): dodaj gold = 1 | 75.7 → 🟠 ** 78.7** (`⬆️ +3.0`) | `[76.9, 80.5]` | 0.0% | 4.5% | 🟢 ZYSK |
| #6 | `L3_KB-04_COST_MINUS1` | KB-04 (Faworyt Dworu): cost 2 → 1 | 75.7 → 🟠 ** 78.5** (`⬆️ +2.8`) | `[76.7, 80.3]` | 0.0% | 4.1% | 🟢 ZYSK |
| #7 | `L3_KB-01_COST_PLUS1` | KB-01 (Rozkaz Dworu): cost 1 → 2 | 75.7 → 🟠 ** 78.2** (`⬆️ +2.5`) | `[76.5, 79.9]` | 0.0% | 5.5% | 🟢 ZYSK |
| #8 | `L3_SO-12_TARGET_HERESY_MINUS1` | SO-12 (Straż Trybunalska): target_heresy 1 → 0 | 75.7 → 🟠 ** 78.2** (`⬆️ +2.5`) | `[76.4, 80.0]` | 0.0% | 4.7% | 🟢 ZYSK |