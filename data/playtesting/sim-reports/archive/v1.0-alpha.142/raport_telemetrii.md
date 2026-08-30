# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.142

**Wersja Balansu:** `v1.0-alpha.142` | **Data:** 2026-08-30 10:20 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 0.58s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🟠 ** 72.1** | 🟠 72.1 | 33.3% | - | 40.9% | - | 29.2% | 29.8% | 🟠 WYMAGA UWAGI |
| `3p-cienie-korona-gildia` | 3 | 🟠 ** 78.0** | 🟠 78.0 | 33.3% | - | 33.1% | 28.2% | - | 38.7% | 🟠 WYMAGA UWAGI |
| `3p-cienie-korona-kabala` | 3 | 🟠 ** 72.9** | 🟠 72.9 | 33.3% | - | 37.8% | 36.2% | 26.0% | - | 🟠 WYMAGA UWAGI |
| `3p-korona-kabala-gildia` | 3 | 🟠 ** 73.9** | 🟠 73.9 | 33.3% | - | - | 32.4% | 27.7% | 40.0% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-alandalus-gildia` | 3 | 🟡 ** 82.7** | 🟡 82.7 | 33.3% | 34.4% | 28.6% | - | - | 37.0% | 🟡 AKCEPTOWALNY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 52.7** | 🔴 52.7 | 33.3% | 46.1% | 24.9% | - | 29.0% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 ** 56.6** | 🔴 56.6 | 33.3% | 35.9% | 22.1% | 42.1% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 ** 57.1** | 🔴 57.1 | 33.3% | 26.5% | - | - | 28.5% | 45.0% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🟠 ** 70.8** | 🟠 70.8 | 33.3% | 28.0% | - | 30.9% | - | 41.1% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-korona-kabala` | 3 | 🟡 ** 87.7** | 🟡 87.7 | 33.3% | 31.1% | - | 31.9% | 37.0% | - | 🟡 AKCEPTOWALNY |
| `4p-core` | 4 | 🟢 ** 96.4** | 🟢 96.4 | 25.0% | 24.3% | 24.3% | 25.6% | 25.8% | - | 🟢 ZBALANSOWANY |
| `4p-no-cienie` | 4 | 🟠 ** 78.7** | 🟠 78.7 | 25.0% | 22.4% | - | 21.6% | 29.3% | 26.7% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🟡 ** 84.1** | 🟡 84.1 | 25.0% | 23.1% | 26.4% | 22.3% | - | 28.3% | 🟡 AKCEPTOWALNY |
| `4p-no-korona` | 4 | 🟢 ** 97.8** | 🟢 97.8 | 25.0% | 25.1% | 25.7% | - | 24.8% | 24.4% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟢 ** 92.3** | 🟢 92.3 | 25.0% | - | 24.4% | 23.2% | 26.5% | 26.0% | 🟢 ZBALANSOWANY |
| `5p-full` | 5 | 🟡 ** 80.2** | 🟡 80.2 | 20.0% | 20.3% | 22.7% | 16.9% | 22.4% | 17.8% | 🟡 AKCEPTOWALNY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.48 🟢 | 0.1% 🟢 | 1.1% 🟢 | 1.22 🟢 | 6.16 🟢 | 7.92zł | 5.79 | 🟢 OPTYMALNA |
| `3p-cienie-korona-gildia` | 6.8 🟡 | 0.0% 🟢 | 4.1% 🟢 | 1.25 🟢 | 7.47 🟢 | 7.75zł | 6.57 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.24 🔴 | 0.9% 🟢 | 5.1% 🟢 | 1.33 🟢 | 6.37 🟢 | 6.42zł | 5.85 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.89 🟡 | 0.2% 🟢 | 6.2% 🟢 | 1.28 🟢 | 6.73 🟢 | 2.77zł | 6.0 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-gildia` | 6.1 🟢 | 0.0% 🟢 | 0.4% 🟢 | 1.81 🟡 | 7.63 🟢 | 9.49zł | 6.98 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 6.59 🟡 | 0.1% 🟢 | 0.6% 🟢 | 2.07 🔴 | 7.47 🟢 | 8.13zł | 6.47 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 6.64 🟡 | 0.0% 🟢 | 3.5% 🟢 | 2.07 🔴 | 7.61 🟢 | 7.54zł | 6.82 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 6.19 🟢 | 0.0% 🟢 | 0.9% 🟢 | 1.84 🟡 | 7.7 🟢 | 4.57zł | 6.81 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-gildia` | 6.22 🟢 | 0.0% 🟢 | 4.0% 🟢 | 1.77 🟢 | 7.73 🟢 | 4.21zł | 7.18 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 6.66 🟡 | 0.0% 🟢 | 4.4% 🟢 | 2.05 🔴 | 7.15 🟢 | 2.91zł | 6.42 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.09 🟢 | 0.0% 🟢 | 4.6% 🟢 | 1.9 🟡 | 7.66 🟢 | 7.54zł | 7.91 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.79 🟢 | 0.0% 🟢 | 5.2% 🟢 | 1.77 🟢 | 7.76 🟢 | 4.16zł | 8.33 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.76 🟢 | 0.0% 🟢 | 4.3% 🟢 | 1.72 🟢 | 7.96 🟢 | 8.43zł | 8.5 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.68 🟢 | 0.0% 🟢 | 1.0% 🟢 | 1.78 🟢 | 7.67 🟢 | 8.85zł | 8.22 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 6.16 🟢 | 0.0% 🟢 | 5.6% 🟢 | 1.15 🟢 | 6.91 🟢 | 7.12zł | 7.49 | 🟢 OPTYMALNA |
| `5p-full` | 5.44 🟢 | 0.0% 🟢 | 5.4% 🟢 | 1.65 🟢 | 7.62 🟢 | 8.44zł | 9.52 | 🟢 OPTYMALNA |

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
| **SO** | 28.8% | `3p-oficjum-alandalus-kabala` | +12.8% | 🟡 DOMINUJE |
| **GC** | 32.3% | `3p-oficjum-kabala-gildia` | +11.7% | 🟡 DOMINUJE |
| **CAA** | 28.3% | `3p-oficjum-alandalus-korona` | -11.2% | 🟡 SŁABA |
| **KB** | 28.3% | `3p-oficjum-alandalus-korona` | +8.8% | 🟡 DOMINUJE |
| **KT** | 27.8% | `3p-cienie-korona-kabala` | -7.3% | 🟡 SŁABA |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `3p-oficjum-alandalus-kabala` | 🔴 ** 52.7** | SO dominuje (46.1% vs ideal 33.3%) |
| `3p-oficjum-alandalus-korona` | 🔴 ** 56.6** | CAA za słaba (22.1% vs ideal 33.3%) |
| `3p-oficjum-kabala-gildia` | 🔴 ** 57.1** | GC dominuje (45.0% vs ideal 33.3%) |
| `3p-oficjum-korona-gildia` | 🟠 ** 70.8** | GC dominuje (41.1% vs ideal 33.3%) |
| `3p-cienie-kabala-gildia` | 🟠 ** 72.1** | CAA dominuje (40.9% vs ideal 33.3%) |
| `3p-cienie-korona-kabala` | 🟠 ** 72.9** | KT za słaba (26.0% vs ideal 33.3%) |
| `3p-korona-kabala-gildia` | 🟠 ** 73.9** | GC dominuje (40.0% vs ideal 33.3%) |
| `3p-cienie-korona-gildia` | 🟠 ** 78.0** | GC dominuje (38.7% vs ideal 33.3%) |
| `4p-no-cienie` | 🟠 ** 78.7** | KT dominuje (29.3% vs ideal 25.0%) |
| `5p-full` | 🟡 ** 80.2** | KB za słaba (16.9% vs ideal 20.0%) |
| `3p-oficjum-alandalus-gildia` | 🟡 ** 82.7** | CAA za słaba (28.6% vs ideal 33.3%) |
| `4p-no-kabala` | 🟡 ** 84.1** | GC dominuje (28.3% vs ideal 25.0%) |
| `3p-oficjum-korona-kabala` | 🟡 ** 87.7** | KT dominuje (37.0% vs ideal 33.3%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 1** | 0 |   0.0% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 2** | 152 |   0.1% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 2,317 |   1.5% | `█                   ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 14,621 |   9.2% | `█████               ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 34,381 |  21.6% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 42,422 |  26.6% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 36,301 |  22.8% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 17,217 |  10.8% | `█████               ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 6,636 |   4.2% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 3,903 |   2.4% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 822 |   0.5% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 548 |   0.3% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 1** | 0 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 2** | 152 | 10 | 142 | 0 | 0 | 0 | **CAA (142)** |
| **Era 3** | 2,317 | 344 | 1,117 | 202 | 637 | 17 | **CAA (1,117)** |
| **Era 4** | 14,621 | 1,805 | 4,160 | 2,227 | 5,319 | 1,110 | **KT (5,319)** |
| **Era 5** | 34,381 | 5,155 | 9,288 | 5,367 | 9,218 | 5,353 | **CAA (9,288)** |
| **Era 6** | 42,422 | 8,411 | 8,655 | 7,666 | 8,448 | 9,242 | **GC (9,242)** |
| **Era 7** | 36,301 | 9,384 | 4,848 | 8,259 | 4,246 | 9,564 | **GC (9,564)** |
| **Era 8** | 17,217 | 3,481 | 1,765 | 2,781 | 1,723 | 7,467 | **GC (7,467)** |
| **Era 9** | 6,636 | 1,974 | 661 | 1,751 | 644 | 1,606 | **SO (1,974)** |
| **Era 10** | 3,903 | 888 | 287 | 1,964 | 127 | 637 | **KB (1,964)** |
| **Era 11** | 822 | 131 | 101 | 324 | 56 | 210 | **KB (324)** |
| **Era 12** | 548 | 98 | 41 | 176 | 53 | 180 | **GC (180)** |
| **SUMA** | **159,320** | **31,681** | **31,065** | **30,717** | **30,471** | **35,386** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **6.09** |  0.1% | 13.1% | 70.7% | 15.7% |  0.4% | **KB (27.5%)** |
| `4p-no-cienie` | **5.79** |  0.0% | 12.0% | 81.7% |  6.3% |  0.0% | **GC (30.1%)** |
| `4p-no-kabala` | **5.76** |  0.2% | 12.8% | 81.2% |  5.8% |  0.0% | **GC (31.8%)** |
| `4p-no-korona` | **5.68** |  0.2% | 15.3% | 78.1% |  6.4% |  0.0% | **GC (32.0%)** |
| `4p-no-oficjum` | **6.16** |  0.1% | 11.1% | 70.0% | 18.5% |  0.3% | **KB (30.5%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **3.5 – 8.5** | 🟡 2.0–3.5 / 8.5–10.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 80 | 🟠 ≥ 65 | 🔴 < 65