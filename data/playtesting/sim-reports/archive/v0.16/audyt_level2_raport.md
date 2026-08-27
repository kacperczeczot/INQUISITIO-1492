[Strona główna](../../../../../README.md) > [v0.16](README.md) > [audyt_level2_raport](audyt_level2_raport.md)

---

# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.16

**Wersja Balansu:** `v0.16` | **Data:** 2026-08-14 12:46 | **Przeanalizowano Wariantów:** 28 | **Próba:** 2000 gier/setup | **Czas:** 97.19s
**Wynik Bazy Poziomu 2 (Global):** `🟢 81.2 pkt` | 3p: `90.5 pkt` | 4p: `71.1 pkt` | 5p: `82.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (5)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🟢 ** 81.2** | 90.5 | 71.1 | 82.0 | ⚪ OPTYMALNY |
| `L2_KB_ERA_MINUS1` | Korona Era: 6 → 5 | 81.2 → 🟢 ** 90.3** (`⬆️ +9.1`) | 90.5 → 87.0 (`-3.5`) | 71.1 → 85.0 (`⬆️ +13.9`) | 82.0 → 98.8 (`⬆️ +16.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 3–8 → 3–7 | 81.2 → 🟢 ** 82.5** (`⬆️ +1.3`) | 90.5 → 90.2 (`-0.3`) | 71.1 → 74.2 (`⬆️ +3.1`) | 82.0 → 83.0 (`⬆️ +1.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_CAA_ERA_MINUS1` | Cienie Era: 5 → 4 | 81.2 → 🟢 ** 81.3** (`⬆️ +0.1`) | 90.5 | 71.1 → 71.3 (`⬆️ +0.2`) | 82.0 → 82.1 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2 → 3 | 81.2 → 🟢 ** 77.9** (`-3.3`) | 90.5 → 91.5 (`⬆️ +1.0`) | 71.1 → 55.9 (`-15.2`) | 82.0 → 86.4 (`⬆️ +4.4`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 23 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_PLUS1` | Cienie Era: 5 → 6 | 81.2 → 🟢 ** 81.0** (`-0.2`) | 90.5 | 71.1 → 70.7 (`-0.4`) | 82.0 → 81.7 (`-0.3`) | ⚪ OPTYMALNY |
| `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 81.2 → 🟢 ** 79.8** (`-1.4`) | 90.5 → 90.4 (`-0.1`) | 71.1 → 67.4 (`-3.7`) | 82.0 → 81.6 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–8 → 3–9 | 81.2 → 🟢 ** 79.4** (`-1.8`) | 90.5 → 87.7 (`-2.8`) | 71.1 → 69.0 (`-2.1`) | 82.0 → 81.6 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 81.2 → 🟢 ** 75.0** (`-6.2`) | 90.5 → 90.0 (`-0.5`) | 71.1 → 63.6 (`-7.5`) | 82.0 → 71.4 (`-10.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 3 → 4 | 81.2 → 🟢 ** 73.5** (`-7.7`) | 90.5 → 68.0 (`-22.5`) | 71.1 → 70.4 (`-0.7`) | 82.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 3 → 2 | 81.2 → 🟢 ** 69.3** (`-11.9`) | 90.5 → 69.3 (`-21.2`) | 71.1 → 56.7 (`-14.4`) | 82.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 81.2 → 🟢 ** 69.1** (`-12.1`) | 90.5 → 88.9 (`-1.6`) | 71.1 → 65.2 (`-5.9`) | 82.0 → 53.1 (`-28.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 81.2 → 🟢 ** 59.0** (`-22.2`) | 90.5 → 88.5 (`-2.0`) | 71.1 → 40.3 (`-30.8`) | 82.0 → 48.3 (`-33.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 3/4/4 → 4/5/5 | 81.2 → 🟢 ** 53.3** (`-27.9`) | 90.5 → 61.3 (`-29.2`) | 71.1 → 31.6 (`-39.5`) | 82.0 → 66.9 (`-15.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 0 → 1 | 81.2 → 🟢 ** 50.0** (`-31.2`) | 90.5 → 70.8 (`-19.7`) | 71.1 → 29.3 (`-41.8`) | 82.0 → 0.0 (`-82.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 2 → 3 | 81.2 → 🟡 ** 49.1** (`-32.1`) | 90.5 → 63.9 (`-26.6`) | 71.1 → 34.3 (`-36.8`) | 82.0 → 0.0 (`-82.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 2 → 1 | 81.2 → 🟡 ** 49.1** (`-32.1`) | 90.5 → 63.9 (`-26.6`) | 71.1 → 34.3 (`-36.8`) | 82.0 → 0.0 (`-82.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 7/6/6 → 8/7/7 | 81.2 → 🟡 ** 45.1** (`-36.1`) | 90.5 → 71.2 (`-19.3`) | 71.1 → 33.7 (`-37.4`) | 82.0 → 30.3 (`-51.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 2/3 → 3/4 | 81.2 → 🟡 ** 37.5** (`-43.7`) | 90.5 → 41.4 (`-49.1`) | 71.1 → 33.6 (`-37.5`) | 82.0 → 0.0 (`-82.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 7/6/6 → 6/5/5 | 81.2 → 🟡 ** 37.3** (`-43.9`) | 90.5 → 62.4 (`-28.1`) | 71.1 → 12.2 (`-58.9`) | 82.0 → 0.0 (`-82.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_PLUS1` | Korona Era: 6 → 7 | 81.2 → 🟡 ** 36.9** (`-44.3`) | 90.5 → 59.1 (`-31.4`) | 71.1 → 14.6 (`-56.5`) | 82.0 → 0.0 (`-82.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 3/4/4 → 2/3/3 | 81.2 → 🟡 ** 35.9** (`-45.3`) | 90.5 → 43.4 (`-47.1`) | 71.1 → 28.3 (`-42.8`) | 82.0 → 0.0 (`-82.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 2/3 → 1/2 | 81.2 → 🟡 ** 31.3** (`-49.9`) | 90.5 → 42.8 (`-47.7`) | 71.1 → 19.9 (`-51.2`) | 82.0 → 0.0 (`-82.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 81.2 → 🟡 ** 25.2** (`-56.0`) | 90.5 → 35.9 (`-54.6`) | 71.1 → 14.6 (`-56.5`) | 82.0 → 0.0 (`-82.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 81.2 → 🟡 ** 25.2** (`-56.0`) | 90.5 → 35.9 (`-54.6`) | 71.1 → 14.6 (`-56.5`) | 82.0 → 0.0 (`-82.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2 → 1 | 81.2 → 🟡 ** 25.1** (`-56.1`) | 90.5 → 35.8 (`-54.7`) | 71.1 → 14.4 (`-56.7`) | 82.0 → 0.0 (`-82.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 81.2 → 🔴 ** 23.6** (`-57.6`) | 90.5 → 37.0 (`-53.5`) | 71.1 → 10.1 (`-61.0`) | 82.0 → 0.0 (`-82.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 81.2 → 🔴 ** 23.6** (`-57.6`) | 90.5 → 37.0 (`-53.5`) | 71.1 → 10.1 (`-61.0`) | 82.0 → 0.0 (`-82.0`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (5)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 5.61 Er (1–9) | 3.1% | 28.6% | 1.04 (0–3) | 3.65 (0–18) | 0.52zł (0.0–2.7) | 6.27 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_MINUS1` | 5.48 Er (1–9) | 3.1% | 28.2% | 1.02 (0–3) | 3.48 (0–18) | 0.51zł (0.0–2.7) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 5.63 Er (1–9) | 4.0% | 28.7% | 1.04 (0–4) | 3.70 (0–18) | 0.52zł (0.0–2.7) | 6.28 (0.7–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_MINUS1` | 5.60 Er (1–9) | 3.1% | 28.6% | 1.04 (0–3) | 3.64 (0–18) | 0.52zł (0.0–2.7) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 5.63 Er (1–9) | 3.4% | 28.7% | 1.04 (0–3) | 3.68 (0–18) | 0.52zł (0.0–2.7) | 6.28 (0.7–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 23 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_PLUS1` | 5.62 Er (1–9) | 3.1% | 28.7% | 1.04 (0–3) | 3.66 (0–18) | 0.52zł (0.0–2.7) | 6.28 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_MINUS1` | 5.60 Er (1–9) | 3.1% | 28.6% | 1.04 (0–3) | 3.65 (0–18) | 0.52zł (0.0–2.7) | 6.27 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 5.59 Er (1–9) | 2.7% | 28.6% | 1.04 (0–3) | 3.63 (0–18) | 0.52zł (0.0–2.7) | 6.27 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_PLUS1` | 5.62 Er (1–9) | 3.2% | 28.7% | 1.04 (0–3) | 3.68 (0–18) | 0.52zł (0.0–2.7) | 6.28 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 5.69 Er (1–9) | 3.7% | 28.9% | 1.05 (0–3) | 3.76 (0–19) | 0.52zł (0.0–2.7) | 6.32 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 5.46 Er (1–9) | 2.6% | 28.2% | 1.02 (0–3) | 3.47 (0–17) | 0.52zł (0.0–2.8) | 6.17 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.58 Er (1–9) | 2.9% | 28.5% | 1.04 (0–3) | 3.61 (0–18) | 0.52zł (0.0–2.7) | 6.25 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 5.68 Er (1–9) | 4.4% | 28.9% | 1.05 (0–3) | 3.77 (0–18) | 0.53zł (0.0–2.7) | 6.32 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 5.70 Er (1–9) | 3.7% | 28.9% | 1.05 (0–3) | 3.77 (0–18) | 0.52zł (0.0–2.7) | 6.32 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 5.65 Er (1–9) | 3.4% | 28.8% | 1.05 (0–3) | 3.72 (0–20) | 0.53zł (0.0–2.7) | 6.29 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 5.76 Er (2–9) | 3.6% | 29.1% | 1.06 (0–3) | 3.83 (0–18) | 0.52zł (0.0–2.7) | 6.38 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 5.10 Er (1–9) | 2.5% | 27.4% | 0.96 (0–3) | 3.18 (0–18) | 0.55zł (0.0–3.0) | 5.83 (0.4–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 5.76 Er (1–9) | 4.0% | 29.2% | 1.06 (0–4) | 3.88 (0–18) | 0.55zł (0.0–2.7) | 6.36 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 5.85 Er (2–9) | 4.1% | 29.3% | 1.08 (0–3) | 3.94 (0–19) | 0.53zł (0.0–2.7) | 6.43 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.40 Er (1–9) | 2.8% | 27.9% | 1.01 (0–3) | 3.37 (0–18) | 0.51zł (0.0–2.7) | 6.11 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_PLUS1` | 5.70 Er (1–9) | 3.1% | 29.1% | 1.05 (0–3) | 3.79 (0–18) | 0.54zł (0.0–2.7) | 6.33 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.41 Er (1–9) | 2.4% | 28.0% | 1.01 (0–3) | 3.42 (0–18) | 0.51zł (0.0–2.7) | 6.16 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 4.96 Er (1–9) | 2.0% | 27.0% | 0.93 (0–3) | 2.99 (0–17) | 0.55zł (0.0–3.0) | 5.73 (0.4–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_KB_DECREES_PLUS1` | 5.76 Er (1–9) | 5.1% | 29.1% | 1.06 (0–3) | 3.89 (0–20) | 0.54zł (0.0–2.7) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.41 Er (1–9) | 1.1% | 28.1% | 1.01 (0–3) | 3.35 (0–18) | 0.51zł (0.0–2.7) | 6.14 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 4.75 Er (1–9) | 1.6% | 25.6% | 0.91 (0–3) | 2.86 (0–18) | 0.51zł (0.0–3.0) | 5.68 (0.7–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_PLUS1` | 5.92 Er (1–9) | 4.8% | 29.5% | 1.08 (0–4) | 4.01 (0–18) | 0.52zł (0.0–2.7) | 6.51 (1.8–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.02 Er (1–9) | 1.1% | 23.9% | 0.81 (0–3) | 2.20 (0–15) | 0.68zł (0.0–4.0) | 4.89 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.