# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v0.99.26

**Wersja Balansu:** `v0.99.26` | **Data:** 2026-08-18 16:44 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 14.2s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 ** 26.8** | 🔴 26.8 | 33.3% | - | 22.6% | - | 20.9% | 56.5% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 27.0** | 🔴 27.0 | 33.3% | - | 14.1% | 31.9% | - | 54.0% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 **  6.1** | 🔴 39.3 | 33.3% | - | 17.1% | 47.3% | 35.6% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 33.3** | 🔴 33.3 | 33.3% | - | - | 23.1% | 23.5% | 53.4% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 ** 31.9** | 🔴 43.9 | 33.3% | 47.6% | 20.1% | - | - | 32.3% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 **  8.0** | 🔴 34.6 | 33.3% | 48.1% | 14.9% | - | 37.0% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 **  1.6** | 🔴 7.0 | 33.3% | 73.9% | 15.3% | 10.8% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 ** 52.7** | 🔴 52.7 | 33.3% | 20.7% | - | - | 36.9% | 42.4% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 ** 30.5** | 🔴 30.5 | 33.3% | 50.2% | - | 13.6% | - | 36.2% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 ** 10.3** | 🔴 14.8 | 33.3% | 57.5% | - | 4.1% | 38.4% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟠 ** 71.6** | 🟠 71.6 | 25.0% | 30.6% | 22.9% | 19.7% | 26.8% | - | 🟠 WYMAGA UWAGI |
| `4p-no-cienie` | 4 | 🟡 ** 84.8** | 🟡 84.8 | 25.0% | 24.9% | - | 25.9% | 27.8% | 21.4% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟠 ** 61.8** | 🟠 61.8 | 25.0% | 25.5% | 15.9% | 28.7% | - | 29.9% | 🟠 WYMAGA UWAGI |
| `4p-no-korona` | 4 | 🟡 ** 87.7** | 🟡 87.7 | 25.0% | 21.8% | 26.4% | - | 26.7% | 25.1% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🟡 ** 80.1** | 🟡 80.1 | 25.0% | - | 22.1% | 27.7% | 22.0% | 28.2% | 🟡 AKCEPTOWALNY |
| `5p-full` | 5 | 🔴 ** 38.4** | 🔴 38.4 | 20.0% | 31.9% | 23.1% | 13.2% | 10.5% | 21.3% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.75 🟡 | 2.2% 🟢 | 0.3% 🟢 | 1.97 🟡 | 4.08 🟢 | 20.98zł | 7.68 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 6.72 🟡 | 1.9% 🟢 | 2.0% 🟢 | 1.89 🟡 | 3.64 🟢 | 17.83zł | 7.88 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.8 🔴 | 23.6% 🔴 | 1.6% 🟢 | 2.07 🔴 | 6.21 🔴 | 20.38zł | 7.83 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.27 🟢 | 0.6% 🟢 | 2.8% 🟢 | 1.88 🟡 | 4.04 🟢 | 13.94zł | 8.58 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 8.68 🔴 | 8.2% 🟡 | 0.1% 🟢 | 2.98 🔴 | 3.52 🟢 | 28.14zł | 6.19 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-kabala` | 8.33 🔴 | 19.6% 🔴 | 0.1% 🟢 | 3.0 🔴 | 3.2 🟢 | 26.49zł | 5.64 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 9.53 🔴 | 20.0% 🔴 | 1.3% 🟢 | 3.13 🔴 | 4.52 🟡 | 27.24zł | 6.7 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 7.5 🔴 | 0.8% 🟢 | 0.2% 🟢 | 2.56 🔴 | 5.12 🔴 | 22.07zł | 6.92 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 7.55 🔴 | 2.4% 🟢 | 1.9% 🟢 | 2.61 🔴 | 4.74 🟡 | 19.5zł | 7.88 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-kabala` | 7.71 🔴 | 8.6% 🟡 | 1.8% 🟢 | 2.83 🔴 | 5.41 🔴 | 19.47zł | 7.76 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.6 🟡 | 0.9% 🟢 | 1.6% 🟢 | 2.49 🔴 | 4.77 🟡 | 17.47zł | 6.74 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-cienie` | 5.97 🟢 | 0.0% 🟢 | 2.1% 🟢 | 2.32 🔴 | 4.21 🟢 | 13.95zł | 7.69 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.52 🟡 | 0.4% 🟢 | 1.7% 🟢 | 2.35 🔴 | 3.55 🟢 | 18.05zł | 6.65 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-korona` | 6.44 🟢 | 0.0% 🟢 | 0.2% 🟢 | 2.49 🔴 | 4.84 🟡 | 19.71zł | 6.55 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.56 🟢 | 0.1% 🟢 | 2.0% 🟢 | 1.54 🟢 | 3.51 🟢 | 13.74zł | 7.36 | 🟢 OPTYMALNA |
| `5p-full` | 5.51 🟢 | 0.0% 🟢 | 1.5% 🟢 | 2.1 🔴 | 3.91 🟢 | 14.62zł | 6.59 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.860 | Paraliż Gry / Deadlocks 23.6% (>5%) |
| `3p-korona-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-gildia` | ⚠️ Ostrzeżenie Witalności | 0.320 | Paraliż Gry / Deadlocks 8.2% (>5%) |
| `3p-oficjum-alandalus-kabala` | ⚠️ Ostrzeżenie Witalności | 1.460 | Paraliż Gry / Deadlocks 19.6% (>5%) |
| `3p-oficjum-alandalus-korona` | ⚠️ Ostrzeżenie Witalności | 1.500 | Paraliż Gry / Deadlocks 20.0% (>5%) |
| `3p-oficjum-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 0.360 | Paraliż Gry / Deadlocks 8.6% (>5%) |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |