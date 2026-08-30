# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v1.0-alpha.100

**Wersja Balansu:** `v1.0-alpha.100` | **Data:** 2026-08-30 00:27 | **Przeanalizowano Wariantów:** 17 | **Próba:** 10000 gier/setup | **Czas:** 8.13s
**Wynik Bazy Poziomu 2 (Global):** `🔴 58.0 pkt` | 3p: `19.0 pkt` | 4p: `90.7 pkt` | 5p: `64.2 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (7)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 58.0 → 🔴 ** 58.0** (`= 0.0`) | 19.0 → 19.0 (`= 0.0`) | 90.7 → 90.7 (`= 0.0`) | 64.2 → 64.2 (`= 0.0`) | ⚪ OPTYMALNY |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 7 → 8 | 58.0 → 🔴 ** 57.8** (`🔻 -0.2`) | 19.0 → 14.2 (`🔻 -4.8`) | 90.7 → 75.4 (`🔻 -15.3`) | 64.2 → 83.8 (`⬆️ +19.6`) | ⚪ OPTYMALNY |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki: 9 → 8 | 58.0 → 🔴 ** 52.2** (`🔻 -5.8`) | 19.0 → 21.5 (`⬆️ +2.5`) | 90.7 → 70.2 (`🔻 -20.5`) | 64.2 → 64.8 (`⬆️ +0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 7 → 6 | 58.0 → 🔴 ** 41.1** (`🔻 -16.9`) | 19.0 → 19.8 (`⬆️ +0.8`) | 90.7 → 74.2 (`🔻 -16.5`) | 64.2 → 29.3 (`🔻 -34.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2/3/3 → 3/4/4 | 58.0 → 🔴 ** 39.0** (`🔻 -19.0`) | 19.0 → 22.7 (`⬆️ +3.7`) | 90.7 → 29.9 (`🔻 -60.8`) | 64.2 → 64.3 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS2` | Oficjum Skazania: 2/3/3 → 4/5/5 | 58.0 → 🔴 ** 23.3** (`🔻 -34.7`) | 19.0 → 23.4 (`⬆️ +4.4`) | 90.7 → 28.6 (`🔻 -62.1`) | 64.2 → 17.8 (`🔻 -46.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2/3/3 → 1/2/2 | 58.0 → 🔴 ** 13.6** (`🔻 -44.4`) | 19.0 → 21.4 (`⬆️ +2.4`) | 90.7 → 19.2 (`🔻 -71.5`) | 64.2 → 0.1 (`🔻 -64.1`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 10 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki: 9 → 10 | 58.0 → 🔴 ** 45.0** (`🔻 -13.0`) | 19.0 → 15.8 (`🔻 -3.2`) | 90.7 → 75.9 (`🔻 -14.8`) | 64.2 → 43.2 (`🔻 -21.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 58.0 → 🔴 ** 43.8** (`🔻 -14.2`) | 19.0 → 14.0 (`🔻 -5.0`) | 90.7 → 64.0 (`🔻 -26.7`) | 64.2 → 53.3 (`🔻 -10.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS2` | Gildia Upadki: 9 → 11 | 58.0 → 🔴 ** 33.8** (`🔻 -24.2`) | 19.0 → 11.8 (`🔻 -7.2`) | 90.7 → 57.1 (`🔻 -33.6`) | 64.2 → 32.6 (`🔻 -31.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_PLUS2` | Oficjum Stosy: 7 → 9 | 58.0 → 🔴 ** 29.0** (`🔻 -29.0`) | 19.0 → 12.6 (`🔻 -6.4`) | 90.7 → 49.4 (`🔻 -41.3`) | 64.2 → 25.0 (`🔻 -39.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 58.0 → 🔴 ** 24.7** (`🔻 -33.3`) | 19.0 → 9.1 (`🔻 -9.9`) | 90.7 → 35.8 (`🔻 -54.9`) | 64.2 → 29.1 (`🔻 -35.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 58.0 → 🔴 ** 22.3** (`🔻 -35.7`) | 19.0 → 7.7 (`🔻 -11.3`) | 90.7 → 35.8 (`🔻 -54.9`) | 64.2 → 23.5 (`🔻 -40.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 58.0 → 🔴 ** 21.2** (`🔻 -36.8`) | 19.0 → 10.7 (`🔻 -8.3`) | 90.7 → 32.4 (`🔻 -58.3`) | 64.2 → 20.6 (`🔻 -43.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS2` | Cienie Relikwie: 2 → 4 | 58.0 → 🔴 ** 20.6** (`🔻 -37.4`) | 19.0 → 7.9 (`🔻 -11.1`) | 90.7 → 30.3 (`🔻 -60.4`) | 64.2 → 23.7 (`🔻 -40.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 58.0 → 🔴 **  8.5** (`🔻 -49.5`) | 19.0 → 6.0 (`🔻 -13.0`) | 90.7 → 19.5 (`🔻 -71.2`) | 64.2 → 0.1 (`🔻 -64.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 58.0 → 🔴 **  7.8** (`🔻 -50.2`) | 19.0 → 6.9 (`🔻 -12.1`) | 90.7 → 16.4 (`🔻 -74.3`) | 64.2 → 0.1 (`🔻 -64.1`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (7)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 6.51 Er (8–1) | 0.1% | 3.8% | 1.70 (0–0) | 7.88 (0–0) | 8.34zł (0.0–0.0) | 7.24 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 6.62 Er (8–1) | 0.1% | 3.8% | 1.72 (0–0) | 8.11 (0–0) | 8.45zł (0.0–0.0) | 7.25 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 6.38 Er (8–1) | 0.1% | 3.8% | 1.66 (0–0) | 7.56 (0–0) | 8.19zł (0.0–0.0) | 7.20 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 6.33 Er (8–1) | 0.1% | 3.8% | 1.66 (0–0) | 7.51 (0–0) | 8.17zł (0.0–0.0) | 7.20 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 6.53 Er (8–1) | 0.1% | 3.8% | 1.70 (0–0) | 7.96 (0–0) | 8.35zł (0.0–0.0) | 7.25 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS2` | 6.52 Er (8–1) | 0.1% | 3.8% | 1.70 (0–0) | 7.95 (0–0) | 8.33zł (0.0–0.0) | 7.25 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 5.86 Er (8–1) | 0.1% | 3.7% | 1.55 (0–0) | 6.59 (0–0) | 7.80zł (0.0–0.0) | 7.09 (0.0–0.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 10 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_GC_FALLS_PLUS1` | 6.63 Er (8–1) | 0.1% | 3.8% | 1.73 (0–0) | 8.14 (0–0) | 8.48zł (0.0–0.0) | 7.25 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 6.70 Er (8–1) | 0.2% | 4.1% | 1.75 (0–0) | 8.24 (0–0) | 8.50zł (0.0–0.0) | 7.30 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS2` | 6.71 Er (8–1) | 0.1% | 3.8% | 1.74 (0–0) | 8.35 (0–0) | 8.59zł (0.0–0.0) | 7.27 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS2` | 6.69 Er (8–1) | 0.2% | 3.8% | 1.73 (0–0) | 8.24 (0–0) | 8.51zł (0.0–0.0) | 7.25 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 6.93 Er (8–1) | 0.2% | 3.9% | 1.82 (0–0) | 8.90 (0–0) | 8.82zł (0.0–0.0) | 7.43 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.91 Er (8–1) | 0.8% | 3.8% | 1.80 (0–0) | 8.91 (0–0) | 8.67zł (0.0–0.0) | 7.36 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 6.89 Er (8–1) | 0.2% | 3.8% | 1.80 (0–0) | 8.83 (0–0) | 8.87zł (0.0–0.0) | 7.49 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS2` | 6.99 Er (8–1) | 0.3% | 3.9% | 1.84 (0–0) | 9.07 (0–0) | 8.90zł (0.0–0.0) | 7.45 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.26 Er (8–1) | 0.0% | 3.2% | 1.31 (0–0) | 5.30 (0–0) | 7.16zł (0.0–0.0) | 6.36 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.66 Er (8–1) | 0.0% | 3.5% | 1.09 (0–0) | 4.73 (0–0) | 6.17zł (0.0–0.0) | 5.55 (0.0–0.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.