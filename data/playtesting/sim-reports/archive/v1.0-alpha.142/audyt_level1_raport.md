# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v1.0-alpha.142

**Wersja Balansu:** `v1.0-alpha.142` | **Data:** 2026-08-30 10:20 | **Przeanalizowano Wariantów:** 22 | **Próba:** 10000 gier/setup | **Czas:** 29.16s
**Wynik Bazy Poziomu 1 (Global):** `🟠 78.4 pkt` | 3p: `69.0 pkt` | 4p: `88.4 pkt` | 5p: `77.9 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (5)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 78.4 → 🟠 ** 78.4** (`= 0.0`) | 69.0 → 69.0 (`= 0.0`) | 88.4 → 88.4 (`= 0.0`) | 77.9 → 77.9 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 5/4/4zł → 6/5/5zł | 78.4 → 🟡 ** 80.1** (`⬆️ +1.7`) | 69.0 → 73.2 (`⬆️ +4.2`) | 88.4 → 85.6 (`🔻 -2.8`) | 77.9 → 81.6 (`⬆️ +3.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 7/7/8 → 6/6/7 | 78.4 → 🟠 ** 79.6** (`⬆️ +1.2`) | 69.0 → 74.8 (`⬆️ +5.8`) | 88.4 → 91.5 (`⬆️ +3.1`) | 77.9 → 72.6 (`🔻 -5.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 7/7/8 → 8/8/9 | 78.4 → 🟠 ** 74.6** (`🔻 -3.8`) | 69.0 → 61.5 (`🔻 -7.5`) | 88.4 → 82.8 (`🔻 -5.6`) | 77.9 → 79.5 (`⬆️ +1.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 78.4 → 🟠 ** 73.4** (`🔻 -5.0`) | 69.0 → 62.2 (`🔻 -6.8`) | 88.4 → 79.2 (`🔻 -9.2`) | 77.9 → 78.9 (`⬆️ +1.0`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 17 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_OBSERVED_PLUS1` | Próg Obserwowanej: 3 → 4 | 78.4 → 🟠 ** 78.4** (`= 0.0`) | 69.0 → 69.0 (`= 0.0`) | 88.4 → 88.4 (`= 0.0`) | 77.9 → 77.9 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_OBSERVED_MINUS1` | Próg Obserwowanej: 3 → 2 | 78.4 → 🟠 ** 78.4** (`= 0.0`) | 69.0 → 69.0 (`= 0.0`) | 88.4 → 88.4 (`= 0.0`) | 77.9 → 77.9 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 15 → 16 | 78.4 → 🟠 ** 78.4** (`= 0.0`) | 69.0 → 69.0 (`= 0.0`) | 88.4 → 88.4 (`= 0.0`) | 77.9 → 77.9 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 15 → 14 | 78.4 → 🟠 ** 78.4** (`= 0.0`) | 69.0 → 69.0 (`= 0.0`) | 88.4 → 88.4 (`= 0.0`) | 77.9 → 77.9 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 78.4 → 🟠 ** 78.4** (`= 0.0`) | 69.0 → 69.0 (`= 0.0`) | 88.4 → 88.4 (`= 0.0`) | 77.9 → 77.9 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 78.4 → 🟠 ** 78.4** (`= 0.0`) | 69.0 → 69.0 (`= 0.0`) | 88.4 → 88.4 (`= 0.0`) | 77.9 → 77.9 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 5/4/4zł → 4/3/3zł | 78.4 → 🟠 ** 70.7** (`🔻 -7.7`) | 69.0 → 65.2 (`🔻 -3.8`) | 88.4 → 77.1 (`🔻 -11.3`) | 77.9 → 69.7 (`🔻 -8.2`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 78.4 → 🟠 ** 70.3** (`🔻 -8.1`) | 69.0 → 64.7 (`🔻 -4.3`) | 88.4 → 76.2 (`🔻 -12.2`) | 77.9 → 70.0 (`🔻 -7.9`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS2` | Złoto startowe: 5/4/4zł → 3/2/2zł | 78.4 → 🔴 ** 63.5** (`🔻 -14.9`) | 69.0 → 52.3 (`🔻 -16.7`) | 88.4 → 71.0 (`🔻 -17.4`) | 77.9 → 67.3 (`🔻 -10.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS3` | Złoto startowe: 5/4/4zł → 2/1/1zł | 78.4 → 🔴 ** 56.8** (`🔻 -21.6`) | 69.0 → 48.5 (`🔻 -20.5`) | 88.4 → 60.1 (`🔻 -28.3`) | 77.9 → 61.8 (`🔻 -16.1`) | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_PLUS1` | Akcja Gospodarcza: 1 → 2 | 78.4 → 🔴 ** 54.4** (`🔻 -24.0`) | 69.0 → 56.6 (`🔻 -12.4`) | 88.4 → 54.4 (`🔻 -34.0`) | 77.9 → 52.2 (`🔻 -25.7`) | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_DOUBLE` | Akcja Gospodarcza: 1 → 2 (podwojenie) | 78.4 → 🔴 ** 54.4** (`🔻 -24.0`) | 69.0 → 56.6 (`🔻 -12.4`) | 88.4 → 54.4 (`🔻 -34.0`) | 77.9 → 52.2 (`🔻 -25.7`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 78.4 → 🔴 ** 53.2** (`🔻 -25.2`) | 69.0 → 59.2 (`🔻 -9.8`) | 88.4 → 68.7 (`🔻 -19.7`) | 77.9 → 31.6 (`🔻 -46.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_MINUS1` | Akcja Gospodarcza: 1 → 0 | 78.4 → 🔴 ** 42.7** (`🔻 -35.7`) | 69.0 → 40.2 (`🔻 -28.8`) | 88.4 → 47.8 (`🔻 -40.6`) | 77.9 → 40.2 (`🔻 -37.7`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 78.4 → 🔴 ** 41.4** (`🔻 -37.0`) | 69.0 → 46.0 (`🔻 -23.0`) | 88.4 → 55.5 (`🔻 -32.9`) | 77.9 → 22.7 (`🔻 -55.2`) | 🔴 POGARSZA GLOBALNIE |
| `L1_CARDS_PER_ERA_PLUS1` | Karty/Erę: 2 → 3 | 78.4 → 🔴 ** 25.5** (`🔻 -52.9`) | 69.0 → 54.8 (`🔻 -14.2`) | 88.4 → 21.6 (`🔻 -66.8`) | 77.9 → 0.2 (`🔻 -77.7`) | 🔴 POGARSZA GLOBALNIE |
| `L1_CARDS_PER_ERA_MINUS1` | Karty/Erę: 2 → 1 | 78.4 → 🔴 ** 16.2** (`🔻 -62.2`) | 69.0 → 13.0 (`🔻 -56.0`) | 88.4 → 21.1 (`🔻 -67.3`) | 77.9 → 14.4 (`🔻 -63.5`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (5)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 6.30 Er (8–1) | 0.1% | 3.5% | 1.67 (0–0) | 7.35 (0–0) | 6.65zł (0.0–0.0) | 7.18 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 6.16 Er (8–1) | 0.1% | 2.6% | 1.63 (0–0) | 7.10 (0–0) | 7.04zł (0.0–0.0) | 7.12 (0.0–0.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 6.34 Er (8–1) | 0.1% | 3.4% | 1.65 (0–0) | 8.28 (0–0) | 6.87zł (0.0–0.0) | 7.13 (0.0–0.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_PLUS1` | 6.24 Er (8–1) | 0.1% | 3.6% | 1.68 (0–0) | 6.47 (0–0) | 6.42zł (0.0–0.0) | 7.22 (0.0–0.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 6.53 Er (8–1) | 0.1% | 3.9% | 1.58 (0–0) | 7.90 (0–0) | 7.43zł (0.0–0.0) | 7.28 (0.0–0.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 17 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_OBSERVED_PLUS1` | 6.30 Er (8–1) | 0.1% | 3.5% | 1.67 (0–0) | 7.35 (0–0) | 6.65zł (0.0–0.0) | 7.18 (0.0–0.0) | 🟢 W NORMIE |
| `L1_OBSERVED_MINUS1` | 6.30 Er (8–1) | 0.1% | 3.5% | 1.67 (0–0) | 7.35 (0–0) | 6.65zł (0.0–0.0) | 7.18 (0.0–0.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 6.30 Er (8–1) | 0.1% | 3.5% | 1.67 (0–0) | 7.35 (0–0) | 6.65zł (0.0–0.0) | 7.18 (0.0–0.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 6.30 Er (8–1) | 0.1% | 3.5% | 1.67 (0–0) | 7.35 (0–0) | 6.65zł (0.0–0.0) | 7.18 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 6.30 Er (8–1) | 0.1% | 3.5% | 1.67 (0–0) | 7.35 (0–0) | 6.65zł (0.0–0.0) | 7.18 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 6.30 Er (8–1) | 0.1% | 3.5% | 1.67 (0–0) | 7.35 (0–0) | 6.65zł (0.0–0.0) | 7.18 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 6.41 Er (8–1) | 0.1% | 4.5% | 1.70 (0–0) | 7.58 (0–0) | 6.28zł (0.0–0.0) | 7.22 (0.0–0.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 6.02 Er (8–1) | 0.0% | 3.2% | 1.65 (0–0) | 6.66 (0–0) | 5.68zł (0.0–0.0) | 7.06 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS2` | 6.57 Er (8–1) | 0.1% | 5.9% | 1.75 (0–0) | 7.82 (0–0) | 6.02zł (0.0–0.0) | 7.28 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS3` | 6.77 Er (8–1) | 0.2% | 7.6% | 1.80 (0–0) | 7.95 (0–0) | 5.88zł (0.0–0.0) | 7.32 (0.0–0.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_PLUS1` | 6.12 Er (8–1) | 0.0% | 2.8% | 1.60 (0–0) | 6.80 (0–0) | 7.97zł (0.0–0.0) | 7.04 (0.0–0.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_DOUBLE` | 6.12 Er (8–1) | 0.0% | 2.8% | 1.60 (0–0) | 6.80 (0–0) | 7.97zł (0.0–0.0) | 7.04 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 5.91 Er (8–1) | 0.0% | 3.4% | 1.60 (0–0) | 6.62 (0–0) | 6.39zł (0.0–0.0) | 7.19 (0.0–0.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_MINUS1` | 6.47 Er (8–1) | 0.6% | 5.9% | 1.69 (0–0) | 7.90 (0–0) | 5.24zł (0.0–0.0) | 7.29 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 6.77 Er (8–1) | 0.2% | 3.9% | 1.74 (0–0) | 8.20 (0–0) | 6.98zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L1_CARDS_PER_ERA_PLUS1` | 5.41 Er (8–1) | 0.0% | 6.7% | 1.34 (0–0) | 6.85 (0–0) | 7.22zł (0.0–0.0) | 7.23 (0.0–0.0) | 🟢 W NORMIE |
| `L1_CARDS_PER_ERA_MINUS1` | 7.78 Er (8–1) | 0.7% | 0.3% | 1.95 (0–0) | 7.19 (0–0) | 6.95zł (0.0–0.0) | 6.92 (0.0–0.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.