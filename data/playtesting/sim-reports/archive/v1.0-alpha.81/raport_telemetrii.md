# Raport Telemetrii i Szans Wygranych (Win Shares) dla Kanonu 4P — Wersja Balansu: v1.0-alpha.81

**Wersja Balansu:** `v1.0-alpha.81` | **Data:** 2026-08-29 01:37 | **Wielkość Próby:** 10000 gier/setup (50000 gier łącznie) | **Czas Symulacji:** 0.16s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟠 ** 72.7** | 🟠 72.7 | 25.0% | 30.1% | 19.5% | 27.0% | 23.5% | - | 🟠 WYMAGA UWAGI |
| `4p-no-cienie` | 4 | 🟠 ** 66.9** | 🟠 66.9 | 25.0% | 29.7% | - | 18.3% | 29.3% | 22.7% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🟢 ** 96.2** | 🟢 96.2 | 25.0% | 25.6% | 23.9% | 25.8% | - | 24.8% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟠 ** 68.3** | 🟠 68.3 | 25.0% | 32.8% | 22.8% | - | 23.3% | 21.1% | 🟠 WYMAGA UWAGI |
| `4p-no-oficjum` | 4 | 🟡 ** 86.2** | 🟡 86.2 | 25.0% | - | 26.5% | 24.8% | 21.6% | 27.1% | 🟡 AKCEPTOWALNY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.94 🟢 | 0.0% 🟢 | 5.3% 🟢 | 1.66 🟢 | 7.88 🟢 | 7.28zł | 8.11 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.63 🟢 | 0.0% 🟢 | 6.2% 🟢 | 1.56 🟢 | 7.42 🟢 | 4.52zł | 8.42 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.89 🟢 | 0.0% 🟢 | 5.2% 🟢 | 1.58 🟢 | 8.13 🟢 | 9.96zł | 8.53 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.49 🟢 | 0.0% 🟢 | 1.3% 🟢 | 1.56 🟢 | 7.59 🟢 | 9.58zł | 8.41 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.96 🟢 | 0.0% 🟢 | 5.0% 🟢 | 1.1 🟢 | 7.15 🟢 | 9.16zł | 7.69 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |