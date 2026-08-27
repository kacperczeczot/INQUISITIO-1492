[Strona główna](../../../../../README.md) > [v0.18](README.md) > [audyt_level2_raport](audyt_level2_raport.md)

---

# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.18

**Wersja Balansu:** `v0.18` | **Data:** 2026-08-14 13:29 | **Przeanalizowano Wariantów:** 28 | **Próba:** 3000 gier/setup | **Czas:** 143.91s
**Wynik Bazy Poziomu 2 (Global):** `🟢 89.9 pkt` | 3p: `86.2 pkt` | 4p: `84.5 pkt` | 5p: `98.9 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (7)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🟢 ** 89.9** | 86.2 | 84.5 | 98.9 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 3–8 → 3–7 | 89.9 → 🟢 ** 91.7** (`⬆️ +1.8`) | 86.2 → 87.1 (`⬆️ +0.9`) | 84.5 → 88.6 (`⬆️ +4.1`) | 98.9 → 99.3 (`⬆️ +0.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 89.9 → 🟢 ** 90.1** (`⬆️ +0.2`) | 86.2 → 85.8 (`-0.4`) | 84.5 → 84.8 (`⬆️ +0.3`) | 98.9 → 99.6 (`⬆️ +0.7`) | ⚪ OPTYMALNY |
| `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 89.9 → 🟢 ** 90.0** (`⬆️ +0.1`) | 86.2 | 84.5 → 85.7 (`⬆️ +1.2`) | 98.9 → 98.2 (`-0.7`) | ⚪ OPTYMALNY |
| `L2_CAA_ERA_MINUS1` | Cienie Era: 5 → 4 | 🟢 ** 89.9** | 86.2 | 84.5 | 98.9 → 99.0 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–8 → 3–9 | 89.9 → 🟢 ** 89.2** (`-0.7`) | 86.2 → 83.8 (`-2.4`) | 84.5 → 85.4 (`⬆️ +0.9`) | 98.9 → 98.5 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_PLUS1` | Korona Era: 5 → 6 | 89.9 → 🟢 ** 82.5** (`-7.4`) | 86.2 → 90.4 (`⬆️ +4.2`) | 84.5 → 73.3 (`-11.2`) | 98.9 → 83.7 (`-15.2`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 21 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_PLUS1` | Cienie Era: 5 → 6 | 89.9 → 🟢 ** 89.2** (`-0.7`) | 86.2 → 85.2 (`-1.0`) | 84.5 → 83.6 (`-0.9`) | 98.9 → 98.7 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2 → 3 | 89.9 → 🟢 ** 82.9** (`-7.0`) | 86.2 → 84.8 (`-1.4`) | 84.5 → 66.0 (`-18.5`) | 98.9 → 98.0 (`-0.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 3 → 2 | 89.9 → 🟢 ** 78.9** (`-11.0`) | 86.2 → 69.3 (`-16.9`) | 84.5 → 68.4 (`-16.1`) | 98.9 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 89.9 → 🟢 ** 77.4** (`-12.5`) | 86.2 → 84.6 (`-1.6`) | 84.5 → 68.7 (`-15.8`) | 98.9 → 78.8 (`-20.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 3 → 4 | 89.9 → 🟢 ** 76.9** (`-13.0`) | 86.2 → 63.3 (`-22.9`) | 84.5 → 68.4 (`-16.1`) | 98.9 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_MINUS1` | Korona Era: 5 → 4 | 89.9 → 🟢 ** 75.1** (`-14.8`) | 86.2 → 71.7 (`-14.5`) | 84.5 → 55.8 (`-28.7`) | 98.9 → 97.7 (`-1.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 89.9 → 🟢 ** 74.5** (`-15.4`) | 86.2 → 84.9 (`-1.3`) | 84.5 → 66.1 (`-18.4`) | 98.9 → 72.4 (`-26.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 0 → 1 | 89.9 → 🟢 ** 58.8** (`-31.1`) | 86.2 → 83.2 (`-3.0`) | 84.5 → 34.4 (`-50.1`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 7/6/6 → 8/7/7 | 89.9 → 🟢 ** 57.2** (`-32.7`) | 86.2 → 63.4 (`-22.8`) | 84.5 → 50.3 (`-34.2`) | 98.9 → 58.0 (`-40.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 7/6/6 → 6/5/5 | 89.9 → 🟢 ** 52.0** (`-37.9`) | 86.2 → 54.9 (`-31.3`) | 84.5 → 49.1 (`-35.4`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 3/4/4 → 4/5/5 | 89.9 → 🟡 ** 47.1** (`-42.8`) | 86.2 → 47.1 (`-39.1`) | 84.5 → 37.0 (`-47.5`) | 98.9 → 57.3 (`-41.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 3/4/4 → 2/3/3 | 89.9 → 🟡 ** 45.1** (`-44.8`) | 86.2 → 45.0 (`-41.2`) | 84.5 → 45.2 (`-39.3`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 2 → 3 | 89.9 → 🟡 ** 45.1** (`-44.8`) | 86.2 → 57.5 (`-28.7`) | 84.5 → 32.7 (`-51.8`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 2 → 1 | 89.9 → 🟡 ** 45.1** (`-44.8`) | 86.2 → 57.5 (`-28.7`) | 84.5 → 32.7 (`-51.8`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 2/3 → 1/2 | 89.9 → 🟡 ** 28.6** (`-61.3`) | 86.2 → 40.6 (`-45.6`) | 84.5 → 16.7 (`-67.8`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 89.9 → 🟡 ** 27.2** (`-62.7`) | 86.2 → 37.0 (`-49.2`) | 84.5 → 17.4 (`-67.1`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 89.9 → 🟡 ** 27.2** (`-62.7`) | 86.2 → 37.0 (`-49.2`) | 84.5 → 17.4 (`-67.1`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 2/3 → 3/4 | 89.9 → 🟡 ** 25.6** (`-64.3`) | 86.2 → 34.5 (`-51.7`) | 84.5 → 16.7 (`-67.8`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 89.9 → 🟡 ** 25.3** (`-64.6`) | 86.2 → 35.9 (`-50.3`) | 84.5 → 14.7 (`-69.8`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 89.9 → 🟡 ** 25.3** (`-64.6`) | 86.2 → 35.9 (`-50.3`) | 84.5 → 14.7 (`-69.8`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2 → 1 | 89.9 → 🔴 ** 23.6** (`-66.3`) | 86.2 → 31.2 (`-55.0`) | 84.5 → 16.1 (`-68.4`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (7)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 5.48 Er (1–9) | 3.2% | 28.2% | 1.02 (0–4) | 3.49 (0–20) | 0.51zł (0.0–3.0) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 5.51 Er (1–9) | 4.1% | 28.3% | 1.02 (0–4) | 3.53 (0–20) | 0.52zł (0.0–3.0) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_PLUS1` | 5.49 Er (1–9) | 3.3% | 28.3% | 1.02 (0–4) | 3.51 (0–20) | 0.51zł (0.0–3.0) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_MINUS1` | 5.48 Er (1–9) | 3.2% | 28.2% | 1.02 (0–4) | 3.48 (0–20) | 0.51zł (0.0–3.0) | 6.18 (0.7–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_MINUS1` | 5.47 Er (1–9) | 3.2% | 28.2% | 1.02 (0–4) | 3.48 (0–20) | 0.51zł (0.0–3.0) | 6.18 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 5.47 Er (1–9) | 2.8% | 28.2% | 1.02 (0–4) | 3.47 (0–18) | 0.51zł (0.0–3.0) | 6.18 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_PLUS1` | 5.61 Er (1–9) | 3.2% | 28.6% | 1.04 (0–4) | 3.66 (0–20) | 0.52zł (0.0–3.0) | 6.27 (0.7–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 21 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_PLUS1` | 5.49 Er (1–9) | 3.2% | 28.2% | 1.02 (0–4) | 3.50 (0–20) | 0.51zł (0.0–3.0) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 5.50 Er (1–9) | 3.5% | 28.3% | 1.02 (0–4) | 3.51 (0–20) | 0.51zł (0.0–3.0) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 5.35 Er (1–9) | 2.7% | 27.8% | 1.00 (0–4) | 3.32 (0–20) | 0.51zł (0.0–3.0) | 6.10 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 5.55 Er (1–9) | 4.4% | 28.5% | 1.03 (0–4) | 3.60 (0–20) | 0.52zł (0.0–3.0) | 6.23 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 5.55 Er (1–9) | 3.7% | 28.4% | 1.03 (0–4) | 3.58 (0–20) | 0.52zł (0.0–3.0) | 6.23 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_MINUS1` | 5.36 Er (1–9) | 3.2% | 27.8% | 1.00 (0–4) | 3.34 (0–20) | 0.51zł (0.0–3.0) | 6.11 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.45 Er (1–9) | 3.0% | 28.1% | 1.02 (0–4) | 3.44 (0–18) | 0.51zł (0.0–3.0) | 6.17 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 5.57 Er (1–9) | 3.5% | 28.6% | 1.04 (0–4) | 3.64 (0–20) | 0.52zł (0.0–3.0) | 6.25 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 5.63 Er (1–9) | 4.0% | 28.8% | 1.04 (0–4) | 3.72 (0–20) | 0.55zł (0.0–3.0) | 6.28 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.29 Er (1–9) | 2.9% | 27.5% | 0.99 (0–4) | 3.23 (0–20) | 0.50zł (0.0–3.0) | 6.04 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 5.56 Er (1–9) | 3.8% | 28.5% | 1.03 (0–4) | 3.59 (0–20) | 0.52zł (0.0–3.0) | 6.23 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.31 Er (1–9) | 2.5% | 27.7% | 1.00 (0–4) | 3.28 (0–20) | 0.51zł (0.0–3.0) | 6.09 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 5.63 Er (2–9) | 3.6% | 28.6% | 1.04 (0–4) | 3.66 (0–20) | 0.52zł (0.0–3.0) | 6.29 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 4.99 Er (1–9) | 2.5% | 27.0% | 0.94 (0–4) | 3.04 (0–20) | 0.55zł (0.0–3.0) | 5.76 (0.4–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_GC_FALLS_MINUS1` | 4.86 Er (1–9) | 2.0% | 26.7% | 0.92 (0–4) | 2.87 (0–20) | 0.54zł (0.0–3.0) | 5.67 (0.4–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_PLUS1` | 5.78 Er (1–9) | 4.8% | 29.0% | 1.06 (0–4) | 3.82 (0–20) | 0.51zł (0.0–2.8) | 6.41 (1.8–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 3.97 Er (1–9) | 1.1% | 23.6% | 0.80 (0–4) | 2.14 (0–15) | 0.68zł (0.0–4.0) | 4.86 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_GC_FALLS_PLUS1` | 5.70 Er (2–9) | 4.1% | 28.8% | 1.05 (0–4) | 3.75 (0–20) | 0.52zł (0.0–3.0) | 6.33 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 5.76 Er (1–9) | 5.2% | 29.1% | 1.06 (0–4) | 3.90 (0–20) | 0.54zł (0.0–3.0) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.03 Er (1–9) | 1.1% | 26.5% | 0.95 (0–4) | 2.85 (0–20) | 0.49zł (0.0–3.0) | 5.85 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 4.69 Er (1–9) | 1.6% | 25.4% | 0.90 (0–4) | 2.76 (0–20) | 0.51zł (0.0–3.0) | 5.64 (0.7–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.