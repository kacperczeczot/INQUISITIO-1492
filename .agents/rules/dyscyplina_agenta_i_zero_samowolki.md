# Reguła Projektowa: Dyscyplina Agenta, Zakaz Samowolki i Matematyczna Walidacja

Każdy model AI / asystent pracujący w tym repozytorium **MUSI** bezwzględnie przestrzegać poniższych reguł operacyjnych:

---

## 1. Bezwzględny Tryb Konsultacyjny (Zero Samowolki)
- **Zakaz wyrywania się przed szereg:** Asystentowi kategorycznie zabrania się modyfikowania plików `game_config.yaml`, kodu silnika (`sim/`), skryptów audytora czy dokumentacji w odpowiedzi na luźne pytanie, hipotezę lub dyskusję.
- **Forma odpowiedzi:** Na pytania dotyczące balansu asystent odpowiada **WYŁĄCZNIE analizą, diagnozą i propozycją wariantów do wyboru**.
- **Warunek wdrożenia:** Modyfikacja kodu lub parametrów może nastąpić **WYŁĄCZNIE po wyraźnym poleceniu użytkownika** (np. *„wprowadź”*, *„zastosuj”*, *„napraw”*, *„wykonaj”*).

---

## 2. Obowiązkowa Weryfikacja Matematyczna i Fizyczna (Math Check)
Przed przedstawieniem jakiejkolwiek propozycji zmiany parametrów zwycięstwa lub kosztu kart asystent **MUSI** przeprowadzić audyt fizyczny talii:
1. **Liczba kart w talii vs wymóg zwycięstwa:**
   - Zakaz podnoszenia wymogu (np. `decrees: 3`), jeśli talia fizycznie zawiera mniejszą liczbę kart z danym efektem (np. 2 karty dekretu w talii Korony).
2. **Relacja zysku do darmowej Akcji Gospodarczej:**
   - Karta ekonomiczna musi oferować wyraźny zysk taktyczny nad pasywnym pobraniem złota (+1 zł / +2 zł na Rynku).
3. **Pasma i sygnatury:**
   - Zakaz usuwania efektów stabilizujących, jeśli finiszer sam z siebie wyrzuca frakcję z wymaganego pasma.

---

## 3. Zgodność z Konstytucją ADR (ADR-0001 do ADR-0015)
- Każda propozycja musi być w 100% zgodna z aktywnymi rekordami ADR w `docs/adr/`.
- Zakaz ponownego proponowania rozwiązań, które zostały formalnie odrzucone (np. sztuczne bramki `era >= X`, manipulacja liczbą pionków na gracza czy cięcie talii na warstwy).

---

## 4. Rygor Procesowy i Integralność Dokumentacji
- Każda zatwierdzona zmiana parametrów w `game_config.yaml` wymaga:
  1. Podbicia wersji `v1.0-alpha.X` $\to$ `v1.0-alpha.Y` i aktualizacji daty.
  2. Rzetelnego wpisu w `playtesting/balance-notes.md` (bez cenzury i pomijania faktów).
  3. Uruchomienia `./sim/.venv/bin/python3 tools/sync_config.py`.
  4. Weryfikacji 100% testów `./sim/.venv/bin/pytest`.

---

## 5. Protokół Samonaprawy i Natychmiastowej Aktualizacji Reguł (Continuous Rule Codification)
- **Obowiązkowa reakcja na błąd:** Jeśli w toku pracy pojawi się jakikolwiek błąd, pomyłka, regresja, niezrozumienie intencji użytkownika lub próba pójścia na skrót ze strony asystenta AI, asystent ma **bezwzględny obowiązek natychmiastowego zaktualizowania i zaostrzenia odpowiedniego pliku w `.agents/rules/` lub utworzenia/uzupełnienia rekordu w `docs/adr/`**.
- **Zakaz powtarzania błędów:** Każde upomnienie ze strony użytkownika musi zostać w tym samym kroku przekształcone w formalną, trwałą regułę systemową, aby błąd nigdy więcej się nie powtórzył.

---

## 6. Obowiązkowy Proces Monitorująco-Reagujący (Watchdog Schedule)
- **Zakaz biernego oczekiwania:** Przy uruchomieniu jakiegokolwiek długotrwałego procesu w tle (np. audytor kanonu, wielogodzinna symulacja), asystent ma **bezwzględny obowiązek natychmiastowego ustawienia cyklicznego harmonogramu monitorowania (`schedule`)**.
- **Aktywna reakcja:** Każde wybudzenie z harmonogramu wymaga sprawdzenia logów, wykrycia ewentualnej stagnacji, martwych pętli lub spadku witalności i podjęcia aktywnej reakcji (zgodnie z ADR-0005).

---

## 7. Bezwzględna Proaktywność i Synchronizacja Środowiska Uruchomieniowego (Runtime Alignment)
- **Zakaz oczekiwania na upomnienia użytkownika:** Jeśli asystent identyfikuje wadę logiczną, naruszenie ADR lub wprowadza modyfikację w plikach źródłowych Pythona (`scoring.py`, `win.py`, `engine/`), ma **bezwzględny obowiązek natychmiastowego i w pełni samodzielnego zrestartowania działających w tle procesów symulacyjnych**.
- **Zakaz pozostawiania procesów na starym kodzie w pamięci RAM:** Pozostawienie działającego w tle procesu po edycji kodu jest traktowane jako błąd krytyczny kradnący czas obliczeniowy. Asystent odpowiada w 100% za stan pamięci operacyjnej i zgodność procesów w tle ze stanem plików na dysku.

---

## 8. Obowiązkowa Interwencja i Ręczna Blokada Złych Zmian Audytora (Proactive Manual Intervention)
- **Kategoryczny zakaz biernego przyklaskiwania optymalizatorowi:** Asystentowi surowo zabrania się bezkrytycznego akceptowania, usprawiedliwiania lub wdrażania propozycji algorytmu, które psują logikę stołu, niszczą tożsamość frakcji lub osłabiają kluczowe mechaniki gry (np. Autodafé, Haki, Relikwie, Fragmenty, Upadki).
- **Bezwzględny Obowiązek Natychmiastowej Interwencji Manualnej:**
  1. Jeśli audytor forsuje problematyczną zmianę (np. próbuje „naprawić” balans przez kastrację lub uśmiercenie mechaniki), asystent **MUSI natychmiast zatrzymać proces i ręcznie zablokować ten wektor w kodzie (`scoring.py`)**.
  2. Asystent **MUSI manualnie wprowadzić właściwą korektę zgodną z Game Designem (np. precyzyjne dostrojenie kart L3 w YAML)**, zsynchronizować SSOT (`sync_config.py`), sprawdzić testy `pytest` i zrestartować proces symulacyjny na czystym stanie.
  3. Każda taka interwencja musi zostać natychmiast odnotowana i skodyfikowana w `.agents/rules/` lub `docs/adr/`.
