[Strona główna](../../../../../README.md) > [v0.76](README.md) > [audyt_level1_raport](audyt_level1_raport.md)

---

# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.76

**Wersja Balansu:** `v0.76` | **Data:** 2026-08-17 01:49 | **Przeanalizowano Wariantów:** 13 | **Próba:** 3000 gier/setup | **Czas:** 235.15s
**Wynik Bazy Poziomu 1 (Global):** `🔴 58.3 pkt` | 3p: `39.5 pkt` | 4p: `68.8 pkt` | 5p: `66.6 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (9)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🔴 ** 58.3** | 39.5 | 68.8 | 66.6 | ⚪ OPTYMALNY |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 58.3 → 🟠 ** 64.4** (`⬆️ +6.1`) | 39.5 → 42.7 (`⬆️ +3.2`) | 68.8 → 75.6 (`⬆️ +6.8`) | 66.6 → 75.0 (`⬆️ +8.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 12 → 13 | 58.3 → 🟠 ** 61.0** (`⬆️ +2.7`) | 39.5 → 48.1 (`⬆️ +8.6`) | 68.8 → 68.5 (`-0.3`) | 66.6 → 66.5 (`-0.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 58.3 → 🟠 ** 60.4** (`⬆️ +2.1`) | 39.5 → 30.1 (`-9.4`) | 68.8 → 69.8 (`⬆️ +1.0`) | 66.6 → 81.4 (`⬆️ +14.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 58.3 → 🔴 ** 59.4** (`⬆️ +1.1`) | 39.5 → 47.1 (`⬆️ +7.6`) | 68.8 → 68.6 (`-0.2`) | 66.6 → 62.5 (`-4.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 4zł → 5zł | 58.3 → 🔴 ** 56.4** (`-1.9`) | 39.5 → 51.2 (`⬆️ +11.7`) | 68.8 → 64.0 (`-4.8`) | 66.6 → 54.0 (`-12.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/8 → 5/6/7 | 58.3 → 🔴 ** 56.0** (`-2.3`) | 39.5 → 35.4 (`-4.1`) | 68.8 → 64.5 (`-4.3`) | 66.6 → 68.2 (`⬆️ +1.6`) | 🔴 POGARSZA GLOBALNIE |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 12 → 11 | 58.3 → 🔴 ** 53.9** (`-4.4`) | 39.5 → 26.2 (`-13.3`) | 68.8 → 68.9 (`⬆️ +0.1`) | 66.6 | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 58.3 → 🔴 ** 52.3** (`-6.0`) | 39.5 → 40.9 (`⬆️ +1.4`) | 68.8 → 56.5 (`-12.3`) | 66.6 → 59.4 (`-7.2`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 4 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 58.3 → 🔴 ** 53.0** (`-5.3`) | 39.5 → 38.7 (`-0.8`) | 68.8 → 62.7 (`-6.1`) | 66.6 → 57.5 (`-9.1`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 4zł → 3zł | 58.3 → 🔴 ** 46.5** (`-11.8`) | 39.5 → 28.4 (`-11.1`) | 68.8 → 50.9 (`-17.9`) | 66.6 → 60.2 (`-6.4`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 58.3 → 🔴 ** 45.7** (`-12.6`) | 39.5 → 35.3 (`-4.2`) | 68.8 → 52.7 (`-16.1`) | 66.6 → 49.2 (`-17.4`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 58.3 → 🔴 ** 44.3** (`-14.0`) | 39.5 → 33.4 (`-6.1`) | 68.8 → 45.8 (`-23.0`) | 66.6 → 53.7 (`-12.9`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (9)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 6.63 Er (1–12) | 5.9% | 5.3% | 1.62 (0–4) | 3.71 (0–25) | 3.23zł (0.0–11.0) | 6.15 (0.0–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 6.89 Er (1–12) | 6.6% | 6.3% | 1.68 (0–4) | 3.69 (0–23) | 3.67zł (0.0–12.3) | 6.11 (0.3–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 6.67 Er (1–13) | 3.9% | 5.2% | 1.63 (0–4) | 3.74 (0–27) | 3.23zł (0.0–11.0) | 6.16 (0.0–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 6.85 Er (1–12) | 8.3% | 5.4% | 1.57 (0–4) | 3.82 (0–25) | 3.17zł (0.0–12.3) | 5.99 (0.0–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_PLUS1` | 6.56 Er (1–12) | 5.2% | 5.6% | 1.63 (0–4) | 2.66 (0–20) | 3.09zł (0.0–11.7) | 6.12 (0.0–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 6.37 Er (1–12) | 4.7% | 4.3% | 1.55 (0–4) | 3.59 (0–25) | 3.73zł (0.0–12.3) | 6.15 (0.7–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 6.71 Er (1–12) | 6.2% | 4.8% | 1.60 (0–4) | 4.80 (0–25) | 3.41zł (0.0–12.3) | 6.13 (0.0–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 6.58 Er (1–11) | 9.2% | 5.3% | 1.61 (0–3) | 3.66 (0–22) | 3.23zł (0.0–11.0) | 6.14 (0.0–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 6.43 Er (1–12) | 4.2% | 5.2% | 1.60 (0–4) | 3.60 (0–21) | 3.20zł (0.0–12.3) | 6.31 (0.7–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 4 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 6.79 Er (1–12) | 7.1% | 5.1% | 1.21 (0–3) | 3.64 (0–23) | 3.32zł (0.0–11.7) | 6.02 (0.0–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 6.81 Er (1–12) | 6.8% | 6.4% | 1.67 (0–4) | 3.72 (0–21) | 2.77zł (0.0–11.3) | 6.07 (0.3–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 6.40 Er (1–12) | 5.0% | 5.4% | 2.22 (0–6) | 3.81 (0–22) | 3.15zł (0.0–12.0) | 6.31 (0.8–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 6.37 Er (1–12) | 4.9% | 4.9% | 1.55 (0–4) | 3.63 (0–25) | 2.88zł (0.0–11.0) | 6.14 (0.7–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.