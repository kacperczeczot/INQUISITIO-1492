[Strona główna](../../../../../README.md) > [v1.0-alpha.36](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.36 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.35` (4P: `59.5 pkt`) → **Nowa Wersja:** `v1.0-alpha.36` (4P: `63.2 pkt`)
**Data:** 2026-08-23 03:49 | **Czas Trwania Iteracji:** 615.0s | **Zysk 4P:** `+3.7 pkt` | **Zysk Global:** `+4.4 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_KB-04_HERESY_MINUS1` — **KB-04 (Faworyt Dworu): heresy 1 → 0**
- **Opis Modyfikacji:** Karta `kb-04` (Faworyt Dworu): `heresy` → `0`
- **Wynik Kanonu 4P Balance:** 59.5 → 🟠 ** 63.2** (`⬆️ +3.7`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 59.9 → 55.3 (`-4.6`) pkt
  - `4p-no-cienie`: 33.9 → 53.8 (`⬆️ +19.9`) pkt
  - `4p-no-kabala`: 70.8 → 76.2 (`⬆️ +5.4`) pkt
  - `4p-no-korona`: 55.8 pkt
  - `4p-no-oficjum`: 77.3 → 74.8 (`-2.5`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 23.0 → 27.2 (`⬆️ +4.2`) pkt
- **Tryb 4-osobowy (4p Avg):** 57.8 → 60.9 (`⬆️ +3.1`) pkt
- **Tryb 5-osobowy (5p Avg):** 11.0 → 16.9 (`⬆️ +5.9`) pkt
- **Global Game Balance Score:** 30.6 → 🔴 ** 35.0** (`⬆️ +4.4`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `4.74 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `3.3%` (norma: <30%)
  - **Autodafé / partię:** `1.57`
  - **Oskarżenia / partię:** `4.71`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_KB-04_HERESY_MINUS1` | KB-04 (Faworyt Dworu): heresy 1 → 0 | 59.5 → 🟠 ** 63.2** (`⬆️ +3.7`) | 0.0% | 3.3% | 🌟 ZWYCIĘZCA |
| #2 | `L3_GC-09_HERESY_MINUS1` | GC-09 (Lista Dłużników): heresy 1 → 0 | 59.5 → 🟠 ** 62.5** (`⬆️ +3.0`) | 0.0% | 3.4% | 🟢 ZYSK |
| #3 | `L3_GC-04_HERESY_MINUS1` | GC-04 (Informator): heresy 1 → 0 | 59.5 → 🟠 ** 62.5** (`⬆️ +3.0`) | 0.0% | 3.4% | 🟢 ZYSK |
| #4 | `L3_GC-06_HERESY_MINUS1` | GC-06 (Szantaż): heresy 1 → 0 | 59.5 → 🟠 ** 62.5** (`⬆️ +3.0`) | 0.0% | 3.4% | 🟢 ZYSK |
| #5 | `L3_CAA-09_GOLD_SET2` | CAA-09 (Kurier Relikwii): dodaj gold = 2 | 59.5 → 🟠 ** 61.9** (`⬆️ +2.4`) | 0.0% | 3.4% | 🟢 ZYSK |
| #6 | `L3_CAA-09_GOLD_SET3` | CAA-09 (Kurier Relikwii): dodaj gold = 3 | 59.5 → 🟠 ** 61.8** (`⬆️ +2.3`) | 0.0% | 3.4% | 🟢 ZYSK |
| #7 | `L3_KT-09_HERESY_MINUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 0 | 59.5 → 🟠 ** 61.5** (`⬆️ +2.0`) | 0.0% | 3.4% | 🟢 ZYSK |
| #8 | `L1_OBSERVED_PLUS1` | Próg Obserwowanej: 5 → 6 | 59.5 → 🟠 ** 61.4** (`⬆️ +1.9`) | 0.0% | 3.3% | 🟢 ZYSK |
| #9 | `L3_GC-02_COST_PLUS1` | GC-02 (Czarny Rynek): cost 0 → 1 | 59.5 → 🟠 ** 61.1** (`⬆️ +1.6`) | 0.0% | 3.4% | 🟢 ZYSK |
| #10 | `L3_KB-01_HERESY_MINUS1` | KB-01 (Rozkaz Dworu): heresy 1 → 0 | 59.5 → 🟠 ** 61.0** (`⬆️ +1.5`) | 0.0% | 3.4% | 🟢 ZYSK |
| #11 | `L3_KB-11_COST_MINUS1` | KB-11 (Tajny Emisariusz): cost 1 → 0 | 59.5 → 🟠 ** 60.4** (`⬆️ +0.9`) | 0.0% | 2.8% | 🟢 ZYSK |
| #12 | `L3_KT-01_GOLD_SET2` | KT-01 (Rytuał Przejścia): dodaj gold = 2 | 59.5 → 🟠 ** 60.0** (`⬆️ +0.5`) | 0.0% | 3.3% | 🟢 ZYSK |
| #13 | `L3_SO-02_TARGET_HERESY_MINUS1` | SO-02 (Skarbiec Trybunału): target_heresy 1 → 0 | 59.5 → 🔴 ** 59.9** (`⬆️ +0.4`) | 0.0% | 3.5% | 🟢 ZYSK |
| #14 | `L3_KB-02_COST_MINUS1` | KB-02 (Pobór Podatków): cost 1 → 0 | 59.5 → 🔴 ** 59.0** (`-0.5`) | 0.0% | 2.6% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_SO-06_GOLD_SET3` | SO-06 (Areszt Trybunalski): dodaj gold = 3 | 59.5 → 🔴 ** 57.2** (`-2.3`) | 0.0% | 2.9% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_SO-12_TARGET_HERESY_SET2` | SO-12 (Straż Trybunalska): dodaj target_heresy = 2 | 59.5 → 🔴 ** 56.1** (`-3.4`) | 0.0% | 3.2% | ⚪ STRATA/NEUTRALNY |
| #17 | `L2_SO_CONDEMNS_PLUS2` | Oficjum Skazania: 2/3/3 → 4/5/5 | 59.5 → 🟠 ** 66.3** (`⬆️ +6.8`) | 0.0% | 3.4% | 🟢 ZYSK |
| #18 | `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2/3/3 → 3/4/4 | 59.5 → 🟠 ** 66.3** (`⬆️ +6.8`) | 0.0% | 3.4% | 🟢 ZYSK |
| #19 | `L2_SO_STACKS_PLUS2` | Oficjum Stosy: 6 → 8 | 59.5 → 🟠 ** 64.7** (`⬆️ +5.2`) | 0.0% | 3.4% | 🟢 ZYSK |
| #20 | `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 6 → 7 | 59.5 → 🟠 ** 64.5** (`⬆️ +5.0`) | 0.0% | 3.4% | 🟢 ZYSK |