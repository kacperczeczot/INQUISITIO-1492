# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.70 (Iteracja #4, Faza 2D)

**Wersja Poprzednia:** `v1.0-alpha.69` (4P: `73.3 pkt`) → **Nowa Wersja:** `v1.0-alpha.70` (4P: `75.6 pkt`)
**Data:** 2026-08-24 08:08 | **Czas Trwania Iteracji:** 603.0s | **Zysk 4P:** `+2.3 pkt` | **Zysk Global:** `+0.7 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (2D):** `L1_OBSERVED_MINUS1__L3_CAA-01_COST_PLUS1` — **Próg Obserwowanej: 5 → 4 + CAA-01 (Przejście Podziemiami): cost 0 → 1**
- **Opis Modyfikacji:** Próg Obserwowanej: offset -1 (nowy: 4) + Karta `caa-01` (Przejście Podziemiami): `cost` → `1`
- **Wynik Kanonu 4P Balance:** 73.3 → 🟡 ** 75.6** (`⬆️ +2.3`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 75.9 → 89.5 (`⬆️ +13.6`) pkt
  - `4p-no-cienie`: 67.8 → 58.0 (`-9.8`) pkt
  - `4p-no-kabala`: 75.8 → 93.0 (`⬆️ +17.2`) pkt
  - `4p-no-korona`: 80.7 → 78.1 (`-2.6`) pkt
  - `4p-no-oficjum`: 66.3 → 59.5 (`-6.8`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 30.6 → 32.1 (`⬆️ +1.5`) pkt
- **Tryb 4-osobowy (4p Avg):** 63.7 → 70.9 (`⬆️ +7.2`) pkt
- **Tryb 5-osobowy (5p Avg):** 27.2 → 20.6 (`-6.6`) pkt
- **Global Game Balance Score:** 40.5 → 🔴 ** 41.2** (`⬆️ +0.7`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.78 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.2%` (norma: <30%)
  - **Autodafé / partię:** `1.53`
  - **Oskarżenia / partię:** `6.68`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L1_OBSERVED_MINUS1__L3_CAA-01_COST_PLUS1` | Próg Obserwowanej: 5 → 4 + CAA-01 (Przejście Podziemiami): cost 0 → 1 | 73.3 → 🟡 ** 75.6** (`⬆️ +2.3`) | 0.0% | 4.2% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-06_GOLD_SET2__L3_CAA-06_GOLD_SET3` | SO-06 (Areszt Trybunalski): dodaj gold = 2 + CAA-06 (Ucieczka z Lochów): dodaj gold = 3 | 73.3 → 🟡 ** 75.3** (`⬆️ +2.0`) | 0.0% | 4.1% | 🟢 ZYSK |
| #3 | `L3_SO-06_GOLD_SET2__L3_CAA-06_TARGET_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): dodaj gold = 2 + CAA-06 (Ucieczka z Lochów): target_heresy 2 → 3 | 73.3 → 🟠 ** 74.7** (`⬆️ +1.4`) | 0.0% | 4.1% | 🟢 ZYSK |
| #4 | `L3_SO-06_GOLD_SET2__L3_CAA-06_GOLD_SET2` | SO-06 (Areszt Trybunalski): dodaj gold = 2 + CAA-06 (Ucieczka z Lochów): dodaj gold = 2 | 73.3 → 🟠 ** 74.4** (`⬆️ +1.1`) | 0.0% | 4.1% | 🟢 ZYSK |
| #5 | `L3_SO-12_COST_MINUS1__L3_CAA-06_COST_PLUS1` | SO-12 (Straż Trybunalska): cost 1 → 0 + CAA-06 (Ucieczka z Lochów): cost 0 → 1 | 73.3 → 🟠 ** 74.3** (`⬆️ +1.0`) | 0.0% | 4.0% | 🟢 ZYSK |
| #6 | `L3_SO-05_TARGET_HERESY_MINUS1__L3_CAA-01_HERESY_SET1` | SO-05 (Wezwanie do Trybunału): target_heresy 1 → 0 + CAA-01 (Przejście Podziemiami): dodaj heresy = 1 | 73.3 → 🟠 ** 73.5** (`⬆️ +0.2`) | 0.0% | 4.4% | 🟢 ZYSK |
| #7 | `L3_SO-05_TARGET_HERESY_MINUS1__L3_CAA-01_HERESY_PLUS1` | SO-05 (Wezwanie do Trybunału): target_heresy 1 → 0 + CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 73.3 → 🟠 ** 73.5** (`⬆️ +0.2`) | 0.0% | 4.4% | 🟢 ZYSK |
| #8 | `L3_SO-12_COST_MINUS1__L1_START_GOLD_PLUS1` | SO-12 (Straż Trybunalska): cost 1 → 0 + Złoto startowe: 4zł → 5zł | 🟠 ** 73.3** | 0.0% | 3.2% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_SO-01_HERESY_SET2__L3_CAA-10_GOLD_SET2` | SO-01 (Patrol Familiariuszy): dodaj heresy = 2 + CAA-10 (Echo Alhambry): dodaj gold = 2 | 73.3 → 🟠 ** 73.0** (`-0.3`) | 0.0% | 4.7% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_SO-06_GOLD_SET2__L3_CAA-06_COST_PLUS1` | SO-06 (Areszt Trybunalski): dodaj gold = 2 + CAA-06 (Ucieczka z Lochów): cost 0 → 1 | 73.3 → 🟡 ** 75.4** (`⬆️ +2.1`) | 0.0% | 4.1% | 🟢 ZYSK |
| #11 | `L3_SO-06_GOLD_SET2__L3_CAA-04_TARGET_HERESY_MINUS1` | SO-06 (Areszt Trybunalski): dodaj gold = 2 + CAA-04 (Fałszywy Trop): target_heresy 1 → 0 | 73.3 → 🟡 ** 77.3** (`⬆️ +4.0`) | 0.0% | 4.1% | 🟢 ZYSK |
| #12 | `L3_SO-05_TARGET_HERESY_MINUS1__L3_CAA-01_TARGET_HERESY_MINUS1` | SO-05 (Wezwanie do Trybunału): target_heresy 1 → 0 + CAA-01 (Przejście Podziemiami): target_heresy 1 → 0 | 73.3 → 🟠 ** 74.0** (`⬆️ +0.7`) | 0.0% | 4.4% | 🟢 ZYSK |
| #13 | `L3_SO-05_TARGET_HERESY_MINUS1__L3_CAA-01_HERESY_SET2` | SO-05 (Wezwanie do Trybunału): target_heresy 1 → 0 + CAA-01 (Przejście Podziemiami): dodaj heresy = 2 | 73.3 → 🟠 ** 73.6** (`⬆️ +0.3`) | 0.0% | 4.4% | 🟢 ZYSK |
| #14 | `L3_SO-05_TARGET_HERESY_MINUS1__L3_CAA-03_TARGET_HERESY_SET2` | SO-05 (Wezwanie do Trybunału): target_heresy 1 → 0 + CAA-03 (Cień na Rynku): dodaj target_heresy = 2 | 73.3 → 🟡 ** 76.3** (`⬆️ +3.0`) | 0.0% | 4.4% | 🟢 ZYSK |
| #15 | `L1_OBSERVED_MINUS1__L3_CAA-07_TARGET_HERESY_SET1` | Próg Obserwowanej: 5 → 4 + CAA-07 (Szantaż Bractwa): dodaj target_heresy = 1 | 73.3 → 🟠 ** 74.5** (`⬆️ +1.2`) | 0.0% | 4.4% | 🟢 ZYSK |
| #16 | `L1_OBSERVED_MINUS1__L3_CAA-07_TARGET_HERESY_PLUS1` | Próg Obserwowanej: 5 → 4 + CAA-07 (Szantaż Bractwa): target_heresy 0 → 1 | 73.3 → 🟠 ** 74.5** (`⬆️ +1.2`) | 0.0% | 4.4% | 🟢 ZYSK |
| #17 | `L3_SO-06_GOLD_SET2__L3_CAA-03_TARGET_HERESY_SET2` | SO-06 (Areszt Trybunalski): dodaj gold = 2 + CAA-03 (Cień na Rynku): dodaj target_heresy = 2 | 73.3 → 🟡 ** 75.5** (`⬆️ +2.2`) | 0.0% | 4.1% | 🟢 ZYSK |
| #18 | `L3_SO-06_GOLD_SET2__L3_CAA-05_TARGET_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): dodaj gold = 2 + CAA-05 (Ukryty Kurier): target_heresy 2 → 3 | 73.3 → 🟡 ** 76.5** (`⬆️ +3.2`) | 0.0% | 4.1% | 🟢 ZYSK |
| #19 | `L3_SO-01_HERESY_SET2__L3_CAA-04_TARGET_HERESY_MINUS1` | SO-01 (Patrol Familiariuszy): dodaj heresy = 2 + CAA-04 (Fałszywy Trop): target_heresy 1 → 0 | 73.3 → 🟡 ** 76.3** (`⬆️ +3.0`) | 0.0% | 4.7% | 🟢 ZYSK |
| #20 | `L1_HAND_LIMIT_PLUS1__L3_CAA-03_TARGET_HERESY_PLUS1` | Limit ręki: 5 → 6 + CAA-03 (Cień na Rynku): target_heresy 0 → 1 | 73.3 → 🟠 ** 63.6** (`-9.7`) | 0.0% | 3.7% | ⚪ STRATA/NEUTRALNY |