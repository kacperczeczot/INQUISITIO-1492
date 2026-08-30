# 🏛️ Punkty Odniesienia i Geneza Talii (Kanon Kart w Momencie Utworzenia)

> **Cel Dokumentu:** Trwały punkt odniesienia dla projektanta gry, audytora i systemu balansu.
> Pozwala w ułamku sekundy zweryfikować, jak dana karta została pierwotnie zaprojektowana w momencie jej powstania oraz jakie odchylenia wprowadzono w trakcie strojenia parametrów.

## 📜 Kamienie Milowe Powstania Talii:
1. **Wersja `v0.0` (13 sierpnia 2026):** Powstanie bazowych kart **`01 .. 10`** dla 5 frakcji (50 kart).
2. **Wersja `v0.40` (15 sierpnia 2026):** Refaktor i wdrożenie 10 kart Edyktów Ery Kroniki Dziejów (`time-01 .. 10`).
3. **Wersja `v0.76` (17 sierpnia 2026):** Wprowadzenie kart **`11` i `12`** dla 5 frakcji (rozszerzenie talii do 70 kart).

---

## ⛪ Święte Oficjum (`so`)

| ID | Nazwa | Typ / Rola | Koszt | Złoto | Herezja | Rywal H | Działanie Bazowe | Geneza |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| `so-01` | **Patrol Familiariuszy** | akcja | 1 zł | — | +0H | — | `move_agent` | `v0.0` |
| `so-02` | **Skarbiec Trybunału** | akcja | 1 zł | 3 | +0H | — | `gain_gold` | `v0.0` |
| `so-03` | **Podejrzenie** | akcja | 2 zł | — | +0H | 1 | `frame_rival` | `v0.0` |
| `so-04` | **Publiczne Ostrzeżenie** | akcja | 1 zł | — | +0H | — | `send_inquisitor` | `v0.0` |
| `so-05` | **Wezwanie do Trybunału** | reakcja | 0 zł | — | +0H | 1 | `frame_rival` | `v0.0` |
| `so-06` | **Areszt Trybunalski** | akcja | 2 zł | — | +0H | — | `arrest` | `v0.0` |
| `so-07` | **Przesłuchanie Oficjum** | akcja | 2 zł | — | +0H | — | `interrogate` | `v0.0` |
| `so-08` | **Nasłanie Inkwizytora** | akcja | 1 zł | — | +0H | — | `send_inquisitor` | `v0.0` |
| `so-09` | **Świadek Koronny** | akcja | 2 zł | — | +0H | — | `creates_hook` | `v0.0` |
| `so-10` | **Oczyść Miasto** | signature | 5 zł | — | +2H | — | `autodafe` | `v0.0` |
| `so-11` | **Dekret Czystości Wiary** | akcja | 1 zł | 1 | +0H | 1 | `frame_rival` | `v0.76` |
| `so-12` | **Straż Trybunalska** | akcja | 1 zł | 1 | +0H | — | `move_agent` | `v0.76` |

## 🕌 Cienie Al-Andalus (`caa`)

| ID | Nazwa | Typ / Rola | Koszt | Złoto | Herezja | Rywal H | Działanie Bazowe | Geneza |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| `caa-01` | **Przejście Podziemiami** | akcja | 0 zł | — | +0H | — | `move_agent` | `v0.0` |
| `caa-02` | **Złoto z Kryjówki** | akcja | 1 zł | 2 | +0H | — | `gain_gold` | `v0.0` |
| `caa-03` | **Cień na Rynku** | akcja | 0 zł | — | +1H | — | `move_agent` | `v0.0` |
| `caa-04` | **Fałszywy Trop** | akcja | 1 zł | — | +0H | 1 | `frame_rival` | `v0.0` |
| `caa-05` | **Ukryty Kurier** | akcja | 1 zł | — | +0H | — | `evacuate_relic` | `v0.0` |
| `caa-06` | **Ucieczka z Lochów** | akcja | 2 zł | — | +1H | — | `move_agent` | `v0.0` |
| `caa-07` | **Szantaż Bractwa** | akcja | 1 zł | — | +0H | — | `creates_hook` | `v0.0` |
| `caa-08` | **Kaptur Nocy** | akcja | 2 zł | — | +1H | — | `move_agent` | `v0.0` |
| `caa-09` | **Kurier Relikwii** | akcja | 2 zł | — | +0H | — | `move_agent` | `v0.0` |
| `caa-10` | **Echo Alhambry** | signature | 1 zł | — | +1H | — | `evacuate_relic` | `v0.0` |
| `caa-11` | **Nocna Zmiana Warty** | akcja | 1 zł | — | +0H | — | `move_agent` | `v0.76` |
| `caa-12` | **Skrytka w Murach** | akcja | 0 zł | 2 | +1H | — | `gain_gold` | `v0.76` |

## 👑 Korona Borgiowie (`kb`)

| ID | Nazwa | Typ / Rola | Koszt | Złoto | Herezja | Rywal H | Działanie Bazowe | Geneza |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| `kb-01` | **Rozkaz Dworu** | akcja | 1 zł | — | +1H | — | `move_agent` | `v0.0` |
| `kb-02` | **Pobór Podatków** | akcja | 1 zł | 2 | +0H | — | `gain_gold` | `v0.0` |
| `kb-03` | **Plotka Dworska** | akcja | 1 zł | — | +0H | 1 | `frame_rival` | `v0.0` |
| `kb-04` | **Faworyt Dworu** | akcja | 2 zł | — | +1H | — | `creates_hook` | `v0.0` |
| `kb-05` | **List Żelazny** | akcja | 2 zł | — | +0H | — | `creates_hook` | `v0.0` |
| `kb-06` | **Areszt Królewski** | akcja | 1 zł | — | +0H | — | `arrest` | `v0.0` |
| `kb-07` | **Szantaż Pieczęcią** | akcja | 2 zł | — | +0H | — | `creates_hook` | `v0.0` |
| `kb-08` | **Przekupstwo Sędziego** | akcja | 2 zł | — | +0H | — | `creates_hook` | `v0.0` |
| `kb-09` | **Dekret Królewski** | signature | 3 zł | — | +1H | — | `creates_hook` | `v0.0` |
| `kb-10` | **Pieczęć Korony** | signature | 2 zł | — | +2H | — | `check_victory` | `v0.0` |
| `kb-11` | **Tajny Emisariusz** | akcja | 1 zł | 1 | +0H | — | `move_agent` | `v0.76` |
| `kb-12` | **Szantaż Salonowy** | akcja | 1 zł | — | +0H | — | `creates_hook` | `v0.76` |

## 📜 Kabała z Toledo (`kt`)

| ID | Nazwa | Typ / Rola | Koszt | Złoto | Herezja | Rywal H | Działanie Bazowe | Geneza |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| `kt-01` | **Rytuał Przejścia** | akcja | 1 zł | — | +0H | — | `move_agent` | `v0.0` |
| `kt-02` | **Transmutacja Złota** | akcja | 1 zł | 2 | +0H | — | `gain_gold` | `v0.0` |
| `kt-03` | **Zakazana Wiedza** | akcja | 0 zł | — | +1H | — | `grant_fragment` | `v0.0` |
| `kt-04` | **Zwierciadło Herezji** | akcja | 1 zł | — | +0H | 1 | `frame_rival` | `v0.0` |
| `kt-05` | **Wskazówka Cyklu** | akcja | 1 zł | — | +0H | — | `grant_fragment` | `v0.0` |
| `kt-06` | **Przesłuchanie Imienia** | akcja | 2 zł | — | +0H | — | `interrogate` | `v0.0` |
| `kt-07` | **Archiwum Ukryte** | akcja | 1 zł | — | +1H | — | `creates_hook` | `v0.0` |
| `kt-08` | **Areszt Wiedzy** | akcja | 1 zł | — | +0H | — | `arrest` | `v0.0` |
| `kt-09` | **Fragment Kodeksu** | akcja | 2 zł | — | +1H | — | `grant_fragment` | `v0.0` |
| `kt-10` | **Pieczęć Salomona** | signature | 2 zł | — | +1H | — | `check_victory` | `v0.0` |
| `kt-11` | **Medytacja Sefirot** | akcja | 1 zł | 1 | +0H | — | `heresy_adjust` | `v0.76` |
| `kt-12` | **Strażnik Archiwum** | akcja | 0 zł | — | +1H | — | `move_agent` | `v0.76` |

## 🗡️ Gildia Cieni (`gc`)

| ID | Nazwa | Typ / Rola | Koszt | Złoto | Herezja | Rywal H | Działanie Bazowe | Geneza |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| `gc-01` | **Przekupiony Strażnik** | akcja | 1 zł | — | +1H | — | `move_agent` | `v0.0` |
| `gc-02` | **Czarny Rynek** | akcja | 1 zł | 3 | +1H | — | `gain_gold` | `v0.0` |
| `gc-03` | **Podrzucenie Księgi** | akcja | 1 zł | — | +0H | 1 | `frame_rival` | `v0.0` |
| `gc-04` | **Informator** | akcja | 0 zł | — | +1H | — | `creates_hook` | `v0.0` |
| `gc-05` | **Fałszywy Świadek** | reakcja | 0 zł | — | +0H | — | `frame_rival` | `v0.0` |
| `gc-06` | **Szantaż** | akcja | 2 zł | — | +0H | — | `creates_hook` | `v0.0` |
| `gc-07` | **Skrytobójstwo** | akcja | 2 zł | — | +0H | — | `arrest` | `v0.0` |
| `gc-08` | **Zatrute Złoto** | akcja | 2 zł | 1 | +0H | 1 | `gain_gold` | `v0.0` |
| `gc-09` | **Lista Dłużników** | akcja | 2 zł | — | +0H | — | `creates_hook` | `v0.0` |
| `gc-10` | **Upadek Domu** | signature | 4 zł | — | +1H | — | `creates_hook` | `v0.0` |
| `gc-11` | **Fałszywe Świadectwo Cechu** | akcja | 1 zł | — | +0H | 1 | `frame_rival` | `v0.76` |
| `gc-12` | **Złodziejski Zwiad** | akcja | 0 zł | 1 | +1H | — | `move_agent` | `v0.76` |

---

## 🛠️ Jak korzystać z Punktów Odniesienia przy Edycji Kart?

1. **Porównanie z bazą:** Przed każdą modyfikacją karty w `game_config.yaml` uruchom skrypt:
   ```bash
   python3 scripts/sim/compare_with_genesis.py
   ```
2. **Tożsamość karty:** Jeśli karta taktyczna oddala się zbyt daleko od swojej roli bazowej (np. dostaje złoto lub traci swój unikalny mechanizm), należy zweryfikować, czy zmiana nie niszczy zamysłu Game Designu.
3. **Twarde granice:** Wszelkie zmiany muszą mieścić się w limitach: `cost: 0..5`, `gold: 0..3`, `heresy: 0..3`, `target_heresy: 0..2`.
