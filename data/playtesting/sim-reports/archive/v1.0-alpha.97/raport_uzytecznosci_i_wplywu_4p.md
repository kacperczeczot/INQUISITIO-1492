# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v1.0-alpha.97

**Wersja Gry:** `v1.0-alpha.97` | **Data Badania:** 2026-08-29 22:27 | **Próba:** 5000 gier/setup (25000 gier na wariant) | **Ziarno:** 42
**4P Score (win share):** 🟢 ** 93.6** pkt | **Witalność (osobna kara):** `0.000` | **Śr. Er:** `5.76` | **Deadlocki:** `0.0%` | **Pas Biedy:** `4.9%`
**Udziały 4P:** CAA 24.5% · GC 24.9% · KB 25.0% · KT 25.4% · SO 25.3%

Klasyfikacja L1/L2/L4 i Δ 4P liczą wyłącznie równość win share (`calculate_balance_score`). Kara witalności jest osobno.

---

## 0. Wady z tej próby (nie HUD win share)

Kubełki klasyfikatora i ostrzeżenia witalności z bieżącego runu.

- **DEAD_WEIGHT:** `caa-02` Złoto z Kryjówki, `caa-01` Przejście Podziemiami, `gc-12` Złodziejski Zwiad, `gc-01` Przekupiony Strażnik, `gc-03` Podrzucenie Księgi, `gc-05` Fałszywy Świadek, `gc-11` Fałszywe Świadectwo Cechu, `gc-08` Zatrute Złoto, `gc-06` Szantaż, `gc-10` Upadek Domu, `kb-01` Rozkaz Dworu, `kb-06` Areszt Królewski, `kb-08` Przekupstwo Sędziego, `kb-10` Pieczęć Korony, `kt-01` Rytuał Przejścia, `kt-07` Archiwum Ukryte, `so-05` Wezwanie do Trybunału, `so-01` Patrol Familiariuszy, `so-02` Skarbiec Trybunału, `so-12` Straż Trybunalska, `so-03` Podejrzenie, `so-09` Świadek Koronny
- **Karty Kroniki |Δ4P| ≤ 0.8:** 10/10
- **Ablacja całej Kroniki (`L4_NO_TIME_DECK`):** Δ4P +0.0 (DEAD)
- **Mechaniki WEAK/NEUTRAL:** Szlak Morski: era 4 → nigdy (99)
- **Mechaniki DEAD:** Próg Oskarżenia: 7 → 1; Próg Oskarżenia: 7 → 14; Złoto startowe: 4zł → 0zł (wyłączenie); Złoto startowe: 4zł → 8zł; Liczba Agentów: 3 → 1; Liczba Agentów: 3 → 6; Limit kart na ręce: 5 → 1; Limit kart na ręce: 5 → 10; Kabała: fragmenty 3 → 1; Akcja Gospodarcza: 0zł (brak zysku złota); Akcja Gospodarcza: 1 → 2 (podwojenie); Kronika Dziejów: całkowite wyłączenie; Kronika Dziejów: co 3 Ery (spowolniony zegar); Inkwizytor Patrol: ruch 1 → 0 (wyłączenie); Inkwizytor Patrol: ruch x2 (podwojona prędkość)

---

## 1. 🗺️ Podsumowanie Ekosystemu Kart Kanonu 4P (Matryca Wpływu Kart, 60 kart)

Rozkład wszystkich 60 kart frakcyjnych w matrycy **Wpływ na Frakcję ($\Delta \text{Share}$)** vs **Wpływ na Kanon 4P ($\Delta \text{4P Score}$)**:

| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |
| :--- | :---: | :---: | :--- | :--- |
| 🩸 **Autopodatek (Self-Harm)** | **0** | 0.0% | Wyłączenie **podnosi** win share własnej frakcji — karta jest haraczem, nie silnikiem | **Rework / osłabienie kosztu, nie filar** |
| 🔄 **Rozcieńczalnik Talii (Tempo Filler)** | **0** | 0.0% | Normalna karta tempa — ablacja fałszywie flaguje ją jako autopodatek z powodu odchudzenia talii | **Normalny element deckbuildingu** |
| 💤 **Karta Pasywna (Dead Weight)** | **22** | 36.7% | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia lub wycięcia** |
| ⚠️ **Karta Destabilizująca (Disruptor)** | **0** | 0.0% | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |
| ⚖️ **Zbalansowane Narzędzie** | **38** | 63.3% | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Narzędzie, nie złoty środek całego kanonu** |
| 👑 / ⚓ **Filar / Kotwica Kanonu** | **0** | 0.0% | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |

---

## 2. 🃏 Warstwa I — Szczegółowa Analiza 60 Kart Frakcji w Kanonie 4P

### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)
Karty, których brak powoduje spadek wyniku Kanonu 4P o $\ge 4.0$ pkt lub załamanie winrate frakcji o $\ge 4.0\%$ — **bez** autopodatków (te są w 2.1b):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |

### 2.1b. 🩸 Autopodatek Frakcji (Self-Harm)
Karty, których wyłączenie **podnosi** win share własnej frakcji. Gracz zauważy je jako haracz, nawet gdy stół 4P jest równy dzięki temu haraczowi.

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *Brak kart-autopodatków* | - | - | - | - | - | - |

### 2.2. ⚠️ Karty Destabilizujące Kanon 4P (Disruptors)
Karty, których wyłączenie podnosi 4P Score ($\Delta \text{4P} \ge +1.5$ pkt):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *Brak kart destabilizujących* | - | - | - | - | - | - |

### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich 60 Kart Frakcji w Kanonie 4P

| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Play-Rate | Faction Win Share 4P | $\Delta$ Frakcji | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `caa-02` | **Złoto z Kryjówki** | Cienie Al-Andalus | 0 | 0 | 0.24 | 24.5% → 24.5% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `caa-03` | **Cień na Rynku** | Cienie Al-Andalus | 0 | 1 | 0.93 | 24.5% → 24.5% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-04` | **Fałszywy Trop** | Cienie Al-Andalus | 0 | 0 | 0.97 | 24.5% → 24.5% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-05` | **Ukryty Kurier** | Cienie Al-Andalus | 0 | 0 | 1.01 | 24.5% → 24.5% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-12` | **Skrytka w Murach** | Cienie Al-Andalus | 1 | 0 | 0.93 | 24.5% → 24.5% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-01` | **Przejście Podziemiami** | Cienie Al-Andalus | 2 | 2 | 0.00 | 24.5% → 24.5% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `caa-06` | **Ucieczka z Lochów** | Cienie Al-Andalus | 0 | 0 | 0.68 | 24.5% → 24.5% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-07` | **Szantaż Bractwa** | Cienie Al-Andalus | 0 | 0 | 0.55 | 24.5% → 24.5% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-11` | **Nocna Zmiana Warty** | Cienie Al-Andalus | 1 | 0 | 0.69 | 24.5% → 24.5% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-08` | **Kaptur Nocy** | Cienie Al-Andalus | 2 | 0 | 0.80 | 24.5% → 24.5% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-09` | **Kurier Relikwii** | Cienie Al-Andalus | 0 | 0 | 0.93 | 24.5% → 24.5% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `caa-10` | **Echo Alhambry** | Cienie Al-Andalus | 2 | 0 | 0.99 | 24.5% → 24.5% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-02` | **Czarny Rynek** | Gildia Cieni | 0 | 0 | 0.78 | 24.9% → 24.9% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-12` | **Złodziejski Zwiad** | Gildia Cieni | 0 | 2 | 0.44 | 24.9% → 24.9% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `gc-01` | **Przekupiony Strażnik** | Gildia Cieni | 1 | 1 | 0.47 | 24.9% → 24.9% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `gc-03` | **Podrzucenie Księgi** | Gildia Cieni | 1 | 2 | 0.08 | 24.9% → 24.9% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `gc-04` | **Informator** | Gildia Cieni | 1 | 1 | 0.80 | 24.9% → 24.9% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-05` | **Fałszywy Świadek** | Gildia Cieni | 1 | 0 | 0.00 | 24.9% → 24.9% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `gc-07` | **Skrytobójstwo** | Gildia Cieni | 0 | 0 | 0.79 | 24.9% → 24.9% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-11` | **Fałszywe Świadectwo Cechu** | Gildia Cieni | 0 | 2 | 0.31 | 24.9% → 24.9% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `gc-08` | **Zatrute Złoto** | Gildia Cieni | 1 | 2 | 0.00 | 24.9% → 24.9% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `gc-06` | **Szantaż** | Gildia Cieni | 3 | 1 | 0.43 | 24.9% → 24.9% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `gc-09` | **Lista Dłużników** | Gildia Cieni | 1 | 0 | 0.79 | 24.9% → 24.9% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `gc-10` | **Upadek Domu** | Gildia Cieni | 4 | 2 | 0.46 | 24.9% → 24.9% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `kb-01` | **Rozkaz Dworu** | Korona & Borgiowie | 1 | 1 | 0.25 | 25.0% → 25.0% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `kb-02` | **Pobór Podatków** | Korona & Borgiowie | 1 | 0 | 0.84 | 25.0% → 25.0% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-03` | **Plotka Dworska** | Korona & Borgiowie | 1 | 1 | 0.64 | 25.0% → 25.0% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-11` | **Tajny Emisariusz** | Korona & Borgiowie | 1 | 0 | 0.83 | 25.0% → 25.0% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-04` | **Faworyt Dworu** | Korona & Borgiowie | 2 | 0 | 0.74 | 25.0% → 25.0% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-05` | **List Żelazny** | Korona & Borgiowie | 2 | 1 | 0.82 | 25.0% → 25.0% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-12` | **Szantaż Salonowy** | Korona & Borgiowie | 1 | 2 | 0.82 | 25.0% → 25.0% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-06` | **Areszt Królewski** | Korona & Borgiowie | 2 | 0 | 0.44 | 25.0% → 25.0% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `kb-07` | **Szantaż Pieczęcią** | Korona & Borgiowie | 2 | 0 | 0.62 | 25.0% → 25.0% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-08` | **Przekupstwo Sędziego** | Korona & Borgiowie | 3 | 2 | 0.08 | 25.0% → 25.0% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `kb-09` | **Dekret Królewski** | Korona & Borgiowie | 2 | 0 | 0.85 | 25.0% → 25.0% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kb-10` | **Pieczęć Korony** | Korona & Borgiowie | 4 | 1 | 0.16 | 25.0% → 25.0% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `kt-02` | **Transmutacja Złota** | Kabała z Toledo | 0 | 0 | 0.95 | 25.4% → 25.4% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-03` | **Zakazana Wiedza** | Kabała z Toledo | 0 | 2 | 0.81 | 25.4% → 25.4% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-01` | **Rytuał Przejścia** | Kabała z Toledo | 1 | 1 | 0.05 | 25.4% → 25.4% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `kt-04` | **Zwierciadło Herezji** | Kabała z Toledo | 1 | 0 | 0.52 | 25.4% → 25.4% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-05` | **Wskazówka Cyklu** | Kabała z Toledo | 1 | 1 | 0.96 | 25.4% → 25.4% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-12` | **Strażnik Archiwum** | Kabała z Toledo | 1 | 0 | 0.91 | 25.4% → 25.4% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-07` | **Archiwum Ukryte** | Kabała z Toledo | 1 | 0 | 0.30 | 25.4% → 25.4% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `kt-08` | **Areszt Wiedzy** | Kabała z Toledo | 1 | 0 | 0.88 | 25.4% → 25.4% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-06` | **Przesłuchanie Imienia** | Kabała z Toledo | 2 | 0 | 0.82 | 25.4% → 25.4% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-11` | **Medytacja Sefirot** | Kabała z Toledo | 2 | 0 | 0.92 | 25.4% → 25.4% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-09` | **Fragment Kodeksu** | Kabała z Toledo | 1 | 1 | 0.96 | 25.4% → 25.4% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `kt-10` | **Pieczęć Salomona** | Kabała z Toledo | 4 | 0 | 0.52 | 25.4% → 25.4% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-05` | **Wezwanie do Trybunału** | Święte Oficjum | 0 | 4 | 0.00 | 25.3% → 25.3% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | 💤 KARTA NIEZAGRYWANA (Dead / Unplayed) |
| `so-01` | **Patrol Familiariuszy** | Święte Oficjum | 1 | 2 | 0.26 | 25.3% → 25.3% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `so-02` | **Skarbiec Trybunału** | Święte Oficjum | 1 | 2 | 0.49 | 25.3% → 25.3% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `so-04` | **Publiczne Ostrzeżenie** | Święte Oficjum | 1 | 0 | 0.86 | 25.3% → 25.3% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-12` | **Straż Trybunalska** | Święte Oficjum | 1 | 2 | 0.25 | 25.3% → 25.3% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `so-03` | **Podejrzenie** | Święte Oficjum | 2 | 4 | 0.30 | 25.3% → 25.3% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `so-08` | **Nasłanie Inkwizytora** | Święte Oficjum | 0 | 0 | 0.86 | 25.3% → 25.3% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-07` | **Przesłuchanie Oficjum** | Święte Oficjum | 1 | 0 | 0.84 | 25.3% → 25.3% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-09` | **Świadek Koronny** | Święte Oficjum | 1 | 1 | 0.15 | 25.3% → 25.3% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) |
| `so-11` | **Dekret Czystości Wiary** | Święte Oficjum | 1 | 1 | 0.84 | 25.3% → 25.3% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-06` | **Areszt Trybunalski** | Święte Oficjum | 2 | 0 | 0.89 | 25.3% → 25.3% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |
| `so-10` | **Oczyść Miasto** | Święte Oficjum | 5 | 1 | 0.75 | 25.3% → 25.3% | `+0.0%` | 93.6 | `0.0` | 5.76 | 0.0% | ⚖️ ZBALANSOWANE NARZĘDZIE (Utility) |

### 2.4. 🎯 Monokultura Talii (Deck Concentration Index)

Jak mocno skoncentrowane jest zagrywanie kart w obrębie każdej frakcji.
Wskaźnik HHI (Herfindahl–Hirschman Index) mierzy koncentrację: HHI = 1.0 oznacza, że 100% zagrań to 1 karta; HHI ≈ 1/N oznacza idealnie równomierny rozkład.

| Frakcja | Kart w Talii | Top Karta (Play-Rate) | Top 2 (%) | HHI | Ocena |
| :--- | :---: | :--- | :---: | :---: | :--- |
| Cienie Al-Andalus | 12 | `caa-05` (1.01) | 22.9% | 0.098 | 🟢 Zdrowy rozkład |
| Gildia Cieni | 12 | `gc-04` (0.80) | 29.6% | 0.119 | 🟢 Zdrowy rozkład |
| Korona & Borgiowie | 12 | `kb-09` (0.85) | 23.8% | 0.101 | 🟢 Zdrowy rozkład |
| Kabała z Toledo | 12 | `kt-05` (0.96) | 22.4% | 0.097 | 🟢 Zdrowy rozkład |
| Święte Oficjum | 12 | `so-06` (0.89) | 27.0% | 0.112 | 🟢 Zdrowy rozkład |

---

## 3. ⏳ Warstwa II — Kronika Dziejów w 4P (Ablacja 8 Kart Wydarzeń Czasu)

Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans w 4P:

| ID | Karta Wydarzenia | 4P Score | $\Delta$ 4P | Średnia Er | Deadlock % | Status Roli w Kronice |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `time-01` | **Kapitulacja Grenady** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-02` | **Godzina Policyjna** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-03` | **Flota Odkrywców** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-04` | **Rewizja w Dzielnicach** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-05` | **Gorączka Donosów** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-06` | **Nocna Obława** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-07` | **Bunt w Lochach** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-08` | **Święte Przymierze** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-09` | **Jarmark Królewski** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |
| `time-10` | **Amnestia Biskupia** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 💤 Martwa karta kroniki (Δ≈0) |

---

## 4. ⚙️ Warstwa III — Matryca 9 Obszarów Wpływu Mechanik Gry (L1, L2, L4)

Mechaniki w tym raporcie: **skraj albo wyłączenie**. Testy ±1 są w `audit_level1` / `audit_level2` / `audit_level4`. **Δ≈0 nie jest harmonią.**

| Kategoria Mechaniki | Liczba Testów | Rola w Ekosystemie Kanonu 4P | Rekomendacja Balansowa |
| :--- | :---: | :--- | :--- |
| 👑 / 🛡️ **Filary i Bezpieczniki** | **15** | Ablacja wali w stół — gracze czują tę gałkę | **Cel kanonu** |
| ⚠️ **Za słabe dźwignie** | **1** | Rusza share, nie trzyma stołu — nie jest „zbalansowana” | **Wzmocnić aż będzie filarem** |
| 💤 **Martwe / uśpione ścieżki** | **15** | Dual-win z witalności albo ablacja Δ≈0 | Wada pomiaru, nie harmonia |
| ⚠️ / 💡 **Wady bieżącej wartości** | **0** | Inna wartość gałki **podnosi** 4P — obecny setting szkodzi | **Przekręcić albo rework** |

### 4.0. ⚠️ Problematyczne mechaniki (osobny wykaz)
Wszystkie mechaniki z grup **DEAD**, **WEAK/NEUTRAL** i **DISRUPTOR**: ścieżki dual-win z `evaluate_vitality`, testy z $|\Delta\text{4P}| \le 0.8$ i ruchem share $\le 1.5$ pp (DEAD), za słabe dźwignie (WEAK) oraz wady bieżącej wartości (DISRUPTOR).

| Badany Podsystem | Kategoria | 4P Score | $\Delta$ 4P | Klasyfikacja |
| :--- | :--- | :---: | :---: | :--- |
| **Akcja Gospodarcza: 0zł (brak zysku złota)** | Poziom 1: System Core | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Akcja Gospodarcza: 1 → 2 (podwojenie)** | Poziom 1: System Core | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Inkwizytor Patrol: ruch 1 → 0 (wyłączenie)** | Poziom 4: Warianty i Modyfikatory | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Inkwizytor Patrol: ruch x2 (podwojona prędkość)** | Poziom 4: Warianty i Modyfikatory | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Kabała: fragmenty 3 → 1** | Poziom 2: Warunki Zwycięstwa | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Kronika Dziejów: całkowite wyłączenie** | Poziom 4: Warianty i Modyfikatory | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Kronika Dziejów: co 3 Ery (spowolniony zegar)** | Poziom 4: Warianty i Modyfikatory | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Liczba Agentów: 3 → 1** | Poziom 1: System Core | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Liczba Agentów: 3 → 6** | Poziom 1: System Core | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Limit kart na ręce: 5 → 1** | Poziom 1: System Core | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Limit kart na ręce: 5 → 10** | Poziom 1: System Core | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Próg Oskarżenia: 7 → 1** | Poziom 1: System Core | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Próg Oskarżenia: 7 → 14** | Poziom 1: System Core | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Złoto startowe: 4zł → 0zł (wyłączenie)** | Poziom 1: System Core | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Złoto startowe: 4zł → 8zł** | Poziom 1: System Core | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Szlak Morski: era 4 → nigdy (99)** | Poziom 4: Warianty i Modyfikatory | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | `-0.9 pkt` | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |

### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)

| Badany Podsystem / Modyfikator L1 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Limit Er: 15 → 7 (skrajna presja)** | 93.6 → 🟡 ** 86.3** (`🔻 -7.3`) | `-7.3 pkt` | 5.64 Er | 9.3% | 4.9% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Próg Oskarżenia: 7 → 1** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 4.9% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Próg Oskarżenia: 7 → 14** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 4.9% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Złoto startowe: 4zł → 0zł (wyłączenie)** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 4.9% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Złoto startowe: 4zł → 8zł** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 4.9% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Liczba Agentów: 3 → 1** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 4.9% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Liczba Agentów: 3 → 6** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 4.9% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Limit kart na ręce: 5 → 1** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 4.9% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Limit kart na ręce: 5 → 10** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 4.9% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Autodafé: cooldown 3 → 0 (co erę)** | 93.6 → 🔴 ** 11.3** (`🔻 -82.3`) | `-82.3 pkt` | 4.88 Er | 0.0% | 5.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé: całkowite wyłączenie** | 93.6 → 🔴 ** 63.4** (`🔻 -30.2`) | `-30.2 pkt` | 5.96 Er | 0.0% | 5.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Akcja Gospodarcza: 0zł (brak zysku złota)** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 4.9% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Akcja Gospodarcza: 1 → 2 (podwojenie)** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 4.9% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Próg Obserwowanej: 3 → 2 (skrajna presja)** | 93.6 → 🟠 ** 78.5** (`🔻 -15.1`) | `-15.1 pkt` | 5.68 Er | 0.0% | 4.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)

| Badany Warunek Zwycięstwa L2 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: stosy 7 → 1** | 93.6 → 🔴 ** 18.8** (`🔻 -74.8`) | `-74.8 pkt` | 3.90 Er | 0.0% | 4.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: stosy 7 → 14** | 93.6 → 🟠 ** 72.5** (`🔻 -21.1`) | `-21.1 pkt` | 5.84 Er | 0.0% | 5.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 1** | 93.6 → 🔴 ** 18.5** (`🔻 -75.1`) | `-75.1 pkt` | 3.41 Er | 0.0% | 3.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: skazania 3 → 6** | 93.6 → 🔴 ** 59.1** (`🔻 -34.5`) | `-34.5 pkt` | 5.85 Er | 0.0% | 5.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Cienie: relikwie 2 → 4** | 93.6 → 🔴 ** 32.9** (`🔻 -60.7`) | `-60.7 pkt` | 6.08 Er | 0.0% | 5.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: dekrety 2 → 4** | 93.6 → 🔴 ** 34.0** (`🔻 -59.6`) | `-59.6 pkt` | 6.02 Er | 0.0% | 4.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: wymóg haków 2 → 0** | 93.6 → 🟡 ** 80.4** (`🔻 -13.2`) | `-13.2 pkt` | 5.71 Er | 0.0% | 4.9% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Korona: wymóg haków 2 → 4** | 93.6 → 🔴 ** 33.9** (`🔻 -59.7`) | `-59.7 pkt` | 6.02 Er | 0.0% | 4.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: fragmenty 3 → 1** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 4.9% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Kabała: fragmenty 3 → 6** | 93.6 → 🔴 ** 37.0** (`🔻 -56.6`) | `-56.6 pkt` | 6.08 Er | 0.0% | 5.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 9 → 1** | 93.6 → 🔴 ** 18.1** (`🔻 -75.5`) | `-75.5 pkt` | 2.97 Er | 0.0% | 2.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: upadki 9 → 18** | 93.6 → 🔴 ** 32.9** (`🔻 -60.7`) | `-60.7 pkt` | 6.02 Er | 0.0% | 5.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)

| Badany Wariant / Modyfikator L4 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kronika Dziejów: całkowite wyłączenie** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 4.9% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Kronika Dziejów: co 3 Ery (spowolniony zegar)** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 4.9% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Inkwizytor Patrol: ruch 1 → 0 (wyłączenie)** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 4.9% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Inkwizytor Patrol: ruch x2 (podwojona prędkość)** | 93.6 → 🟢 ** 93.6** (`= 0.0`) | `0.0 pkt` | 5.76 Er | 0.0% | 4.9% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Szlak Morski: era 4 → nigdy (99)** | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | `-0.9 pkt` | 5.77 Er | 0.0% | 4.9% | ⚠️ ZA SŁABA DŹWIGNIA (rusza share, nie trzyma stołu) |

---

## 5. 👥 Warstwa IV — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych. Kolumna win share to HUD kanonu; setup+witalność to stary blend (kara martwej ścieżki).

| Nieobecna Frakcja | Setup Testowy | Win share | Setup+witalność | Diagnoza |
| :--- | :--- | :---: | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`89.9`** | `89.9` | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`95.4`** | `95.4` | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`95.4`** | `95.4` | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`87.9`** | `87.9` | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`99.2`** | `99.2` | Brak presji stosów i bezpośredniego Inkwizytora |