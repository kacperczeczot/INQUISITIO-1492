# 🤖 Szalony Audytor (Auto-Balancer) — Instrukcja Użytkownika

**Szalony Audytor** (`tools/sim/szalony_audytor.py` / `tools/sim/auto_balancer.py`) to w pełni autonomiczny optymalizator balansu gry **INQUISITIO-1492**, działający w pętli *Greedy Hill-Climbing* z dwustopniową weryfikacją Monte Carlo.

---

## 🎯 Jak Działa Pętla Optymalizacji?

W każdej iteracji:
1. **Badanie przestrzeni zmian:** Skrypt generuje ponad 200 potencjalnych modyfikacji (Poziomy 1–4: mechaniki systemowe, warunki zwycięstwa, parametry wszystkich 50 kart, warianty edyktów).
2. **Krok 1 (Szybki przesiew):** Błyskawiczna symulacja (250 partii/setup) wyłania TOP 5 najbardziej obiecujących kandydatów.
3. **Krok 2 (Precyzyjna weryfikacja):** Wybrani liderzy są sprawdzani dużą próbą (1500–3000 partii/setup) z innym ziarnem losowym w celu wykluczenia szumu statystycznego.
4. **Weryfikacja telemetrii:** Sprawdza twarde limity (deadlocks < 16%, pas biedy < 35%, średnia długość 4.2–7.8 er).
5. **Aplikacja zmiany:** Najlepszy kandydat jest automatycznie zapisywany w `game_config.yaml`, numer wersji zostaje podbity (np. `v0.19` → `v0.20`), a przebieg odnotowany w `playtesting/sim-reports/auto_balancer_log.md`.
6. **Kolejny cykl:** Pętla powtarza się z nową wersją bazową, aż do osiągnięcia optimum (brak zysku punktowego) lub upływu zadanego czasu.

---

## 🚀 Przykłady Uruchomienia z Terminala

Wszystkie komendy uruchamiaj z głównego katalogu repozytorium:

### 1. Uruchomienie na określony czas (np. na noc / na 4 godziny) — [REKOMENDOWANE]
```bash
sim/.venv/bin/python tools/sim/szalony_audytor.py --hours 4.0
```

### 2. Działanie do osiągnięcia lokalnego optimum (brak limitu czasu)
```bash
sim/.venv/bin/python tools/sim/szalony_audytor.py
```
*Działa nieprzerwanie, dopóki w żadnym raporcie nie będzie już możliwy wzrost wyniku globalnego.*

### 3. Ograniczenie do zadanej liczby ulepszeń (np. 5 iteracji)
```bash
sim/.venv/bin/python tools/sim/szalony_audytor.py --max-iters 5
```

### 4. Optymalizacja tylko wybranego obszaru:
```bash
# Tylko parametry kart (Poziom 3):
sim/.venv/bin/python tools/sim/szalony_audytor.py --level 3

# Tylko warunki zwycięstwa frakcji (Poziom 2):
sim/.venv/bin/python tools/sim/szalony_audytor.py --level 2

# Tylko zasady systemowe (Poziom 1):
sim/.venv/bin/python tools/sim/szalony_audytor.py --level 1
```

### 5. Tryb testowy / Podgląd bez modyfikowania plików (Dry-Run):
```bash
sim/.venv/bin/python tools/sim/szalony_audytor.py --dry-run
```

---

## ⚙️ Dostępne Flagi i Parametry CLI

| Flaga | Domyślnie | Opis |
| :--- | :---: | :--- |
| `--hours <float>` | `None` | Maksymalny czas pracy w godzinach (np. `2.5`, `4.0`, `8.0`). |
| `--max-iters <int>` | `None` | Limit liczby wprowadzonych ulepszeń. |
| `--min-delta <float>` | `0.1` | Minimalny zysk punktowy wymagany do zaakceptowania zmiany. |
| `--mode` | `two-stage` | Tryb: `two-stage` (szybki przesiew + weryfikacja), `grand` (3k gier), `standard` (500 gier), `fast` (250 gier). |
| `--fast-games <int>` | `250` | Liczba gier/setup w kroku przesiewu (dla `two-stage`). |
| `--confirm-games <int>`| `1500` | Liczba gier/setup w kroku precyzyjnej weryfikacji (dla `two-stage`). |
| `--top-k <int>` | `5` | Ilu liderów z kroku 1 weryfikować w kroku 2. |
| `--level` | `all` | Wybór poziomów do testowania: `all`, `1`, `2`, `3`, `4`. |
| `--param` | `cost,heresy` | Parametry kart dla Poziomu 3: `cost,heresy`, `gold,target_heresy`, `all`. |
| `--workers <int>` | Liczba rdzeni CPU | Liczba równoległych procesów symulacji. |
| `--dry-run` | `False` | Tryb symulacyjny (wypisuje najlepszą zmianę, nie dotyka plików). |

---

## 🛑 Jak Bezpiecznie Zatrzymać Skrypt?

Wciśnij w terminalu skrót **`Ctrl + C`**. 
Skrypt przechwyci sygnał (*Graceful Exit*), bezpiecznie domknie bieżącą symulację i wyświetli podsumowanie sesji bez uszkadzania pliku `game_config.yaml`.

---

## 📊 Gdzie Sprawdzać Wyniki?

1. **Dziennik ewolucji w czasie rzeczywistym:** [`playtesting/sim-reports/auto_balancer_log.md`](file:///Users/kacper/Documents/GitHub/INQUISITIO-1492/playtesting/sim-reports/auto_balancer_log.md)
2. **Aktualny plik konfiguracyjny:** [`game_config.yaml`](file:///Users/kacper/Documents/GitHub/INQUISITIO-1492/game_config.yaml)
3. **Kopia zapasowa ostatniej konfiguracji:** `game_config.yaml.bak`
