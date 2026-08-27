# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v0.99.18

**Wersja Balansu:** `v0.99.18` | **Data:** 2026-08-18 13:41 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 13.54s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 ** 33.5** | 🔴 33.5 | 33.3% | - | 23.6% | - | 23.1% | 53.3% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 28.5** | 🔴 28.5 | 33.3% | - | 15.1% | 31.3% | - | 53.6% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 **  7.4** | 🔴 42.8 | 33.3% | - | 18.1% | 46.0% | 35.9% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 45.6** | 🔴 45.6 | 33.3% | - | - | 23.9% | 27.6% | 48.5% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 **  5.6** | 🔴 49.9 | 33.3% | 44.0% | 20.3% | - | - | 35.7% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 **  1.5** | 🔴 37.7 | 33.3% | 45.1% | 15.4% | - | 39.5% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 **  0.1** | 🔴 7.4 | 33.3% | 73.3% | 15.3% | 11.4% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 ** 10.8** | 🔴 36.0 | 33.3% | 14.8% | - | - | 45.9% | 39.3% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 ** 11.3** | 🔴 37.6 | 33.3% | 41.4% | - | 15.1% | - | 43.5% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 **  2.1** | 🔴 18.8 | 33.3% | 46.5% | - | 5.3% | 48.2% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟠 ** 71.7** | 🟠 71.7 | 25.0% | 29.3% | 22.8% | 19.4% | 28.5% | - | 🟠 WYMAGA UWAGI |
| `4p-no-cienie` | 4 | 🟠 ** 66.6** | 🟠 66.6 | 25.0% | 22.5% | - | 30.2% | 28.9% | 18.4% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🟠 ** 68.0** | 🟠 68.0 | 25.0% | 27.1% | 17.1% | 27.2% | - | 28.6% | 🟠 WYMAGA UWAGI |
| `4p-no-korona` | 4 | 🟡 ** 82.7** | 🟡 82.7 | 25.0% | 22.3% | 26.2% | - | 28.7% | 22.8% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🟠 ** 69.2** | 🟠 69.2 | 25.0% | - | 21.1% | 32.3% | 21.8% | 24.8% | 🟠 WYMAGA UWAGI |
| `5p-full` | 5 | 🔴 ** 40.7** | 🔴 40.7 | 20.0% | 31.4% | 23.0% | 12.7% | 11.7% | 21.2% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.73 🟡 | 3.5% 🟢 | 0.3% 🟢 | 1.98 🟡 | 3.69 🟢 | 20.88zł | 7.55 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 6.81 🟡 | 2.5% 🟢 | 2.0% 🟢 | 1.92 🟡 | 3.47 🟢 | 18.12zł | 7.63 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.43 🔴 | 22.5% 🔴 | 1.8% 🟢 | 2.02 🔴 | 5.15 🔴 | 19.49zł | 7.57 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.27 🟢 | 0.7% 🟢 | 2.9% 🟢 | 1.9 🟡 | 3.36 🟢 | 14.1zł | 8.26 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 8.84 🔴 | 14.8% 🔴 | 0.1% 🟢 | 3.02 🔴 | 3.65 🟢 | 28.68zł | 6.06 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-kabala` | 8.3 🔴 | 25.4% 🔴 | 0.1% 🟢 | 3.0 🔴 | 3.06 🟢 | 26.34zł | 5.46 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 9.71 🔴 | 32.8% 🔴 | 1.3% 🟢 | 3.11 🔴 | 4.91 🟡 | 27.8zł | 6.54 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 7.49 🔴 | 0.7% 🟢 | 0.2% 🟢 | 2.55 🔴 | 4.81 🟡 | 21.93zł | 6.8 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 7.88 🔴 | 3.4% 🟢 | 1.9% 🟢 | 2.66 🔴 | 4.89 🟡 | 20.34zł | 7.63 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-kabala` | 8.24 🔴 | 15.0% 🔴 | 1.8% 🟢 | 2.81 🔴 | 5.76 🔴 | 21.19zł | 7.4 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.57 🟡 | 2.5% 🟢 | 1.6% 🟢 | 2.52 🔴 | 4.33 🟢 | 17.51zł | 6.49 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-cienie` | 5.98 🟢 | 0.0% 🟢 | 2.1% 🟢 | 2.35 🔴 | 3.7 🟢 | 14.04zł | 7.46 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.64 🟡 | 0.8% 🟢 | 1.6% 🟢 | 2.43 🔴 | 3.35 🟢 | 18.45zł | 6.4 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-korona` | 6.36 🟢 | 0.2% 🟢 | 0.2% 🟢 | 2.46 🔴 | 4.43 🟢 | 19.45zł | 6.36 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.53 🟢 | 0.3% 🟢 | 1.9% 🟢 | 1.53 🟢 | 3.1 🟢 | 13.71zł | 7.24 | 🟢 OPTYMALNA |
| `5p-full` | 5.55 🟢 | 0.0% 🟢 | 1.5% 🟢 | 2.12 🔴 | 3.63 🟢 | 14.79zł | 6.43 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.750 | Paraliż Gry / Deadlocks 22.5% (>5%) |
| `3p-korona-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-gildia` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.180 | Paraliż Gry / Deadlocks 14.8% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/416 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-alandalus-kabala` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 3.240 | Paraliż Gry / Deadlocks 25.4% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/234 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-alandalus-korona` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 3.980 | Paraliż Gry / Deadlocks 32.8% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/530 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka skazania (swiete-oficjum): 0/146 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka skazania (swiete-oficjum): 0/406 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-korona-kabala` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.200 | Paraliż Gry / Deadlocks 15.0% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/374 wygranych (<8%) — gra tylko stosy |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |