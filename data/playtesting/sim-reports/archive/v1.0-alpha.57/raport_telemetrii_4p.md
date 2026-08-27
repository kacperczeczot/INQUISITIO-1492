[Strona główna](../../../../../README.md) > [v1.0-alpha.57](README.md) > [raport_telemetrii_4p](raport_telemetrii_4p.md)

---

# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.57

**Wersja Balansu:** `v1.0-alpha.57` | **Data:** 2026-08-23 21:39 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 19.11s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🔴 **  0.2** | 🔴 0.4 | 25.0% | 91.2% | 2.3% | 5.2% | 1.3% | - | 🔴 ODCHYLONY |
| `4p-no-cienie` | 4 | 🔴 **  4.7** | 🔴 4.7 | 25.0% | 57.2% | - | 1.0% | 2.7% | 39.1% | 🔴 ODCHYLONY |
| `4p-no-kabala` | 4 | 🔴 **  4.6** | 🔴 4.6 | 25.0% | 35.7% | 1.0% | 3.5% | - | 59.8% | 🔴 ODCHYLONY |
| `4p-no-korona` | 4 | 🔴 **  1.5** | 🔴 5.0 | 25.0% | 43.8% | 1.1% | - | 1.8% | 53.2% | 🔴 ODCHYLONY |
| `4p-no-oficjum` | 4 | 🔴 **  0.3** | 🔴 0.3 | 25.0% | - | 0.5% | 3.3% | 1.5% | 94.6% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 7.28 🔴 | 0.1% 🟢 | 6.6% 🟢 | 1.87 🟡 | 10.18 🔴 | 6.99zł | 9.38 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-cienie` | 5.6 🟢 | 0.0% 🟢 | 7.7% 🟢 | 1.34 🟢 | 6.9 🔴 | 2.62zł | 9.25 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.24 🟢 | 0.0% 🟢 | 6.2% 🟢 | 1.46 🟢 | 7.92 🔴 | 7.07zł | 9.01 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.95 🟢 | 0.0% 🟢 | 2.3% 🟢 | 1.51 🟢 | 7.28 🔴 | 6.89zł | 8.92 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 6.21 🟢 | 0.0% 🟢 | 4.7% 🟢 | 1.09 🟢 | 7.75 🔴 | 6.61zł | 8.99 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | ⚠️ Ostrzeżenie Witalności | 0.746 | Ekstremalny Deadlock (Era 11+): 3.7% gier (>0.5%) |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 291/4382 wygranych (<8%) — gra tylko skazania |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |

## 3.1. Frakcje Wymagające Uwagi

| Frakcja | Śr. Win Share (wszystkie setupy) | Najgorszy Setup | Max Odchylenie od Ideału | Status |
| :--- | :---: | :--- | :---: | :--- |
| **GC** | 61.7% | `4p-no-oficjum` | +69.6% | 🟡 DOMINUJE |
| **SO** | 57.0% | `4p-core` | +66.2% | 🟡 DOMINUJE |
| **CAA** | 1.2% | `4p-no-oficjum` | -24.5% | 🟡 SŁABA |
| **KB** | 3.2% | `4p-no-cienie` | -24.0% | 🟡 SŁABA |
| **KT** | 1.8% | `4p-core` | -23.7% | 🟡 SŁABA |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `4p-core` | 🔴 **  0.2** | SO dominuje (91.2% vs ideal 25.0%) |
| `4p-no-oficjum` | 🔴 **  0.3** | GC dominuje (94.6% vs ideal 25.0%) |
| `4p-no-korona` | 🔴 **  1.5** | GC dominuje (53.2% vs ideal 25.0%) |
| `4p-no-kabala` | 🔴 **  4.6** | GC dominuje (59.8% vs ideal 25.0%) |
| `4p-no-cienie` | 🔴 **  4.7** | SO dominuje (57.2% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 3** | 297 |   0.6% | `                    ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 4,709 |   9.4% | `█████               ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 10,557 |  21.1% | `███████████         ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 13,926 |  27.9% | `██████████████      ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 11,664 |  23.3% | `████████████        ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 6,040 |  12.1% | `██████              ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 1,756 |   3.5% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 676 |   1.4% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 265 |   0.5% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 87 |   0.2% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 13** | 14 |   0.0% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 14** | 9 |   0.0% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 3** | 297 | 95 | 0 | 0 | 196 | 6 | **KT (196)** |
| **Era 4** | 4,709 | 3,090 | 0 | 0 | 310 | 1,309 | **SO (3,090)** |
| **Era 5** | 10,557 | 6,267 | 0 | 0 | 179 | 4,111 | **SO (6,267)** |
| **Era 6** | 13,926 | 4,989 | 215 | 796 | 38 | 7,888 | **GC (7,888)** |
| **Era 7** | 11,664 | 3,553 | 143 | 265 | 12 | 7,691 | **GC (7,691)** |
| **Era 8** | 6,040 | 2,498 | 46 | 99 | 0 | 3,397 | **GC (3,397)** |
| **Era 9** | 1,756 | 1,456 | 37 | 29 | 0 | 234 | **SO (1,456)** |
| **Era 10** | 676 | 515 | 30 | 88 | 0 | 43 | **SO (515)** |
| **Era 11** | 265 | 226 | 22 | 15 | 0 | 2 | **SO (226)** |
| **Era 12** | 87 | 82 | 5 | 0 | 0 | 0 | **SO (82)** |
| **Era 13** | 14 | 14 | 0 | 0 | 0 | 0 | **SO (14)** |
| **Era 14** | 9 | 5 | 0 | 1 | 3 | 0 | **SO (5)** |
| **SUMA** | **50,000** | **22,790** | **498** | **1,293** | **738** | **24,681** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **7.28** |  0.0% |  4.2% | 50.7% | 41.3% |  3.7% | **SO (85.1%)** |
| `4p-no-cienie` | **5.60** |  0.0% | 16.8% | 78.8% |  4.4% |  0.0% | **SO (49.5%)** |
| `4p-no-kabala` | **6.24** |  0.0% |  8.7% | 76.1% | 15.2% |  0.0% | **GC (60.9%)** |
| `4p-no-korona` | **5.95** |  0.0% | 13.4% | 75.7% | 10.9% |  0.0% | **GC (58.6%)** |
| `4p-no-oficjum` | **6.21** |  0.0% |  7.0% | 80.1% | 12.8% |  0.0% | **GC (89.8%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **2.0 – 4.5** | 🟡 1.5–2.0 / 4.5–5.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 75 | 🟠 ≥ 60 | 🔴 < 60