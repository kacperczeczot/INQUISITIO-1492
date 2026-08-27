[Strona główna](../../../../../README.md) > [v1.0-alpha.11](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.11 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.10` (4P: `76.9 pkt`) → **Nowa Wersja:** `v1.0-alpha.11` (4P: `77.4 pkt`)
**Data:** 2026-08-20 22:45 | **Czas Trwania Iteracji:** 768.6s | **Zysk 4P:** `+0.5 pkt` | **Zysk Global:** `-0.8 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_GC-11_COST_MINUS1` — **GC-11 (Fałszywe Świadectwo Cechu): cost 1 → 0**
- **Opis Modyfikacji:** Karta `gc-11` (Fałszywe Świadectwo Cechu): `cost` → `0`
- **Wynik Kanonu 4P Balance:** 76.9 → 🟡 ** 77.4** (`⬆️ +0.5`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 67.2 pkt
  - `4p-no-cienie`: 89.1 → 90.7 (`⬆️ +1.6`) pkt
  - `4p-no-kabala`: 61.1 → 61.2 (`⬆️ +0.1`) pkt
  - `4p-no-korona`: 92.6 → 93.4 (`⬆️ +0.8`) pkt
  - `4p-no-oficjum`: 74.6 → 74.5 (`-0.1`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 22.9 → 22.6 (`-0.3`) pkt
- **Tryb 4-osobowy (4p Avg):** 79.8 → 79.9 (`⬆️ +0.1`) pkt
- **Tryb 5-osobowy (5p Avg):** 34.2 → 31.8 (`-2.4`) pkt
- **Global Game Balance Score:** 45.6 → 🔴 ** 44.8** (`-0.8`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.20 Er`
  - **Deadlocki (Limit Er):** `0.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.5%` (norma: <30%)
  - **Autodafé / partię:** `2.21`
  - **Oskarżenia / partię:** `4.25`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-11_COST_MINUS1` | GC-11 (Fałszywe Świadectwo Cechu): cost 1 → 0 | 76.9 → 🟡 ** 77.4** (`⬆️ +0.5`) | 0.3% | 1.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KB-10_TARGET_HERESY_MINUS1` | KB-10 (Pieczęć Korony): target_heresy 1 → 0 | 76.9 → 🟡 ** 77.3** (`⬆️ +0.4`) | 0.3% | 1.6% | 🟢 ZYSK |
| #3 | `L3_SO-06_TARGET_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): target_heresy 0 → 1 | 76.9 → 🟡 ** 77.2** (`⬆️ +0.3`) | 0.3% | 1.6% | 🟢 ZYSK |
| #4 | `L3_SO-03_HERESY_PLUS1` | SO-03 (Podejrzenie): heresy 0 → 1 | 76.9 → 🟡 ** 77.1** (`⬆️ +0.2`) | 0.3% | 1.6% | 🟢 ZYSK |
| #5 | `L3_GC-11_COST_PLUS1` | GC-11 (Fałszywe Świadectwo Cechu): cost 1 → 2 | 76.9 → 🟡 ** 77.0** (`⬆️ +0.1`) | 0.3% | 1.6% | 🟢 ZYSK |
| #6 | `L3_SO-11_HERESY_PLUS1` | SO-11 (Dekret Czystości Wiary): heresy 1 → 2 | 76.9 → 🟡 ** 77.0** (`⬆️ +0.1`) | 0.3% | 1.6% | 🟢 ZYSK |
| #7 | `L3_SO-03_COST_MINUS1` | SO-03 (Podejrzenie): cost 2 → 1 | 🟡 ** 76.9** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_SO-06_COST_PLUS1` | SO-06 (Areszt Trybunalski): cost 2 → 3 | 🟡 ** 76.9** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_SO-07_COST_PLUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 3 | 🟡 ** 76.9** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_SO-01_COST_PLUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 2 | 🟡 ** 76.9** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_SO-03_COST_PLUS1` | SO-03 (Podejrzenie): cost 2 → 3 | 🟡 ** 76.9** | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_GC-12_COST_PLUS1` | GC-12 (Złodziejski Zwiad): cost 0 → 1 | 76.9 → 🟡 ** 76.8** (`-0.1`) | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |