[Strona główna](../../../../../README.md) > [v1.0-alpha.75](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.75 (Iteracja #9, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.74` (4P: `79.2 pkt`) → **Nowa Wersja:** `v1.0-alpha.75` (4P: `83.5 pkt`)
**Data:** 2026-08-24 15:27 | **Czas Trwania Iteracji:** 2243.8s | **Zysk 4P:** `+4.3 pkt` | **Zysk Global:** `-0.4 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_CAA-11_TARGET_HERESY_SET2` — **CAA-11 (Nocna Zmiana Warty): dodaj target_heresy = 2**
- **Opis Modyfikacji:** Karta `caa-11` (Nocna Zmiana Warty): `target_heresy` → `2`
- **Wynik Kanonu 4P Balance:** 79.2 → 🟡 ** 83.5** (`⬆️ +4.3`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 84.7 → 95.1 (`⬆️ +10.4`) pkt
  - `4p-no-cienie`: 72.5 pkt
  - `4p-no-kabala`: 89.6 → 96.4 (`⬆️ +6.8`) pkt
  - `4p-no-korona`: 87.5 → 84.4 (`-3.1`) pkt
  - `4p-no-oficjum`: 61.7 → 69.3 (`⬆️ +7.6`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 28.5 → 28.1 (`-0.4`) pkt
- **Tryb 4-osobowy (4p Avg):** 69.2 → 76.6 (`⬆️ +7.4`) pkt
- **Tryb 5-osobowy (5p Avg):** 25.8 → 17.8 (`-8.0`) pkt
- **Global Game Balance Score:** 41.2 → 🔴 ** 40.8** (`-0.4`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.74 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.2%` (norma: <30%)
  - **Autodafé / partię:** `1.51`
  - **Oskarżenia / partię:** `6.89`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-11_TARGET_HERESY_SET2` | CAA-11 (Nocna Zmiana Warty): dodaj target_heresy = 2 | 79.2 → 🟡 ** 83.5** (`⬆️ +4.3`) | 0.0% | 4.2% | 🌟 ZWYCIĘZCA |
| #2 | `L3_CAA-03_TARGET_HERESY_PLUS1` | CAA-03 (Cień na Rynku): target_heresy 0 → 1 | 79.2 → 🟡 ** 81.5** (`⬆️ +2.3`) | 0.0% | 4.2% | 🟢 ZYSK |
| #3 | `L3_CAA-03_TARGET_HERESY_SET1` | CAA-03 (Cień na Rynku): dodaj target_heresy = 1 | 79.2 → 🟡 ** 81.5** (`⬆️ +2.3`) | 0.0% | 4.2% | 🟢 ZYSK |
| #4 | `L3_CAA-04_TARGET_HERESY_MINUS1` | CAA-04 (Fałszywy Trop): target_heresy 1 → 0 | 79.2 → 🟡 ** 81.3** (`⬆️ +2.1`) | 0.0% | 4.2% | 🟢 ZYSK |
| #5 | `L3_KB-01_COST_MINUS1` | KB-01 (Rozkaz Dworu): cost 1 → 0 | 79.2 → 🟡 ** 81.0** (`⬆️ +1.8`) | 0.0% | 3.4% | 🟢 ZYSK |
| #6 | `L3_SO-01_TARGET_HERESY_PLUS1` | SO-01 (Patrol Familiariuszy): target_heresy 0 → 1 | 79.2 → 🟡 ** 81.0** (`⬆️ +1.8`) | 0.0% | 4.1% | 🟢 ZYSK |
| #7 | `L3_CAA-06_TARGET_HERESY_MINUS1` | CAA-06 (Ucieczka z Lochów): target_heresy 2 → 1 | 79.2 → 🟡 ** 80.6** (`⬆️ +1.4`) | 0.0% | 4.2% | 🟢 ZYSK |
| #8 | `L3_GC-07_HERESY_SET1` | GC-07 (Skrytobójstwo): dodaj heresy = 1 | 79.2 → 🟡 ** 80.1** (`⬆️ +0.9`) | 0.0% | 4.2% | 🟢 ZYSK |
| #9 | `L3_GC-07_HERESY_PLUS1` | GC-07 (Skrytobójstwo): heresy 0 → 1 | 79.2 → 🟡 ** 80.1** (`⬆️ +0.9`) | 0.0% | 4.2% | 🟢 ZYSK |
| #10 | `L3_KB-09_TARGET_HERESY_PLUS1` | KB-09 (Dekret Królewski): target_heresy 0 → 1 | 79.2 → 🟡 ** 78.3** (`-0.9`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_KB-02_COST_PLUS1` | KB-02 (Pobór Podatków): cost 1 → 2 | 79.2 → 🟡 ** 77.9** (`-1.3`) | 0.0% | 5.2% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 79.2 → 🟡 ** 76.2** (`-3.0`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_KT-11_COST_PLUS1` | KT-11 (Medytacja Sefirot): cost 2 → 3 | 79.2 → 🟡 ** 78.2** (`-1.0`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_CAA-04_GOLD_MINUS1` | CAA-04 (Fałszywy Trop): gold 3 → 2 | 79.2 → 🟡 ** 81.9** (`⬆️ +2.7`) | 0.0% | 4.2% | 🟢 ZYSK |
| #15 | `L3_CAA-04_COST_PLUS1` | CAA-04 (Fałszywy Trop): cost 0 → 1 | 79.2 → 🟡 ** 81.9** (`⬆️ +2.7`) | 0.0% | 4.2% | 🟢 ZYSK |
| #16 | `L3_CAA-10_GOLD_SET2` | CAA-10 (Echo Alhambry): dodaj gold = 2 | 🟡 ** 79.2** | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_CAA-10_COST_MINUS1` | CAA-10 (Echo Alhambry): cost 3 → 2 | 79.2 → 🟡 ** 78.4** (`-0.8`) | 0.0% | 4.2% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_CAA-10_TARGET_HERESY_PLUS1` | CAA-10 (Echo Alhambry): target_heresy 0 → 1 | 79.2 → 🟡 ** 78.8** (`-0.4`) | 0.0% | 4.1% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_CAA-10_TARGET_HERESY_SET1` | CAA-10 (Echo Alhambry): dodaj target_heresy = 1 | 79.2 → 🟡 ** 78.8** (`-0.4`) | 0.0% | 4.1% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_CAA-10_TARGET_HERESY_SET2` | CAA-10 (Echo Alhambry): dodaj target_heresy = 2 | 79.2 → 🟡 ** 77.4** (`-1.8`) | 0.0% | 4.1% | ⚪ STRATA/NEUTRALNY |