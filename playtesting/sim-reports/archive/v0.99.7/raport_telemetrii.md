# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v0.99.7

**Wersja Balansu:** `v0.99.7` | **Data:** 2026-08-18 02:38 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 11.77s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 ** 36.0** | 🔴 42.7 | 33.3% | - | 21.7% | - | 29.2% | 49.1% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 22.0** | 🔴 22.0 | 33.3% | - | 13.5% | 28.8% | - | 57.7% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 **  4.2** | 🔴 36.5 | 33.3% | - | 15.9% | 47.9% | 36.2% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 59.9** | 🔴 59.9 | 33.3% | - | - | 24.3% | 32.6% | 43.1% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 **  2.2** | 🔴 35.7 | 33.3% | 48.8% | 16.0% | - | - | 35.2% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 **  0.9** | 🔴 31.8 | 33.3% | 45.3% | 12.7% | - | 42.0% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 **  0.1** | 🔴 7.1 | 33.3% | 73.7% | 16.2% | 10.1% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 ** 13.6** | 🔴 45.6 | 33.3% | 18.9% | - | - | 45.0% | 36.1% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 **  5.8** | 🔴 34.0 | 33.3% | 47.2% | - | 14.2% | - | 38.6% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 **  0.4** | 🔴 17.4 | 33.3% | 48.0% | - | 4.3% | 47.7% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟠 ** 60.0** | 🟠 63.7 | 25.0% | 31.6% | 21.3% | 18.7% | 28.4% | - | 🟠 WYMAGA UWAGI |
| `4p-no-cienie` | 4 | 🟠 ** 64.2** | 🟠 64.2 | 25.0% | 23.5% | - | 32.3% | 26.2% | 18.0% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🔴 ** 56.9** | 🔴 56.9 | 25.0% | 29.0% | 14.5% | 26.2% | - | 30.3% | 🔴 ODCHYLONY |
| `4p-no-korona` | 4 | 🟡 ** 75.9** | 🟡 75.9 | 25.0% | 27.1% | 26.9% | - | 27.1% | 18.9% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🟠 ** 62.9** | 🟠 62.9 | 25.0% | - | 18.8% | 32.2% | 21.1% | 27.9% | 🟠 WYMAGA UWAGI |
| `5p-full` | 5 | 🔴 ** 38.7** | 🔴 38.7 | 20.0% | 32.9% | 21.5% | 14.6% | 10.6% | 20.4% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.89 🟡 | 6.7% 🟡 | 0.2% 🟢 | 2.01 🔴 | 6.49 🔴 | 21.24zł | 7.64 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 6.9 🟡 | 4.3% 🟢 | 1.7% 🟢 | 1.92 🟡 | 6.92 🔴 | 18.25zł | 7.69 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.34 🔴 | 26.6% 🔴 | 1.5% 🟢 | 1.99 🟡 | 7.75 🔴 | 19.56zł | 7.61 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.61 🟡 | 2.8% 🟢 | 2.3% 🟢 | 1.97 🟡 | 6.1 🔴 | 15.7zł | 7.72 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-gildia` | 8.57 🔴 | 21.0% 🔴 | 0.1% 🟢 | 2.72 🔴 | 7.88 🔴 | 28.22zł | 6.74 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-kabala` | 8.05 🔴 | 28.7% 🔴 | 0.1% 🟢 | 2.83 🔴 | 5.22 🔴 | 26.07zł | 5.89 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 9.42 🔴 | 42.0% 🔴 | 1.1% 🟢 | 2.81 🔴 | 8.57 🔴 | 27.79zł | 7.03 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 7.76 🔴 | 5.1% 🟡 | 0.2% 🟢 | 2.45 🔴 | 7.54 🔴 | 23.66zł | 6.79 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 8.15 🔴 | 10.7% 🔴 | 1.6% 🟢 | 2.39 🔴 | 8.82 🔴 | 22.43zł | 7.88 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-kabala` | 8.44 🔴 | 29.6% 🔴 | 1.5% 🟢 | 2.71 🔴 | 8.52 🔴 | 23.53zł | 7.35 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.53 🟡 | 5.6% 🟡 | 1.5% 🟢 | 2.34 🔴 | 5.25 🔴 | 18.02zł | 6.53 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-cienie` | 5.95 🟢 | 0.3% 🟢 | 1.9% 🟢 | 2.18 🔴 | 4.39 🟢 | 14.9zł | 7.03 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.53 🟡 | 1.6% 🟢 | 1.6% 🟢 | 2.22 🔴 | 4.58 🟡 | 18.5zł | 6.36 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-korona` | 6.3 🟢 | 1.2% 🟢 | 0.2% 🟢 | 2.32 🔴 | 5.25 🔴 | 19.7zł | 6.45 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.52 🟢 | 0.3% 🟢 | 1.7% 🟢 | 1.54 🟢 | 4.1 🟢 | 13.83zł | 7.18 | 🟢 OPTYMALNA |
| `5p-full` | 5.55 🟢 | 0.0% 🟢 | 1.5% 🟢 | 2.03 🔴 | 3.54 🟢 | 15.19zł | 6.54 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.170 | Paraliż Gry / Deadlocks 6.7% (>5%) |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.160 | Paraliż Gry / Deadlocks 26.6% (>5%) |
| `3p-korona-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-gildia` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.800 | Paraliż Gry / Deadlocks 21.0% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/420 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-alandalus-kabala` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 3.570 | Paraliż Gry / Deadlocks 28.7% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/213 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-alandalus-korona` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 4.900 | Paraliż Gry / Deadlocks 42.0% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/490 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 1.210 | Paraliż Gry / Deadlocks 5.1% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/182 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 1.770 | Paraliż Gry / Deadlocks 10.7% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/449 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-korona-kabala` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 3.660 | Paraliż Gry / Deadlocks 29.6% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/256 wygranych (<8%) — gra tylko stosy |
| `4p-core` | ⚠️ Ostrzeżenie Witalności | 0.060 | Paraliż Gry / Deadlocks 5.6% (>5%) |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |