# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v0.75

**Wersja Gry:** `v0.75` | **Data Badania:** 2026-08-17 00:50 | **Próba:** 30 gier/setup (150 gier na wariant) | **Ziarno:** 42
**Wynik Bazowy Kanonu 4P:** 🔴 ** 44.3** pkt | **Średnia Długość Partii:** `5.66 Er` | **Deadlocki:** `2.0%` | **Pas Biedy:** `7.0%`

---

## 1. 🗺️ Podsumowanie Ekosystemu Kart Kanonu 4P (Matryca Wpływu Kart 3x3)

Rozkład wszystkich 50 kart frakcyjnych w matrycy **Wpływ na Frakcję ($\Delta \text{Share}$)** vs **Wpływ na Kanon 4P ($\Delta \text{4P Score}$)**:

| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |
| :--- | :---: | :---: | :--- | :--- |
| 👑 / ⚓ **Filar / Kotwica Kanonu** | **49** | 98% | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |
| ⚖️ **Zbalansowane Narzędzie** | **1** | 2% | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Optymalne** |
| 💤 **Karta Pasywna (Dead Weight)** | **0** | 0% | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia** |
| ⚠️ **Karta Destabilizująca (Disruptor)** | **0** | 0% | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |

---

## 2. 🃏 Warstwa I — Szczegółowa Analiza 50 Kart Frakcji w Kanonie 4P

### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)
Karty, których brak powoduje spadek wyniku Kanonu 4P o $\ge 4.0$ pkt lub załamanie winrate frakcji o $\ge 4.0\%$:

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `caa-08` **Kaptur Nocy** | Cienie Al-Andalus | 2zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 28.3% → **50.0%** | **`+21.7%`** | 44.3 → **16.7 pkt** (`-27.6`) |
| `kb-10` **Pieczęć Korony** | Korona & Borgiowie | 2zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 17.5% → **0.8%** | **`-16.7%`** | 44.3 → **18.9 pkt** (`-25.4`) |
| `kb-09` **Dekret Królewski** | Korona & Borgiowie | 3zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 17.5% → **1.7%** | **`-15.8%`** | 44.3 → **19.7 pkt** (`-24.6`) |
| `caa-02` **Złoto z Kryjówki** | Cienie Al-Andalus | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 28.3% → **43.3%** | **`+15.0%`** | 44.3 → **20.3 pkt** (`-24.0`) |
| `kb-02` **Pobór Podatków** | Korona & Borgiowie | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 17.5% → **1.7%** | **`-15.8%`** | 44.3 → **20.7 pkt** (`-23.6`) |
| `caa-09` **Kurier Relikwii** | Cienie Al-Andalus | 2zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 28.3% → **44.2%** | **`+15.9%`** | 44.3 → **21.0 pkt** (`-23.3`) |
| `kt-04` **Zwierciadło Herezji** | Kabała z Toledo | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 37.5% → **47.5%** | **`+10.0%`** | 44.3 → **21.0 pkt** (`-23.3`) |
| `caa-07` **Szantaż Bractwa** | Cienie Al-Andalus | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 28.3% → **45.0%** | **`+16.7%`** | 44.3 → **21.6 pkt** (`-22.7`) |
| `caa-04` **Fałszywy Trop** | Cienie Al-Andalus | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 28.3% → **44.2%** | **`+15.9%`** | 44.3 → **22.6 pkt** (`-21.7`) |
| `kb-01` **Rozkaz Dworu** | Korona & Borgiowie | 1zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 17.5% → **8.3%** | **`-9.2%`** | 44.3 → **22.9 pkt** (`-21.4`) |
| `kt-03` **Zakazana Wiedza** | Kabała z Toledo | 0zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 37.5% → **48.3%** | **`+10.8%`** | 44.3 → **23.8 pkt** (`-20.5`) |
| `so-09` **Świadek Koronny** | Święte Oficjum | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 17.5% → **7.5%** | **`-10.0%`** | 44.3 → **25.6 pkt** (`-18.7`) |
| `so-04` **Publiczne Ostrzeżenie** | Święte Oficjum | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 17.5% → **10.0%** | **`-7.5%`** | 44.3 → **26.1 pkt** (`-18.2`) |
| `caa-10` **Echo Alhambry** | Cienie Al-Andalus | 1zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 28.3% → **30.8%** | **`+2.5%`** | 44.3 → **26.3 pkt** (`-18.0`) |
| `caa-06` **Ucieczka z Lochów** | Cienie Al-Andalus | 2zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 28.3% → **34.2%** | **`+5.9%`** | 44.3 → **26.6 pkt** (`-17.7`) |
| `kb-06` **Areszt Królewski** | Korona & Borgiowie | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 17.5% → **10.0%** | **`-7.5%`** | 44.3 → **26.8 pkt** (`-17.5`) |
| `so-08` **Nasłanie Inkwizytora** | Święte Oficjum | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 17.5% → **10.0%** | **`-7.5%`** | 44.3 → **26.8 pkt** (`-17.5`) |
| `kt-07` **Archiwum Ukryte** | Kabała z Toledo | 1zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 37.5% → **44.2%** | **`+6.7%`** | 44.3 → **27.2 pkt** (`-17.1`) |
| `kb-03` **Plotka Dworska** | Korona & Borgiowie | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 17.5% → **10.8%** | **`-6.7%`** | 44.3 → **27.7 pkt** (`-16.6`) |
| `kt-01` **Rytuał Przejścia** | Kabała z Toledo | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 37.5% → **42.5%** | **`+5.0%`** | 44.3 → **27.9 pkt** (`-16.4`) |
| `so-01` **Patrol Familiariuszy** | Święte Oficjum | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 17.5% → **5.8%** | **`-11.7%`** | 44.3 → **28.6 pkt** (`-15.7`) |
| `gc-05` **Fałszywy Świadek** | Gildia Cieni | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.2% → **23.3%** | **`-0.9%`** | 44.3 → **29.2 pkt** (`-15.1`) |
| `kt-02` **Transmutacja Złota** | Kabała z Toledo | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 37.5% → **44.2%** | **`+6.7%`** | 44.3 → **29.2 pkt** (`-15.1`) |
| `so-03` **Podejrzenie** | Święte Oficjum | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 17.5% → **10.0%** | **`-7.5%`** | 44.3 → **29.2 pkt** (`-15.1`) |
| `caa-03` **Cień na Rynku** | Cienie Al-Andalus | 0zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 28.3% → **34.2%** | **`+5.9%`** | 44.3 → **30.3 pkt** (`-14.0`) |
| `gc-08` **Zatrute Złoto** | Gildia Cieni | 2zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.2% → **39.2%** | **`+15.0%`** | 44.3 → **30.4 pkt** (`-13.9`) |
| `gc-04` **Informator** | Gildia Cieni | 0zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.2% → **30.0%** | **`+5.8%`** | 44.3 → **31.5 pkt** (`-12.8`) |
| `gc-06` **Szantaż** | Gildia Cieni | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.2% → **19.2%** | **`-5.0%`** | 44.3 → **31.5 pkt** (`-12.8`) |
| `kt-08` **Areszt Wiedzy** | Kabała z Toledo | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 37.5% → **39.2%** | **`+1.7%`** | 44.3 → **31.5 pkt** (`-12.8`) |
| `kt-09` **Fragment Kodeksu** | Kabała z Toledo | 2zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 37.5% → **37.5%** | **`+0.0%`** | 44.3 → **32.3 pkt** (`-12.0`) |
| `so-05` **Wezwanie do Trybunału** | Święte Oficjum | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 17.5% → **12.5%** | **`-5.0%`** | 44.3 → **33.3 pkt** (`-11.0`) |
| `so-02` **Skarbiec Trybunału** | Święte Oficjum | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 17.5% → **8.3%** | **`-9.2%`** | 44.3 → **33.9 pkt** (`-10.4`) |
| `gc-07` **Skrytobójstwo** | Gildia Cieni | 2zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.2% → **37.5%** | **`+13.3%`** | 44.3 → **34.1 pkt** (`-10.2`) |
| `so-07` **Przesłuchanie Oficjum** | Święte Oficjum | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 17.5% → **12.5%** | **`-5.0%`** | 44.3 → **34.8 pkt** (`-9.5`) |
| `kt-10` **Pieczęć Salomona** | Kabała z Toledo | 2zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 37.5% → **40.0%** | **`+2.5%`** | 44.3 → **34.9 pkt** (`-9.4`) |
| `gc-09` **Lista Dłużników** | Gildia Cieni | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.2% → **19.2%** | **`-5.0%`** | 44.3 → **35.5 pkt** (`-8.8`) |
| `gc-01` **Przekupiony Strażnik** | Gildia Cieni | 1zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.2% → **34.2%** | **`+10.0%`** | 44.3 → **35.9 pkt** (`-8.4`) |
| `caa-05` **Ukryty Kurier** | Cienie Al-Andalus | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 28.3% → **34.2%** | **`+5.9%`** | 44.3 → **36.9 pkt** (`-7.4`) |
| `caa-01` **Przejście Podziemiami** | Cienie Al-Andalus | 0zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 28.3% → **38.3%** | **`+10.0%`** | 44.3 → **37.6 pkt** (`-6.7`) |
| `gc-02` **Czarny Rynek** | Gildia Cieni | 1zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.2% → **31.7%** | **`+7.5%`** | 44.3 → **38.0 pkt** (`-6.3`) |
| `kb-07` **Szantaż Pieczęcią** | Korona & Borgiowie | 2zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 17.5% → **17.5%** | **`+0.0%`** | 44.3 → **38.0 pkt** (`-6.3`) |
| `kb-08` **Przekupstwo Sędziego** | Korona & Borgiowie | 2zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 17.5% → **17.5%** | **`+0.0%`** | 44.3 → **38.0 pkt** (`-6.3`) |
| `so-10` **Oczyść Miasto** | Święte Oficjum | 5zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 17.5% → **14.2%** | **`-3.3%`** | 44.3 → **38.2 pkt** (`-6.1`) |
| `so-06` **Areszt Trybunalski** | Święte Oficjum | 2zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 17.5% → **15.8%** | **`-1.7%`** | 44.3 → **38.5 pkt** (`-5.8`) |
| `gc-03` **Podrzucenie Księgi** | Gildia Cieni | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.2% → **31.7%** | **`+7.5%`** | 44.3 → **39.4 pkt** (`-4.9`) |
| `kt-05` **Wskazówka Cyklu** | Kabała z Toledo | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 37.5% → **18.3%** | **`-19.2%`** | 44.3 → **40.6 pkt** (`-3.7`) |
| `gc-10` **Upadek Domu** | Gildia Cieni | 4zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.2% → **29.2%** | **`+5.0%`** | 44.3 → **41.2 pkt** (`-3.1`) |
| `kt-06` **Przesłuchanie Imienia** | Kabała z Toledo | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 37.5% → **35.0%** | **`-2.5%`** | 44.3 → **41.5 pkt** (`-2.8`) |
| `kb-04` **Faworyt Dworu** | Korona & Borgiowie | 2zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 17.5% → **22.5%** | **`+5.0%`** | 44.3 → **42.2 pkt** (`-2.1`) |

### 2.2. ⚠️ Karty Destabilizujące Kanon 4P (Disruptors)
Karty, których wyłączenie podnosi 4P Score ($\Delta \text{4P} \ge +1.5$ pkt):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *Brak kart destabilizujących* | - | - | - | - | - | - |

### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich 50 Kart Frakcji w Kanonie 4P

| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Faction Win Share 4P | $\Delta$ Frakcji | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `caa-01` | **Przejście Podziemiami** | Cienie Al-Andalus | 0 | 0 | 28.3% → 38.3% | `+10.0%` | 37.6 | `-6.7` | 5.43 | 2.7% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `caa-03` | **Cień na Rynku** | Cienie Al-Andalus | 0 | 1 | 28.3% → 34.2% | `+5.9%` | 30.3 | `-14.0` | 6.08 | 3.3% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `caa-02` | **Złoto z Kryjówki** | Cienie Al-Andalus | 1 | 0 | 28.3% → 43.3% | `+15.0%` | 20.3 | `-24.0` | 5.26 | 0.7% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `caa-04` | **Fałszywy Trop** | Cienie Al-Andalus | 1 | 0 | 28.3% → 44.2% | `+15.9%` | 22.6 | `-21.7` | 5.46 | 2.7% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `caa-05` | **Ukryty Kurier** | Cienie Al-Andalus | 1 | 0 | 28.3% → 34.2% | `+5.9%` | 36.9 | `-7.4` | 5.51 | 1.3% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `caa-07` | **Szantaż Bractwa** | Cienie Al-Andalus | 1 | 0 | 28.3% → 45.0% | `+16.7%` | 21.6 | `-22.7` | 5.47 | 0.7% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `caa-06` | **Ucieczka z Lochów** | Cienie Al-Andalus | 2 | 1 | 28.3% → 34.2% | `+5.9%` | 26.6 | `-17.7` | 5.55 | 2.0% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `caa-08` | **Kaptur Nocy** | Cienie Al-Andalus | 2 | 1 | 28.3% → 50.0% | `+21.7%` | 16.7 | `-27.6` | 5.32 | 0.7% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `caa-10` | **Echo Alhambry** | Cienie Al-Andalus | 1 | 1 | 28.3% → 30.8% | `+2.5%` | 26.3 | `-18.0` | 5.87 | 2.0% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `caa-09` | **Kurier Relikwii** | Cienie Al-Andalus | 2 | 0 | 28.3% → 44.2% | `+15.9%` | 21.0 | `-23.3` | 5.53 | 0.7% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `gc-04` | **Informator** | Gildia Cieni | 0 | 1 | 24.2% → 30.0% | `+5.8%` | 31.5 | `-12.8` | 5.65 | 2.0% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `gc-05` | **Fałszywy Świadek** | Gildia Cieni | 0 | 0 | 24.2% → 23.3% | `-0.9%` | 29.2 | `-15.1` | 5.53 | 0.7% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-01` | **Przekupiony Strażnik** | Gildia Cieni | 1 | 1 | 24.2% → 34.2% | `+10.0%` | 35.9 | `-8.4` | 5.39 | 1.3% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `gc-02` | **Czarny Rynek** | Gildia Cieni | 1 | 1 | 24.2% → 31.7% | `+7.5%` | 38.0 | `-6.3` | 5.61 | 1.3% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `gc-03` | **Podrzucenie Księgi** | Gildia Cieni | 1 | 0 | 24.2% → 31.7% | `+7.5%` | 39.4 | `-4.9` | 5.65 | 0.7% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `gc-06` | **Szantaż** | Gildia Cieni | 2 | 0 | 24.2% → 19.2% | `-5.0%` | 31.5 | `-12.8` | 5.77 | 2.7% | 👑 FILAR KANONU (Core Keystone) |
| `gc-07` | **Skrytobójstwo** | Gildia Cieni | 2 | 0 | 24.2% → 37.5% | `+13.3%` | 34.1 | `-10.2` | 5.53 | 0.7% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `gc-08` | **Zatrute Złoto** | Gildia Cieni | 2 | 0 | 24.2% → 39.2% | `+15.0%` | 30.4 | `-13.9` | 5.54 | 2.0% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `gc-09` | **Lista Dłużników** | Gildia Cieni | 2 | 0 | 24.2% → 19.2% | `-5.0%` | 35.5 | `-8.8` | 5.81 | 2.0% | 👑 FILAR KANONU (Core Keystone) |
| `gc-10` | **Upadek Domu** | Gildia Cieni | 4 | 1 | 24.2% → 29.2% | `+5.0%` | 41.2 | `-3.1` | 5.72 | 2.7% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kb-01` | **Rozkaz Dworu** | Korona & Borgiowie | 1 | 1 | 17.5% → 8.3% | `-9.2%` | 22.9 | `-21.4` | 5.43 | 0.7% | 👑 FILAR KANONU (Core Keystone) |
| `kb-02` | **Pobór Podatków** | Korona & Borgiowie | 1 | 0 | 17.5% → 1.7% | `-15.8%` | 20.7 | `-23.6` | 5.53 | 1.3% | 👑 FILAR KANONU (Core Keystone) |
| `kb-03` | **Plotka Dworska** | Korona & Borgiowie | 1 | 0 | 17.5% → 10.8% | `-6.7%` | 27.7 | `-16.6` | 5.57 | 0.7% | 👑 FILAR KANONU (Core Keystone) |
| `kb-04` | **Faworyt Dworu** | Korona & Borgiowie | 2 | 1 | 17.5% → 22.5% | `+5.0%` | 42.2 | `-2.1` | 5.32 | 0.7% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kb-05` | **List Żelazny** | Korona & Borgiowie | 2 | 0 | 17.5% → 16.7% | `-0.8%` | 43.9 | `-0.4` | 5.33 | 0.7% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-06` | **Areszt Królewski** | Korona & Borgiowie | 1 | 0 | 17.5% → 10.0% | `-7.5%` | 26.8 | `-17.5` | 5.66 | 1.3% | 👑 FILAR KANONU (Core Keystone) |
| `kb-07` | **Szantaż Pieczęcią** | Korona & Borgiowie | 2 | 0 | 17.5% → 17.5% | `+0.0%` | 38.0 | `-6.3` | 5.55 | 0.7% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kb-08` | **Przekupstwo Sędziego** | Korona & Borgiowie | 2 | 0 | 17.5% → 17.5% | `+0.0%` | 38.0 | `-6.3` | 5.55 | 0.7% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kb-10` | **Pieczęć Korony** | Korona & Borgiowie | 2 | 2 | 17.5% → 0.8% | `-16.7%` | 18.9 | `-25.4` | 5.94 | 4.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-09` | **Dekret Królewski** | Korona & Borgiowie | 3 | 1 | 17.5% → 1.7% | `-15.8%` | 19.7 | `-24.6` | 5.81 | 3.3% | 👑 FILAR KANONU (Core Keystone) |
| `kt-03` | **Zakazana Wiedza** | Kabała z Toledo | 0 | 1 | 37.5% → 48.3% | `+10.8%` | 23.8 | `-20.5` | 5.50 | 1.3% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-01` | **Rytuał Przejścia** | Kabała z Toledo | 1 | 0 | 37.5% → 42.5% | `+5.0%` | 27.9 | `-16.4` | 5.37 | 0.0% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-02` | **Transmutacja Złota** | Kabała z Toledo | 1 | 0 | 37.5% → 44.2% | `+6.7%` | 29.2 | `-15.1` | 5.45 | 0.0% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-04` | **Zwierciadło Herezji** | Kabała z Toledo | 1 | 0 | 37.5% → 47.5% | `+10.0%` | 21.0 | `-23.3` | 5.41 | 0.7% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-05` | **Wskazówka Cyklu** | Kabała z Toledo | 1 | 0 | 37.5% → 18.3% | `-19.2%` | 40.6 | `-3.7` | 5.79 | 2.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-07` | **Archiwum Ukryte** | Kabała z Toledo | 1 | 1 | 37.5% → 44.2% | `+6.7%` | 27.2 | `-17.1` | 5.63 | 0.7% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-08` | **Areszt Wiedzy** | Kabała z Toledo | 1 | 0 | 37.5% → 39.2% | `+1.7%` | 31.5 | `-12.8` | 5.45 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kt-06` | **Przesłuchanie Imienia** | Kabała z Toledo | 2 | 0 | 37.5% → 35.0% | `-2.5%` | 41.5 | `-2.8` | 5.67 | 0.7% | 👑 FILAR KANONU (Core Keystone) |
| `kt-09` | **Fragment Kodeksu** | Kabała z Toledo | 2 | 1 | 37.5% → 37.5% | `+0.0%` | 32.3 | `-12.0` | 5.65 | 0.7% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kt-10` | **Pieczęć Salomona** | Kabała z Toledo | 2 | 1 | 37.5% → 40.0% | `+2.5%` | 34.9 | `-9.4` | 5.75 | 3.3% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `so-05` | **Wezwanie do Trybunału** | Święte Oficjum | 0 | 0 | 17.5% → 12.5% | `-5.0%` | 33.3 | `-11.0` | 5.39 | 0.7% | 👑 FILAR KANONU (Core Keystone) |
| `so-01` | **Patrol Familiariuszy** | Święte Oficjum | 1 | 0 | 17.5% → 5.8% | `-11.7%` | 28.6 | `-15.7` | 5.19 | 0.7% | 👑 FILAR KANONU (Core Keystone) |
| `so-02` | **Skarbiec Trybunału** | Święte Oficjum | 1 | 0 | 17.5% → 8.3% | `-9.2%` | 33.9 | `-10.4` | 5.36 | 0.7% | 👑 FILAR KANONU (Core Keystone) |
| `so-04` | **Publiczne Ostrzeżenie** | Święte Oficjum | 1 | 0 | 17.5% → 10.0% | `-7.5%` | 26.1 | `-18.2` | 5.19 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `so-03` | **Podejrzenie** | Święte Oficjum | 2 | 0 | 17.5% → 10.0% | `-7.5%` | 29.2 | `-15.1` | 5.20 | 1.3% | 👑 FILAR KANONU (Core Keystone) |
| `so-08` | **Nasłanie Inkwizytora** | Święte Oficjum | 1 | 0 | 17.5% → 10.0% | `-7.5%` | 26.8 | `-17.5` | 5.59 | 2.7% | 👑 FILAR KANONU (Core Keystone) |
| `so-06` | **Areszt Trybunalski** | Święte Oficjum | 2 | 0 | 17.5% → 15.8% | `-1.7%` | 38.5 | `-5.8` | 5.39 | 1.3% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-07` | **Przesłuchanie Oficjum** | Święte Oficjum | 2 | 0 | 17.5% → 12.5% | `-5.0%` | 34.8 | `-9.5` | 5.50 | 1.3% | 👑 FILAR KANONU (Core Keystone) |
| `so-09` | **Świadek Koronny** | Święte Oficjum | 2 | 0 | 17.5% → 7.5% | `-10.0%` | 25.6 | `-18.7` | 5.35 | 0.7% | 👑 FILAR KANONU (Core Keystone) |
| `so-10` | **Oczyść Miasto** | Święte Oficjum | 5 | 2 | 17.5% → 14.2% | `-3.3%` | 38.2 | `-6.1` | 5.17 | 0.7% | 👑 FILAR KANONU (Core Keystone) |

---

## 3. ⏳ Warstwa II — Kronika Dziejów w 4P (Ablacja 8 Kart Wydarzeń Czasu)

Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans w 4P:

| ID | Karta Wydarzenia | 4P Score | $\Delta$ 4P | Średnia Er | Deadlock % | Status Roli w Kronice |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `tc-01` | **Kres Średniowiecza** | 🔴 ** 44.3** | `0.0 pkt` | 5.66 Er | 2.0% | ⚖️ Neutralna Kronika |
| `tc-02` | **Płonący Stos** | 🔴 ** 44.3** | `0.0 pkt` | 5.66 Er | 2.0% | ⚖️ Neutralna Kronika |
| `tc-03` | **Królewski Podatek** | 🔴 ** 44.3** | `0.0 pkt` | 5.66 Er | 2.0% | ⚖️ Neutralna Kronika |
| `tc-04` | **Spisek w Cieniu** | 🔴 ** 44.3** | `0.0 pkt` | 5.66 Er | 2.0% | ⚖️ Neutralna Kronika |
| `tc-05` | **Złoty Wiek** | 🔴 ** 44.3** | `0.0 pkt` | 5.66 Er | 2.0% | ⚖️ Neutralna Kronika |
| `tc-06` | **Czystka w Mieście** | 🔴 ** 44.3** | `0.0 pkt` | 5.66 Er | 2.0% | ⚖️ Neutralna Kronika |
| `tc-07` | **Druga Szansa** | 🔴 ** 44.3** | `0.0 pkt` | 5.66 Er | 2.0% | ⚖️ Neutralna Kronika |
| `tc-08` | **Zaćmienie Słońca** | 🔴 ** 44.3** | `0.0 pkt` | 5.66 Er | 2.0% | ⚖️ Neutralna Kronika |

---

## 4. ⚙️ Warstwa III — Matryca 9 Obszarów Wpływu Mechanik Gry (L1, L2, L4)

Zestawienie odporności Kanonu 4P na modyfikacje i ablację poszczególnych podsystemów według 9 obszarów istotności i efektu:

| Kategoria Mechaniki | Liczba Testów | Rola w Ekosystemie Kanonu 4P | Rekomendacja Balansowa |
| :--- | :---: | :--- | :--- |
| 👑 / 🛡️ **Filary i Bezpieczniki Stabilizujące** | **25** | Mechaniki krytyczne — ich brak lub rozregulowanie niszczy balans | **Nienaruszalny Kanon** |
| ⚖️ **Zbalansowane Regulatory / Pasywne** | **14** | Mechaniki harmonijnie wpisane w dynamikę rozgrywki | **Optymalne w Kanonie** |
| ⚠️ / 💡 **Obciążenia i Kandydaci do Uproszczenia** | **9** | Mechaniki, których modyfikacja lub redukcja podnosi wynik 4P | **Kandydaci do optymalizacji** |

### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)

| Badany Podsystem / Modyfikator L1 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Limit Er: 12 → 8 Er (Presja czasu)** | 44.3 → 🔴 ** 33.3** (`-11.0`) | `-11.0 pkt` | 5.45 Er | 13.3% | 7.1% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Limit Er: 12 → 16 Er (Wydłużony silnik)** | 44.3 → 🔴 ** 45.9** (`⬆️ +1.6`) | `+1.6 pkt` | 5.69 Er | 0.0% | 6.9% | 💡 KANDYDAT DO UPROSZCZENIA (Simplification) |
| **Próg Oskarżenia na Dworze: -1 (Agresywny Dwór)** | 44.3 → 🔴 ** 44.9** (`⬆️ +0.6`) | `+0.6 pkt` | 5.81 Er | 1.3% | 6.4% | ⚖️ ZBALANSOWANY REGULATOR (Balanced Regulator) |
| **Próg Oskarżenia na Dworze: +1 (Pasywny Dwór)** | 44.3 → 🔴 ** 41.4** (`-2.9`) | `-2.9 pkt` | 5.46 Er | 0.7% | 7.3% | ⚖️ ZBALANSOWANY REGULATOR (Balanced Regulator) |
| **Złoto startowe: 4zł → 0zł (Skrajne ubóstwo)** | 44.3 → 🔴 ** 11.4** (`-32.9`) | `-32.9 pkt` | 6.15 Er | 2.0% | 24.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 6zł (Bogaty start)** | 44.3 → 🔴 ** 31.9** (`-12.4`) | `-12.4 pkt` | 4.77 Er | 1.3% | 4.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 2 Agentów (Ograniczony zasięg)** | 44.3 → 🔴 ** 28.3** (`-16.0`) | `-16.0 pkt` | 5.67 Er | 1.3% | 7.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 4 Agentów (Gęsta plansza)** | 44.3 → 🔴 ** 33.3** (`-11.0`) | `-11.0 pkt` | 5.61 Er | 0.7% | 7.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 3 karty (Zmniejszona elastyczność)** | 44.3 → 🔴 ** 44.0** (`-0.3`) | `-0.3 pkt` | 6.05 Er | 2.7% | 10.3% | ⚓ KLUCZOWY STABILIZATOR (Key Anchor) |
| **Limit kart na ręce: 5 → 7 kart (Pełna swoboda)** | 44.3 → 🔴 ** 15.7** (`-28.6`) | `-28.6 pkt` | 5.03 Er | 0.0% | 7.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé Inkwizytora: Cooldown 2 Ery (Częsta czystka)** | 44.3 → 🔴 ** 35.7** (`-8.6`) | `-8.6 pkt` | 5.29 Er | 0.7% | 7.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé Inkwizytora: Cooldown 4 Ery (Rzadka czystka)** | 44.3 → 🔴 ** 32.9** (`-11.4`) | `-11.4 pkt` | 5.84 Er | 4.0% | 6.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Autodafé Inkwizytora: Całkowity brak czystki** | 44.3 → 🔴 ** 20.2** (`-24.1`) | `-24.1 pkt` | 6.17 Er | 6.7% | 5.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)

| Badany Warunek Zwycięstwa L2 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: Wymóg Stosów +2** | 44.3 → 🔴 ** 29.6** (`-14.7`) | `-14.7 pkt` | 5.82 Er | 4.0% | 6.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: Wymóg Stosów -1** | 44.3 → 🔴 ** 46.7** (`⬆️ +2.4`) | `+2.4 pkt` | 5.50 Er | 2.0% | 7.0% | ⚠️ UMIARKOWANE OBCIĄŻENIE (Moderate Drag) |
| **Święte Oficjum: Wymóg Skazań +2 (Zamiast 2-3)** | 🔴 ** 44.3** | `0.0 pkt` | 5.66 Er | 2.0% | 7.0% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Święte Oficjum: Wymóg Skazań -1** | 44.3 → 🔴 ** 48.6** (`⬆️ +4.3`) | `+4.3 pkt` | 5.58 Er | 2.0% | 7.0% | ⚠️ UMIARKOWANE OBCIĄŻENIE (Moderate Drag) |
| **Cienie: Wymóg Relikwii 2 → 4** | 44.3 → 🔴 ** 13.9** (`-30.4`) | `-30.4 pkt` | 6.39 Er | 2.7% | 7.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Cienie: Wymóg Relikwii 2 → 1** | 44.3 → 🔴 **  3.0** (`-41.3`) | `-41.3 pkt` | 4.02 Er | 0.7% | 6.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Cienie: Wymóg Ery 5 → Era 3 (Wczesna ucieczka)** | 44.3 → 🔴 ** 45.6** (`⬆️ +1.3`) | `+1.3 pkt` | 5.63 Er | 2.0% | 7.0% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Cienie: Wymóg Ery 5 → Era 8 (Późna ucieczka)** | 44.3 → 🔴 ** 44.8** (`⬆️ +0.5`) | `+0.5 pkt` | 5.71 Er | 2.0% | 7.0% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Korona: Wymóg Dekretów 2 → 3** | 44.3 → 🔴 ** 21.8** (`-22.5`) | `-22.5 pkt` | 5.93 Er | 2.0% | 7.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: Wymóg Dekretów 2 → 1** | 44.3 → 🔴 ** 11.1** (`-33.2`) | `-33.2 pkt` | 4.31 Er | 0.7% | 6.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: Brak wymogu Haków (0 Haków)** | 44.3 → 🔴 ** 47.2** (`⬆️ +2.9`) | `+2.9 pkt` | 5.63 Er | 2.0% | 7.0% | 💡 KANDYDAT DO UPROSZCZENIA (Simplification) |
| **Korona: Wymóg Haków +2** | 44.3 → 🔴 ** 21.8** (`-22.5`) | `-22.5 pkt` | 5.93 Er | 2.0% | 7.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: Wymóg Ery 5 → Era 3** | 🔴 ** 44.3** | `0.0 pkt` | 5.65 Er | 2.0% | 7.0% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Korona: Wymóg Ery 5 → Era 7** | 44.3 → 🔴 ** 39.5** (`-4.8`) | `-4.8 pkt` | 5.79 Er | 2.0% | 7.0% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Kabała: Wymóg Fragmentów 3 → 4** | 44.3 → 🔴 ** 46.3** (`⬆️ +2.0`) | `+2.0 pkt` | 5.92 Er | 2.0% | 7.0% | ⚠️ KRYTYCZNA WADA (Critical Flaw) |
| **Kabała: Wymóg Fragmentów 3 → 2** | 44.3 → 🔴 ** 29.0** (`-15.3`) | `-15.3 pkt` | 5.41 Er | 0.7% | 7.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: Wymóg Ery 6 → Era 4** | 44.3 → 🔴 ** 35.7** (`-8.6`) | `-8.6 pkt` | 5.45 Er | 2.0% | 6.8% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Kabała: Wymóg Ery 6 → Era 8** | 44.3 → 🔴 ** 51.0** (`⬆️ +6.7`) | `+6.7 pkt` | 6.04 Er | 2.0% | 7.0% | ⚠️ KRYTYCZNA WADA (Critical Flaw) |
| **Kabała: Próg Dolny Pasma 3 → 5 (Zawężenie od dołu)** | 🔴 ** 44.3** | `0.0 pkt` | 5.67 Er | 2.0% | 7.0% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Kabała: Próg Dolny Pasma 3 → 1 (Rozszerzenie w dół)** | 🔴 ** 44.3** | `0.0 pkt` | 5.66 Er | 2.0% | 7.0% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Kabała: Próg Górny Pasma 8 → 6 (Zawężenie od góry)** | 44.3 → 🔴 ** 55.5** (`⬆️ +11.2`) | `+11.2 pkt` | 5.76 Er | 2.0% | 7.0% | ⚠️ UMIARKOWANE OBCIĄŻENIE (Moderate Drag) |
| **Kabała: Próg Górny Pasma 8 → 10 (Rozszerzenie w górę)** | 44.3 → 🔴 ** 38.8** (`-5.5`) | `-5.5 pkt` | 5.57 Er | 0.7% | 7.0% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Kabała: Całe Pasmo Wąskie (4–6)** | 44.3 → 🔴 ** 55.5** (`⬆️ +11.2`) | `+11.2 pkt` | 5.76 Er | 2.0% | 7.0% | ⚠️ UMIARKOWANE OBCIĄŻENIE (Moderate Drag) |
| **Kabała: Całe Pasmo Szerokie (2–9)** | 44.3 → 🔴 ** 44.9** (`⬆️ +0.6`) | `+0.6 pkt` | 5.61 Er | 1.3% | 7.0% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Gildia: Wymóg Upadków (z Oficjum) 2 → 3** | 44.3 → 🔴 ** 40.6** (`-3.7`) | `-3.7 pkt` | 5.77 Er | 2.0% | 7.0% | ⚖️ ZBALANSOWANY REGULATOR (Balanced Regulator) |
| **Gildia: Wymóg Upadków (z Oficjum) 2 → 1** | 44.3 → 🔴 ** 31.8** (`-12.5`) | `-12.5 pkt` | 5.24 Er | 2.0% | 6.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: Wymóg Upadków (bez Oficjum) 3 → 4** | 44.3 → 🔴 ** 38.1** (`-6.2`) | `-6.2 pkt` | 5.74 Er | 2.0% | 7.0% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Gildia: Wymóg Upadków (bez Oficjum) 3 → 2** | 44.3 → 🔴 ** 42.7** (`-1.6`) | `-1.6 pkt` | 5.60 Er | 2.0% | 7.0% | 💤 MECHANIKA PASYWNA (Low Impact) |

### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)

| Badany Wariant / Modyfikator L4 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kronika Dziejów: Całkowite wyłączenie edyktów czasu** | 44.3 → 🔴 ** 18.6** (`-25.7`) | `-25.7 pkt` | 5.56 Er | 1.3% | 8.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kronika Dziejów: Częstotliwość co 2 Ery** | 44.3 → 🔴 ** 19.7** (`-24.6`) | `-24.6 pkt` | 5.54 Er | 0.7% | 7.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Werdykt Sądu: Tajny (brak koordynacji anty-snowball)** | 44.3 → 🔴 ** 46.5** (`⬆️ +2.2`) | `+2.2 pkt` | 5.34 Er | 0.7% | 6.9% | ⚠️ UMIARKOWANE OBCIĄŻENIE (Moderate Drag) |
| **Szlak Morski: Odblokowanie w Erze 4 (Wczesne)** | 44.3 → 🔴 ** 45.6** (`⬆️ +1.3`) | `+1.3 pkt` | 5.63 Er | 2.0% | 7.0% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Szlak Morski: Odblokowanie w Erze 6 (Późne)** | 🔴 ** 44.3** | `0.0 pkt` | 5.66 Er | 2.0% | 7.0% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Inkwizytor Patrol: Ruch 0 pól (Stacjonarny)** | 44.3 → 🔴 ** 22.7** (`-21.6`) | `-21.6 pkt` | 5.45 Er | 1.3% | 7.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Inkwizytor Patrol: Ruch 2 pola (Szybki patrol)** | 44.3 → 🔴 ** 31.2** (`-13.1`) | `-13.1 pkt` | 5.50 Er | 2.0% | 6.9% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |

---

## 5. 👥 Warstwa IV — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych w Kanonie 4P:

| Nieobecna Frakcja | Setup Testowy | 4P Score Setupu | Diagnoza Wpływu Braku Frakcji na Stół 4P |
| :--- | :--- | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`50.5 pkt`** | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`50.5 pkt`** | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`48.3 pkt`** | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`13.7 pkt`** | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`58.4 pkt`** | Brak presji stosów i bezpośredniego Inkwizytora |