[Strona główna](../../../../../README.md) > [v0.29](README.md) > [audyt_level1_raport](audyt_level1_raport.md)

---

# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.29

**Wersja Balansu:** `v0.29` | **Data:** 2026-08-15 00:33 | **Przeanalizowano Wariantów:** 13 | **Próba:** 20000 gier/setup | **Czas:** 708.31s
**Wynik Bazy Poziomu 1 (Global):** `🟢 94.2 pkt` | 3p: `88.7 pkt` | 4p: `95.1 pkt` | 5p: `98.9 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (2)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🟢 ** 94.2** | 88.7 | 95.1 | 98.9 | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 94.2 → 🟢 ** 92.5** (`-1.7`) | 88.7 → 88.1 (`-0.6`) | 95.1 → 96.7 (`⬆️ +1.6`) | 98.9 → 92.7 (`-6.2`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 11 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 10 → 11 | 🟢 ** 94.2** | 88.7 | 95.1 | 98.9 | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 10 → 9 | 94.2 → 🟢 ** 94.1** (`-0.1`) | 88.7 → 88.4 (`-0.3`) | 95.1 | 98.9 | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 94.2 → 🟢 ** 94.0** (`-0.2`) | 88.7 → 88.6 (`-0.1`) | 95.1 → 94.6 (`-0.5`) | 98.9 | ⚪ OPTYMALNY |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 94.2 → 🟡 ** 85.6** (`-8.6`) | 88.7 → 81.5 (`-7.2`) | 95.1 → 94.8 (`-0.3`) | 98.9 → 80.4 (`-18.5`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 94.2 → 🟡 ** 82.2** (`-12.0`) | 88.7 → 79.8 (`-8.9`) | 95.1 → 78.5 (`-16.6`) | 98.9 → 88.2 (`-10.7`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 94.2 → 🟠 ** 74.4** (`-19.8`) | 88.7 → 79.5 (`-9.2`) | 95.1 → 55.2 (`-39.9`) | 98.9 → 88.5 (`-10.4`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/8 → 5/6/7 | 94.2 → 🟠 ** 68.4** (`-25.8`) | 88.7 → 71.3 (`-17.4`) | 95.1 → 45.6 (`-49.5`) | 98.9 → 88.3 (`-10.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 94.2 → 🟠 ** 68.1** (`-26.1`) | 88.7 → 73.5 (`-15.2`) | 95.1 → 51.6 (`-43.5`) | 98.9 → 79.2 (`-19.7`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 3/3/2zł → 4/4/3zł | 94.2 → 🔴 ** 55.1** (`-39.1`) | 88.7 → 69.9 (`-18.8`) | 95.1 → 41.0 (`-54.1`) | 98.9 → 54.4 (`-44.5`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 3/3/2zł → 2/2/1zł | 94.2 → 🔴 ** 54.4** (`-39.8`) | 88.7 → 70.7 (`-18.0`) | 95.1 → 38.0 (`-57.1`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 94.2 → 🔴 ** 45.8** (`-48.4`) | 88.7 → 47.6 (`-41.1`) | 95.1 → 44.0 (`-51.1`) | 98.9 → 0.0 (`-98.9`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (2)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 5.51 Er (1–10) | 1.1% | 26.2% | 1.03 (0–4) | 3.57 (0–19) | 1.16zł (0.0–5.0) | 6.30 (0.3–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.50 Er (1–10) | 1.1% | 26.1% | 1.05 (0–4) | 3.57 (0–19) | 1.16zł (0.0–5.0) | 6.31 (0.3–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 11 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_MAX_ERAS_PLUS1` | 5.51 Er (1–11) | 0.4% | 26.2% | 1.03 (0–4) | 3.57 (0–21) | 1.16zł (0.0–5.3) | 6.30 (0.3–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 5.50 Er (1–9) | 2.7% | 26.2% | 1.03 (0–4) | 3.56 (0–18) | 1.17zł (0.0–5.0) | 6.30 (0.3–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 5.51 Er (1–10) | 1.1% | 26.2% | 1.01 (0–4) | 3.57 (0–19) | 1.17zł (0.0–5.0) | 6.29 (0.3–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 5.45 Er (1–10) | 0.9% | 25.9% | 1.06 (0–4) | 3.60 (0–20) | 1.16zł (0.0–5.3) | 6.48 (0.7–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 5.77 Er (1–10) | 1.6% | 32.8% | 1.03 (0–4) | 3.53 (0–22) | 1.44zł (0.0–5.3) | 6.21 (0.0–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_AGENTS_MINUS1` | 5.67 Er (1–10) | 1.5% | 26.8% | 0.99 (0–4) | 3.54 (0–20) | 1.18zł (0.0–5.0) | 6.07 (0.7–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 5.34 Er (1–10) | 0.9% | 25.6% | 1.00 (0–4) | 4.53 (0–21) | 1.15zł (0.0–5.7) | 6.34 (0.3–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_PLUS1` | 5.67 Er (1–10) | 1.3% | 26.7% | 1.05 (0–4) | 2.53 (0–18) | 1.18zł (0.0–6.0) | 6.22 (0.3–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.32 Er (1–10) | 0.8% | 24.1% | 1.05 (0–4) | 3.69 (0–21) | 1.51zł (0.0–6.3) | 6.43 (0.3–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 5.81 Er (1–10) | 1.7% | 27.0% | 0.93 (0–4) | 3.28 (0–21) | 0.83zł (0.0–4.7) | 6.15 (0.5–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.31 Er (1–10) | 0.8% | 21.1% | 1.05 (0–4) | 3.48 (0–19) | 0.95zł (0.0–4.3) | 6.38 (0.7–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.