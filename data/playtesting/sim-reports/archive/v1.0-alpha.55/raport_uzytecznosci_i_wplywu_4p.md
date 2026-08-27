[Strona główna](../../../../../README.md) > [v1.0-alpha.55](README.md) > [raport_uzytecznosci_i_wplywu_4p](raport_uzytecznosci_i_wplywu_4p.md)

---

# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v1.0-alpha.55

**Wersja Gry:** `v1.0-alpha.55` | **Data Badania:** 2026-08-23 18:05 | **Próba:** 5000 gier/setup (25000 gier na wariant) | **Ziarno:** 42
**4P Score (win share):** 🟠 ** 68.0** pkt | **Witalność (osobna kara):** `0.533` | **Śr. Er:** `5.59` | **Deadlocki:** `0.0%` | **Pas Biedy:** `4.9%`
**Udziały 4P:** CAA 20.3% · GC 21.1% · KB 28.8% · KT 24.7% · SO 30.1%

Klasyfikacja L1/L2/L4 i Δ 4P liczą wyłącznie równość win share (`calculate_balance_score`). Kara witalności jest osobno.

**Ostrzeżenia witalności (nie w 4P Score):**
- 4p-core: Przedwczesne Zwycięstwa (Era 1-2): 0.6% gier (>0.5%)
- 4p-core: Ekstremalny Deadlock (Era 11+): 0.6% gier (>0.5%)
- 4p-no-kabala: Przedwczesne Zwycięstwa (Era 1-2): 1.0% gier (>0.5%)
- 4p-no-korona: Przedwczesne Zwycięstwa (Era 1-2): 1.0% gier (>0.5%)
- 4p-no-korona: Nadmiar Wczesnych Zakończeń (Era 3-4): 27.8% gier (>25.0%)
- 4p-no-oficjum: Przedwczesne Zwycięstwa (Era 1-2): 0.8% gier (>0.5%)

---

## 0. Wady z tej próby (nie HUD win share)

Kubełki klasyfikatora i ostrzeżenia witalności z bieżącego runu.

- **Share |Δ| ≥ 2.5 pp od 25%:** CAA 20.3%, GC 21.1%, KB 28.8%, SO 30.1%
- **Autopodatek (SELF_HARM):** 2/60
- **SELF_HARM z Δ4P ≥ 1.2:** `caa-01` Δ4P +4.5, `caa-02` Δ4P +4.4
- **DEAD_WEIGHT:** `gc-10` Upadek Domu
- **Karty Kroniki |Δ4P| ≤ 0.8:** 1/10
- **Ablacja całej Kroniki (`L4_NO_TIME_DECK`):** Δ4P -9.5 (STABILIZER)
- **Mechaniki WEAK/NEUTRAL:** Autodafé: całkowite wyłączenie; Kabała: fragmenty 3 → 1; Kronika Dziejów: co 3 Ery (spowolniony zegar); Szlak Morski: era 4 → nigdy (99)
- **Mechaniki DEAD:** Inkwizytor Patrol: ruch x2 (podwojona prędkość)
- **Mechaniki DISRUPTOR:** Limit Er: 14 → 7 (skrajna presja); Święte Oficjum: stosy 7 → 14

---

## 1. 🗺️ Podsumowanie Ekosystemu Kart Kanonu 4P (Matryca Wpływu Kart, 60 kart)

Rozkład wszystkich 60 kart frakcyjnych w matrycy **Wpływ na Frakcję ($\Delta \text{Share}$)** vs **Wpływ na Kanon 4P ($\Delta \text{4P Score}$)**:

| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |
| :--- | :---: | :---: | :--- | :--- |
| 🩸 **Autopodatek (Self-Harm)** | **2** | 3.3% | Wyłączenie **podnosi** win share własnej frakcji — karta jest haraczem, nie silnikiem | **Rework / osłabienie kosztu, nie filar** |
| 🔄 **Rozcieńczalnik Talii (Tempo Filler)** | **7** | 11.7% | Normalna karta tempa — ablacja fałszywie flaguje ją jako autopodatek z powodu odchudzenia talii | **Normalny element deckbuildingu** |
| 💤 **Karta Pasywna (Dead Weight)** | **1** | 1.7% | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia lub wycięcia** |
| ⚠️ **Karta Destabilizująca (Disruptor)** | **8** | 13.3% | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |
| ⚖️ **Zbalansowane Narzędzie** | **29** | 48.3% | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Narzędzie, nie złoty środek całego kanonu** |
| 👑 / ⚓ **Filar / Kotwica Kanonu** | **13** | 21.7% | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |

---

## 2. 🃏 Warstwa I — Szczegółowa Analiza 60 Kart Frakcji w Kanonie 4P

### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)
Karty, których brak powoduje spadek wyniku Kanonu 4P o $\ge 4.0$ pkt lub załamanie winrate frakcji o $\ge 4.0\%$ — **bez** autopodatków (te są w 2.1b):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kb-09` **Dekret Królewski** | Korona & Borgiowie | 4zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 28.8% → **0.0%** | **`-28.8%`** | 68.0 → **26.6 pkt** (`-41.4`) |
| `kt-10` **Pieczęć Salomona** | Kabała z Toledo | 5zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 24.7% → **0.0%** | **`-24.7%`** | 68.0 → **27.1 pkt** (`-40.9`) |
| `caa-10` **Echo Alhambry** | Cienie Al-Andalus | 3zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 20.3% → **1.6%** | **`-18.7%`** | 68.0 → **29.2 pkt** (`-38.8`) |
| `kt-02` **Transmutacja Złota** | Kabała z Toledo | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.7% → **2.4%** | **`-22.3%`** | 68.0 → **29.6 pkt** (`-38.4`) |
| `kt-03` **Zakazana Wiedza** | Kabała z Toledo | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 24.7% → **12.5%** | **`-12.2%`** | 68.0 → **46.1 pkt** (`-21.9`) |
| `caa-05` **Ukryty Kurier** | Cienie Al-Andalus | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 20.3% → **12.7%** | **`-7.6%`** | 68.0 → **49.9 pkt** (`-18.1`) |
| `gc-09` **Lista Dłużników** | Gildia Cieni | 3zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 21.1% → **15.5%** | **`-5.6%`** | 68.0 → **55.7 pkt** (`-12.3`) |
| `kb-02` **Pobór Podatków** | Korona & Borgiowie | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 28.8% → **15.8%** | **`-13.0%`** | 68.0 → **56.8 pkt** (`-11.2`) |
| `caa-06` **Ucieczka z Lochów** | Cienie Al-Andalus | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 20.3% → **18.5%** | **`-1.8%`** | 68.0 → **62.7 pkt** (`-5.3`) |
| `kb-10` **Pieczęć Korony** | Korona & Borgiowie | 3zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 28.8% → **18.7%** | **`-10.1%`** | 68.0 → **63.0 pkt** (`-5.0`) |
| `gc-06` **Szantaż** | Gildia Cieni | 2zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 21.1% → **18.5%** | **`-2.6%`** | 68.0 → **63.1 pkt** (`-4.9`) |
| `so-10` **Oczyść Miasto** | Święte Oficjum | 5zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 30.1% → **28.9%** | **`-1.2%`** | 68.0 → **65.4 pkt** (`-2.6`) |
| `so-12` **Straż Trybunalska** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 30.1% → **31.4%** | **`+1.3%`** | 68.0 → **65.7 pkt** (`-2.3`) |

### 2.1b. 🩸 Autopodatek Frakcji (Self-Harm)
Karty, których wyłączenie **podnosi** win share własnej frakcji. Gracz zauważy je jako haracz, nawet gdy stół 4P jest równy dzięki temu haraczowi.

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `caa-01` **Przejście Podziemiami** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 20.3% → **23.2%** | **`+2.9%`** | 68.0 → **72.5 pkt** (`4.5`) |
| `caa-02` **Złoto z Kryjówki** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 20.3% → **23.2%** | **`+2.9%`** | 68.0 → **72.4 pkt** (`4.4`) |

### 2.2. ⚠️ Karty Destabilizujące Kanon 4P (Disruptors)
Karty, których wyłączenie podnosi 4P Score ($\Delta \text{4P} \ge +1.5$ pkt):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `so-02` **Skarbiec Trybunału** | Święte Oficjum | 1zł / 0☣ | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) | 30.1% → **26.8%** | `-3.3%` | 68.0 → **72.8 pkt** (`+4.8`) |
| `gc-08` **Zatrute Złoto** | Gildia Cieni | 1zł / 1☣ | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) | 21.1% → **22.7%** | `+1.6%` | 68.0 → **72.2 pkt** (`+4.2`) |
| `gc-07` **Skrytobójstwo** | Gildia Cieni | 0zł / 0☣ | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) | 21.1% → **23.0%** | `+1.9%` | 68.0 → **70.7 pkt** (`+2.7`) |
| `gc-11` **Fałszywe Świadectwo Cechu** | Gildia Cieni | 0zł / 2☣ | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) | 21.1% → **22.8%** | `+1.7%` | 68.0 → **70.5 pkt** (`+2.5`) |
| `so-05` **Wezwanie do Trybunału** | Święte Oficjum | 0zł / 0☣ | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) | 30.1% → **27.2%** | `-2.9%` | 68.0 → **70.0 pkt** (`+2.0`) |
| `so-03` **Podejrzenie** | Święte Oficjum | 2zł / 2☣ | ⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor) | 30.1% → **30.6%** | `+0.5%` | 68.0 → **69.8 pkt** (`+1.8`) |
| `gc-04` **Informator** | Gildia Cieni | 1zł / 0☣ | ⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor) | 21.1% → **21.3%** | `+0.2%` | 68.0 → **69.7 pkt** (`+1.7`) |
| `gc-12` **Złodziejski Zwiad** | Gildia Cieni | 0zł / 2☣ | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) | 21.1% → **22.9%** | `+1.8%` | 68.0 → **69.6 pkt** (`+1.6`) |

### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich 60 Kart Frakcji w Kanonie 4P

| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Play-Rate | Faction Win Share 4P | $\Delta$ Frakcji | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `caa-01` | **Przejście Podziemiami** | Cienie Al-Andalus | 0 | 0 | 0.08 | 20.3% → 23.2% | `+2.9%` | 72.5 | `+4.5` | 5.53 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-02` | **Złoto z Kryjówki** | Cienie Al-Andalus | 0 | 0 | 0.00 | 20.3% → 23.2% | `+2.9%` | 72.4 | `+4.4` | 5.53 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-03` | **Cień na Rynku** | Cienie Al-Andalus | 0 | 1 | 0.97 | 20.3% → 27.7% | `+7.4%` | 76.4 | `+8.4` | 5.61 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-04` | **Fałszywy Trop** | Cienie Al-Andalus | 0 | 0 | 1.02 | 20.3% → 24.7% | `+4.4%` | 75.6 | `+7.6` | 5.53 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-12` | **Skrytka w Murach** | Cienie Al-Andalus | 0 | 0 | 1.07 | 20.3% → 26.2% | `+5.9%` | 75.7 | `+7.7` | 5.48 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-05` | **Ukryty Kurier** | Cienie Al-Andalus | 1 | 0 | 1.03 | 20.3% → 12.7% | `-7.6%` | 49.9 | `-18.1` | 5.72 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `caa-06` | **Ucieczka z Lochów** | Cienie Al-Andalus | 0 | 0 | 0.91 | 20.3% → 18.5% | `-1.8%` | 62.7 | `-5.3` | 5.56 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-07` | **Szantaż Bractwa** | Cienie Al-Andalus | 0 | 0 | 0.40 | 20.3% → 24.0% | `+3.7%` | 75.0 | `+7.0` | 5.53 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `caa-08` | **Kaptur Nocy** | Cienie Al-Andalus | 1 | 0 | 0.85 | 20.3% → 24.6% | `+4.3%` | 73.2 | `+5.2` | 5.53 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-11` | **Nocna Zmiana Warty** | Cienie Al-Andalus | 1 | 0 | 0.88 | 20.3% → 24.2% | `+3.9%` | 72.9 | `+4.9` | 5.53 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-09` | **Kurier Relikwii** | Cienie Al-Andalus | 0 | 0 | 0.83 | 20.3% → 24.8% | `+4.5%` | 74.0 | `+6.0` | 5.51 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-10` | **Echo Alhambry** | Cienie Al-Andalus | 3 | 0 | 0.97 | 20.3% → 1.6% | `-18.7%` | 29.2 | `-38.8` | 5.90 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `gc-02` | **Czarny Rynek** | Gildia Cieni | 0 | 0 | 0.84 | 21.1% → 21.0% | `-0.1%` | 67.0 | `-1.0` | 5.55 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-05` | **Fałszywy Świadek** | Gildia Cieni | 0 | 0 | 0.62 | 21.1% → 21.0% | `-0.1%` | 66.9 | `-1.1` | 5.58 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-12` | **Złodziejski Zwiad** | Gildia Cieni | 0 | 2 | 0.51 | 21.1% → 22.9% | `+1.8%` | 69.6 | `+1.6` | 5.56 | 0.0% | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) |
| `gc-01` | **Przekupiony Strażnik** | Gildia Cieni | 1 | 1 | 0.38 | 21.1% → 21.6% | `+0.5%` | 68.9 | `+0.9` | 5.57 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-03` | **Podrzucenie Księgi** | Gildia Cieni | 1 | 0 | 0.83 | 21.1% → 21.2% | `+0.1%` | 67.6 | `-0.4` | 5.55 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-04` | **Informator** | Gildia Cieni | 1 | 0 | 1.08 | 21.1% → 21.3% | `+0.2%` | 69.7 | `+1.7` | 5.54 | 0.0% | ⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor) |
| `gc-07` | **Skrytobójstwo** | Gildia Cieni | 0 | 0 | 1.05 | 21.1% → 23.0% | `+1.9%` | 70.7 | `+2.7` | 5.64 | 0.0% | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) |
| `gc-11` | **Fałszywe Świadectwo Cechu** | Gildia Cieni | 0 | 2 | 0.32 | 21.1% → 22.8% | `+1.7%` | 70.5 | `+2.5` | 5.59 | 0.0% | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) |
| `gc-08` | **Zatrute Złoto** | Gildia Cieni | 1 | 1 | 0.94 | 21.1% → 22.7% | `+1.6%` | 72.2 | `+4.2` | 5.59 | 0.0% | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) |
| `gc-06` | **Szantaż** | Gildia Cieni | 2 | 1 | 0.86 | 21.1% → 18.5% | `-2.6%` | 63.1 | `-4.9` | 5.64 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `gc-09` | **Lista Dłużników** | Gildia Cieni | 3 | 0 | 1.09 | 21.1% → 15.5% | `-5.6%` | 55.7 | `-12.3` | 5.61 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `gc-10` | **Upadek Domu** | Gildia Cieni | 4 | 2 | 0.01 | 21.1% → 21.5% | `+0.4%` | 67.4 | `-0.6` | 5.57 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `kb-01` | **Rozkaz Dworu** | Korona & Borgiowie | 1 | 1 | 0.69 | 28.8% → 35.9% | `+7.1%` | 56.4 | `-11.6` | 5.53 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-02` | **Pobór Podatków** | Korona & Borgiowie | 1 | 0 | 0.77 | 28.8% → 15.8% | `-13.0%` | 56.8 | `-11.2` | 5.71 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-03` | **Plotka Dworska** | Korona & Borgiowie | 1 | 1 | 0.41 | 28.8% → 34.7% | `+5.9%` | 58.8 | `-9.2` | 5.55 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kb-11` | **Tajny Emisariusz** | Korona & Borgiowie | 1 | 0 | 0.82 | 28.8% → 34.2% | `+5.4%` | 56.8 | `-11.2` | 5.49 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-04` | **Faworyt Dworu** | Korona & Borgiowie | 2 | 0 | 0.77 | 28.8% → 35.3% | `+6.5%` | 54.4 | `-13.6` | 5.41 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-05` | **List Żelazny** | Korona & Borgiowie | 2 | 0 | 0.91 | 28.8% → 44.4% | `+15.6%` | 36.4 | `-31.6` | 5.24 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-12` | **Szantaż Salonowy** | Korona & Borgiowie | 1 | 0 | 0.84 | 28.8% → 30.9% | `+2.1%` | 63.5 | `-4.5` | 5.56 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-06` | **Areszt Królewski** | Korona & Borgiowie | 2 | 0 | 0.28 | 28.8% → 33.0% | `+4.2%` | 61.0 | `-7.0` | 5.56 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kb-07` | **Szantaż Pieczęcią** | Korona & Borgiowie | 2 | 0 | 0.72 | 28.8% → 33.2% | `+4.4%` | 58.8 | `-9.2` | 5.52 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-08` | **Przekupstwo Sędziego** | Korona & Borgiowie | 3 | 0 | 0.34 | 28.8% → 34.1% | `+5.3%` | 57.7 | `-10.3` | 5.53 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kb-10` | **Pieczęć Korony** | Korona & Borgiowie | 3 | 2 | 0.26 | 28.8% → 18.7% | `-10.1%` | 63.0 | `-5.0` | 5.83 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-09` | **Dekret Królewski** | Korona & Borgiowie | 4 | 0 | 0.48 | 28.8% → 0.0% | `-28.8%` | 26.6 | `-41.4` | 5.96 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-02` | **Transmutacja Złota** | Kabała z Toledo | 0 | 0 | 0.99 | 24.7% → 2.4% | `-22.3%` | 29.6 | `-38.4` | 5.90 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-03` | **Zakazana Wiedza** | Kabała z Toledo | 0 | 0 | 1.07 | 24.7% → 12.5% | `-12.2%` | 46.1 | `-21.9` | 5.74 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `kt-12` | **Strażnik Archiwum** | Kabała z Toledo | 0 | 1 | 0.23 | 24.7% → 28.9% | `+4.2%` | 65.1 | `-2.9` | 5.52 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kt-01` | **Rytuał Przejścia** | Kabała z Toledo | 1 | 0 | 0.34 | 24.7% → 28.6% | `+3.9%` | 65.2 | `-2.8` | 5.52 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kt-04` | **Zwierciadło Herezji** | Kabała z Toledo | 1 | 0 | 0.71 | 24.7% → 32.5% | `+7.8%` | 60.5 | `-7.5` | 5.49 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-05` | **Wskazówka Cyklu** | Kabała z Toledo | 1 | 1 | 1.00 | 24.7% → 25.1% | `+0.4%` | 66.2 | `-1.8` | 5.66 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-07` | **Archiwum Ukryte** | Kabała z Toledo | 1 | 1 | 0.26 | 24.7% → 28.9% | `+4.2%` | 65.9 | `-2.1` | 5.52 | 0.0% | 🔄 ROZCIEŃCZALNIK TALII (Tempo Filler) |
| `kt-08` | **Areszt Wiedzy** | Kabała z Toledo | 1 | 0 | 0.89 | 24.7% → 29.2% | `+4.5%` | 68.0 | `0.0` | 5.56 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-06` | **Przesłuchanie Imienia** | Kabała z Toledo | 2 | 0 | 1.09 | 24.7% → 35.4% | `+10.7%` | 51.2 | `-16.8` | 5.34 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-11` | **Medytacja Sefirot** | Kabała z Toledo | 2 | 0 | 0.81 | 24.7% → 28.7% | `+4.0%` | 64.5 | `-3.5` | 5.47 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-09` | **Fragment Kodeksu** | Kabała z Toledo | 2 | 1 | 0.86 | 24.7% → 28.6% | `+3.9%` | 64.5 | `-3.5` | 5.59 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-10` | **Pieczęć Salomona** | Kabała z Toledo | 5 | 2 | 0.35 | 24.7% → 0.0% | `-24.7%` | 27.1 | `-40.9` | 6.00 | 0.0% | 👑 FILAR KANONU (Core Keystone) |
| `so-05` | **Wezwanie do Trybunału** | Święte Oficjum | 0 | 0 | 1.06 | 30.1% → 27.2% | `-2.9%` | 70.0 | `+2.0` | 5.61 | 0.0% | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) |
| `so-01` | **Patrol Familiariuszy** | Święte Oficjum | 1 | 0 | 0.38 | 30.1% → 31.0% | `+0.9%` | 66.9 | `-1.1` | 5.56 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-02` | **Skarbiec Trybunału** | Święte Oficjum | 1 | 0 | 1.11 | 30.1% → 26.8% | `-3.3%` | 72.8 | `+4.8` | 5.68 | 0.0% | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) |
| `so-04` | **Publiczne Ostrzeżenie** | Święte Oficjum | 1 | 0 | 1.03 | 30.1% → 32.1% | `+2.0%` | 64.0 | `-4.0` | 5.54 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-12` | **Straż Trybunalska** | Święte Oficjum | 1 | 0 | 0.91 | 30.1% → 31.4% | `+1.3%` | 65.7 | `-2.3` | 5.57 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-03` | **Podejrzenie** | Święte Oficjum | 2 | 2 | 0.91 | 30.1% → 30.6% | `+0.5%` | 69.8 | `+1.8` | 5.68 | 0.0% | ⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor) |
| `so-08` | **Nasłanie Inkwizytora** | Święte Oficjum | 0 | 0 | 1.05 | 30.1% → 32.3% | `+2.2%` | 63.4 | `-4.6` | 5.56 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-09` | **Świadek Koronny** | Święte Oficjum | 1 | 0 | 0.71 | 30.1% → 29.9% | `-0.2%` | 69.1 | `+1.1` | 5.56 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-11` | **Dekret Czystości Wiary** | Święte Oficjum | 1 | 1 | 0.56 | 30.1% → 31.2% | `+1.1%` | 66.8 | `-1.2` | 5.59 | 0.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `so-06` | **Areszt Trybunalski** | Święte Oficjum | 2 | 0 | 1.03 | 30.1% → 32.2% | `+2.1%` | 67.1 | `-0.9` | 5.57 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-07` | **Przesłuchanie Oficjum** | Święte Oficjum | 2 | 0 | 0.08 | 30.1% → 31.3% | `+1.2%` | 66.7 | `-1.3` | 5.57 | 0.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `so-10` | **Oczyść Miasto** | Święte Oficjum | 5 | 1 | 0.65 | 30.1% → 28.9% | `-1.2%` | 65.4 | `-2.6` | 5.70 | 0.0% | ⚓ KOTWICA KANONU (Balance Anchor) |

### 2.4. 🎯 Monokultura Talii (Deck Concentration Index)

Jak mocno skoncentrowane jest zagrywanie kart w obrębie każdej frakcji.
Wskaźnik HHI (Herfindahl–Hirschman Index) mierzy koncentrację: HHI = 1.0 oznacza, że 100% zagrań to 1 karta; HHI ≈ 1/N oznacza idealnie równomierny rozkład.

| Frakcja | Kart w Talii | Top Karta (Play-Rate) | Top 2 (%) | HHI | Ocena |
| :--- | :---: | :--- | :---: | :---: | :--- |
| Cienie Al-Andalus | 12 | `caa-12` (1.07) | 23.3% | 0.102 | 🟢 Zdrowy rozkład |
| Gildia Cieni | 12 | `gc-09` (1.09) | 25.4% | 0.101 | 🟢 Zdrowy rozkład |
| Korona & Borgiowie | 12 | `kb-05` (0.91) | 24.0% | 0.095 | 🟢 Zdrowy rozkład |
| Kabała z Toledo | 12 | `kt-06` (1.09) | 25.1% | 0.100 | 🟢 Zdrowy rozkład |
| Święte Oficjum | 12 | `so-02` (1.11) | 22.9% | 0.096 | 🟢 Zdrowy rozkład |

---

## 3. ⏳ Warstwa II — Kronika Dziejów w 4P (Ablacja 8 Kart Wydarzeń Czasu)

Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans w 4P:

| ID | Karta Wydarzenia | 4P Score | $\Delta$ 4P | Średnia Er | Deadlock % | Status Roli w Kronice |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `time-01` | **Kapitulacja Grenady** | 68.0 → 🟠 ** 66.6** (`-1.4`) | `-1.4 pkt` | 5.61 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-02` | **Godzina Policyjna** | 68.0 → 🟠 ** 65.9** (`-2.1`) | `-2.1 pkt` | 5.59 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-03` | **Flota Odkrywców** | 68.0 → 🟠 ** 66.7** (`-1.3`) | `-1.3 pkt` | 5.67 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-04` | **Rewizja w Dzielnicach** | 68.0 → 🟠 ** 70.0** (`⬆️ +2.0`) | `+2.0 pkt` | 5.64 Er | 0.0% | ⚠️ Spowalniacz |
| `time-05` | **Gorączka Donosów** | 68.0 → 🟠 ** 65.7** (`-2.3`) | `-2.3 pkt` | 5.60 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-06` | **Nocna Obława** | 68.0 → 🟠 ** 64.9** (`-3.1`) | `-3.1 pkt` | 5.58 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-07` | **Bunt w Lochach** | 68.0 → 🟠 ** 65.9** (`-2.1`) | `-2.1 pkt` | 5.59 Er | 0.0% | 🟢 Stabilizator tempa |
| `time-08` | **Święte Przymierze** | 68.0 → 🟠 ** 69.7** (`⬆️ +1.7`) | `+1.7 pkt` | 5.52 Er | 0.0% | ⚠️ Spowalniacz |
| `time-09` | **Jarmark Królewski** | 🟠 ** 68.0** | `0.0 pkt` | 5.60 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-10` | **Amnestia Biskupia** | 68.0 → 🟠 ** 65.5** (`-2.5`) | `-2.5 pkt` | 5.59 Er | 0.0% | 🟢 Stabilizator tempa |

---

## 4. ⚙️ Warstwa III — Matryca 9 Obszarów Wpływu Mechanik Gry (L1, L2, L4)

Mechaniki w tym raporcie: **skraj albo wyłączenie**. Testy ±1 są w `audit_level1` / `audit_level2` / `audit_level4`. **Δ≈0 nie jest harmonią.**

| Kategoria Mechaniki | Liczba Testów | Rola w Ekosystemie Kanonu 4P | Rekomendacja Balansowa |
| :--- | :---: | :--- | :--- |
| 👑 / 🛡️ **Filary i Bezpieczniki** | **22** | Ablacja wali w stół — gracze czują tę gałkę | **Cel kanonu** |
| ⚠️ **Za słabe dźwignie** | **4** | Rusza share, nie trzyma stołu — nie jest „zbalansowana” | **Wzmocnić aż będzie filarem** |
| 💤 **Martwe / uśpione ścieżki** | **1** | Dual-win z witalności albo ablacja Δ≈0 | Wada pomiaru, nie harmonia |
| ⚠️ / 💡 **Wady bieżącej wartości** | **2** | Inna wartość gałki **podnosi** 4P — obecny setting szkodzi | **Przekręcić albo rework** |

### 4.0. ⚠️ Problematyczne mechaniki (osobny wykaz)
Wszystkie mechaniki z grup **DEAD**, **WEAK/NEUTRAL** i **DISRUPTOR**: ścieżki dual-win z `evaluate_vitality`, testy z $|\Delta\text{4P}| \le 0.8$ i ruchem share $\le 1.5$ pp (DEAD), za słabe dźwignie (WEAK) oraz wady bieżącej wartości (DISRUPTOR).

| Badany Podsystem | Kategoria | 4P Score | $\Delta$ 4P | Klasyfikacja |
| :--- | :--- | :---: | :---: | :--- |
| **Inkwizytor Patrol: ruch x2 (podwojona prędkość)** | Poziom 4: Warianty i Modyfikatory | 68.0 → 🟠 ** 68.5** (`⬆️ +0.5`) | `+0.5 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Kabała: fragmenty 3 → 1** | Poziom 2: Warunki Zwycięstwa | 68.0 → 🟠 ** 68.1** (`⬆️ +0.1`) | `+0.1 pkt` | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |
| **Kronika Dziejów: co 3 Ery (spowolniony zegar)** | Poziom 4: Warianty i Modyfikatory | 68.0 → 🟠 ** 67.0** (`-1.0`) | `-1.0 pkt` | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |
| **Autodafé: całkowite wyłączenie** | Poziom 1: System Core | 68.0 → 🟠 ** 66.8** (`-1.2`) | `-1.2 pkt` | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |
| **Szlak Morski: era 4 → nigdy (99)** | Poziom 4: Warianty i Modyfikatory | 68.0 → 🟠 ** 64.3** (`-3.7`) | `-3.7 pkt` | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |
| **Limit Er: 14 → 7 (skrajna presja)** | Poziom 1: System Core | 68.0 → 🟠 ** 69.6** (`⬆️ +1.6`) | `+1.6 pkt` | 💡 KANDYDAT DO UPROSZCZENIA (Simplification) |
| **Święte Oficjum: stosy 7 → 14** | Poziom 2: Warunki Zwycięstwa | 68.0 → 🟠 ** 73.7** (`⬆️ +5.7`) | `+5.7 pkt` | ⚠️ UMIARKOWANE OBCIĄŻENIE (Moderate Drag) |

### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)

| Badany Podsystem / Modyfikator L1 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Limit Er: 14 → 7 (skrajna presja)** | 68.0 → 🟠 ** 69.6** (`⬆️ +1.6`) | `+1.6 pkt` | 5.46 Er | 24.4% | 4.9% | 💡 KANDYDAT DO UPROSZCZENIA (Simplification) |
| **Próg Oskarżenia: 7 → 1** | 68.0 → 🔴 ** 24.6** (`-43.4`) | `-43.4 pkt` | 4.99 Er | 0.0% | 3.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Oskarżenia: 7 → 14** | 68.0 → 🔴 ** 26.4** (`-41.6`) | `-41.6 pkt` | 6.16 Er | 0.2% | 6.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 0zł (wyłączenie)** | 68.0 → 🔴 ** 49.6** (`-18.4`) | `-18.4 pkt` | 6.60 Er | 0.0% | 13.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 8zł** | 68.0 → 🔴 ** 25.3** (`-42.7`) | `-42.7 pkt` | 4.86 Er | 0.0% | 1.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 1** | 68.0 → 🔴 ** 36.1** (`-31.9`) | `-31.9 pkt` | 6.71 Er | 0.1% | 5.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 6** | 68.0 → 🔴 ** 16.0** (`-52.0`) | `-52.0 pkt` | 4.42 Er | 0.0% | 4.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 1** | 68.0 → 🔴 ** 10.0** (`-58.0`) | `-58.0 pkt` | 8.44 Er | 1.3% | 51.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 10** | 68.0 → 🔴 ** 53.5** (`-14.5`) | `-14.5 pkt` | 5.47 Er | 0.0% | 4.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: cooldown 4 → 0 (co erę)** | 68.0 → 🔴 ** 16.0** (`-52.0`) | `-52.0 pkt` | 4.64 Er | 0.0% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: całkowite wyłączenie** | 68.0 → 🟠 ** 66.8** (`-1.2`) | `-1.2 pkt` | 5.80 Er | 0.0% | 4.6% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |
| **Akcja Gospodarcza: 0zł (brak zysku złota)** | 68.0 → 🟠 ** 60.7** (`-7.3`) | `-7.3 pkt` | 5.70 Er | 0.0% | 7.2% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Akcja Gospodarcza: 1 → 2 (podwojenie)** | 68.0 → 🔴 ** 44.0** (`-24.0`) | `-24.0 pkt` | 5.46 Er | 0.0% | 4.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Obserwowanej: 5 → 2 (skrajna presja)** | 68.0 → 🔴 ** 57.5** (`-10.5`) | `-10.5 pkt` | 5.46 Er | 0.0% | 5.0% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |

### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)

| Badany Warunek Zwycięstwa L2 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: stosy 7 → 1** | 68.0 → 🔴 ** 14.2** (`-53.8`) | `-53.8 pkt` | 3.92 Er | 0.0% | 4.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: stosy 7 → 14** | 68.0 → 🟠 ** 73.7** (`⬆️ +5.7`) | `+5.7 pkt` | 5.64 Er | 0.0% | 5.0% | ⚠️ UMIARKOWANE OBCIĄŻENIE (Moderate Drag) |
| **Święte Oficjum: skazania 3 → 1** | 68.0 → 🔴 ** 14.2** (`-53.8`) | `-53.8 pkt` | 3.35 Er | 0.0% | 4.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 6** | 68.0 → 🔴 ** 47.3** (`-20.7`) | `-20.7 pkt` | 5.81 Er | 0.0% | 5.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Cienie: relikwie 2 → 4** | 68.0 → 🔴 ** 27.4** (`-40.6`) | `-40.6 pkt` | 5.91 Er | 0.0% | 5.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: dekrety 2 → 4** | 68.0 → 🔴 ** 26.2** (`-41.8`) | `-41.8 pkt` | 5.88 Er | 0.0% | 4.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: fragmenty 3 → 1** | 68.0 → 🟠 ** 68.1** (`⬆️ +0.1`) | `+0.1 pkt` | 5.48 Er | 0.0% | 4.9% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |
| **Kabała: fragmenty 3 → 6** | 68.0 → 🔴 ** 28.7** (`-39.3`) | `-39.3 pkt` | 5.95 Er | 0.0% | 5.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 8 → 1** | 68.0 → 🔴 ** 14.2** (`-53.8`) | `-53.8 pkt` | 3.13 Er | 0.0% | 4.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 8 → 16** | 68.0 → 🔴 ** 27.5** (`-40.5`) | `-40.5 pkt` | 5.79 Er | 0.0% | 5.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)

| Badany Wariant / Modyfikator L4 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kronika Dziejów: całkowite wyłączenie** | 68.0 → 🔴 ** 58.5** (`-9.5`) | `-9.5 pkt` | 5.70 Er | 0.0% | 5.7% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Kronika Dziejów: co 3 Ery (spowolniony zegar)** | 68.0 → 🟠 ** 67.0** (`-1.0`) | `-1.0 pkt` | 5.75 Er | 0.0% | 5.6% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |
| **Inkwizytor Patrol: ruch 1 → 0 (wyłączenie)** | 68.0 → 🔴 ** 35.8** (`-32.2`) | `-32.2 pkt` | 6.34 Er | 0.1% | 5.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Inkwizytor Patrol: ruch x2 (podwojona prędkość)** | 68.0 → 🟠 ** 68.5** (`⬆️ +0.5`) | `+0.5 pkt` | 5.54 Er | 0.0% | 5.0% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Szlak Morski: era 4 → nigdy (99)** | 68.0 → 🟠 ** 64.3** (`-3.7`) | `-3.7 pkt` | 5.63 Er | 0.0% | 5.0% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |

---

## 5. 👥 Warstwa IV — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych. Kolumna win share to HUD kanonu; setup+witalność to stary blend (kara martwej ścieżki).

| Nieobecna Frakcja | Setup Testowy | Win share | Setup+witalność | Diagnoza |
| :--- | :--- | :---: | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`70.4`** | `53.5` | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`70.6`** | `55.2` | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`67.3`** | `39.5` | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`62.1`** | `62.1` | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`69.7`** | `56.5` | Brak presji stosów i bezpośredniego Inkwizytora |