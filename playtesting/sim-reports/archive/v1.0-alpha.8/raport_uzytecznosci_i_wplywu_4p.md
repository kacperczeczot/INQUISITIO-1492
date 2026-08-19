# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v1.0-alpha.8

**Wersja Gry:** `v1.0-alpha.8` | **Data Badania:** 2026-08-19 12:49 | **Próba:** 5000 gier/setup (25000 gier na wariant) | **Ziarno:** 42
**4P Score (win share):** 🟡 ** 76.5** pkt | **Witalność (osobna kara):** `0.000` | **Śr. Er:** `6.21` | **Deadlocki:** `0.3%` | **Pas Biedy:** `1.6%`
**Udziały 4P:** CAA 21.7% · GC 26.4% · KB 25.6% · KT 24.7% · SO 26.6%

Klasyfikacja L1/L2/L4 i Δ 4P liczą wyłącznie równość win share (`calculate_balance_score`). Kara witalności jest osobno.

---

## 0. Wady z tej próby (nie HUD win share)

Kubełki klasyfikatora i ostrzeżenia witalności z bieżącego runu.

- **Share |Δ| ≥ 2.5 pp od 25%:** CAA 21.7%
- **Autopodatek (SELF_HARM):** 20/60
- **DEAD_WEIGHT:** `kb-01` Rozkaz Dworu, `kb-03` Plotka Dworska
- **Karty Kroniki |Δ4P| ≤ 0.8:** 2/10
- **Ablacja całej Kroniki (`L4_NO_TIME_DECK`):** Δ4P -14.9 (STABILIZER)
- **Mechaniki WEAK/NEUTRAL:** Werdykt Sądu: tajny (wyłączenie jawnej koordynacji)

---

## 1. 🗺️ Podsumowanie Ekosystemu Kart Kanonu 4P (Matryca Wpływu Kart, 60 kart)

Rozkład wszystkich 60 kart frakcyjnych w matrycy **Wpływ na Frakcję ($\Delta \text{Share}$)** vs **Wpływ na Kanon 4P ($\Delta \text{4P Score}$)**:

| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |
| :--- | :---: | :---: | :--- | :--- |
| 🩸 **Autopodatek (Self-Harm)** | **20** | 33.3% | Wyłączenie **podnosi** win share własnej frakcji — karta jest haraczem, nie silnikiem | **Rework / osłabienie kosztu, nie filar** |
| 💤 **Karta Pasywna (Dead Weight)** | **2** | 3.3% | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia lub wycięcia** |
| ⚠️ **Karta Destabilizująca (Disruptor)** | **0** | 0.0% | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |
| ⚖️ **Zbalansowane Narzędzie** | **15** | 25.0% | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Narzędzie, nie złoty środek całego kanonu** |
| 👑 / ⚓ **Filar / Kotwica Kanonu** | **23** | 38.3% | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |

---

## 2. 🃏 Warstwa I — Szczegółowa Analiza 60 Kart Frakcji w Kanonie 4P

### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)
Karty, których brak powoduje spadek wyniku Kanonu 4P o $\ge 4.0$ pkt lub załamanie winrate frakcji o $\ge 4.0\%$ — **bez** autopodatków (te są w 2.1b):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kt-03` **Zakazana Wiedza** | Kabała z Toledo | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.7% → **4.3%** | **`-20.4%`** | 76.5 → **27.6 pkt** (`-48.9`) |
| `kb-09` **Dekret Królewski** | Korona & Borgiowie | 4zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 25.6% → **0.1%** | **`-25.5%`** | 76.5 → **29.5 pkt** (`-47.0`) |
| `kb-10` **Pieczęć Korony** | Korona & Borgiowie | 3zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 25.6% → **0.2%** | **`-25.4%`** | 76.5 → **29.8 pkt** (`-46.7`) |
| `caa-10` **Echo Alhambry** | Cienie Al-Andalus | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 21.7% → **4.4%** | **`-17.3%`** | 76.5 → **38.5 pkt** (`-38.0`) |
| `kt-05` **Wskazówka Cyklu** | Kabała z Toledo | 1zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 24.7% → **14.3%** | **`-10.4%`** | 76.5 → **49.8 pkt** (`-26.7`) |
| `caa-05` **Ukryty Kurier** | Cienie Al-Andalus | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 21.7% → **13.0%** | **`-8.7%`** | 76.5 → **55.9 pkt** (`-20.6`) |
| `caa-03` **Cień na Rynku** | Cienie Al-Andalus | 0zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 21.7% → **21.2%** | **`-0.5%`** | 76.5 → **62.7 pkt** (`-13.8`) |
| `kt-10` **Pieczęć Salomona** | Kabała z Toledo | 2zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 24.7% → **19.0%** | **`-5.7%`** | 76.5 → **64.2 pkt** (`-12.3`) |
| `caa-02` **Złoto z Kryjówki** | Cienie Al-Andalus | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 21.7% → **23.2%** | **`+1.5%`** | 76.5 → **70.9 pkt** (`-5.6`) |
| `caa-12` **Skrytka w Murach** | Cienie Al-Andalus | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 21.7% → **23.3%** | **`+1.6%`** | 76.5 → **71.3 pkt** (`-5.2`) |
| `kb-02` **Pobór Podatków** | Korona & Borgiowie | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.6% → **21.8%** | **`-3.8%`** | 76.5 → **71.3 pkt** (`-5.2`) |
| `so-05` **Wezwanie do Trybunału** | Święte Oficjum | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 26.6% → **24.2%** | **`-2.4%`** | 76.5 → **72.0 pkt** (`-4.5`) |
| `caa-09` **Kurier Relikwii** | Cienie Al-Andalus | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 21.7% → **23.3%** | **`+1.6%`** | 76.5 → **72.1 pkt** (`-4.4`) |
| `gc-06` **Szantaż** | Gildia Cieni | 2zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 26.4% → **24.0%** | **`-2.4%`** | 76.5 → **72.4 pkt** (`-4.1`) |
| `so-02` **Skarbiec Trybunału** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 26.6% → **24.4%** | **`-2.2%`** | 76.5 → **72.6 pkt** (`-3.9`) |
| `caa-06` **Ucieczka z Lochów** | Cienie Al-Andalus | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 21.7% → **19.6%** | **`-2.1%`** | 76.5 → **73.5 pkt** (`-3.0`) |
| `gc-09` **Lista Dłużników** | Gildia Cieni | 3zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 26.4% → **24.5%** | **`-1.9%`** | 76.5 → **73.5 pkt** (`-3.0`) |
| `so-04` **Publiczne Ostrzeżenie** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 26.6% → **26.2%** | **`-0.4%`** | 76.5 → **73.8 pkt** (`-2.7`) |
| `gc-05` **Fałszywy Świadek** | Gildia Cieni | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 26.4% → **25.7%** | **`-0.7%`** | 76.5 → **73.9 pkt** (`-2.6`) |
| `gc-03` **Podrzucenie Księgi** | Gildia Cieni | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 26.4% → **26.7%** | **`+0.3%`** | 76.5 → **74.2 pkt** (`-2.3`) |
| `gc-01` **Przekupiony Strażnik** | Gildia Cieni | 2zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 26.4% → **26.9%** | **`+0.5%`** | 76.5 → **74.2 pkt** (`-2.3`) |
| `so-08` **Nasłanie Inkwizytora** | Święte Oficjum | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 26.6% → **26.0%** | **`-0.6%`** | 76.5 → **74.4 pkt** (`-2.1`) |
| `so-11` **Dekret Czystości Wiary** | Święte Oficjum | 1zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 26.6% → **27.0%** | **`+0.4%`** | 76.5 → **74.4 pkt** (`-2.1`) |

### 2.1b. 🩸 Autopodatek Frakcji (Self-Harm)
Karty, których wyłączenie **podnosi** win share własnej frakcji. Gracz zauważy je jako haracz, nawet gdy stół 4P jest równy dzięki temu haraczowi.

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `caa-04` **Fałszywy Trop** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 21.7% → **37.1%** | **`+15.4%`** | 76.5 → **59.2 pkt** (`-17.3`) |
| `caa-11` **Nocna Zmiana Warty** | Cienie Al-Andalus | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 21.7% → **36.5%** | **`+14.8%`** | 76.5 → **60.3 pkt** (`-16.2`) |
| `caa-08` **Kaptur Nocy** | Cienie Al-Andalus | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 21.7% → **36.4%** | **`+14.7%`** | 76.5 → **60.8 pkt** (`-15.7`) |
| `caa-01` **Przejście Podziemiami** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 21.7% → **36.2%** | **`+14.5%`** | 76.5 → **61.3 pkt** (`-15.2`) |
| `caa-07` **Szantaż Bractwa** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 21.7% → **36.0%** | **`+14.3%`** | 76.5 → **61.5 pkt** (`-15.0`) |
| `kb-04` **Faworyt Dworu** | Korona & Borgiowie | 2zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.6% → **37.5%** | **`+11.9%`** | 76.5 → **58.1 pkt** (`-18.4`) |
| `kt-01` **Rytuał Przejścia** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.7% → **30.1%** | **`+5.4%`** | 76.5 → **69.4 pkt** (`-7.1`) |
| `kt-02` **Transmutacja Złota** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.7% → **30.1%** | **`+5.4%`** | 76.5 → **69.4 pkt** (`-7.1`) |
| `kt-09` **Fragment Kodeksu** | Kabała z Toledo | 2zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.7% → **29.8%** | **`+5.1%`** | 76.5 → **69.6 pkt** (`-6.9`) |
| `kt-07` **Archiwum Ukryte** | Kabała z Toledo | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.7% → **29.7%** | **`+5.0%`** | 76.5 → **69.7 pkt** (`-6.8`) |
| `kt-08` **Areszt Wiedzy** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.7% → **29.7%** | **`+5.0%`** | 76.5 → **69.7 pkt** (`-6.8`) |
| `kb-05` **List Żelazny** | Korona & Borgiowie | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.6% → **30.4%** | **`+4.8%`** | 76.5 → **68.3 pkt** (`-8.2`) |
| `kb-07` **Szantaż Pieczęcią** | Korona & Borgiowie | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.6% → **30.4%** | **`+4.8%`** | 76.5 → **68.9 pkt** (`-7.6`) |
| `kb-08` **Przekupstwo Sędziego** | Korona & Borgiowie | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.6% → **30.4%** | **`+4.8%`** | 76.5 → **68.9 pkt** (`-7.6`) |
| `kt-04` **Zwierciadło Herezji** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.7% → **29.4%** | **`+4.7%`** | 76.5 → **70.5 pkt** (`-6.0`) |
| `kt-12` **Strażnik Archiwum** | Kabała z Toledo | 0zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.7% → **29.1%** | **`+4.4%`** | 76.5 → **71.7 pkt** (`-4.8`) |
| `kt-11` **Medytacja Sefirot** | Kabała z Toledo | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.7% → **29.0%** | **`+4.3%`** | 76.5 → **71.7 pkt** (`-4.8`) |
| `gc-02` **Czarny Rynek** | Gildia Cieni | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 26.4% → **30.2%** | **`+3.8%`** | 76.5 → **66.1 pkt** (`-10.4`) |
| `gc-04` **Informator** | Gildia Cieni | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 26.4% → **30.0%** | **`+3.6%`** | 76.5 → **65.3 pkt** (`-11.2`) |
| `kb-12` **Szantaż Salonowy** | Korona & Borgiowie | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.6% → **28.6%** | **`+3.0%`** | 76.5 → **74.0 pkt** (`-2.5`) |

### 2.2. ⚠️ Karty Destabilizujące Kanon 4P (Disruptors)
Karty, których wyłączenie podnosi 4P Score ($\Delta \text{4P} \ge +1.5$ pkt):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *Brak kart destabilizujących* | - | - | - | - | - | - |

### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich 60 Kart Frakcji w Kanonie 4P

| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Faction Win Share 4P | $\Delta$ Frakcji | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `caa-01` | **Przejście Podziemiami** | Cienie Al-Andalus | 0 | 0 | 21.7% → 36.2% | `+14.5%` | 61.3 | `-15.2` | 5.91 | 0.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-02` | **Złoto z Kryjówki** | Cienie Al-Andalus | 0 | 0 | 21.7% → 23.2% | `+1.5%` | 70.9 | `-5.6` | 6.20 | 0.3% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-03` | **Cień na Rynku** | Cienie Al-Andalus | 0 | 1 | 21.7% → 21.2% | `-0.5%` | 62.7 | `-13.8` | 6.52 | 0.4% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-04` | **Fałszywy Trop** | Cienie Al-Andalus | 0 | 0 | 21.7% → 37.1% | `+15.4%` | 59.2 | `-17.3` | 5.91 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-05` | **Ukryty Kurier** | Cienie Al-Andalus | 0 | 0 | 21.7% → 13.0% | `-8.7%` | 55.9 | `-20.6` | 6.42 | 0.3% | 👑 FILAR KANONU (Core Keystone) |
| `caa-12` | **Skrytka w Murach** | Cienie Al-Andalus | 0 | 0 | 21.7% → 23.3% | `+1.6%` | 71.3 | `-5.2` | 6.20 | 0.3% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-06` | **Ucieczka z Lochów** | Cienie Al-Andalus | 0 | 0 | 21.7% → 19.6% | `-2.1%` | 73.5 | `-3.0` | 6.06 | 0.4% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-07` | **Szantaż Bractwa** | Cienie Al-Andalus | 0 | 0 | 21.7% → 36.0% | `+14.3%` | 61.5 | `-15.0` | 5.92 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-08` | **Kaptur Nocy** | Cienie Al-Andalus | 1 | 0 | 21.7% → 36.4% | `+14.7%` | 60.8 | `-15.7` | 5.92 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-11` | **Nocna Zmiana Warty** | Cienie Al-Andalus | 1 | 0 | 21.7% → 36.5% | `+14.8%` | 60.3 | `-16.2` | 5.90 | 0.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-09` | **Kurier Relikwii** | Cienie Al-Andalus | 0 | 0 | 21.7% → 23.3% | `+1.6%` | 72.1 | `-4.4` | 6.20 | 0.3% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-10` | **Echo Alhambry** | Cienie Al-Andalus | 1 | 0 | 21.7% → 4.4% | `-17.3%` | 38.5 | `-38.0` | 6.66 | 0.4% | 👑 FILAR KANONU (Core Keystone) |
| `gc-05` | **Fałszywy Świadek** | Gildia Cieni | 0 | 0 | 26.4% → 25.7% | `-0.7%` | 73.9 | `-2.6` | 6.19 | 0.3% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-12` | **Złodziejski Zwiad** | Gildia Cieni | 0 | 2 | 26.4% → 26.4% | `+0.0%` | 75.0 | `-1.5` | 6.17 | 0.2% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-02` | **Czarny Rynek** | Gildia Cieni | 1 | 1 | 26.4% → 30.2% | `+3.8%` | 66.1 | `-10.4` | 6.26 | 0.3% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `gc-03` | **Podrzucenie Księgi** | Gildia Cieni | 1 | 0 | 26.4% → 26.7% | `+0.3%` | 74.2 | `-2.3` | 6.19 | 0.3% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-04` | **Informator** | Gildia Cieni | 1 | 1 | 26.4% → 30.0% | `+3.6%` | 65.3 | `-11.2` | 6.28 | 0.3% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `gc-01` | **Przekupiony Strażnik** | Gildia Cieni | 2 | 1 | 26.4% → 26.9% | `+0.5%` | 74.2 | `-2.3` | 6.18 | 0.3% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-07` | **Skrytobójstwo** | Gildia Cieni | 1 | 0 | 26.4% → 26.4% | `+0.0%` | 75.8 | `-0.7` | 6.18 | 0.2% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-08` | **Zatrute Złoto** | Gildia Cieni | 1 | 1 | 26.4% → 26.4% | `+0.0%` | 75.3 | `-1.2` | 6.19 | 0.2% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-11` | **Fałszywe Świadectwo Cechu** | Gildia Cieni | 1 | 0 | 26.4% → 26.6% | `+0.2%` | 74.8 | `-1.7` | 6.17 | 0.2% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-06` | **Szantaż** | Gildia Cieni | 2 | 1 | 26.4% → 24.0% | `-2.4%` | 72.4 | `-4.1` | 6.38 | 0.3% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-09` | **Lista Dłużników** | Gildia Cieni | 3 | 1 | 26.4% → 24.5% | `-1.9%` | 73.5 | `-3.0` | 6.38 | 0.3% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-10` | **Upadek Domu** | Gildia Cieni | 4 | 2 | 26.4% → 26.8% | `+0.4%` | 75.9 | `-0.6` | 6.17 | 0.2% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-01` | **Rozkaz Dworu** | Korona & Borgiowie | 1 | 1 | 25.6% → 25.5% | `-0.1%` | 76.5 | `0.0` | 6.19 | 0.2% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `kb-02` | **Pobór Podatków** | Korona & Borgiowie | 1 | 0 | 25.6% → 21.8% | `-3.8%` | 71.3 | `-5.2` | 6.28 | 0.3% | 👑 FILAR KANONU (Core Keystone) |
| `kb-03` | **Plotka Dworska** | Korona & Borgiowie | 1 | 1 | 25.6% → 25.3% | `-0.3%` | 76.7 | `+0.2` | 6.20 | 0.2% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `kb-11` | **Tajny Emisariusz** | Korona & Borgiowie | 1 | 0 | 25.6% → 26.2% | `+0.6%` | 77.3 | `+0.8` | 6.17 | 0.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-04` | **Faworyt Dworu** | Korona & Borgiowie | 2 | 1 | 25.6% → 37.5% | `+11.9%` | 58.1 | `-18.4` | 5.95 | 0.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-05` | **List Żelazny** | Korona & Borgiowie | 2 | 0 | 25.6% → 30.4% | `+4.8%` | 68.3 | `-8.2` | 6.07 | 0.3% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-12` | **Szantaż Salonowy** | Korona & Borgiowie | 1 | 0 | 25.6% → 28.6% | `+3.0%` | 74.0 | `-2.5` | 6.21 | 0.3% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-06` | **Areszt Królewski** | Korona & Borgiowie | 2 | 0 | 25.6% → 25.1% | `-0.5%` | 74.7 | `-1.8` | 6.20 | 0.2% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-07` | **Szantaż Pieczęcią** | Korona & Borgiowie | 2 | 0 | 25.6% → 30.4% | `+4.8%` | 68.9 | `-7.6` | 6.19 | 0.4% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-08` | **Przekupstwo Sędziego** | Korona & Borgiowie | 2 | 0 | 25.6% → 30.4% | `+4.8%` | 68.9 | `-7.6` | 6.19 | 0.4% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-10` | **Pieczęć Korony** | Korona & Borgiowie | 3 | 2 | 25.6% → 0.2% | `-25.4%` | 29.8 | `-46.7` | 6.64 | 0.4% | 👑 FILAR KANONU (Core Keystone) |
| `kb-09` | **Dekret Królewski** | Korona & Borgiowie | 4 | 1 | 25.6% → 0.1% | `-25.5%` | 29.5 | `-47.0` | 6.60 | 0.5% | 👑 FILAR KANONU (Core Keystone) |
| `kt-03` | **Zakazana Wiedza** | Kabała z Toledo | 0 | 0 | 24.7% → 4.3% | `-20.4%` | 27.6 | `-48.9` | 6.57 | 0.4% | 👑 FILAR KANONU (Core Keystone) |
| `kt-12` | **Strażnik Archiwum** | Kabała z Toledo | 0 | 1 | 24.7% → 29.1% | `+4.4%` | 71.7 | `-4.8` | 6.11 | 0.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-01` | **Rytuał Przejścia** | Kabała z Toledo | 1 | 0 | 24.7% → 30.1% | `+5.4%` | 69.4 | `-7.1` | 6.10 | 0.3% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-02` | **Transmutacja Złota** | Kabała z Toledo | 1 | 0 | 24.7% → 30.1% | `+5.4%` | 69.4 | `-7.1` | 6.10 | 0.3% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-04` | **Zwierciadło Herezji** | Kabała z Toledo | 1 | 0 | 24.7% → 29.4% | `+4.7%` | 70.5 | `-6.0` | 6.10 | 0.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-05` | **Wskazówka Cyklu** | Kabała z Toledo | 1 | 1 | 24.7% → 14.3% | `-10.4%` | 49.8 | `-26.7` | 6.39 | 0.4% | 👑 FILAR KANONU (Core Keystone) |
| `kt-07` | **Archiwum Ukryte** | Kabała z Toledo | 1 | 1 | 24.7% → 29.7% | `+5.0%` | 69.7 | `-6.8` | 6.11 | 0.3% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-08` | **Areszt Wiedzy** | Kabała z Toledo | 1 | 0 | 24.7% → 29.7% | `+5.0%` | 69.7 | `-6.8` | 6.11 | 0.3% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-06` | **Przesłuchanie Imienia** | Kabała z Toledo | 2 | 0 | 24.7% → 25.3% | `+0.6%` | 75.1 | `-1.4` | 6.20 | 0.4% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-11` | **Medytacja Sefirot** | Kabała z Toledo | 2 | 0 | 24.7% → 29.0% | `+4.3%` | 71.7 | `-4.8` | 6.12 | 0.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-09` | **Fragment Kodeksu** | Kabała z Toledo | 2 | 1 | 24.7% → 29.8% | `+5.1%` | 69.6 | `-6.9` | 6.12 | 0.3% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-10` | **Pieczęć Salomona** | Kabała z Toledo | 2 | 2 | 24.7% → 19.0% | `-5.7%` | 64.2 | `-12.3` | 6.36 | 0.5% | 👑 FILAR KANONU (Core Keystone) |
| `so-05` | **Wezwanie do Trybunału** | Święte Oficjum | 0 | 0 | 26.6% → 24.2% | `-2.4%` | 72.0 | `-4.5` | 6.21 | 0.3% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-01` | **Patrol Familiariuszy** | Święte Oficjum | 1 | 0 | 26.6% → 27.2% | `+0.6%` | 75.7 | `-0.8` | 6.22 | 0.3% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-02` | **Skarbiec Trybunału** | Święte Oficjum | 1 | 0 | 26.6% → 24.4% | `-2.2%` | 72.6 | `-3.9` | 6.31 | 0.4% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-04` | **Publiczne Ostrzeżenie** | Święte Oficjum | 1 | 0 | 26.6% → 26.2% | `-0.4%` | 73.8 | `-2.7` | 6.20 | 0.3% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-12` | **Straż Trybunalska** | Święte Oficjum | 1 | 0 | 26.6% → 27.2% | `+0.6%` | 75.0 | `-1.5` | 6.21 | 0.3% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-03` | **Podejrzenie** | Święte Oficjum | 2 | 0 | 26.6% → 26.9% | `+0.3%` | 75.0 | `-1.5` | 6.20 | 0.3% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-08` | **Nasłanie Inkwizytora** | Święte Oficjum | 0 | 0 | 26.6% → 26.0% | `-0.6%` | 74.4 | `-2.1` | 6.20 | 0.3% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-11` | **Dekret Czystości Wiary** | Święte Oficjum | 1 | 1 | 26.6% → 27.0% | `+0.4%` | 74.4 | `-2.1` | 6.21 | 0.3% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-06` | **Areszt Trybunalski** | Święte Oficjum | 2 | 0 | 26.6% → 27.1% | `+0.5%` | 74.7 | `-1.8` | 6.21 | 0.3% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-07` | **Przesłuchanie Oficjum** | Święte Oficjum | 2 | 0 | 26.6% → 27.1% | `+0.5%` | 74.7 | `-1.8` | 6.21 | 0.3% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-09` | **Świadek Koronny** | Święte Oficjum | 2 | 0 | 26.6% → 27.2% | `+0.6%` | 75.5 | `-1.0` | 6.21 | 0.3% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-10` | **Oczyść Miasto** | Święte Oficjum | 5 | 2 | 26.6% → 27.2% | `+0.6%` | 75.3 | `-1.2` | 6.24 | 0.3% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |

---

## 3. ⏳ Warstwa II — Kronika Dziejów w 4P (Ablacja 8 Kart Wydarzeń Czasu)

Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans w 4P:

| ID | Karta Wydarzenia | 4P Score | $\Delta$ 4P | Średnia Er | Deadlock % | Status Roli w Kronice |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `time-01` | **Kapitulacja Grenady** | 76.5 → 🟠 ** 72.3** (`-4.2`) | `-4.2 pkt` | 6.24 Er | 0.3% | 🟢 Stabilizator tempa |
| `time-02` | **Godzina Policyjna** | 76.5 → 🟡 ** 75.6** (`-0.9`) | `-0.9 pkt` | 6.20 Er | 0.3% | ⚖️ Neutralna Kronika |
| `time-03` | **Flota Odkrywców** | 76.5 → 🟠 ** 74.7** (`-1.8`) | `-1.8 pkt` | 6.22 Er | 0.3% | 🟢 Stabilizator tempa |
| `time-04` | **Rewizja w Dzielnicach** | 76.5 → 🟡 ** 75.0** (`-1.5`) | `-1.5 pkt` | 6.25 Er | 0.4% | 🟢 Stabilizator tempa |
| `time-05` | **Gorączka Donosów** | 76.5 → 🟡 ** 75.2** (`-1.3`) | `-1.3 pkt` | 6.24 Er | 0.4% | 🟢 Stabilizator tempa |
| `time-06` | **Nocna Obława** | 76.5 → 🟠 ** 74.6** (`-1.9`) | `-1.9 pkt` | 6.23 Er | 0.3% | 🟢 Stabilizator tempa |
| `time-07` | **Bunt w Lochach** | 76.5 → 🟠 ** 74.6** (`-1.9`) | `-1.9 pkt` | 6.18 Er | 0.3% | 🟢 Stabilizator tempa |
| `time-08` | **Święte Przymierze** | 76.5 → 🟡 ** 76.1** (`-0.4`) | `-0.4 pkt` | 6.11 Er | 0.1% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-09` | **Jarmark Królewski** | 76.5 → 🟡 ** 76.1** (`-0.4`) | `-0.4 pkt` | 6.21 Er | 0.3% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-10` | **Amnestia Biskupia** | 76.5 → 🟡 ** 75.5** (`-1.0`) | `-1.0 pkt` | 6.20 Er | 0.3% | 🟢 Stabilizator tempa |

