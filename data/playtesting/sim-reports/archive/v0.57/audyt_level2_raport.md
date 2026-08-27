[Strona główna](../../../../../README.md) > [v0.57](README.md) > [audyt_level2_raport](audyt_level2_raport.md)

---

# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.57

**Wersja Balansu:** `v0.57` | **Data:** 2026-08-16 15:38 | **Przeanalizowano Wariantów:** 29 | **Próba:** 3000 gier/setup | **Czas:** 193.29s
**Wynik Bazy Poziomu 2 (Global):** `🔴 51.6 pkt` | 3p: `66.8 pkt` | 4p: `49.4 pkt` | 5p: `38.5 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (11)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🔴 ** 51.6** | 66.8 | 49.4 | 38.5 | ⚪ OPTYMALNY |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 2/3 → 3/4 | 51.6 → 🟠 ** 62.5** (`⬆️ +10.9`) | 66.8 → 79.4 (`⬆️ +12.6`) | 49.4 → 52.5 (`⬆️ +3.1`) | 38.5 → 55.5 (`⬆️ +17.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 2 → 3 | 51.6 → 🔴 ** 58.6** (`⬆️ +7.0`) | 66.8 → 75.9 (`⬆️ +9.1`) | 49.4 → 44.4 (`-5.0`) | 38.5 → 55.5 (`⬆️ +17.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 6/6/6 → 5/5/5 | 51.6 → 🔴 ** 55.8** (`⬆️ +4.2`) | 66.8 → 62.9 (`-3.9`) | 49.4 → 58.4 (`⬆️ +9.0`) | 38.5 → 46.0 (`⬆️ +7.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 3 → 4 | 51.6 → 🔴 ** 55.4** (`⬆️ +3.8`) | 66.8 → 70.3 (`⬆️ +3.5`) | 49.4 → 57.5 (`⬆️ +8.1`) | 38.5 | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 51.6 → 🔴 ** 55.3** (`⬆️ +3.7`) | 66.8 → 64.5 (`-2.3`) | 49.4 → 57.0 (`⬆️ +7.6`) | 38.5 → 44.5 (`⬆️ +6.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KB_ERA_MINUS1` | Korona Era: 4/4/4 → 3/3/3 | 51.6 → 🔴 ** 53.3** (`⬆️ +1.7`) | 66.8 → 67.5 (`⬆️ +0.7`) | 49.4 → 51.4 (`⬆️ +2.0`) | 38.5 → 41.0 (`⬆️ +2.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–8 → 3–9 | 51.6 → 🔴 ** 53.1** (`⬆️ +1.5`) | 66.8 → 66.1 (`-0.7`) | 49.4 → 53.0 (`⬆️ +3.6`) | 38.5 → 40.2 (`⬆️ +1.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_CAA_ERA_MINUS1` | Cienie Era: 5 → 4 | 51.6 → 🔴 ** 52.3** (`⬆️ +0.7`) | 66.8 → 67.4 (`⬆️ +0.6`) | 49.4 → 50.4 (`⬆️ +1.0`) | 38.5 → 39.1 (`⬆️ +0.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2 → 3 | 51.6 → 🔴 ** 51.7** (`⬆️ +0.1`) | 66.8 → 65.9 (`-0.9`) | 49.4 → 51.7 (`⬆️ +2.3`) | 38.5 → 37.4 (`-1.1`) | ⚪ OPTYMALNY |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 4/4/5 → 5/5/6 | 51.6 → 🔴 ** 49.5** (`-2.1`) | 66.8 → 57.9 (`-8.9`) | 49.4 → 55.3 (`⬆️ +5.9`) | 38.5 → 35.4 (`-3.1`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 18 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 🔴 ** 51.6** | 66.8 | 49.4 | 38.5 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 🔴 ** 51.6** | 66.8 | 49.4 | 38.5 | ⚪ OPTYMALNY |
| `L2_CAA_ERA_PLUS1` | Cienie Era: 5 → 6 | 51.6 → 🔴 ** 50.0** (`-1.6`) | 66.8 → 65.2 (`-1.6`) | 49.4 → 47.3 (`-2.1`) | 38.5 → 37.4 (`-1.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_PLUS1` | Korona Era: 4/4/4 → 5/5/5 | 51.6 → 🔴 ** 48.5** (`-3.1`) | 66.8 → 65.1 (`-1.7`) | 49.4 → 45.9 (`-3.5`) | 38.5 → 34.6 (`-3.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 3–8 → 3–7 | 51.6 → 🔴 ** 46.3** (`-5.3`) | 66.8 → 60.6 (`-6.2`) | 49.4 → 42.8 (`-6.6`) | 38.5 → 35.4 (`-3.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 3 → 2 | 51.6 → 🔴 ** 45.3** (`-6.3`) | 66.8 → 54.9 (`-11.9`) | 49.4 → 42.4 (`-7.0`) | 38.5 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_MINUS1` | Korona Haki: 1 → 0 | 51.6 → 🔴 ** 41.0** (`-10.6`) | 66.8 → 46.7 (`-20.1`) | 49.4 → 44.7 (`-4.7`) | 38.5 → 31.5 (`-7.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 6/6/6 → 7/7/7 | 51.6 → 🔴 ** 39.9** (`-11.7`) | 66.8 → 58.3 (`-8.5`) | 49.4 → 35.0 (`-14.4`) | 38.5 → 26.4 (`-12.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 4/4/5 → 3/3/4 | 51.6 → 🔴 ** 38.8** (`-12.8`) | 66.8 → 56.6 (`-10.2`) | 49.4 → 28.1 (`-21.3`) | 38.5 → 31.8 (`-6.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 51.6 → 🔴 ** 38.4** (`-13.2`) | 66.8 → 53.5 (`-13.3`) | 49.4 → 33.7 (`-15.7`) | 38.5 → 28.1 (`-10.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 51.6 → 🔴 ** 31.8** (`-19.8`) | 66.8 → 38.7 (`-28.1`) | 49.4 → 32.6 (`-16.8`) | 38.5 → 24.1 (`-14.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 2 → 1 | 51.6 → 🔴 ** 27.7** (`-23.9`) | 66.8 → 55.3 (`-11.5`) | 49.4 → 23.7 (`-25.7`) | 38.5 → 4.1 (`-34.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 1 → 2 | 51.6 → 🔴 ** 25.7** (`-25.9`) | 66.8 → 31.8 (`-35.0`) | 49.4 → 25.2 (`-24.2`) | 38.5 → 20.1 (`-18.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 51.6 → 🔴 ** 24.3** (`-27.3`) | 66.8 → 32.4 (`-34.4`) | 49.4 → 22.8 (`-26.6`) | 38.5 → 17.6 (`-20.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 51.6 → 🔴 ** 24.1** (`-27.5`) | 66.8 → 30.7 (`-36.1`) | 49.4 → 23.4 (`-26.0`) | 38.5 → 18.2 (`-20.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 2/3 → 1/2 | 51.6 → 🔴 ** 21.4** (`-30.2`) | 66.8 → 43.3 (`-23.5`) | 49.4 → 16.7 (`-32.7`) | 38.5 → 4.1 (`-34.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2 → 1 | 51.6 → 🔴 ** 13.8** (`-37.8`) | 66.8 → 29.9 (`-36.9`) | 49.4 → 11.1 (`-38.3`) | 38.5 → 0.5 (`-38.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 51.6 → 🔴 ** 12.4** (`-39.2`) | 66.8 → 25.7 (`-41.1`) | 49.4 → 10.8 (`-38.6`) | 38.5 → 0.8 (`-37.7`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (11)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 1.91zł (0.0–8.3) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 5.83 Er (2–11) | 1.3% | 26.5% | 1.45 (0–4) | 3.54 (0–21) | 1.96zł (0.0–8.7) | 6.46 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 5.71 Er (2–11) | 1.1% | 26.1% | 1.43 (0–4) | 3.38 (0–20) | 1.93zł (0.0–8.3) | 6.40 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.32 Er (1–11) | 0.8% | 24.7% | 1.31 (0–4) | 3.01 (0–20) | 1.87zł (0.0–8.3) | 6.15 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 5.58 Er (1–11) | 1.1% | 25.8% | 1.39 (0–4) | 3.33 (0–21) | 1.94zł (0.0–8.7) | 6.31 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.39 Er (1–11) | 0.7% | 25.1% | 1.36 (0–4) | 3.09 (0–20) | 1.89zł (0.0–8.3) | 6.21 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_MINUS1` | 5.44 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.15 (0–20) | 1.92zł (0.0–8.3) | 6.22 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 5.42 Er (1–11) | 0.7% | 25.2% | 1.37 (0–4) | 3.13 (0–20) | 1.89zł (0.0–8.3) | 6.24 (1.0–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_MINUS1` | 5.43 Er (1–11) | 0.8% | 25.3% | 1.37 (0–4) | 3.15 (0–20) | 1.91zł (0.0–8.3) | 6.23 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 5.52 Er (1–11) | 0.9% | 25.6% | 1.39 (0–4) | 3.22 (0–20) | 1.93zł (0.0–8.3) | 6.27 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 5.56 Er (1–11) | 1.1% | 25.8% | 1.40 (0–4) | 3.25 (0–20) | 1.93zł (0.0–8.3) | 6.28 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 18 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_HERESY_LOW_MINUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 1.91zł (0.0–8.3) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_PLUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 1.91zł (0.0–8.3) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_PLUS1` | 5.50 Er (1–11) | 0.8% | 25.6% | 1.39 (0–4) | 3.21 (0–20) | 1.93zł (0.0–8.3) | 6.28 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_PLUS1` | 5.51 Er (1–11) | 0.8% | 25.6% | 1.38 (0–4) | 3.22 (0–20) | 1.92zł (0.0–8.3) | 6.27 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 5.52 Er (1–11) | 1.0% | 25.6% | 1.39 (0–4) | 3.25 (0–21) | 1.94zł (0.0–8.3) | 6.26 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 5.30 Er (1–11) | 0.7% | 24.9% | 1.34 (0–4) | 2.95 (0–18) | 1.89zł (0.0–8.0) | 6.13 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_MINUS1` | 5.18 Er (1–11) | 0.6% | 24.1% | 1.30 (0–4) | 2.85 (0–20) | 1.85zł (0.0–8.3) | 6.10 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 5.58 Er (1–11) | 0.9% | 25.9% | 1.40 (0–4) | 3.32 (0–20) | 1.96zł (0.0–8.3) | 6.30 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.26 Er (1–11) | 0.5% | 24.6% | 1.32 (0–4) | 3.02 (0–20) | 1.87zł (0.0–8.3) | 6.16 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 5.60 Er (1–11) | 1.2% | 25.9% | 1.40 (0–4) | 3.34 (0–20) | 1.96zł (0.0–8.3) | 6.30 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.02 Er (1–11) | 0.6% | 23.5% | 1.25 (0–4) | 2.68 (0–18) | 1.81zł (0.0–8.3) | 5.96 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 4.96 Er (1–11) | 0.7% | 24.0% | 1.22 (0–4) | 2.80 (0–20) | 1.92zł (0.0–8.3) | 5.81 (0.5–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_KB_HOOKS_PLUS1` | 5.71 Er (1–11) | 2.2% | 26.2% | 1.44 (0–4) | 3.48 (0–20) | 1.99zł (0.0–9.0) | 6.34 (1.0–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 5.81 Er (1–11) | 1.3% | 26.6% | 1.48 (0–4) | 3.54 (0–20) | 1.98zł (0.0–9.0) | 6.47 (1.8–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 5.73 Er (1–11) | 2.3% | 26.3% | 1.45 (0–4) | 3.50 (0–24) | 1.99zł (0.0–9.0) | 6.35 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 4.79 Er (1–11) | 0.5% | 23.4% | 1.19 (0–4) | 2.58 (0–18) | 1.90zł (0.0–8.0) | 5.69 (0.5–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_SO_CONDEMNS_MINUS1` | 4.39 Er (1–11) | 0.4% | 20.4% | 1.06 (0–4) | 2.42 (0–20) | 1.81zł (0.0–8.3) | 5.55 (1.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_MINUS1` | 4.41 Er (1–11) | 0.2% | 21.0% | 1.03 (0–4) | 2.12 (0–16) | 1.80zł (0.0–6.7) | 5.38 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.