[Strona główna](../../../../../README.md) > [v1.0-alpha.8](README.md) > [raport_telemetrii_4p](raport_telemetrii_4p.md)

---

# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.8

**Wersja Balansu:** `v1.0-alpha.8` | **Data:** 2026-08-19 11:51 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 32.04s

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟠 ** 69.1** | 25.0% | 31.9% | 24.3% | 19.5% | 24.3% | - | 🟠 WYMAGA UWAGI |
| `4p-no-cienie` | 4 | 🟡 ** 83.8** | 25.0% | 23.5% | - | 25.7% | 28.7% | 22.1% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟠 ** 60.0** | 25.0% | 26.6% | 15.3% | 27.8% | - | 30.3% | 🟠 WYMAGA UWAGI |
| `4p-no-korona` | 4 | 🟡 ** 88.1** | 25.0% | 22.0% | 27.1% | - | 25.0% | 25.9% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🟠 ** 74.4** | 25.0% | - | 19.9% | 28.9% | 23.0% | 28.1% | 🟠 WYMAGA UWAGI |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 6.58 🟡 | 0.8% 🟢 | 1.8% 🟢 | 2.48 🔴 | 4.69 🟡 | 17.19zł | 6.69 | ⚠️ WARTOŚCI BRZEGOWE |
| `4p-no-cienie` | 5.96 🟢 | 0.0% 🟢 | 2.2% 🟢 | 2.29 🔴 | 4.13 🟢 | 13.94zł | 7.68 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.47 🟢 | 0.3% 🟢 | 1.6% 🟢 | 2.32 🔴 | 3.55 🟢 | 17.81zł | 6.61 | 🟢 OPTYMALNA |
| `4p-no-korona` | 6.43 🟢 | 0.1% 🟢 | 0.1% 🟢 | 2.44 🔴 | 4.83 🟡 | 19.5zł | 6.5 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.6 🟢 | 0.0% 🟢 | 2.2% 🟢 | 1.56 🟢 | 3.56 🟢 | 13.56zł | 7.46 | 🟢 OPTYMALNA |

## 3. Frakcje Wymagające Uwagi

| Frakcja | Śr. Win Share (wszystkie setupy) | Najgorszy Setup | Max Odchylenie od Ideału | Status |
| :--- | :---: | :--- | :---: | :--- |
| **CAA** | 21.6% | `4p-no-kabala` | -9.7% | 🟡 SŁABA |
| **SO** | 26.0% | `4p-core` | +6.9% | 🟡 DOMINUJE |
| **KB** | 25.5% | `4p-core` | -5.5% | 🟡 SŁABA |
| **GC** | 26.6% | `4p-no-kabala` | +5.3% | 🟡 DOMINUJE |
| **KT** | 25.2% | `4p-no-cienie` | +3.7% | 🟢 OK |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `4p-no-kabala` | 🟠 ** 60.0** | CAA za słaba (15.3% vs ideal 25.0%) |
| `4p-core` | 🟠 ** 69.1** | SO dominuje (31.9% vs ideal 25.0%) |
| `4p-no-oficjum` | 🟠 ** 74.4** | CAA za słaba (19.9% vs ideal 25.0%) |
| `4p-no-cienie` | 🟡 ** 83.8** | KT dominuje (28.7% vs ideal 25.0%) |
| `4p-no-korona` | 🟡 ** 88.1** | SO za słaba (22.0% vs ideal 25.0%) |

## 4. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **2.0 – 4.5** | 🟡 1.5–2.0 / 4.5–5.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 75 | 🟠 ≥ 60 | 🔴 < 60