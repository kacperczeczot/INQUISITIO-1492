# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.19

**Wersja Balansu:** `v0.19` | **Data:** 2026-08-14 13:39 | **Przeanalizowano Wariantów:** 28 | **Próba:** 3000 gier/setup | **Czas:** 145.29s
**Wynik Bazy Poziomu 2 (Global):** `🟢 91.7 pkt` | 3p: `87.1 pkt` | 4p: `88.6 pkt` | 5p: `99.3 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (5)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🟢 ** 91.7** | 87.1 | 88.6 | 99.3 | ⚪ OPTYMALNY |
| `L2_CAA_ERA_MINUS1` | Cienie Era: 5 → 4 | 91.7 → 🟢 ** 91.8** (`⬆️ +0.1`) | 87.1 → 87.2 (`⬆️ +0.1`) | 88.6 → 88.7 (`⬆️ +0.1`) | 99.3 → 99.4 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–7 → 2–7 | 91.7 → 🟢 ** 91.6** (`-0.1`) | 87.1 → 87.2 (`⬆️ +0.1`) | 88.6 → 88.7 (`⬆️ +0.1`) | 99.3 → 98.8 (`-0.5`) | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 3–7 → 3–6 | 91.7 → 🟢 ** 86.6** (`-5.1`) | 87.1 → 78.4 (`-8.7`) | 88.6 → 81.9 (`-6.7`) | 99.3 → 99.6 (`⬆️ +0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_PLUS1` | Korona Era: 5 → 6 | 91.7 → 🟢 ** 84.1** (`-7.6`) | 87.1 → 90.9 (`⬆️ +3.8`) | 88.6 → 76.9 (`-11.7`) | 99.3 → 84.4 (`-14.9`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 23 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_PLUS1` | Cienie Era: 5 → 6 | 91.7 → 🟢 ** 89.9** (`-1.8`) | 87.1 → 86.7 (`-0.4`) | 88.6 → 84.0 (`-4.6`) | 99.3 → 99.1 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–7 → 3–8 | 91.7 → 🟢 ** 89.9** (`-1.8`) | 87.1 → 86.2 (`-0.9`) | 88.6 → 84.5 (`-4.1`) | 99.3 → 98.9 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–7 → 4–7 | 91.7 → 🟢 ** 88.9** (`-2.8`) | 87.1 → 85.3 (`-1.8`) | 88.6 → 82.2 (`-6.4`) | 99.3 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2 → 3 | 91.7 → 🟢 ** 84.8** (`-6.9`) | 87.1 → 85.8 (`-1.3`) | 88.6 → 69.9 (`-18.7`) | 99.3 → 98.6 (`-0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 91.7 → 🟢 ** 81.2** (`-10.5`) | 87.1 → 86.4 (`-0.7`) | 88.6 → 79.8 (`-8.8`) | 99.3 → 77.4 (`-21.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 3 → 4 | 91.7 → 🟢 ** 78.1** (`-13.6`) | 87.1 → 62.6 (`-24.5`) | 88.6 → 72.4 (`-16.2`) | 99.3 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 3 → 2 | 91.7 → 🟢 ** 78.1** (`-13.6`) | 87.1 → 62.6 (`-24.5`) | 88.6 → 72.4 (`-16.2`) | 99.3 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_MINUS1` | Korona Era: 5 → 4 | 91.7 → 🟢 ** 75.5** (`-16.2`) | 87.1 → 67.7 (`-19.4`) | 88.6 → 60.7 (`-27.9`) | 99.3 → 98.2 (`-1.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 91.7 → 🟢 ** 70.3** (`-21.4`) | 87.1 → 74.4 (`-12.7`) | 88.6 → 61.9 (`-26.7`) | 99.3 → 74.7 (`-24.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 0 → 1 | 91.7 → 🟢 ** 62.5** (`-29.2`) | 87.1 → 86.1 (`-1.0`) | 88.6 → 38.9 (`-49.7`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 7/6/6 → 6/5/5 | 91.7 → 🟢 ** 56.4** (`-35.3`) | 87.1 → 56.9 (`-30.2`) | 88.6 → 55.9 (`-32.7`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 3/4/4 → 4/5/5 | 91.7 → 🟢 ** 54.9** (`-36.8`) | 87.1 → 53.8 (`-33.3`) | 88.6 → 37.9 (`-50.7`) | 99.3 → 72.9 (`-26.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 7/6/6 → 8/7/7 | 91.7 → 🟡 ** 46.1** (`-45.6`) | 87.1 → 48.2 (`-38.9`) | 88.6 → 36.7 (`-51.9`) | 99.3 → 53.3 (`-46.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 2 → 3 | 91.7 → 🟡 ** 45.5** (`-46.2`) | 87.1 → 58.3 (`-28.8`) | 88.6 → 32.7 (`-55.9`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 2 → 1 | 91.7 → 🟡 ** 45.5** (`-46.2`) | 87.1 → 58.3 (`-28.8`) | 88.6 → 32.7 (`-55.9`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 3/4/4 → 2/3/3 | 91.7 → 🟡 ** 43.3** (`-48.4`) | 87.1 → 45.2 (`-41.9`) | 88.6 → 41.4 (`-47.2`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 91.7 → 🟡 ** 29.0** (`-62.7`) | 87.1 → 38.9 (`-48.2`) | 88.6 → 19.1 (`-69.5`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 91.7 → 🟡 ** 29.0** (`-62.7`) | 87.1 → 38.9 (`-48.2`) | 88.6 → 19.1 (`-69.5`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 91.7 → 🟡 ** 26.3** (`-65.4`) | 87.1 → 35.4 (`-51.7`) | 88.6 → 17.2 (`-71.4`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 91.7 → 🟡 ** 26.3** (`-65.4`) | 87.1 → 35.4 (`-51.7`) | 88.6 → 17.2 (`-71.4`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 2/3 → 3/4 | 91.7 → 🟡 ** 25.2** (`-66.5`) | 87.1 → 33.7 (`-53.4`) | 88.6 → 16.6 (`-72.0`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 2/3 → 1/2 | 91.7 → 🟡 ** 25.2** (`-66.5`) | 87.1 → 33.7 (`-53.4`) | 88.6 → 16.6 (`-72.0`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2 → 1 | 91.7 → 🔴 ** 24.3** (`-67.4`) | 87.1 → 32.4 (`-54.7`) | 88.6 → 16.2 (`-72.4`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (5)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 5.51 Er (1–9) | 4.1% | 28.3% | 1.02 (0–4) | 3.53 (0–20) | 0.52zł (0.0–3.0) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_MINUS1` | 5.50 Er (1–9) | 4.1% | 28.3% | 1.02 (0–4) | 3.52 (0–20) | 0.52zł (0.0–3.0) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_MINUS1` | 5.50 Er (1–9) | 4.1% | 28.3% | 1.02 (0–4) | 3.53 (0–20) | 0.52zł (0.0–3.0) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 5.55 Er (1–9) | 5.4% | 28.4% | 1.03 (0–4) | 3.60 (0–21) | 0.53zł (0.0–3.3) | 6.22 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_PLUS1` | 5.63 Er (1–9) | 4.1% | 28.7% | 1.04 (0–4) | 3.70 (0–20) | 0.52zł (0.0–3.0) | 6.28 (0.7–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 23 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_PLUS1` | 5.52 Er (1–9) | 4.1% | 28.3% | 1.03 (0–4) | 3.54 (0–20) | 0.52zł (0.0–3.0) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 5.48 Er (1–9) | 3.2% | 28.2% | 1.02 (0–4) | 3.49 (0–20) | 0.51zł (0.0–3.0) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_PLUS1` | 5.52 Er (1–9) | 4.2% | 28.4% | 1.03 (0–4) | 3.56 (0–20) | 0.52zł (0.0–3.0) | 6.21 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 5.53 Er (1–9) | 4.4% | 28.4% | 1.03 (0–4) | 3.55 (0–20) | 0.52zł (0.0–3.0) | 6.21 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.48 Er (1–9) | 3.8% | 28.2% | 1.02 (0–4) | 3.49 (0–18) | 0.52zł (0.0–3.0) | 6.18 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 5.58 Er (1–9) | 4.7% | 28.5% | 1.03 (0–4) | 3.63 (0–20) | 0.52zł (0.0–3.0) | 6.24 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 5.37 Er (1–9) | 3.4% | 27.9% | 1.00 (0–4) | 3.36 (0–20) | 0.51zł (0.0–3.0) | 6.10 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_MINUS1` | 5.39 Er (1–9) | 4.1% | 27.9% | 1.01 (0–4) | 3.39 (0–20) | 0.51zł (0.0–3.0) | 6.12 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 5.57 Er (1–9) | 5.2% | 28.5% | 1.03 (0–4) | 3.64 (0–20) | 0.52zł (0.0–3.0) | 6.24 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 5.60 Er (1–9) | 4.4% | 28.7% | 1.04 (0–4) | 3.69 (0–20) | 0.53zł (0.0–3.0) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.32 Er (1–9) | 3.5% | 27.6% | 1.00 (0–4) | 3.27 (0–20) | 0.51zł (0.0–3.0) | 6.05 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 5.59 Er (1–9) | 4.8% | 28.6% | 1.04 (0–4) | 3.64 (0–20) | 0.52zł (0.0–3.0) | 6.24 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 5.65 Er (1–9) | 5.3% | 28.8% | 1.05 (0–4) | 3.75 (0–21) | 0.55zł (0.0–3.0) | 6.29 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 5.66 Er (2–9) | 4.6% | 28.7% | 1.05 (0–4) | 3.71 (0–20) | 0.52zł (0.0–3.0) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 5.01 Er (1–9) | 3.3% | 27.1% | 0.94 (0–4) | 3.07 (0–20) | 0.55zł (0.0–3.0) | 5.77 (0.4–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.33 Er (1–9) | 3.2% | 27.7% | 1.00 (0–4) | 3.31 (0–20) | 0.51zł (0.0–3.0) | 6.10 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 5.79 Er (1–9) | 6.4% | 29.2% | 1.07 (0–4) | 3.96 (0–20) | 0.55zł (0.0–3.0) | 6.36 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.04 Er (1–9) | 1.6% | 26.6% | 0.95 (0–4) | 2.87 (0–20) | 0.49zł (0.0–3.0) | 5.86 (0.7–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 5.81 Er (1–9) | 6.0% | 29.1% | 1.07 (0–4) | 3.88 (0–20) | 0.52zł (0.0–2.8) | 6.43 (1.8–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 3.98 Er (1–9) | 1.6% | 23.7% | 0.80 (0–4) | 2.16 (0–18) | 0.68zł (0.0–4.0) | 4.87 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_GC_FALLS_PLUS1` | 5.73 Er (2–9) | 5.3% | 28.9% | 1.06 (0–4) | 3.80 (0–20) | 0.53zł (0.0–3.0) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 4.88 Er (1–9) | 2.6% | 26.7% | 0.92 (0–4) | 2.90 (0–20) | 0.55zł (0.0–3.0) | 5.67 (0.4–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_SO_CONDEMNS_MINUS1` | 4.70 Er (1–9) | 2.2% | 25.4% | 0.90 (0–4) | 2.79 (0–20) | 0.52zł (0.0–3.0) | 5.64 (0.7–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.