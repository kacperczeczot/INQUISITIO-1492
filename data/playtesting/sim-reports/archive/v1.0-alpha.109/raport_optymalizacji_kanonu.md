# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.109 (Iteracja #1, Faza 1DD)

**Wersja Poprzednia:** `v1.0-alpha.108` (4P: `92.2 pkt`) → **Nowa Wersja:** `v1.0-alpha.109` (4P: `92.7 pkt`)
**Data:** 2026-08-30 02:49 | **Czas Trwania Iteracji:** 53.9s | **Zysk 4P:** `+0.5 pkt` | **Zysk Global:** `-0.7 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1DD):** `L3_KB-04_G0_H1` — **KB-04 (Faworyt Dworu): złoto 0→0, herezja 0→1**
- **Opis Modyfikacji:** Karta `kb-04` (Faworyt Dworu): `gold` → `0` + Karta `kb-04` (Faworyt Dworu): `heresy` → `1`
- **Wynik Kanonu 4P Balance:** 92.2 → 🟢 ** 92.7** (`⬆️ +0.5`) pkt (±0.85)
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 91.3 → 90.7 (`🔻 -0.6`) pkt
  - `4p-no-cienie`: 83.6 → 86.3 (`⬆️ +2.7`) pkt
  - `4p-no-kabala`: 95.4 → 95.7 (`⬆️ +0.3`) pkt
  - `4p-no-korona`: 97.0 → 97.0 (`= 0.0`) pkt
  - `4p-no-oficjum`: 93.6 → 94.0 (`⬆️ +0.4`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 55.7 → 54.2 (`🔻 -1.5`) pkt
- **Tryb 4-osobowy (4p Avg):** 92.2 → 92.7 (`⬆️ +0.5`) pkt
- **Tryb 5-osobowy (5p Avg):** 63.6 → 62.6 (`🔻 -1.0`) pkt
- **Global Game Balance Score:** 70.5 → 🟠 ** 69.8** (`🔻 -0.7`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.78 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.0%` (norma: <30%)
  - **Autodafé / partię:** `1.62`
  - **Oskarżenia / partię:** `7.56`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | CI 95% | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_KB-04_G0_H1` | KB-04 (Faworyt Dworu): złoto 0→0, herezja 0→1 | 92.2 → 🟢 ** 96.0** (`⬆️ +3.8`) | `[94.3, 97.7]` | 0.0% | 4.0% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-05_GOLD_PLUS1` | SO-05 (Wezwanie do Trybunału): gold 3 → 4 | 92.2 → 🟢 ** 95.7** (`⬆️ +3.5`) | `[94.0, 97.4]` | 0.0% | 4.1% | 🟢 ZYSK |
