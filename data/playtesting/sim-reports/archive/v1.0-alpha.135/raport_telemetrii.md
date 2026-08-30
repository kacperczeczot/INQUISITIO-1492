# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.135

**Wersja Balansu:** `v1.0-alpha.135` | **Data:** 2026-08-30 09:24 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 0.56s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🟠 ** 66.1** | 🟠 66.1 | 33.3% | - | 42.4% | - | 29.7% | 27.9% | 🟠 WYMAGA UWAGI |
| `3p-cienie-korona-gildia` | 3 | 🟢 ** 96.5** | 🟢 96.5 | 33.3% | - | 33.5% | 32.1% | - | 34.3% | 🟢 ZBALANSOWANY |
| `3p-cienie-korona-kabala` | 3 | 🟠 ** 67.2** | 🟠 67.2 | 33.3% | - | 35.3% | 39.8% | 24.8% | - | 🟠 WYMAGA UWAGI |
| `3p-korona-kabala-gildia` | 3 | 🟠 ** 72.2** | 🟠 72.2 | 33.3% | - | - | 37.4% | 25.8% | 36.8% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-alandalus-gildia` | 3 | 🟠 ** 70.8** | 🟠 70.8 | 33.3% | 40.1% | 26.3% | - | - | 33.7% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 46.7** | 🔴 46.7 | 33.3% | 47.8% | 23.0% | - | 29.2% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 ** 44.5** | 🔴 44.5 | 33.3% | 34.6% | 19.1% | 46.2% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 ** 49.5** | 🔴 49.5 | 33.3% | 33.4% | - | - | 21.1% | 45.4% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🟢 ** 97.9** | 🟢 97.9 | 33.3% | 34.0% | - | 32.5% | - | 33.5% | 🟢 ZBALANSOWANY |
| `3p-oficjum-korona-kabala` | 3 | 🟢 ** 97.5** | 🟢 97.5 | 33.3% | 33.3% | - | 34.2% | 32.5% | - | 🟢 ZBALANSOWANY |
| `4p-core` | 4 | 🟡 ** 82.9** | 🟡 82.9 | 25.0% | 24.0% | 22.2% | 29.2% | 24.6% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟡 ** 88.0** | 🟡 88.0 | 25.0% | 23.0% | - | 23.5% | 27.8% | 25.8% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟢 ** 91.3** | 🟢 91.3 | 25.0% | 23.5% | 23.9% | 27.2% | - | 25.4% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟢 ** 97.7** | 🟢 97.7 | 25.0% | 24.5% | 24.5% | - | 25.5% | 25.5% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟢 ** 98.3** | 🟢 98.3 | 25.0% | - | 24.4% | 25.0% | 25.1% | 25.5% | 🟢 ZBALANSOWANY |
| `5p-full` | 5 | 🟢 ** 95.7** | 🟢 95.7 | 20.0% | 19.8% | 21.1% | 19.3% | 20.4% | 19.4% | 🟢 ZBALANSOWANY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.63 🟡 | 0.2% 🟢 | 1.5% 🟢 | 1.25 🟢 | 5.75 🟢 | 13.67zł | 5.66 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 6.98 🟡 | 0.0% 🟢 | 4.0% 🟢 | 1.3 🟢 | 7.09 🟢 | 14.08zł | 6.45 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.33 🔴 | 0.8% 🟢 | 5.6% 🟢 | 1.37 🟢 | 6.22 🟢 | 10.93zł | 5.81 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 7.06 🔴 | 0.2% 🟢 | 6.9% 🟢 | 1.33 🟢 | 6.75 🟢 | 4.78zł | 5.95 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-gildia` | 6.14 🟢 | 0.0% 🟢 | 0.5% 🟢 | 1.8 🟢 | 7.71 🟢 | 15.15zł | 7.01 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 6.72 🟡 | 0.1% 🟢 | 0.9% 🟢 | 2.08 🔴 | 7.98 🟢 | 12.33zł | 6.52 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 6.64 🟡 | 0.0% 🟢 | 3.6% 🟢 | 2.04 🔴 | 7.72 🟢 | 11.77zł | 6.8 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 6.43 🟢 | 0.0% 🟢 | 1.4% 🟢 | 1.84 🟡 | 8.41 🟢 | 6.75zł | 6.92 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-gildia` | 6.32 🟢 | 0.0% 🟢 | 3.9% 🟢 | 1.78 🟢 | 7.86 🟢 | 6.43zł | 7.2 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 6.67 🟡 | 0.0% 🟢 | 4.7% 🟢 | 2.03 🔴 | 7.53 🟢 | 3.04zł | 6.5 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.12 🟢 | 0.0% 🟢 | 5.0% 🟢 | 1.91 🟡 | 7.85 🟢 | 11.41zł | 7.94 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.82 🟢 | 0.0% 🟢 | 5.6% 🟢 | 1.75 🟢 | 7.88 🟢 | 6.0zł | 8.34 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.75 🟢 | 0.0% 🟢 | 4.4% 🟢 | 1.71 🟢 | 7.85 🟢 | 13.8zł | 8.49 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.71 🟢 | 0.0% 🟢 | 1.4% 🟢 | 1.75 🟢 | 7.84 🟢 | 13.93zł | 8.23 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 6.22 🟢 | 0.0% 🟢 | 5.9% 🟢 | 1.16 🟢 | 6.48 🟢 | 12.65zł | 7.37 | 🟢 OPTYMALNA |
| `5p-full` | 5.45 🟢 | 0.0% 🟢 | 5.7% 🟢 | 1.63 🟢 | 7.65 🟢 | 13.43zł | 9.55 | 🟢 OPTYMALNA |

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
| **SO** | 30.7% | `3p-oficjum-alandalus-kabala` | +14.5% | 🟡 DOMINUJE |
| **CAA** | 26.9% | `3p-oficjum-alandalus-korona` | -14.2% | 🟡 SŁABA |
| **KB** | 31.5% | `3p-oficjum-alandalus-korona` | +12.9% | 🟡 DOMINUJE |
| **KT** | 26.0% | `3p-oficjum-kabala-gildia` | -12.2% | 🟡 SŁABA |
| **GC** | 30.3% | `3p-oficjum-kabala-gildia` | +12.1% | 🟡 DOMINUJE |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `3p-oficjum-alandalus-korona` | 🔴 ** 44.5** | CAA za słaba (19.1% vs ideal 33.3%) |
| `3p-oficjum-alandalus-kabala` | 🔴 ** 46.7** | SO dominuje (47.8% vs ideal 33.3%) |
| `3p-oficjum-kabala-gildia` | 🔴 ** 49.5** | KT za słaba (21.1% vs ideal 33.3%) |
| `3p-cienie-kabala-gildia` | 🟠 ** 66.1** | CAA dominuje (42.4% vs ideal 33.3%) |
| `3p-cienie-korona-kabala` | 🟠 ** 67.2** | KT za słaba (24.8% vs ideal 33.3%) |
| `3p-oficjum-alandalus-gildia` | 🟠 ** 70.8** | CAA za słaba (26.3% vs ideal 33.3%) |
| `3p-korona-kabala-gildia` | 🟠 ** 72.2** | KT za słaba (25.8% vs ideal 33.3%) |
| `4p-core` | 🟡 ** 82.9** | KB dominuje (29.2% vs ideal 25.0%) |
| `4p-no-cienie` | 🟡 ** 88.0** | KT dominuje (27.8% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 1** | 0 |   0.0% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 2** | 114 |   0.1% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 2,552 |   1.6% | `█                   ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 14,457 |   9.1% | `█████               ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 32,321 |  20.3% | `██████████          ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 41,371 |  26.0% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 36,218 |  22.8% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 18,030 |  11.3% | `██████              ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 7,969 |   5.0% | `███                 ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 4,417 |   2.8% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 1,030 |   0.6% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 686 |   0.4% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 1** | 0 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 2** | 114 | 8 | 106 | 0 | 0 | 0 | **CAA (106)** |
| **Era 3** | 2,552 | 299 | 1,262 | 230 | 755 | 6 | **CAA (1,262)** |
| **Era 4** | 14,457 | 1,690 | 4,128 | 2,607 | 5,082 | 950 | **KT (5,082)** |
| **Era 5** | 32,321 | 5,137 | 8,418 | 6,081 | 7,469 | 5,216 | **CAA (8,418)** |
| **Era 6** | 41,371 | 8,908 | 7,749 | 8,429 | 7,770 | 8,515 | **SO (8,908)** |
| **Era 7** | 36,218 | 10,361 | 4,692 | 8,916 | 4,448 | 7,801 | **SO (10,361)** |
| **Era 8** | 18,030 | 3,999 | 1,853 | 3,148 | 2,000 | 7,030 | **GC (7,030)** |
| **Era 9** | 7,969 | 2,116 | 783 | 2,047 | 686 | 2,337 | **GC (2,337)** |
| **Era 10** | 4,417 | 938 | 353 | 2,144 | 185 | 797 | **KB (2,144)** |
| **Era 11** | 1,030 | 174 | 150 | 375 | 56 | 275 | **KB (375)** |
| **Era 12** | 686 | 125 | 67 | 191 | 40 | 263 | **GC (263)** |
| **SUMA** | **159,165** | **33,755** | **29,561** | **34,168** | **28,491** | **33,190** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **6.12** |  0.1% | 13.3% | 69.7% | 16.5% |  0.4% | **KB (32.5%)** |
| `4p-no-cienie` | **5.82** |  0.0% | 12.2% | 80.7% |  7.0% |  0.0% | **GC (28.0%)** |
| `4p-no-kabala` | **5.75** |  0.2% | 14.3% | 78.7% |  6.8% |  0.0% | **KB (29.7%)** |
| `4p-no-korona` | **5.71** |  0.2% | 15.7% | 77.1% |  7.0% |  0.0% | **GC (31.9%)** |
| `4p-no-oficjum` | **6.22** |  0.1% | 11.9% | 67.0% | 20.6% |  0.3% | **KB (33.0%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **3.5 – 8.5** | 🟡 2.0–3.5 / 8.5–10.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 80 | 🟠 ≥ 65 | 🔴 < 65