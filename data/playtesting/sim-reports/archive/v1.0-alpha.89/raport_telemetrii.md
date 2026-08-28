# Raport Telemetrii i Szans Wygranych (Win Shares) dla Kanonu 4P — Wersja Balansu: v1.0-alpha.89

**Wersja Balansu:** `v1.0-alpha.89` | **Data:** 2026-08-29 01:54 | **Wielkość Próby:** 10000 gier/setup (50000 gier łącznie) | **Czas Symulacji:** 0.14s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟡 ** 88.4** | 🟡 88.4 | 25.0% | 26.2% | 22.1% | 26.9% | 24.7% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟡 ** 80.4** | 🟡 80.4 | 25.0% | 25.8% | - | 21.4% | 29.3% | 23.5% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟢 ** 97.5** | 🟢 97.5 | 25.0% | 24.2% | 25.7% | 25.0% | - | 25.1% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟡 ** 88.6** | 🟡 88.6 | 25.0% | 28.0% | 23.6% | - | 23.4% | 24.9% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🟢 ** 95.8** | 🟢 95.8 | 25.0% | - | 25.3% | 24.7% | 23.9% | 26.1% | 🟢 ZBALANSOWANY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.85 🟢 | 0.0% 🟢 | 5.2% 🟢 | 1.68 🟢 | 7.76 🟢 | 8.23zł | 7.97 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.5 🟢 | 0.0% 🟢 | 6.0% 🟢 | 1.54 🟢 | 7.5 🟢 | 4.91zł | 8.44 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.78 🟢 | 0.0% 🟢 | 5.5% 🟢 | 1.64 🟢 | 8.0 🟢 | 10.74zł | 8.43 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.44 🟢 | 0.0% 🟢 | 1.7% 🟢 | 1.55 🟢 | 7.75 🟢 | 10.21zł | 8.42 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.9 🟢 | 0.0% 🟢 | 4.9% 🟢 | 1.08 🟢 | 6.79 🟢 | 9.32zł | 7.63 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |