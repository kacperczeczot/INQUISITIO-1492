[Strona główna](../../../../../README.md) > [v0.90](README.md) > [raport_uzytecznosci_i_wplywu_4p](raport_uzytecznosci_i_wplywu_4p.md)

---

# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v0.90

**Wersja Gry:** `v0.90` | **Data Badania:** 2026-08-17 13:23 | **Próba:** 400 gier/setup (2000 gier na wariant) | **Ziarno:** 42
**Wynik Bazowy Kanonu 4P:** 🔴 ** 27.6** pkt | **Średnia Długość Partii:** `5.59 Er` | **Deadlocki:** `0.5%` | **Pas Biedy:** `5.6%`

**Tryb:** `--no-cards` — raport bez ablacji kart frakcji i kroniki (tylko L1/L2/L4 i stoły 4P).

---


---

## 4. ⚙️ Warstwa III — Matryca 9 Obszarów Wpływu Mechanik Gry (L1, L2, L4)

Zestawienie odporności Kanonu 4P na modyfikacje i ablację poszczególnych podsystemów. **Δ≈0 nie jest harmonią** — to klauzula, której gracze nie czują.

| Kategoria Mechaniki | Liczba Testów | Rola w Ekosystemie Kanonu 4P | Rekomendacja Balansowa |
| :--- | :---: | :--- | :--- |
| 👑 / 🛡️ **Filary i Bezpieczniki Stabilizujące** | **25** | Mechaniki krytyczne — ich brak lub rozregulowanie niszczy balans | **Nienaruszalny Kanon** |
| ⚖️ **Zbalansowane Regulatory** | **2** | Mechaniki, które ruszają share, ale nie walą w 4P Score | **Optymalne w Kanonie** |
| 💤 **Martwe Mechaniki (Δ≈0)** | **18** | Ablacja nic albo prawie nic nie zmienia — klauzula nie gra | **Ożywić albo wyciąć** |
| ⚠️ / 💡 **Obciążenia i Kandydaci do Uproszczenia** | **3** | Mechaniki, których modyfikacja lub redukcja podnosi wynik 4P | **Kandydaci do optymalizacji** |

### 4.0. 💤 Martwe mechaniki (osobny wykaz)
Testy z $|\Delta\text{4P}| \le 0.8$ i ruchem share $\le 1.5$ pp. To nie jest „optymalny kanon”.

| Badany Podsystem | Kategoria | 4P Score | $\Delta$ 4P | Klasyfikacja |
| :--- | :--- | :---: | :---: | :--- |
| **Święte Oficjum: Wymóg Skazań +2 (Zamiast 2-3)** | Poziom 2: Warunki Zwycięstwa | 🔴 ** 27.6** | `0.0 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Limit Er: 12 → 16 Er (Wydłużony silnik)** | Poziom 1: System Core | 27.6 → 🔴 ** 28.0** (`⬆️ +0.4`) | `+0.4 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Próg Oskarżenia na Dworze: +1 (Pasywny Dwór)** | Poziom 1: System Core | 27.6 → 🔴 ** 28.1** (`⬆️ +0.5`) | `+0.5 pkt` | 💤 MARTWA MECHANIKA (Low Impact) |
| **Szlak Morski: Odblokowanie w Erze 6 (Późne)** | Poziom 4: Warianty i Modyfikatory | 27.6 → 🔴 ** 28.1** (`⬆️ +0.5`) | `+0.5 pkt` | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Gildia: Wymóg Upadków (bez Oficjum) 3 → 4** | Poziom 2: Warunki Zwycięstwa | 27.6 → 🔴 ** 26.6** (`-1.0`) | `-1.0 pkt` | 💤 MARTWA MECHANIKA (Low Impact) |
| **Kabała: Próg Górny Pasma 9 → 11 (Rozszerzenie w górę)** | Poziom 2: Warunki Zwycięstwa | 27.6 → 🔴 ** 28.9** (`⬆️ +1.3`) | `+1.3 pkt` | 💤 MARTWA MECHANIKA (Low Impact) |
| **Próg Oskarżenia na Dworze: -1 (Agresywny Dwór)** | Poziom 1: System Core | 27.6 → 🔴 ** 25.7** (`-1.9`) | `-1.9 pkt` | 💤 MARTWA MECHANIKA (Low Impact) |
| **Inkwizytor Patrol: Ruch 2 pola (Szybki patrol)** | Poziom 4: Warianty i Modyfikatory | 27.6 → 🔴 ** 24.7** (`-2.9`) | `-2.9 pkt` | 💤 MARTWA MECHANIKA (Low Impact) |
| **Kabała: Próg Górny Pasma 9 → 7 (Zawężenie od góry)** | Poziom 2: Warunki Zwycięstwa | 27.6 → 🔴 ** 24.3** (`-3.3`) | `-3.3 pkt` | 💤 MARTWA MECHANIKA (Low Impact) |

### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)

| Badany Podsystem / Modyfikator L1 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Limit Er: 12 → 8 Er (Presja czasu)** | 27.6 → 🔴 **  6.9** (`-20.7`) | `-20.7 pkt` | 5.46 Er | 17.8% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit Er: 12 → 16 Er (Wydłużony silnik)** | 27.6 → 🔴 ** 28.0** (`⬆️ +0.4`) | `+0.4 pkt` | 5.60 Er | 0.0% | 5.6% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Próg Oskarżenia na Dworze: -1 (Agresywny Dwór)** | 27.6 → 🔴 ** 25.7** (`-1.9`) | `-1.9 pkt` | 5.70 Er | 0.8% | 4.9% | 💤 MARTWA MECHANIKA (Low Impact) |
| **Próg Oskarżenia na Dworze: +1 (Pasywny Dwór)** | 27.6 → 🔴 ** 28.1** (`⬆️ +0.5`) | `+0.5 pkt` | 5.43 Er | 0.4% | 6.0% | 💤 MARTWA MECHANIKA (Low Impact) |
| **Złoto startowe: 4zł → 0zł (Skrajne ubóstwo)** | 27.6 → 🔴 **  9.0** (`-18.6`) | `-18.6 pkt` | 6.39 Er | 1.6% | 19.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 6zł (Bogaty start)** | 27.6 → 🔴 ** 13.7** (`-13.9`) | `-13.9 pkt` | 5.01 Er | 0.1% | 3.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 2 Agentów (Ograniczony zasięg)** | 27.6 → 🔴 ** 30.5** (`⬆️ +2.9`) | `+2.9 pkt` | 5.71 Er | 0.7% | 5.8% | 💡 KANDYDAT DO UPROSZCZENIA (Simplification) |
| **Liczba Agentów: 3 → 4 Agentów (Gęsta plansza)** | 27.6 → 🔴 ** 20.1** (`-7.5`) | `-7.5 pkt` | 5.32 Er | 0.5% | 5.6% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Limit kart na ręce: 5 → 3 karty (Zmniejszona elastyczność)** | 27.6 → 🔴 ** 24.2** (`-3.4`) | `-3.4 pkt` | 6.08 Er | 0.4% | 10.0% | ⚖️ ZBALANSOWANY REGULATOR (Balanced Regulator) |
| **Limit kart na ręce: 5 → 7 kart (Pełna swoboda)** | 27.6 → 🔴 ** 20.8** (`-6.8`) | `-6.8 pkt` | 5.21 Er | 0.1% | 4.9% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Autodafé Inkwizytora: Cooldown 2 Ery (Częsta czystka)** | 27.6 → 🔴 ** 13.5** (`-14.1`) | `-14.1 pkt` | 5.15 Er | 0.2% | 5.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé Inkwizytora: Cooldown 4 Ery (Rzadka czystka)** | 27.6 → 🔴 ** 33.8** (`⬆️ +6.2`) | `+6.2 pkt` | 5.87 Er | 0.8% | 5.4% | ⚠️ UMIARKOWANE OBCIĄŻENIE (Moderate Drag) |
| **Autodafé Inkwizytora: Całkowity brak czystki** | 27.6 → 🔴 ** 25.7** (`-1.9`) | `-1.9 pkt` | 6.44 Er | 2.7% | 4.8% | ⚓ KLUCZOWY STABILIZATOR (Key Anchor) |

### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)

| Badany Warunek Zwycięstwa L2 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: Wymóg Stosów +2** | 27.6 → 🔴 ** 25.0** (`-2.6`) | `-2.6 pkt` | 5.88 Er | 1.4% | 5.5% | ⚓ KLUCZOWY STABILIZATOR (Key Anchor) |
| **Święte Oficjum: Wymóg Stosów -1** | 27.6 → 🔴 ** 21.8** (`-5.8`) | `-5.8 pkt` | 5.29 Er | 0.4% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: Wymóg Skazań +2 (Zamiast 2-3)** | 🔴 ** 27.6** | `0.0 pkt` | 5.59 Er | 0.5% | 5.6% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Święte Oficjum: Wymóg Skazań -1** | 27.6 → 🔴 ** 48.2** (`⬆️ +20.6`) | `+20.6 pkt` | 5.48 Er | 0.5% | 5.6% | ⚠️ KRYTYCZNA WADA (Critical Flaw) |
| **Cienie: Wymóg Relikwii 2 → 4** | 27.6 → 🔴 **  8.9** (`-18.7`) | `-18.7 pkt` | 6.04 Er | 1.0% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Cienie: Wymóg Relikwii 2 → 1** | 27.6 → 🔴 **  6.5** (`-21.1`) | `-21.1 pkt` | 4.65 Er | 0.1% | 5.4% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: Wymóg Dekretów 2 → 3** | 27.6 → 🔴 **  9.3** (`-18.3`) | `-18.3 pkt` | 5.93 Er | 1.1% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: Wymóg Dekretów 2 → 1** | 27.6 → 🔴 **  3.1** (`-24.5`) | `-24.5 pkt` | 2.93 Er | 0.1% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: Wymóg Haków +2** | 27.6 → 🔴 ** 20.1** (`-7.5`) | `-7.5 pkt` | 5.78 Er | 0.6% | 5.6% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Kabała: Wymóg Fragmentów 3 → 4** | 27.6 → 🔴 ** 16.2** (`-11.4`) | `-11.4 pkt` | 5.76 Er | 0.9% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: Wymóg Fragmentów 3 → 2** | 27.6 → 🔴 ** 24.9** (`-2.7`) | `-2.7 pkt` | 5.40 Er | 0.4% | 5.6% | ⚓ KLUCZOWY STABILIZATOR (Key Anchor) |
| **Kabała: Wymóg Ery 6 → Era 4** | 27.6 → 🔴 ** 27.9** (`⬆️ +0.3`) | `+0.3 pkt` | 5.44 Er | 0.5% | 5.5% | ⚖️ ZBALANSOWANY REGULATOR (Balanced Regulator) |
| **Kabała: Wymóg Ery 6 → Era 8** | 27.6 → 🔴 ** 19.4** (`-8.2`) | `-8.2 pkt` | 5.74 Er | 0.6% | 5.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Kabała: Próg Górny Pasma 9 → 7 (Zawężenie od góry)** | 27.6 → 🔴 ** 24.3** (`-3.3`) | `-3.3 pkt` | 5.64 Er | 0.9% | 5.5% | 💤 MARTWA MECHANIKA (Low Impact) |
| **Kabała: Próg Górny Pasma 9 → 11 (Rozszerzenie w górę)** | 27.6 → 🔴 ** 28.9** (`⬆️ +1.3`) | `+1.3 pkt` | 5.55 Er | 0.2% | 5.6% | 💤 MARTWA MECHANIKA (Low Impact) |
| **Kabała: Całe Pasmo Wąskie (4–6)** | 27.6 → 🔴 ** 19.2** (`-8.4`) | `-8.4 pkt` | 5.71 Er | 1.0% | 5.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Gildia: Wymóg Upadków (z Oficjum) 2 → 3** | 27.6 → 🔴 ** 25.7** (`-1.9`) | `-1.9 pkt` | 5.89 Er | 0.7% | 5.6% | ⚓ KLUCZOWY STABILIZATOR (Key Anchor) |
| **Gildia: Wymóg Upadków (z Oficjum) 2 → 1** | 27.6 → 🔴 ** 21.7** (`-5.9`) | `-5.9 pkt` | 5.10 Er | 0.4% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: Wymóg Upadków (bez Oficjum) 3 → 4** | 27.6 → 🔴 ** 26.6** (`-1.0`) | `-1.0 pkt` | 5.65 Er | 0.7% | 5.6% | 💤 MARTWA MECHANIKA (Low Impact) |
| **Gildia: Wymóg Upadków (bez Oficjum) 3 → 2** | 27.6 → 🔴 ** 20.2** (`-7.4`) | `-7.4 pkt` | 5.51 Er | 0.4% | 5.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |

### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)

| Badany Wariant / Modyfikator L4 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kronika Dziejów: Całkowite wyłączenie edyktów czasu** | 27.6 → 🔴 ** 12.2** (`-15.4`) | `-15.4 pkt` | 5.70 Er | 0.9% | 6.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kronika Dziejów: Częstotliwość co 2 Ery** | 27.6 → 🔴 ** 18.5** (`-9.1`) | `-9.1 pkt` | 5.75 Er | 1.2% | 5.8% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Werdykt Sądu: Tajny (brak koordynacji anty-snowball)** | 27.6 → 🔴 ** 24.1** (`-3.5`) | `-3.5 pkt` | 5.13 Er | 0.3% | 5.7% | ⚓ KLUCZOWY STABILIZATOR (Key Anchor) |
| **Szlak Morski: Odblokowanie w Erze 6 (Późne)** | 27.6 → 🔴 ** 28.1** (`⬆️ +0.5`) | `+0.5 pkt` | 5.58 Er | 0.5% | 5.6% | 💤 MARTWA MECHANIKA (Δ≈0 — klauzula nie gra) |
| **Inkwizytor Patrol: Ruch 0 pól (Stacjonarny)** | 27.6 → 🔴 ** 27.5** (`-0.1`) | `-0.1 pkt` | 6.00 Er | 1.0% | 5.5% | ⚓ KLUCZOWY STABILIZATOR (Key Anchor) |
| **Inkwizytor Patrol: Ruch 2 pola (Szybki patrol)** | 27.6 → 🔴 ** 24.7** (`-2.9`) | `-2.9 pkt` | 5.43 Er | 0.4% | 5.6% | 💤 MARTWA MECHANIKA (Low Impact) |

---

## 5. 👥 Warstwa IV — Odporność Stołu 4P na Nieobecność Konkretnej Frakcji

Zestawienie stabilności 5 wariantów 4-osobowych w Kanonie 4P:

| Nieobecna Frakcja | Setup Testowy | 4P Score Setupu | Diagnoza Wpływu Braku Frakcji na Stół 4P |
| :--- | :--- | :---: | :--- |
| **Bez Gildii Cieni** | `4p-core` | **`14.3 pkt`** | Stół klasyczny (czysta walka religijno-polityczna) |
| **Bez Kabały z Toledo** | `4p-no-kabala` | **`14.9 pkt`** | Brak presji okultystycznej i manipulacji czasem |
| **Bez Korony i Borgiów** | `4p-no-korona` | **`13.2 pkt`** | Brak presji podatkowej i aresztów królewskich |
| **Bez Cieni Al-Andalus** | `4p-no-cienie` | **`11.8 pkt`** | Brak szlaków morskich i ucieczek podziemiami |
| **Bez Świętego Oficjum** | `4p-no-oficjum` | **`83.9 pkt`** | Brak presji stosów i bezpośredniego Inkwizytora |