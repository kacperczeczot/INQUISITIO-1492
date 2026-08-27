[Strona główna](../../../../../README.md) > [v0.13](README.md) > [audyt_level1_raport](audyt_level1_raport.md)

---

# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.13

**Wersja Balansu:** `v0.13` | **Data:** 2026-08-14 11:44 | **Przeanalizowano Wariantów:** 13 | **Próba:** 500 gier/setup | **Czas:** 13.71s
**Wynik Bazy Poziomu 1 (Global):** `🟢 80.5 pkt` | 3p: `91.5 pkt` | 4p: `67.9 pkt` | 5p: `82.2 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🟢 ** 80.5** | 91.5 | 67.9 | 82.2 | ⚪ OPTYMALNY |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/7 → 7/8/8 | 80.5 → 🟢 ** 76.8** (`-3.7`) | 91.5 → 68.4 (`-23.1`) | 67.9 → 63.1 (`-4.8`) | 82.2 → 98.9 (`⬆️ +16.7`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/7 → 5/6/6 | 80.5 → 🟡 ** 48.8** (`-31.7`) | 91.5 → 70.2 (`-21.3`) | 67.9 → 19.7 (`-48.2`) | 82.2 → 56.6 (`-25.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 9 → 10 | 80.5 → 🟢 ** 81.5** (`⬆️ +1.0`) | 91.5 → 92.5 (`⬆️ +1.0`) | 67.9 → 69.7 (`⬆️ +1.8`) | 82.2 → 82.3 (`⬆️ +0.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 9 → 8 | 80.5 → 🟢 ** 77.4** (`-3.1`) | 91.5 → 83.0 (`-8.5`) | 67.9 → 67.0 (`-0.9`) | 82.2 | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 3/3/2zł → 4/4/3zł | 80.5 → 🟢 ** 70.6** (`-9.9`) | 91.5 → 84.1 (`-7.4`) | 67.9 → 57.1 (`-10.8`) | 82.2 → 0.0 (`-82.2`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 3/3/2zł → 2/2/1zł | 80.5 → 🟢 ** 55.8** (`-24.7`) | 91.5 → 65.8 (`-25.7`) | 67.9 → 45.9 (`-22.0`) | 82.2 → 0.0 (`-82.2`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 80.5 → 🟢 ** 64.9** (`-15.6`) | 91.5 → 88.8 (`-2.7`) | 67.9 → 36.7 (`-31.2`) | 82.2 → 69.2 (`-13.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 80.5 → 🟢 ** 59.7** (`-20.8`) | 91.5 → 59.3 (`-32.2`) | 67.9 → 34.1 (`-33.8`) | 82.2 → 85.8 (`⬆️ +3.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5/5/5 → 6/6/6 | 80.5 → 🟡 ** 35.0** (`-45.5`) | 91.5 → 65.4 (`-26.1`) | 67.9 → 4.6 (`-63.3`) | 82.2 → 0.0 (`-82.2`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5/5/5 → 4/4/4 | 80.5 → 🟢 ** 65.1** (`-15.4`) | 91.5 → 71.3 (`-20.2`) | 67.9 → 58.5 (`-9.4`) | 82.2 → 65.6 (`-16.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 80.5 → 🟢 ** 79.6** (`-0.9`) | 91.5 → 90.5 (`-1.0`) | 67.9 → 63.8 (`-4.1`) | 82.2 → 84.4 (`⬆️ +2.2`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 80.5 → 🟢 ** 79.4** (`-1.1`) | 91.5 → 91.0 (`-0.5`) | 67.9 → 65.6 (`-2.3`) | 82.2 → 81.7 (`-0.5`) | 🔴 POGARSZA GLOBALNIE |

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 5.63 Er (1–9) | 3.2% | 28.7% | 1.03 (0–3) | 3.73 (0–15) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_PLUS1` | 5.82 Er (2–9) | 3.9% | 29.2% | 1.06 (0–3) | 2.62 (0–14) | 0.53zł (0.0–2.7) | 6.19 (1.2–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 5.44 Er (1–9) | 2.9% | 28.2% | 1.00 (0–3) | 4.75 (0–19) | 0.52zł (0.0–2.7) | 6.32 (1.2–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 5.64 Er (1–10) | 1.1% | 28.7% | 1.03 (0–3) | 3.74 (0–16) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 5.60 Er (1–8) | 7.1% | 28.6% | 1.03 (0–3) | 3.71 (0–15) | 0.53zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.40 Er (1–9) | 2.1% | 26.4% | 1.04 (0–3) | 3.86 (0–18) | 0.76zł (0.0–3.7) | 6.34 (1.5–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 5.95 Er (1–9) | 5.2% | 31.4% | 0.95 (0–3) | 3.47 (0–18) | 0.43zł (0.0–2.3) | 6.12 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_AGENTS_PLUS1` | 5.60 Er (1–9) | 3.1% | 28.6% | 1.06 (0–3) | 3.79 (0–17) | 0.53zł (0.0–2.7) | 6.47 (1.5–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 5.80 Er (1–9) | 3.9% | 29.3% | 0.98 (0–3) | 3.70 (0–17) | 0.53zł (0.0–2.7) | 6.02 (1.2–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.48 Er (1–9) | 2.7% | 25.9% | 1.07 (0–3) | 3.69 (0–18) | 0.50zł (0.0–2.3) | 6.32 (1.0–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 5.84 Er (1–9) | 3.5% | 34.4% | 1.03 (0–3) | 3.65 (0–17) | 0.74zł (0.0–3.0) | 6.16 (1.0–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 5.63 Er (1–9) | 3.2% | 28.7% | 1.01 (0–3) | 3.73 (0–15) | 0.53zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.62 Er (1–9) | 3.1% | 28.7% | 1.06 (0–4) | 3.73 (0–15) | 0.53zł (0.0–2.7) | 6.28 (1.2–10.0) | 🟢 W NORMIE |

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.