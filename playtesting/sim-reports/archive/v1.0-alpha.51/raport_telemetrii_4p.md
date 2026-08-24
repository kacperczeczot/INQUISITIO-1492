# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.51

**Wersja Balansu:** `v1.0-alpha.51` | **Data:** 2026-08-23 15:15 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 17.13s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🔴 ** 44.6** | 🟠 63.1 | 25.0% | 31.8% | 16.9% | 25.2% | 26.1% | - | 🔴 ODCHYLONY |
| `4p-no-cienie` | 4 | 🔴 ** 59.7** | 🟡 75.9 | 25.0% | 30.9% | - | 21.5% | 24.0% | 23.6% | 🔴 ODCHYLONY |
| `4p-no-kabala` | 4 | 🔴 ** 49.1** | 🟠 67.8 | 25.0% | 27.4% | 17.3% | 25.7% | - | 29.5% | 🔴 ODCHYLONY |
| `4p-no-korona` | 4 | 🔴 ** 27.1** | 🟠 61.3 | 25.0% | 33.6% | 19.1% | - | 26.0% | 21.2% | 🔴 ODCHYLONY |
| `4p-no-oficjum` | 4 | 🔴 ** 27.3** | 🟠 64.4 | 25.0% | - | 18.0% | 30.8% | 22.3% | 28.9% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.26 🟢 | 0.0% 🟢 | 4.4% 🟢 | 2.03 🔴 | 5.19 🔴 | 6.82zł | 8.06 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 4.94 🟡 | 0.0% 🟢 | 4.7% 🟢 | 1.81 🟡 | 5.22 🔴 | 2.96zł | 8.52 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-kabala` | 5.16 🟢 | 0.0% 🟢 | 4.0% 🟢 | 1.94 🟡 | 5.49 🔴 | 7.41zł | 8.52 | 🟢 OPTYMALNA |
| `4p-no-korona` | 4.86 🟡 | 0.0% 🟢 | 1.1% 🟢 | 1.89 🟡 | 5.05 🔴 | 7.28zł | 8.16 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-oficjum` | 4.9 🟡 | 0.0% 🟢 | 3.2% 🟢 | 1.25 🟢 | 4.63 🟡 | 7.09zł | 7.84 | ⚠️ WARTOŚCI BRZEGOWE |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | ⚠️ Ostrzeżenie Witalności | 0.347 | Przedwczesne Zwycięstwa (Era 1-2): 0.7% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 7.7% gier (>6.0%) |
| `4p-no-cienie` | ⚠️ Ostrzeżenie Witalności | 0.239 | Zbyt Wczesne Zakończenia (Era 1-3): 7.4% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.94 Er (<5.0 Er) |
| `4p-no-kabala` | ⚠️ Ostrzeżenie Witalności | 0.323 | Przedwczesne Zwycięstwa (Era 1-2): 1.1% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 6.6% gier (>6.0%) |
| `4p-no-korona` | ⚠️ Ostrzeżenie Witalności | 0.814 | Przedwczesne Zwycięstwa (Era 1-2): 1.2% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 8.9% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.86 Er (<5.0 Er) |
| `4p-no-oficjum` | ⚠️ Ostrzeżenie Witalności | 0.860 | Przedwczesne Zwycięstwa (Era 1-2): 1.3% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 9.9% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.90 Er (<5.0 Er) |

## 3.1. Frakcje Wymagające Uwagi

| Frakcja | Śr. Win Share (wszystkie setupy) | Najgorszy Setup | Max Odchylenie od Ideału | Status |
| :--- | :---: | :--- | :---: | :--- |
| **SO** | 30.9% | `4p-no-korona` | +8.6% | 🟡 DOMINUJE |
| **CAA** | 17.8% | `4p-core` | -8.1% | 🟡 SŁABA |
| **KB** | 25.8% | `4p-no-oficjum` | +5.8% | 🟡 DOMINUJE |
| **GC** | 25.8% | `4p-no-kabala` | +4.5% | 🟢 OK |
| **KT** | 24.6% | `4p-no-oficjum` | -2.7% | 🟢 OK |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `4p-no-korona` | 🔴 ** 27.1** | SO dominuje (33.6% vs ideal 25.0%) |
| `4p-no-oficjum` | 🔴 ** 27.3** | CAA za słaba (18.0% vs ideal 25.0%) |
| `4p-core` | 🔴 ** 44.6** | CAA za słaba (16.9% vs ideal 25.0%) |
| `4p-no-kabala` | 🔴 ** 49.1** | CAA za słaba (17.3% vs ideal 25.0%) |
| `4p-no-cienie` | 🔴 ** 59.7** | SO dominuje (30.9% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 461 |   0.9% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 3,592 |   7.2% | `████                ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 13,164 |  26.3% | `█████████████       ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 16,224 |  32.4% | `████████████████    ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 12,056 |  24.1% | `████████████        ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 3,166 |   6.3% | `███                 ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 970 |   1.9% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 313 |   0.6% | `                    ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 46 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 11** | 8 |   0.0% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Szans Wygranych Frakcji w poszczególnych Erach (% Wygranych Frakcji w danej Erze)

*Wiersze sumują się do 100.0% — wskazują która frakcja dominuje w danej fazie czasowej partii.*

| Era Końca Gry | Gry w Erze | SO % | CAA % | KB % | KT % | GC % | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 461 |   0.2% |  84.6% |   3.0% |  12.1% |   0.0% | **CAA (84.6%)** |
| **Era 3** | 3,592 |  11.4% |  25.7% |  21.5% |  38.6% |   2.8% | **KT (38.6%)** |
| **Era 4** | 13,164 |  28.4% |  18.0% |  21.1% |  21.6% |  10.9% | **SO (28.4%)** |
| **Era 5** | 16,224 |  30.0% |   9.7% |  24.4% |  16.8% |  19.1% | **SO (30.0%)** |
| **Era 6** | 12,056 |  17.3% |  13.3% |  18.7% |  17.1% |  33.6% | **GC (33.6%)** |
| **Era 7** | 3,166 |  24.1% |   5.3% |  13.2% |  20.1% |  37.4% | **GC (37.4%)** |
| **Era 8** | 970 |  25.2% |   9.4% |   9.2% |  11.3% |  44.9% | **GC (44.9%)** |
| **Era 9** | 313 |  74.4% |   6.1% |   4.5% |   6.7% |   8.3% | **SO (74.4%)** |
| **Era 10** | 46 |  39.1% |   6.5% |  21.7% |  23.9% |   8.7% | **SO (39.1%)** |
| **Era 11** | 8 |  50.0% |   0.0% |  37.5% |  12.5% |   0.0% | **SO (50.0%)** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–9 (Późne) % | Ery 10+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **5.26** |  0.7% | 30.5% | 63.0% |  5.3% |  0.4% | **SO (29.8%)** |
| `4p-no-cienie` | **4.94** |  0.3% | 34.3% | 63.6% |  1.7% |  0.0% | **GC (40.3%)** |
| `4p-no-kabala` | **5.16** |  1.1% | 27.7% | 68.4% |  2.8% |  0.0% | **GC (42.1%)** |
| `4p-no-korona` | **4.86** |  1.2% | 41.3% | 55.5% |  1.9% |  0.0% | **GC (34.7%)** |
| `4p-no-oficjum` | **4.90** |  1.3% | 33.6% | 63.9% |  1.2% |  0.0% | **GC (49.9%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **2.0 – 4.5** | 🟡 1.5–2.0 / 4.5–5.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 75 | 🟠 ≥ 60 | 🔴 < 60