# Raport Audytu Poziomu 4 (Warianty Niszowe i Edykty) — Wersja Balansu: v1.0-alpha.23

**Wersja Balansu:** `v1.0-alpha.23` | **Data:** 2026-08-22 14:58 | **Przeanalizowano Wariantów:** 6 | **Próba:** 3000 gier/setup | **Czas:** 46.77s
**Wynik Bazy Poziomu 4 (Global):** `🟡 82.9 pkt` | 3p: `0.0 pkt` | 4p: `82.9 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (2)

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | Baza (Bieżące warianty niszowe i zasady edyktów) | 🟡 ** 82.9** | 0.0 | 82.9 | 0.0 | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA_PLUS1` | Szlak Morski: Era 4 → 5 | 82.9 → 🟡 ** 83.1** (`⬆️ +0.2`) | 0.0 | 82.9 → 83.1 (`⬆️ +0.2`) | 0.0 | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 4 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_SEA_ROUTE_ERA_MINUS1` | Szlak Morski: Era 4 → 3 | 🟡 ** 82.9** | 0.0 | 82.9 | 0.0 | ⚪ OPTYMALNY |
| `L4_TIME_DECK_EVERY_2ERAS` | Edykty Czasu: co 1 Erę → co 2 Ery | 82.9 → 🟡 ** 79.3** (`-3.6`) | 0.0 | 82.9 → 79.3 (`-3.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L4_NO_TIME_DECK` | Kronika Dziejów: Całkowite wyłączenie edyktów | 82.9 → 🟡 ** 75.7** (`-7.2`) | 0.0 | 82.9 → 75.7 (`-7.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L4_INQUISITOR_SPEED0` | Inkwizytor Patrol: ruch 1 → 0 | 82.9 → 🔴 **  2.4** (`-80.5`) | 0.0 | 82.9 → 2.4 (`-80.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (2)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | 5.91 Er (1–14) | 0.2% | 1.2% | 1.67 (0–4) | 4.25 (0–20) | 15.38zł (1.5–46.8) | 6.99 (0.2–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA_PLUS1` | 5.91 Er (1–14) | 0.2% | 1.2% | 1.67 (0–4) | 4.26 (0–20) | 15.40zł (1.5–46.8) | 6.99 (0.2–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 4 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_SEA_ROUTE_ERA_MINUS1` | 5.90 Er (1–14) | 0.2% | 1.2% | 1.67 (0–4) | 4.25 (0–20) | 15.38zł (1.5–46.8) | 6.99 (0.2–10.0) | 🟢 W NORMIE |
| `L4_TIME_DECK_EVERY_2ERAS` | 5.95 Er (1–14) | 0.1% | 1.4% | 1.70 (0–4) | 4.34 (0–23) | 15.04zł (1.5–47.5) | 7.05 (0.2–10.0) | 🟢 W NORMIE |
| `L4_NO_TIME_DECK` | 5.92 Er (1–14) | 0.1% | 1.5% | 1.69 (0–4) | 4.55 (0–20) | 14.50zł (1.5–44.5) | 7.03 (0.2–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED0` | 9.25 Er (1–14) | 37.0% | 0.7% | 0.01 (0–1) | 3.29 (0–21) | 27.35zł (1.5–55.8) | 4.62 (0.2–10.0) | 🔴 PRZEKROCZONE NORMY |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.