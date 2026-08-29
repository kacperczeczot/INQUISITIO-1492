# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v1.0-alpha.100

**Wersja Gry:** `v1.0-alpha.100` | **Data Badania:** 2026-08-29 23:26 | **Próba:** 10000 gier/setup (50000 gier na wariant) | **Ziarno:** 42
**4P Score (win share):** 🟡 ** 89.5** pkt | **Witalność (osobna kara):** `0.000` | **Śr. Er:** `5.85` | **Deadlocki:** `0.0%` | **Pas Biedy:** `4.2%`
**Udziały 4P:** CAA 24.5% · GC 25.5% · KB 26.0% · KT 25.8% · SO 23.3%

Klasyfikacja L1/L2/L4 i Δ 4P liczą wyłącznie równość win share (`calculate_balance_score`). Kara witalności jest osobno.

---

## 0. Wady z tej próby (nie HUD win share)

Kubełki klasyfikatora i ostrzeżenia witalności z bieżącego runu.

- **Autopodatek (SELF_HARM):** 2/60
- **DEAD_WEIGHT:** `gc-05` Fałszywy Świadek, `gc-08` Zatrute Złoto, `so-05` Wezwanie do Trybunału, `so-09` Świadek Koronny
- **Karty Kroniki |Δ4P| ≤ 0.8:** 3/10
- **Ablacja całej Kroniki (`L4_NO_TIME_DECK`):** Δ4P -22.4 (STABILIZER)
- **Mechaniki WEAK/NEUTRAL:** Inkwizytor Patrol: ruch x2 (podwojona prędkość); Szlak Morski: era 4 → nigdy (99)

---

## 1. 🗺️ Podsumowanie Ekosystemu Kart Kanonu 4P (Matryca Wpływu Kart, 60 kart)

Rozkład wszystkich 60 kart frakcyjnych w matrycy **Wpływ na Frakcję ($\Delta \text{Share}$)** vs **Wpływ na Kanon 4P ($\Delta \text{4P Score}$)**:

| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |
| :--- | :---: | :---: | :--- | :--- |
| 🩸 **Autopodatek (Self-Harm)** | **2** | 3.3% | Wyłączenie **podnosi** win share własnej frakcji — karta jest haraczem, nie silnikiem | **Rework / osłabienie kosztu, nie filar** |
| 🔄 **Rozcieńczalnik Talii (Tempo Filler)** | **5** | 8.3% | Normalna karta tempa — ablacja fałszywie flaguje ją jako autopodatek z powodu odchudzenia talii | **Normalny element deckbuildingu** |
| 💤 **Karta Pasywna (Dead Weight)** | **4** | 6.7% | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia lub wycięcia** |
| ⚠️ **Karta Destabilizująca (Disruptor)** | **1** | 1.7% | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |
| ⚖️ **Zbalansowane Narzędzie** | **23** | 38.3% | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Narzędzie, nie złoty środek całego kanonu** |
| 👑 / ⚓ **Filar / Kotwica Kanonu** | **25** | 41.7% | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |

---

## 2. 🃏 Warstwa I — Szczegółowa Analiza 60 Kart Frakcji w Kanonie 4P

### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)
Karty, których brak powoduje spadek wyniku Kanonu 4P o $\ge 4.0$ pkt lub załamanie winrate frakcji o $\ge 4.0\%$ — **bez** autopodatków (te są w 2.1b):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kt-10` **Pieczęć Salomona** | Kabała z Toledo | 4zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.8% → **0.0%** | **`-25.8%`** | 89.5 → **32.7 pkt** (`-56.8`) |
| `kb-09` **Dekret Królewski** | Korona & Borgiowie | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 26.0% → **1.3%** | **`-24.7%`** | 89.5 → **36.3 pkt** (`-53.2`) |
| `caa-10` **Echo Alhambry** | Cienie Al-Andalus | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.5% → **4.3%** | **`-20.2%`** | 89.5 → **38.6 pkt** (`-50.9`) |
| `kt-02` **Transmutacja Złota** | Kabała z Toledo | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.8% → **9.6%** | **`-16.2%`** | 89.5 → **49.5 pkt** (`-40.0`) |
| `caa-05` **Ukryty Kurier** | Cienie Al-Andalus | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.5% → **12.8%** | **`-11.7%`** | 89.5 → **56.7 pkt** (`-32.8`) |
| `kb-02` **Pobór Podatków** | Korona & Borgiowie | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 26.0% → **15.1%** | **`-10.9%`** | 89.5 → **66.7 pkt** (`-22.8`) |
| `kt-11` **Medytacja Sefirot** | Kabała z Toledo | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.8% → **16.4%** | **`-9.4%`** | 89.5 → **67.8 pkt** (`-21.7`) |
| `kt-03` **Zakazana Wiedza** | Kabała z Toledo | 0zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 25.8% → **20.7%** | **`-5.1%`** | 89.5 → **74.5 pkt** (`-15.0`) |
| `kt-05` **Wskazówka Cyklu** | Kabała z Toledo | 1zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 25.8% → **19.7%** | **`-6.1%`** | 89.5 → **76.8 pkt** (`-12.7`) |
| `kb-10` **Pieczęć Korony** | Korona & Borgiowie | 4zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 26.0% → **21.1%** | **`-4.9%`** | 89.5 → **78.4 pkt** (`-11.1`) |
| `so-10` **Oczyść Miasto** | Święte Oficjum | 5zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 23.3% → **19.6%** | **`-3.7%`** | 89.5 → **78.5 pkt** (`-11.0`) |
| `gc-09` **Lista Dłużników** | Gildia Cieni | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.5% → **20.7%** | **`-4.8%`** | 89.5 → **79.8 pkt** (`-9.7`) |
| `gc-10` **Upadek Domu** | Gildia Cieni | 4zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 25.5% → **20.6%** | **`-4.9%`** | 89.5 → **80.6 pkt** (`-8.9`) |
| `caa-06` **Ucieczka z Lochów** | Cienie Al-Andalus | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.5% → **21.5%** | **`-3.0%`** | 89.5 → **82.1 pkt** (`-7.4`) |
| `so-04` **Publiczne Ostrzeżenie** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.3% → **22.5%** | **`-0.8%`** | 89.5 → **83.7 pkt** (`-5.8`) |
| `so-08` **Nasłanie Inkwizytora** | Święte Oficjum | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.3% → **23.3%** | **`+0.0%`** | 89.5 → **83.8 pkt** (`-5.7`) |
| `gc-07` **Skrytobójstwo** | Gildia Cieni | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.5% → **26.5%** | **`+1.0%`** | 89.5 → **85.4 pkt** (`-4.1`) |
| `kt-09` **Fragment Kodeksu** | Kabała z Toledo | 1zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.8% → **24.2%** | **`-1.6%`** | 89.5 → **85.4 pkt** (`-4.1`) |
| `gc-04` **Informator** | Gildia Cieni | 1zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 25.5% → **22.8%** | **`-2.7%`** | 89.5 → **85.5 pkt** (`-4.0`) |
| `gc-01` **Przekupiony Strażnik** | Gildia Cieni | 1zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.5% → **27.4%** | **`+1.9%`** | 89.5 → **85.7 pkt** (`-3.8`) |
| `so-07` **Przesłuchanie Oficjum** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.3% → **25.1%** | **`+1.8%`** | 89.5 → **86.0 pkt** (`-3.5`) |
| `gc-11` **Fałszywe Świadectwo Cechu** | Gildia Cieni | 0zł / 2☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.5% → **27.2%** | **`+1.7%`** | 89.5 → **86.1 pkt** (`-3.4`) |
| `gc-02` **Czarny Rynek** | Gildia Cieni | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.5% → **25.6%** | **`+0.1%`** | 89.5 → **86.7 pkt** (`-2.8`) |
| `gc-03` **Podrzucenie Księgi** | Gildia Cieni | 1zł / 2☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.5% → **26.9%** | **`+1.4%`** | 89.5 → **86.9 pkt** (`-2.6`) |
| `so-03` **Podejrzenie** | Święte Oficjum | 2zł / 4☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.3% → **24.5%** | **`+1.2%`** | 89.5 → **86.9 pkt** (`-2.6`) |

### 2.1b. 🩸 Autopodatek Frakcji (Self-Harm)
Karty, których wyłączenie **podnosi** win share własnej frakcji. Gracz zauważy je jako haracz, nawet gdy stół 4P jest równy dzięki temu haraczowi.

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kt-04` **Zwierciadło Herezji** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.8% → **30.4%** | **`+4.6%`** | 89.5 → **79.1 pkt** (`-10.4`) |
| `caa-11` **Nocna Zmiana Warty** | Cienie Al-Andalus | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.5% → **28.4%** | **`+3.9%`** | 89.5 → **83.4 pkt** (`-6.1`) |

