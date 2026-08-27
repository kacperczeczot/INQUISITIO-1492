# Raport Audytu Poziomu 4 (Warianty Niszowe i Edykty) — Wersja Balansu: v0.70

**Wersja Balansu:** `v0.70` | **Data:** 2026-08-16 21:18 | **Przeanalizowano Wariantów:** 8 | **Próba:** 3000 gier/setup | **Czas:** 111.9s
**Wynik Bazy Poziomu 4 (Global):** `🟠 63.8 pkt` | 3p: `72.9 pkt` | 4p: `69.4 pkt` | 5p: `49.1 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (5)

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | Baza (Bieżące warianty niszowe i zasady edyktów) | 🟠 ** 63.8** | 72.9 | 69.4 | 49.1 | ⚪ OPTYMALNY |
| `L4_INQUISITOR_SPEED0` | Inkwizytor Patrol: ruch 1 → 0 | 63.8 → 🟠 ** 72.1** (`⬆️ +8.3`) | 72.9 → 67.6 (`-5.3`) | 69.4 → 81.6 (`⬆️ +12.2`) | 49.1 → 67.1 (`⬆️ +18.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L4_SEA_ROUTE_ERA4` | Szlak Morski: Era 6 → Era 4 | 63.8 → 🟠 ** 65.0** (`⬆️ +1.2`) | 72.9 → 74.6 (`⬆️ +1.7`) | 69.4 → 71.1 (`⬆️ +1.7`) | 49.1 → 49.3 (`⬆️ +0.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L4_SEA_ROUTE_ERA5` | Szlak Morski: Era 6 → Era 5 | 63.8 → 🟠 ** 64.2** (`⬆️ +0.4`) | 72.9 → 73.6 (`⬆️ +0.7`) | 69.4 → 69.9 (`⬆️ +0.5`) | 49.1 → 49.0 (`-0.1`) | ⚪ OPTYMALNY |
| `L4_INQUISITOR_SPEED2` | Inkwizytor Patrol: ruch 1 → 2 | 63.8 → 🟠 ** 63.5** (`-0.3`) | 72.9 → 74.2 (`⬆️ +1.3`) | 69.4 → 69.7 (`⬆️ +0.3`) | 49.1 → 46.5 (`-2.6`) | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 3 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_TIME_DECK_EVERY_2ERAS` | Edykty Czasu: co 1 Erę → co 2 Ery | 63.8 → 🔴 ** 56.4** (`-7.4`) | 72.9 → 67.1 (`-5.8`) | 69.4 → 60.0 (`-9.4`) | 49.1 → 42.2 (`-6.9`) | 🔴 POGARSZA GLOBALNIE |
| `L4_VERDICT_SECRET` | Werdykt: jawny → tajny (brak koordynacji anty-snowball) | 63.8 → 🔴 ** 43.7** (`-20.1`) | 72.9 → 63.7 (`-9.2`) | 69.4 → 40.2 (`-29.2`) | 49.1 → 27.3 (`-21.8`) | 🔴 POGARSZA GLOBALNIE |
| `L4_NO_TIME_DECK` | Kronika Dziejów: Całkowite wyłączenie edyktów | 63.8 → 🔴 ** 39.3** (`-24.5`) | 72.9 → 54.0 (`-18.9`) | 69.4 → 37.9 (`-31.5`) | 49.1 → 25.9 (`-23.2`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (5)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | 5.73 Er (1–12) | 0.6% | 24.9% | 1.48 (0–4) | 3.56 (0–21) | 1.62zł (0.0–7.7) | 6.56 (0.7–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED0` | 5.70 Er (1–12) | 0.6% | 24.8% | 1.11 (0–4) | 3.52 (0–20) | 1.62zł (0.0–7.7) | 6.52 (0.7–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA4` | 5.70 Er (1–12) | 0.6% | 24.8% | 1.47 (0–4) | 3.55 (0–21) | 1.61zł (0.0–7.7) | 6.54 (0.7–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA5` | 5.72 Er (1–12) | 0.6% | 24.9% | 1.48 (0–4) | 3.56 (0–21) | 1.62zł (0.0–7.7) | 6.55 (0.7–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED2` | 5.70 Er (1–12) | 0.5% | 24.9% | 1.48 (0–4) | 3.56 (0–22) | 1.61zł (0.0–7.0) | 6.59 (0.7–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 3 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_TIME_DECK_EVERY_2ERAS` | 5.91 Er (1–12) | 0.8% | 26.2% | 1.51 (0–4) | 3.73 (0–20) | 1.50zł (0.0–7.0) | 6.57 (1.0–10.0) | 🟢 W NORMIE |
| `L4_VERDICT_SECRET` | 5.48 Er (1–12) | 0.4% | 24.0% | 1.40 (0–4) | 3.23 (0–19) | 1.59zł (0.0–7.0) | 6.29 (0.7–10.0) | 🟢 W NORMIE |
| `L4_NO_TIME_DECK` | 5.95 Er (1–12) | 0.9% | 26.9% | 1.50 (0–4) | 4.10 (0–22) | 1.39zł (0.0–7.0) | 6.57 (1.0–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.