# 🤖 Szalony Audytor (Auto-Balancer) — Instrukcja Użytkownika

**Szalony Audytor** (`tools/sim/szalony_audytor.py` / `tools/sim/auto_balancer.py`) to w pełni autonomiczny optymalizator balansu gry **INQUISITIO-1492**, działający w pętli *Greedy Hill-Climbing* z dwustopniową weryfikacją Monte Carlo (*Paired Common Random Numbers*) oraz **automatycznym generowaniem pełnej dokumentacji i archiwów**.

---

## 🎯 Co Szalony Audytor Robi w Każdej Iteracji?

1. **Badanie przestrzeni zmian:** Generuje ponad 200 potencjalnych modyfikacji (Poziomy 1–4: mechaniki systemowe, warunki zwycięstwa, parametry wszystkich 50 kart, warianty edyktów).
2. **Krok 1 (Solidny Przesiew):** Symulacja **1 000 partii / setup** (16 000 partii per wariant) wyłania TOP 5 najbardziej obiecujących kandydatów.
3. **Krok 2 (Precyzyjna Weryfikacja Grand Monte Carlo):** Wybrani liderzy są sprawdzani dużą próbą **3 000 partii / setup** (48 000 partii per test) w symulacji parowanej (*Common Random Numbers*) w celu całkowitego wyeliminowania szumu losowego.
4. **Twarde Bezpieczniki:** Kandydat jest akceptowany TYLKO wtedy, gdy:
   - Na próbie 3 000 gier osiąga realny zysk punktowy: `Δ Global Score >= +0.10 pkt`,
   - Nie narusza norm telemetrii (Deadlocks < 16%, Pas Biedy < 35%, średnia liczba er: 4.2–7.8).
5. **Aplikacja zmiany i wersjonowanie:** 
   - Wprowadza zwycięski parametr do `game_config.yaml`.
   - Podbija numer wersji (np. `v0.21` → `v0.22`).
6. **📄 Automatyczna Dokumentacja i Raporty:**
   - Tworzy katalog archiwum wersji: `playtesting/sim-reports/archive/{wersja}/` ze snapshotem `game_config.yaml`.
   - Generuje szczegółowy raport danej iteracji: `raport_optymalizacji.md` (ranking kandydatów, delty, telemetria).
   - Generuje pełny raport telemetrii i win shares 16 setupów: `raport_telemetrii.md`.
   - Automatycznie dopisuje notatkę o nowym patchu do `playtesting/balance-notes.md`.
   - Zapisuje wpis w dzienniku ewolucji `playtesting/sim-reports/auto_balancer_log.md`.
7. **Kolejny cykl:** Pętla powtarza się z nową bazą, aż do osiągnięcia lokalnego optimum lub limitu czasu.

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

### 3. Z automatycznym generowaniem pełnego pakietu 6 raportów po zakończeniu:
```bash
sim/.venv/bin/python tools/sim/szalony_audytor.py --hours 4.0 --full-audit-on-finish
```

### 4. Ograniczenie do zadanej liczby ulepszeń (np. 5 iteracji)
```bash
sim/.venv/bin/python tools/sim/szalony_audytor.py --max-iters 5
```

### 5. Optymalizacja tylko wybranego obszaru:
```bash
# Tylko parametry kart (Poziom 3):
sim/.venv/bin/python tools/sim/szalony_audytor.py --level 3

# Tylko warunki zwycięstwa frakcji (Poziom 2):
sim/.venv/bin/python tools/sim/szalony_audytor.py --level 2

# Tylko zasady systemowe (Poziom 1):
sim/.venv/bin/python tools/sim/szalony_audytor.py --level 1
```

### 6. Tryb testowy / Podgląd bez modyfikowania plików (Dry-Run):
```bash
sim/.venv/bin/python tools/sim/szalony_audytor.py --dry-run
```

---

## ⚙️ Domyślne Parametry i Flagi CLI

| Flaga | Domyślnie | Opis |
| :--- | :---: | :--- |
| `--fast-games <int>` | `1000` | Liczba gier/setup w kroku przesiewu (16 000 partii na wariant). |
| `--confirm-games <int>`| `3000` | Liczba gier/setup w kroku weryfikacji Grand (48 000 partii per test). |
| `--min-delta <float>` | `0.1` | Minimalny zysk punktowy wymagany do zaakceptowania zmiany. |
| `--hours <float>` | `None` | Maksymalny czas pracy w godzinach (np. `2.5`, `4.0`, `8.0`). |
| `--max-iters <int>` | `None` | Limit liczby wprowadzonych ulepszeń. |
| `--mode` | `two-stage` | Tryb: `two-stage` (przesiew + Grand weryfikacja), `grand` (3k gier bezpośrednio), `standard` (500 gier). |
| `--top-k <int>` | `5` | Ilu liderów z kroku 1 weryfikować w kroku 2. |
| `--level` | `all` | Wybór poziomów do testowania: `all`, `1`, `2`, `3`, `4`. |
| `--param` | `cost,heresy` | Parametry kart dla Poziomu 3: `cost,heresy`, `gold,target_heresy`, `all`. |
| `--full-audit-on-finish`| `False` | Po znalezieniu optimum generuje komplet 6 raportów symulacyjnych. |
| `--workers <int>` | Liczba rdzeni CPU | Liczba równoległych procesów symulacji. |
| `--dry-run` | `False` | Tryb symulacyjny (wypisuje najlepszą zmianę, nie dotyka plików). |

---

## 🛑 Jak Bezpiecznie Zatrzymać Skrypt?

Wciśnij w terminalu skrót **`Ctrl + C`**. 
Skrypt przechwyci sygnał (*Graceful Exit*), bezpiecznie domknie bieżącą symulację, wygeneruje dokumentację i wyświetli podsumowanie sesji bez uszkadzania pliku `game_config.yaml`.
