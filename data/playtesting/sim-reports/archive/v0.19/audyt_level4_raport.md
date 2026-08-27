[Strona główna](../../../../../README.md) > [v0.19](README.md) > [audyt_level4_raport](audyt_level4_raport.md)

---

# Raport Audytu Poziomu 4 (Warianty Niszowe i Edykty) — Wersja Balansu: v0.19

**Wersja Balansu:** `v0.19` | **Data:** 2026-08-14 13:43 | **Przeanalizowano Wariantów:** 8 | **Próba:** 3000 gier/setup | **Czas:** 44.44s
**Wynik Bazy Poziomu 4 (Global):** `🟢 91.7 pkt` | 3p: `87.1 pkt` | 4p: `88.6 pkt` | 5p: `99.3 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (2)

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | Baza (Bieżące warianty niszowe i zasady edyktów) | 🟢 ** 91.7** | 87.1 | 88.6 | 99.3 | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA4` | Szlak Morski: Era 5 → Era 4 | 91.7 → 🟢 ** 92.4** (`⬆️ +0.7`) | 87.1 → 87.4 (`⬆️ +0.3`) | 88.6 → 90.1 (`⬆️ +1.5`) | 99.3 → 99.6 (`⬆️ +0.3`) | 🟢 POPRAWIA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 6 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_TIME_DECK_EVERY_ERA` | Edykty Czasu: co 1 Erę → co 1 Erę | 🟢 ** 91.7** | 87.1 | 88.6 | 99.3 | ⚪ OPTYMALNY |
| `L4_VERDICT_SECRET` | Werdykt: jawny → tajny | 🟢 ** 91.7** | 87.1 | 88.6 | 99.3 | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA6` | Szlak Morski: Era 5 → Era 6 | 91.7 → 🟢 ** 91.1** (`-0.6`) | 87.1 → 86.7 (`-0.4`) | 88.6 → 87.7 (`-0.9`) | 99.3 → 99.0 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L4_INQUISITOR_SPEED2` | Inkwizytor Patrol: ruch 1 → 2 | 91.7 → 🟢 ** 91.0** (`-0.7`) | 87.1 → 86.8 (`-0.3`) | 88.6 → 88.5 (`-0.1`) | 99.3 → 97.8 (`-1.5`) | 🔴 POGARSZA GLOBALNIE |
| `L4_INQUISITOR_SPEED0` | Inkwizytor Patrol: ruch 1 → 0 | 91.7 → 🟢 ** 88.4** (`-3.3`) | 87.1 → 85.4 (`-1.7`) | 88.6 → 80.9 (`-7.7`) | 99.3 → 99.0 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L4_TIME_DECK_EVERY_2ERAS` | Edykty Czasu: co 1 Erę → co 2 Ery | 91.7 → 🟢 ** 82.9** (`-8.8`) | 87.1 → 71.4 (`-15.7`) | 88.6 → 80.1 (`-8.5`) | 99.3 → 97.3 (`-2.0`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (2)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | 5.51 Er (1–9) | 4.1% | 28.3% | 1.02 (0–4) | 3.53 (0–20) | 0.52zł (0.0–3.0) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA4` | 5.50 Er (1–9) | 4.1% | 28.3% | 1.02 (0–4) | 3.52 (0–20) | 0.52zł (0.0–3.0) | 6.19 (0.7–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 6 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_TIME_DECK_EVERY_ERA` | 5.51 Er (1–9) | 4.1% | 28.3% | 1.02 (0–4) | 3.53 (0–20) | 0.52zł (0.0–3.0) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L4_VERDICT_SECRET` | 5.51 Er (1–9) | 4.1% | 28.3% | 1.02 (0–4) | 3.53 (0–20) | 0.52zł (0.0–3.0) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA6` | 5.51 Er (1–9) | 4.1% | 28.3% | 1.03 (0–4) | 3.54 (0–20) | 0.52zł (0.0–3.0) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED2` | 5.51 Er (1–9) | 4.1% | 28.3% | 1.05 (0–4) | 3.54 (0–17) | 0.52zł (0.0–3.0) | 6.23 (0.8–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED0` | 5.32 Er (1–9) | 3.2% | 27.7% | 0.93 (0–3) | 3.52 (0–19) | 0.52zł (0.0–3.3) | 6.04 (0.7–10.0) | 🟢 W NORMIE |
| `L4_TIME_DECK_EVERY_2ERAS` | 5.70 Er (1–9) | 5.4% | 28.9% | 0.75 (0–3) | 3.46 (0–18) | 0.52zł (0.0–3.0) | 5.98 (1.0–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.