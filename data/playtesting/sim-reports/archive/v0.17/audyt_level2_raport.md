[Strona główna](../../../../../README.md) > [v0.17](README.md) > [audyt_level2_raport](audyt_level2_raport.md)

---

# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.17

**Wersja Balansu:** `v0.17` | **Data:** 2026-08-14 13:17 | **Przeanalizowano Wariantów:** 28 | **Próba:** 300 gier/setup | **Czas:** 15.41s
**Wynik Bazy Poziomu 2 (Global):** `🟢 86.0 pkt` | 3p: `87.9 pkt` | 4p: `70.9 pkt` | 5p: `99.2 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (7)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🟢 ** 86.0** | 87.9 | 70.9 | 99.2 | ⚪ OPTYMALNY |
| `L2_KB_ERA_MINUS1` | Korona Era: 6 → 5 | 86.0 → 🟢 ** 92.0** (`⬆️ +6.0`) | 87.9 → 89.0 (`⬆️ +1.1`) | 70.9 → 89.0 (`⬆️ +18.1`) | 99.2 → 98.0 (`-1.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 3–8 → 3–7 | 86.0 → 🟢 ** 86.5** (`⬆️ +0.5`) | 87.9 → 88.6 (`⬆️ +0.7`) | 70.9 → 71.9 (`⬆️ +1.0`) | 99.2 → 98.9 (`-0.3`) | ⚪ OPTYMALNY |
| `L2_CAA_ERA_MINUS1` | Cienie Era: 5 → 4 | 86.0 → 🟢 ** 86.1** (`⬆️ +0.1`) | 87.9 | 70.9 → 71.1 (`⬆️ +0.2`) | 99.2 → 99.3 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 86.0 → 🟢 ** 85.6** (`-0.4`) | 87.9 → 87.5 (`-0.4`) | 70.9 → 71.9 (`⬆️ +1.0`) | 99.2 → 97.3 (`-1.9`) | ⚪ OPTYMALNY |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2 → 3 | 86.0 → 🟢 ** 83.8** (`-2.2`) | 87.9 → 88.3 (`⬆️ +0.4`) | 70.9 → 63.6 (`-7.3`) | 99.2 → 99.6 (`⬆️ +0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–8 → 3–9 | 86.0 → 🟢 ** 83.5** (`-2.5`) | 87.9 → 82.7 (`-5.2`) | 70.9 → 68.6 (`-2.3`) | 99.2 → 99.3 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 21 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_PLUS1` | Cienie Era: 5 → 6 | 86.0 → 🟢 ** 85.2** (`-0.8`) | 87.9 | 70.9 → 69.5 (`-1.4`) | 99.2 → 98.2 (`-1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 86.0 → 🟢 ** 85.0** (`-1.0`) | 87.9 | 70.9 → 68.3 (`-2.6`) | 99.2 → 98.8 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 86.0 → 🟢 ** 79.5** (`-6.5`) | 87.9 → 86.1 (`-1.8`) | 70.9 → 54.5 (`-16.4`) | 99.2 → 97.8 (`-1.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 3 → 4 | 86.0 → 🟢 ** 74.7** (`-11.3`) | 87.9 → 70.1 (`-17.8`) | 70.9 → 54.7 (`-16.2`) | 99.2 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 3 → 2 | 86.0 → 🟢 ** 71.5** (`-14.5`) | 87.9 → 60.5 (`-27.4`) | 70.9 → 54.7 (`-16.2`) | 99.2 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 86.0 → 🟢 ** 61.6** (`-24.4`) | 87.9 → 87.5 (`-0.4`) | 70.9 → 41.5 (`-29.4`) | 99.2 → 55.9 (`-43.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 3/4/4 → 4/5/5 | 86.0 → 🟢 ** 57.8** (`-28.2`) | 87.9 → 54.0 (`-33.9`) | 70.9 → 32.7 (`-38.2`) | 99.2 → 86.7 (`-12.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 2 → 3 | 86.0 → 🟡 ** 48.9** (`-37.1`) | 87.9 → 61.6 (`-26.3`) | 70.9 → 36.1 (`-34.8`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 2 → 1 | 86.0 → 🟡 ** 48.9** (`-37.1`) | 87.9 → 61.6 (`-26.3`) | 70.9 → 36.1 (`-34.8`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 7/6/6 → 8/7/7 | 86.0 → 🟡 ** 44.6** (`-41.4`) | 87.9 → 73.9 (`-14.0`) | 70.9 → 15.3 (`-55.6`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 0 → 1 | 86.0 → 🟡 ** 44.4** (`-41.6`) | 87.9 → 65.2 (`-22.7`) | 70.9 → 23.6 (`-47.3`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 3/4/4 → 2/3/3 | 86.0 → 🟡 ** 37.1** (`-48.9`) | 87.9 → 45.6 (`-42.3`) | 70.9 → 28.7 (`-42.2`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 7/6/6 → 6/5/5 | 86.0 → 🟡 ** 36.5** (`-49.5`) | 87.9 → 61.3 (`-26.6`) | 70.9 → 11.8 (`-59.1`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_PLUS1` | Korona Era: 6 → 7 | 86.0 → 🟡 ** 33.4** (`-52.6`) | 87.9 → 56.2 (`-31.7`) | 70.9 → 10.5 (`-60.4`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 2/3 → 3/4 | 86.0 → 🟡 ** 31.8** (`-54.2`) | 87.9 → 43.8 (`-44.1`) | 70.9 → 19.9 (`-51.0`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 2/3 → 1/2 | 86.0 → 🟡 ** 27.1** (`-58.9`) | 87.9 → 34.2 (`-53.7`) | 70.9 → 19.9 (`-51.0`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2 → 1 | 86.0 → 🟡 ** 26.8** (`-59.2`) | 87.9 → 37.4 (`-50.5`) | 70.9 → 16.2 (`-54.7`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 86.0 → 🔴 ** 23.2** (`-62.8`) | 87.9 → 33.9 (`-54.0`) | 70.9 → 12.5 (`-58.4`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 86.0 → 🔴 ** 23.2** (`-62.8`) | 87.9 → 33.9 (`-54.0`) | 70.9 → 12.5 (`-58.4`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 86.0 → 🔴 ** 22.2** (`-63.8`) | 87.9 → 34.0 (`-53.9`) | 70.9 → 10.5 (`-60.4`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 86.0 → 🔴 ** 22.2** (`-63.8`) | 87.9 → 34.0 (`-53.9`) | 70.9 → 10.5 (`-60.4`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (7)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 5.61 Er (1–9) | 3.0% | 28.6% | 1.02 (0–3) | 3.60 (0–15) | 0.53zł (0.0–2.3) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_MINUS1` | 5.49 Er (1–9) | 3.0% | 28.2% | 1.01 (0–3) | 3.44 (0–15) | 0.53zł (0.0–2.3) | 6.16 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 5.64 Er (1–9) | 3.9% | 28.7% | 1.02 (0–3) | 3.65 (0–18) | 0.53zł (0.0–2.3) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_MINUS1` | 5.60 Er (1–9) | 3.0% | 28.6% | 1.02 (0–3) | 3.59 (0–15) | 0.53zł (0.0–2.3) | 6.22 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_PLUS1` | 5.62 Er (1–9) | 3.1% | 28.7% | 1.02 (0–3) | 3.63 (0–15) | 0.53zł (0.0–2.3) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 5.64 Er (1–9) | 3.4% | 28.7% | 1.02 (0–3) | 3.62 (0–15) | 0.53zł (0.0–2.3) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 5.60 Er (1–9) | 2.6% | 28.6% | 1.02 (0–3) | 3.58 (0–14) | 0.53zł (0.0–2.3) | 6.22 (1.2–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 21 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_PLUS1` | 5.62 Er (1–9) | 3.0% | 28.7% | 1.02 (0–3) | 3.62 (0–15) | 0.53zł (0.0–2.3) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_MINUS1` | 5.61 Er (1–9) | 3.0% | 28.6% | 1.02 (0–3) | 3.60 (0–15) | 0.53zł (0.0–2.3) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.58 Er (1–9) | 2.9% | 28.5% | 1.02 (0–3) | 3.55 (0–15) | 0.53zł (0.0–2.3) | 6.21 (1.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 5.70 Er (1–9) | 3.6% | 28.9% | 1.03 (0–3) | 3.72 (0–15) | 0.53zł (0.0–2.3) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 5.47 Er (1–9) | 2.7% | 28.2% | 1.00 (0–3) | 3.42 (0–14) | 0.53zł (0.0–2.3) | 6.13 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 5.68 Er (1–9) | 4.5% | 28.9% | 1.03 (0–3) | 3.72 (0–15) | 0.54zł (0.0–2.3) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 5.70 Er (1–9) | 3.6% | 28.9% | 1.03 (0–3) | 3.71 (0–15) | 0.54zł (0.0–2.3) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 5.78 Er (2–9) | 3.5% | 29.1% | 1.05 (0–3) | 3.79 (0–15) | 0.53zł (0.0–2.3) | 6.35 (1.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 5.08 Er (1–9) | 2.3% | 27.4% | 0.93 (0–3) | 3.11 (0–15) | 0.57zł (0.0–3.0) | 5.78 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 5.77 Er (1–9) | 4.2% | 29.2% | 1.04 (0–3) | 3.85 (0–18) | 0.56zł (0.0–2.3) | 6.33 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 5.66 Er (1–9) | 3.5% | 28.8% | 1.03 (0–3) | 3.67 (0–15) | 0.54zł (0.0–2.3) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.42 Er (1–9) | 2.2% | 28.0% | 0.99 (0–3) | 3.37 (0–15) | 0.52zł (0.0–2.3) | 6.12 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.40 Er (1–9) | 2.6% | 27.9% | 0.99 (0–3) | 3.31 (0–15) | 0.52zł (0.0–2.3) | 6.07 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_PLUS1` | 5.71 Er (1–9) | 3.0% | 29.0% | 1.03 (0–3) | 3.73 (0–15) | 0.55zł (0.0–2.3) | 6.29 (1.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 5.87 Er (2–9) | 4.1% | 29.3% | 1.06 (0–3) | 3.91 (0–15) | 0.54zł (0.0–2.3) | 6.40 (1.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 4.94 Er (1–9) | 2.0% | 26.9% | 0.91 (0–3) | 2.92 (0–14) | 0.56zł (0.0–3.0) | 5.68 (0.7–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_SO_CONDEMNS_MINUS1` | 4.75 Er (1–9) | 1.6% | 25.5% | 0.89 (0–3) | 2.80 (0–15) | 0.53zł (0.0–2.3) | 5.63 (1.2–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_PLUS1` | 5.94 Er (1–9) | 4.9% | 29.5% | 1.07 (0–3) | 3.97 (0–16) | 0.53zł (0.0–2.3) | 6.47 (2.0–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.02 Er (1–9) | 1.1% | 24.0% | 0.78 (0–3) | 2.17 (0–14) | 0.69zł (0.0–3.3) | 4.85 (0.0–9.7) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_KB_DECREES_PLUS1` | 5.76 Er (1–9) | 5.1% | 29.1% | 1.04 (0–3) | 3.84 (0–15) | 0.56zł (0.0–2.3) | 6.32 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.40 Er (1–9) | 1.0% | 28.1% | 0.99 (0–3) | 3.30 (0–13) | 0.53zł (0.0–2.3) | 6.09 (1.2–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.