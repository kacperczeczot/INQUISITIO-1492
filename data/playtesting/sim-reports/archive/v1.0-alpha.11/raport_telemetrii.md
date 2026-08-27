# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.11

**Wersja Balansu:** `v1.0-alpha.11` | **Data:** 2026-08-20 22:45 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 7.91s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 ** 23.5** | 🔴 23.5 | 33.3% | - | 22.2% | - | 19.5% | 58.3% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 25.9** | 🔴 25.9 | 33.3% | - | 13.4% | 32.3% | - | 54.3% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 **  6.6** | 🔴 41.8 | 33.3% | - | 17.9% | 46.5% | 35.6% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 31.9** | 🔴 31.9 | 33.3% | - | - | 23.1% | 22.9% | 54.0% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 ** 31.0** | 🔴 41.0 | 33.3% | 48.5% | 19.2% | - | - | 32.3% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 **  7.6** | 🔴 33.7 | 33.3% | 48.7% | 14.7% | - | 36.6% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 **  1.6** | 🔴 7.0 | 33.3% | 73.9% | 15.3% | 10.8% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 ** 56.5** | 🔴 56.5 | 33.3% | 22.4% | - | - | 34.8% | 42.8% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 ** 31.5** | 🔴 31.5 | 33.3% | 49.6% | - | 13.9% | - | 36.5% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 **  9.7** | 🔴 14.1 | 33.3% | 59.4% | - | 4.5% | 36.1% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟡 ** 75.1** | 🟡 75.1 | 25.0% | 29.9% | 24.3% | 19.8% | 26.0% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟡 ** 82.6** | 🟡 82.6 | 25.0% | 24.3% | - | 25.6% | 28.7% | 21.4% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟠 ** 64.2** | 🟠 64.2 | 25.0% | 25.0% | 16.6% | 28.9% | - | 29.5% | 🟠 WYMAGA UWAGI |
| `4p-no-korona` | 4 | 🟢 ** 90.4** | 🟢 90.4 | 25.0% | 22.6% | 27.0% | - | 25.3% | 25.1% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟡 ** 87.2** | 🟡 87.2 | 25.0% | - | 22.7% | 26.9% | 23.3% | 27.1% | 🟡 AKCEPTOWALNY |
| `5p-full` | 5 | 🔴 ** 31.8** | 🔴 31.8 | 20.0% | 33.1% | 24.2% | 12.6% | 8.2% | 21.9% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.79 🟡 | 2.0% 🟢 | 0.2% 🟢 | 1.99 🟡 | 4.2 🟢 | 20.6zł | 7.8 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 6.74 🟡 | 1.8% 🟢 | 2.0% 🟢 | 1.89 🟡 | 3.66 🟢 | 17.6zł | 7.91 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.8 🔴 | 23.5% 🔴 | 1.8% 🟢 | 2.06 🔴 | 6.19 🔴 | 19.98zł | 7.81 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.27 🟢 | 0.5% 🟢 | 2.9% 🟢 | 1.89 🟡 | 4.12 🟢 | 13.74zł | 8.63 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 8.67 🔴 | 7.8% 🟡 | 0.1% 🟢 | 2.99 🔴 | 3.58 🟢 | 27.86zł | 6.22 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-kabala` | 8.34 🔴 | 19.9% 🔴 | 0.1% 🟢 | 3.0 🔴 | 3.38 🟢 | 25.75zł | 5.75 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 9.53 🔴 | 20.0% 🔴 | 1.3% 🟢 | 3.13 🔴 | 4.52 🟡 | 26.97zł | 6.7 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 7.44 🔴 | 0.8% 🟢 | 0.2% 🟢 | 2.58 🔴 | 5.25 🔴 | 21.37zł | 7.03 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 7.56 🔴 | 2.2% 🟢 | 1.8% 🟢 | 2.6 🔴 | 4.68 🟡 | 19.54zł | 7.88 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-kabala` | 7.68 🔴 | 8.8% 🟡 | 1.9% 🟢 | 2.81 🔴 | 5.52 🔴 | 19.07zł | 7.78 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.59 🟡 | 0.9% 🟢 | 1.7% 🟢 | 2.49 🔴 | 4.8 🟡 | 16.81zł | 6.77 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-cienie` | 5.96 🟢 | 0.0% 🟢 | 2.1% 🟢 | 2.3 🔴 | 4.34 🟢 | 13.5zł | 7.72 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.43 🟢 | 0.3% 🟢 | 1.6% 🟢 | 2.33 🔴 | 3.46 🟢 | 17.6zł | 6.59 | 🟢 OPTYMALNA |
| `4p-no-korona` | 6.42 🟢 | 0.0% 🟢 | 0.1% 🟢 | 2.48 🔴 | 4.98 🟡 | 18.99zł | 6.63 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.55 🟢 | 0.1% 🟢 | 2.0% 🟢 | 1.54 🟢 | 3.59 🟢 | 13.32zł | 7.38 | 🟢 OPTYMALNA |
| `5p-full` | 5.49 🟢 | 0.0% 🟢 | 1.6% 🟢 | 2.09 🔴 | 3.94 🟢 | 14.05zł | 6.58 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.850 | Paraliż Gry / Deadlocks 23.5% (>5%) |
| `3p-korona-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-gildia` | ⚠️ Ostrzeżenie Witalności | 0.280 | Paraliż Gry / Deadlocks 7.8% (>5%) |
| `3p-oficjum-alandalus-kabala` | ⚠️ Ostrzeżenie Witalności | 1.490 | Paraliż Gry / Deadlocks 19.9% (>5%) |
| `3p-oficjum-alandalus-korona` | ⚠️ Ostrzeżenie Witalności | 1.500 | Paraliż Gry / Deadlocks 20.0% (>5%) |
| `3p-oficjum-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 0.380 | Paraliż Gry / Deadlocks 8.8% (>5%) |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |