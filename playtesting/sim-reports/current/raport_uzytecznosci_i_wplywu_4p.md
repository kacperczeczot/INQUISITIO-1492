# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v0.56

**Wersja Gry:** `v0.56` | **Data Badania:** 2026-08-16 14:47 | **Próba:** 3000 gier/setup (15000 gier na wariant) | **Ziarno:** 42
**Wynik Bazowy Kanonu 4P:** 🟢 ** 94.9** pkt | **Średnia Długość Partii:** `5.47 Er` | **Deadlocki:** `0.4%` | **Pas Biedy:** `25.3%`

---

## 1. 🗺️ Podsumowanie Ekosystemu Kanonu 4P (Matryca Wpływu Kart 3x3)

Rozkład wszystkich 50 kart frakcyjnych w matrycy **Wpływ na Frakcję ($\Delta \text{Share}$)** vs **Wpływ na Kanon 4P ($\Delta \text{4P Score}$)**:

| Kategoria Karty | Liczba Kart | Udział w Talii | Rola w Balansie Kanonu 4P | Działanie Projektowe |
| :--- | :---: | :---: | :--- | :--- |
| 👑 / ⚓ **Filar / Kotwica Kanonu** | **0** | 0% | Kluczowe karty napędowe frakcji lub kotwice chroniące Kanon 4P | **Nienaruszalne (Kanon)** |
| ⚖️ **Zbalansowane Narzędzie** | **0** | 0% | Płynne narzędzia taktyczne o zrównoważonym profilu w 4P | **Optymalne** |
| 💤 **Karta Pasywna (Dead Weight)** | **50** | 100% | Znikomy wpływ na tempo i wynik partii w 4P | **Kandydaci do wzmocnienia** |
| ⚠️ **Karta Destabilizująca (Disruptor)** | **0** | 0% | Ich usunięcie podnosi 4P Score | **Kandydaci do osłabienia/reworku** |

---

## 2. 🃏 Warstwa I — Szczegółowa Analiza 50 Kart Frakcji w Kanonie 4P

### 2.1. 👑 Filar i Kotwice Kanonu 4P (Karty o Najsilniejszym Wpływie Stabilizującym)
Karty, których brak powoduje spadek wyniku Kanonu 4P o $\ge 4.0$ pkt lub załamanie winrate frakcji o $\ge 4.0\%$:

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |

### 2.2. ⚠️ Karty Destabilizujące Kanon 4P (Disruptors)
Karty, których wyłączenie podnosi 4P Score ($\Delta \text{4P} \ge +1.5$ pkt):

| Karta | Frakcja | Koszt / Herezja | Rola w Matrycy 4P | Win Share Frakcji (Baza → Bez) | $\Delta$ Frakcji | 4P Score po Wyłączeniu |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *Brak kart destabilizujących* | - | - | - | - | - | - |

### 2.3. 📋 Pełny Wykaz Ablacji Wszystkich 50 Kart Frakcji w Kanonie 4P

| ID | Nazwa Karty | Frakcja | Koszt | Herezja | Faction Win Share 4P | $\Delta$ Frakcji | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Rola w Matrycy 4P |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `caa-01` | **Przejście Podziemiami** | Cienie Al-Andalus | 0 | 0 | 24.7% → 24.7% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `caa-03` | **Cień na Rynku** | Cienie Al-Andalus | 0 | 1 | 24.7% → 24.7% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `caa-02` | **Złoto z Kryjówki** | Cienie Al-Andalus | 1 | 0 | 24.7% → 24.7% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `caa-04` | **Fałszywy Trop** | Cienie Al-Andalus | 1 | 0 | 24.7% → 24.7% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `caa-05` | **Ukryty Kurier** | Cienie Al-Andalus | 1 | 0 | 24.7% → 24.7% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `caa-07` | **Szantaż Bractwa** | Cienie Al-Andalus | 1 | 0 | 24.7% → 24.7% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `caa-06` | **Ucieczka z Lochów** | Cienie Al-Andalus | 2 | 1 | 24.7% → 24.7% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `caa-08` | **Kaptur Nocy** | Cienie Al-Andalus | 2 | 1 | 24.7% → 24.7% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `caa-10` | **Echo Alhambry** | Cienie Al-Andalus | 0 | 1 | 24.7% → 24.7% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `caa-09` | **Kurier Relikwii** | Cienie Al-Andalus | 2 | 0 | 24.7% → 24.7% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `gc-04` | **Informator** | Gildia Cieni | 0 | 1 | 24.0% → 24.0% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `gc-05` | **Fałszywy Świadek** | Gildia Cieni | 0 | 0 | 24.0% → 24.0% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `gc-01` | **Przekupiony Strażnik** | Gildia Cieni | 1 | 1 | 24.0% → 24.0% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `gc-03` | **Podrzucenie Księgi** | Gildia Cieni | 1 | 0 | 24.0% → 24.0% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `gc-02` | **Czarny Rynek** | Gildia Cieni | 2 | 1 | 24.0% → 24.0% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `gc-06` | **Szantaż** | Gildia Cieni | 2 | 0 | 24.0% → 24.0% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `gc-07` | **Skrytobójstwo** | Gildia Cieni | 2 | 0 | 24.0% → 24.0% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `gc-08` | **Zatrute Złoto** | Gildia Cieni | 2 | 0 | 24.0% → 24.0% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `gc-09` | **Lista Dłużników** | Gildia Cieni | 2 | 0 | 24.0% → 24.0% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `gc-10` | **Upadek Domu** | Gildia Cieni | 4 | 2 | 24.0% → 24.0% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `kb-01` | **Rozkaz Dworu** | Korona & Borgiowie | 1 | 0 | 25.4% → 25.4% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `kb-02` | **Pobór Podatków** | Korona & Borgiowie | 1 | 0 | 25.4% → 25.4% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `kb-03` | **Plotka Dworska** | Korona & Borgiowie | 1 | 0 | 25.4% → 25.4% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `kb-04` | **Faworyt Dworu** | Korona & Borgiowie | 2 | 1 | 25.4% → 25.4% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `kb-05` | **List Żelazny** | Korona & Borgiowie | 2 | 0 | 25.4% → 25.4% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `kb-06` | **Areszt Królewski** | Korona & Borgiowie | 1 | 0 | 25.4% → 25.4% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `kb-07` | **Szantaż Pieczęcią** | Korona & Borgiowie | 2 | 0 | 25.4% → 25.4% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `kb-08` | **Przekupstwo Sędziego** | Korona & Borgiowie | 3 | 0 | 25.4% → 25.4% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `kb-10` | **Pieczęć Korony** | Korona & Borgiowie | 2 | 2 | 25.4% → 25.4% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `kb-09` | **Dekret Królewski** | Korona & Borgiowie | 3 | 1 | 25.4% → 25.4% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `kt-03` | **Zakazana Wiedza** | Kabała z Toledo | 0 | 1 | 25.3% → 25.3% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `kt-04` | **Zwierciadło Herezji** | Kabała z Toledo | 0 | 0 | 25.3% → 25.3% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `kt-01` | **Rytuał Przejścia** | Kabała z Toledo | 1 | 0 | 25.3% → 25.3% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `kt-02` | **Transmutacja Złota** | Kabała z Toledo | 1 | 0 | 25.3% → 25.3% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `kt-05` | **Wskazówka Cyklu** | Kabała z Toledo | 1 | 0 | 25.3% → 25.3% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `kt-07` | **Archiwum Ukryte** | Kabała z Toledo | 1 | 1 | 25.3% → 25.3% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `kt-06` | **Przesłuchanie Imienia** | Kabała z Toledo | 2 | 0 | 25.3% → 25.3% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `kt-08` | **Areszt Wiedzy** | Kabała z Toledo | 2 | 0 | 25.3% → 25.3% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `kt-09` | **Fragment Kodeksu** | Kabała z Toledo | 1 | 1 | 25.3% → 25.3% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `kt-10` | **Pieczęć Salomona** | Kabała z Toledo | 2 | 1 | 25.3% → 25.3% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `so-05` | **Wezwanie do Trybunału** | Święte Oficjum | 0 | 0 | 25.6% → 25.6% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `so-01` | **Patrol Familiariuszy** | Święte Oficjum | 1 | 0 | 25.6% → 25.6% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `so-02` | **Skarbiec Trybunału** | Święte Oficjum | 1 | 0 | 25.6% → 25.6% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `so-04` | **Publiczne Ostrzeżenie** | Święte Oficjum | 1 | 0 | 25.6% → 25.6% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `so-03` | **Podejrzenie** | Święte Oficjum | 2 | 0 | 25.6% → 25.6% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `so-08` | **Nasłanie Inkwizytora** | Święte Oficjum | 1 | 0 | 25.6% → 25.6% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `so-06` | **Areszt Trybunalski** | Święte Oficjum | 2 | 0 | 25.6% → 25.6% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `so-07` | **Przesłuchanie Oficjum** | Święte Oficjum | 2 | 0 | 25.6% → 25.6% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `so-09` | **Świadek Koronny** | Święte Oficjum | 2 | 0 | 25.6% → 25.6% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |
| `so-10` | **Oczyść Miasto** | Święte Oficjum | 5 | 2 | 25.6% → 25.6% | `+0.0%` | 94.9 | `0.0` | 5.47 | 0.4% | 💤 KARTA PASYWNA (Dead Weight) |

---

## 3. ⏳ Warstwa II — Kronika Dziejów w 4P (Ablacja 8 Kart Wydarzeń Czasu)

Badanie wpływu wyłączenia każdej pojedynczej karty z **Talii Czasu** na tempo gry, poziom deadlocków i ogólny balans w 4P:

| ID | Karta Wydarzenia | 4P Score | $\Delta$ 4P | Średnia Er | Deadlock % | Status Roli w Kronice |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `tc-01` | **Kres Średniowiecza** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | ⚖️ Neutralna Kronika |
| `tc-02` | **Płonący Stos** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | ⚖️ Neutralna Kronika |
| `tc-03` | **Królewski Podatek** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | ⚖️ Neutralna Kronika |
| `tc-04` | **Spisek w Cieniu** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | ⚖️ Neutralna Kronika |
| `tc-05` | **Złoty Wiek** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | ⚖️ Neutralna Kronika |
| `tc-06` | **Czystka w Mieście** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | ⚖️ Neutralna Kronika |
| `tc-07` | **Druga Szansa** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | ⚖️ Neutralna Kronika |
| `tc-08` | **Zaćmienie Słońca** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | ⚖️ Neutralna Kronika |

---

## 4. ⚙️ Warstwa III — Globalne Mechaniki i Parametry Silnika w 4P

Badanie odporności Kanonu 4P na wyłączenie lub skrajne przestawienie bazowych parametrów silnika:

| Badany Podsystem / Parametr | 4P Score | $\Delta$ 4P | Średnia Er | Deadlocks % | Pas Biedy % | Diagnoza i Wpływ na Silnik |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Wyłączone Autodafé Inkwizytora** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | 25.3% | ⚪ Wpływ neutralny / mechanika stabilna |
| **Wyłączony Trybunał i Oskarżenia** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | 25.3% | ⚪ Wpływ neutralny / mechanika stabilna |
| **Wyłączona Kronika Dziejów (Talia Czasu)** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | 25.3% | ⚪ Wpływ neutralny / mechanika stabilna |
| **Autodafé Cooldown = 2 Ery (Agresywna czystka)** | 94.9 → 🟢 ** 94.1** (`-0.8`) | `-0.8 pkt` | 5.47 Er | 0.5% | 25.3% | ⚪ Wpływ neutralny / mechanika stabilna |
| **Autodafé Cooldown = 4 Ery (Rzadka czystka)** | 94.9 → 🟢 ** 94.6** (`-0.3`) | `-0.3 pkt` | 5.47 Er | 0.5% | 25.3% | ⚪ Wpływ neutralny / mechanika stabilna |

---

## 5. ⚔️ Warstwa IV — Asymetryczne Ścieżki Zwycięstwa w 4P (Victory Paths)

Badanie krytyczności i elastyczności unikalnych bramek zwycięstwa dla każdej frakcji w Kanonie 4P:

| Badana Ścieżka / Bramka Wygranej | 4P Score | $\Delta$ 4P | Średnia Er | Deadlocks % | Pas Biedy % | Diagnoza Ścieżki Zwycięstwa |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: Brak wygranej ze Stosów** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | 25.3% | ⚪ Ścieżka alternatywna / opcjonalna |
| **Święte Oficjum: Brak wygranej ze Skazań** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | 25.3% | ⚪ Ścieżka alternatywna / opcjonalna |
| **Cienie: Brak wygranej przez Marionetkę** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | 25.3% | ⚪ Ścieżka alternatywna / opcjonalna |
| **Cienie: Brak wygranej ze Szlaku Morskiego** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | 25.3% | ⚪ Ścieżka alternatywna / opcjonalna |
| **Korona: Wymóg 0 Haków (Tylko Dekrety)** | 🟢 ** 94.9** | `0.0 pkt` | 5.47 Er | 0.4% | 25.3% | ⚪ Ścieżka alternatywna / opcjonalna |

---

## 6. 👥 Warstwa V — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych w Kanonie 4P:

| Nieobecna Frakcja | Setup Testowy | 4P Score Setupu | Diagnoza Wpływu Braku Frakcji na Stół 4P |
| :--- | :--- | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`99.3 pkt`** | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`94.8 pkt`** | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`92.5 pkt`** | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`92.6 pkt`** | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`95.4 pkt`** | Brak presji stosów i bezpośredniego Inkwizytora |