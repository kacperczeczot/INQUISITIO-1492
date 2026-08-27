[Strona główna](../../../../../README.md) > [v1.0-alpha.24](README.md) > [audyt_kart_problemowych_4p](audyt_kart_problemowych_4p.md)

---

# Raport Audytora Kart Problemowych 4P — Wersja Balansu: v1.0-alpha.24

**Wersja:** `v1.0-alpha.24` | **Data:** 2026-08-22 16:32 | **Próba:** 5000 gier/setup | **Ziarno:** 42
**Baza 4P Score:** 84.30 pkt | **Najlepsza Mutacja:** 84.10 pkt (Δ -0.20 pkt)

## 1. Zidentyfikowane Karty Problematyczne

| ID Karty | Nazwa Karty | Frakcja | Klasyfikacja w Matrycy 4P | Rola Projektowa |
| :--- | :--- | :--- | :--- | :--- |
| `caa-01` | **Przejście Podziemiami** | Cienie Al-Andalus | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `caa-04` | **Fałszywy Trop** | Cienie Al-Andalus | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `caa-07` | **Szantaż Bractwa** | Cienie Al-Andalus | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `caa-08` | **Kaptur Nocy** | Cienie Al-Andalus | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `caa-11` | **Nocna Zmiana Warty** | Cienie Al-Andalus | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `gc-02` | **Czarny Rynek** | Gildia Cieni | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `gc-10` | **Upadek Domu** | Gildia Cieni | ⚠️ SZUM DESTABILIZUJĄCY (Meta Disruptor) | DISRUPTOR |
| `kb-04` | **Faworyt Dworu** | Korona & Borgiowie | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `kb-05` | **List Żelazny** | Korona & Borgiowie | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `kb-06` | **Areszt Królewski** | Korona & Borgiowie | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `kt-01` | **Rytuał Przejścia** | Kabała z Toledo | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `kt-02` | **Transmutacja Złota** | Kabała z Toledo | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `kt-04` | **Zwierciadło Herezji** | Kabała z Toledo | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `kt-07` | **Archiwum Ukryte** | Kabała z Toledo | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `kt-10` | **Pieczęć Salomona** | Kabała z Toledo | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `kt-11` | **Medytacja Sefirot** | Kabała z Toledo | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |
| `kt-12` | **Strażnik Archiwum** | Kabała z Toledo | 🩸 AUTOPODATEK FRAKCJI (Self-Harm Tax) | SELF_HARM |

## 2. Wyniki Testów Celowanych (TOP Finaliści)

