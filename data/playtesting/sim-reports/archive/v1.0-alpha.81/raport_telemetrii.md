# Raport Telemetrii i Szans Wygranych (Win Shares) dla Kanonu 4P — Wersja Balansu: v1.0-alpha.81

**Wersja Balansu:** `v1.0-alpha.81` | **Data:** 2026-08-29 01:28 | **Wielkość Próby:** 10000 gier/setup (50000 gier łącznie) | **Czas Symulacji:** 0.16s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟠 ** 79.4** | 🟠 79.4 | 25.0% | 29.6% | 21.0% | 25.2% | 24.2% | - | 🟠 WYMAGA UWAGI |
| `4p-no-cienie` | 4 | 🟠 ** 66.3** | 🟠 66.3 | 25.0% | 28.0% | - | 18.1% | 30.8% | 23.1% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🟢 ** 95.1** | 🟢 95.1 | 25.0% | 25.2% | 25.7% | 23.5% | - | 25.7% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟠 ** 77.4** | 🟠 77.4 | 25.0% | 30.3% | 23.3% | - | 24.9% | 21.4% | 🟠 WYMAGA UWAGI |
| `4p-no-oficjum` | 4 | 🟡 ** 81.6** | 🟡 81.6 | 25.0% | - | 27.1% | 22.5% | 22.0% | 28.3% | 🟡 AKCEPTOWALNY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.98 🟢 | 0.0% 🟢 | 5.1% 🟢 | 1.72 🟢 | 7.95 🟢 | 7.32zł | 8.07 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.64 🟢 | 0.0% 🟢 | 6.0% 🟢 | 1.6 🟢 | 7.42 🟢 | 4.52zł | 8.38 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.96 🟢 | 0.0% 🟢 | 5.1% 🟢 | 1.63 🟢 | 8.28 🟢 | 10.08zł | 8.5 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.51 🟢 | 0.0% 🟢 | 1.2% 🟢 | 1.6 🟢 | 7.61 🟢 | 9.72zł | 8.36 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 6.0 🟢 | 0.0% 🟢 | 5.0% 🟢 | 1.1 🟢 | 7.27 🟢 | 9.15zł | 7.71 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |