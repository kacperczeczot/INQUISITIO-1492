[Strona główna](../../../../../README.md) > [v1.0-alpha.26](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.26 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.25` (4P: `27.6 pkt`) → **Nowa Wersja:** `v1.0-alpha.26` (4P: `35.5 pkt`)
**Data:** 2026-08-22 22:35 | **Czas Trwania Iteracji:** 722.1s | **Zysk 4P:** `+7.9 pkt` | **Zysk Global:** `+3.3 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L2_GC_FALLS_MINUS1` — **Gildia Upadki: 8 → 7**
- **Opis Modyfikacji:** Gildia Cieni: Upadki offset -1
- **Wynik Kanonu 4P Balance:** 27.6 → 🔴 ** 35.5** (`⬆️ +7.9`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 66.3 pkt
  - `4p-no-cienie`: 7.0 → 9.1 (`⬆️ +2.1`) pkt
  - `4p-no-kabala`: 14.9 → 24.1 (`⬆️ +9.2`) pkt
  - `4p-no-korona`: 17.5 → 22.4 (`⬆️ +4.9`) pkt
  - `4p-no-oficjum`: 32.3 → 55.5 (`⬆️ +23.2`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 24.2 → 25.8 (`⬆️ +1.6`) pkt
- **Tryb 4-osobowy (4p Avg):** 26.8 → 34.0 (`⬆️ +7.2`) pkt
- **Tryb 5-osobowy (5p Avg):** 1.9 → 2.9 (`⬆️ +1.0`) pkt
- **Global Game Balance Score:** 17.6 → 🔴 ** 20.9** (`⬆️ +3.3`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `4.78 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `3.4%` (norma: <30%)
  - **Autodafé / partię:** `1.76`
  - **Oskarżenia / partię:** `5.00`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L2_GC_FALLS_MINUS1` | Gildia Upadki: 8 → 7 | 27.6 → 🔴 ** 35.5** (`⬆️ +7.9`) | 0.0% | 3.4% | 🌟 ZWYCIĘZCA |
| #2 | `L2_SO_STACKS_PLUS2` | Oficjum Stosy: 6 → 8 | 27.6 → 🔴 ** 34.2** (`⬆️ +6.6`) | 0.0% | 3.6% | 🟢 ZYSK |
| #3 | `L1_INTRIGUE_GOLD_PLUS1` | Akcja Gospodarcza: 1 → 2 | 27.6 → 🔴 ** 34.2** (`⬆️ +6.6`) | 0.0% | 2.9% | 🟢 ZYSK |
| #4 | `L1_INTRIGUE_GOLD_DOUBLE` | Akcja Gospodarcza: 1 → 2 (podwojenie) | 27.6 → 🔴 ** 34.2** (`⬆️ +6.6`) | 0.0% | 2.9% | 🟢 ZYSK |
| #5 | `L3_KB-05_GOLD_SET1` | KB-05 (List Żelazny): dodaj gold = 1 | 27.6 → 🔴 ** 33.6** (`⬆️ +6.0`) | 0.0% | 3.0% | 🟢 ZYSK |
| #6 | `L3_KB-05_GOLD_PLUS1` | KB-05 (List Żelazny): gold 0 → 1 | 27.6 → 🔴 ** 33.6** (`⬆️ +6.0`) | 0.0% | 3.0% | 🟢 ZYSK |
| #7 | `L3_KB-05_COST_MINUS1` | KB-05 (List Żelazny): cost 2 → 1 | 27.6 → 🔴 ** 33.4** (`⬆️ +5.8`) | 0.0% | 2.7% | 🟢 ZYSK |
| #8 | `L3_KB-12_GOLD_SET1` | KB-12 (Szantaż Salonowy): dodaj gold = 1 | 27.6 → 🔴 ** 33.2** (`⬆️ +5.6`) | 0.0% | 3.0% | 🟢 ZYSK |
| #9 | `L3_KB-12_GOLD_PLUS1` | KB-12 (Szantaż Salonowy): gold 0 → 1 | 27.6 → 🔴 ** 33.2** (`⬆️ +5.6`) | 0.0% | 3.0% | 🟢 ZYSK |
| #10 | `L3_GC-10_HERESY_MINUS1` | GC-10 (Upadek Domu): heresy 2 → 1 | 27.6 → 🔴 ** 32.9** (`⬆️ +5.3`) | 0.0% | 3.4% | 🟢 ZYSK |
| #11 | `L3_KB-06_GOLD_SET2` | KB-06 (Areszt Królewski): dodaj gold = 2 | 27.6 → 🔴 ** 32.4** (`⬆️ +4.8`) | 0.0% | 3.1% | 🟢 ZYSK |
| #12 | `L3_KB-09_HERESY_MINUS1` | KB-09 (Dekret Królewski): heresy 1 → 0 | 27.6 → 🔴 ** 32.0** (`⬆️ +4.4`) | 0.0% | 3.4% | 🟢 ZYSK |
| #13 | `L2_KT_FRAGS_PLUS2` | Kabała Fragmenty: offset +2 | 27.6 → 🔴 ** 31.8** (`⬆️ +4.2`) | 0.0% | 3.5% | 🟢 ZYSK |
| #14 | `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 6 → 7 | 27.6 → 🔴 ** 31.7** (`⬆️ +4.1`) | 0.0% | 3.5% | 🟢 ZYSK |
| #15 | `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2/3/3 → 3/4/4 | 27.6 → 🔴 ** 31.4** (`⬆️ +3.8`) | 0.0% | 3.5% | 🟢 ZYSK |
| #16 | `L2_SO_CONDEMNS_PLUS2` | Oficjum Skazania: 2/3/3 → 4/5/5 | 27.6 → 🔴 ** 31.4** (`⬆️ +3.8`) | 0.0% | 3.5% | 🟢 ZYSK |
| #17 | `L3_SO-10_GOLD_SET1` | SO-10 (Oczyść Miasto): dodaj gold = 1 | 27.6 → 🔴 ** 27.5** (`-0.1`) | 0.0% | 3.0% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_SO-10_GOLD_PLUS1` | SO-10 (Oczyść Miasto): gold 0 → 1 | 27.6 → 🔴 ** 27.5** (`-0.1`) | 0.0% | 3.0% | ⚪ STRATA/NEUTRALNY |
| #19 | `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 27.6 → 🔴 ** 26.4** (`-1.2`) | 0.0% | 3.5% | ⚪ STRATA/NEUTRALNY |
| #20 | `L2_KT_ERA_PLUS1` | Kabała Era: 6 → 7 | 27.6 → 🔴 ** 25.4** (`-2.2`) | 0.0% | 3.5% | ⚪ STRATA/NEUTRALNY |