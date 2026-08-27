# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.78

**Wersja Balansu:** `v1.0-alpha.78` | **Data:** 2026-08-24 20:14 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 88.55s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 ** 46.8** | 🟠 73.4 | 33.3% | - | 40.4% | - | 31.5% | 28.2% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 52.1** | 🟠 66.7 | 33.3% | - | 38.6% | 24.4% | - | 37.0% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 ** 18.3** | 🟡 86.3 | 33.3% | - | 30.9% | 37.3% | 31.8% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 57.0** | 🟡 86.7 | 33.3% | - | - | 32.2% | 30.6% | 37.1% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 ** 13.3** | 🔴 13.3 | 33.3% | 63.8% | 28.2% | - | - | 8.1% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 32.8** | 🔴 32.8 | 33.3% | 53.1% | 27.2% | - | 19.7% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 ** 44.8** | 🔴 50.1 | 33.3% | 46.2% | 22.5% | 31.3% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 **  0.3** | 🔴 5.4 | 33.3% | 77.1% | - | - | 14.5% | 8.5% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 **  2.2** | 🔴 7.4 | 33.3% | 73.0% | - | 17.5% | - | 9.5% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 **  9.9** | 🔴 32.8 | 33.3% | 52.2% | - | 17.5% | 30.3% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟢 ** 92.6** | 🟢 92.6 | 25.0% | 25.3% | 24.7% | 26.8% | 23.2% | - | 🟢 ZBALANSOWANY |
| `4p-no-cienie` | 4 | 🟠 ** 68.7** | 🟠 68.7 | 25.0% | 31.5% | - | 20.3% | 26.8% | 21.3% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🟡 ** 87.2** | 🟡 87.2 | 25.0% | 26.2% | 27.1% | 24.9% | - | 21.8% | 🟡 AKCEPTOWALNY |
| `4p-no-korona` | 4 | 🟡 ** 81.4** | 🟡 81.4 | 25.0% | 27.6% | 27.9% | - | 23.0% | 21.5% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🟡 ** 75.6** | 🟡 75.6 | 25.0% | - | 21.1% | 22.6% | 25.8% | 30.4% | 🟡 AKCEPTOWALNY |
| `5p-full` | 5 | 🔴 ** 19.6** | 🔴 33.1 | 20.0% | 36.1% | 20.8% | 14.6% | 16.7% | 11.9% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.28 🟢 | 0.1% 🟢 | 0.2% 🟢 | 1.17 🟢 | 7.28 🟢 | 14.09zł | 7.78 | 🟢 OPTYMALNA |
| `3p-cienie-korona-gildia` | 6.85 🟡 | 0.0% 🟢 | 5.8% 🟢 | 1.25 🟢 | 8.14 🟢 | 14.82zł | 8.86 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 6.85 🟡 | 0.7% 🟢 | 5.8% 🟢 | 1.23 🟢 | 7.49 🟢 | 10.42zł | 7.91 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.5 🟢 | 0.1% 🟢 | 6.5% 🟢 | 1.16 🟢 | 7.45 🟢 | 5.19zł | 8.09 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 5.64 🟢 | 0.0% 🟢 | 1.0% 🟢 | 1.67 🟢 | 6.91 🟢 | 14.41zł | 9.14 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 5.75 🟢 | 0.1% 🟢 | 1.0% 🟢 | 1.64 🟢 | 6.57 🟢 | 10.57zł | 8.62 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-korona` | 6.33 🟢 | 0.0% 🟢 | 5.4% 🟢 | 1.7 🟢 | 7.6 🟢 | 10.73zł | 9.19 | 🟢 OPTYMALNA |
| `3p-oficjum-kabala-gildia` | 4.97 🟡 | 0.0% 🟢 | 1.0% 🟢 | 1.45 🟢 | 6.11 🟢 | 5.56zł | 8.79 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 5.95 🟢 | 0.0% 🟢 | 6.3% 🟢 | 1.74 🟢 | 7.1 🟢 | 6.11zł | 9.43 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 5.85 🟢 | 0.0% 🟢 | 6.4% 🟢 | 1.65 🟢 | 6.38 🟢 | 2.62zł | 8.66 | 🟢 OPTYMALNA |
| `4p-core` | 5.95 🟢 | 0.0% 🟢 | 4.7% 🟢 | 1.73 🟢 | 8.06 🟢 | 8.27zł | 8.01 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.66 🟢 | 0.0% 🟢 | 5.5% 🟢 | 1.64 🟢 | 7.52 🟢 | 4.57zł | 8.33 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.91 🟢 | 0.0% 🟢 | 4.8% 🟢 | 1.63 🟢 | 8.21 🟢 | 10.82zł | 8.49 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.6 🟢 | 0.0% 🟢 | 0.8% 🟢 | 1.64 🟢 | 7.9 🟢 | 10.59zł | 8.19 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.73 🟢 | 0.0% 🟢 | 4.8% 🟢 | 1.05 🟢 | 7.24 🟢 | 9.5zł | 7.7 | 🟢 OPTYMALNA |
| `5p-full` | 5.21 🟢 | 0.0% 🟢 | 4.0% 🟢 | 1.49 🟢 | 7.51 🟢 | 8.12zł | 7.7 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.450 | Ekstremalny Deadlock (Era 11+): 2.2% gier (>0.5%) |
| `3p-cienie-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 0.248 | Ekstremalny Deadlock (Era 11+): 1.2% gier (>0.5%) |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.554 | Ekstremalny Deadlock (Era 11+): 7.8% gier (>0.5%) |
| `3p-korona-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.420 | Ekstremalny Deadlock (Era 11+): 2.1% gier (>0.5%) |
| `3p-oficjum-alandalus-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-korona` | ⚠️ Ostrzeżenie Witalności | 0.110 | Ekstremalny Deadlock (Era 11+): 0.5% gier (>0.5%) |
| `3p-oficjum-kabala-gildia` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.745 | Przedwczesne Zwycięstwa (Era 1-2): 0.8% gier (>0.5%), Nadmiar Wczesnych Zakończeń (Era 3-4): 38.2% gier (>25.0%), Zbyt Krótka Średnia Rozgrywka 4.97 Er (<5.0 Er), Martwa ścieżka stosy (swiete-oficjum): 20/7707 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 382/7299 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 251/5221 wygranych (<8%) — gra tylko skazania |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | ⚠️ Ostrzeżenie Witalności | 0.526 | Nadmiar Wczesnych Zakończeń (Era 3-4): 30.3% gier (>25.0%) |

## 3.1. Frakcje Wymagające Uwagi

| Frakcja | Śr. Win Share (wszystkie setupy) | Najgorszy Setup | Max Odchylenie od Ideału | Status |
| :--- | :---: | :--- | :---: | :--- |
| **SO** | 46.6% | `3p-oficjum-kabala-gildia` | +43.8% | 🟡 DOMINUJE |
| **GC** | 21.4% | `3p-oficjum-alandalus-gildia` | -25.2% | 🟡 SŁABA |
| **KT** | 24.9% | `3p-oficjum-kabala-gildia` | -18.8% | 🟡 SŁABA |
| **KB** | 24.5% | `3p-oficjum-korona-gildia` | -15.8% | 🟡 SŁABA |
| **CAA** | 28.1% | `3p-oficjum-alandalus-korona` | -10.8% | 🟡 SŁABA |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `3p-oficjum-kabala-gildia` | 🔴 **  0.3** | SO dominuje (77.1% vs ideal 33.3%) |
| `3p-oficjum-korona-gildia` | 🔴 **  2.2** | SO dominuje (73.0% vs ideal 33.3%) |
| `3p-oficjum-korona-kabala` | 🔴 **  9.9** | SO dominuje (52.2% vs ideal 33.3%) |
| `3p-oficjum-alandalus-gildia` | 🔴 ** 13.3** | SO dominuje (63.8% vs ideal 33.3%) |
| `3p-cienie-korona-kabala` | 🔴 ** 18.3** | KB dominuje (37.3% vs ideal 33.3%) |
| `5p-full` | 🔴 ** 19.6** | SO dominuje (36.1% vs ideal 20.0%) |
| `3p-oficjum-alandalus-kabala` | 🔴 ** 32.8** | SO dominuje (53.1% vs ideal 33.3%) |
| `3p-oficjum-alandalus-korona` | 🔴 ** 44.8** | SO dominuje (46.2% vs ideal 33.3%) |
| `3p-cienie-kabala-gildia` | 🔴 ** 46.8** | CAA dominuje (40.4% vs ideal 33.3%) |
| `3p-cienie-korona-gildia` | 🔴 ** 52.1** | KB za słaba (24.4% vs ideal 33.3%) |
| `3p-korona-kabala-gildia` | 🔴 ** 57.0** | GC dominuje (37.1% vs ideal 33.3%) |
| `4p-no-cienie` | 🟠 ** 68.7** | SO dominuje (31.5% vs ideal 25.0%) |
| `4p-no-oficjum` | 🟡 ** 75.6** | GC dominuje (30.4% vs ideal 25.0%) |
| `4p-no-korona` | 🟡 ** 81.4** | GC za słaba (21.5% vs ideal 25.0%) |
| `4p-no-kabala` | 🟡 ** 87.2** | GC za słaba (21.8% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 355 |   0.2% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 5,682 |   3.6% | `██                  ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 23,505 |  14.7% | `███████             ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 38,246 |  23.9% | `████████████        ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 40,633 |  25.4% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 25,746 |  16.1% | `████████            ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 15,942 |  10.0% | `█████               ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 5,802 |   3.6% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 2,551 |   1.6% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 855 |   0.5% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 379 |   0.2% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 13** | 208 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 14** | 96 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 355 | 128 | 227 | 0 | 0 | 0 | **CAA (227)** |
| **Era 3** | 5,682 | 2,390 | 1,500 | 110 | 1,679 | 3 | **SO (2,390)** |
| **Era 4** | 23,505 | 9,473 | 4,575 | 1,080 | 7,783 | 594 | **SO (9,473)** |
| **Era 5** | 38,246 | 14,762 | 6,307 | 4,159 | 9,403 | 3,615 | **SO (14,762)** |
| **Era 6** | 40,633 | 9,774 | 11,109 | 8,582 | 5,488 | 5,680 | **CAA (11,109)** |
| **Era 7** | 25,746 | 8,405 | 4,407 | 5,947 | 2,006 | 4,981 | **SO (8,405)** |
| **Era 8** | 15,942 | 4,297 | 1,547 | 3,749 | 566 | 5,783 | **GC (5,783)** |
| **Era 9** | 5,802 | 1,425 | 747 | 1,404 | 260 | 1,966 | **GC (1,966)** |
| **Era 10** | 2,551 | 472 | 347 | 1,069 | 115 | 548 | **KB (1,069)** |
| **Era 11** | 855 | 53 | 105 | 441 | 27 | 229 | **KB (441)** |
| **Era 12** | 379 | 25 | 29 | 201 | 12 | 112 | **KB (201)** |
| **Era 13** | 208 | 4 | 11 | 168 | 3 | 22 | **KB (168)** |
| **Era 14** | 96 | 4 | 4 | 41 | 42 | 5 | **KT (42)** |
| **SUMA** | **160,000** | **51,212** | **30,915** | **26,951** | **27,384** | **23,538** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **5.95** |  0.1% | 14.5% | 70.7% | 14.4% |  0.2% | **KB (33.5%)** |
| `4p-no-cienie` | **5.66** |  0.0% | 17.6% | 74.1% |  8.3% |  0.0% | **KB (31.6%)** |
| `4p-no-kabala` | **5.91** |  0.3% | 12.8% | 77.0% |  9.8% |  0.0% | **KB (31.5%)** |
| `4p-no-korona` | **5.60** |  0.4% | 23.1% | 67.0% |  9.5% |  0.1% | **CAA (36.1%)** |
| `4p-no-oficjum` | **5.73** |  0.2% | 16.7% | 73.1% | 10.0% |  0.0% | **KB (34.9%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **3.5 – 8.5** | 🟡 2.0–3.5 / 8.5–10.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 75 | 🟠 ≥ 60 | 🔴 < 60