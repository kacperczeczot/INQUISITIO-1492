# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v1.0-alpha.105

**Wersja Balansu:** `v1.0-alpha.105` | **Data:** 2026-08-30 01:59 | **Przeanalizowano Wariantów:** 22 | **Próba:** 10000 gier/setup | **Czas:** 10.67s
**Wynik Bazy Poziomu 1 (Global):** `🟠 70.2 pkt` | 3p: `36.0 pkt` | 4p: `90.7 pkt` | 5p: `83.8 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (4)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 70.2 → 🟠 ** 70.2** (`= 0.0`) | 36.0 → 36.0 (`= 0.0`) | 90.7 → 90.7 (`= 0.0`) | 83.8 → 83.8 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 7/7/8 → 8/8/9 | 70.2 → 🟠 ** 69.7** (`🔻 -0.5`) | 36.0 → 33.1 (`🔻 -2.9`) | 90.7 → 87.6 (`🔻 -3.1`) | 83.8 → 88.5 (`⬆️ +4.7`) | ⚪ OPTYMALNY |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 5/4/4zł → 6/5/5zł | 70.2 → 🔴 ** 60.2** (`🔻 -10.0`) | 36.0 → 41.2 (`⬆️ +5.2`) | 90.7 → 80.5 (`🔻 -10.2`) | 83.8 → 58.8 (`🔻 -25.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 70.2 → 🔴 ** 53.0** (`🔻 -17.2`) | 36.0 → 37.1 (`⬆️ +1.1`) | 90.7 → 70.4 (`🔻 -20.3`) | 83.8 → 51.5 (`🔻 -32.3`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 18 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_OBSERVED_PLUS1` | Próg Obserwowanej: 3 → 4 | 70.2 → 🟠 ** 70.2** (`= 0.0`) | 36.0 → 36.0 (`= 0.0`) | 90.7 → 90.7 (`= 0.0`) | 83.8 → 83.8 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_OBSERVED_MINUS1` | Próg Obserwowanej: 3 → 2 | 70.2 → 🟠 ** 70.2** (`= 0.0`) | 36.0 → 36.0 (`= 0.0`) | 90.7 → 90.7 (`= 0.0`) | 83.8 → 83.8 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 15 → 16 | 70.2 → 🟠 ** 70.2** (`= 0.0`) | 36.0 → 36.0 (`= 0.0`) | 90.7 → 90.7 (`= 0.0`) | 83.8 → 83.8 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 15 → 14 | 70.2 → 🟠 ** 70.2** (`= 0.0`) | 36.0 → 36.0 (`= 0.0`) | 90.7 → 90.7 (`= 0.0`) | 83.8 → 83.8 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 70.2 → 🟠 ** 70.2** (`= 0.0`) | 36.0 → 36.0 (`= 0.0`) | 90.7 → 90.7 (`= 0.0`) | 83.8 → 83.8 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 70.2 → 🟠 ** 70.2** (`= 0.0`) | 36.0 → 36.0 (`= 0.0`) | 90.7 → 90.7 (`= 0.0`) | 83.8 → 83.8 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 7/7/8 → 6/6/7 | 70.2 → 🔴 ** 62.5** (`🔻 -7.7`) | 36.0 → 34.0 (`🔻 -2.0`) | 90.7 → 89.9 (`🔻 -0.8`) | 83.8 → 63.7 (`🔻 -20.1`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 5/4/4zł → 4/3/3zł | 70.2 → 🔴 ** 60.2** (`🔻 -10.0`) | 36.0 → 29.2 (`🔻 -6.8`) | 90.7 → 81.5 (`🔻 -9.2`) | 83.8 → 70.0 (`🔻 -13.8`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 70.2 → 🔴 ** 60.2** (`🔻 -10.0`) | 36.0 → 31.2 (`🔻 -4.8`) | 90.7 → 77.1 (`🔻 -13.6`) | 83.8 → 72.2 (`🔻 -11.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS2` | Złoto startowe: 5/4/4zł → 3/2/2zł | 70.2 → 🔴 ** 51.6** (`🔻 -18.6`) | 36.0 → 25.5 (`🔻 -10.5`) | 90.7 → 65.3 (`🔻 -25.4`) | 83.8 → 64.1 (`🔻 -19.7`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 70.2 → 🔴 ** 44.7** (`🔻 -25.5`) | 36.0 → 29.7 (`🔻 -6.3`) | 90.7 → 76.9 (`🔻 -13.8`) | 83.8 → 27.4 (`🔻 -56.4`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS3` | Złoto startowe: 5/4/4zł → 2/1/1zł | 70.2 → 🔴 ** 40.0** (`🔻 -30.2`) | 36.0 → 21.7 (`🔻 -14.3`) | 90.7 → 50.5 (`🔻 -40.2`) | 83.8 → 47.9 (`🔻 -35.9`) | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_MINUS1` | Akcja Gospodarcza: 1 → 0 | 70.2 → 🔴 ** 38.7** (`🔻 -31.5`) | 36.0 → 19.7 (`🔻 -16.3`) | 90.7 → 49.0 (`🔻 -41.7`) | 83.8 → 47.4 (`🔻 -36.4`) | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_PLUS1` | Akcja Gospodarcza: 1 → 2 | 70.2 → 🔴 ** 37.5** (`🔻 -32.7`) | 36.0 → 25.3 (`🔻 -10.7`) | 90.7 → 49.3 (`🔻 -41.4`) | 83.8 → 38.0 (`🔻 -45.8`) | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_DOUBLE` | Akcja Gospodarcza: 1 → 2 (podwojenie) | 70.2 → 🔴 ** 37.5** (`🔻 -32.7`) | 36.0 → 25.3 (`🔻 -10.7`) | 90.7 → 49.3 (`🔻 -41.4`) | 83.8 → 38.0 (`🔻 -45.8`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 70.2 → 🔴 ** 33.8** (`🔻 -36.4`) | 36.0 → 23.8 (`🔻 -12.2`) | 90.7 → 57.1 (`🔻 -33.6`) | 83.8 → 20.6 (`🔻 -63.2`) | 🔴 POGARSZA GLOBALNIE |
| `L1_CARDS_PER_ERA_PLUS1` | Karty/Erę: 2 → 3 | 70.2 → 🔴 ** 12.9** (`🔻 -57.3`) | 36.0 → 22.8 (`🔻 -13.2`) | 90.7 → 15.9 (`🔻 -74.8`) | 83.8 → 0.1 (`🔻 -83.7`) | 🔴 POGARSZA GLOBALNIE |
| `L1_CARDS_PER_ERA_MINUS1` | Karty/Erę: 2 → 1 | 70.2 → 🔴 ** 11.3** (`🔻 -58.9`) | 36.0 → 6.5 (`🔻 -29.5`) | 90.7 → 17.3 (`🔻 -73.4`) | 83.8 → 10.1 (`🔻 -73.7`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (4)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 6.29 Er (8–1) | 0.1% | 3.8% | 1.65 (0–0) | 7.46 (0–0) | 8.14zł (0.0–0.0) | 7.21 (0.0–0.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_PLUS1` | 6.22 Er (8–1) | 0.1% | 3.9% | 1.64 (0–0) | 6.60 (0–0) | 7.81zł (0.0–0.0) | 7.26 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 6.14 Er (8–1) | 0.1% | 2.9% | 1.61 (0–0) | 7.15 (0–0) | 8.47zł (0.0–0.0) | 7.12 (0.0–0.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 6.06 Er (8–1) | 0.0% | 3.5% | 1.60 (0–0) | 6.92 (0–0) | 7.60zł (0.0–0.0) | 7.10 (0.0–0.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 18 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_OBSERVED_PLUS1` | 6.29 Er (8–1) | 0.1% | 3.8% | 1.65 (0–0) | 7.46 (0–0) | 8.14zł (0.0–0.0) | 7.21 (0.0–0.0) | 🟢 W NORMIE |
| `L1_OBSERVED_MINUS1` | 6.29 Er (8–1) | 0.1% | 3.8% | 1.65 (0–0) | 7.46 (0–0) | 8.14zł (0.0–0.0) | 7.21 (0.0–0.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 6.29 Er (8–1) | 0.1% | 3.8% | 1.65 (0–0) | 7.46 (0–0) | 8.14zł (0.0–0.0) | 7.21 (0.0–0.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 6.29 Er (8–1) | 0.1% | 3.8% | 1.65 (0–0) | 7.46 (0–0) | 8.14zł (0.0–0.0) | 7.21 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 6.29 Er (8–1) | 0.1% | 3.8% | 1.65 (0–0) | 7.46 (0–0) | 8.14zł (0.0–0.0) | 7.21 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 6.29 Er (8–1) | 0.1% | 3.8% | 1.65 (0–0) | 7.46 (0–0) | 8.14zł (0.0–0.0) | 7.21 (0.0–0.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 6.35 Er (8–1) | 0.1% | 3.7% | 1.65 (0–0) | 8.45 (0–0) | 8.44zł (0.0–0.0) | 7.16 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 6.43 Er (8–1) | 0.1% | 4.7% | 1.68 (0–0) | 7.72 (0–0) | 7.89zł (0.0–0.0) | 7.28 (0.0–0.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 6.53 Er (8–1) | 0.2% | 4.0% | 1.61 (0–0) | 7.99 (0–0) | 8.87zł (0.0–0.0) | 7.29 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS2` | 6.60 Er (8–1) | 0.1% | 5.8% | 1.74 (0–0) | 7.85 (0–0) | 7.73zł (0.0–0.0) | 7.31 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 5.90 Er (8–1) | 0.0% | 3.6% | 1.59 (0–0) | 6.72 (0–0) | 7.79zł (0.0–0.0) | 7.21 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS3` | 6.77 Er (8–1) | 0.2% | 7.4% | 1.77 (0–0) | 8.01 (0–0) | 7.58zł (0.0–0.0) | 7.35 (0.0–0.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_MINUS1` | 6.46 Er (8–1) | 0.6% | 6.1% | 1.60 (0–0) | 8.02 (0–0) | 6.34zł (0.0–0.0) | 7.35 (0.0–0.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_PLUS1` | 6.15 Er (8–1) | 0.0% | 3.0% | 1.62 (0–0) | 7.01 (0–0) | 9.93zł (0.0–0.0) | 7.08 (0.0–0.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_DOUBLE` | 6.15 Er (8–1) | 0.0% | 3.0% | 1.62 (0–0) | 7.01 (0–0) | 9.93zł (0.0–0.0) | 7.08 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 6.77 Er (8–1) | 0.1% | 4.2% | 1.71 (0–0) | 8.31 (0–0) | 8.56zł (0.0–0.0) | 7.21 (0.0–0.0) | 🟢 W NORMIE |
| `L1_CARDS_PER_ERA_PLUS1` | 5.42 Er (8–1) | 0.0% | 6.7% | 1.36 (0–0) | 7.00 (0–0) | 9.23zł (0.0–0.0) | 7.26 (0.0–0.0) | 🟢 W NORMIE |
| `L1_CARDS_PER_ERA_MINUS1` | 7.77 Er (8–1) | 0.7% | 0.3% | 1.93 (0–0) | 7.18 (0–0) | 8.17zł (0.0–0.0) | 6.95 (0.0–0.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.