# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.79

**Wersja Balansu:** `v1.0-alpha.79` | **Data:** 2026-08-24 20:28 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 76.7s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 ** 48.8** | 🟠 73.9 | 33.3% | - | 40.2% | - | 31.6% | 28.2% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 52.1** | 🟠 66.7 | 33.3% | - | 38.6% | 24.4% | - | 37.0% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 ** 21.8** | 🟡 86.2 | 33.3% | - | 30.4% | 37.2% | 32.4% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 60.3** | 🟡 88.6 | 33.3% | - | - | 31.6% | 31.7% | 36.8% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 ** 13.3** | 🔴 13.3 | 33.3% | 63.8% | 28.2% | - | - | 8.1% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 35.2** | 🔴 35.2 | 33.3% | 52.3% | 26.4% | - | 21.2% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 ** 44.8** | 🔴 50.1 | 33.3% | 46.2% | 22.5% | 31.3% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 **  0.5** | 🔴 5.8 | 33.3% | 76.1% | - | - | 15.3% | 8.7% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 **  2.2** | 🔴 7.4 | 33.3% | 73.0% | - | 17.5% | - | 9.5% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 ** 11.6** | 🔴 38.5 | 33.3% | 49.6% | - | 18.7% | 31.7% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟢 ** 90.9** | 🟢 90.9 | 25.0% | 25.5% | 24.3% | 27.1% | 23.1% | - | 🟢 ZBALANSOWANY |
| `4p-no-cienie` | 4 | 🟠 ** 74.6** | 🟠 74.6 | 25.0% | 29.9% | - | 21.1% | 27.2% | 21.8% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🟡 ** 87.2** | 🟡 87.2 | 25.0% | 26.2% | 27.1% | 24.9% | - | 21.8% | 🟡 AKCEPTOWALNY |
| `4p-no-korona` | 4 | 🟡 ** 83.2** | 🟡 83.2 | 25.0% | 27.3% | 27.7% | - | 23.1% | 21.9% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🟠 ** 73.6** | 🟠 73.6 | 25.0% | - | 20.5% | 23.2% | 25.4% | 30.9% | 🟠 WYMAGA UWAGI |
| `5p-full` | 5 | 🔴 ** 21.3** | 🔴 35.3 | 20.0% | 35.4% | 20.4% | 14.9% | 16.9% | 12.3% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.26 🟢 | 0.1% 🟢 | 0.2% 🟢 | 1.17 🟢 | 7.18 🟢 | 14.0zł | 7.78 | 🟢 OPTYMALNA |
| `3p-cienie-korona-gildia` | 6.85 🟡 | 0.0% 🟢 | 5.8% 🟢 | 1.25 🟢 | 8.14 🟢 | 14.82zł | 8.86 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 6.82 🟡 | 0.7% 🟢 | 5.9% 🟢 | 1.22 🟢 | 7.39 🟢 | 10.35zł | 7.91 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.48 🟢 | 0.1% 🟢 | 6.6% 🟢 | 1.16 🟢 | 7.31 🟢 | 5.08zł | 8.08 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 5.64 🟢 | 0.0% 🟢 | 1.0% 🟢 | 1.67 🟢 | 6.91 🟢 | 14.41zł | 9.14 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 5.76 🟢 | 0.0% 🟢 | 1.1% 🟢 | 1.64 🟢 | 6.57 🟢 | 10.59zł | 8.63 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-korona` | 6.33 🟢 | 0.0% 🟢 | 5.4% 🟢 | 1.7 🟢 | 7.6 🟢 | 10.73zł | 9.19 | 🟢 OPTYMALNA |
| `3p-oficjum-kabala-gildia` | 5.03 🟢 | 0.0% 🟢 | 1.0% 🟢 | 1.47 🟢 | 6.12 🟢 | 5.58zł | 8.79 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-gildia` | 5.95 🟢 | 0.0% 🟢 | 6.3% 🟢 | 1.74 🟢 | 7.1 🟢 | 6.11zł | 9.43 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 5.9 🟢 | 0.0% 🟢 | 6.6% 🟢 | 1.67 🟢 | 6.4 🟢 | 2.64zł | 8.64 | 🟢 OPTYMALNA |
| `4p-core` | 5.98 🟢 | 0.0% 🟢 | 4.8% 🟢 | 1.72 🟢 | 8.09 🟢 | 8.29zł | 8.03 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.7 🟢 | 0.0% 🟢 | 5.6% 🟢 | 1.64 🟢 | 7.52 🟢 | 4.58zł | 8.31 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.91 🟢 | 0.0% 🟢 | 4.8% 🟢 | 1.63 🟢 | 8.21 🟢 | 10.82zł | 8.49 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.62 🟢 | 0.0% 🟢 | 0.8% 🟢 | 1.65 🟢 | 7.91 🟢 | 10.62zł | 8.19 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.74 🟢 | 0.0% 🟢 | 4.8% 🟢 | 1.05 🟢 | 7.16 🟢 | 9.48zł | 7.68 | 🟢 OPTYMALNA |
| `5p-full` | 5.21 🟢 | 0.0% 🟢 | 4.1% 🟢 | 1.49 🟢 | 7.48 🟢 | 8.12zł | 7.7 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.416 | Ekstremalny Deadlock (Era 11+): 2.1% gier (>0.5%) |
| `3p-cienie-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 0.248 | Ekstremalny Deadlock (Era 11+): 1.2% gier (>0.5%) |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.374 | Ekstremalny Deadlock (Era 11+): 6.9% gier (>0.5%) |
| `3p-korona-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.384 | Ekstremalny Deadlock (Era 11+): 1.9% gier (>0.5%) |
| `3p-oficjum-alandalus-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-korona` | ⚠️ Ostrzeżenie Witalności | 0.110 | Ekstremalny Deadlock (Era 11+): 0.5% gier (>0.5%) |
| `3p-oficjum-kabala-gildia` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.527 | Przedwczesne Zwycięstwa (Era 1-2): 0.7% gier (>0.5%), Nadmiar Wczesnych Zakończeń (Era 3-4): 36.5% gier (>25.0%), Martwa ścieżka stosy (swiete-oficjum): 36/7606 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 382/7299 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 230/4960 wygranych (<8%) — gra tylko skazania |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | ⚠️ Ostrzeżenie Witalności | 0.505 | Nadmiar Wczesnych Zakończeń (Era 3-4): 30.0% gier (>25.0%) |

## 3.1. Frakcje Wymagające Uwagi

| Frakcja | Śr. Win Share (wszystkie setupy) | Najgorszy Setup | Max Odchylenie od Ideału | Status |
| :--- | :---: | :--- | :---: | :--- |
| **SO** | 45.9% | `3p-oficjum-kabala-gildia` | +42.8% | 🟡 DOMINUJE |
| **GC** | 21.5% | `3p-oficjum-alandalus-gildia` | -25.2% | 🟡 SŁABA |
| **KT** | 25.4% | `3p-oficjum-kabala-gildia` | -18.0% | 🟡 SŁABA |
| **KB** | 24.7% | `3p-oficjum-korona-gildia` | -15.8% | 🟡 SŁABA |
| **CAA** | 27.8% | `3p-oficjum-alandalus-korona` | -10.8% | 🟡 SŁABA |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `3p-oficjum-kabala-gildia` | 🔴 **  0.5** | SO dominuje (76.1% vs ideal 33.3%) |
| `3p-oficjum-korona-gildia` | 🔴 **  2.2** | SO dominuje (73.0% vs ideal 33.3%) |
| `3p-oficjum-korona-kabala` | 🔴 ** 11.6** | SO dominuje (49.6% vs ideal 33.3%) |
| `3p-oficjum-alandalus-gildia` | 🔴 ** 13.3** | SO dominuje (63.8% vs ideal 33.3%) |
| `5p-full` | 🔴 ** 21.3** | SO dominuje (35.4% vs ideal 20.0%) |
| `3p-cienie-korona-kabala` | 🔴 ** 21.8** | KB dominuje (37.2% vs ideal 33.3%) |
| `3p-oficjum-alandalus-kabala` | 🔴 ** 35.2** | SO dominuje (52.3% vs ideal 33.3%) |
| `3p-oficjum-alandalus-korona` | 🔴 ** 44.8** | SO dominuje (46.2% vs ideal 33.3%) |
| `3p-cienie-kabala-gildia` | 🔴 ** 48.8** | CAA dominuje (40.2% vs ideal 33.3%) |
| `3p-cienie-korona-gildia` | 🔴 ** 52.1** | KB za słaba (24.4% vs ideal 33.3%) |
| `3p-korona-kabala-gildia` | 🔴 ** 60.3** | GC dominuje (36.8% vs ideal 33.3%) |
| `4p-no-oficjum` | 🟠 ** 73.6** | GC dominuje (30.9% vs ideal 25.0%) |
| `4p-no-cienie` | 🟠 ** 74.6** | SO dominuje (29.9% vs ideal 25.0%) |
| `4p-no-korona` | 🟡 ** 83.2** | GC za słaba (21.9% vs ideal 25.0%) |
| `4p-no-kabala` | 🟡 ** 87.2** | GC za słaba (21.8% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 339 |   0.2% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 5,514 |   3.4% | `██                  ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 23,235 |  14.5% | `███████             ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 37,968 |  23.7% | `████████████        ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 40,791 |  25.5% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 26,089 |  16.3% | `████████            ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 16,327 |  10.2% | `█████               ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 5,784 |   3.6% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 2,538 |   1.6% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 845 |   0.5% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 321 |   0.2% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 13** | 153 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 14** | 96 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 339 | 117 | 222 | 0 | 0 | 0 | **CAA (222)** |
| **Era 3** | 5,514 | 2,219 | 1,500 | 110 | 1,682 | 3 | **SO (2,219)** |
| **Era 4** | 23,235 | 9,188 | 4,568 | 1,099 | 7,781 | 599 | **SO (9,188)** |
| **Era 5** | 37,968 | 14,445 | 6,304 | 4,206 | 9,388 | 3,625 | **SO (14,445)** |
| **Era 6** | 40,791 | 9,848 | 10,998 | 8,622 | 5,605 | 5,718 | **CAA (10,998)** |
| **Era 7** | 26,089 | 8,325 | 4,281 | 6,089 | 2,287 | 5,107 | **SO (8,325)** |
| **Era 8** | 16,327 | 4,382 | 1,584 | 3,807 | 704 | 5,850 | **GC (5,850)** |
| **Era 9** | 5,784 | 1,440 | 684 | 1,416 | 299 | 1,945 | **GC (1,945)** |
| **Era 10** | 2,538 | 483 | 347 | 1,095 | 105 | 508 | **KB (1,095)** |
| **Era 11** | 845 | 61 | 99 | 430 | 35 | 220 | **KB (430)** |
| **Era 12** | 321 | 25 | 21 | 169 | 11 | 95 | **KB (169)** |
| **Era 13** | 153 | 3 | 7 | 125 | 1 | 17 | **KB (125)** |
| **Era 14** | 96 | 4 | 4 | 40 | 40 | 8 | **KB (40)** |
| **SUMA** | **160,000** | **50,540** | **30,619** | **27,208** | **27,938** | **23,695** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **5.98** |  0.1% | 14.3% | 70.2% | 15.2% |  0.2% | **KB (34.3%)** |
| `4p-no-cienie` | **5.70** |  0.0% | 16.8% | 74.6% |  8.6% |  0.0% | **KB (32.5%)** |
| `4p-no-kabala` | **5.91** |  0.3% | 12.8% | 77.0% |  9.8% |  0.0% | **KB (31.5%)** |
| `4p-no-korona` | **5.62** |  0.3% | 22.6% | 67.1% |  9.8% |  0.1% | **CAA (35.6%)** |
| `4p-no-oficjum` | **5.74** |  0.2% | 16.5% | 73.4% |  9.9% |  0.0% | **KB (36.8%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **3.5 – 8.5** | 🟡 2.0–3.5 / 8.5–10.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 80 | 🟠 ≥ 65 | 🔴 < 65