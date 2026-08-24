# ADR-0013: Deterministyczna Gramatyka Kart i Generowanie Tekstów z SSOT

* **Status:** ACCEPTED
* **Data:** 2026-08-23
* **Autorzy:** Antigravity & Designer
* **Dotyczy:** `tools/sync_config.py`, `game_config.yaml`, `game/cards/`, `assets/prototypes/card-editor.html`

---

## 1. Kontekst Problemu
W początkowej fazie projektu opisy efektów na kartach markdown były pisane ręcznie, co prowadziło do rozbieżności między tym, co symulował kod Pythona, a tym, co widniało na kartach do druku (PnP).

---

## 2. Decyzja Projektowa
1. **SSOT jako Jedyne Źródło Prawdy o Efektach:**
   - Plik `game_config.yaml` definiuje wszystkie parametry mechaniczne karty (koszt, złoto, ruch, areszt, oskarżenie, herezja, tagi).
2. **Deterministyczny Generator Tekstów (Card Grammar Engine):**
   - Skrypt `tools/sync_config.py` w sposób deterministyczny przekształca parametry YAML w polskie opisy efektów z zachowaniem poprawnej fleksji gramatycznej (*„1 złoto / 2 złote / 5 sztuk złota”*, *„1 Relikwię / 2 Relikwie”*).
3. **Zakaz ręcznego nadpisywania:**
   - Kategorycznie zabrania się wpisywania w plikach markdown kart (`game/cards/`) mechanik, które nie wynikają wprost ze struktury YAML.

---

## 3. Szczegółowe Uzasadnienie (Game Design & Software Engineering)
* **Zero rozbieżności:** Co widzi symulator, to samo widzi gracz przy stole na karcie PnP.
* **Automatyzacja:** Zmiana kosztu lub parametru w YAML natychmiast aktualizuje opisy we wszystkich 60 plikach kart, katalogu `KATALOG.md` oraz generatorze wizualnym `card-editor.html`.

---

## 4. Niezmienniki Architektoniczne (Invariants)
* 🛑 **ZAKAZ:** Ręcznej edycji sekcji efektu mechanicznego w plikach kart markdown bez odzwierciedlenia w YAML.
* 🛡️ **GWARANCJA:** Uruchomienie `tools/sync_config.py` zapewnia 100% synchronizację między SSOT a kartami PnP.

---

## 5. Konsekwencje
* Pełna transparentność i spójność dokumentacji kart z silnikiem symulacji.
