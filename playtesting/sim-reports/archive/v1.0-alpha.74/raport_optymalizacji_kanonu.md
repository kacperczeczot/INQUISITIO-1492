# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.74 (Iteracja #8, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.73` (4P: `78.3 pkt`) → **Nowa Wersja:** `v1.0-alpha.74` (4P: `81.1 pkt`)
**Data:** 2026-08-24 14:49 | **Czas Trwania Iteracji:** 6351.6s | **Zysk 4P:** `+2.8 pkt` | **Zysk Global:** `-6.3 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_SO-12_TARGET_HERESY_SET1` — **SO-12 (Straż Trybunalska): dodaj target_heresy = 1**
- **Opis Modyfikacji:** Karta `so-12` (Straż Trybunalska): `target_heresy` → `1`
- **Wynik Kanonu 4P Balance:** 78.3 → 🟡 ** 81.1** (`⬆️ +2.8`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 81.5 → 94.0 (`⬆️ +12.5`) pkt
  - `4p-no-cienie`: 75.7 → 69.2 (`-6.5`) pkt
  - `4p-no-kabala`: 80.9 → 89.3 (`⬆️ +8.4`) pkt
  - `4p-no-korona`: 91.8 pkt
  - `4p-no-oficjum`: 61.4 pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 29.9 → 28.5 (`-1.4`) pkt
- **Tryb 4-osobowy (4p Avg):** 72.2 → 69.2 (`-3.0`) pkt
- **Tryb 5-osobowy (5p Avg):** 40.5 → 25.8 (`-14.7`) pkt
- **Global Game Balance Score:** 47.5 → 🔴 ** 41.2** (`-6.3`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.77 Er`
  - **Deadlocki (Limit Er):** `0.0%` (norma: <5%)
  - **Pas Biedy (Złoto):** `4.2%` (norma: <30%)
  - **Autodafé / partię:** `1.53`
  - **Oskarżenia / partię:** `6.81`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-12_TARGET_HERESY_SET1` | SO-12 (Straż Trybunalska): dodaj target_heresy = 1 | 78.3 → 🟡 ** 81.1** (`⬆️ +2.8`) | 0.0% | 4.2% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-12_TARGET_HERESY_PLUS1` | SO-12 (Straż Trybunalska): target_heresy 0 → 1 | 78.3 → 🟡 ** 81.1** (`⬆️ +2.8`) | 0.0% | 4.2% | 🟢 ZYSK |
| #3 | `L3_CAA-11_GOLD_MINUS1` | CAA-11 (Nocna Zmiana Warty): gold 3 → 2 | 78.3 → 🟡 ** 80.5** (`⬆️ +2.2`) | 0.0% | 4.4% | 🟢 ZYSK |
| #4 | `L3_CAA-11_COST_PLUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 2 | 78.3 → 🟡 ** 80.3** (`⬆️ +2.0`) | 0.0% | 4.4% | 🟢 ZYSK |
| #5 | `L3_CAA-01_TARGET_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): target_heresy 1 → 2 | 78.3 → 🟡 ** 80.2** (`⬆️ +1.9`) | 0.0% | 4.3% | 🟢 ZYSK |
| #6 | `L3_KT-12_GOLD_PLUS1` | KT-12 (Strażnik Archiwum): gold 0 → 1 | 78.3 → 🟡 ** 80.0** (`⬆️ +1.7`) | 0.0% | 4.4% | 🟢 ZYSK |
| #7 | `L3_KT-12_GOLD_SET1` | KT-12 (Strażnik Archiwum): dodaj gold = 1 | 78.3 → 🟡 ** 80.0** (`⬆️ +1.7`) | 0.0% | 4.4% | 🟢 ZYSK |
| #8 | `L3_CAA-11_HERESY_SET2` | CAA-11 (Nocna Zmiana Warty): dodaj heresy = 2 | 78.3 → 🟡 ** 80.0** (`⬆️ +1.7`) | 0.0% | 4.3% | 🟢 ZYSK |
| #9 | `L3_CAA-04_TARGET_HERESY_PLUS1` | CAA-04 (Fałszywy Trop): target_heresy 1 → 2 | 78.3 → 🟡 ** 79.9** (`⬆️ +1.6`) | 0.0% | 4.4% | 🟢 ZYSK |
| #10 | `L3_GC-07_COST_PLUS1` | GC-07 (Skrytobójstwo): cost 0 → 1 | 78.3 → 🟡 ** 79.7** (`⬆️ +1.4`) | 0.0% | 4.4% | 🟢 ZYSK |
| #11 | `L3_SO-02_TARGET_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): target_heresy 1 → 2 | 78.3 → 🟡 ** 79.3** (`⬆️ +1.0`) | 0.0% | 4.1% | 🟢 ZYSK |
| #12 | `L3_SO-11_TARGET_HERESY_PLUS1` | SO-11 (Dekret Czystości Wiary): target_heresy 1 → 2 | 78.3 → 🟡 ** 79.2** (`⬆️ +0.9`) | 0.0% | 4.2% | 🟢 ZYSK |
| #13 | `L3_GC-03_TARGET_HERESY_MINUS1` | GC-03 (Podrzucenie Księgi): target_heresy 1 → 0 | 78.3 → 🟡 ** 79.0** (`⬆️ +0.7`) | 0.0% | 4.4% | 🟢 ZYSK |
| #14 | `L3_SO-09_COST_MINUS1` | SO-09 (Świadek Koronny): cost 1 → 0 | 78.3 → 🟡 ** 78.5** (`⬆️ +0.2`) | 0.0% | 4.0% | 🟢 ZYSK |
| #15 | `L3_SO-03_HERESY_PLUS1` | SO-03 (Podejrzenie): heresy 3 → 4 | 78.3 → 🟡 ** 78.4** (`⬆️ +0.1`) | 0.0% | 4.4% | 🟢 ZYSK |
| #16 | `L3_CAA-12_HERESY_PLUS1` | CAA-12 (Skrytka w Murach): heresy 0 → 1 | 78.3 → 🟡 ** 78.4** (`⬆️ +0.1`) | 0.0% | 4.3% | 🟢 ZYSK |
| #17 | `L3_SO-11_COST_MINUS1` | SO-11 (Dekret Czystości Wiary): cost 1 → 0 | 🟡 ** 78.3** | 0.0% | 3.9% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_CAA-09_HERESY_SET1` | CAA-09 (Kurier Relikwii): dodaj heresy = 1 | 78.3 → 🟡 ** 76.7** (`-1.6`) | 0.0% | 4.3% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_CAA-09_HERESY_PLUS1` | CAA-09 (Kurier Relikwii): heresy 0 → 1 | 78.3 → 🟡 ** 76.7** (`-1.6`) | 0.0% | 4.3% | ⚪ STRATA/NEUTRALNY |
| #20 | `L4_SEA_ROUTE_ERA_MINUS1` | Szlak Morski: Era 4 → 3 | 78.3 → 🟡 ** 75.8** (`-2.5`) | 0.0% | 4.3% | ⚪ STRATA/NEUTRALNY |