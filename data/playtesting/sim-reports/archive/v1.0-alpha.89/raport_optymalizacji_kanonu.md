# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.89 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.88` (4P: `89.3 pkt`) → **Nowa Wersja:** `v1.0-alpha.89` (4P: `90.1 pkt`)
**Data:** 2026-08-29 01:54 | **Czas Trwania Iteracji:** 42.1s | **Zysk 4P:** `+0.8 pkt` | **Zysk Global:** `+0.2 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_GC-08_TARGET_HERESY_MINUS1` — **GC-08 (Zatrute Złoto): target_heresy 1 → 0**
- **Opis Modyfikacji:** Karta `gc-08` (Zatrute Złoto): `target_heresy` → `0`
- **Wynik Kanonu 4P Balance:** 89.3 → 🟢 ** 90.1** (`⬆️ +0.8`) pkt (±0.88)
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 87.0 → 86.8 (`🔻 -0.2`) pkt
  - `4p-no-cienie`: 81.5 → 83.1 (`⬆️ +1.6`) pkt
  - `4p-no-kabala`: 95.8 → 95.1 (`🔻 -0.7`) pkt
  - `4p-no-korona`: 86.2 → 88.7 (`⬆️ +2.5`) pkt
  - `4p-no-oficjum`: 96.3 → 96.1 (`🔻 -0.2`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 33.0 → 33.0 (`= 0.0`) pkt
- **Tryb 4-osobowy (4p Avg):** 89.3 → 90.1 (`⬆️ +0.8`) pkt
- **Tryb 5-osobowy (5p Avg):** 25.5 → 25.5 (`= 0.0`) pkt
- **Global Game Balance Score:** 49.3 → 🔴 ** 49.5** (`⬆️ +0.2`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.69 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.6%` (norma: <30%)
  - **Autodafé / partię:** `1.50`
  - **Oskarżenia / partię:** `7.54`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | CI 95% | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-08_TARGET_HERESY_MINUS1` | GC-08 (Zatrute Złoto): target_heresy 1 → 0 | 89.3 → 🟢 ** 90.0** (`⬆️ +0.7`) | `[88.3, 91.7]` | 0.0% | 4.6% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KB-08_HERESY_PLUS1` | KB-08 (Przekupstwo Sędziego): heresy 2 → 3 | 89.3 → 🟢 ** 90.0** (`⬆️ +0.7`) | `[88.3, 91.7]` | 0.0% | 4.6% | 🟢 ZYSK |
| #3 | `L3_SO-02_TARGET_HERESY_MINUS1` | SO-02 (Skarbiec Trybunału): target_heresy 1 → 0 | 89.3 → 🟡 ** 89.8** (`⬆️ +0.5`) | `[88.1, 91.5]` | 0.0% | 4.7% | 🟢 ZYSK |
| #4 | `L3_CAA-01_HERESY_MINUS1` | CAA-01 (Przejście Podziemiami): heresy 1 → 0 | 89.3 → 🟡 ** 89.7** (`⬆️ +0.4`) | `[88.0, 91.4]` | 0.0% | 4.6% | 🟢 ZYSK |
| #5 | `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 89.3 → 🟡 ** 89.6** (`⬆️ +0.3`) | `[87.9, 91.3]` | 0.0% | 4.6% | 🟢 ZYSK |
| #6 | `L3_CAA-11_COST_MINUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 0 | 89.3 → 🟡 ** 89.6** (`⬆️ +0.3`) | `[87.9, 91.3]` | 0.0% | 4.6% | 🟢 ZYSK |
| #7 | `L3_GC-03_COST_MINUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 0 | 89.3 → 🟡 ** 89.5** (`⬆️ +0.2`) | `[87.8, 91.2]` | 0.0% | 4.6% | 🟢 ZYSK |
| #8 | `L3_KB-01_HERESY_PLUS1` | KB-01 (Rozkaz Dworu): heresy 1 → 2 | 89.3 → 🟡 ** 89.3** (`= 0.0`) | `[87.6, 91.0]` | 0.0% | 4.5% | ⚪ STRATA/NEUTRALNY |