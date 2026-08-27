[Strona główna](../../../../../README.md) > [v0.24](README.md) > [raport_optymalizacji](raport_optymalizacji.md)

---

# Raport Optymalizacji Balansu (Szalony Audytor) — Wersja v0.24 (Iteracja #2)

**Wersja Poprzednia:** `v0.23` (`94.7 pkt`) → **Nowa Wersja:** `v0.24` (`95.2 pkt`)
**Data:** 2026-08-14 15:53 | **Czas Trwania Iteracji:** 1050.5s | **Zysk Global:** `+0.5 pkt`

## 1. Wprowadzona Zmiana i Wynik Balansu
- **Wybrany Wariant:** `L3_GC-04_COST_MINUS1` — **GC-04 (Informator): cost 1 → 0**
- **Opis Modyfikacji:** Karta `gc-04` (Informator): `cost` → `0`
- **Global Game Balance Score:** 94.7 → 🟢 ** 95.2** (`⬆️ +0.5`) pkt
- **Rozbicie Składów Graczy:**
  - **3p:** 86.2 → 87.8 (`⬆️ +1.6`) pkt
  - **4p:** 98.4 → 98.1 (`-0.3`) pkt
  - **5p:** 99.4 → 99.7 (`⬆️ +0.3`) pkt
- **Kluczowa Telemetria Silnika:**
  - **Średnia Długość Gry:** `5.53 Er` (zakres: 1–9)
  - **Deadlocki (Limit 8/9 Er):** `3.7%` (norma: <15%)
  - **Pas Biedy (Wymuszony brak monety):** `26.6%` (norma: <30%)
  - **Autodafé / partię:** `1.03`
  - **Oskarżenia / partię:** `3.60`

## 2. Ranking Przebadanych Kandydatów w tej Iteracji

| Poz. | ID Wariantu | Nazwa / Opis | Global (baza → test) | 3p | 4p | 5p | Deadlocks % | Pas Biedy % | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| #1 | `L3_GC-04_COST_MINUS1` | GC-04 (Informator): cost 1 → 0 | 94.7 → 🟢 ** 95.2** (`⬆️ +0.5`) | 87.8 | 98.1 | 99.7 | 3.7% | 26.6% | 🌟 ZWYCIĘZCA |