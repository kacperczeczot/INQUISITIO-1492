# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v0.99.10

**Wersja Gry:** `v0.99.10` | **Data Badania:** 2026-08-18 10:23 | **Próba:** 5000 gier/setup (25000 gier na wariant) | **Ziarno:** 42
**4P Score (win share):** 🟠 ** 66.0** pkt | **Witalność (osobna kara):** `0.048` | **Śr. Er:** `6.13` | **Deadlocki:** `1.7%` | **Pas Biedy:** `1.5%`
**Udziały 4P:** CAA 21.2% · GC 24.3% · KB 30.0% · KT 24.8% · SO 24.6%

Klasyfikacja L1/L2/L4 i Δ 4P liczą wyłącznie równość win share (`calculate_balance_score`). Kara witalności jest osobno.

**Ostrzeżenia witalności (nie w 4P Score):**
- 4p-core: Paraliż Gry / Deadlocks 5.5% (>5%)

---

## 0. Wady z tej próby (nie HUD win share)

Kubełki klasyfikatora i ostrzeżenia witalności z bieżącego runu.

- **Share |Δ| ≥ 2.5 pp od 25%:** CAA 21.2%, KB 30.0%
- **Autopodatek (SELF_HARM):** 21/60
- **DEAD_WEIGHT:** `gc-11` Fałszywe Świadectwo Cechu, `gc-07` Skrytobójstwo, `gc-08` Zatrute Złoto, `gc-10` Upadek Domu, `so-08` Nasłanie Inkwizytora
- **Karty Kroniki |Δ4P| ≤ 0.8:** 8/8
- **Ablacja całej Kroniki (`L4_NO_TIME_DECK`):** Δ4P -8.3 (STABILIZER)
- **Mechaniki WEAK/NEUTRAL:** Limit Er: 12 → 6 (skrajna presja); Święte Oficjum: skazania 3 → 6; Werdykt Sądu: tajny (wyłączenie jawnej koordynacji)

---

## 1. 🗺️ Podsumowanie Ekosystemu Kart Kanonu 4P (Matryca Wpływu Kart, 60 kart)

Rozkład wszystkich 60 kart frakcyjnych w matrycy **Wpływ na Frakcję ($\Delta \text{Share}$)** vs **Wpływ na Kanon 4P ($\Delta \text{4P Score}$)**:

| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |
| :--- | :---: | :---: | :--- | :--- |
| 🩸 **Autopodatek (Self-Harm)** | **21** | 35.0% | Wyłączenie **podnosi** win share własnej frakcji — karta jest haraczem, nie silnikiem | **Rework / osłabienie kosztu, nie filar** |
| 💤 **Karta Pasywna (Dead Weight)** | **5** | 8.3% | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia lub wycięcia** |
| ⚠️ **Karta Destabilizująca (Disruptor)** | **6** | 10.0% | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |
| ⚖️ **Zbalansowane Narzędzie** | **13** | 21.7% | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Narzędzie, nie złoty środek całego kanonu** |
| 👑 / ⚓ **Filar / Kotwica Kanonu** | **15** | 25.0% | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |

---

## 2. 🃏 Warstwa I — Szczegółowa Analiza 60 Kart Frakcji w Kanonie 4P

### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)
Karty, których brak powoduje spadek wyniku Kanonu 4P o $\ge 4.0$ pkt lub załamanie winrate frakcji o $\ge 4.0\%$ — **bez** autopodatków (te są w 2.1b):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kb-09` **Dekret Królewski** | Korona & Borgiowie | 4zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 30.0% → **0.1%** | **`-29.9%`** | 66.0 → **27.8 pkt** (`-38.2`) |
| `kb-10` **Pieczęć Korony** | Korona & Borgiowie | 3zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 30.0% → **0.2%** | **`-29.8%`** | 66.0 → **28.5 pkt** (`-37.5`) |
| `caa-10` **Echo Alhambry** | Cienie Al-Andalus | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 21.2% → **4.2%** | **`-17.0%`** | 66.0 → **31.7 pkt** (`-34.3`) |
| `kt-03` **Zakazana Wiedza** | Kabała z Toledo | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.8% → **7.5%** | **`-17.3%`** | 66.0 → **32.5 pkt** (`-33.5`) |
| `kt-05` **Wskazówka Cyklu** | Kabała z Toledo | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.8% → **13.1%** | **`-11.7%`** | 66.0 → **45.3 pkt** (`-20.7`) |
| `caa-05` **Ukryty Kurier** | Cienie Al-Andalus | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 21.2% → **12.9%** | **`-8.3%`** | 66.0 → **48.8 pkt** (`-17.2`) |
| `kt-10` **Pieczęć Salomona** | Kabała z Toledo | 2zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 24.8% → **17.6%** | **`-7.2%`** | 66.0 → **56.4 pkt** (`-9.6`) |
| `caa-03` **Cień na Rynku** | Cienie Al-Andalus | 0zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 21.2% → **20.2%** | **`-1.0%`** | 66.0 → **56.9 pkt** (`-9.1`) |
| `caa-06` **Ucieczka z Lochów** | Cienie Al-Andalus | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 21.2% → **19.3%** | **`-1.9%`** | 66.0 → **61.0 pkt** (`-5.0`) |
| `gc-06` **Szantaż** | Gildia Cieni | 2zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.3% → **22.0%** | **`-2.3%`** | 66.0 → **61.5 pkt** (`-4.5`) |
| `gc-09` **Lista Dłużników** | Gildia Cieni | 3zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.3% → **22.2%** | **`-2.1%`** | 66.0 → **62.5 pkt** (`-3.5`) |
| `caa-02` **Złoto z Kryjówki** | Cienie Al-Andalus | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 21.2% → **23.0%** | **`+1.8%`** | 66.0 → **63.0 pkt** (`-3.0`) |
| `so-05` **Wezwanie do Trybunału** | Święte Oficjum | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.6% → **22.5%** | **`-2.1%`** | 66.0 → **63.1 pkt** (`-2.9`) |
| `caa-09` **Kurier Relikwii** | Cienie Al-Andalus | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 21.2% → **22.3%** | **`+1.1%`** | 66.0 → **64.0 pkt** (`-2.0`) |
| `kb-02` **Pobór Podatków** | Korona & Borgiowie | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 30.0% → **27.4%** | **`-2.6%`** | 66.0 → **65.8 pkt** (`-0.2`) |

### 2.1b. 🩸 Autopodatek Frakcji (Self-Harm)
Karty, których wyłączenie **podnosi** win share własnej frakcji. Gracz zauważy je jako haracz, nawet gdy stół 4P jest równy dzięki temu haraczowi.

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kb-04` **Faworyt Dworu** | Korona & Borgiowie | 2zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 30.0% → **45.1%** | **`+15.1%`** | 66.0 → **44.7 pkt** (`-21.3`) |
| `caa-04` **Fałszywy Trop** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 21.2% → **35.4%** | **`+14.2%`** | 66.0 → **54.4 pkt** (`-11.6`) |
| `caa-11` **Nocna Zmiana Warty** | Cienie Al-Andalus | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 21.2% → **35.0%** | **`+13.8%`** | 66.0 → **54.7 pkt** (`-11.3`) |
| `caa-01` **Przejście Podziemiami** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 21.2% → **34.7%** | **`+13.5%`** | 66.0 → **55.7 pkt** (`-10.3`) |
| `caa-07` **Szantaż Bractwa** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 21.2% → **34.6%** | **`+13.4%`** | 66.0 → **55.6 pkt** (`-10.4`) |
| `caa-08` **Kaptur Nocy** | Cienie Al-Andalus | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 21.2% → **34.4%** | **`+13.2%`** | 66.0 → **56.4 pkt** (`-9.6`) |
| `kb-07` **Szantaż Pieczęcią** | Korona & Borgiowie | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 30.0% → **35.8%** | **`+5.8%`** | 66.0 → **57.6 pkt** (`-8.4`) |
| `kb-08` **Przekupstwo Sędziego** | Korona & Borgiowie | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 30.0% → **35.8%** | **`+5.8%`** | 66.0 → **57.6 pkt** (`-8.4`) |
| `kt-01` **Rytuał Przejścia** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.8% → **29.6%** | **`+4.8%`** | 66.0 → **60.4 pkt** (`-5.6`) |
| `kt-02` **Transmutacja Złota** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.8% → **29.6%** | **`+4.8%`** | 66.0 → **60.4 pkt** (`-5.6`) |
| `kt-04` **Zwierciadło Herezji** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.8% → **29.3%** | **`+4.5%`** | 66.0 → **60.9 pkt** (`-5.1`) |
| `kt-07` **Archiwum Ukryte** | Kabała z Toledo | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.8% → **29.2%** | **`+4.4%`** | 66.0 → **59.4 pkt** (`-6.6`) |
| `kt-08` **Areszt Wiedzy** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.8% → **29.2%** | **`+4.4%`** | 66.0 → **59.4 pkt** (`-6.6`) |
| `kt-09` **Fragment Kodeksu** | Kabała z Toledo | 2zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.8% → **29.2%** | **`+4.4%`** | 66.0 → **59.2 pkt** (`-6.8`) |
| `kb-05` **List Żelazny** | Korona & Borgiowie | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 30.0% → **34.2%** | **`+4.2%`** | 66.0 → **60.6 pkt** (`-5.4`) |
| `kt-11` **Medytacja Sefirot** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.8% → **28.9%** | **`+4.1%`** | 66.0 → **59.5 pkt** (`-6.5`) |
| `kt-12` **Strażnik Archiwum** | Kabała z Toledo | 0zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.8% → **28.8%** | **`+4.0%`** | 66.0 → **59.6 pkt** (`-6.4`) |
| `kb-12` **Szantaż Salonowy** | Korona & Borgiowie | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 30.0% → **33.6%** | **`+3.6%`** | 66.0 → **62.0 pkt** (`-4.0`) |
| `gc-02` **Czarny Rynek** | Gildia Cieni | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.3% → **27.8%** | **`+3.5%`** | 66.0 → **60.5 pkt** (`-5.5`) |
| `gc-04` **Informator** | Gildia Cieni | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.3% → **27.7%** | **`+3.4%`** | 66.0 → **60.8 pkt** (`-5.2`) |
| `caa-12` **Skrytka w Murach** | Cienie Al-Andalus | 0zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 21.2% → **23.3%** | **`+2.1%`** | 66.0 → **64.0 pkt** (`-2.0`) |

### 2.2. ⚠️ Karty Destabilizujące Kanon 4P (Disruptors)
Karty, których wyłączenie podnosi 4P Score ($\Delta \text{4P} \ge +1.5$ pkt):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kb-11` **Tajny Emisariusz** | Korona & Borgiowie | 1zł / 0☣ | ⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor) | 30.0% → **29.2%** | `-0.8%` | 66.0 → **70.5 pkt** (`+4.5`) |
| `kb-03` **Plotka Dworska** | Korona & Borgiowie | 1zł / 1☣ | ⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor) | 30.0% → **29.4%** | `-0.6%` | 66.0 → **69.4 pkt** (`+3.4`) |
| `kb-06` **Areszt Królewski** | Korona & Borgiowie | 1zł / 0☣ | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) | 30.0% → **28.9%** | `-1.1%` | 66.0 → **69.2 pkt** (`+3.2`) |
| `kb-01` **Rozkaz Dworu** | Korona & Borgiowie | 1zł / 1☣ | ⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor) | 30.0% → **29.4%** | `-0.6%` | 66.0 → **68.9 pkt** (`+2.9`) |
| `gc-01` **Przekupiony Strażnik** | Gildia Cieni | 1zł / 1☣ | ⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor) | 24.3% → **24.4%** | `+0.1%` | 66.0 → **67.3 pkt** (`+1.3`) |
| `kt-06` **Przesłuchanie Imienia** | Kabała z Toledo | 2zł / 0☣ | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) | 24.8% → **22.8%** | `-2.0%` | 66.0 → **67.2 pkt** (`+1.2`) |

### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich 60 Kart Frakcji w Kanonie 4P

| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Faction Win Share 4P | $\Delta$ Frakcji | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `caa-01` | **Przejście Podziemiami** | Cienie Al-Andalus | 0 | 0 | 21.2% → 34.7% | `+13.5%` | 55.7 | `-10.3` | 5.86 | 1.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-02` | **Złoto z Kryjówki** | Cienie Al-Andalus | 0 | 0 | 21.2% → 23.0% | `+1.8%` | 63.0 | `-3.0` | 6.12 | 2.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-03` | **Cień na Rynku** | Cienie Al-Andalus | 0 | 1 | 21.2% → 20.2% | `-1.0%` | 56.9 | `-9.1` | 6.44 | 2.5% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-04` | **Fałszywy Trop** | Cienie Al-Andalus | 0 | 0 | 21.2% → 35.4% | `+14.2%` | 54.4 | `-11.6` | 5.87 | 1.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-05` | **Ukryty Kurier** | Cienie Al-Andalus | 0 | 0 | 21.2% → 12.9% | `-8.3%` | 48.8 | `-17.2` | 6.33 | 2.0% | 👑 FILAR KANONU (Core Keystone) |
| `caa-12` | **Skrytka w Murach** | Cienie Al-Andalus | 0 | 1 | 21.2% → 23.3% | `+2.1%` | 64.0 | `-2.0` | 6.18 | 2.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-06` | **Ucieczka z Lochów** | Cienie Al-Andalus | 0 | 0 | 21.2% → 19.3% | `-1.9%` | 61.0 | `-5.0` | 6.02 | 1.9% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-07` | **Szantaż Bractwa** | Cienie Al-Andalus | 0 | 0 | 21.2% → 34.6% | `+13.4%` | 55.6 | `-10.4` | 5.87 | 1.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-08` | **Kaptur Nocy** | Cienie Al-Andalus | 1 | 0 | 21.2% → 34.4% | `+13.2%` | 56.4 | `-9.6` | 5.88 | 1.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-11` | **Nocna Zmiana Warty** | Cienie Al-Andalus | 1 | 0 | 21.2% → 35.0% | `+13.8%` | 54.7 | `-11.3` | 5.85 | 1.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-09` | **Kurier Relikwii** | Cienie Al-Andalus | 0 | 0 | 21.2% → 22.3% | `+1.1%` | 64.0 | `-2.0` | 6.13 | 2.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-10` | **Echo Alhambry** | Cienie Al-Andalus | 0 | 0 | 21.2% → 4.2% | `-17.0%` | 31.7 | `-34.3` | 6.58 | 2.3% | 👑 FILAR KANONU (Core Keystone) |
| `gc-05` | **Fałszywy Świadek** | Gildia Cieni | 0 | 0 | 24.3% → 23.6% | `-0.7%` | 65.5 | `-0.5` | 6.11 | 1.7% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-12` | **Złodziejski Zwiad** | Gildia Cieni | 0 | 2 | 24.3% → 24.4% | `+0.1%` | 66.5 | `+0.5` | 6.09 | 1.5% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-01` | **Przekupiony Strażnik** | Gildia Cieni | 1 | 1 | 24.3% → 24.4% | `+0.1%` | 67.3 | `+1.3` | 6.10 | 1.7% | ⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor) |
| `gc-02` | **Czarny Rynek** | Gildia Cieni | 1 | 1 | 24.3% → 27.8% | `+3.5%` | 60.5 | `-5.5` | 6.17 | 1.9% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `gc-03` | **Podrzucenie Księgi** | Gildia Cieni | 1 | 0 | 24.3% → 24.5% | `+0.2%` | 66.6 | `+0.6` | 6.11 | 1.7% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-04` | **Informator** | Gildia Cieni | 1 | 1 | 24.3% → 27.7% | `+3.4%` | 60.8 | `-5.2` | 6.18 | 1.9% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `gc-11` | **Fałszywe Świadectwo Cechu** | Gildia Cieni | 1 | 0 | 24.3% → 24.5% | `+0.2%` | 66.4 | `+0.4` | 6.09 | 1.6% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `gc-06` | **Szantaż** | Gildia Cieni | 2 | 1 | 24.3% → 22.0% | `-2.3%` | 61.5 | `-4.5` | 6.29 | 2.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-07` | **Skrytobójstwo** | Gildia Cieni | 2 | 0 | 24.3% → 24.1% | `-0.2%` | 65.8 | `-0.2` | 6.11 | 1.7% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `gc-08` | **Zatrute Złoto** | Gildia Cieni | 2 | 0 | 24.3% → 24.1% | `-0.2%` | 65.8 | `-0.2` | 6.11 | 1.7% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `gc-09` | **Lista Dłużników** | Gildia Cieni | 3 | 1 | 24.3% → 22.2% | `-2.1%` | 62.5 | `-3.5` | 6.29 | 2.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-10` | **Upadek Domu** | Gildia Cieni | 4 | 2 | 24.3% → 24.4% | `+0.1%` | 66.4 | `+0.4` | 6.10 | 1.6% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `kb-01` | **Rozkaz Dworu** | Korona & Borgiowie | 1 | 1 | 30.0% → 29.4% | `-0.6%` | 68.9 | `+2.9` | 6.13 | 1.4% | ⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor) |
| `kb-02` | **Pobór Podatków** | Korona & Borgiowie | 1 | 0 | 30.0% → 27.4% | `-2.6%` | 65.8 | `-0.2` | 6.20 | 2.1% | 👑 FILAR KANONU (Core Keystone) |
| `kb-03` | **Plotka Dworska** | Korona & Borgiowie | 1 | 1 | 30.0% → 29.4% | `-0.6%` | 69.4 | `+3.4` | 6.12 | 1.4% | ⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor) |
| `kb-11` | **Tajny Emisariusz** | Korona & Borgiowie | 1 | 0 | 30.0% → 29.2% | `-0.8%` | 70.5 | `+4.5` | 6.13 | 1.3% | ⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor) |
| `kb-04` | **Faworyt Dworu** | Korona & Borgiowie | 2 | 1 | 30.0% → 45.1% | `+15.1%` | 44.7 | `-21.3` | 5.84 | 1.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-05` | **List Żelazny** | Korona & Borgiowie | 2 | 0 | 30.0% → 34.2% | `+4.2%` | 60.6 | `-5.4` | 5.99 | 1.8% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-06` | **Areszt Królewski** | Korona & Borgiowie | 1 | 0 | 30.0% → 28.9% | `-1.1%` | 69.2 | `+3.2` | 6.15 | 1.4% | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) |
| `kb-12` | **Szantaż Salonowy** | Korona & Borgiowie | 1 | 0 | 30.0% → 33.6% | `+3.6%` | 62.0 | `-4.0` | 6.11 | 1.9% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-07` | **Szantaż Pieczęcią** | Korona & Borgiowie | 2 | 0 | 30.0% → 35.8% | `+5.8%` | 57.6 | `-8.4` | 6.09 | 2.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-08` | **Przekupstwo Sędziego** | Korona & Borgiowie | 2 | 0 | 30.0% → 35.8% | `+5.8%` | 57.6 | `-8.4` | 6.09 | 2.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-10` | **Pieczęć Korony** | Korona & Borgiowie | 3 | 2 | 30.0% → 0.2% | `-29.8%` | 28.5 | `-37.5` | 6.52 | 2.3% | 👑 FILAR KANONU (Core Keystone) |
| `kb-09` | **Dekret Królewski** | Korona & Borgiowie | 4 | 1 | 30.0% → 0.1% | `-29.9%` | 27.8 | `-38.2` | 6.56 | 3.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-03` | **Zakazana Wiedza** | Kabała z Toledo | 0 | 0 | 24.8% → 7.5% | `-17.3%` | 32.5 | `-33.5` | 6.46 | 2.6% | 👑 FILAR KANONU (Core Keystone) |
| `kt-12` | **Strażnik Archiwum** | Kabała z Toledo | 0 | 1 | 24.8% → 28.8% | `+4.0%` | 59.6 | `-6.4` | 6.02 | 1.5% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-01` | **Rytuał Przejścia** | Kabała z Toledo | 1 | 0 | 24.8% → 29.6% | `+4.8%` | 60.4 | `-5.6` | 6.02 | 1.5% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-02` | **Transmutacja Złota** | Kabała z Toledo | 1 | 0 | 24.8% → 29.6% | `+4.8%` | 60.4 | `-5.6` | 6.02 | 1.5% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-04` | **Zwierciadło Herezji** | Kabała z Toledo | 1 | 0 | 24.8% → 29.3% | `+4.5%` | 60.9 | `-5.1` | 6.02 | 1.5% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-05` | **Wskazówka Cyklu** | Kabała z Toledo | 1 | 0 | 24.8% → 13.1% | `-11.7%` | 45.3 | `-20.7` | 6.34 | 2.5% | 👑 FILAR KANONU (Core Keystone) |
| `kt-07` | **Archiwum Ukryte** | Kabała z Toledo | 1 | 1 | 24.8% → 29.2% | `+4.4%` | 59.4 | `-6.6` | 6.03 | 1.6% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-08` | **Areszt Wiedzy** | Kabała z Toledo | 1 | 0 | 24.8% → 29.2% | `+4.4%` | 59.4 | `-6.6` | 6.03 | 1.6% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-11` | **Medytacja Sefirot** | Kabała z Toledo | 1 | 0 | 24.8% → 28.9% | `+4.1%` | 59.5 | `-6.5` | 6.02 | 1.5% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-06` | **Przesłuchanie Imienia** | Kabała z Toledo | 2 | 0 | 24.8% → 22.8% | `-2.0%` | 67.2 | `+1.2` | 6.16 | 1.9% | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) |
| `kt-09` | **Fragment Kodeksu** | Kabała z Toledo | 2 | 1 | 24.8% → 29.2% | `+4.4%` | 59.2 | `-6.8` | 6.03 | 1.6% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-10` | **Pieczęć Salomona** | Kabała z Toledo | 2 | 2 | 24.8% → 17.6% | `-7.2%` | 56.4 | `-9.6` | 6.30 | 2.9% | 👑 FILAR KANONU (Core Keystone) |
| `so-05` | **Wezwanie do Trybunału** | Święte Oficjum | 0 | 0 | 24.6% → 22.5% | `-2.1%` | 63.1 | `-2.9` | 6.16 | 1.9% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-01` | **Patrol Familiariuszy** | Święte Oficjum | 1 | 0 | 24.6% → 25.7% | `+1.1%` | 65.3 | `-0.7` | 6.15 | 1.9% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `so-02` | **Skarbiec Trybunału** | Święte Oficjum | 1 | 0 | 24.6% → 23.3% | `-1.3%` | 64.7 | `-1.3` | 6.24 | 2.4% | ⚡ MOTOR FRAKCJI (Offensive Engine) |
| `so-04` | **Publiczne Ostrzeżenie** | Święte Oficjum | 1 | 0 | 24.6% → 25.7% | `+1.1%` | 65.1 | `-0.9` | 6.13 | 1.8% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `so-12` | **Straż Trybunalska** | Święte Oficjum | 1 | 0 | 24.6% → 25.6% | `+1.0%` | 65.6 | `-0.4` | 6.12 | 1.7% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `so-03` | **Podejrzenie** | Święte Oficjum | 2 | 0 | 24.6% → 25.7% | `+1.1%` | 65.1 | `-0.9` | 6.13 | 1.8% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `so-08` | **Nasłanie Inkwizytora** | Święte Oficjum | 0 | 0 | 24.6% → 24.8% | `+0.2%` | 65.9 | `-0.1` | 6.13 | 1.7% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `so-11` | **Dekret Czystości Wiary** | Święte Oficjum | 1 | 0 | 24.6% → 25.4% | `+0.8%` | 65.0 | `-1.0` | 6.13 | 1.7% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-06` | **Areszt Trybunalski** | Święte Oficjum | 2 | 0 | 24.6% → 25.4% | `+0.8%` | 65.4 | `-0.6` | 6.12 | 1.6% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-07` | **Przesłuchanie Oficjum** | Święte Oficjum | 2 | 0 | 24.6% → 25.4% | `+0.8%` | 65.4 | `-0.6` | 6.12 | 1.6% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-09` | **Świadek Koronny** | Święte Oficjum | 2 | 0 | 24.6% → 25.5% | `+0.9%` | 65.5 | `-0.5` | 6.13 | 1.8% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-10` | **Oczyść Miasto** | Święte Oficjum | 5 | 2 | 24.6% → 25.3% | `+0.7%` | 66.3 | `+0.3` | 6.14 | 1.8% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |

---

## 3. ⏳ Warstwa II — Kronika Dziejów w 4P (Ablacja 8 Kart Wydarzeń Czasu)

Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans w 4P:

| ID | Karta Wydarzenia | 4P Score | $\Delta$ 4P | Średnia Er | Deadlock % | Status Roli w Kronice |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `tc-01` | **Kres Średniowiecza** | 🟠 ** 66.0** | `0.0 pkt` | 6.13 Er | 1.7% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-02` | **Płonący Stos** | 🟠 ** 66.0** | `0.0 pkt` | 6.13 Er | 1.7% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-03` | **Królewski Podatek** | 🟠 ** 66.0** | `0.0 pkt` | 6.13 Er | 1.7% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-04` | **Spisek w Cieniu** | 🟠 ** 66.0** | `0.0 pkt` | 6.13 Er | 1.7% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-05` | **Złoty Wiek** | 🟠 ** 66.0** | `0.0 pkt` | 6.13 Er | 1.7% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-06` | **Czystka w Mieście** | 🟠 ** 66.0** | `0.0 pkt` | 6.13 Er | 1.7% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-07` | **Druga Szansa** | 🟠 ** 66.0** | `0.0 pkt` | 6.13 Er | 1.7% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-08` | **Zaćmienie Słońca** | 🟠 ** 66.0** | `0.0 pkt` | 6.13 Er | 1.7% | 💤 Martwa karta kroniki (Δ≈0) |

