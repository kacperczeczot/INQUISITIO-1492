# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v1.0-alpha.23

**Wersja Balansu:** `v1.0-alpha.23` | **Data:** 2026-08-22 14:36 | **Przeanalizowano Wariantów:** 19 | **Próba:** 3000 gier/setup | **Czas:** 86.61s
**Wynik Bazy Poziomu 1 (Global):** `🟡 82.9 pkt` | 3p: `0.0 pkt` | 4p: `82.9 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (2)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🟡 ** 82.9** | 0.0 | 82.9 | 0.0 | ⚪ OPTYMALNY |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 4zł → 5zł | 82.9 → 🟡 ** 83.2** (`⬆️ +0.3`) | 0.0 | 82.9 → 83.2 (`⬆️ +0.3`) | 0.0 | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 17 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 7 → 8 | 🟡 ** 82.9** | 0.0 | 82.9 | 0.0 | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 14 → 15 | 🟡 ** 82.9** | 0.0 | 82.9 | 0.0 | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 14 → 13 | 🟡 ** 82.9** | 0.0 | 82.9 | 0.0 | ⚪ OPTYMALNY |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 4zł → 3zł | 82.9 → 🟡 ** 78.1** (`-4.8`) | 0.0 | 82.9 → 78.1 (`-4.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_OBSERVED_MINUS1` | Próg Obserwowanej: 5 → 4 | 82.9 → 🟠 ** 73.4** (`-9.5`) | 0.0 | 82.9 → 73.4 (`-9.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_OBSERVED_PLUS1` | Próg Obserwowanej: 5 → 6 | 82.9 → 🟠 ** 72.4** (`-10.5`) | 0.0 | 82.9 → 72.4 (`-10.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 82.9 → 🔴 ** 56.1** (`-26.8`) | 0.0 | 82.9 → 56.1 (`-26.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 7 → 6 | 82.9 → 🔴 ** 54.8** (`-28.1`) | 0.0 | 82.9 → 54.8 (`-28.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 82.9 → 🔴 ** 50.2** (`-32.7`) | 0.0 | 82.9 → 50.2 (`-32.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 82.9 → 🔴 ** 49.4** (`-33.5`) | 0.0 | 82.9 → 49.4 (`-33.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_CARDS_PER_ERA_PLUS1` | Karty/Erę: 2 → 3 | 82.9 → 🔴 ** 45.3** (`-37.6`) | 0.0 | 82.9 → 45.3 (`-37.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 82.9 → 🔴 ** 34.7** (`-48.2`) | 0.0 | 82.9 → 34.7 (`-48.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 82.9 → 🔴 ** 33.3** (`-49.6`) | 0.0 | 82.9 → 33.3 (`-49.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 82.9 → 🔴 ** 33.1** (`-49.8`) | 0.0 | 82.9 → 33.1 (`-49.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_CARDS_PER_ERA_MINUS1` | Karty/Erę: 2 → 1 | 82.9 → 🔴 ** 30.7** (`-52.2`) | 0.0 | 82.9 → 30.7 (`-52.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_MINUS1` | Akcja Gospodarcza: 1 → 0 | 82.9 → 🔴 ** 16.9** (`-66.0`) | 0.0 | 82.9 → 16.9 (`-66.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_PLUS1` | Akcja Gospodarcza: 1 → 2 | 82.9 → 🔴 ** 12.9** (`-70.0`) | 0.0 | 82.9 → 12.9 (`-70.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (2)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 5.91 Er (1–14) | 0.2% | 1.2% | 1.67 (0–4) | 4.25 (0–20) | 15.38zł (1.5–46.8) | 6.99 (0.2–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.88 Er (1–14) | 0.1% | 0.7% | 1.66 (0–4) | 4.26 (0–16) | 16.14zł (2.2–48.0) | 6.97 (0.2–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 17 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_THRESHOLD_PLUS1` | 5.91 Er (1–14) | 0.2% | 1.2% | 1.67 (0–4) | 4.25 (0–20) | 15.38zł (1.5–46.8) | 6.99 (0.2–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 5.91 Er (1–15) | 0.2% | 1.2% | 1.67 (0–5) | 4.25 (0–22) | 15.39zł (1.5–49.0) | 6.99 (0.2–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 5.90 Er (1–13) | 0.3% | 1.2% | 1.67 (0–4) | 4.25 (0–20) | 15.38zł (1.5–43.5) | 6.99 (0.2–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 6.00 Er (1–14) | 0.2% | 1.3% | 1.72 (0–4) | 4.30 (0–21) | 14.85zł (1.5–45.8) | 7.04 (0.2–10.0) | 🟢 W NORMIE |
| `L1_OBSERVED_MINUS1` | 5.78 Er (1–14) | 0.0% | 1.2% | 1.64 (0–4) | 3.93 (0–20) | 15.21zł (1.5–45.5) | 6.88 (0.2–10.0) | 🟢 W NORMIE |
| `L1_OBSERVED_PLUS1` | 5.95 Er (1–14) | 0.3% | 1.2% | 1.68 (0–4) | 4.51 (0–26) | 15.30zł (1.5–46.8) | 7.09 (0.2–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 6.40 Er (1–14) | 0.8% | 1.2% | 1.23 (0–3) | 4.18 (0–22) | 16.92zł (1.5–48.0) | 6.59 (0.2–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 6.09 Er (1–14) | 0.2% | 1.1% | 1.75 (0–4) | 6.72 (0–27) | 16.34zł (1.5–47.8) | 6.86 (0.2–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 5.49 Er (1–14) | 0.0% | 1.2% | 1.54 (0–4) | 3.86 (0–21) | 14.34zł (1.8–47.8) | 7.05 (0.2–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 6.46 Er (1–14) | 0.4% | 1.0% | 1.88 (0–4) | 4.54 (0–23) | 18.18zł (1.5–48.8) | 7.01 (0.2–10.0) | 🟢 W NORMIE |
| `L1_CARDS_PER_ERA_PLUS1` | 5.59 Er (2–14) | 0.2% | 2.6% | 1.52 (0–4) | 4.03 (0–21) | 19.64zł (3.2–61.8) | 6.84 (0.8–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.38 Er (1–14) | 0.0% | 1.3% | 1.46 (0–4) | 3.87 (0–18) | 12.98zł (1.5–42.5) | 6.89 (0.2–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 7.31 Er (2–14) | 3.5% | 1.1% | 2.07 (0–4) | 5.12 (0–26) | 19.55zł (2.5–48.2) | 6.79 (0.8–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.16 Er (1–14) | 0.1% | 1.2% | 2.24 (0–6) | 4.15 (0–27) | 13.61zł (1.5–45.0) | 7.41 (0.2–10.0) | 🟢 W NORMIE |
| `L1_CARDS_PER_ERA_MINUS1` | 6.93 Er (2–14) | 0.5% | 0.0% | 2.05 (0–4) | 4.56 (0–20) | 12.87zł (2.5–33.5) | 7.07 (0.2–10.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_MINUS1` | 5.25 Er (1–10) | 0.0% | 4.0% | 1.72 (0–5) | 5.17 (0–18) | 6.47zł (0.2–17.2) | 7.87 (0.2–10.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_PLUS1` | 7.15 Er (1–14) | 0.7% | 0.0% | 2.11 (0–4) | 4.35 (0–24) | 35.30zł (2.8–75.8) | 6.41 (0.2–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.