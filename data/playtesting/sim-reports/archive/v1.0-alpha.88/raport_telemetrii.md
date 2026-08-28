# Raport Telemetrii i Szans Wygranych (Win Shares) dla Kanonu 4P — Wersja Balansu: v1.0-alpha.88

**Wersja Balansu:** `v1.0-alpha.88` | **Data:** 2026-08-29 01:53 | **Wielkość Próby:** 10000 gier/setup (50000 gier łącznie) | **Czas Symulacji:** 0.18s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟡 ** 88.4** | 🟡 88.4 | 25.0% | 26.2% | 22.1% | 26.9% | 24.7% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟡 ** 80.8** | 🟡 80.8 | 25.0% | 26.3% | - | 21.7% | 29.0% | 22.9% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟢 ** 96.5** | 🟢 96.5 | 25.0% | 24.0% | 25.8% | 25.3% | - | 24.9% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟡 ** 86.1** | 🟡 86.1 | 25.0% | 28.7% | 23.6% | - | 23.4% | 24.3% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🟢 ** 94.7** | 🟢 94.7 | 25.0% | - | 26.2% | 25.0% | 23.5% | 25.2% | 🟢 ZBALANSOWANY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.85 🟢 | 0.0% 🟢 | 5.2% 🟢 | 1.68 🟢 | 7.76 🟢 | 8.23zł | 7.97 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.5 🟢 | 0.0% 🟢 | 6.0% 🟢 | 1.54 🟢 | 7.55 🟢 | 4.95zł | 8.46 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.78 🟢 | 0.0% 🟢 | 5.4% 🟢 | 1.63 🟢 | 8.03 🟢 | 10.78zł | 8.43 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.44 🟢 | 0.0% 🟢 | 1.7% 🟢 | 1.55 🟢 | 7.8 🟢 | 10.27zł | 8.43 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.92 🟢 | 0.0% 🟢 | 4.9% 🟢 | 1.09 🟢 | 6.92 🟢 | 9.41zł | 7.64 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |