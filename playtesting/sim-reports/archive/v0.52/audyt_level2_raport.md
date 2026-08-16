# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.52

**Wersja Balansu:** `v0.52` | **Data:** 2026-08-16 13:47 | **Przeanalizowano Wariantów:** 29 | **Próba:** 1000 gier/setup | **Czas:** 73.95s
**Wynik Bazy Poziomu 2 (Global):** `🟡 86.7 pkt` | 3p: `74.9 pkt` | 4p: `99.5 pkt` | 5p: `85.7 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (9)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🟡 ** 86.7** | 74.9 | 99.5 | 85.7 | ⚪ OPTYMALNY |
| `L2_KB_ERA_MINUS1` | Korona Era: 5/5/5 → 4/4/4 | 86.7 → 🟡 ** 89.4** (`⬆️ +2.7`) | 74.9 → 72.4 (`-2.5`) | 99.5 | 85.7 → 96.4 (`⬆️ +10.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_CAA_ERA_MINUS1` | Cienie Era: 5 → 4 | 86.7 → 🟡 ** 86.9** (`⬆️ +0.2`) | 74.9 | 99.5 | 85.7 → 86.3 (`⬆️ +0.6`) | ⚪ OPTYMALNY |
| `L2_CAA_ERA_PLUS1` | Cienie Era: 5 → 6 | 🟡 ** 86.7** | 74.9 → 74.7 (`-0.2`) | 99.5 | 85.7 → 86.0 (`⬆️ +0.3`) | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–8 → 3–9 | 86.7 → 🟡 ** 84.0** (`-2.7`) | 74.9 → 67.4 (`-7.5`) | 99.5 → 97.8 (`-1.7`) | 85.7 → 86.8 (`⬆️ +1.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 3–8 → 3–7 | 86.7 → 🟡 ** 82.0** (`-4.7`) | 74.9 → 77.0 (`⬆️ +2.1`) | 99.5 → 98.9 (`-0.6`) | 85.7 → 70.1 (`-15.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_PLUS1` | Korona Era: 5/5/5 → 6/6/6 | 86.7 → 🟡 ** 79.6** (`-7.1`) | 74.9 → 76.9 (`⬆️ +2.0`) | 99.5 → 94.8 (`-4.7`) | 85.7 → 67.0 (`-18.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 6/6/6 → 7/7/7 | 86.7 → 🟠 ** 60.3** (`-26.4`) | 74.9 → 81.7 (`⬆️ +6.8`) | 99.5 → 69.9 (`-29.6`) | 85.7 → 29.4 (`-56.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 4/4/5 → 3/3/4 | 86.7 → 🔴 ** 51.8** (`-34.9`) | 74.9 → 90.7 (`⬆️ +15.8`) | 99.5 → 19.9 (`-79.6`) | 85.7 → 44.9 (`-40.8`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 20 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 🟡 ** 86.7** | 74.9 | 99.5 | 85.7 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 🟡 ** 86.7** | 74.9 | 99.5 | 85.7 | ⚪ OPTYMALNY |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 3 → 2 | 86.7 → 🟡 ** 78.5** (`-8.2`) | 74.9 → 70.2 (`-4.7`) | 99.5 → 79.6 (`-19.9`) | 85.7 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 6/6/6 → 5/5/5 | 86.7 → 🟡 ** 78.1** (`-8.6`) | 74.9 → 68.7 (`-6.2`) | 99.5 → 81.0 (`-18.5`) | 85.7 → 84.7 (`-1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 3 → 4 | 86.7 → 🟠 ** 74.6** (`-12.1`) | 74.9 → 54.4 (`-20.5`) | 99.5 → 83.6 (`-15.9`) | 85.7 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2 → 3 | 86.7 → 🟠 ** 64.0** (`-22.7`) | 74.9 → 41.9 (`-33.0`) | 99.5 → 91.4 (`-8.1`) | 85.7 → 58.7 (`-27.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 4/4/5 → 5/5/6 | 86.7 → 🟠 ** 63.2** (`-23.5`) | 74.9 → 48.0 (`-26.9`) | 99.5 → 85.8 (`-13.7`) | 85.7 → 55.7 (`-30.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 86.7 → 🔴 ** 54.0** (`-32.7`) | 74.9 → 44.9 (`-30.0`) | 99.5 → 52.5 (`-47.0`) | 85.7 → 64.7 (`-21.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 2 → 1 | 86.7 → 🔴 ** 45.5** (`-41.2`) | 74.9 → 51.1 (`-23.8`) | 99.5 → 39.8 (`-59.7`) | 85.7 → 0.0 (`-85.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 2 → 3 | 86.7 → 🔴 ** 44.0** (`-42.7`) | 74.9 → 51.1 (`-23.8`) | 99.5 → 39.8 (`-59.7`) | 85.7 → 41.2 (`-44.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 86.7 → 🔴 ** 37.4** (`-49.3`) | 74.9 → 54.7 (`-20.2`) | 99.5 → 20.1 (`-79.4`) | 85.7 → 0.0 (`-85.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 2/3 → 1/2 | 86.7 → 🔴 ** 33.2** (`-53.5`) | 74.9 → 46.4 (`-28.5`) | 99.5 → 20.0 (`-79.5`) | 85.7 → 0.0 (`-85.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 2/3 → 3/4 | 86.7 → 🔴 ** 31.9** (`-54.8`) | 74.9 → 30.6 (`-44.3`) | 99.5 → 23.9 (`-75.6`) | 85.7 → 41.2 (`-44.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 86.7 → 🔴 ** 27.8** (`-58.9`) | 74.9 → 35.6 (`-39.3`) | 99.5 → 20.0 (`-79.5`) | 85.7 → 0.0 (`-85.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 86.7 → 🔴 ** 27.8** (`-58.9`) | 74.9 → 35.6 (`-39.3`) | 99.5 → 20.0 (`-79.5`) | 85.7 → 0.0 (`-85.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 1 → 2 | 86.7 → 🔴 ** 27.8** (`-58.9`) | 74.9 → 35.6 (`-39.3`) | 99.5 → 20.0 (`-79.5`) | 85.7 → 0.0 (`-85.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_MINUS1` | Korona Haki: 1 → 0 | 86.7 → 🔴 ** 27.8** (`-58.9`) | 74.9 → 35.6 (`-39.3`) | 99.5 → 20.0 (`-79.5`) | 85.7 → 0.0 (`-85.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2 → 1 | 86.7 → 🔴 ** 27.6** (`-59.1`) | 74.9 → 35.2 (`-39.7`) | 99.5 → 19.9 (`-79.6`) | 85.7 → 0.0 (`-85.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 86.7 → 🔴 ** 21.2** (`-65.5`) | 74.9 → 22.6 (`-52.3`) | 99.5 → 19.9 (`-79.6`) | 85.7 → 0.0 (`-85.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 86.7 → 🔴 ** 21.2** (`-65.5`) | 74.9 → 22.6 (`-52.3`) | 99.5 → 19.9 (`-79.6`) | 85.7 → 0.0 (`-85.7`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (9)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 5.99 Er (1–11) | 1.9% | 27.2% | 0.40 (0–4) | 3.58 (0–18) | 1.89zł (0.0–8.7) | 6.21 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_MINUS1` | 5.94 Er (1–11) | 1.9% | 27.0% | 0.40 (0–4) | 3.52 (0–18) | 1.88zł (0.0–8.7) | 6.17 (1.0–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_MINUS1` | 5.97 Er (1–11) | 1.9% | 27.1% | 0.40 (0–4) | 3.57 (0–18) | 1.89zł (0.0–8.7) | 6.20 (1.0–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_PLUS1` | 6.01 Er (1–11) | 1.9% | 27.2% | 0.40 (0–4) | 3.60 (0–18) | 1.90zł (0.0–8.7) | 6.22 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 5.95 Er (1–11) | 1.7% | 27.0% | 0.40 (0–4) | 3.53 (0–18) | 1.87zł (0.0–8.7) | 6.20 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 6.05 Er (1–11) | 2.0% | 27.4% | 0.40 (0–4) | 3.65 (0–18) | 1.92zł (0.0–8.7) | 6.22 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_PLUS1` | 6.07 Er (1–11) | 1.9% | 27.4% | 0.40 (0–4) | 3.67 (0–18) | 1.91zł (0.0–8.7) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 6.11 Er (1–11) | 1.9% | 27.6% | 0.40 (0–4) | 3.73 (0–18) | 1.95zł (0.0–8.7) | 6.26 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.83 Er (1–11) | 1.4% | 26.6% | 0.40 (0–3) | 3.46 (0–18) | 1.86zł (0.0–8.7) | 6.15 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 20 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_HERESY_LOW_MINUS1` | 5.99 Er (1–11) | 1.9% | 27.2% | 0.40 (0–4) | 3.58 (0–18) | 1.89zł (0.0–8.7) | 6.21 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_PLUS1` | 5.99 Er (1–11) | 1.9% | 27.2% | 0.40 (0–4) | 3.58 (0–18) | 1.89zł (0.0–8.7) | 6.21 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 5.84 Er (1–11) | 1.6% | 26.7% | 0.40 (0–4) | 3.41 (0–18) | 1.86zł (0.0–8.7) | 6.12 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.86 Er (1–11) | 1.8% | 26.7% | 0.40 (0–4) | 3.44 (0–18) | 1.85zł (0.0–8.7) | 6.13 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 6.07 Er (1–11) | 2.2% | 27.4% | 0.40 (0–4) | 3.68 (0–18) | 1.91zł (0.0–8.7) | 6.24 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 6.08 Er (1–11) | 2.3% | 27.5% | 0.40 (0–4) | 3.65 (0–18) | 1.92zł (0.0–8.7) | 6.22 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 6.05 Er (1–11) | 2.2% | 27.4% | 0.40 (0–4) | 3.63 (0–18) | 1.91zł (0.0–8.7) | 6.23 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.83 Er (1–11) | 1.6% | 26.6% | 0.40 (0–4) | 3.40 (0–18) | 1.84zł (0.0–8.7) | 6.14 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 5.40 Er (1–11) | 1.4% | 25.8% | 0.36 (0–4) | 3.16 (0–18) | 1.89zł (0.0–8.7) | 5.78 (0.6–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 6.20 Er (2–11) | 2.3% | 27.7% | 0.41 (0–4) | 3.75 (0–18) | 1.92zł (0.0–8.7) | 6.31 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 6.21 Er (1–11) | 3.1% | 27.9% | 0.40 (0–4) | 3.85 (0–19) | 1.99zł (0.0–8.7) | 6.29 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 5.26 Er (1–11) | 1.1% | 25.4% | 0.36 (0–4) | 2.99 (0–18) | 1.86zł (0.0–8.7) | 5.69 (0.6–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 6.28 Er (2–11) | 2.7% | 27.9% | 0.41 (0–4) | 3.85 (0–18) | 1.94zł (0.0–8.7) | 6.34 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.33 Er (1–11) | 4.9% | 28.1% | 0.41 (0–4) | 4.00 (0–22) | 2.00zł (0.0–8.7) | 6.32 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.61 Er (1–11) | 1.4% | 25.8% | 0.39 (0–4) | 3.15 (0–17) | 1.81zł (0.0–8.7) | 5.99 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 6.31 Er (1–11) | 4.9% | 28.0% | 0.41 (0–4) | 3.97 (0–22) | 2.00zł (0.0–8.7) | 6.31 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_MINUS1` | 5.74 Er (1–11) | 1.5% | 26.3% | 0.39 (0–3) | 3.30 (0–18) | 1.83zł (0.0–8.7) | 6.11 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 4.64 Er (1–11) | 0.5% | 21.6% | 0.35 (0–3) | 2.62 (0–18) | 1.75zł (0.0–8.7) | 5.47 (1.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_PLUS1` | 6.48 Er (1–11) | 3.3% | 28.5% | 0.42 (0–4) | 4.06 (0–19) | 1.99zł (0.0–8.7) | 6.46 (2.0–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.68 Er (1–11) | 0.6% | 22.4% | 0.34 (0–3) | 2.32 (0–16) | 1.78zł (0.0–6.7) | 5.25 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.