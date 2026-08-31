# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v1.0-alpha.170

**Wersja Gry:** `v1.0-alpha.170` | **Data Badania:** 2026-08-30 23:08 | **Próba:** 10000 gier/setup (50000 gier na wariant) | **Ziarno:** 42
**4P Score (win share):** 🟢 ** 90.6** pkt | **Witalność (osobna kara):** `0.000` | **Śr. Er:** `5.88` | **Deadlocki:** `0.0%` | **Pas Biedy:** `2.9%`
**Udziały 4P:** CAA 24.3% · GC 25.8% · KB 26.1% · KT 25.8% · SO 23.0%

Klasyfikacja L1/L2/L4 i Δ 4P liczą wyłącznie równość win share (`calculate_balance_score`). Kara witalności jest osobno.

---

## 0. Wady z tej próby (nie HUD win share)

Kubełki klasyfikatora i ostrzeżenia witalności z bieżącego runu.

- **Autopodatek (SELF_HARM):** 6/60
- **DEAD_WEIGHT:** `gc-05` Fałszywy Świadek, `so-05` Wezwanie do Trybunału, `so-09` Świadek Koronny
- **Karty Kroniki |Δ4P| ≤ 0.8:** 3/10
- **Ablacja całej Kroniki (`L4_NO_TIME_DECK`):** Δ4P -24.3 (STABILIZER)
- **Mechaniki WEAK/NEUTRAL:** Szlak Morski: era 4 → nigdy (99)

---

## 1. 🗺️ Podsumowanie Ekosystemu Kart Kanonu 4P (Matryca Wpływu Kart, 60 kart)

Rozkład wszystkich 60 kart frakcyjnych w matrycy **Wpływ na Frakcję ($\Delta \text{Share}$)** vs **Wpływ na Kanon 4P ($\Delta \text{4P Score}$)**:

| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |
| :--- | :---: | :---: | :--- | :--- |
| 🩸 **Autopodatek (Self-Harm)** | **6** | 10.0% | Wyłączenie **podnosi** win share własnej frakcji — karta jest haraczem, nie silnikiem | **Rework / osłabienie kosztu, nie filar** |
| 🔄 **Rozcieńczalnik Talii (Tempo Filler)** | **9** | 15.0% | Normalna karta tempa — ablacja fałszywie flaguje ją jako autopodatek z powodu odchudzenia talii | **Normalny element deckbuildingu** |
| 💤 **Karta Pasywna (Dead Weight)** | **3** | 5.0% | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia lub wycięcia** |
| ⚠️ **Karta Destabilizująca (Disruptor)** | **1** | 1.7% | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |
| ⚖️ **Zbalansowane Narzędzie** | **22** | 36.7% | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Narzędzie, nie złoty środek całego kanonu** |
| 👑 / ⚓ **Filar / Kotwica Kanonu** | **19** | 31.7% | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |

---

## 2. 🃏 Warstwa I — Szczegółowa Analiza 60 Kart Frakcji w Kanonie 4P

### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)
Karty, których brak powoduje spadek wyniku Kanonu 4P o $\ge 4.0$ pkt lub załamanie winrate frakcji o $\ge 4.0\%$ — **bez** autopodatków (te są w 2.1b):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kt-10` **Pieczęć Salomona** | Kabała z Toledo | 4zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.8% → **0.0%** | **`-25.8%`** | 90.6 → **33.9 pkt** (`-56.7`) |
| `kb-09` **Dekret Królewski** | Korona & Borgiowie | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 26.1% → **0.6%** | **`-25.5%`** | 90.6 → **35.0 pkt** (`-55.6`) |
| `caa-10` **Echo Alhambry** | Cienie Al-Andalus | 3zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.3% → **4.1%** | **`-20.2%`** | 90.6 → **38.0 pkt** (`-52.6`) |
| `kt-02` **Transmutacja Złota** | Kabała z Toledo | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.8% → **7.5%** | **`-18.3%`** | 90.6 → **46.2 pkt** (`-44.4`) |
| `caa-05` **Ukryty Kurier** | Cienie Al-Andalus | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.3% → **13.0%** | **`-11.3%`** | 90.6 → **57.9 pkt** (`-32.7`) |
| `kt-03` **Zakazana Wiedza** | Kabała z Toledo | 0zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 25.8% → **17.2%** | **`-8.6%`** | 90.6 → **61.9 pkt** (`-28.7`) |
| `kb-02` **Pobór Podatków** | Korona & Borgiowie | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 26.1% → **15.3%** | **`-10.8%`** | 90.6 → **67.3 pkt** (`-23.3`) |
| `kt-11` **Medytacja Sefirot** | Kabała z Toledo | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.8% → **17.1%** | **`-8.7%`** | 90.6 → **70.7 pkt** (`-19.9`) |
| `gc-10` **Upadek Domu** | Gildia Cieni | 4zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.8% → **17.6%** | **`-8.2%`** | 90.6 → **71.1 pkt** (`-19.5`) |
| `kt-05` **Wskazówka Cyklu** | Kabała z Toledo | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.8% → **17.9%** | **`-7.9%`** | 90.6 → **73.6 pkt** (`-17.0`) |
| `so-10` **Oczyść Miasto** | Święte Oficjum | 5zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 23.0% → **18.3%** | **`-4.7%`** | 90.6 → **75.0 pkt** (`-15.6`) |
| `kt-09` **Fragment Kodeksu** | Kabała z Toledo | 2zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 25.8% → **22.4%** | **`-3.4%`** | 90.6 → **81.2 pkt** (`-9.4`) |
| `gc-09` **Lista Dłużników** | Gildia Cieni | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.8% → **21.3%** | **`-4.5%`** | 90.6 → **82.2 pkt** (`-8.4`) |
| `kb-10` **Pieczęć Korony** | Korona & Borgiowie | 4zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 26.1% → **25.0%** | **`-1.1%`** | 90.6 → **82.5 pkt** (`-8.1`) |
| `so-04` **Publiczne Ostrzeżenie** | Święte Oficjum | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.0% → **21.2%** | **`-1.8%`** | 90.6 → **84.0 pkt** (`-6.6`) |
| `caa-06` **Ucieczka z Lochów** | Cienie Al-Andalus | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.3% → **21.8%** | **`-2.5%`** | 90.6 → **84.8 pkt** (`-5.8`) |
| `gc-08` **Zatrute Złoto** | Gildia Cieni | 0zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.8% → **26.9%** | **`+1.1%`** | 90.6 → **86.4 pkt** (`-4.2`) |
| `gc-02` **Czarny Rynek** | Gildia Cieni | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.8% → **27.0%** | **`+1.2%`** | 90.6 → **87.0 pkt** (`-3.6`) |
| `gc-04` **Informator** | Gildia Cieni | 1zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.8% → **23.4%** | **`-2.4%`** | 90.6 → **88.0 pkt** (`-2.6`) |

### 2.1b. 🩸 Autopodatek Frakcji (Self-Harm)
Karty, których wyłączenie **podnosi** win share własnej frakcji. Gracz zauważy je jako haracz, nawet gdy stół 4P jest równy dzięki temu haraczowi.

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kb-04` **Faworyt Dworu** | Korona & Borgiowie | 4zł / 3☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 26.1% → **35.7%** | **`+9.6%`** | 90.6 → **63.6 pkt** (`-27.0`) |
| `caa-02` **Złoto z Kryjówki** | Cienie Al-Andalus | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.3% → **29.6%** | **`+5.3%`** | 90.6 → **81.0 pkt** (`-9.6`) |
| `caa-11` **Nocna Zmiana Warty** | Cienie Al-Andalus | 2zł / 2☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.3% → **29.4%** | **`+5.1%`** | 90.6 → **81.3 pkt** (`-9.3`) |
| `gc-03` **Podrzucenie Księgi** | Gildia Cieni | 1zł / 3☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.8% → **29.1%** | **`+3.3%`** | 90.6 → **82.1 pkt** (`-8.5`) |
| `gc-01` **Przekupiony Strażnik** | Gildia Cieni | 1zł / 3☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.8% → **29.0%** | **`+3.2%`** | 90.6 → **82.2 pkt** (`-8.4`) |
| `so-12` **Straż Trybunalska** | Święte Oficjum | 1zł / 3☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 23.0% → **25.0%** | **`+2.0%`** | 90.6 → **91.0 pkt** (`0.4`) |

### 2.2. ⚠️ Karty Destabilizujące Kanon 4P (Disruptors)
Karty, których wyłączenie podnosi 4P Score ($\Delta \text{4P} \ge +1.5$ pkt):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `so-06` **Areszt Trybunalski** | Święte Oficjum | 2zł / 0☣ | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) | 23.0% → **24.9%** | `+1.9%` | 90.6 → **92.4 pkt** (`+1.8`) |

### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich 60 Kart Frakcji w Kanonie 4P

| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Play-Rate | Faction Win Share 4P | $\Delta$ Frakcji | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `caa-01` | **Przejście Podziemiami** | Cienie Al-Andalus | 0 | 0 | 1.00 | 24.3% → 27.7% | `+3.4%` | 86.4 | `-4.2` | 5.83 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-04` | **Fałszywy Trop** | Cienie Al-Andalus | 0 | 0 | 0.87 | 24.3% → 29.7% | `+5.4%` | 80.3 | `-10.3` | 5.80 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-05` | **Ukryty Kurier** | Cienie Al-Andalus | 0 | 0 | 1.04 | 24.3% → 13.0% | `-11.3%` | 57.9 | `-32.7` | 6.06 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `caa-07` | **Szantaż Bractwa** | Cienie Al-Andalus | 0 | 0 | 0.87 | 24.3% → 29.3% | `+5.0%` | 81.4 | `-9.2` | 5.80 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-06` | **Ucieczka z Lochów** | Cienie Al-Andalus | 1 | 0 | 0.87 | 24.3% → 21.8% | `-2.5%` | 84.8 | `-5.8` | 5.88 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `caa-08` | **Kaptur Nocy** | Cienie Al-Andalus | 1 | 0 | 1.01 | 24.3% → 29.0% | `+4.7%` | 82.2 | `-8.4` | 5.82 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-09` | **Kurier Relikwii** | Cienie Al-Andalus | 1 | 0 | 0.96 | 24.3% → 30.0% | `+5.7%` | 79.8 | `-10.8` | 5.78 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-12` | **Skrytka w Murach** | Cienie Al-Andalus | 1 | 0 | 0.44 | 24.3% → 29.6% | `+5.3%` | 80.8 | `-9.8` | 5.79 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `caa-02` | **Złoto z Kryjówki** | Cienie Al-Andalus | 2 | 0 | 0.00 | 24.3% → 29.6% | `+5.3%` | 81.0 | `-9.6` | 5.80 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-03` | **Cień na Rynku** | Cienie Al-Andalus | 2 | 1 | 0.79 | 24.3% → 32.2% | `+7.9%` | 69.5 | `-21.1` | 5.85 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-11` | **Nocna Zmiana Warty** | Cienie Al-Andalus | 2 | 2 | 0.00 | 24.3% → 29.4% | `+5.1%` | 81.3 | `-9.3` | 5.80 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-10` | **Echo Alhambry** | Cienie Al-Andalus | 3 | 0 | 1.02 | 24.3% → 4.1% | `-20.2%` | 38.0 | `-52.6` | 6.14 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `gc-02` | **Czarny Rynek** | Gildia Cieni | 0 | 0 | 0.90 | 25.8% → 27.0% | `+1.2%` | 87.0 | `-3.6` | 5.85 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-08` | **Zatrute Złoto** | Gildia Cieni | 0 | 1 | 0.91 | 25.8% → 26.9% | `+1.1%` | 86.4 | `-4.2` | 5.87 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-11` | **Fałszywe Świadectwo Cechu** | Gildia Cieni | 0 | 2 | 0.47 | 25.8% → 30.1% | `+4.3%` | 78.1 | `-12.5` | 5.84 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `gc-01` | **Przekupiony Strażnik** | Gildia Cieni | 1 | 3 | 0.09 | 25.8% → 29.0% | `+3.2%` | 82.2 | `-8.4` | 5.83 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `gc-03` | **Podrzucenie Księgi** | Gildia Cieni | 1 | 3 | 0.00 | 25.8% → 29.1% | `+3.3%` | 82.1 | `-8.5` | 5.84 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `gc-04` | **Informator** | Gildia Cieni | 1 | 1 | 0.90 | 25.8% → 23.4% | `-2.4%` | 88.0 | `-2.6` | 5.93 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-07` | **Skrytobójstwo** | Gildia Cieni | 1 | 1 | 0.90 | 25.8% → 29.6% | `+3.8%` | 80.7 | `-9.9` | 5.86 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-09` | **Lista Dłużników** | Gildia Cieni | 1 | 0 | 0.91 | 25.8% → 21.3% | `-4.5%` | 82.2 | `-8.4` | 5.92 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `gc-12` | **Złodziejski Zwiad** | Gildia Cieni | 1 | 2 | 0.28 | 25.8% → 29.6% | `+3.8%` | 81.1 | `-9.5` | 5.83 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `gc-05` | **Fałszywy Świadek** | Gildia Cieni | 2 | 1 | 0.00 | 25.8% → 26.8% | `+1.0%` | 87.9 | `-2.7` | 5.89 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `gc-06` | **Szantaż** | Gildia Cieni | 3 | 1 | 0.30 | 25.8% → 28.5% | `+2.7%` | 84.0 | `-6.6` | 5.86 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `gc-10` | **Upadek Domu** | Gildia Cieni | 4 | 0 | 0.91 | 25.8% → 17.6% | `-8.2%` | 71.1 | `-19.5` | 5.97 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-02` | **Pobór Podatków** | Korona & Borgiowie | 0 | 0 | 0.89 | 26.1% → 15.3% | `-10.8%` | 67.3 | `-23.3` | 6.03 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-01` | **Rozkaz Dworu** | Korona & Borgiowie | 1 | 1 | 0.29 | 26.1% → 36.9% | `+10.8%` | 60.5 | `-30.1` | 5.75 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kb-03` | **Plotka Dworska** | Korona & Borgiowie | 1 | 1 | 0.70 | 26.1% → 35.8% | `+9.7%` | 62.6 | `-28.0` | 5.79 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-11` | **Tajny Emisariusz** | Korona & Borgiowie | 1 | 0 | 0.87 | 26.1% → 34.1% | `+8.0%` | 68.6 | `-22.0` | 5.77 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-12` | **Szantaż Salonowy** | Korona & Borgiowie | 1 | 0 | 0.87 | 26.1% → 30.8% | `+4.7%` | 78.4 | `-12.2` | 5.83 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-05` | **List Żelazny** | Korona & Borgiowie | 2 | 0 | 0.87 | 26.1% → 37.5% | `+11.4%` | 59.6 | `-31.0` | 5.70 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-06` | **Areszt Królewski** | Korona & Borgiowie | 2 | 0 | 0.54 | 26.1% → 37.0% | `+10.9%` | 60.9 | `-29.7` | 5.75 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-07` | **Szantaż Pieczęcią** | Korona & Borgiowie | 2 | 0 | 0.71 | 26.1% → 35.4% | `+9.3%` | 65.3 | `-25.3` | 5.75 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-08` | **Przekupstwo Sędziego** | Korona & Borgiowie | 2 | 0 | 0.71 | 26.1% → 35.4% | `+9.3%` | 65.3 | `-25.3` | 5.75 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-09` | **Dekret Królewski** | Korona & Borgiowie | 2 | 0 | 0.90 | 26.1% → 0.6% | `-25.5%` | 35.0 | `-55.6` | 6.18 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-04` | **Faworyt Dworu** | Korona & Borgiowie | 4 | 3 | 0.04 | 26.1% → 35.7% | `+9.6%` | 63.6 | `-27.0` | 5.77 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-10` | **Pieczęć Korony** | Korona & Borgiowie | 4 | 1 | 0.14 | 26.1% → 25.0% | `-1.1%` | 82.5 | `-8.1` | 5.97 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kt-02` | **Transmutacja Złota** | Kabała z Toledo | 0 | 0 | 0.97 | 25.8% → 7.5% | `-18.3%` | 46.2 | `-44.4` | 6.06 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-03` | **Zakazana Wiedza** | Kabała z Toledo | 0 | 2 | 0.84 | 25.8% → 17.2% | `-8.6%` | 61.9 | `-28.7` | 6.17 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-01` | **Ścieżka Wtajemniczenia** | Kabała z Toledo | 1 | 0 | 0.96 | 25.8% → 31.5% | `+5.7%` | 76.4 | `-14.2` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-04` | **Zwierciadło Herezji** | Kabała z Toledo | 1 | 0 | 0.36 | 25.8% → 31.1% | `+5.3%` | 77.4 | `-13.2` | 5.79 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kt-07` | **Archiwum Ukryte** | Kabała z Toledo | 1 | 0 | 0.28 | 25.8% → 30.8% | `+5.0%` | 78.8 | `-11.8` | 5.79 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kt-11` | **Medytacja Sefirot** | Kabała z Toledo | 1 | 0 | 0.98 | 25.8% → 17.1% | `-8.7%` | 70.7 | `-19.9` | 5.84 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-12` | **Strażnik Archiwum** | Kabała z Toledo | 1 | 0 | 0.87 | 25.8% → 30.1% | `+4.3%` | 81.0 | `-9.6` | 5.79 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-05` | **Wskazówka Cyklu** | Kabała z Toledo | 2 | 0 | 0.96 | 25.8% → 17.9% | `-7.9%` | 73.6 | `-17.0` | 5.98 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-06` | **Przesłuchanie Imienia** | Kabała z Toledo | 2 | 0 | 0.80 | 25.8% → 36.6% | `+10.8%` | 61.3 | `-29.3` | 5.73 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-09` | **Fragment Kodeksu** | Kabała z Toledo | 2 | 1 | 0.93 | 25.8% → 22.4% | `-3.4%` | 81.2 | `-9.4` | 6.04 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-08` | **Areszt Wiedzy** | Kabała z Toledo | 3 | 0 | 0.33 | 25.8% → 31.6% | `+5.8%` | 76.3 | `-14.3` | 5.78 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kt-10` | **Pieczęć Salomona** | Kabała z Toledo | 4 | 0 | 0.50 | 25.8% → 0.0% | `-25.8%` | 33.9 | `-56.7` | 6.15 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `so-04` | **Publiczne Ostrzeżenie** | Święte Oficjum | 0 | 0 | 0.89 | 23.0% → 21.2% | `-1.8%` | 84.0 | `-6.6` | 5.85 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-05` | **Wezwanie do Trybunału** | Święte Oficjum | 0 | 1 | 0.00 | 23.0% → 20.6% | `-2.4%` | 82.4 | `-8.2` | 5.93 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `so-08` | **Nasłanie Inkwizytora** | Święte Oficjum | 0 | 0 | 0.89 | 23.0% → 23.1% | `+0.1%` | 89.4 | `-1.2` | 5.85 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-09` | **Świadek Koronny** | Święte Oficjum | 0 | 3 | 0.00 | 23.0% → 24.2% | `+1.2%` | 91.6 | `+1.0` | 5.89 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `so-11` | **Dekret Czystości Wiary** | Święte Oficjum | 0 | 1 | 0.93 | 23.0% → 22.9% | `-0.1%` | 90.1 | `-0.5` | 5.89 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-01` | **Patrol Familiariuszy** | Święte Oficjum | 1 | 2 | 0.34 | 23.0% → 25.7% | `+2.7%` | 89.8 | `-0.8` | 5.87 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `so-02` | **Skarbiec Trybunału** | Święte Oficjum | 1 | 2 | 0.59 | 23.0% → 23.5% | `+0.5%` | 90.7 | `+0.1` | 5.90 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-03` | **Podejrzenie** | Święte Oficjum | 1 | 2 | 0.23 | 23.0% → 24.7% | `+1.7%` | 90.9 | `+0.3` | 5.88 | 0.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `so-07` | **Przesłuchanie Oficjum** | Święte Oficjum | 1 | 0 | 0.85 | 23.0% → 24.4% | `+1.4%` | 91.6 | `+1.0` | 5.80 | 0.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `so-12` | **Straż Trybunalska** | Święte Oficjum | 1 | 3 | 0.16 | 23.0% → 25.0% | `+2.0%` | 91.0 | `+0.4` | 5.89 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `so-06` | **Areszt Trybunalski** | Święte Oficjum | 2 | 0 | 0.92 | 23.0% → 24.9% | `+1.9%` | 92.4 | `+1.8` | 5.85 | 0.0% | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) |
| `so-10` | **Oczyść Miasto** | Święte Oficjum | 5 | 1 | 0.89 | 23.0% → 18.3% | `-4.7%` | 75.0 | `-15.6` | 6.05 | 0.0% | 👑 FILAR KANONU (Core Keystone) |

### 2.4. 🎯 Monokultura Talii (Deck Concentration Index)

Jak mocno skoncentrowane jest zagrywanie kart w obrębie każdej frakcji.
Wskaźnik HHI (Herfindahl–Hirschman Index) mierzy koncentrację: HHI = 1.0 oznacza, że 100% zagrań to 1 karta; HHI ≈ 1/N oznacza idealnie równomierny rozkład.

| Frakcja | Kart w Talii | Top Karta (Play-Rate) | Top 2 (%) | HHI | Ocena |
| :--- | :---: | :--- | :---: | :---: | :--- |
| Cienie Al-Andalus | 12 | `caa-05` (1.04) | 23.3% | 0.104 | 🟢 Zdrowy rozkład |
| Gildia Cieni | 12 | `gc-08` (0.91) | 27.7% | 0.123 | 🟢 Zdrowy rozkład |
| Korona & Borgiowie | 12 | `kb-09` (0.90) | 23.8% | 0.102 | 🟢 Zdrowy rozkład |
| Kabała z Toledo | 12 | `kt-11` (0.98) | 22.2% | 0.094 | 🟢 Zdrowy rozkład |
| Święte Oficjum | 12 | `so-11` (0.93) | 27.6% | 0.119 | 🟢 Zdrowy rozkład |

