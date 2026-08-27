[Strona główna](../../../../../README.md) > [v0.19](README.md) > [audyt_level3_raport](audyt_level3_raport.md)

---

# Raport Precyzyjnego Audytu Poziomu 3 (Parametry Pojedynczych Kart) — Wersja Balansu: v0.19

**Wersja Balansu:** `v0.19` | **Data:** 2026-08-14 13:53 | **Przeanalizowano Wariantów Kart:** 161 | **Próba:** 2000 gier/setup | **Czas:** 637.16s
**Filtry:** Parametry: `cost,heresy` | Frakcja: `all` | Karta: `Wszystkie`
**Wynik Bazy Poziomu 3 (Global):** `🟢 91.1 pkt` | 3p: `87.1 pkt` | 4p: `86.9 pkt` | 5p: `99.2 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (75)

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | Baza (Bieżące parametry wszystkich kart) | 🟢 ** 91.1** | 87.1 | 86.9 | 99.2 | ⚪ OPTYMALNY |
| `L3_CAA-03_COST_MINUS1` | CAA-03 (Cień na Rynku): cost 1 → 0 | 91.1 → 🟢 ** 93.4** (`⬆️ +2.3`) | 87.1 → 86.3 (`-0.8`) | 86.9 → 94.7 (`⬆️ +7.8`) | 99.2 → 99.1 (`-0.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-08_COST_MINUS1` | KB-08 (Przekupstwo Sędziego): cost 3 → 2 | 91.1 → 🟢 ** 92.4** (`⬆️ +1.3`) | 87.1 → 88.5 (`⬆️ +1.4`) | 86.9 → 90.7 (`⬆️ +3.8`) | 99.2 → 98.1 (`-1.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-05_COST_MINUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 | 91.1 → 🟢 ** 91.9** (`⬆️ +0.8`) | 87.1 → 86.3 (`-0.8`) | 86.9 → 90.0 (`⬆️ +3.1`) | 99.2 → 99.5 (`⬆️ +0.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-06_COST_MINUS1` | SO-06 (Areszt Trybunalski): cost 2 → 1 | 91.1 → 🟢 ** 91.8** (`⬆️ +0.7`) | 87.1 → 86.3 (`-0.8`) | 86.9 → 91.6 (`⬆️ +4.7`) | 99.2 → 97.4 (`-1.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-03_HERESY_PLUS1` | GC-03 (Podrzucenie Księgi): heresy 0 → 1 | 91.1 → 🟢 ** 91.7** (`⬆️ +0.6`) | 87.1 → 86.4 (`-0.7`) | 86.9 → 89.7 (`⬆️ +2.8`) | 99.2 → 99.0 (`-0.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-02_HERESY_PLUS1` | GC-02 (Czarny Rynek): heresy 0 → 1 | 91.1 → 🟢 ** 91.6** (`⬆️ +0.5`) | 87.1 → 85.9 (`-1.2`) | 86.9 → 90.2 (`⬆️ +3.3`) | 99.2 → 98.7 (`-0.5`) | ⚪ OPTYMALNY |
| `L3_CAA-09_COST_MINUS1` | CAA-09 (Kurier Relikwii): cost 2 → 1 | 91.1 → 🟢 ** 91.5** (`⬆️ +0.4`) | 87.1 → 85.5 (`-1.6`) | 86.9 → 90.3 (`⬆️ +3.4`) | 99.2 → 98.8 (`-0.4`) | ⚪ OPTYMALNY |
| `L3_CAA-08_COST_PLUS1` | CAA-08 (Kaptur Nocy): cost 1 → 2 | 91.1 → 🟢 ** 91.4** (`⬆️ +0.3`) | 87.1 → 85.4 (`-1.7`) | 86.9 → 90.7 (`⬆️ +3.8`) | 99.2 → 98.0 (`-1.2`) | ⚪ OPTYMALNY |
| `L3_SO-07_COST_PLUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 3 | 91.1 → 🟢 ** 91.3** (`⬆️ +0.2`) | 87.1 → 85.5 (`-1.6`) | 86.9 → 89.7 (`⬆️ +2.8`) | 99.2 → 98.8 (`-0.4`) | ⚪ OPTYMALNY |
| `L3_SO-06_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): heresy 0 → 1 | 91.1 → 🟢 ** 91.3** (`⬆️ +0.2`) | 87.1 → 86.0 (`-1.1`) | 86.9 → 88.6 (`⬆️ +1.7`) | 99.2 | ⚪ OPTYMALNY |
| `L3_KB-08_HERESY_PLUS1` | KB-08 (Przekupstwo Sędziego): heresy 0 → 1 | 91.1 → 🟢 ** 91.2** (`⬆️ +0.1`) | 87.1 → 87.5 (`⬆️ +0.4`) | 86.9 → 87.0 (`⬆️ +0.1`) | 99.2 | ⚪ OPTYMALNY |
| `L3_SO-09_COST_MINUS1` | SO-09 (Świadek Koronny): cost 2 → 1 | 🟢 ** 91.1** | 87.1 → 86.6 (`-0.5`) | 86.9 → 87.9 (`⬆️ +1.0`) | 99.2 → 98.9 (`-0.3`) | ⚪ OPTYMALNY |
| `L3_GC-09_HERESY_PLUS1` | GC-09 (Lista Dłużników): heresy 0 → 1 | 91.1 → 🟢 ** 91.0** (`-0.1`) | 87.1 → 84.2 (`-2.9`) | 86.9 → 90.0 (`⬆️ +3.1`) | 99.2 → 98.7 (`-0.5`) | ⚪ OPTYMALNY |
| `L3_GC-06_HERESY_PLUS1` | GC-06 (Szantaż): heresy 0 → 1 | 91.1 → 🟢 ** 91.0** (`-0.1`) | 87.1 → 85.4 (`-1.7`) | 86.9 → 88.3 (`⬆️ +1.4`) | 99.2 | ⚪ OPTYMALNY |
| `L3_SO-08_COST_PLUS1` | SO-08 (Nasłanie Inkwizytora): cost 2 → 3 | 91.1 → 🟢 ** 90.9** (`-0.2`) | 87.1 → 84.1 (`-3.0`) | 86.9 → 89.5 (`⬆️ +2.6`) | 99.2 | ⚪ OPTYMALNY |
| `L3_GC-04_COST_MINUS1` | GC-04 (Informator): cost 1 → 0 | 91.1 → 🟢 ** 90.9** (`-0.2`) | 87.1 → 87.7 (`⬆️ +0.6`) | 86.9 → 85.6 (`-1.3`) | 99.2 → 99.5 (`⬆️ +0.3`) | ⚪ OPTYMALNY |
| `L3_CAA-10_COST_MINUS1` | CAA-10 (Echo Alhambry): cost 1 → 0 | 91.1 → 🟢 ** 90.9** (`-0.2`) | 87.1 → 86.4 (`-0.7`) | 86.9 → 87.5 (`⬆️ +0.6`) | 99.2 → 98.7 (`-0.5`) | ⚪ OPTYMALNY |
| `L3_CAA-01_COST_MINUS1` | CAA-01 (Przejście Podziemiami): cost 1 → 0 | 91.1 → 🟢 ** 90.9** (`-0.2`) | 87.1 → 86.7 (`-0.4`) | 86.9 → 86.5 (`-0.4`) | 99.2 → 99.6 (`⬆️ +0.4`) | ⚪ OPTYMALNY |
| `L3_KT-10_COST_MINUS1` | KT-10 (Pieczęć Salomona): cost 1 → 0 | 91.1 → 🟢 ** 90.9** (`-0.2`) | 87.1 → 86.9 (`-0.2`) | 86.9 → 87.0 (`⬆️ +0.1`) | 99.2 → 98.9 (`-0.3`) | ⚪ OPTYMALNY |
| `L3_GC-01_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): heresy 0 → 1 | 91.1 → 🟢 ** 90.8** (`-0.3`) | 87.1 → 85.2 (`-1.9`) | 86.9 → 88.2 (`⬆️ +1.3`) | 99.2 → 99.1 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_GC-09_COST_PLUS1` | GC-09 (Lista Dłużników): cost 2 → 3 | 91.1 → 🟢 ** 90.8** (`-0.3`) | 87.1 → 85.4 (`-1.7`) | 86.9 → 88.1 (`⬆️ +1.2`) | 99.2 → 98.9 (`-0.3`) | ⚪ OPTYMALNY |
| `L3_KT-03_HERESY_MINUS1` | KT-03 (Zakazana Wiedza): heresy 1 → 0 | 91.1 → 🟢 ** 90.8** (`-0.3`) | 87.1 → 86.1 (`-1.0`) | 86.9 → 86.8 (`-0.1`) | 99.2 → 99.6 (`⬆️ +0.4`) | ⚪ OPTYMALNY |
| `L3_KT-04_COST_MINUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 0 | 91.1 → 🟢 ** 90.8** (`-0.3`) | 87.1 → 87.2 (`⬆️ +0.1`) | 86.9 → 86.8 (`-0.1`) | 99.2 → 98.5 (`-0.7`) | ⚪ OPTYMALNY |
| `L3_CAA-07_HERESY_PLUS1` | CAA-07 (Szantaż Bractwa): heresy 0 → 1 | 91.1 → 🟢 ** 90.7** (`-0.4`) | 87.1 → 88.0 (`⬆️ +0.9`) | 86.9 → 84.2 (`-2.7`) | 99.2 → 99.8 (`⬆️ +0.6`) | ⚪ OPTYMALNY |
| `L3_GC-01_COST_PLUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 2 | 91.1 → 🟢 ** 90.7** (`-0.4`) | 87.1 → 87.6 (`⬆️ +0.5`) | 86.9 → 85.7 (`-1.2`) | 99.2 → 98.8 (`-0.4`) | ⚪ OPTYMALNY |
| `L3_KT-07_COST_MINUS1` | KT-07 (Archiwum Ukryte): cost 1 → 0 | 91.1 → 🟢 ** 90.7** (`-0.4`) | 87.1 → 86.5 (`-0.6`) | 86.9 → 87.2 (`⬆️ +0.3`) | 99.2 → 98.3 (`-0.9`) | ⚪ OPTYMALNY |
| `L3_CAA-06_HERESY_PLUS1` | CAA-06 (Ucieczka z Lochów): heresy 0 → 1 | 91.1 → 🟢 ** 90.7** (`-0.4`) | 87.1 → 86.2 (`-0.9`) | 86.9 → 86.6 (`-0.3`) | 99.2 → 99.3 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_GC-07_HERESY_PLUS1` | GC-07 (Skrytobójstwo): heresy 1 → 2 | 91.1 → 🟢 ** 90.7** (`-0.4`) | 87.1 → 86.1 (`-1.0`) | 86.9 → 87.0 (`⬆️ +0.1`) | 99.2 → 99.1 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_KB-05_HERESY_PLUS1` | KB-05 (List Żelazny): heresy 0 → 1 | 91.1 → 🟢 ** 90.7** (`-0.4`) | 87.1 | 86.9 → 85.6 (`-1.3`) | 99.2 → 99.3 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_CAA-06_COST_MINUS1` | CAA-06 (Ucieczka z Lochów): cost 2 → 1 | 91.1 → 🟢 ** 90.6** (`-0.5`) | 87.1 → 83.7 (`-3.4`) | 86.9 → 88.9 (`⬆️ +2.0`) | 99.2 → 99.1 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_KT-06_COST_MINUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 1 | 91.1 → 🟢 ** 90.5** (`-0.6`) | 87.1 → 86.9 (`-0.2`) | 86.9 → 85.2 (`-1.7`) | 99.2 → 99.3 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_HERESY_PLUS1` | GC-04 (Informator): heresy 1 → 2 | 91.1 → 🟢 ** 90.4** (`-0.7`) | 87.1 → 84.6 (`-2.5`) | 86.9 → 87.8 (`⬆️ +0.9`) | 99.2 → 98.9 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_HERESY_MINUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 0 | 91.1 → 🟢 ** 90.4** (`-0.7`) | 87.1 → 86.6 (`-0.5`) | 86.9 → 85.0 (`-1.9`) | 99.2 → 99.5 (`⬆️ +0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_COST_PLUS1` | GC-02 (Czarny Rynek): cost 1 → 2 | 91.1 → 🟢 ** 90.3** (`-0.8`) | 87.1 → 81.4 (`-5.7`) | 86.9 → 91.3 (`⬆️ +4.4`) | 99.2 → 98.1 (`-1.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_HERESY_PLUS1` | KB-06 (Areszt Królewski): heresy 0 → 1 | 91.1 → 🟢 ** 90.3** (`-0.8`) | 87.1 → 86.5 (`-0.6`) | 86.9 → 85.1 (`-1.8`) | 99.2 → 99.3 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 0 → 1 | 91.1 → 🟢 ** 90.2** (`-0.9`) | 87.1 → 83.9 (`-3.2`) | 86.9 → 87.5 (`⬆️ +0.6`) | 99.2 → 99.3 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_HERESY_PLUS1` | KB-04 (Faworyt Dworu): heresy 1 → 2 | 91.1 → 🟢 ** 90.2** (`-0.9`) | 87.1 → 87.5 (`⬆️ +0.4`) | 86.9 → 85.9 (`-1.0`) | 99.2 → 97.3 (`-1.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 91.1 → 🟢 ** 90.1** (`-1.0`) | 87.1 → 82.5 (`-4.6`) | 86.9 → 88.6 (`⬆️ +1.7`) | 99.2 | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_COST_PLUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 2 | 91.1 → 🟢 ** 90.1** (`-1.0`) | 87.1 → 87.2 (`⬆️ +0.1`) | 86.9 → 84.1 (`-2.8`) | 99.2 → 98.9 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_HERESY_PLUS1` | KB-01 (Rozkaz Dworu): heresy 0 → 1 | 91.1 → 🟢 ** 89.9** (`-1.2`) | 87.1 → 87.5 (`⬆️ +0.4`) | 86.9 → 83.1 (`-3.8`) | 99.2 → 99.0 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_HERESY_PLUS1` | SO-09 (Świadek Koronny): heresy 0 → 1 | 91.1 → 🟢 ** 89.9** (`-1.2`) | 87.1 → 86.1 (`-1.0`) | 86.9 → 84.3 (`-2.6`) | 99.2 → 99.3 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_COST_MINUS1` | GC-09 (Lista Dłużników): cost 2 → 1 | 91.1 → 🟢 ** 89.7** (`-1.4`) | 87.1 → 88.3 (`⬆️ +1.2`) | 86.9 → 82.4 (`-4.5`) | 99.2 → 98.3 (`-0.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 2 → 3 | 91.1 → 🟢 ** 89.7** (`-1.4`) | 87.1 → 86.9 (`-0.2`) | 86.9 → 82.8 (`-4.1`) | 99.2 → 99.3 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_COST_MINUS1` | KT-09 (Fragment Kodeksu): cost 1 → 0 | 91.1 → 🟢 ** 89.5** (`-1.6`) | 87.1 → 87.2 (`⬆️ +0.1`) | 86.9 → 83.3 (`-3.6`) | 99.2 → 98.1 (`-1.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_COST_MINUS1` | CAA-08 (Kaptur Nocy): cost 1 → 0 | 91.1 → 🟢 ** 89.4** (`-1.7`) | 87.1 | 86.9 → 81.7 (`-5.2`) | 99.2 → 99.5 (`⬆️ +0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_COST_MINUS1` | SO-10 (Oczyść Miasto): cost 4 → 3 | 91.1 → 🟢 ** 89.3** (`-1.8`) | 87.1 → 83.5 (`-3.6`) | 86.9 → 88.8 (`⬆️ +1.9`) | 99.2 → 95.7 (`-3.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_HERESY_MINUS1` | SO-08 (Nasłanie Inkwizytora): heresy 1 → 0 | 91.1 → 🟢 ** 89.2** (`-1.9`) | 87.1 → 81.8 (`-5.3`) | 86.9 → 86.2 (`-0.7`) | 99.2 → 99.6 (`⬆️ +0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_COST_MINUS1` | GC-07 (Skrytobójstwo): cost 2 → 1 | 91.1 → 🟢 ** 89.0** (`-2.1`) | 87.1 → 88.1 (`⬆️ +1.0`) | 86.9 → 80.7 (`-6.2`) | 99.2 → 98.2 (`-1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 91.1 → 🟢 ** 89.0** (`-2.1`) | 87.1 → 85.6 (`-1.5`) | 86.9 → 81.9 (`-5.0`) | 99.2 → 99.5 (`⬆️ +0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_COST_PLUS1` | SO-09 (Świadek Koronny): cost 2 → 3 | 91.1 → 🟢 ** 88.8** (`-2.3`) | 87.1 → 86.0 (`-1.1`) | 86.9 → 92.1 (`⬆️ +5.2`) | 99.2 → 88.3 (`-10.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-04_COST_PLUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 2 | 91.1 → 🟢 ** 88.7** (`-2.4`) | 87.1 → 84.6 (`-2.5`) | 86.9 → 81.8 (`-5.1`) | 99.2 → 99.6 (`⬆️ +0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_HERESY_PLUS1` | KT-05 (Wskazówka Cyklu): heresy 0 → 1 | 91.1 → 🟢 ** 88.7** (`-2.4`) | 87.1 → 81.8 (`-5.3`) | 86.9 → 85.0 (`-1.9`) | 99.2 → 99.3 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_COST_PLUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 2 | 91.1 → 🟢 ** 88.3** (`-2.8`) | 87.1 → 87.2 (`⬆️ +0.1`) | 86.9 → 79.7 (`-7.2`) | 99.2 → 97.9 (`-1.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_HERESY_MINUS1` | CAA-10 (Echo Alhambry): heresy 1 → 0 | 91.1 → 🟢 ** 88.2** (`-2.9`) | 87.1 → 77.8 (`-9.3`) | 86.9 → 88.2 (`⬆️ +1.3`) | 99.2 → 98.5 (`-0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_COST_MINUS1` | GC-02 (Czarny Rynek): cost 1 → 0 | 91.1 → 🟢 ** 87.8** (`-3.3`) | 87.1 → 87.7 (`⬆️ +0.6`) | 86.9 → 76.9 (`-10.0`) | 99.2 → 98.8 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-03_COST_MINUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 0 | 91.1 → 🟢 ** 87.7** (`-3.4`) | 87.1 → 88.4 (`⬆️ +1.3`) | 86.9 → 76.2 (`-10.7`) | 99.2 → 98.5 (`-0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_COST_PLUS1` | KT-08 (Areszt Wiedzy): cost 2 → 3 | 91.1 → 🟢 ** 87.7** (`-3.4`) | 87.1 → 84.6 (`-2.5`) | 86.9 → 79.0 (`-7.9`) | 99.2 → 99.4 (`⬆️ +0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_HERESY_PLUS1` | SO-01 (Patrol Familiariuszy): heresy 0 → 1 | 91.1 → 🟢 ** 87.7** (`-3.4`) | 87.1 → 83.8 (`-3.3`) | 86.9 → 80.1 (`-6.8`) | 99.2 → 99.3 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_COST_PLUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 2 | 91.1 → 🟢 ** 87.6** (`-3.5`) | 87.1 → 79.0 (`-8.1`) | 86.9 → 84.1 (`-2.8`) | 99.2 → 99.6 (`⬆️ +0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_COST_PLUS1` | GC-06 (Szantaż): cost 2 → 3 | 91.1 → 🟢 ** 87.5** (`-3.6`) | 87.1 → 77.3 (`-9.8`) | 86.9 → 87.2 (`⬆️ +0.3`) | 99.2 → 98.1 (`-1.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_COST_MINUS1` | GC-10 (Upadek Domu): cost 3 → 2 | 91.1 → 🟢 ** 87.4** (`-3.7`) | 87.1 → 87.2 (`⬆️ +0.1`) | 86.9 → 76.0 (`-10.9`) | 99.2 → 99.1 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_COST_MINUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 0 | 91.1 → 🟢 ** 87.2** (`-3.9`) | 87.1 → 87.5 (`⬆️ +0.4`) | 86.9 → 75.4 (`-11.5`) | 99.2 → 98.7 (`-0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_COST_PLUS1` | GC-07 (Skrytobójstwo): cost 2 → 3 | 91.1 → 🟢 ** 87.0** (`-4.1`) | 87.1 → 87.3 (`⬆️ +0.2`) | 86.9 → 74.9 (`-12.0`) | 99.2 → 98.9 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_HERESY_PLUS1` | SO-03 (Podejrzenie): heresy 0 → 1 | 91.1 → 🟢 ** 86.8** (`-4.3`) | 87.1 → 81.4 (`-5.7`) | 86.9 → 79.8 (`-7.1`) | 99.2 → 99.3 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_COST_MINUS1` | GC-08 (Zatrute Złoto): cost 1 → 0 | 91.1 → 🟢 ** 86.5** (`-4.6`) | 87.1 → 88.0 (`⬆️ +0.9`) | 86.9 → 72.3 (`-14.6`) | 99.2 → 99.1 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_HERESY_PLUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 2 | 91.1 → 🟢 ** 86.0** (`-5.1`) | 87.1 → 72.5 (`-14.6`) | 86.9 → 86.0 (`-0.9`) | 99.2 → 99.5 (`⬆️ +0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_COST_PLUS1` | KB-02 (Pobór Podatków): cost 1 → 2 | 91.1 → 🟢 ** 85.3** (`-5.8`) | 87.1 → 93.5 (`⬆️ +6.4`) | 86.9 → 77.1 (`-9.8`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_HERESY_PLUS1` | KT-03 (Zakazana Wiedza): heresy 1 → 2 | 91.1 → 🟢 ** 85.0** (`-6.1`) | 87.1 → 72.3 (`-14.8`) | 86.9 → 83.0 (`-3.9`) | 99.2 → 99.6 (`⬆️ +0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_COST_MINUS1` | GC-06 (Szantaż): cost 2 → 1 | 91.1 → 🟢 ** 84.8** (`-6.3`) | 87.1 → 87.5 (`⬆️ +0.4`) | 86.9 → 69.0 (`-17.9`) | 99.2 → 97.8 (`-1.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_HERESY_PLUS1` | KB-02 (Pobór Podatków): heresy 0 → 1 | 91.1 → 🟢 ** 84.1** (`-7.0`) | 87.1 → 88.6 (`⬆️ +1.5`) | 86.9 → 84.8 (`-2.1`) | 99.2 → 78.8 (`-20.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_COST_PLUS1` | KB-10 (Pieczęć Korony): cost 2 → 3 | 91.1 → 🟢 ** 81.7** (`-9.4`) | 87.1 → 88.5 (`⬆️ +1.4`) | 86.9 → 74.9 (`-12.0`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_HERESY_PLUS1` | KT-06 (Przesłuchanie Imienia): heresy 0 → 1 | 91.1 → 🟢 ** 81.0** (`-10.1`) | 87.1 → 64.2 (`-22.9`) | 86.9 → 79.4 (`-7.5`) | 99.2 → 99.5 (`⬆️ +0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_COST_PLUS1` | KB-06 (Areszt Królewski): cost 2 → 3 | 91.1 → 🟢 ** 80.7** (`-10.4`) | 87.1 → 63.2 (`-23.9`) | 86.9 → 79.3 (`-7.6`) | 99.2 → 99.5 (`⬆️ +0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_COST_PLUS1` | KB-05 (List Żelazny): cost 2 → 3 | 91.1 → 🟢 ** 72.3** (`-18.8`) | 87.1 → 94.9 (`⬆️ +7.8`) | 86.9 → 89.2 (`⬆️ +2.3`) | 99.2 → 32.7 (`-66.5`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 86 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_GC-05_COST_PLUS1` | GC-05 (Fałszywy Świadek): cost 0 → 1 | 🟢 ** 91.1** | 87.1 | 86.9 | 99.2 | ⚪ OPTYMALNY |
| `L3_GC-05_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): heresy 0 → 1 | 🟢 ** 91.1** | 87.1 | 86.9 | 99.2 | ⚪ OPTYMALNY |
| `L3_SO-05_COST_PLUS1` | SO-05 (Wezwanie do Trybunału): cost 0 → 1 | 🟢 ** 91.1** | 87.1 | 86.9 | 99.2 | ⚪ OPTYMALNY |
| `L3_SO-05_HERESY_PLUS1` | SO-05 (Wezwanie do Trybunału): heresy 0 → 1 | 🟢 ** 91.1** | 87.1 | 86.9 | 99.2 | ⚪ OPTYMALNY |
| `L3_KT-02_COST_MINUS1` | KT-02 (Transmutacja Złota): cost 1 → 0 | 91.1 → 🟢 ** 90.8** (`-0.3`) | 87.1 → 86.7 (`-0.4`) | 86.9 → 86.4 (`-0.5`) | 99.2 | ⚪ OPTYMALNY |
| `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 91.1 → 🟢 ** 90.4** (`-0.7`) | 87.1 → 85.8 (`-1.3`) | 86.9 → 86.1 (`-0.8`) | 99.2 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_HERESY_PLUS1` | KB-03 (Plotka Dworska): heresy 0 → 1 | 91.1 → 🟢 ** 90.3** (`-0.8`) | 87.1 → 86.6 (`-0.5`) | 86.9 → 85.7 (`-1.2`) | 99.2 → 98.7 (`-0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_COST_PLUS1` | KT-07 (Archiwum Ukryte): cost 1 → 2 | 91.1 → 🟢 ** 90.3** (`-0.8`) | 87.1 → 85.7 (`-1.4`) | 86.9 → 86.0 (`-0.9`) | 99.2 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_COST_MINUS1` | KT-08 (Areszt Wiedzy): cost 2 → 1 | 91.1 → 🟢 ** 90.3** (`-0.8`) | 87.1 → 86.4 (`-0.7`) | 86.9 → 85.6 (`-1.3`) | 99.2 → 98.8 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_COST_MINUS1` | CAA-02 (Złoto z Kryjówki): cost 1 → 0 | 91.1 → 🟢 ** 90.2** (`-0.9`) | 87.1 → 86.4 (`-0.7`) | 86.9 → 85.0 (`-1.9`) | 99.2 → 99.1 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_COST_MINUS1` | CAA-04 (Fałszywy Trop): cost 1 → 0 | 91.1 → 🟢 ** 90.2** (`-0.9`) | 87.1 → 86.1 (`-1.0`) | 86.9 → 85.6 (`-1.3`) | 99.2 → 99.0 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_COST_MINUS1` | SO-03 (Podejrzenie): cost 1 → 0 | 91.1 → 🟢 ** 90.2** (`-0.9`) | 87.1 → 86.6 (`-0.5`) | 86.9 → 85.8 (`-1.1`) | 99.2 → 98.2 (`-1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_HERESY_MINUS1` | GC-07 (Skrytobójstwo): heresy 1 → 0 | 91.1 → 🟢 ** 90.1** (`-1.0`) | 87.1 | 86.9 → 84.4 (`-2.5`) | 99.2 → 98.8 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_COST_MINUS1` | KT-01 (Rytuał Przejścia): cost 1 → 0 | 91.1 → 🟢 ** 90.1** (`-1.0`) | 87.1 → 86.5 (`-0.6`) | 86.9 → 85.2 (`-1.7`) | 99.2 → 98.6 (`-0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-07_COST_MINUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 1 | 91.1 → 🟢 ** 90.1** (`-1.0`) | 87.1 → 85.8 (`-1.3`) | 86.9 → 85.9 (`-1.0`) | 99.2 → 98.5 (`-0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_COST_PLUS1` | GC-04 (Informator): cost 1 → 2 | 91.1 → 🟢 ** 89.9** (`-1.2`) | 87.1 → 86.5 (`-0.6`) | 86.9 → 84.8 (`-2.1`) | 99.2 → 98.3 (`-0.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_COST_PLUS1` | KB-08 (Przekupstwo Sędziego): cost 3 → 4 | 91.1 → 🟢 ** 89.9** (`-1.2`) | 87.1 → 85.7 (`-1.4`) | 86.9 → 85.2 (`-1.7`) | 99.2 → 98.8 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_COST_PLUS1` | SO-06 (Areszt Trybunalski): cost 2 → 3 | 91.1 → 🟢 ** 89.9** (`-1.2`) | 87.1 → 86.8 (`-0.3`) | 86.9 → 84.4 (`-2.5`) | 99.2 → 98.4 (`-0.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-01_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 91.1 → 🟢 ** 89.8** (`-1.3`) | 87.1 → 86.7 (`-0.4`) | 86.9 → 83.6 (`-3.3`) | 99.2 → 99.0 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_COST_MINUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 0 | 91.1 → 🟢 ** 89.7** (`-1.4`) | 87.1 → 86.1 (`-1.0`) | 86.9 → 84.2 (`-2.7`) | 99.2 → 98.8 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_HERESY_PLUS1` | CAA-04 (Fałszywy Trop): heresy 0 → 1 | 91.1 → 🟢 ** 89.5** (`-1.6`) | 87.1 → 87.0 (`-0.1`) | 86.9 → 82.6 (`-4.3`) | 99.2 → 99.0 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_HERESY_MINUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 0 | 91.1 → 🟢 ** 89.5** (`-1.6`) | 87.1 → 84.0 (`-3.1`) | 86.9 → 85.4 (`-1.5`) | 99.2 → 99.1 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_COST_MINUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 0 | 91.1 → 🟢 ** 89.5** (`-1.6`) | 87.1 | 86.9 → 83.4 (`-3.5`) | 99.2 → 98.0 (`-1.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-07_HERESY_PLUS1` | SO-07 (Przesłuchanie Oficjum): heresy 0 → 1 | 91.1 → 🟢 ** 89.5** (`-1.6`) | 87.1 → 85.4 (`-1.7`) | 86.9 → 84.0 (`-2.9`) | 99.2 → 99.1 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_HERESY_PLUS1` | CAA-05 (Ukryty Kurier): heresy 0 → 1 | 91.1 → 🟢 ** 89.3** (`-1.8`) | 87.1 → 84.4 (`-2.7`) | 86.9 → 84.7 (`-2.2`) | 99.2 → 98.8 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_COST_PLUS1` | KT-10 (Pieczęć Salomona): cost 1 → 2 | 91.1 → 🟢 ** 89.1** (`-2.0`) | 87.1 → 83.9 (`-3.2`) | 86.9 → 84.6 (`-2.3`) | 99.2 → 98.8 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_COST_MINUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 0 | 91.1 → 🟢 ** 89.1** (`-2.0`) | 87.1 → 86.3 (`-0.8`) | 86.9 → 83.4 (`-3.5`) | 99.2 → 97.7 (`-1.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_COST_PLUS1` | SO-03 (Podejrzenie): cost 1 → 2 | 91.1 → 🟢 ** 89.1** (`-2.0`) | 87.1 → 82.5 (`-4.6`) | 86.9 → 86.0 (`-0.9`) | 99.2 → 98.8 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_COST_PLUS1` | KT-03 (Zakazana Wiedza): cost 0 → 1 | 91.1 → 🟢 ** 89.0** (`-2.1`) | 87.1 → 85.8 (`-1.3`) | 86.9 → 81.9 (`-5.0`) | 99.2 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_HERESY_PLUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 2 | 91.1 → 🟢 ** 88.7** (`-2.4`) | 87.1 → 85.2 (`-1.9`) | 86.9 → 81.9 (`-5.0`) | 99.2 → 99.1 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_HERESY_PLUS1` | KT-02 (Transmutacja Złota): heresy 0 → 1 | 91.1 → 🟢 ** 88.7** (`-2.4`) | 87.1 → 81.9 (`-5.2`) | 86.9 → 85.0 (`-1.9`) | 99.2 → 99.1 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_HERESY_PLUS1` | CAA-03 (Cień na Rynku): heresy 1 → 2 | 91.1 → 🟢 ** 88.4** (`-2.7`) | 87.1 → 85.5 (`-1.6`) | 86.9 → 81.1 (`-5.8`) | 99.2 → 98.7 (`-0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 91.1 → 🟢 ** 88.4** (`-2.7`) | 87.1 → 82.2 (`-4.9`) | 86.9 → 84.0 (`-2.9`) | 99.2 → 98.9 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-03_COST_PLUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 2 | 91.1 → 🟢 ** 88.4** (`-2.7`) | 87.1 → 85.3 (`-1.8`) | 86.9 → 81.8 (`-5.1`) | 99.2 → 98.0 (`-1.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_COST_MINUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 0 | 91.1 → 🟢 ** 88.4** (`-2.7`) | 87.1 → 86.5 (`-0.6`) | 86.9 → 80.7 (`-6.2`) | 99.2 → 98.1 (`-1.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_COST_MINUS1` | SO-08 (Nasłanie Inkwizytora): cost 2 → 1 | 91.1 → 🟢 ** 88.3** (`-2.8`) | 87.1 → 85.7 (`-1.4`) | 86.9 → 80.5 (`-6.4`) | 99.2 → 98.8 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_COST_PLUS1` | KB-04 (Faworyt Dworu): cost 1 → 2 | 91.1 → 🟢 ** 88.1** (`-3.0`) | 87.1 → 83.7 (`-3.4`) | 86.9 → 83.7 (`-3.2`) | 99.2 → 96.8 (`-2.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_COST_PLUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 3 | 91.1 → 🟢 ** 88.1** (`-3.0`) | 87.1 → 83.1 (`-4.0`) | 86.9 → 82.0 (`-4.9`) | 99.2 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 1 → 2 | 91.1 → 🟢 ** 88.1** (`-3.0`) | 87.1 → 79.1 (`-8.0`) | 86.9 → 86.6 (`-0.3`) | 99.2 → 98.5 (`-0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_HERESY_PLUS1` | CAA-02 (Złoto z Kryjówki): heresy 0 → 1 | 91.1 → 🟢 ** 88.0** (`-3.1`) | 87.1 → 84.2 (`-2.9`) | 86.9 → 80.6 (`-6.3`) | 99.2 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_HERESY_PLUS1` | KT-07 (Archiwum Ukryte): heresy 0 → 1 | 91.1 → 🟢 ** 87.9** (`-3.2`) | 87.1 → 81.4 (`-5.7`) | 86.9 → 83.0 (`-3.9`) | 99.2 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_HERESY_PLUS1` | KB-07 (Szantaż Pieczęcią): heresy 0 → 1 | 91.1 → 🟢 ** 87.8** (`-3.3`) | 87.1 → 84.3 (`-2.8`) | 86.9 → 80.2 (`-6.7`) | 99.2 → 98.9 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_HERESY_PLUS1` | KT-01 (Rytuał Przejścia): heresy 0 → 1 | 91.1 → 🟢 ** 87.8** (`-3.3`) | 87.1 → 80.6 (`-6.5`) | 86.9 → 83.7 (`-3.2`) | 99.2 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_COST_MINUS1` | CAA-07 (Szantaż Bractwa): cost 2 → 1 | 91.1 → 🟢 ** 87.7** (`-3.4`) | 87.1 → 78.4 (`-8.7`) | 86.9 → 85.9 (`-1.0`) | 99.2 → 98.8 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_HERESY_PLUS1` | SO-10 (Oczyść Miasto): heresy 2 → 3 | 91.1 → 🟢 ** 87.5** (`-3.6`) | 87.1 → 84.7 (`-2.4`) | 86.9 → 79.0 (`-7.9`) | 99.2 → 98.8 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_HERESY_MINUS1` | GC-04 (Informator): heresy 1 → 0 | 91.1 → 🟢 ** 87.4** (`-3.7`) | 87.1 → 87.0 (`-0.1`) | 86.9 → 76.6 (`-10.3`) | 99.2 → 98.5 (`-0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_HERESY_PLUS1` | KT-08 (Areszt Wiedzy): heresy 0 → 1 | 91.1 → 🟢 ** 87.2** (`-3.9`) | 87.1 → 81.3 (`-5.8`) | 86.9 → 81.1 (`-5.8`) | 99.2 → 99.1 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_HERESY_PLUS1` | SO-08 (Nasłanie Inkwizytora): heresy 1 → 2 | 91.1 → 🟢 ** 87.0** (`-4.1`) | 87.1 → 82.1 (`-5.0`) | 86.9 → 80.0 (`-6.9`) | 99.2 → 99.0 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-04_HERESY_PLUS1` | KT-04 (Zwierciadło Herezji): heresy 0 → 1 | 91.1 → 🟢 ** 86.2** (`-4.9`) | 87.1 → 82.4 (`-4.7`) | 86.9 → 77.2 (`-9.7`) | 99.2 → 99.1 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_HERESY_PLUS1` | SO-04 (Publiczne Ostrzeżenie): heresy 0 → 1 | 91.1 → 🟢 ** 86.0** (`-5.1`) | 87.1 → 80.2 (`-6.9`) | 86.9 → 78.7 (`-8.2`) | 99.2 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_COST_PLUS1` | CAA-06 (Ucieczka z Lochów): cost 2 → 3 | 91.1 → 🟢 ** 85.8** (`-5.3`) | 87.1 → 83.8 (`-3.3`) | 86.9 → 76.8 (`-10.1`) | 99.2 → 96.8 (`-2.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): heresy 0 → 1 | 91.1 → 🟢 ** 85.8** (`-5.3`) | 87.1 → 81.7 (`-5.4`) | 86.9 → 76.6 (`-10.3`) | 99.2 → 99.1 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 1 → 2 | 91.1 → 🟢 ** 85.2** (`-5.9`) | 87.1 → 83.3 (`-3.8`) | 86.9 → 74.5 (`-12.4`) | 99.2 → 97.9 (`-1.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_HERESY_MINUS1` | SO-10 (Oczyść Miasto): heresy 2 → 1 | 91.1 → 🟢 ** 85.2** (`-5.9`) | 87.1 → 80.2 (`-6.9`) | 86.9 → 76.4 (`-10.5`) | 99.2 → 99.1 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_COST_MINUS1` | KB-06 (Areszt Królewski): cost 2 → 1 | 91.1 → 🟢 ** 85.1** (`-6.0`) | 87.1 → 85.8 (`-1.3`) | 86.9 → 85.5 (`-1.4`) | 99.2 → 83.9 (`-15.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_COST_PLUS1` | CAA-09 (Kurier Relikwii): cost 2 → 3 | 91.1 → 🟢 ** 85.0** (`-6.1`) | 87.1 → 84.3 (`-2.8`) | 86.9 → 73.0 (`-13.9`) | 99.2 → 97.8 (`-1.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_COST_PLUS1` | CAA-04 (Fałszywy Trop): cost 1 → 2 | 91.1 → 🟢 ** 84.8** (`-6.3`) | 87.1 → 82.5 (`-4.6`) | 86.9 → 73.3 (`-13.6`) | 99.2 → 98.6 (`-0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_COST_PLUS1` | GC-10 (Upadek Domu): cost 3 → 4 | 91.1 → 🟢 ** 84.8** (`-6.3`) | 87.1 → 81.0 (`-6.1`) | 86.9 → 86.1 (`-0.8`) | 99.2 → 87.3 (`-11.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 1 → 2 | 91.1 → 🟢 ** 84.3** (`-6.8`) | 87.1 → 83.8 (`-3.3`) | 86.9 → 84.3 (`-2.6`) | 99.2 → 84.7 (`-14.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_HERESY_MINUS1` | KB-04 (Faworyt Dworu): heresy 1 → 0 | 91.1 → 🟢 ** 83.5** (`-7.6`) | 87.1 → 81.5 (`-5.6`) | 86.9 → 83.7 (`-3.2`) | 99.2 → 85.2 (`-14.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_COST_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 2 | 91.1 → 🟢 ** 83.3** (`-7.8`) | 87.1 → 79.4 (`-7.7`) | 86.9 → 72.2 (`-14.7`) | 99.2 → 98.2 (`-1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_HERESY_MINUS1` | KB-09 (Dekret Królewski): heresy 1 → 0 | 91.1 → 🟢 ** 81.8** (`-9.3`) | 87.1 → 67.6 (`-19.5`) | 86.9 → 79.9 (`-7.0`) | 99.2 → 98.0 (`-1.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 1 → 2 | 91.1 → 🟢 ** 81.5** (`-9.6`) | 87.1 → 75.9 (`-11.2`) | 86.9 → 71.3 (`-15.6`) | 99.2 → 97.3 (`-1.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_HERESY_MINUS1` | GC-10 (Upadek Domu): heresy 2 → 1 | 91.1 → 🟢 ** 80.4** (`-10.7`) | 87.1 → 83.8 (`-3.3`) | 86.9 → 69.8 (`-17.1`) | 99.2 → 87.7 (`-11.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_COST_PLUS1` | SO-10 (Oczyść Miasto): cost 4 → 5 | 91.1 → 🟢 ** 78.8** (`-12.3`) | 87.1 → 76.6 (`-10.5`) | 86.9 → 62.3 (`-24.6`) | 99.2 → 97.5 (`-1.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_HERESY_PLUS1` | KT-10 (Pieczęć Salomona): heresy 0 → 1 | 91.1 → 🟢 ** 78.2** (`-12.9`) | 87.1 → 61.2 (`-25.9`) | 86.9 → 74.7 (`-12.2`) | 99.2 → 98.6 (`-0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_HERESY_PLUS1` | CAA-09 (Kurier Relikwii): heresy 0 → 1 | 91.1 → 🟢 ** 77.9** (`-13.2`) | 87.1 → 72.8 (`-14.3`) | 86.9 → 63.7 (`-23.2`) | 99.2 → 97.1 (`-2.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_COST_PLUS1` | KB-01 (Rozkaz Dworu): cost 1 → 2 | 91.1 → 🟢 ** 77.2** (`-13.9`) | 87.1 → 56.6 (`-30.5`) | 86.9 → 77.0 (`-9.9`) | 99.2 → 98.1 (`-1.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_COST_PLUS1` | CAA-03 (Cień na Rynku): cost 1 → 2 | 91.1 → 🟢 ** 76.7** (`-14.4`) | 87.1 → 73.6 (`-13.5`) | 86.9 → 70.2 (`-16.7`) | 99.2 → 86.4 (`-12.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_COST_PLUS1` | KB-03 (Plotka Dworska): cost 1 → 2 | 91.1 → 🟢 ** 76.3** (`-14.8`) | 87.1 → 62.4 (`-24.7`) | 86.9 → 79.6 (`-7.3`) | 99.2 → 87.0 (`-12.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_HERESY_PLUS1` | KB-09 (Dekret Królewski): heresy 1 → 2 | 91.1 → 🟢 ** 72.0** (`-19.1`) | 87.1 → 86.7 (`-0.4`) | 86.9 → 57.3 (`-29.6`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_HERESY_PLUS1` | GC-10 (Upadek Domu): heresy 2 → 3 | 91.1 → 🟢 ** 69.1** (`-22.0`) | 87.1 → 64.8 (`-22.3`) | 86.9 → 79.2 (`-7.7`) | 99.2 → 63.3 (`-35.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_COST_MINUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 1 | 91.1 → 🟢 ** 69.1** (`-22.0`) | 87.1 → 56.8 (`-30.3`) | 86.9 → 64.5 (`-22.4`) | 99.2 → 86.0 (`-13.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_COST_MINUS1` | KB-04 (Faworyt Dworu): cost 1 → 0 | 91.1 → 🟢 ** 67.4** (`-23.7`) | 87.1 → 56.9 (`-30.2`) | 86.9 → 48.4 (`-38.5`) | 99.2 → 96.9 (`-2.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_COST_PLUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 3 | 91.1 → 🟢 ** 66.8** (`-24.3`) | 87.1 → 56.3 (`-30.8`) | 86.9 → 46.2 (`-40.7`) | 99.2 → 97.8 (`-1.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_HERESY_PLUS1` | KB-10 (Pieczęć Korony): heresy 2 → 3 | 91.1 → 🟢 ** 66.7** (`-24.4`) | 87.1 → 80.5 (`-6.6`) | 86.9 → 65.2 (`-21.7`) | 99.2 → 54.5 (`-44.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_HERESY_PLUS1` | CAA-10 (Echo Alhambry): heresy 1 → 2 | 91.1 → 🟢 ** 65.9** (`-25.2`) | 87.1 → 65.0 (`-22.1`) | 86.9 → 66.7 (`-20.2`) | 99.2 → 66.0 (`-33.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_COST_MINUS1` | KB-01 (Rozkaz Dworu): cost 1 → 0 | 91.1 → 🟢 ** 65.1** (`-26.0`) | 87.1 → 55.8 (`-31.3`) | 86.9 → 52.6 (`-34.3`) | 99.2 → 86.8 (`-12.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_COST_MINUS1` | KB-03 (Plotka Dworska): cost 1 → 0 | 91.1 → 🟢 ** 63.4** (`-27.7`) | 87.1 → 56.9 (`-30.2`) | 86.9 → 49.4 (`-37.5`) | 99.2 → 84.0 (`-15.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_HERESY_MINUS1` | KB-10 (Pieczęć Korony): heresy 2 → 1 | 91.1 → 🟢 ** 58.9** (`-32.2`) | 87.1 → 50.0 (`-37.1`) | 86.9 → 53.4 (`-33.5`) | 99.2 → 73.2 (`-26.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_COST_MINUS1` | KB-05 (List Żelazny): cost 2 → 1 | 91.1 → 🟢 ** 57.7** (`-33.4`) | 87.1 → 47.7 (`-39.4`) | 86.9 → 39.4 (`-47.5`) | 99.2 → 86.1 (`-13.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_COST_PLUS1` | CAA-10 (Echo Alhambry): cost 1 → 2 | 91.1 → 🟢 ** 54.0** (`-37.1`) | 87.1 → 53.7 (`-33.4`) | 86.9 → 46.0 (`-40.9`) | 99.2 → 62.2 (`-37.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_COST_MINUS1` | KB-02 (Pobór Podatków): cost 1 → 0 | 91.1 → 🟢 ** 52.8** (`-38.3`) | 87.1 → 54.1 (`-33.0`) | 86.9 → 45.8 (`-41.1`) | 99.2 → 58.5 (`-40.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_COST_MINUS1` | KB-10 (Pieczęć Korony): cost 2 → 1 | 91.1 → 🟡 ** 35.0** (`-56.1`) | 87.1 → 46.4 (`-40.7`) | 86.9 → 25.8 (`-61.1`) | 99.2 → 32.7 (`-66.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_COST_PLUS1` | KB-09 (Dekret Królewski): cost 3 → 4 | 91.1 → 🟡 ** 32.9** (`-58.2`) | 87.1 → 49.0 (`-38.1`) | 86.9 → 16.7 (`-70.2`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_COST_MINUS1` | KB-09 (Dekret Królewski): cost 3 → 2 | 91.1 → 🟡 ** 27.8** (`-63.3`) | 87.1 → 38.9 (`-48.2`) | 86.9 → 16.7 (`-70.2`) | 99.2 → 0.0 (`-99.2`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (75)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | 5.50 Er (1–9) | 4.0% | 28.3% | 1.02 (0–4) | 3.52 (0–18) | 0.52zł (0.0–2.7) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_COST_MINUS1` | 5.47 Er (1–9) | 3.7% | 27.9% | 1.02 (0–3) | 3.51 (0–18) | 0.56zł (0.0–3.0) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-08_COST_MINUS1` | 5.51 Er (1–9) | 4.0% | 28.2% | 1.03 (0–4) | 3.54 (0–18) | 0.52zł (0.0–2.7) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_COST_MINUS1` | 5.47 Er (1–9) | 3.6% | 27.8% | 1.02 (0–3) | 3.50 (0–20) | 0.55zł (0.0–3.0) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-06_COST_MINUS1` | 5.51 Er (1–9) | 4.0% | 27.5% | 1.03 (0–4) | 3.51 (0–18) | 0.51zł (0.0–3.0) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-03_HERESY_PLUS1` | 5.48 Er (1–9) | 3.9% | 28.2% | 1.02 (0–4) | 3.59 (0–18) | 0.52zł (0.0–2.7) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-02_HERESY_PLUS1` | 5.48 Er (1–9) | 3.9% | 28.3% | 1.02 (0–4) | 3.59 (0–18) | 0.52zł (0.0–3.0) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_COST_MINUS1` | 5.46 Er (1–9) | 3.7% | 28.1% | 1.02 (0–3) | 3.49 (0–18) | 0.54zł (0.0–2.7) | 6.15 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_COST_PLUS1` | 5.51 Er (1–9) | 3.9% | 29.7% | 1.02 (0–4) | 3.49 (0–18) | 0.58zł (0.0–2.7) | 6.12 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-07_COST_PLUS1` | 5.50 Er (1–9) | 3.9% | 28.3% | 1.04 (0–3) | 3.52 (0–18) | 0.54zł (0.0–3.3) | 6.21 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-06_HERESY_PLUS1` | 5.49 Er (1–9) | 3.6% | 28.3% | 1.01 (0–4) | 3.54 (0–18) | 0.52zł (0.0–2.7) | 6.24 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-08_HERESY_PLUS1` | 5.50 Er (1–9) | 3.9% | 28.3% | 1.02 (0–4) | 3.53 (0–18) | 0.52zł (0.0–2.7) | 6.21 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-09_COST_MINUS1` | 5.50 Er (1–9) | 3.9% | 27.5% | 1.05 (0–3) | 3.53 (0–18) | 0.52zł (0.0–3.0) | 6.23 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-09_HERESY_PLUS1` | 5.48 Er (1–9) | 3.8% | 28.2% | 1.02 (0–4) | 3.61 (0–18) | 0.52zł (0.0–3.0) | 6.33 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-06_HERESY_PLUS1` | 5.49 Er (1–9) | 3.7% | 28.2% | 1.02 (0–4) | 3.57 (0–18) | 0.52zł (0.0–2.7) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-08_COST_PLUS1` | 5.54 Er (1–9) | 4.3% | 28.6% | 1.04 (0–3) | 3.48 (0–18) | 0.53zł (0.0–3.0) | 6.15 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-04_COST_MINUS1` | 5.47 Er (1–9) | 3.7% | 27.6% | 1.02 (0–4) | 3.55 (0–17) | 0.54zł (0.0–2.7) | 6.27 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_COST_MINUS1` | 5.48 Er (1–9) | 3.8% | 27.7% | 1.02 (0–3) | 3.53 (0–18) | 0.55zł (0.0–3.0) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_COST_MINUS1` | 5.47 Er (1–9) | 3.8% | 27.9% | 1.02 (0–3) | 3.51 (0–18) | 0.56zł (0.0–2.7) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-10_COST_MINUS1` | 5.50 Er (1–9) | 4.0% | 28.2% | 1.02 (0–4) | 3.53 (0–18) | 0.69zł (0.0–3.0) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-01_HERESY_PLUS1` | 5.49 Er (1–9) | 3.9% | 28.2% | 1.02 (0–4) | 3.55 (0–18) | 0.52zł (0.0–2.7) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-09_COST_PLUS1` | 5.52 Er (1–9) | 4.1% | 28.8% | 1.03 (0–4) | 3.50 (0–19) | 0.51zł (0.0–3.0) | 6.16 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-03_HERESY_MINUS1` | 5.50 Er (1–9) | 3.3% | 28.3% | 1.03 (0–3) | 3.47 (0–18) | 0.51zł (0.0–2.7) | 6.05 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-04_COST_MINUS1` | 5.50 Er (1–9) | 3.9% | 28.1% | 1.02 (0–4) | 3.53 (0–18) | 0.68zł (0.0–3.0) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_HERESY_PLUS1` | 5.48 Er (1–9) | 3.7% | 28.2% | 1.02 (0–3) | 3.59 (0–19) | 0.52zł (0.0–2.7) | 6.29 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-01_COST_PLUS1` | 5.50 Er (1–9) | 3.8% | 28.8% | 1.02 (0–4) | 3.50 (0–19) | 0.53zł (0.0–2.7) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-07_COST_MINUS1` | 5.50 Er (1–9) | 4.0% | 28.1% | 1.02 (0–4) | 3.52 (0–18) | 0.68zł (0.0–3.3) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_HERESY_PLUS1` | 5.50 Er (1–9) | 3.8% | 28.3% | 1.02 (0–3) | 3.56 (0–18) | 0.52zł (0.0–2.7) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-07_HERESY_PLUS1` | 5.50 Er (1–9) | 4.0% | 28.3% | 1.02 (0–4) | 3.55 (0–18) | 0.52zł (0.0–2.7) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-05_HERESY_PLUS1` | 5.49 Er (1–9) | 3.9% | 28.3% | 1.02 (0–4) | 3.55 (0–18) | 0.52zł (0.0–2.7) | 6.24 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_COST_MINUS1` | 5.47 Er (1–9) | 3.7% | 28.1% | 1.02 (0–3) | 3.48 (0–18) | 0.53zł (0.0–2.7) | 6.14 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-06_COST_MINUS1` | 5.50 Er (1–9) | 4.0% | 28.2% | 1.02 (0–4) | 3.53 (0–18) | 0.71zł (0.0–3.0) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-04_HERESY_PLUS1` | 5.48 Er (1–9) | 3.8% | 28.2% | 1.02 (0–4) | 3.66 (0–18) | 0.52zł (0.0–3.0) | 6.32 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-09_HERESY_MINUS1` | 5.50 Er (1–9) | 3.4% | 28.3% | 1.02 (0–4) | 3.49 (0–18) | 0.53zł (0.0–2.7) | 6.07 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-02_COST_PLUS1` | 5.54 Er (1–9) | 4.2% | 30.1% | 1.03 (0–4) | 3.53 (0–17) | 0.51zł (0.0–3.0) | 6.15 (0.7–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-06_HERESY_PLUS1` | 5.49 Er (1–9) | 3.9% | 28.2% | 1.02 (0–4) | 3.52 (0–19) | 0.52zł (0.0–2.7) | 6.21 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-08_HERESY_PLUS1` | 5.50 Er (1–9) | 3.9% | 28.4% | 1.02 (0–4) | 3.61 (0–18) | 0.52zł (0.0–3.0) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-04_HERESY_PLUS1` | 5.45 Er (1–9) | 3.7% | 28.1% | 1.01 (0–4) | 3.62 (0–19) | 0.52zł (0.0–2.7) | 6.25 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-02_COST_PLUS1` | 5.53 Er (1–9) | 4.2% | 30.5% | 1.01 (0–3) | 3.49 (0–18) | 0.54zł (0.0–2.7) | 6.17 (0.7–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-04_COST_PLUS1` | 5.49 Er (1–9) | 4.0% | 29.1% | 1.01 (0–3) | 3.52 (0–18) | 0.54zł (0.0–2.7) | 6.18 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-01_HERESY_PLUS1` | 5.48 Er (1–9) | 3.7% | 28.2% | 1.02 (0–4) | 3.54 (0–18) | 0.52zł (0.0–2.7) | 6.24 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-09_HERESY_PLUS1` | 5.45 Er (1–9) | 3.4% | 28.1% | 1.02 (0–3) | 3.56 (0–18) | 0.52zł (0.0–2.7) | 6.27 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-09_COST_MINUS1` | 5.48 Er (1–9) | 3.4% | 27.9% | 1.02 (0–4) | 3.58 (0–17) | 0.54zł (0.0–3.0) | 6.28 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_COST_PLUS1` | 5.51 Er (1–9) | 4.0% | 28.9% | 1.03 (0–4) | 3.51 (0–18) | 0.53zł (0.0–2.7) | 6.18 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-09_COST_MINUS1` | 5.50 Er (1–9) | 4.0% | 28.1% | 1.02 (0–4) | 3.52 (0–18) | 0.70zł (0.0–3.0) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_COST_MINUS1` | 5.49 Er (1–9) | 3.9% | 28.0% | 1.02 (0–3) | 3.56 (0–18) | 0.57zł (0.0–2.7) | 6.24 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-10_COST_MINUS1` | 5.44 Er (1–9) | 3.4% | 27.2% | 1.12 (0–4) | 3.56 (0–18) | 0.56zł (0.0–3.0) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-08_HERESY_MINUS1` | 5.56 Er (1–9) | 4.6% | 28.5% | 1.03 (0–4) | 3.46 (0–18) | 0.52zł (0.0–2.7) | 6.08 (0.3–10.0) | 🟢 W NORMIE |
| `L3_GC-07_COST_MINUS1` | 5.48 Er (1–9) | 3.7% | 27.8% | 1.02 (0–4) | 3.55 (0–20) | 0.51zł (0.0–2.7) | 6.28 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_PLUS1` | 5.52 Er (1–9) | 4.2% | 28.7% | 1.03 (0–4) | 3.54 (0–18) | 0.43zł (0.0–2.7) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-09_COST_PLUS1` | 5.50 Er (1–9) | 3.7% | 28.4% | 1.04 (0–3) | 3.51 (0–18) | 0.53zł (0.0–2.7) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-04_COST_PLUS1` | 5.53 Er (1–9) | 4.1% | 28.6% | 1.03 (0–3) | 3.52 (0–18) | 0.42zł (0.0–2.7) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-05_HERESY_PLUS1` | 5.51 Er (1–9) | 4.6% | 28.3% | 1.02 (0–3) | 3.61 (0–18) | 0.52zł (0.0–2.7) | 6.33 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-01_COST_PLUS1` | 5.50 Er (1–9) | 3.9% | 29.1% | 1.02 (0–4) | 3.52 (0–18) | 0.54zł (0.0–3.0) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_MINUS1` | 5.53 Er (1–9) | 4.5% | 28.4% | 1.03 (0–4) | 3.39 (0–18) | 0.52zł (0.0–3.0) | 5.81 (0.3–10.0) | 🟢 W NORMIE |
| `L3_GC-02_COST_MINUS1` | 5.45 Er (1–9) | 3.6% | 27.5% | 1.02 (0–4) | 3.52 (0–19) | 0.55zł (0.0–3.0) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-03_COST_MINUS1` | 5.45 Er (1–9) | 3.6% | 27.5% | 1.01 (0–4) | 3.52 (0–18) | 0.54zł (0.0–3.0) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-08_COST_PLUS1` | 5.52 Er (1–9) | 4.2% | 28.6% | 1.03 (0–4) | 3.53 (0–18) | 0.44zł (0.0–2.7) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-01_HERESY_PLUS1` | 5.43 Er (1–9) | 3.3% | 28.0% | 1.01 (0–3) | 3.55 (0–18) | 0.51zł (0.0–2.7) | 6.28 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-05_COST_PLUS1` | 5.53 Er (1–9) | 4.2% | 28.7% | 1.03 (0–4) | 3.52 (0–18) | 0.43zł (0.0–2.7) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-06_COST_PLUS1` | 5.53 Er (1–9) | 4.2% | 28.8% | 1.03 (0–4) | 3.58 (0–19) | 0.52zł (0.0–3.3) | 6.25 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-10_COST_MINUS1` | 5.45 Er (1–9) | 3.3% | 27.9% | 1.01 (0–4) | 3.58 (0–19) | 0.49zł (0.0–2.7) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-01_COST_MINUS1` | 5.48 Er (1–9) | 3.6% | 27.6% | 1.02 (0–4) | 3.50 (0–16) | 0.54zł (0.0–2.7) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-07_COST_PLUS1` | 5.49 Er (1–9) | 3.9% | 28.5% | 1.02 (0–4) | 3.50 (0–17) | 0.52zł (0.0–2.7) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-03_HERESY_PLUS1` | 5.40 Er (1–9) | 3.1% | 27.9% | 1.01 (0–3) | 3.58 (0–18) | 0.51zł (0.0–2.7) | 6.29 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_MINUS1` | 5.46 Er (1–9) | 3.5% | 27.6% | 1.01 (0–4) | 3.52 (0–18) | 0.54zł (0.0–3.0) | 6.27 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-09_HERESY_PLUS1` | 5.52 Er (1–9) | 5.2% | 28.3% | 1.02 (0–3) | 3.63 (0–19) | 0.52zł (0.0–3.0) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-02_COST_PLUS1` | 5.62 Er (1–9) | 4.6% | 30.8% | 1.04 (0–4) | 3.65 (0–18) | 0.53zł (0.0–2.7) | 6.24 (0.7–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-03_HERESY_PLUS1` | 5.52 Er (1–9) | 5.3% | 28.4% | 1.03 (0–3) | 3.64 (0–18) | 0.53zł (0.0–3.0) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-06_COST_MINUS1` | 5.45 Er (1–9) | 3.6% | 27.7% | 1.01 (0–4) | 3.49 (0–18) | 0.53zł (0.0–3.0) | 6.25 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-02_HERESY_PLUS1` | 5.48 Er (1–9) | 3.6% | 28.4% | 1.02 (0–4) | 3.60 (0–19) | 0.52zł (0.0–2.7) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-10_COST_PLUS1` | 5.68 Er (1–9) | 5.6% | 29.5% | 1.05 (0–4) | 3.65 (0–18) | 0.54zł (0.0–3.0) | 6.23 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-06_HERESY_PLUS1` | 5.53 Er (1–9) | 5.6% | 28.4% | 1.03 (0–3) | 3.65 (0–19) | 0.53zł (0.0–3.0) | 6.36 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-06_COST_PLUS1` | 5.47 Er (1–9) | 3.6% | 28.4% | 1.02 (0–4) | 3.49 (0–19) | 0.52zł (0.0–2.7) | 6.21 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-05_COST_PLUS1` | 5.57 Er (1–9) | 4.5% | 29.0% | 1.03 (0–4) | 3.53 (0–18) | 0.52zł (0.0–3.0) | 6.22 (0.7–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 86 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_GC-05_COST_PLUS1` | 5.50 Er (1–9) | 4.0% | 28.3% | 1.02 (0–4) | 3.52 (0–18) | 0.52zł (0.0–2.7) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-05_HERESY_PLUS1` | 5.50 Er (1–9) | 4.0% | 28.3% | 1.02 (0–4) | 3.52 (0–18) | 0.52zł (0.0–2.7) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-05_COST_PLUS1` | 5.50 Er (1–9) | 4.0% | 28.3% | 1.02 (0–4) | 3.52 (0–18) | 0.52zł (0.0–2.7) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-05_HERESY_PLUS1` | 5.50 Er (1–9) | 4.0% | 28.3% | 1.02 (0–4) | 3.52 (0–18) | 0.52zł (0.0–2.7) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-02_COST_MINUS1` | 5.50 Er (1–9) | 4.0% | 28.2% | 1.02 (0–4) | 3.52 (0–18) | 0.69zł (0.0–3.3) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-02_COST_PLUS1` | 5.52 Er (1–9) | 4.3% | 29.1% | 1.03 (0–4) | 3.55 (0–18) | 0.42zł (0.0–2.7) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-03_HERESY_PLUS1` | 5.47 Er (1–9) | 3.7% | 28.2% | 1.02 (0–4) | 3.57 (0–19) | 0.52zł (0.0–2.7) | 6.24 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-07_COST_PLUS1` | 5.52 Er (1–9) | 4.3% | 28.6% | 1.03 (0–3) | 3.55 (0–18) | 0.42zł (0.0–2.7) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-08_COST_MINUS1` | 5.50 Er (1–9) | 4.0% | 28.2% | 1.02 (0–4) | 3.53 (0–18) | 0.68zł (0.0–3.0) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_COST_MINUS1` | 5.48 Er (1–9) | 3.9% | 27.9% | 1.02 (0–4) | 3.50 (0–18) | 0.57zł (0.0–3.0) | 6.18 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_COST_MINUS1` | 5.46 Er (1–9) | 3.7% | 27.9% | 1.02 (0–4) | 3.51 (0–18) | 0.56zł (0.0–2.7) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-03_COST_MINUS1` | 5.49 Er (1–9) | 3.8% | 27.3% | 1.04 (0–3) | 3.55 (0–18) | 0.54zł (0.0–3.0) | 6.22 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-07_HERESY_MINUS1` | 5.51 Er (1–9) | 4.1% | 28.3% | 1.03 (0–4) | 3.51 (0–18) | 0.52zł (0.0–2.7) | 6.14 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_MINUS1` | 5.50 Er (1–9) | 3.9% | 28.2% | 1.02 (0–4) | 3.52 (0–18) | 0.67zł (0.0–3.0) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-07_COST_MINUS1` | 5.50 Er (1–9) | 4.1% | 27.5% | 1.04 (0–4) | 3.51 (0–18) | 0.51zł (0.0–3.0) | 6.21 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-04_COST_PLUS1` | 5.53 Er (1–9) | 4.2% | 28.9% | 1.03 (0–4) | 3.48 (0–16) | 0.52zł (0.0–3.3) | 6.13 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-08_COST_PLUS1` | 5.50 Er (1–9) | 3.9% | 28.3% | 1.02 (0–4) | 3.52 (0–19) | 0.52zł (0.0–2.7) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-06_COST_PLUS1` | 5.49 Er (1–9) | 3.7% | 28.2% | 1.04 (0–3) | 3.52 (0–18) | 0.54zł (0.0–3.0) | 6.22 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_HERESY_PLUS1` | 5.48 Er (1–9) | 3.7% | 28.2% | 1.02 (0–3) | 3.58 (0–19) | 0.52zł (0.0–2.7) | 6.31 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-05_COST_MINUS1` | 5.50 Er (1–9) | 4.0% | 28.1% | 1.02 (0–4) | 3.53 (0–18) | 0.69zł (0.0–3.0) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_HERESY_PLUS1` | 5.47 Er (1–9) | 3.6% | 28.2% | 1.02 (0–4) | 3.59 (0–19) | 0.52zł (0.0–2.7) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_HERESY_MINUS1` | 5.51 Er (1–9) | 4.2% | 28.3% | 1.03 (0–4) | 3.49 (0–18) | 0.52zł (0.0–2.7) | 6.12 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-01_COST_MINUS1` | 5.49 Er (1–9) | 3.8% | 27.4% | 1.04 (0–4) | 3.53 (0–18) | 0.54zł (0.0–2.7) | 6.22 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-07_HERESY_PLUS1` | 5.46 Er (1–9) | 3.5% | 28.2% | 1.02 (0–3) | 3.55 (0–18) | 0.52zł (0.0–2.7) | 6.27 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_HERESY_PLUS1` | 5.46 Er (1–9) | 3.6% | 28.2% | 1.02 (0–3) | 3.61 (0–19) | 0.52zł (0.0–2.7) | 6.32 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-10_COST_PLUS1` | 5.52 Er (1–9) | 4.3% | 28.6% | 1.03 (0–4) | 3.52 (0–18) | 0.42zł (0.0–2.7) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-02_COST_MINUS1` | 5.47 Er (1–9) | 3.9% | 27.2% | 1.08 (0–4) | 3.54 (0–18) | 0.57zł (0.0–3.7) | 6.24 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-03_COST_PLUS1` | 5.53 Er (1–9) | 4.2% | 29.2% | 1.02 (0–4) | 3.46 (0–18) | 0.54zł (0.0–2.7) | 6.15 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-03_COST_PLUS1` | 5.52 Er (1–9) | 4.1% | 28.7% | 1.03 (0–4) | 3.53 (0–20) | 0.39zł (0.0–2.3) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_HERESY_PLUS1` | 5.49 Er (1–9) | 3.8% | 28.3% | 1.02 (0–4) | 3.57 (0–19) | 0.52zł (0.0–2.7) | 6.29 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-02_HERESY_PLUS1` | 5.51 Er (1–9) | 4.7% | 28.3% | 1.02 (0–3) | 3.59 (0–19) | 0.52zł (0.0–3.0) | 6.33 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_HERESY_PLUS1` | 5.47 Er (1–9) | 3.6% | 28.2% | 1.02 (0–3) | 3.63 (0–19) | 0.52zł (0.0–2.7) | 6.32 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_HERESY_MINUS1` | 5.52 Er (1–9) | 4.2% | 28.4% | 1.03 (0–4) | 3.45 (0–18) | 0.52zł (0.0–2.7) | 6.04 (0.3–10.0) | 🟢 W NORMIE |
| `L3_GC-03_COST_PLUS1` | 5.54 Er (1–9) | 4.2% | 28.9% | 1.03 (0–4) | 3.47 (0–19) | 0.52zł (0.0–2.7) | 6.16 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-04_COST_MINUS1` | 5.48 Er (1–9) | 3.9% | 27.2% | 1.05 (0–3) | 3.55 (0–18) | 0.55zł (0.0–3.3) | 6.22 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-08_COST_MINUS1` | 5.45 Er (1–9) | 3.7% | 27.2% | 1.03 (0–4) | 3.53 (0–18) | 0.50zł (0.0–3.0) | 6.22 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-04_COST_PLUS1` | 5.52 Er (1–9) | 3.9% | 29.2% | 1.02 (0–4) | 3.50 (0–18) | 0.53zł (0.0–3.3) | 6.18 (0.6–10.0) | 🟢 W NORMIE |
| `L3_KT-06_COST_PLUS1` | 5.53 Er (1–9) | 4.5% | 28.9% | 1.03 (0–3) | 3.52 (0–19) | 0.44zł (0.0–2.7) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-09_COST_PLUS1` | 5.52 Er (1–9) | 4.1% | 28.7% | 1.03 (0–4) | 3.51 (0–18) | 0.43zł (0.0–2.7) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_HERESY_PLUS1` | 5.48 Er (1–9) | 3.7% | 28.3% | 1.02 (0–3) | 3.61 (0–19) | 0.51zł (0.0–2.7) | 6.32 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-07_HERESY_PLUS1` | 5.51 Er (1–9) | 4.8% | 28.3% | 1.02 (0–4) | 3.61 (0–18) | 0.52zł (0.0–3.0) | 6.34 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-07_HERESY_PLUS1` | 5.44 Er (1–9) | 3.4% | 28.1% | 1.01 (0–4) | 3.52 (0–18) | 0.52zł (0.0–2.7) | 6.23 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-01_HERESY_PLUS1` | 5.52 Er (1–9) | 4.7% | 28.3% | 1.02 (0–4) | 3.59 (0–18) | 0.53zł (0.0–3.0) | 6.33 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_COST_MINUS1` | 5.46 Er (1–9) | 3.7% | 28.0% | 1.02 (0–3) | 3.49 (0–18) | 0.53zł (0.0–2.7) | 6.15 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-10_HERESY_PLUS1` | 5.40 Er (1–9) | 3.5% | 28.0% | 1.01 (0–3) | 3.57 (0–18) | 0.51zł (0.0–2.7) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-04_HERESY_MINUS1` | 5.52 Er (1–9) | 4.1% | 28.4% | 1.03 (0–4) | 3.39 (0–18) | 0.52zł (0.0–2.7) | 6.05 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-08_HERESY_PLUS1` | 5.51 Er (1–9) | 4.6% | 28.3% | 1.02 (0–3) | 3.59 (0–20) | 0.52zł (0.0–3.0) | 6.34 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-08_HERESY_PLUS1` | 5.41 Er (1–9) | 3.2% | 28.0% | 1.01 (0–3) | 3.57 (0–18) | 0.51zł (0.0–2.7) | 6.27 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-04_HERESY_PLUS1` | 5.50 Er (1–9) | 4.7% | 28.3% | 1.02 (0–4) | 3.63 (0–18) | 0.52zł (0.0–3.0) | 6.34 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-04_HERESY_PLUS1` | 5.39 Er (1–9) | 3.1% | 27.9% | 1.01 (0–3) | 3.58 (0–18) | 0.51zł (0.0–2.7) | 6.28 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_COST_PLUS1` | 5.52 Er (1–9) | 4.2% | 28.6% | 1.03 (0–3) | 3.56 (0–18) | 0.53zł (0.0–2.7) | 6.23 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-02_HERESY_PLUS1` | 5.39 Er (1–9) | 3.1% | 27.9% | 1.02 (0–3) | 3.58 (0–18) | 0.52zł (0.0–2.7) | 6.28 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_COST_PLUS1` | 5.53 Er (1–9) | 4.2% | 30.7% | 1.03 (0–3) | 3.57 (0–19) | 0.55zł (0.0–2.7) | 6.22 (0.7–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-10_HERESY_MINUS1` | 5.61 Er (1–9) | 4.5% | 28.6% | 1.04 (0–4) | 3.46 (0–18) | 0.52zł (0.0–2.7) | 6.16 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-06_COST_MINUS1` | 5.52 Er (1–9) | 4.2% | 27.8% | 1.02 (0–4) | 3.53 (0–19) | 0.51zł (0.0–2.7) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_COST_PLUS1` | 5.55 Er (1–9) | 4.2% | 29.2% | 1.03 (0–4) | 3.51 (0–20) | 0.52zł (0.0–2.7) | 6.19 (0.8–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_COST_PLUS1` | 5.54 Er (1–9) | 4.3% | 29.6% | 1.03 (0–4) | 3.52 (0–18) | 0.55zł (0.0–2.7) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-10_COST_PLUS1` | 5.56 Er (1–9) | 4.5% | 28.9% | 1.03 (0–4) | 3.47 (0–18) | 0.51zł (0.0–2.7) | 6.06 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_PLUS1` | 5.56 Er (1–9) | 4.2% | 29.4% | 1.03 (0–4) | 3.48 (0–17) | 0.51zł (0.0–3.0) | 6.13 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-04_HERESY_MINUS1` | 5.56 Er (1–9) | 4.3% | 28.4% | 1.03 (0–4) | 3.43 (0–18) | 0.52zł (0.0–3.0) | 6.12 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_COST_PLUS1` | 5.56 Er (1–9) | 4.4% | 29.1% | 1.03 (0–4) | 3.55 (0–20) | 0.54zł (0.0–2.7) | 6.20 (0.8–10.0) | 🟢 W NORMIE |
| `L3_KB-09_HERESY_MINUS1` | 5.52 Er (1–9) | 3.9% | 28.4% | 1.03 (0–4) | 3.41 (0–18) | 0.52zł (0.0–2.7) | 6.07 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_COST_PLUS1` | 5.53 Er (1–9) | 4.2% | 29.6% | 1.03 (0–4) | 3.58 (0–20) | 0.55zł (0.0–2.7) | 6.23 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-10_HERESY_MINUS1` | 5.54 Er (1–9) | 4.3% | 28.4% | 1.03 (0–4) | 3.24 (0–18) | 0.52zł (0.0–3.0) | 5.96 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-10_COST_PLUS1` | 5.63 Er (1–9) | 4.6% | 27.5% | 0.87 (0–4) | 3.39 (0–18) | 0.52zł (0.0–3.0) | 6.14 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-10_HERESY_PLUS1` | 5.52 Er (1–9) | 5.5% | 28.3% | 1.03 (0–4) | 3.75 (0–20) | 0.53zł (0.0–3.0) | 6.46 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_HERESY_PLUS1` | 5.44 Er (1–9) | 3.4% | 28.0% | 1.01 (0–4) | 3.69 (0–18) | 0.52zł (0.0–2.7) | 6.38 (1.3–10.0) | 🟢 W NORMIE |
| `L3_KB-01_COST_PLUS1` | 5.46 Er (1–9) | 3.6% | 29.1% | 1.01 (0–4) | 3.48 (0–18) | 0.52zł (0.0–2.7) | 6.22 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_COST_PLUS1` | 5.56 Er (1–9) | 4.4% | 29.1% | 1.03 (0–4) | 3.54 (0–20) | 0.54zł (0.0–2.7) | 6.17 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-03_COST_PLUS1` | 5.49 Er (1–9) | 3.8% | 29.2% | 1.02 (0–4) | 3.41 (0–18) | 0.52zł (0.0–2.7) | 6.14 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-09_HERESY_PLUS1` | 5.53 Er (1–9) | 4.2% | 28.3% | 1.03 (0–4) | 3.73 (0–18) | 0.53zł (0.0–2.7) | 6.28 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-10_HERESY_PLUS1` | 5.42 Er (1–9) | 3.7% | 28.0% | 1.01 (0–4) | 3.87 (0–18) | 0.52zł (0.0–3.0) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-07_COST_MINUS1` | 5.47 Er (1–9) | 3.7% | 27.8% | 1.02 (0–4) | 3.48 (0–18) | 0.51zł (0.0–2.7) | 6.21 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-04_COST_MINUS1` | 5.42 Er (1–9) | 3.4% | 27.5% | 1.01 (0–4) | 3.47 (0–18) | 0.52zł (0.0–2.7) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-07_COST_PLUS1` | 5.45 Er (1–9) | 3.6% | 28.4% | 1.01 (0–4) | 3.42 (0–18) | 0.51zł (0.0–3.0) | 6.17 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-10_HERESY_PLUS1` | 5.36 Er (1–9) | 3.6% | 27.9% | 1.00 (0–4) | 3.78 (0–20) | 0.52zł (0.0–3.3) | 6.23 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_PLUS1` | 5.41 Er (1–9) | 3.4% | 28.0% | 1.01 (0–3) | 3.77 (0–18) | 0.51zł (0.0–2.7) | 6.40 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-01_COST_MINUS1` | 5.44 Er (1–9) | 3.4% | 27.5% | 1.01 (0–4) | 3.45 (0–18) | 0.52zł (0.0–2.7) | 6.21 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-03_COST_MINUS1` | 5.42 Er (1–9) | 3.5% | 27.5% | 1.01 (0–4) | 3.48 (0–19) | 0.52zł (0.0–2.7) | 6.22 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-10_HERESY_MINUS1` | 5.58 Er (1–9) | 4.3% | 28.5% | 1.04 (0–4) | 3.20 (0–18) | 0.52zł (0.0–2.7) | 6.02 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-05_COST_MINUS1` | 5.41 Er (1–9) | 3.0% | 28.2% | 1.01 (0–4) | 3.42 (0–18) | 0.49zł (0.0–2.7) | 6.17 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_COST_PLUS1` | 5.61 Er (1–9) | 4.8% | 29.2% | 1.04 (0–4) | 3.58 (0–18) | 0.54zł (0.0–2.7) | 6.18 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-02_COST_MINUS1` | 5.40 Er (1–9) | 3.3% | 27.7% | 1.01 (0–4) | 3.44 (0–18) | 0.53zł (0.0–3.0) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-10_COST_MINUS1` | 5.28 Er (1–9) | 2.5% | 27.8% | 0.99 (0–4) | 3.42 (0–18) | 0.48zł (0.0–2.7) | 6.20 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-09_COST_PLUS1` | 5.76 Er (1–9) | 5.6% | 30.3% | 1.06 (0–4) | 3.84 (0–20) | 0.51zł (0.0–2.7) | 6.30 (0.7–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-09_COST_MINUS1` | 5.31 Er (1–9) | 2.8% | 27.8% | 0.99 (0–4) | 3.39 (0–18) | 0.47zł (0.0–2.7) | 6.16 (0.7–10.0) | 🟢 W NORMIE |

</details>