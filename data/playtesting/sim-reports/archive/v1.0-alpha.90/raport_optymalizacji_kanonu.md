# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.90 (Iteracja #2, Faza 2D)

**Wersja Poprzednia:** `v1.0-alpha.89` (4P: `90.1 pkt`) → **Nowa Wersja:** `v1.0-alpha.90` (4P: `92.0 pkt`)
**Data:** 2026-08-29 01:57 | **Czas Trwania Iteracji:** 125.6s | **Zysk 4P:** `+1.9 pkt` | **Zysk Global:** `+0.4 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (2D):** `L3_KT-12_HERESY_MINUS1__L3_KT-12_COST_PLUS1` — **KT-12 (Strażnik Archiwum): heresy 1 → 0 + KT-12 (Strażnik Archiwum): cost 0 → 1**
- **Opis Modyfikacji:** Karta `kt-12` (Strażnik Archiwum): `heresy` → `0` + Karta `kt-12` (Strażnik Archiwum): `cost` → `1`
- **Wynik Kanonu 4P Balance:** 90.1 → 🟢 ** 92.0** (`⬆️ +1.9`) pkt (±0.85)
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 90.0 → 90.4 (`⬆️ +0.4`) pkt
  - `4p-no-cienie`: 81.9 → 83.2 (`⬆️ +1.3`) pkt
  - `4p-no-kabala`: 96.0 → 95.4 (`🔻 -0.6`) pkt
  - `4p-no-korona`: 88.3 → 94.1 (`⬆️ +5.8`) pkt
  - `4p-no-oficjum`: 97.7 → 98.6 (`⬆️ +0.9`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 33.0 → 32.7 (`🔻 -0.3`) pkt
- **Tryb 4-osobowy (4p Avg):** 90.1 → 92.0 (`⬆️ +1.9`) pkt
- **Tryb 5-osobowy (5p Avg):** 25.5 → 25.1 (`🔻 -0.4`) pkt
- **Global Game Balance Score:** 49.5 → 🔴 ** 49.9** (`⬆️ +0.4`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.77 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.9%` (norma: <30%)
  - **Autodafé / partię:** `1.52`
  - **Oskarżenia / partię:** `7.60`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | CI 95% | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_KT-12_HERESY_MINUS1__L3_KT-12_COST_PLUS1` | KT-12 (Strażnik Archiwum): heresy 1 → 0 + KT-12 (Strażnik Archiwum): cost 0 → 1 | 90.1 → 🟢 ** 92.3** (`⬆️ +2.2`) | `[90.6, 94.0]` | 0.0% | 4.9% | 🌟 ZWYCIĘZCA |
| #2 | `L3_GC-03_TARGET_HERESY_MINUS1__L3_KT-10_GOLD_SET2` | GC-03 (Podrzucenie Księgi): target_heresy 1 → 0 + KT-10 (Pieczęć Salomona): dodaj gold = 2 | 90.1 → 🟢 ** 91.8** (`⬆️ +1.7`) | `[90.2, 93.4]` | 0.0% | 4.6% | 🟢 ZYSK |
| #3 | `L3_SO-01_TARGET_HERESY_SET1__L3_SO-06_HERESY_PLUS1` | SO-01 (Patrol Familiariuszy): dodaj target_heresy = 1 + SO-06 (Areszt Trybunalski): heresy 0 → 1 | 90.1 → 🟢 ** 91.4** (`⬆️ +1.3`) | `[89.7, 93.1]` | 0.0% | 4.7% | 🟢 ZYSK |
| #4 | `L3_SO-10_GOLD_SET1__L3_SO-06_HERESY_SET1` | SO-10 (Oczyść Miasto): dodaj gold = 1 + SO-06 (Areszt Trybunalski): dodaj heresy = 1 | 90.1 → 🟢 ** 91.2** (`⬆️ +1.1`) | `[89.5, 92.9]` | 0.0% | 4.4% | 🟢 ZYSK |
| #5 | `L3_SO-01_GOLD_PLUS1__L3_SO-06_COST_PLUS1` | SO-01 (Patrol Familiariuszy): gold 2 → 3 + SO-06 (Areszt Trybunalski): cost 2 → 3 | 90.1 → 🟢 ** 90.7** (`⬆️ +0.6`) | `[89.0, 92.4]` | 0.0% | 4.6% | 🟢 ZYSK |
| #6 | `L3_GC-05_TARGET_HERESY_SET2__L3_GC-07_COST_PLUS1` | GC-05 (Fałszywy Świadek): dodaj target_heresy = 2 + GC-07 (Skrytobójstwo): cost 0 → 1 | 90.1 → 🟢 ** 90.5** (`⬆️ +0.4`) | `[88.8, 92.2]` | 0.0% | 4.6% | 🟢 ZYSK |
| #7 | `L3_KT-10_GOLD_SET1__L1_AUTODAFE_COOLDOWN_MINUS1` | KT-10 (Pieczęć Salomona): dodaj gold = 1 + Cooldown Autodafé: 4 → 3 Ery | 90.1 → 🟢 ** 90.5** (`⬆️ +0.4`) | `[88.8, 92.2]` | 0.0% | 4.6% | 🟢 ZYSK |
| #8 | `L3_SO-11_COST_MINUS1__L3_SO-03_HERESY_PLUS1` | SO-11 (Dekret Czystości Wiary): cost 1 → 0 + SO-03 (Podejrzenie): heresy 4 → 5 | 90.1 → 🟢 ** 90.4** (`⬆️ +0.3`) | `[88.7, 92.1]` | 0.0% | 4.1% | 🟢 ZYSK |
| #9 | `L3_SO-05_TARGET_HERESY_PLUS1__L3_SO-07_HERESY_PLUS1` | SO-05 (Wezwanie do Trybunału): target_heresy 1 → 2 + SO-07 (Przesłuchanie Oficjum): heresy 0 → 1 | 90.1 → 🟢 ** 90.3** (`⬆️ +0.2`) | `[88.6, 92.0]` | 0.0% | 4.7% | 🟢 ZYSK |
| #10 | `L3_KT-07_GOLD_PLUS1__L3_KT-08_COST_PLUS1` | KT-07 (Archiwum Ukryte): gold 0 → 1 + KT-08 (Areszt Wiedzy): cost 1 → 2 | 90.1 → 🟢 ** 90.2** (`⬆️ +0.1`) | `[88.5, 91.9]` | 0.0% | 4.7% | 🟢 ZYSK |
| #11 | `L3_GC-05_TARGET_HERESY_SET1__L1_AUTODAFE_COOLDOWN_PLUS1` | GC-05 (Fałszywy Świadek): dodaj target_heresy = 1 + Cooldown Autodafé: 4 → 5 Ery | 90.1 → 🟢 ** 90.2** (`⬆️ +0.1`) | `[88.5, 91.9]` | 0.0% | 4.6% | 🟢 ZYSK |
| #12 | `L3_KT-09_COST_MINUS1__L3_KT-11_GOLD_MINUS1` | KT-09 (Fragment Kodeksu): cost 1 → 0 + KT-11 (Medytacja Sefirot): gold 1 → 0 | 90.1 → 🟢 ** 90.2** (`⬆️ +0.1`) | `[88.5, 91.9]` | 0.0% | 4.6% | 🟢 ZYSK |
| #13 | `L3_KT-04_HERESY_PLUS1__L3_GC-05_TARGET_HERESY_SET2` | KT-04 (Zwierciadło Herezji): heresy 0 → 1 + GC-05 (Fałszywy Świadek): dodaj target_heresy = 2 | 90.1 → 🟢 ** 90.1** (`= 0.0`) | `[88.4, 91.8]` | 0.0% | 4.7% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_GC-03_TARGET_HERESY_MINUS1__L3_KT-12_GOLD_SET1` | GC-03 (Podrzucenie Księgi): target_heresy 1 → 0 + KT-12 (Strażnik Archiwum): dodaj gold = 1 | 90.1 → 🟢 ** 90.1** (`= 0.0`) | `[88.4, 91.8]` | 0.0% | 4.6% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_CAA-08_GOLD_PLUS1__L3_CAA-11_GOLD_MINUS1` | CAA-08 (Kaptur Nocy): gold 3 → 4 + CAA-11 (Nocna Zmiana Warty): gold 3 → 2 | 90.1 → 🟢 ** 90.1** (`= 0.0`) | `[88.4, 91.8]` | 0.0% | 4.7% | ⚪ STRATA/NEUTRALNY |