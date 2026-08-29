# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.98

**Wersja Balansu:** `v1.0-alpha.98` | **Data:** 2026-08-29 22:46 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 0.18s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟢 ** 92.2** | 🟢 92.2 | 25.0% | 25.3% | 23.5% | 27.0% | 24.2% | - | 🟢 ZBALANSOWANY |
| `4p-no-cienie` | 4 | 🟡 ** 88.3** | 🟡 88.3 | 25.0% | 25.1% | - | 22.3% | 27.6% | 25.0% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟢 ** 97.7** | 🟢 97.7 | 25.0% | 24.8% | 24.3% | 25.2% | - | 25.7% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟢 ** 97.5** | 🟢 97.5 | 25.0% | 25.4% | 24.2% | - | 25.0% | 25.4% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟢 ** 98.1** | 🟢 98.1 | 25.0% | - | 25.5% | 24.4% | 25.2% | 24.9% | 🟢 ZBALANSOWANY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.91 🟢 | 0.0% 🟢 | 5.1% 🟢 | 1.82 🟡 | 7.78 🟢 | 8.18zł | 7.99 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.6 🟢 | 0.0% 🟢 | 5.7% 🟢 | 1.63 🟢 | 7.76 🟢 | 5.45zł | 8.48 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.78 🟢 | 0.0% 🟢 | 4.9% 🟢 | 1.71 🟢 | 8.08 🟢 | 11.22zł | 8.52 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.54 🟢 | 0.0% 🟢 | 1.4% 🟢 | 1.67 🟢 | 7.91 🟢 | 10.98zł | 8.4 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.97 🟢 | 0.0% 🟢 | 5.2% 🟢 | 1.1 🟢 | 6.65 🟢 | 9.81zł | 7.54 | 🟢 OPTYMALNA |

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
| **KB** | 24.7% | `4p-no-cienie` | -2.7% | 🟢 OK |
| **KT** | 25.5% | `4p-no-cienie` | +2.6% | 🟢 OK |
| **CAA** | 24.4% | `4p-core` | -1.5% | 🟢 OK |
| **GC** | 25.2% | `4p-no-kabala` | +0.7% | 🟢 OK |
| **SO** | 25.1% | `4p-no-korona` | +0.4% | 🟢 OK |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `4p-no-cienie` | 🟡 ** 88.3** | KB za słaba (22.3% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 1** | 0 |   0.0% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 2** | 82 |   0.2% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 1,289 |   2.6% | `█                   ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 6,329 |  12.7% | `██████              ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 13,967 |  27.9% | `██████████████      ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 15,404 |  30.8% | `███████████████     ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 8,403 |  16.8% | `████████            ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 3,372 |   6.7% | `███                 ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 968 |   1.9% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 147 |   0.3% | `                    ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 29 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 8 |   0.0% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 1** | 0 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 2** | 82 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 3** | 1,289 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 4** | 6,329 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 5** | 13,967 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 6** | 15,404 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 7** | 8,403 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 8** | 3,372 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 9** | 968 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 10** | 147 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 11** | 29 | 0 | 0 | 0 | 0 | 0 | - |
| **Era 12** | 8 | 0 | 0 | 0 | 0 | 0 | - |
| **SUMA** | **49,998** | **0** | **0** | **0** | **0** | **0** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **5.91** |  0.1% | 16.2% | 70.3% | 13.2% |  0.2% | Brak gier w Erze 6 |
| `4p-no-cienie` | **5.60** |  0.0% | 15.8% | 79.3% |  4.8% |  0.0% | Brak gier w Erze 6 |
| `4p-no-kabala` | **5.78** |  0.3% | 12.7% | 80.4% |  6.7% |  0.0% | Brak gier w Erze 6 |
| `4p-no-korona` | **5.54** |  0.3% | 18.1% | 76.2% |  5.3% |  0.0% | Brak gier w Erze 6 |
| `4p-no-oficjum` | **5.97** |  0.1% | 13.3% | 71.5% | 14.9% |  0.1% | Brak gier w Erze 6 |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **3.5 – 8.5** | 🟡 2.0–3.5 / 8.5–10.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 80 | 🟠 ≥ 65 | 🔴 < 65