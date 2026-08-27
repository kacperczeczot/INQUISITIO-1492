[Strona główna](../../../../../README.md) > [v0.57](README.md) > [audyt_level1_raport](audyt_level1_raport.md)

---

# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.57

**Wersja Balansu:** `v0.57` | **Data:** 2026-08-16 15:35 | **Przeanalizowano Wariantów:** 13 | **Próba:** 3000 gier/setup | **Czas:** 107.42s
**Wynik Bazy Poziomu 1 (Global):** `🔴 51.6 pkt` | 3p: `66.8 pkt` | 4p: `49.4 pkt` | 5p: `38.5 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (7)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🔴 ** 51.6** | 66.8 | 49.4 | 38.5 | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 51.6 → 🟠 ** 63.3** (`⬆️ +11.7`) | 66.8 → 72.2 (`⬆️ +5.4`) | 49.4 → 67.8 (`⬆️ +18.4`) | 38.5 → 49.8 (`⬆️ +11.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 51.6 → 🔴 ** 57.0** (`⬆️ +5.4`) | 66.8 → 69.1 (`⬆️ +2.3`) | 49.4 → 57.8 (`⬆️ +8.4`) | 38.5 → 44.1 (`⬆️ +5.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 51.6 → 🔴 ** 55.8** (`⬆️ +4.2`) | 66.8 → 64.3 (`-2.5`) | 49.4 → 55.0 (`⬆️ +5.6`) | 38.5 → 48.0 (`⬆️ +9.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 51.6 → 🔴 ** 53.0** (`⬆️ +1.4`) | 66.8 → 63.2 (`-3.6`) | 49.4 → 52.0 (`⬆️ +2.6`) | 38.5 → 43.8 (`⬆️ +5.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 11 → 10 | 51.6 → 🔴 ** 51.5** (`-0.1`) | 66.8 → 66.5 (`-0.3`) | 49.4 → 49.5 (`⬆️ +0.1`) | 38.5 | ⚪ OPTYMALNY |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 4/4/4zł → 5/5/5zł | 51.6 → 🔴 ** 46.2** (`-5.4`) | 66.8 → 54.7 (`-12.1`) | 49.4 → 44.6 (`-4.8`) | 38.5 → 39.4 (`⬆️ +0.9`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 6 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 11 → 12 | 51.6 → 🔴 ** 51.5** (`-0.1`) | 66.8 → 66.7 (`-0.1`) | 49.4 | 38.5 | ⚪ OPTYMALNY |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/8 → 5/6/7 | 51.6 → 🔴 ** 45.8** (`-5.8`) | 66.8 → 60.2 (`-6.6`) | 49.4 → 41.2 (`-8.2`) | 38.5 → 36.1 (`-2.4`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 51.6 → 🔴 ** 40.9** (`-10.7`) | 66.8 → 55.9 (`-10.9`) | 49.4 → 39.3 (`-10.1`) | 38.5 → 27.4 (`-11.1`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 51.6 → 🔴 ** 37.7** (`-13.9`) | 66.8 → 53.4 (`-13.4`) | 49.4 → 35.8 (`-13.6`) | 38.5 → 24.0 (`-14.5`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 4/4/4zł → 3/3/3zł | 51.6 → 🔴 ** 36.3** (`-15.3`) | 66.8 → 46.6 (`-20.2`) | 49.4 → 33.9 (`-15.5`) | 38.5 → 28.5 (`-10.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 51.6 → 🔴 ** 32.7** (`-18.9`) | 66.8 → 45.5 (`-21.3`) | 49.4 → 28.1 (`-21.3`) | 38.5 → 24.4 (`-14.1`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (7)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 1.91zł (0.0–8.3) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 5.57 Er (1–11) | 1.0% | 25.6% | 1.04 (0–3) | 3.17 (0–20) | 1.92zł (0.0–9.0) | 6.17 (1.0–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_PLUS1` | 5.52 Er (1–11) | 0.9% | 25.6% | 1.40 (0–4) | 2.36 (0–19) | 1.92zł (0.0–7.7) | 6.15 (1.0–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 5.69 Er (1–11) | 1.6% | 26.7% | 1.32 (0–4) | 3.34 (0–21) | 1.87zł (0.0–8.3) | 6.16 (0.8–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 5.69 Er (1–11) | 1.1% | 31.9% | 1.45 (0–4) | 3.22 (0–23) | 2.21zł (0.0–9.0) | 6.19 (1.0–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_MAX_ERAS_MINUS1` | 5.46 Er (1–10) | 2.3% | 25.4% | 1.37 (0–4) | 3.17 (0–20) | 1.92zł (0.0–8.3) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.09 Er (1–11) | 0.5% | 24.2% | 1.40 (0–4) | 3.25 (0–21) | 2.28zł (0.0–9.0) | 6.46 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 6 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_MAX_ERAS_PLUS1` | 5.47 Er (1–12) | 0.3% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 1.91zł (0.0–8.7) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 5.40 Er (1–11) | 0.8% | 25.2% | 1.34 (0–4) | 3.99 (0–23) | 1.91zł (0.0–8.3) | 6.32 (1.0–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.30 Er (1–11) | 0.6% | 20.6% | 1.33 (0–4) | 3.07 (0–19) | 1.78zł (0.0–7.7) | 6.29 (0.7–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 5.32 Er (1–11) | 0.6% | 24.8% | 1.37 (0–4) | 3.08 (0–23) | 1.91zł (0.0–8.7) | 6.37 (1.0–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 5.68 Er (1–11) | 1.4% | 27.0% | 1.38 (0–4) | 3.06 (0–19) | 1.57zł (0.0–8.0) | 6.03 (0.7–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.25 Er (1–11) | 0.7% | 24.8% | 1.91 (0–6) | 3.15 (0–21) | 1.88zł (0.0–8.3) | 6.33 (1.0–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.