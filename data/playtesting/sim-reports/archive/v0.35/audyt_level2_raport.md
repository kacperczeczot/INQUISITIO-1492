[Strona główna](../../../../../README.md) > [v0.35](README.md) > [audyt_level2_raport](audyt_level2_raport.md)

---

# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.35

**Wersja Balansu:** `v0.35` | **Data:** 2026-08-15 20:26 | **Przeanalizowano Wariantów:** 28 | **Próba:** 3000 gier/setup | **Czas:** 550.18s
**Wynik Bazy Poziomu 2 (Global):** `🟢 97.5 pkt` | 3p: `94.2 pkt` | 4p: `99.1 pkt` | 5p: `99.3 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (4)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🟢 ** 97.5** | 94.2 | 99.1 | 99.3 | ⚪ OPTYMALNY |
| `L2_CAA_ERA_PLUS1` | Cienie Era: 5 → 6 | 97.5 → 🟢 ** 97.0** (`-0.5`) | 94.2 → 93.9 (`-0.3`) | 99.1 → 97.5 (`-1.6`) | 99.3 → 99.5 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 97.5 → 🟢 ** 97.0** (`-0.5`) | 94.2 → 94.3 (`⬆️ +0.1`) | 99.1 → 97.8 (`-1.3`) | 99.3 → 99.0 (`-0.3`) | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 3–8 → 3–7 | 97.5 → 🟢 ** 96.8** (`-0.7`) | 94.2 → 91.8 (`-2.4`) | 99.1 → 99.2 (`⬆️ +0.1`) | 99.3 → 99.4 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 24 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_MINUS1` | Cienie Era: 5 → 4 | 🟢 ** 97.5** | 94.2 → 94.1 (`-0.1`) | 99.1 | 99.3 → 99.2 (`-0.1`) | ⚪ OPTYMALNY |
| `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 97.5 → 🟢 ** 97.3** (`-0.2`) | 94.2 → 94.1 (`-0.1`) | 99.1 → 99.0 (`-0.1`) | 99.3 → 98.9 (`-0.4`) | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–8 → 3–9 | 97.5 → 🟢 ** 96.8** (`-0.7`) | 94.2 → 92.3 (`-1.9`) | 99.1 → 99.0 (`-0.1`) | 99.3 → 99.1 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_MINUS1` | Korona Era: 6/5/5 → 5/4/4 | 97.5 → 🟡 ** 87.8** (`-9.7`) | 94.2 → 89.2 (`-5.0`) | 99.1 → 75.0 (`-24.1`) | 99.3 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2 → 3 | 97.5 → 🟡 ** 86.3** (`-11.2`) | 94.2 → 93.8 (`-0.4`) | 99.1 → 81.1 (`-18.0`) | 99.3 → 83.9 (`-15.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 97.5 → 🟡 ** 84.9** (`-12.6`) | 94.2 → 93.3 (`-0.9`) | 99.1 → 78.2 (`-20.9`) | 99.3 → 83.1 (`-16.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 3 → 4 | 97.5 → 🟡 ** 83.2** (`-14.3`) | 94.2 → 70.9 (`-23.3`) | 99.1 → 79.3 (`-19.8`) | 99.3 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 3 → 2 | 97.5 → 🟡 ** 81.0** (`-16.5`) | 94.2 → 64.3 (`-29.9`) | 99.1 → 79.3 (`-19.8`) | 99.3 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 97.5 → 🟠 ** 73.8** (`-23.7`) | 94.2 → 89.5 (`-4.7`) | 99.1 → 69.2 (`-29.9`) | 99.3 → 62.7 (`-36.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_PLUS1` | Korona Era: 6/5/5 → 7/6/6 | 97.5 → 🟠 ** 69.4** (`-28.1`) | 94.2 → 71.2 (`-23.0`) | 99.1 → 64.8 (`-34.3`) | 99.3 → 72.1 (`-27.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 3/4/4 → 4/5/5 | 97.5 → 🔴 ** 58.1** (`-39.4`) | 94.2 → 62.5 (`-31.7`) | 99.1 → 44.1 (`-55.0`) | 99.3 → 67.8 (`-31.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 0 → 1 | 97.5 → 🔴 ** 55.2** (`-42.3`) | 94.2 → 72.2 (`-22.0`) | 99.1 → 38.1 (`-61.0`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 7/6/6 → 8/7/7 | 97.5 → 🔴 ** 53.1** (`-44.4`) | 94.2 → 70.0 (`-24.2`) | 99.1 → 36.2 (`-62.9`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 2 → 3 | 97.5 → 🔴 ** 53.0** (`-44.5`) | 94.2 → 66.5 (`-27.7`) | 99.1 → 39.5 (`-59.6`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 2 → 1 | 97.5 → 🔴 ** 53.0** (`-44.5`) | 94.2 → 66.5 (`-27.7`) | 99.1 → 39.5 (`-59.6`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 7/6/6 → 6/5/5 | 97.5 → 🔴 ** 41.4** (`-56.1`) | 94.2 → 58.0 (`-36.2`) | 99.1 → 24.8 (`-74.3`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 3/4/4 → 2/3/3 | 97.5 → 🔴 ** 40.8** (`-56.7`) | 94.2 → 45.2 (`-49.0`) | 99.1 → 36.4 (`-62.7`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 2/3 → 3/4 | 97.5 → 🔴 ** 31.5** (`-66.0`) | 94.2 → 43.2 (`-51.0`) | 99.1 → 19.7 (`-79.4`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2 → 1 | 97.5 → 🔴 ** 29.8** (`-67.7`) | 94.2 → 39.8 (`-54.4`) | 99.1 → 19.8 (`-79.3`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 97.5 → 🔴 ** 28.8** (`-68.7`) | 94.2 → 37.6 (`-56.6`) | 99.1 → 19.9 (`-79.2`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 97.5 → 🔴 ** 28.8** (`-68.7`) | 94.2 → 37.6 (`-56.6`) | 99.1 → 19.9 (`-79.2`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 97.5 → 🔴 ** 28.6** (`-68.9`) | 94.2 → 37.5 (`-56.7`) | 99.1 → 19.8 (`-79.3`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 97.5 → 🔴 ** 28.6** (`-68.9`) | 94.2 → 37.5 (`-56.7`) | 99.1 → 19.8 (`-79.3`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 2/3 → 1/2 | 97.5 → 🔴 ** 28.1** (`-69.4`) | 94.2 → 36.6 (`-57.6`) | 99.1 → 19.7 (`-79.4`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (4)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 5.55 Er (1–10) | 1.3% | 26.2% | 1.04 (0–4) | 3.62 (0–18) | 1.21zł (0.0–5.0) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_PLUS1` | 5.56 Er (1–10) | 1.3% | 26.3% | 1.04 (0–4) | 3.63 (0–18) | 1.21zł (0.0–5.0) | 6.36 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_PLUS1` | 5.57 Er (1–10) | 1.3% | 26.3% | 1.04 (0–4) | 3.65 (0–18) | 1.22zł (0.0–5.7) | 6.36 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 5.58 Er (1–10) | 1.6% | 26.3% | 1.04 (0–4) | 3.67 (0–18) | 1.22zł (0.0–5.3) | 6.36 (0.7–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 24 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_MINUS1` | 5.54 Er (1–10) | 1.3% | 26.2% | 1.04 (0–4) | 3.61 (0–18) | 1.21zł (0.0–5.0) | 6.34 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_MINUS1` | 5.55 Er (1–10) | 1.3% | 26.2% | 1.04 (0–4) | 3.61 (0–18) | 1.21zł (0.0–5.0) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 5.54 Er (1–10) | 1.1% | 26.2% | 1.04 (0–4) | 3.60 (0–18) | 1.21zł (0.0–5.0) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_MINUS1` | 5.43 Er (1–10) | 1.3% | 25.7% | 1.02 (0–4) | 3.46 (0–18) | 1.20zł (0.0–5.0) | 6.27 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 5.59 Er (1–10) | 1.4% | 26.4% | 1.05 (0–4) | 3.65 (0–18) | 1.22zł (0.0–5.0) | 6.36 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.52 Er (1–10) | 1.2% | 26.1% | 1.04 (0–4) | 3.57 (0–18) | 1.21zł (0.0–5.0) | 6.33 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 5.63 Er (1–10) | 1.5% | 26.5% | 1.05 (0–4) | 3.73 (0–20) | 1.22zł (0.0–5.0) | 6.40 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 5.41 Er (1–10) | 1.0% | 25.8% | 1.02 (0–4) | 3.44 (0–18) | 1.20zł (0.0–5.0) | 6.25 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 5.63 Er (1–10) | 1.7% | 26.5% | 1.05 (0–4) | 3.74 (0–21) | 1.22zł (0.0–5.0) | 6.39 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_PLUS1` | 5.67 Er (1–10) | 1.3% | 26.8% | 1.06 (0–4) | 3.80 (0–18) | 1.25zł (0.0–5.0) | 6.42 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 5.64 Er (1–10) | 1.6% | 26.5% | 1.05 (0–4) | 3.72 (0–18) | 1.22zł (0.0–5.0) | 6.39 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 5.61 Er (1–10) | 1.4% | 26.5% | 1.05 (0–4) | 3.73 (0–18) | 1.23zł (0.0–5.0) | 6.38 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 5.71 Er (1–10) | 1.6% | 26.8% | 1.06 (0–4) | 3.84 (0–18) | 1.24zł (0.0–5.3) | 6.43 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 5.70 Er (1–10) | 1.5% | 26.6% | 1.06 (0–4) | 3.77 (0–18) | 1.22zł (0.0–5.0) | 6.45 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 5.06 Er (1–10) | 1.0% | 25.0% | 0.96 (0–4) | 3.18 (0–18) | 1.23zł (0.0–5.0) | 5.90 (0.5–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.36 Er (1–10) | 1.2% | 25.4% | 1.01 (0–4) | 3.37 (0–18) | 1.17zł (0.0–5.0) | 6.22 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.36 Er (1–10) | 0.9% | 25.5% | 1.01 (0–4) | 3.41 (0–18) | 1.20zł (0.0–5.0) | 6.24 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 5.78 Er (1–10) | 1.7% | 26.9% | 1.07 (0–4) | 3.88 (0–20) | 1.23zł (0.0–5.0) | 6.50 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 4.69 Er (1–10) | 0.5% | 22.7% | 0.91 (0–4) | 2.87 (0–18) | 1.18zł (0.0–5.0) | 5.74 (0.7–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_PLUS1` | 5.91 Er (1–10) | 2.0% | 27.3% | 1.09 (0–4) | 4.02 (0–18) | 1.22zł (0.0–5.0) | 6.61 (1.5–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.04 Er (1–10) | 0.5% | 21.4% | 0.82 (0–3) | 2.22 (0–18) | 1.31zł (0.0–4.7) | 4.96 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_KB_DECREES_PLUS1` | 5.75 Er (1–10) | 2.6% | 26.9% | 1.07 (0–4) | 3.93 (0–19) | 1.26zł (0.0–5.0) | 6.44 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.24 Er (1–10) | 0.4% | 25.1% | 0.99 (0–4) | 3.17 (0–18) | 1.17zł (0.0–5.0) | 6.15 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 4.92 Er (1–10) | 0.8% | 24.6% | 0.94 (0–4) | 3.00 (0–18) | 1.22zł (0.0–5.0) | 5.80 (0.5–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.