# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v0.99.21

**Wersja Balansu:** `v0.99.21` | **Data:** 2026-08-18 14:38 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 14.13s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 ** 28.3** | 🔴 28.3 | 33.3% | - | 23.1% | - | 21.2% | 55.7% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 28.5** | 🔴 28.5 | 33.3% | - | 15.1% | 31.3% | - | 53.6% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 **  6.3** | 🔴 39.8 | 33.3% | - | 17.2% | 47.1% | 35.7% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 34.6** | 🔴 34.6 | 33.3% | - | - | 22.8% | 24.4% | 52.8% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 **  5.6** | 🔴 49.9 | 33.3% | 44.0% | 20.3% | - | - | 35.7% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 **  1.6** | 🔴 36.3 | 33.3% | 46.9% | 15.3% | - | 37.8% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 **  0.1** | 🔴 7.4 | 33.3% | 73.3% | 15.3% | 11.4% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 ** 11.7** | 🔴 39.0 | 33.3% | 15.6% | - | - | 42.1% | 42.3% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 ** 11.3** | 🔴 37.6 | 33.3% | 41.4% | - | 15.1% | - | 43.5% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 **  2.4** | 🔴 18.0 | 33.3% | 49.5% | - | 4.8% | 45.7% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟠 ** 71.6** | 🟠 71.6 | 25.0% | 30.4% | 23.7% | 19.2% | 26.7% | - | 🟠 WYMAGA UWAGI |
| `4p-no-cienie` | 4 | 🟡 ** 77.7** | 🟡 77.7 | 25.0% | 22.8% | - | 26.6% | 29.5% | 21.1% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟠 ** 68.0** | 🟠 68.0 | 25.0% | 27.1% | 17.1% | 27.2% | - | 28.6% | 🟠 WYMAGA UWAGI |
| `4p-no-korona` | 4 | 🟡 ** 87.7** | 🟡 87.7 | 25.0% | 22.0% | 25.9% | - | 27.3% | 24.8% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🟡 ** 77.1** | 🟡 77.1 | 25.0% | - | 21.1% | 29.6% | 22.6% | 26.7% | 🟡 AKCEPTOWALNY |
| `5p-full` | 5 | 🔴 ** 37.2** | 🔴 37.2 | 20.0% | 31.7% | 22.5% | 12.1% | 10.5% | 23.2% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.76 🟡 | 3.6% 🟢 | 0.3% 🟢 | 1.98 🟡 | 3.89 🟢 | 21.08zł | 7.6 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 6.81 🟡 | 2.5% 🟢 | 2.0% 🟢 | 1.92 🟡 | 3.47 🟢 | 18.12zł | 7.63 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.55 🔴 | 23.4% 🔴 | 1.7% 🟢 | 2.08 🔴 | 5.46 🔴 | 19.66zł | 7.69 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.31 🟢 | 1.1% 🟢 | 2.8% 🟢 | 1.9 🟡 | 3.73 🟢 | 14.08zł | 8.37 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 8.84 🔴 | 14.8% 🔴 | 0.1% 🟢 | 3.02 🔴 | 3.65 🟢 | 28.68zł | 6.06 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-kabala` | 8.29 🔴 | 24.5% 🔴 | 0.1% 🟢 | 3.0 🔴 | 3.27 🟢 | 26.31zł | 5.54 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 9.71 🔴 | 32.8% 🔴 | 1.3% 🟢 | 3.11 🔴 | 4.91 🟡 | 27.8zł | 6.54 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 7.64 🔴 | 0.9% 🟢 | 0.2% 🟢 | 2.55 🔴 | 5.24 🔴 | 22.45zł | 6.76 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 7.88 🔴 | 3.4% 🟢 | 1.9% 🟢 | 2.66 🔴 | 4.89 🟡 | 20.34zł | 7.63 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-kabala` | 8.27 🔴 | 13.3% 🔴 | 1.7% 🟢 | 2.79 🔴 | 6.1 🔴 | 21.07zł | 7.5 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.64 🟡 | 2.1% 🟢 | 1.6% 🟢 | 2.53 🔴 | 4.65 🟡 | 17.57zł | 6.57 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-cienie` | 6.02 🟢 | 0.0% 🟢 | 2.1% 🟢 | 2.36 🔴 | 4.03 🟢 | 14.07zł | 7.48 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.64 🟡 | 0.8% 🟢 | 1.6% 🟢 | 2.43 🔴 | 3.35 🟢 | 18.45zł | 6.4 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-korona` | 6.42 🟢 | 0.3% 🟢 | 0.2% 🟢 | 2.47 🔴 | 4.69 🟡 | 19.67zł | 6.38 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.57 🟢 | 0.3% 🟢 | 2.0% 🟢 | 1.54 🟢 | 3.33 🟢 | 13.77zł | 7.24 | 🟢 OPTYMALNA |
| `5p-full` | 5.58 🟢 | 0.0% 🟢 | 1.5% 🟢 | 2.12 🔴 | 3.84 🟢 | 14.8zł | 6.48 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.840 | Paraliż Gry / Deadlocks 23.4% (>5%) |
| `3p-korona-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-gildia` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.180 | Paraliż Gry / Deadlocks 14.8% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/416 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-alandalus-kabala` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 3.150 | Paraliż Gry / Deadlocks 24.5% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/260 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-alandalus-korona` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 3.980 | Paraliż Gry / Deadlocks 32.8% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/530 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka skazania (swiete-oficjum): 0/155 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka skazania (swiete-oficjum): 0/406 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-korona-kabala` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.030 | Paraliż Gry / Deadlocks 13.3% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/416 wygranych (<8%) — gra tylko stosy |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |