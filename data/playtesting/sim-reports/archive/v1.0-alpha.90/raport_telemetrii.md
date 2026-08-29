# Raport Telemetrii i Szans Wygranych (Win Shares) dla Kanonu 4P — Wersja Balansu: v1.0-alpha.90

**Wersja Balansu:** `v1.0-alpha.90` | **Data:** 2026-08-29 01:57 | **Wielkość Próby:** 10000 gier/setup (50000 gier łącznie) | **Czas Symulacji:** 0.14s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟡 ** 85.0** | 🟡 85.0 | 25.0% | 25.1% | 21.5% | 27.9% | 25.6% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟡 ** 84.3** | 🟡 84.3 | 25.0% | 24.6% | - | 22.2% | 28.8% | 24.3% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟢 ** 97.5** | 🟢 97.5 | 25.0% | 24.2% | 25.7% | 25.0% | - | 25.1% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟢 ** 94.1** | 🟢 94.1 | 25.0% | 26.8% | 24.2% | - | 24.4% | 24.6% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟢 ** 98.9** | 🟢 98.9 | 25.0% | - | 25.2% | 24.8% | 25.3% | 24.7% | 🟢 ZBALANSOWANY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.91 🟢 | 0.0% 🟢 | 5.4% 🟢 | 1.71 🟢 | 7.71 🟢 | 8.16zł | 7.93 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.62 🟢 | 0.0% 🟢 | 6.3% 🟢 | 1.57 🟢 | 7.69 🟢 | 4.9zł | 8.41 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.78 🟢 | 0.0% 🟢 | 5.5% 🟢 | 1.64 🟢 | 8.0 🟢 | 10.74zł | 8.43 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.52 🟢 | 0.0% 🟢 | 1.9% 🟢 | 1.59 🟢 | 7.8 🟢 | 10.21zł | 8.35 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.96 🟢 | 0.0% 🟢 | 5.2% 🟢 | 1.1 🟢 | 6.7 🟢 | 9.29zł | 7.55 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |