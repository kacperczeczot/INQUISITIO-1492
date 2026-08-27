# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v0.99.16

**Wersja Balansu:** `v0.99.16` | **Data:** 2026-08-18 13:19 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 13.29s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 ** 31.5** | 🔴 31.5 | 33.3% | - | 22.9% | - | 22.9% | 54.2% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 28.1** | 🔴 28.1 | 33.3% | - | 14.4% | 32.3% | - | 53.3% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 **  7.3** | 🔴 40.5 | 33.3% | - | 17.3% | 46.6% | 36.1% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 45.8** | 🔴 45.8 | 33.3% | - | - | 23.8% | 27.8% | 48.4% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 **  5.8** | 🔴 45.8 | 33.3% | 43.1% | 18.3% | - | - | 38.6% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 **  1.5** | 🔴 38.2 | 33.3% | 45.1% | 15.6% | - | 39.3% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 **  0.2** | 🔴 7.6 | 33.3% | 72.9% | 15.8% | 11.3% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 ** 10.8** | 🔴 35.9 | 33.3% | 14.8% | - | - | 46.1% | 39.1% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 ** 11.8** | 🔴 39.2 | 33.3% | 41.5% | - | 15.7% | - | 42.8% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 **  2.1** | 🔴 18.8 | 33.3% | 46.5% | - | 5.3% | 48.2% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟠 ** 70.0** | 🟠 70.0 | 25.0% | 30.3% | 21.7% | 19.9% | 28.1% | - | 🟠 WYMAGA UWAGI |
| `4p-no-cienie` | 4 | 🟠 ** 67.0** | 🟠 67.0 | 25.0% | 22.3% | - | 29.6% | 29.5% | 18.6% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🟠 ** 67.5** | 🟠 67.5 | 25.0% | 27.9% | 17.0% | 26.6% | - | 28.5% | 🟠 WYMAGA UWAGI |
| `4p-no-korona` | 4 | 🟡 ** 79.7** | 🟡 79.7 | 25.0% | 25.2% | 25.3% | - | 29.0% | 20.5% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🟠 ** 67.0** | 🟠 67.0 | 25.0% | - | 20.5% | 32.8% | 22.0% | 24.7% | 🟠 WYMAGA UWAGI |
| `5p-full` | 5 | 🔴 ** 37.3** | 🔴 37.3 | 20.0% | 32.7% | 22.8% | 12.7% | 11.0% | 20.8% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.64 🟡 | 2.4% 🟢 | 0.2% 🟢 | 1.97 🟡 | 3.81 🟢 | 20.57zł | 7.74 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 6.63 🟡 | 2.3% 🟢 | 2.0% 🟢 | 1.87 🟡 | 3.53 🟢 | 17.49zł | 7.68 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.39 🔴 | 22.1% 🔴 | 1.8% 🟢 | 2.0 🟡 | 5.27 🔴 | 19.28zł | 7.72 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.25 🟢 | 0.5% 🟢 | 2.8% 🟢 | 1.89 🟡 | 3.35 🟢 | 14.04zł | 8.24 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 8.83 🔴 | 13.7% 🔴 | 0.1% 🟢 | 2.98 🔴 | 4.01 🟢 | 28.56zł | 6.11 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-kabala` | 8.26 🔴 | 25.5% 🔴 | 0.1% 🟢 | 2.96 🔴 | 3.19 🟢 | 26.16zł | 5.59 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 9.68 🔴 | 32.2% 🔴 | 1.3% 🟢 | 3.04 🔴 | 5.24 🔴 | 27.65zł | 6.57 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 7.49 🔴 | 0.8% 🟢 | 0.2% 🟢 | 2.55 🔴 | 4.82 🟡 | 21.91zł | 6.8 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 7.93 🔴 | 3.3% 🟢 | 1.9% 🟢 | 2.65 🔴 | 4.9 🟡 | 20.51zł | 7.63 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-kabala` | 8.24 🔴 | 15.0% 🔴 | 1.8% 🟢 | 2.81 🔴 | 5.76 🔴 | 21.19zł | 7.4 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.49 🟢 | 1.9% 🟢 | 1.7% 🟢 | 2.48 🔴 | 4.3 🟢 | 17.18zł | 6.64 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 6.0 🟢 | 0.0% 🟢 | 2.1% 🟢 | 2.35 🔴 | 3.74 🟢 | 14.07zł | 7.45 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.54 🟡 | 0.7% 🟢 | 1.6% 🟢 | 2.38 🔴 | 3.4 🟢 | 18.13zł | 6.44 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-korona` | 6.27 🟢 | 0.1% 🟢 | 0.2% 🟢 | 2.43 🔴 | 4.38 🟢 | 19.14zł | 6.51 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.5 🟢 | 0.4% 🟢 | 1.9% 🟢 | 1.52 🟢 | 3.21 🟢 | 13.57zł | 7.4 | 🟢 OPTYMALNA |
| `5p-full` | 5.51 🟢 | 0.0% 🟢 | 1.5% 🟢 | 2.1 🔴 | 3.64 🟢 | 14.62zł | 6.55 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.710 | Paraliż Gry / Deadlocks 22.1% (>5%) |
| `3p-korona-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-gildia` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.070 | Paraliż Gry / Deadlocks 13.7% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/413 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-alandalus-kabala` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 3.250 | Paraliż Gry / Deadlocks 25.5% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/238 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-alandalus-korona` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 3.920 | Paraliż Gry / Deadlocks 32.2% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/531 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka skazania (swiete-oficjum): 0/146 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka skazania (swiete-oficjum): 0/408 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-korona-kabala` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.200 | Paraliż Gry / Deadlocks 15.0% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/374 wygranych (<8%) — gra tylko stosy |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |