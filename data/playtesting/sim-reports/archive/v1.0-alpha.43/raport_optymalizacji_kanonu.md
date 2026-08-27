[Strona główna](../../../../../README.md) > [v1.0-alpha.43](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.43 (Iteracja #1, Faza 3D)

**Wersja Poprzednia:** `v1.0-alpha.42` (4P: `74.4 pkt`) → **Nowa Wersja:** `v1.0-alpha.43` (4P: `76.2 pkt`)
**Data:** 2026-08-23 09:05 | **Czas Trwania Iteracji:** 883.3s | **Zysk 4P:** `+1.8 pkt` | **Zysk Global:** `0.0 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (3D):** `L3_GC-01_COST_MINUS1__L3_CAA-08_GOLD_PLUS1__L3_CAA-01_TARGET_HERESY_PLUS1` — **GC-01 (Przekupiony Strażnik): cost 2 → 1 + CAA-08 (Kaptur Nocy): gold 0 → 1 + CAA-01 (Przejście Podziemiami): target_heresy 0 → 1**
- **Opis Modyfikacji:** Karta `gc-01` (Przekupiony Strażnik): `cost` → `1` + Karta `caa-08` (Kaptur Nocy): `gold` → `1` + Karta `caa-01` (Przejście Podziemiami): `target_heresy` → `1`
- **Wynik Kanonu 4P Balance:** 74.4 → 🟡 ** 76.2** (`⬆️ +1.8`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 64.8 → 67.8 (`⬆️ +3.0`) pkt
  - `4p-no-cienie`: 80.5 → 79.1 (`-1.4`) pkt
  - `4p-no-kabala`: 72.6 → 75.4 (`⬆️ +2.8`) pkt
  - `4p-no-korona`: 76.3 → 81.1 (`⬆️ +4.8`) pkt
  - `4p-no-oficjum`: 77.9 → 77.6 (`-0.3`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 25.5 → 22.6 (`-2.9`) pkt
- **Tryb 4-osobowy (4p Avg):** 51.3 → 54.0 (`⬆️ +2.7`) pkt
- **Tryb 5-osobowy (5p Avg):** 7.5 → 7.6 (`⬆️ +0.1`) pkt
- **Global Game Balance Score:** 🔴 ** 28.1** pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `4.78 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `3.5%` (norma: <30%)
  - **Autodafé / partię:** `1.57`
  - **Oskarżenia / partię:** `4.57`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_KB-10_TARGET_HERESY_SET2__L1_THRESHOLD_MINUS1__L3_CAA-04_TARGET_HERESY_PLUS1` | KB-10 (Pieczęć Korony): dodaj target_heresy = 2 + Próg Oskarżenia: 7 → 6 + CAA-04 (Fałszywy Trop): target_heresy 1 → 2 | 74.4 → 🟠 ** 71.4** (`-3.0`) | 0.0% | 3.2% | ⚪ STRATA/NEUTRALNY |
| #2 | `L3_KT-10_COST_PLUS1__L3_CAA-09_TARGET_HERESY_PLUS1__L3_CAA-06_COST_PLUS1` | KT-10 (Pieczęć Salomona): cost 2 → 3 + CAA-09 (Kurier Relikwii): target_heresy 0 → 1 + CAA-06 (Ucieczka z Lochów): cost 0 → 1 | 74.4 → 🟠 ** 74.6** (`⬆️ +0.2`) | 0.0% | 3.6% | 🟢 ZYSK |
| #3 | `L3_GC-01_COST_MINUS1__L3_CAA-08_GOLD_PLUS1__L3_CAA-01_TARGET_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): cost 2 → 1 + CAA-08 (Kaptur Nocy): gold 0 → 1 + CAA-01 (Przejście Podziemiami): target_heresy 0 → 1 | 74.4 → 🟡 ** 76.2** (`⬆️ +1.8`) | 0.0% | 3.5% | 🌟 ZWYCIĘZCA |
| #4 | `L3_GC-01_COST_MINUS1__L3_CAA-08_COST_MINUS1__L3_CAA-01_TARGET_HERESY_SET1` | GC-01 (Przekupiony Strażnik): cost 2 → 1 + CAA-08 (Kaptur Nocy): cost 1 → 0 + CAA-01 (Przejście Podziemiami): dodaj target_heresy = 1 | 74.4 → 🟡 ** 76.2** (`⬆️ +1.8`) | 0.0% | 3.5% | 🟢 ZYSK |
| #5 | `L3_GC-01_COST_MINUS1__L3_CAA-08_GOLD_PLUS1__L3_CAA-01_TARGET_HERESY_SET1` | GC-01 (Przekupiony Strażnik): cost 2 → 1 + CAA-08 (Kaptur Nocy): gold 0 → 1 + CAA-01 (Przejście Podziemiami): dodaj target_heresy = 1 | 74.4 → 🟡 ** 76.2** (`⬆️ +1.8`) | 0.0% | 3.5% | 🟢 ZYSK |
| #6 | `L3_GC-01_COST_MINUS1__L3_CAA-08_COST_MINUS1__L3_CAA-01_TARGET_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): cost 2 → 1 + CAA-08 (Kaptur Nocy): cost 1 → 0 + CAA-01 (Przejście Podziemiami): target_heresy 0 → 1 | 74.4 → 🟡 ** 76.2** (`⬆️ +1.8`) | 0.0% | 3.5% | 🟢 ZYSK |
| #7 | `L3_KT-10_COST_PLUS1__L3_CAA-09_TARGET_HERESY_PLUS1__L3_CAA-02_GOLD_PLUS1` | KT-10 (Pieczęć Salomona): cost 2 → 3 + CAA-09 (Kurier Relikwii): target_heresy 0 → 1 + CAA-02 (Złoto z Kryjówki): gold 2 → 3 | 74.4 → 🟡 ** 75.3** (`⬆️ +0.9`) | 0.0% | 3.6% | 🟢 ZYSK |
| #8 | `L3_CAA-03_HERESY_PLUS1__L3_GC-03_GOLD_SET2__L3_GC-06_COST_PLUS1` | CAA-03 (Cień na Rynku): heresy 1 → 2 + GC-03 (Podrzucenie Księgi): dodaj gold = 2 + GC-06 (Szantaż): cost 2 → 3 | 74.4 → 🟠 ** 72.5** (`-1.9`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_CAA-03_HERESY_PLUS1__L3_GC-03_GOLD_SET2__L3_GC-01_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 2 + GC-03 (Podrzucenie Księgi): dodaj gold = 2 + GC-01 (Przekupiony Strażnik): heresy 1 → 0 | 74.4 → 🟡 ** 75.8** (`⬆️ +1.4`) | 0.0% | 3.5% | 🟢 ZYSK |
| #10 | `L3_CAA-03_HERESY_PLUS1__L3_GC-03_GOLD_SET3__L3_GC-08_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 2 + GC-03 (Podrzucenie Księgi): dodaj gold = 3 + GC-08 (Zatrute Złoto): heresy 1 → 0 | 74.4 → 🟡 ** 76.2** (`⬆️ +1.8`) | 0.0% | 3.5% | 🟢 ZYSK |
| #11 | `L3_GC-01_COST_MINUS1__L3_CAA-08_GOLD_PLUS1__L3_CAA-10_COST_MINUS1` | GC-01 (Przekupiony Strażnik): cost 2 → 1 + CAA-08 (Kaptur Nocy): gold 0 → 1 + CAA-10 (Echo Alhambry): cost 1 → 0 | 74.4 → 🟡 ** 76.0** (`⬆️ +1.6`) | 0.0% | 3.5% | 🟢 ZYSK |
| #12 | `L3_GC-01_COST_MINUS1__L3_CAA-08_COST_MINUS1__L3_CAA-10_COST_MINUS1` | GC-01 (Przekupiony Strażnik): cost 2 → 1 + CAA-08 (Kaptur Nocy): cost 1 → 0 + CAA-10 (Echo Alhambry): cost 1 → 0 | 74.4 → 🟡 ** 76.0** (`⬆️ +1.6`) | 0.0% | 3.5% | 🟢 ZYSK |
| #13 | `L3_GC-01_COST_MINUS1__L3_CAA-08_GOLD_PLUS1__L3_CAA-10_GOLD_PLUS1` | GC-01 (Przekupiony Strażnik): cost 2 → 1 + CAA-08 (Kaptur Nocy): gold 0 → 1 + CAA-10 (Echo Alhambry): gold 0 → 1 | 74.4 → 🟡 ** 76.0** (`⬆️ +1.6`) | 0.0% | 3.5% | 🟢 ZYSK |
| #14 | `L3_GC-01_COST_MINUS1__L3_CAA-08_GOLD_PLUS1__L3_CAA-10_GOLD_SET1` | GC-01 (Przekupiony Strażnik): cost 2 → 1 + CAA-08 (Kaptur Nocy): gold 0 → 1 + CAA-10 (Echo Alhambry): dodaj gold = 1 | 74.4 → 🟡 ** 76.0** (`⬆️ +1.6`) | 0.0% | 3.5% | 🟢 ZYSK |
| #15 | `L3_GC-01_COST_MINUS1__L3_CAA-08_GOLD_PLUS1__L3_CAA-10_GOLD_SET2` | GC-01 (Przekupiony Strażnik): cost 2 → 1 + CAA-08 (Kaptur Nocy): gold 0 → 1 + CAA-10 (Echo Alhambry): dodaj gold = 2 | 74.4 → 🟡 ** 76.0** (`⬆️ +1.6`) | 0.0% | 3.5% | 🟢 ZYSK |
| #16 | `L3_GC-01_COST_MINUS1__L3_CAA-08_COST_MINUS1__L3_CAA-10_GOLD_SET2` | GC-01 (Przekupiony Strażnik): cost 2 → 1 + CAA-08 (Kaptur Nocy): cost 1 → 0 + CAA-10 (Echo Alhambry): dodaj gold = 2 | 74.4 → 🟡 ** 76.0** (`⬆️ +1.6`) | 0.0% | 3.5% | 🟢 ZYSK |
| #17 | `L3_CAA-03_HERESY_PLUS1__L3_GC-03_GOLD_SET3__L3_GC-01_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 2 + GC-03 (Podrzucenie Księgi): dodaj gold = 3 + GC-01 (Przekupiony Strażnik): heresy 1 → 0 | 74.4 → 🟡 ** 75.9** (`⬆️ +1.5`) | 0.0% | 3.4% | 🟢 ZYSK |
| #18 | `L3_CAA-03_HERESY_PLUS1__L3_GC-03_GOLD_SET2__L3_GC-01_COST_PLUS1` | CAA-03 (Cień na Rynku): heresy 1 → 2 + GC-03 (Podrzucenie Księgi): dodaj gold = 2 + GC-01 (Przekupiony Strażnik): cost 2 → 3 | 74.4 → 🟡 ** 75.6** (`⬆️ +1.2`) | 0.0% | 3.4% | 🟢 ZYSK |
| #19 | `L3_KT-10_COST_PLUS1__L3_CAA-09_TARGET_HERESY_PLUS1__L3_CAA-04_HERESY_SET2` | KT-10 (Pieczęć Salomona): cost 2 → 3 + CAA-09 (Kurier Relikwii): target_heresy 0 → 1 + CAA-04 (Fałszywy Trop): dodaj heresy = 2 | 74.4 → 🟠 ** 72.5** (`-1.9`) | 0.0% | 3.5% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_KB-07_TARGET_HERESY_PLUS1__L3_CAA-07_TARGET_HERESY_SET2__L3_CAA-07_HERESY_SET2` | KB-07 (Szantaż Pieczęcią): target_heresy 0 → 1 + CAA-07 (Szantaż Bractwa): dodaj target_heresy = 2 + CAA-07 (Szantaż Bractwa): dodaj heresy = 2 | 74.4 → 🟠 ** 69.3** (`-5.1`) | 0.0% | 3.4% | ⚪ STRATA/NEUTRALNY |