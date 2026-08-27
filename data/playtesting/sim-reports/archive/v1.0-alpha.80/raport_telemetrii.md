[Strona główna](../../../../../README.md) > [v1.0-alpha.80](README.md) > [raport_telemetrii](raport_telemetrii.md)

---

# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.80

**Wersja Balansu:** `v1.0-alpha.80` | **Data:** 2026-08-24 21:28 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 25.65s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟢 ** 93.2** | 🟢 93.2 | 25.0% | 25.2% | 24.5% | 26.8% | 23.5% | - | 🟢 ZBALANSOWANY |
| `4p-no-cienie` | 4 | 🟠 ** 73.6** | 🟠 73.6 | 25.0% | 30.8% | - | 20.4% | 25.6% | 23.1% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🟡 ** 87.0** | 🟡 87.0 | 25.0% | 26.6% | 27.1% | 24.3% | - | 22.0% | 🟡 AKCEPTOWALNY |
| `4p-no-korona` | 4 | 🟡 ** 84.9** | 🟡 84.9 | 25.0% | 27.0% | 27.6% | - | 22.3% | 23.1% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🟠 ** 76.9** | 🟠 76.9 | 25.0% | - | 21.4% | 23.0% | 25.2% | 30.4% | 🟠 WYMAGA UWAGI |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.95 🟢 | 0.0% 🟢 | 5.1% 🟢 | 1.73 🟢 | 8.06 🟢 | 7.95zł | 8.05 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.67 🟢 | 0.0% 🟢 | 5.8% 🟢 | 1.61 🟢 | 7.7 🟢 | 4.42zł | 8.42 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.88 🟢 | 0.0% 🟢 | 5.2% 🟢 | 1.67 🟢 | 8.18 🟢 | 10.53zł | 8.54 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.59 🟢 | 0.0% 🟢 | 1.0% 🟢 | 1.63 🟢 | 7.9 🟢 | 10.26zł | 8.26 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.74 🟢 | 0.0% 🟢 | 4.8% 🟢 | 1.05 🟢 | 7.14 🟢 | 9.3zł | 7.68 | 🟢 OPTYMALNA |

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
| **SO** | 27.4% | `4p-no-cienie` | +5.8% | 🟡 DOMINUJE |
| **GC** | 24.6% | `4p-no-oficjum` | +5.4% | 🟡 DOMINUJE |
| **KB** | 23.6% | `4p-no-cienie` | -4.6% | 🟢 OK |
| **CAA** | 25.1% | `4p-no-oficjum` | -3.6% | 🟢 OK |
| **KT** | 24.1% | `4p-no-korona` | -2.7% | 🟢 OK |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `4p-no-cienie` | 🟠 ** 73.6** | SO dominuje (30.8% vs ideal 25.0%) |
| `4p-no-oficjum` | 🟠 ** 76.9** | GC dominuje (30.4% vs ideal 25.0%) |
| `4p-no-korona` | 🟡 ** 84.9** | KT za słaba (22.3% vs ideal 25.0%) |
| `4p-no-kabala` | 🟡 ** 87.0** | GC za słaba (22.0% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 94 |   0.2% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 1,451 |   2.9% | `█                   ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 6,932 |  13.9% | `███████             ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 12,494 |  25.0% | `████████████        ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 15,937 |  31.9% | `████████████████    ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 8,235 |  16.5% | `████████            ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 3,684 |   7.4% | `████                ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 989 |   2.0% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 153 |   0.3% | `                    ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 26 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 5 |   0.0% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 94 | 6 | 88 | 0 | 0 | 0 | **CAA (88)** |
| **Era 3** | 1,451 | 197 | 669 | 53 | 530 | 2 | **CAA (669)** |
| **Era 4** | 6,932 | 1,818 | 1,810 | 559 | 2,395 | 350 | **KT (2,395)** |
| **Era 5** | 12,494 | 3,253 | 2,332 | 1,921 | 3,342 | 1,646 | **KT (3,342)** |
| **Era 6** | 15,937 | 2,394 | 3,645 | 4,257 | 2,467 | 3,174 | **KB (4,257)** |
| **Era 7** | 8,235 | 1,823 | 1,049 | 1,830 | 794 | 2,739 | **GC (2,739)** |
| **Era 8** | 3,684 | 928 | 330 | 532 | 112 | 1,782 | **GC (1,782)** |
| **Era 9** | 989 | 501 | 113 | 218 | 23 | 134 | **SO (501)** |
| **Era 10** | 153 | 33 | 21 | 69 | 3 | 27 | **KB (69)** |
| **Era 11** | 26 | 8 | 1 | 13 | 0 | 4 | **KB (13)** |
| **Era 12** | 5 | 2 | 1 | 2 | 0 | 0 | **SO (2)** |
| **SUMA** | **50,000** | **10,963** | **10,059** | **9,454** | **9,666** | **9,858** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **5.95** |  0.1% | 14.5% | 71.5% | 13.7% |  0.2% | **KB (33.6%)** |
| `4p-no-cienie` | **5.67** |  0.0% | 16.5% | 76.0% |  7.4% |  0.0% | **KB (30.7%)** |
| `4p-no-kabala` | **5.88** |  0.3% | 13.1% | 78.2% |  8.4% |  0.0% | **CAA (31.1%)** |
| `4p-no-korona` | **5.59** |  0.3% | 22.8% | 68.2% |  8.6% |  0.0% | **CAA (34.8%)** |
| `4p-no-oficjum` | **5.74** |  0.2% | 16.9% | 72.8% | 10.1% |  0.1% | **KB (36.6%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **3.5 – 8.5** | 🟡 2.0–3.5 / 8.5–10.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 80 | 🟠 ≥ 65 | 🔴 < 65