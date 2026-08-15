# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.40

**Wersja Balansu:** `v0.40` | **Data:** 2026-08-15 22:48 | **Przeanalizowano Wariantów:** 13 | **Próba:** 500 gier/setup | **Czas:** 32.26s
**Wynik Bazy Poziomu 1 (Global):** `🔴 34.0 pkt` | 3p: `51.3 pkt` | 4p: `16.6 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (8)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🔴 ** 34.0** | 51.3 | 16.6 | 0.0 | ⚪ OPTYMALNY |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 3/3/2zł → 4/4/3zł | 34.0 → 🟡 ** 81.2** (`⬆️ +47.2`) | 51.3 → 93.4 (`⬆️ +42.1`) | 16.6 → 69.0 (`⬆️ +52.4`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 34.0 → 🟠 ** 60.2** (`⬆️ +26.2`) | 51.3 → 72.3 (`⬆️ +21.0`) | 16.6 → 64.8 (`⬆️ +48.2`) | 0.0 → 43.6 (`⬆️ +43.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 34.0 → 🔴 ** 38.7** (`⬆️ +4.7`) | 51.3 → 52.5 (`⬆️ +1.2`) | 16.6 → 24.9 (`⬆️ +8.3`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 10 → 11 | 34.0 → 🔴 ** 35.4** (`⬆️ +1.4`) | 51.3 → 54.2 (`⬆️ +2.9`) | 16.6 | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 34.0 → 🔴 ** 34.5** (`⬆️ +0.5`) | 51.3 → 51.1 (`-0.2`) | 16.6 → 18.0 (`⬆️ +1.4`) | 0.0 | ⚪ OPTYMALNY |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/8 → 5/6/7 | 34.0 → 🔴 ** 31.6** (`-2.4`) | 51.3 → 55.9 (`⬆️ +4.6`) | 16.6 → 7.2 (`-9.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 10 → 9 | 34.0 → 🔴 ** 29.2** (`-4.8`) | 51.3 → 41.7 (`-9.6`) | 16.6 → 16.8 (`⬆️ +0.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 5 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 3/3/2zł → 2/2/1zł | 34.0 → 🔴 ** 33.9** (`-0.1`) | 51.3 → 33.9 (`-17.4`) | 16.6 → 0.0 (`-16.6`) | 0.0 | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 34.0 → 🔴 ** 33.5** (`-0.5`) | 51.3 → 50.9 (`-0.4`) | 16.6 → 16.0 (`-0.6`) | 0.0 | ⚪ OPTYMALNY |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 34.0 → 🔴 ** 29.3** (`-4.7`) | 51.3 → 29.3 (`-22.0`) | 16.6 → 0.0 (`-16.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 34.0 → 🔴 ** 24.6** (`-9.4`) | 51.3 → 37.1 (`-14.2`) | 16.6 → 12.2 (`-4.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 34.0 → 🔴 ** 22.1** (`-11.9`) | 51.3 → 42.4 (`-8.9`) | 16.6 → 1.8 (`-14.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (8)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 6.12 Er (1–10) | 3.5% | 26.4% | 0.47 (0–3) | 3.31 (0–16) | 1.27zł (0.0–6.0) | 5.93 (0.8–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.69 Er (1–10) | 1.8% | 25.5% | 0.57 (0–3) | 3.57 (0–16) | 1.57zł (0.0–7.3) | 6.13 (0.8–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 6.39 Er (1–10) | 5.4% | 32.7% | 0.49 (0–3) | 3.38 (0–17) | 1.54zł (0.0–6.7) | 5.94 (0.7–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_AGENTS_PLUS1` | 6.03 Er (1–10) | 2.9% | 26.0% | 0.53 (0–3) | 3.28 (0–15) | 1.29zł (0.0–6.7) | 6.02 (0.8–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 6.13 Er (1–11) | 1.5% | 26.4% | 0.47 (0–3) | 3.32 (0–16) | 1.26zł (0.0–5.7) | 5.93 (0.8–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 6.11 Er (1–10) | 3.6% | 26.4% | 0.48 (0–3) | 3.31 (0–16) | 1.27zł (0.0–6.0) | 5.93 (0.8–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 5.95 Er (1–10) | 3.1% | 26.0% | 0.46 (0–3) | 4.14 (0–20) | 1.25zł (0.0–5.3) | 5.99 (0.8–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 6.08 Er (1–9) | 8.9% | 26.3% | 0.47 (0–3) | 3.28 (0–16) | 1.28zł (0.0–5.7) | 5.91 (0.8–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 5 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_START_GOLD_MINUS1` | 6.38 Er (1–10) | 4.9% | 28.6% | 0.39 (0–3) | 3.05 (0–16) | 1.01zł (0.0–4.7) | 5.72 (0.7–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 6.12 Er (1–10) | 3.6% | 26.4% | 0.46 (0–3) | 3.31 (0–16) | 1.27zł (0.0–6.0) | 5.92 (0.8–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.92 Er (1–10) | 2.6% | 21.3% | 0.44 (0–3) | 3.08 (0–14) | 1.09zł (0.0–4.7) | 5.89 (0.8–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 6.39 Er (1–10) | 5.6% | 27.6% | 0.35 (0–3) | 3.42 (0–15) | 1.20zł (0.0–5.7) | 5.88 (0.7–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_PLUS1` | 6.25 Er (1–10) | 3.6% | 26.7% | 0.48 (0–3) | 2.42 (0–16) | 1.28zł (0.0–6.7) | 5.86 (0.8–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.