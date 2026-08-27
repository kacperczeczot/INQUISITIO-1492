# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v0.99.24

**Wersja Balansu:** `v0.99.24` | **Data:** 2026-08-18 16:19 | **Wielkość Próby:** 1000 gier/setup (16000 gier łącznie) | **Czas Symulacji:** 15.06s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | 🔴 ** 26.8** | 🔴 26.8 | 33.3% | - | 22.6% | - | 20.9% | 56.5% | 🔴 ODCHYLONY |
| `3p-cienie-korona-gildia` | 3 | 🔴 ** 27.0** | 🔴 27.0 | 33.3% | - | 14.1% | 31.9% | - | 54.0% | 🔴 ODCHYLONY |
| `3p-cienie-korona-kabala` | 3 | 🔴 **  6.3** | 🔴 39.8 | 33.3% | - | 17.2% | 47.1% | 35.7% | - | 🔴 ODCHYLONY |
| `3p-korona-kabala-gildia` | 3 | 🔴 ** 33.5** | 🔴 33.5 | 33.3% | - | - | 23.0% | 23.7% | 53.3% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-gildia` | 3 | 🔴 ** 18.8** | 🔴 43.5 | 33.3% | 47.8% | 20.1% | - | - | 32.1% | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-kabala` | 3 | 🔴 **  6.0** | 🔴 34.6 | 33.3% | 48.1% | 14.9% | - | 37.0% | - | 🔴 ODCHYLONY |
| `3p-oficjum-alandalus-korona` | 3 | 🔴 **  0.7** | 🔴 6.9 | 33.3% | 74.0% | 15.3% | 10.7% | - | - | 🔴 ODCHYLONY |
| `3p-oficjum-kabala-gildia` | 3 | 🔴 ** 52.7** | 🔴 52.7 | 33.3% | 20.7% | - | - | 36.9% | 42.4% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-gildia` | 3 | 🔴 ** 31.5** | 🔴 31.5 | 33.3% | 48.6% | - | 13.4% | - | 38.0% | 🔴 ODCHYLONY |
| `3p-oficjum-korona-kabala` | 3 | 🔴 **  8.4** | 🔴 15.5 | 33.3% | 56.1% | - | 4.3% | 39.6% | - | 🔴 ODCHYLONY |
| `4p-core` | 4 | 🟠 ** 70.8** | 🟠 70.8 | 25.0% | 30.4% | 23.2% | 19.2% | 27.2% | - | 🟠 WYMAGA UWAGI |
| `4p-no-cienie` | 4 | 🟡 ** 85.7** | 🟡 85.7 | 25.0% | 24.5% | - | 26.1% | 27.7% | 21.7% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🔴 ** 59.9** | 🔴 59.9 | 25.0% | 24.6% | 15.8% | 28.6% | - | 31.0% | 🔴 ODCHYLONY |
| `4p-no-korona` | 4 | 🟡 ** 87.7** | 🟡 87.7 | 25.0% | 21.8% | 26.4% | - | 26.7% | 25.1% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🟡 ** 82.3** | 🟡 82.3 | 25.0% | - | 22.5% | 27.4% | 22.2% | 27.9% | 🟡 AKCEPTOWALNY |
| `5p-full` | 5 | 🔴 ** 37.6** | 🔴 37.6 | 20.0% | 31.9% | 22.9% | 13.1% | 10.1% | 22.0% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 6.72 🟡 | 3.0% 🟢 | 0.3% 🟢 | 1.97 🟡 | 4.06 🟢 | 20.92zł | 7.67 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-gildia` | 6.74 🟡 | 2.2% 🟢 | 2.0% 🟢 | 1.91 🟡 | 3.55 🟢 | 17.91zł | 7.7 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-cienie-korona-kabala` | 7.55 🔴 | 23.4% 🔴 | 1.7% 🟢 | 2.08 🔴 | 5.46 🔴 | 19.66zł | 7.69 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-korona-kabala-gildia` | 6.28 🟢 | 0.8% 🟢 | 2.8% 🟢 | 1.89 🟡 | 3.89 🟢 | 13.97zł | 8.41 | 🟢 OPTYMALNA |
| `3p-oficjum-alandalus-gildia` | 8.59 🔴 | 13.4% 🔴 | 0.1% 🟢 | 2.98 🔴 | 3.44 🟢 | 27.91zł | 6.18 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-kabala` | 8.14 🔴 | 22.5% 🔴 | 0.1% 🟢 | 3.0 🔴 | 3.01 🟢 | 25.9zł | 5.62 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-alandalus-korona` | 9.36 🔴 | 28.4% 🔴 | 1.3% 🟢 | 3.13 🔴 | 4.24 🟢 | 26.74zł | 6.57 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-kabala-gildia` | 7.49 🔴 | 0.9% 🟢 | 0.2% 🟢 | 2.56 🔴 | 5.12 🔴 | 22.05zł | 6.92 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-gildia` | 7.66 🔴 | 2.9% 🟢 | 1.9% 🟢 | 2.64 🔴 | 4.71 🟡 | 19.85zł | 7.73 | ⚠️ WARTOŚCI BRZEGOWE |
| `3p-oficjum-korona-kabala` | 7.7 🔴 | 11.2% 🔴 | 1.8% 🟢 | 2.86 🔴 | 5.29 🔴 | 19.45zł | 7.7 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-core` | 6.64 🟡 | 2.1% 🟢 | 1.6% 🟢 | 2.52 🔴 | 4.67 🟡 | 17.59zł | 6.64 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-cienie` | 5.98 🟢 | 0.0% 🟢 | 2.1% 🟢 | 2.33 🔴 | 4.1 🟢 | 14.0zł | 7.57 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.61 🟡 | 0.7% 🟢 | 1.7% 🟢 | 2.38 🔴 | 3.48 🟢 | 18.33zł | 6.5 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-korona` | 6.44 🟢 | 0.2% 🟢 | 0.2% 🟢 | 2.49 🔴 | 4.84 🟡 | 19.71zł | 6.55 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.55 🟢 | 0.3% 🟢 | 2.0% 🟢 | 1.54 🟢 | 3.41 🟢 | 13.74zł | 7.24 | 🟢 OPTYMALNA |
| `5p-full` | 5.55 🟢 | 0.0% 🟢 | 1.5% 🟢 | 2.12 🔴 | 3.86 🟢 | 14.71zł | 6.51 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-cienie-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 1.840 | Paraliż Gry / Deadlocks 23.4% (>5%) |
| `3p-korona-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-alandalus-gildia` | ⚠️ Ostrzeżenie Witalności | 0.840 | Paraliż Gry / Deadlocks 13.4% (>5%) |
| `3p-oficjum-alandalus-kabala` | ⚠️ Ostrzeżenie Witalności | 1.750 | Paraliż Gry / Deadlocks 22.5% (>5%) |
| `3p-oficjum-alandalus-korona` | 🔴 Zagrożenie Witalności (Kastracja Mechanik) | 2.340 | Paraliż Gry / Deadlocks 28.4% (>5%) |
| `3p-oficjum-kabala-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-korona-gildia` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `3p-oficjum-korona-kabala` | ⚠️ Ostrzeżenie Witalności | 0.620 | Paraliż Gry / Deadlocks 11.2% (>5%) |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `5p-full` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |