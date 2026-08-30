# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v1.0-alpha.100

**Wersja Balansu:** `v1.0-alpha.100` | **Data:** 2026-08-30 00:27 | **Przeanalizowano Wariantów:** 20 | **Próba:** 10000 gier/setup | **Czas:** 8.52s
**Wynik Bazy Poziomu 1 (Global):** `🔴 58.0 pkt` | 3p: `19.0 pkt` | 4p: `90.7 pkt` | 5p: `64.2 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (6)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 58.0 → 🔴 ** 58.0** (`= 0.0`) | 19.0 → 19.0 (`= 0.0`) | 90.7 → 90.7 (`= 0.0`) | 64.2 → 64.2 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 7 → 8 | 58.0 → 🔴 ** 63.3** (`⬆️ +5.3`) | 19.0 → 24.2 (`⬆️ +5.2`) | 90.7 → 87.6 (`🔻 -3.1`) | 64.2 → 78.1 (`⬆️ +13.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 4zł → 5zł | 58.0 → 🔴 ** 50.5** (`🔻 -7.5`) | 19.0 → 20.7 (`⬆️ +1.7`) | 90.7 → 80.5 (`🔻 -10.2`) | 64.2 → 50.3 (`🔻 -13.9`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 58.0 → 🔴 ** 46.0** (`🔻 -12.0`) | 19.0 → 19.7 (`⬆️ +0.7`) | 90.7 → 70.4 (`🔻 -20.3`) | 64.2 → 47.8 (`🔻 -16.4`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 58.0 → 🔴 ** 45.8** (`🔻 -12.2`) | 19.0 → 9.1 (`🔻 -9.9`) | 90.7 → 57.1 (`🔻 -33.6`) | 64.2 → 71.3 (`⬆️ +7.1`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 58.0 → 🔴 ** 37.5** (`🔻 -20.5`) | 19.0 → 23.7 (`⬆️ +4.7`) | 90.7 → 76.9 (`🔻 -13.8`) | 64.2 → 12.0 (`🔻 -52.2`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 14 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_OBSERVED_PLUS1` | Próg Obserwowanej: 3 → 4 | 58.0 → 🔴 ** 58.0** (`= 0.0`) | 19.0 → 19.0 (`= 0.0`) | 90.7 → 90.7 (`= 0.0`) | 64.2 → 64.2 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_OBSERVED_MINUS1` | Próg Obserwowanej: 3 → 2 | 58.0 → 🔴 ** 58.0** (`= 0.0`) | 19.0 → 19.0 (`= 0.0`) | 90.7 → 90.7 (`= 0.0`) | 64.2 → 64.2 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 15 → 16 | 58.0 → 🔴 ** 58.0** (`= 0.0`) | 19.0 → 19.0 (`= 0.0`) | 90.7 → 90.7 (`= 0.0`) | 64.2 → 64.2 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 15 → 14 | 58.0 → 🔴 ** 58.0** (`= 0.0`) | 19.0 → 19.0 (`= 0.0`) | 90.7 → 90.7 (`= 0.0`) | 64.2 → 64.2 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 58.0 → 🔴 ** 58.0** (`= 0.0`) | 19.0 → 19.0 (`= 0.0`) | 90.7 → 90.7 (`= 0.0`) | 64.2 → 64.2 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 58.0 → 🔴 ** 58.0** (`= 0.0`) | 19.0 → 19.0 (`= 0.0`) | 90.7 → 90.7 (`= 0.0`) | 64.2 → 64.2 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 7 → 6 | 58.0 → 🔴 ** 53.4** (`🔻 -4.6`) | 19.0 → 16.5 (`🔻 -2.5`) | 90.7 → 89.9 (`🔻 -0.8`) | 64.2 → 53.7 (`🔻 -10.5`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 4zł → 3zł | 58.0 → 🔴 ** 52.5** (`🔻 -5.5`) | 19.0 → 18.1 (`🔻 -0.9`) | 90.7 → 81.5 (`🔻 -9.2`) | 64.2 → 58.0 (`🔻 -6.2`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 58.0 → 🔴 ** 49.9** (`🔻 -8.1`) | 19.0 → 18.1 (`🔻 -0.9`) | 90.7 → 77.1 (`🔻 -13.6`) | 64.2 → 54.5 (`🔻 -9.7`) | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_MINUS1` | Akcja Gospodarcza: 1 → 0 | 58.0 → 🔴 ** 33.1** (`🔻 -24.9`) | 19.0 → 11.7 (`🔻 -7.3`) | 90.7 → 49.0 (`🔻 -41.7`) | 64.2 → 38.6 (`🔻 -25.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_PLUS1` | Akcja Gospodarcza: 1 → 2 | 58.0 → 🔴 ** 31.7** (`🔻 -26.3`) | 19.0 → 13.0 (`🔻 -6.0`) | 90.7 → 49.3 (`🔻 -41.4`) | 64.2 → 32.9 (`🔻 -31.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_DOUBLE` | Akcja Gospodarcza: 1 → 2 (podwojenie) | 58.0 → 🔴 ** 31.7** (`🔻 -26.3`) | 19.0 → 13.0 (`🔻 -6.0`) | 90.7 → 49.3 (`🔻 -41.4`) | 64.2 → 32.9 (`🔻 -31.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_CARDS_PER_ERA_PLUS1` | Karty/Erę: 2 → 3 | 58.0 → 🔴 ** 10.2** (`🔻 -47.8`) | 19.0 → 14.5 (`🔻 -4.5`) | 90.7 → 15.9 (`🔻 -74.8`) | 64.2 → 0.1 (`🔻 -64.1`) | 🔴 POGARSZA GLOBALNIE |
| `L1_CARDS_PER_ERA_MINUS1` | Karty/Erę: 2 → 1 | 58.0 → 🔴 ** 10.2** (`🔻 -47.8`) | 19.0 → 2.3 (`🔻 -16.7`) | 90.7 → 17.3 (`🔻 -73.4`) | 64.2 → 11.1 (`🔻 -53.1`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (6)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 6.51 Er (8–1) | 0.1% | 3.8% | 1.70 (0–0) | 7.88 (0–0) | 8.34zł (0.0–0.0) | 7.24 (0.0–0.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_PLUS1` | 6.43 Er (8–1) | 0.1% | 3.9% | 1.69 (0–0) | 7.02 (0–0) | 8.01zł (0.0–0.0) | 7.29 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 6.34 Er (8–1) | 0.1% | 2.9% | 1.65 (0–0) | 7.55 (0–0) | 8.67zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 6.25 Er (8–1) | 0.0% | 3.6% | 1.65 (0–0) | 7.29 (0–0) | 7.74zł (0.0–0.0) | 7.12 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 6.97 Er (8–1) | 0.2% | 4.2% | 1.75 (0–0) | 8.74 (0–0) | 8.78zł (0.0–0.0) | 7.23 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 6.12 Er (8–1) | 0.0% | 3.6% | 1.64 (0–0) | 7.15 (0–0) | 7.99zł (0.0–0.0) | 7.24 (0.0–0.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 14 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_OBSERVED_PLUS1` | 6.51 Er (8–1) | 0.1% | 3.8% | 1.70 (0–0) | 7.88 (0–0) | 8.34zł (0.0–0.0) | 7.24 (0.0–0.0) | 🟢 W NORMIE |
| `L1_OBSERVED_MINUS1` | 6.51 Er (8–1) | 0.1% | 3.8% | 1.70 (0–0) | 7.88 (0–0) | 8.34zł (0.0–0.0) | 7.24 (0.0–0.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 6.51 Er (8–1) | 0.1% | 3.8% | 1.70 (0–0) | 7.88 (0–0) | 8.34zł (0.0–0.0) | 7.24 (0.0–0.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 6.51 Er (8–1) | 0.1% | 3.8% | 1.70 (0–0) | 7.88 (0–0) | 8.34zł (0.0–0.0) | 7.24 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 6.51 Er (8–1) | 0.1% | 3.8% | 1.70 (0–0) | 7.88 (0–0) | 8.34zł (0.0–0.0) | 7.24 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 6.51 Er (8–1) | 0.1% | 3.8% | 1.70 (0–0) | 7.88 (0–0) | 8.34zł (0.0–0.0) | 7.24 (0.0–0.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 6.56 Er (8–1) | 0.1% | 3.7% | 1.69 (0–0) | 8.88 (0–0) | 8.64zł (0.0–0.0) | 7.18 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 6.66 Er (8–1) | 0.1% | 4.7% | 1.73 (0–0) | 8.17 (0–0) | 8.11zł (0.0–0.0) | 7.30 (0.0–0.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 6.77 Er (8–1) | 0.2% | 4.0% | 1.65 (0–0) | 8.45 (0–0) | 9.14zł (0.0–0.0) | 7.31 (0.0–0.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_MINUS1` | 6.71 Er (8–1) | 0.6% | 6.2% | 1.65 (0–0) | 8.56 (0–0) | 6.43zł (0.0–0.0) | 7.38 (0.0–0.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_PLUS1` | 6.34 Er (8–1) | 0.1% | 3.0% | 1.66 (0–0) | 7.38 (0–0) | 10.29zł (0.0–0.0) | 7.10 (0.0–0.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_DOUBLE` | 6.34 Er (8–1) | 0.1% | 3.0% | 1.66 (0–0) | 7.38 (0–0) | 10.29zł (0.0–0.0) | 7.10 (0.0–0.0) | 🟢 W NORMIE |
| `L1_CARDS_PER_ERA_PLUS1` | 5.59 Er (8–1) | 0.0% | 6.7% | 1.40 (0–0) | 7.33 (0–0) | 9.47zł (0.0–0.0) | 7.27 (0.0–0.0) | 🟢 W NORMIE |
| `L1_CARDS_PER_ERA_MINUS1` | 8.04 Er (8–1) | 0.9% | 0.3% | 1.98 (0–0) | 7.71 (0–0) | 8.34zł (0.0–0.0) | 7.01 (0.0–0.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.