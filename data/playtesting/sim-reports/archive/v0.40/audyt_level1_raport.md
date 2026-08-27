# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.40

**Wersja Balansu:** `v0.40` | **Data:** 2026-08-15 23:30 | **Przeanalizowano Wariantów:** 13 | **Próba:** 10000 gier/setup | **Czas:** 770.21s
**Wynik Bazy Poziomu 1 (Global):** `🔴 30.8 pkt` | 3p: `44.3 pkt` | 4p: `17.3 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (8)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🔴 ** 30.8** | 44.3 | 17.3 | 0.0 | ⚪ OPTYMALNY |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 3/3/2zł → 4/4/3zł | 30.8 → 🟡 ** 85.0** (`⬆️ +54.2`) | 44.3 → 95.6 (`⬆️ +51.3`) | 17.3 → 74.4 (`⬆️ +57.1`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 30.8 → 🟠 ** 61.2** (`⬆️ +30.4`) | 44.3 → 59.7 (`⬆️ +15.4`) | 17.3 → 62.7 (`⬆️ +45.4`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 30.8 → 🔴 ** 39.4** (`⬆️ +8.6`) | 44.3 → 39.4 (`-4.9`) | 17.3 → 0.0 (`-17.3`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/8 → 5/6/7 | 30.8 → 🔴 ** 37.9** (`⬆️ +7.1`) | 44.3 → 56.0 (`⬆️ +11.7`) | 17.3 → 19.7 (`⬆️ +2.4`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 30.8 → 🔴 ** 34.9** (`⬆️ +4.1`) | 44.3 → 49.2 (`⬆️ +4.9`) | 17.3 → 20.6 (`⬆️ +3.3`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 10 → 11 | 30.8 → 🔴 ** 34.8** (`⬆️ +4.0`) | 44.3 → 52.0 (`⬆️ +7.7`) | 17.3 → 17.5 (`⬆️ +0.2`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 30.8 → 🔴 ** 31.0** (`⬆️ +0.2`) | 44.3 → 44.7 (`⬆️ +0.4`) | 17.3 | 0.0 | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 5 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 30.8 → 🔴 ** 30.7** (`-0.1`) | 44.3 → 44.1 (`-0.2`) | 17.3 | 0.0 | ⚪ OPTYMALNY |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 3/3/2zł → 2/2/1zł | 30.8 → 🔴 ** 30.2** (`-0.6`) | 44.3 → 30.2 (`-14.1`) | 17.3 → 0.0 (`-17.3`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 10 → 9 | 30.8 → 🔴 ** 25.1** (`-5.7`) | 44.3 → 34.9 (`-9.4`) | 17.3 → 15.3 (`-2.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 30.8 → 🔴 ** 23.6** (`-7.2`) | 44.3 → 23.6 (`-20.7`) | 17.3 → 0.0 (`-17.3`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 30.8 → 🔴 ** 21.6** (`-9.2`) | 44.3 → 31.6 (`-12.7`) | 17.3 → 11.7 (`-5.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (8)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 6.25 Er (1–10) | 4.0% | 26.7% | 0.45 (0–3) | 3.23 (0–19) | 1.24zł (0.0–7.0) | 5.87 (0.0–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.74 Er (1–10) | 2.0% | 25.7% | 0.56 (0–3) | 3.57 (0–21) | 1.53zł (0.0–7.7) | 6.08 (0.6–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 6.50 Er (1–10) | 5.9% | 32.9% | 0.49 (0–3) | 3.29 (0–20) | 1.52zł (0.0–7.3) | 5.88 (0.0–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_THRESHOLD_PLUS1` | 6.37 Er (1–10) | 4.5% | 27.0% | 0.46 (0–3) | 2.33 (0–18) | 1.26zł (0.0–7.7) | 5.78 (0.0–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 6.11 Er (1–10) | 3.4% | 26.3% | 0.44 (0–3) | 4.08 (0–20) | 1.22zł (0.0–7.0) | 5.94 (0.0–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 6.17 Er (1–10) | 3.3% | 26.3% | 0.51 (0–4) | 3.21 (0–19) | 1.25zł (0.0–7.7) | 5.97 (0.3–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 6.26 Er (1–11) | 1.6% | 26.7% | 0.45 (0–3) | 3.24 (0–19) | 1.23zł (0.0–6.7) | 5.88 (0.0–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 6.24 Er (1–10) | 3.9% | 26.6% | 0.46 (0–4) | 3.22 (0–19) | 1.24zł (0.0–7.0) | 5.88 (0.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 5 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 6.25 Er (1–10) | 4.0% | 26.7% | 0.44 (0–3) | 3.23 (0–19) | 1.24zł (0.0–7.0) | 5.87 (0.0–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 6.51 Er (1–10) | 6.2% | 28.8% | 0.38 (0–3) | 2.98 (0–21) | 1.00zł (0.0–6.3) | 5.67 (0.0–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 6.21 Er (1–9) | 9.4% | 26.6% | 0.45 (0–3) | 3.20 (0–18) | 1.26zł (0.0–6.3) | 5.86 (0.0–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 6.01 Er (1–10) | 3.0% | 21.4% | 0.43 (0–4) | 2.99 (0–20) | 1.06zł (0.0–5.7) | 5.82 (0.6–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 6.49 Er (1–10) | 6.3% | 27.8% | 0.34 (0–3) | 3.37 (0–20) | 1.18zł (0.0–6.7) | 5.84 (0.3–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.