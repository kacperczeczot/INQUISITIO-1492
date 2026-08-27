[Strona główna](../../../../../README.md) > [v0.70](README.md) > [audyt_level1_raport](audyt_level1_raport.md)

---

# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.70

**Wersja Balansu:** `v0.70` | **Data:** 2026-08-16 20:22 | **Przeanalizowano Wariantów:** 13 | **Próba:** 3000 gier/setup | **Czas:** 310.89s
**Wynik Bazy Poziomu 1 (Global):** `🟠 63.8 pkt` | 3p: `72.9 pkt` | 4p: `69.4 pkt` | 5p: `49.1 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (7)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🟠 ** 63.8** | 72.9 | 69.4 | 49.1 | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 63.8 → 🟠 ** 74.0** (`⬆️ +10.2`) | 72.9 → 74.4 (`⬆️ +1.5`) | 69.4 → 82.6 (`⬆️ +13.2`) | 49.1 → 64.9 (`⬆️ +15.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 63.8 → 🟠 ** 73.9** (`⬆️ +10.1`) | 72.9 → 72.6 (`-0.3`) | 69.4 → 86.4 (`⬆️ +17.0`) | 49.1 → 62.8 (`⬆️ +13.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 12 → 11 | 63.8 → 🟠 ** 63.9** (`⬆️ +0.1`) | 72.9 → 73.1 (`⬆️ +0.2`) | 69.4 | 49.1 | ⚪ OPTYMALNY |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 63.8 → 🟠 ** 63.7** (`-0.1`) | 72.9 → 66.2 (`-6.7`) | 69.4 → 71.6 (`⬆️ +2.2`) | 49.1 → 53.4 (`⬆️ +4.3`) | ⚪ OPTYMALNY |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 63.8 → 🟠 ** 61.2** (`-2.6`) | 72.9 → 68.8 (`-4.1`) | 69.4 → 65.4 (`-4.0`) | 49.1 → 49.5 (`⬆️ +0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 63.8 → 🔴 ** 58.2** (`-5.6`) | 72.9 → 75.8 (`⬆️ +2.9`) | 69.4 → 59.4 (`-10.0`) | 49.1 → 39.3 (`-9.8`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 6 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 12 → 13 | 🟠 ** 63.8** | 72.9 → 72.8 (`-0.1`) | 69.4 | 49.1 | ⚪ OPTYMALNY |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 63.8 → 🔴 ** 56.6** (`-7.2`) | 72.9 → 64.0 (`-8.9`) | 69.4 → 60.1 (`-9.3`) | 49.1 → 45.8 (`-3.3`) | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/8 → 5/6/7 | 63.8 → 🔴 ** 55.4** (`-8.4`) | 72.9 → 71.6 (`-1.3`) | 69.4 → 55.1 (`-14.3`) | 49.1 → 39.6 (`-9.5`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 4zł → 5zł | 63.8 → 🔴 ** 49.3** (`-14.5`) | 72.9 → 53.1 (`-19.8`) | 69.4 → 54.2 (`-15.2`) | 49.1 → 40.7 (`-8.4`) | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 4zł → 3zł | 63.8 → 🔴 ** 49.2** (`-14.6`) | 72.9 → 61.8 (`-11.1`) | 69.4 → 48.3 (`-21.1`) | 49.1 → 37.6 (`-11.5`) | 🔴 POGARSZA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 63.8 → 🔴 ** 45.7** (`-18.1`) | 72.9 → 60.0 (`-12.9`) | 69.4 → 48.5 (`-20.9`) | 49.1 → 28.7 (`-20.4`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (7)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 5.73 Er (1–12) | 0.6% | 24.9% | 1.48 (0–4) | 3.56 (0–21) | 1.62zł (0.0–7.7) | 6.56 (0.7–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 5.81 Er (1–12) | 0.6% | 25.1% | 1.15 (0–4) | 3.54 (0–20) | 1.63zł (0.0–8.3) | 6.47 (0.7–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_PLUS1` | 5.81 Er (1–12) | 0.6% | 25.1% | 1.51 (0–4) | 2.72 (0–17) | 1.63zł (0.0–8.3) | 6.48 (0.7–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 5.72 Er (1–11) | 1.4% | 24.9% | 1.48 (0–4) | 3.56 (0–21) | 1.62zł (0.0–7.7) | 6.56 (0.7–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 6.01 Er (1–12) | 0.8% | 31.6% | 1.56 (0–4) | 3.62 (0–19) | 1.96zł (0.0–8.3) | 6.51 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_AGENTS_MINUS1` | 5.95 Er (1–12) | 0.9% | 26.1% | 1.43 (0–4) | 3.71 (0–27) | 1.56zł (0.0–7.3) | 6.45 (0.7–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.55 Er (1–12) | 0.3% | 19.9% | 1.44 (0–4) | 3.48 (0–20) | 1.41zł (0.0–7.0) | 6.59 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 6 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_MAX_ERAS_PLUS1` | 5.73 Er (1–13) | 0.3% | 24.9% | 1.48 (0–4) | 3.57 (0–22) | 1.62zł (0.0–7.3) | 6.56 (0.7–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 5.60 Er (1–12) | 0.4% | 24.4% | 1.48 (0–4) | 3.47 (0–20) | 1.63zł (0.0–7.3) | 6.69 (0.7–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 5.65 Er (1–12) | 0.5% | 24.7% | 1.45 (0–4) | 4.39 (0–20) | 1.61zł (0.0–7.3) | 6.62 (0.7–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.33 Er (1–12) | 0.4% | 23.7% | 1.47 (0–4) | 3.55 (0–21) | 1.98zł (0.0–8.3) | 6.66 (0.5–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 6.01 Er (1–12) | 0.8% | 26.6% | 1.55 (0–4) | 3.62 (0–21) | 1.29zł (0.0–7.0) | 6.49 (0.7–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.58 Er (1–12) | 0.4% | 24.5% | 2.03 (0–6) | 3.58 (0–19) | 1.60zł (0.0–7.7) | 6.68 (0.7–10.0) | 🟢 W NORMIE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.