[Strona główna](../../../../../README.md) > [v0.99.18](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v0.99.18 (Iteracja #5, Faza 1D)

**Wersja Poprzednia:** `v0.99.17` (4P: `70.7 pkt`) → **Nowa Wersja:** `v0.99.18` (4P: `71.2 pkt`)
**Data:** 2026-08-18 13:41 | **Czas Trwania Iteracji:** 654.9s | **Zysk 4P:** `+0.5 pkt` | **Zysk Global:** `-0.8 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_GC-01_COST_PLUS1` — **GC-01 (Przekupiony Strażnik): cost 1 → 2**
- **Opis Modyfikacji:** Karta `gc-01` (Przekupiony Strażnik): `cost` → `2`
- **Wynik Kanonu 4P Score:** 70.7 → 🟠 ** 71.2** (`⬆️ +0.5`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 73.0 pkt
  - `4p-no-cienie`: 68.7 → 69.4 (`⬆️ +0.7`) pkt
  - `4p-no-kabala`: 64.7 → 65.7 (`⬆️ +1.0`) pkt
  - `4p-no-korona`: 80.4 → 81.5 (`⬆️ +1.1`) pkt
  - `4p-no-oficjum`: 66.7 → 66.5 (`-0.2`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 14.8 → 14.6 (`-0.2`) pkt
- **Tryb 4-osobowy (4p Avg):** 71.8 → 71.6 (`-0.2`) pkt
- **Tryb 5-osobowy (5p Avg):** 42.8 → 40.7 (`-2.1`) pkt
- **Global Game Balance Score:** 43.1 → 🔴 ** 42.3** (`-0.8`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.21 Er`
  - **Deadlocki (Limit Er):** `0.7%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.5%` (norma: <30%)
  - **Autodafé / partię:** `2.23`
  - **Oskarżenia / partię:** `3.80`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-01_COST_PLUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 2 | 70.7 → 🟠 ** 71.2** (`⬆️ +0.5`) | 0.7% | 1.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_GC-01_TARGET_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): target_heresy 0 → 1 | 70.7 → 🟠 ** 72.0** (`⬆️ +1.3`) | 0.7% | 1.5% | 🟢 ZYSK |
| #3 | `L3_GC-11_GOLD_PLUS1` | GC-11 (Fałszywe Świadectwo Cechu): gold 0 → 1 | 70.7 → 🟠 ** 71.5** (`⬆️ +0.8`) | 0.7% | 1.5% | 🟢 ZYSK |
| #4 | `L3_SO-03_TARGET_HERESY_PLUS1` | SO-03 (Podejrzenie): target_heresy 1 → 2 | 70.7 → 🟠 ** 71.4** (`⬆️ +0.7`) | 0.7% | 1.5% | 🟢 ZYSK |
| #5 | `L3_SO-01_TARGET_HERESY_PLUS1` | SO-01 (Patrol Familiariuszy): target_heresy 0 → 1 | 70.7 → 🟠 ** 71.3** (`⬆️ +0.6`) | 0.7% | 1.5% | 🟢 ZYSK |
| #6 | `L3_SO-11_HERESY_PLUS1` | SO-11 (Dekret Czystości Wiary): heresy 0 → 1 | 70.7 → 🟠 ** 71.0** (`⬆️ +0.3`) | 0.7% | 1.5% | 🟢 ZYSK |
| #7 | `L3_GC-03_GOLD_PLUS1` | GC-03 (Podrzucenie Księgi): gold 0 → 1 | 70.7 → 🟠 ** 71.0** (`⬆️ +0.3`) | 0.7% | 1.5% | 🟢 ZYSK |
| #8 | `L3_KT-11_COST_PLUS1` | KT-11 (Medytacja Sefirot): cost 1 → 2 | 70.7 → 🟠 ** 70.9** (`⬆️ +0.2`) | 0.7% | 1.5% | 🟢 ZYSK |
| #9 | `L3_KT-01_COST_MINUS1` | KT-01 (Rytuał Przejścia): cost 1 → 0 | 70.7 → 🟠 ** 70.8** (`⬆️ +0.1`) | 0.7% | 1.5% | 🟢 ZYSK |
| #10 | `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 70.7 → 🟠 ** 70.8** (`⬆️ +0.1`) | 0.7% | 1.5% | 🟢 ZYSK |
| #11 | `L3_KT-12_COST_PLUS1` | KT-12 (Strażnik Archiwum): cost 0 → 1 | 🟠 ** 70.7** | 0.7% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 2 → 3 | 70.7 → 🟠 ** 70.6** (`-0.1`) | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #13 | `L1_MAX_ERAS_MINUS1` | Limit Er: 13 → 12 | 70.7 → 🟠 ** 68.6** (`-2.1`) | 2.1% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #14 | `L3_SO-05_COST_PLUS1` | SO-05 (Wezwanie do Trybunału): cost 0 → 1 | 🟠 ** 70.7** | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #15 | `L3_SO-02_GOLD_MINUS1` | SO-02 (Skarbiec Trybunału): gold 3 → 2 | 70.7 → 🟠 ** 70.6** (`-0.1`) | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #16 | `L3_GC-01_COST_MINUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 0 | 🟠 ** 70.7** | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #17 | `L3_KB-06_COST_MINUS1` | KB-06 (Areszt Królewski): cost 2 → 1 | 70.7 → 🟠 ** 69.8** (`-0.9`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #18 | `L3_CAA-12_GOLD_MINUS1` | CAA-12 (Skrytka w Murach): gold 3 → 2 | 70.7 → 🟠 ** 70.4** (`-0.3`) | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #19 | `L3_CAA-12_COST_PLUS1` | CAA-12 (Skrytka w Murach): cost 0 → 1 | 70.7 → 🟠 ** 70.4** (`-0.3`) | 0.7% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #20 | `L3_GC-07_TARGET_HERESY_PLUS1` | GC-07 (Skrytobójstwo): target_heresy 0 → 1 | 70.7 → 🟠 ** 71.1** (`⬆️ +0.4`) | 0.7% | 1.5% | 🟢 ZYSK |
| #21 | `L3_KT-10_GOLD_PLUS1` | KT-10 (Pieczęć Salomona): gold 0 → 1 | 70.7 → 🟠 ** 71.0** (`⬆️ +0.3`) | 0.7% | 1.5% | 🟢 ZYSK |
| #22 | `L3_GC-08_COST_MINUS1` | GC-08 (Zatrute Złoto): cost 1 → 0 | 70.7 → 🟠 ** 69.9** (`-0.8`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #23 | `L3_GC-08_TARGET_HERESY_PLUS1` | GC-08 (Zatrute Złoto): target_heresy 1 → 2 | 70.7 → 🟠 ** 70.6** (`-0.1`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #24 | `L3_GC-08_GOLD_PLUS1` | GC-08 (Zatrute Złoto): gold 1 → 2 | 70.7 → 🟠 ** 69.8** (`-0.9`) | 0.6% | 1.5% | ⚪ STRATA/NEUTRALNY |