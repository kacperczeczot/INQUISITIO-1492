# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v0.99.10

**Wersja Balansu:** `v0.99.10` | **Data:** 2026-08-18 03:07 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 10.89s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 ** 37.3** | 🔴 43.7 | 33.3% | - | 21.9% | - | 29.4% | 48.7% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 21.7** | 🔴 21.7 | 33.3% | - | 13.8% | 28.1% | - | 58.1% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 **  4.2** | 🔴 36.5 | 33.3% | - | 16.0% | 48.1% | 35.9% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 59.9** | 🔴 59.9 | 33.3% | - | - | 24.3% | 32.6% | 43.1% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 **  2.6** | 🔴 39.7 | 33.3% | 48.5% | 18.3% | - | - | 33.2% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 **  1.0** | 🔴 34.3 | 33.3% | 46.0% | 14.0% | - | 40.0% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 **  0.1** | 🔴 6.6 | 33.3% | 74.6% | 16.1% | 9.3% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 ** 13.6** | 🔴 45.2 | 33.3% | 18.7% | - | - | 45.0% | 36.3% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 **  6.6** | 🔴 34.9 | 33.3% | 45.9% | - | 14.3% | - | 39.8% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 **  0.5** | 🔴 18.5 | 33.3% | 47.3% | - | 5.1% | 47.6% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟠 ** 63.5** | 🟠 66.8 | 25.0% | 30.8% | 23.2% | 18.2% | 27.8% | - | 🟠 WYMAGA UWAGI |
| `4p-no-cienie` | 4 | 🟠 ** 63.3** | 🟠 63.3 | 25.0% | 23.7% | - | 31.1% | 28.1% | 17.1% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🟠 ** 61.3** | 🟠 61.3 | 25.0% | 28.9% | 15.8% | 25.4% | - | 29.9% | 🟠 WYMAGA UWAGI |
| `4p-no-korona` | 4 | 🟠 ** 69.8** | 🟠 69.8 | 25.0% | 27.7% | 25.8% | - | 28.8% | 17.7% | 🟠 WYMAGA UWAGI |
| `4p-no-oficjum` | 4 | 🟠 ** 65.4** | 🟠 65.4 | 25.0% | - | 19.5% | 31.7% | 21.0% | 27.8% | 🟠 WYMAGA UWAGI |
| `5p-full` | 5 | 🔴 ** 37.7** | 🔴 37.7 | 20.0% | 32.7% | 22.0% | 13.7% | 10.4% | 21.2% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.89 🟡 | 6.6% 🟡 | 0.2% 🟢 | 2.02 🔴 | 6.39 🔴 | 21.41zł | 7.6 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 6.89 🟡 | 4.3% 🟢 | 1.7% 🟢 | 1.91 🟡 | 6.91 🔴 | 18.47zł | 7.69 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.34 🔴 | 26.7% 🔴 | 1.5% 🟢 | 1.99 🟡 | 7.59 🔴 | 19.67zł | 7.53 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.61 🟡 | 2.8% 🟢 | 2.3% 🟢 | 1.97 🟡 | 6.1 🔴 | 15.7zł | 7.72 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-gildia` | 8.43 🔴 | 20.3% 🔴 | 0.1% 🟢 | 2.73 🔴 | 7.72 🔴 | 27.74zł | 6.71 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-kabala` | 8.01 🔴 | 28.0% 🔴 | 0.1% 🟢 | 2.89 🔴 | 5.11 🔴 | 25.8zł | 5.81 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 9.41 🔴 | 41.1% 🔴 | 1.1% 🟢 | 2.85 🔴 | 8.68 🔴 | 27.78zł | 7.07 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 7.75 🔴 | 4.9% 🟢 | 0.2% 🟢 | 2.48 🔴 | 7.56 🔴 | 23.35zł | 6.83 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 8.14 🔴 | 9.7% 🟡 | 1.6% 🟢 | 2.41 🔴 | 8.76 🔴 | 22.11zł | 7.9 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-kabala` | 8.41 🔴 | 28.9% 🔴 | 1.5% 🟢 | 2.69 🔴 | 8.53 🔴 | 23.14zł | 7.39 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.51 🟡 | 5.5% 🟡 | 1.5% 🟢 | 2.39 🔴 | 5.16 🔴 | 17.89zł | 6.48 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-cienie` | 5.96 🟢 | 0.4% 🟢 | 1.9% 🟢 | 2.23 🔴 | 4.37 🟢 | 14.72zł | 7.05 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.54 🟡 | 1.6% 🟢 | 1.6% 🟢 | 2.27 🔴 | 4.59 🟡 | 18.53zł | 6.38 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-korona` | 6.33 🟢 | 1.1% 🟢 | 0.2% 🟢 | 2.37 🔴 | 5.2 🔴 | 19.73zł | 6.39 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.52 🟢 | 0.3% 🟢 | 1.7% 🟢 | 1.53 🟢 | 4.08 🟢 | 13.98zł | 7.12 | 🟢 OPTYMALNA |
| `5p-full` | 5.55 🟢 | 0.0% 🟢 | 1.5% 🟢 | 2.06 🔴 | 3.53 🟢 | 15.13zł | 6.49 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.160 | Paraliż Gry / Deadlocks 6.6% (>5%) |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.170 | Paraliż Gry / Deadlocks 26.7% (>5%) |
| `3p-korona-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-gildia` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.730 | Paraliż Gry / Deadlocks 20.3% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/425 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-alandalus-kabala` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 3.500 | Paraliż Gry / Deadlocks 28.0% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/226 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-alandalus-korona` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 4.810 | Paraliż Gry / Deadlocks 41.1% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/502 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka skazania (swiete-oficjum): 0/181 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 1.670 | Paraliż Gry / Deadlocks 9.7% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/439 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-korona-kabala` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 3.590 | Paraliż Gry / Deadlocks 28.9% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/264 wygranych (<8%) — gra tylko stosy |
| `4p-core` | ⚠️ Ostrzeżenie Witalności | 0.050 | Paraliż Gry / Deadlocks 5.5% (>5%) |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |