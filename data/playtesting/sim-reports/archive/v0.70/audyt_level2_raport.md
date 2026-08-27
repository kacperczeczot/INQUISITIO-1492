[Strona główna](../../../../../README.md) > [v0.70](README.md) > [audyt_level2_raport](audyt_level2_raport.md)

---

# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.70

**Wersja Balansu:** `v0.70` | **Data:** 2026-08-16 20:30 | **Przeanalizowano Wariantów:** 29 | **Próba:** 3000 gier/setup | **Czas:** 467.64s
**Wynik Bazy Poziomu 2 (Global):** `🟠 63.8 pkt` | 3p: `72.9 pkt` | 4p: `69.4 pkt` | 5p: `49.1 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (10)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🟠 ** 63.8** | 72.9 | 69.4 | 49.1 | ⚪ OPTYMALNY |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 5 → 6 | 63.8 → 🟡 ** 77.2** (`⬆️ +13.4`) | 72.9 → 64.2 (`-8.7`) | 69.4 → 87.0 (`⬆️ +17.6`) | 49.1 → 80.5 (`⬆️ +31.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2 → 3 | 63.8 → 🟠 ** 72.4** (`⬆️ +8.6`) | 72.9 → 67.8 (`-5.1`) | 69.4 → 87.9 (`⬆️ +18.5`) | 49.1 → 61.5 (`⬆️ +12.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 6 → 5 | 63.8 → 🟠 ** 69.3** (`⬆️ +5.5`) | 72.9 → 66.2 (`-6.7`) | 69.4 → 72.9 (`⬆️ +3.5`) | 49.1 → 68.9 (`⬆️ +19.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 63.8 → 🟠 ** 67.7** (`⬆️ +3.9`) | 72.9 → 68.7 (`-4.2`) | 69.4 → 74.5 (`⬆️ +5.1`) | 49.1 → 60.0 (`⬆️ +10.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–8 → 3–9 | 63.8 → 🟠 ** 65.1** (`⬆️ +1.3`) | 72.9 → 69.7 (`-3.2`) | 69.4 → 73.5 (`⬆️ +4.1`) | 49.1 → 52.2 (`⬆️ +3.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_CAA_ERA_MINUS1` | Cienie Era: 4 → 3 | 63.8 → 🟠 ** 64.0** (`⬆️ +0.2`) | 72.9 | 69.4 → 69.8 (`⬆️ +0.4`) | 49.1 → 49.4 (`⬆️ +0.3`) | ⚪ OPTYMALNY |
| `L2_KB_ERA_MINUS1` | Korona Era: 4 → 3 | 63.8 → 🟠 ** 63.9** (`⬆️ +0.1`) | 72.9 → 72.0 (`-0.9`) | 69.4 → 69.9 (`⬆️ +0.5`) | 49.1 → 49.9 (`⬆️ +0.8`) | ⚪ OPTYMALNY |
| `L2_KB_ERA_PLUS1` | Korona Era: 4 → 5 | 63.8 → 🟠 ** 60.8** (`-3.0`) | 72.9 → 74.0 (`⬆️ +1.1`) | 69.4 → 65.0 (`-4.4`) | 49.1 → 43.4 (`-5.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 3 → 4 | 63.8 → 🔴 ** 49.6** (`-14.2`) | 72.9 → 75.3 (`⬆️ +2.4`) | 69.4 → 48.6 (`-20.8`) | 49.1 → 25.0 (`-24.1`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 19 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 🟠 ** 63.8** | 72.9 | 69.4 | 49.1 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 🟠 ** 63.8** | 72.9 | 69.4 | 49.1 | ⚪ OPTYMALNY |
| `L2_CAA_ERA_PLUS1` | Cienie Era: 4 → 5 | 63.8 → 🟠 ** 62.7** (`-1.1`) | 72.9 → 71.8 (`-1.1`) | 69.4 → 68.0 (`-1.4`) | 49.1 → 48.3 (`-0.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 4 → 5 | 63.8 → 🔴 ** 59.3** (`-4.5`) | 72.9 → 64.9 (`-8.0`) | 69.4 → 63.9 (`-5.5`) | 49.1 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 4 → 3 | 63.8 → 🔴 ** 57.0** (`-6.8`) | 72.9 → 63.2 (`-9.7`) | 69.4 → 58.8 (`-10.6`) | 49.1 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 3–8 → 3–7 | 63.8 → 🔴 ** 56.4** (`-7.4`) | 72.9 → 66.4 (`-6.5`) | 69.4 → 60.0 (`-9.4`) | 49.1 → 42.9 (`-6.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 6 → 7 | 63.8 → 🔴 ** 48.7** (`-15.1`) | 72.9 → 65.4 (`-7.5`) | 69.4 → 50.5 (`-18.9`) | 49.1 → 30.1 (`-19.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_MINUS1` | Korona Haki: 1 → 0 | 63.8 → 🔴 ** 47.3** (`-16.5`) | 72.9 → 49.9 (`-23.0`) | 69.4 → 51.1 (`-18.3`) | 49.1 → 41.0 (`-8.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 63.8 → 🔴 ** 45.4** (`-18.4`) | 72.9 → 59.2 (`-13.7`) | 69.4 → 47.2 (`-22.2`) | 49.1 → 29.8 (`-19.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 3/4 → 4/5 | 63.8 → 🔴 ** 45.1** (`-18.7`) | 72.9 → 67.3 (`-5.6`) | 69.4 → 43.1 (`-26.3`) | 49.1 → 25.0 (`-24.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 3 → 2 | 63.8 → 🔴 ** 44.4** (`-19.4`) | 72.9 → 61.2 (`-11.7`) | 69.4 → 45.9 (`-23.5`) | 49.1 → 26.1 (`-23.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 5 → 4 | 63.8 → 🔴 ** 43.1** (`-20.7`) | 72.9 → 70.4 (`-2.5`) | 69.4 → 41.8 (`-27.6`) | 49.1 → 17.0 (`-32.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 3/4 → 2/3 | 63.8 → 🔴 ** 37.7** (`-26.1`) | 72.9 → 51.6 (`-21.3`) | 69.4 → 35.3 (`-34.1`) | 49.1 → 26.1 (`-23.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 1 → 2 | 63.8 → 🔴 ** 29.0** (`-34.8`) | 72.9 → 35.8 (`-37.1`) | 69.4 → 30.0 (`-39.4`) | 49.1 → 21.3 (`-27.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 63.8 → 🔴 ** 27.6** (`-36.2`) | 72.9 → 37.6 (`-35.3`) | 69.4 → 27.9 (`-41.5`) | 49.1 → 17.4 (`-31.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 63.8 → 🔴 ** 25.4** (`-38.4`) | 72.9 → 32.9 (`-40.0`) | 69.4 → 25.7 (`-43.7`) | 49.1 → 17.5 (`-31.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 63.8 → 🔴 ** 23.7** (`-40.1`) | 72.9 → 32.6 (`-40.3`) | 69.4 → 23.6 (`-45.8`) | 49.1 → 14.9 (`-34.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2 → 1 | 63.8 → 🔴 ** 17.4** (`-46.4`) | 72.9 → 32.9 (`-40.0`) | 69.4 → 19.2 (`-50.2`) | 49.1 → 0.2 (`-48.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 63.8 → 🔴 ** 14.4** (`-49.4`) | 72.9 → 29.9 (`-43.0`) | 69.4 → 13.2 (`-56.2`) | 49.1 → 0.2 (`-48.9`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (10)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 5.73 Er (1–12) | 0.6% | 24.9% | 1.48 (0–4) | 3.56 (0–21) | 1.62zł (0.0–7.7) | 6.56 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 5.81 Er (1–12) | 0.8% | 25.2% | 1.50 (0–4) | 3.64 (0–21) | 1.63zł (0.0–7.7) | 6.58 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 5.84 Er (1–12) | 0.7% | 25.3% | 1.51 (0–4) | 3.65 (0–21) | 1.64zł (0.0–7.7) | 6.59 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.58 Er (1–12) | 0.6% | 24.3% | 1.42 (0–4) | 3.39 (0–21) | 1.58zł (0.0–7.7) | 6.46 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.65 Er (1–12) | 0.5% | 24.6% | 1.46 (0–4) | 3.47 (0–20) | 1.60zł (0.0–7.7) | 6.53 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 5.68 Er (1–12) | 0.5% | 24.7% | 1.47 (0–4) | 3.50 (0–21) | 1.60zł (0.0–7.7) | 6.55 (0.7–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_MINUS1` | 5.71 Er (1–12) | 0.6% | 24.9% | 1.48 (0–4) | 3.55 (0–21) | 1.63zł (0.0–7.7) | 6.54 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_MINUS1` | 5.69 Er (1–12) | 0.6% | 24.9% | 1.47 (0–4) | 3.53 (0–21) | 1.63zł (0.0–7.7) | 6.53 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_PLUS1` | 5.79 Er (1–12) | 0.6% | 25.1% | 1.49 (0–4) | 3.63 (0–21) | 1.63zł (0.0–7.7) | 6.59 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 5.91 Er (2–12) | 0.7% | 25.4% | 1.53 (0–4) | 3.72 (0–21) | 1.63zł (0.0–7.7) | 6.65 (0.7–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 19 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_HERESY_LOW_MINUS1` | 5.73 Er (1–12) | 0.6% | 24.9% | 1.48 (0–4) | 3.56 (0–21) | 1.62zł (0.0–7.7) | 6.56 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_PLUS1` | 5.73 Er (1–12) | 0.6% | 24.9% | 1.48 (0–4) | 3.56 (0–21) | 1.62zł (0.0–7.7) | 6.56 (0.7–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_PLUS1` | 5.76 Er (1–12) | 0.6% | 25.0% | 1.49 (0–4) | 3.59 (0–21) | 1.62zł (0.0–7.7) | 6.58 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 5.82 Er (1–12) | 0.7% | 25.2% | 1.50 (0–4) | 3.68 (0–21) | 1.63zł (0.0–7.7) | 6.60 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 5.59 Er (1–12) | 0.5% | 24.5% | 1.46 (0–4) | 3.39 (0–21) | 1.60zł (0.0–7.7) | 6.48 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 5.79 Er (1–12) | 0.6% | 25.1% | 1.49 (0–4) | 3.65 (0–21) | 1.64zł (0.0–7.7) | 6.57 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 5.85 Er (1–12) | 0.6% | 25.4% | 1.51 (0–4) | 3.71 (0–21) | 1.65zł (0.0–7.7) | 6.61 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_MINUS1` | 5.49 Er (1–12) | 0.5% | 23.9% | 1.41 (0–4) | 3.28 (0–21) | 1.58zł (0.0–7.7) | 6.44 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 5.87 Er (1–12) | 0.8% | 25.4% | 1.51 (0–5) | 3.74 (0–21) | 1.66zł (0.0–7.7) | 6.62 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 6.00 Er (2–12) | 0.9% | 25.7% | 1.54 (0–4) | 3.84 (0–21) | 1.65zł (0.0–7.7) | 6.69 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 5.41 Er (1–12) | 0.4% | 23.9% | 1.40 (0–4) | 3.29 (0–21) | 1.60zł (0.0–7.7) | 6.37 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.57 Er (1–12) | 0.4% | 24.3% | 1.44 (0–4) | 3.43 (0–21) | 1.59zł (0.0–7.7) | 6.50 (0.7–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 5.28 Er (1–12) | 0.3% | 23.5% | 1.38 (0–4) | 3.13 (0–21) | 1.59zł (0.0–7.7) | 6.29 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 6.04 Er (1–12) | 1.6% | 25.9% | 1.56 (0–4) | 3.95 (0–22) | 1.69zł (0.0–7.7) | 6.68 (0.7–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 6.11 Er (1–12) | 0.8% | 26.1% | 1.59 (0–4) | 3.98 (0–21) | 1.68zł (0.0–7.7) | 6.80 (2.0–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.09 Er (1–12) | 1.8% | 26.0% | 1.58 (0–4) | 4.01 (0–22) | 1.70zł (0.0–7.7) | 6.69 (0.7–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.14 Er (1–12) | 0.4% | 22.4% | 1.31 (0–4) | 2.89 (0–19) | 1.51zł (0.0–7.7) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 4.28 Er (1–12) | 0.2% | 18.8% | 1.05 (0–4) | 2.49 (0–21) | 1.58zł (0.0–7.7) | 5.61 (0.7–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_MINUS1` | 4.26 Er (1–12) | 0.1% | 17.8% | 1.05 (0–4) | 2.04 (0–18) | 1.51zł (0.0–6.0) | 5.41 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.