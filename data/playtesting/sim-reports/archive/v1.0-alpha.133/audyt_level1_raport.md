# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v1.0-alpha.133

**Wersja Balansu:** `v1.0-alpha.133` | **Data:** 2026-08-30 08:30 | **Przeanalizowano Wariantów:** 22 | **Próba:** 10000 gier/setup | **Czas:** 18.86s
**Wynik Bazy Poziomu 1 (Global):** `🟡 83.6 pkt` | 3p: `69.8 pkt` | 4p: `91.3 pkt` | 5p: `89.6 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (2)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 83.6 → 🟡 ** 83.6** (`= 0.0`) | 69.8 → 69.8 (`= 0.0`) | 91.3 → 91.3 (`= 0.0`) | 89.6 → 89.6 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 5/4/4zł → 6/5/5zł | 83.6 → 🟠 ** 76.5** (`🔻 -7.1`) | 69.8 → 72.0 (`⬆️ +2.2`) | 91.3 → 78.8 (`🔻 -12.5`) | 89.6 → 78.7 (`🔻 -10.9`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 20 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_OBSERVED_PLUS1` | Próg Obserwowanej: 3 → 4 | 83.6 → 🟡 ** 83.6** (`= 0.0`) | 69.8 → 69.8 (`= 0.0`) | 91.3 → 91.3 (`= 0.0`) | 89.6 → 89.6 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_OBSERVED_MINUS1` | Próg Obserwowanej: 3 → 2 | 83.6 → 🟡 ** 83.6** (`= 0.0`) | 69.8 → 69.8 (`= 0.0`) | 91.3 → 91.3 (`= 0.0`) | 89.6 → 89.6 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 15 → 16 | 83.6 → 🟡 ** 83.6** (`= 0.0`) | 69.8 → 69.8 (`= 0.0`) | 91.3 → 91.3 (`= 0.0`) | 89.6 → 89.6 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 15 → 14 | 83.6 → 🟡 ** 83.6** (`= 0.0`) | 69.8 → 69.8 (`= 0.0`) | 91.3 → 91.3 (`= 0.0`) | 89.6 → 89.6 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 83.6 → 🟡 ** 83.6** (`= 0.0`) | 69.8 → 69.8 (`= 0.0`) | 91.3 → 91.3 (`= 0.0`) | 89.6 → 89.6 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 83.6 → 🟡 ** 83.6** (`= 0.0`) | 69.8 → 69.8 (`= 0.0`) | 91.3 → 91.3 (`= 0.0`) | 89.6 → 89.6 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 7/7/8 → 8/8/9 | 83.6 → 🟠 ** 79.1** (`🔻 -4.5`) | 69.8 → 62.8 (`🔻 -7.0`) | 91.3 → 85.5 (`🔻 -5.8`) | 89.6 → 89.0 (`🔻 -0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 7/7/8 → 6/6/7 | 83.6 → 🟠 ** 78.0** (`🔻 -5.6`) | 69.8 → 64.8 (`🔻 -5.0`) | 91.3 → 86.0 (`🔻 -5.3`) | 89.6 → 83.1 (`🔻 -6.5`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 5/4/4zł → 4/3/3zł | 83.6 → 🟠 ** 75.0** (`🔻 -8.6`) | 69.8 → 63.6 (`🔻 -6.2`) | 91.3 → 85.0 (`🔻 -6.3`) | 89.6 → 76.3 (`🔻 -13.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 83.6 → 🟠 ** 73.9** (`🔻 -9.7`) | 69.8 → 58.0 (`🔻 -11.8`) | 91.3 → 79.2 (`🔻 -12.1`) | 89.6 → 84.6 (`🔻 -5.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 83.6 → 🟠 ** 65.9** (`🔻 -17.7`) | 69.8 → 64.3 (`🔻 -5.5`) | 91.3 → 70.6 (`🔻 -20.7`) | 89.6 → 62.8 (`🔻 -26.8`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS2` | Złoto startowe: 5/4/4zł → 3/2/2zł | 83.6 → 🔴 ** 59.9** (`🔻 -23.7`) | 69.8 → 51.3 (`🔻 -18.5`) | 91.3 → 66.7 (`🔻 -24.6`) | 89.6 → 61.7 (`🔻 -27.9`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 83.6 → 🔴 ** 55.6** (`🔻 -28.0`) | 69.8 → 55.4 (`🔻 -14.4`) | 91.3 → 72.6 (`🔻 -18.7`) | 89.6 → 38.9 (`🔻 -50.7`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS3` | Złoto startowe: 5/4/4zł → 2/1/1zł | 83.6 → 🔴 ** 52.9** (`🔻 -30.7`) | 69.8 → 45.0 (`🔻 -24.8`) | 91.3 → 57.1 (`🔻 -34.2`) | 89.6 → 56.7 (`🔻 -32.9`) | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_MINUS1` | Akcja Gospodarcza: 1 → 0 | 83.6 → 🔴 ** 46.7** (`🔻 -36.9`) | 69.8 → 41.2 (`🔻 -28.6`) | 91.3 → 49.4 (`🔻 -41.9`) | 89.6 → 49.4 (`🔻 -40.2`) | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_PLUS1` | Akcja Gospodarcza: 1 → 2 | 83.6 → 🔴 ** 41.9** (`🔻 -41.7`) | 69.8 → 45.1 (`🔻 -24.7`) | 91.3 → 43.0 (`🔻 -48.3`) | 89.6 → 37.5 (`🔻 -52.1`) | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_DOUBLE` | Akcja Gospodarcza: 1 → 2 (podwojenie) | 83.6 → 🔴 ** 41.9** (`🔻 -41.7`) | 69.8 → 45.1 (`🔻 -24.7`) | 91.3 → 43.0 (`🔻 -48.3`) | 89.6 → 37.5 (`🔻 -52.1`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 83.6 → 🔴 ** 37.3** (`🔻 -46.3`) | 69.8 → 37.8 (`🔻 -32.0`) | 91.3 → 52.7 (`🔻 -38.6`) | 89.6 → 21.3 (`🔻 -68.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_CARDS_PER_ERA_PLUS1` | Karty/Erę: 2 → 3 | 83.6 → 🔴 ** 26.1** (`🔻 -57.5`) | 69.8 → 50.2 (`🔻 -19.6`) | 91.3 → 27.9 (`🔻 -63.4`) | 89.6 → 0.3 (`🔻 -89.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_CARDS_PER_ERA_MINUS1` | Karty/Erę: 2 → 1 | 83.6 → 🔴 ** 15.1** (`🔻 -68.5`) | 69.8 → 14.1 (`🔻 -55.7`) | 91.3 → 19.6 (`🔻 -71.7`) | 89.6 → 11.7 (`🔻 -77.9`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (2)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 6.37 Er (8–1) | 0.1% | 3.8% | 1.67 (0–0) | 7.40 (0–0) | 10.39zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 6.23 Er (8–1) | 0.1% | 2.9% | 1.63 (0–0) | 7.14 (0–0) | 10.71zł (0.0–0.0) | 7.10 (0.0–0.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 20 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_OBSERVED_PLUS1` | 6.37 Er (8–1) | 0.1% | 3.8% | 1.67 (0–0) | 7.40 (0–0) | 10.39zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L1_OBSERVED_MINUS1` | 6.37 Er (8–1) | 0.1% | 3.8% | 1.67 (0–0) | 7.40 (0–0) | 10.39zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 6.37 Er (8–1) | 0.1% | 3.8% | 1.67 (0–0) | 7.40 (0–0) | 10.39zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 6.37 Er (8–1) | 0.1% | 3.8% | 1.67 (0–0) | 7.40 (0–0) | 10.39zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 6.37 Er (8–1) | 0.1% | 3.8% | 1.67 (0–0) | 7.40 (0–0) | 10.39zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 6.37 Er (8–1) | 0.1% | 3.8% | 1.67 (0–0) | 7.40 (0–0) | 10.39zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_PLUS1` | 6.30 Er (8–1) | 0.1% | 3.9% | 1.68 (0–0) | 6.52 (0–0) | 10.02zł (0.0–0.0) | 7.22 (0.0–0.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 6.43 Er (8–1) | 0.1% | 3.7% | 1.66 (0–0) | 8.42 (0–0) | 10.74zł (0.0–0.0) | 7.11 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 6.50 Er (8–1) | 0.1% | 4.8% | 1.70 (0–0) | 7.63 (0–0) | 10.12zł (0.0–0.0) | 7.21 (0.0–0.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 6.61 Er (8–1) | 0.1% | 4.2% | 1.59 (0–0) | 7.87 (0–0) | 10.64zł (0.0–0.0) | 7.24 (0.0–0.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 6.10 Er (8–1) | 0.0% | 3.5% | 1.65 (0–0) | 6.82 (0–0) | 9.66zł (0.0–0.0) | 7.09 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS2` | 6.67 Er (8–1) | 0.1% | 6.2% | 1.77 (0–0) | 7.74 (0–0) | 9.97zł (0.0–0.0) | 7.25 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 5.95 Er (8–1) | 0.0% | 3.6% | 1.59 (0–0) | 6.64 (0–0) | 9.88zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS3` | 6.88 Er (8–1) | 0.2% | 7.9% | 1.82 (0–0) | 7.82 (0–0) | 9.88zł (0.0–0.0) | 7.29 (0.0–0.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_MINUS1` | 6.55 Er (8–1) | 0.7% | 6.3% | 1.67 (0–0) | 8.00 (0–0) | 8.61zł (0.0–0.0) | 7.29 (0.0–0.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_PLUS1` | 6.20 Er (8–1) | 0.0% | 3.0% | 1.61 (0–0) | 6.86 (0–0) | 12.27zł (0.0–0.0) | 7.01 (0.0–0.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_DOUBLE` | 6.20 Er (8–1) | 0.0% | 3.0% | 1.61 (0–0) | 6.86 (0–0) | 12.27zł (0.0–0.0) | 7.01 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 6.87 Er (8–1) | 0.2% | 4.2% | 1.74 (0–0) | 8.28 (0–0) | 11.00zł (0.0–0.0) | 7.16 (0.0–0.0) | 🟢 W NORMIE |
| `L1_CARDS_PER_ERA_PLUS1` | 5.51 Er (8–1) | 0.0% | 7.1% | 1.37 (0–0) | 7.00 (0–0) | 11.22zł (0.0–0.0) | 7.22 (0.0–0.0) | 🟢 W NORMIE |
| `L1_CARDS_PER_ERA_MINUS1` | 7.78 Er (8–1) | 0.7% | 0.3% | 1.94 (0–0) | 7.11 (0–0) | 9.62zł (0.0–0.0) | 6.91 (0.0–0.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.