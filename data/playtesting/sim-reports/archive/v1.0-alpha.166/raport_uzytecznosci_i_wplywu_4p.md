# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v1.0-alpha.166

**Wersja Gry:** `v1.0-alpha.166` | **Data Badania:** 2026-08-30 16:58 | **Próba:** 10000 gier/setup (50000 gier na wariant) | **Ziarno:** 42
**4P Score (win share):** 🟢 ** 92.3** pkt | **Witalność (osobna kara):** `0.000` | **Śr. Er:** `5.88` | **Deadlocki:** `0.0%` | **Pas Biedy:** `2.8%`
**Udziały 4P:** CAA 24.2% · GC 24.2% · KB 26.4% · KT 25.6% · SO 24.6%

Klasyfikacja L1/L2/L4 i Δ 4P liczą wyłącznie równość win share (`calculate_balance_score`). Kara witalności jest osobno.

---

## 0. Wady z tej próby (nie HUD win share)

Kubełki klasyfikatora i ostrzeżenia witalności z bieżącego runu.

- **Autopodatek (SELF_HARM):** 7/60
- **DEAD_WEIGHT:** `gc-05` Fałszywy Świadek, `so-05` Wezwanie do Trybunału, `so-09` Świadek Koronny
- **Karty Kroniki |Δ4P| ≤ 0.8:** 2/10
- **Ablacja całej Kroniki (`L4_NO_TIME_DECK`):** Δ4P -21.2 (STABILIZER)
- **Mechaniki WEAK/NEUTRAL:** Szlak Morski: era 4 → nigdy (99)

---

## 1. 🗺️ Podsumowanie Ekosystemu Kart Kanonu 4P (Matryca Wpływu Kart, 60 kart)

Rozkład wszystkich 60 kart frakcyjnych w matrycy **Wpływ na Frakcję ($\Delta \text{Share}$)** vs **Wpływ na Kanon 4P ($\Delta \text{4P Score}$)**:

| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |
| :--- | :---: | :---: | :--- | :--- |
| 🩸 **Autopodatek (Self-Harm)** | **7** | 11.7% | Wyłączenie **podnosi** win share własnej frakcji — karta jest haraczem, nie silnikiem | **Rework / osłabienie kosztu, nie filar** |
| 🔄 **Rozcieńczalnik Talii (Tempo Filler)** | **9** | 15.0% | Normalna karta tempa — ablacja fałszywie flaguje ją jako autopodatek z powodu odchudzenia talii | **Normalny element deckbuildingu** |
| 💤 **Karta Pasywna (Dead Weight)** | **3** | 5.0% | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia lub wycięcia** |
| ⚠️ **Karta Destabilizująca (Disruptor)** | **0** | 0.0% | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |
| ⚖️ **Zbalansowane Narzędzie** | **23** | 38.3% | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Narzędzie, nie złoty środek całego kanonu** |
| 👑 / ⚓ **Filar / Kotwica Kanonu** | **18** | 30.0% | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |

---

## 2. 🃏 Warstwa I — Szczegółowa Analiza 60 Kart Frakcji w Kanonie 4P

### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)
Karty, których brak powoduje spadek wyniku Kanonu 4P o $\ge 4.0$ pkt lub załamanie winrate frakcji o $\ge 4.0\%$ — **bez** autopodatków (te są w 2.1b):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kt-10` **Pieczęć Salomona** | Kabała z Toledo | 4zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.6% → **0.0%** | **`-25.6%`** | 92.3 → **34.4 pkt** (`-57.9`) |
| `kb-09` **Dekret Królewski** | Korona & Borgiowie | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 26.4% → **0.6%** | **`-25.8%`** | 92.3 → **35.2 pkt** (`-57.1`) |
| `caa-10` **Echo Alhambry** | Cienie Al-Andalus | 3zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.2% → **4.3%** | **`-19.9%`** | 92.3 → **40.2 pkt** (`-52.1`) |
| `kt-02` **Transmutacja Złota** | Kabała z Toledo | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.6% → **7.3%** | **`-18.3%`** | 92.3 → **46.2 pkt** (`-46.1`) |
| `caa-05` **Ukryty Kurier** | Cienie Al-Andalus | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.2% → **12.9%** | **`-11.3%`** | 92.3 → **59.7 pkt** (`-32.6`) |
| `gc-10` **Upadek Domu** | Gildia Cieni | 4zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.2% → **16.2%** | **`-8.0%`** | 92.3 → **65.9 pkt** (`-26.4`) |
| `kt-03` **Zakazana Wiedza** | Kabała z Toledo | 0zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 25.6% → **17.9%** | **`-7.7%`** | 92.3 → **67.8 pkt** (`-24.5`) |
| `kb-02` **Pobór Podatków** | Korona & Borgiowie | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 26.4% → **15.8%** | **`-10.6%`** | 92.3 → **69.1 pkt** (`-23.2`) |
| `kt-11` **Medytacja Sefirot** | Kabała z Toledo | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.6% → **16.7%** | **`-8.9%`** | 92.3 → **70.6 pkt** (`-21.7`) |
| `kt-05` **Wskazówka Cyklu** | Kabała z Toledo | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.6% → **17.8%** | **`-7.8%`** | 92.3 → **73.8 pkt** (`-18.5`) |
| `gc-09` **Lista Dłużników** | Gildia Cieni | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.2% → **19.6%** | **`-4.6%`** | 92.3 → **78.9 pkt** (`-13.4`) |
| `so-10` **Oczyść Miasto** | Święte Oficjum | 5zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 24.6% → **20.9%** | **`-3.7%`** | 92.3 → **81.8 pkt** (`-10.5`) |
| `kt-09` **Fragment Kodeksu** | Kabała z Toledo | 2zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 25.6% → **21.8%** | **`-3.8%`** | 92.3 → **83.5 pkt** (`-8.8`) |
| `caa-06` **Ucieczka z Lochów** | Cienie Al-Andalus | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.2% → **21.2%** | **`-3.0%`** | 92.3 → **84.1 pkt** (`-8.2`) |
| `gc-04` **Informator** | Gildia Cieni | 1zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.2% → **21.8%** | **`-2.4%`** | 92.3 → **85.9 pkt** (`-6.4`) |
| `kb-10` **Pieczęć Korony** | Korona & Borgiowie | 4zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 26.4% → **25.5%** | **`-0.9%`** | 92.3 → **86.4 pkt** (`-5.9`) |
| `so-04` **Publiczne Ostrzeżenie** | Święte Oficjum | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.6% → **23.8%** | **`-0.8%`** | 92.3 → **88.1 pkt** (`-4.2`) |
| `so-08` **Nasłanie Inkwizytora** | Święte Oficjum | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.6% → **25.0%** | **`+0.4%`** | 92.3 → **90.0 pkt** (`-2.3`) |

### 2.1b. 🩸 Autopodatek Frakcji (Self-Harm)
Karty, których wyłączenie **podnosi** win share własnej frakcji. Gracz zauważy je jako haracz, nawet gdy stół 4P jest równy dzięki temu haraczowi.

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kb-04` **Faworyt Dworu** | Korona & Borgiowie | 4zł / 3☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 26.4% → **35.4%** | **`+9.0%`** | 92.3 → **65.4 pkt** (`-26.9`) |
| `caa-02` **Złoto z Kryjówki** | Cienie Al-Andalus | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.2% → **29.2%** | **`+5.0%`** | 92.3 → **83.2 pkt** (`-9.1`) |
| `caa-11` **Nocna Zmiana Warty** | Cienie Al-Andalus | 2zł / 2☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.2% → **29.0%** | **`+4.8%`** | 92.3 → **84.5 pkt** (`-7.8`) |
| `gc-01` **Przekupiony Strażnik** | Gildia Cieni | 1zł / 3☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.2% → **27.7%** | **`+3.5%`** | 92.3 → **87.6 pkt** (`-4.7`) |
| `gc-03` **Podrzucenie Księgi** | Gildia Cieni | 1zł / 3☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.2% → **27.3%** | **`+3.1%`** | 92.3 → **89.3 pkt** (`-3.0`) |
| `so-03` **Podejrzenie** | Święte Oficjum | 1zł / 2☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.6% → **27.2%** | **`+2.6%`** | 92.3 → **89.0 pkt** (`-3.3`) |
| `so-12` **Straż Trybunalska** | Święte Oficjum | 1zł / 3☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.6% → **27.2%** | **`+2.6%`** | 92.3 → **88.2 pkt** (`-4.1`) |

### 2.2. ⚠️ Karty Destabilizujące Kanon 4P (Disruptors)
Karty, których wyłączenie podnosi 4P Score ($\Delta \text{4P} \ge +1.5$ pkt):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *Brak kart destabilizujących* | - | - | - | - | - | - |

### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich 60 Kart Frakcji w Kanonie 4P

| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Play-Rate | Faction Win Share 4P | $\Delta$ Frakcji | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `caa-01` | **Przejście Podziemiami** | Cienie Al-Andalus | 0 | 0 | 1.00 | 24.2% → 27.5% | `+3.3%` | 87.6 | `-4.7` | 5.82 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-04` | **Fałszywy Trop** | Cienie Al-Andalus | 0 | 0 | 0.88 | 24.2% → 29.1% | `+4.9%` | 83.6 | `-8.7` | 5.80 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-05` | **Ukryty Kurier** | Cienie Al-Andalus | 0 | 0 | 1.04 | 24.2% → 12.9% | `-11.3%` | 59.7 | `-32.6` | 6.07 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `caa-07` | **Szantaż Bractwa** | Cienie Al-Andalus | 0 | 0 | 0.88 | 24.2% → 28.9% | `+4.7%` | 83.9 | `-8.4` | 5.79 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-06` | **Ucieczka z Lochów** | Cienie Al-Andalus | 1 | 0 | 0.87 | 24.2% → 21.2% | `-3.0%` | 84.1 | `-8.2` | 5.87 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `caa-08` | **Kaptur Nocy** | Cienie Al-Andalus | 1 | 0 | 1.01 | 24.2% → 28.6% | `+4.4%` | 84.2 | `-8.1` | 5.81 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-09` | **Kurier Relikwii** | Cienie Al-Andalus | 1 | 0 | 0.96 | 24.2% → 29.3% | `+5.1%` | 83.6 | `-8.7` | 5.79 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-12` | **Skrytka w Murach** | Cienie Al-Andalus | 1 | 0 | 0.46 | 24.2% → 29.1% | `+4.9%` | 84.1 | `-8.2` | 5.80 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `caa-02` | **Złoto z Kryjówki** | Cienie Al-Andalus | 2 | 0 | 0.00 | 24.2% → 29.2% | `+5.0%` | 83.2 | `-9.1` | 5.78 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-03` | **Cień na Rynku** | Cienie Al-Andalus | 2 | 1 | 0.76 | 24.2% → 32.1% | `+7.9%` | 73.6 | `-18.7` | 5.84 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-11` | **Nocna Zmiana Warty** | Cienie Al-Andalus | 2 | 2 | 0.00 | 24.2% → 29.0% | `+4.8%` | 84.5 | `-7.8` | 5.81 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-10` | **Echo Alhambry** | Cienie Al-Andalus | 3 | 0 | 1.02 | 24.2% → 4.3% | `-19.9%` | 40.2 | `-52.1` | 6.14 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `gc-02` | **Czarny Rynek** | Gildia Cieni | 0 | 0 | 0.88 | 24.2% → 25.0% | `+0.8%` | 92.2 | `-0.1` | 5.86 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-08` | **Zatrute Złoto** | Gildia Cieni | 0 | 1 | 0.89 | 24.2% → 25.4% | `+1.2%` | 91.8 | `-0.5` | 5.88 | 0.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `gc-11` | **Fałszywe Świadectwo Cechu** | Gildia Cieni | 0 | 2 | 0.41 | 24.2% → 28.5% | `+4.3%` | 85.2 | `-7.1` | 5.84 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `gc-01` | **Przekupiony Strażnik** | Gildia Cieni | 1 | 3 | 0.08 | 24.2% → 27.7% | `+3.5%` | 87.6 | `-4.7` | 5.84 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `gc-03` | **Podrzucenie Księgi** | Gildia Cieni | 1 | 3 | 0.00 | 24.2% → 27.3% | `+3.1%` | 89.3 | `-3.0` | 5.84 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `gc-04` | **Informator** | Gildia Cieni | 1 | 1 | 0.88 | 24.2% → 21.8% | `-2.4%` | 85.9 | `-6.4` | 5.93 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-07` | **Skrytobójstwo** | Gildia Cieni | 1 | 1 | 0.88 | 24.2% → 27.9% | `+3.7%` | 87.8 | `-4.5` | 5.86 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-09` | **Lista Dłużników** | Gildia Cieni | 1 | 0 | 0.89 | 24.2% → 19.6% | `-4.6%` | 78.9 | `-13.4` | 5.92 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `gc-12` | **Złodziejski Zwiad** | Gildia Cieni | 1 | 2 | 0.23 | 24.2% → 28.0% | `+3.8%` | 87.5 | `-4.8` | 5.83 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `gc-05` | **Fałszywy Świadek** | Gildia Cieni | 2 | 1 | 0.00 | 24.2% → 24.1% | `-0.1%` | 91.6 | `-0.7` | 5.89 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `gc-06` | **Szantaż** | Gildia Cieni | 3 | 1 | 0.26 | 24.2% → 26.8% | `+2.6%` | 90.2 | `-2.1` | 5.85 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `gc-10` | **Upadek Domu** | Gildia Cieni | 4 | 0 | 0.88 | 24.2% → 16.2% | `-8.0%` | 65.9 | `-26.4` | 5.95 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-02` | **Pobór Podatków** | Korona & Borgiowie | 0 | 0 | 0.89 | 26.4% → 15.8% | `-10.6%` | 69.1 | `-23.2` | 6.04 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-01` | **Rozkaz Dworu** | Korona & Borgiowie | 1 | 1 | 0.24 | 26.4% → 36.9% | `+10.5%` | 61.2 | `-31.1` | 5.76 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kb-03` | **Plotka Dworska** | Korona & Borgiowie | 1 | 1 | 0.66 | 26.4% → 36.1% | `+9.7%` | 63.0 | `-29.3` | 5.80 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-11` | **Tajny Emisariusz** | Korona & Borgiowie | 1 | 0 | 0.87 | 26.4% → 34.3% | `+7.9%` | 68.5 | `-23.8` | 5.77 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-12` | **Szantaż Salonowy** | Korona & Borgiowie | 1 | 0 | 0.87 | 26.4% → 31.4% | `+5.0%` | 77.5 | `-14.8` | 5.83 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-05` | **List Żelazny** | Korona & Borgiowie | 2 | 0 | 0.87 | 26.4% → 38.5% | `+12.1%` | 56.6 | `-35.7` | 5.69 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-06` | **Areszt Królewski** | Korona & Borgiowie | 2 | 0 | 0.57 | 26.4% → 37.8% | `+11.4%` | 58.6 | `-33.7` | 5.75 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-07` | **Szantaż Pieczęcią** | Korona & Borgiowie | 2 | 0 | 0.72 | 26.4% → 35.8% | `+9.4%` | 64.1 | `-28.2` | 5.74 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-08` | **Przekupstwo Sędziego** | Korona & Borgiowie | 2 | 0 | 0.72 | 26.4% → 35.8% | `+9.4%` | 64.1 | `-28.2` | 5.74 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-09` | **Dekret Królewski** | Korona & Borgiowie | 2 | 0 | 0.90 | 26.4% → 0.6% | `-25.8%` | 35.2 | `-57.1` | 6.19 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-04` | **Faworyt Dworu** | Korona & Borgiowie | 4 | 3 | 0.04 | 26.4% → 35.4% | `+9.0%` | 65.4 | `-26.9` | 5.78 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-10` | **Pieczęć Korony** | Korona & Borgiowie | 4 | 1 | 0.14 | 26.4% → 25.5% | `-0.9%` | 86.4 | `-5.9` | 5.99 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kt-02` | **Transmutacja Złota** | Kabała z Toledo | 0 | 0 | 0.98 | 25.6% → 7.3% | `-18.3%` | 46.2 | `-46.1` | 6.05 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-03` | **Zakazana Wiedza** | Kabała z Toledo | 0 | 2 | 0.81 | 25.6% → 17.9% | `-7.7%` | 67.8 | `-24.5` | 6.17 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-01` | **Ścieżka Wtajemniczenia** | Kabała z Toledo | 1 | 0 | 0.97 | 25.6% → 30.9% | `+5.3%` | 78.1 | `-14.2` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-04` | **Zwierciadło Herezji** | Kabała z Toledo | 1 | 0 | 0.38 | 25.6% → 30.8% | `+5.2%` | 78.8 | `-13.5` | 5.78 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kt-07` | **Archiwum Ukryte** | Kabała z Toledo | 1 | 0 | 0.28 | 25.6% → 30.5% | `+4.9%` | 80.1 | `-12.2` | 5.79 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kt-11` | **Medytacja Sefirot** | Kabała z Toledo | 1 | 0 | 0.98 | 25.6% → 16.7% | `-8.9%` | 70.6 | `-21.7` | 5.83 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-12` | **Strażnik Archiwum** | Kabała z Toledo | 1 | 0 | 0.89 | 25.6% → 29.7% | `+4.1%` | 81.8 | `-10.5` | 5.78 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-05` | **Wskazówka Cyklu** | Kabała z Toledo | 2 | 0 | 0.97 | 25.6% → 17.8% | `-7.8%` | 73.8 | `-18.5` | 5.96 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-06` | **Przesłuchanie Imienia** | Kabała z Toledo | 2 | 0 | 0.81 | 25.6% → 35.6% | `+10.0%` | 64.2 | `-28.1` | 5.74 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-09` | **Fragment Kodeksu** | Kabała z Toledo | 2 | 1 | 0.93 | 25.6% → 21.8% | `-3.8%` | 83.5 | `-8.8` | 6.05 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-08` | **Areszt Wiedzy** | Kabała z Toledo | 3 | 0 | 0.34 | 25.6% → 31.0% | `+5.4%` | 78.5 | `-13.8` | 5.78 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kt-10` | **Pieczęć Salomona** | Kabała z Toledo | 4 | 0 | 0.49 | 25.6% → 0.0% | `-25.6%` | 34.4 | `-57.9` | 6.14 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `so-04` | **Publiczne Ostrzeżenie** | Święte Oficjum | 0 | 0 | 0.86 | 24.6% → 23.8% | `-0.8%` | 88.1 | `-4.2` | 5.85 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-05` | **Wezwanie do Trybunału** | Święte Oficjum | 0 | 1 | 0.00 | 24.6% → 22.6% | `-2.0%` | 88.2 | `-4.1` | 5.94 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `so-08` | **Nasłanie Inkwizytora** | Święte Oficjum | 0 | 0 | 0.87 | 24.6% → 25.0% | `+0.4%` | 90.0 | `-2.3` | 5.85 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-09` | **Świadek Koronny** | Święte Oficjum | 0 | 3 | 0.00 | 24.6% → 26.5% | `+1.9%` | 91.2 | `-1.1` | 5.88 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `so-11` | **Dekret Czystości Wiary** | Święte Oficjum | 0 | 1 | 0.90 | 24.6% → 25.4% | `+0.8%` | 90.8 | `-1.5` | 5.89 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-01` | **Patrol Familiariuszy** | Święte Oficjum | 1 | 2 | 0.32 | 24.6% → 28.2% | `+3.6%` | 85.7 | `-6.6` | 5.87 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `so-02` | **Skarbiec Trybunału** | Święte Oficjum | 1 | 2 | 0.56 | 24.6% → 25.9% | `+1.3%` | 91.1 | `-1.2` | 5.90 | 0.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `so-03` | **Podejrzenie** | Święte Oficjum | 1 | 2 | 0.19 | 24.6% → 27.2% | `+2.6%` | 89.0 | `-3.3` | 5.88 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `so-07` | **Przesłuchanie Oficjum** | Święte Oficjum | 1 | 0 | 0.84 | 24.6% → 26.6% | `+2.0%` | 88.0 | `-4.3` | 5.81 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-12` | **Straż Trybunalska** | Święte Oficjum | 1 | 3 | 0.13 | 24.6% → 27.2% | `+2.6%` | 88.2 | `-4.1` | 5.88 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `so-06` | **Areszt Trybunalski** | Święte Oficjum | 2 | 0 | 0.90 | 24.6% → 26.9% | `+2.3%` | 89.7 | `-2.6` | 5.85 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-10` | **Oczyść Miasto** | Święte Oficjum | 5 | 1 | 0.86 | 24.6% → 20.9% | `-3.7%` | 81.8 | `-10.5` | 6.05 | 0.0% | 👑 FILAR KANONU (Core Keystone) |

### 2.4. 🎯 Monokultura Talii (Deck Concentration Index)

Jak mocno skoncentrowane jest zagrywanie kart w obrębie każdej frakcji.
Wskaźnik HHI (Herfindahl–Hirschman Index) mierzy koncentrację: HHI = 1.0 oznacza, że 100% zagrań to 1 karta; HHI ≈ 1/N oznacza idealnie równomierny rozkład.

| Frakcja | Kart w Talii | Top Karta (Play-Rate) | Top 2 (%) | HHI | Ocena |
| :--- | :---: | :--- | :---: | :---: | :--- |
| Cienie Al-Andalus | 12 | `caa-05` (1.04) | 23.2% | 0.103 | 🟢 Zdrowy rozkład |
| Gildia Cieni | 12 | `gc-08` (0.89) | 28.3% | 0.126 | 🟢 Zdrowy rozkład |
| Korona & Borgiowie | 12 | `kb-09` (0.90) | 23.9% | 0.102 | 🟢 Zdrowy rozkład |
| Kabała z Toledo | 12 | `kt-11` (0.98) | 22.2% | 0.094 | 🟢 Zdrowy rozkład |
| Święte Oficjum | 12 | `so-11` (0.90) | 28.0% | 0.122 | 🟢 Zdrowy rozkład |

