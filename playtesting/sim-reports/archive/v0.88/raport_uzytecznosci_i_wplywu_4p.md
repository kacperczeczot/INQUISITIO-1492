# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v0.88

**Wersja Gry:** `v0.88` | **Data Badania:** 2026-08-17 13:20 | **Próba:** 400 gier/setup (2000 gier na wariant) | **Ziarno:** 42
**Wynik Bazowy Kanonu 4P:** 🔴 ** 34.7** pkt | **Średnia Długość Partii:** `5.98 Er` | **Deadlocki:** `1.1%` | **Pas Biedy:** `5.6%`

**Tryb:** `--no-cards` — raport bez ablacji kart frakcji i kroniki (tylko L1/L2/L4 i stoły 4P).

---


---

## 4. ⚙️ Warstwa III — Matryca 9 Obszarów Wpływu Mechanik Gry (L1, L2, L4)

Zestawienie odporności Kanonu 4P na modyfikacje i ablację poszczególnych podsystemów. **Δ≈0 nie jest harmonią** — to klauzula, której gracze nie czują.

| Kategoria Mechaniki | Liczba Testów | Rola w Ekosystemie Kanonu 4P | Rekomendacja Balansowa |
| :--- | :---: | :--- | :--- |
| 👑 / 🛡️ **Filary i Bezpieczniki Stabilizujące** | **27** | Mechaniki krytyczne — ich brak lub rozregulowanie niszczy balans | **Nienaruszalny Kanon** |
| ⚖️ **Zbalansowane Regulatory** | **1** | Mechaniki, które ruszają share, ale nie walą w 4P Score | **Optymalne w Kanonie** |
| 💤 **Martwe Mechaniki (Δ≈0)** | **18** | Ablacja nic albo prawie nic nie zmienia — klauzula nie gra | **Ożywić albo wyciąć** |
| ⚠️ / 💡 **Obciążenia i Kandydaci do Uproszczenia** | **2** | Mechaniki, których modyfikacja lub redukcja podnosi wynik 4P | **Kandydaci do optymalizacji** |

### 4.0. 💤 Martwe mechaniki (osobny wykaz)
Testy z $|\Delta\text{4P}| \le 0.8$ i ruchem share $\le 1.5$ pp. To nie jest „optymalny kanon”.