---

## 3. ⏳ Warstwa II — Kronika Dziejów w 4P (Ablacja 8 Kart Wydarzeń Czasu)

Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans w 4P:

| ID | Karta Wydarzenia | 4P Score | $\Delta$ 4P | Średnia Er | Deadlock % | Status Roli w Kronice |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `time-01` | **Kapitulacja Grenady** | 90.6 → 🟡 ** 89.6** (`🔻 -1.0`) | `-1.0 pkt` | 5.92 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-02` | **Godzina Policyjna** | 90.6 → 🟡 ** 88.5** (`🔻 -2.1`) | `-2.1 pkt` | 5.88 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-03` | **Flota Odkrywców** | 90.6 → 🟡 ** 89.7** (`🔻 -0.9`) | `-0.9 pkt` | 5.96 Er | 0.0% | ⚖️ Neutralna Kronika |
| `time-04` | **Rewizja w Dzielnicach** | 90.6 → 🟢 ** 90.2** (`🔻 -0.4`) | `-0.4 pkt` | 5.93 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-05` | **Gorączka Donosów** | 90.6 → 🟡 ** 88.0** (`🔻 -2.6`) | `-2.6 pkt` | 5.88 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-06` | **Nocna Obława** | 90.6 → 🟡 ** 88.0** (`🔻 -2.6`) | `-2.6 pkt` | 5.87 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-07` | **Bunt w Lochach** | 90.6 → 🟡 ** 87.9** (`🔻 -2.7`) | `-2.7 pkt` | 5.88 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-08` | **Święte Przymierze** | 90.6 → 🟡 ** 82.9** (`🔻 -7.7`) | `-7.7 pkt` | 5.78 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-09` | **Jarmark Królewski** | 90.6 → 🟢 ** 90.5** (`🔻 -0.1`) | `-0.1 pkt` | 5.89 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-10` | **Amnestia Biskupia** | 90.6 → 🟢 ** 90.2** (`🔻 -0.4`) | `-0.4 pkt` | 5.86 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |

---

## 4. ⚙️ Warstwa III — Matryca 9 Obszarów Wpływu Mechanik Gry (L1, L2, L4)

Mechaniki w tym raporcie: **skraj albo wyłączenie**. Testy ±1 są w `audit_level1` / `audit_level2` / `audit_level4`. **Δ≈0 nie jest harmonią.**

| Kategoria Mechaniki | Liczba Testów | Rola w Ekosystemie Kanonu 4P | Rekomendacja Balansowa |
| :--- | :---: | :--- | :--- |
| 👑 / 🛡️ **Filary i Bezpieczniki** | **30** | Ablacja wali w stół — gracze czują tę gałkę | **Cel kanonu** |
| ⚠️ **Za słabe dźwignie** | **1** | Rusza share, nie trzyma stołu — nie jest „zbalansowana” | **Wzmocnić aż będzie filarem** |
| 💤 **Martwe / uśpione ścieżki** | **0** | Dual-win z witalności albo ablacja Δ≈0 | Wada pomiaru, nie harmonia |
| ⚠️ / 💡 **Wady bieżącej wartości** | **0** | Inna wartość gałki **podnosi** 4P — obecny setting szkodzi | **Przekręcić albo rework** |

### 4.0. ⚠️ Problematyczne mechaniki (osobny wykaz)
Wszystkie mechaniki z grup **DEAD**, **WEAK/NEUTRAL** i **DISRUPTOR**: ścieżki dual-win z `evaluate_vitality`, testy z $|\Delta\text{4P}| \le 0.8$ i ruchem share $\le 1.5$ pp (DEAD), za słabe dźwignie (WEAK) oraz wady bieżącej wartości (DISRUPTOR).

| Badany Podsystem | Kategoria | 4P Score | $\Delta$ 4P | Klasyfikacja |
| :--- | :--- | :---: | :---: | :--- |
| **Szlak Morski: era 4 → nigdy (99)** | Poziom 4: Warianty i Modyfikatory | 90.6 → 🟡 ** 86.9** (`🔻 -3.7`) | `-3.7 pkt` | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |

### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)

| Badany Podsystem / Modyfikator L1 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Limit Er: 15 → 7 (skrajna presja)** | 90.6 → 🟠 ** 79.8** (`🔻 -10.8`) | `-10.8 pkt` | 5.74 Er | 10.7% | 2.9% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Próg Oskarżenia: 7 → 1** | 90.6 → 🔴 ** 24.1** (`🔻 -66.5`) | `-66.5 pkt` | 5.22 Er | 0.0% | 1.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Oskarżenia: 7 → 14** | 90.6 → 🔴 ** 34.8** (`🔻 -55.8`) | `-55.8 pkt` | 6.50 Er | 0.0% | 4.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 0zł (wyłączenie)** | 90.6 → 🔴 ** 56.3** (`🔻 -34.3`) | `-34.3 pkt` | 6.53 Er | 0.0% | 11.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 8zł** | 90.6 → 🔴 ** 28.0** (`🔻 -62.6`) | `-62.6 pkt` | 5.19 Er | 0.0% | 0.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 1** | 90.6 → 🔴 ** 26.6** (`🔻 -64.0`) | `-64.0 pkt` | 6.84 Er | 0.0% | 3.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 6** | 90.6 → 🟠 ** 76.2** (`🔻 -14.4`) | `-14.4 pkt` | 5.53 Er | 0.0% | 2.8% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Limit kart na ręce: 5 → 1** | 90.6 → 🔴 **  6.3** (`🔻 -84.3`) | `-84.3 pkt` | 8.79 Er | 0.9% | 37.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 10** | 90.6 → 🔴 **  6.2** (`🔻 -84.4`) | `-84.4 pkt` | 4.64 Er | 0.0% | 0.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: cooldown 3 → 0 (co erę)** | 90.6 → 🔴 ** 13.4** (`🔻 -77.2`) | `-77.2 pkt` | 4.96 Er | 0.0% | 3.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: całkowite wyłączenie** | 90.6 → 🔴 ** 64.9** (`🔻 -25.7`) | `-25.7 pkt` | 6.02 Er | 0.0% | 3.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Akcja Gospodarcza: 0zł (brak zysku złota)** | 90.6 → 🟠 ** 65.3** (`🔻 -25.3`) | `-25.3 pkt` | 5.97 Er | 0.0% | 4.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Akcja Gospodarcza: 1 → 2 (podwojenie)** | 90.6 → 🔴 ** 51.9** (`🔻 -38.7`) | `-38.7 pkt` | 5.75 Er | 0.0% | 2.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Obserwowanej: 3 → 2 (skrajna presja)** | 90.6 → 🟠 ** 74.9** (`🔻 -15.7`) | `-15.7 pkt` | 5.73 Er | 0.0% | 2.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)

