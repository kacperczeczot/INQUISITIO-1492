# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.13 (Iteracja #3, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.12` (4P: `77.8 pkt`) → **Nowa Wersja:** `v1.0-alpha.13` (4P: `78.1 pkt`)
**Data:** 2026-08-20 23:11 | **Czas Trwania Iteracji:** 782.1s | **Zysk 4P:** `+0.3 pkt` | **Zysk Global:** `+0.2 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_GC-07_COST_MINUS1` — **GC-07 (Skrytobójstwo): cost 1 → 0**
- **Opis Modyfikacji:** Karta `gc-07` (Skrytobójstwo): `cost` → `0`
- **Wynik Kanonu 4P Balance:** 77.8 → 🟡 ** 78.1** (`⬆️ +0.3`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 67.2 pkt
  - `4p-no-cienie`: 91.5 → 92.0 (`⬆️ +0.5`) pkt
  - `4p-no-kabala`: 61.1 → 61.0 (`-0.1`) pkt
  - `4p-no-korona`: 95.7 pkt
  - `4p-no-oficjum`: 73.7 → 74.7 (`⬆️ +1.0`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 22.6 pkt
- **Tryb 4-osobowy (4p Avg):** 80.3 → 80.5 (`⬆️ +0.2`) pkt
- **Tryb 5-osobowy (5p Avg):** 33.3 → 33.6 (`⬆️ +0.3`) pkt
- **Global Game Balance Score:** 45.4 → 🔴 ** 45.6** (`⬆️ +0.2`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.20 Er`
  - **Deadlocki (Limit Er):** `0.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.5%` (norma: <30%)
  - **Autodafé / partię:** `2.21`
  - **Oskarżenia / partię:** `4.25`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-07_COST_MINUS1` | GC-07 (Skrytobójstwo): cost 1 → 0 | 77.8 → 🟡 ** 78.1** (`⬆️ +0.3`) | 0.3% | 1.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KB-10_TARGET_HERESY_MINUS1` | KB-10 (Pieczęć Korony): target_heresy 1 → 0 | 77.8 → 🟡 ** 78.1** (`⬆️ +0.3`) | 0.3% | 1.5% | 🟢 ZYSK |
| #3 | `L3_SO-03_HERESY_PLUS1` | SO-03 (Podejrzenie): heresy 0 → 1 | 77.8 → 🟡 ** 78.0** (`⬆️ +0.2`) | 0.3% | 1.5% | 🟢 ZYSK |
| #4 | `L3_CAA-08_COST_PLUS1` | CAA-08 (Kaptur Nocy): cost 1 → 2 | 77.8 → 🟡 ** 78.0** (`⬆️ +0.2`) | 0.3% | 1.5% | 🟢 ZYSK |
| #5 | `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 🟡 ** 77.8** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_SO-09_COST_PLUS1` | SO-09 (Świadek Koronny): cost 2 → 3 | 🟡 ** 77.8** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_SO-12_COST_PLUS1` | SO-12 (Straż Trybunalska): cost 1 → 2 | 🟡 ** 77.8** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_SO-02_GOLD_MINUS1` | SO-02 (Skarbiec Trybunału): gold 3 → 2 | 77.8 → 🟡 ** 77.7** (`-0.1`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_GC-04_GOLD_PLUS1` | GC-04 (Informator): gold 0 → 1 | 77.8 → 🟡 ** 77.7** (`-0.1`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 77.8 → 🟡 ** 77.6** (`-0.2`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 0 → 1 | 77.8 → 🟡 ** 77.6** (`-0.2`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 2 → 3 | 77.8 → 🟡 ** 77.3** (`-0.5`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |