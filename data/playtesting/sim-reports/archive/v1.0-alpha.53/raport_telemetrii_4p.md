# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.53

**Wersja Balansu:** `v1.0-alpha.53` | **Data:** 2026-08-23 15:48 | **Wielkość Próby:** 2000 gier/setup (32000 gier łącznie) | **Czas Symulacji:** 4.36s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🔴 ** 45.6** | 🟡 84.6 | 25.0% | 23.2% | 23.4% | 29.0% | 24.4% | - | 🔴 ODCHYLONY |
| `4p-no-cienie` | 4 | 🔴 ** 22.0** | 🟠 72.9 | 25.0% | 30.3% | - | 21.5% | 27.2% | 21.0% | 🔴 ODCHYLONY |
| `4p-no-kabala` | 4 | 🟠 ** 60.7** | 🟡 77.0 | 25.0% | 24.0% | 21.6% | 30.6% | - | 23.8% | 🟠 WYMAGA UWAGI |
| `4p-no-korona` | 4 | 🔴 ** 16.3** | 🟠 74.8 | 25.0% | 28.3% | 26.4% | - | 26.5% | 18.8% | 🔴 ODCHYLONY |
| `4p-no-oficjum` | 4 | 🔴 ** 50.7** | 🟠 74.7 | 25.0% | - | 21.1% | 30.8% | 25.4% | 22.8% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.87 🟢 | 0.0% 🟢 | 6.3% 🟢 | 1.58 🟢 | 6.02 🔴 | 6.9zł | 8.01 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.48 🟢 | 0.0% 🟢 | 7.4% 🟢 | 1.43 🟢 | 6.1 🔴 | 2.78zł | 8.57 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.86 🟢 | 0.0% 🟢 | 6.1% 🟢 | 1.55 🟢 | 6.67 🔴 | 7.55zł | 8.55 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.45 🟢 | 0.0% 🟢 | 2.0% 🟢 | 1.5 🟢 | 5.99 🔴 | 7.23zł | 8.27 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.54 🟢 | 0.0% 🟢 | 4.8% 🟢 | 1.0 🟢 | 5.41 🔴 | 7.13zł | 7.92 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | ⚠️ Ostrzeżenie Witalności | 0.617 | Przedwczesne Zwycięstwa (Era 1-2): 0.5% gier (>0.5%), Ekstremalny Deadlock (Era 10+): 2.4% gier (>1.0%) |
| `4p-no-cienie` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 39/607 wygranych (<8%) — gra tylko skazania |
| `4p-no-kabala` | ⚠️ Ostrzeżenie Witalności | 0.237 | Przedwczesne Zwycięstwa (Era 1-2): 0.9% gier (>0.5%) |
| `4p-no-korona` | ⚠️ Ostrzeżenie Witalności | 1.522 | Przedwczesne Zwycięstwa (Era 1-2): 1.2% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 6.1% gier (>6.0%), Martwa ścieżka stosy (swiete-oficjum): 17/567 wygranych (<8%) — gra tylko skazania |
| `4p-no-oficjum` | ⚠️ Ostrzeżenie Witalności | 0.387 | Przedwczesne Zwycięstwa (Era 1-2): 1.1% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 7.2% gier (>6.0%) |

## 3.1. Frakcje Wymagające Uwagi

| Frakcja | Śr. Win Share (wszystkie setupy) | Najgorszy Setup | Max Odchylenie od Ideału | Status |
| :--- | :---: | :--- | :---: | :--- |
| **GC** | 21.6% | `4p-no-korona` | -6.2% | 🟡 SŁABA |
| **KB** | 28.0% | `4p-no-oficjum` | +5.8% | 🟡 DOMINUJE |
| **SO** | 26.4% | `4p-no-cienie` | +5.3% | 🟡 DOMINUJE |
| **CAA** | 23.1% | `4p-no-oficjum` | -3.9% | 🟢 OK |
| **KT** | 25.9% | `4p-no-cienie` | +2.2% | 🟢 OK |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `4p-no-korona` | 🔴 ** 16.3** | GC za słaba (18.8% vs ideal 25.0%) |
| `4p-no-cienie` | 🔴 ** 22.0** | SO dominuje (30.3% vs ideal 25.0%) |
| `4p-core` | 🔴 ** 45.6** | KB dominuje (29.0% vs ideal 25.0%) |
| `4p-no-oficjum` | 🔴 ** 50.7** | KB dominuje (30.8% vs ideal 25.0%) |
| `4p-no-kabala` | 🟠 ** 60.7** | KB dominuje (30.6% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 77 |   0.8% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 515 |   5.1% | `███                 ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 1,673 |  16.7% | `████████            ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 2,370 |  23.7% | `████████████        ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 2,877 |  28.8% | `██████████████      ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 1,417 |  14.2% | `███████             ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 748 |   7.5% | `████                ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 253 |   2.5% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 48 |   0.5% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 11** | 18 |   0.2% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 3 |   0.0% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 13** | 1 |   0.0% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 77 | 0 | 74 | 0 | 3 | 0 | **CAA (74)** |
| **Era 3** | 515 | 28 | 194 | 183 | 109 | 1 | **CAA (194)** |
| **Era 4** | 1,673 | 393 | 492 | 255 | 480 | 53 | **CAA (492)** |
| **Era 5** | 2,370 | 691 | 285 | 607 | 554 | 233 | **SO (691)** |
| **Era 6** | 2,877 | 366 | 599 | 902 | 541 | 469 | **KB (902)** |
| **Era 7** | 1,417 | 282 | 128 | 207 | 286 | 514 | **GC (514)** |
| **Era 8** | 748 | 180 | 52 | 48 | 59 | 409 | **GC (409)** |
| **Era 9** | 253 | 154 | 19 | 15 | 26 | 39 | **SO (154)** |
| **Era 10** | 48 | 16 | 2 | 16 | 6 | 8 | **SO (16)** |
| **Era 11** | 18 | 5 | 2 | 5 | 4 | 2 | **SO (5)** |
| **Era 12** | 3 | 2 | 1 | 0 | 0 | 0 | **SO (2)** |
| **Era 13** | 1 | 0 | 0 | 0 | 1 | 0 | **KT (1)** |
| **SUMA** | **10,000** | **2,117** | **1,848** | **2,238** | **2,069** | **1,728** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–9 (Późne) % | Ery 10+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **5.87** |  0.5% | 20.2% | 63.6% | 13.3% |  2.4% | **KB (40.9%)** |
| `4p-no-cienie` | **5.48** |  0.1% | 24.1% | 68.0% |  7.6% |  0.2% | **KB (29.9%)** |
| `4p-no-kabala` | **5.86** |  0.9% | 17.6% | 67.8% | 13.0% |  0.6% | **KB (43.1%)** |
| `4p-no-korona` | **5.45** |  1.2% | 26.4% | 64.0% |  8.1% |  0.2% | **CAA (32.0%)** |
| `4p-no-oficjum` | **5.54** |  1.1% | 21.1% | 69.8% |  8.0% |  0.1% | **KB (41.4%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **2.0 – 4.5** | 🟡 1.5–2.0 / 4.5–5.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 75 | 🟠 ≥ 60 | 🔴 < 60