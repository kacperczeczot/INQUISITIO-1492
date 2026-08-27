[Strona główna](../../../../../README.md) > [v0.98](README.md) > [audyt_level1_raport](audyt_level1_raport.md)

---

# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v0.98

**Wersja Balansu:** `v0.98` | **Data:** 2026-08-17 23:02 | **Przeanalizowano Wariantów:** 19 | **Próba:** 3000 gier/setup | **Czas:** 201.06s
**Wynik Bazy Poziomu 1 (Global):** `🔴 3.7 pkt` | 3p: `3.0 pkt` | 4p: `4.7 pkt` | 5p: `3.5 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (15)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🔴 **  3.7** | 3.0 | 4.7 | 3.5 | ⚪ OPTYMALNY |
| `L1_INTRIGUE_GOLD_MINUS1` | Akcja Gospodarcza: 1 → 0 | 3.7 → 🔴 ** 24.4** (`⬆️ +20.7`) | 3.0 → 19.4 (`⬆️ +16.4`) | 4.7 → 37.0 (`⬆️ +32.3`) | 3.5 → 16.7 (`⬆️ +13.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_OBSERVED_PLUS1` | Próg Obserwowanej: 4 → 5 | 3.7 → 🔴 **  5.5** (`⬆️ +1.8`) | 3.0 → 2.6 (`-0.4`) | 4.7 → 6.0 (`⬆️ +1.3`) | 3.5 → 7.9 (`⬆️ +4.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 3.7 → 🔴 **  5.2** (`⬆️ +1.5`) | 3.0 → 2.0 (`-1.0`) | 4.7 → 3.1 (`-1.6`) | 3.5 → 10.5 (`⬆️ +7.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_CARDS_PER_ERA_PLUS1` | Karty/Erę: 2 → 3 | 3.7 → 🔴 **  4.4** (`⬆️ +0.7`) | 3.0 → 5.1 (`⬆️ +2.1`) | 4.7 → 5.5 (`⬆️ +0.8`) | 3.5 → 2.5 (`-1.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 3.7 → 🔴 **  4.4** (`⬆️ +0.7`) | 3.0 → 4.4 (`⬆️ +1.4`) | 4.7 → 5.5 (`⬆️ +0.8`) | 3.5 → 3.2 (`-0.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 6/7/8 → 5/6/7 | 3.7 → 🔴 **  4.2** (`⬆️ +0.5`) | 3.0 → 1.4 (`-1.6`) | 4.7 → 7.3 (`⬆️ +2.6`) | 3.5 → 4.0 (`⬆️ +0.5`) | ⚪ OPTYMALNY |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 4zł → 5zł | 3.7 → 🔴 **  4.0** (`⬆️ +0.3`) | 3.0 → 4.0 (`⬆️ +1.0`) | 4.7 → 5.0 (`⬆️ +0.3`) | 3.5 → 3.0 (`-0.5`) | ⚪ OPTYMALNY |
| `L1_OBSERVED_MINUS1` | Próg Obserwowanej: 4 → 3 | 3.7 → 🔴 **  4.0** (`⬆️ +0.3`) | 3.0 → 3.9 (`⬆️ +0.9`) | 4.7 → 5.4 (`⬆️ +0.7`) | 3.5 → 2.8 (`-0.7`) | ⚪ OPTYMALNY |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 6/7/8 → 7/8/9 | 3.7 → 🔴 **  3.9** (`⬆️ +0.2`) | 3.0 → 3.8 (`⬆️ +0.8`) | 4.7 → 4.4 (`-0.3`) | 3.5 → 3.4 (`-0.1`) | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 12 → 13 | 3.7 → 🔴 **  3.9** (`⬆️ +0.2`) | 3.0 → 3.4 (`⬆️ +0.4`) | 4.7 | 3.5 | ⚪ OPTYMALNY |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 4zł → 3zł | 🔴 **  3.7** | 3.0 → 2.7 (`-0.3`) | 4.7 → 4.6 (`-0.1`) | 3.5 → 3.7 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 3.7 → 🔴 **  3.4** (`-0.3`) | 3.0 → 3.9 (`⬆️ +0.9`) | 4.7 → 4.1 (`-0.6`) | 3.5 → 2.2 (`-1.3`) | ⚪ OPTYMALNY |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 3.7 → 🔴 **  3.3** (`-0.4`) | 3.0 → 3.3 (`⬆️ +0.3`) | 4.7 → 3.4 (`-1.3`) | 3.5 → 3.1 (`-0.4`) | ⚪ OPTYMALNY |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 3.7 → 🔴 **  3.3** (`-0.4`) | 3.0 → 3.1 (`⬆️ +0.1`) | 4.7 → 4.2 (`-0.5`) | 3.5 → 2.7 (`-0.8`) | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 4 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 12 → 11 | 🔴 **  3.7** | 3.0 | 4.7 | 3.5 | ⚪ OPTYMALNY |
| `L1_CARDS_PER_ERA_MINUS1` | Karty/Erę: 2 → 1 | 3.7 → 🔴 **  3.2** (`-0.5`) | 3.0 → 1.6 (`-1.4`) | 4.7 | 3.5 → 3.2 (`-0.3`) | ⚪ OPTYMALNY |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 3.7 → 🔴 **  1.7** (`-2.0`) | 3.0 → 2.1 (`-0.9`) | 4.7 → 1.5 (`-3.2`) | 3.5 → 1.4 (`-2.1`) | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_PLUS1` | Akcja Gospodarcza: 1 → 2 | 3.7 → 🔴 **  0.8** (`-2.9`) | 3.0 → 0.6 (`-2.4`) | 4.7 → 0.8 (`-3.9`) | 3.5 → 1.0 (`-2.5`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (15)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 6.15 Er (2–12) | 8.5% | 0.8% | 2.02 (0–5) | 4.58 (0–28) | 17.77zł (1.3–44.3) | 6.21 (1.4–10.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_MINUS1` | 4.99 Er (2–12) | 0.9% | 4.0% | 1.70 (0–5) | 4.49 (0–26) | 4.93zł (0.0–18.7) | 7.08 (2.0–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L1_OBSERVED_PLUS1` | 6.35 Er (2–12) | 10.4% | 0.8% | 2.05 (0–5) | 4.93 (0–28) | 18.40zł (1.3–44.3) | 6.30 (1.4–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 6.70 Er (2–12) | 11.7% | 0.6% | 2.14 (0–5) | 4.83 (0–27) | 20.27zł (1.3–44.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L1_CARDS_PER_ERA_PLUS1` | 5.86 Er (1–12) | 7.9% | 1.8% | 1.82 (0–5) | 4.23 (0–27) | 22.64zł (0.7–57.7) | 5.98 (1.2–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.71 Er (2–12) | 6.0% | 1.1% | 1.93 (0–5) | 4.33 (0–28) | 15.68zł (1.0–44.3) | 6.23 (1.5–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 6.66 Er (2–12) | 9.5% | 0.7% | 2.13 (0–5) | 6.82 (0–29) | 19.51zł (1.2–44.3) | 6.50 (1.4–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.82 Er (1–12) | 7.9% | 0.6% | 1.88 (0–5) | 4.33 (0–27) | 17.80zł (0.7–45.3) | 5.98 (1.2–10.0) | 🟢 W NORMIE |
| `L1_OBSERVED_MINUS1` | 5.94 Er (2–12) | 6.9% | 0.8% | 1.99 (0–5) | 4.17 (0–28) | 17.11zł (1.3–44.3) | 6.06 (1.3–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_PLUS1` | 5.81 Er (2–12) | 7.4% | 0.9% | 1.92 (0–5) | 3.04 (0–26) | 16.56zł (1.7–44.3) | 6.09 (1.4–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 6.22 Er (2–13) | 6.2% | 0.8% | 2.02 (0–5) | 4.69 (0–30) | 17.95zł (1.3–47.3) | 6.22 (1.4–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 6.24 Er (2–12) | 8.8% | 1.1% | 2.05 (0–5) | 4.60 (0–27) | 17.13zł (0.7–43.3) | 6.23 (1.5–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 6.68 Er (2–12) | 14.6% | 0.8% | 1.62 (0–4) | 4.22 (0–26) | 19.57zł (1.3–44.7) | 5.74 (1.4–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 7.07 Er (2–12) | 17.5% | 0.8% | 2.13 (0–5) | 5.22 (0–28) | 20.08zł (1.3–44.0) | 5.86 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L1_AGENTS_PLUS1` | 5.34 Er (2–12) | 4.8% | 0.9% | 1.80 (0–5) | 4.12 (0–27) | 15.28zł (1.3–43.3) | 6.26 (1.4–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 4 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_MAX_ERAS_MINUS1` | 6.07 Er (2–11) | 9.3% | 0.8% | 1.99 (0–4) | 4.41 (0–25) | 17.54zł (1.3–41.3) | 6.18 (1.4–10.0) | 🟢 W NORMIE |
| `L1_CARDS_PER_ERA_MINUS1` | 6.87 Er (2–12) | 11.8% | 0.1% | 2.21 (0–5) | 5.21 (0–27) | 13.26zł (0.7–31.0) | 6.32 (1.3–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.37 Er (2–12) | 6.6% | 0.9% | 2.52 (0–6) | 4.73 (0–28) | 15.22zł (1.3–43.7) | 6.57 (1.7–10.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_PLUS1` | 7.30 Er (2–12) | 17.6% | 0.0% | 2.13 (0–4) | 4.39 (0–24) | 37.12zł (2.7–66.7) | 5.74 (1.0–10.0) | 🔴 PRZEKROCZONE NORMY |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.