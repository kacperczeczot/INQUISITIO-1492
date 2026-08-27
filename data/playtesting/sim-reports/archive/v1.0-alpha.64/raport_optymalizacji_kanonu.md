[Strona główna](../../../../../README.md) > [v1.0-alpha.64](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.64 (Iteracja #3, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.63` (4P: `68.8 pkt`) → **Nowa Wersja:** `v1.0-alpha.64` (4P: `73.1 pkt`)
**Data:** 2026-08-24 07:08 | **Czas Trwania Iteracji:** 432.4s | **Zysk 4P:** `+4.3 pkt` | **Zysk Global:** `+4.7 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_GC-08_HERESY_PLUS1` — **GC-08 (Zatrute Złoto): heresy 1 → 2**
- **Opis Modyfikacji:** Karta `gc-08` (Zatrute Złoto): `heresy` → `2`
- **Wynik Kanonu 4P Balance:** 68.8 → 🟠 ** 73.1** (`⬆️ +4.3`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 76.3 pkt
  - `4p-no-cienie`: 48.4 → 61.4 (`⬆️ +13.0`) pkt
  - `4p-no-kabala`: 76.2 → 69.1 (`-7.1`) pkt
  - `4p-no-korona`: 82.8 → 96.2 (`⬆️ +13.4`) pkt
  - `4p-no-oficjum`: 60.3 → 62.7 (`⬆️ +2.4`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 30.0 → 32.5 (`⬆️ +2.5`) pkt
- **Tryb 4-osobowy (4p Avg):** 61.6 → 72.7 (`⬆️ +11.1`) pkt
- **Tryb 5-osobowy (5p Avg):** 2.4 → 2.8 (`⬆️ +0.4`) pkt
- **Global Game Balance Score:** 31.3 → 🔴 ** 36.0** (`⬆️ +4.7`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.80 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `5.3%` (norma: <30%)
  - **Autodafé / partię:** `1.40`
  - **Oskarżenia / partię:** `6.88`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 1 → 2 | 68.8 → 🟠 ** 73.1** (`⬆️ +4.3`) | 0.0% | 5.3% | 🌟 ZWYCIĘZCA |
| #2 | `L3_GC-08_TARGET_HERESY_MINUS1` | GC-08 (Zatrute Złoto): target_heresy 1 → 0 | 68.8 → 🟠 ** 72.5** (`⬆️ +3.7`) | 0.0% | 5.3% | 🟢 ZYSK |
| #3 | `L3_GC-03_HERESY_SET2` | GC-03 (Podrzucenie Księgi): dodaj heresy = 2 | 68.8 → 🟠 ** 72.3** (`⬆️ +3.5`) | 0.0% | 5.3% | 🟢 ZYSK |
| #4 | `L3_KB-07_COST_PLUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 3 | 68.8 → 🟠 ** 71.7** (`⬆️ +2.9`) | 0.0% | 5.4% | 🟢 ZYSK |
| #5 | `L3_GC-03_TARGET_HERESY_MINUS1` | GC-03 (Podrzucenie Księgi): target_heresy 1 → 0 | 68.8 → 🟠 ** 71.6** (`⬆️ +2.8`) | 0.0% | 5.3% | 🟢 ZYSK |
| #6 | `L3_SO-08_GOLD_SET3` | SO-08 (Nasłanie Inkwizytora): dodaj gold = 3 | 68.8 → 🟠 ** 71.1** (`⬆️ +2.3`) | 0.0% | 4.6% | 🟢 ZYSK |
| #7 | `L3_SO-02_GOLD_PLUS1` | SO-02 (Skarbiec Trybunału): gold 2 → 3 | 68.8 → 🟠 ** 71.1** (`⬆️ +2.3`) | 0.0% | 4.8% | 🟢 ZYSK |
| #8 | `L3_KT-04_TARGET_HERESY_PLUS1` | KT-04 (Zwierciadło Herezji): target_heresy 1 → 2 | 68.8 → 🟠 ** 70.9** (`⬆️ +2.1`) | 0.0% | 5.3% | 🟢 ZYSK |
| #9 | `L3_KT-08_GOLD_SET1` | KT-08 (Areszt Wiedzy): dodaj gold = 1 | 68.8 → 🟠 ** 68.7** (`-0.1`) | 0.0% | 5.2% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_KB-03_COST_PLUS1` | KB-03 (Plotka Dworska): cost 1 → 2 | 68.8 → 🟠 ** 68.2** (`-0.6`) | 0.0% | 6.1% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_SO-02_COST_MINUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 0 | 68.8 → 🟠 ** 70.4** (`⬆️ +1.6`) | 0.0% | 4.6% | 🟢 ZYSK |
| #12 | `L3_KB-05_COST_PLUS1` | KB-05 (List Żelazny): cost 2 → 3 | 68.8 → 🟠 ** 69.7** (`⬆️ +0.9`) | 0.0% | 5.9% | 🟢 ZYSK |
| #13 | `L3_KB-02_COST_PLUS1` | KB-02 (Pobór Podatków): cost 1 → 2 | 68.8 → 🟠 ** 70.1** (`⬆️ +1.3`) | 0.0% | 6.5% | 🟢 ZYSK |
| #14 | `L3_KB-01_HERESY_MINUS1` | KB-01 (Rozkaz Dworu): heresy 1 → 0 | 68.8 → 🟠 ** 70.4** (`⬆️ +1.6`) | 0.0% | 5.4% | 🟢 ZYSK |
| #15 | `L3_SO-10_COST_PLUS1` | SO-10 (Oczyść Miasto): cost 5 → 6 | 68.8 → 🟠 ** 70.8** (`⬆️ +2.0`) | 0.0% | 5.0% | 🟢 ZYSK |
| #16 | `L3_SO-02_HERESY_SET2` | SO-02 (Skarbiec Trybunału): dodaj heresy = 2 | 68.8 → 🟠 ** 70.4** (`⬆️ +1.6`) | 0.0% | 5.7% | 🟢 ZYSK |
| #17 | `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 4 → 5 Ery | 68.8 → 🟠 ** 69.9** (`⬆️ +1.1`) | 0.0% | 5.1% | 🟢 ZYSK |
| #18 | `L3_GC-03_GOLD_SET3` | GC-03 (Podrzucenie Księgi): dodaj gold = 3 | 68.8 → 🟠 ** 69.2** (`⬆️ +0.4`) | 0.0% | 5.3% | 🟢 ZYSK |
| #19 | `L3_KB-04_TARGET_HERESY_SET2` | KB-04 (Faworyt Dworu): dodaj target_heresy = 2 | 68.8 → 🟠 ** 68.2** (`-0.6`) | 0.0% | 5.3% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_CAA-10_GOLD_SET3` | CAA-10 (Echo Alhambry): dodaj gold = 3 | 68.8 → 🟠 ** 64.9** (`-3.9`) | 0.0% | 5.2% | ⚪ STRATA/NEUTRALNY |