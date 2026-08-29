# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v1.0-alpha.99

**Wersja Gry:** `v1.0-alpha.99` | **Data Badania:** 2026-08-29 22:50 | **Próba:** 5000 gier/setup (25000 gier na wariant) | **Ziarno:** 42
**4P Score (win share):** 🟢 ** 93.9** pkt | **Witalność (osobna kara):** `0.000` | **Śr. Er:** `5.76` | **Deadlocki:** `0.0%` | **Pas Biedy:** `4.5%`
**Udziały 4P:** CAA 24.3% · GC 25.0% · KB 24.4% · KT 25.1% · SO 26.1%

Klasyfikacja L1/L2/L4 i Δ 4P liczą wyłącznie równość win share (`calculate_balance_score`). Kara witalności jest osobno.

---

## 0. Wady z tej próby (nie HUD win share)

Kubełki klasyfikatora i ostrzeżenia witalności z bieżącego runu.

- **Autopodatek (SELF_HARM):** 3/60
- **DEAD_WEIGHT:** `gc-05` Fałszywy Świadek, `gc-08` Zatrute Złoto, `so-05` Wezwanie do Trybunału
- **Karty Kroniki |Δ4P| ≤ 0.8:** 4/10
- **Ablacja całej Kroniki (`L4_NO_TIME_DECK`):** Δ4P -29.6 (STABILIZER)
- **Mechaniki WEAK/NEUTRAL:** Szlak Morski: era 4 → nigdy (99)

---

## 1. 🗺️ Podsumowanie Ekosystemu Kart Kanonu 4P (Matryca Wpływu Kart, 60 kart)

Rozkład wszystkich 60 kart frakcyjnych w matrycy **Wpływ na Frakcję ($\Delta \text{Share}$)** vs **Wpływ na Kanon 4P ($\Delta \text{4P Score}$)**:

| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |
| :--- | :---: | :---: | :--- | :--- |
| 🩸 **Autopodatek (Self-Harm)** | **3** | 5.0% | Wyłączenie **podnosi** win share własnej frakcji — karta jest haraczem, nie silnikiem | **Rework / osłabienie kosztu, nie filar** |
| 🔄 **Rozcieńczalnik Talii (Tempo Filler)** | **8** | 13.3% | Normalna karta tempa — ablacja fałszywie flaguje ją jako autopodatek z powodu odchudzenia talii | **Normalny element deckbuildingu** |
| 💤 **Karta Pasywna (Dead Weight)** | **3** | 5.0% | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia lub wycięcia** |
| ⚠️ **Karta Destabilizująca (Disruptor)** | **0** | 0.0% | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |
| ⚖️ **Zbalansowane Narzędzie** | **17** | 28.3% | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Narzędzie, nie złoty środek całego kanonu** |
| 👑 / ⚓ **Filar / Kotwica Kanonu** | **29** | 48.3% | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |

---

## 2. 🃏 Warstwa I — Szczegółowa Analiza 60 Kart Frakcji w Kanonie 4P

### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)
Karty, których brak powoduje spadek wyniku Kanonu 4P o $\ge 4.0$ pkt lub załamanie winrate frakcji o $\ge 4.0\%$ — **bez** autopodatków (te są w 2.1b):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kt-10` **Pieczęć Salomona** | Kabała z Toledo | 4zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.1% → **0.0%** | **`-25.1%`** | 93.9 → **34.7 pkt** (`-59.2`) |
| `kb-09` **Dekret Królewski** | Korona & Borgiowie | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.4% → **1.0%** | **`-23.4%`** | 93.9 → **35.0 pkt** (`-58.9`) |
| `caa-10` **Echo Alhambry** | Cienie Al-Andalus | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.3% → **4.5%** | **`-19.8%`** | 93.9 → **38.9 pkt** (`-55.0`) |
| `kt-02` **Transmutacja Złota** | Kabała z Toledo | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.1% → **8.2%** | **`-16.9%`** | 93.9 → **48.3 pkt** (`-45.6`) |
| `caa-05` **Ukryty Kurier** | Cienie Al-Andalus | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.3% → **13.3%** | **`-11.0%`** | 93.9 → **59.6 pkt** (`-34.3`) |
| `kt-11` **Medytacja Sefirot** | Kabała z Toledo | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.1% → **15.7%** | **`-9.4%`** | 93.9 → **66.1 pkt** (`-27.8`) |
| `kb-02` **Pobór Podatków** | Korona & Borgiowie | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.4% → **15.1%** | **`-9.3%`** | 93.9 → **66.2 pkt** (`-27.7`) |
| `kb-10` **Pieczęć Korony** | Korona & Borgiowie | 4zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 24.4% → **20.7%** | **`-3.7%`** | 93.9 → **80.4 pkt** (`-13.5`) |
| `kt-05` **Wskazówka Cyklu** | Kabała z Toledo | 1zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 25.1% → **19.4%** | **`-5.7%`** | 93.9 → **80.4 pkt** (`-13.5`) |
| `kt-03` **Zakazana Wiedza** | Kabała z Toledo | 0zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 25.1% → **20.5%** | **`-4.6%`** | 93.9 → **80.7 pkt** (`-13.2`) |
| `gc-10` **Upadek Domu** | Gildia Cieni | 4zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 25.0% → **20.8%** | **`-4.2%`** | 93.9 → **81.9 pkt** (`-12.0`) |
| `gc-09` **Lista Dłużników** | Gildia Cieni | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.0% → **20.7%** | **`-4.3%`** | 93.9 → **82.0 pkt** (`-11.9`) |
| `caa-06` **Ucieczka z Lochów** | Cienie Al-Andalus | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.3% → **21.1%** | **`-3.2%`** | 93.9 → **83.7 pkt** (`-10.2`) |
| `so-10` **Oczyść Miasto** | Święte Oficjum | 5zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 26.1% → **21.4%** | **`-4.7%`** | 93.9 → **85.3 pkt** (`-8.6`) |
| `so-04` **Publiczne Ostrzeżenie** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 26.1% → **25.1%** | **`-1.0%`** | 93.9 → **87.3 pkt** (`-6.6`) |
| `so-03` **Podejrzenie** | Święte Oficjum | 2zł / 4☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 26.1% → **26.7%** | **`+0.6%`** | 93.9 → **87.7 pkt** (`-6.2`) |
| `so-08` **Nasłanie Inkwizytora** | Święte Oficjum | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 26.1% → **25.4%** | **`-0.7%`** | 93.9 → **87.9 pkt** (`-6.0`) |
| `so-01` **Patrol Familiariuszy** | Święte Oficjum | 1zł / 2☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 26.1% → **27.7%** | **`+1.6%`** | 93.9 → **88.2 pkt** (`-5.7`) |
| `gc-04` **Informator** | Gildia Cieni | 1zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.0% → **22.6%** | **`-2.4%`** | 93.9 → **88.7 pkt** (`-5.2`) |
| `so-07` **Przesłuchanie Oficjum** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 26.1% → **26.6%** | **`+0.5%`** | 93.9 → **88.7 pkt** (`-5.2`) |
| `kt-09` **Fragment Kodeksu** | Kabała z Toledo | 1zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.1% → **23.5%** | **`-1.6%`** | 93.9 → **89.0 pkt** (`-4.9`) |
| `so-06` **Areszt Trybunalski** | Święte Oficjum | 2zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 26.1% → **26.8%** | **`+0.7%`** | 93.9 → **89.1 pkt** (`-4.8`) |
| `gc-07` **Skrytobójstwo** | Gildia Cieni | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.0% → **26.3%** | **`+1.3%`** | 93.9 → **89.5 pkt** (`-4.4`) |
| `gc-06` **Szantaż** | Gildia Cieni | 3zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.0% → **25.2%** | **`+0.2%`** | 93.9 → **91.3 pkt** (`-2.6`) |
| `so-12` **Straż Trybunalska** | Święte Oficjum | 1zł / 2☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 26.1% → **27.2%** | **`+1.1%`** | 93.9 → **91.3 pkt** (`-2.6`) |
| `gc-03` **Podrzucenie Księgi** | Gildia Cieni | 1zł / 2☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.0% → **26.3%** | **`+1.3%`** | 93.9 → **91.4 pkt** (`-2.5`) |
| `so-09` **Świadek Koronny** | Święte Oficjum | 1zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 26.1% → **25.8%** | **`-0.3%`** | 93.9 → **91.5 pkt** (`-2.4`) |
| `so-02` **Skarbiec Trybunału** | Święte Oficjum | 1zł / 2☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 26.1% → **26.1%** | **`+0.0%`** | 93.9 → **91.7 pkt** (`-2.2`) |
| `gc-02` **Czarny Rynek** | Gildia Cieni | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.0% → **25.9%** | **`+0.9%`** | 93.9 → **91.8 pkt** (`-2.1`) |

### 2.1b. 🩸 Autopodatek Frakcji (Self-Harm)
Karty, których wyłączenie **podnosi** win share własnej frakcji. Gracz zauważy je jako haracz, nawet gdy stół 4P jest równy dzięki temu haraczowi.

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kb-08` **Przekupstwo Sędziego** | Korona & Borgiowie | 3zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.4% → **33.8%** | **`+9.4%`** | 93.9 → **69.6 pkt** (`-24.3`) |
| `caa-01` **Przejście Podziemiami** | Cienie Al-Andalus | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.3% → **29.1%** | **`+4.8%`** | 93.9 → **84.4 pkt** (`-9.5`) |
| `kt-01` **Rytuał Przejścia** | Kabała z Toledo | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.1% → **29.3%** | **`+4.2%`** | 93.9 → **84.5 pkt** (`-9.4`) |

### 2.2. ⚠️ Karty Destabilizujące Kanon 4P (Disruptors)
Karty, których wyłączenie podnosi 4P Score ($\Delta \text{4P} \ge +1.5$ pkt):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *Brak kart destabilizujących* | - | - | - | - | - | - |

### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich 60 Kart Frakcji w Kanonie 4P

| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Play-Rate | Faction Win Share 4P | $\Delta$ Frakcji | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `caa-02` | **Złoto z Kryjówki** | Cienie Al-Andalus | 0 | 0 | 0.23 | 24.3% → 29.4% | `+5.1%` | 83.0 | `-10.9` | 5.69 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `caa-03` | **Cień na Rynku** | Cienie Al-Andalus | 0 | 1 | 0.93 | 24.3% → 32.8% | `+8.5%` | 71.1 | `-22.8` | 5.78 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-04` | **Fałszywy Trop** | Cienie Al-Andalus | 0 | 0 | 0.97 | 24.3% → 30.0% | `+5.7%` | 81.2 | `-12.7` | 5.68 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-05` | **Ukryty Kurier** | Cienie Al-Andalus | 0 | 0 | 1.01 | 24.3% → 13.3% | `-11.0%` | 59.6 | `-34.3` | 5.94 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `caa-01` | **Przejście Podziemiami** | Cienie Al-Andalus | 1 | 1 | 0.13 | 24.3% → 29.1% | `+4.8%` | 84.4 | `-9.5` | 5.71 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-12` | **Skrytka w Murach** | Cienie Al-Andalus | 1 | 0 | 0.92 | 24.3% → 30.7% | `+6.4%` | 78.6 | `-15.3` | 5.66 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-06` | **Ucieczka z Lochów** | Cienie Al-Andalus | 0 | 0 | 0.67 | 24.3% → 21.1% | `-3.2%` | 83.7 | `-10.2` | 5.76 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `caa-07` | **Szantaż Bractwa** | Cienie Al-Andalus | 0 | 0 | 0.48 | 24.3% → 29.1% | `+4.8%` | 83.7 | `-10.2` | 5.68 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `caa-11` | **Nocna Zmiana Warty** | Cienie Al-Andalus | 1 | 0 | 0.67 | 24.3% → 28.2% | `+3.9%` | 87.2 | `-6.7` | 5.70 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-08` | **Kaptur Nocy** | Cienie Al-Andalus | 2 | 0 | 0.80 | 24.3% → 29.0% | `+4.7%` | 84.3 | `-9.6` | 5.68 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-09` | **Kurier Relikwii** | Cienie Al-Andalus | 0 | 0 | 0.93 | 24.3% → 30.4% | `+6.1%` | 79.7 | `-14.2` | 5.66 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-10` | **Echo Alhambry** | Cienie Al-Andalus | 2 | 0 | 0.99 | 24.3% → 4.5% | `-19.8%` | 38.9 | `-55.0` | 6.02 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `gc-02` | **Czarny Rynek** | Gildia Cieni | 0 | 0 | 0.78 | 25.0% → 25.9% | `+0.9%` | 91.8 | `-2.1` | 5.75 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-12` | **Złodziejski Zwiad** | Gildia Cieni | 0 | 2 | 0.44 | 25.0% → 28.1% | `+3.1%` | 85.6 | `-8.3` | 5.74 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `gc-01` | **Przekupiony Strażnik** | Gildia Cieni | 1 | 1 | 0.47 | 25.0% → 27.0% | `+2.0%` | 89.2 | `-4.7` | 5.75 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `gc-03` | **Podrzucenie Księgi** | Gildia Cieni | 1 | 2 | 0.08 | 25.0% → 26.3% | `+1.3%` | 91.4 | `-2.5` | 5.76 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-04` | **Informator** | Gildia Cieni | 1 | 1 | 0.80 | 25.0% → 22.6% | `-2.4%` | 88.7 | `-5.2` | 5.81 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-05` | **Fałszywy Świadek** | Gildia Cieni | 1 | 0 | 0.00 | 25.0% → 25.1% | `+0.1%` | 91.9 | `-2.0` | 5.77 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `gc-07` | **Skrytobójstwo** | Gildia Cieni | 0 | 0 | 0.79 | 25.0% → 26.3% | `+1.3%` | 89.5 | `-4.4` | 5.80 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-11` | **Fałszywe Świadectwo Cechu** | Gildia Cieni | 0 | 2 | 0.31 | 25.0% → 27.2% | `+2.2%` | 89.6 | `-4.3` | 5.74 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `gc-08` | **Zatrute Złoto** | Gildia Cieni | 1 | 2 | 0.00 | 25.0% → 26.0% | `+1.0%` | 90.4 | `-3.5` | 5.75 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `gc-06` | **Szantaż** | Gildia Cieni | 3 | 1 | 0.43 | 25.0% → 25.2% | `+0.2%` | 91.3 | `-2.6` | 5.77 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-09` | **Lista Dłużników** | Gildia Cieni | 1 | 0 | 0.79 | 25.0% → 20.7% | `-4.3%` | 82.0 | `-11.9` | 5.80 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `gc-10` | **Upadek Domu** | Gildia Cieni | 4 | 2 | 0.46 | 25.0% → 20.8% | `-4.2%` | 81.9 | `-12.0` | 5.84 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-01` | **Rozkaz Dworu** | Korona & Borgiowie | 1 | 1 | 0.26 | 24.4% → 35.3% | `+10.9%` | 65.0 | `-28.9` | 5.67 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kb-02` | **Pobór Podatków** | Korona & Borgiowie | 1 | 0 | 0.84 | 24.4% → 15.1% | `-9.3%` | 66.2 | `-27.7` | 5.87 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-03` | **Plotka Dworska** | Korona & Borgiowie | 1 | 1 | 0.64 | 24.4% → 34.8% | `+10.4%` | 65.4 | `-28.5` | 5.68 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-11` | **Tajny Emisariusz** | Korona & Borgiowie | 1 | 0 | 0.83 | 24.4% → 33.2% | `+8.8%` | 71.6 | `-22.3` | 5.66 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-04` | **Faworyt Dworu** | Korona & Borgiowie | 2 | 0 | 0.73 | 24.4% → 31.2% | `+6.8%` | 77.7 | `-16.2` | 5.67 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-05` | **List Żelazny** | Korona & Borgiowie | 2 | 1 | 0.82 | 24.4% → 33.1% | `+8.7%` | 71.5 | `-22.4` | 5.61 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-12` | **Szantaż Salonowy** | Korona & Borgiowie | 1 | 2 | 0.82 | 24.4% → 29.3% | `+4.9%` | 83.4 | `-10.5` | 5.72 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-06` | **Areszt Królewski** | Korona & Borgiowie | 2 | 0 | 0.41 | 24.4% → 35.2% | `+10.8%` | 65.5 | `-28.4` | 5.66 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kb-07` | **Szantaż Pieczęcią** | Korona & Borgiowie | 2 | 0 | 0.61 | 24.4% → 31.9% | `+7.5%` | 75.7 | `-18.2` | 5.68 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-08` | **Przekupstwo Sędziego** | Korona & Borgiowie | 3 | 1 | 0.12 | 24.4% → 33.8% | `+9.4%` | 69.6 | `-24.3` | 5.67 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-09` | **Dekret Królewski** | Korona & Borgiowie | 2 | 0 | 0.85 | 24.4% → 1.0% | `-23.4%` | 35.0 | `-58.9` | 6.01 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-10` | **Pieczęć Korony** | Korona & Borgiowie | 4 | 1 | 0.16 | 24.4% → 20.7% | `-3.7%` | 80.4 | `-13.5` | 5.89 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-02` | **Transmutacja Złota** | Kabała z Toledo | 0 | 0 | 0.95 | 25.1% → 8.2% | `-16.9%` | 48.3 | `-45.6` | 5.91 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-03` | **Zakazana Wiedza** | Kabała z Toledo | 0 | 2 | 0.81 | 25.1% → 20.5% | `-4.6%` | 80.7 | `-13.2` | 6.02 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-01` | **Rytuał Przejścia** | Kabała z Toledo | 1 | 1 | 0.05 | 25.1% → 29.3% | `+4.2%` | 84.5 | `-9.4` | 5.68 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-04` | **Zwierciadło Herezji** | Kabała z Toledo | 1 | 0 | 0.52 | 25.1% → 30.1% | `+5.0%` | 83.0 | `-10.9` | 5.66 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-05` | **Wskazówka Cyklu** | Kabała z Toledo | 1 | 1 | 0.96 | 25.1% → 19.4% | `-5.7%` | 80.4 | `-13.5` | 5.95 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-12` | **Strażnik Archiwum** | Kabała z Toledo | 1 | 0 | 0.91 | 25.1% → 29.5% | `+4.4%` | 84.7 | `-9.2` | 5.65 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-07` | **Archiwum Ukryte** | Kabała z Toledo | 1 | 0 | 0.30 | 25.1% → 29.4% | `+4.3%` | 85.2 | `-8.7` | 5.68 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kt-08` | **Areszt Wiedzy** | Kabała z Toledo | 1 | 0 | 0.88 | 25.1% → 28.8% | `+3.7%` | 86.2 | `-7.7` | 5.70 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-06` | **Przesłuchanie Imienia** | Kabała z Toledo | 2 | 0 | 0.83 | 25.1% → 35.1% | `+10.0%` | 67.3 | `-26.6` | 5.60 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-11` | **Medytacja Sefirot** | Kabała z Toledo | 2 | 0 | 0.92 | 25.1% → 15.7% | `-9.4%` | 66.1 | `-27.8` | 5.72 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-09` | **Fragment Kodeksu** | Kabała z Toledo | 1 | 1 | 0.96 | 25.1% → 23.5% | `-1.6%` | 89.0 | `-4.9` | 5.89 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kt-10` | **Pieczęć Salomona** | Kabała z Toledo | 4 | 0 | 0.52 | 25.1% → 0.0% | `-25.1%` | 34.7 | `-59.2` | 6.03 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `so-05` | **Wezwanie do Trybunału** | Święte Oficjum | 0 | 4 | 0.00 | 26.1% → 22.1% | `-4.0%` | 86.2 | `-7.7` | 5.81 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `so-01` | **Patrol Familiariuszy** | Święte Oficjum | 1 | 2 | 0.24 | 26.1% → 27.7% | `+1.6%` | 88.2 | `-5.7` | 5.78 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-02` | **Skarbiec Trybunału** | Święte Oficjum | 1 | 2 | 0.50 | 26.1% → 26.1% | `+0.0%` | 91.7 | `-2.2` | 5.80 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-04` | **Publiczne Ostrzeżenie** | Święte Oficjum | 1 | 0 | 0.88 | 26.1% → 25.1% | `-1.0%` | 87.3 | `-6.6` | 5.72 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-12` | **Straż Trybunalska** | Święte Oficjum | 1 | 2 | 0.25 | 26.1% → 27.2% | `+1.1%` | 91.3 | `-2.6` | 5.79 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-03` | **Podejrzenie** | Święte Oficjum | 2 | 4 | 0.30 | 26.1% → 26.7% | `+0.6%` | 87.7 | `-6.2` | 5.82 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-08` | **Nasłanie Inkwizytora** | Święte Oficjum | 0 | 0 | 0.87 | 26.1% → 25.4% | `-0.7%` | 87.9 | `-6.0` | 5.74 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-11` | **Dekret Czystości Wiary** | Święte Oficjum | 0 | 1 | 0.92 | 26.1% → 26.5% | `+0.4%` | 93.3 | `-0.6` | 5.78 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-07` | **Przesłuchanie Oficjum** | Święte Oficjum | 1 | 0 | 0.85 | 26.1% → 26.6% | `+0.5%` | 88.7 | `-5.2` | 5.69 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-09` | **Świadek Koronny** | Święte Oficjum | 1 | 1 | 0.15 | 26.1% → 25.8% | `-0.3%` | 91.5 | `-2.4` | 5.79 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-06` | **Areszt Trybunalski** | Święte Oficjum | 2 | 0 | 0.92 | 26.1% → 26.8% | `+0.7%` | 89.1 | `-4.8` | 5.72 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-10` | **Oczyść Miasto** | Święte Oficjum | 5 | 1 | 0.78 | 26.1% → 21.4% | `-4.7%` | 85.3 | `-8.6` | 5.91 | 0.0% | 👑 FILAR KANONU (Core Keystone) |

### 2.4. 🎯 Monokultura Talii (Deck Concentration Index)

Jak mocno skoncentrowane jest zagrywanie kart w obrębie każdej frakcji.
Wskaźnik HHI (Herfindahl–Hirschman Index) mierzy koncentrację: HHI = 1.0 oznacza, że 100% zagrań to 1 karta; HHI ≈ 1/N oznacza idealnie równomierny rozkład.

| Frakcja | Kart w Talii | Top Karta (Play-Rate) | Top 2 (%) | HHI | Ocena |
| :--- | :---: | :--- | :---: | :---: | :--- |
| Cienie Al-Andalus | 12 | `caa-05` (1.01) | 22.9% | 0.096 | 🟢 Zdrowy rozkład |
| Gildia Cieni | 12 | `gc-04` (0.80) | 29.7% | 0.119 | 🟢 Zdrowy rozkład |
| Korona & Borgiowie | 12 | `kb-09` (0.85) | 23.8% | 0.100 | 🟢 Zdrowy rozkład |
| Kabała z Toledo | 12 | `kt-09` (0.96) | 22.3% | 0.097 | 🟢 Zdrowy rozkład |
| Święte Oficjum | 12 | `so-06` (0.92) | 27.5% | 0.113 | 🟢 Zdrowy rozkład |

