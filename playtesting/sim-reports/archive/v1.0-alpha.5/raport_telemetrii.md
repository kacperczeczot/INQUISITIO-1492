# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.5

**Wersja Balansu:** `v1.0-alpha.5` | **Data:** 2026-08-18 23:57 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 9.11s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 ** 25.4** | 🔴 25.4 | 33.3% | - | 22.4% | - | 20.4% | 57.2% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 25.7** | 🔴 25.7 | 33.3% | - | 13.4% | 32.1% | - | 54.5% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 **  6.4** | 🔴 41.4 | 33.3% | - | 17.8% | 46.7% | 35.5% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 32.2** | 🔴 32.2 | 33.3% | - | - | 23.1% | 23.0% | 53.9% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 ** 18.3** | 🔴 40.3 | 33.3% | 48.9% | 19.2% | - | - | 31.9% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 **  6.0** | 🔴 34.6 | 33.3% | 48.1% | 14.9% | - | 37.0% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 **  0.7** | 🔴 7.0 | 33.3% | 73.9% | 15.3% | 10.8% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 ** 52.3** | 🔴 52.3 | 33.3% | 20.5% | - | - | 37.3% | 42.2% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 ** 31.9** | 🔴 31.9 | 33.3% | 49.4% | - | 14.0% | - | 36.6% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 **  9.0** | 🔴 15.4 | 33.3% | 56.3% | - | 4.2% | 39.5% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟠 ** 73.8** | 🟠 73.8 | 25.0% | 30.5% | 24.0% | 19.9% | 25.6% | - | 🟠 WYMAGA UWAGI |
| `4p-no-cienie` | 4 | 🟡 ** 82.2** | 🟡 82.2 | 25.0% | 24.8% | - | 25.7% | 28.5% | 21.0% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟠 ** 63.5** | 🟠 63.5 | 25.0% | 25.1% | 16.4% | 29.0% | - | 29.5% | 🟠 WYMAGA UWAGI |
| `4p-no-korona` | 4 | 🟡 ** 89.5** | 🟡 89.5 | 25.0% | 22.3% | 26.9% | - | 25.8% | 25.0% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🟡 ** 87.5** | 🟡 87.5 | 25.0% | - | 22.0% | 26.9% | 24.5% | 26.6% | 🟡 AKCEPTOWALNY |
| `5p-full` | 5 | 🔴 ** 39.6** | 🔴 39.6 | 20.0% | 31.7% | 22.7% | 13.5% | 10.7% | 21.4% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.76 🟡 | 2.9% 🟢 | 0.2% 🟢 | 1.98 🟡 | 4.08 🟢 | 21.05zł | 7.72 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 6.72 🟡 | 2.1% 🟢 | 2.0% 🟢 | 1.89 🟡 | 3.64 🟢 | 17.83zł | 7.91 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.56 🔴 | 23.6% 🔴 | 1.8% 🟢 | 2.06 🔴 | 5.63 🔴 | 19.63zł | 7.8 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.27 🟢 | 0.7% 🟢 | 3.0% 🟢 | 1.88 🟡 | 4.02 🟢 | 13.88zł | 8.59 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 8.58 🔴 | 12.9% 🔴 | 0.1% 🟢 | 2.98 🔴 | 3.51 🟢 | 27.88zł | 6.21 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-kabala` | 8.14 🔴 | 22.5% 🔴 | 0.1% 🟢 | 3.0 🔴 | 3.01 🟢 | 25.9zł | 5.62 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 9.33 🔴 | 27.8% 🔴 | 1.3% 🟢 | 3.12 🔴 | 4.3 🟢 | 26.65zł | 6.68 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 7.47 🔴 | 0.9% 🟢 | 0.2% 🟢 | 2.56 🔴 | 5.12 🔴 | 22.0zł | 6.91 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 7.54 🔴 | 2.6% 🟢 | 1.9% 🟢 | 2.6 🔴 | 4.64 🟡 | 19.5zł | 7.87 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-kabala` | 7.63 🔴 | 10.4% 🔴 | 2.0% 🟢 | 2.85 🔴 | 5.26 🔴 | 19.24zł | 7.74 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.59 🟡 | 1.8% 🟢 | 1.8% 🟢 | 2.5 🔴 | 4.71 🟡 | 17.39zł | 6.73 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-cienie` | 5.96 🟢 | 0.0% 🟢 | 2.2% 🟢 | 2.31 🔴 | 4.17 🟢 | 13.9zł | 7.67 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.44 🟢 | 0.4% 🟢 | 1.6% 🟢 | 2.33 🔴 | 3.46 🟢 | 17.81zł | 6.6 | 🟢 OPTYMALNA |
| `4p-no-korona` | 6.44 🟢 | 0.2% 🟢 | 0.1% 🟢 | 2.49 🔴 | 4.81 🟡 | 19.71zł | 6.56 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.57 🟢 | 0.4% 🟢 | 2.0% 🟢 | 1.55 🟢 | 3.54 🟢 | 13.76zł | 7.36 | 🟢 OPTYMALNA |
| `5p-full` | 5.51 🟢 | 0.0% 🟢 | 1.6% 🟢 | 2.12 🔴 | 3.85 🟢 | 14.58zł | 6.56 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.860 | Paraliż Gry / Deadlocks 23.6% (>5%) |
| `3p-korona-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-gildia` | ⚠️ Ostrzeżenie Witalności | 0.790 | Paraliż Gry / Deadlocks 12.9% (>5%) |
| `3p-oficjum-alandalus-kabala` | ⚠️ Ostrzeżenie Witalności | 1.750 | Paraliż Gry / Deadlocks 22.5% (>5%) |
| `3p-oficjum-alandalus-korona` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.280 | Paraliż Gry / Deadlocks 27.8% (>5%) |
| `3p-oficjum-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 0.540 | Paraliż Gry / Deadlocks 10.4% (>5%) |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |