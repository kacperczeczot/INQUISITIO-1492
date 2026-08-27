[Strona główna](../../../../../README.md) > [v0.42](README.md) > [audyt_level1_raport](audyt_level1_raport.md)

---

# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.42

**Wersja Balansu:** `v0.42` | **Data:** 2026-08-16 00:40 | **Przeanalizowano Wariantów:** 13 | **Próba:** 5000 gier/setup | **Czas:** 133.29s
**Wynik Bazy Poziomu 1 (Global):** `🔴 56.7 pkt` | 3p: `46.3 pkt` | 4p: `67.1 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (7)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🔴 ** 56.7** | 46.3 | 67.1 | 0.0 | ⚪ OPTYMALNY |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 56.7 → 🟠 ** 65.4** (`⬆️ +8.7`) | 46.3 → 54.3 (`⬆️ +8.0`) | 67.1 → 76.6 (`⬆️ +9.5`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 56.7 → 🟠 ** 60.8** (`⬆️ +4.1`) | 46.3 → 35.9 (`-10.4`) | 67.1 → 85.8 (`⬆️ +18.7`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 56.7 → 🔴 ** 59.2** (`⬆️ +2.5`) | 46.3 → 34.8 (`-11.5`) | 67.1 → 98.9 (`⬆️ +31.8`) | 0.0 → 43.8 (`⬆️ +43.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 56.7 → 🔴 ** 58.9** (`⬆️ +2.2`) | 46.3 → 52.3 (`⬆️ +6.0`) | 67.1 → 65.5 (`-1.6`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 11 → 10 | 56.7 → 🔴 ** 58.8** (`⬆️ +2.1`) | 46.3 → 50.7 (`⬆️ +4.4`) | 67.1 → 66.9 (`-0.2`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/8 → 5/6/7 | 56.7 → 🔴 ** 27.6** (`-29.1`) | 46.3 → 48.5 (`⬆️ +2.2`) | 67.1 → 6.7 (`-60.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 6 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 11 → 12 | 56.7 → 🔴 ** 56.5** (`-0.2`) | 46.3 → 46.0 (`-0.3`) | 67.1 | 0.0 | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 56.7 → 🔴 ** 54.1** (`-2.6`) | 46.3 → 41.3 (`-5.0`) | 67.1 → 67.0 (`-0.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 4/4/4zł → 5/5/5zł | 56.7 → 🔴 ** 35.5** (`-21.2`) | 46.3 → 22.0 (`-24.3`) | 67.1 → 49.0 (`-18.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 56.7 → 🔴 ** 24.6** (`-32.1`) | 46.3 → 24.6 (`-21.7`) | 67.1 → 0.0 (`-67.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 4/4/4zł → 3/3/3zł | 56.7 → 🔴 ** 23.2** (`-33.5`) | 46.3 → 29.8 (`-16.5`) | 67.1 → 16.7 (`-50.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 56.7 → 🔴 ** 18.6** (`-38.1`) | 46.3 → 22.4 (`-23.9`) | 67.1 → 14.9 (`-52.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (7)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 5.65 Er (1–11) | 1.0% | 25.3% | 0.57 (0–3) | 3.51 (0–19) | 1.51zł (0.0–7.7) | 6.05 (1.0–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 5.60 Er (1–11) | 0.8% | 25.0% | 0.63 (0–3) | 3.49 (0–19) | 1.52zł (0.0–8.0) | 6.13 (0.7–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 6.00 Er (1–11) | 1.5% | 32.2% | 0.57 (0–3) | 3.53 (0–19) | 1.85zł (0.0–7.7) | 5.97 (0.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_THRESHOLD_PLUS1` | 5.83 Er (1–11) | 1.2% | 25.8% | 0.58 (0–3) | 2.57 (0–18) | 1.54zł (0.0–7.7) | 5.99 (1.0–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.64 Er (1–11) | 1.0% | 25.3% | 0.58 (0–4) | 3.50 (0–19) | 1.51zł (0.0–7.7) | 6.05 (1.0–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 5.64 Er (1–10) | 2.4% | 25.3% | 0.57 (0–3) | 3.50 (0–19) | 1.52zł (0.0–7.7) | 6.04 (1.0–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 5.47 Er (1–11) | 0.9% | 24.8% | 0.55 (0–3) | 4.37 (0–20) | 1.49zł (0.0–7.3) | 6.08 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 6 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_MAX_ERAS_PLUS1` | 5.65 Er (1–12) | 0.4% | 25.3% | 0.57 (0–3) | 3.51 (0–21) | 1.51zł (0.0–7.7) | 6.05 (1.0–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 5.65 Er (1–11) | 1.1% | 25.3% | 0.55 (0–3) | 3.51 (0–19) | 1.52zł (0.0–7.7) | 6.04 (1.0–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.43 Er (1–11) | 0.7% | 23.2% | 0.61 (0–3) | 3.52 (0–18) | 1.87zł (0.0–8.3) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.38 Er (1–11) | 0.5% | 19.9% | 0.61 (0–3) | 3.38 (0–20) | 1.29zł (0.0–6.0) | 6.14 (0.7–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 6.19 Er (1–11) | 2.0% | 26.2% | 0.46 (0–3) | 3.18 (0–18) | 1.21zł (0.0–6.3) | 5.85 (0.0–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 5.84 Er (1–11) | 1.7% | 26.5% | 0.47 (0–3) | 3.65 (0–20) | 1.45zł (0.0–7.3) | 6.02 (0.8–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.