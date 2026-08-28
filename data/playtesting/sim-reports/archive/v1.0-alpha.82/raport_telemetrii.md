# Raport Telemetrii i Szans Wygranych (Win Shares) dla Kanonu 4P — Wersja Balansu: v1.0-alpha.82

**Wersja Balansu:** `v1.0-alpha.82` | **Data:** 2026-08-29 01:29 | **Wielkość Próby:** 10000 gier/setup (50000 gier łącznie) | **Czas Symulacji:** 0.15s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟠 ** 78.1** | 🟠 78.1 | 25.0% | 29.7% | 20.6% | 25.4% | 24.3% | - | 🟠 WYMAGA UWAGI |
| `4p-no-cienie` | 4 | 🟠 ** 66.3** | 🟠 66.3 | 25.0% | 28.2% | - | 18.0% | 30.6% | 23.3% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🟢 ** 94.0** | 🟢 94.0 | 25.0% | 25.0% | 26.1% | 23.3% | - | 25.7% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟠 ** 77.1** | 🟠 77.1 | 25.0% | 30.6% | 23.1% | - | 24.4% | 21.9% | 🟠 WYMAGA UWAGI |
| `4p-no-oficjum` | 4 | 🟡 ** 81.6** | 🟡 81.6 | 25.0% | - | 27.1% | 22.5% | 22.0% | 28.3% | 🟡 AKCEPTOWALNY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.97 🟢 | 0.0% 🟢 | 5.0% 🟢 | 1.76 🟢 | 7.95 🟢 | 7.4zł | 8.07 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.63 🟢 | 0.0% 🟢 | 5.8% 🟢 | 1.63 🟢 | 7.47 🟢 | 4.62zł | 8.4 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.93 🟢 | 0.0% 🟢 | 4.9% 🟢 | 1.67 🟢 | 8.27 🟢 | 10.14zł | 8.51 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.5 🟢 | 0.0% 🟢 | 1.1% 🟢 | 1.64 🟢 | 7.62 🟢 | 9.82zł | 8.39 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 6.0 🟢 | 0.0% 🟢 | 5.0% 🟢 | 1.1 🟢 | 7.27 🟢 | 9.15zł | 7.71 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |