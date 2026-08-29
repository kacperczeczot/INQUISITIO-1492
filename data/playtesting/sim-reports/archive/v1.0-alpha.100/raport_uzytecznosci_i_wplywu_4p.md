# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v1.0-alpha.100

**Wersja Gry:** `v1.0-alpha.100` | **Data Badania:** 2026-08-29 23:11 | **Próba:** 5000 gier/setup (25000 gier na wariant) | **Ziarno:** 42
**4P Score (win share):** 🟢 ** 90.9** pkt | **Witalność (osobna kara):** `0.000` | **Śr. Er:** `5.83` | **Deadlocki:** `0.0%` | **Pas Biedy:** `4.5%`
**Udziały 4P:** CAA 25.3% · GC 25.6% · KB 25.6% · KT 24.6% · SO 24.0%

Klasyfikacja L1/L2/L4 i Δ 4P liczą wyłącznie równość win share (`calculate_balance_score`). Kara witalności jest osobno.

---

## 0. Wady z tej próby (nie HUD win share)

Kubełki klasyfikatora i ostrzeżenia witalności z bieżącego runu.

- **Autopodatek (SELF_HARM):** 2/60
- **DEAD_WEIGHT:** `gc-05` Fałszywy Świadek, `gc-08` Zatrute Złoto, `gc-06` Szantaż, `so-05` Wezwanie do Trybunału, `so-09` Świadek Koronny
- **Karty Kroniki |Δ4P| ≤ 0.8:** 4/10
- **Ablacja całej Kroniki (`L4_NO_TIME_DECK`):** Δ4P -25.4 (STABILIZER)
- **Mechaniki WEAK/NEUTRAL:** Szlak Morski: era 4 → nigdy (99)

---

## 1. 🗺️ Podsumowanie Ekosystemu Kart Kanonu 4P (Matryca Wpływu Kart, 60 kart)

Rozkład wszystkich 60 kart frakcyjnych w matrycy **Wpływ na Frakcję ($\Delta \text{Share}$)** vs **Wpływ na Kanon 4P ($\Delta \text{4P Score}$)**:

| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |
| :--- | :---: | :---: | :--- | :--- |
| 🩸 **Autopodatek (Self-Harm)** | **2** | 3.3% | Wyłączenie **podnosi** win share własnej frakcji — karta jest haraczem, nie silnikiem | **Rework / osłabienie kosztu, nie filar** |
| 🔄 **Rozcieńczalnik Talii (Tempo Filler)** | **6** | 10.0% | Normalna karta tempa — ablacja fałszywie flaguje ją jako autopodatek z powodu odchudzenia talii | **Normalny element deckbuildingu** |
| 💤 **Karta Pasywna (Dead Weight)** | **5** | 8.3% | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia lub wycięcia** |
| ⚠️ **Karta Destabilizująca (Disruptor)** | **0** | 0.0% | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |
| ⚖️ **Zbalansowane Narzędzie** | **25** | 41.7% | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Narzędzie, nie złoty środek całego kanonu** |
| 👑 / ⚓ **Filar / Kotwica Kanonu** | **22** | 36.7% | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |

---

## 2. 🃏 Warstwa I — Szczegółowa Analiza 60 Kart Frakcji w Kanonie 4P

### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)
Karty, których brak powoduje spadek wyniku Kanonu 4P o $\ge 4.0$ pkt lub załamanie winrate frakcji o $\ge 4.0\%$ — **bez** autopodatków (te są w 2.1b):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kt-10` **Pieczęć Salomona** | Kabała z Toledo | 4zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.6% → **0.0%** | **`-24.6%`** | 90.9 → **33.4 pkt** (`-57.5`) |
| `kb-09` **Dekret Królewski** | Korona & Borgiowie | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.6% → **1.3%** | **`-24.3%`** | 90.9 → **35.9 pkt** (`-55.0`) |
| `caa-10` **Echo Alhambry** | Cienie Al-Andalus | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.3% → **4.6%** | **`-20.7%`** | 90.9 → **38.9 pkt** (`-52.0`) |
| `kt-02` **Transmutacja Złota** | Kabała z Toledo | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.6% → **7.3%** | **`-17.3%`** | 90.9 → **45.4 pkt** (`-45.5`) |
| `caa-05` **Ukryty Kurier** | Cienie Al-Andalus | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.3% → **13.3%** | **`-12.0%`** | 90.9 → **58.5 pkt** (`-32.4`) |
| `kt-11` **Medytacja Sefirot** | Kabała z Toledo | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.6% → **15.6%** | **`-9.0%`** | 90.9 → **65.7 pkt** (`-25.2`) |
| `kb-02` **Pobór Podatków** | Korona & Borgiowie | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.6% → **14.9%** | **`-10.7%`** | 90.9 → **66.2 pkt** (`-24.7`) |
| `kt-03` **Zakazana Wiedza** | Kabała z Toledo | 0zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 24.6% → **20.2%** | **`-4.4%`** | 90.9 → **74.0 pkt** (`-16.9`) |
| `kt-05` **Wskazówka Cyklu** | Kabała z Toledo | 1zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 24.6% → **19.3%** | **`-5.3%`** | 90.9 → **76.1 pkt** (`-14.8`) |
| `kb-10` **Pieczęć Korony** | Korona & Borgiowie | 4zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 25.6% → **20.9%** | **`-4.7%`** | 90.9 → **77.7 pkt** (`-13.2`) |
| `so-10` **Oczyść Miasto** | Święte Oficjum | 5zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 24.0% → **20.4%** | **`-3.6%`** | 90.9 → **79.1 pkt** (`-11.8`) |
| `gc-10` **Upadek Domu** | Gildia Cieni | 4zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 25.6% → **20.3%** | **`-5.3%`** | 90.9 → **79.8 pkt** (`-11.1`) |
| `gc-09` **Lista Dłużników** | Gildia Cieni | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.6% → **20.8%** | **`-4.8%`** | 90.9 → **82.6 pkt** (`-8.3`) |
| `caa-06` **Ucieczka z Lochów** | Cienie Al-Andalus | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.3% → **21.6%** | **`-3.7%`** | 90.9 → **83.1 pkt** (`-7.8`) |
| `so-04` **Publiczne Ostrzeżenie** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.0% → **22.7%** | **`-1.3%`** | 90.9 → **84.5 pkt** (`-6.4`) |
| `so-03` **Podejrzenie** | Święte Oficjum | 2zł / 4☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.0% → **25.1%** | **`+1.1%`** | 90.9 → **84.9 pkt** (`-6.0`) |
| `so-08` **Nasłanie Inkwizytora** | Święte Oficjum | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.0% → **23.7%** | **`-0.3%`** | 90.9 → **85.2 pkt** (`-5.7`) |
| `kt-09` **Fragment Kodeksu** | Kabała z Toledo | 1zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.6% → **23.4%** | **`-1.2%`** | 90.9 → **86.6 pkt** (`-4.3`) |
| `so-07` **Przesłuchanie Oficjum** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.0% → **25.5%** | **`+1.5%`** | 90.9 → **86.6 pkt** (`-4.3`) |
| `gc-01` **Przekupiony Strażnik** | Gildia Cieni | 1zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.6% → **27.4%** | **`+1.8%`** | 90.9 → **87.1 pkt** (`-3.8`) |
| `gc-11` **Fałszywe Świadectwo Cechu** | Gildia Cieni | 0zł / 2☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.6% → **27.2%** | **`+1.6%`** | 90.9 → **87.8 pkt** (`-3.1`) |
| `gc-04` **Informator** | Gildia Cieni | 1zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 25.6% → **23.1%** | **`-2.5%`** | 90.9 → **88.6 pkt** (`-2.3`) |

### 2.1b. 🩸 Autopodatek Frakcji (Self-Harm)
Karty, których wyłączenie **podnosi** win share własnej frakcji. Gracz zauważy je jako haracz, nawet gdy stół 4P jest równy dzięki temu haraczowi.

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kt-07` **Archiwum Ukryte** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.6% → **29.1%** | **`+4.5%`** | 90.9 → **84.1 pkt** (`-6.8`) |
| `caa-02` **Złoto z Kryjówki** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.3% → **29.7%** | **`+4.4%`** | 90.9 → **80.7 pkt** (`-10.2`) |

