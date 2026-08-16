# Raport Precyzyjnego Audytu Poziomu 3 (Parametry Pojedynczych Kart) — Wersja Balansu: v0.57

**Wersja Balansu:** `v0.57` | **Data:** 2026-08-16 15:58 | **Przeanalizowano Wariantów Kart:** 159 | **Próba:** 3000 gier/setup | **Czas:** 1218.09s
**Filtry:** Parametry: `cost,heresy` | Frakcja: `all` | Karta: `Wszystkie`
**Wynik Bazy Poziomu 3 (Global):** `🔴 51.6 pkt` | 3p: `66.8 pkt` | 4p: `49.4 pkt` | 5p: `38.5 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (87)

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | Baza (Bieżące parametry wszystkich kart) | 🔴 ** 51.6** | 66.8 | 49.4 | 38.5 | ⚪ OPTYMALNY |
| `L3_GC-06_COST_PLUS1` | GC-06 (Szantaż): cost 2 → 3 | 51.6 → 🔴 ** 58.4** (`⬆️ +6.8`) | 66.8 → 75.1 (`⬆️ +8.3`) | 49.4 → 54.9 (`⬆️ +5.5`) | 38.5 → 45.3 (`⬆️ +6.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-03_COST_PLUS1` | KB-03 (Plotka Dworska): cost 1 → 2 | 51.6 → 🔴 ** 56.0** (`⬆️ +4.4`) | 66.8 → 67.6 (`⬆️ +0.8`) | 49.4 → 58.2 (`⬆️ +8.8`) | 38.5 → 42.2 (`⬆️ +3.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-01_COST_MINUS1` | KB-01 (Rozkaz Dworu): cost 1 → 0 | 51.6 → 🔴 ** 54.7** (`⬆️ +3.1`) | 66.8 → 64.6 (`-2.2`) | 49.4 → 54.6 (`⬆️ +5.2`) | 38.5 → 44.8 (`⬆️ +6.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-07_COST_MINUS1` | GC-07 (Skrytobójstwo): cost 2 → 1 | 51.6 → 🔴 ** 54.7** (`⬆️ +3.1`) | 66.8 → 71.2 (`⬆️ +4.4`) | 49.4 → 52.2 (`⬆️ +2.8`) | 38.5 → 40.6 (`⬆️ +2.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-10_HERESY_MINUS1` | CAA-10 (Echo Alhambry): heresy 1 → 0 | 51.6 → 🔴 ** 54.4** (`⬆️ +2.8`) | 66.8 → 69.7 (`⬆️ +2.9`) | 49.4 → 53.6 (`⬆️ +4.2`) | 38.5 → 39.8 (`⬆️ +1.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-06_HERESY_MINUS1` | CAA-06 (Ucieczka z Lochów): heresy 1 → 0 | 51.6 → 🔴 ** 54.3** (`⬆️ +2.7`) | 66.8 → 69.8 (`⬆️ +3.0`) | 49.4 → 52.6 (`⬆️ +3.2`) | 38.5 → 40.4 (`⬆️ +1.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-08_HERESY_MINUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 0 | 51.6 → 🔴 ** 54.2** (`⬆️ +2.6`) | 66.8 → 69.1 (`⬆️ +2.3`) | 49.4 → 52.4 (`⬆️ +3.0`) | 38.5 → 41.2 (`⬆️ +2.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-04_COST_PLUS1` | GC-04 (Informator): cost 0 → 1 | 51.6 → 🔴 ** 53.9** (`⬆️ +2.3`) | 66.8 → 70.4 (`⬆️ +3.6`) | 49.4 → 51.8 (`⬆️ +2.4`) | 38.5 → 39.6 (`⬆️ +1.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-06_HERESY_PLUS1` | GC-06 (Szantaż): heresy 0 → 1 | 51.6 → 🔴 ** 53.9** (`⬆️ +2.3`) | 66.8 → 69.7 (`⬆️ +2.9`) | 49.4 → 51.3 (`⬆️ +1.9`) | 38.5 → 40.8 (`⬆️ +2.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-09_COST_PLUS1` | GC-09 (Lista Dłużników): cost 2 → 3 | 51.6 → 🔴 ** 53.8** (`⬆️ +2.2`) | 66.8 → 71.1 (`⬆️ +4.3`) | 49.4 → 50.8 (`⬆️ +1.4`) | 38.5 → 39.5 (`⬆️ +1.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-09_HERESY_PLUS1` | GC-09 (Lista Dłużników): heresy 0 → 1 | 51.6 → 🔴 ** 53.7** (`⬆️ +2.1`) | 66.8 → 69.9 (`⬆️ +3.1`) | 49.4 → 51.4 (`⬆️ +2.0`) | 38.5 → 39.9 (`⬆️ +1.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-08_COST_MINUS1` | KB-08 (Przekupstwo Sędziego): cost 3 → 2 | 51.6 → 🔴 ** 53.7** (`⬆️ +2.1`) | 66.8 → 68.0 (`⬆️ +1.2`) | 49.4 → 51.9 (`⬆️ +2.5`) | 38.5 → 41.3 (`⬆️ +2.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-02_COST_PLUS1` | GC-02 (Czarny Rynek): cost 2 → 3 | 51.6 → 🔴 ** 53.6** (`⬆️ +2.0`) | 66.8 → 67.5 (`⬆️ +0.7`) | 49.4 → 50.0 (`⬆️ +0.6`) | 38.5 → 43.2 (`⬆️ +4.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 51.6 → 🔴 ** 53.6** (`⬆️ +2.0`) | 66.8 → 70.2 (`⬆️ +3.4`) | 49.4 → 52.0 (`⬆️ +2.6`) | 38.5 → 38.7 (`⬆️ +0.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-07_HERESY_MINUS1` | KT-07 (Archiwum Ukryte): heresy 1 → 0 | 51.6 → 🔴 ** 53.5** (`⬆️ +1.9`) | 66.8 → 63.1 (`-3.7`) | 49.4 → 55.3 (`⬆️ +5.9`) | 38.5 → 42.0 (`⬆️ +3.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-10_HERESY_MINUS1` | KB-10 (Pieczęć Korony): heresy 2 → 1 | 51.6 → 🔴 ** 53.5** (`⬆️ +1.9`) | 66.8 → 66.3 (`-0.5`) | 49.4 → 52.7 (`⬆️ +3.3`) | 38.5 → 41.4 (`⬆️ +2.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-09_HERESY_MINUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 0 | 51.6 → 🔴 ** 53.3** (`⬆️ +1.7`) | 66.8 → 62.2 (`-4.6`) | 49.4 → 56.1 (`⬆️ +6.7`) | 38.5 → 41.5 (`⬆️ +3.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-01_COST_PLUS1` | KB-01 (Rozkaz Dworu): cost 1 → 2 | 51.6 → 🔴 ** 53.1** (`⬆️ +1.5`) | 66.8 → 65.4 (`-1.4`) | 49.4 → 52.7 (`⬆️ +3.3`) | 38.5 → 41.2 (`⬆️ +2.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-08_COST_PLUS1` | KB-08 (Przekupstwo Sędziego): cost 3 → 4 | 51.6 → 🔴 ** 53.1** (`⬆️ +1.5`) | 66.8 → 66.6 (`-0.2`) | 49.4 → 51.2 (`⬆️ +1.8`) | 38.5 → 41.6 (`⬆️ +3.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-10_HERESY_MINUS1` | SO-10 (Oczyść Miasto): heresy 2 → 1 | 51.6 → 🔴 ** 53.0** (`⬆️ +1.4`) | 66.8 → 68.2 (`⬆️ +1.4`) | 49.4 → 50.8 (`⬆️ +1.4`) | 38.5 → 40.0 (`⬆️ +1.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-10_HERESY_MINUS1` | KT-10 (Pieczęć Salomona): heresy 1 → 0 | 51.6 → 🔴 ** 52.9** (`⬆️ +1.3`) | 66.8 → 55.8 (`-11.0`) | 49.4 → 58.2 (`⬆️ +8.8`) | 38.5 → 44.8 (`⬆️ +6.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-04_COST_PLUS1` | KB-04 (Faworyt Dworu): cost 2 → 3 | 51.6 → 🔴 ** 52.9** (`⬆️ +1.3`) | 66.8 → 59.8 (`-7.0`) | 49.4 → 56.6 (`⬆️ +7.2`) | 38.5 → 42.2 (`⬆️ +3.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-06_COST_MINUS1` | KB-06 (Areszt Królewski): cost 1 → 0 | 51.6 → 🔴 ** 52.9** (`⬆️ +1.3`) | 66.8 → 62.3 (`-4.5`) | 49.4 → 55.3 (`⬆️ +5.9`) | 38.5 → 41.2 (`⬆️ +2.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-10_COST_PLUS1` | SO-10 (Oczyść Miasto): cost 5 → 6 | 51.6 → 🔴 ** 52.9** (`⬆️ +1.3`) | 66.8 → 66.7 (`-0.1`) | 49.4 → 50.1 (`⬆️ +0.7`) | 38.5 → 41.8 (`⬆️ +3.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-03_HERESY_MINUS1` | KT-03 (Zakazana Wiedza): heresy 1 → 0 | 51.6 → 🔴 ** 52.8** (`⬆️ +1.2`) | 66.8 → 62.2 (`-4.6`) | 49.4 → 55.9 (`⬆️ +6.5`) | 38.5 → 40.4 (`⬆️ +1.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-06_COST_MINUS1` | SO-06 (Areszt Trybunalski): cost 2 → 1 | 51.6 → 🔴 ** 52.8** (`⬆️ +1.2`) | 66.8 → 66.0 (`-0.8`) | 49.4 → 50.6 (`⬆️ +1.2`) | 38.5 → 41.8 (`⬆️ +3.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-07_HERESY_PLUS1` | GC-07 (Skrytobójstwo): heresy 0 → 1 | 51.6 → 🔴 ** 52.7** (`⬆️ +1.1`) | 66.8 → 67.9 (`⬆️ +1.1`) | 49.4 → 50.7 (`⬆️ +1.3`) | 38.5 → 39.4 (`⬆️ +0.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-02_COST_MINUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 0 | 51.6 → 🔴 ** 52.6** (`⬆️ +1.0`) | 66.8 → 65.7 (`-1.1`) | 49.4 → 50.1 (`⬆️ +0.7`) | 38.5 → 42.1 (`⬆️ +3.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-03_COST_PLUS1` | SO-03 (Podejrzenie): cost 2 → 3 | 51.6 → 🔴 ** 52.6** (`⬆️ +1.0`) | 66.8 → 66.4 (`-0.4`) | 49.4 → 51.7 (`⬆️ +2.3`) | 38.5 → 39.8 (`⬆️ +1.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-08_COST_PLUS1` | SO-08 (Nasłanie Inkwizytora): cost 1 → 2 | 51.6 → 🔴 ** 52.6** (`⬆️ +1.0`) | 66.8 → 66.3 (`-0.5`) | 49.4 → 50.8 (`⬆️ +1.4`) | 38.5 → 40.8 (`⬆️ +2.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 1 → 2 | 51.6 → 🔴 ** 52.6** (`⬆️ +1.0`) | 66.8 → 66.9 (`⬆️ +0.1`) | 49.4 → 51.2 (`⬆️ +1.8`) | 38.5 → 39.8 (`⬆️ +1.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-04_COST_MINUS1` | KB-04 (Faworyt Dworu): cost 2 → 1 | 51.6 → 🔴 ** 52.5** (`⬆️ +0.9`) | 66.8 → 68.4 (`⬆️ +1.6`) | 49.4 → 50.7 (`⬆️ +1.3`) | 38.5 → 38.4 (`-0.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-02_HERESY_PLUS1` | GC-02 (Czarny Rynek): heresy 1 → 2 | 51.6 → 🔴 ** 52.5** (`⬆️ +0.9`) | 66.8 → 67.8 (`⬆️ +1.0`) | 49.4 → 49.7 (`⬆️ +0.3`) | 38.5 → 39.9 (`⬆️ +1.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 0 → 1 | 51.6 → 🔴 ** 52.5** (`⬆️ +0.9`) | 66.8 → 67.7 (`⬆️ +0.9`) | 49.4 → 50.1 (`⬆️ +0.7`) | 38.5 → 39.6 (`⬆️ +1.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-07_COST_MINUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 1 | 51.6 → 🔴 ** 52.4** (`⬆️ +0.8`) | 66.8 → 65.8 (`-1.0`) | 49.4 → 49.6 (`⬆️ +0.2`) | 38.5 → 41.7 (`⬆️ +3.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-04_HERESY_PLUS1` | GC-04 (Informator): heresy 1 → 2 | 51.6 → 🔴 ** 52.4** (`⬆️ +0.8`) | 66.8 → 69.7 (`⬆️ +2.9`) | 49.4 → 49.6 (`⬆️ +0.2`) | 38.5 → 38.0 (`-0.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-10_COST_PLUS1` | KT-10 (Pieczęć Salomona): cost 2 → 3 | 51.6 → 🔴 ** 52.4** (`⬆️ +0.8`) | 66.8 → 67.1 (`⬆️ +0.3`) | 49.4 → 49.8 (`⬆️ +0.4`) | 38.5 → 40.2 (`⬆️ +1.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 2 → 3 | 51.6 → 🔴 ** 52.2** (`⬆️ +0.6`) | 66.8 → 68.7 (`⬆️ +1.9`) | 49.4 → 51.6 (`⬆️ +2.2`) | 38.5 → 36.3 (`-2.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 51.6 → 🔴 ** 52.2** (`⬆️ +0.6`) | 66.8 → 66.9 (`⬆️ +0.1`) | 49.4 → 49.3 (`-0.1`) | 38.5 → 40.5 (`⬆️ +2.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-03_HERESY_PLUS1` | GC-03 (Podrzucenie Księgi): heresy 0 → 1 | 51.6 → 🔴 ** 52.2** (`⬆️ +0.6`) | 66.8 → 68.4 (`⬆️ +1.6`) | 49.4 → 49.2 (`-0.2`) | 38.5 → 39.0 (`⬆️ +0.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-10_COST_PLUS1` | CAA-10 (Echo Alhambry): cost 0 → 1 | 51.6 → 🔴 ** 52.2** (`⬆️ +0.6`) | 66.8 → 67.1 (`⬆️ +0.3`) | 49.4 → 49.8 (`⬆️ +0.4`) | 38.5 → 39.7 (`⬆️ +1.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-03_COST_MINUS1` | KB-03 (Plotka Dworska): cost 1 → 0 | 51.6 → 🔴 ** 52.1** (`⬆️ +0.5`) | 66.8 → 62.6 (`-4.2`) | 49.4 → 52.8 (`⬆️ +3.4`) | 38.5 → 40.8 (`⬆️ +2.3`) | ⚪ OPTYMALNY |
| `L3_KB-09_HERESY_MINUS1` | KB-09 (Dekret Królewski): heresy 1 → 0 | 51.6 → 🔴 ** 52.1** (`⬆️ +0.5`) | 66.8 → 66.3 (`-0.5`) | 49.4 → 51.2 (`⬆️ +1.8`) | 38.5 → 38.9 (`⬆️ +0.4`) | ⚪ OPTYMALNY |
| `L3_KT-06_COST_PLUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 3 | 51.6 → 🔴 ** 52.0** (`⬆️ +0.4`) | 66.8 → 66.7 (`-0.1`) | 49.4 → 48.9 (`-0.5`) | 38.5 → 40.4 (`⬆️ +1.9`) | ⚪ OPTYMALNY |
| `L3_SO-04_COST_PLUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 2 | 51.6 → 🔴 ** 52.0** (`⬆️ +0.4`) | 66.8 → 67.2 (`⬆️ +0.4`) | 49.4 → 48.8 (`-0.6`) | 38.5 → 40.1 (`⬆️ +1.6`) | ⚪ OPTYMALNY |
| `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 0 → 1 | 51.6 → 🔴 ** 52.0** (`⬆️ +0.4`) | 66.8 → 67.0 (`⬆️ +0.2`) | 49.4 → 50.7 (`⬆️ +1.3`) | 38.5 → 38.4 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_SO-09_COST_MINUS1` | SO-09 (Świadek Koronny): cost 2 → 1 | 51.6 → 🔴 ** 51.9** (`⬆️ +0.3`) | 66.8 → 65.0 (`-1.8`) | 49.4 → 48.8 (`-0.6`) | 38.5 → 41.9 (`⬆️ +3.4`) | ⚪ OPTYMALNY |
| `L3_CAA-09_COST_PLUS1` | CAA-09 (Kurier Relikwii): cost 2 → 3 | 51.6 → 🔴 ** 51.9** (`⬆️ +0.3`) | 66.8 → 66.5 (`-0.3`) | 49.4 → 49.5 (`⬆️ +0.1`) | 38.5 → 39.8 (`⬆️ +1.3`) | ⚪ OPTYMALNY |
| `L3_CAA-05_COST_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 2 | 51.6 → 🔴 ** 51.9** (`⬆️ +0.3`) | 66.8 → 66.4 (`-0.4`) | 49.4 → 49.7 (`⬆️ +0.3`) | 38.5 → 39.7 (`⬆️ +1.2`) | ⚪ OPTYMALNY |
| `L3_KB-06_COST_PLUS1` | KB-06 (Areszt Królewski): cost 1 → 2 | 51.6 → 🔴 ** 51.9** (`⬆️ +0.3`) | 66.8 → 67.0 (`⬆️ +0.2`) | 49.4 → 50.3 (`⬆️ +0.9`) | 38.5 | ⚪ OPTYMALNY |
| `L3_SO-01_COST_PLUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 2 | 51.6 → 🔴 ** 51.8** (`⬆️ +0.2`) | 66.8 → 66.0 (`-0.8`) | 49.4 → 48.7 (`-0.7`) | 38.5 → 40.6 (`⬆️ +2.1`) | ⚪ OPTYMALNY |
| `L3_GC-01_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): heresy 1 → 2 | 51.6 → 🔴 ** 51.8** (`⬆️ +0.2`) | 66.8 → 68.6 (`⬆️ +1.8`) | 49.4 → 48.7 (`-0.7`) | 38.5 → 38.0 (`-0.5`) | ⚪ OPTYMALNY |
| `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 1 → 2 | 51.6 → 🔴 ** 51.8** (`⬆️ +0.2`) | 66.8 → 66.5 (`-0.3`) | 49.4 → 50.1 (`⬆️ +0.7`) | 38.5 → 38.8 (`⬆️ +0.3`) | ⚪ OPTYMALNY |
| `L3_KT-05_COST_PLUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 2 | 51.6 → 🔴 ** 51.8** (`⬆️ +0.2`) | 66.8 → 66.7 (`-0.1`) | 49.4 → 49.8 (`⬆️ +0.4`) | 38.5 → 39.0 (`⬆️ +0.5`) | ⚪ OPTYMALNY |
| `L3_GC-03_COST_PLUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 2 | 51.6 → 🔴 ** 51.7** (`⬆️ +0.1`) | 66.8 → 65.7 (`-1.1`) | 49.4 → 49.0 (`-0.4`) | 38.5 → 40.4 (`⬆️ +1.9`) | ⚪ OPTYMALNY |
| `L3_CAA-04_COST_PLUS1` | CAA-04 (Fałszywy Trop): cost 1 → 2 | 51.6 → 🔴 ** 51.7** (`⬆️ +0.1`) | 66.8 → 66.7 (`-0.1`) | 49.4 → 50.3 (`⬆️ +0.9`) | 38.5 → 38.2 (`-0.3`) | ⚪ OPTYMALNY |
| `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 51.6 → 🔴 ** 51.7** (`⬆️ +0.1`) | 66.8 → 66.7 (`-0.1`) | 49.4 → 49.8 (`⬆️ +0.4`) | 38.5 → 38.7 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L3_CAA-07_COST_MINUS1` | CAA-07 (Szantaż Bractwa): cost 1 → 0 | 🔴 ** 51.6** | 66.8 → 66.0 (`-0.8`) | 49.4 → 49.9 (`⬆️ +0.5`) | 38.5 → 38.9 (`⬆️ +0.4`) | ⚪ OPTYMALNY |
| `L3_KT-07_COST_PLUS1` | KT-07 (Archiwum Ukryte): cost 1 → 2 | 🔴 ** 51.6** | 66.8 → 66.4 (`-0.4`) | 49.4 → 49.8 (`⬆️ +0.4`) | 38.5 | ⚪ OPTYMALNY |
| `L3_CAA-08_COST_MINUS1` | CAA-08 (Kaptur Nocy): cost 2 → 1 | 🔴 ** 51.6** | 66.8 → 66.3 (`-0.5`) | 49.4 → 49.7 (`⬆️ +0.3`) | 38.5 → 38.7 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L3_KT-01_COST_MINUS1` | KT-01 (Rytuał Przejścia): cost 1 → 0 | 🔴 ** 51.6** | 66.8 → 66.9 (`⬆️ +0.1`) | 49.4 → 49.5 (`⬆️ +0.1`) | 38.5 → 38.3 (`-0.2`) | ⚪ OPTYMALNY |
| `L3_KT-04_COST_PLUS1` | KT-04 (Zwierciadło Herezji): cost 0 → 1 | 🔴 ** 51.6** | 66.8 → 66.7 (`-0.1`) | 49.4 | 38.5 → 38.6 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_CAA-08_COST_PLUS1` | CAA-08 (Kaptur Nocy): cost 2 → 3 | 51.6 → 🔴 ** 51.5** (`-0.1`) | 66.8 → 66.1 (`-0.7`) | 49.4 → 50.5 (`⬆️ +1.1`) | 38.5 → 37.8 (`-0.7`) | ⚪ OPTYMALNY |
| `L3_CAA-09_COST_MINUS1` | CAA-09 (Kurier Relikwii): cost 2 → 1 | 51.6 → 🔴 ** 51.5** (`-0.1`) | 66.8 → 66.0 (`-0.8`) | 49.4 → 49.6 (`⬆️ +0.2`) | 38.5 → 38.9 (`⬆️ +0.4`) | ⚪ OPTYMALNY |
| `L3_KT-07_COST_MINUS1` | KT-07 (Archiwum Ukryte): cost 1 → 0 | 51.6 → 🔴 ** 51.5** (`-0.1`) | 66.8 → 66.5 (`-0.3`) | 49.4 → 49.2 (`-0.2`) | 38.5 → 38.7 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L3_CAA-02_COST_MINUS1` | CAA-02 (Złoto z Kryjówki): cost 1 → 0 | 51.6 → 🔴 ** 51.5** (`-0.1`) | 66.8 → 66.6 (`-0.2`) | 49.4 → 49.2 (`-0.2`) | 38.5 → 38.6 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_KT-05_COST_MINUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 0 | 51.6 → 🔴 ** 51.5** (`-0.1`) | 66.8 → 66.6 (`-0.2`) | 49.4 → 49.2 (`-0.2`) | 38.5 → 38.6 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_KT-09_COST_MINUS1` | KT-09 (Fragment Kodeksu): cost 1 → 0 | 51.6 → 🔴 ** 51.5** (`-0.1`) | 66.8 | 49.4 → 49.5 (`⬆️ +0.1`) | 38.5 → 38.3 (`-0.2`) | ⚪ OPTYMALNY |
| `L3_KT-10_COST_MINUS1` | KT-10 (Pieczęć Salomona): cost 2 → 1 | 51.6 → 🔴 ** 51.5** (`-0.1`) | 66.8 → 66.7 (`-0.1`) | 49.4 → 49.3 (`-0.1`) | 38.5 → 38.6 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_CAA-05_COST_MINUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 | 51.6 → 🔴 ** 51.4** (`-0.2`) | 66.8 → 66.1 (`-0.7`) | 49.4 → 49.5 (`⬆️ +0.1`) | 38.5 → 38.7 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L3_CAA-06_COST_MINUS1` | CAA-06 (Ucieczka z Lochów): cost 2 → 1 | 51.6 → 🔴 ** 51.4** (`-0.2`) | 66.8 → 66.3 (`-0.5`) | 49.4 → 49.5 (`⬆️ +0.1`) | 38.5 → 38.3 (`-0.2`) | ⚪ OPTYMALNY |
| `L3_KT-06_COST_MINUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 1 | 51.6 → 🔴 ** 51.4** (`-0.2`) | 66.8 → 66.5 (`-0.3`) | 49.4 → 49.2 (`-0.2`) | 38.5 → 38.6 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_KT-08_COST_MINUS1` | KT-08 (Areszt Wiedzy): cost 2 → 1 | 51.6 → 🔴 ** 51.4** (`-0.2`) | 66.8 → 66.5 (`-0.3`) | 49.4 → 49.2 (`-0.2`) | 38.5 → 38.6 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_SO-07_COST_PLUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 3 | 51.6 → 🔴 ** 51.3** (`-0.3`) | 66.8 → 66.5 (`-0.3`) | 49.4 → 47.7 (`-1.7`) | 38.5 → 39.6 (`⬆️ +1.1`) | ⚪ OPTYMALNY |
| `L3_CAA-04_COST_MINUS1` | CAA-04 (Fałszywy Trop): cost 1 → 0 | 51.6 → 🔴 ** 51.3** (`-0.3`) | 66.8 → 66.1 (`-0.7`) | 49.4 → 49.8 (`⬆️ +0.4`) | 38.5 → 38.0 (`-0.5`) | ⚪ OPTYMALNY |
| `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 1 → 2 | 51.6 → 🔴 ** 51.2** (`-0.4`) | 66.8 → 66.3 (`-0.5`) | 49.4 → 50.0 (`⬆️ +0.6`) | 38.5 → 37.2 (`-1.3`) | ⚪ OPTYMALNY |
| `L3_SO-08_COST_MINUS1` | SO-08 (Nasłanie Inkwizytora): cost 1 → 0 | 51.6 → 🔴 ** 51.1** (`-0.5`) | 66.8 → 65.0 (`-1.8`) | 49.4 → 48.3 (`-1.1`) | 38.5 → 40.0 (`⬆️ +1.5`) | ⚪ OPTYMALNY |
| `L3_SO-01_COST_MINUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 0 | 51.6 → 🔴 ** 50.8** (`-0.8`) | 66.8 → 65.8 (`-1.0`) | 49.4 → 47.8 (`-1.6`) | 38.5 → 38.9 (`⬆️ +0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_HERESY_MINUS1` | GC-01 (Przekupiony Strażnik): heresy 1 → 0 | 51.6 → 🔴 ** 50.8** (`-0.8`) | 66.8 → 64.7 (`-2.1`) | 49.4 → 49.1 (`-0.3`) | 38.5 → 38.7 (`⬆️ +0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 51.6 → 🔴 ** 50.8** (`-0.8`) | 66.8 → 66.6 (`-0.2`) | 49.4 → 49.5 (`⬆️ +0.1`) | 38.5 → 36.4 (`-2.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_COST_MINUS1` | KB-02 (Pobór Podatków): cost 1 → 0 | 51.6 → 🔴 ** 50.3** (`-1.3`) | 66.8 → 58.0 (`-8.8`) | 49.4 → 53.3 (`⬆️ +3.9`) | 38.5 → 39.6 (`⬆️ +1.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_HERESY_PLUS1` | GC-10 (Upadek Domu): heresy 2 → 3 | 51.6 → 🔴 ** 50.3** (`-1.3`) | 66.8 → 70.4 (`⬆️ +3.6`) | 49.4 → 45.7 (`-3.7`) | 38.5 → 34.7 (`-3.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_HERESY_MINUS1` | GC-04 (Informator): heresy 1 → 0 | 51.6 → 🔴 ** 50.2** (`-1.4`) | 66.8 → 63.3 (`-3.5`) | 49.4 → 49.7 (`⬆️ +0.3`) | 38.5 → 37.5 (`-1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_COST_MINUS1` | KB-05 (List Żelazny): cost 2 → 1 | 51.6 → 🔴 ** 50.1** (`-1.5`) | 66.8 → 55.1 (`-11.7`) | 49.4 → 53.2 (`⬆️ +3.8`) | 38.5 → 42.0 (`⬆️ +3.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_COST_MINUS1` | SO-10 (Oczyść Miasto): cost 5 → 4 | 51.6 → 🔴 ** 49.2** (`-2.4`) | 66.8 → 63.4 (`-3.4`) | 49.4 → 43.2 (`-6.2`) | 38.5 → 40.9 (`⬆️ +2.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_COST_MINUS1` | KB-10 (Pieczęć Korony): cost 2 → 1 | 51.6 → 🔴 ** 46.4** (`-5.2`) | 66.8 → 51.5 (`-15.3`) | 49.4 → 48.9 (`-0.5`) | 38.5 → 38.9 (`⬆️ +0.4`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 72 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_GC-05_COST_PLUS1` | GC-05 (Fałszywy Świadek): cost 0 → 1 | 🔴 ** 51.6** | 66.8 | 49.4 | 38.5 | ⚪ OPTYMALNY |
| `L3_GC-05_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): heresy 0 → 1 | 🔴 ** 51.6** | 66.8 | 49.4 | 38.5 | ⚪ OPTYMALNY |
| `L3_KT-03_COST_PLUS1` | KT-03 (Zakazana Wiedza): cost 0 → 1 | 🔴 ** 51.6** | 66.8 | 49.4 | 38.5 | ⚪ OPTYMALNY |
| `L3_SO-05_COST_PLUS1` | SO-05 (Wezwanie do Trybunału): cost 0 → 1 | 🔴 ** 51.6** | 66.8 | 49.4 | 38.5 | ⚪ OPTYMALNY |
| `L3_SO-05_HERESY_PLUS1` | SO-05 (Wezwanie do Trybunału): heresy 0 → 1 | 🔴 ** 51.6** | 66.8 | 49.4 | 38.5 | ⚪ OPTYMALNY |
| `L3_KT-02_COST_MINUS1` | KT-02 (Transmutacja Złota): cost 1 → 0 | 51.6 → 🔴 ** 51.5** (`-0.1`) | 66.8 → 66.7 (`-0.1`) | 49.4 | 38.5 → 38.4 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_CAA-03_COST_PLUS1` | CAA-03 (Cień na Rynku): cost 0 → 1 | 51.6 → 🔴 ** 51.4** (`-0.2`) | 66.8 | 49.4 → 49.2 (`-0.2`) | 38.5 → 38.2 (`-0.3`) | ⚪ OPTYMALNY |
| `L3_CAA-06_COST_PLUS1` | CAA-06 (Ucieczka z Lochów): cost 2 → 3 | 51.6 → 🔴 ** 51.4** (`-0.2`) | 66.8 → 66.7 (`-0.1`) | 49.4 → 49.3 (`-0.1`) | 38.5 → 38.1 (`-0.4`) | ⚪ OPTYMALNY |
| `L3_KT-08_COST_PLUS1` | KT-08 (Areszt Wiedzy): cost 2 → 3 | 51.6 → 🔴 ** 51.3** (`-0.3`) | 66.8 | 49.4 → 48.7 (`-0.7`) | 38.5 → 38.4 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_KB-08_HERESY_PLUS1` | KB-08 (Przekupstwo Sędziego): heresy 0 → 1 | 51.6 → 🔴 ** 51.0** (`-0.6`) | 66.8 → 66.1 (`-0.7`) | 49.4 → 49.0 (`-0.4`) | 38.5 → 37.8 (`-0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_HERESY_MINUS1` | GC-02 (Czarny Rynek): heresy 1 → 0 | 51.6 → 🔴 ** 50.9** (`-0.7`) | 66.8 → 65.8 (`-1.0`) | 49.4 → 49.2 (`-0.2`) | 38.5 → 37.6 (`-0.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_COST_MINUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 0 | 51.6 → 🔴 ** 50.8** (`-0.8`) | 66.8 → 66.2 (`-0.6`) | 49.4 → 47.9 (`-1.5`) | 38.5 → 38.4 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_COST_PLUS1` | SO-09 (Świadek Koronny): cost 2 → 3 | 51.6 → 🔴 ** 50.8** (`-0.8`) | 66.8 → 65.5 (`-1.3`) | 49.4 → 48.5 (`-0.9`) | 38.5 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_HERESY_PLUS1` | KB-05 (List Żelazny): heresy 0 → 1 | 51.6 → 🔴 ** 50.6** (`-1.0`) | 66.8 → 66.0 (`-0.8`) | 49.4 → 48.4 (`-1.0`) | 38.5 → 37.3 (`-1.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_HERESY_PLUS1` | KB-06 (Areszt Królewski): heresy 0 → 1 | 51.6 → 🔴 ** 50.5** (`-1.1`) | 66.8 → 66.7 (`-0.1`) | 49.4 → 47.2 (`-2.2`) | 38.5 → 37.7 (`-0.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_COST_MINUS1` | SO-03 (Podejrzenie): cost 2 → 1 | 51.6 → 🔴 ** 50.5** (`-1.1`) | 66.8 → 65.3 (`-1.5`) | 49.4 → 48.2 (`-1.2`) | 38.5 → 38.1 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_HERESY_PLUS1` | KB-03 (Plotka Dworska): heresy 0 → 1 | 51.6 → 🔴 ** 50.4** (`-1.2`) | 66.8 → 65.6 (`-1.2`) | 49.4 → 48.1 (`-1.3`) | 38.5 → 37.5 (`-1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_COST_PLUS1` | SO-06 (Areszt Trybunalski): cost 2 → 3 | 51.6 → 🔴 ** 50.3** (`-1.3`) | 66.8 → 66.0 (`-0.8`) | 49.4 → 48.3 (`-1.1`) | 38.5 → 36.5 (`-2.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): heresy 0 → 1 | 51.6 → 🔴 ** 50.3** (`-1.3`) | 66.8 → 66.0 (`-0.8`) | 49.4 → 48.8 (`-0.6`) | 38.5 → 36.1 (`-2.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_HERESY_PLUS1` | SO-09 (Świadek Koronny): heresy 0 → 1 | 51.6 → 🔴 ** 50.1** (`-1.5`) | 66.8 → 65.8 (`-1.0`) | 49.4 → 47.9 (`-1.5`) | 38.5 → 36.6 (`-1.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_HERESY_PLUS1` | KB-04 (Faworyt Dworu): heresy 1 → 2 | 51.6 → 🔴 ** 50.0** (`-1.6`) | 66.8 → 65.2 (`-1.6`) | 49.4 → 47.3 (`-2.1`) | 38.5 → 37.5 (`-1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_HERESY_PLUS1` | SO-03 (Podejrzenie): heresy 0 → 1 | 51.6 → 🔴 ** 50.0** (`-1.6`) | 66.8 → 65.0 (`-1.8`) | 49.4 → 47.3 (`-2.1`) | 38.5 → 37.6 (`-0.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_HERESY_PLUS1` | KB-01 (Rozkaz Dworu): heresy 0 → 1 | 51.6 → 🔴 ** 49.8** (`-1.8`) | 66.8 → 65.3 (`-1.5`) | 49.4 → 47.6 (`-1.8`) | 38.5 → 36.5 (`-2.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_HERESY_PLUS1` | SO-01 (Patrol Familiariuszy): heresy 0 → 1 | 51.6 → 🔴 ** 49.8** (`-1.8`) | 66.8 → 65.6 (`-1.2`) | 49.4 → 46.9 (`-2.5`) | 38.5 → 36.9 (`-1.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-07_HERESY_PLUS1` | SO-07 (Przesłuchanie Oficjum): heresy 0 → 1 | 51.6 → 🔴 ** 49.6** (`-2.0`) | 66.8 → 65.1 (`-1.7`) | 49.4 → 47.5 (`-1.9`) | 38.5 → 36.2 (`-2.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_HERESY_MINUS1` | GC-10 (Upadek Domu): heresy 2 → 1 | 51.6 → 🔴 ** 49.5** (`-2.1`) | 66.8 → 63.0 (`-3.8`) | 49.4 → 48.7 (`-0.7`) | 38.5 → 36.7 (`-1.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_HERESY_PLUS1` | SO-08 (Nasłanie Inkwizytora): heresy 0 → 1 | 51.6 → 🔴 ** 49.5** (`-2.1`) | 66.8 → 65.2 (`-1.6`) | 49.4 → 47.0 (`-2.4`) | 38.5 → 36.2 (`-2.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_HERESY_PLUS1` | SO-04 (Publiczne Ostrzeżenie): heresy 0 → 1 | 51.6 → 🔴 ** 49.3** (`-2.3`) | 66.8 → 64.7 (`-2.1`) | 49.4 → 46.8 (`-2.6`) | 38.5 → 36.5 (`-2.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_COST_PLUS1` | GC-10 (Upadek Domu): cost 4 → 5 | 51.6 → 🔴 ** 49.2** (`-2.4`) | 66.8 → 63.9 (`-2.9`) | 49.4 → 48.1 (`-1.3`) | 38.5 → 35.6 (`-2.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): heresy 0 → 1 | 51.6 → 🔴 ** 48.5** (`-3.1`) | 66.8 → 65.2 (`-1.6`) | 49.4 → 45.6 (`-3.8`) | 38.5 → 34.7 (`-3.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_HERESY_PLUS1` | SO-10 (Oczyść Miasto): heresy 2 → 3 | 51.6 → 🔴 ** 48.5** (`-3.1`) | 66.8 → 64.2 (`-2.6`) | 49.4 → 45.1 (`-4.3`) | 38.5 → 36.1 (`-2.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_HERESY_PLUS1` | KB-09 (Dekret Królewski): heresy 1 → 2 | 51.6 → 🔴 ** 48.3** (`-3.3`) | 66.8 → 65.0 (`-1.8`) | 49.4 → 44.8 (`-4.6`) | 38.5 → 35.1 (`-3.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_HERESY_PLUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 2 | 51.6 → 🔴 ** 48.2** (`-3.4`) | 66.8 → 62.0 (`-4.8`) | 49.4 → 45.6 (`-3.8`) | 38.5 → 36.9 (`-1.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_COST_MINUS1` | GC-09 (Lista Dłużników): cost 2 → 1 | 51.6 → 🔴 ** 48.2** (`-3.4`) | 66.8 → 62.6 (`-4.2`) | 49.4 → 47.3 (`-2.1`) | 38.5 → 34.8 (`-3.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_HERESY_PLUS1` | CAA-06 (Ucieczka z Lochów): heresy 1 → 2 | 51.6 → 🔴 ** 47.9** (`-3.7`) | 66.8 → 61.0 (`-5.8`) | 49.4 → 44.6 (`-4.8`) | 38.5 → 38.0 (`-0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_COST_PLUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 2 | 51.6 → 🔴 ** 47.3** (`-4.3`) | 66.8 → 60.6 (`-6.2`) | 49.4 → 46.0 (`-3.4`) | 38.5 → 35.4 (`-3.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_COST_PLUS1` | GC-07 (Skrytobójstwo): cost 2 → 3 | 51.6 → 🔴 ** 47.3** (`-4.3`) | 66.8 → 64.3 (`-2.5`) | 49.4 → 45.7 (`-3.7`) | 38.5 → 31.9 (`-6.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-01_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 51.6 → 🔴 ** 47.2** (`-4.4`) | 66.8 → 61.2 (`-5.6`) | 49.4 → 44.3 (`-5.1`) | 38.5 → 36.2 (`-2.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_HERESY_PLUS1` | CAA-07 (Szantaż Bractwa): heresy 0 → 1 | 51.6 → 🔴 ** 47.2** (`-4.4`) | 66.8 → 60.4 (`-6.4`) | 49.4 → 44.6 (`-4.8`) | 38.5 → 36.5 (`-2.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_HERESY_PLUS1` | CAA-02 (Złoto z Kryjówki): heresy 0 → 1 | 51.6 → 🔴 ** 47.1** (`-4.5`) | 66.8 → 60.9 (`-5.9`) | 49.4 → 44.8 (`-4.6`) | 38.5 → 35.7 (`-2.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_HERESY_PLUS1` | CAA-04 (Fałszywy Trop): heresy 0 → 1 | 51.6 → 🔴 ** 47.1** (`-4.5`) | 66.8 → 61.1 (`-5.7`) | 49.4 → 44.4 (`-5.0`) | 38.5 → 35.7 (`-2.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_HERESY_PLUS1` | CAA-05 (Ukryty Kurier): heresy 0 → 1 | 51.6 → 🔴 ** 47.1** (`-4.5`) | 66.8 → 60.9 (`-5.9`) | 49.4 → 43.9 (`-5.5`) | 38.5 → 36.6 (`-1.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_COST_MINUS1` | GC-08 (Zatrute Złoto): cost 2 → 1 | 51.6 → 🔴 ** 47.1** (`-4.5`) | 66.8 → 63.9 (`-2.9`) | 49.4 → 43.6 (`-5.8`) | 38.5 → 33.8 (`-4.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_HERESY_PLUS1` | CAA-03 (Cień na Rynku): heresy 1 → 2 | 51.6 → 🔴 ** 46.5** (`-5.1`) | 66.8 → 60.4 (`-6.4`) | 49.4 → 43.4 (`-6.0`) | 38.5 → 35.8 (`-2.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_COST_MINUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 0 | 51.6 → 🔴 ** 46.1** (`-5.5`) | 66.8 → 61.2 (`-5.6`) | 49.4 → 43.0 (`-6.4`) | 38.5 → 34.1 (`-4.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_COST_MINUS1` | GC-10 (Upadek Domu): cost 4 → 3 | 51.6 → 🔴 ** 46.0** (`-5.6`) | 66.8 → 60.7 (`-6.1`) | 49.4 → 44.2 (`-5.2`) | 38.5 → 33.0 (`-5.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_HERESY_PLUS1` | KT-08 (Areszt Wiedzy): heresy 0 → 1 | 51.6 → 🔴 ** 44.6** (`-7.0`) | 66.8 → 57.6 (`-9.2`) | 49.4 → 40.5 (`-8.9`) | 38.5 → 35.7 (`-2.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-03_COST_MINUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 0 | 51.6 → 🔴 ** 44.5** (`-7.1`) | 66.8 → 61.5 (`-5.3`) | 49.4 → 40.3 (`-9.1`) | 38.5 → 31.7 (`-6.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_COST_MINUS1` | GC-02 (Czarny Rynek): cost 2 → 1 | 51.6 → 🔴 ** 44.0** (`-7.6`) | 66.8 → 60.6 (`-6.2`) | 49.4 → 40.9 (`-8.5`) | 38.5 → 30.5 (`-8.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_HERESY_PLUS1` | KT-01 (Rytuał Przejścia): heresy 0 → 1 | 51.6 → 🔴 ** 43.9** (`-7.7`) | 66.8 → 57.5 (`-9.3`) | 49.4 → 40.1 (`-9.3`) | 38.5 → 34.2 (`-4.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_COST_MINUS1` | KB-09 (Dekret Królewski): cost 3 → 2 | 51.6 → 🔴 ** 43.7** (`-7.9`) | 66.8 → 48.0 (`-18.8`) | 49.4 → 47.4 (`-2.0`) | 38.5 → 35.8 (`-2.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-04_HERESY_PLUS1` | KT-04 (Zwierciadło Herezji): heresy 0 → 1 | 51.6 → 🔴 ** 43.6** (`-8.0`) | 66.8 → 56.2 (`-10.6`) | 49.4 → 39.8 (`-9.6`) | 38.5 → 34.7 (`-3.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_HERESY_PLUS1` | KT-02 (Transmutacja Złota): heresy 0 → 1 | 51.6 → 🔴 ** 43.4** (`-8.2`) | 66.8 → 56.8 (`-10.0`) | 49.4 → 39.6 (`-9.8`) | 38.5 → 33.8 (`-4.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_HERESY_PLUS1` | KB-10 (Pieczęć Korony): heresy 2 → 3 | 51.6 → 🔴 ** 43.2** (`-8.4`) | 66.8 → 58.0 (`-8.8`) | 49.4 → 39.8 (`-9.6`) | 38.5 → 31.8 (`-6.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_HERESY_PLUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 2 | 51.6 → 🔴 ** 43.0** (`-8.6`) | 66.8 → 57.5 (`-9.3`) | 49.4 → 40.5 (`-8.9`) | 38.5 → 30.9 (`-7.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_HERESY_PLUS1` | KT-07 (Archiwum Ukryte): heresy 1 → 2 | 51.6 → 🔴 ** 42.7** (`-8.9`) | 66.8 → 56.3 (`-10.5`) | 49.4 → 39.1 (`-10.3`) | 38.5 → 32.6 (`-5.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_COST_PLUS1` | KB-05 (List Żelazny): cost 2 → 3 | 51.6 → 🔴 ** 42.1** (`-9.5`) | 66.8 → 52.0 (`-14.8`) | 49.4 → 42.2 (`-7.2`) | 38.5 → 32.0 (`-6.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_HERESY_PLUS1` | KT-03 (Zakazana Wiedza): heresy 1 → 2 | 51.6 → 🔴 ** 42.1** (`-9.5`) | 66.8 → 56.3 (`-10.5`) | 49.4 → 38.8 (`-10.6`) | 38.5 → 31.2 (`-7.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_HERESY_PLUS1` | KT-05 (Wskazówka Cyklu): heresy 0 → 1 | 51.6 → 🔴 ** 41.8** (`-9.8`) | 66.8 → 55.6 (`-11.2`) | 49.4 → 38.6 (`-10.8`) | 38.5 → 31.3 (`-7.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_HERESY_PLUS1` | KT-06 (Przesłuchanie Imienia): heresy 0 → 1 | 51.6 → 🔴 ** 41.7** (`-9.9`) | 66.8 → 55.0 (`-11.8`) | 49.4 → 39.1 (`-10.3`) | 38.5 → 30.9 (`-7.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_COST_MINUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 1 | 51.6 → 🔴 ** 41.6** (`-10.0`) | 66.8 → 45.6 (`-21.2`) | 49.4 → 45.1 (`-4.3`) | 38.5 → 34.2 (`-4.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_HERESY_PLUS1` | KB-02 (Pobór Podatków): heresy 0 → 1 | 51.6 → 🔴 ** 41.2** (`-10.4`) | 66.8 → 55.1 (`-11.7`) | 49.4 → 38.3 (`-11.1`) | 38.5 → 30.3 (`-8.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_COST_MINUS1` | GC-06 (Szantaż): cost 2 → 1 | 51.6 → 🔴 ** 41.1** (`-10.5`) | 66.8 → 56.9 (`-9.9`) | 49.4 → 38.3 (`-11.1`) | 38.5 → 28.0 (`-10.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_HERESY_MINUS1` | KB-04 (Faworyt Dworu): heresy 1 → 0 | 51.6 → 🔴 ** 41.0** (`-10.6`) | 66.8 → 51.0 (`-15.8`) | 49.4 → 39.6 (`-9.8`) | 38.5 → 32.5 (`-6.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_HERESY_PLUS1` | CAA-09 (Kurier Relikwii): heresy 0 → 1 | 51.6 → 🔴 ** 40.8** (`-10.8`) | 66.8 → 54.6 (`-12.2`) | 49.4 → 38.2 (`-11.2`) | 38.5 → 29.6 (`-8.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_HERESY_PLUS1` | CAA-10 (Echo Alhambry): heresy 1 → 2 | 51.6 → 🔴 ** 40.7** (`-10.9`) | 66.8 → 54.4 (`-12.4`) | 49.4 → 36.4 (`-13.0`) | 38.5 → 31.4 (`-7.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_HERESY_PLUS1` | KB-07 (Szantaż Pieczęcią): heresy 0 → 1 | 51.6 → 🔴 ** 38.5** (`-13.1`) | 66.8 → 48.6 (`-18.2`) | 49.4 → 36.8 (`-12.6`) | 38.5 → 30.2 (`-8.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_HERESY_PLUS1` | KT-10 (Pieczęć Salomona): heresy 1 → 2 | 51.6 → 🔴 ** 34.9** (`-16.7`) | 66.8 → 47.2 (`-19.6`) | 49.4 → 29.5 (`-19.9`) | 38.5 → 27.9 (`-10.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_COST_PLUS1` | KB-10 (Pieczęć Korony): cost 2 → 3 | 51.6 → 🔴 ** 34.8** (`-16.8`) | 66.8 → 43.6 (`-23.2`) | 49.4 → 31.9 (`-17.5`) | 38.5 → 28.8 (`-9.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_COST_PLUS1` | KB-09 (Dekret Królewski): cost 3 → 4 | 51.6 → 🔴 ** 34.2** (`-17.4`) | 66.8 → 44.9 (`-21.9`) | 49.4 → 32.0 (`-17.4`) | 38.5 → 25.6 (`-12.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_COST_PLUS1` | KB-02 (Pobór Podatków): cost 1 → 2 | 51.6 → 🔴 ** 32.7** (`-18.9`) | 66.8 → 41.2 (`-25.6`) | 49.4 → 31.2 (`-18.2`) | 38.5 → 25.7 (`-12.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_COST_PLUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 3 | 51.6 → 🔴 ** 28.9** (`-22.7`) | 66.8 → 35.5 (`-31.3`) | 49.4 → 27.5 (`-21.9`) | 38.5 → 23.8 (`-14.7`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (87)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 1.91zł (0.0–8.3) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-06_COST_PLUS1` | 5.54 Er (1–11) | 1.0% | 25.9% | 1.39 (0–4) | 3.26 (0–21) | 1.94zł (0.0–8.0) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-03_COST_PLUS1` | 5.43 Er (1–11) | 0.8% | 26.1% | 1.37 (0–4) | 3.06 (0–18) | 1.91zł (0.0–8.3) | 6.16 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-01_COST_MINUS1` | 5.40 Er (1–11) | 0.6% | 24.6% | 1.36 (0–4) | 3.11 (0–18) | 1.90zł (0.0–8.3) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-07_COST_MINUS1` | 5.49 Er (1–11) | 0.8% | 24.9% | 1.36 (0–4) | 3.19 (0–19) | 1.93zł (0.0–8.3) | 6.26 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_MINUS1` | 5.54 Er (1–11) | 1.2% | 25.8% | 1.39 (0–4) | 3.10 (0–20) | 1.96zł (0.0–9.0) | 5.93 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_HERESY_MINUS1` | 5.50 Er (1–11) | 1.0% | 25.6% | 1.38 (0–4) | 3.14 (0–20) | 1.93zł (0.0–8.7) | 6.14 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_HERESY_MINUS1` | 5.50 Er (1–11) | 1.0% | 25.6% | 1.38 (0–4) | 3.16 (0–20) | 1.93zł (0.0–9.7) | 6.15 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-04_COST_PLUS1` | 5.52 Er (1–11) | 1.0% | 26.6% | 1.38 (0–4) | 3.18 (0–21) | 1.89zł (0.0–8.7) | 6.16 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-06_HERESY_PLUS1` | 5.48 Er (1–11) | 0.9% | 25.5% | 1.37 (0–4) | 3.22 (0–19) | 1.92zł (0.0–8.3) | 6.36 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-09_COST_PLUS1` | 5.52 Er (1–11) | 0.9% | 26.2% | 1.39 (0–4) | 3.19 (0–21) | 1.93zł (0.0–8.0) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-09_HERESY_PLUS1` | 5.46 Er (1–11) | 0.8% | 25.5% | 1.37 (0–4) | 3.21 (0–18) | 1.91zł (0.0–8.3) | 6.38 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-08_COST_MINUS1` | 5.44 Er (1–11) | 0.9% | 25.2% | 1.37 (0–4) | 3.15 (0–18) | 1.91zł (0.0–8.3) | 6.23 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-02_COST_PLUS1` | 5.48 Er (1–11) | 0.8% | 26.1% | 1.38 (0–4) | 3.17 (0–22) | 1.91zł (0.0–8.7) | 6.17 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_HERESY_MINUS1` | 5.51 Er (1–11) | 1.0% | 25.6% | 1.39 (0–4) | 3.14 (0–20) | 1.94zł (0.0–8.7) | 6.11 (0.5–10.0) | 🟢 W NORMIE |
| `L3_KT-07_HERESY_MINUS1` | 5.44 Er (1–11) | 0.7% | 25.3% | 1.37 (0–4) | 3.04 (0–20) | 1.90zł (0.0–8.0) | 6.11 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-10_HERESY_MINUS1` | 5.57 Er (1–11) | 1.0% | 25.8% | 1.41 (0–4) | 3.04 (0–19) | 1.93zł (0.0–8.3) | 6.07 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-09_HERESY_MINUS1` | 5.44 Er (1–11) | 0.6% | 25.3% | 1.37 (0–4) | 3.04 (0–18) | 1.91zł (0.0–8.0) | 6.12 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-01_COST_PLUS1` | 5.40 Er (1–11) | 0.7% | 26.0% | 1.35 (0–4) | 3.11 (0–19) | 1.91zł (0.0–8.3) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-08_COST_PLUS1` | 5.46 Er (1–11) | 0.9% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 1.91zł (0.0–8.7) | 6.25 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-10_HERESY_MINUS1` | 5.49 Er (1–11) | 0.9% | 25.5% | 1.38 (0–4) | 3.16 (0–20) | 1.92zł (0.0–8.3) | 6.20 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-10_HERESY_MINUS1` | 5.44 Er (1–11) | 0.6% | 25.3% | 1.38 (0–4) | 2.92 (0–18) | 1.91zł (0.0–7.7) | 5.97 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-04_COST_PLUS1` | 5.37 Er (1–11) | 0.6% | 25.5% | 1.35 (0–4) | 3.03 (0–19) | 1.89zł (0.0–8.3) | 6.21 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-06_COST_MINUS1` | 5.37 Er (1–11) | 0.5% | 24.4% | 1.35 (0–4) | 3.08 (0–18) | 1.90zł (0.0–8.3) | 6.24 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-10_COST_PLUS1` | 5.47 Er (1–11) | 0.9% | 25.9% | 1.31 (0–4) | 3.14 (0–20) | 1.91zł (0.0–8.3) | 6.16 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-03_HERESY_MINUS1` | 5.44 Er (1–11) | 0.6% | 25.3% | 1.37 (0–4) | 3.03 (0–20) | 1.90zł (0.0–8.0) | 6.11 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-06_COST_MINUS1` | 5.47 Er (1–11) | 0.8% | 24.9% | 1.38 (0–4) | 3.18 (0–20) | 1.95zł (0.0–8.7) | 6.25 (0.8–10.0) | 🟢 W NORMIE |
| `L3_GC-07_HERESY_PLUS1` | 5.47 Er (1–11) | 0.8% | 25.5% | 1.38 (0–4) | 3.19 (0–18) | 1.92zł (0.0–8.3) | 6.31 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-02_COST_MINUS1` | 5.46 Er (1–11) | 0.9% | 24.8% | 1.40 (0–4) | 3.18 (0–20) | 1.98zł (0.0–8.3) | 6.28 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-03_COST_PLUS1` | 5.49 Er (1–11) | 0.9% | 25.9% | 1.38 (0–4) | 3.17 (0–20) | 1.94zł (0.0–8.3) | 6.24 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-08_COST_PLUS1` | 5.48 Er (1–11) | 0.8% | 26.2% | 1.36 (0–4) | 3.16 (0–20) | 1.90zł (0.0–8.3) | 6.21 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_COST_PLUS1` | 5.46 Er (1–11) | 0.8% | 25.5% | 1.37 (0–4) | 3.16 (0–21) | 1.75zł (0.0–7.7) | 6.24 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-04_COST_MINUS1` | 5.41 Er (1–11) | 0.8% | 24.8% | 1.36 (0–4) | 3.16 (0–21) | 1.90zł (0.0–8.7) | 6.27 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-02_HERESY_PLUS1` | 5.47 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.20 (0–20) | 1.91zł (0.0–8.3) | 6.32 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-08_HERESY_PLUS1` | 5.47 Er (1–11) | 0.8% | 25.5% | 1.37 (0–4) | 3.20 (0–18) | 1.91zł (0.0–8.3) | 6.32 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-07_COST_MINUS1` | 5.46 Er (1–11) | 0.9% | 24.8% | 1.38 (0–4) | 3.19 (0–20) | 1.95zł (0.0–8.3) | 6.27 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-04_HERESY_PLUS1` | 5.45 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.28 (0–21) | 1.91zł (0.0–8.3) | 6.38 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-10_COST_PLUS1` | 5.46 Er (1–11) | 0.8% | 25.1% | 1.38 (0–4) | 3.16 (0–20) | 1.73zł (0.0–8.0) | 6.24 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_PLUS1` | 5.49 Er (1–11) | 0.9% | 25.8% | 1.38 (0–4) | 3.16 (0–19) | 1.92zł (0.0–8.0) | 6.23 (0.8–10.0) | 🟢 W NORMIE |
| `L3_SO-02_COST_PLUS1` | 5.47 Er (1–11) | 0.9% | 26.9% | 1.36 (0–4) | 3.16 (0–20) | 1.91zł (0.0–8.3) | 6.22 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-03_HERESY_PLUS1` | 5.44 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.22 (0–22) | 1.91zł (0.0–8.3) | 6.36 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_COST_PLUS1` | 5.47 Er (1–11) | 0.9% | 25.5% | 1.37 (0–4) | 3.17 (0–20) | 1.72zł (0.0–7.7) | 6.24 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-03_COST_MINUS1` | 5.36 Er (1–11) | 0.6% | 24.4% | 1.35 (0–4) | 3.10 (0–19) | 1.90zł (0.0–8.7) | 6.26 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-09_HERESY_MINUS1` | 5.55 Er (1–11) | 1.0% | 25.7% | 1.40 (0–4) | 3.17 (0–20) | 1.93zł (0.0–8.3) | 6.13 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-06_COST_PLUS1` | 5.47 Er (1–11) | 0.8% | 25.1% | 1.38 (0–4) | 3.16 (0–20) | 1.71zł (0.0–8.0) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-04_COST_PLUS1` | 5.46 Er (1–11) | 0.9% | 26.2% | 1.36 (0–4) | 3.16 (0–20) | 1.90zł (0.0–8.3) | 6.23 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_COST_PLUS1` | 5.47 Er (1–11) | 0.8% | 25.5% | 1.37 (0–4) | 3.18 (0–20) | 1.75zł (0.0–7.7) | 6.24 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-09_COST_MINUS1` | 5.45 Er (1–11) | 0.9% | 24.8% | 1.38 (0–4) | 3.18 (0–20) | 1.95zł (0.0–8.3) | 6.27 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_COST_PLUS1` | 5.47 Er (1–11) | 0.9% | 25.5% | 1.37 (0–4) | 3.17 (0–18) | 1.75zł (0.0–8.0) | 6.24 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_COST_PLUS1` | 5.46 Er (1–11) | 0.8% | 25.5% | 1.37 (0–4) | 3.16 (0–21) | 1.73zł (0.0–8.0) | 6.24 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-06_COST_PLUS1` | 5.42 Er (1–11) | 0.7% | 26.0% | 1.37 (0–4) | 3.15 (0–21) | 1.92zł (0.0–8.3) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-01_COST_PLUS1` | 5.46 Er (1–11) | 0.9% | 26.2% | 1.36 (0–4) | 3.17 (0–20) | 1.92zł (0.0–8.3) | 6.25 (0.8–10.0) | 🟢 W NORMIE |
| `L3_GC-01_HERESY_PLUS1` | 5.45 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.20 (0–20) | 1.91zł (0.0–8.3) | 6.35 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_COST_PLUS1` | 5.47 Er (1–11) | 0.9% | 25.5% | 1.37 (0–4) | 3.17 (0–20) | 1.74zł (0.0–7.7) | 6.24 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-05_COST_PLUS1` | 5.46 Er (1–11) | 0.8% | 25.3% | 1.38 (0–4) | 3.17 (0–20) | 1.73zł (0.0–8.0) | 6.24 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-03_COST_PLUS1` | 5.46 Er (1–11) | 0.9% | 26.2% | 1.38 (0–4) | 3.12 (0–25) | 1.90zł (0.0–8.0) | 6.19 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_COST_PLUS1` | 5.47 Er (1–11) | 0.9% | 25.5% | 1.37 (0–4) | 3.17 (0–22) | 1.75zł (0.0–8.0) | 6.24 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_PLUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.17 (0–20) | 1.75zł (0.0–8.0) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_COST_MINUS1` | 5.47 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 2.10zł (0.0–9.0) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-07_COST_PLUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 1.73zł (0.0–7.7) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_COST_MINUS1` | 5.47 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 2.07zł (0.0–8.7) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_MINUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 2.08zł (0.0–8.7) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-04_COST_PLUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.17 (0–20) | 1.74zł (0.0–8.0) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_COST_PLUS1` | 5.47 Er (1–11) | 0.9% | 25.5% | 1.38 (0–4) | 3.18 (0–21) | 1.78zł (0.0–8.0) | 6.24 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_COST_MINUS1` | 5.47 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 2.10zł (0.0–8.7) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-07_COST_MINUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 2.10zł (0.0–9.0) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_COST_MINUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 2.09zł (0.0–9.0) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-05_COST_MINUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 2.10zł (0.0–8.7) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-09_COST_MINUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 2.11zł (0.0–9.0) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-10_COST_MINUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 2.11zł (0.0–8.7) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_COST_MINUS1` | 5.47 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 2.11zł (0.0–8.7) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_COST_MINUS1` | 5.47 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 2.08zł (0.0–8.7) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-06_COST_MINUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 2.12zł (0.0–8.7) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-08_COST_MINUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 2.09zł (0.0–9.0) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-07_COST_PLUS1` | 5.46 Er (1–11) | 0.9% | 25.9% | 1.37 (0–4) | 3.18 (0–20) | 1.92zł (0.0–8.3) | 6.24 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_COST_MINUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 2.09zł (0.0–8.7) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-09_COST_PLUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.17 (0–20) | 1.71zł (0.0–7.7) | 6.24 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-08_COST_MINUS1` | 5.43 Er (1–11) | 0.8% | 24.9% | 1.40 (0–4) | 3.20 (0–20) | 1.96zł (0.0–8.3) | 6.30 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-01_COST_MINUS1` | 5.46 Er (1–11) | 0.8% | 24.8% | 1.38 (0–4) | 3.17 (0–20) | 1.98zł (0.0–8.3) | 6.26 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-01_HERESY_MINUS1` | 5.48 Er (1–11) | 0.9% | 25.5% | 1.38 (0–4) | 3.14 (0–20) | 1.92zł (0.0–8.7) | 6.12 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-02_COST_PLUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 1.73zł (0.0–7.7) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-02_COST_MINUS1` | 5.30 Er (1–11) | 0.5% | 24.4% | 1.33 (0–4) | 3.02 (0–18) | 1.89zł (0.0–8.3) | 6.21 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-10_HERESY_PLUS1` | 5.41 Er (1–11) | 0.8% | 25.2% | 1.36 (0–4) | 3.39 (0–23) | 1.91zł (0.0–8.3) | 6.33 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-04_HERESY_MINUS1` | 5.48 Er (1–11) | 0.9% | 25.4% | 1.38 (0–4) | 3.10 (0–20) | 1.91zł (0.0–8.7) | 6.08 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-05_COST_MINUS1` | 5.30 Er (1–11) | 0.5% | 24.9% | 1.33 (0–4) | 3.03 (0–18) | 1.86zł (0.0–8.3) | 6.21 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-10_COST_MINUS1` | 5.32 Er (1–11) | 0.7% | 25.9% | 1.47 (0–4) | 3.31 (0–20) | 1.89zł (0.0–8.3) | 6.38 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-10_COST_MINUS1` | 5.21 Er (1–11) | 0.5% | 24.5% | 1.30 (0–4) | 3.05 (0–19) | 1.84zł (0.0–8.3) | 6.24 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 72 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_GC-05_COST_PLUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 1.91zł (0.0–8.3) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-05_HERESY_PLUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 1.91zł (0.0–8.3) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-03_COST_PLUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 1.71zł (0.0–7.7) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-05_COST_PLUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 1.91zł (0.0–8.3) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-05_HERESY_PLUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 1.91zł (0.0–8.3) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-02_COST_MINUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–20) | 2.09zł (0.0–9.0) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_COST_PLUS1` | 5.46 Er (1–11) | 0.9% | 25.5% | 1.37 (0–4) | 3.17 (0–21) | 1.73zł (0.0–7.7) | 6.24 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_COST_PLUS1` | 5.47 Er (1–11) | 0.9% | 25.5% | 1.37 (0–4) | 3.18 (0–21) | 1.76zł (0.0–8.0) | 6.24 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-08_COST_PLUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.38 (0–4) | 3.18 (0–20) | 1.74zł (0.0–7.7) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-08_HERESY_PLUS1` | 5.46 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.18 (0–18) | 1.92zł (0.0–8.3) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-02_HERESY_MINUS1` | 5.47 Er (1–11) | 0.8% | 25.4% | 1.37 (0–4) | 3.17 (0–20) | 1.91zł (0.0–8.3) | 6.17 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-04_COST_MINUS1` | 5.46 Er (1–11) | 0.9% | 24.8% | 1.39 (0–4) | 3.19 (0–20) | 1.97zł (0.0–8.3) | 6.28 (0.8–10.0) | 🟢 W NORMIE |
| `L3_SO-09_COST_PLUS1` | 5.46 Er (1–11) | 0.8% | 25.9% | 1.37 (0–4) | 3.16 (0–20) | 1.92zł (0.0–8.3) | 6.24 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-05_HERESY_PLUS1` | 5.44 Er (1–11) | 0.8% | 25.3% | 1.37 (0–4) | 3.19 (0–20) | 1.91zł (0.0–8.3) | 6.28 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-06_HERESY_PLUS1` | 5.43 Er (1–11) | 0.9% | 25.3% | 1.36 (0–4) | 3.21 (0–21) | 1.91zł (0.0–8.3) | 6.31 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-03_COST_MINUS1` | 5.45 Er (1–11) | 0.9% | 24.8% | 1.37 (0–4) | 3.19 (0–20) | 1.95zł (0.0–8.3) | 6.27 (0.8–10.0) | 🟢 W NORMIE |
| `L3_KB-03_HERESY_PLUS1` | 5.42 Er (1–11) | 0.8% | 25.2% | 1.36 (0–4) | 3.21 (0–21) | 1.91zł (0.0–8.3) | 6.29 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-06_COST_PLUS1` | 5.46 Er (1–11) | 0.8% | 25.8% | 1.38 (0–4) | 3.18 (0–20) | 1.95zł (0.0–8.3) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-06_HERESY_PLUS1` | 5.45 Er (1–11) | 0.8% | 25.3% | 1.36 (0–4) | 3.18 (0–20) | 1.91zł (0.0–8.3) | 6.35 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-09_HERESY_PLUS1` | 5.43 Er (1–11) | 0.7% | 25.3% | 1.37 (0–4) | 3.20 (0–20) | 1.91zł (0.0–8.3) | 6.39 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-04_HERESY_PLUS1` | 5.43 Er (1–11) | 0.9% | 25.3% | 1.36 (0–4) | 3.24 (0–21) | 1.91zł (0.0–8.3) | 6.29 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-03_HERESY_PLUS1` | 5.43 Er (1–11) | 0.8% | 25.3% | 1.36 (0–4) | 3.20 (0–20) | 1.91zł (0.0–8.3) | 6.37 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-01_HERESY_PLUS1` | 5.44 Er (1–11) | 0.8% | 25.3% | 1.37 (0–4) | 3.18 (0–21) | 1.91zł (0.0–8.3) | 6.29 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-01_HERESY_PLUS1` | 5.43 Er (1–11) | 0.7% | 25.3% | 1.36 (0–4) | 3.20 (0–20) | 1.91zł (0.0–8.3) | 6.38 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-07_HERESY_PLUS1` | 5.43 Er (1–11) | 0.8% | 25.3% | 1.36 (0–4) | 3.19 (0–20) | 1.91zł (0.0–8.3) | 6.38 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-10_HERESY_MINUS1` | 5.49 Er (1–11) | 0.9% | 25.4% | 1.38 (0–4) | 3.02 (0–21) | 1.91zł (0.0–8.3) | 6.09 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-08_HERESY_PLUS1` | 5.42 Er (1–11) | 0.7% | 25.2% | 1.36 (0–4) | 3.20 (0–20) | 1.91zł (0.0–8.3) | 6.42 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-04_HERESY_PLUS1` | 5.42 Er (1–11) | 0.7% | 25.2% | 1.36 (0–4) | 3.21 (0–20) | 1.91zł (0.0–8.3) | 6.41 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-10_COST_PLUS1` | 5.48 Er (1–11) | 0.9% | 24.2% | 1.37 (0–4) | 3.10 (0–20) | 1.94zł (0.0–8.3) | 6.12 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-02_HERESY_PLUS1` | 5.41 Er (1–11) | 0.7% | 25.2% | 1.37 (0–4) | 3.21 (0–20) | 1.91zł (0.0–8.3) | 6.40 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-10_HERESY_PLUS1` | 5.40 Er (1–11) | 0.8% | 25.3% | 1.37 (0–4) | 3.21 (0–20) | 1.90zł (0.0–8.3) | 6.27 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-09_HERESY_PLUS1` | 5.43 Er (1–11) | 0.8% | 25.2% | 1.37 (0–4) | 3.24 (0–21) | 1.92zł (0.0–8.3) | 6.30 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_HERESY_PLUS1` | 5.43 Er (1–11) | 0.7% | 25.3% | 1.36 (0–4) | 3.17 (0–20) | 1.90zł (0.0–8.0) | 6.32 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-09_COST_MINUS1` | 5.41 Er (1–11) | 0.7% | 24.8% | 1.36 (0–4) | 3.18 (0–18) | 1.92zł (0.0–8.3) | 6.34 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_HERESY_PLUS1` | 5.43 Er (1–11) | 0.7% | 25.3% | 1.36 (0–4) | 3.20 (0–24) | 1.90zł (0.0–8.0) | 6.33 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-01_COST_PLUS1` | 5.45 Er (1–11) | 0.9% | 26.0% | 1.35 (0–4) | 3.12 (0–22) | 1.91zł (0.0–8.0) | 6.16 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-07_COST_PLUS1` | 5.43 Er (1–11) | 0.7% | 25.3% | 1.37 (0–4) | 3.14 (0–20) | 1.94zł (0.0–8.3) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_HERESY_PLUS1` | 5.42 Er (1–11) | 0.7% | 25.2% | 1.36 (0–4) | 3.20 (0–20) | 1.90zł (0.0–9.0) | 6.33 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_HERESY_PLUS1` | 5.42 Er (1–11) | 0.7% | 25.2% | 1.36 (0–4) | 3.21 (0–19) | 1.90zł (0.0–8.7) | 6.34 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_HERESY_PLUS1` | 5.42 Er (1–11) | 0.7% | 25.2% | 1.36 (0–4) | 3.20 (0–19) | 1.90zł (0.0–8.7) | 6.33 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_HERESY_PLUS1` | 5.42 Er (1–11) | 0.7% | 25.2% | 1.36 (0–4) | 3.20 (0–18) | 1.89zł (0.0–8.0) | 6.33 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_HERESY_PLUS1` | 5.41 Er (1–11) | 0.7% | 25.2% | 1.36 (0–4) | 3.20 (0–20) | 1.89zł (0.0–8.7) | 6.34 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_MINUS1` | 5.41 Er (1–11) | 0.7% | 24.2% | 1.36 (0–4) | 3.18 (0–20) | 1.93zł (0.0–8.0) | 6.32 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_HERESY_PLUS1` | 5.41 Er (1–11) | 0.7% | 25.2% | 1.36 (0–4) | 3.22 (0–24) | 1.90zł (0.0–8.0) | 6.33 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-01_COST_MINUS1` | 5.41 Er (1–11) | 0.7% | 24.3% | 1.36 (0–4) | 3.16 (0–20) | 1.94zł (0.0–9.0) | 6.29 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-10_COST_MINUS1` | 5.37 Er (1–11) | 0.6% | 24.8% | 1.35 (0–4) | 3.15 (0–20) | 1.88zł (0.0–8.7) | 6.35 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-08_HERESY_PLUS1` | 5.49 Er (1–11) | 1.0% | 25.5% | 1.38 (0–4) | 3.31 (0–20) | 1.93zł (0.0–8.0) | 6.36 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-03_COST_MINUS1` | 5.39 Er (1–11) | 0.7% | 24.3% | 1.36 (0–4) | 3.15 (0–19) | 1.94zł (0.0–9.0) | 6.29 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-02_COST_MINUS1` | 5.37 Er (1–11) | 0.6% | 23.6% | 1.35 (0–4) | 3.14 (0–19) | 1.92zł (0.0–8.7) | 6.33 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-01_HERESY_PLUS1` | 5.50 Er (1–11) | 0.9% | 25.5% | 1.38 (0–4) | 3.27 (0–20) | 1.93zł (0.0–8.0) | 6.35 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-09_COST_MINUS1` | 5.21 Er (1–11) | 0.4% | 24.4% | 1.30 (0–4) | 3.00 (0–18) | 1.82zł (0.0–8.3) | 6.20 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-04_HERESY_PLUS1` | 5.49 Er (1–11) | 0.9% | 25.5% | 1.37 (0–4) | 3.33 (0–20) | 1.93zł (0.0–8.3) | 6.36 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-02_HERESY_PLUS1` | 5.50 Er (1–11) | 1.0% | 25.5% | 1.38 (0–4) | 3.32 (0–20) | 1.93zł (0.0–8.3) | 6.36 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-10_HERESY_PLUS1` | 5.36 Er (1–11) | 0.9% | 25.0% | 1.33 (0–4) | 3.46 (0–20) | 1.90zł (0.0–8.3) | 6.36 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-09_HERESY_PLUS1` | 5.48 Er (1–11) | 1.0% | 25.4% | 1.37 (0–4) | 3.34 (0–21) | 1.92zł (0.0–7.7) | 6.35 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-07_HERESY_PLUS1` | 5.49 Er (1–11) | 1.0% | 25.5% | 1.37 (0–4) | 3.34 (0–20) | 1.93zł (0.0–9.0) | 6.36 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-05_COST_PLUS1` | 5.57 Er (1–11) | 1.4% | 26.2% | 1.40 (0–4) | 3.26 (0–20) | 1.94zł (0.0–8.3) | 6.27 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-03_HERESY_PLUS1` | 5.48 Er (1–11) | 1.0% | 25.5% | 1.37 (0–4) | 3.34 (0–20) | 1.94zł (0.0–9.3) | 6.35 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-05_HERESY_PLUS1` | 5.49 Er (1–11) | 0.9% | 25.5% | 1.37 (0–4) | 3.34 (0–20) | 1.93zł (0.0–8.3) | 6.35 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-06_HERESY_PLUS1` | 5.50 Er (1–11) | 1.0% | 25.5% | 1.37 (0–4) | 3.36 (0–20) | 1.93zł (0.0–8.3) | 6.35 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-07_COST_MINUS1` | 5.21 Er (1–11) | 0.6% | 24.0% | 1.30 (0–4) | 2.90 (0–18) | 1.85zł (0.0–8.3) | 6.17 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-02_HERESY_PLUS1` | 5.50 Er (1–11) | 1.0% | 25.8% | 1.38 (0–4) | 3.32 (0–19) | 1.93zł (0.0–8.7) | 6.34 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-06_COST_MINUS1` | 5.35 Er (1–11) | 0.7% | 24.1% | 1.35 (0–4) | 3.08 (0–19) | 1.92zł (0.0–7.7) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-04_HERESY_MINUS1` | 5.61 Er (1–11) | 1.4% | 25.8% | 1.42 (0–4) | 3.26 (0–22) | 1.95zł (0.0–9.0) | 6.23 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_HERESY_PLUS1` | 5.36 Er (1–11) | 0.6% | 24.9% | 1.34 (0–4) | 3.26 (0–18) | 1.87zł (0.0–8.3) | 6.39 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_PLUS1` | 5.34 Er (1–11) | 0.6% | 24.8% | 1.34 (0–4) | 3.30 (0–20) | 1.87zł (0.0–8.0) | 6.38 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-07_HERESY_PLUS1` | 5.53 Er (1–11) | 1.2% | 25.7% | 1.39 (0–4) | 3.31 (0–20) | 1.94zł (0.0–9.7) | 6.34 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-10_HERESY_PLUS1` | 5.49 Er (1–11) | 1.1% | 25.5% | 1.36 (0–4) | 3.51 (0–20) | 1.96zł (0.0–9.3) | 6.42 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-10_COST_PLUS1` | 5.69 Er (1–11) | 1.5% | 26.6% | 1.44 (0–4) | 3.34 (0–24) | 1.98zł (0.0–8.7) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-09_COST_PLUS1` | 5.66 Er (1–11) | 1.3% | 27.2% | 1.43 (0–4) | 3.38 (0–20) | 1.95zł (0.0–8.3) | 6.31 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-02_COST_PLUS1` | 5.65 Er (1–11) | 1.6% | 27.9% | 1.43 (0–4) | 3.37 (0–21) | 1.96zł (0.0–8.3) | 6.28 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-07_COST_PLUS1` | 5.66 Er (1–11) | 1.7% | 26.6% | 1.43 (0–4) | 3.41 (0–20) | 1.98zł (0.0–9.0) | 6.35 (1.0–10.0) | 🟢 W NORMIE |

</details>