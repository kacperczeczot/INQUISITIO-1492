[Strona główna](../../../../../README.md) > [v0.99.14](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.99.14 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v0.99.13` (4P: `65.8 pkt`) → **Nowa Wersja:** `v0.99.14` (4P: `68.6 pkt`)
**Data:** 2026-08-18 12:56 | **Czas Trwania Iteracji:** 645.5s | **Zysk 4P:** `+2.8 pkt` | **Zysk Global:** `0.0 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_KB-01_TARGET_HERESY_PLUS1` — **KB-01 (Rozkaz Dworu): target_heresy 0 → 1**
- **Opis Modyfikacji:** Karta `kb-01` (Rozkaz Dworu): `target_heresy` → `1`
- **Wynik Kanonu 4P Score:** 65.8 → 🟠 ** 68.6** (`⬆️ +2.8`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 74.5 → 71.8 (`-2.7`) pkt
  - `4p-no-cienie`: 57.4 → 63.7 (`⬆️ +6.3`) pkt
  - `4p-no-kabala`: 59.7 pkt
  - `4p-no-korona`: 84.6 pkt
  - `4p-no-oficjum`: 52.8 → 63.4 (`⬆️ +10.6`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 14.2 → 14.3 (`⬆️ +0.1`) pkt
- **Tryb 4-osobowy (4p Avg):** 59.5 → 63.2 (`⬆️ +3.7`) pkt
- **Tryb 5-osobowy (5p Avg):** 40.5 → 36.7 (`-3.8`) pkt
- **Global Game Balance Score:** 🔴 ** 38.1** pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.14 Er`
  - **Deadlocki (Limit Er):** `0.6%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.5%` (norma: <30%)
  - **Autodafé / partię:** `2.17`
  - **Oskarżenia / partię:** `3.74`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_KB-01_TARGET_HERESY_PLUS1` | KB-01 (Rozkaz Dworu): target_heresy 0 → 1 | 65.8 → 🟠 ** 68.6** (`⬆️ +2.8`) | 0.6% | 1.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KB-06_TARGET_HERESY_PLUS1` | KB-06 (Areszt Królewski): target_heresy 0 → 1 | 65.8 → 🟠 ** 68.4** (`⬆️ +2.6`) | 0.6% | 1.6% | 🟢 ZYSK |
| #3 | `L3_KB-12_HERESY_PLUS1` | KB-12 (Szantaż Salonowy): heresy 0 → 1 | 65.8 → 🟠 ** 67.7** (`⬆️ +1.9`) | 0.5% | 1.5% | 🟢 ZYSK |
| #4 | `L3_KB-11_TARGET_HERESY_PLUS1` | KB-11 (Tajny Emisariusz): target_heresy 0 → 1 | 65.8 → 🟠 ** 67.6** (`⬆️ +1.8`) | 0.6% | 1.5% | 🟢 ZYSK |
| #5 | `L3_CAA-03_TARGET_HERESY_PLUS1` | CAA-03 (Cień na Rynku): target_heresy 0 → 1 | 65.8 → 🟠 ** 64.9** (`-0.9`) | 0.5% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_KB-05_HERESY_PLUS1` | KB-05 (List Żelazny): heresy 0 → 1 | 65.8 → 🟠 ** 66.4** (`⬆️ +0.6`) | 0.6% | 1.5% | 🟢 ZYSK |
| #7 | `L3_KT-07_COST_PLUS1` | KT-07 (Archiwum Ukryte): cost 1 → 2 | 65.8 → 🟠 ** 66.0** (`⬆️ +0.2`) | 0.6% | 1.5% | 🟢 ZYSK |
| #8 | `L3_KT-03_GOLD_PLUS1` | KT-03 (Zakazana Wiedza): gold 0 → 1 | 🟠 ** 65.8** | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_KB-01_COST_MINUS1` | KB-01 (Rozkaz Dworu): cost 1 → 0 | 65.8 → 🟠 ** 66.2** (`⬆️ +0.4`) | 0.5% | 0.6% | 🟢 ZYSK |
| #10 | `L3_GC-08_COST_MINUS1` | GC-08 (Zatrute Złoto): cost 2 → 1 | 65.8 → 🟠 ** 66.4** (`⬆️ +0.6`) | 0.6% | 1.5% | 🟢 ZYSK |
| #11 | `L3_KB-01_COST_PLUS1` | KB-01 (Rozkaz Dworu): cost 1 → 2 | 65.8 → 🟠 ** 65.6** (`-0.2`) | 0.6% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_SO-02_TARGET_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): target_heresy 1 → 2 | 65.8 → 🟠 ** 66.6** (`⬆️ +0.8`) | 0.5% | 1.5% | 🟢 ZYSK |
| #13 | `L3_SO-12_TARGET_HERESY_PLUS1` | SO-12 (Straż Trybunalska): target_heresy 0 → 1 | 65.8 → 🟠 ** 66.1** (`⬆️ +0.3`) | 0.6% | 1.5% | 🟢 ZYSK |
| #14 | `L3_SO-10_GOLD_PLUS1` | SO-10 (Oczyść Miasto): gold 0 → 1 | 65.8 → 🟠 ** 66.0** (`⬆️ +0.2`) | 0.6% | 1.5% | 🟢 ZYSK |
| #15 | `L3_SO-10_HERESY_PLUS1` | SO-10 (Oczyść Miasto): heresy 2 → 3 | 65.8 → 🟠 ** 66.0** (`⬆️ +0.2`) | 0.6% | 1.5% | 🟢 ZYSK |
| #16 | `L3_SO-10_TARGET_HERESY_PLUS1` | SO-10 (Oczyść Miasto): target_heresy 0 → 1 | 65.8 → 🟠 ** 66.0** (`⬆️ +0.2`) | 0.5% | 1.5% | 🟢 ZYSK |
| #17 | `L1_MAX_ERAS_MINUS1` | Limit Er: 13 → 12 | 65.8 → 🟠 ** 65.6** (`-0.2`) | 1.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_SO-02_GOLD_MINUS1` | SO-02 (Skarbiec Trybunału): gold 3 → 2 | 65.8 → 🟠 ** 65.9** (`⬆️ +0.1`) | 0.6% | 1.5% | 🟢 ZYSK |
| #19 | `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 65.8 → 🟠 ** 65.9** (`⬆️ +0.1`) | 0.6% | 1.5% | 🟢 ZYSK |
| #20 | `L3_SO-06_TARGET_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): target_heresy 0 → 1 | 65.8 → 🟠 ** 65.9** (`⬆️ +0.1`) | 0.6% | 1.5% | 🟢 ZYSK |
| #21 | `L3_SO-10_HERESY_MINUS1` | SO-10 (Oczyść Miasto): heresy 2 → 1 | 🟠 ** 65.8** | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_KT-05_COST_PLUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 2 | 65.8 → 🟠 ** 66.3** (`⬆️ +0.5`) | 0.6% | 1.4% | 🟢 ZYSK |
| #23 | `L3_KB-06_COST_MINUS1` | KB-06 (Areszt Królewski): cost 2 → 1 | 65.8 → 🟠 ** 65.9** (`⬆️ +0.1`) | 0.5% | 1.5% | 🟢 ZYSK |
| #24 | `L3_CAA-10_TARGET_HERESY_PLUS1` | CAA-10 (Echo Alhambry): target_heresy 0 → 1 | 65.8 → 🟠 ** 61.5** (`-4.3`) | 0.4% | 1.5% | ⚪ STRATA/NEUTRALNY |