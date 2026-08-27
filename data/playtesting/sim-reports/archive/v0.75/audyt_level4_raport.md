# Raport Audytu Poziomu 4 (Warianty Niszowe i Edykty) — Wersja Balansu: v0.75

**Wersja Balansu:** `v0.75` | **Data:** 2026-08-17 00:57 | **Przeanalizowano Wariantów:** 8 | **Próba:** 3000 gier/setup | **Czas:** 120.35s
**Wynik Bazy Poziomu 4 (Global):** `🔴 35.5 pkt` | 3p: `34.1 pkt` | 4p: `34.3 pkt` | 5p: `38.1 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (5)

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | Baza (Bieżące warianty niszowe i zasady edyktów) | 🔴 ** 35.5** | 34.1 | 34.3 | 38.1 | ⚪ OPTYMALNY |
| `L4_VERDICT_SECRET` | Werdykt: jawny → tajny (brak koordynacji anty-snowball) | 35.5 → 🔴 ** 40.6** (`⬆️ +5.1`) | 34.1 → 34.3 (`⬆️ +0.2`) | 34.3 → 42.4 (`⬆️ +8.1`) | 38.1 → 45.2 (`⬆️ +7.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L4_INQUISITOR_SPEED2` | Inkwizytor Patrol: ruch 1 → 2 | 35.5 → 🔴 ** 35.0** (`-0.5`) | 34.1 → 35.3 (`⬆️ +1.2`) | 34.3 → 35.3 (`⬆️ +1.0`) | 38.1 → 34.5 (`-3.6`) | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA5` | Szlak Morski: Era 6 → Era 5 | 35.5 → 🔴 ** 35.0** (`-0.5`) | 34.1 → 34.2 (`⬆️ +0.1`) | 34.3 → 34.0 (`-0.3`) | 38.1 → 36.7 (`-1.4`) | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA4` | Szlak Morski: Era 6 → Era 4 | 35.5 → 🔴 ** 34.8** (`-0.7`) | 34.1 → 34.3 (`⬆️ +0.2`) | 34.3 → 33.7 (`-0.6`) | 38.1 → 36.3 (`-1.8`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 3 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_TIME_DECK_EVERY_2ERAS` | Edykty Czasu: co 1 Erę → co 2 Ery | 35.5 → 🔴 ** 31.3** (`-4.2`) | 34.1 → 29.3 (`-4.8`) | 34.3 → 30.7 (`-3.6`) | 38.1 → 34.0 (`-4.1`) | 🔴 POGARSZA GLOBALNIE |
| `L4_INQUISITOR_SPEED0` | Inkwizytor Patrol: ruch 1 → 0 | 35.5 → 🔴 ** 27.5** (`-8.0`) | 34.1 → 31.1 (`-3.0`) | 34.3 → 27.8 (`-6.5`) | 38.1 → 23.6 (`-14.5`) | 🔴 POGARSZA GLOBALNIE |
| `L4_NO_TIME_DECK` | Kronika Dziejów: Całkowite wyłączenie edyktów | 35.5 → 🔴 ** 27.4** (`-8.1`) | 34.1 → 26.1 (`-8.0`) | 34.3 → 26.7 (`-7.6`) | 38.1 → 29.5 (`-8.6`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (5)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | 6.10 Er (1–12) | 4.5% | 6.5% | 1.44 (0–4) | 3.08 (0–21) | 2.19zł (0.0–8.3) | 5.79 (0.7–10.0) | 🟢 W NORMIE |
| `L4_VERDICT_SECRET` | 5.85 Er (1–12) | 3.1% | 6.5% | 1.37 (0–4) | 2.73 (0–25) | 2.12zł (0.0–8.3) | 5.51 (0.7–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED2` | 6.07 Er (1–12) | 4.3% | 6.5% | 1.44 (0–4) | 3.08 (0–24) | 2.17zł (0.0–8.3) | 5.82 (0.0–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA5` | 6.09 Er (1–12) | 4.5% | 6.5% | 1.43 (0–4) | 3.07 (0–21) | 2.19zł (0.0–8.3) | 5.78 (0.7–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA4` | 6.07 Er (1–12) | 4.5% | 6.5% | 1.43 (0–4) | 3.06 (0–21) | 2.18zł (0.0–8.3) | 5.77 (0.7–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 3 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_TIME_DECK_EVERY_2ERAS` | 6.20 Er (1–12) | 5.3% | 6.8% | 1.45 (0–4) | 3.14 (0–22) | 2.03zł (0.0–8.3) | 5.79 (0.3–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED0` | 6.03 Er (1–12) | 3.8% | 6.5% | 1.06 (0–4) | 2.94 (0–22) | 2.20zł (0.0–8.7) | 5.76 (0.5–10.0) | 🟢 W NORMIE |
| `L4_NO_TIME_DECK` | 6.26 Er (1–12) | 5.5% | 7.3% | 1.46 (0–4) | 3.38 (0–23) | 1.88zł (0.0–7.3) | 5.80 (0.3–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.