---

## 3. ⏳ Warstwa II — Kronika Dziejów w 4P (Ablacja 8 Kart Wydarzeń Czasu)

Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans w 4P:

| ID | Karta Wydarzenia | 4P Score | $\Delta$ 4P | Średnia Er | Deadlock % | Status Roli w Kronice |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `time-01` | **Kapitulacja Grenady** | 93.9 → 🟢 ** 91.9** (`🔻 -2.0`) | `-2.0 pkt` | 5.80 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-02` | **Godzina Policyjna** | 93.9 → 🟢 ** 93.5** (`🔻 -0.4`) | `-0.4 pkt` | 5.77 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-03` | **Flota Odkrywców** | 93.9 → 🟢 ** 91.6** (`🔻 -2.3`) | `-2.3 pkt` | 5.84 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-04` | **Rewizja w Dzielnicach** | 93.9 → 🟢 ** 90.1** (`🔻 -3.8`) | `-3.8 pkt` | 5.81 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-05` | **Gorączka Donosów** | 93.9 → 🟢 ** 93.6** (`🔻 -0.3`) | `-0.3 pkt` | 5.78 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-06` | **Nocna Obława** | 93.9 → 🟢 ** 93.7** (`🔻 -0.2`) | `-0.2 pkt` | 5.78 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-07` | **Bunt w Lochach** | 93.9 → 🟢 ** 92.9** (`🔻 -1.0`) | `-1.0 pkt` | 5.78 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-08` | **Święte Przymierze** | 93.9 → 🟡 ** 84.4** (`🔻 -9.5`) | `-9.5 pkt` | 5.68 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-09` | **Jarmark Królewski** | 93.9 → 🟢 ** 93.1** (`🔻 -0.8`) | `-0.8 pkt` | 5.79 Er | 0.0% | ⚖️ Neutralna Kronika |
| `time-10` | **Amnestia Biskupia** | 93.9 → 🟢 ** 91.5** (`🔻 -2.4`) | `-2.4 pkt` | 5.76 Er | 0.0% | 🟢 Stabilizator tempa |

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
| **Szlak Morski: era 4 → nigdy (99)** | Poziom 4: Warianty i Modyfikatory | 93.9 → 🟢 ** 92.9** (`🔻 -1.0`) | `-1.0 pkt` | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |

### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)

| Badany Podsystem / Modyfikator L1 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Limit Er: 15 → 7 (skrajna presja)** | 93.9 → 🟡 ** 86.0** (`🔻 -7.9`) | `-7.9 pkt` | 5.64 Er | 9.0% | 4.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Próg Oskarżenia: 7 → 1** | 93.9 → 🔴 ** 26.6** (`🔻 -67.3`) | `-67.3 pkt` | 5.34 Er | 0.0% | 2.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Oskarżenia: 7 → 14** | 93.9 → 🔴 ** 31.6** (`🔻 -62.3`) | `-62.3 pkt` | 6.39 Er | 0.0% | 5.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 0zł (wyłączenie)** | 93.9 → 🔴 ** 48.5** (`🔻 -45.4`) | `-45.4 pkt` | 6.46 Er | 0.0% | 11.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 8zł** | 93.9 → 🔴 ** 31.5** (`🔻 -62.4`) | `-62.4 pkt` | 5.07 Er | 0.0% | 1.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 1** | 93.9 → 🔴 ** 33.1** (`🔻 -60.8`) | `-60.8 pkt` | 6.69 Er | 0.0% | 5.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 6** | 93.9 → 🟠 ** 68.9** (`🔻 -25.0`) | `-25.0 pkt` | 5.45 Er | 0.0% | 4.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 1** | 93.9 → 🔴 **  6.5** (`🔻 -87.4`) | `-87.4 pkt` | 8.57 Er | 0.5% | 40.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 10** | 93.9 → 🔴 **  9.9** (`🔻 -84.0`) | `-84.0 pkt` | 4.77 Er | 0.0% | 3.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: cooldown 3 → 0 (co erę)** | 93.9 → 🔴 ** 11.4** (`🔻 -82.5`) | `-82.5 pkt` | 4.87 Er | 0.0% | 5.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: całkowite wyłączenie** | 93.9 → 🟠 ** 66.0** (`🔻 -27.9`) | `-27.9 pkt` | 5.94 Er | 0.0% | 4.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Akcja Gospodarcza: 0zł (brak zysku złota)** | 93.9 → 🔴 ** 50.4** (`🔻 -43.5`) | `-43.5 pkt` | 5.87 Er | 0.0% | 7.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Akcja Gospodarcza: 1 → 2 (podwojenie)** | 93.9 → 🔴 ** 46.4** (`🔻 -47.5`) | `-47.5 pkt` | 5.63 Er | 0.0% | 3.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Obserwowanej: 3 → 2 (skrajna presja)** | 93.9 → 🟠 ** 77.9** (`🔻 -16.0`) | `-16.0 pkt` | 5.68 Er | 0.0% | 4.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)

