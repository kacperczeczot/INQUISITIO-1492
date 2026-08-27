[Strona główna](../../../../../README.md) > [v1.0-alpha.24](README.md) > [raport_telemetrii_4p](raport_telemetrii_4p.md)

---

# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.24

**Wersja Balansu:** `v1.0-alpha.24` | **Data:** 2026-08-22 18:03 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 16.12s

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟡 ** 89.9** | 25.0% | 22.8% | 25.3% | 24.5% | 27.4% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟠 ** 73.9** | 25.0% | 21.8% | - | 31.5% | 23.3% | 23.5% | 🟠 WYMAGA UWAGI |
| `4p-no-kabala` | 4 | 🟡 ** 88.4** | 25.0% | 27.5% | 23.4% | 26.0% | - | 23.1% | 🟡 AKCEPTOWALNY |
| `4p-no-korona` | 4 | 🟡 ** 82.1** | 25.0% | 21.1% | 25.7% | - | 28.6% | 24.7% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🟠 ** 73.5** | 25.0% | - | 19.7% | 29.6% | 27.6% | 23.1% | 🟠 WYMAGA UWAGI |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 6.15 🟢 | 0.4% 🟢 | 1.1% 🟢 | 1.77 🟢 | 3.82 🟢 | 16.08zł | 6.2 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.89 🟢 | 0.0% 🟢 | 1.0% 🟢 | 1.69 🟢 | 3.86 🟢 | 14.58zł | 7.14 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.15 🟢 | 0.0% 🟢 | 1.0% 🟢 | 1.73 🟢 | 3.74 🟢 | 16.41zł | 6.49 | 🟢 OPTYMALNA |
| `4p-no-korona` | 6.15 🟢 | 0.0% 🟢 | 0.0% 🟢 | 1.77 🟢 | 4.61 🟡 | 18.8zł | 6.42 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.5 🟢 | 0.0% 🟢 | 1.6% 🟢 | 1.54 🟢 | 3.41 🟢 | 13.15zł | 7.37 | 🟢 OPTYMALNA |

## 3. Frakcje Wymagające Uwagi

| Frakcja | Śr. Win Share (wszystkie setupy) | Najgorszy Setup | Max Odchylenie od Ideału | Status |
| :--- | :---: | :--- | :---: | :--- |
| **KB** | 27.9% | `4p-no-cienie` | +6.5% | 🟡 DOMINUJE |
| **CAA** | 23.5% | `4p-no-oficjum` | -5.3% | 🟡 SŁABA |
| **SO** | 23.3% | `4p-no-korona` | -3.9% | 🟢 OK |
| **KT** | 26.7% | `4p-no-korona` | +3.6% | 🟢 OK |
| **GC** | 23.6% | `4p-no-kabala` | -1.9% | 🟢 OK |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `4p-no-oficjum` | 🟠 ** 73.5** | CAA za słaba (19.7% vs ideal 25.0%) |
| `4p-no-cienie` | 🟠 ** 73.9** | KB dominuje (31.5% vs ideal 25.0%) |
| `4p-no-korona` | 🟡 ** 82.1** | SO za słaba (21.1% vs ideal 25.0%) |
| `4p-no-kabala` | 🟡 ** 88.4** | SO dominuje (27.5% vs ideal 25.0%) |
| `4p-core` | 🟡 ** 89.9** | KT dominuje (27.4% vs ideal 25.0%) |

## 4. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **2.0 – 4.5** | 🟡 1.5–2.0 / 4.5–5.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 75 | 🟠 ≥ 60 | 🔴 < 60