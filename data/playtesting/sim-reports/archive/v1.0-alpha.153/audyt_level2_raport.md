# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v1.0-alpha.153

**Wersja Balansu:** `v1.0-alpha.153` | **Data:** 2026-08-30 11:23 | **Przeanalizowano Wariantów:** 19 | **Próba:** 10000 gier/setup | **Czas:** 8.06s
**Wynik Bazy Poziomu 2 (Global):** `🟡 82.4 pkt` | 3p: `69.8 pkt` | 4p: `90.6 pkt` | 5p: `86.9 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (1)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 82.4 → 🟡 ** 82.4** (`= 0.0`) | 69.8 → 69.8 (`= 0.0`) | 90.6 → 90.6 (`= 0.0`) | 86.9 → 86.9 (`= 0.0`) | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 18 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki: 8/9/9 → 7/8/8 | 82.4 → 🟠 ** 67.3** (`🔻 -15.1`) | 69.8 → 69.8 (`= 0.0`) | 90.6 → 63.0 (`🔻 -27.6`) | 86.9 → 69.2 (`🔻 -17.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki: 8/9/9 → 9/10/10 | 82.4 → 🔴 ** 61.8** (`🔻 -20.6`) | 69.8 → 49.9 (`🔻 -19.9`) | 90.6 → 75.0 (`🔻 -15.6`) | 86.9 → 60.6 (`🔻 -26.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 6/7/8 → 5/6/7 | 82.4 → 🔴 ** 61.0** (`🔻 -21.4`) | 69.8 → 69.8 (`= 0.0`) | 90.6 → 76.5 (`🔻 -14.1`) | 86.9 → 36.6 (`🔻 -50.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 82.4 → 🔴 ** 60.8** (`🔻 -21.6`) | 69.8 → 51.4 (`🔻 -18.4`) | 90.6 → 63.3 (`🔻 -27.3`) | 86.9 → 67.6 (`🔻 -19.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS2` | Kabała Fragmenty: 3 → 1 | 82.4 → 🔴 ** 51.0** (`🔻 -31.4`) | 69.8 → 47.5 (`🔻 -22.3`) | 90.6 → 53.1 (`🔻 -37.5`) | 86.9 → 52.4 (`🔻 -34.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS2` | Gildia Upadki: 8/9/9 → 10/11/11 | 82.4 → 🔴 ** 45.8** (`🔻 -36.6`) | 69.8 → 38.5 (`🔻 -31.3`) | 90.6 → 54.9 (`🔻 -35.7`) | 86.9 → 43.9 (`🔻 -43.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS2` | Gildia Upadki: 8/9/9 → 6/7/7 | 82.4 → 🔴 ** 38.2** (`🔻 -44.2`) | 69.8 → 52.6 (`🔻 -17.2`) | 90.6 → 38.9 (`🔻 -51.7`) | 86.9 → 23.2 (`🔻 -63.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 82.4 → 🔴 ** 34.7** (`🔻 -47.7`) | 69.8 → 35.6 (`🔻 -34.2`) | 90.6 → 36.4 (`🔻 -54.2`) | 86.9 → 32.2 (`🔻 -54.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS2` | Oficjum Stosy: 6/7/8 → 4/5/6 | 82.4 → 🔴 ** 33.8** (`🔻 -48.6`) | 69.8 → 58.0 (`🔻 -11.8`) | 90.6 → 40.0 (`🔻 -50.6`) | 86.9 → 3.3 (`🔻 -83.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 82.4 → 🔴 ** 32.7** (`🔻 -49.7`) | 69.8 → 34.1 (`🔻 -35.7`) | 90.6 → 35.6 (`🔻 -55.0`) | 86.9 → 28.3 (`🔻 -58.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 82.4 → 🔴 ** 31.2** (`🔻 -51.2`) | 69.8 → 35.5 (`🔻 -34.3`) | 90.6 → 32.3 (`🔻 -58.3`) | 86.9 → 25.8 (`🔻 -61.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS2` | Cienie Relikwie: 2 → 4 | 82.4 → 🔴 ** 30.0** (`🔻 -52.4`) | 69.8 → 33.2 (`🔻 -36.6`) | 90.6 → 31.0 (`🔻 -59.6`) | 86.9 → 25.9 (`🔻 -61.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2/3/3 → 1/2/2 | 82.4 → 🔴 ** 25.0** (`🔻 -57.4`) | 69.8 → 53.5 (`🔻 -16.3`) | 90.6 → 21.4 (`🔻 -69.2`) | 86.9 → 0.1 (`🔻 -86.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS3` | Gildia Upadki: 8/9/9 → 5/6/6 | 82.4 → 🔴 ** 21.0** (`🔻 -61.4`) | 69.8 → 38.3 (`🔻 -31.5`) | 90.6 → 22.9 (`🔻 -67.7`) | 86.9 → 1.9 (`🔻 -85.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS3` | Oficjum Stosy: 6/7/8 → 3/4/5 | 82.4 → 🔴 ** 19.6** (`🔻 -62.8`) | 69.8 → 38.3 (`🔻 -31.5`) | 90.6 → 20.4 (`🔻 -70.2`) | 86.9 → 0.1 (`🔻 -86.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS2` | Oficjum Skazania: 2/3/3 → 0/1/1 | 82.4 → 🔴 ** 16.4** (`🔻 -66.0`) | 69.8 → 30.3 (`🔻 -39.5`) | 90.6 → 18.8 (`🔻 -71.8`) | 86.9 → 0.1 (`🔻 -86.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 82.4 → 🔴 ** 15.4** (`🔻 -67.0`) | 69.8 → 26.7 (`🔻 -43.1`) | 90.6 → 19.5 (`🔻 -71.1`) | 86.9 → 0.1 (`🔻 -86.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 82.4 → 🔴 ** 15.1** (`🔻 -67.3`) | 69.8 → 28.5 (`🔻 -41.3`) | 90.6 → 16.8 (`🔻 -73.8`) | 86.9 → 0.1 (`🔻 -86.8`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (1)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 6.26 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 7.26 (0–0) | 7.05zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 18 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_GC_FALLS_MINUS1` | 6.21 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.14 (0–0) | 7.00zł (0.0–0.0) | 7.13 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 6.46 Er (8–1) | 0.1% | 2.5% | 1.70 (0–0) | 7.67 (0–0) | 7.27zł (0.0–0.0) | 7.18 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 6.21 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.14 (0–0) | 6.99zł (0.0–0.0) | 7.12 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 6.43 Er (8–1) | 0.1% | 2.8% | 1.71 (0–0) | 7.60 (0–0) | 7.19zł (0.0–0.0) | 7.21 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS2` | 6.51 Er (8–1) | 0.1% | 2.9% | 1.73 (0–0) | 7.71 (0–0) | 7.24zł (0.0–0.0) | 7.24 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS2` | 6.53 Er (8–1) | 0.2% | 2.5% | 1.72 (0–0) | 7.83 (0–0) | 7.35zł (0.0–0.0) | 7.19 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS2` | 6.01 Er (8–1) | 0.1% | 2.4% | 1.59 (0–0) | 6.72 (0–0) | 6.79zł (0.0–0.0) | 7.07 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 6.62 Er (8–1) | 0.2% | 2.5% | 1.76 (0–0) | 8.14 (0–0) | 7.45zł (0.0–0.0) | 7.32 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS2` | 5.96 Er (8–1) | 0.1% | 2.5% | 1.58 (0–0) | 6.62 (0–0) | 6.77zł (0.0–0.0) | 7.02 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.59 Er (8–1) | 0.6% | 2.5% | 1.75 (0–0) | 8.11 (0–0) | 7.35zł (0.0–0.0) | 7.28 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 6.61 Er (8–1) | 0.2% | 2.4% | 1.75 (0–0) | 8.14 (0–0) | 7.52zł (0.0–0.0) | 7.40 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS2` | 6.67 Er (8–1) | 0.2% | 2.5% | 1.78 (0–0) | 8.28 (0–0) | 7.51zł (0.0–0.0) | 7.33 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 5.79 Er (8–1) | 0.1% | 2.4% | 1.54 (0–0) | 6.35 (0–0) | 6.68zł (0.0–0.0) | 7.01 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS3` | 5.74 Er (8–1) | 0.1% | 2.4% | 1.53 (0–0) | 6.18 (0–0) | 6.51zł (0.0–0.0) | 6.97 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS3` | 5.59 Er (8–1) | 0.1% | 2.4% | 1.48 (0–0) | 5.84 (0–0) | 6.39zł (0.0–0.0) | 6.83 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS2` | 4.33 Er (8–1) | 0.1% | 2.0% | 0.96 (0–0) | 3.73 (0–0) | 5.69zł (0.0–0.0) | 5.93 (0.0–0.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_KB_DECREES_MINUS1` | 5.13 Er (8–1) | 0.0% | 1.9% | 1.32 (0–0) | 4.97 (0–0) | 6.22zł (0.0–0.0) | 6.35 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.49 Er (8–1) | 0.0% | 2.2% | 1.08 (0–0) | 4.32 (0–0) | 5.40zł (0.0–0.0) | 5.47 (0.0–0.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.