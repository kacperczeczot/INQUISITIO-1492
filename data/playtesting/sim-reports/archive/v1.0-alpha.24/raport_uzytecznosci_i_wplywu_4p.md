# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v1.0-alpha.24

**Wersja Gry:** `v1.0-alpha.24` | **Data Badania:** 2026-08-22 20:08 | **Próba:** 5000 gier/setup (25000 gier na wariant) | **Ziarno:** 42
**4P Score (win share):** 🟡 ** 84.0** pkt | **Witalność (osobna kara):** `0.000` | **Śr. Er:** `5.98` | **Deadlocki:** `0.1%` | **Pas Biedy:** `1.0%`
**Udziały 4P:** CAA 23.7% · GC 24.1% · KB 27.4% · KT 26.3% · SO 23.5%

Klasyfikacja L1/L2/L4 i Δ 4P liczą wyłącznie równość win share (`calculate_balance_score`). Kara witalności jest osobno.

---

## 0. Wady z tej próby (nie HUD win share)

Kubełki klasyfikatora i ostrzeżenia witalności z bieżącego runu.

- **Autopodatek (SELF_HARM):** 19/60
- **DEAD_WEIGHT:** `gc-05` Fałszywy Świadek, `gc-12` Złodziejski Zwiad, `gc-11` Fałszywe Świadectwo Cechu, `gc-08` Zatrute Złoto, `gc-10` Upadek Domu
- **Karty Kroniki |Δ4P| ≤ 0.8:** 1/10
- **Ablacja całej Kroniki (`L4_NO_TIME_DECK`):** Δ4P -5.3 (STABILIZER)
- **Mechaniki WEAK/NEUTRAL:** Szlak Morski: era 4 → nigdy (99)

---

## 1. 🗺️ Podsumowanie Ekosystemu Kart Kanonu 4P (Matryca Wpływu Kart, 60 kart)

Rozkład wszystkich 60 kart frakcyjnych w matrycy **Wpływ na Frakcję ($\Delta \text{Share}$)** vs **Wpływ na Kanon 4P ($\Delta \text{4P Score}$)**:

| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |
| :--- | :---: | :---: | :--- | :--- |
| 🩸 **Autopodatek (Self-Harm)** | **19** | 31.7% | Wyłączenie **podnosi** win share własnej frakcji — karta jest haraczem, nie silnikiem | **Rework / osłabienie kosztu, nie filar** |
| 💤 **Karta Pasywna (Dead Weight)** | **5** | 8.3% | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia lub wycięcia** |
| ⚠️ **Karta Destabilizująca (Disruptor)** | **0** | 0.0% | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |
| ⚖️ **Zbalansowane Narzędzie** | **13** | 21.7% | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Narzędzie, nie złoty środek całego kanonu** |
| 👑 / ⚓ **Filar / Kotwica Kanonu** | **23** | 38.3% | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |

---

## 2. 🃏 Warstwa I — Szczegółowa Analiza 60 Kart Frakcji w Kanonie 4P

### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)
Karty, których brak powoduje spadek wyniku Kanonu 4P o $\ge 4.0$ pkt lub załamanie winrate frakcji o $\ge 4.0\%$ — **bez** autopodatków (te są w 2.1b):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kb-09` **Dekret Królewski** | Korona & Borgiowie | 4zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 27.4% → **0.1%** | **`-27.3%`** | 84.0 → **30.6 pkt** (`-53.4`) |
| `kb-10` **Pieczęć Korony** | Korona & Borgiowie | 3zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 27.4% → **1.6%** | **`-25.8%`** | 84.0 → **32.9 pkt** (`-51.1`) |
| `caa-10` **Echo Alhambry** | Cienie Al-Andalus | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 23.7% → **2.6%** | **`-21.1%`** | 84.0 → **33.6 pkt** (`-50.4`) |
| `caa-05` **Ukryty Kurier** | Cienie Al-Andalus | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 23.7% → **11.5%** | **`-12.2%`** | 84.0 → **50.8 pkt** (`-33.2`) |
| `kt-03` **Zakazana Wiedza** | Kabała z Toledo | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 26.3% → **13.5%** | **`-12.8%`** | 84.0 → **57.7 pkt** (`-26.3`) |
| `kt-05` **Wskazówka Cyklu** | Kabała z Toledo | 1zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 26.3% → **16.6%** | **`-9.7%`** | 84.0 → **66.2 pkt** (`-17.8`) |
| `kb-11` **Tajny Emisariusz** | Korona & Borgiowie | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 27.4% → **27.8%** | **`+0.4%`** | 84.0 → **74.3 pkt** (`-9.7`) |
| `kb-03` **Plotka Dworska** | Korona & Borgiowie | 1zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 27.4% → **27.1%** | **`-0.3%`** | 84.0 → **74.8 pkt** (`-9.2`) |
| `kb-01` **Rozkaz Dworu** | Korona & Borgiowie | 1zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 27.4% → **27.3%** | **`-0.1%`** | 84.0 → **75.3 pkt** (`-8.7`) |
| `kb-02` **Pobór Podatków** | Korona & Borgiowie | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 27.4% → **28.0%** | **`+0.6%`** | 84.0 → **75.4 pkt** (`-8.6`) |
| `caa-03` **Cień na Rynku** | Cienie Al-Andalus | 0zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.7% → **25.2%** | **`+1.5%`** | 84.0 → **76.4 pkt** (`-7.6`) |
| `so-02` **Skarbiec Trybunału** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.5% → **22.0%** | **`-1.5%`** | 84.0 → **77.2 pkt** (`-6.8`) |
| `gc-06` **Szantaż** | Gildia Cieni | 2zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 24.1% → **20.7%** | **`-3.4%`** | 84.0 → **77.8 pkt** (`-6.2`) |
| `caa-06` **Ucieczka z Lochów** | Cienie Al-Andalus | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.7% → **21.5%** | **`-2.2%`** | 84.0 → **78.4 pkt** (`-5.6`) |
| `gc-09` **Lista Dłużników** | Gildia Cieni | 3zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 24.1% → **21.2%** | **`-2.9%`** | 84.0 → **80.1 pkt** (`-3.9`) |
| `kb-12` **Szantaż Salonowy** | Korona & Borgiowie | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 27.4% → **28.6%** | **`+1.2%`** | 84.0 → **80.2 pkt** (`-3.8`) |
| `kb-07` **Szantaż Pieczęcią** | Korona & Borgiowie | 2zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 27.4% → **29.2%** | **`+1.8%`** | 84.0 → **80.3 pkt** (`-3.7`) |
| `kb-08` **Przekupstwo Sędziego** | Korona & Borgiowie | 2zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 27.4% → **29.2%** | **`+1.8%`** | 84.0 → **80.3 pkt** (`-3.7`) |
| `so-05` **Wezwanie do Trybunału** | Święte Oficjum | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.5% → **21.9%** | **`-1.6%`** | 84.0 → **80.6 pkt** (`-3.4`) |
| `so-06` **Areszt Trybunalski** | Święte Oficjum | 2zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.5% → **24.2%** | **`+0.7%`** | 84.0 → **81.0 pkt** (`-3.0`) |
| `gc-04` **Informator** | Gildia Cieni | 1zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.1% → **25.6%** | **`+1.5%`** | 84.0 → **81.2 pkt** (`-2.8`) |
| `so-03` **Podejrzenie** | Święte Oficjum | 2zł / 2☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.5% → **24.3%** | **`+0.8%`** | 84.0 → **82.0 pkt** (`-2.0`) |
| `kt-09` **Fragment Kodeksu** | Kabała z Toledo | 2zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 26.3% → **23.4%** | **`-2.9%`** | 84.0 → **85.0 pkt** (`1.0`) |

### 2.1b. 🩸 Autopodatek Frakcji (Self-Harm)
Karty, których wyłączenie **podnosi** win share własnej frakcji. Gracz zauważy je jako haracz, nawet gdy stół 4P jest równy dzięki temu haraczowi.

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `caa-11` **Nocna Zmiana Warty** | Cienie Al-Andalus | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 23.7% → **44.2%** | **`+20.5%`** | 84.0 → **40.6 pkt** (`-43.4`) |
| `caa-04` **Fałszywy Trop** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 23.7% → **43.6%** | **`+19.9%`** | 84.0 → **41.8 pkt** (`-42.2`) |
| `caa-01` **Przejście Podziemiami** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 23.7% → **43.4%** | **`+19.7%`** | 84.0 → **41.9 pkt** (`-42.1`) |
| `caa-08` **Kaptur Nocy** | Cienie Al-Andalus | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 23.7% → **43.1%** | **`+19.4%`** | 84.0 → **42.7 pkt** (`-41.3`) |
| `kb-04` **Faworyt Dworu** | Korona & Borgiowie | 2zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 27.4% → **42.0%** | **`+14.6%`** | 84.0 → **46.8 pkt** (`-37.2`) |
| `kt-10` **Pieczęć Salomona** | Kabała z Toledo | 2zł / 2☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 26.3% → **39.4%** | **`+13.1%`** | 84.0 → **49.7 pkt** (`-34.3`) |
| `caa-07` **Szantaż Bractwa** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 23.7% → **34.1%** | **`+10.4%`** | 84.0 → **63.2 pkt** (`-20.8`) |
| `kb-06` **Areszt Królewski** | Korona & Borgiowie | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 27.4% → **33.4%** | **`+6.0%`** | 84.0 → **66.0 pkt** (`-18.0`) |
| `kb-05` **List Żelazny** | Korona & Borgiowie | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 27.4% → **31.9%** | **`+4.5%`** | 84.0 → **72.9 pkt** (`-11.1`) |
| `caa-12` **Skrytka w Murach** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 23.7% → **26.7%** | **`+3.0%`** | 84.0 → **81.9 pkt** (`-2.1`) |
| `gc-02` **Czarny Rynek** | Gildia Cieni | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.1% → **26.9%** | **`+2.8%`** | 84.0 → **80.4 pkt** (`-3.6`) |
| `kt-11` **Medytacja Sefirot** | Kabała z Toledo | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 26.3% → **29.1%** | **`+2.8%`** | 84.0 → **77.1 pkt** (`-6.9`) |
| `kt-12` **Strażnik Archiwum** | Kabała z Toledo | 0zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 26.3% → **29.0%** | **`+2.7%`** | 84.0 → **77.1 pkt** (`-6.9`) |
| `kt-07` **Archiwum Ukryte** | Kabała z Toledo | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 26.3% → **28.9%** | **`+2.6%`** | 84.0 → **77.8 pkt** (`-6.2`) |
| `caa-09` **Kurier Relikwii** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 23.7% → **26.1%** | **`+2.4%`** | 84.0 → **84.1 pkt** (`0.1`) |
| `kt-01` **Rytuał Przejścia** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 26.3% → **28.6%** | **`+2.3%`** | 84.0 → **78.6 pkt** (`-5.4`) |
| `kt-02` **Transmutacja Złota** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 26.3% → **28.6%** | **`+2.3%`** | 84.0 → **78.6 pkt** (`-5.4`) |
| `caa-02` **Złoto z Kryjówki** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 23.7% → **25.7%** | **`+2.0%`** | 84.0 → **82.8 pkt** (`-1.2`) |
| `kt-04` **Zwierciadło Herezji** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 26.3% → **28.3%** | **`+2.0%`** | 84.0 → **79.5 pkt** (`-4.5`) |

### 2.2. ⚠️ Karty Destabilizujące Kanon 4P (Disruptors)
Karty, których wyłączenie podnosi 4P Score ($\Delta \text{4P} \ge +1.5$ pkt):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *Brak kart destabilizujących* | - | - | - | - | - | - |

### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich 60 Kart Frakcji w Kanonie 4P

| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Faction Win Share 4P | $\Delta$ Frakcji | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `caa-01` | **Przejście Podziemiami** | Cienie Al-Andalus | 0 | 0 | 23.7% → 43.4% | `+19.7%` | 41.9 | `-42.1` | 5.63 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-02` | **Złoto z Kryjówki** | Cienie Al-Andalus | 0 | 0 | 23.7% → 25.7% | `+2.0%` | 82.8 | `-1.2` | 5.91 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-03` | **Cień na Rynku** | Cienie Al-Andalus | 0 | 1 | 23.7% → 25.2% | `+1.5%` | 76.4 | `-7.6` | 6.23 | 0.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-04` | **Fałszywy Trop** | Cienie Al-Andalus | 0 | 0 | 23.7% → 43.6% | `+19.9%` | 41.8 | `-42.2` | 5.65 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-05` | **Ukryty Kurier** | Cienie Al-Andalus | 0 | 0 | 23.7% → 11.5% | `-12.2%` | 50.8 | `-33.2` | 6.21 | 0.2% | 👑 FILAR KANONU (Core Keystone) |
| `caa-12` | **Skrytka w Murach** | Cienie Al-Andalus | 0 | 0 | 23.7% → 26.7% | `+3.0%` | 81.9 | `-2.1` | 5.90 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-06` | **Ucieczka z Lochów** | Cienie Al-Andalus | 0 | 0 | 23.7% → 21.5% | `-2.2%` | 78.4 | `-5.6` | 5.85 | 0.2% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-07` | **Szantaż Bractwa** | Cienie Al-Andalus | 0 | 0 | 23.7% → 34.1% | `+10.4%` | 63.2 | `-20.8` | 5.73 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-08` | **Kaptur Nocy** | Cienie Al-Andalus | 1 | 0 | 23.7% → 43.1% | `+19.4%` | 42.7 | `-41.3` | 5.65 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-11` | **Nocna Zmiana Warty** | Cienie Al-Andalus | 1 | 0 | 23.7% → 44.2% | `+20.5%` | 40.6 | `-43.4` | 5.62 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-09` | **Kurier Relikwii** | Cienie Al-Andalus | 0 | 0 | 23.7% → 26.1% | `+2.4%` | 84.1 | `+0.1` | 5.93 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-10` | **Echo Alhambry** | Cienie Al-Andalus | 1 | 0 | 23.7% → 2.6% | `-21.1%` | 33.6 | `-50.4` | 6.46 | 0.2% | 👑 FILAR KANONU (Core Keystone) |
| `gc-05` | **Fałszywy Świadek** | Gildia Cieni | 0 | 0 | 24.1% → 23.7% | `-0.4%` | 84.3 | `+0.3` | 5.93 | 0.1% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `gc-12` | **Złodziejski Zwiad** | Gildia Cieni | 0 | 2 | 24.1% → 24.3% | `+0.2%` | 83.7 | `-0.3` | 5.93 | 0.1% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `gc-02` | **Czarny Rynek** | Gildia Cieni | 1 | 1 | 24.1% → 26.9% | `+2.8%` | 80.4 | `-3.6` | 5.99 | 0.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `gc-03` | **Podrzucenie Księgi** | Gildia Cieni | 1 | 0 | 24.1% → 24.0% | `-0.1%` | 84.7 | `+0.7` | 5.93 | 0.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-04` | **Informator** | Gildia Cieni | 1 | 1 | 24.1% → 25.6% | `+1.5%` | 81.2 | `-2.8` | 5.99 | 0.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-01` | **Przekupiony Strażnik** | Gildia Cieni | 2 | 1 | 24.1% → 24.0% | `-0.1%` | 83.3 | `-0.7` | 5.93 | 0.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-07` | **Skrytobójstwo** | Gildia Cieni | 0 | 0 | 24.1% → 24.3% | `+0.2%` | 82.3 | `-1.7` | 5.95 | 0.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-11` | **Fałszywe Świadectwo Cechu** | Gildia Cieni | 0 | 2 | 24.1% → 24.3% | `+0.2%` | 83.7 | `-0.3` | 5.93 | 0.1% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `gc-08` | **Zatrute Złoto** | Gildia Cieni | 1 | 1 | 24.1% → 24.1% | `+0.0%` | 84.1 | `+0.1` | 5.93 | 0.1% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `gc-06` | **Szantaż** | Gildia Cieni | 2 | 1 | 24.1% → 20.7% | `-3.4%` | 77.8 | `-6.2` | 6.07 | 0.2% | 👑 FILAR KANONU (Core Keystone) |
| `gc-09` | **Lista Dłużników** | Gildia Cieni | 3 | 1 | 24.1% → 21.2% | `-2.9%` | 80.1 | `-3.9` | 6.07 | 0.2% | 👑 FILAR KANONU (Core Keystone) |
| `gc-10` | **Upadek Domu** | Gildia Cieni | 4 | 2 | 24.1% → 24.2% | `+0.1%` | 84.4 | `+0.4` | 5.99 | 0.1% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `kb-01` | **Rozkaz Dworu** | Korona & Borgiowie | 1 | 1 | 27.4% → 27.3% | `-0.1%` | 75.3 | `-8.7` | 5.95 | 0.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kb-02` | **Pobór Podatków** | Korona & Borgiowie | 1 | 0 | 27.4% → 28.0% | `+0.6%` | 75.4 | `-8.6` | 5.95 | 0.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kb-03` | **Plotka Dworska** | Korona & Borgiowie | 1 | 1 | 27.4% → 27.1% | `-0.3%` | 74.8 | `-9.2` | 5.96 | 0.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kb-11` | **Tajny Emisariusz** | Korona & Borgiowie | 1 | 0 | 27.4% → 27.8% | `+0.4%` | 74.3 | `-9.7` | 5.94 | 0.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kb-04` | **Faworyt Dworu** | Korona & Borgiowie | 2 | 1 | 27.4% → 42.0% | `+14.6%` | 46.8 | `-37.2` | 5.75 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-05` | **List Żelazny** | Korona & Borgiowie | 2 | 0 | 27.4% → 31.9% | `+4.5%` | 72.9 | `-11.1` | 5.84 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-12` | **Szantaż Salonowy** | Korona & Borgiowie | 1 | 0 | 27.4% → 28.6% | `+1.2%` | 80.2 | `-3.8` | 5.99 | 0.2% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kb-06` | **Areszt Królewski** | Korona & Borgiowie | 2 | 0 | 27.4% → 33.4% | `+6.0%` | 66.0 | `-18.0` | 5.88 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-07` | **Szantaż Pieczęcią** | Korona & Borgiowie | 2 | 0 | 27.4% → 29.2% | `+1.8%` | 80.3 | `-3.7` | 5.96 | 0.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kb-08` | **Przekupstwo Sędziego** | Korona & Borgiowie | 2 | 0 | 27.4% → 29.2% | `+1.8%` | 80.3 | `-3.7` | 5.96 | 0.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kb-10` | **Pieczęć Korony** | Korona & Borgiowie | 3 | 2 | 27.4% → 1.6% | `-25.8%` | 32.9 | `-51.1` | 6.27 | 0.1% | 👑 FILAR KANONU (Core Keystone) |
| `kb-09` | **Dekret Królewski** | Korona & Borgiowie | 4 | 1 | 27.4% → 0.1% | `-27.3%` | 30.6 | `-53.4` | 6.35 | 0.3% | 👑 FILAR KANONU (Core Keystone) |
| `kt-03` | **Zakazana Wiedza** | Kabała z Toledo | 0 | 0 | 26.3% → 13.5% | `-12.8%` | 57.7 | `-26.3` | 6.15 | 0.2% | 👑 FILAR KANONU (Core Keystone) |
| `kt-12` | **Strażnik Archiwum** | Kabała z Toledo | 0 | 1 | 26.3% → 29.0% | `+2.7%` | 77.1 | `-6.9` | 5.93 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-01` | **Rytuał Przejścia** | Kabała z Toledo | 1 | 0 | 26.3% → 28.6% | `+2.3%` | 78.6 | `-5.4` | 5.94 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-02` | **Transmutacja Złota** | Kabała z Toledo | 1 | 0 | 26.3% → 28.6% | `+2.3%` | 78.6 | `-5.4` | 5.94 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-04` | **Zwierciadło Herezji** | Kabała z Toledo | 1 | 0 | 26.3% → 28.3% | `+2.0%` | 79.5 | `-4.5` | 5.94 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-05` | **Wskazówka Cyklu** | Kabała z Toledo | 1 | 1 | 26.3% → 16.6% | `-9.7%` | 66.2 | `-17.8` | 6.11 | 0.2% | 👑 FILAR KANONU (Core Keystone) |
| `kt-07` | **Archiwum Ukryte** | Kabała z Toledo | 1 | 1 | 26.3% → 28.9% | `+2.6%` | 77.8 | `-6.2` | 5.93 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-08` | **Areszt Wiedzy** | Kabała z Toledo | 1 | 0 | 26.3% → 26.3% | `+0.0%` | 82.4 | `-1.6` | 5.99 | 0.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-06` | **Przesłuchanie Imienia** | Kabała z Toledo | 2 | 0 | 26.3% → 25.0% | `-1.3%` | 84.0 | `0.0` | 5.99 | 0.1% | ⚡ MOTOR FRAKCJI (Offensive Engine) |
| `kt-11` | **Medytacja Sefirot** | Kabała z Toledo | 2 | 0 | 26.3% → 29.1% | `+2.8%` | 77.1 | `-6.9` | 5.93 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-09` | **Fragment Kodeksu** | Kabała z Toledo | 2 | 1 | 26.3% → 23.4% | `-2.9%` | 85.0 | `+1.0` | 6.01 | 0.2% | 👑 FILAR KANONU (Core Keystone) |
| `kt-10` | **Pieczęć Salomona** | Kabała z Toledo | 2 | 2 | 26.3% → 39.4% | `+13.1%` | 49.7 | `-34.3` | 5.84 | 0.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `so-05` | **Wezwanie do Trybunału** | Święte Oficjum | 0 | 0 | 23.5% → 21.9% | `-1.6%` | 80.6 | `-3.4` | 5.96 | 0.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-01` | **Patrol Familiariuszy** | Święte Oficjum | 1 | 0 | 23.5% → 24.4% | `+0.9%` | 82.7 | `-1.3` | 5.95 | 0.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-02` | **Skarbiec Trybunału** | Święte Oficjum | 1 | 0 | 23.5% → 22.0% | `-1.5%` | 77.2 | `-6.8` | 6.02 | 0.2% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-04` | **Publiczne Ostrzeżenie** | Święte Oficjum | 1 | 0 | 23.5% → 24.2% | `+0.7%` | 83.5 | `-0.5` | 5.94 | 0.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-12` | **Straż Trybunalska** | Święte Oficjum | 1 | 0 | 23.5% → 24.3% | `+0.8%` | 82.3 | `-1.7` | 5.95 | 0.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-03` | **Podejrzenie** | Święte Oficjum | 2 | 2 | 23.5% → 24.3% | `+0.8%` | 82.0 | `-2.0` | 5.95 | 0.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-08` | **Nasłanie Inkwizytora** | Święte Oficjum | 0 | 0 | 23.5% → 23.9% | `+0.4%` | 82.3 | `-1.7` | 5.94 | 0.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-09` | **Świadek Koronny** | Święte Oficjum | 1 | 0 | 23.5% → 22.4% | `-1.1%` | 82.5 | `-1.5` | 5.96 | 0.1% | ⚡ MOTOR FRAKCJI (Offensive Engine) |
| `so-11` | **Dekret Czystości Wiary** | Święte Oficjum | 1 | 1 | 23.5% → 24.3% | `+0.8%` | 82.3 | `-1.7` | 5.95 | 0.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-06` | **Areszt Trybunalski** | Święte Oficjum | 2 | 0 | 23.5% → 24.2% | `+0.7%` | 81.0 | `-3.0` | 5.96 | 0.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-07` | **Przesłuchanie Oficjum** | Święte Oficjum | 2 | 0 | 23.5% → 24.3% | `+0.8%` | 82.9 | `-1.1` | 5.95 | 0.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-10` | **Oczyść Miasto** | Święte Oficjum | 5 | 1 | 23.5% → 24.4% | `+0.9%` | 82.4 | `-1.6` | 5.95 | 0.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |

---

## 3. ⏳ Warstwa II — Kronika Dziejów w 4P (Ablacja 8 Kart Wydarzeń Czasu)

Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans w 4P:

| ID | Karta Wydarzenia | 4P Score | $\Delta$ 4P | Średnia Er | Deadlock % | Status Roli w Kronice |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `time-01` | **Kapitulacja Grenady** | 84.0 → 🟡 ** 80.9** (`-3.1`) | `-3.1 pkt` | 6.01 Er | 0.2% | 🟢 Stabilizator tempa |
| `time-02` | **Godzina Policyjna** | 84.0 → 🟡 ** 83.0** (`-1.0`) | `-1.0 pkt` | 5.96 Er | 0.2% | 🟢 Stabilizator tempa |
| `time-03` | **Flota Odkrywców** | 84.0 → 🟡 ** 83.8** (`-0.2`) | `-0.2 pkt` | 5.98 Er | 0.2% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-04` | **Rewizja w Dzielnicach** | 84.0 → 🟡 ** 82.7** (`-1.3`) | `-1.3 pkt` | 6.00 Er | 0.2% | 🟢 Stabilizator tempa |
| `time-05` | **Gorączka Donosów** | 84.0 → 🟡 ** 80.6** (`-3.4`) | `-3.4 pkt` | 6.00 Er | 0.2% | 🟢 Stabilizator tempa |
| `time-06` | **Nocna Obława** | 84.0 → 🟡 ** 82.4** (`-1.6`) | `-1.6 pkt` | 5.96 Er | 0.1% | 🟢 Stabilizator tempa |
| `time-07` | **Bunt w Lochach** | 84.0 → 🟡 ** 82.2** (`-1.8`) | `-1.8 pkt` | 5.95 Er | 0.2% | 🟢 Stabilizator tempa |
| `time-08` | **Święte Przymierze** | 84.0 → 🟡 ** 82.3** (`-1.7`) | `-1.7 pkt` | 5.89 Er | 0.1% | 🟢 Stabilizator tempa |
| `time-09` | **Jarmark Królewski** | 84.0 → 🟡 ** 82.8** (`-1.2`) | `-1.2 pkt` | 5.97 Er | 0.1% | 🟢 Stabilizator tempa |
| `time-10` | **Amnestia Biskupia** | 84.0 → 🟡 ** 82.8** (`-1.2`) | `-1.2 pkt` | 5.98 Er | 0.1% | 🟢 Stabilizator tempa |

---

## 4. ⚙️ Warstwa III — Matryca 9 Obszarów Wpływu Mechanik Gry (L1, L2, L4)

Mechaniki w tym raporcie: **skraj albo wyłączenie**. Testy ±1 są w `audit_level1` / `audit_level2` / `audit_level4`. **Δ≈0 nie jest harmonią.**

| Kategoria Mechaniki | Liczba Testów | Rola w Ekosystemie Kanonu 4P | Rekomendacja Balansowa |
| :--- | :---: | :--- | :--- |
| 👑 / 🛡️ **Filary i Bezpieczniki** | **29** | Ablacja wali w stół — gracze czują tę gałkę | **Cel kanonu** |
| ⚠️ **Za słabe dźwignie** | **1** | Rusza share, nie trzyma stołu — nie jest „zbalansowana” | **Wzmocnić aż będzie filarem** |
| 💤 **Martwe / uśpione ścieżki** | **0** | Dual-win z witalności albo ablacja Δ≈0 | Wada pomiaru, nie harmonia |
| ⚠️ / 💡 **Wady bieżącej wartości** | **0** | Inna wartość gałki **podnosi** 4P — obecny setting szkodzi | **Przekręcić albo rework** |

### 4.0. ⚠️ Problematyczne mechaniki (osobny wykaz)
Wszystkie mechaniki z grup **DEAD**, **WEAK/NEUTRAL** i **DISRUPTOR**: ścieżki dual-win z `evaluate_vitality`, testy z $|\Delta\text{4P}| \le 0.8$ i ruchem share $\le 1.5$ pp (DEAD), za słabe dźwignie (WEAK) oraz wady bieżącej wartości (DISRUPTOR).

| Badany Podsystem | Kategoria | 4P Score | $\Delta$ 4P | Klasyfikacja |
| :--- | :--- | :---: | :---: | :--- |
| **Szlak Morski: era 4 → nigdy (99)** | Poziom 4: Warianty i Modyfikatory | 84.0 → 🟡 ** 81.2** (`-2.8`) | `-2.8 pkt` | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |

### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)

| Badany Podsystem / Modyfikator L1 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Limit Er: 14 → 7 (skrajna presja)** | 84.0 → 🟡 ** 75.3** (`-8.7`) | `-8.7 pkt` | 5.68 Er | 25.0% | 1.0% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Próg Oskarżenia: 7 → 1** | 84.0 → 🔴 **  1.6** (`-82.4`) | `-82.4 pkt` | 5.47 Er | 0.0% | 0.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Oskarżenia: 7 → 14** | 84.0 → 🔴 ** 21.9** (`-62.1`) | `-62.1 pkt` | 5.90 Er | 0.3% | 1.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 5zł → 0zł (wyłączenie)** | 84.0 → 🔴 ** 31.8** (`-52.2`) | `-52.2 pkt` | 6.26 Er | 0.1% | 5.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 5zł → 10zł** | 84.0 → 🔴 ** 56.4** (`-27.6`) | `-27.6 pkt` | 5.66 Er | 0.1% | 0.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 1** | 84.0 → 🔴 ** 21.1** (`-62.9`) | `-62.9 pkt` | 8.18 Er | 9.8% | 0.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 6** | 84.0 → 🔴 **  9.7** (`-74.3`) | `-74.3 pkt` | 4.27 Er | 0.0% | 1.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 1** | 84.0 → 🔴 **  2.2** (`-81.8`) | `-81.8 pkt` | 8.69 Er | 1.8% | 11.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 10** | 84.0 → 🔴 **  4.5** (`-79.5`) | `-79.5 pkt` | 4.21 Er | 0.0% | 1.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: cooldown 3 → 0 (co erę)** | 84.0 → 🔴 ** 19.1** (`-64.9`) | `-64.9 pkt` | 5.18 Er | 0.1% | 1.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: całkowite wyłączenie** | 84.0 → 🔴 ** 23.5** (`-60.5`) | `-60.5 pkt` | 8.20 Er | 19.7% | 0.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Akcja Gospodarcza: 0zł (brak zysku złota)** | 84.0 → 🔴 ** 18.1** (`-65.9`) | `-65.9 pkt` | 5.37 Er | 0.0% | 3.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Akcja Gospodarcza: 1 → 2 (podwojenie)** | 84.0 → 🔴 ** 15.1** (`-68.9`) | `-68.9 pkt` | 7.14 Er | 1.2% | 0.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Obserwowanej: 5 → 2 (skrajna presja)** | 84.0 → 🔴 ** 39.6** (`-44.4`) | `-44.4 pkt` | 5.51 Er | 0.0% | 0.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)

| Badany Warunek Zwycięstwa L2 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: stosy 6 → 1** | 84.0 → 🔴 ** 16.2** (`-67.8`) | `-67.8 pkt` | 3.71 Er | 0.0% | 1.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: stosy 6 → 12** | 84.0 → 🔴 ** 52.7** (`-31.3`) | `-31.3 pkt` | 6.22 Er | 1.1% | 0.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 1** | 84.0 → 🔴 ** 16.3** (`-67.7`) | `-67.7 pkt` | 4.12 Er | 0.0% | 1.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 6** | 84.0 → 🟡 ** 78.1** (`-5.9`) | `-5.9 pkt` | 6.01 Er | 0.1% | 1.0% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Cienie: relikwie 2 → 4** | 84.0 → 🔴 ** 30.1** (`-53.9`) | `-53.9 pkt` | 6.46 Er | 0.1% | 1.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: dekrety 2 → 4** | 84.0 → 🔴 ** 31.2** (`-52.8`) | `-52.8 pkt` | 6.24 Er | 0.2% | 1.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: fragmenty 2 → 4** | 84.0 → 🔴 ** 37.4** (`-46.6`) | `-46.6 pkt` | 6.23 Er | 0.2% | 0.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: era 6 → 1** | 84.0 → 🔴 ** 41.3** (`-42.7`) | `-42.7 pkt` | 4.79 Er | 0.1% | 0.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: era 6 → 12** | 84.0 → 🔴 ** 33.4** (`-50.6`) | `-50.6 pkt` | 6.25 Er | 0.1% | 0.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 8 → 1** | 84.0 → 🔴 ** 18.6** (`-65.4`) | `-65.4 pkt` | 3.11 Er | 0.1% | 1.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 8 → 16** | 84.0 → 🔴 ** 36.0** (`-48.0`) | `-48.0 pkt` | 6.31 Er | 0.4% | 0.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)

| Badany Wariant / Modyfikator L4 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kronika Dziejów: całkowite wyłączenie** | 84.0 → 🟡 ** 78.7** (`-5.3`) | `-5.3 pkt` | 6.01 Er | 0.1% | 1.0% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Kronika Dziejów: co 3 Ery (spowolniony zegar)** | 84.0 → 🟡 ** 79.5** (`-4.5`) | `-4.5 pkt` | 6.06 Er | 0.2% | 1.0% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Inkwizytor Patrol: ruch 1 → 0 (wyłączenie)** | 84.0 → 🔴 ** 25.5** (`-58.5`) | `-58.5 pkt` | 8.93 Er | 26.8% | 0.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Inkwizytor Patrol: ruch x2 (podwojona prędkość)** | 84.0 → 🟡 ** 77.7** (`-6.3`) | `-6.3 pkt` | 5.96 Er | 0.2% | 1.0% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Szlak Morski: era 4 → nigdy (99)** | 84.0 → 🟡 ** 81.2** (`-2.8`) | `-2.8 pkt` | 5.99 Er | 0.1% | 0.9% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |

---

## 5. 👥 Warstwa IV — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych. Kolumna win share to HUD kanonu; setup+witalność to stary blend (kara martwej ścieżki).

| Nieobecna Frakcja | Setup Testowy | Win share | Setup+witalność | Diagnoza |
| :--- | :--- | :---: | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`92.1`** | `92.1` | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`91.7`** | `91.7` | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`83.7`** | `83.7` | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`73.4`** | `73.4` | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`79.2`** | `79.2` | Brak presji stosów i bezpośredniego Inkwizytora |