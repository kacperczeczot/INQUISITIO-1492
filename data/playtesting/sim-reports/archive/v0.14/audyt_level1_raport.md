# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.14

**Wersja Balansu:** `v0.14` | **Data:** 2026-08-14 11:55 | **Przeanalizowano Wariantów:** 13 | **Próba:** 2000 gier/setup | **Czas:** 51.52s
**Wynik Bazy Poziomu 1 (Global):** `🟢 77.6 pkt` | 3p: `90.5 pkt` | 4p: `55.9 pkt` | 5p: `86.4 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🟢 ** 77.6** | 90.5 | 55.9 | 86.4 | ⚪ OPTYMALNY |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 77.6 → 🟢 ** 67.8** (`-9.8`) | 90.5 → 73.6 (`-16.9`) | 55.9 → 62.5 (`⬆️ +6.6`) | 86.4 → 67.3 (`-19.1`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/8 → 5/6/7 | 77.6 → 🟢 ** 61.2** (`-16.4`) | 90.5 → 71.4 (`-19.1`) | 55.9 → 29.2 (`-26.7`) | 86.4 → 82.9 (`-3.5`) | 🔴 POGARSZA GLOBALNIE |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 9 → 10 | 77.6 → 🟢 ** 78.2** (`⬆️ +0.6`) | 90.5 → 92.5 (`⬆️ +2.0`) | 55.9 → 55.8 (`-0.1`) | 86.4 | 🟢 POPRAWIA GLOBALNIE |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 9 → 8 | 77.6 → 🟢 ** 74.9** (`-2.7`) | 90.5 → 83.4 (`-7.1`) | 55.9 → 55.5 (`-0.4`) | 86.4 → 85.9 (`-0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 3/3/2zł → 4/4/3zł | 77.6 → 🟢 ** 55.3** (`-22.3`) | 90.5 → 77.4 (`-13.1`) | 55.9 → 52.4 (`-3.5`) | 86.4 → 36.2 (`-50.2`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 3/3/2zł → 2/2/1zł | 77.6 → 🟢 ** 50.4** (`-27.2`) | 90.5 → 65.8 (`-24.7`) | 55.9 → 35.0 (`-20.9`) | 86.4 → 0.0 (`-86.4`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 77.6 → 🟢 ** 79.2** (`⬆️ +1.6`) | 90.5 → 88.7 (`-1.8`) | 55.9 → 70.2 (`⬆️ +14.3`) | 86.4 → 78.6 (`-7.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 77.6 → 🟢 ** 60.9** (`-16.7`) | 90.5 → 58.5 (`-32.0`) | 55.9 → 47.9 (`-8.0`) | 86.4 → 76.3 (`-10.1`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5/5/5 → 6/6/6 | 77.6 → 🟡 ** 44.8** (`-32.8`) | 90.5 → 80.9 (`-9.6`) | 55.9 → 8.6 (`-47.3`) | 86.4 → 0.0 (`-86.4`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5/5/5 → 4/4/4 | 77.6 → 🟢 ** 66.8** (`-10.8`) | 90.5 → 71.3 (`-19.2`) | 55.9 → 60.3 (`⬆️ +4.4`) | 86.4 → 68.8 (`-17.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 77.6 → 🟢 ** 77.5** (`-0.1`) | 90.5 → 90.6 (`⬆️ +0.1`) | 55.9 → 55.6 (`-0.3`) | 86.4 | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 77.6 → 🟢 ** 80.6** (`⬆️ +3.0`) | 90.5 → 88.9 (`-1.6`) | 55.9 → 55.3 (`-0.6`) | 86.4 → 97.5 (`⬆️ +11.1`) | 🟢 POPRAWIA GLOBALNIE |

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 5.62 Er (1–9) | 3.2% | 28.7% | 1.04 (0–3) | 3.67 (0–18) | 0.52zł (0.0–2.7) | 6.28 (0.7–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_PLUS1` | 5.79 Er (1–9) | 3.9% | 29.1% | 1.07 (0–4) | 2.57 (0–16) | 0.52zł (0.0–2.7) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 5.43 Er (1–9) | 2.8% | 28.2% | 1.01 (0–4) | 4.66 (0–19) | 0.52zł (0.0–2.8) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 5.63 Er (1–10) | 1.2% | 28.7% | 1.04 (0–4) | 3.68 (0–18) | 0.52zł (0.0–3.0) | 6.28 (0.7–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 5.59 Er (1–8) | 7.0% | 28.6% | 1.04 (0–3) | 3.64 (0–18) | 0.52zł (0.0–2.7) | 6.27 (0.7–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.40 Er (1–9) | 2.1% | 26.4% | 1.05 (0–3) | 3.79 (0–18) | 0.75zł (0.0–3.7) | 6.35 (1.0–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 5.96 Er (1–9) | 5.2% | 31.4% | 0.95 (0–3) | 3.40 (0–18) | 0.43zł (0.0–2.5) | 6.12 (0.8–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_AGENTS_PLUS1` | 5.56 Er (1–9) | 3.0% | 28.5% | 1.07 (0–4) | 3.70 (0–17) | 0.52zł (0.0–2.7) | 6.46 (1.3–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 5.78 Er (1–9) | 4.1% | 29.2% | 1.00 (0–3) | 3.61 (0–17) | 0.52zł (0.0–2.7) | 6.02 (0.7–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.46 Er (1–9) | 2.8% | 25.9% | 1.08 (0–3) | 3.60 (0–18) | 0.49zł (0.0–2.7) | 6.32 (1.0–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 5.86 Er (1–9) | 3.8% | 34.5% | 1.04 (0–4) | 3.59 (0–18) | 0.73zł (0.0–3.0) | 6.16 (0.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 5.63 Er (1–9) | 3.3% | 28.7% | 1.03 (0–4) | 3.67 (0–18) | 0.52zł (0.0–2.7) | 6.27 (0.7–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.61 Er (1–9) | 3.2% | 28.7% | 1.06 (0–4) | 3.66 (0–18) | 0.52zł (0.0–2.7) | 6.29 (0.7–10.0) | 🟢 W NORMIE |

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.