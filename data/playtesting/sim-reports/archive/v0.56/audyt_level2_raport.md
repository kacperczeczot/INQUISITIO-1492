[Strona główna](../../../../../README.md) > [v0.56](README.md) > [audyt_level2_raport](audyt_level2_raport.md)

---

# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.56

**Wersja Balansu:** `v0.56` | **Data:** 2026-08-16 14:15 | **Przeanalizowano Wariantów:** 29 | **Próba:** 3000 gier/setup | **Czas:** 222.04s
**Wynik Bazy Poziomu 2 (Global):** `🟠 66.9 pkt` | 3p: `35.6 pkt` | 4p: `94.9 pkt` | 5p: `70.3 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (9)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🟠 ** 66.9** | 35.6 | 94.9 | 70.3 | ⚪ OPTYMALNY |
| `L2_CAA_ERA_PLUS1` | Cienie Era: 5 → 6 | 66.9 → 🟠 ** 67.6** (`⬆️ +0.7`) | 35.6 → 35.4 (`-0.2`) | 94.9 → 94.5 (`-0.4`) | 70.3 → 72.9 (`⬆️ +2.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KB_ERA_MINUS1` | Korona Era: 4/4/4 → 3/3/3 | 66.9 → 🟠 ** 67.4** (`⬆️ +0.5`) | 35.6 → 34.9 (`-0.7`) | 94.9 → 93.8 (`-1.1`) | 70.3 → 73.6 (`⬆️ +3.3`) | ⚪ OPTYMALNY |
| `L2_CAA_ERA_MINUS1` | Cienie Era: 5 → 4 | 66.9 → 🟠 ** 66.7** (`-0.2`) | 35.6 → 35.7 (`⬆️ +0.1`) | 94.9 → 95.0 (`⬆️ +0.1`) | 70.3 → 69.4 (`-0.9`) | ⚪ OPTYMALNY |
| `L2_KB_ERA_PLUS1` | Korona Era: 4/4/4 → 5/5/5 | 66.9 → 🟠 ** 64.6** (`-2.3`) | 35.6 → 38.7 (`⬆️ +3.1`) | 94.9 → 93.6 (`-1.3`) | 70.3 → 61.4 (`-8.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–8 → 3–9 | 66.9 → 🟠 ** 63.5** (`-3.4`) | 35.6 → 27.7 (`-7.9`) | 94.9 → 90.0 (`-4.9`) | 70.3 → 72.9 (`⬆️ +2.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 3–8 → 3–7 | 66.9 → 🟠 ** 60.3** (`-6.6`) | 35.6 → 43.9 (`⬆️ +8.3`) | 94.9 → 88.9 (`-6.0`) | 70.3 → 48.1 (`-22.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 6/6/6 → 7/7/7 | 66.9 → 🔴 ** 48.4** (`-18.5`) | 35.6 → 42.6 (`⬆️ +7.0`) | 94.9 → 54.1 (`-40.8`) | 70.3 → 0.0 (`-70.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 4/4/5 → 3/3/4 | 66.9 → 🔴 ** 29.9** (`-37.0`) | 35.6 → 62.0 (`⬆️ +26.4`) | 94.9 → 19.1 (`-75.8`) | 70.3 → 8.7 (`-61.6`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 20 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 🟠 ** 66.9** | 35.6 | 94.9 | 70.3 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 🟠 ** 66.9** | 35.6 | 94.9 | 70.3 | ⚪ OPTYMALNY |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 3 → 2 | 66.9 → 🔴 ** 58.6** (`-8.3`) | 35.6 → 29.8 (`-5.8`) | 94.9 → 75.8 (`-19.1`) | 70.3 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 3 → 4 | 66.9 → 🔴 ** 55.8** (`-11.1`) | 35.6 → 21.2 (`-14.4`) | 94.9 → 75.8 (`-19.1`) | 70.3 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 6/6/6 → 5/5/5 | 66.9 → 🔴 ** 43.9** (`-23.0`) | 35.6 → 26.6 (`-9.0`) | 94.9 → 56.6 (`-38.3`) | 70.3 → 48.6 (`-21.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 2 → 3 | 66.9 → 🔴 ** 32.6** (`-34.3`) | 35.6 → 26.4 (`-9.2`) | 94.9 → 38.9 (`-56.0`) | 70.3 → 0.0 (`-70.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 2 → 1 | 66.9 → 🔴 ** 32.6** (`-34.3`) | 35.6 → 26.4 (`-9.2`) | 94.9 → 38.9 (`-56.0`) | 70.3 → 0.0 (`-70.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 4/4/5 → 5/5/6 | 66.9 → 🔴 ** 31.7** (`-35.2`) | 35.6 → 25.8 (`-9.8`) | 94.9 → 61.1 (`-33.8`) | 70.3 → 8.3 (`-62.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2 → 3 | 66.9 → 🔴 ** 28.5** (`-38.4`) | 35.6 → 23.5 (`-12.1`) | 94.9 → 61.3 (`-33.6`) | 70.3 → 0.8 (`-69.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2 → 1 | 66.9 → 🔴 ** 20.2** (`-46.7`) | 35.6 → 21.4 (`-14.2`) | 94.9 → 19.1 (`-75.8`) | 70.3 → 0.0 (`-70.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 2/3 → 1/2 | 66.9 → 🔴 ** 20.2** (`-46.7`) | 35.6 → 20.6 (`-15.0`) | 94.9 → 19.9 (`-75.0`) | 70.3 → 0.0 (`-70.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 66.9 → 🔴 ** 19.9** (`-47.0`) | 35.6 → 21.4 (`-14.2`) | 94.9 → 18.5 (`-76.4`) | 70.3 → 0.0 (`-70.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 66.9 → 🔴 ** 19.9** (`-47.0`) | 35.6 → 21.4 (`-14.2`) | 94.9 → 18.5 (`-76.4`) | 70.3 → 0.0 (`-70.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 1 → 2 | 66.9 → 🔴 ** 19.9** (`-47.0`) | 35.6 → 21.4 (`-14.2`) | 94.9 → 18.5 (`-76.4`) | 70.3 → 0.0 (`-70.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_MINUS1` | Korona Haki: 1 → 0 | 66.9 → 🔴 ** 19.9** (`-47.0`) | 35.6 → 21.4 (`-14.2`) | 94.9 → 18.5 (`-76.4`) | 70.3 → 0.0 (`-70.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 66.9 → 🔴 ** 19.9** (`-47.0`) | 35.6 → 14.8 (`-20.8`) | 94.9 → 19.0 (`-75.9`) | 70.3 → 25.8 (`-44.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 66.9 → 🔴 ** 18.9** (`-48.0`) | 35.6 → 18.7 (`-16.9`) | 94.9 → 19.0 (`-75.9`) | 70.3 → 0.0 (`-70.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 2/3 → 3/4 | 66.9 → 🔴 ** 16.0** (`-50.9`) | 35.6 → 12.1 (`-23.5`) | 94.9 → 19.9 (`-75.0`) | 70.3 → 0.0 (`-70.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 66.9 → 🔴 ** 12.1** (`-54.8`) | 35.6 → 5.7 (`-29.9`) | 94.9 → 18.5 (`-76.4`) | 70.3 → 0.0 (`-70.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 66.9 → 🔴 ** 12.1** (`-54.8`) | 35.6 → 5.7 (`-29.9`) | 94.9 → 18.5 (`-76.4`) | 70.3 → 0.0 (`-70.3`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (9)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 5.95 Er (1–11) | 2.0% | 26.8% | 0.39 (0–3) | 3.55 (0–21) | 2.06zł (0.0–8.7) | 6.11 (1.0–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_PLUS1` | 5.97 Er (1–11) | 2.0% | 26.9% | 0.39 (0–3) | 3.56 (0–21) | 2.07zł (0.0–8.7) | 6.13 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_MINUS1` | 5.92 Er (1–11) | 2.0% | 26.8% | 0.39 (0–3) | 3.52 (0–21) | 2.07zł (0.0–8.7) | 6.09 (1.0–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_MINUS1` | 5.93 Er (1–11) | 2.0% | 26.8% | 0.39 (0–3) | 3.54 (0–21) | 2.06zł (0.0–8.7) | 6.10 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_PLUS1` | 6.00 Er (1–11) | 2.0% | 27.0% | 0.39 (0–3) | 3.60 (0–21) | 2.08zł (0.0–8.7) | 6.14 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 5.90 Er (1–11) | 1.8% | 26.7% | 0.39 (0–3) | 3.50 (0–21) | 2.04zł (0.0–8.7) | 6.11 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 6.01 Er (1–11) | 2.2% | 27.0% | 0.39 (0–3) | 3.62 (0–21) | 2.10zł (0.0–8.7) | 6.13 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 6.07 Er (1–11) | 2.1% | 27.3% | 0.39 (0–3) | 3.69 (0–21) | 2.12zł (0.0–8.7) | 6.17 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.79 Er (1–11) | 1.5% | 26.3% | 0.39 (0–3) | 3.43 (0–21) | 2.03zł (0.0–8.7) | 6.06 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 20 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_HERESY_LOW_MINUS1` | 5.95 Er (1–11) | 2.0% | 26.8% | 0.39 (0–3) | 3.55 (0–21) | 2.06zł (0.0–8.7) | 6.11 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_PLUS1` | 5.95 Er (1–11) | 2.0% | 26.8% | 0.39 (0–3) | 3.55 (0–21) | 2.06zł (0.0–8.7) | 6.11 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 5.81 Er (1–11) | 1.8% | 26.4% | 0.39 (0–3) | 3.38 (0–20) | 2.03zł (0.0–8.7) | 6.03 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 6.03 Er (1–11) | 2.3% | 27.0% | 0.39 (0–3) | 3.64 (0–24) | 2.09zł (0.0–9.0) | 6.15 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.82 Er (1–11) | 2.0% | 26.3% | 0.39 (0–3) | 3.41 (0–21) | 2.02zł (0.0–8.7) | 6.04 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 6.15 Er (2–11) | 2.7% | 27.3% | 0.40 (0–3) | 3.70 (0–21) | 2.09zł (0.0–8.7) | 6.20 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 5.37 Er (1–11) | 1.4% | 25.5% | 0.35 (0–3) | 3.13 (0–21) | 2.05zł (0.0–8.7) | 5.71 (0.5–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 6.01 Er (1–11) | 2.4% | 27.0% | 0.39 (0–3) | 3.60 (0–21) | 2.08zł (0.0–8.7) | 6.13 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 6.04 Er (1–11) | 2.6% | 27.1% | 0.39 (0–3) | 3.61 (0–21) | 2.09zł (0.0–8.7) | 6.13 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 4.62 Er (1–11) | 0.6% | 21.3% | 0.34 (0–3) | 2.61 (0–21) | 1.90zł (0.0–8.7) | 5.41 (1.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_GC_FALLS_MINUS1` | 5.23 Er (1–11) | 1.2% | 25.1% | 0.35 (0–3) | 2.97 (0–20) | 2.02zł (0.0–8.7) | 5.63 (0.5–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.35 Er (1–11) | 5.3% | 27.9% | 0.40 (0–3) | 4.03 (0–22) | 2.19zł (0.0–9.3) | 6.26 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.40 Er (1–11) | 1.6% | 24.7% | 0.37 (0–3) | 2.94 (0–21) | 1.93zł (0.0–8.7) | 5.79 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 6.32 Er (1–11) | 5.2% | 27.9% | 0.40 (0–3) | 4.00 (0–22) | 2.19zł (0.0–9.3) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_MINUS1` | 5.58 Er (1–11) | 1.6% | 25.4% | 0.38 (0–3) | 3.14 (0–18) | 1.98zł (0.0–8.7) | 5.96 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.79 Er (1–11) | 1.7% | 26.2% | 0.39 (0–3) | 3.36 (0–20) | 2.01zł (0.0–8.7) | 6.05 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 6.17 Er (1–11) | 3.2% | 27.6% | 0.39 (0–3) | 3.81 (0–21) | 2.16zł (0.0–9.0) | 6.19 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 6.23 Er (2–11) | 3.0% | 27.6% | 0.40 (0–3) | 3.80 (0–24) | 2.12zł (0.0–9.0) | 6.24 (1.0–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 6.41 Er (1–11) | 3.4% | 28.2% | 0.41 (0–3) | 4.00 (0–21) | 2.18zł (0.0–9.0) | 6.35 (1.7–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.67 Er (1–11) | 0.8% | 21.9% | 0.33 (0–3) | 2.31 (0–17) | 1.89zł (0.0–7.7) | 5.20 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.