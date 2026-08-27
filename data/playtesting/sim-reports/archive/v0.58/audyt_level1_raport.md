[Strona główna](../../../../../README.md) > [v0.58](README.md) > [audyt_level1_raport](audyt_level1_raport.md)

---

# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.58

**Wersja Balansu:** `v0.58` | **Data:** 2026-08-16 16:18 | **Przeanalizowano Wariantów:** 13 | **Próba:** 3000 gier/setup | **Czas:** 142.43s
**Wynik Bazy Poziomu 1 (Global):** `🟠 70.6 pkt` | 3p: `76.6 pkt` | 4p: `79.6 pkt` | 5p: `55.5 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (8)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🟠 ** 70.6** | 76.6 | 79.6 | 55.5 | ⚪ OPTYMALNY |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 70.6 → 🟠 ** 72.8** (`⬆️ +2.2`) | 76.6 → 65.5 (`-11.1`) | 79.6 → 82.3 (`⬆️ +2.7`) | 55.5 → 70.6 (`⬆️ +15.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 70.6 → 🟠 ** 71.4** (`⬆️ +0.8`) | 76.6 → 69.2 (`-7.4`) | 79.6 → 80.3 (`⬆️ +0.7`) | 55.5 → 64.6 (`⬆️ +9.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 11 → 12 | 🟠 ** 70.6** | 76.6 → 76.5 (`-0.1`) | 79.6 → 79.7 (`⬆️ +0.1`) | 55.5 | ⚪ OPTYMALNY |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 70.6 → 🟠 ** 70.1** (`-0.5`) | 76.6 → 78.3 (`⬆️ +1.7`) | 79.6 → 80.3 (`⬆️ +0.7`) | 55.5 → 51.7 (`-3.8`) | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 70.6 → 🟠 ** 67.1** (`-3.5`) | 76.6 → 65.1 (`-11.5`) | 79.6 → 72.2 (`-7.4`) | 55.5 → 64.1 (`⬆️ +8.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/8 → 5/6/7 | 70.6 → 🟠 ** 66.2** (`-4.4`) | 76.6 → 81.6 (`⬆️ +5.0`) | 79.6 → 70.1 (`-9.5`) | 55.5 → 46.9 (`-8.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 70.6 → 🔴 ** 58.0** (`-12.6`) | 76.6 → 78.8 (`⬆️ +2.2`) | 79.6 → 59.1 (`-20.5`) | 55.5 → 36.1 (`-19.4`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 5 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 11 → 10 | 70.6 → 🟠 ** 68.7** (`-1.9`) | 76.6 → 71.2 (`-5.4`) | 79.6 → 79.3 (`-0.3`) | 55.5 | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 70.6 → 🔴 ** 57.9** (`-12.7`) | 76.6 → 63.2 (`-13.4`) | 79.6 → 62.2 (`-17.4`) | 55.5 → 48.2 (`-7.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 4zł → 5zł | 70.6 → 🔴 ** 57.2** (`-13.4`) | 76.6 → 64.3 (`-12.3`) | 79.6 → 60.5 (`-19.1`) | 55.5 → 46.7 (`-8.8`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 4zł → 3zł | 70.6 → 🔴 ** 54.6** (`-16.0`) | 76.6 → 65.7 (`-10.9`) | 79.6 → 54.8 (`-24.8`) | 55.5 → 43.3 (`-12.2`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 70.6 → 🔴 ** 54.6** (`-16.0`) | 76.6 → 70.7 (`-5.9`) | 79.6 → 53.8 (`-25.8`) | 55.5 → 39.3 (`-16.2`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (8)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 5.95 Er (2–11) | 1.7% | 26.9% | 1.48 (0–4) | 3.64 (0–21) | 1.98zł (0.0–8.7) | 6.50 (1.0–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 6.19 Er (2–11) | 2.3% | 33.3% | 1.56 (0–4) | 3.68 (0–24) | 2.31zł (0.0–9.0) | 6.47 (1.0–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_THRESHOLD_PLUS1` | 5.99 Er (2–11) | 1.8% | 27.0% | 1.50 (0–4) | 2.74 (0–19) | 1.98zł (0.0–10.0) | 6.38 (1.0–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 5.95 Er (2–12) | 0.7% | 26.9% | 1.48 (0–4) | 3.64 (0–21) | 1.98zł (0.0–8.7) | 6.50 (1.0–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 5.79 Er (2–11) | 1.3% | 26.4% | 1.48 (0–4) | 3.55 (0–24) | 1.98zł (0.0–9.7) | 6.64 (1.0–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 6.00 Er (2–11) | 2.0% | 27.0% | 1.11 (0–3) | 3.57 (0–20) | 1.99zł (0.0–9.0) | 6.38 (1.0–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 5.91 Er (1–11) | 1.7% | 26.8% | 1.45 (0–4) | 4.53 (0–23) | 1.98zł (0.0–8.7) | 6.60 (1.0–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.81 Er (2–11) | 1.5% | 26.6% | 2.07 (0–6) | 3.69 (0–21) | 1.96zł (0.0–8.3) | 6.66 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 5 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_MAX_ERAS_MINUS1` | 5.93 Er (2–10) | 4.4% | 26.9% | 1.47 (0–4) | 3.62 (0–21) | 1.99zł (0.0–8.3) | 6.50 (1.0–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 6.18 Er (2–11) | 3.0% | 28.1% | 1.41 (0–4) | 3.79 (0–21) | 1.94zł (0.0–8.7) | 6.39 (0.8–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.53 Er (1–11) | 1.0% | 25.8% | 1.49 (0–4) | 3.73 (0–21) | 2.34zł (0.0–9.0) | 6.71 (1.0–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 6.24 Er (2–11) | 3.0% | 28.5% | 1.50 (0–4) | 3.57 (0–19) | 1.65zł (0.0–8.3) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.76 Er (2–11) | 1.3% | 21.9% | 1.43 (0–4) | 3.51 (0–19) | 1.81zł (0.0–8.7) | 6.53 (0.7–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.