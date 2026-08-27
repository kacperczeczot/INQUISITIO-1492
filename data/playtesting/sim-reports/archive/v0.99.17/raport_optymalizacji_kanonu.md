[Strona główna](../../../../../README.md) > [v0.99.17](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.99.17 (Iteracja #4, Faza 1D)

**Wersja Poprzednia:** `v0.99.16` (4P: `69.3 pkt`) → **Nowa Wersja:** `v0.99.17` (4P: `70.7 pkt`)
**Data:** 2026-08-18 13:30 | **Czas Trwania Iteracji:** 653.4s | **Zysk 4P:** `+1.4 pkt` | **Zysk Global:** `+2.4 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_CAA-12_HERESY_MINUS1` — **CAA-12 (Skrytka w Murach): heresy 1 → 0**
- **Opis Modyfikacji:** Karta `caa-12` (Skrytka w Murach): `heresy` → `0`
- **Wynik Kanonu 4P Score:** 69.3 → 🟠 ** 70.7** (`⬆️ +1.4`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 69.2 → 73.0 (`⬆️ +3.8`) pkt
  - `4p-no-cienie`: 68.7 pkt
  - `4p-no-kabala`: 62.9 → 64.7 (`⬆️ +1.8`) pkt
  - `4p-no-korona`: 82.7 → 80.4 (`-2.3`) pkt
  - `4p-no-oficjum`: 62.9 → 66.7 (`⬆️ +3.8`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 14.5 → 14.8 (`⬆️ +0.3`) pkt
- **Tryb 4-osobowy (4p Avg):** 70.2 → 71.8 (`⬆️ +1.6`) pkt
- **Tryb 5-osobowy (5p Avg):** 37.3 → 42.8 (`⬆️ +5.5`) pkt
- **Global Game Balance Score:** 40.7 → 🔴 ** 43.1** (`⬆️ +2.4`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.21 Er`
  - **Deadlocki (Limit Er):** `0.7%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.5%` (norma: <30%)
  - **Autodafé / partię:** `2.23`
  - **Oskarżenia / partię:** `3.82`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-12_HERESY_MINUS1` | CAA-12 (Skrytka w Murach): heresy 1 → 0 | 69.3 → 🟠 ** 70.7** (`⬆️ +1.4`) | 0.7% | 1.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-09_TARGET_HERESY_PLUS1` | SO-09 (Świadek Koronny): target_heresy 0 → 1 | 69.3 → 🟠 ** 70.0** (`⬆️ +0.7`) | 0.6% | 1.5% | 🟢 ZYSK |
| #3 | `L3_SO-01_TARGET_HERESY_PLUS1` | SO-01 (Patrol Familiariuszy): target_heresy 0 → 1 | 69.3 → 🟠 ** 69.8** (`⬆️ +0.5`) | 0.6% | 1.5% | 🟢 ZYSK |
| #4 | `L3_SO-03_TARGET_HERESY_PLUS1` | SO-03 (Podejrzenie): target_heresy 1 → 2 | 69.3 → 🟠 ** 69.8** (`⬆️ +0.5`) | 0.6% | 1.5% | 🟢 ZYSK |
| #5 | `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 2 → 3 | 69.3 → 🟠 ** 69.6** (`⬆️ +0.3`) | 0.6% | 1.5% | 🟢 ZYSK |
| #6 | `L3_KT-11_COST_PLUS1` | KT-11 (Medytacja Sefirot): cost 1 → 2 | 69.3 → 🟠 ** 69.6** (`⬆️ +0.3`) | 0.6% | 1.5% | 🟢 ZYSK |
| #7 | `L3_KT-01_COST_MINUS1` | KT-01 (Rytuał Przejścia): cost 1 → 0 | 69.3 → 🟠 ** 69.4** (`⬆️ +0.1`) | 0.6% | 1.5% | 🟢 ZYSK |
| #8 | `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 69.3 → 🟠 ** 69.4** (`⬆️ +0.1`) | 0.6% | 1.5% | 🟢 ZYSK |
| #9 | `L3_KT-03_GOLD_PLUS1` | KT-03 (Zakazana Wiedza): gold 0 → 1 | 🟠 ** 69.3** | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_KT-12_COST_PLUS1` | KT-12 (Strażnik Archiwum): cost 0 → 1 | 69.3 → 🟠 ** 69.2** (`-0.1`) | 0.6% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_KT-07_COST_PLUS1` | KT-07 (Archiwum Ukryte): cost 1 → 2 | 69.3 → 🟠 ** 69.2** (`-0.1`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #12 | `L1_MAX_ERAS_MINUS1` | Limit Er: 13 → 12 | 69.3 → 🟠 ** 68.8** (`-0.5`) | 1.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_KB-01_HERESY_MINUS1` | KB-01 (Rozkaz Dworu): heresy 1 → 0 | 69.3 → 🟠 ** 69.4** (`⬆️ +0.1`) | 0.6% | 1.6% | 🟢 ZYSK |
| #14 | `L3_KB-06_COST_MINUS1` | KB-06 (Areszt Królewski): cost 2 → 1 | 69.3 → 🟠 ** 68.9** (`-0.4`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_SO-10_TARGET_HERESY_PLUS1` | SO-10 (Oczyść Miasto): target_heresy 0 → 1 | 69.3 → 🟠 ** 69.5** (`⬆️ +0.2`) | 0.5% | 1.5% | 🟢 ZYSK |
| #16 | `L3_SO-02_GOLD_MINUS1` | SO-02 (Skarbiec Trybunału): gold 3 → 2 | 69.3 → 🟠 ** 69.2** (`-0.1`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 69.3 → 🟠 ** 69.1** (`-0.2`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_GC-11_COST_MINUS1` | GC-11 (Fałszywe Świadectwo Cechu): cost 1 → 0 | 69.3 → 🟠 ** 69.9** (`⬆️ +0.6`) | 0.6% | 1.5% | 🟢 ZYSK |
| #19 | `L3_KT-06_TARGET_HERESY_PLUS1` | KT-06 (Przesłuchanie Imienia): target_heresy 0 → 1 | 69.3 → 🟠 ** 69.5** (`⬆️ +0.2`) | 0.5% | 1.5% | 🟢 ZYSK |
| #20 | `L3_SO-10_HERESY_PLUS1` | SO-10 (Oczyść Miasto): heresy 2 → 3 | 69.3 → 🟠 ** 68.4** (`-0.9`) | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_SO-10_GOLD_PLUS1` | SO-10 (Oczyść Miasto): gold 0 → 1 | 69.3 → 🟠 ** 68.4** (`-0.9`) | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_GC-01_TARGET_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): target_heresy 0 → 1 | 69.3 → 🟠 ** 70.5** (`⬆️ +1.2`) | 0.6% | 1.5% | 🟢 ZYSK |
| #23 | `L3_KB-10_TARGET_HERESY_PLUS1` | KB-10 (Pieczęć Korony): target_heresy 0 → 1 | 69.3 → 🟠 ** 69.1** (`-0.2`) | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_KT-03_TARGET_HERESY_PLUS1` | KT-03 (Zakazana Wiedza): target_heresy 0 → 1 | 🟠 ** 69.3** | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |