[Strona główna](../../README.md) > [adr](README.md) > [0006-standard-pelnych-talii-i-eliminacja-warstwowosci](0006-standard-pelnych-talii-i-eliminacja-warstwowosci.md)

---

# ADR-0006: Standard Pełnych Talii (Full Deck Paradigm) i Eliminacja Warstwowości

* **Status:** ACCEPTED
* **Data:** 2026-08-23
* **Autorzy:** Antigravity & Designer
* **Dotyczy:** `sim/inquisitio/engine/`, `sim/inquisitio/cards/`, `game_config.yaml`, `docs/rules/`

---

## 1. Kontekst Problemu
We wczesnych fazach prototypowania i testów jednostkowych wprowadzono koncepcję „warstw zawartości” (Warstwa A: 6 kart podstawowych; Warstwa B: mechaniki aresztowań i haków; Warstwa C: pełne 12 kart ze specjalnymi sygnaturami i kartami edyktów czasu).

### Dlaczego podział warstwowy stał się problemem?
1. **Zaburzenie logiki fizycznej planszówki:** W docelowej grze pudełkowej gracz nie dzieli talii na sztuczne podzbiory – operuje na pełnej talii frakcyjnej od 1. tury.
2. **Podwójny kod i ukryte wyjątki:** W silniku symulacji namnożyły się warunki typu `if state.layer == "C"`, które ukrywały rzeczywiste zachowanie kart i tworzyły asymetrię między testami a pełną grą.
3. **Zafałszowanie telemetrii:** Badanie balansu na wycinkach talii (A/B) dawało mylne wnioski, które nie przekładały się na pełną grę 4P/5P.

---

## 2. Decyzja Projektowa
1. **Całkowita likwidacja pojęcia warstw (A/B/C) w silniku symulacji, loaderze kart i pliku konfiguracyjnym SSOT.**
2. **Kanon Pełnej Gry (Full Deck Paradigm):**
   - Każda talia frakcyjna składa się ze zdefiniowanego, stałego zestawu unikalnych kart fizycznych.
   - Talia Kroniki Dziejów (Time Deck) jest integralną częścią każdej pełnej rozgrywki i odkrywa wydarzenia zgodnie z ustaloną częstotliwością.
   - Wszystkie reguły systemowe (aresztowania, procesy, werdykty, Autodafé, haki) działają w pełnej formule od samego początku partii.

---

## 3. Szczegółowe Uzasadnienie (Game Design)
* **Jednolity standard mentalny gracza:** Zasady gry są spójne, czytelne i nie wymagają przyswajania „wariantów etapowych”.
* **Czysty silnik:** Usunięcie przełączników warstw upraszcza architekturę kodu i eliminuje ryzyko, że mechanika działa inaczej w testach niż w symulacji wielkoskalowej.
* **Autentyczność symulacji:** Wyniki telemetrii i macierze win-share w 100% odzwierciedlają doświadczenie graczy przy stole z kompletnymi komponentami.

---

## 4. Niezmienniki Architektoniczne (Invariants)
* 🛑 **ZAKAZ:** Wprowadzania flag warstwowych (`layer`, `max_layer`, `is_layer_a`) do silnika gry i kart w `game_config.yaml`.
* 🛡️ **GWARANCJA:** Wszystkie testy jednostkowe i audyty balansu są przeprowadzane wyłącznie na pełnych, kompletnych taliach.

---

## 5. Konsekwencje
* Usunięto atrybut `layer` ze wszystkich 60 kart w `game_config.yaml`.
* Uproszczono moduły `loader.py`, `win.py`, `turn.py`, `verdict.py` oraz `registry.py`.
* Wszystkie frakcje startują z pełną pulą taktyczną.
