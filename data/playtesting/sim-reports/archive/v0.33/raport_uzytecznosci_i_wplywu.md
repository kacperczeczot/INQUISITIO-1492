# Raport Użyteczności i Wpływu Elementów Gry (5-Warstwowy Audyt Ablacyjny) — Wersja: v0.33

**Wersja Gry:** `v0.33` | **Data:** 2026-08-15 10:47 | **Próba:** 1000 gier/setup (16000 gier/test) | **Czas Analizy:** 423.7s

Kompleksowy audyt badania wkładu poszczególnych elementów gry w balans ekosystemu (**Leave-One-Out Feature Importance**).
Analiza obejmuje 5 komplementarnych warstw architektury mechanicznej *INQUISITIO-1492*.

---

## 1. 🏛️ Architektura 5 Warstw Badania Ablacyjnego

| Warstwa Architektury | Badany Zakres Elementów | Liczba Testów | Kluczowy Wskaźnik |
| :--- | :--- | :---: | :--- |
| **Warstwa I: Karty Frakcyjne** | 50 kart akcji, reakcji i permanentów (po 10 na frakcję) | `50` | Matryca 3x3 (Filar vs Kotwica vs Destabilizator) |
| **Warstwa II: Kronika Dziejów** | 8 kart wydarzeń z Talii Czasu | `8` | Wpływ na tempo partii i stabilność metagry |
| **Warstwa III: Mechaniki Silnika** | Inkwizytor, Autodafé, Limit ręki, Złoto startowe | `6` | Odporność rdzenia na skrajne modyfikatory |
| **Warstwa IV: Ścieżki Zwycięstwa** | Bramki frakcyjne (Haki KB, Pasmo KT, Szlak CAA, Stosy SO) | `7` | Krytyczność asymetrycznych warunków wygranej |
| **Warstwa V: Skalowanie Stołu** | Formaty 3-osobowe, 4-osobowe i 5-osobowe (16 setupów) | `16` | Symetria i brak dominacji przy różnej liczbie graczy |

---

## 2. 🃏 Warstwa I — Karty Frakcyjne (Symetryczna Matryca 3x3)

Wszystkie 50 kart frakcji sklasyfikowano na przecięciu dwóch ortogonalnych osi:
- **Oś Globalna (Stół):** Wpływ wyłączenia karty na ogólny stan balansu gry ($\Delta \text{Global Score}$).
- **Oś Lokalna (Frakcja):** Wpływ wyłączenia karty na szanse zwycięstwa danej frakcji ($\Delta \text{Faction Share}$).

| Grupa Ekosystemu \ Profil Frakcji | 🛑 Hamulec Tempa (Δ ≤ -2.0%) | ⚪ Narzędzie Taktyczne (Neutralne) | 👑 Motor Wygranych (Δ ≥ +2.5%) | ŁĄCZNIE |
| :--- | :---: | :---: | :---: | :---: |
| **⚠️ I. Destabilizatory Stołu** (Δ Global ≥ +1.0 pkt) | `0` *(Toksyczny Balast)* | `2` *(Toksyczny Zgrzyt)* | `0` *(Toksyczny Dominator)* | **`2`** |
| **⚖️ II. Zbalansowane dla Stołu** (-5.0 < Δ < +1.0 pkt) | `1` *(Zdrowy Hamulec)* | `21` *(Zrównoważone Narzędzie)* | `0` *(Lokalny Silnik)* | **`22`** |
| **⚓ III. Krytyczne dla Balansu** (Δ Global ≤ -5.0 pkt) | `17` *(Kotwica Stołu)* | `1` *(Zwornik Różnorodności)* | `8` *(Filar Frakcji i Stołu)* | **`26`** |
| **ŁĄCZNIE** | **`18`** | **`24`** | **`8`** | **50 kart** |

### 2.1. ⚠️ Destabilizatory Ekosystemu (Kandydaci do Osłabienia / Reworku)
Karty, których wyłączenie **podnosi** ogólny wynik balansu gry ($\Delta \text{Global} \ge +1.0$ pkt):

| Karta | Frakcja | Koszt / Herezja | Podgrupa 3x3 | Global Score (Baza → Bez) | Zysk Balansu ($\Delta$) | Win Share Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kt-02` **Transmutacja Złota** | KT | 1zł / 0☣ | ⚠️⚪ Toksyczny Zgrzyt | 93.9 → **95.5 pkt** | **`+1.6 pkt`** 🟢 | 29.9% → 29.8% (`+0.1%`) |
| `so-05` **Wezwanie do Trybunału** | SO | 0zł / 0☣ | ⚠️⚪ Toksyczny Zgrzyt | 93.9 → **95.4 pkt** | **`+1.5 pkt`** 🟢 | 28.8% → 29.7% (`-0.8%`) |

### 2.2. ⚓ Karty Krytyczne dla Balansu Stołu (Filary i Kotwice)
Karty, których wyłączenie **drastycznie załamuje** równowagę gry ($\Delta \text{Global} \le -5.0$ pkt):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 3x3 | Win Share Frakcji (Baza → Bez) | Wpływ na Frakcję ($\Delta$) | Global Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kb-09` **Dekret Królewski** | KB | 3zł / 1☣ | ⚓👑 Filar Frakcji i Stołu | 28.6% → **8.0%** | **`-20.6%`** 🔻 | 93.9 → **26.5 pkt** (`-67.4`) |
| `kb-10` **Pieczęć Korony** | KB | 2zł / 2☣ | ⚓👑 Filar Frakcji i Stołu | 28.6% → **4.9%** | **`-23.7%`** 🔻 | 93.9 → **26.5 pkt** (`-67.4`) |
| `caa-10` **Echo Alhambry** | CAA | 0zł / 1☣ | ⚓👑 Filar Frakcji i Stołu | 28.9% → **9.4%** | **`-19.5%`** 🔻 | 93.9 → **27.9 pkt** (`-66.0`) |
| `kb-02` **Pobór Podatków** | KB | 1zł / 0☣ | ⚓👑 Filar Frakcji i Stołu | 28.6% → **17.6%** | **`-11.0%`** 🔻 | 93.9 → **33.2 pkt** (`-60.7`) |
| `gc-09` **Lista Dłużników** | GC | 2zł / 0☣ | ⚓👑 Filar Frakcji i Stołu | 29.2% → **19.2%** | **`-10.1%`** 🔻 | 93.9 → **47.5 pkt** (`-46.4`) |
| `kt-05` **Wskazówka Cyklu** | KT | 1zł / 0☣ | ⚓👑 Filar Frakcji i Stołu | 29.9% → **22.4%** | **`-7.5%`** 🔻 | 93.9 → **67.4 pkt** (`-26.5`) |
| `so-10` **Oczyść Miasto** | SO | 4zł / 2☣ | ⚓👑 Filar Frakcji i Stołu | 28.8% → **23.4%** | **`-5.4%`** 🔻 | 93.9 → **72.2 pkt** (`-21.7`) |
| `gc-06` **Szantaż** | GC | 2zł / 0☣ | ⚓👑 Filar Frakcji i Stołu | 29.2% → **25.8%** | **`-3.4%`** 🔻 | 93.9 → **77.9 pkt** (`-16.0`) |
| `kb-05` **List Żelazny** | KB | 2zł / 0☣ | ⚓🛑 Kotwica Stołu (Bezpiecznik) | 28.6% → **42.6%** | **`+14.0%`** 🚀 | 93.9 → **37.4 pkt** (`-56.5`) |
| `caa-08` **Kaptur Nocy** | CAA | 1zł / 1☣ | ⚓🛑 Kotwica Stołu (Bezpiecznik) | 28.9% → **40.2%** | **`+11.3%`** 🚀 | 93.9 → **54.0 pkt** (`-39.9`) |
| `caa-04` **Fałszywy Trop** | CAA | 1zł / 0☣ | ⚓🛑 Kotwica Stołu (Bezpiecznik) | 28.9% → **36.4%** | **`+7.4%`** 🚀 | 93.9 → **66.8 pkt** (`-27.1`) |
| `kt-04` **Zwierciadło Herezji** | KT | 0zł / 0☣ | ⚓🛑 Kotwica Stołu (Bezpiecznik) | 29.9% → **32.2%** | **`+2.4%`** 🚀 | 93.9 → **70.1 pkt** (`-23.8`) |
| `caa-07` **Szantaż Bractwa** | CAA | 2zł / 0☣ | ⚓🛑 Kotwica Stołu (Bezpiecznik) | 28.9% → **35.2%** | **`+6.3%`** 🚀 | 93.9 → **76.6 pkt** (`-17.3`) |
| `gc-07` **Skrytobójstwo** | GC | 2zł / 1☣ | ⚓🛑 Kotwica Stołu (Bezpiecznik) | 29.2% → **34.6%** | **`+5.4%`** 🚀 | 93.9 → **77.9 pkt** (`-16.0`) |
| `gc-10` **Upadek Domu** | GC | 4zł / 2☣ | ⚓🛑 Kotwica Stołu (Bezpiecznik) | 29.2% → **33.5%** | **`+4.3%`** 🚀 | 93.9 → **78.0 pkt** (`-15.9`) |
| `caa-03` **Cień na Rynku** | CAA | 0zł / 1☣ | ⚓🛑 Kotwica Stołu (Bezpiecznik) | 28.9% → **34.8%** | **`+5.8%`** 🚀 | 93.9 → **79.5 pkt** (`-14.4`) |
| `kb-03` **Plotka Dworska** | KB | 1zł / 0☣ | ⚓🛑 Kotwica Stołu (Bezpiecznik) | 28.6% → **33.4%** | **`+4.7%`** 🚀 | 93.9 → **79.6 pkt** (`-14.3`) |
| `caa-02` **Złoto z Kryjówki** | CAA | 1zł / 0☣ | ⚓🛑 Kotwica Stołu (Bezpiecznik) | 28.9% → **33.5%** | **`+4.6%`** 🚀 | 93.9 → **85.3 pkt** (`-8.6`) |
| `caa-09` **Kurier Relikwii** | CAA | 2zł / 0☣ | ⚓🛑 Kotwica Stołu (Bezpiecznik) | 28.9% → **32.3%** | **`+3.4%`** 🚀 | 93.9 → **85.5 pkt** (`-8.4`) |
| `kb-07` **Szantaż Pieczęcią** | KB | 2zł / 0☣ | ⚓🛑 Kotwica Stołu (Bezpiecznik) | 28.6% → **32.8%** | **`+4.2%`** 🚀 | 93.9 → **85.9 pkt** (`-8.0`) |
| `kb-04` **Faworyt Dworu** | KB | 2zł / 1☣ | ⚓🛑 Kotwica Stołu (Bezpiecznik) | 28.6% → **33.4%** | **`+4.8%`** 🚀 | 93.9 → **86.1 pkt** (`-7.8`) |
| `kb-01` **Rozkaz Dworu** | KB | 1zł / 0☣ | ⚓🛑 Kotwica Stołu (Bezpiecznik) | 28.6% → **33.0%** | **`+4.4%`** 🚀 | 93.9 → **86.3 pkt** (`-7.6`) |
| `caa-01` **Przejście Podziemiami** | CAA | 0zł / 0☣ | ⚓🛑 Kotwica Stołu (Bezpiecznik) | 28.9% → **32.8%** | **`+3.8%`** 🚀 | 93.9 → **86.6 pkt** (`-7.3`) |
| `gc-01` **Przekupiony Strażnik** | GC | 1zł / 1☣ | ⚓🛑 Kotwica Stołu (Bezpiecznik) | 29.2% → **33.9%** | **`+4.7%`** 🚀 | 93.9 → **86.7 pkt** (`-7.2`) |
| `kb-06` **Areszt Królewski** | KB | 1zł / 0☣ | ⚓🛑 Kotwica Stołu (Bezpiecznik) | 28.6% → **32.9%** | **`+4.3%`** 🚀 | 93.9 → **86.8 pkt** (`-7.1`) |
| `caa-05` **Ukryty Kurier** | CAA | 1zł / 0☣ | ⚓⚪ Zwornik Różnorodności | 28.9% → **30.9%** | `-1.9%` | 93.9 → **85.1 pkt** (`-8.8`) |

### 2.3. ⚖️ Karty Zbalansowane i Narzędzia Taktyczne
Karty o stabilnym, neutralnym wpływie na stół ($-5.0 < \Delta \text{Global} < +1.0$ pkt):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 3x3 | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | Global Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `gc-08` **Zatrute Złoto** | GC | 1zł / 0☣ | ⚖️⚪ Zrównoważone Narzędzie | 29.2% → 26.8% | `+2.5%` | 92.3 pkt (`-1.6`) |
| `gc-05` **Fałszywy Świadek** | GC | 0zł / 0☣ | ⚖️🛑 Zdrowy Hamulec | 29.2% → 31.2% | `-2.0%` | 91.6 pkt (`-2.3`) |
| `gc-04` **Informator** | GC | 0zł / 1☣ | ⚖️⚪ Zrównoważone Narzędzie | 29.2% → 31.2% | `-2.0%` | 94.8 pkt (`+0.9`) |
| `kt-10` **Pieczęć Salomona** | KT | 1zł / 0☣ | ⚖️⚪ Zrównoważone Narzędzie | 29.9% → 28.0% | `+1.9%` | 92.2 pkt (`-1.7`) |
| `kb-08` **Przekupstwo Sędziego** | KB | 3zł / 0☣ | ⚖️⚪ Zrównoważone Narzędzie | 28.6% → 30.4% | `-1.8%` | 92.3 pkt (`-1.6`) |
| `kt-03` **Zakazana Wiedza** | KT | 0zł / 1☣ | ⚖️⚪ Zrównoważone Narzędzie | 29.9% → 31.3% | `-1.4%` | 94.6 pkt (`+0.7`) |
| `so-07` **Przesłuchanie Oficjum** | SO | 2zł / 0☣ | ⚖️⚪ Zrównoważone Narzędzie | 28.8% → 30.1% | `-1.3%` | 91.6 pkt (`-2.3`) |
| `so-06` **Areszt Trybunalski** | SO | 2zł / 0☣ | ⚖️⚪ Zrównoważone Narzędzie | 28.8% → 30.1% | `-1.2%` | 93.2 pkt (`-0.7`) |
| `kt-06` **Przesłuchanie Imienia** | KT | 2zł / 0☣ | ⚖️⚪ Zrównoważone Narzędzie | 29.9% → 31.0% | `-1.1%` | 90.8 pkt (`-3.1`) |
| `so-01` **Patrol Familiariuszy** | SO | 1zł / 0☣ | ⚖️⚪ Zrównoważone Narzędzie | 28.8% → 29.9% | `-1.1%` | 90.9 pkt (`-3.0`) |
| `so-03` **Podejrzenie** | SO | 2zł / 0☣ | ⚖️⚪ Zrównoważone Narzędzie | 28.8% → 27.8% | `+1.0%` | 94.0 pkt (`+0.1`) |
| `so-02` **Skarbiec Trybunału** | SO | 1zł / 0☣ | ⚖️⚪ Zrównoważone Narzędzie | 28.8% → 27.9% | `+1.0%` | 94.8 pkt (`+0.9`) |
| `kt-08` **Areszt Wiedzy** | KT | 2zł / 0☣ | ⚖️⚪ Zrównoważone Narzędzie | 29.9% → 29.0% | `+0.9%` | 90.2 pkt (`-3.7`) |
| `caa-06` **Ucieczka z Lochów** | CAA | 2zł / 1☣ | ⚖️⚪ Zrównoważone Narzędzie | 28.9% → 29.8% | `-0.9%` | 93.9 pkt (`+0.0`) |
| `gc-03` **Podrzucenie Księgi** | GC | 1zł / 0☣ | ⚖️⚪ Zrównoważone Narzędzie | 29.2% → 28.4% | `+0.8%` | 94.2 pkt (`+0.3`) |
| `so-04` **Publiczne Ostrzeżenie** | SO | 1zł / 0☣ | ⚖️⚪ Zrównoważone Narzędzie | 28.8% → 29.6% | `-0.8%` | 94.5 pkt (`+0.6`) |
| `gc-02` **Czarny Rynek** | GC | 1zł / 1☣ | ⚖️⚪ Zrównoważone Narzędzie | 29.2% → 28.5% | `+0.7%` | 93.2 pkt (`-0.7`) |
| `kt-01` **Rytuał Przejścia** | KT | 1zł / 0☣ | ⚖️⚪ Zrównoważone Narzędzie | 29.9% → 30.5% | `-0.6%` | 90.6 pkt (`-3.3`) |
| `so-09` **Świadek Koronny** | SO | 2zł / 0☣ | ⚖️⚪ Zrównoważone Narzędzie | 28.8% → 29.4% | `-0.5%` | 94.6 pkt (`+0.7`) |
| `kt-07` **Archiwum Ukryte** | KT | 1zł / 0☣ | ⚖️⚪ Zrównoważone Narzędzie | 29.9% → 30.4% | `-0.5%` | 90.3 pkt (`-3.6`) |
| `so-08` **Nasłanie Inkwizytora** | SO | 1zł / 0☣ | ⚖️⚪ Zrównoważone Narzędzie | 28.8% → 29.0% | `-0.2%` | 89.8 pkt (`-4.1`) |
| `kt-09` **Fragment Kodeksu** | KT | 1zł / 1☣ | ⚖️⚪ Zrównoważone Narzędzie | 29.9% → 29.9% | `+0.0%` | 94.0 pkt (`+0.1`) |

### 2.4. 📋 Pełny Wykaz Ablacji Wszystkich 50 Kart Frakcji

| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Faction Win Share | $\Delta$ Frakcji | Global Score | $\Delta$ Global | Śr. Er | Deadlock % | Rola w Matrycy 3x3 |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `caa-01` | **Przejście Podziemiami** | CAA | 0 | 0 | 28.9% → 32.8% | `+3.8%` | 86.6 | `-7.3` | 5.48 | 1.2% | ⚓🛑 Kotwica Stołu (Bezpiecznik) |
| `caa-02` | **Złoto z Kryjówki** | CAA | 1 | 0 | 28.9% → 33.5% | `+4.6%` | 85.3 | `-8.6` | 5.48 | 1.2% | ⚓🛑 Kotwica Stołu (Bezpiecznik) |
| `caa-03` | **Cień na Rynku** | CAA | 0 | 1 | 28.9% → 34.8% | `+5.8%` | 79.5 | `-14.4` | 5.56 | 1.5% | ⚓🛑 Kotwica Stołu (Bezpiecznik) |
| `caa-04` | **Fałszywy Trop** | CAA | 1 | 0 | 28.9% → 36.4% | `+7.4%` | 66.8 | `-27.1` | 5.46 | 1.1% | ⚓🛑 Kotwica Stołu (Bezpiecznik) |
| `caa-05` | **Ukryty Kurier** | CAA | 1 | 0 | 28.9% → 30.9% | `+1.9%` | 85.1 | `-8.8` | 5.50 | 1.1% | ⚓⚪ Zwornik Różnorodności |
| `caa-06` | **Ucieczka z Lochów** | CAA | 2 | 1 | 28.9% → 29.8% | `+0.9%` | 93.9 | `0.0` | 5.55 | 1.5% | ⚖️⚪ Zrównoważone Narzędzie |
| `caa-07` | **Szantaż Bractwa** | CAA | 2 | 0 | 28.9% → 35.2% | `+6.3%` | 76.6 | `-17.3` | 5.44 | 1.1% | ⚓🛑 Kotwica Stołu (Bezpiecznik) |
| `caa-08` | **Kaptur Nocy** | CAA | 1 | 1 | 28.9% → 40.2% | `+11.3%` | 54.0 | `-39.9` | 5.45 | 1.3% | ⚓🛑 Kotwica Stołu (Bezpiecznik) |
| `caa-09` | **Kurier Relikwii** | CAA | 2 | 0 | 28.9% → 32.3% | `+3.4%` | 85.5 | `-8.4` | 5.50 | 1.1% | ⚓🛑 Kotwica Stołu (Bezpiecznik) |
| `caa-10` | **Echo Alhambry** | CAA | 0 | 1 | 28.9% → 9.4% | `-19.5%` | 27.9 | `-66.0` | 5.90 | 2.8% | ⚓👑 Filar Frakcji i Stołu |
| `gc-01` | **Przekupiony Strażnik** | GC | 1 | 1 | 29.2% → 33.9% | `+4.7%` | 86.7 | `-7.2` | 5.51 | 1.2% | ⚓🛑 Kotwica Stołu (Bezpiecznik) |
| `gc-02` | **Czarny Rynek** | GC | 1 | 1 | 29.2% → 28.5% | `-0.7%` | 93.2 | `-0.7` | 5.60 | 1.5% | ⚖️⚪ Zrównoważone Narzędzie |
| `gc-03` | **Podrzucenie Księgi** | GC | 1 | 0 | 29.2% → 28.4% | `-0.8%` | 94.2 | `+0.3` | 5.57 | 1.1% | ⚖️⚪ Zrównoważone Narzędzie |
| `gc-04` | **Informator** | GC | 0 | 1 | 29.2% → 31.2% | `+2.0%` | 94.8 | `+0.9` | 5.55 | 1.3% | ⚖️⚪ Zrównoważone Narzędzie |
| `gc-05` | **Fałszywy Świadek** | GC | 0 | 0 | 29.2% → 31.2% | `+2.0%` | 91.6 | `-2.3` | 5.50 | 1.2% | ⚖️🛑 Zdrowy Hamulec |
| `gc-06` | **Szantaż** | GC | 2 | 0 | 29.2% → 25.8% | `-3.4%` | 77.9 | `-16.0` | 5.55 | 1.1% | ⚓👑 Filar Frakcji i Stołu |
| `gc-07` | **Skrytobójstwo** | GC | 2 | 1 | 29.2% → 34.6% | `+5.4%` | 77.9 | `-16.0` | 5.46 | 1.1% | ⚓🛑 Kotwica Stołu (Bezpiecznik) |
| `gc-08` | **Zatrute Złoto** | GC | 1 | 0 | 29.2% → 26.8% | `-2.5%` | 92.3 | `-1.6` | 5.63 | 1.4% | ⚖️⚪ Zrównoważone Narzędzie |
| `gc-09` | **Lista Dłużników** | GC | 2 | 0 | 29.2% → 19.2% | `-10.1%` | 47.5 | `-46.4` | 5.64 | 1.3% | ⚓👑 Filar Frakcji i Stołu |
| `gc-10` | **Upadek Domu** | GC | 4 | 2 | 29.2% → 33.5% | `+4.3%` | 78.0 | `-15.9` | 5.56 | 1.3% | ⚓🛑 Kotwica Stołu (Bezpiecznik) |
| `kb-01` | **Rozkaz Dworu** | KB | 1 | 0 | 28.6% → 33.0% | `+4.4%` | 86.3 | `-7.6` | 5.52 | 0.9% | ⚓🛑 Kotwica Stołu (Bezpiecznik) |
| `kb-02` | **Pobór Podatków** | KB | 1 | 0 | 28.6% → 17.6% | `-11.0%` | 33.2 | `-60.7` | 5.70 | 1.6% | ⚓👑 Filar Frakcji i Stołu |
| `kb-03` | **Plotka Dworska** | KB | 1 | 0 | 28.6% → 33.4% | `+4.7%` | 79.6 | `-14.3` | 5.55 | 0.9% | ⚓🛑 Kotwica Stołu (Bezpiecznik) |
| `kb-04` | **Faworyt Dworu** | KB | 2 | 1 | 28.6% → 33.4% | `+4.8%` | 86.1 | `-7.8` | 5.53 | 0.9% | ⚓🛑 Kotwica Stołu (Bezpiecznik) |
| `kb-05` | **List Żelazny** | KB | 2 | 0 | 28.6% → 42.6% | `+14.0%` | 37.4 | `-56.5` | 5.33 | 0.4% | ⚓🛑 Kotwica Stołu (Bezpiecznik) |
| `kb-06` | **Areszt Królewski** | KB | 1 | 0 | 28.6% → 32.9% | `+4.3%` | 86.8 | `-7.1` | 5.50 | 0.9% | ⚓🛑 Kotwica Stołu (Bezpiecznik) |
| `kb-07` | **Szantaż Pieczęcią** | KB | 2 | 0 | 28.6% → 32.8% | `+4.2%` | 85.9 | `-8.0` | 5.50 | 0.8% | ⚓🛑 Kotwica Stołu (Bezpiecznik) |
| `kb-08` | **Przekupstwo Sędziego** | KB | 3 | 0 | 28.6% → 30.4% | `+1.8%` | 92.3 | `-1.6` | 5.54 | 1.1% | ⚖️⚪ Zrównoważone Narzędzie |
| `kb-09` | **Dekret Królewski** | KB | 3 | 1 | 28.6% → 8.0% | `-20.6%` | 26.5 | `-67.4` | 5.78 | 1.9% | ⚓👑 Filar Frakcji i Stołu |
| `kb-10` | **Pieczęć Korony** | KB | 2 | 2 | 28.6% → 4.9% | `-23.7%` | 26.5 | `-67.4` | 5.92 | 3.2% | ⚓👑 Filar Frakcji i Stołu |
| `kt-01` | **Rytuał Przejścia** | KT | 1 | 0 | 29.9% → 30.5% | `+0.6%` | 90.6 | `-3.3` | 5.57 | 1.4% | ⚖️⚪ Zrównoważone Narzędzie |
| `kt-02` | **Transmutacja Złota** | KT | 1 | 0 | 29.9% → 29.8% | `-0.1%` | 95.5 | `+1.6` | 5.56 | 1.3% | ⚠️⚪ Toksyczny Zgrzyt |
| `kt-03` | **Zakazana Wiedza** | KT | 0 | 1 | 29.9% → 31.3% | `+1.4%` | 94.6 | `+0.7` | 5.55 | 1.1% | ⚖️⚪ Zrównoważone Narzędzie |
| `kt-04` | **Zwierciadło Herezji** | KT | 0 | 0 | 29.9% → 32.2% | `+2.4%` | 70.1 | `-23.8` | 5.62 | 1.4% | ⚓🛑 Kotwica Stołu (Bezpiecznik) |
| `kt-05` | **Wskazówka Cyklu** | KT | 1 | 0 | 29.9% → 22.4% | `-7.5%` | 67.4 | `-26.5` | 5.67 | 2.4% | ⚓👑 Filar Frakcji i Stołu |
| `kt-06` | **Przesłuchanie Imienia** | KT | 2 | 0 | 29.9% → 31.0% | `+1.1%` | 90.8 | `-3.1` | 5.61 | 1.5% | ⚖️⚪ Zrównoważone Narzędzie |
| `kt-07` | **Archiwum Ukryte** | KT | 1 | 0 | 29.9% → 30.4% | `+0.5%` | 90.3 | `-3.6` | 5.56 | 1.3% | ⚖️⚪ Zrównoważone Narzędzie |
| `kt-08` | **Areszt Wiedzy** | KT | 2 | 0 | 29.9% → 29.0% | `-0.9%` | 90.2 | `-3.7` | 5.55 | 1.4% | ⚖️⚪ Zrównoważone Narzędzie |
| `kt-09` | **Fragment Kodeksu** | KT | 1 | 1 | 29.9% → 29.9% | `-0.0%` | 94.0 | `+0.1` | 5.55 | 1.2% | ⚖️⚪ Zrównoważone Narzędzie |
| `kt-10` | **Pieczęć Salomona** | KT | 1 | 0 | 29.9% → 28.0% | `-1.9%` | 92.2 | `-1.7` | 5.58 | 1.7% | ⚖️⚪ Zrównoważone Narzędzie |
| `so-01` | **Patrol Familiariuszy** | SO | 1 | 0 | 28.8% → 29.9% | `+1.1%` | 90.9 | `-3.0` | 5.54 | 1.2% | ⚖️⚪ Zrównoważone Narzędzie |
| `so-02` | **Skarbiec Trybunału** | SO | 1 | 0 | 28.8% → 27.9% | `-1.0%` | 94.8 | `+0.9` | 5.56 | 1.2% | ⚖️⚪ Zrównoważone Narzędzie |
| `so-03` | **Podejrzenie** | SO | 2 | 0 | 28.8% → 27.8% | `-1.0%` | 94.0 | `+0.1` | 5.57 | 1.3% | ⚖️⚪ Zrównoważone Narzędzie |
| `so-04` | **Publiczne Ostrzeżenie** | SO | 1 | 0 | 28.8% → 29.6% | `+0.8%` | 94.5 | `+0.6` | 5.54 | 1.2% | ⚖️⚪ Zrównoważone Narzędzie |
| `so-05` | **Wezwanie do Trybunału** | SO | 0 | 0 | 28.8% → 29.7% | `+0.8%` | 95.4 | `+1.5` | 5.54 | 1.3% | ⚠️⚪ Toksyczny Zgrzyt |
| `so-06` | **Areszt Trybunalski** | SO | 2 | 0 | 28.8% → 30.1% | `+1.2%` | 93.2 | `-0.7` | 5.54 | 1.0% | ⚖️⚪ Zrównoważone Narzędzie |
| `so-07` | **Przesłuchanie Oficjum** | SO | 2 | 0 | 28.8% → 30.1% | `+1.3%` | 91.6 | `-2.3` | 5.53 | 1.1% | ⚖️⚪ Zrównoważone Narzędzie |
| `so-08` | **Nasłanie Inkwizytora** | SO | 1 | 0 | 28.8% → 29.0% | `+0.2%` | 89.8 | `-4.1` | 5.56 | 1.2% | ⚖️⚪ Zrównoważone Narzędzie |
| `so-09` | **Świadek Koronny** | SO | 2 | 0 | 28.8% → 29.4% | `+0.5%` | 94.6 | `+0.7` | 5.56 | 1.3% | ⚖️⚪ Zrównoważone Narzędzie |
| `so-10` | **Oczyść Miasto** | SO | 4 | 2 | 28.8% → 23.4% | `-5.4%` | 72.2 | `-21.7` | 5.75 | 1.6% | ⚓👑 Filar Frakcji i Stołu |

---

## 3. ⏳ Warstwa II — Kronika Dziejów (Ablacja 8 Kart Wydarzeń Czasu)

Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans:

| ID | Karta Wydarzenia | Global Score | $\Delta$ Global | Średnia Er | Deadlock % | Status Roli w Kronice |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `time-01` | **Upadek Grenady** | 93.9 → 🟡 ** 87.8** (`-6.1`) | `-6.1 pkt` | 5.62 Er | 1.3% | ⚓ Filar stabilności (niezbędna w Kronice) |
| `time-02` | **Edykt z Alhambry** | 93.9 → 🟢 ** 93.1** (`-0.8`) | `-0.8 pkt` | 5.56 Er | 1.3% | ⚖️ Zrównoważone wydarzenie |
| `time-03` | **Flota Kolumba** | 93.9 → 🟡 ** 86.5** (`-7.4`) | `-7.4 pkt` | 5.59 Er | 1.4% | ⚓ Filar stabilności (niezbędna w Kronice) |
| `time-04` | **Archiwa Alhambry** | 93.9 → 🟡 ** 75.4** (`-18.5`) | `-18.5 pkt` | 5.60 Er | 1.7% | ⚓ Filar stabilności (niezbędna w Kronice) |
| `time-05` | **Auto-da-fé Toledo** | 93.9 → 🟢 ** 91.1** (`-2.8`) | `-2.8 pkt` | 5.57 Er | 1.4% | ⚖️ Zrównoważone wydarzenie |
| `time-06` | **Spisek na Dworze** | 93.9 → 🟢 ** 94.6** (`⬆️ +0.7`) | `+0.7 pkt` | 5.57 Er | 1.6% | ⚖️ Zrównoważone wydarzenie |
| `time-07` | **Niepokój na Rynku** | 93.9 → 🟢 ** 96.0** (`⬆️ +2.1`) | `+2.1 pkt` | 5.52 Er | 1.2% | ⚠️ Destabilizuje (usunięcie poprawia stół) |
| `time-08` | **Krypta pod Toledo** | 93.9 → 🟢 ** 92.1** (`-1.8`) | `-1.8 pkt` | 5.53 Er | 1.3% | ⚖️ Zrównoważone wydarzenie |

