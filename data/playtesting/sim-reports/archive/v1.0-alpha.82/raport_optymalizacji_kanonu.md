# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.82 (Iteracja #2, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.81` (4P: `75.7 pkt`) → **Nowa Wersja:** `v1.0-alpha.82` (4P: `79.4 pkt`)
**Data:** 2026-08-29 01:29 | **Czas Trwania Iteracji:** 42.6s | **Zysk 4P:** `+3.7 pkt` | **Zysk Global:** `+1.8 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_SO-01_GOLD_PLUS1` — **SO-01 (Patrol Familiariuszy): gold 3 → 4**
- **Opis Modyfikacji:** Karta `so-01` (Patrol Familiariuszy): `gold` → `4`
- **Wynik Kanonu 4P Balance:** 75.7 → 🟠 ** 79.4** (`⬆️ +3.7`) pkt (±0.92)
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 75.0 → 80.8 (`⬆️ +5.8`) pkt
  - `4p-no-cienie`: 65.6 → 65.9 (`⬆️ +0.3`) pkt
  - `4p-no-kabala`: 92.1 → 91.6 (`🔻 -0.5`) pkt
  - `4p-no-korona`: 64.8 → 80.2 (`⬆️ +15.4`) pkt
  - `4p-no-oficjum`: 84.6 → 83.6 (`🔻 -1.0`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 31.5 → 32.2 (`⬆️ +0.7`) pkt
- **Tryb 4-osobowy (4p Avg):** 75.7 → 79.4 (`⬆️ +3.7`) pkt
- **Tryb 5-osobowy (5p Avg):** 23.3 → 24.3 (`⬆️ +1.0`) pkt
- **Global Game Balance Score:** 43.5 → 🔴 ** 45.3** (`⬆️ +1.8`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.81 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.4%` (norma: <30%)
  - **Autodafé / partię:** `1.56`
  - **Oskarżenia / partię:** `7.71`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | CI 95% | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 75.7 → 🟡 ** 82.1** (`⬆️ +6.4`) | `[80.3, 83.9]` | 0.0% | 4.7% | 🟢 ZYSK |
| #2 | `L3_SO-01_GOLD_PLUS1` | SO-01 (Patrol Familiariuszy): gold 3 → 4 | 75.7 → 🟡 ** 80.4** (`⬆️ +4.7`) | `[78.6, 82.2]` | 0.0% | 4.4% | 🌟 ZWYCIĘZCA |
| #3 | `L3_KB-07_COST_MINUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 1 | 75.7 → 🟠 ** 79.2** (`⬆️ +3.5`) | `[77.5, 81.0]` | 0.0% | 4.3% | 🟢 ZYSK |
| #4 | `L3_KB-06_GOLD_SET1` | KB-06 (Areszt Królewski): dodaj gold = 1 | 75.7 → 🟠 ** 79.0** (`⬆️ +3.3`) | `[77.2, 80.8]` | 0.0% | 4.5% | 🟢 ZYSK |
| #5 | `L3_KB-10_HERESY_MINUS1` | KB-10 (Pieczęć Korony): heresy 1 → 0 | 75.7 → 🟠 ** 78.9** (`⬆️ +3.2`) | `[77.2, 80.6]` | 0.0% | 4.7% | 🟢 ZYSK |
| #6 | `L3_KB-10_TARGET_HERESY_SET2` | KB-10 (Pieczęć Korony): dodaj target_heresy = 2 | 75.7 → 🟠 ** 78.2** (`⬆️ +2.5`) | `[76.4, 80.0]` | 0.0% | 4.7% | 🟢 ZYSK |
| #7 | `L3_KB-04_COST_MINUS1` | KB-04 (Faworyt Dworu): cost 2 → 1 | 75.7 → 🟠 ** 78.1** (`⬆️ +2.4`) | `[76.3, 79.9]` | 0.0% | 4.1% | 🟢 ZYSK |
| #8 | `L3_KB-10_TARGET_HERESY_PLUS1` | KB-10 (Pieczęć Korony): target_heresy 0 → 1 | 75.7 → 🟠 ** 78.1** (`⬆️ +2.4`) | `[76.3, 79.9]` | 0.0% | 4.7% | 🟢 ZYSK |