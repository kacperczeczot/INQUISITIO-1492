# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.23

**Wersja Balansu:** `v0.23` | **Data:** 2026-08-14 14:32 | **Przeanalizowano Wariantów:** 28 | **Próba:** 500 gier/setup | **Czas:** 31.7s
**Wynik Bazy Poziomu 2 (Global):** `🟢 88.6 pkt` | 3p: `78.5 pkt` | 4p: `88.4 pkt` | 5p: `98.8 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (7)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🟢 ** 88.6** | 78.5 | 88.4 | 98.8 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–7 → 4–7 | 88.6 → 🟢 ** 89.7** (`⬆️ +1.1`) | 78.5 → 78.6 (`⬆️ +0.1`) | 88.4 → 91.3 (`⬆️ +2.9`) | 98.8 → 99.1 (`⬆️ +0.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 3–7 → 3–6 | 88.6 → 🟢 ** 89.4** (`⬆️ +0.8`) | 78.5 → 73.7 (`-4.8`) | 88.4 → 95.4 (`⬆️ +7.0`) | 98.8 → 99.1 (`⬆️ +0.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_CAA_ERA_PLUS1` | Cienie Era: 5 → 6 | 🟢 ** 88.6** | 78.5 → 79.2 (`⬆️ +0.7`) | 88.4 → 88.3 (`-0.1`) | 98.8 → 98.4 (`-0.4`) | ⚪ OPTYMALNY |
| `L2_CAA_ERA_MINUS1` | Cienie Era: 5 → 4 | 🟢 ** 88.6** | 78.5 | 88.4 → 88.5 (`⬆️ +0.1`) | 98.8 → 98.9 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–7 → 2–7 | 🟢 ** 88.6** | 78.5 → 78.6 (`⬆️ +0.1`) | 88.4 → 88.5 (`⬆️ +0.1`) | 98.8 → 98.7 (`-0.1`) | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–7 → 3–8 | 88.6 → 🟢 ** 84.0** (`-4.6`) | 78.5 → 80.0 (`⬆️ +1.5`) | 88.4 → 73.5 (`-14.9`) | 98.8 → 98.4 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 21 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2 → 3 | 88.6 → 🟢 ** 84.0** (`-4.6`) | 78.5 → 77.8 (`-0.7`) | 88.4 → 76.0 (`-12.4`) | 98.8 → 98.3 (`-0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_MINUS1` | Korona Era: 6/5/5 → 5/4/4 | 88.6 → 🟢 ** 81.0** (`-7.6`) | 78.5 → 70.4 (`-8.1`) | 88.4 → 74.0 (`-14.4`) | 98.8 → 98.5 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 3 → 4 | 88.6 → 🟢 ** 77.8** (`-10.8`) | 78.5 → 54.3 (`-24.2`) | 88.4 → 80.3 (`-8.1`) | 98.8 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 3 → 2 | 88.6 → 🟢 ** 76.8** (`-11.8`) | 78.5 → 62.8 (`-15.7`) | 88.4 → 68.8 (`-19.6`) | 98.8 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 88.6 → 🟢 ** 76.5** (`-12.1`) | 78.5 → 77.6 (`-0.9`) | 88.4 → 74.9 (`-13.5`) | 98.8 → 76.9 (`-21.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_PLUS1` | Korona Era: 6/5/5 → 7/6/6 | 88.6 → 🟢 ** 71.3** (`-17.3`) | 78.5 → 53.0 (`-25.5`) | 88.4 → 82.4 (`-6.0`) | 98.8 → 78.6 (`-20.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 88.6 → 🟢 ** 67.7** (`-20.9`) | 78.5 → 74.9 (`-3.6`) | 88.4 → 66.3 (`-22.1`) | 98.8 → 61.9 (`-36.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 7/6/6 → 6/5/5 | 88.6 → 🟢 ** 54.7** (`-33.9`) | 78.5 → 60.2 (`-18.3`) | 88.4 → 49.2 (`-39.2`) | 98.8 → 0.0 (`-98.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 3/4/4 → 4/5/5 | 88.6 → 🟢 ** 52.6** (`-36.0`) | 78.5 → 61.7 (`-16.8`) | 88.4 → 36.1 (`-52.3`) | 98.8 → 59.9 (`-38.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 7/6/6 → 8/7/7 | 88.6 → 🟢 ** 51.3** (`-37.3`) | 78.5 → 61.3 (`-17.2`) | 88.4 → 48.8 (`-39.6`) | 98.8 → 43.8 (`-55.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 3/4/4 → 2/3/3 | 88.6 → 🟡 ** 46.0** (`-42.6`) | 78.5 → 41.1 (`-37.4`) | 88.4 → 51.0 (`-37.4`) | 98.8 → 0.0 (`-98.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 0 → 1 | 88.6 → 🟡 ** 45.4** (`-43.2`) | 78.5 → 58.6 (`-19.9`) | 88.4 → 32.1 (`-56.3`) | 98.8 → 0.0 (`-98.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 2 → 3 | 88.6 → 🟡 ** 43.6** (`-45.0`) | 78.5 → 53.1 (`-25.4`) | 88.4 → 34.1 (`-54.3`) | 98.8 → 0.0 (`-98.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 2 → 1 | 88.6 → 🟡 ** 43.6** (`-45.0`) | 78.5 → 53.1 (`-25.4`) | 88.4 → 34.1 (`-54.3`) | 98.8 → 0.0 (`-98.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2 → 1 | 88.6 → 🟡 ** 27.6** (`-61.0`) | 78.5 → 35.5 (`-43.0`) | 88.4 → 19.6 (`-68.8`) | 98.8 → 0.0 (`-98.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 88.6 → 🟡 ** 27.4** (`-61.2`) | 78.5 → 34.9 (`-43.6`) | 88.4 → 19.9 (`-68.5`) | 98.8 → 0.0 (`-98.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 88.6 → 🟡 ** 27.4** (`-61.2`) | 78.5 → 34.9 (`-43.6`) | 88.4 → 19.9 (`-68.5`) | 98.8 → 0.0 (`-98.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 2/3 → 3/4 | 88.6 → 🟡 ** 27.4** (`-61.2`) | 78.5 → 28.9 (`-49.6`) | 88.4 → 26.0 (`-62.4`) | 98.8 → 0.0 (`-98.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 2/3 → 1/2 | 88.6 → 🟡 ** 25.9** (`-62.7`) | 78.5 → 37.4 (`-41.1`) | 88.4 → 14.5 (`-73.9`) | 98.8 → 0.0 (`-98.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 88.6 → 🔴 ** 20.5** (`-68.1`) | 78.5 → 26.4 (`-52.1`) | 88.4 → 14.7 (`-73.7`) | 98.8 → 0.0 (`-98.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 88.6 → 🔴 ** 20.5** (`-68.1`) | 78.5 → 26.4 (`-52.1`) | 88.4 → 14.7 (`-73.7`) | 98.8 → 0.0 (`-98.8`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (7)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 5.67 Er (1–9) | 4.7% | 29.2% | 1.05 (0–4) | 3.55 (0–17) | 0.58zł (0.0–3.0) | 6.06 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_PLUS1` | 5.68 Er (1–9) | 4.9% | 29.3% | 1.05 (0–4) | 3.58 (0–17) | 0.58zł (0.0–3.0) | 6.07 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 5.71 Er (1–9) | 6.2% | 29.4% | 1.05 (0–4) | 3.62 (0–17) | 0.59zł (0.0–3.0) | 6.09 (1.2–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_PLUS1` | 5.68 Er (1–9) | 4.7% | 29.3% | 1.05 (0–4) | 3.56 (0–17) | 0.58zł (0.0–3.0) | 6.07 (1.2–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_MINUS1` | 5.66 Er (1–9) | 4.7% | 29.2% | 1.05 (0–4) | 3.54 (0–17) | 0.58zł (0.0–3.0) | 6.06 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_MINUS1` | 5.66 Er (1–9) | 4.7% | 29.2% | 1.05 (0–4) | 3.54 (0–17) | 0.58zł (0.0–3.0) | 6.06 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 5.64 Er (1–9) | 3.7% | 29.1% | 1.04 (0–4) | 3.50 (0–17) | 0.57zł (0.0–3.0) | 6.05 (1.2–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 21 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_SO_CONDEMNS_PLUS1` | 5.69 Er (1–9) | 5.1% | 29.3% | 1.05 (0–4) | 3.57 (0–17) | 0.58zł (0.0–3.0) | 6.07 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_MINUS1` | 5.55 Er (1–9) | 4.7% | 28.8% | 1.03 (0–4) | 3.40 (0–17) | 0.57zł (0.0–3.0) | 6.00 (1.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 5.73 Er (1–9) | 5.3% | 29.4% | 1.06 (0–4) | 3.64 (0–21) | 0.58zł (0.0–3.0) | 6.10 (1.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 5.53 Er (1–9) | 4.1% | 28.8% | 1.02 (0–4) | 3.38 (0–16) | 0.58zł (0.0–3.0) | 5.97 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.64 Er (1–9) | 4.4% | 29.1% | 1.04 (0–4) | 3.51 (0–17) | 0.58zł (0.0–3.0) | 6.04 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_PLUS1` | 5.79 Er (1–9) | 4.7% | 29.7% | 1.07 (0–4) | 3.73 (0–17) | 0.59zł (0.0–3.0) | 6.14 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 5.74 Er (1–9) | 6.0% | 29.5% | 1.06 (0–4) | 3.66 (0–17) | 0.58zł (0.0–3.0) | 6.11 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.47 Er (1–9) | 4.0% | 28.5% | 1.02 (0–3) | 3.29 (0–17) | 0.58zł (0.0–3.0) | 5.91 (1.2–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 5.76 Er (1–9) | 5.5% | 29.5% | 1.06 (0–4) | 3.66 (0–17) | 0.58zł (0.0–3.0) | 6.10 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 5.81 Er (1–9) | 6.0% | 29.7% | 1.07 (0–4) | 3.77 (0–17) | 0.61zł (0.0–3.0) | 6.16 (1.2–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.50 Er (1–9) | 3.7% | 28.8% | 1.02 (0–4) | 3.35 (0–17) | 0.58zł (0.0–3.0) | 5.97 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 5.74 Er (1–9) | 5.0% | 29.5% | 1.06 (0–4) | 3.67 (0–17) | 0.58zł (0.0–3.0) | 6.10 (1.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 5.82 Er (2–9) | 5.4% | 29.6% | 1.07 (0–4) | 3.70 (0–17) | 0.58zł (0.0–3.0) | 6.16 (1.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 5.15 Er (1–9) | 3.8% | 28.0% | 0.96 (0–4) | 3.09 (0–17) | 0.61zł (0.0–3.0) | 5.65 (0.6–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 4.81 Er (1–9) | 2.3% | 26.3% | 0.91 (0–4) | 2.80 (0–17) | 0.59zł (0.0–3.0) | 5.50 (1.2–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_PLUS1` | 6.04 Er (1–9) | 7.3% | 30.2% | 1.10 (0–4) | 3.95 (0–17) | 0.58zł (0.0–2.7) | 6.32 (1.8–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L2_CAA_RELICS_MINUS1` | 4.05 Er (1–9) | 2.0% | 24.2% | 0.80 (0–3) | 2.14 (0–14) | 0.77zł (0.0–4.0) | 4.71 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_GC_FALLS_PLUS1` | 5.88 Er (2–9) | 6.0% | 29.8% | 1.08 (0–4) | 3.79 (0–21) | 0.58zł (0.0–3.0) | 6.19 (1.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 5.01 Er (1–9) | 3.1% | 27.6% | 0.93 (0–4) | 2.93 (0–16) | 0.61zł (0.0–3.0) | 5.56 (0.6–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 5.87 Er (1–9) | 7.1% | 29.9% | 1.08 (0–4) | 3.87 (0–19) | 0.60zł (0.0–3.0) | 6.17 (1.2–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.33 Er (1–9) | 2.1% | 28.1% | 0.99 (0–4) | 3.06 (0–17) | 0.58zł (0.0–3.0) | 5.83 (1.2–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.