---

## 4. ⚙️ Warstwa III — Globalne Mechaniki i Parametry Silnika

Badanie odporności gry na wyłączenie lub skrajne przestawienie bazowych parametrów silnika:

| Badany Podsystem / Parametr | Global Score | $\Delta$ Global | Średnia Er | Deadlocks % | Pas Biedy % | Diagnoza i Wpływ na Silnik |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Talia Czasu (Kronika Dziejów): Całkowite WYŁĄCZENIE** | 93.9 → 🟠 ** 72.6** (`-21.3`) | `-21.3 pkt` | 5.94 Er | 2.9% | 27.4% | 🔴 Katastrofa ekosystemu — filar bezwzględnie krytyczny dla gry |
| **Autodafé: Całkowite WYŁĄCZENIE (brak kary śmierci)** | 93.9 → 🔴 ** 27.6** (`-66.3`) | `-66.3 pkt` | 5.75 Er | 2.4% | 26.8% | 🔴 Katastrofa ekosystemu — filar bezwzględnie krytyczny dla gry |
| **Cooldown Autodafé: WYŁĄCZENIE (Autodafé co turę)** | 93.9 → 🟢 ** 93.7** (`-0.2`) | `-0.2 pkt` | 5.55 Er | 1.2% | 26.2% | ⚪ Wpływ neutralny / mechanika stabilna |
| **Ruch Inkwizytora: WYŁĄCZENIE (Inkwizytor stoi w miejscu)** | 93.9 → 🟢 ** 91.4** (`-2.5`) | `-2.5 pkt` | 5.36 Er | 1.0% | 25.5% | ⚪ Wpływ neutralny / mechanika stabilna |
| **Złoto Startowe: WYŁĄCZENIE (Start z 0 zł)** | 93.9 → 🔴 ** 23.6** (`-70.3`) | `-70.3 pkt` | 6.14 Er | 3.5% | 30.4% | 🔴 Katastrofa ekosystemu — filar bezwzględnie krytyczny dla gry |
| **Limit Ręki: Redukcja do 4 kart (Presja dociągu)** | 93.9 → 🟡 ** 77.0** (`-16.9`) | `-16.9 pkt` | 5.82 Er | 1.8% | 32.8% | 🔴 Katastrofa ekosystemu — filar bezwzględnie krytyczny dla gry |

---

## 5. ⚔️ Warstwa IV — Asymetryczne Ścieżki Zwycięstwa (Victory Paths)

Badanie krytyczności i elastyczności unikalnych bramek zwycięstwa (*Victory Gating*) dla każdej frakcji:

| Badana Ścieżka / Bramka Wygranej | Global Score | $\Delta$ Global | Średnia Er | Deadlocks % | Pas Biedy % | Diagnoza Ścieżki Zwycięstwa |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: Wyłączenie Skazań (Wygrana TYLKO przez Stosy)** | 93.9 → 🟡 ** 81.6** (`-12.3`) | `-12.3 pkt` | 5.60 Er | 1.5% | 26.4% | 🟠 Istotna ścieżka — jej brak zauważalnie ubożeje przestrzeń decyzyjną |
| **Święte Oficjum: Wyłączenie Stosów (Wygrana TYLKO przez Skazania)** | 93.9 → 🔴 ** 28.0** (`-65.9`) | `-65.9 pkt` | 5.75 Er | 2.5% | 26.8% | 🔴 Krytyczna ścieżka — frakcja nie posiada alternatywnego motoru |
| **Cienie Al-Andalus: Wyłączenie Szlaku Morskiego (Tylko Ląd)** | 93.9 → 🟢 ** 93.2** (`-0.7`) | `-0.7 pkt` | 5.58 Er | 1.4% | 26.3% | ⚪ Ścieżka alternatywna / opcjonalna |
| **Cienie Al-Andalus: Szlak Morski Otwarty od Ery 1** | 93.9 → 🟡 ** 81.6** (`-12.3`) | `-12.3 pkt` | 5.52 Er | 1.3% | 26.1% | 🟠 Istotna ścieżka — jej brak zauważalnie ubożeje przestrzeń decyzyjną |
| **Korona & Borgiowie: Wyłączenie Wymogu Haków (Tylko Dekrety)** | 🟢 ** 93.9** | `0.0 pkt` | 5.56 Er | 1.4% | 26.2% | ⚪ Ścieżka alternatywna / opcjonalna |
| **Kabała z Toledo: Wyłączenie Pasma Herezji (Bezpieczna Iluminacja)** | 93.9 → 🟡 ** 89.0** (`-4.9`) | `-4.9 pkt` | 5.53 Er | 1.0% | 26.1% | ⚪ Ścieżka alternatywna / opcjonalna |
| **Gildia Cieni: Wyłączenie Modyfikatora 'Bez Oficjum' (Stały próg upadków)** | 93.9 → 🟡 ** 78.6** (`-15.3`) | `-15.3 pkt` | 5.42 Er | 1.1% | 25.8% | 🔴 Krytyczna ścieżka — frakcja nie posiada alternatywnego motoru |

