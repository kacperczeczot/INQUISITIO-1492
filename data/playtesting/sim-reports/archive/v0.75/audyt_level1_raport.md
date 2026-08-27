# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.75

**Wersja Balansu:** `v0.75` | **Data:** 2026-08-16 23:54 | **Przeanalizowano Wariantów:** 13 | **Próba:** 3000 gier/setup | **Czas:** 237.4s
**Wynik Bazy Poziomu 1 (Global):** `🔴 35.5 pkt` | 3p: `34.1 pkt` | 4p: `34.3 pkt` | 5p: `38.1 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (9)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🔴 ** 35.5** | 34.1 | 34.3 | 38.1 | ⚪ OPTYMALNY |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 35.5 → 🔴 ** 49.3** (`⬆️ +13.8`) | 34.1 → 43.1 (`⬆️ +9.0`) | 34.3 → 49.0 (`⬆️ +14.7`) | 38.1 → 55.9 (`⬆️ +17.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 4zł → 5zł | 35.5 → 🔴 ** 46.3** (`⬆️ +10.8`) | 34.1 → 46.2 (`⬆️ +12.1`) | 34.3 → 47.7 (`⬆️ +13.4`) | 38.1 → 44.9 (`⬆️ +6.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 35.5 → 🔴 ** 37.0** (`⬆️ +1.5`) | 34.1 → 36.5 (`⬆️ +2.4`) | 34.3 → 36.0 (`⬆️ +1.7`) | 38.1 → 38.5 (`⬆️ +0.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 12 → 13 | 35.5 → 🔴 ** 35.9** (`⬆️ +0.4`) | 34.1 → 35.4 (`⬆️ +1.3`) | 34.3 → 34.1 (`-0.2`) | 38.1 | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 12 → 11 | 35.5 → 🔴 ** 34.8** (`-0.7`) | 34.1 → 31.9 (`-2.2`) | 34.3 → 34.5 (`⬆️ +0.2`) | 38.1 | 🔴 POGARSZA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 35.5 → 🔴 ** 34.7** (`-0.8`) | 34.1 → 30.8 (`-3.3`) | 34.3 | 38.1 → 38.9 (`⬆️ +0.8`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 35.5 → 🔴 ** 33.4** (`-2.1`) | 34.1 → 31.6 (`-2.5`) | 34.3 → 34.7 (`⬆️ +0.4`) | 38.1 → 33.8 (`-4.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 35.5 → 🔴 ** 31.7** (`-3.8`) | 34.1 → 34.8 (`⬆️ +0.7`) | 34.3 → 31.1 (`-3.2`) | 38.1 → 29.2 (`-8.9`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 4 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/8 → 5/6/7 | 35.5 → 🔴 ** 33.3** (`-2.2`) | 34.1 → 34.0 (`-0.1`) | 34.3 → 32.7 (`-1.6`) | 38.1 → 33.2 (`-4.9`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 35.5 → 🔴 ** 31.1** (`-4.4`) | 34.1 → 30.6 (`-3.5`) | 34.3 → 31.0 (`-3.3`) | 38.1 → 31.8 (`-6.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 4zł → 3zł | 35.5 → 🔴 ** 26.8** (`-8.7`) | 34.1 → 28.0 (`-6.1`) | 34.3 → 26.7 (`-7.6`) | 38.1 → 25.8 (`-12.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 35.5 → 🔴 ** 21.6** (`-13.9`) | 34.1 → 26.4 (`-7.7`) | 34.3 → 21.0 (`-13.3`) | 38.1 → 17.4 (`-20.7`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (9)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 6.10 Er (1–12) | 4.5% | 6.5% | 1.44 (0–4) | 3.08 (0–21) | 2.19zł (0.0–8.3) | 5.79 (0.7–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 6.42 Er (1–12) | 5.3% | 7.1% | 1.50 (0–4) | 3.15 (0–22) | 2.59zł (0.0–9.3) | 5.80 (0.0–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.94 Er (1–12) | 3.8% | 5.5% | 1.38 (0–4) | 3.07 (0–24) | 2.61zł (0.0–9.0) | 5.84 (0.7–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_PLUS1` | 6.06 Er (1–12) | 4.2% | 6.9% | 1.45 (0–4) | 2.11 (0–20) | 2.05zł (0.0–8.0) | 5.75 (0.7–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 6.13 Er (1–13) | 3.1% | 6.5% | 1.44 (0–4) | 3.10 (0–23) | 2.18zł (0.0–8.3) | 5.79 (0.7–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 6.05 Er (1–11) | 6.7% | 6.5% | 1.43 (0–3) | 3.04 (0–21) | 2.19zł (0.0–8.0) | 5.78 (0.7–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.88 Er (1–12) | 3.5% | 6.9% | 1.98 (0–6) | 3.19 (0–24) | 2.14zł (0.0–8.0) | 5.99 (0.8–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 6.28 Er (1–12) | 6.8% | 6.8% | 1.38 (0–4) | 3.16 (0–24) | 2.13zł (0.0–8.3) | 5.60 (0.3–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 6.22 Er (1–12) | 5.4% | 6.3% | 1.03 (0–3) | 2.96 (0–22) | 2.24zł (0.0–8.3) | 5.61 (0.7–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 4 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_THRESHOLD_MINUS1` | 6.12 Er (1–12) | 4.4% | 6.0% | 1.41 (0–4) | 4.04 (0–26) | 2.35zł (0.0–8.3) | 5.78 (0.7–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 5.98 Er (1–12) | 3.4% | 6.4% | 1.44 (0–4) | 3.02 (0–25) | 2.19zł (0.0–8.3) | 5.99 (0.5–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 6.18 Er (1–12) | 4.9% | 8.9% | 1.47 (0–4) | 2.89 (0–22) | 1.80zł (0.0–8.0) | 5.63 (0.3–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.72 Er (1–12) | 3.6% | 6.8% | 1.35 (0–4) | 2.80 (0–20) | 1.83zł (0.0–7.7) | 5.64 (0.3–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.