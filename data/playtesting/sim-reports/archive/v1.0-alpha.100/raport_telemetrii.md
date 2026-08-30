# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.100

**Wersja Balansu:** `v1.0-alpha.100` | **Data:** 2026-08-30 00:27 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 0.42s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 ** 21.8** | 🔴 50.5 | 33.3% | - | 46.9% | - | 27.9% | 25.1% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 46.0** | 🟠 74.7 | 33.3% | - | 37.4% | 36.1% | - | 26.5% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 ** 21.6** | 🔴 50.9 | 33.3% | - | 36.5% | 43.2% | 20.3% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 26.2** | 🔴 53.6 | 33.3% | - | - | 44.8% | 22.8% | 32.4% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 ** 23.6** | 🟠 78.5 | 33.3% | 31.7% | 29.2% | - | - | 39.1% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 **  8.0** | 🔴 54.2 | 33.3% | 45.5% | 24.5% | - | 30.1% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 **  5.7** | 🔴 27.7 | 33.3% | 23.8% | 20.2% | 56.0% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 **  6.4** | 🔴 21.3 | 33.3% | 20.4% | - | - | 19.9% | 59.7% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 ** 19.4** | 🔴 64.6 | 33.3% | 23.8% | - | 36.9% | - | 39.3% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 ** 15.7** | 🟠 78.2 | 33.3% | 28.5% | - | 38.9% | 32.6% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟡 ** 87.6** | 🟡 87.6 | 25.0% | 24.4% | 24.4% | 28.2% | 22.9% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟡 ** 85.1** | 🟡 85.1 | 25.0% | 23.2% | - | 22.3% | 27.6% | 27.0% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟡 ** 89.2** | 🟡 89.2 | 25.0% | 22.1% | 25.2% | 26.4% | - | 26.3% | 🟡 AKCEPTOWALNY |
| `4p-no-korona` | 4 | 🟢 ** 98.1** | 🟢 98.1 | 25.0% | 25.1% | 24.9% | - | 24.4% | 25.6% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟢 ** 93.3** | 🟢 93.3 | 25.0% | - | 26.7% | 25.3% | 24.3% | 23.7% | 🟢 ZBALANSOWANY |
| `5p-full` | 5 | 🟠 ** 75.6** | 🟠 75.6 | 20.0% | 24.2% | 21.5% | 18.4% | 20.0% | 15.8% | 🟠 WYMAGA UWAGI |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.71 🟡 | 0.2% 🟢 | 0.8% 🟢 | 1.28 🟢 | 6.47 🟢 | 10.88zł | 5.81 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 7.13 🔴 | 0.0% 🟢 | 4.0% 🟢 | 1.34 🟢 | 7.41 🟢 | 11.18zł | 6.42 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.26 🔴 | 0.9% 🟢 | 4.9% 🟢 | 1.34 🟢 | 6.27 🟢 | 7.14zł | 5.85 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 7.24 🔴 | 0.2% 🟢 | 6.1% 🟢 | 1.36 🟢 | 7.5 🟢 | 4.8zł | 6.04 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-gildia` | 6.62 🟡 | 0.0% 🟢 | 0.9% 🟢 | 1.96 🟡 | 8.86 🟡 | 12.87zł | 7.13 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-kabala` | 6.99 🟡 | 0.1% 🟢 | 0.9% 🟢 | 2.11 🔴 | 8.92 🟡 | 8.73zł | 6.64 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 7.01 🔴 | 0.0% 🟢 | 4.1% 🟢 | 2.16 🔴 | 8.39 🟢 | 8.48zł | 6.85 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 6.92 🟡 | 0.0% 🟢 | 1.4% 🟢 | 1.92 🟡 | 9.84 🟡 | 6.47zł | 7.08 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 6.87 🟡 | 0.0% 🟢 | 4.8% 🟢 | 1.93 🟡 | 9.05 🟡 | 6.33zł | 7.28 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-kabala` | 6.98 🟡 | 0.0% 🟢 | 5.0% 🟢 | 2.06 🔴 | 8.37 🟢 | 2.46zł | 6.61 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.03 🟢 | 0.0% 🟢 | 5.1% 🟢 | 1.87 🟡 | 7.78 🟢 | 7.8zł | 7.94 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.7 🟢 | 0.0% 🟢 | 5.8% 🟢 | 1.69 🟢 | 7.83 🟢 | 5.43zł | 8.45 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.82 🟢 | 0.0% 🟢 | 5.1% 🟢 | 1.74 🟢 | 8.01 🟢 | 10.87zł | 8.44 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.57 🟢 | 0.0% 🟢 | 1.2% 🟢 | 1.7 🟢 | 7.82 🟢 | 10.55zł | 8.35 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 6.0 🟢 | 0.0% 🟢 | 5.2% 🟢 | 1.11 🟢 | 6.34 🟢 | 9.43zł | 7.39 | 🟢 OPTYMALNA |
| `5p-full` | 5.3 🟢 | 0.0% 🟢 | 5.7% 🟢 | 1.57 🟢 | 7.39 🟢 | 10.19zł | 9.51 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.840 | Ekstremalny Deadlock (Era 11+): 4.2% gier (>0.5%) |
| `3p-cienie-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 0.486 | Ekstremalny Deadlock (Era 11+): 2.4% gier (>0.5%) |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 0.856 | Ekstremalny Deadlock (Era 11+): 4.3% gier (>0.5%) |
| `3p-korona-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.714 | Ekstremalny Deadlock (Era 11+): 3.6% gier (>0.5%) |
| `3p-oficjum-alandalus-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka skazania (swiete-oficjum): 0/3168 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-alandalus-kabala` | ⚠️ Ostrzeżenie Witalności | 1.908 | Ekstremalny Deadlock (Era 11+): 3.5% gier (>0.5%), Martwa ścieżka skazania (swiete-oficjum): 0/4547 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-alandalus-korona` | ⚠️ Ostrzeżenie Witalności | 1.578 | Ekstremalny Deadlock (Era 11+): 1.9% gier (>0.5%), Martwa ścieżka skazania (swiete-oficjum): 0/2383 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka skazania (swiete-oficjum): 0/2045 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka skazania (swiete-oficjum): 0/2384 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.604 | Ekstremalny Deadlock (Era 11+): 2.0% gier (>0.5%), Martwa ścieżka skazania (swiete-oficjum): 0/2850 wygranych (<8%) — gra tylko stosy |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |

## 3.1. Frakcje Wymagające Uwagi

| Frakcja | Śr. Win Share (wszystkie setupy) | Najgorszy Setup | Max Odchylenie od Ideału | Status |
| :--- | :---: | :--- | :---: | :--- |
| **GC** | 31.0% | `3p-oficjum-kabala-gildia` | +26.4% | 🟡 DOMINUJE |
| **KB** | 34.2% | `3p-oficjum-alandalus-korona` | +22.7% | 🟡 DOMINUJE |
| **CAA** | 28.9% | `3p-cienie-kabala-gildia` | +13.6% | 🟡 DOMINUJE |
| **KT** | 24.8% | `3p-oficjum-kabala-gildia` | -13.4% | 🟡 SŁABA |
| **SO** | 26.6% | `3p-oficjum-kabala-gildia` | -12.9% | 🟡 SŁABA |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `3p-oficjum-alandalus-korona` | 🔴 **  5.7** | KB dominuje (56.0% vs ideal 33.3%) |
| `3p-oficjum-kabala-gildia` | 🔴 **  6.4** | GC dominuje (59.7% vs ideal 33.3%) |
| `3p-oficjum-alandalus-kabala` | 🔴 **  8.0** | SO dominuje (45.5% vs ideal 33.3%) |
| `3p-oficjum-korona-kabala` | 🔴 ** 15.7** | KB dominuje (38.9% vs ideal 33.3%) |
| `3p-oficjum-korona-gildia` | 🔴 ** 19.4** | SO za słaba (23.8% vs ideal 33.3%) |
| `3p-cienie-korona-kabala` | 🔴 ** 21.6** | KT za słaba (20.3% vs ideal 33.3%) |
| `3p-cienie-kabala-gildia` | 🔴 ** 21.8** | CAA dominuje (46.9% vs ideal 33.3%) |
| `3p-oficjum-alandalus-gildia` | 🔴 ** 23.6** | GC dominuje (39.1% vs ideal 33.3%) |
| `3p-korona-kabala-gildia` | 🔴 ** 26.2** | KB dominuje (44.8% vs ideal 33.3%) |
| `3p-cienie-korona-gildia` | 🔴 ** 46.0** | GC za słaba (26.5% vs ideal 33.3%) |
| `5p-full` | 🟠 ** 75.6** | SO dominuje (24.2% vs ideal 20.0%) |
| `4p-no-cienie` | 🟡 ** 85.1** | KB za słaba (22.3% vs ideal 25.0%) |
| `4p-core` | 🟡 ** 87.6** | KB dominuje (28.2% vs ideal 25.0%) |
| `4p-no-kabala` | 🟡 ** 89.2** | SO za słaba (22.1% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 1** | 0 |   0.0% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 2** | 218 |   0.1% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 2,815 |   1.8% | `█                   ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 14,575 |   9.2% | `█████               ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 30,893 |  19.4% | `██████████          ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 36,126 |  22.7% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 35,288 |  22.2% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 20,361 |  12.8% | `██████              ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 9,918 |   6.2% | `███                 ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 6,588 |   4.1% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 1,440 |   0.9% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 888 |   0.6% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 1** | 0 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 2** | 218 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 3** | 2,815 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 4** | 14,575 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 5** | 30,893 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 6** | 36,126 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 7** | 35,288 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 8** | 20,361 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 9** | 9,918 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 10** | 6,588 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 11** | 1,440 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 12** | 888 | 0 | 0 | 0 | 0 | 0 | - |
| **SUMA** | **159,110** | **0** | **0** | **0** | **0** | **0** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **6.03** |  0.1% | 15.4% | 68.1% | 15.9% |  0.4% | Brak gier w Erze 6 |
| `4p-no-cienie` | **5.70** |  0.0% | 13.8% | 80.3% |  5.8% |  0.0% | Brak gier w Erze 6 |
| `4p-no-kabala` | **5.82** |  0.3% | 12.8% | 78.6% |  8.2% |  0.0% | Brak gier w Erze 6 |
| `4p-no-korona` | **5.57** |  0.4% | 17.5% | 76.4% |  5.7% |  0.0% | Brak gier w Erze 6 |
| `4p-no-oficjum` | **6.00** |  0.1% | 13.4% | 70.9% | 15.4% |  0.3% | Brak gier w Erze 6 |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **3.5 – 8.5** | 🟡 2.0–3.5 / 8.5–10.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 80 | 🟠 ≥ 65 | 🔴 < 65