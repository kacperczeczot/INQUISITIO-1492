# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.19

**Wersja Balansu:** `v1.0-alpha.19` | **Data:** 2026-08-21 00:30 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 7.79s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 ** 24.9** | 🔴 24.9 | 33.3% | - | 22.5% | - | 20.0% | 57.5% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 26.9** | 🔴 26.9 | 33.3% | - | 14.3% | 31.5% | - | 54.2% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 **  6.8** | 🔴 42.7 | 33.3% | - | 18.1% | 46.1% | 35.8% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 33.6** | 🔴 33.6 | 33.3% | - | - | 22.0% | 24.8% | 53.2% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 ** 30.8** | 🔴 40.4 | 33.3% | 48.8% | 19.1% | - | - | 32.1% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 **  7.6** | 🔴 33.6 | 33.3% | 48.8% | 14.7% | - | 36.5% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 **  1.5** | 🔴 6.9 | 33.3% | 74.0% | 15.3% | 10.7% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🟠 ** 67.0** | 🟠 67.0 | 33.3% | 26.6% | - | - | 31.6% | 41.8% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-korona-gildia` | 3 | 🔴 ** 32.9** | 🔴 32.9 | 33.3% | 48.2% | - | 14.0% | - | 37.8% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 **  9.3** | 🔴 14.2 | 33.3% | 59.5% | - | 4.7% | 35.8% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟡 ** 75.9** | 🟡 75.9 | 25.0% | 29.7% | 24.8% | 19.8% | 25.7% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟡 ** 86.2** | 🟡 86.2 | 25.0% | 24.5% | - | 25.8% | 27.8% | 21.9% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟠 ** 64.2** | 🟠 64.2 | 25.0% | 24.7% | 16.7% | 29.2% | - | 29.4% | 🟠 WYMAGA UWAGI |
| `4p-no-korona` | 4 | 🟢 ** 91.5** | 🟢 91.5 | 25.0% | 22.6% | 26.3% | - | 25.4% | 25.7% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟡 ** 89.5** | 🟡 89.5 | 25.0% | - | 22.7% | 26.2% | 24.1% | 27.0% | 🟡 AKCEPTOWALNY |
| `5p-full` | 5 | 🔴 ** 28.9** | 🔴 28.9 | 20.0% | 34.5% | 23.9% | 12.4% | 7.6% | 21.6% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.75 🟡 | 1.9% 🟢 | 0.1% 🟢 | 1.97 🟡 | 4.19 🟢 | 20.91zł | 7.79 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 6.79 🟡 | 2.0% 🟢 | 1.9% 🟢 | 1.92 🟡 | 3.58 🟢 | 18.13zł | 7.72 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.78 🔴 | 23.3% 🔴 | 1.8% 🟢 | 2.08 🔴 | 6.0 🔴 | 19.94zł | 7.69 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.3 🟢 | 0.6% 🟢 | 2.7% 🟢 | 1.9 🟡 | 4.04 🟢 | 14.25zł | 8.49 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 8.68 🔴 | 7.7% 🟡 | 0.0% 🟢 | 3.0 🔴 | 3.58 🟢 | 28.25zł | 6.23 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-kabala` | 8.33 🔴 | 19.9% 🔴 | 0.1% 🟢 | 2.99 🔴 | 3.44 🟢 | 25.78zł | 6.0 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 9.56 🔴 | 20.5% 🔴 | 1.3% 🟢 | 3.13 🔴 | 4.47 🟢 | 27.08zł | 6.6 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 7.37 🔴 | 0.9% 🟢 | 0.1% 🟢 | 2.52 🔴 | 5.31 🔴 | 21.63zł | 7.27 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 7.68 🔴 | 2.1% 🟢 | 1.8% 🟢 | 2.64 🔴 | 4.64 🟡 | 20.3zł | 7.73 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-kabala` | 7.75 🔴 | 9.2% 🟡 | 1.9% 🟢 | 2.76 🔴 | 5.68 🔴 | 19.45zł | 7.93 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.64 🟡 | 1.1% 🟢 | 1.7% 🟢 | 2.48 🔴 | 4.83 🟡 | 17.05zł | 6.84 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-cienie` | 5.95 🟢 | 0.0% 🟢 | 2.0% 🟢 | 2.28 🔴 | 4.42 🟢 | 13.85zł | 7.77 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.5 🟢 | 0.2% 🟢 | 1.6% 🟢 | 2.34 🔴 | 3.42 🟢 | 18.1zł | 6.43 | 🟢 OPTYMALNA |
| `4p-no-korona` | 6.41 🟢 | 0.0% 🟢 | 0.1% 🟢 | 2.45 🔴 | 5.08 🔴 | 19.32zł | 6.78 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.59 🟢 | 0.1% 🟢 | 1.9% 🟢 | 1.56 🟢 | 3.6 🟢 | 13.74zł | 7.31 | 🟢 OPTYMALNA |
| `5p-full` | 5.48 🟢 | 0.0% 🟢 | 1.5% 🟢 | 2.03 🔴 | 3.94 🟢 | 14.34zł | 6.64 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.830 | Paraliż Gry / Deadlocks 23.3% (>5%) |
| `3p-korona-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-gildia` | ⚠️ Ostrzeżenie Witalności | 0.270 | Paraliż Gry / Deadlocks 7.7% (>5%) |
| `3p-oficjum-alandalus-kabala` | ⚠️ Ostrzeżenie Witalności | 1.490 | Paraliż Gry / Deadlocks 19.9% (>5%) |
| `3p-oficjum-alandalus-korona` | ⚠️ Ostrzeżenie Witalności | 1.550 | Paraliż Gry / Deadlocks 20.5% (>5%) |
| `3p-oficjum-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 0.420 | Paraliż Gry / Deadlocks 9.2% (>5%) |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |