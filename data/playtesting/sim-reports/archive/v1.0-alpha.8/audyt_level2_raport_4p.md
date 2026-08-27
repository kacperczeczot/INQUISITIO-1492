[Strona główna](../../../../../README.md) > [v1.0-alpha.8](README.md) > [audyt_level2_raport_4p](audyt_level2_raport_4p.md)

---

# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v1.0-alpha.8

**Wersja Balansu:** `v1.0-alpha.8` | **Data:** 2026-08-19 11:56 | **Przeanalizowano Wariantów:** 17 | **Próba:** 3000 gier/setup | **Czas:** 165.75s
**Wynik Bazy Poziomu 2 (Global):** `🟡 77.8 pkt` | 3p: `0.0 pkt` | 4p: `77.8 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (1)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 🟡 ** 77.8** | 0.0 | 77.8 | 0.0 | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 16 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_PLUS1` | Cienie Era ścieżki: 1 → 2 | 🟡 ** 77.8** | 0.0 | 77.8 | 0.0 | ⚪ OPTYMALNY |
| `L2_CAA_ERA_MINUS1` | Cienie Era ścieżki: 1 → 0 | 🟡 ** 77.8** | 0.0 | 77.8 | 0.0 | ⚪ OPTYMALNY |
| `L2_KT_ERA_MINUS1` | Kabała Era: 6 → 5 | 77.8 → 🟠 ** 70.9** (`-6.9`) | 0.0 | 77.8 → 70.9 (`-6.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki: 8 → 9 | 77.8 → 🟠 ** 66.3** (`-11.5`) | 0.0 | 77.8 → 66.3 (`-11.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy: 6 → 7 | 77.8 → 🟠 ** 63.8** (`-14.0`) | 0.0 | 77.8 → 63.8 (`-14.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki: 8 → 7 | 77.8 → 🔴 ** 57.5** (`-20.3`) | 0.0 | 77.8 → 57.5 (`-20.3`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_ERA_PLUS1` | Kabała Era: 6 → 7 | 77.8 → 🔴 ** 51.1** (`-26.7`) | 0.0 | 77.8 → 51.1 (`-26.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy: 6 → 5 | 77.8 → 🔴 ** 49.6** (`-28.2`) | 0.0 | 77.8 → 49.6 (`-28.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty: 2 → 3 | 77.8 → 🔴 ** 38.4** (`-39.4`) | 0.0 | 77.8 → 38.4 (`-39.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie: 2 → 3 | 77.8 → 🔴 ** 34.8** (`-43.0`) | 0.0 | 77.8 → 34.8 (`-43.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty: 2 → 1 | 77.8 → 🔴 ** 33.6** (`-44.2`) | 0.0 | 77.8 → 33.6 (`-44.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_PLUS1` | Oficjum Skazania: 2/3/3 → 3/4/4 | 77.8 → 🔴 ** 32.5** (`-45.3`) | 0.0 | 77.8 → 32.5 (`-45.3`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety: 2 → 3 | 77.8 → 🔴 ** 30.0** (`-47.8`) | 0.0 | 77.8 → 30.0 (`-47.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania: 2/3/3 → 1/2/2 | 77.8 → 🔴 ** 21.3** (`-56.5`) | 0.0 | 77.8 → 21.3 (`-56.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety: 2 → 1 | 77.8 → 🔴 ** 20.3** (`-57.5`) | 0.0 | 77.8 → 20.3 (`-57.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie: 2 → 1 | 77.8 → 🔴 ** 18.3** (`-59.5`) | 0.0 | 77.8 → 18.3 (`-59.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (1)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 6.20 Er (1–14) | 0.3% | 1.6% | 2.21 (0–5) | 4.14 (0–26) | 16.40zł (1.2–46.8) | 6.97 (0.2–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 16 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_CAA_ERA_PLUS1` | 6.22 Er (2–14) | 0.3% | 1.6% | 2.21 (0–5) | 4.14 (0–26) | 16.44zł (3.0–46.8) | 6.99 (0.2–10.0) | 🟢 W NORMIE |
| `L2_CAA_ERA_MINUS1` | 6.20 Er (1–14) | 0.3% | 1.6% | 2.21 (0–5) | 4.14 (0–26) | 16.40zł (1.2–46.8) | 6.97 (0.2–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_MINUS1` | 5.97 Er (1–14) | 0.3% | 1.5% | 1.98 (0–5) | 3.79 (0–26) | 15.84zł (1.2–46.8) | 6.76 (0.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 6.32 Er (1–14) | 0.3% | 1.5% | 2.26 (0–5) | 4.35 (0–26) | 16.74zł (1.2–46.8) | 7.01 (0.2–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 6.35 Er (1–14) | 0.7% | 1.5% | 2.26 (0–5) | 4.42 (0–28) | 16.83zł (1.2–46.8) | 7.02 (0.2–10.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 6.04 Er (1–14) | 0.3% | 1.6% | 2.15 (0–5) | 3.86 (0–26) | 15.91zł (1.2–46.8) | 6.90 (0.2–10.0) | 🟢 W NORMIE |
| `L2_KT_ERA_PLUS1` | 6.32 Er (1–14) | 0.3% | 1.6% | 2.22 (0–5) | 4.35 (0–26) | 16.69zł (1.2–46.8) | 7.02 (0.2–10.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 5.96 Er (1–14) | 0.1% | 1.6% | 2.13 (0–5) | 3.72 (0–20) | 15.69zł (1.2–45.0) | 6.86 (0.2–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 6.36 Er (1–14) | 0.3% | 1.6% | 2.24 (0–5) | 4.46 (0–26) | 16.81zł (1.2–46.8) | 7.04 (0.2–10.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 6.64 Er (3–14) | 0.4% | 1.5% | 2.41 (1–5) | 4.64 (0–26) | 17.60zł (3.2–46.8) | 7.36 (3.2–10.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 5.89 Er (1–14) | 0.2% | 1.6% | 2.15 (0–5) | 3.60 (0–26) | 15.45zł (1.2–46.5) | 6.84 (0.2–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_PLUS1` | 6.23 Er (1–14) | 0.3% | 1.6% | 2.22 (0–5) | 4.23 (0–26) | 16.48zł (1.2–46.8) | 6.97 (0.2–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.53 Er (1–14) | 0.4% | 1.5% | 2.35 (0–5) | 4.79 (0–26) | 17.28zł (1.2–46.8) | 7.11 (0.2–10.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 5.48 Er (1–14) | 0.1% | 1.6% | 1.93 (0–5) | 2.86 (0–13) | 14.31zł (1.2–44.8) | 6.64 (0.2–10.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 4.71 Er (1–14) | 0.1% | 1.7% | 1.63 (0–5) | 2.33 (0–20) | 12.48zł (1.0–46.8) | 5.70 (0.2–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L2_CAA_RELICS_MINUS1` | 3.86 Er (1–14) | 0.1% | 1.6% | 1.32 (0–5) | 1.86 (0–21) | 10.33zł (1.2–45.0) | 4.66 (0.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.