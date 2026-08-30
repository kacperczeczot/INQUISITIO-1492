# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v1.0-alpha.105

**Wersja Balansu:** `v1.0-alpha.105` | **Data:** 2026-08-30 01:59 | **Przeanalizowano Wariantów:** 19 | **Próba:** 10000 gier/setup | **Czas:** 8.44s
**Wynik Bazy Poziomu 2 (Global):** `🟠 70.2 pkt` | 3p: `36.0 pkt` | 4p: `90.7 pkt` | 5p: `83.8 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (2)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 70.2 → 🟠 ** 70.2** (`= 0.0`) | 36.0 → 36.0 (`= 0.0`) | 90.7 → 90.7 (`= 0.0`) | 83.8 → 83.8 (`= 0.0`) | ⚪ OPTYMALNY |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 3/3/3 → 2/2/2 | 70.2 → 🔴 ** 20.0** (`🔻 -50.2`) | 36.0 → 40.6 (`⬆️ +4.6`) | 90.7 → 19.2 (`🔻 -71.5`) | 83.8 → 0.1 (`🔻 -83.7`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 17 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki: 8/9/9 → 7/8/8 | 70.2 → 🔴 ** 59.5** (`🔻 -10.7`) | 36.0 → 36.0 (`= 0.0`) | 90.7 → 70.2 (`🔻 -20.5`) | 83.8 → 72.3 (`🔻 -11.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki: 8/9/9 → 9/10/10 | 70.2 → 🔴 ** 51.9** (`🔻 -18.3`) | 36.0 → 20.4 (`🔻 -15.6`) | 90.7 → 75.9 (`🔻 -14.8`) | 83.8 → 59.4 (`🔻 -24.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 70.2 → 🔴 ** 49.9** (`🔻 -20.3`) | 36.0 → 25.5 (`🔻 -10.5`) | 90.7 → 64.0 (`🔻 -26.7`) | 83.8 → 60.3 (`🔻 -23.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 6/7/8 → 5/6/7 | 70.2 → 🔴 ** 46.5** (`🔻 -23.7`) | 36.0 → 36.0 (`= 0.0`) | 90.7 → 74.2 (`🔻 -16.5`) | 83.8 → 29.3 (`🔻 -54.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS2` | Kabała Fragmenty: 3 → 1 | 70.2 → 🔴 ** 41.9** (`🔻 -28.3`) | 36.0 → 23.9 (`🔻 -12.1`) | 90.7 → 54.6 (`🔻 -36.1`) | 83.8 → 47.3 (`🔻 -36.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS2` | Gildia Upadki: 8/9/9 → 10/11/11 | 70.2 → 🔴 ** 39.3** (`🔻 -30.9`) | 36.0 → 16.4 (`🔻 -19.6`) | 90.7 → 57.1 (`🔻 -33.6`) | 83.8 → 44.5 (`🔻 -39.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS2` | Gildia Upadki: 8/9/9 → 6/7/7 | 70.2 → 🔴 ** 33.3** (`🔻 -36.9`) | 36.0 → 31.4 (`🔻 -4.6`) | 90.7 → 46.1 (`🔻 -44.6`) | 83.8 → 22.3 (`🔻 -61.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 70.2 → 🔴 ** 27.9** (`🔻 -42.3`) | 36.0 → 15.6 (`🔻 -20.4`) | 90.7 → 35.8 (`🔻 -54.9`) | 83.8 → 32.3 (`🔻 -51.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 70.2 → 🔴 ** 26.3** (`🔻 -43.9`) | 36.0 → 14.5 (`🔻 -21.5`) | 90.7 → 35.8 (`🔻 -54.9`) | 83.8 → 28.6 (`🔻 -55.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 70.2 → 🔴 ** 25.2** (`🔻 -45.0`) | 36.0 → 17.6 (`🔻 -18.4`) | 90.7 → 32.4 (`🔻 -58.3`) | 83.8 → 25.7 (`🔻 -58.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS2` | Oficjum Stosy: 6/7/8 → 4/5/6 | 70.2 → 🔴 ** 24.8** (`🔻 -45.4`) | 36.0 → 31.2 (`🔻 -4.8`) | 90.7 → 39.3 (`🔻 -51.4`) | 83.8 → 4.0 (`🔻 -79.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS2` | Cienie Relikwie: 2 → 4 | 70.2 → 🔴 ** 23.3** (`🔻 -46.9`) | 36.0 → 13.8 (`🔻 -22.2`) | 90.7 → 30.3 (`🔻 -60.4`) | 83.8 → 25.9 (`🔻 -57.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS3` | Gildia Upadki: 8/9/9 → 5/6/6 | 70.2 → 🔴 ** 18.5** (`🔻 -51.7`) | 36.0 → 24.5 (`🔻 -11.5`) | 90.7 → 28.2 (`🔻 -62.5`) | 83.8 → 2.9 (`🔻 -80.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS3` | Oficjum Stosy: 6/7/8 → 3/4/5 | 70.2 → 🔴 ** 15.3** (`🔻 -54.9`) | 36.0 → 27.1 (`🔻 -8.9`) | 90.7 → 18.8 (`🔻 -71.9`) | 83.8 → 0.1 (`🔻 -83.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS2` | Oficjum Skazania: 3/3/3 → 1/1/1 | 70.2 → 🔴 ** 14.2** (`🔻 -56.0`) | 36.0 → 25.4 (`🔻 -10.6`) | 90.7 → 17.2 (`🔻 -73.5`) | 83.8 → 0.1 (`🔻 -83.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 70.2 → 🔴 ** 10.2** (`🔻 -60.0`) | 36.0 → 10.9 (`🔻 -25.1`) | 90.7 → 19.5 (`🔻 -71.2`) | 83.8 → 0.1 (`🔻 -83.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 70.2 → 🔴 **  9.3** (`🔻 -60.9`) | 36.0 → 11.4 (`🔻 -24.6`) | 90.7 → 16.4 (`🔻 -74.3`) | 83.8 → 0.1 (`🔻 -83.7`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (2)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 6.29 Er (8–1) | 0.1% | 3.8% | 1.65 (0–0) | 7.46 (0–0) | 8.14zł (0.0–0.0) | 7.21 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 5.78 Er (8–1) | 0.1% | 3.7% | 1.53 (0–0) | 6.41 (0–0) | 7.71zł (0.0–0.0) | 7.06 (0.0–0.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 17 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_GC_FALLS_MINUS1` | 6.26 Er (8–1) | 0.1% | 3.8% | 1.64 (0–0) | 7.35 (0–0) | 8.09zł (0.0–0.0) | 7.19 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 6.48 Er (8–1) | 0.1% | 3.8% | 1.70 (0–0) | 7.86 (0–0) | 8.34zł (0.0–0.0) | 7.24 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 6.47 Er (8–1) | 0.1% | 4.0% | 1.70 (0–0) | 7.78 (0–0) | 8.28zł (0.0–0.0) | 7.27 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 6.25 Er (8–1) | 0.1% | 3.8% | 1.64 (0–0) | 7.33 (0–0) | 8.08zł (0.0–0.0) | 7.19 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS2` | 6.53 Er (8–1) | 0.1% | 4.2% | 1.72 (0–0) | 7.87 (0–0) | 8.33zł (0.0–0.0) | 7.30 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS2` | 6.55 Er (8–1) | 0.1% | 3.8% | 1.71 (0–0) | 8.03 (0–0) | 8.43zł (0.0–0.0) | 7.25 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS2` | 6.10 Er (8–1) | 0.1% | 3.7% | 1.60 (0–0) | 7.00 (0–0) | 7.93zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 6.67 Er (8–1) | 0.2% | 3.8% | 1.77 (0–0) | 8.38 (0–0) | 8.56zł (0.0–0.0) | 7.39 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.63 Er (8–1) | 0.8% | 3.8% | 1.74 (0–0) | 8.32 (0–0) | 8.42zł (0.0–0.0) | 7.33 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 6.63 Er (8–1) | 0.1% | 3.7% | 1.75 (0–0) | 8.31 (0–0) | 8.63zł (0.0–0.0) | 7.46 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS2` | 5.99 Er (8–1) | 0.1% | 3.7% | 1.58 (0–0) | 6.79 (0–0) | 7.84zł (0.0–0.0) | 7.10 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS2` | 6.73 Er (8–1) | 0.3% | 3.8% | 1.78 (0–0) | 8.52 (0–0) | 8.63zł (0.0–0.0) | 7.42 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS3` | 5.87 Er (8–1) | 0.1% | 3.7% | 1.56 (0–0) | 6.58 (0–0) | 7.78zł (0.0–0.0) | 7.07 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS3` | 5.62 Er (8–1) | 0.1% | 3.6% | 1.48 (0–0) | 5.97 (0–0) | 7.43zł (0.0–0.0) | 6.91 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS2` | 4.23 Er (8–1) | 0.1% | 3.2% | 0.85 (0–0) | 3.63 (0–0) | 6.41zł (0.0–0.0) | 5.89 (0.0–0.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_KB_DECREES_MINUS1` | 5.12 Er (8–1) | 0.0% | 3.2% | 1.28 (0–0) | 5.03 (0–0) | 7.02zł (0.0–0.0) | 6.35 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.53 Er (8–1) | 0.0% | 3.5% | 1.07 (0–0) | 4.46 (0–0) | 6.06zł (0.0–0.0) | 5.53 (0.0–0.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.