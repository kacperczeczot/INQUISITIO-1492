# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v1.0-alpha.101

**Wersja Balansu:** `v1.0-alpha.101` | **Data:** 2026-08-30 00:43 | **Przeanalizowano Wariantów:** 17 | **Próba:** 10000 gier/setup | **Czas:** 8.16s
**Wynik Bazy Poziomu 2 (Global):** `🔴 64.5 pkt` | 3p: `19.0 pkt` | 4p: `90.7 pkt` | 5p: `83.8 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (6)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 64.5 → 🔴 ** 64.5** (`= 0.0`) | 19.0 → 19.0 (`= 0.0`) | 90.7 → 90.7 (`= 0.0`) | 83.8 → 83.8 (`= 0.0`) | ⚪ OPTYMALNY |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki: 9 → 8 | 64.5 → 🔴 ** 54.7** (`🔻 -9.8`) | 19.0 → 21.5 (`⬆️ +2.5`) | 90.7 → 70.2 (`🔻 -20.5`) | 83.8 → 72.3 (`🔻 -11.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 7/7/8 → 6/6/7 | 64.5 → 🔴 ** 41.1** (`🔻 -23.4`) | 19.0 → 19.8 (`⬆️ +0.8`) | 90.7 → 74.2 (`🔻 -16.5`) | 83.8 → 29.3 (`🔻 -54.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2/3/3 → 3/4/4 | 64.5 → 🔴 ** 32.5** (`🔻 -32.0`) | 19.0 → 22.7 (`⬆️ +3.7`) | 90.7 → 29.9 (`🔻 -60.8`) | 83.8 → 44.8 (`🔻 -39.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS2` | Oficjum Skazania: 2/3/3 → 4/5/5 | 64.5 → 🔴 ** 21.2** (`🔻 -43.3`) | 19.0 → 23.4 (`⬆️ +4.4`) | 90.7 → 28.6 (`🔻 -62.1`) | 83.8 → 11.6 (`🔻 -72.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2/3/3 → 1/2/2 | 64.5 → 🔴 ** 13.6** (`🔻 -50.9`) | 19.0 → 21.4 (`⬆️ +2.4`) | 90.7 → 19.2 (`🔻 -71.5`) | 83.8 → 0.1 (`🔻 -83.7`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 11 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 7/7/8 → 8/8/9 | 64.5 → 🔴 ** 57.8** (`🔻 -6.7`) | 19.0 → 14.2 (`🔻 -4.8`) | 90.7 → 75.4 (`🔻 -15.3`) | 83.8 → 83.8 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki: 9 → 10 | 64.5 → 🔴 ** 50.4** (`🔻 -14.1`) | 19.0 → 15.8 (`🔻 -3.2`) | 90.7 → 75.9 (`🔻 -14.8`) | 83.8 → 59.4 (`🔻 -24.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 64.5 → 🔴 ** 46.1** (`🔻 -18.4`) | 19.0 → 14.0 (`🔻 -5.0`) | 90.7 → 64.0 (`🔻 -26.7`) | 83.8 → 60.3 (`🔻 -23.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS2` | Gildia Upadki: 9 → 11 | 64.5 → 🔴 ** 37.8** (`🔻 -26.7`) | 19.0 → 11.8 (`🔻 -7.2`) | 90.7 → 57.1 (`🔻 -33.6`) | 83.8 → 44.5 (`🔻 -39.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_PLUS2` | Oficjum Stosy: 7/7/8 → 9/9/10 | 64.5 → 🔴 ** 29.0** (`🔻 -35.5`) | 19.0 → 12.6 (`🔻 -6.4`) | 90.7 → 49.4 (`🔻 -41.3`) | 83.8 → 25.0 (`🔻 -58.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 64.5 → 🔴 ** 25.7** (`🔻 -38.8`) | 19.0 → 9.1 (`🔻 -9.9`) | 90.7 → 35.8 (`🔻 -54.9`) | 83.8 → 32.3 (`🔻 -51.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 64.5 → 🔴 ** 24.0** (`🔻 -40.5`) | 19.0 → 7.7 (`🔻 -11.3`) | 90.7 → 35.8 (`🔻 -54.9`) | 83.8 → 28.6 (`🔻 -55.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 64.5 → 🔴 ** 22.9** (`🔻 -41.6`) | 19.0 → 10.7 (`🔻 -8.3`) | 90.7 → 32.4 (`🔻 -58.3`) | 83.8 → 25.7 (`🔻 -58.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS2` | Cienie Relikwie: 2 → 4 | 64.5 → 🔴 ** 21.4** (`🔻 -43.1`) | 19.0 → 7.9 (`🔻 -11.1`) | 90.7 → 30.3 (`🔻 -60.4`) | 83.8 → 25.9 (`🔻 -57.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 64.5 → 🔴 **  8.5** (`🔻 -56.0`) | 19.0 → 6.0 (`🔻 -13.0`) | 90.7 → 19.5 (`🔻 -71.2`) | 83.8 → 0.1 (`🔻 -83.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 64.5 → 🔴 **  7.8** (`🔻 -56.7`) | 19.0 → 6.9 (`🔻 -12.1`) | 90.7 → 16.4 (`🔻 -74.3`) | 83.8 → 0.1 (`🔻 -83.7`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (6)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 6.51 Er (8–1) | 0.1% | 3.8% | 1.70 (0–0) | 7.89 (0–0) | 8.34zł (0.0–0.0) | 7.24 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 6.38 Er (8–1) | 0.1% | 3.8% | 1.66 (0–0) | 7.57 (0–0) | 8.19zł (0.0–0.0) | 7.21 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 6.33 Er (8–1) | 0.1% | 3.8% | 1.66 (0–0) | 7.51 (0–0) | 8.17zł (0.0–0.0) | 7.20 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 6.53 Er (8–1) | 0.1% | 3.8% | 1.70 (0–0) | 7.98 (0–0) | 8.35zł (0.0–0.0) | 7.25 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS2` | 6.52 Er (8–1) | 0.1% | 3.8% | 1.70 (0–0) | 7.96 (0–0) | 8.34zł (0.0–0.0) | 7.26 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 5.86 Er (8–1) | 0.1% | 3.7% | 1.55 (0–0) | 6.59 (0–0) | 7.80zł (0.0–0.0) | 7.09 (0.0–0.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 11 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_SO_STACKS_PLUS1` | 6.62 Er (8–1) | 0.1% | 3.8% | 1.72 (0–0) | 8.11 (0–0) | 8.45zł (0.0–0.0) | 7.25 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 6.63 Er (8–1) | 0.1% | 3.8% | 1.73 (0–0) | 8.15 (0–0) | 8.49zł (0.0–0.0) | 7.26 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 6.70 Er (8–1) | 0.2% | 4.1% | 1.75 (0–0) | 8.25 (0–0) | 8.50zł (0.0–0.0) | 7.30 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS2` | 6.72 Er (8–1) | 0.1% | 3.8% | 1.75 (0–0) | 8.36 (0–0) | 8.60zł (0.0–0.0) | 7.27 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS2` | 6.69 Er (8–1) | 0.2% | 3.8% | 1.73 (0–0) | 8.24 (0–0) | 8.51zł (0.0–0.0) | 7.25 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 6.93 Er (8–1) | 0.2% | 3.9% | 1.82 (0–0) | 8.91 (0–0) | 8.83zł (0.0–0.0) | 7.43 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.91 Er (8–1) | 0.8% | 3.8% | 1.80 (0–0) | 8.92 (0–0) | 8.68zł (0.0–0.0) | 7.37 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 6.90 Er (8–1) | 0.2% | 3.8% | 1.80 (0–0) | 8.84 (0–0) | 8.87zł (0.0–0.0) | 7.49 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS2` | 7.00 Er (8–1) | 0.3% | 3.9% | 1.85 (0–0) | 9.08 (0–0) | 8.91zł (0.0–0.0) | 7.45 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.26 Er (8–1) | 0.0% | 3.2% | 1.31 (0–0) | 5.30 (0–0) | 7.16zł (0.0–0.0) | 6.36 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.67 Er (8–1) | 0.0% | 3.5% | 1.09 (0–0) | 4.74 (0–0) | 6.17zł (0.0–0.0) | 5.55 (0.0–0.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.