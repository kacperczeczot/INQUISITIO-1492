# Raport 21: Audyt +-1 dla Poziomu 1 (Główne Mechaniki Systemowe)

**Przeanalizowano Wariantów:** 13 | **Próba:** 300 gier/setup | **Czas:** 55.24s
**Wynik Bazy Poziomu 1:** `50.2 / 100.0 pkt`

## 1. Tabela Porównawcza Wpływu Wariacji +-1 Poziomu 1 na Balans Gry

| ID | Element Poziomu 1 | Global Score | Różnica vs Baza | 3p Avg | 4p Avg | 5p Avg | Czy Poprawia Wynik? |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Level 1 Baza (Zaktualizowane Ogólne Zasady Systemowe) | ** 50.2** | `0.0` | 41.1 | 59.4 | 0.0 | ⚪ OPTYMALNY |
| `L1_THRESHOLD_PLUS1` | 1. Próg Oskarżenia (Herezja): 9 (+1) | ** 22.9** | `-27.3` | 10.9 | 35.0 | 0.0 | 🔴 NIE (Pogarsza) |
| `L1_THRESHOLD_MINUS1` | 1. Próg Oskarżenia (Herezja): 7 (-1) | ** 37.5** | `-12.7` | 52.9 | 43.2 | 16.4 | 🔴 NIE (Pogarsza) |
| `L1_MAX_ERAS_PLUS1` | 2. Maksymalny limit Er: 9 (+1) | ** 50.2** | `0.0` | 41.1 | 59.4 | 0.0 | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_MINUS1` | 2. Maksymalny limit Er: 7 (-1) | ** 50.2** | `0.0` | 41.1 | 59.4 | 0.0 | ⚪ OPTYMALNY |
| `L1_START_GOLD_PLUS1` | 3. Złoto startowe: 4zł (+1) | ** 50.2** | `0.0` | 41.1 | 59.4 | 0.0 | ⚪ OPTYMALNY |
| `L1_START_GOLD_MINUS1` | 3. Złoto startowe: 2zł (-1) | ** 50.2** | `0.0` | 41.1 | 59.4 | 0.0 | ⚪ OPTYMALNY |
| `L1_AGENTS_PLUS1` | 4. Liczba agentów na gracza: 4 (+1) | ** 50.2** | `0.0` | 41.1 | 59.4 | 0.0 | ⚪ OPTYMALNY |
| `L1_AGENTS_MINUS1` | 4. Liczba agentów na gracza: 2 (-1) | ** 50.2** | `0.0` | 41.1 | 59.4 | 0.0 | ⚪ OPTYMALNY |
| `L1_HAND_LIMIT_PLUS1` | 5. Limit kart na ręce: 6 (+1) | ** 50.2** | `0.0` | 41.1 | 59.4 | 0.0 | ⚪ OPTYMALNY |
| `L1_HAND_LIMIT_MINUS1` | 5. Limit kart na ręce: 4 (-1) | ** 50.2** | `0.0` | 41.1 | 59.4 | 0.0 | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 6. Cooldown Autodafé: Co 3 Ery (+1) | ** 50.2** | `0.0` | 41.1 | 59.4 | 0.0 | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 6. Cooldown Autodafé: Co 1 Erę (-1) | ** 50.2** | `0.0` | 41.1 | 59.4 | 0.0 | ⚪ OPTYMALNY |

## 2. Wnioski Analityczne dla Poziomu 1

### L1_THRESHOLD_PLUS1: 1. Próg Oskarżenia (Herezja): 9 (+1)
- **Wpływ na Score:** `22.9 pkt` (Różnica vs Baza: `-27.3 pkt`) = **POGORSZENIE BALANSU**

### L1_THRESHOLD_MINUS1: 1. Próg Oskarżenia (Herezja): 7 (-1)
- **Wpływ na Score:** `37.5 pkt` (Różnica vs Baza: `-12.7 pkt`) = **POGORSZENIE BALANSU**

### L1_MAX_ERAS_PLUS1: 2. Maksymalny limit Er: 9 (+1)
- **Wpływ na Score:** `50.2 pkt` (Różnica vs Baza: `+0.0 pkt`) = **OPTYMALNY STABILNY**

### L1_MAX_ERAS_MINUS1: 2. Maksymalny limit Er: 7 (-1)
- **Wpływ na Score:** `50.2 pkt` (Różnica vs Baza: `+0.0 pkt`) = **OPTYMALNY STABILNY**

### L1_START_GOLD_PLUS1: 3. Złoto startowe: 4zł (+1)
- **Wpływ na Score:** `50.2 pkt` (Różnica vs Baza: `+0.0 pkt`) = **OPTYMALNY STABILNY**

### L1_START_GOLD_MINUS1: 3. Złoto startowe: 2zł (-1)
- **Wpływ na Score:** `50.2 pkt` (Różnica vs Baza: `+0.0 pkt`) = **OPTYMALNY STABILNY**

### L1_AGENTS_PLUS1: 4. Liczba agentów na gracza: 4 (+1)
- **Wpływ na Score:** `50.2 pkt` (Różnica vs Baza: `+0.0 pkt`) = **OPTYMALNY STABILNY**

### L1_AGENTS_MINUS1: 4. Liczba agentów na gracza: 2 (-1)
- **Wpływ na Score:** `50.2 pkt` (Różnica vs Baza: `+0.0 pkt`) = **OPTYMALNY STABILNY**

### L1_HAND_LIMIT_PLUS1: 5. Limit kart na ręce: 6 (+1)
- **Wpływ na Score:** `50.2 pkt` (Różnica vs Baza: `+0.0 pkt`) = **OPTYMALNY STABILNY**

### L1_HAND_LIMIT_MINUS1: 5. Limit kart na ręce: 4 (-1)
- **Wpływ na Score:** `50.2 pkt` (Różnica vs Baza: `+0.0 pkt`) = **OPTYMALNY STABILNY**

### L1_AUTODAFE_COOLDOWN_PLUS1: 6. Cooldown Autodafé: Co 3 Ery (+1)
- **Wpływ na Score:** `50.2 pkt` (Różnica vs Baza: `+0.0 pkt`) = **OPTYMALNY STABILNY**

### L1_AUTODAFE_COOLDOWN_MINUS1: 6. Cooldown Autodafé: Co 1 Erę (-1)
- **Wpływ na Score:** `50.2 pkt` (Różnica vs Baza: `+0.0 pkt`) = **OPTYMALNY STABILNY**