---

## 6. 👥 Warstwa V — Skalowalność i Odporność Topologii Stołu (3P / 4P / 5P)

Zestawienie stabilności ekosystemu gry w zależności od formatu liczby graczy i obecności poszczególnych frakcji:

### 6.1. Balans w Podziale na Formaty Liczby Graczy

| Format Gry | Liczba Badanych Setupów | Średni Global Score | Średnia Długość (Er) | Stan Balansu Formatu |
| :--- | :---: | :---: | :---: | :--- |
| **Format 3-osobowy (3P)** | 10 setupów | **`92.7 pkt`** | 5.56 Er | 🟢 Bardzo wysoki |
| **Format 4-osobowy (4P)** | 5 setupów | **`90.3 pkt`** | 5.56 Er | 🟢 Bardzo wysoki |
| **Format 5-osobowy (5P - Pełny Stół)** | 1 setup (`5p-full`) | **`98.7 pkt`** | 5.56 Er | 🟢 Bardzo wysoki |

### 6.2. Odporność Stołu na Nieobecność Konkretnej Frakcji (Formaty 4P)

| Nieobecna Frakcja | Setup Testowy | Global Score | Diagnoza Wpływu Braku Frakcji na Stół |
| :--- | :--- | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`88.5 pkt`** | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`99.3 pkt`** | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`80.9 pkt`** | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`99.0 pkt`** | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`84.0 pkt`** | Brak presji stosów i bezpośredniego Inkwizytora |

---

## 7. 📐 Metodologia Badania i Matryca Klasyfikacji 3x3

Raport opiera się na **dwuwymiarowej przestrzeni metryk ablacyjnych (Leave-One-Out)**:

1. **OŚ LOKALNA — Wpływ na Frakcję ($\Delta \text{Faction Share} = WS_{\text{baza}} - WS_{\text{bez\_karty}}$):**
   - Wartość dodatnia ($> 0$): Usunięcie karty osłabia frakcję $\rightarrow$ Karta jest **motorem zwycięstwa (Filar)**.
   - Wartość ujemna ($< 0$): Usunięcie karty podnosi winrate frakcji $\rightarrow$ Karta jest **hamulcem tempa / kartą defensywną**.
2. **OŚ GLOBALNA — Wpływ na Ekosystem ($\Delta \text{Global Score} = GS_{\text{bez\_karty}} - GS_{\text{baza}}$):**
   - Wartość dodatnia ($> 0$): Usunięcie karty poprawia balans stołu $\rightarrow$ Karta była **toksyczna / destabilizująca**.
   - Wartość ujemna ($< 0$): Usunięcie karty załamuje balans stołu $\rightarrow$ Karta jest **stabilizatorem / kotwicą stołu**.

- **Rygor Próby:** Każdy element badany jest na pełnym pakiecie 16 setupów (min. 1000 partii / setup = min. 16 000 partii na wariant).