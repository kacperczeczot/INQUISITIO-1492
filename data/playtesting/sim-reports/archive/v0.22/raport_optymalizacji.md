# Raport Optymalizacji Balansu (Szalony Audytor) — Wersja v0.22 (Iteracja #1)

**Wersja Poprzednia:** `v0.21` (`92.9 pkt`) → **Nowa Wersja:** `v0.22` (`94.4 pkt`)
**Data:** 2026-08-14 15:05 | **Czas Trwania Iteracji:** 577.1s | **Zysk Global:** `+1.5 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu
- **Wybrany Wariant:** `L3_CAA-10_COST_MINUS1` — **CAA-10 (Echo Alhambry): cost 1 → 0**
- **Opis Modyfikacji:** Karta `caa-10` (Echo Alhambry): `cost` → `0`
- **Global Game Balance Score:** 92.9 → 🟢 ** 94.4** (`⬆️ +1.5`) pkt
- **Rozbicie Składów Graczy:**
  - **3p:** 87.2 → 88.0 (`⬆️ +0.8`) pkt
  - **4p:** 93.0 → 95.9 (`⬆️ +2.9`) pkt
  - **5p:** 98.5 → 99.3 (`⬆️ +0.8`) pkt
- **Kluczowa Telemetria Silnika:**
  - **Średnia Długość Gry:** `5.59 Er` (zakres: 1–9)
  - **Deadlocki (Limit 8/9 Er):** `4.1%` (norma: <15%)
  - **Pas Biedy (Wymuszony brak monety):** `27.6%` (norma: <30%)
  - **Autodafé / partię:** `1.04`
  - **Oskarżenia / partię:** `3.56`

## 2. Ranking Przebadanych Kandydatów w tej Iteracji

| Poz. | ID Wariantu | Nazwa / Opis | Global (baza → test) | 3p | 4p | 5p | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_CAA-10_COST_MINUS1` | CAA-10 (Echo Alhambry): cost 1 → 0 | 92.9 → 🟢 ** 94.4** (`⬆️ +1.5`) | 88.0 | 95.9 | 99.3 | 4.1% | 27.6% | 🌟 ZWYCIĘZCA |
| #2 | `L3_GC-07_COST_MINUS1` | GC-07 (Skrytobójstwo): cost 2 → 1 | 92.9 → 🟢 ** 94.0** (`⬆️ +1.1`) | 88.1 | 95.1 | 98.8 | 3.9% | 28.1% | 🟢 ZYSK |
| #3 | `L3_CAA-02_COST_MINUS1` | CAA-02 (Złoto z Kryjówki): cost 1 → 0 | 92.9 → 🟢 ** 93.9** (`⬆️ +1.0`) | 86.2 | 96.2 | 99.3 | 4.0% | 27.7% | 🟢 ZYSK |
| #4 | `L3_GC-02_HERESY_PLUS1` | GC-02 (Czarny Rynek): heresy 0 → 1 | 92.9 → 🟢 ** 93.4** (`⬆️ +0.5`) | 85.5 | 95.5 | 99.1 | 3.9% | 28.8% | 🟢 ZYSK |
| #5 | `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 92.9 → 🟢 ** 93.3** (`⬆️ +0.4`) | 85.6 | 95.3 | 98.9 | 4.4% | 29.6% | 🟢 ZYSK |