# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v1.0-alpha.9

**Wersja Balansu:** `v1.0-alpha.9` | **Data:** 2026-08-19 19:09 | **Przeanalizowano Wariantów:** 15 | **Próba:** 1000 gier/setup | **Czas:** 45.24s
**Wynik Bazy Poziomu 2 (Global):** `🟡 79.7 pkt` | 3p: `0.0 pkt` | 4p: `79.7 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (1)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🟡 ** 79.7** | 0.0 | 79.7 | 0.0 | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 14 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_ERA_MINUS1` | Kabała Era: 6 → 5 | 79.7 → 🟠 ** 70.2** (`-9.5`) | 0.0 | 79.7 → 70.2 (`-9.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki: 8 → 9 | 79.7 → 🟠 ** 69.4** (`-10.3`) | 0.0 | 79.7 → 69.4 (`-10.3`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 6 → 7 | 79.7 → 🟠 ** 67.7** (`-12.0`) | 0.0 | 79.7 → 67.7 (`-12.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki: 8 → 7 | 79.7 → 🔴 ** 59.5** (`-20.2`) | 0.0 | 79.7 → 59.5 (`-20.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 6 → 7 | 79.7 → 🔴 ** 53.2** (`-26.5`) | 0.0 | 79.7 → 53.2 (`-26.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 6 → 5 | 79.7 → 🔴 ** 52.9** (`-26.8`) | 0.0 | 79.7 → 52.9 (`-26.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 2 → 3 | 79.7 → 🔴 ** 37.5** (`-42.2`) | 0.0 | 79.7 → 37.5 (`-42.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 79.7 → 🔴 ** 34.6** (`-45.1`) | 0.0 | 79.7 → 34.6 (`-45.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2/3/3 → 3/4/4 | 79.7 → 🔴 ** 34.3** (`-45.4`) | 0.0 | 79.7 → 34.3 (`-45.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 2 → 1 | 79.7 → 🔴 ** 32.8** (`-46.9`) | 0.0 | 79.7 → 32.8 (`-46.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 79.7 → 🔴 ** 30.1** (`-49.6`) | 0.0 | 79.7 → 30.1 (`-49.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2/3/3 → 1/2/2 | 79.7 → 🔴 ** 23.7** (`-56.0`) | 0.0 | 79.7 → 23.7 (`-56.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 79.7 → 🔴 ** 20.3** (`-59.4`) | 0.0 | 79.7 → 20.3 (`-59.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 79.7 → 🔴 ** 17.7** (`-62.0`) | 0.0 | 79.7 → 17.7 (`-62.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (1)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 6.19 Er (1–14) | 0.3% | 1.5% | 2.23 (0–5) | 4.13 (0–23) | 16.31zł (1.8–43.5) | 6.98 (0.2–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 14 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_ERA_MINUS1` | 5.96 Er (1–14) | 0.3% | 1.5% | 1.99 (0–5) | 3.77 (0–23) | 15.73zł (1.8–43.5) | 6.77 (0.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 6.30 Er (1–14) | 0.3% | 1.5% | 2.27 (0–5) | 4.33 (0–23) | 16.64zł (1.8–44.5) | 7.02 (0.2–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 6.33 Er (1–14) | 0.6% | 1.5% | 2.27 (0–5) | 4.38 (0–25) | 16.71zł (1.8–45.8) | 7.02 (0.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 6.03 Er (1–14) | 0.2% | 1.6% | 2.17 (0–5) | 3.85 (0–23) | 15.82zł (1.8–43.5) | 6.90 (0.2–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 6.31 Er (1–14) | 0.3% | 1.6% | 2.24 (0–5) | 4.34 (0–23) | 16.62zł (1.8–43.5) | 7.04 (0.2–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.96 Er (1–14) | 0.1% | 1.6% | 2.15 (0–5) | 3.72 (0–17) | 15.64zł (1.8–43.5) | 6.87 (0.2–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 6.36 Er (1–14) | 0.3% | 1.5% | 2.27 (0–5) | 4.47 (0–23) | 16.77zł (1.8–43.5) | 7.06 (0.2–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 6.63 Er (3–14) | 0.4% | 1.5% | 2.43 (1–5) | 4.62 (0–23) | 17.49zł (3.2–44.8) | 7.37 (3.2–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 6.22 Er (1–14) | 0.3% | 1.5% | 2.24 (0–5) | 4.21 (0–23) | 16.39zł (1.8–43.5) | 6.99 (0.2–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.89 Er (1–14) | 0.2% | 1.6% | 2.17 (0–5) | 3.60 (0–23) | 15.39zł (1.8–43.5) | 6.86 (0.2–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.50 Er (1–14) | 0.3% | 1.5% | 2.36 (0–5) | 4.74 (0–23) | 17.15zł (1.8–43.5) | 7.12 (0.2–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 5.48 Er (1–14) | 0.1% | 1.6% | 1.95 (0–5) | 2.87 (0–12) | 14.27zł (1.8–43.5) | 6.66 (0.2–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 4.70 Er (1–14) | 0.0% | 1.7% | 1.65 (0–5) | 2.32 (0–18) | 12.40zł (1.5–43.5) | 5.73 (0.2–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_MINUS1` | 3.87 Er (1–14) | 0.1% | 1.6% | 1.33 (0–5) | 1.88 (0–20) | 10.32zł (1.2–43.0) | 4.67 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.