[Strona główna](../../../../../README.md) > [v1.0-alpha.10](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.10 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.9` (4P: `76.5 pkt`) → **Nowa Wersja:** `v1.0-alpha.10` (4P: `76.9 pkt`)
**Data:** 2026-08-19 19:56 | **Czas Trwania Iteracji:** 821.7s | **Zysk 4P:** `+0.4 pkt` | **Zysk Global:** `-1.3 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_SO-03_TARGET_HERESY_PLUS1` — **SO-03 (Podejrzenie): target_heresy 1 → 2**
- **Opis Modyfikacji:** Karta `so-03` (Podejrzenie): `target_heresy` → `2`
- **Wynik Kanonu 4P Balance:** 76.5 → 🟡 ** 76.9** (`⬆️ +0.4`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 67.9 → 67.2 (`-0.7`) pkt
  - `4p-no-cienie`: 87.0 → 89.1 (`⬆️ +2.1`) pkt
  - `4p-no-kabala`: 61.1 pkt
  - `4p-no-korona`: 91.7 → 92.6 (`⬆️ +0.9`) pkt
  - `4p-no-oficjum`: 74.6 pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 22.3 → 22.9 (`⬆️ +0.6`) pkt
- **Tryb 4-osobowy (4p Avg):** 79.7 → 79.8 (`⬆️ +0.1`) pkt
- **Tryb 5-osobowy (5p Avg):** 38.7 → 34.2 (`-4.5`) pkt
- **Global Game Balance Score:** 46.9 → 🔴 ** 45.6** (`-1.3`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.21 Er`
  - **Deadlocki (Limit Er):** `0.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.6%` (norma: <30%)
  - **Autodafé / partię:** `2.22`
  - **Oskarżenia / partię:** `4.21`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-03_TARGET_HERESY_PLUS1` | SO-03 (Podejrzenie): target_heresy 1 → 2 | 76.5 → 🟡 ** 76.9** (`⬆️ +0.4`) | 0.3% | 1.6% | 🌟 ZWYCIĘZCA |
| #2 | `L3_GC-02_GOLD_PLUS1` | GC-02 (Czarny Rynek): gold 3 → 4 | 76.5 → 🟡 ** 76.8** (`⬆️ +0.3`) | 0.3% | 1.6% | 🟢 ZYSK |
| #3 | `L3_SO-06_TARGET_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): target_heresy 0 → 1 | 76.5 → 🟡 ** 76.7** (`⬆️ +0.2`) | 0.3% | 1.6% | 🟢 ZYSK |
| #4 | `L4_SEA_ROUTE_ERA_MINUS1` | Szlak Morski: Era 4 → 3 | 76.5 → 🟡 ** 76.6** (`⬆️ +0.1`) | 0.3% | 1.6% | 🟢 ZYSK |
| #5 | `L3_GC-11_COST_MINUS1` | GC-11 (Fałszywe Świadectwo Cechu): cost 1 → 0 | 76.5 → 🟡 ** 76.6** (`⬆️ +0.1`) | 0.3% | 1.5% | 🟢 ZYSK |
| #6 | `L3_KB-10_TARGET_HERESY_MINUS1` | KB-10 (Pieczęć Korony): target_heresy 1 → 0 | 76.5 → 🟡 ** 76.6** (`⬆️ +0.1`) | 0.3% | 1.6% | 🟢 ZYSK |
| #7 | `L3_SO-11_HERESY_PLUS1` | SO-11 (Dekret Czystości Wiary): heresy 1 → 2 | 🟡 ** 76.5** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_SO-12_TARGET_HERESY_PLUS1` | SO-12 (Straż Trybunalska): target_heresy 0 → 1 | 🟡 ** 76.5** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_GC-12_COST_PLUS1` | GC-12 (Złodziejski Zwiad): cost 0 → 1 | 76.5 → 🟡 ** 76.4** (`-0.1`) | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 1 → 2 | 76.5 → 🟡 ** 76.3** (`-0.2`) | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_SO-10_HERESY_MINUS1` | SO-10 (Oczyść Miasto): heresy 2 → 1 | 76.5 → 🟡 ** 76.3** (`-0.2`) | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 2 → 3 | 76.5 → 🟡 ** 75.9** (`-0.6`) | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |