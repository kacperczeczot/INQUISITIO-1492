# Raport Precyzyjnego Audytu Poziomu 3 (Parametry Pojedynczych Kart) — Wersja Balansu: v1.0-alpha.97

**Wersja Balansu:** `v1.0-alpha.97` | **Data:** 2026-08-29 22:34 | **Przeanalizowano Wariantów Kart:** 1103 | **Próba:** 5000 gier/setup | **Czas:** 80.06s
**Filtry:** Parametry: `cost,heresy` | Frakcja: `all` | Karta: `Wszystkie`
**Wynik Bazy Poziomu 3 (Global):** `🟢 93.6 pkt` | 3p: `0.0 pkt` | 4p: `93.6 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (82)

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | Baza (Bieżące parametry wszystkich kart) | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-04_C2_G3` | SO-04 (Publiczne Ostrzeżenie): koszt 1→2, złoto 1→3 | 93.6 → 🟢 ** 95.0** (`⬆️ +1.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 95.0 (`⬆️ +1.4`) | 0.0 → 0.0 (`= 0.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-11_COST_MINUS1` | SO-11 (Dekret Czystości Wiary): cost 1 → 0 | 93.6 → 🟢 ** 94.7** (`⬆️ +1.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.7 (`⬆️ +1.1`) | 0.0 → 0.0 (`= 0.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-04_C0_H1` | SO-04 (Publiczne Ostrzeżenie): koszt 1→0, herezja 0→1 | 93.6 → 🟢 ** 94.6** (`⬆️ +1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.6 (`⬆️ +1.0`) | 0.0 → 0.0 (`= 0.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-07_C2_G4` | SO-07 (Przesłuchanie Oficjum): koszt 1→2, złoto 2→4 | 93.6 → 🟢 ** 94.6** (`⬆️ +1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.6 (`⬆️ +1.0`) | 0.0 → 0.0 (`= 0.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-01_C0_G3` | SO-01 (Patrol Familiariuszy): koszt 1→0, złoto 2→3 | 93.6 → 🟢 ** 94.5** (`⬆️ +0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.5 (`⬆️ +0.9`) | 0.0 → 0.0 (`= 0.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-09_COST_PLUS1` | CAA-09 (Kurier Relikwii): cost 0 → 1 | 93.6 → 🟢 ** 94.4** (`⬆️ +0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.4 (`⬆️ +0.8`) | 0.0 → 0.0 (`= 0.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-09_C1_H0` | CAA-09 (Kurier Relikwii): koszt 0→1, herezja 0→0 | 93.6 → 🟢 ** 94.4** (`⬆️ +0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.4 (`⬆️ +0.8`) | 0.0 → 0.0 (`= 0.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-09_COST_PLUS2` | GC-09 (Lista Dłużników): cost 1 → 3 | 93.6 → 🟢 ** 94.4** (`⬆️ +0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.4 (`⬆️ +0.8`) | 0.0 → 0.0 (`= 0.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-07_COST_MINUS1` | SO-07 (Przesłuchanie Oficjum): cost 1 → 0 | 93.6 → 🟢 ** 94.4** (`⬆️ +0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.4 (`⬆️ +0.8`) | 0.0 → 0.0 (`= 0.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-07_C0_H0` | SO-07 (Przesłuchanie Oficjum): koszt 1→0, herezja 0→0 | 93.6 → 🟢 ** 94.4** (`⬆️ +0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.4 (`⬆️ +0.8`) | 0.0 → 0.0 (`= 0.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-07_C0_H1` | SO-07 (Przesłuchanie Oficjum): koszt 1→0, herezja 0→1 | 93.6 → 🟢 ** 94.4** (`⬆️ +0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.4 (`⬆️ +0.8`) | 0.0 → 0.0 (`= 0.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-11_C2_G3` | SO-11 (Dekret Czystości Wiary): koszt 1→2, złoto 1→3 | 93.6 → 🟢 ** 94.4** (`⬆️ +0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.4 (`⬆️ +0.8`) | 0.0 → 0.0 (`= 0.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-12_COST_MINUS1` | SO-12 (Straż Trybunalska): cost 1 → 0 | 93.6 → 🟢 ** 94.4** (`⬆️ +0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.4 (`⬆️ +0.8`) | 0.0 → 0.0 (`= 0.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-09_COST_PLUS2` | CAA-09 (Kurier Relikwii): cost 0 → 2 | 93.6 → 🟢 ** 94.3** (`⬆️ +0.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.3 (`⬆️ +0.7`) | 0.0 → 0.0 (`= 0.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-07_C2_G3` | SO-07 (Przesłuchanie Oficjum): koszt 1→2, złoto 2→3 | 93.6 → 🟢 ** 94.3** (`⬆️ +0.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.3 (`⬆️ +0.7`) | 0.0 → 0.0 (`= 0.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-07_G3_H0` | SO-07 (Przesłuchanie Oficjum): złoto 2→3, herezja 0→0 | 93.6 → 🟢 ** 94.3** (`⬆️ +0.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.3 (`⬆️ +0.7`) | 0.0 → 0.0 (`= 0.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-08_C1_G5` | SO-08 (Nasłanie Inkwizytora): koszt 0→1, złoto 3→5 | 93.6 → 🟢 ** 94.3** (`⬆️ +0.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.3 (`⬆️ +0.7`) | 0.0 → 0.0 (`= 0.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-07_C0_G3` | SO-07 (Przesłuchanie Oficjum): koszt 1→0, złoto 2→3 | 93.6 → 🟢 ** 94.2** (`⬆️ +0.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.2 (`⬆️ +0.6`) | 0.0 → 0.0 (`= 0.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-01_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): heresy 1 → 2 | 93.6 → 🟢 ** 94.1** (`⬆️ +0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.1 (`⬆️ +0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-01_COST_MINUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 0 | 93.6 → 🟢 ** 94.1** (`⬆️ +0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.1 (`⬆️ +0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-04_C2_G2` | SO-04 (Publiczne Ostrzeżenie): koszt 1→2, złoto 1→2 | 93.6 → 🟢 ** 94.1** (`⬆️ +0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.1 (`⬆️ +0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-04_G2_H0` | SO-04 (Publiczne Ostrzeżenie): złoto 1→2, herezja 0→0 | 93.6 → 🟢 ** 94.1** (`⬆️ +0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.1 (`⬆️ +0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-12_C2_G3` | SO-12 (Straż Trybunalska): koszt 1→2, złoto 1→3 | 93.6 → 🟢 ** 94.1** (`⬆️ +0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.1 (`⬆️ +0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-01_HERESY_PLUS2` | GC-01 (Przekupiony Strażnik): heresy 1 → 3 | 93.6 → 🟢 ** 94.0** (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.0 (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-01_G0_H2` | GC-01 (Przekupiony Strażnik): złoto 1→0, herezja 1→2 | 93.6 → 🟢 ** 94.0** (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.0 (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-11_HERESY_PLUS1` | GC-11 (Fałszywe Świadectwo Cechu): heresy 2 → 3 | 93.6 → 🟢 ** 94.0** (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.0 (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-11_C0_H3` | GC-11 (Fałszywe Świadectwo Cechu): koszt 0→0, herezja 2→3 | 93.6 → 🟢 ** 94.0** (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.0 (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-11_C1_H3` | GC-11 (Fałszywe Świadectwo Cechu): koszt 0→1, herezja 2→3 | 93.6 → 🟢 ** 94.0** (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.0 (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-11_G0_H3` | GC-11 (Fałszywe Świadectwo Cechu): złoto 0→0, herezja 2→3 | 93.6 → 🟢 ** 94.0** (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.0 (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-04_G2_H1` | SO-04 (Publiczne Ostrzeżenie): złoto 1→2, herezja 0→1 | 93.6 → 🟢 ** 94.0** (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.0 (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-05_COST_PLUS1` | SO-05 (Wezwanie do Trybunału): cost 0 → 1 | 93.6 → 🟢 ** 94.0** (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.0 (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-05_C1_H3` | SO-05 (Wezwanie do Trybunału): koszt 0→1, herezja 4→3 | 93.6 → 🟢 ** 94.0** (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.0 (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-05_C1_H5` | SO-05 (Wezwanie do Trybunału): koszt 0→1, herezja 4→5 | 93.6 → 🟢 ** 94.0** (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.0 (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-05_C1_G4` | SO-05 (Wezwanie do Trybunału): koszt 0→1, złoto 3→4 | 93.6 → 🟢 ** 94.0** (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.0 (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-05_C1_G5` | SO-05 (Wezwanie do Trybunału): koszt 0→1, złoto 3→5 | 93.6 → 🟢 ** 94.0** (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.0 (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-07_G3_H1` | SO-07 (Przesłuchanie Oficjum): złoto 2→3, herezja 0→1 | 93.6 → 🟢 ** 94.0** (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.0 (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-08_C0_G4` | SO-08 (Nasłanie Inkwizytora): koszt 0→0, złoto 3→4 | 93.6 → 🟢 ** 94.0** (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.0 (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-08_C0_G5` | SO-08 (Nasłanie Inkwizytora): koszt 0→0, złoto 3→5 | 93.6 → 🟢 ** 94.0** (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.0 (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-08_G4_H0` | SO-08 (Nasłanie Inkwizytora): złoto 3→4, herezja 0→0 | 93.6 → 🟢 ** 94.0** (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.0 (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-11_COST_PLUS1` | SO-11 (Dekret Czystości Wiary): cost 1 → 2 | 93.6 → 🟢 ** 94.0** (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 94.0 (`⬆️ +0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-01_HERESY_MINUS2` | CAA-01 (Przejście Podziemiami): heresy 2 → 0 | 93.6 → 🟢 ** 93.9** (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.9 (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-03_COST_PLUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 2 | 93.6 → 🟢 ** 93.9** (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.9 (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-03_COST_PLUS2` | GC-03 (Podrzucenie Księgi): cost 1 → 3 | 93.6 → 🟢 ** 93.9** (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.9 (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-03_C2_H3` | GC-03 (Podrzucenie Księgi): koszt 1→2, herezja 2→3 | 93.6 → 🟢 ** 93.9** (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.9 (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-05_COST_PLUS1` | GC-05 (Fałszywy Świadek): cost 1 → 2 | 93.6 → 🟢 ** 93.9** (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.9 (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-05_C2_H0` | GC-05 (Fałszywy Świadek): koszt 1→2, herezja 0→0 | 93.6 → 🟢 ** 93.9** (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.9 (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-05_C2_H1` | GC-05 (Fałszywy Świadek): koszt 1→2, herezja 0→1 | 93.6 → 🟢 ** 93.9** (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.9 (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-05_C2_G1` | GC-05 (Fałszywy Świadek): koszt 1→2, złoto 0→1 | 93.6 → 🟢 ** 93.9** (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.9 (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-05_C2_G2` | GC-05 (Fałszywy Świadek): koszt 1→2, złoto 0→2 | 93.6 → 🟢 ** 93.9** (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.9 (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-11_HERESY_PLUS2` | GC-11 (Fałszywe Świadectwo Cechu): heresy 2 → 4 | 93.6 → 🟢 ** 93.9** (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.9 (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-04_COST_MINUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 0 | 93.6 → 🟢 ** 93.9** (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.9 (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-04_C0_H0` | SO-04 (Publiczne Ostrzeżenie): koszt 1→0, herezja 0→0 | 93.6 → 🟢 ** 93.9** (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.9 (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-07_HERESY_PLUS2` | SO-07 (Przesłuchanie Oficjum): heresy 0 → 2 | 93.6 → 🟢 ** 93.9** (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.9 (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-07_HERESY_SET2` | SO-07 (Przesłuchanie Oficjum): dodaj heresy = 2 | 93.6 → 🟢 ** 93.9** (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.9 (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-12_C2_G2` | SO-12 (Straż Trybunalska): koszt 1→2, złoto 1→2 | 93.6 → 🟢 ** 93.9** (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.9 (`⬆️ +0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-09_C0_G1` | GC-09 (Lista Dłużników): koszt 1→0, złoto 0→1 | 93.6 → 🟢 ** 93.8** (`⬆️ +0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.8 (`⬆️ +0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-09_C0_G2` | GC-09 (Lista Dłużników): koszt 1→0, złoto 0→2 | 93.6 → 🟢 ** 93.8** (`⬆️ +0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.8 (`⬆️ +0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KT-01_HERESY_PLUS1` | KT-01 (Rytuał Przejścia): heresy 1 → 2 | 93.6 → 🟢 ** 93.8** (`⬆️ +0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.8 (`⬆️ +0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KT-04_C0_H1` | KT-04 (Zwierciadło Herezji): koszt 1→0, herezja 0→1 | 93.6 → 🟢 ** 93.8** (`⬆️ +0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.8 (`⬆️ +0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-01_C2_G4` | SO-01 (Patrol Familiariuszy): koszt 1→2, złoto 2→4 | 93.6 → 🟢 ** 93.8** (`⬆️ +0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.8 (`⬆️ +0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-08_COST_PLUS1` | SO-08 (Nasłanie Inkwizytora): cost 0 → 1 | 93.6 → 🟢 ** 93.8** (`⬆️ +0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.8 (`⬆️ +0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-08_C1_H0` | SO-08 (Nasłanie Inkwizytora): koszt 0→1, herezja 0→0 | 93.6 → 🟢 ** 93.8** (`⬆️ +0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.8 (`⬆️ +0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-10_COST_MINUS1` | SO-10 (Oczyść Miasto): cost 5 → 4 | 93.6 → 🟢 ** 93.8** (`⬆️ +0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.8 (`⬆️ +0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 2 → 3 | 93.6 → 🟢 ** 93.7** (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.7 (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-01_HERESY_MINUS1` | CAA-01 (Przejście Podziemiami): heresy 2 → 1 | 93.6 → 🟢 ** 93.7** (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.7 (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-01_C3_H1` | CAA-01 (Przejście Podziemiami): koszt 2→3, herezja 2→1 | 93.6 → 🟢 ** 93.7** (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.7 (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-01_C3_H3` | CAA-01 (Przejście Podziemiami): koszt 2→3, herezja 2→3 | 93.6 → 🟢 ** 93.7** (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.7 (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-01_C3_G1` | CAA-01 (Przejście Podziemiami): koszt 2→3, złoto 0→1 | 93.6 → 🟢 ** 93.7** (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.7 (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-01_G0_H1` | CAA-01 (Przejście Podziemiami): złoto 0→0, herezja 2→1 | 93.6 → 🟢 ** 93.7** (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.7 (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-01_C2_H2` | GC-01 (Przekupiony Strażnik): koszt 1→2, herezja 1→2 | 93.6 → 🟢 ** 93.7** (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.7 (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-03_HERESY_PLUS1` | GC-03 (Podrzucenie Księgi): heresy 2 → 3 | 93.6 → 🟢 ** 93.7** (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.7 (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-03_C0_H3` | GC-03 (Podrzucenie Księgi): koszt 1→0, herezja 2→3 | 93.6 → 🟢 ** 93.7** (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.7 (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-03_C2_G1` | GC-03 (Podrzucenie Księgi): koszt 1→2, złoto 0→1 | 93.6 → 🟢 ** 93.7** (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.7 (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-03_G0_H3` | GC-03 (Podrzucenie Księgi): złoto 0→0, herezja 2→3 | 93.6 → 🟢 ** 93.7** (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.7 (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-09_G1_H0` | GC-09 (Lista Dłużników): złoto 0→1, herezja 0→0 | 93.6 → 🟢 ** 93.7** (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.7 (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KB-01_HERESY_PLUS1` | KB-01 (Rozkaz Dworu): heresy 1 → 2 | 93.6 → 🟢 ** 93.7** (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.7 (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KB-01_G0_H2` | KB-01 (Rozkaz Dworu): złoto 0→0, herezja 1→2 | 93.6 → 🟢 ** 93.7** (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.7 (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-03_C3_G1` | SO-03 (Podejrzenie): koszt 2→3, złoto 0→1 | 93.6 → 🟢 ** 93.7** (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.7 (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-07_HERESY_PLUS1` | SO-07 (Przesłuchanie Oficjum): heresy 0 → 1 | 93.6 → 🟢 ** 93.7** (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.7 (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-07_HERESY_SET1` | SO-07 (Przesłuchanie Oficjum): dodaj heresy = 1 | 93.6 → 🟢 ** 93.7** (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.7 (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-08_COST_PLUS2` | SO-08 (Nasłanie Inkwizytora): cost 0 → 2 | 93.6 → 🟢 ** 93.7** (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.7 (`⬆️ +0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 1021 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_CAA-01_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): heresy 2 → 3 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-01_HERESY_PLUS2` | CAA-01 (Przejście Podziemiami): heresy 2 → 4 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-01_G0_H3` | CAA-01 (Przejście Podziemiami): złoto 0→0, herezja 2→3 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-02_C1_G4` | CAA-02 (Złoto z Kryjówki): koszt 0→1, złoto 3→4 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-03_C1_G3` | CAA-03 (Cień na Rynku): koszt 0→1, złoto 2→3 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-05_COST_PLUS1` | CAA-05 (Ukryty Kurier): cost 0 → 1 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-05_C1_H0` | CAA-05 (Ukryty Kurier): koszt 0→1, herezja 0→0 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-05_C0_G5` | CAA-05 (Ukryty Kurier): koszt 0→0, złoto 4→5 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-05_C0_G6` | CAA-05 (Ukryty Kurier): koszt 0→0, złoto 4→6 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-05_C1_G5` | CAA-05 (Ukryty Kurier): koszt 0→1, złoto 4→5 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-05_C1_G6` | CAA-05 (Ukryty Kurier): koszt 0→1, złoto 4→6 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-05_G3_H0` | CAA-05 (Ukryty Kurier): złoto 4→3, herezja 0→0 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-05_G5_H0` | CAA-05 (Ukryty Kurier): złoto 4→5, herezja 0→0 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-07_C0_G4` | CAA-07 (Szantaż Bractwa): koszt 0→0, złoto 3→4 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-07_C1_G4` | CAA-07 (Szantaż Bractwa): koszt 0→1, złoto 3→4 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-07_G4_H0` | CAA-07 (Szantaż Bractwa): złoto 3→4, herezja 0→0 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-09_C1_G1` | CAA-09 (Kurier Relikwii): koszt 0→1, złoto 0→1 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-11_C2_G2` | CAA-11 (Nocna Zmiana Warty): koszt 1→2, złoto 1→2 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-03_G1_H3` | GC-03 (Podrzucenie Księgi): złoto 0→1, herezja 2→3 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-05_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): heresy 0 → 1 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-05_HERESY_PLUS2` | GC-05 (Fałszywy Świadek): heresy 0 → 2 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-05_HERESY_SET1` | GC-05 (Fałszywy Świadek): dodaj heresy = 1 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-05_HERESY_SET2` | GC-05 (Fałszywy Świadek): dodaj heresy = 2 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-05_G0_H1` | GC-05 (Fałszywy Świadek): złoto 0→0, herezja 0→1 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-05_G1_H0` | GC-05 (Fałszywy Świadek): złoto 0→1, herezja 0→0 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-05_G1_H1` | GC-05 (Fałszywy Świadek): złoto 0→1, herezja 0→1 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-06_COST_MINUS1` | GC-06 (Szantaż): cost 3 → 2 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-08_G0_H3` | GC-08 (Zatrute Złoto): złoto 1→0, herezja 2→3 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-10_C3_G2` | GC-10 (Upadek Domu): koszt 4→3, złoto 0→2 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KB-05_HERESY_MINUS1` | KB-05 (List Żelazny): heresy 1 → 0 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KB-05_G0_H0` | KB-05 (List Żelazny): złoto 0→0, herezja 1→0 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KB-12_HERESY_MINUS2` | KB-12 (Szantaż Salonowy): heresy 2 → 0 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KT-01_G0_H0` | KT-01 (Rytuał Przejścia): złoto 1→0, herezja 1→0 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-01_C0_G4` | SO-01 (Patrol Familiariuszy): koszt 1→0, złoto 2→4 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-05_HERESY_PLUS1` | SO-05 (Wezwanie do Trybunału): heresy 4 → 5 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-05_HERESY_PLUS2` | SO-05 (Wezwanie do Trybunału): heresy 4 → 6 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-05_HERESY_MINUS1` | SO-05 (Wezwanie do Trybunału): heresy 4 → 3 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-05_HERESY_MINUS2` | SO-05 (Wezwanie do Trybunału): heresy 4 → 2 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-05_C0_H3` | SO-05 (Wezwanie do Trybunału): koszt 0→0, herezja 4→3 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-05_C0_H5` | SO-05 (Wezwanie do Trybunału): koszt 0→0, herezja 4→5 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-05_C0_G4` | SO-05 (Wezwanie do Trybunału): koszt 0→0, złoto 3→4 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-05_C0_G5` | SO-05 (Wezwanie do Trybunału): koszt 0→0, złoto 3→5 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-05_G2_H3` | SO-05 (Wezwanie do Trybunału): złoto 3→2, herezja 4→3 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-05_G2_H5` | SO-05 (Wezwanie do Trybunału): złoto 3→2, herezja 4→5 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-05_G4_H3` | SO-05 (Wezwanie do Trybunału): złoto 3→4, herezja 4→3 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-05_G4_H5` | SO-05 (Wezwanie do Trybunału): złoto 3→4, herezja 4→5 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-06_HERESY_PLUS2` | SO-06 (Areszt Trybunalski): heresy 0 → 2 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-06_HERESY_SET2` | SO-06 (Areszt Trybunalski): dodaj heresy = 2 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-06_G1_H1` | SO-06 (Areszt Trybunalski): złoto 0→1, herezja 0→1 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-08_G2_H0` | SO-08 (Nasłanie Inkwizytora): złoto 3→2, herezja 0→0 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-09_C0_H2` | SO-09 (Świadek Koronny): koszt 1→0, herezja 1→2 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-11_C0_H2` | SO-11 (Dekret Czystości Wiary): koszt 1→0, herezja 1→2 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-11_C2_H2` | SO-11 (Dekret Czystości Wiary): koszt 1→2, herezja 1→2 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-12_HERESY_PLUS1` | SO-12 (Straż Trybunalska): heresy 2 → 3 | 93.6 → 🟢 ** 93.6** (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.6 (`= 0.0`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-01_COST_PLUS2` | CAA-01 (Przejście Podziemiami): cost 2 → 4 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-04_C1_G4` | CAA-04 (Fałszywy Trop): koszt 0→1, złoto 3→4 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-06_C1_G1` | CAA-06 (Ucieczka z Lochów): koszt 0→1, złoto 0→1 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-07_C1_G5` | CAA-07 (Szantaż Bractwa): koszt 0→1, złoto 3→5 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-08_COST_PLUS1` | CAA-08 (Kaptur Nocy): cost 2 → 3 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-08_C3_H0` | CAA-08 (Kaptur Nocy): koszt 2→3, herezja 0→0 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-02_COST_PLUS1` | GC-02 (Czarny Rynek): cost 0 → 1 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-02_C1_H0` | GC-02 (Czarny Rynek): koszt 0→1, herezja 0→0 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-02_C1_G3` | GC-02 (Czarny Rynek): koszt 0→1, złoto 2→3 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-02_G1_H0` | GC-02 (Czarny Rynek): złoto 2→1, herezja 0→0 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-03_COST_MINUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 0 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-03_HERESY_PLUS2` | GC-03 (Podrzucenie Księgi): heresy 2 → 4 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-08_COST_PLUS2` | GC-08 (Zatrute Złoto): cost 1 → 3 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 2 → 3 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-08_HERESY_PLUS2` | GC-08 (Zatrute Złoto): heresy 2 → 4 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-09_COST_MINUS1` | GC-09 (Lista Dłużników): cost 1 → 0 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-09_C0_H0` | GC-09 (Lista Dłużników): koszt 1→0, herezja 0→0 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-10_COST_MINUS1` | GC-10 (Upadek Domu): cost 4 → 3 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-11_COST_PLUS1` | GC-11 (Fałszywe Świadectwo Cechu): cost 0 → 1 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-11_C1_G1` | GC-11 (Fałszywe Świadectwo Cechu): koszt 0→1, złoto 0→1 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KT-01_HERESY_PLUS2` | KT-01 (Rytuał Przejścia): heresy 1 → 3 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KT-01_G0_H2` | KT-01 (Rytuał Przejścia): złoto 1→0, herezja 1→2 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KT-04_COST_PLUS2` | KT-04 (Zwierciadło Herezji): cost 1 → 3 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KT-04_G1_H1` | KT-04 (Zwierciadło Herezji): złoto 0→1, herezja 0→1 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-01_HERESY_PLUS1` | SO-01 (Patrol Familiariuszy): heresy 2 → 3 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-02_COST_PLUS2` | SO-02 (Skarbiec Trybunału): cost 1 → 3 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-02_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): heresy 2 → 3 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-02_C0_H3` | SO-02 (Skarbiec Trybunału): koszt 1→0, herezja 2→3 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-02_G1_H3` | SO-02 (Skarbiec Trybunału): złoto 2→1, herezja 2→3 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-08_C1_G4` | SO-08 (Nasłanie Inkwizytora): koszt 0→1, złoto 3→4 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-11_C0_G3` | SO-11 (Dekret Czystości Wiary): koszt 1→0, złoto 1→3 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-12_C2_H1` | SO-12 (Straż Trybunalska): koszt 1→2, herezja 2→1 | 93.6 → 🟢 ** 93.5** (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.5 (`🔻 -0.1`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-01_C1_H1` | CAA-01 (Przejście Podziemiami): koszt 2→1, herezja 2→1 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-01_G1_H1` | CAA-01 (Przejście Podziemiami): złoto 0→1, herezja 2→1 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-07_C0_G5` | CAA-07 (Szantaż Bractwa): koszt 0→0, złoto 3→5 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-08_C3_G3` | CAA-08 (Kaptur Nocy): koszt 2→3, złoto 2→3 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-10_C3_G1` | CAA-10 (Echo Alhambry): koszt 2→3, złoto 0→1 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-10_G1_H0` | CAA-10 (Echo Alhambry): złoto 0→1, herezja 0→0 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-01_COST_PLUS2` | GC-01 (Przekupiony Strażnik): cost 1 → 3 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-01_C0_G3` | GC-01 (Przekupiony Strażnik): koszt 1→0, złoto 1→3 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-05_COST_MINUS1` | GC-05 (Fałszywy Świadek): cost 1 → 0 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-05_C0_H0` | GC-05 (Fałszywy Świadek): koszt 1→0, herezja 0→0 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-05_C0_H1` | GC-05 (Fałszywy Świadek): koszt 1→0, herezja 0→1 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-05_C0_G1` | GC-05 (Fałszywy Świadek): koszt 1→0, złoto 0→1 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-05_C0_G2` | GC-05 (Fałszywy Świadek): koszt 1→0, złoto 0→2 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 1 → 2 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-08_C2_H3` | GC-08 (Zatrute Złoto): koszt 1→2, herezja 2→3 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-08_C2_G2` | GC-08 (Zatrute Złoto): koszt 1→2, złoto 1→2 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-08_G0_H1` | GC-08 (Zatrute Złoto): złoto 1→0, herezja 2→1 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-11_COST_PLUS2` | GC-11 (Fałszywe Świadectwo Cechu): cost 0 → 2 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KT-01_COST_PLUS2` | KT-01 (Rytuał Przejścia): cost 1 → 3 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KT-02_C1_G4` | KT-02 (Transmutacja Złota): koszt 0→1, złoto 3→4 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KT-04_HERESY_PLUS1` | KT-04 (Zwierciadło Herezji): heresy 0 → 1 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KT-04_HERESY_SET1` | KT-04 (Zwierciadło Herezji): dodaj heresy = 1 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KT-04_G0_H1` | KT-04 (Zwierciadło Herezji): złoto 0→0, herezja 0→1 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KT-05_C2_G1` | KT-05 (Wskazówka Cyklu): koszt 1→2, złoto 0→1 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-02_HERESY_PLUS2` | SO-02 (Skarbiec Trybunału): heresy 2 → 4 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-03_G1_H5` | SO-03 (Podejrzenie): złoto 0→1, herezja 4→5 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-11_C0_G2` | SO-11 (Dekret Czystości Wiary): koszt 1→0, złoto 1→2 | 93.6 → 🟢 ** 93.4** (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.4 (`🔻 -0.2`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-01_C1_H3` | CAA-01 (Przejście Podziemiami): koszt 2→1, herezja 2→3 | 93.6 → 🟢 ** 93.3** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.3 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-01_G1_H3` | CAA-01 (Przejście Podziemiami): złoto 0→1, herezja 2→3 | 93.6 → 🟢 ** 93.3** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.3 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-03_C0_G3` | CAA-03 (Cień na Rynku): koszt 0→0, złoto 2→3 | 93.6 → 🟢 ** 93.3** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.3 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-03_C1_G4` | CAA-03 (Cień na Rynku): koszt 0→1, złoto 2→4 | 93.6 → 🟢 ** 93.3** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.3 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-12_G3_H1` | CAA-12 (Skrytka w Murach): złoto 4→3, herezja 0→1 | 93.6 → 🟢 ** 93.3** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.3 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-01_C0_G2` | GC-01 (Przekupiony Strażnik): koszt 1→0, złoto 1→2 | 93.6 → 🟢 ** 93.3** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.3 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-04_C2_G1` | GC-04 (Informator): koszt 1→2, złoto 0→1 | 93.6 → 🟢 ** 93.3** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.3 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-05_COST_PLUS2` | GC-05 (Fałszywy Świadek): cost 1 → 3 | 93.6 → 🟢 ** 93.3** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.3 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-07_G2_H0` | GC-07 (Skrytobójstwo): złoto 3→2, herezja 0→0 | 93.6 → 🟢 ** 93.3** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.3 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-08_C0_H3` | GC-08 (Zatrute Złoto): koszt 1→0, herezja 2→3 | 93.6 → 🟢 ** 93.3** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.3 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-08_C2_H1` | GC-08 (Zatrute Złoto): koszt 1→2, herezja 2→1 | 93.6 → 🟢 ** 93.3** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.3 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-09_COST_PLUS1` | GC-09 (Lista Dłużników): cost 1 → 2 | 93.6 → 🟢 ** 93.3** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.3 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-09_C2_H0` | GC-09 (Lista Dłużników): koszt 1→2, herezja 0→0 | 93.6 → 🟢 ** 93.3** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.3 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-09_C2_G2` | GC-09 (Lista Dłużników): koszt 1→2, złoto 0→2 | 93.6 → 🟢 ** 93.3** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.3 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-10_C3_G1` | GC-10 (Upadek Domu): koszt 4→3, złoto 0→1 | 93.6 → 🟢 ** 93.3** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.3 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-12_C0_G2` | GC-12 (Złodziejski Zwiad): koszt 0→0, złoto 1→2 | 93.6 → 🟢 ** 93.3** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.3 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KB-08_G1_H3` | KB-08 (Przekupstwo Sędziego): złoto 0→1, herezja 2→3 | 93.6 → 🟢 ** 93.3** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.3 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KT-09_C2_G1` | KT-09 (Fragment Kodeksu): koszt 1→2, złoto 0→1 | 93.6 → 🟢 ** 93.3** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.3 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-03_C1_H5` | SO-03 (Podejrzenie): koszt 2→1, herezja 4→5 | 93.6 → 🟢 ** 93.3** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.3 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-08_G4_H1` | SO-08 (Nasłanie Inkwizytora): złoto 3→4, herezja 0→1 | 93.6 → 🟢 ** 93.3** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.3 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-09_C2_H0` | SO-09 (Świadek Koronny): koszt 1→2, herezja 1→0 | 93.6 → 🟢 ** 93.3** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.3 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-11_C2_G2` | SO-11 (Dekret Czystości Wiary): koszt 1→2, złoto 1→2 | 93.6 → 🟢 ** 93.3** (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.3 (`🔻 -0.3`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 0 → 1 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-02_C1_H0` | CAA-02 (Złoto z Kryjówki): koszt 0→1, herezja 0→0 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-02_G2_H0` | CAA-02 (Złoto z Kryjówki): złoto 3→2, herezja 0→0 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-04_COST_PLUS1` | CAA-04 (Fałszywy Trop): cost 0 → 1 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-04_C1_H0` | CAA-04 (Fałszywy Trop): koszt 0→1, herezja 0→0 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-04_G2_H0` | CAA-04 (Fałszywy Trop): złoto 3→2, herezja 0→0 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-08_C3_H1` | CAA-08 (Kaptur Nocy): koszt 2→3, herezja 0→1 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-08_G1_H0` | CAA-08 (Kaptur Nocy): złoto 2→1, herezja 0→0 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-12_COST_PLUS2` | CAA-12 (Skrytka w Murach): cost 1 → 3 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-12_C2_H1` | CAA-12 (Skrytka w Murach): koszt 1→2, herezja 0→1 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-12_C2_G5` | CAA-12 (Skrytka w Murach): koszt 1→2, złoto 4→5 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-12_G3_H0` | CAA-12 (Skrytka w Murach): złoto 4→3, herezja 0→0 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-01_COST_PLUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 2 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-03_C2_G2` | GC-03 (Podrzucenie Księgi): koszt 1→2, złoto 0→2 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-04_COST_PLUS1` | GC-04 (Informator): cost 1 → 2 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-04_C2_G2` | GC-04 (Informator): koszt 1→2, złoto 0→2 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-06_G1_H2` | GC-06 (Szantaż): złoto 0→1, herezja 1→2 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-08_G2_H3` | GC-08 (Zatrute Złoto): złoto 1→2, herezja 2→3 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-12_C0_G3` | GC-12 (Złodziejski Zwiad): koszt 0→0, złoto 1→3 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KB-08_COST_PLUS2` | KB-08 (Przekupstwo Sędziego): cost 3 → 5 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KB-08_G1_H1` | KB-08 (Przekupstwo Sędziego): złoto 0→1, herezja 2→1 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KT-03_C1_G1` | KT-03 (Zakazana Wiedza): koszt 0→1, złoto 0→1 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KT-12_C2_G1` | KT-12 (Strażnik Archiwum): koszt 1→2, złoto 0→1 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-01_C2_G3` | SO-01 (Patrol Familiariuszy): koszt 1→2, złoto 2→3 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-04_HERESY_PLUS1` | SO-04 (Publiczne Ostrzeżenie): heresy 0 → 1 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-04_HERESY_SET1` | SO-04 (Publiczne Ostrzeżenie): dodaj heresy = 1 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-09_HERESY_MINUS1` | SO-09 (Świadek Koronny): heresy 1 → 0 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-09_G0_H0` | SO-09 (Świadek Koronny): złoto 0→0, herezja 1→0 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-10_C6_H0` | SO-10 (Oczyść Miasto): koszt 5→6, herezja 1→0 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-11_COST_PLUS2` | SO-11 (Dekret Czystości Wiary): cost 1 → 3 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-11_HERESY_PLUS2` | SO-11 (Dekret Czystości Wiary): heresy 1 → 3 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-11_G2_H2` | SO-11 (Dekret Czystości Wiary): złoto 1→2, herezja 1→2 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-12_HERESY_PLUS2` | SO-12 (Straż Trybunalska): heresy 2 → 4 | 93.6 → 🟢 ** 93.2** (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.2 (`🔻 -0.4`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-03_C0_G4` | CAA-03 (Cień na Rynku): koszt 0→0, złoto 2→4 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-05_COST_PLUS2` | CAA-05 (Ukryty Kurier): cost 0 → 2 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 0 → 1 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-07_C1_H0` | CAA-07 (Szantaż Bractwa): koszt 0→1, herezja 0→0 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-07_C1_H1` | CAA-07 (Szantaż Bractwa): koszt 0→1, herezja 0→1 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-07_G2_H0` | CAA-07 (Szantaż Bractwa): złoto 3→2, herezja 0→0 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-07_G2_H1` | CAA-07 (Szantaż Bractwa): złoto 3→2, herezja 0→1 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-08_G1_H1` | CAA-08 (Kaptur Nocy): złoto 2→1, herezja 0→1 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-12_COST_PLUS1` | CAA-12 (Skrytka w Murach): cost 1 → 2 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-12_C2_H0` | CAA-12 (Skrytka w Murach): koszt 1→2, herezja 0→0 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-01_COST_MINUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 0 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-06_C2_H2` | GC-06 (Szantaż): koszt 3→2, herezja 1→2 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-06_C4_H0` | GC-06 (Szantaż): koszt 3→4, herezja 1→0 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-07_C0_G4` | GC-07 (Skrytobójstwo): koszt 0→0, złoto 3→4 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-07_C0_G5` | GC-07 (Skrytobójstwo): koszt 0→0, złoto 3→5 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-07_G4_H0` | GC-07 (Skrytobójstwo): złoto 3→4, herezja 0→0 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-09_C2_G1` | GC-09 (Lista Dłużników): koszt 1→2, złoto 0→1 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_GC-10_COST_MINUS2` | GC-10 (Upadek Domu): cost 4 → 2 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KB-01_HERESY_PLUS2` | KB-01 (Rozkaz Dworu): heresy 1 → 3 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KB-08_HERESY_PLUS1` | KB-08 (Przekupstwo Sędziego): heresy 2 → 3 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KB-08_HERESY_MINUS1` | KB-08 (Przekupstwo Sędziego): heresy 2 → 1 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KB-08_G0_H1` | KB-08 (Przekupstwo Sędziego): złoto 0→0, herezja 2→1 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KB-08_G0_H3` | KB-08 (Przekupstwo Sędziego): złoto 0→0, herezja 2→3 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KT-04_COST_PLUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 2 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_KT-04_C2_H0` | KT-04 (Zwierciadło Herezji): koszt 1→2, herezja 0→0 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-02_G3_H3` | SO-02 (Skarbiec Trybunału): złoto 2→3, herezja 2→3 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-03_COST_MINUS1` | SO-03 (Podejrzenie): cost 2 → 1 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-09_HERESY_PLUS1` | SO-09 (Świadek Koronny): heresy 1 → 2 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-09_HERESY_PLUS2` | SO-09 (Świadek Koronny): heresy 1 → 3 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-09_C2_G1` | SO-09 (Świadek Koronny): koszt 1→2, złoto 0→1 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-09_G0_H2` | SO-09 (Świadek Koronny): złoto 0→0, herezja 1→2 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-11_HERESY_PLUS1` | SO-11 (Dekret Czystości Wiary): heresy 1 → 2 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-11_G0_H2` | SO-11 (Dekret Czystości Wiary): złoto 1→0, herezja 1→2 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_SO-12_COST_PLUS2` | SO-12 (Straż Trybunalska): cost 1 → 3 | 93.6 → 🟢 ** 93.1** (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.1 (`🔻 -0.5`) | 0.0 → 0.0 (`= 0.0`) | ⚪ OPTYMALNY |
| `L3_CAA-01_C3_G2` | CAA-01 (Przejście Podziemiami): koszt 2→3, złoto 0→2 | 93.6 → 🟢 ** 93.0** (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.0 (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_COST_PLUS1` | CAA-03 (Cień na Rynku): cost 0 → 1 | 93.6 → 🟢 ** 93.0** (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.0 (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_COST_MINUS1` | CAA-10 (Echo Alhambry): cost 2 → 1 | 93.6 → 🟢 ** 93.0** (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.0 (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_C1_H0` | CAA-10 (Echo Alhambry): koszt 2→1, herezja 0→0 | 93.6 → 🟢 ** 93.0** (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.0 (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-12_COST_MINUS1` | CAA-12 (Skrytka w Murach): cost 1 → 0 | 93.6 → 🟢 ** 93.0** (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.0 (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-12_C0_H0` | CAA-12 (Skrytka w Murach): koszt 1→0, herezja 0→0 | 93.6 → 🟢 ** 93.0** (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.0 (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-12_G5_H0` | CAA-12 (Skrytka w Murach): złoto 4→5, herezja 0→0 | 93.6 → 🟢 ** 93.0** (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.0 (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_C2_G2` | GC-01 (Przekupiony Strażnik): koszt 1→2, złoto 1→2 | 93.6 → 🟢 ** 93.0** (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.0 (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_C2_G3` | GC-01 (Przekupiony Strażnik): koszt 1→2, złoto 1→3 | 93.6 → 🟢 ** 93.0** (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.0 (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_HERESY_PLUS1` | GC-02 (Czarny Rynek): heresy 0 → 1 | 93.6 → 🟢 ** 93.0** (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.0 (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_HERESY_SET1` | GC-02 (Czarny Rynek): dodaj heresy = 1 | 93.6 → 🟢 ** 93.0** (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.0 (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_C0_H1` | GC-02 (Czarny Rynek): koszt 0→0, herezja 0→1 | 93.6 → 🟢 ** 93.0** (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.0 (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_COST_MINUS1` | GC-04 (Informator): cost 1 → 0 | 93.6 → 🟢 ** 93.0** (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.0 (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_C4_G2` | GC-06 (Szantaż): koszt 3→4, złoto 0→2 | 93.6 → 🟢 ** 93.0** (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.0 (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_C1_G4` | GC-07 (Skrytobójstwo): koszt 0→1, złoto 3→4 | 93.6 → 🟢 ** 93.0** (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.0 (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_COST_PLUS2` | KB-04 (Faworyt Dworu): cost 2 → 4 | 93.6 → 🟢 ** 93.0** (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.0 (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_HERESY_PLUS1` | SO-03 (Podejrzenie): heresy 4 → 5 | 93.6 → 🟢 ** 93.0** (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.0 (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_G0_H5` | SO-03 (Podejrzenie): złoto 0→0, herezja 4→5 | 93.6 → 🟢 ** 93.0** (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.0 (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_C0_G2` | SO-04 (Publiczne Ostrzeżenie): koszt 1→0, złoto 1→2 | 93.6 → 🟢 ** 93.0** (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.0 (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-07_C0_G4` | SO-07 (Przesłuchanie Oficjum): koszt 1→0, złoto 2→4 | 93.6 → 🟢 ** 93.0** (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.0 (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_G1_H2` | SO-09 (Świadek Koronny): złoto 0→1, herezja 1→2 | 93.6 → 🟢 ** 93.0** (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 93.0 (`🔻 -0.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_COST_PLUS2` | CAA-04 (Fałszywy Trop): cost 0 → 2 | 93.6 → 🟢 ** 92.9** (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.9 (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_C1_G2` | CAA-10 (Echo Alhambry): koszt 2→1, złoto 0→2 | 93.6 → 🟢 ** 92.9** (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.9 (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_C3_G2` | CAA-10 (Echo Alhambry): koszt 2→3, złoto 0→2 | 93.6 → 🟢 ** 92.9** (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.9 (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-12_C0_G6` | CAA-12 (Skrytka w Murach): koszt 1→0, złoto 4→6 | 93.6 → 🟢 ** 92.9** (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.9 (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_C1_H1` | GC-02 (Czarny Rynek): koszt 0→1, herezja 0→1 | 93.6 → 🟢 ** 92.9** (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.9 (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_C0_G1` | GC-04 (Informator): koszt 1→0, złoto 0→1 | 93.6 → 🟢 ** 92.9** (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.9 (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_COST_PLUS2` | GC-07 (Skrytobójstwo): cost 0 → 2 | 93.6 → 🟢 ** 92.9** (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.9 (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_HERESY_MINUS2` | GC-08 (Zatrute Złoto): heresy 2 → 0 | 93.6 → 🟢 ** 92.9** (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.9 (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-12_C1_G2` | GC-12 (Złodziejski Zwiad): koszt 0→1, złoto 1→2 | 93.6 → 🟢 ** 92.9** (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.9 (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-12_C1_G3` | GC-12 (Złodziejski Zwiad): koszt 0→1, złoto 1→3 | 93.6 → 🟢 ** 92.9** (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.9 (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_HERESY_MINUS1` | KB-01 (Rozkaz Dworu): heresy 1 → 0 | 93.6 → 🟢 ** 92.9** (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.9 (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_G0_H0` | KB-01 (Rozkaz Dworu): złoto 0→0, herezja 1→0 | 93.6 → 🟢 ** 92.9** (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.9 (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_C3_G1` | KB-04 (Faworyt Dworu): koszt 2→3, złoto 0→1 | 93.6 → 🟢 ** 92.9** (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.9 (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_C4_H1` | KB-08 (Przekupstwo Sędziego): koszt 3→4, herezja 2→1 | 93.6 → 🟢 ** 92.9** (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.9 (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_C2_G2` | KT-01 (Rytuał Przejścia): koszt 1→2, złoto 1→2 | 93.6 → 🟢 ** 92.9** (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.9 (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-05_COST_PLUS2` | SO-05 (Wezwanie do Trybunału): cost 0 → 2 | 93.6 → 🟢 ** 92.9** (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.9 (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_COST_PLUS2` | SO-06 (Areszt Trybunalski): cost 2 → 4 | 93.6 → 🟢 ** 92.9** (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.9 (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_C1_H1` | SO-06 (Areszt Trybunalski): koszt 2→1, herezja 0→1 | 93.6 → 🟢 ** 92.9** (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.9 (`🔻 -0.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-01_COST_MINUS1` | CAA-01 (Przejście Podziemiami): cost 2 → 1 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_COST_PLUS2` | CAA-07 (Szantaż Bractwa): cost 0 → 2 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_COST_PLUS2` | CAA-08 (Kaptur Nocy): cost 2 → 4 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_COST_MINUS1` | CAA-08 (Kaptur Nocy): cost 2 → 1 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_C1_H0` | CAA-08 (Kaptur Nocy): koszt 2→1, herezja 0→0 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_C3_G4` | CAA-08 (Kaptur Nocy): koszt 2→3, złoto 2→4 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_G3_H0` | CAA-08 (Kaptur Nocy): złoto 2→3, herezja 0→0 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_COST_MINUS2` | CAA-10 (Echo Alhambry): cost 2 → 0 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_C1_G1` | CAA-10 (Echo Alhambry): koszt 2→1, złoto 0→1 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-12_C0_G5` | CAA-12 (Skrytka w Murach): koszt 1→0, złoto 4→5 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_C0_G4` | GC-02 (Czarny Rynek): koszt 0→0, złoto 2→4 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-12_G2_H1` | GC-12 (Złodziejski Zwiad): złoto 1→2, herezja 2→1 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_C4_G1` | KB-08 (Przekupstwo Sędziego): koszt 3→4, złoto 0→1 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_G1_H0` | KB-10 (Pieczęć Korony): złoto 2→1, herezja 1→0 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_C2_H0` | KT-01 (Rytuał Przejścia): koszt 1→2, herezja 1→0 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_C2_H2` | KT-01 (Rytuał Przejścia): koszt 1→2, herezja 1→2 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-04_C2_G1` | KT-04 (Zwierciadło Herezji): koszt 1→2, złoto 0→1 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_HERESY_PLUS1` | KT-07 (Archiwum Ukryte): heresy 0 → 1 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_HERESY_SET1` | KT-07 (Archiwum Ukryte): dodaj heresy = 1 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_C2_G1` | KT-07 (Archiwum Ukryte): koszt 1→2, złoto 0→1 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_G0_H1` | KT-07 (Archiwum Ukryte): złoto 0→0, herezja 0→1 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): heresy 0 → 1 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_HERESY_SET1` | SO-06 (Areszt Trybunalski): dodaj heresy = 1 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_C3_H1` | SO-06 (Areszt Trybunalski): koszt 2→3, herezja 0→1 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_G0_H1` | SO-06 (Areszt Trybunalski): złoto 0→0, herezja 0→1 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_HERESY_MINUS1` | SO-10 (Oczyść Miasto): heresy 1 → 0 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_C4_G1` | SO-10 (Oczyść Miasto): koszt 5→4, złoto 0→1 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_G0_H0` | SO-10 (Oczyść Miasto): złoto 0→0, herezja 1→0 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-12_C0_H1` | SO-12 (Straż Trybunalska): koszt 1→0, herezja 2→1 | 93.6 → 🟢 ** 92.8** (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.8 (`🔻 -0.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_COST_PLUS2` | CAA-02 (Złoto z Kryjówki): cost 0 → 2 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_C1_H1` | CAA-02 (Złoto z Kryjówki): koszt 0→1, herezja 0→1 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_G2_H1` | CAA-02 (Złoto z Kryjówki): złoto 3→2, herezja 0→1 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_COST_PLUS2` | CAA-03 (Cień na Rynku): cost 0 → 2 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_COST_PLUS1` | CAA-06 (Ucieczka z Lochów): cost 0 → 1 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_C1_H0` | CAA-06 (Ucieczka z Lochów): koszt 0→1, herezja 0→0 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_COST_PLUS2` | GC-02 (Czarny Rynek): cost 0 → 2 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_HERESY_PLUS2` | GC-02 (Czarny Rynek): heresy 0 → 2 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_HERESY_SET2` | GC-02 (Czarny Rynek): dodaj heresy = 2 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_G1_H1` | GC-02 (Czarny Rynek): złoto 2→1, herezja 0→1 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-03_HERESY_MINUS2` | GC-03 (Podrzucenie Księgi): heresy 2 → 0 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-11_C0_G1` | GC-11 (Fałszywe Świadectwo Cechu): koszt 0→0, złoto 0→1 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_COST_PLUS1` | KB-08 (Przekupstwo Sędziego): cost 3 → 4 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_C4_G2` | KB-08 (Przekupstwo Sędziego): koszt 3→4, złoto 0→2 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-04_HERESY_PLUS2` | KT-04 (Zwierciadło Herezji): heresy 0 → 2 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-04_HERESY_SET2` | KT-04 (Zwierciadło Herezji): dodaj heresy = 2 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_HERESY_MINUS1` | SO-01 (Patrol Familiariuszy): heresy 2 → 1 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_C2_G4` | SO-02 (Skarbiec Trybunału): koszt 1→2, złoto 2→4 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_G1_H1` | SO-02 (Skarbiec Trybunału): złoto 2→1, herezja 2→1 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_COST_PLUS1` | SO-09 (Świadek Koronny): cost 1 → 2 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_C2_G2` | SO-09 (Świadek Koronny): koszt 1→2, złoto 0→2 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_C6_G1` | SO-10 (Oczyść Miasto): koszt 5→6, złoto 0→1 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-12_C2_H3` | SO-12 (Straż Trybunalska): koszt 1→2, herezja 2→3 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-12_G2_H1` | SO-12 (Straż Trybunalska): złoto 1→2, herezja 2→1 | 93.6 → 🟢 ** 92.7** (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.7 (`🔻 -0.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_HERESY_PLUS1` | CAA-02 (Złoto z Kryjówki): heresy 0 → 1 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_HERESY_PLUS2` | CAA-02 (Złoto z Kryjówki): heresy 0 → 2 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_HERESY_SET1` | CAA-02 (Złoto z Kryjówki): dodaj heresy = 1 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_HERESY_SET2` | CAA-02 (Złoto z Kryjówki): dodaj heresy = 2 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_C0_H1` | CAA-02 (Złoto z Kryjówki): koszt 0→0, herezja 0→1 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_HERESY_PLUS2` | CAA-08 (Kaptur Nocy): heresy 0 → 2 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_HERESY_SET2` | CAA-08 (Kaptur Nocy): dodaj heresy = 2 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-11_COST_MINUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 0 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-11_C0_H0` | CAA-11 (Nocna Zmiana Warty): koszt 1→0, herezja 0→0 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-11_C2_G3` | CAA-11 (Nocna Zmiana Warty): koszt 1→2, złoto 1→3 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-11_G2_H0` | CAA-11 (Nocna Zmiana Warty): złoto 1→2, herezja 0→0 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-12_C2_G6` | CAA-12 (Skrytka w Murach): koszt 1→2, złoto 4→6 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_C0_H2` | GC-01 (Przekupiony Strażnik): koszt 1→0, herezja 1→2 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-03_C0_G1` | GC-03 (Podrzucenie Księgi): koszt 1→0, złoto 0→1 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_C1_G5` | GC-07 (Skrytobójstwo): koszt 0→1, złoto 3→5 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_HERESY_MINUS1` | GC-08 (Zatrute Złoto): heresy 2 → 1 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_C4_H3` | KB-08 (Przekupstwo Sędziego): koszt 3→4, herezja 2→3 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_G1_H0` | KT-10 (Pieczęć Salomona): złoto 0→1, herezja 0→0 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_HERESY_PLUS2` | SO-01 (Patrol Familiariuszy): heresy 2 → 4 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_COST_PLUS1` | SO-06 (Areszt Trybunalski): cost 2 → 3 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_C3_H0` | SO-06 (Areszt Trybunalski): koszt 2→3, herezja 0→0 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_COST_PLUS1` | SO-10 (Oczyść Miasto): cost 5 → 6 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-12_C0_H3` | SO-12 (Straż Trybunalska): koszt 1→0, herezja 2→3 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-12_G2_H3` | SO-12 (Straż Trybunalska): złoto 1→2, herezja 2→3 | 93.6 → 🟢 ** 92.6** (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.6 (`🔻 -1.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_COST_MINUS2` | CAA-08 (Kaptur Nocy): cost 2 → 0 | 93.6 → 🟢 ** 92.5** (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.5 (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_C1_G3` | CAA-08 (Kaptur Nocy): koszt 2→1, złoto 2→3 | 93.6 → 🟢 ** 92.5** (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.5 (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_C0_G3` | GC-02 (Czarny Rynek): koszt 0→0, złoto 2→3 | 93.6 → 🟢 ** 92.5** (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.5 (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_G3_H0` | GC-02 (Czarny Rynek): złoto 2→3, herezja 0→0 | 93.6 → 🟢 ** 92.5** (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.5 (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_C5_G2` | GC-10 (Upadek Domu): koszt 4→5, złoto 0→2 | 93.6 → 🟢 ** 92.5** (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.5 (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_HERESY_PLUS2` | KB-08 (Przekupstwo Sędziego): heresy 2 → 4 | 93.6 → 🟢 ** 92.5** (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.5 (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_HERESY_MINUS2` | KB-08 (Przekupstwo Sędziego): heresy 2 → 0 | 93.6 → 🟢 ** 92.5** (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.5 (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-04_C2_H1` | KT-04 (Zwierciadło Herezji): koszt 1→2, herezja 0→1 | 93.6 → 🟢 ** 92.5** (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.5 (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_HERESY_PLUS2` | KT-07 (Archiwum Ukryte): heresy 0 → 2 | 93.6 → 🟢 ** 92.5** (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.5 (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_HERESY_SET2` | KT-07 (Archiwum Ukryte): dodaj heresy = 2 | 93.6 → 🟢 ** 92.5** (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.5 (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_C2_G1` | KT-08 (Areszt Wiedzy): koszt 1→2, złoto 0→1 | 93.6 → 🟢 ** 92.5** (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.5 (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-11_C3_G3` | KT-11 (Medytacja Sefirot): koszt 2→3, złoto 1→3 | 93.6 → 🟢 ** 92.5** (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.5 (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_COST_MINUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 0 | 93.6 → 🟢 ** 92.5** (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.5 (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_C6_G2` | SO-10 (Oczyść Miasto): koszt 5→6, złoto 0→2 | 93.6 → 🟢 ** 92.5** (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.5 (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-12_COST_PLUS1` | SO-12 (Straż Trybunalska): cost 1 → 2 | 93.6 → 🟢 ** 92.5** (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.5 (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-12_C0_G2` | SO-12 (Straż Trybunalska): koszt 1→0, złoto 1→2 | 93.6 → 🟢 ** 92.5** (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.5 (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-12_G0_H1` | SO-12 (Straż Trybunalska): złoto 1→0, herezja 2→1 | 93.6 → 🟢 ** 92.5** (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.5 (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-12_G0_H3` | SO-12 (Straż Trybunalska): złoto 1→0, herezja 2→3 | 93.6 → 🟢 ** 92.5** (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.5 (`🔻 -1.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-11_COST_PLUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 2 | 93.6 → 🟢 ** 92.4** (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.4 (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-11_C2_H0` | CAA-11 (Nocna Zmiana Warty): koszt 1→2, herezja 0→0 | 93.6 → 🟢 ** 92.4** (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.4 (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-11_G0_H0` | CAA-11 (Nocna Zmiana Warty): złoto 1→0, herezja 0→0 | 93.6 → 🟢 ** 92.4** (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.4 (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-03_C2_H1` | GC-03 (Podrzucenie Księgi): koszt 1→2, herezja 2→1 | 93.6 → 🟢 ** 92.4** (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.4 (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_COST_PLUS1` | GC-07 (Skrytobójstwo): cost 0 → 1 | 93.6 → 🟢 ** 92.4** (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.4 (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_C1_H0` | GC-07 (Skrytobójstwo): koszt 0→1, herezja 0→0 | 93.6 → 🟢 ** 92.4** (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.4 (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-11_C1_G2` | GC-11 (Fałszywe Świadectwo Cechu): koszt 0→1, złoto 0→2 | 93.6 → 🟢 ** 92.4** (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.4 (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-12_HERESY_MINUS1` | GC-12 (Złodziejski Zwiad): heresy 2 → 1 | 93.6 → 🟢 ** 92.4** (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.4 (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-12_C0_H1` | GC-12 (Złodziejski Zwiad): koszt 0→0, herezja 2→1 | 93.6 → 🟢 ** 92.4** (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.4 (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_C3_G1` | KT-06 (Przesłuchanie Imienia): koszt 2→3, złoto 0→1 | 93.6 → 🟢 ** 92.4** (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.4 (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_C2_H1` | SO-02 (Skarbiec Trybunału): koszt 1→2, herezja 2→1 | 93.6 → 🟢 ** 92.4** (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.4 (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_HERESY_MINUS1` | SO-03 (Podejrzenie): heresy 4 → 3 | 93.6 → 🟢 ** 92.4** (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.4 (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_G0_H3` | SO-03 (Podejrzenie): złoto 0→0, herezja 4→3 | 93.6 → 🟢 ** 92.4** (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.4 (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_C0_G3` | SO-04 (Publiczne Ostrzeżenie): koszt 1→0, złoto 1→3 | 93.6 → 🟢 ** 92.4** (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.4 (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_C3_G1` | SO-06 (Areszt Trybunalski): koszt 2→3, złoto 0→1 | 93.6 → 🟢 ** 92.4** (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.4 (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_COST_MINUS1` | SO-09 (Świadek Koronny): cost 1 → 0 | 93.6 → 🟢 ** 92.4** (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.4 (`🔻 -1.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_HERESY_MINUS1` | GC-01 (Przekupiony Strażnik): heresy 1 → 0 | 93.6 → 🟢 ** 92.3** (`🔻 -1.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.3 (`🔻 -1.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_C0_G2` | GC-04 (Informator): koszt 1→0, złoto 0→2 | 93.6 → 🟢 ** 92.3** (`🔻 -1.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.3 (`🔻 -1.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_COST_MINUS1` | KT-01 (Rytuał Przejścia): cost 1 → 0 | 93.6 → 🟢 ** 92.3** (`🔻 -1.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.3 (`🔻 -1.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_HERESY_MINUS1` | KT-01 (Rytuał Przejścia): heresy 1 → 0 | 93.6 → 🟢 ** 92.3** (`🔻 -1.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.3 (`🔻 -1.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_C2_G3` | SO-02 (Skarbiec Trybunału): koszt 1→2, złoto 2→3 | 93.6 → 🟢 ** 92.3** (`🔻 -1.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.3 (`🔻 -1.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_HERESY_PLUS1` | CAA-08 (Kaptur Nocy): heresy 0 → 1 | 93.6 → 🟢 ** 92.2** (`🔻 -1.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.2 (`🔻 -1.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_HERESY_SET1` | CAA-08 (Kaptur Nocy): dodaj heresy = 1 | 93.6 → 🟢 ** 92.2** (`🔻 -1.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.2 (`🔻 -1.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_G2_H2` | GC-01 (Przekupiony Strażnik): złoto 1→2, herezja 1→2 | 93.6 → 🟢 ** 92.2** (`🔻 -1.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.2 (`🔻 -1.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_C3_G2` | SO-03 (Podejrzenie): koszt 2→3, złoto 0→2 | 93.6 → 🟢 ** 92.2** (`🔻 -1.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.2 (`🔻 -1.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_C1_H1` | SO-08 (Nasłanie Inkwizytora): koszt 0→1, herezja 0→1 | 93.6 → 🟢 ** 92.2** (`🔻 -1.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.2 (`🔻 -1.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_G2_H1` | SO-08 (Nasłanie Inkwizytora): złoto 3→2, herezja 0→1 | 93.6 → 🟢 ** 92.2** (`🔻 -1.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.2 (`🔻 -1.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_COST_PLUS2` | SO-09 (Świadek Koronny): cost 1 → 3 | 93.6 → 🟢 ** 92.2** (`🔻 -1.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.2 (`🔻 -1.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_C0_H0` | SO-09 (Świadek Koronny): koszt 1→0, herezja 1→0 | 93.6 → 🟢 ** 92.2** (`🔻 -1.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.2 (`🔻 -1.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_C0_G4` | CAA-04 (Fałszywy Trop): koszt 0→0, złoto 3→4 | 93.6 → 🟢 ** 92.1** (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.1 (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_G4_H0` | CAA-04 (Fałszywy Trop): złoto 3→4, herezja 0→0 | 93.6 → 🟢 ** 92.1** (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.1 (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_C1_G4` | GC-02 (Czarny Rynek): koszt 0→1, złoto 2→4 | 93.6 → 🟢 ** 92.1** (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.1 (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_C4_G1` | GC-06 (Szantaż): koszt 3→4, złoto 0→1 | 93.6 → 🟢 ** 92.1** (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.1 (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_C2_G3` | KT-01 (Rytuał Przejścia): koszt 1→2, złoto 1→3 | 93.6 → 🟢 ** 92.1** (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.1 (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_COST_PLUS1` | KT-07 (Archiwum Ukryte): cost 1 → 2 | 93.6 → 🟢 ** 92.1** (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.1 (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_C2_H0` | KT-07 (Archiwum Ukryte): koszt 1→2, herezja 0→0 | 93.6 → 🟢 ** 92.1** (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.1 (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_HERESY_PLUS1` | SO-08 (Nasłanie Inkwizytora): heresy 0 → 1 | 93.6 → 🟢 ** 92.1** (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.1 (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_HERESY_SET1` | SO-08 (Nasłanie Inkwizytora): dodaj heresy = 1 | 93.6 → 🟢 ** 92.1** (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.1 (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_C0_H1` | SO-08 (Nasłanie Inkwizytora): koszt 0→0, herezja 0→1 | 93.6 → 🟢 ** 92.1** (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.1 (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_C2_H2` | SO-09 (Świadek Koronny): koszt 1→2, herezja 1→2 | 93.6 → 🟢 ** 92.1** (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.1 (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-12_HERESY_MINUS1` | SO-12 (Straż Trybunalska): heresy 2 → 1 | 93.6 → 🟢 ** 92.1** (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.1 (`🔻 -1.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_C1_H1` | CAA-04 (Fałszywy Trop): koszt 0→1, herezja 0→1 | 93.6 → 🟢 ** 92.0** (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.0 (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_C0_G5` | CAA-04 (Fałszywy Trop): koszt 0→0, złoto 3→5 | 93.6 → 🟢 ** 92.0** (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.0 (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_C1_G5` | CAA-04 (Fałszywy Trop): koszt 0→1, złoto 3→5 | 93.6 → 🟢 ** 92.0** (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.0 (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_G2_H1` | CAA-04 (Fałszywy Trop): złoto 3→2, herezja 0→1 | 93.6 → 🟢 ** 92.0** (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.0 (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_COST_PLUS1` | CAA-10 (Echo Alhambry): cost 2 → 3 | 93.6 → 🟢 ** 92.0** (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.0 (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_C3_H0` | CAA-10 (Echo Alhambry): koszt 2→3, herezja 0→0 | 93.6 → 🟢 ** 92.0** (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.0 (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-03_HERESY_MINUS1` | GC-03 (Podrzucenie Księgi): heresy 2 → 1 | 93.6 → 🟢 ** 92.0** (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.0 (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-03_G0_H1` | GC-03 (Podrzucenie Księgi): złoto 0→0, herezja 2→1 | 93.6 → 🟢 ** 92.0** (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.0 (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_COST_MINUS1` | KB-06 (Areszt Królewski): cost 2 → 1 | 93.6 → 🟢 ** 92.0** (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.0 (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_C1_H0` | KB-06 (Areszt Królewski): koszt 2→1, herezja 0→0 | 93.6 → 🟢 ** 92.0** (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.0 (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_COST_PLUS2` | KT-07 (Archiwum Ukryte): cost 1 → 3 | 93.6 → 🟢 ** 92.0** (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.0 (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_C2_H3` | SO-02 (Skarbiec Trybunału): koszt 1→2, herezja 2→3 | 93.6 → 🟢 ** 92.0** (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.0 (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_G0_H0` | SO-04 (Publiczne Ostrzeżenie): złoto 1→0, herezja 0→0 | 93.6 → 🟢 ** 92.0** (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.0 (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_G1_H0` | SO-10 (Oczyść Miasto): złoto 0→1, herezja 1→0 | 93.6 → 🟢 ** 92.0** (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.0 (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-12_C0_G3` | SO-12 (Straż Trybunalska): koszt 1→0, złoto 1→3 | 93.6 → 🟢 ** 92.0** (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 92.0 (`🔻 -1.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_C2_G1` | GC-06 (Szantaż): koszt 3→2, złoto 0→1 | 93.6 → 🟢 ** 91.9** (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.9 (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_COST_MINUS1` | GC-08 (Zatrute Złoto): cost 1 → 0 | 93.6 → 🟢 ** 91.9** (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.9 (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-11_C0_G2` | GC-11 (Fałszywe Świadectwo Cechu): koszt 0→0, złoto 0→2 | 93.6 → 🟢 ** 91.9** (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.9 (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_C2_H1` | KB-08 (Przekupstwo Sędziego): koszt 3→2, herezja 2→1 | 93.6 → 🟢 ** 91.9** (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.9 (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_G3_H2` | KB-10 (Pieczęć Korony): złoto 2→3, herezja 1→2 | 93.6 → 🟢 ** 91.9** (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.9 (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_C0_G2` | KT-01 (Rytuał Przejścia): koszt 1→0, złoto 1→2 | 93.6 → 🟢 ** 91.9** (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.9 (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-12_COST_PLUS1` | KT-12 (Strażnik Archiwum): cost 1 → 2 | 93.6 → 🟢 ** 91.9** (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.9 (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-12_C2_H0` | KT-12 (Strażnik Archiwum): koszt 1→2, herezja 0→0 | 93.6 → 🟢 ** 91.9** (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.9 (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_C0_H1` | SO-01 (Patrol Familiariuszy): koszt 1→0, herezja 2→1 | 93.6 → 🟢 ** 91.9** (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.9 (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_G3_H1` | SO-01 (Patrol Familiariuszy): złoto 2→3, herezja 2→1 | 93.6 → 🟢 ** 91.9** (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.9 (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_G3_H3` | SO-01 (Patrol Familiariuszy): złoto 2→3, herezja 2→3 | 93.6 → 🟢 ** 91.9** (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.9 (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_COST_MINUS2` | SO-03 (Podejrzenie): cost 2 → 0 | 93.6 → 🟢 ** 91.9** (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.9 (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_COST_PLUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 2 | 93.6 → 🟢 ** 91.9** (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.9 (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_C2_H0` | SO-04 (Publiczne Ostrzeżenie): koszt 1→2, herezja 0→0 | 93.6 → 🟢 ** 91.9** (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.9 (`🔻 -1.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_HERESY_PLUS2` | CAA-07 (Szantaż Bractwa): heresy 0 → 2 | 93.6 → 🟢 ** 91.8** (`🔻 -1.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.8 (`🔻 -1.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_HERESY_SET2` | CAA-07 (Szantaż Bractwa): dodaj heresy = 2 | 93.6 → 🟢 ** 91.8** (`🔻 -1.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.8 (`🔻 -1.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_C2_H0` | GC-04 (Informator): koszt 1→2, herezja 1→0 | 93.6 → 🟢 ** 91.8** (`🔻 -1.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.8 (`🔻 -1.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_C0_H2` | KB-01 (Rozkaz Dworu): koszt 1→0, herezja 1→2 | 93.6 → 🟢 ** 91.8** (`🔻 -1.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.8 (`🔻 -1.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_G1_H1` | KT-10 (Pieczęć Salomona): złoto 0→1, herezja 0→1 | 93.6 → 🟢 ** 91.8** (`🔻 -1.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.8 (`🔻 -1.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 93.6 → 🟢 ** 91.8** (`🔻 -1.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.8 (`🔻 -1.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_HERESY_PLUS1` | CAA-07 (Szantaż Bractwa): heresy 0 → 1 | 93.6 → 🟢 ** 91.7** (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.7 (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_HERESY_SET1` | CAA-07 (Szantaż Bractwa): dodaj heresy = 1 | 93.6 → 🟢 ** 91.7** (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.7 (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_C0_H1` | CAA-07 (Szantaż Bractwa): koszt 0→0, herezja 0→1 | 93.6 → 🟢 ** 91.7** (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.7 (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_C1_G4` | CAA-08 (Kaptur Nocy): koszt 2→1, złoto 2→4 | 93.6 → 🟢 ** 91.7** (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.7 (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_C2_H0` | GC-01 (Przekupiony Strażnik): koszt 1→2, herezja 1→0 | 93.6 → 🟢 ** 91.7** (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.7 (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_C2_G2` | GC-06 (Szantaż): koszt 3→2, złoto 0→2 | 93.6 → 🟢 ** 91.7** (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.7 (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_C2_G3` | GC-08 (Zatrute Złoto): koszt 1→2, złoto 1→3 | 93.6 → 🟢 ** 91.7** (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.7 (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_C5_G1` | GC-10 (Upadek Domu): koszt 4→5, złoto 0→1 | 93.6 → 🟢 ** 91.7** (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.7 (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_C3_G1` | KB-07 (Szantaż Pieczęcią): koszt 2→3, złoto 0→1 | 93.6 → 🟢 ** 91.7** (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.7 (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_C2_H0` | KT-05 (Wskazówka Cyklu): koszt 1→2, herezja 1→0 | 93.6 → 🟢 ** 91.7** (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.7 (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_HERESY_MINUS2` | SO-01 (Patrol Familiariuszy): heresy 2 → 0 | 93.6 → 🟢 ** 91.7** (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.7 (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_C3_H3` | SO-03 (Podejrzenie): koszt 2→3, herezja 4→3 | 93.6 → 🟢 ** 91.7** (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.7 (`🔻 -1.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_HERESY_MINUS1` | GC-06 (Szantaż): heresy 1 → 0 | 93.6 → 🟢 ** 91.6** (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.6 (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_G0_H0` | GC-06 (Szantaż): złoto 0→0, herezja 1→0 | 93.6 → 🟢 ** 91.6** (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.6 (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_C0_H1` | GC-09 (Lista Dłużników): koszt 1→0, herezja 0→1 | 93.6 → 🟢 ** 91.6** (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.6 (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-12_HERESY_PLUS1` | GC-12 (Złodziejski Zwiad): heresy 2 → 3 | 93.6 → 🟢 ** 91.6** (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.6 (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-12_C0_H3` | GC-12 (Złodziejski Zwiad): koszt 0→0, herezja 2→3 | 93.6 → 🟢 ** 91.6** (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.6 (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_HERESY_PLUS1` | KB-03 (Plotka Dworska): heresy 1 → 2 | 93.6 → 🟢 ** 91.6** (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.6 (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_G0_H2` | KB-03 (Plotka Dworska): złoto 0→0, herezja 1→2 | 93.6 → 🟢 ** 91.6** (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.6 (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_COST_PLUS2` | KB-07 (Szantaż Pieczęcią): cost 2 → 4 | 93.6 → 🟢 ** 91.6** (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.6 (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_HERESY_PLUS1` | KB-07 (Szantaż Pieczęcią): heresy 0 → 1 | 93.6 → 🟢 ** 91.6** (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.6 (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_HERESY_SET1` | KB-07 (Szantaż Pieczęcią): dodaj heresy = 1 | 93.6 → 🟢 ** 91.6** (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.6 (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_G0_H1` | KB-07 (Szantaż Pieczęcią): złoto 0→0, herezja 0→1 | 93.6 → 🟢 ** 91.6** (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.6 (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_COST_MINUS1` | KB-08 (Przekupstwo Sędziego): cost 3 → 2 | 93.6 → 🟢 ** 91.6** (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.6 (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_C2_H1` | KT-07 (Archiwum Ukryte): koszt 1→2, herezja 0→1 | 93.6 → 🟢 ** 91.6** (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.6 (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_G1_H1` | KT-07 (Archiwum Ukryte): złoto 0→1, herezja 0→1 | 93.6 → 🟢 ** 91.6** (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.6 (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_HERESY_PLUS1` | KT-10 (Pieczęć Salomona): heresy 0 → 1 | 93.6 → 🟢 ** 91.6** (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.6 (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_HERESY_SET1` | KT-10 (Pieczęć Salomona): dodaj heresy = 1 | 93.6 → 🟢 ** 91.6** (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.6 (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_G0_H1` | KT-10 (Pieczęć Salomona): złoto 0→0, herezja 0→1 | 93.6 → 🟢 ** 91.6** (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.6 (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_C1_G1` | SO-03 (Podejrzenie): koszt 2→1, złoto 0→1 | 93.6 → 🟢 ** 91.6** (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.6 (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-11_C2_H0` | SO-11 (Dekret Czystości Wiary): koszt 1→2, herezja 1→0 | 93.6 → 🟢 ** 91.6** (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.6 (`🔻 -2.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-11_C0_G2` | CAA-11 (Nocna Zmiana Warty): koszt 1→0, złoto 1→2 | 93.6 → 🟢 ** 91.5** (`🔻 -2.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.5 (`🔻 -2.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_COST_MINUS2` | GC-06 (Szantaż): cost 3 → 1 | 93.6 → 🟢 ** 91.5** (`🔻 -2.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.5 (`🔻 -2.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_C2_H1` | GC-09 (Lista Dłużników): koszt 1→2, herezja 0→1 | 93.6 → 🟢 ** 91.5** (`🔻 -2.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.5 (`🔻 -2.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_COST_PLUS1` | KB-02 (Pobór Podatków): cost 1 → 2 | 93.6 → 🟢 ** 91.5** (`🔻 -2.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.5 (`🔻 -2.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_C2_H0` | KB-02 (Pobór Podatków): koszt 1→2, herezja 0→0 | 93.6 → 🟢 ** 91.5** (`🔻 -2.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.5 (`🔻 -2.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_COST_PLUS2` | KB-05 (List Żelazny): cost 2 → 4 | 93.6 → 🟢 ** 91.5** (`🔻 -2.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.5 (`🔻 -2.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_COST_PLUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 3 | 93.6 → 🟢 ** 91.5** (`🔻 -2.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.5 (`🔻 -2.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_C3_H0` | KT-06 (Przesłuchanie Imienia): koszt 2→3, herezja 0→0 | 93.6 → 🟢 ** 91.5** (`🔻 -2.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.5 (`🔻 -2.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_G1_H1` | KT-06 (Przesłuchanie Imienia): złoto 0→1, herezja 0→1 | 93.6 → 🟢 ** 91.5** (`🔻 -2.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.5 (`🔻 -2.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_C0_H1` | KT-07 (Archiwum Ukryte): koszt 1→0, herezja 0→1 | 93.6 → 🟢 ** 91.5** (`🔻 -2.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.5 (`🔻 -2.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-11_HERESY_PLUS1` | CAA-11 (Nocna Zmiana Warty): heresy 0 → 1 | 93.6 → 🟢 ** 91.4** (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.4 (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-11_HERESY_SET1` | CAA-11 (Nocna Zmiana Warty): dodaj heresy = 1 | 93.6 → 🟢 ** 91.4** (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.4 (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-11_C0_G3` | CAA-11 (Nocna Zmiana Warty): koszt 1→0, złoto 1→3 | 93.6 → 🟢 ** 91.4** (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.4 (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-11_HERESY_MINUS1` | GC-11 (Fałszywe Świadectwo Cechu): heresy 2 → 1 | 93.6 → 🟢 ** 91.4** (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.4 (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-11_C0_H1` | GC-11 (Fałszywe Świadectwo Cechu): koszt 0→0, herezja 2→1 | 93.6 → 🟢 ** 91.4** (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.4 (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-11_G0_H1` | GC-11 (Fałszywe Świadectwo Cechu): złoto 0→0, herezja 2→1 | 93.6 → 🟢 ** 91.4** (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.4 (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-11_G1_H3` | GC-11 (Fałszywe Świadectwo Cechu): złoto 0→1, herezja 2→3 | 93.6 → 🟢 ** 91.4** (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.4 (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_HERESY_PLUS2` | KB-03 (Plotka Dworska): heresy 1 → 3 | 93.6 → 🟢 ** 91.4** (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.4 (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_G1_H0` | KT-07 (Archiwum Ukryte): złoto 0→1, herezja 0→0 | 93.6 → 🟢 ** 91.4** (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.4 (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_COST_PLUS1` | SO-03 (Podejrzenie): cost 2 → 3 | 93.6 → 🟢 ** 91.4** (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.4 (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_C1_G2` | SO-03 (Podejrzenie): koszt 2→1, złoto 0→2 | 93.6 → 🟢 ** 91.4** (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.4 (`🔻 -2.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_C0_G4` | CAA-02 (Złoto z Kryjówki): koszt 0→0, złoto 3→4 | 93.6 → 🟢 ** 91.3** (`🔻 -2.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.3 (`🔻 -2.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_C1_G5` | CAA-02 (Złoto z Kryjówki): koszt 0→1, złoto 3→5 | 93.6 → 🟢 ** 91.3** (`🔻 -2.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.3 (`🔻 -2.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_G4_H0` | CAA-02 (Złoto z Kryjówki): złoto 3→4, herezja 0→0 | 93.6 → 🟢 ** 91.3** (`🔻 -2.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.3 (`🔻 -2.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_G0_H0` | GC-01 (Przekupiony Strażnik): złoto 1→0, herezja 1→0 | 93.6 → 🟢 ** 91.3** (`🔻 -2.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.3 (`🔻 -2.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-12_C1_H1` | GC-12 (Złodziejski Zwiad): koszt 0→1, herezja 2→1 | 93.6 → 🟢 ** 91.3** (`🔻 -2.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.3 (`🔻 -2.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_C0_H1` | KB-02 (Pobór Podatków): koszt 1→0, herezja 0→1 | 93.6 → 🟢 ** 91.3** (`🔻 -2.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.3 (`🔻 -2.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_C0_H3` | SO-01 (Patrol Familiariuszy): koszt 1→0, herezja 2→3 | 93.6 → 🟢 ** 91.3** (`🔻 -2.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.3 (`🔻 -2.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_C0_G3` | SO-02 (Skarbiec Trybunału): koszt 1→0, złoto 2→3 | 93.6 → 🟢 ** 91.3** (`🔻 -2.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.3 (`🔻 -2.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-11_G0_H0` | SO-11 (Dekret Czystości Wiary): złoto 1→0, herezja 1→0 | 93.6 → 🟢 ** 91.3** (`🔻 -2.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.3 (`🔻 -2.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-03_C0_H1` | GC-03 (Podrzucenie Księgi): koszt 1→0, herezja 2→1 | 93.6 → 🟢 ** 91.2** (`🔻 -2.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.2 (`🔻 -2.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-12_G0_H1` | GC-12 (Złodziejski Zwiad): złoto 1→0, herezja 2→1 | 93.6 → 🟢 ** 91.2** (`🔻 -2.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.2 (`🔻 -2.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_C2_H0` | KB-03 (Plotka Dworska): koszt 1→2, herezja 1→0 | 93.6 → 🟢 ** 91.2** (`🔻 -2.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.2 (`🔻 -2.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_HERESY_PLUS1` | KB-04 (Faworyt Dworu): heresy 0 → 1 | 93.6 → 🟢 ** 91.2** (`🔻 -2.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.2 (`🔻 -2.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_HERESY_SET1` | KB-04 (Faworyt Dworu): dodaj heresy = 1 | 93.6 → 🟢 ** 91.2** (`🔻 -2.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.2 (`🔻 -2.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_G0_H1` | KB-04 (Faworyt Dworu): złoto 0→0, herezja 0→1 | 93.6 → 🟢 ** 91.2** (`🔻 -2.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.2 (`🔻 -2.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_COST_PLUS2` | KT-06 (Przesłuchanie Imienia): cost 2 → 4 | 93.6 → 🟢 ** 91.2** (`🔻 -2.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.2 (`🔻 -2.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_HERESY_MINUS2` | SO-02 (Skarbiec Trybunału): heresy 2 → 0 | 93.6 → 🟢 ** 91.2** (`🔻 -2.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.2 (`🔻 -2.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_G1_H0` | SO-09 (Świadek Koronny): złoto 0→1, herezja 1→0 | 93.6 → 🟢 ** 91.2** (`🔻 -2.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.2 (`🔻 -2.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-11_HERESY_MINUS1` | SO-11 (Dekret Czystości Wiary): heresy 1 → 0 | 93.6 → 🟢 ** 91.2** (`🔻 -2.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.2 (`🔻 -2.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-03_G1_H1` | GC-03 (Podrzucenie Księgi): złoto 0→1, herezja 2→1 | 93.6 → 🟢 ** 91.1** (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.1 (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_HERESY_PLUS1` | GC-09 (Lista Dłużników): heresy 0 → 1 | 93.6 → 🟢 ** 91.1** (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.1 (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_HERESY_SET1` | GC-09 (Lista Dłużników): dodaj heresy = 1 | 93.6 → 🟢 ** 91.1** (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.1 (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_G0_H1` | GC-09 (Lista Dłużników): złoto 0→0, herezja 0→1 | 93.6 → 🟢 ** 91.1** (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.1 (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_HERESY_PLUS1` | KT-06 (Przesłuchanie Imienia): heresy 0 → 1 | 93.6 → 🟢 ** 91.1** (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.1 (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_HERESY_SET1` | KT-06 (Przesłuchanie Imienia): dodaj heresy = 1 | 93.6 → 🟢 ** 91.1** (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.1 (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_G0_H1` | KT-06 (Przesłuchanie Imienia): złoto 0→0, herezja 0→1 | 93.6 → 🟢 ** 91.1** (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.1 (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-11_G0_H0` | KT-11 (Medytacja Sefirot): złoto 1→0, herezja 0→0 | 93.6 → 🟢 ** 91.1** (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.1 (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-12_HERESY_PLUS2` | KT-12 (Strażnik Archiwum): heresy 0 → 2 | 93.6 → 🟢 ** 91.1** (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.1 (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-12_HERESY_SET2` | KT-12 (Strażnik Archiwum): dodaj heresy = 2 | 93.6 → 🟢 ** 91.1** (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.1 (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_C4_G2` | SO-10 (Oczyść Miasto): koszt 5→4, złoto 0→2 | 93.6 → 🟢 ** 91.1** (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.1 (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-11_G2_H0` | SO-11 (Dekret Czystości Wiary): złoto 1→2, herezja 1→0 | 93.6 → 🟢 ** 91.1** (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.1 (`🔻 -2.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-03_C0_G2` | GC-03 (Podrzucenie Księgi): koszt 1→0, złoto 0→2 | 93.6 → 🟢 ** 91.0** (`🔻 -2.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.0 (`🔻 -2.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-12_G2_H3` | GC-12 (Złodziejski Zwiad): złoto 1→2, herezja 2→3 | 93.6 → 🟢 ** 91.0** (`🔻 -2.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.0 (`🔻 -2.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_C1_H1` | KT-06 (Przesłuchanie Imienia): koszt 2→1, herezja 0→1 | 93.6 → 🟢 ** 91.0** (`🔻 -2.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.0 (`🔻 -2.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_C2_G2` | KT-07 (Archiwum Ukryte): koszt 1→2, złoto 0→2 | 93.6 → 🟢 ** 91.0** (`🔻 -2.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.0 (`🔻 -2.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_C3_H5` | SO-03 (Podejrzenie): koszt 2→3, herezja 4→5 | 93.6 → 🟢 ** 91.0** (`🔻 -2.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.0 (`🔻 -2.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_C4_H0` | SO-10 (Oczyść Miasto): koszt 5→4, herezja 1→0 | 93.6 → 🟢 ** 91.0** (`🔻 -2.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 91.0 (`🔻 -2.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_G3_H1` | GC-02 (Czarny Rynek): złoto 2→3, herezja 0→1 | 93.6 → 🟢 ** 90.9** (`🔻 -2.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.9 (`🔻 -2.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_COST_PLUS1` | GC-06 (Szantaż): cost 3 → 4 | 93.6 → 🟢 ** 90.9** (`🔻 -2.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.9 (`🔻 -2.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_G1_H1` | GC-09 (Lista Dłużników): złoto 0→1, herezja 0→1 | 93.6 → 🟢 ** 90.9** (`🔻 -2.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.9 (`🔻 -2.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_C2_G1` | KB-08 (Przekupstwo Sędziego): koszt 3→2, złoto 0→1 | 93.6 → 🟢 ** 90.9** (`🔻 -2.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.9 (`🔻 -2.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_C3_H1` | KT-06 (Przesłuchanie Imienia): koszt 2→3, herezja 0→1 | 93.6 → 🟢 ** 90.9** (`🔻 -2.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.9 (`🔻 -2.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_COST_PLUS2` | SO-03 (Podejrzenie): cost 2 → 4 | 93.6 → 🟢 ** 90.9** (`🔻 -2.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.9 (`🔻 -2.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_G1_H3` | SO-03 (Podejrzenie): złoto 0→1, herezja 4→3 | 93.6 → 🟢 ** 90.9** (`🔻 -2.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.9 (`🔻 -2.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_HERESY_PLUS1` | KB-10 (Pieczęć Korony): heresy 1 → 2 | 93.6 → 🟢 ** 90.8** (`🔻 -2.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.8 (`🔻 -2.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_C1_H1` | KT-03 (Zakazana Wiedza): koszt 0→1, herezja 2→1 | 93.6 → 🟢 ** 90.8** (`🔻 -2.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.8 (`🔻 -2.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_HERESY_MINUS1` | SO-02 (Skarbiec Trybunału): heresy 2 → 1 | 93.6 → 🟢 ** 90.8** (`🔻 -2.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.8 (`🔻 -2.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-11_C0_H0` | SO-11 (Dekret Czystości Wiary): koszt 1→0, herezja 1→0 | 93.6 → 🟢 ** 90.8** (`🔻 -2.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.8 (`🔻 -2.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_G1_H2` | KB-01 (Rozkaz Dworu): złoto 0→1, herezja 1→2 | 93.6 → 🟢 ** 90.7** (`🔻 -2.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.7 (`🔻 -2.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_COST_MINUS1` | KT-07 (Archiwum Ukryte): cost 1 → 0 | 93.6 → 🟢 ** 90.7** (`🔻 -2.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.7 (`🔻 -2.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_C0_H0` | KT-07 (Archiwum Ukryte): koszt 1→0, herezja 0→0 | 93.6 → 🟢 ** 90.7** (`🔻 -2.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.7 (`🔻 -2.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-11_C3_G2` | KT-11 (Medytacja Sefirot): koszt 2→3, złoto 1→2 | 93.6 → 🟢 ** 90.7** (`🔻 -2.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.7 (`🔻 -2.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-12_G1_H1` | KT-12 (Strażnik Archiwum): złoto 0→1, herezja 0→1 | 93.6 → 🟢 ** 90.7** (`🔻 -2.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.7 (`🔻 -2.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_HERESY_PLUS2` | SO-08 (Nasłanie Inkwizytora): heresy 0 → 2 | 93.6 → 🟢 ** 90.7** (`🔻 -2.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.7 (`🔻 -2.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_HERESY_SET2` | SO-08 (Nasłanie Inkwizytora): dodaj heresy = 2 | 93.6 → 🟢 ** 90.7** (`🔻 -2.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.7 (`🔻 -2.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_C0_H0` | GC-01 (Przekupiony Strażnik): koszt 1→0, herezja 1→0 | 93.6 → 🟢 ** 90.6** (`🔻 -3.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.6 (`🔻 -3.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_G2_H0` | GC-01 (Przekupiony Strażnik): złoto 1→2, herezja 1→0 | 93.6 → 🟢 ** 90.6** (`🔻 -3.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.6 (`🔻 -3.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_C3_H1` | KB-07 (Szantaż Pieczęcią): koszt 2→3, herezja 0→1 | 93.6 → 🟢 ** 90.6** (`🔻 -3.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.6 (`🔻 -3.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_COST_MINUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 1 | 93.6 → 🟢 ** 90.6** (`🔻 -3.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.6 (`🔻 -3.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_C1_H0` | KT-06 (Przesłuchanie Imienia): koszt 2→1, herezja 0→0 | 93.6 → 🟢 ** 90.6** (`🔻 -3.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.6 (`🔻 -3.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-12_C0_H1` | KT-12 (Strażnik Archiwum): koszt 1→0, herezja 0→1 | 93.6 → 🟢 ** 90.6** (`🔻 -3.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.6 (`🔻 -3.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_C0_G1` | CAA-09 (Kurier Relikwii): koszt 0→0, złoto 0→1 | 93.6 → 🟢 ** 90.5** (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.5 (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_C1_G2` | CAA-09 (Kurier Relikwii): koszt 0→1, złoto 0→2 | 93.6 → 🟢 ** 90.5** (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.5 (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_G1_H0` | CAA-09 (Kurier Relikwii): złoto 0→1, herezja 0→0 | 93.6 → 🟢 ** 90.5** (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.5 (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-11_C2_H1` | CAA-11 (Nocna Zmiana Warty): koszt 1→2, herezja 0→1 | 93.6 → 🟢 ** 90.5** (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.5 (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-11_G0_H1` | CAA-11 (Nocna Zmiana Warty): złoto 1→0, herezja 0→1 | 93.6 → 🟢 ** 90.5** (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.5 (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_C0_H0` | GC-04 (Informator): koszt 1→0, herezja 1→0 | 93.6 → 🟢 ** 90.5** (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.5 (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_HERESY_PLUS1` | GC-07 (Skrytobójstwo): heresy 0 → 1 | 93.6 → 🟢 ** 90.5** (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.5 (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_HERESY_SET1` | GC-07 (Skrytobójstwo): dodaj heresy = 1 | 93.6 → 🟢 ** 90.5** (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.5 (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_C0_H1` | GC-07 (Skrytobójstwo): koszt 0→0, herezja 0→1 | 93.6 → 🟢 ** 90.5** (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.5 (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_C0_H1` | GC-08 (Zatrute Złoto): koszt 1→0, herezja 2→1 | 93.6 → 🟢 ** 90.5** (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.5 (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_COST_PLUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 3 | 93.6 → 🟢 ** 90.5** (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.5 (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_C3_H0` | KB-07 (Szantaż Pieczęcią): koszt 2→3, herezja 0→0 | 93.6 → 🟢 ** 90.5** (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.5 (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_G1_H3` | KT-03 (Zakazana Wiedza): złoto 0→1, herezja 2→3 | 93.6 → 🟢 ** 90.5** (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.5 (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-04_COST_MINUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 0 | 93.6 → 🟢 ** 90.5** (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.5 (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-04_C0_H0` | KT-04 (Zwierciadło Herezji): koszt 1→0, herezja 0→0 | 93.6 → 🟢 ** 90.5** (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.5 (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_COST_PLUS1` | KT-08 (Areszt Wiedzy): cost 1 → 2 | 93.6 → 🟢 ** 90.5** (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.5 (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_C0_H1` | KT-08 (Areszt Wiedzy): koszt 1→0, herezja 0→1 | 93.6 → 🟢 ** 90.5** (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.5 (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_C2_H0` | KT-08 (Areszt Wiedzy): koszt 1→2, herezja 0→0 | 93.6 → 🟢 ** 90.5** (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.5 (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_C0_G4` | SO-02 (Skarbiec Trybunału): koszt 1→0, złoto 2→4 | 93.6 → 🟢 ** 90.5** (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.5 (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-07_C2_H1` | SO-07 (Przesłuchanie Oficjum): koszt 1→2, herezja 0→1 | 93.6 → 🟢 ** 90.5** (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.5 (`🔻 -3.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_G2_H1` | GC-07 (Skrytobójstwo): złoto 3→2, herezja 0→1 | 93.6 → 🟢 ** 90.4** (`🔻 -3.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.4 (`🔻 -3.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_G2_H1` | GC-08 (Zatrute Złoto): złoto 1→2, herezja 2→1 | 93.6 → 🟢 ** 90.4** (`🔻 -3.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.4 (`🔻 -3.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-11_C1_H1` | GC-11 (Fałszywe Świadectwo Cechu): koszt 0→1, herezja 2→1 | 93.6 → 🟢 ** 90.4** (`🔻 -3.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.4 (`🔻 -3.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_HERESY_MINUS1` | KB-03 (Plotka Dworska): heresy 1 → 0 | 93.6 → 🟢 ** 90.4** (`🔻 -3.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.4 (`🔻 -3.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_G0_H0` | KB-03 (Plotka Dworska): złoto 0→0, herezja 1→0 | 93.6 → 🟢 ** 90.4** (`🔻 -3.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.4 (`🔻 -3.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_HERESY_PLUS1` | KB-05 (List Żelazny): heresy 1 → 2 | 93.6 → 🟢 ** 90.4** (`🔻 -3.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.4 (`🔻 -3.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_G0_H2` | KB-05 (List Żelazny): złoto 0→0, herezja 1→2 | 93.6 → 🟢 ** 90.4** (`🔻 -3.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.4 (`🔻 -3.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-11_C2_H1` | KB-11 (Tajny Emisariusz): koszt 1→2, herezja 0→1 | 93.6 → 🟢 ** 90.4** (`🔻 -3.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.4 (`🔻 -3.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_COST_PLUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 2 | 93.6 → 🟢 ** 90.4** (`🔻 -3.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.4 (`🔻 -3.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_COST_PLUS1` | KB-06 (Areszt Królewski): cost 2 → 3 | 93.6 → 🟢 ** 90.3** (`🔻 -3.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.3 (`🔻 -3.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_C3_H0` | KB-06 (Areszt Królewski): koszt 2→3, herezja 0→0 | 93.6 → 🟢 ** 90.3** (`🔻 -3.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.3 (`🔻 -3.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_C2_H3` | KB-08 (Przekupstwo Sędziego): koszt 3→2, herezja 2→3 | 93.6 → 🟢 ** 90.3** (`🔻 -3.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.3 (`🔻 -3.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-04_G1_H0` | KT-04 (Zwierciadło Herezji): złoto 0→1, herezja 0→0 | 93.6 → 🟢 ** 90.3** (`🔻 -3.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.3 (`🔻 -3.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_G1_H0` | KT-06 (Przesłuchanie Imienia): złoto 0→1, herezja 0→0 | 93.6 → 🟢 ** 90.3** (`🔻 -3.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.3 (`🔻 -3.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-12_C2_H1` | KT-12 (Strażnik Archiwum): koszt 1→2, herezja 0→1 | 93.6 → 🟢 ** 90.3** (`🔻 -3.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.3 (`🔻 -3.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_HERESY_PLUS2` | SO-03 (Podejrzenie): heresy 4 → 6 | 93.6 → 🟢 ** 90.3** (`🔻 -3.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.3 (`🔻 -3.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_C3_G2` | SO-06 (Areszt Trybunalski): koszt 2→3, złoto 0→2 | 93.6 → 🟢 ** 90.3** (`🔻 -3.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.3 (`🔻 -3.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-11_C0_H1` | CAA-11 (Nocna Zmiana Warty): koszt 1→0, herezja 0→1 | 93.6 → 🟢 ** 90.2** (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.2 (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-11_G2_H1` | CAA-11 (Nocna Zmiana Warty): złoto 1→2, herezja 0→1 | 93.6 → 🟢 ** 90.2** (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.2 (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_HERESY_PLUS1` | GC-04 (Informator): heresy 1 → 2 | 93.6 → 🟢 ** 90.2** (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.2 (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_HERESY_MINUS1` | GC-04 (Informator): heresy 1 → 0 | 93.6 → 🟢 ** 90.2** (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.2 (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_G0_H0` | GC-04 (Informator): złoto 0→0, herezja 1→0 | 93.6 → 🟢 ** 90.2** (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.2 (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_G0_H2` | GC-04 (Informator): złoto 0→0, herezja 1→2 | 93.6 → 🟢 ** 90.2** (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.2 (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_C1_H1` | GC-07 (Skrytobójstwo): koszt 0→1, herezja 0→1 | 93.6 → 🟢 ** 90.2** (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.2 (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_G4_H1` | GC-07 (Skrytobójstwo): złoto 3→4, herezja 0→1 | 93.6 → 🟢 ** 90.2** (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.2 (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_COST_MINUS2` | KB-08 (Przekupstwo Sędziego): cost 3 → 1 | 93.6 → 🟢 ** 90.2** (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.2 (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_C0_H2` | KT-01 (Rytuał Przejścia): koszt 1→0, herezja 1→2 | 93.6 → 🟢 ** 90.2** (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.2 (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_G2_H2` | KT-01 (Rytuał Przejścia): złoto 1→2, herezja 1→2 | 93.6 → 🟢 ** 90.2** (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.2 (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_G1_H2` | KT-05 (Wskazówka Cyklu): złoto 0→1, herezja 1→2 | 93.6 → 🟢 ** 90.2** (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.2 (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_G1_H1` | KT-08 (Areszt Wiedzy): złoto 0→1, herezja 0→1 | 93.6 → 🟢 ** 90.2** (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.2 (`🔻 -3.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_C1_H1` | CAA-09 (Kurier Relikwii): koszt 0→1, herezja 0→1 | 93.6 → 🟢 ** 90.1** (`🔻 -3.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.1 (`🔻 -3.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-11_HERESY_PLUS2` | CAA-11 (Nocna Zmiana Warty): heresy 0 → 2 | 93.6 → 🟢 ** 90.1** (`🔻 -3.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.1 (`🔻 -3.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-11_HERESY_SET2` | CAA-11 (Nocna Zmiana Warty): dodaj heresy = 2 | 93.6 → 🟢 ** 90.1** (`🔻 -3.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.1 (`🔻 -3.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_HERESY_PLUS1` | GC-06 (Szantaż): heresy 1 → 2 | 93.6 → 🟢 ** 90.1** (`🔻 -3.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.1 (`🔻 -3.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_G0_H2` | GC-06 (Szantaż): złoto 0→0, herezja 1→2 | 93.6 → 🟢 ** 90.1** (`🔻 -3.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.1 (`🔻 -3.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-12_COST_PLUS1` | GC-12 (Złodziejski Zwiad): cost 0 → 1 | 93.6 → 🟢 ** 90.1** (`🔻 -3.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.1 (`🔻 -3.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_C3_H1` | KB-04 (Faworyt Dworu): koszt 2→3, herezja 0→1 | 93.6 → 🟢 ** 90.1** (`🔻 -3.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.1 (`🔻 -3.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_C0_H2` | KT-05 (Wskazówka Cyklu): koszt 1→0, herezja 1→2 | 93.6 → 🟢 ** 90.1** (`🔻 -3.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.1 (`🔻 -3.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_C0_G1` | KT-09 (Fragment Kodeksu): koszt 1→0, złoto 0→1 | 93.6 → 🟢 ** 90.1** (`🔻 -3.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.1 (`🔻 -3.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_C2_H1` | SO-01 (Patrol Familiariuszy): koszt 1→2, herezja 2→1 | 93.6 → 🟢 ** 90.1** (`🔻 -3.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.1 (`🔻 -3.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_G1_H3` | SO-01 (Patrol Familiariuszy): złoto 2→1, herezja 2→3 | 93.6 → 🟢 ** 90.1** (`🔻 -3.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.1 (`🔻 -3.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_C0_G5` | CAA-02 (Złoto z Kryjówki): koszt 0→0, złoto 3→5 | 93.6 → 🟢 ** 90.0** (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.0 (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_C1_H2` | CAA-03 (Cień na Rynku): koszt 0→1, herezja 1→2 | 93.6 → 🟢 ** 90.0** (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.0 (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_G1_H2` | CAA-03 (Cień na Rynku): złoto 2→1, herezja 1→2 | 93.6 → 🟢 ** 90.0** (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.0 (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_G1_H2` | GC-04 (Informator): złoto 0→1, herezja 1→2 | 93.6 → 🟢 ** 90.0** (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.0 (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-12_G0_H3` | GC-12 (Złodziejski Zwiad): złoto 1→0, herezja 2→3 | 93.6 → 🟢 ** 90.0** (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.0 (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_C3_G1` | KB-05 (List Żelazny): koszt 2→3, złoto 0→1 | 93.6 → 🟢 ** 90.0** (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.0 (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_C2_H1` | KB-12 (Szantaż Salonowy): koszt 1→2, herezja 2→1 | 93.6 → 🟢 ** 90.0** (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.0 (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_C2_H1` | KT-08 (Areszt Wiedzy): koszt 1→2, herezja 0→1 | 93.6 → 🟢 ** 90.0** (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.0 (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-12_HERESY_PLUS1` | KT-12 (Strażnik Archiwum): heresy 0 → 1 | 93.6 → 🟢 ** 90.0** (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.0 (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-12_HERESY_SET1` | KT-12 (Strażnik Archiwum): dodaj heresy = 1 | 93.6 → 🟢 ** 90.0** (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.0 (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-12_G0_H1` | KT-12 (Strażnik Archiwum): złoto 0→0, herezja 0→1 | 93.6 → 🟢 ** 90.0** (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.0 (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_C1_H3` | SO-03 (Podejrzenie): koszt 2→1, herezja 4→3 | 93.6 → 🟢 ** 90.0** (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 90.0 (`🔻 -3.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_C0_H2` | GC-04 (Informator): koszt 1→0, herezja 1→2 | 93.6 → 🟡 ** 89.9** (`🔻 -3.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.9 (`🔻 -3.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-11_G1_H1` | GC-11 (Fałszywe Świadectwo Cechu): złoto 0→1, herezja 2→1 | 93.6 → 🟡 ** 89.9** (`🔻 -3.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.9 (`🔻 -3.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-12_C1_H3` | GC-12 (Złodziejski Zwiad): koszt 0→1, herezja 2→3 | 93.6 → 🟡 ** 89.9** (`🔻 -3.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.9 (`🔻 -3.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_COST_PLUS1` | KB-03 (Plotka Dworska): cost 1 → 2 | 93.6 → 🟡 ** 89.9** (`🔻 -3.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.9 (`🔻 -3.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_C1_H1` | KB-04 (Faworyt Dworu): koszt 2→1, herezja 0→1 | 93.6 → 🟡 ** 89.9** (`🔻 -3.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.9 (`🔻 -3.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_HERESY_PLUS2` | KT-06 (Przesłuchanie Imienia): heresy 0 → 2 | 93.6 → 🟡 ** 89.9** (`🔻 -3.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.9 (`🔻 -3.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_HERESY_SET2` | KT-06 (Przesłuchanie Imienia): dodaj heresy = 2 | 93.6 → 🟡 ** 89.9** (`🔻 -3.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.9 (`🔻 -3.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 1 → 2 | 93.6 → 🟡 ** 89.9** (`🔻 -3.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.9 (`🔻 -3.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_G1_H1` | SO-01 (Patrol Familiariuszy): złoto 2→1, herezja 2→1 | 93.6 → 🟡 ** 89.9** (`🔻 -3.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.9 (`🔻 -3.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-07_COST_PLUS1` | SO-07 (Przesłuchanie Oficjum): cost 1 → 2 | 93.6 → 🟡 ** 89.9** (`🔻 -3.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.9 (`🔻 -3.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-07_C2_H0` | SO-07 (Przesłuchanie Oficjum): koszt 1→2, herezja 0→0 | 93.6 → 🟡 ** 89.9** (`🔻 -3.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.9 (`🔻 -3.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-11_COST_PLUS2` | CAA-11 (Nocna Zmiana Warty): cost 1 → 3 | 93.6 → 🟡 ** 89.8** (`🔻 -3.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.8 (`🔻 -3.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_G1_H0` | GC-06 (Szantaż): złoto 0→1, herezja 1→0 | 93.6 → 🟡 ** 89.8** (`🔻 -3.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.8 (`🔻 -3.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_COST_PLUS1` | KB-01 (Rozkaz Dworu): cost 1 → 2 | 93.6 → 🟡 ** 89.8** (`🔻 -3.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.8 (`🔻 -3.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_C2_H3` | SO-01 (Patrol Familiariuszy): koszt 1→2, herezja 2→3 | 93.6 → 🟡 ** 89.8** (`🔻 -3.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.8 (`🔻 -3.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_HERESY_PLUS2` | SO-04 (Publiczne Ostrzeżenie): heresy 0 → 2 | 93.6 → 🟡 ** 89.8** (`🔻 -3.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.8 (`🔻 -3.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_HERESY_SET2` | SO-04 (Publiczne Ostrzeżenie): dodaj heresy = 2 | 93.6 → 🟡 ** 89.8** (`🔻 -3.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.8 (`🔻 -3.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-07_G1_H0` | SO-07 (Przesłuchanie Oficjum): złoto 2→1, herezja 0→0 | 93.6 → 🟡 ** 89.8** (`🔻 -3.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.8 (`🔻 -3.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_COST_MINUS2` | SO-10 (Oczyść Miasto): cost 5 → 3 | 93.6 → 🟡 ** 89.8** (`🔻 -3.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.8 (`🔻 -3.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_G1_H0` | GC-04 (Informator): złoto 0→1, herezja 1→0 | 93.6 → 🟡 ** 89.7** (`🔻 -3.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.7 (`🔻 -3.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_C2_H0` | KB-01 (Rozkaz Dworu): koszt 1→2, herezja 1→0 | 93.6 → 🟡 ** 89.7** (`🔻 -3.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.7 (`🔻 -3.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_COST_MINUS1` | KB-02 (Pobór Podatków): cost 1 → 0 | 93.6 → 🟡 ** 89.7** (`🔻 -3.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.7 (`🔻 -3.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_C0_H0` | KB-02 (Pobór Podatków): koszt 1→0, herezja 0→0 | 93.6 → 🟡 ** 89.7** (`🔻 -3.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.7 (`🔻 -3.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-11_HERESY_PLUS2` | KB-11 (Tajny Emisariusz): heresy 0 → 2 | 93.6 → 🟡 ** 89.7** (`🔻 -3.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.7 (`🔻 -3.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-11_HERESY_SET2` | KB-11 (Tajny Emisariusz): dodaj heresy = 2 | 93.6 → 🟡 ** 89.7** (`🔻 -3.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.7 (`🔻 -3.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-04_C2_G2` | KT-04 (Zwierciadło Herezji): koszt 1→2, złoto 0→2 | 93.6 → 🟡 ** 89.7** (`🔻 -3.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.7 (`🔻 -3.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_HERESY_PLUS1` | KT-08 (Areszt Wiedzy): heresy 0 → 1 | 93.6 → 🟡 ** 89.7** (`🔻 -3.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.7 (`🔻 -3.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_HERESY_SET1` | KT-08 (Areszt Wiedzy): dodaj heresy = 1 | 93.6 → 🟡 ** 89.7** (`🔻 -3.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.7 (`🔻 -3.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_G0_H1` | KT-08 (Areszt Wiedzy): złoto 0→0, herezja 0→1 | 93.6 → 🟡 ** 89.7** (`🔻 -3.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.7 (`🔻 -3.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_C0_G2` | CAA-09 (Kurier Relikwii): koszt 0→0, złoto 0→2 | 93.6 → 🟡 ** 89.6** (`🔻 -4.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.6 (`🔻 -4.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_C4_H2` | GC-06 (Szantaż): koszt 3→4, herezja 1→2 | 93.6 → 🟡 ** 89.6** (`🔻 -4.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.6 (`🔻 -4.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-12_COST_PLUS2` | GC-12 (Złodziejski Zwiad): cost 0 → 2 | 93.6 → 🟡 ** 89.6** (`🔻 -4.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.6 (`🔻 -4.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_COST_MINUS1` | KB-01 (Rozkaz Dworu): cost 1 → 0 | 93.6 → 🟡 ** 89.6** (`🔻 -4.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.6 (`🔻 -4.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_COST_MINUS1` | KB-04 (Faworyt Dworu): cost 2 → 1 | 93.6 → 🟡 ** 89.6** (`🔻 -4.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.6 (`🔻 -4.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_C1_H0` | KB-04 (Faworyt Dworu): koszt 2→1, herezja 0→0 | 93.6 → 🟡 ** 89.6** (`🔻 -4.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.6 (`🔻 -4.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_HERESY_MINUS1` | KB-12 (Szantaż Salonowy): heresy 2 → 1 | 93.6 → 🟡 ** 89.6** (`🔻 -4.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.6 (`🔻 -4.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_G0_H1` | KB-12 (Szantaż Salonowy): złoto 0→0, herezja 2→1 | 93.6 → 🟡 ** 89.6** (`🔻 -4.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.6 (`🔻 -4.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_C2_H0` | KT-09 (Fragment Kodeksu): koszt 1→2, herezja 1→0 | 93.6 → 🟡 ** 89.6** (`🔻 -4.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.6 (`🔻 -4.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_C2_H0` | GC-06 (Szantaż): koszt 3→2, herezja 1→0 | 93.6 → 🟡 ** 89.5** (`🔻 -4.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.5 (`🔻 -4.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_C2_H2` | KB-01 (Rozkaz Dworu): koszt 1→2, herezja 1→2 | 93.6 → 🟡 ** 89.5** (`🔻 -4.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.5 (`🔻 -4.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_HERESY_MINUS1` | KB-10 (Pieczęć Korony): heresy 1 → 0 | 93.6 → 🟡 ** 89.5** (`🔻 -4.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.5 (`🔻 -4.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_HERESY_PLUS2` | KT-08 (Areszt Wiedzy): heresy 0 → 2 | 93.6 → 🟡 ** 89.5** (`🔻 -4.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.5 (`🔻 -4.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_HERESY_SET2` | KT-08 (Areszt Wiedzy): dodaj heresy = 2 | 93.6 → 🟡 ** 89.5** (`🔻 -4.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.5 (`🔻 -4.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_C1_H1` | CAA-08 (Kaptur Nocy): koszt 2→1, herezja 0→1 | 93.6 → 🟡 ** 89.4** (`🔻 -4.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.4 (`🔻 -4.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_G3_H1` | CAA-08 (Kaptur Nocy): złoto 2→3, herezja 0→1 | 93.6 → 🟡 ** 89.4** (`🔻 -4.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.4 (`🔻 -4.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_COST_PLUS2` | GC-04 (Informator): cost 1 → 3 | 93.6 → 🟡 ** 89.4** (`🔻 -4.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.4 (`🔻 -4.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-11_HERESY_MINUS2` | GC-11 (Fałszywe Świadectwo Cechu): heresy 2 → 0 | 93.6 → 🟡 ** 89.4** (`🔻 -4.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.4 (`🔻 -4.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_G3_H0` | KB-10 (Pieczęć Korony): złoto 2→3, herezja 1→0 | 93.6 → 🟡 ** 89.4** (`🔻 -4.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.4 (`🔻 -4.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_COST_PLUS2` | SO-01 (Patrol Familiariuszy): cost 1 → 3 | 93.6 → 🟡 ** 89.4** (`🔻 -4.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.4 (`🔻 -4.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_HERESY_PLUS2` | GC-06 (Szantaż): heresy 1 → 3 | 93.6 → 🟡 ** 89.3** (`🔻 -4.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.3 (`🔻 -4.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_C2_G1` | KB-01 (Rozkaz Dworu): koszt 1→2, złoto 0→1 | 93.6 → 🟡 ** 89.3** (`🔻 -4.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.3 (`🔻 -4.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_C3_G2` | KT-06 (Przesłuchanie Imienia): koszt 2→3, złoto 0→2 | 93.6 → 🟡 ** 89.3** (`🔻 -4.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.3 (`🔻 -4.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_C0_H2` | KT-09 (Fragment Kodeksu): koszt 1→0, herezja 1→2 | 93.6 → 🟡 ** 89.3** (`🔻 -4.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.3 (`🔻 -4.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_C3_H1` | KT-10 (Pieczęć Salomona): koszt 4→3, herezja 0→1 | 93.6 → 🟡 ** 89.3** (`🔻 -4.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.3 (`🔻 -4.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-07_G1_H1` | SO-07 (Przesłuchanie Oficjum): złoto 2→1, herezja 0→1 | 93.6 → 🟡 ** 89.3** (`🔻 -4.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.3 (`🔻 -4.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_C0_G1` | SO-09 (Świadek Koronny): koszt 1→0, złoto 0→1 | 93.6 → 🟡 ** 89.3** (`🔻 -4.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.3 (`🔻 -4.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_C0_G2` | GC-08 (Zatrute Złoto): koszt 1→0, złoto 1→2 | 93.6 → 🟡 ** 89.2** (`🔻 -4.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.2 (`🔻 -4.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_HERESY_MINUS1` | GC-10 (Upadek Domu): heresy 2 → 1 | 93.6 → 🟡 ** 89.2** (`🔻 -4.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.2 (`🔻 -4.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_G0_H1` | GC-10 (Upadek Domu): złoto 0→0, herezja 2→1 | 93.6 → 🟡 ** 89.2** (`🔻 -4.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.2 (`🔻 -4.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-12_HERESY_PLUS2` | GC-12 (Złodziejski Zwiad): heresy 2 → 4 | 93.6 → 🟡 ** 89.2** (`🔻 -4.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.2 (`🔻 -4.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_COST_PLUS2` | KB-12 (Szantaż Salonowy): cost 1 → 3 | 93.6 → 🟡 ** 89.2** (`🔻 -4.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.2 (`🔻 -4.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_C2_G1` | KB-12 (Szantaż Salonowy): koszt 1→2, złoto 0→1 | 93.6 → 🟡 ** 89.2** (`🔻 -4.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.2 (`🔻 -4.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_C0_G3` | KT-01 (Rytuał Przejścia): koszt 1→0, złoto 1→3 | 93.6 → 🟡 ** 89.2** (`🔻 -4.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.2 (`🔻 -4.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-12_HERESY_MINUS2` | SO-12 (Straż Trybunalska): heresy 2 → 0 | 93.6 → 🟡 ** 89.2** (`🔻 -4.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.2 (`🔻 -4.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-01_COST_MINUS2` | CAA-01 (Przejście Podziemiami): cost 2 → 0 | 93.6 → 🟡 ** 89.1** (`🔻 -4.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.1 (`🔻 -4.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-01_C1_G1` | CAA-01 (Przejście Podziemiami): koszt 2→1, złoto 0→1 | 93.6 → 🟡 ** 89.1** (`🔻 -4.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.1 (`🔻 -4.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_C0_H2` | KB-03 (Plotka Dworska): koszt 1→0, herezja 1→2 | 93.6 → 🟡 ** 89.1** (`🔻 -4.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.1 (`🔻 -4.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_G1_H2` | KB-10 (Pieczęć Korony): złoto 2→1, herezja 1→2 | 93.6 → 🟡 ** 89.1** (`🔻 -4.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.1 (`🔻 -4.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_C0_G1` | CAA-06 (Ucieczka z Lochów): koszt 0→0, złoto 0→1 | 93.6 → 🟡 ** 89.0** (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.0 (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_C1_G2` | CAA-06 (Ucieczka z Lochów): koszt 0→1, złoto 0→2 | 93.6 → 🟡 ** 89.0** (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.0 (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_G1_H0` | CAA-06 (Ucieczka z Lochów): złoto 0→1, herezja 0→0 | 93.6 → 🟡 ** 89.0** (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.0 (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_COST_PLUS2` | KB-01 (Rozkaz Dworu): cost 1 → 3 | 93.6 → 🟡 ** 89.0** (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.0 (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_COST_PLUS1` | KB-05 (List Żelazny): cost 2 → 3 | 93.6 → 🟡 ** 89.0** (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.0 (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_C3_H0` | KB-05 (List Żelazny): koszt 2→3, herezja 1→0 | 93.6 → 🟡 ** 89.0** (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.0 (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-11_HERESY_PLUS1` | KB-11 (Tajny Emisariusz): heresy 0 → 1 | 93.6 → 🟡 ** 89.0** (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.0 (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-11_HERESY_SET1` | KB-11 (Tajny Emisariusz): dodaj heresy = 1 | 93.6 → 🟡 ** 89.0** (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.0 (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-11_G0_H1` | KB-11 (Tajny Emisariusz): złoto 0→0, herezja 0→1 | 93.6 → 🟡 ** 89.0** (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.0 (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_COST_MINUS1` | KT-09 (Fragment Kodeksu): cost 1 → 0 | 93.6 → 🟡 ** 89.0** (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.0 (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_G1_H2` | KT-09 (Fragment Kodeksu): złoto 0→1, herezja 1→2 | 93.6 → 🟡 ** 89.0** (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.0 (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_C5_G2` | KT-10 (Pieczęć Salomona): koszt 4→5, złoto 0→2 | 93.6 → 🟡 ** 89.0** (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.0 (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_COST_MINUS1` | SO-06 (Areszt Trybunalski): cost 2 → 1 | 93.6 → 🟡 ** 89.0** (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.0 (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_C1_H0` | SO-06 (Areszt Trybunalski): koszt 2→1, herezja 0→0 | 93.6 → 🟡 ** 89.0** (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.0 (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_G1_H0` | SO-06 (Areszt Trybunalski): złoto 0→1, herezja 0→0 | 93.6 → 🟡 ** 89.0** (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 89.0 (`🔻 -4.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-12_HERESY_PLUS1` | CAA-12 (Skrytka w Murach): heresy 0 → 1 | 93.6 → 🟡 ** 88.9** (`🔻 -4.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.9 (`🔻 -4.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-12_HERESY_SET1` | CAA-12 (Skrytka w Murach): dodaj heresy = 1 | 93.6 → 🟡 ** 88.9** (`🔻 -4.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.9 (`🔻 -4.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_COST_PLUS2` | GC-06 (Szantaż): cost 3 → 5 | 93.6 → 🟡 ** 88.9** (`🔻 -4.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.9 (`🔻 -4.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-12_C2_G2` | KT-12 (Strażnik Archiwum): koszt 1→2, złoto 0→2 | 93.6 → 🟡 ** 88.9** (`🔻 -4.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.9 (`🔻 -4.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_HERESY_PLUS1` | CAA-09 (Kurier Relikwii): heresy 0 → 1 | 93.6 → 🟡 ** 88.8** (`🔻 -4.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.8 (`🔻 -4.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_HERESY_SET1` | CAA-09 (Kurier Relikwii): dodaj heresy = 1 | 93.6 → 🟡 ** 88.8** (`🔻 -4.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.8 (`🔻 -4.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_C0_H1` | CAA-09 (Kurier Relikwii): koszt 0→0, herezja 0→1 | 93.6 → 🟡 ** 88.8** (`🔻 -4.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.8 (`🔻 -4.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_G0_H1` | CAA-09 (Kurier Relikwii): złoto 0→0, herezja 0→1 | 93.6 → 🟡 ** 88.8** (`🔻 -4.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.8 (`🔻 -4.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_C5_H1` | GC-10 (Upadek Domu): koszt 4→5, herezja 2→1 | 93.6 → 🟡 ** 88.8** (`🔻 -4.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.8 (`🔻 -4.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_HERESY_PLUS2` | KB-04 (Faworyt Dworu): heresy 0 → 2 | 93.6 → 🟡 ** 88.8** (`🔻 -4.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.8 (`🔻 -4.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_HERESY_SET2` | KB-04 (Faworyt Dworu): dodaj heresy = 2 | 93.6 → 🟡 ** 88.8** (`🔻 -4.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.8 (`🔻 -4.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_COST_PLUS1` | KT-03 (Zakazana Wiedza): cost 0 → 1 | 93.6 → 🟡 ** 88.8** (`🔻 -4.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.8 (`🔻 -4.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_COST_PLUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 2 | 93.6 → 🟡 ** 88.7** (`🔻 -4.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.7 (`🔻 -4.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_C2_G2` | KT-09 (Fragment Kodeksu): koszt 1→2, złoto 0→2 | 93.6 → 🟡 ** 88.7** (`🔻 -4.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.7 (`🔻 -4.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_C5_G1` | KT-10 (Pieczęć Salomona): koszt 4→5, złoto 0→1 | 93.6 → 🟡 ** 88.7** (`🔻 -4.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.7 (`🔻 -4.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_G1_H1` | GC-10 (Upadek Domu): złoto 0→1, herezja 2→1 | 93.6 → 🟡 ** 88.6** (`🔻 -5.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.6 (`🔻 -5.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-11_COST_PLUS1` | KB-11 (Tajny Emisariusz): cost 1 → 2 | 93.6 → 🟡 ** 88.6** (`🔻 -5.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.6 (`🔻 -5.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-11_C2_H0` | KB-11 (Tajny Emisariusz): koszt 1→2, herezja 0→0 | 93.6 → 🟡 ** 88.6** (`🔻 -5.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.6 (`🔻 -5.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_C0_H1` | KB-12 (Szantaż Salonowy): koszt 1→0, herezja 2→1 | 93.6 → 🟡 ** 88.6** (`🔻 -5.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.6 (`🔻 -5.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_C0_G3` | GC-08 (Zatrute Złoto): koszt 1→0, złoto 1→3 | 93.6 → 🟡 ** 88.5** (`🔻 -5.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.5 (`🔻 -5.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_C1_H2` | KB-05 (List Żelazny): koszt 2→1, herezja 1→2 | 93.6 → 🟡 ** 88.5** (`🔻 -5.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.5 (`🔻 -5.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_C3_G1` | KB-06 (Areszt Królewski): koszt 2→3, złoto 0→1 | 93.6 → 🟡 ** 88.5** (`🔻 -5.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.5 (`🔻 -5.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_HERESY_PLUS1` | CAA-04 (Fałszywy Trop): heresy 0 → 1 | 93.6 → 🟡 ** 88.4** (`🔻 -5.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.4 (`🔻 -5.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_HERESY_SET1` | CAA-04 (Fałszywy Trop): dodaj heresy = 1 | 93.6 → 🟡 ** 88.4** (`🔻 -5.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.4 (`🔻 -5.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_C0_H1` | CAA-04 (Fałszywy Trop): koszt 0→0, herezja 0→1 | 93.6 → 🟡 ** 88.4** (`🔻 -5.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.4 (`🔻 -5.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_COST_MINUS1` | KB-03 (Plotka Dworska): cost 1 → 0 | 93.6 → 🟡 ** 88.4** (`🔻 -5.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.4 (`🔻 -5.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_HERESY_PLUS2` | KB-07 (Szantaż Pieczęcią): heresy 0 → 2 | 93.6 → 🟡 ** 88.4** (`🔻 -5.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.4 (`🔻 -5.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_HERESY_SET2` | KB-07 (Szantaż Pieczęcią): dodaj heresy = 2 | 93.6 → 🟡 ** 88.4** (`🔻 -5.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.4 (`🔻 -5.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_COST_PLUS1` | KB-12 (Szantaż Salonowy): cost 1 → 2 | 93.6 → 🟡 ** 88.4** (`🔻 -5.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.4 (`🔻 -5.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_C2_G2` | KT-08 (Areszt Wiedzy): koszt 1→2, złoto 0→2 | 93.6 → 🟡 ** 88.4** (`🔻 -5.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.4 (`🔻 -5.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_G1_H0` | KT-08 (Areszt Wiedzy): złoto 0→1, herezja 0→0 | 93.6 → 🟡 ** 88.4** (`🔻 -5.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.4 (`🔻 -5.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_HERESY_MINUS2` | SO-03 (Podejrzenie): heresy 4 → 2 | 93.6 → 🟡 ** 88.4** (`🔻 -5.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.4 (`🔻 -5.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_C1_H1` | KB-07 (Szantaż Pieczęcią): koszt 2→1, herezja 0→1 | 93.6 → 🟡 ** 88.3** (`🔻 -5.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.3 (`🔻 -5.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_COST_MINUS1` | KT-08 (Areszt Wiedzy): cost 1 → 0 | 93.6 → 🟡 ** 88.3** (`🔻 -5.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.3 (`🔻 -5.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_C0_H0` | KT-08 (Areszt Wiedzy): koszt 1→0, herezja 0→0 | 93.6 → 🟡 ** 88.3** (`🔻 -5.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.3 (`🔻 -5.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_COST_PLUS2` | CAA-06 (Ucieczka z Lochów): cost 0 → 2 | 93.6 → 🟡 ** 88.2** (`🔻 -5.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.2 (`🔻 -5.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-12_HERESY_MINUS2` | GC-12 (Złodziejski Zwiad): heresy 2 → 0 | 93.6 → 🟡 ** 88.2** (`🔻 -5.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.2 (`🔻 -5.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_COST_PLUS1` | KB-04 (Faworyt Dworu): cost 2 → 3 | 93.6 → 🟡 ** 88.2** (`🔻 -5.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.2 (`🔻 -5.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_C3_H0` | KB-04 (Faworyt Dworu): koszt 2→3, herezja 0→0 | 93.6 → 🟡 ** 88.2** (`🔻 -5.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.2 (`🔻 -5.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_C1_H1` | KB-09 (Dekret Królewski): koszt 2→1, herezja 0→1 | 93.6 → 🟡 ** 88.2** (`🔻 -5.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.2 (`🔻 -5.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_C3_G1` | KB-09 (Dekret Królewski): koszt 2→3, złoto 0→1 | 93.6 → 🟡 ** 88.2** (`🔻 -5.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.2 (`🔻 -5.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_C0_G4` | KT-02 (Transmutacja Złota): koszt 0→0, złoto 3→4 | 93.6 → 🟡 ** 88.2** (`🔻 -5.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.2 (`🔻 -5.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_C1_G5` | KT-02 (Transmutacja Złota): koszt 0→1, złoto 3→5 | 93.6 → 🟡 ** 88.2** (`🔻 -5.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.2 (`🔻 -5.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_G4_H0` | KT-02 (Transmutacja Złota): złoto 3→4, herezja 0→0 | 93.6 → 🟡 ** 88.2** (`🔻 -5.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.2 (`🔻 -5.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-11_G2_H0` | KT-11 (Medytacja Sefirot): złoto 1→2, herezja 0→0 | 93.6 → 🟡 ** 88.2** (`🔻 -5.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.2 (`🔻 -5.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_C3_H1` | GC-10 (Upadek Domu): koszt 4→3, herezja 2→1 | 93.6 → 🟡 ** 88.1** (`🔻 -5.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.1 (`🔻 -5.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_C2_H3` | KB-12 (Szantaż Salonowy): koszt 1→2, herezja 2→3 | 93.6 → 🟡 ** 88.1** (`🔻 -5.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.1 (`🔻 -5.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-12_G1_H0` | KT-12 (Strażnik Archiwum): złoto 0→1, herezja 0→0 | 93.6 → 🟡 ** 88.1** (`🔻 -5.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.1 (`🔻 -5.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_C2_H2` | GC-04 (Informator): koszt 1→2, herezja 1→2 | 93.6 → 🟡 ** 88.0** (`🔻 -5.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.0 (`🔻 -5.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_HERESY_PLUS2` | GC-07 (Skrytobójstwo): heresy 0 → 2 | 93.6 → 🟡 ** 88.0** (`🔻 -5.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.0 (`🔻 -5.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_HERESY_SET2` | GC-07 (Skrytobójstwo): dodaj heresy = 2 | 93.6 → 🟡 ** 88.0** (`🔻 -5.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 88.0 (`🔻 -5.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_C3_H2` | KB-05 (List Żelazny): koszt 2→3, herezja 1→2 | 93.6 → 🟡 ** 87.9** (`🔻 -5.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.9 (`🔻 -5.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_C0_G2` | SO-09 (Świadek Koronny): koszt 1→0, złoto 0→2 | 93.6 → 🟡 ** 87.9** (`🔻 -5.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.9 (`🔻 -5.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_C0_H1` | SO-02 (Skarbiec Trybunału): koszt 1→0, herezja 2→1 | 93.6 → 🟡 ** 87.8** (`🔻 -5.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.8 (`🔻 -5.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_HERESY_PLUS1` | KB-09 (Dekret Królewski): heresy 0 → 1 | 93.6 → 🟡 ** 87.7** (`🔻 -5.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.7 (`🔻 -5.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_HERESY_SET1` | KB-09 (Dekret Królewski): dodaj heresy = 1 | 93.6 → 🟡 ** 87.7** (`🔻 -5.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.7 (`🔻 -5.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_G0_H1` | KB-09 (Dekret Królewski): złoto 0→0, herezja 0→1 | 93.6 → 🟡 ** 87.7** (`🔻 -5.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.7 (`🔻 -5.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_G1_H1` | KB-09 (Dekret Królewski): złoto 0→1, herezja 0→1 | 93.6 → 🟡 ** 87.7** (`🔻 -5.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.7 (`🔻 -5.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_COST_PLUS2` | KT-08 (Areszt Wiedzy): cost 1 → 3 | 93.6 → 🟡 ** 87.7** (`🔻 -5.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.7 (`🔻 -5.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-12_COST_MINUS1` | KT-12 (Strażnik Archiwum): cost 1 → 0 | 93.6 → 🟡 ** 87.7** (`🔻 -5.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.7 (`🔻 -5.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-12_C0_H0` | KT-12 (Strażnik Archiwum): koszt 1→0, herezja 0→0 | 93.6 → 🟡 ** 87.7** (`🔻 -5.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.7 (`🔻 -5.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_HERESY_PLUS2` | CAA-09 (Kurier Relikwii): heresy 0 → 2 | 93.6 → 🟡 ** 87.6** (`🔻 -6.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.6 (`🔻 -6.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_HERESY_SET2` | CAA-09 (Kurier Relikwii): dodaj heresy = 2 | 93.6 → 🟡 ** 87.6** (`🔻 -6.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.6 (`🔻 -6.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_G4_H1` | KT-02 (Transmutacja Złota): złoto 3→4, herezja 0→1 | 93.6 → 🟡 ** 87.6** (`🔻 -6.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.6 (`🔻 -6.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_COST_PLUS1` | KT-10 (Pieczęć Salomona): cost 4 → 5 | 93.6 → 🟡 ** 87.6** (`🔻 -6.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.6 (`🔻 -6.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_C5_H0` | KT-10 (Pieczęć Salomona): koszt 4→5, herezja 0→0 | 93.6 → 🟡 ** 87.6** (`🔻 -6.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.6 (`🔻 -6.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-11_COST_PLUS2` | KB-11 (Tajny Emisariusz): cost 1 → 3 | 93.6 → 🟡 ** 87.5** (`🔻 -6.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.5 (`🔻 -6.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_C0_G1` | KT-03 (Zakazana Wiedza): koszt 0→0, złoto 0→1 | 93.6 → 🟡 ** 87.5** (`🔻 -6.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.5 (`🔻 -6.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_G3_H1` | SO-02 (Skarbiec Trybunału): złoto 2→3, herezja 2→1 | 93.6 → 🟡 ** 87.5** (`🔻 -6.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.5 (`🔻 -6.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_HERESY_PLUS1` | KB-02 (Pobór Podatków): heresy 0 → 1 | 93.6 → 🟡 ** 87.4** (`🔻 -6.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.4 (`🔻 -6.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_HERESY_SET1` | KB-02 (Pobór Podatków): dodaj heresy = 1 | 93.6 → 🟡 ** 87.4** (`🔻 -6.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.4 (`🔻 -6.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_C0_H0` | KT-01 (Rytuał Przejścia): koszt 1→0, herezja 1→0 | 93.6 → 🟡 ** 87.4** (`🔻 -6.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.4 (`🔻 -6.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_G0_H1` | SO-04 (Publiczne Ostrzeżenie): złoto 1→0, herezja 0→1 | 93.6 → 🟡 ** 87.4** (`🔻 -6.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.4 (`🔻 -6.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_HERESY_PLUS2` | KB-12 (Szantaż Salonowy): heresy 2 → 4 | 93.6 → 🟡 ** 87.2** (`🔻 -6.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.2 (`🔻 -6.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-07_COST_PLUS2` | SO-07 (Przesłuchanie Oficjum): cost 1 → 3 | 93.6 → 🟡 ** 87.2** (`🔻 -6.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.2 (`🔻 -6.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_G4_H1` | CAA-02 (Złoto z Kryjówki): złoto 3→4, herezja 0→1 | 93.6 → 🟡 ** 87.1** (`🔻 -6.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.1 (`🔻 -6.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_HERESY_PLUS1` | CAA-03 (Cień na Rynku): heresy 1 → 2 | 93.6 → 🟡 ** 87.1** (`🔻 -6.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.1 (`🔻 -6.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_C0_H2` | CAA-03 (Cień na Rynku): koszt 0→0, herezja 1→2 | 93.6 → 🟡 ** 87.1** (`🔻 -6.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.1 (`🔻 -6.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_C2_H2` | KB-03 (Plotka Dworska): koszt 1→2, herezja 1→2 | 93.6 → 🟡 ** 87.1** (`🔻 -6.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.1 (`🔻 -6.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-11_C0_H1` | KB-11 (Tajny Emisariusz): koszt 1→0, herezja 0→1 | 93.6 → 🟡 ** 87.1** (`🔻 -6.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.1 (`🔻 -6.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_C1_G2` | KT-03 (Zakazana Wiedza): koszt 0→1, złoto 0→2 | 93.6 → 🟡 ** 87.1** (`🔻 -6.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.1 (`🔻 -6.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 0 → 1 | 93.6 → 🟡 ** 87.0** (`🔻 -6.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.0 (`🔻 -6.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_C1_H0` | KT-02 (Transmutacja Złota): koszt 0→1, herezja 0→0 | 93.6 → 🟡 ** 87.0** (`🔻 -6.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 87.0 (`🔻 -6.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-11_C2_G1` | KB-11 (Tajny Emisariusz): koszt 1→2, złoto 0→1 | 93.6 → 🟡 ** 86.9** (`🔻 -6.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 86.9 (`🔻 -6.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_G2_H0` | KT-01 (Rytuał Przejścia): złoto 1→2, herezja 1→0 | 93.6 → 🟡 ** 86.9** (`🔻 -6.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 86.9 (`🔻 -6.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_G4_H1` | CAA-07 (Szantaż Bractwa): złoto 3→4, herezja 0→1 | 93.6 → 🟡 ** 86.8** (`🔻 -6.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 86.8 (`🔻 -6.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_HERESY_PLUS2` | GC-09 (Lista Dłużników): heresy 0 → 2 | 93.6 → 🟡 ** 86.8** (`🔻 -6.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 86.8 (`🔻 -6.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_HERESY_SET2` | GC-09 (Lista Dłużników): dodaj heresy = 2 | 93.6 → 🟡 ** 86.8** (`🔻 -6.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 86.8 (`🔻 -6.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_C0_G2` | KT-09 (Fragment Kodeksu): koszt 1→0, złoto 0→2 | 93.6 → 🟡 ** 86.8** (`🔻 -6.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 86.8 (`🔻 -6.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_HERESY_PLUS2` | KT-10 (Pieczęć Salomona): heresy 0 → 2 | 93.6 → 🟡 ** 86.6** (`🔻 -7.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 86.6 (`🔻 -7.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_HERESY_SET2` | KT-10 (Pieczęć Salomona): dodaj heresy = 2 | 93.6 → 🟡 ** 86.6** (`🔻 -7.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 86.6 (`🔻 -7.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_C2_H1` | SO-04 (Publiczne Ostrzeżenie): koszt 1→2, herezja 0→1 | 93.6 → 🟡 ** 86.3** (`🔻 -7.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 86.3 (`🔻 -7.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_COST_PLUS2` | CAA-10 (Echo Alhambry): cost 2 → 4 | 93.6 → 🟡 ** 86.2** (`🔻 -7.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 86.2 (`🔻 -7.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-12_C0_H1` | CAA-12 (Skrytka w Murach): koszt 1→0, herezja 0→1 | 93.6 → 🟡 ** 86.2** (`🔻 -7.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 86.2 (`🔻 -7.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-12_G5_H1` | CAA-12 (Skrytka w Murach): złoto 4→5, herezja 0→1 | 93.6 → 🟡 ** 86.2** (`🔻 -7.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 86.2 (`🔻 -7.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_G1_H1` | KB-04 (Faworyt Dworu): złoto 0→1, herezja 0→1 | 93.6 → 🟡 ** 86.2** (`🔻 -7.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 86.2 (`🔻 -7.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_G1_H3` | KB-12 (Szantaż Salonowy): złoto 0→1, herezja 2→3 | 93.6 → 🟡 ** 86.2** (`🔻 -7.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 86.2 (`🔻 -7.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_G1_H1` | KB-12 (Szantaż Salonowy): złoto 0→1, herezja 2→1 | 93.6 → 🟡 ** 86.1** (`🔻 -7.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 86.1 (`🔻 -7.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_G1_H2` | SO-10 (Oczyść Miasto): złoto 0→1, herezja 1→2 | 93.6 → 🟡 ** 86.1** (`🔻 -7.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 86.1 (`🔻 -7.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_COST_MINUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 1 | 93.6 → 🟡 ** 86.0** (`🔻 -7.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 86.0 (`🔻 -7.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_C1_H0` | KB-07 (Szantaż Pieczęcią): koszt 2→1, herezja 0→0 | 93.6 → 🟡 ** 86.0** (`🔻 -7.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 86.0 (`🔻 -7.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-12_COST_PLUS2` | KT-12 (Strażnik Archiwum): cost 1 → 3 | 93.6 → 🟡 ** 86.0** (`🔻 -7.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 86.0 (`🔻 -7.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_COST_MINUS2` | KT-06 (Przesłuchanie Imienia): cost 2 → 0 | 93.6 → 🟡 ** 85.9** (`🔻 -7.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 85.9 (`🔻 -7.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_COST_PLUS2` | SO-10 (Oczyść Miasto): cost 5 → 7 | 93.6 → 🟡 ** 85.9** (`🔻 -7.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 85.9 (`🔻 -7.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_COST_MINUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 0 | 93.6 → 🟡 ** 85.8** (`🔻 -7.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 85.8 (`🔻 -7.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_COST_MINUS1` | KB-09 (Dekret Królewski): cost 2 → 1 | 93.6 → 🟡 ** 85.7** (`🔻 -7.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 85.7 (`🔻 -7.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_C1_H0` | KB-09 (Dekret Królewski): koszt 2→1, herezja 0→0 | 93.6 → 🟡 ** 85.7** (`🔻 -7.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 85.7 (`🔻 -7.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_C1_G1` | KT-06 (Przesłuchanie Imienia): koszt 2→1, złoto 0→1 | 93.6 → 🟡 ** 85.7** (`🔻 -7.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 85.7 (`🔻 -7.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_COST_PLUS2` | KB-03 (Plotka Dworska): cost 1 → 3 | 93.6 → 🟡 ** 85.5** (`🔻 -8.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 85.5 (`🔻 -8.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_HERESY_MINUS1` | KT-03 (Zakazana Wiedza): heresy 2 → 1 | 93.6 → 🟡 ** 85.4** (`🔻 -8.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 85.4 (`🔻 -8.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_C0_H1` | KT-03 (Zakazana Wiedza): koszt 0→0, herezja 2→1 | 93.6 → 🟡 ** 85.4** (`🔻 -8.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 85.4 (`🔻 -8.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_G0_H1` | KT-03 (Zakazana Wiedza): złoto 0→0, herezja 2→1 | 93.6 → 🟡 ** 85.4** (`🔻 -8.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 85.4 (`🔻 -8.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_COST_MINUS1` | KT-10 (Pieczęć Salomona): cost 4 → 3 | 93.6 → 🟡 ** 85.4** (`🔻 -8.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 85.4 (`🔻 -8.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_C3_H0` | KT-10 (Pieczęć Salomona): koszt 4→3, herezja 0→0 | 93.6 → 🟡 ** 85.4** (`🔻 -8.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 85.4 (`🔻 -8.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_HERESY_PLUS2` | KB-05 (List Żelazny): heresy 1 → 3 | 93.6 → 🟡 ** 85.3** (`🔻 -8.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 85.3 (`🔻 -8.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_C1_G1` | SO-06 (Areszt Trybunalski): koszt 2→1, złoto 0→1 | 93.6 → 🟡 ** 85.3** (`🔻 -8.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 85.3 (`🔻 -8.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_C2_G2` | KT-05 (Wskazówka Cyklu): koszt 1→2, złoto 0→2 | 93.6 → 🟡 ** 85.2** (`🔻 -8.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 85.2 (`🔻 -8.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_C3_G2` | KB-09 (Dekret Królewski): koszt 2→3, złoto 0→2 | 93.6 → 🟡 ** 85.1** (`🔻 -8.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 85.1 (`🔻 -8.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-12_HERESY_PLUS2` | CAA-12 (Skrytka w Murach): heresy 0 → 2 | 93.6 → 🟡 ** 85.0** (`🔻 -8.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 85.0 (`🔻 -8.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-12_HERESY_SET2` | CAA-12 (Skrytka w Murach): dodaj heresy = 2 | 93.6 → 🟡 ** 85.0** (`🔻 -8.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 85.0 (`🔻 -8.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_HERESY_PLUS2` | GC-04 (Informator): heresy 1 → 3 | 93.6 → 🟡 ** 85.0** (`🔻 -8.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 85.0 (`🔻 -8.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_C0_H3` | KB-12 (Szantaż Salonowy): koszt 1→0, herezja 2→3 | 93.6 → 🟡 ** 85.0** (`🔻 -8.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 85.0 (`🔻 -8.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_G2_H0` | KT-02 (Transmutacja Złota): złoto 3→2, herezja 0→0 | 93.6 → 🟡 ** 85.0** (`🔻 -8.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 85.0 (`🔻 -8.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-11_COST_PLUS1` | KT-11 (Medytacja Sefirot): cost 2 → 3 | 93.6 → 🟡 ** 85.0** (`🔻 -8.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 85.0 (`🔻 -8.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-11_C3_H0` | KT-11 (Medytacja Sefirot): koszt 2→3, herezja 0→0 | 93.6 → 🟡 ** 85.0** (`🔻 -8.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 85.0 (`🔻 -8.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_COST_MINUS2` | SO-06 (Areszt Trybunalski): cost 2 → 0 | 93.6 → 🟡 ** 84.9** (`🔻 -8.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.9 (`🔻 -8.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 93.6 → 🟡 ** 84.8** (`🔻 -8.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.8 (`🔻 -8.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_C0_H0` | CAA-03 (Cień na Rynku): koszt 0→0, herezja 1→0 | 93.6 → 🟡 ** 84.8** (`🔻 -8.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.8 (`🔻 -8.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_C1_H0` | CAA-03 (Cień na Rynku): koszt 0→1, herezja 1→0 | 93.6 → 🟡 ** 84.8** (`🔻 -8.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.8 (`🔻 -8.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_G1_H0` | CAA-03 (Cień na Rynku): złoto 2→1, herezja 1→0 | 93.6 → 🟡 ** 84.8** (`🔻 -8.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.8 (`🔻 -8.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_G3_H0` | CAA-03 (Cień na Rynku): złoto 2→3, herezja 1→0 | 93.6 → 🟡 ** 84.8** (`🔻 -8.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.8 (`🔻 -8.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_G3_H2` | CAA-03 (Cień na Rynku): złoto 2→3, herezja 1→2 | 93.6 → 🟡 ** 84.8** (`🔻 -8.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.8 (`🔻 -8.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_HERESY_MINUS2` | GC-10 (Upadek Domu): heresy 2 → 0 | 93.6 → 🟡 ** 84.8** (`🔻 -8.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.8 (`🔻 -8.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_C1_H1` | KB-06 (Areszt Królewski): koszt 2→1, herezja 0→1 | 93.6 → 🟡 ** 84.8** (`🔻 -8.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.8 (`🔻 -8.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_C2_G1` | KB-03 (Plotka Dworska): koszt 1→2, złoto 0→1 | 93.6 → 🟡 ** 84.7** (`🔻 -8.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.7 (`🔻 -8.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_HERESY_PLUS1` | KT-03 (Zakazana Wiedza): heresy 2 → 3 | 93.6 → 🟡 ** 84.7** (`🔻 -8.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.7 (`🔻 -8.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_C0_H3` | KT-03 (Zakazana Wiedza): koszt 0→0, herezja 2→3 | 93.6 → 🟡 ** 84.7** (`🔻 -8.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.7 (`🔻 -8.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_G0_H3` | KT-03 (Zakazana Wiedza): złoto 0→0, herezja 2→3 | 93.6 → 🟡 ** 84.7** (`🔻 -8.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.7 (`🔻 -8.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_C0_G1` | KT-07 (Archiwum Ukryte): koszt 1→0, złoto 0→1 | 93.6 → 🟡 ** 84.7** (`🔻 -8.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.7 (`🔻 -8.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_HERESY_PLUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 2 | 93.6 → 🟡 ** 84.7** (`🔻 -8.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.7 (`🔻 -8.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_G0_H2` | KT-09 (Fragment Kodeksu): złoto 0→0, herezja 1→2 | 93.6 → 🟡 ** 84.7** (`🔻 -8.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.7 (`🔻 -8.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_COST_MINUS1` | KB-05 (List Żelazny): cost 2 → 1 | 93.6 → 🟡 ** 84.6** (`🔻 -9.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.6 (`🔻 -9.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_C1_H0` | KB-05 (List Żelazny): koszt 2→1, herezja 1→0 | 93.6 → 🟡 ** 84.6** (`🔻 -9.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.6 (`🔻 -9.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-11_COST_MINUS1` | KB-11 (Tajny Emisariusz): cost 1 → 0 | 93.6 → 🟡 ** 84.5** (`🔻 -9.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.5 (`🔻 -9.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-11_C0_H0` | KB-11 (Tajny Emisariusz): koszt 1→0, herezja 0→0 | 93.6 → 🟡 ** 84.5** (`🔻 -9.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.5 (`🔻 -9.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_COST_PLUS2` | KT-09 (Fragment Kodeksu): cost 1 → 3 | 93.6 → 🟡 ** 84.5** (`🔻 -9.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.5 (`🔻 -9.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_HERESY_PLUS1` | CAA-05 (Ukryty Kurier): heresy 0 → 1 | 93.6 → 🟡 ** 84.4** (`🔻 -9.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.4 (`🔻 -9.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_HERESY_SET1` | CAA-05 (Ukryty Kurier): dodaj heresy = 1 | 93.6 → 🟡 ** 84.4** (`🔻 -9.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.4 (`🔻 -9.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_C0_H1` | CAA-05 (Ukryty Kurier): koszt 0→0, herezja 0→1 | 93.6 → 🟡 ** 84.4** (`🔻 -9.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.4 (`🔻 -9.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_C1_H1` | CAA-05 (Ukryty Kurier): koszt 0→1, herezja 0→1 | 93.6 → 🟡 ** 84.4** (`🔻 -9.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.4 (`🔻 -9.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_G3_H1` | CAA-05 (Ukryty Kurier): złoto 4→3, herezja 0→1 | 93.6 → 🟡 ** 84.4** (`🔻 -9.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.4 (`🔻 -9.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_G5_H1` | CAA-05 (Ukryty Kurier): złoto 4→5, herezja 0→1 | 93.6 → 🟡 ** 84.4** (`🔻 -9.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.4 (`🔻 -9.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_C2_G2` | KB-01 (Rozkaz Dworu): koszt 1→2, złoto 0→2 | 93.6 → 🟡 ** 84.4** (`🔻 -9.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.4 (`🔻 -9.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_C4_H2` | SO-10 (Oczyść Miasto): koszt 5→4, herezja 1→2 | 93.6 → 🟡 ** 84.4** (`🔻 -9.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.4 (`🔻 -9.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_C5_H1` | KT-10 (Pieczęć Salomona): koszt 4→5, herezja 0→1 | 93.6 → 🟡 ** 84.2** (`🔻 -9.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.2 (`🔻 -9.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_COST_PLUS2` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 3 | 93.6 → 🟡 ** 84.2** (`🔻 -9.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.2 (`🔻 -9.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_HERESY_MINUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 0 | 93.6 → 🟡 ** 84.1** (`🔻 -9.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.1 (`🔻 -9.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_G0_H0` | KT-09 (Fragment Kodeksu): złoto 0→0, herezja 1→0 | 93.6 → 🟡 ** 84.1** (`🔻 -9.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.1 (`🔻 -9.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_HERESY_PLUS1` | SO-10 (Oczyść Miasto): heresy 1 → 2 | 93.6 → 🟡 ** 84.1** (`🔻 -9.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.1 (`🔻 -9.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_G0_H2` | SO-10 (Oczyść Miasto): złoto 0→0, herezja 1→2 | 93.6 → 🟡 ** 84.1** (`🔻 -9.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.1 (`🔻 -9.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_HERESY_PLUS2` | CAA-04 (Fałszywy Trop): heresy 0 → 2 | 93.6 → 🟡 ** 84.0** (`🔻 -9.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.0 (`🔻 -9.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_HERESY_SET2` | CAA-04 (Fałszywy Trop): dodaj heresy = 2 | 93.6 → 🟡 ** 84.0** (`🔻 -9.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.0 (`🔻 -9.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_G4_H1` | CAA-04 (Fałszywy Trop): złoto 3→4, herezja 0→1 | 93.6 → 🟡 ** 84.0** (`🔻 -9.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 84.0 (`🔻 -9.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_C0_G2` | CAA-06 (Ucieczka z Lochów): koszt 0→0, złoto 0→2 | 93.6 → 🟡 ** 83.9** (`🔻 -9.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 83.9 (`🔻 -9.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-01_C1_G2` | CAA-01 (Przejście Podziemiami): koszt 2→1, złoto 0→2 | 93.6 → 🟡 ** 83.8** (`🔻 -9.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 83.8 (`🔻 -9.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_C0_H0` | KB-01 (Rozkaz Dworu): koszt 1→0, herezja 1→0 | 93.6 → 🟡 ** 83.8** (`🔻 -9.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 83.8 (`🔻 -9.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_HERESY_PLUS2` | CAA-03 (Cień na Rynku): heresy 1 → 3 | 93.6 → 🟡 ** 83.7** (`🔻 -9.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 83.7 (`🔻 -9.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_C0_H0` | KT-09 (Fragment Kodeksu): koszt 1→0, herezja 1→0 | 93.6 → 🟡 ** 83.7** (`🔻 -9.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 83.7 (`🔻 -9.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-11_COST_MINUS1` | KT-11 (Medytacja Sefirot): cost 2 → 1 | 93.6 → 🟡 ** 83.7** (`🔻 -9.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 83.7 (`🔻 -9.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-11_C1_H0` | KT-11 (Medytacja Sefirot): koszt 2→1, herezja 0→0 | 93.6 → 🟡 ** 83.7** (`🔻 -9.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 83.7 (`🔻 -9.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_C3_G1` | KT-10 (Pieczęć Salomona): koszt 4→3, złoto 0→1 | 93.6 → 🟡 ** 83.6** (`🔻 -10.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 83.6 (`🔻 -10.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-11_G2_H1` | KT-11 (Medytacja Sefirot): złoto 1→2, herezja 0→1 | 93.6 → 🟡 ** 83.6** (`🔻 -10.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 83.6 (`🔻 -10.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_G1_H2` | KB-03 (Plotka Dworska): złoto 0→1, herezja 1→2 | 93.6 → 🟡 ** 83.5** (`🔻 -10.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 83.5 (`🔻 -10.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_C6_H2` | SO-10 (Oczyść Miasto): koszt 5→6, herezja 1→2 | 93.6 → 🟡 ** 83.4** (`🔻 -10.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 83.4 (`🔻 -10.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_COST_PLUS1` | GC-10 (Upadek Domu): cost 4 → 5 | 93.6 → 🟡 ** 83.3** (`🔻 -10.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 83.3 (`🔻 -10.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_G1_H0` | KB-06 (Areszt Królewski): złoto 0→1, herezja 0→0 | 93.6 → 🟡 ** 83.2** (`🔻 -10.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 83.2 (`🔻 -10.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_COST_MINUS1` | KB-12 (Szantaż Salonowy): cost 1 → 0 | 93.6 → 🟡 ** 83.2** (`🔻 -10.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 83.2 (`🔻 -10.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_C3_G2` | KT-10 (Pieczęć Salomona): koszt 4→3, złoto 0→2 | 93.6 → 🟡 ** 83.2** (`🔻 -10.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 83.2 (`🔻 -10.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_C0_G5` | KT-02 (Transmutacja Złota): koszt 0→0, złoto 3→5 | 93.6 → 🟡 ** 83.1** (`🔻 -10.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 83.1 (`🔻 -10.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-11_C1_H1` | KT-11 (Medytacja Sefirot): koszt 2→1, herezja 0→1 | 93.6 → 🟡 ** 83.1** (`🔻 -10.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 83.1 (`🔻 -10.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_G1_H1` | CAA-09 (Kurier Relikwii): złoto 0→1, herezja 0→1 | 93.6 → 🟡 ** 83.0** (`🔻 -10.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 83.0 (`🔻 -10.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_G1_H1` | KB-07 (Szantaż Pieczęcią): złoto 0→1, herezja 0→1 | 93.6 → 🟡 ** 83.0** (`🔻 -10.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 83.0 (`🔻 -10.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_HERESY_PLUS1` | KB-12 (Szantaż Salonowy): heresy 2 → 3 | 93.6 → 🟡 ** 82.9** (`🔻 -10.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 82.9 (`🔻 -10.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_G0_H3` | KB-12 (Szantaż Salonowy): złoto 0→0, herezja 2→3 | 93.6 → 🟡 ** 82.9** (`🔻 -10.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 82.9 (`🔻 -10.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_HERESY_PLUS1` | KT-05 (Wskazówka Cyklu): heresy 1 → 2 | 93.6 → 🟡 ** 82.5** (`🔻 -11.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 82.5 (`🔻 -11.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_G0_H2` | KT-05 (Wskazówka Cyklu): złoto 0→0, herezja 1→2 | 93.6 → 🟡 ** 82.5** (`🔻 -11.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 82.5 (`🔻 -11.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_G1_H0` | KT-09 (Fragment Kodeksu): złoto 0→1, herezja 1→0 | 93.6 → 🟡 ** 82.5** (`🔻 -11.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 82.5 (`🔻 -11.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_G1_H1` | CAA-06 (Ucieczka z Lochów): złoto 0→1, herezja 0→1 | 93.6 → 🟡 ** 82.4** (`🔻 -11.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 82.4 (`🔻 -11.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-11_G1_H1` | KB-11 (Tajny Emisariusz): złoto 0→1, herezja 0→1 | 93.6 → 🟡 ** 82.2** (`🔻 -11.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 82.2 (`🔻 -11.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_C1_H1` | CAA-10 (Echo Alhambry): koszt 2→1, herezja 0→1 | 93.6 → 🟡 ** 82.1** (`🔻 -11.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 82.1 (`🔻 -11.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_G1_H1` | CAA-10 (Echo Alhambry): złoto 0→1, herezja 0→1 | 93.6 → 🟡 ** 82.1** (`🔻 -11.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 82.1 (`🔻 -11.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_C0_G2` | KT-03 (Zakazana Wiedza): koszt 0→0, złoto 0→2 | 93.6 → 🟡 ** 81.8** (`🔻 -11.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 81.8 (`🔻 -11.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_G1_H0` | KB-09 (Dekret Królewski): złoto 0→1, herezja 0→0 | 93.6 → 🟡 ** 81.7** (`🔻 -11.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 81.7 (`🔻 -11.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-12_C0_G1` | KT-12 (Strażnik Archiwum): koszt 1→0, złoto 0→1 | 93.6 → 🟡 ** 81.7** (`🔻 -11.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 81.7 (`🔻 -11.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_HERESY_PLUS1` | GC-10 (Upadek Domu): heresy 2 → 3 | 93.6 → 🟡 ** 81.6** (`🔻 -12.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 81.6 (`🔻 -12.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_G0_H3` | GC-10 (Upadek Domu): złoto 0→0, herezja 2→3 | 93.6 → 🟡 ** 81.6** (`🔻 -12.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 81.6 (`🔻 -12.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_C3_H3` | GC-10 (Upadek Domu): koszt 4→3, herezja 2→3 | 93.6 → 🟡 ** 81.5** (`🔻 -12.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 81.5 (`🔻 -12.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_G1_H2` | KB-05 (List Żelazny): złoto 0→1, herezja 1→2 | 93.6 → 🟡 ** 81.5** (`🔻 -12.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 81.5 (`🔻 -12.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_G1_H3` | GC-10 (Upadek Domu): złoto 0→1, herezja 2→3 | 93.6 → 🟡 ** 81.4** (`🔻 -12.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 81.4 (`🔻 -12.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_C2_G2` | KB-08 (Przekupstwo Sędziego): koszt 3→2, złoto 0→2 | 93.6 → 🟡 ** 81.3** (`🔻 -12.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 81.3 (`🔻 -12.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_C1_G2` | SO-06 (Areszt Trybunalski): koszt 2→1, złoto 0→2 | 93.6 → 🟡 ** 81.3** (`🔻 -12.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 81.3 (`🔻 -12.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_COST_PLUS2` | GC-10 (Upadek Domu): cost 4 → 6 | 93.6 → 🟡 ** 80.9** (`🔻 -12.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 80.9 (`🔻 -12.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_HERESY_PLUS1` | CAA-10 (Echo Alhambry): heresy 0 → 1 | 93.6 → 🟡 ** 80.5** (`🔻 -13.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 80.5 (`🔻 -13.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_HERESY_SET1` | CAA-10 (Echo Alhambry): dodaj heresy = 1 | 93.6 → 🟡 ** 80.5** (`🔻 -13.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 80.5 (`🔻 -13.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_G0_H1` | CAA-10 (Echo Alhambry): złoto 0→0, herezja 0→1 | 93.6 → 🟡 ** 80.5** (`🔻 -13.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 80.5 (`🔻 -13.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_COST_PLUS2` | KB-06 (Areszt Królewski): cost 2 → 4 | 93.6 → 🟡 ** 80.5** (`🔻 -13.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 80.5 (`🔻 -13.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_HERESY_MINUS1` | KT-05 (Wskazówka Cyklu): heresy 1 → 0 | 93.6 → 🟡 ** 80.3** (`🔻 -13.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 80.3 (`🔻 -13.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_G0_H0` | KT-05 (Wskazówka Cyklu): złoto 0→0, herezja 1→0 | 93.6 → 🟡 ** 80.3** (`🔻 -13.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 80.3 (`🔻 -13.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_C5_H3` | GC-10 (Upadek Domu): koszt 4→5, herezja 2→3 | 93.6 → 🟡 ** 80.2** (`🔻 -13.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 80.2 (`🔻 -13.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-04_C0_G1` | KT-04 (Zwierciadło Herezji): koszt 1→0, złoto 0→1 | 93.6 → 🟡 ** 80.2** (`🔻 -13.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 80.2 (`🔻 -13.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_C0_G1` | KT-05 (Wskazówka Cyklu): koszt 1→0, złoto 0→1 | 93.6 → 🟡 ** 80.0** (`🔻 -13.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 80.0 (`🔻 -13.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_G1_H0` | KB-07 (Szantaż Pieczęcią): złoto 0→1, herezja 0→0 | 93.6 → 🟠 ** 79.9** (`🔻 -13.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 79.9 (`🔻 -13.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_HERESY_PLUS2` | GC-10 (Upadek Domu): heresy 2 → 4 | 93.6 → 🟠 ** 79.7** (`🔻 -13.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 79.7 (`🔻 -13.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_C0_G1` | KT-08 (Areszt Wiedzy): koszt 1→0, złoto 0→1 | 93.6 → 🟠 ** 79.6** (`🔻 -14.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 79.6 (`🔻 -14.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_G1_H0` | KB-05 (List Żelazny): złoto 0→1, herezja 1→0 | 93.6 → 🟠 ** 79.5** (`🔻 -14.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 79.5 (`🔻 -14.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_COST_PLUS2` | KT-03 (Zakazana Wiedza): cost 0 → 2 | 93.6 → 🟠 ** 79.5** (`🔻 -14.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 79.5 (`🔻 -14.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-11_C1_G2` | KT-11 (Medytacja Sefirot): koszt 2→1, złoto 1→2 | 93.6 → 🟠 ** 79.4** (`🔻 -14.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 79.4 (`🔻 -14.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_HERESY_PLUS1` | CAA-06 (Ucieczka z Lochów): heresy 0 → 1 | 93.6 → 🟠 ** 78.9** (`🔻 -14.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 78.9 (`🔻 -14.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_HERESY_SET1` | CAA-06 (Ucieczka z Lochów): dodaj heresy = 1 | 93.6 → 🟠 ** 78.9** (`🔻 -14.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 78.9 (`🔻 -14.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_C0_H1` | CAA-06 (Ucieczka z Lochów): koszt 0→0, herezja 0→1 | 93.6 → 🟠 ** 78.9** (`🔻 -14.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 78.9 (`🔻 -14.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_G0_H1` | CAA-06 (Ucieczka z Lochów): złoto 0→0, herezja 0→1 | 93.6 → 🟠 ** 78.9** (`🔻 -14.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 78.9 (`🔻 -14.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_C3_G2` | KB-07 (Szantaż Pieczęcią): koszt 2→3, złoto 0→2 | 93.6 → 🟠 ** 78.9** (`🔻 -14.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 78.9 (`🔻 -14.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_C0_H0` | KB-03 (Plotka Dworska): koszt 1→0, herezja 1→0 | 93.6 → 🟠 ** 78.8** (`🔻 -14.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 78.8 (`🔻 -14.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_HERESY_PLUS1` | KB-06 (Areszt Królewski): heresy 0 → 1 | 93.6 → 🟠 ** 78.5** (`🔻 -15.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 78.5 (`🔻 -15.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_HERESY_SET1` | KB-06 (Areszt Królewski): dodaj heresy = 1 | 93.6 → 🟠 ** 78.5** (`🔻 -15.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 78.5 (`🔻 -15.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_G0_H1` | KB-06 (Areszt Królewski): złoto 0→0, herezja 0→1 | 93.6 → 🟠 ** 78.5** (`🔻 -15.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 78.5 (`🔻 -15.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_C2_H2` | KT-09 (Fragment Kodeksu): koszt 1→2, herezja 1→2 | 93.6 → 🟠 ** 78.5** (`🔻 -15.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 78.5 (`🔻 -15.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_COST_PLUS2` | KT-05 (Wskazówka Cyklu): cost 1 → 3 | 93.6 → 🟠 ** 78.3** (`🔻 -15.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 78.3 (`🔻 -15.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_C1_G2` | KT-06 (Przesłuchanie Imienia): koszt 2→1, złoto 0→2 | 93.6 → 🟠 ** 78.2** (`🔻 -15.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 78.2 (`🔻 -15.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_G1_H0` | KB-04 (Faworyt Dworu): złoto 0→1, herezja 0→0 | 93.6 → 🟠 ** 77.7** (`🔻 -15.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 77.7 (`🔻 -15.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_C2_H2` | KT-05 (Wskazówka Cyklu): koszt 1→2, herezja 1→2 | 93.6 → 🟠 ** 77.4** (`🔻 -16.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 77.4 (`🔻 -16.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_C3_H1` | CAA-10 (Echo Alhambry): koszt 2→3, herezja 0→1 | 93.6 → 🟠 ** 77.0** (`🔻 -16.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 77.0 (`🔻 -16.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_COST_MINUS2` | KT-10 (Pieczęć Salomona): cost 4 → 2 | 93.6 → 🟠 ** 76.9** (`🔻 -16.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 76.9 (`🔻 -16.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_C0_G2` | KT-07 (Archiwum Ukryte): koszt 1→0, złoto 0→2 | 93.6 → 🟠 ** 76.8** (`🔻 -16.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 76.8 (`🔻 -16.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-12_C0_G2` | KT-12 (Strażnik Archiwum): koszt 1→0, złoto 0→2 | 93.6 → 🟠 ** 76.7** (`🔻 -16.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 76.7 (`🔻 -16.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_G1_H1` | KT-03 (Zakazana Wiedza): złoto 0→1, herezja 2→1 | 93.6 → 🟠 ** 76.5** (`🔻 -17.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 76.5 (`🔻 -17.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_G1_H1` | KB-06 (Areszt Królewski): złoto 0→1, herezja 0→1 | 93.6 → 🟠 ** 76.3** (`🔻 -17.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 76.3 (`🔻 -17.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_C1_H3` | KT-03 (Zakazana Wiedza): koszt 0→1, herezja 2→3 | 93.6 → 🟠 ** 76.2** (`🔻 -17.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 76.2 (`🔻 -17.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_HERESY_PLUS1` | KT-02 (Transmutacja Złota): heresy 0 → 1 | 93.6 → 🟠 ** 75.9** (`🔻 -17.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 75.9 (`🔻 -17.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_HERESY_SET1` | KT-02 (Transmutacja Złota): dodaj heresy = 1 | 93.6 → 🟠 ** 75.9** (`🔻 -17.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 75.9 (`🔻 -17.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_C0_H1` | KT-02 (Transmutacja Złota): koszt 0→0, herezja 0→1 | 93.6 → 🟠 ** 75.9** (`🔻 -17.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 75.9 (`🔻 -17.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_C1_H1` | CAA-06 (Ucieczka z Lochów): koszt 0→1, herezja 0→1 | 93.6 → 🟠 ** 75.8** (`🔻 -17.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 75.8 (`🔻 -17.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-11_G1_H0` | KB-11 (Tajny Emisariusz): złoto 0→1, herezja 0→0 | 93.6 → 🟠 ** 75.6** (`🔻 -18.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 75.6 (`🔻 -18.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-11_COST_MINUS2` | KT-11 (Medytacja Sefirot): cost 2 → 0 | 93.6 → 🟠 ** 75.4** (`🔻 -18.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 75.4 (`🔻 -18.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_C0_G2` | KT-08 (Areszt Wiedzy): koszt 1→0, złoto 0→2 | 93.6 → 🟠 ** 75.2** (`🔻 -18.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 75.2 (`🔻 -18.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_HERESY_PLUS2` | KB-06 (Areszt Królewski): heresy 0 → 2 | 93.6 → 🟠 ** 75.1** (`🔻 -18.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 75.1 (`🔻 -18.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_HERESY_SET2` | KB-06 (Areszt Królewski): dodaj heresy = 2 | 93.6 → 🟠 ** 75.1** (`🔻 -18.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 75.1 (`🔻 -18.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_C3_H1` | KB-06 (Areszt Królewski): koszt 2→3, herezja 0→1 | 93.6 → 🟠 ** 75.1** (`🔻 -18.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 75.1 (`🔻 -18.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_G1_H0` | KB-01 (Rozkaz Dworu): złoto 0→1, herezja 1→0 | 93.6 → 🟠 ** 75.0** (`🔻 -18.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 75.0 (`🔻 -18.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_G3_H1` | KB-02 (Pobór Podatków): złoto 2→3, herezja 0→1 | 93.6 → 🟠 ** 74.9** (`🔻 -18.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 74.9 (`🔻 -18.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_C0_G2` | KT-05 (Wskazówka Cyklu): koszt 1→0, złoto 0→2 | 93.6 → 🟠 ** 74.8** (`🔻 -18.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 74.8 (`🔻 -18.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_COST_PLUS2` | KT-10 (Pieczęć Salomona): cost 4 → 6 | 93.6 → 🟠 ** 74.8** (`🔻 -18.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 74.8 (`🔻 -18.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_COST_MINUS2` | KB-06 (Areszt Królewski): cost 2 → 0 | 93.6 → 🟠 ** 74.7** (`🔻 -18.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 74.7 (`🔻 -18.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_HERESY_PLUS2` | KB-02 (Pobór Podatków): heresy 0 → 2 | 93.6 → 🟠 ** 74.3** (`🔻 -19.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 74.3 (`🔻 -19.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_HERESY_SET2` | KB-02 (Pobór Podatków): dodaj heresy = 2 | 93.6 → 🟠 ** 74.3** (`🔻 -19.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 74.3 (`🔻 -19.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-11_C1_G3` | KT-11 (Medytacja Sefirot): koszt 2→1, złoto 1→3 | 93.6 → 🟠 ** 74.1** (`🔻 -19.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 74.1 (`🔻 -19.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_HERESY_PLUS2` | KB-09 (Dekret Królewski): heresy 0 → 2 | 93.6 → 🟠 ** 73.9** (`🔻 -19.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 73.9 (`🔻 -19.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_HERESY_SET2` | KB-09 (Dekret Królewski): dodaj heresy = 2 | 93.6 → 🟠 ** 73.9** (`🔻 -19.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 73.9 (`🔻 -19.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_HERESY_MINUS2` | KT-03 (Zakazana Wiedza): heresy 2 → 0 | 93.6 → 🟠 ** 73.7** (`🔻 -19.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 73.7 (`🔻 -19.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_HERESY_PLUS2` | KT-03 (Zakazana Wiedza): heresy 2 → 4 | 93.6 → 🟠 ** 73.6** (`🔻 -20.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 73.6 (`🔻 -20.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_HERESY_PLUS2` | KT-09 (Fragment Kodeksu): heresy 1 → 3 | 93.6 → 🟠 ** 73.4** (`🔻 -20.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 73.4 (`🔻 -20.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-11_HERESY_PLUS1` | KT-11 (Medytacja Sefirot): heresy 0 → 1 | 93.6 → 🟠 ** 73.3** (`🔻 -20.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 73.3 (`🔻 -20.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-11_HERESY_SET1` | KT-11 (Medytacja Sefirot): dodaj heresy = 1 | 93.6 → 🟠 ** 73.3** (`🔻 -20.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 73.3 (`🔻 -20.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_HERESY_PLUS2` | CAA-06 (Ucieczka z Lochów): heresy 0 → 2 | 93.6 → 🟠 ** 72.5** (`🔻 -21.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 72.5 (`🔻 -21.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_HERESY_SET2` | CAA-06 (Ucieczka z Lochów): dodaj heresy = 2 | 93.6 → 🟠 ** 72.5** (`🔻 -21.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 72.5 (`🔻 -21.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_C3_G2` | KB-06 (Areszt Królewski): koszt 2→3, złoto 0→2 | 93.6 → 🟠 ** 72.4** (`🔻 -21.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 72.4 (`🔻 -21.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-04_C0_G2` | KT-04 (Zwierciadło Herezji): koszt 1→0, złoto 0→2 | 93.6 → 🟠 ** 72.4** (`🔻 -21.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 72.4 (`🔻 -21.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_HERESY_PLUS2` | CAA-05 (Ukryty Kurier): heresy 0 → 2 | 93.6 → 🟠 ** 72.2** (`🔻 -21.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 72.2 (`🔻 -21.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_HERESY_SET2` | CAA-05 (Ukryty Kurier): dodaj heresy = 2 | 93.6 → 🟠 ** 72.2** (`🔻 -21.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 72.2 (`🔻 -21.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_HERESY_PLUS2` | KT-05 (Wskazówka Cyklu): heresy 1 → 3 | 93.6 → 🟠 ** 72.0** (`🔻 -21.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 72.0 (`🔻 -21.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_C3_G2` | KB-05 (List Żelazny): koszt 2→3, złoto 0→2 | 93.6 → 🟠 ** 71.9** (`🔻 -21.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 71.9 (`🔻 -21.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-11_COST_PLUS2` | KT-11 (Medytacja Sefirot): cost 2 → 4 | 93.6 → 🟠 ** 71.9** (`🔻 -21.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 71.9 (`🔻 -21.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_G1_H0` | KB-03 (Plotka Dworska): złoto 0→1, herezja 1→0 | 93.6 → 🟠 ** 71.4** (`🔻 -22.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 71.4 (`🔻 -22.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_C3_G2` | KB-04 (Faworyt Dworu): koszt 2→3, złoto 0→2 | 93.6 → 🟠 ** 69.8** (`🔻 -23.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 69.8 (`🔻 -23.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_COST_MINUS2` | KB-07 (Szantaż Pieczęcią): cost 2 → 0 | 93.6 → 🟠 ** 69.7** (`🔻 -23.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 69.7 (`🔻 -23.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_G1_H0` | KT-05 (Wskazówka Cyklu): złoto 0→1, herezja 1→0 | 93.6 → 🟠 ** 69.7** (`🔻 -23.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 69.7 (`🔻 -23.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_C2_H1` | KB-02 (Pobór Podatków): koszt 1→2, herezja 0→1 | 93.6 → 🟠 ** 69.5** (`🔻 -24.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 69.5 (`🔻 -24.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_C0_H0` | KT-05 (Wskazówka Cyklu): koszt 1→0, herezja 1→0 | 93.6 → 🟠 ** 69.4** (`🔻 -24.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 69.4 (`🔻 -24.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_COST_MINUS2` | KB-09 (Dekret Królewski): cost 2 → 0 | 93.6 → 🟠 ** 68.9** (`🔻 -24.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 68.9 (`🔻 -24.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_C2_G2` | KB-03 (Plotka Dworska): koszt 1→2, złoto 0→2 | 93.6 → 🟠 ** 68.6** (`🔻 -25.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 68.6 (`🔻 -25.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_COST_PLUS1` | KB-09 (Dekret Królewski): cost 2 → 3 | 93.6 → 🟠 ** 68.4** (`🔻 -25.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 68.4 (`🔻 -25.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_C3_H0` | KB-09 (Dekret Królewski): koszt 2→3, herezja 0→0 | 93.6 → 🟠 ** 68.4** (`🔻 -25.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 68.4 (`🔻 -25.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_C3_H1` | KB-09 (Dekret Królewski): koszt 2→3, herezja 0→1 | 93.6 → 🟠 ** 68.2** (`🔻 -25.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 68.2 (`🔻 -25.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-11_G0_H1` | KT-11 (Medytacja Sefirot): złoto 1→0, herezja 0→1 | 93.6 → 🟠 ** 67.8** (`🔻 -25.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 67.8 (`🔻 -25.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-11_C3_H1` | KT-11 (Medytacja Sefirot): koszt 2→3, herezja 0→1 | 93.6 → 🟠 ** 67.2** (`🔻 -26.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 67.2 (`🔻 -26.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_COST_MINUS2` | KB-04 (Faworyt Dworu): cost 2 → 0 | 93.6 → 🟠 ** 66.8** (`🔻 -26.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 66.8 (`🔻 -26.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_C0_G1` | KB-01 (Rozkaz Dworu): koszt 1→0, złoto 0→1 | 93.6 → 🟠 ** 66.3** (`🔻 -27.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 66.3 (`🔻 -27.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_HERESY_PLUS2` | KB-10 (Pieczęć Korony): heresy 1 → 3 | 93.6 → 🟠 ** 65.9** (`🔻 -27.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 65.9 (`🔻 -27.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_C0_G1` | KB-03 (Plotka Dworska): koszt 1→0, złoto 0→1 | 93.6 → 🟠 ** 65.8** (`🔻 -27.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 65.8 (`🔻 -27.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_G3_H0` | KB-02 (Pobór Podatków): złoto 2→3, herezja 0→0 | 93.6 → 🟠 ** 65.6** (`🔻 -28.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 65.6 (`🔻 -28.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_G1_H0` | KB-02 (Pobór Podatków): złoto 2→1, herezja 0→0 | 93.6 → 🔴 ** 64.9** (`🔻 -28.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 64.9 (`🔻 -28.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_COST_PLUS2` | KT-02 (Transmutacja Złota): cost 0 → 2 | 93.6 → 🔴 ** 64.5** (`🔻 -29.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 64.5 (`🔻 -29.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_C2_G2` | KB-12 (Szantaż Salonowy): koszt 1→2, złoto 0→2 | 93.6 → 🔴 ** 63.1** (`🔻 -30.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 63.1 (`🔻 -30.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_C5_G4` | KB-10 (Pieczęć Korony): koszt 4→5, złoto 2→4 | 93.6 → 🔴 ** 62.9** (`🔻 -30.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 62.9 (`🔻 -30.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_C1_G1` | KB-06 (Areszt Królewski): koszt 2→1, złoto 0→1 | 93.6 → 🔴 ** 62.8** (`🔻 -30.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 62.8 (`🔻 -30.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_C5_H0` | KB-10 (Pieczęć Korony): koszt 4→5, herezja 1→0 | 93.6 → 🔴 ** 62.6** (`🔻 -31.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 62.6 (`🔻 -31.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_C1_G1` | KB-07 (Szantaż Pieczęcią): koszt 2→1, złoto 0→1 | 93.6 → 🔴 ** 62.5** (`🔻 -31.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 62.5 (`🔻 -31.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_C1_H1` | KT-02 (Transmutacja Złota): koszt 0→1, herezja 0→1 | 93.6 → 🔴 ** 62.2** (`🔻 -31.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 62.2 (`🔻 -31.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_G2_H1` | KT-02 (Transmutacja Złota): złoto 3→2, herezja 0→1 | 93.6 → 🔴 ** 62.2** (`🔻 -31.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 62.2 (`🔻 -31.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-11_HERESY_PLUS2` | KT-11 (Medytacja Sefirot): heresy 0 → 2 | 93.6 → 🔴 ** 62.2** (`🔻 -31.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 62.2 (`🔻 -31.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-11_HERESY_SET2` | KT-11 (Medytacja Sefirot): dodaj heresy = 2 | 93.6 → 🔴 ** 62.2** (`🔻 -31.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 62.2 (`🔻 -31.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_C1_G1` | KB-09 (Dekret Królewski): koszt 2→1, złoto 0→1 | 93.6 → 🔴 ** 62.1** (`🔻 -31.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 62.1 (`🔻 -31.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_C2_G3` | KB-02 (Pobór Podatków): koszt 1→2, złoto 2→3 | 93.6 → 🔴 ** 62.0** (`🔻 -31.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 62.0 (`🔻 -31.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_C5_G3` | KB-10 (Pieczęć Korony): koszt 4→5, złoto 2→3 | 93.6 → 🔴 ** 61.9** (`🔻 -31.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 61.9 (`🔻 -31.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_COST_PLUS1` | KB-10 (Pieczęć Korony): cost 4 → 5 | 93.6 → 🔴 ** 60.8** (`🔻 -32.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 60.8 (`🔻 -32.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-11_C0_G1` | KB-11 (Tajny Emisariusz): koszt 1→0, złoto 0→1 | 93.6 → 🔴 ** 60.7** (`🔻 -32.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 60.7 (`🔻 -32.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_C1_G1` | KB-04 (Faworyt Dworu): koszt 2→1, złoto 0→1 | 93.6 → 🔴 ** 60.6** (`🔻 -33.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 60.6 (`🔻 -33.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_COST_MINUS2` | KB-05 (List Żelazny): cost 2 → 0 | 93.6 → 🔴 ** 60.6** (`🔻 -33.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 60.6 (`🔻 -33.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_G1_H1` | KB-02 (Pobór Podatków): złoto 2→1, herezja 0→1 | 93.6 → 🔴 ** 60.1** (`🔻 -33.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 60.1 (`🔻 -33.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_C5_H2` | KB-10 (Pieczęć Korony): koszt 4→5, herezja 1→2 | 93.6 → 🔴 ** 59.6** (`🔻 -34.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 59.6 (`🔻 -34.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-11_C2_G2` | KB-11 (Tajny Emisariusz): koszt 1→2, złoto 0→2 | 93.6 → 🔴 ** 59.3** (`🔻 -34.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 59.3 (`🔻 -34.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_C1_G1` | KB-05 (List Żelazny): koszt 2→1, złoto 0→1 | 93.6 → 🔴 ** 58.8** (`🔻 -34.8`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 58.8 (`🔻 -34.8`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_COST_PLUS2` | KB-02 (Pobór Podatków): cost 1 → 3 | 93.6 → 🔴 ** 58.7** (`🔻 -34.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 58.7 (`🔻 -34.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_C0_G3` | KB-02 (Pobór Podatków): koszt 1→0, złoto 2→3 | 93.6 → 🔴 ** 56.0** (`🔻 -37.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 56.0 (`🔻 -37.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_HERESY_PLUS2` | KT-02 (Transmutacja Złota): heresy 0 → 2 | 93.6 → 🔴 ** 55.2** (`🔻 -38.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 55.2 (`🔻 -38.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_HERESY_SET2` | KT-02 (Transmutacja Złota): dodaj heresy = 2 | 93.6 → 🔴 ** 55.2** (`🔻 -38.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 55.2 (`🔻 -38.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_C0_G1` | KB-12 (Szantaż Salonowy): koszt 1→0, złoto 0→1 | 93.6 → 🔴 ** 54.7** (`🔻 -38.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 54.7 (`🔻 -38.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_C2_G4` | KB-02 (Pobór Podatków): koszt 1→2, złoto 2→4 | 93.6 → 🔴 ** 53.6** (`🔻 -40.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 53.6 (`🔻 -40.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_HERESY_PLUS2` | CAA-10 (Echo Alhambry): heresy 0 → 2 | 93.6 → 🔴 ** 51.7** (`🔻 -41.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 51.7 (`🔻 -41.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_HERESY_SET2` | CAA-10 (Echo Alhambry): dodaj heresy = 2 | 93.6 → 🔴 ** 51.7** (`🔻 -41.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 51.7 (`🔻 -41.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_COST_PLUS2` | KB-10 (Pieczęć Korony): cost 4 → 6 | 93.6 → 🔴 ** 50.5** (`🔻 -43.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 50.5 (`🔻 -43.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_COST_PLUS2` | KB-09 (Dekret Królewski): cost 2 → 4 | 93.6 → 🔴 ** 48.0** (`🔻 -45.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 48.0 (`🔻 -45.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_C3_H2` | KB-10 (Pieczęć Korony): koszt 4→3, herezja 1→2 | 93.6 → 🔴 ** 47.5** (`🔻 -46.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 47.5 (`🔻 -46.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_C0_G2` | KB-01 (Rozkaz Dworu): koszt 1→0, złoto 0→2 | 93.6 → 🔴 ** 44.7** (`🔻 -48.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 44.7 (`🔻 -48.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_C0_G2` | KB-03 (Plotka Dworska): koszt 1→0, złoto 0→2 | 93.6 → 🔴 ** 44.0** (`🔻 -49.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 44.0 (`🔻 -49.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-11_C0_G2` | KB-11 (Tajny Emisariusz): koszt 1→0, złoto 0→2 | 93.6 → 🔴 ** 40.0** (`🔻 -53.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 40.0 (`🔻 -53.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_COST_MINUS1` | KB-10 (Pieczęć Korony): cost 4 → 3 | 93.6 → 🔴 ** 39.0** (`🔻 -54.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 39.0 (`🔻 -54.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_C1_G2` | KB-06 (Areszt Królewski): koszt 2→1, złoto 0→2 | 93.6 → 🔴 ** 38.9** (`🔻 -54.7`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 38.9 (`🔻 -54.7`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_C1_G2` | KB-09 (Dekret Królewski): koszt 2→1, złoto 0→2 | 93.6 → 🔴 ** 38.6** (`🔻 -55.0`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 38.6 (`🔻 -55.0`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_C1_G2` | KB-07 (Szantaż Pieczęcią): koszt 2→1, złoto 0→2 | 93.6 → 🔴 ** 38.5** (`🔻 -55.1`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 38.5 (`🔻 -55.1`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_C1_G2` | KB-04 (Faworyt Dworu): koszt 2→1, złoto 0→2 | 93.6 → 🔴 ** 37.7** (`🔻 -55.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 37.7 (`🔻 -55.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_C0_G4` | KB-02 (Pobór Podatków): koszt 1→0, złoto 2→4 | 93.6 → 🔴 ** 37.1** (`🔻 -56.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 37.1 (`🔻 -56.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_C3_G3` | KB-10 (Pieczęć Korony): koszt 4→3, złoto 2→3 | 93.6 → 🔴 ** 37.1** (`🔻 -56.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 37.1 (`🔻 -56.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_C3_G4` | KB-10 (Pieczęć Korony): koszt 4→3, złoto 2→4 | 93.6 → 🔴 ** 36.7** (`🔻 -56.9`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 36.7 (`🔻 -56.9`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_C0_G2` | KB-12 (Szantaż Salonowy): koszt 1→0, złoto 0→2 | 93.6 → 🔴 ** 36.2** (`🔻 -57.4`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 36.2 (`🔻 -57.4`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_C3_H0` | KB-10 (Pieczęć Korony): koszt 4→3, herezja 1→0 | 93.6 → 🔴 ** 36.1** (`🔻 -57.5`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 36.1 (`🔻 -57.5`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_C1_G2` | KB-05 (List Żelazny): koszt 2→1, złoto 0→2 | 93.6 → 🔴 ** 36.0** (`🔻 -57.6`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 36.0 (`🔻 -57.6`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_HERESY_PLUS2` | SO-10 (Oczyść Miasto): heresy 1 → 3 | 93.6 → 🔴 ** 28.3** (`🔻 -65.3`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 28.3 (`🔻 -65.3`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_COST_MINUS2` | KB-10 (Pieczęć Korony): cost 4 → 2 | 93.6 → 🔴 ** 21.4** (`🔻 -72.2`) | 0.0 → 0.0 (`= 0.0`) | 93.6 → 21.4 (`🔻 -72.2`) | 0.0 → 0.0 (`= 0.0`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (82)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-04_C2_G3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.61 (0–0) | 9.06zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_COST_MINUS1` | 5.76 Er (8–1) | 0.0% | 4.5% | 1.59 (0–0) | 7.64 (0–0) | 9.13zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-04_C0_H1` | 5.74 Er (8–1) | 0.0% | 4.6% | 1.52 (0–0) | 7.69 (0–0) | 9.12zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-07_C2_G4` | 5.77 Er (8–1) | 0.0% | 5.0% | 1.55 (0–0) | 7.62 (0–0) | 9.07zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-01_C0_G3` | 5.75 Er (8–1) | 0.0% | 4.1% | 1.56 (0–0) | 7.57 (0–0) | 9.17zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-09_COST_PLUS1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.79zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-09_C1_H0` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.79zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-09_COST_PLUS2` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.66 (0–0) | 8.67zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-07_COST_MINUS1` | 5.74 Er (8–1) | 0.0% | 4.6% | 1.54 (0–0) | 7.62 (0–0) | 9.08zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-07_C0_H0` | 5.74 Er (8–1) | 0.0% | 4.6% | 1.54 (0–0) | 7.62 (0–0) | 9.08zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-07_C0_H1` | 5.74 Er (8–1) | 0.0% | 4.6% | 1.53 (0–0) | 7.66 (0–0) | 9.08zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_C2_G3` | 5.77 Er (8–1) | 0.0% | 4.8% | 1.60 (0–0) | 7.61 (0–0) | 9.13zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-12_COST_MINUS1` | 5.77 Er (8–1) | 0.0% | 4.3% | 1.54 (0–0) | 7.60 (0–0) | 8.99zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-09_COST_PLUS2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.64zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-07_C2_G3` | 5.78 Er (8–1) | 0.0% | 5.1% | 1.55 (0–0) | 7.63 (0–0) | 8.98zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-07_G3_H0` | 5.75 Er (8–1) | 0.0% | 4.8% | 1.54 (0–0) | 7.61 (0–0) | 9.06zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-08_C1_G5` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.64 (0–0) | 9.07zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-07_C0_G3` | 5.74 Er (8–1) | 0.0% | 4.5% | 1.54 (0–0) | 7.63 (0–0) | 9.17zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-01_HERESY_PLUS1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.03zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-01_COST_MINUS1` | 5.76 Er (8–1) | 0.0% | 4.1% | 1.54 (0–0) | 7.53 (0–0) | 9.08zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-04_C2_G2` | 5.77 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.60 (0–0) | 8.98zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-04_G2_H0` | 5.75 Er (8–1) | 0.0% | 4.7% | 1.53 (0–0) | 7.63 (0–0) | 9.06zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-12_C2_G3` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.55 (0–0) | 7.59 (0–0) | 8.98zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-01_HERESY_PLUS2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.03zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-01_G0_H2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.64 (0–0) | 9.01zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-11_HERESY_PLUS1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.58 (0–0) | 8.97zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-11_C0_H3` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.58 (0–0) | 8.97zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-11_C1_H3` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.57 (0–0) | 8.94zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-11_G0_H3` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.58 (0–0) | 8.97zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-04_G2_H1` | 5.74 Er (8–1) | 0.0% | 4.8% | 1.51 (0–0) | 7.70 (0–0) | 9.10zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-05_COST_PLUS1` | 5.78 Er (8–1) | 0.0% | 5.2% | 1.51 (0–0) | 7.63 (0–0) | 8.90zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-05_C1_H3` | 5.78 Er (8–1) | 0.0% | 5.2% | 1.51 (0–0) | 7.63 (0–0) | 8.90zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-05_C1_H5` | 5.78 Er (8–1) | 0.0% | 5.2% | 1.51 (0–0) | 7.63 (0–0) | 8.90zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-05_C1_G4` | 5.78 Er (8–1) | 0.0% | 5.2% | 1.51 (0–0) | 7.63 (0–0) | 8.90zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-05_C1_G5` | 5.78 Er (8–1) | 0.0% | 5.2% | 1.51 (0–0) | 7.63 (0–0) | 8.90zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-07_G3_H1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.64 (0–0) | 9.07zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-08_C0_G4` | 5.75 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.63 (0–0) | 9.08zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-08_C0_G5` | 5.75 Er (8–1) | 0.0% | 4.6% | 1.54 (0–0) | 7.63 (0–0) | 9.18zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-08_G4_H0` | 5.75 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.63 (0–0) | 9.08zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_COST_PLUS1` | 5.76 Er (8–1) | 0.0% | 5.1% | 1.51 (0–0) | 7.58 (0–0) | 8.90zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-01_HERESY_MINUS2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.88zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-03_COST_PLUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.61 (0–0) | 8.98zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-03_COST_PLUS2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.60 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-03_C2_H3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.60 (0–0) | 8.99zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-05_COST_PLUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.83zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-05_C2_H0` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.83zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-05_C2_H1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.83zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-05_C2_G1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.83zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-05_C2_G2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.83zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-11_HERESY_PLUS2` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.57 (0–0) | 8.96zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-04_COST_MINUS1` | 5.74 Er (8–1) | 0.0% | 4.6% | 1.54 (0–0) | 7.63 (0–0) | 9.09zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-04_C0_H0` | 5.74 Er (8–1) | 0.0% | 4.6% | 1.54 (0–0) | 7.63 (0–0) | 9.09zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-07_HERESY_PLUS2` | 5.73 Er (8–1) | 0.0% | 4.9% | 1.49 (0–0) | 7.68 (0–0) | 9.11zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-07_HERESY_SET2` | 5.73 Er (8–1) | 0.0% | 4.9% | 1.49 (0–0) | 7.68 (0–0) | 9.11zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-12_C2_G2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.61 (0–0) | 8.98zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-09_C0_G1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 9.36zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-09_C0_G2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.61 (0–0) | 9.55zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_HERESY_PLUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-04_C0_H1` | 5.74 Er (8–1) | 0.0% | 4.7% | 1.53 (0–0) | 7.62 (0–0) | 9.01zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-01_C2_G4` | 5.76 Er (8–1) | 0.0% | 4.7% | 1.55 (0–0) | 7.53 (0–0) | 9.08zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-08_COST_PLUS1` | 5.78 Er (8–1) | 0.0% | 5.3% | 1.52 (0–0) | 7.61 (0–0) | 8.92zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-08_C1_H0` | 5.78 Er (8–1) | 0.0% | 5.3% | 1.52 (0–0) | 7.61 (0–0) | 8.92zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-10_COST_MINUS1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.55 (0–0) | 7.64 (0–0) | 9.05zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-01_COST_PLUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.99zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-01_HERESY_MINUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.98zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-01_C3_H1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.99zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-01_C3_H3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.99zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-01_C3_G1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.99zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-01_G0_H1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.98zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-01_C2_H2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.01zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-03_HERESY_PLUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 9.00zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-03_C0_H3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 9.01zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-03_C2_G1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-03_G0_H3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 9.00zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-09_G1_H0` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.61 (0–0) | 9.17zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-01_HERESY_PLUS1` | 5.75 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.61 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-01_G0_H2` | 5.75 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.61 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-03_C3_G1` | 5.77 Er (8–1) | 0.0% | 4.8% | 1.54 (0–0) | 7.63 (0–0) | 9.02zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-07_HERESY_PLUS1` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.66 (0–0) | 8.99zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-07_HERESY_SET1` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.66 (0–0) | 8.99zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-08_COST_PLUS2` | 5.80 Er (8–1) | 0.0% | 5.7% | 1.50 (0–0) | 7.59 (0–0) | 8.85zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 1021 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_CAA-01_HERESY_PLUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-01_HERESY_PLUS2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-01_G0_H3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-02_C1_G4` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-03_C1_G3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.98zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-05_COST_PLUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.73zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-05_C1_H0` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.73zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-05_C0_G5` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.25zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-05_C0_G6` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.50zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-05_C1_G5` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.98zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-05_C1_G6` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.23zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-05_G3_H0` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.74zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-05_G5_H0` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.25zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-07_C0_G4` | 5.78 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.67 (0–0) | 9.50zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-07_C1_G4` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-07_G4_H0` | 5.78 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.67 (0–0) | 9.50zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-09_C1_G1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.97zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-11_C2_G2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.98zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-03_G1_H3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 9.01zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-05_HERESY_PLUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-05_HERESY_PLUS2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-05_HERESY_SET1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-05_HERESY_SET2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-05_G0_H1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-05_G1_H0` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-05_G1_H1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-06_COST_MINUS1` | 5.74 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.55 (0–0) | 8.77zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_G0_H3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-10_C3_G2` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.60 (0–0) | 9.30zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-05_HERESY_MINUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-05_G0_H0` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-12_HERESY_MINUS2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_G0_H0` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-01_C0_G4` | 5.74 Er (8–1) | 0.0% | 4.1% | 1.60 (0–0) | 7.58 (0–0) | 9.39zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-05_HERESY_PLUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-05_HERESY_PLUS2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-05_HERESY_MINUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-05_HERESY_MINUS2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-05_C0_H3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-05_C0_H5` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-05_C0_G4` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-05_C0_G5` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-05_G2_H3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-05_G2_H5` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-05_G4_H3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-05_G4_H5` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-06_HERESY_PLUS2` | 5.73 Er (8–1) | 0.0% | 4.4% | 1.49 (0–0) | 7.50 (0–0) | 9.20zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-06_HERESY_SET2` | 5.73 Er (8–1) | 0.0% | 4.4% | 1.49 (0–0) | 7.50 (0–0) | 9.20zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-06_G1_H1` | 5.72 Er (8–1) | 0.0% | 4.7% | 1.52 (0–0) | 7.72 (0–0) | 9.09zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-08_G2_H0` | 5.77 Er (8–1) | 0.0% | 5.1% | 1.53 (0–0) | 7.60 (0–0) | 8.92zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-09_C0_H2` | 5.77 Er (8–1) | 0.0% | 3.7% | 1.54 (0–0) | 7.63 (0–0) | 9.07zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_C0_H2` | 5.78 Er (8–1) | 0.0% | 3.8% | 1.53 (0–0) | 7.57 (0–0) | 9.32zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_C2_H2` | 5.77 Er (8–1) | 0.0% | 4.7% | 1.53 (0–0) | 7.55 (0–0) | 9.31zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-12_HERESY_PLUS1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.66 (0–0) | 8.99zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-01_COST_PLUS2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.61 (0–0) | 8.99zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-04_C1_G4` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.98zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-06_C1_G1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.97zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-07_C1_G5` | 5.78 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.67 (0–0) | 9.49zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-08_COST_PLUS1` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.59 (0–0) | 8.86zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-08_C3_H0` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.59 (0–0) | 8.86zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-02_COST_PLUS1` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.69 (0–0) | 8.80zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-02_C1_H0` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.69 (0–0) | 8.80zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-02_C1_G3` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.64 (0–0) | 9.00zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-02_G1_H0` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.68 (0–0) | 8.80zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-03_COST_MINUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.65 (0–0) | 9.02zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-03_HERESY_PLUS2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.61 (0–0) | 9.00zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_PLUS2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.00zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_HERESY_PLUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_HERESY_PLUS2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-09_COST_MINUS1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.61 (0–0) | 9.17zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-09_C0_H0` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.61 (0–0) | 9.17zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-10_COST_MINUS1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.59 (0–0) | 9.02zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-11_COST_PLUS1` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.58 (0–0) | 8.93zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-11_C1_G1` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_HERESY_PLUS2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_G0_H2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-04_COST_PLUS2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.60 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-04_G1_H1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.61 (0–0) | 9.02zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-01_HERESY_PLUS1` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.66 (0–0) | 8.98zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-02_COST_PLUS2` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.54 (0–0) | 9.07zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-02_HERESY_PLUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.62 (0–0) | 9.08zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-02_C0_H3` | 5.75 Er (8–1) | 0.0% | 3.9% | 1.52 (0–0) | 7.73 (0–0) | 9.14zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-02_G1_H3` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.59 (0–0) | 9.08zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-08_C1_G4` | 5.77 Er (8–1) | 0.0% | 5.1% | 1.52 (0–0) | 7.63 (0–0) | 8.98zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_C0_G3` | 5.77 Er (8–1) | 0.0% | 4.1% | 1.60 (0–0) | 7.60 (0–0) | 9.55zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-12_C2_H1` | 5.77 Er (8–1) | 0.0% | 5.3% | 1.48 (0–0) | 7.64 (0–0) | 8.77zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-01_C1_H1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.88zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-01_G1_H1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.88zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-07_C0_G5` | 5.78 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.68 (0–0) | 9.80zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-08_C3_G3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.98zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-10_C3_G1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.98zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-10_G1_H0` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 9.24zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-01_COST_PLUS2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 8.91zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-01_C0_G3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.59 (0–0) | 9.46zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-05_COST_MINUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 9.16zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-05_C0_H0` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 9.16zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-05_C0_H1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 9.16zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-05_C0_G1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 9.16zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-05_C0_G2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 9.16zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_PLUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_C2_H3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_C2_G2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_G0_H1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.98zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-11_COST_PLUS2` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.55 (0–0) | 8.92zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_PLUS2` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.62 (0–0) | 8.98zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-02_C1_G4` | 5.76 Er (8–1) | 0.0% | 5.1% | 1.53 (0–0) | 7.63 (0–0) | 9.01zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-04_HERESY_PLUS1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.60 (0–0) | 9.00zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-04_HERESY_SET1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.60 (0–0) | 9.00zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-04_G0_H1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.60 (0–0) | 9.00zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-05_C2_G1` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.63 (0–0) | 9.00zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-02_HERESY_PLUS2` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.59 (0–0) | 9.09zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-03_G1_H5` | 5.75 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.71 (0–0) | 9.01zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_C0_G2` | 5.78 Er (8–1) | 0.0% | 4.3% | 1.59 (0–0) | 7.60 (0–0) | 9.38zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-01_C1_H3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-01_G1_H3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-03_C0_G3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.23zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-03_C1_G4` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.21zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-12_G3_H1` | 5.74 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.66 (0–0) | 8.73zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-01_C0_G2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.59 (0–0) | 9.26zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-04_C2_G1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.98zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-05_COST_PLUS2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.66zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-07_G2_H0` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.81zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_C0_H3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.00zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_C2_H1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.98zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-09_COST_PLUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 8.83zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-09_C2_H0` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 8.83zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-09_C2_G2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 9.17zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-10_C3_G1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.59 (0–0) | 9.15zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-12_C0_G2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.18zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-08_G1_H3` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.61 (0–0) | 8.98zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-09_C2_G1` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.63 (0–0) | 9.00zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-03_C1_H5` | 5.75 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.71 (0–0) | 9.00zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-08_G4_H1` | 5.74 Er (8–1) | 0.0% | 4.8% | 1.51 (0–0) | 7.67 (0–0) | 9.11zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-09_C2_H0` | 5.81 Er (8–1) | 0.0% | 5.3% | 1.47 (0–0) | 7.62 (0–0) | 8.71zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_C2_G2` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.60 (0–0) | 8.98zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-02_COST_PLUS1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.86zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-02_C1_H0` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.86zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-02_G2_H0` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.86zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-04_COST_PLUS1` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.76zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-04_C1_H0` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.76zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-04_G2_H0` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.77zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-08_C3_H1` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.59 (0–0) | 9.28zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-08_G1_H0` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.60 (0–0) | 8.87zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-12_COST_PLUS2` | 5.74 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.64 (0–0) | 8.71zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-12_C2_H1` | 5.74 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.66 (0–0) | 8.73zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-12_C2_G5` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 9.00zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-12_G3_H0` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.66 (0–0) | 8.75zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-01_COST_PLUS1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.86zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-03_C2_G2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.65 (0–0) | 9.02zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-04_COST_PLUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.82zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-04_C2_G2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.60 (0–0) | 9.16zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-06_G1_H2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 9.25zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_G2_H3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.00zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-12_C0_G3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.32zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-08_COST_PLUS2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.57 (0–0) | 8.98zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-08_G1_H1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.61 (0–0) | 8.98zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-03_C1_G1` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.54 (0–0) | 7.63 (0–0) | 9.00zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-12_C2_G1` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.61 (0–0) | 8.98zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-01_C2_G3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.98zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-04_HERESY_PLUS1` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.69 (0–0) | 9.01zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-04_HERESY_SET1` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.69 (0–0) | 9.01zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-09_HERESY_MINUS1` | 5.80 Er (8–1) | 0.0% | 5.1% | 1.52 (0–0) | 7.59 (0–0) | 8.76zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-09_G0_H0` | 5.80 Er (8–1) | 0.0% | 5.1% | 1.52 (0–0) | 7.59 (0–0) | 8.76zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-10_C6_H0` | 5.81 Er (8–1) | 0.0% | 5.1% | 1.53 (0–0) | 7.59 (0–0) | 8.99zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_COST_PLUS2` | 5.77 Er (8–1) | 0.0% | 4.7% | 1.52 (0–0) | 7.55 (0–0) | 9.26zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_HERESY_PLUS2` | 5.77 Er (8–1) | 0.0% | 4.7% | 1.53 (0–0) | 7.54 (0–0) | 9.30zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_G2_H2` | 5.77 Er (8–1) | 0.0% | 4.7% | 1.53 (0–0) | 7.54 (0–0) | 9.31zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-12_HERESY_PLUS2` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.64 (0–0) | 8.98zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-03_C0_G4` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.48zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-05_COST_PLUS2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 8.48zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-07_COST_PLUS1` | 5.74 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.57 (0–0) | 8.74zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-07_C1_H0` | 5.74 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.57 (0–0) | 8.74zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-07_C1_H1` | 5.74 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.59 (0–0) | 8.72zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-07_G2_H0` | 5.74 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.57 (0–0) | 8.74zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-07_G2_H1` | 5.74 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.59 (0–0) | 8.72zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-08_G1_H1` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.60 (0–0) | 9.28zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-12_COST_PLUS1` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.66 (0–0) | 8.75zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-12_C2_H0` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.66 (0–0) | 8.75zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-01_COST_MINUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.59 (0–0) | 9.05zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-06_C2_H2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.65 (0–0) | 9.25zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-06_C4_H0` | 5.77 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.60 (0–0) | 8.29zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-07_C0_G4` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 9.19zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-07_C0_G5` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 9.38zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-07_G4_H0` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 9.19zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-09_C2_G1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 9.00zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-10_COST_MINUS2` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.60 (0–0) | 9.16zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-01_HERESY_PLUS2` | 5.75 Er (8–1) | 0.0% | 4.6% | 1.53 (0–0) | 7.60 (0–0) | 9.00zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-08_HERESY_PLUS1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.99zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-08_HERESY_MINUS1` | 5.77 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.64 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-08_G0_H1` | 5.77 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.64 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-08_G0_H3` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.99zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-04_COST_PLUS1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.61 (0–0) | 8.97zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-04_C2_H0` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.61 (0–0) | 8.97zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-02_G3_H3` | 5.75 Er (8–1) | 0.0% | 4.7% | 1.52 (0–0) | 7.72 (0–0) | 9.13zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-03_COST_MINUS1` | 5.76 Er (8–1) | 0.0% | 4.8% | 1.54 (0–0) | 7.67 (0–0) | 8.99zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-09_HERESY_PLUS1` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.62 (0–0) | 9.08zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-09_HERESY_PLUS2` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.62 (0–0) | 9.08zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-09_C2_G1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.62 (0–0) | 9.00zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-09_G0_H2` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.62 (0–0) | 9.08zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_HERESY_PLUS1` | 5.77 Er (8–1) | 0.0% | 4.7% | 1.53 (0–0) | 7.54 (0–0) | 9.31zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_G0_H2` | 5.77 Er (8–1) | 0.0% | 4.7% | 1.53 (0–0) | 7.54 (0–0) | 9.30zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-12_COST_PLUS2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.97zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-01_C3_G2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.94zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-03_COST_PLUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.75zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-10_COST_MINUS1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.24zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-10_C1_H0` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.24zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-12_COST_MINUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.28zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-12_C0_H0` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.28zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-12_G5_H0` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.26zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-01_C2_G2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.00zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-01_C2_G3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.60 (0–0) | 9.05zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-02_HERESY_PLUS1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.71 (0–0) | 8.96zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-02_HERESY_SET1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.71 (0–0) | 8.96zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-02_C0_H1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.71 (0–0) | 8.96zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-04_COST_MINUS1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.59 (0–0) | 9.17zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-06_C4_G2` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.60 (0–0) | 8.73zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-07_C1_G4` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.62 (0–0) | 9.01zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-04_COST_PLUS2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.67 (0–0) | 9.03zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-03_HERESY_PLUS1` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 9.03zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-03_G0_H5` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 9.03zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-04_C0_G2` | 5.74 Er (8–1) | 0.0% | 4.5% | 1.54 (0–0) | 7.66 (0–0) | 9.19zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-07_C0_G4` | 5.74 Er (8–1) | 0.0% | 4.5% | 1.55 (0–0) | 7.64 (0–0) | 9.27zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-09_G1_H2` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.63 (0–0) | 9.07zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-04_COST_PLUS2` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.58 (0–0) | 8.67zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-10_C1_G2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.74zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-10_C3_G2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.61 (0–0) | 9.22zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-12_C0_G6` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 9.79zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-02_C1_H1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.69 (0–0) | 8.87zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-04_C0_G1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.59 (0–0) | 9.36zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-07_COST_PLUS2` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.61 (0–0) | 8.63zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_HERESY_MINUS2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.55 (0–0) | 8.78zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-12_C1_G2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.00zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-12_C1_G3` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.63 (0–0) | 9.20zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-01_HERESY_MINUS1` | 5.80 Er (8–1) | 0.0% | 5.3% | 1.55 (0–0) | 7.65 (0–0) | 9.00zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-01_G0_H0` | 5.80 Er (8–1) | 0.0% | 5.3% | 1.55 (0–0) | 7.65 (0–0) | 9.00zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-04_C3_G1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.60 (0–0) | 9.01zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-08_C4_H1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.57 (0–0) | 8.98zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_C2_G2` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.62 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-05_COST_PLUS2` | 5.79 Er (8–1) | 0.0% | 5.5% | 1.49 (0–0) | 7.60 (0–0) | 8.82zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-06_COST_PLUS2` | 5.80 Er (8–1) | 0.0% | 5.3% | 1.48 (0–0) | 7.61 (0–0) | 8.91zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-06_C1_H1` | 5.72 Er (8–1) | 0.0% | 4.7% | 1.52 (0–0) | 7.75 (0–0) | 9.08zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-01_COST_MINUS1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.94zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-07_COST_PLUS2` | 5.75 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.59 (0–0) | 8.70zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-08_COST_PLUS2` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.58 (0–0) | 9.13zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-08_COST_MINUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.68 (0–0) | 9.19zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-08_C1_H0` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.68 (0–0) | 9.19zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-08_C3_G4` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.68 (0–0) | 9.16zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-08_G3_H0` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.68 (0–0) | 9.17zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-10_COST_MINUS2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.51zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-10_C1_G1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.49zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-12_C0_G5` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.53zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-02_C0_G4` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.62 (0–0) | 9.34zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-12_G2_H1` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.58 (0–0) | 9.11zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-08_C4_G1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.57 (0–0) | 8.98zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-10_G1_H0` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.61 (0–0) | 8.96zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_PLUS1` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.62 (0–0) | 8.98zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_C2_H0` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.62 (0–0) | 8.98zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_C2_H2` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.62 (0–0) | 8.98zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-04_C2_G1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.61 (0–0) | 8.98zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-07_HERESY_PLUS1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 8.99zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-07_HERESY_SET1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 8.99zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-07_C2_G1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.00zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-07_G0_H1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 8.99zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-06_HERESY_PLUS1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.70 (0–0) | 8.97zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-06_HERESY_SET1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.70 (0–0) | 8.97zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-06_C3_H1` | 5.76 Er (8–1) | 0.0% | 5.1% | 1.49 (0–0) | 7.64 (0–0) | 8.93zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-06_G0_H1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.70 (0–0) | 8.97zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-10_HERESY_MINUS1` | 5.77 Er (8–1) | 0.0% | 5.1% | 1.54 (0–0) | 7.53 (0–0) | 8.98zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-10_C4_G1` | 5.73 Er (8–1) | 0.0% | 4.6% | 1.56 (0–0) | 7.62 (0–0) | 9.21zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-10_G0_H0` | 5.77 Er (8–1) | 0.0% | 5.1% | 1.54 (0–0) | 7.53 (0–0) | 8.98zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-12_C0_H1` | 5.77 Er (8–1) | 0.0% | 4.6% | 1.56 (0–0) | 7.61 (0–0) | 8.95zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-02_COST_PLUS2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.85zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-02_C1_H1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 8.85zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-02_G2_H1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 8.85zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-03_COST_PLUS2` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.63 (0–0) | 8.60zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-06_COST_PLUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 8.84zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-06_C1_H0` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 8.84zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-02_COST_PLUS2` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.71 (0–0) | 8.53zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-02_HERESY_PLUS2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.71 (0–0) | 8.91zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-02_HERESY_SET2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.71 (0–0) | 8.91zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-02_G1_H1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.70 (0–0) | 8.87zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-03_HERESY_MINUS2` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.64 (0–0) | 8.57zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-11_C0_G1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.68 (0–0) | 9.14zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-08_COST_PLUS1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.56 (0–0) | 8.98zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-08_C4_G2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.57 (0–0) | 8.98zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-04_HERESY_PLUS2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.59 (0–0) | 9.00zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-04_HERESY_SET2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.59 (0–0) | 9.00zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-01_HERESY_MINUS1` | 5.79 Er (8–1) | 0.0% | 4.8% | 1.57 (0–0) | 7.62 (0–0) | 8.97zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-02_C2_G4` | 5.75 Er (8–1) | 0.0% | 4.7% | 1.54 (0–0) | 7.66 (0–0) | 9.12zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-02_G1_H1` | 5.77 Er (8–1) | 0.0% | 5.0% | 1.51 (0–0) | 7.69 (0–0) | 8.86zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-09_COST_PLUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.00zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-09_C2_G2` | 5.76 Er (8–1) | 0.0% | 5.1% | 1.53 (0–0) | 7.68 (0–0) | 8.80zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-10_C6_G1` | 5.78 Er (8–1) | 0.0% | 4.6% | 1.52 (0–0) | 7.64 (0–0) | 9.11zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-12_C2_H3` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 8.97zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-12_G2_H1` | 5.77 Er (8–1) | 0.0% | 4.7% | 1.56 (0–0) | 7.61 (0–0) | 8.96zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-02_HERESY_PLUS1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 8.90zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-02_HERESY_PLUS2` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.65 (0–0) | 8.86zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-02_HERESY_SET1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 8.90zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-02_HERESY_SET2` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.65 (0–0) | 8.86zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-02_C0_H1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 8.90zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-08_HERESY_PLUS2` | 5.74 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.61 (0–0) | 9.32zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-08_HERESY_SET2` | 5.74 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.61 (0–0) | 9.32zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-11_COST_MINUS1` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.63 (0–0) | 9.09zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-11_C0_H0` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.63 (0–0) | 9.09zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-11_C2_G3` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.07zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-11_G2_H0` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.63 (0–0) | 9.08zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-12_C2_G6` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 9.27zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-01_C0_H2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.61 (0–0) | 9.15zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-03_C0_G1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.73 (0–0) | 9.17zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-07_C1_G5` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.61 (0–0) | 9.20zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_HERESY_MINUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.95zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-08_C4_H3` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.56 (0–0) | 8.98zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-10_G1_H0` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.61 (0–0) | 9.10zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-01_HERESY_PLUS2` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.66 (0–0) | 8.97zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-06_COST_PLUS1` | 5.78 Er (8–1) | 0.0% | 5.2% | 1.51 (0–0) | 7.61 (0–0) | 8.94zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-06_C3_H0` | 5.78 Er (8–1) | 0.0% | 5.2% | 1.51 (0–0) | 7.61 (0–0) | 8.94zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-10_COST_PLUS1` | 5.80 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.66 (0–0) | 9.01zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-12_C0_H3` | 5.76 Er (8–1) | 0.0% | 4.2% | 1.53 (0–0) | 7.64 (0–0) | 9.04zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-12_G2_H3` | 5.75 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.64 (0–0) | 9.04zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-08_COST_MINUS2` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.73 (0–0) | 9.40zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-08_C1_G3` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.73 (0–0) | 9.38zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-02_C0_G3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.62 (0–0) | 9.14zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-02_G3_H0` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.62 (0–0) | 9.14zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-10_C5_G2` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.56 (0–0) | 8.99zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-08_HERESY_PLUS2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.60 (0–0) | 8.99zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-08_HERESY_MINUS2` | 5.78 Er (8–1) | 0.0% | 5.0% | 1.54 (0–0) | 7.66 (0–0) | 9.00zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-04_C2_H1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.59 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-07_HERESY_PLUS2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 8.99zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-07_HERESY_SET2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 8.99zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-08_C2_G1` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.64 (0–0) | 9.00zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-11_C3_G3` | 5.74 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.57 (0–0) | 9.11zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-02_COST_MINUS1` | 5.74 Er (8–1) | 0.0% | 4.2% | 1.54 (0–0) | 7.70 (0–0) | 9.12zł (0.0–0.0) | 8.26 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-10_C6_G2` | 5.77 Er (8–1) | 0.0% | 4.5% | 1.53 (0–0) | 7.63 (0–0) | 9.22zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-12_COST_PLUS1` | 5.74 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.61 (0–0) | 8.94zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-12_C0_G2` | 5.75 Er (8–1) | 0.0% | 4.3% | 1.55 (0–0) | 7.63 (0–0) | 9.10zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-12_G0_H1` | 5.78 Er (8–1) | 0.0% | 5.4% | 1.47 (0–0) | 7.67 (0–0) | 8.76zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-12_G0_H3` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.66 (0–0) | 8.98zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-11_COST_PLUS1` | 5.77 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.65 (0–0) | 9.10zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-11_C2_H0` | 5.77 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.65 (0–0) | 9.10zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-11_G0_H0` | 5.77 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.65 (0–0) | 9.11zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-03_C2_H1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.65 (0–0) | 8.47zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-07_COST_PLUS1` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.62 (0–0) | 8.82zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-07_C1_H0` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.62 (0–0) | 8.82zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-11_C1_G2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.68 (0–0) | 9.14zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-12_HERESY_MINUS1` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.58 (0–0) | 8.89zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-12_C0_H1` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.58 (0–0) | 8.89zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-06_C3_G1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.98zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-02_C2_H1` | 5.78 Er (8–1) | 0.0% | 5.1% | 1.52 (0–0) | 7.66 (0–0) | 8.88zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-03_HERESY_MINUS1` | 5.77 Er (8–1) | 0.0% | 5.0% | 1.54 (0–0) | 7.66 (0–0) | 8.96zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-03_G0_H3` | 5.77 Er (8–1) | 0.0% | 5.0% | 1.54 (0–0) | 7.66 (0–0) | 8.96zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-04_C0_G3` | 5.72 Er (8–1) | 0.0% | 4.3% | 1.54 (0–0) | 7.64 (0–0) | 9.29zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-06_C3_G1` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.61 (0–0) | 9.01zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-09_COST_MINUS1` | 5.76 Er (8–1) | 0.0% | 4.4% | 1.53 (0–0) | 7.71 (0–0) | 8.79zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-01_HERESY_MINUS1` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.55 (0–0) | 8.78zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-04_C0_G2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.59 (0–0) | 9.55zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_MINUS1` | 5.75 Er (8–1) | 0.0% | 4.6% | 1.54 (0–0) | 7.63 (0–0) | 9.05zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_HERESY_MINUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.61 (0–0) | 9.00zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-02_C2_G3` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.61 (0–0) | 8.98zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-08_HERESY_PLUS1` | 5.74 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.62 (0–0) | 9.25zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-08_HERESY_SET1` | 5.74 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.62 (0–0) | 9.25zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-01_G2_H2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.61 (0–0) | 9.16zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-03_C3_G2` | 5.75 Er (8–1) | 0.0% | 4.8% | 1.54 (0–0) | 7.67 (0–0) | 8.99zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-08_C1_H1` | 5.77 Er (8–1) | 0.0% | 5.4% | 1.51 (0–0) | 7.67 (0–0) | 8.94zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-08_G2_H1` | 5.76 Er (8–1) | 0.0% | 5.1% | 1.51 (0–0) | 7.66 (0–0) | 8.95zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-09_COST_PLUS2` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.60 (0–0) | 9.06zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-09_C0_H0` | 5.79 Er (8–1) | 0.0% | 4.7% | 1.56 (0–0) | 7.58 (0–0) | 8.83zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-04_C0_G4` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.65 (0–0) | 9.26zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-04_G4_H0` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.65 (0–0) | 9.26zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-02_C1_G4` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.62 (0–0) | 9.15zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-06_C4_G1` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.63 (0–0) | 9.04zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_C2_G3` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.62 (0–0) | 9.04zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-07_COST_PLUS1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.98zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-07_C2_H0` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.98zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-08_HERESY_PLUS1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.66 (0–0) | 9.01zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-08_HERESY_SET1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.66 (0–0) | 9.01zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-08_C0_H1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.66 (0–0) | 9.01zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-09_C2_H2` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.62 (0–0) | 9.07zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-12_HERESY_MINUS1` | 5.78 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.66 (0–0) | 8.86zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-04_C1_H1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.68zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-04_C0_G5` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.65 (0–0) | 9.51zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-04_C1_G5` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.65 (0–0) | 9.25zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-04_G2_H1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.68zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-10_COST_PLUS1` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.66 (0–0) | 8.76zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-10_C3_H0` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.66 (0–0) | 8.76zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-03_HERESY_MINUS1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.68 (0–0) | 8.61zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-03_G0_H1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.68 (0–0) | 8.61zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-06_COST_MINUS1` | 5.77 Er (8–1) | 0.0% | 4.7% | 1.53 (0–0) | 7.62 (0–0) | 9.00zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-06_C1_H0` | 5.77 Er (8–1) | 0.0% | 4.7% | 1.53 (0–0) | 7.62 (0–0) | 9.00zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-07_COST_PLUS2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.97zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-02_C2_H3` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.59 (0–0) | 9.07zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-04_G0_H0` | 5.77 Er (8–1) | 0.0% | 5.2% | 1.52 (0–0) | 7.60 (0–0) | 8.92zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-10_G1_H0` | 5.75 Er (8–1) | 0.0% | 4.8% | 1.54 (0–0) | 7.52 (0–0) | 9.10zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-12_C0_G3` | 5.73 Er (8–1) | 0.0% | 4.2% | 1.58 (0–0) | 7.64 (0–0) | 9.22zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-06_C2_G1` | 5.73 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.53 (0–0) | 8.94zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_MINUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.61 (0–0) | 9.07zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-11_C0_G2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.69 (0–0) | 9.32zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-08_C2_H1` | 5.75 Er (8–1) | 0.0% | 5.1% | 1.53 (0–0) | 7.59 (0–0) | 8.97zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-10_G3_H2` | 5.78 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.69 (0–0) | 9.05zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_C0_G2` | 5.73 Er (8–1) | 0.0% | 4.6% | 1.53 (0–0) | 7.58 (0–0) | 9.16zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-12_COST_PLUS1` | 5.77 Er (8–1) | 0.0% | 5.1% | 1.53 (0–0) | 7.68 (0–0) | 8.91zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-12_C2_H0` | 5.77 Er (8–1) | 0.0% | 5.1% | 1.53 (0–0) | 7.68 (0–0) | 8.91zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-01_C0_H1` | 5.78 Er (8–1) | 0.0% | 4.4% | 1.59 (0–0) | 7.60 (0–0) | 9.11zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-01_G3_H1` | 5.79 Er (8–1) | 0.0% | 4.6% | 1.60 (0–0) | 7.61 (0–0) | 9.11zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-01_G3_H3` | 5.75 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.59 (0–0) | 9.07zł (0.0–0.0) | 8.12 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-03_COST_MINUS2` | 5.73 Er (8–1) | 0.0% | 4.2% | 1.53 (0–0) | 7.68 (0–0) | 8.98zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-04_COST_PLUS1` | 5.78 Er (8–1) | 0.0% | 5.3% | 1.51 (0–0) | 7.60 (0–0) | 8.92zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-04_C2_H0` | 5.78 Er (8–1) | 0.0% | 5.3% | 1.51 (0–0) | 7.60 (0–0) | 8.92zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-07_HERESY_PLUS2` | 5.74 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.62 (0–0) | 8.75zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-07_HERESY_SET2` | 5.74 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.62 (0–0) | 8.75zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-04_C2_H0` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.55 (0–0) | 8.69zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-01_C0_H2` | 5.72 Er (8–1) | 0.0% | 3.7% | 1.52 (0–0) | 7.61 (0–0) | 8.94zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-10_G1_H1` | 5.73 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.61 (0–0) | 9.06zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-02_COST_PLUS1` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.58 (0–0) | 9.06zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-07_HERESY_PLUS1` | 5.73 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.61 (0–0) | 8.79zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-07_HERESY_SET1` | 5.73 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.61 (0–0) | 8.79zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-07_C0_H1` | 5.73 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.61 (0–0) | 8.79zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-08_C1_G4` | 5.77 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.76 (0–0) | 9.65zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-01_C2_H0` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.56 (0–0) | 8.53zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-06_C2_G2` | 5.72 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.52 (0–0) | 9.12zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_C2_G3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.61 (0–0) | 9.07zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-10_C5_G1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.60 (0–0) | 8.98zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-07_C3_G1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-05_C2_H0` | 5.86 Er (8–1) | 0.0% | 5.2% | 1.56 (0–0) | 7.65 (0–0) | 9.00zł (0.0–0.0) | 8.12 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-01_HERESY_MINUS2` | 5.81 Er (8–1) | 0.0% | 4.7% | 1.59 (0–0) | 7.53 (0–0) | 8.98zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-03_C3_H3` | 5.79 Er (8–1) | 0.0% | 4.9% | 1.56 (0–0) | 7.60 (0–0) | 9.00zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-06_HERESY_MINUS1` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.53 (0–0) | 8.48zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-06_G0_H0` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.53 (0–0) | 8.48zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-09_C0_H1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.68 (0–0) | 9.28zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-12_HERESY_PLUS1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.65 (0–0) | 9.03zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-12_C0_H3` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.65 (0–0) | 9.03zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-03_HERESY_PLUS1` | 5.75 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.59 (0–0) | 9.02zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-03_G0_H2` | 5.75 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.59 (0–0) | 9.02zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-07_COST_PLUS2` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.62 (0–0) | 9.02zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-07_HERESY_PLUS1` | 5.71 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.58 (0–0) | 8.98zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-07_HERESY_SET1` | 5.71 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.58 (0–0) | 8.98zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-07_G0_H1` | 5.71 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.58 (0–0) | 8.98zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-08_COST_MINUS1` | 5.73 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.58 (0–0) | 8.96zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-07_C2_H1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.61 (0–0) | 8.98zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-07_G1_H1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.65 (0–0) | 9.01zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-10_HERESY_PLUS1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.96zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-10_HERESY_SET1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.96zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-10_G0_H1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.62 (0–0) | 8.96zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-03_C1_G1` | 5.73 Er (8–1) | 0.0% | 4.7% | 1.53 (0–0) | 7.68 (0–0) | 8.98zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_C2_H0` | 5.80 Er (8–1) | 0.0% | 5.1% | 1.54 (0–0) | 7.51 (0–0) | 8.92zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-11_C0_G2` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.67 (0–0) | 9.37zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-06_COST_MINUS2` | 5.73 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.54 (0–0) | 8.95zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-09_C2_H1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.69 (0–0) | 8.93zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-02_COST_PLUS1` | 5.79 Er (8–1) | 0.0% | 5.9% | 1.53 (0–0) | 7.64 (0–0) | 9.05zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-02_C2_H0` | 5.79 Er (8–1) | 0.0% | 5.9% | 1.53 (0–0) | 7.64 (0–0) | 9.05zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-05_COST_PLUS2` | 5.77 Er (8–1) | 0.0% | 5.4% | 1.53 (0–0) | 7.67 (0–0) | 9.05zł (0.0–0.0) | 8.26 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-06_COST_PLUS1` | 5.78 Er (8–1) | 0.0% | 5.1% | 1.54 (0–0) | 7.69 (0–0) | 8.95zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-06_C3_H0` | 5.78 Er (8–1) | 0.0% | 5.1% | 1.54 (0–0) | 7.69 (0–0) | 8.95zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-06_G1_H1` | 5.69 Er (8–1) | 0.0% | 4.8% | 1.51 (0–0) | 7.60 (0–0) | 9.05zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-07_C0_H1` | 5.74 Er (8–1) | 0.0% | 4.6% | 1.53 (0–0) | 7.65 (0–0) | 9.01zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-11_HERESY_PLUS1` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.66 (0–0) | 9.28zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-11_HERESY_SET1` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.66 (0–0) | 9.28zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-11_C0_G3` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.68 (0–0) | 9.62zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-11_HERESY_MINUS1` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.68 (0–0) | 8.84zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-11_C0_H1` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.68 (0–0) | 8.84zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-11_G0_H1` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.68 (0–0) | 8.84zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-11_G1_H3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.66 (0–0) | 9.14zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-03_HERESY_PLUS2` | 5.75 Er (8–1) | 0.0% | 4.7% | 1.53 (0–0) | 7.59 (0–0) | 9.03zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-07_G1_H0` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.57 (0–0) | 9.06zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-03_COST_PLUS1` | 5.79 Er (8–1) | 0.0% | 4.8% | 1.56 (0–0) | 7.57 (0–0) | 9.05zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-03_C1_G2` | 5.72 Er (8–1) | 0.0% | 4.5% | 1.53 (0–0) | 7.69 (0–0) | 9.00zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-02_C0_G4` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.63 (0–0) | 9.43zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-02_C1_G5` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.63 (0–0) | 9.42zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-02_G4_H0` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.63 (0–0) | 9.43zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-01_G0_H0` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.56 (0–0) | 8.54zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-12_C1_H1` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.62 (0–0) | 8.79zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-02_C0_H1` | 5.67 Er (8–1) | 0.0% | 4.1% | 1.50 (0–0) | 7.61 (0–0) | 8.90zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-01_C0_H3` | 5.75 Er (8–1) | 0.0% | 4.1% | 1.53 (0–0) | 7.59 (0–0) | 9.07zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-02_C0_G3` | 5.72 Er (8–1) | 0.0% | 4.1% | 1.56 (0–0) | 7.66 (0–0) | 9.27zł (0.0–0.0) | 8.26 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_G0_H0` | 5.80 Er (8–1) | 0.0% | 5.1% | 1.53 (0–0) | 7.51 (0–0) | 8.91zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-03_C0_H1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.72 (0–0) | 8.89zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-12_G0_H1` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.61 (0–0) | 8.78zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-03_C2_H0` | 5.79 Er (8–1) | 0.0% | 5.6% | 1.54 (0–0) | 7.58 (0–0) | 9.02zł (0.0–0.0) | 8.11 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-04_HERESY_PLUS1` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.64 (0–0) | 8.99zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-04_HERESY_SET1` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.64 (0–0) | 8.99zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-04_G0_H1` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.64 (0–0) | 8.99zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-06_COST_PLUS2` | 5.77 Er (8–1) | 0.0% | 5.1% | 1.53 (0–0) | 7.70 (0–0) | 8.96zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-02_HERESY_MINUS2` | 5.79 Er (8–1) | 0.0% | 4.7% | 1.56 (0–0) | 7.65 (0–0) | 8.99zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-09_G1_H0` | 5.80 Er (8–1) | 0.0% | 4.8% | 1.56 (0–0) | 7.58 (0–0) | 8.85zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_HERESY_MINUS1` | 5.79 Er (8–1) | 0.0% | 4.8% | 1.58 (0–0) | 7.52 (0–0) | 9.01zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-03_G1_H1` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.73 (0–0) | 8.89zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-09_HERESY_PLUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.67 (0–0) | 9.10zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-09_HERESY_SET1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.67 (0–0) | 9.10zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-09_G0_H1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.67 (0–0) | 9.10zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-06_HERESY_PLUS1` | 5.71 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.63 (0–0) | 9.01zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-06_HERESY_SET1` | 5.71 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.63 (0–0) | 9.01zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-06_G0_H1` | 5.71 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.63 (0–0) | 9.01zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-11_G0_H0` | 5.78 Er (8–1) | 0.0% | 5.1% | 1.54 (0–0) | 7.70 (0–0) | 8.89zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-12_HERESY_PLUS2` | 5.70 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.64 (0–0) | 8.94zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-12_HERESY_SET2` | 5.70 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.64 (0–0) | 8.94zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-10_C4_G2` | 5.71 Er (8–1) | 0.0% | 4.4% | 1.56 (0–0) | 7.61 (0–0) | 9.38zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_G2_H0` | 5.80 Er (8–1) | 0.0% | 4.6% | 1.61 (0–0) | 7.53 (0–0) | 9.16zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-03_C0_G2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.75 (0–0) | 9.36zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-12_G2_H3` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.66 (0–0) | 9.19zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-06_C1_H1` | 5.70 Er (8–1) | 0.0% | 4.8% | 1.51 (0–0) | 7.61 (0–0) | 9.05zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-07_C2_G2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.58 (0–0) | 9.06zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-03_C3_H5` | 5.78 Er (8–1) | 0.0% | 4.7% | 1.56 (0–0) | 7.57 (0–0) | 9.05zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-10_C4_H0` | 5.74 Er (8–1) | 0.0% | 5.0% | 1.54 (0–0) | 7.51 (0–0) | 9.03zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-02_G3_H1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.69 (0–0) | 9.28zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-06_COST_PLUS1` | 5.78 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.67 (0–0) | 9.04zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-09_G1_H1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.66 (0–0) | 9.27zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-08_C2_G1` | 5.69 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.50 (0–0) | 8.92zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-06_C3_H1` | 5.73 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.68 (0–0) | 9.01zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-03_COST_PLUS2` | 5.79 Er (8–1) | 0.0% | 4.7% | 1.57 (0–0) | 7.54 (0–0) | 9.05zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-03_G1_H3` | 5.75 Er (8–1) | 0.0% | 4.8% | 1.54 (0–0) | 7.64 (0–0) | 8.83zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-10_HERESY_PLUS1` | 5.79 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.72 (0–0) | 9.02zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-03_C1_H1` | 5.84 Er (8–1) | 0.0% | 5.2% | 1.56 (0–0) | 7.64 (0–0) | 8.97zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-02_HERESY_MINUS1` | 5.76 Er (8–1) | 0.0% | 4.8% | 1.54 (0–0) | 7.75 (0–0) | 8.96zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-11_C0_H0` | 5.80 Er (8–1) | 0.0% | 4.5% | 1.61 (0–0) | 7.54 (0–0) | 9.15zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-01_G1_H2` | 5.73 Er (8–1) | 0.0% | 4.7% | 1.52 (0–0) | 7.55 (0–0) | 8.96zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-07_COST_MINUS1` | 5.75 Er (8–1) | 0.0% | 4.7% | 1.53 (0–0) | 7.56 (0–0) | 9.04zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-07_C0_H0` | 5.75 Er (8–1) | 0.0% | 4.7% | 1.53 (0–0) | 7.56 (0–0) | 9.04zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-11_C3_G2` | 5.77 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.66 (0–0) | 9.01zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-12_G1_H1` | 5.71 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.61 (0–0) | 9.02zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-08_HERESY_PLUS2` | 5.74 Er (8–1) | 0.0% | 4.8% | 1.50 (0–0) | 7.66 (0–0) | 9.02zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-08_HERESY_SET2` | 5.74 Er (8–1) | 0.0% | 4.8% | 1.50 (0–0) | 7.66 (0–0) | 9.02zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-01_C0_H0` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.54 (0–0) | 8.96zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-01_G2_H0` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.56 (0–0) | 8.96zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-07_C3_H1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.61 (0–0) | 9.02zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-06_COST_MINUS1` | 5.76 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.60 (0–0) | 9.10zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-06_C1_H0` | 5.76 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.60 (0–0) | 9.10zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-12_C0_H1` | 5.71 Er (8–1) | 0.0% | 4.7% | 1.51 (0–0) | 7.61 (0–0) | 9.02zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-09_C0_G1` | 5.78 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.65 (0–0) | 9.20zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-09_C1_G2` | 5.78 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.65 (0–0) | 9.18zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-09_G1_H0` | 5.78 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.65 (0–0) | 9.20zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-11_C2_H1` | 5.79 Er (8–1) | 0.0% | 5.0% | 1.54 (0–0) | 7.69 (0–0) | 9.45zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-11_G0_H1` | 5.79 Er (8–1) | 0.0% | 5.0% | 1.54 (0–0) | 7.69 (0–0) | 9.45zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-04_C0_H0` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.55 (0–0) | 9.05zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-07_HERESY_PLUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.68 (0–0) | 9.12zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-07_HERESY_SET1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.68 (0–0) | 9.12zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-07_C0_H1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.68 (0–0) | 9.12zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_C0_H1` | 5.78 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.62 (0–0) | 9.15zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-07_COST_PLUS1` | 5.77 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.68 (0–0) | 9.02zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-07_C3_H0` | 5.77 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.68 (0–0) | 9.02zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-03_G1_H3` | 5.73 Er (8–1) | 0.0% | 4.8% | 1.52 (0–0) | 7.70 (0–0) | 9.02zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-04_COST_MINUS1` | 5.74 Er (8–1) | 0.0% | 4.7% | 1.53 (0–0) | 7.60 (0–0) | 9.06zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-04_C0_H0` | 5.74 Er (8–1) | 0.0% | 4.7% | 1.53 (0–0) | 7.60 (0–0) | 9.06zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-08_COST_PLUS1` | 5.79 Er (8–1) | 0.0% | 5.0% | 1.54 (0–0) | 7.70 (0–0) | 8.95zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-08_C0_H1` | 5.72 Er (8–1) | 0.0% | 4.7% | 1.52 (0–0) | 7.63 (0–0) | 9.02zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-08_C2_H0` | 5.79 Er (8–1) | 0.0% | 5.0% | 1.54 (0–0) | 7.70 (0–0) | 8.95zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-02_C0_G4` | 5.71 Er (8–1) | 0.0% | 4.0% | 1.58 (0–0) | 7.69 (0–0) | 9.43zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-07_C2_H1` | 5.74 Er (8–1) | 0.0% | 5.4% | 1.48 (0–0) | 7.72 (0–0) | 8.85zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-07_G2_H1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.68 (0–0) | 8.94zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_G2_H1` | 5.78 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.62 (0–0) | 9.15zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-11_C1_H1` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.62 (0–0) | 8.57zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-03_HERESY_MINUS1` | 5.80 Er (8–1) | 0.0% | 5.0% | 1.54 (0–0) | 7.62 (0–0) | 9.01zł (0.0–0.0) | 8.10 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-03_G0_H0` | 5.80 Er (8–1) | 0.0% | 5.0% | 1.54 (0–0) | 7.62 (0–0) | 9.01zł (0.0–0.0) | 8.10 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-05_HERESY_PLUS1` | 5.67 Er (8–1) | 0.0% | 5.0% | 1.50 (0–0) | 7.57 (0–0) | 8.92zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-05_G0_H2` | 5.67 Er (8–1) | 0.0% | 5.0% | 1.50 (0–0) | 7.57 (0–0) | 8.92zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-11_C2_H1` | 5.73 Er (8–1) | 0.0% | 5.3% | 1.51 (0–0) | 7.59 (0–0) | 8.99zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-01_COST_PLUS1` | 5.74 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.64 (0–0) | 8.94zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-06_COST_PLUS1` | 5.73 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.52 (0–0) | 8.96zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-06_C3_H0` | 5.73 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.52 (0–0) | 8.96zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-08_C2_H3` | 5.72 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.59 (0–0) | 8.95zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-04_G1_H0` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.59 (0–0) | 9.07zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-06_G1_H0` | 5.75 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.59 (0–0) | 9.10zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-12_C2_H1` | 5.73 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.68 (0–0) | 8.92zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-03_HERESY_PLUS2` | 5.78 Er (8–1) | 0.0% | 4.6% | 1.57 (0–0) | 7.50 (0–0) | 9.07zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-06_C3_G2` | 5.75 Er (8–1) | 0.0% | 4.6% | 1.55 (0–0) | 7.63 (0–0) | 9.10zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-11_C0_H1` | 5.73 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.67 (0–0) | 9.19zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-11_G2_H1` | 5.73 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.67 (0–0) | 9.18zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-04_HERESY_PLUS1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.64 (0–0) | 9.22zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-04_HERESY_MINUS1` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.56 (0–0) | 8.86zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-04_G0_H0` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.56 (0–0) | 8.86zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-04_G0_H2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.64 (0–0) | 9.22zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-07_C1_H1` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.68 (0–0) | 8.95zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-07_G4_H1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.68 (0–0) | 9.31zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-08_COST_MINUS2` | 5.68 Er (8–1) | 0.0% | 4.7% | 1.52 (0–0) | 7.51 (0–0) | 8.91zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_C0_H2` | 5.75 Er (8–1) | 0.0% | 4.6% | 1.54 (0–0) | 7.68 (0–0) | 9.03zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_G2_H2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.68 (0–0) | 9.03zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-05_G1_H2` | 5.70 Er (8–1) | 0.0% | 4.8% | 1.51 (0–0) | 7.65 (0–0) | 9.00zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-08_G1_H1` | 5.71 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.62 (0–0) | 9.03zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-09_C1_H1` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.67 (0–0) | 9.06zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-11_HERESY_PLUS2` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.68 (0–0) | 9.35zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-11_HERESY_SET2` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.68 (0–0) | 9.35zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-06_HERESY_PLUS1` | 5.79 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.69 (0–0) | 9.36zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-06_G0_H2` | 5.79 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.69 (0–0) | 9.36zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-12_COST_PLUS1` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.65 (0–0) | 8.81zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-04_C3_H1` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.67 (0–0) | 9.02zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-05_C0_H2` | 5.70 Er (8–1) | 0.0% | 4.8% | 1.51 (0–0) | 7.66 (0–0) | 9.01zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-09_C0_G1` | 5.74 Er (8–1) | 0.0% | 4.7% | 1.53 (0–0) | 7.52 (0–0) | 9.36zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-01_C2_H1` | 5.75 Er (8–1) | 0.0% | 5.1% | 1.51 (0–0) | 7.67 (0–0) | 8.82zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-01_G1_H3` | 5.74 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.65 (0–0) | 8.95zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-02_C0_G5` | 5.78 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.64 (0–0) | 9.83zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-03_C1_H2` | 5.73 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.69 (0–0) | 8.75zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-03_G1_H2` | 5.73 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.69 (0–0) | 8.75zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-04_G1_H2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.64 (0–0) | 9.34zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-12_G0_H3` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.66 (0–0) | 8.81zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-05_C3_G1` | 5.74 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.59 (0–0) | 8.98zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-12_C2_H1` | 5.75 Er (8–1) | 0.0% | 5.3% | 1.52 (0–0) | 7.70 (0–0) | 9.05zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-08_C2_H1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.65 (0–0) | 9.02zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-12_HERESY_PLUS1` | 5.71 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.66 (0–0) | 8.95zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-12_HERESY_SET1` | 5.71 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.66 (0–0) | 8.95zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-12_G0_H1` | 5.71 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.66 (0–0) | 8.95zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-03_C1_H3` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.64 (0–0) | 8.81zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-04_C0_H2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 9.33zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-11_G1_H1` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.67 (0–0) | 9.01zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-12_C1_H3` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.66 (0–0) | 8.81zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-03_COST_PLUS1` | 5.77 Er (8–1) | 0.0% | 5.6% | 1.53 (0–0) | 7.54 (0–0) | 9.03zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-04_C1_H1` | 5.67 Er (8–1) | 0.0% | 4.5% | 1.50 (0–0) | 7.49 (0–0) | 8.91zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-06_HERESY_PLUS2` | 5.69 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.67 (0–0) | 9.04zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-06_HERESY_SET2` | 5.69 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.67 (0–0) | 9.04zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-09_COST_PLUS1` | 5.80 Er (8–1) | 0.0% | 5.2% | 1.54 (0–0) | 7.76 (0–0) | 8.93zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-01_G1_H1` | 5.76 Er (8–1) | 0.0% | 5.1% | 1.51 (0–0) | 7.69 (0–0) | 8.82zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-07_COST_PLUS1` | 5.77 Er (8–1) | 0.0% | 5.3% | 1.51 (0–0) | 7.61 (0–0) | 8.90zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-07_C2_H0` | 5.77 Er (8–1) | 0.0% | 5.3% | 1.51 (0–0) | 7.61 (0–0) | 8.90zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-11_COST_PLUS2` | 5.79 Er (8–1) | 0.0% | 5.0% | 1.54 (0–0) | 7.70 (0–0) | 9.42zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-06_G1_H0` | 5.74 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.51 (0–0) | 8.68zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-01_COST_PLUS1` | 5.75 Er (8–1) | 0.0% | 5.9% | 1.53 (0–0) | 7.56 (0–0) | 9.00zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-01_C2_H3` | 5.74 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.65 (0–0) | 8.94zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-04_HERESY_PLUS2` | 5.74 Er (8–1) | 0.0% | 4.8% | 1.50 (0–0) | 7.63 (0–0) | 9.25zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-04_HERESY_SET2` | 5.74 Er (8–1) | 0.0% | 4.8% | 1.50 (0–0) | 7.63 (0–0) | 9.25zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-07_G1_H0` | 5.76 Er (8–1) | 0.0% | 5.2% | 1.51 (0–0) | 7.62 (0–0) | 8.91zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-10_COST_MINUS2` | 5.71 Er (8–1) | 0.0% | 4.7% | 1.55 (0–0) | 7.65 (0–0) | 9.16zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-04_G1_H0` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.56 (0–0) | 9.06zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-01_C2_H0` | 5.77 Er (8–1) | 0.0% | 5.9% | 1.53 (0–0) | 7.60 (0–0) | 9.00zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-02_COST_MINUS1` | 5.71 Er (8–1) | 0.0% | 4.2% | 1.51 (0–0) | 7.54 (0–0) | 8.92zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-02_C0_H0` | 5.71 Er (8–1) | 0.0% | 4.2% | 1.51 (0–0) | 7.54 (0–0) | 8.92zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-11_HERESY_PLUS2` | 5.69 Er (8–1) | 0.0% | 4.7% | 1.50 (0–0) | 7.61 (0–0) | 8.98zł (0.0–0.0) | 8.30 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-11_HERESY_SET2` | 5.69 Er (8–1) | 0.0% | 4.7% | 1.50 (0–0) | 7.61 (0–0) | 8.98zł (0.0–0.0) | 8.30 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-04_C2_G2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.58 (0–0) | 9.06zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-08_HERESY_PLUS1` | 5.74 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.67 (0–0) | 8.99zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-08_HERESY_SET1` | 5.74 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.67 (0–0) | 8.99zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-08_G0_H1` | 5.74 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.67 (0–0) | 8.99zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-09_C0_G2` | 5.78 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.66 (0–0) | 9.45zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-06_C4_H2` | 5.79 Er (8–1) | 0.0% | 4.9% | 1.55 (0–0) | 7.70 (0–0) | 9.39zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-12_COST_PLUS2` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.66 (0–0) | 8.79zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-01_COST_MINUS1` | 5.72 Er (8–1) | 0.0% | 4.0% | 1.52 (0–0) | 7.55 (0–0) | 8.93zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-04_COST_MINUS1` | 5.70 Er (8–1) | 0.0% | 4.4% | 1.52 (0–0) | 7.49 (0–0) | 8.91zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-04_C1_H0` | 5.70 Er (8–1) | 0.0% | 4.4% | 1.52 (0–0) | 7.49 (0–0) | 8.91zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-12_HERESY_MINUS1` | 5.71 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.62 (0–0) | 8.97zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-12_G0_H1` | 5.71 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.62 (0–0) | 8.97zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-09_C2_H0` | 5.86 Er (8–1) | 0.0% | 5.2% | 1.56 (0–0) | 7.68 (0–0) | 8.98zł (0.0–0.0) | 8.11 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-06_C2_H0` | 5.74 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.50 (0–0) | 8.69zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-01_C2_H2` | 5.76 Er (8–1) | 0.0% | 5.8% | 1.53 (0–0) | 7.56 (0–0) | 9.00zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-10_HERESY_MINUS1` | 5.74 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.54 (0–0) | 8.97zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-08_HERESY_PLUS2` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.68 (0–0) | 9.01zł (0.0–0.0) | 8.26 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-08_HERESY_SET2` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.68 (0–0) | 9.01zł (0.0–0.0) | 8.26 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-08_C1_H1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.67 (0–0) | 9.25zł (0.0–0.0) | 8.26 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-08_G3_H1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.68 (0–0) | 9.25zł (0.0–0.0) | 8.26 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-04_COST_PLUS2` | 5.78 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.65 (0–0) | 8.98zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-11_HERESY_MINUS2` | 5.77 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.64 (0–0) | 8.73zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-10_G3_H0` | 5.73 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.53 (0–0) | 9.01zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-01_COST_PLUS2` | 5.75 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.64 (0–0) | 8.94zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-06_HERESY_PLUS2` | 5.79 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.70 (0–0) | 9.38zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-01_C2_G1` | 5.75 Er (8–1) | 0.0% | 5.8% | 1.53 (0–0) | 7.55 (0–0) | 8.99zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-06_C3_G2` | 5.73 Er (8–1) | 0.0% | 4.8% | 1.52 (0–0) | 7.54 (0–0) | 9.07zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-09_C0_H2` | 5.72 Er (8–1) | 0.0% | 4.8% | 1.52 (0–0) | 7.67 (0–0) | 9.08zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-10_C3_H1` | 5.68 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.45 (0–0) | 8.95zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-07_G1_H1` | 5.73 Er (8–1) | 0.0% | 5.3% | 1.48 (0–0) | 7.69 (0–0) | 8.85zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-09_C0_G1` | 5.75 Er (8–1) | 0.0% | 4.4% | 1.59 (0–0) | 7.64 (0–0) | 8.95zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_C0_G2` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.62 (0–0) | 9.25zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-10_HERESY_MINUS1` | 5.73 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.54 (0–0) | 8.45zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-10_G0_H1` | 5.73 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.54 (0–0) | 8.45zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-12_HERESY_PLUS2` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.63 (0–0) | 8.87zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-12_COST_PLUS2` | 5.80 Er (8–1) | 0.0% | 5.5% | 1.54 (0–0) | 7.74 (0–0) | 9.08zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-12_C2_G1` | 5.73 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.52 (0–0) | 8.97zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_C0_G3` | 5.70 Er (8–1) | 0.0% | 4.5% | 1.52 (0–0) | 7.51 (0–0) | 9.31zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-12_HERESY_MINUS2` | 5.80 Er (8–1) | 0.0% | 4.8% | 1.54 (0–0) | 7.54 (0–0) | 8.84zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-01_COST_MINUS2` | 5.73 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.64 (0–0) | 8.88zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-01_C1_G1` | 5.73 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.64 (0–0) | 8.88zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-03_C0_H2` | 5.70 Er (8–1) | 0.0% | 3.7% | 1.51 (0–0) | 7.59 (0–0) | 8.96zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-10_G1_H2` | 5.79 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.74 (0–0) | 9.01zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-06_C0_G1` | 5.78 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.64 (0–0) | 9.06zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-06_C1_G2` | 5.78 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.65 (0–0) | 8.97zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-06_G1_H0` | 5.78 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.64 (0–0) | 9.06zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-01_COST_PLUS2` | 5.75 Er (8–1) | 0.0% | 5.9% | 1.53 (0–0) | 7.54 (0–0) | 8.97zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-05_COST_PLUS1` | 5.78 Er (8–1) | 0.0% | 5.4% | 1.53 (0–0) | 7.73 (0–0) | 9.05zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-05_C3_H0` | 5.78 Er (8–1) | 0.0% | 5.4% | 1.53 (0–0) | 7.73 (0–0) | 9.05zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-11_HERESY_PLUS1` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.66 (0–0) | 8.95zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-11_HERESY_SET1` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.66 (0–0) | 8.95zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-11_G0_H1` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.66 (0–0) | 8.95zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-09_COST_MINUS1` | 5.72 Er (8–1) | 0.0% | 4.8% | 1.52 (0–0) | 7.49 (0–0) | 9.09zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-09_G1_H2` | 5.72 Er (8–1) | 0.0% | 4.8% | 1.52 (0–0) | 7.68 (0–0) | 9.09zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-10_C5_G2` | 5.81 Er (8–1) | 0.0% | 4.9% | 1.55 (0–0) | 7.75 (0–0) | 9.21zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-06_COST_MINUS1` | 5.72 Er (8–1) | 0.0% | 4.6% | 1.54 (0–0) | 7.66 (0–0) | 9.04zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-06_C1_H0` | 5.72 Er (8–1) | 0.0% | 4.6% | 1.54 (0–0) | 7.66 (0–0) | 9.04zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-06_G1_H0` | 5.72 Er (8–1) | 0.0% | 4.6% | 1.54 (0–0) | 7.63 (0–0) | 9.05zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-12_HERESY_PLUS1` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.69 (0–0) | 8.78zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-12_HERESY_SET1` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.69 (0–0) | 8.78zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-06_COST_PLUS2` | 5.78 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.67 (0–0) | 9.18zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-12_C2_G2` | 5.73 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.53 (0–0) | 9.08zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-09_HERESY_PLUS1` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.68 (0–0) | 9.14zł (0.0–0.0) | 8.29 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-09_HERESY_SET1` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.68 (0–0) | 9.14zł (0.0–0.0) | 8.29 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-09_C0_H1` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.68 (0–0) | 9.14zł (0.0–0.0) | 8.29 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-09_G0_H1` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.68 (0–0) | 9.14zł (0.0–0.0) | 8.29 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-10_C5_H1` | 5.73 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.54 (0–0) | 8.23zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-04_HERESY_PLUS2` | 5.68 Er (8–1) | 0.0% | 4.9% | 1.50 (0–0) | 7.61 (0–0) | 9.00zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-04_HERESY_SET2` | 5.68 Er (8–1) | 0.0% | 4.9% | 1.50 (0–0) | 7.61 (0–0) | 9.00zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-03_COST_PLUS1` | 5.81 Er (8–1) | 0.0% | 5.2% | 1.55 (0–0) | 7.77 (0–0) | 8.96zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-05_COST_PLUS1` | 5.81 Er (8–1) | 0.0% | 5.2% | 1.55 (0–0) | 7.76 (0–0) | 8.97zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-09_C2_G2` | 5.72 Er (8–1) | 0.0% | 4.8% | 1.51 (0–0) | 7.49 (0–0) | 9.09zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-10_C5_G1` | 5.80 Er (8–1) | 0.0% | 5.0% | 1.55 (0–0) | 7.75 (0–0) | 9.11zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-10_G1_H1` | 5.73 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.53 (0–0) | 8.65zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-11_COST_PLUS1` | 5.78 Er (8–1) | 0.0% | 5.4% | 1.53 (0–0) | 7.67 (0–0) | 9.01zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-11_C2_H0` | 5.78 Er (8–1) | 0.0% | 5.4% | 1.53 (0–0) | 7.67 (0–0) | 9.01zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-12_C0_H1` | 5.64 Er (8–1) | 0.0% | 4.2% | 1.49 (0–0) | 7.45 (0–0) | 8.90zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-08_C0_G3` | 5.78 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.64 (0–0) | 9.46zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-05_C1_H2` | 5.64 Er (8–1) | 0.0% | 4.5% | 1.50 (0–0) | 7.49 (0–0) | 8.88zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-06_C3_G1` | 5.73 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.51 (0–0) | 8.98zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-04_HERESY_PLUS1` | 5.73 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.69 (0–0) | 8.80zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-04_HERESY_SET1` | 5.73 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.69 (0–0) | 8.80zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-04_C0_H1` | 5.73 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.69 (0–0) | 8.80zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-03_COST_MINUS1` | 5.71 Er (8–1) | 0.0% | 4.1% | 1.52 (0–0) | 7.57 (0–0) | 8.93zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-07_HERESY_PLUS2` | 5.68 Er (8–1) | 0.0% | 4.8% | 1.50 (0–0) | 7.57 (0–0) | 9.00zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-07_HERESY_SET2` | 5.68 Er (8–1) | 0.0% | 4.8% | 1.50 (0–0) | 7.57 (0–0) | 9.00zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-12_COST_PLUS1` | 5.81 Er (8–1) | 0.0% | 5.4% | 1.54 (0–0) | 7.76 (0–0) | 9.06zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-08_C2_G2` | 5.73 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.55 (0–0) | 9.09zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-08_G1_H0` | 5.73 Er (8–1) | 0.0% | 4.8% | 1.52 (0–0) | 7.53 (0–0) | 9.08zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-03_HERESY_MINUS2` | 5.79 Er (8–1) | 0.0% | 5.3% | 1.51 (0–0) | 7.72 (0–0) | 8.67zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-07_C1_H1` | 5.66 Er (8–1) | 0.0% | 4.5% | 1.50 (0–0) | 7.47 (0–0) | 8.90zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-08_COST_MINUS1` | 5.72 Er (8–1) | 0.0% | 4.7% | 1.52 (0–0) | 7.53 (0–0) | 9.07zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-08_C0_H0` | 5.72 Er (8–1) | 0.0% | 4.7% | 1.52 (0–0) | 7.53 (0–0) | 9.07zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-06_COST_PLUS2` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.70 (0–0) | 8.74zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-12_HERESY_MINUS2` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.55 (0–0) | 8.77zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-04_COST_PLUS1` | 5.79 Er (8–1) | 0.0% | 5.1% | 1.54 (0–0) | 7.73 (0–0) | 9.04zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-04_C3_H0` | 5.79 Er (8–1) | 0.0% | 5.1% | 1.54 (0–0) | 7.73 (0–0) | 9.04zł (0.0–0.0) | 8.22 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-09_C1_H1` | 5.65 Er (8–1) | 0.0% | 4.4% | 1.50 (0–0) | 7.47 (0–0) | 8.89zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-09_C3_G1` | 5.78 Er (8–1) | 0.0% | 5.1% | 1.53 (0–0) | 7.68 (0–0) | 9.05zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-02_C0_G4` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.52 (0–0) | 9.12zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-02_C1_G5` | 5.73 Er (8–1) | 0.0% | 5.0% | 1.51 (0–0) | 7.53 (0–0) | 9.14zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-02_G4_H0` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.52 (0–0) | 9.12zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-11_G2_H0` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.53 (0–0) | 9.09zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-10_C3_H1` | 5.73 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.54 (0–0) | 8.66zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-12_C2_H3` | 5.72 Er (8–1) | 0.0% | 5.3% | 1.51 (0–0) | 7.71 (0–0) | 9.05zł (0.0–0.0) | 8.26 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-12_G1_H0` | 5.74 Er (8–1) | 0.0% | 4.8% | 1.52 (0–0) | 7.54 (0–0) | 9.09zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-04_C2_H2` | 5.78 Er (8–1) | 0.0% | 4.8% | 1.55 (0–0) | 7.66 (0–0) | 9.21zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-07_HERESY_PLUS2` | 5.76 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.72 (0–0) | 9.23zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-07_HERESY_SET2` | 5.76 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.72 (0–0) | 9.23zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-05_C3_H2` | 5.71 Er (8–1) | 0.0% | 5.2% | 1.51 (0–0) | 7.70 (0–0) | 9.00zł (0.0–0.0) | 8.30 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-09_C0_G2` | 5.73 Er (8–1) | 0.0% | 4.3% | 1.60 (0–0) | 7.62 (0–0) | 9.08zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-02_C0_H1` | 5.75 Er (8–1) | 0.0% | 4.3% | 1.58 (0–0) | 7.75 (0–0) | 9.08zł (0.0–0.0) | 8.29 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-09_HERESY_PLUS1` | 5.71 Er (8–1) | 0.0% | 5.0% | 1.51 (0–0) | 7.62 (0–0) | 8.97zł (0.0–0.0) | 8.26 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-09_HERESY_SET1` | 5.71 Er (8–1) | 0.0% | 5.0% | 1.51 (0–0) | 7.62 (0–0) | 8.97zł (0.0–0.0) | 8.26 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-09_G0_H1` | 5.71 Er (8–1) | 0.0% | 5.0% | 1.51 (0–0) | 7.62 (0–0) | 8.97zł (0.0–0.0) | 8.26 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-09_G1_H1` | 5.64 Er (8–1) | 0.0% | 4.5% | 1.49 (0–0) | 7.42 (0–0) | 8.91zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-08_COST_PLUS2` | 5.78 Er (8–1) | 0.0% | 4.9% | 1.55 (0–0) | 7.68 (0–0) | 9.00zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-12_COST_MINUS1` | 5.73 Er (8–1) | 0.0% | 4.8% | 1.52 (0–0) | 7.53 (0–0) | 9.09zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-12_C0_H0` | 5.73 Er (8–1) | 0.0% | 4.8% | 1.52 (0–0) | 7.53 (0–0) | 9.09zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-09_HERESY_PLUS2` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.69 (0–0) | 9.24zł (0.0–0.0) | 8.29 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-09_HERESY_SET2` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.69 (0–0) | 9.24zł (0.0–0.0) | 8.29 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-02_G4_H1` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.72 (0–0) | 8.98zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-10_COST_PLUS1` | 5.81 Er (8–1) | 0.0% | 5.0% | 1.55 (0–0) | 7.76 (0–0) | 9.02zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-10_C5_H0` | 5.81 Er (8–1) | 0.0% | 5.0% | 1.55 (0–0) | 7.76 (0–0) | 9.02zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-11_COST_PLUS2` | 5.76 Er (8–1) | 0.0% | 5.7% | 1.53 (0–0) | 7.63 (0–0) | 8.99zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-03_C0_G1` | 5.70 Er (8–1) | 0.0% | 4.8% | 1.51 (0–0) | 7.48 (0–0) | 9.07zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-02_G3_H1` | 5.75 Er (8–1) | 0.0% | 4.5% | 1.58 (0–0) | 7.75 (0–0) | 9.09zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-02_HERESY_PLUS1` | 5.73 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.70 (0–0) | 8.97zł (0.0–0.0) | 8.29 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-02_HERESY_SET1` | 5.73 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.70 (0–0) | 8.97zł (0.0–0.0) | 8.29 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_C0_H0` | 5.75 Er (8–1) | 0.0% | 4.6% | 1.54 (0–0) | 7.49 (0–0) | 9.18zł (0.0–0.0) | 8.11 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-04_G0_H1` | 5.75 Er (8–1) | 0.0% | 5.4% | 1.50 (0–0) | 7.65 (0–0) | 8.92zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-12_HERESY_PLUS2` | 5.73 Er (8–1) | 0.0% | 4.6% | 1.51 (0–0) | 7.71 (0–0) | 9.08zł (0.0–0.0) | 8.26 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-07_COST_PLUS2` | 5.75 Er (8–1) | 0.0% | 5.4% | 1.48 (0–0) | 7.66 (0–0) | 8.79zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-02_G4_H1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.68 (0–0) | 9.08zł (0.0–0.0) | 8.26 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-03_HERESY_PLUS1` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.71 (0–0) | 8.89zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-03_C0_H2` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.71 (0–0) | 8.89zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-03_C2_H2` | 5.77 Er (8–1) | 0.0% | 5.6% | 1.53 (0–0) | 7.51 (0–0) | 9.04zł (0.0–0.0) | 8.11 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-11_C0_H1` | 5.67 Er (8–1) | 0.0% | 4.1% | 1.50 (0–0) | 7.55 (0–0) | 8.89zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-03_C1_G2` | 5.70 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.48 (0–0) | 9.07zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-02_COST_PLUS1` | 5.82 Er (8–1) | 0.0% | 5.4% | 1.55 (0–0) | 7.81 (0–0) | 8.92zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-02_C1_H0` | 5.82 Er (8–1) | 0.0% | 5.4% | 1.55 (0–0) | 7.81 (0–0) | 8.92zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-11_C2_G1` | 5.72 Er (8–1) | 0.0% | 5.1% | 1.51 (0–0) | 7.46 (0–0) | 8.96zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-01_G2_H0` | 5.75 Er (8–1) | 0.0% | 4.8% | 1.54 (0–0) | 7.50 (0–0) | 9.18zł (0.0–0.0) | 8.11 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-07_G4_H1` | 5.73 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.71 (0–0) | 9.04zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-09_HERESY_PLUS2` | 5.77 Er (8–1) | 0.0% | 4.8% | 1.54 (0–0) | 7.73 (0–0) | 9.20zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-09_HERESY_SET2` | 5.77 Er (8–1) | 0.0% | 4.8% | 1.54 (0–0) | 7.73 (0–0) | 9.20zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-09_C0_G2` | 5.73 Er (8–1) | 0.0% | 4.6% | 1.52 (0–0) | 7.47 (0–0) | 9.55zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-10_HERESY_PLUS2` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.67 (0–0) | 8.96zł (0.0–0.0) | 8.29 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-10_HERESY_SET2` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.67 (0–0) | 8.96zł (0.0–0.0) | 8.29 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-04_C2_H1` | 5.75 Er (8–1) | 0.0% | 5.4% | 1.49 (0–0) | 7.64 (0–0) | 8.90zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-10_COST_PLUS2` | 5.82 Er (8–1) | 0.0% | 5.0% | 1.55 (0–0) | 7.78 (0–0) | 8.71zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-12_C0_H1` | 5.71 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.71 (0–0) | 8.97zł (0.0–0.0) | 8.30 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-12_G5_H1` | 5.71 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.71 (0–0) | 8.97zł (0.0–0.0) | 8.30 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-04_G1_H1` | 5.65 Er (8–1) | 0.0% | 4.6% | 1.50 (0–0) | 7.42 (0–0) | 8.91zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-12_G1_H3` | 5.61 Er (8–1) | 0.0% | 4.5% | 1.48 (0–0) | 7.55 (0–0) | 8.93zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-12_G1_H1` | 5.64 Er (8–1) | 0.0% | 4.5% | 1.49 (0–0) | 7.41 (0–0) | 8.90zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-10_G1_H2` | 5.83 Er (8–1) | 0.0% | 4.3% | 1.57 (0–0) | 7.69 (0–0) | 9.48zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-07_COST_MINUS1` | 5.71 Er (8–1) | 0.0% | 4.6% | 1.52 (0–0) | 7.48 (0–0) | 8.92zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-07_C1_H0` | 5.71 Er (8–1) | 0.0% | 4.6% | 1.52 (0–0) | 7.48 (0–0) | 8.92zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-12_COST_PLUS2` | 5.78 Er (8–1) | 0.0% | 5.1% | 1.53 (0–0) | 7.75 (0–0) | 8.88zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-06_COST_MINUS2` | 5.72 Er (8–1) | 0.0% | 4.7% | 1.52 (0–0) | 7.48 (0–0) | 9.21zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-10_COST_PLUS2` | 5.87 Er (8–1) | 0.0% | 4.5% | 1.44 (0–0) | 7.73 (0–0) | 9.47zł (0.0–0.0) | 8.12 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-05_COST_MINUS1` | 5.70 Er (8–1) | 0.0% | 4.8% | 1.51 (0–0) | 7.46 (0–0) | 9.03zł (0.0–0.0) | 8.11 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-09_COST_MINUS1` | 5.70 Er (8–1) | 0.0% | 4.4% | 1.51 (0–0) | 7.47 (0–0) | 8.90zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-09_C1_H0` | 5.70 Er (8–1) | 0.0% | 4.4% | 1.51 (0–0) | 7.47 (0–0) | 8.90zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-06_C1_G1` | 5.72 Er (8–1) | 0.0% | 4.7% | 1.52 (0–0) | 7.48 (0–0) | 9.21zł (0.0–0.0) | 8.12 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-03_COST_PLUS2` | 5.76 Er (8–1) | 0.0% | 5.6% | 1.53 (0–0) | 7.46 (0–0) | 9.02zł (0.0–0.0) | 8.10 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-03_HERESY_MINUS1` | 5.80 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.53 (0–0) | 9.06zł (0.0–0.0) | 8.07 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-03_C0_H1` | 5.80 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.53 (0–0) | 9.06zł (0.0–0.0) | 8.07 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-03_G0_H1` | 5.80 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.53 (0–0) | 9.06zł (0.0–0.0) | 8.07 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-10_COST_MINUS1` | 5.70 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.44 (0–0) | 8.98zł (0.0–0.0) | 8.11 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-10_C3_H0` | 5.70 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.44 (0–0) | 8.98zł (0.0–0.0) | 8.11 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-05_HERESY_PLUS2` | 5.62 Er (8–1) | 0.0% | 4.9% | 1.49 (0–0) | 7.53 (0–0) | 8.93zł (0.0–0.0) | 8.29 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-06_C1_G1` | 5.69 Er (8–1) | 0.0% | 4.3% | 1.54 (0–0) | 7.62 (0–0) | 9.14zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-05_C2_G2` | 5.69 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.43 (0–0) | 9.01zł (0.0–0.0) | 8.10 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-09_C3_G2` | 5.69 Er (8–1) | 0.0% | 4.8% | 1.50 (0–0) | 7.43 (0–0) | 8.98zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-12_HERESY_PLUS2` | 5.71 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.77 (0–0) | 8.71zł (0.0–0.0) | 8.31 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-12_HERESY_SET2` | 5.71 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.77 (0–0) | 8.71zł (0.0–0.0) | 8.31 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-04_HERESY_PLUS2` | 5.78 Er (8–1) | 0.0% | 4.8% | 1.55 (0–0) | 7.70 (0–0) | 9.35zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-12_C0_H3` | 5.62 Er (8–1) | 0.0% | 3.9% | 1.49 (0–0) | 7.61 (0–0) | 8.93zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-02_G2_H0` | 5.82 Er (8–1) | 0.0% | 5.0% | 1.55 (0–0) | 7.84 (0–0) | 8.91zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-11_COST_PLUS1` | 5.80 Er (8–1) | 0.0% | 5.1% | 1.54 (0–0) | 7.76 (0–0) | 8.94zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-11_C3_H0` | 5.80 Er (8–1) | 0.0% | 5.1% | 1.54 (0–0) | 7.76 (0–0) | 8.94zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-06_COST_MINUS2` | 5.69 Er (8–1) | 0.0% | 4.3% | 1.54 (0–0) | 7.63 (0–0) | 9.15zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-03_HERESY_MINUS1` | 5.81 Er (8–1) | 0.0% | 5.0% | 1.55 (0–0) | 7.53 (0–0) | 9.10zł (0.0–0.0) | 8.03 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-03_C0_H0` | 5.81 Er (8–1) | 0.0% | 5.0% | 1.55 (0–0) | 7.53 (0–0) | 9.10zł (0.0–0.0) | 8.03 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-03_C1_H0` | 5.81 Er (8–1) | 0.0% | 5.0% | 1.55 (0–0) | 7.51 (0–0) | 8.83zł (0.0–0.0) | 8.03 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-03_G1_H0` | 5.81 Er (8–1) | 0.0% | 5.0% | 1.55 (0–0) | 7.51 (0–0) | 8.85zł (0.0–0.0) | 8.03 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-03_G3_H0` | 5.81 Er (8–1) | 0.0% | 5.0% | 1.55 (0–0) | 7.53 (0–0) | 9.35zł (0.0–0.0) | 8.03 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-03_G3_H2` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.71 (0–0) | 9.08zł (0.0–0.0) | 8.30 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-10_HERESY_MINUS2` | 5.73 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.46 (0–0) | 8.37zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-06_C1_H1` | 5.71 Er (8–1) | 0.0% | 4.5% | 1.51 (0–0) | 7.52 (0–0) | 8.98zł (0.0–0.0) | 8.23 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-03_C2_G1` | 5.74 Er (8–1) | 0.0% | 5.4% | 1.52 (0–0) | 7.47 (0–0) | 8.99zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-03_HERESY_PLUS1` | 5.79 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.84 (0–0) | 9.02zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-03_C0_H3` | 5.79 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.84 (0–0) | 9.02zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-03_G0_H3` | 5.79 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.84 (0–0) | 9.02zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-07_C0_G1` | 5.72 Er (8–1) | 0.0% | 4.6% | 1.52 (0–0) | 7.46 (0–0) | 9.21zł (0.0–0.0) | 8.11 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-09_HERESY_PLUS1` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.79 (0–0) | 9.03zł (0.0–0.0) | 8.29 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-09_G0_H2` | 5.76 Er (8–1) | 0.0% | 5.0% | 1.53 (0–0) | 7.79 (0–0) | 9.03zł (0.0–0.0) | 8.29 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-05_COST_MINUS1` | 5.70 Er (8–1) | 0.0% | 4.4% | 1.51 (0–0) | 7.45 (0–0) | 8.89zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-05_C1_H0` | 5.70 Er (8–1) | 0.0% | 4.4% | 1.51 (0–0) | 7.45 (0–0) | 8.89zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-11_COST_MINUS1` | 5.69 Er (8–1) | 0.0% | 4.2% | 1.51 (0–0) | 7.47 (0–0) | 8.91zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-11_C0_H0` | 5.69 Er (8–1) | 0.0% | 4.2% | 1.51 (0–0) | 7.47 (0–0) | 8.91zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-09_COST_PLUS2` | 5.82 Er (8–1) | 0.0% | 5.4% | 1.55 (0–0) | 7.83 (0–0) | 8.91zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-05_HERESY_PLUS1` | 5.70 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.71 (0–0) | 8.88zł (0.0–0.0) | 8.32 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-05_HERESY_SET1` | 5.70 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.71 (0–0) | 8.88zł (0.0–0.0) | 8.32 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-05_C0_H1` | 5.70 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.71 (0–0) | 8.88zł (0.0–0.0) | 8.32 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-05_C1_H1` | 5.70 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.71 (0–0) | 8.62zł (0.0–0.0) | 8.32 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-05_G3_H1` | 5.70 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.71 (0–0) | 8.63zł (0.0–0.0) | 8.32 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-05_G5_H1` | 5.70 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.71 (0–0) | 9.13zł (0.0–0.0) | 8.32 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-01_C2_G2` | 5.72 Er (8–1) | 0.0% | 5.6% | 1.52 (0–0) | 7.45 (0–0) | 8.95zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-10_C4_H2` | 5.83 Er (8–1) | 0.0% | 4.4% | 1.62 (0–0) | 7.69 (0–0) | 9.41zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-10_C5_H1` | 5.78 Er (8–1) | 0.0% | 5.0% | 1.54 (0–0) | 7.75 (0–0) | 8.99zł (0.0–0.0) | 8.29 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-04_COST_PLUS2` | 5.76 Er (8–1) | 0.0% | 5.6% | 1.46 (0–0) | 7.56 (0–0) | 8.83zł (0.0–0.0) | 8.11 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-09_HERESY_MINUS1` | 5.82 Er (8–1) | 0.0% | 4.9% | 1.55 (0–0) | 7.55 (0–0) | 9.10zł (0.0–0.0) | 8.06 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-09_G0_H0` | 5.82 Er (8–1) | 0.0% | 4.9% | 1.55 (0–0) | 7.55 (0–0) | 9.10zł (0.0–0.0) | 8.06 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-10_HERESY_PLUS1` | 5.84 Er (8–1) | 0.0% | 4.4% | 1.54 (0–0) | 7.70 (0–0) | 9.44zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-10_G0_H2` | 5.84 Er (8–1) | 0.0% | 4.4% | 1.54 (0–0) | 7.70 (0–0) | 9.44zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-04_HERESY_PLUS2` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.73 (0–0) | 8.72zł (0.0–0.0) | 8.31 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-04_HERESY_SET2` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.73 (0–0) | 8.72zł (0.0–0.0) | 8.31 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-04_G4_H1` | 5.73 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.74 (0–0) | 9.01zł (0.0–0.0) | 8.31 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-06_C0_G2` | 5.79 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.66 (0–0) | 9.08zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-01_C1_G2` | 5.70 Er (8–1) | 0.0% | 4.8% | 1.51 (0–0) | 7.73 (0–0) | 8.78zł (0.0–0.0) | 8.31 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-01_C0_H0` | 5.74 Er (8–1) | 0.0% | 4.4% | 1.53 (0–0) | 7.46 (0–0) | 8.94zł (0.0–0.0) | 8.11 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-03_HERESY_PLUS2` | 5.71 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.78 (0–0) | 8.83zł (0.0–0.0) | 8.31 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-09_C0_H0` | 5.83 Er (8–1) | 0.0% | 4.8% | 1.55 (0–0) | 7.52 (0–0) | 9.32zł (0.0–0.0) | 8.06 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-11_COST_MINUS1` | 5.70 Er (8–1) | 0.0% | 4.8% | 1.51 (0–0) | 7.46 (0–0) | 9.06zł (0.0–0.0) | 8.12 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-11_C1_H0` | 5.70 Er (8–1) | 0.0% | 4.8% | 1.51 (0–0) | 7.46 (0–0) | 9.06zł (0.0–0.0) | 8.12 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-10_C3_G1` | 5.69 Er (8–1) | 0.0% | 4.9% | 1.51 (0–0) | 7.42 (0–0) | 9.10zł (0.0–0.0) | 8.10 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-11_G2_H1` | 5.75 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.77 (0–0) | 9.10zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-03_G1_H2` | 5.69 Er (8–1) | 0.0% | 4.6% | 1.51 (0–0) | 7.45 (0–0) | 8.95zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-10_C6_H2` | 5.86 Er (8–1) | 0.0% | 4.2% | 1.43 (0–0) | 7.72 (0–0) | 9.60zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-10_COST_PLUS1` | 5.81 Er (8–1) | 0.0% | 5.0% | 1.55 (0–0) | 7.78 (0–0) | 9.39zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-06_G1_H0` | 5.72 Er (8–1) | 0.0% | 4.8% | 1.51 (0–0) | 7.47 (0–0) | 8.97zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-12_COST_MINUS1` | 5.67 Er (8–1) | 0.0% | 4.3% | 1.50 (0–0) | 7.39 (0–0) | 8.89zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-10_C3_G2` | 5.69 Er (8–1) | 0.0% | 4.8% | 1.51 (0–0) | 7.42 (0–0) | 9.23zł (0.0–0.0) | 8.10 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-02_C0_G5` | 5.71 Er (8–1) | 0.0% | 4.8% | 1.51 (0–0) | 7.44 (0–0) | 9.32zł (0.0–0.0) | 8.10 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-11_C1_H1` | 5.75 Er (8–1) | 0.0% | 4.8% | 1.53 (0–0) | 7.77 (0–0) | 9.11zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-09_G1_H1` | 5.71 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.69 (0–0) | 9.11zł (0.0–0.0) | 8.31 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-07_G1_H1` | 5.66 Er (8–1) | 0.0% | 4.6% | 1.50 (0–0) | 7.42 (0–0) | 8.93zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-12_HERESY_PLUS1` | 5.66 Er (8–1) | 0.0% | 4.8% | 1.50 (0–0) | 7.68 (0–0) | 8.98zł (0.0–0.0) | 8.29 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-12_G0_H3` | 5.66 Er (8–1) | 0.0% | 4.8% | 1.50 (0–0) | 7.68 (0–0) | 8.98zł (0.0–0.0) | 8.29 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-05_HERESY_PLUS1` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.82 (0–0) | 9.06zł (0.0–0.0) | 8.30 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-05_G0_H2` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.82 (0–0) | 9.06zł (0.0–0.0) | 8.30 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-09_G1_H0` | 5.83 Er (8–1) | 0.0% | 4.8% | 1.55 (0–0) | 7.52 (0–0) | 9.32zł (0.0–0.0) | 8.06 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-06_G1_H1` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.71 (0–0) | 9.11zł (0.0–0.0) | 8.26 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-11_G1_H1` | 5.64 Er (8–1) | 0.0% | 4.5% | 1.49 (0–0) | 7.43 (0–0) | 8.89zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-10_C1_H1` | 5.71 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.73 (0–0) | 9.29zł (0.0–0.0) | 8.33 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-10_G1_H1` | 5.72 Er (8–1) | 0.0% | 4.9% | 1.52 (0–0) | 7.74 (0–0) | 9.29zł (0.0–0.0) | 8.33 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-03_C0_G2` | 5.67 Er (8–1) | 0.0% | 4.7% | 1.50 (0–0) | 7.39 (0–0) | 9.23zł (0.0–0.0) | 8.10 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-09_G1_H0` | 5.68 Er (8–1) | 0.0% | 4.5% | 1.50 (0–0) | 7.42 (0–0) | 8.92zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-12_C0_G1` | 5.71 Er (8–1) | 0.0% | 4.7% | 1.51 (0–0) | 7.42 (0–0) | 9.23zł (0.0–0.0) | 8.10 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-10_HERESY_PLUS1` | 5.83 Er (8–1) | 0.0% | 5.0% | 1.56 (0–0) | 7.82 (0–0) | 9.54zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-10_G0_H3` | 5.83 Er (8–1) | 0.0% | 5.0% | 1.56 (0–0) | 7.82 (0–0) | 9.54zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-10_C3_H3` | 5.82 Er (8–1) | 0.0% | 5.0% | 1.56 (0–0) | 7.79 (0–0) | 9.53zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-05_G1_H2` | 5.61 Er (8–1) | 0.0% | 4.5% | 1.48 (0–0) | 7.38 (0–0) | 8.87zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-10_G1_H3` | 5.82 Er (8–1) | 0.0% | 5.0% | 1.56 (0–0) | 7.81 (0–0) | 9.54zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-08_C2_G2` | 5.61 Er (8–1) | 0.0% | 4.6% | 1.49 (0–0) | 7.32 (0–0) | 8.85zł (0.0–0.0) | 8.16 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-06_C1_G2` | 5.66 Er (8–1) | 0.0% | 4.1% | 1.54 (0–0) | 7.61 (0–0) | 9.28zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-10_COST_PLUS2` | 5.82 Er (8–1) | 0.0% | 5.0% | 1.56 (0–0) | 7.81 (0–0) | 9.54zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_PLUS1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.78 (0–0) | 9.17zł (0.0–0.0) | 8.34 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_SET1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.78 (0–0) | 9.17zł (0.0–0.0) | 8.34 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-10_G0_H1` | 5.74 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.78 (0–0) | 9.17zł (0.0–0.0) | 8.34 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-06_COST_PLUS2` | 5.70 Er (8–1) | 0.0% | 4.8% | 1.51 (0–0) | 7.42 (0–0) | 8.97zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-05_HERESY_MINUS1` | 5.80 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.51 (0–0) | 9.03zł (0.0–0.0) | 8.04 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-05_G0_H0` | 5.80 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.51 (0–0) | 9.03zł (0.0–0.0) | 8.04 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-10_C5_H3` | 5.82 Er (8–1) | 0.0% | 5.0% | 1.55 (0–0) | 7.81 (0–0) | 9.54zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-04_C0_G1` | 5.70 Er (8–1) | 0.0% | 4.6% | 1.52 (0–0) | 7.48 (0–0) | 9.23zł (0.0–0.0) | 8.11 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-05_C0_G1` | 5.67 Er (8–1) | 0.0% | 4.7% | 1.50 (0–0) | 7.37 (0–0) | 9.17zł (0.0–0.0) | 8.07 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-07_G1_H0` | 5.69 Er (8–1) | 0.0% | 4.6% | 1.51 (0–0) | 7.42 (0–0) | 8.93zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |
| `L3_GC-10_HERESY_PLUS2` | 5.83 Er (8–1) | 0.0% | 5.0% | 1.56 (0–0) | 7.83 (0–0) | 9.61zł (0.0–0.0) | 8.21 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-08_C0_G1` | 5.66 Er (8–1) | 0.0% | 4.7% | 1.50 (0–0) | 7.37 (0–0) | 9.15zł (0.0–0.0) | 8.09 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-05_G1_H0` | 5.67 Er (8–1) | 0.0% | 4.4% | 1.50 (0–0) | 7.36 (0–0) | 8.89zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-03_COST_PLUS2` | 5.86 Er (8–1) | 0.0% | 5.5% | 1.56 (0–0) | 7.88 (0–0) | 9.03zł (0.0–0.0) | 8.29 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-11_C1_G2` | 5.69 Er (8–1) | 0.0% | 4.7% | 1.51 (0–0) | 7.42 (0–0) | 9.23zł (0.0–0.0) | 8.10 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-06_HERESY_PLUS1` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.75 (0–0) | 9.20zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-06_HERESY_SET1` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.75 (0–0) | 9.20zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-06_C0_H1` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.75 (0–0) | 9.20zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-06_G0_H1` | 5.77 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.75 (0–0) | 9.20zł (0.0–0.0) | 8.25 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-07_C3_G2` | 5.68 Er (8–1) | 0.0% | 4.7% | 1.50 (0–0) | 7.41 (0–0) | 8.93zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-03_C0_H0` | 5.74 Er (8–1) | 0.0% | 4.3% | 1.53 (0–0) | 7.49 (0–0) | 8.96zł (0.0–0.0) | 8.09 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-06_HERESY_PLUS1` | 5.69 Er (8–1) | 0.0% | 4.8% | 1.51 (0–0) | 7.43 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-06_HERESY_SET1` | 5.69 Er (8–1) | 0.0% | 4.8% | 1.51 (0–0) | 7.43 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-06_G0_H1` | 5.69 Er (8–1) | 0.0% | 4.8% | 1.51 (0–0) | 7.43 (0–0) | 8.99zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-09_C2_H2` | 5.79 Er (8–1) | 0.0% | 5.2% | 1.54 (0–0) | 7.87 (0–0) | 9.01zł (0.0–0.0) | 8.32 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-05_COST_PLUS2` | 5.85 Er (8–1) | 0.0% | 5.4% | 1.56 (0–0) | 7.91 (0–0) | 8.97zł (0.0–0.0) | 8.30 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-06_C1_G2` | 5.69 Er (8–1) | 0.0% | 4.6% | 1.51 (0–0) | 7.37 (0–0) | 9.38zł (0.0–0.0) | 8.08 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-04_G1_H0` | 5.67 Er (8–1) | 0.0% | 4.5% | 1.50 (0–0) | 7.36 (0–0) | 8.90zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-05_C2_H2` | 5.80 Er (8–1) | 0.0% | 5.1% | 1.54 (0–0) | 7.89 (0–0) | 9.05zł (0.0–0.0) | 8.33 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-10_C3_H1` | 5.78 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.85 (0–0) | 9.19zł (0.0–0.0) | 8.34 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-10_COST_MINUS2` | 5.66 Er (8–1) | 0.0% | 4.8% | 1.50 (0–0) | 7.32 (0–0) | 9.03zł (0.0–0.0) | 8.06 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-07_C0_G2` | 5.68 Er (8–1) | 0.0% | 4.6% | 1.51 (0–0) | 7.37 (0–0) | 9.42zł (0.0–0.0) | 8.07 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-12_C0_G2` | 5.69 Er (8–1) | 0.0% | 4.6% | 1.51 (0–0) | 7.35 (0–0) | 9.39zł (0.0–0.0) | 8.07 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-03_G1_H1` | 5.74 Er (8–1) | 0.0% | 4.8% | 1.52 (0–0) | 7.38 (0–0) | 9.16zł (0.0–0.0) | 8.00 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-06_G1_H1` | 5.68 Er (8–1) | 0.0% | 4.7% | 1.50 (0–0) | 7.40 (0–0) | 8.97zł (0.0–0.0) | 8.19 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-03_C1_H3` | 5.83 Er (8–1) | 0.0% | 5.3% | 1.56 (0–0) | 7.93 (0–0) | 9.06zł (0.0–0.0) | 8.31 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-02_HERESY_PLUS1` | 5.77 Er (8–1) | 0.0% | 5.0% | 1.54 (0–0) | 7.89 (0–0) | 8.87zł (0.0–0.0) | 8.35 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-02_HERESY_SET1` | 5.77 Er (8–1) | 0.0% | 5.0% | 1.54 (0–0) | 7.89 (0–0) | 8.87zł (0.0–0.0) | 8.35 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-02_C0_H1` | 5.77 Er (8–1) | 0.0% | 5.0% | 1.54 (0–0) | 7.89 (0–0) | 8.87zł (0.0–0.0) | 8.35 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-06_C1_H1` | 5.79 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.78 (0–0) | 9.25zł (0.0–0.0) | 8.26 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-11_G1_H0` | 5.67 Er (8–1) | 0.0% | 4.5% | 1.50 (0–0) | 7.35 (0–0) | 8.91zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-11_COST_MINUS2` | 5.67 Er (8–1) | 0.0% | 4.6% | 1.50 (0–0) | 7.35 (0–0) | 9.20zł (0.0–0.0) | 8.07 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-08_C0_G2` | 5.63 Er (8–1) | 0.0% | 4.7% | 1.49 (0–0) | 7.32 (0–0) | 9.31zł (0.0–0.0) | 8.06 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-06_HERESY_PLUS2` | 5.68 Er (8–1) | 0.0% | 4.8% | 1.50 (0–0) | 7.40 (0–0) | 9.00zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-06_HERESY_SET2` | 5.68 Er (8–1) | 0.0% | 4.8% | 1.50 (0–0) | 7.40 (0–0) | 9.00zł (0.0–0.0) | 8.18 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-06_C3_H1` | 5.69 Er (8–1) | 0.0% | 4.8% | 1.50 (0–0) | 7.38 (0–0) | 9.00zł (0.0–0.0) | 8.17 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-01_G1_H0` | 5.71 Er (8–1) | 0.0% | 4.8% | 1.52 (0–0) | 7.35 (0–0) | 8.92zł (0.0–0.0) | 8.08 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-02_G3_H1` | 5.59 Er (8–1) | 0.0% | 4.6% | 1.47 (0–0) | 7.28 (0–0) | 8.83zł (0.0–0.0) | 8.20 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-05_C0_G2` | 5.64 Er (8–1) | 0.0% | 4.6% | 1.49 (0–0) | 7.30 (0–0) | 9.34zł (0.0–0.0) | 8.04 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-10_COST_PLUS2` | 5.85 Er (8–1) | 0.0% | 5.0% | 1.56 (0–0) | 7.93 (0–0) | 9.10zł (0.0–0.0) | 8.32 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-06_COST_MINUS2` | 5.69 Er (8–1) | 0.0% | 3.9% | 1.50 (0–0) | 7.38 (0–0) | 8.89zł (0.0–0.0) | 8.12 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-02_HERESY_PLUS2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.85 (0–0) | 9.02zł (0.0–0.0) | 8.33 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-02_HERESY_SET2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.85 (0–0) | 9.02zł (0.0–0.0) | 8.33 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-11_C1_G3` | 5.67 Er (8–1) | 0.0% | 4.7% | 1.50 (0–0) | 7.34 (0–0) | 9.40zł (0.0–0.0) | 8.07 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-09_HERESY_PLUS2` | 5.71 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.74 (0–0) | 9.03zł (0.0–0.0) | 8.31 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-09_HERESY_SET2` | 5.71 Er (8–1) | 0.0% | 5.0% | 1.52 (0–0) | 7.74 (0–0) | 9.03zł (0.0–0.0) | 8.31 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-03_HERESY_MINUS2` | 5.87 Er (8–1) | 0.0% | 4.9% | 1.56 (0–0) | 7.50 (0–0) | 9.18zł (0.0–0.0) | 7.93 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-03_HERESY_PLUS2` | 5.87 Er (8–1) | 0.0% | 4.9% | 1.57 (0–0) | 8.04 (0–0) | 9.18zł (0.0–0.0) | 8.31 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-09_HERESY_PLUS2` | 5.80 Er (8–1) | 0.0% | 5.0% | 1.55 (0–0) | 8.01 (0–0) | 9.12zł (0.0–0.0) | 8.35 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-11_HERESY_PLUS1` | 5.78 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.87 (0–0) | 9.02zł (0.0–0.0) | 8.35 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-11_HERESY_SET1` | 5.78 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.87 (0–0) | 9.02zł (0.0–0.0) | 8.35 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-06_HERESY_PLUS2` | 5.80 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.82 (0–0) | 9.35zł (0.0–0.0) | 8.26 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-06_HERESY_SET2` | 5.80 Er (8–1) | 0.0% | 4.9% | 1.54 (0–0) | 7.82 (0–0) | 9.35zł (0.0–0.0) | 8.26 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-06_C3_G2` | 5.69 Er (8–1) | 0.0% | 5.0% | 1.50 (0–0) | 7.36 (0–0) | 8.95zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-04_C0_G2` | 5.67 Er (8–1) | 0.0% | 4.6% | 1.51 (0–0) | 7.37 (0–0) | 9.37zł (0.0–0.0) | 8.07 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-05_HERESY_PLUS2` | 5.65 Er (8–1) | 0.0% | 4.8% | 1.51 (0–0) | 7.79 (0–0) | 8.77zł (0.0–0.0) | 8.43 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-05_HERESY_SET2` | 5.65 Er (8–1) | 0.0% | 4.8% | 1.51 (0–0) | 7.79 (0–0) | 8.77zł (0.0–0.0) | 8.43 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-05_HERESY_PLUS2` | 5.81 Er (8–1) | 0.0% | 5.0% | 1.55 (0–0) | 8.02 (0–0) | 9.14zł (0.0–0.0) | 8.37 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-05_C3_G2` | 5.62 Er (8–1) | 0.0% | 4.6% | 1.48 (0–0) | 7.25 (0–0) | 8.87zł (0.0–0.0) | 8.11 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-11_COST_PLUS2` | 5.81 Er (8–1) | 0.0% | 5.1% | 1.54 (0–0) | 7.90 (0–0) | 8.91zł (0.0–0.0) | 8.35 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-03_G1_H0` | 5.70 Er (8–1) | 0.0% | 4.6% | 1.51 (0–0) | 7.32 (0–0) | 8.93zł (0.0–0.0) | 8.05 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-04_C3_G2` | 5.64 Er (8–1) | 0.0% | 4.8% | 1.49 (0–0) | 7.26 (0–0) | 8.89zł (0.0–0.0) | 8.11 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-07_COST_MINUS2` | 5.61 Er (8–1) | 0.0% | 3.8% | 1.48 (0–0) | 7.21 (0–0) | 8.80zł (0.0–0.0) | 8.10 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-05_G1_H0` | 5.74 Er (8–1) | 0.0% | 4.8% | 1.52 (0–0) | 7.33 (0–0) | 9.09zł (0.0–0.0) | 7.97 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-02_C2_H1` | 5.85 Er (8–1) | 0.0% | 6.0% | 1.56 (0–0) | 7.91 (0–0) | 9.11zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-05_C0_H0` | 5.74 Er (8–1) | 0.0% | 4.8% | 1.52 (0–0) | 7.33 (0–0) | 9.10zł (0.0–0.0) | 7.96 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-09_COST_MINUS2` | 5.60 Er (8–1) | 0.0% | 3.7% | 1.48 (0–0) | 7.21 (0–0) | 8.81zł (0.0–0.0) | 8.11 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-03_C2_G2` | 5.65 Er (8–1) | 0.0% | 5.1% | 1.50 (0–0) | 7.22 (0–0) | 8.90zł (0.0–0.0) | 8.10 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-09_COST_PLUS1` | 5.85 Er (8–1) | 0.0% | 5.5% | 1.56 (0–0) | 7.92 (0–0) | 9.11zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-09_C3_H0` | 5.85 Er (8–1) | 0.0% | 5.5% | 1.56 (0–0) | 7.92 (0–0) | 9.11zł (0.0–0.0) | 8.24 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-09_C3_H1` | 5.80 Er (8–1) | 0.0% | 5.4% | 1.54 (0–0) | 7.89 (0–0) | 9.09zł (0.0–0.0) | 8.29 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-11_G0_H1` | 5.80 Er (8–1) | 0.0% | 5.0% | 1.54 (0–0) | 7.92 (0–0) | 8.98zł (0.0–0.0) | 8.38 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-11_C3_H1` | 5.80 Er (8–1) | 0.0% | 5.0% | 1.54 (0–0) | 7.93 (0–0) | 9.00zł (0.0–0.0) | 8.39 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-04_COST_MINUS2` | 5.58 Er (8–1) | 0.0% | 3.8% | 1.48 (0–0) | 7.14 (0–0) | 8.76zł (0.0–0.0) | 8.08 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-01_C0_G1` | 5.59 Er (8–1) | 0.0% | 3.9% | 1.48 (0–0) | 7.12 (0–0) | 8.81zł (0.0–0.0) | 8.13 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-10_HERESY_PLUS2` | 5.86 Er (8–1) | 0.0% | 4.8% | 1.57 (0–0) | 7.99 (0–0) | 9.12zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-03_C0_G1` | 5.61 Er (8–1) | 0.0% | 3.8% | 1.48 (0–0) | 7.26 (0–0) | 8.84zł (0.0–0.0) | 8.15 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-02_G3_H0` | 5.60 Er (8–1) | 0.0% | 4.5% | 1.48 (0–0) | 7.17 (0–0) | 8.82zł (0.0–0.0) | 8.09 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-02_G1_H0` | 5.88 Er (8–1) | 0.0% | 5.4% | 1.57 (0–0) | 8.00 (0–0) | 9.11zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-02_COST_PLUS2` | 5.87 Er (8–1) | 0.0% | 5.8% | 1.56 (0–0) | 8.08 (0–0) | 8.85zł (0.0–0.0) | 8.40 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-12_C2_G2` | 5.62 Er (8–1) | 0.0% | 4.6% | 1.47 (0–0) | 7.19 (0–0) | 8.87zł (0.0–0.0) | 8.10 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-10_C5_G4` | 5.90 Er (8–1) | 0.0% | 4.9% | 1.58 (0–0) | 8.08 (0–0) | 9.18zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-06_C1_G1` | 5.66 Er (8–1) | 0.0% | 4.3% | 1.49 (0–0) | 7.24 (0–0) | 8.89zł (0.0–0.0) | 8.09 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-10_C5_H0` | 5.90 Er (8–1) | 0.0% | 4.9% | 1.58 (0–0) | 8.09 (0–0) | 9.16zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-07_C1_G1` | 5.59 Er (8–1) | 0.0% | 4.0% | 1.47 (0–0) | 7.12 (0–0) | 8.79zł (0.0–0.0) | 8.07 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-02_C1_H1` | 5.83 Er (8–1) | 0.0% | 5.6% | 1.55 (0–0) | 8.05 (0–0) | 8.83zł (0.0–0.0) | 8.43 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-02_G2_H1` | 5.83 Er (8–1) | 0.0% | 5.0% | 1.56 (0–0) | 8.06 (0–0) | 8.84zł (0.0–0.0) | 8.43 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-11_HERESY_PLUS2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.93 (0–0) | 9.03zł (0.0–0.0) | 8.43 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-11_HERESY_SET2` | 5.76 Er (8–1) | 0.0% | 4.9% | 1.53 (0–0) | 7.93 (0–0) | 9.03zł (0.0–0.0) | 8.43 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-09_C1_G1` | 5.57 Er (8–1) | 0.0% | 3.9% | 1.47 (0–0) | 7.13 (0–0) | 8.81zł (0.0–0.0) | 8.08 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-02_C2_G3` | 5.66 Er (8–1) | 0.0% | 5.4% | 1.49 (0–0) | 7.25 (0–0) | 8.92zł (0.0–0.0) | 8.14 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-10_C5_G3` | 5.90 Er (8–1) | 0.0% | 4.9% | 1.58 (0–0) | 8.09 (0–0) | 9.17zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-10_COST_PLUS1` | 5.91 Er (8–1) | 0.0% | 4.9% | 1.58 (0–0) | 8.11 (0–0) | 9.16zł (0.0–0.0) | 8.28 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-11_C0_G1` | 5.59 Er (8–1) | 0.0% | 3.8% | 1.47 (0–0) | 7.12 (0–0) | 8.81zł (0.0–0.0) | 8.10 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-04_C1_G1` | 5.56 Er (8–1) | 0.0% | 4.0% | 1.47 (0–0) | 7.07 (0–0) | 8.75zł (0.0–0.0) | 8.06 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-05_COST_MINUS2` | 5.58 Er (8–1) | 0.0% | 3.8% | 1.48 (0–0) | 7.13 (0–0) | 8.78zł (0.0–0.0) | 8.08 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-02_G1_H1` | 5.86 Er (8–1) | 0.0% | 5.3% | 1.56 (0–0) | 8.03 (0–0) | 9.10zł (0.0–0.0) | 8.34 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-10_C5_H2` | 5.91 Er (8–1) | 0.0% | 4.9% | 1.59 (0–0) | 8.12 (0–0) | 9.17zł (0.0–0.0) | 8.29 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-11_C2_G2` | 5.60 Er (8–1) | 0.0% | 4.8% | 1.48 (0–0) | 7.12 (0–0) | 8.85zł (0.0–0.0) | 8.10 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-05_C1_G1` | 5.56 Er (8–1) | 0.0% | 3.9% | 1.47 (0–0) | 7.08 (0–0) | 8.77zł (0.0–0.0) | 8.07 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-02_COST_PLUS2` | 5.91 Er (8–1) | 0.0% | 6.4% | 1.57 (0–0) | 8.06 (0–0) | 9.17zł (0.0–0.0) | 8.27 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-02_C0_G3` | 5.53 Er (8–1) | 0.0% | 3.8% | 1.44 (0–0) | 6.99 (0–0) | 8.75zł (0.0–0.0) | 8.03 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-02_HERESY_PLUS2` | 5.81 Er (8–1) | 0.0% | 4.8% | 1.55 (0–0) | 8.12 (0–0) | 8.87zł (0.0–0.0) | 8.47 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KT-02_HERESY_SET2` | 5.81 Er (8–1) | 0.0% | 4.8% | 1.55 (0–0) | 8.12 (0–0) | 8.87zł (0.0–0.0) | 8.47 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-12_C0_G1` | 5.52 Er (8–1) | 0.0% | 3.9% | 1.45 (0–0) | 6.94 (0–0) | 8.72zł (0.0–0.0) | 8.02 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-02_C2_G4` | 5.59 Er (8–1) | 0.0% | 4.9% | 1.47 (0–0) | 7.07 (0–0) | 8.86zł (0.0–0.0) | 8.09 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_PLUS2` | 5.83 Er (8–1) | 0.0% | 4.9% | 1.56 (0–0) | 8.15 (0–0) | 9.63zł (0.0–0.0) | 8.43 (0.0–0.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_SET2` | 5.83 Er (8–1) | 0.0% | 4.9% | 1.56 (0–0) | 8.15 (0–0) | 9.63zł (0.0–0.0) | 8.43 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-10_COST_PLUS2` | 5.95 Er (8–1) | 0.0% | 4.8% | 1.60 (0–0) | 8.25 (0–0) | 9.21zł (0.0–0.0) | 8.31 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-09_COST_PLUS2` | 5.93 Er (8–1) | 0.0% | 5.4% | 1.59 (0–0) | 8.22 (0–0) | 9.27zł (0.0–0.0) | 8.30 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-10_C3_H2` | 5.53 Er (8–1) | 0.0% | 4.9% | 1.45 (0–0) | 6.92 (0–0) | 8.72zł (0.0–0.0) | 8.09 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-01_C0_G2` | 5.46 Er (8–1) | 0.0% | 3.6% | 1.44 (0–0) | 6.72 (0–0) | 8.70zł (0.0–0.0) | 8.03 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-03_C0_G2` | 5.47 Er (8–1) | 0.0% | 3.5% | 1.44 (0–0) | 6.84 (0–0) | 8.72zł (0.0–0.0) | 8.06 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-11_C0_G2` | 5.45 Er (8–1) | 0.0% | 3.5% | 1.43 (0–0) | 6.69 (0–0) | 8.68zł (0.0–0.0) | 7.99 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-10_COST_MINUS1` | 5.48 Er (8–1) | 0.0% | 4.9% | 1.43 (0–0) | 6.73 (0–0) | 8.66zł (0.0–0.0) | 8.01 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-06_C1_G2` | 5.49 Er (8–1) | 0.0% | 3.9% | 1.44 (0–0) | 6.74 (0–0) | 8.71zł (0.0–0.0) | 7.99 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-09_C1_G2` | 5.41 Er (8–1) | 0.0% | 3.6% | 1.41 (0–0) | 6.69 (0–0) | 8.68zł (0.0–0.0) | 7.97 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-07_C1_G2` | 5.41 Er (8–1) | 0.0% | 3.7% | 1.42 (0–0) | 6.61 (0–0) | 8.62zł (0.0–0.0) | 7.94 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-04_C1_G2` | 5.40 Er (8–1) | 0.0% | 3.6% | 1.41 (0–0) | 6.59 (0–0) | 8.60zł (0.0–0.0) | 7.95 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-02_C0_G4` | 5.39 Er (8–1) | 0.0% | 3.4% | 1.39 (0–0) | 6.58 (0–0) | 8.65zł (0.0–0.0) | 7.91 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-10_C3_G3` | 5.46 Er (8–1) | 0.0% | 4.9% | 1.43 (0–0) | 6.69 (0–0) | 8.73zł (0.0–0.0) | 8.00 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-10_C3_G4` | 5.46 Er (8–1) | 0.0% | 4.9% | 1.43 (0–0) | 6.67 (0–0) | 8.82zł (0.0–0.0) | 8.00 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-12_C0_G2` | 5.37 Er (8–1) | 0.0% | 3.4% | 1.40 (0–0) | 6.53 (0–0) | 8.59zł (0.0–0.0) | 7.93 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-10_C3_H0` | 5.46 Er (8–1) | 0.0% | 5.0% | 1.42 (0–0) | 6.65 (0–0) | 8.64zł (0.0–0.0) | 7.91 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-05_C1_G2` | 5.40 Er (8–1) | 0.0% | 3.6% | 1.41 (0–0) | 6.58 (0–0) | 8.61zł (0.0–0.0) | 7.95 (0.0–0.0) | 🟢 W NORMIE |
| `L3_SO-10_HERESY_PLUS2` | 5.88 Er (8–1) | 0.0% | 3.9% | 1.09 (0–0) | 7.71 (0–0) | 10.36zł (0.0–0.0) | 8.10 (0.0–0.0) | 🟢 W NORMIE |
| `L3_KB-10_COST_MINUS2` | 5.19 Er (8–1) | 0.0% | 4.4% | 1.33 (0–0) | 5.90 (0–0) | 8.32zł (0.0–0.0) | 7.79 (0.0–0.0) | 🟢 W NORMIE |

</details>