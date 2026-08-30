# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.106

**Wersja Balansu:** `v1.0-alpha.106` | **Data:** 2026-08-30 02:13 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 0.45s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 ** 63.4** | 🔴 63.4 | 33.3% | - | 43.1% | - | 27.2% | 29.7% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🟡 ** 89.5** | 🟡 89.5 | 33.3% | - | 36.2% | 30.7% | - | 33.1% | 🟡 AKCEPTOWALNY |
| `3p-cienie-korona-kabala` | 3 | 🔴 ** 51.1** | 🔴 51.1 | 33.3% | - | 36.5% | 43.1% | 20.4% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 56.8** | 🔴 56.8 | 33.3% | - | - | 36.8% | 21.8% | 41.3% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🟠 ** 68.5** | 🟠 68.5 | 33.3% | 41.0% | 26.3% | - | - | 32.7% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 41.5** | 🔴 41.5 | 33.3% | 49.8% | 22.4% | - | 27.7% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 ** 44.9** | 🔴 44.9 | 33.3% | 34.4% | 19.4% | 46.2% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 ** 35.1** | 🔴 35.1 | 33.3% | 30.5% | - | - | 18.3% | 51.3% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🟠 ** 78.6** | 🟠 78.6 | 33.3% | 35.9% | - | 27.4% | - | 36.7% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-korona-kabala` | 3 | 🟡 ** 81.8** | 🟡 81.8 | 33.3% | 38.5% | - | 30.3% | 31.2% | - | 🟡 AKCEPTOWALNY |
| `4p-core` | 4 | 🟡 ** 87.6** | 🟡 87.6 | 25.0% | 24.4% | 24.4% | 28.2% | 22.9% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟡 ** 85.1** | 🟡 85.1 | 25.0% | 23.2% | - | 22.3% | 27.6% | 27.0% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟡 ** 89.2** | 🟡 89.2 | 25.0% | 22.1% | 25.2% | 26.4% | - | 26.3% | 🟡 AKCEPTOWALNY |
| `4p-no-korona` | 4 | 🟢 ** 98.1** | 🟢 98.1 | 25.0% | 25.1% | 24.9% | - | 24.4% | 25.6% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟢 ** 93.3** | 🟢 93.3 | 25.0% | - | 26.7% | 25.3% | 24.3% | 23.7% | 🟢 ZBALANSOWANY |
| `5p-full` | 5 | 🟡 ** 88.4** | 🟡 88.4 | 20.0% | 20.1% | 22.1% | 19.3% | 20.7% | 17.7% | 🟡 AKCEPTOWALNY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.47 🟢 | 0.1% 🟢 | 0.8% 🟢 | 1.22 🟢 | 6.03 🟢 | 10.55zł | 5.77 | 🟢 OPTYMALNA |
| `3p-cienie-korona-gildia` | 6.92 🟡 | 0.0% 🟢 | 4.0% 🟢 | 1.3 🟢 | 7.01 🟢 | 10.88zł | 6.37 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.26 🔴 | 1.0% 🟢 | 4.9% 🟢 | 1.34 🟢 | 6.27 🟢 | 7.14zł | 5.85 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.9 🟡 | 0.1% 🟢 | 6.1% 🟢 | 1.28 🟢 | 6.89 🟢 | 4.58zł | 5.99 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-gildia` | 6.13 🟢 | 0.0% 🟢 | 0.8% 🟢 | 1.83 🟡 | 7.83 🟢 | 12.09zł | 7.06 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 6.48 🟢 | 0.0% 🟢 | 0.9% 🟢 | 2.02 🔴 | 7.85 🟢 | 8.22zł | 6.6 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-korona` | 6.74 🟡 | 0.0% 🟢 | 4.1% 🟢 | 2.1 🔴 | 7.87 🟢 | 8.2zł | 6.82 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 6.37 🟢 | 0.0% 🟢 | 1.4% 🟢 | 1.82 🟡 | 8.63 🟡 | 6.0zł | 7.02 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-gildia` | 6.4 🟢 | 0.0% 🟢 | 4.7% 🟢 | 1.83 🟡 | 8.09 🟢 | 5.94zł | 7.21 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 6.6 🟡 | 0.0% 🟢 | 5.0% 🟢 | 1.99 🟡 | 7.66 🟢 | 2.37zł | 6.58 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.03 🟢 | 0.0% 🟢 | 5.1% 🟢 | 1.87 🟡 | 7.78 🟢 | 7.8zł | 7.94 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.7 🟢 | 0.0% 🟢 | 5.8% 🟢 | 1.69 🟢 | 7.83 🟢 | 5.43zł | 8.45 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.82 🟢 | 0.0% 🟢 | 5.1% 🟢 | 1.74 🟢 | 8.01 🟢 | 10.87zł | 8.44 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.57 🟢 | 0.0% 🟢 | 1.2% 🟢 | 1.7 🟢 | 7.82 🟢 | 10.55zł | 8.35 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 6.0 🟢 | 0.0% 🟢 | 5.2% 🟢 | 1.11 🟢 | 6.34 🟢 | 9.43zł | 7.39 | 🟢 OPTYMALNA |
| `5p-full` | 5.34 🟢 | 0.0% 🟢 | 5.7% 🟢 | 1.58 🟢 | 7.52 🟢 | 10.26zł | 9.54 | 🟢 OPTYMALNA |

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
| **GC** | 31.4% | `3p-oficjum-kabala-gildia` | +18.0% | 🟡 DOMINUJE |
| **SO** | 31.4% | `3p-oficjum-alandalus-kabala` | +16.5% | 🟡 DOMINUJE |
| **KT** | 24.2% | `3p-oficjum-kabala-gildia` | -15.0% | 🟡 SŁABA |
| **CAA** | 27.9% | `3p-oficjum-alandalus-korona` | -13.9% | 🟡 SŁABA |
| **KB** | 30.5% | `3p-oficjum-alandalus-korona` | +12.9% | 🟡 DOMINUJE |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `3p-oficjum-kabala-gildia` | 🔴 ** 35.1** | GC dominuje (51.3% vs ideal 33.3%) |
| `3p-oficjum-alandalus-kabala` | 🔴 ** 41.5** | SO dominuje (49.8% vs ideal 33.3%) |
| `3p-oficjum-alandalus-korona` | 🔴 ** 44.9** | CAA za słaba (19.4% vs ideal 33.3%) |
| `3p-cienie-korona-kabala` | 🔴 ** 51.1** | KT za słaba (20.4% vs ideal 33.3%) |
| `3p-korona-kabala-gildia` | 🔴 ** 56.8** | KT za słaba (21.8% vs ideal 33.3%) |
| `3p-cienie-kabala-gildia` | 🔴 ** 63.4** | CAA dominuje (43.1% vs ideal 33.3%) |
| `3p-oficjum-alandalus-gildia` | 🟠 ** 68.5** | SO dominuje (41.0% vs ideal 33.3%) |
| `3p-oficjum-korona-gildia` | 🟠 ** 78.6** | KB za słaba (27.4% vs ideal 33.3%) |
| `3p-oficjum-korona-kabala` | 🟡 ** 81.8** | SO dominuje (38.5% vs ideal 33.3%) |
| `4p-no-cienie` | 🟡 ** 85.1** | KB za słaba (22.3% vs ideal 25.0%) |
| `4p-core` | 🟡 ** 87.6** | KB dominuje (28.2% vs ideal 25.0%) |
| `5p-full` | 🟡 ** 88.4** | GC za słaba (17.7% vs ideal 20.0%) |
| `4p-no-kabala` | 🟡 ** 89.2** | SO za słaba (22.1% vs ideal 25.0%) |
| `3p-cienie-korona-gildia` | 🟡 ** 89.5** | CAA dominuje (36.2% vs ideal 33.3%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 1** | 0 |   0.0% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 2** | 220 |   0.1% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 2,866 |   1.8% | `█                   ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 15,331 |   9.6% | `█████               ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 34,049 |  21.4% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 41,483 |  26.0% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 34,885 |  21.9% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 17,322 |  10.9% | `█████               ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 7,568 |   4.8% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 4,128 |   2.6% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 924 |   0.6% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 534 |   0.3% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 1** | 0 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 2** | 220 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 3** | 2,866 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 4** | 15,331 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 5** | 34,049 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 6** | 41,483 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 7** | 34,885 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 8** | 17,322 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 9** | 7,568 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 10** | 4,128 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 11** | 924 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 12** | 534 | 0 | 0 | 0 | 0 | 0 | - |
| **SUMA** | **159,310** | **0** | **0** | **0** | **0** | **0** | **Łącznie: 100.0%** |

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