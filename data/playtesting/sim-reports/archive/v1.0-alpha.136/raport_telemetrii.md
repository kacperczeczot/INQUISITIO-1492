# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.136

**Wersja Balansu:** `v1.0-alpha.136` | **Data:** 2026-08-30 09:30 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 0.56s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🟠 ** 67.1** | 🟠 67.1 | 33.3% | - | 42.2% | - | 28.0% | 29.8% | 🟠 WYMAGA UWAGI |
| `3p-cienie-korona-gildia` | 3 | 🟢 ** 96.0** | 🟢 96.0 | 33.3% | - | 32.2% | 33.1% | - | 34.7% | 🟢 ZBALANSOWANY |
| `3p-cienie-korona-kabala` | 3 | 🔴 ** 58.2** | 🔴 58.2 | 33.3% | - | 34.1% | 42.8% | 23.1% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🟠 ** 67.8** | 🟠 67.8 | 33.3% | - | - | 39.2% | 24.8% | 36.0% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-alandalus-gildia` | 3 | 🟠 ** 66.1** | 🟠 66.1 | 33.3% | 41.9% | 26.2% | - | - | 32.0% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 43.4** | 🔴 43.4 | 33.3% | 48.9% | 21.8% | - | 29.3% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 ** 44.0** | 🔴 44.0 | 33.3% | 35.6% | 18.6% | 45.8% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 ** 55.2** | 🔴 55.2 | 33.3% | 34.3% | - | - | 22.3% | 43.4% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🟢 ** 95.7** | 🟢 95.7 | 33.3% | 34.5% | - | 33.6% | - | 31.9% | 🟢 ZBALANSOWANY |
| `3p-oficjum-korona-kabala` | 3 | 🟢 ** 98.1** | 🟢 98.1 | 33.3% | 33.5% | - | 33.9% | 32.6% | - | 🟢 ZBALANSOWANY |
| `4p-core` | 4 | 🟠 ** 79.3** | 🟠 79.3 | 25.0% | 26.0% | 20.4% | 28.9% | 24.6% | - | 🟠 WYMAGA UWAGI |
| `4p-no-cienie` | 4 | 🟡 ** 86.8** | 🟡 86.8 | 25.0% | 25.0% | - | 23.6% | 28.3% | 23.1% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟡 ** 84.9** | 🟡 84.9 | 25.0% | 28.4% | 23.0% | 25.9% | - | 22.7% | 🟡 AKCEPTOWALNY |
| `4p-no-korona` | 4 | 🟠 ** 79.2** | 🟠 79.2 | 25.0% | 30.0% | 24.0% | - | 24.4% | 21.6% | 🟠 WYMAGA UWAGI |
| `4p-no-oficjum` | 4 | 🟢 ** 91.7** | 🟢 91.7 | 25.0% | - | 23.3% | 27.1% | 24.4% | 25.1% | 🟢 ZBALANSOWANY |
| `5p-full` | 5 | 🟠 ** 73.3** | 🟠 73.3 | 20.0% | 24.9% | 20.8% | 18.0% | 20.7% | 15.7% | 🟠 WYMAGA UWAGI |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.68 🟡 | 0.1% 🟢 | 1.4% 🟢 | 1.26 🟢 | 6.59 🟢 | 10.01zł | 5.99 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 6.89 🟡 | 0.0% 🟢 | 4.0% 🟢 | 1.27 🟢 | 7.57 🟢 | 9.98zł | 6.58 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.26 🔴 | 0.6% 🟢 | 5.3% 🟢 | 1.33 🟢 | 6.6 🟢 | 7.56zł | 5.98 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 7.09 🔴 | 0.1% 🟢 | 6.9% 🟢 | 1.32 🟢 | 7.15 🟢 | 3.76zł | 6.04 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-gildia` | 6.12 🟢 | 0.0% 🟢 | 0.6% 🟢 | 1.81 🟡 | 8.04 🟢 | 11.27zł | 7.12 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 6.58 🟡 | 0.0% 🟢 | 0.9% 🟢 | 2.06 🔴 | 7.98 🟢 | 8.84zł | 6.61 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 6.57 🟡 | 0.0% 🟢 | 3.5% 🟢 | 2.02 🔴 | 7.89 🟢 | 8.5zł | 6.88 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 6.43 🟢 | 0.0% 🟢 | 1.5% 🟢 | 1.83 🟡 | 8.6 🟡 | 5.5zł | 6.96 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-gildia` | 6.3 🟢 | 0.0% 🟢 | 4.1% 🟢 | 1.78 🟢 | 8.03 🟢 | 5.29zł | 7.24 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 6.67 🟡 | 0.0% 🟢 | 4.7% 🟢 | 2.03 🔴 | 7.51 🟢 | 2.87zł | 6.49 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.02 🟢 | 0.0% 🟢 | 4.9% 🟢 | 1.88 🟡 | 7.89 🟢 | 8.33zł | 8.06 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.8 🟢 | 0.0% 🟢 | 5.7% 🟢 | 1.75 🟢 | 8.0 🟢 | 4.89zł | 8.38 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.72 🟢 | 0.0% 🟢 | 4.5% 🟢 | 1.71 🟢 | 8.29 🟢 | 10.12zł | 8.67 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.63 🟢 | 0.0% 🟢 | 1.3% 🟢 | 1.73 🟢 | 8.1 🟢 | 10.17zł | 8.44 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 6.21 🟢 | 0.0% 🟢 | 5.8% 🟢 | 1.16 🟢 | 7.13 🟢 | 8.97zł | 7.6 | 🟢 OPTYMALNA |
| `5p-full` | 5.4 🟢 | 0.0% 🟢 | 5.6% 🟢 | 1.62 🟢 | 7.93 🟢 | 9.89zł | 9.78 | 🟢 OPTYMALNA |

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
| **SO** | 33.0% | `3p-oficjum-alandalus-kabala` | +15.6% | 🟡 DOMINUJE |
| **CAA** | 26.1% | `3p-oficjum-alandalus-korona` | -14.7% | 🟡 SŁABA |
| **KB** | 32.0% | `3p-oficjum-alandalus-korona` | +12.5% | 🟡 DOMINUJE |
| **KT** | 25.7% | `3p-oficjum-kabala-gildia` | -11.0% | 🟡 SŁABA |
| **GC** | 28.7% | `3p-oficjum-kabala-gildia` | +10.1% | 🟡 DOMINUJE |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `3p-oficjum-alandalus-kabala` | 🔴 ** 43.4** | SO dominuje (48.9% vs ideal 33.3%) |
| `3p-oficjum-alandalus-korona` | 🔴 ** 44.0** | CAA za słaba (18.6% vs ideal 33.3%) |
| `3p-oficjum-kabala-gildia` | 🔴 ** 55.2** | KT za słaba (22.3% vs ideal 33.3%) |
| `3p-cienie-korona-kabala` | 🔴 ** 58.2** | KT za słaba (23.1% vs ideal 33.3%) |
| `3p-oficjum-alandalus-gildia` | 🟠 ** 66.1** | SO dominuje (41.9% vs ideal 33.3%) |
| `3p-cienie-kabala-gildia` | 🟠 ** 67.1** | CAA dominuje (42.2% vs ideal 33.3%) |
| `3p-korona-kabala-gildia` | 🟠 ** 67.8** | KT za słaba (24.8% vs ideal 33.3%) |
| `5p-full` | 🟠 ** 73.3** | SO dominuje (24.9% vs ideal 20.0%) |
| `4p-no-korona` | 🟠 ** 79.2** | SO dominuje (30.0% vs ideal 25.0%) |
| `4p-core` | 🟠 ** 79.3** | CAA za słaba (20.4% vs ideal 25.0%) |
| `4p-no-kabala` | 🟡 ** 84.9** | SO dominuje (28.4% vs ideal 25.0%) |
| `4p-no-cienie` | 🟡 ** 86.8** | KT dominuje (28.3% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 1** | 0 |   0.0% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 2** | 142 |   0.1% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 2,407 |   1.5% | `█                   ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 14,719 |   9.2% | `█████               ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 32,568 |  20.4% | `██████████          ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 42,446 |  26.6% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 36,139 |  22.7% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 17,785 |  11.2% | `██████              ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 7,435 |   4.7% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 4,257 |   2.7% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 930 |   0.6% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 572 |   0.4% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 1** | 0 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 2** | 142 | 14 | 128 | 0 | 0 | 0 | **CAA (128)** |
| **Era 3** | 2,407 | 378 | 1,175 | 229 | 621 | 4 | **CAA (1,175)** |
| **Era 4** | 14,719 | 2,245 | 4,153 | 2,752 | 4,866 | 703 | **KT (4,866)** |
| **Era 5** | 32,568 | 6,163 | 8,335 | 6,210 | 7,600 | 4,260 | **CAA (8,335)** |
| **Era 6** | 42,446 | 9,809 | 7,863 | 8,659 | 7,930 | 8,185 | **SO (9,809)** |
| **Era 7** | 36,139 | 10,850 | 4,412 | 9,146 | 4,368 | 7,363 | **SO (10,850)** |
| **Era 8** | 17,785 | 3,891 | 1,598 | 3,152 | 1,906 | 7,238 | **GC (7,238)** |
| **Era 9** | 7,435 | 1,833 | 620 | 1,903 | 625 | 2,454 | **GC (2,454)** |
| **Era 10** | 4,257 | 813 | 230 | 2,247 | 157 | 810 | **KB (2,247)** |
| **Era 11** | 930 | 143 | 92 | 354 | 50 | 291 | **KB (354)** |
| **Era 12** | 572 | 111 | 39 | 181 | 46 | 195 | **GC (195)** |
| **SUMA** | **159,400** | **36,250** | **28,645** | **34,833** | **28,169** | **31,503** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **6.02** |  0.1% | 14.2% | 71.2% | 14.1% |  0.3% | **KB (31.6%)** |
| `4p-no-cienie` | **5.80** |  0.0% | 12.6% | 80.7% |  6.7% |  0.0% | **GC (27.6%)** |
| `4p-no-kabala` | **5.72** |  0.2% | 14.2% | 79.7% |  5.9% |  0.0% | **KB (27.5%)** |
| `4p-no-korona` | **5.63** |  0.3% | 16.1% | 77.9% |  5.8% |  0.0% | **GC (28.8%)** |
| `4p-no-oficjum` | **6.21** |  0.1% | 11.5% | 67.8% | 20.3% |  0.2% | **KB (35.7%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **3.5 – 8.5** | 🟡 2.0–3.5 / 8.5–10.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 80 | 🟠 ≥ 65 | 🔴 < 65