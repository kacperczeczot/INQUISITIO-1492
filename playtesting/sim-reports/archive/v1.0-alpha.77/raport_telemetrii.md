# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.77

**Wersja Balansu:** `v1.0-alpha.77` | **Data:** 2026-08-24 17:42 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 5.06s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🟠 ** 68.3** | 🟡 86.9 | 33.3% | - | 36.3% | - | 34.0% | 29.7% | 🟠 WYMAGA UWAGI |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 54.4** | 🟠 61.3 | 33.3% | - | 32.5% | 24.7% | - | 42.8% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 ** 17.0** | 🟡 80.9 | 33.3% | - | 28.7% | 38.0% | 33.3% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🟠 ** 60.0** | 🟠 70.4 | 33.3% | - | - | 27.9% | 30.9% | 41.2% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 ** 14.6** | 🔴 14.6 | 33.3% | 63.3% | 26.4% | - | - | 10.3% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 35.3** | 🔴 35.3 | 33.3% | 52.2% | 27.0% | - | 20.8% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 ** 40.8** | 🔴 47.9 | 33.3% | 43.9% | 19.4% | 36.7% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 **  0.3** | 🔴 5.8 | 33.3% | 76.0% | - | - | 16.7% | 7.3% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 **  2.3** | 🔴 7.5 | 33.3% | 73.1% | - | 14.5% | - | 12.4% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 **  9.4** | 🔴 31.1 | 33.3% | 50.9% | - | 14.5% | 34.6% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟡 ** 87.1** | 🟡 87.1 | 25.0% | 24.3% | 25.1% | 28.1% | 22.5% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟠 ** 63.7** | 🟠 63.7 | 25.0% | 33.3% | - | 19.7% | 25.4% | 21.6% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🟢 ** 97.8** | 🟢 97.8 | 25.0% | 24.3% | 25.6% | 24.9% | - | 25.2% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟡 ** 86.5** | 🟡 86.5 | 25.0% | 27.3% | 26.9% | - | 22.8% | 23.0% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🟠 ** 69.4** | 🟠 69.4 | 25.0% | - | 20.7% | 21.3% | 26.4% | 31.6% | 🟠 WYMAGA UWAGI |
| `5p-full` | 5 | 🔴 ** 13.9** | 🔴 29.5 | 20.0% | 37.9% | 17.2% | 14.5% | 18.6% | 11.8% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.09 🟢 | 0.0% 🟢 | 0.2% 🟢 | 1.13 🟢 | 6.24 🔴 | 13.2zł | 7.87 | 🟢 OPTYMALNA |
| `3p-cienie-korona-gildia` | 6.68 🟡 | 0.0% 🟢 | 6.1% 🟢 | 1.18 🟢 | 7.27 🔴 | 13.88zł | 9.03 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 6.82 🟡 | 0.8% 🟢 | 6.1% 🟢 | 1.21 🟢 | 6.42 🔴 | 10.31zł | 7.9 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.32 🟢 | 0.0% 🟢 | 6.5% 🟢 | 1.15 🟢 | 6.56 🔴 | 4.58zł | 8.36 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 5.61 🟢 | 0.0% 🟢 | 1.1% 🟢 | 1.65 🟢 | 6.29 🔴 | 13.9zł | 9.26 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 5.75 🟢 | 0.0% 🟢 | 1.0% 🟢 | 1.67 🟢 | 5.62 🔴 | 10.56zł | 8.63 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-korona` | 6.53 🟡 | 0.1% 🟢 | 5.8% 🟢 | 1.76 🟢 | 7.11 🔴 | 11.01zł | 9.28 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 4.89 🟡 | 0.0% 🟢 | 1.1% 🟢 | 1.41 🟢 | 5.41 🔴 | 5.08zł | 8.93 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 5.91 🟢 | 0.0% 🟢 | 6.6% 🟢 | 1.66 🟢 | 6.57 🔴 | 5.68zł | 9.59 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 5.8 🟢 | 0.0% 🟢 | 6.6% 🟢 | 1.62 🟢 | 5.44 🔴 | 2.55zł | 8.65 | 🟢 OPTYMALNA |
| `4p-core` | 5.98 🟢 | 0.0% 🟢 | 4.9% 🟢 | 1.71 🟢 | 7.07 🔴 | 8.29zł | 7.96 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.63 🟢 | 0.0% 🟢 | 5.7% 🟢 | 1.63 🟢 | 6.79 🔴 | 4.3zł | 8.48 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.86 🟢 | 0.0% 🟢 | 5.0% 🟢 | 1.58 🟢 | 7.36 🔴 | 10.47zł | 8.6 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.54 🟢 | 0.0% 🟢 | 0.9% 🟢 | 1.63 🟢 | 6.94 🔴 | 10.27zł | 8.34 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.77 🟢 | 0.0% 🟢 | 5.1% 🟢 | 1.05 🟢 | 6.54 🔴 | 9.23zł | 7.87 | 🟢 OPTYMALNA |
| `5p-full` | 5.15 🟢 | 0.0% 🟢 | 4.1% 🟢 | 1.45 🟢 | 6.38 🔴 | 7.85zł | 7.76 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.240 | Ekstremalny Deadlock (Era 11+): 1.2% gier (>0.5%) |
| `3p-cienie-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 0.120 | Ekstremalny Deadlock (Era 11+): 0.6% gier (>0.5%) |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.560 | Ekstremalny Deadlock (Era 11+): 7.8% gier (>0.5%) |
| `3p-korona-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.160 | Ekstremalny Deadlock (Era 11+): 0.8% gier (>0.5%) |
| `3p-oficjum-alandalus-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-korona` | ⚠️ Ostrzeżenie Witalności | 0.160 | Ekstremalny Deadlock (Era 11+): 0.8% gier (>0.5%) |
| `3p-oficjum-kabala-gildia` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.936 | Przedwczesne Zwycięstwa (Era 1-2): 0.8% gier (>0.5%), Nadmiar Wczesnych Zakończeń (Era 3-4): 38.7% gier (>25.0%), Zbyt Krótka Średnia Rozgrywka 4.89 Er (<5.0 Er), Martwa ścieżka stosy (swiete-oficjum): 4/760 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 34/731 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 40/509 wygranych (<8%) — gra tylko skazania |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | ⚠️ Ostrzeżenie Witalności | 0.750 | Nadmiar Wczesnych Zakończeń (Era 3-4): 32.5% gier (>25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 30 |   0.2% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 563 |   3.5% | `██                  ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 2,413 |  15.1% | `████████            ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 3,876 |  24.2% | `████████████        ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 4,084 |  25.5% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 2,636 |  16.5% | `████████            ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 1,542 |   9.6% | `█████               ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 516 |   3.2% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 218 |   1.4% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 65 |   0.4% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 30 |   0.2% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 13** | 18 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 14** | 9 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 30 | 11 | 19 | 0 | 0 | 0 | **CAA (19)** |
| **Era 3** | 563 | 228 | 141 | 12 | 182 | 0 | **SO (228)** |
| **Era 4** | 2,413 | 932 | 450 | 79 | 866 | 86 | **SO (932)** |
| **Era 5** | 3,876 | 1,440 | 620 | 395 | 978 | 443 | **SO (1,440)** |
| **Era 6** | 4,084 | 979 | 1,047 | 881 | 523 | 654 | **CAA (1,047)** |
| **Era 7** | 2,636 | 874 | 381 | 609 | 210 | 562 | **SO (874)** |
| **Era 8** | 1,542 | 396 | 118 | 358 | 62 | 608 | **GC (608)** |
| **Era 9** | 516 | 151 | 46 | 137 | 22 | 160 | **GC (160)** |
| **Era 10** | 218 | 47 | 25 | 95 | 10 | 41 | **KB (95)** |
| **Era 11** | 65 | 2 | 9 | 42 | 2 | 10 | **KB (42)** |
| **Era 12** | 30 | 4 | 1 | 19 | 1 | 5 | **KB (19)** |
| **Era 13** | 18 | 1 | 1 | 15 | 1 | 0 | **KB (15)** |
| **Era 14** | 9 | 0 | 0 | 6 | 3 | 0 | **KB (6)** |
| **SUMA** | **16,000** | **5,065** | **2,858** | **2,648** | **2,860** | **2,569** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **5.98** |  0.2% | 15.7% | 67.9% | 15.8% |  0.4% | **KB (40.2%)** |
| `4p-no-cienie` | **5.63** |  0.0% | 18.0% | 75.1% |  6.8% |  0.1% | **KB (31.8%)** |
| `4p-no-kabala` | **5.86** |  0.3% | 13.8% | 77.3% |  8.6% |  0.0% | **KB (31.9%)** |
| `4p-no-korona` | **5.54** |  0.5% | 24.5% | 66.5% |  8.5% |  0.0% | **CAA (34.8%)** |
| `4p-no-oficjum` | **5.77** |  0.1% | 16.3% | 73.3% | 10.3% |  0.0% | **KB (32.1%)** |