# Raport Audytu Poziomu 4 (Warianty Niszowe i Edykty) — Wersja Balansu: v1.0-alpha.166

**Wersja Balansu:** `v1.0-alpha.166` | **Data:** 2026-08-30 16:57 | **Przeanalizowano Wariantów:** 10 | **Próba:** 10000 gier/setup | **Czas:** 7.86s
**Wynik Bazy Poziomu 4 (Global):** `🟡 84.5 pkt` | 3p: `70.8 pkt` | 4p: `90.3 pkt` | 5p: `92.4 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (2)

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | Baza (Bieżące warianty niszowe i zasady edyktów) | 84.5 → 🟡 ** 84.5** (`= 0.0`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_OFF` | Szlak Morski: Era 4 → Wyłączony (99) | 84.5 → 🟡 ** 84.0** (`🔻 -0.5`) | 70.8 → 70.5 (`🔻 -0.3`) | 90.3 → 86.9 (`🔻 -3.4`) | 92.4 → 94.5 (`⬆️ +2.1`) | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 8 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_SEA_ROUTE_ERA_PLUS1` | Szlak Morski: Era 4 → 5 | 84.5 → 🟡 ** 84.5** (`= 0.0`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA_MINUS1` | Szlak Morski: Era 4 → 3 | 84.5 → 🟡 ** 84.5** (`= 0.0`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA_PLUS2` | Szlak Morski: Era 4 → 6 | 84.5 → 🟡 ** 84.5** (`= 0.0`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | ⚪ OPTYMALNY |
| `L4_INQUISITOR_SPEED2` | Inkwizytor Patrol: ruch 1 → 2 (podwojenie) | 84.5 → 🟡 ** 80.1** (`🔻 -4.4`) | 70.8 → 65.6 (`🔻 -5.2`) | 90.3 → 83.9 (`🔻 -6.4`) | 92.4 → 90.8 (`🔻 -1.6`) | 🔴 POGARSZA GLOBALNIE |
| `L4_TIME_DECK_EVERY_2ERAS` | Edykty Czasu: co 1 Erę → co 2 Ery | 84.5 → 🟠 ** 76.5** (`🔻 -8.0`) | 70.8 → 66.2 (`🔻 -4.6`) | 90.3 → 80.4 (`🔻 -9.9`) | 92.4 → 82.8 (`🔻 -9.6`) | 🔴 POGARSZA GLOBALNIE |
| `L4_TIME_DECK_EVERY_3ERAS` | Edykty Czasu: co 1 Erę → co 3 Ery | 84.5 → 🟠 ** 70.2** (`🔻 -14.3`) | 70.8 → 63.8 (`🔻 -7.0`) | 90.3 → 73.7 (`🔻 -16.6`) | 92.4 → 73.1 (`🔻 -19.3`) | 🔴 POGARSZA GLOBALNIE |
| `L4_NO_TIME_DECK` | Kronika Dziejów: Całkowite wyłączenie edyktów | 84.5 → 🔴 ** 61.7** (`🔻 -22.8`) | 70.8 → 53.8 (`🔻 -17.0`) | 90.3 → 66.3 (`🔻 -24.0`) | 92.4 → 64.9 (`🔻 -27.5`) | 🔴 POGARSZA GLOBALNIE |
| `L4_INQUISITOR_SPEED0` | Inkwizytor Patrol: ruch 1 → 0 (wyłączenie) | 84.5 → 🔴 ** 13.2** (`🔻 -71.3`) | 70.8 → 20.6 (`🔻 -50.2`) | 90.3 → 17.5 (`🔻 -72.8`) | 92.4 → 1.5 (`🔻 -90.9`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (2)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.28 (0–0) | 7.06zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_OFF` | 6.32 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 7.35 (0–0) | 7.21zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 8 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_SEA_ROUTE_ERA_PLUS1` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.28 (0–0) | 7.06zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA_MINUS1` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.28 (0–0) | 7.06zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA_PLUS2` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.28 (0–0) | 7.06zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED2` | 6.24 Er (8–1) | 0.1% | 2.5% | 1.66 (0–0) | 7.25 (0–0) | 7.01zł (0.0–0.0) | 7.18 (0.0–0.0) | 🟢 W NORMIE |
| `L4_TIME_DECK_EVERY_2ERAS` | 6.32 Er (8–1) | 0.1% | 2.8% | 1.65 (0–0) | 7.73 (0–0) | 6.89zł (0.0–0.0) | 7.20 (0.0–0.0) | 🟢 W NORMIE |
| `L4_TIME_DECK_EVERY_3ERAS` | 6.34 Er (8–1) | 0.1% | 2.9% | 1.65 (0–0) | 7.94 (0–0) | 6.86zł (0.0–0.0) | 7.23 (0.0–0.0) | 🟢 W NORMIE |
| `L4_NO_TIME_DECK` | 6.33 Er (8–1) | 0.1% | 2.9% | 1.64 (0–0) | 8.20 (0–0) | 6.75zł (0.0–0.0) | 7.25 (0.0–0.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED0` | 6.97 Er (8–1) | 0.5% | 2.3% | 1.03 (0–0) | 7.99 (0–0) | 7.89zł (0.0–0.0) | 6.60 (0.0–0.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.