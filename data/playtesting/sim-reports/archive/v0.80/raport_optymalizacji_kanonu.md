[Strona główna](../../../../../README.md) > [v0.80](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.80 (Iteracja #3, Faza 1D)

**Wersja Poprzednia:** `v0.79` (4P: `86.0 pkt`) → **Nowa Wersja:** `v0.80` (4P: `87.8 pkt`)
**Data:** 2026-08-17 02:57 | **Czas Trwania Iteracji:** 684.4s | **Zysk 4P:** `+1.8 pkt` | **Zysk Global:** `+0.8 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_GC-01_GOLD_PLUS1` — **GC-01 (Przekupiony Strażnik): gold 0 → 1**
- **Opis Modyfikacji:** Karta `gc-01` (Przekupiony Strażnik): `gold` → `1`
- **Wynik Kanonu 4P Score:** 86.0 → 🟡 ** 87.8** (`⬆️ +1.8`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 86.5 pkt
  - `4p-no-cienie`: 73.0 → 76.7 (`⬆️ +3.7`) pkt
  - `4p-no-kabala`: 89.8 → 94.7 (`⬆️ +4.9`) pkt
  - `4p-no-korona`: 89.8 → 93.3 (`⬆️ +3.5`) pkt
  - `4p-no-oficjum`: 90.8 → 88.0 (`-2.8`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 39.2 → 40.5 (`⬆️ +1.3`) pkt
- **Tryb 4-osobowy (4p Avg):** 85.3 → 86.3 (`⬆️ +1.0`) pkt
- **Tryb 5-osobowy (5p Avg):** 67.1 → 67.3 (`⬆️ +0.2`) pkt
- **Global Game Balance Score:** 63.9 → 🟠 ** 64.7** (`⬆️ +0.8`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.03 Er`
  - **Deadlocki (Limit Er):** `1.4%` (norma: <5%)
  - **Pas Biedy (Złoto):** `5.9%` (norma: <30%)
  - **Autodafé / partię:** `1.57`
  - **Oskarżenia / partię:** `3.57`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-01_GOLD_PLUS1` | GC-01 (Przekupiony Strażnik): gold 0 → 1 | 86.0 → 🟡 ** 87.8** (`⬆️ +1.8`) | 1.4% | 5.9% | 🌟 ZWYCIĘZCA |
| #2 | `L3_GC-01_COST_MINUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 0 | 86.0 → 🟡 ** 87.8** (`⬆️ +1.8`) | 1.4% | 5.6% | 🟢 ZYSK |
| #3 | `L3_GC-09_HERESY_PLUS1` | GC-09 (Lista Dłużników): heresy 0 → 1 | 86.0 → 🟡 ** 87.7** (`⬆️ +1.7`) | 1.5% | 5.4% | 🟢 ZYSK |
| #4 | `L2_KB_ERA_MINUS1` | Korona Era: 4 → 3 | 86.0 → 🟡 ** 87.1** (`⬆️ +1.1`) | 1.5% | 5.5% | 🟢 ZYSK |
| #5 | `L3_KT-11_COST_MINUS1` | KT-11 (Medytacja Sefirot): cost 1 → 0 | 86.0 → 🟡 ** 86.7** (`⬆️ +0.7`) | 1.7% | 5.3% | 🟢 ZYSK |
| #6 | `L2_KB_HOOKS_MINUS1` | Korona Haki: 1 → 0 | 86.0 → 🟡 ** 86.5** (`⬆️ +0.5`) | 1.5% | 5.5% | 🟢 ZYSK |
| #7 | `L3_KT-11_HERESY_PLUS1` | KT-11 (Medytacja Sefirot): heresy 0 → 1 | 86.0 → 🟡 ** 86.5** (`⬆️ +0.5`) | 1.5% | 5.5% | 🟢 ZYSK |
| #8 | `L3_KB-08_COST_PLUS1` | KB-08 (Przekupstwo Sędziego): cost 2 → 3 | 86.0 → 🟡 ** 86.4** (`⬆️ +0.4`) | 1.4% | 5.4% | 🟢 ZYSK |
| #9 | `L2_CAA_ERA_MINUS1` | Cienie Era: 4 → 3 | 86.0 → 🟡 ** 86.1** (`⬆️ +0.1`) | 1.5% | 5.5% | 🟢 ZYSK |
| #10 | `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 86.0 → 🟡 ** 86.1** (`⬆️ +0.1`) | 1.5% | 5.5% | 🟢 ZYSK |
| #11 | `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 🟡 ** 86.0** | 1.5% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #12 | `L1_MAX_ERAS_PLUS1` | Limit Er: 12 → 13 | 🟡 ** 86.0** | 0.9% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_SO-12_COST_MINUS1` | SO-12 (Straż Trybunalska): cost 1 → 0 | 🟡 ** 86.0** | 1.4% | 5.3% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_SO-12_GOLD_PLUS1` | SO-12 (Straż Trybunalska): gold 1 → 2 | 🟡 ** 86.0** | 1.4% | 5.3% | ⚪ STRATA/NEUTRALNY |
| #15 | `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 3 → 4 | 86.0 → 🟡 ** 85.8** (`-0.2`) | 1.5% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_GC-11_HERESY_PLUS1` | GC-11 (Fałszywe Świadectwo Cechu): heresy 0 → 1 | 86.0 → 🟡 ** 85.7** (`-0.3`) | 1.4% | 5.3% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_CAA-03_HERESY_PLUS1` | CAA-03 (Cień na Rynku): heresy 1 → 2 | 86.0 → 🟡 ** 85.6** (`-0.4`) | 1.6% | 5.4% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_CAA-03_GOLD_PLUS1` | CAA-03 (Cień na Rynku): gold 0 → 1 | 86.0 → 🟡 ** 85.5** (`-0.5`) | 1.5% | 5.4% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_SO-11_HERESY_PLUS1` | SO-11 (Dekret Czystości Wiary): heresy 0 → 1 | 86.0 → 🟡 ** 85.4** (`-0.6`) | 1.2% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_SO-11_COST_MINUS1` | SO-11 (Dekret Czystości Wiary): cost 1 → 0 | 86.0 → 🟡 ** 85.3** (`-0.7`) | 1.5% | 5.4% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_SO-11_GOLD_PLUS1` | SO-11 (Dekret Czystości Wiary): gold 1 → 2 | 86.0 → 🟡 ** 85.3** (`-0.7`) | 1.5% | 5.4% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 86.0 → 🟡 ** 85.2** (`-0.8`) | 1.5% | 5.5% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_GC-01_COST_PLUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 2 | 86.0 → 🟡 ** 85.2** (`-0.8`) | 1.5% | 6.2% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_KT-08_COST_MINUS1` | KT-08 (Areszt Wiedzy): cost 1 → 0 | 86.0 → 🟡 ** 85.0** (`-1.0`) | 1.5% | 5.3% | ⚪ STRATA/NEUTRALNY |