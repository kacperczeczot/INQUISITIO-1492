# Raport 22: Audyt +-1 dla Poziomu 2 (Warunki Zwycięstwa i Skalowanie)

**Przeanalizowano Wariantów:** 17 | **Próba:** 300 gier/setup | **Czas:** 70.9s
**Wynik Bazy Poziomu 2:** `50.2 / 100.0 pkt`

## 1. Tabela Porównawcza Wpływu Wariacji +-1 Poziomu 2 na Balans Gry

| ID | Warunek Zwycięstwa Poziomu 2 | Global Score | Różnica vs Baza | 3p Avg | 4p Avg | 5p Avg | Czy Poprawia Wynik? |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Level 2 Baza (Zaktualizowane Warunki Zwycięstwa per Liczba Graczy) | ** 50.2** | `0.0` | 41.1 | 59.4 | 0.0 | ⚪ OPTYMALNY |
| `L2_SO_STACKS_PLUS1` | 1. Oficjum Stosy: +1 (4@3p / 4@4p / 6@5p) | ** 50.2** | `0.0` | 41.1 | 59.4 | 0.0 | ⚪ OPTYMALNY |
| `L2_SO_STACKS_MINUS1` | 1. Oficjum Stosy: -1 (2@3p / 2@4p / 4@5p) | ** 33.2** | `-17.0` | 47.1 | 19.3 | 0.0 | 🔴 NIE (Pogarsza) |
| `L2_SO_CONDEMNS_PLUS1` | 2. Oficjum Skazania: +1 (3@3p / 4@4p / 5@5p) | ** 50.2** | `0.0` | 41.1 | 59.4 | 0.0 | ⚪ OPTYMALNY |
| `L2_SO_CONDEMNS_MINUS1` | 2. Oficjum Skazania: -1 (1@3p / 2@4p / 3@5p) | ** 37.6** | `-12.6` | 28.1 | 47.1 | 0.0 | 🔴 NIE (Pogarsza) |
| `L2_CAA_RELICS_PLUS1` | 3. Cienie Relikwie: 3 (+1) | ** 44.2** | `-6.0` | 41.0 | 47.5 | 0.0 | 🔴 NIE (Pogarsza) |
| `L2_CAA_RELICS_MINUS1` | 3. Cienie Relikwie: 1 (-1) | ** 12.9** | `-37.3` | 12.9 | 0.0 | 0.0 | 🔴 NIE (Pogarsza) |
| `L2_CAA_ERA_PLUS1` | 4. Cienie Era Ścieżki: +1 (Era 7@3p / Era 6@4-5p) | ** 50.2** | `0.0` | 41.1 | 59.4 | 0.0 | ⚪ OPTYMALNY |
| `L2_CAA_ERA_MINUS1` | 4. Cienie Era Ścieżki: -1 (Era 5@3p / Era 4@4-5p) | ** 50.2** | `0.0` | 41.1 | 59.4 | 0.0 | ⚪ OPTYMALNY |
| `L2_KB_ERA_PLUS1` | 5. Korona Era Zwycięstwa: +1 (Era 7@3p / Era 6@4-5p) | ** 50.3** | `+0.1` | 41.1 | 59.5 | 0.0 | ⚪ OPTYMALNY |
| `L2_KB_ERA_MINUS1` | 5. Korona Era Zwycięstwa: -1 (Era 5@3p / Era 4@4-5p) | ** 49.2** | `-1.0` | 40.3 | 58.1 | 0.0 | 🔴 NIE (Pogarsza) |
| `L2_KT_FRAGS_PLUS1` | 6. Kabała Fragmenty: +1 (4@3-4p / 3@5p) | ** 50.7** | `+0.5` | 40.7 | 60.7 | 0.0 | ⚪ OPTYMALNY |
| `L2_KT_FRAGS_MINUS1` | 6. Kabała Fragmenty: -1 (2@3-4p / 1@5p) | ** 41.5** | `-8.7` | 42.6 | 40.5 | 0.0 | 🔴 NIE (Pogarsza) |
| `L2_KT_HERESY_NARROW` | 7. Kabała Pasmo Herezji: Zawężone 4–6 (-1 szerokość) | ** 51.2** | `+1.0` | 40.8 | 61.6 | 0.0 | 🟢 TAK (Poprawia) |
| `L2_KT_HERESY_WIDE` | 7. Kabała Pasmo Herezji: Poszerzone 2–8 (+1 szerokość) | ** 48.6** | `-1.6` | 37.7 | 59.5 | 0.0 | 🔴 NIE (Pogarsza) |
| `L2_GC_FALLS_PLUS1` | 8. Gildia Upadki: +1 (3@3-4p / 4@5p) | ** 50.2** | `0.0` | 41.1 | 59.4 | 0.0 | ⚪ OPTYMALNY |
| `L2_GC_FALLS_MINUS1` | 8. Gildia Upadki: -1 (1@3-4p / 2@5p) | ** 25.6** | `-24.6` | 31.8 | 14.0 | 31.0 | 🔴 NIE (Pogarsza) |

