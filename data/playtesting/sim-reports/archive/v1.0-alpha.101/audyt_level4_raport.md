# Raport Audytu Poziomu 4 (Warianty Niszowe i Edykty) — Wersja Balansu: v1.0-alpha.101

**Wersja Balansu:** `v1.0-alpha.101` | **Data:** 2026-08-30 00:51 | **Przeanalizowano Wariantów:** 10 | **Próba:** 10000 gier/setup | **Czas:** 4.64s
**Wynik Bazy Poziomu 4 (Global):** `🔴 64.5 pkt` | 3p: `19.0 pkt` | 4p: `90.7 pkt` | 5p: `83.8 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (5)

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | Baza (Bieżące warianty niszowe i zasady edyktów) | 64.5 → 🔴 ** 64.5** (`= 0.0`) | 19.0 → 19.0 (`= 0.0`) | 90.7 → 90.7 (`= 0.0`) | 83.8 → 83.8 (`= 0.0`) | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_OFF` | Szlak Morski: Era 4 → Wyłączony (99) | 64.5 → 🟠 ** 65.4** (`⬆️ +0.9`) | 19.0 → 19.1 (`⬆️ +0.1`) | 90.7 → 90.2 (`🔻 -0.5`) | 83.8 → 86.8 (`⬆️ +3.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L4_TIME_DECK_EVERY_2ERAS` | Edykty Czasu: co 1 Erę → co 2 Ery | 64.5 → 🔴 ** 57.6** (`🔻 -6.9`) | 19.0 → 20.9 (`⬆️ +1.9`) | 90.7 → 81.1 (`🔻 -9.6`) | 83.8 → 70.8 (`🔻 -13.0`) | 🔴 POGARSZA GLOBALNIE |
| `L4_TIME_DECK_EVERY_3ERAS` | Edykty Czasu: co 1 Erę → co 3 Ery | 64.5 → 🔴 ** 53.3** (`🔻 -11.2`) | 19.0 → 19.8 (`⬆️ +0.8`) | 90.7 → 75.0 (`🔻 -15.7`) | 83.8 → 65.2 (`🔻 -18.6`) | 🔴 POGARSZA GLOBALNIE |
| `L4_NO_TIME_DECK` | Kronika Dziejów: Całkowite wyłączenie edyktów | 64.5 → 🔴 ** 47.7** (`🔻 -16.8`) | 19.0 → 19.4 (`⬆️ +0.4`) | 90.7 → 66.4 (`🔻 -24.3`) | 83.8 → 57.4 (`🔻 -26.4`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 5 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_SEA_ROUTE_ERA_PLUS1` | Szlak Morski: Era 4 → 5 | 64.5 → 🔴 ** 64.5** (`= 0.0`) | 19.0 → 19.0 (`= 0.0`) | 90.7 → 90.7 (`= 0.0`) | 83.8 → 83.8 (`= 0.0`) | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA_MINUS1` | Szlak Morski: Era 4 → 3 | 64.5 → 🔴 ** 64.5** (`= 0.0`) | 19.0 → 19.0 (`= 0.0`) | 90.7 → 90.7 (`= 0.0`) | 83.8 → 83.8 (`= 0.0`) | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA_PLUS2` | Szlak Morski: Era 4 → 6 | 64.5 → 🔴 ** 64.5** (`= 0.0`) | 19.0 → 19.0 (`= 0.0`) | 90.7 → 90.7 (`= 0.0`) | 83.8 → 83.8 (`= 0.0`) | ⚪ OPTYMALNY |
| `L4_INQUISITOR_SPEED2` | Inkwizytor Patrol: ruch 1 → 2 (podwojenie) | 64.5 → 🔴 ** 59.5** (`🔻 -5.0`) | 19.0 → 19.0 (`= 0.0`) | 90.7 → 87.0 (`🔻 -3.7`) | 83.8 → 72.4 (`🔻 -11.4`) | 🔴 POGARSZA GLOBALNIE |
| `L4_INQUISITOR_SPEED0` | Inkwizytor Patrol: ruch 1 → 0 (wyłączenie) | 64.5 → 🔴 **  6.6** (`🔻 -57.9`) | 19.0 → 6.0 (`🔻 -13.0`) | 90.7 → 12.4 (`🔻 -78.3`) | 83.8 → 1.5 (`🔻 -82.3`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (5)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | 6.51 Er (8–1) | 0.1% | 3.8% | 1.70 (0–0) | 7.89 (0–0) | 8.34zł (0.0–0.0) | 7.24 (0.0–0.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_OFF` | 6.55 Er (8–1) | 0.1% | 3.8% | 1.71 (0–0) | 7.97 (0–0) | 8.45zł (0.0–0.0) | 7.25 (0.0–0.0) | 🟢 W NORMIE |
| `L4_TIME_DECK_EVERY_2ERAS` | 6.55 Er (8–1) | 0.1% | 4.2% | 1.70 (0–0) | 8.38 (0–0) | 8.16zł (0.0–0.0) | 7.29 (0.0–0.0) | 🟢 W NORMIE |
| `L4_TIME_DECK_EVERY_3ERAS` | 6.57 Er (8–1) | 0.1% | 4.3% | 1.70 (0–0) | 8.56 (0–0) | 8.12zł (0.0–0.0) | 7.32 (0.0–0.0) | 🟢 W NORMIE |
| `L4_NO_TIME_DECK` | 6.56 Er (8–1) | 0.1% | 4.4% | 1.69 (0–0) | 8.85 (0–0) | 7.99zł (0.0–0.0) | 7.34 (0.0–0.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 5 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_SEA_ROUTE_ERA_PLUS1` | 6.51 Er (8–1) | 0.1% | 3.8% | 1.70 (0–0) | 7.89 (0–0) | 8.34zł (0.0–0.0) | 7.24 (0.0–0.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA_MINUS1` | 6.51 Er (8–1) | 0.1% | 3.8% | 1.70 (0–0) | 7.89 (0–0) | 8.34zł (0.0–0.0) | 7.24 (0.0–0.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA_PLUS2` | 6.51 Er (8–1) | 0.1% | 3.8% | 1.70 (0–0) | 7.89 (0–0) | 8.34zł (0.0–0.0) | 7.24 (0.0–0.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED2` | 6.49 Er (8–1) | 0.1% | 3.9% | 1.72 (0–0) | 7.90 (0–0) | 8.30zł (0.0–0.0) | 7.28 (0.0–0.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED0` | 7.04 Er (8–1) | 0.4% | 3.7% | 1.05 (0–0) | 8.29 (0–0) | 9.13zł (0.0–0.0) | 6.68 (0.0–0.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.