# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.63

**Wersja Balansu:** `v1.0-alpha.63` | **Data:** 2026-08-24 07:01 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 4.94s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🟡 ** 77.3** | 🟡 77.3 | 33.3% | - | 37.1% | - | 27.1% | 35.8% | 🟡 AKCEPTOWALNY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 42.1** | 🔴 42.1 | 33.3% | - | 20.9% | 30.1% | - | 49.0% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 ** 20.4** | 🟠 67.8 | 33.3% | - | 24.7% | 38.7% | 36.6% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 45.6** | 🔴 51.4 | 33.3% | - | - | 31.4% | 22.8% | 45.8% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 **  6.1** | 🔴 23.6 | 33.3% | 56.5% | 29.8% | - | - | 13.7% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 34.4** | 🔴 34.4 | 33.3% | 52.9% | 23.5% | - | 23.6% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🟠 ** 63.7** | 🟠 63.7 | 33.3% | 42.2% | 25.2% | 32.6% | - | - | 🟠 WYMAGA UWAGI |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 **  0.1** | 🔴 3.5 | 33.3% | 82.2% | - | - | 11.3% | 6.5% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 **  0.4** | 🔴 8.7 | 33.3% | 71.3% | - | 15.6% | - | 13.1% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 ** 10.2** | 🔴 33.9 | 33.3% | 49.6% | - | 15.4% | 35.0% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟡 ** 79.2** | 🟡 79.2 | 25.0% | 21.5% | 23.2% | 29.7% | 25.6% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🔴 **  6.5** | 🔴 48.3 | 25.0% | 36.6% | - | 19.7% | 26.9% | 16.8% | 🔴 ODCHYLONY |
| `4p-no-kabala` | 4 | 🟠 ** 71.6** | 🟠 71.6 | 25.0% | 18.0% | 26.4% | 27.3% | - | 28.3% | 🟠 WYMAGA UWAGI |
| `4p-no-korona` | 4 | 🟢 ** 92.4** | 🟢 92.4 | 25.0% | 26.7% | 24.5% | - | 25.6% | 23.2% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🔴 ** 58.5** | 🔴 58.5 | 25.0% | - | 16.9% | 24.7% | 24.6% | 33.8% | 🔴 ODCHYLONY |
| `5p-full` | 5 | 🔴 **  2.4** | 🔴 34.4 | 20.0% | 35.3% | 17.8% | 15.6% | 20.6% | 10.7% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.22 🟢 | 0.0% 🟢 | 0.2% 🟢 | 1.16 🟢 | 6.61 🔴 | 9.8zł | 8.15 | 🟢 OPTYMALNA |
| `3p-cienie-korona-gildia` | 6.83 🟡 | 0.0% 🟢 | 6.2% 🟢 | 1.2 🟢 | 7.96 🔴 | 9.54zł | 9.31 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 6.73 🟡 | 0.6% 🟢 | 6.4% 🟢 | 1.22 🟢 | 6.26 🔴 | 8.18zł | 7.91 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.41 🟢 | 0.0% 🟢 | 7.0% 🟢 | 1.12 🟢 | 6.91 🔴 | 2.88zł | 8.69 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 5.93 🟢 | 0.0% 🟢 | 2.3% 🟢 | 1.56 🟢 | 6.83 🔴 | 10.59zł | 9.32 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 5.8 🟢 | 0.0% 🟢 | 2.0% 🟢 | 1.65 🟢 | 5.39 🔴 | 8.6zł | 8.45 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-korona` | 6.48 🟢 | 0.0% 🟢 | 7.0% 🟢 | 1.6 🟢 | 6.8 🔴 | 8.57zł | 9.19 | 🟢 OPTYMALNA |
| `3p-oficjum-kabala-gildia` | 4.89 🟡 | 0.0% 🟢 | 2.7% 🟢 | 1.38 🟢 | 5.29 🔴 | 3.6zł | 8.91 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 5.77 🟢 | 0.0% 🟢 | 8.4% 🟢 | 1.4 🟢 | 6.61 🔴 | 3.57zł | 9.73 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 5.69 🟢 | 0.0% 🟢 | 8.6% 🟢 | 1.53 🟢 | 5.21 🔴 | 2.19zł | 8.67 | 🟢 OPTYMALNA |
| `4p-core` | 6.07 🟢 | 0.0% 🟢 | 6.0% 🟢 | 1.54 🟢 | 6.91 🔴 | 6.78zł | 8.01 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.57 🟢 | 0.0% 🟢 | 7.1% 🟢 | 1.4 🟢 | 6.81 🔴 | 3.05zł | 8.64 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.12 🟢 | 0.0% 🟢 | 6.7% 🟢 | 1.44 🟢 | 7.82 🔴 | 7.92zł | 8.68 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.68 🟢 | 0.0% 🟢 | 1.8% 🟢 | 1.53 🟢 | 6.99 🔴 | 7.86zł | 8.31 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.82 🟢 | 0.0% 🟢 | 5.0% 🟢 | 1.07 🟢 | 6.7 🔴 | 6.95zł | 8.08 | 🟢 OPTYMALNA |
| `5p-full` | 5.14 🟢 | 0.0% 🟢 | 5.2% 🟢 | 1.27 🟢 | 6.16 🔴 | 6.1zł | 7.8 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.200 | Ekstremalny Deadlock (Era 11+): 6.0% gier (>0.5%) |
| `3p-korona-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.120 | Ekstremalny Deadlock (Era 11+): 0.6% gier (>0.5%) |
| `3p-oficjum-alandalus-gildia` | ⚠️ Ostrzeżenie Witalności | 1.350 | Przedwczesne Zwycięstwa (Era 1-2): 0.6% gier (>0.5%), Martwa ścieżka stosy (swiete-oficjum): 42/565 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-alandalus-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-kabala-gildia` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 4.664 | Przedwczesne Zwycięstwa (Era 1-2): 0.9% gier (>0.5%), Nadmiar Wczesnych Zakończeń (Era 3-4): 35.8% gier (>25.0%), Zbyt Krótka Średnia Rozgrywka 4.89 Er (<5.0 Er), Zbyt rzadkie Autodafé (1.38/partię < 1.40) — naruszenie ADR-0016 (~2 Autodafé na partię), Martwa ścieżka stosy (swiete-oficjum): 0/822 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-gildia` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 3.200 | Zbyt rzadkie Autodafé (1.40/partię < 1.40) — naruszenie ADR-0016 (~2 Autodafé na partię), Martwa ścieżka stosy (swiete-oficjum): 10/713 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 29/496 wygranych (<8%) — gra tylko skazania |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.000 | Zbyt rzadkie Autodafé (1.40/partię < 1.40) — naruszenie ADR-0016 (~2 Autodafé na partię) |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.680 | Nadmiar Wczesnych Zakończeń (Era 3-4): 31.8% gier (>25.0%), Zbyt rzadkie Autodafé (1.27/partię < 1.40) — naruszenie ADR-0016 (~2 Autodafé na partię) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 29 |   0.2% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 479 |   3.0% | `█                   ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 2,345 |  14.7% | `███████             ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 3,626 |  22.7% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 4,280 |  26.8% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 2,660 |  16.6% | `████████            ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 1,791 |  11.2% | `██████              ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 522 |   3.3% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 176 |   1.1% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 56 |   0.4% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 20 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 13** | 10 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 14** | 6 |   0.0% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 29 | 14 | 15 | 0 | 0 | 0 | **CAA (15)** |
| **Era 3** | 479 | 183 | 118 | 9 | 169 | 0 | **SO (183)** |
| **Era 4** | 2,345 | 868 | 471 | 80 | 838 | 88 | **SO (868)** |
| **Era 5** | 3,626 | 1,532 | 293 | 431 | 937 | 433 | **SO (1,532)** |
| **Era 6** | 4,280 | 1,000 | 1,100 | 1,011 | 564 | 605 | **CAA (1,100)** |
| **Era 7** | 2,660 | 737 | 416 | 671 | 181 | 655 | **SO (737)** |
| **Era 8** | 1,791 | 410 | 222 | 334 | 56 | 769 | **GC (769)** |
| **Era 9** | 522 | 132 | 49 | 123 | 42 | 176 | **GC (176)** |
| **Era 10** | 176 | 43 | 10 | 81 | 8 | 34 | **KB (81)** |
| **Era 11** | 56 | 6 | 4 | 39 | 1 | 6 | **KB (39)** |
| **Era 12** | 20 | 1 | 1 | 17 | 0 | 1 | **KB (17)** |
| **Era 13** | 10 | 2 | 0 | 8 | 0 | 0 | **KB (8)** |
| **Era 14** | 6 | 0 | 1 | 4 | 1 | 0 | **KB (4)** |
| **SUMA** | **16,000** | **4,928** | **2,700** | **2,808** | **2,797** | **2,767** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **6.07** |  0.1% | 13.3% | 68.9% | 17.4% |  0.3% | **KB (41.4%)** |
| `4p-no-cienie` | **5.57** |  0.1% | 18.9% | 74.5% |  6.5% |  0.0% | **KB (34.2%)** |
| `4p-no-kabala` | **6.12** |  0.0% | 10.1% | 76.1% | 13.8% |  0.0% | **KB (37.7%)** |
| `4p-no-korona` | **5.68** |  0.3% | 23.5% | 64.3% | 11.9% |  0.0% | **CAA (33.0%)** |
| `4p-no-oficjum` | **5.82** |  0.1% | 16.2% | 72.0% | 11.7% |  0.0% | **KB (36.4%)** |