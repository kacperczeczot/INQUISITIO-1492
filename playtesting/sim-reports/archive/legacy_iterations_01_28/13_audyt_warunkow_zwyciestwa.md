# Raport Audytu Wariacji Warunków Zwycięstwa Frakcji (3p, 4p, 5p)

**Przeanalizowano Wariantów:** 20 | **Próba:** 300 gier/setup | **Czas:** 83.1s
**Wynik Bazy (Zaktualizowany Pakiet):** `41.6 / 100.0 pkt`

## 1. Tabela Porównawcza Wpływu Zmian Warunków Zwycięstwa na Balans

| ID | Nazwa Wariantu Warunku Zwycięstwa | Global Score | Różnica vs Baza | 3p Avg | 4p Avg | 5p Avg | Czy Poprawia Wynik? |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BAZA` | Baza (Obecny Zaktualizowany Pakiet Zasad) | ** 41.6** | `0.0` | 15.8 | 59.8 | 49.3 | ⚪ NEUTRALNY |
| `WIN_SO_01` | Oficjum: Stosy 4/5/6 (+1 dla 3p/4p/5p) | ** 41.6** | `0.0` | 15.8 | 59.8 | 49.3 | ⚪ NEUTRALNY |
| `WIN_SO_02` | Oficjum: Stosy 2/3/4 (-1 dla 3p/4p/5p) | ** 28.5** | `-13.1` | 4.3 | 61.6 | 19.7 | 🔴 NIE (Pogarsza) |
| `WIN_SO_03` | Oficjum: Skazania 3/4/5 (+1 dla 3p/4p/5p) | ** 41.6** | `0.0` | 15.8 | 59.8 | 49.3 | ⚪ NEUTRALNY |
| `WIN_SO_04` | Oficjum: Skazania 1/2/3 (-1 dla 3p/4p/5p) | ** 36.7** | `-4.9` | 4.9 | 55.9 | 49.3 | 🔴 NIE (Pogarsza) |
| `WIN_CAA_01` | Cienie: Relikwie = 3 (wszystkie składy) | ** 42.6** | `+1.0` | 18.9 | 59.7 | 49.3 | 🟢 TAK (Poprawia) |
| `WIN_CAA_02` | Cienie: Relikwie = 1 (dla 5p) | ** 37.8** | `-3.8` | 15.8 | 59.8 | 0.0 | 🔴 NIE (Pogarsza) |
| `WIN_CAA_03` | Cienie: Odblokowanie Ścieżki Era -1 (Era 4/5) | ** 41.6** | `0.0` | 15.8 | 59.8 | 49.3 | ⚪ NEUTRALNY |
| `WIN_CAA_04` | Cienie: Odblokowanie Ścieżki Era +1 (Era 6/7) | ** 41.6** | `0.0` | 15.8 | 59.8 | 49.3 | ⚪ NEUTRALNY |
| `WIN_KB_01` | Korona: Wymagane Dekrety = 3 (dla 3p) | ** 41.6** | `0.0` | 15.6 | 59.8 | 49.3 | ⚪ NEUTRALNY |
| `WIN_KB_02` | Korona: Wymagane Haki = 2 (wszystkie składy) | ** 41.5** | `-0.1` | 15.6 | 59.7 | 49.3 | ⚪ NEUTRALNY |
| `WIN_KB_03` | Korona: Era Zwycięstwa -1 (Era 6/5) | ** 36.8** | `-4.8` | 22.1 | 50.9 | 37.3 | 🔴 NIE (Pogarsza) |
| `WIN_KB_04` | Korona: Era Zwycięstwa +1 (Era 8/7) | ** 41.5** | `-0.1` | 15.6 | 59.7 | 49.3 | ⚪ NEUTRALNY |
| `WIN_KT_01` | Kabała: Wymagane Fragmenty = 4 (wszystkie składy) | ** 39.9** | `-1.7` | 15.7 | 58.0 | 46.1 | 🔴 NIE (Pogarsza) |
| `WIN_KT_02` | Kabała: Wymagane Fragmenty = 2 (dla 5p) | ** 46.7** | `+5.1` | 15.8 | 59.8 | 64.5 | 🟢 TAK (Poprawia) |
| `WIN_KT_03` | Kabała: Przesunięcie pasma Herezji: 5–7 (+1) | ** 39.5** | `-2.1` | 17.0 | 52.1 | 49.3 | 🔴 NIE (Pogarsza) |
| `WIN_KT_04` | Kabała: Poszerzenie pasma Herezji: 3–7 (±1) | ** 44.7** | `+3.1` | 17.6 | 54.3 | 62.1 | 🟢 TAK (Poprawia) |
| `WIN_KT_05` | Kabała: Odblokowanie Zwycięstwa Era -1 (Era 6/5/4) | ** 38.6** | `-3.0` | 8.2 | 46.0 | 61.6 | 🔴 NIE (Pogarsza) |
| `WIN_GC_01` | Gildia: Wymagane Upadki 3/4 (+1 dla 3-4p/5p) | ** 41.6** | `0.0` | 15.8 | 59.8 | 49.3 | ⚪ NEUTRALNY |
| `WIN_GC_02` | Gildia: Wymagane Upadki 1/2 (-1 dla 3p/4-5p) | **  8.3** | `-33.3` | 7.6 | 9.0 | 0.0 | 🔴 NIE (Pogarsza) |

## 2. Podsumowanie Wniosków dla Projektanta GDD

### WIN_SO_01: Oficjum: Stosy 4/5/6 (+1 dla 3p/4p/5p)
- **Wpływ na Score:** `41.6 pkt` (Różnica vs Baza: `+0.0 pkt`) = **POGORSZENIE BALANSU**

### WIN_SO_02: Oficjum: Stosy 2/3/4 (-1 dla 3p/4p/5p)
- **Wpływ na Score:** `28.5 pkt` (Różnica vs Baza: `-13.1 pkt`) = **POGORSZENIE BALANSU**

### WIN_SO_03: Oficjum: Skazania 3/4/5 (+1 dla 3p/4p/5p)
- **Wpływ na Score:** `41.6 pkt` (Różnica vs Baza: `+0.0 pkt`) = **POGORSZENIE BALANSU**

### WIN_SO_04: Oficjum: Skazania 1/2/3 (-1 dla 3p/4p/5p)
- **Wpływ na Score:** `36.7 pkt` (Różnica vs Baza: `-4.9 pkt`) = **POGORSZENIE BALANSU**

### WIN_CAA_01: Cienie: Relikwie = 3 (wszystkie składy)
- **Wpływ na Score:** `42.6 pkt` (Różnica vs Baza: `+1.0 pkt`) = **POPRAWA BALANSU**

### WIN_CAA_02: Cienie: Relikwie = 1 (dla 5p)
- **Wpływ na Score:** `37.8 pkt` (Różnica vs Baza: `-3.8 pkt`) = **POGORSZENIE BALANSU**

### WIN_CAA_03: Cienie: Odblokowanie Ścieżki Era -1 (Era 4/5)
- **Wpływ na Score:** `41.6 pkt` (Różnica vs Baza: `+0.0 pkt`) = **POGORSZENIE BALANSU**

### WIN_CAA_04: Cienie: Odblokowanie Ścieżki Era +1 (Era 6/7)
- **Wpływ na Score:** `41.6 pkt` (Różnica vs Baza: `+0.0 pkt`) = **POGORSZENIE BALANSU**

### WIN_KB_01: Korona: Wymagane Dekrety = 3 (dla 3p)
- **Wpływ na Score:** `41.6 pkt` (Różnica vs Baza: `+0.0 pkt`) = **POGORSZENIE BALANSU**

### WIN_KB_02: Korona: Wymagane Haki = 2 (wszystkie składy)
- **Wpływ na Score:** `41.5 pkt` (Różnica vs Baza: `-0.1 pkt`) = **POGORSZENIE BALANSU**

### WIN_KB_03: Korona: Era Zwycięstwa -1 (Era 6/5)
- **Wpływ na Score:** `36.8 pkt` (Różnica vs Baza: `-4.8 pkt`) = **POGORSZENIE BALANSU**

### WIN_KB_04: Korona: Era Zwycięstwa +1 (Era 8/7)
- **Wpływ na Score:** `41.5 pkt` (Różnica vs Baza: `-0.1 pkt`) = **POGORSZENIE BALANSU**

### WIN_KT_01: Kabała: Wymagane Fragmenty = 4 (wszystkie składy)
- **Wpływ na Score:** `39.9 pkt` (Różnica vs Baza: `-1.7 pkt`) = **POGORSZENIE BALANSU**

### WIN_KT_02: Kabała: Wymagane Fragmenty = 2 (dla 5p)
- **Wpływ na Score:** `46.7 pkt` (Różnica vs Baza: `+5.1 pkt`) = **POPRAWA BALANSU**

### WIN_KT_03: Kabała: Przesunięcie pasma Herezji: 5–7 (+1)
- **Wpływ na Score:** `39.5 pkt` (Różnica vs Baza: `-2.1 pkt`) = **POGORSZENIE BALANSU**

### WIN_KT_04: Kabała: Poszerzenie pasma Herezji: 3–7 (±1)
- **Wpływ na Score:** `44.7 pkt` (Różnica vs Baza: `+3.1 pkt`) = **POPRAWA BALANSU**

### WIN_KT_05: Kabała: Odblokowanie Zwycięstwa Era -1 (Era 6/5/4)
- **Wpływ na Score:** `38.6 pkt` (Różnica vs Baza: `-3.0 pkt`) = **POGORSZENIE BALANSU**

### WIN_GC_01: Gildia: Wymagane Upadki 3/4 (+1 dla 3-4p/5p)
- **Wpływ na Score:** `41.6 pkt` (Różnica vs Baza: `+0.0 pkt`) = **POGORSZENIE BALANSU**

### WIN_GC_02: Gildia: Wymagane Upadki 1/2 (-1 dla 3p/4-5p)
- **Wpływ na Score:** `8.3 pkt` (Różnica vs Baza: `-33.3 pkt`) = **POGORSZENIE BALANSU**
