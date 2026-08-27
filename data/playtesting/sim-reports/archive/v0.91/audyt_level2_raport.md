# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.91

**Wersja Balansu:** `v0.91` | **Data:** 2026-08-17 14:42 | **Przeanalizowano Wariantów:** 22 | **Próba:** 5000 gier/setup | **Czas:** 275.37s
**Wynik Bazy Poziomu 2 (Global):** `🔴 26.9 pkt` | 3p: `24.9 pkt` | 4p: `37.1 pkt` | 5p: `18.8 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (12)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🔴 ** 26.9** | 24.9 | 37.1 | 18.8 | ⚪ OPTYMALNY |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 3 → 2 | 26.9 → 🔴 ** 56.8** (`⬆️ +29.9`) | 24.9 → 49.3 (`⬆️ +24.4`) | 37.1 → 71.7 (`⬆️ +34.6`) | 18.8 → 49.4 (`⬆️ +30.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 5 → 4 | 26.9 → 🔴 ** 27.5** (`⬆️ +0.6`) | 24.9 → 29.6 (`⬆️ +4.7`) | 37.1 → 34.2 (`-2.9`) | 18.8 | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 6 → 5 | 26.9 → 🔴 ** 27.4** (`⬆️ +0.5`) | 24.9 → 23.8 (`-1.1`) | 37.1 → 35.2 (`-1.9`) | 18.8 → 23.3 (`⬆️ +4.5`) | ⚪ OPTYMALNY |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 0 → 1 | 26.9 → 🔴 ** 27.2** (`⬆️ +0.3`) | 24.9 → 25.0 (`⬆️ +0.1`) | 37.1 → 37.5 (`⬆️ +0.4`) | 18.8 → 19.1 (`⬆️ +0.3`) | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 0–9 → 0–8 | 26.9 → 🔴 ** 26.7** (`-0.2`) | 24.9 → 25.0 (`⬆️ +0.1`) | 37.1 → 36.9 (`-0.2`) | 18.8 → 18.3 (`-0.5`) | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 0–9 → 0–10 | 26.9 → 🔴 ** 25.8** (`-1.1`) | 24.9 → 22.6 (`-2.3`) | 37.1 → 34.9 (`-2.2`) | 18.8 → 19.9 (`⬆️ +1.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 6 → 7 | 26.9 → 🔴 ** 25.1** (`-1.8`) | 24.9 → 26.5 (`⬆️ +1.6`) | 37.1 → 35.1 (`-2.0`) | 18.8 → 13.7 (`-5.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 5 → 6 | 26.9 → 🔴 ** 23.9** (`-3.0`) | 24.9 → 21.1 (`-3.8`) | 37.1 → 30.7 (`-6.4`) | 18.8 → 20.0 (`⬆️ +1.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 26.9 → 🔴 ** 21.1** (`-5.8`) | 24.9 → 18.6 (`-6.3`) | 37.1 → 21.6 (`-15.5`) | 18.8 → 23.0 (`⬆️ +4.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 5 → 4 | 26.9 → 🔴 ** 20.6** (`-6.3`) | 24.9 → 27.6 (`⬆️ +2.7`) | 37.1 → 26.5 (`-10.6`) | 18.8 → 7.6 (`-11.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 3/5 → 2/4 | 26.9 → 🔴 ** 19.4** (`-7.5`) | 24.9 → 27.0 (`⬆️ +2.1`) | 37.1 → 22.8 (`-14.3`) | 18.8 → 8.5 (`-10.3`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 10 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 0–9 → 1–9 | 🔴 ** 26.9** | 24.9 | 37.1 | 18.8 | ⚪ OPTYMALNY |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 5 → 6 | 26.9 → 🔴 ** 23.7** (`-3.2`) | 24.9 → 19.4 (`-5.5`) | 37.1 → 32.9 (`-4.2`) | 18.8 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 3 → 4 | 26.9 → 🔴 ** 21.0** (`-5.9`) | 24.9 → 23.5 (`-1.4`) | 37.1 → 28.8 (`-8.3`) | 18.8 → 10.7 (`-8.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 3 → 2 | 26.9 → 🔴 ** 18.9** (`-8.0`) | 24.9 → 22.3 (`-2.6`) | 37.1 → 25.8 (`-11.3`) | 18.8 → 8.5 (`-10.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 26.9 → 🔴 ** 17.9** (`-9.0`) | 24.9 → 20.8 (`-4.1`) | 37.1 → 23.4 (`-13.7`) | 18.8 → 9.6 (`-9.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 3/5 → 4/6 | 26.9 → 🔴 ** 17.8** (`-9.1`) | 24.9 → 18.1 (`-6.8`) | 37.1 → 24.6 (`-12.5`) | 18.8 → 10.7 (`-8.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 26.9 → 🔴 ** 10.9** (`-16.0`) | 24.9 → 12.2 (`-12.7`) | 37.1 → 13.9 (`-23.2`) | 18.8 → 6.7 (`-12.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 26.9 → 🔴 **  9.6** (`-17.3`) | 24.9 → 9.9 (`-15.0`) | 37.1 → 13.0 (`-24.1`) | 18.8 → 5.9 (`-12.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 26.9 → 🔴 **  7.9** (`-19.0`) | 24.9 → 12.9 (`-12.0`) | 37.1 → 8.5 (`-28.6`) | 18.8 → 2.4 (`-16.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 26.9 → 🔴 **  4.7** (`-22.2`) | 24.9 → 8.5 (`-16.4`) | 37.1 → 5.6 (`-31.5`) | 18.8 → 0.1 (`-18.7`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (12)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 6.72 Er (1–12) | 5.7% | 5.0% | 1.62 (0–4) | 4.28 (0–25) | 3.84zł (0.0–14.7) | 6.51 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 6.60 Er (1–12) | 5.0% | 5.0% | 1.59 (0–4) | 4.18 (0–25) | 3.79zł (0.0–14.7) | 6.47 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 6.60 Er (1–12) | 5.0% | 5.0% | 1.60 (0–4) | 4.12 (0–25) | 3.79zł (0.0–14.7) | 6.46 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 6.63 Er (1–12) | 5.7% | 4.9% | 1.57 (0–4) | 4.19 (0–25) | 3.81zł (0.0–14.7) | 6.45 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 6.76 Er (1–12) | 5.7% | 5.0% | 1.63 (0–4) | 4.31 (0–25) | 3.84zł (0.0–14.7) | 6.54 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 6.76 Er (1–12) | 6.0% | 4.9% | 1.63 (0–4) | 4.33 (0–25) | 3.86zł (0.0–14.7) | 6.51 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 6.63 Er (1–12) | 3.9% | 5.0% | 1.60 (0–4) | 4.16 (0–23) | 3.79zł (0.0–14.7) | 6.51 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 6.83 Er (1–12) | 5.8% | 5.0% | 1.64 (0–4) | 4.40 (0–25) | 3.89zł (0.0–14.7) | 6.56 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 6.85 Er (1–12) | 7.2% | 4.9% | 1.65 (0–4) | 4.40 (0–25) | 3.90zł (0.0–14.7) | 6.54 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 6.40 Er (1–12) | 5.1% | 5.0% | 1.56 (0–4) | 3.90 (0–25) | 3.72zł (0.0–14.7) | 6.41 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 6.49 Er (1–12) | 4.2% | 5.0% | 1.56 (0–4) | 4.08 (0–25) | 3.75zł (0.0–14.7) | 6.44 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 6.19 Er (1–12) | 4.0% | 5.0% | 1.50 (0–4) | 3.77 (0–25) | 3.64zł (0.0–14.7) | 6.26 (0.7–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 10 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_HERESY_LOW_PLUS1` | 6.72 Er (1–12) | 5.7% | 5.0% | 1.62 (0–4) | 4.28 (0–25) | 3.84zł (0.0–14.7) | 6.51 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 6.81 Er (1–12) | 6.5% | 4.9% | 1.63 (0–4) | 4.39 (0–25) | 3.88zł (0.0–14.7) | 6.54 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 6.95 Er (1–12) | 6.5% | 4.9% | 1.67 (0–4) | 4.47 (0–25) | 3.93zł (0.0–14.7) | 6.60 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 6.32 Er (1–12) | 4.8% | 5.0% | 1.52 (0–4) | 3.93 (0–25) | 3.69zł (0.0–14.7) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 7.02 Er (1–12) | 7.0% | 4.9% | 1.68 (0–4) | 4.63 (0–25) | 3.97zł (0.0–14.7) | 6.62 (0.7–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_GC_FALLS_PLUS1` | 7.04 Er (1–12) | 7.3% | 4.9% | 1.68 (0–4) | 4.58 (0–25) | 3.97zł (0.0–14.7) | 6.63 (0.7–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_PLUS1` | 7.24 Er (2–12) | 7.6% | 5.0% | 1.76 (0–4) | 4.81 (0–25) | 4.03zł (0.0–14.7) | 6.82 (2.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_KB_DECREES_PLUS1` | 7.25 Er (1–12) | 9.3% | 5.0% | 1.75 (0–4) | 4.94 (0–25) | 4.05zł (0.0–14.7) | 6.70 (0.7–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_MINUS1` | 5.56 Er (1–12) | 2.0% | 5.0% | 1.30 (0–4) | 3.13 (0–23) | 3.47zł (0.0–12.0) | 5.74 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 3.90 Er (1–12) | 2.2% | 4.3% | 0.82 (0–4) | 1.83 (0–22) | 3.21zł (0.0–14.7) | 4.41 (0.5–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.