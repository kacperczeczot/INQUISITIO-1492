# Raport Optymalizacji Balansu (Szalony Audytor — Progressive Beam) — Wersja v0.44 (Iteracja #2, Faza 1D)

**Wersja Poprzednia:** `v0.43` (`65.5 pkt`) → **Nowa Wersja:** `v0.44` (`73.8 pkt`)
**Data:** 2026-08-16 02:03 | **Czas Trwania Iteracji:** 1148.9s | **Zysk Global:** `+8.3 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu
- **Wybrany Wariant (1D):** `L3_KT-10_HERESY_PLUS1` — **KT-10 (Pieczęć Salomona): heresy 0 → 1**
- **Opis Modyfikacji:** Karta `kt-10` (Pieczęć Salomona): `heresy` → `1`
- **Global Game Balance Score:** 65.5 → 🟠 ** 73.8** (`⬆️ +8.3`) pkt
- **Rozbicie Składów Graczy:**
  - **3p:** 55.9 → 72.5 (`⬆️ +16.6`) pkt
  - **4p:** 75.2 → 75.1 (`-0.1`) pkt
  - **5p:** 0.0 pkt
- **Kluczowa Telemetria Silnika:**
  - **Średnia Długość Gry:** `5.65 Er`
  - **Deadlocki (Limit Er):** `1.1%` (norma: <5%)
  - **Pas Biedy (Złoto):** `24.9%` (norma: <30%)
  - **Autodafé / partię:** `0.55`
  - **Oskarżenia / partię:** `3.61`

## 2. Ranking Przebadanych Kandydatów w tej Iteracji (TOP Finaliści)

| Poz. | ID Wariantu | Nazwa / Opis | Global (baza → test) | 3p | 4p | 5p | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_KT-10_HERESY_PLUS1` | KT-10 (Pieczęć Salomona): heresy 0 → 1 | 65.5 → 🟠 ** 73.8** (`⬆️ +8.3`) | 72.5 | 75.1 | 0.0 | 1.1% | 24.9% | 🌟 ZWYCIĘZCA |
| #2 | `L2_KB_ERA_MINUS1` | Korona Era: 5/5/5 → 4/4/4 | 65.5 → 🟠 ** 69.8** (`⬆️ +4.3`) | 54.4 | 85.1 | 0.0 | 0.9% | 24.9% | 🟢 ZYSK |
| #3 | `L3_SO-03_TARGET_HERESY_MINUS1` | SO-03 (Podejrzenie): target_heresy 1 → 0 | 65.5 → 🟠 ** 69.1** (`⬆️ +3.6`) | 55.2 | 83.0 | 0.0 | 0.9% | 25.1% | 🟢 ZYSK |
| #4 | `L3_KT-08_HERESY_PLUS1` | KT-08 (Areszt Wiedzy): heresy 0 → 1 | 65.5 → 🟠 ** 68.5** (`⬆️ +3.0`) | 55.8 | 81.3 | 0.0 | 1.0% | 24.9% | 🟢 ZYSK |
| #5 | `L3_KT-07_HERESY_PLUS1` | KT-07 (Archiwum Ukryte): heresy 0 → 1 | 65.5 → 🟠 ** 68.2** (`⬆️ +2.7`) | 56.0 | 80.5 | 0.0 | 1.0% | 24.9% | 🟢 ZYSK |
| #6 | `L3_KT-09_HERESY_PLUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 2 | 65.5 → 🟠 ** 67.7** (`⬆️ +2.2`) | 58.1 | 77.2 | 0.0 | 1.1% | 24.9% | 🟢 ZYSK |
| #7 | `L3_CAA-09_COST_PLUS1` | CAA-09 (Kurier Relikwii): cost 2 → 3 | 65.5 → 🟠 ** 67.1** (`⬆️ +1.6`) | 55.7 | 78.4 | 0.0 | 1.0% | 25.2% | 🟢 ZYSK |
| #8 | `L3_CAA-03_COST_PLUS1` | CAA-03 (Cień na Rynku): cost 0 → 1 | 65.5 → 🟠 ** 66.3** (`⬆️ +0.8`) | 56.3 | 76.4 | 0.0 | 0.9% | 25.2% | 🟢 ZYSK |
| #9 | `L3_CAA-02_GOLD_PLUS1` | CAA-02 (Złoto z Kryjówki): gold 2 → 3 | 65.5 → 🟠 ** 65.8** (`⬆️ +0.3`) | 54.8 | 76.9 | 0.0 | 1.0% | 25.0% | 🟢 ZYSK |
| #10 | `L3_SO-01_COST_PLUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 2 | 65.5 → 🟠 ** 65.7** (`⬆️ +0.2`) | 55.2 | 76.2 | 0.0 | 1.0% | 25.8% | 🟢 ZYSK |
| #11 | `L3_KT-03_HERESY_PLUS1` | KT-03 (Zakazana Wiedza): heresy 1 → 2 | 65.5 → 🟠 ** 64.2** (`-1.3`) | 56.9 | 71.5 | 0.0 | 1.0% | 24.9% | ⚪ STRATA/NEUTRALNY |
| #12 | `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 1 → 2 | 65.5 → 🔴 ** 53.2** (`-12.3`) | 55.8 | 87.8 | 16.1 | 1.0% | 25.9% | ⚪ STRATA/NEUTRALNY |