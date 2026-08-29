# Raport Telemetrii i Szans Wygranych (Win Shares) dla Kanonu 4P — Wersja Balansu: v1.0-alpha.95

**Wersja Balansu:** `v1.0-alpha.95` | **Data:** 2026-08-29 16:09 | **Wielkość Próby:** 10000 gier/setup (50000 gier łącznie) | **Czas Symulacji:** 0.15s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟢 ** 93.5** | 🟢 93.5 | 25.0% | 25.3% | 23.5% | 26.6% | 24.5% | - | 🟢 ZBALANSOWANY |
| `4p-no-cienie` | 4 | 🟡 ** 88.0** | 🟡 88.0 | 25.0% | 25.0% | - | 22.5% | 27.9% | 24.6% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟢 ** 96.0** | 🟢 96.0 | 25.0% | 23.8% | 24.9% | 25.4% | - | 25.9% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟢 ** 96.8** | 🟢 96.8 | 25.0% | 25.8% | 24.3% | - | 25.4% | 24.5% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟢 ** 97.3** | 🟢 97.3 | 25.0% | - | 25.9% | 24.8% | 24.9% | 24.5% | 🟢 ZBALANSOWANY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.91 🟢 | 0.0% 🟢 | 5.6% 🟢 | 1.73 🟢 | 7.82 🟢 | 6.97zł | 8.0 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.59 🟢 | 0.0% 🟢 | 6.3% 🟢 | 1.57 🟢 | 7.73 🟢 | 5.06zł | 8.47 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.78 🟢 | 0.0% 🟢 | 5.5% 🟢 | 1.65 🟢 | 8.05 🟢 | 9.85zł | 8.5 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.53 🟢 | 0.0% 🟢 | 1.9% 🟢 | 1.59 🟢 | 7.86 🟢 | 9.61zł | 8.39 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.97 🟢 | 0.0% 🟢 | 5.3% 🟢 | 1.1 🟢 | 6.65 🟢 | 8.58zł | 7.53 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |