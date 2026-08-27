[Strona główna](../../../../../README.md) > [v0.75](README.md) > [audyt_level2_raport](audyt_level2_raport.md)

---

# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.75

**Wersja Balansu:** `v0.75` | **Data:** 2026-08-17 00:02 | **Przeanalizowano Wariantów:** 29 | **Próba:** 3000 gier/setup | **Czas:** 465.56s
**Wynik Bazy Poziomu 2 (Global):** `🔴 35.5 pkt` | 3p: `34.1 pkt` | 4p: `34.3 pkt` | 5p: `38.1 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (11)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🔴 ** 35.5** | 34.1 | 34.3 | 38.1 | ⚪ OPTYMALNY |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 5 → 4 | 35.5 → 🔴 ** 46.4** (`⬆️ +10.9`) | 34.1 → 41.7 (`⬆️ +7.6`) | 34.3 → 48.6 (`⬆️ +14.3`) | 38.1 → 48.9 (`⬆️ +10.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 3 → 2 | 35.5 → 🔴 ** 39.9** (`⬆️ +4.4`) | 34.1 → 36.6 (`⬆️ +2.5`) | 34.3 → 40.9 (`⬆️ +6.6`) | 38.1 → 42.1 (`⬆️ +4.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KB_HOOKS_MINUS1` | Korona Haki: 1 → 0 | 35.5 → 🔴 ** 36.8** (`⬆️ +1.3`) | 34.1 → 34.4 (`⬆️ +0.3`) | 34.3 → 35.7 (`⬆️ +1.4`) | 38.1 → 40.4 (`⬆️ +2.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 3 → 4 | 35.5 → 🔴 ** 36.3** (`⬆️ +0.8`) | 34.1 → 38.1 (`⬆️ +4.0`) | 34.3 → 34.9 (`⬆️ +0.6`) | 38.1 → 35.8 (`-2.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 3/4 → 4/5 | 35.5 → 🔴 ** 36.3** (`⬆️ +0.8`) | 34.1 → 37.5 (`⬆️ +3.4`) | 34.3 → 35.7 (`⬆️ +1.4`) | 38.1 → 35.8 (`-2.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KB_ERA_MINUS1` | Korona Era: 4 → 3 | 35.5 → 🔴 ** 36.3** (`⬆️ +0.8`) | 34.1 → 34.4 (`⬆️ +0.3`) | 34.3 → 35.0 (`⬆️ +0.7`) | 38.1 → 39.6 (`⬆️ +1.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 3–8 → 3–7 | 35.5 → 🔴 ** 36.2** (`⬆️ +0.7`) | 34.1 → 34.8 (`⬆️ +0.7`) | 34.3 → 35.4 (`⬆️ +1.1`) | 38.1 → 38.3 (`⬆️ +0.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_CAA_ERA_PLUS1` | Cienie Era: 4 → 5 | 35.5 → 🔴 ** 36.0** (`⬆️ +0.5`) | 34.1 → 34.0 (`-0.1`) | 34.3 → 34.6 (`⬆️ +0.3`) | 38.1 → 39.3 (`⬆️ +1.2`) | ⚪ OPTYMALNY |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 4 → 5 | 35.5 → 🔴 ** 35.6** (`⬆️ +0.1`) | 34.1 → 33.5 (`-0.6`) | 34.3 → 35.1 (`⬆️ +0.8`) | 38.1 | ⚪ OPTYMALNY |
| `L2_CAA_ERA_MINUS1` | Cienie Era: 4 → 3 | 🔴 ** 35.5** | 34.1 → 34.2 (`⬆️ +0.1`) | 34.3 | 38.1 → 37.9 (`-0.2`) | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 18 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 3 → 4 | 🔴 ** 35.5** | 34.1 | 34.3 | 38.1 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 🔴 ** 35.5** | 34.1 | 34.3 | 38.1 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 🔴 ** 35.5** | 34.1 | 34.3 | 38.1 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–8 → 3–9 | 35.5 → 🔴 ** 34.9** (`-0.6`) | 34.1 → 33.5 (`-0.6`) | 34.3 → 33.3 (`-1.0`) | 38.1 → 38.0 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_PLUS1` | Korona Era: 4 → 5 | 35.5 → 🔴 ** 34.4** (`-1.1`) | 34.1 → 33.7 (`-0.4`) | 34.3 → 32.9 (`-1.4`) | 38.1 → 36.5 (`-1.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 6 → 5 | 35.5 → 🔴 ** 34.3** (`-1.2`) | 34.1 → 33.7 (`-0.4`) | 34.3 → 32.8 (`-1.5`) | 38.1 → 36.3 (`-1.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 6 → 7 | 35.5 → 🔴 ** 32.9** (`-2.6`) | 34.1 → 33.9 (`-0.2`) | 34.3 → 33.4 (`-0.9`) | 38.1 → 31.4 (`-6.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 35.5 → 🔴 ** 32.6** (`-2.9`) | 34.1 → 33.5 (`-0.6`) | 34.3 → 33.1 (`-1.2`) | 38.1 → 31.3 (`-6.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 35.5 → 🔴 ** 32.4** (`-3.1`) | 34.1 → 31.1 (`-3.0`) | 34.3 → 30.4 (`-3.9`) | 38.1 → 35.8 (`-2.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 4 → 3 | 35.5 → 🔴 ** 31.6** (`-3.9`) | 34.1 → 26.8 (`-7.3`) | 34.3 → 29.8 (`-4.5`) | 38.1 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 5 → 6 | 35.5 → 🔴 ** 29.2** (`-6.3`) | 34.1 → 30.6 (`-3.5`) | 34.3 → 28.3 (`-6.0`) | 38.1 → 28.6 (`-9.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 1 → 2 | 35.5 → 🔴 ** 25.8** (`-9.7`) | 34.1 → 27.0 (`-7.1`) | 34.3 → 24.6 (`-9.7`) | 38.1 → 25.9 (`-12.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 3 → 2 | 35.5 → 🔴 ** 22.2** (`-13.3`) | 34.1 → 30.1 (`-4.0`) | 34.3 → 21.8 (`-12.5`) | 38.1 → 14.7 (`-23.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 35.5 → 🔴 ** 20.4** (`-15.1`) | 34.1 → 22.7 (`-11.4`) | 34.3 → 19.4 (`-14.9`) | 38.1 → 19.0 (`-19.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 3/4 → 2/3 | 35.5 → 🔴 ** 18.2** (`-17.3`) | 34.1 → 22.7 (`-11.4`) | 34.3 → 17.3 (`-17.0`) | 38.1 → 14.7 (`-23.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 35.5 → 🔴 ** 15.9** (`-19.6`) | 34.1 → 12.2 (`-21.9`) | 34.3 → 15.5 (`-18.8`) | 38.1 → 20.1 (`-18.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 35.5 → 🔴 ** 10.3** (`-25.2`) | 34.1 → 19.7 (`-14.4`) | 34.3 → 9.4 (`-24.9`) | 38.1 → 1.9 (`-36.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 35.5 → 🔴 **  4.6** (`-30.9`) | 34.1 → 8.5 (`-25.6`) | 34.3 → 5.3 (`-29.0`) | 38.1 → 0.1 (`-38.0`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (11)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 6.10 Er (1–12) | 4.5% | 6.5% | 1.44 (0–4) | 3.08 (0–21) | 2.19zł (0.0–8.3) | 5.79 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.99 Er (1–12) | 3.4% | 6.5% | 1.41 (0–4) | 2.98 (0–21) | 2.15zł (0.0–8.3) | 5.76 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 6.03 Er (1–12) | 3.9% | 6.5% | 1.42 (0–4) | 3.02 (0–21) | 2.17zł (0.0–8.3) | 5.77 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_MINUS1` | 6.08 Er (1–12) | 4.5% | 6.5% | 1.43 (0–4) | 3.06 (0–21) | 2.19zł (0.0–8.3) | 5.77 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 6.37 Er (1–12) | 5.6% | 6.5% | 1.49 (0–4) | 3.31 (0–21) | 2.24zł (0.0–8.3) | 5.91 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 6.49 Er (1–12) | 6.2% | 6.5% | 1.51 (0–4) | 3.46 (0–23) | 2.27zł (0.0–8.3) | 5.96 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_MINUS1` | 6.08 Er (1–12) | 4.5% | 6.5% | 1.44 (0–4) | 3.06 (0–21) | 2.19zł (0.0–8.3) | 5.78 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 6.17 Er (1–12) | 4.8% | 6.5% | 1.45 (0–4) | 3.16 (0–21) | 2.21zł (0.0–8.3) | 5.79 (0.7–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_PLUS1` | 6.13 Er (1–12) | 4.5% | 6.5% | 1.44 (0–4) | 3.10 (0–21) | 2.20zł (0.0–8.3) | 5.81 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 6.22 Er (1–12) | 5.1% | 6.5% | 1.46 (0–4) | 3.23 (0–23) | 2.21zł (0.0–8.3) | 5.84 (0.7–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_MINUS1` | 6.08 Er (1–12) | 4.5% | 6.5% | 1.43 (0–4) | 3.07 (0–21) | 2.18zł (0.0–8.3) | 5.77 (0.7–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 18 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_SO_CONDEMNS_PLUS1` | 6.10 Er (1–12) | 4.5% | 6.5% | 1.44 (0–4) | 3.08 (0–21) | 2.19zł (0.0–8.3) | 5.79 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_MINUS1` | 6.10 Er (1–12) | 4.5% | 6.5% | 1.44 (0–4) | 3.08 (0–21) | 2.19zł (0.0–8.3) | 5.79 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_PLUS1` | 6.10 Er (1–12) | 4.5% | 6.5% | 1.44 (0–4) | 3.08 (0–21) | 2.19zł (0.0–8.3) | 5.79 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 6.06 Er (1–12) | 4.3% | 6.5% | 1.43 (0–4) | 3.03 (0–21) | 2.17zł (0.0–8.3) | 5.79 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_PLUS1` | 6.13 Er (1–12) | 4.5% | 6.5% | 1.44 (0–4) | 3.11 (0–21) | 2.19zł (0.0–8.3) | 5.80 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.97 Er (1–12) | 4.5% | 6.5% | 1.37 (0–4) | 2.94 (0–21) | 2.15zł (0.0–8.3) | 5.69 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 6.25 Er (1–12) | 4.7% | 6.5% | 1.47 (0–4) | 3.24 (0–21) | 2.22zł (0.0–8.3) | 5.83 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 6.38 Er (1–12) | 5.7% | 6.5% | 1.50 (0–4) | 3.40 (0–21) | 2.26zł (0.0–8.3) | 5.91 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.93 Er (1–12) | 4.1% | 6.5% | 1.40 (0–4) | 2.88 (0–21) | 2.16zł (0.0–8.3) | 5.73 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 5.94 Er (1–12) | 4.1% | 6.5% | 1.41 (0–4) | 2.88 (0–21) | 2.16zł (0.0–8.3) | 5.70 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 6.16 Er (1–12) | 5.6% | 6.5% | 1.45 (0–4) | 3.14 (0–21) | 2.21zł (0.0–8.3) | 5.80 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 6.24 Er (1–12) | 5.1% | 6.5% | 1.47 (0–4) | 3.23 (0–21) | 2.22zł (0.0–8.3) | 5.85 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 5.71 Er (1–12) | 3.6% | 6.5% | 1.35 (0–4) | 2.75 (0–21) | 2.12zł (0.0–8.3) | 5.56 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.34 Er (1–12) | 6.3% | 6.5% | 1.50 (0–4) | 3.36 (0–22) | 2.25zł (0.0–8.3) | 5.89 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 5.55 Er (1–12) | 3.2% | 6.5% | 1.33 (0–4) | 2.55 (0–21) | 2.09zł (0.0–8.3) | 5.47 (0.7–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 6.86 Er (1–12) | 6.5% | 6.5% | 1.65 (0–4) | 3.76 (0–23) | 2.33zł (0.0–8.3) | 6.28 (2.0–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 4.71 Er (1–12) | 1.2% | 6.5% | 1.09 (0–4) | 1.69 (0–18) | 1.92zł (0.0–8.3) | 4.97 (0.7–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_MINUS1` | 4.43 Er (1–12) | 1.7% | 6.4% | 0.99 (0–4) | 1.57 (0–20) | 1.88zł (0.0–8.0) | 4.60 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.