---

## 4. ⚙️ Warstwa III — Matryca 9 Obszarów Wpływu Mechanik Gry (L1, L2, L4)

Mechaniki w tym raporcie: **skraj albo wyłączenie**. Testy ±1 są w `audit_level1` / `audit_level2` / `audit_level4`. **Δ≈0 nie jest harmonią.**

| Kategoria Mechaniki | Liczba Testów | Rola w Ekosystemie Kanonu 4P | Rekomendacja Balansowa |
| :--- | :---: | :--- | :--- |
| 👑 / 🛡️ **Filary i Bezpieczniki** | **23** | Ablacja wali w stół — gracze czują tę gałkę | **Cel kanonu** |
| ⚠️ **Za słabe dźwignie** | **3** | Rusza share, nie trzyma stołu — nie jest „zbalansowana” | **Wzmocnić aż będzie filarem** |
| 💤 **Martwe / uśpione ścieżki** | **0** | Dual-win z witalności albo ablacja Δ≈0 | Wada pomiaru, nie harmonia |
| ⚠️ / 💡 **Wady bieżącej wartości** | **0** | Inna wartość gałki **podnosi** 4P — obecny setting szkodzi | **Przekręcić albo rework** |

### 4.0. ⚠️ Problematyczne mechaniki (osobny wykaz)
Wszystkie mechaniki z grup **DEAD**, **WEAK/NEUTRAL** i **DISRUPTOR**: ścieżki dual-win z `evaluate_vitality`, testy z $|\Delta\text{4P}| \le 0.8$ i ruchem share $\le 1.5$ pp (DEAD), za słabe dźwignie (WEAK) oraz wady bieżącej wartości (DISRUPTOR).

| Badany Podsystem | Kategoria | 4P Score | $\Delta$ 4P | Klasyfikacja |
| :--- | :--- | :---: | :---: | :--- |
| **Werdykt Sądu: tajny (wyłączenie jawnej koordynacji)** | Poziom 4: Warianty i Modyfikatory | 66.0 → 🟠 ** 65.8** (`-0.2`) | `-0.2 pkt` | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |
| **Święte Oficjum: skazania 3 → 6** | Poziom 2: Warunki Zwycięstwa | 66.0 → 🟠 ** 63.7** (`-2.3`) | `-2.3 pkt` | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |
| **Limit Er: 12 → 6 (skrajna presja)** | Poziom 1: System Core | 66.0 → 🟠 ** 63.3** (`-2.7`) | `-2.7 pkt` | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |

### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)

| Badany Podsystem / Modyfikator L1 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Limit Er: 12 → 6 (skrajna presja)** | 66.0 → 🟠 ** 63.3** (`-2.7`) | `-2.7 pkt` | 5.43 Er | 68.4% | 1.6% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |
| **Próg Oskarżenia: 7 → 1** | 66.0 → 🔴 **  2.5** (`-63.5`) | `-63.5 pkt` | 5.42 Er | 0.0% | 0.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Oskarżenia: 7 → 14** | 66.0 → 🔴 ** 22.6** (`-43.4`) | `-43.4 pkt` | 6.09 Er | 1.7% | 1.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 0zł (wyłączenie)** | 66.0 → 🔴 ** 45.7** (`-20.3`) | `-20.3 pkt` | 6.42 Er | 2.0% | 6.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 8zł** | 66.0 → 🔴 ** 51.7** (`-14.3`) | `-14.3 pkt` | 5.86 Er | 1.3% | 0.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 1** | 66.0 → 🔴 ** 19.2** (`-46.8`) | `-46.8 pkt` | 8.41 Er | 29.6% | 1.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 6** | 66.0 → 🔴 ** 10.9** (`-55.1`) | `-55.1 pkt` | 4.47 Er | 0.0% | 1.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 1** | 66.0 → 🔴 **  1.6** (`-64.4`) | `-64.4 pkt` | 8.79 Er | 12.5% | 10.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 10** | 66.0 → 🔴 **  7.1** (`-58.9`) | `-58.9 pkt` | 4.58 Er | 0.0% | 2.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: cooldown 3 → 0 (co erę)** | 66.0 → 🔴 ** 13.7** (`-52.3`) | `-52.3 pkt` | 5.08 Er | 0.7% | 1.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: całkowite wyłączenie** | 66.0 → 🔴 ** 23.7** (`-42.3`) | `-42.3 pkt` | 8.61 Er | 46.8% | 0.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)