### 2.2. ⚠️ Karty Destabilizujące Kanon 4P (Disruptors)
Karty, których wyłączenie podnosi 4P Score ($\Delta \text{4P} \ge +1.5$ pkt):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *Brak kart destabilizujących* | - | - | - | - | - | - |

### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich 60 Kart Frakcji w Kanonie 4P

| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Play-Rate | Faction Win Share 4P | $\Delta$ Frakcji | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `caa-01` | **Przejście Podziemiami** | Cienie Al-Andalus | 0 | 0 | 0.98 | 25.3% → 29.6% | `+4.3%` | 82.0 | `-8.9` | 5.77 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-02` | **Złoto z Kryjówki** | Cienie Al-Andalus | 0 | 0 | 0.11 | 25.3% → 29.7% | `+4.4%` | 80.7 | `-10.2` | 5.75 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-03` | **Cień na Rynku** | Cienie Al-Andalus | 0 | 1 | 0.92 | 25.3% → 33.8% | `+8.5%` | 67.5 | `-23.4` | 5.81 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-04` | **Fałszywy Trop** | Cienie Al-Andalus | 0 | 0 | 0.97 | 25.3% → 29.8% | `+4.5%` | 80.5 | `-10.4` | 5.74 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-05` | **Ukryty Kurier** | Cienie Al-Andalus | 0 | 0 | 1.02 | 25.3% → 13.3% | `-12.0%` | 58.5 | `-32.4` | 6.01 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `caa-12` | **Skrytka w Murach** | Cienie Al-Andalus | 1 | 0 | 0.87 | 25.3% → 31.0% | `+5.7%` | 77.4 | `-13.5` | 5.72 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-06` | **Ucieczka z Lochów** | Cienie Al-Andalus | 0 | 0 | 0.63 | 25.3% → 21.6% | `-3.7%` | 83.1 | `-7.8` | 5.81 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `caa-07` | **Szantaż Bractwa** | Cienie Al-Andalus | 0 | 0 | 0.34 | 25.3% → 28.8% | `+3.5%` | 83.6 | `-7.3` | 5.76 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `caa-11` | **Nocna Zmiana Warty** | Cienie Al-Andalus | 1 | 0 | 0.34 | 25.3% → 28.6% | `+3.3%` | 84.0 | `-6.9` | 5.77 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `caa-08` | **Kaptur Nocy** | Cienie Al-Andalus | 2 | 0 | 0.72 | 25.3% → 30.0% | `+4.7%` | 80.3 | `-10.6` | 5.74 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-09` | **Kurier Relikwii** | Cienie Al-Andalus | 0 | 0 | 0.90 | 25.3% → 30.5% | `+5.2%` | 78.9 | `-12.0` | 5.73 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-10` | **Echo Alhambry** | Cienie Al-Andalus | 2 | 0 | 1.00 | 25.3% → 4.6% | `-20.7%` | 38.9 | `-52.0` | 6.11 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `gc-02` | **Czarny Rynek** | Gildia Cieni | 0 | 0 | 0.79 | 25.6% → 25.8% | `+0.2%` | 90.8 | `-0.1` | 5.82 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-12` | **Złodziejski Zwiad** | Gildia Cieni | 0 | 2 | 0.44 | 25.6% → 28.4% | `+2.8%` | 84.3 | `-6.6` | 5.81 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `gc-01` | **Przekupiony Strażnik** | Gildia Cieni | 1 | 1 | 0.48 | 25.6% → 27.4% | `+1.8%` | 87.1 | `-3.8` | 5.80 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-03` | **Podrzucenie Księgi** | Gildia Cieni | 1 | 2 | 0.08 | 25.6% → 26.6% | `+1.0%` | 89.8 | `-1.1` | 5.81 | 0.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `gc-04` | **Informator** | Gildia Cieni | 1 | 1 | 0.80 | 25.6% → 23.1% | `-2.5%` | 88.6 | `-2.3` | 5.87 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `gc-05` | **Fałszywy Świadek** | Gildia Cieni | 1 | 0 | 0.00 | 25.6% → 25.6% | `+0.0%` | 89.6 | `-1.3` | 5.83 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `gc-07` | **Skrytobójstwo** | Gildia Cieni | 0 | 0 | 0.80 | 25.6% → 26.8% | `+1.2%` | 89.4 | `-1.5` | 5.87 | 0.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `gc-11` | **Fałszywe Świadectwo Cechu** | Gildia Cieni | 0 | 2 | 0.31 | 25.6% → 27.2% | `+1.6%` | 87.8 | `-3.1` | 5.81 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-08` | **Zatrute Złoto** | Gildia Cieni | 1 | 2 | 0.00 | 25.6% → 26.5% | `+0.9%` | 90.0 | `-0.9` | 5.81 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `gc-06` | **Szantaż** | Gildia Cieni | 3 | 1 | 0.44 | 25.6% → 25.4% | `-0.2%` | 90.8 | `-0.1` | 5.83 | 0.0% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `gc-09` | **Lista Dłużników** | Gildia Cieni | 1 | 0 | 0.79 | 25.6% → 20.8% | `-4.8%` | 82.6 | `-8.3` | 5.86 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `gc-10` | **Upadek Domu** | Gildia Cieni | 4 | 2 | 0.47 | 25.6% → 20.3% | `-5.3%` | 79.8 | `-11.1` | 5.90 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-01` | **Rozkaz Dworu** | Korona & Borgiowie | 1 | 1 | 0.23 | 25.6% → 35.9% | `+10.3%` | 63.1 | `-27.8` | 5.72 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kb-02` | **Pobór Podatków** | Korona & Borgiowie | 1 | 0 | 0.85 | 25.6% → 14.9% | `-10.7%` | 66.2 | `-24.7` | 5.95 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-03` | **Plotka Dworska** | Korona & Borgiowie | 1 | 1 | 0.60 | 25.6% → 36.5% | `+10.9%` | 60.7 | `-30.2` | 5.73 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-11` | **Tajny Emisariusz** | Korona & Borgiowie | 1 | 0 | 0.84 | 25.6% → 33.4% | `+7.8%` | 71.1 | `-19.8` | 5.71 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-04` | **Faworyt Dworu** | Korona & Borgiowie | 2 | 0 | 0.72 | 25.6% → 34.4% | `+8.8%` | 67.9 | `-23.0` | 5.72 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-05` | **List Żelazny** | Korona & Borgiowie | 2 | 1 | 0.82 | 25.6% → 35.9% | `+10.3%` | 63.7 | `-27.2` | 5.67 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-12` | **Szantaż Salonowy** | Korona & Borgiowie | 1 | 2 | 0.82 | 25.6% → 30.9% | `+5.3%` | 78.7 | `-12.2` | 5.77 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-06` | **Areszt Królewski** | Korona & Borgiowie | 2 | 0 | 0.26 | 25.6% → 34.0% | `+8.4%` | 68.5 | `-22.4` | 5.74 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kb-07` | **Szantaż Pieczęcią** | Korona & Borgiowie | 2 | 0 | 0.52 | 25.6% → 34.4% | `+8.8%` | 67.5 | `-23.4` | 5.72 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-08` | **Przekupstwo Sędziego** | Korona & Borgiowie | 2 | 0 | 0.52 | 25.6% → 34.4% | `+8.8%` | 67.5 | `-23.4` | 5.72 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-09` | **Dekret Królewski** | Korona & Borgiowie | 2 | 0 | 0.86 | 25.6% → 1.3% | `-24.3%` | 35.9 | `-55.0` | 6.09 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-10` | **Pieczęć Korony** | Korona & Borgiowie | 4 | 1 | 0.17 | 25.6% → 20.9% | `-4.7%` | 77.7 | `-13.2` | 5.96 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-02` | **Transmutacja Złota** | Kabała z Toledo | 0 | 0 | 0.96 | 24.6% → 7.3% | `-17.3%` | 45.4 | `-45.5` | 5.97 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-03` | **Zakazana Wiedza** | Kabała z Toledo | 0 | 2 | 0.75 | 24.6% → 20.2% | `-4.4%` | 74.0 | `-16.9` | 6.08 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-01` | **Rytuał Przejścia** | Kabała z Toledo | 1 | 0 | 0.96 | 24.6% → 30.5% | `+5.9%` | 79.4 | `-11.5` | 5.69 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-04` | **Zwierciadło Herezji** | Kabała z Toledo | 1 | 0 | 0.25 | 24.6% → 29.3% | `+4.7%` | 83.5 | `-7.4` | 5.74 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kt-05` | **Wskazówka Cyklu** | Kabała z Toledo | 1 | 1 | 0.96 | 24.6% → 19.3% | `-5.3%` | 76.1 | `-14.8` | 6.01 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-12` | **Strażnik Archiwum** | Kabała z Toledo | 1 | 0 | 0.88 | 24.6% → 28.6% | `+4.0%` | 85.6 | `-5.3` | 5.71 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-07` | **Archiwum Ukryte** | Kabała z Toledo | 1 | 0 | 0.09 | 24.6% → 29.1% | `+4.5%` | 84.1 | `-6.8` | 5.74 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-08` | **Areszt Wiedzy** | Kabała z Toledo | 1 | 0 | 0.79 | 24.6% → 27.5% | `+2.9%` | 86.6 | `-4.3` | 5.75 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-06` | **Przesłuchanie Imienia** | Kabała z Toledo | 2 | 0 | 0.73 | 24.6% → 32.6% | `+8.0%` | 72.8 | `-18.1` | 5.69 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-11` | **Medytacja Sefirot** | Kabała z Toledo | 2 | 0 | 0.91 | 24.6% → 15.6% | `-9.0%` | 65.7 | `-25.2` | 5.78 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-09` | **Fragment Kodeksu** | Kabała z Toledo | 1 | 1 | 0.96 | 24.6% → 23.4% | `-1.2%` | 86.6 | `-4.3` | 5.94 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kt-10` | **Pieczęć Salomona** | Kabała z Toledo | 4 | 0 | 0.50 | 24.6% → 0.0% | `-24.6%` | 33.4 | `-57.5` | 6.09 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `so-05` | **Wezwanie do Trybunału** | Święte Oficjum | 0 | 4 | 0.00 | 24.0% → 20.6% | `-3.4%` | 80.2 | `-10.7` | 5.86 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `so-01` | **Patrol Familiariuszy** | Święte Oficjum | 1 | 2 | 0.25 | 24.0% → 25.9% | `+1.9%` | 89.4 | `-1.5` | 5.83 | 0.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `so-02` | **Skarbiec Trybunału** | Święte Oficjum | 1 | 2 | 0.51 | 24.0% → 24.8% | `+0.8%` | 90.2 | `-0.7` | 5.85 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-04` | **Publiczne Ostrzeżenie** | Święte Oficjum | 1 | 0 | 0.90 | 24.0% → 22.7% | `-1.3%` | 84.5 | `-6.4` | 5.76 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-12` | **Straż Trybunalska** | Święte Oficjum | 1 | 2 | 0.26 | 24.0% → 25.0% | `+1.0%` | 89.4 | `-1.5` | 5.83 | 0.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `so-03` | **Podejrzenie** | Święte Oficjum | 2 | 4 | 0.30 | 24.0% → 25.1% | `+1.1%` | 84.9 | `-6.0` | 5.88 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-08` | **Nasłanie Inkwizytora** | Święte Oficjum | 0 | 0 | 0.89 | 24.0% → 23.7% | `-0.3%` | 85.2 | `-5.7` | 5.79 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-11` | **Dekret Czystości Wiary** | Święte Oficjum | 0 | 1 | 0.94 | 24.0% → 24.6% | `+0.6%` | 90.1 | `-0.8` | 5.84 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-07` | **Przesłuchanie Oficjum** | Święte Oficjum | 1 | 0 | 0.86 | 24.0% → 25.5% | `+1.5%` | 86.6 | `-4.3` | 5.75 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-09` | **Świadek Koronny** | Święte Oficjum | 1 | 1 | 0.16 | 24.0% → 24.6% | `+0.6%` | 89.3 | `-1.6` | 5.83 | 0.0% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `so-06` | **Areszt Trybunalski** | Święte Oficjum | 2 | 0 | 0.93 | 24.0% → 25.3% | `+1.3%` | 90.6 | `-0.3` | 5.78 | 0.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `so-10` | **Oczyść Miasto** | Święte Oficjum | 5 | 1 | 0.81 | 24.0% → 20.4% | `-3.6%` | 79.1 | `-11.8` | 5.95 | 0.0% | 👑 FILAR KANONU (Core Keystone) |

### 2.4. 🎯 Monokultura Talii (Deck Concentration Index)

Jak mocno skoncentrowane jest zagrywanie kart w obrębie każdej frakcji.
Wskaźnik HHI (Herfindahl–Hirschman Index) mierzy koncentrację: HHI = 1.0 oznacza, że 100% zagrań to 1 karta; HHI ≈ 1/N oznacza idealnie równomierny rozkład.

| Frakcja | Kart w Talii | Top Karta (Play-Rate) | Top 2 (%) | HHI | Ocena |
| :--- | :---: | :--- | :---: | :---: | :--- |
| Cienie Al-Andalus | 12 | `caa-05` (1.02) | 23.0% | 0.097 | 🟢 Zdrowy rozkład |
| Gildia Cieni | 12 | `gc-04` (0.80) | 29.6% | 0.119 | 🟢 Zdrowy rozkład |
| Korona & Borgiowie | 12 | `kb-09` (0.86) | 23.7% | 0.098 | 🟢 Zdrowy rozkład |
| Kabała z Toledo | 12 | `kt-01` (0.96) | 22.0% | 0.096 | 🟢 Zdrowy rozkład |
| Święte Oficjum | 12 | `so-11` (0.94) | 27.5% | 0.113 | 🟢 Zdrowy rozkład |

---

## 3. ⏳ Warstwa II — Kronika Dziejów w 4P (Ablacja 8 Kart Wydarzeń Czasu)

Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans w 4P:

| ID | Karta Wydarzenia | 4P Score | $\Delta$ 4P | Średnia Er | Deadlock % | Status Roli w Kronice |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `time-01` | **Kapitulacja Grenady** | 90.9 → 🟢 ** 90.4** (`🔻 -0.5`) | `-0.5 pkt` | 5.85 Er | 0.0% | ⚖️ Neutralna Kronika |
| `time-02` | **Godzina Policyjna** | 90.9 → 🟢 ** 90.3** (`🔻 -0.6`) | `-0.6 pkt` | 5.82 Er | 0.0% | ⚖️ Neutralna Kronika |
| `time-03` | **Flota Odkrywców** | 90.9 → 🟢 ** 90.5** (`🔻 -0.4`) | `-0.4 pkt` | 5.89 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-04` | **Rewizja w Dzielnicach** | 90.9 → 🟡 ** 89.7** (`🔻 -1.2`) | `-1.2 pkt` | 5.87 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-05` | **Gorączka Donosów** | 90.9 → 🟡 ** 89.1** (`🔻 -1.8`) | `-1.8 pkt` | 5.84 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-06` | **Nocna Obława** | 90.9 → 🟡 ** 88.7** (`🔻 -2.2`) | `-2.2 pkt` | 5.83 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-07` | **Bunt w Lochach** | 90.9 → 🟡 ** 89.2** (`🔻 -1.7`) | `-1.7 pkt` | 5.83 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-08` | **Święte Przymierze** | 90.9 → 🟡 ** 82.5** (`🔻 -8.4`) | `-8.4 pkt` | 5.73 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-09` | **Jarmark Królewski** | 90.9 → 🟡 ** 89.6** (`🔻 -1.3`) | `-1.3 pkt` | 5.83 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-10` | **Amnestia Biskupia** | 90.9 → 🟢 ** 90.2** (`🔻 -0.7`) | `-0.7 pkt` | 5.82 Er | 0.0% | ⚖️ Neutralna Kronika |

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
| **Szlak Morski: era 4 → nigdy (99)** | Poziom 4: Warianty i Modyfikatory | 90.9 → 🟢 ** 90.0** (`🔻 -0.9`) | `-0.9 pkt` | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |

### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)

| Badany Podsystem / Modyfikator L1 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Limit Er: 15 → 7 (skrajna presja)** | 90.9 → 🟡 ** 83.4** (`🔻 -7.5`) | `-7.5 pkt` | 5.69 Er | 10.4% | 4.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Próg Oskarżenia: 7 → 1** | 90.9 → 🔴 ** 28.0** (`🔻 -62.9`) | `-62.9 pkt` | 5.50 Er | 0.0% | 2.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Oskarżenia: 7 → 14** | 90.9 → 🔴 ** 32.1** (`🔻 -58.8`) | `-58.8 pkt` | 6.41 Er | 0.0% | 5.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 0zł (wyłączenie)** | 90.9 → 🔴 ** 50.0** (`🔻 -40.9`) | `-40.9 pkt` | 6.51 Er | 0.0% | 11.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 8zł** | 90.9 → 🔴 ** 25.4** (`🔻 -65.5`) | `-65.5 pkt` | 5.04 Er | 0.0% | 1.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 1** | 90.9 → 🔴 ** 30.8** (`🔻 -60.1`) | `-60.1 pkt` | 6.76 Er | 0.0% | 5.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 6** | 90.9 → 🟠 ** 72.9** (`🔻 -18.0`) | `-18.0 pkt` | 5.49 Er | 0.0% | 4.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 1** | 90.9 → 🔴 **  8.3** (`🔻 -82.6`) | `-82.6 pkt` | 8.75 Er | 0.7% | 41.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 10** | 90.9 → 🔴 **  6.6** (`🔻 -84.3`) | `-84.3 pkt` | 4.91 Er | 0.0% | 3.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: cooldown 3 → 0 (co erę)** | 90.9 → 🔴 ** 12.6** (`🔻 -78.3`) | `-78.3 pkt` | 4.95 Er | 0.0% | 5.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: całkowite wyłączenie** | 90.9 → 🔴 ** 60.9** (`🔻 -30.0`) | `-30.0 pkt` | 5.98 Er | 0.0% | 4.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Akcja Gospodarcza: 0zł (brak zysku złota)** | 90.9 → 🔴 ** 50.9** (`🔻 -40.0`) | `-40.0 pkt` | 5.93 Er | 0.0% | 6.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Akcja Gospodarcza: 1 → 2 (podwojenie)** | 90.9 → 🔴 ** 49.0** (`🔻 -41.9`) | `-41.9 pkt` | 5.69 Er | 0.0% | 3.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Obserwowanej: 3 → 2 (skrajna presja)** | 90.9 → 🟠 ** 75.8** (`🔻 -15.1`) | `-15.1 pkt` | 5.74 Er | 0.0% | 4.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)

| Badany Warunek Zwycięstwa L2 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: stosy 7 → 1** | 90.9 → 🔴 ** 17.6** (`🔻 -73.3`) | `-73.3 pkt` | 3.95 Er | 0.0% | 3.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: stosy 7 → 14** | 90.9 → 🟠 ** 65.5** (`🔻 -25.4`) | `-25.4 pkt` | 5.91 Er | 0.0% | 4.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 1** | 90.9 → 🔴 ** 17.6** (`🔻 -73.3`) | `-73.3 pkt` | 3.45 Er | 0.0% | 3.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 6** | 90.9 → 🔴 ** 58.6** (`🔻 -32.3`) | `-32.3 pkt` | 5.90 Er | 0.0% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Cienie: relikwie 2 → 4** | 90.9 → 🔴 ** 32.6** (`🔻 -58.3`) | `-58.3 pkt` | 6.17 Er | 0.0% | 4.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: dekrety 2 → 4** | 90.9 → 🔴 ** 34.2** (`🔻 -56.7`) | `-56.7 pkt` | 6.09 Er | 0.0% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: wymóg haków 2 → 0** | 90.9 → 🟠 ** 76.4** (`🔻 -14.5`) | `-14.5 pkt` | 5.78 Er | 0.0% | 4.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Korona: wymóg haków 2 → 4** | 90.9 → 🔴 ** 34.1** (`🔻 -56.8`) | `-56.8 pkt` | 6.09 Er | 0.0% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: fragmenty 3 → 1** | 90.9 → 🔴 ** 56.3** (`🔻 -34.6`) | `-34.6 pkt` | 6.03 Er | 0.0% | 4.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: fragmenty 3 → 6** | 90.9 → 🔴 ** 33.4** (`🔻 -57.5`) | `-57.5 pkt` | 6.12 Er | 0.0% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 9 → 1** | 90.9 → 🔴 ** 17.8** (`🔻 -73.1`) | `-73.1 pkt` | 3.00 Er | 0.0% | 2.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 9 → 18** | 90.9 → 🔴 ** 32.4** (`🔻 -58.5`) | `-58.5 pkt` | 6.09 Er | 0.0% | 4.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)

| Badany Wariant / Modyfikator L4 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kronika Dziejów: całkowite wyłączenie** | 90.9 → 🟠 ** 65.5** (`🔻 -25.4`) | `-25.4 pkt` | 5.85 Er | 0.0% | 5.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kronika Dziejów: co 3 Ery (spowolniony zegar)** | 90.9 → 🟠 ** 75.4** (`🔻 -15.5`) | `-15.5 pkt` | 5.87 Er | 0.0% | 5.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Inkwizytor Patrol: ruch 1 → 0 (wyłączenie)** | 90.9 → 🔴 ** 32.4** (`🔻 -58.5`) | `-58.5 pkt` | 6.39 Er | 0.0% | 4.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Inkwizytor Patrol: ruch x2 (podwojona prędkość)** | 90.9 → 🟡 ** 85.8** (`🔻 -5.1`) | `-5.1 pkt` | 5.79 Er | 0.0% | 4.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Szlak Morski: era 4 → nigdy (99)** | 90.9 → 🟢 ** 90.0** (`🔻 -0.9`) | `-0.9 pkt` | 5.85 Er | 0.0% | 4.5% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |

---

## 5. 👥 Warstwa IV — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych. Kolumna win share to HUD kanonu; setup+witalność to stary blend (kara martwej ścieżki).

| Nieobecna Frakcja | Setup Testowy | Win share | Setup+witalność | Diagnoza |
| :--- | :--- | :---: | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`88.2`** | `88.2` | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`90.0`** | `90.0` | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`96.5`** | `96.5` | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`87.7`** | `87.7` | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`92.0`** | `92.0` | Brak presji stosów i bezpośredniego Inkwizytora |