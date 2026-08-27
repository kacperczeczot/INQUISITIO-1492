# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.74

**Wersja Balansu:** `v1.0-alpha.74` | **Data:** 2026-08-24 14:49 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 4.65s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🟡 ** 80.2** | 🟢 96.0 | 33.3% | - | 34.6% | - | 32.1% | 33.3% | 🟡 AKCEPTOWALNY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 47.3** | 🔴 47.3 | 33.3% | - | 19.9% | 34.8% | - | 45.3% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 ** 12.2** | 🟠 65.4 | 33.3% | - | 24.9% | 41.1% | 34.0% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 45.7** | 🔴 51.5 | 33.3% | - | - | 27.2% | 26.1% | 46.7% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 **  3.9** | 🔴 13.0 | 33.3% | 65.4% | 23.5% | - | - | 11.1% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 32.3** | 🔴 32.3 | 33.3% | 53.8% | 24.2% | - | 22.0% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 ** 49.7** | 🔴 49.7 | 33.3% | 45.3% | 21.1% | 33.6% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 **  1.1** | 🔴 7.8 | 33.3% | 72.7% | - | - | 15.0% | 12.3% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 **  3.2** | 🔴 10.8 | 33.3% | 68.6% | - | 15.2% | - | 16.2% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 **  9.4** | 🔴 31.1 | 33.3% | 50.9% | - | 14.5% | 34.6% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟡 ** 77.2** | 🟡 77.2 | 25.0% | 22.2% | 23.8% | 30.7% | 23.3% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟠 ** 66.6** | 🟠 66.6 | 25.0% | 32.8% | - | 19.9% | 22.8% | 24.5% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🟡 ** 78.6** | 🟡 78.6 | 25.0% | 19.8% | 26.5% | 25.5% | - | 28.2% | 🟡 AKCEPTOWALNY |
| `4p-no-korona` | 4 | 🟠 ** 67.4** | 🟡 81.5 | 25.0% | 28.0% | 27.1% | - | 23.9% | 21.0% | 🟠 WYMAGA UWAGI |
| `4p-no-oficjum` | 4 | 🔴 ** 56.4** | 🔴 56.4 | 25.0% | - | 17.6% | 21.2% | 26.9% | 34.3% | 🔴 ODCHYLONY |
| `5p-full` | 5 | 🔴 ** 25.8** | 🔴 34.5 | 20.0% | 35.9% | 19.3% | 15.4% | 17.3% | 12.1% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.13 🟢 | 0.0% 🟢 | 0.2% 🟢 | 1.14 🟢 | 6.16 🔴 | 11.7zł | 8.01 | 🟢 OPTYMALNA |
| `3p-cienie-korona-gildia` | 6.76 🟡 | 0.0% 🟢 | 5.8% 🟢 | 1.19 🟢 | 7.53 🔴 | 11.69zł | 9.14 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 6.83 🟡 | 0.8% 🟢 | 6.1% 🟢 | 1.22 🟢 | 6.35 🔴 | 10.12zł | 7.87 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.33 🟢 | 0.1% 🟢 | 6.6% 🟢 | 1.14 🟢 | 6.62 🔴 | 3.09zł | 8.5 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 5.53 🟢 | 0.0% 🟢 | 1.0% 🟢 | 1.56 🟢 | 6.13 🔴 | 12.49zł | 9.23 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 5.77 🟢 | 0.0% 🟢 | 0.9% 🟢 | 1.67 🟢 | 5.33 🔴 | 10.56zł | 8.57 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-korona` | 6.46 🟢 | 0.0% 🟢 | 5.6% 🟢 | 1.78 🟢 | 6.75 🔴 | 10.77zł | 9.22 | 🟢 OPTYMALNA |
| `3p-oficjum-kabala-gildia` | 5.1 🟢 | 0.0% 🟢 | 1.1% 🟢 | 1.44 🟢 | 5.81 🔴 | 4.38zł | 9.08 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-gildia` | 5.87 🟢 | 0.0% 🟢 | 6.8% 🟢 | 1.62 🟢 | 6.68 🔴 | 4.46zł | 9.65 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 5.8 🟢 | 0.0% 🟢 | 6.6% 🟢 | 1.62 🟢 | 5.44 🔴 | 2.55zł | 8.65 | 🟢 OPTYMALNA |
| `4p-core` | 6.0 🟢 | 0.0% 🟢 | 4.9% 🟢 | 1.75 🟢 | 6.88 🔴 | 8.26zł | 7.94 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.65 🟢 | 0.0% 🟢 | 5.7% 🟢 | 1.61 🟢 | 6.89 🔴 | 3.63zł | 8.56 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.94 🟢 | 0.0% 🟢 | 5.0% 🟢 | 1.6 🟢 | 7.39 🔴 | 9.59zł | 8.54 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.48 🟢 | 0.0% 🟢 | 0.8% 🟢 | 1.58 🟢 | 6.52 🔴 | 9.4zł | 8.32 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.76 🟢 | 0.0% 🟢 | 5.0% 🟢 | 1.06 🟢 | 6.3 🔴 | 8.16zł | 7.87 | 🟢 OPTYMALNA |
| `5p-full` | 5.25 🟢 | 0.0% 🟢 | 4.2% 🟢 | 1.46 🟢 | 6.42 🔴 | 7.4zł | 7.79 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.180 | Ekstremalny Deadlock (Era 11+): 0.9% gier (>0.5%) |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.680 | Ekstremalny Deadlock (Era 11+): 8.4% gier (>0.5%) |
| `3p-korona-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.120 | Ekstremalny Deadlock (Era 11+): 0.6% gier (>0.5%) |
| `3p-oficjum-alandalus-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 43/654 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-alandalus-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 1.920 | Nadmiar Wczesnych Zakończeń (Era 3-4): 32.2% gier (>25.0%), Martwa ścieżka stosy (swiete-oficjum): 1/727 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 27/686 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 40/509 wygranych (<8%) — gra tylko skazania |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | ⚠️ Ostrzeżenie Witalności | 0.190 | Nadmiar Wczesnych Zakończeń (Era 3-4): 26.9% gier (>25.0%) |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | ⚠️ Ostrzeżenie Witalności | 0.290 | Nadmiar Wczesnych Zakończeń (Era 3-4): 27.9% gier (>25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 21 |   0.1% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 512 |   3.2% | `██                  ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 2,340 |  14.6% | `███████             ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 3,857 |  24.1% | `████████████        ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 4,107 |  25.7% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 2,767 |  17.3% | `█████████           ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 1,614 |  10.1% | `█████               ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 498 |   3.1% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 171 |   1.1% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 63 |   0.4% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 28 |   0.2% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 13** | 13 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 14** | 9 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 21 | 5 | 16 | 0 | 0 | 0 | **CAA (16)** |
| **Era 3** | 512 | 199 | 131 | 7 | 175 | 0 | **SO (199)** |
| **Era 4** | 2,340 | 873 | 435 | 80 | 847 | 105 | **SO (873)** |
| **Era 5** | 3,857 | 1,500 | 575 | 371 | 942 | 469 | **SO (1,500)** |
| **Era 6** | 4,107 | 972 | 939 | 952 | 527 | 717 | **SO (972)** |
| **Era 7** | 2,767 | 872 | 346 | 677 | 187 | 685 | **SO (872)** |
| **Era 8** | 1,614 | 352 | 119 | 421 | 66 | 656 | **GC (656)** |
| **Era 9** | 498 | 135 | 46 | 120 | 19 | 178 | **GC (178)** |
| **Era 10** | 171 | 38 | 11 | 86 | 11 | 25 | **KB (86)** |
| **Era 11** | 63 | 3 | 5 | 44 | 0 | 11 | **KB (44)** |
| **Era 12** | 28 | 5 | 0 | 19 | 1 | 3 | **KB (19)** |
| **Era 13** | 13 | 0 | 1 | 11 | 1 | 0 | **KB (11)** |
| **Era 14** | 9 | 0 | 1 | 3 | 4 | 1 | **KT (4)** |
| **SUMA** | **16,000** | **4,954** | **2,625** | **2,791** | **2,780** | **2,850** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **6.00** |  0.1% | 14.3% | 70.0% | 15.5% |  0.1% | **KB (45.7%)** |
| `4p-no-cienie` | **5.65** |  0.0% | 18.0% | 73.9% |  8.1% |  0.0% | **KB (32.0%)** |
| `4p-no-kabala` | **5.94** |  0.2% | 12.2% | 78.3% |  9.2% |  0.1% | **KB (31.6%)** |
| `4p-no-korona` | **5.48** |  0.3% | 26.9% | 65.1% |  7.7% |  0.0% | **CAA (34.9%)** |
| `4p-no-oficjum` | **5.76** |  0.0% | 17.6% | 70.8% | 11.6% |  0.0% | **KB (35.2%)** |