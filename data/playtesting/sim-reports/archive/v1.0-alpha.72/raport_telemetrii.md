# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.72

**Wersja Balansu:** `v1.0-alpha.72` | **Data:** 2026-08-24 09:52 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 4.43s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🟡 ** 80.7** | 🟢 94.7 | 33.3% | - | 35.1% | - | 32.1% | 32.8% | 🟡 AKCEPTOWALNY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 47.4** | 🔴 47.4 | 33.3% | - | 20.1% | 34.4% | - | 45.5% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 ** 14.3** | 🟠 69.2 | 33.3% | - | 26.5% | 40.9% | 32.6% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 45.7** | 🔴 51.5 | 33.3% | - | - | 27.2% | 26.1% | 46.7% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 ** 19.2** | 🔴 19.2 | 33.3% | 60.0% | 26.6% | - | - | 13.4% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 43.5** | 🔴 43.5 | 33.3% | 49.0% | 28.5% | - | 22.5% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 ** 56.9** | 🟠 66.8 | 33.3% | 39.2% | 24.5% | 36.3% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 **  1.3** | 🔴 9.0 | 33.3% | 70.9% | - | - | 15.3% | 13.8% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 **  4.0** | 🔴 13.4 | 33.3% | 65.8% | - | 16.5% | - | 17.7% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 ** 31.5** | 🔴 36.2 | 33.3% | 48.8% | - | 16.3% | 34.9% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟡 ** 84.1** | 🟡 84.1 | 25.0% | 22.7% | 22.5% | 27.8% | 27.0% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🔴 ** 54.7** | 🔴 54.7 | 25.0% | 34.7% | - | 18.8% | 27.4% | 19.1% | 🔴 ODCHYLONY |
| `4p-no-kabala` | 4 | 🟡 ** 80.3** | 🟡 80.3 | 25.0% | 20.0% | 27.2% | 27.0% | - | 25.8% | 🟡 AKCEPTOWALNY |
| `4p-no-korona` | 4 | 🟡 ** 86.7** | 🟡 86.7 | 25.0% | 24.8% | 28.2% | - | 24.6% | 22.4% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🔴 ** 55.0** | 🔴 55.0 | 25.0% | - | 17.2% | 21.3% | 26.9% | 34.6% | 🔴 ODCHYLONY |
| `5p-full` | 5 | 🔴 **  3.2** | 🔴 36.7 | 20.0% | 34.2% | 20.8% | 14.3% | 19.5% | 11.2% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.11 🟢 | 0.0% 🟢 | 0.2% 🟢 | 1.14 🟢 | 6.13 🔴 | 11.39zł | 7.99 | 🟢 OPTYMALNA |
| `3p-cienie-korona-gildia` | 6.76 🟡 | 0.0% 🟢 | 5.8% 🟢 | 1.18 🟢 | 7.55 🔴 | 11.27zł | 9.17 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 6.88 🟡 | 1.2% 🟢 | 6.0% 🟢 | 1.23 🟢 | 6.43 🔴 | 9.67zł | 7.9 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.33 🟢 | 0.1% 🟢 | 6.6% 🟢 | 1.14 🟢 | 6.62 🔴 | 3.09zł | 8.5 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 5.71 🟢 | 0.0% 🟢 | 1.7% 🟢 | 1.62 🟢 | 6.35 🔴 | 12.41zł | 9.27 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 5.85 🟢 | 0.0% 🟢 | 1.7% 🟢 | 1.68 🟢 | 5.48 🔴 | 10.13zł | 8.51 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-korona` | 6.63 🟡 | 0.0% 🟢 | 6.5% 🟢 | 1.76 🟢 | 6.78 🔴 | 10.45zł | 9.12 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 5.17 🟢 | 0.0% 🟢 | 2.0% 🟢 | 1.41 🟢 | 5.87 🔴 | 4.23zł | 9.08 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-gildia` | 5.89 🟢 | 0.0% 🟢 | 7.9% 🟢 | 1.56 🟢 | 6.76 🔴 | 4.11zł | 9.66 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 5.93 🟢 | 0.0% 🟢 | 7.4% 🟢 | 1.6 🟢 | 5.61 🔴 | 2.35zł | 8.69 | 🟢 OPTYMALNA |
| `4p-core` | 5.98 🟢 | 0.0% 🟢 | 5.6% 🟢 | 1.67 🟢 | 6.87 🔴 | 7.69zł | 7.92 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.54 🟢 | 0.0% 🟢 | 6.2% 🟢 | 1.5 🟢 | 6.73 🔴 | 3.4zł | 8.52 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.98 🟢 | 0.0% 🟢 | 5.8% 🟢 | 1.56 🟢 | 7.43 🔴 | 9.21zł | 8.54 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.54 🟢 | 0.0% 🟢 | 1.3% 🟢 | 1.55 🟢 | 6.79 🔴 | 8.97zł | 8.33 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.77 🟢 | 0.0% 🟢 | 5.0% 🟢 | 1.06 🟢 | 6.31 🔴 | 7.9zł | 7.84 | 🟢 OPTYMALNA |
| `5p-full` | 5.14 🟢 | 0.0% 🟢 | 4.6% 🟢 | 1.38 🟢 | 6.21 🔴 | 6.95zł | 7.73 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.160 | Ekstremalny Deadlock (Era 11+): 0.8% gier (>0.5%) |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.580 | Ekstremalny Deadlock (Era 11+): 7.9% gier (>0.5%) |
| `3p-korona-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.120 | Ekstremalny Deadlock (Era 11+): 0.6% gier (>0.5%) |
| `3p-oficjum-alandalus-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-korona` | ⚠️ Ostrzeżenie Witalności | 0.160 | Ekstremalny Deadlock (Era 11+): 0.8% gier (>0.5%) |
| `3p-oficjum-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 1.970 | Przedwczesne Zwycięstwa (Era 1-2): 0.8% gier (>0.5%), Nadmiar Wczesnych Zakończeń (Era 3-4): 30.7% gier (>25.0%), Martwa ścieżka stosy (swiete-oficjum): 5/709 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 26/658 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 0.140 | Ekstremalny Deadlock (Era 11+): 0.7% gier (>0.5%) |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.430 | Nadmiar Wczesnych Zakończeń (Era 3-4): 29.3% gier (>25.0%), Zbyt rzadkie Autodafé (1.38/partię < 1.40) — naruszenie ADR-0016 (~2 Autodafé na partię) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 28 |   0.2% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 527 |   3.3% | `██                  ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 2,208 |  13.8% | `███████             ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 3,780 |  23.6% | `████████████        ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 4,187 |  26.2% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 2,761 |  17.3% | `█████████           ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 1,673 |  10.5% | `█████               ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 547 |   3.4% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 177 |   1.1% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 61 |   0.4% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 22 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 13** | 16 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 14** | 13 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 28 | 8 | 20 | 0 | 0 | 0 | **CAA (20)** |
| **Era 3** | 527 | 190 | 140 | 11 | 186 | 0 | **SO (190)** |
| **Era 4** | 2,208 | 742 | 461 | 86 | 820 | 99 | **KT (820)** |
| **Era 5** | 3,780 | 1,339 | 599 | 398 | 953 | 491 | **SO (1,339)** |
| **Era 6** | 4,187 | 979 | 994 | 941 | 585 | 688 | **CAA (994)** |
| **Era 7** | 2,761 | 836 | 367 | 671 | 234 | 653 | **SO (836)** |
| **Era 8** | 1,673 | 417 | 111 | 393 | 68 | 684 | **GC (684)** |
| **Era 9** | 547 | 145 | 53 | 143 | 24 | 182 | **GC (182)** |
| **Era 10** | 177 | 42 | 19 | 83 | 10 | 23 | **KB (83)** |
| **Era 11** | 61 | 1 | 6 | 46 | 2 | 6 | **KB (46)** |
| **Era 12** | 22 | 2 | 0 | 16 | 1 | 3 | **KB (16)** |
| **Era 13** | 16 | 0 | 2 | 14 | 0 | 0 | **KB (14)** |
| **Era 14** | 13 | 0 | 0 | 6 | 6 | 1 | **KB (6)** |
| **SUMA** | **16,000** | **4,701** | **2,772** | **2,808** | **2,889** | **2,830** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **5.98** |  0.1% | 14.5% | 69.8% | 15.5% |  0.1% | **KB (40.1%)** |
| `4p-no-cienie` | **5.54** |  0.0% | 19.6% | 74.0% |  6.4% |  0.0% | **KB (31.3%)** |
| `4p-no-kabala` | **5.98** |  0.3% | 10.4% | 80.6% |  8.7% |  0.0% | **KB (33.5%)** |
| `4p-no-korona` | **5.54** |  0.3% | 25.0% | 65.7% |  9.0% |  0.0% | **CAA (35.1%)** |
| `4p-no-oficjum` | **5.77** |  0.0% | 17.4% | 71.6% | 11.0% |  0.0% | **KB (32.7%)** |