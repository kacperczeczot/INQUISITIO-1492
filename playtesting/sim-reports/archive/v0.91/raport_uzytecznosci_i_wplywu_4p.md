# Raport Użyteczności i Wpływu Elementów w Kanonie 4P (Ablation & Impact Audit 4P) — Wersja v0.91

**Wersja Gry:** `v0.91` | **Data Badania:** 2026-08-17 13:45 | **Próba:** 5000 gier/setup (25000 gier na wariant) | **Ziarno:** 42
**4P Score (win share):** 🟡 ** 86.6** pkt | **Witalność (osobna kara):** `1.200` | **Śr. Er:** `5.96` | **Deadlocki:** `1.1%` | **Pas Biedy:** `5.5%`
**Udziały 4P:** CAA 21.3% · GC 25.4% · KB 26.5% · KT 25.8% · SO 25.9%

Klasyfikacja L1/L2/L4 i Δ 4P liczą **wyłącznie równość win share** (`calculate_balance_score`). Kara witalności nie wchodzi do tej liczby — inaczej martwa ścieżka Oficjum zaniża kanon z ~90 pkt do ~35 i etykietuje leczenie skazań jako „wadę”.

**Tryb:** `--no-cards` — raport bez ablacji kart frakcji i kroniki (tylko L1/L2/L4 i stoły 4P).

**Ostrzeżenia witalności (nie w 4P Score):**
- 4p-core: Martwa ścieżka skazania (swiete-oficjum): 19/1264 wygranych (<8%) — gra tylko stosy
- 4p-no-cienie: Martwa ścieżka skazania (swiete-oficjum): 35/1237 wygranych (<8%) — gra tylko stosy
- 4p-no-kabala: Martwa ścieżka skazania (swiete-oficjum): 39/1316 wygranych (<8%) — gra tylko stosy
- 4p-no-korona: Martwa ścieżka skazania (swiete-oficjum): 39/1291 wygranych (<8%) — gra tylko stosy

---


---

## 4. ⚙️ Warstwa III — Matryca 9 Obszarów Wpływu Mechanik Gry (L1, L2, L4)

Docelowo **każda kluczowa gałka L1/L2/L4** ląduje w filarach. Inne kubełki to dług, nie złoty środek. **Δ≈0 nie jest harmonią.**

| Kategoria Mechaniki | Liczba Testów | Rola w Ekosystemie Kanonu 4P | Rekomendacja Balansowa |
| :--- | :---: | :--- | :--- |
| 👑 / 🛡️ **Filary i Bezpieczniki** | **34** | Ablacja wali w stół — gracze czują tę gałkę | **Cel kanonu** |
| ⚠️ **Za słabe dźwignie** | **0** | Rusza share, nie trzyma stołu — nie jest „zbalansowana” | **Wzmocnić aż będzie filarem** |
| 💤 **Martwe / nietestowalne bezpieczniki** | **0** | Δ≈0: klauzula nie gra albo poluzowaliśmy bezpiecznik, który i tak nie strzela | **Ożywić, wyciąć, albo nie testować jako mechaniki** |
| ⚠️ / 💡 **Wady bieżącej wartości** | **0** | Inna wartość gałki **podnosi** 4P — obecny setting szkodzi | **Przekręcić albo rework** |

### 4.0. 💤 Martwe mechaniki (osobny wykaz)
Bezpieczników (limit Er 16, szlak 6, patrol 2) i zaostrzenia uśpionej ścieżki (skazania +2) **nie testujemy**. Jedyny żywy dług: **skazania Oficjum przy progu 3** — ostrzeżenia witalności na górze. Nie obniżamy do 2 bez rekompensaty.

| Badany Podsystem | Kategoria | 4P Score | $\Delta$ 4P | Klasyfikacja |
| :--- | :--- | :---: | :---: | :--- |
| *Lista pusta — kontrfakty wycięte z audytu* | - | - | - | - |

### 4.1. ⚙️ Poziom 1: Główne Mechaniki Systemowe (Global System Core)

| Badany Podsystem / Modyfikator L1 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Limit Er: 12 → 8 Er (Presja czasu)** | 86.6 → 🟠 ** 71.8** (`-14.8`) | `-14.8 pkt` | 5.73 Er | 23.6% | 5.6% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Próg Oskarżenia na Dworze: -1 (Agresywny Dwór)** | 86.6 → 🟠 ** 73.3** (`-13.3`) | `-13.3 pkt` | 6.08 Er | 1.6% | 4.9% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Próg Oskarżenia na Dworze: +1 (Pasywny Dwór)** | 86.6 → 🟡 ** 80.9** (`-5.7`) | `-5.7 pkt` | 5.85 Er | 0.7% | 6.1% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Złoto startowe: 4zł → 0zł (Skrajne ubóstwo)** | 86.6 → 🔴 ** 39.3** (`-47.3`) | `-47.3 pkt` | 6.96 Er | 4.1% | 18.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Złoto startowe: 4zł → 6zł (Bogaty start)** | 86.6 → 🔴 ** 33.9** (`-52.7`) | `-52.7 pkt` | 5.21 Er | 0.5% | 3.3% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Liczba Agentów: 3 → 2 Agentów (Ograniczony zasięg)** | 86.6 → 🟡 ** 78.5** (`-8.1`) | `-8.1 pkt` | 6.16 Er | 2.1% | 5.7% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Liczba Agentów: 3 → 4 Agentów (Gęsta plansza)** | 86.6 → 🟠 ** 70.2** (`-16.4`) | `-16.4 pkt` | 5.83 Er | 0.7% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 3 karty (Zmniejszona elastyczność)** | 86.6 → 🔴 ** 58.5** (`-28.1`) | `-28.1 pkt` | 6.52 Er | 1.9% | 10.0% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Limit kart na ręce: 5 → 7 kart (Pełna swoboda)** | 86.6 → 🔴 ** 58.9** (`-27.7`) | `-27.7 pkt` | 5.62 Er | 0.9% | 5.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé Inkwizytora: Cooldown 2 Ery (Częsta czystka)** | 86.6 → 🔴 ** 57.4** (`-29.2`) | `-29.2 pkt` | 5.69 Er | 0.8% | 5.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Autodafé Inkwizytora: Cooldown 4 Ery (Rzadka czystka)** | 86.6 → 🟠 ** 74.2** (`-12.4`) | `-12.4 pkt` | 6.14 Er | 1.6% | 5.3% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Autodafé Inkwizytora: Całkowity brak czystki** | 86.6 → 🔴 ** 31.8** (`-54.8`) | `-54.8 pkt` | 6.43 Er | 2.8% | 4.8% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

### 4.2. ⚔️ Poziom 2: Asymetryczne Warunki Zwycięstwa (Victory Paths)

