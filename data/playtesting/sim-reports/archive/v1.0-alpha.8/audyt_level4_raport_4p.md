[Strona główna](../../../../../README.md) > [v1.0-alpha.8](README.md) > [audyt_level4_raport_4p](audyt_level4_raport_4p.md)

---

# Raport Audytu Poziomu 4 (Warianty Niszowe i Edykty) — Wersja Balansu: v1.0-alpha.8

**Wersja Balansu:** `v1.0-alpha.8` | **Data:** 2026-08-19 12:22 | **Przeanalizowano Wariantów:** 7 | **Próba:** 3000 gier/setup | **Czas:** 63.82s
**Wynik Bazy Poziomu 4 (Global):** `🟡 77.8 pkt` | 3p: `0.0 pkt` | 4p: `77.8 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (2)

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | Baza (Bieżące warianty niszowe i zasady edyktów) | 🟡 ** 77.8** | 0.0 | 77.8 | 0.0 | ⚪ OPTYMALNY |
| `L4_SEA_ROUTE_ERA_MINUS1` | Szlak Morski: Era 4 → 3 | 77.8 → 🟡 ** 78.0** (`⬆️ +0.2`) | 0.0 | 77.8 → 78.0 (`⬆️ +0.2`) | 0.0 | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 5 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Wariant Niszowy Poziomu 4 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L4_SEA_ROUTE_ERA_PLUS1` | Szlak Morski: Era 4 → 5 | 77.8 → 🟡 ** 76.3** (`-1.5`) | 0.0 | 77.8 → 76.3 (`-1.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L4_VERDICT_SECRET` | Werdykt: jawny → tajny (brak koordynacji anty-snowball) | 77.8 → 🟠 ** 74.7** (`-3.1`) | 0.0 | 77.8 → 74.7 (`-3.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L4_TIME_DECK_EVERY_2ERAS` | Edykty Czasu: co 1 Erę → co 2 Ery | 77.8 → 🟠 ** 68.9** (`-8.9`) | 0.0 | 77.8 → 68.9 (`-8.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L4_NO_TIME_DECK` | Kronika Dziejów: Całkowite wyłączenie edyktów | 77.8 → 🟠 ** 61.4** (`-16.4`) | 0.0 | 77.8 → 61.4 (`-16.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L4_INQUISITOR_SPEED0` | Inkwizytor Patrol: ruch 1 → 0 | 77.8 → 🔴 **  0.8** (`-77.0`) | 0.0 | 77.8 → 0.8 (`-77.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (2)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_BAZA` | 6.20 Er (1–14) | 0.3% | 1.6% | 2.21 (0–5) | 4.14 (0–26) | 16.40zł (1.2–46.8) | 6.97 (0.2–10.0) | 🟢 W NORMIE |
| `L4_SEA_ROUTE_ERA_MINUS1` | 6.19 Er (1–14) | 0.3% | 1.6% | 2.21 (0–5) | 4.13 (0–26) | 16.36zł (1.2–46.8) | 6.95 (0.2–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 5 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L4_SEA_ROUTE_ERA_PLUS1` | 6.23 Er (1–14) | 0.3% | 1.6% | 2.22 (0–5) | 4.17 (0–26) | 16.46zł (1.2–46.8) | 6.98 (0.2–10.0) | 🟢 W NORMIE |
| `L4_VERDICT_SECRET` | 6.13 Er (1–14) | 0.2% | 1.6% | 2.18 (0–5) | 3.96 (0–20) | 16.17zł (1.2–47.0) | 6.96 (0.2–10.0) | 🟢 W NORMIE |
| `L4_TIME_DECK_EVERY_2ERAS` | 6.28 Er (1–14) | 0.2% | 1.9% | 2.25 (0–5) | 4.24 (0–26) | 16.16zł (1.2–46.5) | 7.05 (0.2–10.0) | 🟢 W NORMIE |
| `L4_NO_TIME_DECK` | 6.29 Er (1–14) | 0.2% | 1.9% | 2.27 (0–5) | 4.37 (0–25) | 15.63zł (1.2–46.8) | 7.02 (0.2–10.0) | 🟢 W NORMIE |
| `L4_INQUISITOR_SPEED0` | 9.71 Er (1–14) | 44.5% | 0.8% | 0.45 (0–2) | 2.73 (0–20) | 28.87zł (1.2–55.8) | 4.15 (0.2–8.5) | 🔴 PRZEKROCZONE NORMY |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.