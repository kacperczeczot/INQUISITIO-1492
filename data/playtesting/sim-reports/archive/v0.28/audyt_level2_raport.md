[Strona główna](../../../../../README.md) > [v0.28](README.md) > [audyt_level2_raport](audyt_level2_raport.md)

---

# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.28

**Wersja Balansu:** `v0.28` | **Data:** 2026-08-14 18:30 | **Przeanalizowano Wariantów:** 28 | **Próba:** 3000 gier/setup | **Czas:** 175.65s
**Wynik Bazy Poziomu 2 (Global):** `🟢 95.8 pkt` | 3p: `90.0 pkt` | 4p: `98.4 pkt` | 5p: `99.1 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (7)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🟢 ** 95.8** | 90.0 | 98.4 | 99.1 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 95.8 → 🟢 ** 95.9** (`⬆️ +0.1`) | 90.0 → 89.8 (`-0.2`) | 98.4 → 98.2 (`-0.2`) | 99.1 → 99.7 (`⬆️ +0.6`) | ⚪ OPTYMALNY |
| `L2_CAA_ERA_MINUS1` | Cienie Era: 5 → 4 | 95.8 → 🟢 ** 95.9** (`⬆️ +0.1`) | 90.0 | 98.4 → 98.5 (`⬆️ +0.1`) | 99.1 | ⚪ OPTYMALNY |
| `L2_CAA_ERA_PLUS1` | Cienie Era: 5 → 6 | 95.8 → 🟢 ** 95.4** (`-0.4`) | 90.0 → 90.8 (`⬆️ +0.8`) | 98.4 → 96.3 (`-2.1`) | 99.1 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 3–8 → 3–7 | 95.8 → 🟢 ** 95.1** (`-0.7`) | 90.0 → 87.4 (`-2.6`) | 98.4 | 99.1 → 99.6 (`⬆️ +0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2 → 3 | 95.8 → 🟢 ** 91.8** (`-4.0`) | 90.0 → 92.3 (`⬆️ +2.3`) | 98.4 → 85.4 (`-13.0`) | 99.1 → 97.6 (`-1.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 95.8 → 🟢 ** 87.5** (`-8.3`) | 90.0 → 90.6 (`⬆️ +0.6`) | 98.4 → 91.1 (`-7.3`) | 99.1 → 80.9 (`-18.2`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 21 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 95.8 → 🟢 ** 95.7** (`-0.1`) | 90.0 | 98.4 | 99.1 → 98.7 (`-0.4`) | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–8 → 3–9 | 95.8 → 🟢 ** 95.7** (`-0.1`) | 90.0 → 89.9 (`-0.1`) | 98.4 → 98.3 (`-0.1`) | 99.1 → 98.8 (`-0.3`) | ⚪ OPTYMALNY |
| `L2_KB_ERA_MINUS1` | Korona Era: 6/5/5 → 5/4/4 | 95.8 → 🟢 ** 90.9** (`-4.9`) | 90.0 → 88.1 (`-1.9`) | 98.4 → 85.9 (`-12.5`) | 99.1 → 98.6 (`-0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 3 → 2 | 95.8 → 🟢 ** 81.2** (`-14.6`) | 90.0 → 65.8 (`-24.2`) | 98.4 → 78.7 (`-19.7`) | 99.1 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 3 → 4 | 95.8 → 🟢 ** 81.1** (`-14.7`) | 90.0 → 65.5 (`-24.5`) | 98.4 → 78.7 (`-19.7`) | 99.1 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 95.8 → 🟢 ** 79.8** (`-16.0`) | 90.0 → 84.0 (`-6.0`) | 98.4 → 76.8 (`-21.6`) | 99.1 → 78.7 (`-20.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_PLUS1` | Korona Era: 6/5/5 → 7/6/6 | 95.8 → 🟢 ** 73.9** (`-21.9`) | 90.0 → 59.3 (`-30.7`) | 98.4 → 82.3 (`-16.1`) | 99.1 → 80.0 (`-19.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 7/6/6 → 6/5/5 | 95.8 → 🟢 ** 63.4** (`-32.4`) | 90.0 → 63.2 (`-26.8`) | 98.4 → 63.5 (`-34.9`) | 99.1 → 0.0 (`-99.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 0 → 1 | 95.8 → 🟢 ** 58.8** (`-37.0`) | 90.0 → 78.2 (`-11.8`) | 98.4 → 39.4 (`-59.0`) | 99.1 → 0.0 (`-99.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 3/4/4 → 4/5/5 | 95.8 → 🟢 ** 56.6** (`-39.2`) | 90.0 → 65.1 (`-24.9`) | 98.4 → 55.7 (`-42.7`) | 99.1 → 49.0 (`-50.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 7/6/6 → 8/7/7 | 95.8 → 🟢 ** 54.3** (`-41.5`) | 90.0 → 66.3 (`-23.7`) | 98.4 → 33.6 (`-64.8`) | 99.1 → 63.1 (`-36.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 2 → 3 | 95.8 → 🟢 ** 51.2** (`-44.6`) | 90.0 → 63.1 (`-26.9`) | 98.4 → 39.4 (`-59.0`) | 99.1 → 0.0 (`-99.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 2 → 1 | 95.8 → 🟢 ** 51.2** (`-44.6`) | 90.0 → 63.1 (`-26.9`) | 98.4 → 39.4 (`-59.0`) | 99.1 → 0.0 (`-99.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 3/4/4 → 2/3/3 | 95.8 → 🟡 ** 45.6** (`-50.2`) | 90.0 → 43.6 (`-46.4`) | 98.4 → 47.6 (`-50.8`) | 99.1 → 0.0 (`-99.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 2/3 → 1/2 | 95.8 → 🟡 ** 29.2** (`-66.6`) | 90.0 → 38.9 (`-51.1`) | 98.4 → 19.6 (`-78.8`) | 99.1 → 0.0 (`-99.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 2/3 → 3/4 | 95.8 → 🟡 ** 29.1** (`-66.7`) | 90.0 → 38.5 (`-51.5`) | 98.4 → 19.6 (`-78.8`) | 99.1 → 0.0 (`-99.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2 → 1 | 95.8 → 🟡 ** 28.8** (`-67.0`) | 90.0 → 37.7 (`-52.3`) | 98.4 → 19.8 (`-78.6`) | 99.1 → 0.0 (`-99.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 95.8 → 🟡 ** 28.1** (`-67.7`) | 90.0 → 36.8 (`-53.2`) | 98.4 → 19.5 (`-78.9`) | 99.1 → 0.0 (`-99.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 95.8 → 🟡 ** 28.1** (`-67.7`) | 90.0 → 36.8 (`-53.2`) | 98.4 → 19.5 (`-78.9`) | 99.1 → 0.0 (`-99.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 95.8 → 🟡 ** 28.0** (`-67.8`) | 90.0 → 36.1 (`-53.9`) | 98.4 → 19.9 (`-78.5`) | 99.1 → 0.0 (`-99.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 95.8 → 🟡 ** 28.0** (`-67.8`) | 90.0 → 36.1 (`-53.9`) | 98.4 → 19.9 (`-78.5`) | 99.1 → 0.0 (`-99.1`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (7)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 5.51 Er (1–10) | 1.2% | 26.4% | 1.02 (0–4) | 3.59 (0–19) | 1.04zł (0.0–4.3) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_PLUS1` | 5.52 Er (1–10) | 1.2% | 26.4% | 1.02 (0–4) | 3.61 (0–19) | 1.04zł (0.0–4.3) | 6.32 (0.7–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_MINUS1` | 5.50 Er (1–10) | 1.2% | 26.4% | 1.02 (0–4) | 3.58 (0–19) | 1.04zł (0.0–4.3) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_PLUS1` | 5.52 Er (1–10) | 1.2% | 26.4% | 1.02 (0–4) | 3.60 (0–19) | 1.04zł (0.0–4.3) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 5.54 Er (1–10) | 1.5% | 26.5% | 1.03 (0–4) | 3.63 (0–19) | 1.04zł (0.0–4.7) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 5.53 Er (1–10) | 1.3% | 26.5% | 1.03 (0–4) | 3.61 (0–19) | 1.04zł (0.0–4.3) | 6.32 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.48 Er (1–10) | 1.1% | 26.3% | 1.02 (0–4) | 3.54 (0–19) | 1.03zł (0.0–4.3) | 6.29 (0.7–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 21 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_HERESY_LOW_MINUS1` | 5.50 Er (1–10) | 1.2% | 26.4% | 1.02 (0–4) | 3.58 (0–19) | 1.04zł (0.0–4.3) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 5.49 Er (1–10) | 1.0% | 26.3% | 1.02 (0–4) | 3.56 (0–19) | 1.03zł (0.0–4.3) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_MINUS1` | 5.38 Er (1–10) | 1.2% | 25.9% | 1.00 (0–4) | 3.42 (0–19) | 1.03zł (0.0–4.3) | 6.23 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 5.37 Er (1–10) | 0.9% | 26.0% | 1.00 (0–4) | 3.41 (0–19) | 1.03zł (0.0–4.7) | 6.21 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 5.58 Er (1–10) | 1.4% | 26.6% | 1.03 (0–4) | 3.68 (0–19) | 1.04zł (0.0–4.3) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 5.58 Er (1–10) | 1.6% | 26.7% | 1.03 (0–4) | 3.71 (0–20) | 1.05zł (0.0–4.7) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_PLUS1` | 5.63 Er (1–10) | 1.2% | 26.9% | 1.04 (0–4) | 3.76 (0–19) | 1.08zł (0.0–4.3) | 6.38 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.32 Er (1–10) | 1.0% | 25.6% | 1.00 (0–4) | 3.33 (0–19) | 0.99zł (0.0–4.3) | 6.17 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 5.57 Er (1–10) | 1.3% | 26.7% | 1.03 (0–4) | 3.69 (0–19) | 1.05zł (0.0–4.3) | 6.34 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 5.60 Er (1–10) | 1.4% | 26.7% | 1.04 (0–4) | 3.70 (0–19) | 1.05zł (0.0–4.3) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 5.65 Er (1–10) | 1.5% | 26.9% | 1.04 (0–4) | 3.80 (0–19) | 1.07zł (0.0–4.3) | 6.40 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 5.65 Er (1–10) | 1.3% | 26.8% | 1.05 (0–4) | 3.75 (0–19) | 1.04zł (0.0–4.3) | 6.41 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 5.03 Er (1–10) | 0.9% | 25.2% | 0.94 (0–4) | 3.14 (0–19) | 1.06zł (0.0–4.3) | 5.87 (0.4–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.31 Er (1–10) | 0.8% | 25.7% | 1.00 (0–3) | 3.36 (0–19) | 1.02zł (0.0–4.3) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 4.89 Er (1–10) | 0.7% | 24.7% | 0.92 (0–4) | 2.97 (0–19) | 1.05zł (0.0–4.7) | 5.77 (0.4–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_GC_FALLS_PLUS1` | 5.73 Er (1–10) | 1.6% | 27.0% | 1.06 (0–4) | 3.85 (0–19) | 1.05zł (0.0–4.3) | 6.46 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 4.69 Er (1–10) | 0.6% | 23.2% | 0.90 (0–3) | 2.83 (0–19) | 1.01zł (0.0–4.3) | 5.71 (0.7–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_KB_DECREES_PLUS1` | 5.71 Er (1–10) | 2.4% | 27.2% | 1.05 (0–4) | 3.90 (0–21) | 1.08zł (0.0–4.3) | 6.41 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.22 Er (1–10) | 0.4% | 25.2% | 0.98 (0–3) | 3.16 (0–16) | 1.00zł (0.0–4.3) | 6.11 (0.7–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 5.85 Er (1–10) | 1.9% | 27.4% | 1.07 (0–4) | 3.97 (0–19) | 1.05zł (0.0–5.0) | 6.56 (1.6–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.01 Er (1–10) | 0.4% | 21.7% | 0.80 (0–4) | 2.21 (0–15) | 1.18zł (0.0–4.7) | 4.95 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.