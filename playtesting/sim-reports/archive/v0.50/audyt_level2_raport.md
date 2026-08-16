# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.50

**Wersja Balansu:** `v0.50` | **Data:** 2026-08-16 13:12 | **Przeanalizowano Wariantów:** 29 | **Próba:** 3000 gier/setup | **Czas:** 205.5s
**Wynik Bazy Poziomu 2 (Global):** `🟡 85.6 pkt` | 3p: `82.4 pkt` | 4p: `88.8 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (12)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🟡 ** 85.6** | 82.4 | 88.8 | 0.0 | ⚪ OPTYMALNY |
| `L2_CAA_ERA_MINUS1` | Cienie Era: 5 → 4 | 85.6 → 🟡 ** 85.8** (`⬆️ +0.2`) | 82.4 | 88.8 → 89.2 (`⬆️ +0.4`) | 0.0 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–8 → 3–9 | 85.6 → 🟡 ** 82.5** (`-3.1`) | 82.4 → 71.3 (`-11.1`) | 88.8 → 93.8 (`⬆️ +5.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 3–8 → 3–7 | 85.6 → 🟡 ** 79.1** (`-6.5`) | 82.4 → 84.9 (`⬆️ +2.5`) | 88.8 → 73.2 (`-15.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_PLUS1` | Korona Era: 5/5/5 → 6/6/6 | 85.6 → 🟡 ** 76.8** (`-8.8`) | 82.4 → 87.5 (`⬆️ +5.1`) | 88.8 → 66.1 (`-22.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_MINUS1` | Korona Era: 5/5/5 → 4/4/4 | 85.6 → 🟠 ** 69.5** (`-16.1`) | 82.4 → 79.9 (`-2.5`) | 88.8 → 93.1 (`⬆️ +4.3`) | 0.0 → 35.6 (`⬆️ +35.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 4/4/4 → 5/5/5 | 85.6 → 🟠 ** 65.7** (`-19.9`) | 82.4 → 46.4 (`-36.0`) | 88.8 → 84.8 (`-4.0`) | 0.0 → 66.0 (`⬆️ +66.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2 → 3 | 85.6 → 🟠 ** 64.7** (`-20.9`) | 82.4 → 51.5 (`-30.9`) | 88.8 → 99.1 (`⬆️ +10.3`) | 0.0 → 43.6 (`⬆️ +43.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 6/6/6 → 5/5/5 | 85.6 → 🟠 ** 64.0** (`-21.6`) | 82.4 → 63.0 (`-19.4`) | 88.8 → 75.6 (`-13.2`) | 0.0 → 53.5 (`⬆️ +53.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 6/6/6 → 7/7/7 | 85.6 → 🟠 ** 60.6** (`-25.0`) | 82.4 → 83.2 (`⬆️ +0.8`) | 88.8 → 38.0 (`-50.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 85.6 → 🔴 ** 58.2** (`-27.4`) | 82.4 → 47.6 (`-34.8`) | 88.8 → 77.3 (`-11.5`) | 0.0 → 49.6 (`⬆️ +49.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 4/4/4 → 3/3/3 | 85.6 → 🔴 ** 53.0** (`-32.6`) | 82.4 → 86.2 (`⬆️ +3.8`) | 88.8 → 19.9 (`-68.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 17 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 🟡 ** 85.6** | 82.4 | 88.8 | 0.0 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 🟡 ** 85.6** | 82.4 | 88.8 | 0.0 | ⚪ OPTYMALNY |
| `L2_CAA_ERA_PLUS1` | Cienie Era: 5 → 6 | 85.6 → 🟡 ** 81.2** (`-4.4`) | 82.4 → 82.3 (`-0.1`) | 88.8 → 80.0 (`-8.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 3 → 2 | 85.6 → 🟠 ** 73.2** (`-12.4`) | 82.4 → 77.6 (`-4.8`) | 88.8 → 68.9 (`-19.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 3 → 4 | 85.6 → 🟠 ** 65.9** (`-19.7`) | 82.4 → 57.1 (`-25.3`) | 88.8 → 74.7 (`-14.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 2 → 3 | 85.6 → 🔴 ** 46.9** (`-38.7`) | 82.4 → 57.6 (`-24.8`) | 88.8 → 36.2 (`-52.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 2 → 1 | 85.6 → 🔴 ** 46.9** (`-38.7`) | 82.4 → 57.6 (`-24.8`) | 88.8 → 36.2 (`-52.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 85.6 → 🔴 ** 42.0** (`-43.6`) | 82.4 → 64.3 (`-18.1`) | 88.8 → 19.8 (`-69.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 2/3 → 1/2 | 85.6 → 🔴 ** 34.5** (`-51.1`) | 82.4 → 52.9 (`-29.5`) | 88.8 → 16.2 (`-72.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2 → 1 | 85.6 → 🔴 ** 27.3** (`-58.3`) | 82.4 → 34.8 (`-47.6`) | 88.8 → 19.9 (`-68.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 2/3 → 3/4 | 85.6 → 🔴 ** 27.2** (`-58.4`) | 82.4 → 32.4 (`-50.0`) | 88.8 → 22.0 (`-66.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_MINUS1` | Korona Haki: 1 → 0 | 85.6 → 🔴 ** 26.5** (`-59.1`) | 82.4 → 36.1 (`-46.3`) | 88.8 → 16.8 (`-72.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 85.6 → 🔴 ** 26.4** (`-59.2`) | 82.4 → 36.1 (`-46.3`) | 88.8 → 16.6 (`-72.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 85.6 → 🔴 ** 26.4** (`-59.2`) | 82.4 → 36.1 (`-46.3`) | 88.8 → 16.6 (`-72.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 1 → 2 | 85.6 → 🔴 ** 26.4** (`-59.2`) | 82.4 → 36.1 (`-46.3`) | 88.8 → 16.6 (`-72.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 85.6 → 🔴 ** 22.9** (`-62.7`) | 82.4 → 29.4 (`-53.0`) | 88.8 → 16.3 (`-72.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 85.6 → 🔴 ** 22.9** (`-62.7`) | 82.4 → 29.4 (`-53.0`) | 88.8 → 16.3 (`-72.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (12)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 5.80 Er (1–11) | 1.5% | 27.4% | 0.56 (0–3) | 3.72 (0–20) | 1.88zł (0.0–8.7) | 6.34 (1.0–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_MINUS1` | 5.79 Er (1–11) | 1.5% | 27.4% | 0.56 (0–3) | 3.71 (0–20) | 1.87zł (0.0–8.7) | 6.33 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 5.76 Er (1–11) | 1.4% | 27.3% | 0.56 (0–3) | 3.68 (0–20) | 1.86zł (0.0–8.7) | 6.34 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 5.86 Er (1–11) | 1.7% | 27.6% | 0.56 (0–3) | 3.79 (0–20) | 1.90zł (0.0–8.7) | 6.36 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_PLUS1` | 5.88 Er (1–11) | 1.5% | 27.7% | 0.56 (0–3) | 3.82 (0–20) | 1.89zł (0.0–8.7) | 6.38 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_MINUS1` | 5.75 Er (1–11) | 1.5% | 27.2% | 0.56 (0–3) | 3.66 (0–20) | 1.87zł (0.0–8.7) | 6.31 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 5.88 Er (1–11) | 1.7% | 27.7% | 0.56 (0–3) | 3.80 (0–20) | 1.89zł (0.0–8.7) | 6.37 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 5.87 Er (1–11) | 1.8% | 27.6% | 0.56 (0–3) | 3.77 (0–20) | 1.89zł (0.0–8.7) | 6.36 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.67 Er (1–11) | 1.5% | 26.9% | 0.55 (0–3) | 3.55 (0–20) | 1.83zł (0.0–8.7) | 6.26 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 5.92 Er (1–11) | 1.5% | 27.8% | 0.56 (0–3) | 3.87 (0–20) | 1.93zł (0.0–8.7) | 6.40 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.66 Er (1–11) | 1.3% | 26.9% | 0.55 (0–3) | 3.55 (0–20) | 1.83zł (0.0–8.7) | 6.28 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.63 Er (1–11) | 1.1% | 26.8% | 0.55 (0–3) | 3.56 (0–20) | 1.84zł (0.0–8.7) | 6.27 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 17 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_HERESY_LOW_MINUS1` | 5.80 Er (1–11) | 1.5% | 27.4% | 0.56 (0–3) | 3.72 (0–20) | 1.88zł (0.0–8.7) | 6.34 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_PLUS1` | 5.80 Er (1–11) | 1.5% | 27.4% | 0.56 (0–3) | 3.72 (0–20) | 1.88zł (0.0–8.7) | 6.34 (1.0–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_PLUS1` | 5.82 Er (1–11) | 1.5% | 27.5% | 0.56 (0–3) | 3.74 (0–20) | 1.88zł (0.0–8.7) | 6.36 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 5.66 Er (1–11) | 1.3% | 27.0% | 0.56 (0–3) | 3.55 (0–19) | 1.85zł (0.0–8.7) | 6.26 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 5.88 Er (1–11) | 1.8% | 27.6% | 0.56 (0–3) | 3.82 (0–20) | 1.90zł (0.0–8.7) | 6.38 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 5.98 Er (1–11) | 1.9% | 27.8% | 0.57 (0–3) | 3.89 (0–20) | 1.90zł (0.0–8.7) | 6.44 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 5.29 Er (1–11) | 1.1% | 26.4% | 0.52 (0–3) | 3.29 (0–20) | 1.86zł (0.0–8.7) | 5.96 (0.6–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 5.99 Er (1–11) | 2.4% | 28.0% | 0.57 (0–3) | 3.97 (0–20) | 1.96zł (0.0–8.7) | 6.42 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 5.15 Er (1–11) | 0.9% | 26.0% | 0.52 (0–3) | 3.12 (0–19) | 1.83zł (0.0–8.7) | 5.88 (0.6–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 4.72 Er (1–11) | 0.5% | 23.4% | 0.49 (0–3) | 2.87 (0–20) | 1.74zł (0.0–8.7) | 5.73 (1.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_GC_FALLS_PLUS1` | 6.06 Er (1–11) | 2.2% | 28.0% | 0.57 (0–3) | 3.99 (0–20) | 1.92zł (0.0–8.7) | 6.48 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_MINUS1` | 5.57 Er (1–11) | 1.2% | 26.6% | 0.55 (0–3) | 3.44 (0–18) | 1.82zł (0.0–8.7) | 6.24 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.12 Er (1–11) | 4.2% | 28.2% | 0.57 (0–4) | 4.14 (0–22) | 1.98zł (0.0–8.7) | 6.46 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.45 Er (1–11) | 1.2% | 26.2% | 0.54 (0–3) | 3.30 (0–20) | 1.80zł (0.0–8.7) | 6.14 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 6.10 Er (1–11) | 4.2% | 28.2% | 0.57 (0–4) | 4.11 (0–22) | 1.97zł (0.0–8.7) | 6.45 (1.0–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 6.24 Er (1–11) | 2.5% | 28.6% | 0.58 (0–3) | 4.18 (0–20) | 1.96zł (0.0–8.7) | 6.59 (1.7–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.57 Er (1–11) | 0.5% | 23.2% | 0.48 (0–3) | 2.45 (0–17) | 1.77zł (0.0–6.7) | 5.39 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.