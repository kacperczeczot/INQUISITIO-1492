# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.92 (Iteracja #1, Faza 7D)

**Wersja Poprzednia:** `v1.0-alpha.91` (4P: `92.1 pkt`) → **Nowa Wersja:** `v1.0-alpha.92` (4P: `93.8 pkt`)
**Data:** 2026-08-29 10:30 | **Czas Trwania Iteracji:** 1.0s | **Zysk 4P:** `+1.7 pkt` | **Zysk Global:** `+0.9 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (7D):** `L3_CAA-06_TARGET_HERESY_MINUS1__L3_KT-01_G1_H1__L3_CAA-01_C2_H2__L3_CAA-11_GOLD_MINUS2__L1_MAX_ERAS_PLUS1__L3_SO-02_TARGET_HERESY_PLUS1__L1_AUTODAFE_COOLDOWN_MINUS1` — **Limit Er: offset +1 (nowy: 15) + Cooldown Autodafé: offset -1 (nowy: 3) + Karta `caa-06` (Ucieczka z Lochów): `target_heresy` → `1` + Karta `kt-01` (Rytuał Przejścia): `gold` → `1`, `heresy` → `1` + Karta `caa-01` (Przejście Podziemiami): `cost` → `2`, `heresy` → `2` + Karta `caa-11` (Nocna Zmiana Warty): `gold` → `1` + Karta `so-02` (Skarbiec Trybunału): `target_heresy` → `2`**
- **Opis Modyfikacji:** Limit Er: offset +1 (nowy: 15) + Cooldown Autodafé: offset -1 (nowy: 3) + Karta `caa-06` (Ucieczka z Lochów): `target_heresy` → `1` + Karta `kt-01` (Rytuał Przejścia): `gold` → `1`, `heresy` → `1` + Karta `caa-01` (Przejście Podziemiami): `cost` → `2`, `heresy` → `2` + Karta `caa-11` (Nocna Zmiana Warty): `gold` → `1` + Karta `so-02` (Skarbiec Trybunału): `target_heresy` → `2`
- **Wynik Kanonu 4P Balance:** 92.1 → 🟢 ** 93.8** (`⬆️ +1.7`) pkt (±0.35)
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 85.0 → 92.1 (`⬆️ +7.1`) pkt
  - `4p-no-cienie`: 84.8 → 86.7 (`⬆️ +1.9`) pkt
  - `4p-no-kabala`: 96.5 → 95.4 (`🔻 -1.1`) pkt
  - `4p-no-korona`: 94.4 → 96.1 (`⬆️ +1.7`) pkt
  - `4p-no-oficjum`: 99.8 → 98.5 (`🔻 -1.3`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 32.7 → 33.1 (`⬆️ +0.4`) pkt
- **Tryb 4-osobowy (4p Avg):** 92.1 → 93.8 (`⬆️ +1.7`) pkt
- **Tryb 5-osobowy (5p Avg):** 25.1 → 25.7 (`⬆️ +0.6`) pkt
- **Global Game Balance Score:** 50.0 → 🔴 ** 50.9** (`⬆️ +0.9`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.76 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.8%` (norma: <30%)
  - **Autodafé / partię:** `1.52`
  - **Oskarżenia / partię:** `7.60`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | CI 95% | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-06_TARGET_HERESY_MINUS1__L3_KT-01_G1_H1__L3_CAA-01_C2_H2__L3_CAA-11_GOLD_MINUS2__L1_MAX_ERAS_PLUS1__L3_SO-02_TARGET_HERESY_PLUS1__L1_AUTODAFE_COOLDOWN_MINUS1` | Limit Er: offset +1 (nowy: 15) + Cooldown Autodafé: offset -1 (nowy: 3) + Karta `caa-06` (Ucieczka z Lochów): `target_heresy` → `1` + Karta `kt-01` (Rytuał Przejścia): `gold` → `1`, `heresy` → `1` + Karta `caa-01` (Przejście Podziemiami): `cost` → `2`, `heresy` → `2` + Karta `caa-11` (Nocna Zmiana Warty): `gold` → `1` + Karta `so-02` (Skarbiec Trybunału): `target_heresy` → `2` | 92.1 → 🟢 ** 93.8** (`⬆️ +1.7`) | `-` | 0.0% | 4.8% | 🌟 ZWYCIĘZCA |