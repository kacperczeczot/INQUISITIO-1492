# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.87 (Iteracja #4, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.86` (4P: `87.5 pkt`) → **Nowa Wersja:** `v1.0-alpha.87` (4P: `88.4 pkt`)
**Data:** 2026-08-29 01:47 | **Czas Trwania Iteracji:** 42.2s | **Zysk 4P:** `+0.9 pkt` | **Zysk Global:** `+0.4 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_SO-03_HERESY_PLUS1` — **SO-03 (Podejrzenie): heresy 3 → 4**
- **Opis Modyfikacji:** Karta `so-03` (Podejrzenie): `heresy` → `4`
- **Wynik Kanonu 4P Balance:** 87.5 → 🟡 ** 88.4** (`⬆️ +0.9`) pkt (±0.88)
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 86.6 → 90.2 (`⬆️ +3.6`) pkt
  - `4p-no-cienie`: 75.5 → 76.3 (`⬆️ +0.8`) pkt
  - `4p-no-kabala`: 96.0 → 94.8 (`🔻 -1.2`) pkt
  - `4p-no-korona`: 80.9 → 87.4 (`⬆️ +6.5`) pkt
  - `4p-no-oficjum`: 94.3 → 95.3 (`⬆️ +1.0`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 32.9 → 33.0 (`⬆️ +0.1`) pkt
- **Tryb 4-osobowy (4p Avg):** 87.5 → 88.4 (`⬆️ +0.9`) pkt
- **Tryb 5-osobowy (5p Avg):** 25.4 → 25.6 (`⬆️ +0.2`) pkt
- **Global Game Balance Score:** 48.6 → 🔴 ** 49.0** (`⬆️ +0.4`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.72 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.7%` (norma: <30%)
  - **Autodafé / partię:** `1.51`
  - **Oskarżenia / partię:** `7.62`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | CI 95% | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-03_HERESY_PLUS1` | SO-03 (Podejrzenie): heresy 3 → 4 | 87.5 → 🟡 ** 88.8** (`⬆️ +1.3`) | `[87.1, 90.5]` | 0.0% | 4.7% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-01_COST_MINUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 0 | 87.5 → 🟡 ** 88.7** (`⬆️ +1.2`) | `[86.9, 90.5]` | 0.0% | 4.0% | 🟢 ZYSK |
| #3 | `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 4 → 3 Ery | 87.5 → 🟡 ** 88.6** (`⬆️ +1.1`) | `[86.9, 90.3]` | 0.0% | 4.8% | 🟢 ZYSK |
| #4 | `L3_CAA-07_HERESY_SET2` | CAA-07 (Szantaż Bractwa): dodaj heresy = 2 | 87.5 → 🟡 ** 88.3** (`⬆️ +0.8`) | `[86.6, 90.0]` | 0.0% | 4.7% | 🟢 ZYSK |
| #5 | `L3_CAA-02_TARGET_HERESY_PLUS1` | CAA-02 (Złoto z Kryjówki): target_heresy 0 → 1 | 87.5 → 🟡 ** 88.2** (`⬆️ +0.7`) | `[86.5, 89.9]` | 0.0% | 4.7% | 🟢 ZYSK |
| #6 | `L3_GC-04_GOLD_SET2` | GC-04 (Informator): dodaj gold = 2 | 87.5 → 🟡 ** 88.2** (`⬆️ +0.7`) | `[86.5, 89.9]` | 0.0% | 4.7% | 🟢 ZYSK |
| #7 | `L3_SO-02_TARGET_HERESY_MINUS1` | SO-02 (Skarbiec Trybunału): target_heresy 1 → 0 | 87.5 → 🟡 ** 88.0** (`⬆️ +0.5`) | `[86.2, 89.8]` | 0.0% | 4.7% | 🟢 ZYSK |
| #8 | `L3_GC-11_HERESY_PLUS1` | GC-11 (Fałszywe Świadectwo Cechu): heresy 2 → 3 | 87.5 → 🟡 ** 87.8** (`⬆️ +0.3`) | `[86.1, 89.5]` | 0.0% | 4.7% | 🟢 ZYSK |