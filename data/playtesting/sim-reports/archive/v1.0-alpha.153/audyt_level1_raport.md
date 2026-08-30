# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v1.0-alpha.153

**Wersja Balansu:** `v1.0-alpha.153` | **Data:** 2026-08-30 11:23 | **Przeanalizowano Wariantów:** 22 | **Próba:** 10000 gier/setup | **Czas:** 11.09s
**Wynik Bazy Poziomu 1 (Global):** `🟡 82.4 pkt` | 3p: `69.8 pkt` | 4p: `90.6 pkt` | 5p: `86.9 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (5)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 82.4 → 🟡 ** 82.4** (`= 0.0`) | 69.8 → 69.8 (`= 0.0`) | 90.6 → 90.6 (`= 0.0`) | 86.9 → 86.9 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/8 → 5/6/7 | 82.4 → 🟡 ** 80.9** (`🔻 -1.5`) | 69.8 → 71.6 (`⬆️ +1.8`) | 90.6 → 92.0 (`⬆️ +1.4`) | 86.9 → 79.2 (`🔻 -7.7`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 82.4 → 🟡 ** 80.0** (`🔻 -2.4`) | 69.8 → 62.9 (`🔻 -6.9`) | 90.6 → 85.1 (`🔻 -5.5`) | 86.9 → 92.1 (`⬆️ +5.2`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 82.4 → 🟠 ** 78.3** (`🔻 -4.1`) | 69.8 → 61.7 (`🔻 -8.1`) | 90.6 → 83.8 (`🔻 -6.8`) | 86.9 → 89.3 (`⬆️ +2.4`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 4/4/4zł → 5/5/5zł | 82.4 → 🟠 ** 67.1** (`🔻 -15.3`) | 69.8 → 71.0 (`⬆️ +1.2`) | 90.6 → 72.8 (`🔻 -17.8`) | 86.9 → 57.5 (`🔻 -29.4`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 17 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_OBSERVED_PLUS1` | Próg Obserwowanej: 3 → 4 | 82.4 → 🟡 ** 82.4** (`= 0.0`) | 69.8 → 69.8 (`= 0.0`) | 90.6 → 90.6 (`= 0.0`) | 86.9 → 86.9 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_OBSERVED_MINUS1` | Próg Obserwowanej: 3 → 2 | 82.4 → 🟡 ** 82.4** (`= 0.0`) | 69.8 → 69.8 (`= 0.0`) | 90.6 → 90.6 (`= 0.0`) | 86.9 → 86.9 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 15 → 16 | 82.4 → 🟡 ** 82.4** (`= 0.0`) | 69.8 → 69.8 (`= 0.0`) | 90.6 → 90.6 (`= 0.0`) | 86.9 → 86.9 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 15 → 14 | 82.4 → 🟡 ** 82.4** (`= 0.0`) | 69.8 → 69.8 (`= 0.0`) | 90.6 → 90.6 (`= 0.0`) | 86.9 → 86.9 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 82.4 → 🟡 ** 82.4** (`= 0.0`) | 69.8 → 69.8 (`= 0.0`) | 90.6 → 90.6 (`= 0.0`) | 86.9 → 86.9 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 82.4 → 🟡 ** 82.4** (`= 0.0`) | 69.8 → 69.8 (`= 0.0`) | 90.6 → 90.6 (`= 0.0`) | 86.9 → 86.9 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 4/4/4zł → 3/3/3zł | 82.4 → 🟠 ** 75.6** (`🔻 -6.8`) | 69.8 → 66.3 (`🔻 -3.5`) | 90.6 → 83.3 (`🔻 -7.3`) | 86.9 → 77.3 (`🔻 -9.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 82.4 → 🟠 ** 67.7** (`🔻 -14.7`) | 69.8 → 62.8 (`🔻 -7.0`) | 90.6 → 72.3 (`🔻 -18.3`) | 86.9 → 67.9 (`🔻 -19.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS2` | Złoto startowe: 4/4/4zł → 2/2/2zł | 82.4 → 🟠 ** 66.2** (`🔻 -16.2`) | 69.8 → 54.8 (`🔻 -15.0`) | 90.6 → 73.3 (`🔻 -17.3`) | 86.9 → 70.6 (`🔻 -16.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS3` | Złoto startowe: 4/4/4zł → 1/1/1zł | 82.4 → 🔴 ** 59.6** (`🔻 -22.8`) | 69.8 → 51.8 (`🔻 -18.0`) | 90.6 → 65.0 (`🔻 -25.6`) | 86.9 → 61.9 (`🔻 -25.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_MINUS1` | Akcja Gospodarcza: 1 → 0 | 82.4 → 🔴 ** 56.9** (`🔻 -25.5`) | 69.8 → 48.3 (`🔻 -21.5`) | 90.6 → 62.0 (`🔻 -28.6`) | 86.9 → 60.3 (`🔻 -26.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 82.4 → 🔴 ** 56.7** (`🔻 -25.7`) | 69.8 → 61.4 (`🔻 -8.4`) | 90.6 → 73.3 (`🔻 -17.3`) | 86.9 → 35.5 (`🔻 -51.4`) | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_PLUS1` | Akcja Gospodarcza: 1 → 2 | 82.4 → 🔴 ** 52.0** (`🔻 -30.4`) | 69.8 → 55.2 (`🔻 -14.6`) | 90.6 → 53.0 (`🔻 -37.6`) | 86.9 → 47.8 (`🔻 -39.1`) | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_DOUBLE` | Akcja Gospodarcza: 1 → 2 (podwojenie) | 82.4 → 🔴 ** 52.0** (`🔻 -30.4`) | 69.8 → 55.2 (`🔻 -14.6`) | 90.6 → 53.0 (`🔻 -37.6`) | 86.9 → 47.8 (`🔻 -39.1`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 82.4 → 🔴 ** 40.6** (`🔻 -41.8`) | 69.8 → 45.9 (`🔻 -23.9`) | 90.6 → 54.1 (`🔻 -36.5`) | 86.9 → 21.7 (`🔻 -65.2`) | 🔴 POGARSZA GLOBALNIE |
| `L1_CARDS_PER_ERA_PLUS1` | Karty/Erę: 2 → 3 | 82.4 → 🔴 ** 23.1** (`🔻 -59.3`) | 69.8 → 50.6 (`🔻 -19.2`) | 90.6 → 18.4 (`🔻 -72.2`) | 86.9 → 0.3 (`🔻 -86.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_CARDS_PER_ERA_MINUS1` | Karty/Erę: 2 → 1 | 82.4 → 🔴 ** 12.1** (`🔻 -70.3`) | 69.8 → 11.6 (`🔻 -58.2`) | 90.6 → 15.2 (`🔻 -75.4`) | 86.9 → 9.4 (`🔻 -77.5`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (5)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 6.26 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 7.26 (0–0) | 7.05zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 6.31 Er (8–1) | 0.1% | 2.4% | 1.64 (0–0) | 8.20 (0–0) | 7.30zł (0.0–0.0) | 7.09 (0.0–0.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_PLUS1` | 6.21 Er (8–1) | 0.1% | 2.6% | 1.67 (0–0) | 6.41 (0–0) | 6.82zł (0.0–0.0) | 7.20 (0.0–0.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 6.51 Er (8–1) | 0.1% | 3.1% | 1.57 (0–0) | 7.79 (0–0) | 8.03zł (0.0–0.0) | 7.23 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 6.08 Er (8–1) | 0.0% | 1.8% | 1.60 (0–0) | 6.88 (0–0) | 7.42zł (0.0–0.0) | 7.05 (0.0–0.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 17 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_OBSERVED_PLUS1` | 6.26 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 7.26 (0–0) | 7.05zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L1_OBSERVED_MINUS1` | 6.26 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 7.26 (0–0) | 7.05zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 6.26 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 7.26 (0–0) | 7.05zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 6.26 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 7.26 (0–0) | 7.05zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 6.26 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 7.26 (0–0) | 7.05zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 6.26 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 7.26 (0–0) | 7.05zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 6.39 Er (8–1) | 0.1% | 3.3% | 1.70 (0–0) | 7.53 (0–0) | 6.69zł (0.0–0.0) | 7.20 (0.0–0.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.98 Er (8–1) | 0.0% | 2.0% | 1.63 (0–0) | 6.61 (0–0) | 6.10zł (0.0–0.0) | 7.04 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS2` | 6.55 Er (8–1) | 0.1% | 4.5% | 1.75 (0–0) | 7.78 (0–0) | 6.42zł (0.0–0.0) | 7.26 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS3` | 6.73 Er (8–1) | 0.1% | 5.9% | 1.78 (0–0) | 7.93 (0–0) | 6.24zł (0.0–0.0) | 7.28 (0.0–0.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_MINUS1` | 6.36 Er (8–1) | 0.4% | 4.1% | 1.65 (0–0) | 7.61 (0–0) | 5.48zł (0.0–0.0) | 7.24 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 5.87 Er (8–1) | 0.0% | 2.4% | 1.58 (0–0) | 6.55 (0–0) | 6.78zł (0.0–0.0) | 7.16 (0.0–0.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_PLUS1` | 6.11 Er (8–1) | 0.0% | 2.0% | 1.59 (0–0) | 6.78 (0–0) | 8.37zł (0.0–0.0) | 7.02 (0.0–0.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_DOUBLE` | 6.11 Er (8–1) | 0.0% | 2.0% | 1.59 (0–0) | 6.78 (0–0) | 8.37zł (0.0–0.0) | 7.02 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 6.72 Er (8–1) | 0.2% | 2.6% | 1.73 (0–0) | 8.09 (0–0) | 7.43zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L1_CARDS_PER_ERA_PLUS1` | 5.38 Er (8–1) | 0.0% | 5.6% | 1.34 (0–0) | 6.73 (0–0) | 7.87zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L1_CARDS_PER_ERA_MINUS1` | 7.68 Er (8–1) | 0.6% | 0.1% | 1.92 (0–0) | 6.90 (0–0) | 7.42zł (0.0–0.0) | 6.82 (0.0–0.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.