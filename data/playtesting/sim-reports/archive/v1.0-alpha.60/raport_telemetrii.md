# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.60

**Wersja Balansu:** `v1.0-alpha.60` | **Data:** 2026-08-23 22:43 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 4.77s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🟡 ** 85.5** | 🟡 85.5 | 33.3% | - | 34.7% | - | 29.2% | 36.1% | 🟡 AKCEPTOWALNY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 40.3** | 🔴 40.3 | 33.3% | - | 18.7% | 32.8% | - | 48.5% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 ** 16.6** | 🔴 57.3 | 33.3% | - | 21.7% | 39.6% | 38.7% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 45.6** | 🔴 51.4 | 33.3% | - | - | 31.4% | 22.8% | 45.8% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 **  3.8** | 🔴 12.7 | 33.3% | 66.2% | 20.8% | - | - | 13.0% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 **  3.0** | 🔴 19.1 | 33.3% | 61.0% | 16.8% | - | 22.2% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 **  9.3** | 🔴 34.6 | 33.3% | 51.0% | 17.4% | 31.6% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 **  0.3** | 🔴 3.1 | 33.3% | 83.7% | - | - | 11.0% | 5.3% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 **  1.8** | 🔴 5.9 | 33.3% | 76.1% | - | 12.7% | - | 11.2% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 **  7.7** | 🔴 25.6 | 33.3% | 54.4% | - | 13.2% | 32.4% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🔴 ** 59.2** | 🔴 59.2 | 25.0% | 23.9% | 16.3% | 32.5% | 27.3% | - | 🔴 ODCHYLONY |
| `4p-no-cienie` | 4 | 🔴 ** 39.5** | 🔴 39.5 | 25.0% | 38.6% | - | 15.1% | 28.4% | 17.9% | 🔴 ODCHYLONY |
| `4p-no-kabala` | 4 | 🟠 ** 67.1** | 🟠 67.1 | 25.0% | 21.8% | 19.5% | 31.7% | - | 27.0% | 🟠 WYMAGA UWAGI |
| `4p-no-korona` | 4 | 🔴 ** 47.8** | 🟠 63.9 | 25.0% | 33.2% | 20.5% | - | 25.7% | 20.6% | 🔴 ODCHYLONY |
| `4p-no-oficjum` | 4 | 🔴 ** 58.4** | 🔴 58.4 | 25.0% | - | 16.2% | 24.6% | 26.1% | 33.1% | 🔴 ODCHYLONY |
| `5p-full` | 5 | 🔴 **  7.3** | 🔴 19.5 | 20.0% | 42.7% | 13.6% | 16.3% | 17.8% | 9.6% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.22 🟢 | 0.0% 🟢 | 0.2% 🟢 | 1.18 🟢 | 6.28 🔴 | 9.75zł | 8.06 | 🟢 OPTYMALNA |
| `3p-cienie-korona-gildia` | 6.82 🟡 | 0.0% 🟢 | 6.3% 🟢 | 1.21 🟢 | 7.69 🔴 | 9.35zł | 9.22 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 6.78 🟡 | 1.1% 🟢 | 6.5% 🟢 | 1.23 🟢 | 5.92 🔴 | 8.16zł | 7.75 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.41 🟢 | 0.0% 🟢 | 7.0% 🟢 | 1.12 🟢 | 6.91 🔴 | 2.88zł | 8.69 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 5.61 🟢 | 0.0% 🟢 | 2.5% 🟢 | 1.34 🟢 | 5.99 🔴 | 9.72zł | 9.16 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 5.53 🟢 | 0.0% 🟢 | 2.0% 🟢 | 1.43 🟢 | 4.51 🟡 | 8.11zł | 8.13 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-korona` | 6.5 🟢 | 0.0% 🟢 | 7.3% 🟢 | 1.49 🟢 | 6.42 🔴 | 7.99zł | 9.11 | 🟢 OPTYMALNA |
| `3p-oficjum-kabala-gildia` | 4.95 🟡 | 0.0% 🟢 | 2.9% 🟢 | 1.26 🟢 | 5.17 🔴 | 3.41zł | 8.72 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 5.66 🟢 | 0.0% 🟢 | 9.4% 🟢 | 1.24 🟢 | 6.33 🔴 | 3.28zł | 9.65 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 5.65 🟢 | 0.0% 🟢 | 9.4% 🟢 | 1.38 🟢 | 5.06 🔴 | 1.97zł | 8.63 | 🟢 OPTYMALNA |
| `4p-core` | 6.09 🟢 | 0.0% 🟢 | 6.5% 🟢 | 1.53 🟢 | 6.55 🔴 | 6.33zł | 7.91 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.56 🟢 | 0.0% 🟢 | 7.8% 🟢 | 1.37 🟢 | 6.61 🔴 | 2.88zł | 8.59 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.08 🟢 | 0.0% 🟢 | 6.7% 🟢 | 1.33 🟢 | 7.47 🔴 | 7.39zł | 8.69 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.65 🟢 | 0.0% 🟢 | 2.0% 🟢 | 1.5 🟢 | 6.6 🔴 | 7.51zł | 8.2 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.78 🟢 | 0.0% 🟢 | 5.1% 🟢 | 1.08 🟢 | 6.3 🔴 | 6.9zł | 7.94 | 🟢 OPTYMALNA |
| `5p-full` | 5.1 🟢 | 0.0% 🟢 | 5.1% 🟢 | 1.33 🟢 | 5.92 🔴 | 5.76zł | 7.73 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.240 | Ekstremalny Deadlock (Era 11+): 6.2% gier (>0.5%) |
| `3p-korona-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.120 | Ekstremalny Deadlock (Era 11+): 0.6% gier (>0.5%) |
| `3p-oficjum-alandalus-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 30/662 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-alandalus-kabala` | ⚠️ Ostrzeżenie Witalności | 1.840 | Nadmiar Wczesnych Zakończeń (Era 3-4): 31.4% gier (>25.0%), Martwa ścieżka stosy (swiete-oficjum): 45/610 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-alandalus-korona` | ⚠️ Ostrzeżenie Witalności | 1.320 | Ekstremalny Deadlock (Era 11+): 0.6% gier (>0.5%), Martwa ścieżka stosy (swiete-oficjum): 24/510 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-kabala-gildia` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.242 | Nadmiar Wczesnych Zakończeń (Era 3-4): 34.6% gier (>25.0%), Zbyt Krótka Średnia Rozgrywka 4.95 Er (<5.0 Er), Martwa ścieżka stosy (swiete-oficjum): 1/837 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 8/761 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 15/544 wygranych (<8%) — gra tylko skazania |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | ⚠️ Ostrzeżenie Witalności | 0.290 | Nadmiar Wczesnych Zakończeń (Era 3-4): 27.9% gier (>25.0%) |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | ⚠️ Ostrzeżenie Witalności | 0.980 | Nadmiar Wczesnych Zakończeń (Era 3-4): 34.8% gier (>25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 24 |   0.1% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 515 |   3.2% | `██                  ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 2,683 |  16.8% | `████████            ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 3,733 |  23.3% | `████████████        ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 3,798 |  23.7% | `████████████        ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 2,650 |  16.6% | `████████            ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 1,776 |  11.1% | `██████              ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 535 |   3.3% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 197 |   1.2% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 44 |   0.3% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 22 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 13** | 12 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 14** | 11 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 24 | 9 | 15 | 0 | 0 | 0 | **CAA (15)** |
| **Era 3** | 515 | 208 | 118 | 7 | 182 | 0 | **SO (208)** |
| **Era 4** | 2,683 | 1,175 | 483 | 80 | 871 | 74 | **SO (1,175)** |
| **Era 5** | 3,733 | 1,799 | 275 | 383 | 886 | 390 | **SO (1,799)** |
| **Era 6** | 3,798 | 999 | 710 | 981 | 549 | 559 | **SO (999)** |
| **Era 7** | 2,650 | 745 | 342 | 690 | 204 | 669 | **SO (745)** |
| **Era 8** | 1,776 | 384 | 163 | 394 | 67 | 768 | **GC (768)** |
| **Era 9** | 535 | 155 | 38 | 127 | 37 | 178 | **GC (178)** |
| **Era 10** | 197 | 46 | 8 | 102 | 6 | 35 | **KB (102)** |
| **Era 11** | 44 | 3 | 7 | 25 | 4 | 5 | **KB (25)** |
| **Era 12** | 22 | 3 | 1 | 14 | 1 | 3 | **KB (14)** |
| **Era 13** | 12 | 0 | 2 | 9 | 1 | 0 | **KB (9)** |
| **Era 14** | 11 | 0 | 0 | 3 | 8 | 0 | **KT (8)** |
| **SUMA** | **16,000** | **5,526** | **2,162** | **2,815** | **2,816** | **2,681** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **6.09** |  0.2% | 14.5% | 65.7% | 19.3% |  0.3% | **KB (47.9%)** |
| `4p-no-cienie` | **5.56** |  0.0% | 20.2% | 72.4% |  7.4% |  0.0% | **KB (29.2%)** |
| `4p-no-kabala` | **6.08** |  0.0% | 11.4% | 76.9% | 11.7% |  0.0% | **KB (44.5%)** |
| `4p-no-korona` | **5.65** |  0.2% | 27.9% | 58.0% | 13.9% |  0.0% | **KT (30.1%)** |
| `4p-no-oficjum` | **5.78** |  0.2% | 18.7% | 69.1% | 12.0% |  0.0% | **KB (41.5%)** |