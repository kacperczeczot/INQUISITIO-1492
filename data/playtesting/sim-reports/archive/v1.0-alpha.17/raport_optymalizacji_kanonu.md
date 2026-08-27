[Strona główna](../../../../../README.md) > [v1.0-alpha.17](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.17 (Iteracja #7, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.16` (4P: `78.8 pkt`) → **Nowa Wersja:** `v1.0-alpha.17` (4P: `79.4 pkt`)
**Data:** 2026-08-21 00:04 | **Czas Trwania Iteracji:** 788.7s | **Zysk 4P:** `+0.6 pkt` | **Zysk Global:** `-0.3 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_GC-02_GOLD_PLUS1` — **GC-02 (Czarny Rynek): gold 3 → 4**
- **Opis Modyfikacji:** Karta `gc-02` (Czarny Rynek): `gold` → `4`
- **Wynik Kanonu 4P Balance:** 78.8 → 🟡 ** 79.4** (`⬆️ +0.6`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 67.2 pkt
  - `4p-no-cienie`: 94.6 → 92.9 (`-1.7`) pkt
  - `4p-no-kabala`: 60.2 → 61.3 (`⬆️ +1.1`) pkt
  - `4p-no-korona`: 95.9 → 96.7 (`⬆️ +0.8`) pkt
  - `4p-no-oficjum`: 76.2 → 78.8 (`⬆️ +2.6`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 23.1 → 23.9 (`⬆️ +0.8`) pkt
- **Tryb 4-osobowy (4p Avg):** 81.1 → 81.2 (`⬆️ +0.1`) pkt
- **Tryb 5-osobowy (5p Avg):** 34.3 → 32.5 (`-1.8`) pkt
- **Global Game Balance Score:** 46.2 → 🔴 ** 45.9** (`-0.3`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.24 Er`
  - **Deadlocki (Limit Er):** `0.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.5%` (norma: <30%)
  - **Autodafé / partię:** `2.22`
  - **Oskarżenia / partię:** `4.21`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-02_GOLD_PLUS1` | GC-02 (Czarny Rynek): gold 3 → 4 | 78.8 → 🟡 ** 79.4** (`⬆️ +0.6`) | 0.3% | 1.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_CAA-08_COST_PLUS1` | CAA-08 (Kaptur Nocy): cost 1 → 2 | 78.8 → 🟡 ** 78.9** (`⬆️ +0.1`) | 0.3% | 1.5% | 🟢 ZYSK |
| #3 | `L3_SO-09_COST_PLUS1` | SO-09 (Świadek Koronny): cost 2 → 3 | 78.8 → 🟡 ** 78.9** (`⬆️ +0.1`) | 0.3% | 1.5% | 🟢 ZYSK |
| #4 | `L3_SO-02_GOLD_PLUS1` | SO-02 (Skarbiec Trybunału): gold 3 → 4 | 🟡 ** 78.8** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #5 | `L3_SO-12_COST_PLUS1` | SO-12 (Straż Trybunalska): cost 1 → 2 | 🟡 ** 78.8** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_CAA-03_GOLD_PLUS1` | CAA-03 (Cień na Rynku): gold 2 → 3 | 🟡 ** 78.8** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_SO-03_COST_PLUS1` | SO-03 (Podejrzenie): cost 2 → 3 | 78.8 → 🟡 ** 78.7** (`-0.1`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_SO-02_GOLD_MINUS1` | SO-02 (Skarbiec Trybunału): gold 3 → 2 | 78.8 → 🟡 ** 78.7** (`-0.1`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 78.8 → 🟡 ** 78.6** (`-0.2`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_SO-06_TARGET_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): target_heresy 0 → 1 | 78.8 → 🟡 ** 78.6** (`-0.2`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_GC-04_GOLD_PLUS1` | GC-04 (Informator): gold 0 → 1 | 78.8 → 🟡 ** 78.6** (`-0.2`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 78.8 → 🟡 ** 78.5** (`-0.3`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |