# Reguła Projektowa: Dyscyplina Agenta, Zakaz Samowolki i Matematyczna Walidacja

Każdy model AI / asystent pracujący w tym repozytorium **MUSI** bezwzględnie przestrzegać poniższych reguł operacyjnych:

---

## 1. Bezwzględny Tryb Konsultacyjny (Zero Samowolki)
- **Zakaz wyrywania się przed szereg:** Asystentowi kategorycznie zabrania się modyfikowania plików `data/data/game_config.yaml`, kodu silnika (`sim/`), skryptów audytora czy dokumentacji w odpowiedzi na luźne pytanie, hipotezę lub dyskusję.
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
- Każda zatwierdzona zmiana parametrów w `data/data/game_config.yaml` wymaga:
  1. Podbicia wersji `v1.0-alpha.X` $\to$ `v1.0-alpha.Y` i aktualizacji daty.
  2. Rzetelnego wpisu w `data/playtesting/balance-notes.md` (bez cenzury i pomijania faktów).
  3. Uruchomienia `src/.venv/bin/python3 scripts/sync_config.py`.
  4. Weryfikacji 100% testów `src/.venv/bin/pytest`.

---

## 5. Protokół Samonaprawy i Natychmiastowej Aktualizacji Reguł (Continuous Rule Codification)
- **Obowiązkowa reakcja na błąd:** Jeśli w toku pracy pojawi się jakikolwiek błąd, pomyłka, regresja, niezrozumienie intencji użytkownika lub próba pójścia na skrót ze strony asystenta AI, asystent ma **bezwzględny obowiązek natychmiastowego zaktualizowania i zaostrzenia odpowiedniego pliku w `.agents/rules/` lub utworzenia/uzupełnienia rekordu w `docs/adr/`**.
- **Zakaz powtarzania błędów:** Każde upomnienie ze strony użytkownika musi zostać w tym samym kroku przekształcone w formalną, trwałą regułę systemową, aby błąd nigdy więcej się nie powtórzył.

---

## 6. Obowiązkowy Proces Monitorująco-Reagujący i Limit Przestoju (Anti-Stagnation Watchdog)
- **Zakaz biernego oczekiwania:** Przy uruchomieniu jakiegokolwiek długotrwałego procesu w tle (np. audytor kanonu, wielogodzinna symulacja), asystent ma **bezwzględny obowiązek natychmiastowego ustawienia cyklicznego harmonogramu monitorowania (`schedule`)**.
- **Twardy Limit Przestoju (Anti-Stagnation Hard Rule):** Jeśli w ciągu **maksymalnie 60 minut** lub po **1 pełnym cyklu wiązek (1D→2D→3D)** optymalizator nie wdroży żadnego nowego patcha i kręci się w pętli resetów z brakiem zysku:
  1. Asystent **NIE MOŻE** biernie czekać do rana ani powtarzać pustych cykli.
  2. Asystent **MUSI natychmiast zatrzymać proces**, przeprowadzić manualną dekompozycję telemetryczną najsłabszego setupu (bottom setup), zidentyfikować blokujące karty/frakcje i przygotować konkretną diagnozę inżynieryjną lub interweniować manualnie w przestrzeni mutacji.
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

---

## 9. Bezwzględna Zasada Próby Minimalnej (Zasada 5000 / ADR-0014)
- **Kategoryczny zakaz zapisu raportów na małych próbach:** Żaden raport zapisywany jako plik markdown (`raport_telemetrii.md`, `raport_optymalizacji.md`, archiwa) **NIE MOŻE** opierać się na próbie mniejszej niż **5 000 partii na setup** (dla pełnych raportów telemetrii wydania: **10 000 partii na setup** = 160 000 partii dla 16 setupów).
- **Twarda blokada programowa w silniku:** Funkcja `save_and_archive_report()` w `src/inquisitio/runner/audit_facts.py` oraz wszystkie skrypty narzędziowe posiadają twardy warunek zgłaszający `ValueError` i przerywający wykonanie, jeśli próba zapisu nastąpi dla próby $< 5000$ gier/setup.
- **Zero kompromisów statystycznych:** Pomiar balansu gry asymetrycznej na próbach rzędu 500 czy 1000 gier generuje niedopuszczalny szum statystyczny ($\pm 2.5\%$) i jest traktowany jako krytyczne naruszenie dyscypliny inżynierskiej.

