# Raport Telemetrii i Szans Wygranych (Win Shares) dla Kanonu 4P — Wersja Balansu: v1.0-alpha.91

**Wersja Balansu:** `v1.0-alpha.91` | **Data:** 2026-08-29 02:58 | **Wielkość Próby:** 10000 gier/setup (50000 gier łącznie) | **Czas Symulacji:** 0.14s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟡 ** 85.2** | 🟡 85.2 | 25.0% | 25.2% | 21.3% | 27.6% | 25.9% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟡 ** 86.0** | 🟡 86.0 | 25.0% | 24.6% | - | 22.4% | 28.4% | 24.6% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟢 ** 97.0** | 🟢 97.0 | 25.0% | 24.0% | 25.5% | 25.3% | - | 25.2% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟢 ** 93.5** | 🟢 93.5 | 25.0% | 26.8% | 23.8% | - | 24.3% | 25.1% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟢 ** 99.1** | 🟢 99.1 | 25.0% | - | 24.9% | 25.0% | 24.7% | 25.4% | 🟢 ZBALANSOWANY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.91 🟢 | 0.0% 🟢 | 5.4% 🟢 | 1.71 🟢 | 7.75 🟢 | 8.16zł | 7.93 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.62 🟢 | 0.0% 🟢 | 6.3% 🟢 | 1.57 🟢 | 7.69 🟢 | 5.36zł | 8.41 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.78 🟢 | 0.0% 🟢 | 5.4% 🟢 | 1.64 🟢 | 8.01 🟢 | 11.18zł | 8.43 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.51 🟢 | 0.0% 🟢 | 1.9% 🟢 | 1.59 🟢 | 7.8 🟢 | 10.65zł | 8.37 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.94 🟢 | 0.0% 🟢 | 5.2% 🟢 | 1.1 🟢 | 6.69 🟢 | 9.7zł | 7.54 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |