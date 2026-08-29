# Raport Audytu Poziomu 4 (Warianty Niszowe i Edykty) — Wersja Balansu: v1.0-alpha.97

**Wersja Balansu:** `v1.0-alpha.97` | **Data:** 2026-08-29 22:33 | **Przeanalizowano Wariantów:** 10 | **Próba:** 5000 gier/setup | **Czas:** 1.09s
**Wynik Bazy Poziomu 4 (Global):** `🟢 93.6 pkt` | 3p: `0.0 pkt` | 4p: `93.6 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (1)

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | Baza (Bieżące warianty niszowe i zasady edyktów) | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 9 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_NO_TIME_DECK` | Kronika Dziejów: Całkowite wyłączenie edyktów | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L4_TIME_DECK_EVERY_2ERAS` | Edykty Czasu: co 1 Erę → co 2 Ery | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L4_TIME_DECK_EVERY_3ERAS` | Edykty Czasu: co 1 Erę → co 3 Ery | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA_PLUS1` | Szlak Morski: Era 4 → 5 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA_MINUS1` | Szlak Morski: Era 4 → 3 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA_PLUS2` | Szlak Morski: Era 4 → 6 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L4_INQUISITOR_SPEED0` | Inkwizytor Patrol: ruch 1 → 0 (wyłączenie) | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L4_INQUISITOR_SPEED2` | Inkwizytor Patrol: ruch 1 → 2 (podwojenie) | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_OFF` | Szlak Morski: Era 4 → Wyłączony (99) | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (1)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 9 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_NO_TIME_DECK` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L4_TIME_DECK_EVERY_2ERAS` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L4_TIME_DECK_EVERY_3ERAS` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA_PLUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA_MINUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA_PLUS2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED0` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_OFF` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.66 (0–0) | 9.06zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.