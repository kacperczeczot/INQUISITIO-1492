# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v0.87

**Wersja Gry:** `v0.87` | **Data Badania:** 2026-08-17 13:19 | **Próba:** 400 gier/setup (2000 gier na wariant) | **Ziarno:** 42
**Wynik Bazowy Kanonu 4P:** 🔴 ** 35.1** pkt | **Średnia Długość Partii:** `5.96 Er` | **Deadlocki:** `1.0%` | **Pas Biedy:** `5.6%`

**Tryb:** `--no-cards` — raport bez ablacji kart frakcji i kroniki (tylko L1/L2/L4 i stoły 4P).

---


---

## 4. ⚙️ Warstwa III — Matryca 9 Obszarów Wpływu Mechanik Gry (L1, L2, L4)

Zestawienie odporności Kanonu 4P na modyfikacje i ablację poszczególnych podsystemów. **Δ≈0 nie jest harmonią** — to klauzula, której gracze nie czują.

| Kategoria Mechaniki | Liczba Testów | Rola w Ekosystemie Kanonu 4P | Rekomendacja Balansowa |
| :--- | :---: | :--- | :--- |
| 👑 / 🛡️ **Filary i Bezpieczniki Stabilizujące** | **27** | Mechaniki krytyczne — ich brak lub rozregulowanie niszczy balans | **Nienaruszalny Kanon** |
| ⚖️ **Zbalansowane Regulatory** | **2** | Mechaniki, które ruszają share, ale nie walą w 4P Score | **Optymalne w Kanonie** |
| 💤 **Martwe Mechaniki (Δ≈0)** | **18** | Ablacja nic albo prawie nic nie zmienia — klauzula nie gra | **Ożywić albo wyciąć** |
| ⚠️ / 💡 **Obciążenia i Kandydaci do Uproszczenia** | **1** | Mechaniki, których modyfikacja lub redukcja podnosi wynik 4P | **Kandydaci do optymalizacji** |

### 4.0. 💤 Martwe mechaniki (osobny wykaz)
Testy z $|\Delta\text{4P}| \le 0.8$ i ruchem share $\le 1.5$ pp. To nie jest „optymalny kanon”.

| Badany Podsystem | Kategoria | 4P Score | $\Delta$ 4P | Klasyfikacja |
| :--- | :--- | :---: | :---: | :--- |
| **Limit Er: 12 → 16 Er (Wydłużony silnik)** | Poziom 1: System Core | 🔴 ** 35.1** | `0.0 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Szlak Morski: Odblokowanie w Erze 6 (Późne)** | Poziom 4: Warianty i Modyfikatory | 🔴 ** 35.1** | `0.0 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Święte Oficjum: Wymóg Skazań +2 (Zamiast 2-3)** | Poziom 2: Warunki Zwycięstwa | 35.1 → 🔴 ** 35.2** (`⬆️ +0.1`) | `+0.1 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Kabała: Próg Górny Pasma 9 → 11 (Rozszerzenie w górę)** | Poziom 2: Warunki Zwycięstwa | 35.1 → 🔴 ** 34.0** (`-1.1`) | `-1.1 pkt` | 💤 MARTWA MECHANIKA (Low Impact) |
| **Inkwizytor Patrol: Ruch 2 pola (Szybki patrol)** | Poziom 4: Warianty i Modyfikatory | 35.1 → 🔴 ** 36.3** (`⬆️ +1.2`) | `+1.2 pkt` | 💤 MARTWA MECHANIKA (Low Impact) |
| **Gildia: Wymóg Upadków (bez Oficjum) 3 → 2** | Poziom 2: Warunki Zwycięstwa | 35.1 → 🔴 ** 33.7** (`-1.4`) | `-1.4 pkt` | 💤 MARTWA MECHANIKA (Low Impact) |
| **Kabała: Próg Górny Pasma 9 → 7 (Zawężenie od góry)** | Poziom 2: Warunki Zwycięstwa | 35.1 → 🔴 ** 33.7** (`-1.4`) | `-1.4 pkt` | 💤 MARTWA MECHANIKA (Low Impact) |
| **Próg Oskarżenia na Dworze: +1 (Pasywny Dwór)** | Poziom 1: System Core | 35.1 → 🔴 ** 31.8** (`-3.3`) | `-3.3 pkt` | 💤 MARTWA MECHANIKA (Low Impact) |
| **Gildia: Wymóg Upadków (bez Oficjum) 3 → 4** | Poziom 2: Warunki Zwycięstwa | 35.1 → 🔴 ** 31.6** (`-3.5`) | `-3.5 pkt` | 💤 MARTWA MECHANIKA (Low Impact) |

### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)

| Badany Podsystem / Modyfikator L1 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Limit Er: 12 → 8 Er (Presja czasu)** | 35.1 → 🔴 **  3.9** (`-31.2`) | `-31.2 pkt` | 5.74 Er | 24.6% | 5.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit Er: 12 → 16 Er (Wydłużony silnik)** | 🔴 ** 35.1** | `0.0 pkt` | 5.97 Er | 0.0% | 5.6% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Próg Oskarżenia na Dworze: -1 (Agresywny Dwór)** | 35.1 → 🔴 ** 30.6** (`-4.5`) | `-4.5 pkt` | 6.08 Er | 1.4% | 5.0% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Próg Oskarżenia na Dworze: +1 (Pasywny Dwór)** | 35.1 → 🔴 ** 31.8** (`-3.3`) | `-3.3 pkt` | 5.89 Er | 0.7% | 6.1% | 💤 MARTWA MECHANIKA (Low Impact) |
| **Złoto startowe: 4zł → 0zł (Skrajne ubóstwo)** | 35.1 → 🔴 ** 13.3** (`-21.8`) | `-21.8 pkt` | 7.05 Er | 3.8% | 17.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 6zł (Bogaty start)** | 35.1 → 🔴 ** 11.4** (`-23.7`) | `-23.7 pkt` | 5.31 Er | 0.3% | 3.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 2 Agentów (Ograniczony zasięg)** | 35.1 → 🔴 ** 30.5** (`-4.6`) | `-4.6 pkt` | 6.19 Er | 2.0% | 5.8% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Liczba Agentów: 3 → 4 Agentów (Gęsta plansza)** | 35.1 → 🔴 ** 31.6** (`-3.5`) | `-3.5 pkt` | 5.84 Er | 0.5% | 5.6% | ⚖️ ZBALANSOWANY REGULATOR (Balanced Regulator) |
| **Limit kart na ręce: 5 → 3 karty (Zmniejszona elastyczność)** | 35.1 → 🔴 ** 24.4** (`-10.7`) | `-10.7 pkt` | 6.58 Er | 1.9% | 9.9% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Limit kart na ręce: 5 → 7 kart (Pełna swoboda)** | 35.1 → 🔴 ** 27.6** (`-7.5`) | `-7.5 pkt` | 5.61 Er | 0.8% | 5.0% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Autodafé Inkwizytora: Cooldown 2 Ery (Częsta czystka)** | 35.1 → 🔴 ** 26.0** (`-9.1`) | `-9.1 pkt` | 5.71 Er | 0.8% | 5.7% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Autodafé Inkwizytora: Cooldown 4 Ery (Rzadka czystka)** | 35.1 → 🔴 ** 29.9** (`-5.2`) | `-5.2 pkt` | 6.18 Er | 1.7% | 5.3% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Autodafé Inkwizytora: Całkowity brak czystki** | 35.1 → 🔴 ** 19.3** (`-15.8`) | `-15.8 pkt` | 6.46 Er | 2.9% | 4.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)

| Badany Warunek Zwycięstwa L2 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: Wymóg Stosów +2** | 35.1 → 🔴 ** 30.5** (`-4.6`) | `-4.6 pkt` | 6.21 Er | 2.6% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: Wymóg Stosów -1** | 35.1 → 🔴 ** 23.7** (`-11.4`) | `-11.4 pkt` | 5.71 Er | 0.5% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: Wymóg Skazań +2 (Zamiast 2-3)** | 35.1 → 🔴 ** 35.2** (`⬆️ +0.1`) | `+0.1 pkt` | 5.97 Er | 1.0% | 5.6% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Święte Oficjum: Wymóg Skazań -1** | 35.1 → 🟠 ** 65.2** (`⬆️ +30.1`) | `+30.1 pkt` | 5.81 Er | 0.8% | 5.6% | ⚠️ KRYTYCZNA WADA (Critical Flaw) |
| **Cienie: Wymóg Relikwii 2 → 4** | 35.1 → 🔴 ** 12.5** (`-22.6`) | `-22.6 pkt` | 6.47 Er | 1.4% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Cienie: Wymóg Relikwii 2 → 1** | 35.1 → 🔴 **  8.4** (`-26.7`) | `-26.7 pkt` | 4.97 Er | 0.2% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: Wymóg Dekretów 2 → 3** | 35.1 → 🔴 ** 12.3** (`-22.8`) | `-22.8 pkt` | 6.45 Er | 2.4% | 5.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: Wymóg Dekretów 2 → 1** | 35.1 → 🔴 **  5.7** (`-29.4`) | `-29.4 pkt` | 3.09 Er | 0.1% | 4.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: Wymóg Haków +2** | 35.1 → 🔴 ** 30.4** (`-4.7`) | `-4.7 pkt` | 6.20 Er | 1.2% | 5.7% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Kabała: Wymóg Fragmentów 3 → 4** | 35.1 → 🔴 ** 22.4** (`-12.7`) | `-12.7 pkt` | 6.20 Er | 1.7% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: Wymóg Fragmentów 3 → 2** | 35.1 → 🔴 ** 21.0** (`-14.1`) | `-14.1 pkt` | 5.67 Er | 0.8% | 5.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: Wymóg Ery 6 → Era 4** | 35.1 → 🔴 ** 32.8** (`-2.3`) | `-2.3 pkt` | 5.82 Er | 1.0% | 5.5% | ⚖️ ZBALANSOWANY REGULATOR (Balanced Regulator) |
| **Kabała: Wymóg Ery 6 → Era 8** | 35.1 → 🔴 ** 29.5** (`-5.6`) | `-5.6 pkt` | 6.14 Er | 1.0% | 5.6% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Kabała: Próg Górny Pasma 9 → 7 (Zawężenie od góry)** | 35.1 → 🔴 ** 33.7** (`-1.4`) | `-1.4 pkt` | 6.02 Er | 1.1% | 5.6% | 💤 MARTWA MECHANIKA (Low Impact) |
| **Kabała: Próg Górny Pasma 9 → 11 (Rozszerzenie w górę)** | 35.1 → 🔴 ** 34.0** (`-1.1`) | `-1.1 pkt` | 5.91 Er | 0.6% | 5.6% | 💤 MARTWA MECHANIKA (Low Impact) |
| **Kabała: Całe Pasmo Wąskie (4–6)** | 35.1 → 🔴 ** 29.0** (`-6.1`) | `-6.1 pkt` | 6.10 Er | 1.4% | 5.6% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Gildia: Wymóg Upadków (z Oficjum) 2 → 3** | 35.1 → 🔴 ** 26.3** (`-8.8`) | `-8.8 pkt` | 6.20 Er | 1.1% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: Wymóg Upadków (z Oficjum) 2 → 1** | 35.1 → 🔴 ** 23.8** (`-11.3`) | `-11.3 pkt` | 5.52 Er | 0.6% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: Wymóg Upadków (bez Oficjum) 3 → 4** | 35.1 → 🔴 ** 31.6** (`-3.5`) | `-3.5 pkt` | 6.02 Er | 1.1% | 5.6% | 💤 MARTWA MECHANIKA (Low Impact) |
| **Gildia: Wymóg Upadków (bez Oficjum) 3 → 2** | 35.1 → 🔴 ** 33.7** (`-1.4`) | `-1.4 pkt` | 5.90 Er | 0.9% | 5.6% | 💤 MARTWA MECHANIKA (Low Impact) |

### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)

| Badany Wariant / Modyfikator L4 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kronika Dziejów: Całkowite wyłączenie edyktów czasu** | 35.1 → 🔴 ** 19.2** (`-15.9`) | `-15.9 pkt` | 6.39 Er | 2.8% | 6.2% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kronika Dziejów: Częstotliwość co 2 Ery** | 35.1 → 🔴 ** 25.5** (`-9.6`) | `-9.6 pkt` | 6.25 Er | 2.1% | 5.9% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Werdykt Sądu: Tajny (brak koordynacji anty-snowball)** | 35.1 → 🔴 ** 24.4** (`-10.7`) | `-10.7 pkt` | 5.50 Er | 0.4% | 5.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Szlak Morski: Odblokowanie w Erze 6 (Późne)** | 🔴 ** 35.1** | `0.0 pkt` | 5.96 Er | 1.0% | 5.6% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Inkwizytor Patrol: Ruch 0 pól (Stacjonarny)** | 35.1 → 🔴 ** 27.1** (`-8.0`) | `-8.0 pkt` | 6.01 Er | 1.0% | 5.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Inkwizytor Patrol: Ruch 2 pola (Szybki patrol)** | 35.1 → 🔴 ** 36.3** (`⬆️ +1.2`) | `+1.2 pkt` | 5.93 Er | 0.8% | 5.6% | 💤 MARTWA MECHANIKA (Low Impact) |

---

## 5. 👥 Warstwa IV — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych w Kanonie 4P:

| Nieobecna Frakcja | Setup Testowy | 4P Score Setupu | Diagnoza Wpływu Braku Frakcji na Stół 4P |
| :--- | :--- | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`26.7 pkt`** | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`27.9 pkt`** | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`26.4 pkt`** | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`26.4 pkt`** | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`68.0 pkt`** | Brak presji stosów i bezpośredniego Inkwizytora |