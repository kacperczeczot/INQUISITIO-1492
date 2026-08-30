# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v1.0-alpha.142

**Wersja Balansu:** `v1.0-alpha.142` | **Data:** 2026-08-30 10:20 | **Przeanalizowano Wariantów:** 19 | **Próba:** 10000 gier/setup | **Czas:** 16.36s
**Wynik Bazy Poziomu 2 (Global):** `🟠 78.4 pkt` | 3p: `69.0 pkt` | 4p: `88.4 pkt` | 5p: `77.9 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (1)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 78.4 → 🟠 ** 78.4** (`= 0.0`) | 69.0 → 69.0 (`= 0.0`) | 88.4 → 88.4 (`= 0.0`) | 77.9 → 77.9 (`= 0.0`) | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 18 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki: 8/9/9 → 7/8/8 | 78.4 → 🟠 ** 65.1** (`🔻 -13.3`) | 69.0 → 69.0 (`= 0.0`) | 88.4 → 64.3 (`🔻 -24.1`) | 77.9 → 62.1 (`🔻 -15.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki: 8/9/9 → 9/10/10 | 78.4 → 🔴 ** 62.9** (`🔻 -15.5`) | 69.0 → 52.8 (`🔻 -16.2`) | 88.4 → 76.8 (`🔻 -11.6`) | 77.9 → 59.0 (`🔻 -18.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 78.4 → 🔴 ** 59.4** (`🔻 -19.0`) | 69.0 → 51.5 (`🔻 -17.5`) | 88.4 → 61.7 (`🔻 -26.7`) | 77.9 → 65.0 (`🔻 -12.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 6/7/8 → 5/6/7 | 78.4 → 🔴 ** 57.5** (`🔻 -20.9`) | 69.0 → 69.0 (`= 0.0`) | 88.4 → 71.0 (`🔻 -17.4`) | 77.9 → 32.6 (`🔻 -45.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS2` | Kabała Fragmenty: 3 → 1 | 78.4 → 🔴 ** 49.2** (`🔻 -29.2`) | 69.0 → 45.2 (`🔻 -23.8`) | 88.4 → 51.6 (`🔻 -36.8`) | 77.9 → 50.7 (`🔻 -27.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS2` | Gildia Upadki: 8/9/9 → 10/11/11 | 78.4 → 🔴 ** 46.8** (`🔻 -31.6`) | 69.0 → 40.3 (`🔻 -28.7`) | 88.4 → 57.1 (`🔻 -31.3`) | 77.9 → 42.9 (`🔻 -35.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS2` | Gildia Upadki: 8/9/9 → 6/7/7 | 78.4 → 🔴 ** 38.9** (`🔻 -39.5`) | 69.0 → 51.9 (`🔻 -17.1`) | 88.4 → 40.8 (`🔻 -47.6`) | 77.9 → 24.0 (`🔻 -53.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 78.4 → 🔴 ** 34.4** (`🔻 -44.0`) | 69.0 → 35.9 (`🔻 -33.1`) | 88.4 → 35.2 (`🔻 -53.2`) | 77.9 → 32.1 (`🔻 -45.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS2` | Oficjum Stosy: 6/7/8 → 4/5/6 | 78.4 → 🔴 ** 32.4** (`🔻 -46.0`) | 69.0 → 55.8 (`🔻 -13.2`) | 88.4 → 37.7 (`🔻 -50.7`) | 77.9 → 3.7 (`🔻 -74.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 78.4 → 🔴 ** 31.5** (`🔻 -46.9`) | 69.0 → 32.6 (`🔻 -36.4`) | 88.4 → 34.3 (`🔻 -54.1`) | 77.9 → 27.6 (`🔻 -50.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 78.4 → 🔴 ** 29.9** (`🔻 -48.5`) | 69.0 → 34.6 (`🔻 -34.4`) | 88.4 → 30.1 (`🔻 -58.3`) | 77.9 → 25.0 (`🔻 -52.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS2` | Cienie Relikwie: 2 → 4 | 78.4 → 🔴 ** 29.2** (`🔻 -49.2`) | 69.0 → 33.4 (`🔻 -35.6`) | 88.4 → 29.3 (`🔻 -59.1`) | 77.9 → 25.0 (`🔻 -52.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2/3/3 → 1/2/2 | 78.4 → 🔴 ** 23.5** (`🔻 -54.9`) | 69.0 → 50.3 (`🔻 -18.7`) | 88.4 → 20.1 (`🔻 -68.3`) | 77.9 → 0.1 (`🔻 -77.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS3` | Gildia Upadki: 8/9/9 → 5/6/6 | 78.4 → 🔴 ** 22.0** (`🔻 -56.4`) | 69.0 → 38.6 (`🔻 -30.4`) | 88.4 → 25.4 (`🔻 -63.0`) | 77.9 → 2.1 (`🔻 -75.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS3` | Oficjum Stosy: 6/7/8 → 3/4/5 | 78.4 → 🔴 ** 18.8** (`🔻 -59.6`) | 69.0 → 37.1 (`🔻 -31.9`) | 88.4 → 19.3 (`🔻 -69.1`) | 77.9 → 0.1 (`🔻 -77.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS2` | Oficjum Skazania: 2/3/3 → 0/1/1 | 78.4 → 🔴 ** 15.9** (`🔻 -62.5`) | 69.0 → 29.6 (`🔻 -39.4`) | 88.4 → 18.0 (`🔻 -70.4`) | 77.9 → 0.1 (`🔻 -77.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 78.4 → 🔴 ** 15.2** (`🔻 -63.2`) | 69.0 → 26.4 (`🔻 -42.6`) | 88.4 → 19.0 (`🔻 -69.4`) | 77.9 → 0.1 (`🔻 -77.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 78.4 → 🔴 ** 14.8** (`🔻 -63.6`) | 69.0 → 28.7 (`🔻 -40.3`) | 88.4 → 15.5 (`🔻 -72.9`) | 77.9 → 0.1 (`🔻 -77.8`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (1)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 6.30 Er (8–1) | 0.1% | 3.5% | 1.67 (0–0) | 7.35 (0–0) | 6.65zł (0.0–0.0) | 7.18 (0.0–0.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 18 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_GC_FALLS_MINUS1` | 6.25 Er (8–1) | 0.1% | 3.5% | 1.65 (0–0) | 7.22 (0–0) | 6.60zł (0.0–0.0) | 7.16 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 6.50 Er (8–1) | 0.1% | 3.5% | 1.72 (0–0) | 7.77 (0–0) | 6.86zł (0.0–0.0) | 7.21 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 6.49 Er (8–1) | 0.1% | 3.8% | 1.72 (0–0) | 7.71 (0–0) | 6.78zł (0.0–0.0) | 7.25 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 6.25 Er (8–1) | 0.1% | 3.5% | 1.65 (0–0) | 7.22 (0–0) | 6.59zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS2` | 6.55 Er (8–1) | 0.1% | 3.9% | 1.74 (0–0) | 7.82 (0–0) | 6.83zł (0.0–0.0) | 7.28 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS2` | 6.57 Er (8–1) | 0.2% | 3.6% | 1.73 (0–0) | 7.93 (0–0) | 6.94zł (0.0–0.0) | 7.22 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS2` | 6.05 Er (8–1) | 0.1% | 3.5% | 1.60 (0–0) | 6.80 (0–0) | 6.41zł (0.0–0.0) | 7.10 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 6.66 Er (8–1) | 0.2% | 3.6% | 1.78 (0–0) | 8.25 (0–0) | 7.02zł (0.0–0.0) | 7.36 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS2` | 5.99 Er (8–1) | 0.1% | 3.5% | 1.59 (0–0) | 6.69 (0–0) | 6.37zł (0.0–0.0) | 7.05 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.59 Er (8–1) | 0.7% | 3.5% | 1.75 (0–0) | 8.12 (0–0) | 6.90zł (0.0–0.0) | 7.28 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 6.67 Er (8–1) | 0.2% | 3.5% | 1.77 (0–0) | 8.27 (0–0) | 7.11zł (0.0–0.0) | 7.44 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS2` | 6.72 Er (8–1) | 0.2% | 3.6% | 1.80 (0–0) | 8.40 (0–0) | 7.08zł (0.0–0.0) | 7.37 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 5.80 Er (8–1) | 0.1% | 3.4% | 1.55 (0–0) | 6.37 (0–0) | 6.27zł (0.0–0.0) | 7.03 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS3` | 5.78 Er (8–1) | 0.1% | 3.4% | 1.55 (0–0) | 6.25 (0–0) | 6.16zł (0.0–0.0) | 7.01 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS3` | 5.62 Er (8–1) | 0.1% | 3.4% | 1.49 (0–0) | 5.89 (0–0) | 6.02zł (0.0–0.0) | 6.86 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS2` | 4.32 Er (8–1) | 0.1% | 3.0% | 0.95 (0–0) | 3.72 (0–0) | 5.35zł (0.0–0.0) | 5.93 (0.0–0.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_KB_DECREES_MINUS1` | 5.19 Er (8–1) | 0.0% | 3.0% | 1.35 (0–0) | 5.09 (0–0) | 5.89zł (0.0–0.0) | 6.42 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.46 Er (8–1) | 0.0% | 3.2% | 1.08 (0–0) | 4.31 (0–0) | 4.99zł (0.0–0.0) | 5.41 (0.0–0.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.