# Raport Optymalizacji Balansu (Szalony Audytor) — Wersja v0.29 (Iteracja #3)

**Wersja Poprzednia:** `v0.28` (`96.2 pkt`) → **Nowa Wersja:** `v0.29` (`96.5 pkt`)
**Data:** 2026-08-14 20:18 | **Czas Trwania Iteracji:** 939.6s | **Zysk Global:** `+0.3 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu
- **Wybrany Wariant:** `L3_CAA-01_COST_MINUS1` — **CAA-01 (Przejście Podziemiami): cost 1 → 0**
- **Opis Modyfikacji:** Karta `caa-01` (Przejście Podziemiami): `cost` → `0`
- **Global Game Balance Score:** 96.2 → 🟢 ** 96.5** (`⬆️ +0.3`) pkt
- **Rozbicie Składów Graczy:**
  - **3p:** 91.5 → 91.7 (`⬆️ +0.2`) pkt
  - **4p:** 98.1 → 98.3 (`⬆️ +0.2`) pkt
  - **5p:** 98.9 → 99.4 (`⬆️ +0.5`) pkt
- **Kluczowa Telemetria Silnika:**
  - **Średnia Długość Gry:** `5.51 Er` (zakres: 1–10)
  - **Deadlocki (Limit 8/9 Er):** `1.1%` (norma: <15%)
  - **Pas Biedy (Wymuszony brak monety):** `26.1%` (norma: <30%)
  - **Autodafé / partię:** `1.02`
  - **Oskarżenia / partię:** `3.58`

## 2. Ranking Przebadanych Kandydatów w tej Iteracji

| Poz. | ID Wariantu | Nazwa / Opis | Global (baza → test) | 3p | 4p | 5p | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-01_COST_MINUS1` | CAA-01 (Przejście Podziemiami): cost 1 → 0 | 96.2 → 🟢 ** 96.5** (`⬆️ +0.3`) | 91.7 | 98.3 | 99.4 | 1.1% | 26.1% | 🌟 ZWYCIĘZCA |