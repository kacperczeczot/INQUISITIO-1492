# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v1.0-alpha.133

**Wersja Balansu:** `v1.0-alpha.133` | **Data:** 2026-08-30 08:31 | **Przeanalizowano Wariantów:** 19 | **Próba:** 10000 gier/setup | **Czas:** 14.67s
**Wynik Bazy Poziomu 2 (Global):** `🟡 83.6 pkt` | 3p: `69.8 pkt` | 4p: `91.3 pkt` | 5p: `89.6 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (1)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 83.6 → 🟡 ** 83.6** (`= 0.0`) | 69.8 → 69.8 (`= 0.0`) | 91.3 → 91.3 (`= 0.0`) | 89.6 → 89.6 (`= 0.0`) | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 18 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki: 8/9/9 → 7/8/8 | 83.6 → 🟠 ** 69.1** (`🔻 -14.5`) | 69.8 → 69.8 (`= 0.0`) | 91.3 → 67.9 (`🔻 -23.4`) | 89.6 → 69.7 (`🔻 -19.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 83.6 → 🔴 ** 63.0** (`🔻 -20.6`) | 69.8 → 53.3 (`🔻 -16.5`) | 91.3 → 62.5 (`🔻 -28.8`) | 89.6 → 73.2 (`🔻 -16.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 6/7/8 → 5/6/7 | 83.6 → 🔴 ** 61.8** (`🔻 -21.8`) | 69.8 → 69.8 (`= 0.0`) | 91.3 → 71.9 (`🔻 -19.4`) | 89.6 → 43.8 (`🔻 -45.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki: 8/9/9 → 9/10/10 | 83.6 → 🔴 ** 60.4** (`🔻 -23.2`) | 69.8 → 43.1 (`🔻 -26.7`) | 91.3 → 73.2 (`🔻 -18.1`) | 89.6 → 65.0 (`🔻 -24.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS2` | Kabała Fragmenty: 3 → 1 | 83.6 → 🔴 ** 51.6** (`🔻 -32.0`) | 69.8 → 44.9 (`🔻 -24.9`) | 91.3 → 53.2 (`🔻 -38.1`) | 89.6 → 56.7 (`🔻 -32.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS2` | Gildia Upadki: 8/9/9 → 10/11/11 | 83.6 → 🔴 ** 46.2** (`🔻 -37.4`) | 69.8 → 36.1 (`🔻 -33.7`) | 91.3 → 54.6 (`🔻 -36.7`) | 89.6 → 47.9 (`🔻 -41.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS2` | Gildia Upadki: 8/9/9 → 6/7/7 | 83.6 → 🔴 ** 43.1** (`🔻 -40.5`) | 69.8 → 59.1 (`🔻 -10.7`) | 91.3 → 43.0 (`🔻 -48.3`) | 89.6 → 27.2 (`🔻 -62.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 83.6 → 🔴 ** 35.5** (`🔻 -48.1`) | 69.8 → 38.5 (`🔻 -31.3`) | 91.3 → 36.1 (`🔻 -55.2`) | 89.6 → 31.8 (`🔻 -57.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 83.6 → 🔴 ** 32.2** (`🔻 -51.4`) | 69.8 → 31.3 (`🔻 -38.5`) | 91.3 → 36.0 (`🔻 -55.3`) | 89.6 → 29.2 (`🔻 -60.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS2` | Oficjum Stosy: 6/7/8 → 4/5/6 | 83.6 → 🔴 ** 31.7** (`🔻 -51.9`) | 69.8 → 50.8 (`🔻 -19.0`) | 91.3 → 39.3 (`🔻 -52.0`) | 89.6 → 5.0 (`🔻 -84.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS2` | Cienie Relikwie: 2 → 4 | 83.6 → 🔴 ** 31.3** (`🔻 -52.3`) | 69.8 → 36.4 (`🔻 -33.4`) | 91.3 → 31.5 (`🔻 -59.8`) | 89.6 → 26.0 (`🔻 -63.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 83.6 → 🔴 ** 30.9** (`🔻 -52.7`) | 69.8 → 34.5 (`🔻 -35.3`) | 91.3 → 32.3 (`🔻 -59.0`) | 89.6 → 26.0 (`🔻 -63.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS3` | Gildia Upadki: 8/9/9 → 5/6/6 | 83.6 → 🔴 ** 25.8** (`🔻 -57.8`) | 69.8 → 46.2 (`🔻 -23.6`) | 91.3 → 26.7 (`🔻 -64.6`) | 89.6 → 4.6 (`🔻 -85.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2/3/3 → 1/2/2 | 83.6 → 🔴 ** 23.3** (`🔻 -60.3`) | 69.8 → 48.4 (`🔻 -21.4`) | 91.3 → 21.3 (`🔻 -70.0`) | 89.6 → 0.2 (`🔻 -89.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS3` | Oficjum Stosy: 6/7/8 → 3/4/5 | 83.6 → 🔴 ** 18.7** (`🔻 -64.9`) | 69.8 → 35.7 (`🔻 -34.1`) | 91.3 → 20.4 (`🔻 -70.9`) | 89.6 → 0.1 (`🔻 -89.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 83.6 → 🔴 ** 16.4** (`🔻 -67.2`) | 69.8 → 31.6 (`🔻 -38.2`) | 91.3 → 17.6 (`🔻 -73.7`) | 89.6 → 0.1 (`🔻 -89.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS2` | Oficjum Skazania: 2/3/3 → 0/1/1 | 83.6 → 🔴 ** 16.0** (`🔻 -67.6`) | 69.8 → 29.0 (`🔻 -40.8`) | 91.3 → 19.0 (`🔻 -72.3`) | 89.6 → 0.1 (`🔻 -89.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 83.6 → 🔴 ** 14.6** (`🔻 -69.0`) | 69.8 → 23.9 (`🔻 -45.9`) | 91.3 → 19.8 (`🔻 -71.5`) | 89.6 → 0.1 (`🔻 -89.5`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (1)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 6.37 Er (8–1) | 0.1% | 3.8% | 1.67 (0–0) | 7.40 (0–0) | 10.39zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 18 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_GC_FALLS_MINUS1` | 6.33 Er (8–1) | 0.1% | 3.8% | 1.66 (0–0) | 7.28 (0–0) | 10.32zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 6.54 Er (8–1) | 0.1% | 4.0% | 1.72 (0–0) | 7.70 (0–0) | 10.61zł (0.0–0.0) | 7.21 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 6.32 Er (8–1) | 0.1% | 3.8% | 1.65 (0–0) | 7.26 (0–0) | 10.30zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 6.55 Er (8–1) | 0.1% | 3.8% | 1.71 (0–0) | 7.79 (0–0) | 10.66zł (0.0–0.0) | 7.20 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS2` | 6.61 Er (8–1) | 0.2% | 4.1% | 1.74 (0–0) | 7.81 (0–0) | 10.70zł (0.0–0.0) | 7.24 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS2` | 6.62 Er (8–1) | 0.2% | 3.8% | 1.73 (0–0) | 7.94 (0–0) | 10.77zł (0.0–0.0) | 7.21 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS2` | 6.17 Er (8–1) | 0.1% | 3.8% | 1.62 (0–0) | 6.94 (0–0) | 10.10zł (0.0–0.0) | 7.10 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 6.74 Er (8–1) | 0.2% | 3.9% | 1.78 (0–0) | 8.29 (0–0) | 11.04zł (0.0–0.0) | 7.34 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.71 Er (8–1) | 0.7% | 3.8% | 1.77 (0–0) | 8.27 (0–0) | 10.83zł (0.0–0.0) | 7.29 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS2` | 6.06 Er (8–1) | 0.1% | 3.7% | 1.59 (0–0) | 6.72 (0–0) | 9.93zł (0.0–0.0) | 7.04 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS2` | 6.79 Er (8–1) | 0.3% | 3.9% | 1.80 (0–0) | 8.43 (0–0) | 11.14zł (0.0–0.0) | 7.36 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 6.74 Er (8–1) | 0.2% | 3.8% | 1.77 (0–0) | 8.29 (0–0) | 10.99zł (0.0–0.0) | 7.41 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS3` | 5.94 Er (8–1) | 0.1% | 3.7% | 1.57 (0–0) | 6.51 (0–0) | 9.85zł (0.0–0.0) | 7.02 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 5.88 Er (8–1) | 0.1% | 3.7% | 1.56 (0–0) | 6.43 (0–0) | 9.76zł (0.0–0.0) | 7.04 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS3` | 5.68 Er (8–1) | 0.1% | 3.7% | 1.49 (0–0) | 5.90 (0–0) | 9.35zł (0.0–0.0) | 6.85 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.83 Er (8–1) | 0.0% | 3.5% | 1.16 (0–0) | 4.61 (0–0) | 7.87zł (0.0–0.0) | 5.85 (0.0–0.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_SO_CONDEMNS_MINUS2` | 4.34 Er (8–1) | 0.1% | 3.2% | 0.93 (0–0) | 3.68 (0–0) | 7.92zł (0.0–0.0) | 5.92 (0.0–0.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_KB_DECREES_MINUS1` | 5.24 Er (8–1) | 0.0% | 3.3% | 1.34 (0–0) | 5.12 (0–0) | 8.91zł (0.0–0.0) | 6.39 (0.0–0.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.