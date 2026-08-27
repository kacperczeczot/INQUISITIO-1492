[Strona główna](../../../../../README.md) > [v1.0-alpha.58](README.md) > [raport_telemetrii_4p](raport_telemetrii_4p.md)

---

# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.58

**Wersja Balansu:** `v1.0-alpha.58` | **Data:** 2026-08-23 21:45 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 19.54s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🔴 **  0.2** | 🔴 0.4 | 25.0% | 92.0% | 2.4% | 5.5% | 0.1% | - | 🔴 ODCHYLONY |
| `4p-no-cienie` | 4 | 🔴 **  1.0** | 🔴 3.2 | 25.0% | 64.1% | - | 0.9% | 0.1% | 34.9% | 🔴 ODCHYLONY |
| `4p-no-kabala` | 4 | 🔴 **  4.6** | 🔴 4.6 | 25.0% | 35.7% | 1.0% | 3.5% | - | 59.8% | 🔴 ODCHYLONY |
| `4p-no-korona` | 4 | 🔴 **  1.3** | 🔴 4.5 | 25.0% | 46.7% | 1.2% | - | 0.1% | 52.0% | 🔴 ODCHYLONY |
| `4p-no-oficjum` | 4 | 🔴 **  0.3** | 🔴 0.3 | 25.0% | - | 0.5% | 3.4% | 0.0% | 96.0% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 7.29 🔴 | 0.0% 🟢 | 6.3% 🟢 | 1.93 🟡 | 10.28 🔴 | 7.23zł | 9.34 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-cienie` | 5.4 🟢 | 0.0% 🟢 | 7.0% 🟢 | 1.39 🟢 | 6.55 🔴 | 2.7zł | 9.26 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.24 🟢 | 0.0% 🟢 | 6.2% 🟢 | 1.46 🟢 | 7.92 🔴 | 7.07zł | 9.01 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.82 🟢 | 0.0% 🟢 | 1.9% 🟢 | 1.55 🟢 | 7.08 🔴 | 6.96zł | 8.86 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 6.09 🟢 | 0.0% 🟢 | 4.5% 🟢 | 1.07 🟢 | 7.64 🔴 | 6.82zł | 8.91 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | ⚠️ Ostrzeżenie Witalności | 0.800 | Ekstremalny Deadlock (Era 11+): 4.0% gier (>0.5%) |
| `4p-no-cienie` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 431/6408 wygranych (<8%) — gra tylko skazania |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 236/4669 wygranych (<8%) — gra tylko skazania |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |

## 3.1. Frakcje Wymagające Uwagi

| Frakcja | Śr. Win Share (wszystkie setupy) | Najgorszy Setup | Max Odchylenie od Ideału | Status |
| :--- | :---: | :--- | :---: | :--- |
| **GC** | 60.7% | `4p-no-oficjum` | +71.0% | 🟡 DOMINUJE |
| **SO** | 59.6% | `4p-core` | +67.0% | 🟡 DOMINUJE |
| **KT** | 0.1% | `4p-no-oficjum` | -25.0% | 🟡 SŁABA |
| **CAA** | 1.3% | `4p-no-oficjum` | -24.5% | 🟡 SŁABA |
| **KB** | 3.3% | `4p-no-cienie` | -24.1% | 🟡 SŁABA |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `4p-core` | 🔴 **  0.2** | SO dominuje (92.0% vs ideal 25.0%) |
| `4p-no-oficjum` | 🔴 **  0.3** | GC dominuje (96.0% vs ideal 25.0%) |
| `4p-no-cienie` | 🔴 **  1.0** | SO dominuje (64.1% vs ideal 25.0%) |
| `4p-no-korona` | 🔴 **  1.3** | GC dominuje (52.0% vs ideal 25.0%) |
| `4p-no-kabala` | 🔴 **  4.6** | GC dominuje (59.8% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 3** | 195 |   0.4% | `                    ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 5,632 |  11.3% | `██████              ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 11,692 |  23.4% | `████████████        ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 13,688 |  27.4% | `██████████████      ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 10,224 |  20.4% | `██████████          ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 5,652 |  11.3% | `██████              ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 1,827 |   3.7% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 686 |   1.4% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 293 |   0.6% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 93 |   0.2% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 13** | 14 |   0.0% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 14** | 4 |   0.0% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 3** | 195 | 168 | 0 | 0 | 22 | 5 | **SO (168)** |
| **Era 4** | 5,632 | 4,080 | 0 | 0 | 6 | 1,546 | **SO (4,080)** |
| **Era 5** | 11,692 | 7,304 | 0 | 0 | 1 | 4,387 | **SO (7,304)** |
| **Era 6** | 13,688 | 4,464 | 237 | 845 | 0 | 8,142 | **GC (8,142)** |
| **Era 7** | 10,224 | 2,894 | 149 | 270 | 0 | 6,911 | **GC (6,911)** |
| **Era 8** | 5,652 | 2,491 | 42 | 88 | 0 | 3,031 | **GC (3,031)** |
| **Era 9** | 1,827 | 1,546 | 22 | 35 | 0 | 224 | **SO (1,546)** |
| **Era 10** | 686 | 543 | 39 | 79 | 0 | 25 | **SO (543)** |
| **Era 11** | 293 | 250 | 22 | 17 | 0 | 4 | **SO (250)** |
| **Era 12** | 93 | 90 | 2 | 1 | 0 | 0 | **SO (90)** |
| **Era 13** | 14 | 13 | 1 | 0 | 0 | 0 | **SO (13)** |
| **Era 14** | 4 | 0 | 1 | 0 | 3 | 0 | **KT (3)** |
| **SUMA** | **50,000** | **23,843** | **515** | **1,335** | **32** | **24,275** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **7.29** |  0.0% |  5.2% | 48.3% | 42.6% |  4.0% | **SO (82.1%)** |
| `4p-no-cienie` | **5.40** |  0.0% | 20.5% | 75.6% |  3.8% |  0.0% | **SO (49.1%)** |
| `4p-no-kabala` | **6.24** |  0.0% |  8.7% | 76.1% | 15.2% |  0.0% | **GC (60.9%)** |
| `4p-no-korona` | **5.82** |  0.0% | 16.0% | 74.0% | 10.0% |  0.0% | **GC (63.1%)** |
| `4p-no-oficjum` | **6.09** |  0.0% |  7.9% | 82.1% | 10.1% |  0.0% | **GC (90.1%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **2.0 – 4.5** | 🟡 1.5–2.0 / 4.5–5.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 75 | 🟠 ≥ 60 | 🔴 < 60