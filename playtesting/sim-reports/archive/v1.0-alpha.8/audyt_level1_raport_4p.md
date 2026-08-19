# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v1.0-alpha.8

**Wersja Balansu:** `v1.0-alpha.8` | **Data:** 2026-08-19 11:53 | **Przeanalizowano Wariantów:** 19 | **Próba:** 3000 gier/setup | **Czas:** 134.64s
**Wynik Bazy Poziomu 1 (Global):** `🟡 77.8 pkt` | 3p: `0.0 pkt` | 4p: `77.8 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (1)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🟡 ** 77.8** | 0.0 | 77.8 | 0.0 | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 18 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 7 → 8 | 🟡 ** 77.8** | 0.0 | 77.8 | 0.0 | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 14 → 15 | 🟡 ** 77.8** | 0.0 | 77.8 | 0.0 | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 14 → 13 | 🟡 ** 77.8** | 0.0 | 77.8 | 0.0 | ⚪ OPTYMALNY |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 4zł → 5zł | 77.8 → 🟠 ** 74.3** (`-3.5`) | 0.0 | 77.8 → 74.3 (`-3.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_OBSERVED_PLUS1` | Próg Obserwowanej: 5 → 6 | 77.8 → 🟠 ** 67.0** (`-10.8`) | 0.0 | 77.8 → 67.0 (`-10.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 4zł → 3zł | 77.8 → 🟠 ** 65.4** (`-12.4`) | 0.0 | 77.8 → 65.4 (`-12.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 7 → 6 | 77.8 → 🟠 ** 60.0** (`-17.8`) | 0.0 | 77.8 → 60.0 (`-17.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 77.8 → 🔴 ** 59.6** (`-18.2`) | 0.0 | 77.8 → 59.6 (`-18.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_OBSERVED_MINUS1` | Próg Obserwowanej: 5 → 4 | 77.8 → 🔴 ** 56.0** (`-21.8`) | 0.0 | 77.8 → 56.0 (`-21.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 77.8 → 🔴 ** 50.5** (`-27.3`) | 0.0 | 77.8 → 50.5 (`-27.3`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_CARDS_PER_ERA_PLUS1` | Karty/Erę: 2 → 3 | 77.8 → 🔴 ** 48.1** (`-29.7`) | 0.0 | 77.8 → 48.1 (`-29.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 77.8 → 🔴 ** 43.0** (`-34.8`) | 0.0 | 77.8 → 43.0 (`-34.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 77.8 → 🔴 ** 41.0** (`-36.8`) | 0.0 | 77.8 → 41.0 (`-36.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_CARDS_PER_ERA_MINUS1` | Karty/Erę: 2 → 1 | 77.8 → 🔴 ** 33.2** (`-44.6`) | 0.0 | 77.8 → 33.2 (`-44.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 77.8 → 🔴 ** 32.0** (`-45.8`) | 0.0 | 77.8 → 32.0 (`-45.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 77.8 → 🔴 ** 25.8** (`-52.0`) | 0.0 | 77.8 → 25.8 (`-52.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_MINUS1` | Akcja Gospodarcza: 1 → 0 | 77.8 → 🔴 ** 15.2** (`-62.6`) | 0.0 | 77.8 → 15.2 (`-62.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_PLUS1` | Akcja Gospodarcza: 1 → 2 | 77.8 → 🔴 **  3.3** (`-74.5`) | 0.0 | 77.8 → 3.3 (`-74.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (1)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 6.20 Er (1–14) | 0.3% | 1.6% | 2.21 (0–5) | 4.14 (0–26) | 16.40zł (1.2–46.8) | 6.97 (0.2–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 18 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_THRESHOLD_PLUS1` | 6.20 Er (1–14) | 0.3% | 1.6% | 2.21 (0–5) | 4.14 (0–26) | 16.40zł (1.2–46.8) | 6.97 (0.2–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 6.21 Er (1–15) | 0.2% | 1.6% | 2.21 (0–6) | 4.14 (0–29) | 16.40zł (1.2–49.8) | 6.97 (0.2–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 6.20 Er (1–13) | 0.5% | 1.6% | 2.21 (0–5) | 4.14 (0–23) | 16.39zł (1.2–43.8) | 6.97 (0.2–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 6.12 Er (1–14) | 0.3% | 1.1% | 2.18 (0–5) | 4.08 (0–26) | 17.05zł (2.2–47.8) | 6.93 (0.2–10.0) | 🟢 W NORMIE |
| `L1_OBSERVED_PLUS1` | 6.32 Er (1–14) | 0.5% | 1.5% | 2.24 (0–5) | 4.39 (0–28) | 16.76zł (1.2–47.2) | 7.03 (0.2–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 6.28 Er (1–14) | 0.3% | 1.9% | 2.25 (0–5) | 4.20 (0–29) | 15.69zł (1.2–45.2) | 7.00 (0.2–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 6.32 Er (1–14) | 0.4% | 1.4% | 2.16 (0–5) | 6.47 (0–31) | 17.18zł (1.2–48.0) | 6.85 (0.2–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 6.78 Er (1–14) | 1.3% | 1.6% | 1.74 (0–4) | 3.95 (0–24) | 18.40zł (1.2–48.8) | 6.52 (0.2–10.0) | 🟢 W NORMIE |
| `L1_OBSERVED_MINUS1` | 6.02 Er (1–14) | 0.2% | 1.6% | 2.16 (0–5) | 3.81 (0–24) | 15.85zł (1.2–46.5) | 6.87 (0.2–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 5.76 Er (1–14) | 0.0% | 1.6% | 2.08 (0–5) | 3.78 (0–28) | 15.18zł (1.5–44.2) | 7.08 (0.2–10.0) | 🟢 W NORMIE |
| `L1_CARDS_PER_ERA_PLUS1` | 6.05 Er (2–14) | 0.5% | 2.9% | 2.09 (0–5) | 3.93 (0–27) | 21.71zł (4.2–61.5) | 6.85 (0.2–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.63 Er (1–14) | 0.0% | 2.0% | 2.07 (0–5) | 3.80 (0–25) | 13.59zł (1.2–47.8) | 6.87 (0.2–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 6.79 Er (1–14) | 0.5% | 1.2% | 2.33 (0–5) | 4.39 (0–27) | 19.38zł (2.0–48.2) | 7.00 (0.2–10.0) | 🟢 W NORMIE |
| `L1_CARDS_PER_ERA_MINUS1` | 7.00 Er (2–14) | 0.5% | 0.1% | 2.52 (0–5) | 4.42 (0–26) | 12.25zł (2.2–34.0) | 7.19 (0.2–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 7.80 Er (2–14) | 5.9% | 1.4% | 2.68 (0–5) | 4.99 (0–27) | 21.09zł (2.5–48.8) | 6.67 (0.8–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.25 Er (1–14) | 0.2% | 1.7% | 2.74 (0–7) | 4.07 (0–32) | 13.59zł (1.2–46.2) | 7.41 (0.2–10.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_MINUS1` | 5.44 Er (1–13) | 0.0% | 4.8% | 2.01 (0–5) | 4.89 (0–16) | 6.31zł (0.5–17.2) | 7.58 (0.2–10.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_PLUS1` | 7.65 Er (1–14) | 1.2% | 0.0% | 2.25 (0–4) | 4.24 (0–24) | 38.57zł (2.8–75.8) | 6.49 (0.2–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.