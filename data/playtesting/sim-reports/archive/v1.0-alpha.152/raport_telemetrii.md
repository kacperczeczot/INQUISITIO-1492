# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.152

**Wersja Balansu:** `v1.0-alpha.152` | **Data:** 2026-08-30 11:16 | **Wielkość Próby:** 100000 gier/setup (1600000 gier łącznie) | **Czas Symulacji:** 4.63s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🟠 ** 70.5** | 🟠 70.5 | 33.3% | - | 41.0% | - | 27.5% | 31.5% | 🟠 WYMAGA UWAGI |
| `3p-cienie-korona-gildia` | 3 | 🟡 ** 86.7** | 🟡 86.7 | 33.3% | - | 33.6% | 29.8% | - | 36.5% | 🟡 AKCEPTOWALNY |
| `3p-cienie-korona-kabala` | 3 | 🟠 ** 69.4** | 🟠 69.4 | 33.3% | - | 37.4% | 37.6% | 25.0% | - | 🟠 WYMAGA UWAGI |
| `3p-korona-kabala-gildia` | 3 | 🟠 ** 68.2** | 🟠 68.2 | 33.3% | - | - | 37.1% | 24.7% | 38.1% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-alandalus-gildia` | 3 | 🟡 ** 83.9** | 🟡 83.9 | 33.3% | 34.8% | 28.8% | - | - | 36.4% | 🟡 AKCEPTOWALNY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 48.9** | 🔴 48.9 | 33.3% | 47.6% | 25.8% | - | 26.6% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 ** 54.0** | 🔴 54.0 | 33.3% | 33.7% | 22.2% | 44.1% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 ** 53.0** | 🔴 53.0 | 33.3% | 26.8% | - | - | 27.0% | 46.3% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🟠 ** 75.2** | 🟠 75.2 | 33.3% | 27.5% | - | 33.2% | - | 39.3% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-korona-kabala` | 3 | 🟢 ** 91.9** | 🟢 91.9 | 33.3% | 30.8% | - | 34.2% | 35.0% | - | 🟢 ZBALANSOWANY |
| `4p-core` | 4 | 🟡 ** 87.9** | 🟡 87.9 | 25.0% | 23.5% | 24.4% | 28.3% | 23.9% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟡 ** 84.2** | 🟡 84.2 | 25.0% | 22.8% | - | 22.5% | 28.2% | 26.5% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟡 ** 87.9** | 🟡 87.9 | 25.0% | 22.2% | 25.8% | 24.6% | - | 27.4% | 🟡 AKCEPTOWALNY |
| `4p-no-korona` | 4 | 🟢 ** 95.4** | 🟢 95.4 | 25.0% | 24.6% | 26.2% | - | 23.9% | 25.2% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟢 ** 97.8** | 🟢 97.8 | 25.0% | - | 24.5% | 25.3% | 24.6% | 25.6% | 🟢 ZBALANSOWANY |
| `5p-full` | 5 | 🟡 ** 87.6** | 🟡 87.6 | 20.0% | 20.1% | 22.6% | 18.8% | 20.4% | 18.0% | 🟡 AKCEPTOWALNY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.52 🟡 | 0.2% 🟢 | 1.1% 🟢 | 1.22 🟢 | 6.29 🟢 | 8.6zł | 5.8 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 6.75 🟡 | 0.0% 🟢 | 2.9% 🟢 | 1.24 🟢 | 7.37 🟢 | 8.5zł | 6.54 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.16 🔴 | 0.9% 🟢 | 4.2% 🟢 | 1.32 🟢 | 6.27 🟢 | 6.24zł | 5.82 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.82 🟡 | 0.1% 🟢 | 5.2% 🟢 | 1.26 🟢 | 6.7 🟢 | 3.57zł | 6.02 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-gildia` | 6.11 🟢 | 0.0% 🟢 | 0.0% 🟢 | 1.81 🟡 | 7.59 🟢 | 10.23zł | 6.95 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-kabala` | 6.63 🟡 | 0.0% 🟢 | 0.4% 🟢 | 2.09 🔴 | 7.53 🟢 | 8.08zł | 6.48 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 6.56 🟡 | 0.0% 🟢 | 2.1% 🟢 | 2.02 🔴 | 7.43 🟢 | 7.38zł | 6.76 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 6.24 🟢 | 0.0% 🟢 | 0.6% 🟢 | 1.85 🟡 | 7.79 🟢 | 5.41zł | 6.83 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-gildia` | 6.18 🟢 | 0.0% 🟢 | 2.3% 🟢 | 1.76 🟢 | 7.65 🟢 | 5.02zł | 7.16 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 6.65 🟡 | 0.0% 🟢 | 3.1% 🟢 | 2.04 🔴 | 7.18 🟢 | 2.92zł | 6.43 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.06 🟢 | 0.0% 🟢 | 3.3% 🟢 | 1.9 🟡 | 7.56 🟢 | 7.29zł | 7.86 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.76 🟢 | 0.0% 🟢 | 3.6% 🟢 | 1.75 🟢 | 7.7 🟢 | 4.91zł | 8.33 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.72 🟢 | 0.0% 🟢 | 2.6% 🟢 | 1.7 🟢 | 7.83 🟢 | 8.95zł | 8.42 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.71 🟢 | 0.0% 🟢 | 0.5% 🟢 | 1.79 🟢 | 7.72 🟢 | 9.46zł | 8.23 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 6.14 🟢 | 0.0% 🟢 | 4.5% 🟢 | 1.13 🟢 | 6.93 🟢 | 7.75zł | 7.49 | 🟢 OPTYMALNA |
| `5p-full` | 5.42 🟢 | 0.0% 🟢 | 3.8% 🟢 | 1.64 🟢 | 7.62 🟢 | 8.92zł | 9.49 | 🟢 OPTYMALNA |

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
| **SO** | 28.6% | `3p-oficjum-alandalus-kabala` | +14.3% | 🟡 DOMINUJE |
| **GC** | 31.9% | `3p-oficjum-kabala-gildia` | +13.0% | 🟡 DOMINUJE |
| **CAA** | 28.4% | `3p-oficjum-alandalus-korona` | -11.1% | 🟡 SŁABA |
| **KB** | 30.5% | `3p-oficjum-alandalus-korona` | +10.8% | 🟡 DOMINUJE |
| **KT** | 26.1% | `3p-korona-kabala-gildia` | -8.6% | 🟡 SŁABA |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `3p-oficjum-alandalus-kabala` | 🔴 ** 48.9** | SO dominuje (47.6% vs ideal 33.3%) |
| `3p-oficjum-kabala-gildia` | 🔴 ** 53.0** | GC dominuje (46.3% vs ideal 33.3%) |
| `3p-oficjum-alandalus-korona` | 🔴 ** 54.0** | CAA za słaba (22.2% vs ideal 33.3%) |
| `3p-korona-kabala-gildia` | 🟠 ** 68.2** | KT za słaba (24.7% vs ideal 33.3%) |
| `3p-cienie-korona-kabala` | 🟠 ** 69.4** | KT za słaba (25.0% vs ideal 33.3%) |
| `3p-cienie-kabala-gildia` | 🟠 ** 70.5** | CAA dominuje (41.0% vs ideal 33.3%) |
| `3p-oficjum-korona-gildia` | 🟠 ** 75.2** | GC dominuje (39.3% vs ideal 33.3%) |
| `3p-oficjum-alandalus-gildia` | 🟡 ** 83.9** | CAA za słaba (28.8% vs ideal 33.3%) |
| `4p-no-cienie` | 🟡 ** 84.2** | KT dominuje (28.2% vs ideal 25.0%) |
| `3p-cienie-korona-gildia` | 🟡 ** 86.7** | KB za słaba (29.8% vs ideal 33.3%) |
| `5p-full` | 🟡 ** 87.6** | CAA dominuje (22.6% vs ideal 20.0%) |
| `4p-core` | 🟡 ** 87.9** | KB dominuje (28.3% vs ideal 25.0%) |
| `4p-no-kabala` | 🟡 ** 87.9** | SO za słaba (22.2% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 1** | 0 |   0.0% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 2** | 1,143 |   0.1% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 31,371 |   2.0% | `█                   ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 138,779 |   8.7% | `████                ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 340,796 |  21.4% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 430,851 |  27.0% | `██████████████      ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 367,867 |  23.1% | `████████████        ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 169,241 |  10.6% | `█████               ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 64,512 |   4.0% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 36,515 |   2.3% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 7,939 |   0.5% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 5,241 |   0.3% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 1** | 0 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 2** | 1,143 | 187 | 953 | 0 | 2 | 1 | **CAA (953)** |
| **Era 3** | 31,371 | 3,163 | 10,474 | 11,216 | 6,352 | 166 | **KB (11,216)** |
| **Era 4** | 138,779 | 17,558 | 41,060 | 22,216 | 46,009 | 11,936 | **KT (46,009)** |
| **Era 5** | 340,796 | 52,100 | 90,872 | 55,818 | 84,782 | 57,224 | **CAA (90,872)** |
| **Era 6** | 430,851 | 83,469 | 89,042 | 83,698 | 82,175 | 92,467 | **GC (92,467)** |
| **Era 7** | 367,867 | 93,738 | 50,893 | 89,252 | 41,684 | 92,300 | **SO (93,738)** |
| **Era 8** | 169,241 | 34,525 | 17,910 | 28,563 | 16,722 | 71,521 | **GC (71,521)** |
| **Era 9** | 64,512 | 18,534 | 6,539 | 18,363 | 5,652 | 15,424 | **SO (18,534)** |
| **Era 10** | 36,515 | 8,200 | 2,879 | 18,508 | 1,342 | 5,586 | **KB (18,508)** |
| **Era 11** | 7,939 | 1,407 | 1,250 | 2,875 | 507 | 1,900 | **KB (2,875)** |
| **Era 12** | 5,241 | 1,025 | 412 | 1,681 | 407 | 1,716 | **GC (1,716)** |
| **SUMA** | **1,594,255** | **313,906** | **312,284** | **332,190** | **285,634** | **350,241** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **6.06** |  0.1% | 13.8% | 70.0% | 15.8% |  0.3% | **KB (31.1%)** |
| `4p-no-cienie` | **5.76** |  0.0% | 12.3% | 81.9% |  5.8% |  0.0% | **GC (30.3%)** |
| `4p-no-kabala` | **5.72** |  0.2% | 14.1% | 79.8% |  6.0% |  0.0% | **GC (30.6%)** |
| `4p-no-korona` | **5.71** |  0.1% | 14.1% | 79.2% |  6.6% |  0.0% | **GC (31.6%)** |
| `4p-no-oficjum` | **6.14** |  0.1% | 11.0% | 70.9% | 17.7% |  0.2% | **KB (32.1%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **3.5 – 8.5** | 🟡 2.0–3.5 / 8.5–10.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 80 | 🟠 ≥ 65 | 🔴 < 65