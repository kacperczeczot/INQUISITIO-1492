# Raport 26: Ponowny Audyt +-1 dla Poziomu 1 (Główne Mechaniki z Nowego Punktu)

**Przeanalizowano Wariantów:** 13 | **Próba:** 300 gier/setup | **Czas:** 54.72s
**Nowy Wynik Bazy Poziomu 1:** `52.0 / 100.0 pkt`

## 1. Tabela Porównawcza Wpływu Wariacji +-1 Poziomu 1

| ID | Element Poziomu 1 | Global Score | Różnica vs Baza | 3p Avg | 4p Avg | 5p Avg | Czy Poprawia Wynik? |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_NEW_BAZA` | Current Baseline (Ogólne Zasady Systemowe) | ** 52.0** | `0.0` | 44.6 | 59.4 | 0.0 | ⚪ OPTYMALNY |
| `L1_THRESHOLD_PLUS1` | 1. Próg Oskarżenia (Herezja): 9 (+1) | ** 22.1** | `-29.9` | 9.3 | 35.0 | 0.0 | 🔴 NIE (Pogarsza) |
| `L1_THRESHOLD_MINUS1` | 1. Próg Oskarżenia (Herezja): 7 (-1) | ** 53.5** | `+1.5` | 63.8 | 43.2 | 0.0 | 🟢 TAK (Poprawia) |
| `L1_MAX_ERAS_PLUS1` | 2. Maksymalny limit Er: 9 (+1) | ** 52.6** | `+0.6` | 58.6 | 46.6 | 0.0 | 🟢 TAK (Poprawia) |
| `L1_MAX_ERAS_MINUS1` | 2. Maksymalny limit Er: 7 (-1) | ** 22.8** | `-29.2` | 4.1 | 41.5 | 0.0 | 🔴 NIE (Pogarsza) |
| `L1_START_GOLD_PLUS1` | 3. Złoto startowe: 4zł (+1) | ** 27.4** | `-24.6` | 36.8 | 18.1 | 0.0 | 🔴 NIE (Pogarsza) |
| `L1_START_GOLD_MINUS1` | 3. Złoto startowe: 2zł (-1) | ** 12.1** | `-39.9` | 10.5 | 13.7 | 0.0 | 🔴 NIE (Pogarsza) |
| `L1_AGENTS_PLUS1` | 4. Liczba agentów na gracza: 4 (+1) | ** 32.7** | `-19.3` | 58.9 | 38.1 | 1.0 | 🔴 NIE (Pogarsza) |
| `L1_AGENTS_MINUS1` | 4. Liczba agentów na gracza: 2 (-1) | ** 39.2** | `-12.8` | 16.1 | 62.4 | 0.0 | 🔴 NIE (Pogarsza) |
| `L1_HAND_LIMIT_PLUS1` | 5. Limit kart na ręce: 6 (+1) | ** 22.6** | `-29.4` | 20.4 | 24.9 | 0.0 | 🔴 NIE (Pogarsza) |
| `L1_HAND_LIMIT_MINUS1` | 5. Limit kart na ręce: 4 (-1) | ** 34.2** | `-17.8` | 18.8 | 49.7 | 0.0 | 🔴 NIE (Pogarsza) |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 6. Cooldown Autodafé: Co 3 Ery (+1) | ** 30.9** | `-21.1` | 42.4 | 47.1 | 3.3 | 🔴 NIE (Pogarsza) |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 6. Cooldown Autodafé: Co 1 Erę (-1) | ** 30.9** | `-21.1` | 45.8 | 43.5 | 3.3 | 🔴 NIE (Pogarsza) |

## 2. Podsumowanie Wniosków
- Weryfikacja czy obecne parametry (Próg oskarżenia = 8, start_gold = 3, max_eras = 8, agents = 3, hand = 5, autodafe = 2) są najbardziej optymalnym układem w nowym zbalansowanym ekosystemie.