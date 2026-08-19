# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v1.0-alpha.8

**Wersja Balansu:** `v1.0-alpha.8` | **Data:** 2026-08-19 13:43 | **Przeanalizowano Wariantów:** 15 | **Próba:** 50 gier/setup | **Czas:** 8.56s
**Wynik Bazy Poziomu 2 (Global):** `🔴 39.5 pkt` | 3p: `16.1 pkt` | 4p: `55.6 pkt` | 5p: `46.8 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (5)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🔴 ** 39.5** | 16.1 | 55.6 | 46.8 | ⚪ OPTYMALNY |
| `L2_KT_ERA_MINUS1` | Kabała Era: 6 → 5 | 39.5 → 🔴 ** 52.1** (`⬆️ +12.6`) | 16.1 → 21.1 (`⬆️ +5.0`) | 55.6 → 66.4 (`⬆️ +10.8`) | 46.8 → 68.9 (`⬆️ +22.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki: 8 → 9 | 39.5 → 🔴 ** 37.6** (`-1.9`) | 16.1 → 22.4 (`⬆️ +6.3`) | 55.6 → 56.0 (`⬆️ +0.4`) | 46.8 → 34.5 (`-12.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 2 → 1 | 39.5 → 🔴 ** 37.1** (`-2.4`) | 16.1 → 22.6 (`⬆️ +6.5`) | 55.6 → 33.5 (`-22.1`) | 46.8 → 55.1 (`⬆️ +8.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 6 → 5 | 39.5 → 🔴 ** 24.6** (`-14.9`) | 16.1 → 20.3 (`⬆️ +4.2`) | 55.6 → 46.5 (`-9.1`) | 46.8 → 7.1 (`-39.7`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 10 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2/3/3 → 3/4/4 | 39.5 → 🔴 ** 37.7** (`-1.8`) | 16.1 → 13.9 (`-2.2`) | 55.6 → 52.5 (`-3.1`) | 46.8 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 6 → 7 | 39.5 → 🔴 ** 35.1** (`-4.4`) | 16.1 → 15.0 (`-1.1`) | 55.6 → 46.0 (`-9.6`) | 46.8 → 44.3 (`-2.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki: 8 → 7 | 39.5 → 🔴 ** 26.8** (`-12.7`) | 16.1 → 12.3 (`-3.8`) | 55.6 → 39.1 (`-16.5`) | 46.8 → 28.9 (`-17.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 6 → 7 | 39.5 → 🔴 ** 26.6** (`-12.9`) | 16.1 → 16.0 (`-0.1`) | 55.6 → 33.6 (`-22.0`) | 46.8 → 30.1 (`-16.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 2 → 3 | 39.5 → 🔴 ** 24.1** (`-15.4`) | 16.1 → 9.3 (`-6.8`) | 55.6 → 33.3 (`-22.3`) | 46.8 → 29.7 (`-17.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 39.5 → 🔴 ** 19.0** (`-20.5`) | 16.1 → 13.0 (`-3.1`) | 55.6 → 31.8 (`-23.8`) | 46.8 → 12.3 (`-34.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 39.5 → 🔴 ** 15.5** (`-24.0`) | 16.1 → 9.8 (`-6.3`) | 55.6 → 21.0 (`-34.6`) | 46.8 → 15.6 (`-31.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 39.5 → 🔴 ** 10.1** (`-29.4`) | 16.1 → 13.8 (`-2.3`) | 55.6 → 14.0 (`-41.6`) | 46.8 → 2.6 (`-44.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 39.5 → 🔴 **  9.3** (`-30.2`) | 16.1 → 14.2 (`-1.9`) | 55.6 → 13.1 (`-42.5`) | 46.8 → 0.6 (`-46.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2/3/3 → 1/2/2 | 39.5 → 🔴 **  8.6** (`-30.9`) | 16.1 → 7.1 (`-9.0`) | 55.6 → 18.3 (`-37.3`) | 46.8 → 0.3 (`-46.5`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (5)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 7.27 Er (1–14) | 7.6% | 1.5% | 2.46 (0–5) | 4.63 (0–24) | 20.05zł (3.3–49.7) | 7.29 (0.3–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_KT_ERA_MINUS1` | 7.08 Er (1–14) | 7.6% | 1.5% | 2.27 (0–5) | 4.36 (0–24) | 19.58zł (3.3–49.7) | 7.11 (0.3–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_GC_FALLS_PLUS1` | 7.44 Er (1–14) | 7.9% | 1.4% | 2.51 (0–5) | 4.91 (0–24) | 20.55zł (3.3–49.7) | 7.35 (0.3–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_KT_FRAGS_MINUS1` | 6.66 Er (1–14) | 4.2% | 1.6% | 2.33 (0–5) | 3.74 (0–23) | 18.14zł (3.3–48.3) | 7.06 (0.3–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 7.00 Er (1–14) | 5.1% | 1.5% | 2.41 (0–5) | 4.22 (0–24) | 19.21zł (3.0–49.7) | 7.21 (0.3–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 10 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_SO_CONDEMNS_PLUS1` | 7.46 Er (1–14) | 8.1% | 1.4% | 2.48 (0–5) | 4.99 (0–24) | 20.62zł (3.3–49.7) | 7.30 (0.3–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_SO_STACKS_PLUS1` | 7.40 Er (1–14) | 8.5% | 1.5% | 2.48 (0–5) | 4.84 (0–24) | 20.46zł (3.3–49.7) | 7.33 (0.3–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_GC_FALLS_MINUS1` | 7.06 Er (1–14) | 7.4% | 1.5% | 2.39 (0–5) | 4.32 (0–24) | 19.41zł (3.3–49.7) | 7.21 (0.3–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_KT_ERA_PLUS1` | 7.38 Er (1–14) | 7.6% | 1.5% | 2.47 (0–5) | 4.82 (0–24) | 20.34zł (3.3–49.7) | 7.34 (0.3–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_KT_FRAGS_PLUS1` | 7.53 Er (1–14) | 8.4% | 1.4% | 2.51 (0–5) | 5.09 (0–25) | 20.77zł (3.3–49.7) | 7.37 (0.3–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_PLUS1` | 7.65 Er (3–14) | 8.5% | 1.5% | 2.61 (1–5) | 5.03 (0–24) | 21.16zł (4.0–49.7) | 7.60 (4.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_KB_DECREES_PLUS1` | 7.58 Er (1–14) | 8.8% | 1.5% | 2.56 (0–5) | 5.24 (0–24) | 20.89zł (3.3–49.7) | 7.42 (0.3–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_KB_DECREES_MINUS1` | 5.58 Er (1–14) | 4.0% | 1.6% | 1.89 (0–5) | 2.69 (0–21) | 15.34zł (1.7–49.7) | 6.00 (0.3–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.62 Er (1–14) | 2.2% | 1.6% | 1.54 (0–5) | 2.37 (0–21) | 12.61zł (1.3–49.7) | 5.04 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_SO_CONDEMNS_MINUS1` | 5.94 Er (1–14) | 3.0% | 1.6% | 2.05 (0–5) | 2.84 (0–24) | 16.04zł (3.0–48.0) | 6.77 (0.3–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.