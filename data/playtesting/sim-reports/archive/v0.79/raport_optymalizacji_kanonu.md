[Strona główna](../../../../../README.md) > [v0.79](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.79 (Iteracja #2, Faza 1D)

**Wersja Poprzednia:** `v0.78` (4P: `81.3 pkt`) → **Nowa Wersja:** `v0.79` (4P: `86.0 pkt`)
**Data:** 2026-08-17 02:45 | **Czas Trwania Iteracji:** 702.3s | **Zysk 4P:** `+4.7 pkt` | **Zysk Global:** `+1.0 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_SO-02_TARGET_HERESY_PLUS1` — **SO-02 (Skarbiec Trybunału): target_heresy 0 → 1**
- **Opis Modyfikacji:** Karta `so-02` (Skarbiec Trybunału): `target_heresy` → `1`
- **Wynik Kanonu 4P Score:** 81.3 → 🟡 ** 86.0** (`⬆️ +4.7`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 79.6 → 86.5 (`⬆️ +6.9`) pkt
  - `4p-no-cienie`: 71.2 → 73.0 (`⬆️ +1.8`) pkt
  - `4p-no-kabala`: 83.5 → 89.8 (`⬆️ +6.3`) pkt
  - `4p-no-korona`: 81.5 → 89.8 (`⬆️ +8.3`) pkt
  - `4p-no-oficjum`: 90.8 pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 37.7 → 39.2 (`⬆️ +1.5`) pkt
- **Tryb 4-osobowy (4p Avg):** 81.8 → 85.3 (`⬆️ +3.5`) pkt
- **Tryb 5-osobowy (5p Avg):** 69.2 → 67.1 (`-2.1`) pkt
- **Global Game Balance Score:** 62.9 → 🟠 ** 63.9** (`⬆️ +1.0`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.03 Er`
  - **Deadlocki (Limit Er):** `1.5%` (norma: <5%)
  - **Pas Biedy (Złoto):** `5.5%` (norma: <30%)
  - **Autodafé / partię:** `1.56`
  - **Oskarżenia / partię:** `3.56`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-02_TARGET_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): target_heresy 0 → 1 | 81.3 → 🟡 ** 86.0** (`⬆️ +4.7`) | 1.5% | 5.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_GC-01_TARGET_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): target_heresy 0 → 1 | 81.3 → 🟡 ** 84.7** (`⬆️ +3.4`) | 1.5% | 6.1% | 🟢 ZYSK |
| #3 | `L3_GC-01_COST_MINUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 0 | 81.3 → 🟡 ** 83.9** (`⬆️ +2.6`) | 1.6% | 5.7% | 🟢 ZYSK |
| #4 | `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 81.3 → 🟡 ** 83.5** (`⬆️ +2.2`) | 1.6% | 5.7% | 🟢 ZYSK |
| #5 | `L3_KT-11_COST_MINUS1` | KT-11 (Medytacja Sefirot): cost 1 → 0 | 81.3 → 🟡 ** 83.5** (`⬆️ +2.2`) | 1.7% | 5.4% | 🟢 ZYSK |
| #6 | `L3_GC-01_GOLD_PLUS1` | GC-01 (Przekupiony Strażnik): gold 0 → 1 | 81.3 → 🟡 ** 83.5** (`⬆️ +2.2`) | 1.6% | 5.9% | 🟢 ZYSK |
| #7 | `L3_SO-06_TARGET_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): target_heresy 0 → 1 | 81.3 → 🟡 ** 83.3** (`⬆️ +2.0`) | 1.3% | 5.7% | 🟢 ZYSK |
| #8 | `L3_KT-11_GOLD_PLUS1` | KT-11 (Medytacja Sefirot): gold 1 → 2 | 81.3 → 🟡 ** 83.3** (`⬆️ +2.0`) | 1.7% | 5.5% | 🟢 ZYSK |
| #9 | `L3_SO-10_TARGET_HERESY_PLUS1` | SO-10 (Oczyść Miasto): target_heresy 0 → 1 | 81.3 → 🟡 ** 83.3** (`⬆️ +2.0`) | 1.5% | 5.6% | 🟢 ZYSK |
| #10 | `L3_GC-02_HERESY_PLUS1` | GC-02 (Czarny Rynek): heresy 1 → 2 | 81.3 → 🟡 ** 83.2** (`⬆️ +1.9`) | 1.6% | 5.5% | 🟢 ZYSK |
| #11 | `L3_CAA-06_TARGET_HERESY_PLUS1` | CAA-06 (Ucieczka z Lochów): target_heresy 0 → 1 | 81.3 → 🟡 ** 83.1** (`⬆️ +1.8`) | 1.5% | 5.7% | 🟢 ZYSK |
| #12 | `L3_SO-09_TARGET_HERESY_PLUS1` | SO-09 (Świadek Koronny): target_heresy 0 → 1 | 81.3 → 🟡 ** 82.8** (`⬆️ +1.5`) | 1.5% | 5.6% | 🟢 ZYSK |
| #13 | `L3_SO-02_GOLD_PLUS1` | SO-02 (Skarbiec Trybunału): gold 3 → 4 | 81.3 → 🟡 ** 82.7** (`⬆️ +1.4`) | 1.5% | 5.3% | 🟢 ZYSK |
| #14 | `L3_SO-02_COST_MINUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 0 | 81.3 → 🟡 ** 82.7** (`⬆️ +1.4`) | 1.5% | 5.3% | 🟢 ZYSK |
| #15 | `L3_SO-12_HERESY_PLUS1` | SO-12 (Straż Trybunalska): heresy 0 → 1 | 81.3 → 🟡 ** 82.6** (`⬆️ +1.3`) | 1.4% | 5.5% | 🟢 ZYSK |
| #16 | `L3_SO-08_HERESY_PLUS1` | SO-08 (Nasłanie Inkwizytora): heresy 0 → 1 | 81.3 → 🟡 ** 82.4** (`⬆️ +1.1`) | 1.3% | 5.5% | 🟢 ZYSK |
| #17 | `L3_SO-04_COST_PLUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 2 | 81.3 → 🟡 ** 82.4** (`⬆️ +1.1`) | 1.7% | 5.7% | 🟢 ZYSK |
| #18 | `L3_SO-09_GOLD_PLUS1` | SO-09 (Świadek Koronny): gold 0 → 1 | 81.3 → 🟡 ** 82.4** (`⬆️ +1.1`) | 1.7% | 5.5% | 🟢 ZYSK |
| #19 | `L3_SO-06_GOLD_PLUS1` | SO-06 (Areszt Trybunalski): gold 0 → 1 | 81.3 → 🟡 ** 82.2** (`⬆️ +0.9`) | 1.6% | 5.5% | 🟢 ZYSK |
| #20 | `L3_KT-08_COST_MINUS1` | KT-08 (Areszt Wiedzy): cost 1 → 0 | 81.3 → 🟡 ** 82.1** (`⬆️ +0.8`) | 1.7% | 5.4% | 🟢 ZYSK |
| #21 | `L3_SO-07_HERESY_PLUS1` | SO-07 (Przesłuchanie Oficjum): heresy 0 → 1 | 81.3 → 🟡 ** 81.8** (`⬆️ +0.5`) | 1.7% | 5.2% | 🟢 ZYSK |
| #22 | `L3_SO-03_COST_PLUS1` | SO-03 (Podejrzenie): cost 2 → 3 | 81.3 → 🟡 ** 81.4** (`⬆️ +0.1`) | 1.7% | 5.5% | 🟢 ZYSK |
| #23 | `L3_CAA-04_GOLD_PLUS1` | CAA-04 (Fałszywy Trop): gold 0 → 1 | 81.3 → 🟡 ** 80.2** (`-1.1`) | 1.6% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_CAA-04_COST_MINUS1` | CAA-04 (Fałszywy Trop): cost 1 → 0 | 81.3 → 🟡 ** 80.1** (`-1.2`) | 1.6% | 5.5% | ⚪ STRATA/NEUTRALNY |