# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.97 (Iteracja #1, Faza 2D (Beam 100)D)

**Wersja Poprzednia:** `v1.0-alpha.96` (4P: `94.5 pkt`) → **Nowa Wersja:** `v1.0-alpha.97` (4P: `94.6 pkt`)
**Data:** 2026-08-29 21:06 | **Czas Trwania Iteracji:** 3276.4s | **Zysk 4P:** `+0.1 pkt` | **Zysk Global:** `+0.1 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (2D (Beam 100)D):** `L3_CAA-08_COST_MINUS1__L3_CAA-08_GOLD_MINUS1__L3_SO-05_G3_H4` — **CAA-08 (Kaptur Nocy): cost 3 → 2 + CAA-08 (Kaptur Nocy): gold 3 → 2 + SO-05 (Wezwanie do Trybunału): złoto 2→3, herezja 3→4**
- **Opis Modyfikacji:** Karta `caa-08` (Kaptur Nocy): `cost` → `2` + Karta `caa-08` (Kaptur Nocy): `gold` → `2` + Karta `so-05` (Wezwanie do Trybunału): `gold` → `3` + Karta `so-05` (Wezwanie do Trybunału): `heresy` → `4`
- **Wynik Kanonu 4P Balance:** 94.5 → 🟢 ** 94.6** (`⬆️ +0.1`) pkt (±0.81)
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 92.7 → 92.9 (`⬆️ +0.2`) pkt
  - `4p-no-cienie`: 87.6 → 87.6 (`= 0.0`) pkt
  - `4p-no-kabala`: 97.1 → 97.4 (`⬆️ +0.3`) pkt
  - `4p-no-korona`: 97.1 → 97.0 (`🔻 -0.1`) pkt
  - `4p-no-oficjum`: 98.1 → 98.1 (`= 0.0`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 33.1 → 33.1 (`= 0.0`) pkt
- **Tryb 4-osobowy (4p Avg):** 94.5 → 94.6 (`⬆️ +0.1`) pkt
- **Tryb 5-osobowy (5p Avg):** 25.8 → 25.8 (`= 0.0`) pkt
- **Global Game Balance Score:** 51.1 → 🔴 ** 51.2** (`⬆️ +0.1`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.77 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.9%` (norma: <30%)
  - **Autodafé / partię:** `1.53`
  - **Oskarżenia / partię:** `7.64`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | CI 95% | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_KB-05_G0_H0__L3_SO-05_GOLD_PLUS1__L3_SO-05_HERESY_PLUS2__L3_SO-05_TARGET_HERESY_PLUS1` | KB-05 (List Żelazny): złoto 0→0, herezja 1→0 + SO-05 (Wezwanie do Trybunału): gold 2 → 3 + SO-05 (Wezwanie do Trybunału): heresy 3 → 5 + SO-05 (Wezwanie do Trybunału): target_heresy 3 → 4 | 94.5 → 🟢 ** 97.2** (`⬆️ +2.7`) | `[95.6, 98.8]` | 0.0% | 4.9% | 🟢 ZYSK |
| #2 | `L1_AUTODAFE_COOLDOWN_MINUS1__L1_AUTODAFE_COOLDOWN_PLUS1__L1_THRESHOLD_PLUS1__L3_SO-05_HERESY_MINUS1` | Cooldown Autodafé: 3 → 2 Ery + Cooldown Autodafé: 3 → 4 Ery + Próg Oskarżenia: 7 → 8 + SO-05 (Wezwanie do Trybunału): heresy 3 → 2 | 94.5 → 🟢 ** 97.2** (`⬆️ +2.7`) | `[95.6, 98.8]` | 0.0% | 4.9% | 🟢 ZYSK |
| #3 | `L3_CAA-08_COST_MINUS1__L3_CAA-08_GOLD_MINUS1__L3_SO-05_G3_H4` | CAA-08 (Kaptur Nocy): cost 3 → 2 + CAA-08 (Kaptur Nocy): gold 3 → 2 + SO-05 (Wezwanie do Trybunału): złoto 2→3, herezja 3→4 | 94.5 → 🟢 ** 97.1** (`⬆️ +2.6`) | `[95.5, 98.7]` | 0.0% | 4.9% | 🌟 ZWYCIĘZCA |
| #4 | `L3_CAA-03_GOLD_PLUS1__L3_GC-05_G0_H1__L3_GC-05_TARGET_HERESY_SET1` | CAA-03 (Cień na Rynku): gold 2 → 3 + GC-05 (Fałszywy Świadek): dodaj target_heresy = 1 + GC-05 (Fałszywy Świadek): złoto 0→0, herezja 0→1 | 94.5 → 🟢 ** 97.1** (`⬆️ +2.6`) | `[95.5, 98.7]` | 0.0% | 4.9% | 🟢 ZYSK |
| #5 | `L1_START_GOLD_MINUS1__L3_GC-05_C0_H1__L3_GC-05_GOLD_SET2` | GC-05 (Fałszywy Świadek): dodaj gold = 2 + GC-05 (Fałszywy Świadek): koszt 1→0, herezja 0→1 + Złoto startowe: 4zł → 3zł | 94.5 → 🟢 ** 97.1** (`⬆️ +2.6`) | `[95.5, 98.7]` | 0.0% | 4.9% | 🟢 ZYSK |
| #6 | `L1_AUTODAFE_COOLDOWN_PLUS1__L1_START_GOLD_MINUS1__L1_THRESHOLD_MINUS1__L3_CAA-01_C3_H3` | CAA-01 (Przejście Podziemiami): koszt 2→3, herezja 2→3 + Cooldown Autodafé: 3 → 4 Ery + Próg Oskarżenia: 7 → 6 + Złoto startowe: 4zł → 3zł | 94.5 → 🟢 ** 97.0** (`⬆️ +2.5`) | `[95.4, 98.6]` | 0.0% | 4.9% | 🟢 ZYSK |
| #7 | `L3_CAA-11_C2_G2__L3_GC-01_COST_MINUS1__L3_GC-01_GOLD_MINUS1` | CAA-11 (Nocna Zmiana Warty): koszt 1→2, złoto 1→2 + GC-01 (Przekupiony Strażnik): cost 1 → 0 + GC-01 (Przekupiony Strażnik): gold 1 → 0 | 94.5 → 🟢 ** 97.0** (`⬆️ +2.5`) | `[95.4, 98.6]` | 0.0% | 4.9% | 🟢 ZYSK |
| #8 | `L3_CAA-01_COST_PLUS1__L3_GC-05_COST_PLUS2__L3_GC-05_G1_H1__L3_GC-05_TARGET_HERESY_SET2` | CAA-01 (Przejście Podziemiami): cost 2 → 3 + GC-05 (Fałszywy Świadek): cost 1 → 3 + GC-05 (Fałszywy Świadek): dodaj target_heresy = 2 + GC-05 (Fałszywy Świadek): złoto 0→1, herezja 0→1 | 94.5 → 🟢 ** 97.0** (`⬆️ +2.5`) | `[95.4, 98.6]` | 0.0% | 4.9% | 🟢 ZYSK |
| #9 | `L3_CAA-01_G0_H3__L3_GC-05_COST_MINUS1__L3_GC-05_GOLD_SET1__L3_GC-05_HERESY_PLUS2` | CAA-01 (Przejście Podziemiami): złoto 0→0, herezja 2→3 + GC-05 (Fałszywy Świadek): cost 1 → 0 + GC-05 (Fałszywy Świadek): dodaj gold = 1 + GC-05 (Fałszywy Świadek): heresy 0 → 2 | 94.5 → 🟢 ** 97.0** (`⬆️ +2.5`) | `[95.4, 98.6]` | 0.0% | 4.9% | 🟢 ZYSK |
| #10 | `L3_CAA-01_G1_H3__L3_GC-05_G0_H1__L3_GC-05_TARGET_HERESY_SET1` | CAA-01 (Przejście Podziemiami): złoto 0→1, herezja 2→3 + GC-05 (Fałszywy Świadek): dodaj target_heresy = 1 + GC-05 (Fałszywy Świadek): złoto 0→0, herezja 0→1 | 94.5 → 🟢 ** 97.0** (`⬆️ +2.5`) | `[95.4, 98.6]` | 0.0% | 4.9% | 🟢 ZYSK |
| #11 | `L3_GC-05_C0_G2__L3_GC-05_HERESY_SET1__L3_GC-05_TARGET_HERESY_SET2__L3_SO-05_HERESY_MINUS1` | GC-05 (Fałszywy Świadek): dodaj heresy = 1 + GC-05 (Fałszywy Świadek): dodaj target_heresy = 2 + GC-05 (Fałszywy Świadek): koszt 1→0, złoto 0→2 + SO-05 (Wezwanie do Trybunału): heresy 3 → 2 | 94.5 → 🟢 ** 97.0** (`⬆️ +2.5`) | `[95.4, 98.6]` | 0.0% | 4.9% | 🟢 ZYSK |
| #12 | `L3_CAA-08_C4_H0__L3_SO-05_GOLD_PLUS1__L3_SO-05_HERESY_PLUS2__L3_SO-05_TARGET_HERESY_PLUS1` | CAA-08 (Kaptur Nocy): koszt 3→4, herezja 0→0 + SO-05 (Wezwanie do Trybunału): gold 2 → 3 + SO-05 (Wezwanie do Trybunału): heresy 3 → 5 + SO-05 (Wezwanie do Trybunału): target_heresy 3 → 4 | 94.5 → 🟢 ** 97.0** (`⬆️ +2.5`) | `[95.4, 98.6]` | 0.0% | 4.9% | 🟢 ZYSK |
| #13 | `L1_START_GOLD_PLUS1__L3_CAA-01_COST_MINUS2__L3_CAA-01_TARGET_HERESY_MINUS1` | CAA-01 (Przejście Podziemiami): cost 2 → 0 + CAA-01 (Przejście Podziemiami): target_heresy 1 → 0 + Złoto startowe: 4zł → 5zł | 94.5 → 🟢 ** 97.0** (`⬆️ +2.5`) | `[95.4, 98.6]` | 0.0% | 4.9% | 🟢 ZYSK |
| #14 | `L3_CAA-01_G1_H3__L3_CAA-08_COST_MINUS1__L3_CAA-08_GOLD_MINUS1` | CAA-01 (Przejście Podziemiami): złoto 0→1, herezja 2→3 + CAA-08 (Kaptur Nocy): cost 3 → 2 + CAA-08 (Kaptur Nocy): gold 3 → 2 | 94.5 → 🟢 ** 97.0** (`⬆️ +2.5`) | `[95.4, 98.6]` | 0.0% | 4.9% | 🟢 ZYSK |
| #15 | `L1_AUTODAFE_COOLDOWN_PLUS1__L2_KT_FRAGS_MINUS1__L3_SO-05_C0_G3__L4_SEA_ROUTE_ERA_PLUS1` | Cooldown Autodafé: 3 → 4 Ery + Kabała Fragmenty: 3 → 2 + SO-05 (Wezwanie do Trybunału): koszt 0→0, złoto 2→3 + Szlak Morski: Era 4 → 5 | 94.5 → 🟢 ** 97.0** (`⬆️ +2.5`) | `[95.4, 98.6]` | 0.0% | 4.9% | 🟢 ZYSK |
| #16 | `L1_AUTODAFE_COOLDOWN_MINUS1__L1_AUTODAFE_COOLDOWN_PLUS1__L1_START_GOLD_MINUS1__L3_CAA-01_C1_H3` | CAA-01 (Przejście Podziemiami): koszt 2→1, herezja 2→3 + Cooldown Autodafé: 3 → 2 Ery + Cooldown Autodafé: 3 → 4 Ery + Złoto startowe: 4zł → 3zł | 94.5 → 🟢 ** 97.0** (`⬆️ +2.5`) | `[95.4, 98.6]` | 0.0% | 4.9% | 🟢 ZYSK |
| #17 | `L1_THRESHOLD_PLUS1__L3_SO-05_C0_H4__L3_SO-05_GOLD_PLUS2__L3_SO-05_TARGET_HERESY_MINUS2` | Próg Oskarżenia: 7 → 8 + SO-05 (Wezwanie do Trybunału): gold 2 → 4 + SO-05 (Wezwanie do Trybunału): koszt 0→0, herezja 3→4 + SO-05 (Wezwanie do Trybunału): target_heresy 3 → 1 | 94.5 → 🟢 ** 97.0** (`⬆️ +2.5`) | `[95.4, 98.6]` | 0.0% | 4.9% | 🟢 ZYSK |
| #18 | `L3_CAA-01_COST_MINUS2__L3_CAA-01_HERESY_PLUS1__L3_CAA-01_TARGET_HERESY_MINUS1__L3_CAA-11_C2_G2` | CAA-01 (Przejście Podziemiami): cost 2 → 0 + CAA-01 (Przejście Podziemiami): heresy 2 → 3 + CAA-01 (Przejście Podziemiami): target_heresy 1 → 0 + CAA-11 (Nocna Zmiana Warty): koszt 1→2, złoto 1→2 | 94.5 → 🟢 ** 97.0** (`⬆️ +2.5`) | `[95.4, 98.6]` | 0.0% | 4.9% | 🟢 ZYSK |
| #19 | `L1_OBSERVED_MINUS1__L1_OBSERVED_PLUS1__L2_KT_FRAGS_MINUS1__L3_GC-05_TARGET_HERESY_PLUS2` | GC-05 (Fałszywy Świadek): target_heresy 0 → 2 + Kabała Fragmenty: 3 → 2 + Próg Obserwowanej: 3 → 2 + Próg Obserwowanej: 3 → 4 | 94.5 → 🟢 ** 97.0** (`⬆️ +2.5`) | `[95.4, 98.6]` | 0.0% | 4.9% | 🟢 ZYSK |
| #20 | `L1_START_GOLD_PLUS1__L3_SO-05_GOLD_PLUS1__L3_SO-05_TARGET_HERESY_PLUS2` | SO-05 (Wezwanie do Trybunału): gold 2 → 3 + SO-05 (Wezwanie do Trybunału): target_heresy 3 → 5 + Złoto startowe: 4zł → 5zł | 94.5 → 🟢 ** 97.0** (`⬆️ +2.5`) | `[95.4, 98.6]` | 0.0% | 4.9% | 🟢 ZYSK |
| #21 | `L3_GC-05_GOLD_SET3__L3_SO-05_C0_G3__L3_SO-05_TARGET_HERESY_MINUS1` | GC-05 (Fałszywy Świadek): dodaj gold = 3 + SO-05 (Wezwanie do Trybunału): koszt 0→0, złoto 2→3 + SO-05 (Wezwanie do Trybunału): target_heresy 3 → 2 | 94.5 → 🟢 ** 97.0** (`⬆️ +2.5`) | `[95.4, 98.6]` | 0.0% | 4.9% | 🟢 ZYSK |
| #22 | `L1_THRESHOLD_PLUS1__L3_CAA-01_HERESY_MINUS1__L4_SEA_ROUTE_ERA_PLUS1__L4_SEA_ROUTE_ERA_PLUS2` | CAA-01 (Przejście Podziemiami): heresy 2 → 1 + Próg Oskarżenia: 7 → 8 + Szlak Morski: Era 4 → 5 + Szlak Morski: Era 4 → 6 | 94.5 → 🟢 ** 97.0** (`⬆️ +2.5`) | `[95.4, 98.6]` | 0.0% | 4.9% | 🟢 ZYSK |
| #23 | `L3_GC-05_GOLD_SET3__L3_GC-05_HERESY_PLUS2__L3_SO-05_C0_H4` | GC-05 (Fałszywy Świadek): dodaj gold = 3 + GC-05 (Fałszywy Świadek): heresy 0 → 2 + SO-05 (Wezwanie do Trybunału): koszt 0→0, herezja 3→4 | 94.5 → 🟢 ** 97.0** (`⬆️ +2.5`) | `[95.4, 98.6]` | 0.0% | 4.9% | 🟢 ZYSK |
| #24 | `L3_CAA-01_C3_H1__L3_CAA-01_GOLD_PLUS1__L3_CAA-01_TARGET_HERESY_MINUS1__L3_GC-05_COST_PLUS2` | CAA-01 (Przejście Podziemiami): gold 0 → 1 + CAA-01 (Przejście Podziemiami): koszt 2→3, herezja 2→1 + CAA-01 (Przejście Podziemiami): target_heresy 1 → 0 + GC-05 (Fałszywy Świadek): cost 1 → 3 | 94.5 → 🟢 ** 96.9** (`⬆️ +2.4`) | `[95.3, 98.5]` | 0.0% | 4.9% | 🟢 ZYSK |
| #25 | `L1_AUTODAFE_COOLDOWN_MINUS1__L1_AUTODAFE_COOLDOWN_PLUS1__L1_START_GOLD_MINUS1__L3_CAA-08_G2_H0` | CAA-08 (Kaptur Nocy): złoto 3→2, herezja 0→0 + Cooldown Autodafé: 3 → 2 Ery + Cooldown Autodafé: 3 → 4 Ery + Złoto startowe: 4zł → 3zł | 94.5 → 🟢 ** 96.9** (`⬆️ +2.4`) | `[95.3, 98.5]` | 0.0% | 5.0% | 🟢 ZYSK |
| #26 | `L1_AUTODAFE_COOLDOWN_MINUS1__L1_AUTODAFE_COOLDOWN_PLUS1__L1_START_GOLD_MINUS1__L3_GC-08_HERESY_PLUS1` | Cooldown Autodafé: 3 → 2 Ery + Cooldown Autodafé: 3 → 4 Ery + GC-08 (Zatrute Złoto): heresy 2 → 3 + Złoto startowe: 4zł → 3zł | 94.5 → 🟢 ** 96.9** (`⬆️ +2.4`) | `[95.3, 98.5]` | 0.0% | 4.9% | 🟢 ZYSK |
| #27 | `L3_CAA-09_C1_G1__L3_GC-05_G0_H1__L3_GC-05_TARGET_HERESY_SET1` | CAA-09 (Kurier Relikwii): koszt 0→1, złoto 0→1 + GC-05 (Fałszywy Świadek): dodaj target_heresy = 1 + GC-05 (Fałszywy Świadek): złoto 0→0, herezja 0→1 | 94.5 → 🟢 ** 96.9** (`⬆️ +2.4`) | `[95.3, 98.5]` | 0.0% | 4.9% | 🟢 ZYSK |
| #28 | `L3_SO-05_C0_H4__L3_SO-05_GOLD_PLUS2__L3_SO-05_TARGET_HERESY_MINUS2__L4_SEA_ROUTE_ERA_MINUS1` | SO-05 (Wezwanie do Trybunału): gold 2 → 4 + SO-05 (Wezwanie do Trybunału): koszt 0→0, herezja 3→4 + SO-05 (Wezwanie do Trybunału): target_heresy 3 → 1 + Szlak Morski: Era 4 → 3 | 94.5 → 🟢 ** 96.9** (`⬆️ +2.4`) | `[95.3, 98.5]` | 0.0% | 4.9% | 🟢 ZYSK |
| #29 | `L3_SO-05_C0_H4__L3_SO-05_GOLD_PLUS2__L3_SO-05_TARGET_HERESY_MINUS2__L3_SO-07_HERESY_SET1` | SO-05 (Wezwanie do Trybunału): gold 2 → 4 + SO-05 (Wezwanie do Trybunału): koszt 0→0, herezja 3→4 + SO-05 (Wezwanie do Trybunału): target_heresy 3 → 1 + SO-07 (Przesłuchanie Oficjum): dodaj heresy = 1 | 94.5 → 🟢 ** 96.9** (`⬆️ +2.4`) | `[95.3, 98.5]` | 0.0% | 5.0% | 🟢 ZYSK |
| #30 | `L3_GC-05_G0_H1__L3_GC-05_TARGET_HERESY_SET1__L3_SO-05_G1_H4` | GC-05 (Fałszywy Świadek): dodaj target_heresy = 1 + GC-05 (Fałszywy Świadek): złoto 0→0, herezja 0→1 + SO-05 (Wezwanie do Trybunału): złoto 2→1, herezja 3→4 | 94.5 → 🟢 ** 96.9** (`⬆️ +2.4`) | `[95.3, 98.5]` | 0.0% | 4.9% | 🟢 ZYSK |