[Strona główna](../../../../../README.md) > [v1.0-alpha.23](README.md) > [raport_telemetrii_4p](raport_telemetrii_4p.md)

---

# Raport Telemetrii i Szans Wygranych (Win Shares) dla Wszystkich 16 Setupów — Wersja Balansu: v1.0-alpha.23

**Wersja Balansu:** `v1.0-alpha.23` | **Data:** 2026-08-22 15:05 | **Wielkość Próby:** 10000 gier/setup (160000 gier łącznie) | **Czas Symulacji:** 17.01s

## 1. Tabela Szans Wygranych Frakcji (Win Share %) vs Punkt Idealny

| Setup | Gr. | Score | Ideal % | SO % | CAA % | KB % | KT % | GC % | Status Rozkładu Frakcji |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 4 | 🟡 ** 80.2** | 25.0% | 24.4% | 25.9% | 20.7% | 28.9% | - | 🟡 AKCEPTOWALNY |
| `4p-no-cienie` | 4 | 🟡 ** 79.5** | 25.0% | 21.8% | - | 29.6% | 25.7% | 22.9% | 🟡 AKCEPTOWALNY |
| `4p-no-kabala` | 4 | 🟡 ** 87.3** | 25.0% | 27.9% | 22.6% | 23.9% | - | 25.6% | 🟡 AKCEPTOWALNY |
| `4p-no-korona` | 4 | 🟡 ** 79.5** | 25.0% | 20.6% | 25.6% | - | 29.1% | 24.7% | 🟡 AKCEPTOWALNY |
| `4p-no-oficjum` | 4 | 🟠 ** 74.7** | 25.0% | - | 20.0% | 25.3% | 30.3% | 24.4% | 🟠 WYMAGA UWAGI |

## 2. Pełna Tabela Telemetrii 5 Filarów Silnika Gry z Oceną Optymalności

| Setup | Średnia Er | Limit Er % (Deadlock) | Pas Biedy % (Złoto) | Autodafé / Partię | Oskarżenia / Partię | Śr. Złoto End | Śr. Herezja End | Globalny Status Telemetrii |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `4p-core` | 6.25 🟢 | 0.4% 🟢 | 1.7% 🟢 | 1.81 🟡 | 3.91 🟢 | 15.56zł | 6.25 | 🟢 OPTYMALNA |
| `4p-no-cienie` | 5.98 🟢 | 0.1% 🟢 | 1.5% 🟢 | 1.74 🟢 | 3.89 🟢 | 13.99zł | 7.22 | 🟢 OPTYMALNA |
| `4p-no-kabala` | 6.26 🟢 | 0.1% 🟢 | 1.6% 🟢 | 1.77 🟢 | 3.85 🟢 | 15.92zł | 6.6 | 🟢 OPTYMALNA |
| `4p-no-korona` | 6.16 🟢 | 0.0% 🟢 | 0.1% 🟢 | 1.76 🟢 | 4.6 🟡 | 17.87zł | 6.42 | 🟢 OPTYMALNA |
| `4p-no-oficjum` | 5.55 🟢 | 0.0% 🟢 | 2.5% 🟢 | 1.56 🟢 | 3.42 🟢 | 12.52zł | 7.39 | 🟢 OPTYMALNA |

## 3. Frakcje Wymagające Uwagi

| Frakcja | Śr. Win Share (wszystkie setupy) | Najgorszy Setup | Max Odchylenie od Ideału | Status |
| :--- | :---: | :--- | :---: | :--- |
| **KT** | 28.5% | `4p-no-oficjum` | +5.3% | 🟡 DOMINUJE |
| **CAA** | 23.5% | `4p-no-oficjum` | -5.0% | 🟢 OK |
| **KB** | 24.9% | `4p-no-cienie` | +4.6% | 🟢 OK |
| **SO** | 23.7% | `4p-no-korona` | -4.4% | 🟢 OK |
| **GC** | 24.4% | `4p-no-cienie` | -2.1% | 🟢 OK |

### Setupy poniżej Score 90 (wymagające poprawy):

| Setup | Score | Główny problem |
| :--- | :---: | :--- |
| `4p-no-oficjum` | 🟠 ** 74.7** | KT dominuje (30.3% vs ideal 25.0%) |
| `4p-no-cienie` | 🟡 ** 79.5** | KB dominuje (29.6% vs ideal 25.0%) |
| `4p-no-korona` | 🟡 ** 79.5** | SO za słaba (20.6% vs ideal 25.0%) |
| `4p-core` | 🟡 ** 80.2** | KB za słaba (20.7% vs ideal 25.0%) |
| `4p-no-kabala` | 🟡 ** 87.3** | SO dominuje (27.9% vs ideal 25.0%) |

## 4. Legenda Wskaźników Telemetrii i Norm Balansowych

- **🎯 Punkt Idealny (Ideal Share):** 33.3% w 3p | 25.0% w 4p | 20.0% w 5p
- **⏱️ Średnia Er (Tempo Gry):** 🟢 **5.0 – 6.5 Er** | 🟡 4.5–5.0 / 6.5–7.0 | 🔴 poza zakresem
- **🔒 Remisy po Limicie Er (Deadlock %):** 🟢 **< 5.0%** | 🟡 5–10% | 🔴 > 10%
- **💰 Pas Biedy (Poverty Rate %):** 🟢 **< 28.0%** | 🟡 28–32% | 🔴 > 32%
- **🔥 Autodafé / Partię:** 🟢 **0.7 – 1.8** | 🟡 0.5–0.7 / 1.8–2.0 | 🔴 poza zakresem
- **⚖️ Oskarżenia / Partię:** 🟢 **2.0 – 4.5** | 🟡 1.5–2.0 / 4.5–5.0 | 🔴 poza zakresem
- **📊 Status Setupu:** 🟢 Score ≥ 90 | 🟡 ≥ 75 | 🟠 ≥ 60 | 🔴 < 60