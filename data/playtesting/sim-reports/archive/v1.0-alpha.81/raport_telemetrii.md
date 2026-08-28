# Raport Telemetrii i Szans Wygranych (Win Shares) dla Kanonu 4P — Wersja Balansu: v1.0-alpha.81

**Wersja Balansu:** `v1.0-alpha.81` | **Data:** 2026-08-28 15:20 | **Wielkość Próby:** 10000 gier/setup (50000 gier łącznie) | **Czas Symulacji:** 1.02s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🔴 **  6.3** | 🔴 8.3 | 25.0% | 57.6% | 25.3% | 2.9% | 14.1% | - | 🔴 ODCHYLONY |
| `4p-no-cienie` | 4 | 🔴 ** 16.5** | 🔴 16.5 | 25.0% | 43.1% | - | 0.8% | 22.3% | 33.8% | 🔴 ODCHYLONY |
| `4p-no-kabala` | 4 | 🔴 ** 20.8** | 🔴 20.8 | 25.0% | 35.0% | 28.1% | 1.1% | - | 35.9% | 🔴 ODCHYLONY |
| `4p-no-korona` | 4 | 🔴 ** 48.2** | 🔴 48.2 | 25.0% | 36.8% | 24.4% | - | 15.4% | 23.3% | 🔴 ODCHYLONY |
| `4p-no-oficjum` | 4 | 🔴 **  9.3** | 🔴 11.4 | 25.0% | - | 35.1% | 2.1% | 13.5% | 49.3% | 🔴 ODCHYLONY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 6.51 🟡 | 0.0% 🟢 | 5.5% 🟢 | 1.85 🟡 | 9.81 🟡 | 7.81zł | 8.53 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-cienie` | 5.87 🟢 | 0.0% 🟢 | 6.3% 🟢 | 1.64 🟢 | 8.46 🟢 | 4.61zł | 8.63 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.19 🟢 | 0.0% 🟢 | 5.3% 🟢 | 1.67 🟢 | 9.16 🟡 | 10.34zł | 8.75 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.55 🟢 | 0.0% 🟢 | 1.3% 🟢 | 1.58 🟢 | 7.82 🟢 | 9.69zł | 8.46 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 6.51 🟡 | 0.0% 🟢 | 5.1% 🟢 | 1.22 🟢 | 8.84 🟡 | 9.94zł | 8.0 | ⚠️ WARTOŚCI BRZEGOWE |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | ⚠️ Ostrzeżenie Witalności | 0.284 | Ekstremalny Deadlock (Era 11+): 1.4% gier (>0.5%) |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | ⚠️ Ostrzeżenie Witalności | 0.198 | Ekstremalny Deadlock (Era 11+): 1.0% gier (>0.5%) |