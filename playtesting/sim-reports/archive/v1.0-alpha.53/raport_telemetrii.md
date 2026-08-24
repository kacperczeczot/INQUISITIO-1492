# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.53

**Wersja Balansu:** `v1.0-alpha.53` | **Data:** 2026-08-23 15:48 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 44.94s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 ** 40.6** | 🟡 80.8 | 33.3% | - | 38.4% | - | 29.2% | 32.4% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 35.2** | 🟠 73.0 | 33.3% | - | 26.1% | 35.6% | - | 38.3% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 **  7.3** | 🟢 94.4 | 33.3% | - | 34.2% | 31.4% | 34.3% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 26.4** | 🔴 35.8 | 33.3% | - | - | 27.9% | 20.3% | 51.8% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 **  2.2** | 🔴 10.7 | 33.3% | 67.6% | 23.9% | - | - | 8.5% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 **  4.3** | 🔴 20.1 | 33.3% | 60.2% | 23.4% | - | 16.4% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 **  5.9** | 🔴 34.7 | 33.3% | 52.6% | 21.6% | 25.8% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 **  0.9** | 🔴 3.0 | 33.3% | 84.2% | - | - | 5.6% | 10.2% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 **  3.4** | 🔴 11.4 | 33.3% | 67.4% | - | 21.6% | - | 11.0% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 **  5.0** | 🔴 20.8 | 33.3% | 59.6% | - | 16.1% | 24.3% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🔴 ** 39.1** | 🟡 77.5 | 25.0% | 23.4% | 22.2% | 30.6% | 23.8% | - | 🔴 ODCHYLONY |
| `4p-no-cienie` | 4 | 🔴 ** 21.3** | 🟠 70.8 | 25.0% | 29.4% | - | 22.4% | 28.8% | 19.5% | 🔴 ODCHYLONY |
| `4p-no-kabala` | 4 | 🔴 ** 51.4** | 🟠 72.6 | 25.0% | 22.1% | 23.3% | 31.8% | - | 22.7% | 🔴 ODCHYLONY |
| `4p-no-korona` | 4 | 🔴 ** 16.7** | 🟠 74.7 | 25.0% | 28.3% | 25.1% | - | 27.6% | 19.0% | 🔴 ODCHYLONY |
| `4p-no-oficjum` | 4 | 🔴 ** 50.1** | 🟠 73.7 | 25.0% | - | 20.7% | 31.1% | 24.9% | 23.3% | 🔴 ODCHYLONY |
| `5p-full` | 5 | 🔴 **  3.4** | 🔴 24.4 | 20.0% | 39.7% | 17.8% | 18.9% | 14.4% | 9.2% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.21 🟢 | 0.0% 🟢 | 0.5% 🟢 | 1.14 🟢 | 5.91 🔴 | 10.06zł | 8.23 | 🟢 OPTYMALNA |
| `3p-cienie-korona-gildia` | 6.52 🟡 | 0.0% 🟢 | 5.7% 🟢 | 1.18 🟢 | 6.39 🔴 | 10.35zł | 8.98 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 6.69 🟡 | 1.0% 🟢 | 6.5% 🟢 | 1.2 🟢 | 5.47 🔴 | 9.44zł | 7.77 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.48 🟢 | 0.0% 🟢 | 7.3% 🟢 | 1.15 🟢 | 6.67 🔴 | 3.31zł | 9.0 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 5.42 🟢 | 0.0% 🟢 | 2.4% 🟢 | 1.45 🟢 | 5.32 🔴 | 9.47zł | 8.91 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 5.56 🟢 | 0.0% 🟢 | 2.5% 🟢 | 1.54 🟢 | 4.37 🟢 | 8.54zł | 8.33 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-korona` | 6.08 🟢 | 0.0% 🟢 | 7.0% 🟢 | 1.6 🟢 | 5.39 🔴 | 8.93zł | 8.84 | 🟢 OPTYMALNA |
| `3p-oficjum-kabala-gildia` | 5.33 🟢 | 0.0% 🟢 | 3.2% 🟢 | 1.38 🟢 | 5.64 🔴 | 3.2zł | 9.0 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-gildia` | 5.67 🟢 | 0.0% 🟢 | 8.6% 🟢 | 1.44 🟢 | 5.76 🔴 | 3.26zł | 9.39 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 5.55 🟢 | 0.0% 🟢 | 9.0% 🟢 | 1.43 🟢 | 4.61 🟡 | 2.34zł | 8.66 | 🟢 OPTYMALNA |
| `4p-core` | 5.85 🟢 | 0.0% 🟢 | 6.3% 🟢 | 1.57 🟢 | 5.98 🔴 | 6.88zł | 8.0 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.48 🟢 | 0.0% 🟢 | 7.3% 🟢 | 1.42 🟢 | 6.05 🔴 | 2.79zł | 8.55 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.77 🟢 | 0.0% 🟢 | 6.0% 🟢 | 1.51 🟢 | 6.42 🔴 | 7.47zł | 8.47 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.49 🟢 | 0.0% 🟢 | 2.0% 🟢 | 1.5 🟢 | 6.06 🔴 | 7.26zł | 8.25 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.53 🟢 | 0.0% 🟢 | 4.8% 🟢 | 0.99 🟢 | 5.37 🔴 | 7.11zł | 7.91 | 🟢 OPTYMALNA |
| `5p-full` | 4.98 🟡 | 0.0% 🟢 | 4.9% 🟢 | 1.33 🟢 | 5.31 🔴 | 5.79zł | 7.76 | ⚠️ WARTOŚCI BRZEGOWE |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.689 | Przedwczesne Zwycięstwa (Era 1-2): 1.2% gier (>0.5%), Ekstremalny Deadlock (Era 10+): 2.0% gier (>1.0%) |
| `3p-cienie-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 0.728 | Przedwczesne Zwycięstwa (Era 1-2): 0.6% gier (>0.5%), Ekstremalny Deadlock (Era 10+): 2.9% gier (>1.0%) |
| `3p-cienie-korona-kabala` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.558 | Ekstremalny Deadlock (Era 10+): 12.8% gier (>1.0%) |
| `3p-korona-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.304 | Ekstremalny Deadlock (Era 10+): 1.5% gier (>1.0%) |
| `3p-oficjum-alandalus-gildia` | ⚠️ Ostrzeżenie Witalności | 1.574 | Przedwczesne Zwycięstwa (Era 1-2): 1.1% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 7.1% gier (>6.0%), Martwa ścieżka stosy (swiete-oficjum): 92/6759 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-alandalus-kabala` | ⚠️ Ostrzeżenie Witalności | 1.530 | Ekstremalny Deadlock (Era 10+): 1.7% gier (>1.0%), Martwa ścieżka stosy (swiete-oficjum): 113/6018 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-alandalus-korona` | ⚠️ Ostrzeżenie Witalności | 1.764 | Ekstremalny Deadlock (Era 10+): 2.8% gier (>1.0%), Martwa ścieżka stosy (swiete-oficjum): 99/5262 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 1.232 | Zbyt Wczesne Zakończenia (Era 1-3): 6.3% gier (>6.0%), Martwa ścieżka stosy (swiete-oficjum): 1/8415 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 25/6739 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.422 | Ekstremalny Deadlock (Era 10+): 1.1% gier (>1.0%), Martwa ścieżka stosy (swiete-oficjum): 32/5957 wygranych (<8%) — gra tylko skazania |
| `4p-core` | ⚠️ Ostrzeżenie Witalności | 0.684 | Przedwczesne Zwycięstwa (Era 1-2): 0.7% gier (>0.5%), Ekstremalny Deadlock (Era 10+): 2.6% gier (>1.0%) |
| `4p-no-cienie` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 202/2938 wygranych (<8%) — gra tylko skazania |
| `4p-no-kabala` | ⚠️ Ostrzeżenie Witalności | 0.345 | Przedwczesne Zwycięstwa (Era 1-2): 1.1% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 6.7% gier (>6.0%) |
| `4p-no-korona` | ⚠️ Ostrzeżenie Witalności | 1.499 | Przedwczesne Zwycięstwa (Era 1-2): 1.1% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 6.3% gier (>6.0%), Martwa ścieżka stosy (swiete-oficjum): 130/2831 wygranych (<8%) — gra tylko skazania |
| `4p-no-oficjum` | ⚠️ Ostrzeżenie Witalności | 0.387 | Przedwczesne Zwycięstwa (Era 1-2): 1.1% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 7.2% gier (>6.0%) |
| `5p-full` | ⚠️ Ostrzeżenie Witalności | 1.974 | Przedwczesne Zwycięstwa (Era 1-2): 1.5% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 9.8% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.98 Er (<5.0 Er), Martwa ścieżka stosy (swiete-oficjum): 68/3966 wygranych (<8%) — gra tylko skazania |

