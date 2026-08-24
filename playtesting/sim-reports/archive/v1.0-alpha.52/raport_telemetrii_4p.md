# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.52

**Wersja Balansu:** `v1.0-alpha.52` | **Data:** 2026-08-23 15:24 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 17.89s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🔴 ** 47.4** | 🟠 66.5 | 25.0% | 31.8% | 18.2% | 25.2% | 24.8% | - | 🔴 ODCHYLONY |
| `4p-no-cienie` | 4 | 🟠 ** 62.8** | 🟠 68.2 | 25.0% | 32.2% | - | 21.2% | 20.8% | 25.8% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🔴 ** 48.9** | 🟠 70.3 | 25.0% | 27.0% | 18.8% | 23.9% | - | 30.4% | 🔴 ODCHYLONY |
| `4p-no-korona` | 4 | 🔴 ** 34.4** | 🟠 63.5 | 25.0% | 33.8% | 20.2% | - | 23.8% | 22.2% | 🔴 ODCHYLONY |
| `4p-no-oficjum` | 4 | 🔴 ** 31.8** | 🔴 58.3 | 25.0% | - | 18.4% | 30.1% | 19.7% | 31.8% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.38 🟢 | 0.0% 🟢 | 6.1% 🟢 | 1.99 🟡 | 5.34 🔴 | 6.53zł | 8.08 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.07 🟢 | 0.0% 🟢 | 6.6% 🟢 | 1.79 🟢 | 5.37 🔴 | 2.68zł | 8.53 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.22 🟢 | 0.0% 🟢 | 5.5% 🟢 | 1.9 🟡 | 5.48 🔴 | 6.95zł | 8.48 | 🟢 OPTYMALNA |
| `4p-no-korona` | 4.94 🟡 | 0.0% 🟢 | 1.7% 🟢 | 1.82 🟡 | 5.17 🔴 | 6.76zł | 8.22 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-oficjum` | 5.04 🟢 | 0.0% 🟢 | 4.7% 🟢 | 1.31 🟢 | 4.81 🟡 | 6.71zł | 7.88 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | ⚠️ Ostrzeżenie Witalności | 0.338 | Przedwczesne Zwycięstwa (Era 1-2): 0.8% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 7.4% gier (>6.0%) |
| `4p-no-cienie` | ⚠️ Ostrzeżenie Witalności | 0.082 | Zbyt Wczesne Zakończenia (Era 1-3): 6.8% gier (>6.0%) |
| `4p-no-kabala` | ⚠️ Ostrzeżenie Witalności | 0.363 | Przedwczesne Zwycięstwa (Era 1-2): 1.1% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 6.9% gier (>6.0%) |
| `4p-no-korona` | ⚠️ Ostrzeżenie Witalności | 0.612 | Przedwczesne Zwycięstwa (Era 1-2): 1.2% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 8.3% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.94 Er (<5.0 Er) |
| `4p-no-oficjum` | ⚠️ Ostrzeżenie Witalności | 0.604 | Przedwczesne Zwycięstwa (Era 1-2): 1.2% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 9.1% gier (>6.0%) |

## 3.1. Frakcje Wymagające Uwagi

| Frakcja | Śr. Win Share (wszystkie setupy) | Najgorszy Setup | Max Odchylenie od Ideału | Status |
| :--- | :---: | :--- | :---: | :--- |
| **SO** | 31.2% | `4p-no-korona` | +8.8% | 🟡 DOMINUJE |
| **CAA** | 18.9% | `4p-core` | -6.8% | 🟡 SŁABA |
| **GC** | 27.6% | `4p-no-oficjum` | +6.8% | 🟡 DOMINUJE |
| **KT** | 22.3% | `4p-no-oficjum` | -5.3% | 🟡 SŁABA |
| **KB** | 25.1% | `4p-no-oficjum` | +5.1% | 🟡 DOMINUJE |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `4p-no-oficjum` | 🔴 ** 31.8** | GC dominuje (31.8% vs ideal 25.0%) |
| `4p-no-korona` | 🔴 ** 34.4** | SO dominuje (33.8% vs ideal 25.0%) |
| `4p-core` | 🔴 ** 47.4** | SO dominuje (31.8% vs ideal 25.0%) |
| `4p-no-kabala` | 🔴 ** 48.9** | CAA za słaba (18.8% vs ideal 25.0%) |
| `4p-no-cienie` | 🟠 ** 62.8** | SO dominuje (32.2% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 433 |   0.9% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 3,419 |   6.8% | `███                 ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 12,372 |  24.7% | `████████████        ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 14,182 |  28.4% | `██████████████      ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 14,310 |  28.6% | `██████████████      ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 3,735 |   7.5% | `████                ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 1,120 |   2.2% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 349 |   0.7% | `                    ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 74 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 11** | 6 |   0.0% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Szans Wygranych Frakcji w poszczególnych Erach (% Wygranych Frakcji w danej Erze)

*Wiersze sumują się do 100.0% — wskazują która frakcja dominuje w danej fazie czasowej partii.*

| Era Końca Gry | Gry w Erze | SO % | CAA % | KB % | KT % | GC % | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 433 |   0.0% |  94.9% |   0.0% |   5.1% |   0.0% | **CAA (94.9%)** |
| **Era 3** | 3,419 |  10.9% |  28.6% |  25.9% |  33.1% |   1.4% | **KT (33.1%)** |
| **Era 4** | 12,372 |  29.2% |  19.1% |  22.6% |  19.6% |   9.4% | **SO (29.2%)** |
| **Era 5** | 14,182 |  33.2% |  11.3% |  17.3% |  16.0% |  22.1% | **SO (33.2%)** |
| **Era 6** | 14,310 |  16.2% |  12.9% |  23.4% |  14.9% |  32.6% | **GC (32.6%)** |
| **Era 7** | 3,735 |  23.5% |   5.4% |  11.5% |  19.7% |  39.8% | **GC (39.8%)** |
| **Era 8** | 1,120 |  26.0% |   9.7% |   8.4% |  12.9% |  43.0% | **GC (43.0%)** |
| **Era 9** | 349 |  75.4% |   5.4% |   2.9% |   8.3% |   8.0% | **SO (75.4%)** |
| **Era 10** | 74 |  40.5% |   6.8% |  20.3% |  20.3% |  12.2% | **SO (40.5%)** |
| **Era 11** | 6 |  16.7% |  16.7% |  50.0% |  16.7% |   0.0% | **KB (50.0%)** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–9 (Późne) % | Ery 10+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **5.38** |  0.8% | 29.8% | 62.8% |  5.9% |  0.7% | **KB (31.8%)** |
| `4p-no-cienie` | **5.07** |  0.1% | 30.9% | 67.0% |  2.0% |  0.0% | **GC (39.0%)** |
| `4p-no-kabala` | **5.22** |  1.1% | 28.3% | 67.8% |  2.8% |  0.0% | **GC (39.0%)** |
| `4p-no-korona` | **4.94** |  1.2% | 38.7% | 57.7% |  2.4% |  0.0% | **GC (34.7%)** |
| `4p-no-oficjum` | **5.04** |  1.2% | 30.3% | 66.9% |  1.6% |  0.0% | **GC (49.8%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **2.0 – 4.5** | 🟡 1.5–2.0 / 4.5–5.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 75 | 🟠 ≥ 60 | 🔴 < 60