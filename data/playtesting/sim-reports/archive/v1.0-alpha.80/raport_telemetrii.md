# Raport Telemetrii i Szans Wygranych (Win Shares) dla Kanonu 4P — Wersja Balansu: v1.0-alpha.80

**Wersja Balansu:** `v1.0-alpha.80` | **Data:** 2026-08-29 01:32 | **Wielkość Próby:** 10000 gier/setup (50000 gier łącznie) | **Czas Symulacji:** 0.16s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟠 ** 71.6** | 🟠 71.6 | 25.0% | 31.1% | 19.7% | 25.3% | 23.8% | - | 🟠 WYMAGA UWAGI |
| `4p-no-cienie` | 4 | 🔴 ** 63.6** | 🔴 63.6 | 25.0% | 30.1% | - | 17.2% | 29.4% | 23.3% | 🔴 ODCHYLONY |
| `4p-no-kabala` | 4 | 🟢 ** 93.5** | 🟢 93.5 | 25.0% | 26.3% | 24.5% | 23.4% | - | 25.9% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟠 ** 68.3** | 🟠 68.3 | 25.0% | 32.8% | 22.8% | - | 23.3% | 21.1% | 🟠 WYMAGA UWAGI |
| `4p-no-oficjum` | 4 | 🟡 ** 81.6** | 🟡 81.6 | 25.0% | - | 27.1% | 22.5% | 22.0% | 28.3% | 🟡 AKCEPTOWALNY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.98 🟢 | 0.0% 🟢 | 5.3% 🟢 | 1.67 🟢 | 7.99 🟢 | 7.24zł | 8.14 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.64 🟢 | 0.0% 🟢 | 6.2% 🟢 | 1.57 🟢 | 7.48 🟢 | 4.47zł | 8.43 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.93 🟢 | 0.0% 🟢 | 5.2% 🟢 | 1.59 🟢 | 8.25 🟢 | 9.94zł | 8.55 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.49 🟢 | 0.0% 🟢 | 1.3% 🟢 | 1.56 🟢 | 7.59 🟢 | 9.58zł | 8.41 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 6.0 🟢 | 0.0% 🟢 | 5.0% 🟢 | 1.1 🟢 | 7.27 🟢 | 9.15zł | 7.71 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |