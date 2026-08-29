# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v1.0-alpha.97

**Wersja Balansu:** `v1.0-alpha.97` | **Data:** 2026-08-29 22:33 | **Przeanalizowano Wariantów:** 17 | **Próba:** 5000 gier/setup | **Czas:** 1.42s
**Wynik Bazy Poziomu 2 (Global):** `🟢 93.6 pkt` | 3p: `0.0 pkt` | 4p: `93.6 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (1)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 16 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 7 → 8 | 93.6 → 🟡 ** 83.0** (`🔻 -10.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 83.0 (`🔻 -10.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki: 9 → 10 | 93.6 → 🟠 ** 74.2** (`🔻 -19.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 74.2 (`🔻 -19.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki: 9 → 8 | 93.6 → 🟠 ** 74.2** (`🔻 -19.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 74.2 (`🔻 -19.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 7 → 6 | 93.6 → 🟠 ** 70.7** (`🔻 -22.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 70.7 (`🔻 -22.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 93.6 → 🔴 ** 58.2** (`🔻 -35.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 58.2 (`🔻 -35.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS2` | Gildia Upadki: 9 → 11 | 93.6 → 🔴 ** 57.5** (`🔻 -36.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 57.5 (`🔻 -36.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_PLUS2` | Oficjum Stosy: 7 → 9 | 93.6 → 🔴 ** 54.2** (`🔻 -39.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 54.2 (`🔻 -39.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 93.6 → 🔴 ** 37.2** (`🔻 -56.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 37.2 (`🔻 -56.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 93.6 → 🔴 ** 36.1** (`🔻 -57.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 36.1 (`🔻 -57.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS2` | Cienie Relikwie: 2 → 4 | 93.6 → 🔴 ** 32.4** (`🔻 -61.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 32.4 (`🔻 -61.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2/3/3 → 3/4/4 | 93.6 → 🔴 ** 30.2** (`🔻 -63.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 30.2 (`🔻 -63.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS2` | Oficjum Skazania: 2/3/3 → 4/5/5 | 93.6 → 🔴 ** 28.7** (`🔻 -64.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 28.7 (`🔻 -64.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2/3/3 → 1/2/2 | 93.6 → 🔴 ** 19.3** (`🔻 -74.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 19.3 (`🔻 -74.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 93.6 → 🔴 ** 19.2** (`🔻 -74.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 19.2 (`🔻 -74.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 93.6 → 🔴 ** 17.7** (`🔻 -75.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 17.7 (`🔻 -75.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (1)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 16 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_FRAGS_MINUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 5.81 Er (8–1) | 0.0% | 5.0% | 1.55 (0–0) | 7.76 (0–0) | 9.06zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 5.84 Er (8–1) | 0.0% | 5.0% | 1.56 (0–0) | 7.85 (0–0) | 9.11zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 5.66 Er (8–1) | 0.0% | 4.9% | 1.50 (0–0) | 7.34 (0–0) | 8.86zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.64 Er (8–1) | 0.0% | 4.9% | 1.50 (0–0) | 7.32 (0–0) | 8.85zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 5.97 Er (8–1) | 0.0% | 5.0% | 1.60 (0–0) | 8.20 (0–0) | 9.30zł (0.0–0.0) | 8.36 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS2` | 5.90 Er (8–1) | 0.0% | 5.0% | 1.58 (0–0) | 8.01 (0–0) | 9.18zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS2` | 5.83 Er (8–1) | 0.0% | 5.0% | 1.55 (0–0) | 7.81 (0–0) | 9.09zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 6.05 Er (8–1) | 0.0% | 5.0% | 1.63 (0–0) | 8.52 (0–0) | 9.37zł (0.0–0.0) | 8.39 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.00 Er (8–1) | 0.0% | 4.9% | 1.61 (0–0) | 8.43 (0–0) | 9.28zł (0.0–0.0) | 8.35 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS2` | 6.08 Er (8–1) | 0.0% | 5.0% | 1.65 (0–0) | 8.63 (0–0) | 9.41zł (0.0–0.0) | 8.40 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 5.87 Er (8–1) | 0.0% | 5.0% | 1.55 (0–0) | 7.97 (0–0) | 9.07zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS2` | 5.85 Er (8–1) | 0.0% | 5.0% | 1.54 (0–0) | 7.94 (0–0) | 9.05zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 5.05 Er (8–1) | 0.0% | 4.7% | 1.34 (0–0) | 6.00 (0–0) | 8.31zł (0.0–0.0) | 7.88 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 4.51 Er (8–1) | 0.0% | 4.1% | 1.13 (0–0) | 4.71 (0–0) | 7.60zł (0.0–0.0) | 7.10 (0.0–0.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_MINUS1` | 3.87 Er (8–1) | 0.0% | 4.3% | 0.90 (0–0) | 4.02 (0–0) | 6.64zł (0.0–0.0) | 5.98 (0.0–0.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.