# Raport Audytu Poziomu 4 (Warianty Niszowe i Modyfikatory) — Wersja Balansu: v0.12

**Wersja Balansu:** `v0.12` | **Data:** 2026-08-14 11:34 | **Przeanalizowano Wariantów:** 8 | **Próba:** 2000 gier/setup | **Czas:** 29.58s
**Wynik Bazy Poziomu 4 (Global):** `🟢 58.3 pkt` | 3p: `82.8 pkt` | 4p: `55.1 pkt` | 5p: `37.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | Baza (Bieżące warianty niszowe i zasady edyktów) | 🟢 ** 58.3** | 82.8 | 55.1 | 37.0 | ⚪ OPTYMALNY |
| `L4_TIME_DECK_EVERY_ERA` | Edykty Czasu: co 1 Erę → co 1 Erę | 🟢 ** 58.3** | 82.8 | 55.1 | 37.0 | ⚪ OPTYMALNY |
| `L4_TIME_DECK_EVERY_2ERAS` | Edykty Czasu: co 1 Erę → co 2 Ery | 58.3 → 🟢 ** 50.4** (`-7.9`) | 82.8 → 64.4 (`-18.4`) | 55.1 → 36.3 (`-18.8`) | 37.0 → 0.0 (`-37.0`) | 🔴 POGARSZA GLOBALNIE |
| `L4_SEA_ROUTE_ERA4` | Szlak Morski: Era 5 → Era 4 | 58.3 → 🟢 ** 60.1** (`⬆️ +1.8`) | 82.8 → 83.0 (`⬆️ +0.2`) | 55.1 → 58.5 (`⬆️ +3.4`) | 37.0 → 38.7 (`⬆️ +1.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L4_SEA_ROUTE_ERA6` | Szlak Morski: Era 5 → Era 6 | 58.3 → 🟢 ** 52.0** (`-6.3`) | 82.8 → 82.7 (`-0.1`) | 55.1 → 38.2 (`-16.9`) | 37.0 → 35.2 (`-1.8`) | 🔴 POGARSZA GLOBALNIE |
| `L4_INQUISITOR_SPEED2` | Inkwizytor Patrol: ruch 1 → 2 | 58.3 → 🟢 ** 58.0** (`-0.3`) | 82.8 → 81.8 (`-1.0`) | 55.1 → 50.2 (`-4.9`) | 37.0 → 42.1 (`⬆️ +5.1`) | ⚪ OPTYMALNY |
| `L4_INQUISITOR_SPEED0` | Inkwizytor Patrol: ruch 1 → 0 | 58.3 → 🟢 ** 61.6** (`⬆️ +3.3`) | 82.8 → 79.5 (`-3.3`) | 55.1 → 63.8 (`⬆️ +8.7`) | 37.0 → 41.6 (`⬆️ +4.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L4_VERDICT_SECRET` | Werdykt: jawny → tajny | 🟢 ** 58.3** | 82.8 | 55.1 | 37.0 | ⚪ OPTYMALNY |

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | 5.57 Er (1–9) | 3.4% | 28.6% | 1.03 (0–3) | 3.71 (0–20) | 0.52zł (0.0–2.7) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L4_TIME_DECK_EVERY_ERA` | 5.57 Er (1–9) | 3.4% | 28.6% | 1.03 (0–3) | 3.71 (0–20) | 0.52zł (0.0–2.7) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L4_TIME_DECK_EVERY_2ERAS` | 5.85 Er (1–9) | 5.5% | 29.5% | 0.75 (0–3) | 3.76 (0–18) | 0.53zł (0.0–3.0) | 6.07 (1.0–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA4` | 5.56 Er (1–9) | 3.4% | 28.6% | 1.03 (0–3) | 3.70 (0–20) | 0.52zł (0.0–2.7) | 6.25 (0.7–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA6` | 5.58 Er (1–9) | 3.4% | 28.6% | 1.04 (0–4) | 3.72 (0–20) | 0.52zł (0.0–2.7) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED2` | 5.58 Er (1–9) | 3.6% | 28.6% | 1.05 (0–4) | 3.71 (0–17) | 0.52zł (0.0–2.7) | 6.28 (0.8–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED0` | 5.38 Er (1–9) | 2.8% | 28.0% | 0.94 (0–3) | 3.72 (0–19) | 0.53zł (0.0–3.3) | 6.09 (0.7–10.0) | 🟢 W NORMIE |
| `L4_VERDICT_SECRET` | 5.57 Er (1–9) | 3.4% | 28.6% | 1.03 (0–3) | 3.71 (0–20) | 0.52zł (0.0–2.7) | 6.26 (0.7–10.0) | 🟢 W NORMIE |

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.