| Badany Warunek Zwycięstwa L2 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: stosy 7 → 1** | 90.6 → 🔴 ** 18.6** (`🔻 -72.0`) | `-72.0 pkt` | 3.88 Er | 0.0% | 2.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: stosy 7 → 14** | 90.6 → 🔴 ** 62.5** (`🔻 -28.1`) | `-28.1 pkt` | 5.97 Er | 0.0% | 2.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 1** | 90.6 → 🔴 ** 18.6** (`🔻 -72.0`) | `-72.0 pkt` | 3.54 Er | 0.0% | 2.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 6** | 90.6 → 🔴 ** 57.3** (`🔻 -33.3`) | `-33.3 pkt` | 5.94 Er | 0.0% | 2.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Cienie: relikwie 2 → 4** | 90.6 → 🔴 ** 32.0** (`🔻 -58.6`) | `-58.6 pkt` | 6.20 Er | 0.0% | 3.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: dekrety 2 → 4** | 90.6 → 🔴 ** 34.3** (`🔻 -56.3`) | `-56.3 pkt` | 6.17 Er | 0.0% | 2.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: wymóg haków 2 → 0** | 90.6 → 🟠 ** 73.1** (`🔻 -17.5`) | `-17.5 pkt` | 5.83 Er | 0.0% | 2.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: wymóg haków 2 → 4** | 90.6 → 🔴 ** 34.2** (`🔻 -56.4`) | `-56.4 pkt` | 6.17 Er | 0.0% | 2.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: fragmenty 3 → 1** | 90.6 → 🔴 ** 55.2** (`🔻 -35.4`) | `-35.4 pkt` | 6.09 Er | 0.0% | 3.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: fragmenty 3 → 6** | 90.6 → 🔴 ** 33.7** (`🔻 -56.9`) | `-56.9 pkt` | 6.16 Er | 0.0% | 2.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 9 → 1** | 90.6 → 🔴 ** 16.9** (`🔻 -73.7`) | `-73.7 pkt` | 2.99 Er | 0.0% | 1.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 9 → 18** | 90.6 → 🔴 ** 31.5** (`🔻 -59.1`) | `-59.1 pkt` | 6.14 Er | 0.0% | 3.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)

| Badany Wariant / Modyfikator L4 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kronika Dziejów: całkowite wyłączenie** | 90.6 → 🟠 ** 66.3** (`🔻 -24.3`) | `-24.3 pkt` | 5.95 Er | 0.0% | 3.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kronika Dziejów: co 3 Ery (spowolniony zegar)** | 90.6 → 🟠 ** 73.7** (`🔻 -16.9`) | `-16.9 pkt` | 5.95 Er | 0.0% | 3.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Inkwizytor Patrol: ruch 1 → 0 (wyłączenie)** | 90.6 → 🔴 ** 31.8** (`🔻 -58.8`) | `-58.8 pkt` | 6.54 Er | 0.1% | 2.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Inkwizytor Patrol: ruch x2 (podwojona prędkość)** | 90.6 → 🟡 ** 83.9** (`🔻 -6.7`) | `-6.7 pkt` | 5.84 Er | 0.0% | 2.9% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Szlak Morski: era 4 → nigdy (99)** | 90.6 → 🟡 ** 86.9** (`🔻 -3.7`) | `-3.7 pkt` | 5.91 Er | 0.0% | 2.9% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |

---

## 5. 👥 Warstwa IV — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych. Kolumna win share to HUD kanonu; setup+witalność to stary blend (kara martwej ścieżki).

| Nieobecna Frakcja | Setup Testowy | Win share | Setup+witalność | Diagnoza |
| :--- | :--- | :---: | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`84.3`** | `84.3` | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`92.0`** | `92.0` | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`97.4`** | `97.4` | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`85.5`** | `85.5` | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`93.7`** | `93.7` | Brak presji stosów i bezpośredniego Inkwizytora |