# Raport Telemetrii i Szans Wygranych (Win Shares) dla Kanonu 4P — Wersja Balansu: v1.0-alpha.84

**Wersja Balansu:** `v1.0-alpha.84` | **Data:** 2026-08-29 01:44 | **Wielkość Próby:** 10000 gier/setup (50000 gier łącznie) | **Czas Symulacji:** 0.14s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟡 ** 81.3** | 🟡 81.3 | 25.0% | 28.2% | 20.7% | 26.6% | 24.5% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟠 ** 69.4** | 🟠 69.4 | 25.0% | 28.7% | - | 18.9% | 29.6% | 22.7% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🟢 ** 98.5** | 🟢 98.5 | 25.0% | 25.4% | 24.9% | 25.3% | - | 24.5% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟠 ** 76.1** | 🟠 76.1 | 25.0% | 30.8% | 22.9% | - | 24.4% | 21.8% | 🟠 WYMAGA UWAGI |
| `4p-no-oficjum` | 4 | 🟢 ** 93.2** | 🟢 93.2 | 25.0% | - | 26.4% | 24.7% | 23.3% | 25.6% | 🟢 ZBALANSOWANY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.88 🟢 | 0.0% 🟢 | 5.4% 🟢 | 1.7 🟢 | 7.78 🟢 | 7.58zł | 8.05 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.54 🟢 | 0.0% 🟢 | 6.3% 🟢 | 1.56 🟢 | 7.48 🟢 | 4.52zł | 8.47 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.86 🟢 | 0.0% 🟢 | 5.5% 🟢 | 1.64 🟢 | 8.1 🟢 | 10.29zł | 8.5 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.45 🟢 | 0.0% 🟢 | 1.5% 🟢 | 1.58 🟢 | 7.63 🟢 | 9.87zł | 8.45 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.94 🟢 | 0.0% 🟢 | 4.9% 🟢 | 1.09 🟢 | 6.93 🟢 | 9.42zł | 7.62 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |