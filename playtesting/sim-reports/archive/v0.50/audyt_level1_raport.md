# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.50

**Wersja Balansu:** `v0.50` | **Data:** 2026-08-16 13:08 | **Przeanalizowano Wariantów:** 13 | **Próba:** 3000 gier/setup | **Czas:** 110.96s
**Wynik Bazy Poziomu 1 (Global):** `🟡 85.6 pkt` | 3p: `82.4 pkt` | 4p: `88.8 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (9)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🟡 ** 85.6** | 82.4 | 88.8 | 0.0 | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 85.6 → 🟡 ** 86.8** (`⬆️ +1.2`) | 82.4 → 81.3 (`-1.1`) | 88.8 → 92.3 (`⬆️ +3.5`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 11 → 12 | 85.6 → 🟡 ** 85.7** (`⬆️ +0.1`) | 82.4 → 82.6 (`⬆️ +0.2`) | 88.8 | 0.0 | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 85.6 → 🟡 ** 81.1** (`-4.5`) | 82.4 → 84.0 (`⬆️ +1.6`) | 88.8 → 78.2 (`-10.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 85.6 → 🟡 ** 77.5** (`-8.1`) | 82.4 → 85.8 (`⬆️ +3.4`) | 88.8 → 69.3 (`-19.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 85.6 → 🟠 ** 71.0** (`-14.6`) | 82.4 → 50.5 (`-31.9`) | 88.8 → 97.3 (`⬆️ +8.5`) | 0.0 → 65.2 (`⬆️ +65.2`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/8 → 5/6/7 | 85.6 → 🔴 ** 55.5** (`-30.1`) | 82.4 → 89.9 (`⬆️ +7.5`) | 88.8 → 21.0 (`-67.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 85.6 → 🔴 ** 49.2** (`-36.4`) | 82.4 → 65.8 (`-16.6`) | 88.8 → 53.6 (`-35.2`) | 0.0 → 28.2 (`⬆️ +28.2`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 4/4/4zł → 5/5/5zł | 85.6 → 🔴 ** 25.7** (`-59.9`) | 82.4 → 34.5 (`-47.9`) | 88.8 → 28.0 (`-60.8`) | 0.0 → 14.7 (`⬆️ +14.7`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 4 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 11 → 10 | 85.6 → 🟡 ** 85.3** (`-0.3`) | 82.4 → 81.8 (`-0.6`) | 88.8 | 0.0 | ⚪ OPTYMALNY |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 85.6 → 🟠 ** 69.0** (`-16.6`) | 82.4 → 49.2 (`-33.2`) | 88.8 → 88.7 (`-0.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 4/4/4zł → 3/3/3zł | 85.6 → 🔴 ** 49.7** (`-35.9`) | 82.4 → 62.4 (`-20.0`) | 88.8 → 37.0 (`-51.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 85.6 → 🔴 ** 29.9** (`-55.7`) | 82.4 → 54.5 (`-27.9`) | 88.8 → 5.4 (`-83.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (9)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 5.80 Er (1–11) | 1.5% | 27.4% | 0.56 (0–3) | 3.72 (0–20) | 1.88zł (0.0–8.7) | 6.34 (1.0–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 5.80 Er (1–11) | 1.5% | 27.4% | 0.55 (0–3) | 3.72 (0–20) | 1.88zł (0.0–8.7) | 6.33 (1.0–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 5.80 Er (1–12) | 0.6% | 27.4% | 0.56 (0–3) | 3.72 (0–20) | 1.87zł (0.0–8.0) | 6.34 (1.0–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.79 Er (1–11) | 1.5% | 27.4% | 0.58 (0–3) | 3.72 (0–20) | 1.88zł (0.0–8.7) | 6.35 (1.0–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 5.73 Er (1–11) | 1.2% | 27.1% | 0.61 (0–3) | 3.70 (0–20) | 1.88zł (0.0–8.0) | 6.44 (1.0–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_PLUS1` | 5.93 Er (1–11) | 1.7% | 27.7% | 0.57 (0–4) | 2.69 (0–20) | 1.90zł (0.0–8.0) | 6.24 (1.0–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 5.68 Er (1–11) | 1.6% | 27.1% | 0.55 (0–3) | 4.68 (0–21) | 1.87zł (0.0–8.7) | 6.41 (1.0–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 6.04 Er (1–11) | 2.6% | 28.7% | 0.46 (0–2) | 3.91 (0–24) | 1.82zł (0.0–7.7) | 6.31 (1.0–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.51 Er (1–11) | 1.0% | 25.4% | 0.60 (0–3) | 3.80 (0–20) | 2.25zł (0.0–9.0) | 6.52 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 4 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_MAX_ERAS_MINUS1` | 5.78 Er (1–10) | 3.7% | 27.4% | 0.56 (0–3) | 3.71 (0–20) | 1.89zł (0.0–8.3) | 6.34 (1.0–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 6.09 Er (1–11) | 2.2% | 33.6% | 0.56 (0–3) | 3.74 (0–20) | 2.20zł (0.0–9.3) | 6.28 (1.0–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_START_GOLD_MINUS1` | 6.27 Er (1–11) | 3.0% | 27.9% | 0.45 (0–3) | 3.55 (0–19) | 1.59zł (0.0–8.0) | 6.13 (0.7–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.58 Er (1–11) | 1.0% | 22.5% | 0.57 (0–3) | 3.59 (0–21) | 1.67zł (0.0–7.7) | 6.39 (0.7–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.