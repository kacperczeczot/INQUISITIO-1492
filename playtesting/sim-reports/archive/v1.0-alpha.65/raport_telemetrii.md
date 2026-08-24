# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.65

**Wersja Balansu:** `v1.0-alpha.65` | **Data:** 2026-08-24 07:16 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 4.6s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🟠 ** 71.0** | 🟡 86.7 | 33.3% | - | 34.6% | - | 29.5% | 35.9% | 🟠 WYMAGA UWAGI |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 48.0** | 🔴 48.0 | 33.3% | - | 22.1% | 31.0% | - | 46.9% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 ** 16.2** | 🟠 60.8 | 33.3% | - | 23.9% | 42.3% | 33.8% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 46.6** | 🔴 46.6 | 33.3% | - | - | 26.3% | 25.4% | 48.3% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 ** 17.0** | 🔴 19.7 | 33.3% | 59.9% | 25.8% | - | - | 14.3% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 18.0** | 🔴 22.0 | 33.3% | 59.1% | 17.9% | - | 23.0% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🟠 ** 62.8** | 🟠 62.8 | 33.3% | 40.2% | 23.5% | 36.3% | - | - | 🟠 WYMAGA UWAGI |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 **  0.1** | 🔴 4.0 | 33.3% | 80.5% | - | - | 12.6% | 6.9% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 **  0.3** | 🔴 6.7 | 33.3% | 74.4% | - | 10.7% | - | 14.9% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 **  8.8** | 🔴 29.3 | 33.3% | 52.2% | - | 14.3% | 33.5% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟠 ** 73.7** | 🟠 73.7 | 25.0% | 22.0% | 21.2% | 30.8% | 26.0% | - | 🟠 WYMAGA UWAGI |
| `4p-no-cienie` | 4 | 🔴 **  7.4** | 🔴 55.0 | 25.0% | 33.4% | - | 19.3% | 29.3% | 18.0% | 🔴 ODCHYLONY |
| `4p-no-kabala` | 4 | 🔴 **  9.9** | 🟠 72.9 | 25.0% | 18.6% | 25.0% | 27.8% | - | 28.6% | 🔴 ODCHYLONY |
| `4p-no-korona` | 4 | 🟢 ** 91.4** | 🟢 91.4 | 25.0% | 25.9% | 22.6% | - | 26.3% | 25.2% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🔴 ** 53.8** | 🔴 53.8 | 25.0% | - | 16.6% | 22.9% | 25.2% | 35.3% | 🔴 ODCHYLONY |
| `5p-full` | 5 | 🔴 **  2.2** | 🔴 33.3 | 20.0% | 36.2% | 17.5% | 13.5% | 19.9% | 12.9% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.11 🟢 | 0.0% 🟢 | 0.2% 🟢 | 1.18 🟢 | 6.39 🔴 | 9.91zł | 8.0 | 🟢 OPTYMALNA |
| `3p-cienie-korona-gildia` | 6.7 🟡 | 0.0% 🟢 | 6.4% 🟢 | 1.19 🟢 | 7.61 🔴 | 9.9zł | 9.18 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 6.8 🟡 | 0.7% 🟢 | 6.5% 🟢 | 1.25 🟢 | 6.38 🔴 | 8.25zł | 7.99 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.26 🟢 | 0.0% 🟢 | 7.3% 🟢 | 1.13 🟢 | 6.7 🔴 | 3.13zł | 8.61 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 5.83 🟢 | 0.0% 🟢 | 2.2% 🟢 | 1.57 🟢 | 6.6 🔴 | 10.92zł | 9.31 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 5.64 🟢 | 0.0% 🟢 | 1.9% 🟢 | 1.66 🟢 | 5.17 🔴 | 8.52zł | 8.53 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-korona` | 6.5 🟢 | 0.0% 🟢 | 6.9% 🟢 | 1.62 🟢 | 6.8 🔴 | 8.65zł | 9.14 | 🟢 OPTYMALNA |
| `3p-oficjum-kabala-gildia` | 4.87 🟡 | 0.0% 🟢 | 2.6% 🟢 | 1.39 🟢 | 5.06 🔴 | 3.84zł | 8.82 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 5.69 🟢 | 0.0% 🟢 | 8.4% 🟢 | 1.38 🟢 | 6.32 🔴 | 3.81zł | 9.72 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 5.66 🟢 | 0.0% 🟢 | 8.6% 🟢 | 1.53 🟢 | 5.19 🔴 | 2.19zł | 8.72 | 🟢 OPTYMALNA |
| `4p-core` | 5.91 🟢 | 0.0% 🟢 | 6.2% 🟢 | 1.52 🟢 | 6.6 🔴 | 6.69zł | 7.94 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.51 🟢 | 0.0% 🟢 | 7.2% 🟢 | 1.39 🟢 | 6.42 🔴 | 3.21zł | 8.54 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.99 🟢 | 0.0% 🟢 | 6.5% 🟢 | 1.39 🟢 | 7.49 🔴 | 8.11zł | 8.67 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.61 🟢 | 0.0% 🟢 | 1.8% 🟢 | 1.54 🟢 | 6.89 🔴 | 7.99zł | 8.29 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.77 🟢 | 0.0% 🟢 | 5.1% 🟢 | 1.05 🟢 | 6.54 🔴 | 7.12zł | 7.96 | 🟢 OPTYMALNA |
| `5p-full` | 5.15 🟢 | 0.0% 🟢 | 5.4% 🟢 | 1.29 🟢 | 6.16 🔴 | 6.19zł | 7.81 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.200 | Ekstremalny Deadlock (Era 11+): 1.0% gier (>0.5%) |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.320 | Ekstremalny Deadlock (Era 11+): 6.6% gier (>0.5%) |
| `3p-korona-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-gildia` | ⚠️ Ostrzeżenie Witalności | 0.150 | Przedwczesne Zwycięstwa (Era 1-2): 0.6% gier (>0.5%) |
| `3p-oficjum-alandalus-kabala` | ⚠️ Ostrzeżenie Witalności | 0.200 | Nadmiar Wczesnych Zakończeń (Era 3-4): 27.0% gier (>25.0%) |
| `3p-oficjum-alandalus-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-kabala-gildia` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 5.144 | Przedwczesne Zwycięstwa (Era 1-2): 1.1% gier (>0.5%), Nadmiar Wczesnych Zakończeń (Era 3-4): 39.8% gier (>25.0%), Zbyt Krótka Średnia Rozgrywka 4.87 Er (<5.0 Er), Zbyt rzadkie Autodafé (1.39/partię < 1.40) — naruszenie ADR-0016 (~2 Autodafé na partię), Martwa ścieżka stosy (swiete-oficjum): 2/805 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-gildia` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 3.200 | Zbyt rzadkie Autodafé (1.38/partię < 1.40) — naruszenie ADR-0016 (~2 Autodafé na partię), Martwa ścieżka stosy (swiete-oficjum): 5/744 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 26/522 wygranych (<8%) — gra tylko skazania |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.000 | Zbyt rzadkie Autodafé (1.39/partię < 1.40) — naruszenie ADR-0016 (~2 Autodafé na partię) |
| `4p-no-kabala` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.000 | Zbyt rzadkie Autodafé (1.39/partię < 1.40) — naruszenie ADR-0016 (~2 Autodafé na partię) |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.720 | Nadmiar Wczesnych Zakończeń (Era 3-4): 32.2% gier (>25.0%), Zbyt rzadkie Autodafé (1.29/partię < 1.40) — naruszenie ADR-0016 (~2 Autodafé na partię) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 28 |   0.2% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 562 |   3.5% | `██                  ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 2,505 |  15.7% | `████████            ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 3,638 |  22.7% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 4,265 |  26.7% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 2,634 |  16.5% | `████████            ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 1,688 |  10.5% | `█████               ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 417 |   2.6% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 171 |   1.1% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 58 |   0.4% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 12 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 13** | 15 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 14** | 7 |   0.0% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 28 | 15 | 12 | 0 | 1 | 0 | **SO (15)** |
| **Era 3** | 562 | 211 | 138 | 11 | 202 | 0 | **SO (211)** |
| **Era 4** | 2,505 | 1,032 | 463 | 60 | 835 | 115 | **SO (1,032)** |
| **Era 5** | 3,638 | 1,504 | 284 | 418 | 954 | 478 | **SO (1,504)** |
| **Era 6** | 4,265 | 964 | 1,022 | 1,049 | 564 | 666 | **KB (1,049)** |
| **Era 7** | 2,634 | 752 | 338 | 634 | 190 | 720 | **SO (752)** |
| **Era 8** | 1,688 | 405 | 200 | 308 | 57 | 718 | **GC (718)** |
| **Era 9** | 417 | 104 | 39 | 120 | 29 | 125 | **GC (125)** |
| **Era 10** | 171 | 34 | 7 | 87 | 8 | 35 | **KB (87)** |
| **Era 11** | 58 | 3 | 4 | 35 | 1 | 15 | **KB (35)** |
| **Era 12** | 12 | 0 | 0 | 12 | 0 | 0 | **KB (12)** |
| **Era 13** | 15 | 0 | 0 | 14 | 1 | 0 | **KB (14)** |
| **Era 14** | 7 | 0 | 0 | 4 | 3 | 0 | **KB (4)** |
| **SUMA** | **16,000** | **5,024** | **2,507** | **2,752** | **2,845** | **2,872** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **5.91** |  0.3% | 17.0% | 66.6% | 16.1% |  0.0% | **KB (42.7%)** |
| `4p-no-cienie` | **5.51** |  0.0% | 19.5% | 74.2% |  6.3% |  0.0% | **KB (36.2%)** |
| `4p-no-kabala` | **5.99** |  0.0% | 12.1% | 77.3% | 10.6% |  0.0% | **KB (39.7%)** |
| `4p-no-korona` | **5.61** |  0.4% | 24.1% | 66.2% |  9.3% |  0.0% | **CAA (31.1%)** |
| `4p-no-oficjum` | **5.77** |  0.0% | 17.7% | 73.3% |  9.0% |  0.0% | **KB (33.9%)** |