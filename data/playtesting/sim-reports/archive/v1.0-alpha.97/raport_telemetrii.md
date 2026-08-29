# Raport Telemetrii i Szans Wygranych (Win Shares) dla Kanonu 4P — Wersja Balansu: v1.0-alpha.97

**Wersja Balansu:** `v1.0-alpha.97` | **Data:** 2026-08-29 21:06 | **Wielkość Próby:** 10000 gier/setup (50000 gier łącznie) | **Czas Symulacji:** 0.17s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟢 ** 92.9** | 🟢 92.9 | 25.0% | 25.1% | 23.7% | 26.9% | 24.3% | - | 🟢 ZBALANSOWANY |
| `4p-no-cienie` | 4 | 🟡 ** 87.6** | 🟡 87.6 | 25.0% | 25.1% | - | 22.3% | 27.8% | 24.8% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟢 ** 97.4** | 🟢 97.4 | 25.0% | 24.4% | 24.6% | 25.7% | - | 25.3% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟢 ** 97.0** | 🟢 97.0 | 25.0% | 25.8% | 24.5% | - | 25.3% | 24.3% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟢 ** 98.1** | 🟢 98.1 | 25.0% | - | 25.5% | 24.4% | 25.2% | 24.9% | 🟢 ZBALANSOWANY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.92 🟢 | 0.0% 🟢 | 5.6% 🟢 | 1.74 🟢 | 7.81 🟢 | 7.99zł | 8.0 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.59 🟢 | 0.0% 🟢 | 6.3% 🟢 | 1.57 🟢 | 7.73 🟢 | 5.28zł | 8.48 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.78 🟢 | 0.0% 🟢 | 5.5% 🟢 | 1.65 🟢 | 8.03 🟢 | 11.07zł | 8.51 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.52 🟢 | 0.0% 🟢 | 1.9% 🟢 | 1.59 🟢 | 7.84 🟢 | 10.77zł | 8.38 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.97 🟢 | 0.0% 🟢 | 5.2% 🟢 | 1.1 🟢 | 6.65 🟢 | 9.81zł | 7.54 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |