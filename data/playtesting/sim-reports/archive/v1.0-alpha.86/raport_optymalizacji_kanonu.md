# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.86 (Iteracja #3, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.85` (4P: `85.1 pkt`) → **Nowa Wersja:** `v1.0-alpha.86` (4P: `87.5 pkt`)
**Data:** 2026-08-29 01:47 | **Czas Trwania Iteracji:** 41.8s | **Zysk 4P:** `+2.4 pkt` | **Zysk Global:** `+1.0 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_SO-03_GOLD_MINUS1` — **SO-03 (Podejrzenie): gold 1 → 0**
- **Opis Modyfikacji:** Karta `so-03` (Podejrzenie): `gold` → `0`
- **Wynik Kanonu 4P Balance:** 85.1 → 🟡 ** 87.5** (`⬆️ +2.4`) pkt (±0.88)
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 81.7 → 87.3 (`⬆️ +5.6`) pkt
  - `4p-no-cienie`: 73.2 → 79.6 (`⬆️ +6.4`) pkt
  - `4p-no-kabala`: 98.4 → 92.7 (`🔻 -5.7`) pkt
  - `4p-no-korona`: 80.7 → 84.9 (`⬆️ +4.2`) pkt
  - `4p-no-oficjum`: 95.2 → 97.1 (`⬆️ +1.9`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 32.7 → 32.9 (`⬆️ +0.2`) pkt
- **Tryb 4-osobowy (4p Avg):** 85.1 → 87.5 (`⬆️ +2.4`) pkt
- **Tryb 5-osobowy (5p Avg):** 24.9 → 25.4 (`⬆️ +0.5`) pkt
- **Global Game Balance Score:** 47.6 → 🔴 ** 48.6** (`⬆️ +1.0`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.73 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.8%` (norma: <30%)
  - **Autodafé / partię:** `1.52`
  - **Oskarżenia / partię:** `7.64`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | CI 95% | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-03_GOLD_MINUS1` | SO-03 (Podejrzenie): gold 1 → 0 | 85.1 → 🟡 ** 88.3** (`⬆️ +3.2`) | `[86.6, 90.0]` | 0.0% | 4.8% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-03_TARGET_HERESY_MINUS1` | SO-03 (Podejrzenie): target_heresy 3 → 2 | 85.1 → 🟡 ** 87.9** (`⬆️ +2.8`) | `[86.1, 89.7]` | 0.0% | 4.5% | 🟢 ZYSK |
| #3 | `L3_SO-08_HERESY_PLUS1` | SO-08 (Nasłanie Inkwizytora): heresy 0 → 1 | 85.1 → 🟡 ** 87.5** (`⬆️ +2.4`) | `[85.9, 89.1]` | 0.0% | 4.7% | 🟢 ZYSK |
| #4 | `L3_GC-09_GOLD_SET2` | GC-09 (Lista Dłużników): dodaj gold = 2 | 85.1 → 🟡 ** 87.0** (`⬆️ +1.9`) | `[85.3, 88.7]` | 0.0% | 4.7% | 🟢 ZYSK |
| #5 | `L3_GC-11_HERESY_PLUS1` | GC-11 (Fałszywe Świadectwo Cechu): heresy 2 → 3 | 85.1 → 🟡 ** 86.8** (`⬆️ +1.7`) | `[85.1, 88.5]` | 0.0% | 4.7% | 🟢 ZYSK |
| #6 | `L3_SO-11_COST_PLUS1` | SO-11 (Dekret Czystości Wiary): cost 1 → 2 | 85.1 → 🟡 ** 86.5** (`⬆️ +1.4`) | `[84.8, 88.2]` | 0.0% | 4.7% | 🟢 ZYSK |
| #7 | `L3_KB-08_HERESY_SET2` | KB-08 (Przekupstwo Sędziego): dodaj heresy = 2 | 85.1 → 🟡 ** 86.4** (`⬆️ +1.3`) | `[84.7, 88.1]` | 0.0% | 4.6% | 🟢 ZYSK |
| #8 | `L1_START_GOLD_PLUS1` | Złoto startowe: 4zł → 5zł | 85.1 → 🟡 ** 86.2** (`⬆️ +1.1`) | `[84.5, 87.9]` | 0.0% | 4.7% | 🟢 ZYSK |