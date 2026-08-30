# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v1.0-alpha.101

**Wersja Gry:** `v1.0-alpha.101` | **Data Badania:** 2026-08-30 00:51 | **Próba:** 10000 gier/setup (50000 gier na wariant) | **Ziarno:** 42
**4P Score (win share):** 🟢 ** 90.7** pkt | **Witalność (osobna kara):** `0.000` | **Śr. Er:** `5.83` | **Deadlocki:** `0.0%` | **Pas Biedy:** `4.5%`
**Udziały 4P:** CAA 25.3% · GC 25.6% · KB 25.6% · KT 24.8% · SO 23.7%

Klasyfikacja L1/L2/L4 i Δ 4P liczą wyłącznie równość win share (`calculate_balance_score`). Kara witalności jest osobno.

---

## 0. Wady z tej próby (nie HUD win share)

Kubełki klasyfikatora i ostrzeżenia witalności z bieżącego runu.

- **Autopodatek (SELF_HARM):** 2/60
- **DEAD_WEIGHT:** `gc-05` Fałszywy Świadek, `gc-08` Zatrute Złoto, `so-05` Wezwanie do Trybunału, `so-09` Świadek Koronny
- **Karty Kroniki |Δ4P| ≤ 0.8:** 3/10
- **Ablacja całej Kroniki (`L4_NO_TIME_DECK`):** Δ4P -24.3 (STABILIZER)
- **Mechaniki WEAK/NEUTRAL:** Inkwizytor Patrol: ruch x2 (podwojona prędkość)
- **Mechaniki DEAD:** Szlak Morski: era 4 → nigdy (99)

---

## 1. 🗺️ Podsumowanie Ekosystemu Kart Kanonu 4P (Matryca Wpływu Kart, 60 kart)

Rozkład wszystkich 60 kart frakcyjnych w matrycy **Wpływ na Frakcję ($\Delta \text{Share}$)** vs **Wpływ na Kanon 4P ($\Delta \text{4P Score}$)**:

| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |
| :--- | :---: | :---: | :--- | :--- |
| 🩸 **Autopodatek (Self-Harm)** | **2** | 3.3% | Wyłączenie **podnosi** win share własnej frakcji — karta jest haraczem, nie silnikiem | **Rework / osłabienie kosztu, nie filar** |
| 🔄 **Rozcieńczalnik Talii (Tempo Filler)** | **7** | 11.7% | Normalna karta tempa — ablacja fałszywie flaguje ją jako autopodatek z powodu odchudzenia talii | **Normalny element deckbuildingu** |
| 💤 **Karta Pasywna (Dead Weight)** | **4** | 6.7% | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia lub wycięcia** |
| ⚠️ **Karta Destabilizująca (Disruptor)** | **0** | 0.0% | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |
| ⚖️ **Zbalansowane Narzędzie** | **28** | 46.7% | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Narzędzie, nie złoty środek całego kanonu** |
| 👑 / ⚓ **Filar / Kotwica Kanonu** | **19** | 31.7% | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |

---

## 2. 🃏 Warstwa I — Szczegółowa Analiza 60 Kart Frakcji w Kanonie 4P

### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)
Karty, których brak powoduje spadek wyniku Kanonu 4P o $\ge 4.0$ pkt lub załamanie winrate frakcji o $\ge 4.0\%$ — **bez** autopodatków (te są w 2.1b):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kt-10` **Pieczęć Salomona** | Kabała z Toledo | 4zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.8% → **0.0%** | **`-24.8%`** | 90.7 → **33.3 pkt** (`-57.4`) |
| `kb-09` **Dekret Królewski** | Korona & Borgiowie | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.6% → **1.2%** | **`-24.4%`** | 90.7 → **36.1 pkt** (`-54.6`) |
| `caa-10` **Echo Alhambry** | Cienie Al-Andalus | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.3% → **4.7%** | **`-20.6%`** | 90.7 → **38.0 pkt** (`-52.7`) |
| `kt-02` **Transmutacja Złota** | Kabała z Toledo | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.8% → **6.8%** | **`-18.0%`** | 90.7 → **44.4 pkt** (`-46.3`) |
| `caa-05` **Ukryty Kurier** | Cienie Al-Andalus | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.3% → **13.4%** | **`-11.9%`** | 90.7 → **58.2 pkt** (`-32.5`) |
| `kb-02` **Pobór Podatków** | Korona & Borgiowie | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.6% → **14.8%** | **`-10.8%`** | 90.7 → **66.2 pkt** (`-24.5`) |
| `kt-11` **Medytacja Sefirot** | Kabała z Toledo | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.8% → **16.2%** | **`-8.6%`** | 90.7 → **67.2 pkt** (`-23.5`) |
| `kt-03` **Zakazana Wiedza** | Kabała z Toledo | 0zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 24.8% → **20.0%** | **`-4.8%`** | 90.7 → **74.2 pkt** (`-16.5`) |
| `kt-05` **Wskazówka Cyklu** | Kabała z Toledo | 1zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 24.8% → **19.6%** | **`-5.2%`** | 90.7 → **77.4 pkt** (`-13.3`) |
| `kb-10` **Pieczęć Korony** | Korona & Borgiowie | 4zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 25.6% → **20.2%** | **`-5.4%`** | 90.7 → **77.9 pkt** (`-12.8`) |
| `so-10` **Oczyść Miasto** | Święte Oficjum | 5zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 23.7% → **19.9%** | **`-3.8%`** | 90.7 → **79.0 pkt** (`-11.7`) |
| `caa-06` **Ucieczka z Lochów** | Cienie Al-Andalus | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.3% → **21.5%** | **`-3.8%`** | 90.7 → **81.8 pkt** (`-8.9`) |
| `gc-10` **Upadek Domu** | Gildia Cieni | 4zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 25.6% → **21.2%** | **`-4.4%`** | 90.7 → **83.2 pkt** (`-7.5`) |
| `gc-09` **Lista Dłużników** | Gildia Cieni | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.6% → **21.0%** | **`-4.6%`** | 90.7 → **83.6 pkt** (`-7.1`) |
| `kt-09` **Fragment Kodeksu** | Kabała z Toledo | 1zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.8% → **23.2%** | **`-1.6%`** | 90.7 → **84.9 pkt** (`-5.8`) |
| `so-03` **Podejrzenie** | Święte Oficjum | 2zł / 4☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.7% → **25.2%** | **`+1.5%`** | 90.7 → **85.1 pkt** (`-5.6`) |
| `so-04` **Publiczne Ostrzeżenie** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.7% → **23.2%** | **`-0.5%`** | 90.7 → **87.1 pkt** (`-3.6`) |
| `so-08` **Nasłanie Inkwizytora** | Święte Oficjum | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.7% → **23.6%** | **`-0.1%`** | 90.7 → **88.6 pkt** (`-2.1`) |
| `gc-04` **Informator** | Gildia Cieni | 1zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 25.6% → **22.9%** | **`-2.7%`** | 90.7 → **88.9 pkt** (`-1.8`) |

### 2.1b. 🩸 Autopodatek Frakcji (Self-Harm)
Karty, których wyłączenie **podnosi** win share własnej frakcji. Gracz zauważy je jako haracz, nawet gdy stół 4P jest równy dzięki temu haraczowi.

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kt-07` **Archiwum Ukryte** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.8% → **29.2%** | **`+4.4%`** | 90.7 → **83.5 pkt** (`-7.2`) |
| `caa-02` **Złoto z Kryjówki** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.3% → **28.8%** | **`+3.5%`** | 90.7 → **82.8 pkt** (`-7.9`) |

### 2.2. ⚠️ Karty Destabilizujące Kanon 4P (Disruptors)
Karty, których wyłączenie podnosi 4P Score ($\Delta \text{4P} \ge +1.5$ pkt):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *Brak kart destabilizujących* | - | - | - | - | - | - |

### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich 60 Kart Frakcji w Kanonie 4P

| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Play-Rate | Faction Win Share 4P | $\Delta$ Frakcji | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `caa-01` | **Przejście Podziemiami** | Cienie Al-Andalus | 0 | 0 | 0.97 | 25.3% → 29.3% | `+4.0%` | 82.0 | `-8.7` | 5.75 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-02` | **Złoto z Kryjówki** | Cienie Al-Andalus | 0 | 0 | 0.11 | 25.3% → 28.8% | `+3.5%` | 82.8 | `-7.9` | 5.75 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-03` | **Cień na Rynku** | Cienie Al-Andalus | 0 | 1 | 0.92 | 25.3% → 33.0% | `+7.7%` | 68.6 | `-22.1` | 5.80 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-04` | **Fałszywy Trop** | Cienie Al-Andalus | 0 | 0 | 0.97 | 25.3% → 29.8% | `+4.5%` | 80.4 | `-10.3` | 5.73 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-05` | **Ukryty Kurier** | Cienie Al-Andalus | 0 | 0 | 1.02 | 25.3% → 13.4% | `-11.9%` | 58.2 | `-32.5` | 6.01 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `caa-12` | **Skrytka w Murach** | Cienie Al-Andalus | 1 | 0 | 0.87 | 25.3% → 30.7% | `+5.4%` | 77.3 | `-13.4` | 5.72 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-06` | **Ucieczka z Lochów** | Cienie Al-Andalus | 0 | 0 | 0.62 | 25.3% → 21.5% | `-3.8%` | 81.8 | `-8.9` | 5.81 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `caa-07` | **Szantaż Bractwa** | Cienie Al-Andalus | 0 | 0 | 0.34 | 25.3% → 28.8% | `+3.5%` | 82.5 | `-8.2` | 5.75 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `caa-11` | **Nocna Zmiana Warty** | Cienie Al-Andalus | 1 | 0 | 0.34 | 25.3% → 29.1% | `+3.8%` | 81.8 | `-8.9` | 5.75 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `caa-08` | **Kaptur Nocy** | Cienie Al-Andalus | 2 | 0 | 0.72 | 25.3% → 29.7% | `+4.4%` | 80.0 | `-10.7` | 5.74 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-09` | **Kurier Relikwii** | Cienie Al-Andalus | 0 | 0 | 0.90 | 25.3% → 30.5% | `+5.2%` | 77.9 | `-12.8` | 5.72 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-10` | **Echo Alhambry** | Cienie Al-Andalus | 2 | 0 | 1.00 | 25.3% → 4.7% | `-20.6%` | 38.0 | `-52.7` | 6.11 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `gc-02` | **Czarny Rynek** | Gildia Cieni | 0 | 0 | 0.79 | 25.6% → 26.2% | `+0.6%` | 89.6 | `-1.1` | 5.80 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-12` | **Złodziejski Zwiad** | Gildia Cieni | 0 | 2 | 0.44 | 25.6% → 28.5% | `+2.9%` | 84.3 | `-6.4` | 5.78 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `gc-01` | **Przekupiony Strażnik** | Gildia Cieni | 1 | 1 | 0.48 | 25.6% → 26.8% | `+1.2%` | 90.0 | `-0.7` | 5.79 | 0.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `gc-03` | **Podrzucenie Księgi** | Gildia Cieni | 1 | 2 | 0.08 | 25.6% → 27.0% | `+1.4%` | 89.2 | `-1.5` | 5.79 | 0.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `gc-04` | **Informator** | Gildia Cieni | 1 | 1 | 0.80 | 25.6% → 22.9% | `-2.7%` | 88.9 | `-1.8` | 5.86 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `gc-05` | **Fałszywy Świadek** | Gildia Cieni | 1 | 0 | 0.00 | 25.6% → 25.5% | `-0.1%` | 89.8 | `-0.9` | 5.82 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `gc-07` | **Skrytobójstwo** | Gildia Cieni | 0 | 0 | 0.79 | 25.6% → 26.9% | `+1.3%` | 89.1 | `-1.6` | 5.87 | 0.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `gc-11` | **Fałszywe Świadectwo Cechu** | Gildia Cieni | 0 | 2 | 0.31 | 25.6% → 27.7% | `+2.1%` | 87.2 | `-3.5` | 5.80 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `gc-08` | **Zatrute Złoto** | Gildia Cieni | 1 | 2 | 0.00 | 25.6% → 26.8% | `+1.2%` | 89.3 | `-1.4` | 5.81 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `gc-06` | **Szantaż** | Gildia Cieni | 3 | 1 | 0.44 | 25.6% → 25.2% | `-0.4%` | 91.6 | `+0.9` | 5.83 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-09` | **Lista Dłużników** | Gildia Cieni | 1 | 0 | 0.79 | 25.6% → 21.0% | `-4.6%` | 83.6 | `-7.1` | 5.85 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `gc-10` | **Upadek Domu** | Gildia Cieni | 4 | 2 | 0.47 | 25.6% → 21.2% | `-4.4%` | 83.2 | `-7.5` | 5.89 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-01` | **Rozkaz Dworu** | Korona & Borgiowie | 1 | 1 | 0.23 | 25.6% → 35.7% | `+10.1%` | 63.6 | `-27.1` | 5.72 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kb-02` | **Pobór Podatków** | Korona & Borgiowie | 1 | 0 | 0.85 | 25.6% → 14.8% | `-10.8%` | 66.2 | `-24.5` | 5.95 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-03` | **Plotka Dworska** | Korona & Borgiowie | 1 | 1 | 0.60 | 25.6% → 36.1% | `+10.5%` | 61.9 | `-28.8` | 5.73 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-11` | **Tajny Emisariusz** | Korona & Borgiowie | 1 | 0 | 0.84 | 25.6% → 33.2% | `+7.6%` | 71.4 | `-19.3` | 5.71 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-04` | **Faworyt Dworu** | Korona & Borgiowie | 2 | 0 | 0.73 | 25.6% → 33.7% | `+8.1%` | 70.1 | `-20.6` | 5.72 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-05` | **List Żelazny** | Korona & Borgiowie | 2 | 1 | 0.82 | 25.6% → 35.6% | `+10.0%` | 64.7 | `-26.0` | 5.67 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-12` | **Szantaż Salonowy** | Korona & Borgiowie | 1 | 2 | 0.82 | 25.6% → 30.2% | `+4.6%` | 78.5 | `-12.2` | 5.77 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-06` | **Areszt Królewski** | Korona & Borgiowie | 2 | 0 | 0.26 | 25.6% → 34.1% | `+8.5%` | 68.5 | `-22.2` | 5.73 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kb-07` | **Szantaż Pieczęcią** | Korona & Borgiowie | 2 | 0 | 0.52 | 25.6% → 34.4% | `+8.8%` | 67.8 | `-22.9` | 5.71 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-08` | **Przekupstwo Sędziego** | Korona & Borgiowie | 2 | 0 | 0.52 | 25.6% → 34.4% | `+8.8%` | 67.8 | `-22.9` | 5.71 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-09` | **Dekret Królewski** | Korona & Borgiowie | 2 | 0 | 0.86 | 25.6% → 1.2% | `-24.4%` | 36.1 | `-54.6` | 6.08 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-10` | **Pieczęć Korony** | Korona & Borgiowie | 4 | 1 | 0.17 | 25.6% → 20.2% | `-5.4%` | 77.9 | `-12.8` | 5.96 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-02` | **Transmutacja Złota** | Kabała z Toledo | 0 | 0 | 0.96 | 24.8% → 6.8% | `-18.0%` | 44.4 | `-46.3` | 5.98 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-03` | **Zakazana Wiedza** | Kabała z Toledo | 0 | 2 | 0.75 | 24.8% → 20.0% | `-4.8%` | 74.2 | `-16.5` | 6.08 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-01` | **Ścieżka Wtajemniczenia** | Kabała z Toledo | 1 | 0 | 0.96 | 24.8% → 29.9% | `+5.1%` | 81.5 | `-9.2` | 5.70 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-04` | **Zwierciadło Herezji** | Kabała z Toledo | 1 | 0 | 0.25 | 24.8% → 29.4% | `+4.6%` | 83.2 | `-7.5` | 5.74 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kt-05` | **Wskazówka Cyklu** | Kabała z Toledo | 1 | 1 | 0.96 | 24.8% → 19.6% | `-5.2%` | 77.4 | `-13.3` | 6.01 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-12` | **Strażnik Archiwum** | Kabała z Toledo | 1 | 0 | 0.88 | 24.8% → 29.1% | `+4.3%` | 83.7 | `-7.0` | 5.71 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-07` | **Archiwum Ukryte** | Kabała z Toledo | 1 | 0 | 0.09 | 24.8% → 29.2% | `+4.4%` | 83.5 | `-7.2` | 5.74 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-08` | **Areszt Wiedzy** | Kabała z Toledo | 1 | 0 | 0.79 | 24.8% → 27.8% | `+3.0%` | 86.6 | `-4.1` | 5.75 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-06` | **Przesłuchanie Imienia** | Kabała z Toledo | 2 | 0 | 0.73 | 24.8% → 33.5% | `+8.7%` | 70.4 | `-20.3` | 5.69 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-11` | **Medytacja Sefirot** | Kabała z Toledo | 2 | 0 | 0.90 | 24.8% → 16.2% | `-8.6%` | 67.2 | `-23.5` | 5.78 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-09` | **Fragment Kodeksu** | Kabała z Toledo | 1 | 1 | 0.96 | 24.8% → 23.2% | `-1.6%` | 84.9 | `-5.8` | 5.95 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kt-10` | **Pieczęć Salomona** | Kabała z Toledo | 4 | 0 | 0.50 | 24.8% → 0.0% | `-24.8%` | 33.3 | `-57.4` | 6.10 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `so-05` | **Wezwanie do Trybunału** | Święte Oficjum | 0 | 4 | 0.00 | 23.7% → 21.0% | `-2.7%` | 84.1 | `-6.6` | 5.86 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `so-01` | **Patrol Familiariuszy** | Święte Oficjum | 1 | 2 | 0.25 | 23.7% → 25.4% | `+1.7%` | 89.6 | `-1.1` | 5.83 | 0.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `so-02` | **Skarbiec Trybunału** | Święte Oficjum | 1 | 2 | 0.52 | 23.7% → 24.0% | `+0.3%` | 89.9 | `-0.8` | 5.86 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-04` | **Publiczne Ostrzeżenie** | Święte Oficjum | 1 | 0 | 0.90 | 23.7% → 23.2% | `-0.5%` | 87.1 | `-3.6` | 5.77 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-12` | **Straż Trybunalska** | Święte Oficjum | 1 | 2 | 0.26 | 23.7% → 24.7% | `+1.0%` | 89.1 | `-1.6` | 5.83 | 0.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `so-03` | **Podejrzenie** | Święte Oficjum | 2 | 4 | 0.30 | 23.7% → 25.2% | `+1.5%` | 85.1 | `-5.6` | 5.88 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-08` | **Nasłanie Inkwizytora** | Święte Oficjum | 0 | 0 | 0.89 | 23.7% → 23.6% | `-0.1%` | 88.6 | `-2.1` | 5.79 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-11` | **Dekret Czystości Wiary** | Święte Oficjum | 0 | 1 | 0.93 | 23.7% → 24.6% | `+0.9%` | 90.0 | `-0.7` | 5.83 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-07` | **Przesłuchanie Oficjum** | Święte Oficjum | 1 | 0 | 0.86 | 23.7% → 25.1% | `+1.4%` | 90.6 | `-0.1` | 5.75 | 0.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `so-09` | **Świadek Koronny** | Święte Oficjum | 1 | 1 | 0.16 | 23.7% → 24.3% | `+0.6%` | 90.5 | `-0.2` | 5.84 | 0.0% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `so-06` | **Areszt Trybunalski** | Święte Oficjum | 2 | 0 | 0.93 | 23.7% → 25.3% | `+1.6%` | 91.1 | `+0.4` | 5.78 | 0.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `so-10` | **Oczyść Miasto** | Święte Oficjum | 5 | 1 | 0.80 | 23.7% → 19.9% | `-3.8%` | 79.0 | `-11.7` | 5.95 | 0.0% | 👑 FILAR KANONU (Core Keystone) |

### 2.4. 🎯 Monokultura Talii (Deck Concentration Index)

Jak mocno skoncentrowane jest zagrywanie kart w obrębie każdej frakcji.
Wskaźnik HHI (Herfindahl–Hirschman Index) mierzy koncentrację: HHI = 1.0 oznacza, że 100% zagrań to 1 karta; HHI ≈ 1/N oznacza idealnie równomierny rozkład.

| Frakcja | Kart w Talii | Top Karta (Play-Rate) | Top 2 (%) | HHI | Ocena |
| :--- | :---: | :--- | :---: | :---: | :--- |
| Cienie Al-Andalus | 12 | `caa-05` (1.02) | 23.0% | 0.097 | 🟢 Zdrowy rozkład |
| Gildia Cieni | 12 | `gc-04` (0.80) | 29.6% | 0.119 | 🟢 Zdrowy rozkład |
| Korona & Borgiowie | 12 | `kb-09` (0.86) | 23.7% | 0.098 | 🟢 Zdrowy rozkład |
| Kabała z Toledo | 12 | `kt-01` (0.96) | 22.1% | 0.096 | 🟢 Zdrowy rozkład |
| Święte Oficjum | 12 | `so-11` (0.93) | 27.4% | 0.113 | 🟢 Zdrowy rozkład |

---

## 3. ⏳ Warstwa II — Kronika Dziejów w 4P (Ablacja 8 Kart Wydarzeń Czasu)

Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans w 4P:

| ID | Karta Wydarzenia | 4P Score | $\Delta$ 4P | Średnia Er | Deadlock % | Status Roli w Kronice |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `time-01` | **Kapitulacja Grenady** | 90.7 → 🟡 ** 89.7** (`🔻 -1.0`) | `-1.0 pkt` | 5.85 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-02` | **Godzina Policyjna** | 90.7 → 🟡 ** 89.4** (`🔻 -1.3`) | `-1.3 pkt` | 5.81 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-03` | **Flota Odkrywców** | 90.7 → 🟢 ** 90.5** (`🔻 -0.2`) | `-0.2 pkt` | 5.89 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-04` | **Rewizja w Dzielnicach** | 90.7 → 🟡 ** 89.2** (`🔻 -1.5`) | `-1.5 pkt` | 5.85 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-05` | **Gorączka Donosów** | 90.7 → 🟡 ** 88.4** (`🔻 -2.3`) | `-2.3 pkt` | 5.81 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-06` | **Nocna Obława** | 90.7 → 🟡 ** 88.9** (`🔻 -1.8`) | `-1.8 pkt` | 5.81 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-07` | **Bunt w Lochach** | 90.7 → 🟡 ** 88.2** (`🔻 -2.5`) | `-2.5 pkt` | 5.81 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-08` | **Święte Przymierze** | 90.7 → 🟡 ** 84.4** (`🔻 -6.3`) | `-6.3 pkt` | 5.72 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-09` | **Jarmark Królewski** | 90.7 → 🟢 ** 90.8** (`⬆️ +0.1`) | `+0.1 pkt` | 5.82 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-10` | **Amnestia Biskupia** | 90.7 → 🟢 ** 91.5** (`⬆️ +0.8`) | `+0.8 pkt` | 5.80 Er | 0.0% | ⚖️ Neutralna Kronika |

---

## 4. ⚙️ Warstwa III — Matryca 9 Obszarów Wpływu Mechanik Gry (L1, L2, L4)

Mechaniki w tym raporcie: **skraj albo wyłączenie**. Testy ±1 są w `audit_level1` / `audit_level2` / `audit_level4`. **Δ≈0 nie jest harmonią.**

| Kategoria Mechaniki | Liczba Testów | Rola w Ekosystemie Kanonu 4P | Rekomendacja Balansowa |
| :--- | :---: | :--- | :--- |
| 👑 / 🛡️ **Filary i Bezpieczniki** | **29** | Ablacja wali w stół — gracze czują tę gałkę | **Cel kanonu** |
| ⚠️ **Za słabe dźwignie** | **1** | Rusza share, nie trzyma stołu — nie jest „zbalansowana” | **Wzmocnić aż będzie filarem** |
| 💤 **Martwe / uśpione ścieżki** | **1** | Dual-win z witalności albo ablacja Δ≈0 | Wada pomiaru, nie harmonia |
| ⚠️ / 💡 **Wady bieżącej wartości** | **0** | Inna wartość gałki **podnosi** 4P — obecny setting szkodzi | **Przekręcić albo rework** |

### 4.0. ⚠️ Problematyczne mechaniki (osobny wykaz)
Wszystkie mechaniki z grup **DEAD**, **WEAK/NEUTRAL** i **DISRUPTOR**: ścieżki dual-win z `evaluate_vitality`, testy z $|\Delta\text{4P}| \le 0.8$ i ruchem share $\le 1.5$ pp (DEAD), za słabe dźwignie (WEAK) oraz wady bieżącej wartości (DISRUPTOR).

| Badany Podsystem | Kategoria | 4P Score | $\Delta$ 4P | Klasyfikacja |
| :--- | :--- | :---: | :---: | :--- |
| **Szlak Morski: era 4 → nigdy (99)** | Poziom 4: Warianty i Modyfikatory | 90.7 → 🟢 ** 90.2** (`🔻 -0.5`) | `-0.5 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Inkwizytor Patrol: ruch x2 (podwojona prędkość)** | Poziom 4: Warianty i Modyfikatory | 90.7 → 🟡 ** 87.0** (`🔻 -3.7`) | `-3.7 pkt` | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |

### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)

| Badany Podsystem / Modyfikator L1 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Limit Er: 15 → 7 (skrajna presja)** | 90.7 → 🟡 ** 83.1** (`🔻 -7.6`) | `-7.6 pkt` | 5.68 Er | 10.1% | 4.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Próg Oskarżenia: 7 → 1** | 90.7 → 🔴 ** 27.7** (`🔻 -63.0`) | `-63.0 pkt` | 5.51 Er | 0.0% | 2.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Oskarżenia: 7 → 14** | 90.7 → 🔴 ** 32.3** (`🔻 -58.4`) | `-58.4 pkt` | 6.38 Er | 0.0% | 5.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 0zł (wyłączenie)** | 90.7 → 🔴 ** 51.2** (`🔻 -39.5`) | `-39.5 pkt` | 6.52 Er | 0.0% | 11.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 8zł** | 90.7 → 🔴 ** 26.3** (`🔻 -64.4`) | `-64.4 pkt` | 5.04 Er | 0.0% | 1.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 1** | 90.7 → 🔴 ** 30.4** (`🔻 -60.3`) | `-60.3 pkt` | 6.76 Er | 0.0% | 5.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 6** | 90.7 → 🟠 ** 76.9** (`🔻 -13.8`) | `-13.8 pkt` | 5.49 Er | 0.0% | 4.3% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Limit kart na ręce: 5 → 1** | 90.7 → 🔴 **  8.2** (`🔻 -82.5`) | `-82.5 pkt` | 8.74 Er | 0.7% | 40.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 10** | 90.7 → 🔴 **  6.6** (`🔻 -84.1`) | `-84.1 pkt` | 4.90 Er | 0.0% | 3.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: cooldown 3 → 0 (co erę)** | 90.7 → 🔴 ** 12.8** (`🔻 -77.9`) | `-77.9 pkt` | 4.95 Er | 0.0% | 5.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: całkowite wyłączenie** | 90.7 → 🔴 ** 59.0** (`🔻 -31.7`) | `-31.7 pkt` | 5.97 Er | 0.0% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Akcja Gospodarcza: 0zł (brak zysku złota)** | 90.7 → 🔴 ** 50.5** (`🔻 -40.2`) | `-40.2 pkt` | 5.93 Er | 0.0% | 6.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Akcja Gospodarcza: 1 → 2 (podwojenie)** | 90.7 → 🔴 ** 49.3** (`🔻 -41.4`) | `-41.4 pkt` | 5.69 Er | 0.0% | 3.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Obserwowanej: 3 → 2 (skrajna presja)** | 90.7 → 🟡 ** 80.8** (`🔻 -9.9`) | `-9.9 pkt` | 5.73 Er | 0.0% | 4.4% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |

### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)

| Badany Warunek Zwycięstwa L2 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: stosy 7 → 1** | 90.7 → 🔴 ** 17.7** (`🔻 -73.0`) | `-73.0 pkt` | 3.96 Er | 0.0% | 3.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: stosy 7 → 14** | 90.7 → 🟠 ** 66.7** (`🔻 -24.0`) | `-24.0 pkt` | 5.90 Er | 0.0% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 1** | 90.7 → 🔴 ** 17.4** (`🔻 -73.3`) | `-73.3 pkt` | 3.46 Er | 0.0% | 3.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 6** | 90.7 → 🔴 ** 58.2** (`🔻 -32.5`) | `-32.5 pkt` | 5.90 Er | 0.0% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Cienie: relikwie 2 → 4** | 90.7 → 🔴 ** 31.5** (`🔻 -59.2`) | `-59.2 pkt` | 6.17 Er | 0.0% | 4.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: dekrety 2 → 4** | 90.7 → 🔴 ** 34.4** (`🔻 -56.3`) | `-56.3 pkt` | 6.08 Er | 0.0% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: wymóg haków 2 → 0** | 90.7 → 🟠 ** 77.2** (`🔻 -13.5`) | `-13.5 pkt` | 5.76 Er | 0.0% | 4.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Korona: wymóg haków 2 → 4** | 90.7 → 🔴 ** 34.3** (`🔻 -56.4`) | `-56.4 pkt` | 6.08 Er | 0.0% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: fragmenty 3 → 1** | 90.7 → 🔴 ** 55.6** (`🔻 -35.1`) | `-35.1 pkt` | 6.04 Er | 0.0% | 4.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: fragmenty 3 → 6** | 90.7 → 🔴 ** 33.3** (`🔻 -57.4`) | `-57.4 pkt` | 6.11 Er | 0.0% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 9 → 1** | 90.7 → 🔴 ** 18.3** (`🔻 -72.4`) | `-72.4 pkt` | 2.99 Er | 0.0% | 2.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 9 → 18** | 90.7 → 🔴 ** 33.0** (`🔻 -57.7`) | `-57.7 pkt` | 6.08 Er | 0.0% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)

| Badany Wariant / Modyfikator L4 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kronika Dziejów: całkowite wyłączenie** | 90.7 → 🟠 ** 66.4** (`🔻 -24.3`) | `-24.3 pkt` | 5.85 Er | 0.0% | 5.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kronika Dziejów: co 3 Ery (spowolniony zegar)** | 90.7 → 🟠 ** 75.0** (`🔻 -15.7`) | `-15.7 pkt` | 5.86 Er | 0.0% | 5.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Inkwizytor Patrol: ruch 1 → 0 (wyłączenie)** | 90.7 → 🔴 ** 32.9** (`🔻 -57.8`) | `-57.8 pkt` | 6.38 Er | 0.0% | 4.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Inkwizytor Patrol: ruch x2 (podwojona prędkość)** | 90.7 → 🟡 ** 87.0** (`🔻 -3.7`) | `-3.7 pkt` | 5.78 Er | 0.0% | 4.5% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |
| **Szlak Morski: era 4 → nigdy (99)** | 90.7 → 🟢 ** 90.2** (`🔻 -0.5`) | `-0.5 pkt` | 5.84 Er | 0.0% | 4.5% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |

---

## 5. 👥 Warstwa IV — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych. Kolumna win share to HUD kanonu; setup+witalność to stary blend (kara martwej ścieżki).

| Nieobecna Frakcja | Setup Testowy | Win share | Setup+witalność | Diagnoza |
| :--- | :--- | :---: | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`87.6`** | `87.6` | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`89.2`** | `89.2` | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`98.1`** | `98.1` | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`85.1`** | `85.1` | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`93.3`** | `93.3` | Brak presji stosów i bezpośredniego Inkwizytora |