| Badany Warunek Zwycięstwa L2 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Święte Oficjum: Wymóg Stosów +2** | 86.6 → 🔴 ** 50.3** (`-36.3`) | `-36.3 pkt` | 6.18 Er | 2.3% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: Wymóg Stosów -1** | 86.6 → 🔴 ** 51.1** (`-35.5`) | `-35.5 pkt` | 5.72 Er | 0.7% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Święte Oficjum: Wymóg Skazań -1** | 86.6 → 🟠 ** 71.7** (`-14.9`) | `-14.9 pkt` | 5.81 Er | 0.9% | 5.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Cienie: Wymóg Relikwii 2 → 4** | 86.6 → 🔴 ** 34.4** (`-52.2`) | `-52.2 pkt` | 6.47 Er | 1.8% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Cienie: Wymóg Relikwii 2 → 1** | 86.6 → 🔴 ** 24.8** (`-61.8`) | `-61.8 pkt` | 4.92 Er | 0.2% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: Wymóg Dekretów 2 → 3** | 86.6 → 🔴 ** 33.3** (`-53.3`) | `-53.3 pkt` | 6.48 Er | 2.7% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: Wymóg Dekretów 2 → 1** | 86.6 → 🔴 ** 18.4** (`-68.2`) | `-68.2 pkt` | 3.11 Er | 0.2% | 4.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Korona: Wymóg Haków +2** | 86.6 → 🟠 ** 68.4** (`-18.2`) | `-18.2 pkt` | 6.22 Er | 1.4% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: Wymóg Fragmentów 3 → 4** | 86.6 → 🔴 ** 54.0** (`-32.6`) | `-32.6 pkt` | 6.20 Er | 1.6% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: Wymóg Fragmentów 3 → 2** | 86.6 → 🔴 ** 52.0** (`-34.6`) | `-34.6 pkt` | 5.68 Er | 0.9% | 5.6% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: Wymóg Ery 6 → Era 4** | 86.6 → 🟡 ** 79.2** (`-7.4`) | `-7.4 pkt` | 5.81 Er | 1.1% | 5.4% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Kabała: Wymóg Ery 6 → Era 8** | 86.6 → 🟠 ** 66.0** (`-20.6`) | `-20.6 pkt` | 6.16 Er | 1.1% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kabała: Próg Górny Pasma 9 → 7 (Zawężenie od góry)** | 86.6 → 🟡 ** 81.0** (`-5.6`) | `-5.6 pkt` | 6.02 Er | 1.3% | 5.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Kabała: Próg Górny Pasma 9 → 11 (Rozszerzenie w górę)** | 86.6 → 🟡 ** 80.9** (`-5.7`) | `-5.7 pkt` | 5.92 Er | 0.6% | 5.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Kabała: Całe Pasmo Wąskie (4–6)** | 86.6 → 🟠 ** 69.4** (`-17.2`) | `-17.2 pkt` | 6.09 Er | 1.5% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: Wymóg Upadków (z Oficjum) 3 → 4** | 86.6 → 🔴 ** 59.0** (`-27.6`) | `-27.6 pkt` | 6.20 Er | 1.3% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: Wymóg Upadków (z Oficjum) 3 → 2** | 86.6 → 🔴 ** 49.0** (`-37.6`) | `-37.6 pkt` | 5.52 Er | 0.8% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Gildia: Wymóg Upadków (bez Oficjum) 5 → 6** | 86.6 → 🟡 ** 82.4** (`-4.2`) | `-4.2 pkt` | 6.01 Er | 1.3% | 5.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |
| **Gildia: Wymóg Upadków (bez Oficjum) 5 → 4** | 86.6 → 🟡 ** 83.6** (`-3.0`) | `-3.0 pkt` | 5.89 Er | 1.0% | 5.5% | 🛡️ ISTOTNY BEZPIECZNIK (Important Safeguard) |

### 4.3. 🎲 Poziom 4: Warianty Niszowe & Modyfikatory Globalne (Level 4)

| Badany Wariant / Modyfikator L4 | 4P Score | $\Delta$ 4P | Śr. Er | Deadlock % | Pas Biedy % | Klasyfikacja w Matrycy 3x3 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kronika Dziejów: Całkowite wyłączenie edyktów czasu** | 86.6 → 🔴 ** 44.2** (`-42.4`) | `-42.4 pkt` | 6.36 Er | 2.4% | 6.1% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Kronika Dziejów: Częstotliwość co 2 Ery** | 86.6 → 🟠 ** 63.6** (`-23.0`) | `-23.0 pkt` | 6.23 Er | 2.0% | 5.9% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Werdykt Sądu: Tajny (brak koordynacji anty-snowball)** | 86.6 → 🔴 ** 52.8** (`-33.8`) | `-33.8 pkt` | 5.49 Er | 0.4% | 5.7% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |
| **Inkwizytor Patrol: Ruch 0 pól (Stacjonarny)** | 86.6 → 🟠 ** 68.1** (`-18.5`) | `-18.5 pkt` | 6.03 Er | 1.1% | 5.5% | 👑 KRYTYCZNY FILAR (Core Engine Pillar) |

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