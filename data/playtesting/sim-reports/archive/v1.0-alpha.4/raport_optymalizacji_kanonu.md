[Strona główna](../../../../../README.md) > [v1.0-alpha.4](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.4 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.3` (4P: `74.7 pkt`) → **Nowa Wersja:** `v1.0-alpha.4` (4P: `75.9 pkt`)
**Data:** 2026-08-18 23:49 | **Czas Trwania Iteracji:** 459.1s | **Zysk 4P:** `+1.2 pkt` | **Zysk Global:** `+0.9 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L1_MAX_ERAS_PLUS1` — **Limit Er: 12 → 13**
- **Opis Modyfikacji:** Limit Er: offset +1 (nowy: 13)
- **Wynik Kanonu 4P Score:** 74.7 → 🟡 ** 75.9** (`⬆️ +1.2`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 61.8 → 68.0 (`⬆️ +6.2`) pkt
  - `4p-no-cienie`: 86.9 pkt
  - `4p-no-kabala`: 62.4 pkt
  - `4p-no-korona`: 89.1 → 89.3 (`⬆️ +0.2`) pkt
  - `4p-no-oficjum`: 73.1 pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 18.6 → 21.0 (`⬆️ +2.4`) pkt
- **Tryb 4-osobowy (4p Avg):** 77.5 → 77.7 (`⬆️ +0.2`) pkt
- **Tryb 5-osobowy (5p Avg):** 40.5 pkt
- **Global Game Balance Score:** 45.5 → 🔴 ** 46.4** (`⬆️ +0.9`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.21 Er`
  - **Deadlocki (Limit Er):** `0.5%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.6%` (norma: <30%)
  - **Autodafé / partię:** `2.22`
  - **Oskarżenia / partię:** `4.16`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L1_MAX_ERAS_PLUS1` | Limit Er: 12 → 13 | 74.7 → 🟡 ** 75.9** (`⬆️ +1.2`) | 0.5% | 1.6% | 🌟 ZWYCIĘZCA |
| #2 | `L3_GC-07_COST_MINUS1` | GC-07 (Skrytobójstwo): cost 2 → 1 | 74.7 → 🟡 ** 75.0** (`⬆️ +0.3`) | 1.9% | 1.6% | 🟢 ZYSK |
| #3 | `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 74.7 → 🟠 ** 74.9** (`⬆️ +0.2`) | 1.8% | 1.6% | 🟢 ZYSK |
| #4 | `L3_KT-01_COST_MINUS1` | KT-01 (Rytuał Przejścia): cost 1 → 0 | 74.7 → 🟠 ** 74.8** (`⬆️ +0.1`) | 1.8% | 1.6% | 🟢 ZYSK |
| #5 | `L3_KT-11_COST_MINUS1` | KT-11 (Medytacja Sefirot): cost 1 → 0 | 74.7 → 🟠 ** 74.8** (`⬆️ +0.1`) | 1.8% | 1.6% | 🟢 ZYSK |
| #6 | `L3_KT-07_COST_MINUS1` | KT-07 (Archiwum Ukryte): cost 1 → 0 | 🟠 ** 74.7** | 1.8% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_SO-11_HERESY_PLUS1` | SO-11 (Dekret Czystości Wiary): heresy 1 → 2 | 🟠 ** 74.7** | 1.9% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #8 | `L2_CAA_ERA_MINUS1` | Cienie Era ścieżki: 1 → 0 | 🟠 ** 74.7** | 1.9% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #9 | `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 7 → 8 | 🟠 ** 74.7** | 1.9% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #10 | `L2_CAA_ERA_PLUS1` | Cienie Era ścieżki: 1 → 2 | 🟠 ** 74.7** | 1.9% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_CAA-01_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 🟠 ** 74.7** | 1.9% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 0 → 1 | 🟠 ** 74.7** | 1.9% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #13 | `L3_CAA-07_HERESY_PLUS1` | CAA-07 (Szantaż Bractwa): heresy 0 → 1 | 🟠 ** 74.7** | 1.9% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_CAA-09_COST_PLUS1` | CAA-09 (Kurier Relikwii): cost 0 → 1 | 🟠 ** 74.7** | 1.9% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 0 → 1 | 🟠 ** 74.7** | 1.9% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_CAA-10_COST_PLUS1` | CAA-10 (Echo Alhambry): cost 0 → 1 | 🟠 ** 74.7** | 1.9% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_CAA-09_GOLD_PLUS1` | CAA-09 (Kurier Relikwii): gold 0 → 1 | 🟠 ** 74.7** | 1.9% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_CAA-11_COST_MINUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 0 | 🟠 ** 74.7** | 1.9% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_CAA-11_COST_PLUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 2 | 🟠 ** 74.7** | 1.9% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_CAA-11_HERESY_PLUS1` | CAA-11 (Nocna Zmiana Warty): heresy 0 → 1 | 🟠 ** 74.7** | 1.9% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #21 | `L3_GC-12_COST_PLUS1` | GC-12 (Złodziejski Zwiad): cost 0 → 1 | 74.7 → 🟠 ** 74.6** (`-0.1`) | 1.9% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #22 | `L3_CAA-02_GOLD_PLUS1` | CAA-02 (Złoto z Kryjówki): gold 3 → 4 | 74.7 → 🟠 ** 74.5** (`-0.2`) | 1.9% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 1 → 2 | 74.7 → 🟠 ** 74.4** (`-0.3`) | 1.9% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 2 → 3 | 74.7 → 🟠 ** 74.1** (`-0.6`) | 1.8% | 1.6% | ⚪ STRATA/NEUTRALNY |