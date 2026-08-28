# Raport Telemetrii i Szans Wygranych (Win Shares) dla Kanonu 4P — Wersja Balansu: v1.0-alpha.83

**Wersja Balansu:** `v1.0-alpha.83` | **Data:** 2026-08-29 01:43 | **Wielkość Próby:** 10000 gier/setup (50000 gier łącznie) | **Czas Symulacji:** 0.18s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟡 ** 80.5** | 🟡 80.5 | 25.0% | 28.6% | 20.7% | 26.2% | 24.5% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟠 ** 69.4** | 🟠 69.4 | 25.0% | 28.7% | - | 18.9% | 29.6% | 22.7% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🟢 ** 98.8** | 🟢 98.8 | 25.0% | 25.4% | 25.2% | 24.7% | - | 24.7% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟠 ** 75.0** | 🟠 75.0 | 25.0% | 31.1% | 23.2% | - | 24.1% | 21.6% | 🟠 WYMAGA UWAGI |
| `4p-no-oficjum` | 4 | 🟡 ** 88.1** | 🟡 88.1 | 25.0% | - | 26.8% | 24.5% | 22.1% | 26.5% | 🟡 AKCEPTOWALNY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.87 🟢 | 0.0% 🟢 | 5.4% 🟢 | 1.69 🟢 | 7.83 🟢 | 7.59zł | 8.07 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.54 🟢 | 0.0% 🟢 | 6.3% 🟢 | 1.56 🟢 | 7.48 🟢 | 4.52zł | 8.47 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.82 🟢 | 0.0% 🟢 | 5.5% 🟢 | 1.62 🟢 | 8.12 🟢 | 10.25zł | 8.52 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.44 🟢 | 0.0% 🟢 | 1.6% 🟢 | 1.57 🟢 | 7.72 🟢 | 9.87zł | 8.46 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.94 🟢 | 0.0% 🟢 | 5.0% 🟢 | 1.09 🟢 | 7.08 🟢 | 9.44zł | 7.66 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |