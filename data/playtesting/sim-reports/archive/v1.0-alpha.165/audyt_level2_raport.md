# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v1.0-alpha.165

**Wersja Balansu:** `v1.0-alpha.165` | **Data:** 2026-08-30 15:44 | **Przeanalizowano Wariantów:** 19 | **Próba:** 10000 gier/setup | **Czas:** 15.2s
**Wynik Bazy Poziomu 2 (Global):** `🟡 84.5 pkt` | 3p: `70.8 pkt` | 4p: `90.3 pkt` | 5p: `92.4 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (1)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 84.5 → 🟡 ** 84.5** (`= 0.0`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 18 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki: 8/9/9 → 7/8/8 | 84.5 → 🟠 ** 67.3** (`🔻 -17.2`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 63.2 (`🔻 -27.1`) | 92.4 → 67.8 (`🔻 -24.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 84.5 → 🔴 ** 62.0** (`🔻 -22.5`) | 70.8 → 52.4 (`🔻 -18.4`) | 90.3 → 63.6 (`🔻 -26.7`) | 92.4 → 69.9 (`🔻 -22.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki: 8/9/9 → 9/10/10 | 84.5 → 🔴 ** 61.6** (`🔻 -22.9`) | 70.8 → 48.5 (`🔻 -22.3`) | 90.3 → 72.6 (`🔻 -17.7`) | 92.4 → 63.6 (`🔻 -28.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 6/7/8 → 5/6/7 | 84.5 → 🔴 ** 60.5** (`🔻 -24.0`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 74.8 (`🔻 -15.5`) | 92.4 → 36.0 (`🔻 -56.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS2` | Kabała Fragmenty: 3 → 1 | 84.5 → 🔴 ** 51.4** (`🔻 -33.1`) | 70.8 → 48.2 (`🔻 -22.6`) | 90.3 → 53.0 (`🔻 -37.3`) | 92.4 → 53.0 (`🔻 -39.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS2` | Gildia Upadki: 8/9/9 → 10/11/11 | 84.5 → 🔴 ** 45.8** (`🔻 -38.7`) | 70.8 → 37.9 (`🔻 -32.9`) | 90.3 → 53.6 (`🔻 -36.7`) | 92.4 → 45.8 (`🔻 -46.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS2` | Gildia Upadki: 8/9/9 → 6/7/7 | 84.5 → 🔴 ** 38.1** (`🔻 -46.4`) | 70.8 → 53.5 (`🔻 -17.3`) | 90.3 → 38.8 (`🔻 -51.5`) | 92.4 → 21.9 (`🔻 -70.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 84.5 → 🔴 ** 34.2** (`🔻 -50.3`) | 70.8 → 36.4 (`🔻 -34.4`) | 90.3 → 35.6 (`🔻 -54.7`) | 92.4 → 30.6 (`🔻 -61.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS2` | Oficjum Stosy: 6/7/8 → 4/5/6 | 84.5 → 🔴 ** 33.6** (`🔻 -50.9`) | 70.8 → 57.7 (`🔻 -13.1`) | 90.3 → 39.5 (`🔻 -50.8`) | 92.4 → 3.6 (`🔻 -88.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 84.5 → 🔴 ** 33.0** (`🔻 -51.5`) | 70.8 → 34.7 (`🔻 -36.1`) | 90.3 → 35.5 (`🔻 -54.8`) | 92.4 → 28.7 (`🔻 -63.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 84.5 → 🔴 ** 31.2** (`🔻 -53.3`) | 70.8 → 35.0 (`🔻 -35.8`) | 90.3 → 32.7 (`🔻 -57.6`) | 92.4 → 26.0 (`🔻 -66.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS2` | Cienie Relikwie: 2 → 4 | 84.5 → 🔴 ** 30.3** (`🔻 -54.2`) | 70.8 → 34.1 (`🔻 -36.7`) | 90.3 → 30.9 (`🔻 -59.4`) | 92.4 → 25.9 (`🔻 -66.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2/3/3 → 1/2/2 | 84.5 → 🔴 ** 25.0** (`🔻 -59.5`) | 70.8 → 53.8 (`🔻 -17.0`) | 90.3 → 21.0 (`🔻 -69.3`) | 92.4 → 0.1 (`🔻 -92.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS3` | Gildia Upadki: 8/9/9 → 5/6/6 | 84.5 → 🔴 ** 21.1** (`🔻 -63.4`) | 70.8 → 38.5 (`🔻 -32.3`) | 90.3 → 22.8 (`🔻 -67.5`) | 92.4 → 2.0 (`🔻 -90.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS3` | Oficjum Stosy: 6/7/8 → 3/4/5 | 84.5 → 🔴 ** 19.6** (`🔻 -64.9`) | 70.8 → 38.8 (`🔻 -32.0`) | 90.3 → 19.8 (`🔻 -70.5`) | 92.4 → 0.1 (`🔻 -92.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS2` | Oficjum Skazania: 2/3/3 → 0/1/1 | 84.5 → 🔴 ** 16.6** (`🔻 -67.9`) | 70.8 → 31.3 (`🔻 -39.5`) | 90.3 → 18.4 (`🔻 -71.9`) | 92.4 → 0.1 (`🔻 -92.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 84.5 → 🔴 ** 15.6** (`🔻 -68.9`) | 70.8 → 27.2 (`🔻 -43.6`) | 90.3 → 19.5 (`🔻 -70.8`) | 92.4 → 0.1 (`🔻 -92.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 84.5 → 🔴 ** 15.4** (`🔻 -69.1`) | 70.8 → 29.3 (`🔻 -41.5`) | 90.3 → 16.8 (`🔻 -73.5`) | 92.4 → 0.1 (`🔻 -92.3`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (1)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.28 (0–0) | 7.06zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 18 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_GC_FALLS_MINUS1` | 6.23 Er (8–1) | 0.1% | 2.5% | 1.63 (0–0) | 7.15 (0–0) | 7.00zł (0.0–0.0) | 7.12 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 6.45 Er (8–1) | 0.1% | 2.7% | 1.70 (0–0) | 7.61 (0–0) | 7.22zł (0.0–0.0) | 7.20 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 6.47 Er (8–1) | 0.1% | 2.5% | 1.69 (0–0) | 7.68 (0–0) | 7.28zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 6.23 Er (8–1) | 0.1% | 2.5% | 1.63 (0–0) | 7.15 (0–0) | 6.99zł (0.0–0.0) | 7.11 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS2` | 6.53 Er (8–1) | 0.1% | 2.9% | 1.72 (0–0) | 7.73 (0–0) | 7.28zł (0.0–0.0) | 7.23 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS2` | 6.55 Er (8–1) | 0.2% | 2.5% | 1.71 (0–0) | 7.84 (0–0) | 7.37zł (0.0–0.0) | 7.18 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS2` | 6.03 Er (8–1) | 0.1% | 2.4% | 1.58 (0–0) | 6.74 (0–0) | 6.77zł (0.0–0.0) | 7.06 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 6.63 Er (8–1) | 0.2% | 2.5% | 1.75 (0–0) | 8.14 (0–0) | 7.48zł (0.0–0.0) | 7.30 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS2` | 5.98 Er (8–1) | 0.1% | 2.5% | 1.57 (0–0) | 6.63 (0–0) | 6.72zł (0.0–0.0) | 7.01 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.62 Er (8–1) | 0.6% | 2.5% | 1.74 (0–0) | 8.15 (0–0) | 7.39zł (0.0–0.0) | 7.28 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 6.64 Er (8–1) | 0.2% | 2.4% | 1.74 (0–0) | 8.17 (0–0) | 7.54zł (0.0–0.0) | 7.40 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS2` | 6.67 Er (8–1) | 0.3% | 2.5% | 1.76 (0–0) | 8.27 (0–0) | 7.54zł (0.0–0.0) | 7.32 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 5.81 Er (8–1) | 0.1% | 2.4% | 1.53 (0–0) | 6.35 (0–0) | 6.63zł (0.0–0.0) | 7.00 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS3` | 5.76 Er (8–1) | 0.1% | 2.4% | 1.52 (0–0) | 6.19 (0–0) | 6.49zł (0.0–0.0) | 6.96 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS3` | 5.60 Er (8–1) | 0.1% | 2.4% | 1.47 (0–0) | 5.84 (0–0) | 6.32zł (0.0–0.0) | 6.81 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS2` | 4.33 Er (8–1) | 0.1% | 2.0% | 0.96 (0–0) | 3.73 (0–0) | 5.62zł (0.0–0.0) | 5.91 (0.0–0.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_KB_DECREES_MINUS1` | 5.13 Er (8–1) | 0.0% | 1.9% | 1.30 (0–0) | 4.97 (0–0) | 6.10zł (0.0–0.0) | 6.33 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.56 Er (8–1) | 0.0% | 2.2% | 1.09 (0–0) | 4.39 (0–0) | 5.46zł (0.0–0.0) | 5.54 (0.0–0.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.