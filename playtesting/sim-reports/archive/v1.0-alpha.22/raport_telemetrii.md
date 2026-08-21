# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.22

**Wersja Balansu:** `v1.0-alpha.22` | **Data:** 2026-08-21 07:53 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 7.66s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 ** 27.3** | 🔴 27.3 | 33.3% | - | 23.0% | - | 20.8% | 56.2% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 26.9** | 🔴 26.9 | 33.3% | - | 14.3% | 31.5% | - | 54.2% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 **  6.8** | 🔴 42.7 | 33.3% | - | 18.1% | 46.1% | 35.8% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 32.5** | 🔴 32.5 | 33.3% | - | - | 21.8% | 24.5% | 53.7% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 ** 30.2** | 🔴 39.2 | 33.3% | 49.5% | 19.1% | - | - | 31.4% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 **  7.1** | 🔴 31.6 | 33.3% | 49.5% | 13.9% | - | 36.6% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 **  1.5** | 🔴 6.9 | 33.3% | 74.1% | 15.9% | 10.0% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🟠 ** 69.2** | 🟠 69.2 | 33.3% | 29.0% | - | - | 29.3% | 41.7% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-korona-gildia` | 3 | 🔴 ** 32.8** | 🔴 32.8 | 33.3% | 48.0% | - | 13.9% | - | 38.1% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 **  8.3** | 🔴 13.1 | 33.3% | 61.3% | - | 4.6% | 34.1% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟡 ** 77.1** | 🟡 77.1 | 25.0% | 29.6% | 24.5% | 20.2% | 25.7% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟡 ** 89.1** | 🟡 89.1 | 25.0% | 24.8% | - | 25.5% | 27.3% | 22.4% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟠 ** 63.9** | 🟠 63.9 | 25.0% | 24.6% | 16.7% | 28.9% | - | 29.8% | 🟠 WYMAGA UWAGI |
| `4p-no-korona` | 4 | 🟢 ** 96.5** | 🟢 96.5 | 25.0% | 23.9% | 25.7% | - | 25.0% | 25.4% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟢 ** 91.0** | 🟢 91.0 | 25.0% | - | 22.6% | 25.9% | 25.0% | 26.5% | 🟢 ZBALANSOWANY |
| `5p-full` | 5 | 🔴 ** 29.2** | 🔴 29.2 | 20.0% | 35.0% | 22.0% | 12.2% | 8.3% | 22.5% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.74 🟡 | 1.9% 🟢 | 0.1% 🟢 | 1.97 🟡 | 4.18 🟢 | 20.92zł | 7.79 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 6.79 🟡 | 2.0% 🟢 | 1.9% 🟢 | 1.92 🟡 | 3.58 🟢 | 18.13zł | 7.72 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.78 🔴 | 23.3% 🔴 | 1.8% 🟢 | 2.08 🔴 | 6.0 🔴 | 19.94zł | 7.69 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.3 🟢 | 0.6% 🟢 | 2.7% 🟢 | 1.9 🟡 | 4.04 🟢 | 14.27zł | 8.5 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 8.68 🔴 | 7.6% 🟡 | 0.0% 🟢 | 3.01 🔴 | 3.57 🟢 | 28.25zł | 6.05 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-kabala` | 8.34 🔴 | 19.9% 🔴 | 0.1% 🟢 | 2.99 🔴 | 3.47 🟢 | 25.26zł | 5.9 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 9.56 🔴 | 20.2% 🔴 | 1.3% 🟢 | 3.17 🔴 | 4.41 🟢 | 27.02zł | 6.43 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 7.32 🔴 | 0.9% 🟢 | 0.1% 🟢 | 2.53 🔴 | 5.29 🔴 | 21.06zł | 7.11 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 7.76 🔴 | 2.3% 🟢 | 1.7% 🟢 | 2.72 🔴 | 4.6 🟡 | 20.43zł | 7.55 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-kabala` | 7.73 🔴 | 9.6% 🟡 | 1.9% 🟢 | 2.78 🔴 | 5.55 🔴 | 18.88zł | 7.75 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.62 🟡 | 1.1% 🟢 | 1.7% 🟢 | 2.54 🔴 | 4.81 🟡 | 16.57zł | 6.79 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-cienie` | 5.94 🟢 | 0.0% 🟢 | 2.0% 🟢 | 2.3 🔴 | 4.44 🟢 | 13.51zł | 7.66 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.5 🟢 | 0.2% 🟢 | 1.6% 🟢 | 2.39 🔴 | 3.44 🟢 | 18.03zł | 6.33 | 🟢 OPTYMALNA |
| `4p-no-korona` | 6.41 🟢 | 0.0% 🟢 | 0.1% 🟢 | 2.49 🔴 | 5.08 🔴 | 18.99zł | 6.7 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.6 🟢 | 0.1% 🟢 | 1.9% 🟢 | 1.56 🟢 | 3.63 🟢 | 13.79zł | 7.33 | 🟢 OPTYMALNA |
| `5p-full` | 5.48 🟢 | 0.0% 🟢 | 1.6% 🟢 | 2.09 🔴 | 4.01 🟢 | 14.07zł | 6.6 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.830 | Paraliż Gry / Deadlocks 23.3% (>5%) |
| `3p-korona-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-gildia` | ⚠️ Ostrzeżenie Witalności | 0.260 | Paraliż Gry / Deadlocks 7.6% (>5%) |
| `3p-oficjum-alandalus-kabala` | ⚠️ Ostrzeżenie Witalności | 1.490 | Paraliż Gry / Deadlocks 19.9% (>5%) |
| `3p-oficjum-alandalus-korona` | ⚠️ Ostrzeżenie Witalności | 1.520 | Paraliż Gry / Deadlocks 20.2% (>5%) |
| `3p-oficjum-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 0.460 | Paraliż Gry / Deadlocks 9.6% (>5%) |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |