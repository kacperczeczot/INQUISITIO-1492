# Raport Telemetrii i Szans Wygranych (Win Shares) dla Kanonu 4P — Wersja Balansu: v1.0-alpha.96

**Wersja Balansu:** `v1.0-alpha.96` | **Data:** 2026-08-29 16:42 | **Wielkość Próby:** 10000 gier/setup (50000 gier łącznie) | **Czas Symulacji:** 0.14s

*Score* = legacy (win share + kara witalności w jednym wykładniku). *Balance* = tylko równość win share.

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Balance | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟢 ** 93.7** | 🟢 93.7 | 25.0% | 25.3% | 23.5% | 26.6% | 24.5% | - | 🟢 ZBALANSOWANY |
| `4p-no-cienie` | 4 | 🟡 ** 88.3** | 🟡 88.3 | 25.0% | 24.8% | - | 22.6% | 27.9% | 24.7% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟢 ** 96.7** | 🟢 96.7 | 25.0% | 24.1% | 24.6% | 25.6% | - | 25.6% | 🟢 ZBALANSOWANY |
| `4p-no-korona` | 4 | 🟢 ** 96.3** | 🟢 96.3 | 25.0% | 25.9% | 24.4% | - | 25.5% | 24.2% | 🟢 ZBALANSOWANY |
| `4p-no-oficjum` | 4 | 🟢 ** 98.3** | 🟢 98.3 | 25.0% | - | 25.6% | 24.8% | 24.9% | 24.7% | 🟢 ZBALANSOWANY |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 5.91 🟢 | 0.0% 🟢 | 5.6% 🟢 | 1.73 🟢 | 7.82 🟢 | 7.96zł | 8.0 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.59 🟢 | 0.0% 🟢 | 6.3% 🟢 | 1.57 🟢 | 7.73 🟢 | 5.29zł | 8.47 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 5.78 🟢 | 0.0% 🟢 | 5.5% 🟢 | 1.65 🟢 | 8.04 🟢 | 11.04zł | 8.5 | 🟢 OPTYMALNA |
| `4p-no-korona` | 5.52 🟢 | 0.0% 🟢 | 1.9% 🟢 | 1.59 🟢 | 7.84 🟢 | 10.76zł | 8.38 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.97 🟢 | 0.0% 🟢 | 5.3% 🟢 | 1.1 🟢 | 6.64 🟢 | 9.81zł | 7.53 | 🟢 OPTYMALNA |

## 3. Witalność Mechanik Frakcji (Mechanic Vitality & Degeneration Gate)

| Setup | Status Witalności | Kara | Zidentyfikowane Ostrzeżenia / Degradacje Mechanik |
| :--- | :---: | :---: | :--- |
| `4p-core` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-cienie` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-kabala` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-korona` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |
| `4p-no-oficjum` | 🟢 Pełna Witalność | 0.000 | Brak — wszystkie mechaniki aktywne i płynne |