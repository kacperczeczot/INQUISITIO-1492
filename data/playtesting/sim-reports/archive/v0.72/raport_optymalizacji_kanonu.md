[Strona główna](../../../../../README.md) > [v0.72](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.72 (Iteracja #2, Faza 1D)

**Wersja Poprzednia:** `v0.71` (4P: `88.4 pkt`) → **Nowa Wersja:** `v0.72` (4P: `93.7 pkt`)
**Data:** 2026-08-16 23:11 | **Czas Trwania Iteracji:** 817.0s | **Zysk 4P:** `+5.3 pkt` | **Zysk Global:** `+5.3 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_SO-05_TARGET_HERESY_MINUS1` — **SO-05 (Wezwanie do Trybunału): target_heresy 2 → 1**
- **Opis Modyfikacji:** Karta `so-05` (Wezwanie do Trybunału): `target_heresy` → `1`
- **Wynik Kanonu 4P Score:** 88.4 → 🟢 ** 93.7** (`⬆️ +5.3`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 89.1 → 97.7 (`⬆️ +8.6`) pkt
  - `4p-no-cienie`: 87.6 → 94.0 (`⬆️ +6.4`) pkt
  - `4p-no-kabala`: 87.6 → 92.7 (`⬆️ +5.1`) pkt
  - `4p-no-korona`: 83.8 → 90.3 (`⬆️ +6.5`) pkt
  - `4p-no-oficjum`: 93.8 pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 68.0 → 64.4 (`-3.6`) pkt
- **Tryb 4-osobowy (4p Avg):** 85.7 → 91.2 (`⬆️ +5.5`) pkt
- **Tryb 5-osobowy (5p Avg):** 53.9 → 67.8 (`⬆️ +13.9`) pkt
- **Global Game Balance Score:** 69.2 → 🟠 ** 74.5** (`⬆️ +5.3`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.44 Er`
  - **Deadlocki (Limit Er):** `0.1%` (norma: <5%)
  - **Pas Biedy (Złoto):** `24.0%` (norma: <30%)
  - **Autodafé / partię:** `1.50`
  - **Oskarżenia / partię:** `3.17`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-05_TARGET_HERESY_MINUS1` | SO-05 (Wezwanie do Trybunału): target_heresy 2 → 1 | 88.4 → 🟢 ** 93.7** (`⬆️ +5.3`) | 0.1% | 24.0% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-08_TARGET_HERESY_MINUS1` | SO-08 (Nasłanie Inkwizytora): target_heresy 1 → 0 | 88.4 → 🟢 ** 93.1** (`⬆️ +4.7`) | 0.1% | 24.2% | 🟢 ZYSK |
| #3 | `L3_SO-10_HERESY_MINUS1` | SO-10 (Oczyść Miasto): heresy 2 → 1 | 88.4 → 🟢 ** 92.9** (`⬆️ +4.5`) | 0.1% | 24.0% | 🟢 ZYSK |
| #4 | `L3_CAA-06_HERESY_MINUS1` | CAA-06 (Ucieczka z Lochów): heresy 1 → 0 | 88.4 → 🟢 ** 91.6** (`⬆️ +3.2`) | 0.1% | 23.9% | 🟢 ZYSK |
| #5 | `L3_KT-06_COST_PLUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 3 | 88.4 → 🟢 ** 91.0** (`⬆️ +2.6`) | 0.1% | 23.4% | 🟢 ZYSK |
| #6 | `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 88.4 → 🟢 ** 90.9** (`⬆️ +2.5`) | 0.1% | 24.0% | 🟢 ZYSK |
| #7 | `L3_CAA-04_TARGET_HERESY_MINUS1` | CAA-04 (Fałszywy Trop): target_heresy 1 → 0 | 88.4 → 🟢 ** 90.4** (`⬆️ +2.0`) | 0.1% | 23.9% | 🟢 ZYSK |
| #8 | `L4_SEA_ROUTE_ERA4` | Szlak Morski: Era 6 → Era 4 | 88.4 → 🟡 ** 89.9** (`⬆️ +1.5`) | 0.1% | 23.8% | 🟢 ZYSK |
| #9 | `L3_KT-08_GOLD_PLUS1` | KT-08 (Areszt Wiedzy): gold 0 → 1 | 88.4 → 🟡 ** 89.8** (`⬆️ +1.4`) | 0.1% | 23.9% | 🟢 ZYSK |
| #10 | `L3_KT-02_GOLD_MINUS1` | KT-02 (Transmutacja Złota): gold 2 → 1 | 88.4 → 🟡 ** 89.7** (`⬆️ +1.3`) | 0.1% | 23.9% | 🟢 ZYSK |
| #11 | `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 88.4 → 🟡 ** 89.6** (`⬆️ +1.2`) | 0.1% | 24.1% | 🟢 ZYSK |
| #12 | `L3_SO-01_GOLD_PLUS1` | SO-01 (Patrol Familiariuszy): gold 0 → 1 | 88.4 → 🟡 ** 89.5** (`⬆️ +1.1`) | 0.1% | 23.5% | 🟢 ZYSK |
| #13 | `L3_KT-10_COST_PLUS1` | KT-10 (Pieczęć Salomona): cost 2 → 3 | 88.4 → 🟡 ** 89.4** (`⬆️ +1.0`) | 0.1% | 23.5% | 🟢 ZYSK |
| #14 | `L3_GC-06_HERESY_PLUS1` | GC-06 (Szantaż): heresy 0 → 1 | 88.4 → 🟡 ** 89.2** (`⬆️ +0.8`) | 0.1% | 23.9% | 🟢 ZYSK |
| #15 | `L3_CAA-02_GOLD_MINUS1` | CAA-02 (Złoto z Kryjówki): gold 2 → 1 | 88.4 → 🟡 ** 89.0** (`⬆️ +0.6`) | 0.1% | 23.9% | 🟢 ZYSK |
| #16 | `L3_GC-01_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): heresy 1 → 2 | 88.4 → 🟡 ** 88.9** (`⬆️ +0.5`) | 0.1% | 23.9% | 🟢 ZYSK |
| #17 | `L4_SEA_ROUTE_ERA5` | Szlak Morski: Era 6 → Era 5 | 88.4 → 🟡 ** 88.9** (`⬆️ +0.5`) | 0.1% | 23.8% | 🟢 ZYSK |
| #18 | `L3_KT-02_GOLD_PLUS1` | KT-02 (Transmutacja Złota): gold 2 → 3 | 88.4 → 🟡 ** 88.8** (`⬆️ +0.4`) | 0.1% | 23.9% | 🟢 ZYSK |
| #19 | `L3_GC-03_HERESY_PLUS1` | GC-03 (Podrzucenie Księgi): heresy 0 → 1 | 88.4 → 🟡 ** 88.8** (`⬆️ +0.4`) | 0.1% | 23.9% | 🟢 ZYSK |
| #20 | `L3_KT-05_GOLD_PLUS1` | KT-05 (Wskazówka Cyklu): gold 0 → 1 | 88.4 → 🟡 ** 88.7** (`⬆️ +0.3`) | 0.1% | 23.9% | 🟢 ZYSK |
| #21 | `L3_CAA-02_GOLD_PLUS1` | CAA-02 (Złoto z Kryjówki): gold 2 → 3 | 88.4 → 🟡 ** 88.3** (`-0.1`) | 0.1% | 23.9% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_SO-01_COST_PLUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 2 | 88.4 → 🟡 ** 88.3** (`-0.1`) | 0.0% | 24.5% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_SO-02_COST_MINUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 0 | 88.4 → 🟡 ** 88.2** (`-0.2`) | 0.1% | 23.4% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_CAA-07_GOLD_PLUS1` | CAA-07 (Szantaż Bractwa): gold 0 → 1 | 88.4 → 🟡 ** 87.1** (`-1.3`) | 0.1% | 23.8% | ⚪ STRATA/NEUTRALNY |