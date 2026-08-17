# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.99.1

**Wersja Balansu:** `v0.99.1` | **Data:** 2026-08-18 01:11 | **Przeanalizowano Wariantów:** 17 | **Próba:** 3000 gier/setup | **Czas:** 251.34s
**Wynik Bazy Poziomu 2 (Global):** `🔴 14.3 pkt` | 3p: `4.3 pkt` | 4p: `16.5 pkt` | 5p: `22.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (8)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🔴 ** 14.3** | 4.3 | 16.5 | 22.0 | ⚪ OPTYMALNY |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 14.3 → 🔴 ** 19.2** (`⬆️ +4.9`) | 4.3 → 11.1 (`⬆️ +6.8`) | 16.5 → 26.9 (`⬆️ +10.4`) | 22.0 → 19.6 (`-2.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 7 → 6 | 14.3 → 🔴 ** 19.1** (`⬆️ +4.8`) | 4.3 → 5.2 (`⬆️ +0.9`) | 16.5 → 24.0 (`⬆️ +7.5`) | 22.0 → 28.0 (`⬆️ +6.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki: 7 → 8 | 14.3 → 🔴 ** 18.5** (`⬆️ +4.2`) | 4.3 → 4.0 (`-0.3`) | 16.5 → 24.2 (`⬆️ +7.7`) | 22.0 → 27.4 (`⬆️ +5.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 4 → 3 | 14.3 → 🔴 ** 14.6** (`⬆️ +0.3`) | 4.3 | 16.5 → 17.5 (`⬆️ +1.0`) | 22.0 | ⚪ OPTYMALNY |
| `L2_CAA_ERA_MINUS1` | Cienie Era ścieżki: 4 → 3 | 14.3 → 🔴 ** 14.4** (`⬆️ +0.1`) | 4.3 | 16.5 → 16.8 (`⬆️ +0.3`) | 22.0 → 22.2 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 14.3 → 🔴 **  9.4** (`-4.9`) | 4.3 → 6.8 (`⬆️ +2.5`) | 16.5 → 12.0 (`-4.5`) | 22.0 → 9.5 (`-12.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 3 → 2 | 14.3 → 🔴 **  9.0** (`-5.3`) | 4.3 → 7.8 (`⬆️ +3.5`) | 16.5 → 15.0 (`-1.5`) | 22.0 → 4.3 (`-17.7`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 9 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_PLUS1` | Cienie Era ścieżki: 4 → 5 | 14.3 → 🔴 ** 13.6** (`-0.7`) | 4.3 → 4.2 (`-0.1`) | 16.5 → 16.1 (`-0.4`) | 22.0 → 20.6 (`-1.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 4 → 5 | 14.3 → 🔴 ** 13.0** (`-1.3`) | 4.3 | 16.5 → 16.1 (`-0.4`) | 22.0 → 18.5 (`-3.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 7 → 8 | 14.3 → 🔴 ** 11.5** (`-2.8`) | 4.3 → 3.8 (`-0.5`) | 16.5 → 12.4 (`-4.1`) | 22.0 → 18.4 (`-3.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki: 7 → 6 | 14.3 → 🔴 ** 10.2** (`-4.1`) | 4.3 → 4.2 (`-0.1`) | 16.5 → 10.6 (`-5.9`) | 22.0 → 15.8 (`-6.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 14.3 → 🔴 **  9.6** (`-4.7`) | 4.3 → 3.5 (`-0.8`) | 16.5 → 11.2 (`-5.3`) | 22.0 → 14.1 (`-7.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 14.3 → 🔴 **  7.8** (`-6.5`) | 4.3 → 2.6 (`-1.7`) | 16.5 → 9.1 (`-7.4`) | 22.0 → 11.7 (`-10.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 3 → 4 | 14.3 → 🔴 **  4.8** (`-9.5`) | 4.3 | 16.5 → 6.0 (`-10.5`) | 22.0 → 4.2 (`-17.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 14.3 → 🔴 **  4.7** (`-9.6`) | 4.3 → 1.5 (`-2.8`) | 16.5 → 5.6 (`-10.9`) | 22.0 → 6.9 (`-15.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 14.3 → 🔴 **  1.7** (`-12.6`) | 4.3 → 1.3 (`-3.0`) | 16.5 → 3.6 (`-12.9`) | 22.0 → 0.1 (`-21.9`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (8)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 7.02 Er (2–12) | 17.1% | 0.8% | 2.17 (0–5) | 6.50 (0–28) | 20.09zł (1.0–44.3) | 6.63 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L2_KT_FRAGS_MINUS1` | 6.30 Er (2–12) | 12.8% | 0.8% | 1.95 (0–5) | 5.31 (0–26) | 17.82zł (1.0–44.3) | 6.22 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 6.79 Er (2–12) | 13.2% | 0.8% | 2.14 (0–5) | 6.03 (0–28) | 19.34zł (1.0–44.3) | 6.57 (1.3–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 7.27 Er (2–12) | 18.5% | 0.7% | 2.22 (0–5) | 7.01 (0–28) | 20.87zł (1.0–44.3) | 6.71 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L2_KT_ERA_MINUS1` | 6.93 Er (2–12) | 17.1% | 0.8% | 2.17 (0–5) | 6.40 (0–28) | 19.82zł (1.0–44.3) | 6.53 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L2_CAA_ERA_MINUS1` | 6.99 Er (2–12) | 17.1% | 0.8% | 2.17 (0–5) | 6.47 (0–28) | 19.99zł (1.0–44.3) | 6.60 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L2_CAA_RELICS_MINUS1` | 5.47 Er (2–12) | 7.3% | 0.9% | 1.71 (0–5) | 3.91 (0–26) | 15.22zł (1.0–44.3) | 5.75 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 6.31 Er (2–12) | 10.3% | 0.8% | 2.03 (0–5) | 5.09 (0–28) | 17.85zł (1.0–44.3) | 6.40 (1.3–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 9 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_PLUS1` | 7.06 Er (2–12) | 17.1% | 0.7% | 2.17 (0–5) | 6.55 (0–28) | 20.20zł (1.0–44.3) | 6.65 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L2_KT_ERA_PLUS1` | 7.12 Er (2–12) | 17.1% | 0.7% | 2.17 (0–5) | 6.61 (0–28) | 20.38zł (1.0–44.3) | 6.68 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L2_SO_STACKS_PLUS1` | 7.16 Er (2–12) | 20.1% | 0.7% | 2.18 (0–5) | 6.80 (0–28) | 20.56zł (1.0–44.3) | 6.66 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L2_GC_FALLS_MINUS1` | 6.74 Er (2–12) | 16.1% | 0.8% | 2.10 (0–5) | 5.96 (0–28) | 19.22zł (1.0–44.3) | 6.52 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L2_CAA_RELICS_PLUS1` | 7.19 Er (2–12) | 17.9% | 0.7% | 2.22 (0–5) | 6.80 (0–28) | 20.63zł (1.0–44.3) | 6.72 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L2_KT_FRAGS_PLUS1` | 7.40 Er (2–12) | 18.9% | 0.7% | 2.28 (0–5) | 7.16 (0–28) | 21.27zł (1.0–44.3) | 6.83 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L2_SO_CONDEMNS_PLUS1` | 7.06 Er (2–12) | 17.3% | 0.7% | 2.17 (0–5) | 6.61 (0–30) | 20.20zł (1.0–44.3) | 6.64 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L2_KB_DECREES_PLUS1` | 7.86 Er (3–12) | 19.8% | 0.7% | 2.43 (0–5) | 7.92 (0–28) | 22.52zł (4.0–44.3) | 7.16 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L2_KB_DECREES_MINUS1` | 3.93 Er (1–12) | 8.1% | 0.7% | 1.03 (0–5) | 2.68 (0–24) | 11.70zł (0.0–44.3) | 4.06 (0.5–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.