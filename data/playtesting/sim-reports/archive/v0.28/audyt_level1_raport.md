[Strona główna](../../../../../README.md) > [v0.28](README.md) > [audyt_level1_raport](audyt_level1_raport.md)

---

# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.28

**Wersja Balansu:** `v0.28` | **Data:** 2026-08-14 18:27 | **Przeanalizowano Wariantów:** 13 | **Próba:** 3000 gier/setup | **Czas:** 98.25s
**Wynik Bazy Poziomu 1 (Global):** `🟢 95.8 pkt` | 3p: `90.0 pkt` | 4p: `98.4 pkt` | 5p: `99.1 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (4)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🟢 ** 95.8** | 90.0 | 98.4 | 99.1 | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 95.8 → 🟢 ** 96.2** (`⬆️ +0.4`) | 90.0 → 90.8 (`⬆️ +0.8`) | 98.4 → 98.5 (`⬆️ +0.1`) | 99.1 → 99.2 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 10 → 9 | 95.8 → 🟢 ** 96.0** (`⬆️ +0.2`) | 90.0 → 90.4 (`⬆️ +0.4`) | 98.4 | 99.1 | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 95.8 → 🟢 ** 95.7** (`-0.1`) | 90.0 → 91.5 (`⬆️ +1.5`) | 98.4 → 96.4 (`-2.0`) | 99.1 | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 9 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 10 → 11 | 🟢 ** 95.8** | 90.0 → 89.9 (`-0.1`) | 98.4 | 99.1 | ⚪ OPTYMALNY |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 95.8 → 🟢 ** 92.8** (`-3.0`) | 90.0 → 83.1 (`-6.9`) | 98.4 → 98.0 (`-0.4`) | 99.1 → 97.2 (`-1.9`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 95.8 → 🟢 ** 89.6** (`-6.2`) | 90.0 → 81.8 (`-8.2`) | 98.4 → 88.8 (`-9.6`) | 99.1 → 98.1 (`-1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 95.8 → 🟢 ** 85.7** (`-10.1`) | 90.0 → 86.3 (`-3.7`) | 98.4 → 73.6 (`-24.8`) | 99.1 → 97.1 (`-2.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/8 → 5/6/7 | 95.8 → 🟢 ** 78.1** (`-17.7`) | 90.0 → 71.8 (`-18.2`) | 98.4 → 64.3 (`-34.1`) | 99.1 → 98.3 (`-0.8`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 95.8 → 🟢 ** 72.9** (`-22.9`) | 90.0 → 70.4 (`-19.6`) | 98.4 → 76.4 (`-22.0`) | 99.1 → 71.9 (`-27.2`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 3/3/2zł → 4/4/3zł | 95.8 → 🟢 ** 70.1** (`-25.7`) | 90.0 → 80.0 (`-10.0`) | 98.4 → 72.0 (`-26.4`) | 99.1 → 58.4 (`-40.7`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 3/3/2zł → 2/2/1zł | 95.8 → 🟢 ** 62.1** (`-33.7`) | 90.0 → 70.9 (`-19.1`) | 98.4 → 53.3 (`-45.1`) | 99.1 → 0.0 (`-99.1`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 95.8 → 🟢 ** 53.0** (`-42.8`) | 90.0 → 53.6 (`-36.4`) | 98.4 → 69.8 (`-28.6`) | 99.1 → 35.7 (`-63.4`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (4)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 5.51 Er (1–10) | 1.2% | 26.4% | 1.02 (0–4) | 3.59 (0–19) | 1.04zł (0.0–4.3) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.50 Er (1–10) | 1.1% | 26.4% | 1.04 (0–4) | 3.58 (0–19) | 1.04zł (0.0–4.3) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 5.49 Er (1–9) | 2.8% | 26.4% | 1.02 (0–4) | 3.58 (0–17) | 1.04zł (0.0–4.3) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 5.51 Er (1–10) | 1.2% | 26.4% | 1.01 (0–3) | 3.59 (0–19) | 1.04zł (0.0–4.7) | 6.30 (0.7–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 9 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_MAX_ERAS_PLUS1` | 5.51 Er (1–11) | 0.4% | 26.4% | 1.02 (0–4) | 3.59 (0–20) | 1.04zł (0.0–4.3) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 5.45 Er (1–10) | 0.9% | 26.2% | 1.05 (0–4) | 3.62 (0–18) | 1.03zł (0.0–5.0) | 6.48 (1.2–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 5.78 Er (1–10) | 1.6% | 32.9% | 1.03 (0–3) | 3.56 (0–19) | 1.29zł (0.0–4.7) | 6.21 (0.7–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_AGENTS_MINUS1` | 5.68 Er (1–10) | 1.5% | 27.0% | 0.98 (0–3) | 3.55 (0–18) | 1.05zł (0.0–4.3) | 6.07 (0.7–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 5.34 Er (1–10) | 1.0% | 25.8% | 0.99 (0–4) | 4.53 (0–22) | 1.02zł (0.0–5.0) | 6.34 (0.7–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_PLUS1` | 5.66 Er (1–10) | 1.3% | 26.9% | 1.05 (0–3) | 2.53 (0–17) | 1.04zł (0.0–4.3) | 6.22 (0.7–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.32 Er (1–10) | 0.8% | 24.3% | 1.04 (0–3) | 3.72 (0–20) | 1.35zł (0.0–6.0) | 6.44 (1.0–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 5.85 Er (1–10) | 1.7% | 27.8% | 0.93 (0–4) | 3.32 (0–18) | 0.80zł (0.0–3.7) | 6.16 (0.6–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.32 Er (1–10) | 0.8% | 21.9% | 1.05 (0–4) | 3.49 (0–19) | 0.87zł (0.0–4.3) | 6.36 (0.7–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.