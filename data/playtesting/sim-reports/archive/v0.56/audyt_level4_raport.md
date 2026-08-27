# Raport Audytu Poziomu 4 (Warianty Niszowe i Edykty) — Wersja Balansu: v0.56

**Wersja Balansu:** `v0.56` | **Data:** 2026-08-16 14:38 | **Przeanalizowano Wariantów:** 9 | **Próba:** 3000 gier/setup | **Czas:** 63.22s
**Wynik Bazy Poziomu 4 (Global):** `🟠 66.9 pkt` | 3p: `35.6 pkt` | 4p: `94.9 pkt` | 5p: `70.3 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (7)

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | Baza (Bieżące warianty niszowe i zasady edyktów) | 🟠 ** 66.9** | 35.6 | 94.9 | 70.3 | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA6` | Szlak Morski: Era 5 → Era 6 | 66.9 → 🟠 ** 68.0** (`⬆️ +1.1`) | 35.6 → 34.4 (`-1.2`) | 94.9 → 93.1 (`-1.8`) | 70.3 → 76.4 (`⬆️ +6.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L4_SEA_ROUTE_ERA4` | Szlak Morski: Era 5 → Era 4 | 66.9 → 🟠 ** 65.9** (`-1.0`) | 35.6 → 36.1 (`⬆️ +0.5`) | 94.9 → 94.7 (`-0.2`) | 70.3 → 66.9 (`-3.4`) | 🔴 POGARSZA GLOBALNIE |
| `L4_INQUISITOR_SPEED2` | Inkwizytor Patrol: ruch 1 → 2 | 66.9 → 🔴 ** 58.7** (`-8.2`) | 35.6 → 39.1 (`⬆️ +3.5`) | 94.9 → 92.7 (`-2.2`) | 70.3 → 44.3 (`-26.0`) | 🔴 POGARSZA GLOBALNIE |
| `L4_VERDICT_SECRET` | Werdykt: jawny → tajny (brak koordynacji anty-snowball) | 66.9 → 🔴 ** 42.0** (`-24.9`) | 35.6 → 73.8 (`⬆️ +38.2`) | 94.9 → 10.2 (`-84.7`) | 70.3 → 0.0 (`-70.3`) | 🔴 POGARSZA GLOBALNIE |
| `L4_TIME_DECK_EVERY_2ERAS` | Edykty Czasu: co 1 Erę → co 2 Ery | 66.9 → 🔴 ** 38.3** (`-28.6`) | 35.6 → 37.7 (`⬆️ +2.1`) | 94.9 → 34.7 (`-60.2`) | 70.3 → 42.4 (`-27.9`) | 🔴 POGARSZA GLOBALNIE |
| `L4_NO_TIME_DECK` | Kronika Dziejów: Całkowite wyłączenie edyktów | 66.9 → 🔴 ** 24.9** (`-42.0`) | 35.6 → 36.5 (`⬆️ +0.9`) | 94.9 → 13.2 (`-81.7`) | 70.3 → 0.0 (`-70.3`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 2 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_TIME_DECK_EVERY_ERA` | Edykty Czasu: co 1 Erę → co 1 Erę | 🟠 ** 66.9** | 35.6 | 94.9 | 70.3 | ⚪ OPTYMALNY |
| `L4_INQUISITOR_SPEED0` | Inkwizytor Patrol: ruch 1 → 0 | 66.9 → 🔴 ** 53.3** (`-13.6`) | 35.6 → 35.1 (`-0.5`) | 94.9 → 88.2 (`-6.7`) | 70.3 → 36.7 (`-33.6`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (7)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | 5.95 Er (1–11) | 2.0% | 26.8% | 0.39 (0–3) | 3.55 (0–21) | 2.06zł (0.0–8.7) | 6.11 (1.0–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA6` | 5.96 Er (1–11) | 2.0% | 26.9% | 0.39 (0–3) | 3.56 (0–21) | 2.07zł (0.0–8.7) | 6.12 (1.0–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA4` | 5.93 Er (1–11) | 2.0% | 26.8% | 0.39 (0–3) | 3.52 (0–21) | 2.06zł (0.0–8.7) | 6.10 (1.0–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED2` | 5.92 Er (1–11) | 2.0% | 26.8% | 0.41 (0–3) | 3.53 (0–20) | 2.06zł (0.0–9.0) | 6.13 (0.7–10.0) | 🟢 W NORMIE |
| `L4_VERDICT_SECRET` | 5.59 Er (1–11) | 1.3% | 25.6% | 0.37 (0–3) | 3.10 (0–19) | 1.99zł (0.0–8.7) | 5.76 (1.0–10.0) | 🟢 W NORMIE |
| `L4_TIME_DECK_EVERY_2ERAS` | 6.16 Er (1–11) | 3.1% | 28.4% | 0.38 (0–3) | 3.74 (0–20) | 1.94zł (0.0–9.3) | 6.11 (1.2–10.0) | 🟢 W NORMIE |
| `L4_NO_TIME_DECK` | 6.25 Er (1–11) | 3.4% | 29.6% | 0.37 (0–3) | 4.14 (0–24) | 1.83zł (0.0–7.7) | 6.12 (1.2–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 2 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_TIME_DECK_EVERY_ERA` | 5.95 Er (1–11) | 2.0% | 26.8% | 0.39 (0–3) | 3.55 (0–21) | 2.06zł (0.0–8.7) | 6.11 (1.0–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED0` | 5.92 Er (1–11) | 2.0% | 26.7% | 0.32 (0–3) | 3.53 (0–19) | 2.06zł (0.0–9.7) | 6.10 (1.0–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.