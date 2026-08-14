# Raport Precyzyjnego Audytu Poziomu 3 (Parametry Pojedynczych Kart) — Wersja Balansu: v0.17

**Wersja Balansu:** `v0.17` | **Data:** 2026-08-14 13:11 | **Przeanalizowano Wariantów Kart:** 161 | **Próba:** 300 gier/setup | **Czas:** 151.61s
**Filtry:** Parametry: `cost,heresy` | Frakcja: `all` | Karta: `Wszystkie`
**Wynik Bazy Poziomu 3 (Global):** `🟢 86.0 pkt` | 3p: `87.9 pkt` | 4p: `70.9 pkt` | 5p: `99.2 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (71)

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | Baza (Bieżące parametry wszystkich kart) | 🟢 ** 86.0** | 87.9 | 70.9 | 99.2 | ⚪ OPTYMALNY |
| `L3_KB-04_HERESY_MINUS1` | KB-04 (Faworyt Dworu): heresy 1 → 0 | 86.0 → 🟢 ** 90.0** (`⬆️ +4.0`) | 87.9 → 90.8 (`⬆️ +2.9`) | 70.9 → 80.6 (`⬆️ +9.7`) | 99.2 → 98.6 (`-0.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-09_HERESY_MINUS1` | KB-09 (Dekret Królewski): heresy 1 → 0 | 86.0 → 🟢 ** 89.9** (`⬆️ +3.9`) | 87.9 → 88.9 (`⬆️ +1.0`) | 70.9 → 82.2 (`⬆️ +11.3`) | 99.2 → 98.7 (`-0.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-08_COST_PLUS1` | KB-08 (Przekupstwo Sędziego): cost 3 → 4 | 86.0 → 🟢 ** 87.8** (`⬆️ +1.8`) | 87.9 → 90.9 (`⬆️ +3.0`) | 70.9 → 74.9 (`⬆️ +4.0`) | 99.2 → 97.7 (`-1.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-07_COST_PLUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 3 | 86.0 → 🟢 ** 87.6** (`⬆️ +1.6`) | 87.9 → 91.4 (`⬆️ +3.5`) | 70.9 → 72.6 (`⬆️ +1.7`) | 99.2 → 98.7 (`-0.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-03_HERESY_PLUS1` | CAA-03 (Cień na Rynku): heresy 1 → 2 | 86.0 → 🟢 ** 87.6** (`⬆️ +1.6`) | 87.9 → 90.4 (`⬆️ +2.5`) | 70.9 → 73.8 (`⬆️ +2.9`) | 99.2 → 98.6 (`-0.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-07_HERESY_PLUS1` | CAA-07 (Szantaż Bractwa): heresy 0 → 1 | 86.0 → 🟢 ** 86.6** (`⬆️ +0.6`) | 87.9 → 86.2 (`-1.7`) | 70.9 → 74.3 (`⬆️ +3.4`) | 99.2 → 99.4 (`⬆️ +0.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-05_HERESY_PLUS1` | KT-05 (Wskazówka Cyklu): heresy 0 → 1 | 86.0 → 🟢 ** 86.6** (`⬆️ +0.6`) | 87.9 → 88.4 (`⬆️ +0.5`) | 70.9 → 73.5 (`⬆️ +2.6`) | 99.2 → 97.8 (`-1.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-10_COST_PLUS1` | KT-10 (Pieczęć Salomona): cost 1 → 2 | 86.0 → 🟢 ** 86.5** (`⬆️ +0.5`) | 87.9 → 91.4 (`⬆️ +3.5`) | 70.9 → 69.2 (`-1.7`) | 99.2 → 99.0 (`-0.2`) | ⚪ OPTYMALNY |
| `L3_KB-01_COST_MINUS1` | KB-01 (Rozkaz Dworu): cost 1 → 0 | 86.0 → 🟢 ** 86.4** (`⬆️ +0.4`) | 87.9 → 85.4 (`-2.5`) | 70.9 → 75.8 (`⬆️ +4.9`) | 99.2 → 98.0 (`-1.2`) | ⚪ OPTYMALNY |
| `L3_KT-07_HERESY_PLUS1` | KT-07 (Archiwum Ukryte): heresy 0 → 1 | 86.0 → 🟢 ** 86.4** (`⬆️ +0.4`) | 87.9 → 91.1 (`⬆️ +3.2`) | 70.9 → 69.4 (`-1.5`) | 99.2 → 98.6 (`-0.6`) | ⚪ OPTYMALNY |
| `L3_CAA-02_HERESY_PLUS1` | CAA-02 (Złoto z Kryjówki): heresy 0 → 1 | 86.0 → 🟢 ** 86.1** (`⬆️ +0.1`) | 87.9 | 70.9 → 72.6 (`⬆️ +1.7`) | 99.2 → 97.9 (`-1.3`) | ⚪ OPTYMALNY |
| `L3_KT-01_HERESY_PLUS1` | KT-01 (Rytuał Przejścia): heresy 0 → 1 | 86.0 → 🟢 ** 85.9** (`-0.1`) | 87.9 → 89.2 (`⬆️ +1.3`) | 70.9 → 69.5 (`-1.4`) | 99.2 → 99.0 (`-0.2`) | ⚪ OPTYMALNY |
| `L3_KB-01_COST_PLUS1` | KB-01 (Rozkaz Dworu): cost 1 → 2 | 86.0 → 🟢 ** 85.8** (`-0.2`) | 87.9 → 83.3 (`-4.6`) | 70.9 → 80.0 (`⬆️ +9.1`) | 99.2 → 94.2 (`-5.0`) | ⚪ OPTYMALNY |
| `L3_GC-03_COST_PLUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 2 | 86.0 → 🟢 ** 85.8** (`-0.2`) | 87.9 → 87.4 (`-0.5`) | 70.9 → 70.2 (`-0.7`) | 99.2 → 99.8 (`⬆️ +0.6`) | ⚪ OPTYMALNY |
| `L3_KT-03_HERESY_MINUS1` | KT-03 (Zakazana Wiedza): heresy 1 → 0 | 86.0 → 🟢 ** 85.7** (`-0.3`) | 87.9 → 87.2 (`-0.7`) | 70.9 → 72.9 (`⬆️ +2.0`) | 99.2 → 96.9 (`-2.3`) | ⚪ OPTYMALNY |
| `L3_SO-06_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): heresy 0 → 1 | 86.0 → 🟢 ** 85.7** (`-0.3`) | 87.9 → 88.4 (`⬆️ +0.5`) | 70.9 → 69.9 (`-1.0`) | 99.2 → 98.8 (`-0.4`) | ⚪ OPTYMALNY |
| `L3_GC-02_COST_PLUS1` | GC-02 (Czarny Rynek): cost 1 → 2 | 86.0 → 🟢 ** 85.5** (`-0.5`) | 87.9 → 83.9 (`-4.0`) | 70.9 → 74.4 (`⬆️ +3.5`) | 99.2 → 98.3 (`-0.9`) | ⚪ OPTYMALNY |
| `L3_KB-06_HERESY_PLUS1` | KB-06 (Areszt Królewski): heresy 0 → 1 | 86.0 → 🟢 ** 85.5** (`-0.5`) | 87.9 → 88.0 (`⬆️ +0.1`) | 70.9 → 69.8 (`-1.1`) | 99.2 → 98.8 (`-0.4`) | ⚪ OPTYMALNY |
| `L3_SO-09_HERESY_PLUS1` | SO-09 (Świadek Koronny): heresy 0 → 1 | 86.0 → 🟢 ** 85.4** (`-0.6`) | 87.9 → 88.4 (`⬆️ +0.5`) | 70.9 → 70.2 (`-0.7`) | 99.2 → 97.5 (`-1.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_COST_PLUS1` | KT-03 (Zakazana Wiedza): cost 0 → 1 | 86.0 → 🟢 ** 85.3** (`-0.7`) | 87.9 → 90.7 (`⬆️ +2.8`) | 70.9 → 68.8 (`-2.1`) | 99.2 → 96.3 (`-2.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_COST_PLUS1` | GC-04 (Informator): cost 1 → 2 | 86.0 → 🟢 ** 85.3** (`-0.7`) | 87.9 → 86.7 (`-1.2`) | 70.9 → 72.0 (`⬆️ +1.1`) | 99.2 → 97.3 (`-1.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_HERESY_PLUS1` | KT-06 (Przesłuchanie Imienia): heresy 0 → 1 | 86.0 → 🟢 ** 85.2** (`-0.8`) | 87.9 → 86.7 (`-1.2`) | 70.9 → 71.9 (`⬆️ +1.0`) | 99.2 → 97.0 (`-2.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_HERESY_PLUS1` | GC-07 (Skrytobójstwo): heresy 1 → 2 | 86.0 → 🟢 ** 85.2** (`-0.8`) | 87.9 → 88.1 (`⬆️ +0.2`) | 70.9 → 68.7 (`-2.2`) | 99.2 → 98.8 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_COST_MINUS1` | KB-02 (Pobór Podatków): cost 1 → 0 | 86.0 → 🟢 ** 84.9** (`-1.1`) | 87.9 → 81.2 (`-6.7`) | 70.9 → 76.0 (`⬆️ +5.1`) | 99.2 → 97.6 (`-1.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_COST_PLUS1` | SO-09 (Świadek Koronny): cost 2 → 3 | 86.0 → 🟢 ** 84.8** (`-1.2`) | 87.9 → 89.2 (`⬆️ +1.3`) | 70.9 → 68.2 (`-2.7`) | 99.2 → 97.0 (`-2.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_HERESY_PLUS1` | CAA-06 (Ucieczka z Lochów): heresy 0 → 1 | 86.0 → 🟢 ** 84.3** (`-1.7`) | 87.9 → 86.8 (`-1.1`) | 70.9 → 66.3 (`-4.6`) | 99.2 → 99.8 (`⬆️ +0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_COST_PLUS1` | KB-04 (Faworyt Dworu): cost 1 → 2 | 86.0 → 🟢 ** 84.1** (`-1.9`) | 87.9 → 90.9 (`⬆️ +3.0`) | 70.9 → 78.2 (`⬆️ +7.3`) | 99.2 → 83.2 (`-16.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_COST_PLUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 2 | 86.0 → 🟢 ** 83.9** (`-2.1`) | 87.9 → 92.0 (`⬆️ +4.1`) | 70.9 → 62.5 (`-8.4`) | 99.2 → 97.2 (`-2.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_HERESY_MINUS1` | SO-08 (Nasłanie Inkwizytora): heresy 1 → 0 | 86.0 → 🟢 ** 83.9** (`-2.1`) | 87.9 → 79.5 (`-8.4`) | 70.9 → 72.9 (`⬆️ +2.0`) | 99.2 → 99.4 (`⬆️ +0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_HERESY_MINUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 0 | 86.0 → 🟢 ** 83.5** (`-2.5`) | 87.9 → 85.8 (`-2.1`) | 70.9 → 65.2 (`-5.7`) | 99.2 → 99.5 (`⬆️ +0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_HERESY_MINUS1` | KB-10 (Pieczęć Korony): heresy 2 → 1 | 86.0 → 🟢 ** 83.4** (`-2.6`) | 87.9 → 85.3 (`-2.6`) | 70.9 → 79.7 (`⬆️ +8.8`) | 99.2 → 85.1 (`-14.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 86.0 → 🟢 ** 82.6** (`-3.4`) | 87.9 → 89.2 (`⬆️ +1.3`) | 70.9 → 60.7 (`-10.2`) | 99.2 → 97.9 (`-1.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_HERESY_PLUS1` | KT-02 (Transmutacja Złota): heresy 0 → 1 | 86.0 → 🟢 ** 82.5** (`-3.5`) | 87.9 → 93.1 (`⬆️ +5.2`) | 70.9 → 75.6 (`⬆️ +4.7`) | 99.2 → 78.7 (`-20.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_COST_MINUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 0 | 86.0 → 🟢 ** 82.5** (`-3.5`) | 87.9 → 92.9 (`⬆️ +5.0`) | 70.9 → 69.9 (`-1.0`) | 99.2 → 84.7 (`-14.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_HERESY_PLUS1` | CAA-05 (Ukryty Kurier): heresy 0 → 1 | 86.0 → 🟢 ** 82.4** (`-3.6`) | 87.9 → 88.1 (`⬆️ +0.2`) | 70.9 → 59.9 (`-11.0`) | 99.2 → 99.3 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_COST_MINUS1` | SO-06 (Areszt Trybunalski): cost 2 → 1 | 86.0 → 🟢 ** 82.3** (`-3.7`) | 87.9 → 87.3 (`-0.6`) | 70.9 → 74.5 (`⬆️ +3.6`) | 99.2 → 85.0 (`-14.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_COST_MINUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 1 | 86.0 → 🟢 ** 82.2** (`-3.8`) | 87.9 → 85.5 (`-2.4`) | 70.9 → 86.8 (`⬆️ +15.9`) | 99.2 → 74.3 (`-24.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_COST_MINUS1` | KT-02 (Transmutacja Złota): cost 1 → 0 | 86.0 → 🟢 ** 81.9** (`-4.1`) | 87.9 → 87.8 (`-0.1`) | 70.9 → 72.4 (`⬆️ +1.5`) | 99.2 → 85.4 (`-13.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_COST_MINUS1` | KB-08 (Przekupstwo Sędziego): cost 3 → 2 | 86.0 → 🟢 ** 81.8** (`-4.2`) | 87.9 → 88.5 (`⬆️ +0.6`) | 70.9 → 58.6 (`-12.3`) | 99.2 → 98.4 (`-0.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 86.0 → 🟢 ** 81.5** (`-4.5`) | 87.9 → 88.0 (`⬆️ +0.1`) | 70.9 → 59.7 (`-11.2`) | 99.2 → 96.9 (`-2.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 86.0 → 🟢 ** 81.4** (`-4.6`) | 87.9 → 90.1 (`⬆️ +2.2`) | 70.9 → 74.3 (`⬆️ +3.4`) | 99.2 → 79.7 (`-19.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_COST_PLUS1` | KB-06 (Areszt Królewski): cost 2 → 3 | 86.0 → 🟢 ** 81.3** (`-4.7`) | 87.9 → 88.9 (`⬆️ +1.0`) | 70.9 → 71.1 (`⬆️ +0.2`) | 99.2 → 83.9 (`-15.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_COST_PLUS1` | SO-03 (Podejrzenie): cost 1 → 2 | 86.0 → 🟢 ** 81.2** (`-4.8`) | 87.9 → 89.7 (`⬆️ +1.8`) | 70.9 → 56.2 (`-14.7`) | 99.2 → 97.6 (`-1.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-04_COST_PLUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 2 | 86.0 → 🟢 ** 80.5** (`-5.5`) | 87.9 → 89.3 (`⬆️ +1.4`) | 70.9 → 53.9 (`-17.0`) | 99.2 → 98.2 (`-1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-07_COST_PLUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 3 | 86.0 → 🟢 ** 80.4** (`-5.6`) | 87.9 → 90.2 (`⬆️ +2.3`) | 70.9 → 55.9 (`-15.0`) | 99.2 → 95.1 (`-4.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_COST_PLUS1` | GC-06 (Szantaż): cost 2 → 3 | 86.0 → 🟢 ** 80.0** (`-6.0`) | 87.9 → 82.4 (`-5.5`) | 70.9 → 75.4 (`⬆️ +4.5`) | 99.2 → 82.1 (`-17.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_COST_PLUS1` | GC-07 (Skrytobójstwo): cost 2 → 3 | 86.0 → 🟢 ** 79.9** (`-6.1`) | 87.9 → 89.5 (`⬆️ +1.6`) | 70.9 → 64.9 (`-6.0`) | 99.2 → 85.3 (`-13.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_COST_MINUS1` | CAA-02 (Złoto z Kryjówki): cost 1 → 0 | 86.0 → 🟢 ** 79.7** (`-6.3`) | 87.9 → 86.8 (`-1.1`) | 70.9 → 75.4 (`⬆️ +4.5`) | 99.2 → 77.0 (`-22.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_HERESY_PLUS1` | KT-08 (Areszt Wiedzy): heresy 0 → 1 | 86.0 → 🟢 ** 79.6** (`-6.4`) | 87.9 → 88.7 (`⬆️ +0.8`) | 70.9 → 69.2 (`-1.7`) | 99.2 → 80.8 (`-18.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_COST_MINUS1` | CAA-04 (Fałszywy Trop): cost 1 → 0 | 86.0 → 🟢 ** 79.1** (`-6.9`) | 87.9 → 79.6 (`-8.3`) | 70.9 → 71.5 (`⬆️ +0.6`) | 99.2 → 86.1 (`-13.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_COST_MINUS1` | SO-03 (Podejrzenie): cost 1 → 0 | 86.0 → 🟢 ** 79.0** (`-7.0`) | 87.9 → 92.3 (`⬆️ +4.4`) | 70.9 → 62.4 (`-8.5`) | 99.2 → 82.4 (`-16.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_COST_MINUS1` | KB-05 (List Żelazny): cost 2 → 1 | 86.0 → 🟢 ** 77.7** (`-8.3`) | 87.9 → 73.6 (`-14.3`) | 70.9 → 73.0 (`⬆️ +2.1`) | 99.2 → 86.4 (`-12.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_COST_MINUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 0 | 86.0 → 🟢 ** 77.5** (`-8.5`) | 87.9 → 86.9 (`-1.0`) | 70.9 → 73.4 (`⬆️ +2.5`) | 99.2 → 72.1 (`-27.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_COST_MINUS1` | KT-08 (Areszt Wiedzy): cost 2 → 1 | 86.0 → 🟢 ** 77.3** (`-8.7`) | 87.9 → 86.6 (`-1.3`) | 70.9 → 72.1 (`⬆️ +1.2`) | 99.2 → 73.2 (`-26.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_HERESY_MINUS1` | GC-04 (Informator): heresy 1 → 0 | 86.0 → 🟢 ** 76.7** (`-9.3`) | 87.9 → 76.2 (`-11.7`) | 70.9 → 54.3 (`-16.6`) | 99.2 → 99.6 (`⬆️ +0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_COST_PLUS1` | CAA-08 (Kaptur Nocy): cost 1 → 2 | 86.0 → 🟢 ** 75.2** (`-10.8`) | 87.9 → 85.2 (`-2.7`) | 70.9 → 71.1 (`⬆️ +0.2`) | 99.2 → 69.4 (`-29.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-04_COST_MINUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 0 | 86.0 → 🟢 ** 74.7** (`-11.3`) | 87.9 → 89.5 (`⬆️ +1.6`) | 70.9 → 72.1 (`⬆️ +1.2`) | 99.2 → 62.4 (`-36.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_HERESY_PLUS1` | SO-03 (Podejrzenie): heresy 0 → 1 | 86.0 → 🟢 ** 73.8** (`-12.2`) | 87.9 → 79.0 (`-8.9`) | 70.9 → 43.1 (`-27.8`) | 99.2 → 99.3 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_COST_MINUS1` | CAA-09 (Kurier Relikwii): cost 2 → 1 | 86.0 → 🟢 ** 73.3** (`-12.7`) | 87.9 → 76.9 (`-11.0`) | 70.9 → 82.7 (`⬆️ +11.8`) | 99.2 → 60.2 (`-39.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_COST_MINUS1` | CAA-10 (Echo Alhambry): cost 1 → 0 | 86.0 → 🟢 ** 73.3** (`-12.7`) | 87.9 → 80.0 (`-7.9`) | 70.9 → 77.7 (`⬆️ +6.8`) | 99.2 → 62.2 (`-37.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-04_HERESY_PLUS1` | KT-04 (Zwierciadło Herezji): heresy 0 → 1 | 86.0 → 🟢 ** 72.7** (`-13.3`) | 87.9 → 88.7 (`⬆️ +0.8`) | 70.9 → 42.7 (`-28.2`) | 99.2 → 86.8 (`-12.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-01_COST_MINUS1` | CAA-01 (Przejście Podziemiami): cost 1 → 0 | 86.0 → 🟢 ** 72.1** (`-13.9`) | 87.9 → 79.8 (`-8.1`) | 70.9 → 75.7 (`⬆️ +4.8`) | 99.2 → 60.9 (`-38.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_COST_PLUS1` | KT-07 (Archiwum Ukryte): cost 1 → 2 | 86.0 → 🟢 ** 70.7** (`-15.3`) | 87.9 → 90.5 (`⬆️ +2.6`) | 70.9 → 47.9 (`-23.0`) | 99.2 → 73.6 (`-25.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_COST_MINUS1` | CAA-06 (Ucieczka z Lochów): cost 2 → 1 | 86.0 → 🟢 ** 70.4** (`-15.6`) | 87.9 → 81.9 (`-6.0`) | 70.9 → 74.3 (`⬆️ +3.4`) | 99.2 → 55.0 (`-44.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_COST_MINUS1` | KB-06 (Areszt Królewski): cost 2 → 1 | 86.0 → 🟢 ** 69.8** (`-16.2`) | 87.9 → 89.4 (`⬆️ +1.5`) | 70.9 → 60.2 (`-10.7`) | 99.2 → 59.7 (`-39.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_COST_PLUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 3 | 86.0 → 🟢 ** 69.0** (`-17.0`) | 87.9 → 89.4 (`⬆️ +1.5`) | 70.9 → 51.7 (`-19.2`) | 99.2 → 66.0 (`-33.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_COST_PLUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 2 | 86.0 → 🟢 ** 68.1** (`-17.9`) | 87.9 → 94.1 (`⬆️ +6.2`) | 70.9 → 62.3 (`-8.6`) | 99.2 → 47.9 (`-51.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-07_COST_MINUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 1 | 86.0 → 🟢 ** 67.9** (`-18.1`) | 87.9 → 89.7 (`⬆️ +1.8`) | 70.9 → 54.4 (`-16.5`) | 99.2 → 59.6 (`-39.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_COST_MINUS1` | GC-09 (Lista Dłużników): cost 2 → 1 | 86.0 → 🟢 ** 63.7** (`-22.3`) | 87.9 → 88.5 (`⬆️ +0.6`) | 70.9 → 40.3 (`-30.6`) | 99.2 → 62.4 (`-36.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_COST_MINUS1` | SO-09 (Świadek Koronny): cost 2 → 1 | 86.0 → 🟢 ** 63.1** (`-22.9`) | 87.9 → 89.2 (`⬆️ +1.3`) | 70.9 → 48.9 (`-22.0`) | 99.2 → 51.1 (`-48.1`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 90 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_GC-05_COST_PLUS1` | GC-05 (Fałszywy Świadek): cost 0 → 1 | 🟢 ** 86.0** | 87.9 | 70.9 | 99.2 | ⚪ OPTYMALNY |
| `L3_GC-05_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): heresy 0 → 1 | 🟢 ** 86.0** | 87.9 | 70.9 | 99.2 | ⚪ OPTYMALNY |
| `L3_SO-05_COST_PLUS1` | SO-05 (Wezwanie do Trybunału): cost 0 → 1 | 🟢 ** 86.0** | 87.9 | 70.9 | 99.2 | ⚪ OPTYMALNY |
| `L3_SO-05_HERESY_PLUS1` | SO-05 (Wezwanie do Trybunału): heresy 0 → 1 | 🟢 ** 86.0** | 87.9 | 70.9 | 99.2 | ⚪ OPTYMALNY |
| `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 1 → 2 | 86.0 → 🟢 ** 85.3** (`-0.7`) | 87.9 → 87.3 (`-0.6`) | 70.9 → 69.9 (`-1.0`) | 99.2 → 98.6 (`-0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-01_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 86.0 → 🟢 ** 85.2** (`-0.8`) | 87.9 → 87.4 (`-0.5`) | 70.9 → 70.0 (`-0.9`) | 99.2 → 98.2 (`-1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_HERESY_MINUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 0 | 86.0 → 🟢 ** 85.2** (`-0.8`) | 87.9 → 86.0 (`-1.9`) | 70.9 → 70.4 (`-0.5`) | 99.2 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_HERESY_PLUS1` | KB-08 (Przekupstwo Sędziego): heresy 0 → 1 | 86.0 → 🟢 ** 84.9** (`-1.1`) | 87.9 → 87.0 (`-0.9`) | 70.9 → 68.9 (`-2.0`) | 99.2 → 98.7 (`-0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_HERESY_PLUS1` | KT-03 (Zakazana Wiedza): heresy 1 → 2 | 86.0 → 🟢 ** 84.6** (`-1.4`) | 87.9 → 87.7 (`-0.2`) | 70.9 → 68.4 (`-2.5`) | 99.2 → 97.8 (`-1.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_HERESY_MINUS1` | GC-07 (Skrytobójstwo): heresy 1 → 0 | 86.0 → 🟢 ** 84.1** (`-1.9`) | 87.9 → 84.7 (`-3.2`) | 70.9 → 68.7 (`-2.2`) | 99.2 → 99.0 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 86.0 → 🟢 ** 83.6** (`-2.4`) | 87.9 → 83.7 (`-4.2`) | 70.9 → 68.0 (`-2.9`) | 99.2 → 99.1 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_HERESY_MINUS1` | SO-10 (Oczyść Miasto): heresy 2 → 1 | 86.0 → 🟢 ** 83.5** (`-2.5`) | 87.9 → 81.4 (`-6.5`) | 70.9 → 70.2 (`-0.7`) | 99.2 → 99.0 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-07_HERESY_PLUS1` | SO-07 (Przesłuchanie Oficjum): heresy 0 → 1 | 86.0 → 🟢 ** 83.0** (`-3.0`) | 87.9 → 82.3 (`-5.6`) | 70.9 → 69.8 (`-1.1`) | 99.2 → 97.0 (`-2.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_COST_PLUS1` | CAA-04 (Fałszywy Trop): cost 1 → 2 | 86.0 → 🟢 ** 82.8** (`-3.2`) | 87.9 → 87.8 (`-0.1`) | 70.9 → 61.8 (`-9.1`) | 99.2 → 98.9 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_HERESY_PLUS1` | KB-05 (List Żelazny): heresy 0 → 1 | 86.0 → 🟢 ** 82.3** (`-3.7`) | 87.9 → 83.0 (`-4.9`) | 70.9 → 66.4 (`-4.5`) | 99.2 → 97.5 (`-1.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_HERESY_PLUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 2 | 86.0 → 🟢 ** 81.8** (`-4.2`) | 87.9 → 87.5 (`-0.4`) | 70.9 | 99.2 → 87.1 (`-12.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 2 → 3 | 86.0 → 🟢 ** 81.2** (`-4.8`) | 87.9 → 87.4 (`-0.5`) | 70.9 → 57.5 (`-13.4`) | 99.2 → 98.8 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 0 → 1 | 86.0 → 🟢 ** 81.1** (`-4.9`) | 87.9 → 85.1 (`-2.8`) | 70.9 → 61.3 (`-9.6`) | 99.2 → 96.8 (`-2.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_HERESY_PLUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 2 | 86.0 → 🟢 ** 80.8** (`-5.2`) | 87.9 → 86.5 (`-1.4`) | 70.9 → 57.3 (`-13.6`) | 99.2 → 98.6 (`-0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_COST_MINUS1` | KT-01 (Rytuał Przejścia): cost 1 → 0 | 86.0 → 🟢 ** 80.8** (`-5.2`) | 87.9 → 86.2 (`-1.7`) | 70.9 → 70.0 (`-0.9`) | 99.2 → 86.1 (`-13.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_HERESY_PLUS1` | SO-01 (Patrol Familiariuszy): heresy 0 → 1 | 86.0 → 🟢 ** 80.3** (`-5.7`) | 87.9 → 82.0 (`-5.9`) | 70.9 → 60.3 (`-10.6`) | 99.2 → 98.7 (`-0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_COST_PLUS1` | SO-06 (Areszt Trybunalski): cost 2 → 3 | 86.0 → 🟢 ** 80.3** (`-5.7`) | 87.9 → 87.4 (`-0.5`) | 70.9 → 56.1 (`-14.8`) | 99.2 → 97.4 (`-1.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_HERESY_PLUS1` | CAA-04 (Fałszywy Trop): heresy 0 → 1 | 86.0 → 🟢 ** 80.1** (`-5.9`) | 87.9 → 86.7 (`-1.2`) | 70.9 → 57.2 (`-13.7`) | 99.2 → 96.3 (`-2.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_HERESY_PLUS1` | GC-06 (Szantaż): heresy 0 → 1 | 86.0 → 🟢 ** 80.0** (`-6.0`) | 87.9 → 84.3 (`-3.6`) | 70.9 → 57.5 (`-13.4`) | 99.2 → 98.2 (`-1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_COST_PLUS1` | KT-08 (Areszt Wiedzy): cost 2 → 3 | 86.0 → 🟢 ** 79.9** (`-6.1`) | 87.9 → 87.0 (`-0.9`) | 70.9 → 55.9 (`-15.0`) | 99.2 → 96.7 (`-2.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_COST_MINUS1` | KT-10 (Pieczęć Salomona): cost 1 → 0 | 86.0 → 🟢 ** 79.4** (`-6.6`) | 87.9 → 87.4 (`-0.5`) | 70.9 → 64.5 (`-6.4`) | 99.2 → 86.3 (`-12.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_COST_PLUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 2 | 86.0 → 🟢 ** 79.2** (`-6.8`) | 87.9 → 85.7 (`-2.2`) | 70.9 → 66.8 (`-4.1`) | 99.2 → 85.1 (`-14.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_HERESY_MINUS1` | CAA-10 (Echo Alhambry): heresy 1 → 0 | 86.0 → 🟢 ** 78.9** (`-7.1`) | 87.9 → 83.4 (`-4.5`) | 70.9 | 99.2 → 82.4 (`-16.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_HERESY_PLUS1` | KB-01 (Rozkaz Dworu): heresy 0 → 1 | 86.0 → 🟢 ** 78.5** (`-7.5`) | 87.9 → 77.7 (`-10.2`) | 70.9 → 60.4 (`-10.5`) | 99.2 → 97.3 (`-1.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_COST_MINUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 1 | 86.0 → 🟢 ** 78.0** (`-8.0`) | 87.9 → 86.5 (`-1.4`) | 70.9 → 66.8 (`-4.1`) | 99.2 → 80.6 (`-18.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 1 → 2 | 86.0 → 🟢 ** 77.6** (`-8.4`) | 87.9 → 86.0 (`-1.9`) | 70.9 → 62.3 (`-8.6`) | 99.2 → 84.6 (`-14.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-03_HERESY_PLUS1` | GC-03 (Podrzucenie Księgi): heresy 0 → 1 | 86.0 → 🟢 ** 77.3** (`-8.7`) | 87.9 → 84.3 (`-3.6`) | 70.9 → 62.8 (`-8.1`) | 99.2 → 84.7 (`-14.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_HERESY_PLUS1` | KB-07 (Szantaż Pieczęcią): heresy 0 → 1 | 86.0 → 🟢 ** 77.3** (`-8.7`) | 87.9 → 77.8 (`-10.1`) | 70.9 → 55.8 (`-15.1`) | 99.2 → 98.2 (`-1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_COST_PLUS1` | CAA-03 (Cień na Rynku): cost 1 → 2 | 86.0 → 🟢 ** 77.2** (`-8.8`) | 87.9 → 78.2 (`-9.7`) | 70.9 → 55.5 (`-15.4`) | 99.2 → 98.0 (`-1.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_COST_PLUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 2 | 86.0 → 🟢 ** 77.0** (`-9.0`) | 87.9 → 87.7 (`-0.2`) | 70.9 → 70.6 (`-0.3`) | 99.2 → 72.8 (`-26.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_COST_PLUS1` | SO-08 (Nasłanie Inkwizytora): cost 2 → 3 | 86.0 → 🟢 ** 76.9** (`-9.1`) | 87.9 → 83.3 (`-4.6`) | 70.9 → 63.0 (`-7.9`) | 99.2 → 84.5 (`-14.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_COST_MINUS1` | CAA-07 (Szantaż Bractwa): cost 2 → 1 | 86.0 → 🟢 ** 76.8** (`-9.2`) | 87.9 → 75.2 (`-12.7`) | 70.9 → 68.1 (`-2.8`) | 99.2 → 87.2 (`-12.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_HERESY_PLUS1` | GC-09 (Lista Dłużników): heresy 0 → 1 | 86.0 → 🟢 ** 76.8** (`-9.2`) | 87.9 → 85.5 (`-2.4`) | 70.9 → 59.4 (`-11.5`) | 99.2 → 85.5 (`-13.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 1 → 2 | 86.0 → 🟢 ** 76.5** (`-9.5`) | 87.9 → 83.2 (`-4.7`) | 70.9 → 61.9 (`-9.0`) | 99.2 → 84.3 (`-14.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_COST_PLUS1` | KB-03 (Plotka Dworska): cost 1 → 2 | 86.0 → 🟢 ** 76.3** (`-9.7`) | 87.9 → 79.2 (`-8.7`) | 70.9 → 66.7 (`-4.2`) | 99.2 → 83.1 (`-16.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_HERESY_PLUS1` | SO-08 (Nasłanie Inkwizytora): heresy 1 → 2 | 86.0 → 🟢 ** 76.3** (`-9.7`) | 87.9 → 77.2 (`-10.7`) | 70.9 → 53.9 (`-17.0`) | 99.2 → 97.8 (`-1.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_HERESY_PLUS1` | SO-10 (Oczyść Miasto): heresy 2 → 3 | 86.0 → 🟢 ** 76.1** (`-9.9`) | 87.9 → 77.5 (`-10.4`) | 70.9 → 53.0 (`-17.9`) | 99.2 → 97.9 (`-1.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_COST_PLUS1` | CAA-09 (Kurier Relikwii): cost 2 → 3 | 86.0 → 🟢 ** 76.0** (`-10.0`) | 87.9 → 85.2 (`-2.7`) | 70.9 → 55.9 (`-15.0`) | 99.2 → 87.0 (`-12.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_COST_PLUS1` | GC-09 (Lista Dłużników): cost 2 → 3 | 86.0 → 🟢 ** 76.0** (`-10.0`) | 87.9 → 86.6 (`-1.3`) | 70.9 → 68.1 (`-2.8`) | 99.2 → 73.4 (`-25.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_COST_MINUS1` | KT-07 (Archiwum Ukryte): cost 1 → 0 | 86.0 → 🟢 ** 75.7** (`-10.3`) | 87.9 → 87.4 (`-0.5`) | 70.9 → 70.2 (`-0.7`) | 99.2 → 69.5 (`-29.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_COST_MINUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 | 86.0 → 🟢 ** 75.6** (`-10.4`) | 87.9 → 80.0 (`-7.9`) | 70.9 → 61.8 (`-9.1`) | 99.2 → 85.1 (`-14.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_COST_MINUS1` | KB-04 (Faworyt Dworu): cost 1 → 0 | 86.0 → 🟢 ** 75.4** (`-10.6`) | 87.9 → 83.2 (`-4.7`) | 70.9 → 58.0 (`-12.9`) | 99.2 → 85.0 (`-14.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_COST_MINUS1` | CAA-08 (Kaptur Nocy): cost 1 → 0 | 86.0 → 🟢 ** 75.2** (`-10.8`) | 87.9 → 86.6 (`-1.3`) | 70.9 → 62.3 (`-8.6`) | 99.2 → 76.7 (`-22.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_HERESY_PLUS1` | KT-10 (Pieczęć Salomona): heresy 0 → 1 | 86.0 → 🟢 ** 74.6** (`-11.4`) | 87.9 → 82.6 (`-5.3`) | 70.9 → 59.8 (`-11.1`) | 99.2 → 81.5 (`-17.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_HERESY_PLUS1` | CAA-09 (Kurier Relikwii): heresy 0 → 1 | 86.0 → 🟢 ** 74.5** (`-11.5`) | 87.9 → 78.5 (`-9.4`) | 70.9 → 61.7 (`-9.2`) | 99.2 → 83.3 (`-15.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_COST_PLUS1` | GC-10 (Upadek Domu): cost 3 → 4 | 86.0 → 🟢 ** 73.9** (`-12.1`) | 87.9 → 80.7 (`-7.2`) | 70.9 → 70.2 (`-0.7`) | 99.2 → 70.8 (`-28.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): heresy 0 → 1 | 86.0 → 🟢 ** 73.8** (`-12.2`) | 87.9 → 84.6 (`-3.3`) | 70.9 → 54.8 (`-16.1`) | 99.2 → 81.9 (`-17.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_COST_PLUS1` | SO-10 (Oczyść Miasto): cost 4 → 5 | 86.0 → 🟢 ** 73.2** (`-12.8`) | 87.9 → 78.2 (`-9.7`) | 70.9 → 63.6 (`-7.3`) | 99.2 → 77.8 (`-21.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_COST_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 2 | 86.0 → 🟢 ** 73.1** (`-12.9`) | 87.9 → 82.3 (`-5.6`) | 70.9 → 39.1 (`-31.8`) | 99.2 → 98.0 (`-1.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): heresy 0 → 1 | 86.0 → 🟢 ** 72.6** (`-13.4`) | 87.9 → 73.4 (`-14.5`) | 70.9 → 59.3 (`-11.6`) | 99.2 → 85.2 (`-14.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 1 → 2 | 86.0 → 🟢 ** 71.9** (`-14.1`) | 87.9 → 83.9 (`-4.0`) | 70.9 → 59.2 (`-11.7`) | 99.2 → 72.6 (`-26.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_COST_MINUS1` | KT-09 (Fragment Kodeksu): cost 1 → 0 | 86.0 → 🟢 ** 71.5** (`-14.5`) | 87.9 → 86.3 (`-1.6`) | 70.9 → 66.8 (`-4.1`) | 99.2 → 61.5 (`-37.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_COST_MINUS1` | KB-03 (Plotka Dworska): cost 1 → 0 | 86.0 → 🟢 ** 71.1** (`-14.9`) | 87.9 → 77.5 (`-10.4`) | 70.9 → 60.5 (`-10.4`) | 99.2 → 75.4 (`-23.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_HERESY_PLUS1` | SO-04 (Publiczne Ostrzeżenie): heresy 0 → 1 | 86.0 → 🟢 ** 71.0** (`-15.0`) | 87.9 → 77.9 (`-10.0`) | 70.9 → 36.6 (`-34.3`) | 99.2 → 98.4 (`-0.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_HERESY_PLUS1` | GC-02 (Czarny Rynek): heresy 0 → 1 | 86.0 → 🟢 ** 70.8** (`-15.2`) | 87.9 → 85.9 (`-2.0`) | 70.9 → 46.6 (`-24.3`) | 99.2 → 79.8 (`-19.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_COST_PLUS1` | KB-05 (List Żelazny): cost 2 → 3 | 86.0 → 🟢 ** 70.6** (`-15.4`) | 87.9 → 85.3 (`-2.6`) | 70.9 → 55.9 (`-15.0`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_COST_MINUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 0 | 86.0 → 🟢 ** 70.2** (`-15.8`) | 87.9 → 87.8 (`-0.1`) | 70.9 → 60.4 (`-10.5`) | 99.2 → 62.3 (`-36.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_HERESY_PLUS1` | GC-04 (Informator): heresy 1 → 2 | 86.0 → 🟢 ** 69.6** (`-16.4`) | 87.9 → 82.2 (`-5.7`) | 70.9 → 48.8 (`-22.1`) | 99.2 → 77.7 (`-21.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_COST_MINUS1` | CAA-03 (Cień na Rynku): cost 1 → 0 | 86.0 → 🟢 ** 69.4** (`-16.6`) | 87.9 → 79.0 (`-8.9`) | 70.9 | 99.2 → 58.3 (`-40.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_HERESY_MINUS1` | GC-10 (Upadek Domu): heresy 2 → 1 | 86.0 → 🟢 ** 69.3** (`-16.7`) | 87.9 → 76.0 (`-11.9`) | 70.9 → 34.7 (`-36.2`) | 99.2 → 97.3 (`-1.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_COST_PLUS1` | CAA-06 (Ucieczka z Lochów): cost 2 → 3 | 86.0 → 🟢 ** 69.2** (`-16.8`) | 87.9 → 86.2 (`-1.7`) | 70.9 → 52.1 (`-18.8`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_COST_MINUS1` | GC-04 (Informator): cost 1 → 0 | 86.0 → 🟢 ** 68.8** (`-17.2`) | 87.9 → 73.7 (`-14.2`) | 70.9 → 34.2 (`-36.7`) | 99.2 → 98.6 (`-0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_COST_PLUS1` | CAA-10 (Echo Alhambry): cost 1 → 2 | 86.0 → 🟢 ** 68.5** (`-17.5`) | 87.9 → 63.0 (`-24.9`) | 70.9 → 60.3 (`-10.6`) | 99.2 → 82.3 (`-16.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_COST_MINUS1` | GC-07 (Skrytobójstwo): cost 2 → 1 | 86.0 → 🟢 ** 68.4** (`-17.6`) | 87.9 → 72.7 (`-15.2`) | 70.9 → 49.5 (`-21.4`) | 99.2 → 82.9 (`-16.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_HERESY_PLUS1` | KB-02 (Pobór Podatków): heresy 0 → 1 | 86.0 → 🟢 ** 67.2** (`-18.8`) | 87.9 → 80.2 (`-7.7`) | 70.9 → 54.1 (`-16.8`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_COST_MINUS1` | SO-08 (Nasłanie Inkwizytora): cost 2 → 1 | 86.0 → 🟢 ** 67.2** (`-18.8`) | 87.9 → 85.5 (`-2.4`) | 70.9 → 43.8 (`-27.1`) | 99.2 → 72.4 (`-26.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-03_COST_MINUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 0 | 86.0 → 🟢 ** 66.0** (`-20.0`) | 87.9 → 83.4 (`-4.5`) | 70.9 → 27.3 (`-43.6`) | 99.2 → 87.3 (`-11.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_COST_MINUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 0 | 86.0 → 🟢 ** 65.9** (`-20.1`) | 87.9 → 87.3 (`-0.6`) | 70.9 → 45.5 (`-25.4`) | 99.2 → 64.9 (`-34.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_HERESY_PLUS1` | KB-03 (Plotka Dworska): heresy 0 → 1 | 86.0 → 🟢 ** 65.8** (`-20.2`) | 87.9 → 84.1 (`-3.8`) | 70.9 → 56.3 (`-14.6`) | 99.2 → 56.9 (`-42.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_COST_MINUS1` | GC-02 (Czarny Rynek): cost 1 → 0 | 86.0 → 🟢 ** 64.3** (`-21.7`) | 87.9 → 83.8 (`-4.1`) | 70.9 → 29.0 (`-41.9`) | 99.2 → 80.1 (`-19.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_COST_MINUS1` | GC-08 (Zatrute Złoto): cost 1 → 0 | 86.0 → 🟢 ** 62.4** (`-23.6`) | 87.9 → 86.4 (`-1.5`) | 70.9 → 33.0 (`-37.9`) | 99.2 → 67.7 (`-31.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_COST_MINUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 0 | 86.0 → 🟢 ** 61.9** (`-24.1`) | 87.9 → 80.9 (`-7.0`) | 70.9 → 19.9 (`-51.0`) | 99.2 → 84.9 (`-14.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_COST_MINUS1` | SO-10 (Oczyść Miasto): cost 4 → 3 | 86.0 → 🟢 ** 61.5** (`-24.5`) | 87.9 → 87.1 (`-0.8`) | 70.9 → 62.4 (`-8.5`) | 99.2 → 35.1 (`-64.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_COST_MINUS1` | GC-06 (Szantaż): cost 2 → 1 | 86.0 → 🟢 ** 61.2** (`-24.8`) | 87.9 → 81.1 (`-6.8`) | 70.9 → 42.4 (`-28.5`) | 99.2 → 60.2 (`-39.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_HERESY_PLUS1` | GC-10 (Upadek Domu): heresy 2 → 3 | 86.0 → 🟢 ** 60.2** (`-25.8`) | 87.9 → 69.9 (`-18.0`) | 70.9 → 50.5 (`-20.4`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_HERESY_PLUS1` | CAA-10 (Echo Alhambry): heresy 1 → 2 | 86.0 → 🟢 ** 59.5** (`-26.5`) | 87.9 → 69.7 (`-18.2`) | 70.9 → 53.7 (`-17.2`) | 99.2 → 55.1 (`-44.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_COST_MINUS1` | GC-10 (Upadek Domu): cost 3 → 2 | 86.0 → 🟢 ** 56.3** (`-29.7`) | 87.9 | 70.9 → 19.9 (`-51.0`) | 99.2 → 61.2 (`-38.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_COST_MINUS1` | KB-10 (Pieczęć Korony): cost 2 → 1 | 86.0 → 🟢 ** 54.6** (`-31.4`) | 87.9 → 58.6 (`-29.3`) | 70.9 → 35.5 (`-35.4`) | 99.2 → 69.6 (`-29.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_COST_PLUS1` | KB-02 (Pobór Podatków): cost 1 → 2 | 86.0 → 🟢 ** 52.4** (`-33.6`) | 87.9 → 76.7 (`-11.2`) | 70.9 → 28.0 (`-42.9`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_HERESY_PLUS1` | KB-04 (Faworyt Dworu): heresy 1 → 2 | 86.0 → 🟢 ** 51.5** (`-34.5`) | 87.9 → 69.7 (`-18.2`) | 70.9 → 56.2 (`-14.7`) | 99.2 → 28.6 (`-70.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_COST_MINUS1` | KB-09 (Dekret Królewski): cost 3 → 2 | 86.0 → 🟢 ** 51.5** (`-34.5`) | 87.9 → 58.3 (`-29.6`) | 70.9 → 50.4 (`-20.5`) | 99.2 → 45.9 (`-53.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_HERESY_PLUS1` | KB-09 (Dekret Królewski): heresy 1 → 2 | 86.0 → 🟡 ** 43.1** (`-42.9`) | 87.9 → 63.8 (`-24.1`) | 70.9 → 22.4 (`-48.5`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_COST_PLUS1` | KB-10 (Pieczęć Korony): cost 2 → 3 | 86.0 → 🟡 ** 39.0** (`-47.0`) | 87.9 → 67.6 (`-20.3`) | 70.9 → 10.5 (`-60.4`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_COST_PLUS1` | KB-09 (Dekret Królewski): cost 3 → 4 | 86.0 → 🟡 ** 29.4** (`-56.6`) | 87.9 → 48.4 (`-39.5`) | 70.9 → 10.5 (`-60.4`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_HERESY_PLUS1` | KB-10 (Pieczęć Korony): heresy 2 → 3 | 86.0 → 🔴 ** 24.7** (`-61.3`) | 87.9 → 44.0 (`-43.9`) | 70.9 → 10.5 (`-60.4`) | 99.2 → 19.6 (`-79.6`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (71)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | 5.61 Er (1–9) | 3.0% | 28.6% | 1.02 (0–3) | 3.60 (0–15) | 0.53zł (0.0–2.3) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-04_HERESY_MINUS1` | 5.67 Er (1–9) | 3.2% | 28.7% | 1.03 (0–3) | 3.53 (0–16) | 0.53zł (0.0–2.3) | 6.16 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-09_HERESY_MINUS1` | 5.65 Er (1–9) | 3.0% | 28.7% | 1.03 (0–3) | 3.51 (0–15) | 0.53zł (0.0–2.3) | 6.13 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-08_COST_PLUS1` | 5.62 Er (1–9) | 2.9% | 28.7% | 1.02 (0–3) | 3.61 (0–14) | 0.53zł (0.0–2.3) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-07_COST_PLUS1` | 5.58 Er (1–9) | 2.7% | 28.8% | 1.02 (0–3) | 3.57 (0–17) | 0.52zł (0.0–3.0) | 6.21 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_HERESY_PLUS1` | 5.59 Er (1–9) | 2.8% | 28.6% | 1.01 (0–3) | 3.73 (0–16) | 0.53zł (0.0–2.3) | 6.36 (1.4–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_HERESY_PLUS1` | 5.59 Er (1–9) | 2.8% | 28.6% | 1.02 (0–3) | 3.69 (0–15) | 0.53zł (0.0–2.3) | 6.32 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-05_HERESY_PLUS1` | 5.61 Er (1–9) | 3.5% | 28.6% | 1.02 (0–3) | 3.68 (0–18) | 0.53zł (0.0–2.3) | 6.37 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-10_COST_PLUS1` | 5.64 Er (1–9) | 3.6% | 28.9% | 1.02 (0–3) | 3.62 (0–15) | 0.43zł (0.0–2.3) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-01_COST_MINUS1` | 5.58 Er (1–9) | 2.5% | 28.1% | 1.00 (0–3) | 3.61 (0–15) | 0.54zł (0.0–2.3) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-07_HERESY_PLUS1` | 5.61 Er (1–9) | 3.8% | 28.6% | 1.02 (0–3) | 3.68 (0–18) | 0.53zł (0.0–2.7) | 6.38 (1.3–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_HERESY_PLUS1` | 5.57 Er (1–9) | 2.7% | 28.6% | 1.02 (0–3) | 3.69 (0–14) | 0.52zł (0.0–2.7) | 6.34 (1.3–10.0) | 🟢 W NORMIE |
| `L3_KT-01_HERESY_PLUS1` | 5.62 Er (1–9) | 3.9% | 28.7% | 1.02 (0–3) | 3.67 (0–18) | 0.53zł (0.0–2.7) | 6.36 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-01_COST_PLUS1` | 5.61 Er (1–9) | 2.6% | 29.7% | 1.02 (0–3) | 3.65 (0–16) | 0.55zł (0.0–2.3) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-03_COST_PLUS1` | 5.65 Er (1–9) | 3.2% | 29.2% | 1.02 (0–3) | 3.58 (0–15) | 0.54zł (0.0–2.7) | 6.20 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-03_HERESY_MINUS1` | 5.62 Er (1–9) | 2.7% | 28.7% | 1.02 (0–3) | 3.56 (0–15) | 0.51zł (0.0–2.3) | 6.09 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-06_HERESY_PLUS1` | 5.60 Er (1–9) | 2.8% | 28.6% | 1.01 (0–3) | 3.62 (0–15) | 0.53zł (0.0–2.3) | 6.27 (1.3–10.0) | 🟢 W NORMIE |
| `L3_GC-02_COST_PLUS1` | 5.67 Er (1–9) | 3.6% | 30.5% | 1.04 (0–3) | 3.65 (0–15) | 0.52zł (0.0–2.3) | 6.20 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-06_HERESY_PLUS1` | 5.60 Er (1–9) | 3.1% | 28.5% | 1.02 (0–3) | 3.61 (0–19) | 0.54zł (0.0–2.3) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-09_HERESY_PLUS1` | 5.56 Er (1–9) | 2.4% | 28.5% | 1.02 (0–3) | 3.64 (0–15) | 0.53zł (0.0–2.7) | 6.30 (1.3–10.0) | 🟢 W NORMIE |
| `L3_KT-03_COST_PLUS1` | 5.63 Er (1–9) | 3.3% | 29.1% | 1.02 (0–3) | 3.63 (0–15) | 0.40zł (0.0–2.0) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-04_COST_PLUS1` | 5.65 Er (1–9) | 3.4% | 29.3% | 1.03 (0–3) | 3.56 (0–14) | 0.54zł (0.0–2.7) | 6.18 (1.3–10.0) | 🟢 W NORMIE |
| `L3_KT-06_HERESY_PLUS1` | 5.64 Er (1–9) | 4.9% | 28.7% | 1.02 (0–3) | 3.73 (0–18) | 0.54zł (0.0–2.7) | 6.40 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-07_HERESY_PLUS1` | 5.61 Er (1–9) | 3.0% | 28.6% | 1.02 (0–3) | 3.65 (0–14) | 0.53zł (0.0–2.3) | 6.29 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-02_COST_MINUS1` | 5.58 Er (1–9) | 2.5% | 28.5% | 1.01 (0–3) | 3.61 (0–15) | 0.54zł (0.0–2.5) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-09_COST_PLUS1` | 5.60 Er (1–9) | 2.9% | 28.7% | 1.04 (0–3) | 3.58 (0–15) | 0.54zł (0.0–2.5) | 6.22 (1.3–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_HERESY_PLUS1` | 5.61 Er (1–9) | 3.3% | 28.6% | 1.02 (0–3) | 3.65 (0–15) | 0.53zł (0.0–2.3) | 6.29 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-04_COST_PLUS1` | 5.67 Er (1–9) | 3.0% | 29.7% | 1.03 (0–3) | 3.63 (0–15) | 0.55zł (0.0–2.7) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-05_COST_PLUS1` | 5.65 Er (1–9) | 3.4% | 29.0% | 1.02 (0–3) | 3.62 (0–15) | 0.44zł (0.0–2.3) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-08_HERESY_MINUS1` | 5.66 Er (1–9) | 3.4% | 28.8% | 1.03 (0–3) | 3.52 (0–15) | 0.53zł (0.0–2.3) | 6.09 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_HERESY_MINUS1` | 5.61 Er (1–9) | 3.1% | 28.6% | 1.02 (0–3) | 3.55 (0–15) | 0.53zł (0.0–2.3) | 6.14 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-10_HERESY_MINUS1` | 5.71 Er (1–9) | 3.2% | 28.9% | 1.04 (0–3) | 3.34 (0–14) | 0.53zł (0.0–2.7) | 6.09 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_PLUS1` | 5.64 Er (1–9) | 3.4% | 29.0% | 1.02 (0–3) | 3.62 (0–16) | 0.44zł (0.0–2.3) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-02_HERESY_PLUS1` | 5.61 Er (1–9) | 3.8% | 28.7% | 1.02 (0–3) | 3.68 (0–18) | 0.53zł (0.0–2.7) | 6.36 (1.5–10.0) | 🟢 W NORMIE |
| `L3_SO-04_COST_MINUS1` | 5.60 Er (1–9) | 3.0% | 27.4% | 1.06 (0–3) | 3.66 (0–15) | 0.55zł (0.0–2.7) | 6.27 (1.3–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_HERESY_PLUS1` | 5.58 Er (1–9) | 2.9% | 28.6% | 1.01 (0–3) | 3.70 (0–15) | 0.53zł (0.0–2.3) | 6.35 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-06_COST_MINUS1` | 5.60 Er (1–9) | 3.3% | 27.7% | 1.02 (0–3) | 3.60 (0–15) | 0.51zł (0.0–3.0) | 6.22 (1.3–10.0) | 🟢 W NORMIE |
| `L3_KB-07_COST_MINUS1` | 5.60 Er (1–9) | 3.0% | 28.3% | 1.02 (0–3) | 3.61 (0–14) | 0.52zł (0.0–2.3) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-02_COST_MINUS1` | 5.61 Er (1–9) | 3.1% | 28.5% | 1.02 (0–3) | 3.60 (0–15) | 0.71zł (0.0–2.7) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-08_COST_MINUS1` | 5.63 Er (1–9) | 3.1% | 28.6% | 1.02 (0–3) | 3.66 (0–17) | 0.53zł (0.0–2.3) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-02_COST_PLUS1` | 5.65 Er (1–9) | 3.3% | 30.7% | 1.00 (0–3) | 3.57 (0–15) | 0.54zł (0.0–2.7) | 6.21 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-02_COST_PLUS1` | 5.63 Er (1–9) | 3.5% | 29.4% | 1.02 (0–3) | 3.64 (0–15) | 0.43zł (0.0–2.0) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-06_COST_PLUS1` | 5.60 Er (1–9) | 2.9% | 28.8% | 1.02 (0–3) | 3.61 (0–15) | 0.54zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-03_COST_PLUS1` | 5.65 Er (1–9) | 3.3% | 29.3% | 1.02 (0–4) | 3.57 (0–15) | 0.53zł (0.0–2.3) | 6.19 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-04_COST_PLUS1` | 5.65 Er (1–9) | 3.6% | 29.0% | 1.02 (0–3) | 3.60 (0–15) | 0.44zł (0.0–2.3) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-07_COST_PLUS1` | 5.59 Er (1–9) | 3.0% | 28.6% | 1.03 (0–3) | 3.62 (0–15) | 0.55zł (0.0–2.3) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-06_COST_PLUS1` | 5.67 Er (1–9) | 3.7% | 29.2% | 1.03 (0–3) | 3.69 (0–16) | 0.53zł (0.0–2.3) | 6.31 (1.3–10.0) | 🟢 W NORMIE |
| `L3_GC-07_COST_PLUS1` | 5.61 Er (1–9) | 3.4% | 28.9% | 1.03 (0–3) | 3.62 (0–16) | 0.52zł (0.0–2.3) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_COST_MINUS1` | 5.58 Er (1–9) | 2.9% | 28.4% | 1.02 (0–3) | 3.57 (0–17) | 0.58zł (0.0–2.7) | 6.21 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-08_HERESY_PLUS1` | 5.62 Er (1–9) | 3.7% | 28.7% | 1.02 (0–3) | 3.68 (0–18) | 0.53zł (0.0–2.7) | 6.37 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_COST_MINUS1` | 5.58 Er (1–9) | 2.9% | 28.4% | 1.02 (0–3) | 3.59 (0–17) | 0.57zł (0.0–2.3) | 6.21 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-03_COST_MINUS1` | 5.59 Er (1–9) | 2.9% | 27.4% | 1.04 (0–3) | 3.64 (0–15) | 0.54zł (0.0–2.3) | 6.25 (1.3–10.0) | 🟢 W NORMIE |
| `L3_KB-05_COST_MINUS1` | 5.57 Er (1–9) | 2.5% | 28.7% | 1.02 (0–3) | 3.56 (0–14) | 0.51zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-05_COST_MINUS1` | 5.61 Er (1–9) | 3.2% | 28.5% | 1.02 (0–3) | 3.60 (0–15) | 0.71zł (0.0–2.7) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-08_COST_MINUS1` | 5.62 Er (1–9) | 3.2% | 28.6% | 1.02 (0–4) | 3.60 (0–15) | 0.70zł (0.0–2.7) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-04_HERESY_MINUS1` | 5.62 Er (1–9) | 3.1% | 28.7% | 1.02 (0–3) | 3.49 (0–15) | 0.53zł (0.0–2.3) | 6.08 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_COST_PLUS1` | 5.63 Er (1–9) | 2.9% | 30.2% | 1.02 (0–3) | 3.56 (0–16) | 0.59zł (0.0–2.3) | 6.15 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-04_COST_MINUS1` | 5.61 Er (1–9) | 3.1% | 28.5% | 1.02 (0–3) | 3.60 (0–15) | 0.70zł (0.0–2.7) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-03_HERESY_PLUS1` | 5.52 Er (1–9) | 2.5% | 28.3% | 1.01 (0–3) | 3.68 (0–15) | 0.53zł (0.0–2.3) | 6.33 (1.3–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_COST_MINUS1` | 5.57 Er (1–9) | 2.9% | 28.6% | 1.02 (0–3) | 3.56 (0–16) | 0.54zł (0.0–2.7) | 6.17 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_COST_MINUS1` | 5.59 Er (1–9) | 2.9% | 28.2% | 1.02 (0–3) | 3.61 (0–17) | 0.56zł (0.0–2.7) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-04_HERESY_PLUS1` | 5.60 Er (1–9) | 3.6% | 28.6% | 1.02 (0–3) | 3.69 (0–18) | 0.53zł (0.0–2.7) | 6.36 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_COST_MINUS1` | 5.58 Er (1–9) | 2.8% | 28.4% | 1.02 (0–3) | 3.58 (0–17) | 0.57zł (0.0–2.3) | 6.21 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-07_COST_PLUS1` | 5.64 Er (1–9) | 3.5% | 29.1% | 1.02 (0–3) | 3.64 (0–15) | 0.43zł (0.0–2.3) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_COST_MINUS1` | 5.57 Er (1–9) | 2.8% | 28.6% | 1.01 (0–3) | 3.57 (0–17) | 0.54zł (0.0–2.7) | 6.16 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-06_COST_MINUS1` | 5.66 Er (1–9) | 3.7% | 28.2% | 1.02 (0–3) | 3.71 (0–16) | 0.52zł (0.0–2.3) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-06_COST_PLUS1` | 5.65 Er (1–9) | 3.9% | 29.2% | 1.02 (0–3) | 3.62 (0–15) | 0.46zł (0.0–2.3) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-01_COST_PLUS1` | 5.61 Er (1–9) | 3.0% | 29.3% | 1.02 (0–3) | 3.63 (0–15) | 0.54zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-07_COST_MINUS1` | 5.57 Er (1–9) | 3.2% | 27.5% | 1.04 (0–3) | 3.60 (0–15) | 0.52zł (0.0–2.3) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-09_COST_MINUS1` | 5.62 Er (1–9) | 2.7% | 28.4% | 1.02 (0–3) | 3.69 (0–15) | 0.56zł (0.0–2.3) | 6.34 (1.5–10.0) | 🟢 W NORMIE |
| `L3_SO-09_COST_MINUS1` | 5.61 Er (1–9) | 3.2% | 27.7% | 1.04 (0–3) | 3.60 (0–15) | 0.52zł (0.0–3.0) | 6.25 (1.3–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 90 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_GC-05_COST_PLUS1` | 5.61 Er (1–9) | 3.0% | 28.6% | 1.02 (0–3) | 3.60 (0–15) | 0.53zł (0.0–2.3) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-05_HERESY_PLUS1` | 5.61 Er (1–9) | 3.0% | 28.6% | 1.02 (0–3) | 3.60 (0–15) | 0.53zł (0.0–2.3) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-05_COST_PLUS1` | 5.61 Er (1–9) | 3.0% | 28.6% | 1.02 (0–3) | 3.60 (0–15) | 0.53zł (0.0–2.3) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-05_HERESY_PLUS1` | 5.61 Er (1–9) | 3.0% | 28.6% | 1.02 (0–3) | 3.60 (0–15) | 0.53zł (0.0–2.3) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-09_COST_PLUS1` | 5.65 Er (1–9) | 3.6% | 29.1% | 1.02 (0–3) | 3.60 (0–15) | 0.44zł (0.0–2.3) | 6.22 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_HERESY_PLUS1` | 5.58 Er (1–9) | 2.8% | 28.5% | 1.01 (0–3) | 3.68 (0–15) | 0.53zł (0.0–2.3) | 6.33 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-09_HERESY_MINUS1` | 5.61 Er (1–9) | 3.1% | 28.6% | 1.02 (0–3) | 3.57 (0–14) | 0.54zł (0.0–2.7) | 6.10 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-08_HERESY_PLUS1` | 5.60 Er (1–9) | 3.0% | 28.6% | 1.02 (0–3) | 3.62 (0–15) | 0.53zł (0.0–2.3) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-03_HERESY_PLUS1` | 5.62 Er (1–9) | 4.4% | 28.6% | 1.02 (0–3) | 3.71 (0–18) | 0.54zł (0.0–3.0) | 6.37 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-07_HERESY_MINUS1` | 5.60 Er (1–9) | 3.2% | 28.6% | 1.02 (0–4) | 3.60 (0–14) | 0.52zł (0.0–2.3) | 6.16 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_HERESY_MINUS1` | 5.63 Er (1–9) | 3.0% | 28.7% | 1.02 (0–3) | 3.52 (0–14) | 0.53zł (0.0–2.3) | 6.06 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-10_HERESY_MINUS1` | 5.70 Er (1–9) | 3.4% | 28.9% | 1.03 (0–4) | 3.53 (0–15) | 0.53zł (0.0–2.3) | 6.18 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-07_HERESY_PLUS1` | 5.56 Er (1–9) | 2.6% | 28.5% | 1.01 (0–3) | 3.64 (0–15) | 0.53zł (0.0–2.3) | 6.30 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_COST_PLUS1` | 5.65 Er (1–9) | 3.2% | 30.1% | 1.02 (0–3) | 3.60 (0–14) | 0.55zł (0.0–2.3) | 6.22 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-05_HERESY_PLUS1` | 5.59 Er (1–9) | 2.9% | 28.6% | 1.02 (0–3) | 3.65 (0–15) | 0.53zł (0.0–2.3) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-09_HERESY_PLUS1` | 5.62 Er (1–9) | 4.2% | 28.7% | 1.02 (0–3) | 3.72 (0–18) | 0.53zł (0.0–3.0) | 6.38 (1.3–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_COST_PLUS1` | 5.62 Er (1–9) | 3.0% | 29.3% | 1.02 (0–3) | 3.59 (0–18) | 0.53zł (0.0–2.3) | 6.22 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-08_HERESY_PLUS1` | 5.60 Er (1–9) | 2.9% | 28.7% | 1.02 (0–3) | 3.67 (0–13) | 0.53zł (0.0–2.3) | 6.34 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_HERESY_PLUS1` | 5.58 Er (1–9) | 2.7% | 28.6% | 1.02 (0–3) | 3.66 (0–15) | 0.53zł (0.0–2.3) | 6.31 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_MINUS1` | 5.62 Er (1–9) | 3.1% | 28.6% | 1.02 (0–3) | 3.60 (0–15) | 0.70zł (0.0–2.7) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-01_HERESY_PLUS1` | 5.54 Er (1–9) | 2.4% | 28.4% | 1.01 (0–3) | 3.64 (0–15) | 0.53zł (0.0–2.3) | 6.31 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-06_COST_PLUS1` | 5.59 Er (1–9) | 2.8% | 28.5% | 1.04 (0–3) | 3.59 (0–15) | 0.54zł (0.0–2.7) | 6.24 (1.3–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_HERESY_PLUS1` | 5.57 Er (1–9) | 2.7% | 28.5% | 1.02 (0–3) | 3.69 (0–14) | 0.53zł (0.0–2.3) | 6.33 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-06_HERESY_PLUS1` | 5.61 Er (1–9) | 3.0% | 28.6% | 1.02 (0–3) | 3.67 (0–15) | 0.53zł (0.0–2.3) | 6.35 (1.4–10.0) | 🟢 W NORMIE |
| `L3_KT-08_COST_PLUS1` | 5.63 Er (1–9) | 3.5% | 29.1% | 1.02 (0–3) | 3.61 (0–15) | 0.45zł (0.0–2.3) | 6.22 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-10_COST_MINUS1` | 5.63 Er (1–9) | 3.2% | 28.6% | 1.02 (0–3) | 3.61 (0–15) | 0.71zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-01_COST_PLUS1` | 5.61 Er (1–9) | 3.0% | 29.1% | 1.02 (0–3) | 3.60 (0–15) | 0.54zł (0.0–2.3) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_MINUS1` | 5.63 Er (1–9) | 3.1% | 28.7% | 1.02 (0–3) | 3.44 (0–15) | 0.53zł (0.0–2.5) | 5.82 (0.7–9.7) | 🟢 W NORMIE |
| `L3_KB-01_HERESY_PLUS1` | 5.58 Er (1–9) | 2.8% | 28.6% | 1.01 (0–3) | 3.63 (0–14) | 0.53zł (0.0–2.3) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-06_COST_MINUS1` | 5.62 Er (1–9) | 3.2% | 28.6% | 1.02 (0–4) | 3.61 (0–15) | 0.74zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_PLUS1` | 5.68 Er (1–9) | 3.7% | 29.7% | 1.03 (0–3) | 3.57 (0–15) | 0.52zł (0.0–2.3) | 6.19 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-03_HERESY_PLUS1` | 5.58 Er (1–9) | 2.8% | 28.5% | 1.02 (0–3) | 3.68 (0–15) | 0.53zł (0.0–2.3) | 6.34 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-07_HERESY_PLUS1` | 5.57 Er (1–9) | 2.6% | 28.5% | 1.01 (0–3) | 3.61 (0–18) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_COST_PLUS1` | 5.67 Er (1–9) | 3.6% | 29.6% | 1.03 (0–3) | 3.64 (0–17) | 0.54zł (0.0–2.3) | 6.20 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-04_COST_PLUS1` | 5.60 Er (1–9) | 3.2% | 29.3% | 1.00 (0–3) | 3.61 (0–15) | 0.53zł (0.0–2.3) | 6.21 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-08_COST_PLUS1` | 5.64 Er (1–9) | 3.5% | 28.9% | 1.03 (0–3) | 3.57 (0–15) | 0.54zł (0.0–3.0) | 6.18 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_COST_MINUS1` | 5.55 Er (1–9) | 2.6% | 28.5% | 1.01 (0–3) | 3.56 (0–15) | 0.54zł (0.0–2.3) | 6.16 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-09_HERESY_PLUS1` | 5.60 Er (1–9) | 3.0% | 28.5% | 1.02 (0–3) | 3.68 (0–14) | 0.53zł (0.0–3.0) | 6.36 (1.5–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_COST_PLUS1` | 5.66 Er (1–9) | 3.8% | 31.2% | 1.02 (0–3) | 3.69 (0–17) | 0.56zł (0.0–2.3) | 6.26 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-03_COST_PLUS1` | 5.62 Er (1–9) | 2.7% | 29.8% | 1.02 (0–3) | 3.55 (0–17) | 0.54zł (0.0–2.3) | 6.18 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-08_HERESY_PLUS1` | 5.51 Er (1–9) | 2.2% | 28.3% | 1.01 (0–3) | 3.66 (0–15) | 0.53zł (0.0–2.3) | 6.30 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-10_HERESY_PLUS1` | 5.50 Er (1–9) | 2.8% | 28.3% | 1.01 (0–3) | 3.66 (0–15) | 0.52zł (0.0–2.3) | 6.22 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_COST_PLUS1` | 5.66 Er (1–9) | 3.4% | 29.6% | 1.02 (0–3) | 3.60 (0–14) | 0.53zł (0.0–2.3) | 6.21 (1.3–10.0) | 🟢 W NORMIE |
| `L3_GC-09_COST_PLUS1` | 5.67 Er (1–9) | 3.6% | 29.2% | 1.04 (0–3) | 3.62 (0–14) | 0.51zł (0.0–2.3) | 6.22 (1.3–10.0) | 🟢 W NORMIE |
| `L3_KT-07_COST_MINUS1` | 5.63 Er (1–9) | 3.2% | 28.6% | 1.02 (0–3) | 3.61 (0–15) | 0.71zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_COST_MINUS1` | 5.58 Er (1–9) | 2.9% | 28.4% | 1.01 (0–3) | 3.59 (0–17) | 0.56zł (0.0–2.7) | 6.20 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-04_COST_MINUS1` | 5.55 Er (1–9) | 2.8% | 28.1% | 1.01 (0–3) | 3.61 (0–16) | 0.54zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_COST_MINUS1` | 5.60 Er (1–9) | 3.0% | 28.5% | 1.02 (0–3) | 3.65 (0–17) | 0.58zł (0.0–2.3) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-10_HERESY_PLUS1` | 5.60 Er (1–9) | 4.1% | 28.6% | 1.02 (0–3) | 3.82 (0–17) | 0.54zł (0.0–2.3) | 6.48 (1.4–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_HERESY_PLUS1` | 5.58 Er (1–9) | 2.7% | 28.5% | 1.01 (0–3) | 3.79 (0–16) | 0.53zł (0.0–2.3) | 6.42 (1.8–10.0) | 🟢 W NORMIE |
| `L3_GC-10_COST_PLUS1` | 5.67 Er (2–9) | 3.5% | 29.2% | 1.03 (0–3) | 3.56 (0–18) | 0.52zł (0.0–2.7) | 6.10 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-01_HERESY_PLUS1` | 5.60 Er (1–9) | 3.0% | 28.6% | 1.02 (0–3) | 3.64 (0–15) | 0.53zł (0.0–2.3) | 6.34 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-10_COST_PLUS1` | 5.73 Er (2–9) | 4.0% | 27.9% | 0.88 (0–3) | 3.50 (0–15) | 0.53zł (0.0–2.7) | 6.18 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_COST_PLUS1` | 5.68 Er (1–9) | 3.7% | 29.6% | 1.03 (0–3) | 3.64 (0–15) | 0.54zł (0.0–2.3) | 6.22 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-02_HERESY_PLUS1` | 5.50 Er (1–9) | 2.3% | 28.3% | 1.02 (0–3) | 3.67 (0–15) | 0.53zł (0.0–2.3) | 6.31 (1.3–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_COST_PLUS1` | 5.65 Er (1–9) | 3.5% | 30.1% | 1.02 (0–3) | 3.70 (0–17) | 0.57zł (0.0–2.3) | 6.26 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-09_COST_MINUS1` | 5.62 Er (1–9) | 3.3% | 28.6% | 1.02 (0–3) | 3.61 (0–15) | 0.72zł (0.0–2.7) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-03_COST_MINUS1` | 5.57 Er (1–9) | 2.5% | 28.1% | 1.01 (0–4) | 3.65 (0–16) | 0.54zł (0.0–2.3) | 6.29 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-04_HERESY_PLUS1` | 5.50 Er (1–9) | 2.3% | 28.3% | 1.01 (0–3) | 3.68 (0–15) | 0.52zł (0.0–2.3) | 6.33 (1.3–10.0) | 🟢 W NORMIE |
| `L3_GC-02_HERESY_PLUS1` | 5.59 Er (1–9) | 2.9% | 28.6% | 1.02 (0–3) | 3.69 (0–14) | 0.53zł (0.0–3.0) | 6.34 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-05_COST_PLUS1` | 5.64 Er (1–9) | 3.1% | 29.3% | 1.03 (0–3) | 3.61 (0–14) | 0.53zł (0.0–2.3) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-01_COST_MINUS1` | 5.59 Er (2–9) | 3.1% | 27.5% | 1.03 (0–4) | 3.62 (0–15) | 0.54zł (0.0–2.3) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-04_HERESY_PLUS1` | 5.59 Er (1–9) | 3.0% | 28.5% | 1.02 (0–3) | 3.71 (0–15) | 0.53zł (0.0–2.3) | 6.35 (1.4–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_COST_MINUS1` | 5.58 Er (1–9) | 2.7% | 28.5% | 1.01 (0–3) | 3.60 (0–17) | 0.57zł (0.0–2.7) | 6.21 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-10_HERESY_MINUS1` | 5.65 Er (1–9) | 3.5% | 28.8% | 1.04 (0–3) | 3.32 (0–15) | 0.53zł (0.0–2.3) | 6.02 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_COST_PLUS1` | 5.63 Er (1–9) | 3.5% | 29.0% | 1.02 (0–3) | 3.64 (0–15) | 0.54zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-04_COST_MINUS1` | 5.58 Er (1–9) | 2.8% | 28.0% | 1.01 (0–3) | 3.67 (0–15) | 0.55zł (0.0–2.3) | 6.30 (1.4–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_COST_PLUS1` | 5.72 Er (1–9) | 3.6% | 29.6% | 1.04 (0–3) | 3.66 (0–14) | 0.54zł (0.0–2.3) | 6.20 (1.3–10.0) | 🟢 W NORMIE |
| `L3_GC-07_COST_MINUS1` | 5.59 Er (1–9) | 2.9% | 28.2% | 1.02 (0–3) | 3.63 (0–15) | 0.51zł (0.0–2.3) | 6.32 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-02_HERESY_PLUS1` | 5.58 Er (1–9) | 2.8% | 28.7% | 1.02 (0–3) | 3.68 (0–19) | 0.53zł (0.0–2.3) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-08_COST_MINUS1` | 5.54 Er (1–9) | 2.9% | 27.3% | 1.03 (0–4) | 3.60 (0–15) | 0.50zł (0.0–3.0) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-03_COST_MINUS1` | 5.59 Er (1–9) | 3.1% | 27.9% | 1.01 (0–3) | 3.65 (0–14) | 0.56zł (0.0–2.7) | 6.31 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-02_COST_MINUS1` | 5.59 Er (1–9) | 3.3% | 27.5% | 1.07 (0–3) | 3.63 (0–15) | 0.58zł (0.0–2.7) | 6.28 (1.3–10.0) | 🟢 W NORMIE |
| `L3_KB-03_HERESY_PLUS1` | 5.59 Er (1–9) | 2.9% | 28.5% | 1.02 (0–3) | 3.68 (0–19) | 0.53zł (0.0–2.3) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-02_COST_MINUS1` | 5.58 Er (1–9) | 2.9% | 27.9% | 1.02 (0–3) | 3.62 (0–15) | 0.56zł (0.0–2.7) | 6.31 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_MINUS1` | 5.57 Er (1–9) | 2.8% | 27.9% | 1.01 (0–3) | 3.62 (0–15) | 0.55zł (0.0–2.3) | 6.30 (1.3–10.0) | 🟢 W NORMIE |
| `L3_GC-01_COST_MINUS1` | 5.59 Er (1–9) | 2.9% | 27.9% | 1.02 (0–3) | 3.59 (0–15) | 0.55zł (0.0–2.3) | 6.30 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-10_COST_MINUS1` | 5.57 Er (1–9) | 2.8% | 27.5% | 1.12 (0–4) | 3.64 (0–15) | 0.56zł (0.0–2.3) | 6.31 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-06_COST_MINUS1` | 5.57 Er (1–9) | 2.9% | 28.1% | 1.01 (0–3) | 3.61 (0–15) | 0.55zł (0.0–2.7) | 6.29 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-10_HERESY_PLUS1` | 5.52 Er (1–9) | 3.0% | 28.2% | 1.00 (0–3) | 3.93 (0–15) | 0.53zł (0.0–2.3) | 6.37 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_PLUS1` | 5.52 Er (1–9) | 2.6% | 28.3% | 1.00 (0–3) | 3.85 (0–17) | 0.52zł (0.0–2.3) | 6.44 (1.7–10.0) | 🟢 W NORMIE |
| `L3_GC-10_COST_MINUS1` | 5.56 Er (1–9) | 2.4% | 28.3% | 1.01 (0–3) | 3.68 (0–15) | 0.50zł (0.0–2.7) | 6.34 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-10_COST_MINUS1` | 5.48 Er (1–9) | 2.0% | 28.5% | 0.99 (0–3) | 3.65 (0–14) | 0.50zł (0.0–2.3) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-02_COST_PLUS1` | 5.67 Er (1–9) | 3.6% | 31.0% | 1.02 (0–3) | 3.70 (0–15) | 0.54zł (0.0–2.3) | 6.23 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-04_HERESY_PLUS1` | 5.54 Er (1–9) | 2.9% | 28.4% | 1.01 (0–3) | 3.72 (0–19) | 0.53zł (0.0–2.7) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-09_COST_MINUS1` | 5.50 Er (1–9) | 1.9% | 28.5% | 1.00 (0–3) | 3.57 (0–14) | 0.49zł (0.0–2.3) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-09_HERESY_PLUS1` | 5.60 Er (1–9) | 3.4% | 28.5% | 1.02 (0–3) | 3.74 (0–16) | 0.54zł (0.0–2.3) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-10_COST_PLUS1` | 5.71 Er (1–9) | 4.6% | 29.7% | 1.04 (0–3) | 3.67 (0–17) | 0.54zł (0.0–2.3) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-09_COST_PLUS1` | 5.76 Er (1–9) | 4.3% | 30.2% | 1.04 (0–3) | 3.75 (0–17) | 0.51zł (0.0–2.7) | 6.28 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-10_HERESY_PLUS1` | 5.45 Er (1–9) | 2.5% | 28.2% | 0.99 (0–3) | 3.90 (0–18) | 0.53zł (0.0–2.3) | 6.24 (1.2–10.0) | 🟢 W NORMIE |

</details>