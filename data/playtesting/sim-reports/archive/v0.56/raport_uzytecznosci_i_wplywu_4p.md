# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v0.56

**Wersja Gry:** `v0.56` | **Data Badania:** 2026-08-16 14:59 | **Próba:** 3000 gier/setup (15000 gier na wariant) | **Ziarno:** 42
**Wynik Bazowy Kanonu 4P:** 🟢 ** 94.9** pkt | **Średnia Długość Partii:** `5.47 Er` | **Deadlocki:** `0.4%` | **Pas Biedy:** `25.3%`

---

## 1. 🗺️ Podsumowanie Ekosystemu Kanonu 4P (Matryca Wpływu Kart 3x3)

Rozkład wszystkich 50 kart frakcyjnych w matrycy **Wpływ na Frakcję ($\Delta \text{Share}$)** vs **Wpływ na Kanon 4P ($\Delta \text{4P Score}$)**:

| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |
| :--- | :---: | :---: | :--- | :--- |
| 👑 / ⚓ **Filar / Kotwica Kanonu** | **42** | 84% | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |
| ⚖️ **Zbalansowane Narzędzie** | **7** | 14% | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Optymalne** |
| 💤 **Karta Pasywna (Dead Weight)** | **0** | 0% | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia** |
| ⚠️ **Karta Destabilizująca (Disruptor)** | **1** | 2% | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |

---

## 2. 🃏 Warstwa I — Szczegółowa Analiza 50 Kart Frakcji w Kanonie 4P

### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)
Karty, których brak powoduje spadek wyniku Kanonu 4P o $\ge 4.0$ pkt lub załamanie winrate frakcji o $\ge 4.0\%$:

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `caa-10` **Echo Alhambry** | Cienie Al-Andalus | 0zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 24.7% → **8.9%** | **`-15.8%`** | 94.9 → **18.5 pkt** (`-76.4`) |
| `kb-02` **Pobór Podatków** | Korona & Borgiowie | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.4% → **7.6%** | **`-17.8%`** | 94.9 → **18.5 pkt** (`-76.4`) |
| `kb-04` **Faworyt Dworu** | Korona & Borgiowie | 2zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 25.4% → **35.8%** | **`+10.4%`** | 94.9 → **18.5 pkt** (`-76.4`) |
| `kb-05` **List Żelazny** | Korona & Borgiowie | 2zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 25.4% → **47.1%** | **`+21.7%`** | 94.9 → **18.5 pkt** (`-76.4`) |
| `kb-07` **Szantaż Pieczęcią** | Korona & Borgiowie | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.4% → **4.9%** | **`-20.5%`** | 94.9 → **18.5 pkt** (`-76.4`) |
| `kb-10` **Pieczęć Korony** | Korona & Borgiowie | 2zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 25.4% → **3.2%** | **`-22.2%`** | 94.9 → **18.5 pkt** (`-76.4`) |
| `kb-09` **Dekret Królewski** | Korona & Borgiowie | 3zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 25.4% → **9.3%** | **`-16.1%`** | 94.9 → **18.5 pkt** (`-76.4`) |
| `kt-03` **Zakazana Wiedza** | Kabała z Toledo | 0zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 25.3% → **35.1%** | **`+9.8%`** | 94.9 → **19.0 pkt** (`-75.9`) |
| `kt-05` **Wskazówka Cyklu** | Kabała z Toledo | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.3% → **7.3%** | **`-18.0%`** | 94.9 → **19.0 pkt** (`-75.9`) |
| `caa-08` **Kaptur Nocy** | Cienie Al-Andalus | 2zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.7% → **34.0%** | **`+9.3%`** | 94.9 → **19.2 pkt** (`-75.7`) |
| `gc-09` **Lista Dłużników** | Gildia Cieni | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.0% → **13.1%** | **`-10.9%`** | 94.9 → **19.9 pkt** (`-75.0`) |
| `kt-07` **Archiwum Ukryte** | Kabała z Toledo | 1zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 25.3% → **33.2%** | **`+7.9%`** | 94.9 → **28.6 pkt** (`-66.3`) |
| `caa-02` **Złoto z Kryjówki** | Cienie Al-Andalus | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.7% → **31.3%** | **`+6.6%`** | 94.9 → **42.9 pkt** (`-52.0`) |
| `caa-07` **Szantaż Bractwa** | Cienie Al-Andalus | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.7% → **31.0%** | **`+6.3%`** | 94.9 → **45.9 pkt** (`-49.0`) |
| `gc-06` **Szantaż** | Gildia Cieni | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.0% → **19.7%** | **`-4.3%`** | 94.9 → **56.6 pkt** (`-38.3`) |
| `gc-10` **Upadek Domu** | Gildia Cieni | 4zł / 2☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.0% → **30.4%** | **`+6.4%`** | 94.9 → **59.1 pkt** (`-35.8`) |
| `caa-04` **Fałszywy Trop** | Cienie Al-Andalus | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.7% → **30.9%** | **`+6.2%`** | 94.9 → **60.7 pkt** (`-34.2`) |
| `kb-03` **Plotka Dworska** | Korona & Borgiowie | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 25.4% → **29.1%** | **`+3.7%`** | 94.9 → **61.3 pkt** (`-33.6`) |
| `caa-09` **Kurier Relikwii** | Cienie Al-Andalus | 2zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.7% → **28.7%** | **`+4.0%`** | 94.9 → **63.9 pkt** (`-31.0`) |
| `kt-04` **Zwierciadło Herezji** | Kabała z Toledo | 0zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 25.3% → **30.0%** | **`+4.7%`** | 94.9 → **64.2 pkt** (`-30.7`) |
| `caa-01` **Przejście Podziemiami** | Cienie Al-Andalus | 0zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.7% → **28.2%** | **`+3.5%`** | 94.9 → **71.3 pkt** (`-23.6`) |
| `caa-03` **Cień na Rynku** | Cienie Al-Andalus | 0zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.7% → **29.4%** | **`+4.7%`** | 94.9 → **72.6 pkt** (`-22.3`) |
| `kt-01` **Rytuał Przejścia** | Kabała z Toledo | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 25.3% → **29.2%** | **`+3.9%`** | 94.9 → **76.9 pkt** (`-18.0`) |
| `kt-09` **Fragment Kodeksu** | Kabała z Toledo | 1zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 25.3% → **29.4%** | **`+4.1%`** | 94.9 → **78.2 pkt** (`-16.7`) |
| `caa-05` **Ukryty Kurier** | Cienie Al-Andalus | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.7% → **26.5%** | **`+1.8%`** | 94.9 → **79.1 pkt** (`-15.8`) |
| `kb-06` **Areszt Królewski** | Korona & Borgiowie | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 25.4% → **28.2%** | **`+2.8%`** | 94.9 → **79.6 pkt** (`-15.3`) |
| `kt-02` **Transmutacja Złota** | Kabała z Toledo | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 25.3% → **28.7%** | **`+3.4%`** | 94.9 → **80.6 pkt** (`-14.3`) |
| `so-06` **Areszt Trybunalski** | Święte Oficjum | 2zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.6% → **27.7%** | **`+2.1%`** | 94.9 → **83.4 pkt** (`-11.5`) |
| `kt-10` **Pieczęć Salomona** | Kabała z Toledo | 2zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.3% → **27.7%** | **`+2.4%`** | 94.9 → **84.5 pkt** (`-10.4`) |
| `kb-01` **Rozkaz Dworu** | Korona & Borgiowie | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.4% → **26.8%** | **`+1.4%`** | 94.9 → **84.7 pkt** (`-10.2`) |
| `gc-01` **Przekupiony Strażnik** | Gildia Cieni | 1zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.0% → **27.5%** | **`+3.5%`** | 94.9 → **85.5 pkt** (`-9.4`) |
| `so-05` **Wezwanie do Trybunału** | Święte Oficjum | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.6% → **27.4%** | **`+1.8%`** | 94.9 → **87.8 pkt** (`-7.1`) |
| `gc-07` **Skrytobójstwo** | Gildia Cieni | 2zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.0% → **26.4%** | **`+2.4%`** | 94.9 → **88.9 pkt** (`-6.0`) |
| `so-07` **Przesłuchanie Oficjum** | Święte Oficjum | 2zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.6% → **27.9%** | **`+2.3%`** | 94.9 → **89.1 pkt** (`-5.8`) |
| `caa-06` **Ucieczka z Lochów** | Cienie Al-Andalus | 2zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.7% → **23.8%** | **`-0.9%`** | 94.9 → **90.7 pkt** (`-4.2`) |
| `so-04` **Publiczne Ostrzeżenie** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.6% → **27.4%** | **`+1.8%`** | 94.9 → **91.2 pkt** (`-3.7`) |
| `kb-08` **Przekupstwo Sędziego** | Korona & Borgiowie | 3zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.4% → **24.3%** | **`-1.1%`** | 94.9 → **91.4 pkt** (`-3.5`) |
| `so-09` **Świadek Koronny** | Święte Oficjum | 2zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.6% → **26.9%** | **`+1.3%`** | 94.9 → **91.4 pkt** (`-3.5`) |
| `so-08` **Nasłanie Inkwizytora** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.6% → **23.9%** | **`-1.7%`** | 94.9 → **91.7 pkt** (`-3.2`) |
| `so-01` **Patrol Familiariuszy** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.6% → **27.1%** | **`+1.5%`** | 94.9 → **91.9 pkt** (`-3.0`) |
| `kt-06` **Przesłuchanie Imienia** | Kabała z Toledo | 2zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.3% → **24.3%** | **`-1.0%`** | 94.9 → **92.1 pkt** (`-2.8`) |
| `so-03` **Podejrzenie** | Święte Oficjum | 2zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.6% → **25.7%** | **`+0.1%`** | 94.9 → **92.4 pkt** (`-2.5`) |

