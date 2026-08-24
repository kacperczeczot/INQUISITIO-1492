# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.70

**Wersja Balansu:** `v1.0-alpha.70` | **Data:** 2026-08-24 08:08 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 4.73s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🟡 ** 87.7** | 🟡 87.7 | 33.3% | - | 36.9% | - | 32.3% | 30.8% | 🟡 AKCEPTOWALNY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 50.7** | 🔴 50.7 | 33.3% | - | 21.1% | 34.2% | - | 44.7% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 ** 17.6** | 🟠 71.5 | 33.3% | - | 26.1% | 39.4% | 34.5% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 45.7** | 🔴 51.5 | 33.3% | - | - | 27.2% | 26.1% | 46.7% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 **  3.7** | 🔴 12.3 | 33.3% | 65.8% | 24.5% | - | - | 9.7% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 34.0** | 🔴 34.0 | 33.3% | 53.0% | 24.9% | - | 22.1% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 ** 51.7** | 🟠 61.9 | 33.3% | 42.3% | 24.4% | 33.3% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 **  0.1** | 🔴 4.7 | 33.3% | 78.9% | - | - | 11.1% | 10.0% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 **  3.5** | 🔴 11.7 | 33.3% | 67.6% | - | 15.6% | - | 16.8% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 ** 26.5** | 🔴 31.7 | 33.3% | 51.5% | - | 15.5% | 33.0% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟡 ** 85.0** | 🟡 85.0 | 25.0% | 21.8% | 24.8% | 28.3% | 25.1% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🔴 ** 59.0** | 🔴 59.0 | 25.0% | 34.1% | - | 17.6% | 24.7% | 23.6% | 🔴 ODCHYLONY |
| `4p-no-kabala` | 4 | 🟡 ** 86.3** | 🟡 86.3 | 25.0% | 21.6% | 26.1% | 27.3% | - | 25.0% | 🟡 AKCEPTOWALNY |
| `4p-no-korona` | 4 | 🟠 ** 65.4** | 🟡 80.7 | 25.0% | 28.3% | 27.3% | - | 23.0% | 21.4% | 🟠 WYMAGA UWAGI |
| `4p-no-oficjum` | 4 | 🔴 ** 58.9** | 🔴 58.9 | 25.0% | - | 17.1% | 22.1% | 28.0% | 32.8% | 🔴 ODCHYLONY |
| `5p-full` | 5 | 🔴 ** 20.6** | 🔴 32.6 | 20.0% | 36.3% | 19.4% | 12.7% | 18.8% | 12.8% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.1 🟢 | 0.0% 🟢 | 0.2% 🟢 | 1.13 🟢 | 6.08 🔴 | 10.11zł | 7.96 | 🟢 OPTYMALNA |
| `3p-cienie-korona-gildia` | 6.76 🟡 | 0.0% 🟢 | 5.8% 🟢 | 1.17 🟢 | 7.46 🔴 | 9.96zł | 9.13 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 6.78 🟡 | 1.4% 🟢 | 6.2% 🟢 | 1.22 🟢 | 5.97 🔴 | 8.3zł | 7.79 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.33 🟢 | 0.1% 🟢 | 6.6% 🟢 | 1.14 🟢 | 6.62 🔴 | 3.09zł | 8.5 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 5.5 🟢 | 0.0% 🟢 | 0.9% 🟢 | 1.56 🟢 | 5.93 🔴 | 11.15zł | 9.15 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 5.73 🟢 | 0.0% 🟢 | 1.2% 🟢 | 1.72 🟢 | 4.93 🟡 | 9.13zł | 8.34 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-korona` | 6.69 🟡 | 0.0% 🟢 | 5.9% 🟢 | 1.8 🟢 | 6.69 🔴 | 9.37zł | 9.1 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 4.93 🟡 | 0.0% 🟢 | 1.2% 🟢 | 1.4 🟢 | 5.29 🔴 | 4.41zł | 8.82 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 5.79 🟢 | 0.0% 🟢 | 6.9% 🟢 | 1.56 🟢 | 6.39 🔴 | 4.37zł | 9.58 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 5.83 🟢 | 0.0% 🟢 | 6.8% 🟢 | 1.6 🟢 | 5.48 🔴 | 2.56zł | 8.61 | 🟢 OPTYMALNA |
| `4p-core` | 6.02 🟢 | 0.0% 🟢 | 5.0% 🟢 | 1.75 🟢 | 6.69 🔴 | 6.96zł | 7.92 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.58 🟢 | 0.0% 🟢 | 5.6% 🟢 | 1.58 🟢 | 6.69 🔴 | 3.58zł | 8.48 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.04 🟢 | 0.0% 🟢 | 5.2% 🟢 | 1.67 🟢 | 7.31 🔴 | 8.47zł | 8.53 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.51 🟢 | 0.0% 🟢 | 0.8% 🟢 | 1.6 🟢 | 6.52 🔴 | 8.3zł | 8.25 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.76 🟢 | 0.0% 🟢 | 5.0% 🟢 | 1.04 🟢 | 6.22 🔴 | 7.06zł | 7.82 | 🟢 OPTYMALNA |
| `5p-full` | 5.21 🟢 | 0.0% 🟢 | 4.3% 🟢 | 1.44 🟢 | 6.22 🔴 | 6.56zł | 7.78 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.400 | Ekstremalny Deadlock (Era 11+): 7.0% gier (>0.5%) |
| `3p-korona-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.120 | Ekstremalny Deadlock (Era 11+): 0.6% gier (>0.5%) |
| `3p-oficjum-alandalus-gildia` | ⚠️ Ostrzeżenie Witalności | 1.210 | Nadmiar Wczesnych Zakończeń (Era 3-4): 25.1% gier (>25.0%), Martwa ścieżka stosy (swiete-oficjum): 35/658 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-alandalus-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-korona` | ⚠️ Ostrzeżenie Witalności | 0.180 | Ekstremalny Deadlock (Era 11+): 0.9% gier (>0.5%) |
| `3p-oficjum-kabala-gildia` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 4.975 | Przedwczesne Zwycięstwa (Era 1-2): 0.8% gier (>0.5%), Nadmiar Wczesnych Zakończeń (Era 3-4): 39.7% gier (>25.0%), Zbyt Krótka Średnia Rozgrywka 4.93 Er (<5.0 Er), Zbyt rzadkie Autodafé (1.40/partię < 1.40) — naruszenie ADR-0016 (~2 Autodafé na partię), Martwa ścieżka stosy (swiete-oficjum): 1/789 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 14/676 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 0.180 | Ekstremalny Deadlock (Era 11+): 0.9% gier (>0.5%) |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | ⚠️ Ostrzeżenie Witalności | 0.210 | Nadmiar Wczesnych Zakończeń (Era 3-4): 27.1% gier (>25.0%) |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | ⚠️ Ostrzeżenie Witalności | 0.460 | Nadmiar Wczesnych Zakończeń (Era 3-4): 29.6% gier (>25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 29 |   0.2% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 577 |   3.6% | `██                  ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 2,451 |  15.3% | `████████            ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 3,474 |  21.7% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 4,386 |  27.4% | `██████████████      ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 2,665 |  16.7% | `████████            ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 1,626 |  10.2% | `█████               ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 505 |   3.2% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 183 |   1.1% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 54 |   0.3% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 21 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 13** | 14 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 14** | 15 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 29 | 9 | 19 | 0 | 1 | 0 | **CAA (19)** |
| **Era 3** | 577 | 246 | 134 | 8 | 189 | 0 | **SO (246)** |
| **Era 4** | 2,451 | 1,001 | 448 | 87 | 816 | 99 | **SO (1,001)** |
| **Era 5** | 3,474 | 1,446 | 311 | 351 | 905 | 461 | **SO (1,446)** |
| **Era 6** | 4,386 | 949 | 1,283 | 899 | 572 | 683 | **CAA (1,283)** |
| **Era 7** | 2,665 | 771 | 361 | 682 | 211 | 640 | **SO (771)** |
| **Era 8** | 1,626 | 395 | 113 | 392 | 61 | 665 | **GC (665)** |
| **Era 9** | 505 | 141 | 40 | 142 | 18 | 164 | **GC (164)** |
| **Era 10** | 183 | 43 | 11 | 97 | 9 | 23 | **KB (97)** |
| **Era 11** | 54 | 7 | 3 | 39 | 0 | 5 | **KB (39)** |
| **Era 12** | 21 | 4 | 1 | 14 | 0 | 2 | **KB (14)** |
| **Era 13** | 14 | 0 | 2 | 12 | 0 | 0 | **KB (12)** |
| **Era 14** | 15 | 0 | 0 | 9 | 5 | 1 | **KB (9)** |
| **SUMA** | **16,000** | **5,012** | **2,726** | **2,732** | **2,787** | **2,743** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **6.02** |  0.2% | 13.5% | 70.2% | 16.0% |  0.1% | **CAA (40.2%)** |
| `4p-no-cienie` | **5.58** |  0.0% | 21.3% | 71.6% |  7.1% |  0.0% | **KB (30.3%)** |
| `4p-no-kabala` | **6.04** |  0.2% | 11.2% | 79.1% |  9.5% |  0.0% | **CAA (33.9%)** |
| `4p-no-korona` | **5.51** |  0.4% | 27.1% | 63.0% |  9.5% |  0.0% | **CAA (42.1%)** |
| `4p-no-oficjum` | **5.76** |  0.0% | 17.4% | 73.2% |  9.4% |  0.0% | **KB (32.0%)** |