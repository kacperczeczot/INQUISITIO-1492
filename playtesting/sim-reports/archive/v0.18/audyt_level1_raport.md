# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.18

**Wersja Balansu:** `v0.18` | **Data:** 2026-08-14 13:27 | **Przeanalizowano Wariantów:** 13 | **Próba:** 3000 gier/setup | **Czas:** 81.44s
**Wynik Bazy Poziomu 1 (Global):** `🟢 89.9 pkt` | 3p: `86.2 pkt` | 4p: `84.5 pkt` | 5p: `98.9 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (5)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🟢 ** 89.9** | 86.2 | 84.5 | 98.9 | ⚪ OPTYMALNY |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 89.9 → 🟢 ** 92.1** (`⬆️ +2.2`) | 86.2 → 90.7 (`⬆️ +4.5`) | 84.5 → 89.2 (`⬆️ +4.7`) | 98.9 → 96.5 (`-2.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 89.9 → 🟢 ** 91.3** (`⬆️ +1.4`) | 86.2 → 85.9 (`-0.3`) | 84.5 → 88.9 (`⬆️ +4.4`) | 98.9 → 99.2 (`⬆️ +0.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 9 → 10 | 89.9 → 🟢 ** 90.8** (`⬆️ +0.9`) | 86.2 → 88.9 (`⬆️ +2.7`) | 84.5 → 84.6 (`⬆️ +0.1`) | 98.9 | 🟢 POPRAWIA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 89.9 → 🟢 ** 81.7** (`-8.2`) | 86.2 → 92.0 (`⬆️ +5.8`) | 84.5 → 87.2 (`⬆️ +2.7`) | 98.9 → 66.0 (`-32.9`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 8 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 89.9 → 🟢 ** 89.0** (`-0.9`) | 86.2 → 85.8 (`-0.4`) | 84.5 → 82.2 (`-2.3`) | 98.9 | 🔴 POGARSZA GLOBALNIE |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 9 → 8 | 89.9 → 🟢 ** 87.0** (`-2.9`) | 86.2 → 77.8 (`-8.4`) | 84.5 → 84.3 (`-0.2`) | 98.9 | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/8 → 5/6/7 | 89.9 → 🟢 ** 80.5** (`-9.4`) | 86.2 → 84.6 (`-1.6`) | 84.5 → 59.0 (`-25.5`) | 98.9 → 97.8 (`-1.1`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 89.9 → 🟢 ** 72.5** (`-17.4`) | 86.2 → 64.5 (`-21.7`) | 84.5 → 69.8 (`-14.7`) | 98.9 → 83.3 (`-15.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 3/3/2zł → 4/4/3zł | 89.9 → 🟢 ** 67.4** (`-22.5`) | 86.2 → 66.1 (`-20.1`) | 84.5 → 67.5 (`-17.0`) | 98.9 → 68.7 (`-30.2`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 89.9 → 🟢 ** 57.2** (`-32.7`) | 86.2 → 40.7 (`-45.5`) | 84.5 → 53.3 (`-31.2`) | 98.9 → 77.5 (`-21.4`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 3/3/2zł → 2/2/1zł | 89.9 → 🟢 ** 54.6** (`-35.3`) | 86.2 → 65.6 (`-20.6`) | 84.5 → 43.6 (`-40.9`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 89.9 → 🟢 ** 53.1** (`-36.8`) | 86.2 → 54.8 (`-31.4`) | 84.5 → 53.6 (`-30.9`) | 98.9 → 50.9 (`-48.0`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (5)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 5.48 Er (1–9) | 3.2% | 28.2% | 1.02 (0–4) | 3.49 (0–20) | 0.51zł (0.0–3.0) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 5.43 Er (1–9) | 2.9% | 28.0% | 1.05 (0–4) | 3.53 (0–17) | 0.51zł (0.0–2.7) | 6.38 (1.2–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.47 Er (1–9) | 3.1% | 28.2% | 1.04 (0–4) | 3.48 (0–20) | 0.51zł (0.0–3.0) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 5.49 Er (1–10) | 1.2% | 28.2% | 1.02 (0–4) | 3.50 (0–21) | 0.51zł (0.0–3.0) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.31 Er (1–9) | 2.7% | 25.3% | 1.05 (0–3) | 3.41 (0–18) | 0.44zł (0.0–2.7) | 6.23 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 8 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 5.48 Er (1–9) | 3.2% | 28.2% | 1.00 (0–4) | 3.49 (0–20) | 0.51zł (0.0–3.0) | 6.18 (0.7–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 5.45 Er (1–8) | 6.8% | 28.1% | 1.02 (0–4) | 3.46 (0–18) | 0.51zł (0.0–3.0) | 6.18 (0.7–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 5.29 Er (1–9) | 2.8% | 27.6% | 0.99 (0–4) | 4.47 (0–19) | 0.51zł (0.0–3.3) | 6.23 (0.7–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 5.73 Er (1–9) | 3.7% | 34.1% | 1.02 (0–4) | 3.43 (0–18) | 0.72zł (0.0–3.0) | 6.08 (0.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_START_GOLD_PLUS1` | 5.23 Er (1–9) | 2.1% | 25.5% | 1.03 (0–3) | 3.57 (0–18) | 0.74zł (0.0–3.7) | 6.26 (1.0–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 5.63 Er (1–9) | 4.0% | 28.7% | 0.98 (0–3) | 3.43 (0–17) | 0.52zł (0.0–2.7) | 5.94 (0.7–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 5.85 Er (1–9) | 4.9% | 31.1% | 0.94 (0–4) | 3.27 (0–18) | 0.43zł (0.0–2.5) | 6.06 (0.7–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_THRESHOLD_PLUS1` | 5.65 Er (1–9) | 3.9% | 28.7% | 1.05 (0–4) | 2.41 (0–16) | 0.51zł (0.0–3.0) | 6.11 (0.7–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.