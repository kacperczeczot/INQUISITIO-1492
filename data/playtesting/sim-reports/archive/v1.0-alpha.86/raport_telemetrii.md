# Raport Telemetrii i Szans Wygranych (Win Shares) dla Kanonu 4P — Wersja Balansu: v1.0-alpha.86

**Wersja Balansu:** `v1.0-alpha.86` | **Data:** 2026-08-29 01:47 | **Wielkość Próby:** 10000 gier/setup (50000 gier łącznie) | **Czas Symulacji:** 0.14s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟡 ** 87.7** | 🟡 87.7 | 25.0% | 26.9% | 22.1% | 26.6% | 24.4% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟠 ** 78.0** | 🟠 78.0 | 25.0% | 26.7% | - | 19.7% | 28.2% | 25.4% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🟢 ** 96.3** | 🟢 96.3 | 25.0% | 24.0% | 25.5% | 24.7% | - | 25.8% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟡 ** 82.1** | 🟡 82.1 | 25.0% | 29.5% | 23.7% | - | 22.4% | 24.4% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🟢 ** 93.2** | 🟢 93.2 | 25.0% | - | 26.4% | 24.7% | 23.3% | 25.6% | 🟢 ZBALANSOWANY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.9 🟢 | 0.0% 🟢 | 5.4% 🟢 | 1.71 🟢 | 7.84 🟢 | 8.25zł | 7.98 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.54 🟢 | 0.0% 🟢 | 6.3% 🟢 | 1.57 🟢 | 7.72 🟢 | 4.88zł | 8.48 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.82 🟢 | 0.0% 🟢 | 5.6% 🟢 | 1.66 🟢 | 8.05 🟢 | 10.8zł | 8.43 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.44 🟢 | 0.0% 🟢 | 1.6% 🟢 | 1.58 🟢 | 7.78 🟢 | 10.2zł | 8.46 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.94 🟢 | 0.0% 🟢 | 4.9% 🟢 | 1.09 🟢 | 6.93 🟢 | 9.42zł | 7.62 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |