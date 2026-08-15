# Raport Użyteczności i Wpływu Elementów Gry (Ablation & Impact Audit) — Wersja: v0.32

**Wersja Gry:** `v0.32` | **Data:** 2026-08-15 08:35 | **Próba:** 500 gier/setup (8000 gier/test) | **Czas Analizy:** 206.0s

Raport przedstawia wyniki badania ablacyjnego (**Feature Importance / Ablation Study**).
Dla każdego elementu zbadano zachowanie ekosystemu gry **po jego całkowitym wyłączeniu**.

---

## 1. Podsumowanie Wniosków Strategicznych

- **👑 Liczba Filarów Frakcji (Kluczowe Karty Wygranych):** `8` kart
- **💤 Liczba Martwych Kart (Kandydaci do Wzmocnienia / Reworku):** `0` kart
- **⚠️ Liczba Kart Destabilizujących (Kandydaci do Osłabienia):** `27` kart
- **⚖️ Liczba Zbalansowanych Narzędzi Taktycznych:** `15` kart

---

## 2. 👑 Filary Frakcji (Najważniejsze Karty Napędzające Wygraną)

Karty, których wyłączenie drastycznie obniża szanse na zwycięstwo danej frakcji ($\Delta 	ext{Win Share} \ge +3.0\%$):

| Karta | Frakcja | Koszt / Herezja | Win Share (Baza → Bez Karty) | Spadek Szans ($\Delta$) | Global Score po Usunięciu | Rola i Diagnoza |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `kb-10` **Pieczęć Korony** | KB | 2zł / 2☣ | 28.6% → **5.5%** | **`-23.1%`** 🔻 | 24.3 pkt | Kluczowa dla wygranej; usunięcie drastycznie osłabia frakcję. |
| `kb-09` **Dekret Królewski** | KB | 3zł / 1☣ | 28.6% → **7.4%** | **`-21.2%`** 🔻 | 24.3 pkt | Kluczowa dla wygranej; usunięcie drastycznie osłabia frakcję. |
| `caa-10` **Echo Alhambry** | CAA | 0zł / 1☣ | 28.7% → **9.2%** | **`-19.5%`** 🔻 | 25.6 pkt | Kluczowa dla wygranej; usunięcie drastycznie osłabia frakcję. |
| `kb-02` **Pobór Podatków** | KB | 1zł / 0☣ | 28.6% → **17.2%** | **`-11.4%`** 🔻 | 30.5 pkt | Kluczowa dla wygranej; usunięcie drastycznie osłabia frakcję. |
| `gc-09` **Lista Dłużników** | GC | 2zł / 0☣ | 27.8% → **18.2%** | **`-9.6%`** 🔻 | 39.4 pkt | Kluczowa dla wygranej; usunięcie drastycznie osłabia frakcję. |
| `kt-05` **Wskazówka Cyklu** | KT | 1zł / 0☣ | 30.4% → **22.5%** | **`-8.0%`** 🔻 | 58.8 pkt | Kluczowa dla wygranej; usunięcie drastycznie osłabia frakcję. |
| `so-10` **Oczyść Miasto** | SO | 4zł / 2☣ | 29.9% → **24.3%** | **`-5.6%`** 🔻 | 75.9 pkt | Kluczowa dla wygranej; usunięcie drastycznie osłabia frakcję. |
| `so-03` **Podejrzenie** | SO | 1zł / 0☣ | 29.9% → **26.7%** | **`-3.2%`** 🔻 | 83.9 pkt | Kluczowa dla wygranej; usunięcie drastycznie osłabia frakcję. |

---

## 3. 💤 Martwe Karty (Kandydaci do Wzmocnienia lub Reworku)

Karty, których usunięcie z gry nie wywołuje niemal żadnego mierzalnego efektu ($|\Delta 	ext{Win Share}| \le 0.6\%$). Są rzadko zagrywane lub ich efekt jest zbyt słaby:

| Karta | Frakcja | Koszt / Herezja | Win Share (Baza → Bez Karty) | Wpływ ($\Delta$) | Status Rekomendacji |
| :--- | :---: | :---: | :---: | :---: | :--- |
| — | — | — | — | — | ✅ Brak całkowicie martwych kart w talii! |

---

## 4. ⚠️ Karty Destabilizujące / Toksyczne

Karty, których wyłączenie z talii **podnosi ogólny wynik zbalansowania gry** ($\Delta 	ext{Global} > +1.0$ pkt):

| Karta | Frakcja | Koszt / Herezja | Global Score (Baza → Bez Karty) | Zysk Balansu ($\Delta$) | Diagnoza |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `so-02` **Skarbiec Trybunału** | SO | 1zł / 0☣ | 86.2 → **93.3 pkt** | **`+7.1 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `gc-08` **Zatrute Złoto** | GC | 1zł / 0☣ | 86.2 → **92.5 pkt** | **`+6.3 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `gc-03` **Podrzucenie Księgi** | GC | 1zł / 0☣ | 86.2 → **91.3 pkt** | **`+5.1 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `kt-02` **Transmutacja Złota** | KT | 1zł / 0☣ | 86.2 → **91.3 pkt** | **`+5.1 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `gc-02` **Czarny Rynek** | GC | 1zł / 1☣ | 86.2 → **89.2 pkt** | **`+3.0 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `caa-06` **Ucieczka z Lochów** | CAA | 2zł / 1☣ | 86.2 → **88.5 pkt** | **`+2.3 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `kt-06` **Przesłuchanie Imienia** | KT | 2zł / 0☣ | 86.2 → **88.0 pkt** | **`+1.8 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `so-05` **Wezwanie do Trybunału** | SO | 0zł / 0☣ | 86.2 → **88.0 pkt** | **`+1.8 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `gc-01` **Przekupiony Strażnik** | GC | 1zł / 1☣ | 86.2 → **86.7 pkt** | **`+0.5 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `gc-04` **Informator** | GC | 0zł / 1☣ | 86.2 → **86.4 pkt** | **`+0.2 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `kb-06` **Areszt Królewski** | KB | 1zł / 0☣ | 86.2 → **86.0 pkt** | **`-0.2 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `caa-02` **Złoto z Kryjówki** | CAA | 1zł / 0☣ | 86.2 → **85.6 pkt** | **`-0.6 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `kb-01` **Rozkaz Dworu** | KB | 1zł / 0☣ | 86.2 → **84.4 pkt** | **`-1.8 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `caa-01` **Przejście Podziemiami** | CAA | 0zł / 0☣ | 86.2 → **82.1 pkt** | **`-4.1 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `kb-04` **Faworyt Dworu** | KB | 2zł / 1☣ | 86.2 → **81.6 pkt** | **`-4.6 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `caa-03` **Cień na Rynku** | CAA | 0zł / 1☣ | 86.2 → **81.3 pkt** | **`-4.9 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `gc-05` **Fałszywy Świadek** | GC | 0zł / 0☣ | 86.2 → **79.9 pkt** | **`-6.3 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `kb-07` **Szantaż Pieczęcią** | KB | 2zł / 0☣ | 86.2 → **78.7 pkt** | **`-7.5 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `gc-10` **Upadek Domu** | GC | 4zł / 2☣ | 86.2 → **76.0 pkt** | **`-10.2 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `kt-04` **Zwierciadło Herezji** | KT | 0zł / 0☣ | 86.2 → **74.9 pkt** | **`-11.3 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `gc-07` **Skrytobójstwo** | GC | 2zł / 1☣ | 86.2 → **70.8 pkt** | **`-15.4 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `caa-09` **Kurier Relikwii** | CAA | 2zł / 0☣ | 86.2 → **70.4 pkt** | **`-15.8 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `kb-03` **Plotka Dworska** | KB | 1zł / 0☣ | 86.2 → **70.4 pkt** | **`-15.8 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `caa-04` **Fałszywy Trop** | CAA | 1zł / 0☣ | 86.2 → **69.4 pkt** | **`-16.8 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `caa-07` **Szantaż Bractwa** | CAA | 2zł / 0☣ | 86.2 → **63.4 pkt** | **`-22.8 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `caa-08` **Kaptur Nocy** | CAA | 1zł / 1☣ | 86.2 → **53.5 pkt** | **`-32.7 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |
| `kb-05` **List Żelazny** | KB | 2zł / 0☣ | 86.2 → **45.7 pkt** | **`-40.5 pkt`** 🟢 | Usunięcie poprawia ogólny balans stołu lub redukuje toksyczną dominację. |

