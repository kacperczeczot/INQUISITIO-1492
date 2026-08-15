# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.40

**Wersja Balansu:** `v0.40` | **Data:** 2026-08-15 22:49 | **Przeanalizowano Wariantów:** 28 | **Próba:** 500 gier/setup | **Czas:** 52.67s
**Wynik Bazy Poziomu 2 (Global):** `🔴 34.0 pkt` | 3p: `51.3 pkt` | 4p: `16.6 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (12)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🔴 ** 34.0** | 51.3 | 16.6 | 0.0 | ⚪ OPTYMALNY |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 34.0 → 🔴 ** 49.8** (`⬆️ +15.8`) | 51.3 → 45.1 (`-6.2`) | 16.6 → 32.3 (`⬆️ +15.7`) | 0.0 → 72.1 (`⬆️ +72.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 7/6/6 → 8/7/7 | 34.0 → 🔴 ** 47.3** (`⬆️ +13.3`) | 51.3 → 79.6 (`⬆️ +28.3`) | 16.6 → 15.0 (`-1.6`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 3/4/4 → 4/5/5 | 34.0 → 🔴 ** 41.9** (`⬆️ +7.9`) | 51.3 → 41.9 (`-9.4`) | 16.6 → 0.0 (`-16.6`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 34.0 → 🔴 ** 40.5** (`⬆️ +6.5`) | 51.3 → 73.1 (`⬆️ +21.8`) | 16.6 → 8.0 (`-8.6`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 3–8 → 3–7 | 34.0 → 🔴 ** 37.6** (`⬆️ +3.6`) | 51.3 → 59.0 (`⬆️ +7.7`) | 16.6 → 16.2 (`-0.4`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 34.0 → 🔴 ** 36.7** (`⬆️ +2.7`) | 51.3 → 36.7 (`-14.6`) | 16.6 → 0.0 (`-16.6`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 2 → 3 | 34.0 → 🔴 ** 36.5** (`⬆️ +2.5`) | 51.3 → 36.5 (`-14.8`) | 16.6 → 0.0 (`-16.6`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 2 → 1 | 34.0 → 🔴 ** 36.5** (`⬆️ +2.5`) | 51.3 → 36.5 (`-14.8`) | 16.6 → 0.0 (`-16.6`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L2_KB_ERA_MINUS1` | Korona Era: 6/5/5 → 5/4/4 | 34.0 → 🔴 ** 35.6** (`⬆️ +1.6`) | 51.3 → 54.6 (`⬆️ +3.3`) | 16.6 | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 34.0 → 🔴 ** 35.5** (`⬆️ +1.5`) | 51.3 → 53.5 (`⬆️ +2.2`) | 16.6 → 17.6 (`⬆️ +1.0`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L2_CAA_ERA_MINUS1` | Cienie Era: 5 → 4 | 🔴 ** 34.0** | 51.3 → 51.2 (`-0.1`) | 16.6 → 16.7 (`⬆️ +0.1`) | 0.0 | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 16 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_PLUS1` | Cienie Era: 5 → 6 | 🔴 ** 34.0** | 51.3 | 16.6 | 0.0 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–8 → 3–9 | 34.0 → 🔴 ** 33.8** (`-0.2`) | 51.3 → 51.0 (`-0.3`) | 16.6 → 16.5 (`-0.1`) | 0.0 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 34.0 → 🔴 ** 32.6** (`-1.4`) | 51.3 → 51.0 (`-0.3`) | 16.6 → 14.3 (`-2.3`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 3 → 4 | 34.0 → 🔴 ** 28.9** (`-5.1`) | 51.3 → 41.1 (`-10.2`) | 16.6 | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_PLUS1` | Korona Era: 6/5/5 → 7/6/6 | 34.0 → 🔴 ** 27.8** (`-6.2`) | 51.3 → 38.9 (`-12.4`) | 16.6 | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2 → 3 | 34.0 → 🔴 ** 26.6** (`-7.4`) | 51.3 → 51.0 (`-0.3`) | 16.6 → 2.3 (`-14.3`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 2/3 → 3/4 | 34.0 → 🔴 ** 26.3** (`-7.7`) | 51.3 → 26.3 (`-25.0`) | 16.6 → 0.0 (`-16.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 3 → 2 | 34.0 → 🔴 ** 25.4** (`-8.6`) | 51.3 → 34.2 (`-17.1`) | 16.6 | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2 → 1 | 34.0 → 🔴 ** 23.9** (`-10.1`) | 51.3 → 23.9 (`-27.4`) | 16.6 → 0.0 (`-16.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 7/6/6 → 6/5/5 | 34.0 → 🔴 ** 22.3** (`-11.7`) | 51.3 → 41.3 (`-10.0`) | 16.6 → 3.4 (`-13.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 34.0 → 🔴 ** 19.9** (`-14.1`) | 51.3 → 23.1 (`-28.2`) | 16.6 | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 1 → 2 | 34.0 → 🔴 ** 19.9** (`-14.1`) | 51.3 → 23.1 (`-28.2`) | 16.6 | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 2/3 → 1/2 | 34.0 → 🔴 ** 19.4** (`-14.6`) | 51.3 → 19.4 (`-31.9`) | 16.6 → 0.0 (`-16.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 3/4/4 → 2/3/3 | 34.0 → 🔴 ** 18.8** (`-15.2`) | 51.3 → 30.2 (`-21.1`) | 16.6 → 7.4 (`-9.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 34.0 → 🔴 **  6.9** (`-27.1`) | 51.3 → 6.9 (`-44.4`) | 16.6 → 0.0 (`-16.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 34.0 → 🔴 **  6.9** (`-27.1`) | 51.3 → 6.9 (`-44.4`) | 16.6 → 0.0 (`-16.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (12)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 6.12 Er (1–10) | 3.5% | 26.4% | 0.47 (0–3) | 3.31 (0–16) | 1.27zł (0.0–6.0) | 5.93 (0.8–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.87 Er (1–10) | 2.5% | 25.7% | 0.46 (0–3) | 3.02 (0–16) | 1.21zł (0.0–6.0) | 5.78 (0.8–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 6.27 Er (1–10) | 3.7% | 26.9% | 0.48 (0–3) | 3.48 (0–16) | 1.33zł (0.0–6.0) | 6.00 (0.8–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 6.22 Er (1–10) | 4.3% | 26.7% | 0.47 (0–3) | 3.39 (0–16) | 1.29zł (0.0–6.0) | 5.97 (0.8–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 6.33 Er (1–10) | 6.6% | 27.0% | 0.48 (0–3) | 3.57 (0–21) | 1.35zł (0.0–6.0) | 6.02 (0.8–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 6.14 Er (1–10) | 4.0% | 26.5% | 0.47 (0–3) | 3.33 (0–16) | 1.27zł (0.0–6.0) | 5.93 (0.8–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 6.00 Er (1–10) | 2.7% | 26.0% | 0.46 (0–3) | 3.16 (0–15) | 1.23zł (0.0–6.0) | 5.86 (0.8–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 6.30 Er (2–10) | 4.2% | 26.8% | 0.48 (0–3) | 3.47 (0–16) | 1.28zł (0.0–6.0) | 6.04 (0.8–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 5.51 Er (1–10) | 2.7% | 25.1% | 0.42 (0–3) | 2.86 (0–16) | 1.26zł (0.0–6.0) | 5.45 (0.6–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_MINUS1` | 6.09 Er (1–10) | 3.5% | 26.3% | 0.47 (0–3) | 3.28 (0–16) | 1.26zł (0.0–6.0) | 5.91 (0.8–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_PLUS1` | 6.17 Er (1–10) | 3.8% | 26.6% | 0.47 (0–3) | 3.37 (0–16) | 1.29zł (0.0–6.0) | 5.96 (0.8–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_MINUS1` | 6.11 Er (1–10) | 3.5% | 26.4% | 0.47 (0–3) | 3.30 (0–16) | 1.27zł (0.0–6.0) | 5.92 (0.8–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 16 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_PLUS1` | 6.14 Er (1–10) | 3.5% | 26.5% | 0.47 (0–3) | 3.32 (0–16) | 1.27zł (0.0–6.0) | 5.94 (0.8–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 6.11 Er (1–10) | 3.4% | 26.4% | 0.47 (0–3) | 3.30 (0–16) | 1.26zł (0.0–6.0) | 5.93 (0.8–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_MINUS1` | 6.10 Er (1–10) | 3.5% | 26.3% | 0.47 (0–3) | 3.28 (0–16) | 1.26zł (0.0–6.0) | 5.91 (0.8–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 6.20 Er (1–10) | 4.1% | 26.7% | 0.47 (0–3) | 3.41 (0–17) | 1.28zł (0.0–6.3) | 5.97 (0.8–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_PLUS1` | 6.17 Er (1–10) | 3.5% | 26.5% | 0.47 (0–3) | 3.37 (0–16) | 1.28zł (0.0–6.0) | 5.95 (0.8–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 6.16 Er (1–10) | 3.9% | 26.5% | 0.47 (0–3) | 3.34 (0–16) | 1.27zł (0.0–6.0) | 5.94 (0.8–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 6.39 Er (2–10) | 4.8% | 27.1% | 0.48 (0–3) | 3.57 (0–17) | 1.30zł (0.0–6.3) | 6.08 (0.8–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 5.96 Er (1–10) | 3.0% | 26.0% | 0.46 (0–3) | 3.12 (0–15) | 1.24zł (0.0–6.0) | 5.83 (0.8–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 5.13 Er (1–10) | 1.3% | 23.2% | 0.41 (0–3) | 2.60 (0–16) | 1.17zł (0.0–5.7) | 5.35 (0.8–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.98 Er (1–10) | 3.5% | 26.0% | 0.46 (0–3) | 3.16 (0–16) | 1.21zł (0.0–6.0) | 5.85 (0.8–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.26 Er (1–10) | 5.8% | 26.7% | 0.47 (0–3) | 3.50 (0–17) | 1.32zł (0.0–6.3) | 5.99 (0.8–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 6.25 Er (1–10) | 5.7% | 26.7% | 0.47 (0–3) | 3.49 (0–17) | 1.32zł (0.0–6.3) | 5.99 (0.8–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 5.35 Er (1–10) | 2.2% | 24.7% | 0.42 (0–3) | 2.67 (0–15) | 1.23zł (0.0–6.0) | 5.35 (0.6–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.87 Er (1–10) | 2.4% | 25.7% | 0.46 (0–3) | 3.11 (0–16) | 1.23zł (0.0–6.0) | 5.81 (0.8–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 6.62 Er (1–10) | 5.7% | 27.6% | 0.49 (0–3) | 3.81 (0–17) | 1.34zł (0.0–6.0) | 6.24 (1.8–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.58 Er (1–10) | 1.3% | 21.9% | 0.38 (0–3) | 1.92 (0–15) | 1.23zł (0.0–4.7) | 4.69 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.