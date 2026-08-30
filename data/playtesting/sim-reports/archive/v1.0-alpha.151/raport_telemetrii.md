# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.151

**Wersja Balansu:** `v1.0-alpha.151` | **Data:** 2026-08-30 10:54 | **Wielkość Próby:** 100000 gier/setup (1600000 gier łącznie) | **Czas Symulacji:** 6.16s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🟠 ** 72.7** | 🟠 72.7 | 33.3% | - | 40.7% | - | 28.6% | 30.7% | 🟠 WYMAGA UWAGI |
| `3p-cienie-korona-gildia` | 3 | 🟡 ** 86.1** | 🟡 86.1 | 33.3% | - | 33.6% | 29.7% | - | 36.7% | 🟡 AKCEPTOWALNY |
| `3p-cienie-korona-kabala` | 3 | 🟠 ** 71.1** | 🟠 71.1 | 33.3% | - | 37.3% | 37.2% | 25.5% | - | 🟠 WYMAGA UWAGI |
| `3p-korona-kabala-gildia` | 3 | 🟠 ** 72.6** | 🟠 72.6 | 33.3% | - | - | 36.4% | 25.9% | 37.7% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-alandalus-gildia` | 3 | 🟡 ** 84.7** | 🟡 84.7 | 33.3% | 34.7% | 29.0% | - | - | 36.3% | 🟡 AKCEPTOWALNY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 52.0** | 🔴 52.0 | 33.3% | 46.5% | 25.6% | - | 27.9% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 ** 52.3** | 🔴 52.3 | 33.3% | 32.8% | 22.2% | 45.0% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 ** 56.6** | 🔴 56.6 | 33.3% | 26.7% | - | - | 28.2% | 45.1% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🟠 ** 75.4** | 🟠 75.4 | 33.3% | 27.3% | - | 33.7% | - | 39.0% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-korona-kabala` | 3 | 🟡 ** 85.9** | 🟡 85.9 | 33.3% | 29.5% | - | 33.9% | 36.6% | - | 🟡 AKCEPTOWALNY |
| `4p-core` | 4 | 🟡 ** 84.7** | 🟡 84.7 | 25.0% | 22.5% | 23.8% | 28.8% | 24.8% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟡 ** 83.3** | 🟡 83.3 | 25.0% | 22.2% | - | 23.2% | 28.7% | 25.9% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟡 ** 88.0** | 🟡 88.0 | 25.0% | 21.9% | 25.6% | 25.6% | - | 27.0% | 🟡 AKCEPTOWALNY |
| `4p-no-korona` | 4 | 🟢 ** 97.2** | 🟢 97.2 | 25.0% | 24.3% | 25.9% | - | 24.8% | 25.1% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟢 ** 97.4** | 🟢 97.4 | 25.0% | - | 24.2% | 25.2% | 24.9% | 25.7% | 🟢 ZBALANSOWANY |
| `5p-full` | 5 | 🟡 ** 87.5** | 🟡 87.5 | 20.0% | 19.8% | 22.3% | 19.4% | 21.0% | 17.6% | 🟡 AKCEPTOWALNY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.51 🟡 | 0.2% 🟢 | 1.0% 🟢 | 1.22 🟢 | 6.2 🟢 | 8.58zł | 5.78 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 6.75 🟡 | 0.0% 🟢 | 2.9% 🟢 | 1.24 🟢 | 7.36 🟢 | 8.48zł | 6.54 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.15 🔴 | 0.8% 🟢 | 4.2% 🟢 | 1.32 🟢 | 6.21 🟢 | 6.23zł | 5.82 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.78 🟡 | 0.1% 🟢 | 5.1% 🟢 | 1.26 🟢 | 6.57 🟢 | 3.57zł | 6.0 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-gildia` | 6.11 🟢 | 0.0% 🟢 | 0.0% 🟢 | 1.81 🟡 | 7.58 🟢 | 10.2zł | 6.95 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 6.6 🟡 | 0.0% 🟢 | 0.3% 🟢 | 2.08 🔴 | 7.44 🟢 | 8.04zł | 6.45 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 6.53 🟡 | 0.0% 🟢 | 2.1% 🟢 | 2.01 🔴 | 7.35 🟢 | 7.33zł | 6.75 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 6.21 🟢 | 0.0% 🟢 | 0.6% 🟢 | 1.84 🟡 | 7.71 🟢 | 5.4zł | 6.81 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-gildia` | 6.17 🟢 | 0.0% 🟢 | 2.3% 🟢 | 1.76 🟢 | 7.63 🟢 | 5.01zł | 7.16 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 6.61 🟡 | 0.0% 🟢 | 3.1% 🟢 | 2.04 🔴 | 7.09 🟢 | 2.91zł | 6.41 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.02 🟢 | 0.0% 🟢 | 3.3% 🟢 | 1.88 🟡 | 7.46 🟢 | 7.26zł | 7.83 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.74 🟢 | 0.0% 🟢 | 3.6% 🟢 | 1.74 🟢 | 7.63 🟢 | 4.89zł | 8.3 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.71 🟢 | 0.0% 🟢 | 2.6% 🟢 | 1.7 🟢 | 7.78 🟢 | 8.92zł | 8.42 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.7 🟢 | 0.0% 🟢 | 0.5% 🟢 | 1.78 🟢 | 7.68 🟢 | 9.45zł | 8.21 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 6.15 🟢 | 0.0% 🟢 | 4.5% 🟢 | 1.13 🟢 | 6.9 🟢 | 7.75zł | 7.48 | 🟢 OPTYMALNA |
| `5p-full` | 5.4 🟢 | 0.0% 🟢 | 3.8% 🟢 | 1.63 🟢 | 7.55 🟢 | 8.89zł | 9.47 | 🟢 OPTYMALNA |

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
| **SO** | 28.0% | `3p-oficjum-alandalus-kabala` | +13.2% | 🟡 DOMINUJE |
| **GC** | 31.5% | `3p-oficjum-kabala-gildia` | +11.8% | 🟡 DOMINUJE |
| **KB** | 30.7% | `3p-oficjum-alandalus-korona` | +11.7% | 🟡 DOMINUJE |
| **CAA** | 28.2% | `3p-oficjum-alandalus-korona` | -11.1% | 🟡 SŁABA |
| **KT** | 27.0% | `3p-cienie-korona-kabala` | -7.8% | 🟡 SŁABA |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `3p-oficjum-alandalus-kabala` | 🔴 ** 52.0** | SO dominuje (46.5% vs ideal 33.3%) |
| `3p-oficjum-alandalus-korona` | 🔴 ** 52.3** | KB dominuje (45.0% vs ideal 33.3%) |
| `3p-oficjum-kabala-gildia` | 🔴 ** 56.6** | GC dominuje (45.1% vs ideal 33.3%) |
| `3p-cienie-korona-kabala` | 🟠 ** 71.1** | KT za słaba (25.5% vs ideal 33.3%) |
| `3p-korona-kabala-gildia` | 🟠 ** 72.6** | KT za słaba (25.9% vs ideal 33.3%) |
| `3p-cienie-kabala-gildia` | 🟠 ** 72.7** | CAA dominuje (40.7% vs ideal 33.3%) |
| `3p-oficjum-korona-gildia` | 🟠 ** 75.4** | SO za słaba (27.3% vs ideal 33.3%) |
| `4p-no-cienie` | 🟡 ** 83.3** | KT dominuje (28.7% vs ideal 25.0%) |
| `3p-oficjum-alandalus-gildia` | 🟡 ** 84.7** | CAA za słaba (29.0% vs ideal 33.3%) |
| `4p-core` | 🟡 ** 84.7** | KB dominuje (28.8% vs ideal 25.0%) |
| `3p-oficjum-korona-kabala` | 🟡 ** 85.9** | SO za słaba (29.5% vs ideal 33.3%) |
| `3p-cienie-korona-gildia` | 🟡 ** 86.1** | KB za słaba (29.7% vs ideal 33.3%) |
| `5p-full` | 🟡 ** 87.5** | GC za słaba (17.6% vs ideal 20.0%) |
| `4p-no-kabala` | 🟡 ** 88.0** | SO za słaba (21.9% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 1** | 0 |   0.0% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 2** | 1,191 |   0.1% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 31,585 |   2.0% | `█                   ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 143,590 |   9.0% | `█████               ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 344,303 |  21.6% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 430,387 |  27.0% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 363,702 |  22.8% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 166,732 |  10.5% | `█████               ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 63,588 |   4.0% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 36,292 |   2.3% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 7,785 |   0.5% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 5,249 |   0.3% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 1** | 0 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 2** | 1,191 | 192 | 997 | 0 | 2 | 0 | **CAA (997)** |
| **Era 3** | 31,585 | 3,135 | 10,386 | 11,376 | 6,522 | 166 | **KB (11,376)** |
| **Era 4** | 143,590 | 17,421 | 41,232 | 22,806 | 50,115 | 12,016 | **KT (50,115)** |
| **Era 5** | 344,303 | 51,620 | 90,407 | 56,798 | 88,588 | 56,890 | **CAA (90,407)** |
| **Era 6** | 430,387 | 82,101 | 87,951 | 85,332 | 83,701 | 91,302 | **GC (91,302)** |
| **Era 7** | 363,702 | 91,674 | 50,330 | 89,328 | 41,991 | 90,379 | **SO (91,674)** |
| **Era 8** | 166,732 | 33,459 | 17,687 | 28,171 | 16,866 | 70,549 | **GC (70,549)** |
| **Era 9** | 63,588 | 17,994 | 6,588 | 17,979 | 5,705 | 15,322 | **SO (17,994)** |
| **Era 10** | 36,292 | 7,861 | 2,831 | 18,606 | 1,333 | 5,661 | **KB (18,606)** |
| **Era 11** | 7,785 | 1,374 | 1,238 | 2,858 | 444 | 1,871 | **KB (2,858)** |
| **Era 12** | 5,249 | 1,016 | 408 | 1,632 | 410 | 1,783 | **GC (1,783)** |
| **SUMA** | **1,594,404** | **307,847** | **310,055** | **334,886** | **295,677** | **345,939** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **6.02** |  0.1% | 14.3% | 70.1% | 15.2% |  0.3% | **KB (31.8%)** |
| `4p-no-cienie` | **5.74** |  0.0% | 12.8% | 81.6% |  5.6% |  0.0% | **GC (30.0%)** |
| `4p-no-kabala` | **5.71** |  0.2% | 14.2% | 79.9% |  5.7% |  0.0% | **GC (30.2%)** |
| `4p-no-korona` | **5.70** |  0.1% | 14.5% | 78.8% |  6.5% |  0.0% | **GC (31.9%)** |
| `4p-no-oficjum` | **6.15** |  0.1% | 11.0% | 70.7% | 17.9% |  0.3% | **KB (31.9%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **3.5 – 8.5** | 🟡 2.0–3.5 / 8.5–10.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 80 | 🟠 ≥ 65 | 🔴 < 65