| #3 | `L3_GC-08_HERESY_MINUS2` | GC-08 (Zatrute Złoto): heresy 2 → 0 | 92.2 → 🟢 ** 95.6** (`⬆️ +3.4`) | `[93.9, 97.3]` | 0.0% | 4.1% | 🟢 ZYSK |
| #4 | `L3_KB-04_G1_H1` | KB-04 (Faworyt Dworu): złoto 0→1, herezja 0→1 | 92.2 → 🟢 ** 95.6** (`⬆️ +3.4`) | `[93.9, 97.3]` | 0.0% | 4.0% | 🟢 ZYSK |
| #5 | `L3_GC-05_HERESY_SET2` | GC-05 (Fałszywy Świadek): dodaj heresy = 2 | 92.2 → 🟢 ** 95.6** (`⬆️ +3.4`) | `[93.9, 97.3]` | 0.0% | 4.1% | 🟢 ZYSK |
| #6 | `L3_KT-10_GOLD_PLUS1` | KT-10 (Pieczęć Salomona): gold 0 → 1 | 92.2 → 🟢 ** 95.6** (`⬆️ +3.4`) | `[93.9, 97.3]` | 0.0% | 4.0% | 🟢 ZYSK |
| #7 | `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 2 → 3 | 92.2 → 🟢 ** 95.5** (`⬆️ +3.3`) | `[93.8, 97.2]` | 0.0% | 4.1% | 🟢 ZYSK |
| #8 | `L3_CAA-03_GOLD_PLUS1` | CAA-03 (Cień na Rynku): gold 2 → 3 | 92.2 → 🟢 ** 95.5** (`⬆️ +3.3`) | `[93.8, 97.2]` | 0.0% | 4.0% | 🟢 ZYSK |
| #9 | `L3_SO-05_G4_H5` | SO-05 (Wezwanie do Trybunału): złoto 3→4, herezja 4→5 | 92.2 → 🟢 ** 95.5** (`⬆️ +3.3`) | `[93.8, 97.2]` | 0.0% | 4.0% | 🟢 ZYSK |
| #10 | `L3_GC-08_G0_H1` | GC-08 (Zatrute Złoto): złoto 1→0, herezja 2→1 | 92.2 → 🟢 ** 95.5** (`⬆️ +3.3`) | `[93.8, 97.2]` | 0.0% | 4.1% | 🟢 ZYSK |
| #11 | `L3_GC-03_G1_H3` | GC-03 (Podrzucenie Księgi): złoto 0→1, herezja 2→3 | 92.2 → 🟢 ** 95.4** (`⬆️ +3.2`) | `[93.7, 97.1]` | 0.0% | 4.1% | 🟢 ZYSK |
| #12 | `L3_GC-04_GOLD_SET1` | GC-04 (Informator): dodaj gold = 1 | 92.2 → 🟢 ** 95.3** (`⬆️ +3.1`) | `[93.6, 97.0]` | 0.0% | 4.1% | 🟢 ZYSK |
| #13 | `L3_SO-05_G2_H5` | SO-05 (Wezwanie do Trybunału): złoto 3→2, herezja 4→5 | 92.2 → 🟢 ** 95.2** (`⬆️ +3.0`) | `[93.5, 96.9]` | 0.0% | 4.1% | 🟢 ZYSK |
| #14 | `L3_GC-05_GOLD_SET3` | GC-05 (Fałszywy Świadek): dodaj gold = 3 | 92.2 → 🟢 ** 95.2** (`⬆️ +3.0`) | `[93.5, 96.9]` | 0.0% | 4.1% | 🟢 ZYSK |
| #15 | `L3_GC-05_TARGET_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): target_heresy 0 → 1 | 92.2 → 🟢 ** 95.2** (`⬆️ +3.0`) | `[93.5, 96.9]` | 0.0% | 4.1% | 🟢 ZYSK |
| #16 | `L3_CAA-03_C0_G4` | CAA-03 (Cień na Rynku): koszt 0→0, złoto 2→4 | 92.2 → 🟢 ** 95.2** (`⬆️ +3.0`) | `[93.5, 96.9]` | 0.0% | 4.1% | 🟢 ZYSK |
| #17 | `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 0 → 1 | 92.2 → 🟢 ** 95.2** (`⬆️ +3.0`) | `[93.5, 96.9]` | 0.0% | 4.1% | 🟢 ZYSK |
| #18 | `L3_CAA-01_GOLD_SET2` | CAA-01 (Przejście Podziemiami): dodaj gold = 2 | 92.2 → 🟢 ** 95.2** (`⬆️ +3.0`) | `[93.5, 96.9]` | 0.0% | 4.1% | 🟢 ZYSK |
| #19 | `L3_CAA-09_C1_G1` | CAA-09 (Kurier Relikwii): koszt 0→1, złoto 0→1 | 92.2 → 🟢 ** 95.2** (`⬆️ +3.0`) | `[93.5, 96.9]` | 0.0% | 4.1% | 🟢 ZYSK |
| #20 | `L3_GC-07_GOLD_PLUS2` | GC-07 (Skrytobójstwo): gold 3 → 5 | 92.2 → 🟢 ** 95.2** (`⬆️ +3.0`) | `[93.5, 96.9]` | 0.0% | 4.1% | 🟢 ZYSK |
| #21 | `L3_CAA-11_C2_H1` | CAA-11 (Nocna Zmiana Warty): koszt 1→2, herezja 0→1 | 92.2 → 🟢 ** 95.1** (`⬆️ +2.9`) | `[93.3, 96.8]` | 0.0% | 4.1% | 🟢 ZYSK |
| #22 | `L3_CAA-12_COST_MINUS1` | CAA-12 (Skrytka w Murach): cost 1 → 0 | 92.2 → 🟢 ** 95.1** (`⬆️ +2.9`) | `[93.4, 96.8]` | 0.0% | 4.1% | 🟢 ZYSK |
| #23 | `L3_SO-07_G3_H0` | SO-07 (Przesłuchanie Oficjum): złoto 2→3, herezja 0→0 | 92.2 → 🟢 ** 95.1** (`⬆️ +2.9`) | `[93.4, 96.8]` | 0.0% | 4.0% | 🟢 ZYSK |
| #24 | `L1_OBSERVED_PLUS1` | Próg Obserwowanej: 3 → 4 | 92.2 → 🟢 ** 95.1** (`⬆️ +2.9`) | `[93.4, 96.8]` | 0.0% | 4.1% | 🟢 ZYSK |
| #25 | `L3_CAA-12_G5_H0` | CAA-12 (Skrytka w Murach): złoto 4→5, herezja 0→0 | 92.2 → 🟢 ** 95.1** (`⬆️ +2.9`) | `[93.4, 96.8]` | 0.0% | 4.1% | 🟢 ZYSK |
| #26 | `L3_CAA-10_GOLD_SET2` | CAA-10 (Echo Alhambry): dodaj gold = 2 | 92.2 → 🟢 ** 95.0** (`⬆️ +2.8`) | `[93.3, 96.7]` | 0.0% | 4.0% | 🟢 ZYSK |
| #27 | `L3_CAA-03_C0_G3` | CAA-03 (Cień na Rynku): koszt 0→0, złoto 2→3 | 92.2 → 🟢 ** 95.0** (`⬆️ +2.8`) | `[93.3, 96.7]` | 0.0% | 4.1% | 🟢 ZYSK |
| #28 | `L3_SO-05_TARGET_HERESY_MINUS2` | SO-05 (Wezwanie do Trybunału): target_heresy 3 → 1 | 92.2 → 🟢 ** 95.0** (`⬆️ +2.8`) | `[93.2, 96.8]` | 0.0% | 4.1% | 🟢 ZYSK |
| #29 | `L3_SO-05_GOLD_PLUS2` | SO-05 (Wezwanie do Trybunału): gold 3 → 5 | 92.2 → 🟢 ** 95.0** (`⬆️ +2.8`) | `[93.3, 96.7]` | 0.0% | 4.1% | 🟢 ZYSK |
| #30 | `L3_CAA-11_C2_G2` | CAA-11 (Nocna Zmiana Warty): koszt 1→2, złoto 1→2 | 92.2 → 🟢 ** 95.0** (`⬆️ +2.8`) | `[93.3, 96.7]` | 0.0% | 4.1% | 🟢 ZYSK |