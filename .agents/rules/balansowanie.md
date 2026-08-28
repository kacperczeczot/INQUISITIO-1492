# Reguła Projektowa: Organiczne Balansowanie, Integralność Silnika (Anti-Cheat) i Nadzór ADR

Każdy model AI / asystent pracujący w tym repozytorium **MUSI** bezwzględnie przestrzegać poniższych reguł przy projektowaniu, badaniu i modyfikacji balansu gry:

---

## 1. Zgodność z Konstytucją Architektoniczną (ADR-0001 do ADR-0005)
Wszystkie propozycje, zmiany parametrów i kod silnika muszą być w 100% zgodne z dokumentami w `docs/adr/`:
- **ADR-0001 (Organiczna Progresja Er):** Kategoryczny zakaz wprowadzania sztucznych bramek czasowych `if state.era < X` lub `state.era >= X` w warunkach zwycięstwa, efektach kart i silniku. Pacing gry musi wynikać w 100% z fizycznych ograniczeń planszy (koszty złota, liczba ruchów, liczba wymaganych kroków/zasobów).
- **ADR-0002 (Kanon 4P jako Kotwica):** Wszystkie decyzje i oceny telemetrii są weryfikowane na 5 kanonicznych setupach 4P (50 000 partii).
- **ADR-0003 (Asymetria Warunków Zwycięstwa):** Każda frakcja ma unikalną, nienaruszalną tożsamość ścieżki do wygranej.
- **ADR-0004 (Złote Okno Rozgrywki):** Cel to >65% gier kończących się w Erach 5–7 ze szczytem w Erze 6. Gry w Erze 1–2 są zablokowane (<0.3%), w Erze 3 bardzo trudne i rzadkie (<3%), w Erze 4 dojrzałe (~10-18%).
- **ADR-0005 (Zasady Nadzoru & SSOT):** Wszystkie zmienne balansu żyją wyłącznie w `data/data/game_config.yaml`.

---

## 2. Bezwzględny Zakaz Oszukiwania Silnika (Zero Engine Hacks / Zero Fake Guarantees)
- Kategorycznie zabrania się wprowadzania w kodzie Pythona (`src/inquisitio/engine/`) jakichkolwiek:
  1. Ukrytych modyfikatorów, których nie ma na fizycznej karcie lub w `data/data/game_config.yaml`.
  2. Sztucznych blokad er na kartach (np. `if card.id == "kb-04" and state.era < 4: allowed = False`).
  3. Ukrytych mnożników wartości (np. sztuczne podwajanie oskarżeń lub haków).
- Silnik symulacji musi być w 100% przezroczysty – telemetria ma odzwierciedlać nagą prawdę o fizycznych kartach na stole.

---

## 3. Zakaz Samowolnego Wdrażania Zmian (Wymagana Zgoda Użytkownika)
- Asystent **NIE MOŻE** samowolnie edytować `data/data/game_config.yaml`, podbijać wersji i generować raportów w ramach odpowiedzi na luźne pytanie lub hipotezę.
- Wszelkie pomysły muszą zostać najpierw przedstawione użytkownikowi w formie przejrzystej propozycji z uzasadnieniem.
- Wdrożenie następuje **WYŁĄCZNIE** po wyraźnym poleceniu użytkownika (np. „wprowadź”, „zastosuj”, „napraw”).

---

## 4. Matematyczna Weryfikacja Fizyczna przed Propozycją
- Przed zaproponowaniem zmiany progu zwycięstwa asystent **MUSI** sprawdzić fizyczną zawartość talii frakcji:
  - Przykład: Zakaz ustawiania wymogu `decrees: 3`, jeśli w talii są fizycznie tylko 2 karty dekretu.
  - Przykład: Zakaz usuwania mechanizmów pasmowych, jeśli finiszer sam z siebie wyrzuca gracza z pasma.

---

## 5. Pełna Przejrzystość i Rzetelność Dokumentacji
- Wszelkie zmiany parametrów i poprawki silnika muszą być szczegółowo, bez pomijania niewygodnych faktów, odnotowane w `data/playtesting/balance-notes.md`.
- Każda zmiana w `data/data/game_config.yaml` wymaga uruchomienia `src/.venv/bin/python3 scripts/sync_config.py` oraz przejścia 100% testów `src/.venv/bin/pytest`.
