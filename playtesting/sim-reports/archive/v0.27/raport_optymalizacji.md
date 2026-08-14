# Raport Optymalizacji Balansu (Szalony Audytor) — Wersja v0.27 (Iteracja #3)

**Wersja Poprzednia:** `v0.26` (`95.6 pkt`) → **Nowa Wersja:** `v0.27` (`96.1 pkt`)
**Data:** 2026-08-14 17:02 | **Czas Trwania Iteracji:** 867.0s | **Zysk Global:** `+0.5 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu
- **Wybrany Wariant:** `L1_MAX_ERAS_PLUS1` — **Limit Er: 9 → 10**
- **Opis Modyfikacji:** Limit Er: offset +1 (nowy: 10)
- **Global Game Balance Score:** 95.6 → 🟢 ** 96.1** (`⬆️ +0.5`) pkt
- **Rozbicie Składów Graczy:**
  - **3p:** 89.7 → 91.3 (`⬆️ +1.6`) pkt
  - **4p:** 97.9 pkt
  - **5p:** 99.2 pkt
- **Kluczowa Telemetria Silnika:**
  - **Średnia Długość Gry:** `5.52 Er` (zakres: 1–10)
  - **Deadlocki (Limit 8/9 Er):** `1.1%` (norma: <15%)
  - **Pas Biedy (Wymuszony brak monety):** `26.5%` (norma: <30%)
  - **Autodafé / partię:** `1.03`
  - **Oskarżenia / partię:** `3.57`

## 2. Ranking Przebadanych Kandydatów w tej Iteracji

| Poz. | ID Wariantu | Nazwa / Opis | Global (baza → test) | 3p | 4p | 5p | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| #1 | `L1_MAX_ERAS_PLUS1` | Limit Er: 9 → 10 | 95.6 → 🟢 ** 96.1** (`⬆️ +0.5`) | 91.3 | 97.9 | 99.2 | 1.1% | 26.5% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KT-04_COST_MINUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 0 | 95.6 → 🟢 ** 95.9** (`⬆️ +0.3`) | 90.6 | 98.1 | 98.9 | 2.9% | 26.4% | 🟢 ZYSK |
| #3 | `L3_KT-01_COST_MINUS1` | KT-01 (Rytuał Przejścia): cost 1 → 0 | 95.6 → 🟢 ** 95.9** (`⬆️ +0.3`) | 90.5 | 98.0 | 99.2 | 2.9% | 26.4% | 🟢 ZYSK |