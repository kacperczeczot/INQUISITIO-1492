[Strona główna](../../../../../README.md) > [v0.14](README.md) > [audyt_level2_raport](audyt_level2_raport.md)

---

# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.14

**Wersja Balansu:** `v0.14` | **Data:** 2026-08-14 11:52 | **Przeanalizowano Wariantów:** 28 | **Próba:** 500 gier/setup | **Czas:** 22.84s
**Wynik Bazy Poziomu 2 (Global):** `🟢 86.1 pkt` | 3p: `91.5 pkt` | 4p: `67.9 pkt` | 5p: `98.9 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🟢 ** 86.1** | 91.5 | 67.9 | 98.9 | ⚪ OPTYMALNY |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 3/4/4 → 4/5/5 | 86.1 → 🟡 ** 39.2** (`-46.9`) | 91.5 → 56.7 (`-34.8`) | 67.9 → 16.6 (`-51.3`) | 98.9 → 44.2 (`-54.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 3/4/4 → 2/3/3 | 86.1 → 🟡 ** 38.4** (`-47.7`) | 91.5 → 45.2 (`-46.3`) | 67.9 → 31.6 (`-36.3`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2/3/3 → 3/4/4 | 🟢 ** 86.1** | 91.5 → 91.6 (`⬆️ +0.1`) | 67.9 | 98.9 | ⚪ OPTYMALNY |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2/3/3 → 1/2/2 | 86.1 → 🟢 ** 69.1** (`-17.0`) | 91.5 → 37.6 (`-53.9`) | 67.9 → 70.7 (`⬆️ +2.8`) | 98.9 → 99.1 (`⬆️ +0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 86.1 → 🟡 ** 26.0** (`-60.1`) | 91.5 → 37.1 (`-54.4`) | 67.9 → 14.9 (`-53.0`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 86.1 → 🟡 ** 26.0** (`-60.1`) | 91.5 → 37.1 (`-54.4`) | 67.9 → 14.9 (`-53.0`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_ERA_PLUS1` | Cienie Era: 5/5/5 → 6/6/6 | 86.1 → 🟢 ** 85.7** (`-0.4`) | 91.5 → 91.4 (`-0.1`) | 67.9 → 66.9 (`-1.0`) | 98.9 → 98.8 (`-0.1`) | ⚪ OPTYMALNY |
| `L2_CAA_ERA_MINUS1` | Cienie Era: 5/5/5 → 4/4/4 | 86.1 → 🟢 ** 86.8** (`⬆️ +0.7`) | 91.5 | 67.9 → 70.1 (`⬆️ +2.2`) | 98.9 | 🟢 POPRAWIA GLOBALNIE |
| `L2_KB_ERA_PLUS1` | Korona Era: 6/6/6 → 7/7/7 | 86.1 → 🟡 ** 36.9** (`-49.2`) | 91.5 → 70.2 (`-21.3`) | 67.9 → 3.6 (`-64.3`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_MINUS1` | Korona Era: 6/6/6 → 5/5/5 | 86.1 → 🟢 ** 77.6** (`-8.5`) | 91.5 → 89.1 (`-2.4`) | 67.9 → 68.7 (`⬆️ +0.8`) | 98.9 → 75.1 (`-23.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2/2/2 → 3/3/3 | 86.1 → 🔴 ** 19.7** (`-66.4`) | 91.5 → 35.7 (`-55.8`) | 67.9 → 3.6 (`-64.3`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2/2/2 → 1/1/1 | 86.1 → 🔴 ** 19.7** (`-66.4`) | 91.5 → 35.7 (`-55.8`) | 67.9 → 3.6 (`-64.3`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 0/0/0 → 1/1/1 | 86.1 → 🟡 ** 44.5** (`-41.6`) | 91.5 → 70.8 (`-20.7`) | 67.9 → 18.2 (`-49.7`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3/3/3 → 4/4/4 | 86.1 → 🟢 ** 68.7** (`-17.4`) | 91.5 → 89.1 (`-2.4`) | 67.9 → 32.8 (`-35.1`) | 98.9 → 84.1 (`-14.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3/3/3 → 2/2/2 | 86.1 → 🟢 ** 75.2** (`-10.9`) | 91.5 → 89.3 (`-2.2`) | 67.9 → 61.5 (`-6.4`) | 98.9 → 74.8 (`-24.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 7/6/6 → 8/7/7 | 86.1 → 🟢 ** 53.9** (`-32.2`) | 91.5 → 65.2 (`-26.3`) | 67.9 → 28.9 (`-39.0`) | 98.9 → 67.5 (`-31.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 7/6/6 → 6/5/5 | 86.1 → 🟡 ** 37.5** (`-48.6`) | 91.5 → 61.6 (`-29.9`) | 67.9 → 13.3 (`-54.6`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 86.1 → 🟢 ** 84.6** (`-1.5`) | 91.5 → 90.8 (`-0.7`) | 67.9 → 64.6 (`-3.3`) | 98.9 → 98.4 (`-0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 86.1 → 🟢 ** 86.4** (`⬆️ +0.3`) | 91.5 → 90.8 (`-0.7`) | 67.9 → 68.7 (`⬆️ +0.8`) | 98.9 → 99.8 (`⬆️ +0.9`) | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–8 → 3–9 | 86.1 → 🟢 ** 82.6** (`-3.5`) | 91.5 → 87.3 (`-4.2`) | 67.9 → 62.0 (`-5.9`) | 98.9 → 98.4 (`-0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 3–8 → 3–7 | 86.1 → 🟢 ** 86.8** (`⬆️ +0.7`) | 91.5 → 91.1 (`-0.4`) | 67.9 → 70.0 (`⬆️ +2.1`) | 98.9 → 99.3 (`⬆️ +0.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 2/3 → 3/4 | 86.1 → 🟡 ** 38.0** (`-48.1`) | 91.5 → 41.4 (`-50.1`) | 67.9 → 34.7 (`-33.2`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 2/3 → 1/2 | 86.1 → 🟡 ** 28.2** (`-57.9`) | 91.5 → 37.0 (`-54.5`) | 67.9 → 19.5 (`-48.4`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 2 → 3 | 86.1 → 🟢 ** 50.4** (`-35.7`) | 91.5 → 64.7 (`-26.8`) | 67.9 → 36.1 (`-31.8`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 2 → 1 | 86.1 → 🟢 ** 50.4** (`-35.7`) | 91.5 → 64.7 (`-26.8`) | 67.9 → 36.1 (`-31.8`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 3 → 4 | 86.1 → 🟢 ** 77.8** (`-8.3`) | 91.5 → 68.1 (`-23.4`) | 67.9 → 66.5 (`-1.4`) | 98.9 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 3 → 2 | 86.1 → 🟢 ** 71.4** (`-14.7`) | 91.5 → 63.8 (`-27.7`) | 67.9 → 51.4 (`-16.5`) | 98.9 | 🔴 POGARSZA GLOBALNIE |

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 5.64 Er (1–9) | 3.2% | 28.7% | 1.03 (0–3) | 3.65 (0–15) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 5.74 Er (1–9) | 3.9% | 29.0% | 1.05 (0–3) | 3.77 (0–15) | 0.53zł (0.0–2.7) | 6.31 (1.2–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.44 Er (1–9) | 2.4% | 28.1% | 1.01 (0–3) | 3.42 (0–15) | 0.52zł (0.0–2.7) | 6.15 (1.2–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 5.65 Er (1–9) | 3.4% | 28.8% | 1.04 (0–3) | 3.66 (0–15) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 5.16 Er (1–9) | 1.9% | 27.2% | 0.97 (0–3) | 3.22 (0–15) | 0.52zł (0.0–2.7) | 5.95 (1.2–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 5.97 Er (1–9) | 5.1% | 29.6% | 1.08 (0–4) | 4.03 (0–16) | 0.53zł (0.0–2.3) | 6.51 (1.8–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.02 Er (1–9) | 1.1% | 24.0% | 0.79 (0–3) | 2.19 (0–15) | 0.70zł (0.0–4.0) | 4.86 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_ERA_PLUS1` | 5.65 Er (1–9) | 3.2% | 28.8% | 1.04 (0–3) | 3.66 (0–15) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_MINUS1` | 5.63 Er (1–9) | 3.2% | 28.7% | 1.03 (0–3) | 3.64 (0–15) | 0.53zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_PLUS1` | 5.74 Er (1–9) | 3.2% | 29.2% | 1.05 (0–3) | 3.79 (0–15) | 0.55zł (0.0–2.7) | 6.33 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_MINUS1` | 5.51 Er (1–9) | 3.2% | 28.3% | 1.02 (0–3) | 3.48 (0–15) | 0.53zł (0.0–2.7) | 6.19 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 5.79 Er (1–9) | 5.3% | 29.3% | 1.06 (0–3) | 3.89 (0–16) | 0.55zł (0.0–2.7) | 6.35 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.43 Er (1–9) | 1.1% | 28.2% | 1.00 (0–3) | 3.34 (0–15) | 0.52zł (0.0–2.7) | 6.12 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 5.69 Er (1–9) | 3.6% | 28.9% | 1.04 (0–3) | 3.73 (0–15) | 0.54zł (0.0–2.7) | 6.29 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 5.71 Er (1–9) | 4.7% | 29.0% | 1.04 (0–3) | 3.77 (0–15) | 0.53zł (0.0–2.7) | 6.31 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.61 Er (1–9) | 2.9% | 28.6% | 1.03 (0–3) | 3.59 (0–15) | 0.53zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 5.80 Er (1–9) | 4.2% | 29.3% | 1.06 (0–4) | 3.89 (0–18) | 0.56zł (0.0–2.7) | 6.36 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.43 Er (1–9) | 2.8% | 28.0% | 1.00 (0–3) | 3.36 (0–15) | 0.52zł (0.0–2.7) | 6.11 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_MINUS1` | 5.64 Er (1–9) | 3.2% | 28.7% | 1.03 (0–3) | 3.64 (0–15) | 0.53zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_PLUS1` | 5.66 Er (1–9) | 3.3% | 28.8% | 1.04 (0–3) | 3.68 (0–15) | 0.53zł (0.0–2.7) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 5.63 Er (1–9) | 2.8% | 28.7% | 1.03 (0–3) | 3.63 (0–15) | 0.53zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 5.67 Er (1–9) | 4.1% | 28.8% | 1.04 (0–4) | 3.70 (0–18) | 0.53zł (0.0–2.7) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 5.90 Er (2–9) | 4.3% | 29.4% | 1.07 (0–3) | 3.95 (0–16) | 0.53zł (0.0–2.7) | 6.43 (1.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 4.97 Er (1–9) | 2.0% | 27.1% | 0.92 (0–3) | 2.97 (0–15) | 0.56zł (0.0–3.0) | 5.72 (0.6–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 5.81 Er (2–9) | 3.7% | 29.2% | 1.06 (0–3) | 3.84 (0–15) | 0.53zł (0.0–2.7) | 6.38 (1.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 5.11 Er (1–9) | 2.4% | 27.5% | 0.95 (0–3) | 3.16 (0–15) | 0.56zł (0.0–3.0) | 5.82 (0.6–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 5.73 Er (1–9) | 3.8% | 29.0% | 1.05 (0–3) | 3.76 (0–16) | 0.53zł (0.0–2.7) | 6.32 (1.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 5.49 Er (1–9) | 2.7% | 28.3% | 1.01 (0–3) | 3.46 (0–15) | 0.52zł (0.0–2.7) | 6.16 (1.2–10.0) | 🟢 W NORMIE |

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.