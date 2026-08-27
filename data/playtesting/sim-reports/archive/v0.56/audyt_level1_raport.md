# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.56

**Wersja Balansu:** `v0.56` | **Data:** 2026-08-16 14:12 | **Przeanalizowano Wariantów:** 13 | **Próba:** 3000 gier/setup | **Czas:** 127.57s
**Wynik Bazy Poziomu 1 (Global):** `🟠 66.9 pkt` | 3p: `35.6 pkt` | 4p: `94.9 pkt` | 5p: `70.3 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (8)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🟠 ** 66.9** | 35.6 | 94.9 | 70.3 | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 66.9 → 🟠 ** 68.1** (`⬆️ +1.2`) | 35.6 → 38.2 (`⬆️ +2.6`) | 94.9 → 94.1 (`-0.8`) | 70.3 → 71.9 (`⬆️ +1.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 66.9 → 🟠 ** 67.4** (`⬆️ +0.5`) | 35.6 → 43.3 (`⬆️ +7.7`) | 94.9 → 85.1 (`-9.8`) | 70.3 → 73.7 (`⬆️ +3.4`) | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 11 → 12 | 66.9 → 🟠 ** 67.2** (`⬆️ +0.3`) | 35.6 → 36.3 (`⬆️ +0.7`) | 94.9 | 70.3 | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 11 → 10 | 66.9 → 🟠 ** 67.2** (`⬆️ +0.3`) | 35.6 → 36.1 (`⬆️ +0.5`) | 94.9 | 70.3 → 70.6 (`⬆️ +0.3`) | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 🟠 ** 66.9** | 35.6 → 36.4 (`⬆️ +0.8`) | 94.9 → 94.6 (`-0.3`) | 70.3 → 69.6 (`-0.7`) | ⚪ OPTYMALNY |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 66.9 → 🔴 ** 54.5** (`-12.4`) | 35.6 → 20.8 (`-14.8`) | 94.9 → 71.5 (`-23.4`) | 70.3 → 71.1 (`⬆️ +0.8`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/8 → 5/6/7 | 66.9 → 🔴 ** 52.3** (`-14.6`) | 35.6 → 47.5 (`⬆️ +11.9`) | 94.9 → 52.8 (`-42.1`) | 70.3 → 56.7 (`-13.6`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 5 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 66.9 → 🔴 ** 50.1** (`-16.8`) | 35.6 → 23.5 (`-12.1`) | 94.9 → 77.0 (`-17.9`) | 70.3 → 49.8 (`-20.5`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 66.9 → 🔴 ** 42.4** (`-24.5`) | 35.6 → 18.9 (`-16.7`) | 94.9 → 56.0 (`-38.9`) | 70.3 → 52.2 (`-18.1`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 4/4/4zł → 3/3/3zł | 66.9 → 🔴 ** 26.6** (`-40.3`) | 35.6 → 28.3 (`-7.3`) | 94.9 → 24.8 (`-70.1`) | 70.3 → 0.0 (`-70.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 4/4/4zł → 5/5/5zł | 66.9 → 🔴 ** 20.4** (`-46.5`) | 35.6 → 23.5 (`-12.1`) | 94.9 → 17.2 (`-77.7`) | 70.3 → 0.0 (`-70.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 66.9 → 🔴 ** 15.3** (`-51.6`) | 35.6 → 25.3 (`-10.3`) | 94.9 → 5.3 (`-89.6`) | 70.3 → 0.0 (`-70.3`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (8)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 5.95 Er (1–11) | 2.0% | 26.8% | 0.39 (0–3) | 3.55 (0–21) | 2.06zł (0.0–8.7) | 6.11 (1.0–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.94 Er (1–11) | 2.0% | 26.8% | 0.40 (0–3) | 3.54 (0–21) | 2.06zł (0.0–8.7) | 6.12 (1.0–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 5.88 Er (1–11) | 1.7% | 26.5% | 0.45 (0–3) | 3.53 (0–20) | 2.08zł (0.0–9.0) | 6.20 (1.0–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 5.95 Er (1–12) | 0.9% | 26.9% | 0.39 (0–3) | 3.55 (0–21) | 2.06zł (0.0–8.7) | 6.11 (1.0–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 5.92 Er (1–10) | 4.7% | 26.8% | 0.39 (0–3) | 3.53 (0–21) | 2.07zł (0.0–8.7) | 6.11 (1.0–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 5.95 Er (1–11) | 2.0% | 26.8% | 0.38 (0–3) | 3.54 (0–21) | 2.06zł (0.0–8.7) | 6.11 (1.0–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 6.23 Er (1–11) | 2.8% | 33.3% | 0.43 (0–3) | 3.58 (0–20) | 2.41zł (0.0–10.0) | 6.09 (1.0–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_THRESHOLD_MINUS1` | 5.86 Er (1–11) | 2.1% | 26.6% | 0.38 (0–3) | 4.44 (0–23) | 2.06zł (0.0–8.7) | 6.21 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 5 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_THRESHOLD_PLUS1` | 6.01 Er (1–11) | 2.2% | 27.0% | 0.40 (0–3) | 2.60 (0–17) | 2.07zł (0.0–8.3) | 5.98 (1.0–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 6.20 Er (1–11) | 3.3% | 28.1% | 0.29 (0–3) | 3.74 (0–24) | 2.01zł (0.0–8.3) | 6.09 (1.0–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 6.32 Er (1–11) | 3.6% | 28.5% | 0.25 (0–3) | 3.49 (0–19) | 1.75zł (0.0–8.3) | 5.91 (0.7–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.50 Er (1–11) | 1.2% | 25.7% | 0.52 (0–3) | 3.61 (0–20) | 2.41zł (0.0–9.3) | 6.32 (1.0–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.73 Er (1–11) | 1.4% | 21.8% | 0.38 (0–4) | 3.41 (0–19) | 1.88zł (0.0–8.0) | 6.14 (0.7–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.