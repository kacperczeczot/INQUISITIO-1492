# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.49

**Wersja Balansu:** `v1.0-alpha.49` | **Data:** 2026-08-23 14:52 | **Wielkość Próby:** 5000 gier/setup (80000 gier łącznie) | **Czas Symulacji:** 10.15s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🔴 ** 34.3** | 🔴 44.7 | 25.0% | 37.7% | 16.0% | 26.7% | 19.6% | - | 🔴 ODCHYLONY |
| `4p-no-cienie` | 4 | 🔴 ** 36.1** | 🔴 48.0 | 25.0% | 38.0% | - | 21.4% | 17.8% | 22.8% | 🔴 ODCHYLONY |
| `4p-no-kabala` | 4 | 🔴 ** 42.8** | 🔴 56.8 | 25.0% | 33.8% | 16.1% | 25.5% | - | 24.6% | 🔴 ODCHYLONY |
| `4p-no-korona` | 4 | 🔴 ** 20.2** | 🔴 39.0 | 25.0% | 41.1% | 18.0% | - | 19.5% | 21.4% | 🔴 ODCHYLONY |
| `4p-no-oficjum` | 4 | 🔴 ** 24.6** | 🔴 40.7 | 25.0% | - | 15.1% | 33.4% | 16.8% | 34.6% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.25 🟢 | 0.0% 🟢 | 4.3% 🟢 | 2.05 🔴 | 5.15 🔴 | 6.25zł | 8.15 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 4.92 🟡 | 0.0% 🟢 | 4.7% 🟢 | 1.81 🟡 | 5.2 🔴 | 2.83zł | 8.57 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-kabala` | 5.06 🟢 | 0.0% 🟢 | 3.8% 🟢 | 1.92 🟡 | 5.17 🔴 | 7.05zł | 8.47 | 🟢 OPTYMALNA |
| `4p-no-korona` | 4.87 🟡 | 0.0% 🟢 | 1.2% 🟢 | 1.9 🟡 | 5.06 🔴 | 6.74zł | 8.28 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-oficjum` | 5.03 🟢 | 0.0% 🟢 | 3.3% 🟢 | 1.29 🟢 | 4.85 🟡 | 6.63zł | 8.01 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | ⚠️ Ostrzeżenie Witalności | 0.265 | Przedwczesne Zwycięstwa (Era 1-2): 0.6% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 7.1% gier (>6.0%) |
| `4p-no-cienie` | ⚠️ Ostrzeżenie Witalności | 0.285 | Zbyt Wczesne Zakończenia (Era 1-3): 7.7% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.92 Er (<5.0 Er) |
| `4p-no-kabala` | ⚠️ Ostrzeżenie Witalności | 0.282 | Przedwczesne Zwycięstwa (Era 1-2): 0.8% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 6.8% gier (>6.0%) |
| `4p-no-korona` | ⚠️ Ostrzeżenie Witalności | 0.656 | Przedwczesne Zwycięstwa (Era 1-2): 0.9% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 8.3% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.87 Er (<5.0 Er) |
| `4p-no-oficjum` | ⚠️ Ostrzeżenie Witalności | 0.501 | Przedwczesne Zwycięstwa (Era 1-2): 0.9% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 8.7% gier (>6.0%) |

## 3.1. Frakcje Wymagające Uwagi

