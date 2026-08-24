# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.40

**Wersja Balansu:** `v1.0-alpha.40` | **Data:** 2026-08-23 04:43 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 4.44s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 ** 23.8** | 🔴 23.8 | 33.3% | - | 27.0% | - | 15.7% | 57.3% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 35.3** | 🔴 35.3 | 33.3% | - | 19.6% | 28.6% | - | 51.8% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 ** 25.9** | 🔴 25.9 | 33.3% | - | 18.6% | 24.7% | 56.7% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 21.6** | 🔴 21.6 | 33.3% | - | - | 24.3% | 16.6% | 59.1% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 ** 39.8** | 🔴 39.8 | 33.3% | 50.7% | 25.5% | - | - | 23.8% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 ** 11.2** | 🔴 37.1 | 33.3% | 35.7% | 16.3% | - | 48.0% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 ** 45.6** | 🔴 45.6 | 33.3% | 48.5% | 27.6% | 23.9% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 **  6.0** | 🔴 20.0 | 33.3% | 60.0% | - | - | 15.3% | 24.7% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 ** 16.0** | 🔴 53.0 | 33.3% | 46.1% | - | 25.2% | - | 28.7% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 ** 11.0** | 🔴 36.5 | 33.3% | 45.3% | - | 14.9% | 39.8% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🔴 ** 57.1** | 🔴 57.1 | 25.0% | 15.7% | 27.4% | 24.1% | 32.8% | - | 🔴 ODCHYLONY |
| `4p-no-cienie` | 4 | 🟡 ** 79.7** | 🟡 79.7 | 25.0% | 30.2% | - | 23.0% | 23.3% | 23.5% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟠 ** 73.6** | 🟠 73.6 | 25.0% | 22.1% | 25.6% | 21.3% | - | 31.0% | 🟠 WYMAGA UWAGI |
| `4p-no-korona` | 4 | 🟡 ** 87.8** | 🟡 87.8 | 25.0% | 27.3% | 26.5% | - | 23.2% | 23.0% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🟠 ** 70.9** | 🟠 70.9 | 25.0% | - | 20.4% | 31.5% | 22.4% | 25.7% | 🟠 WYMAGA UWAGI |
| `5p-full` | 5 | 🔴 ** 22.4** | 🔴 22.4 | 20.0% | 33.8% | 18.9% | 11.7% | 5.1% | 30.5% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 4.98 🟡 | 0.0% 🟢 | 0.2% 🟢 | 1.29 🟢 | 4.31 🟢 | 9.63zł | 8.36 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 5.13 🟢 | 0.0% 🟢 | 3.5% 🟢 | 1.34 🟢 | 4.45 🟢 | 9.42zł | 8.43 | 🟢 OPTYMALNA |
| `3p-cienie-korona-kabala` | 5.21 🟢 | 0.0% 🟢 | 4.1% 🟢 | 1.42 🟢 | 3.39 🟢 | 8.56zł | 7.69 | 🟢 OPTYMALNA |
| `3p-korona-kabala-gildia` | 5.08 🟢 | 0.0% 🟢 | 4.3% 🟢 | 1.32 🟢 | 4.53 🟡 | 3.25zł | 8.85 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 4.88 🟡 | 0.0% 🟢 | 1.7% 🟢 | 1.61 🟢 | 4.54 🟡 | 9.8zł | 8.71 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-kabala` | 5.07 🟢 | 0.0% 🟢 | 2.1% 🟢 | 1.8 🟢 | 3.64 🟢 | 8.59zł | 7.94 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-korona` | 5.52 🟢 | 0.0% 🟢 | 4.9% 🟢 | 1.75 🟢 | 4.49 🟢 | 8.79zł | 8.45 | 🟢 OPTYMALNA |
| `3p-oficjum-kabala-gildia` | 4.69 🟡 | 0.0% 🟢 | 2.1% 🟢 | 1.53 🟢 | 4.62 🟡 | 3.54zł | 8.76 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 5.13 🟢 | 0.0% 🟢 | 6.0% 🟢 | 1.5 🟢 | 5.03 🔴 | 3.65zł | 9.35 | 🟢 OPTYMALNA |
| `3p-oficjum-korona-kabala` | 4.95 🟡 | 0.0% 🟢 | 6.1% 🟢 | 1.69 🟢 | 3.86 🟢 | 2.37zł | 8.68 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 5.01 🟢 | 0.0% 🟢 | 4.4% 🟢 | 1.84 🟡 | 4.55 🟡 | 6.79zł | 7.88 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 4.88 🟡 | 0.0% 🟢 | 4.6% 🟢 | 1.63 🟢 | 5.08 🔴 | 3.13zł | 8.55 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-kabala` | 4.72 🟡 | 0.0% 🟢 | 3.9% 🟢 | 1.55 🟢 | 4.54 🟡 | 7.48zł | 8.06 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-korona` | 4.74 🟡 | 0.0% 🟢 | 1.6% 🟢 | 1.71 🟢 | 4.84 🟡 | 7.59zł | 8.01 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-oficjum` | 4.79 🟡 | 0.0% 🟢 | 2.9% 🟢 | 1.2 🟢 | 4.46 🟢 | 7.46zł | 7.76 | ⚠️ WARTOŚCI BRZEGOWE |
| `5p-full` | 4.36 🔴 | 0.0% 🟢 | 3.3% 🟢 | 1.56 🟢 | 4.47 🟢 | 6.09zł | 7.59 | ⚠️ WARTOŚCI BRZEGOWE |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-korona-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-kabala` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 9/357 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-alandalus-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 3/600 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 36/461 wygranych (<8%) — gra tylko skazania |
| `3p-oficjum-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka stosy (swiete-oficjum): 3/453 wygranych (<8%) — gra tylko skazania |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |