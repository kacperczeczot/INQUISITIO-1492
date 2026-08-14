# Raport Audytu Poziomu 4 (Warianty Niszowe i Edykty) — Wersja Balansu: v0.23

**Wersja Balansu:** `v0.23` | **Data:** 2026-08-14 14:32 | **Przeanalizowano Wariantów:** 8 | **Próba:** 500 gier/setup | **Czas:** 9.19s
**Wynik Bazy Poziomu 4 (Global):** `🟢 88.6 pkt` | 3p: `78.5 pkt` | 4p: `88.4 pkt` | 5p: `98.8 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (5)

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | Baza (Bieżące warianty niszowe i zasady edyktów) | 🟢 ** 88.6** | 78.5 | 88.4 | 98.8 | ⚪ OPTYMALNY |
| `L4_INQUISITOR_SPEED0` | Inkwizytor Patrol: ruch 1 → 0 | 88.6 → 🟢 ** 90.1** (`⬆️ +1.5`) | 78.5 → 82.7 (`⬆️ +4.2`) | 88.4 → 90.6 (`⬆️ +2.2`) | 98.8 → 97.0 (`-1.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L4_SEA_ROUTE_ERA4` | Szlak Morski: Era 5 → Era 4 | 88.6 → 🟢 ** 88.7** (`⬆️ +0.1`) | 78.5 → 77.5 (`-1.0`) | 88.4 → 89.6 (`⬆️ +1.2`) | 98.8 → 98.9 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA6` | Szlak Morski: Era 5 → Era 6 | 88.6 → 🟢 ** 87.8** (`-0.8`) | 78.5 → 79.4 (`⬆️ +0.9`) | 88.4 → 85.7 (`-2.7`) | 98.8 → 98.2 (`-0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L4_INQUISITOR_SPEED2` | Inkwizytor Patrol: ruch 1 → 2 | 88.6 → 🟢 ** 87.4** (`-1.2`) | 78.5 → 87.5 (`⬆️ +9.0`) | 88.4 → 76.2 (`-12.2`) | 98.8 → 98.6 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 3 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_TIME_DECK_EVERY_ERA` | Edykty Czasu: co 1 Erę → co 1 Erę | 🟢 ** 88.6** | 78.5 | 88.4 | 98.8 | ⚪ OPTYMALNY |
| `L4_VERDICT_SECRET` | Werdykt: jawny → tajny | 🟢 ** 88.6** | 78.5 | 88.4 | 98.8 | ⚪ OPTYMALNY |
| `L4_TIME_DECK_EVERY_2ERAS` | Edykty Czasu: co 1 Erę → co 2 Ery | 88.6 → 🟢 ** 75.5** (`-13.1`) | 78.5 → 74.0 (`-4.5`) | 88.4 → 67.6 (`-20.8`) | 98.8 → 85.0 (`-13.8`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (5)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | 5.67 Er (1–9) | 4.7% | 29.2% | 1.05 (0–4) | 3.55 (0–17) | 0.58zł (0.0–3.0) | 6.06 (1.2–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED0` | 5.48 Er (1–9) | 3.5% | 28.6% | 0.94 (0–3) | 3.56 (0–15) | 0.58zł (0.0–3.0) | 5.91 (1.2–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA4` | 5.66 Er (1–9) | 4.7% | 29.2% | 1.04 (0–4) | 3.53 (0–17) | 0.58zł (0.0–3.0) | 6.05 (1.2–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA6` | 5.68 Er (1–9) | 4.7% | 29.3% | 1.05 (0–4) | 3.56 (0–17) | 0.58zł (0.0–3.0) | 6.07 (1.2–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED2` | 5.65 Er (1–9) | 4.5% | 29.2% | 1.05 (0–4) | 3.55 (0–16) | 0.59zł (0.0–3.0) | 6.06 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 3 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_TIME_DECK_EVERY_ERA` | 5.67 Er (1–9) | 4.7% | 29.2% | 1.05 (0–4) | 3.55 (0–17) | 0.58zł (0.0–3.0) | 6.06 (1.2–10.0) | 🟢 W NORMIE |
| `L4_VERDICT_SECRET` | 5.67 Er (1–9) | 4.7% | 29.2% | 1.05 (0–4) | 3.55 (0–17) | 0.58zł (0.0–3.0) | 6.06 (1.2–10.0) | 🟢 W NORMIE |
| `L4_TIME_DECK_EVERY_2ERAS` | 5.86 Er (1–9) | 6.1% | 29.8% | 0.76 (0–3) | 3.45 (0–16) | 0.58zł (0.0–3.0) | 5.80 (1.2–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.