# Raport Optymalizacji Balansu (Szalony Audytor) — Wersja v0.25 (Iteracja #1)

**Wersja Poprzednia:** `v0.24` (`95.2 pkt`) → **Nowa Wersja:** `v0.25` (`95.3 pkt`)
**Data:** 2026-08-14 16:31 | **Czas Trwania Iteracji:** 917.8s | **Zysk Global:** `+0.1 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu
- **Wybrany Wariant:** `L3_KT-03_GOLD_PLUS1` — **KT-03 (Zakazana Wiedza): gold 0 → 1**
- **Opis Modyfikacji:** Karta `kt-03` (Zakazana Wiedza): `gold` → `1`
- **Global Game Balance Score:** 95.2 → 🟢 ** 95.3** (`⬆️ +0.1`) pkt
- **Rozbicie Składów Graczy:**
  - **3p:** 87.8 → 87.9 (`⬆️ +0.1`) pkt
  - **4p:** 98.1 → 98.2 (`⬆️ +0.1`) pkt
  - **5p:** 99.7 pkt
- **Kluczowa Telemetria Silnika:**
  - **Średnia Długość Gry:** `5.54 Er` (zakres: 1–9)
  - **Deadlocki (Limit 8/9 Er):** `3.8%` (norma: <15%)
  - **Pas Biedy (Wymuszony brak monety):** `26.6%` (norma: <30%)
  - **Autodafé / partię:** `1.03`
  - **Oskarżenia / partię:** `3.61`

## 2. Ranking Przebadanych Kandydatów w tej Iteracji

| Poz. | ID Wariantu | Nazwa / Opis | Global (baza → test) | 3p | 4p | 5p | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_KT-03_GOLD_PLUS1` | KT-03 (Zakazana Wiedza): gold 0 → 1 | 95.2 → 🟢 ** 95.3** (`⬆️ +0.1`) | 87.9 | 98.2 | 99.7 | 3.8% | 26.6% | 🌟 ZWYCIĘZCA |
| #2 | `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–7 → 2–7 | 🟢 ** 95.2** | 88.0 | 98.1 | 99.6 | 3.7% | 26.6% | ⚪ STRATA/NEUTRALNY |