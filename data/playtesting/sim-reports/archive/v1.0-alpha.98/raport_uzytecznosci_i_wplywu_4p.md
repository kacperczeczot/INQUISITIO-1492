# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v1.0-alpha.98

**Wersja Gry:** `v1.0-alpha.98` | **Data Badania:** 2026-08-29 22:46 | **Próba:** 5000 gier/setup (25000 gier na wariant) | **Ziarno:** 42
**4P Score (win share):** 🟢 ** 94.7** pkt | **Witalność (osobna kara):** `0.000` | **Śr. Er:** `5.76` | **Deadlocki:** `0.0%` | **Pas Biedy:** `4.5%`
**Udziały 4P:** CAA 24.4% · GC 25.0% · KB 24.8% · KT 25.3% · SO 25.4%

Klasyfikacja L1/L2/L4 i Δ 4P liczą wyłącznie równość win share (`calculate_balance_score`). Kara witalności jest osobno.

---

## 0. Wady z tej próby (nie HUD win share)

Kubełki klasyfikatora i ostrzeżenia witalności z bieżącego runu.

- **Autopodatek (SELF_HARM):** 3/60
- **DEAD_WEIGHT:** `gc-05` Fałszywy Świadek, `gc-08` Zatrute Złoto, `so-05` Wezwanie do Trybunału
- **Karty Kroniki |Δ4P| ≤ 0.8:** 3/10
- **Ablacja całej Kroniki (`L4_NO_TIME_DECK`):** Δ4P -29.8 (STABILIZER)
- **Mechaniki WEAK/NEUTRAL:** Szlak Morski: era 4 → nigdy (99)

---

## 1. 🗺️ Podsumowanie Ekosystemu Kart Kanonu 4P (Matryca Wpływu Kart, 60 kart)

Rozkład wszystkich 60 kart frakcyjnych w matrycy **Wpływ na Frakcję ($\Delta \text{Share}$)** vs **Wpływ na Kanon 4P ($\Delta \text{4P Score}$)**:

| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |
| :--- | :---: | :---: | :--- | :--- |
| 🩸 **Autopodatek (Self-Harm)** | **3** | 5.0% | Wyłączenie **podnosi** win share własnej frakcji — karta jest haraczem, nie silnikiem | **Rework / osłabienie kosztu, nie filar** |
| 🔄 **Rozcieńczalnik Talii (Tempo Filler)** | **7** | 11.7% | Normalna karta tempa — ablacja fałszywie flaguje ją jako autopodatek z powodu odchudzenia talii | **Normalny element deckbuildingu** |
| 💤 **Karta Pasywna (Dead Weight)** | **3** | 5.0% | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia lub wycięcia** |
| ⚠️ **Karta Destabilizująca (Disruptor)** | **0** | 0.0% | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |
| ⚖️ **Zbalansowane Narzędzie** | **18** | 30.0% | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Narzędzie, nie złoty środek całego kanonu** |
| 👑 / ⚓ **Filar / Kotwica Kanonu** | **29** | 48.3% | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |

---

## 2. 🃏 Warstwa I — Szczegółowa Analiza 60 Kart Frakcji w Kanonie 4P

### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)
Karty, których brak powoduje spadek wyniku Kanonu 4P o $\ge 4.0$ pkt lub załamanie winrate frakcji o $\ge 4.0\%$ — **bez** autopodatków (te są w 2.1b):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kt-10` **Pieczęć Salomona** | Kabała z Toledo | 4zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.3% → **0.0%** | **`-25.3%`** | 94.7 → **34.9 pkt** (`-59.8`) |
| `kb-09` **Dekret Królewski** | Korona & Borgiowie | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.8% → **1.1%** | **`-23.7%`** | 94.7 → **35.7 pkt** (`-59.0`) |
| `caa-10` **Echo Alhambry** | Cienie Al-Andalus | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.4% → **4.4%** | **`-20.0%`** | 94.7 → **39.1 pkt** (`-55.6`) |
| `kt-02` **Transmutacja Złota** | Kabała z Toledo | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.3% → **8.2%** | **`-17.1%`** | 94.7 → **48.6 pkt** (`-46.1`) |
| `caa-05` **Ukryty Kurier** | Cienie Al-Andalus | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.4% → **13.1%** | **`-11.3%`** | 94.7 → **59.6 pkt** (`-35.1`) |
| `kt-11` **Medytacja Sefirot** | Kabała z Toledo | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.3% → **15.7%** | **`-9.6%`** | 94.7 → **66.7 pkt** (`-28.0`) |
| `kb-02` **Pobór Podatków** | Korona & Borgiowie | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.8% → **15.3%** | **`-9.5%`** | 94.7 → **67.6 pkt** (`-27.1`) |
| `kt-03` **Zakazana Wiedza** | Kabała z Toledo | 0zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 25.3% → **20.2%** | **`-5.1%`** | 94.7 → **80.0 pkt** (`-14.7`) |
| `kt-05` **Wskazówka Cyklu** | Kabała z Toledo | 1zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 25.3% → **19.3%** | **`-6.0%`** | 94.7 → **80.2 pkt** (`-14.5`) |
| `kb-10` **Pieczęć Korony** | Korona & Borgiowie | 4zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 24.8% → **21.0%** | **`-3.8%`** | 94.7 → **82.1 pkt** (`-12.6`) |
| `gc-10` **Upadek Domu** | Gildia Cieni | 4zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 25.0% → **20.8%** | **`-4.2%`** | 94.7 → **82.6 pkt** (`-12.1`) |
| `gc-09` **Lista Dłużników** | Gildia Cieni | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.0% → **20.8%** | **`-4.2%`** | 94.7 → **82.8 pkt** (`-11.9`) |
| `so-10` **Oczyść Miasto** | Święte Oficjum | 5zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 25.4% → **20.9%** | **`-4.5%`** | 94.7 → **83.8 pkt** (`-10.9`) |
| `caa-06` **Ucieczka z Lochów** | Cienie Al-Andalus | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.4% → **21.2%** | **`-3.2%`** | 94.7 → **84.1 pkt** (`-10.6`) |
| `so-04` **Publiczne Ostrzeżenie** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.4% → **24.7%** | **`-0.7%`** | 94.7 → **87.6 pkt** (`-7.1`) |
| `so-03` **Podejrzenie** | Święte Oficjum | 2zł / 4☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.4% → **25.8%** | **`+0.4%`** | 94.7 → **88.2 pkt** (`-6.5`) |
| `so-08` **Nasłanie Inkwizytora** | Święte Oficjum | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.4% → **24.9%** | **`-0.5%`** | 94.7 → **88.5 pkt** (`-6.2`) |
| `gc-07` **Skrytobójstwo** | Gildia Cieni | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.0% → **26.4%** | **`+1.4%`** | 94.7 → **89.3 pkt** (`-5.4`) |
| `so-07` **Przesłuchanie Oficjum** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.4% → **26.0%** | **`+0.6%`** | 94.7 → **89.3 pkt** (`-5.4`) |
| `gc-04` **Informator** | Gildia Cieni | 1zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.0% → **22.7%** | **`-2.3%`** | 94.7 → **89.4 pkt** (`-5.3`) |
| `kt-09` **Fragment Kodeksu** | Kabała z Toledo | 1zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.3% → **23.4%** | **`-1.9%`** | 94.7 → **89.5 pkt** (`-5.2`) |
| `so-01` **Patrol Familiariuszy** | Święte Oficjum | 1zł / 2☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.4% → **27.2%** | **`+1.8%`** | 94.7 → **89.7 pkt** (`-5.0`) |
| `so-06` **Areszt Trybunalski** | Święte Oficjum | 2zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.4% → **26.2%** | **`+0.8%`** | 94.7 → **89.9 pkt** (`-4.8`) |
| `gc-06` **Szantaż** | Gildia Cieni | 3zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.0% → **25.1%** | **`+0.1%`** | 94.7 → **91.8 pkt** (`-2.9`) |
| `gc-02` **Czarny Rynek** | Gildia Cieni | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.0% → **26.1%** | **`+1.1%`** | 94.7 → **91.9 pkt** (`-2.8`) |
| `gc-03` **Podrzucenie Księgi** | Gildia Cieni | 1zł / 2☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.0% → **26.3%** | **`+1.3%`** | 94.7 → **92.2 pkt** (`-2.5`) |
| `so-02` **Skarbiec Trybunału** | Święte Oficjum | 1zł / 2☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.4% → **25.2%** | **`-0.2%`** | 94.7 → **92.4 pkt** (`-2.3`) |
| `so-12` **Straż Trybunalska** | Święte Oficjum | 1zł / 2☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.4% → **26.7%** | **`+1.3%`** | 94.7 → **92.4 pkt** (`-2.3`) |
| `so-09` **Świadek Koronny** | Święte Oficjum | 1zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.4% → **25.7%** | **`+0.3%`** | 94.7 → **92.4 pkt** (`-2.3`) |

### 2.1b. 🩸 Autopodatek Frakcji (Self-Harm)
Karty, których wyłączenie **podnosi** win share własnej frakcji. Gracz zauważy je jako haracz, nawet gdy stół 4P jest równy dzięki temu haraczowi.

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kb-08` **Przekupstwo Sędziego** | Korona & Borgiowie | 3zł / 2☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.8% → **34.0%** | **`+9.2%`** | 94.7 → **69.4 pkt** (`-25.3`) |
| `caa-01` **Przejście Podziemiami** | Cienie Al-Andalus | 2zł / 2☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.4% → **29.0%** | **`+4.6%`** | 94.7 → **85.1 pkt** (`-9.6`) |
| `kt-01` **Rytuał Przejścia** | Kabała z Toledo | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.3% → **29.3%** | **`+4.0%`** | 94.7 → **85.0 pkt** (`-9.7`) |

### 2.2. ⚠️ Karty Destabilizujące Kanon 4P (Disruptors)
Karty, których wyłączenie podnosi 4P Score ($\Delta \text{4P} \ge +1.5$ pkt):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *Brak kart destabilizujących* | - | - | - | - | - | - |

### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich 60 Kart Frakcji w Kanonie 4P

| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Play-Rate | Faction Win Share 4P | $\Delta$ Frakcji | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `caa-02` | **Złoto z Kryjówki** | Cienie Al-Andalus | 0 | 0 | 0.24 | 24.4% → 29.4% | `+5.0%` | 83.5 | `-11.2` | 5.69 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `caa-03` | **Cień na Rynku** | Cienie Al-Andalus | 0 | 1 | 0.93 | 24.4% → 33.0% | `+8.6%` | 70.0 | `-24.7` | 5.78 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-04` | **Fałszywy Trop** | Cienie Al-Andalus | 0 | 0 | 0.97 | 24.4% → 30.1% | `+5.7%` | 81.7 | `-13.0` | 5.68 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-05` | **Ukryty Kurier** | Cienie Al-Andalus | 0 | 0 | 1.01 | 24.4% → 13.1% | `-11.3%` | 59.6 | `-35.1` | 5.95 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `caa-12` | **Skrytka w Murach** | Cienie Al-Andalus | 1 | 0 | 0.92 | 24.4% → 30.6% | `+6.2%` | 79.5 | `-15.2` | 5.66 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-01` | **Przejście Podziemiami** | Cienie Al-Andalus | 2 | 2 | 0.00 | 24.4% → 29.0% | `+4.6%` | 85.1 | `-9.6` | 5.70 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-06` | **Ucieczka z Lochów** | Cienie Al-Andalus | 0 | 0 | 0.68 | 24.4% → 21.2% | `-3.2%` | 84.1 | `-10.6` | 5.76 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `caa-07` | **Szantaż Bractwa** | Cienie Al-Andalus | 0 | 0 | 0.55 | 24.4% → 29.3% | `+4.9%` | 83.5 | `-11.2` | 5.67 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-11` | **Nocna Zmiana Warty** | Cienie Al-Andalus | 1 | 0 | 0.69 | 24.4% → 28.1% | `+3.7%` | 88.1 | `-6.6` | 5.71 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-08` | **Kaptur Nocy** | Cienie Al-Andalus | 2 | 0 | 0.80 | 24.4% → 29.2% | `+4.8%` | 84.2 | `-10.5` | 5.69 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-09` | **Kurier Relikwii** | Cienie Al-Andalus | 0 | 0 | 0.93 | 24.4% → 30.2% | `+5.8%` | 80.7 | `-14.0` | 5.66 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-10` | **Echo Alhambry** | Cienie Al-Andalus | 2 | 0 | 0.99 | 24.4% → 4.4% | `-20.0%` | 39.1 | `-55.6` | 6.03 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `gc-02` | **Czarny Rynek** | Gildia Cieni | 0 | 0 | 0.78 | 25.0% → 26.1% | `+1.1%` | 91.9 | `-2.8` | 5.75 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-12` | **Złodziejski Zwiad** | Gildia Cieni | 0 | 2 | 0.44 | 25.0% → 28.1% | `+3.1%` | 86.0 | `-8.7` | 5.74 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `gc-01` | **Przekupiony Strażnik** | Gildia Cieni | 1 | 1 | 0.47 | 25.0% → 27.2% | `+2.2%` | 88.7 | `-6.0` | 5.76 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `gc-03` | **Podrzucenie Księgi** | Gildia Cieni | 1 | 2 | 0.08 | 25.0% → 26.3% | `+1.3%` | 92.2 | `-2.5` | 5.76 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-04` | **Informator** | Gildia Cieni | 1 | 1 | 0.80 | 25.0% → 22.7% | `-2.3%` | 89.4 | `-5.3` | 5.81 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-05` | **Fałszywy Świadek** | Gildia Cieni | 1 | 0 | 0.00 | 25.0% → 25.2% | `+0.2%` | 92.2 | `-2.5` | 5.77 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `gc-07` | **Skrytobójstwo** | Gildia Cieni | 0 | 0 | 0.79 | 25.0% → 26.4% | `+1.4%` | 89.3 | `-5.4` | 5.80 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-11` | **Fałszywe Świadectwo Cechu** | Gildia Cieni | 0 | 2 | 0.31 | 25.0% → 27.1% | `+2.1%` | 90.4 | `-4.3` | 5.74 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `gc-08` | **Zatrute Złoto** | Gildia Cieni | 1 | 2 | 0.00 | 25.0% → 26.3% | `+1.3%` | 90.8 | `-3.9` | 5.75 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `gc-06` | **Szantaż** | Gildia Cieni | 3 | 1 | 0.43 | 25.0% → 25.1% | `+0.1%` | 91.8 | `-2.9` | 5.77 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-09` | **Lista Dłużników** | Gildia Cieni | 1 | 0 | 0.79 | 25.0% → 20.8% | `-4.2%` | 82.8 | `-11.9` | 5.81 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `gc-10` | **Upadek Domu** | Gildia Cieni | 4 | 2 | 0.46 | 25.0% → 20.8% | `-4.2%` | 82.6 | `-12.1` | 5.84 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-01` | **Rozkaz Dworu** | Korona & Borgiowie | 1 | 1 | 0.25 | 24.8% → 35.6% | `+10.8%` | 64.5 | `-30.2` | 5.67 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kb-02` | **Pobór Podatków** | Korona & Borgiowie | 1 | 0 | 0.84 | 24.8% → 15.3% | `-9.5%` | 67.6 | `-27.1` | 5.88 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-03` | **Plotka Dworska** | Korona & Borgiowie | 1 | 1 | 0.64 | 24.8% → 35.3% | `+10.5%` | 64.3 | `-30.4` | 5.68 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-11` | **Tajny Emisariusz** | Korona & Borgiowie | 1 | 0 | 0.83 | 24.8% → 33.5% | `+8.7%` | 71.1 | `-23.6` | 5.66 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-04` | **Faworyt Dworu** | Korona & Borgiowie | 2 | 0 | 0.74 | 24.8% → 31.9% | `+7.1%` | 75.9 | `-18.8` | 5.66 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-05` | **List Żelazny** | Korona & Borgiowie | 2 | 1 | 0.82 | 24.8% → 33.5% | `+8.7%` | 70.9 | `-23.8` | 5.60 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-12` | **Szantaż Salonowy** | Korona & Borgiowie | 1 | 2 | 0.82 | 24.8% → 29.4% | `+4.6%` | 83.5 | `-11.2` | 5.72 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-06` | **Areszt Królewski** | Korona & Borgiowie | 2 | 0 | 0.44 | 24.8% → 36.1% | `+11.3%` | 63.4 | `-31.3` | 5.65 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kb-07` | **Szantaż Pieczęcią** | Korona & Borgiowie | 2 | 0 | 0.62 | 24.8% → 32.2% | `+7.4%` | 75.2 | `-19.5` | 5.67 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-08` | **Przekupstwo Sędziego** | Korona & Borgiowie | 3 | 2 | 0.08 | 24.8% → 34.0% | `+9.2%` | 69.4 | `-25.3` | 5.68 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-09` | **Dekret Królewski** | Korona & Borgiowie | 2 | 0 | 0.85 | 24.8% → 1.1% | `-23.7%` | 35.7 | `-59.0` | 6.01 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-10` | **Pieczęć Korony** | Korona & Borgiowie | 4 | 1 | 0.16 | 24.8% → 21.0% | `-3.8%` | 82.1 | `-12.6` | 5.90 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-02` | **Transmutacja Złota** | Kabała z Toledo | 0 | 0 | 0.95 | 25.3% → 8.2% | `-17.1%` | 48.6 | `-46.1` | 5.91 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-03` | **Zakazana Wiedza** | Kabała z Toledo | 0 | 2 | 0.81 | 25.3% → 20.2% | `-5.1%` | 80.0 | `-14.7` | 6.01 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-01` | **Rytuał Przejścia** | Kabała z Toledo | 1 | 1 | 0.05 | 25.3% → 29.3% | `+4.0%` | 85.0 | `-9.7` | 5.68 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-04` | **Zwierciadło Herezji** | Kabała z Toledo | 1 | 0 | 0.52 | 25.3% → 29.9% | `+4.6%` | 83.4 | `-11.3` | 5.67 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-05` | **Wskazówka Cyklu** | Kabała z Toledo | 1 | 1 | 0.96 | 25.3% → 19.3% | `-6.0%` | 80.2 | `-14.5` | 5.95 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-12` | **Strażnik Archiwum** | Kabała z Toledo | 1 | 0 | 0.91 | 25.3% → 29.3% | `+4.0%` | 85.8 | `-8.9` | 5.65 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-07` | **Archiwum Ukryte** | Kabała z Toledo | 1 | 0 | 0.30 | 25.3% → 29.3% | `+4.0%` | 85.7 | `-9.0` | 5.69 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kt-08` | **Areszt Wiedzy** | Kabała z Toledo | 1 | 0 | 0.88 | 25.3% → 28.7% | `+3.4%` | 86.4 | `-8.3` | 5.70 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-06` | **Przesłuchanie Imienia** | Kabała z Toledo | 2 | 0 | 0.82 | 25.3% → 35.2% | `+9.9%` | 67.1 | `-27.6` | 5.60 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-11` | **Medytacja Sefirot** | Kabała z Toledo | 2 | 0 | 0.92 | 25.3% → 15.7% | `-9.6%` | 66.7 | `-28.0` | 5.72 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-09` | **Fragment Kodeksu** | Kabała z Toledo | 1 | 1 | 0.96 | 25.3% → 23.4% | `-1.9%` | 89.5 | `-5.2` | 5.89 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kt-10` | **Pieczęć Salomona** | Kabała z Toledo | 4 | 0 | 0.52 | 25.3% → 0.0% | `-25.3%` | 34.9 | `-59.8` | 6.03 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `so-05` | **Wezwanie do Trybunału** | Święte Oficjum | 0 | 4 | 0.00 | 25.4% → 21.6% | `-3.8%` | 85.2 | `-9.5` | 5.81 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `so-01` | **Patrol Familiariuszy** | Święte Oficjum | 1 | 2 | 0.24 | 25.4% → 27.2% | `+1.8%` | 89.7 | `-5.0` | 5.78 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-02` | **Skarbiec Trybunału** | Święte Oficjum | 1 | 2 | 0.50 | 25.4% → 25.2% | `-0.2%` | 92.4 | `-2.3` | 5.80 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-04` | **Publiczne Ostrzeżenie** | Święte Oficjum | 1 | 0 | 0.88 | 25.4% → 24.7% | `-0.7%` | 87.6 | `-7.1` | 5.72 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-12` | **Straż Trybunalska** | Święte Oficjum | 1 | 2 | 0.25 | 25.4% → 26.7% | `+1.3%` | 92.4 | `-2.3` | 5.79 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-03` | **Podejrzenie** | Święte Oficjum | 2 | 4 | 0.30 | 25.4% → 25.8% | `+0.4%` | 88.2 | `-6.5` | 5.82 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-08` | **Nasłanie Inkwizytora** | Święte Oficjum | 0 | 0 | 0.87 | 25.4% → 24.9% | `-0.5%` | 88.5 | `-6.2` | 5.74 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-11` | **Dekret Czystości Wiary** | Święte Oficjum | 0 | 1 | 0.92 | 25.4% → 25.9% | `+0.5%` | 94.8 | `+0.1` | 5.78 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-07` | **Przesłuchanie Oficjum** | Święte Oficjum | 1 | 0 | 0.85 | 25.4% → 26.0% | `+0.6%` | 89.3 | `-5.4` | 5.69 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-09` | **Świadek Koronny** | Święte Oficjum | 1 | 1 | 0.15 | 25.4% → 25.7% | `+0.3%` | 92.4 | `-2.3` | 5.80 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-06` | **Areszt Trybunalski** | Święte Oficjum | 2 | 0 | 0.92 | 25.4% → 26.2% | `+0.8%` | 89.9 | `-4.8` | 5.72 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-10` | **Oczyść Miasto** | Święte Oficjum | 5 | 1 | 0.78 | 25.4% → 20.9% | `-4.5%` | 83.8 | `-10.9` | 5.91 | 0.0% | 👑 FILAR KANONU (Core Keystone) |

### 2.4. 🎯 Monokultura Talii (Deck Concentration Index)

Jak mocno skoncentrowane jest zagrywanie kart w obrębie każdej frakcji.
Wskaźnik HHI (Herfindahl–Hirschman Index) mierzy koncentrację: HHI = 1.0 oznacza, że 100% zagrań to 1 karta; HHI ≈ 1/N oznacza idealnie równomierny rozkład.

| Frakcja | Kart w Talii | Top Karta (Play-Rate) | Top 2 (%) | HHI | Ocena |
| :--- | :---: | :--- | :---: | :---: | :--- |
| Cienie Al-Andalus | 12 | `caa-05` (1.01) | 22.9% | 0.098 | 🟢 Zdrowy rozkład |
| Gildia Cieni | 12 | `gc-04` (0.80) | 29.7% | 0.119 | 🟢 Zdrowy rozkład |
| Korona & Borgiowie | 12 | `kb-09` (0.85) | 23.8% | 0.101 | 🟢 Zdrowy rozkład |
| Kabała z Toledo | 12 | `kt-05` (0.96) | 22.3% | 0.097 | 🟢 Zdrowy rozkład |
| Święte Oficjum | 12 | `so-06` (0.92) | 27.5% | 0.113 | 🟢 Zdrowy rozkład |

---

## 3. ⏳ Warstwa II — Kronika Dziejów w 4P (Ablacja 8 Kart Wydarzeń Czasu)

Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans w 4P:

| ID | Karta Wydarzenia | 4P Score | $\Delta$ 4P | Średnia Er | Deadlock % | Status Roli w Kronice |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `time-01` | **Kapitulacja Grenady** | 94.7 → 🟢 ** 93.4** (`🔻 -1.3`) | `-1.3 pkt` | 5.80 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-02` | **Godzina Policyjna** | 94.7 → 🟢 ** 94.1** (`🔻 -0.6`) | `-0.6 pkt` | 5.78 Er | 0.0% | ⚖️ Neutralna Kronika |
| `time-03` | **Flota Odkrywców** | 94.7 → 🟢 ** 93.4** (`🔻 -1.3`) | `-1.3 pkt` | 5.84 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-04` | **Rewizja w Dzielnicach** | 94.7 → 🟢 ** 92.0** (`🔻 -2.7`) | `-2.7 pkt` | 5.81 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-05` | **Gorączka Donosów** | 94.7 → 🟢 ** 93.6** (`🔻 -1.1`) | `-1.1 pkt` | 5.79 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-06` | **Nocna Obława** | 94.7 → 🟢 ** 94.2** (`🔻 -0.5`) | `-0.5 pkt` | 5.78 Er | 0.0% | ⚖️ Neutralna Kronika |
| `time-07` | **Bunt w Lochach** | 94.7 → 🟢 ** 93.2** (`🔻 -1.5`) | `-1.5 pkt` | 5.78 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-08` | **Święte Przymierze** | 94.7 → 🟡 ** 85.8** (`🔻 -8.9`) | `-8.9 pkt` | 5.68 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-09` | **Jarmark Królewski** | 94.7 → 🟢 ** 94.7** (`= 0.0`) | `0.0 pkt` | 5.79 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-10` | **Amnestia Biskupia** | 94.7 → 🟢 ** 93.0** (`🔻 -1.7`) | `-1.7 pkt` | 5.76 Er | 0.0% | 🟢 Stabilizator tempa |

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
| **Szlak Morski: era 4 → nigdy (99)** | Poziom 4: Warianty i Modyfikatory | 94.7 → 🟢 ** 92.4** (`🔻 -2.3`) | `-2.3 pkt` | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |

### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)

| Badany Podsystem / Modyfikator L1 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Limit Er: 15 → 7 (skrajna presja)** | 94.7 → 🟡 ** 85.8** (`🔻 -8.9`) | `-8.9 pkt` | 5.64 Er | 9.0% | 4.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Próg Oskarżenia: 7 → 1** | 94.7 → 🔴 ** 25.8** (`🔻 -68.9`) | `-68.9 pkt` | 5.32 Er | 0.0% | 2.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Oskarżenia: 7 → 14** | 94.7 → 🔴 ** 32.1** (`🔻 -62.6`) | `-62.6 pkt` | 6.40 Er | 0.0% | 5.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 0zł (wyłączenie)** | 94.7 → 🔴 ** 49.5** (`🔻 -45.2`) | `-45.2 pkt` | 6.47 Er | 0.0% | 11.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 8zł** | 94.7 → 🔴 ** 31.8** (`🔻 -62.9`) | `-62.9 pkt` | 5.06 Er | 0.0% | 1.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 1** | 94.7 → 🔴 ** 33.0** (`🔻 -61.7`) | `-61.7 pkt` | 6.68 Er | 0.0% | 5.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 6** | 94.7 → 🟠 ** 69.2** (`🔻 -25.5`) | `-25.5 pkt` | 5.44 Er | 0.0% | 4.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 1** | 94.7 → 🔴 **  5.4** (`🔻 -89.3`) | `-89.3 pkt` | 8.59 Er | 0.8% | 38.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 10** | 94.7 → 🔴 **  9.9** (`🔻 -84.8`) | `-84.8 pkt` | 4.77 Er | 0.0% | 3.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: cooldown 3 → 0 (co erę)** | 94.7 → 🔴 ** 11.3** (`🔻 -83.4`) | `-83.4 pkt` | 4.88 Er | 0.0% | 5.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: całkowite wyłączenie** | 94.7 → 🟠 ** 65.6** (`🔻 -29.1`) | `-29.1 pkt` | 5.94 Er | 0.0% | 4.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Akcja Gospodarcza: 0zł (brak zysku złota)** | 94.7 → 🔴 ** 50.9** (`🔻 -43.8`) | `-43.8 pkt` | 5.88 Er | 0.0% | 7.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Akcja Gospodarcza: 1 → 2 (podwojenie)** | 94.7 → 🔴 ** 45.8** (`🔻 -48.9`) | `-48.9 pkt` | 5.63 Er | 0.0% | 3.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Obserwowanej: 3 → 2 (skrajna presja)** | 94.7 → 🟡 ** 80.0** (`🔻 -14.7`) | `-14.7 pkt` | 5.67 Er | 0.0% | 4.4% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |

### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)

| Badany Warunek Zwycięstwa L2 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: stosy 7 → 1** | 94.7 → 🔴 ** 18.8** (`🔻 -75.9`) | `-75.9 pkt` | 3.93 Er | 0.0% | 3.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: stosy 7 → 14** | 94.7 → 🟠 ** 72.2** (`🔻 -22.5`) | `-22.5 pkt` | 5.84 Er | 0.0% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 1** | 94.7 → 🔴 ** 18.5** (`🔻 -76.2`) | `-76.2 pkt` | 3.41 Er | 0.0% | 3.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 6** | 94.7 → 🔴 ** 59.9** (`🔻 -34.8`) | `-34.8 pkt` | 5.85 Er | 0.0% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Cienie: relikwie 2 → 4** | 94.7 → 🔴 ** 33.0** (`🔻 -61.7`) | `-61.7 pkt` | 6.08 Er | 0.0% | 4.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: dekrety 2 → 4** | 94.7 → 🔴 ** 34.3** (`🔻 -60.4`) | `-60.4 pkt` | 6.02 Er | 0.0% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: wymóg haków 2 → 0** | 94.7 → 🟡 ** 80.6** (`🔻 -14.1`) | `-14.1 pkt` | 5.72 Er | 0.0% | 4.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Korona: wymóg haków 2 → 4** | 94.7 → 🔴 ** 34.2** (`🔻 -60.5`) | `-60.5 pkt` | 6.02 Er | 0.0% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: fragmenty 3 → 1** | 94.7 → 🔴 ** 55.3** (`🔻 -39.4`) | `-39.4 pkt` | 6.00 Er | 0.0% | 4.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: fragmenty 3 → 6** | 94.7 → 🔴 ** 34.8** (`🔻 -59.9`) | `-59.9 pkt` | 6.05 Er | 0.0% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 9 → 1** | 94.7 → 🔴 ** 18.4** (`🔻 -76.3`) | `-76.3 pkt` | 2.96 Er | 0.0% | 2.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 9 → 18** | 94.7 → 🔴 ** 33.1** (`🔻 -61.6`) | `-61.6 pkt` | 6.02 Er | 0.0% | 4.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)

