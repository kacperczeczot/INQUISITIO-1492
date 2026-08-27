[Strona główna](../../../../../README.md) > [v1.0-alpha.73](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.73 (Iteracja #7, Faza 2D)

**Wersja Poprzednia:** `v1.0-alpha.72` (4P: `78.0 pkt`) → **Nowa Wersja:** `v1.0-alpha.73` (4P: `81.1 pkt`)
**Data:** 2026-08-24 13:03 | **Czas Trwania Iteracji:** 8257.7s | **Zysk 4P:** `+3.1 pkt` | **Zysk Global:** `+10.9 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (2D):** `L3_SO-07_GOLD_SET2__L3_CAA-01_HERESY_SET1` — **SO-07 (Przesłuchanie Oficjum): dodaj gold = 2 + CAA-01 (Przejście Podziemiami): dodaj heresy = 1**
- **Opis Modyfikacji:** Karta `so-07` (Przesłuchanie Oficjum): `gold` → `2` + Karta `caa-01` (Przejście Podziemiami): `heresy` → `1`
- **Wynik Kanonu 4P Balance:** 78.0 → 🟡 ** 81.1** (`⬆️ +3.1`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 79.8 → 87.3 (`⬆️ +7.5`) pkt
  - `4p-no-cienie`: 67.0 → 78.2 (`⬆️ +11.2`) pkt
  - `4p-no-kabala`: 83.4 → 87.7 (`⬆️ +4.3`) pkt
  - `4p-no-korona`: 97.1 → 89.5 (`-7.6`) pkt
  - `4p-no-oficjum`: 62.8 → 63.0 (`⬆️ +0.2`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 34.5 → 29.9 (`-4.6`) pkt
- **Tryb 4-osobowy (4p Avg):** 72.2 pkt
- **Tryb 5-osobowy (5p Avg):** 3.2 → 40.5 (`⬆️ +37.3`) pkt
- **Global Game Balance Score:** 36.6 → 🔴 ** 47.5** (`⬆️ +10.9`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.78 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.3%` (norma: <30%)
  - **Autodafé / partię:** `1.53`
  - **Oskarżenia / partię:** `6.75`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-07_GOLD_SET2__L3_CAA-01_HERESY_SET1` | SO-07 (Przesłuchanie Oficjum): dodaj gold = 2 + CAA-01 (Przejście Podziemiami): dodaj heresy = 1 | 78.0 → 🟡 ** 81.1** (`⬆️ +3.1`) | 0.0% | 4.3% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-07_GOLD_SET2__L3_CAA-01_HERESY_PLUS1` | SO-07 (Przesłuchanie Oficjum): dodaj gold = 2 + CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 78.0 → 🟡 ** 81.1** (`⬆️ +3.1`) | 0.0% | 4.3% | 🟢 ZYSK |
| #3 | `L3_SO-07_GOLD_SET2__L3_CAA-01_COST_PLUS1` | SO-07 (Przesłuchanie Oficjum): dodaj gold = 2 + CAA-01 (Przejście Podziemiami): cost 1 → 2 | 78.0 → 🟡 ** 80.7** (`⬆️ +2.7`) | 0.0% | 4.3% | 🟢 ZYSK |
| #4 | `L3_KB-06_COST_MINUS1__L3_CAA-08_COST_PLUS1` | KB-06 (Areszt Królewski): cost 2 → 1 + CAA-08 (Kaptur Nocy): cost 2 → 3 | 78.0 → 🟡 ** 79.7** (`⬆️ +1.7`) | 0.0% | 4.3% | 🟢 ZYSK |
| #5 | `L3_KB-06_COST_MINUS1__L3_CAA-08_GOLD_MINUS1` | KB-06 (Areszt Królewski): cost 2 → 1 + CAA-08 (Kaptur Nocy): gold 3 → 2 | 78.0 → 🟡 ** 79.6** (`⬆️ +1.6`) | 0.0% | 4.3% | 🟢 ZYSK |
| #6 | `L3_KB-06_COST_MINUS1__L3_CAA-05_TARGET_HERESY_PLUS1` | KB-06 (Areszt Królewski): cost 2 → 1 + CAA-05 (Ukryty Kurier): target_heresy 2 → 3 | 78.0 → 🟡 ** 79.4** (`⬆️ +1.4`) | 0.0% | 4.3% | 🟢 ZYSK |
| #7 | `L3_SO-07_GOLD_SET2__L3_CAA-01_GOLD_SET3` | SO-07 (Przesłuchanie Oficjum): dodaj gold = 2 + CAA-01 (Przejście Podziemiami): dodaj gold = 3 | 78.0 → 🟡 ** 79.4** (`⬆️ +1.4`) | 0.0% | 4.3% | 🟢 ZYSK |
| #8 | `L3_SO-07_GOLD_SET2__L3_CAA-03_TARGET_HERESY_SET2` | SO-07 (Przesłuchanie Oficjum): dodaj gold = 2 + CAA-03 (Cień na Rynku): dodaj target_heresy = 2 | 78.0 → 🟡 ** 79.2** (`⬆️ +1.2`) | 0.0% | 4.3% | 🟢 ZYSK |
| #9 | `L3_KT-10_TARGET_HERESY_SET1__L3_CAA-01_GOLD_SET3` | KT-10 (Pieczęć Salomona): dodaj target_heresy = 1 + CAA-01 (Przejście Podziemiami): dodaj gold = 3 | 78.0 → 🟡 ** 78.8** (`⬆️ +0.8`) | 0.0% | 4.6% | 🟢 ZYSK |
| #10 | `L3_KT-10_TARGET_HERESY_PLUS1__L3_CAA-01_GOLD_SET3` | KT-10 (Pieczęć Salomona): target_heresy 0 → 1 + CAA-01 (Przejście Podziemiami): dodaj gold = 3 | 78.0 → 🟡 ** 78.8** (`⬆️ +0.8`) | 0.0% | 4.6% | 🟢 ZYSK |
| #11 | `L3_KB-06_COST_MINUS1__L3_CAA-08_HERESY_SET2` | KB-06 (Areszt Królewski): cost 2 → 1 + CAA-08 (Kaptur Nocy): dodaj heresy = 2 | 78.0 → 🟡 ** 78.4** (`⬆️ +0.4`) | 0.0% | 4.3% | 🟢 ZYSK |
| #12 | `L3_KB-06_COST_MINUS1__L3_CAA-08_HERESY_SET1` | KB-06 (Areszt Królewski): cost 2 → 1 + CAA-08 (Kaptur Nocy): dodaj heresy = 1 | 78.0 → 🟡 ** 78.3** (`⬆️ +0.3`) | 0.0% | 4.3% | 🟢 ZYSK |
| #13 | `L3_KB-06_COST_MINUS1__L3_CAA-08_HERESY_PLUS1` | KB-06 (Areszt Królewski): cost 2 → 1 + CAA-08 (Kaptur Nocy): heresy 0 → 1 | 78.0 → 🟡 ** 78.3** (`⬆️ +0.3`) | 0.0% | 4.3% | 🟢 ZYSK |
| #14 | `L3_KB-06_COST_MINUS1__L3_CAA-08_TARGET_HERESY_MINUS1` | KB-06 (Areszt Królewski): cost 2 → 1 + CAA-08 (Kaptur Nocy): target_heresy 2 → 1 | 78.0 → 🟡 ** 77.5** (`-0.5`) | 0.0% | 4.3% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_KB-06_COST_MINUS1__L3_CAA-04_HERESY_PLUS1` | KB-06 (Areszt Królewski): cost 2 → 1 + CAA-04 (Fałszywy Trop): heresy 0 → 1 | 78.0 → 🟡 ** 76.5** (`-1.5`) | 0.0% | 4.3% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_KB-06_COST_MINUS1__L3_CAA-04_HERESY_SET1` | KB-06 (Areszt Królewski): cost 2 → 1 + CAA-04 (Fałszywy Trop): dodaj heresy = 1 | 78.0 → 🟡 ** 76.5** (`-1.5`) | 0.0% | 4.3% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_SO-07_HERESY_SET2__L3_CAA-01_GOLD_SET3` | SO-07 (Przesłuchanie Oficjum): dodaj heresy = 2 + CAA-01 (Przejście Podziemiami): dodaj gold = 3 | 78.0 → 🟠 ** 74.9** (`-3.1`) | 0.0% | 4.4% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_CAA-10_GOLD_SET3__L3_GC-01_TARGET_HERESY_SET1` | CAA-10 (Echo Alhambry): dodaj gold = 3 + GC-01 (Przekupiony Strażnik): dodaj target_heresy = 1 | 78.0 → 🟠 ** 71.8** (`-6.2`) | 0.0% | 4.6% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_CAA-10_GOLD_SET3__L3_GC-01_TARGET_HERESY_PLUS1` | CAA-10 (Echo Alhambry): dodaj gold = 3 + GC-01 (Przekupiony Strażnik): target_heresy 0 → 1 | 78.0 → 🟠 ** 71.8** (`-6.2`) | 0.0% | 4.6% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_SO-07_GOLD_SET2__L3_CAA-01_TARGET_HERESY_MINUS1` | SO-07 (Przesłuchanie Oficjum): dodaj gold = 2 + CAA-01 (Przejście Podziemiami): target_heresy 1 → 0 | 78.0 → 🟡 ** 80.7** (`⬆️ +2.7`) | 0.0% | 4.3% | 🟢 ZYSK |