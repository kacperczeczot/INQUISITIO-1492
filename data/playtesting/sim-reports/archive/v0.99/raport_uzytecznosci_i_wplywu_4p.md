[Strona główna](../../../../../README.md) > [v0.99](README.md) > [raport_uzytecznosci_i_wplywu_4p](raport_uzytecznosci_i_wplywu_4p.md)

---

# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v0.99

**Wersja Gry:** `v0.99` | **Data Badania:** 2026-08-18 00:36 | **Próba:** 5000 gier/setup (25000 gier na wariant) | **Ziarno:** 42
**4P Score (win share):** 🔴 ** 11.2** pkt | **Witalność (osobna kara):** `0.444` | **Śr. Er:** `5.75` | **Deadlocki:** `2.5%` | **Pas Biedy:** `0.9%`
**Udziały 4P:** CAA 7.9% · GC 53.1% · KB 32.7% · KT 8.7% · SO 22.6%

Klasyfikacja L1/L2/L4 i Δ 4P liczą wyłącznie równość win share (`calculate_balance_score`). Kara witalności jest osobno.

**Ostrzeżenia witalności (nie w 4P Score):**
- 4p-core: Paraliż Gry / Deadlocks 9.4% (>5%)

---

## 0. Wady z tej próby (nie HUD win share)

Kubełki klasyfikatora i ostrzeżenia witalności z bieżącego runu.

- **Share |Δ| ≥ 2.5 pp od 25%:** CAA 7.9%, KT 8.7%, KB 32.7%, GC 53.1%
- **Autopodatek (SELF_HARM):** 20/60
- **SELF_HARM z Δ4P ≥ 1.2:** `kt-01` Δ4P +3.0, `kt-02` Δ4P +3.0, `kt-12` Δ4P +2.6, `kt-07` Δ4P +2.6, `kt-08` Δ4P +2.6, `kt-09` Δ4P +2.6, `kt-11` Δ4P +2.5, `kt-04` Δ4P +2.2, `caa-11` Δ4P +1.4
- **DEAD_WEIGHT:** `caa-12` Skrytka w Murach, `caa-09` Kurier Relikwii, `gc-05` Fałszywy Świadek, `so-01` Patrol Familiariuszy, `so-04` Publiczne Ostrzeżenie, `so-12` Straż Trybunalska, `so-03` Podejrzenie, `so-08` Nasłanie Inkwizytora, `so-11` Dekret Czystości Wiary, `so-06` Areszt Trybunalski, `so-07` Przesłuchanie Oficjum, `so-09` Świadek Koronny, `so-10` Oczyść Miasto
- **Karty Kroniki |Δ4P| ≤ 0.8:** 8/8
- **Ablacja całej Kroniki (`L4_NO_TIME_DECK`):** Δ4P -1.6 (WEAK)
- **Mechaniki WEAK/NEUTRAL:** Święte Oficjum: stosy 7 → 14; Święte Oficjum: skazania 3 → 6; Korona: wymóg haków 0 → 2 (podatek); Kabała: era 4 → 1; Kabała: era 4 → 8; Kronika Dziejów: całkowite wyłączenie
- **Mechaniki DEAD:** Szlak Morski: era 4 → nigdy (99)
- **Mechaniki DISRUPTOR:** Limit Er: 12 → 6 (skrajna presja); Złoto startowe: 4zł → 0zł (wyłączenie); Gildia: upadki 7 → 14; Werdykt Sądu: tajny (wyłączenie jawnej koordynacji)

---

## 1. 🗺️ Podsumowanie Ekosystemu Kart Kanonu 4P (Matryca Wpływu Kart, 60 kart)

Rozkład wszystkich 60 kart frakcyjnych w matrycy **Wpływ na Frakcję ($\Delta \text{Share}$)** vs **Wpływ na Kanon 4P ($\Delta \text{4P Score}$)**:

| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |
| :--- | :---: | :---: | :--- | :--- |
| 🩸 **Autopodatek (Self-Harm)** | **20** | 33.3% | Wyłączenie **podnosi** win share własnej frakcji — karta jest haraczem, nie silnikiem | **Rework / osłabienie kosztu, nie filar** |
| 💤 **Karta Pasywna (Dead Weight)** | **13** | 21.7% | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia lub wycięcia** |
| ⚠️ **Karta Destabilizująca (Disruptor)** | **5** | 8.3% | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |
| ⚖️ **Zbalansowane Narzędzie** | **14** | 23.3% | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Narzędzie, nie złoty środek całego kanonu** |
| 👑 / ⚓ **Filar / Kotwica Kanonu** | **8** | 13.3% | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |

---

## 2. 🃏 Warstwa I — Szczegółowa Analiza 60 Kart Frakcji w Kanonie 4P

### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)
Karty, których brak powoduje spadek wyniku Kanonu 4P o $\ge 4.0$ pkt lub załamanie winrate frakcji o $\ge 4.0\%$ — **bez** autopodatków (te są w 2.1b):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kb-10` **Pieczęć Korony** | Korona & Borgiowie | 2zł / 2☣ | 👑 FILAR KANONU (Core Keystone) | 32.7% → **1.4%** | **`-31.3%`** | 11.2 → **3.3 pkt** (`-7.9`) |
| `kb-09` **Dekret Królewski** | Korona & Borgiowie | 3zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 32.7% → **0.0%** | **`-32.7%`** | 11.2 → **3.3 pkt** (`-7.9`) |
| `caa-10` **Echo Alhambry** | Cienie Al-Andalus | 1zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 7.9% → **0.0%** | **`-7.9%`** | 11.2 → **6.7 pkt** (`-4.5`) |
| `kt-10` **Pieczęć Salomona** | Kabała z Toledo | 2zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 8.7% → **0.6%** | **`-8.1%`** | 11.2 → **6.8 pkt** (`-4.4`) |
| `kt-03` **Zakazana Wiedza** | Kabała z Toledo | 0zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 8.7% → **0.5%** | **`-8.2%`** | 11.2 → **7.1 pkt** (`-4.1`) |
| `kt-05` **Wskazówka Cyklu** | Kabała z Toledo | 1zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 8.7% → **0.4%** | **`-8.3%`** | 11.2 → **7.2 pkt** (`-4.0`) |
| `caa-03` **Cień na Rynku** | Cienie Al-Andalus | 0zł / 1☣ | 👑 FILAR KANONU (Core Keystone) | 7.9% → **3.1%** | **`-4.8%`** | 11.2 → **8.1 pkt** (`-3.1`) |
| `kt-06` **Przesłuchanie Imienia** | Kabała z Toledo | 2zł / 0☣ | 👑 FILAR KANONU (Core Keystone) | 8.7% → **4.3%** | **`-4.4%`** | 11.2 → **8.8 pkt** (`-2.4`) |

### 2.1b. 🩸 Autopodatek Frakcji (Self-Harm)
Karty, których wyłączenie **podnosi** win share własnej frakcji. Gracz zauważy je jako haracz, nawet gdy stół 4P jest równy dzięki temu haraczowi.

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kb-04` **Faworyt Dworu** | Korona & Borgiowie | 2zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 32.7% → **46.1%** | **`+13.4%`** | 11.2 → **10.0 pkt** (`-1.2`) |
| `kb-03` **Plotka Dworska** | Korona & Borgiowie | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 32.7% → **39.8%** | **`+7.1%`** | 11.2 → **11.3 pkt** (`0.1`) |
| `kb-01` **Rozkaz Dworu** | Korona & Borgiowie | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 32.7% → **39.7%** | **`+7.0%`** | 11.2 → **11.4 pkt** (`0.2`) |
| `kb-06` **Areszt Królewski** | Korona & Borgiowie | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 32.7% → **39.4%** | **`+6.7%`** | 11.2 → **11.4 pkt** (`0.2`) |
| `kb-11` **Tajny Emisariusz** | Korona & Borgiowie | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 32.7% → **39.2%** | **`+6.5%`** | 11.2 → **11.5 pkt** (`0.3`) |
| `kb-07` **Szantaż Pieczęcią** | Korona & Borgiowie | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 32.7% → **38.3%** | **`+5.6%`** | 11.2 → **11.3 pkt** (`0.1`) |
| `kb-08` **Przekupstwo Sędziego** | Korona & Borgiowie | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 32.7% → **38.3%** | **`+5.6%`** | 11.2 → **11.3 pkt** (`0.1`) |
| `kb-05` **List Żelazny** | Korona & Borgiowie | 2zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 32.7% → **38.1%** | **`+5.4%`** | 11.2 → **10.9 pkt** (`-0.3`) |
| `kb-12` **Szantaż Salonowy** | Korona & Borgiowie | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 32.7% → **38.1%** | **`+5.4%`** | 11.2 → **11.2 pkt** (`0.0`) |
| `kt-01` **Rytuał Przejścia** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 8.7% → **12.9%** | **`+4.2%`** | 11.2 → **14.2 pkt** (`3.0`) |
| `kt-02` **Transmutacja Złota** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 8.7% → **12.9%** | **`+4.2%`** | 11.2 → **14.2 pkt** (`3.0`) |
| `kt-12` **Strażnik Archiwum** | Kabała z Toledo | 0zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 8.7% → **12.4%** | **`+3.7%`** | 11.2 → **13.8 pkt** (`2.6`) |
| `kt-07` **Archiwum Ukryte** | Kabała z Toledo | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 8.7% → **12.4%** | **`+3.7%`** | 11.2 → **13.8 pkt** (`2.6`) |
| `kt-08` **Areszt Wiedzy** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 8.7% → **12.4%** | **`+3.7%`** | 11.2 → **13.8 pkt** (`2.6`) |
| `kt-11` **Medytacja Sefirot** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 8.7% → **12.4%** | **`+3.7%`** | 11.2 → **13.7 pkt** (`2.5`) |
| `kt-09` **Fragment Kodeksu** | Kabała z Toledo | 2zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 8.7% → **12.4%** | **`+3.7%`** | 11.2 → **13.8 pkt** (`2.6`) |
| `kt-04` **Zwierciadło Herezji** | Kabała z Toledo | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 8.7% → **12.1%** | **`+3.4%`** | 11.2 → **13.4 pkt** (`2.2`) |
| `gc-02` **Czarny Rynek** | Gildia Cieni | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 53.1% → **55.9%** | **`+2.8%`** | 11.2 → **9.5 pkt** (`-1.7`) |
| `gc-04` **Informator** | Gildia Cieni | 1zł / 1☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 53.1% → **55.7%** | **`+2.6%`** | 11.2 → **9.6 pkt** (`-1.6`) |
| `caa-11` **Nocna Zmiana Warty** | Cienie Al-Andalus | 1zł / 0☣ | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | 7.9% → **10.0%** | **`+2.1%`** | 11.2 → **12.6 pkt** (`1.4`) |

