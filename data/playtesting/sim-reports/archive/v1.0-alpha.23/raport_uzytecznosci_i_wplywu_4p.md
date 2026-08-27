[Strona główna](../../../../../README.md) > [v1.0-alpha.23](README.md) > [raport_uzytecznosci_i_wplywu_4p](raport_uzytecznosci_i_wplywu_4p.md)

---

# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v1.0-alpha.23

**Wersja Gry:** `v1.0-alpha.23` | **Data Badania:** 2026-08-22 15:43 | **Próba:** 5000 gier/setup (25000 gier na wariant) | **Ziarno:** 42
**4P Score (win share):** 🟡 ** 82.1** pkt | **Witalność (osobna kara):** `0.000` | **Śr. Er:** `6.04` | **Deadlocki:** `0.1%` | **Pas Biedy:** `1.5%`
**Udziały 4P:** CAA 23.5% · GC 24.7% · KB 24.9% · KT 28.1% · SO 23.9%

Klasyfikacja L1/L2/L4 i Δ 4P liczą wyłącznie równość win share (`calculate_balance_score`). Kara witalności jest osobno.

---

## 0. Wady z tej próby (nie HUD win share)

Kubełki klasyfikatora i ostrzeżenia witalności z bieżącego runu.

- **Share |Δ| ≥ 2.5 pp od 25%:** KT 28.1%
- **Autopodatek (SELF_HARM):** 19/60
- **DEAD_WEIGHT:** `gc-12` Złodziejski Zwiad, `gc-11` Fałszywe Świadectwo Cechu, `gc-08` Zatrute Złoto
- **Karty Kroniki |Δ4P| ≤ 0.8:** 2/10
- **Ablacja całej Kroniki (`L4_NO_TIME_DECK`):** Δ4P -8.6 (STABILIZER)
- **Mechaniki WEAK/NEUTRAL:** Szlak Morski: era 4 → nigdy (99)

---

## 1. 🗺️ Podsumowanie Ekosystemu Kart Kanonu 4P (Matryca Wpływu Kart, 60 kart)

Rozkład wszystkich 60 kart frakcyjnych w matrycy **Wpływ na Frakcję ($\Delta \text{Share}$)** vs **Wpływ na Kanon 4P ($\Delta \text{4P Score}$)**:

| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |
| :--- | :---: | :---: | :--- | :--- |
| 🩸 **Autopodatek (Self-Harm)** | **19** | 31.7% | Wyłączenie **podnosi** win share własnej frakcji — karta jest haraczem, nie silnikiem | **Rework / osłabienie kosztu, nie filar** |
| 💤 **Karta Pasywna (Dead Weight)** | **3** | 5.0% | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia lub wycięcia** |
| ⚠️ **Karta Destabilizująca (Disruptor)** | **2** | 3.3% | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |
| ⚖️ **Zbalansowane Narzędzie** | **11** | 18.3% | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Narzędzie, nie złoty środek całego kanonu** |
| 👑 / ⚓ **Filar / Kotwica Kanonu** | **25** | 41.7% | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |

---

## 2. 🃏 Warstwa I — Szczegółowa Analiza 60 Kart Frakcji w Kanonie 4P

### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)
Karty, których brak powoduje spadek wyniku Kanonu 4P o $\ge 4.0$ pkt lub załamanie winrate frakcji o $\ge 4.0\%$ — **bez** autopodatków (te są w 2.1b):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kb-09` **Dekret Królewski** | Korona & Borgiowie | 4zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 24.9% → **0.1%** | **`-24.8%`** | 82.1 → **30.7 pkt** (`-51.4`) |
| `kb-10` **Pieczęć Korony** | Korona & Borgiowie | 3zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 24.9% → **0.8%** | **`-24.1%`** | 82.1 → **31.7 pkt** (`-50.4`) |
| `caa-10` **Echo Alhambry** | Cienie Al-Andalus | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 23.5% → **2.4%** | **`-21.1%`** | 82.1 → **34.0 pkt** (`-48.1`) |
| `caa-05` **Ukryty Kurier** | Cienie Al-Andalus | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 23.5% → **11.7%** | **`-11.8%`** | 82.1 → **51.7 pkt** (`-30.4`) |
| `kt-03` **Zakazana Wiedza** | Kabała z Toledo | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 28.1% → **14.0%** | **`-14.1%`** | 82.1 → **57.0 pkt** (`-25.1`) |
| `kt-05` **Wskazówka Cyklu** | Kabała z Toledo | 1zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 28.1% → **17.8%** | **`-10.3%`** | 82.1 → **67.9 pkt** (`-14.2`) |
| `kb-11` **Tajny Emisariusz** | Korona & Borgiowie | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.9% → **23.6%** | **`-1.3%`** | 82.1 → **70.1 pkt** (`-12.0`) |
| `kb-03` **Plotka Dworska** | Korona & Borgiowie | 1zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.9% → **23.5%** | **`-1.4%`** | 82.1 → **70.8 pkt** (`-11.3`) |
| `kb-01` **Rozkaz Dworu** | Korona & Borgiowie | 1zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.9% → **23.7%** | **`-1.2%`** | 82.1 → **71.5 pkt** (`-10.6`) |
| `kb-02` **Pobór Podatków** | Korona & Borgiowie | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.9% → **24.7%** | **`-0.2%`** | 82.1 → **74.6 pkt** (`-7.5`) |
| `so-02` **Skarbiec Trybunału** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.9% → **22.2%** | **`-1.7%`** | 82.1 → **75.5 pkt** (`-6.6`) |
| `kt-04` **Zwierciadło Herezji** | Kabała z Toledo | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 28.1% → **29.9%** | **`+1.8%`** | 82.1 → **76.2 pkt** (`-5.9`) |
| `gc-04` **Informator** | Gildia Cieni | 1zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.7% → **26.2%** | **`+1.5%`** | 82.1 → **77.8 pkt** (`-4.3`) |
| `so-06` **Areszt Trybunalski** | Święte Oficjum | 2zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.9% → **24.3%** | **`+0.4%`** | 82.1 → **78.7 pkt** (`-3.4`) |
| `gc-09` **Lista Dłużników** | Gildia Cieni | 3zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 24.7% → **21.9%** | **`-2.8%`** | 82.1 → **78.8 pkt** (`-3.3`) |
| `caa-03` **Cień na Rynku** | Cienie Al-Andalus | 0zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.5% → **25.4%** | **`+1.9%`** | 82.1 → **78.9 pkt** (`-3.2`) |
| `so-12` **Straż Trybunalska** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.9% → **24.4%** | **`+0.5%`** | 82.1 → **79.0 pkt** (`-3.1`) |
| `so-11` **Dekret Czystości Wiary** | Święte Oficjum | 1zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.9% → **24.4%** | **`+0.5%`** | 82.1 → **79.0 pkt** (`-3.1`) |
| `so-10` **Oczyść Miasto** | Święte Oficjum | 5zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.9% → **24.5%** | **`+0.6%`** | 82.1 → **79.0 pkt** (`-3.1`) |
| `gc-07` **Skrytobójstwo** | Gildia Cieni | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 24.7% → **25.3%** | **`+0.6%`** | 82.1 → **79.1 pkt** (`-3.0`) |
| `gc-06` **Szantaż** | Gildia Cieni | 2zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 24.7% → **21.7%** | **`-3.0%`** | 82.1 → **79.1 pkt** (`-3.0`) |
| `so-05` **Wezwanie do Trybunału** | Święte Oficjum | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.9% → **22.2%** | **`-1.7%`** | 82.1 → **79.5 pkt** (`-2.6`) |
| `so-08` **Nasłanie Inkwizytora** | Święte Oficjum | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 23.9% → **24.2%** | **`+0.3%`** | 82.1 → **79.5 pkt** (`-2.6`) |
| `caa-06` **Ucieczka z Lochów** | Cienie Al-Andalus | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 23.5% → **21.0%** | **`-2.5%`** | 82.1 → **80.0 pkt** (`-2.1`) |
| `kt-08` **Areszt Wiedzy** | Kabała z Toledo | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 28.1% → **27.9%** | **`-0.2%`** | 82.1 → **80.0 pkt** (`-2.1`) |

### 2.1b. 🩸 Autopodatek Frakcji (Self-Harm)
Karty, których wyłączenie **podnosi** win share własnej frakcji. Gracz zauważy je jako haracz, nawet gdy stół 4P jest równy dzięki temu haraczowi.

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `caa-11` **Nocna Zmiana Warty** | Cienie Al-Andalus | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 23.5% → **44.1%** | **`+20.6%`** | 82.1 → **42.2 pkt** (`-39.9`) |
| `caa-04` **Fałszywy Trop** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 23.5% → **43.7%** | **`+20.2%`** | 82.1 → **43.0 pkt** (`-39.1`) |
| `caa-01` **Przejście Podziemiami** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 23.5% → **43.3%** | **`+19.8%`** | 82.1 → **43.7 pkt** (`-38.4`) |
| `caa-08` **Kaptur Nocy** | Cienie Al-Andalus | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 23.5% → **43.3%** | **`+19.8%`** | 82.1 → **43.5 pkt** (`-38.6`) |
| `kb-04` **Faworyt Dworu** | Korona & Borgiowie | 2zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.9% → **40.5%** | **`+15.6%`** | 82.1 → **50.9 pkt** (`-31.2`) |
| `kt-10` **Pieczęć Salomona** | Kabała z Toledo | 2zł / 2☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 28.1% → **41.1%** | **`+13.0%`** | 82.1 → **46.7 pkt** (`-35.4`) |
| `caa-07` **Szantaż Bractwa** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 23.5% → **34.3%** | **`+10.8%`** | 82.1 → **62.5 pkt** (`-19.6`) |
| `kb-05` **List Żelazny** | Korona & Borgiowie | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.9% → **29.7%** | **`+4.8%`** | 82.1 → **80.7 pkt** (`-1.4`) |
| `kb-06` **Areszt Królewski** | Korona & Borgiowie | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.9% → **29.5%** | **`+4.6%`** | 82.1 → **70.8 pkt** (`-11.3`) |
| `kb-07` **Szantaż Pieczęcią** | Korona & Borgiowie | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.9% → **28.5%** | **`+3.6%`** | 82.1 → **79.3 pkt** (`-2.8`) |
| `kb-08` **Przekupstwo Sędziego** | Korona & Borgiowie | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.9% → **28.5%** | **`+3.6%`** | 82.1 → **79.3 pkt** (`-2.8`) |
| `gc-02` **Czarny Rynek** | Gildia Cieni | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 24.7% → **27.9%** | **`+3.2%`** | 82.1 → **76.0 pkt** (`-6.1`) |
| `caa-12` **Skrytka w Murach** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 23.5% → **26.5%** | **`+3.0%`** | 82.1 → **82.4 pkt** (`0.3`) |
| `kt-12` **Strażnik Archiwum** | Kabała z Toledo | 0zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 28.1% → **30.8%** | **`+2.7%`** | 82.1 → **74.1 pkt** (`-8.0`) |
| `kt-11` **Medytacja Sefirot** | Kabała z Toledo | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 28.1% → **30.8%** | **`+2.7%`** | 82.1 → **74.4 pkt** (`-7.7`) |
| `kt-07` **Archiwum Ukryte** | Kabała z Toledo | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 28.1% → **30.6%** | **`+2.5%`** | 82.1 → **74.0 pkt** (`-8.1`) |
| `caa-02` **Złoto z Kryjówki** | Cienie Al-Andalus | 0zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 23.5% → **25.6%** | **`+2.1%`** | 82.1 → **82.4 pkt** (`0.3`) |
| `kt-01` **Rytuał Przejścia** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 28.1% → **30.2%** | **`+2.1%`** | 82.1 → **75.3 pkt** (`-6.8`) |
| `kt-02` **Transmutacja Złota** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 28.1% → **30.2%** | **`+2.1%`** | 82.1 → **75.3 pkt** (`-6.8`) |

### 2.2. ⚠️ Karty Destabilizujące Kanon 4P (Disruptors)
Karty, których wyłączenie podnosi 4P Score ($\Delta \text{4P} \ge +1.5$ pkt):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kt-06` **Przesłuchanie Imienia** | Kabała z Toledo | 2zł / 0☣ | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) | 28.1% → **26.3%** | `-1.8%` | 82.1 → **84.1 pkt** (`+2.0`) |
| `kt-09` **Fragment Kodeksu** | Kabała z Toledo | 2zł / 1☣ | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) | 28.1% → **24.6%** | `-3.5%` | 82.1 → **83.4 pkt** (`+1.3`) |

### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich 60 Kart Frakcji w Kanonie 4P

| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Faction Win Share 4P | $\Delta$ Frakcji | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `caa-01` | **Przejście Podziemiami** | Cienie Al-Andalus | 0 | 0 | 23.5% → 43.3% | `+19.8%` | 43.7 | `-38.4` | 5.68 | 0.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-02` | **Złoto z Kryjówki** | Cienie Al-Andalus | 0 | 0 | 23.5% → 25.6% | `+2.1%` | 82.4 | `+0.3` | 5.98 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-03` | **Cień na Rynku** | Cienie Al-Andalus | 0 | 1 | 23.5% → 25.4% | `+1.9%` | 78.9 | `-3.2` | 6.30 | 0.2% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-04` | **Fałszywy Trop** | Cienie Al-Andalus | 0 | 0 | 23.5% → 43.7% | `+20.2%` | 43.0 | `-39.1` | 5.70 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-05` | **Ukryty Kurier** | Cienie Al-Andalus | 0 | 0 | 23.5% → 11.7% | `-11.8%` | 51.7 | `-30.4` | 6.27 | 0.2% | 👑 FILAR KANONU (Core Keystone) |
| `caa-12` | **Skrytka w Murach** | Cienie Al-Andalus | 0 | 0 | 23.5% → 26.5% | `+3.0%` | 82.4 | `+0.3` | 5.97 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-06` | **Ucieczka z Lochów** | Cienie Al-Andalus | 0 | 0 | 23.5% → 21.0% | `-2.5%` | 80.0 | `-2.1` | 5.93 | 0.2% | 👑 FILAR KANONU (Core Keystone) |
| `caa-07` | **Szantaż Bractwa** | Cienie Al-Andalus | 0 | 0 | 23.5% → 34.3% | `+10.8%` | 62.5 | `-19.6` | 5.79 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-08` | **Kaptur Nocy** | Cienie Al-Andalus | 1 | 0 | 23.5% → 43.3% | `+19.8%` | 43.5 | `-38.6` | 5.70 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-11` | **Nocna Zmiana Warty** | Cienie Al-Andalus | 1 | 0 | 23.5% → 44.1% | `+20.6%` | 42.2 | `-39.9` | 5.68 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-09` | **Kurier Relikwii** | Cienie Al-Andalus | 0 | 0 | 23.5% → 25.4% | `+1.9%` | 83.1 | `+1.0` | 6.00 | 0.1% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `caa-10` | **Echo Alhambry** | Cienie Al-Andalus | 1 | 0 | 23.5% → 2.4% | `-21.1%` | 34.0 | `-48.1` | 6.53 | 0.2% | 👑 FILAR KANONU (Core Keystone) |
| `gc-05` | **Fałszywy Świadek** | Gildia Cieni | 0 | 0 | 24.7% → 24.4% | `-0.3%` | 82.6 | `+0.5` | 6.03 | 0.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-12` | **Złodziejski Zwiad** | Gildia Cieni | 0 | 2 | 24.7% → 25.1% | `+0.4%` | 82.4 | `+0.3` | 6.01 | 0.1% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `gc-02` | **Czarny Rynek** | Gildia Cieni | 1 | 1 | 24.7% → 27.9% | `+3.2%` | 76.0 | `-6.1` | 6.07 | 0.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `gc-03` | **Podrzucenie Księgi** | Gildia Cieni | 1 | 0 | 24.7% → 24.6% | `-0.1%` | 80.8 | `-1.3` | 6.01 | 0.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-04` | **Informator** | Gildia Cieni | 1 | 1 | 24.7% → 26.2% | `+1.5%` | 77.8 | `-4.3` | 6.06 | 0.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-01` | **Przekupiony Strażnik** | Gildia Cieni | 2 | 1 | 24.7% → 24.6% | `-0.1%` | 83.0 | `+0.9` | 6.01 | 0.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-07` | **Skrytobójstwo** | Gildia Cieni | 0 | 0 | 24.7% → 25.3% | `+0.6%` | 79.1 | `-3.0` | 6.03 | 0.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-11` | **Fałszywe Świadectwo Cechu** | Gildia Cieni | 0 | 2 | 24.7% → 25.1% | `+0.4%` | 82.4 | `+0.3` | 6.01 | 0.1% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `gc-08` | **Zatrute Złoto** | Gildia Cieni | 1 | 1 | 24.7% → 24.8% | `+0.1%` | 81.7 | `-0.4` | 6.00 | 0.1% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `gc-06` | **Szantaż** | Gildia Cieni | 2 | 1 | 24.7% → 21.7% | `-3.0%` | 79.1 | `-3.0` | 6.15 | 0.1% | 👑 FILAR KANONU (Core Keystone) |
| `gc-09` | **Lista Dłużników** | Gildia Cieni | 3 | 1 | 24.7% → 21.9% | `-2.8%` | 78.8 | `-3.3` | 6.14 | 0.1% | 👑 FILAR KANONU (Core Keystone) |
| `gc-10` | **Upadek Domu** | Gildia Cieni | 4 | 2 | 24.7% → 25.0% | `+0.3%` | 81.4 | `-0.7` | 6.05 | 0.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-01` | **Rozkaz Dworu** | Korona & Borgiowie | 1 | 1 | 24.9% → 23.7% | `-1.2%` | 71.5 | `-10.6` | 6.03 | 0.2% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kb-02` | **Pobór Podatków** | Korona & Borgiowie | 1 | 0 | 24.9% → 24.7% | `-0.2%` | 74.6 | `-7.5` | 6.02 | 0.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kb-03` | **Plotka Dworska** | Korona & Borgiowie | 1 | 1 | 24.9% → 23.5% | `-1.4%` | 70.8 | `-11.3` | 6.02 | 0.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kb-11` | **Tajny Emisariusz** | Korona & Borgiowie | 1 | 0 | 24.9% → 23.6% | `-1.3%` | 70.1 | `-12.0` | 6.03 | 0.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kb-04` | **Faworyt Dworu** | Korona & Borgiowie | 2 | 1 | 24.9% → 40.5% | `+15.6%` | 50.9 | `-31.2` | 5.81 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-05` | **List Żelazny** | Korona & Borgiowie | 2 | 0 | 24.9% → 29.7% | `+4.8%` | 80.7 | `-1.4` | 5.91 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-12` | **Szantaż Salonowy** | Korona & Borgiowie | 1 | 0 | 24.9% → 26.4% | `+1.5%` | 82.3 | `+0.2` | 6.03 | 0.1% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `kb-06` | **Areszt Królewski** | Korona & Borgiowie | 2 | 0 | 24.9% → 29.5% | `+4.6%` | 70.8 | `-11.3` | 5.98 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-07` | **Szantaż Pieczęcią** | Korona & Borgiowie | 2 | 0 | 24.9% → 28.5% | `+3.6%` | 79.3 | `-2.8` | 6.00 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-08` | **Przekupstwo Sędziego** | Korona & Borgiowie | 2 | 0 | 24.9% → 28.5% | `+3.6%` | 79.3 | `-2.8` | 6.00 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-10` | **Pieczęć Korony** | Korona & Borgiowie | 3 | 2 | 24.9% → 0.8% | `-24.1%` | 31.7 | `-50.4` | 6.31 | 0.1% | 👑 FILAR KANONU (Core Keystone) |
| `kb-09` | **Dekret Królewski** | Korona & Borgiowie | 4 | 1 | 24.9% → 0.1% | `-24.8%` | 30.7 | `-51.4` | 6.36 | 0.3% | 👑 FILAR KANONU (Core Keystone) |
| `kt-03` | **Zakazana Wiedza** | Kabała z Toledo | 0 | 0 | 28.1% → 14.0% | `-14.1%` | 57.0 | `-25.1` | 6.21 | 0.2% | 👑 FILAR KANONU (Core Keystone) |
| `kt-12` | **Strażnik Archiwum** | Kabała z Toledo | 0 | 1 | 28.1% → 30.8% | `+2.7%` | 74.1 | `-8.0` | 5.99 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-01` | **Rytuał Przejścia** | Kabała z Toledo | 1 | 0 | 28.1% → 30.2% | `+2.1%` | 75.3 | `-6.8` | 5.99 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-02` | **Transmutacja Złota** | Kabała z Toledo | 1 | 0 | 28.1% → 30.2% | `+2.1%` | 75.3 | `-6.8` | 5.99 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-04` | **Zwierciadło Herezji** | Kabała z Toledo | 1 | 0 | 28.1% → 29.9% | `+1.8%` | 76.2 | `-5.9` | 5.99 | 0.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kt-05` | **Wskazówka Cyklu** | Kabała z Toledo | 1 | 1 | 28.1% → 17.8% | `-10.3%` | 67.9 | `-14.2` | 6.17 | 0.2% | 👑 FILAR KANONU (Core Keystone) |
| `kt-07` | **Archiwum Ukryte** | Kabała z Toledo | 1 | 1 | 28.1% → 30.6% | `+2.5%` | 74.0 | `-8.1` | 5.99 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-08` | **Areszt Wiedzy** | Kabała z Toledo | 1 | 0 | 28.1% → 27.9% | `-0.2%` | 80.0 | `-2.1` | 6.04 | 0.2% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kt-06` | **Przesłuchanie Imienia** | Kabała z Toledo | 2 | 0 | 28.1% → 26.3% | `-1.8%` | 84.1 | `+2.0` | 6.05 | 0.1% | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) |
| `kt-11` | **Medytacja Sefirot** | Kabała z Toledo | 2 | 0 | 28.1% → 30.8% | `+2.7%` | 74.4 | `-7.7` | 5.99 | 0.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-09` | **Fragment Kodeksu** | Kabała z Toledo | 2 | 1 | 28.1% → 24.6% | `-3.5%` | 83.4 | `+1.3` | 6.08 | 0.2% | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) |
| `kt-10` | **Pieczęć Salomona** | Kabała z Toledo | 2 | 2 | 28.1% → 41.1% | `+13.0%` | 46.7 | `-35.4` | 5.89 | 0.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `so-05` | **Wezwanie do Trybunału** | Święte Oficjum | 0 | 0 | 23.9% → 22.2% | `-1.7%` | 79.5 | `-2.6` | 6.04 | 0.2% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-01` | **Patrol Familiariuszy** | Święte Oficjum | 1 | 0 | 23.9% → 24.7% | `+0.8%` | 81.5 | `-0.6` | 6.01 | 0.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-02` | **Skarbiec Trybunału** | Święte Oficjum | 1 | 0 | 23.9% → 22.2% | `-1.7%` | 75.5 | `-6.6` | 6.09 | 0.2% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-04` | **Publiczne Ostrzeżenie** | Święte Oficjum | 1 | 0 | 23.9% → 24.4% | `+0.5%` | 80.7 | `-1.4` | 6.01 | 0.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-12` | **Straż Trybunalska** | Święte Oficjum | 1 | 0 | 23.9% → 24.4% | `+0.5%` | 79.0 | `-3.1` | 6.01 | 0.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-03` | **Podejrzenie** | Święte Oficjum | 2 | 2 | 23.9% → 24.6% | `+0.7%` | 80.3 | `-1.8` | 6.01 | 0.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-08` | **Nasłanie Inkwizytora** | Święte Oficjum | 0 | 0 | 23.9% → 24.2% | `+0.3%` | 79.5 | `-2.6` | 6.02 | 0.2% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-09` | **Świadek Koronny** | Święte Oficjum | 1 | 0 | 23.9% → 23.2% | `-0.7%` | 80.3 | `-1.8` | 6.03 | 0.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-11` | **Dekret Czystości Wiary** | Święte Oficjum | 1 | 1 | 23.9% → 24.4% | `+0.5%` | 79.0 | `-3.1` | 6.01 | 0.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-06` | **Areszt Trybunalski** | Święte Oficjum | 2 | 0 | 23.9% → 24.3% | `+0.4%` | 78.7 | `-3.4` | 6.03 | 0.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-07` | **Przesłuchanie Oficjum** | Święte Oficjum | 2 | 0 | 23.9% → 24.7% | `+0.8%` | 81.1 | `-1.0` | 6.01 | 0.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-10` | **Oczyść Miasto** | Święte Oficjum | 5 | 1 | 23.9% → 24.5% | `+0.6%` | 79.0 | `-3.1` | 6.01 | 0.1% | ⚓ KOTWICA KANONU (Balance Anchor) |

---

## 3. ⏳ Warstwa II — Kronika Dziejów w 4P (Ablacja 8 Kart Wydarzeń Czasu)

Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans w 4P:

| ID | Karta Wydarzenia | 4P Score | $\Delta$ 4P | Średnia Er | Deadlock % | Status Roli w Kronice |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `time-01` | **Kapitulacja Grenady** | 82.1 → 🟡 ** 78.9** (`-3.2`) | `-3.2 pkt` | 6.08 Er | 0.2% | 🟢 Stabilizator tempa |
| `time-02` | **Godzina Policyjna** | 82.1 → 🟡 ** 80.9** (`-1.2`) | `-1.2 pkt` | 6.04 Er | 0.2% | 🟢 Stabilizator tempa |
| `time-03` | **Flota Odkrywców** | 82.1 → 🟡 ** 80.4** (`-1.7`) | `-1.7 pkt` | 6.05 Er | 0.2% | 🟢 Stabilizator tempa |
| `time-04` | **Rewizja w Dzielnicach** | 82.1 → 🟡 ** 80.2** (`-1.9`) | `-1.9 pkt` | 6.07 Er | 0.2% | 🟢 Stabilizator tempa |
| `time-05` | **Gorączka Donosów** | 82.1 → 🟡 ** 80.7** (`-1.4`) | `-1.4 pkt` | 6.07 Er | 0.2% | 🟢 Stabilizator tempa |
| `time-06` | **Nocna Obława** | 82.1 → 🟡 ** 81.7** (`-0.4`) | `-0.4 pkt` | 6.03 Er | 0.1% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-07` | **Bunt w Lochach** | 82.1 → 🟡 ** 81.8** (`-0.3`) | `-0.3 pkt` | 6.03 Er | 0.2% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-08` | **Święte Przymierze** | 82.1 → 🟡 ** 81.1** (`-1.0`) | `-1.0 pkt` | 5.95 Er | 0.1% | 🟢 Stabilizator tempa |
| `time-09` | **Jarmark Królewski** | 82.1 → 🟡 ** 83.3** (`⬆️ +1.2`) | `+1.2 pkt` | 6.03 Er | 0.2% | ⚠️ Spowalniacz |
| `time-10` | **Amnestia Biskupia** | 82.1 → 🟡 ** 84.4** (`⬆️ +2.3`) | `+2.3 pkt` | 6.03 Er | 0.1% | ⚠️ Spowalniacz |

---

## 4. ⚙️ Warstwa III — Matryca 9 Obszarów Wpływu Mechanik Gry (L1, L2, L4)

Mechaniki w tym raporcie: **skraj albo wyłączenie**. Testy ±1 są w `audit_level1` / `audit_level2` / `audit_level4`. **Δ≈0 nie jest harmonią.**

| Kategoria Mechaniki | Liczba Testów | Rola w Ekosystemie Kanonu 4P | Rekomendacja Balansowa |
| :--- | :---: | :--- | :--- |
| 👑 / 🛡️ **Filary i Bezpieczniki** | **24** | Ablacja wali w stół — gracze czują tę gałkę | **Cel kanonu** |
| ⚠️ **Za słabe dźwignie** | **1** | Rusza share, nie trzyma stołu — nie jest „zbalansowana” | **Wzmocnić aż będzie filarem** |
| 💤 **Martwe / uśpione ścieżki** | **0** | Dual-win z witalności albo ablacja Δ≈0 | Wada pomiaru, nie harmonia |
| ⚠️ / 💡 **Wady bieżącej wartości** | **0** | Inna wartość gałki **podnosi** 4P — obecny setting szkodzi | **Przekręcić albo rework** |

### 4.0. ⚠️ Problematyczne mechaniki (osobny wykaz)
Wszystkie mechaniki z grup **DEAD**, **WEAK/NEUTRAL** i **DISRUPTOR**: ścieżki dual-win z `evaluate_vitality`, testy z $|\Delta\text{4P}| \le 0.8$ i ruchem share $\le 1.5$ pp (DEAD), za słabe dźwignie (WEAK) oraz wady bieżącej wartości (DISRUPTOR).

| Badany Podsystem | Kategoria | 4P Score | $\Delta$ 4P | Klasyfikacja |
| :--- | :--- | :---: | :---: | :--- |
| **Szlak Morski: era 4 → nigdy (99)** | Poziom 4: Warianty i Modyfikatory | 82.1 → 🟡 ** 80.4** (`-1.7`) | `-1.7 pkt` | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |

### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)

| Badany Podsystem / Modyfikator L1 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Limit Er: 14 → 7 (skrajna presja)** | 82.1 → 🟠 ** 72.7** (`-9.4`) | `-9.4 pkt` | 5.72 Er | 25.7% | 1.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Próg Oskarżenia: 7 → 1** | 82.1 → 🔴 **  1.6** (`-80.5`) | `-80.5 pkt` | 5.47 Er | 0.0% | 0.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Oskarżenia: 7 → 14** | 82.1 → 🔴 ** 20.9** (`-61.2`) | `-61.2 pkt` | 5.96 Er | 0.2% | 1.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 0zł (wyłączenie)** | 82.1 → 🔴 ** 31.8** (`-50.3`) | `-50.3 pkt` | 6.26 Er | 0.1% | 5.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 8zł** | 82.1 → 🟠 ** 64.9** (`-17.2`) | `-17.2 pkt` | 5.74 Er | 0.1% | 0.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 1** | 82.1 → 🔴 ** 20.0** (`-62.1`) | `-62.1 pkt` | 8.27 Er | 10.2% | 1.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 6** | 82.1 → 🔴 **  9.6** (`-72.5`) | `-72.5 pkt` | 4.35 Er | 0.0% | 1.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 1** | 82.1 → 🔴 **  2.2** (`-79.9`) | `-79.9 pkt` | 8.69 Er | 1.8% | 11.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 10** | 82.1 → 🔴 **  3.1** (`-79.0`) | `-79.0 pkt` | 4.21 Er | 0.0% | 2.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: cooldown 3 → 0 (co erę)** | 82.1 → 🔴 ** 16.1** (`-66.0`) | `-66.0 pkt` | 5.24 Er | 0.1% | 1.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: całkowite wyłączenie** | 82.1 → 🔴 ** 23.6** (`-58.5`) | `-58.5 pkt` | 8.27 Er | 20.2% | 1.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)

| Badany Warunek Zwycięstwa L2 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: stosy 6 → 1** | 82.1 → 🔴 ** 15.3** (`-66.8`) | `-66.8 pkt` | 3.74 Er | 0.0% | 1.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: stosy 6 → 12** | 82.1 → 🔴 ** 52.4** (`-29.7`) | `-29.7 pkt` | 6.28 Er | 1.1% | 1.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 1** | 82.1 → 🔴 ** 15.4** (`-66.7`) | `-66.7 pkt` | 4.15 Er | 0.0% | 1.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 6** | 82.1 → 🟡 ** 75.7** (`-6.4`) | `-6.4 pkt` | 6.07 Er | 0.1% | 1.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Cienie: relikwie 2 → 4** | 82.1 → 🔴 ** 31.2** (`-50.9`) | `-50.9 pkt` | 6.52 Er | 0.2% | 1.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: dekrety 2 → 4** | 82.1 → 🔴 ** 31.0** (`-51.1`) | `-51.1 pkt` | 6.27 Er | 0.2% | 1.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: fragmenty 2 → 4** | 82.1 → 🔴 ** 36.3** (`-45.8`) | `-45.8 pkt` | 6.29 Er | 0.2% | 1.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: era 6 → 1** | 82.1 → 🔴 ** 40.3** (`-41.8`) | `-41.8 pkt` | 4.83 Er | 0.1% | 1.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: era 6 → 12** | 82.1 → 🔴 ** 31.9** (`-50.2`) | `-50.2 pkt` | 6.33 Er | 0.1% | 1.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 8 → 1** | 82.1 → 🔴 ** 16.8** (`-65.3`) | `-65.3 pkt` | 3.16 Er | 0.1% | 1.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 8 → 16** | 82.1 → 🔴 ** 34.3** (`-47.8`) | `-47.8 pkt` | 6.37 Er | 0.5% | 1.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)

| Badany Wariant / Modyfikator L4 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kronika Dziejów: całkowite wyłączenie** | 82.1 → 🟠 ** 73.5** (`-8.6`) | `-8.6 pkt` | 6.06 Er | 0.2% | 1.8% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Inkwizytor Patrol: ruch 1 → 0 (wyłączenie)** | 82.1 → 🔴 ** 25.3** (`-56.8`) | `-56.8 pkt` | 8.99 Er | 27.2% | 0.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Szlak Morski: era 4 → nigdy (99)** | 82.1 → 🟡 ** 80.4** (`-1.7`) | `-1.7 pkt` | 6.05 Er | 0.2% | 1.4% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |

---

## 5. 👥 Warstwa IV — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych. Kolumna win share to HUD kanonu; setup+witalność to stary blend (kara martwej ścieżki).

| Nieobecna Frakcja | Setup Testowy | Win share | Setup+witalność | Diagnoza |
| :--- | :--- | :---: | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`83.0`** | `83.0` | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`88.5`** | `88.5` | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`84.2`** | `84.2` | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`80.1`** | `80.1` | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`74.6`** | `74.6` | Brak presji stosów i bezpośredniego Inkwizytora |