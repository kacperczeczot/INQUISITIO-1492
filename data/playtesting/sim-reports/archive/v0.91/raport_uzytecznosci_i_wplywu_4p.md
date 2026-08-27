[Strona główna](../../../../../README.md) > [v0.91](README.md) > [raport_uzytecznosci_i_wplywu_4p](raport_uzytecznosci_i_wplywu_4p.md)

---

# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v0.91

**Wersja Gry:** `v0.91` | **Data Badania:** 2026-08-17 14:37 | **Próba:** 5000 gier/setup (25000 gier na wariant) | **Ziarno:** 42
**4P Score (win share):** 🟡 ** 86.6** pkt | **Witalność (osobna kara):** `1.200` | **Śr. Er:** `5.96` | **Deadlocki:** `1.1%` | **Pas Biedy:** `5.5%`
**Udziały 4P:** CAA 21.3% · GC 25.4% · KB 26.5% · KT 25.8% · SO 25.9%

Klasyfikacja L1/L2/L4 i Δ 4P liczą wyłącznie równość win share (`calculate_balance_score`). Kara witalności jest osobno.

**Ostrzeżenia witalności (nie w 4P Score):**
- 4p-core: Martwa ścieżka skazania (swiete-oficjum): 19/1264 wygranych (<8%) — gra tylko stosy
- 4p-no-cienie: Martwa ścieżka skazania (swiete-oficjum): 35/1237 wygranych (<8%) — gra tylko stosy
- 4p-no-kabala: Martwa ścieżka skazania (swiete-oficjum): 39/1316 wygranych (<8%) — gra tylko stosy
- 4p-no-korona: Martwa ścieżka skazania (swiete-oficjum): 39/1291 wygranych (<8%) — gra tylko stosy

---

## 0. Wady z tej próby (nie HUD win share)

Kubełki klasyfikatora i ostrzeżenia witalności z bieżącego runu.

- **swiete-oficjum: ścieżka skazania uśpiona (19/1264; gra tylko stosy)** — kara witalności `1.200`
- **Share |Δ| ≥ 2.5 pp od 25%:** CAA 21.3%
- **Autopodatek (SELF_HARM):** 24/60
- **SELF_HARM z Δ4P ≥ 1.2:** `caa-09` Δ4P +6.5, `caa-02` Δ4P +6.0, `caa-12` Δ4P +5.5, `caa-08` Δ4P +5.4, `caa-07` Δ4P +4.5
- **DEAD_WEIGHT:** `so-10` Oczyść Miasto
- **Karty Kroniki |Δ4P| ≤ 0.8:** 8/8
- **Ablacja całej Kroniki (`L4_NO_TIME_DECK`):** Δ4P -42.4 (STABILIZER)
- **Mechaniki DEAD:** Święte Oficjum: skazania 3 → 6; Szlak Morski: era 4 → nigdy (99)

---

## 1. 🗺️ Podsumowanie Ekosystemu Kart Kanonu 4P (Matryca Wpływu Kart, 60 kart)

Rozkład wszystkich 60 kart frakcyjnych w matrycy **Wpływ na Frakcję ($\Delta \text{Share}$)** vs **Wpływ na Kanon 4P ($\Delta \text{4P Score}$)**:

| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |
| :--- | :---: | :---: | :--- | :--- |
| 🩸 **Autopodatek (Self-Harm)** | **24** | 40.0% | Wyłączenie **podnosi** win share własnej frakcji — karta jest haraczem, nie silnikiem | **Rework / osłabienie kosztu, nie filar** |
| 💤 **Karta Pasywna (Dead Weight)** | **1** | 1.7% | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia lub wycięcia** |
| ⚠️ **Karta Destabilizująca (Disruptor)** | **1** | 1.7% | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |
| ⚖️ **Zbalansowane Narzędzie** | **7** | 11.7% | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Narzędzie, nie złoty środek całego kanonu** |
| 👑 / ⚓ **Filar / Kotwica Kanonu** | **27** | 45.0% | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |

---

## 2. 🃏 Warstwa I — Szczegółowa Analiza 60 Kart Frakcji w Kanonie 4P

### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)
Karty, których brak powoduje spadek wyniku Kanonu 4P o $\ge 4.0$ pkt lub załamanie winrate frakcji o $\ge 4.0\%$ — **bez** autopodatków (te są w 2.1b):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kb-09` **Dekret Królewski** | Korona & Borgiowie | 3zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 26.5% → **1.1%** | **`-25.4%`** | 86.6 → **33.1 pkt** (`-53.5`) |
| `kb-10` **Pieczęć Korony** | Korona & Borgiowie | 2zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 26.5% → **3.2%** | **`-23.3%`** | 86.6 → **36.1 pkt** (`-50.5`) |
| `kt-05` **Wskazówka Cyklu** | Kabała z Toledo | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.8% → **10.7%** | **`-15.1%`** | 86.6 → **48.9 pkt** (`-37.7`) |
| `gc-06` **Szantaż** | Gildia Cieni | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.4% → **13.8%** | **`-11.6%`** | 86.6 → **57.5 pkt** (`-29.1`) |
| `gc-09` **Lista Dłużników** | Gildia Cieni | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.4% → **14.5%** | **`-10.9%`** | 86.6 → **58.2 pkt** (`-28.4`) |
| `kb-02` **Pobór Podatków** | Korona & Borgiowie | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 26.5% → **14.3%** | **`-12.2%`** | 86.6 → **59.8 pkt** (`-26.8`) |
| `caa-10` **Echo Alhambry** | Cienie Al-Andalus | 1zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 21.3% → **15.7%** | **`-5.6%`** | 86.6 → **67.8 pkt** (`-18.8`) |
| `caa-05` **Ukryty Kurier** | Cienie Al-Andalus | 0zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 21.3% → **16.3%** | **`-5.0%`** | 86.6 → **69.5 pkt** (`-17.1`) |
| `caa-03` **Cień na Rynku** | Cienie Al-Andalus | 0zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 21.3% → **19.1%** | **`-2.2%`** | 86.6 → **78.1 pkt** (`-8.5`) |
| `caa-06` **Ucieczka z Lochów** | Cienie Al-Andalus | 2zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 21.3% → **19.5%** | **`-1.8%`** | 86.6 → **79.0 pkt** (`-7.6`) |
| `kt-06` **Przesłuchanie Imienia** | Kabała z Toledo | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 25.8% → **22.6%** | **`-3.2%`** | 86.6 → **79.3 pkt** (`-7.3`) |
| `kb-03` **Plotka Dworska** | Korona & Borgiowie | 1zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 26.5% → **23.6%** | **`-2.9%`** | 86.6 → **81.1 pkt** (`-5.5`) |
| `kb-01` **Rozkaz Dworu** | Korona & Borgiowie | 1zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 26.5% → **23.2%** | **`-3.3%`** | 86.6 → **81.2 pkt** (`-5.4`) |
| `caa-01` **Przejście Podziemiami** | Cienie Al-Andalus | 0zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 21.3% → **20.0%** | **`-1.3%`** | 86.6 → **81.5 pkt** (`-5.1`) |
| `gc-10` **Upadek Domu** | Gildia Cieni | 4zł / 2☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.4% → **26.1%** | **`+0.7%`** | 86.6 → **81.7 pkt** (`-4.9`) |
| `gc-11` **Fałszywe Świadectwo Cechu** | Gildia Cieni | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.4% → **26.2%** | **`+0.8%`** | 86.6 → **82.2 pkt** (`-4.4`) |
| `so-06` **Areszt Trybunalski** | Święte Oficjum | 2zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.9% → **27.0%** | **`+1.1%`** | 86.6 → **82.2 pkt** (`-4.4`) |
| `kb-11` **Tajny Emisariusz** | Korona & Borgiowie | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 26.5% → **23.0%** | **`-3.5%`** | 86.6 → **82.3 pkt** (`-4.3`) |
| `kt-10` **Pieczęć Salomona** | Kabała z Toledo | 2zł / 1☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.8% → **26.8%** | **`+1.0%`** | 86.6 → **83.2 pkt** (`-3.4`) |
| `caa-11` **Nocna Zmiana Warty** | Cienie Al-Andalus | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 21.3% → **20.9%** | **`-0.4%`** | 86.6 → **83.3 pkt** (`-3.3`) |
| `gc-03` **Podrzucenie Księgi** | Gildia Cieni | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.4% → **26.2%** | **`+0.8%`** | 86.6 → **83.3 pkt** (`-3.3`) |
| `so-04` **Publiczne Ostrzeżenie** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.9% → **26.9%** | **`+1.0%`** | 86.6 → **83.4 pkt** (`-3.2`) |
| `kb-12` **Szantaż Salonowy** | Korona & Borgiowie | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 26.5% → **28.3%** | **`+1.8%`** | 86.6 → **83.5 pkt** (`-3.1`) |
| `so-12` **Straż Trybunalska** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.9% → **26.9%** | **`+1.0%`** | 86.6 → **83.7 pkt** (`-2.9`) |
| `so-08` **Nasłanie Inkwizytora** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.9% → **26.9%** | **`+1.0%`** | 86.6 → **83.7 pkt** (`-2.9`) |
| `so-01` **Patrol Familiariuszy** | Święte Oficjum | 1zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.9% → **27.0%** | **`+1.1%`** | 86.6 → **83.8 pkt** (`-2.8`) |
| `gc-08` **Zatrute Złoto** | Gildia Cieni | 2zł / 0☣ | ⚓ KOTWICA KANONU (Balance Anchor) | 25.4% → **26.5%** | **`+1.1%`** | 86.6 → **84.3 pkt** (`-2.3`) |

### 2.1b. 🩸 Autopodatek Frakcji (Self-Harm)
Karty, których wyłączenie **podnosi** win share własnej frakcji. Gracz zauważy je jako haracz, nawet gdy stół 4P jest równy dzięki temu haraczowi.

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kb-04` **Faworyt Dworu** | Korona & Borgiowie | 2zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 26.5% → **43.4%** | **`+16.9%`** | 86.6 → **44.9 pkt** (`-41.7`) |
| `kb-05` **List Żelazny** | Korona & Borgiowie | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 26.5% → **41.9%** | **`+15.4%`** | 86.6 → **47.8 pkt** (`-38.8`) |
| `kb-07` **Szantaż Pieczęcią** | Korona & Borgiowie | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 26.5% → **40.0%** | **`+13.5%`** | 86.6 → **51.9 pkt** (`-34.7`) |
| `kb-08` **Przekupstwo Sędziego** | Korona & Borgiowie | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 26.5% → **40.0%** | **`+13.5%`** | 86.6 → **51.9 pkt** (`-34.7`) |
| `kt-12` **Strażnik Archiwum** | Kabała z Toledo | 0zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.8% → **31.5%** | **`+5.7%`** | 86.6 → **73.4 pkt** (`-13.2`) |
| `kt-02` **Transmutacja Złota** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.8% → **31.0%** | **`+5.2%`** | 86.6 → **74.4 pkt** (`-12.2`) |
| `kt-07` **Archiwum Ukryte** | Kabała z Toledo | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.8% → **30.9%** | **`+5.1%`** | 86.6 → **74.9 pkt** (`-11.7`) |
| `kt-04` **Zwierciadło Herezji** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.8% → **30.8%** | **`+5.0%`** | 86.6 → **74.6 pkt** (`-12.0`) |
| `caa-12` **Skrytka w Murach** | Cienie Al-Andalus | 0zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 21.3% → **26.2%** | **`+4.9%`** | 86.6 → **92.1 pkt** (`5.5`) |
| `gc-12` **Złodziejski Zwiad** | Gildia Cieni | 0zł / 2☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.4% → **30.3%** | **`+4.9%`** | 86.6 → **75.7 pkt** (`-10.9`) |
| `kt-11` **Medytacja Sefirot** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.8% → **30.6%** | **`+4.8%`** | 86.6 → **76.3 pkt** (`-10.3`) |
| `kt-01` **Rytuał Przejścia** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.8% → **30.2%** | **`+4.4%`** | 86.6 → **76.7 pkt** (`-9.9`) |
| `kt-03` **Zakazana Wiedza** | Kabała z Toledo | 0zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.8% → **29.7%** | **`+3.9%`** | 86.6 → **78.1 pkt** (`-8.5`) |
| `caa-09` **Kurier Relikwii** | Cienie Al-Andalus | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 21.3% → **24.6%** | **`+3.3%`** | 86.6 → **93.1 pkt** (`6.5`) |
| `gc-07` **Skrytobójstwo** | Gildia Cieni | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.4% → **28.5%** | **`+3.1%`** | 86.6 → **81.2 pkt** (`-5.4`) |
| `caa-02` **Złoto z Kryjówki** | Cienie Al-Andalus | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 21.3% → **24.2%** | **`+2.9%`** | 86.6 → **92.6 pkt** (`6.0`) |
| `gc-04` **Informator** | Gildia Cieni | 0zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.4% → **28.3%** | **`+2.9%`** | 86.6 → **81.0 pkt** (`-5.6`) |
| `gc-01` **Przekupiony Strażnik** | Gildia Cieni | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.4% → **28.3%** | **`+2.9%`** | 86.6 → **81.8 pkt** (`-4.8`) |
| `caa-08` **Kaptur Nocy** | Cienie Al-Andalus | 2zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 21.3% → **24.0%** | **`+2.7%`** | 86.6 → **92.0 pkt** (`5.4`) |
| `gc-02` **Czarny Rynek** | Gildia Cieni | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.4% → **28.1%** | **`+2.7%`** | 86.6 → **82.0 pkt** (`-4.6`) |
| `kt-08` **Areszt Wiedzy** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 25.8% → **28.4%** | **`+2.6%`** | 86.6 → **81.6 pkt** (`-5.0`) |
| `caa-07` **Szantaż Bractwa** | Cienie Al-Andalus | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 21.3% → **23.6%** | **`+2.3%`** | 86.6 → **91.1 pkt** (`4.5`) |
| `kb-06` **Areszt Królewski** | Korona & Borgiowie | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 26.5% → **28.8%** | **`+2.3%`** | 86.6 → **82.1 pkt** (`-4.5`) |
| `caa-04` **Fałszywy Trop** | Cienie Al-Andalus | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 21.3% → **23.4%** | **`+2.1%`** | 86.6 → **87.5 pkt** (`0.9`) |

### 2.2. ⚠️ Karty Destabilizujące Kanon 4P (Disruptors)
Karty, których wyłączenie podnosi 4P Score ($\Delta \text{4P} \ge +1.5$ pkt):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `so-02` **Skarbiec Trybunału** | Święte Oficjum | 1zł / 0☣ | ⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor) | 25.9% → **25.5%** | `-0.4%` | 86.6 → **89.0 pkt** (`+2.4`) |

### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich 60 Kart Frakcji w Kanonie 4P

| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Faction Win Share 4P | $\Delta$ Frakcji | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `caa-01` | **Przejście Podziemiami** | Cienie Al-Andalus | 0 | 0 | 21.3% → 20.0% | `-1.3%` | 81.5 | `-5.1` | 5.97 | 1.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-03` | **Cień na Rynku** | Cienie Al-Andalus | 0 | 1 | 21.3% → 19.1% | `-2.2%` | 78.1 | `-8.5` | 6.17 | 1.4% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-05` | **Ukryty Kurier** | Cienie Al-Andalus | 0 | 0 | 21.3% → 16.3% | `-5.0%` | 69.5 | `-17.1` | 6.01 | 1.2% | 👑 FILAR KANONU (Core Keystone) |
| `caa-12` | **Skrytka w Murach** | Cienie Al-Andalus | 0 | 1 | 21.3% → 26.2% | `+4.9%` | 92.1 | `+5.5` | 5.91 | 1.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-02` | **Złoto z Kryjówki** | Cienie Al-Andalus | 1 | 0 | 21.3% → 24.2% | `+2.9%` | 92.6 | `+6.0` | 5.85 | 1.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-04` | **Fałszywy Trop** | Cienie Al-Andalus | 1 | 0 | 21.3% → 23.4% | `+2.1%` | 87.5 | `+0.9` | 5.90 | 1.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-07` | **Szantaż Bractwa** | Cienie Al-Andalus | 1 | 0 | 21.3% → 23.6% | `+2.3%` | 91.1 | `+4.5` | 5.88 | 1.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-11` | **Nocna Zmiana Warty** | Cienie Al-Andalus | 1 | 0 | 21.3% → 20.9% | `-0.4%` | 83.3 | `-3.3` | 5.96 | 1.2% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-06` | **Ucieczka z Lochów** | Cienie Al-Andalus | 2 | 1 | 21.3% → 19.5% | `-1.8%` | 79.0 | `-7.6` | 5.98 | 1.3% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `caa-08` | **Kaptur Nocy** | Cienie Al-Andalus | 2 | 1 | 21.3% → 24.0% | `+2.7%` | 92.0 | `+5.4` | 5.88 | 0.9% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-10` | **Echo Alhambry** | Cienie Al-Andalus | 1 | 1 | 21.3% → 15.7% | `-5.6%` | 67.8 | `-18.8` | 6.30 | 1.6% | 👑 FILAR KANONU (Core Keystone) |
| `caa-09` | **Kurier Relikwii** | Cienie Al-Andalus | 2 | 0 | 21.3% → 24.6% | `+3.3%` | 93.1 | `+6.5` | 5.87 | 1.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `gc-04` | **Informator** | Gildia Cieni | 0 | 1 | 25.4% → 28.3% | `+2.9%` | 81.0 | `-5.6` | 5.89 | 1.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `gc-05` | **Fałszywy Świadek** | Gildia Cieni | 0 | 0 | 25.4% → 26.7% | `+1.3%` | 85.6 | `-1.0` | 5.93 | 1.1% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `gc-12` | **Złodziejski Zwiad** | Gildia Cieni | 0 | 2 | 25.4% → 30.3% | `+4.9%` | 75.7 | `-10.9` | 5.88 | 1.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `gc-01` | **Przekupiony Strażnik** | Gildia Cieni | 1 | 1 | 25.4% → 28.3% | `+2.9%` | 81.8 | `-4.8` | 5.90 | 1.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `gc-02` | **Czarny Rynek** | Gildia Cieni | 1 | 1 | 25.4% → 28.1% | `+2.7%` | 82.0 | `-4.6` | 5.92 | 1.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `gc-03` | **Podrzucenie Księgi** | Gildia Cieni | 1 | 0 | 25.4% → 26.2% | `+0.8%` | 83.3 | `-3.3` | 5.93 | 1.2% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-11` | **Fałszywe Świadectwo Cechu** | Gildia Cieni | 1 | 0 | 25.4% → 26.2% | `+0.8%` | 82.2 | `-4.4` | 5.94 | 1.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-06` | **Szantaż** | Gildia Cieni | 2 | 0 | 25.4% → 13.8% | `-11.6%` | 57.5 | `-29.1` | 6.18 | 1.6% | 👑 FILAR KANONU (Core Keystone) |
| `gc-07` | **Skrytobójstwo** | Gildia Cieni | 2 | 0 | 25.4% → 28.5% | `+3.1%` | 81.2 | `-5.4` | 5.89 | 1.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `gc-08` | **Zatrute Złoto** | Gildia Cieni | 2 | 0 | 25.4% → 26.5% | `+1.1%` | 84.3 | `-2.3` | 5.93 | 1.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `gc-09` | **Lista Dłużników** | Gildia Cieni | 2 | 0 | 25.4% → 14.5% | `-10.9%` | 58.2 | `-28.4` | 6.18 | 1.5% | 👑 FILAR KANONU (Core Keystone) |
| `gc-10` | **Upadek Domu** | Gildia Cieni | 4 | 2 | 25.4% → 26.1% | `+0.7%` | 81.7 | `-4.9` | 6.02 | 1.2% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kb-01` | **Rozkaz Dworu** | Korona & Borgiowie | 1 | 1 | 26.5% → 23.2% | `-3.3%` | 81.2 | `-5.4` | 6.05 | 1.2% | 👑 FILAR KANONU (Core Keystone) |
| `kb-02` | **Pobór Podatków** | Korona & Borgiowie | 1 | 0 | 26.5% → 14.3% | `-12.2%` | 59.8 | `-26.8` | 6.26 | 2.0% | 👑 FILAR KANONU (Core Keystone) |
| `kb-03` | **Plotka Dworska** | Korona & Borgiowie | 1 | 1 | 26.5% → 23.6% | `-2.9%` | 81.1 | `-5.5` | 6.01 | 1.2% | 👑 FILAR KANONU (Core Keystone) |
| `kb-11` | **Tajny Emisariusz** | Korona & Borgiowie | 1 | 0 | 26.5% → 23.0% | `-3.5%` | 82.3 | `-4.3` | 6.03 | 1.3% | 👑 FILAR KANONU (Core Keystone) |
| `kb-04` | **Faworyt Dworu** | Korona & Borgiowie | 2 | 1 | 26.5% → 43.4% | `+16.9%` | 44.9 | `-41.7` | 5.60 | 0.6% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-05` | **List Żelazny** | Korona & Borgiowie | 2 | 0 | 26.5% → 41.9% | `+15.4%` | 47.8 | `-38.8` | 5.55 | 0.5% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-06` | **Areszt Królewski** | Korona & Borgiowie | 1 | 0 | 26.5% → 28.8% | `+2.3%` | 82.1 | `-4.5` | 5.91 | 1.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-12` | **Szantaż Salonowy** | Korona & Borgiowie | 1 | 0 | 26.5% → 28.3% | `+1.8%` | 83.5 | `-3.1` | 5.89 | 1.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `kb-07` | **Szantaż Pieczęcią** | Korona & Borgiowie | 2 | 0 | 26.5% → 40.0% | `+13.5%` | 51.9 | `-34.7` | 5.67 | 0.5% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-08` | **Przekupstwo Sędziego** | Korona & Borgiowie | 2 | 0 | 26.5% → 40.0% | `+13.5%` | 51.9 | `-34.7` | 5.67 | 0.5% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-10` | **Pieczęć Korony** | Korona & Borgiowie | 2 | 2 | 26.5% → 3.2% | `-23.3%` | 36.1 | `-50.5` | 6.56 | 2.3% | 👑 FILAR KANONU (Core Keystone) |
| `kb-09` | **Dekret Królewski** | Korona & Borgiowie | 3 | 1 | 26.5% → 1.1% | `-25.4%` | 33.1 | `-53.5` | 6.53 | 2.8% | 👑 FILAR KANONU (Core Keystone) |
| `kt-03` | **Zakazana Wiedza** | Kabała z Toledo | 0 | 1 | 25.8% → 29.7% | `+3.9%` | 78.1 | `-8.5` | 5.98 | 1.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-12` | **Strażnik Archiwum** | Kabała z Toledo | 0 | 1 | 25.8% → 31.5% | `+5.7%` | 73.4 | `-13.2` | 5.86 | 1.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-01` | **Rytuał Przejścia** | Kabała z Toledo | 1 | 0 | 25.8% → 30.2% | `+4.4%` | 76.7 | `-9.9` | 5.86 | 1.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-02` | **Transmutacja Złota** | Kabała z Toledo | 1 | 0 | 25.8% → 31.0% | `+5.2%` | 74.4 | `-12.2` | 5.87 | 1.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-04` | **Zwierciadło Herezji** | Kabała z Toledo | 1 | 0 | 25.8% → 30.8% | `+5.0%` | 74.6 | `-12.0` | 5.88 | 1.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-05` | **Wskazówka Cyklu** | Kabała z Toledo | 1 | 0 | 25.8% → 10.7% | `-15.1%` | 48.9 | `-37.7` | 6.26 | 2.6% | 👑 FILAR KANONU (Core Keystone) |
| `kt-07` | **Archiwum Ukryte** | Kabała z Toledo | 1 | 1 | 25.8% → 30.9% | `+5.1%` | 74.9 | `-11.7` | 5.88 | 1.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-08` | **Areszt Wiedzy** | Kabała z Toledo | 1 | 0 | 25.8% → 28.4% | `+2.6%` | 81.6 | `-5.0` | 5.88 | 1.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-11` | **Medytacja Sefirot** | Kabała z Toledo | 1 | 0 | 25.8% → 30.6% | `+4.8%` | 76.3 | `-10.3` | 5.86 | 1.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-06` | **Przesłuchanie Imienia** | Kabała z Toledo | 2 | 0 | 25.8% → 22.6% | `-3.2%` | 79.3 | `-7.3` | 6.01 | 1.6% | 👑 FILAR KANONU (Core Keystone) |
| `kt-09` | **Fragment Kodeksu** | Kabała z Toledo | 2 | 1 | 25.8% → 25.9% | `+0.1%` | 85.3 | `-1.3` | 6.00 | 1.2% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-10` | **Pieczęć Salomona** | Kabała z Toledo | 2 | 1 | 25.8% → 26.8% | `+1.0%` | 83.2 | `-3.4` | 6.03 | 1.2% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-05` | **Wezwanie do Trybunału** | Święte Oficjum | 0 | 0 | 25.9% → 24.5% | `-1.4%` | 86.5 | `-0.1` | 6.00 | 1.2% | ⚡ MOTOR FRAKCJI (Offensive Engine) |
| `so-01` | **Patrol Familiariuszy** | Święte Oficjum | 1 | 0 | 25.9% → 27.0% | `+1.1%` | 83.8 | `-2.8` | 5.96 | 1.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-02` | **Skarbiec Trybunału** | Święte Oficjum | 1 | 0 | 25.9% → 25.5% | `-0.4%` | 89.0 | `+2.4` | 6.01 | 1.3% | ⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor) |
| `so-04` | **Publiczne Ostrzeżenie** | Święte Oficjum | 1 | 0 | 25.9% → 26.9% | `+1.0%` | 83.4 | `-3.2` | 5.99 | 1.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-12` | **Straż Trybunalska** | Święte Oficjum | 1 | 0 | 25.9% → 26.9% | `+1.0%` | 83.7 | `-2.9` | 5.95 | 1.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-03` | **Podejrzenie** | Święte Oficjum | 2 | 0 | 25.9% → 25.9% | `+0.0%` | 85.4 | `-1.2` | 5.99 | 1.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-08` | **Nasłanie Inkwizytora** | Święte Oficjum | 1 | 0 | 25.9% → 26.9% | `+1.0%` | 83.7 | `-2.9` | 5.97 | 1.1% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-11` | **Dekret Czystości Wiary** | Święte Oficjum | 1 | 0 | 25.9% → 24.6% | `-1.3%` | 86.8 | `+0.2` | 5.99 | 1.2% | ⚡ MOTOR FRAKCJI (Offensive Engine) |
| `so-06` | **Areszt Trybunalski** | Święte Oficjum | 2 | 0 | 25.9% → 27.0% | `+1.1%` | 82.2 | `-4.4` | 5.91 | 1.0% | ⚓ KOTWICA KANONU (Balance Anchor) |
| `so-07` | **Przesłuchanie Oficjum** | Święte Oficjum | 2 | 0 | 25.9% → 26.4% | `+0.5%` | 86.1 | `-0.5` | 5.96 | 1.1% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-09` | **Świadek Koronny** | Święte Oficjum | 2 | 0 | 25.9% → 26.7% | `+0.8%` | 85.0 | `-1.6` | 5.94 | 1.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-10` | **Oczyść Miasto** | Święte Oficjum | 5 | 2 | 25.9% → 26.0% | `+0.1%` | 86.4 | `-0.2` | 5.97 | 1.2% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |

---

## 3. ⏳ Warstwa II — Kronika Dziejów w 4P (Ablacja 8 Kart Wydarzeń Czasu)

Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans w 4P:

| ID | Karta Wydarzenia | 4P Score | $\Delta$ 4P | Średnia Er | Deadlock % | Status Roli w Kronice |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `tc-01` | **Kres Średniowiecza** | 🟡 ** 86.6** | `0.0 pkt` | 5.96 Er | 1.1% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-02` | **Płonący Stos** | 🟡 ** 86.6** | `0.0 pkt` | 5.96 Er | 1.1% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-03` | **Królewski Podatek** | 🟡 ** 86.6** | `0.0 pkt` | 5.96 Er | 1.1% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-04` | **Spisek w Cieniu** | 🟡 ** 86.6** | `0.0 pkt` | 5.96 Er | 1.1% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-05` | **Złoty Wiek** | 🟡 ** 86.6** | `0.0 pkt` | 5.96 Er | 1.1% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-06` | **Czystka w Mieście** | 🟡 ** 86.6** | `0.0 pkt` | 5.96 Er | 1.1% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-07` | **Druga Szansa** | 🟡 ** 86.6** | `0.0 pkt` | 5.96 Er | 1.1% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-08` | **Zaćmienie Słońca** | 🟡 ** 86.6** | `0.0 pkt` | 5.96 Er | 1.1% | 💤 Martwa karta kroniki (Δ≈0) |

---

## 4. ⚙️ Warstwa III — Matryca 9 Obszarów Wpływu Mechanik Gry (L1, L2, L4)

Mechaniki w tym raporcie: **skraj albo wyłączenie**. Testy ±1 są w `audit_level1` / `audit_level2` / `audit_level4`. **Δ≈0 nie jest harmonią.**

| Kategoria Mechaniki | Liczba Testów | Rola w Ekosystemie Kanonu 4P | Rekomendacja Balansowa |
| :--- | :---: | :--- | :--- |
| 👑 / 🛡️ **Filary i Bezpieczniki** | **29** | Ablacja wali w stół — gracze czują tę gałkę | **Cel kanonu** |
| ⚠️ **Za słabe dźwignie** | **0** | Rusza share, nie trzyma stołu — nie jest „zbalansowana” | **Wzmocnić aż będzie filarem** |
| 💤 **Martwe / uśpione ścieżki** | **3** | Dual-win z witalności albo ablacja Δ≈0 | Wada pomiaru, nie harmonia |
| ⚠️ / 💡 **Wady bieżącej wartości** | **0** | Inna wartość gałki **podnosi** 4P — obecny setting szkodzi | **Przekręcić albo rework** |

### 4.0. 💤 Martwe mechaniki (osobny wykaz)
Ścieżki dual-win z `evaluate_vitality` oraz testy z $|\Delta\text{4P}| \le 0.8$ i ruchem share $\le 1.5$ pp.

| Badany Podsystem | Kategoria | 4P Score | $\Delta$ 4P | Klasyfikacja |
| :--- | :--- | :---: | :---: | :--- |
| **Szlak Morski: era 4 → nigdy (99)** | Poziom 4: Warianty i Modyfikatory | 🟡 ** 86.6** | `0.0 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **swiete-oficjum: ścieżka skazania uśpiona (19/1264; gra tylko stosy)** | Poziom 2: Warunki Zwycięstwa | 🟡 ** 86.6** | `0.0 pkt` | 💤 UŚPIONA ŚCIEŻKA ZWYCIĘSTWA |
| **Święte Oficjum: skazania 3 → 6** | Poziom 2: Warunki Zwycięstwa | 🟡 ** 86.6** | `0.0 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |

### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)

| Badany Podsystem / Modyfikator L1 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Limit Er: 12 → 6 (skrajna presja)** | 86.6 → 🔴 ** 44.7** (`-41.9`) | `-41.9 pkt` | 5.13 Er | 63.5% | 5.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Oskarżenia: 7 → 1** | 86.6 → 🔴 **  5.3** (`-81.3`) | `-81.3 pkt` | 5.22 Er | 4.4% | 2.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Oskarżenia: 7 → 14** | 86.6 → 🔴 **  9.5** (`-77.1`) | `-77.1 pkt` | 6.21 Er | 2.4% | 8.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 0zł (wyłączenie)** | 86.6 → 🔴 ** 39.3** (`-47.3`) | `-47.3 pkt` | 6.96 Er | 4.1% | 18.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 8zł** | 86.6 → 🔴 ** 25.3** (`-61.3`) | `-61.3 pkt` | 4.91 Er | 0.3% | 1.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 1** | 86.6 → 🔴 ** 54.7** (`-31.9`) | `-31.9 pkt` | 6.94 Er | 4.9% | 5.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 6** | 86.6 → 🔴 ** 35.4** (`-51.2`) | `-51.2 pkt` | 5.53 Er | 0.6% | 5.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 1** | 86.6 → 🔴 ** 52.3** (`-34.3`) | `-34.3 pkt` | 7.55 Er | 6.9% | 24.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 10** | 86.6 → 🔴 ** 40.3** (`-46.3`) | `-46.3 pkt` | 5.34 Er | 0.9% | 6.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: cooldown 3 → 0 (co erę)** | 86.6 → 🔴 ** 25.0** (`-61.6`) | `-61.6 pkt` | 5.22 Er | 0.9% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: całkowite wyłączenie** | 86.6 → 🔴 ** 31.8** (`-54.8`) | `-54.8 pkt` | 6.43 Er | 2.8% | 4.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)

| Badany Warunek Zwycięstwa L2 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **swiete-oficjum: ścieżka skazania uśpiona (19/1264; gra tylko stosy)** | 🟡 ** 86.6** | `0.0 pkt` | 5.96 Er | 1.1% | 5.5% | 💤 UŚPIONA ŚCIEŻKA ZWYCIĘSTWA |
| **Święte Oficjum: stosy 5 → 1** | 86.6 → 🔴 ** 16.2** (`-70.4`) | `-70.4 pkt` | 3.72 Er | 0.3% | 4.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: stosy 5 → 10** | 86.6 → 🔴 ** 38.2** (`-48.4`) | `-48.4 pkt` | 6.26 Er | 3.5% | 5.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 1** | 86.6 → 🔴 ** 16.7** (`-69.9`) | `-69.9 pkt` | 4.08 Er | 0.3% | 5.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 6** | 🟡 ** 86.6** | `0.0 pkt` | 5.96 Er | 1.2% | 5.5% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Cienie: relikwie 2 → 4** | 86.6 → 🔴 ** 34.4** (`-52.2`) | `-52.2 pkt` | 6.47 Er | 1.8% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: dekrety 2 → 4** | 86.6 → 🔴 ** 33.3** (`-53.3`) | `-53.3 pkt` | 6.48 Er | 2.7% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: haki 0 → 2** | 86.6 → 🟠 ** 68.4** (`-18.2`) | `-18.2 pkt` | 6.22 Er | 1.4% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: fragmenty 3 → 1** | 86.6 → 🔴 ** 33.4** (`-53.2`) | `-53.2 pkt` | 5.48 Er | 0.6% | 5.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: fragmenty 3 → 6** | 86.6 → 🔴 ** 32.4** (`-54.2`) | `-54.2 pkt` | 6.35 Er | 3.0% | 5.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: era 6 → 1** | 86.6 → 🟡 ** 78.1** (`-8.5`) | `-8.5 pkt` | 5.79 Er | 1.1% | 5.4% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Kabała: era 6 → 12** | 86.6 → 🔴 ** 32.5** (`-54.1`) | `-54.1 pkt` | 6.36 Er | 3.2% | 5.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: pasmo 0–9 → 3–5** | 86.6 → 🔴 ** 52.7** (`-33.9`) | `-33.9 pkt` | 6.18 Er | 1.9% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki (z Oficjum) 3 → 1** | 86.6 → 🔴 ** 35.0** (`-51.6`) | `-51.6 pkt` | 4.71 Er | 0.6% | 5.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki (z Oficjum) 3 → 6** | 86.6 → 🔴 ** 43.9** (`-42.7`) | `-42.7 pkt` | 6.33 Er | 1.5% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki (bez Oficjum) 5 → 1** | 86.6 → 🟠 ** 71.3** (`-15.3`) | `-15.3 pkt` | 5.47 Er | 0.8% | 5.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki (bez Oficjum) 5 → 10** | 86.6 → 🟡 ** 75.8** (`-10.8`) | `-10.8 pkt` | 6.08 Er | 1.8% | 5.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |

### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)

| Badany Wariant / Modyfikator L4 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kronika Dziejów: całkowite wyłączenie** | 86.6 → 🔴 ** 44.2** (`-42.4`) | `-42.4 pkt` | 6.36 Er | 2.4% | 6.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Werdykt Sądu: tajny (wyłączenie jawnej koordynacji)** | 86.6 → 🔴 ** 52.8** (`-33.8`) | `-33.8 pkt` | 5.49 Er | 0.4% | 5.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Inkwizytor Patrol: ruch 1 → 0 (wyłączenie)** | 86.6 → 🟠 ** 68.1** (`-18.5`) | `-18.5 pkt` | 6.03 Er | 1.1% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Szlak Morski: era 4 → nigdy (99)** | 🟡 ** 86.6** | `0.0 pkt` | 5.96 Er | 1.1% | 5.5% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |

---

## 5. 👥 Warstwa IV — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych. Kolumna win share to HUD kanonu; setup+witalność to stary blend (kara martwej ścieżki).

| Nieobecna Frakcja | Setup Testowy | Win share | Setup+witalność | Diagnoza |
| :--- | :--- | :---: | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`86.4`** | `26.0` | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`83.9`** | `25.3` | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`90.2`** | `27.2` | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`93.3`** | `28.1` | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`79.1`** | `79.1` | Brak presji stosów i bezpośredniego Inkwizytora |