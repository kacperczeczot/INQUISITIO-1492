# Raport Optymalizacji Balansu (Szalony Audytor — Progressive Beam) — Wersja v0.43 (Iteracja #1, Faza 1D)

**Wersja Poprzednia:** `v0.42` (`56.7 pkt`) → **Nowa Wersja:** `v0.43` (`65.5 pkt`)
**Data:** 2026-08-16 01:44 | **Czas Trwania Iteracji:** 966.5s | **Zysk Global:** `+8.8 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu
- **Wybrany Wariant (1D):** `L3_SO-08_TARGET_HERESY_PLUS1` — **SO-08 (Nasłanie Inkwizytora): target_heresy 0 → 1**
- **Opis Modyfikacji:** Karta `so-08` (Nasłanie Inkwizytora): `target_heresy` → `1`
- **Global Game Balance Score:** 56.7 → 🟠 ** 65.5** (`⬆️ +8.8`) pkt
- **Rozbicie Składów Graczy:**
  - **3p:** 46.3 → 55.9 (`⬆️ +9.6`) pkt
  - **4p:** 67.1 → 75.2 (`⬆️ +8.1`) pkt
  - **5p:** 0.0 pkt
- **Kluczowa Telemetria Silnika:**
  - **Średnia Długość Gry:** `5.67 Er`
  - **Deadlocki (Limit Er):** `0.9%` (norma: <5%)
  - **Pas Biedy (Złoto):** `25.0%` (norma: <30%)
  - **Autodafé / partię:** `0.55`
  - **Oskarżenia / partię:** `3.51`

## 2. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści)

| Poz. | ID Wariantu | Nazwa / Opis | Global (baza → test) | 3p | 4p | 5p | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_SO-08_TARGET_HERESY_PLUS1` | SO-08 (Nasłanie Inkwizytora): target_heresy 0 → 1 | 56.7 → 🟠 ** 65.5** (`⬆️ +8.8`) | 55.9 | 75.2 | 0.0 | 0.9% | 25.0% | 🌟 ZWYCIĘZCA |
| #2 | `L3_GC-08_GOLD_MINUS1` | GC-08 (Zatrute Złoto): gold 1 → 0 | 56.7 → 🟠 ** 65.3** (`⬆️ +8.6`) | 40.5 | 90.2 | 0.0 | 1.1% | 26.1% | 🟢 ZYSK |
| #3 | `L3_SO-04_COST_MINUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 0 | 56.7 → 🟠 ** 63.6** (`⬆️ +6.9`) | 52.0 | 75.2 | 0.0 | 0.9% | 24.5% | 🟢 ZYSK |
| #4 | `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 0 → 1 | 56.7 → 🟠 ** 61.2** (`⬆️ +4.5`) | 48.6 | 73.8 | 0.0 | 1.0% | 25.3% | 🟢 ZYSK |
| #5 | `L3_GC-06_HERESY_PLUS1` | GC-06 (Szantaż): heresy 0 → 1 | 56.7 → 🟠 ** 60.6** (`⬆️ +3.9`) | 48.2 | 72.9 | 0.0 | 1.0% | 25.3% | 🟢 ZYSK |
| #6 | `L3_GC-04_COST_PLUS1` | GC-04 (Informator): cost 0 → 1 | 56.7 → 🔴 ** 59.9** (`⬆️ +3.2`) | 35.0 | 84.8 | 0.0 | 1.1% | 26.1% | 🟢 ZYSK |
| #7 | `L3_GC-04_HERESY_PLUS1` | GC-04 (Informator): heresy 1 → 2 | 56.7 → 🔴 ** 59.6** (`⬆️ +2.9`) | 44.7 | 74.4 | 0.0 | 1.0% | 25.2% | 🟢 ZYSK |
| #8 | `L3_SO-10_COST_MINUS1` | SO-10 (Oczyść Miasto): cost 4 → 3 | 56.7 → 🔴 ** 58.9** (`⬆️ +2.2`) | 52.9 | 64.9 | 0.0 | 0.8% | 24.4% | 🟢 ZYSK |
| #9 | `L3_SO-04_GOLD_PLUS1` | SO-04 (Publiczne Ostrzeżenie): gold 0 → 1 | 56.7 → 🔴 ** 58.8** (`⬆️ +2.1`) | 52.8 | 64.8 | 0.0 | 0.9% | 24.5% | 🟢 ZYSK |
| #10 | `L3_SO-01_COST_MINUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 0 | 56.7 → 🔴 ** 58.6** (`⬆️ +1.9`) | 52.0 | 65.2 | 0.0 | 1.0% | 24.5% | 🟢 ZYSK |
| #11 | `L3_SO-10_HERESY_MINUS1` | SO-10 (Oczyść Miasto): heresy 2 → 1 | 🔴 ** 56.7** | 40.0 | 95.0 | 35.1 | 1.2% | 25.8% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 1 → 2 | 56.7 → 🔴 ** 47.6** (`-9.1`) | 40.5 | 89.5 | 12.8 | 1.1% | 26.2% | ⚪ STRATA/NEUTRALNY |