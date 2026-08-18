# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v0.99.10

**Wersja Gry:** `v0.99.10` | **Data Badania:** 2026-08-18 09:14 | **Próba:** 5000 gier/setup (25000 gier na wariant) | **Ziarno:** 42
**4P Score (win share):** 🟠 ** 65.2** pkt | **Witalność (osobna kara):** `0.178` | **Śr. Er:** `6.19` | **Deadlocki:** `2.1%` | **Pas Biedy:** `1.4%`
**Udziały 4P:** CAA 21.3% · GC 23.7% · KB 26.9% · KT 25.4% · SO 27.6%

Klasyfikacja L1/L2/L4 i Δ 4P liczą wyłącznie równość win share (`calculate_balance_score`). Kara witalności jest osobno.

**Ostrzeżenia witalności (nie w 4P Score):**
- 4p-core: Paraliż Gry / Deadlocks 6.8% (>5%)

---

## 0. Wady z tej próby (nie HUD win share)

Kubełki klasyfikatora i ostrzeżenia witalności z bieżącego runu.

- **Share |Δ| ≥ 2.5 pp od 25%:** CAA 21.3%, SO 27.6%
- **Autopodatek (SELF_HARM):** 21/60
- **Karty Kroniki |Δ4P| ≤ 0.8:** 8/8
- **Ablacja całej Kroniki (`L4_NO_TIME_DECK`):** Δ4P -7.1 (STABILIZER)
- **Mechaniki WEAK/NEUTRAL:** Święte Oficjum: skazania 3 → 6
- **Mechaniki DEAD:** Korona: wymóg haków 0 → 2 (podatek)
- **Mechaniki DISRUPTOR:** Limit Er: 12 → 6 (skrajna presja)

---

## 1. 🗺️ Podsumowanie Ekosystemu Kart Kanonu 4P (Matryca Wpływu Kart, 60 kart)

Rozkład wszystkich 60 kart frakcyjnych w matrycy **Wpływ na Frakcję ($\Delta \text{Share}$)** vs **Wpływ na Kanon 4P ($\Delta \text{4P Score}$)**:

| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |
| :--- | :---: | :---: | :--- | :--- |
| 🩸 **Autopodatek (Self-Harm)** | **21** | 35.0% | Wyłączenie **podnosi** win share własnej frakcji — karta jest haraczem, nie silnikiem | **Rework / osłabienie kosztu, nie filar** |
| 💤 **Karta Pasywna (Dead Weight)** | **0** | 0.0% | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia lub wycięcia** |
| ⚠️ **Karta Destabilizująca (Disruptor)** | **3** | 5.0% | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |
| ⚖️ **Zbalansowane Narzędzie** | **16** | 26.7% | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Narzędzie, nie złoty środek całego kanonu** |
| 👑 / ⚓ **Filar / Kotwica Kanonu** | **20** | 33.3% | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |

---

## 2. 🃏 Warstwa I — Szczegółowa Analiza 60 Kart Frakcji w Kanonie 4P

### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)
Karty, których brak powoduje spadek wyniku Kanonu 4P o $\ge 4.0$ pkt lub załamanie winrate frakcji o $\ge 4.0\%$ — **bez** autopodatków (te są w 2.1b):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kb-09` **Dekret Królewski** | Korona & Borgiowie | 4zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 26.9% → **0.1%** | **`-26.8%`** | 65.2 → **26.7 pkt** (`-38.5`) |
| `kb-10` **Pieczęć Korony** | Korona & Borgiowie | 3zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 26.9% → **0.2%** | **`-26.7%`** | 65.2 → **27.0 pkt** (`-38.2`) |
| `kt-03` **Zakazana Wiedza** | Kabała z Toledo | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.4% → **7.6%** | **`-17.8%`** | 65.2 → **31.8 pkt** (`-33.4`) |
| `caa-10` **Echo Alhambry** | Cienie Al-Andalus | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 21.3% → **4.2%** | **`-17.1%`** | 65.2 → **32.0 pkt** (`-33.2`) |
| `kt-05` **Wskazówka Cyklu** | Kabała z Toledo | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.4% → **13.5%** | **`-11.9%`** | 65.2 → **45.1 pkt** (`-20.1`) |
| `caa-05` **Ukryty Kurier** | Cienie Al-Andalus | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 21.3% → **13.0%** | **`-8.3%`** | 65.2 → **48.5 pkt** (`-16.7`) |
| `kt-10` **Pieczęć Salomona** | Kabała z Toledo | 2zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 25.4% → **18.2%** | **`-7.2%`** | 65.2 → **55.9 pkt** (`-9.3`) |
| `caa-03` **Cień na Rynku** | Cienie Al-Andalus | 0zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 21.3% → **20.2%** | **`-1.1%`** | 65.2 → **57.0 pkt** (`-8.2`) |
| `gc-06` **Szantaż** | Gildia Cieni | 2zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.7% → **22.3%** | **`-1.4%`** | 65.2 → **60.5 pkt** (`-4.7`) |
| `caa-06` **Ucieczka z Lochów** | Cienie Al-Andalus | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 21.3% → **19.0%** | **`-2.3%`** | 65.2 → **60.7 pkt** (`-4.5`) |
| `caa-02` **Złoto z Kryjówki** | Cienie Al-Andalus | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 21.3% → **23.2%** | **`+1.9%`** | 65.2 → **61.6 pkt** (`-3.6`) |
| `gc-05` **Fałszywy Świadek** | Gildia Cieni | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.7% → **22.4%** | **`-1.3%`** | 65.2 → **61.6 pkt** (`-3.6`) |
| `caa-09` **Kurier Relikwii** | Cienie Al-Andalus | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 21.3% → **22.6%** | **`+1.3%`** | 65.2 → **62.0 pkt** (`-3.2`) |
| `kb-02` **Pobór Podatków** | Korona & Borgiowie | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 26.9% → **24.7%** | **`-2.2%`** | 65.2 → **62.1 pkt** (`-3.1`) |
| `gc-09` **Lista Dłużników** | Gildia Cieni | 3zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.7% → **22.2%** | **`-1.5%`** | 65.2 → **62.3 pkt** (`-2.9`) |
| `gc-03` **Podrzucenie Księgi** | Gildia Cieni | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.7% → **23.6%** | **`-0.1%`** | 65.2 → **62.6 pkt** (`-2.6`) |
| `so-11` **Dekret Czystości Wiary** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 27.6% → **28.3%** | **`+0.7%`** | 65.2 → **62.9 pkt** (`-2.3`) |
| `so-06` **Areszt Trybunalski** | Święte Oficjum | 2zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 27.6% → **28.7%** | **`+1.1%`** | 65.2 → **63.0 pkt** (`-2.2`) |
| `so-07` **Przesłuchanie Oficjum** | Święte Oficjum | 2zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 27.6% → **28.7%** | **`+1.1%`** | 65.2 → **63.0 pkt** (`-2.2`) |
| `so-05` **Wezwanie do Trybunału** | Święte Oficjum | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 27.6% → **25.1%** | **`-2.5%`** | 65.2 → **65.5 pkt** (`0.3`) |

### 2.1b. 🩸 Autopodatek Frakcji (Self-Harm)
Karty, których wyłączenie **podnosi** win share własnej frakcji. Gracz zauważy je jako haracz, nawet gdy stół 4P jest równy dzięki temu haraczowi.

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kb-04` **Faworyt Dworu** | Korona & Borgiowie | 2zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 26.9% → **41.5%** | **`+14.6%`** | 65.2 → **47.9 pkt** (`-17.3`) |
| `caa-01` **Przejście Podziemiami** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 21.3% → **34.9%** | **`+13.6%`** | 65.2 → **56.0 pkt** (`-9.2`) |
| `caa-11` **Nocna Zmiana Warty** | Cienie Al-Andalus | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 21.3% → **34.9%** | **`+13.6%`** | 65.2 → **56.4 pkt** (`-8.8`) |
| `caa-04` **Fałszywy Trop** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 21.3% → **34.8%** | **`+13.5%`** | 65.2 → **56.4 pkt** (`-8.8`) |
| `caa-07` **Szantaż Bractwa** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 21.3% → **34.3%** | **`+13.0%`** | 65.2 → **57.3 pkt** (`-7.9`) |
| `caa-08` **Kaptur Nocy** | Cienie Al-Andalus | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 21.3% → **34.1%** | **`+12.8%`** | 65.2 → **57.9 pkt** (`-7.3`) |
| `kb-07` **Szantaż Pieczęcią** | Korona & Borgiowie | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 26.9% → **32.4%** | **`+5.5%`** | 65.2 → **57.2 pkt** (`-8.0`) |
| `kb-08` **Przekupstwo Sędziego** | Korona & Borgiowie | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 26.9% → **32.4%** | **`+5.5%`** | 65.2 → **57.2 pkt** (`-8.0`) |
| `kt-01` **Rytuał Przejścia** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.4% → **30.5%** | **`+5.1%`** | 65.2 → **59.6 pkt** (`-5.6`) |
| `kt-02` **Transmutacja Złota** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.4% → **30.5%** | **`+5.1%`** | 65.2 → **59.6 pkt** (`-5.6`) |
| `kt-04` **Zwierciadło Herezji** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.4% → **30.2%** | **`+4.8%`** | 65.2 → **60.2 pkt** (`-5.0`) |
| `kt-07` **Archiwum Ukryte** | Kabała z Toledo | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.4% → **30.2%** | **`+4.8%`** | 65.2 → **59.5 pkt** (`-5.7`) |
| `kt-08` **Areszt Wiedzy** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.4% → **30.2%** | **`+4.8%`** | 65.2 → **59.5 pkt** (`-5.7`) |
| `kt-09` **Fragment Kodeksu** | Kabała z Toledo | 2zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.4% → **30.2%** | **`+4.8%`** | 65.2 → **59.8 pkt** (`-5.4`) |
| `kt-11` **Medytacja Sefirot** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.4% → **29.8%** | **`+4.4%`** | 65.2 → **60.0 pkt** (`-5.2`) |
| `kt-12` **Strażnik Archiwum** | Kabała z Toledo | 0zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.4% → **29.7%** | **`+4.3%`** | 65.2 → **59.9 pkt** (`-5.3`) |
| `gc-04` **Informator** | Gildia Cieni | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 23.7% → **27.4%** | **`+3.7%`** | 65.2 → **63.3 pkt** (`-1.9`) |
| `kb-12` **Szantaż Salonowy** | Korona & Borgiowie | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 26.9% → **30.4%** | **`+3.5%`** | 65.2 → **60.3 pkt** (`-4.9`) |
| `kb-05` **List Żelazny** | Korona & Borgiowie | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 26.9% → **30.1%** | **`+3.2%`** | 65.2 → **62.8 pkt** (`-2.4`) |
| `gc-02` **Czarny Rynek** | Gildia Cieni | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 23.7% → **26.7%** | **`+3.0%`** | 65.2 → **63.0 pkt** (`-2.2`) |
| `caa-12` **Skrytka w Murach** | Cienie Al-Andalus | 0zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 21.3% → **23.7%** | **`+2.4%`** | 65.2 → **63.1 pkt** (`-2.1`) |

