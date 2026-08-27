[Strona główna](../../../../../README.md) > [v1.0-alpha.24](README.md) > [audyt_level1_raport_4p](audyt_level1_raport_4p.md)

---

# Raport Audytu Poziomu 1 (Główne Mechaniki Systemowe) — Wersja Balansu: v1.0-alpha.24

**Wersja Balansu:** `v1.0-alpha.24` | **Data:** 2026-08-22 18:05 | **Przeanalizowano Wariantów:** 20 | **Próba:** 3000 gier/setup | **Czas:** 97.76s
**Wynik Bazy Poziomu 1 (Global):** `🟡 84.3 pkt` | 3p: `0.0 pkt` | 4p: `84.3 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (1)

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | Baza (Bieżące parametry systemowe) | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 19 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Element Poziomu 1 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L1_THRESHOLD_PLUS1` | Próg Oskarżenia: 7 → 8 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_PLUS1` | Limit Er: 14 → 15 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L1_MAX_ERAS_MINUS1` | Limit Er: 14 → 13 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L1_START_GOLD_MINUS1` | Złoto startowe: 5zł → 4zł | 84.3 → 🟡 ** 81.1** (`-3.2`) | 0.0 | 84.3 → 81.1 (`-3.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_START_GOLD_PLUS1` | Złoto startowe: 5zł → 6zł | 84.3 → 🟡 ** 77.9** (`-6.4`) | 0.0 | 84.3 → 77.9 (`-6.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_THRESHOLD_MINUS1` | Próg Oskarżenia: 7 → 6 | 84.3 → 🟠 ** 71.7** (`-12.6`) | 0.0 | 84.3 → 71.7 (`-12.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_OBSERVED_PLUS1` | Próg Obserwowanej: 5 → 6 | 84.3 → 🟠 ** 70.1** (`-14.2`) | 0.0 | 84.3 → 70.1 (`-14.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_OBSERVED_MINUS1` | Próg Obserwowanej: 5 → 4 | 84.3 → 🟠 ** 66.8** (`-17.5`) | 0.0 | 84.3 → 66.8 (`-17.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | Cooldown Autodafé: 3 → 4 Ery | 84.3 → 🔴 ** 58.4** (`-25.9`) | 0.0 | 84.3 → 58.4 (`-25.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_MINUS1` | Limit ręki: 5 → 4 | 84.3 → 🔴 ** 53.9** (`-30.4`) | 0.0 | 84.3 → 53.9 (`-30.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_PLUS1` | Agenci: 3 → 4 | 84.3 → 🔴 ** 51.4** (`-32.9`) | 0.0 | 84.3 → 51.4 (`-32.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_CARDS_PER_ERA_MINUS1` | Karty/Erę: 2 → 1 | 84.3 → 🔴 ** 47.8** (`-36.5`) | 0.0 | 84.3 → 47.8 (`-36.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_CARDS_PER_ERA_PLUS1` | Karty/Erę: 2 → 3 | 84.3 → 🔴 ** 42.9** (`-41.4`) | 0.0 | 84.3 → 42.9 (`-41.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_AGENTS_MINUS1` | Agenci: 3 → 2 | 84.3 → 🔴 ** 41.2** (`-43.1`) | 0.0 | 84.3 → 41.2 (`-43.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | Cooldown Autodafé: 3 → 2 Ery | 84.3 → 🔴 ** 40.3** (`-44.0`) | 0.0 | 84.3 → 40.3 (`-44.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_HAND_LIMIT_PLUS1` | Limit ręki: 5 → 6 | 84.3 → 🔴 ** 33.6** (`-50.7`) | 0.0 | 84.3 → 33.6 (`-50.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_MINUS1` | Akcja Gospodarcza: 1 → 0 | 84.3 → 🔴 ** 17.6** (`-66.7`) | 0.0 | 84.3 → 17.6 (`-66.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_PLUS1` | Akcja Gospodarcza: 1 → 2 | 84.3 → 🔴 ** 15.1** (`-69.2`) | 0.0 | 84.3 → 15.1 (`-69.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L1_INTRIGUE_GOLD_DOUBLE` | Akcja Gospodarcza: 1 → 2 (podwojenie) | 84.3 → 🔴 ** 15.1** (`-69.2`) | 0.0 | 84.3 → 15.1 (`-69.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (1)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_BAZA` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 19 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L1_THRESHOLD_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_PLUS1` | 5.98 Er (1–15) | 0.1% | 1.0% | 1.70 (0–5) | 3.91 (0–25) | 15.82zł (2.2–49.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L1_MAX_ERAS_MINUS1` | 5.97 Er (1–13) | 0.2% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–43.8) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_MINUS1` | 6.03 Er (1–14) | 0.1% | 1.5% | 1.72 (0–4) | 3.95 (0–26) | 15.14zł (1.5–45.2) | 6.76 (0.2–10.0) | 🟢 W NORMIE |
| `L1_START_GOLD_PLUS1` | 5.87 Er (1–14) | 0.1% | 1.0% | 1.66 (0–4) | 3.83 (0–20) | 16.37zł (3.2–47.2) | 6.71 (0.2–10.0) | 🟢 W NORMIE |
| `L1_THRESHOLD_MINUS1` | 6.06 Er (1–14) | 0.1% | 0.9% | 1.72 (0–4) | 6.26 (0–30) | 16.30zł (2.2–47.0) | 6.56 (0.2–10.0) | 🟢 W NORMIE |
| `L1_OBSERVED_PLUS1` | 5.99 Er (1–14) | 0.2% | 1.0% | 1.70 (0–4) | 4.09 (0–22) | 15.68zł (2.2–46.8) | 6.78 (0.2–10.0) | 🟢 W NORMIE |
| `L1_OBSERVED_MINUS1` | 5.87 Er (1–14) | 0.1% | 0.9% | 1.68 (0–4) | 3.65 (0–22) | 15.73zł (2.2–46.2) | 6.63 (0.2–10.0) | 🟢 W NORMIE |
| `L1_AUTODAFE_COOLDOWN_PLUS1` | 6.39 Er (1–14) | 0.5% | 1.0% | 1.21 (0–3) | 3.84 (0–29) | 16.97zł (2.2–49.8) | 6.36 (0.2–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_MINUS1` | 6.46 Er (1–14) | 0.3% | 0.7% | 1.88 (0–4) | 4.12 (0–25) | 18.56zł (2.8–48.2) | 6.75 (0.2–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_PLUS1` | 5.50 Er (1–14) | 0.0% | 1.0% | 1.56 (0–4) | 3.56 (0–26) | 14.50zł (2.8–42.2) | 6.78 (0.2–10.0) | 🟢 W NORMIE |
| `L1_CARDS_PER_ERA_MINUS1` | 6.79 Er (2–14) | 0.2% | 0.1% | 1.99 (0–4) | 4.14 (0–19) | 12.22zł (3.2–33.8) | 6.86 (0.2–10.0) | 🟢 W NORMIE |
| `L1_CARDS_PER_ERA_PLUS1` | 5.58 Er (2–14) | 0.1% | 1.7% | 1.52 (0–4) | 3.57 (0–22) | 19.82zł (4.2–63.0) | 6.57 (0.8–10.0) | 🟢 W NORMIE |
| `L1_AGENTS_MINUS1` | 7.08 Er (2–14) | 2.0% | 0.9% | 1.96 (0–4) | 4.41 (0–24) | 18.72zł (2.5–48.8) | 6.46 (0.5–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L1_AUTODAFE_COOLDOWN_MINUS1` | 5.25 Er (1–14) | 0.1% | 1.0% | 2.24 (0–6) | 3.80 (0–24) | 14.11zł (2.2–45.8) | 7.01 (0.2–10.0) | 🟢 W NORMIE |
| `L1_HAND_LIMIT_PLUS1` | 5.46 Er (1–14) | 0.0% | 1.2% | 1.49 (0–4) | 3.60 (0–21) | 13.28zł (2.2–42.0) | 6.58 (0.2–10.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_MINUS1` | 5.37 Er (1–12) | 0.0% | 3.1% | 1.95 (0–5) | 4.32 (0–16) | 7.50zł (1.0–21.0) | 7.04 (0.0–10.0) | 🟢 W NORMIE |
| `L1_INTRIGUE_GOLD_PLUS1` | 7.15 Er (1–14) | 1.3% | 0.1% | 2.07 (0–4) | 4.52 (0–24) | 34.15zł (3.2–75.5) | 6.54 (0.2–10.0) | ⚠️ WARTOŚCI BRZEGOWE |
| `L1_INTRIGUE_GOLD_DOUBLE` | 7.15 Er (1–14) | 1.3% | 0.1% | 2.07 (0–4) | 4.52 (0–24) | 34.15zł (3.2–75.5) | 6.54 (0.2–10.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.