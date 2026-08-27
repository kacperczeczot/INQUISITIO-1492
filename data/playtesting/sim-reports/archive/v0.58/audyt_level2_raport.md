[Strona główna](../../../../../README.md) > [v0.58](README.md) > [audyt_level2_raport](audyt_level2_raport.md)

---

# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.58

**Wersja Balansu:** `v0.58` | **Data:** 2026-08-16 16:22 | **Przeanalizowano Wariantów:** 29 | **Próba:** 3000 gier/setup | **Czas:** 266.4s
**Wynik Bazy Poziomu 2 (Global):** `🟠 70.6 pkt` | 3p: `76.6 pkt` | 4p: `79.6 pkt` | 5p: `55.5 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (12)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🟠 ** 70.6** | 76.6 | 79.6 | 55.5 | ⚪ OPTYMALNY |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 5 → 6 | 70.6 → 🟡 ** 76.4** (`⬆️ +5.8`) | 76.6 → 65.9 (`-10.7`) | 79.6 → 83.8 (`⬆️ +4.2`) | 55.5 → 79.5 (`⬆️ +24.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2 → 3 | 70.6 → 🟠 ** 72.4** (`⬆️ +1.8`) | 76.6 → 64.0 (`-12.6`) | 79.6 → 83.0 (`⬆️ +3.4`) | 55.5 → 70.2 (`⬆️ +14.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KB_ERA_MINUS1` | Korona Era: 4 → 3 | 70.6 → 🟠 ** 70.8** (`⬆️ +0.2`) | 76.6 → 76.0 (`-0.6`) | 79.6 → 80.0 (`⬆️ +0.4`) | 55.5 → 56.4 (`⬆️ +0.9`) | ⚪ OPTYMALNY |
| `L2_CAA_ERA_MINUS1` | Cienie Era: 5 → 4 | 70.6 → 🟠 ** 70.4** (`-0.2`) | 76.6 → 77.0 (`⬆️ +0.4`) | 79.6 → 79.2 (`-0.4`) | 55.5 → 55.1 (`-0.4`) | ⚪ OPTYMALNY |
| `L2_KB_ERA_PLUS1` | Korona Era: 4 → 5 | 70.6 → 🟠 ** 68.9** (`-1.7`) | 76.6 → 78.3 (`⬆️ +1.7`) | 79.6 → 76.5 (`-3.1`) | 55.5 → 52.0 (`-3.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 3–8 → 3–7 | 70.6 → 🟠 ** 68.3** (`-2.3`) | 76.6 → 82.0 (`⬆️ +5.4`) | 79.6 → 74.8 (`-4.8`) | 55.5 → 48.1 (`-7.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–8 → 3–9 | 70.6 → 🟠 ** 68.1** (`-2.5`) | 76.6 → 66.5 (`-10.1`) | 79.6 → 77.6 (`-2.0`) | 55.5 → 60.2 (`⬆️ +4.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 70.6 → 🟠 ** 67.1** (`-3.5`) | 76.6 → 66.2 (`-10.4`) | 79.6 → 71.0 (`-8.6`) | 55.5 → 64.2 (`⬆️ +8.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 6 → 5 | 70.6 → 🟠 ** 62.8** (`-7.8`) | 76.6 → 65.0 (`-11.6`) | 79.6 → 62.9 (`-16.7`) | 55.5 → 60.4 (`⬆️ +4.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 6 → 7 | 70.6 → 🟠 ** 60.4** (`-10.2`) | 76.6 → 82.8 (`⬆️ +6.2`) | 79.6 → 64.3 (`-15.3`) | 55.5 → 34.2 (`-21.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 5 → 4 | 70.6 → 🔴 ** 50.7** (`-19.9`) | 76.6 → 79.4 (`⬆️ +2.8`) | 79.6 → 52.5 (`-27.1`) | 55.5 → 20.3 (`-35.2`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 17 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 🟠 ** 70.6** | 76.6 | 79.6 | 55.5 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 🟠 ** 70.6** | 76.6 | 79.6 | 55.5 | ⚪ OPTYMALNY |
| `L2_CAA_ERA_PLUS1` | Cienie Era: 5 → 6 | 70.6 → 🟠 ** 69.8** (`-0.8`) | 76.6 → 75.9 (`-0.7`) | 79.6 → 79.5 (`-0.1`) | 55.5 → 54.0 (`-1.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 4 → 3 | 70.6 → 🟠 ** 66.7** (`-3.9`) | 76.6 → 73.1 (`-3.5`) | 79.6 → 71.5 (`-8.1`) | 55.5 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 4 → 5 | 70.6 → 🟠 ** 65.1** (`-5.5`) | 76.6 → 67.6 (`-9.0`) | 79.6 → 72.3 (`-7.3`) | 55.5 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 70.6 → 🔴 ** 57.0** (`-13.6`) | 76.6 → 75.8 (`-0.8`) | 79.6 → 59.5 (`-20.1`) | 55.5 → 35.7 (`-19.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 3 → 2 | 70.6 → 🔴 ** 54.4** (`-16.2`) | 76.6 → 61.4 (`-15.2`) | 79.6 → 63.4 (`-16.2`) | 55.5 → 38.5 (`-17.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 3/4 → 2/3 | 70.6 → 🔴 ** 50.6** (`-20.0`) | 76.6 → 57.9 (`-18.7`) | 79.6 → 55.3 (`-24.3`) | 55.5 → 38.5 (`-17.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 3 → 4 | 70.6 → 🔴 ** 49.8** (`-20.8`) | 76.6 → 63.9 (`-12.7`) | 79.6 → 56.2 (`-23.4`) | 55.5 → 29.3 (`-26.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 3/4 → 4/5 | 70.6 → 🔴 ** 44.3** (`-26.3`) | 76.6 → 54.9 (`-21.7`) | 79.6 → 48.8 (`-30.8`) | 55.5 → 29.3 (`-26.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_MINUS1` | Korona Haki: 1 → 0 | 70.6 → 🔴 ** 41.3** (`-29.3`) | 76.6 → 49.7 (`-26.9`) | 79.6 → 42.0 (`-37.6`) | 55.5 → 32.1 (`-23.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 1 → 2 | 70.6 → 🔴 ** 32.1** (`-38.5`) | 76.6 → 42.3 (`-34.3`) | 79.6 → 31.7 (`-47.9`) | 55.5 → 22.3 (`-33.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 70.6 → 🔴 ** 30.8** (`-39.8`) | 76.6 → 44.1 (`-32.5`) | 79.6 → 29.2 (`-50.4`) | 55.5 → 19.0 (`-36.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 70.6 → 🔴 ** 30.1** (`-40.5`) | 76.6 → 41.3 (`-35.3`) | 79.6 → 28.9 (`-50.7`) | 55.5 → 20.0 (`-35.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 70.6 → 🔴 ** 28.8** (`-41.8`) | 76.6 → 36.2 (`-40.4`) | 79.6 → 30.0 (`-49.6`) | 55.5 → 20.1 (`-35.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2 → 1 | 70.6 → 🔴 ** 17.2** (`-53.4`) | 76.6 → 32.4 (`-44.2`) | 79.6 → 18.9 (`-60.7`) | 55.5 → 0.3 (`-55.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 70.6 → 🔴 ** 14.7** (`-55.9`) | 76.6 → 28.9 (`-47.7`) | 79.6 → 14.8 (`-64.8`) | 55.5 → 0.4 (`-55.1`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (12)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 5.95 Er (2–11) | 1.7% | 26.9% | 1.48 (0–4) | 3.64 (0–21) | 1.98zł (0.0–8.7) | 6.50 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 6.01 Er (2–11) | 2.2% | 27.1% | 1.49 (0–4) | 3.69 (0–21) | 2.00zł (0.0–8.7) | 6.52 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 6.07 Er (2–11) | 2.2% | 27.3% | 1.51 (0–4) | 3.73 (0–21) | 2.01zł (0.0–8.7) | 6.53 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_MINUS1` | 5.92 Er (2–11) | 1.7% | 26.9% | 1.47 (0–4) | 3.61 (0–21) | 1.99zł (0.0–8.7) | 6.47 (1.0–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_MINUS1` | 5.91 Er (2–11) | 1.7% | 26.8% | 1.47 (0–4) | 3.60 (0–21) | 1.97zł (0.0–8.7) | 6.48 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_PLUS1` | 6.00 Er (2–11) | 1.7% | 27.1% | 1.49 (0–4) | 3.69 (0–21) | 1.99zł (0.0–8.7) | 6.53 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 6.03 Er (2–11) | 2.0% | 27.2% | 1.49 (0–4) | 3.74 (0–21) | 2.02zł (0.0–8.7) | 6.52 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 5.89 Er (2–11) | 1.6% | 26.7% | 1.47 (0–4) | 3.56 (0–21) | 1.95zł (0.0–8.7) | 6.49 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.85 Er (2–11) | 1.6% | 26.5% | 1.46 (0–4) | 3.52 (0–21) | 1.95zł (0.0–8.7) | 6.46 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.78 Er (2–11) | 1.7% | 26.2% | 1.40 (0–4) | 3.44 (0–21) | 1.93zł (0.0–8.7) | 6.39 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 6.10 Er (2–11) | 1.8% | 27.5% | 1.51 (0–4) | 3.82 (0–21) | 2.04zł (0.0–8.7) | 6.57 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.82 Er (2–11) | 1.3% | 26.4% | 1.45 (0–4) | 3.53 (0–21) | 1.95zł (0.0–8.7) | 6.46 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 17 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_HERESY_LOW_MINUS1` | 5.95 Er (2–11) | 1.7% | 26.9% | 1.48 (0–4) | 3.64 (0–21) | 1.98zł (0.0–8.7) | 6.50 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_PLUS1` | 5.95 Er (2–11) | 1.7% | 26.9% | 1.48 (0–4) | 3.64 (0–21) | 1.98zł (0.0–8.7) | 6.50 (1.0–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_PLUS1` | 5.99 Er (2–11) | 1.7% | 27.1% | 1.50 (0–4) | 3.68 (0–21) | 2.00zł (0.0–8.7) | 6.53 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 5.83 Er (2–11) | 1.5% | 26.6% | 1.46 (0–4) | 3.48 (0–20) | 1.96zł (0.0–8.3) | 6.44 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 6.03 Er (2–11) | 2.0% | 27.1% | 1.49 (0–4) | 3.73 (0–22) | 2.00zł (0.0–8.7) | 6.53 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 6.13 Er (2–11) | 2.4% | 27.5% | 1.52 (0–4) | 3.85 (0–21) | 2.05zł (0.0–8.7) | 6.57 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 5.67 Er (1–11) | 1.3% | 26.1% | 1.42 (0–4) | 3.40 (0–21) | 1.96zł (0.0–8.7) | 6.34 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 5.55 Er (1–11) | 1.1% | 25.8% | 1.40 (0–4) | 3.25 (0–20) | 1.93zł (0.0–8.3) | 6.28 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 6.10 Er (2–11) | 2.1% | 27.3% | 1.51 (0–4) | 3.76 (0–21) | 2.00zł (0.0–8.7) | 6.57 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 6.18 Er (2–11) | 2.4% | 27.5% | 1.52 (0–4) | 3.86 (0–22) | 2.02zł (0.0–8.7) | 6.60 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_MINUS1` | 5.59 Er (2–11) | 1.3% | 25.5% | 1.38 (0–4) | 3.24 (0–21) | 1.90zł (0.0–8.7) | 6.33 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 6.28 Er (2–11) | 4.3% | 27.9% | 1.56 (0–4) | 4.04 (0–22) | 2.09zł (0.0–9.0) | 6.62 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.40 Er (2–11) | 1.3% | 24.8% | 1.33 (0–4) | 3.03 (0–19) | 1.86zł (0.0–8.7) | 6.16 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.31 Er (2–11) | 4.4% | 27.9% | 1.57 (0–4) | 4.07 (0–24) | 2.09zł (0.0–9.0) | 6.63 (1.0–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 6.38 Er (2–11) | 2.6% | 28.2% | 1.60 (0–4) | 4.09 (0–21) | 2.07zł (0.0–9.0) | 6.76 (2.2–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 4.57 Er (1–11) | 0.7% | 21.1% | 1.09 (0–4) | 2.64 (0–21) | 1.84zł (0.0–8.7) | 5.67 (1.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_MINUS1` | 4.69 Er (1–11) | 0.6% | 21.9% | 1.09 (0–4) | 2.36 (0–18) | 1.82zł (0.0–7.7) | 5.53 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.