| Badany Warunek Zwycięstwa L2 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: stosy 6 → 1** | 66.0 → 🔴 ** 10.7** (`-55.3`) | `-55.3 pkt` | 3.79 Er | 0.1% | 1.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: stosy 6 → 12** | 66.0 → 🔴 ** 45.1** (`-20.9`) | `-20.9 pkt` | 6.37 Er | 4.7% | 1.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 1** | 66.0 → 🔴 ** 10.9** (`-55.1`) | `-55.1 pkt` | 4.41 Er | 0.1% | 1.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 6** | 66.0 → 🟠 ** 63.7** (`-2.3`) | `-2.3 pkt` | 6.15 Er | 1.8% | 1.4% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |
| **Cienie: relikwie 2 → 4** | 66.0 → 🔴 ** 25.6** (`-40.4`) | `-40.4 pkt` | 6.57 Er | 2.2% | 1.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: dekrety 2 → 4** | 66.0 → 🔴 ** 28.0** (`-38.0`) | `-38.0 pkt` | 6.51 Er | 2.5% | 1.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: fragmenty 2 → 4** | 66.0 → 🔴 ** 26.3** (`-39.7`) | `-39.7 pkt` | 6.36 Er | 2.0% | 1.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: era 6 → 1** | 66.0 → 🔴 ** 29.7** (`-36.3`) | `-36.3 pkt` | 4.73 Er | 1.7% | 1.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: era 6 → 12** | 66.0 → 🔴 ** 25.5** (`-40.5`) | `-40.5 pkt` | 6.37 Er | 2.0% | 1.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 8 → 1** | 66.0 → 🔴 ** 15.2** (`-50.8`) | `-50.8 pkt` | 3.32 Er | 1.1% | 1.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 8 → 16** | 66.0 → 🔴 ** 34.6** (`-31.4`) | `-31.4 pkt` | 6.51 Er | 5.8% | 1.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)

| Badany Wariant / Modyfikator L4 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kronika Dziejów: całkowite wyłączenie** | 66.0 → 🔴 ** 57.7** (`-8.3`) | `-8.3 pkt` | 6.22 Er | 2.1% | 1.8% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Werdykt Sądu: tajny (wyłączenie jawnej koordynacji)** | 66.0 → 🟠 ** 65.8** (`-0.2`) | `-0.2 pkt` | 6.06 Er | 1.3% | 1.5% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |
| **Inkwizytor Patrol: ruch 1 → 0 (wyłączenie)** | 66.0 → 🔴 ** 18.3** (`-47.7`) | `-47.7 pkt` | 8.71 Er | 47.4% | 0.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Szlak Morski: era 4 → nigdy (99)** | 66.0 → 🟠 ** 61.4** (`-4.6`) | `-4.6 pkt` | 6.18 Er | 1.8% | 1.4% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |

---

## 5. 👥 Warstwa IV — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych. Kolumna win share to HUD kanonu; setup+witalność to stary blend (kara martwej ścieżki).

| Nieobecna Frakcja | Setup Testowy | Win share | Setup+witalność | Diagnoza |
| :--- | :--- | :---: | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`74.7`** | `71.2` | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`60.3`** | `60.3` | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`84.7`** | `84.7` | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`58.6`** | `58.6` | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`51.9`** | `51.9` | Brak presji stosów i bezpośredniego Inkwizytora |