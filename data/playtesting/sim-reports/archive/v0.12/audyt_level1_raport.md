[Strona główna](../../../../../README.md) > [v0.12](README.md) > [audyt_level1_raport](audyt_level1_raport.md)

---

# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.12

**Wersja Balansu:** `v0.12` | **Data:** 2026-08-14 11:29 | **Przeanalizowano Wariantów:** 13 | **Próba:** 2000 gier/setup | **Czas:** 52.39s
**Wynik Bazy Poziomu 1 (Global):** `🟢 58.3 pkt` | 3p: `82.8 pkt` | 4p: `55.1 pkt` | 5p: `37.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🟢 ** 58.3** | 82.8 | 55.1 | 37.0 | ⚪ OPTYMALNY |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/7 → 7/8/8 | 58.3 → 🟡 ** 41.7** (`-16.6`) | 82.8 → 60.9 (`-21.9`) | 55.1 → 28.6 (`-26.5`) | 37.0 → 35.7 (`-1.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/7 → 5/6/6 | 58.3 → 🟡 ** 41.0** (`-17.3`) | 82.8 → 69.1 (`-13.7`) | 55.1 → 25.4 (`-29.7`) | 37.0 → 28.6 (`-8.4`) | 🔴 POGARSZA GLOBALNIE |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 9 → 10 | 58.3 → 🟢 ** 59.3** (`⬆️ +1.0`) | 82.8 → 85.6 (`⬆️ +2.8`) | 55.1 → 55.2 (`⬆️ +0.1`) | 37.0 | 🟢 POPRAWIA GLOBALNIE |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 9 → 8 | 58.3 → 🟢 ** 53.9** (`-4.4`) | 82.8 → 70.9 (`-11.9`) | 55.1 → 54.4 (`-0.7`) | 37.0 → 36.4 (`-0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 3/3/2zł → 4/4/3zł | 58.3 → 🟢 ** 60.4** (`⬆️ +2.1`) | 82.8 → 80.2 (`-2.6`) | 55.1 → 40.5 (`-14.6`) | 37.0 → 0.0 (`-37.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 3/3/2zł → 2/2/1zł | 58.3 → 🟡 ** 27.3** (`-31.0`) | 82.8 → 43.0 (`-39.8`) | 55.1 → 11.6 (`-43.5`) | 37.0 → 0.0 (`-37.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 58.3 → 🟢 ** 55.8** (`-2.5`) | 82.8 → 78.2 (`-4.6`) | 55.1 → 56.0 (`⬆️ +0.9`) | 37.0 → 33.2 (`-3.8`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 58.3 → 🟡 ** 28.5** (`-29.8`) | 82.8 → 51.3 (`-31.5`) | 55.1 → 19.9 (`-35.2`) | 37.0 → 14.3 (`-22.7`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5/5/5 → 6/6/6 | 58.3 → 🟡 ** 40.8** (`-17.5`) | 82.8 → 68.6 (`-14.2`) | 55.1 → 12.9 (`-42.2`) | 37.0 → 0.0 (`-37.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5/5/5 → 4/4/4 | 58.3 → 🟢 ** 55.9** (`-2.4`) | 82.8 → 69.8 (`-13.0`) | 55.1 → 41.5 (`-13.6`) | 37.0 → 56.3 (`⬆️ +19.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 58.3 → 🟢 ** 57.9** (`-0.4`) | 82.8 | 55.1 → 52.3 (`-2.8`) | 37.0 → 38.5 (`⬆️ +1.5`) | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 58.3 → 🟢 ** 57.6** (`-0.7`) | 82.8 → 77.9 (`-4.9`) | 55.1 → 56.3 (`⬆️ +1.2`) | 37.0 → 38.6 (`⬆️ +1.6`) | 🔴 POGARSZA GLOBALNIE |

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 5.57 Er (1–9) | 3.4% | 28.6% | 1.03 (0–3) | 3.71 (0–20) | 0.52zł (0.0–2.7) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_PLUS1` | 5.74 Er (1–9) | 4.0% | 29.0% | 1.06 (0–4) | 2.60 (0–16) | 0.53zł (0.0–2.7) | 6.16 (0.7–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 5.38 Er (1–9) | 3.0% | 28.0% | 1.00 (0–4) | 4.70 (0–19) | 0.52zł (0.0–2.8) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 5.58 Er (1–10) | 1.2% | 28.6% | 1.03 (0–3) | 3.72 (0–22) | 0.52zł (0.0–3.0) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 5.53 Er (1–8) | 7.4% | 28.5% | 1.03 (0–3) | 3.68 (0–18) | 0.52zł (0.0–2.7) | 6.25 (0.7–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.29 Er (1–9) | 2.2% | 25.8% | 1.04 (0–3) | 3.72 (0–18) | 0.74zł (0.0–3.7) | 6.30 (1.0–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 5.97 Er (1–9) | 5.7% | 31.3% | 0.95 (0–3) | 3.51 (0–18) | 0.43zł (0.0–2.5) | 6.13 (0.8–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_AGENTS_PLUS1` | 5.51 Er (1–9) | 3.2% | 28.4% | 1.06 (0–4) | 3.75 (0–17) | 0.52zł (0.0–2.7) | 6.44 (1.3–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 5.73 Er (1–9) | 4.3% | 29.1% | 0.99 (0–3) | 3.66 (0–17) | 0.53zł (0.0–2.7) | 6.00 (0.7–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.43 Er (1–9) | 3.0% | 25.7% | 1.07 (0–3) | 3.67 (0–18) | 0.47zł (0.0–2.7) | 6.31 (1.0–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 5.80 Er (1–9) | 3.8% | 34.3% | 1.03 (0–4) | 3.63 (0–17) | 0.73zł (0.0–3.0) | 6.14 (0.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 5.57 Er (1–9) | 3.4% | 28.6% | 1.02 (0–4) | 3.71 (0–20) | 0.52zł (0.0–2.7) | 6.25 (0.7–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.55 Er (1–9) | 3.3% | 28.5% | 1.06 (0–4) | 3.70 (0–18) | 0.52zł (0.0–2.7) | 6.27 (0.7–10.0) | 🟢 W NORMIE |

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.