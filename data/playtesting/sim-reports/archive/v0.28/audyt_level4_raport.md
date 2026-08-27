# Raport Audytu Poziomu 4 (Warianty Niszowe i Edykty) — Wersja Balansu: v0.28

**Wersja Balansu:** `v0.28` | **Data:** 2026-08-14 18:49 | **Przeanalizowano Wariantów:** 8 | **Próba:** 3000 gier/setup | **Czas:** 49.69s
**Wynik Bazy Poziomu 4 (Global):** `🟢 95.8 pkt` | 3p: `90.0 pkt` | 4p: `98.4 pkt` | 5p: `99.1 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (4)

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | Baza (Bieżące warianty niszowe i zasady edyktów) | 🟢 ** 95.8** | 90.0 | 98.4 | 99.1 | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA6` | Szlak Morski: Era 5 → Era 6 | 95.8 → 🟢 ** 96.1** (`⬆️ +0.3`) | 90.0 → 91.5 (`⬆️ +1.5`) | 98.4 → 98.1 (`-0.3`) | 99.1 → 98.7 (`-0.4`) | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA4` | Szlak Morski: Era 5 → Era 4 | 95.8 → 🟢 ** 95.7** (`-0.1`) | 90.0 → 89.4 (`-0.6`) | 98.4 → 98.7 (`⬆️ +0.3`) | 99.1 → 99.0 (`-0.1`) | ⚪ OPTYMALNY |
| `L4_TIME_DECK_EVERY_2ERAS` | Edykty Czasu: co 1 Erę → co 2 Ery | 95.8 → 🟢 ** 93.2** (`-2.6`) | 90.0 → 89.8 (`-0.2`) | 98.4 → 90.2 (`-8.2`) | 99.1 → 99.6 (`⬆️ +0.5`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 4 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_TIME_DECK_EVERY_ERA` | Edykty Czasu: co 1 Erę → co 1 Erę | 🟢 ** 95.8** | 90.0 | 98.4 | 99.1 | ⚪ OPTYMALNY |
| `L4_VERDICT_SECRET` | Werdykt: jawny → tajny | 🟢 ** 95.8** | 90.0 | 98.4 | 99.1 | ⚪ OPTYMALNY |
| `L4_INQUISITOR_SPEED2` | Inkwizytor Patrol: ruch 1 → 2 | 95.8 → 🟢 ** 94.4** (`-1.4`) | 90.0 → 89.5 (`-0.5`) | 98.4 → 94.7 (`-3.7`) | 99.1 → 98.9 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L4_INQUISITOR_SPEED0` | Inkwizytor Patrol: ruch 1 → 0 | 95.8 → 🟢 ** 88.0** (`-7.8`) | 90.0 → 82.3 (`-7.7`) | 98.4 → 84.5 (`-13.9`) | 99.1 → 97.2 (`-1.9`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (4)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | 5.51 Er (1–10) | 1.2% | 26.4% | 1.02 (0–4) | 3.59 (0–19) | 1.04zł (0.0–4.3) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA6` | 5.52 Er (1–10) | 1.2% | 26.4% | 1.02 (0–4) | 3.60 (0–19) | 1.04zł (0.0–5.0) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA4` | 5.49 Er (1–10) | 1.1% | 26.3% | 1.02 (0–4) | 3.57 (0–19) | 1.03zł (0.0–4.3) | 6.29 (0.7–10.0) | 🟢 W NORMIE |
| `L4_TIME_DECK_EVERY_2ERAS` | 5.72 Er (1–10) | 1.7% | 27.1% | 0.74 (0–4) | 3.55 (0–19) | 1.05zł (0.0–4.7) | 6.09 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 4 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_TIME_DECK_EVERY_ERA` | 5.51 Er (1–10) | 1.2% | 26.4% | 1.02 (0–4) | 3.59 (0–19) | 1.04zł (0.0–4.3) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L4_VERDICT_SECRET` | 5.51 Er (1–10) | 1.2% | 26.4% | 1.02 (0–4) | 3.59 (0–19) | 1.04zł (0.0–4.3) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED2` | 5.52 Er (1–10) | 1.1% | 26.5% | 1.05 (0–4) | 3.58 (0–18) | 1.04zł (0.0–4.7) | 6.33 (0.7–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED0` | 5.32 Er (1–10) | 0.8% | 25.7% | 0.93 (0–3) | 3.58 (0–18) | 1.03zł (0.0–4.7) | 6.14 (1.0–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.