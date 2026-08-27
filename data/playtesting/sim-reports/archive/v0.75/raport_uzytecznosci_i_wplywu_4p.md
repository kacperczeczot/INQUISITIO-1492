[Strona główna](../../../../../README.md) > [v0.75](README.md) > [raport_uzytecznosci_i_wplywu_4p](raport_uzytecznosci_i_wplywu_4p.md)

---

# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v0.75

**Wersja Gry:** `v0.75` | **Data Badania:** 2026-08-17 01:06 | **Próba:** 2000 gier/setup (10000 gier na wariant) | **Ziarno:** 42
**Wynik Bazowy Kanonu 4P:** 🔴 ** 35.1** pkt | **Średnia Długość Partii:** `5.53 Er` | **Deadlocki:** `1.2%` | **Pas Biedy:** `6.9%`

---

## 1. 🗺️ Podsumowanie Ekosystemu Kart Kanonu 4P (Matryca Wpływu Kart 3x3)

Rozkład wszystkich 50 kart frakcyjnych w matrycy **Wpływ na Frakcję ($\Delta \text{Share}$)** vs **Wpływ na Kanon 4P ($\Delta \text{4P Score}$)**:

| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |
| :--- | :---: | :---: | :--- | :--- |
| 👑 / ⚓ **Filar / Kotwica Kanonu** | **24** | 48% | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |
| ⚖️ **Zbalansowane Narzędzie** | **10** | 20% | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Optymalne** |
| 💤 **Karta Pasywna (Dead Weight)** | **1** | 2% | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia** |
| ⚠️ **Karta Destabilizująca (Disruptor)** | **15** | 30% | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |

---

## 2. 🃏 Warstwa I — Szczegółowa Analiza 50 Kart Frakcji w Kanonie 4P

### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)
Karty, których brak powoduje spadek wyniku Kanonu 4P o $\ge 4.0$ pkt lub załamanie winrate frakcji o $\ge 4.0\%$:

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kb-09` **Dekret Królewski** | Korona & Borgiowie | 3zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 14.7% → **1.6%** | **`-13.1%`** | 35.1 → **19.9 pkt** (`-15.2`) |
| `kb-10` **Pieczęć Korony** | Korona & Borgiowie | 2zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 14.7% → **2.6%** | **`-12.1%`** | 35.1 → **21.4 pkt** (`-13.7`) |
| `caa-09` **Kurier Relikwii** | Cienie Al-Andalus | 2zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 34.5% → **44.6%** | **`+10.1%`** | 35.1 → **24.6 pkt** (`-10.5`) |
| `kb-02` **Pobór Podatków** | Korona & Borgiowie | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 14.7% → **5.9%** | **`-8.8%`** | 35.1 → **24.6 pkt** (`-10.5`) |
| `caa-07` **Szantaż Bractwa** | Cienie Al-Andalus | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 34.5% → **42.3%** | **`+7.8%`** | 35.1 → **27.2 pkt** (`-7.9`) |
| `caa-02` **Złoto z Kryjówki** | Cienie Al-Andalus | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 34.5% → **42.3%** | **`+7.8%`** | 35.1 → **27.3 pkt** (`-7.8`) |
| `caa-04` **Fałszywy Trop** | Cienie Al-Andalus | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 34.5% → **42.2%** | **`+7.7%`** | 35.1 → **27.4 pkt** (`-7.7`) |
| `caa-08` **Kaptur Nocy** | Cienie Al-Andalus | 2zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 34.5% → **42.7%** | **`+8.2%`** | 35.1 → **27.6 pkt** (`-7.5`) |
| `kb-01` **Rozkaz Dworu** | Korona & Borgiowie | 1zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 14.7% → **9.3%** | **`-5.4%`** | 35.1 → **28.0 pkt** (`-7.1`) |
| `kt-03` **Zakazana Wiedza** | Kabała z Toledo | 0zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 31.0% → **39.0%** | **`+8.0%`** | 35.1 → **28.8 pkt** (`-6.3`) |
| `gc-04` **Informator** | Gildia Cieni | 0zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 33.6% → **37.6%** | **`+4.0%`** | 35.1 → **29.0 pkt** (`-6.1`) |
| `kb-03` **Plotka Dworska** | Korona & Borgiowie | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 14.7% → **10.4%** | **`-4.3%`** | 35.1 → **29.2 pkt** (`-5.9`) |
| `kb-06` **Areszt Królewski** | Korona & Borgiowie | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 14.7% → **10.4%** | **`-4.3%`** | 35.1 → **30.1 pkt** (`-5.0`) |
| `gc-02` **Czarny Rynek** | Gildia Cieni | 1zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 33.6% → **37.3%** | **`+3.7%`** | 35.1 → **30.7 pkt** (`-4.4`) |
| `kt-07` **Archiwum Ukryte** | Kabała z Toledo | 1zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 31.0% → **38.2%** | **`+7.2%`** | 35.1 → **30.8 pkt** (`-4.3`) |
| `gc-01` **Przekupiony Strażnik** | Gildia Cieni | 1zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 33.6% → **37.0%** | **`+3.4%`** | 35.1 → **31.0 pkt** (`-4.1`) |
| `gc-07` **Skrytobójstwo** | Gildia Cieni | 2zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 33.6% → **38.0%** | **`+4.4%`** | 35.1 → **31.3 pkt** (`-3.8`) |
| `kt-01` **Rytuał Przejścia** | Kabała z Toledo | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 31.0% → **37.5%** | **`+6.5%`** | 35.1 → **31.4 pkt** (`-3.7`) |
| `kt-04` **Zwierciadło Herezji** | Kabała z Toledo | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 31.0% → **37.1%** | **`+6.1%`** | 35.1 → **31.4 pkt** (`-3.7`) |
| `kt-02` **Transmutacja Złota** | Kabała z Toledo | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 31.0% → **37.1%** | **`+6.1%`** | 35.1 → **31.5 pkt** (`-3.6`) |
| `gc-05` **Fałszywy Świadek** | Gildia Cieni | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 33.6% → **35.2%** | **`+1.6%`** | 35.1 → **31.8 pkt** (`-3.3`) |
| `kt-10` **Pieczęć Salomona** | Kabała z Toledo | 2zł / 1☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 31.0% → **35.2%** | **`+4.2%`** | 35.1 → **32.6 pkt** (`-2.5`) |
| `kt-08` **Areszt Wiedzy** | Kabała z Toledo | 1zł / 0☣ | 🛡️ TARCZA DEFENSYWNA (Faction Shield) | 31.0% → **35.1%** | **`+4.1%`** | 35.1 → **33.1 pkt** (`-2.0`) |
| `kt-05` **Wskazówka Cyklu** | Kabała z Toledo | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 31.0% → **15.3%** | **`-15.7%`** | 35.1 → **34.2 pkt** (`-0.9`) |

### 2.2. ⚠️ Karty Destabilizujące Kanon 4P (Disruptors)
Karty, których wyłączenie podnosi 4P Score ($\Delta \text{4P} \ge +1.5$ pkt):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kb-04` **Faworyt Dworu** | Korona & Borgiowie | 2zł / 1☣ | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) | 14.7% → **26.9%** | `+12.2%` | 35.1 → **47.2 pkt** (`+12.1`) |
| `kb-05` **List Żelazny** | Korona & Borgiowie | 2zł / 0☣ | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) | 14.7% → **27.4%** | `+12.7%` | 35.1 → **46.4 pkt** (`+11.3`) |
| `caa-06` **Ucieczka z Lochów** | Cienie Al-Andalus | 2zł / 1☣ | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) | 34.5% → **31.1%** | `-3.4%` | 35.1 → **39.0 pkt** (`+3.9`) |
| `caa-05` **Ukryty Kurier** | Cienie Al-Andalus | 1zł / 0☣ | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) | 34.5% → **26.1%** | `-8.4%` | 35.1 → **38.7 pkt** (`+3.6`) |
| `kb-07` **Szantaż Pieczęcią** | Korona & Borgiowie | 2zł / 0☣ | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) | 14.7% → **18.2%** | `+3.5%` | 35.1 → **38.6 pkt** (`+3.5`) |
| `kb-08` **Przekupstwo Sędziego** | Korona & Borgiowie | 2zł / 0☣ | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) | 14.7% → **18.2%** | `+3.5%` | 35.1 → **38.6 pkt** (`+3.5`) |
| `gc-06` **Szantaż** | Gildia Cieni | 2zł / 0☣ | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) | 33.6% → **21.7%** | `-11.9%` | 35.1 → **37.8 pkt** (`+2.7`) |
| `caa-03` **Cień na Rynku** | Cienie Al-Andalus | 0zł / 1☣ | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) | 34.5% → **33.4%** | `-1.1%` | 35.1 → **37.7 pkt** (`+2.6`) |
| `so-06` **Areszt Trybunalski** | Święte Oficjum | 2zł / 0☣ | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) | 11.1% → **13.2%** | `+2.1%` | 35.1 → **37.7 pkt** (`+2.6`) |
| `gc-09` **Lista Dłużników** | Gildia Cieni | 2zł / 0☣ | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) | 33.6% → **21.4%** | `-12.2%` | 35.1 → **37.1 pkt** (`+2.0`) |
| `gc-10` **Upadek Domu** | Gildia Cieni | 4zł / 1☣ | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) | 33.6% → **30.9%** | `-2.7%` | 35.1 → **36.9 pkt** (`+1.8`) |
| `so-04` **Publiczne Ostrzeżenie** | Święte Oficjum | 1zł / 0☣ | ⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor) | 11.1% → **11.8%** | `+0.7%` | 35.1 → **36.9 pkt** (`+1.8`) |
| `so-07` **Przesłuchanie Oficjum** | Święte Oficjum | 2zł / 0☣ | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) | 11.1% → **12.0%** | `+0.9%` | 35.1 → **36.7 pkt** (`+1.6`) |
| `so-08` **Nasłanie Inkwizytora** | Święte Oficjum | 1zł / 0☣ | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) | 11.1% → **12.2%** | `+1.1%` | 35.1 → **36.4 pkt** (`+1.3`) |
| `so-02` **Skarbiec Trybunału** | Święte Oficjum | 1zł / 0☣ | ⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor) | 11.1% → **11.8%** | `+0.7%` | 35.1 → **36.3 pkt** (`+1.2`) |

### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich 50 Kart Frakcji w Kanonie 4P

| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Faction Win Share 4P | $\Delta$ Frakcji | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `caa-01` | **Przejście Podziemiami** | Cienie Al-Andalus | 0 | 0 | 34.5% → 35.0% | `+0.5%` | 36.2 | `+1.1` | 5.50 | 1.2% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-03` | **Cień na Rynku** | Cienie Al-Andalus | 0 | 1 | 34.5% → 33.4% | `-1.1%` | 37.7 | `+2.6` | 5.75 | 1.6% | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) |
| `caa-02` | **Złoto z Kryjówki** | Cienie Al-Andalus | 1 | 0 | 34.5% → 42.3% | `+7.8%` | 27.3 | `-7.8` | 5.32 | 1.0% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `caa-04` | **Fałszywy Trop** | Cienie Al-Andalus | 1 | 0 | 34.5% → 42.2% | `+7.7%` | 27.4 | `-7.7` | 5.36 | 1.0% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `caa-05` | **Ukryty Kurier** | Cienie Al-Andalus | 1 | 0 | 34.5% → 26.1% | `-8.4%` | 38.7 | `+3.6` | 5.62 | 1.1% | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) |
| `caa-07` | **Szantaż Bractwa** | Cienie Al-Andalus | 1 | 0 | 34.5% → 42.3% | `+7.8%` | 27.2 | `-7.9` | 5.30 | 1.0% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `caa-06` | **Ucieczka z Lochów** | Cienie Al-Andalus | 2 | 1 | 34.5% → 31.1% | `-3.4%` | 39.0 | `+3.9` | 5.55 | 1.7% | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) |
| `caa-08` | **Kaptur Nocy** | Cienie Al-Andalus | 2 | 1 | 34.5% → 42.7% | `+8.2%` | 27.6 | `-7.5` | 5.32 | 1.0% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `caa-10` | **Echo Alhambry** | Cienie Al-Andalus | 1 | 1 | 34.5% → 33.0% | `-1.5%` | 35.2 | `+0.1` | 5.78 | 1.6% | ⚡ MOTOR FRAKCJI (Offensive Engine) |
| `caa-09` | **Kurier Relikwii** | Cienie Al-Andalus | 2 | 0 | 34.5% → 44.6% | `+10.1%` | 24.6 | `-10.5` | 5.30 | 1.0% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `gc-04` | **Informator** | Gildia Cieni | 0 | 1 | 33.6% → 37.6% | `+4.0%` | 29.0 | `-6.1` | 5.42 | 0.7% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `gc-05` | **Fałszywy Świadek** | Gildia Cieni | 0 | 0 | 33.6% → 35.2% | `+1.6%` | 31.8 | `-3.3` | 5.47 | 0.9% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-01` | **Przekupiony Strażnik** | Gildia Cieni | 1 | 1 | 33.6% → 37.0% | `+3.4%` | 31.0 | `-4.1` | 5.43 | 1.0% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `gc-02` | **Czarny Rynek** | Gildia Cieni | 1 | 1 | 33.6% → 37.3% | `+3.7%` | 30.7 | `-4.4` | 5.49 | 0.9% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `gc-03` | **Podrzucenie Księgi** | Gildia Cieni | 1 | 0 | 33.6% → 34.5% | `+0.9%` | 33.2 | `-1.9` | 5.49 | 1.2% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-06` | **Szantaż** | Gildia Cieni | 2 | 0 | 33.6% → 21.7% | `-11.9%` | 37.8 | `+2.7` | 5.76 | 1.5% | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) |
| `gc-07` | **Skrytobójstwo** | Gildia Cieni | 2 | 0 | 33.6% → 38.0% | `+4.4%` | 31.3 | `-3.8` | 5.40 | 0.9% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `gc-08` | **Zatrute Złoto** | Gildia Cieni | 2 | 0 | 33.6% → 34.8% | `+1.2%` | 33.3 | `-1.8` | 5.46 | 1.1% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `gc-09` | **Lista Dłużników** | Gildia Cieni | 2 | 0 | 33.6% → 21.4% | `-12.2%` | 37.1 | `+2.0` | 5.74 | 1.8% | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) |
| `gc-10` | **Upadek Domu** | Gildia Cieni | 4 | 1 | 33.6% → 30.9% | `-2.7%` | 36.9 | `+1.8` | 5.59 | 1.4% | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) |
| `kb-01` | **Rozkaz Dworu** | Korona & Borgiowie | 1 | 1 | 14.7% → 9.3% | `-5.4%` | 28.0 | `-7.1` | 5.60 | 1.4% | 👑 FILAR KANONU (Core Keystone) |
| `kb-02` | **Pobór Podatków** | Korona & Borgiowie | 1 | 0 | 14.7% → 5.9% | `-8.8%` | 24.6 | `-10.5` | 5.68 | 1.8% | 👑 FILAR KANONU (Core Keystone) |
| `kb-03` | **Plotka Dworska** | Korona & Borgiowie | 1 | 0 | 14.7% → 10.4% | `-4.3%` | 29.2 | `-5.9` | 5.59 | 1.4% | 👑 FILAR KANONU (Core Keystone) |
| `kb-04` | **Faworyt Dworu** | Korona & Borgiowie | 2 | 1 | 14.7% → 26.9% | `+12.2%` | 47.2 | `+12.1` | 5.31 | 0.9% | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) |
| `kb-05` | **List Żelazny** | Korona & Borgiowie | 2 | 0 | 14.7% → 27.4% | `+12.7%` | 46.4 | `+11.3` | 5.21 | 0.6% | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) |
| `kb-06` | **Areszt Królewski** | Korona & Borgiowie | 1 | 0 | 14.7% → 10.4% | `-4.3%` | 30.1 | `-5.0` | 5.56 | 1.3% | 👑 FILAR KANONU (Core Keystone) |
| `kb-07` | **Szantaż Pieczęcią** | Korona & Borgiowie | 2 | 0 | 14.7% → 18.2% | `+3.5%` | 38.6 | `+3.5` | 5.43 | 0.8% | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) |
| `kb-08` | **Przekupstwo Sędziego** | Korona & Borgiowie | 2 | 0 | 14.7% → 18.2% | `+3.5%` | 38.6 | `+3.5` | 5.43 | 0.8% | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) |
| `kb-10` | **Pieczęć Korony** | Korona & Borgiowie | 2 | 2 | 14.7% → 2.6% | `-12.1%` | 21.4 | `-13.7` | 5.83 | 1.7% | 👑 FILAR KANONU (Core Keystone) |
| `kb-09` | **Dekret Królewski** | Korona & Borgiowie | 3 | 1 | 14.7% → 1.6% | `-13.1%` | 19.9 | `-15.2` | 5.72 | 1.7% | 👑 FILAR KANONU (Core Keystone) |
| `kt-03` | **Zakazana Wiedza** | Kabała z Toledo | 0 | 1 | 31.0% → 39.0% | `+8.0%` | 28.8 | `-6.3` | 5.45 | 0.9% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-01` | **Rytuał Przejścia** | Kabała z Toledo | 1 | 0 | 31.0% → 37.5% | `+6.5%` | 31.4 | `-3.7` | 5.39 | 1.1% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-02` | **Transmutacja Złota** | Kabała z Toledo | 1 | 0 | 31.0% → 37.1% | `+6.1%` | 31.5 | `-3.6` | 5.42 | 1.0% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-04` | **Zwierciadło Herezji** | Kabała z Toledo | 1 | 0 | 31.0% → 37.1% | `+6.1%` | 31.4 | `-3.7` | 5.40 | 1.0% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-05` | **Wskazówka Cyklu** | Kabała z Toledo | 1 | 0 | 31.0% → 15.3% | `-15.7%` | 34.2 | `-0.9` | 5.73 | 2.3% | 👑 FILAR KANONU (Core Keystone) |
| `kt-07` | **Archiwum Ukryte** | Kabała z Toledo | 1 | 1 | 31.0% → 38.2% | `+7.2%` | 30.8 | `-4.3` | 5.36 | 0.9% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-08` | **Areszt Wiedzy** | Kabała z Toledo | 1 | 0 | 31.0% → 35.1% | `+4.1%` | 33.1 | `-2.0` | 5.38 | 1.1% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `kt-06` | **Przesłuchanie Imienia** | Kabała z Toledo | 2 | 0 | 31.0% → 33.2% | `+2.2%` | 34.7 | `-0.4` | 5.44 | 1.5% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `kt-09` | **Fragment Kodeksu** | Kabała z Toledo | 2 | 1 | 31.0% → 33.0% | `+2.0%` | 35.6 | `+0.5` | 5.48 | 1.4% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `kt-10` | **Pieczęć Salomona** | Kabała z Toledo | 2 | 1 | 31.0% → 35.2% | `+4.2%` | 32.6 | `-2.5` | 5.50 | 1.1% | 🛡️ TARCZA DEFENSYWNA (Faction Shield) |
| `so-05` | **Wezwanie do Trybunału** | Święte Oficjum | 0 | 0 | 11.1% → 10.7% | `-0.4%` | 34.3 | `-0.8` | 5.56 | 1.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-01` | **Patrol Familiariuszy** | Święte Oficjum | 1 | 0 | 11.1% → 11.6% | `+0.5%` | 35.6 | `+0.5` | 5.53 | 1.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-02` | **Skarbiec Trybunału** | Święte Oficjum | 1 | 0 | 11.1% → 11.8% | `+0.7%` | 36.3 | `+1.2` | 5.53 | 0.9% | ⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor) |
| `so-04` | **Publiczne Ostrzeżenie** | Święte Oficjum | 1 | 0 | 11.1% → 11.8% | `+0.7%` | 36.9 | `+1.8` | 5.53 | 1.0% | ⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor) |
| `so-03` | **Podejrzenie** | Święte Oficjum | 2 | 0 | 11.1% → 10.8% | `-0.3%` | 35.4 | `+0.3` | 5.55 | 0.9% | 💤 KARTA NISKIEGO WPŁYWU (Passive) |
| `so-08` | **Nasłanie Inkwizytora** | Święte Oficjum | 1 | 0 | 11.1% → 12.2% | `+1.1%` | 36.4 | `+1.3` | 5.53 | 1.2% | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) |
| `so-06` | **Areszt Trybunalski** | Święte Oficjum | 2 | 0 | 11.1% → 13.2% | `+2.1%` | 37.7 | `+2.6` | 5.51 | 1.0% | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) |
| `so-07` | **Przesłuchanie Oficjum** | Święte Oficjum | 2 | 0 | 11.1% → 12.0% | `+0.9%` | 36.7 | `+1.6` | 5.52 | 1.1% | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) |
| `so-09` | **Świadek Koronny** | Święte Oficjum | 2 | 0 | 11.1% → 11.4% | `+0.3%` | 35.6 | `+0.5` | 5.50 | 0.9% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-10` | **Oczyść Miasto** | Święte Oficjum | 5 | 2 | 11.1% → 12.2% | `+1.1%` | 35.5 | `+0.4` | 5.52 | 1.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |

---

## 3. ⏳ Warstwa II — Kronika Dziejów w 4P (Ablacja 8 Kart Wydarzeń Czasu)

Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans w 4P:

| ID | Karta Wydarzenia | 4P Score | $\Delta$ 4P | Średnia Er | Deadlock % | Status Roli w Kronice |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `tc-01` | **Kres Średniowiecza** | 🔴 ** 35.1** | `0.0 pkt` | 5.53 Er | 1.2% | ⚖️ Neutralna Kronika |
| `tc-02` | **Płonący Stos** | 🔴 ** 35.1** | `0.0 pkt` | 5.53 Er | 1.2% | ⚖️ Neutralna Kronika |
| `tc-03` | **Królewski Podatek** | 🔴 ** 35.1** | `0.0 pkt` | 5.53 Er | 1.2% | ⚖️ Neutralna Kronika |
| `tc-04` | **Spisek w Cieniu** | 🔴 ** 35.1** | `0.0 pkt` | 5.53 Er | 1.2% | ⚖️ Neutralna Kronika |
| `tc-05` | **Złoty Wiek** | 🔴 ** 35.1** | `0.0 pkt` | 5.53 Er | 1.2% | ⚖️ Neutralna Kronika |
| `tc-06` | **Czystka w Mieście** | 🔴 ** 35.1** | `0.0 pkt` | 5.53 Er | 1.2% | ⚖️ Neutralna Kronika |
| `tc-07` | **Druga Szansa** | 🔴 ** 35.1** | `0.0 pkt` | 5.53 Er | 1.2% | ⚖️ Neutralna Kronika |
| `tc-08` | **Zaćmienie Słońca** | 🔴 ** 35.1** | `0.0 pkt` | 5.53 Er | 1.2% | ⚖️ Neutralna Kronika |

---

## 4. ⚙️ Warstwa III — Matryca 9 Obszarów Wpływu Mechanik Gry (L1, L2, L4)

Zestawienie odporności Kanonu 4P na modyfikacje i ablację poszczególnych podsystemów według 9 obszarów istotności i efektu:

| Kategoria Mechaniki | Liczba Testów | Rola w Ekosystemie Kanonu 4P | Rekomendacja Balansowa |
| :--- | :---: | :--- | :--- |
| 👑 / 🛡️ **Filary i Bezpieczniki Stabilizujące** | **18** | Mechaniki krytyczne — ich brak lub rozregulowanie niszczy balans | **Nienaruszalny Kanon** |
| ⚖️ **Zbalansowane Regulatory / Pasywne** | **24** | Mechaniki harmonijnie wpisane w dynamikę rozgrywki | **Optymalne w Kanonie** |
| ⚠️ / 💡 **Obciążenia i Kandydaci do Uproszczenia** | **6** | Mechaniki, których modyfikacja lub redukcja podnosi wynik 4P | **Kandydaci do optymalizacji** |

### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)

| Badany Podsystem / Modyfikator L1 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Limit Er: 12 → 8 Er (Presja czasu)** | 35.1 → 🔴 ** 29.6** (`-5.5`) | `-5.5 pkt` | 5.38 Er | 11.5% | 7.0% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Limit Er: 12 → 16 Er (Wydłużony silnik)** | 35.1 → 🔴 ** 34.8** (`-0.3`) | `-0.3 pkt` | 5.54 Er | 0.1% | 6.9% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Próg Oskarżenia na Dworze: -1 (Agresywny Dwór)** | 35.1 → 🔴 ** 34.0** (`-1.1`) | `-1.1 pkt` | 5.52 Er | 1.2% | 6.5% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Próg Oskarżenia na Dworze: +1 (Pasywny Dwór)** | 35.1 → 🔴 ** 36.8** (`⬆️ +1.7`) | `+1.7 pkt` | 5.55 Er | 1.1% | 7.2% | ⚠️ UMIARKOWANE OBCIĄŻENIE (Moderate Drag) |
| **Złoto startowe: 4zł → 0zł (Skrajne ubóstwo)** | 35.1 → 🔴 ** 15.3** (`-19.8`) | `-19.8 pkt` | 6.37 Er | 2.4% | 24.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 6zł (Bogaty start)** | 35.1 → 🔴 ** 36.9** (`⬆️ +1.8`) | `+1.8 pkt` | 5.03 Er | 0.5% | 4.6% | ⚠️ KRYTYCZNA WADA (Critical Flaw) |
| **Liczba Agentów: 3 → 2 Agentów (Ograniczony zasięg)** | 35.1 → 🔴 ** 35.7** (`⬆️ +0.6`) | `+0.6 pkt` | 5.69 Er | 2.3% | 7.2% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Liczba Agentów: 3 → 4 Agentów (Gęsta plansza)** | 35.1 → 🔴 ** 31.5** (`-3.6`) | `-3.6 pkt` | 5.43 Er | 0.9% | 6.8% | ⚖️ ZBALANSOWANY REGULATOR (Balanced Regulator) |
| **Limit kart na ręce: 5 → 3 karty (Zmniejszona elastyczność)** | 35.1 → 🔴 ** 55.6** (`⬆️ +20.5`) | `+20.5 pkt` | 6.20 Er | 1.6% | 9.9% | ⚠️ KRYTYCZNA WADA (Critical Flaw) |
| **Limit kart na ręce: 5 → 7 kart (Pełna swoboda)** | 35.1 → 🔴 ** 16.6** (`-18.5`) | `-18.5 pkt` | 4.96 Er | 0.6% | 7.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé Inkwizytora: Cooldown 2 Ery (Częsta czystka)** | 35.1 → 🔴 ** 35.3** (`⬆️ +0.2`) | `+0.2 pkt` | 5.31 Er | 0.7% | 7.3% | ⚖️ ZBALANSOWANY REGULATOR (Balanced Regulator) |
| **Autodafé Inkwizytora: Cooldown 4 Ery (Rzadka czystka)** | 35.1 → 🔴 ** 31.2** (`-3.9`) | `-3.9 pkt` | 5.66 Er | 1.7% | 6.6% | ⚖️ ZBALANSOWANY REGULATOR (Balanced Regulator) |
| **Autodafé Inkwizytora: Całkowity brak czystki** | 35.1 → 🔴 ** 20.5** (`-14.6`) | `-14.6 pkt` | 5.90 Er | 3.1% | 5.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)

| Badany Warunek Zwycięstwa L2 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: Wymóg Stosów +2** | 35.1 → 🔴 ** 26.3** (`-8.8`) | `-8.8 pkt` | 5.61 Er | 2.0% | 6.9% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Święte Oficjum: Wymóg Stosów -1** | 35.1 → 🔴 ** 48.9** (`⬆️ +13.8`) | `+13.8 pkt` | 5.42 Er | 0.7% | 6.9% | ⚠️ UMIARKOWANE OBCIĄŻENIE (Moderate Drag) |
| **Święte Oficjum: Wymóg Skazań +2 (Zamiast 2-3)** | 🔴 ** 35.1** | `0.0 pkt` | 5.53 Er | 1.2% | 6.9% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Święte Oficjum: Wymóg Skazań -1** | 35.1 → 🔴 ** 41.7** (`⬆️ +6.6`) | `+6.6 pkt` | 5.45 Er | 0.9% | 6.9% | ⚠️ UMIARKOWANE OBCIĄŻENIE (Moderate Drag) |
| **Cienie: Wymóg Relikwii 2 → 4** | 35.1 → 🔴 ** 14.2** (`-20.9`) | `-20.9 pkt` | 6.32 Er | 2.3% | 7.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Cienie: Wymóg Relikwii 2 → 1** | 35.1 → 🔴 **  5.5** (`-29.6`) | `-29.6 pkt` | 3.89 Er | 0.3% | 6.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Cienie: Wymóg Ery 5 → Era 3 (Wczesna ucieczka)** | 35.1 → 🔴 ** 35.0** (`-0.1`) | `-0.1 pkt` | 5.49 Er | 1.2% | 6.9% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Cienie: Wymóg Ery 5 → Era 8 (Późna ucieczka)** | 35.1 → 🔴 ** 36.4** (`⬆️ +1.3`) | `+1.3 pkt` | 5.62 Er | 1.2% | 6.9% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Korona: Wymóg Dekretów 2 → 3** | 35.1 → 🔴 ** 19.4** (`-15.7`) | `-15.7 pkt` | 5.75 Er | 1.9% | 6.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: Wymóg Dekretów 2 → 1** | 35.1 → 🔴 **  9.4** (`-25.7`) | `-25.7 pkt` | 4.31 Er | 0.1% | 6.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: Brak wymogu Haków (0 Haków)** | 35.1 → 🔴 ** 36.2** (`⬆️ +1.1`) | `+1.1 pkt` | 5.50 Er | 1.2% | 6.9% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Korona: Wymóg Haków +2** | 35.1 → 🔴 ** 19.8** (`-15.3`) | `-15.3 pkt` | 5.75 Er | 1.8% | 6.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: Wymóg Ery 5 → Era 3** | 35.1 → 🔴 ** 35.9** (`⬆️ +0.8`) | `+0.8 pkt` | 5.50 Er | 1.2% | 6.9% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Korona: Wymóg Ery 5 → Era 7** | 35.1 → 🔴 ** 31.8** (`-3.3`) | `-3.3 pkt` | 5.62 Er | 1.2% | 6.9% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Kabała: Wymóg Fragmentów 3 → 4** | 35.1 → 🔴 ** 33.4** (`-1.7`) | `-1.7 pkt` | 5.74 Er | 1.6% | 6.9% | ⚓ KLUCZOWY STABILIZATOR (Key Anchor) |
| **Kabała: Wymóg Fragmentów 3 → 2** | 35.1 → 🔴 ** 30.6** (`-4.5`) | `-4.5 pkt` | 5.38 Er | 1.0% | 6.9% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Kabała: Wymóg Ery 6 → Era 4** | 35.1 → 🔴 ** 32.5** (`-2.6`) | `-2.6 pkt` | 5.30 Er | 1.2% | 6.8% | ⚖️ ZBALANSOWANY REGULATOR (Balanced Regulator) |
| **Kabała: Wymóg Ery 6 → Era 8** | 35.1 → 🔴 ** 30.2** (`-4.9`) | `-4.9 pkt` | 5.80 Er | 1.2% | 6.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: Próg Dolny Pasma 3 → 5 (Zawężenie od dołu)** | 35.1 → 🔴 ** 35.2** (`⬆️ +0.1`) | `+0.1 pkt` | 5.53 Er | 1.2% | 6.9% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Kabała: Próg Dolny Pasma 3 → 1 (Rozszerzenie w dół)** | 🔴 ** 35.1** | `0.0 pkt` | 5.53 Er | 1.2% | 6.9% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Kabała: Próg Górny Pasma 8 → 6 (Zawężenie od góry)** | 35.1 → 🔴 ** 36.0** (`⬆️ +0.9`) | `+0.9 pkt` | 5.64 Er | 1.5% | 6.9% | ⚖️ ZBALANSOWANY REGULATOR (Balanced Regulator) |
| **Kabała: Próg Górny Pasma 8 → 10 (Rozszerzenie w górę)** | 35.1 → 🔴 ** 30.3** (`-4.8`) | `-4.8 pkt` | 5.45 Er | 0.7% | 6.9% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Kabała: Całe Pasmo Wąskie (4–6)** | 35.1 → 🔴 ** 36.0** (`⬆️ +0.9`) | `+0.9 pkt` | 5.64 Er | 1.5% | 6.9% | ⚖️ ZBALANSOWANY REGULATOR (Balanced Regulator) |
| **Kabała: Całe Pasmo Szerokie (2–9)** | 35.1 → 🔴 ** 33.8** (`-1.3`) | `-1.3 pkt` | 5.50 Er | 1.1% | 6.9% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Gildia: Wymóg Upadków (z Oficjum) 2 → 3** | 35.1 → 🔴 ** 35.9** (`⬆️ +0.8`) | `+0.8 pkt` | 5.81 Er | 1.6% | 6.9% | ⚓ KLUCZOWY STABILIZATOR (Key Anchor) |
| **Gildia: Wymóg Upadków (z Oficjum) 2 → 1** | 35.1 → 🔴 ** 22.6** (`-12.5`) | `-12.5 pkt` | 5.08 Er | 0.7% | 6.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: Wymóg Upadków (bez Oficjum) 3 → 4** | 35.1 → 🔴 ** 35.4** (`⬆️ +0.3`) | `+0.3 pkt` | 5.59 Er | 1.3% | 6.9% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Gildia: Wymóg Upadków (bez Oficjum) 3 → 2** | 35.1 → 🔴 ** 30.4** (`-4.7`) | `-4.7 pkt` | 5.44 Er | 1.1% | 6.9% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |

### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)

| Badany Wariant / Modyfikator L4 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kronika Dziejów: Całkowite wyłączenie edyktów czasu** | 35.1 → 🔴 ** 27.8** (`-7.3`) | `-7.3 pkt` | 5.67 Er | 1.5% | 7.7% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Kronika Dziejów: Częstotliwość co 2 Ery** | 35.1 → 🔴 ** 31.1** (`-4.0`) | `-4.0 pkt` | 5.63 Er | 1.4% | 7.2% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Werdykt Sądu: Tajny (brak koordynacji anty-snowball)** | 35.1 → 🔴 ** 43.0** (`⬆️ +7.9`) | `+7.9 pkt` | 5.22 Er | 0.3% | 6.9% | ⚠️ UMIARKOWANE OBCIĄŻENIE (Moderate Drag) |
| **Szlak Morski: Odblokowanie w Erze 4 (Wczesne)** | 35.1 → 🔴 ** 34.4** (`-0.7`) | `-0.7 pkt` | 5.50 Er | 1.2% | 6.9% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Szlak Morski: Odblokowanie w Erze 6 (Późne)** | 🔴 ** 35.1** | `0.0 pkt` | 5.53 Er | 1.2% | 6.9% | 💤 MECHANIKA PASYWNA (Low Impact) |
| **Inkwizytor Patrol: Ruch 0 pól (Stacjonarny)** | 35.1 → 🔴 ** 27.9** (`-7.2`) | `-7.2 pkt` | 5.47 Er | 0.9% | 6.9% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Inkwizytor Patrol: Ruch 2 pola (Szybki patrol)** | 35.1 → 🔴 ** 36.2** (`⬆️ +1.1`) | `+1.1 pkt` | 5.50 Er | 1.0% | 6.9% | 💤 MECHANIKA PASYWNA (Low Impact) |

---

## 5. 👥 Warstwa IV — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych w Kanonie 4P:

| Nieobecna Frakcja | Setup Testowy | 4P Score Setupu | Diagnoza Wpływu Braku Frakcji na Stół 4P |
| :--- | :--- | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`31.0 pkt`** | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`32.0 pkt`** | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`38.1 pkt`** | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`26.4 pkt`** | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`47.9 pkt`** | Brak presji stosów i bezpośredniego Inkwizytora |