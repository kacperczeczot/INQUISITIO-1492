[Strona główna](../../../../../README.md) > [v0.57](README.md) > [audyt_level4_raport](audyt_level4_raport.md)

---

# Raport Audytu Poziomu 4 (Warianty Niszowe i Edykty) — Wersja Balansu: v0.57

**Wersja Balansu:** `v0.57` | **Data:** 2026-08-16 15:59 | **Przeanalizowano Wariantów:** 9 | **Próba:** 3000 gier/setup | **Czas:** 60.52s
**Wynik Bazy Poziomu 4 (Global):** `🔴 51.6 pkt` | 3p: `66.8 pkt` | 4p: `49.4 pkt` | 5p: `38.5 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (4)

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | Baza (Bieżące warianty niszowe i zasady edyktów) | 🔴 ** 51.6** | 66.8 | 49.4 | 38.5 | ⚪ OPTYMALNY |
| `L4_INQUISITOR_SPEED0` | Inkwizytor Patrol: ruch 1 → 0 | 51.6 → 🟠 ** 60.6** (`⬆️ +9.0`) | 66.8 | 49.4 → 68.6 (`⬆️ +19.2`) | 38.5 → 46.4 (`⬆️ +7.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L4_SEA_ROUTE_ERA4` | Szlak Morski: Era 5 → Era 4 | 51.6 → 🔴 ** 51.9** (`⬆️ +0.3`) | 66.8 → 67.2 (`⬆️ +0.4`) | 49.4 → 49.9 (`⬆️ +0.5`) | 38.5 → 38.7 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA6` | Szlak Morski: Era 5 → Era 6 | 51.6 → 🔴 ** 51.3** (`-0.3`) | 66.8 → 66.3 (`-0.5`) | 49.4 → 49.1 (`-0.3`) | 38.5 → 38.6 (`⬆️ +0.1`) | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 5 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_TIME_DECK_EVERY_ERA` | Edykty Czasu: co 1 Erę → co 1 Erę | 🔴 ** 51.6** | 66.8 | 49.4 | 38.5 | ⚪ OPTYMALNY |
| `L4_INQUISITOR_SPEED2` | Inkwizytor Patrol: ruch 1 → 2 | 51.6 → 🔴 ** 51.0** (`-0.6`) | 66.8 → 66.0 (`-0.8`) | 49.4 → 49.2 (`-0.2`) | 38.5 → 37.7 (`-0.8`) | 🔴 POGARSZA GLOBALNIE |
| `L4_TIME_DECK_EVERY_2ERAS` | Edykty Czasu: co 1 Erę → co 2 Ery | 51.6 → 🔴 ** 45.9** (`-5.7`) | 66.8 → 56.2 (`-10.6`) | 49.4 → 43.2 (`-6.2`) | 38.5 → 38.4 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L4_NO_TIME_DECK` | Kronika Dziejów: Całkowite wyłączenie edyktów | 51.6 → 🔴 ** 36.6** (`-15.0`) | 66.8 → 44.8 (`-22.0`) | 49.4 → 32.4 (`-17.0`) | 38.5 → 32.7 (`-5.8`) | 🔴 POGARSZA GLOBALNIE |
| `L4_VERDICT_SECRET` | Werdykt: jawny → tajny (brak koordynacji anty-snowball) | 51.6 → 🔴 ** 34.3** (`-17.3`) | 66.8 → 50.5 (`-16.3`) | 49.4 → 24.8 (`-24.6`) | 38.5 → 27.7 (`-10.8`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (4)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 1.91zł (0.0–8.3) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED0` | 5.50 Er (1–11) | 0.8% | 25.4% | 1.03 (0–4) | 3.17 (0–19) | 1.92zł (0.0–8.3) | 6.24 (1.0–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA4` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.17 (0–20) | 1.91zł (0.0–8.3) | 6.24 (1.0–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA6` | 5.47 Er (1–11) | 0.8% | 25.4% | 1.38 (0–4) | 3.18 (0–20) | 1.92zł (0.0–8.3) | 6.25 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 5 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_TIME_DECK_EVERY_ERA` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 1.91zł (0.0–8.3) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED2` | 5.43 Er (1–11) | 0.8% | 25.3% | 1.38 (0–4) | 3.14 (0–19) | 1.90zł (0.0–9.3) | 6.25 (0.7–10.0) | 🟢 W NORMIE |
| `L4_TIME_DECK_EVERY_2ERAS` | 5.62 Er (1–11) | 1.2% | 26.8% | 1.40 (0–4) | 3.32 (0–20) | 1.80zł (0.0–9.3) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L4_NO_TIME_DECK` | 5.68 Er (1–11) | 1.4% | 27.8% | 1.41 (0–4) | 3.67 (0–23) | 1.71zł (0.0–8.7) | 6.26 (1.0–10.0) | 🟢 W NORMIE |
| `L4_VERDICT_SECRET` | 5.15 Er (1–11) | 0.5% | 24.1% | 1.27 (0–4) | 2.79 (0–18) | 1.85zł (0.0–9.3) | 5.90 (1.0–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.