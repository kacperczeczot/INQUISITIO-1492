# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.54 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.53` (4P: `75.5 pkt`) → **Nowa Wersja:** `v1.0-alpha.54` (4P: `75.6 pkt`)
**Data:** 2026-08-23 17:26 | **Czas Trwania Iteracji:** 653.5s | **Zysk 4P:** `+0.1 pkt` | **Zysk Global:** `-0.1 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_SO-03_GOLD_SET1` — **SO-03 (Podejrzenie): dodaj gold = 1**
- **Opis Modyfikacji:** Karta `so-03` (Podejrzenie): `gold` → `1`
- **Wynik Kanonu 4P Balance:** 75.5 → 🟡 ** 75.6** (`⬆️ +0.1`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 76.4 → 74.9 (`-1.5`) pkt
  - `4p-no-cienie`: 68.9 → 70.2 (`⬆️ +1.3`) pkt
  - `4p-no-kabala`: 77.2 → 78.2 (`⬆️ +1.0`) pkt
  - `4p-no-korona`: 79.6 → 79.5 (`-0.1`) pkt
  - `4p-no-oficjum`: 75.4 pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 13.6 → 13.5 (`-0.1`) pkt
- **Tryb 4-osobowy (4p Avg):** 39.1 → 39.2 (`⬆️ +0.1`) pkt
- **Tryb 5-osobowy (5p Avg):** 3.2 → 2.7 (`-0.5`) pkt
- **Global Game Balance Score:** 18.6 → 🔴 ** 18.5** (`-0.1`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.62 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `5.0%` (norma: <30%)
  - **Autodafé / partię:** `1.46`
  - **Oskarżenia / partię:** `6.03`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 75.5 → 🟠 ** 71.1** (`-4.4`) | 0.0% | 5.1% | ⚪ STRATA/NEUTRALNY |
| #2 | `L3_SO-03_GOLD_SET1` | SO-03 (Podejrzenie): dodaj gold = 1 | 75.5 → 🟡 ** 75.6** (`⬆️ +0.1`) | 0.0% | 5.0% | 🌟 ZWYCIĘZCA |
| #3 | `L3_SO-03_GOLD_PLUS1` | SO-03 (Podejrzenie): gold 0 → 1 | 75.5 → 🟡 ** 75.6** (`⬆️ +0.1`) | 0.0% | 5.0% | 🟢 ZYSK |
| #4 | `L3_CAA-12_TARGET_HERESY_PLUS1` | CAA-12 (Skrytka w Murach): target_heresy 0 → 1 | 75.5 → 🟡 ** 76.9** (`⬆️ +1.4`) | 0.0% | 5.3% | 🟢 ZYSK |
| #5 | `L3_CAA-12_TARGET_HERESY_SET1` | CAA-12 (Skrytka w Murach): dodaj target_heresy = 1 | 75.5 → 🟡 ** 76.9** (`⬆️ +1.4`) | 0.0% | 5.3% | 🟢 ZYSK |
| #6 | `L3_GC-08_HERESY_MINUS1` | GC-08 (Zatrute Złoto): heresy 1 → 0 | 75.5 → 🟡 ** 77.7** (`⬆️ +2.2`) | 0.0% | 5.3% | 🟢 ZYSK |
| #7 | `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 75.5 → 🟡 ** 77.0** (`⬆️ +1.5`) | 0.0% | 5.4% | 🟢 ZYSK |
| #8 | `L3_SO-01_HERESY_SET2` | SO-01 (Patrol Familiariuszy): dodaj heresy = 2 | 75.5 → 🟡 ** 76.8** (`⬆️ +1.3`) | 0.0% | 5.3% | 🟢 ZYSK |
| #9 | `L3_SO-01_HERESY_SET1` | SO-01 (Patrol Familiariuszy): dodaj heresy = 1 | 75.5 → 🟡 ** 76.3** (`⬆️ +0.8`) | 0.0% | 5.3% | 🟢 ZYSK |
| #10 | `L3_SO-01_HERESY_PLUS1` | SO-01 (Patrol Familiariuszy): heresy 0 → 1 | 75.5 → 🟡 ** 76.3** (`⬆️ +0.8`) | 0.0% | 5.3% | 🟢 ZYSK |
| #11 | `L3_KB-02_COST_PLUS1` | KB-02 (Pobór Podatków): cost 1 → 2 | 75.5 → 🟡 ** 79.8** (`⬆️ +4.3`) | 0.0% | 6.3% | 🟢 ZYSK |
| #12 | `L3_KB-05_COST_PLUS1` | KB-05 (List Żelazny): cost 2 → 3 | 75.5 → 🟡 ** 77.5** (`⬆️ +2.0`) | 0.0% | 5.8% | 🟢 ZYSK |
| #13 | `L3_KB-07_HERESY_SET2` | KB-07 (Szantaż Pieczęcią): dodaj heresy = 2 | 75.5 → 🟡 ** 76.6** (`⬆️ +1.1`) | 0.0% | 5.3% | 🟢 ZYSK |
| #14 | `L3_GC-09_GOLD_SET1` | GC-09 (Lista Dłużników): dodaj gold = 1 | 75.5 → 🟡 ** 76.0** (`⬆️ +0.5`) | 0.0% | 5.3% | 🟢 ZYSK |
| #15 | `L3_GC-09_GOLD_PLUS1` | GC-09 (Lista Dłużników): gold 0 → 1 | 75.5 → 🟡 ** 76.0** (`⬆️ +0.5`) | 0.0% | 5.3% | 🟢 ZYSK |
| #16 | `L3_GC-08_TARGET_HERESY_MINUS1` | GC-08 (Zatrute Złoto): target_heresy 1 → 0 | 75.5 → 🟡 ** 75.8** (`⬆️ +0.3`) | 0.0% | 5.3% | 🟢 ZYSK |
| #17 | `L3_GC-10_COST_MINUS1` | GC-10 (Upadek Domu): cost 4 → 3 | 75.5 → 🟡 ** 77.7** (`⬆️ +2.2`) | 0.0% | 5.3% | 🟢 ZYSK |
| #18 | `L3_SO-06_HERESY_SET2` | SO-06 (Areszt Trybunalski): dodaj heresy = 2 | 75.5 → 🟡 ** 77.5** (`⬆️ +2.0`) | 0.0% | 5.1% | 🟢 ZYSK |
| #19 | `L3_CAA-10_GOLD_SET3` | CAA-10 (Echo Alhambry): dodaj gold = 3 | 75.5 → 🟡 ** 77.3** (`⬆️ +1.8`) | 0.0% | 5.3% | 🟢 ZYSK |
| #20 | `L3_CAA-05_TARGET_HERESY_SET2` | CAA-05 (Ukryty Kurier): dodaj target_heresy = 2 | 75.5 → 🟡 ** 76.7** (`⬆️ +1.2`) | 0.0% | 5.3% | 🟢 ZYSK |