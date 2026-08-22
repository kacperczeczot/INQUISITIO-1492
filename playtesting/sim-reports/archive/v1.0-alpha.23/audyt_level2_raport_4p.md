# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v1.0-alpha.23

**Wersja Balansu:** `v1.0-alpha.23` | **Data:** 2026-08-22 15:08 | **Przeanalizowano Wariantów:** 15 | **Próba:** 3000 gier/setup | **Czas:** 79.36s
**Wynik Bazy Poziomu 2 (Global):** `🟡 81.1 pkt` | 3p: `0.0 pkt` | 4p: `81.1 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (1)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🟡 ** 81.1** | 0.0 | 81.1 | 0.0 | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 14 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 6 → 7 | 81.1 → 🟠 ** 67.9** (`-13.2`) | 0.0 | 81.1 → 67.9 (`-13.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki: 8 → 9 | 81.1 → 🟠 ** 67.4** (`-13.7`) | 0.0 | 81.1 → 67.4 (`-13.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 6 → 5 | 81.1 → 🟠 ** 67.3** (`-13.8`) | 0.0 | 81.1 → 67.3 (`-13.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 6 → 7 | 81.1 → 🟠 ** 66.9** (`-14.2`) | 0.0 | 81.1 → 66.9 (`-14.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki: 8 → 7 | 81.1 → 🟠 ** 63.4** (`-17.7`) | 0.0 | 81.1 → 63.4 (`-17.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 2 → 3 | 81.1 → 🔴 ** 56.1** (`-25.0`) | 0.0 | 81.1 → 56.1 (`-25.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 6 → 5 | 81.1 → 🔴 ** 54.2** (`-26.9`) | 0.0 | 81.1 → 54.2 (`-26.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 2 → 1 | 81.1 → 🔴 ** 36.9** (`-44.2`) | 0.0 | 81.1 → 36.9 (`-44.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 81.1 → 🔴 ** 34.1** (`-47.0`) | 0.0 | 81.1 → 34.1 (`-47.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2/3/3 → 3/4/4 | 81.1 → 🔴 ** 33.8** (`-47.3`) | 0.0 | 81.1 → 33.8 (`-47.3`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 81.1 → 🔴 ** 30.9** (`-50.2`) | 0.0 | 81.1 → 30.9 (`-50.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 81.1 → 🔴 ** 26.3** (`-54.8`) | 0.0 | 81.1 → 26.3 (`-54.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2/3/3 → 1/2/2 | 81.1 → 🔴 ** 25.1** (`-56.0`) | 0.0 | 81.1 → 25.1 (`-56.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 81.1 → 🔴 ** 16.4** (`-64.7`) | 0.0 | 81.1 → 16.4 (`-64.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (1)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 6.03 Er (1–14) | 0.1% | 1.5% | 1.72 (0–4) | 3.95 (0–26) | 15.14zł (1.5–45.2) | 6.76 (0.2–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 14 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_SO_STACKS_PLUS1` | 6.15 Er (1–14) | 0.3% | 1.4% | 1.76 (0–4) | 4.18 (0–26) | 15.47zł (1.5–47.0) | 6.81 (0.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 6.13 Er (1–14) | 0.2% | 1.4% | 1.75 (0–4) | 4.14 (0–26) | 15.43zł (1.5–45.2) | 6.80 (0.2–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.77 Er (1–14) | 0.1% | 1.5% | 1.49 (0–4) | 3.62 (0–26) | 14.46zł (1.5–45.2) | 6.50 (0.2–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 6.17 Er (1–14) | 0.1% | 1.4% | 1.74 (0–4) | 4.20 (0–26) | 15.52zł (1.5–45.2) | 6.83 (0.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 5.87 Er (1–14) | 0.1% | 1.5% | 1.66 (0–4) | 3.69 (0–26) | 14.75zł (1.5–45.2) | 6.67 (0.2–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 6.19 Er (1–14) | 0.2% | 1.4% | 1.75 (0–4) | 4.25 (0–26) | 15.59zł (1.5–45.2) | 6.83 (0.2–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.79 Er (1–14) | 0.1% | 1.5% | 1.64 (0–4) | 3.55 (0–26) | 14.55zł (1.5–44.8) | 6.63 (0.2–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.80 Er (1–14) | 0.1% | 1.5% | 1.68 (0–4) | 3.56 (0–26) | 14.52zł (1.5–45.2) | 6.66 (0.2–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 6.50 Er (3–14) | 0.2% | 1.4% | 1.90 (0–4) | 4.52 (0–26) | 16.32zł (4.0–45.2) | 7.17 (2.2–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 6.06 Er (1–14) | 0.1% | 1.5% | 1.73 (0–4) | 4.04 (0–26) | 15.22zł (1.5–45.8) | 6.76 (0.2–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.25 Er (1–14) | 0.2% | 1.5% | 1.82 (0–4) | 4.40 (0–26) | 15.71zł (1.5–45.2) | 6.87 (0.2–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 4.88 Er (1–14) | 0.1% | 1.4% | 1.31 (0–4) | 2.68 (0–26) | 12.61zł (1.2–45.2) | 5.66 (0.2–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_SO_CONDEMNS_MINUS1` | 5.41 Er (1–14) | 0.1% | 1.5% | 1.50 (0–4) | 2.86 (0–16) | 13.53zł (1.5–45.2) | 6.42 (0.2–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 3.73 Er (1–14) | 0.1% | 1.4% | 0.96 (0–4) | 1.66 (0–22) | 9.93zł (1.5–45.2) | 4.39 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.