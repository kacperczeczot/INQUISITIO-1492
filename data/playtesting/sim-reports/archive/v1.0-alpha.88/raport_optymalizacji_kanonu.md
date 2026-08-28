# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.88 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.87` (4P: `88.4 pkt`) → **Nowa Wersja:** `v1.0-alpha.88` (4P: `89.3 pkt`)
**Data:** 2026-08-29 01:53 | **Czas Trwania Iteracji:** 43.2s | **Zysk 4P:** `+0.9 pkt` | **Zysk Global:** `+0.3 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_KB-08_HERESY_SET2` — **KB-08 (Przekupstwo Sędziego): dodaj heresy = 2**
- **Opis Modyfikacji:** Karta `kb-08` (Przekupstwo Sędziego): `heresy` → `2`
- **Wynik Kanonu 4P Balance:** 88.4 → 🟡 ** 89.3** (`⬆️ +0.9`) pkt (±0.86)
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 89.1 → 90.6 (`⬆️ +1.5`) pkt
  - `4p-no-cienie`: 74.0 → 82.3 (`⬆️ +8.3`) pkt
  - `4p-no-kabala`: 97.0 → 96.3 (`🔻 -0.7`) pkt
  - `4p-no-korona`: 85.4 → 90.0 (`⬆️ +4.6`) pkt
  - `4p-no-oficjum`: 94.4 → 96.7 (`⬆️ +2.3`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 33.0 → 33.0 (`= 0.0`) pkt
- **Tryb 4-osobowy (4p Avg):** 88.4 → 89.3 (`⬆️ +0.9`) pkt
- **Tryb 5-osobowy (5p Avg):** 25.6 → 25.5 (`🔻 -0.1`) pkt
- **Global Game Balance Score:** 49.0 → 🔴 ** 49.3** (`⬆️ +0.3`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.70 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.6%` (norma: <30%)
  - **Autodafé / partię:** `1.50`
  - **Oskarżenia / partię:** `7.60`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | CI 95% | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_KB-08_HERESY_SET2` | KB-08 (Przekupstwo Sędziego): dodaj heresy = 2 | 88.4 → 🟢 ** 91.2** (`⬆️ +2.8`) | `[89.5, 92.9]` | 0.0% | 4.6% | 🌟 ZWYCIĘZCA |
| #2 | `L3_CAA-11_COST_PLUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 2 | 88.4 → 🟢 ** 90.8** (`⬆️ +2.4`) | `[89.1, 92.5]` | 0.0% | 4.7% | 🟢 ZYSK |
| #3 | `L3_SO-01_COST_MINUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 0 | 88.4 → 🟢 ** 90.1** (`⬆️ +1.7`) | `[88.4, 91.8]` | 0.0% | 3.9% | 🟢 ZYSK |
| #4 | `L3_KT-01_GOLD_PLUS1` | KT-01 (Rytuał Przejścia): gold 0 → 1 | 88.4 → 🟢 ** 90.1** (`⬆️ +1.7`) | `[88.5, 91.8]` | 0.0% | 4.7% | 🟢 ZYSK |
| #5 | `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 88.4 → 🟢 ** 90.0** (`⬆️ +1.6`) | `[88.3, 91.7]` | 0.0% | 4.7% | 🟢 ZYSK |
| #6 | `L3_SO-02_GOLD_MINUS1` | SO-02 (Skarbiec Trybunału): gold 2 → 1 | 88.4 → 🟡 ** 89.8** (`⬆️ +1.4`) | `[88.1, 91.5]` | 0.0% | 4.7% | 🟢 ZYSK |
| #7 | `L3_GC-09_GOLD_PLUS1` | GC-09 (Lista Dłużników): gold 0 → 1 | 88.4 → 🟡 ** 89.8** (`⬆️ +1.4`) | `[88.1, 91.5]` | 0.0% | 4.7% | 🟢 ZYSK |
| #8 | `L3_CAA-03_COST_PLUS1` | CAA-03 (Cień na Rynku): cost 0 → 1 | 88.4 → 🟡 ** 89.4** (`⬆️ +1.0`) | `[87.7, 91.1]` | 0.0% | 4.7% | 🟢 ZYSK |