### 2.2. ⚠️ Karty Destabilizujące Kanon 4P (Disruptors)
Karty, których wyłączenie podnosi 4P Score ($\Delta \text{4P} \ge +1.5$ pkt):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `gc-04` **Informator** | Gildia Cieni | 0zł / 1☣ | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) | 24.0% → **25.2%** | `+1.2%` | 94.9 → **96.1 pkt** (`+1.2`) |

### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich 50 Kart Frakcji w Kanonie 4P

| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Faction Win Share 4P | $\Delta$ Frakcji | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `caa-01` | **Przejście Podziemiami** | Cienie Al-Andalus | 0 | 0 | 24.7% → 28.2% | `+3.5%` | 71.3 | `-23.6` | 5.38 | 0.3% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `caa-03` | **Cień na Rynku** | Cienie Al-Andalus | 0 | 1 | 24.7% → 29.4% | `+4.7%` | 72.6 | `-22.3` | 5.47 | 0.5% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `caa-02` | **Złoto z Kryjówki** | Cienie Al-Andalus | 1 | 0 | 24.7% → 31.3% | `+6.6%` | 42.9 | `-52.0` | 5.32 | 0.3% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `caa-04` | **Fałszywy Trop** | Cienie Al-Andalus | 1 | 0 | 24.7% → 30.9% | `+6.2%` | 60.7 | `-34.2` | 5.37 | 0.4% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `caa-05` | **Ukryty Kurier** | Cienie Al-Andalus | 1 | 0 | 24.7% → 26.5% | `+1.8%` | 79.1 | `-15.8` | 5.41 | 0.3% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-07` | **Szantaż Bractwa** | Cienie Al-Andalus | 1 | 0 | 24.7% → 31.0% | `+6.3%` | 45.9 | `-49.0` | 5.35 | 0.3% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `caa-06` | **Ucieczka z Lochów** | Cienie Al-Andalus | 2 | 1 | 24.7% → 23.8% | `-0.9%` | 90.7 | `-4.2` | 5.48 | 0.6% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-08` | **Kaptur Nocy** | Cienie Al-Andalus | 2 | 1 | 24.7% → 34.0% | `+9.3%` | 19.2 | `-75.7` | 5.38 | 0.5% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `caa-10` | **Echo Alhambry** | Cienie Al-Andalus | 0 | 1 | 24.7% → 8.9% | `-15.8%` | 18.5 | `-76.4` | 5.83 | 1.0% | 👑 FILAR KANONU (Core Keystone) |
| `caa-09` | **Kurier Relikwii** | Cienie Al-Andalus | 2 | 0 | 24.7% → 28.7% | `+4.0%` | 63.9 | `-31.0` | 5.42 | 0.4% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `gc-04` | **Informator** | Gildia Cieni | 0 | 1 | 24.0% → 25.2% | `+1.2%` | 96.1 | `+1.2` | 5.47 | 0.4% | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) |
| `gc-05` | **Fałszywy Świadek** | Gildia Cieni | 0 | 0 | 24.0% → 25.0% | `+1.0%` | 94.6 | `-0.3` | 5.43 | 0.4% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `gc-01` | **Przekupiony Strażnik** | Gildia Cieni | 1 | 1 | 24.0% → 27.5% | `+3.5%` | 85.5 | `-9.4` | 5.41 | 0.4% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `gc-03` | **Podrzucenie Księgi** | Gildia Cieni | 1 | 0 | 24.0% → 24.5% | `+0.5%` | 95.8 | `+0.9` | 5.46 | 0.4% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-02` | **Czarny Rynek** | Gildia Cieni | 2 | 1 | 24.0% → 24.4% | `+0.4%` | 94.2 | `-0.7` | 5.44 | 0.4% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-06` | **Szantaż** | Gildia Cieni | 2 | 0 | 24.0% → 19.7% | `-4.3%` | 56.6 | `-38.3` | 5.52 | 0.3% | 👑 FILAR KANONU (Core Keystone) |
| `gc-07` | **Skrytobójstwo** | Gildia Cieni | 2 | 0 | 24.0% → 26.4% | `+2.4%` | 88.9 | `-6.0` | 5.39 | 0.4% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-08` | **Zatrute Złoto** | Gildia Cieni | 2 | 0 | 24.0% → 23.8% | `-0.2%` | 94.1 | `-0.8` | 5.46 | 0.4% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-09` | **Lista Dłużników** | Gildia Cieni | 2 | 0 | 24.0% → 13.1% | `-10.9%` | 19.9 | `-75.0` | 5.59 | 0.5% | 👑 FILAR KANONU (Core Keystone) |
| `gc-10` | **Upadek Domu** | Gildia Cieni | 4 | 2 | 24.0% → 30.4% | `+6.4%` | 59.1 | `-35.8` | 5.40 | 0.5% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kb-01` | **Rozkaz Dworu** | Korona & Borgiowie | 1 | 0 | 25.4% → 26.8% | `+1.4%` | 84.7 | `-10.2` | 5.43 | 0.3% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kb-02` | **Pobór Podatków** | Korona & Borgiowie | 1 | 0 | 25.4% → 7.6% | `-17.8%` | 18.5 | `-76.4` | 5.70 | 0.9% | 👑 FILAR KANONU (Core Keystone) |
| `kb-03` | **Plotka Dworska** | Korona & Borgiowie | 1 | 0 | 25.4% → 29.1% | `+3.7%` | 61.3 | `-33.6` | 5.43 | 0.3% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kb-04` | **Faworyt Dworu** | Korona & Borgiowie | 2 | 1 | 25.4% → 35.8% | `+10.4%` | 18.5 | `-76.4` | 5.32 | 0.2% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kb-05` | **List Żelazny** | Korona & Borgiowie | 2 | 0 | 25.4% → 47.1% | `+21.7%` | 18.5 | `-76.4` | 5.00 | 0.1% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kb-06` | **Areszt Królewski** | Korona & Borgiowie | 1 | 0 | 25.4% → 28.2% | `+2.8%` | 79.6 | `-15.3` | 5.40 | 0.3% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kb-07` | **Szantaż Pieczęcią** | Korona & Borgiowie | 2 | 0 | 25.4% → 4.9% | `-20.5%` | 18.5 | `-76.4` | 5.73 | 1.3% | 👑 FILAR KANONU (Core Keystone) |
| `kb-08` | **Przekupstwo Sędziego** | Korona & Borgiowie | 3 | 0 | 25.4% → 24.3% | `-1.1%` | 91.4 | `-3.5` | 5.48 | 0.5% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kb-10` | **Pieczęć Korony** | Korona & Borgiowie | 2 | 2 | 25.4% → 3.2% | `-22.2%` | 18.5 | `-76.4` | 5.93 | 1.4% | 👑 FILAR KANONU (Core Keystone) |
| `kb-09` | **Dekret Królewski** | Korona & Borgiowie | 3 | 1 | 25.4% → 9.3% | `-16.1%` | 18.5 | `-76.4` | 5.74 | 0.9% | 👑 FILAR KANONU (Core Keystone) |
| `kt-03` | **Zakazana Wiedza** | Kabała z Toledo | 0 | 1 | 25.3% → 35.1% | `+9.8%` | 19.0 | `-75.9` | 5.31 | 0.2% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-04` | **Zwierciadło Herezji** | Kabała z Toledo | 0 | 0 | 25.3% → 30.0% | `+4.7%` | 64.2 | `-30.7` | 5.43 | 0.3% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-01` | **Rytuał Przejścia** | Kabała z Toledo | 1 | 0 | 25.3% → 29.2% | `+3.9%` | 76.9 | `-18.0` | 5.37 | 0.2% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-02` | **Transmutacja Złota** | Kabała z Toledo | 1 | 0 | 25.3% → 28.7% | `+3.4%` | 80.6 | `-14.3` | 5.35 | 0.2% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-05` | **Wskazówka Cyklu** | Kabała z Toledo | 1 | 0 | 25.3% → 7.3% | `-18.0%` | 19.0 | `-75.9` | 5.62 | 1.1% | 👑 FILAR KANONU (Core Keystone) |
| `kt-07` | **Archiwum Ukryte** | Kabała z Toledo | 1 | 1 | 25.3% → 33.2% | `+7.9%` | 28.6 | `-66.3` | 5.35 | 0.2% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-06` | **Przesłuchanie Imienia** | Kabała z Toledo | 2 | 0 | 25.3% → 24.3% | `-1.0%` | 92.1 | `-2.8` | 5.39 | 0.4% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kt-08` | **Areszt Wiedzy** | Kabała z Toledo | 2 | 0 | 25.3% → 25.6% | `+0.3%` | 95.5 | `+0.6` | 5.37 | 0.3% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-09` | **Fragment Kodeksu** | Kabała z Toledo | 1 | 1 | 25.3% → 29.4% | `+4.1%` | 78.2 | `-16.7` | 5.41 | 0.4% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-10` | **Pieczęć Salomona** | Kabała z Toledo | 2 | 1 | 25.3% → 27.7% | `+2.4%` | 84.5 | `-10.4` | 5.47 | 0.6% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-05` | **Wezwanie do Trybunału** | Święte Oficjum | 0 | 0 | 25.6% → 27.4% | `+1.8%` | 87.8 | `-7.1` | 5.43 | 0.4% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-01` | **Patrol Familiariuszy** | Święte Oficjum | 1 | 0 | 25.6% → 27.1% | `+1.5%` | 91.9 | `-3.0` | 5.43 | 0.5% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-02` | **Skarbiec Trybunału** | Święte Oficjum | 1 | 0 | 25.6% → 25.9% | `+0.3%` | 94.0 | `-0.9` | 5.46 | 0.5% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-04` | **Publiczne Ostrzeżenie** | Święte Oficjum | 1 | 0 | 25.6% → 27.4% | `+1.8%` | 91.2 | `-3.7` | 5.44 | 0.4% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-03` | **Podejrzenie** | Święte Oficjum | 2 | 0 | 25.6% → 25.7% | `+0.1%` | 92.4 | `-2.5` | 5.48 | 0.4% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-08` | **Nasłanie Inkwizytora** | Święte Oficjum | 1 | 0 | 25.6% → 23.9% | `-1.7%` | 91.7 | `-3.2` | 5.52 | 0.6% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-06` | **Areszt Trybunalski** | Święte Oficjum | 2 | 0 | 25.6% → 27.7% | `+2.1%` | 83.4 | `-11.5` | 5.43 | 0.4% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-07` | **Przesłuchanie Oficjum** | Święte Oficjum | 2 | 0 | 25.6% → 27.9% | `+2.3%` | 89.1 | `-5.8` | 5.41 | 0.4% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-09` | **Świadek Koronny** | Święte Oficjum | 2 | 0 | 25.6% → 26.9% | `+1.3%` | 91.4 | `-3.5` | 5.43 | 0.4% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-10` | **Oczyść Miasto** | Święte Oficjum | 5 | 2 | 25.6% → 25.1% | `-0.5%` | 94.4 | `-0.5` | 5.47 | 0.5% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |

---

## 3. ⏳ Warstwa II — Kronika Dziejów w 4P (Ablacja 8 Kart Wydarzeń Czasu)

Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans w 4P:

| ID | Karta Wydarzenia | 4P Score | $\Delta$ 4P | Średnia Er | Deadlock % | Status Roli w Kronice |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `tc-01` | **Kres Średniowiecza** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | ⚖️ Neutralna Kronika |
| `tc-02` | **Płonący Stos** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | ⚖️ Neutralna Kronika |
| `tc-03` | **Królewski Podatek** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | ⚖️ Neutralna Kronika |
| `tc-04` | **Spisek w Cieniu** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | ⚖️ Neutralna Kronika |
| `tc-05` | **Złoty Wiek** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | ⚖️ Neutralna Kronika |
| `tc-06` | **Czystka w Mieście** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | ⚖️ Neutralna Kronika |
| `tc-07` | **Druga Szansa** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | ⚖️ Neutralna Kronika |
| `tc-08` | **Zaćmienie Słońca** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | ⚖️ Neutralna Kronika |

---

## 4. ⚙️ Warstwa III — Globalne Mechaniki i Parametry Silnika w 4P

Badanie odporności Kanonu 4P na wyłączenie lub skrajne przestawienie bazowych parametrów silnika:

| Badany Podsystem / Parametr | 4P Score | $\Delta$ 4P | Średnia Er | Deadlocks % | Pas Biedy % | Diagnoza i Wpływ na Silnik |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Wyłączona Kronika Dziejów (Talia Czasu)** | 94.9 → 🔴 ** 13.2** (`-81.7`) | `-81.7 pkt` | 5.72 Er | 0.9% | 28.1% | 🔴 Katastrofa ekosystemu — filar bezwzględnie krytyczny dla Kanonu 4P |
| **Autodafé Cooldown = 2 Ery (Agresywna czystka)** | 94.9 → 🟢 ** 94.1** (`-0.8`) | `-0.8 pkt` | 5.47 Er | 0.5% | 25.3% | ⚪ Wpływ neutralny / mechanika stabilna |
| **Autodafé Cooldown = 4 Ery (Rzadka czystka)** | 94.9 → 🟢 ** 94.6** (`-0.3`) | `-0.3 pkt` | 5.47 Er | 0.5% | 25.3% | ⚪ Wpływ neutralny / mechanika stabilna |

---

## 5. ⚔️ Warstwa IV — Asymetryczne Ścieżki Zwycięstwa w 4P (Victory Paths)

Badanie krytyczności i elastyczności unikalnych bramek zwycięstwa dla każdej frakcji w Kanonie 4P:

| Badana Ścieżka / Bramka Wygranej | 4P Score | $\Delta$ 4P | Średnia Er | Deadlocks % | Pas Biedy % | Diagnoza Ścieżki Zwycięstwa |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |

---

## 6. 👥 Warstwa V — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych w Kanonie 4P:

| Nieobecna Frakcja | Setup Testowy | 4P Score Setupu | Diagnoza Wpływu Braku Frakcji na Stół 4P |
| :--- | :--- | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`99.3 pkt`** | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`94.8 pkt`** | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`92.5 pkt`** | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`92.6 pkt`** | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`95.4 pkt`** | Brak presji stosów i bezpośredniego Inkwizytora |