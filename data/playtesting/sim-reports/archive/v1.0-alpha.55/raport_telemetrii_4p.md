[Strona główna](../../../../../README.md) > [v1.0-alpha.55](README.md) > [raport_telemetrii_4p](raport_telemetrii_4p.md)

---

# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.55

**Wersja Balansu:** `v1.0-alpha.55` | **Data:** 2026-08-23 17:48 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 16.65s

*Score* = ogólny wskaźnik zdrowia (win share skorygowany o kary witalności i minimalnej długości gry ≥ 5.0 Er).
*Balance* = czysta symetria szans wygranych frakcji (win share vs ideal).

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🔴 ** 54.7** | 🟠 69.9 | 25.0% | 27.0% | 19.6% | 30.9% | 22.5% | - | 🔴 ODCHYLONY |
| `4p-no-cienie` | 4 | 🔴 ** 59.9** | 🔴 59.9 | 25.0% | 33.3% | - | 22.6% | 26.6% | 17.5% | 🔴 ODCHYLONY |
| `4p-no-kabala` | 4 | 🔴 ** 54.3** | 🟠 70.2 | 25.0% | 26.8% | 20.6% | 31.2% | - | 21.4% | 🔴 ODCHYLONY |
| `4p-no-korona` | 4 | 🔴 ** 39.1** | 🟠 68.1 | 25.0% | 32.2% | 21.8% | - | 25.6% | 20.4% | 🔴 ODCHYLONY |
| `4p-no-oficjum` | 4 | 🔴 ** 53.8** | 🟠 70.9 | 25.0% | - | 19.3% | 31.1% | 24.7% | 24.9% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.8 🟢 | 0.0% 🟢 | 5.9% 🟢 | 1.61 🟢 | 5.95 🔴 | 6.75zł | 8.07 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.39 🟢 | 0.0% 🟢 | 6.8% 🟢 | 1.47 🟢 | 5.9 🔴 | 2.82zł | 8.57 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.68 🟢 | 0.0% 🟢 | 5.6% 🟢 | 1.55 🟢 | 6.27 🔴 | 7.29zł | 8.48 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.47 🟢 | 0.0% 🟢 | 1.5% 🟢 | 1.55 🟢 | 6.11 🔴 | 7.18zł | 8.31 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.56 🟢 | 0.0% 🟢 | 4.8% 🟢 | 1.0 🟢 | 5.45 🔴 | 6.99zł | 7.92 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | ⚠️ Ostrzeżenie Witalności | 0.244 | Przedwczesne Zwycięstwa (Era 1-2): 0.5% gier (>0.5%), Ekstremalny Deadlock (Era 11+): 0.6% gier (>0.5%) |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | ⚠️ Ostrzeżenie Witalności | 0.258 | Przedwczesne Zwycięstwa (Era 1-2): 1.0% gier (>0.5%) |
| `4p-no-korona` | ⚠️ Ostrzeżenie Witalności | 0.554 | Przedwczesne Zwycięstwa (Era 1-2): 1.0% gier (>0.5%), Nadmiar Wczesnych Zakończeń (Era 3-4): 28.0% gier (>25.0%) |
| `4p-no-oficjum` | ⚠️ Ostrzeżenie Witalności | 0.275 | Przedwczesne Zwycięstwa (Era 1-2): 1.1% gier (>0.5%) |

## 3.1. Frakcje Wymagające Uwagi

| Frakcja | Śr. Win Share (wszystkie setupy) | Najgorszy Setup | Max Odchylenie od Ideału | Status |
| :--- | :---: | :--- | :---: | :--- |
| **SO** | 29.8% | `4p-no-cienie` | +8.3% | 🟡 DOMINUJE |
| **GC** | 21.1% | `4p-no-cienie` | -7.5% | 🟡 SŁABA |
| **KB** | 28.9% | `4p-no-kabala` | +6.2% | 🟡 DOMINUJE |
| **CAA** | 20.3% | `4p-no-oficjum` | -5.7% | 🟡 SŁABA |
| **KT** | 24.9% | `4p-core` | -2.5% | 🟢 OK |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `4p-no-korona` | 🔴 ** 39.1** | SO dominuje (32.2% vs ideal 25.0%) |
| `4p-no-oficjum` | 🔴 ** 53.8** | KB dominuje (31.1% vs ideal 25.0%) |
| `4p-no-kabala` | 🔴 ** 54.3** | KB dominuje (31.2% vs ideal 25.0%) |
| `4p-core` | 🔴 ** 54.7** | KB dominuje (30.9% vs ideal 25.0%) |
| `4p-no-cienie` | 🔴 ** 59.9** | SO dominuje (33.3% vs ideal 25.0%) |

## 4. Rozkład Długości Partii i Zwycięstw Frakcji według Er

### 4.1. Ogólny Rozkład Końca Partii według Er (Wszystkie Symulowane Gry)

| Era Końca Gry | Liczba Gier | Udział % | Wizualizacja Rozkładu | Ocena Tempa Gry |
| :---: | :---: | :---: | :--- | :--- |
| **Era 2** | 376 |   0.8% | `                    ` | 🔴 Ekstremalnie wczesna (sprint / anomalia) |
| **Era 3** | 2,797 |   5.6% | `███                 ` | 🟡 Wczesna / Szybka gra |
| **Era 4** | 8,784 |  17.6% | `█████████           ` | 🟡 Wczesna / Szybka gra |
| **Era 5** | 11,956 |  23.9% | `████████████        ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 6** | 13,936 |  27.9% | `██████████████      ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 7** | 7,397 |  14.8% | `███████             ` | 🟢 Złote Okno Rozgrywki (Ery 5–7) |
| **Era 8** | 3,553 |   7.1% | `████                ` | 🟡 Przedłużona / Późna gra |
| **Era 9** | 912 |   1.8% | `█                   ` | 🟡 Przedłużona / Późna gra |
| **Era 10** | 223 |   0.4% | `                    ` | 🟡 Przedłużona / Późna gra |
| **Era 11** | 60 |   0.1% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 12** | 4 |   0.0% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |
| **Era 13** | 2 |   0.0% | `                    ` | 🔴 Ekstremalnie przedłużona (deadlock / anomalia) |

### 4.2. Rozkład Zwycięstw Frakcji według Er (Liczba Wygranych Partii)

| Era Końca Gry | Gry w Erze | SO (wygrane) | CAA (wygrane) | KB (wygrane) | KT (wygrane) | GC (wygrane) | Dominująca Frakcja w tej Erze |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Era 2** | 376 | 0 | 357 | 0 | 19 | 0 | **CAA (357)** |
| **Era 3** | 2,797 | 161 | 1,101 | 895 | 637 | 3 | **CAA (1,101)** |
| **Era 4** | 8,784 | 2,464 | 2,228 | 1,531 | 2,332 | 229 | **SO (2,464)** |
| **Era 5** | 11,956 | 3,882 | 1,159 | 3,151 | 2,596 | 1,168 | **SO (3,882)** |
| **Era 6** | 13,936 | 2,068 | 2,205 | 4,627 | 2,593 | 2,443 | **KB (4,627)** |
| **Era 7** | 7,397 | 1,707 | 752 | 1,020 | 1,384 | 2,534 | **GC (2,534)** |
| **Era 8** | 3,553 | 985 | 243 | 238 | 265 | 1,822 | **GC (1,822)** |
| **Era 9** | 912 | 555 | 57 | 52 | 73 | 175 | **SO (555)** |
| **Era 10** | 223 | 70 | 19 | 61 | 30 | 43 | **SO (70)** |
| **Era 11** | 60 | 32 | 3 | 11 | 8 | 6 | **SO (32)** |
| **Era 12** | 4 | 3 | 0 | 1 | 0 | 0 | **SO (3)** |
| **Era 13** | 2 | 2 | 0 | 0 | 0 | 0 | **SO (2)** |
| **SUMA** | **50,000** | **11,929** | **8,124** | **11,587** | **9,937** | **8,423** | **Łącznie: 100.0%** |

### 4.3. Rozkład Er w Kanonie 4P (5 Głównych Setupów)

| Setup 4P | Śr. Er | Ery 1–2 (Sprint) % | Ery 3–4 (Wczesne) % | Ery 5–7 (Złote Okno) % | Ery 8–10 (Późne) % | Ery 11+ (Deadlock) % | Główny Zwycięzca w Erze 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | **5.80** |  0.5% | 20.9% | 65.4% | 12.6% |  0.6% | **KB (43.8%)** |
| `4p-no-cienie` | **5.39** |  0.1% | 24.8% | 69.1% |  6.1% |  0.0% | **KB (31.2%)** |
| `4p-no-kabala` | **5.68** |  1.0% | 21.0% | 67.5% | 10.4% |  0.1% | **KB (44.2%)** |
| `4p-no-korona` | **5.47** |  1.0% | 28.0% | 62.0% |  9.0% |  0.0% | **KT (28.9%)** |
| `4p-no-oficjum` | **5.56** |  1.1% | 21.1% | 68.9% |  8.8% |  0.0% | **KB (42.8%)** |

## 5. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **2.0 – 4.5** | 🟡 1.5–2.0 / 4.5–5.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 75 | 🟠 ≥ 60 | 🔴 < 60