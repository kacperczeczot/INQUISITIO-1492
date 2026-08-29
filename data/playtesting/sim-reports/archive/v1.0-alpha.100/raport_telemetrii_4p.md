# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.100

**Wersja Balansu:** `v1.0-alpha.100` | **Data:** 2026-08-29 23:35 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 0.16s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟡 ** 87.6** | 🟡 87.6 | 25.0% | 24.4% | 24.4% | 28.2% | 22.9% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟡 ** 85.1** | 🟡 85.1 | 25.0% | 23.2% | - | 22.3% | 27.6% | 27.0% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟡 ** 89.2** | 🟡 89.2 | 25.0% | 22.1% | 25.2% | 26.4% | - | 26.3% | 🟡 AKCEPTOWALNY |
| `4p-no-korona` | 4 | 🟢 ** 98.1** | 🟢 98.1 | 25.0% | 25.1% | 24.9% | - | 24.4% | 25.6% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟢 ** 93.3** | 🟢 93.3 | 25.0% | - | 26.7% | 25.3% | 24.3% | 23.7% | 🟢 ZBALANSOWANY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 6.03 🟢 | 0.0% 🟢 | 5.1% 🟢 | 1.87 🟡 | 7.78 🟢 | 7.8zł | 7.94 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.7 🟢 | 0.0% 🟢 | 5.8% 🟢 | 1.69 🟢 | 7.83 🟢 | 5.43zł | 8.45 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.82 🟢 | 0.0% 🟢 | 5.1% 🟢 | 1.74 🟢 | 8.01 🟢 | 10.87zł | 8.44 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.57 🟢 | 0.0% 🟢 | 1.2% 🟢 | 1.7 🟢 | 7.82 🟢 | 10.55zł | 8.35 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 6.0 🟢 | 0.0% 🟢 | 5.2% 🟢 | 1.11 🟢 | 6.34 🟢 | 9.43zł | 7.39 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |

## 3.1. Frakcje Wymagające Uwagi

| Frakcja | Śr. Win Share (wszystkie setupy) | Najgorszy Setup | Max Odchylenie od Ideału | Status |
| :--- | :---: | :--- | :---: | :--- |
| **KB** | 25.6% | `4p-core` | +3.2% | 🟢 OK |
| **SO** | 23.7% | `4p-no-kabala` | -2.9% | 🟢 OK |
| **KT** | 24.8% | `4p-no-cienie` | +2.6% | 🟢 OK |
| **GC** | 25.7% | `4p-no-cienie` | +2.0% | 🟢 OK |
| **CAA** | 25.3% | `4p-no-oficjum` | +1.7% | 🟢 OK |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `4p-no-cienie` | 🟡 ** 85.1** | KB za słaba (22.3% vs ideal 25.0%) |
| `4p-core` | 🟡 ** 87.6** | KB dominuje (28.2% vs ideal 25.0%) |
| `4p-no-kabala` | 🟡 ** 89.2** | SO za słaba (22.1% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 1** | 0 |   0.0% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 2** | 98 |   0.2% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 1,253 |   2.5% | `█                   ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 6,047 |  12.1% | `██████              ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 13,500 |  27.0% | `██████████████      ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 15,132 |  30.3% | `███████████████     ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 8,800 |  17.6% | `█████████           ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 3,656 |   7.3% | `████                ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 1,223 |   2.4% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 215 |   0.4% | `                    ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 63 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 13 |   0.0% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 1** | 0 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 2** | 98 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 3** | 1,253 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 4** | 6,047 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 5** | 13,500 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 6** | 15,132 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 7** | 8,800 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 8** | 3,656 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 9** | 1,223 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 10** | 215 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 11** | 63 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 12** | 13 | 0 | 0 | 0 | 0 | 0 | - |
| **SUMA** | **50,000** | **0** | **0** | **0** | **0** | **0** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **6.03** |  0.1% | 15.4% | 68.1% | 15.9% |  0.4% | Brak gier w Erze 6 |
| `4p-no-cienie` | **5.70** |  0.0% | 13.8% | 80.3% |  5.8% |  0.0% | Brak gier w Erze 6 |
| `4p-no-kabala` | **5.82** |  0.3% | 12.8% | 78.6% |  8.2% |  0.0% | Brak gier w Erze 6 |
| `4p-no-korona` | **5.57** |  0.4% | 17.5% | 76.4% |  5.7% |  0.0% | Brak gier w Erze 6 |
| `4p-no-oficjum` | **6.00** |  0.1% | 13.4% | 70.9% | 15.4% |  0.3% | Brak gier w Erze 6 |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **3.5 – 8.5** | 🟡 2.0–3.5 / 8.5–10.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 80 | 🟠 ≥ 65 | 🔴 < 65