# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.89

**Wersja Balansu:** `v0.89` | **Data:** 2026-08-17 13:21 | **Przeanalizowano Wariantów:** 29 | **Próba:** 250 gier/setup | **Czas:** 17.64s
**Wynik Bazy Poziomu 2 (Global):** `🔴 27.1 pkt` | 3p: `24.8 pkt` | 4p: `34.8 pkt` | 5p: `21.7 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (12)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🔴 ** 27.1** | 24.8 | 34.8 | 21.7 | ⚪ OPTYMALNY |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 3 → 2 | 27.1 → 🔴 ** 53.4** (`⬆️ +26.3`) | 24.8 → 46.0 (`⬆️ +21.2`) | 34.8 → 62.6 (`⬆️ +27.8`) | 21.7 → 51.6 (`⬆️ +29.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 6 → 5 | 27.1 → 🔴 ** 32.2** (`⬆️ +5.1`) | 24.8 → 23.7 (`-1.1`) | 34.8 → 46.3 (`⬆️ +11.5`) | 21.7 → 26.7 (`⬆️ +5.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 0–9 → 0–10 | 27.1 → 🔴 ** 31.4** (`⬆️ +4.3`) | 24.8 → 23.8 (`-1.0`) | 34.8 → 47.2 (`⬆️ +12.4`) | 21.7 → 23.3 (`⬆️ +1.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 5 → 4 | 27.1 → 🔴 ** 28.0** (`⬆️ +0.9`) | 24.8 → 28.2 (`⬆️ +3.4`) | 34.8 → 34.0 (`-0.8`) | 21.7 | 🟢 POPRAWIA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 3 → 4 | 27.1 → 🔴 ** 27.3** (`⬆️ +0.2`) | 24.8 | 34.8 → 35.0 (`⬆️ +0.2`) | 21.7 → 22.1 (`⬆️ +0.4`) | ⚪ OPTYMALNY |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 0 → 1 | 27.1 → 🔴 ** 27.2** (`⬆️ +0.1`) | 24.8 → 25.0 (`⬆️ +0.2`) | 34.8 → 35.5 (`⬆️ +0.7`) | 21.7 → 21.2 (`-0.5`) | ⚪ OPTYMALNY |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 5 → 6 | 27.1 → 🔴 ** 26.2** (`-0.9`) | 24.8 → 21.2 (`-3.6`) | 34.8 → 37.6 (`⬆️ +2.8`) | 21.7 → 19.9 (`-1.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 6 → 7 | 27.1 → 🔴 ** 24.8** (`-2.3`) | 24.8 → 26.1 (`⬆️ +1.3`) | 34.8 → 32.9 (`-1.9`) | 21.7 → 15.4 (`-6.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 27.1 → 🔴 ** 20.7** (`-6.4`) | 24.8 → 19.2 (`-5.6`) | 34.8 → 21.0 (`-13.8`) | 21.7 → 21.8 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 5 → 4 | 27.1 → 🔴 ** 19.0** (`-8.1`) | 24.8 → 27.3 (`⬆️ +2.5`) | 34.8 → 24.2 (`-10.6`) | 21.7 → 5.5 (`-16.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 3/5 → 2/4 | 27.1 → 🔴 ** 18.5** (`-8.6`) | 24.8 → 25.7 (`⬆️ +0.9`) | 34.8 → 21.7 (`-13.1`) | 21.7 → 8.0 (`-13.7`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 17 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 0–9 → 1–9 | 🔴 ** 27.1** | 24.8 | 34.8 | 21.7 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 0–9 → 0–8 | 27.1 → 🔴 ** 26.7** (`-0.4`) | 24.8 → 24.3 (`-0.5`) | 34.8 → 34.0 (`-0.8`) | 21.7 | ⚪ OPTYMALNY |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 5 → 6 | 27.1 → 🔴 ** 23.9** (`-3.2`) | 24.8 → 19.0 (`-5.8`) | 34.8 → 30.9 (`-3.9`) | 21.7 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 3 → 4 | 27.1 → 🔴 ** 20.1** (`-7.0`) | 24.8 → 24.3 (`-0.5`) | 34.8 → 25.9 (`-8.9`) | 21.7 → 10.2 (`-11.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 3 → 2 | 27.1 → 🔴 ** 17.7** (`-9.4`) | 24.8 → 22.4 (`-2.4`) | 34.8 → 22.6 (`-12.2`) | 21.7 → 8.0 (`-13.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 27.1 → 🔴 ** 17.6** (`-9.5`) | 24.8 → 19.5 (`-5.3`) | 34.8 → 21.6 (`-13.2`) | 21.7 → 11.7 (`-10.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 3/5 → 4/6 | 27.1 → 🔴 ** 16.9** (`-10.2`) | 24.8 → 18.5 (`-6.3`) | 34.8 → 22.0 (`-12.8`) | 21.7 → 10.2 (`-11.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 27.1 → 🔴 ** 11.0** (`-16.1`) | 24.8 → 12.4 (`-12.4`) | 34.8 → 13.8 (`-21.0`) | 21.7 → 6.8 (`-14.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 27.1 → 🔴 **  9.6** (`-17.5`) | 24.8 → 10.1 (`-14.7`) | 34.8 → 12.6 (`-22.2`) | 21.7 → 6.1 (`-15.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 27.1 → 🔴 **  8.2** (`-18.9`) | 24.8 → 13.8 (`-11.0`) | 34.8 → 8.3 (`-26.5`) | 21.7 → 2.6 (`-19.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 27.1 → 🔴 **  5.1** (`-22.0`) | 24.8 → 8.9 (`-15.9`) | 34.8 → 6.0 (`-28.8`) | 21.7 → 0.3 (`-21.4`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (12)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 6.73 Er (1–12) | 5.5% | 5.1% | 1.62 (0–4) | 4.33 (0–22) | 3.84zł (0.0–11.3) | 6.53 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 6.60 Er (1–12) | 4.8% | 5.1% | 1.58 (0–4) | 4.23 (0–22) | 3.78zł (0.0–11.3) | 6.48 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 6.64 Er (1–12) | 5.5% | 5.1% | 1.57 (0–4) | 4.25 (0–22) | 3.80zł (0.0–11.3) | 6.47 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 6.64 Er (1–12) | 3.7% | 5.1% | 1.60 (0–4) | 4.22 (0–22) | 3.79zł (0.0–11.3) | 6.52 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 6.60 Er (1–12) | 4.7% | 5.1% | 1.60 (0–4) | 4.17 (0–22) | 3.79zł (0.0–11.3) | 6.48 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 6.73 Er (1–12) | 5.5% | 5.1% | 1.62 (0–4) | 4.34 (0–22) | 3.84zł (0.0–11.3) | 6.53 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 6.76 Er (1–12) | 5.5% | 5.1% | 1.63 (0–4) | 4.37 (0–22) | 3.84zł (0.0–11.3) | 6.56 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 6.87 Er (1–12) | 7.1% | 5.1% | 1.65 (0–4) | 4.45 (0–22) | 3.90zł (0.0–11.7) | 6.56 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 6.83 Er (1–12) | 5.5% | 5.1% | 1.64 (0–4) | 4.45 (0–22) | 3.89zł (0.2–11.3) | 6.58 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 6.39 Er (1–12) | 4.8% | 5.2% | 1.55 (0–4) | 3.95 (0–21) | 3.71zł (0.0–11.3) | 6.43 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 6.50 Er (1–12) | 4.0% | 5.1% | 1.56 (0–4) | 4.13 (0–22) | 3.75zł (0.0–11.3) | 6.45 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 6.18 Er (1–12) | 3.8% | 5.1% | 1.50 (0–4) | 3.81 (0–22) | 3.64zł (0.0–10.7) | 6.26 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 17 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_HERESY_LOW_PLUS1` | 6.73 Er (1–12) | 5.5% | 5.1% | 1.62 (0–4) | 4.33 (0–22) | 3.84zł (0.0–11.3) | 6.53 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 6.75 Er (1–12) | 5.8% | 5.1% | 1.62 (0–4) | 4.37 (0–22) | 3.85zł (0.0–11.3) | 6.53 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 6.81 Er (1–12) | 6.1% | 5.1% | 1.64 (0–4) | 4.44 (0–22) | 3.88zł (0.0–11.3) | 6.56 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 6.97 Er (1–12) | 6.2% | 5.1% | 1.67 (0–4) | 4.54 (0–22) | 3.93zł (0.0–12.3) | 6.63 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 6.30 Er (1–12) | 4.5% | 5.1% | 1.52 (0–4) | 3.97 (0–22) | 3.68zł (0.0–10.7) | 6.31 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 7.04 Er (1–12) | 6.9% | 5.0% | 1.69 (0–4) | 4.70 (0–22) | 3.97zł (0.0–11.3) | 6.65 (1.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_GC_FALLS_PLUS1` | 7.06 Er (1–12) | 6.8% | 5.1% | 1.69 (0–4) | 4.64 (0–22) | 3.97zł (0.0–12.3) | 6.66 (1.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_PLUS1` | 7.23 Er (2–12) | 7.1% | 5.1% | 1.76 (0–4) | 4.83 (0–22) | 4.02zł (0.0–11.3) | 6.83 (2.3–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_KB_DECREES_PLUS1` | 7.21 Er (1–12) | 8.8% | 5.2% | 1.74 (0–4) | 4.98 (0–22) | 4.02zł (0.0–11.3) | 6.70 (1.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_MINUS1` | 5.59 Er (1–12) | 2.0% | 5.2% | 1.30 (0–4) | 3.21 (0–17) | 3.45zł (0.0–10.7) | 5.79 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 3.88 Er (1–12) | 2.1% | 4.5% | 0.82 (0–4) | 1.86 (0–20) | 3.19zł (0.0–11.3) | 4.43 (0.7–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.