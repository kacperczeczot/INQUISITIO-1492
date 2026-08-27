# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.61 (Iteracja #2, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.60` (4P: `59.4 pkt`) → **Nowa Wersja:** `v1.0-alpha.61` (4P: `66.8 pkt`)
**Data:** 2026-08-23 22:58 | **Czas Trwania Iteracji:** 925.4s | **Zysk 4P:** `+7.4 pkt` | **Zysk Global:** `+10.2 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_SO-03_HERESY_PLUS1` — **SO-03 (Podejrzenie): heresy 2 → 3**
- **Opis Modyfikacji:** Karta `so-03` (Podejrzenie): `heresy` → `3`
- **Wynik Kanonu 4P Balance:** 59.4 → 🟠 ** 66.8** (`⬆️ +7.4`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 65.2 → 68.6 (`⬆️ +3.4`) pkt
  - `4p-no-cienie`: 43.7 → 46.6 (`⬆️ +2.9`) pkt
  - `4p-no-kabala`: 66.9 → 76.8 (`⬆️ +9.9`) pkt
  - `4p-no-korona`: 60.9 → 82.0 (`⬆️ +21.1`) pkt
  - `4p-no-oficjum`: 60.2 pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 21.4 → 28.1 (`⬆️ +6.7`) pkt
- **Tryb 4-osobowy (4p Avg):** 54.4 → 65.4 (`⬆️ +11.0`) pkt
- **Tryb 5-osobowy (5p Avg):** 7.3 → 20.1 (`⬆️ +12.8`) pkt
- **Global Game Balance Score:** 27.7 → 🔴 ** 37.9** (`⬆️ +10.2`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.83 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `5.9%` (norma: <30%)
  - **Autodafé / partię:** `1.29`
  - **Oskarżenia / partię:** `6.83`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-03_HERESY_PLUS1` | SO-03 (Podejrzenie): heresy 2 → 3 | 59.4 → 🟠 ** 66.8** (`⬆️ +7.4`) | 0.0% | 5.9% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-07_GOLD_SET3` | SO-07 (Przesłuchanie Oficjum): dodaj gold = 3 | 59.4 → 🟠 ** 65.2** (`⬆️ +5.8`) | 0.0% | 5.5% | 🟢 ZYSK |
| #3 | `L3_SO-07_TARGET_HERESY_SET2` | SO-07 (Przesłuchanie Oficjum): dodaj target_heresy = 2 | 59.4 → 🟠 ** 63.8** (`⬆️ +4.4`) | 0.0% | 5.7% | 🟢 ZYSK |
| #4 | `L3_CAA-11_GOLD_MINUS1` | CAA-11 (Nocna Zmiana Warty): gold 3 → 2 | 59.4 → 🟠 ** 63.3** (`⬆️ +3.9`) | 0.0% | 5.6% | 🟢 ZYSK |
| #5 | `L3_GC-06_HERESY_MINUS1` | GC-06 (Szantaż): heresy 1 → 0 | 59.4 → 🟠 ** 60.8** (`⬆️ +1.4`) | 0.0% | 5.6% | 🟢 ZYSK |
| #6 | `L3_KT-09_HERESY_MINUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 0 | 59.4 → 🟠 ** 62.4** (`⬆️ +3.0`) | 0.0% | 5.7% | 🟢 ZYSK |
| #7 | `L3_CAA-11_COST_PLUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 2 | 59.4 → 🟠 ** 63.6** (`⬆️ +4.2`) | 0.0% | 5.6% | 🟢 ZYSK |
| #8 | `L3_KT-03_HERESY_MINUS1` | KT-03 (Zakazana Wiedza): heresy 2 → 1 | 59.4 → 🟠 ** 63.3** (`⬆️ +3.9`) | 0.0% | 5.7% | 🟢 ZYSK |
| #9 | `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 59.4 → 🟠 ** 64.4** (`⬆️ +5.0`) | 0.0% | 5.6% | 🟢 ZYSK |
| #10 | `L3_CAA-04_TARGET_HERESY_MINUS1` | CAA-04 (Fałszywy Trop): target_heresy 1 → 0 | 59.4 → 🟠 ** 63.8** (`⬆️ +4.4`) | 0.0% | 5.6% | 🟢 ZYSK |
| #11 | `L3_GC-08_TARGET_HERESY_MINUS1` | GC-08 (Zatrute Złoto): target_heresy 1 → 0 | 59.4 → 🟠 ** 61.2** (`⬆️ +1.8`) | 0.0% | 5.6% | 🟢 ZYSK |
| #12 | `L4_SEA_ROUTE_ERA_MINUS1` | Szlak Morski: Era 4 → 3 | 59.4 → 🟠 ** 65.1** (`⬆️ +5.7`) | 0.0% | 5.5% | 🟢 ZYSK |
| #13 | `L3_GC-03_HERESY_SET2` | GC-03 (Podrzucenie Księgi): dodaj heresy = 2 | 59.4 → 🟠 ** 61.2** (`⬆️ +1.8`) | 0.0% | 5.6% | 🟢 ZYSK |
| #14 | `L3_CAA-10_COST_MINUS1` | CAA-10 (Echo Alhambry): cost 3 → 2 | 59.4 → 🟠 ** 69.7** (`⬆️ +10.3`) | 0.0% | 5.5% | 🟢 ZYSK |
| #15 | `L3_CAA-10_GOLD_SET2` | CAA-10 (Echo Alhambry): dodaj gold = 2 | 59.4 → 🟠 ** 69.9** (`⬆️ +10.5`) | 0.0% | 5.5% | 🟢 ZYSK |
| #16 | `L3_CAA-10_TARGET_HERESY_PLUS1` | CAA-10 (Echo Alhambry): target_heresy 0 → 1 | 59.4 → 🟠 ** 74.0** (`⬆️ +14.6`) | 0.0% | 5.5% | 🟢 ZYSK |
| #17 | `L3_CAA-10_TARGET_HERESY_SET1` | CAA-10 (Echo Alhambry): dodaj target_heresy = 1 | 59.4 → 🟠 ** 74.0** (`⬆️ +14.6`) | 0.0% | 5.5% | 🟢 ZYSK |
| #18 | `L3_CAA-10_TARGET_HERESY_SET2` | CAA-10 (Echo Alhambry): dodaj target_heresy = 2 | 59.4 → 🟠 ** 74.6** (`⬆️ +15.2`) | 0.0% | 5.6% | 🟢 ZYSK |
| #19 | `L3_CAA-10_GOLD_SET3` | CAA-10 (Echo Alhambry): dodaj gold = 3 | 59.4 → 🟠 ** 72.1** (`⬆️ +12.7`) | 0.0% | 5.5% | 🟢 ZYSK |
| #20 | `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 4 → 5 Ery | 59.4 → 🟠 ** 66.4** (`⬆️ +7.0`) | 0.0% | 5.5% | 🟢 ZYSK |