# Raport Audytu Poziomu 4 (Warianty Niszowe i Edykty) — Wersja Balansu: v0.35

**Wersja Balansu:** `v0.35` | **Data:** 2026-08-15 22:33 | **Przeanalizowano Wariantów:** 8 | **Próba:** 1000 gier/setup | **Czas:** 29.25s
**Wynik Bazy Poziomu 4 (Global):** `🟢 91.0 pkt` | 3p: `92.4 pkt` | 4p: `89.6 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (5)

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | Baza (Bieżące warianty niszowe i zasady edyktów) | 🟢 ** 91.0** | 92.4 | 89.6 | 0.0 | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA4` | Szlak Morski: Era 5 → Era 4 | 91.0 → 🟢 ** 92.4** (`⬆️ +1.4`) | 92.4 → 92.3 (`-0.1`) | 89.6 → 92.5 (`⬆️ +2.9`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L4_INQUISITOR_SPEED2` | Inkwizytor Patrol: ruch 1 → 2 | 91.0 → 🟢 ** 90.6** (`-0.4`) | 92.4 → 90.1 (`-2.3`) | 89.6 → 91.1 (`⬆️ +1.5`) | 0.0 | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA6` | Szlak Morski: Era 5 → Era 6 | 91.0 → 🟠 ** 74.5** (`-16.5`) | 92.4 → 91.8 (`-0.6`) | 89.6 → 90.9 (`⬆️ +1.3`) | 0.0 → 40.9 (`⬆️ +40.9`) | 🔴 POGARSZA GLOBALNIE |
| `L4_INQUISITOR_SPEED0` | Inkwizytor Patrol: ruch 1 → 0 | 91.0 → 🔴 ** 53.3** (`-37.7`) | 92.4 → 92.6 (`⬆️ +0.2`) | 89.6 → 42.2 (`-47.4`) | 0.0 → 25.0 (`⬆️ +25.0`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 3 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_TIME_DECK_EVERY_ERA` | Edykty Czasu: co 1 Erę → co 1 Erę | 🟢 ** 91.0** | 92.4 | 89.6 | 0.0 | ⚪ OPTYMALNY |
| `L4_VERDICT_SECRET` | Werdykt: jawny → tajny | 🟢 ** 91.0** | 92.4 | 89.6 | 0.0 | ⚪ OPTYMALNY |
| `L4_TIME_DECK_EVERY_2ERAS` | Edykty Czasu: co 1 Erę → co 2 Ery | 91.0 → 🔴 ** 50.2** (`-40.8`) | 92.4 → 66.2 (`-26.2`) | 89.6 → 34.3 (`-55.3`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (5)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | 5.84 Er (1–10) | 2.3% | 25.9% | 0.56 (0–3) | 3.51 (0–18) | 1.57zł (0.0–5.7) | 6.13 (1.0–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA4` | 5.83 Er (1–10) | 2.3% | 25.8% | 0.56 (0–3) | 3.50 (0–18) | 1.57zł (0.0–5.7) | 6.12 (1.0–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED2` | 5.84 Er (1–10) | 2.2% | 25.9% | 0.58 (0–3) | 3.51 (0–17) | 1.56zł (0.0–6.3) | 6.15 (0.7–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA6` | 5.85 Er (1–10) | 2.3% | 25.9% | 0.56 (0–3) | 3.52 (0–18) | 1.57zł (0.0–5.7) | 6.14 (1.0–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED0` | 5.63 Er (1–10) | 1.8% | 25.2% | 0.50 (0–3) | 3.54 (0–16) | 1.56zł (0.0–5.7) | 6.07 (0.8–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 3 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_TIME_DECK_EVERY_ERA` | 5.84 Er (1–10) | 2.3% | 25.9% | 0.56 (0–3) | 3.51 (0–18) | 1.57zł (0.0–5.7) | 6.13 (1.0–10.0) | 🟢 W NORMIE |
| `L4_VERDICT_SECRET` | 5.84 Er (1–10) | 2.3% | 25.9% | 0.56 (0–3) | 3.51 (0–18) | 1.57zł (0.0–5.7) | 6.13 (1.0–10.0) | 🟢 W NORMIE |
| `L4_TIME_DECK_EVERY_2ERAS` | 6.05 Er (1–10) | 3.3% | 27.2% | 0.53 (0–3) | 3.59 (0–20) | 1.43zł (0.0–5.0) | 6.07 (0.7–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.