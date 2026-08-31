# Raport Audytu Poziomu 2 (Warunki Zwycięstwa i Skalowanie) — Wersja Balansu: v1.0-alpha.170

**Wersja Balansu:** `v1.0-alpha.170` | **Data:** 2026-08-30 23:01 | **Przeanalizowano Wariantów:** 84 | **Próba:** 10000 gier/setup | **Czas:** 36.08s
**Wynik Bazy Poziomu 2 (Global):** `🟡 84.5 pkt` | 3p: `70.8 pkt` | 4p: `90.3 pkt` | 5p: `92.4 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (1)

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | Baza (Bieżące warunki zwycięstwa) | 84.5 → 🟡 ** 84.5** (`= 0.0`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 83 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Warunek Zwycięstwa Poziomu 2 | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L2_SO_STACKS_3P_MINUS1` | Oficjum Stosy (3p): 6 → 5 | 84.5 → 🟡 ** 84.5** (`= 0.0`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | ⚪ OPTYMALNY |
| `L2_SO_STACKS_5P_PLUS1` | Oficjum Stosy (5p): 8 → 9 | 84.5 → 🟡 ** 84.5** (`= 0.0`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | ⚪ OPTYMALNY |
| `L2_GC_FALLS_3P_MINUS1` | Gildia Upadki (3p): 8 → 7 | 84.5 → 🟡 ** 84.5** (`= 0.0`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | ⚪ OPTYMALNY |
| `L2_KB_HOOKS_5P_MINUS1` | Korona Haki (5p): 2 → 1 | 84.5 → 🟡 ** 82.1** (`🔻 -2.4`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 85.1 (`🔻 -7.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_3P_MINUS2` | Oficjum Stosy (3p): 6 → 4 | 84.5 → 🟡 ** 80.1** (`🔻 -4.4`) | 70.8 → 57.7 (`🔻 -13.1`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_3P_MINUS1` | Korona Haki (3p): 2 → 1 | 84.5 → 🟠 ** 79.6** (`🔻 -4.9`) | 70.8 → 56.2 (`🔻 -14.6`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_4P_MINUS1` | Oficjum Stosy (4p): 7 → 6 | 84.5 → 🟠 ** 79.3** (`🔻 -5.2`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 74.8 (`🔻 -15.5`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_3P_MINUS1` | Oficjum Skazania (3p): 2 → 1 | 84.5 → 🟠 ** 78.8** (`🔻 -5.7`) | 70.8 → 53.8 (`🔻 -17.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_4P_MINUS1` | Korona Haki (4p): 2 → 1 | 84.5 → 🟠 ** 78.8** (`🔻 -5.7`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 73.1 (`🔻 -17.2`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_3P_MINUS2` | Gildia Upadki (3p): 8 → 6 | 84.5 → 🟠 ** 78.7** (`🔻 -5.8`) | 70.8 → 53.5 (`🔻 -17.3`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_4P_PLUS1` | Gildia Upadki (4p): 9 → 10 | 84.5 → 🟠 ** 78.6** (`🔻 -5.9`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 72.6 (`🔻 -17.7`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_4P_PLUS1` | Oficjum Stosy (4p): 7 → 8 | 84.5 → 🟠 ** 78.5** (`🔻 -6.0`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 72.4 (`🔻 -17.9`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_3P_MINUS1` | Kabała Fragmenty (3p): 3 → 2 | 84.5 → 🟠 ** 78.4** (`🔻 -6.1`) | 70.8 → 52.4 (`🔻 -18.4`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_3P_PLUS1` | Gildia Upadki (3p): 8 → 9 | 84.5 → 🟠 ** 77.1** (`🔻 -7.4`) | 70.8 → 48.5 (`🔻 -22.3`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_3P_MINUS2` | Kabała Fragmenty (3p): 3 → 1 | 84.5 → 🟠 ** 77.0** (`🔻 -7.5`) | 70.8 → 48.2 (`🔻 -22.6`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_5P_MINUS1` | Kabała Fragmenty (5p): 3 → 2 | 84.5 → 🟠 ** 77.0** (`🔻 -7.5`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 69.9 (`🔻 -22.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_5P_MINUS1` | Gildia Upadki (5p): 9 → 8 | 84.5 → 🟠 ** 76.3** (`🔻 -8.2`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 67.8 (`🔻 -24.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_4P_MINUS1` | Kabała Fragmenty (4p): 3 → 2 | 84.5 → 🟠 ** 75.6** (`🔻 -8.9`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 63.6 (`🔻 -26.7`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_4P_MINUS1` | Gildia Upadki (4p): 9 → 8 | 84.5 → 🟠 ** 75.5** (`🔻 -9.0`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 63.2 (`🔻 -27.1`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_5P_PLUS1` | Gildia Upadki (5p): 9 → 10 | 84.5 → 🟠 ** 74.9** (`🔻 -9.6`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 63.6 (`🔻 -28.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_3P_PLUS1` | Oficjum Stosy (3p): 6 → 7 | 84.5 → 🟠 ** 74.5** (`🔻 -10.0`) | 70.8 → 40.7 (`🔻 -30.1`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_3P_MINUS3` | Oficjum Stosy (3p): 6 → 3 | 84.5 → 🟠 ** 73.8** (`🔻 -10.7`) | 70.8 → 38.8 (`🔻 -32.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_3P_MINUS3` | Gildia Upadki (3p): 8 → 5 | 84.5 → 🟠 ** 73.7** (`🔻 -10.8`) | 70.8 → 38.5 (`🔻 -32.3`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_3P_PLUS2` | Gildia Upadki (3p): 8 → 10 | 84.5 → 🟠 ** 73.5** (`🔻 -11.0`) | 70.8 → 37.9 (`🔻 -32.9`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_3P_PLUS2` | Oficjum Stosy (3p): 6 → 8 | 84.5 → 🟠 ** 73.1** (`🔻 -11.4`) | 70.8 → 36.7 (`🔻 -34.1`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_3P_PLUS1` | Cienie Relikwie (3p): 2 → 3 | 84.5 → 🟠 ** 73.0** (`🔻 -11.5`) | 70.8 → 36.4 (`🔻 -34.4`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_3P_PLUS3` | Oficjum Stosy (3p): 6 → 9 | 84.5 → 🟠 ** 72.7** (`🔻 -11.8`) | 70.8 → 35.3 (`🔻 -35.5`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_3P_PLUS1` | Kabała Fragmenty (3p): 3 → 4 | 84.5 → 🟠 ** 72.6** (`🔻 -11.9`) | 70.8 → 35.0 (`🔻 -35.8`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_3P_PLUS2` | Kabała Fragmenty (3p): 3 → 5 | 84.5 → 🟠 ** 72.6** (`🔻 -11.9`) | 70.8 → 35.1 (`🔻 -35.7`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_3P_PLUS1` | Korona Dekrety (3p): 2 → 3 | 84.5 → 🟠 ** 72.5** (`🔻 -12.0`) | 70.8 → 34.7 (`🔻 -36.1`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_4P_PLUS2` | Gildia Upadki (4p): 9 → 11 | 84.5 → 🟠 ** 72.3** (`🔻 -12.2`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 53.6 (`🔻 -36.7`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_3P_PLUS3` | Gildia Upadki (3p): 8 → 11 | 84.5 → 🟠 ** 72.1** (`🔻 -12.4`) | 70.8 → 33.7 (`🔻 -37.1`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_4P_MINUS2` | Kabała Fragmenty (4p): 3 → 1 | 84.5 → 🟠 ** 72.1** (`🔻 -12.4`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 53.0 (`🔻 -37.3`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_5P_MINUS2` | Kabała Fragmenty (5p): 3 → 1 | 84.5 → 🟠 ** 71.4** (`🔻 -13.1`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 53.0 (`🔻 -39.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_3P_PLUS1` | Korona Haki (3p): 2 → 3 | 84.5 → 🟠 ** 71.2** (`🔻 -13.3`) | 70.8 → 31.0 (`🔻 -39.8`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_3P_MINUS1` | Cienie Relikwie (3p): 2 → 1 | 84.5 → 🟠 ** 70.7** (`🔻 -13.8`) | 70.8 → 29.3 (`🔻 -41.5`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_4P_PLUS2` | Oficjum Stosy (4p): 7 → 9 | 84.5 → 🟠 ** 70.3** (`🔻 -14.2`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 47.6 (`🔻 -42.7`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_3P_MINUS1` | Korona Dekrety (3p): 2 → 1 | 84.5 → 🟠 ** 70.0** (`🔻 -14.5`) | 70.8 → 27.2 (`🔻 -43.6`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_5P_PLUS2` | Gildia Upadki (5p): 9 → 11 | 84.5 → 🟠 ** 69.0** (`🔻 -15.5`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 45.8 (`🔻 -46.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_5P_PLUS1` | Oficjum Skazania (5p): 3 → 4 | 84.5 → 🟠 ** 68.9** (`🔻 -15.6`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 45.5 (`🔻 -46.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_4P_PLUS3` | Gildia Upadki (4p): 9 → 12 | 84.5 → 🟠 ** 68.6** (`🔻 -15.9`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 42.7 (`🔻 -47.6`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_PLUS1` | Oficjum Stosy (global): 6/7/8 → 7/8/9 | 84.5 → 🟠 ** 68.5** (`🔻 -16.0`) | 70.8 → 40.7 (`🔻 -30.1`) | 90.3 → 72.4 (`🔻 -17.9`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_4P_MINUS2` | Oficjum Stosy (4p): 7 → 5 | 84.5 → 🟠 ** 67.6** (`🔻 -16.9`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 39.5 (`🔻 -50.8`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_4P_MINUS2` | Gildia Upadki (4p): 9 → 7 | 84.5 → 🟠 ** 67.3** (`🔻 -17.2`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 38.8 (`🔻 -51.5`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_MINUS1` | Gildia Upadki (global): 8/9/9 → 7/8/8 | 84.5 → 🟠 ** 67.3** (`🔻 -17.2`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 63.2 (`🔻 -27.1`) | 92.4 → 67.8 (`🔻 -24.6`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_4P_PLUS1` | Cienie Relikwie (4p): 2 → 3 | 84.5 → 🟠 ** 66.3** (`🔻 -18.2`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 35.6 (`🔻 -54.7`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_4P_PLUS1` | Korona Dekrety (4p): 2 → 3 | 84.5 → 🟠 ** 66.2** (`🔻 -18.3`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 35.5 (`🔻 -54.8`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_5P_MINUS1` | Oficjum Stosy (5p): 8 → 7 | 84.5 → 🟠 ** 65.7** (`🔻 -18.8`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 36.0 (`🔻 -56.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_5P_PLUS3` | Gildia Upadki (5p): 9 → 12 | 84.5 → 🟠 ** 65.7** (`🔻 -18.8`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 35.9 (`🔻 -56.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_4P_PLUS1` | Kabała Fragmenty (4p): 3 → 4 | 84.5 → 🟠 ** 65.3** (`🔻 -19.2`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 32.7 (`🔻 -57.6`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_4P_PLUS2` | Kabała Fragmenty (4p): 3 → 5 | 84.5 → 🟠 ** 65.3** (`🔻 -19.2`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 32.8 (`🔻 -57.5`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_4P_PLUS1` | Korona Haki (4p): 2 → 3 | 84.5 → 🟠 ** 65.1** (`🔻 -19.4`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 32.2 (`🔻 -58.1`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_4P_PLUS3` | Oficjum Stosy (4p): 7 → 10 | 84.5 → 🟠 ** 65.0** (`🔻 -19.5`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 31.9 (`🔻 -58.4`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_5P_PLUS1` | Cienie Relikwie (5p): 2 → 3 | 84.5 → 🔴 ** 63.9** (`🔻 -20.6`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 30.6 (`🔻 -61.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_5P_PLUS1` | Korona Dekrety (5p): 2 → 3 | 84.5 → 🔴 ** 63.3** (`🔻 -21.2`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 28.7 (`🔻 -63.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_5P_PLUS2` | Oficjum Stosy (5p): 8 → 10 | 84.5 → 🔴 ** 62.8** (`🔻 -21.7`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 27.3 (`🔻 -65.1`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_5P_PLUS3` | Oficjum Stosy (5p): 8 → 11 | 84.5 → 🔴 ** 62.5** (`🔻 -22.0`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 26.5 (`🔻 -65.9`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_5P_PLUS1` | Kabała Fragmenty (5p): 3 → 4 | 84.5 → 🔴 ** 62.4** (`🔻 -22.1`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 26.0 (`🔻 -66.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_5P_PLUS2` | Kabała Fragmenty (5p): 3 → 5 | 84.5 → 🔴 ** 62.4** (`🔻 -22.1`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 26.0 (`🔻 -66.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_HOOKS_5P_PLUS1` | Korona Haki (5p): 2 → 3 | 84.5 → 🔴 ** 62.3** (`🔻 -22.2`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 25.9 (`🔻 -66.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_4P_MINUS3` | Gildia Upadki (4p): 9 → 6 | 84.5 → 🔴 ** 62.0** (`🔻 -22.5`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 22.8 (`🔻 -67.5`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_MINUS1` | Kabała Fragmenty (global): 3 → 2 | 84.5 → 🔴 ** 62.0** (`🔻 -22.5`) | 70.8 → 52.4 (`🔻 -18.4`) | 90.3 → 63.6 (`🔻 -26.7`) | 92.4 → 69.9 (`🔻 -22.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_PLUS1` | Gildia Upadki (global): 8/9/9 → 9/10/10 | 84.5 → 🔴 ** 61.6** (`🔻 -22.9`) | 70.8 → 48.5 (`🔻 -22.3`) | 90.3 → 72.6 (`🔻 -17.7`) | 92.4 → 63.6 (`🔻 -28.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_4P_MINUS1` | Oficjum Skazania (4p): 3 → 2 | 84.5 → 🔴 ** 61.4** (`🔻 -23.1`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 21.0 (`🔻 -69.3`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_4P_MINUS3` | Oficjum Stosy (4p): 7 → 4 | 84.5 → 🔴 ** 61.0** (`🔻 -23.5`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 19.8 (`🔻 -70.5`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_5P_MINUS2` | Gildia Upadki (5p): 9 → 7 | 84.5 → 🔴 ** 61.0** (`🔻 -23.5`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 21.9 (`🔻 -70.5`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_4P_MINUS1` | Korona Dekrety (4p): 2 → 1 | 84.5 → 🔴 ** 60.9** (`🔻 -23.6`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 19.5 (`🔻 -70.8`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_4P_MINUS2` | Oficjum Skazania (4p): 3 → 1 | 84.5 → 🔴 ** 60.5** (`🔻 -24.0`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 18.4 (`🔻 -71.9`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_MINUS1` | Oficjum Stosy (global): 6/7/8 → 5/6/7 | 84.5 → 🔴 ** 60.5** (`🔻 -24.0`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 74.8 (`🔻 -15.5`) | 92.4 → 36.0 (`🔻 -56.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_4P_MINUS1` | Cienie Relikwie (4p): 2 → 1 | 84.5 → 🔴 ** 60.0** (`🔻 -24.5`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 16.8 (`🔻 -73.5`) | 92.4 → 92.4 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_5P_MINUS2` | Oficjum Stosy (5p): 8 → 6 | 84.5 → 🔴 ** 54.9** (`🔻 -29.6`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 3.6 (`🔻 -88.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_GC_FALLS_5P_MINUS3` | Gildia Upadki (5p): 9 → 6 | 84.5 → 🔴 ** 54.4** (`🔻 -30.1`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 2.0 (`🔻 -90.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_STACKS_5P_MINUS3` | Oficjum Stosy (5p): 8 → 5 | 84.5 → 🔴 ** 53.7** (`🔻 -30.8`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 0.1 (`🔻 -92.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_5P_MINUS1` | Oficjum Skazania (5p): 3 → 2 | 84.5 → 🔴 ** 53.7** (`🔻 -30.8`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 0.1 (`🔻 -92.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_5P_MINUS2` | Oficjum Skazania (5p): 3 → 1 | 84.5 → 🔴 ** 53.7** (`🔻 -30.8`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 0.1 (`🔻 -92.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_5P_MINUS1` | Cienie Relikwie (5p): 2 → 1 | 84.5 → 🔴 ** 53.7** (`🔻 -30.8`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 0.1 (`🔻 -92.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_5P_MINUS1` | Korona Dekrety (5p): 2 → 1 | 84.5 → 🔴 ** 53.7** (`🔻 -30.8`) | 70.8 → 70.8 (`= 0.0`) | 90.3 → 90.3 (`= 0.0`) | 92.4 → 0.1 (`🔻 -92.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_PLUS1` | Cienie Relikwie (global): 2 → 3 | 84.5 → 🔴 ** 34.2** (`🔻 -50.3`) | 70.8 → 36.4 (`🔻 -34.4`) | 90.3 → 35.6 (`🔻 -54.7`) | 92.4 → 30.6 (`🔻 -61.8`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_PLUS1` | Korona Dekrety (global): 2 → 3 | 84.5 → 🔴 ** 33.0** (`🔻 -51.5`) | 70.8 → 34.7 (`🔻 -36.1`) | 90.3 → 35.5 (`🔻 -54.8`) | 92.4 → 28.7 (`🔻 -63.7`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KT_FRAGS_PLUS1` | Kabała Fragmenty (global): 3 → 4 | 84.5 → 🔴 ** 31.2** (`🔻 -53.3`) | 70.8 → 35.0 (`🔻 -35.8`) | 90.3 → 32.7 (`🔻 -57.6`) | 92.4 → 26.0 (`🔻 -66.4`) | 🔴 POGARSZA GLOBALNIE |
| `L2_SO_CONDEMNS_MINUS1` | Oficjum Skazania (global): 2/3/3 → 1/2/2 | 84.5 → 🔴 ** 25.0** (`🔻 -59.5`) | 70.8 → 53.8 (`🔻 -17.0`) | 90.3 → 21.0 (`🔻 -69.3`) | 92.4 → 0.1 (`🔻 -92.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_KB_DECREES_MINUS1` | Korona Dekrety (global): 2 → 1 | 84.5 → 🔴 ** 15.6** (`🔻 -68.9`) | 70.8 → 27.2 (`🔻 -43.6`) | 90.3 → 19.5 (`🔻 -70.8`) | 92.4 → 0.1 (`🔻 -92.3`) | 🔴 POGARSZA GLOBALNIE |
| `L2_CAA_RELICS_MINUS1` | Cienie Relikwie (global): 2 → 1 | 84.5 → 🔴 ** 15.4** (`🔻 -69.1`) | 70.8 → 29.3 (`🔻 -41.5`) | 90.3 → 16.8 (`🔻 -73.5`) | 92.4 → 0.1 (`🔻 -92.3`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (1)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_BAZA` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.28 (0–0) | 7.06zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 83 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L2_SO_STACKS_3P_MINUS1` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.28 (0–0) | 7.06zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_5P_PLUS1` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.28 (0–0) | 7.06zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_3P_MINUS1` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.28 (0–0) | 7.06zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_5P_MINUS1` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.27 (0–0) | 7.05zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_3P_MINUS2` | 6.12 Er (8–1) | 0.1% | 2.5% | 1.61 (0–0) | 6.99 (0–0) | 6.90zł (0.0–0.0) | 7.10 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_3P_MINUS1` | 6.19 Er (8–1) | 0.0% | 2.5% | 1.62 (0–0) | 7.04 (0–0) | 6.95zł (0.0–0.0) | 7.11 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_4P_MINUS1` | 6.24 Er (8–1) | 0.1% | 2.5% | 1.63 (0–0) | 7.18 (0–0) | 7.01zł (0.0–0.0) | 7.12 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_3P_MINUS1` | 6.05 Er (8–1) | 0.1% | 2.5% | 1.60 (0–0) | 6.90 (0–0) | 6.87zł (0.0–0.0) | 7.12 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_4P_MINUS1` | 6.26 Er (8–1) | 0.1% | 2.5% | 1.63 (0–0) | 7.21 (0–0) | 7.02zł (0.0–0.0) | 7.12 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_3P_MINUS2` | 6.15 Er (8–1) | 0.1% | 2.5% | 1.61 (0–0) | 7.04 (0–0) | 6.92zł (0.0–0.0) | 7.12 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_4P_PLUS1` | 6.31 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 7.35 (0–0) | 7.09zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_4P_PLUS1` | 6.29 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 7.32 (0–0) | 7.08zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_3P_MINUS1` | 6.40 Er (8–1) | 0.1% | 2.6% | 1.68 (0–0) | 7.49 (0–0) | 7.16zł (0.0–0.0) | 7.18 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_3P_PLUS1` | 6.44 Er (8–1) | 0.1% | 2.5% | 1.68 (0–0) | 7.60 (0–0) | 7.24zł (0.0–0.0) | 7.16 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_3P_MINUS2` | 6.45 Er (8–1) | 0.1% | 2.7% | 1.69 (0–0) | 7.56 (0–0) | 7.20zł (0.0–0.0) | 7.19 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_5P_MINUS1` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 7.29 (0–0) | 7.06zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_5P_MINUS1` | 6.27 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.26 (0–0) | 7.05zł (0.0–0.0) | 7.13 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_4P_MINUS1` | 6.32 Er (8–1) | 0.1% | 2.6% | 1.66 (0–0) | 7.38 (0–0) | 7.10zł (0.0–0.0) | 7.16 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_4P_MINUS1` | 6.24 Er (8–1) | 0.1% | 2.5% | 1.63 (0–0) | 7.17 (0–0) | 7.01zł (0.0–0.0) | 7.12 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_5P_PLUS1` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.29 (0–0) | 7.06zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_3P_PLUS1` | 6.45 Er (8–1) | 0.1% | 2.5% | 1.68 (0–0) | 7.61 (0–0) | 7.25zł (0.0–0.0) | 7.16 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_3P_MINUS3` | 5.89 Er (8–1) | 0.1% | 2.5% | 1.55 (0–0) | 6.56 (0–0) | 6.69zł (0.0–0.0) | 7.02 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_3P_MINUS3` | 5.98 Er (8–1) | 0.1% | 2.5% | 1.58 (0–0) | 6.73 (0–0) | 6.75zł (0.0–0.0) | 7.08 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_3P_PLUS2` | 6.49 Er (8–1) | 0.2% | 2.5% | 1.69 (0–0) | 7.70 (0–0) | 7.30zł (0.0–0.0) | 7.16 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_3P_PLUS2` | 6.50 Er (8–1) | 0.2% | 2.5% | 1.68 (0–0) | 7.71 (0–0) | 7.30zł (0.0–0.0) | 7.16 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_3P_PLUS1` | 6.52 Er (8–1) | 0.2% | 2.5% | 1.71 (0–0) | 7.82 (0–0) | 7.34zł (0.0–0.0) | 7.22 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_3P_PLUS3` | 6.54 Er (8–1) | 0.5% | 2.5% | 1.69 (0–0) | 7.77 (0–0) | 7.34zł (0.0–0.0) | 7.16 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_3P_PLUS1` | 6.54 Er (8–1) | 0.2% | 2.4% | 1.71 (0–0) | 7.84 (0–0) | 7.34zł (0.0–0.0) | 7.28 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_3P_PLUS2` | 6.53 Er (8–1) | 0.2% | 2.4% | 1.70 (0–0) | 7.84 (0–0) | 7.36zł (0.0–0.0) | 7.29 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_3P_PLUS1` | 6.52 Er (8–1) | 0.6% | 2.5% | 1.71 (0–0) | 7.84 (0–0) | 7.26zł (0.0–0.0) | 7.20 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_4P_PLUS2` | 6.32 Er (8–1) | 0.1% | 2.5% | 1.66 (0–0) | 7.40 (0–0) | 7.12zł (0.0–0.0) | 7.16 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_3P_PLUS3` | 6.53 Er (8–1) | 0.3% | 2.5% | 1.69 (0–0) | 7.78 (0–0) | 7.35zł (0.0–0.0) | 7.16 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_4P_MINUS2` | 6.34 Er (8–1) | 0.1% | 2.6% | 1.66 (0–0) | 7.43 (0–0) | 7.13zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_5P_MINUS2` | 6.29 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 7.30 (0–0) | 7.07zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_3P_PLUS1` | 6.57 Er (8–1) | 1.7% | 2.5% | 1.72 (0–0) | 7.99 (0–0) | 7.32zł (0.0–0.0) | 7.21 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_3P_MINUS1` | 5.24 Er (8–1) | 0.0% | 2.4% | 1.33 (0–0) | 5.69 (0–0) | 6.10zł (0.0–0.0) | 6.34 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_4P_PLUS2` | 6.30 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 7.34 (0–0) | 7.09zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_3P_MINUS1` | 5.63 Er (8–1) | 0.0% | 2.2% | 1.47 (0–0) | 6.12 (0–0) | 6.61zł (0.0–0.0) | 6.79 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_5P_PLUS2` | 6.29 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 7.30 (0–0) | 7.07zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_5P_PLUS1` | 6.29 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.30 (0–0) | 7.07zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_4P_PLUS3` | 6.34 Er (8–1) | 0.1% | 2.5% | 1.66 (0–0) | 7.43 (0–0) | 7.13zł (0.0–0.0) | 7.16 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_PLUS1` | 6.47 Er (8–1) | 0.1% | 2.5% | 1.68 (0–0) | 7.66 (0–0) | 7.28zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_4P_MINUS2` | 6.16 Er (8–1) | 0.1% | 2.5% | 1.61 (0–0) | 7.00 (0–0) | 6.92zł (0.0–0.0) | 7.07 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_4P_MINUS2` | 6.18 Er (8–1) | 0.1% | 2.5% | 1.61 (0–0) | 7.03 (0–0) | 6.94zł (0.0–0.0) | 7.09 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_MINUS1` | 6.23 Er (8–1) | 0.1% | 2.5% | 1.63 (0–0) | 7.15 (0–0) | 7.00zł (0.0–0.0) | 7.12 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_4P_PLUS1` | 6.37 Er (8–1) | 0.1% | 2.5% | 1.67 (0–0) | 7.55 (0–0) | 7.18zł (0.0–0.0) | 7.20 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_4P_PLUS1` | 6.36 Er (8–1) | 0.1% | 2.5% | 1.67 (0–0) | 7.54 (0–0) | 7.17zł (0.0–0.0) | 7.20 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_5P_MINUS1` | 6.27 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.25 (0–0) | 7.04zł (0.0–0.0) | 7.13 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_5P_PLUS3` | 6.29 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 7.30 (0–0) | 7.07zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_4P_PLUS1` | 6.37 Er (8–1) | 0.1% | 2.5% | 1.67 (0–0) | 7.56 (0–0) | 7.22zł (0.0–0.0) | 7.24 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_4P_PLUS2` | 6.37 Er (8–1) | 0.1% | 2.5% | 1.67 (0–0) | 7.56 (0–0) | 7.24zł (0.0–0.0) | 7.25 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_4P_PLUS1` | 6.37 Er (8–1) | 0.1% | 2.5% | 1.67 (0–0) | 7.56 (0–0) | 7.17zł (0.0–0.0) | 7.20 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_4P_PLUS3` | 6.30 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 7.34 (0–0) | 7.10zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_5P_PLUS1` | 6.29 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 7.33 (0–0) | 7.08zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_5P_PLUS1` | 6.29 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 7.32 (0–0) | 7.08zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_5P_PLUS2` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.28 (0–0) | 7.06zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_5P_PLUS3` | 6.28 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.28 (0–0) | 7.06zł (0.0–0.0) | 7.14 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_5P_PLUS1` | 6.29 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 7.33 (0–0) | 7.09zł (0.0–0.0) | 7.16 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_5P_PLUS2` | 6.29 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 7.33 (0–0) | 7.10zł (0.0–0.0) | 7.16 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_HOOKS_5P_PLUS1` | 6.29 Er (8–1) | 0.1% | 2.5% | 1.65 (0–0) | 7.32 (0–0) | 7.08zł (0.0–0.0) | 7.15 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_4P_MINUS3` | 6.09 Er (8–1) | 0.1% | 2.4% | 1.59 (0–0) | 6.83 (0–0) | 6.84zł (0.0–0.0) | 7.05 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_MINUS1` | 6.45 Er (8–1) | 0.1% | 2.7% | 1.70 (0–0) | 7.61 (0–0) | 7.22zł (0.0–0.0) | 7.20 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_PLUS1` | 6.47 Er (8–1) | 0.1% | 2.5% | 1.69 (0–0) | 7.68 (0–0) | 7.28zł (0.0–0.0) | 7.17 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_4P_MINUS1` | 6.08 Er (8–1) | 0.1% | 2.4% | 1.59 (0–0) | 6.83 (0–0) | 6.86zł (0.0–0.0) | 7.05 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_4P_MINUS3` | 6.04 Er (8–1) | 0.1% | 2.4% | 1.58 (0–0) | 6.71 (0–0) | 6.78zł (0.0–0.0) | 6.98 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_5P_MINUS2` | 6.26 Er (8–1) | 0.1% | 2.5% | 1.64 (0–0) | 7.23 (0–0) | 7.03zł (0.0–0.0) | 7.13 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_4P_MINUS1` | 5.86 Er (8–1) | 0.1% | 2.3% | 1.51 (0–0) | 6.35 (0–0) | 6.66zł (0.0–0.0) | 6.78 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_4P_MINUS2` | 5.55 Er (8–1) | 0.1% | 2.3% | 1.36 (0–0) | 5.88 (0–0) | 6.50zł (0.0–0.0) | 6.56 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_MINUS1` | 6.23 Er (8–1) | 0.1% | 2.5% | 1.63 (0–0) | 7.15 (0–0) | 6.99zł (0.0–0.0) | 7.11 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_4P_MINUS1` | 5.72 Er (8–1) | 0.1% | 2.4% | 1.45 (0–0) | 6.24 (0–0) | 6.54zł (0.0–0.0) | 6.52 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_5P_MINUS2` | 6.25 Er (8–1) | 0.1% | 2.5% | 1.63 (0–0) | 7.20 (0–0) | 7.02zł (0.0–0.0) | 7.11 (0.0–0.0) | 🟢 W NORMIE |
| `L2_GC_FALLS_5P_MINUS3` | 6.24 Er (8–1) | 0.1% | 2.5% | 1.63 (0–0) | 7.19 (0–0) | 7.01zł (0.0–0.0) | 7.11 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_STACKS_5P_MINUS3` | 6.22 Er (8–1) | 0.1% | 2.5% | 1.63 (0–0) | 7.13 (0–0) | 6.98zł (0.0–0.0) | 7.09 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_5P_MINUS1` | 6.23 Er (8–1) | 0.1% | 2.5% | 1.63 (0–0) | 7.17 (0–0) | 7.01zł (0.0–0.0) | 7.11 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_5P_MINUS2` | 6.11 Er (8–1) | 0.1% | 2.4% | 1.57 (0–0) | 6.93 (0–0) | 6.91zł (0.0–0.0) | 6.96 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_5P_MINUS1` | 6.16 Er (8–1) | 0.1% | 2.5% | 1.60 (0–0) | 7.02 (0–0) | 6.94zł (0.0–0.0) | 6.96 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_5P_MINUS1` | 6.19 Er (8–1) | 0.1% | 2.4% | 1.61 (0–0) | 7.05 (0–0) | 6.95zł (0.0–0.0) | 7.03 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_PLUS1` | 6.63 Er (8–1) | 0.2% | 2.5% | 1.75 (0–0) | 8.14 (0–0) | 7.48zł (0.0–0.0) | 7.30 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_PLUS1` | 6.62 Er (8–1) | 0.6% | 2.5% | 1.74 (0–0) | 8.15 (0–0) | 7.39zł (0.0–0.0) | 7.28 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KT_FRAGS_PLUS1` | 6.64 Er (8–1) | 0.2% | 2.4% | 1.74 (0–0) | 8.17 (0–0) | 7.54zł (0.0–0.0) | 7.40 (0.0–0.0) | 🟢 W NORMIE |
| `L2_SO_CONDEMNS_MINUS1` | 5.81 Er (8–1) | 0.1% | 2.4% | 1.53 (0–0) | 6.35 (0–0) | 6.63zł (0.0–0.0) | 7.00 (0.0–0.0) | 🟢 W NORMIE |
| `L2_KB_DECREES_MINUS1` | 5.13 Er (8–1) | 0.0% | 1.9% | 1.30 (0–0) | 4.97 (0–0) | 6.10zł (0.0–0.0) | 6.33 (0.0–0.0) | 🟢 W NORMIE |
| `L2_CAA_RELICS_MINUS1` | 4.56 Er (8–1) | 0.0% | 2.2% | 1.09 (0–0) | 4.39 (0–0) | 5.46zł (0.0–0.0) | 5.54 (0.0–0.0) | ⚠️ WARTOŚCI BRZEGOWE |

</details>

## 3. Ustalone Ramy i Normy Telemetryczne Silnika Gry

- **⏱️ Długość gry (Ery):** Normatyw: **5.0 – 7.0 Er** (Zakres dopuszczalny: min 1, max 8). Zbyt szybka wygrana (<5 Er) grozi brakiem budowy silniczka, zbyt długa (>7 Er) wywołuje znużenie.
- **🔒 Remisy (Deadlocks %):** Tolerowany próg: **< 15.0%** gier kończących się limitem 8 Er bez zwycięzcy.
- **💰 Pas Biedy (Poverty Rate %):** Tolerowany próg: **< 30.0%** tur spędzonych na wymuszonym pasowaniu z braku monety.
- **🔥 Autodafé / Partię:** Optymalny wskaźnik agresji Inkwizytora: **0.5 – 2.0** wyczyszczeń na grę.
- **⚖️ Oskarżenia na Dworze / Partię:** Optymalna częstotliwość procesów politycznych: **1.5 – 4.5** oskarżeń na grę.