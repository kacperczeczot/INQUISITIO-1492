[Strona główna](../../../../../README.md) > [v1.0-alpha.45](README.md) > [raport_telemetrii](raport_telemetrii.md)

---

# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.45

**Wersja Balansu:** `v1.0-alpha.45` | **Data:** 2026-08-23 11:08 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 45.88s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 **  0.2** | 🔴 38.5 | 33.3% | - | 24.5% | - | 24.3% | 51.2% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 11.5** | 🔴 44.1 | 33.3% | - | 22.0% | 29.4% | - | 48.6% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 **  0.1** | 🟠 67.2 | 33.3% | - | 24.5% | 38.4% | 37.1% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 **  0.3** | 🔴 24.9 | 33.3% | - | - | 21.2% | 21.2% | 57.5% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 **  1.7** | 🔴 41.6 | 33.3% | 50.0% | 24.1% | - | - | 25.8% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 **  0.5** | 🔴 19.7 | 33.3% | 60.8% | 20.2% | - | 19.0% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 ** 14.5** | 🔴 50.6 | 33.3% | 47.0% | 27.1% | 25.9% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 **  0.2** | 🔴 8.4 | 33.3% | 70.8% | - | - | 7.2% | 22.0% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 ** 42.8** | 🔴 47.4 | 33.3% | 47.4% | - | 22.7% | - | 29.9% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 **  0.1** | 🔴 27.1 | 33.3% | 53.6% | - | 13.8% | 32.6% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🔴 **  0.5** | 🟠 63.7 | 25.0% | 34.0% | 22.5% | 22.1% | 21.4% | - | 🔴 ODCHYLONY |
| `4p-no-cienie` | 4 | 🔴 **  1.5** | 🔴 56.9 | 25.0% | 30.6% | - | 17.8% | 19.8% | 31.7% | 🔴 ODCHYLONY |
| `4p-no-kabala` | 4 | 🔴 **  7.3** | 🟠 72.3 | 25.0% | 23.2% | 22.9% | 22.0% | - | 31.9% | 🔴 ODCHYLONY |
| `4p-no-korona` | 4 | 🔴 **  0.5** | 🟠 65.3 | 25.0% | 29.6% | 22.1% | - | 18.3% | 29.9% | 🔴 ODCHYLONY |
| `4p-no-oficjum` | 4 | 🔴 **  0.1** | 🟠 69.3 | 25.0% | - | 21.4% | 23.0% | 23.0% | 32.6% | 🔴 ODCHYLONY |
| `5p-full` | 5 | 🔴 **  0.1** | 🔴 50.4 | 20.0% | 25.8% | 16.9% | 10.5% | 20.8% | 26.0% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 4.56 🟡 | 0.0% 🟢 | 0.4% 🟢 | 1.13 🟢 | 3.66 🟢 | 8.18zł | 7.86 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 5.11 🟢 | 0.0% 🟢 | 3.5% 🟢 | 1.33 🟢 | 4.25 🟢 | 8.57zł | 8.41 | 🟢 OPTYMALNA |
| `3p-cienie-korona-kabala` | 5.6 🟢 | 6.5% 🟡 | 4.8% 🟢 | 1.23 🟢 | 4.97 🟡 | 8.3zł | 7.04 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 4.72 🟡 | 0.0% 🟢 | 4.6% 🟢 | 1.15 🟢 | 4.08 🟢 | 2.83zł | 8.25 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-gildia` | 4.84 🟡 | 0.0% 🟢 | 1.3% 🟢 | 1.81 🟡 | 4.32 🟢 | 9.23zł | 8.62 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-kabala` | 4.73 🟡 | 0.0% 🟢 | 1.5% 🟢 | 1.77 🟢 | 3.44 🟢 | 7.82zł | 7.81 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 5.55 🟢 | 0.0% 🟢 | 4.3% 🟢 | 2.04 🔴 | 4.39 🟢 | 8.46zł | 8.37 | 🟢 OPTYMALNA |
| `3p-oficjum-kabala-gildia` | 4.53 🟡 | 0.0% 🟢 | 1.8% 🟢 | 1.65 🟢 | 4.47 🟢 | 3.21zł | 8.65 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 5.04 🟢 | 0.0% 🟢 | 5.5% 🟢 | 1.74 🟢 | 4.83 🟡 | 3.44zł | 9.26 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 4.38 🔴 | 0.0% 🟢 | 5.4% 🟢 | 1.51 🟢 | 3.25 🟢 | 2.42zł | 7.89 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 4.73 🟡 | 0.0% 🟢 | 4.0% 🟢 | 1.81 🟡 | 4.37 🟢 | 6.19zł | 7.57 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-cienie` | 4.53 🟡 | 0.0% 🟢 | 4.2% 🟢 | 1.64 🟢 | 4.47 🟢 | 2.86zł | 8.22 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-kabala` | 4.71 🟡 | 0.0% 🟢 | 3.5% 🟢 | 1.76 🟢 | 4.38 🟢 | 6.87zł | 8.06 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-korona` | 4.36 🔴 | 0.0% 🟢 | 1.1% 🟢 | 1.65 🟢 | 4.15 🟢 | 6.65zł | 7.79 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-oficjum` | 4.27 🔴 | 0.0% 🟢 | 2.9% 🟢 | 1.04 🟢 | 3.55 🟢 | 6.32zł | 7.14 | ⚠️ WARTOŚCI BRZEGOWE |
| `5p-full` | 4.03 🔴 | 0.0% 🟢 | 3.0% 🟢 | 1.52 🟢 | 3.77 🟢 | 5.43zł | 7.2 | ⚠️ WARTOŚCI BRZEGOWE |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 5.415 | Przedwczesne Zwycięstwa (Era 1-2): 11.4% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 25.1% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.56 Er (<5.0 Er) |
| `3p-cienie-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 1.341 | Przedwczesne Zwycięstwa (Era 1-2): 2.8% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 12.5% gier (>6.0%) |
| `3p-cienie-korona-kabala` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 6.481 | Paraliż Gry / Deadlocks 6.5% (>5%), Przedwczesne Zwycięstwa (Era 1-2): 15.6% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 30.4% gier (>6.0%) |
| `3p-korona-kabala-gildia` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 4.368 | Przedwczesne Zwycięstwa (Era 1-2): 11.0% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 17.9% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.72 Er (<5.0 Er) |
| `3p-oficjum-alandalus-gildia` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 3.227 | Przedwczesne Zwycięstwa (Era 1-2): 3.5% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 15.0% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.84 Er (<5.0 Er), Martwa ścieżka stosy (swiete-oficjum): 275/5005 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-alandalus-kabala` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 3.655 | Przedwczesne Zwycięstwa (Era 1-2): 7.3% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 20.2% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.73 Er (<5.0 Er) |
| `3p-oficjum-alandalus-korona` | ⚠️ Ostrzeżenie Witalności | 1.246 | Przedwczesne Zwycięstwa (Era 1-2): 2.5% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 12.3% gier (>6.0%) |
| `3p-oficjum-kabala-gildia` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 3.834 | Przedwczesne Zwycięstwa (Era 1-2): 2.8% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 18.2% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.53 Er (<5.0 Er), Martwa ścieżka stosy (swiete-oficjum): 31/7082 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 0.103 | Zbyt Wczesne Zakończenia (Era 1-3): 7.0% gier (>6.0%) |
| `3p-oficjum-korona-kabala` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 8.307 | Przedwczesne Zwycięstwa (Era 1-2): 15.3% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 29.4% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.38 Er (<5.0 Er), Martwa ścieżka stosy (swiete-oficjum): 325/5363 wygranych (<8%) — gra tylko skazania |
| `4p-core` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 4.779 | Przedwczesne Zwycięstwa (Era 1-2): 9.7% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 25.6% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.73 Er (<5.0 Er) |
| `4p-no-cienie` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 3.646 | Przedwczesne Zwycięstwa (Era 1-2): 7.1% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 17.6% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.53 Er (<5.0 Er) |
| `4p-no-kabala` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.290 | Przedwczesne Zwycięstwa (Era 1-2): 3.9% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 14.6% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.71 Er (<5.0 Er) |
| `4p-no-korona` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 4.885 | Przedwczesne Zwycięstwa (Era 1-2): 8.9% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 23.0% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.36 Er (<5.0 Er) |
| `4p-no-oficjum` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 6.505 | Przedwczesne Zwycięstwa (Era 1-2): 12.3% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 29.3% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.27 Er (<5.0 Er) |
| `5p-full` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 6.686 | Przedwczesne Zwycięstwa (Era 1-2): 10.9% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 31.2% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.03 Er (<5.0 Er) |

## 3.1. Frakcje Wymagające Uwagi

| Frakcja | Śr. Win Share (wszystkie setupy) | Najgorszy Setup | Max Odchylenie od Ideału | Status |
| :--- | :---: | :--- | :---: | :--- |
| **SO** | 43.0% | `3p-oficjum-kabala-gildia` | +37.5% | 🟡 DOMINUJE |
| **KT** | 22.2% | `3p-oficjum-kabala-gildia` | -26.1% | 🟡 SŁABA |
| **GC** | 35.2% | `3p-korona-kabala-gildia` | +24.2% | 🟡 DOMINUJE |
| **KB** | 22.4% | `3p-oficjum-korona-kabala` | -19.5% | 🟡 SŁABA |
| **CAA** | 22.6% | `3p-oficjum-alandalus-kabala` | -13.1% | 🟡 SŁABA |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `3p-cienie-korona-kabala` | 🔴 **  0.1** | CAA za słaba (24.5% vs ideal 33.3%) |
| `3p-oficjum-korona-kabala` | 🔴 **  0.1** | SO dominuje (53.6% vs ideal 33.3%) |
| `4p-no-oficjum` | 🔴 **  0.1** | GC dominuje (32.6% vs ideal 25.0%) |
| `5p-full` | 🔴 **  0.1** | KB za słaba (10.5% vs ideal 20.0%) |
| `3p-cienie-kabala-gildia` | 🔴 **  0.2** | GC dominuje (51.2% vs ideal 33.3%) |
| `3p-oficjum-kabala-gildia` | 🔴 **  0.2** | SO dominuje (70.8% vs ideal 33.3%) |
| `3p-korona-kabala-gildia` | 🔴 **  0.3** | GC dominuje (57.5% vs ideal 33.3%) |
| `3p-oficjum-alandalus-kabala` | 🔴 **  0.5** | SO dominuje (60.8% vs ideal 33.3%) |
| `4p-core` | 🔴 **  0.5** | SO dominuje (34.0% vs ideal 25.0%) |
| `4p-no-korona` | 🔴 **  0.5** | KT za słaba (18.3% vs ideal 25.0%) |
| `4p-no-cienie` | 🔴 **  1.5** | KB za słaba (17.8% vs ideal 25.0%) |
| `3p-oficjum-alandalus-gildia` | 🔴 **  1.7** | SO dominuje (50.0% vs ideal 33.3%) |
| `4p-no-kabala` | 🔴 **  7.3** | GC dominuje (31.9% vs ideal 25.0%) |
| `3p-cienie-korona-gildia` | 🔴 ** 11.5** | GC dominuje (48.6% vs ideal 33.3%) |
| `3p-oficjum-alandalus-korona` | 🔴 ** 14.5** | SO dominuje (47.0% vs ideal 33.3%) |
| `3p-oficjum-korona-gildia` | 🔴 ** 42.8** | SO dominuje (47.4% vs ideal 33.3%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 1** | 416 |   0.3% | `                    ` | 🔴 Za wczesna (sprint / brak intrygi) |
| **Era 2** | 12,088 |   7.6% | `████                ` | 🔴 Za wczesna (sprint / brak intrygi) |
| **Era 3** | 20,446 |  12.8% | `██████              ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 38,181 |  23.9% | `████████████        ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 44,491 |  27.8% | `██████████████      ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 29,082 |  18.2% | `█████████           ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 9,296 |   5.8% | `███                 ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 3,058 |   1.9% | `█                   ` | 🟡 Przedłużona |
| **Era 9** | 1,262 |   0.8% | `                    ` | 🔴 Limit Er (Deadlock) |
| **Era 10** | 456 |   0.3% | `                    ` | 🔴 Limit Er (Deadlock) |
| **Era 11** | 300 |   0.2% | `                    ` | 🔴 Limit Er (Deadlock) |
| **Era 12** | 184 |   0.1% | `                    ` | 🔴 Limit Er (Deadlock) |
| **Era 13** | 87 |   0.1% | `                    ` | 🔴 Limit Er (Deadlock) |
| **Era 14** | 653 |   0.4% | `                    ` | 🔴 Limit Er (Deadlock) |

### 4.2. Rozkład Szans Wygranych Frakcji w poszczególnych Erach (% Wygranych Frakcji w danej Erze)

*Wiersze sumują się do 100.0% — wskazują która frakcja dominuje w danej fazie czasowej partii.*

| Era Końca Gry | Gry w Erze | SO % | CAA % | KB % | KT % | GC % | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 1** | 416 |   0.0% |  94.2% |   0.0% |   5.8% |   0.0% | **CAA (94.2%)** |
| **Era 2** | 12,088 |   0.8% |  26.2% |   0.1% |  72.9% |   0.0% | **KT (72.9%)** |
| **Era 3** | 20,446 |  18.1% |  35.0% |   8.5% |  34.4% |   4.0% | **CAA (35.0%)** |
| **Era 4** | 38,181 |  35.0% |  14.9% |  15.0% |  14.8% |  20.2% | **SO (35.0%)** |
| **Era 5** | 44,491 |  32.9% |   8.9% |  23.8% |   4.9% |  29.5% | **SO (32.9%)** |
| **Era 6** | 29,082 |  29.9% |  12.1% |  11.8% |   0.5% |  45.7% | **GC (45.7%)** |
| **Era 7** | 9,296 |  53.7% |   5.6% |  11.8% |   0.2% |  28.7% | **SO (53.7%)** |
| **Era 8** | 3,058 |  34.4% |   8.3% |  27.8% |   0.1% |  29.3% | **SO (34.4%)** |
| **Era 9** | 1,262 |  46.4% |   3.8% |  34.2% |   0.0% |  15.5% | **SO (46.4%)** |
| **Era 10** | 456 |  34.0% |  12.7% |  48.0% |   0.0% |   5.3% | **KB (48.0%)** |
| **Era 11** | 300 |   4.0% |   4.7% |  90.7% |   0.0% |   0.7% | **KB (90.7%)** |
| **Era 12** | 184 |   4.3% |   6.0% |  89.7% |   0.0% |   0.0% | **KB (89.7%)** |
| **Era 13** | 87 |   0.0% |  12.6% |  87.4% |   0.0% |   0.0% | **KB (87.4%)** |
| **Era 14** | 653 |   0.2% |   0.6% |  13.2% |  86.1% |   0.0% | **KT (86.1%)** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Era 1-4 (Wczesne / Szybkie) % | Era 5-7 (Złote Okno) % | Era 8+ (Długie) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **4.73** |  45.2% |  49.7% |   5.1% | **SO (50.5%)** |
| `4p-no-cienie` | **4.53** |  45.1% |  54.1% |   0.7% | **GC (60.5%)** |
| `4p-no-kabala` | **4.71** |  41.1% |  58.2% |   0.7% | **GC (45.9%)** |
| `4p-no-korona` | **4.36** |  54.3% |  45.1% |   0.5% | **GC (56.5%)** |
| `4p-no-oficjum` | **4.27** |  51.7% |  47.9% |   0.3% | **GC (68.7%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **2.0 – 4.5** | 🟡 1.5–2.0 / 4.5–5.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 75 | 🟠 ≥ 60 | 🔴 < 60