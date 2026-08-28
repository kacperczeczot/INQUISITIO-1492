# Raport Telemetrii i Szans Wygranych (Win Shares) dla Kanonu 4P — Wersja Balansu: v1.0-alpha.85

**Wersja Balansu:** `v1.0-alpha.85` | **Data:** 2026-08-29 01:45 | **Wielkość Próby:** 10000 gier/setup (50000 gier łącznie) | **Czas Symulacji:** 0.14s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟡 ** 83.3** | 🟡 83.3 | 25.0% | 27.7% | 20.9% | 26.3% | 25.1% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟠 ** 72.6** | 🟠 72.6 | 25.0% | 27.0% | - | 19.3% | 29.9% | 23.8% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🟢 ** 97.8** | 🟢 97.8 | 25.0% | 25.3% | 24.2% | 25.2% | - | 25.2% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟠 ** 78.5** | 🟠 78.5 | 25.0% | 30.3% | 22.2% | - | 24.6% | 23.0% | 🟠 WYMAGA UWAGI |
| `4p-no-oficjum` | 4 | 🟢 ** 93.2** | 🟢 93.2 | 25.0% | - | 26.4% | 24.7% | 23.3% | 25.6% | 🟢 ZBALANSOWANY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.84 🟢 | 0.0% 🟢 | 5.3% 🟢 | 1.71 🟢 | 7.81 🟢 | 7.9zł | 8.05 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.5 🟢 | 0.0% 🟢 | 6.1% 🟢 | 1.56 🟢 | 7.64 🟢 | 4.76zł | 8.5 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.8 🟢 | 0.0% 🟢 | 5.5% 🟢 | 1.66 🟢 | 8.15 🟢 | 10.54zł | 8.51 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.4 🟢 | 0.0% 🟢 | 1.5% 🟢 | 1.57 🟢 | 7.76 🟢 | 10.11zł | 8.5 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.94 🟢 | 0.0% 🟢 | 4.9% 🟢 | 1.09 🟢 | 6.93 🟢 | 9.42zł | 7.62 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |