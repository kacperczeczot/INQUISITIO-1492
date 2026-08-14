# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.23

**Wersja Balansu:** `v0.23` | **Data:** 2026-08-14 14:31 | **Przeanalizowano Wariantów:** 13 | **Próba:** 500 gier/setup | **Czas:** 17.38s
**Wynik Bazy Poziomu 1 (Global):** `🟢 88.6 pkt` | 3p: `78.5 pkt` | 4p: `88.4 pkt` | 5p: `98.8 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (6)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🟢 ** 88.6** | 78.5 | 88.4 | 98.8 | ⚪ OPTYMALNY |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 88.6 → 🟢 ** 93.2** (`⬆️ +4.6`) | 78.5 → 85.6 (`⬆️ +7.1`) | 88.4 → 96.2 (`⬆️ +7.8`) | 98.8 → 97.9 (`-0.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 9 → 10 | 88.6 → 🟢 ** 89.6** (`⬆️ +1.0`) | 78.5 → 81.7 (`⬆️ +3.2`) | 88.4 → 88.3 (`-0.1`) | 98.8 | 🟢 POPRAWIA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 88.6 → 🟢 ** 89.3** (`⬆️ +0.7`) | 78.5 → 77.0 (`-1.5`) | 88.4 → 93.5 (`⬆️ +5.1`) | 98.8 → 97.4 (`-1.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/8 → 5/6/7 | 88.6 → 🟢 ** 89.1** (`⬆️ +0.5`) | 78.5 → 80.8 (`⬆️ +2.3`) | 88.4 → 88.3 (`-0.1`) | 98.8 → 98.3 (`-0.5`) | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 88.6 → 🟢 ** 87.7** (`-0.9`) | 78.5 → 78.2 (`-0.3`) | 88.4 → 85.6 (`-2.8`) | 98.8 → 99.2 (`⬆️ +0.4`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 7 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 9 → 8 | 88.6 → 🟢 ** 82.7** (`-5.9`) | 78.5 → 65.9 (`-12.6`) | 88.4 → 83.6 (`-4.8`) | 98.8 → 98.5 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 88.6 → 🟢 ** 71.1** (`-17.5`) | 78.5 → 76.3 (`-2.2`) | 88.4 → 78.3 (`-10.1`) | 98.8 → 58.7 (`-40.1`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 88.6 → 🟢 ** 70.3** (`-18.3`) | 78.5 → 60.1 (`-18.4`) | 88.4 → 52.9 (`-35.5`) | 98.8 → 98.0 (`-0.8`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 3/3/2zł → 4/4/3zł | 88.6 → 🟢 ** 69.8** (`-18.8`) | 78.5 → 74.8 (`-3.7`) | 88.4 → 59.0 (`-29.4`) | 98.8 → 75.5 (`-23.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 88.6 → 🟢 ** 67.9** (`-20.7`) | 78.5 → 66.0 (`-12.5`) | 88.4 → 55.8 (`-32.6`) | 98.8 → 81.9 (`-16.9`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 88.6 → 🟢 ** 65.2** (`-23.4`) | 78.5 → 65.6 (`-12.9`) | 88.4 → 58.1 (`-30.3`) | 98.8 → 71.8 (`-27.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 3/3/2zł → 2/2/1zł | 88.6 → 🟢 ** 58.6** (`-30.0`) | 78.5 → 67.0 (`-11.5`) | 88.4 → 50.2 (`-38.2`) | 98.8 → 0.0 (`-98.8`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (6)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 5.67 Er (1–9) | 4.7% | 29.2% | 1.05 (0–4) | 3.55 (0–17) | 0.58zł (0.0–3.0) | 6.06 (1.2–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 5.63 Er (1–9) | 4.2% | 29.1% | 1.08 (0–4) | 3.60 (0–16) | 0.58zł (0.0–3.0) | 6.26 (1.3–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 5.69 Er (1–10) | 2.0% | 29.3% | 1.05 (0–4) | 3.57 (0–20) | 0.58zł (0.0–3.0) | 6.07 (1.2–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.66 Er (1–9) | 4.6% | 29.2% | 1.07 (0–4) | 3.55 (0–17) | 0.58zł (0.0–3.0) | 6.08 (1.2–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 5.52 Er (1–9) | 4.2% | 28.8% | 1.02 (0–3) | 4.52 (0–20) | 0.58zł (0.0–3.0) | 6.12 (1.2–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 5.67 Er (1–9) | 4.8% | 29.3% | 1.03 (0–3) | 3.55 (0–17) | 0.58zł (0.0–3.0) | 6.05 (1.2–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 7 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_MAX_ERAS_MINUS1` | 5.62 Er (1–8) | 9.1% | 29.1% | 1.05 (0–4) | 3.51 (0–17) | 0.57zł (0.0–3.0) | 6.05 (1.2–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.47 Er (1–9) | 3.5% | 25.5% | 1.07 (0–3) | 3.46 (0–16) | 0.48zł (0.0–2.7) | 6.11 (1.3–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_PLUS1` | 5.82 Er (1–9) | 5.6% | 29.6% | 1.07 (0–4) | 2.44 (0–14) | 0.58zł (0.0–3.0) | 5.95 (1.2–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.46 Er (1–9) | 3.3% | 26.0% | 1.04 (0–4) | 3.64 (0–15) | 0.82zł (0.0–3.3) | 6.22 (1.5–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 5.91 Er (1–9) | 5.5% | 34.4% | 1.04 (0–4) | 3.46 (0–16) | 0.82zł (0.0–3.3) | 6.00 (0.7–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_AGENTS_MINUS1` | 5.81 Er (1–9) | 5.3% | 29.6% | 1.00 (0–3) | 3.47 (0–16) | 0.58zł (0.0–3.3) | 5.78 (1.2–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 5.97 Er (1–9) | 6.9% | 30.4% | 0.93 (0–3) | 3.21 (0–15) | 0.41zł (0.0–2.3) | 5.86 (1.0–10.0) | 🔴 PRZEKROCZONE NORMY |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.