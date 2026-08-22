# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.23

**Wersja Balansu:** `v1.0-alpha.23` | **Data:** 2026-08-22 13:17 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 4.35s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 ** 28.6** | 🔴 28.6 | 33.3% | - | 26.0% | - | 18.8% | 55.2% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 28.1** | 🔴 28.1 | 33.3% | - | 14.7% | 31.7% | - | 53.6% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 **  7.3** | 🔴 44.8 | 33.3% | - | 19.2% | 46.1% | 34.7% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 32.5** | 🔴 32.5 | 33.3% | - | - | 21.8% | 24.5% | 53.7% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 ** 32.8** | 🔴 42.1 | 33.3% | 48.8% | 20.5% | - | - | 30.7% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 **  8.9** | 🔴 33.5 | 33.3% | 49.0% | 14.8% | - | 36.2% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 **  1.7** | 🔴 7.5 | 33.3% | 73.0% | 16.9% | 10.1% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🟠 ** 69.2** | 🟠 69.2 | 33.3% | 29.0% | - | - | 29.3% | 41.7% | 🟠 WYMAGA UWAGI |
| `3p-oficjum-korona-gildia` | 3 | 🔴 ** 32.8** | 🔴 32.8 | 33.3% | 48.0% | - | 13.9% | - | 38.1% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 **  8.3** | 🔴 13.1 | 33.3% | 61.3% | - | 4.6% | 34.1% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟠 ** 68.5** | 🟠 68.5 | 25.0% | 29.4% | 29.6% | 19.7% | 21.3% | - | 🟠 WYMAGA UWAGI |
| `4p-no-cienie` | 4 | 🟡 ** 89.1** | 🟡 89.1 | 25.0% | 24.8% | - | 25.5% | 27.3% | 22.4% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟠 ** 65.3** | 🟠 65.3 | 25.0% | 23.5% | 17.5% | 29.0% | - | 30.0% | 🟠 WYMAGA UWAGI |
| `4p-no-korona` | 4 | 🟠 ** 73.9** | 🟠 73.9 | 25.0% | 23.8% | 30.8% | - | 20.3% | 25.1% | 🟠 WYMAGA UWAGI |
| `4p-no-oficjum` | 4 | 🟢 ** 94.8** | 🟢 94.8 | 25.0% | - | 24.0% | 26.0% | 24.1% | 25.9% | 🟢 ZBALANSOWANY |
| `5p-full` | 5 | 🔴 ** 28.4** | 🔴 28.4 | 20.0% | 34.0% | 24.9% | 11.5% | 7.6% | 22.0% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.69 🟡 | 2.1% 🟢 | 0.1% 🟢 | 1.95 🟡 | 4.16 🟢 | 21.06zł | 7.72 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 6.76 🟡 | 2.0% 🟢 | 1.9% 🟢 | 1.9 🟡 | 3.58 🟢 | 18.29zł | 7.69 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.75 🔴 | 23.2% 🔴 | 1.8% 🟢 | 2.06 🔴 | 5.91 🔴 | 20.19zł | 7.66 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.3 🟢 | 0.6% 🟢 | 2.7% 🟢 | 1.9 🟡 | 4.04 🟢 | 14.27zł | 8.5 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 8.57 🔴 | 7.5% 🟡 | 0.0% 🟢 | 2.96 🔴 | 3.49 🟢 | 28.16zł | 5.98 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-kabala` | 8.24 🔴 | 18.3% 🔴 | 0.1% 🟢 | 2.96 🔴 | 3.36 🟢 | 25.27zł | 5.86 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 9.46 🔴 | 19.6% 🔴 | 1.3% 🟢 | 3.14 🔴 | 4.28 🟢 | 26.98zł | 6.38 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 7.32 🔴 | 0.9% 🟢 | 0.1% 🟢 | 2.53 🔴 | 5.29 🔴 | 21.06zł | 7.11 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 7.76 🔴 | 2.3% 🟢 | 1.7% 🟢 | 2.72 🔴 | 4.6 🟡 | 20.43zł | 7.55 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-kabala` | 7.73 🔴 | 9.6% 🟡 | 1.9% 🟢 | 2.78 🔴 | 5.55 🔴 | 18.88zł | 7.75 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.52 🟡 | 1.1% 🟢 | 1.7% 🟢 | 2.49 🔴 | 4.67 🟡 | 16.58zł | 6.7 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-cienie` | 5.94 🟢 | 0.0% 🟢 | 2.0% 🟢 | 2.3 🔴 | 4.44 🟢 | 13.51zł | 7.66 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.46 🟢 | 0.2% 🟢 | 1.6% 🟢 | 2.36 🔴 | 3.37 🟢 | 18.11zł | 6.29 | 🟢 OPTYMALNA |
| `4p-no-korona` | 6.33 🟢 | 0.1% 🟢 | 0.1% 🟢 | 2.43 🔴 | 4.95 🟡 | 19.0zł | 6.62 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.54 🟢 | 0.1% 🟢 | 1.9% 🟢 | 1.53 🟢 | 3.51 🟢 | 13.87zł | 7.25 | 🟢 OPTYMALNA |
| `5p-full` | 5.46 🟢 | 0.0% 🟢 | 1.6% 🟢 | 2.07 🔴 | 3.96 🟢 | 14.23zł | 6.57 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.820 | Paraliż Gry / Deadlocks 23.2% (>5%) |
| `3p-korona-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-gildia` | ⚠️ Ostrzeżenie Witalności | 0.250 | Paraliż Gry / Deadlocks 7.5% (>5%) |
| `3p-oficjum-alandalus-kabala` | ⚠️ Ostrzeżenie Witalności | 1.330 | Paraliż Gry / Deadlocks 18.3% (>5%) |
| `3p-oficjum-alandalus-korona` | ⚠️ Ostrzeżenie Witalności | 1.460 | Paraliż Gry / Deadlocks 19.6% (>5%) |
| `3p-oficjum-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 0.460 | Paraliż Gry / Deadlocks 9.6% (>5%) |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |