[Strona główna](../../../../../README.md) > [v0.28](README.md) > [raport_optymalizacji](raport_optymalizacji.md)

---

# Raport Optymalizacji Balansu (Szalony Audytor) — Wersja v0.28 (Iteracja #4)

**Wersja Poprzednia:** `v0.27` (`96.1 pkt`) → **Nowa Wersja:** `v0.28` (`96.2 pkt`)
**Data:** 2026-08-14 17:17 | **Czas Trwania Iteracji:** 910.7s | **Zysk Global:** `+0.1 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu
- **Wybrany Wariant:** `L3_KT-04_COST_MINUS1` — **KT-04 (Zwierciadło Herezji): cost 1 → 0**
- **Opis Modyfikacji:** Karta `kt-04` (Zwierciadło Herezji): `cost` → `0`
- **Global Game Balance Score:** 96.1 → 🟢 ** 96.2** (`⬆️ +0.1`) pkt
- **Rozbicie Składów Graczy:**
  - **3p:** 91.3 → 91.5 (`⬆️ +0.2`) pkt
  - **4p:** 97.9 → 98.1 (`⬆️ +0.2`) pkt
  - **5p:** 99.2 → 98.9 (`-0.3`) pkt
- **Kluczowa Telemetria Silnika:**
  - **Średnia Długość Gry:** `5.52 Er` (zakres: 1–10)
  - **Deadlocki (Limit 8/9 Er):** `1.1%` (norma: <15%)
  - **Pas Biedy (Wymuszony brak monety):** `26.4%` (norma: <30%)
  - **Autodafé / partię:** `1.02`
  - **Oskarżenia / partię:** `3.58`

## 2. Ranking Przebadanych Kandydatów w tej Iteracji

| Poz. | ID Wariantu | Nazwa / Opis | Global (baza → test) | 3p | 4p | 5p | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_KT-04_COST_MINUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 0 | 96.1 → 🟢 ** 96.2** (`⬆️ +0.1`) | 91.5 | 98.1 | 98.9 | 1.1% | 26.4% | 🌟 ZWYCIĘZCA |
| #2 | `L3_KT-10_COST_MINUS1` | KT-10 (Pieczęć Salomona): cost 1 → 0 | 96.1 → 🟢 ** 96.2** (`⬆️ +0.1`) | 91.4 | 98.0 | 99.1 | 1.1% | 26.4% | 🟢 ZYSK |
| #3 | `L3_KT-02_COST_MINUS1` | KT-02 (Transmutacja Złota): cost 1 → 0 | 🟢 ** 96.1** | 91.4 | 98.0 | 99.0 | 1.1% | 26.4% | ⚪ STRATA/NEUTRALNY |
| #4 | `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 🟢 ** 96.1** | 91.0 | 98.0 | 99.4 | 1.1% | 26.8% | ⚪ STRATA/NEUTRALNY |