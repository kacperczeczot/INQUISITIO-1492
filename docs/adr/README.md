# Rejestr Decyzji Projektowych i Architektonicznych (ADR / GDDR)
## INQUISITIO-1492: The Great Board Game Simulation & Engine

Ten katalog zawiera **Architecture & Game Design Decision Records (ADR)** dla projektu INQUISITIO-1492. 
Każdy plik stanowi niezmienną, formalną podstawę dla decyzji w mechanice gry, silniku symulacji, konfiguracji SSOT (`game_config.yaml`) oraz zachowaniu algorytmów optymalizacyjnych (audytora).

---

## 📜 Zasada Niezmienności (ADR Invariants)
1. **Żadna fundamentalna zasada gry nie może zostać zmieniona bez nowego rekordu ADR.**
2. **Audytor kanonu optymalizuje wyłącznie wartości parametrów w ramach dopuszczonych granic ustalonych w ADR.**
3. Jeśli zmiana w kodzie lub konfiguracji jest sprzeczna z aktywnym ADR, kod jest traktowany jako **błędny** (regresja).

---

## 📑 Rejestr Decyzji (ADR Index)

| Nr | Tytuł | Status | Data | Opis |
|---|---|---|---|---|
| [ADR-0001](0001-organiczna-progresja-er-i-likwidacja-sztucznych-barier.md) | Organiczna Progresja Er i Likwidacja Sztucznych Barier | **ACCEPTED** | 2026-08-23 | Zastąpienie twardych bramek `era >= X` organiczną głębią mechanik questowych |
| [ADR-0002](0002-kanon-4p-jako-bezwzgledna-kotwica-balansu.md) | Kanon 4P jako Bezwzględna Kotwica Balansu | **ACCEPTED** | 2026-08-23 | Zakaz optymalizacji pod 3P/5P kosztem 5 setupów 4P |
| [ADR-0003](0003-anatomia-i-asymetria-warunkow-zwyciestwa-frakcji.md) | Anatomia i Asymetria Warunków Zwycięstwa 5 Frakcji | **ACCEPTED** | 2026-08-23 | Szczegółowe uzasadnienie warunków zwycięstwa i late-game dla każdej frakcji |
| [ADR-0004](0004-standardy-czasu-rozgrywki-i-akceptowalne-okno-er.md) | Standardy Czasu Rozgrywki i Złote Okno Er (5–7) | **ACCEPTED** | 2026-08-23 | Definicja rozkładu partii, eliminacja wczesnych sprintów i dominacja Er 5–7 |
| [ADR-0005](0005-zasady-nadzoru-i-interwencji-w-procesie-audytora.md) | Zasady Nadzoru, Reakcji i Eskalacji Wielowymiarowej Audytora | **ACCEPTED** | 2026-08-23 | Procedura „Monitoruj, Kontroluj, Reaguj” i automatyczne przejście 1D $\to$ 2D/3D |
| [ADR-0006](0006-standard-pelnych-talii-i-eliminacja-warstwowosci.md) | Standard Pełnych Talii i Eliminacja Warstwowości (A/B/C) | **ACCEPTED** | 2026-08-23 | Likwidacja sztucznych warstw; pełne talie 12 kart od 1. tury |
| [ADR-0007](0007-geometria-planszy-i-fizyczne-niezmienniki-komponentow.md) | Geometria Planszy i Fizyczne Niezmienniki Komponentów | **ACCEPTED** | 2026-08-23 | Niezmienna liczba 3 agentów na gracza i 5 lokacji na planszy |
| [ADR-0008](0008-model-ekonomiczny-stolu-i-rola-akcji-gospodarczej.md) | Model Ekonomiczny Stołu i Rola Akcji Gospodarczej | **ACCEPTED** | 2026-08-23 | Dwuakcyjność er, relacja kart do dochodu, eliminacja pasów biedy |
| [ADR-0009](0009-mechanika-herezji-jako-osi-ryzyka.md) | Mechanika Herezji jako Dynamicznej Osi Ryzyka | **ACCEPTED** | 2026-08-23 | 3 strefy herezji, zakaz darmowych resetów, push-your-luck |
| [ADR-0010](0010-witalnosc-alternatywnych-sciezek-zwyciestwa.md) | Witalność Alternatywnych Ścieżek Zwycięstwa | **ACCEPTED** | 2026-08-23 | Ochrona podwójnej ścieżki (Stosy vs Skazania) przed degeneracją |
| [ADR-0011](0011-transparentnosc-silnika-i-zero-hacks.md) | Transparentność Silnika Symulacji i Zasada Czystej Fizyki | **ACCEPTED** | 2026-08-23 | Zero ukrytych modyfikatorów w Pythonie; 100% zgodności ze stołem |
| [ADR-0012](0012-czteropoziomowa-hierarchia-balansowania.md) | Czteropoziomowa Hierarchia Balansowania (L1-L4) | **ACCEPTED** | 2026-08-23 | Priorytet zmian makro (L1/L2) przed mikro-korektami pojedynczych kart (L3) |
| [ADR-0013](0013-deterministyczna-gramatyka-kart-z-ssot.md) | Deterministyczna Gramatyka Kart i Generowanie Tekstów z SSOT | **ACCEPTED** | 2026-08-23 | Teksty kart deterministycznie generowane ze schematu YAML |
| [ADR-0014](0014-standardy-proby-statystycznej-i-wieloseedowej.md) | Standardy Próby Statystycznej i Walidacja Wieloseedowa | **ACCEPTED** | 2026-08-23 | Próby $\ge 10\,000$ gier/setup i obowiązkowa weryfikacja na min. 2 seedach |
| [ADR-0015](0015-model-heurystycznego-racjonalnego-gracza.md) | Model Heurystycznego Racjonalnego Gracza w Symulacji | **ACCEPTED** | 2026-08-23 | Uczciwe boty decyzyjne bez dostępu do ukrytych stanów gry |
| [ADR-0016](0016-rytual-autodafe-i-logistyka-inkwizycji.md) | Rytuał Autodafé, Cykliczność i Logistyka Inkwizycji | **ACCEPTED** | 2026-08-23 | Lokalny zasięg stosu (tylko lokacja Inkwizytora), podział areszt vs stos |

---

## 📐 Szablon Nowego Rekordu ADR
Każdy nowy rekord musi zawierać:
1. **Status**: PROPOSED / ACCEPTED / SUPERSEDED.
2. **Kontekst problemu**: Co nie działało lub wywoływało problem?
3. **Decyzja projektowa**: Dokładna reguła mechaniczna i programistyczna.
4. **Szczegółowe uzasadnienie**: Matematyka, psychologia graczy, klimat 1492 roku.
5. **Niezmienniki (Invariants)**: Twarde reguły chroniące przed regresją.
6. **Konsekwencje**: Zmiany w `game_config.yaml`, `sim/inquisitio/` i testach.
