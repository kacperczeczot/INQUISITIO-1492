# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.164

**Wersja Balansu:** `v1.0-alpha.164` | **Data:** 2026-08-30 12:12 | **Wielkość Próby:** 100000 gier/setup (1600000 gier łącznie) | **Czas Symulacji:** 6.17s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🟠 ** 78.6** | 🟠 78.6 | 33.3% | - | 39.2% | - | 29.5% | 31.3% | 🟠 WYMAGA UWAGI |
| `3p-cienie-korona-gildia` | 3 | 🟡 ** 89.3** | 🟡 89.3 | 33.3% | - | 32.0% | 31.4% | - | 36.6% | 🟡 AKCEPTOWALNY |
| `3p-cienie-korona-kabala` | 3 | 🟠 ** 70.2** | 🟠 70.2 | 33.3% | - | 35.5% | 39.0% | 25.5% | - | 🟠 WYMAGA UWAGI |
| `3p-korona-kabala-gildia` | 3 | 🟠 ** 72.0** | 🟠 72.0 | 33.3% | - | - | 36.8% | 25.7% | 37.5% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-alandalus-gildia` | 3 | 🟡 ** 82.4** | 🟡 82.4 | 33.3% | 36.1% | 28.4% | - | - | 35.5% | 🟡 AKCEPTOWALNY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 49.3** | 🔴 49.3 | 33.3% | 47.3% | 24.6% | - | 28.2% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 ** 51.9** | 🔴 51.9 | 33.3% | 32.9% | 22.1% | 45.1% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 ** 59.6** | 🔴 59.6 | 33.3% | 27.5% | - | - | 28.2% | 44.3% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🟡 ** 80.5** | 🟡 80.5 | 33.3% | 28.6% | - | 33.3% | - | 38.1% | 🟡 AKCEPTOWALNY |
| `3p-oficjum-korona-kabala` | 3 | 🟡 ** 86.2** | 🟡 86.2 | 33.3% | 29.4% | - | 34.6% | 36.0% | - | 🟡 AKCEPTOWALNY |
| `4p-core` | 4 | 🟡 ** 82.4** | 🟡 82.4 | 25.0% | 22.5% | 23.7% | 29.5% | 24.3% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟡 ** 83.7** | 🟡 83.7 | 25.0% | 21.8% | - | 23.7% | 28.3% | 26.3% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟢 ** 90.7** | 🟢 90.7 | 25.0% | 22.5% | 25.0% | 25.8% | - | 26.6% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟢 ** 97.2** | 🟢 97.2 | 25.0% | 24.2% | 25.1% | - | 24.9% | 25.8% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟢 ** 93.2** | 🟢 93.2 | 25.0% | - | 23.0% | 26.0% | 25.3% | 25.7% | 🟢 ZBALANSOWANY |
| `5p-full` | 5 | 🟢 ** 92.2** | 🟢 92.2 | 20.0% | 19.6% | 21.2% | 20.0% | 21.0% | 18.2% | 🟢 ZBALANSOWANY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.53 🟡 | 0.2% 🟢 | 1.0% 🟢 | 1.23 🟢 | 6.23 🟢 | 8.27zł | 5.78 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 6.78 🟡 | 0.0% 🟢 | 2.9% 🟢 | 1.24 🟢 | 7.44 🟢 | 8.46zł | 6.54 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.21 🔴 | 0.9% 🟢 | 4.2% 🟢 | 1.33 🟢 | 6.27 🟢 | 6.14zł | 5.82 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.8 🟡 | 0.1% 🟢 | 5.0% 🟢 | 1.26 🟢 | 6.62 🟢 | 3.58zł | 5.98 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-gildia` | 6.12 🟢 | 0.0% 🟢 | 0.0% 🟢 | 1.79 🟢 | 7.58 🟢 | 10.16zł | 6.94 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 6.67 🟡 | 0.1% 🟢 | 0.3% 🟢 | 2.07 🔴 | 7.54 🟢 | 7.95zł | 6.46 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 6.55 🟡 | 0.0% 🟢 | 2.1% 🟢 | 2.0 🟡 | 7.31 🟢 | 7.44zł | 6.74 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 6.2 🟢 | 0.0% 🟢 | 0.6% 🟢 | 1.8 🟢 | 7.68 🟢 | 5.49zł | 6.78 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-gildia` | 6.17 🟢 | 0.0% 🟢 | 2.3% 🟢 | 1.73 🟢 | 7.65 🟢 | 5.16zł | 7.15 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 6.63 🟡 | 0.0% 🟢 | 3.1% 🟢 | 2.01 🔴 | 7.13 🟢 | 2.93zł | 6.4 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.05 🟢 | 0.0% 🟢 | 3.3% 🟢 | 1.87 🟡 | 7.47 🟢 | 7.32zł | 7.83 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.76 🟢 | 0.0% 🟢 | 3.6% 🟢 | 1.73 🟢 | 7.66 🟢 | 4.97zł | 8.28 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.72 🟢 | 0.0% 🟢 | 2.6% 🟢 | 1.69 🟢 | 7.79 🟢 | 9.08zł | 8.41 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.73 🟢 | 0.0% 🟢 | 0.5% 🟢 | 1.77 🟢 | 7.74 🟢 | 9.36zł | 8.2 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 6.18 🟢 | 0.0% 🟢 | 4.4% 🟢 | 1.14 🟢 | 6.89 🟢 | 7.75zł | 7.45 | 🟢 OPTYMALNA |
| `5p-full` | 5.42 🟢 | 0.0% 🟢 | 3.8% 🟢 | 1.62 🟢 | 7.57 🟢 | 8.98zł | 9.45 | 🟢 OPTYMALNA |

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
| **SO** | 28.4% | `3p-oficjum-alandalus-kabala` | +14.0% | 🟡 DOMINUJE |
| **KB** | 31.4% | `3p-oficjum-alandalus-korona` | +11.8% | 🟡 DOMINUJE |
| **CAA** | 27.3% | `3p-oficjum-alandalus-korona` | -11.2% | 🟡 SŁABA |
| **GC** | 31.4% | `3p-oficjum-kabala-gildia` | +11.0% | 🟡 DOMINUJE |
| **KT** | 27.0% | `3p-cienie-korona-kabala` | -7.8% | 🟡 SŁABA |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `3p-oficjum-alandalus-kabala` | 🔴 ** 49.3** | SO dominuje (47.3% vs ideal 33.3%) |
| `3p-oficjum-alandalus-korona` | 🔴 ** 51.9** | KB dominuje (45.1% vs ideal 33.3%) |
| `3p-oficjum-kabala-gildia` | 🔴 ** 59.6** | GC dominuje (44.3% vs ideal 33.3%) |
| `3p-cienie-korona-kabala` | 🟠 ** 70.2** | KT za słaba (25.5% vs ideal 33.3%) |
| `3p-korona-kabala-gildia` | 🟠 ** 72.0** | KT za słaba (25.7% vs ideal 33.3%) |
| `3p-cienie-kabala-gildia` | 🟠 ** 78.6** | CAA dominuje (39.2% vs ideal 33.3%) |
| `3p-oficjum-korona-gildia` | 🟡 ** 80.5** | GC dominuje (38.1% vs ideal 33.3%) |
| `3p-oficjum-alandalus-gildia` | 🟡 ** 82.4** | CAA za słaba (28.4% vs ideal 33.3%) |
| `4p-core` | 🟡 ** 82.4** | KB dominuje (29.5% vs ideal 25.0%) |
| `4p-no-cienie` | 🟡 ** 83.7** | KT dominuje (28.3% vs ideal 25.0%) |
| `3p-oficjum-korona-kabala` | 🟡 ** 86.2** | SO za słaba (29.4% vs ideal 33.3%) |
| `3p-cienie-korona-gildia` | 🟡 ** 89.3** | GC dominuje (36.6% vs ideal 33.3%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 1** | 0 |   0.0% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 2** | 876 |   0.1% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 32,060 |   2.0% | `█                   ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 142,870 |   9.0% | `████                ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 337,391 |  21.2% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 427,927 |  26.9% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 365,942 |  23.0% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 168,414 |  10.6% | `█████               ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 66,081 |   4.1% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 38,241 |   2.4% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 8,365 |   0.5% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 5,554 |   0.3% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 1** | 0 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 2** | 876 | 220 | 653 | 0 | 3 | 0 | **CAA (653)** |
| **Era 3** | 32,060 | 3,573 | 9,700 | 11,904 | 6,705 | 178 | **KB (11,904)** |
| **Era 4** | 142,870 | 17,177 | 38,946 | 23,438 | 51,420 | 11,889 | **KT (51,420)** |
| **Era 5** | 337,391 | 50,186 | 86,785 | 57,439 | 86,688 | 56,293 | **CAA (86,785)** |
| **Era 6** | 427,927 | 83,289 | 86,100 | 86,080 | 81,770 | 90,688 | **GC (90,688)** |
| **Era 7** | 365,942 | 93,216 | 49,153 | 91,213 | 42,611 | 89,749 | **SO (93,216)** |
| **Era 8** | 168,414 | 33,878 | 17,239 | 28,692 | 18,010 | 70,595 | **GC (70,595)** |
| **Era 9** | 66,081 | 18,841 | 6,467 | 18,723 | 6,230 | 15,820 | **SO (18,841)** |
| **Era 10** | 38,241 | 8,712 | 2,855 | 19,434 | 1,292 | 5,948 | **KB (19,434)** |
| **Era 11** | 8,365 | 1,554 | 1,264 | 3,041 | 515 | 1,991 | **KB (3,041)** |
| **Era 12** | 5,554 | 1,120 | 410 | 1,741 | 422 | 1,861 | **GC (1,861)** |
| **SUMA** | **1,593,721** | **311,766** | **299,572** | **341,705** | **295,666** | **345,012** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **6.05** |  0.1% | 14.4% | 69.4% | 15.8% |  0.3% | **KB (32.3%)** |
| `4p-no-cienie` | **5.76** |  0.0% | 12.8% | 81.2% |  6.0% |  0.0% | **GC (30.1%)** |
| `4p-no-kabala` | **5.72** |  0.1% | 14.1% | 79.7% |  6.0% |  0.0% | **GC (29.9%)** |
| `4p-no-korona` | **5.73** |  0.1% | 14.2% | 79.0% |  6.7% |  0.0% | **GC (32.1%)** |
| `4p-no-oficjum` | **6.18** |  0.1% | 11.0% | 70.2% | 18.5% |  0.3% | **KB (33.2%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **3.5 – 8.5** | 🟡 2.0–3.5 / 8.5–10.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 80 | 🟠 ≥ 65 | 🔴 < 65