# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v1.0-alpha.23

**Wersja Balansu:** `v1.0-alpha.23` | **Data:** 2026-08-22 14:37 | **Przeanalizowano Wariantów:** 15 | **Próba:** 3000 gier/setup | **Czas:** 70.63s
**Wynik Bazy Poziomu 2 (Global):** `🟡 82.9 pkt` | 3p: `0.0 pkt` | 4p: `82.9 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (1)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🟡 ** 82.9** | 0.0 | 82.9 | 0.0 | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 14 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 6 → 7 | 82.9 → 🟠 ** 71.0** (`-11.9`) | 0.0 | 82.9 → 71.0 (`-11.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki: 8 → 9 | 82.9 → 🟠 ** 70.3** (`-12.6`) | 0.0 | 82.9 → 70.3 (`-12.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki: 8 → 7 | 82.9 → 🟠 ** 67.6** (`-15.3`) | 0.0 | 82.9 → 67.6 (`-15.3`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 6 → 5 | 82.9 → 🟠 ** 66.8** (`-16.1`) | 0.0 | 82.9 → 66.8 (`-16.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 6 → 5 | 82.9 → 🟠 ** 64.8** (`-18.1`) | 0.0 | 82.9 → 64.8 (`-18.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 6 → 7 | 82.9 → 🔴 ** 52.6** (`-30.3`) | 0.0 | 82.9 → 52.6 (`-30.3`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 2 → 3 | 82.9 → 🔴 ** 49.6** (`-33.3`) | 0.0 | 82.9 → 49.6 (`-33.3`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 2 → 1 | 82.9 → 🔴 ** 44.8** (`-38.1`) | 0.0 | 82.9 → 44.8 (`-38.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2/3/3 → 3/4/4 | 82.9 → 🔴 ** 36.8** (`-46.1`) | 0.0 | 82.9 → 36.8 (`-46.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 82.9 → 🔴 ** 34.9** (`-48.0`) | 0.0 | 82.9 → 34.9 (`-48.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 82.9 → 🔴 ** 29.3** (`-53.6`) | 0.0 | 82.9 → 29.3 (`-53.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2/3/3 → 1/2/2 | 82.9 → 🔴 ** 25.7** (`-57.2`) | 0.0 | 82.9 → 25.7 (`-57.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 82.9 → 🔴 ** 19.3** (`-63.6`) | 0.0 | 82.9 → 19.3 (`-63.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 82.9 → 🔴 ** 16.8** (`-66.1`) | 0.0 | 82.9 → 16.8 (`-66.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (1)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 5.91 Er (1–14) | 0.2% | 1.2% | 1.67 (0–4) | 4.25 (0–20) | 15.38zł (1.5–46.8) | 6.99 (0.2–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 14 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_SO_STACKS_PLUS1` | 6.03 Er (1–14) | 0.3% | 1.2% | 1.72 (0–4) | 4.47 (0–26) | 15.74zł (1.5–47.8) | 7.04 (0.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 6.01 Er (1–14) | 0.2% | 1.2% | 1.71 (0–4) | 4.44 (0–20) | 15.69zł (1.5–46.8) | 7.03 (0.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 5.75 Er (1–14) | 0.2% | 1.2% | 1.61 (0–4) | 3.98 (0–20) | 14.95zł (1.5–46.8) | 6.91 (0.2–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.66 Er (1–14) | 0.2% | 1.2% | 1.45 (0–4) | 3.84 (0–20) | 14.75zł (1.5–46.8) | 6.80 (0.2–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.67 Er (1–14) | 0.1% | 1.2% | 1.59 (0–4) | 3.86 (0–20) | 14.72zł (1.5–46.0) | 6.87 (0.2–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 6.01 Er (1–14) | 0.2% | 1.2% | 1.68 (0–4) | 4.46 (0–20) | 15.67zł (1.5–46.8) | 7.04 (0.2–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 6.03 Er (1–14) | 0.2% | 1.2% | 1.69 (0–4) | 4.50 (0–28) | 15.72zł (1.5–46.8) | 7.03 (0.2–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.73 Er (1–14) | 0.1% | 1.2% | 1.64 (0–4) | 3.95 (0–20) | 14.86zł (1.5–46.0) | 6.92 (0.2–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 5.94 Er (1–14) | 0.2% | 1.2% | 1.68 (0–4) | 4.33 (0–22) | 15.47zł (1.5–46.8) | 7.00 (0.2–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 6.37 Er (2–14) | 0.2% | 1.2% | 1.86 (0–4) | 4.82 (0–20) | 16.61zł (3.2–46.8) | 7.40 (2.5–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.17 Er (1–14) | 0.2% | 1.1% | 1.78 (0–4) | 4.79 (0–22) | 16.15zł (1.5–46.8) | 7.12 (0.2–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 5.20 Er (1–14) | 0.1% | 1.3% | 1.41 (0–4) | 3.02 (0–16) | 13.42zł (1.5–46.8) | 6.62 (0.2–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 4.52 Er (1–14) | 0.1% | 1.2% | 1.20 (0–4) | 2.62 (0–20) | 12.06zł (1.5–46.0) | 5.67 (0.2–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_MINUS1` | 3.68 Er (1–14) | 0.1% | 1.3% | 0.95 (0–4) | 1.91 (0–17) | 9.86zł (1.2–46.0) | 4.70 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.