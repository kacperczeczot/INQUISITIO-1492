[Strona główna](../../../../../README.md) > [v1.0-alpha.31](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.31 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.30` (4P: `48.9 pkt`) → **Nowa Wersja:** `v1.0-alpha.31` (4P: `65.7 pkt`)
**Data:** 2026-08-22 23:25 | **Czas Trwania Iteracji:** 603.2s | **Zysk 4P:** `+16.8 pkt` | **Zysk Global:** `-1.0 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L2_SO_CONDEMNS_PLUS1` — **Oficjum Skazania: 2/3/3 → 3/4/4**
- **Opis Modyfikacji:** Święte Oficjum: Skazania offset +1
- **Wynik Kanonu 4P Balance:** 48.9 → 🟠 ** 65.7** (`⬆️ +16.8`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 66.3 → 29.9 (`-36.4`) pkt
  - `4p-no-cienie`: 15.4 → 61.7 (`⬆️ +46.3`) pkt
  - `4p-no-kabala`: 38.3 → 60.9 (`⬆️ +22.6`) pkt
  - `4p-no-korona`: 38.0 → 89.9 (`⬆️ +51.9`) pkt
  - `4p-no-oficjum`: 86.3 pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 16.9 → 16.5 (`-0.4`) pkt
- **Tryb 4-osobowy (4p Avg):** 50.2 → 33.2 (`-17.0`) pkt
- **Tryb 5-osobowy (5p Avg):** 6.1 → 20.5 (`⬆️ +14.4`) pkt
- **Global Game Balance Score:** 24.4 → 🔴 ** 23.4** (`-1.0`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `4.82 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `3.4%` (norma: <30%)
  - **Autodafé / partię:** `1.75`
  - **Oskarżenia / partię:** `5.15`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2/3/3 → 3/4/4 | 48.9 → 🟠 ** 65.7** (`⬆️ +16.8`) | 0.0% | 3.4% | 🌟 ZWYCIĘZCA |
| #2 | `L2_SO_CONDEMNS_PLUS2` | Oficjum Skazania: 2/3/3 → 4/5/5 | 48.9 → 🟠 ** 65.7** (`⬆️ +16.8`) | 0.0% | 3.4% | 🟢 ZYSK |
| #3 | `L2_SO_STACKS_PLUS2` | Oficjum Stosy: 6 → 8 | 48.9 → 🟠 ** 60.2** (`⬆️ +11.3`) | 0.0% | 3.4% | 🟢 ZYSK |
| #4 | `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 6 → 7 | 48.9 → 🔴 ** 58.2** (`⬆️ +9.3`) | 0.0% | 3.4% | 🟢 ZYSK |
| #5 | `L3_KB-09_HERESY_MINUS1` | KB-09 (Dekret Królewski): heresy 1 → 0 | 48.9 → 🔴 ** 56.5** (`⬆️ +7.6`) | 0.0% | 3.3% | 🟢 ZYSK |
| #6 | `L3_KB-05_GOLD_PLUS1` | KB-05 (List Żelazny): gold 0 → 1 | 48.9 → 🔴 ** 53.7** (`⬆️ +4.8`) | 0.0% | 2.9% | 🟢 ZYSK |
| #7 | `L3_KB-05_GOLD_SET1` | KB-05 (List Żelazny): dodaj gold = 1 | 48.9 → 🔴 ** 53.7** (`⬆️ +4.8`) | 0.0% | 2.9% | 🟢 ZYSK |
| #8 | `L3_KB-06_GOLD_SET2` | KB-06 (Areszt Królewski): dodaj gold = 2 | 48.9 → 🔴 ** 53.5** (`⬆️ +4.6`) | 0.0% | 3.1% | 🟢 ZYSK |
| #9 | `L3_KB-04_HERESY_MINUS1` | KB-04 (Faworyt Dworu): heresy 1 → 0 | 48.9 → 🔴 ** 53.4** (`⬆️ +4.5`) | 0.0% | 3.3% | 🟢 ZYSK |
| #10 | `L1_OBSERVED_PLUS1` | Próg Obserwowanej: 5 → 6 | 48.9 → 🔴 ** 53.2** (`⬆️ +4.3`) | 0.0% | 3.4% | 🟢 ZYSK |
| #11 | `L3_SO-02_HERESY_SET2` | SO-02 (Skarbiec Trybunału): dodaj heresy = 2 | 48.9 → 🔴 ** 52.7** (`⬆️ +3.8`) | 0.0% | 3.6% | 🟢 ZYSK |
| #12 | `L3_KB-01_COST_PLUS1` | KB-01 (Rozkaz Dworu): cost 1 → 2 | 48.9 → 🔴 ** 52.5** (`⬆️ +3.6`) | 0.0% | 3.8% | 🟢 ZYSK |
| #13 | `L3_KB-10_COST_MINUS1` | KB-10 (Pieczęć Korony): cost 3 → 2 | 48.9 → 🔴 ** 52.4** (`⬆️ +3.5`) | 0.0% | 3.1% | 🟢 ZYSK |
| #14 | `L3_SO-10_GOLD_PLUS1` | SO-10 (Oczyść Miasto): gold 0 → 1 | 48.9 → 🔴 ** 52.2** (`⬆️ +3.3`) | 0.0% | 2.9% | 🟢 ZYSK |
| #15 | `L3_GC-09_HERESY_MINUS1` | GC-09 (Lista Dłużników): heresy 1 → 0 | 48.9 → 🔴 ** 52.1** (`⬆️ +3.2`) | 0.0% | 3.4% | 🟢 ZYSK |
| #16 | `L3_GC-04_HERESY_MINUS1` | GC-04 (Informator): heresy 1 → 0 | 48.9 → 🔴 ** 51.9** (`⬆️ +3.0`) | 0.0% | 3.4% | 🟢 ZYSK |
| #17 | `L3_KB-02_TARGET_HERESY_PLUS1` | KB-02 (Pobór Podatków): target_heresy 1 → 2 | 48.9 → 🔴 ** 51.9** (`⬆️ +3.0`) | 0.0% | 3.2% | 🟢 ZYSK |
| #18 | `L3_SO-05_TARGET_HERESY_MINUS1` | SO-05 (Wezwanie do Trybunału): target_heresy 1 → 0 | 48.9 → 🔴 ** 51.5** (`⬆️ +2.6`) | 0.0% | 3.3% | 🟢 ZYSK |
| #19 | `L2_GC_FALLS_MINUS1` | Gildia Upadki: 6 → 5 | 48.9 → 🔴 ** 37.9** (`-11.0`) | 0.0% | 3.3% | ⚪ STRATA/NEUTRALNY |
| #20 | `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 48.9 → 🔴 ** 34.8** (`-14.1`) | 0.0% | 4.0% | ⚪ STRATA/NEUTRALNY |