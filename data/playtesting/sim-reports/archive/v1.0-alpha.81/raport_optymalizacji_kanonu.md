# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.81 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.80` (4P: `75.7 pkt`) → **Nowa Wersja:** `v1.0-alpha.81` (4P: `78.1 pkt`)
**Data:** 2026-08-29 01:37 | **Czas Trwania Iteracji:** 43.4s | **Zysk 4P:** `+2.4 pkt` | **Zysk Global:** `+0.9 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_KB-10_GOLD_SET2` — **KB-10 (Pieczęć Korony): dodaj gold = 2**
- **Opis Modyfikacji:** Karta `kb-10` (Pieczęć Korony): `gold` → `2`
- **Wynik Kanonu 4P Balance:** 75.7 → 🟠 ** 78.1** (`⬆️ +2.4`) pkt (±0.89)
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 74.6 → 77.4 (`⬆️ +2.8`) pkt
  - `4p-no-cienie`: 59.9 → 67.1 (`⬆️ +7.2`) pkt
  - `4p-no-kabala`: 89.9 → 92.6 (`⬆️ +2.7`) pkt
  - `4p-no-korona`: 63.8 → 64.5 (`⬆️ +0.7`) pkt
  - `4p-no-oficjum`: 85.3 → 92.1 (`⬆️ +6.8`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 31.5 → 31.7 (`⬆️ +0.2`) pkt
- **Tryb 4-osobowy (4p Avg):** 75.7 → 78.1 (`⬆️ +2.4`) pkt
- **Tryb 5-osobowy (5p Avg):** 23.3 → 23.5 (`⬆️ +0.2`) pkt
- **Global Game Balance Score:** 43.5 → 🔴 ** 44.4** (`⬆️ +0.9`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.77 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.6%` (norma: <30%)
  - **Autodafé / partię:** `1.49`
  - **Oskarżenia / partię:** `7.61`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | CI 95% | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_KB-10_GOLD_SET2` | KB-10 (Pieczęć Korony): dodaj gold = 2 | 75.7 → 🟠 ** 78.7** (`⬆️ +3.0`) | `[77.0, 80.4]` | 0.0% | 4.6% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KB-01_COST_PLUS1` | KB-01 (Rozkaz Dworu): cost 1 → 2 | 75.7 → 🟠 ** 78.6** (`⬆️ +2.9`) | `[76.9, 80.3]` | 0.0% | 5.6% | 🟢 ZYSK |
| #3 | `L3_SO-06_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): heresy 0 → 1 | 75.7 → 🟠 ** 78.0** (`⬆️ +2.3`) | `[76.2, 79.8]` | 0.0% | 4.7% | 🟢 ZYSK |
| #4 | `L3_GC-09_GOLD_PLUS1` | GC-09 (Lista Dłużników): gold 0 → 1 | 75.7 → 🟠 ** 78.0** (`⬆️ +2.3`) | `[76.2, 79.8]` | 0.0% | 4.6% | 🟢 ZYSK |
| #5 | `L3_KB-06_GOLD_PLUS1` | KB-06 (Areszt Królewski): gold 0 → 1 | 75.7 → 🟠 ** 77.9** (`⬆️ +2.2`) | `[76.1, 79.7]` | 0.0% | 4.5% | 🟢 ZYSK |
| #6 | `L3_KB-04_COST_MINUS1` | KB-04 (Faworyt Dworu): cost 2 → 1 | 75.7 → 🟠 ** 77.7** (`⬆️ +2.0`) | `[76.0, 79.4]` | 0.0% | 4.1% | 🟢 ZYSK |
| #7 | `L3_SO-09_COST_PLUS1` | SO-09 (Świadek Koronny): cost 1 → 2 | 75.7 → 🟠 ** 77.3** (`⬆️ +1.6`) | `[75.5, 79.1]` | 0.0% | 4.8% | 🟢 ZYSK |
| #8 | `L3_SO-12_COST_PLUS1` | SO-12 (Straż Trybunalska): cost 1 → 2 | 75.7 → 🟠 ** 77.2** (`⬆️ +1.5`) | `[75.5, 79.0]` | 0.0% | 5.0% | 🟢 ZYSK |