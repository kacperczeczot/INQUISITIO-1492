[Strona główna](../../../../../README.md) > [v0.86](README.md) > [raport_uzytecznosci_i_wplywu_4p](raport_uzytecznosci_i_wplywu_4p.md)

---

# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v0.86

**Wersja Gry:** `v0.86` | **Data Badania:** 2026-08-17 12:40 | **Próba:** 5000 gier/setup (25000 gier na wariant) | **Ziarno:** 42
**Wynik Bazowy Kanonu 4P:** 🟢 ** 94.6** pkt | **Średnia Długość Partii:** `5.94 Er` | **Deadlocki:** `1.1%` | **Pas Biedy:** `5.6%`

---

## 1. 🗺️ Podsumowanie Ekosystemu Kart Kanonu 4P (Matryca Wpływu Kart 3x3)

Rozkład wszystkich 50 kart frakcyjnych w matrycy **Wpływ na Frakcję ($\Delta \text{Share}$)** vs **Wpływ na Kanon 4P ($\Delta \text{4P Score}$)**:

| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |
| :--- | :---: | :---: | :--- | :--- |
| 👑 / ⚓ **Filar / Kotwica Kanonu** | **57** | 114% | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |
| ⚖️ **Zbalansowane Narzędzie** | **3** | 6% | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Optymalne** |
| 💤 **Karta Pasywna (Dead Weight)** | **0** | 0% | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia** |
| ⚠️ **Karta Destabilizująca (Disruptor)** | **0** | 0% | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |

---

## 2. 🃏 Warstwa I — Szczegółowa Analiza 50 Kart Frakcji w Kanonie 4P

### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)
Karty, których brak powoduje spadek wyniku Kanonu 4P o $\ge 4.0$ pkt lub załamanie winrate frakcji o $\ge 4.0\%$:

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kb-09` **Dekret Królewski** | Korona & Borgiowie | 3zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 24.8% → **1.1%** | **`-23.7%`** | 94.6 → **35.1 pkt** (`-59.5`) |
| `kb-10` **Pieczęć Korony** | Korona & Borgiowie | 2zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 24.8% → **3.2%** | **`-21.6%`** | 94.6 → **38.4 pkt** (`-56.2`) |
| `kb-04` **Faworyt Dworu** | Korona & Borgiowie | 2zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.8% → **40.9%** | **`+16.1%`** | 94.6 → **50.3 pkt** (`-44.3`) |
| `kt-05` **Wskazówka Cyklu** | Kabała z Toledo | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.6% → **10.3%** | **`-14.3%`** | 94.6 → **52.8 pkt** (`-41.8`) |
| `kb-05` **List Żelazny** | Korona & Borgiowie | 2zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.8% → **39.3%** | **`+14.5%`** | 94.6 → **54.0 pkt** (`-40.6`) |
| `kb-07` **Szantaż Pieczęcią** | Korona & Borgiowie | 2zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.8% → **37.3%** | **`+12.5%`** | 94.6 → **59.3 pkt** (`-35.3`) |
| `kb-08` **Przekupstwo Sędziego** | Korona & Borgiowie | 2zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.8% → **37.3%** | **`+12.5%`** | 94.6 → **59.3 pkt** (`-35.3`) |
| `kb-02` **Pobór Podatków** | Korona & Borgiowie | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.8% → **13.5%** | **`-11.3%`** | 94.6 → **61.5 pkt** (`-33.1`) |
| `gc-06` **Szantaż** | Gildia Cieni | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.1% → **13.7%** | **`-11.4%`** | 94.6 → **62.1 pkt** (`-32.5`) |
| `gc-09` **Lista Dłużników** | Gildia Cieni | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.1% → **14.4%** | **`-10.7%`** | 94.6 → **63.0 pkt** (`-31.6`) |
| `caa-05` **Ukryty Kurier** | Cienie Al-Andalus | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.4% → **17.4%** | **`-8.0%`** | 94.6 → **71.8 pkt** (`-22.8`) |
| `caa-12` **Skrytka w Murach** | Cienie Al-Andalus | 0zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 25.4% → **31.3%** | **`+5.9%`** | 94.6 → **76.9 pkt** (`-17.7`) |
| `caa-10` **Echo Alhambry** | Cienie Al-Andalus | 1zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 25.4% → **19.7%** | **`-5.7%`** | 94.6 → **79.6 pkt** (`-15.0`) |
| `kt-04` **Zwierciadło Herezji** | Kabała z Toledo | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.6% → **29.5%** | **`+4.9%`** | 94.6 → **80.1 pkt** (`-14.5`) |
| `kt-12` **Strażnik Archiwum** | Kabała z Toledo | 0zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.6% → **30.2%** | **`+5.6%`** | 94.6 → **80.2 pkt** (`-14.4`) |
| `gc-12` **Złodziejski Zwiad** | Gildia Cieni | 0zł / 2☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 25.1% → **30.1%** | **`+5.0%`** | 94.6 → **81.2 pkt** (`-13.4`) |
| `kt-07` **Archiwum Ukryte** | Kabała z Toledo | 1zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.6% → **29.6%** | **`+5.0%`** | 94.6 → **81.2 pkt** (`-13.4`) |
| `kt-02` **Transmutacja Złota** | Kabała z Toledo | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.6% → **29.7%** | **`+5.1%`** | 94.6 → **81.6 pkt** (`-13.0`) |
| `kt-11` **Medytacja Sefirot** | Kabała z Toledo | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.6% → **29.3%** | **`+4.7%`** | 94.6 → **82.7 pkt** (`-11.9`) |
| `kt-01` **Rytuał Przejścia** | Kabała z Toledo | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.6% → **29.0%** | **`+4.4%`** | 94.6 → **83.5 pkt** (`-11.1`) |
| `caa-02` **Złoto z Kryjówki** | Cienie Al-Andalus | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 25.4% → **28.8%** | **`+3.4%`** | 94.6 → **84.4 pkt** (`-10.2`) |
| `caa-09` **Kurier Relikwii** | Cienie Al-Andalus | 2zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 25.4% → **28.9%** | **`+3.5%`** | 94.6 → **84.4 pkt** (`-10.2`) |
| `kt-03` **Zakazana Wiedza** | Kabała z Toledo | 0zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.6% → **28.6%** | **`+4.0%`** | 94.6 → **85.2 pkt** (`-9.4`) |
| `caa-04` **Fałszywy Trop** | Cienie Al-Andalus | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.4% → **27.6%** | **`+2.2%`** | 94.6 → **85.3 pkt** (`-9.3`) |
| `kt-06` **Przesłuchanie Imienia** | Kabała z Toledo | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.6% → **21.6%** | **`-3.0%`** | 94.6 → **85.4 pkt** (`-9.2`) |
| `caa-08` **Kaptur Nocy** | Cienie Al-Andalus | 2zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 25.4% → **28.5%** | **`+3.1%`** | 94.6 → **85.5 pkt** (`-9.1`) |
| `kb-11` **Tajny Emisariusz** | Korona & Borgiowie | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.8% → **21.7%** | **`-3.1%`** | 94.6 → **85.6 pkt** (`-9.0`) |
| `kb-03` **Plotka Dworska** | Korona & Borgiowie | 1zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 24.8% → **22.3%** | **`-2.5%`** | 94.6 → **86.0 pkt** (`-8.6`) |
| `caa-07` **Szantaż Bractwa** | Cienie Al-Andalus | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 25.4% → **28.1%** | **`+2.7%`** | 94.6 → **86.4 pkt** (`-8.2`) |
| `gc-04` **Informator** | Gildia Cieni | 0zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 25.1% → **28.2%** | **`+3.1%`** | 94.6 → **86.8 pkt** (`-7.8`) |
| `gc-11` **Fałszywe Świadectwo Cechu** | Gildia Cieni | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.1% → **26.1%** | **`+1.0%`** | 94.6 → **86.8 pkt** (`-7.8`) |
| `kb-01` **Rozkaz Dworu** | Korona & Borgiowie | 1zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 24.8% → **22.0%** | **`-2.8%`** | 94.6 → **86.8 pkt** (`-7.8`) |
| `gc-07` **Skrytobójstwo** | Gildia Cieni | 2zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 25.1% → **28.1%** | **`+3.0%`** | 94.6 → **87.1 pkt** (`-7.5`) |
| `so-06` **Areszt Trybunalski** | Święte Oficjum | 2zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.0% → **25.9%** | **`+0.9%`** | 94.6 → **87.2 pkt** (`-7.4`) |
| `kb-06` **Areszt Królewski** | Korona & Borgiowie | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.8% → **27.2%** | **`+2.4%`** | 94.6 → **88.5 pkt** (`-6.1`) |
| `gc-01` **Przekupiony Strażnik** | Gildia Cieni | 1zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 25.1% → **28.1%** | **`+3.0%`** | 94.6 → **88.6 pkt** (`-6.0`) |
| `gc-03` **Podrzucenie Księgi** | Gildia Cieni | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.1% → **26.2%** | **`+1.1%`** | 94.6 → **88.6 pkt** (`-6.0`) |
| `kt-08` **Areszt Wiedzy** | Kabała z Toledo | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 24.6% → **27.2%** | **`+2.6%`** | 94.6 → **88.7 pkt** (`-5.9`) |
| `caa-06` **Ucieczka z Lochów** | Cienie Al-Andalus | 2zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.4% → **23.0%** | **`-2.4%`** | 94.6 → **88.9 pkt** (`-5.7`) |
| `gc-02` **Czarny Rynek** | Gildia Cieni | 1zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 25.1% → **27.9%** | **`+2.8%`** | 94.6 → **89.0 pkt** (`-5.6`) |
| `gc-10` **Upadek Domu** | Gildia Cieni | 4zł / 2☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.1% → **25.6%** | **`+0.5%`** | 94.6 → **90.1 pkt** (`-4.5`) |
| `caa-03` **Cień na Rynku** | Cienie Al-Andalus | 0zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.4% → **23.7%** | **`-1.7%`** | 94.6 → **90.7 pkt** (`-3.9`) |
| `caa-11` **Nocna Zmiana Warty** | Cienie Al-Andalus | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.4% → **24.6%** | **`-0.8%`** | 94.6 → **90.9 pkt** (`-3.7`) |
| `gc-05` **Fałszywy Świadek** | Gildia Cieni | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.1% → **26.5%** | **`+1.4%`** | 94.6 → **90.9 pkt** (`-3.7`) |
| `kt-10` **Pieczęć Salomona** | Kabała z Toledo | 2zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.6% → **25.7%** | **`+1.1%`** | 94.6 → **90.9 pkt** (`-3.7`) |
| `gc-08` **Zatrute Złoto** | Gildia Cieni | 2zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.1% → **26.2%** | **`+1.1%`** | 94.6 → **91.0 pkt** (`-3.6`) |
| `so-12` **Straż Trybunalska** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.0% → **25.9%** | **`+0.9%`** | 94.6 → **91.3 pkt** (`-3.3`) |
| `kb-12` **Szantaż Salonowy** | Korona & Borgiowie | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.8% → **25.8%** | **`+1.0%`** | 94.6 → **91.4 pkt** (`-3.2`) |
| `so-02` **Skarbiec Trybunału** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.0% → **24.5%** | **`-0.5%`** | 94.6 → **91.4 pkt** (`-3.2`) |
| `so-09` **Świadek Koronny** | Święte Oficjum | 2zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.0% → **25.8%** | **`+0.8%`** | 94.6 → **91.7 pkt** (`-2.9`) |
| `caa-01` **Przejście Podziemiami** | Cienie Al-Andalus | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.4% → **23.8%** | **`-1.6%`** | 94.6 → **91.9 pkt** (`-2.7`) |
| `so-05` **Wezwanie do Trybunału** | Święte Oficjum | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.0% → **23.6%** | **`-1.4%`** | 94.6 → **91.9 pkt** (`-2.7`) |
| `so-01` **Patrol Familiariuszy** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.0% → **25.9%** | **`+0.9%`** | 94.6 → **91.9 pkt** (`-2.7`) |
| `so-04` **Publiczne Ostrzeżenie** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.0% → **26.2%** | **`+1.2%`** | 94.6 → **92.0 pkt** (`-2.6`) |
| `so-11` **Dekret Czystości Wiary** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.0% → **23.9%** | **`-1.1%`** | 94.6 → **92.3 pkt** (`-2.3`) |
| `so-08` **Nasłanie Inkwizytora** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.0% → **26.1%** | **`+1.1%`** | 94.6 → **92.4 pkt** (`-2.2`) |
| `kt-09` **Fragment Kodeksu** | Kabała z Toledo | 2zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.6% → **24.8%** | **`+0.2%`** | 94.6 → **92.5 pkt** (`-2.1`) |

### 2.2. ⚠️ Karty Destabilizujące Kanon 4P (Disruptors)
Karty, których wyłączenie podnosi 4P Score ($\Delta \text{4P} \ge +1.5$ pkt):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *Brak kart destabilizujących* | - | - | - | - | - | - |

### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich 50 Kart Frakcji w Kanonie 4P

| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Faction Win Share 4P | $\Delta$ Frakcji | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `caa-01` | **Przejście Podziemiami** | Cienie Al-Andalus | 0 | 0 | 25.4% → 23.8% | `-1.6%` | 91.9 | `-2.7` | 5.96 | 1.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-03` | **Cień na Rynku** | Cienie Al-Andalus | 0 | 1 | 25.4% → 23.7% | `-1.7%` | 90.7 | `-3.9` | 6.13 | 1.4% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-05` | **Ukryty Kurier** | Cienie Al-Andalus | 0 | 0 | 25.4% → 17.4% | `-8.0%` | 71.8 | `-22.8` | 6.07 | 1.2% | 👑 FILAR KANONU (Core Keystone) |
| `caa-12` | **Skrytka w Murach** | Cienie Al-Andalus | 0 | 1 | 25.4% → 31.3% | `+5.9%` | 76.9 | `-17.7` | 5.86 | 1.3% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `caa-02` | **Złoto z Kryjówki** | Cienie Al-Andalus | 1 | 0 | 25.4% → 28.8% | `+3.4%` | 84.4 | `-10.2` | 5.82 | 1.1% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `caa-04` | **Fałszywy Trop** | Cienie Al-Andalus | 1 | 0 | 25.4% → 27.6% | `+2.2%` | 85.3 | `-9.3` | 5.86 | 1.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-07` | **Szantaż Bractwa** | Cienie Al-Andalus | 1 | 0 | 25.4% → 28.1% | `+2.7%` | 86.4 | `-8.2` | 5.85 | 1.0% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `caa-11` | **Nocna Zmiana Warty** | Cienie Al-Andalus | 1 | 0 | 25.4% → 24.6% | `-0.8%` | 90.9 | `-3.7` | 5.94 | 1.2% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-06` | **Ucieczka z Lochów** | Cienie Al-Andalus | 2 | 1 | 25.4% → 23.0% | `-2.4%` | 88.9 | `-5.7` | 5.97 | 1.3% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-08` | **Kaptur Nocy** | Cienie Al-Andalus | 2 | 1 | 25.4% → 28.5% | `+3.1%` | 85.5 | `-9.1` | 5.85 | 0.9% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `caa-10` | **Echo Alhambry** | Cienie Al-Andalus | 1 | 1 | 25.4% → 19.7% | `-5.7%` | 79.6 | `-15.0` | 6.27 | 1.6% | 👑 FILAR KANONU (Core Keystone) |
| `caa-09` | **Kurier Relikwii** | Cienie Al-Andalus | 2 | 0 | 25.4% → 28.9% | `+3.5%` | 84.4 | `-10.2` | 5.85 | 1.1% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `gc-04` | **Informator** | Gildia Cieni | 0 | 1 | 25.1% → 28.2% | `+3.1%` | 86.8 | `-7.8` | 5.88 | 1.1% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `gc-05` | **Fałszywy Świadek** | Gildia Cieni | 0 | 0 | 25.1% → 26.5% | `+1.4%` | 90.9 | `-3.7` | 5.91 | 1.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-12` | **Złodziejski Zwiad** | Gildia Cieni | 0 | 2 | 25.1% → 30.1% | `+5.0%` | 81.2 | `-13.4` | 5.87 | 1.0% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `gc-01` | **Przekupiony Strażnik** | Gildia Cieni | 1 | 1 | 25.1% → 28.1% | `+3.0%` | 88.6 | `-6.0` | 5.89 | 1.0% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `gc-02` | **Czarny Rynek** | Gildia Cieni | 1 | 1 | 25.1% → 27.9% | `+2.8%` | 89.0 | `-5.6` | 5.91 | 1.1% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `gc-03` | **Podrzucenie Księgi** | Gildia Cieni | 1 | 0 | 25.1% → 26.2% | `+1.1%` | 88.6 | `-6.0` | 5.91 | 1.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-11` | **Fałszywe Świadectwo Cechu** | Gildia Cieni | 1 | 0 | 25.1% → 26.1% | `+1.0%` | 86.8 | `-7.8` | 5.92 | 1.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-06` | **Szantaż** | Gildia Cieni | 2 | 0 | 25.1% → 13.7% | `-11.4%` | 62.1 | `-32.5` | 6.16 | 1.6% | 👑 FILAR KANONU (Core Keystone) |
| `gc-07` | **Skrytobójstwo** | Gildia Cieni | 2 | 0 | 25.1% → 28.1% | `+3.0%` | 87.1 | `-7.5` | 5.87 | 1.0% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `gc-08` | **Zatrute Złoto** | Gildia Cieni | 2 | 0 | 25.1% → 26.2% | `+1.1%` | 91.0 | `-3.6` | 5.93 | 1.2% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-09` | **Lista Dłużników** | Gildia Cieni | 2 | 0 | 25.1% → 14.4% | `-10.7%` | 63.0 | `-31.6` | 6.15 | 1.5% | 👑 FILAR KANONU (Core Keystone) |
| `gc-10` | **Upadek Domu** | Gildia Cieni | 4 | 2 | 25.1% → 25.6% | `+0.5%` | 90.1 | `-4.5` | 6.01 | 1.2% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kb-01` | **Rozkaz Dworu** | Korona & Borgiowie | 1 | 1 | 24.8% → 22.0% | `-2.8%` | 86.8 | `-7.8` | 6.01 | 1.2% | 👑 FILAR KANONU (Core Keystone) |
| `kb-02` | **Pobór Podatków** | Korona & Borgiowie | 1 | 0 | 24.8% → 13.5% | `-11.3%` | 61.5 | `-33.1` | 6.19 | 2.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-03` | **Plotka Dworska** | Korona & Borgiowie | 1 | 1 | 24.8% → 22.3% | `-2.5%` | 86.0 | `-8.6` | 5.99 | 1.2% | 👑 FILAR KANONU (Core Keystone) |
| `kb-11` | **Tajny Emisariusz** | Korona & Borgiowie | 1 | 0 | 24.8% → 21.7% | `-3.1%` | 85.6 | `-9.0` | 6.00 | 1.3% | 👑 FILAR KANONU (Core Keystone) |
| `kb-04` | **Faworyt Dworu** | Korona & Borgiowie | 2 | 1 | 24.8% → 40.9% | `+16.1%` | 50.3 | `-44.3` | 5.64 | 0.6% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kb-05` | **List Żelazny** | Korona & Borgiowie | 2 | 0 | 24.8% → 39.3% | `+14.5%` | 54.0 | `-40.6` | 5.60 | 0.5% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kb-06` | **Areszt Królewski** | Korona & Borgiowie | 1 | 0 | 24.8% → 27.2% | `+2.4%` | 88.5 | `-6.1` | 5.89 | 1.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kb-12` | **Szantaż Salonowy** | Korona & Borgiowie | 1 | 0 | 24.8% → 25.8% | `+1.0%` | 91.4 | `-3.2` | 5.93 | 1.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kb-07` | **Szantaż Pieczęcią** | Korona & Borgiowie | 2 | 0 | 24.8% → 37.3% | `+12.5%` | 59.3 | `-35.3` | 5.71 | 0.5% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kb-08` | **Przekupstwo Sędziego** | Korona & Borgiowie | 2 | 0 | 24.8% → 37.3% | `+12.5%` | 59.3 | `-35.3` | 5.71 | 0.5% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kb-10` | **Pieczęć Korony** | Korona & Borgiowie | 2 | 2 | 24.8% → 3.2% | `-21.6%` | 38.4 | `-56.2` | 6.45 | 2.3% | 👑 FILAR KANONU (Core Keystone) |
| `kb-09` | **Dekret Królewski** | Korona & Borgiowie | 3 | 1 | 24.8% → 1.1% | `-23.7%` | 35.1 | `-59.5` | 6.41 | 2.8% | 👑 FILAR KANONU (Core Keystone) |
| `kt-03` | **Zakazana Wiedza** | Kabała z Toledo | 0 | 1 | 24.6% → 28.6% | `+4.0%` | 85.2 | `-9.4` | 5.96 | 1.2% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-12` | **Strażnik Archiwum** | Kabała z Toledo | 0 | 1 | 24.6% → 30.2% | `+5.6%` | 80.2 | `-14.4` | 5.84 | 1.1% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-01` | **Rytuał Przejścia** | Kabała z Toledo | 1 | 0 | 24.6% → 29.0% | `+4.4%` | 83.5 | `-11.1` | 5.85 | 1.2% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-02` | **Transmutacja Złota** | Kabała z Toledo | 1 | 0 | 24.6% → 29.7% | `+5.1%` | 81.6 | `-13.0` | 5.85 | 1.2% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-04` | **Zwierciadło Herezji** | Kabała z Toledo | 1 | 0 | 24.6% → 29.5% | `+4.9%` | 80.1 | `-14.5` | 5.87 | 1.2% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-05` | **Wskazówka Cyklu** | Kabała z Toledo | 1 | 0 | 24.6% → 10.3% | `-14.3%` | 52.8 | `-41.8` | 6.23 | 2.6% | 👑 FILAR KANONU (Core Keystone) |
| `kt-07` | **Archiwum Ukryte** | Kabała z Toledo | 1 | 1 | 24.6% → 29.6% | `+5.0%` | 81.2 | `-13.4` | 5.86 | 1.2% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-08` | **Areszt Wiedzy** | Kabała z Toledo | 1 | 0 | 24.6% → 27.2% | `+2.6%` | 88.7 | `-5.9` | 5.86 | 1.2% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-11` | **Medytacja Sefirot** | Kabała z Toledo | 1 | 0 | 24.6% → 29.3% | `+4.7%` | 82.7 | `-11.9` | 5.84 | 1.1% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-06` | **Przesłuchanie Imienia** | Kabała z Toledo | 2 | 0 | 24.6% → 21.6% | `-3.0%` | 85.4 | `-9.2` | 5.99 | 1.6% | 👑 FILAR KANONU (Core Keystone) |
| `kt-09` | **Fragment Kodeksu** | Kabała z Toledo | 2 | 1 | 24.6% → 24.8% | `+0.2%` | 92.5 | `-2.1` | 5.98 | 1.2% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kt-10` | **Pieczęć Salomona** | Kabała z Toledo | 2 | 1 | 24.6% → 25.7% | `+1.1%` | 90.9 | `-3.7` | 6.01 | 1.2% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-05` | **Wezwanie do Trybunału** | Święte Oficjum | 0 | 0 | 25.0% → 23.6% | `-1.4%` | 91.9 | `-2.7` | 5.98 | 1.2% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-01` | **Patrol Familiariuszy** | Święte Oficjum | 1 | 0 | 25.0% → 25.9% | `+0.9%` | 91.9 | `-2.7` | 5.94 | 1.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-02` | **Skarbiec Trybunału** | Święte Oficjum | 1 | 0 | 25.0% → 24.5% | `-0.5%` | 91.4 | `-3.2` | 5.98 | 1.3% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-04` | **Publiczne Ostrzeżenie** | Święte Oficjum | 1 | 0 | 25.0% → 26.2% | `+1.2%` | 92.0 | `-2.6` | 5.98 | 1.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-12` | **Straż Trybunalska** | Święte Oficjum | 1 | 0 | 25.0% → 25.9% | `+0.9%` | 91.3 | `-3.3` | 5.93 | 1.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-03` | **Podejrzenie** | Święte Oficjum | 2 | 0 | 25.0% → 25.0% | `+0.0%` | 93.1 | `-1.5` | 5.96 | 1.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-08` | **Nasłanie Inkwizytora** | Święte Oficjum | 1 | 0 | 25.0% → 26.1% | `+1.1%` | 92.4 | `-2.2` | 5.95 | 1.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-11` | **Dekret Czystości Wiary** | Święte Oficjum | 1 | 0 | 25.0% → 23.9% | `-1.1%` | 92.3 | `-2.3` | 5.97 | 1.2% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-06` | **Areszt Trybunalski** | Święte Oficjum | 2 | 0 | 25.0% → 25.9% | `+0.9%` | 87.2 | `-7.4` | 5.89 | 1.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-07` | **Przesłuchanie Oficjum** | Święte Oficjum | 2 | 0 | 25.0% → 25.5% | `+0.5%` | 93.0 | `-1.6` | 5.94 | 1.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-09` | **Świadek Koronny** | Święte Oficjum | 2 | 0 | 25.0% → 25.8% | `+0.8%` | 91.7 | `-2.9` | 5.91 | 1.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-10` | **Oczyść Miasto** | Święte Oficjum | 5 | 2 | 25.0% → 25.4% | `+0.4%` | 92.9 | `-1.7` | 5.95 | 1.2% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |

---

## 3. ⏳ Warstwa II — Kronika Dziejów w 4P (Ablacja 8 Kart Wydarzeń Czasu)

Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans w 4P:

| ID | Karta Wydarzenia | 4P Score | $\Delta$ 4P | Średnia Er | Deadlock % | Status Roli w Kronice |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `tc-01` | **Kres Średniowiecza** | 🟢 ** 94.6** | `0.0 pkt` | 5.94 Er | 1.1% | ⚖️ Neutralna Kronika |
| `tc-02` | **Płonący Stos** | 🟢 ** 94.6** | `0.0 pkt` | 5.94 Er | 1.1% | ⚖️ Neutralna Kronika |
| `tc-03` | **Królewski Podatek** | 🟢 ** 94.6** | `0.0 pkt` | 5.94 Er | 1.1% | ⚖️ Neutralna Kronika |
| `tc-04` | **Spisek w Cieniu** | 🟢 ** 94.6** | `0.0 pkt` | 5.94 Er | 1.1% | ⚖️ Neutralna Kronika |
| `tc-05` | **Złoty Wiek** | 🟢 ** 94.6** | `0.0 pkt` | 5.94 Er | 1.1% | ⚖️ Neutralna Kronika |
| `tc-06` | **Czystka w Mieście** | 🟢 ** 94.6** | `0.0 pkt` | 5.94 Er | 1.1% | ⚖️ Neutralna Kronika |
| `tc-07` | **Druga Szansa** | 🟢 ** 94.6** | `0.0 pkt` | 5.94 Er | 1.1% | ⚖️ Neutralna Kronika |
| `tc-08` | **Zaćmienie Słońca** | 🟢 ** 94.6** | `0.0 pkt` | 5.94 Er | 1.1% | ⚖️ Neutralna Kronika |

---

## 4. ⚙️ Warstwa III — Matryca 9 Obszarów Wpływu Mechanik Gry (L1, L2, L4)

Zestawienie odporności Kanonu 4P na modyfikacje i ablację poszczególnych podsystemów według 9 obszarów istotności i efektu:

| Kategoria Mechaniki | Liczba Testów | Rola w Ekosystemie Kanonu 4P | Rekomendacja Balansowa |
| :--- | :---: | :--- | :--- |
| 👑 / 🛡️ **Filary i Bezpieczniki Stabilizujące** | **36** | Mechaniki krytyczne — ich brak lub rozregulowanie niszczy balans | **Nienaruszalny Kanon** |
| ⚖️ **Zbalansowane Regulatory / Pasywne** | **12** | Mechaniki harmonijnie wpisane w dynamikę rozgrywki | **Optymalne w Kanonie** |
| ⚠️ / 💡 **Obciążenia i Kandydaci do Uproszczenia** | **0** | Mechaniki, których modyfikacja lub redukcja podnosi wynik 4P | **Kandydaci do optymalizacji** |

### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)

| Badany Podsystem / Modyfikator L1 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Limit Er: 12 → 8 Er (Presja czasu)** | 94.6 → 🔴 ** 14.6** (`-80.0`) | `-80.0 pkt` | 5.72 Er | 22.1% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit Er: 12 → 16 Er (Wydłużony silnik)** | 94.6 → 🟢 ** 94.5** (`-0.1`) | `-0.1 pkt` | 5.95 Er | 0.1% | 5.5% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Próg Oskarżenia na Dworze: -1 (Agresywny Dwór)** | 94.6 → 🟡 ** 81.1** (`-13.5`) | `-13.5 pkt` | 6.05 Er | 1.6% | 4.9% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Próg Oskarżenia na Dworze: +1 (Pasywny Dwór)** | 94.6 → 🟡 ** 84.6** (`-10.0`) | `-10.0 pkt` | 5.84 Er | 0.7% | 6.1% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Złoto startowe: 4zł → 0zł (Skrajne ubóstwo)** | 94.6 → 🔴 ** 31.8** (`-62.8`) | `-62.8 pkt` | 6.84 Er | 4.2% | 18.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 6zł (Bogaty start)** | 94.6 → 🔴 ** 42.0** (`-52.6`) | `-52.6 pkt` | 5.46 Er | 0.5% | 3.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 2 Agentów (Ograniczony zasięg)** | 94.6 → 🟡 ** 82.2** (`-12.4`) | `-12.4 pkt` | 6.15 Er | 2.1% | 5.8% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Liczba Agentów: 3 → 4 Agentów (Gęsta plansza)** | 94.6 → 🟡 ** 77.0** (`-17.6`) | `-17.6 pkt` | 5.82 Er | 0.7% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 3 karty (Zmniejszona elastyczność)** | 94.6 → 🟠 ** 67.1** (`-27.5`) | `-27.5 pkt` | 6.56 Er | 1.9% | 10.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 7 kart (Pełna swoboda)** | 94.6 → 🔴 ** 56.0** (`-38.6`) | `-38.6 pkt` | 5.54 Er | 0.9% | 5.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé Inkwizytora: Cooldown 2 Ery (Częsta czystka)** | 94.6 → 🟠 ** 63.1** (`-31.5`) | `-31.5 pkt` | 5.68 Er | 0.7% | 5.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé Inkwizytora: Cooldown 4 Ery (Rzadka czystka)** | 94.6 → 🟠 ** 74.4** (`-20.2`) | `-20.2 pkt` | 6.11 Er | 1.6% | 5.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé Inkwizytora: Całkowity brak czystki** | 94.6 → 🔴 ** 31.6** (`-63.0`) | `-63.0 pkt` | 6.37 Er | 2.8% | 4.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)

| Badany Warunek Zwycięstwa L2 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: Wymóg Stosów +2** | 94.6 → 🔴 ** 54.1** (`-40.5`) | `-40.5 pkt` | 6.15 Er | 2.3% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: Wymóg Stosów -1** | 94.6 → 🔴 ** 56.3** (`-38.3`) | `-38.3 pkt` | 5.70 Er | 0.7% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: Wymóg Skazań +2 (Zamiast 2-3)** | 🟢 ** 94.6** | `0.0 pkt` | 5.94 Er | 1.1% | 5.6% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Święte Oficjum: Wymóg Skazań -1** | 94.6 → 🟡 ** 78.3** (`-16.3`) | `-16.3 pkt` | 5.79 Er | 0.8% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Cienie: Wymóg Relikwii 2 → 4** | 94.6 → 🔴 ** 33.6** (`-61.0`) | `-61.0 pkt` | 6.56 Er | 1.8% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Cienie: Wymóg Relikwii 2 → 1** | 94.6 → 🔴 ** 18.1** (`-76.5`) | `-76.5 pkt` | 4.04 Er | 0.2% | 5.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Cienie: Wymóg Ery 5 → Era 3 (Wczesna ucieczka)** | 94.6 → 🟢 ** 94.5** (`-0.1`) | `-0.1 pkt` | 5.91 Er | 1.1% | 5.5% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Cienie: Wymóg Ery 5 → Era 8 (Późna ucieczka)** | 94.6 → 🟢 ** 92.6** (`-2.0`) | `-2.0 pkt` | 6.01 Er | 1.1% | 5.6% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Korona: Wymóg Dekretów 2 → 3** | 94.6 → 🔴 ** 35.6** (`-59.0`) | `-59.0 pkt` | 6.36 Er | 2.7% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: Wymóg Dekretów 2 → 1** | 94.6 → 🔴 ** 20.5** (`-74.1`) | `-74.1 pkt` | 4.51 Er | 0.2% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: Brak wymogu Haków (0 Haków)** | 94.6 → 🟢 ** 94.5** (`-0.1`) | `-0.1 pkt` | 5.92 Er | 1.1% | 5.5% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Korona: Wymóg Haków +2** | 94.6 → 🔴 ** 39.4** (`-55.2`) | `-55.2 pkt` | 6.33 Er | 2.3% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: Wymóg Ery 5 → Era 3** | 🟢 ** 94.6** | `0.0 pkt` | 5.89 Er | 1.1% | 5.5% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Korona: Wymóg Ery 5 → Era 7** | 94.6 → 🟡 ** 89.7** (`-4.9`) | `-4.9 pkt` | 6.07 Er | 1.1% | 5.6% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Kabała: Wymóg Fragmentów 3 → 4** | 94.6 → 🔴 ** 58.1** (`-36.5`) | `-36.5 pkt` | 6.16 Er | 1.6% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: Wymóg Fragmentów 3 → 2** | 94.6 → 🔴 ** 58.8** (`-35.8`) | `-35.8 pkt` | 5.68 Er | 0.9% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: Wymóg Ery 6 → Era 4** | 94.6 → 🟡 ** 86.9** (`-7.7`) | `-7.7 pkt` | 5.79 Er | 1.1% | 5.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Kabała: Wymóg Ery 6 → Era 8** | 94.6 → 🟠 ** 70.1** (`-24.5`) | `-24.5 pkt` | 6.12 Er | 1.1% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: Próg Dolny Pasma 3 → 5 (Zawężenie od dołu)** | 94.6 → 🟢 ** 93.9** (`-0.7`) | `-0.7 pkt` | 5.95 Er | 1.1% | 5.5% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Kabała: Próg Dolny Pasma 3 → 1 (Rozszerzenie w dół)** | 🟢 ** 94.6** | `0.0 pkt` | 5.94 Er | 1.1% | 5.6% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Kabała: Próg Górny Pasma 9 → 7 (Zawężenie od góry)** | 94.6 → 🟡 ** 86.5** (`-8.1`) | `-8.1 pkt` | 5.99 Er | 1.3% | 5.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Kabała: Próg Górny Pasma 9 → 11 (Rozszerzenie w górę)** | 94.6 → 🟡 ** 88.8** (`-5.8`) | `-5.8 pkt` | 5.89 Er | 0.6% | 5.6% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Kabała: Całe Pasmo Wąskie (4–6)** | 94.6 → 🟠 ** 74.0** (`-20.6`) | `-20.6 pkt` | 6.05 Er | 1.5% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: Całe Pasmo Szerokie (2–9)** | 🟢 ** 94.6** | `0.0 pkt` | 5.94 Er | 1.1% | 5.6% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Gildia: Wymóg Upadków (z Oficjum) 2 → 3** | 94.6 → 🟠 ** 65.0** (`-29.6`) | `-29.6 pkt` | 6.17 Er | 1.3% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: Wymóg Upadków (z Oficjum) 2 → 1** | 94.6 → 🔴 ** 53.6** (`-41.0`) | `-41.0 pkt` | 5.50 Er | 0.8% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: Wymóg Upadków (bez Oficjum) 3 → 4** | 94.6 → 🟡 ** 89.0** (`-5.6`) | `-5.6 pkt` | 5.98 Er | 1.3% | 5.6% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Gildia: Wymóg Upadków (bez Oficjum) 3 → 2** | 94.6 → 🟢 ** 90.3** (`-4.3`) | `-4.3 pkt` | 5.87 Er | 1.0% | 5.6% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |

### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)

| Badany Wariant / Modyfikator L4 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kronika Dziejów: Całkowite wyłączenie edyktów czasu** | 94.6 → 🟠 ** 63.3** (`-31.3`) | `-31.3 pkt` | 6.20 Er | 1.9% | 6.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kronika Dziejów: Częstotliwość co 2 Ery** | 94.6 → 🟡 ** 78.4** (`-16.2`) | `-16.2 pkt` | 6.12 Er | 1.7% | 5.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Werdykt Sądu: Tajny (brak koordynacji anty-snowball)** | 94.6 → 🔴 ** 58.5** (`-36.1`) | `-36.1 pkt` | 5.50 Er | 0.4% | 5.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Szlak Morski: Odblokowanie w Erze 4 (Wczesne)** | 94.6 → 🟢 ** 93.2** (`-1.4`) | `-1.4 pkt` | 5.91 Er | 1.1% | 5.5% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Szlak Morski: Odblokowanie w Erze 6 (Późne)** | 🟢 ** 94.6** | `0.0 pkt` | 5.94 Er | 1.1% | 5.6% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Inkwizytor Patrol: Ruch 0 pól (Stacjonarny)** | 94.6 → 🟠 ** 64.8** (`-29.8`) | `-29.8 pkt` | 5.97 Er | 1.1% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Inkwizytor Patrol: Ruch 2 pola (Szybki patrol)** | 94.6 → 🟢 ** 93.2** (`-1.4`) | `-1.4 pkt` | 5.93 Er | 1.1% | 5.6% | 💤 MECHANIKA PASYWNA (Low Impact) |

---

## 5. 👥 Warstwa IV — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych w Kanonie 4P:

| Nieobecna Frakcja | Setup Testowy | 4P Score Setupu | Diagnoza Wpływu Braku Frakcji na Stół 4P |
| :--- | :--- | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`97.6 pkt`** | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`98.5 pkt`** | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`96.4 pkt`** | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`88.9 pkt`** | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`91.6 pkt`** | Brak presji stosów i bezpośredniego Inkwizytora |