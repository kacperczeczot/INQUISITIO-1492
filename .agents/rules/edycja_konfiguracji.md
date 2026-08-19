# Reguła Projektowa: Bezwzględne Zasady Modyfikacji SSOT (`game_config.yaml`)

Każdy model AI / asystent pracujący w tym repozytorium **MUSI** bezwzględnie przestrzegać poniższych reguł przy jakiejkolwiek modyfikacji pliku `game_config.yaml`:

---

## 1. Zakaz Cichej Edycji w Miejscu (Wymagane Podbicie Wersji)
* **Kategorycznie zabrania się** modyfikowania parametrów w `game_config.yaml` bez jednoczesnego:
  1. **Podbicia wersji:** `version: v1.0-alpha.X` $\rightarrow$ `v1.0-alpha.Y`.
  2. **Aktualizacji daty:** `date: 'YYYY-MM-DD'` na bieżącą datę.
* Wszelkie zmiany bez nowego numeru wersji są traktowane jako błąd krytyczny procedury.

---

## 2. Obowiązkowy Wpis w Patch Notes (`playtesting/balance-notes.md`)
* Każda modyfikacja pliku `game_config.yaml` musi zostać natychmiast odnotowana na samej górze sekcji patch notes w [playtesting/balance-notes.md](file:///Users/kacper/Documents/GitHub/INQUISITIO-1492/playtesting/balance-notes.md):
  ```markdown
  ### 🟢 Patch v1.0-alpha.X (YYYY-MM-DD) — [Zwięzły opis zmiany]
  - **Wynik 4P:** [Przed → Po] / [Informacja o statusie]
  - **Modyfikacja:** [Dokładny opis zmienionych pól YAML]
  - **Efekt:** [Uzasadnienie projektowe / cel zmiany]
  ```

---

## 3. Obowiązkowa Synchronizacja Całego Repozytorium
* Bezpośrednio po modyfikacji `game_config.yaml` należy uruchomić skrypt synchronizujący:
  ```bash
  ./sim/.venv/bin/python3 tools/sync_config.py
  ```
* Skrypt ten automatycznie synchronizuje: `README.md`, `docs/rules/ksiega.md`, `docs/rules/wariant-2p.md`, `docs/rules/hierarchia_balansowania.md`, `docs/rules/slownik.md`, `game/cards/KATALOG.md` oraz `assets/prototypes/card-editor.html`.

---

## 4. Zasada Całkowitego Usuwania Martwych Mechanik (Anti-Dead-Weight)
* **Zakaz maskowania:** Kategorycznie zabrania się dopisywania sztucznych testów lub obejść w audytorach dla parametrów, które są martwe lub przezroczyste (np. warunki progowe $\le$ stan początkowy, brak wpływu na rozgrywkę).
* **Czyste cięcie:** Martwa mechanika musi zostać **całkowicie usunięta** ze wszystkich warstw:
  1. `game_config.yaml` (SSOT),
  2. Silnik gry (`sim/inquisitio/engine/`),
  3. Audytory i narzędzia (`tools/sim/`, `tools/sync_config.py`, `tools/pnp/`),
  4. Dokumentacja referencyjna i zasady (`docs/`),
  5. Testy jednostkowe (`sim/tests/`).

---

## 5. Obowiązkowa Weryfikacja Testami
* Przed zakończeniem zadania należy uruchomić pełny zestaw testów:
  ```bash
  ./sim/.venv/bin/pytest
  ```
* Wszystkie testy muszą zakończyć się statusem **PASSED** (brak błędów i regresji).
