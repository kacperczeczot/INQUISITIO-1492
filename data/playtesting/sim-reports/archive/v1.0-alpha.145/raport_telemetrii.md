# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.145

**Wersja Balansu:** `v1.0-alpha.145` | **Data:** 2026-08-30 10:35 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 0.53s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🟠 ** 73.2** | 🟠 73.2 | 33.3% | - | 40.6% | - | 29.1% | 30.3% | 🟠 WYMAGA UWAGI |
| `3p-cienie-korona-gildia` | 3 | 🟡 ** 88.2** | 🟡 88.2 | 33.3% | - | 32.9% | 30.5% | - | 36.6% | 🟡 AKCEPTOWALNY |
| `3p-cienie-korona-kabala` | 3 | 🟠 ** 71.6** | 🟠 71.6 | 33.3% | - | 37.3% | 37.1% | 25.6% | - | 🟠 WYMAGA UWAGI |
| `3p-korona-kabala-gildia` | 3 | 🟠 ** 72.8** | 🟠 72.8 | 33.3% | - | - | 37.5% | 25.9% | 36.6% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-alandalus-gildia` | 3 | 🟡 ** 82.1** | 🟡 82.1 | 33.3% | 34.6% | 28.4% | - | - | 37.0% | 🟡 AKCEPTOWALNY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 52.0** | 🔴 52.0 | 33.3% | 46.3% | 24.7% | - | 29.0% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 ** 50.5** | 🔴 50.5 | 33.3% | 33.5% | 21.4% | 45.1% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 ** 57.9** | 🔴 57.9 | 33.3% | 26.8% | - | - | 28.5% | 44.8% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🟠 ** 71.6** | 🟠 71.6 | 33.3% | 26.7% | - | 33.1% | - | 40.2% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-korona-kabala` | 3 | 🟡 ** 87.2** | 🟡 87.2 | 33.3% | 30.1% | - | 33.2% | 36.7% | - | 🟡 AKCEPTOWALNY |
| `4p-core` | 4 | 🟡 ** 85.7** | 🟡 85.7 | 25.0% | 22.9% | 23.8% | 28.7% | 24.6% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟡 ** 81.8** | 🟡 81.8 | 25.0% | 22.5% | - | 22.4% | 28.9% | 26.2% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟡 ** 89.9** | 🟡 89.9 | 25.0% | 22.3% | 25.6% | 25.3% | - | 26.8% | 🟡 AKCEPTOWALNY |
| `4p-no-korona` | 4 | 🟢 ** 97.8** | 🟢 97.8 | 25.0% | 24.8% | 25.8% | - | 24.9% | 24.5% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟢 ** 97.9** | 🟢 97.9 | 25.0% | - | 24.4% | 24.8% | 25.7% | 25.1% | 🟢 ZBALANSOWANY |
| `5p-full` | 5 | 🟡 ** 86.2** | 🟡 86.2 | 20.0% | 19.5% | 22.1% | 18.9% | 21.8% | 17.7% | 🟡 AKCEPTOWALNY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.49 🟢 | 0.1% 🟢 | 1.1% 🟢 | 1.22 🟢 | 6.17 🟢 | 7.93zł | 5.79 | 🟢 OPTYMALNA |
| `3p-cienie-korona-gildia` | 6.73 🟡 | 0.0% 🟢 | 3.1% 🟢 | 1.23 🟢 | 7.39 🟢 | 7.67zł | 6.56 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.13 🔴 | 0.9% 🟢 | 4.1% 🟢 | 1.31 🟢 | 6.25 🟢 | 6.34zł | 5.84 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.78 🟡 | 0.1% 🟢 | 5.2% 🟢 | 1.25 🟢 | 6.58 🟢 | 2.73zł | 6.0 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-gildia` | 6.09 🟢 | 0.0% 🟢 | 0.1% 🟢 | 1.81 🟡 | 7.61 🟢 | 9.48zł | 6.98 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 6.59 🟡 | 0.1% 🟢 | 0.4% 🟢 | 2.07 🔴 | 7.47 🟢 | 8.13zł | 6.47 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 6.53 🟡 | 0.0% 🟢 | 2.1% 🟢 | 2.02 🔴 | 7.41 🟢 | 7.43zł | 6.77 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 6.2 🟢 | 0.0% 🟢 | 0.7% 🟢 | 1.84 🟡 | 7.71 🟢 | 4.59zł | 6.81 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-gildia` | 6.16 🟢 | 0.0% 🟢 | 2.4% 🟢 | 1.76 🟢 | 7.68 🟢 | 4.2zł | 7.17 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 6.63 🟡 | 0.0% 🟢 | 3.1% 🟢 | 2.04 🔴 | 7.16 🟢 | 2.91zł | 6.42 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.0 🟢 | 0.0% 🟢 | 3.3% 🟢 | 1.87 🟡 | 7.46 🟢 | 7.46zł | 7.84 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.74 🟢 | 0.0% 🟢 | 3.7% 🟢 | 1.74 🟢 | 7.69 🟢 | 4.15zł | 8.31 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.69 🟢 | 0.0% 🟢 | 2.7% 🟢 | 1.69 🟢 | 7.82 🟢 | 8.34zł | 8.44 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.68 🟢 | 0.0% 🟢 | 0.7% 🟢 | 1.78 🟢 | 7.68 🟢 | 8.86zł | 8.23 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 6.1 🟢 | 0.0% 🟢 | 4.6% 🟢 | 1.13 🟢 | 6.84 🟢 | 7.06zł | 7.47 | 🟢 OPTYMALNA |
| `5p-full` | 5.4 🟢 | 0.0% 🟢 | 3.9% 🟢 | 1.64 🟢 | 7.55 🟢 | 8.39zł | 9.48 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-korona-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-korona-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |

## 3.1. Frakcje Wymagające Uwagi

| Frakcja | Śr. Win Share (wszystkie setupy) | Najgorszy Setup | Max Odchylenie od Ideału | Status |
| :--- | :---: | :--- | :---: | :--- |
| **SO** | 28.2% | `3p-oficjum-alandalus-kabala` | +13.0% | 🟡 DOMINUJE |
| **CAA** | 27.9% | `3p-oficjum-alandalus-korona` | -11.9% | 🟡 SŁABA |
| **KB** | 30.6% | `3p-oficjum-alandalus-korona` | +11.8% | 🟡 DOMINUJE |
| **GC** | 31.4% | `3p-oficjum-kabala-gildia` | +11.5% | 🟡 DOMINUJE |
| **KT** | 27.3% | `3p-cienie-korona-kabala` | -7.7% | 🟡 SŁABA |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `3p-oficjum-alandalus-korona` | 🔴 ** 50.5** | CAA za słaba (21.4% vs ideal 33.3%) |
| `3p-oficjum-alandalus-kabala` | 🔴 ** 52.0** | SO dominuje (46.3% vs ideal 33.3%) |
| `3p-oficjum-kabala-gildia` | 🔴 ** 57.9** | GC dominuje (44.8% vs ideal 33.3%) |
| `3p-cienie-korona-kabala` | 🟠 ** 71.6** | KT za słaba (25.6% vs ideal 33.3%) |
| `3p-oficjum-korona-gildia` | 🟠 ** 71.6** | GC dominuje (40.2% vs ideal 33.3%) |
| `3p-korona-kabala-gildia` | 🟠 ** 72.8** | KT za słaba (25.9% vs ideal 33.3%) |
| `3p-cienie-kabala-gildia` | 🟠 ** 73.2** | CAA dominuje (40.6% vs ideal 33.3%) |
| `4p-no-cienie` | 🟡 ** 81.8** | KT dominuje (28.9% vs ideal 25.0%) |
| `3p-oficjum-alandalus-gildia` | 🟡 ** 82.1** | CAA za słaba (28.4% vs ideal 33.3%) |
| `4p-core` | 🟡 ** 85.7** | KB dominuje (28.7% vs ideal 25.0%) |
| `5p-full` | 🟡 ** 86.2** | GC za słaba (17.7% vs ideal 20.0%) |
| `3p-oficjum-korona-kabala` | 🟡 ** 87.2** | KT dominuje (36.7% vs ideal 33.3%) |
| `3p-cienie-korona-gildia` | 🟡 ** 88.2** | GC dominuje (36.6% vs ideal 33.3%) |
| `4p-no-kabala` | 🟡 ** 89.9** | SO za słaba (22.3% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 1** | 0 |   0.0% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 2** | 155 |   0.1% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 3,330 |   2.1% | `█                   ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 14,520 |   9.1% | `█████               ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 34,737 |  21.8% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 42,869 |  26.9% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 36,074 |  22.6% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 16,458 |  10.3% | `█████               ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 6,333 |   4.0% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 3,703 |   2.3% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 746 |   0.5% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 498 |   0.3% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 1** | 0 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 2** | 155 | 10 | 145 | 0 | 0 | 0 | **CAA (145)** |
| **Era 3** | 3,330 | 363 | 1,148 | 1,177 | 623 | 19 | **KB (1,177)** |
| **Era 4** | 14,520 | 1,802 | 4,190 | 2,141 | 5,238 | 1,149 | **KT (5,238)** |
| **Era 5** | 34,737 | 5,309 | 9,250 | 5,676 | 9,088 | 5,414 | **CAA (9,250)** |
| **Era 6** | 42,869 | 8,237 | 8,547 | 8,393 | 8,408 | 9,284 | **GC (9,284)** |
| **Era 7** | 36,074 | 9,070 | 4,781 | 9,069 | 4,136 | 9,018 | **SO (9,070)** |
| **Era 8** | 16,458 | 3,329 | 1,635 | 2,793 | 1,627 | 7,074 | **GC (7,074)** |
| **Era 9** | 6,333 | 1,796 | 584 | 1,782 | 579 | 1,592 | **SO (1,796)** |
| **Era 10** | 3,703 | 841 | 276 | 1,848 | 142 | 596 | **KB (1,848)** |
| **Era 11** | 746 | 112 | 97 | 290 | 48 | 199 | **KB (290)** |
| **Era 12** | 498 | 95 | 38 | 163 | 50 | 152 | **KB (163)** |
| **SUMA** | **159,423** | **30,964** | **30,691** | **33,332** | **29,939** | **34,497** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **6.00** |  0.1% | 14.3% | 70.5% | 14.8% |  0.3% | **KB (31.9%)** |
| `4p-no-cienie` | **5.74** |  0.0% | 13.0% | 81.4% |  5.6% |  0.0% | **GC (30.2%)** |
| `4p-no-kabala` | **5.69** |  0.2% | 14.5% | 79.8% |  5.5% |  0.0% | **GC (30.9%)** |
| `4p-no-korona` | **5.68** |  0.2% | 15.3% | 78.2% |  6.3% |  0.0% | **GC (31.9%)** |
| `4p-no-oficjum` | **6.10** |  0.1% | 11.8% | 70.8% | 17.0% |  0.3% | **KB (31.2%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **3.5 – 8.5** | 🟡 2.0–3.5 / 8.5–10.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 80 | 🟠 ≥ 65 | 🔴 < 65