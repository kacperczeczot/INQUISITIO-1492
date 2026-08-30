# Raport Precyzyjnego Audytu Poziomu 3 (Parametry Pojedynczych Kart) — Wersja Balansu: v1.0-alpha.134

**Wersja Balansu:** `v1.0-alpha.134` | **Data:** 2026-08-30 09:22 | **Przeanalizowano Wariantów Kart:** 19 | **Próba:** 5000 gier/setup | **Czas:** 7.62s
**Filtry:** Parametry: `cost,heresy` | Frakcja: `all` | Karta: `gc-08`
**Wynik Bazy Poziomu 3 (Global):** `🟡 83.1 pkt` | 3p: `69.8 pkt` | 4p: `88.6 pkt` | 5p: `90.9 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (14)

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | Baza (Bieżące parametry wszystkich kart) | 83.1 → 🟡 ** 83.1** (`= 0.0`) | 69.8 → 69.8 (`= 0.0`) | 88.6 → 88.6 (`= 0.0`) | 90.9 → 90.9 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-08_COST_PLUS2` | GC-08 (Zatrute Złoto): cost 1 → 3 | 83.1 → 🟡 ** 83.6** (`⬆️ +0.5`) | 69.8 → 70.0 (`⬆️ +0.2`) | 88.6 → 89.0 (`⬆️ +0.4`) | 90.9 → 91.7 (`⬆️ +0.8`) | ⚪ OPTYMALNY |
| `L3_GC-08_C2_G2` | GC-08 (Zatrute Złoto): koszt 1→2, złoto 0→2 | 83.1 → 🟡 ** 83.4** (`⬆️ +0.3`) | 69.8 → 70.2 (`⬆️ +0.4`) | 88.6 → 89.3 (`⬆️ +0.7`) | 90.9 → 90.8 (`🔻 -0.1`) | ⚪ OPTYMALNY |
| `L3_GC-08_C2_G1` | GC-08 (Zatrute Złoto): koszt 1→2, złoto 0→1 | 83.1 → 🟡 ** 83.4** (`⬆️ +0.3`) | 69.8 → 70.0 (`⬆️ +0.2`) | 88.6 → 88.8 (`⬆️ +0.2`) | 90.9 → 91.4 (`⬆️ +0.5`) | ⚪ OPTYMALNY |
| `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 1 → 2 | 83.1 → 🟡 ** 83.3** (`⬆️ +0.2`) | 69.8 → 70.0 (`⬆️ +0.2`) | 88.6 → 89.3 (`⬆️ +0.7`) | 90.9 → 90.6 (`🔻 -0.3`) | ⚪ OPTYMALNY |
| `L3_GC-08_C2_H2` | GC-08 (Zatrute Złoto): koszt 1→2, herezja 1→2 | 83.1 → 🟡 ** 83.2** (`⬆️ +0.1`) | 69.8 → 70.0 (`⬆️ +0.2`) | 88.6 → 89.1 (`⬆️ +0.5`) | 90.9 → 90.4 (`🔻 -0.5`) | ⚪ OPTYMALNY |
| `L3_GC-08_COST_MINUS1` | GC-08 (Zatrute Złoto): cost 1 → 0 | 83.1 → 🟡 ** 83.1** (`= 0.0`) | 69.8 → 70.3 (`⬆️ +0.5`) | 88.6 → 88.8 (`⬆️ +0.2`) | 90.9 → 90.3 (`🔻 -0.6`) | ⚪ OPTYMALNY |
| `L3_GC-08_G1_H2` | GC-08 (Zatrute Złoto): złoto 0→1, herezja 1→2 | 83.1 → 🟡 ** 83.1** (`= 0.0`) | 69.8 → 70.2 (`⬆️ +0.4`) | 88.6 → 88.5 (`🔻 -0.1`) | 90.9 → 90.5 (`🔻 -0.4`) | ⚪ OPTYMALNY |
| `L3_GC-08_C0_H2` | GC-08 (Zatrute Złoto): koszt 1→0, herezja 1→2 | 83.1 → 🟡 ** 83.0** (`🔻 -0.1`) | 69.8 → 70.2 (`⬆️ +0.4`) | 88.6 → 88.6 (`= 0.0`) | 90.9 → 90.3 (`🔻 -0.6`) | ⚪ OPTYMALNY |
| `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 1 → 2 | 83.1 → 🟡 ** 83.0** (`🔻 -0.1`) | 69.8 → 70.1 (`⬆️ +0.3`) | 88.6 → 88.5 (`🔻 -0.1`) | 90.9 → 90.3 (`🔻 -0.6`) | ⚪ OPTYMALNY |
| `L3_GC-08_G0_H2` | GC-08 (Zatrute Złoto): złoto 0→0, herezja 1→2 | 83.1 → 🟡 ** 83.0** (`🔻 -0.1`) | 69.8 → 70.1 (`⬆️ +0.3`) | 88.6 → 88.5 (`🔻 -0.1`) | 90.9 → 90.3 (`🔻 -0.6`) | ⚪ OPTYMALNY |
| `L3_GC-08_HERESY_PLUS2` | GC-08 (Zatrute Złoto): heresy 1 → 3 | 83.1 → 🟡 ** 82.9** (`🔻 -0.2`) | 69.8 → 70.0 (`⬆️ +0.2`) | 88.6 → 88.6 (`= 0.0`) | 90.9 → 90.2 (`🔻 -0.7`) | ⚪ OPTYMALNY |
| `L3_GC-08_C0_G1` | GC-08 (Zatrute Złoto): koszt 1→0, złoto 0→1 | 83.1 → 🟡 ** 82.2** (`🔻 -0.9`) | 69.8 → 70.8 (`⬆️ +1.0`) | 88.6 → 89.7 (`⬆️ +1.1`) | 90.9 → 86.2 (`🔻 -4.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_C0_G2` | GC-08 (Zatrute Złoto): koszt 1→0, złoto 0→2 | 83.1 → 🟡 ** 81.6** (`🔻 -1.5`) | 69.8 → 70.7 (`⬆️ +0.9`) | 88.6 → 89.6 (`⬆️ +1.0`) | 90.9 → 84.4 (`🔻 -6.5`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 5 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_GC-08_C2_H0` | GC-08 (Zatrute Złoto): koszt 1→2, herezja 1→0 | 83.1 → 🟡 ** 81.0** (`🔻 -2.1`) | 69.8 → 69.4 (`🔻 -0.4`) | 88.6 → 88.2 (`🔻 -0.4`) | 90.9 → 85.5 (`🔻 -5.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_G1_H0` | GC-08 (Zatrute Złoto): złoto 0→1, herezja 1→0 | 83.1 → 🟡 ** 80.8** (`🔻 -2.3`) | 69.8 → 69.3 (`🔻 -0.5`) | 88.6 → 87.5 (`🔻 -1.1`) | 90.9 → 85.5 (`🔻 -5.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_C0_H0` | GC-08 (Zatrute Złoto): koszt 1→0, herezja 1→0 | 83.1 → 🟡 ** 80.7** (`🔻 -2.4`) | 69.8 → 69.2 (`🔻 -0.6`) | 88.6 → 87.5 (`🔻 -1.1`) | 90.9 → 85.4 (`🔻 -5.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_HERESY_MINUS1` | GC-08 (Zatrute Złoto): heresy 1 → 0 | 83.1 → 🟡 ** 80.5** (`🔻 -2.6`) | 69.8 → 69.0 (`🔻 -0.8`) | 88.6 → 88.4 (`🔻 -0.2`) | 90.9 → 84.2 (`🔻 -6.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_G0_H0` | GC-08 (Zatrute Złoto): złoto 0→0, herezja 1→0 | 83.1 → 🟡 ** 80.5** (`🔻 -2.6`) | 69.8 → 69.0 (`🔻 -0.8`) | 88.6 → 88.4 (`🔻 -0.2`) | 90.9 → 84.2 (`🔻 -6.7`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (14)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | 6.38 Er (8–1) | 0.1% | 3.8% | 1.67 (0–0) | 7.40 (0–0) | 10.64zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_PLUS2` | 6.37 Er (8–1) | 0.1% | 3.9% | 1.67 (0–0) | 7.40 (0–0) | 10.63zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_C2_G2` | 6.38 Er (8–1) | 0.1% | 3.8% | 1.67 (0–0) | 7.42 (0–0) | 10.62zł (0.0–0.0) | 7.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_C2_G1` | 6.37 Er (8–1) | 0.1% | 3.8% | 1.67 (0–0) | 7.39 (0–0) | 10.64zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_PLUS1` | 6.37 Er (8–1) | 0.1% | 3.9% | 1.67 (0–0) | 7.40 (0–0) | 10.63zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_C2_H2` | 6.37 Er (8–1) | 0.1% | 3.9% | 1.67 (0–0) | 7.40 (0–0) | 10.66zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_MINUS1` | 6.38 Er (8–1) | 0.1% | 3.8% | 1.67 (0–0) | 7.42 (0–0) | 10.62zł (0.0–0.0) | 7.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_G1_H2` | 6.37 Er (8–1) | 0.1% | 3.8% | 1.67 (0–0) | 7.40 (0–0) | 10.66zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_C0_H2` | 6.37 Er (8–1) | 0.1% | 3.8% | 1.67 (0–0) | 7.40 (0–0) | 10.66zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_HERESY_PLUS1` | 6.38 Er (8–1) | 0.1% | 3.8% | 1.67 (0–0) | 7.40 (0–0) | 10.66zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_G0_H2` | 6.38 Er (8–1) | 0.1% | 3.8% | 1.67 (0–0) | 7.40 (0–0) | 10.66zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_HERESY_PLUS2` | 6.38 Er (8–1) | 0.1% | 3.8% | 1.67 (0–0) | 7.40 (0–0) | 10.67zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_C0_G1` | 6.40 Er (8–1) | 0.1% | 3.8% | 1.68 (0–0) | 7.42 (0–0) | 10.82zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_C0_G2` | 6.39 Er (8–1) | 0.1% | 3.8% | 1.68 (0–0) | 7.39 (0–0) | 10.94zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 5 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_GC-08_C2_H0` | 6.38 Er (8–1) | 0.1% | 3.9% | 1.67 (0–0) | 7.37 (0–0) | 10.05zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_G1_H0` | 6.37 Er (8–1) | 0.1% | 3.8% | 1.67 (0–0) | 7.33 (0–0) | 10.44zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_C0_H0` | 6.38 Er (8–1) | 0.1% | 3.8% | 1.67 (0–0) | 7.33 (0–0) | 10.45zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_HERESY_MINUS1` | 6.38 Er (8–1) | 0.1% | 3.9% | 1.67 (0–0) | 7.35 (0–0) | 10.25zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_G0_H0` | 6.38 Er (8–1) | 0.1% | 3.9% | 1.67 (0–0) | 7.35 (0–0) | 10.25zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |

</details>