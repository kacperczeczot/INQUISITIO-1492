[Strona główna](../../../../../README.md) > [v0.42](README.md) > [audyt_level2_raport](audyt_level2_raport.md)

---

# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.42

**Wersja Balansu:** `v0.42` | **Data:** 2026-08-16 00:51 | **Przeanalizowano Wariantów:** 29 | **Próba:** 5000 gier/setup | **Czas:** 234.97s
**Wynik Bazy Poziomu 2 (Global):** `🔴 56.7 pkt` | 3p: `46.3 pkt` | 4p: `67.1 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (12)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🔴 ** 56.7** | 46.3 | 67.1 | 0.0 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_LOW_MINUS1` | Kabała Pasmo: 3–8 → 2–8 | 56.7 → 🔴 ** 59.5** (`⬆️ +2.8`) | 46.3 → 39.0 (`-7.3`) | 67.1 → 80.1 (`⬆️ +13.0`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L2_KB_ERA_MINUS1` | Korona Era: 5/5/5 → 4/4/4 | 56.7 → 🔴 ** 58.9** (`⬆️ +2.2`) | 46.3 → 44.1 (`-2.2`) | 67.1 → 73.7 (`⬆️ +6.6`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L2_CAA_ERA_MINUS1` | Cienie Era: 5 → 4 | 56.7 → 🔴 ** 57.1** (`⬆️ +0.4`) | 46.3 → 46.4 (`⬆️ +0.1`) | 67.1 → 67.8 (`⬆️ +0.7`) | 0.0 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 3–8 → 3–7 | 56.7 → 🔴 ** 56.9** (`⬆️ +0.2`) | 46.3 → 47.8 (`⬆️ +1.5`) | 67.1 → 65.9 (`-1.2`) | 0.0 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 3–8 → 3–9 | 56.7 → 🔴 ** 56.6** (`-0.1`) | 46.3 → 45.6 (`-0.7`) | 67.1 → 67.6 (`⬆️ +0.5`) | 0.0 | ⚪ OPTYMALNY |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 4/4/4 → 3/3/3 | 56.7 → 🔴 ** 49.7** (`-7.0`) | 46.3 → 81.2 (`⬆️ +34.9`) | 67.1 → 18.1 (`-49.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 6/6/6 → 7/7/7 | 56.7 → 🔴 ** 43.5** (`-13.2`) | 46.3 → 59.1 (`⬆️ +12.8`) | 67.1 → 27.9 (`-39.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 3–8 → 4–8 | 56.7 → 🔴 ** 41.9** (`-14.8`) | 46.3 → 50.4 (`⬆️ +4.1`) | 67.1 → 33.4 (`-33.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 6/6/6 → 5/5/5 | 56.7 → 🔴 ** 38.1** (`-18.6`) | 46.3 → 31.3 (`-15.0`) | 67.1 → 64.5 (`-2.6`) | 0.0 → 18.4 (`⬆️ +18.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_ERA_PLUS1` | Korona Era: 5/5/5 → 6/6/6 | 56.7 → 🔴 ** 37.0** (`-19.7`) | 46.3 → 52.6 (`⬆️ +6.3`) | 67.1 → 21.5 (`-45.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 56.7 → 🔴 ** 33.7** (`-23.0`) | 46.3 → 52.8 (`⬆️ +6.5`) | 67.1 → 14.6 (`-52.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 17 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_PLUS1` | Cienie Era: 5 → 6 | 56.7 → 🔴 ** 56.3** (`-0.4`) | 46.3 → 46.2 (`-0.1`) | 67.1 → 66.4 (`-0.7`) | 0.0 | ⚪ OPTYMALNY |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 3 → 4 | 56.7 → 🔴 ** 45.0** (`-11.7`) | 46.3 → 24.2 (`-22.1`) | 67.1 → 65.7 (`-1.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 56.7 → 🔴 ** 44.7** (`-12.0`) | 46.3 → 23.9 (`-22.4`) | 67.1 → 65.4 (`-1.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 3 → 2 | 56.7 → 🔴 ** 42.8** (`-13.9`) | 46.3 → 36.6 (`-9.7`) | 67.1 → 49.0 (`-18.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2 → 3 | 56.7 → 🔴 ** 42.3** (`-14.4`) | 46.3 → 32.3 (`-14.0`) | 67.1 → 52.3 (`-14.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 2 → 3 | 56.7 → 🔴 ** 37.5** (`-19.2`) | 46.3 → 39.3 (`-7.0`) | 67.1 → 35.7 (`-31.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 4/4/4 → 5/5/5 | 56.7 → 🔴 ** 35.1** (`-21.6`) | 46.3 → 32.0 (`-14.3`) | 67.1 → 38.2 (`-28.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 2 → 1 | 56.7 → 🔴 ** 34.3** (`-22.4`) | 46.3 → 32.9 (`-13.4`) | 67.1 → 35.7 (`-31.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 2/3 → 3/4 | 56.7 → 🔴 ** 25.8** (`-30.9`) | 46.3 → 17.2 (`-29.1`) | 67.1 → 34.3 (`-32.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2 → 1 | 56.7 → 🔴 ** 25.1** (`-31.6`) | 46.3 → 32.0 (`-14.3`) | 67.1 → 18.1 (`-49.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 2/3 → 1/2 | 56.7 → 🔴 ** 20.4** (`-36.3`) | 46.3 → 23.2 (`-23.1`) | 67.1 → 17.6 (`-49.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 56.7 → 🔴 ** 13.4** (`-43.3`) | 46.3 → 13.6 (`-32.7`) | 67.1 → 13.2 (`-53.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 56.7 → 🔴 ** 13.4** (`-43.3`) | 46.3 → 13.6 (`-32.7`) | 67.1 → 13.2 (`-53.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_MINUS1` | Korona Haki: 1 → 0 | 56.7 → 🔴 **  9.9** (`-46.8`) | 46.3 → 13.1 (`-33.2`) | 67.1 → 6.7 (`-60.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 56.7 → 🔴 **  8.3** (`-48.4`) | 46.3 → 13.1 (`-33.2`) | 67.1 → 3.6 (`-63.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 56.7 → 🔴 **  8.3** (`-48.4`) | 46.3 → 13.1 (`-33.2`) | 67.1 → 3.6 (`-63.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 1 → 2 | 56.7 → 🔴 **  8.3** (`-48.4`) | 46.3 → 13.1 (`-33.2`) | 67.1 → 3.6 (`-63.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (12)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 5.65 Er (1–11) | 1.0% | 25.3% | 0.57 (0–3) | 3.51 (0–19) | 1.51zł (0.0–7.7) | 6.05 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_MINUS1` | 5.62 Er (1–11) | 1.0% | 25.2% | 0.56 (0–3) | 3.46 (0–19) | 1.50zł (0.0–7.7) | 6.03 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_MINUS1` | 5.60 Er (1–11) | 1.0% | 25.1% | 0.56 (0–3) | 3.45 (0–19) | 1.51zł (0.0–7.7) | 6.01 (1.0–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_MINUS1` | 5.63 Er (1–11) | 1.0% | 25.3% | 0.57 (0–3) | 3.50 (0–19) | 1.51zł (0.0–7.7) | 6.04 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 5.66 Er (1–11) | 1.1% | 25.4% | 0.57 (0–3) | 3.52 (0–19) | 1.52zł (0.0–7.7) | 6.05 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 5.64 Er (1–11) | 1.0% | 25.3% | 0.57 (0–3) | 3.50 (0–19) | 1.51zł (0.0–7.7) | 6.04 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.51 Er (1–11) | 0.8% | 24.8% | 0.56 (0–3) | 3.36 (0–19) | 1.49zł (0.0–7.7) | 5.98 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 5.77 Er (1–11) | 1.1% | 25.8% | 0.57 (0–3) | 3.65 (0–19) | 1.57zł (0.0–7.7) | 6.11 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_LOW_PLUS1` | 5.71 Er (1–11) | 1.1% | 25.5% | 0.57 (0–3) | 3.59 (0–23) | 1.54zł (0.0–7.7) | 6.08 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.54 Er (1–11) | 1.0% | 24.8% | 0.56 (0–3) | 3.36 (0–19) | 1.49zł (0.0–7.7) | 5.97 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_ERA_PLUS1` | 5.72 Er (1–11) | 1.0% | 25.6% | 0.57 (0–3) | 3.60 (0–19) | 1.53zł (0.0–7.7) | 6.08 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 5.87 Er (1–11) | 2.2% | 26.1% | 0.58 (0–3) | 3.78 (0–19) | 1.60zł (0.0–7.7) | 6.15 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 17 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_PLUS1` | 5.67 Er (1–11) | 1.0% | 25.4% | 0.57 (0–3) | 3.52 (0–19) | 1.52zł (0.0–7.7) | 6.06 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 5.73 Er (1–11) | 1.2% | 25.6% | 0.57 (0–3) | 3.61 (0–20) | 1.53zł (0.0–7.7) | 6.09 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.51 Er (1–11) | 0.7% | 24.7% | 0.56 (0–3) | 3.34 (0–17) | 1.48zł (0.0–7.0) | 5.97 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 5.51 Er (1–11) | 0.9% | 24.8% | 0.56 (0–3) | 3.34 (0–19) | 1.50zł (0.0–7.7) | 5.95 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 5.69 Er (1–11) | 1.3% | 25.4% | 0.57 (0–3) | 3.54 (0–19) | 1.52zł (0.0–7.7) | 6.06 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 5.82 Er (1–11) | 1.2% | 25.8% | 0.58 (0–3) | 3.70 (0–19) | 1.53zł (0.0–7.7) | 6.16 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 5.72 Er (1–11) | 1.2% | 25.6% | 0.57 (0–3) | 3.59 (0–19) | 1.53zł (0.0–7.7) | 6.08 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 5.14 Er (1–11) | 0.8% | 24.1% | 0.54 (0–3) | 3.05 (0–19) | 1.52zł (0.0–7.7) | 5.64 (0.4–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 5.91 Er (1–11) | 1.4% | 26.1% | 0.58 (0–3) | 3.80 (0–20) | 1.54zł (0.0–7.7) | 6.21 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 4.86 Er (1–11) | 0.3% | 22.3% | 0.51 (0–3) | 2.85 (0–19) | 1.45zł (0.0–7.7) | 5.57 (1.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_GC_FALLS_MINUS1` | 5.00 Er (1–11) | 0.6% | 23.6% | 0.53 (0–3) | 2.88 (0–19) | 1.50zł (0.0–7.7) | 5.55 (0.4–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 6.05 Er (1–11) | 1.7% | 26.5% | 0.59 (0–3) | 3.92 (0–19) | 1.56zł (0.0–8.0) | 6.30 (1.5–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.54 Er (1–11) | 0.3% | 21.3% | 0.51 (0–3) | 2.33 (0–16) | 1.46zł (0.0–6.3) | 5.17 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_KB_HOOKS_MINUS1` | 5.44 Er (1–11) | 0.8% | 24.5% | 0.56 (0–3) | 3.23 (0–19) | 1.47zł (0.0–7.7) | 5.94 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 5.92 Er (1–11) | 3.0% | 26.1% | 0.58 (0–3) | 3.88 (0–20) | 1.59zł (0.0–7.7) | 6.17 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.34 Er (1–11) | 0.8% | 24.1% | 0.55 (0–3) | 3.12 (0–19) | 1.46zł (0.0–7.7) | 5.85 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 5.90 Er (1–11) | 3.0% | 26.0% | 0.58 (0–3) | 3.85 (0–19) | 1.58zł (0.0–7.7) | 6.16 (1.0–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.