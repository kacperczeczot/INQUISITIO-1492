# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.13

**Wersja Balansu:** `v0.13` | **Data:** 2026-08-14 11:44 | **Przeanalizowano Wariantów:** 37 | **Próba:** 500 gier/setup | **Czas:** 30.47s
**Wynik Bazy Poziomu 2 (Global):** `🟢 80.5 pkt` | 3p: `91.5 pkt` | 4p: `67.9 pkt` | 5p: `82.2 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🟢 ** 80.5** | 91.5 | 67.9 | 82.2 | ⚪ OPTYMALNY |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 3/4/4 → 4/5/5 | 80.5 → 🟡 ** 32.1** (`-48.4`) | 91.5 → 56.7 (`-34.8`) | 67.9 → 16.6 (`-51.3`) | 82.2 → 23.0 (`-59.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 3/4/4 → 2/3/3 | 80.5 → 🟡 ** 38.4** (`-42.1`) | 91.5 → 45.2 (`-46.3`) | 67.9 → 31.6 (`-36.3`) | 82.2 → 0.0 (`-82.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2/3/3 → 3/4/4 | 80.5 → 🟢 ** 80.6** (`⬆️ +0.1`) | 91.5 → 91.6 (`⬆️ +0.1`) | 67.9 | 82.2 | ⚪ OPTYMALNY |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2/3/3 → 1/2/2 | 80.5 → 🟢 ** 53.3** (`-27.2`) | 91.5 → 37.6 (`-53.9`) | 67.9 → 70.7 (`⬆️ +2.8`) | 82.2 → 51.5 (`-30.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 80.5 → 🟡 ** 26.0** (`-54.5`) | 91.5 → 37.1 (`-54.4`) | 67.9 → 14.9 (`-53.0`) | 82.2 → 0.0 (`-82.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 80.5 → 🟡 ** 26.0** (`-54.5`) | 91.5 → 37.1 (`-54.4`) | 67.9 → 14.9 (`-53.0`) | 82.2 → 0.0 (`-82.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_ERA_PLUS1` | Cienie Era: 5/5/5 → 6/6/6 | 80.5 → 🟢 ** 80.1** (`-0.4`) | 91.5 → 91.4 (`-0.1`) | 67.9 → 66.9 (`-1.0`) | 82.2 → 81.9 (`-0.3`) | ⚪ OPTYMALNY |
| `L2_CAA_ERA_MINUS1` | Cienie Era: 5/5/5 → 4/4/4 | 80.5 → 🟢 ** 81.9** (`⬆️ +1.4`) | 91.5 | 67.9 → 70.1 (`⬆️ +2.2`) | 82.2 → 84.2 (`⬆️ +2.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KB_ERA_PLUS1` | Korona Era: 6/6/6 → 7/7/7 | 80.5 → 🟡 ** 36.9** (`-43.6`) | 91.5 → 70.2 (`-21.3`) | 67.9 → 3.6 (`-64.3`) | 82.2 → 0.0 (`-82.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_MINUS1` | Korona Era: 6/6/6 → 5/5/5 | 80.5 → 🟢 ** 81.6** (`⬆️ +1.1`) | 91.5 → 89.1 (`-2.4`) | 67.9 → 68.7 (`⬆️ +0.8`) | 82.2 → 86.9 (`⬆️ +4.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2/2/2 → 3/3/3 | 80.5 → 🔴 ** 19.7** (`-60.8`) | 91.5 → 35.7 (`-55.8`) | 67.9 → 3.6 (`-64.3`) | 82.2 → 0.0 (`-82.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2/2/2 → 1/1/1 | 80.5 → 🔴 ** 19.7** (`-60.8`) | 91.5 → 35.7 (`-55.8`) | 67.9 → 3.6 (`-64.3`) | 82.2 → 0.0 (`-82.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 0/0/0 → 1/1/1 | 80.5 → 🟡 ** 44.5** (`-36.0`) | 91.5 → 70.8 (`-20.7`) | 67.9 → 18.2 (`-49.7`) | 82.2 → 0.0 (`-82.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_MINUS1` | Korona Haki: 0/0/0 → -1/-1/-1 | 🟢 ** 80.5** | 91.5 | 67.9 | 82.2 | ⚪ OPTYMALNY |
| `L2_KB_ALT_DECREES_PLUS1` | Korona Alt Dekrety: 2 → 3 | 🟢 ** 80.5** | 91.5 | 67.9 | 82.2 | ⚪ OPTYMALNY |
| `L2_KB_ALT_DECREES_MINUS1` | Korona Alt Dekrety: 2 → 1 | 🟢 ** 80.5** | 91.5 | 67.9 | 82.2 | ⚪ OPTYMALNY |
| `L2_KB_ALT_HOOKS_PLUS1` | Korona Alt Haki: 0 → 1 | 🟢 ** 80.5** | 91.5 | 67.9 | 82.2 | ⚪ OPTYMALNY |
| `L2_KB_ALT_HOOKS_MINUS1` | Korona Alt Haki: 0 → -1 | 🟢 ** 80.5** | 91.5 | 67.9 | 82.2 | ⚪ OPTYMALNY |
| `L2_KB_ALT_ERA_PLUS1` | Korona Alt Era: 6 → 7 | 🟢 ** 80.5** | 91.5 | 67.9 | 82.2 | ⚪ OPTYMALNY |
| `L2_KB_ALT_ERA_MINUS1` | Korona Alt Era: 6 → 5 | 🟢 ** 80.5** | 91.5 | 67.9 | 82.2 | ⚪ OPTYMALNY |
| `L2_KB_ALT_MINP_PLUS1` | Korona Alt min graczy: 99 → 100 | 🟢 ** 80.5** | 91.5 | 67.9 | 82.2 | ⚪ OPTYMALNY |
| `L2_KB_ALT_MINP_MINUS1` | Korona Alt min graczy: 99 → 98 | 🟢 ** 80.5** | 91.5 | 67.9 | 82.2 | ⚪ OPTYMALNY |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3/3/3 → 4/4/4 | 80.5 → 🟢 ** 55.9** (`-24.6`) | 91.5 → 89.1 (`-2.4`) | 67.9 → 32.8 (`-35.1`) | 82.2 → 45.8 (`-36.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3/3/3 → 2/2/2 | 80.5 → 🟢 ** 78.0** (`-2.5`) | 91.5 → 89.3 (`-2.2`) | 67.9 → 61.5 (`-6.4`) | 82.2 → 83.1 (`⬆️ +0.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 7/6/6 → 8/7/7 | 80.5 → 🟡 ** 38.0** (`-42.5`) | 91.5 → 65.2 (`-26.3`) | 67.9 → 28.9 (`-39.0`) | 82.2 → 20.0 (`-62.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 7/6/6 → 6/5/5 | 80.5 → 🟡 ** 37.5** (`-43.0`) | 91.5 → 61.6 (`-29.9`) | 67.9 → 13.3 (`-54.6`) | 82.2 → 0.0 (`-82.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 80.5 → 🟢 ** 79.1** (`-1.4`) | 91.5 → 90.8 (`-0.7`) | 67.9 → 64.6 (`-3.3`) | 82.2 → 82.0 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 80.5 → 🟢 ** 80.3** (`-0.2`) | 91.5 → 90.8 (`-0.7`) | 67.9 → 68.7 (`⬆️ +0.8`) | 82.2 → 81.5 (`-0.7`) | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–8 → 3–9 | 80.5 → 🟢 ** 77.1** (`-3.4`) | 91.5 → 87.3 (`-4.2`) | 67.9 → 62.0 (`-5.9`) | 82.2 → 82.1 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 3–8 → 3–7 | 80.5 → 🟢 ** 81.1** (`⬆️ +0.6`) | 91.5 → 91.1 (`-0.4`) | 67.9 → 70.0 (`⬆️ +2.1`) | 82.2 | 🟢 POPRAWIA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 2/3 → 3/4 | 80.5 → 🟡 ** 38.0** (`-42.5`) | 91.5 → 41.4 (`-50.1`) | 67.9 → 34.7 (`-33.2`) | 82.2 → 0.0 (`-82.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 2/3 → 1/2 | 80.5 → 🟡 ** 28.2** (`-52.3`) | 91.5 → 37.0 (`-54.5`) | 67.9 → 19.5 (`-48.4`) | 82.2 → 0.0 (`-82.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 2 → 3 | 80.5 → 🟢 ** 50.4** (`-30.1`) | 91.5 → 64.7 (`-26.8`) | 67.9 → 36.1 (`-31.8`) | 82.2 → 0.0 (`-82.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 2 → 1 | 80.5 → 🟢 ** 50.4** (`-30.1`) | 91.5 → 64.7 (`-26.8`) | 67.9 → 36.1 (`-31.8`) | 82.2 → 0.0 (`-82.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 3 → 4 | 80.5 → 🟢 ** 72.3** (`-8.2`) | 91.5 → 68.1 (`-23.4`) | 67.9 → 66.5 (`-1.4`) | 82.2 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 3 → 2 | 80.5 → 🟢 ** 65.8** (`-14.7`) | 91.5 → 63.8 (`-27.7`) | 67.9 → 51.4 (`-16.5`) | 82.2 | 🔴 POGARSZA GLOBALNIE |

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 5.63 Er (1–9) | 3.2% | 28.7% | 1.03 (0–3) | 3.73 (0–15) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 5.73 Er (1–9) | 3.9% | 29.0% | 1.05 (0–3) | 3.85 (0–15) | 0.53zł (0.0–2.7) | 6.32 (1.2–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.43 Er (1–9) | 2.5% | 28.1% | 1.01 (0–3) | 3.49 (0–15) | 0.52zł (0.0–2.7) | 6.16 (1.2–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 5.64 Er (1–9) | 3.4% | 28.7% | 1.03 (0–3) | 3.74 (0–15) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 5.15 Er (1–9) | 1.9% | 27.2% | 0.97 (0–3) | 3.30 (0–15) | 0.52zł (0.0–2.7) | 5.95 (1.2–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 5.96 Er (1–9) | 5.1% | 29.6% | 1.08 (0–4) | 4.12 (0–16) | 0.53zł (0.0–2.3) | 6.51 (1.8–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.02 Er (1–9) | 1.1% | 23.9% | 0.79 (0–3) | 2.22 (0–15) | 0.70zł (0.0–4.0) | 4.87 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_ERA_PLUS1` | 5.64 Er (1–9) | 3.2% | 28.8% | 1.03 (0–3) | 3.74 (0–15) | 0.53zł (0.0–2.7) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_MINUS1` | 5.62 Er (1–9) | 3.2% | 28.7% | 1.03 (0–3) | 3.72 (0–15) | 0.53zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_PLUS1` | 5.73 Er (1–9) | 3.2% | 29.1% | 1.05 (0–3) | 3.87 (0–15) | 0.55zł (0.0–2.7) | 6.34 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_MINUS1` | 5.50 Er (1–9) | 3.2% | 28.3% | 1.02 (0–3) | 3.56 (0–15) | 0.53zł (0.0–2.7) | 6.19 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 5.78 Er (1–9) | 5.3% | 29.2% | 1.06 (0–3) | 3.98 (0–16) | 0.55zł (0.0–2.7) | 6.36 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.42 Er (1–9) | 1.1% | 28.1% | 1.00 (0–3) | 3.41 (0–15) | 0.52zł (0.0–2.7) | 6.12 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 5.67 Er (1–9) | 3.6% | 28.9% | 1.04 (0–3) | 3.81 (0–15) | 0.54zł (0.0–2.7) | 6.30 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_MINUS1` | 5.63 Er (1–9) | 3.2% | 28.7% | 1.03 (0–3) | 3.73 (0–15) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_ALT_DECREES_PLUS1` | 5.63 Er (1–9) | 3.2% | 28.7% | 1.03 (0–3) | 3.73 (0–15) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_ALT_DECREES_MINUS1` | 5.63 Er (1–9) | 3.2% | 28.7% | 1.03 (0–3) | 3.73 (0–15) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_ALT_HOOKS_PLUS1` | 5.63 Er (1–9) | 3.2% | 28.7% | 1.03 (0–3) | 3.73 (0–15) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_ALT_HOOKS_MINUS1` | 5.63 Er (1–9) | 3.2% | 28.7% | 1.03 (0–3) | 3.73 (0–15) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_ALT_ERA_PLUS1` | 5.63 Er (1–9) | 3.2% | 28.7% | 1.03 (0–3) | 3.73 (0–15) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_ALT_ERA_MINUS1` | 5.63 Er (1–9) | 3.2% | 28.7% | 1.03 (0–3) | 3.73 (0–15) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_ALT_MINP_PLUS1` | 5.63 Er (1–9) | 3.2% | 28.7% | 1.03 (0–3) | 3.73 (0–15) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_ALT_MINP_MINUS1` | 5.63 Er (1–9) | 3.2% | 28.7% | 1.03 (0–3) | 3.73 (0–15) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 5.70 Er (1–9) | 4.6% | 29.0% | 1.04 (0–3) | 3.86 (0–15) | 0.53zł (0.0–2.7) | 6.32 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.59 Er (1–9) | 2.9% | 28.6% | 1.03 (0–3) | 3.67 (0–15) | 0.53zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 5.78 Er (1–9) | 4.2% | 29.2% | 1.05 (0–4) | 3.97 (0–18) | 0.56zł (0.0–2.7) | 6.37 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.42 Er (1–9) | 2.8% | 28.0% | 1.00 (0–3) | 3.44 (0–15) | 0.52zł (0.0–2.7) | 6.11 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_MINUS1` | 5.63 Er (1–9) | 3.2% | 28.7% | 1.03 (0–3) | 3.73 (0–15) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_PLUS1` | 5.64 Er (1–9) | 3.3% | 28.8% | 1.04 (0–3) | 3.76 (0–15) | 0.53zł (0.0–2.7) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 5.62 Er (1–9) | 2.8% | 28.7% | 1.03 (0–3) | 3.71 (0–15) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 5.66 Er (1–9) | 4.1% | 28.8% | 1.04 (0–4) | 3.78 (0–18) | 0.53zł (0.0–2.7) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 5.89 Er (2–9) | 4.3% | 29.4% | 1.07 (0–3) | 4.04 (0–16) | 0.53zł (0.0–2.7) | 6.44 (1.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 4.95 Er (1–9) | 2.0% | 27.1% | 0.92 (0–3) | 3.03 (0–15) | 0.56zł (0.0–3.0) | 5.72 (0.6–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 5.80 Er (2–9) | 3.7% | 29.2% | 1.06 (0–3) | 3.93 (0–15) | 0.53zł (0.0–2.7) | 6.39 (1.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 5.10 Er (1–9) | 2.5% | 27.5% | 0.94 (0–3) | 3.22 (0–15) | 0.56zł (0.0–3.0) | 5.82 (0.6–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 5.72 Er (1–9) | 3.8% | 28.9% | 1.04 (0–3) | 3.85 (0–16) | 0.53zł (0.0–2.7) | 6.32 (1.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 5.48 Er (1–9) | 2.7% | 28.3% | 1.01 (0–3) | 3.54 (0–15) | 0.52zł (0.0–2.7) | 6.17 (1.2–10.0) | 🟢 W NORMIE |

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.