---

## 3. ⏳ Warstwa II — Kronika Dziejów w 4P (Ablacja 8 Kart Wydarzeń Czasu)

Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans w 4P:

| ID | Karta Wydarzenia | 4P Score | $\Delta$ 4P | Średnia Er | Deadlock % | Status Roli w Kronice |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `time-01` | **Kapitulacja Grenady** | 92.3 → 🟢 ** 93.1** (`⬆️ +0.8`) | `+0.8 pkt` | 5.91 Er | 0.0% | ⚖️ Neutralna Kronika |
| `time-02` | **Godzina Policyjna** | 92.3 → 🟡 ** 89.4** (`🔻 -2.9`) | `-2.9 pkt` | 5.87 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-03` | **Flota Odkrywców** | 92.3 → 🟢 ** 91.9** (`🔻 -0.4`) | `-0.4 pkt` | 5.95 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-04` | **Rewizja w Dzielnicach** | 92.3 → 🟢 ** 93.5** (`⬆️ +1.2`) | `+1.2 pkt` | 5.92 Er | 0.0% | ⚠️ Spowalniacz |
| `time-05` | **Gorączka Donosów** | 92.3 → 🟡 ** 89.1** (`🔻 -3.2`) | `-3.2 pkt` | 5.88 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-06` | **Nocna Obława** | 92.3 → 🟡 ** 89.1** (`🔻 -3.2`) | `-3.2 pkt` | 5.87 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-07` | **Bunt w Lochach** | 92.3 → 🟡 ** 88.5** (`🔻 -3.8`) | `-3.8 pkt` | 5.87 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-08` | **Święte Przymierze** | 92.3 → 🟡 ** 89.4** (`🔻 -2.9`) | `-2.9 pkt` | 5.77 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-09` | **Jarmark Królewski** | 92.3 → 🟢 ** 90.1** (`🔻 -2.2`) | `-2.2 pkt` | 5.88 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-10` | **Amnestia Biskupia** | 92.3 → 🟡 ** 88.1** (`🔻 -4.2`) | `-4.2 pkt` | 5.87 Er | 0.0% | 🟢 Stabilizator tempa |

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
| **Szlak Morski: era 4 → nigdy (99)** | Poziom 4: Warianty i Modyfikatory | 92.3 → 🟡 ** 89.3** (`🔻 -3.0`) | `-3.0 pkt` | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |

### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)

| Badany Podsystem / Modyfikator L1 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Limit Er: 15 → 7 (skrajna presja)** | 92.3 → 🟡 ** 84.6** (`🔻 -7.7`) | `-7.7 pkt` | 5.73 Er | 11.3% | 2.8% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Próg Oskarżenia: 6 → 1** | 92.3 → 🔴 ** 24.1** (`🔻 -68.2`) | `-68.2 pkt` | 5.22 Er | 0.0% | 1.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Oskarżenia: 6 → 12** | 92.3 → 🔴 ** 17.0** (`🔻 -75.3`) | `-75.3 pkt` | 6.78 Er | 0.9% | 3.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 0zł (wyłączenie)** | 92.3 → 🔴 ** 55.1** (`🔻 -37.2`) | `-37.2 pkt` | 6.52 Er | 0.0% | 10.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 8zł** | 92.3 → 🔴 ** 28.7** (`🔻 -63.6`) | `-63.6 pkt` | 5.19 Er | 0.0% | 0.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 1** | 92.3 → 🔴 ** 29.7** (`🔻 -62.6`) | `-62.6 pkt` | 6.85 Er | 0.0% | 3.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 6** | 92.3 → 🟠 ** 70.3** (`🔻 -22.0`) | `-22.0 pkt` | 5.52 Er | 0.0% | 2.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 1** | 92.3 → 🔴 **  5.5** (`🔻 -86.8`) | `-86.8 pkt` | 8.85 Er | 1.1% | 36.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 10** | 92.3 → 🔴 **  7.0** (`🔻 -85.3`) | `-85.3 pkt` | 4.62 Er | 0.0% | 0.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: cooldown 3 → 0 (co erę)** | 92.3 → 🔴 ** 13.2** (`🔻 -79.1`) | `-79.1 pkt` | 4.97 Er | 0.0% | 3.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: całkowite wyłączenie** | 92.3 → 🟠 ** 69.3** (`🔻 -23.0`) | `-23.0 pkt` | 6.04 Er | 0.0% | 2.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Akcja Gospodarcza: 0zł (brak zysku złota)** | 92.3 → 🟠 ** 65.5** (`🔻 -26.8`) | `-26.8 pkt` | 5.95 Er | 0.0% | 4.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Akcja Gospodarcza: 1 → 2 (podwojenie)** | 92.3 → 🔴 ** 47.7** (`🔻 -44.6`) | `-44.6 pkt` | 5.74 Er | 0.0% | 2.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Obserwowanej: 3 → 2 (skrajna presja)** | 92.3 → 🟠 ** 71.9** (`🔻 -20.4`) | `-20.4 pkt` | 5.74 Er | 0.0% | 2.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)

| Badany Warunek Zwycięstwa L2 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: stosy 7 → 1** | 92.3 → 🔴 ** 18.2** (`🔻 -74.1`) | `-74.1 pkt` | 3.82 Er | 0.0% | 2.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: stosy 7 → 14** | 92.3 → 🟠 ** 69.6** (`🔻 -22.7`) | `-22.7 pkt` | 5.97 Er | 0.0% | 2.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 1** | 92.3 → 🔴 ** 17.9** (`🔻 -74.4`) | `-74.4 pkt` | 3.46 Er | 0.0% | 2.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 6** | 92.3 → 🔴 ** 57.2** (`🔻 -35.1`) | `-35.1 pkt` | 5.98 Er | 0.0% | 2.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Cienie: relikwie 2 → 4** | 92.3 → 🔴 ** 33.9** (`🔻 -58.4`) | `-58.4 pkt` | 6.20 Er | 0.0% | 2.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: dekrety 2 → 4** | 92.3 → 🔴 ** 34.3** (`🔻 -58.0`) | `-58.0 pkt` | 6.19 Er | 0.0% | 2.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: wymóg haków 2 → 0** | 92.3 → 🟠 ** 70.6** (`🔻 -21.7`) | `-21.7 pkt` | 5.83 Er | 0.0% | 2.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: wymóg haków 2 → 4** | 92.3 → 🔴 ** 34.2** (`🔻 -58.1`) | `-58.1 pkt` | 6.19 Er | 0.0% | 2.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: fragmenty 3 → 1** | 92.3 → 🔴 ** 55.8** (`🔻 -36.5`) | `-36.5 pkt` | 6.09 Er | 0.0% | 3.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: fragmenty 3 → 6** | 92.3 → 🔴 ** 34.3** (`🔻 -58.0`) | `-58.0 pkt` | 6.16 Er | 0.0% | 2.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 9 → 1** | 92.3 → 🔴 ** 17.3** (`🔻 -75.0`) | `-75.0 pkt` | 2.98 Er | 0.0% | 1.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 9 → 18** | 92.3 → 🔴 ** 31.5** (`🔻 -60.8`) | `-60.8 pkt` | 6.14 Er | 0.0% | 2.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)

| Badany Wariant / Modyfikator L4 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kronika Dziejów: całkowite wyłączenie** | 92.3 → 🟠 ** 71.1** (`🔻 -21.2`) | `-21.2 pkt` | 5.95 Er | 0.0% | 3.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kronika Dziejów: co 3 Ery (spowolniony zegar)** | 92.3 → 🟠 ** 79.3** (`🔻 -13.0`) | `-13.0 pkt` | 5.95 Er | 0.0% | 3.2% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Inkwizytor Patrol: ruch 1 → 0 (wyłączenie)** | 92.3 → 🔴 ** 33.0** (`🔻 -59.3`) | `-59.3 pkt` | 6.55 Er | 0.1% | 2.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Inkwizytor Patrol: ruch x2 (podwojona prędkość)** | 92.3 → 🟡 ** 83.9** (`🔻 -8.4`) | `-8.4 pkt` | 5.83 Er | 0.0% | 2.8% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Szlak Morski: era 4 → nigdy (99)** | 92.3 → 🟡 ** 89.3** (`🔻 -3.0`) | `-3.0 pkt` | 5.92 Er | 0.0% | 2.8% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |

---

## 5. 👥 Warstwa IV — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych. Kolumna win share to HUD kanonu; setup+witalność to stary blend (kara martwej ścieżki).

| Nieobecna Frakcja | Setup Testowy | Win share | Setup+witalność | Diagnoza |
| :--- | :--- | :---: | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`85.2`** | `85.2` | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`95.0`** | `95.0` | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`97.6`** | `97.6` | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`91.6`** | `91.6` | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`92.1`** | `92.1` | Brak presji stosów i bezpośredniego Inkwizytora |