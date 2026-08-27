# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.21

**Wersja Balansu:** `v1.0-alpha.21` | **Data:** 2026-08-21 07:41 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 7.64s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 ** 27.3** | 🔴 27.3 | 33.3% | - | 23.0% | - | 20.8% | 56.2% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 26.9** | 🔴 26.9 | 33.3% | - | 14.3% | 31.5% | - | 54.2% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 **  6.8** | 🔴 42.7 | 33.3% | - | 18.1% | 46.1% | 35.8% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 32.5** | 🔴 32.5 | 33.3% | - | - | 21.8% | 24.5% | 53.7% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 ** 30.8** | 🔴 40.4 | 33.3% | 48.8% | 19.1% | - | - | 32.1% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 **  7.1** | 🔴 31.5 | 33.3% | 49.4% | 13.8% | - | 36.8% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 **  1.5** | 🔴 6.9 | 33.3% | 74.0% | 15.3% | 10.7% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🟠 ** 68.9** | 🟠 68.9 | 33.3% | 28.3% | - | - | 30.0% | 41.7% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-korona-gildia` | 3 | 🔴 ** 32.9** | 🔴 32.9 | 33.3% | 48.2% | - | 14.0% | - | 37.8% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 **  8.8** | 🔴 13.4 | 33.3% | 61.1% | - | 4.9% | 34.0% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟡 ** 76.3** | 🟡 76.3 | 25.0% | 29.9% | 24.3% | 20.2% | 25.6% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟡 ** 89.7** | 🟡 89.7 | 25.0% | 25.1% | - | 25.8% | 26.8% | 22.3% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟠 ** 64.2** | 🟠 64.2 | 25.0% | 24.7% | 16.7% | 29.2% | - | 29.4% | 🟠 WYMAGA UWAGI |
| `4p-no-korona` | 4 | 🟢 ** 95.5** | 🟢 95.5 | 25.0% | 23.8% | 26.0% | - | 24.7% | 25.5% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟢 ** 91.0** | 🟢 91.0 | 25.0% | - | 22.6% | 25.9% | 25.0% | 26.5% | 🟢 ZBALANSOWANY |
| `5p-full` | 5 | 🔴 ** 30.5** | 🔴 30.5 | 20.0% | 34.9% | 21.9% | 12.6% | 8.8% | 21.8% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.74 🟡 | 1.9% 🟢 | 0.1% 🟢 | 1.97 🟡 | 4.18 🟢 | 20.92zł | 7.79 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 6.79 🟡 | 2.0% 🟢 | 1.9% 🟢 | 1.92 🟡 | 3.58 🟢 | 18.13zł | 7.72 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.78 🔴 | 23.3% 🔴 | 1.8% 🟢 | 2.08 🔴 | 6.0 🔴 | 19.94zł | 7.69 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.3 🟢 | 0.6% 🟢 | 2.7% 🟢 | 1.9 🟡 | 4.04 🟢 | 14.27zł | 8.5 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 8.68 🔴 | 7.7% 🟡 | 0.0% 🟢 | 3.0 🔴 | 3.58 🟢 | 28.25zł | 6.23 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-kabala` | 8.34 🔴 | 19.9% 🔴 | 0.1% 🟢 | 2.96 🔴 | 3.48 🟢 | 25.37zł | 6.1 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 9.56 🔴 | 20.5% 🔴 | 1.3% 🟢 | 3.13 🔴 | 4.47 🟢 | 27.08zł | 6.6 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 7.33 🔴 | 0.9% 🟢 | 0.1% 🟢 | 2.48 🔴 | 5.3 🔴 | 21.21zł | 7.28 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 7.68 🔴 | 2.1% 🟢 | 1.8% 🟢 | 2.64 🔴 | 4.64 🟡 | 20.3zł | 7.73 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-kabala` | 7.72 🔴 | 9.2% 🟡 | 1.9% 🟢 | 2.69 🔴 | 5.64 🔴 | 19.01zł | 7.91 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.62 🟡 | 1.1% 🟢 | 1.7% 🟢 | 2.47 🔴 | 4.84 🟡 | 16.69zł | 6.89 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-cienie` | 5.93 🟢 | 0.0% 🟢 | 2.0% 🟢 | 2.23 🔴 | 4.45 🟢 | 13.62zł | 7.76 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.5 🟢 | 0.2% 🟢 | 1.6% 🟢 | 2.34 🔴 | 3.42 🟢 | 18.1zł | 6.43 | 🟢 OPTYMALNA |
| `4p-no-korona` | 6.41 🟢 | 0.0% 🟢 | 0.1% 🟢 | 2.44 🔴 | 5.09 🔴 | 19.07zł | 6.83 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.6 🟢 | 0.1% 🟢 | 1.9% 🟢 | 1.56 🟢 | 3.63 🟢 | 13.79zł | 7.33 | 🟢 OPTYMALNA |
| `5p-full` | 5.48 🟢 | 0.0% 🟢 | 1.5% 🟢 | 2.01 🔴 | 4.0 🟢 | 14.19zł | 6.66 | 🟢 OPTYMALNA |

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