### 2.2. ⚠️ Karty Destabilizujące Kanon 4P (Disruptors)
Karty, których wyłączenie podnosi 4P Score ($\Delta \text{4P} \ge +1.5$ pkt):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `so-06` **Areszt Trybunalski** | Święte Oficjum | 2zł / 0☣ | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) | 23.3% → **25.0%** | `+1.7%` | 89.5 → **93.3 pkt** (`+3.8`) |

### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich 60 Kart Frakcji w Kanonie 4P

| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Play-Rate | Faction Win Share 4P | $\Delta$ Frakcji | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `caa-01` | **Przejście Podziemiami** | Cienie Al-Andalus | 0 | 0 | 0.98 | 24.5% → 28.3% | `+3.8%` | 85.2 | `-4.3` | 5.79 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-02` | **Złoto z Kryjówki** | Cienie Al-Andalus | 0 | 0 | 0.68 | 24.5% → 28.7% | `+4.2%` | 82.8 | `-6.7` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-03` | **Cień na Rynku** | Cienie Al-Andalus | 0 | 1 | 0.92 | 24.5% → 31.7% | `+7.2%` | 71.3 | `-18.2` | 5.83 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-04` | **Fałszywy Trop** | Cienie Al-Andalus | 0 | 0 | 0.97 | 24.5% → 28.9% | `+4.4%` | 81.8 | `-7.7` | 5.77 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-05` | **Ukryty Kurier** | Cienie Al-Andalus | 0 | 0 | 1.02 | 24.5% → 12.8% | `-11.7%` | 56.7 | `-32.8` | 6.02 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `caa-12` | **Skrytka w Murach** | Cienie Al-Andalus | 1 | 0 | 0.84 | 24.5% → 29.6% | `+5.1%` | 80.2 | `-9.3` | 5.75 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-06` | **Ucieczka z Lochów** | Cienie Al-Andalus | 0 | 0 | 0.62 | 24.5% → 21.5% | `-3.0%` | 82.1 | `-7.4` | 5.82 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `caa-07` | **Szantaż Bractwa** | Cienie Al-Andalus | 0 | 0 | 0.20 | 24.5% → 28.2% | `+3.7%` | 83.6 | `-5.9` | 5.77 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `caa-11` | **Nocna Zmiana Warty** | Cienie Al-Andalus | 1 | 0 | 0.13 | 24.5% → 28.4% | `+3.9%` | 83.4 | `-6.1` | 5.77 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-08` | **Kaptur Nocy** | Cienie Al-Andalus | 2 | 0 | 0.59 | 24.5% → 28.7% | `+4.2%` | 82.6 | `-6.9` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-09` | **Kurier Relikwii** | Cienie Al-Andalus | 0 | 0 | 0.87 | 24.5% → 30.0% | `+5.5%` | 79.3 | `-10.2` | 5.75 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-10` | **Echo Alhambry** | Cienie Al-Andalus | 2 | 0 | 1.00 | 24.5% → 4.3% | `-20.2%` | 38.6 | `-50.9` | 6.12 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `gc-02` | **Czarny Rynek** | Gildia Cieni | 0 | 0 | 0.79 | 25.5% → 25.6% | `+0.1%` | 86.7 | `-2.8` | 5.83 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-12` | **Złodziejski Zwiad** | Gildia Cieni | 0 | 2 | 0.44 | 25.5% → 28.3% | `+2.8%` | 83.7 | `-5.8` | 5.82 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `gc-01` | **Przekupiony Strażnik** | Gildia Cieni | 1 | 1 | 0.48 | 25.5% → 27.4% | `+1.9%` | 85.7 | `-3.8` | 5.81 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-03` | **Podrzucenie Księgi** | Gildia Cieni | 1 | 2 | 0.08 | 25.5% → 26.9% | `+1.4%` | 86.9 | `-2.6` | 5.82 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-04` | **Informator** | Gildia Cieni | 1 | 1 | 0.80 | 25.5% → 22.8% | `-2.7%` | 85.5 | `-4.0` | 5.89 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `gc-05` | **Fałszywy Świadek** | Gildia Cieni | 1 | 0 | 0.00 | 25.5% → 25.0% | `-0.5%` | 87.4 | `-2.1` | 5.85 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `gc-07` | **Skrytobójstwo** | Gildia Cieni | 0 | 0 | 0.80 | 25.5% → 26.5% | `+1.0%` | 85.4 | `-4.1` | 5.88 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-11` | **Fałszywe Świadectwo Cechu** | Gildia Cieni | 0 | 2 | 0.31 | 25.5% → 27.2% | `+1.7%` | 86.1 | `-3.4` | 5.82 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-08` | **Zatrute Złoto** | Gildia Cieni | 1 | 2 | 0.00 | 25.5% → 26.4% | `+0.9%` | 86.4 | `-3.1` | 5.81 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `gc-06` | **Szantaż** | Gildia Cieni | 3 | 1 | 0.44 | 25.5% → 24.8% | `-0.7%` | 88.3 | `-1.2` | 5.84 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-09` | **Lista Dłużników** | Gildia Cieni | 1 | 0 | 0.79 | 25.5% → 20.7% | `-4.8%` | 79.8 | `-9.7` | 5.87 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `gc-10` | **Upadek Domu** | Gildia Cieni | 4 | 2 | 0.47 | 25.5% → 20.6% | `-4.9%` | 80.6 | `-8.9` | 5.91 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-01` | **Rozkaz Dworu** | Korona & Borgiowie | 1 | 1 | 0.23 | 26.0% → 36.1% | `+10.1%` | 62.5 | `-27.0` | 5.73 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kb-02` | **Pobór Podatków** | Korona & Borgiowie | 1 | 0 | 0.85 | 26.0% → 15.1% | `-10.9%` | 66.7 | `-22.8` | 5.96 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-03` | **Plotka Dworska** | Korona & Borgiowie | 1 | 1 | 0.60 | 26.0% → 36.6% | `+10.6%` | 60.3 | `-29.2` | 5.73 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-11` | **Tajny Emisariusz** | Korona & Borgiowie | 1 | 0 | 0.84 | 26.0% → 33.7% | `+7.7%` | 69.4 | `-20.1` | 5.72 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-04` | **Faworyt Dworu** | Korona & Borgiowie | 2 | 0 | 0.73 | 26.0% → 34.2% | `+8.2%` | 68.2 | `-21.3` | 5.73 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-05` | **List Żelazny** | Korona & Borgiowie | 2 | 1 | 0.82 | 26.0% → 36.3% | `+10.3%` | 62.2 | `-27.3` | 5.67 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-12` | **Szantaż Salonowy** | Korona & Borgiowie | 1 | 2 | 0.82 | 26.0% → 31.0% | `+5.0%` | 76.9 | `-12.6` | 5.78 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-06` | **Areszt Królewski** | Korona & Borgiowie | 2 | 0 | 0.27 | 26.0% → 34.4% | `+8.4%` | 67.7 | `-21.8` | 5.74 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kb-07` | **Szantaż Pieczęcią** | Korona & Borgiowie | 2 | 0 | 0.52 | 26.0% → 34.6% | `+8.6%` | 66.8 | `-22.7` | 5.73 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-08` | **Przekupstwo Sędziego** | Korona & Borgiowie | 2 | 0 | 0.52 | 26.0% → 34.6% | `+8.6%` | 66.8 | `-22.7` | 5.73 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-09` | **Dekret Królewski** | Korona & Borgiowie | 2 | 0 | 0.86 | 26.0% → 1.3% | `-24.7%` | 36.3 | `-53.2` | 6.11 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-10` | **Pieczęć Korony** | Korona & Borgiowie | 4 | 1 | 0.17 | 26.0% → 21.1% | `-4.9%` | 78.4 | `-11.1` | 5.99 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-02` | **Transmutacja Złota** | Kabała z Toledo | 0 | 0 | 0.96 | 25.8% → 9.6% | `-16.2%` | 49.5 | `-40.0` | 5.99 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-03` | **Zakazana Wiedza** | Kabała z Toledo | 0 | 2 | 0.71 | 25.8% → 20.7% | `-5.1%` | 74.5 | `-15.0` | 6.12 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-01` | **Ścieżka Wtajemniczenia** | Kabała z Toledo | 1 | 0 | 0.98 | 25.8% → 32.1% | `+6.3%` | 73.4 | `-16.1` | 5.69 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-04` | **Zwierciadło Herezji** | Kabała z Toledo | 1 | 0 | 0.17 | 25.8% → 30.4% | `+4.6%` | 79.1 | `-10.4` | 5.75 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-05` | **Wskazówka Cyklu** | Kabała z Toledo | 1 | 1 | 0.95 | 25.8% → 19.7% | `-6.1%` | 76.8 | `-12.7` | 6.05 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-12` | **Strażnik Archiwum** | Kabała z Toledo | 1 | 0 | 0.88 | 25.8% → 30.8% | `+5.0%` | 78.2 | `-11.3` | 5.72 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-07` | **Archiwum Ukryte** | Kabała z Toledo | 0 | 0 | 0.41 | 25.8% → 30.3% | `+4.5%` | 79.6 | `-9.9` | 5.75 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kt-08` | **Areszt Wiedzy** | Kabała z Toledo | 1 | 0 | 0.69 | 25.8% → 29.2% | `+3.4%` | 82.8 | `-6.7` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-06` | **Przesłuchanie Imienia** | Kabała z Toledo | 2 | 0 | 0.72 | 25.8% → 34.5% | `+8.7%` | 66.6 | `-22.9` | 5.71 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-11` | **Medytacja Sefirot** | Kabała z Toledo | 2 | 0 | 0.92 | 25.8% → 16.4% | `-9.4%` | 67.8 | `-21.7` | 5.80 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-09` | **Fragment Kodeksu** | Kabała z Toledo | 1 | 1 | 0.96 | 25.8% → 24.2% | `-1.6%` | 85.4 | `-4.1` | 5.99 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kt-10` | **Pieczęć Salomona** | Kabała z Toledo | 4 | 0 | 0.51 | 25.8% → 0.0% | `-25.8%` | 32.7 | `-56.8` | 6.12 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `so-05` | **Wezwanie do Trybunału** | Święte Oficjum | 0 | 4 | 0.00 | 23.3% → 20.5% | `-2.8%` | 80.2 | `-9.3` | 5.88 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `so-01` | **Patrol Familiariuszy** | Święte Oficjum | 1 | 2 | 0.25 | 23.3% → 25.0% | `+1.7%` | 89.9 | `+0.4` | 5.85 | 0.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `so-02` | **Skarbiec Trybunału** | Święte Oficjum | 1 | 2 | 0.52 | 23.3% → 23.6% | `+0.3%` | 90.3 | `+0.8` | 5.87 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-04` | **Publiczne Ostrzeżenie** | Święte Oficjum | 1 | 0 | 0.90 | 23.3% → 22.5% | `-0.8%` | 83.7 | `-5.8` | 5.78 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-12` | **Straż Trybunalska** | Święte Oficjum | 1 | 2 | 0.26 | 23.3% → 24.8% | `+1.5%` | 89.7 | `+0.2` | 5.85 | 0.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `so-03` | **Podejrzenie** | Święte Oficjum | 2 | 4 | 0.30 | 23.3% → 24.5% | `+1.2%` | 86.9 | `-2.6` | 5.90 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-08` | **Nasłanie Inkwizytora** | Święte Oficjum | 0 | 0 | 0.90 | 23.3% → 23.3% | `+0.0%` | 83.8 | `-5.7` | 5.80 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-11` | **Dekret Czystości Wiary** | Święte Oficjum | 0 | 1 | 0.93 | 23.3% → 24.1% | `+0.8%` | 90.2 | `+0.7` | 5.85 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-07` | **Przesłuchanie Oficjum** | Święte Oficjum | 1 | 0 | 0.86 | 23.3% → 25.1% | `+1.8%` | 86.0 | `-3.5` | 5.76 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-09` | **Świadek Koronny** | Święte Oficjum | 1 | 1 | 0.16 | 23.3% → 23.9% | `+0.6%` | 89.5 | `0.0` | 5.85 | 0.0% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `so-06` | **Areszt Trybunalski** | Święte Oficjum | 2 | 0 | 0.93 | 23.3% → 25.0% | `+1.7%` | 93.3 | `+3.8` | 5.78 | 0.0% | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) |
| `so-10` | **Oczyść Miasto** | Święte Oficjum | 5 | 1 | 0.81 | 23.3% → 19.6% | `-3.7%` | 78.5 | `-11.0` | 5.97 | 0.0% | 👑 FILAR KANONU (Core Keystone) |

### 2.4. 🎯 Monokultura Talii (Deck Concentration Index)

Jak mocno skoncentrowane jest zagrywanie kart w obrębie każdej frakcji.
Wskaźnik HHI (Herfindahl–Hirschman Index) mierzy koncentrację: HHI = 1.0 oznacza, że 100% zagrań to 1 karta; HHI ≈ 1/N oznacza idealnie równomierny rozkład.

| Frakcja | Kart w Talii | Top Karta (Play-Rate) | Top 2 (%) | HHI | Ocena |
| :--- | :---: | :--- | :---: | :---: | :--- |
| Cienie Al-Andalus | 12 | `caa-05` (1.02) | 22.9% | 0.097 | 🟢 Zdrowy rozkład |
| Gildia Cieni | 12 | `gc-04` (0.80) | 29.6% | 0.119 | 🟢 Zdrowy rozkład |
| Korona & Borgiowie | 12 | `kb-09` (0.86) | 23.6% | 0.098 | 🟢 Zdrowy rozkład |
| Kabała z Toledo | 12 | `kt-01` (0.98) | 21.9% | 0.093 | 🟢 Zdrowy rozkład |
| Święte Oficjum | 12 | `so-06` (0.93) | 27.3% | 0.113 | 🟢 Zdrowy rozkład |

