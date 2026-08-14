# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.29

**Wersja Balansu:** `v0.29` | **Data:** 2026-08-14 23:01 | **Przeanalizowano Wariantów:** 28 | **Próba:** 20000 gier/setup | **Czas:** 1163.95s
**Wynik Bazy Poziomu 2 (Global):** `🟢 96.2 pkt` | 3p: `91.5 pkt` | 4p: `98.3 pkt` | 5p: `98.9 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (4)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🟢 ** 96.2** | 91.5 | 98.3 | 98.9 | ⚪ OPTYMALNY |
| `L2_CAA_ERA_PLUS1` | Cienie Era: 5 → 6 | 96.2 → 🟢 ** 95.6** (`-0.6`) | 91.5 → 91.7 (`⬆️ +0.2`) | 98.3 → 96.2 (`-2.1`) | 98.9 → 99.0 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2 → 3 | 96.2 → 🟢 ** 91.2** (`-5.0`) | 91.5 → 91.6 (`⬆️ +0.1`) | 98.3 → 83.7 (`-14.6`) | 98.9 → 98.2 (`-0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_MINUS1` | Korona Era: 6/5/5 → 5/4/4 | 96.2 → 🟢 ** 89.2** (`-7.0`) | 91.5 → 88.7 (`-2.8`) | 98.3 → 79.1 (`-19.2`) | 98.9 → 99.7 (`⬆️ +0.8`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 24 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_MINUS1` | Cienie Era: 5 → 4 | 🟢 ** 96.2** | 91.5 → 91.4 (`-0.1`) | 98.3 | 98.9 → 98.8 (`-0.1`) | ⚪ OPTYMALNY |
| `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 96.2 → 🟢 ** 96.1** (`-0.1`) | 91.5 | 98.3 → 98.2 (`-0.1`) | 98.9 → 98.7 (`-0.2`) | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–8 → 3–9 | 96.2 → 🟢 ** 95.6** (`-0.6`) | 91.5 → 89.9 (`-1.6`) | 98.3 → 98.1 (`-0.2`) | 98.9 → 98.8 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 96.2 → 🟢 ** 95.5** (`-0.7`) | 91.5 → 90.2 (`-1.3`) | 98.3 → 98.1 (`-0.2`) | 98.9 → 98.1 (`-0.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 3–8 → 3–7 | 96.2 → 🟢 ** 95.1** (`-1.1`) | 91.5 → 88.2 (`-3.3`) | 98.3 | 98.9 → 98.8 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 96.2 → 🟢 ** 89.4** (`-6.8`) | 91.5 → 90.6 (`-0.9`) | 98.3 → 90.8 (`-7.5`) | 98.9 → 86.8 (`-12.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 3 → 4 | 96.2 → 🟢 ** 81.7** (`-14.5`) | 91.5 → 67.7 (`-23.8`) | 98.3 → 78.6 (`-19.7`) | 98.9 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 3 → 2 | 96.2 → 🟢 ** 81.6** (`-14.6`) | 91.5 → 67.2 (`-24.3`) | 98.3 → 78.6 (`-19.7`) | 98.9 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 96.2 → 🟢 ** 74.3** (`-21.9`) | 91.5 → 80.1 (`-11.4`) | 98.3 → 71.2 (`-27.1`) | 98.9 → 71.6 (`-27.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_PLUS1` | Korona Era: 6/5/5 → 7/6/6 | 96.2 → 🟢 ** 69.3** (`-26.9`) | 91.5 → 57.8 (`-33.7`) | 98.3 → 79.6 (`-18.7`) | 98.9 → 70.5 (`-28.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 7/6/6 → 6/5/5 | 96.2 → 🟢 ** 61.9** (`-34.3`) | 91.5 → 64.7 (`-26.8`) | 98.3 → 59.1 (`-39.2`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 0 → 1 | 96.2 → 🟢 ** 57.0** (`-39.2`) | 91.5 → 74.8 (`-16.7`) | 98.3 → 39.3 (`-59.0`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 3/4/4 → 4/5/5 | 96.2 → 🟢 ** 54.1** (`-42.1`) | 91.5 → 64.7 (`-26.8`) | 98.3 → 43.9 (`-54.4`) | 98.9 → 53.8 (`-45.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 2 → 3 | 96.2 → 🟢 ** 51.9** (`-44.3`) | 91.5 → 64.5 (`-27.0`) | 98.3 → 39.3 (`-59.0`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 2 → 1 | 96.2 → 🟢 ** 51.9** (`-44.3`) | 91.5 → 64.5 (`-27.0`) | 98.3 → 39.3 (`-59.0`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 3/4/4 → 2/3/3 | 96.2 → 🟡 ** 47.4** (`-48.8`) | 91.5 → 44.2 (`-47.3`) | 98.3 → 50.5 (`-47.8`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 7/6/6 → 8/7/7 | 96.2 → 🟡 ** 45.7** (`-50.5`) | 91.5 → 62.4 (`-29.1`) | 98.3 → 30.9 (`-67.4`) | 98.9 → 43.7 (`-55.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 2/3 → 3/4 | 96.2 → 🟡 ** 30.1** (`-66.1`) | 91.5 → 40.6 (`-50.9`) | 98.3 → 19.6 (`-78.7`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 2/3 → 1/2 | 96.2 → 🟡 ** 29.9** (`-66.3`) | 91.5 → 40.2 (`-51.3`) | 98.3 → 19.6 (`-78.7`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2 → 1 | 96.2 → 🟡 ** 29.0** (`-67.2`) | 91.5 → 38.4 (`-53.1`) | 98.3 → 19.7 (`-78.6`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 96.2 → 🟡 ** 28.3** (`-67.9`) | 91.5 → 36.9 (`-54.6`) | 98.3 → 19.7 (`-78.6`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 96.2 → 🟡 ** 28.3** (`-67.9`) | 91.5 → 36.9 (`-54.6`) | 98.3 → 19.7 (`-78.6`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 96.2 → 🟡 ** 27.8** (`-68.4`) | 91.5 → 36.1 (`-55.4`) | 98.3 → 19.5 (`-78.8`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 96.2 → 🟡 ** 27.8** (`-68.4`) | 91.5 → 36.1 (`-55.4`) | 98.3 → 19.5 (`-78.8`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (4)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 5.51 Er (1–10) | 1.1% | 26.2% | 1.03 (0–4) | 3.57 (0–19) | 1.16zł (0.0–5.0) | 6.30 (0.3–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_PLUS1` | 5.52 Er (1–10) | 1.1% | 26.2% | 1.03 (0–4) | 3.58 (0–19) | 1.17zł (0.0–5.0) | 6.31 (0.3–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 5.54 Er (1–10) | 1.2% | 26.3% | 1.03 (0–4) | 3.60 (0–19) | 1.17zł (0.0–5.0) | 6.32 (0.3–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_MINUS1` | 5.39 Er (1–10) | 1.1% | 25.7% | 1.01 (0–4) | 3.41 (0–19) | 1.15zł (0.0–5.0) | 6.23 (0.3–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 24 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_MINUS1` | 5.50 Er (1–10) | 1.1% | 26.1% | 1.03 (0–4) | 3.56 (0–19) | 1.16zł (0.0–5.0) | 6.30 (0.3–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_MINUS1` | 5.51 Er (1–10) | 1.1% | 26.2% | 1.03 (0–4) | 3.57 (0–19) | 1.16zł (0.0–5.0) | 6.30 (0.3–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 5.50 Er (1–10) | 0.9% | 26.1% | 1.03 (0–4) | 3.55 (0–19) | 1.16zł (0.0–5.0) | 6.30 (0.3–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_PLUS1` | 5.52 Er (1–10) | 1.1% | 26.2% | 1.03 (0–4) | 3.60 (0–19) | 1.17zł (0.0–5.0) | 6.31 (0.3–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 5.54 Er (1–10) | 1.4% | 26.3% | 1.03 (0–4) | 3.62 (0–19) | 1.17zł (0.0–5.0) | 6.31 (0.3–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.48 Er (1–10) | 1.0% | 26.1% | 1.02 (0–4) | 3.52 (0–19) | 1.16zł (0.0–5.0) | 6.28 (0.3–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 5.59 Er (1–10) | 1.3% | 26.4% | 1.04 (0–4) | 3.67 (0–20) | 1.18zł (0.0–5.7) | 6.35 (0.3–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 5.37 Er (1–10) | 0.8% | 25.7% | 1.01 (0–4) | 3.39 (0–19) | 1.15zł (0.0–5.0) | 6.20 (0.3–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 5.58 Er (1–10) | 1.5% | 26.5% | 1.04 (0–4) | 3.69 (0–21) | 1.18zł (0.0–5.0) | 6.35 (0.3–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_PLUS1` | 5.63 Er (1–10) | 1.1% | 26.7% | 1.05 (0–4) | 3.75 (0–19) | 1.21zł (0.0–5.0) | 6.38 (0.3–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.33 Er (1–10) | 0.9% | 25.4% | 1.00 (0–4) | 3.32 (0–19) | 1.12zł (0.0–5.0) | 6.16 (0.3–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 5.57 Er (1–10) | 1.2% | 26.5% | 1.04 (0–4) | 3.68 (0–19) | 1.18zł (0.0–5.0) | 6.34 (0.3–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 5.60 Er (1–10) | 1.3% | 26.5% | 1.04 (0–4) | 3.69 (0–19) | 1.17zł (0.0–5.0) | 6.35 (0.3–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 5.66 Er (1–10) | 1.2% | 26.6% | 1.05 (0–4) | 3.74 (0–19) | 1.17zł (0.0–5.0) | 6.41 (0.3–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 5.03 Er (1–10) | 0.9% | 25.0% | 0.95 (0–4) | 3.12 (0–19) | 1.18zł (0.0–5.0) | 5.86 (0.3–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.32 Er (1–10) | 0.8% | 25.5% | 1.00 (0–4) | 3.35 (0–19) | 1.15zł (0.0–5.0) | 6.19 (0.3–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 5.65 Er (1–10) | 1.4% | 26.7% | 1.05 (0–4) | 3.79 (0–19) | 1.20zł (0.0–5.0) | 6.39 (0.3–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 5.74 Er (1–10) | 1.5% | 26.9% | 1.06 (0–4) | 3.84 (0–20) | 1.18zł (0.0–5.7) | 6.46 (0.3–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 4.89 Er (1–10) | 0.6% | 24.5% | 0.93 (0–4) | 2.95 (0–19) | 1.16zł (0.0–5.0) | 5.76 (0.3–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_SO_CONDEMNS_MINUS1` | 4.69 Er (1–10) | 0.6% | 22.9% | 0.90 (0–4) | 2.82 (0–19) | 1.13zł (0.0–5.0) | 5.71 (0.3–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_PLUS1` | 5.86 Er (1–10) | 1.8% | 27.3% | 1.07 (0–4) | 3.96 (0–20) | 1.19zł (0.0–5.3) | 6.56 (1.6–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.01 Er (1–10) | 0.4% | 21.3% | 0.81 (0–4) | 2.19 (0–18) | 1.24zł (0.0–5.0) | 4.94 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_KB_DECREES_PLUS1` | 5.70 Er (1–10) | 2.2% | 26.9% | 1.05 (0–4) | 3.88 (0–21) | 1.21zł (0.0–5.0) | 6.41 (0.3–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.22 Er (1–10) | 0.3% | 25.0% | 0.98 (0–3) | 3.14 (0–18) | 1.13zł (0.0–5.0) | 6.11 (0.3–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.