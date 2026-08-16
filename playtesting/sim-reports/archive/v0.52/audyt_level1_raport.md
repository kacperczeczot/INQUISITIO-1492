# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.52

**Wersja Balansu:** `v0.52` | **Data:** 2026-08-16 13:45 | **Przeanalizowano Wariantów:** 13 | **Próba:** 1000 gier/setup | **Czas:** 40.21s
**Wynik Bazy Poziomu 1 (Global):** `🟡 86.7 pkt` | 3p: `74.9 pkt` | 4p: `99.5 pkt` | 5p: `85.7 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (6)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🟡 ** 86.7** | 74.9 | 99.5 | 85.7 | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 86.7 → 🟢 ** 90.3** (`⬆️ +3.6`) | 74.9 | 99.5 → 99.6 (`⬆️ +0.1`) | 85.7 → 96.4 (`⬆️ +10.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 11 → 12 | 86.7 → 🟡 ** 86.9** (`⬆️ +0.2`) | 74.9 → 75.4 (`⬆️ +0.5`) | 99.5 | 85.7 | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 🟡 ** 86.7** | 74.9 → 75.0 (`⬆️ +0.1`) | 99.5 | 85.7 → 85.5 (`-0.2`) | ⚪ OPTYMALNY |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/8 → 5/6/7 | 86.7 → 🟡 ** 85.4** (`-1.3`) | 74.9 → 85.2 (`⬆️ +10.3`) | 99.5 → 86.8 (`-12.7`) | 85.7 → 84.2 (`-1.5`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 86.7 → 🟡 ** 77.9** (`-8.8`) | 74.9 → 41.6 (`-33.3`) | 99.5 → 93.9 (`-5.6`) | 85.7 → 98.1 (`⬆️ +12.4`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 7 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 11 → 10 | 86.7 → 🟡 ** 86.0** (`-0.7`) | 74.9 → 72.8 (`-2.1`) | 99.5 | 85.7 | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 86.7 → 🟡 ** 81.6** (`-5.1`) | 74.9 → 65.8 (`-9.1`) | 99.5 → 95.8 (`-3.7`) | 85.7 → 83.1 (`-2.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 86.7 → 🟠 ** 69.4** (`-17.3`) | 74.9 → 46.1 (`-28.8`) | 99.5 → 93.1 (`-6.4`) | 85.7 → 68.9 (`-16.8`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 86.7 → 🟠 ** 64.1** (`-22.6`) | 74.9 → 64.2 (`-10.7`) | 99.5 → 78.8 (`-20.7`) | 85.7 → 49.3 (`-36.4`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 4/4/4zł → 5/5/5zł | 86.7 → 🔴 ** 45.6** (`-41.1`) | 74.9 → 33.4 (`-41.5`) | 99.5 → 61.5 (`-38.0`) | 85.7 → 41.8 (`-43.9`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 4/4/4zł → 3/3/3zł | 86.7 → 🔴 ** 34.9** (`-51.8`) | 74.9 → 59.9 (`-15.0`) | 99.5 → 34.5 (`-65.0`) | 85.7 → 10.2 (`-75.5`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 86.7 → 🔴 ** 30.2** (`-56.5`) | 74.9 → 57.2 (`-17.7`) | 99.5 → 3.2 (`-96.3`) | 85.7 → 0.0 (`-85.7`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (6)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 5.99 Er (1–11) | 1.9% | 27.2% | 0.40 (0–4) | 3.58 (0–18) | 1.89zł (0.0–8.7) | 6.21 (1.0–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 5.99 Er (1–11) | 1.8% | 27.2% | 0.39 (0–3) | 3.58 (0–18) | 1.89zł (0.0–8.7) | 6.20 (1.0–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 6.00 Er (1–12) | 0.9% | 27.2% | 0.40 (0–4) | 3.59 (0–18) | 1.89zł (0.0–8.0) | 6.21 (1.0–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.98 Er (1–11) | 1.8% | 27.1% | 0.41 (0–3) | 3.58 (0–18) | 1.89zł (0.0–8.7) | 6.21 (1.0–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 5.94 Er (1–11) | 2.2% | 27.0% | 0.40 (0–2) | 4.52 (0–21) | 1.91zł (0.0–8.7) | 6.31 (1.0–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 6.29 Er (1–11) | 2.7% | 33.5% | 0.43 (0–3) | 3.65 (0–20) | 2.26zł (0.0–9.0) | 6.20 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 7 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_MAX_ERAS_MINUS1` | 5.97 Er (1–10) | 4.4% | 27.1% | 0.40 (0–4) | 3.57 (0–18) | 1.90zł (0.0–8.3) | 6.20 (1.0–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 5.93 Er (1–11) | 1.5% | 26.8% | 0.46 (0–3) | 3.57 (0–20) | 1.91zł (0.0–7.7) | 6.30 (1.0–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_PLUS1` | 6.06 Er (1–11) | 1.9% | 27.3% | 0.40 (0–4) | 2.65 (0–20) | 1.90zł (0.0–8.0) | 6.08 (1.0–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 6.24 Er (1–11) | 3.2% | 28.3% | 0.29 (0–3) | 3.78 (0–24) | 1.83zł (0.0–7.3) | 6.17 (1.5–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.58 Er (1–11) | 1.2% | 26.0% | 0.53 (0–3) | 3.70 (0–17) | 2.26zł (0.0–9.0) | 6.42 (1.0–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 6.34 Er (1–11) | 3.3% | 28.9% | 0.26 (0–3) | 3.52 (0–19) | 1.58zł (0.0–7.0) | 5.98 (0.8–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.77 Er (1–11) | 1.3% | 21.9% | 0.39 (0–4) | 3.47 (0–19) | 1.67zł (0.0–7.3) | 6.22 (0.8–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.