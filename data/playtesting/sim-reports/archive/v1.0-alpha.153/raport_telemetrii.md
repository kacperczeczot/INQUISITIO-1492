# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.153

**Wersja Balansu:** `v1.0-alpha.153` | **Data:** 2026-08-30 11:23 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 0.46s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🟠 ** 69.7** | 🟠 69.7 | 33.3% | - | 41.5% | - | 28.3% | 30.3% | 🟠 WYMAGA UWAGI |
| `3p-cienie-korona-gildia` | 3 | 🟡 ** 85.4** | 🟡 85.4 | 33.3% | - | 33.8% | 29.4% | - | 36.8% | 🟡 AKCEPTOWALNY |
| `3p-cienie-korona-kabala` | 3 | 🟠 ** 70.9** | 🟠 70.9 | 33.3% | - | 37.5% | 37.0% | 25.4% | - | 🟠 WYMAGA UWAGI |
| `3p-korona-kabala-gildia` | 3 | 🟠 ** 71.7** | 🟠 71.7 | 33.3% | - | - | 37.3% | 25.6% | 37.1% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-alandalus-gildia` | 3 | 🟡 ** 86.7** | 🟡 86.7 | 33.3% | 34.6% | 29.5% | - | - | 35.9% | 🟡 AKCEPTOWALNY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 54.3** | 🔴 54.3 | 33.3% | 45.7% | 25.4% | - | 28.8% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 ** 52.5** | 🔴 52.5 | 33.3% | 33.7% | 21.8% | 44.5% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 ** 59.4** | 🔴 59.4 | 33.3% | 27.1% | - | - | 28.6% | 44.3% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🟠 ** 73.9** | 🟠 73.9 | 33.3% | 27.2% | - | 33.2% | - | 39.6% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-korona-kabala` | 3 | 🟡 ** 87.2** | 🟡 87.2 | 33.3% | 30.1% | - | 33.2% | 36.7% | - | 🟡 AKCEPTOWALNY |
| `4p-core` | 4 | 🟡 ** 85.4** | 🟡 85.4 | 25.0% | 22.4% | 24.1% | 28.6% | 24.9% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟡 ** 83.7** | 🟡 83.7 | 25.0% | 22.7% | - | 22.9% | 28.7% | 25.7% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟡 ** 88.0** | 🟡 88.0 | 25.0% | 21.8% | 25.9% | 25.5% | - | 26.8% | 🟡 AKCEPTOWALNY |
| `4p-no-korona` | 4 | 🟢 ** 99.4** | 🟢 99.4 | 25.0% | 24.9% | 25.1% | - | 25.2% | 24.8% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟢 ** 99.5** | 🟢 99.5 | 25.0% | - | 24.9% | 24.9% | 25.0% | 25.2% | 🟢 ZBALANSOWANY |
| `5p-full` | 5 | 🟢 ** 90.4** | 🟢 90.4 | 20.0% | 19.7% | 21.9% | 18.9% | 20.9% | 18.5% | 🟢 ZBALANSOWANY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.5 🟢 | 0.2% 🟢 | 1.0% 🟢 | 1.22 🟢 | 6.17 🟢 | 8.55zł | 5.77 | 🟢 OPTYMALNA |
| `3p-cienie-korona-gildia` | 6.77 🟡 | 0.0% 🟢 | 2.9% 🟢 | 1.24 🟢 | 7.39 🟢 | 8.51zł | 6.55 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.16 🔴 | 0.8% 🟢 | 4.2% 🟢 | 1.32 🟢 | 6.23 🟢 | 6.24zł | 5.82 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.78 🟡 | 0.1% 🟢 | 5.0% 🟢 | 1.25 🟢 | 6.55 🟢 | 3.55zł | 5.99 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-gildia` | 6.11 🟢 | 0.0% 🟢 | 0.0% 🟢 | 1.81 🟡 | 7.56 🟢 | 10.19zł | 6.95 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 6.6 🟡 | 0.0% 🟢 | 0.4% 🟢 | 2.08 🔴 | 7.43 🟢 | 8.03zł | 6.45 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 6.54 🟡 | 0.0% 🟢 | 2.1% 🟢 | 2.03 🔴 | 7.41 🟢 | 7.33zł | 6.75 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 6.2 🟢 | 0.0% 🟢 | 0.6% 🟢 | 1.84 🟡 | 7.68 🟢 | 5.38zł | 6.8 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-gildia` | 6.14 🟢 | 0.0% 🟢 | 2.3% 🟢 | 1.75 🟢 | 7.6 🟢 | 4.98zł | 7.15 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 6.63 🟡 | 0.0% 🟢 | 3.1% 🟢 | 2.04 🔴 | 7.16 🟢 | 2.91zł | 6.42 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.01 🟢 | 0.0% 🟢 | 3.3% 🟢 | 1.87 🟡 | 7.45 🟢 | 7.26zł | 7.82 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.73 🟢 | 0.0% 🟢 | 3.5% 🟢 | 1.74 🟢 | 7.61 🟢 | 4.88zł | 8.31 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.71 🟢 | 0.0% 🟢 | 2.6% 🟢 | 1.7 🟢 | 7.81 🟢 | 8.94zł | 8.42 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.71 🟢 | 0.0% 🟢 | 0.5% 🟢 | 1.78 🟢 | 7.69 🟢 | 9.46zł | 8.21 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 6.14 🟢 | 0.0% 🟢 | 4.4% 🟢 | 1.13 🟢 | 6.86 🟢 | 7.72zł | 7.47 | 🟢 OPTYMALNA |
| `5p-full` | 5.41 🟢 | 0.0% 🟢 | 3.8% 🟢 | 1.64 🟢 | 7.6 🟢 | 8.92zł | 9.48 | 🟢 OPTYMALNA |

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
| **SO** | 28.2% | `3p-oficjum-alandalus-kabala` | +12.4% | 🟡 DOMINUJE |
| **CAA** | 28.3% | `3p-oficjum-alandalus-korona` | -11.5% | 🟡 SŁABA |
| **KB** | 30.5% | `3p-oficjum-alandalus-korona` | +11.2% | 🟡 DOMINUJE |
| **GC** | 31.4% | `3p-oficjum-kabala-gildia` | +11.0% | 🟡 DOMINUJE |
| **KT** | 27.1% | `3p-cienie-korona-kabala` | -7.9% | 🟡 SŁABA |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `3p-oficjum-alandalus-korona` | 🔴 ** 52.5** | CAA za słaba (21.8% vs ideal 33.3%) |
| `3p-oficjum-alandalus-kabala` | 🔴 ** 54.3** | SO dominuje (45.7% vs ideal 33.3%) |
| `3p-oficjum-kabala-gildia` | 🔴 ** 59.4** | GC dominuje (44.3% vs ideal 33.3%) |
| `3p-cienie-kabala-gildia` | 🟠 ** 69.7** | CAA dominuje (41.5% vs ideal 33.3%) |
| `3p-cienie-korona-kabala` | 🟠 ** 70.9** | KT za słaba (25.4% vs ideal 33.3%) |
| `3p-korona-kabala-gildia` | 🟠 ** 71.7** | KT za słaba (25.6% vs ideal 33.3%) |
| `3p-oficjum-korona-gildia` | 🟠 ** 73.9** | GC dominuje (39.6% vs ideal 33.3%) |
| `4p-no-cienie` | 🟡 ** 83.7** | KT dominuje (28.7% vs ideal 25.0%) |
| `3p-cienie-korona-gildia` | 🟡 ** 85.4** | KB za słaba (29.4% vs ideal 33.3%) |
| `4p-core` | 🟡 ** 85.4** | KB dominuje (28.6% vs ideal 25.0%) |
| `3p-oficjum-alandalus-gildia` | 🟡 ** 86.7** | CAA za słaba (29.5% vs ideal 33.3%) |
| `3p-oficjum-korona-kabala` | 🟡 ** 87.2** | KT dominuje (36.7% vs ideal 33.3%) |
| `4p-no-kabala` | 🟡 ** 88.0** | SO za słaba (21.8% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 1** | 0 |   0.0% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 2** | 105 |   0.1% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 3,172 |   2.0% | `█                   ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 14,393 |   9.0% | `█████               ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 34,851 |  21.9% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 42,698 |  26.8% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 36,098 |  22.6% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 16,651 |  10.4% | `█████               ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 6,444 |   4.0% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 3,731 |   2.3% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 753 |   0.5% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 541 |   0.3% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 1** | 0 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 2** | 105 | 14 | 91 | 0 | 0 | 0 | **CAA (91)** |
| **Era 3** | 3,172 | 357 | 1,040 | 1,156 | 600 | 19 | **KB (1,156)** |
| **Era 4** | 14,393 | 1,784 | 4,082 | 2,205 | 5,145 | 1,177 | **KT (5,145)** |
| **Era 5** | 34,851 | 5,244 | 9,371 | 5,755 | 8,859 | 5,622 | **CAA (9,371)** |
| **Era 6** | 42,698 | 8,169 | 8,702 | 8,201 | 8,399 | 9,227 | **GC (9,227)** |
| **Era 7** | 36,098 | 9,089 | 4,941 | 8,841 | 4,253 | 8,974 | **SO (9,089)** |
| **Era 8** | 16,651 | 3,420 | 1,785 | 2,891 | 1,639 | 6,916 | **GC (6,916)** |
| **Era 9** | 6,444 | 1,838 | 650 | 1,805 | 585 | 1,566 | **SO (1,838)** |
| **Era 10** | 3,731 | 830 | 308 | 1,898 | 129 | 566 | **KB (1,898)** |
| **Era 11** | 753 | 116 | 118 | 285 | 42 | 192 | **KB (285)** |
| **Era 12** | 541 | 104 | 47 | 174 | 50 | 166 | **KB (174)** |
| **SUMA** | **159,437** | **30,965** | **31,135** | **33,211** | **29,701** | **34,425** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **6.01** |  0.1% | 14.2% | 70.3% | 15.2% |  0.2% | **KB (32.0%)** |
| `4p-no-cienie` | **5.73** |  0.0% | 13.2% | 81.2% |  5.6% |  0.0% | **GC (30.7%)** |
| `4p-no-kabala` | **5.71** |  0.1% | 14.4% | 79.5% |  5.9% |  0.0% | **GC (30.6%)** |
| `4p-no-korona` | **5.71** |  0.1% | 14.2% | 79.2% |  6.4% |  0.0% | **GC (32.1%)** |
| `4p-no-oficjum` | **6.14** |  0.0% | 11.2% | 70.7% | 17.8% |  0.3% | **KB (30.3%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **3.5 – 8.5** | 🟡 2.0–3.5 / 8.5–10.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 80 | 🟠 ≥ 65 | 🔴 < 65