[Strona główna](../../../../../README.md) > [v1.0-alpha.48](README.md) > [raport_telemetrii_4p](raport_telemetrii_4p.md)

---

# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.48

**Wersja Balansu:** `v1.0-alpha.48` | **Data:** 2026-08-23 14:38 | **Wielkość Próby:** 5000 gier/setup (80000 gier łącznie) | **Czas Symulacji:** 9.43s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🔴 ** 24.9** | 🔴 59.2 | 25.0% | 34.5% | 21.3% | 25.1% | 19.1% | - | 🔴 ODCHYLONY |
| `4p-no-cienie` | 4 | 🔴 ** 36.1** | 🔴 48.0 | 25.0% | 38.0% | - | 21.4% | 17.8% | 22.8% | 🔴 ODCHYLONY |
| `4p-no-kabala` | 4 | 🔴 ** 26.8** | 🟠 72.5 | 25.0% | 31.7% | 21.4% | 24.0% | - | 22.8% | 🔴 ODCHYLONY |
| `4p-no-korona` | 4 | 🔴 ** 12.3** | 🔴 45.5 | 25.0% | 38.9% | 22.7% | - | 19.0% | 19.5% | 🔴 ODCHYLONY |
| `4p-no-oficjum` | 4 | 🔴 ** 16.7** | 🔴 53.1 | 25.0% | - | 21.1% | 31.8% | 15.8% | 31.3% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.11 🟢 | 0.0% 🟢 | 4.2% 🟢 | 1.99 🟡 | 4.91 🟡 | 6.1zł | 8.01 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 4.92 🟡 | 0.0% 🟢 | 4.7% 🟢 | 1.81 🟡 | 5.2 🔴 | 2.83zł | 8.57 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-kabala` | 4.93 🟡 | 0.0% 🟢 | 3.7% 🟢 | 1.87 🟡 | 4.97 🟡 | 6.91zł | 8.33 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-korona` | 4.77 🟡 | 0.0% 🟢 | 1.1% 🟢 | 1.86 🟡 | 4.87 🟡 | 6.63zł | 8.19 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-oficjum` | 4.9 🟡 | 0.0% 🟢 | 3.2% 🟢 | 1.26 🟢 | 4.64 🟡 | 6.49zł | 7.89 | ⚠️ WARTOŚCI BRZEGOWE |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | ⚠️ Ostrzeżenie Witalności | 0.866 | Przedwczesne Zwycięstwa (Era 1-2): 1.9% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 10.0% gier (>6.0%) |
| `4p-no-cienie` | ⚠️ Ostrzeżenie Witalności | 0.285 | Zbyt Wczesne Zakończenia (Era 1-3): 7.7% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.92 Er (<5.0 Er) |
| `4p-no-kabala` | ⚠️ Ostrzeżenie Witalności | 0.995 | Przedwczesne Zwycięstwa (Era 1-2): 1.9% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 10.2% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.93 Er (<5.0 Er) |
| `4p-no-korona` | ⚠️ Ostrzeżenie Witalności | 1.306 | Przedwczesne Zwycięstwa (Era 1-2): 1.8% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 11.0% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.77 Er (<5.0 Er) |
| `4p-no-oficjum` | ⚠️ Ostrzeżenie Witalności | 1.158 | Przedwczesne Zwycięstwa (Era 1-2): 1.8% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 11.6% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.90 Er (<5.0 Er) |

## 3.1. Frakcje Wymagające Uwagi

| Frakcja | Śr. Win Share (wszystkie setupy) | Najgorszy Setup | Max Odchylenie od Ideału | Status |
| :--- | :---: | :--- | :---: | :--- |
| **SO** | 35.8% | `4p-no-korona` | +13.9% | 🟡 DOMINUJE |
| **KT** | 17.9% | `4p-no-oficjum` | -9.2% | 🟡 SŁABA |
| **KB** | 25.6% | `4p-no-oficjum` | +6.8% | 🟡 DOMINUJE |
| **GC** | 24.1% | `4p-no-oficjum` | +6.3% | 🟡 DOMINUJE |
| **CAA** | 21.6% | `4p-no-oficjum` | -3.9% | 🟢 OK |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `4p-no-korona` | 🔴 ** 12.3** | SO dominuje (38.9% vs ideal 25.0%) |
| `4p-no-oficjum` | 🔴 ** 16.7** | KT za słaba (15.8% vs ideal 25.0%) |
| `4p-core` | 🔴 ** 24.9** | SO dominuje (34.5% vs ideal 25.0%) |
| `4p-no-kabala` | 🔴 ** 26.8** | SO dominuje (31.7% vs ideal 25.0%) |
| `4p-no-cienie` | 🔴 ** 36.1** | SO dominuje (38.0% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 383 |   1.5% | `█                   ` | 🔴 Za wczesna (sprint / brak intrygi) |
| **Era 3** | 2,145 |   8.6% | `████                ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 6,696 |  26.8% | `█████████████       ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 7,940 |  31.8% | `████████████████    ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 5,991 |  24.0% | `████████████        ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 1,370 |   5.5% | `███                 ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 361 |   1.4% | `█                   ` | 🟡 Przedłużona |
| **Era 9** | 99 |   0.4% | `                    ` | 🔴 Limit Er (Deadlock) |
| **Era 10** | 13 |   0.1% | `                    ` | 🔴 Limit Er (Deadlock) |
| **Era 11** | 2 |   0.0% | `                    ` | 🔴 Limit Er (Deadlock) |

