# Raport Precyzyjnego Audytu Poziomu 3 (Parametry Pojedynczych Kart) — Wersja Balansu: v1.0-alpha.97

**Wersja Balansu:** `v1.0-alpha.97` | **Data:** 2026-08-29 22:44 | **Przeanalizowano Wariantów Kart:** 19 | **Próba:** 10000 gier/setup | **Czas:** 2.69s
**Filtry:** Parametry: `cost,heresy` | Frakcja: `all` | Karta: `so-11`
**Wynik Bazy Poziomu 3 (Global):** `🟢 94.6 pkt` | 3p: `0.0 pkt` | 4p: `94.6 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (3)

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | Baza (Bieżące parametry wszystkich kart) | 94.6 → 🟢 ** 94.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 94.6 → 94.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-11_COST_MINUS1` | SO-11 (Dekret Czystości Wiary): cost 1 → 0 | 94.6 → 🟢 ** 94.8** (`⬆️ +0.2`) | 0.0 → 0.0 (`= 0.0`) | 94.6 → 94.8 (`⬆️ +0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-11_C2_G2` | SO-11 (Dekret Czystości Wiary): koszt 1→2, złoto 1→2 | 94.6 → 🟢 ** 94.7** (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | 94.6 → 94.7 (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 16 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_SO-11_C2_G3` | SO-11 (Dekret Czystości Wiary): koszt 1→2, złoto 1→3 | 94.6 → 🟢 ** 94.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 94.6 → 94.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-11_COST_PLUS1` | SO-11 (Dekret Czystości Wiary): cost 1 → 2 | 94.6 → 🟢 ** 94.3** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 94.6 → 94.3 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-11_C2_H2` | SO-11 (Dekret Czystości Wiary): koszt 1→2, herezja 1→2 | 94.6 → 🟢 ** 93.9** (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 94.6 → 93.9 (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-11_HERESY_PLUS1` | SO-11 (Dekret Czystości Wiary): heresy 1 → 2 | 94.6 → 🟢 ** 93.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 94.6 → 93.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-11_HERESY_PLUS2` | SO-11 (Dekret Czystości Wiary): heresy 1 → 3 | 94.6 → 🟢 ** 93.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 94.6 → 93.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-11_G0_H2` | SO-11 (Dekret Czystości Wiary): złoto 1→0, herezja 1→2 | 94.6 → 🟢 ** 93.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 94.6 → 93.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-11_C0_H2` | SO-11 (Dekret Czystości Wiary): koszt 1→0, herezja 1→2 | 94.6 → 🟢 ** 93.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 94.6 → 93.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-11_COST_PLUS2` | SO-11 (Dekret Czystości Wiary): cost 1 → 3 | 94.6 → 🟢 ** 93.5** (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 94.6 → 93.5 (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-11_G2_H2` | SO-11 (Dekret Czystości Wiary): złoto 1→2, herezja 1→2 | 94.6 → 🟢 ** 93.3** (`🔻 -1.3`) | 0.0 → 0.0 (`= 0.0`) | 94.6 → 93.3 (`🔻 -1.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-11_C0_G2` | SO-11 (Dekret Czystości Wiary): koszt 1→0, złoto 1→2 | 94.6 → 🟢 ** 93.2** (`🔻 -1.4`) | 0.0 → 0.0 (`= 0.0`) | 94.6 → 93.2 (`🔻 -1.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-11_C0_G3` | SO-11 (Dekret Czystości Wiary): koszt 1→0, złoto 1→3 | 94.6 → 🟢 ** 93.0** (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 94.6 → 93.0 (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-11_HERESY_MINUS1` | SO-11 (Dekret Czystości Wiary): heresy 1 → 0 | 94.6 → 🟢 ** 92.4** (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 94.6 → 92.4 (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-11_C2_H0` | SO-11 (Dekret Czystości Wiary): koszt 1→2, herezja 1→0 | 94.6 → 🟢 ** 92.4** (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 94.6 → 92.4 (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-11_G0_H0` | SO-11 (Dekret Czystości Wiary): złoto 1→0, herezja 1→0 | 94.6 → 🟢 ** 92.4** (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 94.6 → 92.4 (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-11_G2_H0` | SO-11 (Dekret Czystości Wiary): złoto 1→2, herezja 1→0 | 94.6 → 🟢 ** 91.4** (`🔻 -3.2`) | 0.0 → 0.0 (`= 0.0`) | 94.6 → 91.4 (`🔻 -3.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-11_C0_H0` | SO-11 (Dekret Czystości Wiary): koszt 1→0, herezja 1→0 | 94.6 → 🟢 ** 91.3** (`🔻 -3.3`) | 0.0 → 0.0 (`= 0.0`) | 94.6 → 91.3 (`🔻 -3.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (3)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.61 (0–0) | 8.98zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_COST_MINUS1` | 5.76 Er (8–1) | 0.0% | 4.5% | 1.59 (0–0) | 7.64 (0–0) | 9.13zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_C2_G2` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.59 (0–0) | 8.98zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 16 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_SO-11_C2_G3` | 5.77 Er (8–1) | 0.0% | 4.8% | 1.60 (0–0) | 7.61 (0–0) | 9.13zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_COST_PLUS1` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.51 (0–0) | 7.58 (0–0) | 8.91zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_C2_H2` | 5.77 Er (8–1) | 0.0% | 4.7% | 1.53 (0–0) | 7.54 (0–0) | 9.32zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_HERESY_PLUS1` | 5.77 Er (8–1) | 0.0% | 4.7% | 1.53 (0–0) | 7.54 (0–0) | 9.31zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_HERESY_PLUS2` | 5.77 Er (8–1) | 0.0% | 4.7% | 1.53 (0–0) | 7.54 (0–0) | 9.31zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_G0_H2` | 5.77 Er (8–1) | 0.0% | 4.7% | 1.53 (0–0) | 7.54 (0–0) | 9.31zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_C0_H2` | 5.77 Er (8–1) | 0.0% | 3.8% | 1.53 (0–0) | 7.55 (0–0) | 9.32zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_COST_PLUS2` | 5.77 Er (8–1) | 0.0% | 4.7% | 1.52 (0–0) | 7.53 (0–0) | 9.25zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_G2_H2` | 5.77 Er (8–1) | 0.0% | 4.7% | 1.53 (0–0) | 7.54 (0–0) | 9.32zł (0.0–0.0) | 8.12 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_C0_G2` | 5.77 Er (8–1) | 0.0% | 4.2% | 1.59 (0–0) | 7.57 (0–0) | 9.37zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_C0_G3` | 5.76 Er (8–1) | 0.0% | 4.1% | 1.60 (0–0) | 7.57 (0–0) | 9.54zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_HERESY_MINUS1` | 5.79 Er (8–1) | 0.0% | 4.8% | 1.58 (0–0) | 7.50 (0–0) | 9.00zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_C2_H0` | 5.80 Er (8–1) | 0.0% | 5.1% | 1.54 (0–0) | 7.51 (0–0) | 8.92zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_G0_H0` | 5.80 Er (8–1) | 0.0% | 5.1% | 1.54 (0–0) | 7.51 (0–0) | 8.90zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_G2_H0` | 5.80 Er (8–1) | 0.0% | 4.6% | 1.61 (0–0) | 7.51 (0–0) | 9.15zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_C0_H0` | 5.80 Er (8–1) | 0.0% | 4.5% | 1.61 (0–0) | 7.53 (0–0) | 9.15zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |

</details>