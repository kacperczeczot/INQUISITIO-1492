# Raport Telemetrii i Szans Wygranych (Win Shares) dla Kanonu 4P — Wersja Balansu: v1.0-alpha.92

**Wersja Balansu:** `v1.0-alpha.92` | **Data:** 2026-08-29 10:30 | **Wielkość Próby:** 10000 gier/setup (50000 gier łącznie) | **Czas Symulacji:** 0.16s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟢 ** 92.1** | 🟢 92.1 | 25.0% | 25.2% | 23.3% | 27.0% | 24.5% | - | 🟢 ZBALANSOWANY |
| `4p-no-cienie` | 4 | 🟡 ** 86.7** | 🟡 86.7 | 25.0% | 25.2% | - | 22.0% | 27.9% | 24.8% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟢 ** 95.4** | 🟢 95.4 | 25.0% | 23.9% | 24.4% | 25.9% | - | 25.8% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟢 ** 96.1** | 🟢 96.1 | 25.0% | 25.8% | 24.2% | - | 25.7% | 24.3% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟢 ** 98.5** | 🟢 98.5 | 25.0% | - | 25.4% | 24.5% | 25.2% | 24.9% | 🟢 ZBALANSOWANY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.91 🟢 | 0.0% 🟢 | 5.6% 🟢 | 1.74 🟢 | 7.8 🟢 | 7.66zł | 7.99 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.59 🟢 | 0.0% 🟢 | 6.3% 🟢 | 1.57 🟢 | 7.72 🟢 | 5.25zł | 8.48 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.78 🟢 | 0.0% 🟢 | 5.5% 🟢 | 1.65 🟢 | 8.03 🟢 | 10.75zł | 8.5 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.53 🟢 | 0.0% 🟢 | 1.9% 🟢 | 1.59 🟢 | 7.85 🟢 | 10.44zł | 8.39 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.97 🟢 | 0.0% 🟢 | 5.2% 🟢 | 1.1 🟢 | 6.67 🟢 | 9.46zł | 7.54 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |