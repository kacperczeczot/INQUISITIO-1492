# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.84 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.83` (4P: `82.4 pkt`) → **Nowa Wersja:** `v1.0-alpha.84` (4P: `83.7 pkt`)
**Data:** 2026-08-29 01:44 | **Czas Trwania Iteracji:** 40.8s | **Zysk 4P:** `+1.3 pkt` | **Zysk Global:** `+0.5 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_CAA-11_TARGET_HERESY_MINUS1` — **CAA-11 (Nocna Zmiana Warty): target_heresy 2 → 1**
- **Opis Modyfikacji:** Karta `caa-11` (Nocna Zmiana Warty): `target_heresy` → `1`
- **Wynik Kanonu 4P Balance:** 82.4 → 🟡 ** 83.7** (`⬆️ +1.3`) pkt (±0.85)
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 85.4 → 81.5 (`🔻 -3.9`) pkt
  - `4p-no-cienie`: 71.0 → 71.3 (`⬆️ +0.3`) pkt
  - `4p-no-kabala`: 95.9 → 98.9 (`⬆️ +3.0`) pkt
  - `4p-no-korona`: 77.7 → 79.5 (`⬆️ +1.8`) pkt
  - `4p-no-oficjum`: 89.2 → 94.9 (`⬆️ +5.7`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 32.4 → 32.5 (`⬆️ +0.1`) pkt
- **Tryb 4-osobowy (4p Avg):** 82.4 → 83.7 (`⬆️ +1.3`) pkt
- **Tryb 5-osobowy (5p Avg):** 24.6 → 24.7 (`⬆️ +0.1`) pkt
- **Global Game Balance Score:** 46.5 → 🔴 ** 47.0** (`⬆️ +0.5`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.74 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.8%` (norma: <30%)
  - **Autodafé / partię:** `1.51`
  - **Oskarżenia / partię:** `7.59`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | CI 95% | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-11_TARGET_HERESY_MINUS1` | CAA-11 (Nocna Zmiana Warty): target_heresy 2 → 1 | 82.4 → 🟡 ** 85.2** (`⬆️ +2.8`) | `[83.5, 86.9]` | 0.0% | 4.8% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-04_HERESY_PLUS1` | SO-04 (Publiczne Ostrzeżenie): heresy 0 → 1 | 82.4 → 🟡 ** 85.1** (`⬆️ +2.7`) | `[83.3, 86.8]` | 0.0% | 4.9% | 🟢 ZYSK |
| #3 | `L3_GC-07_GOLD_SET3` | GC-07 (Skrytobójstwo): dodaj gold = 3 | 82.4 → 🟡 ** 85.1** (`⬆️ +2.7`) | `[83.4, 86.8]` | 0.0% | 4.8% | 🟢 ZYSK |
| #4 | `L3_SO-05_COST_PLUS1` | SO-05 (Wezwanie do Trybunału): cost 0 → 1 | 82.4 → 🟡 ** 84.6** (`⬆️ +2.2`) | `[82.9, 86.3]` | 0.0% | 5.1% | 🟢 ZYSK |
| #5 | `L3_SO-02_TARGET_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): target_heresy 1 → 2 | 82.4 → 🟡 ** 84.1** (`⬆️ +1.7`) | `[82.4, 85.8]` | 0.0% | 4.8% | 🟢 ZYSK |
| #6 | `L3_CAA-01_HERESY_MINUS1` | CAA-01 (Przejście Podziemiami): heresy 1 → 0 | 82.4 → 🟡 ** 83.9** (`⬆️ +1.5`) | `[82.2, 85.6]` | 0.0% | 4.8% | 🟢 ZYSK |
| #7 | `L3_GC-07_GOLD_SET1` | GC-07 (Skrytobójstwo): dodaj gold = 1 | 82.4 → 🟡 ** 83.9** (`⬆️ +1.5`) | `[82.2, 85.6]` | 0.0% | 4.8% | 🟢 ZYSK |
| #8 | `L3_GC-03_HERESY_PLUS1` | GC-03 (Podrzucenie Księgi): heresy 2 → 3 | 82.4 → 🟡 ** 83.6** (`⬆️ +1.2`) | `[81.9, 85.3]` | 0.0% | 4.8% | 🟢 ZYSK |