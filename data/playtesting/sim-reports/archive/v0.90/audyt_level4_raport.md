[Strona główna](../../../../../README.md) > [v0.90](README.md) > [audyt_level4_raport](audyt_level4_raport.md)

---

# Raport Audytu Poziomu 4 (Warianty Niszowe i Edykty) — Wersja Balansu: v0.90

**Wersja Balansu:** `v0.90` | **Data:** 2026-08-17 13:22 | **Przeanalizowano Wariantów:** 8 | **Próba:** 250 gier/setup | **Czas:** 12.13s
**Wynik Bazy Poziomu 4 (Global):** `🔴 20.3 pkt` | 3p: `26.3 pkt` | 4p: `24.4 pkt` | 5p: `10.2 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (5)

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | Baza (Bieżące warianty niszowe i zasady edyktów) | 🔴 ** 20.3** | 26.3 | 24.4 | 10.2 | ⚪ OPTYMALNY |
| `L4_INQUISITOR_SPEED0` | Inkwizytor Patrol: ruch 1 → 0 | 20.3 → 🔴 ** 31.9** (`⬆️ +11.6`) | 26.3 → 22.4 (`-3.9`) | 24.4 → 51.6 (`⬆️ +27.2`) | 10.2 → 21.6 (`⬆️ +11.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L4_SEA_ROUTE_ERA5` | Szlak Morski: Era 4 → Era 5 | 20.3 → 🔴 ** 20.4** (`⬆️ +0.1`) | 26.3 → 26.1 (`-0.2`) | 24.4 → 24.8 (`⬆️ +0.4`) | 10.2 | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA6` | Szlak Morski: Era 4 → Era 6 | 🔴 ** 20.3** | 26.3 → 26.0 (`-0.3`) | 24.4 → 24.9 (`⬆️ +0.5`) | 10.2 → 10.0 (`-0.2`) | ⚪ OPTYMALNY |
| `L4_INQUISITOR_SPEED2` | Inkwizytor Patrol: ruch 1 → 2 | 20.3 → 🔴 ** 20.0** (`-0.3`) | 26.3 → 27.7 (`⬆️ +1.4`) | 24.4 → 22.8 (`-1.6`) | 10.2 → 9.6 (`-0.6`) | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 3 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_VERDICT_SECRET` | Werdykt: jawny → tajny (brak koordynacji anty-snowball) | 20.3 → 🔴 ** 18.0** (`-2.3`) | 26.3 → 24.8 (`-1.5`) | 24.4 → 23.2 (`-1.2`) | 10.2 → 6.0 (`-4.2`) | 🔴 POGARSZA GLOBALNIE |
| `L4_TIME_DECK_EVERY_2ERAS` | Edykty Czasu: co 1 Erę → co 2 Ery | 20.3 → 🔴 ** 14.7** (`-5.6`) | 26.3 → 17.5 (`-8.8`) | 24.4 → 17.3 (`-7.1`) | 10.2 → 9.3 (`-0.9`) | 🔴 POGARSZA GLOBALNIE |
| `L4_NO_TIME_DECK` | Kronika Dziejów: Całkowite wyłączenie edyktów | 20.3 → 🔴 **  8.6** (`-11.7`) | 26.3 → 9.5 (`-16.8`) | 24.4 → 10.8 (`-13.6`) | 10.2 → 5.4 (`-4.8`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (5)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | 6.34 Er (1–12) | 3.7% | 5.2% | 1.80 (0–4) | 4.02 (0–20) | 3.64zł (0.0–10.7) | 6.49 (1.0–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED0` | 6.75 Er (1–12) | 5.6% | 5.1% | 1.12 (0–4) | 4.23 (0–19) | 3.90zł (0.3–12.3) | 6.41 (1.0–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA5` | 6.33 Er (1–12) | 3.7% | 5.2% | 1.80 (0–4) | 4.01 (0–20) | 3.64zł (0.0–10.7) | 6.48 (1.0–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA6` | 6.33 Er (1–12) | 3.7% | 5.2% | 1.80 (0–4) | 4.01 (0–20) | 3.64zł (0.0–10.7) | 6.48 (1.0–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED2` | 6.21 Er (1–12) | 3.1% | 5.2% | 1.81 (0–4) | 3.95 (0–23) | 3.61zł (0.0–11.0) | 6.48 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 3 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_VERDICT_SECRET` | 5.96 Er (1–12) | 2.7% | 5.3% | 1.67 (0–4) | 3.57 (0–21) | 3.50zł (0.0–10.7) | 6.14 (1.0–10.0) | 🟢 W NORMIE |
| `L4_TIME_DECK_EVERY_2ERAS` | 6.52 Er (1–12) | 4.5% | 5.4% | 1.88 (0–4) | 4.22 (0–21) | 3.50zł (0.0–10.3) | 6.55 (1.0–10.0) | 🟢 W NORMIE |
| `L4_NO_TIME_DECK` | 6.53 Er (1–12) | 5.2% | 5.6% | 1.87 (0–4) | 4.71 (0–22) | 3.35zł (0.0–10.0) | 6.55 (1.0–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.