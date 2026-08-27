[Strona główna](../../../../../README.md) > [v1.0-alpha.12](README.md) > [raport_optymalizacji_kanonu](raport_optymalizacji_kanonu.md)

---

# Raport Optymalizacji Kanonu 4P (Anchor-Based 4P Optimizer) — Wersja v1.0-alpha.12 (Iteracja #2, Faza 1D)

**Wersja Poprzednia:** `v1.0-alpha.11` (4P: `77.4 pkt`) → **Nowa Wersja:** `v1.0-alpha.12` (4P: `77.8 pkt`)
**Data:** 2026-08-20 22:58 | **Czas Trwania Iteracji:** 781.6s | **Zysk 4P:** `+0.4 pkt` | **Zysk Global:** `+0.6 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu Kanonu 4P
- **Wybrany Wariant (1D):** `L3_GC-09_GOLD_PLUS1` — **GC-09 (Lista Dłużników): gold 0 → 1**
- **Opis Modyfikacji:** Karta `gc-09` (Lista Dłużników): `gold` → `1`
- **Wynik Kanonu 4P Balance:** 77.4 → 🟡 ** 77.8** (`⬆️ +0.4`) pkt
- **Rozbicie Setupów Kanonu 4P:**
  - `4p-core`: 67.2 pkt
  - `4p-no-cienie`: 90.7 → 91.5 (`⬆️ +0.8`) pkt
  - `4p-no-kabala`: 61.2 → 61.1 (`-0.1`) pkt
  - `4p-no-korona`: 93.4 → 95.7 (`⬆️ +2.3`) pkt
  - `4p-no-oficjum`: 74.5 → 73.7 (`-0.8`) pkt

## 2. Diagnostyka Wpływu Kolateralnego na Pozostałe Tryby (3P / 5P)
- **Tryb 3-osobowy (3p Avg):** 22.6 pkt
- **Tryb 4-osobowy (4p Avg):** 79.9 → 80.3 (`⬆️ +0.4`) pkt
- **Tryb 5-osobowy (5p Avg):** 31.8 → 33.3 (`⬆️ +1.5`) pkt
- **Global Game Balance Score:** 44.8 → 🔴 ** 45.4** (`⬆️ +0.6`) pkt

- **Kluczowa Telemetria Silnika (Kanon 4P):**
  - **Średnia Długość Gry:** `6.20 Er`
  - **Deadlocki (Limit Er):** `0.3%` (norma: <5%)
  - **Pas Biedy (Złoto):** `1.5%` (norma: <30%)
  - **Autodafé / partię:** `2.21`
  - **Oskarżenia / partię:** `4.25`

## 3. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści 4P)

| Poz. | ID Wariantu | Nazwa / Opis | 4P Score (baza → test) | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-09_GOLD_PLUS1` | GC-09 (Lista Dłużników): gold 0 → 1 | 77.4 → 🟡 ** 77.8** (`⬆️ +0.4`) | 0.3% | 1.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_SO-03_HERESY_PLUS1` | SO-03 (Podejrzenie): heresy 0 → 1 | 77.4 → 🟡 ** 77.6** (`⬆️ +0.2`) | 0.3% | 1.5% | 🟢 ZYSK |
| #3 | `L3_CAA-08_COST_PLUS1` | CAA-08 (Kaptur Nocy): cost 1 → 2 | 77.4 → 🟡 ** 77.5** (`⬆️ +0.1`) | 0.3% | 1.5% | 🟢 ZYSK |
| #4 | `L3_SO-06_TARGET_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): target_heresy 0 → 1 | 77.4 → 🟡 ** 77.5** (`⬆️ +0.1`) | 0.3% | 1.5% | 🟢 ZYSK |
| #5 | `L3_SO-07_COST_PLUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 3 | 🟡 ** 77.4** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #6 | `L3_SO-06_COST_PLUS1` | SO-06 (Areszt Trybunalski): cost 2 → 3 | 🟡 ** 77.4** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #7 | `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 🟡 ** 77.4** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #8 | `L3_GC-11_HERESY_PLUS1` | GC-11 (Fałszywe Świadectwo Cechu): heresy 0 → 1 | 🟡 ** 77.4** | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #9 | `L3_SO-03_COST_PLUS1` | SO-03 (Podejrzenie): cost 2 → 3 | 77.4 → 🟡 ** 77.3** (`-0.1`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #10 | `L3_GC-12_COST_PLUS1` | GC-12 (Złodziejski Zwiad): cost 0 → 1 | 77.4 → 🟡 ** 77.3** (`-0.1`) | 0.3% | 1.6% | ⚪ STRATA/NEUTRALNY |
| #11 | `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 0 → 1 | 77.4 → 🟡 ** 77.3** (`-0.1`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_CAA-02_GOLD_MINUS1` | CAA-02 (Złoto z Kryjówki): gold 3 → 2 | 77.4 → 🟡 ** 77.3** (`-0.1`) | 0.3% | 1.5% | ⚪ STRATA/NEUTRALNY |