# Raport Telemetrii i Szans Wygranych (Win Shares) dla Kanonu 4P — Wersja Balansu: v1.0-alpha.93

**Wersja Balansu:** `v1.0-alpha.93` | **Data:** 2026-08-29 11:19 | **Wielkość Próby:** 10000 gier/setup (50000 gier łącznie) | **Czas Symulacji:** 0.16s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟢 ** 92.6** | 🟢 92.6 | 25.0% | 24.9% | 23.8% | 27.1% | 24.3% | - | 🟢 ZBALANSOWANY |
| `4p-no-cienie` | 4 | 🟡 ** 86.9** | 🟡 86.9 | 25.0% | 25.2% | - | 22.4% | 28.1% | 24.3% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟢 ** 97.0** | 🟢 97.0 | 25.0% | 24.1% | 25.0% | 25.7% | - | 25.2% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟢 ** 96.4** | 🟢 96.4 | 25.0% | 26.0% | 24.5% | - | 25.2% | 24.2% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟢 ** 97.2** | 🟢 97.2 | 25.0% | - | 25.8% | 24.2% | 25.1% | 24.8% | 🟢 ZBALANSOWANY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.91 🟢 | 0.0% 🟢 | 5.6% 🟢 | 1.74 🟢 | 7.79 🟢 | 7.3zł | 7.99 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.59 🟢 | 0.0% 🟢 | 6.3% 🟢 | 1.57 🟢 | 7.7 🟢 | 4.6zł | 8.47 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.79 🟢 | 0.0% 🟢 | 5.5% 🟢 | 1.65 🟢 | 8.05 🟢 | 9.76zł | 8.5 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.53 🟢 | 0.0% 🟢 | 1.9% 🟢 | 1.59 🟢 | 7.84 🟢 | 9.47zł | 8.39 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.97 🟢 | 0.0% 🟢 | 5.3% 🟢 | 1.1 🟢 | 6.66 🟢 | 8.43zł | 7.55 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |