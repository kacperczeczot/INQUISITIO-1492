# 🤖 Szalony Audytor (Auto-Balancer) — Instrukcja Użytkownika

**Szalony Audytor** (`tools/sim/szalony_audytor.py` / `tools/sim/auto_balancer.py`) to w pełni autonomiczny optymalizator balansu gry **INQUISITIO-1492**, działający w oparciu o **Progresywne Przeszukiwanie Wiązkowe (Progressive Beam Search 1D/2D/3D)** oraz **3-Stopniowy Lejek Sukcesywnej Selekcji (Progressive Successive Halving)** z weryfikacją Monte Carlo (*Paired Common Random Numbers*) oraz **automatycznym generowaniem pełnej dokumentacji i archiwów**.

---

## 🎯 Architektura: 3-Stopniowy Lejek Sukcesywnej Selekcji (Funnel)

Zamiast monolitycznego i czasochłonnego testowania setek wariantów na wielkich próbach, Szalony Audytor stosuje trzystopniowy lejek eliminacji szumów i selekcji:

1. **Etap 1: Szybki Przesiew Zgrubny (*Coarse Screen*, ~5–10 min):**
   - Bada całą przestrzeń ~400 kandydatów atomowych (L1 Rdzeń + L2 Zwycięstwa + L3 Karty + L4 Warianty) na próbie **200 gier / setup**.
   - Błyskawicznie eliminuje 80–85% niekorzystnych mutacji, regresji balansu i wariantów generujących deadlocki.
   - Wyłania szeroką stawkę **TOP 48 Półfinalistów**.
2. **Etap 2: Głęboki Przesiew i Konsolidacja (*Refined Screen*, ~10–15 min):**
   - Bada TOP 48 półfinalistów na precyzyjniejszej próbie **1 000 gier / setup** (16 setupów).
   - Odsiewa szumy statystyczne i stabilizuje ranking.
   - Wyłania **TOP 24 Finalistów**.
3. **Etap 3: Weryfikacja Ultra (*Ultra Verification*, ~20–30 min):**
   - Bada pełną stawkę **TOP 24 Finalistów** na próbie **5 000 gier / setup (80 000 gier per wariant)** z użyciem *Common Random Numbers (CRN)*.
   - Sprawdza twarde kryteria telemetrii (Deadlock < 5%, Pas Biedy < 30%, Średnia Er w [4.5, 7.0]).
   - Wybiera najlepszą mutację z zyskiem $\Delta \ge +0.05$ pkt i automatycznie wdraża Patch.

### 🌐 Progresywne Wiązki 1D $\rightarrow$ 2D $\rightarrow$ 3D (Plateau Breaking)
- Jeśli w Fazie 1D żaden pojedynczy wariant nie daje zysku $\ge +0.05$ pkt $\rightarrow$ audytor kwalifikuje **TOP 8 nasion** i eskaluje do **Fazy 2D** (pary synergiczne: nasiona $\times$ atomowe mechaniki).
- Po znalezieniu i wdrożeniu patcha wiązka natychmiast resetuje się do Fazy 1D.

---

## 🚀 Przykłady Uruchomienia z Terminala

Wszystkie komendy uruchamiaj z głównego katalogu repozytorium:

### 1. Uruchomienie standardowe (3-stopniowy lejek do optimum lub limitu czasu):
```bash
sim/.venv/bin/python tools/sim/szalony_audytor.py --hours 4.0
```

### 2. Działanie do osiągnięcia lokalnego optimum (brak limitu czasu):
```bash
sim/.venv/bin/python tools/sim/szalony_audytor.py
```

### 3. Ograniczenie do zadanej liczby ulepszeń (np. 5 patchów):
```bash
sim/.venv/bin/python tools/sim/szalony_audytor.py --max-iters 5
```

### 4. Tryb symulacyjny bez modyfikowania plików (Dry-Run):
```bash
sim/.venv/bin/python tools/sim/szalony_audytor.py --dry-run
```

---

## ⚙️ Domyślne Parametry i Flagi CLI

| Flaga | Domyślnie | Opis |
| :--- | :---: | :--- |
| `--fast-games <int>` | `200` | Liczba gier/setup w Etapie 1 (szybki przesiew zgrubny, min. 100). |
| `--screen-games <int>` | `1000` | Liczba gier/setup w Etapie 2 (głęboki przesiew półfinalistów, min. 500). |
| `--confirm-games <int>`| `5000` | Liczba gier/setup w Etapie 3 (weryfikacja ultra finalistów, min. 3000). |
| `--top-semifinalists <int>` | `48` | Liczba półfinalistów badanych w Etapie 2. |
| `--top-k <int>` | `24` | Liczba finalistów weryfikowanych w Etapie 3 (Weryfikacja Ultra). |
| `--beam-width <int>` | `8` | Liczba nasion kwalifikowanych do wyższych faz wiązkowych (2D/3D). |
| `--min-delta <float>` | `0.05` | Minimalny zysk punktowy wymagany do wdrożenia patcha. |
| `--hours <float>` | `None` | Maksymalny czas pracy w godzinach (np. `2.5`, `4.0`, `8.0`). |
| `--max-iters <int>` | `None` | Limit liczby wprowadzonych ulepszeń. |
| `--workers <int>` | Liczba rdzeni CPU | Liczba równoległych procesów symulacji (max 10). |
| `--dry-run` | `False` | Tryb symulacyjny (wypisuje najlepszą zmianę, nie dotyka plików). |

---

## 🛑 Jak Bezpiecznie Zatrzymać Skrypt?

Wciśnij w terminalu skrót **`Ctrl + C`**. 
Skrypt przechwyci sygnał (*Graceful Exit*), bezpiecznie domknie bieżącą iterację, wygeneruje dokumentację i wyświetli podsumowanie sesji bez uszkadzania pliku `game_config.yaml`.
