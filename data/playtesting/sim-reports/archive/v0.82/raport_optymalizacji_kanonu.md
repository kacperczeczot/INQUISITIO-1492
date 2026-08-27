[Strona główna](../../../../../README.md) > [v0.82](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.82 (Iteracja #5, Faza 1D)

**Wersja Poprzednia:** `v0.81` (4P: `89.6 pkt`) → **Nowa Wersja:** `v0.82` (4P: `92.5 pkt`)
**Data:** 2026-08-17 03:21 | **Czas Trwania Iteracji:** 731.7s | **Zysk 4P:** `+2.9 pkt` | **Zysk Global:** `+0.7 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_KB-02_TARGET_HERESY_PLUS1` — **KB-02 (Pobór Podatków): target_heresy 0 → 1**
- **Opis Modyfikacji:** Karta `kb-02` (Pobór Podatków): `target_heresy` → `1`
- **Wynik Kanonu 4P Score:** 89.6 → 🟢 ** 92.5** (`⬆️ +2.9`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 86.2 → 95.3 (`⬆️ +9.1`) pkt
  - `4p-no-cienie`: 85.1 → 83.4 (`-1.7`) pkt
  - `4p-no-kabala`: 94.3 → 97.2 (`⬆️ +2.9`) pkt
  - `4p-no-korona`: 93.3 pkt
  - `4p-no-oficjum`: 89.3 → 93.3 (`⬆️ +4.0`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 44.4 → 47.4 (`⬆️ +3.0`) pkt
- **Tryb 4-osobowy (4p Avg):** 86.7 → 88.6 (`⬆️ +1.9`) pkt
- **Tryb 5-osobowy (5p Avg):** 69.7 → 66.8 (`-2.9`) pkt
- **Global Game Balance Score:** 66.9 → 🟠 ** 67.6** (`⬆️ +0.7`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `5.94 Er`
  - **Deadlocki (Limit Er):** `1.2%` (norma: <5%)
  - **Pas Biedy (Złoto):** `5.7%` (norma: <30%)
  - **Autodafé / partię:** `1.54`
  - **Oskarżenia / partię:** `3.59`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_KB-02_TARGET_HERESY_PLUS1` | KB-02 (Pobór Podatków): target_heresy 0 → 1 | 89.6 → 🟢 ** 92.5** (`⬆️ +2.9`) | 1.2% | 5.7% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KB-05_TARGET_HERESY_PLUS1` | KB-05 (List Żelazny): target_heresy 0 → 1 | 89.6 → 🟢 ** 91.9** (`⬆️ +2.3`) | 1.2% | 5.8% | 🟢 ZYSK |
| #3 | `L3_KB-07_TARGET_HERESY_PLUS1` | KB-07 (Szantaż Pieczęcią): target_heresy 0 → 1 | 89.6 → 🟢 ** 91.7** (`⬆️ +2.1`) | 1.3% | 5.7% | 🟢 ZYSK |
| #4 | `L3_CAA-08_TARGET_HERESY_PLUS1` | CAA-08 (Kaptur Nocy): target_heresy 0 → 1 | 89.6 → 🟢 ** 90.8** (`⬆️ +1.2`) | 1.4% | 5.9% | 🟢 ZYSK |
| #5 | `L3_CAA-06_COST_PLUS1` | CAA-06 (Ucieczka z Lochów): cost 2 → 3 | 89.6 → 🟢 ** 90.7** (`⬆️ +1.1`) | 1.4% | 5.9% | 🟢 ZYSK |
| #6 | `L3_GC-12_HERESY_PLUS1` | GC-12 (Złodziejski Zwiad): heresy 1 → 2 | 89.6 → 🟢 ** 90.7** (`⬆️ +1.1`) | 1.4% | 5.6% | 🟢 ZYSK |
| #7 | `L2_KB_ERA_MINUS1` | Korona Era: 4 → 3 | 89.6 → 🟢 ** 90.4** (`⬆️ +0.8`) | 1.4% | 5.8% | 🟢 ZYSK |
| #8 | `L3_KT-11_GOLD_PLUS1` | KT-11 (Medytacja Sefirot): gold 1 → 2 | 89.6 → 🟢 ** 90.2** (`⬆️ +0.6`) | 1.4% | 5.8% | 🟢 ZYSK |
| #9 | `L3_KT-11_COST_MINUS1` | KT-11 (Medytacja Sefirot): cost 1 → 0 | 89.6 → 🟢 ** 90.1** (`⬆️ +0.5`) | 1.4% | 5.7% | 🟢 ZYSK |
| #10 | `L3_SO-03_HERESY_PLUS1` | SO-03 (Podejrzenie): heresy 0 → 1 | 89.6 → 🟢 ** 90.1** (`⬆️ +0.5`) | 1.4% | 5.8% | 🟢 ZYSK |
| #11 | `L3_KB-01_COST_MINUS1` | KB-01 (Rozkaz Dworu): cost 1 → 0 | 89.6 → 🟡 ** 89.9** (`⬆️ +0.3`) | 1.3% | 4.2% | 🟢 ZYSK |
| #12 | `L3_KT-03_GOLD_PLUS1` | KT-03 (Zakazana Wiedza): gold 0 → 1 | 89.6 → 🟡 ** 89.9** (`⬆️ +0.3`) | 1.4% | 5.7% | 🟢 ZYSK |
| #13 | `L3_CAA-03_HERESY_PLUS1` | CAA-03 (Cień na Rynku): heresy 1 → 2 | 89.6 → 🟡 ** 89.8** (`⬆️ +0.2`) | 1.5% | 5.8% | 🟢 ZYSK |
| #14 | `L3_KT-01_HERESY_PLUS1` | KT-01 (Rytuał Przejścia): heresy 0 → 1 | 89.6 → 🟡 ** 89.8** (`⬆️ +0.2`) | 1.5% | 5.8% | 🟢 ZYSK |
| #15 | `L3_SO-11_HERESY_PLUS1` | SO-11 (Dekret Czystości Wiary): heresy 0 → 1 | 89.6 → 🟡 ** 89.8** (`⬆️ +0.2`) | 1.2% | 5.8% | 🟢 ZYSK |
| #16 | `L3_KT-04_GOLD_PLUS1` | KT-04 (Zwierciadło Herezji): gold 0 → 1 | 89.6 → 🟡 ** 89.8** (`⬆️ +0.2`) | 1.3% | 5.7% | 🟢 ZYSK |
| #17 | `L2_KB_HOOKS_MINUS1` | Korona Haki: 1 → 0 | 89.6 → 🟡 ** 89.8** (`⬆️ +0.2`) | 1.4% | 5.8% | 🟢 ZYSK |
| #18 | `L3_KT-11_HERESY_PLUS1` | KT-11 (Medytacja Sefirot): heresy 0 → 1 | 89.6 → 🟡 ** 89.7** (`⬆️ +0.1`) | 1.5% | 5.8% | 🟢 ZYSK |
| #19 | `L1_MAX_ERAS_MINUS1` | Limit Er: 12 → 11 | 89.6 → 🟡 ** 89.7** (`⬆️ +0.1`) | 2.7% | 5.8% | 🟢 ZYSK |
| #20 | `L3_KT-12_COST_PLUS1` | KT-12 (Strażnik Archiwum): cost 0 → 1 | 🟡 ** 89.6** | 1.4% | 6.1% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 2 → 3 | 89.6 → 🟡 ** 89.5** (`-0.1`) | 1.4% | 5.8% | ⚪ STRATA/NEUTRALNY |
| #22 | `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 3 → 4 | 89.6 → 🟡 ** 89.5** (`-0.1`) | 1.4% | 5.8% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_KT-06_GOLD_PLUS1` | KT-06 (Przesłuchanie Imienia): gold 0 → 1 | 89.6 → 🟡 ** 89.3** (`-0.3`) | 1.4% | 5.6% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_KT-06_COST_MINUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 1 | 89.6 → 🟡 ** 89.3** (`-0.3`) | 1.4% | 5.6% | ⚪ STRATA/NEUTRALNY |