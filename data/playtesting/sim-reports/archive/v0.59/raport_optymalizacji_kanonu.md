[Strona główna](../../../../../README.md) > [v0.59](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.59 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v0.58` (4P: `78.8 pkt`) → **Nowa Wersja:** `v0.59` (4P: `84.5 pkt`)
**Data:** 2026-08-16 16:35 | **Czas Trwania Iteracji:** 297.5s | **Zysk 4P:** `+5.7 pkt` | **Zysk Global:** `+3.0 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_GC-03_GOLD_PLUS1` — **GC-03 (Podrzucenie Księgi): gold 0 → 1**
- **Opis Modyfikacji:** Karta `gc-03` (Podrzucenie Księgi): `gold` → `1`
- **Wynik Kanonu 4P Score:** 78.8 → 🟡 ** 84.5** (`⬆️ +5.7`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 82.4 pkt
  - `4p-no-cienie`: 69.8 → 79.3 (`⬆️ +9.5`) pkt
  - `4p-no-kabala`: 77.3 → 83.8 (`⬆️ +6.5`) pkt
  - `4p-no-korona`: 74.6 → 83.8 (`⬆️ +9.2`) pkt
  - `4p-no-oficjum`: 89.9 → 93.0 (`⬆️ +3.1`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 75.8 → 76.8 (`⬆️ +1.0`) pkt
- **Tryb 4-osobowy (4p Avg):** 78.2 → 83.9 (`⬆️ +5.7`) pkt
- **Tryb 5-osobowy (5p Avg):** 47.0 → 49.3 (`⬆️ +2.3`) pkt
- **Global Game Balance Score:** 67.0 → 🟠 ** 70.0** (`⬆️ +3.0`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.46 Er`
  - **Deadlocki (Limit Er):** `0.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `24.6%` (norma: <30%)
  - **Autodafé / partię:** `1.44`
  - **Oskarżenia / partię:** `3.26`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-03_GOLD_PLUS1` | GC-03 (Podrzucenie Księgi): gold 0 → 1 | 78.8 → 🟡 ** 84.5** (`⬆️ +5.7`) | 0.3% | 24.6% | 🌟 ZWYCIĘZCA |
| #2 | `L3_GC-07_COST_PLUS1` | GC-07 (Skrytobójstwo): cost 2 → 3 | 78.8 → 🟡 ** 84.2** (`⬆️ +5.4`) | 0.3% | 25.3% | 🟢 ZYSK |
| #3 | `L3_GC-10_HERESY_MINUS1` | GC-10 (Upadek Domu): heresy 2 → 1 | 78.8 → 🟡 ** 83.7** (`⬆️ +4.9`) | 0.4% | 25.5% | 🟢 ZYSK |
| #4 | `L3_GC-04_HERESY_MINUS1` | GC-04 (Informator): heresy 1 → 0 | 78.8 → 🟡 ** 83.4** (`⬆️ +4.6`) | 0.4% | 25.5% | 🟢 ZYSK |
| #5 | `L3_GC-04_GOLD_PLUS1` | GC-04 (Informator): gold 0 → 1 | 78.8 → 🟡 ** 83.2** (`⬆️ +4.4`) | 0.3% | 24.9% | 🟢 ZYSK |
| #6 | `L3_GC-03_COST_MINUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 0 | 78.8 → 🟡 ** 83.0** (`⬆️ +4.2`) | 0.2% | 24.5% | 🟢 ZYSK |
| #7 | `L3_GC-01_GOLD_PLUS1` | GC-01 (Przekupiony Strażnik): gold 0 → 1 | 78.8 → 🟡 ** 82.7** (`⬆️ +3.9`) | 0.3% | 24.5% | 🟢 ZYSK |
| #8 | `L3_GC-10_GOLD_PLUS1` | GC-10 (Upadek Domu): gold 0 → 1 | 78.8 → 🟡 ** 82.6** (`⬆️ +3.8`) | 0.3% | 24.0% | 🟢 ZYSK |
| #9 | `L3_GC-02_COST_MINUS1` | GC-02 (Czarny Rynek): cost 2 → 1 | 78.8 → 🟡 ** 82.3** (`⬆️ +3.5`) | 0.3% | 23.9% | 🟢 ZYSK |
| #10 | `L3_GC-02_GOLD_PLUS1` | GC-02 (Czarny Rynek): gold 2 → 3 | 78.8 → 🟡 ** 81.9** (`⬆️ +3.1`) | 0.2% | 25.3% | 🟢 ZYSK |
| #11 | `L3_CAA-06_HERESY_MINUS1` | CAA-06 (Ucieczka z Lochów): heresy 1 → 0 | 78.8 → 🟡 ** 81.8** (`⬆️ +3.0`) | 0.4% | 25.6% | 🟢 ZYSK |
| #12 | `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 78.8 → 🟡 ** 81.6** (`⬆️ +2.8`) | 0.4% | 25.6% | 🟢 ZYSK |
| #13 | `L3_GC-01_COST_MINUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 0 | 78.8 → 🟡 ** 81.2** (`⬆️ +2.4`) | 0.3% | 24.4% | 🟢 ZYSK |
| #14 | `L3_KB-04_COST_MINUS1` | KB-04 (Faworyt Dworu): cost 2 → 1 | 78.8 → 🟡 ** 81.1** (`⬆️ +2.3`) | 0.3% | 24.8% | 🟢 ZYSK |
| #15 | `L3_KB-06_COST_PLUS1` | KB-06 (Areszt Królewski): cost 1 → 2 | 78.8 → 🟡 ** 80.6** (`⬆️ +1.8`) | 0.3% | 26.0% | 🟢 ZYSK |
| #16 | `L3_KT-04_GOLD_PLUS1` | KT-04 (Zwierciadło Herezji): gold 0 → 1 | 78.8 → 🟡 ** 80.2** (`⬆️ +1.4`) | 0.3% | 25.4% | 🟢 ZYSK |
| #17 | `L3_SO-03_GOLD_PLUS1` | SO-03 (Podejrzenie): gold 0 → 1 | 78.8 → 🟡 ** 80.0** (`⬆️ +1.2`) | 0.3% | 24.7% | 🟢 ZYSK |
| #18 | `L3_SO-01_GOLD_PLUS1` | SO-01 (Patrol Familiariuszy): gold 0 → 1 | 78.8 → 🟡 ** 79.8** (`⬆️ +1.0`) | 0.3% | 25.0% | 🟢 ZYSK |
| #19 | `L3_CAA-04_GOLD_PLUS1` | CAA-04 (Fałszywy Trop): gold 0 → 1 | 78.8 → 🟡 ** 79.8** (`⬆️ +1.0`) | 0.4% | 25.4% | 🟢 ZYSK |
| #20 | `L3_SO-02_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): heresy 0 → 1 | 78.8 → 🟡 ** 79.5** (`⬆️ +0.7`) | 0.3% | 25.3% | 🟢 ZYSK |
| #21 | `L3_SO-09_COST_MINUS1` | SO-09 (Świadek Koronny): cost 2 → 1 | 78.8 → 🟡 ** 79.0** (`⬆️ +0.2`) | 0.3% | 24.8% | 🟢 ZYSK |
| #22 | `L3_CAA-10_HERESY_MINUS1` | CAA-10 (Echo Alhambry): heresy 1 → 0 | 78.8 → 🟡 ** 78.9** (`⬆️ +0.1`) | 0.5% | 25.7% | 🟢 ZYSK |
| #23 | `L3_KT-02_GOLD_MINUS1` | KT-02 (Transmutacja Złota): gold 2 → 1 | 🟡 ** 78.8** | 0.3% | 25.4% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_SO-06_COST_MINUS1` | SO-06 (Areszt Trybunalski): cost 2 → 1 | 78.8 → 🟡 ** 78.4** (`-0.4`) | 0.3% | 24.8% | ⚪ STRATA/NEUTRALNY |