---

## 5. 📋 Pełna Tabela Ablacji Wszystkich 50 Kart Frakcji

| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Faction Win Share | $\Delta$ Frakcji | Global Score | $\Delta$ Global | Śr. Er | Deadlock % | Kategoria Roli |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `caa-01` | **Przejście Podziemiami** | CAA | 0 | 0 | 28.7% → 31.9% | `+3.3%` | 82.1 | `-4.1` | 5.49 | 1.1% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `caa-02` | **Złoto z Kryjówki** | CAA | 1 | 0 | 28.7% → 32.8% | `+4.1%` | 85.6 | `-0.6` | 5.50 | 1.0% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `caa-03` | **Cień na Rynku** | CAA | 0 | 1 | 28.7% → 34.4% | `+5.7%` | 81.3 | `-4.9` | 5.58 | 1.4% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `caa-04` | **Fałszywy Trop** | CAA | 1 | 0 | 28.7% → 36.2% | `+7.5%` | 69.4 | `-16.8` | 5.48 | 1.1% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `caa-05` | **Ukryty Kurier** | CAA | 1 | 0 | 28.7% → 29.1% | `+0.4%` | 81.1 | `-5.1` | 5.53 | 1.1% | ⚖️ ZBALANSOWANE NARZĘDZIE |
| `caa-06` | **Ucieczka z Lochów** | CAA | 2 | 1 | 28.7% → 28.1% | `-0.6%` | 88.5 | `+2.3` | 5.57 | 1.3% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `caa-07` | **Szantaż Bractwa** | CAA | 2 | 0 | 28.7% → 34.5% | `+5.8%` | 63.4 | `-22.8` | 5.43 | 1.0% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `caa-08` | **Kaptur Nocy** | CAA | 1 | 1 | 28.7% → 39.6% | `+11.0%` | 53.5 | `-32.7` | 5.47 | 1.1% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `caa-09` | **Kurier Relikwii** | CAA | 2 | 0 | 28.7% → 31.6% | `+3.0%` | 70.4 | `-15.8` | 5.52 | 1.0% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `caa-10` | **Echo Alhambry** | CAA | 0 | 1 | 28.7% → 9.2% | `-19.5%` | 25.6 | `-60.6` | 5.91 | 2.6% | 👑 FILAR FRAKCJI |
| `gc-01` | **Przekupiony Strażnik** | GC | 1 | 1 | 27.8% → 32.8% | `+5.0%` | 86.7 | `+0.5` | 5.53 | 1.1% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `gc-02` | **Czarny Rynek** | GC | 1 | 1 | 27.8% → 27.6% | `-0.2%` | 89.2 | `+3.0` | 5.62 | 1.3% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `gc-03` | **Podrzucenie Księgi** | GC | 1 | 0 | 27.8% → 27.8% | `-0.1%` | 91.3 | `+5.1` | 5.59 | 1.1% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `gc-04` | **Informator** | GC | 0 | 1 | 27.8% → 31.5% | `+3.7%` | 86.4 | `+0.2` | 5.55 | 1.1% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `gc-05` | **Fałszywy Świadek** | GC | 0 | 0 | 27.8% → 30.3% | `+2.5%` | 79.9 | `-6.3` | 5.52 | 1.0% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `gc-06` | **Szantaż** | GC | 2 | 0 | 27.8% → 25.0% | `-2.8%` | 76.2 | `-10.0` | 5.57 | 1.3% | ⚖️ ZBALANSOWANE NARZĘDZIE |
| `gc-07` | **Skrytobójstwo** | GC | 2 | 1 | 27.8% → 35.0% | `+7.2%` | 70.8 | `-15.4` | 5.45 | 0.9% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `gc-08` | **Zatrute Złoto** | GC | 1 | 0 | 27.8% → 26.8% | `-1.0%` | 92.5 | `+6.3` | 5.60 | 1.1% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `gc-09` | **Lista Dłużników** | GC | 2 | 0 | 27.8% → 18.2% | `-9.6%` | 39.4 | `-46.8` | 5.64 | 1.3% | 👑 FILAR FRAKCJI |
| `gc-10` | **Upadek Domu** | GC | 4 | 2 | 27.8% → 33.3% | `+5.5%` | 76.0 | `-10.2` | 5.56 | 1.3% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `kb-01` | **Rozkaz Dworu** | KB | 1 | 0 | 28.6% → 33.5% | `+4.9%` | 84.4 | `-1.8` | 5.50 | 0.7% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `kb-02` | **Pobór Podatków** | KB | 1 | 0 | 28.6% → 17.2% | `-11.4%` | 30.5 | `-55.7` | 5.67 | 1.2% | 👑 FILAR FRAKCJI |
| `kb-03` | **Plotka Dworska** | KB | 1 | 0 | 28.6% → 33.6% | `+4.9%` | 70.4 | `-15.8` | 5.53 | 0.8% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `kb-04` | **Faworyt Dworu** | KB | 2 | 1 | 28.6% → 32.8% | `+4.2%` | 81.6 | `-4.6` | 5.51 | 0.7% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `kb-05` | **List Żelazny** | KB | 2 | 0 | 28.6% → 41.6% | `+13.0%` | 45.7 | `-40.5` | 5.33 | 0.4% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `kb-06` | **Areszt Królewski** | KB | 1 | 0 | 28.6% → 32.8% | `+4.1%` | 86.0 | `-0.2` | 5.48 | 0.7% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `kb-07` | **Szantaż Pieczęcią** | KB | 2 | 0 | 28.6% → 32.9% | `+4.2%` | 78.7 | `-7.5` | 5.51 | 0.7% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `kb-08` | **Przekupstwo Sędziego** | KB | 3 | 0 | 28.6% → 30.4% | `+1.8%` | 79.5 | `-6.7` | 5.54 | 1.0% | ⚖️ ZBALANSOWANE NARZĘDZIE |
| `kb-09` | **Dekret Królewski** | KB | 3 | 1 | 28.6% → 7.4% | `-21.2%` | 24.3 | `-61.9` | 5.75 | 1.4% | 👑 FILAR FRAKCJI |
| `kb-10` | **Pieczęć Korony** | KB | 2 | 2 | 28.6% → 5.5% | `-23.1%` | 24.3 | `-61.9` | 5.95 | 3.3% | 👑 FILAR FRAKCJI |
| `kt-01` | **Rytuał Przejścia** | KT | 1 | 0 | 30.4% → 31.2% | `+0.8%` | 86.5 | `+0.3` | 5.56 | 1.4% | ⚖️ ZBALANSOWANE NARZĘDZIE |
| `kt-02` | **Transmutacja Złota** | KT | 1 | 0 | 30.4% → 30.6% | `+0.2%` | 91.3 | `+5.1` | 5.56 | 1.3% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `kt-03` | **Zakazana Wiedza** | KT | 0 | 1 | 30.4% → 32.4% | `+2.0%` | 87.5 | `+1.3` | 5.55 | 1.0% | ⚖️ ZBALANSOWANE NARZĘDZIE |
| `kt-04` | **Zwierciadło Herezji** | KT | 0 | 0 | 30.4% → 33.1% | `+2.7%` | 74.9 | `-11.3` | 5.61 | 1.2% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `kt-05` | **Wskazówka Cyklu** | KT | 1 | 0 | 30.4% → 22.5% | `-8.0%` | 58.8 | `-27.4` | 5.64 | 2.0% | 👑 FILAR FRAKCJI |
| `kt-06` | **Przesłuchanie Imienia** | KT | 2 | 0 | 30.4% → 29.7% | `-0.8%` | 88.0 | `+1.8` | 5.60 | 1.2% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `kt-07` | **Archiwum Ukryte** | KT | 1 | 0 | 30.4% → 31.1% | `+0.7%` | 81.8 | `-4.4` | 5.55 | 1.2% | ⚖️ ZBALANSOWANE NARZĘDZIE |
| `kt-08` | **Areszt Wiedzy** | KT | 2 | 0 | 30.4% → 29.4% | `-1.0%` | 87.1 | `+0.9` | 5.54 | 1.2% | ⚖️ ZBALANSOWANE NARZĘDZIE |
| `kt-09` | **Fragment Kodeksu** | KT | 1 | 1 | 30.4% → 31.0% | `+0.6%` | 82.2 | `-4.0` | 5.54 | 1.1% | ⚖️ ZBALANSOWANE NARZĘDZIE |
| `kt-10` | **Pieczęć Salomona** | KT | 1 | 0 | 30.4% → 27.7% | `-2.8%` | 84.1 | `-2.1` | 5.56 | 1.7% | ⚖️ ZBALANSOWANE NARZĘDZIE |
| `so-01` | **Patrol Familiariuszy** | SO | 1 | 0 | 29.9% → 30.8% | `+0.9%` | 85.1 | `-1.1` | 5.53 | 1.2% | ⚖️ ZBALANSOWANE NARZĘDZIE |
| `so-02` | **Skarbiec Trybunału** | SO | 1 | 0 | 29.9% → 30.2% | `+0.3%` | 93.3 | `+7.1` | 5.53 | 1.2% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `so-03` | **Podejrzenie** | SO | 1 | 0 | 29.9% → 26.7% | `-3.2%` | 83.9 | `-2.3` | 5.59 | 1.5% | 👑 FILAR FRAKCJI |
| `so-04` | **Publiczne Ostrzeżenie** | SO | 1 | 0 | 29.9% → 30.4% | `+0.5%` | 81.8 | `-4.4` | 5.53 | 1.3% | ⚖️ ZBALANSOWANE NARZĘDZIE |
| `so-05` | **Wezwanie do Trybunału** | SO | 0 | 0 | 29.9% → 31.4% | `+1.5%` | 88.0 | `+1.8` | 5.54 | 1.3% | ⚠️ TOKSYCZNA / DESTABILIZUJĄCA |
| `so-06` | **Areszt Trybunalski** | SO | 2 | 0 | 29.9% → 30.6% | `+0.8%` | 86.2 | `0.0` | 5.55 | 1.2% | ⚖️ ZBALANSOWANE NARZĘDZIE |
| `so-07` | **Przesłuchanie Oficjum** | SO | 2 | 0 | 29.9% → 31.0% | `+1.1%` | 83.6 | `-2.6` | 5.54 | 1.2% | ⚖️ ZBALANSOWANE NARZĘDZIE |
| `so-08` | **Nasłanie Inkwizytora** | SO | 2 | 0 | 29.9% → 30.8% | `+0.9%` | 81.9 | `-4.3` | 5.54 | 1.2% | ⚖️ ZBALANSOWANE NARZĘDZIE |
| `so-09` | **Świadek Koronny** | SO | 2 | 0 | 29.9% → 30.1% | `+0.2%` | 83.0 | `-3.2` | 5.55 | 1.4% | ⚖️ ZBALANSOWANE NARZĘDZIE |
| `so-10` | **Oczyść Miasto** | SO | 4 | 2 | 29.9% → 24.3% | `-5.6%` | 75.9 | `-10.3` | 5.71 | 1.6% | 👑 FILAR FRAKCJI |

---

## 6. ⚙️ Wpływ Mechanik Systemowych i Reguł Gry (Ablacja Systemu)

Analiza wrażliwości ekosystemu gry na modyfikacje parametrów bazowych L1, warunków zwycięstwa L2 oraz dynamiki planszy L4.

### L1 — Rdzeń Systemu i Silnik Gry

| Badany Wariant / Parametr | Global Score | $\Delta$ Global | Średnia Er | Deadlocks % | Pas Biedy % | Diagnoza i Wpływ na Balans |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Próg Oskarżenia: 6/7/8 → 7/8/9** | 86.2 → 🟠 ** 67.9** (`-18.3`) | `-18.3 pkt` | 5.72 Er | 1.4% | 26.9% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Próg Oskarżenia: 6/7/8 → 5/6/7** | 86.2 → 🟠 ** 74.9** (`-11.3`) | `-11.3 pkt` | 5.43 Er | 1.1% | 25.9% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Limit Er: 10 → 11** | 86.2 → 🟡 ** 86.1** (`-0.1`) | `-0.1 pkt` | 5.57 Er | 0.4% | 26.3% | ⚪ Wpływ neutralny / zrównoważony |
| **Limit Er: 10 → 9** | 86.2 → 🟡 ** 85.6** (`-0.6`) | `-0.6 pkt` | 5.55 Er | 2.9% | 26.3% | ⚪ Wpływ neutralny / zrównoważony |
| **Złoto startowe: 3/3/2zł → 4/4/3zł** | 86.2 → 🟠 ** 72.6** (`-13.6`) | `-13.6 pkt` | 5.42 Er | 1.1% | 24.3% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Złoto startowe: 3/3/2zł → 2/2/1zł** | 86.2 → 🔴 ** 44.5** (`-41.7`) | `-41.7 pkt` | 5.87 Er | 1.8% | 27.3% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Agenci: 3 → 4** | 86.2 → 🟡 ** 83.8** (`-2.4`) | `-2.4 pkt` | 5.52 Er | 1.0% | 26.2% | 🟠 Umiarkowany spadek zbalansowania |
| **Agenci: 3 → 2** | 86.2 → 🟠 ** 64.3** (`-21.9`) | `-21.9 pkt` | 5.76 Er | 2.0% | 27.0% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Limit ręki: 5 → 6** | 86.2 → 🔴 ** 57.4** (`-28.8`) | `-28.8 pkt` | 5.36 Er | 0.8% | 21.2% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Limit ręki: 5 → 4** | 86.2 → 🟠 ** 64.8** (`-21.4`) | `-21.4 pkt` | 5.84 Er | 2.2% | 32.8% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Cooldown Autodafé: 3 → 4 Ery** | 86.2 → 🟢 ** 90.1** (`⬆️ +3.9`) | `+3.9 pkt` | 5.57 Er | 1.2% | 26.3% | 🟢 Zysk balansu — parametr warto rozważyć do trwałej adaptacji |
| **Cooldown Autodafé: 3 → 2 Ery** | 86.2 → 🟡 ** 87.0** (`⬆️ +0.8`) | `+0.8 pkt` | 5.55 Er | 1.2% | 26.3% | ⚪ Wpływ neutralny / zrównoważony |

### L2 — Warunki Zwycięstwa Frakcji

| Badany Wariant / Parametr | Global Score | $\Delta$ Global | Średnia Er | Deadlocks % | Pas Biedy % | Diagnoza i Wpływ na Balans |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Oficjum Stosy: 3/4/4 → 4/5/5** | 86.2 → 🔴 ** 58.8** (`-27.4`) | `-27.4 pkt` | 5.66 Er | 1.5% | 26.6% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Oficjum Stosy: 3/4/4 → 2/3/3** | 86.2 → 🔴 ** 35.9** (`-50.3`) | `-50.3 pkt` | 5.36 Er | 0.8% | 25.6% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Oficjum Skazania: 2 → 3** | 86.2 → 🟡 ** 76.0** (`-10.2`) | `-10.2 pkt` | 5.61 Er | 1.3% | 26.5% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Oficjum Skazania: 2 → 1** | 86.2 → 🔴 ** 25.9** (`-60.3`) | `-60.3 pkt` | 4.63 Er | 0.6% | 22.4% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Cienie Relikwie: 2 → 3** | 86.2 → 🔴 ** 25.6** (`-60.6`) | `-60.6 pkt` | 5.92 Er | 1.9% | 27.4% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Cienie Relikwie: 2 → 1** | 86.2 → 🔴 ** 25.6** (`-60.6`) | `-60.6 pkt` | 4.02 Er | 0.5% | 21.3% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Cienie Era: 5 → 6** | 86.2 → 🟡 ** 87.8** (`⬆️ +1.6`) | `+1.6 pkt` | 5.58 Er | 1.2% | 26.4% | 🟢 Zysk balansu — parametr warto rozważyć do trwałej adaptacji |
| **Cienie Era: 5 → 4** | 86.2 → 🟡 ** 86.7** (`⬆️ +0.5`) | `+0.5 pkt` | 5.56 Er | 1.2% | 26.3% | ⚪ Wpływ neutralny / zrównoważony |
| **Korona Era: 6/5/5 → 7/6/6** | 86.2 → 🟠 ** 60.2** (`-26.0`) | `-26.0 pkt` | 5.69 Er | 1.2% | 26.8% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Korona Era: 6/5/5 → 5/4/4** | 86.2 → 🟡 ** 83.0** (`-3.2`) | `-3.2 pkt` | 5.45 Er | 1.2% | 25.9% | 🟠 Umiarkowany spadek zbalansowania |
| **Korona Dekrety: 2 → 3** | 86.2 → 🔴 ** 24.3** (`-61.9`) | `-61.9 pkt` | 5.77 Er | 2.5% | 27.0% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Korona Dekrety: 2 → 1** | 86.2 → 🔴 ** 24.3** (`-61.9`) | `-61.9 pkt` | 5.24 Er | 0.3% | 25.1% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Korona Haki: 0 → 1** | 86.2 → 🔴 ** 42.4** (`-43.8`) | `-43.8 pkt` | 5.63 Er | 1.3% | 26.6% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Kabała Fragmenty: 3 → 4** | 86.2 → 🟠 ** 74.3** (`-11.9`) | `-11.9 pkt` | 5.65 Er | 1.6% | 26.6% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Kabała Fragmenty: 3 → 2** | 86.2 → 🟡 ** 76.7** (`-9.5`) | `-9.5 pkt` | 5.53 Er | 1.1% | 26.2% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Kabała Era: 7/6/6 → 8/7/7** | 86.2 → 🔴 ** 50.8** (`-35.4`) | `-35.4 pkt` | 5.73 Er | 1.4% | 26.9% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Kabała Era: 7/6/6 → 6/5/5** | 86.2 → 🔴 ** 34.2** (`-52.0`) | `-52.0 pkt` | 5.37 Er | 1.0% | 25.5% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Kabała Pasmo: 3–8 → 2–8** | 86.2 → 🟡 ** 86.4** (`⬆️ +0.2`) | `+0.2 pkt` | 5.56 Er | 1.2% | 26.3% | ⚪ Wpływ neutralny / zrównoważony |
| **Kabała Pasmo: 3–8 → 4–8** | 86.2 → 🟡 ** 86.6** (`⬆️ +0.4`) | `+0.4 pkt` | 5.58 Er | 1.2% | 26.4% | ⚪ Wpływ neutralny / zrównoważony |
| **Kabała Pasmo: 3–8 → 3–9** | 86.2 → 🟡 ** 86.1** (`-0.1`) | `-0.1 pkt` | 5.55 Er | 1.0% | 26.3% | ⚪ Wpływ neutralny / zrównoważony |
| **Kabała Pasmo: 3–8 → 3–7** | 86.2 → 🟡 ** 87.1** (`⬆️ +0.9`) | `+0.9 pkt` | 5.60 Er | 1.6% | 26.4% | ⚪ Wpływ neutralny / zrównoważony |
| **Gildia Upadki (default/bez SO): 2/3 → 3/4** | 86.2 → 🔴 ** 27.4** (`-58.8`) | `-58.8 pkt` | 5.79 Er | 1.6% | 27.0% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Gildia Upadki (default/bez SO): 2/3 → 1/2** | 86.2 → 🔴 ** 24.2** (`-62.0`) | `-62.0 pkt` | 4.96 Er | 0.8% | 24.7% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Gildia Upadki (z Oficjum): 2 → 3** | 86.2 → 🔴 ** 45.2** (`-41.0`) | `-41.0 pkt` | 5.71 Er | 1.3% | 26.7% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Gildia Upadki (z Oficjum): 2 → 1** | 86.2 → 🔴 ** 45.2** (`-41.0`) | `-41.0 pkt` | 5.09 Er | 1.0% | 25.2% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Gildia Upadki (bez Oficjum): 3 → 4** | 86.2 → 🟠 ** 74.3** (`-11.9`) | `-11.9 pkt` | 5.65 Er | 1.5% | 26.6% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Gildia Upadki (bez Oficjum): 3 → 2** | 86.2 → 🟠 ** 72.2** (`-14.0`) | `-14.0 pkt` | 5.43 Er | 1.0% | 25.9% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |

### L4 — Warianty Niszowe, Edykty i Plansza

| Badany Wariant / Parametr | Global Score | $\Delta$ Global | Średnia Er | Deadlocks % | Pas Biedy % | Diagnoza i Wpływ na Balans |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Edykty Czasu: co 1 Erę → co 1 Erę** | 🟡 ** 86.2** | `0.0 pkt` | 5.57 Er | 1.2% | 26.3% | ⚪ Wpływ neutralny / zrównoważony |
| **Edykty Czasu: co 1 Erę → co 2 Ery** | 86.2 → 🟡 ** 81.9** (`-4.3`) | `-4.3 pkt` | 5.76 Er | 1.7% | 27.0% | 🟠 Umiarkowany spadek zbalansowania |
| **Szlak Morski: Era 5 → Era 4** | 86.2 → 🟡 ** 87.6** (`⬆️ +1.4`) | `+1.4 pkt` | 5.55 Er | 1.2% | 26.3% | 🟢 Zysk balansu — parametr warto rozważyć do trwałej adaptacji |
| **Szlak Morski: Era 5 → Era 6** | 86.2 → 🟡 ** 82.7** (`-3.5`) | `-3.5 pkt` | 5.58 Er | 1.2% | 26.4% | 🟠 Umiarkowany spadek zbalansowania |
| **Inkwizytor Patrol: ruch 1 → 2** | 86.2 → 🟢 ** 91.7** (`⬆️ +5.5`) | `+5.5 pkt` | 5.59 Er | 1.2% | 26.4% | 🟢 Zysk balansu — parametr warto rozważyć do trwałej adaptacji |
| **Inkwizytor Patrol: ruch 1 → 0** | 86.2 → 🟡 ** 76.7** (`-9.5`) | `-9.5 pkt` | 5.37 Er | 0.8% | 25.6% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |
| **Werdykt: jawny → tajny** | 🟡 ** 86.2** | `0.0 pkt` | 5.57 Er | 1.2% | 26.3% | ⚪ Wpływ neutralny / zrównoważony |

### L1 — Ekstremalna Ablacja

| Badany Wariant / Parametr | Global Score | $\Delta$ Global | Średnia Er | Deadlocks % | Pas Biedy % | Diagnoza i Wpływ na Balans |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Autodafé bez Cooldownu (możliwość co turę)** | 86.2 → 🟡 ** 83.8** (`-2.4`) | `-2.4 pkt` | 5.53 Er | 1.1% | 26.2% | 🟠 Umiarkowany spadek zbalansowania |
| **Startowe Złoto zredukowane (-2 zł)** | 86.2 → 🔴 ** 18.8** (`-67.4`) | `-67.4 pkt` | 6.15 Er | 3.4% | 30.5% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |

### L4 — Ekstremalna Ablacja

| Badany Wariant / Parametr | Global Score | $\Delta$ Global | Średnia Er | Deadlocks % | Pas Biedy % | Diagnoza i Wpływ na Balans |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Gra bez Kroniki Dziejów (Talia Czasu OFF)** | 86.2 → 🟠 ** 66.8** (`-19.4`) | `-19.4 pkt` | 5.93 Er | 2.9% | 27.5% | 🔴 Silna destabilizacja gry — kluczowy filar stabilności |

---

## 7. Metodologia Badania

- **Ablacja Pojedynczego Elementu (Leave-One-Out):** Każdy test usuwa dokładnie 1 kartę lub zmienia 1 mechanikę bazową.
- **Wpływ na Frakcję ($\Delta$ Win Share):** Różnica $WS_{	ext{baza}} - WS_{	ext{bez\_karty}}$. Dodatnia wartość oznacza, że karta napędzała wygrane frakcji.
- **Wpływ na Balans Gry ($\Delta$ Global):** Zmiana wyniku globalnego po usunięciu elementu.
- **Rygor Próby:** Każdy wariant jest testowany na pełnym pakiecie 16 setupów (min. 1000 gier/setup = 16 000 partii na kartę).