# Raport Audytu Poziomu 4 (Warianty Niszowe i Edykty) — Wersja Balansu: v0.29

**Wersja Balansu:** `v0.29` | **Data:** 2026-08-14 23:15 | **Przeanalizowano Wariantów:** 8 | **Próba:** 20000 gier/setup | **Czas:** 345.2s
**Wynik Bazy Poziomu 4 (Global):** `🟢 96.2 pkt` | 3p: `91.5 pkt` | 4p: `98.3 pkt` | 5p: `98.9 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (4)

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | Baza (Bieżące warianty niszowe i zasady edyktów) | 🟢 ** 96.2** | 91.5 | 98.3 | 98.9 | ⚪ OPTYMALNY |
| `L4_INQUISITOR_SPEED2` | Inkwizytor Patrol: ruch 1 → 2 | 96.2 → 🟢 ** 95.6** (`-0.6`) | 91.5 → 91.8 (`⬆️ +0.3`) | 98.3 → 95.9 (`-2.4`) | 98.9 → 99.0 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L4_SEA_ROUTE_ERA4` | Szlak Morski: Era 5 → Era 4 | 96.2 → 🟢 ** 93.5** (`-2.7`) | 91.5 → 83.7 (`-7.8`) | 98.3 → 98.5 (`⬆️ +0.2`) | 98.9 → 98.3 (`-0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L4_TIME_DECK_EVERY_2ERAS` | Edykty Czasu: co 1 Erę → co 2 Ery | 96.2 → 🟢 ** 92.2** (`-4.0`) | 91.5 → 89.8 (`-1.7`) | 98.3 → 87.0 (`-11.3`) | 98.9 → 99.8 (`⬆️ +0.9`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 4 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_TIME_DECK_EVERY_ERA` | Edykty Czasu: co 1 Erę → co 1 Erę | 🟢 ** 96.2** | 91.5 | 98.3 | 98.9 | ⚪ OPTYMALNY |
| `L4_VERDICT_SECRET` | Werdykt: jawny → tajny | 🟢 ** 96.2** | 91.5 | 98.3 | 98.9 | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA6` | Szlak Morski: Era 5 → Era 6 | 96.2 → 🟢 ** 96.0** (`-0.2`) | 91.5 → 91.2 (`-0.3`) | 98.3 → 98.0 (`-0.3`) | 98.9 | ⚪ OPTYMALNY |
| `L4_INQUISITOR_SPEED0` | Inkwizytor Patrol: ruch 1 → 0 | 96.2 → 🟢 ** 84.3** (`-11.9`) | 91.5 → 81.9 (`-9.6`) | 98.3 → 84.5 (`-13.8`) | 98.9 → 86.6 (`-12.3`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (4)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | 5.51 Er (1–10) | 1.1% | 26.2% | 1.03 (0–4) | 3.57 (0–19) | 1.16zł (0.0–5.0) | 6.30 (0.3–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED2` | 5.52 Er (1–10) | 1.1% | 26.2% | 1.05 (0–4) | 3.58 (0–21) | 1.17zł (0.0–5.3) | 6.33 (0.6–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA4` | 5.50 Er (1–10) | 1.1% | 26.1% | 1.02 (0–4) | 3.55 (0–19) | 1.16zł (0.0–5.0) | 6.29 (0.3–10.0) | 🟢 W NORMIE |
| `L4_TIME_DECK_EVERY_2ERAS` | 5.72 Er (1–10) | 1.8% | 26.9% | 0.74 (0–4) | 3.54 (0–20) | 1.18zł (0.0–5.3) | 6.09 (0.3–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 4 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_TIME_DECK_EVERY_ERA` | 5.51 Er (1–10) | 1.1% | 26.2% | 1.03 (0–4) | 3.57 (0–19) | 1.16zł (0.0–5.0) | 6.30 (0.3–10.0) | 🟢 W NORMIE |
| `L4_VERDICT_SECRET` | 5.51 Er (1–10) | 1.1% | 26.2% | 1.03 (0–4) | 3.57 (0–19) | 1.16zł (0.0–5.0) | 6.30 (0.3–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA6` | 5.52 Er (1–10) | 1.1% | 26.2% | 1.03 (0–4) | 3.58 (0–19) | 1.17zł (0.0–5.3) | 6.31 (0.3–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED0` | 5.32 Er (1–10) | 0.9% | 25.5% | 0.94 (0–4) | 3.58 (0–21) | 1.15zł (0.0–5.0) | 6.14 (0.3–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.