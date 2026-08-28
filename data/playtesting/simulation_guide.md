[Strona główna](../README.md) > [Playtesting](README.md) > [Dokumentacja](README.md)

---

# Instrukcja i Przewodnik po Testach Symulacyjnych Monte Carlo

Ten przewodnik wyjaśnia, jak uruchamiać, modyfikować oraz interpretować testy balansu gry **INQUISITIO-1492** przy użyciu silnika symulacyjnego w Pythonie.

---

## 🚀 1. Szybki Start (Uruchamianie Skryptów)

Wszystkie skrypty znajdują się w folderze `tools/sim/` i korzystają z zainstalowanego środowiska wirtualnego `.venv` w folderze `sim/`.

Aby uruchomić dowolny test, wywołaj z głównego katalogu repozytorium:

```bash
# 0. Synchronizacja zmian po edycji game_config.yaml (odświeża zasady w ksiega.md)
sim/.venv/bin/python tools/sync_config.py

# ─── GŁÓWNE SKRYPTY PEŁNEGO AUDYTU (WSZYSTKIE 6 RAPORTÓW) ───
# Standardowy pełny audyt (optymalna próba, niski szum, czas ~1.5 min):
sim/.venv/bin/python tools/sim/run_standard_audit.py

# Głęboki audyt walidacyjny / Release Gate (maksymalna próba, zero szumu, czas ~4 min):
sim/.venv/bin/python tools/sim/run_deep_audit.py

# ─── POJEDYNCZE MODUŁY AUDYTÓW ───
# 1. Kompletny Raport Zbalansowania i Telemetrii (16 setupów)
sim/.venv/bin/python tools/sim/generate_report.py --games 1000

# 2. Audyt Poziomu 1 (Główne mechaniki systemowe)
sim/.venv/bin/python tools/sim/audit_level1.py --games 500

# 3. Audyt Poziomu 2 (Progi i warunki zwycięstwa frakcji)
sim/.venv/bin/python tools/sim/audit_level2.py --games 500

# 4. Audyt Poziomu 3 (Precyzyjny audyt parametrów kart per karta)
sim/.venv/bin/python tools/sim/audit_level3.py --games 300 --param cost,heresy

# 5. Audyt Poziomu 4 (Warianty niszowe i modyfikatory zasad)
sim/.venv/bin/python tools/sim/audit_level4.py --games 1000

# 6. Testy Stresu Ekonomicznego (Poverty Stress Test)
sim/.venv/bin/python tools/sim/audit_stress_tests.py --games 500
```

---

## ⚙️ 2. Dostępne Parametry Uruchomienia i Filtry

### Ogólne parametry CLI dla wszystkich skryptów:
- `--games <N>`: Liczba partii do symulacji na każdy setup (domyślnie: `300` dla audytów, `500` dla raportu głównego). Wyższa próba (np. `1000`+) podnosi dokładność statystyczną kosztem dłuższego czasu.
- `--seed <S>`: Ziarno losowości (domyślnie: `42`). Zapewnia pełną powtarzalność wyników.
- `--output <path>`: Własna ścieżka zapisu raportu Markdown (domyślnie raporty lądują w `data/playtesting/sim-reports/`).

### Specialne filtry chirurgiczne dla Audytu Poziomu 3 (`audit_level3.py`):
Pozwalają audytować wybrane właściwości lub frakcje bez konieczności uruchamiania pełnego zestawu kart:

- `--param <lista>`: Wybór testowanych parametrów: `cost`, `heresy`, `target_heresy`, `gold` lub `all` (np. `--param cost,heresy`).
- `--faction <kod>`: Filtrowanie po kodzie frakcji: `so` (Święte Oficjum), `caa` (Cienie Al-Andalus), `kb` (Korona Borgiowie), `kt` (Kabała Toledo), `gc` (Gildia Cieni) lub `all`.
- `--card <id>`: Targetowanie konkretnej karty po ID, np. `--card so-04` (Nasłanie Inkwizytora) lub `--card kb-01`.

#### Przykłady wywołań filtrowanych:
```bash
# Audyt tylko kosztów i przydziału Herezji kart Świętego Oficjum:
sim/.venv/bin/python tools/sim/audit_level3.py --faction so --param cost,heresy

# Chirurgiczny audyt ±1 dla wszystkich parametrów karty SO-04:
sim/.venv/bin/python tools/sim/audit_level3.py --card so-04

# Audyt tylko generowania złota w kartach Cieni Al-Andalus:
sim/.venv/bin/python tools/sim/audit_level3.py --faction caa --param gold
```

---

## 📈 3. Jak Interpretować Wyniki Telemetrii (5 Filarów)

Raporty zawierają dwie kluczowe sekcje: **Szanse Wygranych (Win Shares)** oraz **Statystyki Telemetrii**.

### A. Szanse Wygranych (Win Share %)
- **Cel:** Win-rate każdej frakcji powinien być jak najbliższy **Punktowi Idealnemu** (33.3% dla 3p, 25.0% dla 4p, 20.0% dla 5p).
- **Punktacja (Score):** 100.0 pkt to idealny balans. Wynik powyżej **50.0 pkt** oznacza zrównoważony setup (kolor 🟢). Spadek poniżej 25.0 pkt sygnalizuje patologię lub dominację jednej z frakcji (kolor 🔴).

### B. Telemetria 5 Filarów
- **Średnia Er (Tempo Gry):** Normatyw to **5.0 – 7.0 Er**. Zbyt niska średnia oznacza zbyt szybką wygraną (snowball). Zbyt wysoka to paraliż.
- **Deadlock % (Remisy):** Procent partii, które osiągnęły limit Er (`max_eras`) bez wyłonienia zwycięzcy. Tolerowany próg to **< 5.0%** (krytyczny < 15.0%).
- **Pas Biedy % (Poverty Rate):** Procent tur, w których gracze zmuszeni byli spasować z braku złota. Tolerowany próg to **< 30.0%**.
- **Autodafé na grę:** Wskaźnik agresji Inkwizytora. Normatyw: **0.5 – 2.0** Autodafé na partię.
- **Oskarżenia na grę:** Wskaźnik interakcji politycznej na Dworze. Normatyw: **1.5 – 4.5** oskarżeń na partię.

---

## 🧪 4. Propozycje Dodatkowych Testów (Poza +-1)

Jeśli chcesz przetestować głębsze zależności, proponujemy:

1. **Test Przeciążenia Ekonomicznego (Poverty Stress Test):**
   * Uruchomienie symulacji ze zmianą startowego złota od 1 do 5. Pomaga sprawdzić, przy jakiej wartości talia kart ulega całkowitemu zablokowaniu.
2. **Test Odporności na Dominację (Bias Resilience Test):**
   * Uruchomienie partii, w których jedna frakcja gra optymalną strategią botów (S-Tier), a pozostałe losowo, sprawdzając, czy system gry daje radę spowolnić lidera.