| Badany Podsystem | Kategoria | 4P Score | $\Delta$ 4P | Klasyfikacja |
| :--- | :--- | :---: | :---: | :--- |
| **Limit Er: 12 → 16 Er (Wydłużony silnik)** | Poziom 1: System Core | 🔴 ** 34.7** | `0.0 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Święte Oficjum: Wymóg Skazań +2 (Zamiast 2-3)** | Poziom 2: Warunki Zwycięstwa | 34.7 → 🔴 ** 34.9** (`⬆️ +0.2`) | `+0.2 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Szlak Morski: Odblokowanie w Erze 6 (Późne)** | Poziom 4: Warianty i Modyfikatory | 34.7 → 🔴 ** 35.1** (`⬆️ +0.4`) | `+0.4 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Kabała: Próg Górny Pasma 9 → 11 (Rozszerzenie w górę)** | Poziom 2: Warunki Zwycięstwa | 34.7 → 🔴 ** 33.6** (`-1.1`) | `-1.1 pkt` | 💤 MARTWA MECHANIKA (Low Impact) |
| **Gildia: Wymóg Upadków (bez Oficjum) 3 → 2** | Poziom 2: Warunki Zwycięstwa | 34.7 → 🔴 ** 33.3** (`-1.4`) | `-1.4 pkt` | 💤 MARTWA MECHANIKA (Low Impact) |
| **Kabała: Próg Górny Pasma 9 → 7 (Zawężenie od góry)** | Poziom 2: Warunki Zwycięstwa | 34.7 → 🔴 ** 33.3** (`-1.4`) | `-1.4 pkt` | 💤 MARTWA MECHANIKA (Low Impact) |
| **Kabała: Wymóg Ery 6 → Era 4** | Poziom 2: Warunki Zwycięstwa | 34.7 → 🔴 ** 32.6** (`-2.1`) | `-2.1 pkt` | 💤 MARTWA MECHANIKA (Low Impact) |
| **Gildia: Wymóg Upadków (bez Oficjum) 3 → 4** | Poziom 2: Warunki Zwycięstwa | 34.7 → 🔴 ** 31.6** (`-3.1`) | `-3.1 pkt` | 💤 MARTWA MECHANIKA (Low Impact) |
| **Próg Oskarżenia na Dworze: +1 (Pasywny Dwór)** | Poziom 1: System Core | 34.7 → 🔴 ** 31.6** (`-3.1`) | `-3.1 pkt` | 💤 MARTWA MECHANIKA (Low Impact) |

### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)

| Badany Podsystem / Modyfikator L1 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Limit Er: 12 → 8 Er (Presja czasu)** | 34.7 → 🔴 **  3.6** (`-31.1`) | `-31.1 pkt` | 5.75 Er | 25.0% | 5.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit Er: 12 → 16 Er (Wydłużony silnik)** | 🔴 ** 34.7** | `0.0 pkt` | 5.99 Er | 0.0% | 5.6% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Próg Oskarżenia na Dworze: -1 (Agresywny Dwór)** | 34.7 → 🔴 ** 30.7** (`-4.0`) | `-4.0 pkt` | 6.09 Er | 1.4% | 5.0% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Próg Oskarżenia na Dworze: +1 (Pasywny Dwór)** | 34.7 → 🔴 ** 31.6** (`-3.1`) | `-3.1 pkt` | 5.90 Er | 0.7% | 6.1% | 💤 MARTWA MECHANIKA (Low Impact) |
| **Złoto startowe: 4zł → 0zł (Skrajne ubóstwo)** | 34.7 → 🔴 ** 13.5** (`-21.2`) | `-21.2 pkt` | 7.06 Er | 3.8% | 17.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 6zł (Bogaty start)** | 34.7 → 🔴 ** 11.7** (`-23.0`) | `-23.0 pkt` | 5.31 Er | 0.2% | 3.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 2 Agentów (Ograniczony zasięg)** | 34.7 → 🔴 ** 30.6** (`-4.1`) | `-4.1 pkt` | 6.19 Er | 2.0% | 5.9% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Liczba Agentów: 3 → 4 Agentów (Gęsta plansza)** | 34.7 → 🔴 ** 31.2** (`-3.5`) | `-3.5 pkt` | 5.85 Er | 0.5% | 5.7% | ⚖️ ZBALANSOWANY REGULATOR (Balanced Regulator) |
| **Limit kart na ręce: 5 → 3 karty (Zmniejszona elastyczność)** | 34.7 → 🔴 ** 24.5** (`-10.2`) | `-10.2 pkt` | 6.58 Er | 1.9% | 9.9% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Limit kart na ręce: 5 → 7 kart (Pełna swoboda)** | 34.7 → 🔴 ** 27.5** (`-7.2`) | `-7.2 pkt` | 5.62 Er | 0.8% | 5.0% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Autodafé Inkwizytora: Cooldown 2 Ery (Częsta czystka)** | 34.7 → 🔴 ** 25.9** (`-8.8`) | `-8.8 pkt` | 5.72 Er | 0.8% | 5.7% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Autodafé Inkwizytora: Cooldown 4 Ery (Rzadka czystka)** | 34.7 → 🔴 ** 29.5** (`-5.2`) | `-5.2 pkt` | 6.19 Er | 1.7% | 5.3% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Autodafé Inkwizytora: Całkowity brak czystki** | 34.7 → 🔴 ** 19.4** (`-15.3`) | `-15.3 pkt` | 6.46 Er | 2.9% | 4.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)

| Badany Warunek Zwycięstwa L2 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: Wymóg Stosów +2** | 34.7 → 🔴 ** 30.2** (`-4.5`) | `-4.5 pkt` | 6.22 Er | 2.6% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: Wymóg Stosów -1** | 34.7 → 🔴 ** 23.3** (`-11.4`) | `-11.4 pkt` | 5.72 Er | 0.6% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: Wymóg Skazań +2 (Zamiast 2-3)** | 34.7 → 🔴 ** 34.9** (`⬆️ +0.2`) | `+0.2 pkt` | 5.98 Er | 1.1% | 5.6% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Święte Oficjum: Wymóg Skazań -1** | 34.7 → 🟠 ** 64.3** (`⬆️ +29.6`) | `+29.6 pkt` | 5.82 Er | 0.8% | 5.6% | ⚠️ KRYTYCZNA WADA (Critical Flaw) |
| **Cienie: Wymóg Relikwii 2 → 4** | 34.7 → 🔴 ** 12.5** (`-22.2`) | `-22.2 pkt` | 6.49 Er | 1.4% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Cienie: Wymóg Relikwii 2 → 1** | 34.7 → 🔴 **  8.4** (`-26.3`) | `-26.3 pkt` | 4.99 Er | 0.2% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: Wymóg Dekretów 2 → 3** | 34.7 → 🔴 ** 12.2** (`-22.5`) | `-22.5 pkt` | 6.46 Er | 2.5% | 5.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: Wymóg Dekretów 2 → 1** | 34.7 → 🔴 **  5.6** (`-29.1`) | `-29.1 pkt` | 3.09 Er | 0.1% | 4.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: Wymóg Haków +2** | 34.7 → 🔴 ** 30.3** (`-4.4`) | `-4.4 pkt` | 6.21 Er | 1.2% | 5.7% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Kabała: Wymóg Fragmentów 3 → 4** | 34.7 → 🔴 ** 22.2** (`-12.5`) | `-12.5 pkt` | 6.21 Er | 1.7% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: Wymóg Fragmentów 3 → 2** | 34.7 → 🔴 ** 20.8** (`-13.9`) | `-13.9 pkt` | 5.68 Er | 0.9% | 5.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: Wymóg Ery 6 → Era 4** | 34.7 → 🔴 ** 32.6** (`-2.1`) | `-2.1 pkt` | 5.83 Er | 1.1% | 5.5% | 💤 MARTWA MECHANIKA (Low Impact) |
| **Kabała: Wymóg Ery 6 → Era 8** | 34.7 → 🔴 ** 29.1** (`-5.6`) | `-5.6 pkt` | 6.16 Er | 1.1% | 5.6% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Kabała: Próg Górny Pasma 9 → 7 (Zawężenie od góry)** | 34.7 → 🔴 ** 33.3** (`-1.4`) | `-1.4 pkt` | 6.03 Er | 1.1% | 5.6% | 💤 MARTWA MECHANIKA (Low Impact) |
| **Kabała: Próg Górny Pasma 9 → 11 (Rozszerzenie w górę)** | 34.7 → 🔴 ** 33.6** (`-1.1`) | `-1.1 pkt` | 5.93 Er | 0.6% | 5.6% | 💤 MARTWA MECHANIKA (Low Impact) |
| **Kabała: Całe Pasmo Wąskie (4–6)** | 34.7 → 🔴 ** 28.8** (`-5.9`) | `-5.9 pkt` | 6.11 Er | 1.5% | 5.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Gildia: Wymóg Upadków (z Oficjum) 2 → 3** | 34.7 → 🔴 ** 25.9** (`-8.8`) | `-8.8 pkt` | 6.22 Er | 1.2% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: Wymóg Upadków (z Oficjum) 2 → 1** | 34.7 → 🔴 ** 23.5** (`-11.2`) | `-11.2 pkt` | 5.53 Er | 0.7% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: Wymóg Upadków (bez Oficjum) 3 → 4** | 34.7 → 🔴 ** 31.6** (`-3.1`) | `-3.1 pkt` | 6.03 Er | 1.2% | 5.6% | 💤 MARTWA MECHANIKA (Low Impact) |
| **Gildia: Wymóg Upadków (bez Oficjum) 3 → 2** | 34.7 → 🔴 ** 33.3** (`-1.4`) | `-1.4 pkt` | 5.91 Er | 0.9% | 5.6% | 💤 MARTWA MECHANIKA (Low Impact) |

### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)

| Badany Wariant / Modyfikator L4 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kronika Dziejów: Całkowite wyłączenie edyktów czasu** | 34.7 → 🔴 ** 18.5** (`-16.2`) | `-16.2 pkt` | 6.39 Er | 2.8% | 6.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kronika Dziejów: Częstotliwość co 2 Ery** | 34.7 → 🔴 ** 24.9** (`-9.8`) | `-9.8 pkt` | 6.27 Er | 2.2% | 5.9% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Werdykt Sądu: Tajny (brak koordynacji anty-snowball)** | 34.7 → 🔴 ** 24.3** (`-10.4`) | `-10.4 pkt` | 5.50 Er | 0.4% | 5.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Szlak Morski: Odblokowanie w Erze 6 (Późne)** | 34.7 → 🔴 ** 35.1** (`⬆️ +0.4`) | `+0.4 pkt` | 5.96 Er | 1.0% | 5.6% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Inkwizytor Patrol: Ruch 0 pól (Stacjonarny)** | 34.7 → 🔴 ** 27.5** (`-7.2`) | `-7.2 pkt` | 6.00 Er | 1.0% | 5.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Inkwizytor Patrol: Ruch 2 pola (Szybki patrol)** | 34.7 → 🔴 ** 36.3** (`⬆️ +1.6`) | `+1.6 pkt` | 5.94 Er | 0.8% | 5.6% | 💡 KANDYDAT DO UPROSZCZENIA (Simplification) |

---

## 5. 👥 Warstwa IV — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych w Kanonie 4P:

| Nieobecna Frakcja | Setup Testowy | 4P Score Setupu | Diagnoza Wpływu Braku Frakcji na Stół 4P |
| :--- | :--- | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`27.1 pkt`** | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`28.0 pkt`** | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`26.2 pkt`** | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`26.4 pkt`** | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`66.0 pkt`** | Brak presji stosów i bezpośredniego Inkwizytora |