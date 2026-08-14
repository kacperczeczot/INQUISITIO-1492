# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.12

**Wersja Balansu:** `v0.12` | **Data:** 2026-08-14 11:31 | **Przeanalizowano Wariantów:** 37 | **Próba:** 2000 gier/setup | **Czas:** 120.05s
**Wynik Bazy Poziomu 2 (Global):** `🟢 58.3 pkt` | 3p: `82.8 pkt` | 4p: `55.1 pkt` | 5p: `37.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🟢 ** 58.3** | 82.8 | 55.1 | 37.0 | ⚪ OPTYMALNY |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 3/4/4 → 4/5/5 | 58.3 → 🟡 ** 31.2** (`-27.1`) | 82.8 → 50.3 (`-32.5`) | 55.1 → 12.1 (`-43.0`) | 37.0 → 0.0 (`-37.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 3/4/4 → 2/3/3 | 58.3 → 🟡 ** 38.8** (`-19.5`) | 82.8 → 38.2 (`-44.6`) | 55.1 → 39.4 (`-15.7`) | 37.0 → 0.0 (`-37.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2/3/3 → 3/4/4 | 58.3 → 🟢 ** 58.4** (`⬆️ +0.1`) | 82.8 → 83.2 (`⬆️ +0.4`) | 55.1 | 37.0 | ⚪ OPTYMALNY |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2/3/3 → 1/2/2 | 58.3 → 🟡 ** 47.7** (`-10.6`) | 82.8 → 30.7 (`-52.1`) | 55.1 → 64.7 (`⬆️ +9.6`) | 37.0 → 0.0 (`-37.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 58.3 → 🔴 ** 18.5** (`-39.8`) | 82.8 → 29.6 (`-53.2`) | 55.1 → 7.4 (`-47.7`) | 37.0 → 0.0 (`-37.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 58.3 → 🔴 ** 18.5** (`-39.8`) | 82.8 → 29.6 (`-53.2`) | 55.1 → 7.4 (`-47.7`) | 37.0 → 0.0 (`-37.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_ERA_PLUS1` | Cienie Era: 5/5/5 → 6/6/6 | 58.3 → 🟢 ** 54.4** (`-3.9`) | 82.8 → 82.9 (`⬆️ +0.1`) | 55.1 → 43.0 (`-12.1`) | 37.0 → 37.4 (`⬆️ +0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_ERA_MINUS1` | Cienie Era: 5/5/5 → 4/4/4 | 58.3 → 🟢 ** 58.4** (`⬆️ +0.1`) | 82.8 → 82.9 (`⬆️ +0.1`) | 55.1 → 55.2 (`⬆️ +0.1`) | 37.0 → 37.2 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L2_KB_ERA_PLUS1` | Korona Era: 5/5/5 → 6/6/6 | 58.3 → 🟢 ** 53.7** (`-4.6`) | 82.8 → 70.8 (`-12.0`) | 55.1 → 36.6 (`-18.5`) | 37.0 → 0.0 (`-37.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_MINUS1` | Korona Era: 5/5/5 → 4/4/4 | 58.3 → 🟢 ** 60.6** (`⬆️ +2.3`) | 82.8 → 84.7 (`⬆️ +1.9`) | 55.1 → 51.0 (`-4.1`) | 37.0 → 46.0 (`⬆️ +9.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2/2/2 → 3/3/3 | 58.3 → 🔴 ** 22.2** (`-36.1`) | 82.8 → 35.9 (`-46.9`) | 55.1 → 8.5 (`-46.6`) | 37.0 → 0.0 (`-37.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2/2/2 → 1/1/1 | 58.3 → 🔴 ** 22.2** (`-36.1`) | 82.8 → 35.9 (`-46.9`) | 55.1 → 8.5 (`-46.6`) | 37.0 → 0.0 (`-37.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 1/1/1 → 2/2/2 | 58.3 → 🔴 ** 22.2** (`-36.1`) | 82.8 → 35.9 (`-46.9`) | 55.1 → 8.5 (`-46.6`) | 37.0 → 0.0 (`-37.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_MINUS1` | Korona Haki: 1/1/1 → 0/0/0 | 58.3 → 🟢 ** 71.3** (`⬆️ +13.0`) | 82.8 → 87.0 (`⬆️ +4.2`) | 55.1 → 29.4 (`-25.7`) | 37.0 → 97.6 (`⬆️ +60.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KB_ALT_DECREES_PLUS1` | Korona Alt Dekrety: 1 → 2 | 58.3 → 🟢 ** 58.4** (`⬆️ +0.1`) | 82.8 | 55.1 → 34.0 (`-21.1`) | 37.0 → 0.0 (`-37.0`) | ⚪ OPTYMALNY |
| `L2_KB_ALT_DECREES_MINUS1` | Korona Alt Dekrety: 1 → 0 | 🟢 ** 58.3** | 82.8 | 55.1 | 37.0 | ⚪ OPTYMALNY |
| `L2_KB_ALT_HOOKS_PLUS1` | Korona Alt Haki: 2 → 3 | 58.3 → 🟢 ** 58.5** (`⬆️ +0.2`) | 82.8 | 55.1 → 34.2 (`-20.9`) | 37.0 → 0.0 (`-37.0`) | ⚪ OPTYMALNY |
| `L2_KB_ALT_HOOKS_MINUS1` | Korona Alt Haki: 2 → 1 | 58.3 → 🟢 ** 51.6** (`-6.7`) | 82.8 | 55.1 → 19.4 (`-35.7`) | 37.0 → 52.5 (`⬆️ +15.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ALT_ERA_PLUS1` | Korona Alt Era: 6 → 7 | 58.3 → 🟢 ** 64.2** (`⬆️ +5.9`) | 82.8 | 55.1 → 45.6 (`-9.5`) | 37.0 → 0.0 (`-37.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KB_ALT_ERA_MINUS1` | Korona Alt Era: 6 → 5 | 58.3 → 🟢 ** 57.6** (`-0.7`) | 82.8 | 55.1 → 47.1 (`-8.0`) | 37.0 → 43.0 (`⬆️ +6.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ALT_MINP_PLUS1` | Korona Alt min graczy: 4 → 5 | 58.3 → 🟢 ** 51.3** (`-7.0`) | 82.8 | 55.1 → 34.0 (`-21.1`) | 37.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ALT_MINP_MINUS1` | Korona Alt min graczy: 4 → 3 | 58.3 → 🟢 ** 53.8** (`-4.5`) | 82.8 → 69.4 (`-13.4`) | 55.1 | 37.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3/3/3 → 4/4/4 | 58.3 → 🟢 ** 50.0** (`-8.3`) | 82.8 → 85.5 (`⬆️ +2.7`) | 55.1 → 27.2 (`-27.9`) | 37.0 → 37.3 (`⬆️ +0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3/3/3 → 2/2/2 | 58.3 → 🟢 ** 54.2** (`-4.1`) | 82.8 → 76.0 (`-6.8`) | 55.1 → 32.5 (`-22.6`) | 37.0 → 0.0 (`-37.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 7/6/6 → 8/7/7 | 58.3 → 🟡 ** 32.5** (`-25.8`) | 82.8 → 62.6 (`-20.2`) | 55.1 → 24.6 (`-30.5`) | 37.0 → 10.2 (`-26.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 7/6/6 → 6/5/5 | 58.3 → 🟡 ** 28.9** (`-29.4`) | 82.8 → 44.5 (`-38.3`) | 55.1 → 13.4 (`-41.7`) | 37.0 → 0.0 (`-37.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 58.3 → 🟢 ** 56.5** (`-1.8`) | 82.8 | 55.1 → 52.5 (`-2.6`) | 37.0 → 34.1 (`-2.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 58.3 → 🟢 ** 57.8** (`-0.5`) | 82.8 → 83.4 (`⬆️ +0.6`) | 55.1 → 40.5 (`-14.6`) | 37.0 → 49.4 (`⬆️ +12.4`) | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–8 → 3–9 | 58.3 → 🟢 ** 55.4** (`-2.9`) | 82.8 → 80.0 (`-2.8`) | 55.1 → 52.7 (`-2.4`) | 37.0 → 33.5 (`-3.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 3–8 → 3–7 | 58.3 → 🟢 ** 55.4** (`-2.9`) | 82.8 → 85.7 (`⬆️ +2.9`) | 55.1 → 37.0 (`-18.1`) | 37.0 → 43.6 (`⬆️ +6.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 2/3 → 3/4 | 58.3 → 🟡 ** 29.6** (`-28.7`) | 82.8 → 45.5 (`-37.3`) | 55.1 → 13.8 (`-41.3`) | 37.0 → 0.0 (`-37.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 2/3 → 1/2 | 58.3 → 🟡 ** 28.9** (`-29.4`) | 82.8 → 43.9 (`-38.9`) | 55.1 → 13.8 (`-41.3`) | 37.0 → 0.0 (`-37.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 2 → 3 | 58.3 → 🟡 ** 42.4** (`-15.9`) | 82.8 → 58.9 (`-23.9`) | 55.1 → 25.9 (`-29.2`) | 37.0 → 0.0 (`-37.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 2 → 1 | 58.3 → 🟡 ** 42.4** (`-15.9`) | 82.8 → 58.9 (`-23.9`) | 55.1 → 25.9 (`-29.2`) | 37.0 → 0.0 (`-37.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 3 → 4 | 58.3 → 🟡 ** 49.8** (`-8.5`) | 82.8 → 69.4 (`-13.4`) | 55.1 → 43.0 (`-12.1`) | 37.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 3 → 2 | 58.3 → 🟡 ** 49.3** (`-9.0`) | 82.8 → 67.9 (`-14.9`) | 55.1 → 43.0 (`-12.1`) | 37.0 | 🔴 POGARSZA GLOBALNIE |

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 5.57 Er (1–9) | 3.4% | 28.6% | 1.03 (0–3) | 3.71 (0–20) | 0.52zł (0.0–2.7) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 5.66 Er (1–9) | 4.0% | 28.9% | 1.05 (0–3) | 3.83 (0–20) | 0.53zł (0.0–2.7) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.37 Er (1–9) | 2.6% | 28.0% | 1.01 (0–3) | 3.47 (0–20) | 0.52zł (0.0–2.7) | 6.15 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 5.58 Er (1–9) | 3.6% | 28.6% | 1.04 (0–3) | 3.72 (0–20) | 0.52zł (0.0–2.7) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 5.12 Er (1–9) | 1.9% | 27.1% | 0.97 (0–3) | 3.30 (0–20) | 0.52zł (0.0–3.0) | 5.96 (0.7–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 5.88 Er (1–9) | 5.2% | 29.4% | 1.08 (0–4) | 4.08 (0–20) | 0.53zł (0.0–2.7) | 6.49 (1.6–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.01 Er (1–9) | 1.2% | 23.8% | 0.81 (0–3) | 2.24 (0–20) | 0.69zł (0.0–4.0) | 4.89 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_ERA_PLUS1` | 5.58 Er (1–9) | 3.4% | 28.6% | 1.04 (0–3) | 3.72 (0–20) | 0.52zł (0.0–2.7) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_MINUS1` | 5.56 Er (1–9) | 3.4% | 28.6% | 1.03 (0–3) | 3.70 (0–20) | 0.52zł (0.0–2.7) | 6.25 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_PLUS1` | 5.65 Er (1–9) | 3.4% | 28.8% | 1.05 (0–3) | 3.81 (0–20) | 0.53zł (0.0–2.7) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_MINUS1` | 5.50 Er (1–9) | 3.4% | 28.4% | 1.02 (0–3) | 3.63 (0–20) | 0.52zł (0.0–2.7) | 6.21 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 5.75 Er (1–9) | 5.1% | 29.1% | 1.06 (0–3) | 3.97 (0–20) | 0.54zł (0.0–2.7) | 6.36 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.18 Er (1–9) | 1.5% | 27.2% | 0.97 (0–3) | 3.16 (0–20) | 0.50zł (0.0–2.7) | 5.98 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 5.72 Er (1–9) | 4.8% | 29.1% | 1.06 (0–3) | 3.93 (0–20) | 0.54zł (0.0–2.7) | 6.34 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_MINUS1` | 5.47 Er (1–9) | 3.1% | 28.2% | 1.02 (0–3) | 3.55 (0–18) | 0.51zł (0.0–2.7) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ALT_DECREES_PLUS1` | 5.58 Er (1–9) | 3.5% | 28.6% | 1.04 (0–3) | 3.73 (0–20) | 0.52zł (0.0–2.7) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ALT_DECREES_MINUS1` | 5.57 Er (1–9) | 3.4% | 28.6% | 1.03 (0–3) | 3.71 (0–20) | 0.52zł (0.0–2.7) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ALT_HOOKS_PLUS1` | 5.58 Er (1–9) | 3.5% | 28.6% | 1.04 (0–3) | 3.73 (0–20) | 0.52zł (0.0–2.7) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ALT_HOOKS_MINUS1` | 5.54 Er (1–9) | 3.2% | 28.5% | 1.03 (0–3) | 3.67 (0–20) | 0.52zł (0.0–2.7) | 6.24 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ALT_ERA_PLUS1` | 5.57 Er (1–9) | 3.4% | 28.6% | 1.04 (0–3) | 3.72 (0–20) | 0.52zł (0.0–2.7) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ALT_ERA_MINUS1` | 5.55 Er (1–9) | 3.4% | 28.5% | 1.03 (0–3) | 3.69 (0–20) | 0.52zł (0.0–2.7) | 6.25 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ALT_MINP_PLUS1` | 5.58 Er (1–9) | 3.5% | 28.6% | 1.04 (0–3) | 3.73 (0–20) | 0.52zł (0.0–2.7) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ALT_MINP_MINUS1` | 5.52 Er (1–9) | 2.8% | 28.5% | 1.03 (0–3) | 3.65 (0–20) | 0.52zł (0.0–2.7) | 6.23 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 5.64 Er (1–9) | 4.6% | 28.9% | 1.05 (0–4) | 3.84 (0–20) | 0.53zł (0.0–2.7) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.54 Er (1–9) | 3.2% | 28.5% | 1.03 (0–3) | 3.66 (0–20) | 0.52zł (0.0–2.7) | 6.24 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 5.73 Er (1–9) | 4.2% | 29.2% | 1.06 (0–4) | 3.96 (0–20) | 0.56zł (0.0–2.7) | 6.36 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.36 Er (1–9) | 3.0% | 27.8% | 1.00 (0–3) | 3.41 (0–20) | 0.51zł (0.0–2.7) | 6.10 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_MINUS1` | 5.56 Er (1–9) | 3.4% | 28.6% | 1.03 (0–3) | 3.70 (0–20) | 0.52zł (0.0–2.7) | 6.25 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_PLUS1` | 5.58 Er (1–9) | 3.5% | 28.7% | 1.04 (0–3) | 3.74 (0–20) | 0.53zł (0.0–2.7) | 6.27 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 5.56 Er (1–9) | 3.0% | 28.5% | 1.03 (0–3) | 3.69 (0–18) | 0.52zł (0.0–2.7) | 6.25 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 5.59 Er (1–9) | 4.2% | 28.7% | 1.04 (0–4) | 3.76 (0–20) | 0.53zł (0.0–2.7) | 6.27 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 5.82 Er (2–9) | 4.6% | 29.3% | 1.07 (0–3) | 4.02 (0–20) | 0.53zł (0.0–2.7) | 6.42 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 4.91 Er (1–9) | 2.1% | 26.9% | 0.93 (0–3) | 3.01 (0–20) | 0.55zł (0.0–3.0) | 5.71 (0.4–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 5.73 Er (2–9) | 3.9% | 29.0% | 1.06 (0–3) | 3.90 (0–20) | 0.53zł (0.0–2.7) | 6.37 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 5.05 Er (1–9) | 2.6% | 27.3% | 0.95 (0–3) | 3.21 (0–20) | 0.56zł (0.0–3.0) | 5.81 (0.4–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 5.65 Er (1–9) | 4.0% | 28.8% | 1.05 (0–3) | 3.82 (0–20) | 0.53zł (0.0–2.7) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 5.42 Er (1–9) | 2.8% | 28.2% | 1.01 (0–3) | 3.52 (0–20) | 0.52zł (0.0–2.8) | 6.15 (0.7–10.0) | 🟢 W NORMIE |

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.