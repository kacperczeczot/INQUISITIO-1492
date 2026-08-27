[Strona główna](../../../../../README.md) > [v0.88](README.md) > [audyt_level4_raport](audyt_level4_raport.md)

---

# Raport Audytu Poziomu 4 (Warianty Niszowe i Edykty) — Wersja Balansu: v0.88

**Wersja Balansu:** `v0.88` | **Data:** 2026-08-17 13:20 | **Przeanalizowano Wariantów:** 8 | **Próba:** 250 gier/setup | **Czas:** 6.02s
**Wynik Bazy Poziomu 4 (Global):** `🔴 27.1 pkt` | 3p: `24.8 pkt` | 4p: `34.8 pkt` | 5p: `21.7 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (6)

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | Baza (Bieżące warianty niszowe i zasady edyktów) | 🔴 ** 27.1** | 24.8 | 34.8 | 21.7 | ⚪ OPTYMALNY |
| `L4_INQUISITOR_SPEED0` | Inkwizytor Patrol: ruch 1 → 0 | 27.1 → 🔴 ** 28.1** (`⬆️ +1.0`) | 24.8 → 22.4 (`-2.4`) | 34.8 → 40.2 (`⬆️ +5.4`) | 21.7 → 21.6 (`-0.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L4_INQUISITOR_SPEED2` | Inkwizytor Patrol: ruch 1 → 2 | 27.1 → 🔴 ** 28.1** (`⬆️ +1.0`) | 24.8 → 25.3 (`⬆️ +0.5`) | 34.8 → 36.8 (`⬆️ +2.0`) | 21.7 → 22.2 (`⬆️ +0.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L4_SEA_ROUTE_ERA5` | Szlak Morski: Era 4 → Era 5 | 27.1 → 🔴 ** 27.0** (`-0.1`) | 24.8 → 24.7 (`-0.1`) | 34.8 → 35.0 (`⬆️ +0.2`) | 21.7 → 21.4 (`-0.3`) | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA6` | Szlak Morski: Era 4 → Era 6 | 27.1 → 🔴 ** 26.8** (`-0.3`) | 24.8 → 24.4 (`-0.4`) | 34.8 → 34.9 (`⬆️ +0.1`) | 21.7 → 21.2 (`-0.5`) | ⚪ OPTYMALNY |
| `L4_VERDICT_SECRET` | Werdykt: jawny → tajny (brak koordynacji anty-snowball) | 27.1 → 🔴 ** 21.9** (`-5.2`) | 24.8 → 31.7 (`⬆️ +6.9`) | 34.8 → 24.8 (`-10.0`) | 21.7 → 9.1 (`-12.6`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 2 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_TIME_DECK_EVERY_2ERAS` | Edykty Czasu: co 1 Erę → co 2 Ery | 27.1 → 🔴 ** 17.6** (`-9.5`) | 24.8 → 14.2 (`-10.6`) | 34.8 → 22.0 (`-12.8`) | 21.7 → 16.6 (`-5.1`) | 🔴 POGARSZA GLOBALNIE |
| `L4_NO_TIME_DECK` | Kronika Dziejów: Całkowite wyłączenie edyktów | 27.1 → 🔴 ** 12.7** (`-14.4`) | 24.8 → 8.4 (`-16.4`) | 34.8 → 17.6 (`-17.2`) | 21.7 → 12.0 (`-9.7`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (6)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | 6.73 Er (1–12) | 5.5% | 5.1% | 1.62 (0–4) | 4.33 (0–22) | 3.84zł (0.0–11.3) | 6.53 (1.0–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED0` | 6.75 Er (1–12) | 5.6% | 5.1% | 1.12 (0–4) | 4.23 (0–19) | 3.90zł (0.3–12.3) | 6.41 (1.0–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED2` | 6.71 Er (1–12) | 5.3% | 5.1% | 1.63 (0–4) | 4.27 (0–20) | 3.80zł (0.0–12.3) | 6.52 (1.0–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA5` | 6.73 Er (1–12) | 5.5% | 5.1% | 1.62 (0–4) | 4.34 (0–22) | 3.84zł (0.0–11.3) | 6.53 (1.0–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA6` | 6.73 Er (1–12) | 5.5% | 5.1% | 1.62 (0–4) | 4.34 (0–22) | 3.84zł (0.0–11.3) | 6.53 (1.0–10.0) | 🟢 W NORMIE |
| `L4_VERDICT_SECRET` | 6.34 Er (1–12) | 4.0% | 5.2% | 1.52 (0–4) | 3.80 (0–20) | 3.68zł (0.0–12.0) | 6.16 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 2 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_TIME_DECK_EVERY_2ERAS` | 7.00 Er (1–12) | 7.9% | 5.4% | 1.69 (0–4) | 4.62 (0–23) | 3.71zł (0.0–11.3) | 6.58 (1.0–10.0) | 🟢 W NORMIE |
| `L4_NO_TIME_DECK` | 7.15 Er (1–12) | 9.0% | 5.6% | 1.71 (0–4) | 5.19 (0–22) | 3.57zł (0.0–10.7) | 6.66 (1.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.