# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.19

**Wersja Balansu:** `v0.19` | **Data:** 2026-08-14 13:37 | **Przeanalizowano Wariantów:** 13 | **Próba:** 3000 gier/setup | **Czas:** 82.35s
**Wynik Bazy Poziomu 1 (Global):** `🟢 91.7 pkt` | 3p: `87.1 pkt` | 4p: `88.6 pkt` | 5p: `99.3 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (5)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🟢 ** 91.7** | 87.1 | 88.6 | 99.3 | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 9 → 10 | 91.7 → 🟢 ** 91.9** (`⬆️ +0.2`) | 87.1 → 87.9 (`⬆️ +0.8`) | 88.6 | 99.3 | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 🟢 ** 91.7** | 87.1 → 86.3 (`-0.8`) | 88.6 → 89.2 (`⬆️ +0.6`) | 99.3 → 99.5 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 91.7 → 🟢 ** 90.4** (`-1.3`) | 87.1 → 86.9 (`-0.2`) | 88.6 → 84.9 (`-3.7`) | 99.3 → 99.4 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 91.7 → 🟢 ** 80.1** (`-11.6`) | 87.1 → 88.6 (`⬆️ +1.5`) | 88.6 → 85.0 (`-3.6`) | 99.3 → 66.7 (`-32.6`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 8 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 91.7 → 🟢 ** 89.4** (`-2.3`) | 87.1 → 84.6 (`-2.5`) | 88.6 → 87.1 (`-1.5`) | 99.3 → 96.5 (`-2.8`) | 🔴 POGARSZA GLOBALNIE |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 9 → 8 | 91.7 → 🟢 ** 87.5** (`-4.2`) | 87.1 → 74.9 (`-12.2`) | 88.6 → 88.4 (`-0.2`) | 99.3 → 99.2 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 91.7 → 🟢 ** 82.5** (`-9.2`) | 87.1 → 75.3 (`-11.8`) | 88.6 → 84.5 (`-4.1`) | 99.3 → 87.6 (`-11.7`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/8 → 5/6/7 | 91.7 → 🟢 ** 71.4** (`-20.3`) | 87.1 → 72.8 (`-14.3`) | 88.6 → 43.6 (`-45.0`) | 99.3 → 97.7 (`-1.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 3/3/2zł → 2/2/1zł | 91.7 → 🟢 ** 68.8** (`-22.9`) | 87.1 → 81.5 (`-5.6`) | 88.6 → 56.1 (`-32.5`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 91.7 → 🟢 ** 63.9** (`-27.8`) | 87.1 → 47.7 (`-39.4`) | 88.6 → 62.1 (`-26.5`) | 99.3 → 82.0 (`-17.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 91.7 → 🟢 ** 63.4** (`-28.3`) | 87.1 → 69.1 (`-18.0`) | 88.6 → 55.2 (`-33.4`) | 99.3 → 66.0 (`-33.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 3/3/2zł → 4/4/3zł | 91.7 → 🟢 ** 62.8** (`-28.9`) | 87.1 → 60.9 (`-26.2`) | 88.6 → 63.3 (`-25.3`) | 99.3 → 64.3 (`-35.0`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (5)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 5.51 Er (1–9) | 4.1% | 28.3% | 1.02 (0–4) | 3.53 (0–20) | 0.52zł (0.0–3.0) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 5.52 Er (1–10) | 1.5% | 28.3% | 1.02 (0–4) | 3.54 (0–21) | 0.52zł (0.0–3.0) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.49 Er (1–9) | 4.0% | 28.3% | 1.05 (0–4) | 3.53 (0–20) | 0.52zł (0.0–3.0) | 6.21 (0.7–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 5.51 Er (1–9) | 4.1% | 28.3% | 1.01 (0–4) | 3.53 (0–20) | 0.52zł (0.0–3.0) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.34 Er (1–9) | 3.4% | 25.3% | 1.06 (0–3) | 3.45 (0–18) | 0.44zł (0.0–2.7) | 6.24 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 8 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_AGENTS_PLUS1` | 5.45 Er (1–9) | 3.8% | 28.1% | 1.05 (0–4) | 3.58 (0–18) | 0.52zł (0.0–2.7) | 6.39 (1.2–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 5.47 Er (1–8) | 8.3% | 28.2% | 1.02 (0–4) | 3.49 (0–18) | 0.52zł (0.0–3.0) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 5.76 Er (1–9) | 4.5% | 34.1% | 1.03 (0–4) | 3.47 (0–18) | 0.73zł (0.0–3.0) | 6.10 (0.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_THRESHOLD_MINUS1` | 5.31 Er (1–9) | 3.6% | 27.7% | 0.99 (0–4) | 4.52 (0–20) | 0.51zł (0.0–3.3) | 6.24 (0.7–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 5.89 Er (1–9) | 6.2% | 31.1% | 0.94 (0–4) | 3.33 (0–18) | 0.43zł (0.0–2.5) | 6.07 (0.7–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_AGENTS_MINUS1` | 5.66 Er (1–9) | 4.8% | 28.8% | 0.98 (0–3) | 3.47 (0–19) | 0.52zł (0.0–2.7) | 5.95 (0.7–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_PLUS1` | 5.68 Er (1–9) | 4.9% | 28.8% | 1.05 (0–4) | 2.46 (0–16) | 0.52zł (0.0–3.0) | 6.12 (0.7–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.26 Er (1–9) | 2.7% | 25.6% | 1.04 (0–3) | 3.61 (0–18) | 0.74zł (0.0–3.7) | 6.27 (1.0–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.