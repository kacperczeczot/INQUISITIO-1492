# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.97

**Wersja Balansu:** `v0.97` | **Data:** 2026-08-17 22:35 | **Przeanalizowano Wariantów:** 17 | **Próba:** 5000 gier/setup | **Czas:** 347.02s
**Wynik Bazy Poziomu 2 (Global):** `🔴 0.9 pkt` | 3p: `0.7 pkt` | 4p: `0.6 pkt` | 5p: `1.4 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (6)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🔴 **  0.9** | 0.7 | 0.6 | 1.4 | ⚪ OPTYMALNY |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 3 → 2 | 0.9 → 🔴 **  2.5** (`⬆️ +1.6`) | 0.7 → 2.3 (`⬆️ +1.6`) | 0.6 → 2.8 (`⬆️ +2.2`) | 1.4 → 2.4 (`⬆️ +1.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 3 → 2 | 0.9 → 🔴 **  2.2** (`⬆️ +1.3`) | 0.7 → 2.6 (`⬆️ +1.9`) | 0.6 → 2.4 (`⬆️ +1.8`) | 1.4 → 1.7 (`⬆️ +0.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki: 5 → 6 | 0.9 → 🔴 **  1.4** (`⬆️ +0.5`) | 0.7 → 0.9 (`⬆️ +0.2`) | 0.6 → 1.5 (`⬆️ +0.9`) | 1.4 → 1.7 (`⬆️ +0.3`) | ⚪ OPTYMALNY |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 3 → 2 | 0.9 → 🔴 **  1.4** (`⬆️ +0.5`) | 0.7 → 1.0 (`⬆️ +0.3`) | 0.6 → 1.0 (`⬆️ +0.4`) | 1.4 → 2.1 (`⬆️ +0.7`) | ⚪ OPTYMALNY |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 5 → 4 | 0.9 → 🔴 **  0.8** (`-0.1`) | 0.7 → 1.2 (`⬆️ +0.5`) | 0.6 → 0.8 (`⬆️ +0.2`) | 1.4 → 0.5 (`-0.9`) | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 11 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 3 → 4 | 🔴 **  0.9** | 0.7 | 0.6 | 1.4 | ⚪ OPTYMALNY |
| `L2_CAA_ERA_PLUS1` | Cienie Era ścieżki: 5 → 6 | 🔴 **  0.9** | 0.7 | 0.6 | 1.4 | ⚪ OPTYMALNY |
| `L2_CAA_ERA_MINUS1` | Cienie Era ścieżki: 5 → 4 | 🔴 **  0.9** | 0.7 | 0.6 | 1.4 | ⚪ OPTYMALNY |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 3 → 4 | 🔴 **  0.9** | 0.7 | 0.6 | 1.4 | ⚪ OPTYMALNY |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 4 → 5 | 🔴 **  0.9** | 0.7 | 0.6 | 1.4 | ⚪ OPTYMALNY |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 4 → 3 | 🔴 **  0.9** | 0.7 | 0.6 | 1.4 | ⚪ OPTYMALNY |
| `L2_KT_ERA_PLUS1` | Kabała Era: 7 → 8 | 🔴 **  0.9** | 0.7 | 0.6 | 1.4 | ⚪ OPTYMALNY |
| `L2_KT_ERA_MINUS1` | Kabała Era: 7 → 6 | 🔴 **  0.9** | 0.7 | 0.6 | 1.4 | ⚪ OPTYMALNY |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 5 → 6 | 0.9 → 🔴 **  0.6** (`-0.3`) | 0.7 → 0.5 (`-0.2`) | 0.6 → 0.5 (`-0.1`) | 1.4 → 0.7 (`-0.7`) | ⚪ OPTYMALNY |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 3 → 4 | 0.9 → 🔴 **  0.5** (`-0.4`) | 0.7 | 0.6 → 0.3 (`-0.3`) | 1.4 → 0.4 (`-1.0`) | ⚪ OPTYMALNY |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki: 5 → 4 | 0.9 → 🔴 **  0.3** (`-0.6`) | 0.7 → 0.5 (`-0.2`) | 0.6 → 0.3 (`-0.3`) | 1.4 → 0.2 (`-1.2`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (6)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 6.98 Er (3–12) | 11.2% | 0.8% | 2.30 (1–5) | 5.92 (0–28) | 20.15zł (3.0–44.3) | 6.80 (2.3–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 6.29 Er (2–12) | 9.1% | 0.8% | 2.07 (0–5) | 4.80 (0–28) | 18.18zł (1.3–44.3) | 6.30 (1.4–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 6.71 Er (2–12) | 10.1% | 0.8% | 2.21 (0–5) | 5.41 (0–28) | 19.32zł (3.0–44.3) | 6.67 (2.3–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 7.36 Er (3–12) | 11.7% | 0.7% | 2.42 (1–5) | 6.56 (0–28) | 21.33zł (3.0–44.3) | 7.00 (2.3–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_MINUS1` | 6.87 Er (3–12) | 10.6% | 0.8% | 2.25 (1–5) | 5.71 (0–28) | 19.81zł (3.0–44.3) | 6.72 (1.7–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 6.43 Er (3–12) | 8.6% | 0.8% | 2.16 (1–5) | 4.98 (0–28) | 18.46zł (3.0–44.3) | 6.50 (2.3–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 11 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_RELICS_PLUS1` | 6.98 Er (3–12) | 11.2% | 0.8% | 2.31 (1–5) | 5.93 (0–28) | 20.17zł (3.0–44.3) | 6.80 (2.3–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_PLUS1` | 6.98 Er (3–12) | 11.2% | 0.8% | 2.31 (1–5) | 5.92 (0–28) | 20.16zł (3.0–44.3) | 6.80 (2.3–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_MINUS1` | 6.97 Er (3–12) | 11.2% | 0.8% | 2.30 (1–5) | 5.91 (0–28) | 20.15zł (3.0–44.3) | 6.79 (2.3–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.98 Er (3–12) | 11.2% | 0.8% | 2.30 (1–5) | 5.92 (0–28) | 20.15zł (3.0–44.3) | 6.80 (2.3–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 6.98 Er (3–12) | 11.3% | 0.8% | 2.30 (1–5) | 5.92 (0–28) | 20.16zł (3.0–44.3) | 6.80 (2.3–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 6.97 Er (3–12) | 11.1% | 0.8% | 2.30 (1–5) | 5.89 (0–28) | 20.12zł (3.0–44.3) | 6.79 (2.3–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 6.98 Er (3–12) | 11.2% | 0.8% | 2.30 (1–5) | 5.92 (0–28) | 20.15zł (3.0–44.3) | 6.80 (2.3–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 6.98 Er (3–12) | 11.2% | 0.8% | 2.30 (1–5) | 5.91 (0–28) | 20.15zł (3.0–44.3) | 6.80 (2.3–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 7.36 Er (3–12) | 15.0% | 0.8% | 2.39 (1–5) | 6.68 (0–28) | 21.38zł (3.0–44.3) | 6.95 (2.3–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_SO_CONDEMNS_PLUS1` | 6.98 Er (3–12) | 11.2% | 0.8% | 2.31 (1–5) | 5.94 (0–28) | 20.17zł (3.0–44.3) | 6.80 (2.3–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 6.54 Er (3–12) | 10.7% | 0.8% | 2.18 (1–5) | 5.24 (0–28) | 18.81zł (2.7–44.3) | 6.51 (2.0–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.