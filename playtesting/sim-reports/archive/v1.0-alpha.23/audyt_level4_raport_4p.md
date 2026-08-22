# Raport Audytu Poziomu 4 (Warianty Niszowe i Edykty) — Wersja Balansu: v1.0-alpha.23

**Wersja Balansu:** `v1.0-alpha.23` | **Data:** 2026-08-22 15:31 | **Przeanalizowano Wariantów:** 6 | **Próba:** 3000 gier/setup | **Czas:** 48.16s
**Wynik Bazy Poziomu 4 (Global):** `🟡 81.1 pkt` | 3p: `0.0 pkt` | 4p: `81.1 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (2)

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | Baza (Bieżące warianty niszowe i zasady edyktów) | 🟡 ** 81.1** | 0.0 | 81.1 | 0.0 | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA_PLUS1` | Szlak Morski: Era 4 → 5 | 81.1 → 🟡 ** 81.2** (`⬆️ +0.1`) | 0.0 | 81.1 → 81.2 (`⬆️ +0.1`) | 0.0 | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 4 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_SEA_ROUTE_ERA_MINUS1` | Szlak Morski: Era 4 → 3 | 81.1 → 🟡 ** 80.3** (`-0.8`) | 0.0 | 81.1 → 80.3 (`-0.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L4_TIME_DECK_EVERY_2ERAS` | Edykty Czasu: co 1 Erę → co 2 Ery | 81.1 → 🟡 ** 78.5** (`-2.6`) | 0.0 | 81.1 → 78.5 (`-2.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L4_NO_TIME_DECK` | Kronika Dziejów: Całkowite wyłączenie edyktów | 81.1 → 🟠 ** 73.0** (`-8.1`) | 0.0 | 81.1 → 73.0 (`-8.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L4_INQUISITOR_SPEED0` | Inkwizytor Patrol: ruch 1 → 0 | 81.1 → 🔴 **  2.0** (`-79.1`) | 0.0 | 81.1 → 2.0 (`-79.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (2)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | 6.03 Er (1–14) | 0.1% | 1.5% | 1.72 (0–4) | 3.95 (0–26) | 15.14zł (1.5–45.2) | 6.76 (0.2–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA_PLUS1` | 6.03 Er (1–14) | 0.1% | 1.5% | 1.72 (0–4) | 3.94 (0–22) | 15.15zł (1.5–45.2) | 6.75 (0.2–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 4 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_SEA_ROUTE_ERA_MINUS1` | 6.03 Er (1–14) | 0.1% | 1.5% | 1.72 (0–4) | 3.96 (0–22) | 15.15zł (1.5–45.2) | 6.76 (0.2–10.0) | 🟢 W NORMIE |
| `L4_TIME_DECK_EVERY_2ERAS` | 6.07 Er (1–14) | 0.2% | 1.7% | 1.75 (0–4) | 3.99 (0–21) | 14.78zł (1.5–47.5) | 6.80 (0.2–10.0) | 🟢 W NORMIE |
| `L4_NO_TIME_DECK` | 6.05 Er (1–14) | 0.2% | 1.8% | 1.75 (0–4) | 4.04 (0–21) | 14.27zł (1.5–44.0) | 6.76 (0.2–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED0` | 8.98 Er (1–14) | 27.4% | 0.9% | 0.02 (0–1) | 3.20 (0–22) | 25.24zł (1.5–55.2) | 4.64 (0.2–9.5) | 🔴 PRZEKROCZONE NORMY |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.