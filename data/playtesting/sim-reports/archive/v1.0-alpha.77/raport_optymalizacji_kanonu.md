[Strona główna](../../../../../README.md) > [v1.0-alpha.77](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.77 (Iteracja #11, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.76` (4P: `79.6 pkt`) → **Nowa Wersja:** `v1.0-alpha.77` (4P: `82.4 pkt`)
**Data:** 2026-08-24 17:42 | **Czas Trwania Iteracji:** 4943.2s | **Zysk 4P:** `+2.8 pkt` | **Zysk Global:** `+0.3 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_GC-03_HERESY_SET2` — **GC-03 (Podrzucenie Księgi): dodaj heresy = 2**
- **Opis Modyfikacji:** Karta `gc-03` (Podrzucenie Księgi): `heresy` → `2`
- **Wynik Kanonu 4P Balance:** 79.6 → 🟡 ** 82.4** (`⬆️ +2.8`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 95.0 pkt
  - `4p-no-cienie`: 65.9 → 70.8 (`⬆️ +4.9`) pkt
  - `4p-no-kabala`: 96.6 → 95.1 (`-1.5`) pkt
  - `4p-no-korona`: 82.6 → 86.7 (`⬆️ +4.1`) pkt
  - `4p-no-oficjum`: 57.7 → 64.5 (`⬆️ +6.8`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 28.1 → 30.2 (`⬆️ +2.1`) pkt
- **Tryb 4-osobowy (4p Avg):** 78.7 → 80.9 (`⬆️ +2.2`) pkt
- **Tryb 5-osobowy (5p Avg):** 17.3 → 13.9 (`-3.4`) pkt
- **Global Game Balance Score:** 41.4 → 🔴 ** 41.7** (`⬆️ +0.3`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.75 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.2%` (norma: <30%)
  - **Autodafé / partię:** `1.52`
  - **Oskarżenia / partię:** `6.96`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-03_HERESY_SET2` | GC-03 (Podrzucenie Księgi): dodaj heresy = 2 | 79.6 → 🟡 ** 82.4** (`⬆️ +2.8`) | 0.0% | 4.2% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KT-12_HERESY_MINUS1` | KT-12 (Strażnik Archiwum): heresy 1 → 0 | 79.6 → 🟡 ** 81.9** (`⬆️ +2.3`) | 0.0% | 4.4% | 🟢 ZYSK |
| #3 | `L3_SO-05_TARGET_HERESY_MINUS1` | SO-05 (Wezwanie do Trybunału): target_heresy 1 → 0 | 79.6 → 🟡 ** 81.8** (`⬆️ +2.2`) | 0.0% | 4.3% | 🟢 ZYSK |
| #4 | `L3_GC-03_TARGET_HERESY_MINUS1` | GC-03 (Podrzucenie Księgi): target_heresy 1 → 0 | 79.6 → 🟡 ** 81.2** (`⬆️ +1.6`) | 0.0% | 4.2% | 🟢 ZYSK |
| #5 | `L3_KB-01_HERESY_MINUS1` | KB-01 (Rozkaz Dworu): heresy 1 → 0 | 79.6 → 🟡 ** 80.8** (`⬆️ +1.2`) | 0.0% | 4.6% | 🟢 ZYSK |
| #6 | `L3_GC-01_COST_MINUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 0 | 79.6 → 🟡 ** 80.7** (`⬆️ +1.1`) | 0.0% | 4.2% | 🟢 ZYSK |
| #7 | `L3_GC-06_HERESY_MINUS1` | GC-06 (Szantaż): heresy 1 → 0 | 79.6 → 🟡 ** 80.1** (`⬆️ +0.5`) | 0.0% | 4.3% | 🟢 ZYSK |
| #8 | `L3_GC-07_HERESY_SET2` | GC-07 (Skrytobójstwo): dodaj heresy = 2 | 79.6 → 🟡 ** 80.0** (`⬆️ +0.4`) | 0.0% | 4.1% | 🟢 ZYSK |
| #9 | `L3_GC-01_GOLD_PLUS1` | GC-01 (Przekupiony Strażnik): gold 1 → 2 | 79.6 → 🟡 ** 80.0** (`⬆️ +0.4`) | 0.0% | 4.2% | 🟢 ZYSK |
| #10 | `L3_KB-07_GOLD_SET1` | KB-07 (Szantaż Pieczęcią): dodaj gold = 1 | 79.6 → 🟡 ** 79.9** (`⬆️ +0.3`) | 0.0% | 3.9% | 🟢 ZYSK |
| #11 | `L3_KB-07_GOLD_PLUS1` | KB-07 (Szantaż Pieczęcią): gold 0 → 1 | 79.6 → 🟡 ** 79.9** (`⬆️ +0.3`) | 0.0% | 3.9% | 🟢 ZYSK |
| #12 | `L3_KB-01_COST_PLUS1` | KB-01 (Rozkaz Dworu): cost 1 → 2 | 79.6 → 🟡 ** 79.9** (`⬆️ +0.3`) | 0.0% | 5.1% | 🟢 ZYSK |
| #13 | `L3_CAA-03_TARGET_HERESY_PLUS1` | CAA-03 (Cień na Rynku): target_heresy 0 → 1 | 79.6 → 🟡 ** 79.5** (`-0.1`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_CAA-03_TARGET_HERESY_SET1` | CAA-03 (Cień na Rynku): dodaj target_heresy = 1 | 79.6 → 🟡 ** 79.5** (`-0.1`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_KB-03_GOLD_SET1` | KB-03 (Plotka Dworska): dodaj gold = 1 | 79.6 → 🟡 ** 78.4** (`-1.2`) | 0.0% | 3.9% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_KB-03_GOLD_PLUS1` | KB-03 (Plotka Dworska): gold 0 → 1 | 79.6 → 🟡 ** 78.4** (`-1.2`) | 0.0% | 3.9% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_GC-10_HERESY_PLUS1` | GC-10 (Upadek Domu): heresy 2 → 3 | 79.6 → 🟠 ** 74.9** (`-4.7`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_CAA-06_HERESY_SET1` | CAA-06 (Ucieczka z Lochów): dodaj heresy = 1 | 79.6 → 🟡 ** 75.3** (`-4.3`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_CAA-06_HERESY_PLUS1` | CAA-06 (Ucieczka z Lochów): heresy 0 → 1 | 79.6 → 🟡 ** 75.3** (`-4.3`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_SO-10_HERESY_PLUS1` | SO-10 (Oczyść Miasto): heresy 1 → 2 | 79.6 → 🟡 ** 79.5** (`-0.1`) | 0.0% | 3.9% | ⚪ STRATA/NEUTRALNY |