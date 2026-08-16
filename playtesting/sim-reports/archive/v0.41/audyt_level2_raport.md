# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.41

**Wersja Balansu:** `v0.41` | **Data:** 2026-08-16 00:24 | **Przeanalizowano Wariantów:** 29 | **Próba:** 5000 gier/setup | **Czas:** 256.6s
**Wynik Bazy Poziomu 2 (Global):** `🔴 27.6 pkt` | 3p: `38.5 pkt` | 4p: `16.7 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (11)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🔴 ** 27.6** | 38.5 | 16.7 | 0.0 | ⚪ OPTYMALNY |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 27.6 → 🔴 ** 50.9** (`⬆️ +23.3`) | 38.5 → 86.8 (`⬆️ +48.3`) | 16.7 → 14.9 (`-1.8`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 27.6 → 🔴 ** 41.0** (`⬆️ +13.4`) | 38.5 → 18.3 (`-20.2`) | 16.7 → 47.2 (`⬆️ +30.5`) | 0.0 → 57.6 (`⬆️ +57.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 6/6/6 → 7/7/7 | 27.6 → 🔴 ** 37.6** (`⬆️ +10.0`) | 38.5 → 54.3 (`⬆️ +15.8`) | 16.7 → 20.9 (`⬆️ +4.2`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 27.6 → 🔴 ** 36.0** (`⬆️ +8.4`) | 38.5 → 52.3 (`⬆️ +13.8`) | 16.7 → 19.8 (`⬆️ +3.1`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 3–8 → 3–7 | 27.6 → 🔴 ** 31.8** (`⬆️ +4.2`) | 38.5 → 44.6 (`⬆️ +6.1`) | 16.7 → 18.9 (`⬆️ +2.2`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 3/4/4 → 4/5/5 | 27.6 → 🔴 ** 29.8** (`⬆️ +2.2`) | 38.5 → 29.8 (`-8.7`) | 16.7 → 0.0 (`-16.7`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L2_KB_ERA_MINUS1` | Korona Era: 5/5/5 → 4/4/4 | 27.6 → 🔴 ** 28.4** (`⬆️ +0.8`) | 38.5 → 38.6 (`⬆️ +0.1`) | 16.7 → 18.1 (`⬆️ +1.4`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L2_CAA_ERA_PLUS1` | Cienie Era: 5 → 6 | 27.6 → 🔴 ** 27.9** (`⬆️ +0.3`) | 38.5 → 38.6 (`⬆️ +0.1`) | 16.7 → 17.2 (`⬆️ +0.5`) | 0.0 | ⚪ OPTYMALNY |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2 → 3 | 27.6 → 🔴 ** 23.7** (`-3.9`) | 38.5 → 38.9 (`⬆️ +0.4`) | 16.7 → 8.5 (`-8.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_MINUS1` | Korona Haki: 1 → 0 | 27.6 → 🔴 ** 19.4** (`-8.2`) | 38.5 → 10.4 (`-28.1`) | 16.7 → 16.2 (`-0.5`) | 0.0 → 31.7 (`⬆️ +31.7`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 18 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_MINUS1` | Cienie Era: 5 → 4 | 🔴 ** 27.6** | 38.5 | 16.7 | 0.0 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–8 → 3–9 | 27.6 → 🔴 ** 27.0** (`-0.6`) | 38.5 → 38.0 (`-0.5`) | 16.7 → 16.0 (`-0.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 3 → 4 | 27.6 → 🔴 ** 26.4** (`-1.2`) | 38.5 → 36.0 (`-2.5`) | 16.7 | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 27.6 → 🔴 ** 26.3** (`-1.3`) | 38.5 → 38.0 (`-0.5`) | 16.7 → 14.6 (`-2.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_PLUS1` | Korona Era: 5/5/5 → 6/6/6 | 27.6 → 🔴 ** 26.1** (`-1.5`) | 38.5 → 37.0 (`-1.5`) | 16.7 → 15.3 (`-1.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 3 → 2 | 27.6 → 🔴 ** 25.9** (`-1.7`) | 38.5 → 35.1 (`-3.4`) | 16.7 | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 6/6/6 → 5/5/5 | 27.6 → 🔴 ** 20.5** (`-7.1`) | 38.5 → 38.0 (`-0.5`) | 16.7 → 3.0 (`-13.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 27.6 → 🔴 ** 19.7** (`-7.9`) | 38.5 → 38.0 (`-0.5`) | 16.7 → 1.4 (`-15.3`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 2 → 3 | 27.6 → 🔴 ** 18.6** (`-9.0`) | 38.5 → 18.6 (`-19.9`) | 16.7 → 0.0 (`-16.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 2 → 1 | 27.6 → 🔴 ** 18.6** (`-9.0`) | 38.5 → 18.6 (`-19.9`) | 16.7 → 0.0 (`-16.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 3/4/4 → 2/3/3 | 27.6 → 🔴 ** 18.0** (`-9.6`) | 38.5 → 20.4 (`-18.1`) | 16.7 → 15.6 (`-1.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 2/3 → 3/4 | 27.6 → 🔴 ** 16.1** (`-11.5`) | 38.5 → 16.1 (`-22.4`) | 16.7 → 0.0 (`-16.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 2/3 → 1/2 | 27.6 → 🔴 ** 15.2** (`-12.4`) | 38.5 → 15.2 (`-23.3`) | 16.7 → 0.0 (`-16.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 27.6 → 🔴 ** 12.9** (`-14.7`) | 38.5 → 10.4 (`-28.1`) | 16.7 → 15.3 (`-1.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 1 → 2 | 27.6 → 🔴 ** 12.9** (`-14.7`) | 38.5 → 10.4 (`-28.1`) | 16.7 → 15.3 (`-1.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2 → 1 | 27.6 → 🔴 ** 10.4** (`-17.2`) | 38.5 → 10.4 (`-28.1`) | 16.7 → 0.0 (`-16.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 27.6 → 🔴 **  9.9** (`-17.7`) | 38.5 → 9.9 (`-28.6`) | 16.7 → 0.0 (`-16.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 27.6 → 🔴 **  9.9** (`-17.7`) | 38.5 → 9.9 (`-28.6`) | 16.7 → 0.0 (`-16.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (11)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 6.13 Er (1–11) | 1.6% | 26.1% | 0.46 (0–3) | 3.13 (0–18) | 1.20zł (0.0–6.0) | 5.83 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 6.44 Er (1–11) | 3.4% | 27.0% | 0.47 (0–3) | 3.50 (0–19) | 1.31zł (0.0–6.7) | 5.98 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.83 Er (1–11) | 1.2% | 25.3% | 0.45 (0–3) | 2.81 (0–18) | 1.14zł (0.0–6.0) | 5.64 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 6.27 Er (1–11) | 1.6% | 26.6% | 0.46 (0–3) | 3.29 (0–18) | 1.26zł (0.0–6.0) | 5.91 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_PLUS1` | 6.20 Er (1–11) | 1.7% | 26.3% | 0.46 (0–3) | 3.22 (0–18) | 1.23zł (0.0–6.0) | 5.87 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 6.14 Er (1–11) | 1.7% | 26.2% | 0.46 (0–3) | 3.16 (0–18) | 1.20zł (0.0–6.0) | 5.83 (0.0–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 6.21 Er (1–11) | 2.0% | 26.3% | 0.46 (0–3) | 3.20 (0–18) | 1.21zł (0.0–6.3) | 5.86 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_MINUS1` | 6.11 Er (1–11) | 1.6% | 26.1% | 0.46 (0–3) | 3.11 (0–18) | 1.19zł (0.0–6.0) | 5.82 (0.0–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_PLUS1` | 6.15 Er (1–11) | 1.6% | 26.2% | 0.46 (0–3) | 3.15 (0–18) | 1.20zł (0.0–6.0) | 5.85 (0.0–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 6.16 Er (1–11) | 1.8% | 26.2% | 0.46 (0–3) | 3.16 (0–18) | 1.20zł (0.0–6.0) | 5.84 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_MINUS1` | 5.82 Er (1–11) | 1.0% | 25.1% | 0.44 (0–3) | 2.77 (0–18) | 1.14zł (0.0–6.0) | 5.67 (0.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 18 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_MINUS1` | 6.11 Er (1–11) | 1.6% | 26.1% | 0.46 (0–3) | 3.12 (0–18) | 1.20zł (0.0–6.0) | 5.82 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 6.12 Er (1–11) | 1.6% | 26.1% | 0.46 (0–3) | 3.12 (0–18) | 1.19zł (0.0–6.0) | 5.83 (0.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 6.21 Er (1–11) | 1.9% | 26.3% | 0.46 (0–3) | 3.23 (0–19) | 1.21zł (0.0–7.0) | 5.87 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_MINUS1` | 6.09 Er (1–11) | 1.6% | 26.0% | 0.46 (0–3) | 3.09 (0–18) | 1.18zł (0.0–6.0) | 5.80 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_PLUS1` | 6.16 Er (1–11) | 1.6% | 26.2% | 0.46 (0–3) | 3.17 (0–18) | 1.20zł (0.0–6.0) | 5.85 (0.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 5.98 Er (1–11) | 1.4% | 25.7% | 0.46 (0–3) | 2.96 (0–18) | 1.18zł (0.0–6.0) | 5.73 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 6.01 Er (1–11) | 1.6% | 25.7% | 0.45 (0–3) | 3.02 (0–18) | 1.18zł (0.0–6.0) | 5.75 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.92 Er (1–11) | 1.2% | 25.4% | 0.45 (0–3) | 2.90 (0–18) | 1.14zł (0.0–6.0) | 5.71 (0.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 6.31 Er (2–11) | 2.0% | 26.5% | 0.47 (0–3) | 3.29 (0–18) | 1.21zł (0.0–6.0) | 5.94 (0.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 5.52 Er (1–11) | 1.2% | 24.7% | 0.41 (0–3) | 2.70 (0–18) | 1.19zł (0.0–6.0) | 5.35 (0.0–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.89 Er (1–11) | 1.0% | 25.5% | 0.45 (0–3) | 2.95 (0–18) | 1.17zł (0.0–6.0) | 5.72 (0.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 6.40 Er (2–11) | 2.3% | 26.8% | 0.47 (0–3) | 3.38 (0–19) | 1.23zł (0.0–7.0) | 5.98 (0.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 5.38 Er (1–11) | 1.0% | 24.3% | 0.41 (0–3) | 2.53 (0–18) | 1.17zł (0.0–6.0) | 5.25 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.30 Er (1–11) | 3.5% | 26.5% | 0.47 (0–3) | 3.34 (0–19) | 1.24zł (0.0–7.0) | 5.91 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 6.29 Er (1–11) | 3.4% | 26.5% | 0.47 (0–3) | 3.34 (0–19) | 1.24zł (0.0–7.0) | 5.90 (0.0–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 5.17 Er (1–11) | 0.5% | 22.9% | 0.40 (0–3) | 2.45 (0–18) | 1.11zł (0.0–6.0) | 5.26 (0.0–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 6.60 Er (1–11) | 2.6% | 27.3% | 0.48 (0–3) | 3.58 (0–21) | 1.25zł (0.0–6.7) | 6.14 (1.3–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.81 Er (1–11) | 0.6% | 21.8% | 0.38 (0–3) | 1.90 (0–18) | 1.14zł (0.0–6.0) | 4.78 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.