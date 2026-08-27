# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v0.99.14

**Wersja Balansu:** `v0.99.14` | **Data:** 2026-08-18 12:56 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 13.53s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 ** 32.1** | 🔴 32.1 | 33.3% | - | 23.7% | - | 22.4% | 53.9% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 27.6** | 🔴 27.6 | 33.3% | - | 14.1% | 32.4% | - | 53.5% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 **  7.3** | 🔴 40.5 | 33.3% | - | 17.3% | 46.6% | 36.1% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 45.3** | 🔴 45.3 | 33.3% | - | - | 23.4% | 28.1% | 48.5% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 **  5.7** | 🔴 47.9 | 33.3% | 40.5% | 18.8% | - | - | 40.7% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 **  1.3** | 🔴 35.5 | 33.3% | 45.6% | 14.5% | - | 39.9% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 **  0.1** | 🔴 7.2 | 33.3% | 73.5% | 15.9% | 10.6% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 **  9.7** | 🔴 32.2 | 33.3% | 13.1% | - | - | 46.5% | 40.4% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 ** 11.5** | 🔴 38.3 | 33.3% | 41.0% | - | 15.4% | - | 43.6% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 **  2.2** | 🔴 18.8 | 33.3% | 46.3% | - | 5.3% | 48.4% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟡 ** 78.4** | 🟡 78.4 | 25.0% | 28.8% | 22.1% | 21.6% | 27.5% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟠 ** 64.3** | 🟠 64.3 | 25.0% | 21.9% | - | 29.7% | 30.2% | 18.2% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🔴 ** 19.2** | 🟠 63.7 | 25.0% | 25.5% | 16.5% | 27.5% | - | 30.5% | 🔴 ODCHYLONY |
| `4p-no-korona` | 4 | 🟡 ** 84.4** | 🟡 84.4 | 25.0% | 23.6% | 26.5% | - | 28.0% | 21.9% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🟠 ** 69.8** | 🟠 69.8 | 25.0% | - | 21.0% | 32.3% | 22.7% | 24.0% | 🟠 WYMAGA UWAGI |
| `5p-full` | 5 | 🔴 ** 36.7** | 🔴 36.7 | 20.0% | 33.1% | 22.1% | 13.6% | 10.3% | 20.9% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.66 🟡 | 2.4% 🟢 | 0.2% 🟢 | 1.97 🟡 | 3.72 🟢 | 20.78zł | 7.68 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 6.63 🟡 | 2.5% 🟢 | 2.0% 🟢 | 1.87 🟡 | 3.55 🟢 | 17.49zł | 7.68 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.39 🔴 | 22.1% 🔴 | 1.8% 🟢 | 2.0 🟡 | 5.27 🔴 | 19.28zł | 7.72 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.28 🟢 | 0.6% 🟢 | 2.8% 🟢 | 1.9 🟡 | 3.25 🟢 | 14.28zł | 8.22 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 8.81 🔴 | 14.3% 🔴 | 0.1% 🟢 | 2.91 🔴 | 3.97 🟢 | 28.83zł | 6.05 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-kabala` | 8.36 🔴 | 26.2% 🔴 | 0.1% 🟢 | 2.98 🔴 | 3.14 🟢 | 26.86zł | 5.58 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 9.81 🔴 | 35.2% 🔴 | 1.3% 🟢 | 3.02 🔴 | 5.34 🔴 | 28.44zł | 6.55 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 7.49 🔴 | 1.0% 🟢 | 0.2% 🟢 | 2.5 🔴 | 4.64 🟡 | 22.47zł | 6.67 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 7.91 🔴 | 3.0% 🟢 | 1.9% 🟢 | 2.62 🔴 | 4.86 🟡 | 20.76zł | 7.59 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-kabala` | 8.29 🔴 | 14.6% 🔴 | 1.9% 🟢 | 2.79 🔴 | 5.81 🔴 | 21.8zł | 7.38 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.45 🟢 | 1.5% 🟢 | 1.7% 🟢 | 2.42 🔴 | 4.26 🟢 | 17.29zł | 6.61 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.97 🟢 | 0.0% 🟢 | 2.1% 🟢 | 2.3 🔴 | 3.6 🟢 | 14.38zł | 7.36 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.52 🟡 | 0.6% 🟢 | 1.7% 🟢 | 2.35 🔴 | 3.34 🟢 | 18.32zł | 6.44 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-korona` | 6.28 🟢 | 0.3% 🟢 | 0.2% 🟢 | 2.36 🔴 | 4.32 🟢 | 19.56zł | 6.43 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.48 🟢 | 0.4% 🟢 | 1.9% 🟢 | 1.51 🟢 | 3.12 🟢 | 13.63zł | 7.33 | 🟢 OPTYMALNA |
| `5p-full` | 5.55 🟢 | 0.0% 🟢 | 1.5% 🟢 | 2.06 🔴 | 3.57 🟢 | 15.01zł | 6.53 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.710 | Paraliż Gry / Deadlocks 22.1% (>5%) |
| `3p-korona-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-gildia` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.130 | Paraliż Gry / Deadlocks 14.3% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/387 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-alandalus-kabala` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 3.320 | Paraliż Gry / Deadlocks 26.2% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/242 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-alandalus-korona` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 4.220 | Paraliż Gry / Deadlocks 35.2% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/514 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka skazania (swiete-oficjum): 0/129 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka skazania (swiete-oficjum): 0/404 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-korona-kabala` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.160 | Paraliż Gry / Deadlocks 14.6% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/360 wygranych (<8%) — gra tylko stosy |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | ⚠️ Ostrzeżenie Witalności | 1.200 | Martwa ścieżka skazania (swiete-oficjum): 20/254 wygranych (<8%) — gra tylko stosy |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |