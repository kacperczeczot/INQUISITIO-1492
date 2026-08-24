# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.67

**Wersja Balansu:** `v1.0-alpha.67` | **Data:** 2026-08-24 07:26 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 4.8s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🟠 ** 74.2** | 🟡 85.3 | 33.3% | - | 37.3% | - | 30.0% | 32.7% | 🟠 WYMAGA UWAGI |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 46.7** | 🔴 46.7 | 33.3% | - | 23.2% | 28.9% | - | 47.9% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 ** 19.5** | 🟠 70.0 | 33.3% | - | 25.6% | 39.4% | 35.0% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 53.4** | 🔴 53.4 | 33.3% | - | - | 27.7% | 26.2% | 46.1% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 ** 21.0** | 🔴 25.1 | 33.3% | 55.4% | 30.7% | - | - | 13.9% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 34.4** | 🔴 34.4 | 33.3% | 52.9% | 23.5% | - | 23.6% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 ** 56.2** | 🟠 64.6 | 33.3% | 41.1% | 24.6% | 34.3% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 **  0.1** | 🔴 4.1 | 33.3% | 80.3% | - | - | 11.7% | 8.0% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 **  3.3** | 🔴 10.9 | 33.3% | 68.5% | - | 16.2% | - | 15.3% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 ** 10.2** | 🔴 34.0 | 33.3% | 49.0% | - | 15.1% | 35.9% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟠 ** 72.1** | 🟠 72.1 | 25.0% | 18.5% | 24.8% | 28.7% | 28.0% | - | 🟠 WYMAGA UWAGI |
| `4p-no-cienie` | 4 | 🔴 **  9.3** | 🟠 68.5 | 25.0% | 31.9% | - | 21.1% | 26.2% | 20.8% | 🔴 ODCHYLONY |
| `4p-no-kabala` | 4 | 🟠 ** 63.9** | 🟠 63.9 | 25.0% | 16.1% | 27.2% | 29.0% | - | 27.7% | 🟠 WYMAGA UWAGI |
| `4p-no-korona` | 4 | 🟢 ** 96.7** | 🟢 96.7 | 25.0% | 26.1% | 24.5% | - | 24.9% | 24.5% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟠 ** 64.4** | 🟠 64.4 | 25.0% | - | 18.5% | 23.8% | 24.9% | 32.8% | 🟠 WYMAGA UWAGI |
| `5p-full` | 5 | 🔴 **  3.2** | 🔴 44.9 | 20.0% | 31.3% | 20.4% | 14.1% | 21.5% | 12.7% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.17 🟢 | 0.0% 🟢 | 0.2% 🟢 | 1.16 🟢 | 6.46 🔴 | 10.02zł | 8.05 | 🟢 OPTYMALNA |
| `3p-cienie-korona-gildia` | 6.77 🟡 | 0.0% 🟢 | 5.9% 🟢 | 1.19 🟢 | 7.65 🔴 | 9.96zł | 9.16 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 6.83 🟡 | 1.3% 🟢 | 6.1% 🟢 | 1.22 🟢 | 6.37 🔴 | 8.28zł | 7.89 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.38 🟢 | 0.1% 🟢 | 6.6% 🟢 | 1.14 🟢 | 6.71 🔴 | 3.1zł | 8.51 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 5.92 🟢 | 0.0% 🟢 | 2.2% 🟢 | 1.54 🟢 | 6.66 🔴 | 10.94zł | 9.25 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 5.8 🟢 | 0.0% 🟢 | 2.0% 🟢 | 1.65 🟢 | 5.39 🔴 | 8.6zł | 8.45 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-korona` | 6.62 🟡 | 0.0% 🟢 | 6.5% 🟢 | 1.63 🟢 | 6.92 🔴 | 8.69zł | 9.14 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 4.91 🟡 | 0.0% 🟢 | 2.6% 🟢 | 1.38 🟢 | 5.24 🔴 | 3.84zł | 8.86 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 5.79 🟢 | 0.0% 🟢 | 8.1% 🟢 | 1.42 🟢 | 6.37 🔴 | 3.9zł | 9.67 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 5.77 🟢 | 0.0% 🟢 | 8.0% 🟢 | 1.54 🟢 | 5.21 🔴 | 2.22zł | 8.61 | 🟢 OPTYMALNA |
| `4p-core` | 6.07 🟢 | 0.0% 🟢 | 5.7% 🟢 | 1.53 🟢 | 6.74 🔴 | 6.77zł | 7.92 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.64 🟢 | 0.0% 🟢 | 6.7% 🟢 | 1.4 🟢 | 6.71 🔴 | 3.24zł | 8.54 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.17 🟢 | 0.0% 🟢 | 6.2% 🟢 | 1.44 🟢 | 7.72 🔴 | 8.27zł | 8.59 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.66 🟢 | 0.0% 🟢 | 1.8% 🟢 | 1.52 🟢 | 6.85 🔴 | 8.07zł | 8.26 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.81 🟢 | 0.0% 🟢 | 4.9% 🟢 | 1.07 🟢 | 6.53 🔴 | 7.06zł | 7.92 | 🟢 OPTYMALNA |
| `5p-full` | 5.22 🟢 | 0.0% 🟢 | 5.0% 🟢 | 1.3 🟢 | 6.34 🔴 | 6.23zł | 7.72 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.140 | Ekstremalny Deadlock (Era 11+): 0.7% gier (>0.5%) |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.280 | Ekstremalny Deadlock (Era 11+): 6.4% gier (>0.5%) |
| `3p-korona-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-gildia` | ⚠️ Ostrzeżenie Witalności | 0.175 | Przedwczesne Zwycięstwa (Era 1-2): 0.7% gier (>0.5%) |
| `3p-oficjum-alandalus-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-korona` | ⚠️ Ostrzeżenie Witalności | 0.140 | Ekstremalny Deadlock (Era 11+): 0.7% gier (>0.5%) |
| `3p-oficjum-kabala-gildia` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 4.842 | Przedwczesne Zwycięstwa (Era 1-2): 0.8% gier (>0.5%), Nadmiar Wczesnych Zakończeń (Era 3-4): 38.1% gier (>25.0%), Zbyt Krótka Średnia Rozgrywka 4.91 Er (<5.0 Er), Zbyt rzadkie Autodafé (1.38/partię < 1.40) — naruszenie ADR-0016 (~2 Autodafé na partię), Martwa ścieżka stosy (swiete-oficjum): 1/803 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 8/685 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 28/490 wygranych (<8%) — gra tylko skazania |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.000 | Zbyt rzadkie Autodafé (1.40/partię < 1.40) — naruszenie ADR-0016 (~2 Autodafé na partię) |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.650 | Nadmiar Wczesnych Zakończeń (Era 3-4): 31.5% gier (>25.0%), Zbyt rzadkie Autodafé (1.30/partię < 1.40) — naruszenie ADR-0016 (~2 Autodafé na partię) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 28 |   0.2% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 505 |   3.2% | `██                  ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 2,368 |  14.8% | `███████             ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 3,443 |  21.5% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 4,285 |  26.8% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 2,751 |  17.2% | `█████████           ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 1,774 |  11.1% | `██████              ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 544 |   3.4% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 201 |   1.3% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 57 |   0.4% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 19 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 13** | 11 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 14** | 14 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 28 | 13 | 15 | 0 | 0 | 0 | **CAA (15)** |
| **Era 3** | 505 | 194 | 126 | 10 | 175 | 0 | **SO (194)** |
| **Era 4** | 2,368 | 851 | 481 | 82 | 846 | 108 | **SO (851)** |
| **Era 5** | 3,443 | 1,362 | 295 | 384 | 944 | 458 | **SO (1,362)** |
| **Era 6** | 4,285 | 926 | 1,168 | 995 | 584 | 612 | **CAA (1,168)** |
| **Era 7** | 2,751 | 747 | 461 | 666 | 194 | 683 | **SO (747)** |
| **Era 8** | 1,774 | 398 | 185 | 363 | 79 | 749 | **GC (749)** |
| **Era 9** | 544 | 145 | 46 | 144 | 33 | 176 | **GC (176)** |
| **Era 10** | 201 | 62 | 16 | 83 | 11 | 29 | **KB (83)** |
| **Era 11** | 57 | 9 | 6 | 31 | 6 | 5 | **KB (31)** |
| **Era 12** | 19 | 3 | 2 | 11 | 0 | 3 | **KB (11)** |
| **Era 13** | 11 | 1 | 2 | 8 | 0 | 0 | **KB (8)** |
| **Era 14** | 14 | 0 | 0 | 6 | 7 | 1 | **KT (7)** |
| **SUMA** | **16,000** | **4,711** | **2,803** | **2,783** | **2,879** | **2,824** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **6.07** |  0.1% | 13.6% | 69.9% | 16.0% |  0.4% | **CAA (36.4%)** |
| `4p-no-cienie` | **5.64** |  0.0% | 18.2% | 73.9% |  7.9% |  0.0% | **KB (35.5%)** |
| `4p-no-kabala` | **6.17** |  0.0% |  9.8% | 77.1% | 13.1% |  0.0% | **KB (39.0%)** |
| `4p-no-korona` | **5.66** |  0.2% | 24.6% | 64.2% | 10.9% |  0.1% | **CAA (34.8%)** |
| `4p-no-oficjum` | **5.81** |  0.1% | 17.3% | 71.1% | 11.5% |  0.0% | **KB (38.1%)** |