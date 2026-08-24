# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.73

**Wersja Balansu:** `v1.0-alpha.73` | **Data:** 2026-08-24 13:03 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 4.43s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🟡 ** 80.2** | 🟢 96.0 | 33.3% | - | 34.6% | - | 32.1% | 33.3% | 🟡 AKCEPTOWALNY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 47.3** | 🔴 47.3 | 33.3% | - | 19.9% | 34.8% | - | 45.3% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 ** 12.2** | 🟠 65.4 | 33.3% | - | 24.9% | 41.1% | 34.0% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 45.7** | 🔴 51.5 | 33.3% | - | - | 27.2% | 26.1% | 46.7% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 **  6.1** | 🔴 20.1 | 33.3% | 59.0% | 28.1% | - | - | 12.9% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 41.5** | 🔴 41.5 | 33.3% | 49.8% | 27.8% | - | 22.4% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 ** 49.1** | 🟠 60.0 | 33.3% | 42.1% | 23.4% | 34.5% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 **  1.7** | 🔴 10.3 | 33.3% | 69.1% | - | - | 16.7% | 14.2% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 **  4.1** | 🔴 13.7 | 33.3% | 65.5% | - | 16.8% | - | 17.7% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 ** 11.3** | 🔴 37.5 | 33.3% | 47.7% | - | 16.3% | 36.0% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟠 ** 73.1** | 🟠 73.1 | 25.0% | 18.8% | 25.3% | 29.5% | 26.4% | - | 🟠 WYMAGA UWAGI |
| `4p-no-cienie` | 4 | 🟠 ** 67.9** | 🟠 67.9 | 25.0% | 32.5% | - | 19.9% | 24.1% | 23.5% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🟡 ** 77.6** | 🟡 77.6 | 25.0% | 20.4% | 27.7% | 23.4% | - | 28.5% | 🟡 AKCEPTOWALNY |
| `4p-no-korona` | 4 | 🟡 ** 86.0** | 🟡 86.0 | 25.0% | 25.5% | 28.3% | - | 23.6% | 22.6% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🔴 ** 56.4** | 🔴 56.4 | 25.0% | - | 17.6% | 21.2% | 26.9% | 34.3% | 🔴 ODCHYLONY |
| `5p-full` | 5 | 🔴 ** 40.5** | 🔴 45.6 | 20.0% | 31.5% | 22.3% | 15.5% | 17.6% | 13.1% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.13 🟢 | 0.0% 🟢 | 0.2% 🟢 | 1.14 🟢 | 6.16 🔴 | 11.7zł | 8.01 | 🟢 OPTYMALNA |
| `3p-cienie-korona-gildia` | 6.76 🟡 | 0.0% 🟢 | 5.8% 🟢 | 1.19 🟢 | 7.53 🔴 | 11.69zł | 9.14 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 6.83 🟡 | 0.8% 🟢 | 6.1% 🟢 | 1.22 🟢 | 6.35 🔴 | 10.12zł | 7.87 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.33 🟢 | 0.1% 🟢 | 6.6% 🟢 | 1.14 🟢 | 6.62 🔴 | 3.09zł | 8.5 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 5.75 🟢 | 0.0% 🟢 | 1.1% 🟢 | 1.66 🟢 | 6.34 🔴 | 12.94zł | 9.25 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 5.89 🟢 | 0.0% 🟢 | 1.1% 🟢 | 1.72 🟢 | 5.46 🔴 | 10.69zł | 8.52 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-korona` | 6.62 🟡 | 0.0% 🟢 | 6.0% 🟢 | 1.81 🟡 | 6.7 🔴 | 11.11zł | 9.14 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 5.2 🟢 | 0.0% 🟢 | 1.3% 🟢 | 1.48 🟢 | 5.89 🔴 | 4.44zł | 9.1 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-gildia` | 6.0 🟢 | 0.0% 🟢 | 7.1% 🟢 | 1.66 🟢 | 6.83 🔴 | 4.41zł | 9.65 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 5.95 🟢 | 0.0% 🟢 | 6.7% 🟢 | 1.68 🟢 | 5.64 🔴 | 2.54zł | 8.64 | 🟢 OPTYMALNA |
| `4p-core` | 5.96 🟢 | 0.0% 🟢 | 5.1% 🟢 | 1.74 🟢 | 6.67 🔴 | 8.21zł | 7.83 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.66 🟢 | 0.0% 🟢 | 5.7% 🟢 | 1.61 🟢 | 6.96 🔴 | 3.56zł | 8.5 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.91 🟢 | 0.0% 🟢 | 5.3% 🟢 | 1.61 🟢 | 7.17 🔴 | 9.63zł | 8.5 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.55 🟢 | 0.0% 🟢 | 1.0% 🟢 | 1.62 🟢 | 6.65 🔴 | 9.4zł | 8.3 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.76 🟢 | 0.0% 🟢 | 5.0% 🟢 | 1.06 🟢 | 6.3 🔴 | 8.16zł | 7.87 | 🟢 OPTYMALNA |
| `5p-full` | 5.26 🟢 | 0.0% 🟢 | 4.3% 🟢 | 1.46 🟢 | 6.35 🔴 | 7.42zł | 7.75 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.180 | Ekstremalny Deadlock (Era 11+): 0.9% gier (>0.5%) |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.680 | Ekstremalny Deadlock (Era 11+): 8.4% gier (>0.5%) |
| `3p-korona-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.120 | Ekstremalny Deadlock (Era 11+): 0.6% gier (>0.5%) |
| `3p-oficjum-alandalus-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 45/590 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-alandalus-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-korona` | ⚠️ Ostrzeżenie Witalności | 0.200 | Ekstremalny Deadlock (Era 11+): 1.0% gier (>0.5%) |
| `3p-oficjum-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 1.805 | Przedwczesne Zwycięstwa (Era 1-2): 0.7% gier (>0.5%), Nadmiar Wczesnych Zakończeń (Era 3-4): 29.3% gier (>25.0%), Martwa ścieżka stosy (swiete-oficjum): 5/691 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 35/655 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 32/477 wygranych (<8%) — gra tylko skazania |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | ⚠️ Ostrzeżenie Witalności | 0.120 | Nadmiar Wczesnych Zakończeń (Era 3-4): 26.2% gier (>25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 24 |   0.1% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 472 |   2.9% | `█                   ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 2,161 |  13.5% | `███████             ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 3,793 |  23.7% | `████████████        ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 4,266 |  26.7% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 2,733 |  17.1% | `█████████           ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 1,719 |  10.7% | `█████               ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 519 |   3.2% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 193 |   1.2% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 70 |   0.4% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 28 |   0.2% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 13** | 13 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 14** | 9 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 24 | 8 | 16 | 0 | 0 | 0 | **CAA (16)** |
| **Era 3** | 472 | 159 | 135 | 10 | 168 | 0 | **KT (168)** |
| **Era 4** | 2,161 | 703 | 454 | 77 | 823 | 104 | **KT (823)** |
| **Era 5** | 3,793 | 1,326 | 619 | 380 | 973 | 495 | **SO (1,326)** |
| **Era 6** | 4,266 | 965 | 1,018 | 954 | 598 | 731 | **CAA (1,018)** |
| **Era 7** | 2,733 | 862 | 348 | 672 | 191 | 660 | **SO (862)** |
| **Era 8** | 1,719 | 391 | 137 | 404 | 71 | 716 | **GC (716)** |
| **Era 9** | 519 | 147 | 50 | 128 | 19 | 175 | **GC (175)** |
| **Era 10** | 193 | 49 | 14 | 93 | 10 | 27 | **KB (93)** |
| **Era 11** | 70 | 5 | 6 | 50 | 0 | 9 | **KB (50)** |
| **Era 12** | 28 | 4 | 0 | 20 | 1 | 3 | **KB (20)** |
| **Era 13** | 13 | 0 | 1 | 11 | 1 | 0 | **KB (11)** |
| **Era 14** | 9 | 0 | 1 | 3 | 4 | 1 | **KT (4)** |
| **SUMA** | **16,000** | **4,619** | **2,799** | **2,802** | **2,859** | **2,921** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **5.96** |  0.1% | 14.2% | 70.0% | 15.6% |  0.1% | **KB (40.2%)** |
| `4p-no-cienie` | **5.66** |  0.0% | 18.4% | 72.5% |  9.1% |  0.0% | **KB (31.3%)** |
| `4p-no-kabala` | **5.91** |  0.2% | 11.4% | 78.9% |  9.5% |  0.0% | **CAA (30.3%)** |
| `4p-no-korona` | **5.55** |  0.4% | 24.4% | 66.3% |  8.9% |  0.0% | **CAA (34.9%)** |
| `4p-no-oficjum` | **5.76** |  0.0% | 17.6% | 70.8% | 11.6% |  0.0% | **KB (35.2%)** |