# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.81 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.80` (4P: `20.7 pkt`) → **Nowa Wersja:** `v1.0-alpha.81` (4P: `52.3 pkt`)
**Data:** 2026-08-28 15:20 | **Czas Trwania Iteracji:** 18.0s | **Zysk 4P:** `+31.6 pkt` | **Zysk Global:** `+21.0 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L2_KB_DECREES_MINUS1` — **Korona Dekrety: 2 → 1**
- **Opis Modyfikacji:** Korona Borgiowie: Dekrety offset -1
- **Wynik Kanonu 4P Balance:** 20.7 → 🔴 ** 52.3** (`⬆️ +31.6`) pkt (±3.34)
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 11.1 → 34.7 (`⬆️ +23.6`) pkt
  - `4p-no-cienie`: 17.3 → 52.4 (`⬆️ +35.1`) pkt
  - `4p-no-kabala`: 21.5 → 81.0 (`⬆️ +59.5`) pkt
  - `4p-no-korona`: 41.4 → 42.4 (`⬆️ +1.0`) pkt
  - `4p-no-oficjum`: 12.4 → 50.9 (`⬆️ +38.5`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 8.1 → 24.8 (`⬆️ +16.7`) pkt
- **Tryb 4-osobowy (4p Avg):** 20.6 → 54.5 (`⬆️ +33.9`) pkt
- **Tryb 5-osobowy (5p Avg):** 2.0 → 14.4 (`⬆️ +12.4`) pkt
- **Global Game Balance Score:** 10.2 → 🔴 ** 31.2** (`⬆️ +21.0`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.92 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.6%` (norma: <30%)
  - **Autodafé / partię:** `1.55`
  - **Oskarżenia / partię:** `8.08`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | CI 95% | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| #1 | `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 20.7 → 🔴 ** 52.3** (`⬆️ +31.6`) | `[45.8, 58.9]` | 0.0% | 4.6% | 🌟 ZWYCIĘZCA |