### 4.2. Rozkład Szans Wygranych Frakcji w poszczególnych Erach (% Wygranych Frakcji w danej Erze)

*Wiersze sumują się do 100.0% — wskazują która frakcja dominuje w danej fazie czasowej partii.*

| Era Końca Gry | Gry w Erze | SO % | CAA % | KB % | KT % | GC % | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 383 |   1.0% |  90.3% |   0.8% |   7.8% |   0.0% | **CAA (90.3%)** |
| **Era 3** | 2,145 |  13.1% |  40.1% |  20.2% |  24.6% |   2.1% | **CAA (40.1%)** |
| **Era 4** | 6,696 |  31.6% |  19.1% |  22.5% |  16.5% |  10.3% | **SO (31.6%)** |
| **Era 5** | 7,940 |  36.3% |  10.2% |  24.6% |  11.4% |  17.5% | **SO (36.3%)** |
| **Era 6** | 5,991 |  21.3% |  14.7% |  17.5% |  13.1% |  33.5% | **GC (33.5%)** |
| **Era 7** | 1,370 |  28.0% |   7.7% |  11.1% |  14.5% |  38.8% | **GC (38.8%)** |
| **Era 8** | 361 |  36.8% |  10.0% |   6.6% |   6.9% |  39.6% | **GC (39.6%)** |
| **Era 9** | 99 |  74.7% |   7.1% |   2.0% |   5.1% |  11.1% | **SO (74.7%)** |
| **Era 10** | 13 |  38.5% |  15.4% |   7.7% |  15.4% |  23.1% | **SO (38.5%)** |
| **Era 11** | 2 |  50.0% |   0.0% |   0.0% |   0.0% |  50.0% | **SO (50.0%)** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Era 1-4 (Wczesne / Szybkie) % | Era 5-7 (Złote Okno) % | Era 8+ (Długie) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **5.11** |  34.0% |  61.5% |   4.5% | **SO (36.6%)** |
| `4p-no-cienie` | **4.92** |  34.4% |  64.6% |   1.0% | **GC (40.8%)** |
| `4p-no-kabala` | **4.93** |  35.8% |  62.9% |   1.3% | **GC (36.9%)** |
| `4p-no-korona` | **4.77** |  44.9% |  53.8% |   1.2% | **GC (32.2%)** |
| `4p-no-oficjum` | **4.90** |  35.3% |  63.2% |   1.5% | **GC (56.5%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **2.0 – 4.5** | 🟡 1.5–2.0 / 4.5–5.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 75 | 🟠 ≥ 60 | 🔴 < 60