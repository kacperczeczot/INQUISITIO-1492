# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.50

**Wersja Balansu:** `v1.0-alpha.50` | **Data:** 2026-08-23 14:56 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 19.67s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🔴 ** 54.0** | 🔴 58.9 | 25.0% | 32.0% | 15.6% | 25.6% | 26.7% | - | 🔴 ODCHYLONY |
| `4p-no-cienie` | 4 | 🔴 ** 59.7** | 🟡 75.9 | 25.0% | 30.9% | - | 21.5% | 24.0% | 23.6% | 🔴 ODCHYLONY |
| `4p-no-kabala` | 4 | 🔴 ** 55.5** | 🟠 63.1 | 25.0% | 27.8% | 16.1% | 26.2% | - | 29.9% | 🔴 ODCHYLONY |
| `4p-no-korona` | 4 | 🔴 ** 37.6** | 🔴 56.7 | 25.0% | 34.1% | 17.1% | - | 26.7% | 22.1% | 🔴 ODCHYLONY |
| `4p-no-oficjum` | 4 | 🔴 ** 34.3** | 🔴 53.1 | 25.0% | - | 14.8% | 32.2% | 22.8% | 30.2% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.3 🟢 | 0.0% 🟢 | 4.4% 🟢 | 2.05 🔴 | 5.28 🔴 | 6.85zł | 8.11 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 4.94 🟡 | 0.0% 🟢 | 4.7% 🟢 | 1.81 🟡 | 5.22 🔴 | 2.96zł | 8.52 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-kabala` | 5.21 🟢 | 0.0% 🟢 | 4.0% 🟢 | 1.96 🟡 | 5.57 🔴 | 7.45zł | 8.58 | 🟢 OPTYMALNA |
| `4p-no-korona` | 4.92 🟡 | 0.0% 🟢 | 1.1% 🟢 | 1.92 🟡 | 5.19 🔴 | 7.33zł | 8.22 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-oficjum` | 4.97 🟡 | 0.0% 🟢 | 3.3% 🟢 | 1.27 🟢 | 4.76 🟡 | 7.15zł | 7.92 | ⚠️ WARTOŚCI BRZEGOWE |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- :--- |
| `4p-core` | ⚠️ Ostrzeżenie Witalności | 0.087 | Zbyt Wczesne Zakończenia (Era 1-3): 6.9% gier (>6.0%) |
| `4p-no-cienie` | ⚠️ Ostrzeżenie Witalności | 0.239 | Zbyt Wczesne Zakończenia (Era 1-3): 7.4% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.94 Er (<5.0 Er) |
| `4p-no-kabala` | ⚠️ Ostrzeżenie Witalności | 0.128 | Przedwczesne Zwycięstwa (Era 1-2): 0.5% gier (>0.5%) |
| `4p-no-korona` | ⚠️ Ostrzeżenie Witalności | 0.411 | Przedwczesne Zwycięstwa (Era 1-2): 0.6% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 7.4% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.92 Er (<5.0 Er) |
| `4p-no-oficjum` | ⚠️ Ostrzeżenie Witalności | 0.436 | Przedwczesne Zwycięstwa (Era 1-2): 0.6% gier (>0.5%), Zbyt Wczesne Zakończenia (Era 1-3): 8.5% gier (>6.0%), Zbyt Krótka Średnia Rozgrywka 4.97 Er (<5.0 Er) |

## 3.1. Frakcje Wymagające Uwagi

| Frakcja | Śr. Win Share (wszystkie setupy) | Najgorszy Setup | Max Odchylenie od Ideału | Status |
| :--- | :---: | :--- | :---: | :--- |
| **CAA** | 15.9% | `4p-no-oficjum` | -10.2% | 🟡 SŁABA |
| **SO** | 31.2% | `4p-no-korona` | +9.1% | 🟡 DOMINUJE |
| **KB** | 26.4% | `4p-no-oficjum` | +7.2% | 🟡 DOMINUJE |
| **GC** | 26.5% | `4p-no-oficjum` | +5.2% | 🟡 DOMINUJE |
| **KT** | 24.3% | `4p-no-oficjum` | -2.2% | 🟢 OK |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `4p-no-oficjum` | 🔴 ** 34.3** | CAA za słaba (14.8% vs ideal 25.0%) |
| `4p-no-korona` | 🔴 ** 37.6** | SO dominuje (34.1% vs ideal 25.0%) |
| `4p-core` | 🔴 ** 54.0** | CAA za słaba (15.6% vs ideal 25.0%) |
| `4p-no-kabala` | 🔴 ** 55.5** | CAA za słaba (16.1% vs ideal 25.0%) |
| `4p-no-cienie` | 🔴 ** 59.7** | SO dominuje (30.9% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 247 |   0.5% | `                    ` | 🔴 Za wczesna (sprint / brak intrygi) |
| **Era 3** | 3,361 |   6.7% | `████                ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 13,012 |  26.0% | `█████████████       ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 16,345 |  32.7% | `████████████████    ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 12,684 |  25.4% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 3,110 |   6.2% | `███                 ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 890 |   1.8% | `█                   ` | 🟡 Przedłużona |
| **Era 9** | 290 |   0.6% | `                    ` | 🔴 Limit Er (Deadlock) |
| **Era 10** | 52 |   0.1% | `                    ` | 🔴 Limit Er (Deadlock) |
| **Era 11** | 9 |   0.0% | `                    ` | 🔴 Limit Er (Deadlock) |

### 4.2. Rozkład Szans Wygranych Frakcji w poszczególnych Erach (% Wygranych Frakcji w danej Erze)

| Era Końca Gry | Gry w Erze | SO % | CAA % | KB % | KT % | GC % | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 247 |   0.4% |  77.3% |   3.6% |  18.6% |   0.0% | **CAA (77.3%)** |
| **Era 3** | 3,361 |  11.2% |  24.9% |  22.1% |  38.7% |   3.1% | **KT (38.7%)** |
| **Era 4** | 13,012 |  28.2% |  17.9% |  21.2% |  21.8% |  10.9% | **SO (28.2%)** |
| **Era 5** | 16,345 |  30.1% |   9.6% |  24.5% |  16.7% |  19.1% | **SO (30.1%)** |
| **Era 6** | 12,684 |  17.2% |  13.4% |  18.6% |  17.2% |  33.6% | **GC (33.6%)** |
| **Era 7** | 3,110 |  24.2% |   5.2% |  13.1% |  20.2% |  37.3% | **GC (37.3%)** |
| **Era 8** | 890 |  25.1% |   9.6% |   9.1% |  11.4% |  44.8% | **GC (44.8%)** |
| **Era 9** | 290 |  74.5% |   6.2% |   4.5% |   6.6% |   8.2% | **SO (74.5%)** |
| **Era 10** | 52 |  38.5% |   7.7% |  21.2% |  23.1% |   9.5% | **SO (38.5%)** |
| **Era 11** | 9 |  44.4% |   0.0% |  44.4% |  11.1% |   0.0% | **SO/KB (44.4%)** |