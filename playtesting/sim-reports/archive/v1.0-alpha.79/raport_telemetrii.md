# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.79

**Wersja Balansu:** `v1.0-alpha.79` | **Data:** 2026-08-24 21:01 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 26.38s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟢 ** 90.9** | 🟢 90.9 | 25.0% | 25.5% | 24.3% | 27.1% | 23.1% | - | 🟢 ZBALANSOWANY |
| `4p-no-cienie` | 4 | 🟠 ** 74.6** | 🟠 74.6 | 25.0% | 29.9% | - | 21.1% | 27.2% | 21.8% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🟡 ** 87.2** | 🟡 87.2 | 25.0% | 26.2% | 27.1% | 24.9% | - | 21.8% | 🟡 AKCEPTOWALNY |
| `4p-no-korona` | 4 | 🟡 ** 83.2** | 🟡 83.2 | 25.0% | 27.3% | 27.7% | - | 23.1% | 21.9% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🟠 ** 73.6** | 🟠 73.6 | 25.0% | - | 20.5% | 23.2% | 25.4% | 30.9% | 🟠 WYMAGA UWAGI |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.98 🟢 | 0.0% 🟢 | 4.8% 🟢 | 1.72 🟢 | 8.09 🟢 | 8.29zł | 8.03 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.7 🟢 | 0.0% 🟢 | 5.6% 🟢 | 1.64 🟢 | 7.52 🟢 | 4.58zł | 8.31 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.91 🟢 | 0.0% 🟢 | 4.8% 🟢 | 1.63 🟢 | 8.21 🟢 | 10.82zł | 8.49 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.62 🟢 | 0.0% 🟢 | 0.8% 🟢 | 1.65 🟢 | 7.91 🟢 | 10.62zł | 8.19 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.74 🟢 | 0.0% 🟢 | 4.8% 🟢 | 1.05 🟢 | 7.16 🟢 | 9.48zł | 7.68 | 🟢 OPTYMALNA |

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
| **GC** | 24.1% | `4p-no-oficjum` | +5.9% | 🟡 DOMINUJE |
| **SO** | 27.2% | `4p-no-cienie` | +4.9% | 🟢 OK |
| **CAA** | 24.9% | `4p-no-oficjum` | -4.5% | 🟢 OK |
| **KB** | 24.1% | `4p-no-cienie` | -3.9% | 🟢 OK |
| **KT** | 24.7% | `4p-no-cienie` | +2.2% | 🟢 OK |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `4p-no-oficjum` | 🟠 ** 73.6** | GC dominuje (30.9% vs ideal 25.0%) |
| `4p-no-cienie` | 🟠 ** 74.6** | SO dominuje (29.9% vs ideal 25.0%) |
| `4p-no-korona` | 🟡 ** 83.2** | GC za słaba (21.9% vs ideal 25.0%) |
| `4p-no-kabala` | 🟡 ** 87.2** | GC za słaba (21.8% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 94 |   0.2% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 1,383 |   2.8% | `█                   ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 6,932 |  13.9% | `███████             ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 12,459 |  24.9% | `████████████        ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 15,815 |  31.6% | `████████████████    ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 7,953 |  15.9% | `████████            ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 3,979 |   8.0% | `████                ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 1,132 |   2.3% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 223 |   0.4% | `                    ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 26 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 4 |   0.0% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 94 | 8 | 86 | 0 | 0 | 0 | **CAA (86)** |
| **Era 3** | 1,383 | 190 | 645 | 53 | 495 | 0 | **CAA (645)** |
| **Era 4** | 6,932 | 1,882 | 1,728 | 544 | 2,448 | 330 | **KT (2,448)** |
| **Era 5** | 12,459 | 3,172 | 2,307 | 1,929 | 3,454 | 1,597 | **KT (3,454)** |
| **Era 6** | 15,815 | 2,323 | 3,658 | 4,371 | 2,480 | 2,983 | **KB (4,371)** |
| **Era 7** | 7,953 | 1,548 | 1,050 | 1,923 | 815 | 2,617 | **GC (2,617)** |
| **Era 8** | 3,979 | 1,126 | 307 | 527 | 137 | 1,882 | **GC (1,882)** |
| **Era 9** | 1,132 | 591 | 132 | 211 | 30 | 168 | **SO (591)** |
| **Era 10** | 223 | 53 | 35 | 78 | 5 | 52 | **KB (78)** |
| **Era 11** | 26 | 7 | 3 | 8 | 1 | 7 | **KB (8)** |
| **Era 12** | 4 | 2 | 0 | 0 | 0 | 2 | **SO (2)** |
| **SUMA** | **50,000** | **10,902** | **9,951** | **9,644** | **9,865** | **9,638** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **5.98** |  0.1% | 14.3% | 70.2% | 15.2% |  0.2% | **KB (34.3%)** |
| `4p-no-cienie` | **5.70** |  0.0% | 16.8% | 74.6% |  8.6% |  0.0% | **KB (32.5%)** |
| `4p-no-kabala` | **5.91** |  0.3% | 12.8% | 77.0% |  9.8% |  0.0% | **KB (31.5%)** |
| `4p-no-korona` | **5.62** |  0.3% | 22.6% | 67.1% |  9.8% |  0.1% | **CAA (35.6%)** |
| `4p-no-oficjum` | **5.74** |  0.2% | 16.5% | 73.4% |  9.9% |  0.0% | **KB (36.8%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **3.5 – 8.5** | 🟡 2.0–3.5 / 8.5–10.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 80 | 🟠 ≥ 65 | 🔴 < 65