---

## 10. Zasada Jednego Autorytatywnego Źródła Telemetrii (Single Telemetry Truth)
- **Kategoryczny zakaz podwójnej telemetrii:** Zabrania się uruchamiania lub cytowania wyników z modułów alternatywnych (np. niezweryfikowanego modułu C++), jeśli oficjalne raporty na dysku generowane są z innego źródła.
- **Python SSOT jako jedyny standard:** Autorytatywnym silnikiem decyzyjnym, symulacyjnym i audytowym jest wyłącznie kanoniczny kod Pythona (`src/inquisitio/`). Jakiekolwiek moduły akceleracji (C++) mogą być używane tylko wtedy, gdy przejdą formalny test identyczności rozkładu (Kolmogorov-Smirnov / Chi-Square $p > 0.99$).
- **Zakaz rozbieżności werbalno-plikowej:** Wszystkie liczby podawane użytkownikowi w czacie muszą w 100% odpowiadać liczbom generowanym i zapisywanym do plików na dysku.

---

## 11. Zasada Ścisłej Monotoniczności i Zakaz Degradacji Balansu (Strict Monotonicity Gate)
- **Kategoryczny zakaz heurystyk degradujących (*Simulated Annealing*):** W algorytmach optymalizacyjnych zabrania się stosowania mechanizmów probabilistycznej akceptacji gorszych wyników ($\Delta \le 0$).
- **Twardy warunek akceptacji patcha:** Zmiana w `data/data/game_config.yaml` może zostać wdrożona **WYŁĄCZNIE wtedy**, gdy spełnia jednocześnie:
  1. $\Delta \text{Score} \ge +0.50$ pkt (udowodniony zysk globalny).
  2. $\Delta \text{Min} \ge -0.50$ pkt (ochrona najsłabszego setupu przed załamaniem podłogi).
  3. $\text{Kara Witalności} = 0.00$ (brak deadlocków, brak kryzysu biedy, zachowane oskarżenia).

---

## 12. Obowiązkowa Weryfikacja Stanu na Dysku przed Raportowaniem (On-Disk State Verification)
- **Weryfikacja przed odpowiedzią:** Przed udzieleniem odpowiedzi na pytanie o stan gry, wersję czy parametry, asystent ma **bezwzględny obowiązek** sprawdzić stan repozytorium (`git status`), nagłówek [game_config.yaml](file:///Users/kacper/Documents/GitHub/INQUISITIO-1492/game_config.yaml) oraz zawartość bieżącego raportu na dysku.
- **Zakaz deklaracji z pamięci podręcznej:** Zabrania się twierdzenia, że pliki zostały przywrócone lub zmienione, bez natychmiastowego potwierdzenia tego faktu komendą weryfikującą na dysku.

---

## 13. Ścisły Nadzór nad Cyklem Życia Procesów w Tle (Process Lifecycle Lockdown)
- **Zakaz porzucania procesów:** Każde zadanie asynchroniczne uruchomione w tle musi być stale monitorowane za pomocą harmonogramu (`schedule`) lub zakończone (`manage_task kill`) przed oddaniem głosu użytkownikowi.
- **Zakaz samowolnych pętli w tle:** Skrypty działające w tle nie mogą w pętli modyfikować plików konfiguracyjnych i podbijać wersji bez jawnego punktu kontrolnego i zgody użytkownika.

---

## 14. Rygor Narzędziowy i Ślepego Posłuszeństwa
- **Bezwzględny zakaz omijania narzędzi Antigravity:** Asystentowi surowo zabrania się używania komend powłoki (np. `cat << EOF > ...`, `echo`) do tworzenia, edycji lub dopisywania zawartości do plików na dysku. Wszelkie modyfikacje kodu muszą odbywać się wyłącznie przez dedykowane, natywne narzędzia asystenta (`write_to_file`, `multi_replace_file_content`). To kluczowy wymóg IDE.
