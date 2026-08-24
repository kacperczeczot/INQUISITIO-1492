# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.76

**Wersja Balansu:** `v1.0-alpha.76` | **Data:** 2026-08-24 16:19 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 4.48s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🟠 ** 65.7** | 🟡 87.0 | 33.3% | - | 37.0% | - | 30.5% | 32.5% | 🟠 WYMAGA UWAGI |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 57.3** | 🔴 57.3 | 33.3% | - | 28.7% | 26.4% | - | 44.9% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 ** 17.0** | 🟡 80.9 | 33.3% | - | 28.7% | 38.0% | 33.3% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 47.4** | 🔴 53.4 | 33.3% | - | - | 27.8% | 26.1% | 46.1% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 **  4.4** | 🔴 14.6 | 33.3% | 64.0% | 23.8% | - | - | 12.2% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 35.3** | 🔴 35.3 | 33.3% | 52.2% | 27.0% | - | 20.8% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 ** 40.8** | 🔴 47.9 | 33.3% | 43.9% | 19.4% | 36.7% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 **  1.0** | 🔴 7.3 | 33.3% | 73.4% | - | - | 15.5% | 11.1% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 **  3.0** | 🔴 9.9 | 33.3% | 69.7% | - | 14.7% | - | 15.6% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 **  9.4** | 🔴 31.1 | 33.3% | 50.9% | - | 14.5% | 34.6% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟡 ** 87.1** | 🟡 87.1 | 25.0% | 24.3% | 25.1% | 28.1% | 22.5% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟠 ** 70.1** | 🟠 70.1 | 25.0% | 31.7% | - | 19.7% | 24.8% | 23.8% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🟢 ** 91.2** | 🟢 91.2 | 25.0% | 24.4% | 22.9% | 26.1% | - | 26.6% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟡 ** 85.6** | 🟡 85.6 | 25.0% | 28.5% | 25.2% | - | 22.6% | 23.7% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🔴 ** 59.3** | 🔴 59.3 | 25.0% | - | 18.2% | 21.3% | 26.9% | 33.6% | 🔴 ODCHYLONY |
| `5p-full` | 5 | 🔴 ** 17.3** | 🔴 30.4 | 20.0% | 37.7% | 16.8% | 16.5% | 17.3% | 11.7% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.16 🟢 | 0.0% 🟢 | 0.3% 🟢 | 1.13 🟢 | 6.42 🔴 | 12.52zł | 7.99 | 🟢 OPTYMALNA |
| `3p-cienie-korona-gildia` | 6.68 🟡 | 0.0% 🟢 | 6.0% 🟢 | 1.19 🟢 | 7.48 🔴 | 12.91zł | 9.12 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 6.82 🟡 | 0.8% 🟢 | 6.1% 🟢 | 1.21 🟢 | 6.42 🔴 | 10.31zł | 7.9 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.38 🟢 | 0.0% 🟢 | 6.6% 🟢 | 1.13 🟢 | 6.71 🔴 | 3.79zł | 8.48 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 5.69 🟢 | 0.0% 🟢 | 1.2% 🟢 | 1.66 🟢 | 6.6 🔴 | 13.35zł | 9.33 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 5.75 🟢 | 0.0% 🟢 | 1.0% 🟢 | 1.67 🟢 | 5.62 🔴 | 10.56zł | 8.63 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-korona` | 6.53 🟡 | 0.1% 🟢 | 5.8% 🟢 | 1.76 🟢 | 7.11 🔴 | 11.01zł | 9.28 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 5.16 🟢 | 0.0% 🟢 | 1.1% 🟢 | 1.45 🟢 | 5.9 🔴 | 4.71zł | 9.04 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-gildia` | 5.94 🟢 | 0.0% 🟢 | 6.7% 🟢 | 1.65 🟢 | 6.77 🔴 | 4.94zł | 9.65 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 5.8 🟢 | 0.0% 🟢 | 6.6% 🟢 | 1.62 🟢 | 5.44 🔴 | 2.55zł | 8.65 | 🟢 OPTYMALNA |
| `4p-core` | 5.98 🟢 | 0.0% 🟢 | 4.9% 🟢 | 1.71 🟢 | 7.07 🔴 | 8.29zł | 7.96 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.65 🟢 | 0.0% 🟢 | 5.7% 🟢 | 1.63 🟢 | 6.84 🔴 | 3.84zł | 8.53 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.86 🟢 | 0.0% 🟢 | 5.0% 🟢 | 1.56 🟢 | 7.44 🔴 | 9.93zł | 8.61 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.56 🟢 | 0.0% 🟢 | 0.9% 🟢 | 1.62 🟢 | 6.93 🔴 | 9.84zł | 8.35 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.76 🟢 | 0.0% 🟢 | 5.0% 🟢 | 1.05 🟢 | 6.56 🔴 | 8.64zł | 7.87 | 🟢 OPTYMALNA |
| `5p-full` | 5.19 🟢 | 0.0% 🟢 | 4.1% 🟢 | 1.46 🟢 | 6.46 🔴 | 7.55zł | 7.79 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.280 | Ekstremalny Deadlock (Era 11+): 1.4% gier (>0.5%) |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.560 | Ekstremalny Deadlock (Era 11+): 7.8% gier (>0.5%) |
| `3p-korona-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.120 | Ekstremalny Deadlock (Era 11+): 0.6% gier (>0.5%) |
| `3p-oficjum-alandalus-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 49/640 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-alandalus-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-korona` | ⚠️ Ostrzeżenie Witalności | 0.160 | Ekstremalny Deadlock (Era 11+): 0.8% gier (>0.5%) |
| `3p-oficjum-kabala-gildia` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.020 | Przedwczesne Zwycięstwa (Era 1-2): 0.6% gier (>0.5%), Nadmiar Wczesnych Zakończeń (Era 3-4): 31.7% gier (>25.0%), Martwa ścieżka stosy (swiete-oficjum): 4/734 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 25/697 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 40/509 wygranych (<8%) — gra tylko skazania |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | ⚠️ Ostrzeżenie Witalności | 0.560 | Nadmiar Wczesnych Zakończeń (Era 3-4): 30.6% gier (>25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 28 |   0.2% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 503 |   3.1% | `██                  ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 2,276 |  14.2% | `███████             ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 3,852 |  24.1% | `████████████        ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 4,195 |  26.2% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 2,720 |  17.0% | `████████            ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 1,595 |  10.0% | `█████               ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 505 |   3.2% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 205 |   1.3% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 65 |   0.4% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 31 |   0.2% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 13** | 16 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 14** | 9 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 28 | 9 | 19 | 0 | 0 | 0 | **CAA (19)** |
| **Era 3** | 503 | 184 | 136 | 12 | 171 | 0 | **SO (184)** |
| **Era 4** | 2,276 | 834 | 445 | 86 | 831 | 80 | **SO (834)** |
| **Era 5** | 3,852 | 1,441 | 616 | 395 | 955 | 445 | **SO (1,441)** |
| **Era 6** | 4,195 | 1,053 | 981 | 897 | 533 | 731 | **SO (1,053)** |
| **Era 7** | 2,720 | 909 | 345 | 625 | 162 | 679 | **SO (909)** |
| **Era 8** | 1,595 | 390 | 108 | 381 | 57 | 659 | **GC (659)** |
| **Era 9** | 505 | 140 | 36 | 132 | 25 | 172 | **GC (172)** |
| **Era 10** | 205 | 40 | 30 | 94 | 9 | 32 | **KB (94)** |
| **Era 11** | 65 | 2 | 9 | 38 | 1 | 15 | **KB (38)** |
| **Era 12** | 31 | 4 | 3 | 18 | 1 | 5 | **KB (18)** |
| **Era 13** | 16 | 1 | 0 | 14 | 1 | 0 | **KB (14)** |
| **Era 14** | 9 | 0 | 0 | 6 | 3 | 0 | **KB (6)** |
| **SUMA** | **16,000** | **5,007** | **2,728** | **2,698** | **2,749** | **2,818** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **5.98** |  0.2% | 15.7% | 67.9% | 15.8% |  0.4% | **KB (40.2%)** |
| `4p-no-cienie` | **5.65** |  0.0% | 16.6% | 75.8% |  7.6% |  0.0% | **KB (32.7%)** |
| `4p-no-kabala` | **5.86** |  0.3% | 13.2% | 78.7% |  7.8% |  0.0% | **KB (33.4%)** |
| `4p-no-korona` | **5.56** |  0.5% | 24.3% | 65.1% | 10.0% |  0.1% | **CAA (32.1%)** |
| `4p-no-oficjum` | **5.76** |  0.1% | 15.8% | 73.9% | 10.2% |  0.0% | **KB (32.5%)** |