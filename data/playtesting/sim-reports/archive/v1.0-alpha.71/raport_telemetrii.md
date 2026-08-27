# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.71

**Wersja Balansu:** `v1.0-alpha.71` | **Data:** 2026-08-24 08:25 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 4.8s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🟠 ** 71.8** | 🟢 91.3 | 33.3% | - | 34.9% | - | 30.6% | 34.5% | 🟠 WYMAGA UWAGI |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 54.0** | 🔴 54.0 | 33.3% | - | 24.1% | 30.5% | - | 45.4% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 ** 18.8** | 🟠 64.9 | 33.3% | - | 24.7% | 41.1% | 34.2% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 45.7** | 🔴 51.5 | 33.3% | - | - | 27.2% | 26.1% | 46.7% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 **  5.1** | 🔴 20.1 | 33.3% | 59.6% | 26.1% | - | - | 14.3% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 34.7** | 🔴 34.7 | 33.3% | 52.8% | 23.5% | - | 23.7% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 ** 46.7** | 🔴 58.1 | 33.3% | 41.0% | 22.2% | 36.8% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 **  0.1** | 🔴 5.4 | 33.3% | 77.2% | - | - | 12.5% | 10.3% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 **  4.2** | 🔴 13.8 | 33.3% | 65.4% | - | 16.4% | - | 18.2% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 ** 38.8** | 🔴 38.8 | 33.3% | 48.0% | - | 17.3% | 34.7% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟡 ** 86.2** | 🟡 86.2 | 25.0% | 21.8% | 26.1% | 27.6% | 24.5% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🔴 ** 56.5** | 🔴 56.5 | 25.0% | 35.0% | - | 18.2% | 25.3% | 21.5% | 🔴 ODCHYLONY |
| `4p-no-kabala` | 4 | 🟡 ** 81.4** | 🟡 81.4 | 25.0% | 22.0% | 22.7% | 28.8% | - | 26.5% | 🟡 AKCEPTOWALNY |
| `4p-no-korona` | 4 | 🟠 ** 69.4** | 🟠 73.7 | 25.0% | 29.5% | 27.4% | - | 23.6% | 19.5% | 🟠 WYMAGA UWAGI |
| `4p-no-oficjum` | 4 | 🔴 ** 57.7** | 🔴 57.7 | 25.0% | - | 17.2% | 23.5% | 25.0% | 34.3% | 🔴 ODCHYLONY |
| `5p-full` | 5 | 🔴 ** 22.1** | 🔴 30.7 | 20.0% | 36.8% | 20.7% | 12.6% | 17.9% | 12.0% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.2 🟢 | 0.0% 🟢 | 0.2% 🟢 | 1.16 🟢 | 6.45 🔴 | 10.36zł | 8.01 | 🟢 OPTYMALNA |
| `3p-cienie-korona-gildia` | 6.73 🟡 | 0.0% 🟢 | 5.9% 🟢 | 1.19 🟢 | 7.56 🔴 | 10.15zł | 9.16 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 6.84 🟡 | 0.9% 🟢 | 6.1% 🟢 | 1.24 🟢 | 6.33 🔴 | 8.42zł | 7.92 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.33 🟢 | 0.1% 🟢 | 6.6% 🟢 | 1.14 🟢 | 6.62 🔴 | 3.09zł | 8.5 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 5.63 🟢 | 0.0% 🟢 | 1.1% 🟢 | 1.55 🟢 | 6.16 🔴 | 11.42zł | 9.14 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 5.81 🟢 | 0.0% 🟢 | 1.3% 🟢 | 1.7 🟢 | 5.2 🔴 | 9.19zł | 8.38 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-korona` | 6.76 🟡 | 0.0% 🟢 | 6.1% 🟢 | 1.78 🟢 | 6.96 🔴 | 9.61zł | 9.11 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 5.01 🟢 | 0.0% 🟢 | 1.3% 🟢 | 1.4 🟢 | 5.34 🔴 | 4.42zł | 8.78 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-gildia` | 5.87 🟢 | 0.0% 🟢 | 7.2% 🟢 | 1.56 🟢 | 6.4 🔴 | 4.39zł | 9.55 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 5.87 🟢 | 0.0% 🟢 | 6.8% 🟢 | 1.62 🟢 | 5.43 🔴 | 2.53zł | 8.53 | 🟢 OPTYMALNA |
| `4p-core` | 6.05 🟢 | 0.0% 🟢 | 5.0% 🟢 | 1.73 🟢 | 6.79 🔴 | 7.11zł | 7.91 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.61 🟢 | 0.0% 🟢 | 5.7% 🟢 | 1.57 🟢 | 6.55 🔴 | 3.63zł | 8.4 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.1 🟢 | 0.0% 🟢 | 5.2% 🟢 | 1.62 🟢 | 7.51 🔴 | 8.63zł | 8.53 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.57 🟢 | 0.0% 🟢 | 0.9% 🟢 | 1.63 🟢 | 6.74 🔴 | 8.4zł | 8.24 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.79 🟢 | 0.0% 🟢 | 4.9% 🟢 | 1.07 🟢 | 6.43 🔴 | 7.06zł | 7.89 | 🟢 OPTYMALNA |
| `5p-full` | 5.22 🟢 | 0.0% 🟢 | 4.3% 🟢 | 1.42 🟢 | 6.27 🔴 | 6.58zł | 7.7 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.240 | Ekstremalny Deadlock (Era 11+): 1.2% gier (>0.5%) |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.240 | Ekstremalny Deadlock (Era 11+): 6.2% gier (>0.5%) |
| `3p-korona-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.120 | Ekstremalny Deadlock (Era 11+): 0.6% gier (>0.5%) |
| `3p-oficjum-alandalus-gildia` | ⚠️ Ostrzeżenie Witalności | 1.375 | Przedwczesne Zwycięstwa (Era 1-2): 0.7% gier (>0.5%), Martwa ścieżka stosy (swiete-oficjum): 31/596 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-alandalus-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-korona` | ⚠️ Ostrzeżenie Witalności | 0.220 | Ekstremalny Deadlock (Era 11+): 1.1% gier (>0.5%) |
| `3p-oficjum-kabala-gildia` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 4.580 | Przedwczesne Zwycięstwa (Era 1-2): 0.6% gier (>0.5%), Nadmiar Wczesnych Zakończeń (Era 3-4): 37.3% gier (>25.0%), Zbyt rzadkie Autodafé (1.40/partię < 1.40) — naruszenie ADR-0016 (~2 Autodafé na partię), Martwa ścieżka stosy (swiete-oficjum): 1/772 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 18/654 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | ⚠️ Ostrzeżenie Witalności | 0.060 | Nadmiar Wczesnych Zakończeń (Era 3-4): 25.6% gier (>25.0%) |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | ⚠️ Ostrzeżenie Witalności | 0.330 | Nadmiar Wczesnych Zakończeń (Era 3-4): 28.3% gier (>25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 23 |   0.1% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 564 |   3.5% | `██                  ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 2,326 |  14.5% | `███████             ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 3,403 |  21.3% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 4,357 |  27.2% | `██████████████      ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 2,762 |  17.3% | `█████████           ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 1,716 |  10.7% | `█████               ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 553 |   3.5% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 192 |   1.2% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 59 |   0.4% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 22 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 13** | 13 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 14** | 10 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 23 | 8 | 14 | 0 | 1 | 0 | **CAA (14)** |
| **Era 3** | 564 | 235 | 129 | 10 | 190 | 0 | **SO (235)** |
| **Era 4** | 2,326 | 909 | 436 | 83 | 791 | 107 | **SO (909)** |
| **Era 5** | 3,403 | 1,370 | 323 | 354 | 870 | 486 | **SO (1,370)** |
| **Era 6** | 4,357 | 1,013 | 1,140 | 948 | 594 | 662 | **CAA (1,140)** |
| **Era 7** | 2,762 | 779 | 412 | 684 | 227 | 660 | **SO (779)** |
| **Era 8** | 1,716 | 379 | 176 | 407 | 59 | 695 | **GC (695)** |
| **Era 9** | 553 | 136 | 43 | 163 | 29 | 182 | **GC (182)** |
| **Era 10** | 192 | 52 | 18 | 88 | 9 | 25 | **KB (88)** |
| **Era 11** | 59 | 4 | 2 | 39 | 5 | 9 | **KB (39)** |
| **Era 12** | 22 | 5 | 2 | 8 | 2 | 5 | **KB (8)** |
| **Era 13** | 13 | 1 | 1 | 10 | 1 | 0 | **KB (10)** |
| **Era 14** | 10 | 0 | 0 | 6 | 3 | 1 | **KB (6)** |
| **SUMA** | **16,000** | **4,891** | **2,696** | **2,800** | **2,781** | **2,832** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **6.05** |  0.3% | 12.9% | 70.1% | 16.6% |  0.1% | **KB (36.1%)** |
| `4p-no-cienie` | **5.61** |  0.0% | 20.8% | 71.1% |  8.1% |  0.0% | **KB (28.8%)** |
| `4p-no-kabala` | **6.10** |  0.0% |  9.3% | 79.9% | 10.8% |  0.0% | **KB (35.9%)** |
| `4p-no-korona` | **5.57** |  0.2% | 25.6% | 64.8% |  9.4% |  0.0% | **CAA (36.9%)** |
| `4p-no-oficjum` | **5.79** |  0.0% | 17.5% | 71.4% | 11.1% |  0.0% | **KB (36.9%)** |