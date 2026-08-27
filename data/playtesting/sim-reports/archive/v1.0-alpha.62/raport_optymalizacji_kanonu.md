[Strona główna](../../../../../README.md) > [v1.0-alpha.62](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.62 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.61` (4P: `66.4 pkt`) → **Nowa Wersja:** `v1.0-alpha.62` (4P: `67.9 pkt`)
**Data:** 2026-08-24 06:54 | **Czas Trwania Iteracji:** 451.1s | **Zysk 4P:** `+1.5 pkt` | **Zysk Global:** `+5.7 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_SO-01_GOLD_SET2` — **SO-01 (Patrol Familiariuszy): dodaj gold = 2**
- **Opis Modyfikacji:** Karta `so-01` (Patrol Familiariuszy): `gold` → `2`
- **Wynik Kanonu 4P Balance:** 66.4 → 🟠 ** 67.9** (`⬆️ +1.5`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 70.2 → 71.4 (`⬆️ +1.2`) pkt
  - `4p-no-cienie`: 50.4 → 47.7 (`-2.7`) pkt
  - `4p-no-kabala`: 66.2 → 70.9 (`⬆️ +4.7`) pkt
  - `4p-no-korona`: 87.1 → 91.4 (`⬆️ +4.3`) pkt
  - `4p-no-oficjum`: 58.3 pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 26.7 → 27.9 (`⬆️ +1.2`) pkt
- **Tryb 4-osobowy (4p Avg):** 45.2 → 61.3 (`⬆️ +16.1`) pkt
- **Tryb 5-osobowy (5p Avg):** 2.7 → 2.6 (`-0.1`) pkt
- **Global Game Balance Score:** 24.9 → 🔴 ** 30.6** (`⬆️ +5.7`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.83 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `5.3%` (norma: <30%)
  - **Autodafé / partię:** `1.42`
  - **Oskarżenia / partię:** `6.82`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-01_GOLD_SET2` | SO-01 (Patrol Familiariuszy): dodaj gold = 2 | 66.4 → 🟠 ** 67.9** (`⬆️ +1.5`) | 0.0% | 5.3% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KB-04_HERESY_PLUS1` | KB-04 (Faworyt Dworu): heresy 0 → 1 | 66.4 → 🟠 ** 69.3** (`⬆️ +2.9`) | 0.0% | 6.0% | 🟢 ZYSK |
| #3 | `L3_KB-04_HERESY_SET1` | KB-04 (Faworyt Dworu): dodaj heresy = 1 | 66.4 → 🟠 ** 69.3** (`⬆️ +2.9`) | 0.0% | 6.0% | 🟢 ZYSK |
| #4 | `L3_CAA-11_GOLD_MINUS1` | CAA-11 (Nocna Zmiana Warty): gold 3 → 2 | 66.4 → 🟠 ** 68.5** (`⬆️ +2.1`) | 0.0% | 6.0% | 🟢 ZYSK |
| #5 | `L3_CAA-11_COST_PLUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 2 | 66.4 → 🟠 ** 68.3** (`⬆️ +1.9`) | 0.0% | 6.0% | 🟢 ZYSK |
| #6 | `L3_SO-07_GOLD_SET2` | SO-07 (Przesłuchanie Oficjum): dodaj gold = 2 | 66.4 → 🟠 ** 67.6** (`⬆️ +1.2`) | 0.0% | 6.0% | 🟢 ZYSK |
| #7 | `L3_GC-08_TARGET_HERESY_MINUS1` | GC-08 (Zatrute Złoto): target_heresy 1 → 0 | 66.4 → 🟠 ** 67.2** (`⬆️ +0.8`) | 0.0% | 6.0% | 🟢 ZYSK |
| #8 | `L3_SO-12_HERESY_SET2` | SO-12 (Straż Trybunalska): dodaj heresy = 2 | 66.4 → 🟠 ** 67.2** (`⬆️ +0.8`) | 0.0% | 6.2% | 🟢 ZYSK |
| #9 | `L3_GC-01_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): heresy 1 → 2 | 66.4 → 🟠 ** 67.0** (`⬆️ +0.6`) | 0.0% | 6.0% | 🟢 ZYSK |
| #10 | `L3_GC-03_GOLD_SET3` | GC-03 (Podrzucenie Księgi): dodaj gold = 3 | 66.4 → 🟠 ** 66.9** (`⬆️ +0.5`) | 0.0% | 6.0% | 🟢 ZYSK |
| #11 | `L3_GC-03_GOLD_SET2` | GC-03 (Podrzucenie Księgi): dodaj gold = 2 | 66.4 → 🟠 ** 66.9** (`⬆️ +0.5`) | 0.0% | 6.0% | 🟢 ZYSK |
| #12 | `L3_CAA-12_GOLD_MINUS1` | CAA-12 (Skrytka w Murach): gold 4 → 3 | 66.4 → 🟠 ** 66.6** (`⬆️ +0.2`) | 0.0% | 6.0% | 🟢 ZYSK |
| #13 | `L3_KB-11_HERESY_PLUS1` | KB-11 (Tajny Emisariusz): heresy 0 → 1 | 🟠 ** 66.4** | 0.0% | 5.9% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_KB-11_HERESY_SET1` | KB-11 (Tajny Emisariusz): dodaj heresy = 1 | 🟠 ** 66.4** | 0.0% | 5.9% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_SO-05_TARGET_HERESY_MINUS1` | SO-05 (Wezwanie do Trybunału): target_heresy 1 → 0 | 66.4 → 🟠 ** 66.0** (`-0.4`) | 0.0% | 6.0% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_SO-12_COST_PLUS1` | SO-12 (Straż Trybunalska): cost 1 → 2 | 66.4 → 🟠 ** 65.2** (`-1.2`) | 0.0% | 6.4% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_KB-03_COST_PLUS1` | KB-03 (Plotka Dworska): cost 1 → 2 | 66.4 → 🟠 ** 64.3** (`-2.1`) | 0.0% | 6.8% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_KB-11_COST_MINUS1` | KB-11 (Tajny Emisariusz): cost 1 → 0 | 66.4 → 🟠 ** 64.3** (`-2.1`) | 0.0% | 5.1% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_SO-07_COST_MINUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 1 | 66.4 → 🟠 ** 68.1** (`⬆️ +1.7`) | 0.0% | 5.9% | 🟢 ZYSK |
| #20 | `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 4 → 5 Ery | 66.4 → 🟠 ** 70.5** (`⬆️ +4.1`) | 0.0% | 5.9% | 🟢 ZYSK |