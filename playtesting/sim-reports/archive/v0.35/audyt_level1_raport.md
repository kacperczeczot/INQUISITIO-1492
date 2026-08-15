# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.35

**Wersja Balansu:** `v0.35` | **Data:** 2026-08-15 20:16 | **Przeanalizowano Wariantów:** 13 | **Próba:** 3000 gier/setup | **Czas:** 317.44s
**Wynik Bazy Poziomu 1 (Global):** `🟢 97.5 pkt` | 3p: `94.2 pkt` | 4p: `99.1 pkt` | 5p: `99.3 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (3)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🟢 ** 97.5** | 94.2 | 99.1 | 99.3 | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 97.5 → 🟢 ** 97.6** (`⬆️ +0.1`) | 94.2 | 99.1 → 99.2 (`⬆️ +0.1`) | 99.3 | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 97.5 → 🟢 ** 97.4** (`-0.1`) | 94.2 → 93.7 (`-0.5`) | 99.1 → 99.0 (`-0.1`) | 99.3 → 99.4 (`⬆️ +0.1`) | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 10 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 10 → 11 | 🟢 ** 97.5** | 94.2 | 99.1 | 99.3 | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 10 → 9 | 97.5 → 🟢 ** 96.4** (`-1.1`) | 94.2 → 90.8 (`-3.4`) | 99.1 | 99.3 | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/8 → 5/6/7 | 97.5 → 🟡 ** 86.4** (`-11.1`) | 94.2 → 88.7 (`-5.5`) | 99.1 → 71.3 (`-27.8`) | 99.3 → 99.1 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 97.5 → 🟡 ** 86.3** (`-11.2`) | 94.2 → 80.3 (`-13.9`) | 99.1 → 96.0 (`-3.1`) | 99.3 → 82.6 (`-16.7`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 97.5 → 🟡 ** 82.3** (`-15.2`) | 94.2 → 76.5 (`-17.7`) | 99.1 → 81.5 (`-17.6`) | 99.3 → 88.8 (`-10.5`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 97.5 → 🟠 ** 72.6** (`-24.9`) | 94.2 → 72.2 (`-22.0`) | 99.1 → 69.0 (`-30.1`) | 99.3 → 76.7 (`-22.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 97.5 → 🟠 ** 71.4** (`-26.1`) | 94.2 → 67.0 (`-27.2`) | 99.1 → 58.3 (`-40.8`) | 99.3 → 89.0 (`-10.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 3/3/2zł → 4/4/3zł | 97.5 → 🟠 ** 67.8** (`-29.7`) | 94.2 → 84.8 (`-9.4`) | 99.1 → 68.1 (`-31.0`) | 99.3 → 50.5 (`-48.8`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 97.5 → 🟠 ** 62.2** (`-35.3`) | 94.2 → 61.6 (`-32.6`) | 99.1 → 62.8 (`-36.3`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 3/3/2zł → 2/2/1zł | 97.5 → 🔴 ** 49.8** (`-47.7`) | 94.2 → 60.6 (`-33.6`) | 99.1 → 39.0 (`-60.1`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (3)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 5.55 Er (1–10) | 1.3% | 26.2% | 1.04 (0–4) | 3.62 (0–18) | 1.21zł (0.0–5.0) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.54 Er (1–10) | 1.2% | 26.2% | 1.06 (0–4) | 3.62 (0–18) | 1.21zł (0.0–5.0) | 6.36 (0.7–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 5.55 Er (1–10) | 1.2% | 26.2% | 1.02 (0–3) | 3.62 (0–18) | 1.21zł (0.0–5.0) | 6.34 (0.7–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 10 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_MAX_ERAS_PLUS1` | 5.55 Er (1–11) | 0.4% | 26.2% | 1.04 (0–4) | 3.62 (0–20) | 1.21zł (0.0–5.0) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 5.54 Er (1–9) | 3.2% | 26.2% | 1.04 (0–4) | 3.61 (0–18) | 1.21zł (0.0–4.3) | 6.34 (0.7–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 5.40 Er (1–10) | 1.1% | 25.7% | 1.01 (0–3) | 4.51 (0–20) | 1.20zł (0.0–5.7) | 6.39 (0.7–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 5.50 Er (1–10) | 1.1% | 26.0% | 1.08 (0–4) | 3.65 (0–19) | 1.21zł (0.0–4.7) | 6.54 (1.0–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 5.81 Er (1–10) | 1.8% | 32.8% | 1.04 (0–4) | 3.60 (0–20) | 1.46zł (0.0–5.3) | 6.26 (0.7–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_THRESHOLD_PLUS1` | 5.70 Er (1–10) | 1.5% | 26.7% | 1.07 (0–4) | 2.62 (0–18) | 1.22zł (0.0–5.0) | 6.27 (0.7–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 5.73 Er (1–10) | 1.8% | 26.8% | 1.00 (0–3) | 3.61 (0–18) | 1.23zł (0.0–5.0) | 6.10 (0.5–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.39 Er (1–10) | 0.9% | 24.2% | 1.07 (0–4) | 3.75 (0–19) | 1.53zł (0.0–5.7) | 6.51 (0.8–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.37 Er (1–10) | 0.9% | 21.1% | 1.08 (0–4) | 3.52 (0–17) | 1.00zł (0.0–4.0) | 6.45 (0.8–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 5.86 Er (1–10) | 2.0% | 27.1% | 0.94 (0–4) | 3.27 (0–17) | 0.84zł (0.0–4.3) | 6.16 (0.6–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.