### 2.2. ⚠️ Karty Destabilizujące Kanon 4P (Disruptors)
Karty, których wyłączenie podnosi 4P Score ($\Delta \text{4P} \ge +1.5$ pkt):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kb-11` **Tajny Emisariusz** | Korona & Borgiowie | 1zł / 0☣ | ⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor) | 26.9% → **26.6%** | `-0.3%` | 65.2 → **67.8 pkt** (`+2.6`) |
| `kb-06` **Areszt Królewski** | Korona & Borgiowie | 1zł / 0☣ | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) | 26.9% → **26.0%** | `-0.9%` | 65.2 → **67.6 pkt** (`+2.4`) |
| `kb-03` **Plotka Dworska** | Korona & Borgiowie | 1zł / 1☣ | ⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor) | 26.9% → **26.6%** | `-0.3%` | 65.2 → **66.5 pkt** (`+1.3`) |

### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich 60 Kart Frakcji w Kanonie 4P

| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Faction Win Share 4P | $\Delta$ Frakcji | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `caa-01` | **Przejście Podziemiami** | Cienie Al-Andalus | 0 | 0 | 21.3% → 34.9% | `+13.6%` | 56.0 | `-9.2` | 5.91 | 1.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-02` | **Złoto z Kryjówki** | Cienie Al-Andalus | 0 | 0 | 21.3% → 23.2% | `+1.9%` | 61.6 | `-3.6` | 6.17 | 2.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-03` | **Cień na Rynku** | Cienie Al-Andalus | 0 | 1 | 21.3% → 20.2% | `-1.1%` | 57.0 | `-8.2` | 6.51 | 2.6% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-04` | **Fałszywy Trop** | Cienie Al-Andalus | 0 | 0 | 21.3% → 34.8% | `+13.5%` | 56.4 | `-8.8` | 5.90 | 1.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-05` | **Ukryty Kurier** | Cienie Al-Andalus | 0 | 0 | 21.3% → 13.0% | `-8.3%` | 48.5 | `-16.7` | 6.37 | 2.1% | 👑 FILAR KANONU (Core Keystone) |
| `caa-12` | **Skrytka w Murach** | Cienie Al-Andalus | 0 | 1 | 21.3% → 23.7% | `+2.4%` | 63.1 | `-2.1` | 6.25 | 2.5% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-06` | **Ucieczka z Lochów** | Cienie Al-Andalus | 0 | 0 | 21.3% → 19.0% | `-2.3%` | 60.7 | `-4.5` | 6.06 | 1.8% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-07` | **Szantaż Bractwa** | Cienie Al-Andalus | 0 | 0 | 21.3% → 34.3% | `+13.0%` | 57.3 | `-7.9` | 5.91 | 1.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-08` | **Kaptur Nocy** | Cienie Al-Andalus | 1 | 0 | 21.3% → 34.1% | `+12.8%` | 57.9 | `-7.3` | 5.92 | 1.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-11` | **Nocna Zmiana Warty** | Cienie Al-Andalus | 1 | 0 | 21.3% → 34.9% | `+13.6%` | 56.4 | `-8.8` | 5.89 | 1.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-09` | **Kurier Relikwii** | Cienie Al-Andalus | 0 | 0 | 21.3% → 22.6% | `+1.3%` | 62.0 | `-3.2` | 6.17 | 2.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-10` | **Echo Alhambry** | Cienie Al-Andalus | 0 | 0 | 21.3% → 4.2% | `-17.1%` | 32.0 | `-33.2` | 6.63 | 2.6% | 👑 FILAR KANONU (Core Keystone) |
| `gc-05` | **Fałszywy Świadek** | Gildia Cieni | 0 | 0 | 23.7% → 22.4% | `-1.3%` | 61.6 | `-3.6` | 6.17 | 2.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-12` | **Złodziejski Zwiad** | Gildia Cieni | 0 | 2 | 23.7% → 24.2% | `+0.5%` | 64.5 | `-0.7` | 6.14 | 2.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-01` | **Przekupiony Strażnik** | Gildia Cieni | 1 | 1 | 23.7% → 23.4% | `-0.3%` | 63.6 | `-1.6` | 6.15 | 2.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-02` | **Czarny Rynek** | Gildia Cieni | 1 | 1 | 23.7% → 26.7% | `+3.0%` | 63.0 | `-2.2` | 6.24 | 2.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `gc-03` | **Podrzucenie Księgi** | Gildia Cieni | 1 | 0 | 23.7% → 23.6% | `-0.1%` | 62.6 | `-2.6` | 6.16 | 2.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-04` | **Informator** | Gildia Cieni | 1 | 1 | 23.7% → 27.4% | `+3.7%` | 63.3 | `-1.9` | 6.23 | 2.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `gc-11` | **Fałszywe Świadectwo Cechu** | Gildia Cieni | 1 | 0 | 23.7% → 24.2% | `+0.5%` | 64.3 | `-0.9` | 6.15 | 2.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-06` | **Szantaż** | Gildia Cieni | 2 | 1 | 23.7% → 22.3% | `-1.4%` | 60.5 | `-4.7` | 6.37 | 2.5% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-07` | **Skrytobójstwo** | Gildia Cieni | 2 | 0 | 23.7% → 23.8% | `+0.1%` | 63.5 | `-1.7` | 6.17 | 2.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-08` | **Zatrute Złoto** | Gildia Cieni | 2 | 0 | 23.7% → 23.8% | `+0.1%` | 63.5 | `-1.7` | 6.17 | 2.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-09` | **Lista Dłużników** | Gildia Cieni | 3 | 1 | 23.7% → 22.2% | `-1.5%` | 62.3 | `-2.9` | 6.36 | 2.5% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-10` | **Upadek Domu** | Gildia Cieni | 4 | 2 | 23.7% → 24.3% | `+0.6%` | 64.5 | `-0.7` | 6.14 | 1.9% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-01` | **Rozkaz Dworu** | Korona & Borgiowie | 1 | 1 | 26.9% → 25.9% | `-1.0%` | 66.3 | `+1.1` | 6.17 | 1.5% | ⚡ MOTOR FRAKCJI (Offensive Engine) |
| `kb-02` | **Pobór Podatków** | Korona & Borgiowie | 1 | 0 | 26.9% → 24.7% | `-2.2%` | 62.1 | `-3.1` | 6.25 | 2.2% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kb-03` | **Plotka Dworska** | Korona & Borgiowie | 1 | 1 | 26.9% → 26.6% | `-0.3%` | 66.5 | `+1.3` | 6.17 | 1.5% | ⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor) |
| `kb-11` | **Tajny Emisariusz** | Korona & Borgiowie | 1 | 0 | 26.9% → 26.6% | `-0.3%` | 67.8 | `+2.6` | 6.16 | 1.5% | ⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor) |
| `kb-04` | **Faworyt Dworu** | Korona & Borgiowie | 2 | 1 | 26.9% → 41.5% | `+14.6%` | 47.9 | `-17.3` | 5.91 | 1.3% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-05` | **List Żelazny** | Korona & Borgiowie | 2 | 0 | 26.9% → 30.1% | `+3.2%` | 62.8 | `-2.4` | 6.07 | 1.8% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-06` | **Areszt Królewski** | Korona & Borgiowie | 1 | 0 | 26.9% → 26.0% | `-0.9%` | 67.6 | `+2.4` | 6.20 | 1.6% | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) |
| `kb-12` | **Szantaż Salonowy** | Korona & Borgiowie | 1 | 0 | 26.9% → 30.4% | `+3.5%` | 60.3 | `-4.9` | 6.19 | 2.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-07` | **Szantaż Pieczęcią** | Korona & Borgiowie | 2 | 0 | 26.9% → 32.4% | `+5.5%` | 57.2 | `-8.0` | 6.15 | 2.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-08` | **Przekupstwo Sędziego** | Korona & Borgiowie | 2 | 0 | 26.9% → 32.4% | `+5.5%` | 57.2 | `-8.0` | 6.15 | 2.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-10` | **Pieczęć Korony** | Korona & Borgiowie | 3 | 2 | 26.9% → 0.2% | `-26.7%` | 27.0 | `-38.2` | 6.54 | 2.4% | 👑 FILAR KANONU (Core Keystone) |
| `kb-09` | **Dekret Królewski** | Korona & Borgiowie | 4 | 1 | 26.9% → 0.1% | `-26.8%` | 26.7 | `-38.5` | 6.58 | 2.9% | 👑 FILAR KANONU (Core Keystone) |
| `kt-03` | **Zakazana Wiedza** | Kabała z Toledo | 0 | 0 | 25.4% → 7.6% | `-17.8%` | 31.8 | `-33.4` | 6.52 | 2.6% | 👑 FILAR KANONU (Core Keystone) |
| `kt-12` | **Strażnik Archiwum** | Kabała z Toledo | 0 | 1 | 25.4% → 29.7% | `+4.3%` | 59.9 | `-5.3` | 6.08 | 1.6% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-01` | **Rytuał Przejścia** | Kabała z Toledo | 1 | 0 | 25.4% → 30.5% | `+5.1%` | 59.6 | `-5.6` | 6.06 | 1.5% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-02` | **Transmutacja Złota** | Kabała z Toledo | 1 | 0 | 25.4% → 30.5% | `+5.1%` | 59.6 | `-5.6` | 6.06 | 1.5% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-04` | **Zwierciadło Herezji** | Kabała z Toledo | 1 | 0 | 25.4% → 30.2% | `+4.8%` | 60.2 | `-5.0` | 6.06 | 1.5% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-05` | **Wskazówka Cyklu** | Kabała z Toledo | 1 | 0 | 25.4% → 13.5% | `-11.9%` | 45.1 | `-20.1` | 6.39 | 2.5% | 👑 FILAR KANONU (Core Keystone) |
| `kt-07` | **Archiwum Ukryte** | Kabała z Toledo | 1 | 1 | 25.4% → 30.2% | `+4.8%` | 59.5 | `-5.7` | 6.08 | 1.5% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-08` | **Areszt Wiedzy** | Kabała z Toledo | 1 | 0 | 25.4% → 30.2% | `+4.8%` | 59.5 | `-5.7` | 6.08 | 1.5% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-11` | **Medytacja Sefirot** | Kabała z Toledo | 1 | 0 | 25.4% → 29.8% | `+4.4%` | 60.0 | `-5.2` | 6.08 | 1.6% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-06` | **Przesłuchanie Imienia** | Kabała z Toledo | 2 | 0 | 25.4% → 23.4% | `-2.0%` | 65.3 | `+0.1` | 6.20 | 1.9% | ⚡ MOTOR FRAKCJI (Offensive Engine) |
| `kt-09` | **Fragment Kodeksu** | Kabała z Toledo | 2 | 1 | 25.4% → 30.2% | `+4.8%` | 59.8 | `-5.4` | 6.08 | 1.5% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-10` | **Pieczęć Salomona** | Kabała z Toledo | 2 | 2 | 25.4% → 18.2% | `-7.2%` | 55.9 | `-9.3` | 6.37 | 3.0% | 👑 FILAR KANONU (Core Keystone) |
| `so-05` | **Wezwanie do Trybunału** | Święte Oficjum | 0 | 0 | 27.6% → 25.1% | `-2.5%` | 65.5 | `+0.3` | 6.22 | 2.2% | 👑 FILAR KANONU (Core Keystone) |
| `so-01` | **Patrol Familiariuszy** | Święte Oficjum | 1 | 0 | 27.6% → 29.0% | `+1.4%` | 63.4 | `-1.8` | 6.20 | 2.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `so-02` | **Skarbiec Trybunału** | Święte Oficjum | 1 | 0 | 27.6% → 26.5% | `-1.1%` | 65.7 | `+0.5` | 6.30 | 2.5% | ⚡ MOTOR FRAKCJI (Offensive Engine) |
| `so-04` | **Publiczne Ostrzeżenie** | Święte Oficjum | 1 | 0 | 27.6% → 28.5% | `+0.9%` | 63.4 | `-1.8` | 6.18 | 1.9% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-12` | **Straż Trybunalska** | Święte Oficjum | 1 | 0 | 27.6% → 28.5% | `+0.9%` | 63.5 | `-1.7` | 6.17 | 1.8% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-03` | **Podejrzenie** | Święte Oficjum | 2 | 0 | 27.6% → 28.5% | `+0.9%` | 63.4 | `-1.8` | 6.18 | 1.9% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-08` | **Nasłanie Inkwizytora** | Święte Oficjum | 0 | 0 | 27.6% → 27.9% | `+0.3%` | 64.1 | `-1.1` | 6.18 | 2.2% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-11` | **Dekret Czystości Wiary** | Święte Oficjum | 1 | 0 | 27.6% → 28.3% | `+0.7%` | 62.9 | `-2.3` | 6.18 | 1.8% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-06` | **Areszt Trybunalski** | Święte Oficjum | 2 | 0 | 27.6% → 28.7% | `+1.1%` | 63.0 | `-2.2` | 6.18 | 2.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-07` | **Przesłuchanie Oficjum** | Święte Oficjum | 2 | 0 | 27.6% → 28.7% | `+1.1%` | 63.0 | `-2.2` | 6.18 | 2.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-09` | **Świadek Koronny** | Święte Oficjum | 2 | 0 | 27.6% → 28.3% | `+0.7%` | 63.6 | `-1.6` | 6.18 | 2.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-10` | **Oczyść Miasto** | Święte Oficjum | 5 | 2 | 27.6% → 28.5% | `+0.9%` | 63.8 | `-1.4` | 6.20 | 1.9% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |

---

## 3. ⏳ Warstwa II — Kronika Dziejów w 4P (Ablacja 8 Kart Wydarzeń Czasu)

Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans w 4P:

| ID | Karta Wydarzenia | 4P Score | $\Delta$ 4P | Średnia Er | Deadlock % | Status Roli w Kronice |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `tc-01` | **Kres Średniowiecza** | 🟠 ** 65.2** | `0.0 pkt` | 6.19 Er | 2.1% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-02` | **Płonący Stos** | 🟠 ** 65.2** | `0.0 pkt` | 6.19 Er | 2.1% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-03` | **Królewski Podatek** | 🟠 ** 65.2** | `0.0 pkt` | 6.19 Er | 2.1% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-04` | **Spisek w Cieniu** | 🟠 ** 65.2** | `0.0 pkt` | 6.19 Er | 2.1% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-05` | **Złoty Wiek** | 🟠 ** 65.2** | `0.0 pkt` | 6.19 Er | 2.1% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-06` | **Czystka w Mieście** | 🟠 ** 65.2** | `0.0 pkt` | 6.19 Er | 2.1% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-07` | **Druga Szansa** | 🟠 ** 65.2** | `0.0 pkt` | 6.19 Er | 2.1% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-08` | **Zaćmienie Słońca** | 🟠 ** 65.2** | `0.0 pkt` | 6.19 Er | 2.1% | 💤 Martwa karta kroniki (Δ≈0) |

---

## 4. ⚙️ Warstwa III — Matryca 9 Obszarów Wpływu Mechanik Gry (L1, L2, L4)

Mechaniki w tym raporcie: **skraj albo wyłączenie**. Testy ±1 są w `audit_level1` / `audit_level2` / `audit_level4`. **Δ≈0 nie jest harmonią.**

| Kategoria Mechaniki | Liczba Testów | Rola w Ekosystemie Kanonu 4P | Rekomendacja Balansowa |
| :--- | :---: | :--- | :--- |
| 👑 / 🛡️ **Filary i Bezpieczniki** | **24** | Ablacja wali w stół — gracze czują tę gałkę | **Cel kanonu** |
| ⚠️ **Za słabe dźwignie** | **1** | Rusza share, nie trzyma stołu — nie jest „zbalansowana” | **Wzmocnić aż będzie filarem** |
| 💤 **Martwe / uśpione ścieżki** | **1** | Dual-win z witalności albo ablacja Δ≈0 | Wada pomiaru, nie harmonia |
| ⚠️ / 💡 **Wady bieżącej wartości** | **1** | Inna wartość gałki **podnosi** 4P — obecny setting szkodzi | **Przekręcić albo rework** |

### 4.0. 💤 Martwe mechaniki (osobny wykaz)
Ścieżki dual-win z `evaluate_vitality` oraz testy z $|\Delta\text{4P}| \le 0.8$ i ruchem share $\le 1.5$ pp.

| Badany Podsystem | Kategoria | 4P Score | $\Delta$ 4P | Klasyfikacja |
| :--- | :--- | :---: | :---: | :--- |
| **Korona: wymóg haków 0 → 2 (podatek)** | Poziom 2: Warunki Zwycięstwa | 🟠 ** 65.2** | `0.0 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |

### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)

| Badany Podsystem / Modyfikator L1 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Limit Er: 12 → 6 (skrajna presja)** | 65.2 → 🟠 ** 68.4** (`⬆️ +3.2`) | `+3.2 pkt` | 5.44 Er | 69.3% | 1.5% | 💡 KANDYDAT DO UPROSZCZENIA (Simplification) |
| **Próg Oskarżenia: 7 → 1** | 65.2 → 🔴 **  2.5** (`-62.7`) | `-62.7 pkt` | 5.42 Er | 0.0% | 0.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Oskarżenia: 7 → 14** | 65.2 → 🔴 ** 22.6** (`-42.6`) | `-42.6 pkt` | 6.09 Er | 1.7% | 1.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 0zł (wyłączenie)** | 65.2 → 🔴 ** 43.0** (`-22.2`) | `-22.2 pkt` | 6.45 Er | 2.1% | 6.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 8zł** | 65.2 → 🔴 ** 52.2** (`-13.0`) | `-13.0 pkt` | 5.91 Er | 1.4% | 0.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 1** | 65.2 → 🔴 ** 20.1** (`-45.1`) | `-45.1 pkt` | 8.45 Er | 29.6% | 1.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 6** | 65.2 → 🔴 **  9.7** (`-55.5`) | `-55.5 pkt` | 4.47 Er | 0.0% | 1.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 1** | 65.2 → 🔴 **  2.6** (`-62.6`) | `-62.6 pkt` | 9.13 Er | 15.7% | 9.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 10** | 65.2 → 🔴 **  7.4** (`-57.8`) | `-57.8 pkt` | 4.58 Er | 0.0% | 2.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: cooldown 3 → 0 (co erę)** | 65.2 → 🔴 ** 14.2** (`-51.0`) | `-51.0 pkt` | 5.14 Er | 0.8% | 1.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: całkowite wyłączenie** | 65.2 → 🔴 ** 28.4** (`-36.8`) | `-36.8 pkt` | 8.62 Er | 45.9% | 0.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)

| Badany Warunek Zwycięstwa L2 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: stosy 6 → 1** | 65.2 → 🔴 ** 12.6** (`-52.6`) | `-52.6 pkt` | 3.80 Er | 0.1% | 1.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: stosy 6 → 12** | 65.2 → 🔴 ** 47.4** (`-17.8`) | `-17.8 pkt` | 6.48 Er | 5.5% | 1.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 1** | 65.2 → 🔴 ** 12.8** (`-52.4`) | `-52.4 pkt` | 4.30 Er | 0.1% | 1.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 6** | 65.2 → 🟠 ** 64.9** (`-0.3`) | `-0.3 pkt` | 6.22 Er | 2.3% | 1.4% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |
| **Cienie: relikwie 2 → 4** | 65.2 → 🔴 ** 26.6** (`-38.6`) | `-38.6 pkt` | 6.64 Er | 2.4% | 1.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: dekrety 2 → 4** | 65.2 → 🔴 ** 27.1** (`-38.1`) | `-38.1 pkt` | 6.53 Er | 2.8% | 1.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: wymóg haków 0 → 2 (podatek)** | 🟠 ** 65.2** | `0.0 pkt` | 6.19 Er | 2.1% | 1.4% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Kabała: fragmenty 2 → 4** | 65.2 → 🔴 ** 25.7** (`-39.5`) | `-39.5 pkt` | 6.42 Er | 2.2% | 1.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: era 6 → 1** | 65.2 → 🔴 ** 29.3** (`-35.9`) | `-35.9 pkt` | 4.79 Er | 2.1% | 1.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: era 6 → 12** | 65.2 → 🔴 ** 24.7** (`-40.5`) | `-40.5 pkt` | 6.43 Er | 2.2% | 1.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 8 → 1** | 65.2 → 🔴 ** 12.5** (`-52.7`) | `-52.7 pkt` | 3.37 Er | 1.4% | 1.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 8 → 16** | 65.2 → 🔴 ** 34.6** (`-30.6`) | `-30.6 pkt` | 6.57 Er | 5.9% | 1.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)

| Badany Wariant / Modyfikator L4 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kronika Dziejów: całkowite wyłączenie** | 65.2 → 🔴 ** 58.1** (`-7.1`) | `-7.1 pkt` | 6.28 Er | 2.1% | 1.7% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Werdykt Sądu: tajny (wyłączenie jawnej koordynacji)** | 65.2 → 🔴 ** 59.8** (`-5.4`) | `-5.4 pkt` | 6.03 Er | 1.3% | 1.4% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Inkwizytor Patrol: ruch 1 → 0 (wyłączenie)** | 65.2 → 🔴 ** 21.2** (`-44.0`) | `-44.0 pkt` | 8.72 Er | 46.5% | 0.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Szlak Morski: era 4 → nigdy (99)** | 65.2 → 🟠 ** 60.6** (`-4.6`) | `-4.6 pkt` | 6.24 Er | 2.1% | 1.4% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |

---

## 5. 👥 Warstwa IV — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych. Kolumna win share to HUD kanonu; setup+witalność to stary blend (kara martwej ścieżki).

| Nieobecna Frakcja | Setup Testowy | Win share | Setup+witalność | Diagnoza |
| :--- | :--- | :---: | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`61.6`** | `51.6` | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`60.5`** | `60.5` | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`78.0`** | `78.0` | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`64.5`** | `64.5` | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`61.6`** | `61.6` | Brak presji stosów i bezpośredniego Inkwizytora |