| ID Mutacji | Modyfikacja Karty | 4P Score | Δ 4P | Średnia Er | Pas Biedy % | Deadlock % |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `MUT_KT-04_COST_MINUS1` | KT-04 (Zwierciadło Herezji) [Buff Autopodatku]: koszt 1 → 0 | 🟡 ** 84.1** | `-0.20 pkt` | 5.98 | 0.9% | 0.1% |
| `MUT_CAA-08_COST_MINUS1` | CAA-08 (Kaptur Nocy) [Buff Autopodatku]: koszt 1 → 0 | 🟡 ** 84.0** | `-0.30 pkt` | 5.98 | 1.0% | 0.1% |
| `MUT_CAA-08_GOLD_SET1` | CAA-08 (Kaptur Nocy) [Buff Autopodatku]: dodaj złoto = 1 | 🟡 ** 84.0** | `-0.30 pkt` | 5.98 | 1.0% | 0.1% |
| `MUT_CAA-11_COST_MINUS1` | CAA-11 (Nocna Zmiana Warty) [Buff Autopodatku]: koszt 1 → 0 | 🟡 ** 84.0** | `-0.30 pkt` | 5.98 | 1.0% | 0.1% |
| `MUT_CAA-11_GOLD_SET1` | CAA-11 (Nocna Zmiana Warty) [Buff Autopodatku]: dodaj złoto = 1 | 🟡 ** 84.0** | `-0.30 pkt` | 5.98 | 1.0% | 0.1% |
| `MUT_KT-01_GOLD_SET1` | KT-01 (Rytuał Przejścia) [Buff Autopodatku]: dodaj złoto = 1 | 🟡 ** 84.0** | `-0.30 pkt` | 5.98 | 1.0% | 0.1% |
| `MUT_KT-04_GOLD_SET1` | KT-04 (Zwierciadło Herezji) [Buff Autopodatku]: dodaj złoto = 1 | 🟡 ** 84.0** | `-0.30 pkt` | 5.98 | 1.0% | 0.1% |
| `MUT_KT-11_GOLD_PLUS1` | KT-11 (Medytacja Sefirot) [Buff Autopodatku]: złoto 1 → 2 | 🟡 ** 84.0** | `-0.30 pkt` | 5.98 | 1.0% | 0.1% |
| `MUT_KT-12_HERESY_MINUS1` | KT-12 (Strażnik Archiwum) [Buff Autopodatku]: herezja 1 → 0 | 🟡 ** 84.0** | `-0.30 pkt` | 5.98 | 1.0% | 0.1% |
| `MUT_CAA-08_COST_MINUS1__MUT_CAA-11_COST_MINUS1` | CAA-08 (Kaptur Nocy) [Buff Autopodatku]: koszt 1 → 0 + CAA-11 (Nocna Zmiana Warty) [Buff Autopodatku]: koszt 1 → 0 | 🟡 ** 84.0** | `-0.30 pkt` | 5.98 | 1.0% | 0.1% |
| `MUT_CAA-08_COST_MINUS1__MUT_CAA-11_GOLD_SET1` | CAA-08 (Kaptur Nocy) [Buff Autopodatku]: koszt 1 → 0 + CAA-11 (Nocna Zmiana Warty) [Buff Autopodatku]: dodaj złoto = 1 | 🟡 ** 84.0** | `-0.30 pkt` | 5.98 | 1.0% | 0.1% |
| `MUT_CAA-08_COST_MINUS1__MUT_KT-01_GOLD_SET1` | CAA-08 (Kaptur Nocy) [Buff Autopodatku]: koszt 1 → 0 + KT-01 (Rytuał Przejścia) [Buff Autopodatku]: dodaj złoto = 1 | 🟡 ** 84.0** | `-0.30 pkt` | 5.98 | 1.0% | 0.1% |
| `MUT_CAA-08_GOLD_SET1__MUT_CAA-11_COST_MINUS1` | CAA-08 (Kaptur Nocy) [Buff Autopodatku]: dodaj złoto = 1 + CAA-11 (Nocna Zmiana Warty) [Buff Autopodatku]: koszt 1 → 0 | 🟡 ** 84.0** | `-0.30 pkt` | 5.98 | 1.0% | 0.1% |
| `MUT_CAA-08_GOLD_SET1__MUT_CAA-11_GOLD_SET1` | CAA-08 (Kaptur Nocy) [Buff Autopodatku]: dodaj złoto = 1 + CAA-11 (Nocna Zmiana Warty) [Buff Autopodatku]: dodaj złoto = 1 | 🟡 ** 84.0** | `-0.30 pkt` | 5.98 | 1.0% | 0.1% |
| `MUT_CAA-08_GOLD_SET1__MUT_KT-01_GOLD_SET1` | CAA-08 (Kaptur Nocy) [Buff Autopodatku]: dodaj złoto = 1 + KT-01 (Rytuał Przejścia) [Buff Autopodatku]: dodaj złoto = 1 | 🟡 ** 84.0** | `-0.30 pkt` | 5.98 | 1.0% | 0.1% |
| `MUT_CAA-11_COST_MINUS1__MUT_KT-01_GOLD_SET1` | CAA-11 (Nocna Zmiana Warty) [Buff Autopodatku]: koszt 1 → 0 + KT-01 (Rytuał Przejścia) [Buff Autopodatku]: dodaj złoto = 1 | 🟡 ** 84.0** | `-0.30 pkt` | 5.98 | 1.0% | 0.1% |
| `MUT_CAA-11_GOLD_SET1__MUT_KT-01_GOLD_SET1` | CAA-11 (Nocna Zmiana Warty) [Buff Autopodatku]: dodaj złoto = 1 + KT-01 (Rytuał Przejścia) [Buff Autopodatku]: dodaj złoto = 1 | 🟡 ** 84.0** | `-0.30 pkt` | 5.98 | 1.0% | 0.1% |
| `MUT_KT-01_COST_MINUS1` | KT-01 (Rytuał Przejścia) [Buff Autopodatku]: koszt 1 → 0 | 🟡 ** 84.0** | `-0.30 pkt` | 5.98 | 0.9% | 0.1% |
| `MUT_CAA-08_COST_MINUS1__MUT_KT-01_COST_MINUS1` | CAA-08 (Kaptur Nocy) [Buff Autopodatku]: koszt 1 → 0 + KT-01 (Rytuał Przejścia) [Buff Autopodatku]: koszt 1 → 0 | 🟡 ** 84.0** | `-0.30 pkt` | 5.98 | 0.9% | 0.1% |
| `MUT_CAA-08_GOLD_SET1__MUT_KT-01_COST_MINUS1` | CAA-08 (Kaptur Nocy) [Buff Autopodatku]: dodaj złoto = 1 + KT-01 (Rytuał Przejścia) [Buff Autopodatku]: koszt 1 → 0 | 🟡 ** 84.0** | `-0.30 pkt` | 5.98 | 0.9% | 0.1% |