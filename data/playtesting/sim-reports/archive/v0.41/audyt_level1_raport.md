[Strona główna](../../../../../README.md) > [v0.41](README.md) > [audyt_level1_raport](audyt_level1_raport.md)

---

# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.41

**Wersja Balansu:** `v0.41` | **Data:** 2026-08-16 00:16 | **Przeanalizowano Wariantów:** 13 | **Próba:** 5000 gier/setup | **Czas:** 344.19s
**Wynik Bazy Poziomu 1 (Global):** `🔴 27.6 pkt` | 3p: `38.5 pkt` | 4p: `16.7 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (8)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🔴 ** 27.6** | 38.5 | 16.7 | 0.0 | ⚪ OPTYMALNY |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 3/3/3zł → 4/4/4zł | 27.6 → 🟠 ** 74.2** (`⬆️ +46.6`) | 38.5 → 81.2 (`⬆️ +42.7`) | 16.7 → 67.1 (`⬆️ +50.4`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 27.6 → 🟠 ** 64.0** (`⬆️ +36.4`) | 38.5 → 53.5 (`⬆️ +15.0`) | 16.7 → 60.3 (`⬆️ +43.6`) | 0.0 → 78.3 (`⬆️ +78.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 27.6 → 🔴 ** 36.8** (`⬆️ +9.2`) | 38.5 → 36.4 (`-2.1`) | 16.7 → 0.0 (`-16.7`) | 0.0 → 37.1 (`⬆️ +37.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 27.6 → 🔴 ** 31.8** (`⬆️ +4.2`) | 38.5 → 42.9 (`⬆️ +4.4`) | 16.7 → 20.7 (`⬆️ +4.0`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/8 → 5/6/7 | 27.6 → 🔴 ** 30.5** (`⬆️ +2.9`) | 38.5 → 41.4 (`⬆️ +2.9`) | 16.7 → 19.7 (`⬆️ +3.0`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 27.6 → 🔴 ** 27.8** (`⬆️ +0.2`) | 38.5 → 38.6 (`⬆️ +0.1`) | 16.7 → 16.9 (`⬆️ +0.2`) | 0.0 | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 11 → 12 | 27.6 → 🔴 ** 27.7** (`⬆️ +0.1`) | 38.5 → 38.6 (`⬆️ +0.1`) | 16.7 → 16.8 (`⬆️ +0.1`) | 0.0 | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 5 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 27.6 → 🔴 ** 27.4** (`-0.2`) | 38.5 → 38.4 (`-0.1`) | 16.7 → 16.3 (`-0.4`) | 0.0 | ⚪ OPTYMALNY |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 3/3/3zł → 2/2/2zł | 27.6 → 🔴 ** 25.8** (`-1.8`) | 38.5 → 25.8 (`-12.7`) | 16.7 → 0.0 (`-16.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 11 → 10 | 27.6 → 🔴 ** 25.7** (`-1.9`) | 38.5 → 34.7 (`-3.8`) | 16.7 → 16.6 (`-0.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 27.6 → 🔴 ** 23.5** (`-4.1`) | 38.5 → 23.5 (`-15.0`) | 16.7 → 0.0 (`-16.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 27.6 → 🔴 ** 14.8** (`-12.8`) | 38.5 → 27.0 (`-11.5`) | 16.7 → 2.6 (`-14.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (8)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 6.13 Er (1–11) | 1.6% | 26.1% | 0.46 (0–3) | 3.13 (0–18) | 1.20zł (0.0–6.0) | 5.83 (0.0–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.57 Er (1–11) | 0.8% | 25.1% | 0.56 (0–3) | 3.44 (0–19) | 1.50zł (0.0–7.7) | 6.01 (1.0–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 6.40 Er (1–11) | 2.2% | 32.5% | 0.50 (0–3) | 3.21 (0–20) | 1.50zł (0.0–7.3) | 5.83 (0.7–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_THRESHOLD_PLUS1` | 6.26 Er (1–11) | 1.9% | 26.4% | 0.47 (0–3) | 2.25 (0–18) | 1.22zł (0.0–6.7) | 5.74 (0.0–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 6.05 Er (1–11) | 1.2% | 25.7% | 0.52 (0–4) | 3.10 (0–19) | 1.21zł (0.0–7.0) | 5.91 (0.3–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 5.99 Er (1–11) | 1.4% | 25.7% | 0.45 (0–3) | 3.97 (0–23) | 1.18zł (0.0–6.3) | 5.89 (0.0–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 6.12 Er (1–11) | 1.6% | 26.1% | 0.47 (0–4) | 3.13 (0–18) | 1.20zł (0.0–6.0) | 5.83 (0.0–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 6.13 Er (1–12) | 0.6% | 26.1% | 0.46 (0–3) | 3.14 (0–20) | 1.19zł (0.0–6.7) | 5.83 (0.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 5 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 6.13 Er (1–11) | 1.6% | 26.1% | 0.45 (0–3) | 3.13 (0–18) | 1.20zł (0.0–6.0) | 5.82 (0.0–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 6.39 Er (1–11) | 2.6% | 28.6% | 0.38 (0–3) | 2.89 (0–20) | 0.94zł (0.0–5.7) | 5.61 (0.0–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 6.11 Er (1–10) | 3.9% | 26.1% | 0.46 (0–3) | 3.12 (0–18) | 1.21zł (0.0–7.0) | 5.82 (0.0–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.85 Er (1–11) | 1.1% | 20.6% | 0.43 (0–4) | 2.83 (0–20) | 0.99zł (0.0–7.0) | 5.76 (0.7–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 6.38 Er (1–11) | 2.8% | 27.3% | 0.35 (0–3) | 3.28 (0–19) | 1.13zł (0.0–6.7) | 5.80 (0.3–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.