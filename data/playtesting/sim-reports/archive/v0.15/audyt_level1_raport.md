[Strona główna](../../../../../README.md) > [v0.15](README.md) > [audyt_level1_raport](audyt_level1_raport.md)

---

# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.15

**Wersja Balansu:** `v0.15` | **Data:** 2026-08-14 12:03 | **Przeanalizowano Wariantów:** 13 | **Próba:** 2000 gier/setup | **Czas:** 51.48s
**Wynik Bazy Poziomu 1 (Global):** `🟢 81.2 pkt` | 3p: `90.5 pkt` | 4p: `71.1 pkt` | 5p: `82.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🟢 ** 81.2** | 90.5 | 71.1 | 82.0 | ⚪ OPTYMALNY |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 81.2 → 🟢 ** 72.0** (`-9.2`) | 90.5 → 73.6 (`-16.9`) | 71.1 → 73.5 (`⬆️ +2.4`) | 82.0 → 69.0 (`-13.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/8 → 5/6/7 | 81.2 → 🟡 ** 48.6** (`-32.6`) | 90.5 → 71.4 (`-19.1`) | 71.1 → 11.9 (`-59.2`) | 82.0 → 62.4 (`-19.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 9 → 10 | 81.2 → 🟢 ** 81.8** (`⬆️ +0.6`) | 90.5 → 92.5 (`⬆️ +2.0`) | 71.1 | 82.0 → 81.7 (`-0.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 9 → 8 | 81.2 → 🟢 ** 78.9** (`-2.3`) | 90.5 → 83.4 (`-7.1`) | 71.1 → 71.5 (`⬆️ +0.4`) | 82.0 → 81.7 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 3/3/2zł → 4/4/3zł | 81.2 → 🟡 ** 46.6** (`-34.6`) | 90.5 → 77.4 (`-13.1`) | 71.1 → 60.8 (`-10.3`) | 82.0 → 1.6 (`-80.4`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 3/3/2zł → 2/2/1zł | 81.2 → 🟢 ** 56.8** (`-24.4`) | 90.5 → 65.8 (`-24.7`) | 71.1 → 47.9 (`-23.2`) | 82.0 → 0.0 (`-82.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 81.2 → 🟢 ** 72.7** (`-8.5`) | 90.5 → 88.7 (`-1.8`) | 71.1 → 71.2 (`⬆️ +0.1`) | 82.0 → 58.1 (`-23.9`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 81.2 → 🟢 ** 66.0** (`-15.2`) | 90.5 → 58.5 (`-32.0`) | 71.1 → 59.3 (`-11.8`) | 82.0 → 80.2 (`-1.8`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5/5/5 → 6/6/6 | 81.2 → 🟢 ** 51.3** (`-29.9`) | 90.5 → 80.9 (`-9.6`) | 71.1 → 21.7 (`-49.4`) | 82.0 → 0.0 (`-82.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5/5/5 → 4/4/4 | 81.2 → 🟢 ** 70.6** (`-10.6`) | 90.5 → 71.3 (`-19.2`) | 71.1 → 71.2 (`⬆️ +0.1`) | 82.0 → 69.4 (`-12.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 81.2 → 🟢 ** 81.4** (`⬆️ +0.2`) | 90.5 → 90.6 (`⬆️ +0.1`) | 71.1 → 71.2 (`⬆️ +0.1`) | 82.0 → 82.4 (`⬆️ +0.4`) | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 81.2 → 🟢 ** 81.1** (`-0.1`) | 90.5 → 88.9 (`-1.6`) | 71.1 → 70.3 (`-0.8`) | 82.0 → 84.1 (`⬆️ +2.1`) | ⚪ OPTYMALNY |

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 5.61 Er (1–9) | 3.1% | 28.6% | 1.04 (0–3) | 3.65 (0–18) | 0.52zł (0.0–2.7) | 6.27 (0.7–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_PLUS1` | 5.78 Er (1–9) | 3.8% | 29.1% | 1.06 (0–4) | 2.57 (0–16) | 0.52zł (0.0–2.7) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 5.40 Er (1–9) | 2.7% | 28.0% | 1.01 (0–4) | 4.63 (0–19) | 0.51zł (0.0–2.8) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 5.62 Er (1–10) | 1.1% | 28.6% | 1.04 (0–4) | 3.66 (0–18) | 0.52zł (0.0–3.0) | 6.27 (0.7–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 5.57 Er (1–8) | 6.8% | 28.6% | 1.04 (0–3) | 3.62 (0–18) | 0.52zł (0.0–2.7) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.38 Er (1–9) | 2.1% | 26.3% | 1.05 (0–3) | 3.77 (0–18) | 0.75zł (0.0–3.7) | 6.34 (1.0–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 5.95 Er (1–9) | 5.0% | 31.3% | 0.95 (0–3) | 3.38 (0–18) | 0.43zł (0.0–2.5) | 6.12 (0.8–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_AGENTS_PLUS1` | 5.54 Er (1–9) | 2.9% | 28.4% | 1.07 (0–4) | 3.68 (0–17) | 0.52zł (0.0–2.7) | 6.45 (1.3–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 5.77 Er (1–9) | 4.0% | 29.2% | 1.00 (0–3) | 3.60 (0–17) | 0.52zł (0.0–2.7) | 6.01 (0.7–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.45 Er (1–9) | 2.7% | 25.9% | 1.07 (0–3) | 3.59 (0–18) | 0.49zł (0.0–2.7) | 6.31 (1.0–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 5.84 Er (1–9) | 3.7% | 34.4% | 1.04 (0–4) | 3.57 (0–18) | 0.73zł (0.0–3.0) | 6.16 (0.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 5.61 Er (1–9) | 3.2% | 28.7% | 1.02 (0–4) | 3.65 (0–18) | 0.52zł (0.0–2.7) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.59 Er (1–9) | 3.1% | 28.6% | 1.06 (0–4) | 3.64 (0–18) | 0.52zł (0.0–2.7) | 6.28 (0.7–10.0) | 🟢 W NORMIE |

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.