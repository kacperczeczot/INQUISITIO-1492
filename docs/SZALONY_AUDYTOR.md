# 🤖 Szalony Audytor (Auto-Balancer) — Instrukcja Użytkownika

**Szalony Audytor** (`tools/sim/szalony_audytor.py` / `tools/sim/auto_balancer.py`) to w pełni autonomiczny optymalizator balansu gry **INQUISITIO-1492**, działający w pętli *Greedy Hill-Climbing* z dwustopniową weryfikacją Monte Carlo (*Paired Common Random Numbers*) oraz **automatycznym generowaniem pełnej dokumentacji i archiwów**.

---

## 🎯 Taktyka Działania: Kaskada Poziomowa (Hierarchical Waterfall Strategy)

Szalony Audytor optymalizuje grę w sposób **hierarchiczny (od makro-mechanik do mikro-parametrów)**:

1. **Zawsze zaczyna od Poziomu 1 (L1 — Mechaniki Systemowe):** Bada ~12 wariantów **bezpośrednio na pełnej próbie 5 000 partii / setup** (bez potrzeby przesiewu).
2. **Kaskadowe przejście:**
   - Jeśli Poziom 1 przyniesie zysk $\ge +0.05$ pkt $\rightarrow$ wprowadza zmianę i **zostaje na L1**, badając go ponownie.
   - Dopiero gdy Poziom 1 nie ma już żadnych ulepszeń $\rightarrow$ przechodzi do **Poziomu 2 (L2 — Warunki Zwycięstwa Frakcji)** (bezpośrednia próba 5 000 partii na ~28 wariantach).
   - Jeśli Poziom 2 nie ma już ulepszeń $\rightarrow$ przechodzi do **Poziomu 3 (L3 — Parametry Wszystkich 50 Kart)** (tutaj działa **Szybki Przesiew 1000 partii $\rightarrow$ TOP 20 $\rightarrow$ Weryfikacja 5000 partii**).
   - Jeśli Poziom 3 nie ma już ulepszeń $\rightarrow$ przechodzi do **Poziomu 4 (L4 — Warianty Niszowe i Edykty)** (bezpośrednia próba 5 000 partii na ~8 wariantach).
3. **Zasada Resetu do Bazy L1:**
   - **Za każdym razem, gdy na dowolnym wyższym poziomie (L2, L3 lub L4) zostanie wprowadzona zmiana, audytor natychmiast wraca do Poziomu 1** i sprawdza, czy nowe uwarunkowania nie odblokowały nowych ulepszeń systemowych!
4. **Warunek Zakończenia (True Global Optimum):**
   - Audytor kończy pracę dopiero wtedy, gdy sprawdzi kolejno L1 $\rightarrow$ L2 $\rightarrow$ L3 $\rightarrow$ L4 i **na żadnym z nich nie znajdzie ani jednej poprawy**.

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
| `--confirm-games <int>`| `5000` | Liczba gier/setup w kroku weryfikacji Ultra (80 000 partii per test). |
| `--min-delta <float>` | `0.1` | Minimalny zysk punktowy wymagany do zaakceptowania zmiany. |
| `--hours <float>` | `None` | Maksymalny czas pracy w godzinach (np. `2.5`, `4.0`, `8.0`). |
| `--max-iters <int>` | `None` | Limit liczby wprowadzonych ulepszeń. |
| `--mode` | `two-stage` | Tryb: `two-stage` (przesiew + Grand weryfikacja), `grand` (3k gier bezpośrednio), `standard` (500 gier). |
| `--top-k <int>` | `20` | Ilu liderów z kroku 1 weryfikować w kroku 2. |
| `--level` | `all` | Wybór poziomów do testowania: `all`, `1`, `2`, `3`, `4`. |
| `--param` | `all` | Parametry kart dla Poziomu 3: `all` (koszt, herezja, złoto, cel herezji) lub podzbiory (`cost,heresy`, `gold`). |
| `--full-audit-on-finish`| `False` | Po znalezieniu optimum generuje komplet 6 raportów symulacyjnych. |
| `--workers <int>` | Liczba rdzeni CPU | Liczba równoległych procesów symulacji. |
| `--dry-run` | `False` | Tryb symulacyjny (wypisuje najlepszą zmianę, nie dotyka plików). |

---

## 🛑 Jak Bezpiecznie Zatrzymać Skrypt?

Wciśnij w terminalu skrót **`Ctrl + C`**. 
Skrypt przechwyci sygnał (*Graceful Exit*), bezpiecznie domknie bieżącą symulację, wygeneruje dokumentację i wyświetli podsumowanie sesji bez uszkadzania pliku `game_config.yaml`.