| Badany Warunek Zwycięstwa L2 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: stosy 7 → 1** | 93.9 → 🔴 ** 18.7** (`🔻 -75.2`) | `-75.2 pkt` | 3.93 Er | 0.0% | 3.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: stosy 7 → 14** | 93.9 → 🟠 ** 73.6** (`🔻 -20.3`) | `-20.3 pkt` | 5.85 Er | 0.0% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 1** | 93.9 → 🔴 ** 18.4** (`🔻 -75.5`) | `-75.5 pkt` | 3.41 Er | 0.0% | 3.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 6** | 93.9 → 🔴 ** 60.5** (`🔻 -33.4`) | `-33.4 pkt` | 5.86 Er | 0.0% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Cienie: relikwie 2 → 4** | 93.9 → 🔴 ** 32.6** (`🔻 -61.3`) | `-61.3 pkt` | 6.08 Er | 0.0% | 4.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: dekrety 2 → 4** | 93.9 → 🔴 ** 33.6** (`🔻 -60.3`) | `-60.3 pkt` | 6.02 Er | 0.0% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: wymóg haków 2 → 0** | 93.9 → 🟡 ** 81.4** (`🔻 -12.5`) | `-12.5 pkt` | 5.72 Er | 0.0% | 4.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Korona: wymóg haków 2 → 4** | 93.9 → 🔴 ** 33.5** (`🔻 -60.4`) | `-60.4 pkt` | 6.02 Er | 0.0% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: fragmenty 3 → 1** | 93.9 → 🔴 ** 54.8** (`🔻 -39.1`) | `-39.1 pkt` | 5.99 Er | 0.0% | 4.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: fragmenty 3 → 6** | 93.9 → 🔴 ** 34.7** (`🔻 -59.2`) | `-59.2 pkt` | 6.04 Er | 0.0% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 9 → 1** | 93.9 → 🔴 ** 18.5** (`🔻 -75.4`) | `-75.4 pkt` | 2.96 Er | 0.0% | 2.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 9 → 18** | 93.9 → 🔴 ** 32.9** (`🔻 -61.0`) | `-61.0 pkt` | 6.02 Er | 0.0% | 4.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)

| Badany Wariant / Modyfikator L4 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kronika Dziejów: całkowite wyłączenie** | 93.9 → 🔴 ** 64.3** (`🔻 -29.6`) | `-29.6 pkt` | 5.80 Er | 0.0% | 5.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kronika Dziejów: co 3 Ery (spowolniony zegar)** | 93.9 → 🟠 ** 74.0** (`🔻 -19.9`) | `-19.9 pkt` | 5.80 Er | 0.0% | 5.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Inkwizytor Patrol: ruch 1 → 0 (wyłączenie)** | 93.9 → 🔴 ** 39.1** (`🔻 -54.8`) | `-54.8 pkt` | 6.35 Er | 0.0% | 4.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Inkwizytor Patrol: ruch x2 (podwojona prędkość)** | 93.9 → 🟡 ** 80.7** (`🔻 -13.2`) | `-13.2 pkt` | 5.74 Er | 0.0% | 4.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Szlak Morski: era 4 → nigdy (99)** | 93.9 → 🟢 ** 92.9** (`🔻 -1.0`) | `-1.0 pkt` | 5.78 Er | 0.0% | 4.5% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |

---

## 5. 👥 Warstwa IV — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych. Kolumna win share to HUD kanonu; setup+witalność to stary blend (kara martwej ścieżki).

| Nieobecna Frakcja | Setup Testowy | Win share | Setup+witalność | Diagnoza |
| :--- | :--- | :---: | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`91.6`** | `91.6` | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`97.4`** | `97.4` | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`93.8`** | `93.8` | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`87.0`** | `87.0` | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`99.5`** | `99.5` | Brak presji stosów i bezpośredniego Inkwizytora |