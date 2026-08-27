[Strona główna](../../../../../README.md) > [v0.16](README.md) > [audyt_level4_raport](audyt_level4_raport.md)

---

# Raport Audytu Poziomu 4 (Warianty Niszowe i Edykty) — Wersja Balansu: v0.16

**Wersja Balansu:** `v0.16` | **Data:** 2026-08-14 12:49 | **Przeanalizowano Wariantów:** 8 | **Próba:** 2000 gier/setup | **Czas:** 29.87s
**Wynik Bazy Poziomu 4 (Global):** `🟢 81.2 pkt` | 3p: `90.5 pkt` | 4p: `71.1 pkt` | 5p: `82.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (6)

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | Baza (Bieżące warianty niszowe i zasady edyktów) | 🟢 ** 81.2** | 90.5 | 71.1 | 82.0 | ⚪ OPTYMALNY |
| `L4_TIME_DECK_EVERY_2ERAS` | Edykty Czasu: co 1 Erę → co 2 Ery | 81.2 → 🟢 ** 85.9** (`⬆️ +4.7`) | 90.5 → 79.9 (`-10.6`) | 71.1 → 79.7 (`⬆️ +8.6`) | 82.0 → 98.2 (`⬆️ +16.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L4_SEA_ROUTE_ERA4` | Szlak Morski: Era 5 → Era 4 | 81.2 → 🟢 ** 81.5** (`⬆️ +0.3`) | 90.5 → 90.6 (`⬆️ +0.1`) | 71.1 → 73.8 (`⬆️ +2.7`) | 82.0 → 80.1 (`-1.9`) | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA6` | Szlak Morski: Era 5 → Era 6 | 81.2 → 🟢 ** 80.0** (`-1.2`) | 90.5 → 90.1 (`-0.4`) | 71.1 → 66.1 (`-5.0`) | 82.0 → 83.9 (`⬆️ +1.9`) | 🔴 POGARSZA GLOBALNIE |
| `L4_INQUISITOR_SPEED0` | Inkwizytor Patrol: ruch 1 → 0 | 81.2 → 🟢 ** 75.0** (`-6.2`) | 90.5 → 85.8 (`-4.7`) | 71.1 → 55.2 (`-15.9`) | 82.0 → 84.0 (`⬆️ +2.0`) | 🔴 POGARSZA GLOBALNIE |
| `L4_INQUISITOR_SPEED2` | Inkwizytor Patrol: ruch 1 → 2 | 81.2 → 🟢 ** 72.7** (`-8.5`) | 90.5 → 89.4 (`-1.1`) | 71.1 → 74.8 (`⬆️ +3.7`) | 82.0 → 54.0 (`-28.0`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 2 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_TIME_DECK_EVERY_ERA` | Edykty Czasu: co 1 Erę → co 1 Erę | 🟢 ** 81.2** | 90.5 | 71.1 | 82.0 | ⚪ OPTYMALNY |
| `L4_VERDICT_SECRET` | Werdykt: jawny → tajny | 🟢 ** 81.2** | 90.5 | 71.1 | 82.0 | ⚪ OPTYMALNY |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (6)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | 5.61 Er (1–9) | 3.1% | 28.6% | 1.04 (0–3) | 3.65 (0–18) | 0.52zł (0.0–2.7) | 6.27 (0.7–10.0) | 🟢 W NORMIE |
| `L4_TIME_DECK_EVERY_2ERAS` | 5.81 Er (1–9) | 4.5% | 29.2% | 0.74 (0–3) | 3.60 (0–18) | 0.52zł (0.0–3.0) | 6.03 (1.0–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA4` | 5.60 Er (1–9) | 3.1% | 28.6% | 1.04 (0–3) | 3.64 (0–18) | 0.52zł (0.0–2.7) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA6` | 5.62 Er (1–9) | 3.2% | 28.7% | 1.04 (0–4) | 3.66 (0–18) | 0.52zł (0.0–2.7) | 6.28 (0.7–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED0` | 5.42 Er (1–9) | 2.6% | 28.1% | 0.95 (0–3) | 3.66 (0–19) | 0.52zł (0.0–3.3) | 6.11 (0.7–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED2` | 5.61 Er (1–9) | 3.2% | 28.6% | 1.06 (0–4) | 3.65 (0–17) | 0.52zł (0.0–2.7) | 6.29 (0.8–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 2 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_TIME_DECK_EVERY_ERA` | 5.61 Er (1–9) | 3.1% | 28.6% | 1.04 (0–3) | 3.65 (0–18) | 0.52zł (0.0–2.7) | 6.27 (0.7–10.0) | 🟢 W NORMIE |
| `L4_VERDICT_SECRET` | 5.61 Er (1–9) | 3.1% | 28.6% | 1.04 (0–3) | 3.65 (0–18) | 0.52zł (0.0–2.7) | 6.27 (0.7–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.