# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.85 (Iteracja #2, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.84` (4P: `83.7 pkt`) → **Nowa Wersja:** `v1.0-alpha.85` (4P: `85.1 pkt`)
**Data:** 2026-08-29 01:45 | **Czas Trwania Iteracji:** 41.2s | **Zysk 4P:** `+1.4 pkt` | **Zysk Global:** `+0.6 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_SO-09_HERESY_PLUS1` — **SO-09 (Świadek Koronny): heresy 0 → 1**
- **Opis Modyfikacji:** Karta `so-09` (Świadek Koronny): `heresy` → `1`
- **Wynik Kanonu 4P Balance:** 83.7 → 🟡 ** 85.1** (`⬆️ +1.4`) pkt (±0.87)
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 82.7 → 85.0 (`⬆️ +2.3`) pkt
  - `4p-no-cienie`: 70.6 → 74.1 (`⬆️ +3.5`) pkt
  - `4p-no-kabala`: 98.9 → 97.9 (`🔻 -1.0`) pkt
  - `4p-no-korona`: 80.3 → 83.5 (`⬆️ +3.2`) pkt
  - `4p-no-oficjum`: 95.4 → 92.5 (`🔻 -2.9`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 32.5 → 32.7 (`⬆️ +0.2`) pkt
- **Tryb 4-osobowy (4p Avg):** 83.7 → 85.1 (`⬆️ +1.4`) pkt
- **Tryb 5-osobowy (5p Avg):** 24.7 → 24.9 (`⬆️ +0.2`) pkt
- **Global Game Balance Score:** 47.0 → 🔴 ** 47.6** (`⬆️ +0.6`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.70 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.7%` (norma: <30%)
  - **Autodafé / partię:** `1.52`
  - **Oskarżenia / partię:** `7.65`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | CI 95% | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-09_HERESY_PLUS1` | SO-09 (Świadek Koronny): heresy 0 → 1 | 83.7 → 🟡 ** 86.6** (`⬆️ +2.9`) | `[84.9, 88.3]` | 0.0% | 4.7% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KT-07_COST_PLUS1` | KT-07 (Archiwum Ukryte): cost 1 → 2 | 83.7 → 🟡 ** 85.8** (`⬆️ +2.1`) | `[84.1, 87.5]` | 0.0% | 4.8% | 🟢 ZYSK |
| #3 | `L3_SO-06_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): heresy 0 → 1 | 83.7 → 🟡 ** 85.8** (`⬆️ +2.1`) | `[84.1, 87.5]` | 0.0% | 4.9% | 🟢 ZYSK |
| #4 | `L3_SO-05_TARGET_HERESY_MINUS1` | SO-05 (Wezwanie do Trybunału): target_heresy 1 → 0 | 83.7 → 🟡 ** 85.6** (`⬆️ +1.9`) | `[83.9, 87.3]` | 0.0% | 4.8% | 🟢 ZYSK |
| #5 | `L3_GC-08_GOLD_MINUS1` | GC-08 (Zatrute Złoto): gold 1 → 0 | 83.7 → 🟡 ** 85.6** (`⬆️ +1.9`) | `[84.0, 87.2]` | 0.0% | 4.8% | 🟢 ZYSK |
| #6 | `L3_GC-01_HERESY_MINUS1` | GC-01 (Przekupiony Strażnik): heresy 1 → 0 | 83.7 → 🟡 ** 85.4** (`⬆️ +1.7`) | `[83.6, 87.2]` | 0.0% | 4.8% | 🟢 ZYSK |
| #7 | `L3_CAA-11_TARGET_HERESY_MINUS1` | CAA-11 (Nocna Zmiana Warty): target_heresy 1 → 0 | 83.7 → 🟡 ** 85.4** (`⬆️ +1.7`) | `[83.7, 87.1]` | 0.0% | 4.7% | 🟢 ZYSK |
| #8 | `L3_SO-07_COST_MINUS1` | SO-07 (Przesłuchanie Oficjum): cost 1 → 0 | 83.7 → 🟡 ** 85.3** (`⬆️ +1.6`) | `[83.6, 87.0]` | 0.0% | 4.4% | 🟢 ZYSK |