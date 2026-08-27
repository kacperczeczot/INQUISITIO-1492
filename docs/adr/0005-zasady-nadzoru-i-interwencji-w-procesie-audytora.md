[Strona główna](../../README.md) > [adr](README.md) > [0005-zasady-nadzoru-i-interwencji-w-procesie-audytora](0005-zasady-nadzoru-i-interwencji-w-procesie-audytora.md)

---

# ADR-0005: Zasady Ciągłego Nadzoru, Reakcji i Eskalacji Wielowymiarowej Audytora

* **Status:** ACCEPTED
* **Data:** 2026-08-23
* **Autorzy:** Antigravity & Designer
* **Dotyczy:** `tools/sim/audytor_kanonu.py`, procesy asynchroniczne, monitoring CI/CD

---

## 1. Kontekst Problemu
W trakcie wcześniejszych sesji optymalizacyjnych zidentyfikowano następujące nieprawidłowości:
1. **Brak Aktywnego Nadzoru i Reakcji:** Asystent ograniczał się do biernego odczytywania logów z opóźnieniem, zamiast stale kontrolować proces, diagnozować usterki i bezzwłocznie interweniować.
2. **Zapętlenie w 1D (Paraliż Eksploracji):** Audytor po wyczerpaniu zysków z mutacji pojedynczych kart (Faza 1D, plateau ~77 pkt) ponownie generował tę samą pulę atomową z powodu błędu przekazywania nasion (`beam_seeds`), zamiast eskalować do komplementarnych wiązek 2D i 3D.
3. **Ciche Zatrzymanie:** Procesy audytora potrafiły zakończyć bieg lub utknąć na deadlocku bez natychmiastowego wznowienia przez asystenta.

---

## 2. Decyzja Projektowa: Standard „MONITORUJ, KONTROLUJ I REAGUJ”

Wprowadza się formalne zasady nadzoru nad audytorem:

1. **Obowiązek Stałego Monitoringu:**
   - Asystent ma obowiązek kontrolować stan procesów co 60 sekund w trakcie działania optymalizacji.
   - Weryfikacja obejmuje: aktywność PID-ów roboczych, prędkość przetwarzania (`zad/s`), bieżącego lidera i błędy w logu `audytor_live.log`.

2. **Zasada Natychmiastowej Interwencji przy Stagnacji (Plateau Threshold):**
   - Jeśli po 2 kolejnych iteracjach przesiewu 1D żaden kandydat nie podnosi wyniku słabych setupów, audytor **MANDATORYCZNIE eskaluje do Fazy 2D i 3D**.
   - Faza 2D generuje **pary antagonistyczno-synergiczne** (np. Nerf dominanta KT/GC + Buff niedoreprezentowanego SO/KB).

3. **Naprawa Kodu i Ciągłość Pracy:**
   - Wykrycie błędu w skryptach symulacji lub audytora wymaga natychmiastowej poprawki w kodzie źródłowym i ponownego uruchomienia procesu bez oczekiwania na kolejne monity użytkownika.

---

## 3. Szczegółowe Uzasadnienie
* **Wielowymiarowość Przestrzeni Balansu:** W grze 4-osobowej z 5 asymetrycznymi frakcjami zmiana pojedynczego parametru rzadko wystarcza do zbalansowania trudnych setupów (`4p-core`, `4p-no-kabala`). Równowaga wymaga jednoczesnego zestrojenia co najmniej dwóch wektorów ekonomicznych (np. dochód Inkwizycji + koszt pieczęci Kabały).
* **Efektywność Czasowa:** Automatyczna eskalacja eliminuje marnowanie setek cykli procesora na testowanie wariantów, które osiągnęły lokalne optimum.

---

## 4. Niezmienniki (Invariants)
* 🛡️ `audytor_kanonu.py` musi zawsze poprawnie inicjalizować `beam_seeds` z etapu poprzedniego i generować mutacje kombinowane.
* 🛡️ Wszelkie zatrzymania procesu muszą być natychmiast diagnozowane, korygowane i raportowane z planem wznowienia.
