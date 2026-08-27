[Strona główna](../../../../../README.md) > [v0.40](README.md) > [audyt_level2_raport](audyt_level2_raport.md)

---

# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.40

**Wersja Balansu:** `v0.40` | **Data:** 2026-08-15 23:43 | **Przeanalizowano Wariantów:** 29 | **Próba:** 5000 gier/setup | **Czas:** 586.26s
**Wynik Bazy Poziomu 2 (Global):** `🔴 30.4 pkt` | 3p: `44.3 pkt` | 4p: `16.6 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (10)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🔴 ** 30.4** | 44.3 | 16.6 | 0.0 | ⚪ OPTYMALNY |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 30.4 → 🔴 ** 57.4** (`⬆️ +27.0`) | 44.3 → 53.6 (`⬆️ +9.3`) | 16.6 → 47.4 (`⬆️ +30.8`) | 0.0 → 71.2 (`⬆️ +71.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 7/6/6 → 8/7/7 | 30.4 → 🔴 ** 48.4** (`⬆️ +18.0`) | 44.3 → 75.9 (`⬆️ +31.6`) | 16.6 → 20.8 (`⬆️ +4.2`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 30.4 → 🔴 ** 45.2** (`⬆️ +14.8`) | 44.3 → 75.4 (`⬆️ +31.1`) | 16.6 → 15.0 (`-1.6`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L2_KB_HOOKS_MINUS1` | Korona Haki: 1 → 0 | 30.4 → 🔴 ** 41.5** (`⬆️ +11.1`) | 44.3 → 26.8 (`-17.5`) | 16.6 → 16.3 (`-0.3`) | 0.0 → 81.4 (`⬆️ +81.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 30.4 → 🔴 ** 37.9** (`⬆️ +7.5`) | 44.3 → 56.0 (`⬆️ +11.7`) | 16.6 → 19.7 (`⬆️ +3.1`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 3–8 → 3–7 | 30.4 → 🔴 ** 37.0** (`⬆️ +6.6`) | 44.3 → 55.2 (`⬆️ +10.9`) | 16.6 → 18.8 (`⬆️ +2.2`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 3/4/4 → 4/5/5 | 30.4 → 🔴 ** 36.0** (`⬆️ +5.6`) | 44.3 → 36.0 (`-8.3`) | 16.6 → 0.0 (`-16.6`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L2_KB_ERA_MINUS1` | Korona Era: 6/5/5 → 5/4/4 | 30.4 → 🔴 ** 34.2** (`⬆️ +3.8`) | 44.3 → 50.6 (`⬆️ +6.3`) | 16.6 → 17.9 (`⬆️ +1.3`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L2_CAA_ERA_PLUS1` | Cienie Era: 5 → 6 | 30.4 → 🔴 ** 30.8** (`⬆️ +0.4`) | 44.3 → 44.4 (`⬆️ +0.1`) | 16.6 → 17.1 (`⬆️ +0.5`) | 0.0 | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 19 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_MINUS1` | Cienie Era: 5 → 4 | 🔴 ** 30.4** | 44.3 → 44.2 (`-0.1`) | 16.6 → 16.5 (`-0.1`) | 0.0 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–8 → 3–9 | 30.4 → 🔴 ** 29.8** (`-0.6`) | 44.3 → 43.6 (`-0.7`) | 16.6 → 15.9 (`-0.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 30.4 → 🔴 ** 28.9** (`-1.5`) | 44.3 → 43.3 (`-1.0`) | 16.6 → 14.5 (`-2.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_PLUS1` | Korona Era: 6/5/5 → 7/6/6 | 30.4 → 🔴 ** 26.8** (`-3.6`) | 44.3 → 38.3 (`-6.0`) | 16.6 → 15.2 (`-1.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 2 → 3 | 30.4 → 🔴 ** 26.7** (`-3.7`) | 44.3 → 26.7 (`-17.6`) | 16.6 → 0.0 (`-16.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 2 → 1 | 30.4 → 🔴 ** 26.7** (`-3.7`) | 44.3 → 26.7 (`-17.6`) | 16.6 → 0.0 (`-16.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2 → 3 | 30.4 → 🔴 ** 26.3** (`-4.1`) | 44.3 → 43.9 (`-0.4`) | 16.6 → 8.7 (`-7.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 3 → 4 | 30.4 → 🔴 ** 24.7** (`-5.7`) | 44.3 → 32.7 (`-11.6`) | 16.6 | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 3/4/4 → 2/3/3 | 30.4 → 🔴 ** 21.6** (`-8.8`) | 44.3 → 27.7 (`-16.6`) | 16.6 → 15.6 (`-1.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 3 → 2 | 30.4 → 🔴 ** 21.2** (`-9.2`) | 44.3 → 25.9 (`-18.4`) | 16.6 | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 30.4 → 🔴 ** 20.6** (`-9.8`) | 44.3 → 39.9 (`-4.4`) | 16.6 → 1.3 (`-15.3`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2 → 1 | 30.4 → 🔴 ** 19.5** (`-10.9`) | 44.3 → 19.5 (`-24.8`) | 16.6 → 0.0 (`-16.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 7/6/6 → 6/5/5 | 30.4 → 🔴 ** 18.2** (`-12.2`) | 44.3 → 33.7 (`-10.6`) | 16.6 → 2.8 (`-13.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 30.4 → 🔴 ** 17.2** (`-13.2`) | 44.3 → 19.2 (`-25.1`) | 16.6 → 15.2 (`-1.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 1 → 2 | 30.4 → 🔴 ** 17.2** (`-13.2`) | 44.3 → 19.2 (`-25.1`) | 16.6 → 15.2 (`-1.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 2/3 → 3/4 | 30.4 → 🔴 ** 15.1** (`-15.3`) | 44.3 → 15.1 (`-29.2`) | 16.6 → 0.0 (`-16.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 2/3 → 1/2 | 30.4 → 🔴 **  8.4** (`-22.0`) | 44.3 → 8.4 (`-35.9`) | 16.6 → 0.0 (`-16.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 30.4 → 🔴 **  8.0** (`-22.4`) | 44.3 → 8.0 (`-36.3`) | 16.6 → 0.0 (`-16.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 30.4 → 🔴 **  8.0** (`-22.4`) | 44.3 → 8.0 (`-36.3`) | 16.6 → 0.0 (`-16.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (10)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 6.24 Er (1–10) | 3.9% | 26.6% | 0.45 (0–3) | 3.23 (0–18) | 1.24zł (0.0–7.0) | 5.88 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 6.01 Er (1–10) | 2.8% | 26.0% | 0.44 (0–3) | 2.96 (0–18) | 1.19zł (0.0–7.0) | 5.74 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 6.41 Er (1–10) | 4.1% | 27.1% | 0.46 (0–3) | 3.42 (0–18) | 1.31zł (0.0–7.0) | 5.96 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 6.47 Er (1–10) | 7.5% | 27.3% | 0.46 (0–3) | 3.51 (0–19) | 1.33zł (0.0–7.0) | 5.98 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_MINUS1` | 6.00 Er (1–10) | 2.6% | 25.9% | 0.44 (0–3) | 2.94 (0–18) | 1.18zł (0.0–7.0) | 5.76 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_PLUS1` | 6.30 Er (1–10) | 4.2% | 26.8% | 0.46 (0–3) | 3.30 (0–18) | 1.26zł (0.0–7.0) | 5.91 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 6.26 Er (1–10) | 4.3% | 26.7% | 0.45 (0–3) | 3.26 (0–18) | 1.25zł (0.0–7.0) | 5.88 (0.0–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 6.33 Er (1–10) | 4.7% | 26.9% | 0.46 (0–3) | 3.30 (0–18) | 1.26zł (0.0–7.0) | 5.91 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_MINUS1` | 6.22 Er (1–10) | 3.9% | 26.6% | 0.45 (0–3) | 3.20 (0–18) | 1.24zł (0.0–7.0) | 5.86 (0.0–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_PLUS1` | 6.27 Er (1–10) | 3.9% | 26.7% | 0.46 (0–3) | 3.25 (0–18) | 1.24zł (0.0–7.0) | 5.90 (0.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 19 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_MINUS1` | 6.23 Er (1–10) | 3.9% | 26.6% | 0.45 (0–3) | 3.23 (0–18) | 1.24zł (0.0–7.0) | 5.87 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 6.23 Er (1–10) | 3.8% | 26.6% | 0.45 (0–3) | 3.22 (0–18) | 1.24zł (0.0–7.0) | 5.88 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_MINUS1` | 6.21 Er (1–10) | 3.9% | 26.5% | 0.45 (0–3) | 3.20 (0–18) | 1.23zł (0.0–7.0) | 5.86 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_PLUS1` | 6.29 Er (1–10) | 3.9% | 26.7% | 0.46 (0–3) | 3.29 (0–18) | 1.25zł (0.0–7.0) | 5.90 (0.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 6.43 Er (2–10) | 4.7% | 27.1% | 0.47 (0–3) | 3.39 (0–18) | 1.26zł (0.0–7.0) | 5.99 (0.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 5.61 Er (1–10) | 2.9% | 25.3% | 0.40 (0–3) | 2.79 (0–18) | 1.22zł (0.0–7.0) | 5.38 (0.0–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 6.28 Er (1–10) | 4.3% | 26.7% | 0.46 (0–3) | 3.26 (0–18) | 1.25zł (0.0–7.0) | 5.89 (0.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 6.33 Er (1–10) | 4.5% | 26.9% | 0.46 (0–3) | 3.34 (0–18) | 1.26zł (0.0–7.0) | 5.92 (0.0–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 6.01 Er (1–10) | 2.7% | 26.0% | 0.44 (0–3) | 3.05 (0–18) | 1.20zł (0.0–7.0) | 5.77 (0.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 6.09 Er (1–10) | 3.4% | 26.2% | 0.45 (0–3) | 3.05 (0–18) | 1.21zł (0.0–6.7) | 5.78 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 6.11 Er (1–10) | 3.0% | 26.2% | 0.45 (0–3) | 3.08 (0–16) | 1.20zł (0.0–6.0) | 5.81 (0.0–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 5.26 Er (1–10) | 1.4% | 23.5% | 0.40 (0–3) | 2.54 (0–18) | 1.13zł (0.0–7.0) | 5.30 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 6.11 Er (1–10) | 3.9% | 26.2% | 0.45 (0–3) | 3.09 (0–18) | 1.19zł (0.0–7.0) | 5.79 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.38 Er (1–10) | 6.3% | 26.9% | 0.46 (0–3) | 3.41 (0–18) | 1.29zł (0.0–7.0) | 5.94 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 6.37 Er (1–10) | 6.2% | 26.9% | 0.46 (0–3) | 3.41 (0–18) | 1.29zł (0.0–7.0) | 5.94 (0.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 6.52 Er (2–10) | 5.2% | 27.3% | 0.47 (0–3) | 3.49 (0–18) | 1.28zł (0.0–7.0) | 6.04 (0.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 5.46 Er (1–10) | 2.4% | 24.9% | 0.40 (0–3) | 2.61 (0–18) | 1.20zł (0.0–6.7) | 5.28 (0.0–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 6.73 Er (1–10) | 6.2% | 27.8% | 0.48 (0–3) | 3.70 (0–20) | 1.31zł (0.0–7.0) | 6.19 (1.2–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.87 Er (1–10) | 1.6% | 22.3% | 0.38 (0–3) | 1.95 (0–16) | 1.15zł (0.0–6.7) | 4.79 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.