### 2.2. ⚠️ Karty Destabilizujące Kanon 4P (Disruptors)
Karty, których wyłączenie podnosi 4P Score ($\Delta \text{4P} \ge +1.5$ pkt):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `gc-06` **Szantaż** | Gildia Cieni | 2zł / 0☣ | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) | 53.1% → **47.2%** | `-5.9%` | 11.2 → **14.5 pkt** (`+3.3`) |
| `gc-09` **Lista Dłużników** | Gildia Cieni | 3zł / 0☣ | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) | 53.1% → **47.8%** | `-5.3%` | 11.2 → **14.0 pkt** (`+2.8`) |
| `caa-04` **Fałszywy Trop** | Cienie Al-Andalus | 1zł / 0☣ | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) | 7.9% → **9.7%** | `+1.8%` | 11.2 → **12.7 pkt** (`+1.5`) |
| `caa-07` **Szantaż Bractwa** | Cienie Al-Andalus | 1zł / 0☣ | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) | 7.9% → **9.6%** | `+1.7%` | 11.2 → **12.6 pkt** (`+1.4`) |
| `caa-08` **Kaptur Nocy** | Cienie Al-Andalus | 2zł / 1☣ | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) | 7.9% → **9.6%** | `+1.7%` | 11.2 → **12.6 pkt** (`+1.4`) |

### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich 60 Kart Frakcji w Kanonie 4P

| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Faction Win Share 4P | $\Delta$ Frakcji | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `caa-01` | **Przejście Podziemiami** | Cienie Al-Andalus | 0 | 0 | 7.9% → 9.4% | `+1.5%` | 12.3 | `+1.1` | 5.69 | 2.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `caa-03` | **Cień na Rynku** | Cienie Al-Andalus | 0 | 1 | 7.9% → 3.1% | `-4.8%` | 8.1 | `-3.1` | 5.93 | 2.6% | 👑 FILAR KANONU (Core Keystone) |
| `caa-12` | **Skrytka w Murach** | Cienie Al-Andalus | 0 | 1 | 7.9% → 8.2% | `+0.3%` | 10.9 | `-0.3` | 5.84 | 2.8% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `caa-02` | **Złoto z Kryjówki** | Cienie Al-Andalus | 1 | 0 | 7.9% → 9.4% | `+1.5%` | 12.3 | `+1.1` | 5.69 | 2.0% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `caa-04` | **Fałszywy Trop** | Cienie Al-Andalus | 1 | 0 | 7.9% → 9.7% | `+1.8%` | 12.7 | `+1.5` | 5.69 | 2.2% | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) |
| `caa-05` | **Ukryty Kurier** | Cienie Al-Andalus | 1 | 0 | 7.9% → 6.3% | `-1.6%` | 10.0 | `-1.2` | 5.80 | 2.5% | ⚡ MOTOR FRAKCJI (Offensive Engine) |
| `caa-07` | **Szantaż Bractwa** | Cienie Al-Andalus | 1 | 0 | 7.9% → 9.6% | `+1.7%` | 12.6 | `+1.4` | 5.69 | 2.1% | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) |
| `caa-11` | **Nocna Zmiana Warty** | Cienie Al-Andalus | 1 | 0 | 7.9% → 10.0% | `+2.1%` | 12.6 | `+1.4` | 5.69 | 2.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `caa-06` | **Ucieczka z Lochów** | Cienie Al-Andalus | 2 | 1 | 7.9% → 7.5% | `-0.4%` | 10.5 | `-0.7` | 5.69 | 2.2% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-08` | **Kaptur Nocy** | Cienie Al-Andalus | 2 | 1 | 7.9% → 9.6% | `+1.7%` | 12.6 | `+1.4` | 5.69 | 2.1% | ⚠️ TOKSYCZNY BALAST (Disruptor Self-Harm) |
| `caa-10` | **Echo Alhambry** | Cienie Al-Andalus | 1 | 1 | 7.9% → 0.0% | `-7.9%` | 6.7 | `-4.5` | 6.11 | 3.6% | 👑 FILAR KANONU (Core Keystone) |
| `caa-09` | **Kurier Relikwii** | Cienie Al-Andalus | 2 | 0 | 7.9% → 7.9% | `+0.0%` | 11.3 | `+0.1` | 5.75 | 2.3% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `gc-05` | **Fałszywy Świadek** | Gildia Cieni | 0 | 0 | 53.1% → 53.2% | `+0.1%` | 11.4 | `+0.2` | 5.80 | 2.4% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `gc-12` | **Złodziejski Zwiad** | Gildia Cieni | 0 | 2 | 53.1% → 54.8% | `+1.7%` | 10.3 | `-0.9` | 5.72 | 2.4% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `gc-01` | **Przekupiony Strażnik** | Gildia Cieni | 1 | 1 | 53.1% → 54.2% | `+1.1%` | 10.6 | `-0.6` | 5.74 | 2.4% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `gc-02` | **Czarny Rynek** | Gildia Cieni | 1 | 1 | 53.1% → 55.9% | `+2.8%` | 9.5 | `-1.7` | 5.77 | 2.4% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `gc-03` | **Podrzucenie Księgi** | Gildia Cieni | 1 | 0 | 53.1% → 54.6% | `+1.5%` | 10.5 | `-0.7` | 5.74 | 2.4% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `gc-04` | **Informator** | Gildia Cieni | 1 | 1 | 53.1% → 55.7% | `+2.6%` | 9.6 | `-1.6` | 5.77 | 2.4% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `gc-11` | **Fałszywe Świadectwo Cechu** | Gildia Cieni | 1 | 0 | 53.1% → 54.8% | `+1.7%` | 10.3 | `-0.9` | 5.72 | 2.4% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `gc-06` | **Szantaż** | Gildia Cieni | 2 | 0 | 53.1% → 47.2% | `-5.9%` | 14.5 | `+3.3` | 5.90 | 2.7% | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) |
| `gc-07` | **Skrytobójstwo** | Gildia Cieni | 2 | 0 | 53.1% → 54.7% | `+1.6%` | 10.3 | `-0.9` | 5.74 | 2.4% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `gc-08` | **Zatrute Złoto** | Gildia Cieni | 2 | 0 | 53.1% → 54.7% | `+1.6%` | 10.3 | `-0.9` | 5.74 | 2.4% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `gc-09` | **Lista Dłużników** | Gildia Cieni | 3 | 0 | 53.1% → 47.8% | `-5.3%` | 14.0 | `+2.8` | 5.89 | 2.7% | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) |
| `gc-10` | **Upadek Domu** | Gildia Cieni | 4 | 2 | 53.1% → 55.0% | `+1.9%` | 10.2 | `-1.0` | 5.73 | 2.4% | 🛑 HAMULEC FRAKCJI (Control Tool) |
| `kb-01` | **Rozkaz Dworu** | Korona & Borgiowie | 1 | 1 | 32.7% → 39.7% | `+7.0%` | 11.4 | `+0.2` | 5.54 | 2.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-02` | **Pobór Podatków** | Korona & Borgiowie | 1 | 0 | 32.7% → 33.2% | `+0.5%` | 10.6 | `-0.6` | 5.75 | 2.6% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-03` | **Plotka Dworska** | Korona & Borgiowie | 1 | 1 | 32.7% → 39.8% | `+7.1%` | 11.3 | `+0.1` | 5.53 | 2.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-11` | **Tajny Emisariusz** | Korona & Borgiowie | 1 | 0 | 32.7% → 39.2% | `+6.5%` | 11.5 | `+0.3` | 5.54 | 2.0% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-04` | **Faworyt Dworu** | Korona & Borgiowie | 2 | 1 | 32.7% → 46.1% | `+13.4%` | 10.0 | `-1.2` | 5.35 | 1.8% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-05` | **List Żelazny** | Korona & Borgiowie | 2 | 0 | 32.7% → 38.1% | `+5.4%` | 10.9 | `-0.3` | 5.44 | 2.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-06` | **Areszt Królewski** | Korona & Borgiowie | 1 | 0 | 32.7% → 39.4% | `+6.7%` | 11.4 | `+0.2` | 5.56 | 2.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-12` | **Szantaż Salonowy** | Korona & Borgiowie | 1 | 0 | 32.7% → 38.1% | `+5.4%` | 11.2 | `0.0` | 5.58 | 2.4% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-07` | **Szantaż Pieczęcią** | Korona & Borgiowie | 2 | 0 | 32.7% → 38.3% | `+5.6%` | 11.3 | `+0.1` | 5.57 | 2.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-08` | **Przekupstwo Sędziego** | Korona & Borgiowie | 2 | 0 | 32.7% → 38.3% | `+5.6%` | 11.3 | `+0.1` | 5.57 | 2.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kb-10` | **Pieczęć Korony** | Korona & Borgiowie | 2 | 2 | 32.7% → 1.4% | `-31.3%` | 3.3 | `-7.9` | 6.90 | 4.2% | 👑 FILAR KANONU (Core Keystone) |
| `kb-09` | **Dekret Królewski** | Korona & Borgiowie | 3 | 1 | 32.7% → 0.0% | `-32.7%` | 3.3 | `-7.9` | 6.83 | 3.6% | 👑 FILAR KANONU (Core Keystone) |
| `kt-03` | **Zakazana Wiedza** | Kabała z Toledo | 0 | 1 | 8.7% → 0.5% | `-8.2%` | 7.1 | `-4.1` | 5.99 | 2.9% | 👑 FILAR KANONU (Core Keystone) |
| `kt-12` | **Strażnik Archiwum** | Kabała z Toledo | 0 | 1 | 8.7% → 12.4% | `+3.7%` | 13.8 | `+2.6` | 5.64 | 2.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-01` | **Rytuał Przejścia** | Kabała z Toledo | 1 | 0 | 8.7% → 12.9% | `+4.2%` | 14.2 | `+3.0` | 5.65 | 2.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-02` | **Transmutacja Złota** | Kabała z Toledo | 1 | 0 | 8.7% → 12.9% | `+4.2%` | 14.2 | `+3.0` | 5.65 | 2.2% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-04` | **Zwierciadło Herezji** | Kabała z Toledo | 1 | 0 | 8.7% → 12.1% | `+3.4%` | 13.4 | `+2.2` | 5.65 | 2.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-05` | **Wskazówka Cyklu** | Kabała z Toledo | 1 | 0 | 8.7% → 0.4% | `-8.3%` | 7.2 | `-4.0` | 5.94 | 2.5% | 👑 FILAR KANONU (Core Keystone) |
| `kt-07` | **Archiwum Ukryte** | Kabała z Toledo | 1 | 1 | 8.7% → 12.4% | `+3.7%` | 13.8 | `+2.6` | 5.65 | 2.3% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-08` | **Areszt Wiedzy** | Kabała z Toledo | 1 | 0 | 8.7% → 12.4% | `+3.7%` | 13.8 | `+2.6` | 5.65 | 2.3% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-11` | **Medytacja Sefirot** | Kabała z Toledo | 1 | 0 | 8.7% → 12.4% | `+3.7%` | 13.7 | `+2.5` | 5.64 | 2.1% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-06` | **Przesłuchanie Imienia** | Kabała z Toledo | 2 | 0 | 8.7% → 4.3% | `-4.4%` | 8.8 | `-2.4` | 5.86 | 2.5% | 👑 FILAR KANONU (Core Keystone) |
| `kt-09` | **Fragment Kodeksu** | Kabała z Toledo | 2 | 1 | 8.7% → 12.4% | `+3.7%` | 13.8 | `+2.6` | 5.66 | 2.3% | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) |
| `kt-10` | **Pieczęć Salomona** | Kabała z Toledo | 2 | 1 | 8.7% → 0.6% | `-8.1%` | 6.8 | `-4.4` | 5.99 | 3.1% | 👑 FILAR KANONU (Core Keystone) |
| `so-05` | **Wezwanie do Trybunału** | Święte Oficjum | 0 | 0 | 22.6% → 20.7% | `-1.9%` | 11.2 | `0.0` | 5.66 | 2.3% | ⚡ MOTOR FRAKCJI (Offensive Engine) |
| `so-01` | **Patrol Familiariuszy** | Święte Oficjum | 1 | 0 | 22.6% → 22.8% | `+0.2%` | 11.1 | `-0.1` | 5.74 | 2.3% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `so-02` | **Skarbiec Trybunału** | Święte Oficjum | 1 | 0 | 22.6% → 21.4% | `-1.2%` | 11.0 | `-0.2` | 5.79 | 2.7% | ⚡ MOTOR FRAKCJI (Offensive Engine) |
| `so-04` | **Publiczne Ostrzeżenie** | Święte Oficjum | 1 | 0 | 22.6% → 22.6% | `+0.0%` | 11.1 | `-0.1` | 5.75 | 2.3% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `so-12` | **Straż Trybunalska** | Święte Oficjum | 1 | 0 | 22.6% → 22.4% | `-0.2%` | 11.0 | `-0.2` | 5.76 | 2.3% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `so-03` | **Podejrzenie** | Święte Oficjum | 2 | 0 | 22.6% → 22.6% | `+0.0%` | 11.1 | `-0.1` | 5.75 | 2.3% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `so-08` | **Nasłanie Inkwizytora** | Święte Oficjum | 1 | 0 | 22.6% → 22.8% | `+0.2%` | 11.2 | `0.0` | 5.76 | 2.4% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `so-11` | **Dekret Czystości Wiary** | Święte Oficjum | 1 | 0 | 22.6% → 22.4% | `-0.2%` | 11.0 | `-0.2` | 5.76 | 2.3% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `so-06` | **Areszt Trybunalski** | Święte Oficjum | 2 | 0 | 22.6% → 22.8% | `+0.2%` | 11.2 | `0.0` | 5.76 | 2.4% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `so-07` | **Przesłuchanie Oficjum** | Święte Oficjum | 2 | 0 | 22.6% → 22.8% | `+0.2%` | 11.2 | `0.0` | 5.76 | 2.4% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `so-09` | **Świadek Koronny** | Święte Oficjum | 2 | 0 | 22.6% → 22.8% | `+0.2%` | 11.2 | `0.0` | 5.76 | 2.4% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `so-10` | **Oczyść Miasto** | Święte Oficjum | 5 | 2 | 22.6% → 22.5% | `-0.1%` | 10.9 | `-0.3` | 5.77 | 2.4% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |

---

## 3. ⏳ Warstwa II — Kronika Dziejów w 4P (Ablacja 8 Kart Wydarzeń Czasu)

Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans w 4P:

| ID | Karta Wydarzenia | 4P Score | $\Delta$ 4P | Średnia Er | Deadlock % | Status Roli w Kronice |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `tc-01` | **Kres Średniowiecza** | 🔴 ** 11.2** | `0.0 pkt` | 5.75 Er | 2.5% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-02` | **Płonący Stos** | 🔴 ** 11.2** | `0.0 pkt` | 5.75 Er | 2.5% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-03` | **Królewski Podatek** | 🔴 ** 11.2** | `0.0 pkt` | 5.75 Er | 2.5% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-04` | **Spisek w Cieniu** | 🔴 ** 11.2** | `0.0 pkt` | 5.75 Er | 2.5% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-05` | **Złoty Wiek** | 🔴 ** 11.2** | `0.0 pkt` | 5.75 Er | 2.5% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-06` | **Czystka w Mieście** | 🔴 ** 11.2** | `0.0 pkt` | 5.75 Er | 2.5% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-07` | **Druga Szansa** | 🔴 ** 11.2** | `0.0 pkt` | 5.75 Er | 2.5% | 💤 Martwa karta kroniki (Δ≈0) |
| `tc-08` | **Zaćmienie Słońca** | 🔴 ** 11.2** | `0.0 pkt` | 5.75 Er | 2.5% | 💤 Martwa karta kroniki (Δ≈0) |

---

## 4. ⚙️ Warstwa III — Matryca 9 Obszarów Wpływu Mechanik Gry (L1, L2, L4)

Mechaniki w tym raporcie: **skraj albo wyłączenie**. Testy ±1 są w `audit_level1` / `audit_level2` / `audit_level4`. **Δ≈0 nie jest harmonią.**

| Kategoria Mechaniki | Liczba Testów | Rola w Ekosystemie Kanonu 4P | Rekomendacja Balansowa |
| :--- | :---: | :--- | :--- |
| 👑 / 🛡️ **Filary i Bezpieczniki** | **17** | Ablacja wali w stół — gracze czują tę gałkę | **Cel kanonu** |
| ⚠️ **Za słabe dźwignie** | **6** | Rusza share, nie trzyma stołu — nie jest „zbalansowana” | **Wzmocnić aż będzie filarem** |
| 💤 **Martwe / uśpione ścieżki** | **1** | Dual-win z witalności albo ablacja Δ≈0 | Wada pomiaru, nie harmonia |
| ⚠️ / 💡 **Wady bieżącej wartości** | **4** | Inna wartość gałki **podnosi** 4P — obecny setting szkodzi | **Przekręcić albo rework** |

### 4.0. 💤 Martwe mechaniki (osobny wykaz)
Ścieżki dual-win z `evaluate_vitality` oraz testy z $|\Delta\text{4P}| \le 0.8$ i ruchem share $\le 1.5$ pp.

| Badany Podsystem | Kategoria | 4P Score | $\Delta$ 4P | Klasyfikacja |
| :--- | :--- | :---: | :---: | :--- |
| **Szlak Morski: era 4 → nigdy (99)** | Poziom 4: Warianty i Modyfikatory | 🔴 ** 11.2** | `0.0 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |

### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)

| Badany Podsystem / Modyfikator L1 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Limit Er: 12 → 6 (skrajna presja)** | 11.2 → 🔴 ** 14.2** (`⬆️ +3.0`) | `+3.0 pkt` | 4.91 Er | 55.6% | 1.0% | ⚠️ UMIARKOWANE OBCIĄŻENIE (Moderate Drag) |
| **Próg Oskarżenia: 7 → 1** | 11.2 → 🔴 **  1.8** (`-9.4`) | `-9.4 pkt` | 6.07 Er | 0.1% | 0.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Próg Oskarżenia: 7 → 14** | 11.2 → 🔴 **  3.3** (`-7.9`) | `-7.9 pkt` | 4.94 Er | 2.9% | 1.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 0zł (wyłączenie)** | 11.2 → 🔴 ** 16.8** (`⬆️ +5.6`) | `+5.6 pkt` | 6.28 Er | 3.0% | 7.7% | ⚠️ KRYTYCZNA WADA (Critical Flaw) |
| **Złoto startowe: 4zł → 8zł** | 11.2 → 🔴 **  9.7** (`-1.5`) | `-1.5 pkt` | 5.06 Er | 1.8% | 0.1% | ⚓ KLUCZOWY STABILIZATOR (Key Anchor) |
| **Liczba Agentów: 3 → 1** | 11.2 → 🔴 **  7.2** (`-4.0`) | `-4.0 pkt` | 7.68 Er | 29.3% | 0.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 6** | 11.2 → 🔴 ** 12.0** (`⬆️ +0.8`) | `+0.8 pkt` | 4.32 Er | 0.0% | 1.1% | ⚓ KLUCZOWY STABILIZATOR (Key Anchor) |
| **Limit kart na ręce: 5 → 1** | 11.2 → 🔴 **  0.8** (`-10.4`) | `-10.4 pkt` | 8.66 Er | 14.5% | 6.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 10** | 11.2 → 🔴 **  5.7** (`-5.5`) | `-5.5 pkt` | 4.07 Er | 0.0% | 2.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: cooldown 3 → 0 (co erę)** | 11.2 → 🔴 **  4.5** (`-6.7`) | `-6.7 pkt` | 5.23 Er | 2.7% | 1.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: całkowite wyłączenie** | 11.2 → 🔴 **  4.4** (`-6.8`) | `-6.8 pkt` | 7.11 Er | 31.5% | 0.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)

| Badany Warunek Zwycięstwa L2 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: stosy 7 → 1** | 11.2 → 🔴 **  3.5** (`-7.7`) | `-7.7 pkt` | 3.58 Er | 0.0% | 1.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: stosy 7 → 14** | 11.2 → 🔴 **  8.9** (`-2.3`) | `-2.3 pkt` | 5.89 Er | 5.8% | 0.9% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |
| **Święte Oficjum: skazania 3 → 1** | 11.2 → 🔴 **  4.1** (`-7.1`) | `-7.1 pkt` | 4.04 Er | 0.0% | 1.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 6** | 11.2 → 🔴 **  8.8** (`-2.4`) | `-2.4 pkt` | 5.86 Er | 3.0% | 0.9% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |
| **Cienie: relikwie 2 → 4** | 11.2 → 🔴 **  7.1** (`-4.1`) | `-4.1 pkt` | 5.93 Er | 2.8% | 0.9% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Korona: dekrety 2 → 4** | 11.2 → 🔴 **  3.1** (`-8.1`) | `-8.1 pkt` | 6.74 Er | 3.4% | 0.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: wymóg haków 0 → 2 (podatek)** | 11.2 → 🔴 ** 11.4** (`⬆️ +0.2`) | `+0.2 pkt` | 6.04 Er | 2.5% | 0.9% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |
| **Kabała: fragmenty 3 → 1** | 11.2 → 🔴 ** 10.0** (`-1.2`) | `-1.2 pkt` | 4.56 Er | 1.0% | 1.1% | ⚓ KLUCZOWY STABILIZATOR (Key Anchor) |
| **Kabała: fragmenty 3 → 6** | 11.2 → 🔴 **  7.0** (`-4.2`) | `-4.2 pkt` | 5.95 Er | 2.7% | 0.9% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Kabała: era 4 → 1** | 11.2 → 🔴 ** 11.9** (`⬆️ +0.7`) | `+0.7 pkt` | 5.64 Er | 2.5% | 0.9% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |
| **Kabała: era 4 → 8** | 11.2 → 🔴 **  7.9** (`-3.3`) | `-3.3 pkt` | 5.93 Er | 2.5% | 0.9% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |
| **Gildia: upadki 7 → 1** | 11.2 → 🔴 **  2.7** (`-8.5`) | `-8.5 pkt` | 3.30 Er | 1.9% | 1.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 7 → 14** | 11.2 → 🔴 ** 15.5** (`⬆️ +4.3`) | `+4.3 pkt` | 6.88 Er | 10.7% | 0.7% | ⚠️ KRYTYCZNA WADA (Critical Flaw) |

### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)

| Badany Wariant / Modyfikator L4 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kronika Dziejów: całkowite wyłączenie** | 11.2 → 🔴 **  9.6** (`-1.6`) | `-1.6 pkt` | 5.76 Er | 1.9% | 1.0% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |
| **Werdykt Sądu: tajny (wyłączenie jawnej koordynacji)** | 11.2 → 🔴 ** 13.5** (`⬆️ +2.3`) | `+2.3 pkt` | 5.49 Er | 1.5% | 0.9% | 💡 KANDYDAT DO UPROSZCZENIA (Simplification) |
| **Inkwizytor Patrol: ruch 1 → 0 (wyłączenie)** | 11.2 → 🔴 **  4.0** (`-7.2`) | `-7.2 pkt` | 7.20 Er | 32.3% | 0.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Szlak Morski: era 4 → nigdy (99)** | 🔴 ** 11.2** | `0.0 pkt` | 5.75 Er | 2.5% | 0.9% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |

---

## 5. 👥 Warstwa IV — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych. Kolumna win share to HUD kanonu; setup+witalność to stary blend (kara martwej ścieżki).

| Nieobecna Frakcja | Setup Testowy | Win share | Setup+witalność | Diagnoza |
| :--- | :--- | :---: | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`10.6`** | `6.8` | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`14.1`** | `14.1` | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`9.0`** | `9.0` | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`11.0`** | `11.0` | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`11.3`** | `11.3` | Brak presji stosów i bezpośredniego Inkwizytora |