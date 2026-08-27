# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.20

**Wersja Balansu:** `v0.20` | **Data:** 2026-08-14 14:09 | **Przeanalizowano Wariantów:** 28 | **Próba:** 3000 gier/setup | **Czas:** 170.07s
**Wynik Bazy Poziomu 2 (Global):** `🟢 91.0 pkt` | 3p: `80.8 pkt` | 4p: `93.3 pkt` | 5p: `99.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (5)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🟢 ** 91.0** | 80.8 | 93.3 | 99.0 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–7 → 4–7 | 🟢 ** 91.0** | 80.8 → 80.6 (`-0.2`) | 93.3 → 92.8 (`-0.5`) | 99.0 → 99.6 (`⬆️ +0.6`) | ⚪ OPTYMALNY |
| `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–7 → 2–7 | 91.0 → 🟢 ** 90.1** (`-0.9`) | 80.8 → 80.9 (`⬆️ +0.1`) | 93.3 → 91.0 (`-2.3`) | 99.0 → 98.3 (`-0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 3–7 → 3–6 | 91.0 → 🟢 ** 89.4** (`-1.6`) | 80.8 → 75.7 (`-5.1`) | 93.3 → 92.9 (`-0.4`) | 99.0 → 99.7 (`⬆️ +0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_PLUS1` | Korona Era: 5 → 6 | 91.0 → 🟢 ** 85.2** (`-5.8`) | 80.8 → 85.9 (`⬆️ +5.1`) | 93.3 → 87.1 (`-6.2`) | 99.0 → 82.5 (`-16.5`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 23 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_MINUS1` | Cienie Era: 5 → 4 | 🟢 ** 91.0** | 80.8 → 80.7 (`-0.1`) | 93.3 | 99.0 | ⚪ OPTYMALNY |
| `L2_CAA_ERA_PLUS1` | Cienie Era: 5 → 6 | 91.0 → 🟢 ** 90.7** (`-0.3`) | 80.8 → 80.7 (`-0.1`) | 93.3 → 92.5 (`-0.8`) | 99.0 → 98.9 (`-0.1`) | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–7 → 3–8 | 91.0 → 🟢 ** 89.1** (`-1.9`) | 80.8 → 79.6 (`-1.2`) | 93.3 → 89.6 (`-3.7`) | 99.0 → 98.1 (`-0.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2 → 3 | 91.0 → 🟢 ** 87.7** (`-3.3`) | 80.8 → 80.2 (`-0.6`) | 93.3 → 84.7 (`-8.6`) | 99.0 → 98.3 (`-0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 3 → 2 | 91.0 → 🟢 ** 81.6** (`-9.4`) | 80.8 → 72.0 (`-8.8`) | 93.3 → 73.9 (`-19.4`) | 99.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 91.0 → 🟢 ** 80.9** (`-10.1`) | 80.8 | 93.3 → 85.0 (`-8.3`) | 99.0 → 77.0 (`-22.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 3 → 4 | 91.0 → 🟢 ** 77.2** (`-13.8`) | 80.8 → 58.6 (`-22.2`) | 93.3 → 73.9 (`-19.4`) | 99.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 91.0 → 🟢 ** 76.7** (`-14.3`) | 80.8 → 77.1 (`-3.7`) | 93.3 → 72.9 (`-20.4`) | 99.0 → 80.2 (`-18.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_MINUS1` | Korona Era: 5 → 4 | 91.0 → 🟢 ** 73.7** (`-17.3`) | 80.8 → 61.0 (`-19.8`) | 93.3 → 62.2 (`-31.1`) | 99.0 → 98.0 (`-1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 0 → 1 | 91.0 → 🟢 ** 57.8** (`-33.2`) | 80.8 → 78.3 (`-2.5`) | 93.3 → 37.2 (`-56.1`) | 99.0 → 0.0 (`-99.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 7/6/6 → 6/5/5 | 91.0 → 🟢 ** 57.2** (`-33.8`) | 80.8 → 55.0 (`-25.8`) | 93.3 → 59.5 (`-33.8`) | 99.0 → 0.0 (`-99.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 7/6/6 → 8/7/7 | 91.0 → 🟢 ** 55.3** (`-35.7`) | 80.8 → 53.3 (`-27.5`) | 93.3 → 42.2 (`-51.1`) | 99.0 → 70.5 (`-28.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 3/4/4 → 4/5/5 | 91.0 → 🟡 ** 48.9** (`-42.1`) | 80.8 → 47.1 (`-33.7`) | 93.3 → 42.5 (`-50.8`) | 99.0 → 57.2 (`-41.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 3/4/4 → 2/3/3 | 91.0 → 🟡 ** 45.6** (`-45.4`) | 80.8 → 42.7 (`-38.1`) | 93.3 → 48.5 (`-44.8`) | 99.0 → 0.0 (`-99.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 2 → 3 | 91.0 → 🟡 ** 44.8** (`-46.2`) | 80.8 → 53.1 (`-27.7`) | 93.3 → 36.4 (`-56.9`) | 99.0 → 0.0 (`-99.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 2 → 1 | 91.0 → 🟡 ** 44.8** (`-46.2`) | 80.8 → 53.1 (`-27.7`) | 93.3 → 36.4 (`-56.9`) | 99.0 → 0.0 (`-99.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 2/3 → 1/2 | 91.0 → 🟡 ** 30.6** (`-60.4`) | 80.8 → 44.3 (`-36.5`) | 93.3 → 16.9 (`-76.4`) | 99.0 → 0.0 (`-99.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 91.0 → 🟡 ** 26.2** (`-64.8`) | 80.8 → 32.7 (`-48.1`) | 93.3 → 19.7 (`-73.6`) | 99.0 → 0.0 (`-99.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 91.0 → 🟡 ** 26.2** (`-64.8`) | 80.8 → 32.7 (`-48.1`) | 93.3 → 19.7 (`-73.6`) | 99.0 → 0.0 (`-99.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 91.0 → 🟡 ** 26.0** (`-65.0`) | 80.8 → 34.9 (`-45.9`) | 93.3 → 17.2 (`-76.1`) | 99.0 → 0.0 (`-99.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 91.0 → 🟡 ** 26.0** (`-65.0`) | 80.8 → 34.9 (`-45.9`) | 93.3 → 17.2 (`-76.1`) | 99.0 → 0.0 (`-99.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2 → 1 | 91.0 → 🔴 ** 24.3** (`-66.7`) | 80.8 → 29.2 (`-51.6`) | 93.3 → 19.4 (`-73.9`) | 99.0 → 0.0 (`-99.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 2/3 → 3/4 | 91.0 → 🔴 ** 23.9** (`-67.1`) | 80.8 → 30.9 (`-49.9`) | 93.3 → 16.9 (`-76.4`) | 99.0 → 0.0 (`-99.0`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (5)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 5.52 Er (1–9) | 4.1% | 28.5% | 1.03 (0–4) | 3.46 (0–18) | 0.55zł (0.0–3.0) | 6.05 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_PLUS1` | 5.54 Er (1–9) | 4.2% | 28.5% | 1.03 (0–4) | 3.48 (0–18) | 0.55zł (0.0–3.0) | 6.06 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_MINUS1` | 5.52 Er (1–9) | 4.1% | 28.5% | 1.03 (0–4) | 3.45 (0–18) | 0.55zł (0.0–3.0) | 6.04 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 5.56 Er (1–9) | 5.4% | 28.6% | 1.04 (0–4) | 3.53 (0–18) | 0.56zł (0.0–3.0) | 6.07 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_PLUS1` | 5.65 Er (1–9) | 4.1% | 29.0% | 1.05 (0–4) | 3.63 (0–18) | 0.57zł (0.0–3.0) | 6.12 (0.7–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 23 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_MINUS1` | 5.51 Er (1–9) | 4.1% | 28.4% | 1.03 (0–4) | 3.45 (0–18) | 0.55zł (0.0–3.0) | 6.04 (0.7–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_PLUS1` | 5.53 Er (1–9) | 4.1% | 28.5% | 1.03 (0–4) | 3.47 (0–18) | 0.55zł (0.0–3.0) | 6.05 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 5.49 Er (1–9) | 3.2% | 28.4% | 1.03 (0–4) | 3.41 (0–18) | 0.55zł (0.0–3.0) | 6.04 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 5.54 Er (1–9) | 4.4% | 28.6% | 1.03 (0–4) | 3.48 (0–18) | 0.55zł (0.0–3.0) | 6.06 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 5.39 Er (1–9) | 3.4% | 28.1% | 1.01 (0–4) | 3.30 (0–18) | 0.55zł (0.0–3.0) | 5.96 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.49 Er (1–9) | 3.8% | 28.4% | 1.03 (0–4) | 3.41 (0–18) | 0.55zł (0.0–3.0) | 6.03 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 5.59 Er (1–9) | 4.7% | 28.7% | 1.04 (0–4) | 3.54 (0–21) | 0.55zł (0.0–3.0) | 6.08 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 5.59 Er (1–9) | 5.2% | 28.7% | 1.04 (0–4) | 3.57 (0–18) | 0.56zł (0.0–3.0) | 6.10 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_MINUS1` | 5.40 Er (1–9) | 4.1% | 28.0% | 1.01 (0–4) | 3.31 (0–18) | 0.55zł (0.0–3.0) | 5.97 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 5.63 Er (1–9) | 4.5% | 28.9% | 1.05 (0–4) | 3.62 (0–18) | 0.56zł (0.0–3.0) | 6.11 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.33 Er (1–9) | 3.5% | 27.8% | 1.00 (0–4) | 3.20 (0–18) | 0.57zł (0.0–3.0) | 5.90 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 5.66 Er (1–9) | 5.4% | 29.0% | 1.05 (0–4) | 3.67 (0–18) | 0.58zł (0.0–3.0) | 6.14 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 5.61 Er (1–9) | 4.8% | 28.7% | 1.04 (0–4) | 3.57 (0–18) | 0.56zł (0.0–3.0) | 6.09 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.35 Er (1–9) | 3.3% | 27.9% | 1.01 (0–4) | 3.24 (0–18) | 0.55zł (0.0–3.0) | 5.95 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 5.67 Er (1–9) | 4.7% | 28.9% | 1.05 (0–4) | 3.61 (0–18) | 0.55zł (0.0–3.0) | 6.14 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 5.03 Er (1–9) | 3.2% | 27.3% | 0.95 (0–4) | 3.01 (0–18) | 0.59zł (0.0–3.0) | 5.64 (0.4–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 4.90 Er (1–9) | 2.6% | 26.9% | 0.93 (0–4) | 2.86 (0–18) | 0.59zł (0.0–3.0) | 5.56 (0.4–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_PLUS1` | 5.86 Er (1–9) | 6.3% | 29.4% | 1.08 (0–4) | 3.83 (0–18) | 0.55zł (0.0–3.0) | 6.29 (1.8–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.01 Er (1–9) | 1.7% | 23.7% | 0.81 (0–4) | 2.12 (0–16) | 0.73zł (0.0–4.0) | 4.75 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_KB_DECREES_PLUS1` | 5.81 Er (1–9) | 6.5% | 29.5% | 1.08 (0–4) | 3.89 (0–19) | 0.58zł (0.0–3.0) | 6.21 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.06 Er (1–9) | 1.7% | 26.5% | 0.96 (0–4) | 2.79 (0–17) | 0.53zł (0.0–3.0) | 5.71 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 4.75 Er (1–9) | 2.2% | 25.7% | 0.91 (0–4) | 2.75 (0–18) | 0.57zł (0.0–3.0) | 5.52 (0.7–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_GC_FALLS_PLUS1` | 5.73 Er (1–9) | 5.3% | 29.1% | 1.06 (0–4) | 3.70 (0–21) | 0.55zł (0.0–3.0) | 6.18 (0.7–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.