| Frakcja | Śr. Win Share (wszystkie setupy) | Najgorszy Setup | Max Odchylenie od Ideału | Status |
| :--- | :---: | :--- | :---: | :--- |
| **SO** | 37.6% | `4p-no-korona` | +16.1% | 🟡 DOMINUJE |
| **CAA** | 16.3% | `4p-no-oficjum` | -9.9% | 🟡 SŁABA |
| **GC** | 25.9% | `4p-no-oficjum` | +9.6% | 🟡 DOMINUJE |
| **KB** | 26.7% | `4p-no-oficjum` | +8.4% | 🟡 DOMINUJE |
| **KT** | 18.4% | `4p-no-oficjum` | -8.2% | 🟡 SŁABA |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `4p-no-korona` | 🔴 ** 20.2** | SO dominuje (41.1% vs ideal 25.0%) |
| `4p-no-oficjum` | 🔴 ** 24.6** | CAA za słaba (15.1% vs ideal 25.0%) |
| `4p-core` | 🔴 ** 34.3** | SO dominuje (37.7% vs ideal 25.0%) |
| `4p-no-cienie` | 🔴 ** 36.1** | SO dominuje (38.0% vs ideal 25.0%) |
| `4p-no-kabala` | 🔴 ** 42.8** | CAA za słaba (16.1% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 179 |   0.7% | `                    ` | 🔴 Za wczesna (sprint / brak intrygi) |
| **Era 3** | 1,753 |   7.0% | `████                ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 6,477 |  25.9% | `█████████████       ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 8,166 |  32.7% | `████████████████    ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 6,384 |  25.5% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 1,506 |   6.0% | `███                 ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 399 |   1.6% | `█                   ` | 🟡 Przedłużona |
| **Era 9** | 114 |   0.5% | `                    ` | 🔴 Limit Er (Deadlock) |
| **Era 10** | 19 |   0.1% | `                    ` | 🔴 Limit Er (Deadlock) |
| **Era 11** | 3 |   0.0% | `                    ` | 🔴 Limit Er (Deadlock) |

### 4.2. Rozkład Szans Wygranych Frakcji w poszczególnych Erach (% Wygranych Frakcji w danej Erze)

*Wiersze sumują się do 100.0% — wskazują która frakcja dominuje w danej fazie czasowej partii.*

| Era Końca Gry | Gry w Erze | SO % | CAA % | KB % | KT % | GC % | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 179 |   2.2% |  78.8% |   1.7% |  17.3% |   0.0% | **CAA (78.8%)** |
| **Era 3** | 1,753 |  15.6% |  24.8% |  25.2% |  31.8% |   2.6% | **KT (31.8%)** |
| **Era 4** | 6,477 |  34.0% |  14.3% |  23.6% |  17.3% |  11.0% | **SO (34.0%)** |
| **Era 5** | 8,166 |  36.8% |   8.6% |  24.9% |  11.3% |  18.4% | **SO (36.8%)** |
| **Era 6** | 6,384 |  21.6% |  14.3% |  17.7% |  12.8% |  33.7% | **GC (33.7%)** |
| **Era 7** | 1,506 |  28.7% |   6.7% |  12.0% |  13.1% |  39.5% | **GC (39.5%)** |
| **Era 8** | 399 |  34.3% |   9.0% |   7.8% |   8.8% |  40.1% | **GC (40.1%)** |
| **Era 9** | 114 |  79.8% |   4.4% |   3.5% |   4.4% |   7.9% | **SO (79.8%)** |
| **Era 10** | 19 |  42.1% |  10.5% |  10.5% |  21.1% |  15.8% | **SO (42.1%)** |
| **Era 11** | 3 |  33.3% |   0.0% |  33.3% |   0.0% |  33.3% | **SO (33.3%)** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Era 1-4 (Wczesne / Szybkie) % | Era 5-7 (Złote Okno) % | Era 8+ (Długie) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **5.25** |  30.2% |  64.8% |   5.0% | **SO (37.8%)** |
| `4p-no-cienie` | **4.92** |  34.4% |  64.6% |   1.0% | **GC (40.8%)** |
| `4p-no-kabala` | **5.06** |  31.4% |  67.2% |   1.4% | **GC (36.9%)** |
| `4p-no-korona` | **4.87** |  41.7% |  56.7% |   1.6% | **GC (33.6%)** |
| `4p-no-oficjum` | **5.03** |  30.5% |  67.8% |   1.7% | **GC (55.9%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **2.0 – 4.5** | 🟡 1.5–2.0 / 4.5–5.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 75 | 🟠 ≥ 60 | 🔴 < 60