## 3.1. Frakcje Wymagające Uwagi

| Frakcja | Śr. Win Share (wszystkie setupy) | Najgorszy Setup | Max Odchylenie od Ideału | Status |
| :--- | :---: | :--- | :---: | :--- |
| **SO** | 48.6% | `3p-oficjum-kabala-gildia` | +50.9% | 🟡 DOMINUJE |
| **KT** | 22.7% | `3p-oficjum-kabala-gildia` | -27.7% | 🟡 SŁABA |
| **GC** | 22.4% | `3p-oficjum-alandalus-gildia` | -24.8% | 🟡 SŁABA |
| **KB** | 26.7% | `3p-oficjum-korona-kabala` | -17.2% | 🟡 SŁABA |
| **CAA** | 25.2% | `3p-oficjum-alandalus-korona` | -11.7% | 🟡 SŁABA |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `3p-oficjum-kabala-gildia` | 🔴 **  0.9** | SO dominuje (84.2% vs ideal 33.3%) |
| `3p-oficjum-alandalus-gildia` | 🔴 **  2.2** | SO dominuje (67.6% vs ideal 33.3%) |
| `3p-oficjum-korona-gildia` | 🔴 **  3.4** | SO dominuje (67.4% vs ideal 33.3%) |
| `5p-full` | 🔴 **  3.4** | SO dominuje (39.7% vs ideal 20.0%) |
| `3p-oficjum-alandalus-kabala` | 🔴 **  4.3** | SO dominuje (60.2% vs ideal 33.3%) |
| `3p-oficjum-korona-kabala` | 🔴 **  5.0** | SO dominuje (59.6% vs ideal 33.3%) |
| `3p-oficjum-alandalus-korona` | 🔴 **  5.9** | SO dominuje (52.6% vs ideal 33.3%) |
| `3p-cienie-korona-kabala` | 🔴 **  7.3** | KB za słaba (31.4% vs ideal 33.3%) |
| `4p-no-korona` | 🔴 ** 16.7** | GC za słaba (19.0% vs ideal 25.0%) |
| `4p-no-cienie` | 🔴 ** 21.3** | GC za słaba (19.5% vs ideal 25.0%) |
| `3p-korona-kabala-gildia` | 🔴 ** 26.4** | GC dominuje (51.8% vs ideal 33.3%) |
| `3p-cienie-korona-gildia` | 🔴 ** 35.2** | CAA za słaba (26.1% vs ideal 33.3%) |
| `4p-core` | 🔴 ** 39.1** | KB dominuje (30.6% vs ideal 25.0%) |
| `3p-cienie-kabala-gildia` | 🔴 ** 40.6** | CAA dominuje (38.4% vs ideal 33.3%) |
| `4p-no-oficjum` | 🔴 ** 50.1** | KB dominuje (31.1% vs ideal 25.0%) |
| `4p-no-kabala` | 🔴 ** 51.4** | KB dominuje (31.8% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 998 |   0.6% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 7,919 |   4.9% | `██                  ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 25,846 |  16.2% | `████████            ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 37,707 |  23.6% | `████████████        ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 40,768 |  25.5% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 23,404 |  14.6% | `███████             ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 15,224 |   9.5% | `█████               ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 5,121 |   3.2% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 1,729 |   1.1% | `█                   ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 11** | 756 |   0.5% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 282 |   0.2% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 13** | 132 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 14** | 114 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 998 | 42 | 899 | 0 | 57 | 0 | **CAA (899)** |
| **Era 3** | 7,919 | 1,768 | 2,492 | 2,031 | 1,623 | 5 | **CAA (2,492)** |
| **Era 4** | 25,846 | 11,039 | 6,272 | 2,708 | 5,276 | 551 | **SO (11,039)** |
| **Era 5** | 37,707 | 17,055 | 4,508 | 7,544 | 5,639 | 2,961 | **SO (17,055)** |
| **Era 6** | 40,768 | 10,325 | 9,526 | 10,174 | 5,065 | 5,678 | **SO (10,325)** |
| **Era 7** | 23,404 | 7,890 | 2,315 | 3,181 | 3,794 | 6,224 | **SO (7,890)** |
| **Era 8** | 15,224 | 3,117 | 1,007 | 2,190 | 2,163 | 6,747 | **GC (6,747)** |
| **Era 9** | 5,121 | 1,554 | 347 | 678 | 626 | 1,916 | **GC (1,916)** |
| **Era 10** | 1,729 | 496 | 195 | 365 | 269 | 404 | **SO (496)** |
| **Era 11** | 756 | 92 | 79 | 314 | 176 | 95 | **KB (314)** |
| **Era 12** | 282 | 51 | 17 | 72 | 125 | 17 | **KT (125)** |
| **Era 13** | 132 | 6 | 13 | 46 | 65 | 2 | **KT (65)** |
| **Era 14** | 114 | 4 | 3 | 23 | 81 | 3 | **KT (81)** |
| **SUMA** | **160,000** | **53,439** | **27,673** | **29,326** | **24,959** | **24,603** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–9 (Późne) % | Ery 10+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **5.85** |  0.7% | 19.7% | 65.0% | 12.1% |  2.6% | **KB (40.8%)** |
| `4p-no-cienie` | **5.48** |  0.1% | 23.5% | 68.8% |  7.3% |  0.2% | **KB (30.7%)** |
| `4p-no-kabala` | **5.77** |  1.1% | 18.9% | 67.2% | 12.2% |  0.5% | **KB (43.1%)** |
| `4p-no-korona` | **5.49** |  1.1% | 27.5% | 61.3% |  9.8% |  0.4% | **CAA (32.1%)** |
| `4p-no-oficjum` | **5.53** |  1.1% | 20.9% | 70.2% |  7.8% |  0.1% | **KB (41.2%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **2.0 – 4.5** | 🟡 1.5–2.0 / 4.5–5.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 75 | 🟠 ≥ 60 | 🔴 < 60