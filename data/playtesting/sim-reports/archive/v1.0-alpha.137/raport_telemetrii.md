# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.137

**Wersja Balansu:** `v1.0-alpha.137` | **Data:** 2026-08-30 09:39 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 0.5s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 ** 55.5** | 🔴 55.5 | 33.3% | - | 45.4% | - | 25.8% | 28.8% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🟢 ** 95.6** | 🟢 95.6 | 33.3% | - | 31.9% | 33.6% | - | 34.5% | 🟢 ZBALANSOWANY |
| `3p-cienie-korona-kabala` | 3 | 🔴 ** 55.6** | 🔴 55.6 | 33.3% | - | 34.6% | 43.1% | 22.2% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 61.4** | 🔴 61.4 | 33.3% | - | - | 41.9% | 23.8% | 34.3% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 ** 57.6** | 🔴 57.6 | 33.3% | 44.8% | 26.4% | - | - | 28.9% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 38.9** | 🔴 38.9 | 33.3% | 51.1% | 23.8% | - | 25.1% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 ** 49.1** | 🔴 49.1 | 33.3% | 36.0% | 20.0% | 44.0% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🟠 ** 68.4** | 🟠 68.4 | 33.3% | 35.9% | - | - | 25.0% | 39.2% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-korona-gildia` | 3 | 🟢 ** 90.2** | 🟢 90.2 | 33.3% | 35.8% | - | 33.6% | - | 30.6% | 🟢 ZBALANSOWANY |
| `3p-oficjum-korona-kabala` | 3 | 🟢 ** 92.3** | 🟢 92.3 | 33.3% | 34.6% | - | 34.5% | 30.9% | - | 🟢 ZBALANSOWANY |
| `4p-core` | 4 | 🟡 ** 81.9** | 🟡 81.9 | 25.0% | 27.1% | 22.3% | 28.3% | 22.3% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟡 ** 85.3** | 🟡 85.3 | 25.0% | 26.2% | - | 23.6% | 28.0% | 22.2% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟡 ** 80.2** | 🟡 80.2 | 25.0% | 29.4% | 24.4% | 25.0% | - | 21.2% | 🟡 AKCEPTOWALNY |
| `4p-no-korona` | 4 | 🔴 ** 58.8** | 🔴 58.8 | 25.0% | 34.3% | 25.1% | - | 22.5% | 18.1% | 🔴 ODCHYLONY |
| `4p-no-oficjum` | 4 | 🟢 ** 94.1** | 🟢 94.1 | 25.0% | - | 24.0% | 26.8% | 24.6% | 24.6% | 🟢 ZBALANSOWANY |
| `5p-full` | 5 | 🟠 ** 65.2** | 🟠 65.2 | 20.0% | 26.0% | 22.7% | 17.6% | 19.2% | 14.5% | 🟠 WYMAGA UWAGI |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.69 🟡 | 0.1% 🟢 | 1.4% 🟢 | 1.25 🟢 | 6.95 🟢 | 9.8zł | 6.07 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 6.88 🟡 | 0.0% 🟢 | 3.8% 🟢 | 1.26 🟢 | 7.87 🟢 | 9.32zł | 6.68 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.29 🔴 | 0.8% 🟢 | 5.5% 🟢 | 1.34 🟢 | 6.79 🟢 | 6.91zł | 6.04 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 7.17 🔴 | 0.2% 🟢 | 6.7% 🟢 | 1.34 🟢 | 7.54 🟢 | 4.0zł | 6.09 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-gildia` | 6.11 🟢 | 0.0% 🟢 | 0.4% 🟢 | 1.8 🟢 | 7.89 🟢 | 11.0zł | 7.1 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 6.56 🟡 | 0.0% 🟢 | 0.8% 🟢 | 2.07 🔴 | 7.63 🟢 | 8.47zł | 6.62 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 6.59 🟡 | 0.0% 🟢 | 3.5% 🟢 | 2.03 🔴 | 7.66 🟢 | 7.97zł | 6.88 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 6.43 🟢 | 0.0% 🟢 | 1.1% 🟢 | 1.86 🟡 | 8.34 🟢 | 5.83zł | 6.89 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-gildia` | 6.31 🟢 | 0.0% 🟢 | 3.9% 🟢 | 1.76 🟢 | 8.0 🟢 | 5.53zł | 7.19 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 6.73 🟡 | 0.0% 🟢 | 4.7% 🟢 | 2.07 🔴 | 7.35 🟢 | 3.03zł | 6.5 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.03 🟢 | 0.0% 🟢 | 4.9% 🟢 | 1.88 🟡 | 7.68 🟢 | 8.03zł | 8.1 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.83 🟢 | 0.0% 🟢 | 5.4% 🟢 | 1.78 🟢 | 8.04 🟢 | 5.22zł | 8.39 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.69 🟢 | 0.0% 🟢 | 4.2% 🟢 | 1.69 🟢 | 8.16 🟢 | 9.92zł | 8.66 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.66 🟢 | 0.0% 🟢 | 1.1% 🟢 | 1.78 🟢 | 7.95 🟢 | 10.26zł | 8.45 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 6.19 🟢 | 0.0% 🟢 | 5.7% 🟢 | 1.15 🟢 | 7.47 🟢 | 8.59zł | 7.69 | 🟢 OPTYMALNA |
| `5p-full` | 5.41 🟢 | 0.0% 🟢 | 5.4% 🟢 | 1.64 🟢 | 7.91 🟢 | 9.9zł | 9.79 | 🟢 OPTYMALNA |

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
| **SO** | 34.7% | `3p-oficjum-alandalus-kabala` | +17.8% | 🟡 DOMINUJE |
| **CAA** | 27.3% | `3p-oficjum-alandalus-korona` | -13.3% | 🟡 SŁABA |
| **KT** | 24.5% | `3p-cienie-korona-kabala` | -11.1% | 🟡 SŁABA |
| **KB** | 32.0% | `3p-oficjum-alandalus-korona` | +10.7% | 🟡 DOMINUJE |
| **GC** | 27.0% | `4p-no-korona` | -6.9% | 🟡 SŁABA |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `3p-oficjum-alandalus-kabala` | 🔴 ** 38.9** | SO dominuje (51.1% vs ideal 33.3%) |
| `3p-oficjum-alandalus-korona` | 🔴 ** 49.1** | CAA za słaba (20.0% vs ideal 33.3%) |
| `3p-cienie-kabala-gildia` | 🔴 ** 55.5** | CAA dominuje (45.4% vs ideal 33.3%) |
| `3p-cienie-korona-kabala` | 🔴 ** 55.6** | KT za słaba (22.2% vs ideal 33.3%) |
| `3p-oficjum-alandalus-gildia` | 🔴 ** 57.6** | SO dominuje (44.8% vs ideal 33.3%) |
| `4p-no-korona` | 🔴 ** 58.8** | SO dominuje (34.3% vs ideal 25.0%) |
| `3p-korona-kabala-gildia` | 🔴 ** 61.4** | KT za słaba (23.8% vs ideal 33.3%) |
| `5p-full` | 🟠 ** 65.2** | SO dominuje (26.0% vs ideal 20.0%) |
| `3p-oficjum-kabala-gildia` | 🟠 ** 68.4** | KT za słaba (25.0% vs ideal 33.3%) |
| `4p-no-kabala` | 🟡 ** 80.2** | SO dominuje (29.4% vs ideal 25.0%) |
| `4p-core` | 🟡 ** 81.9** | KB dominuje (28.3% vs ideal 25.0%) |
| `4p-no-cienie` | 🟡 ** 85.3** | KT dominuje (28.0% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 1** | 0 |   0.0% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 2** | 162 |   0.1% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 2,511 |   1.6% | `█                   ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 14,436 |   9.1% | `█████               ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 32,652 |  20.5% | `██████████          ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 42,235 |  26.5% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 36,030 |  22.6% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 17,626 |  11.1% | `██████              ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 7,734 |   4.9% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 4,352 |   2.7% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 977 |   0.6% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 612 |   0.4% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 1** | 0 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 2** | 162 | 23 | 139 | 0 | 0 | 0 | **CAA (139)** |
| **Era 3** | 2,511 | 515 | 1,157 | 222 | 610 | 7 | **CAA (1,157)** |
| **Era 4** | 14,436 | 2,267 | 4,366 | 2,765 | 4,466 | 572 | **KT (4,466)** |
| **Era 5** | 32,652 | 6,604 | 8,845 | 6,120 | 7,427 | 3,656 | **CAA (8,845)** |
| **Era 6** | 42,235 | 10,584 | 8,424 | 8,372 | 7,500 | 7,355 | **SO (10,584)** |
| **Era 7** | 36,030 | 11,032 | 4,617 | 9,292 | 4,103 | 6,986 | **SO (11,032)** |
| **Era 8** | 17,626 | 3,994 | 1,498 | 3,268 | 1,841 | 7,025 | **GC (7,025)** |
| **Era 9** | 7,734 | 1,965 | 620 | 1,950 | 620 | 2,579 | **GC (2,579)** |
| **Era 10** | 4,352 | 847 | 241 | 2,265 | 161 | 838 | **KB (2,265)** |
| **Era 11** | 977 | 137 | 108 | 337 | 68 | 327 | **KB (337)** |
| **Era 12** | 612 | 111 | 30 | 199 | 44 | 228 | **GC (228)** |
| **SUMA** | **159,327** | **38,079** | **30,045** | **34,790** | **26,840** | **29,573** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **6.03** |  0.1% | 13.3% | 72.1% | 14.2% |  0.3% | **KB (30.7%)** |
| `4p-no-cienie` | **5.83** |  0.0% | 11.7% | 81.0% |  7.2% |  0.0% | **SO (25.9%)** |
| `4p-no-kabala` | **5.69** |  0.2% | 14.3% | 80.4% |  5.1% |  0.0% | **SO (28.1%)** |
| `4p-no-korona` | **5.66** |  0.3% | 15.5% | 78.2% |  6.0% |  0.0% | **SO (34.2%)** |
| `4p-no-oficjum` | **6.19** |  0.1% | 11.5% | 69.0% | 19.2% |  0.2% | **KB (34.0%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **3.5 – 8.5** | 🟡 2.0–3.5 / 8.5–10.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 80 | 🟠 ≥ 65 | 🔴 < 65