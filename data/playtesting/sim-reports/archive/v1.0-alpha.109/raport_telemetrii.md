# Raport Telemetrii i Szans Wygranych (Win Shares) dla Kanonu 4P — Wersja Balansu: v1.0-alpha.109

**Wersja Balansu:** `v1.0-alpha.109` | **Data:** 2026-08-30 02:49 | **Wielkość Próby:** 10000 gier/setup (50000 gier łącznie) | **Czas Symulacji:** 0.16s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟢 ** 90.7** | 🟢 90.7 | 25.0% | 25.6% | 23.6% | 27.2% | 23.6% | - | 🟢 ZBALANSOWANY |
| `4p-no-cienie` | 4 | 🟡 ** 86.3** | 🟡 86.3 | 25.0% | 24.5% | - | 21.9% | 27.8% | 25.8% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟢 ** 95.7** | 🟢 95.7 | 25.0% | 24.6% | 24.1% | 25.1% | - | 26.3% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟢 ** 97.0** | 🟢 97.0 | 25.0% | 25.3% | 24.8% | - | 24.2% | 25.8% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟢 ** 94.0** | 🟢 94.0 | 25.0% | - | 26.5% | 23.8% | 25.5% | 24.2% | 🟢 ZBALANSOWANY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 6.01 🟢 | 0.0% 🟢 | 4.5% 🟢 | 1.88 🟡 | 7.86 🟢 | 8.18zł | 8.02 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.65 🟢 | 0.0% 🟢 | 5.2% 🟢 | 1.7 🟢 | 7.86 🟢 | 5.76zł | 8.48 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.76 🟢 | 0.0% 🟢 | 4.4% 🟢 | 1.73 🟢 | 8.06 🟢 | 11.1zł | 8.53 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.56 🟢 | 0.0% 🟢 | 0.9% 🟢 | 1.72 🟢 | 7.86 🟢 | 10.89zł | 8.37 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 6.02 🟢 | 0.0% 🟢 | 5.1% 🟢 | 1.11 🟢 | 6.46 🟢 | 9.49zł | 7.43 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |