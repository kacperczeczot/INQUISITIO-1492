# Raport Audytora Kart Problemowych 4P — Wersja Balansu: v1.0-alpha.23

**Wersja:** `v1.0-alpha.23` | **Data:** 2026-08-22 15:56 | **Próba:** 5000 gier/setup | **Ziarno:** 42
**Baza 4P Score:** 81.10 pkt | **Najlepsza Mutacja:** 84.80 pkt (Δ +3.70 pkt)

## 1. Zidentyfikowane Karty Problematyczne

| ID Karty | Nazwa Karty | Frakcja | Klasyfikacja w Matrycy 4P | Rola Projektowa |
| :--- | :--- | :--- | :--- | :--- |
| `caa-01` | **Przejście Podziemiami** | Cienie Al-Andalus | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `caa-02` | **Złoto z Kryjówki** | Cienie Al-Andalus | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `caa-04` | **Fałszywy Trop** | Cienie Al-Andalus | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `caa-07` | **Szantaż Bractwa** | Cienie Al-Andalus | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `caa-08` | **Kaptur Nocy** | Cienie Al-Andalus | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `caa-11` | **Nocna Zmiana Warty** | Cienie Al-Andalus | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `caa-12` | **Skrytka w Murach** | Cienie Al-Andalus | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `gc-02` | **Czarny Rynek** | Gildia Cieni | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `gc-08` | **Zatrute Złoto** | Gildia Cieni | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) | DEAD_WEIGHT |
| `gc-11` | **Fałszywe Świadectwo Cechu** | Gildia Cieni | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) | DEAD_WEIGHT |
| `gc-12` | **Złodziejski Zwiad** | Gildia Cieni | 💤 KARTA NISKIEGO WPŁYWU (Dead / Passive) | DEAD_WEIGHT |
| `kb-04` | **Faworyt Dworu** | Korona & Borgiowie | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `kb-05` | **List Żelazny** | Korona & Borgiowie | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `kb-06` | **Areszt Królewski** | Korona & Borgiowie | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `kb-07` | **Szantaż Pieczęcią** | Korona & Borgiowie | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `kb-08` | **Przekupstwo Sędziego** | Korona & Borgiowie | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `kt-01` | **Rytuał Przejścia** | Kabała z Toledo | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `kt-02` | **Transmutacja Złota** | Kabała z Toledo | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `kt-06` | **Przesłuchanie Imienia** | Kabała z Toledo | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) | DISRUPTOR |
| `kt-07` | **Archiwum Ukryte** | Kabała z Toledo | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `kt-09` | **Fragment Kodeksu** | Kabała z Toledo | ⚠️ TOKSYCZNY PROMOTOR (Disruptor Win-Driver) | DISRUPTOR |
| `kt-10` | **Pieczęć Salomona** | Kabała z Toledo | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `kt-11` | **Medytacja Sefirot** | Kabała z Toledo | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `kt-12` | **Strażnik Archiwum** | Kabała z Toledo | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |

## 2. Wyniki Testów Celowanych (TOP Finaliści)

| ID Mutacji | Modyfikacja Karty | 4P Score | Δ 4P | Średnia Er | Pas Biedy % | Deadlock % |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `MUT_KB-04_COST_MINUS1` | KB-04 (Faworyt Dworu) [Buff Autopodatku]: koszt 2 → 1 | 🟡 ** 84.8** | `+3.70 pkt` | 6.00 | 1.2% | 0.1% |
| `MUT_KT-09_HERESY_PLUS1` | KT-09 (Fragment Kodeksu) [Nerf Disruptora]: herezja 1 → 2 | 🟡 ** 84.8** | `+3.70 pkt` | 6.05 | 1.5% | 0.1% |
| `MUT_KB-05_COST_MINUS1` | KB-05 (List Żelazny) [Buff Autopodatku]: koszt 2 → 1 | 🟡 ** 84.4** | `+3.30 pkt` | 6.00 | 1.1% | 0.1% |
| `MUT_KB-04_GOLD_SET1` | KB-04 (Faworyt Dworu) [Buff Autopodatku]: dodaj złoto = 1 | 🟡 ** 83.7** | `+2.60 pkt` | 5.99 | 1.2% | 0.1% |
| `MUT_KB-05_GOLD_SET1` | KB-05 (List Żelazny) [Buff Autopodatku]: dodaj złoto = 1 | 🟡 ** 83.5** | `+2.40 pkt` | 5.99 | 1.2% | 0.1% |
| `MUT_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu) [Nerf Disruptora]: koszt 2 → 3 | 🟡 ** 83.5** | `+2.40 pkt` | 6.05 | 1.5% | 0.1% |
| `MUT_KB-07_GOLD_SET1` | KB-07 (Szantaż Pieczęcią) [Buff Autopodatku]: dodaj złoto = 1 | 🟡 ** 82.9** | `+1.80 pkt` | 5.99 | 1.4% | 0.1% |
| `MUT_KB-08_COST_MINUS1` | KB-08 (Przekupstwo Sędziego) [Buff Autopodatku]: koszt 2 → 1 | 🟡 ** 82.8** | `+1.70 pkt` | 6.00 | 1.2% | 0.1% |
| `MUT_KB-08_GOLD_SET1` | KB-08 (Przekupstwo Sędziego) [Buff Autopodatku]: dodaj złoto = 1 | 🟡 ** 82.7** | `+1.60 pkt` | 6.00 | 1.4% | 0.1% |
| `MUT_KT-06_HERESY_PLUS1` | KT-06 (Przesłuchanie Imienia) [Nerf Disruptora]: herezja 0 → 1 | 🟡 ** 82.6** | `+1.50 pkt` | 6.04 | 1.5% | 0.1% |
| `MUT_KB-07_COST_MINUS1` | KB-07 (Szantaż Pieczęcią) [Buff Autopodatku]: koszt 2 → 1 | 🟡 ** 82.4** | `+1.30 pkt` | 5.99 | 1.2% | 0.1% |
| `MUT_CAA-12_COST_PLUS2` | CAA-12 (Skrytka w Murach) [Tuning]: koszt 0 → 2 | 🟡 ** 82.4** | `+1.30 pkt` | 6.03 | 1.5% | 0.1% |
| `MUT_KT-10_GOLD_SET1` | KT-10 (Pieczęć Salomona) [Buff Autopodatku]: dodaj złoto = 1 | 🟡 ** 82.4** | `+1.30 pkt` | 6.04 | 1.4% | 0.1% |
| `MUT_KB-06_GOLD_SET1` | KB-06 (Areszt Królewski) [Buff Autopodatku]: dodaj złoto = 1 | 🟡 ** 82.1** | `+1.00 pkt` | 6.03 | 1.5% | 0.1% |
| `MUT_KT-01_COST_MINUS1` | KT-01 (Rytuał Przejścia) [Buff Autopodatku]: koszt 1 → 0 | 🟡 ** 82.1** | `+1.00 pkt` | 6.04 | 1.4% | 0.1% |
| `MUT_CAA-08_COST_MINUS1` | CAA-08 (Kaptur Nocy) [Buff Autopodatku]: koszt 1 → 0 | 🟡 ** 82.1** | `+1.00 pkt` | 6.04 | 1.5% | 0.1% |
| `MUT_KT-11_COST_MINUS1` | KT-11 (Medytacja Sefirot) [Buff Autopodatku]: koszt 2 → 1 | 🟡 ** 81.9** | `+0.80 pkt` | 6.04 | 1.5% | 0.1% |
| `MUT_KB-06_COST_MINUS1` | KB-06 (Areszt Królewski) [Buff Autopodatku]: koszt 2 → 1 | 🟡 ** 81.6** | `+0.50 pkt` | 6.05 | 1.5% | 0.1% |
| `MUT_GC-11_GOLD_SET1` | GC-11 (Fałszywe Świadectwo Cechu) [Aktywacja Dead Weight]: dodaj złoto = 1 | 🟡 ** 81.3** | `+0.20 pkt` | 6.01 | 1.5% | 0.1% |
| `MUT_KT-06_COST_PLUS1` | KT-06 (Przesłuchanie Imienia) [Nerf Disruptora]: koszt 2 → 3 | 🟡 ** 79.9** | `-1.20 pkt` | 6.03 | 1.6% | 0.2% |