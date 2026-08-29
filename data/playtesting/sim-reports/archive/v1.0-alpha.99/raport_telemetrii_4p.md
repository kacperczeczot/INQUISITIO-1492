# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.99

**Wersja Balansu:** `v1.0-alpha.99` | **Data:** 2026-08-29 22:51 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 0.22s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟢 ** 92.1** | 🟢 92.1 | 25.0% | 25.9% | 23.3% | 26.7% | 24.1% | - | 🟢 ZBALANSOWANY |
| `4p-no-cienie` | 4 | 🟡 ** 86.8** | 🟡 86.8 | 25.0% | 25.2% | - | 21.8% | 27.6% | 25.3% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟢 ** 97.4** | 🟢 97.4 | 25.0% | 25.1% | 24.3% | 24.8% | - | 25.8% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟢 ** 96.5** | 🟢 96.5 | 25.0% | 26.1% | 24.3% | - | 24.7% | 24.9% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟢 ** 98.8** | 🟢 98.8 | 25.0% | - | 25.1% | 24.5% | 25.3% | 25.1% | 🟢 ZBALANSOWANY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.92 🟢 | 0.0% 🟢 | 5.1% 🟢 | 1.82 🟡 | 7.79 🟢 | 8.04zł | 8.02 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.6 🟢 | 0.0% 🟢 | 5.8% 🟢 | 1.64 🟢 | 7.78 🟢 | 5.44zł | 8.49 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.78 🟢 | 0.0% 🟢 | 5.0% 🟢 | 1.71 🟢 | 8.1 🟢 | 11.15zł | 8.54 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.53 🟢 | 0.0% 🟢 | 1.4% 🟢 | 1.67 🟢 | 7.88 🟢 | 10.82zł | 8.42 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.97 🟢 | 0.0% 🟢 | 5.2% 🟢 | 1.1 🟢 | 6.7 🟢 | 9.63zł | 7.57 | 🟢 OPTYMALNA |

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
| **KB** | 24.4% | `4p-no-cienie` | -3.2% | 🟢 OK |
| **KT** | 25.4% | `4p-no-cienie` | +2.6% | 🟢 OK |
| **CAA** | 24.2% | `4p-core` | -1.7% | 🟢 OK |
| **SO** | 25.6% | `4p-no-korona` | +1.1% | 🟢 OK |
| **GC** | 25.3% | `4p-no-kabala` | +0.8% | 🟢 OK |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `4p-no-cienie` | 🟡 ** 86.8** | KB za słaba (21.8% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 1** | 0 |   0.0% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 2** | 79 |   0.2% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 1,298 |   2.6% | `█                   ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 6,346 |  12.7% | `██████              ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 13,960 |  27.9% | `██████████████      ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 15,396 |  30.8% | `███████████████     ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 8,431 |  16.9% | `████████            ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 3,318 |   6.6% | `███                 ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 971 |   1.9% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 159 |   0.3% | `                    ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 32 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 9 |   0.0% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 1** | 0 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 2** | 79 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 3** | 1,298 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 4** | 6,346 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 5** | 13,960 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 6** | 15,396 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 7** | 8,431 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 8** | 3,318 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 9** | 971 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 10** | 159 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 11** | 32 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 12** | 9 | 0 | 0 | 0 | 0 | 0 | - |
| **SUMA** | **49,999** | **0** | **0** | **0** | **0** | **0** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **5.92** |  0.1% | 16.2% | 70.4% | 13.0% |  0.3% | Brak gier w Erze 6 |
| `4p-no-cienie` | **5.60** |  0.0% | 15.8% | 79.2% |  5.0% |  0.0% | Brak gier w Erze 6 |
| `4p-no-kabala` | **5.78** |  0.3% | 12.8% | 80.2% |  6.6% |  0.0% | Brak gier w Erze 6 |
| `4p-no-korona` | **5.53** |  0.3% | 18.3% | 76.3% |  5.1% |  0.0% | Brak gier w Erze 6 |
| `4p-no-oficjum` | **5.97** |  0.1% | 13.3% | 71.7% | 14.7% |  0.1% | Brak gier w Erze 6 |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **3.5 – 8.5** | 🟡 2.0–3.5 / 8.5–10.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 80 | 🟠 ≥ 65 | 🔴 < 65