---

## 4. ⚙️ Warstwa III — Matryca 9 Obszarów Wpływu Mechanik Gry (L1, L2, L4)

Mechaniki w tym raporcie: **skraj albo wyłączenie**. Testy ±1 są w `audit_level1` / `audit_level2` / `audit_level4`. **Δ≈0 nie jest harmonią.**

| Kategoria Mechaniki | Liczba Testów | Rola w Ekosystemie Kanonu 4P | Rekomendacja Balansowa |
| :--- | :---: | :--- | :--- |
| 👑 / 🛡️ **Filary i Bezpieczniki** | **25** | Ablacja wali w stół — gracze czują tę gałkę | **Cel kanonu** |
| ⚠️ **Za słabe dźwignie** | **1** | Rusza share, nie trzyma stołu — nie jest „zbalansowana” | **Wzmocnić aż będzie filarem** |
| 💤 **Martwe / uśpione ścieżki** | **0** | Dual-win z witalności albo ablacja Δ≈0 | Wada pomiaru, nie harmonia |
| ⚠️ / 💡 **Wady bieżącej wartości** | **0** | Inna wartość gałki **podnosi** 4P — obecny setting szkodzi | **Przekręcić albo rework** |

### 4.0. ⚠️ Problematyczne mechaniki (osobny wykaz)
Wszystkie mechaniki z grup **DEAD**, **WEAK/NEUTRAL** i **DISRUPTOR**: ścieżki dual-win z `evaluate_vitality`, testy z $|\Delta\text{4P}| \le 0.8$ i ruchem share $\le 1.5$ pp (DEAD), za słabe dźwignie (WEAK) oraz wady bieżącej wartości (DISRUPTOR).

| Badany Podsystem | Kategoria | 4P Score | $\Delta$ 4P | Klasyfikacja |
| :--- | :--- | :---: | :---: | :--- |
| **Werdykt Sądu: tajny (wyłączenie jawnej koordynacji)** | Poziom 4: Warianty i Modyfikatory | 76.5 → 🟠 ** 73.3** (`-3.2`) | `-3.2 pkt` | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |

### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)

| Badany Podsystem / Modyfikator L1 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Limit Er: 14 → 7 (skrajna presja)** | 76.5 → 🟠 ** 69.6** (`-6.9`) | `-6.9 pkt` | 5.75 Er | 29.4% | 1.7% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Próg Oskarżenia: 7 → 1** | 76.5 → 🔴 **  0.8** (`-75.7`) | `-75.7 pkt` | 5.38 Er | 0.0% | 0.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Oskarżenia: 7 → 14** | 76.5 → 🔴 ** 30.2** (`-46.3`) | `-46.3 pkt` | 6.21 Er | 0.9% | 1.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 0zł (wyłączenie)** | 76.5 → 🔴 ** 35.9** (`-40.6`) | `-40.6 pkt` | 6.62 Er | 0.3% | 6.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 8zł** | 76.5 → 🔴 ** 56.1** (`-20.4`) | `-20.4 pkt` | 5.93 Er | 0.2% | 0.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 1** | 76.5 → 🔴 ** 19.0** (`-57.5`) | `-57.5 pkt` | 8.90 Er | 18.5% | 1.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 6** | 76.5 → 🔴 ** 11.4** (`-65.1`) | `-65.1 pkt` | 4.50 Er | 0.0% | 1.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 1** | 76.5 → 🔴 **  1.6** (`-74.9`) | `-74.9 pkt` | 8.83 Er | 1.9% | 10.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 10** | 76.5 → 🔴 **  8.1** (`-68.4`) | `-68.4 pkt` | 4.59 Er | 0.0% | 2.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: cooldown 3 → 0 (co erę)** | 76.5 → 🔴 ** 12.0** (`-64.5`) | `-64.5 pkt` | 5.05 Er | 0.2% | 2.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: całkowite wyłączenie** | 76.5 → 🔴 ** 30.9** (`-45.6`) | `-45.6 pkt` | 9.62 Er | 44.0% | 0.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)

| Badany Warunek Zwycięstwa L2 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: stosy 6 → 1** | 76.5 → 🔴 ** 15.2** (`-61.3`) | `-61.3 pkt` | 3.83 Er | 0.0% | 2.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: stosy 6 → 12** | 76.5 → 🔴 ** 50.3** (`-26.2`) | `-26.2 pkt` | 6.52 Er | 2.9% | 1.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 1** | 76.5 → 🔴 ** 15.4** (`-61.1`) | `-61.1 pkt` | 4.29 Er | 0.0% | 1.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 6** | 76.5 → 🟠 ** 70.3** (`-6.2`) | `-6.2 pkt` | 6.24 Er | 0.3% | 1.6% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Cienie: relikwie 2 → 4** | 76.5 → 🔴 ** 32.1** (`-44.4`) | `-44.4 pkt` | 6.67 Er | 0.4% | 1.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: dekrety 2 → 4** | 76.5 → 🔴 ** 29.6** (`-46.9`) | `-46.9 pkt` | 6.53 Er | 0.4% | 1.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: fragmenty 2 → 4** | 76.5 → 🔴 ** 26.0** (`-50.5`) | `-50.5 pkt` | 6.43 Er | 0.3% | 1.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: era 6 → 1** | 76.5 → 🔴 ** 34.1** (`-42.4`) | `-42.4 pkt` | 4.89 Er | 0.3% | 1.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: era 6 → 12** | 76.5 → 🔴 ** 25.1** (`-51.4`) | `-51.4 pkt` | 6.43 Er | 0.3% | 1.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 8 → 1** | 76.5 → 🔴 ** 13.8** (`-62.7`) | `-62.7 pkt` | 3.35 Er | 0.2% | 2.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 8 → 16** | 76.5 → 🔴 ** 36.0** (`-40.5`) | `-40.5 pkt` | 6.65 Er | 1.2% | 1.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)

| Badany Wariant / Modyfikator L4 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kronika Dziejów: całkowite wyłączenie** | 76.5 → 🟠 ** 61.6** (`-14.9`) | `-14.9 pkt` | 6.29 Er | 0.3% | 2.0% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Werdykt Sądu: tajny (wyłączenie jawnej koordynacji)** | 76.5 → 🟠 ** 73.3** (`-3.2`) | `-3.2 pkt` | 6.13 Er | 0.2% | 1.6% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |
| **Inkwizytor Patrol: ruch 1 → 0 (wyłączenie)** | 76.5 → 🔴 ** 24.2** (`-52.3`) | `-52.3 pkt` | 9.73 Er | 44.5% | 0.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Szlak Morski: era 4 → nigdy (99)** | 76.5 → 🟠 ** 71.1** (`-5.4`) | `-5.4 pkt` | 6.26 Er | 0.3% | 1.6% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |

---

## 5. 👥 Warstwa IV — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych. Kolumna win share to HUD kanonu; setup+witalność to stary blend (kara martwej ścieżki).

| Nieobecna Frakcja | Setup Testowy | Win share | Setup+witalność | Diagnoza |
| :--- | :--- | :---: | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`67.9`** | `67.9` | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`61.1`** | `61.1` | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`91.7`** | `91.7` | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`87.0`** | `87.0` | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`74.6`** | `74.6` | Brak presji stosów i bezpośredniego Inkwizytora |