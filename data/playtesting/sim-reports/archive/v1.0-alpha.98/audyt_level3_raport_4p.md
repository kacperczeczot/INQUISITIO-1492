# Raport Precyzyjnego Audytu Poziomu 3 (Parametry Pojedynczych Kart) — Wersja Balansu: v1.0-alpha.98

**Wersja Balansu:** `v1.0-alpha.98` | **Data:** 2026-08-29 22:47 | **Przeanalizowano Wariantów Kart:** 19 | **Próba:** 10000 gier/setup | **Czas:** 2.99s
**Filtry:** Parametry: `cost,heresy` | Frakcja: `all` | Karta: `kt-01`
**Wynik Bazy Poziomu 3 (Global):** `🟢 94.8 pkt` | 3p: `0.0 pkt` | 4p: `94.8 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (1)

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | Baza (Bieżące parametry wszystkich kart) | 94.8 → 🟢 ** 94.8** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 94.8 → 94.8 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 18 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_KT-01_HERESY_PLUS1` | KT-01 (Rytuał Przejścia): heresy 1 → 2 | 94.8 → 🟢 ** 94.7** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 94.8 → 94.7 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KT-01_HERESY_PLUS2` | KT-01 (Rytuał Przejścia): heresy 1 → 3 | 94.8 → 🟢 ** 94.5** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 94.8 → 94.5 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KT-01_G0_H0` | KT-01 (Rytuał Przejścia): złoto 1→0, herezja 1→0 | 94.8 → 🟢 ** 94.5** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 94.8 → 94.5 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KT-01_G0_H2` | KT-01 (Rytuał Przejścia): złoto 1→0, herezja 1→2 | 94.8 → 🟢 ** 94.4** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 94.8 → 94.4 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KT-01_C0_G2` | KT-01 (Rytuał Przejścia): koszt 1→0, złoto 1→2 | 94.8 → 🟢 ** 94.3** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 94.8 → 94.3 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KT-01_C2_G2` | KT-01 (Rytuał Przejścia): koszt 1→2, złoto 1→2 | 94.8 → 🟢 ** 93.9** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 94.8 → 93.9 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 94.8 → 🟢 ** 93.8** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 94.8 → 93.8 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_C2_H0` | KT-01 (Rytuał Przejścia): koszt 1→2, herezja 1→0 | 94.8 → 🟢 ** 93.8** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 94.8 → 93.8 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_C2_H2` | KT-01 (Rytuał Przejścia): koszt 1→2, herezja 1→2 | 94.8 → 🟢 ** 93.8** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 94.8 → 93.8 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_COST_MINUS1` | KT-01 (Rytuał Przejścia): cost 1 → 0 | 94.8 → 🟢 ** 93.7** (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 94.8 → 93.7 (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_HERESY_MINUS1` | KT-01 (Rytuał Przejścia): heresy 1 → 0 | 94.8 → 🟢 ** 93.7** (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 94.8 → 93.7 (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_C2_G3` | KT-01 (Rytuał Przejścia): koszt 1→2, złoto 1→3 | 94.8 → 🟢 ** 93.4** (`🔻 -1.4`) | 0.0 → 0.0 (`= 0.0`) | 94.8 → 93.4 (`🔻 -1.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_COST_PLUS2` | KT-01 (Rytuał Przejścia): cost 1 → 3 | 94.8 → 🟢 ** 92.9** (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 94.8 → 92.9 (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_C0_G3` | KT-01 (Rytuał Przejścia): koszt 1→0, złoto 1→3 | 94.8 → 🟢 ** 92.3** (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 94.8 → 92.3 (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_G2_H2` | KT-01 (Rytuał Przejścia): złoto 1→2, herezja 1→2 | 94.8 → 🟢 ** 90.8** (`🔻 -4.0`) | 0.0 → 0.0 (`= 0.0`) | 94.8 → 90.8 (`🔻 -4.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_C0_H2` | KT-01 (Rytuał Przejścia): koszt 1→0, herezja 1→2 | 94.8 → 🟢 ** 90.2** (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 94.8 → 90.2 (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_C0_H0` | KT-01 (Rytuał Przejścia): koszt 1→0, herezja 1→0 | 94.8 → 🟡 ** 88.7** (`🔻 -6.1`) | 0.0 → 0.0 (`= 0.0`) | 94.8 → 88.7 (`🔻 -6.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_G2_H0` | KT-01 (Rytuał Przejścia): złoto 1→2, herezja 1→0 | 94.8 → 🟡 ** 88.4** (`🔻 -6.4`) | 0.0 → 0.0 (`= 0.0`) | 94.8 → 88.4 (`🔻 -6.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (1)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | 5.76 Er (8–1) | 0.0% | 4.5% | 1.59 (0–0) | 7.64 (0–0) | 9.13zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 18 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_KT-01_HERESY_PLUS1` | 5.76 Er (8–1) | 0.0% | 4.5% | 1.59 (0–0) | 7.65 (0–0) | 9.13zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_HERESY_PLUS2` | 5.76 Er (8–1) | 0.0% | 4.5% | 1.59 (0–0) | 7.65 (0–0) | 9.12zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_G0_H0` | 5.76 Er (8–1) | 0.0% | 4.5% | 1.59 (0–0) | 7.65 (0–0) | 9.12zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_G0_H2` | 5.76 Er (8–1) | 0.0% | 4.5% | 1.59 (0–0) | 7.64 (0–0) | 9.12zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_C0_G2` | 5.73 Er (8–1) | 0.0% | 4.1% | 1.59 (0–0) | 7.58 (0–0) | 9.30zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_C2_G2` | 5.76 Er (8–1) | 0.0% | 4.5% | 1.59 (0–0) | 7.65 (0–0) | 9.14zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_PLUS1` | 5.77 Er (8–1) | 0.0% | 4.5% | 1.59 (0–0) | 7.65 (0–0) | 9.13zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_C2_H0` | 5.77 Er (8–1) | 0.0% | 4.5% | 1.59 (0–0) | 7.65 (0–0) | 9.13zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_C2_H2` | 5.77 Er (8–1) | 0.0% | 4.5% | 1.59 (0–0) | 7.65 (0–0) | 9.13zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_MINUS1` | 5.76 Er (8–1) | 0.0% | 4.2% | 1.59 (0–0) | 7.63 (0–0) | 9.20zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_HERESY_MINUS1` | 5.76 Er (8–1) | 0.0% | 4.4% | 1.59 (0–0) | 7.62 (0–0) | 9.14zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_C2_G3` | 5.76 Er (8–1) | 0.0% | 4.4% | 1.60 (0–0) | 7.65 (0–0) | 9.20zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_PLUS2` | 5.76 Er (8–1) | 0.0% | 4.5% | 1.59 (0–0) | 7.64 (0–0) | 9.12zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_C0_G3` | 5.71 Er (8–1) | 0.0% | 4.1% | 1.58 (0–0) | 7.53 (0–0) | 9.46zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_G2_H2` | 5.76 Er (8–1) | 0.0% | 4.4% | 1.59 (0–0) | 7.69 (0–0) | 9.17zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_C0_H2` | 5.76 Er (8–1) | 0.0% | 4.1% | 1.60 (0–0) | 7.69 (0–0) | 9.17zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_C0_H0` | 5.76 Er (8–1) | 0.0% | 4.2% | 1.59 (0–0) | 7.51 (0–0) | 9.32zł (0.0–0.0) | 8.12 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_G2_H0` | 5.76 Er (8–1) | 0.0% | 4.3% | 1.59 (0–0) | 7.50 (0–0) | 9.32zł (0.0–0.0) | 8.11 (0.0–0.0) | 🟢 W NORMIE |

</details>