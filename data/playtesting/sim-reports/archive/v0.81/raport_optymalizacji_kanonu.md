[Strona główna](../../../../../README.md) > [v0.81](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.81 (Iteracja #4, Faza 1D)

**Wersja Poprzednia:** `v0.80` (4P: `87.8 pkt`) → **Nowa Wersja:** `v0.81` (4P: `89.6 pkt`)
**Data:** 2026-08-17 03:09 | **Czas Trwania Iteracji:** 703.9s | **Zysk 4P:** `+1.8 pkt` | **Zysk Global:** `+2.2 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_KB-03_HERESY_PLUS1` — **KB-03 (Plotka Dworska): heresy 0 → 1**
- **Opis Modyfikacji:** Karta `kb-03` (Plotka Dworska): `heresy` → `1`
- **Wynik Kanonu 4P Score:** 87.8 → 🟡 ** 89.6** (`⬆️ +1.8`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 86.5 → 86.2 (`-0.3`) pkt
  - `4p-no-cienie`: 76.7 → 85.1 (`⬆️ +8.4`) pkt
  - `4p-no-kabala`: 94.7 → 94.3 (`-0.4`) pkt
  - `4p-no-korona`: 93.3 pkt
  - `4p-no-oficjum`: 88.0 → 89.3 (`⬆️ +1.3`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 40.5 → 44.4 (`⬆️ +3.9`) pkt
- **Tryb 4-osobowy (4p Avg):** 86.3 → 86.7 (`⬆️ +0.4`) pkt
- **Tryb 5-osobowy (5p Avg):** 67.3 → 69.7 (`⬆️ +2.4`) pkt
- **Global Game Balance Score:** 64.7 → 🟠 ** 66.9** (`⬆️ +2.2`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.01 Er`
  - **Deadlocki (Limit Er):** `1.4%` (norma: <5%)
  - **Pas Biedy (Złoto):** `5.8%` (norma: <30%)
  - **Autodafé / partię:** `1.56`
  - **Oskarżenia / partię:** `3.53`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_KB-03_HERESY_PLUS1` | KB-03 (Plotka Dworska): heresy 0 → 1 | 87.8 → 🟡 ** 89.6** (`⬆️ +1.8`) | 1.4% | 5.8% | 🌟 ZWYCIĘZCA |
| #2 | `L2_KB_ERA_MINUS1` | Korona Era: 4 → 3 | 87.8 → 🟡 ** 88.9** (`⬆️ +1.1`) | 1.4% | 5.9% | 🟢 ZYSK |
| #3 | `L3_SO-12_GOLD_PLUS1` | SO-12 (Straż Trybunalska): gold 1 → 2 | 87.8 → 🟡 ** 88.6** (`⬆️ +0.8`) | 1.4% | 5.7% | 🟢 ZYSK |
| #4 | `L3_SO-12_COST_MINUS1` | SO-12 (Straż Trybunalska): cost 1 → 0 | 87.8 → 🟡 ** 88.6** (`⬆️ +0.8`) | 1.4% | 5.7% | 🟢 ZYSK |
| #5 | `L3_KT-01_HERESY_PLUS1` | KT-01 (Rytuał Przejścia): heresy 0 → 1 | 87.8 → 🟡 ** 88.4** (`⬆️ +0.6`) | 1.5% | 5.9% | 🟢 ZYSK |
| #6 | `L3_KT-11_HERESY_PLUS1` | KT-11 (Medytacja Sefirot): heresy 0 → 1 | 87.8 → 🟡 ** 88.4** (`⬆️ +0.6`) | 1.5% | 5.9% | 🟢 ZYSK |
| #7 | `L2_KB_HOOKS_MINUS1` | Korona Haki: 1 → 0 | 87.8 → 🟡 ** 88.4** (`⬆️ +0.6`) | 1.4% | 5.9% | 🟢 ZYSK |
| #8 | `L3_KT-05_COST_PLUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 2 | 87.8 → 🟡 ** 88.3** (`⬆️ +0.5`) | 1.5% | 6.0% | 🟢 ZYSK |
| #9 | `L3_SO-10_HERESY_MINUS1` | SO-10 (Oczyść Miasto): heresy 2 → 1 | 87.8 → 🟡 ** 88.2** (`⬆️ +0.4`) | 1.6% | 5.9% | 🟢 ZYSK |
| #10 | `L1_MAX_ERAS_MINUS1` | Limit Er: 12 → 11 | 87.8 → 🟡 ** 88.0** (`⬆️ +0.2`) | 2.8% | 5.9% | 🟢 ZYSK |
| #11 | `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 87.8 → 🟡 ** 87.9** (`⬆️ +0.1`) | 1.4% | 5.9% | 🟢 ZYSK |
| #12 | `L2_CAA_ERA_MINUS1` | Cienie Era: 4 → 3 | 🟡 ** 87.8** | 1.4% | 5.9% | ⚪ STRATA/NEUTRALNY |
| #13 | `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 🟡 ** 87.8** | 1.4% | 5.9% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_CAA-08_HERESY_PLUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 2 | 🟡 ** 87.8** | 1.4% | 5.9% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_GC-05_TARGET_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): target_heresy 0 → 1 | 🟡 ** 87.8** | 1.4% | 5.9% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_CAA-08_HERESY_MINUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 0 | 🟡 ** 87.8** | 1.4% | 5.9% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_GC-05_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): heresy 0 → 1 | 🟡 ** 87.8** | 1.4% | 5.9% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_CAA-08_GOLD_PLUS1` | CAA-08 (Kaptur Nocy): gold 0 → 1 | 🟡 ** 87.8** | 1.4% | 5.9% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_KT-11_GOLD_MINUS1` | KT-11 (Medytacja Sefirot): gold 1 → 0 | 🟡 ** 87.8** | 1.4% | 5.9% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_GC-05_GOLD_PLUS1` | GC-05 (Fałszywy Świadek): gold 0 → 1 | 🟡 ** 87.8** | 1.4% | 5.9% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_KB-01_HERESY_PLUS1` | KB-01 (Rozkaz Dworu): heresy 1 → 2 | 🟡 ** 87.8** | 1.4% | 5.9% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_CAA-03_HERESY_PLUS1` | CAA-03 (Cień na Rynku): heresy 1 → 2 | 87.8 → 🟡 ** 87.7** (`-0.1`) | 1.5% | 5.8% | ⚪ STRATA/NEUTRALNY |
| #23 | `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 3 → 4 | 87.8 → 🟡 ** 87.7** (`-0.1`) | 1.4% | 5.9% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_SO-12_GOLD_MINUS1` | SO-12 (Straż Trybunalska): gold 1 → 0 | 87.8 → 🟡 ** 86.3** (`-1.5`) | 1.4% | 5.6% | ⚪ STRATA/NEUTRALNY |