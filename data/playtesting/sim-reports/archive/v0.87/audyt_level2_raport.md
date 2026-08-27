[Strona główna](../../../../../README.md) > [v0.87](README.md) > [audyt_level2_raport](audyt_level2_raport.md)

---

# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v0.87

**Wersja Balansu:** `v0.87` | **Data:** 2026-08-17 13:18 | **Przeanalizowano Wariantów:** 29 | **Próba:** 250 gier/setup | **Czas:** 17.49s
**Wynik Bazy Poziomu 2 (Global):** `🔴 26.8 pkt` | 3p: `24.4 pkt` | 4p: `34.9 pkt` | 5p: `21.2 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (12)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🔴 ** 26.8** | 24.4 | 34.9 | 21.2 | ⚪ OPTYMALNY |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 3 → 2 | 26.8 → 🔴 ** 52.3** (`⬆️ +25.5`) | 24.4 → 45.6 (`⬆️ +21.2`) | 34.9 → 63.3 (`⬆️ +28.4`) | 21.2 → 48.1 (`⬆️ +26.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_KT_ERA_MINUS1` | Kabała Era: 6 → 5 | 26.8 → 🔴 ** 28.1** (`⬆️ +1.3`) | 24.4 → 23.5 (`-0.9`) | 34.9 → 34.1 (`-0.8`) | 21.2 → 26.8 (`⬆️ +5.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | Gildia Upadki (bez Oficjum): 5 → 4 | 26.8 → 🔴 ** 27.6** (`⬆️ +0.8`) | 24.4 → 27.6 (`⬆️ +3.2`) | 34.9 → 34.0 (`-0.9`) | 21.2 | 🟢 POPRAWIA GLOBALNIE |
| `L2_KB_HOOKS_PLUS1` | Korona Haki: 0 → 1 | 26.8 → 🔴 ** 27.1** (`⬆️ +0.3`) | 24.4 → 24.6 (`⬆️ +0.2`) | 34.9 → 35.6 (`⬆️ +0.7`) | 21.2 → 21.1 (`-0.1`) | ⚪ OPTYMALNY |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 3 → 4 | 26.8 → 🔴 ** 26.9** (`⬆️ +0.1`) | 24.4 | 34.9 → 35.1 (`⬆️ +0.2`) | 21.2 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_PLUS1` | Kabała Pasmo: 0–9 → 0–10 | 🔴 ** 26.8** | 24.4 → 23.4 (`-1.0`) | 34.9 → 34.0 (`-0.9`) | 21.2 → 22.9 (`⬆️ +1.7`) | ⚪ OPTYMALNY |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 5 → 6 | 26.8 → 🔴 ** 25.8** (`-1.0`) | 24.4 → 20.9 (`-3.5`) | 34.9 → 37.6 (`⬆️ +2.7`) | 21.2 → 18.8 (`-2.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 6 → 7 | 26.8 → 🔴 ** 24.8** (`-2.0`) | 24.4 → 25.9 (`⬆️ +1.5`) | 34.9 → 33.0 (`-1.9`) | 21.2 → 15.5 (`-5.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 3 → 2 | 26.8 → 🔴 ** 20.8** (`-6.0`) | 24.4 → 18.9 (`-5.5`) | 34.9 → 21.3 (`-13.6`) | 21.2 → 22.2 (`⬆️ +1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 5 → 4 | 26.8 → 🔴 ** 19.1** (`-7.7`) | 24.4 → 27.0 (`⬆️ +2.6`) | 34.9 → 24.7 (`-10.2`) | 21.2 → 5.5 (`-15.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (default/bez SO): 3/5 → 2/4 | 26.8 → 🔴 ** 18.3** (`-8.5`) | 24.4 → 25.2 (`⬆️ +0.8`) | 34.9 → 21.9 (`-13.0`) | 21.2 → 7.7 (`-13.5`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 17 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_HERESY_LOW_PLUS1` | Kabała Pasmo: 0–9 → 1–9 | 🔴 ** 26.8** | 24.4 | 34.9 | 21.2 | ⚪ OPTYMALNY |
| `L2_KT_HERESY_HIGH_MINUS1` | Kabała Pasmo: 0–9 → 0–8 | 26.8 → 🔴 ** 26.4** (`-0.4`) | 24.4 → 23.9 (`-0.5`) | 34.9 → 34.1 (`-0.8`) | 21.2 | ⚪ OPTYMALNY |
| `L2_GC_FALLS_NO_SO_PLUS1` | Gildia Upadki (bez Oficjum): 5 → 6 | 26.8 → 🔴 ** 23.5** (`-3.3`) | 24.4 → 18.6 (`-5.8`) | 34.9 → 30.8 (`-4.1`) | 21.2 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | Gildia Upadki (z Oficjum): 3 → 4 | 26.8 → 🔴 ** 20.1** (`-6.7`) | 24.4 → 23.9 (`-0.5`) | 34.9 → 26.4 (`-8.5`) | 21.2 → 10.0 (`-11.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 3 → 4 | 26.8 → 🔴 ** 17.6** (`-9.2`) | 24.4 → 19.5 (`-4.9`) | 34.9 → 21.9 (`-13.0`) | 21.2 → 11.3 (`-9.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | Gildia Upadki (z Oficjum): 3 → 2 | 26.8 → 🔴 ** 17.5** (`-9.3`) | 24.4 → 22.0 (`-2.4`) | 34.9 → 22.8 (`-12.1`) | 21.2 → 7.7 (`-13.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (default/bez SO): 3/5 → 4/6 | 26.8 → 🔴 ** 16.8** (`-10.0`) | 24.4 → 18.1 (`-6.3`) | 34.9 → 22.3 (`-12.6`) | 21.2 → 10.0 (`-11.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 26.8 → 🔴 ** 11.0** (`-15.8`) | 24.4 → 12.4 (`-12.0`) | 34.9 → 13.9 (`-21.0`) | 21.2 → 6.8 (`-14.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 26.8 → 🔴 **  9.5** (`-17.3`) | 24.4 → 10.1 (`-14.3`) | 34.9 → 12.4 (`-22.5`) | 21.2 → 6.0 (`-15.2`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 26.8 → 🔴 **  8.2** (`-18.6`) | 24.4 → 13.8 (`-10.6`) | 34.9 → 8.3 (`-26.6`) | 21.2 → 2.5 (`-18.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 26.8 → 🔴 **  5.0** (`-21.8`) | 24.4 → 8.9 (`-15.5`) | 34.9 → 5.8 (`-29.1`) | 21.2 → 0.3 (`-20.9`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (12)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 6.73 Er (1–12) | 5.5% | 5.1% | 1.62 (0–4) | 4.34 (0–22) | 3.84zł (0.0–11.3) | 6.53 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 6.60 Er (1–12) | 4.8% | 5.1% | 1.58 (0–4) | 4.23 (0–22) | 3.78zł (0.0–11.3) | 6.48 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 6.64 Er (1–12) | 5.5% | 5.1% | 1.57 (0–4) | 4.25 (0–22) | 3.80zł (0.0–11.3) | 6.47 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_MINUS1` | 6.60 Er (1–12) | 4.8% | 5.1% | 1.60 (0–4) | 4.17 (0–22) | 3.79zł (0.0–11.3) | 6.48 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_PLUS1` | 6.76 Er (1–12) | 5.5% | 5.1% | 1.63 (0–4) | 4.37 (0–22) | 3.84zł (0.0–11.3) | 6.56 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 6.73 Er (1–12) | 5.5% | 5.1% | 1.62 (0–4) | 4.34 (0–22) | 3.84zł (0.0–11.3) | 6.53 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_PLUS1` | 6.64 Er (1–12) | 3.7% | 5.1% | 1.60 (0–4) | 4.22 (0–22) | 3.79zł (0.0–11.3) | 6.52 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 6.87 Er (1–12) | 7.1% | 5.1% | 1.65 (0–4) | 4.45 (0–22) | 3.90zł (0.0–11.7) | 6.56 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 6.83 Er (1–12) | 5.5% | 5.1% | 1.64 (0–4) | 4.45 (0–22) | 3.89zł (0.2–11.3) | 6.58 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 6.39 Er (1–12) | 4.8% | 5.2% | 1.55 (0–4) | 3.96 (0–21) | 3.71zł (0.0–11.3) | 6.43 (1.0–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 6.50 Er (1–12) | 4.0% | 5.1% | 1.56 (0–4) | 4.13 (0–22) | 3.75zł (0.0–11.3) | 6.45 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 6.18 Er (1–12) | 3.8% | 5.1% | 1.50 (0–4) | 3.81 (0–22) | 3.63zł (0.0–10.7) | 6.26 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 17 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_KT_HERESY_LOW_PLUS1` | 6.73 Er (1–12) | 5.5% | 5.1% | 1.62 (0–4) | 4.34 (0–22) | 3.84zł (0.0–11.3) | 6.53 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_HERESY_HIGH_MINUS1` | 6.75 Er (1–12) | 5.8% | 5.1% | 1.62 (0–4) | 4.38 (0–22) | 3.85zł (0.0–11.3) | 6.53 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_NO_SO_PLUS1` | 6.81 Er (1–12) | 6.2% | 5.1% | 1.64 (0–4) | 4.44 (0–22) | 3.88zł (0.0–11.3) | 6.56 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_DEFAULT_PLUS1` | 6.97 Er (1–12) | 6.2% | 5.1% | 1.67 (0–4) | 4.54 (0–22) | 3.93zł (0.0–12.3) | 6.63 (1.0–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 7.03 Er (1–12) | 6.9% | 5.0% | 1.68 (0–4) | 4.70 (0–22) | 3.97zł (0.0–11.3) | 6.65 (1.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_GC_FALLS_DEFAULT_MINUS1` | 6.30 Er (1–12) | 4.5% | 5.1% | 1.52 (0–4) | 3.97 (0–22) | 3.68zł (0.0–10.7) | 6.31 (1.0–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 7.06 Er (1–12) | 6.8% | 5.1% | 1.69 (0–4) | 4.64 (0–22) | 3.97zł (0.0–12.3) | 6.66 (1.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_PLUS1` | 7.23 Er (2–12) | 7.1% | 5.1% | 1.76 (0–4) | 4.83 (0–22) | 4.02zł (0.0–11.3) | 6.84 (2.3–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_KB_DECREES_PLUS1` | 7.21 Er (1–12) | 8.8% | 5.2% | 1.74 (0–4) | 4.98 (0–22) | 4.03zł (0.0–11.3) | 6.70 (1.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_MINUS1` | 5.58 Er (1–12) | 2.0% | 5.2% | 1.30 (0–4) | 3.20 (0–17) | 3.45zł (0.0–10.7) | 5.79 (0.0–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 3.88 Er (1–12) | 2.1% | 4.5% | 0.82 (0–4) | 1.86 (0–20) | 3.19zł (0.0–11.3) | 4.43 (0.7–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.