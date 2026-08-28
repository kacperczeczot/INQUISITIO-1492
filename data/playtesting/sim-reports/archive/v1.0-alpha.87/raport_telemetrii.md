# Raport Telemetrii i Szans Wygranych (Win Shares) dla Kanonu 4P — Wersja Balansu: v1.0-alpha.87

**Wersja Balansu:** `v1.0-alpha.87` | **Data:** 2026-08-29 01:47 | **Wielkość Próby:** 10000 gier/setup (50000 gier łącznie) | **Czas Symulacji:** 0.15s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟢 ** 90.0** | 🟢 90.0 | 25.0% | 26.3% | 22.5% | 26.6% | 24.6% | - | 🟢 ZBALANSOWANY |
| `4p-no-cienie` | 4 | 🟠 ** 77.4** | 🟠 77.4 | 25.0% | 26.4% | - | 20.0% | 29.1% | 24.4% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🟢 ** 95.5** | 🟢 95.5 | 25.0% | 24.0% | 26.0% | 24.4% | - | 25.6% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟡 ** 86.1** | 🟡 86.1 | 25.0% | 28.7% | 23.6% | - | 23.4% | 24.3% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🟢 ** 93.2** | 🟢 93.2 | 25.0% | - | 26.4% | 24.7% | 23.3% | 25.6% | 🟢 ZBALANSOWANY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.89 🟢 | 0.0% 🟢 | 5.3% 🟢 | 1.7 🟢 | 7.82 🟢 | 8.27zł | 7.96 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.53 🟢 | 0.0% 🟢 | 6.1% 🟢 | 1.55 🟢 | 7.63 🟢 | 4.95zł | 8.45 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.83 🟢 | 0.0% 🟢 | 5.6% 🟢 | 1.65 🟢 | 8.09 🟢 | 10.84zł | 8.42 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.44 🟢 | 0.0% 🟢 | 1.7% 🟢 | 1.55 🟢 | 7.8 🟢 | 10.27zł | 8.43 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.94 🟢 | 0.0% 🟢 | 4.9% 🟢 | 1.09 🟢 | 6.93 🟢 | 9.42zł | 7.62 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |