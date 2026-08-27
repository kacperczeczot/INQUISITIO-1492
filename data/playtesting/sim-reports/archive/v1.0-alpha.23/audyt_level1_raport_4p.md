[Strona główna](../../../../../README.md) > [v1.0-alpha.23](README.md) > [audyt_level1_raport_4p](audyt_level1_raport_4p.md)

---

# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v1.0-alpha.23

**Wersja Balansu:** `v1.0-alpha.23` | **Data:** 2026-08-22 15:07 | **Przeanalizowano Wariantów:** 19 | **Próba:** 3000 gier/setup | **Czas:** 96.61s
**Wynik Bazy Poziomu 1 (Global):** `🟡 81.1 pkt` | 3p: `0.0 pkt` | 4p: `81.1 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (2)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🟡 ** 81.1** | 0.0 | 81.1 | 0.0 | ⚪ OPTYMALNY |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 4zł → 5zł | 81.1 → 🟡 ** 84.3** (`⬆️ +3.2`) | 0.0 | 81.1 → 84.3 (`⬆️ +3.2`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 17 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 7 → 8 | 🟡 ** 81.1** | 0.0 | 81.1 | 0.0 | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 14 → 15 | 🟡 ** 81.1** | 0.0 | 81.1 | 0.0 | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 14 → 13 | 🟡 ** 81.1** | 0.0 | 81.1 | 0.0 | ⚪ OPTYMALNY |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 4zł → 3zł | 81.1 → 🟡 ** 80.5** (`-0.6`) | 0.0 | 81.1 → 80.5 (`-0.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 7 → 6 | 81.1 → 🟠 ** 70.4** (`-10.7`) | 0.0 | 81.1 → 70.4 (`-10.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_OBSERVED_PLUS1` | Próg Obserwowanej: 5 → 6 | 81.1 → 🟠 ** 70.3** (`-10.8`) | 0.0 | 81.1 → 70.3 (`-10.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 81.1 → 🟠 ** 64.7** (`-16.4`) | 0.0 | 81.1 → 64.7 (`-16.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_OBSERVED_MINUS1` | Próg Obserwowanej: 5 → 4 | 81.1 → 🟠 ** 62.5** (`-18.6`) | 0.0 | 81.1 → 62.5 (`-18.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 81.1 → 🔴 ** 55.1** (`-26.0`) | 0.0 | 81.1 → 55.1 (`-26.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 81.1 → 🔴 ** 51.5** (`-29.6`) | 0.0 | 81.1 → 51.5 (`-29.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_CARDS_PER_ERA_PLUS1` | Karty/Erę: 2 → 3 | 81.1 → 🔴 ** 47.7** (`-33.4`) | 0.0 | 81.1 → 47.7 (`-33.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_CARDS_PER_ERA_MINUS1` | Karty/Erę: 2 → 1 | 81.1 → 🔴 ** 40.9** (`-40.2`) | 0.0 | 81.1 → 40.9 (`-40.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 81.1 → 🔴 ** 38.2** (`-42.9`) | 0.0 | 81.1 → 38.2 (`-42.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 81.1 → 🔴 ** 36.4** (`-44.7`) | 0.0 | 81.1 → 36.4 (`-44.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 81.1 → 🔴 ** 34.5** (`-46.6`) | 0.0 | 81.1 → 34.5 (`-46.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_MINUS1` | Akcja Gospodarcza: 1 → 0 | 81.1 → 🔴 ** 16.2** (`-64.9`) | 0.0 | 81.1 → 16.2 (`-64.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_PLUS1` | Akcja Gospodarcza: 1 → 2 | 81.1 → 🔴 ** 16.1** (`-65.0`) | 0.0 | 81.1 → 16.1 (`-65.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (2)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 6.03 Er (1–14) | 0.1% | 1.5% | 1.72 (0–4) | 3.95 (0–26) | 15.14zł (1.5–45.2) | 6.76 (0.2–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 17 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_THRESHOLD_PLUS1` | 6.03 Er (1–14) | 0.1% | 1.5% | 1.72 (0–4) | 3.95 (0–26) | 15.14zł (1.5–45.2) | 6.76 (0.2–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 6.03 Er (1–15) | 0.1% | 1.5% | 1.72 (0–5) | 3.96 (0–30) | 15.15zł (1.5–48.2) | 6.76 (0.2–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 6.03 Er (1–13) | 0.3% | 1.5% | 1.72 (0–4) | 3.95 (0–22) | 15.14zł (1.5–42.8) | 6.76 (0.2–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 6.11 Er (1–14) | 0.1% | 1.3% | 1.76 (0–4) | 3.98 (0–22) | 14.57zł (1.5–45.0) | 6.74 (0.2–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 6.12 Er (1–14) | 0.2% | 1.3% | 1.75 (0–4) | 6.37 (0–28) | 15.67zł (1.5–45.8) | 6.59 (0.2–10.0) | 🟢 W NORMIE |
| `L1_OBSERVED_PLUS1` | 6.05 Er (1–14) | 0.2% | 1.5% | 1.72 (0–4) | 4.12 (0–26) | 15.02zł (1.5–47.0) | 6.82 (0.2–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 6.43 Er (1–14) | 0.6% | 1.5% | 1.22 (0–3) | 3.86 (0–24) | 16.25zł (1.5–49.5) | 6.39 (0.2–10.0) | 🟢 W NORMIE |
| `L1_OBSERVED_MINUS1` | 5.91 Er (1–14) | 0.1% | 1.4% | 1.70 (0–4) | 3.67 (0–19) | 14.99zł (1.5–46.5) | 6.66 (0.2–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 5.58 Er (1–13) | 0.0% | 1.5% | 1.60 (0–4) | 3.63 (0–16) | 13.93zł (2.0–41.2) | 6.83 (0.2–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 6.51 Er (1–14) | 0.2% | 1.1% | 1.90 (0–4) | 4.14 (0–18) | 17.78zł (2.0–47.2) | 6.80 (0.2–10.0) | 🟢 W NORMIE |
| `L1_CARDS_PER_ERA_PLUS1` | 5.66 Er (2–14) | 0.2% | 2.6% | 1.55 (0–4) | 3.65 (0–22) | 19.25zł (3.5–63.0) | 6.60 (0.5–10.0) | 🟢 W NORMIE |
| `L1_CARDS_PER_ERA_MINUS1` | 6.91 Er (2–14) | 0.3% | 0.1% | 2.03 (0–4) | 4.28 (0–28) | 11.62zł (2.2–32.0) | 6.90 (0.2–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 7.20 Er (2–14) | 2.1% | 1.5% | 2.00 (0–4) | 4.53 (0–26) | 18.21zł (2.2–48.0) | 6.53 (0.5–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.33 Er (1–14) | 0.1% | 1.4% | 2.27 (0–6) | 3.87 (0–30) | 13.54zł (1.5–47.8) | 7.05 (0.2–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.55 Er (1–14) | 0.0% | 1.8% | 1.53 (0–4) | 3.64 (0–21) | 12.74zł (1.5–40.5) | 6.60 (0.2–10.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_MINUS1` | 5.42 Er (1–12) | 0.0% | 3.9% | 1.94 (0–5) | 4.29 (0–19) | 6.87zł (1.0–17.0) | 7.01 (0.2–10.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_PLUS1` | 7.13 Er (1–14) | 1.3% | 0.1% | 2.07 (0–4) | 4.49 (0–24) | 33.06zł (3.5–75.0) | 6.56 (0.2–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.