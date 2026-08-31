# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v1.0-alpha.170

**Wersja Balansu:** `v1.0-alpha.170` | **Data:** 2026-08-30 23:00 | **Przeanalizowano Wariantów:** 42 | **Próba:** 10000 gier/setup | **Czas:** 19.79s
**Wynik Bazy Poziomu 1 (Global):** `🟡 84.5 pkt` | 3p: `70.8 pkt` | 4p: `90.3 pkt` | 5p: `92.4 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (6)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 84.5 → 🟡 ** 84.5** (`= 0.0`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_THRESHOLD_5P_PLUS1` | Próg Oskarżenia (5p): 8 → 9 | 84.5 → 🟡 ** 85.4** (`⬆️ +0.9`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 95.1 (`⬆️ +2.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_THRESHOLD_5P_PLUS2` | Próg Oskarżenia (5p): 8 → 10 | 84.5 → 🟡 ** 85.2** (`⬆️ +0.7`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 94.6 (`⬆️ +2.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_THRESHOLD_4P_MINUS1` | Próg Oskarżenia (4p): 7 → 6 | 84.5 → 🟡 ** 85.1** (`⬆️ +0.6`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 92.1 (`⬆️ +1.8`) | 92.4 → 92.4 (`= 0.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia (global): 6/7/8 → 5/6/7 | 84.5 → 🟡 ** 82.1** (`🔻 -2.4`) | 70.8 → 72.0 (`⬆️ +1.2`) | 90.3 → 92.1 (`⬆️ +1.8`) | 92.4 → 82.3 (`🔻 -10.1`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia (global): 6/7/8 → 7/8/9 | 84.5 → 🟡 ** 81.0** (`🔻 -3.5`) | 70.8 → 63.4 (`🔻 -7.4`) | 90.3 → 84.6 (`🔻 -5.7`) | 92.4 → 95.1 (`⬆️ +2.7`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 36 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_OBSERVED_PLUS1` | Próg Obserwowanej: 3 → 4 | 84.5 → 🟡 ** 84.5** (`= 0.0`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_OBSERVED_MINUS1` | Próg Obserwowanej: 3 → 2 | 84.5 → 🟡 ** 84.5** (`= 0.0`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 15 → 16 | 84.5 → 🟡 ** 84.5** (`= 0.0`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 15 → 14 | 84.5 → 🟡 ** 84.5** (`= 0.0`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 84.5 → 🟡 ** 84.5** (`= 0.0`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 84.5 → 🟡 ** 84.5** (`= 0.0`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_START_GOLD_3P_PLUS1` | Złoto startowe (3p): 4zł → 5zł | 84.5 → 🟡 ** 84.4** (`🔻 -0.1`) | 70.8 → 70.5 (`🔻 -0.3`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | ⚪ OPTYMALNY |
| `L1_START_GOLD_3P_MINUS1` | Złoto startowe (3p): 4zł → 3zł | 84.5 → 🟡 ** 83.3** (`🔻 -1.2`) | 70.8 → 67.1 (`🔻 -3.7`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_4P_PLUS1` | Próg Oskarżenia (4p): 7 → 8 | 84.5 → 🟡 ** 82.6** (`🔻 -1.9`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 84.6 (`🔻 -5.7`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_4P_MINUS1` | Złoto startowe (4p): 4zł → 3zł | 84.5 → 🟡 ** 82.6** (`🔻 -1.9`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 84.7 (`🔻 -5.6`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_3P_PLUS2` | Próg Oskarżenia (3p): 6 → 8 | 84.5 → 🟡 ** 82.5** (`🔻 -2.0`) | 70.8 → 64.8 (`🔻 -6.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_5P_MINUS1` | Limit ręki (5p): 5 → 4 | 84.5 → 🟡 ** 82.5** (`🔻 -2.0`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 86.4 (`🔻 -6.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_5P_MINUS1` | Złoto startowe (5p): 4zł → 3zł | 84.5 → 🟡 ** 82.1** (`🔻 -2.4`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 85.1 (`🔻 -7.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_3P_PLUS1` | Próg Oskarżenia (3p): 6 → 7 | 84.5 → 🟡 ** 82.0** (`🔻 -2.5`) | 70.8 → 63.4 (`🔻 -7.4`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_4P_PLUS2` | Próg Oskarżenia (4p): 7 → 9 | 84.5 → 🟡 ** 82.0** (`🔻 -2.5`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 82.7 (`🔻 -7.6`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_3P_PLUS2` | Złoto startowe (3p): 4zł → 6zł | 84.5 → 🟡 ** 81.9** (`🔻 -2.6`) | 70.8 → 63.1 (`🔻 -7.7`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_3P_MINUS1` | Limit ręki (3p): 5 → 4 | 84.5 → 🟡 ** 81.9** (`🔻 -2.6`) | 70.8 → 62.9 (`🔻 -7.9`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_3P_PLUS1` | Limit ręki (3p): 5 → 6 | 84.5 → 🟡 ** 81.7** (`🔻 -2.8`) | 70.8 → 62.5 (`🔻 -8.3`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_4P_MINUS1` | Limit ręki (4p): 5 → 4 | 84.5 → 🟡 ** 81.4** (`🔻 -3.1`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 80.9 (`🔻 -9.4`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_5P_MINUS1` | Próg Oskarżenia (5p): 8 → 7 | 84.5 → 🟡 ** 81.1** (`🔻 -3.4`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 82.3 (`🔻 -10.1`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_3P_MINUS2` | Złoto startowe (3p): 4zł → 2zł | 84.5 → 🟠 ** 79.2** (`🔻 -5.3`) | 70.8 → 54.8 (`🔻 -16.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_4P_MINUS2` | Złoto startowe (4p): 4zł → 2zł | 84.5 → 🟠 ** 78.8** (`🔻 -5.7`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 73.2 (`🔻 -17.1`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_4P_PLUS1` | Limit ręki (4p): 5 → 6 | 84.5 → 🟠 ** 78.8** (`🔻 -5.7`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 73.2 (`🔻 -17.1`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_4P_PLUS1` | Złoto startowe (4p): 4zł → 5zł | 84.5 → 🟠 ** 77.8** (`🔻 -6.7`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 70.3 (`🔻 -20.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_5P_MINUS2` | Złoto startowe (5p): 4zł → 2zł | 84.5 → 🟠 ** 77.8** (`🔻 -6.7`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 72.4 (`🔻 -20.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_5P_MINUS2` | Próg Oskarżenia (5p): 8 → 6 | 84.5 → 🟠 ** 76.9** (`🔻 -7.6`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 69.7 (`🔻 -22.7`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_5P_PLUS1` | Limit ręki (5p): 5 → 6 | 84.5 → 🟠 ** 76.3** (`🔻 -8.2`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 67.7 (`🔻 -24.7`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_5P_PLUS1` | Złoto startowe (5p): 4zł → 5zł | 84.5 → 🟠 ** 72.9** (`🔻 -11.6`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 57.6 (`🔻 -34.8`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_4P_PLUS2` | Złoto startowe (4p): 4zł → 6zł | 84.5 → 🟠 ** 70.2** (`🔻 -14.3`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 47.5 (`🔻 -42.8`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_5P_PLUS2` | Złoto startowe (5p): 4zł → 6zł | 84.5 → 🔴 ** 60.4** (`🔻 -24.1`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 20.1 (`🔻 -72.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_MINUS1` | Akcja Gospodarcza: 1 → 0 | 84.5 → 🔴 ** 60.4** (`🔻 -24.1`) | 70.8 → 51.8 (`🔻 -19.0`) | 90.3 → 62.4 (`🔻 -27.9`) | 92.4 → 67.0 (`🔻 -25.4`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 84.5 → 🔴 ** 58.4** (`🔻 -26.1`) | 70.8 → 62.4 (`🔻 -8.4`) | 90.3 → 74.2 (`🔻 -16.1`) | 92.4 → 38.5 (`🔻 -53.9`) | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_PLUS1` | Akcja Gospodarcza: 1 → 2 | 84.5 → 🔴 ** 51.0** (`🔻 -33.5`) | 70.8 → 54.5 (`🔻 -16.3`) | 90.3 → 51.9 (`🔻 -38.4`) | 92.4 → 46.7 (`🔻 -45.7`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 84.5 → 🔴 ** 37.8** (`🔻 -46.7`) | 70.8 → 42.2 (`🔻 -28.6`) | 90.3 → 50.7 (`🔻 -39.6`) | 92.4 → 20.4 (`🔻 -72.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_CARDS_PER_ERA_PLUS1` | Karty/Erę: 2 → 3 | 84.5 → 🔴 ** 24.9** (`🔻 -59.6`) | 70.8 → 53.5 (`🔻 -17.3`) | 90.3 → 20.9 (`🔻 -69.4`) | 92.4 → 0.3 (`🔻 -92.1`) | 🔴 POGARSZA GLOBALNIE |
| `L1_CARDS_PER_ERA_MINUS1` | Karty/Erę: 2 → 1 | 84.5 → 🔴 ** 11.9** (`🔻 -72.6`) | 70.8 → 11.4 (`🔻 -59.4`) | 90.3 → 15.4 (`🔻 -74.9`) | 92.4 → 9.0 (`🔻 -83.4`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (6)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.28 (0–0) | 7.06zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_5P_PLUS1` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.21 (0–0) | 7.04zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_5P_PLUS2` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 7.16 (0–0) | 7.03zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_4P_MINUS1` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.63 (0–0) | 7.62 (0–0) | 7.13zł (0.0–0.0) | 7.12 (0.0–0.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 6.33 Er (8–1) | 0.1% | 2.4% | 1.62 (0–0) | 8.22 (0–0) | 7.32zł (0.0–0.0) | 7.07 (0.0–0.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_PLUS1` | 6.22 Er (8–1) | 0.1% | 2.6% | 1.65 (0–0) | 6.43 (0–0) | 6.82zł (0.0–0.0) | 7.19 (0.0–0.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 36 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_OBSERVED_PLUS1` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.28 (0–0) | 7.06zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L1_OBSERVED_MINUS1` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.28 (0–0) | 7.06zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.28 (0–0) | 7.06zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.28 (0–0) | 7.06zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.28 (0–0) | 7.06zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.28 (0–0) | 7.06zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_3P_PLUS1` | 6.17 Er (8–1) | 0.1% | 2.1% | 1.61 (0–0) | 7.07 (0–0) | 7.25zł (0.0–0.0) | 7.08 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_3P_MINUS1` | 6.37 Er (8–1) | 0.1% | 2.9% | 1.67 (0–0) | 7.45 (0–0) | 6.89zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_4P_PLUS1` | 6.27 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 6.99 (0–0) | 7.00zł (0.0–0.0) | 7.16 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_4P_MINUS1` | 6.32 Er (8–1) | 0.1% | 2.8% | 1.66 (0–0) | 7.39 (0–0) | 6.94zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_3P_PLUS2` | 6.22 Er (8–1) | 0.1% | 2.6% | 1.66 (0–0) | 6.32 (0–0) | 6.83zł (0.0–0.0) | 7.19 (0.0–0.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_5P_MINUS1` | 6.29 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.31 (0–0) | 7.14zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_5P_MINUS1` | 6.29 Er (8–1) | 0.1% | 2.6% | 1.64 (0–0) | 7.30 (0–0) | 7.03zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_3P_PLUS1` | 6.23 Er (8–1) | 0.1% | 2.6% | 1.65 (0–0) | 6.78 (0–0) | 6.90zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_4P_PLUS2` | 6.28 Er (8–1) | 0.1% | 2.6% | 1.66 (0–0) | 6.73 (0–0) | 6.96zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_3P_PLUS2` | 6.05 Er (8–1) | 0.1% | 1.9% | 1.57 (0–0) | 6.84 (0–0) | 7.46zł (0.0–0.0) | 7.03 (0.0–0.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_3P_MINUS1` | 6.44 Er (8–1) | 0.1% | 2.8% | 1.59 (0–0) | 7.60 (0–0) | 7.73zł (0.0–0.0) | 7.18 (0.0–0.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_3P_PLUS1` | 6.10 Er (8–1) | 0.0% | 2.2% | 1.64 (0–0) | 6.88 (0–0) | 6.39zł (0.0–0.0) | 7.08 (0.0–0.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_4P_MINUS1` | 6.35 Er (8–1) | 0.1% | 2.7% | 1.62 (0–0) | 7.46 (0–0) | 7.42zł (0.0–0.0) | 7.16 (0.0–0.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_5P_MINUS1` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.36 (0–0) | 7.08zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_3P_MINUS2` | 6.48 Er (8–1) | 0.1% | 3.6% | 1.71 (0–0) | 7.61 (0–0) | 6.75zł (0.0–0.0) | 7.20 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_4P_MINUS2` | 6.37 Er (8–1) | 0.1% | 3.3% | 1.68 (0–0) | 7.47 (0–0) | 6.84zł (0.0–0.0) | 7.19 (0.0–0.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_4P_PLUS1` | 6.19 Er (8–1) | 0.1% | 2.3% | 1.64 (0–0) | 7.04 (0–0) | 6.68zł (0.0–0.0) | 7.10 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_4P_PLUS1` | 6.21 Er (8–1) | 0.1% | 2.3% | 1.62 (0–0) | 7.12 (0–0) | 7.17zł (0.0–0.0) | 7.10 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_5P_MINUS2` | 6.30 Er (8–1) | 0.1% | 2.7% | 1.65 (0–0) | 7.32 (0–0) | 7.00zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_5P_MINUS2` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.43 (0–0) | 7.09zł (0.0–0.0) | 7.13 (0.0–0.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_5P_PLUS1` | 6.26 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.23 (0–0) | 6.98zł (0.0–0.0) | 7.13 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_5P_PLUS1` | 6.27 Er (8–1) | 0.1% | 2.4% | 1.64 (0–0) | 7.25 (0–0) | 7.09zł (0.0–0.0) | 7.13 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_4P_PLUS2` | 6.15 Er (8–1) | 0.1% | 2.1% | 1.60 (0–0) | 6.97 (0–0) | 7.32zł (0.0–0.0) | 7.05 (0.0–0.0) | 🟢 W NORMIE |
| `L1_START_GOLD_5P_PLUS2` | 6.26 Er (8–1) | 0.1% | 2.4% | 1.63 (0–0) | 7.22 (0–0) | 7.13zł (0.0–0.0) | 7.12 (0.0–0.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_MINUS1` | 6.40 Er (8–1) | 0.5% | 4.1% | 1.65 (0–0) | 7.70 (0–0) | 5.46zł (0.0–0.0) | 7.23 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 5.89 Er (8–1) | 0.0% | 2.4% | 1.57 (0–0) | 6.58 (0–0) | 6.77zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_PLUS1` | 6.13 Er (8–1) | 0.0% | 2.0% | 1.58 (0–0) | 6.78 (0–0) | 8.49zł (0.0–0.0) | 7.00 (0.0–0.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 6.76 Er (8–1) | 0.2% | 2.6% | 1.72 (0–0) | 8.14 (0–0) | 7.46zł (0.0–0.0) | 7.13 (0.0–0.0) | 🟢 W NORMIE |
| `L1_CARDS_PER_ERA_PLUS1` | 5.40 Er (8–1) | 0.0% | 5.6% | 1.34 (0–0) | 6.84 (0–0) | 7.99zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L1_CARDS_PER_ERA_MINUS1` | 7.68 Er (8–1) | 0.6% | 0.1% | 1.92 (0–0) | 6.84 (0–0) | 7.28zł (0.0–0.0) | 6.80 (0.0–0.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.