## 2. Wnioski Analityczne dla Poziomu 2

### L2_SO_STACKS_PLUS1: 1. Oficjum Stosy: +1 (4@3p / 4@4p / 6@5p)
- **Wpływ na Score:** `50.2 pkt` (Różnica vs Baza: `+0.0 pkt`) = **OPTYMALNY STABILNY**

### L2_SO_STACKS_MINUS1: 1. Oficjum Stosy: -1 (2@3p / 2@4p / 4@5p)
- **Wpływ na Score:** `33.2 pkt` (Różnica vs Baza: `-17.0 pkt`) = **POGORSZENIE BALANSU**

### L2_SO_CONDEMNS_PLUS1: 2. Oficjum Skazania: +1 (3@3p / 4@4p / 5@5p)
- **Wpływ na Score:** `50.2 pkt` (Różnica vs Baza: `+0.0 pkt`) = **OPTYMALNY STABILNY**

### L2_SO_CONDEMNS_MINUS1: 2. Oficjum Skazania: -1 (1@3p / 2@4p / 3@5p)
- **Wpływ na Score:** `37.6 pkt` (Różnica vs Baza: `-12.6 pkt`) = **POGORSZENIE BALANSU**

### L2_CAA_RELICS_PLUS1: 3. Cienie Relikwie: 3 (+1)
- **Wpływ na Score:** `44.2 pkt` (Różnica vs Baza: `-6.0 pkt`) = **POGORSZENIE BALANSU**

### L2_CAA_RELICS_MINUS1: 3. Cienie Relikwie: 1 (-1)
- **Wpływ na Score:** `12.9 pkt` (Różnica vs Baza: `-37.3 pkt`) = **POGORSZENIE BALANSU**

### L2_CAA_ERA_PLUS1: 4. Cienie Era Ścieżki: +1 (Era 7@3p / Era 6@4-5p)
- **Wpływ na Score:** `50.2 pkt` (Różnica vs Baza: `+0.0 pkt`) = **OPTYMALNY STABILNY**

### L2_CAA_ERA_MINUS1: 4. Cienie Era Ścieżki: -1 (Era 5@3p / Era 4@4-5p)
- **Wpływ na Score:** `50.2 pkt` (Różnica vs Baza: `+0.0 pkt`) = **OPTYMALNY STABILNY**

### L2_KB_ERA_PLUS1: 5. Korona Era Zwycięstwa: +1 (Era 7@3p / Era 6@4-5p)
- **Wpływ na Score:** `50.3 pkt` (Różnica vs Baza: `+0.1 pkt`) = **POPRAWA BALANSU**

### L2_KB_ERA_MINUS1: 5. Korona Era Zwycięstwa: -1 (Era 5@3p / Era 4@4-5p)
- **Wpływ na Score:** `49.2 pkt` (Różnica vs Baza: `-1.0 pkt`) = **POGORSZENIE BALANSU**

### L2_KT_FRAGS_PLUS1: 6. Kabała Fragmenty: +1 (4@3-4p / 3@5p)
- **Wpływ na Score:** `50.7 pkt` (Różnica vs Baza: `+0.5 pkt`) = **POPRAWA BALANSU**

### L2_KT_FRAGS_MINUS1: 6. Kabała Fragmenty: -1 (2@3-4p / 1@5p)
- **Wpływ na Score:** `41.5 pkt` (Różnica vs Baza: `-8.7 pkt`) = **POGORSZENIE BALANSU**

### L2_KT_HERESY_NARROW: 7. Kabała Pasmo Herezji: Zawężone 4–6 (-1 szerokość)
- **Wpływ na Score:** `51.2 pkt` (Różnica vs Baza: `+1.0 pkt`) = **POPRAWA BALANSU**

### L2_KT_HERESY_WIDE: 7. Kabała Pasmo Herezji: Poszerzone 2–8 (+1 szerokość)
- **Wpływ na Score:** `48.6 pkt` (Różnica vs Baza: `-1.6 pkt`) = **POGORSZENIE BALANSU**

### L2_GC_FALLS_PLUS1: 8. Gildia Upadki: +1 (3@3-4p / 4@5p)
- **Wpływ na Score:** `50.2 pkt` (Różnica vs Baza: `+0.0 pkt`) = **OPTYMALNY STABILNY**

### L2_GC_FALLS_MINUS1: 8. Gildia Upadki: -1 (1@3-4p / 2@5p)
- **Wpływ na Score:** `25.6 pkt` (Różnica vs Baza: `-24.6 pkt`) = **POGORSZENIE BALANSU**