---

## 3. ⏳ Warstwa II — Kronika Dziejów w 4P (Ablacja 8 Kart Wydarzeń Czasu)

Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans w 4P:

| ID | Karta Wydarzenia | 4P Score | $\Delta$ 4P | Średnia Er | Deadlock % | Status Roli w Kronice |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `time-01` | **Kapitulacja Grenady** | 89.5 → 🟡 ** 89.8** (`⬆️ +0.3`) | `+0.3 pkt` | 5.87 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-02` | **Godzina Policyjna** | 89.5 → 🟡 ** 88.0** (`🔻 -1.5`) | `-1.5 pkt` | 5.84 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-03` | **Flota Odkrywców** | 89.5 → 🟢 ** 90.2** (`⬆️ +0.7`) | `+0.7 pkt` | 5.91 Er | 0.0% | ⚖️ Neutralna Kronika |
| `time-04` | **Rewizja w Dzielnicach** | 89.5 → 🟡 ** 89.6** (`⬆️ +0.1`) | `+0.1 pkt` | 5.88 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-05` | **Gorączka Donosów** | 89.5 → 🟡 ** 87.3** (`🔻 -2.2`) | `-2.2 pkt` | 5.85 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-06` | **Nocna Obława** | 89.5 → 🟡 ** 88.0** (`🔻 -1.5`) | `-1.5 pkt` | 5.84 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-07` | **Bunt w Lochach** | 89.5 → 🟡 ** 86.4** (`🔻 -3.1`) | `-3.1 pkt` | 5.84 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-08` | **Święte Przymierze** | 89.5 → 🟡 ** 83.4** (`🔻 -6.1`) | `-6.1 pkt` | 5.74 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-09` | **Jarmark Królewski** | 89.5 → 🟡 ** 87.9** (`🔻 -1.6`) | `-1.6 pkt` | 5.85 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-10` | **Amnestia Biskupia** | 89.5 → 🟡 ** 87.9** (`🔻 -1.6`) | `-1.6 pkt` | 5.83 Er | 0.0% | 🟢 Stabilizator tempa |

---

## 4. ⚙️ Warstwa III — Matryca 9 Obszarów Wpływu Mechanik Gry (L1, L2, L4)

Mechaniki w tym raporcie: **skraj albo wyłączenie**. Testy ±1 są w `audit_level1` / `audit_level2` / `audit_level4`. **Δ≈0 nie jest harmonią.**

| Kategoria Mechaniki | Liczba Testów | Rola w Ekosystemie Kanonu 4P | Rekomendacja Balansowa |
| :--- | :---: | :--- | :--- |
| 👑 / 🛡️ **Filary i Bezpieczniki** | **29** | Ablacja wali w stół — gracze czują tę gałkę | **Cel kanonu** |
| ⚠️ **Za słabe dźwignie** | **2** | Rusza share, nie trzyma stołu — nie jest „zbalansowana” | **Wzmocnić aż będzie filarem** |
| 💤 **Martwe / uśpione ścieżki** | **0** | Dual-win z witalności albo ablacja Δ≈0 | Wada pomiaru, nie harmonia |
| ⚠️ / 💡 **Wady bieżącej wartości** | **0** | Inna wartość gałki **podnosi** 4P — obecny setting szkodzi | **Przekręcić albo rework** |

### 4.0. ⚠️ Problematyczne mechaniki (osobny wykaz)
Wszystkie mechaniki z grup **DEAD**, **WEAK/NEUTRAL** i **DISRUPTOR**: ścieżki dual-win z `evaluate_vitality`, testy z $|\Delta\text{4P}| \le 0.8$ i ruchem share $\le 1.5$ pp (DEAD), za słabe dźwignie (WEAK) oraz wady bieżącej wartości (DISRUPTOR).

| Badany Podsystem | Kategoria | 4P Score | $\Delta$ 4P | Klasyfikacja |
| :--- | :--- | :---: | :---: | :--- |
| **Szlak Morski: era 4 → nigdy (99)** | Poziom 4: Warianty i Modyfikatory | 89.5 → 🟡 ** 88.1** (`🔻 -1.4`) | `-1.4 pkt` | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |
| **Inkwizytor Patrol: ruch x2 (podwojona prędkość)** | Poziom 4: Warianty i Modyfikatory | 89.5 → 🟡 ** 86.8** (`🔻 -2.7`) | `-2.7 pkt` | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |

### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)

| Badany Podsystem / Modyfikator L1 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Limit Er: 15 → 7 (skrajna presja)** | 89.5 → 🟡 ** 81.7** (`🔻 -7.8`) | `-7.8 pkt` | 5.70 Er | 10.5% | 4.2% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Próg Oskarżenia: 7 → 1** | 89.5 → 🔴 ** 27.2** (`🔻 -62.3`) | `-62.3 pkt` | 5.56 Er | 0.0% | 2.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Oskarżenia: 7 → 14** | 89.5 → 🔴 ** 33.9** (`🔻 -55.6`) | `-55.6 pkt` | 6.38 Er | 0.0% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 0zł (wyłączenie)** | 89.5 → 🔴 ** 57.6** (`🔻 -31.9`) | `-31.9 pkt` | 6.49 Er | 0.0% | 11.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 8zł** | 89.5 → 🔴 ** 24.5** (`🔻 -65.0`) | `-65.0 pkt` | 5.05 Er | 0.0% | 1.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 1** | 89.5 → 🔴 ** 29.5** (`🔻 -60.0`) | `-60.0 pkt` | 6.76 Er | 0.0% | 5.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 6** | 89.5 → 🟠 ** 77.3** (`🔻 -12.2`) | `-12.2 pkt` | 5.50 Er | 0.0% | 4.0% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Limit kart na ręce: 5 → 1** | 89.5 → 🔴 **  8.4** (`🔻 -81.1`) | `-81.1 pkt` | 8.75 Er | 0.7% | 41.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 10** | 89.5 → 🔴 **  6.5** (`🔻 -83.0`) | `-83.0 pkt` | 4.89 Er | 0.0% | 3.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: cooldown 3 → 0 (co erę)** | 89.5 → 🔴 ** 13.3** (`🔻 -76.2`) | `-76.2 pkt` | 4.95 Er | 0.0% | 4.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: całkowite wyłączenie** | 89.5 → 🔴 ** 60.0** (`🔻 -29.5`) | `-29.5 pkt` | 6.00 Er | 0.0% | 4.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Akcja Gospodarcza: 0zł (brak zysku złota)** | 89.5 → 🔴 ** 52.5** (`🔻 -37.0`) | `-37.0 pkt` | 5.95 Er | 0.0% | 6.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Akcja Gospodarcza: 1 → 2 (podwojenie)** | 89.5 → 🔴 ** 48.2** (`🔻 -41.3`) | `-41.3 pkt` | 5.72 Er | 0.0% | 3.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Obserwowanej: 3 → 2 (skrajna presja)** | 89.5 → 🟡 ** 80.9** (`🔻 -8.6`) | `-8.6 pkt` | 5.76 Er | 0.0% | 4.2% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |

### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)

| Badany Warunek Zwycięstwa L2 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: stosy 7 → 1** | 89.5 → 🔴 ** 17.6** (`🔻 -71.9`) | `-71.9 pkt` | 3.97 Er | 0.0% | 3.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: stosy 7 → 14** | 89.5 → 🔴 ** 64.8** (`🔻 -24.7`) | `-24.7 pkt` | 5.93 Er | 0.0% | 4.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 1** | 89.5 → 🔴 ** 17.5** (`🔻 -72.0`) | `-72.0 pkt` | 3.48 Er | 0.0% | 3.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 6** | 89.5 → 🔴 ** 58.8** (`🔻 -30.7`) | `-30.7 pkt` | 5.92 Er | 0.0% | 4.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Cienie: relikwie 2 → 4** | 89.5 → 🔴 ** 32.3** (`🔻 -57.2`) | `-57.2 pkt` | 6.17 Er | 0.0% | 4.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: dekrety 2 → 4** | 89.5 → 🔴 ** 34.4** (`🔻 -55.1`) | `-55.1 pkt` | 6.12 Er | 0.0% | 4.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: wymóg haków 2 → 0** | 89.5 → 🟠 ** 74.6** (`🔻 -14.9`) | `-14.9 pkt` | 5.79 Er | 0.0% | 4.2% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Korona: wymóg haków 2 → 4** | 89.5 → 🔴 ** 34.3** (`🔻 -55.2`) | `-55.2 pkt` | 6.12 Er | 0.0% | 4.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: fragmenty 3 → 1** | 89.5 → 🔴 ** 56.5** (`🔻 -33.0`) | `-33.0 pkt` | 6.06 Er | 0.0% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: fragmenty 3 → 6** | 89.5 → 🔴 ** 32.7** (`🔻 -56.8`) | `-56.8 pkt` | 6.15 Er | 0.0% | 4.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 9 → 1** | 89.5 → 🔴 ** 16.8** (`🔻 -72.7`) | `-72.7 pkt` | 3.01 Er | 0.0% | 2.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 9 → 18** | 89.5 → 🔴 ** 31.6** (`🔻 -57.9`) | `-57.9 pkt` | 6.10 Er | 0.0% | 4.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)

| Badany Wariant / Modyfikator L4 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kronika Dziejów: całkowite wyłączenie** | 89.5 → 🟠 ** 67.1** (`🔻 -22.4`) | `-22.4 pkt` | 5.89 Er | 0.0% | 4.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kronika Dziejów: co 3 Ery (spowolniony zegar)** | 89.5 → 🟠 ** 75.7** (`🔻 -13.8`) | `-13.8 pkt` | 5.89 Er | 0.0% | 4.7% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Inkwizytor Patrol: ruch 1 → 0 (wyłączenie)** | 89.5 → 🔴 ** 32.2** (`🔻 -57.3`) | `-57.3 pkt` | 6.42 Er | 0.0% | 4.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Inkwizytor Patrol: ruch x2 (podwojona prędkość)** | 89.5 → 🟡 ** 86.8** (`🔻 -2.7`) | `-2.7 pkt` | 5.80 Er | 0.0% | 4.3% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |
| **Szlak Morski: era 4 → nigdy (99)** | 89.5 → 🟡 ** 88.1** (`🔻 -1.4`) | `-1.4 pkt` | 5.87 Er | 0.0% | 4.2% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |

---

## 5. 👥 Warstwa IV — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych. Kolumna win share to HUD kanonu; setup+witalność to stary blend (kara martwej ścieżki).

| Nieobecna Frakcja | Setup Testowy | Win share | Setup+witalność | Diagnoza |
| :--- | :--- | :---: | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`83.1`** | `83.1` | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`86.9`** | `86.9` | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`97.3`** | `97.3` | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`84.8`** | `84.8` | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`95.4`** | `95.4` | Brak presji stosów i bezpośredniego Inkwizytora |