[Strona główna](../../../../../README.md) > [v1.0-alpha.59](README.md) > [raport_telemetrii_4p](raport_telemetrii_4p.md)

---

# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.59

**Wersja Balansu:** `v1.0-alpha.59` | **Data:** 2026-08-23 22:04 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 17.43s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟠 ** 63.6** | 🟠 63.6 | 25.0% | 24.1% | 17.0% | 31.2% | 27.6% | - | 🟠 WYMAGA UWAGI |
| `4p-no-cienie` | 4 | 🔴 ** 57.1** | 🔴 57.1 | 25.0% | 33.3% | - | 15.8% | 25.3% | 25.5% | 🔴 ODCHYLONY |
| `4p-no-kabala` | 4 | 🔴 ** 51.6** | 🔴 51.6 | 25.0% | 18.2% | 18.4% | 28.4% | - | 35.0% | 🔴 ODCHYLONY |
| `4p-no-korona` | 4 | 🔴 ** 50.9** | 🟠 70.4 | 25.0% | 29.2% | 18.5% | - | 23.8% | 28.4% | 🔴 ODCHYLONY |
| `4p-no-oficjum` | 4 | 🔴 ** 39.0** | 🔴 39.0 | 25.0% | - | 13.9% | 22.1% | 24.1% | 39.9% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 6.09 🟢 | 0.0% 🟢 | 6.5% 🟢 | 1.53 🟢 | 6.64 🔴 | 6.4zł | 7.94 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.45 🟢 | 0.0% 🟢 | 7.6% 🟢 | 1.34 🟢 | 6.3 🔴 | 2.87zł | 8.58 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.96 🟢 | 0.0% 🟢 | 6.6% 🟢 | 1.32 🟢 | 7.19 🔴 | 7.38zł | 8.61 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.49 🟢 | 0.0% 🟢 | 1.9% 🟢 | 1.46 🟢 | 6.25 🔴 | 7.42zł | 8.17 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.5 🟢 | 0.0% 🟢 | 4.9% 🟢 | 1.02 🟢 | 5.77 🔴 | 6.71zł | 7.87 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | ⚠️ Ostrzeżenie Witalności | 0.324 | Nadmiar Wczesnych Zakończeń (Era 3-4): 28.2% gier (>25.0%) |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |

## 3.1. Frakcje Wymagające Uwagi

| Frakcja | Śr. Win Share (wszystkie setupy) | Najgorszy Setup | Max Odchylenie od Ideału | Status |
| :--- | :---: | :--- | :---: | :--- |
| **GC** | 32.2% | `4p-no-oficjum` | +14.9% | 🟡 DOMINUJE |
| **CAA** | 16.9% | `4p-no-oficjum` | -11.1% | 🟡 SŁABA |
| **KB** | 24.4% | `4p-no-cienie` | -9.2% | 🟡 SŁABA |
| **SO** | 26.2% | `4p-no-cienie` | +8.3% | 🟡 DOMINUJE |
| **KT** | 25.2% | `4p-core` | +2.6% | 🟢 OK |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `4p-no-oficjum` | 🔴 ** 39.0** | GC dominuje (39.9% vs ideal 25.0%) |
| `4p-no-korona` | 🔴 ** 50.9** | CAA za słaba (18.5% vs ideal 25.0%) |
| `4p-no-kabala` | 🔴 ** 51.6** | GC dominuje (35.0% vs ideal 25.0%) |
| `4p-no-cienie` | 🔴 ** 57.1** | KB za słaba (15.8% vs ideal 25.0%) |
| `4p-core` | 🟠 ** 63.6** | CAA za słaba (17.0% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 76 |   0.2% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 1,352 |   2.7% | `█                   ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 8,568 |  17.1% | `█████████           ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 12,600 |  25.2% | `█████████████       ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 14,690 |  29.4% | `███████████████     ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 7,783 |  15.6% | `████████            ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 3,728 |   7.5% | `████                ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 976 |   2.0% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 176 |   0.4% | `                    ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 45 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 6 |   0.0% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 76 | 4 | 69 | 0 | 3 | 0 | **CAA (69)** |
| **Era 3** | 1,352 | 140 | 590 | 50 | 565 | 7 | **CAA (590)** |
| **Era 4** | 8,568 | 2,392 | 1,773 | 401 | 2,892 | 1,110 | **KT (2,892)** |
| **Era 5** | 12,600 | 3,616 | 963 | 1,992 | 3,362 | 2,667 | **SO (3,616)** |
| **Era 6** | 14,690 | 1,646 | 2,271 | 4,621 | 2,430 | 3,722 | **KB (4,621)** |
| **Era 7** | 7,783 | 1,089 | 747 | 1,953 | 719 | 3,275 | **GC (3,275)** |
| **Era 8** | 3,728 | 944 | 278 | 445 | 78 | 1,983 | **GC (1,983)** |
| **Era 9** | 976 | 578 | 78 | 203 | 35 | 82 | **SO (578)** |
| **Era 10** | 176 | 51 | 12 | 82 | 7 | 24 | **KB (82)** |
| **Era 11** | 45 | 22 | 5 | 14 | 0 | 4 | **SO (22)** |
| **Era 12** | 6 | 5 | 1 | 0 | 0 | 0 | **SO (5)** |
| **SUMA** | **50,000** | **10,487** | **6,787** | **9,761** | **10,091** | **12,874** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **6.09** |  0.1% | 15.3% | 65.4% | 18.7% |  0.5% | **KB (45.5%)** |
| `4p-no-cienie` | **5.45** |  0.0% | 21.5% | 73.4% |  5.1% |  0.0% | **KB (28.3%)** |
| `4p-no-kabala` | **5.96** |  0.2% | 12.2% | 77.8% |  9.8% |  0.0% | **KB (39.6%)** |
| `4p-no-korona` | **5.49** |  0.3% | 28.2% | 62.4% |  9.0% |  0.1% | **GC (32.9%)** |
| `4p-no-oficjum` | **5.50** |  0.1% | 21.9% | 71.8% |  6.2% |  0.0% | **KB (38.8%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **2.0 – 4.5** | 🟡 1.5–2.0 / 4.5–5.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 75 | 🟠 ≥ 60 | 🔴 < 60