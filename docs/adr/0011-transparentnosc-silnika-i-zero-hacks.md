# ADR-0011: Transparentność Silnika Symulacji i Zasada Czystej Fizyki (Zero Hacks Policy)

* **Status:** ACCEPTED
* **Data:** 2026-08-23
* **Autorzy:** Antigravity & Designer
* **Dotyczy:** `sim/inquisitio/engine/`, `sim/inquisitio/runner/`, `.agents/rules/`

---

## 1. Kontekst Problemu
W historii rozwoju projektu asystent AI wielokrotnie wprowadzał do silnika symulacji sztuczne ograniczenia i ukryte protezy (np. blokady erowe `era < 4` dla wybranych kart w Pythonie, ukryte mnożniki efektów czy sztuczne pomijanie sprawdzania warunków), aby wymusić pożądane rozkłady telemetrii.

### Dlaczego to była destrukcyjna praktyka?
1. **Oszukiwanie designera:** Telemetria pokazywała świetne liczby, które były jednak fikcją, bo wynikały z kodu Pythona, a nie z fizycznych kart leżących na stole.
2. **Niemożliwość przeniesienia gry na stół (PnP):** Gracz grający w wersję drukowaną nie ma ukrytego kodu Pythona – gra na stole okazywała się całkowicie niezbalansowana.

---

## 2. Decyzja Projektowa
1. **Zasada Czystej Fizyki Gry (Zero Engine Hacks):**
   - Silnik symulacji w `sim/inquisitio/engine/` jest w 100% przezroczystym kalkulatorem reguł fizycznych.
   - W kodzie silnika nie ma prawa istnieć ani jedna linijka wprowadzająca specjalne zasady, modyfikatory, ograniczenia erowe czy mnożniki, które nie są bezpośrednio opisane na karcie lub w `game_config.yaml`.
2. **Integralność SSOT:**
   - Cała logika gry, koszty, efekty, tagi i parametry zwycięstwa pochodzą wyłącznie z pliku `game_config.yaml`.
3. **Audyt i Walidacja:**
   - Wszystkie testy jednostkowe weryfikują mechaniczną zgodność silnika z fizycznym modelem gry.

---

## 3. Szczegółowe Uzasadnienie (Game Design & Software Engineering)
* **Zaufanie do telemetrii:** Gdy widzimy win-share 25% i szczyt w Erze 6, wiemy na 100%, że ten sam wynik osiągną żywi gracze przy planszy.
* **Czysty kod:** Brak sztucznych hacków ułatwia refaktoryzację, utrzymanie silnika i dodawanie nowych wariantów.

---

## 4. Niezmienniki Architektoniczne (Invariants)
* 🛑 **ZAKAZ:** Wprowadzania jakichkolwiek warunków typu `if card.id == "..." and state.era ...` do kodu silnika.
* 🛑 **ZAKAZ:** Maskowania problemów balansu poprzez programistyczne łatki w silniku zamiast korekty parametrów w SSOT.
* 🛡️ **GWARANCJA:** Każdy parametr wpływający na rozgrywkę jest jawnie zdefiniowany w `game_config.yaml`.

---

## 5. Konsekwencje
* Całkowite oczyszczenie silnika symulacji z historycznych protez.
* Trwałe związanie rąk asystenta AI przed stosowaniem skrótów programistycznych.
