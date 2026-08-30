# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.169

**Wersja Balansu:** `v1.0-alpha.169` | **Data:** 2026-08-30 22:41 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 0.54s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🟠 ** 77.0** | 🟠 77.0 | 33.3% | - | 39.6% | - | 29.4% | 31.0% | 🟠 WYMAGA UWAGI |
| `3p-cienie-korona-gildia` | 3 | 🟡 ** 88.3** | 🟡 88.3 | 33.3% | - | 32.0% | 31.2% | - | 36.8% | 🟡 AKCEPTOWALNY |
| `3p-cienie-korona-kabala` | 3 | 🟠 ** 70.0** | 🟠 70.0 | 33.3% | - | 35.3% | 39.2% | 25.5% | - | 🟠 WYMAGA UWAGI |
| `3p-korona-kabala-gildia` | 3 | 🟠 ** 70.8** | 🟠 70.8 | 33.3% | - | - | 37.2% | 25.4% | 37.4% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-alandalus-gildia` | 3 | 🟡 ** 85.0** | 🟡 85.0 | 33.3% | 36.2% | 29.1% | - | - | 34.7% | 🟡 AKCEPTOWALNY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 49.8** | 🔴 49.8 | 33.3% | 47.1% | 24.6% | - | 28.4% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 ** 52.7** | 🔴 52.7 | 33.3% | 32.6% | 22.4% | 44.9% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 ** 63.6** | 🔴 63.6 | 33.3% | 28.3% | - | - | 28.5% | 43.2% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🟠 ** 79.9** | 🟠 79.9 | 33.3% | 28.8% | - | 32.6% | - | 38.5% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-korona-kabala` | 3 | 🟡 ** 85.7** | 🟡 85.7 | 33.3% | 29.3% | - | 34.3% | 36.4% | - | 🟡 AKCEPTOWALNY |
| `4p-core` | 4 | 🟡 ** 84.3** | 🟡 84.3 | 25.0% | 22.4% | 23.9% | 28.9% | 24.8% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟡 ** 85.5** | 🟡 85.5 | 25.0% | 22.4% | - | 23.3% | 28.0% | 26.2% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟢 ** 92.0** | 🟢 92.0 | 25.0% | 23.0% | 24.5% | 26.1% | - | 26.4% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟢 ** 97.4** | 🟢 97.4 | 25.0% | 24.3% | 25.4% | - | 25.6% | 24.7% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟢 ** 93.7** | 🟢 93.7 | 25.0% | - | 23.3% | 26.2% | 24.8% | 25.7% | 🟢 ZBALANSOWANY |
| `5p-full` | 5 | 🟢 ** 97.2** | 🟢 97.2 | 20.0% | 19.9% | 20.5% | 20.2% | 20.2% | 19.2% | 🟢 ZBALANSOWANY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.53 🟡 | 0.1% 🟢 | 1.0% 🟢 | 1.22 🟢 | 6.22 🟢 | 8.27zł | 5.78 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 6.79 🟡 | 0.0% 🟢 | 2.9% 🟢 | 1.24 🟢 | 7.46 🟢 | 8.48zł | 6.55 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.21 🔴 | 0.9% 🟢 | 4.2% 🟢 | 1.33 🟢 | 6.27 🟢 | 6.12zł | 5.83 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.79 🟡 | 0.1% 🟢 | 5.0% 🟢 | 1.26 🟢 | 6.61 🟢 | 3.55zł | 5.97 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-gildia` | 6.12 🟢 | 0.0% 🟢 | 0.0% 🟢 | 1.8 🟢 | 7.57 🟢 | 10.17zł | 6.94 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 6.67 🟡 | 0.1% 🟢 | 0.3% 🟢 | 2.07 🔴 | 7.52 🟢 | 7.95zł | 6.46 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 6.54 🟡 | 0.0% 🟢 | 2.1% 🟢 | 2.0 🟡 | 7.29 🟢 | 7.39zł | 6.74 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 6.2 🟢 | 0.0% 🟢 | 0.6% 🟢 | 1.8 🟢 | 7.68 🟢 | 5.46zł | 6.77 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-gildia` | 6.14 🟢 | 0.0% 🟢 | 2.3% 🟢 | 1.73 🟢 | 7.64 🟢 | 5.14zł | 7.14 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 6.64 🟡 | 0.0% 🟢 | 3.1% 🟢 | 2.01 🔴 | 7.17 🟢 | 2.93zł | 6.41 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.03 🟢 | 0.0% 🟢 | 3.3% 🟢 | 1.85 🟡 | 7.42 🟢 | 7.33zł | 7.81 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.76 🟢 | 0.0% 🟢 | 3.5% 🟢 | 1.72 🟢 | 7.66 🟢 | 4.97zł | 8.29 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.73 🟢 | 0.0% 🟢 | 2.7% 🟢 | 1.69 🟢 | 7.81 🟢 | 9.1zł | 8.41 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.72 🟢 | 0.0% 🟢 | 0.5% 🟢 | 1.76 🟢 | 7.71 🟢 | 9.35zł | 8.2 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 6.16 🟢 | 0.0% 🟢 | 4.4% 🟢 | 1.14 🟢 | 6.86 🟢 | 7.73zł | 7.45 | 🟢 OPTYMALNA |
| `5p-full` | 5.41 🟢 | 0.0% 🟢 | 3.8% 🟢 | 1.62 🟢 | 7.58 🟢 | 8.97zł | 9.46 | 🟢 OPTYMALNA |

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
| **SO** | 28.6% | `3p-oficjum-alandalus-kabala` | +13.8% | 🟡 DOMINUJE |
| **KB** | 31.3% | `3p-oficjum-alandalus-korona` | +11.6% | 🟡 DOMINUJE |
| **CAA** | 27.3% | `3p-oficjum-alandalus-korona` | -10.9% | 🟡 SŁABA |
| **GC** | 31.3% | `3p-oficjum-kabala-gildia` | +9.9% | 🟡 DOMINUJE |
| **KT** | 27.0% | `3p-korona-kabala-gildia` | -7.9% | 🟡 SŁABA |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `3p-oficjum-alandalus-kabala` | 🔴 ** 49.8** | SO dominuje (47.1% vs ideal 33.3%) |
| `3p-oficjum-alandalus-korona` | 🔴 ** 52.7** | KB dominuje (44.9% vs ideal 33.3%) |
| `3p-oficjum-kabala-gildia` | 🔴 ** 63.6** | GC dominuje (43.2% vs ideal 33.3%) |
| `3p-cienie-korona-kabala` | 🟠 ** 70.0** | KT za słaba (25.5% vs ideal 33.3%) |
| `3p-korona-kabala-gildia` | 🟠 ** 70.8** | KT za słaba (25.4% vs ideal 33.3%) |
| `3p-cienie-kabala-gildia` | 🟠 ** 77.0** | CAA dominuje (39.6% vs ideal 33.3%) |
| `3p-oficjum-korona-gildia` | 🟠 ** 79.9** | GC dominuje (38.5% vs ideal 33.3%) |
| `4p-core` | 🟡 ** 84.3** | KB dominuje (28.9% vs ideal 25.0%) |
| `3p-oficjum-alandalus-gildia` | 🟡 ** 85.0** | CAA za słaba (29.1% vs ideal 33.3%) |
| `4p-no-cienie` | 🟡 ** 85.5** | KT dominuje (28.0% vs ideal 25.0%) |
| `3p-oficjum-korona-kabala` | 🟡 ** 85.7** | SO za słaba (29.3% vs ideal 33.3%) |
| `3p-cienie-korona-gildia` | 🟡 ** 88.3** | GC dominuje (36.8% vs ideal 33.3%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 1** | 0 |   0.0% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 2** | 83 |   0.1% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 3,215 |   2.0% | `█                   ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 14,294 |   9.0% | `████                ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 33,983 |  21.3% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 42,912 |  26.9% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 36,327 |  22.8% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 16,742 |  10.5% | `█████               ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 6,619 |   4.2% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 3,834 |   2.4% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 836 |   0.5% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 551 |   0.3% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 1** | 0 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 2** | 83 | 19 | 64 | 0 | 0 | 0 | **CAA (64)** |
| **Era 3** | 3,215 | 394 | 954 | 1,209 | 634 | 24 | **KB (1,209)** |
| **Era 4** | 14,294 | 1,809 | 3,736 | 2,273 | 5,292 | 1,184 | **KT (5,292)** |
| **Era 5** | 33,983 | 5,034 | 8,897 | 5,811 | 8,551 | 5,690 | **CAA (8,897)** |
| **Era 6** | 42,912 | 8,419 | 8,709 | 8,549 | 8,187 | 9,048 | **GC (9,048)** |
| **Era 7** | 36,327 | 9,286 | 4,867 | 9,098 | 4,302 | 8,774 | **SO (9,286)** |
| **Era 8** | 16,742 | 3,412 | 1,736 | 2,809 | 1,773 | 7,012 | **GC (7,012)** |
| **Era 9** | 6,619 | 1,885 | 619 | 1,878 | 635 | 1,602 | **SO (1,885)** |
| **Era 10** | 3,834 | 885 | 291 | 1,945 | 117 | 596 | **KB (1,945)** |
| **Era 11** | 836 | 146 | 124 | 312 | 48 | 206 | **KB (312)** |
| **Era 12** | 551 | 114 | 48 | 170 | 45 | 174 | **GC (174)** |
| **SUMA** | **159,396** | **31,403** | **30,045** | **34,054** | **29,584** | **34,310** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **6.03** |  0.1% | 14.6% | 69.1% | 15.8% |  0.3% | **KB (31.2%)** |
| `4p-no-cienie` | **5.76** |  0.0% | 12.8% | 81.1% |  6.2% |  0.0% | **GC (30.3%)** |
| `4p-no-kabala` | **5.73** |  0.1% | 13.6% | 80.3% |  6.0% |  0.0% | **GC (29.1%)** |
| `4p-no-korona` | **5.72** |  0.1% | 14.5% | 78.4% |  6.9% |  0.1% | **GC (31.5%)** |
| `4p-no-oficjum` | **6.16** |  0.0% | 11.0% | 70.5% | 18.3% |  0.2% | **KB (34.3%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **3.5 – 8.5** | 🟡 2.0–3.5 / 8.5–10.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 80 | 🟠 ≥ 65 | 🔴 < 65