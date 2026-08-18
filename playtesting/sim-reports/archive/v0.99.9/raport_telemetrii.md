# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v0.99.9

**Wersja Balansu:** `v0.99.9` | **Data:** 2026-08-18 02:57 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 10.97s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 ** 37.3** | 🔴 43.7 | 33.3% | - | 21.9% | - | 29.4% | 48.7% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 21.7** | 🔴 21.7 | 33.3% | - | 13.8% | 28.1% | - | 58.1% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 **  4.2** | 🔴 36.5 | 33.3% | - | 16.0% | 48.1% | 35.9% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 59.9** | 🔴 59.9 | 33.3% | - | - | 24.3% | 32.6% | 43.1% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 **  2.3** | 🔴 37.5 | 33.3% | 48.5% | 16.9% | - | - | 34.6% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 **  0.9** | 🔴 32.6 | 33.3% | 45.3% | 13.1% | - | 41.6% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 **  0.1** | 🔴 7.2 | 33.3% | 73.5% | 16.4% | 10.1% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 ** 13.6** | 🔴 45.6 | 33.3% | 18.9% | - | - | 45.0% | 36.1% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 **  5.8** | 🔴 34.0 | 33.3% | 47.2% | - | 14.2% | - | 38.6% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 **  0.4** | 🔴 17.4 | 33.3% | 48.0% | - | 4.3% | 47.7% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟠 ** 63.1** | 🟠 67.0 | 25.0% | 30.9% | 22.6% | 18.6% | 27.9% | - | 🟠 WYMAGA UWAGI |
| `4p-no-cienie` | 4 | 🟠 ** 64.2** | 🟠 64.2 | 25.0% | 23.5% | - | 32.3% | 26.2% | 18.0% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🔴 ** 57.7** | 🔴 57.7 | 25.0% | 28.8% | 14.7% | 26.3% | - | 30.2% | 🔴 ODCHYLONY |
| `4p-no-korona` | 4 | 🟡 ** 76.3** | 🟡 76.3 | 25.0% | 26.0% | 27.3% | - | 27.6% | 19.1% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🟠 ** 65.4** | 🟠 65.4 | 25.0% | - | 19.5% | 31.7% | 21.0% | 27.8% | 🟠 WYMAGA UWAGI |
| `5p-full` | 5 | 🔴 ** 37.5** | 🔴 37.5 | 20.0% | 32.9% | 22.4% | 13.8% | 10.5% | 20.4% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.89 🟡 | 6.6% 🟡 | 0.2% 🟢 | 2.02 🔴 | 6.39 🔴 | 21.41zł | 7.6 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 6.89 🟡 | 4.3% 🟢 | 1.7% 🟢 | 1.91 🟡 | 6.91 🔴 | 18.47zł | 7.69 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.34 🔴 | 26.7% 🔴 | 1.5% 🟢 | 1.99 🟡 | 7.59 🔴 | 19.67zł | 7.53 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.61 🟡 | 2.8% 🟢 | 2.3% 🟢 | 1.97 🟡 | 6.1 🔴 | 15.7zł | 7.72 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-gildia` | 8.54 🔴 | 21.0% 🔴 | 0.1% 🟢 | 2.71 🔴 | 7.83 🔴 | 28.35zł | 6.72 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-kabala` | 8.05 🔴 | 28.7% 🔴 | 0.1% 🟢 | 2.83 🔴 | 5.06 🔴 | 26.23zł | 5.77 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 9.41 🔴 | 42.2% 🔴 | 1.1% 🟢 | 2.8 🔴 | 8.56 🔴 | 28.02zł | 7.03 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 7.76 🔴 | 5.1% 🟡 | 0.2% 🟢 | 2.45 🔴 | 7.54 🔴 | 23.66zł | 6.79 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 8.15 🔴 | 10.7% 🔴 | 1.6% 🟢 | 2.39 🔴 | 8.82 🔴 | 22.43zł | 7.88 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-kabala` | 8.44 🔴 | 29.6% 🔴 | 1.5% 🟢 | 2.71 🔴 | 8.52 🔴 | 23.53zł | 7.35 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.52 🟡 | 5.6% 🟡 | 1.5% 🟢 | 2.33 🔴 | 5.19 🔴 | 18.15zł | 6.45 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-cienie` | 5.95 🟢 | 0.3% 🟢 | 1.9% 🟢 | 2.18 🔴 | 4.39 🟢 | 14.9zł | 7.03 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.53 🟡 | 1.5% 🟢 | 1.6% 🟢 | 2.22 🔴 | 4.58 🟡 | 18.67zł | 6.34 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-korona` | 6.32 🟢 | 1.2% 🟢 | 0.2% 🟢 | 2.32 🔴 | 5.25 🔴 | 19.93zł | 6.37 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.52 🟢 | 0.3% 🟢 | 1.7% 🟢 | 1.53 🟢 | 4.08 🟢 | 13.98zł | 7.12 | 🟢 OPTYMALNA |
| `5p-full` | 5.54 🟢 | 0.0% 🟢 | 1.5% 🟢 | 2.01 🔴 | 3.5 🟢 | 15.26zł | 6.48 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 0.160 | Paraliż Gry / Deadlocks 6.6% (>5%) |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.170 | Paraliż Gry / Deadlocks 26.7% (>5%) |
| `3p-korona-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-gildia` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.800 | Paraliż Gry / Deadlocks 21.0% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/419 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-alandalus-kabala` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 3.570 | Paraliż Gry / Deadlocks 28.7% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/214 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-alandalus-korona` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 4.920 | Paraliż Gry / Deadlocks 42.2% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/487 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-kabala-gildia` | ⚠️ Ostrzeżenie Witalności | 1.210 | Paraliż Gry / Deadlocks 5.1% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/182 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-korona-gildia` | ⚠️ Ostrzeżenie Witalności | 1.770 | Paraliż Gry / Deadlocks 10.7% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/449 wygranych (<8%) — gra tylko stosy |
| `3p-oficjum-korona-kabala` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 3.660 | Paraliż Gry / Deadlocks 29.6% (>5%), Martwa ścieżka skazania (swiete-oficjum): 0/256 wygranych (<8%) — gra tylko stosy |
| `4p-core` | ⚠️ Ostrzeżenie Witalności | 0.060 | Paraliż Gry / Deadlocks 5.6% (>5%) |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |