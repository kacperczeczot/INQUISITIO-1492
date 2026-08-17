# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.98

**Wersja Balansu:** `v0.98` | **Data:** 2026-08-17 22:42 | **Przeanalizowano Wariantów:** 17 | **Próba:** 3000 gier/setup | **Czas:** 187.33s
**Wynik Bazy Poziomu 2 (Global):** `🔴 3.7 pkt` | 3p: `3.0 pkt` | 4p: `4.7 pkt` | 5p: `3.5 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (9)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🔴 **  3.7** | 3.0 | 4.7 | 3.5 | ⚪ OPTYMALNY |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 3 → 2 | 3.7 → 🔴 ** 10.7** (`⬆️ +7.0`) | 3.0 → 7.8 (`⬆️ +4.8`) | 4.7 → 12.5 (`⬆️ +7.8`) | 3.5 → 11.8 (`⬆️ +8.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki: 5 → 6 | 3.7 → 🔴 **  7.9** (`⬆️ +4.2`) | 3.0 → 3.5 (`⬆️ +0.5`) | 4.7 → 6.9 (`⬆️ +2.2`) | 3.5 → 13.2 (`⬆️ +9.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 3.7 → 🔴 **  5.6** (`⬆️ +1.9`) | 3.0 → 6.5 (`⬆️ +3.5`) | 4.7 → 7.1 (`⬆️ +2.4`) | 3.5 → 3.2 (`-0.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 5 → 6 | 3.7 → 🔴 **  5.5** (`⬆️ +1.8`) | 3.0 → 2.3 (`-0.7`) | 4.7 → 6.0 (`⬆️ +1.3`) | 3.5 → 8.2 (`⬆️ +4.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 3.7 → 🔴 **  4.6** (`⬆️ +0.9`) | 3.0 → 3.3 (`⬆️ +0.3`) | 4.7 → 6.6 (`⬆️ +1.9`) | 3.5 → 3.8 (`⬆️ +0.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 5 → 4 | 3.7 → 🔴 **  4.0** (`⬆️ +0.3`) | 3.0 → 3.8 (`⬆️ +0.8`) | 4.7 | 3.5 → 3.4 (`-0.1`) | ⚪ OPTYMALNY |
| `L2_CAA_ERA_MINUS1` | Cienie Era ścieżki: 4 → 3 | 3.7 → 🔴 **  3.9** (`⬆️ +0.2`) | 3.0 → 3.1 (`⬆️ +0.1`) | 4.7 → 5.0 (`⬆️ +0.3`) | 3.5 → 3.7 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L2_KT_ERA_MINUS1` | Kabała Era: 6 → 5 | 3.7 → 🔴 **  3.8** (`⬆️ +0.1`) | 3.0 → 3.1 (`⬆️ +0.1`) | 4.7 | 3.5 | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 8 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 3.7 → 🔴 **  3.6** (`-0.1`) | 3.0 | 4.7 → 4.4 (`-0.3`) | 3.5 → 3.4 (`-0.1`) | ⚪ OPTYMALNY |
| `L2_KT_ERA_PLUS1` | Kabała Era: 6 → 7 | 3.7 → 🔴 **  3.6** (`-0.1`) | 3.0 | 4.7 → 4.5 (`-0.2`) | 3.5 → 3.4 (`-0.1`) | ⚪ OPTYMALNY |
| `L2_CAA_ERA_PLUS1` | Cienie Era ścieżki: 4 → 5 | 3.7 → 🔴 **  3.5** (`-0.2`) | 3.0 → 2.9 (`-0.1`) | 4.7 → 4.5 (`-0.2`) | 3.5 → 3.1 (`-0.4`) | ⚪ OPTYMALNY |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 3 → 4 | 3.7 → 🔴 **  3.2** (`-0.5`) | 3.0 | 4.7 → 3.3 (`-1.4`) | 3.5 → 3.4 (`-0.1`) | ⚪ OPTYMALNY |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 3.7 → 🔴 **  2.6** (`-1.1`) | 3.0 → 2.3 (`-0.7`) | 4.7 → 3.0 (`-1.7`) | 3.5 → 2.5 (`-1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki: 5 → 4 | 3.7 → 🔴 **  2.6** (`-1.1`) | 3.0 → 2.3 (`-0.7`) | 4.7 → 3.2 (`-1.5`) | 3.5 → 2.2 (`-1.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 3.7 → 🔴 **  1.5** (`-2.2`) | 3.0 → 1.0 (`-2.0`) | 4.7 → 1.1 (`-3.6`) | 3.5 → 2.4 (`-1.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 3.7 → 🔴 **  0.6** (`-3.1`) | 3.0 → 0.9 (`-2.1`) | 4.7 → 0.8 (`-3.9`) | 3.5 → 0.1 (`-3.4`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (9)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 6.15 Er (2–12) | 8.5% | 0.8% | 2.02 (0–5) | 4.58 (0–28) | 17.77zł (1.3–44.3) | 6.21 (1.4–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 5.95 Er (2–12) | 7.4% | 0.8% | 1.95 (0–5) | 4.21 (0–28) | 17.15zł (1.3–44.3) | 6.12 (1.4–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 6.46 Er (2–12) | 8.9% | 0.8% | 2.11 (0–5) | 5.09 (0–28) | 18.71zł (1.3–44.3) | 6.37 (1.4–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 5.00 Er (2–12) | 2.8% | 0.9% | 1.64 (0–5) | 2.82 (0–26) | 14.16zł (1.3–44.3) | 5.46 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 6.45 Er (2–12) | 11.7% | 0.8% | 2.08 (0–5) | 5.17 (0–28) | 18.73zł (1.3–44.3) | 6.34 (1.4–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 6.08 Er (2–12) | 7.9% | 0.8% | 2.00 (0–5) | 4.43 (0–28) | 17.53zł (1.3–44.3) | 6.17 (1.4–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.72 Er (2–12) | 6.1% | 0.9% | 1.90 (0–5) | 3.83 (0–28) | 16.40zł (1.3–44.3) | 5.97 (1.4–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_MINUS1` | 6.12 Er (2–12) | 8.5% | 0.8% | 2.02 (0–5) | 4.55 (0–28) | 17.67zł (1.3–44.3) | 6.18 (1.4–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 6.15 Er (2–12) | 8.5% | 0.8% | 2.01 (0–5) | 4.57 (0–28) | 17.75zł (1.3–44.3) | 6.20 (1.4–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 8 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_FRAGS_PLUS1` | 6.17 Er (2–12) | 8.6% | 0.8% | 2.02 (0–5) | 4.61 (0–28) | 17.81zł (1.3–44.3) | 6.22 (1.4–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 6.16 Er (2–12) | 8.5% | 0.8% | 2.02 (0–5) | 4.59 (0–28) | 17.78zł (1.3–44.3) | 6.21 (1.4–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_PLUS1` | 6.19 Er (2–12) | 8.5% | 0.8% | 2.02 (0–5) | 4.62 (0–28) | 17.87zł (1.3–44.3) | 6.23 (1.4–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 6.16 Er (2–12) | 8.5% | 0.8% | 2.02 (0–5) | 4.60 (0–28) | 17.78zł (1.3–44.3) | 6.21 (1.4–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 6.27 Er (2–12) | 9.0% | 0.8% | 2.06 (0–5) | 4.78 (0–28) | 18.14zł (1.3–44.3) | 6.29 (1.4–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 5.80 Er (2–12) | 8.0% | 0.8% | 1.92 (0–5) | 4.05 (0–28) | 16.69zł (1.3–44.3) | 5.98 (1.4–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.82 Er (3–12) | 10.4% | 0.8% | 2.25 (1–5) | 5.64 (0–28) | 19.67zł (3.3–44.3) | 6.69 (1.7–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 3.54 Er (1–12) | 3.7% | 0.7% | 0.97 (0–5) | 1.79 (0–26) | 10.83zł (0.0–44.3) | 3.82 (0.4–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.