| Badany Wariant / Modyfikator L4 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kronika Dziejów: całkowite wyłączenie** | 94.7 → 🔴 ** 64.9** (`🔻 -29.8`) | `-29.8 pkt` | 5.81 Er | 0.0% | 5.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kronika Dziejów: co 3 Ery (spowolniony zegar)** | 94.7 → 🟠 ** 75.0** (`🔻 -19.7`) | `-19.7 pkt` | 5.81 Er | 0.0% | 5.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Inkwizytor Patrol: ruch 1 → 0 (wyłączenie)** | 94.7 → 🔴 ** 38.3** (`🔻 -56.4`) | `-56.4 pkt` | 6.36 Er | 0.0% | 4.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Inkwizytor Patrol: ruch x2 (podwojona prędkość)** | 94.7 → 🟡 ** 83.4** (`🔻 -11.3`) | `-11.3 pkt` | 5.74 Er | 0.0% | 4.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Szlak Morski: era 4 → nigdy (99)** | 94.7 → 🟢 ** 92.4** (`🔻 -2.3`) | `-2.3 pkt` | 5.78 Er | 0.0% | 4.5% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |

---

## 5. 👥 Warstwa IV — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych. Kolumna win share to HUD kanonu; setup+witalność to stary blend (kara martwej ścieżki).

| Nieobecna Frakcja | Setup Testowy | Win share | Setup+witalność | Diagnoza |
| :--- | :--- | :---: | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`91.3`** | `91.3` | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`97.5`** | `97.5` | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`96.8`** | `96.8` | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`88.9`** | `88.9` | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`99.2`** | `99.2` | Brak presji stosów i bezpośredniego Inkwizytora |