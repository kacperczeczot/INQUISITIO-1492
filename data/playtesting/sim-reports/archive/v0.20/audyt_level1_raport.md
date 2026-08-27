[Strona główna](../../../../../README.md) > [v0.20](README.md) > [audyt_level1_raport](audyt_level1_raport.md)

---

# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.20

**Wersja Balansu:** `v0.20` | **Data:** 2026-08-14 14:06 | **Przeanalizowano Wariantów:** 13 | **Próba:** 3000 gier/setup | **Czas:** 98.02s
**Wynik Bazy Poziomu 1 (Global):** `🟢 91.0 pkt` | 3p: `80.8 pkt` | 4p: `93.3 pkt` | 5p: `99.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (6)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🟢 ** 91.0** | 80.8 | 93.3 | 99.0 | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 9 → 10 | 91.0 → 🟢 ** 91.7** (`⬆️ +0.7`) | 80.8 → 82.9 (`⬆️ +2.1`) | 93.3 → 93.2 (`-0.1`) | 99.0 | 🟢 POPRAWIA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 91.0 → 🟢 ** 91.2** (`⬆️ +0.2`) | 80.8 → 81.2 (`⬆️ +0.4`) | 93.3 → 94.2 (`⬆️ +0.9`) | 99.0 → 98.1 (`-0.9`) | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 🟢 ** 91.0** | 80.8 → 80.4 (`-0.4`) | 93.3 → 93.5 (`⬆️ +0.2`) | 99.0 | ⚪ OPTYMALNY |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/8 → 5/6/7 | 91.0 → 🟢 ** 85.2** (`-5.8`) | 80.8 → 81.6 (`⬆️ +0.8`) | 93.3 → 74.7 (`-18.6`) | 99.0 → 99.2 (`⬆️ +0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 91.0 → 🟢 ** 74.5** (`-16.5`) | 80.8 → 87.8 (`⬆️ +7.0`) | 93.3 → 82.5 (`-10.8`) | 99.0 → 53.1 (`-45.9`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 7 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 91.0 → 🟢 ** 90.1** (`-0.9`) | 80.8 → 80.6 (`-0.2`) | 93.3 → 90.9 (`-2.4`) | 99.0 → 98.8 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 9 → 8 | 91.0 → 🟢 ** 86.4** (`-4.6`) | 80.8 → 69.7 (`-11.1`) | 93.3 → 90.5 (`-2.8`) | 99.0 → 98.9 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 91.0 → 🟢 ** 81.3** (`-9.7`) | 80.8 → 75.3 (`-5.5`) | 93.3 → 84.0 (`-9.3`) | 99.0 → 84.5 (`-14.5`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 3/3/2zł → 4/4/3zł | 91.0 → 🟢 ** 66.3** (`-24.7`) | 80.8 → 59.9 (`-20.9`) | 93.3 → 73.5 (`-19.8`) | 99.0 → 65.4 (`-33.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 3/3/2zł → 2/2/1zł | 91.0 → 🟢 ** 64.9** (`-26.1`) | 80.8 → 76.1 (`-4.7`) | 93.3 → 53.7 (`-39.6`) | 99.0 → 0.0 (`-99.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 91.0 → 🟢 ** 60.8** (`-30.2`) | 80.8 → 50.8 (`-30.0`) | 93.3 → 69.7 (`-23.6`) | 99.0 → 62.0 (`-37.0`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 91.0 → 🟢 ** 60.6** (`-30.4`) | 80.8 → 50.9 (`-29.9`) | 93.3 → 58.1 (`-35.2`) | 99.0 → 72.8 (`-26.2`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (6)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 5.52 Er (1–9) | 4.1% | 28.5% | 1.03 (0–4) | 3.46 (0–18) | 0.55zł (0.0–3.0) | 6.05 (0.7–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 5.54 Er (1–10) | 1.7% | 28.5% | 1.03 (0–4) | 3.47 (0–20) | 0.55zł (0.0–3.0) | 6.05 (0.7–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 5.48 Er (1–9) | 3.7% | 28.3% | 1.06 (0–4) | 3.52 (0–16) | 0.55zł (0.0–3.0) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.51 Er (1–9) | 4.1% | 28.4% | 1.05 (0–4) | 3.46 (0–18) | 0.55zł (0.0–3.0) | 6.06 (0.7–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 5.36 Er (1–9) | 3.7% | 28.0% | 1.00 (0–4) | 4.42 (0–20) | 0.55zł (0.0–3.0) | 6.10 (0.7–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.36 Er (1–9) | 3.4% | 24.9% | 1.06 (0–3) | 3.40 (0–19) | 0.44zł (0.0–2.7) | 6.12 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 7 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 5.53 Er (1–9) | 4.1% | 28.5% | 1.01 (0–3) | 3.46 (0–18) | 0.55zł (0.0–3.0) | 6.04 (0.7–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 5.48 Er (1–8) | 8.2% | 28.3% | 1.03 (0–4) | 3.42 (0–17) | 0.55zł (0.0–3.0) | 6.04 (0.7–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 5.78 Er (1–9) | 4.9% | 33.7% | 1.03 (0–4) | 3.40 (0–19) | 0.78zł (0.0–3.3) | 5.99 (0.7–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_START_GOLD_PLUS1` | 5.30 Er (1–9) | 3.0% | 24.8% | 1.04 (0–4) | 3.56 (0–18) | 0.79zł (0.0–4.0) | 6.22 (1.0–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 5.91 Er (1–9) | 6.8% | 29.8% | 0.94 (0–4) | 3.18 (0–17) | 0.41zł (0.0–2.8) | 5.92 (0.6–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 5.68 Er (1–9) | 5.1% | 29.0% | 0.98 (0–3) | 3.37 (0–17) | 0.55zł (0.0–3.3) | 5.79 (0.7–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_PLUS1` | 5.67 Er (1–9) | 4.6% | 28.9% | 1.05 (0–4) | 2.35 (0–16) | 0.55zł (0.0–3.3) | 5.95 (0.7–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.