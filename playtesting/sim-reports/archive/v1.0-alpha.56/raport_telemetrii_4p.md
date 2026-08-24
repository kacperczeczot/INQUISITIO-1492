# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.56

**Wersja Balansu:** `v1.0-alpha.56` | **Data:** 2026-08-23 21:23 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 16.48s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🔴 ** 36.5** | 🔴 40.8 | 25.0% | 28.8% | 15.9% | 38.0% | 17.3% | - | 🔴 ODCHYLONY |
| `4p-no-cienie` | 4 | 🔴 ** 47.5** | 🟠 71.6 | 25.0% | 31.8% | - | 24.5% | 21.2% | 22.5% | 🔴 ODCHYLONY |
| `4p-no-kabala` | 4 | 🔴 ** 49.0** | 🔴 49.0 | 25.0% | 20.3% | 16.1% | 36.0% | - | 27.6% | 🔴 ODCHYLONY |
| `4p-no-korona` | 4 | 🟠 ** 64.1** | 🟠 64.1 | 25.0% | 27.6% | 18.4% | - | 22.1% | 31.9% | 🟠 WYMAGA UWAGI |
| `4p-no-oficjum` | 4 | 🔴 ** 24.9** | 🔴 33.0 | 25.0% | - | 10.8% | 33.7% | 18.6% | 36.9% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.74 🟢 | 0.0% 🟢 | 6.4% 🟢 | 1.43 🟢 | 6.02 🔴 | 6.13zł | 8.18 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.14 🟢 | 0.0% 🟢 | 7.5% 🟢 | 1.23 🟢 | 5.5 🔴 | 2.61zł | 8.65 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.47 🟢 | 0.0% 🟢 | 6.0% 🟢 | 1.27 🟢 | 5.93 🔴 | 6.59zł | 8.51 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.45 🟢 | 0.0% 🟢 | 2.1% 🟢 | 1.4 🟢 | 5.97 🔴 | 6.47zł | 8.36 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.21 🟢 | 0.0% 🟢 | 4.8% 🟢 | 0.94 🟢 | 5.08 🔴 | 6.08zł | 8.16 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | ⚠️ Ostrzeżenie Witalności | 0.110 | Ekstremalny Deadlock (Era 11+): 0.5% gier (>0.5%) |
| `4p-no-cienie` | ⚠️ Ostrzeżenie Witalności | 0.410 | Nadmiar Wczesnych Zakończeń (Era 3-4): 29.1% gier (>25.0%) |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | ⚠️ Ostrzeżenie Witalności | 0.281 | Nadmiar Wczesnych Zakończeń (Era 3-4): 27.8% gier (>25.0%) |

## 3.1. Frakcje Wymagające Uwagi

| Frakcja | Śr. Win Share (wszystkie setupy) | Najgorszy Setup | Max Odchylenie od Ideału | Status |
| :--- | :---: | :--- | :---: | :--- |
| **CAA** | 15.3% | `4p-no-oficjum` | -14.2% | 🟡 SŁABA |
| **KB** | 33.1% | `4p-core` | +13.0% | 🟡 DOMINUJE |
| **GC** | 29.7% | `4p-no-oficjum` | +11.9% | 🟡 DOMINUJE |
| **KT** | 19.8% | `4p-core` | -7.7% | 🟡 SŁABA |
| **SO** | 27.1% | `4p-no-cienie` | +6.8% | 🟡 DOMINUJE |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `4p-no-oficjum` | 🔴 ** 24.9** | CAA za słaba (10.8% vs ideal 25.0%) |
| `4p-core` | 🔴 ** 36.5** | KB dominuje (38.0% vs ideal 25.0%) |
| `4p-no-cienie` | 🔴 ** 47.5** | SO dominuje (31.8% vs ideal 25.0%) |
| `4p-no-kabala` | 🔴 ** 49.0** | KB dominuje (36.0% vs ideal 25.0%) |
| `4p-no-korona` | 🟠 ** 64.1** | GC dominuje (31.9% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 108 |   0.2% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 3,225 |   6.5% | `███                 ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 9,408 |  18.8% | `█████████           ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 14,512 |  29.0% | `███████████████     ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 13,377 |  26.8% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 6,129 |  12.3% | `██████              ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 2,433 |   4.9% | `██                  ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 568 |   1.1% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 184 |   0.4% | `                    ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 49 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 6 |   0.0% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 13** | 1 |   0.0% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 108 | 0 | 108 | 0 | 0 | 0 | **CAA (108)** |
| **Era 3** | 3,225 | 77 | 580 | 1,845 | 717 | 6 | **KB (1,845)** |
| **Era 4** | 9,408 | 2,016 | 1,581 | 2,053 | 2,673 | 1,085 | **KT (2,673)** |
| **Era 5** | 14,512 | 4,003 | 925 | 4,051 | 3,003 | 2,530 | **KB (4,051)** |
| **Era 6** | 13,377 | 2,112 | 2,188 | 4,082 | 1,324 | 3,671 | **KB (4,082)** |
| **Era 7** | 6,129 | 1,316 | 499 | 930 | 190 | 3,194 | **GC (3,194)** |
| **Era 8** | 2,433 | 784 | 157 | 177 | 10 | 1,305 | **GC (1,305)** |
| **Era 9** | 568 | 417 | 51 | 23 | 1 | 76 | **SO (417)** |
| **Era 10** | 184 | 104 | 30 | 39 | 0 | 11 | **SO (104)** |
| **Era 11** | 49 | 25 | 9 | 14 | 0 | 1 | **SO (25)** |
| **Era 12** | 6 | 6 | 0 | 0 | 0 | 0 | **SO (6)** |
| **Era 13** | 1 | 0 | 0 | 1 | 0 | 0 | **KB (1)** |
| **SUMA** | **50,000** | **10,860** | **6,128** | **13,215** | **7,918** | **11,879** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **5.74** |  0.2% | 21.4% | 63.8% | 14.1% |  0.5% | **KB (45.3%)** |
| `4p-no-cienie` | **5.14** |  0.0% | 29.1% | 68.5% |  2.4% |  0.0% | **GC (30.6%)** |
| `4p-no-kabala` | **5.47** |  0.3% | 23.1% | 70.6% |  5.9% |  0.0% | **KB (40.0%)** |
| `4p-no-korona` | **5.45** |  0.4% | 24.8% | 68.9% |  5.9% |  0.0% | **GC (36.6%)** |
| `4p-no-oficjum` | **5.21** |  0.3% | 27.8% | 68.4% |  3.6% |  0.0% | **GC (39.7%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **2.0 – 4.5** | 🟡 1.5–2.0 / 4.5–5.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 75 | 🟠 ≥ 60 | 🔴 < 60