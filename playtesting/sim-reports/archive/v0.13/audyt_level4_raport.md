# Raport Audytu Poziomu 4 (Warianty Niszowe i Modyfikatory) — Wersja Balansu: v0.13

**Wersja Balansu:** `v0.13` | **Data:** 2026-08-14 11:46 | **Przeanalizowano Wariantów:** 8 | **Próba:** 1000 gier/setup | **Czas:** 14.72s
**Wynik Bazy Poziomu 4 (Global):** `🟢 76.6 pkt` | 3p: `91.1 pkt` | 4p: `57.7 pkt` | 5p: `81.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | Baza (Bieżące warianty niszowe i zasady edyktów) | 🟢 ** 76.6** | 91.1 | 57.7 | 81.0 | ⚪ OPTYMALNY |
| `L4_TIME_DECK_EVERY_ERA` | Edykty Czasu: co 1 Erę → co 1 Erę | 🟢 ** 76.6** | 91.1 | 57.7 | 81.0 | ⚪ OPTYMALNY |
| `L4_TIME_DECK_EVERY_2ERAS` | Edykty Czasu: co 1 Erę → co 2 Ery | 76.6 → 🟢 ** 80.0** (`⬆️ +3.4`) | 91.1 → 81.3 (`-9.8`) | 57.7 → 61.7 (`⬆️ +4.0`) | 81.0 → 97.0 (`⬆️ +16.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L4_SEA_ROUTE_ERA4` | Szlak Morski: Era 5 → Era 4 | 76.6 → 🟢 ** 76.5** (`-0.1`) | 91.1 → 91.3 (`⬆️ +0.2`) | 57.7 → 58.5 (`⬆️ +0.8`) | 81.0 → 79.7 (`-1.3`) | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA6` | Szlak Morski: Era 5 → Era 6 | 76.6 → 🟢 ** 76.3** (`-0.3`) | 91.1 → 89.9 (`-1.2`) | 57.7 → 56.7 (`-1.0`) | 81.0 → 82.3 (`⬆️ +1.3`) | ⚪ OPTYMALNY |
| `L4_INQUISITOR_SPEED2` | Inkwizytor Patrol: ruch 1 → 2 | 76.6 → 🟢 ** 80.3** (`⬆️ +3.7`) | 91.1 → 89.5 (`-1.6`) | 57.7 → 55.7 (`-2.0`) | 81.0 → 95.7 (`⬆️ +14.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L4_INQUISITOR_SPEED0` | Inkwizytor Patrol: ruch 1 → 0 | 76.6 → 🟢 ** 64.7** (`-11.9`) | 91.1 → 86.0 (`-5.1`) | 57.7 → 51.6 (`-6.1`) | 81.0 → 56.4 (`-24.6`) | 🔴 POGARSZA GLOBALNIE |
| `L4_VERDICT_SECRET` | Werdykt: jawny → tajny | 🟢 ** 76.6** | 91.1 | 57.7 | 81.0 | ⚪ OPTYMALNY |

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | 5.61 Er (1–9) | 3.3% | 28.7% | 1.03 (0–3) | 3.74 (0–15) | 0.52zł (0.0–2.7) | 6.28 (0.7–10.0) | 🟢 W NORMIE |
| `L4_TIME_DECK_EVERY_ERA` | 5.61 Er (1–9) | 3.3% | 28.7% | 1.03 (0–3) | 3.74 (0–15) | 0.52zł (0.0–2.7) | 6.28 (0.7–10.0) | 🟢 W NORMIE |
| `L4_TIME_DECK_EVERY_2ERAS` | 5.82 Er (1–9) | 4.6% | 29.3% | 0.74 (0–3) | 3.70 (0–18) | 0.52zł (0.0–2.7) | 6.05 (1.2–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA4` | 5.61 Er (1–9) | 3.3% | 28.7% | 1.03 (0–3) | 3.72 (0–18) | 0.52zł (0.0–2.7) | 6.27 (0.7–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA6` | 5.62 Er (1–9) | 3.3% | 28.7% | 1.03 (0–3) | 3.75 (0–15) | 0.52zł (0.0–2.7) | 6.29 (0.7–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED2` | 5.63 Er (1–9) | 3.5% | 28.8% | 1.05 (0–3) | 3.72 (0–17) | 0.52zł (0.0–2.7) | 6.29 (0.8–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED0` | 5.42 Er (1–9) | 2.6% | 28.1% | 0.94 (0–3) | 3.75 (0–19) | 0.52zł (0.0–3.3) | 6.11 (0.7–10.0) | 🟢 W NORMIE |
| `L4_VERDICT_SECRET` | 5.61 Er (1–9) | 3.3% | 28.7% | 1.03 (0–3) | 3.74 (0–15) | 0.52zł (0.0–2.7) | 6.28 (0.7–10.0) | 🟢 W NORMIE |

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.