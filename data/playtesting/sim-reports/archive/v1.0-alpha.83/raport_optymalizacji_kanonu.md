# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.83 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.82` (4P: `81.3 pkt`) → **Nowa Wersja:** `v1.0-alpha.83` (4P: `82.4 pkt`)
**Data:** 2026-08-29 01:43 | **Czas Trwania Iteracji:** 43.1s | **Zysk 4P:** `+1.1 pkt` | **Zysk Global:** `+0.5 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_CAA-10_COST_MINUS1` — **CAA-10 (Echo Alhambry): cost 3 → 2**
- **Opis Modyfikacji:** Karta `caa-10` (Echo Alhambry): `cost` → `2`
- **Wynik Kanonu 4P Balance:** 81.3 → 🟡 ** 82.4** (`⬆️ +1.1`) pkt (±0.89)
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 80.3 → 86.8 (`⬆️ +6.5`) pkt
  - `4p-no-cienie`: 70.7 → 72.1 (`⬆️ +1.4`) pkt
  - `4p-no-kabala`: 98.0 → 96.7 (`🔻 -1.3`) pkt
  - `4p-no-korona`: 72.4 → 82.4 (`⬆️ +10.0`) pkt
  - `4p-no-oficjum`: 86.8 → 91.1 (`⬆️ +4.3`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 32.3 → 32.4 (`⬆️ +0.1`) pkt
- **Tryb 4-osobowy (4p Avg):** 81.3 → 82.4 (`⬆️ +1.1`) pkt
- **Tryb 5-osobowy (5p Avg):** 24.4 → 24.6 (`⬆️ +0.2`) pkt
- **Global Game Balance Score:** 46.0 → 🔴 ** 46.5** (`⬆️ +0.5`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.71 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.8%` (norma: <30%)
  - **Autodafé / partię:** `1.50`
  - **Oskarżenia / partię:** `7.59`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | CI 95% | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 81.3 → 🟡 ** 86.8** (`⬆️ +5.5`) | `[85.1, 88.5]` | 0.0% | 4.9% | 🟢 ZYSK |
| #2 | `L3_CAA-10_COST_MINUS1` | CAA-10 (Echo Alhambry): cost 3 → 2 | 81.3 → 🟡 ** 85.8** (`⬆️ +4.5`) | `[84.1, 87.5]` | 0.0% | 4.8% | 🌟 ZWYCIĘZCA |
| #3 | `L3_KT-10_GOLD_SET1` | KT-10 (Pieczęć Salomona): dodaj gold = 1 | 81.3 → 🟡 ** 84.8** (`⬆️ +3.5`) | `[83.1, 86.5]` | 0.0% | 4.7% | 🟢 ZYSK |
| #4 | `L3_SO-06_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): heresy 0 → 1 | 81.3 → 🟡 ** 84.5** (`⬆️ +3.2`) | `[82.7, 86.3]` | 0.0% | 4.9% | 🟢 ZYSK |
| #5 | `L3_SO-04_COST_PLUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 2 | 81.3 → 🟡 ** 84.4** (`⬆️ +3.1`) | `[82.6, 86.2]` | 0.0% | 5.2% | 🟢 ZYSK |
| #6 | `L3_KT-01_GOLD_PLUS1` | KT-01 (Rytuał Przejścia): gold 0 → 1 | 81.3 → 🟡 ** 84.3** (`⬆️ +3.0`) | `[82.6, 86.0]` | 0.0% | 4.7% | 🟢 ZYSK |
| #7 | `L3_SO-09_HERESY_PLUS1` | SO-09 (Świadek Koronny): heresy 0 → 1 | 81.3 → 🟡 ** 84.0** (`⬆️ +2.7`) | `[82.3, 85.7]` | 0.0% | 4.7% | 🟢 ZYSK |
| #8 | `L3_GC-05_GOLD_PLUS1` | GC-05 (Fałszywy Świadek): gold 0 → 1 | 81.3 → 🟡 ** 84.0** (`⬆️ +2.7`) | `[82.3, 85.7]` | 0.0% | 4.8% | 🟢 ZYSK |