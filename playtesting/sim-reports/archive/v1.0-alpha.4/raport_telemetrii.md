# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.4

**Wersja Balansu:** `v1.0-alpha.4` | **Data:** 2026-08-18 23:49 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 9.36s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 ** 26.8** | 🔴 26.8 | 33.3% | - | 22.6% | - | 20.9% | 56.5% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 27.0** | 🔴 27.0 | 33.3% | - | 14.1% | 31.9% | - | 54.0% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 **  6.4** | 🔴 41.4 | 33.3% | - | 17.8% | 46.7% | 35.5% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 31.7** | 🔴 31.7 | 33.3% | - | - | 23.1% | 22.8% | 54.1% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 ** 18.8** | 🔴 43.5 | 33.3% | 47.8% | 20.1% | - | - | 32.1% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 **  6.0** | 🔴 34.6 | 33.3% | 48.1% | 14.9% | - | 37.0% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 **  0.7** | 🔴 7.0 | 33.3% | 73.9% | 15.3% | 10.8% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 ** 52.7** | 🔴 52.7 | 33.3% | 20.7% | - | - | 36.9% | 42.4% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 ** 30.5** | 🔴 30.5 | 33.3% | 50.4% | - | 13.7% | - | 35.9% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 **  9.0** | 🔴 15.4 | 33.3% | 56.3% | - | 4.2% | 39.5% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟠 ** 73.8** | 🟠 73.8 | 25.0% | 30.5% | 24.0% | 19.9% | 25.6% | - | 🟠 WYMAGA UWAGI |
| `4p-no-cienie` | 4 | 🟡 ** 82.0** | 🟡 82.0 | 25.0% | 24.6% | - | 25.4% | 28.8% | 21.2% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟠 ** 61.6** | 🟠 61.6 | 25.0% | 25.4% | 15.9% | 28.7% | - | 30.0% | 🟠 WYMAGA UWAGI |
| `4p-no-korona` | 4 | 🟡 ** 87.7** | 🟡 87.7 | 25.0% | 21.8% | 26.4% | - | 26.7% | 25.1% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🟡 ** 83.2** | 🟡 83.2 | 25.0% | - | 21.3% | 26.4% | 24.2% | 28.1% | 🟡 AKCEPTOWALNY |
| `5p-full` | 5 | 🔴 ** 40.5** | 🔴 40.5 | 20.0% | 31.2% | 23.1% | 14.2% | 10.3% | 21.2% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.72 🟡 | 3.0% 🟢 | 0.3% 🟢 | 1.97 🟡 | 4.06 🟢 | 20.92zł | 7.67 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 6.7 🟡 | 2.1% 🟢 | 2.0% 🟢 | 1.89 🟡 | 3.62 🟢 | 17.78zł | 7.88 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.56 🔴 | 23.6% 🔴 | 1.8% 🟢 | 2.06 🔴 | 5.63 🔴 | 19.63zł | 7.8 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.27 🟢 | 0.8% 🟢 | 3.0% 🟢 | 1.89 🟡 | 3.99 🟢 | 13.9zł | 8.59 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 8.59 🔴 | 13.4% 🔴 | 0.1% 🟢 | 2.98 🔴 | 3.44 🟢 | 27.91zł | 6.18 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-kabala` | 8.14 🔴 | 22.5% 🔴 | 0.1% 🟢 | 3.0 🔴 | 3.01 🟢 | 25.9zł | 5.62 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 9.33 🔴 | 27.8% 🔴 | 1.3% 🟢 | 3.12 🔴 | 4.3 🟢 | 26.65zł | 6.68 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 7.49 🔴 | 0.9% 🟢 | 0.2% 🟢 | 2.56 🔴 | 5.12 🔴 | 22.05zł | 6.92 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 7.53 🔴 | 2.8% 🟢 | 1.9% 🟢 | 2.61 🔴 | 4.71 🟡 | 19.43zł | 7.88 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-kabala` | 7.63 🔴 | 10.4% 🔴 | 2.0% 🟢 | 2.85 🔴 | 5.26 🔴 | 19.24zł | 7.74 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.59 🟡 | 1.8% 🟢 | 1.8% 🟢 | 2.5 🔴 | 4.71 🟡 | 17.39zł | 6.73 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-cienie` | 5.97 🟢 | 0.0% 🟢 | 2.1% 🟢 | 2.33 🔴 | 4.16 🟢 | 13.96zł | 7.67 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.51 🟡 | 0.5% 🟢 | 1.7% 🟢 | 2.35 🔴 | 3.55 🟢 | 18.04zł | 6.65 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-korona` | 6.44 🟢 | 0.2% 🟢 | 0.2% 🟢 | 2.49 🔴 | 4.84 🟡 | 19.71zł | 6.55 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.58 🟢 | 0.4% 🟢 | 2.0% 🟢 | 1.56 🟢 | 3.53 🟢 | 13.77zł | 7.36 | 🟢 OPTYMALNA |
| `5p-full` | 5.51 🟢 | 0.0% 🟢 | 1.6% 🟢 | 2.1 🔴 | 3.88 🟢 | 14.57zł | 6.58 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.860 | Paraliż Gry / Deadlocks 23.6% (>5%) |
| `3p-korona-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-gildia` | ⚠️ Ostrzeżenie Witalności | 0.840 | Paraliż Gry / Deadlocks 13.4% (>5%) |
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