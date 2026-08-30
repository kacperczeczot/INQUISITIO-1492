# Reguła Projektowa: Bezwzględne Zasady Modyfikacji SSOT (`data/data/game_config.yaml`)

Każdy model AI / asystent pracujący w tym repozytorium **MUSI** bezwzględnie przestrzegać poniższych reguł przy jakiejkolwiek modyfikacji pliku `data/data/game_config.yaml`:

---

## 1. Zakaz Cichej Edycji w Miejscu (Wymagane Podbicie Wersji)
* **Kategorycznie zabrania się** modyfikowania parametrów w `data/data/game_config.yaml` bez jednoczesnego:
  1. **Podbicia wersji:** `version: v1.0-alpha.X` $\rightarrow$ `v1.0-alpha.Y`.
  2. **Aktualizacji daty:** `date: 'YYYY-MM-DD'` na bieżącą datę.
* Wszelkie zmiany bez nowego numeru wersji są traktowane jako błąd krytyczny procedury.

---

## 2. Obowiązkowy Wpis w Patch Notes (`data/playtesting/balance-notes.md`)
* Każda modyfikacja pliku `data/data/game_config.yaml` musi zostać natychmiast odnotowana na samej górze sekcji patch notes w [data/playtesting/balance-notes.md](file:///Users/kacper/Documents/GitHub/INQUISITIO-1492/data/playtesting/balance-notes.md):
  ```markdown
  ### 🟢 Patch v1.0-alpha.X (YYYY-MM-DD) — [Zwięzły opis zmiany]
  - **Wynik 4P:** [Przed → Po] / [Informacja o statusie]
  - **Modyfikacja:** [Dokładny opis zmienionych pól YAML]
  - **Efekt:** [Uzasadnienie projektowe / cel zmiany]
  ```

---

## 3. Obowiązkowa Synchronizacja Całego Repozytorium
* Bezpośrednio po modyfikacji `data/data/game_config.yaml` należy uruchomić skrypt synchronizujący:
  ```bash
  src/.venv/bin/python3 scripts/sync_config.py
  ```
* Skrypt ten automatycznie synchronizuje: `README.md`, `docs/rules/ksiega.md`, `docs/rules/wariant-2p.md`, `docs/rules/hierarchia_balansowania.md`, `docs/rules/slownik.md`, `game/cards/KATALOG.md` oraz `assets/prototypes/card-editor.html`.

---

## 4. Zasada Całkowitego Usuwania Martwych Mechanik (Anti-Dead-Weight)
* **Zakaz maskowania:** Kategorycznie zabrania się dopisywania sztucznych testów lub obejść w audytorach dla parametrów, które są martwe lub przezroczyste (np. warunki progowe $\le$ stan początkowy, brak wpływu na rozgrywkę).
* **Czyste cięcie:** Martwa mechanika musi zostać **całkowicie usunięta** ze wszystkich warstw:
  1. `data/data/game_config.yaml` (SSOT),
  2. Silnik gry (`src/inquisitio/engine/`),
  3. Audytory i narzędzia (`scripts/sim/`, `scripts/sync_config.py`, `scripts/pnp/`),
  4. Dokumentacja referencyjna i zasady (`docs/`),
  5. Testy jednostkowe (`src/tests/`).

---

## 5. Obowiązkowa Weryfikacja Testami
* Przed zakończeniem zadania należy uruchomić pełny zestaw testów:
  ```bash
  python3 -m pytest
  python3 scripts/verify_hygiene.py
  ```
* Wszystkie testy muszą zakończyć się statusem **PASSED** (brak błędów i regresji).

---

## 6. Obowiązkowy Punkt Odniesienia do Genezy Kart (Baseline Genesis Reference)
* **Punkt odniesienia:** Przed każdą edycją kart należy sprawdzić ich oryginalny zamysł w [docs/game/cards/PUNKTY_ODNIESIENIA_GENEZY_TALII.md](file:///Users/kacper/Documents/GitHub/INQUISITIO-1492/docs/game/cards/PUNKTY_ODNIESIENIA_GENEZY_TALII.md) oraz [data/playtesting/baseline_deck_genesis.yaml](file:///Users/kacper/Documents/GitHub/INQUISITIO-1492/data/playtesting/baseline_deck_genesis.yaml).
* **Narzędzie diffa:** Do porównywania bieżących kart z bazą genezy służy narzędzie:
  ```bash
  python3 scripts/sim/compare_with_genesis.py
  ```
* **Twarde limity kart:** Wszelkie zmiany parametrów kart muszą bezwzględnie mieścić się w sztywnych granicach: `cost: 0..5`, `gold: 0..3`, `heresy: 0..3`, `target_heresy: 0..2`, `agents: 0..2`.

