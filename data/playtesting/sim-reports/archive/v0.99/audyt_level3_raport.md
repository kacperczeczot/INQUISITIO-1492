# Raport Precyzyjnego Audytu Poziomu 3 (Parametry Pojedynczych Kart) — Wersja Balansu: v0.99

**Wersja Balansu:** `v0.99` | **Data:** 2026-08-18 00:54 | **Przeanalizowano Wariantów Kart:** 194 | **Próba:** 1000 gier/setup | **Czas:** 829.47s
**Filtry:** Parametry: `cost,heresy` | Frakcja: `all` | Karta: `Wszystkie`
**Wynik Bazy Poziomu 3 (Global):** `🔴 9.4 pkt` | 3p: `3.3 pkt` | 4p: `10.5 pkt` | 5p: `14.4 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (67)

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | Baza (Bieżące parametry wszystkich kart) | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_KT-09_HERESY_MINUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 0 | 9.4 → 🔴 ** 17.4** (`⬆️ +8.0`) | 3.3 → 9.7 (`⬆️ +6.4`) | 10.5 → 24.5 (`⬆️ +14.0`) | 14.4 → 18.0 (`⬆️ +3.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-09_COST_MINUS1` | KT-09 (Fragment Kodeksu): cost 2 → 1 | 9.4 → 🔴 ** 16.5** (`⬆️ +7.1`) | 3.3 → 6.9 (`⬆️ +3.6`) | 10.5 → 23.4 (`⬆️ +12.9`) | 14.4 → 19.2 (`⬆️ +4.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-10_COST_PLUS1` | KT-10 (Pieczęć Salomona): cost 2 → 3 | 9.4 → 🔴 ** 13.3** (`⬆️ +3.9`) | 3.3 → 4.6 (`⬆️ +1.3`) | 10.5 → 16.3 (`⬆️ +5.8`) | 14.4 → 19.1 (`⬆️ +4.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-05_COST_MINUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 0 | 9.4 → 🔴 ** 12.2** (`⬆️ +2.8`) | 3.3 → 4.3 (`⬆️ +1.0`) | 10.5 → 14.4 (`⬆️ +3.9`) | 14.4 → 18.0 (`⬆️ +3.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-10_HERESY_PLUS1` | KT-10 (Pieczęć Salomona): heresy 1 → 2 | 9.4 → 🔴 ** 12.0** (`⬆️ +2.6`) | 3.3 → 4.3 (`⬆️ +1.0`) | 10.5 → 14.6 (`⬆️ +4.1`) | 14.4 → 17.2 (`⬆️ +2.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-02_COST_MINUS1` | KT-02 (Transmutacja Złota): cost 1 → 0 | 9.4 → 🔴 ** 11.7** (`⬆️ +2.3`) | 3.3 → 4.1 (`⬆️ +0.8`) | 10.5 → 13.5 (`⬆️ +3.0`) | 14.4 → 17.6 (`⬆️ +3.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-03_HERESY_MINUS1` | KT-03 (Zakazana Wiedza): heresy 1 → 0 | 9.4 → 🔴 ** 11.3** (`⬆️ +1.9`) | 3.3 → 3.9 (`⬆️ +0.6`) | 10.5 → 12.1 (`⬆️ +1.6`) | 14.4 → 17.9 (`⬆️ +3.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-02_COST_MINUS1` | CAA-02 (Złoto z Kryjówki): cost 1 → 0 | 9.4 → 🔴 ** 11.0** (`⬆️ +1.6`) | 3.3 → 3.6 (`⬆️ +0.3`) | 10.5 → 12.3 (`⬆️ +1.8`) | 14.4 → 17.0 (`⬆️ +2.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-09_HERESY_PLUS1` | GC-09 (Lista Dłużników): heresy 0 → 1 | 9.4 → 🔴 ** 10.8** (`⬆️ +1.4`) | 3.3 → 3.2 (`-0.1`) | 10.5 → 11.9 (`⬆️ +1.4`) | 14.4 → 17.3 (`⬆️ +2.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-02_HERESY_PLUS1` | GC-02 (Czarny Rynek): heresy 1 → 2 | 9.4 → 🔴 ** 10.8** (`⬆️ +1.4`) | 3.3 | 10.5 → 12.0 (`⬆️ +1.5`) | 14.4 → 17.0 (`⬆️ +2.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-04_HERESY_PLUS1` | GC-04 (Informator): heresy 1 → 2 | 9.4 → 🔴 ** 10.6** (`⬆️ +1.2`) | 3.3 → 3.2 (`-0.1`) | 10.5 → 12.1 (`⬆️ +1.6`) | 14.4 → 16.6 (`⬆️ +2.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-06_HERESY_MINUS1` | CAA-06 (Ucieczka z Lochów): heresy 1 → 0 | 9.4 → 🔴 ** 10.6** (`⬆️ +1.2`) | 3.3 → 3.8 (`⬆️ +0.5`) | 10.5 → 11.7 (`⬆️ +1.2`) | 14.4 → 16.3 (`⬆️ +1.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-06_HERESY_PLUS1` | GC-06 (Szantaż): heresy 0 → 1 | 9.4 → 🔴 ** 10.4** (`⬆️ +1.0`) | 3.3 | 10.5 → 11.2 (`⬆️ +0.7`) | 14.4 → 16.6 (`⬆️ +2.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-05_HERESY_PLUS1` | CAA-05 (Ukryty Kurier): heresy 0 → 1 | 9.4 → 🔴 ** 10.1** (`⬆️ +0.7`) | 3.3 → 3.4 (`⬆️ +0.1`) | 10.5 → 11.3 (`⬆️ +0.8`) | 14.4 → 15.7 (`⬆️ +1.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-06_COST_PLUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 3 | 9.4 → 🔴 ** 10.0** (`⬆️ +0.6`) | 3.3 → 3.5 (`⬆️ +0.2`) | 10.5 → 11.7 (`⬆️ +1.2`) | 14.4 → 14.7 (`⬆️ +0.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-04_COST_MINUS1` | CAA-04 (Fałszywy Trop): cost 1 → 0 | 9.4 → 🔴 **  9.9** (`⬆️ +0.5`) | 3.3 | 10.5 → 10.4 (`-0.1`) | 14.4 → 16.0 (`⬆️ +1.6`) | ⚪ OPTYMALNY |
| `L3_GC-10_COST_MINUS1` | GC-10 (Upadek Domu): cost 4 → 3 | 9.4 → 🔴 **  9.7** (`⬆️ +0.3`) | 3.3 | 10.5 | 14.4 → 15.3 (`⬆️ +0.9`) | ⚪ OPTYMALNY |
| `L3_SO-11_COST_MINUS1` | SO-11 (Dekret Czystości Wiary): cost 1 → 0 | 9.4 → 🔴 **  9.7** (`⬆️ +0.3`) | 3.3 | 10.5 → 10.4 (`-0.1`) | 14.4 → 15.3 (`⬆️ +0.9`) | ⚪ OPTYMALNY |
| `L3_CAA-03_HERESY_PLUS1` | CAA-03 (Cień na Rynku): heresy 1 → 2 | 9.4 → 🔴 **  9.7** (`⬆️ +0.3`) | 3.3 → 3.2 (`-0.1`) | 10.5 → 10.8 (`⬆️ +0.3`) | 14.4 → 15.1 (`⬆️ +0.7`) | ⚪ OPTYMALNY |
| `L3_KB-04_HERESY_MINUS1` | KB-04 (Faworyt Dworu): heresy 1 → 0 | 9.4 → 🔴 **  9.6** (`⬆️ +0.2`) | 3.3 | 10.5 → 11.7 (`⬆️ +1.2`) | 14.4 → 13.9 (`-0.5`) | ⚪ OPTYMALNY |
| `L3_KB-03_COST_MINUS1` | KB-03 (Plotka Dworska): cost 1 → 0 | 9.4 → 🔴 **  9.6** (`⬆️ +0.2`) | 3.3 | 10.5 | 14.4 → 15.1 (`⬆️ +0.7`) | ⚪ OPTYMALNY |
| `L3_CAA-05_COST_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 2 | 9.4 → 🔴 **  9.6** (`⬆️ +0.2`) | 3.3 | 10.5 → 11.0 (`⬆️ +0.5`) | 14.4 → 14.5 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_CAA-09_COST_MINUS1` | CAA-09 (Kurier Relikwii): cost 2 → 1 | 9.4 → 🔴 **  9.6** (`⬆️ +0.2`) | 3.3 | 10.5 → 11.0 (`⬆️ +0.5`) | 14.4 → 14.6 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L3_KT-05_COST_PLUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 2 | 9.4 → 🔴 **  9.6** (`⬆️ +0.2`) | 3.3 | 10.5 | 14.4 → 14.9 (`⬆️ +0.5`) | ⚪ OPTYMALNY |
| `L3_SO-08_COST_MINUS1` | SO-08 (Nasłanie Inkwizytora): cost 1 → 0 | 9.4 → 🔴 **  9.6** (`⬆️ +0.2`) | 3.3 | 10.5 → 10.6 (`⬆️ +0.1`) | 14.4 → 14.9 (`⬆️ +0.5`) | ⚪ OPTYMALNY |
| `L3_KB-06_COST_MINUS1` | KB-06 (Areszt Królewski): cost 1 → 0 | 9.4 → 🔴 **  9.5** (`⬆️ +0.1`) | 3.3 | 10.5 → 10.4 (`-0.1`) | 14.4 → 14.8 (`⬆️ +0.4`) | ⚪ OPTYMALNY |
| `L3_GC-01_COST_PLUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 2 | 9.4 → 🔴 **  9.5** (`⬆️ +0.1`) | 3.3 → 3.4 (`⬆️ +0.1`) | 10.5 → 10.8 (`⬆️ +0.3`) | 14.4 → 14.3 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_GC-06_COST_PLUS1` | GC-06 (Szantaż): cost 2 → 3 | 9.4 → 🔴 **  9.5** (`⬆️ +0.1`) | 3.3 | 10.5 → 10.7 (`⬆️ +0.2`) | 14.4 → 14.6 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L3_KB-01_COST_MINUS1` | KB-01 (Rozkaz Dworu): cost 1 → 0 | 9.4 → 🔴 **  9.5** (`⬆️ +0.1`) | 3.3 | 10.5 | 14.4 → 14.6 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L3_GC-02_COST_MINUS1` | GC-02 (Czarny Rynek): cost 1 → 0 | 🔴 **  9.4** | 3.3 | 10.5 → 10.9 (`⬆️ +0.4`) | 14.4 → 13.9 (`-0.5`) | ⚪ OPTYMALNY |
| `L3_KB-03_COST_PLUS1` | KB-03 (Plotka Dworska): cost 1 → 2 | 🔴 **  9.4** | 3.3 → 3.2 (`-0.1`) | 10.5 → 10.3 (`-0.2`) | 14.4 → 14.8 (`⬆️ +0.4`) | ⚪ OPTYMALNY |
| `L3_KT-05_HERESY_PLUS1` | KT-05 (Wskazówka Cyklu): heresy 0 → 1 | 🔴 **  9.4** | 3.3 → 3.0 (`-0.3`) | 10.5 → 10.4 (`-0.1`) | 14.4 → 14.7 (`⬆️ +0.3`) | ⚪ OPTYMALNY |
| `L3_CAA-12_HERESY_PLUS1` | CAA-12 (Skrytka w Murach): heresy 1 → 2 | 🔴 **  9.4** | 3.3 → 3.2 (`-0.1`) | 10.5 → 10.3 (`-0.2`) | 14.4 → 14.6 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 2 → 3 | 🔴 **  9.4** | 3.3 | 10.5 → 10.7 (`⬆️ +0.2`) | 14.4 → 14.1 (`-0.3`) | ⚪ OPTYMALNY |
| `L3_CAA-04_COST_PLUS1` | CAA-04 (Fałszywy Trop): cost 1 → 2 | 🔴 **  9.4** | 3.3 | 10.5 → 10.6 (`⬆️ +0.1`) | 14.4 | ⚪ OPTYMALNY |
| `L3_CAA-11_COST_PLUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 2 | 🔴 **  9.4** | 3.3 | 10.5 → 10.6 (`⬆️ +0.1`) | 14.4 → 14.2 (`-0.2`) | ⚪ OPTYMALNY |
| `L3_GC-01_COST_MINUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 0 | 🔴 **  9.4** | 3.3 | 10.5 → 10.6 (`⬆️ +0.1`) | 14.4 → 14.3 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_GC-09_COST_MINUS1` | GC-09 (Lista Dłużników): cost 3 → 2 | 🔴 **  9.4** | 3.3 | 10.5 → 10.6 (`⬆️ +0.1`) | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-10_HERESY_MINUS1` | SO-10 (Oczyść Miasto): heresy 2 → 1 | 🔴 **  9.4** | 3.3 | 10.5 → 10.6 (`⬆️ +0.1`) | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-10_HERESY_PLUS1` | SO-10 (Oczyść Miasto): heresy 2 → 3 | 9.4 → 🔴 **  9.3** (`-0.1`) | 3.3 | 10.5 → 10.8 (`⬆️ +0.3`) | 14.4 → 13.8 (`-0.6`) | ⚪ OPTYMALNY |
| `L3_GC-07_COST_MINUS1` | GC-07 (Skrytobójstwo): cost 2 → 1 | 9.4 → 🔴 **  9.3** (`-0.1`) | 3.3 → 3.4 (`⬆️ +0.1`) | 10.5 → 10.7 (`⬆️ +0.2`) | 14.4 → 13.8 (`-0.6`) | ⚪ OPTYMALNY |
| `L3_GC-09_COST_PLUS1` | GC-09 (Lista Dłużników): cost 3 → 4 | 9.4 → 🔴 **  9.3** (`-0.1`) | 3.3 | 10.5 → 10.7 (`⬆️ +0.2`) | 14.4 → 13.8 (`-0.6`) | ⚪ OPTYMALNY |
| `L3_CAA-10_COST_MINUS1` | CAA-10 (Echo Alhambry): cost 1 → 0 | 9.4 → 🔴 **  9.3** (`-0.1`) | 3.3 | 10.5 → 10.6 (`⬆️ +0.1`) | 14.4 → 14.1 (`-0.3`) | ⚪ OPTYMALNY |
| `L3_GC-12_COST_PLUS1` | GC-12 (Złodziejski Zwiad): cost 0 → 1 | 9.4 → 🔴 **  9.3** (`-0.1`) | 3.3 | 10.5 → 10.6 (`⬆️ +0.1`) | 14.4 → 14.1 (`-0.3`) | ⚪ OPTYMALNY |
| `L3_SO-10_COST_PLUS1` | SO-10 (Oczyść Miasto): cost 5 → 6 | 9.4 → 🔴 **  9.3** (`-0.1`) | 3.3 | 10.5 → 10.2 (`-0.3`) | 14.4 → 14.5 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_KB-11_COST_MINUS1` | KB-11 (Tajny Emisariusz): cost 1 → 0 | 9.4 → 🔴 **  9.2** (`-0.2`) | 3.3 → 4.1 (`⬆️ +0.8`) | 10.5 → 11.1 (`⬆️ +0.6`) | 14.4 → 12.4 (`-2.0`) | ⚪ OPTYMALNY |
| `L3_CAA-10_HERESY_PLUS1` | CAA-10 (Echo Alhambry): heresy 1 → 2 | 9.4 → 🔴 **  9.2** (`-0.2`) | 3.3 → 3.1 (`-0.2`) | 10.5 → 9.6 (`-0.9`) | 14.4 → 14.8 (`⬆️ +0.4`) | ⚪ OPTYMALNY |
| `L3_GC-03_COST_PLUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 2 | 9.4 → 🔴 **  9.2** (`-0.2`) | 3.3 → 3.2 (`-0.1`) | 10.5 → 10.6 (`⬆️ +0.1`) | 14.4 → 13.8 (`-0.6`) | ⚪ OPTYMALNY |
| `L3_KT-06_HERESY_PLUS1` | KT-06 (Przesłuchanie Imienia): heresy 0 → 1 | 9.4 → 🔴 **  9.2** (`-0.2`) | 3.3 | 10.5 → 10.6 (`⬆️ +0.1`) | 14.4 → 13.6 (`-0.8`) | ⚪ OPTYMALNY |
| `L3_KB-05_HERESY_PLUS1` | KB-05 (List Żelazny): heresy 0 → 1 | 9.4 → 🔴 **  9.1** (`-0.3`) | 3.3 → 2.9 (`-0.4`) | 10.5 → 9.3 (`-1.2`) | 14.4 → 15.1 (`⬆️ +0.7`) | ⚪ OPTYMALNY |
| `L3_GC-10_COST_PLUS1` | GC-10 (Upadek Domu): cost 4 → 5 | 9.4 → 🔴 **  9.1** (`-0.3`) | 3.3 → 3.5 (`⬆️ +0.2`) | 10.5 → 9.9 (`-0.6`) | 14.4 → 13.9 (`-0.5`) | ⚪ OPTYMALNY |
| `L3_KB-07_HERESY_PLUS1` | KB-07 (Szantaż Pieczęcią): heresy 0 → 1 | 9.4 → 🔴 **  9.1** (`-0.3`) | 3.3 → 3.2 (`-0.1`) | 10.5 → 9.6 (`-0.9`) | 14.4 → 14.5 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_KB-04_HERESY_PLUS1` | KB-04 (Faworyt Dworu): heresy 1 → 2 | 9.4 → 🔴 **  9.0** (`-0.4`) | 3.3 → 3.6 (`⬆️ +0.3`) | 10.5 → 10.2 (`-0.3`) | 14.4 → 13.1 (`-1.3`) | ⚪ OPTYMALNY |
| `L3_KB-07_COST_PLUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 3 | 9.4 → 🔴 **  9.0** (`-0.4`) | 3.3 → 3.1 (`-0.2`) | 10.5 → 9.3 (`-1.2`) | 14.4 → 14.6 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L3_KB-05_COST_MINUS1` | KB-05 (List Żelazny): cost 2 → 1 | 9.4 → 🔴 **  8.9** (`-0.5`) | 3.3 → 3.5 (`⬆️ +0.2`) | 10.5 → 11.1 (`⬆️ +0.6`) | 14.4 → 12.2 (`-2.2`) | ⚪ OPTYMALNY |
| `L3_SO-02_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): heresy 0 → 1 | 9.4 → 🔴 **  8.9** (`-0.5`) | 3.3 | 10.5 → 10.6 (`⬆️ +0.1`) | 14.4 → 12.9 (`-1.5`) | ⚪ OPTYMALNY |
| `L3_KB-05_COST_PLUS1` | KB-05 (List Żelazny): cost 2 → 3 | 9.4 → 🔴 **  8.8** (`-0.6`) | 3.3 → 2.9 (`-0.4`) | 10.5 → 10.7 (`⬆️ +0.2`) | 14.4 → 12.8 (`-1.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_COST_MINUS1` | KB-12 (Szantaż Salonowy): cost 1 → 0 | 9.4 → 🔴 **  8.7** (`-0.7`) | 3.3 → 3.7 (`⬆️ +0.4`) | 10.5 → 10.6 (`⬆️ +0.1`) | 14.4 → 11.8 (`-2.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_COST_MINUS1` | KB-02 (Pobór Podatków): cost 1 → 0 | 9.4 → 🔴 **  8.6** (`-0.8`) | 3.3 → 3.6 (`⬆️ +0.3`) | 10.5 → 11.2 (`⬆️ +0.7`) | 14.4 → 11.1 (`-3.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_COST_PLUS1` | KB-02 (Pobór Podatków): cost 1 → 2 | 9.4 → 🔴 **  8.6** (`-0.8`) | 3.3 → 2.5 (`-0.8`) | 10.5 → 8.6 (`-1.9`) | 14.4 → 14.6 (`⬆️ +0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_COST_MINUS1` | KB-10 (Pieczęć Korony): cost 2 → 1 | 9.4 → 🔴 **  8.5** (`-0.9`) | 3.3 → 4.6 (`⬆️ +1.3`) | 10.5 → 10.9 (`⬆️ +0.4`) | 14.4 → 10.1 (`-4.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_HERESY_PLUS1` | KB-02 (Pobór Podatków): heresy 0 → 1 | 9.4 → 🔴 **  8.5** (`-0.9`) | 3.3 → 2.4 (`-0.9`) | 10.5 → 8.1 (`-2.4`) | 14.4 → 15.1 (`⬆️ +0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_COST_MINUS1` | KB-09 (Dekret Królewski): cost 3 → 2 | 9.4 → 🔴 **  8.5** (`-0.9`) | 3.3 → 3.6 (`⬆️ +0.3`) | 10.5 → 11.1 (`⬆️ +0.6`) | 14.4 → 10.8 (`-3.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_COST_PLUS1` | KB-04 (Faworyt Dworu): cost 2 → 3 | 9.4 → 🔴 **  8.5** (`-0.9`) | 3.3 → 3.8 (`⬆️ +0.5`) | 10.5 → 9.8 (`-0.7`) | 14.4 → 12.0 (`-2.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_HERESY_MINUS1` | KB-10 (Pieczęć Korony): heresy 2 → 1 | 9.4 → 🔴 **  7.9** (`-1.5`) | 3.3 → 5.5 (`⬆️ +2.2`) | 10.5 → 9.2 (`-1.3`) | 14.4 → 9.0 (`-5.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_HERESY_MINUS1` | KB-09 (Dekret Królewski): heresy 1 → 0 | 9.4 → 🔴 **  6.1** (`-3.3`) | 3.3 → 4.5 (`⬆️ +1.2`) | 10.5 → 6.8 (`-3.7`) | 14.4 → 7.0 (`-7.4`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 127 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_CAA-01_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_CAA-02_HERESY_PLUS1` | CAA-02 (Złoto z Kryjówki): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_CAA-03_COST_PLUS1` | CAA-03 (Cień na Rynku): cost 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 → 14.3 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_CAA-04_HERESY_PLUS1` | CAA-04 (Fałszywy Trop): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_CAA-06_COST_MINUS1` | CAA-06 (Ucieczka z Lochów): cost 2 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 1 → 2 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 → 14.3 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_CAA-07_COST_MINUS1` | CAA-07 (Szantaż Bractwa): cost 1 → 0 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_CAA-07_HERESY_PLUS1` | CAA-07 (Szantaż Bractwa): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_CAA-08_COST_PLUS1` | CAA-08 (Kaptur Nocy): cost 2 → 3 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_CAA-08_COST_MINUS1` | CAA-08 (Kaptur Nocy): cost 2 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 → 14.3 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_CAA-08_HERESY_PLUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 2 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_CAA-08_HERESY_MINUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 0 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_CAA-11_COST_MINUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 0 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_CAA-11_HERESY_PLUS1` | CAA-11 (Nocna Zmiana Warty): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_GC-01_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): heresy 1 → 2 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_GC-01_HERESY_MINUS1` | GC-01 (Przekupiony Strażnik): heresy 1 → 0 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_GC-03_HERESY_PLUS1` | GC-03 (Podrzucenie Księgi): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_GC-05_COST_PLUS1` | GC-05 (Fałszywy Świadek): cost 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_GC-05_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_GC-07_HERESY_PLUS1` | GC-07 (Skrytobójstwo): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_GC-10_HERESY_PLUS1` | GC-10 (Upadek Domu): heresy 2 → 3 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_GC-11_HERESY_PLUS1` | GC-11 (Fałszywe Świadectwo Cechu): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_GC-12_HERESY_PLUS1` | GC-12 (Złodziejski Zwiad): heresy 2 → 3 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_GC-12_HERESY_MINUS1` | GC-12 (Złodziejski Zwiad): heresy 2 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_KB-01_HERESY_PLUS1` | KB-01 (Rozkaz Dworu): heresy 1 → 2 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_KB-01_HERESY_MINUS1` | KB-01 (Rozkaz Dworu): heresy 1 → 0 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_KB-03_HERESY_PLUS1` | KB-03 (Plotka Dworska): heresy 1 → 2 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_KB-03_HERESY_MINUS1` | KB-03 (Plotka Dworska): heresy 1 → 0 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_KB-06_COST_PLUS1` | KB-06 (Areszt Królewski): cost 1 → 2 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_KB-06_HERESY_PLUS1` | KB-06 (Areszt Królewski): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_KB-11_HERESY_PLUS1` | KB-11 (Tajny Emisariusz): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 → 14.3 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_KT-01_HERESY_PLUS1` | KT-01 (Rytuał Przejścia): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_KT-02_HERESY_PLUS1` | KT-02 (Transmutacja Złota): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_KT-04_HERESY_PLUS1` | KT-04 (Zwierciadło Herezji): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_KT-07_HERESY_PLUS1` | KT-07 (Archiwum Ukryte): heresy 1 → 2 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_KT-07_HERESY_MINUS1` | KT-07 (Archiwum Ukryte): heresy 1 → 0 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_KT-08_HERESY_PLUS1` | KT-08 (Areszt Wiedzy): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_KT-09_HERESY_PLUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 2 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_KT-11_COST_PLUS1` | KT-11 (Medytacja Sefirot): cost 1 → 2 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 → 14.3 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_KT-11_HERESY_PLUS1` | KT-11 (Medytacja Sefirot): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_KT-12_HERESY_PLUS1` | KT-12 (Strażnik Archiwum): heresy 1 → 2 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_KT-12_HERESY_MINUS1` | KT-12 (Strażnik Archiwum): heresy 1 → 0 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-01_COST_PLUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 2 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-01_COST_MINUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 0 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-01_HERESY_PLUS1` | SO-01 (Patrol Familiariuszy): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-02_COST_MINUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 0 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-03_COST_PLUS1` | SO-03 (Podejrzenie): cost 2 → 3 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-03_COST_MINUS1` | SO-03 (Podejrzenie): cost 2 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-03_HERESY_PLUS1` | SO-03 (Podejrzenie): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-04_COST_PLUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 2 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-04_HERESY_PLUS1` | SO-04 (Publiczne Ostrzeżenie): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-05_COST_PLUS1` | SO-05 (Wezwanie do Trybunału): cost 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-05_HERESY_PLUS1` | SO-05 (Wezwanie do Trybunału): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-06_COST_PLUS1` | SO-06 (Areszt Trybunalski): cost 2 → 3 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-06_COST_MINUS1` | SO-06 (Areszt Trybunalski): cost 2 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-06_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-07_COST_PLUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 3 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-07_COST_MINUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-07_HERESY_PLUS1` | SO-07 (Przesłuchanie Oficjum): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-08_COST_PLUS1` | SO-08 (Nasłanie Inkwizytora): cost 1 → 2 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-08_HERESY_PLUS1` | SO-08 (Nasłanie Inkwizytora): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-09_COST_PLUS1` | SO-09 (Świadek Koronny): cost 2 → 3 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-09_COST_MINUS1` | SO-09 (Świadek Koronny): cost 2 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-09_HERESY_PLUS1` | SO-09 (Świadek Koronny): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-11_HERESY_PLUS1` | SO-11 (Dekret Czystości Wiary): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 → 10.4 (`-0.1`) | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-12_COST_PLUS1` | SO-12 (Straż Trybunalska): cost 1 → 2 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-12_HERESY_PLUS1` | SO-12 (Straż Trybunalska): heresy 0 → 1 | 🔴 **  9.4** | 3.3 | 10.5 | 14.4 | ⚪ OPTYMALNY |
| `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 1 → 2 | 9.4 → 🔴 **  9.3** (`-0.1`) | 3.3 | 10.5 | 14.4 → 14.2 (`-0.2`) | ⚪ OPTYMALNY |
| `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 9.4 → 🔴 **  9.3** (`-0.1`) | 3.3 | 10.5 → 10.2 (`-0.3`) | 14.4 | ⚪ OPTYMALNY |
| `L3_CAA-09_COST_PLUS1` | CAA-09 (Kurier Relikwii): cost 2 → 3 | 9.4 → 🔴 **  9.3** (`-0.1`) | 3.3 | 10.5 | 14.4 → 14.1 (`-0.3`) | ⚪ OPTYMALNY |
| `L3_CAA-09_HERESY_PLUS1` | CAA-09 (Kurier Relikwii): heresy 0 → 1 | 9.4 → 🔴 **  9.3** (`-0.1`) | 3.3 | 10.5 → 10.2 (`-0.3`) | 14.4 | ⚪ OPTYMALNY |
| `L3_GC-06_COST_MINUS1` | GC-06 (Szantaż): cost 2 → 1 | 9.4 → 🔴 **  9.3** (`-0.1`) | 3.3 | 10.5 → 10.3 (`-0.2`) | 14.4 → 14.2 (`-0.2`) | ⚪ OPTYMALNY |
| `L3_KT-01_COST_MINUS1` | KT-01 (Rytuał Przejścia): cost 1 → 0 | 9.4 → 🔴 **  9.3** (`-0.1`) | 3.3 | 10.5 | 14.4 → 14.1 (`-0.3`) | ⚪ OPTYMALNY |
| `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 9.4 → 🔴 **  9.3** (`-0.1`) | 3.3 | 10.5 → 10.4 (`-0.1`) | 14.4 → 14.2 (`-0.2`) | ⚪ OPTYMALNY |
| `L3_KT-04_COST_MINUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 0 | 9.4 → 🔴 **  9.3** (`-0.1`) | 3.3 | 10.5 | 14.4 → 14.0 (`-0.4`) | ⚪ OPTYMALNY |
| `L3_KT-07_COST_PLUS1` | KT-07 (Archiwum Ukryte): cost 1 → 2 | 9.4 → 🔴 **  9.3** (`-0.1`) | 3.3 | 10.5 → 10.4 (`-0.1`) | 14.4 → 14.1 (`-0.3`) | ⚪ OPTYMALNY |
| `L3_KT-08_COST_PLUS1` | KT-08 (Areszt Wiedzy): cost 1 → 2 | 9.4 → 🔴 **  9.3** (`-0.1`) | 3.3 | 10.5 → 10.4 (`-0.1`) | 14.4 → 14.1 (`-0.3`) | ⚪ OPTYMALNY |
| `L3_KT-08_COST_MINUS1` | KT-08 (Areszt Wiedzy): cost 1 → 0 | 9.4 → 🔴 **  9.3** (`-0.1`) | 3.3 | 10.5 | 14.4 → 14.0 (`-0.4`) | ⚪ OPTYMALNY |
| `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 2 → 3 | 9.4 → 🔴 **  9.3** (`-0.1`) | 3.3 | 10.5 → 10.4 (`-0.1`) | 14.4 → 14.1 (`-0.3`) | ⚪ OPTYMALNY |
| `L3_KT-11_COST_MINUS1` | KT-11 (Medytacja Sefirot): cost 1 → 0 | 9.4 → 🔴 **  9.3** (`-0.1`) | 3.3 | 10.5 | 14.4 → 14.0 (`-0.4`) | ⚪ OPTYMALNY |
| `L3_KT-12_COST_PLUS1` | KT-12 (Strażnik Archiwum): cost 0 → 1 | 9.4 → 🔴 **  9.3** (`-0.1`) | 3.3 | 10.5 → 10.4 (`-0.1`) | 14.4 → 14.3 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 9.4 → 🔴 **  9.3** (`-0.1`) | 3.3 | 10.5 | 14.4 → 14.2 (`-0.2`) | ⚪ OPTYMALNY |
| `L3_SO-12_COST_MINUS1` | SO-12 (Straż Trybunalska): cost 1 → 0 | 9.4 → 🔴 **  9.3** (`-0.1`) | 3.3 | 10.5 → 10.4 (`-0.1`) | 14.4 → 14.3 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_CAA-05_COST_MINUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 | 9.4 → 🔴 **  9.2** (`-0.2`) | 3.3 | 10.5 → 10.4 (`-0.1`) | 14.4 → 13.9 (`-0.5`) | ⚪ OPTYMALNY |
| `L3_GC-04_COST_PLUS1` | GC-04 (Informator): cost 1 → 2 | 9.4 → 🔴 **  9.2** (`-0.2`) | 3.3 → 3.2 (`-0.1`) | 10.5 → 10.3 (`-0.2`) | 14.4 → 14.1 (`-0.3`) | ⚪ OPTYMALNY |
| `L3_GC-07_COST_PLUS1` | GC-07 (Skrytobójstwo): cost 2 → 3 | 9.4 → 🔴 **  9.2** (`-0.2`) | 3.3 | 10.5 → 10.3 (`-0.2`) | 14.4 → 13.9 (`-0.5`) | ⚪ OPTYMALNY |
| `L3_GC-08_COST_MINUS1` | GC-08 (Zatrute Złoto): cost 2 → 1 | 9.4 → 🔴 **  9.2** (`-0.2`) | 3.3 | 10.5 → 10.4 (`-0.1`) | 14.4 → 13.8 (`-0.6`) | ⚪ OPTYMALNY |
| `L3_GC-11_COST_MINUS1` | GC-11 (Fałszywe Świadectwo Cechu): cost 1 → 0 | 9.4 → 🔴 **  9.2** (`-0.2`) | 3.3 | 10.5 → 10.3 (`-0.2`) | 14.4 → 14.1 (`-0.3`) | ⚪ OPTYMALNY |
| `L3_KT-04_COST_PLUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 2 | 9.4 → 🔴 **  9.2** (`-0.2`) | 3.3 | 10.5 | 14.4 → 13.9 (`-0.5`) | ⚪ OPTYMALNY |
| `L3_KT-07_COST_MINUS1` | KT-07 (Archiwum Ukryte): cost 1 → 0 | 9.4 → 🔴 **  9.2** (`-0.2`) | 3.3 | 10.5 | 14.4 → 13.7 (`-0.7`) | ⚪ OPTYMALNY |
| `L3_SO-11_COST_PLUS1` | SO-11 (Dekret Czystości Wiary): cost 1 → 2 | 9.4 → 🔴 **  9.2** (`-0.2`) | 3.3 | 10.5 → 10.4 (`-0.1`) | 14.4 → 14.0 (`-0.4`) | ⚪ OPTYMALNY |
| `L3_CAA-10_COST_PLUS1` | CAA-10 (Echo Alhambry): cost 1 → 2 | 9.4 → 🔴 **  9.1** (`-0.3`) | 3.3 → 3.1 (`-0.2`) | 10.5 → 10.1 (`-0.4`) | 14.4 → 14.2 (`-0.2`) | ⚪ OPTYMALNY |
| `L3_GC-03_COST_MINUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 0 | 9.4 → 🔴 **  9.1** (`-0.3`) | 3.3 | 10.5 → 10.2 (`-0.3`) | 14.4 → 13.8 (`-0.6`) | ⚪ OPTYMALNY |
| `L3_GC-11_COST_PLUS1` | GC-11 (Fałszywe Świadectwo Cechu): cost 1 → 2 | 9.4 → 🔴 **  9.1** (`-0.3`) | 3.3 | 10.5 → 10.3 (`-0.2`) | 14.4 → 13.8 (`-0.6`) | ⚪ OPTYMALNY |
| `L3_KB-07_COST_MINUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 1 | 9.4 → 🔴 **  9.1** (`-0.3`) | 3.3 → 3.1 (`-0.2`) | 10.5 → 10.3 (`-0.2`) | 14.4 → 13.8 (`-0.6`) | ⚪ OPTYMALNY |
| `L3_KB-08_COST_MINUS1` | KB-08 (Przekupstwo Sędziego): cost 2 → 1 | 9.4 → 🔴 **  9.1** (`-0.3`) | 3.3 → 3.2 (`-0.1`) | 10.5 → 10.4 (`-0.1`) | 14.4 → 13.6 (`-0.8`) | ⚪ OPTYMALNY |
| `L3_KB-11_COST_PLUS1` | KB-11 (Tajny Emisariusz): cost 1 → 2 | 9.4 → 🔴 **  9.1** (`-0.3`) | 3.3 → 3.2 (`-0.1`) | 10.5 → 10.2 (`-0.3`) | 14.4 → 13.8 (`-0.6`) | ⚪ OPTYMALNY |
| `L3_CAA-12_HERESY_MINUS1` | CAA-12 (Skrytka w Murach): heresy 1 → 0 | 9.4 → 🔴 **  9.0** (`-0.4`) | 3.3 | 10.5 → 10.3 (`-0.2`) | 14.4 → 13.3 (`-1.1`) | ⚪ OPTYMALNY |
| `L3_GC-04_COST_MINUS1` | GC-04 (Informator): cost 1 → 0 | 9.4 → 🔴 **  9.0** (`-0.4`) | 3.3 → 3.2 (`-0.1`) | 10.5 → 10.3 (`-0.2`) | 14.4 → 13.6 (`-0.8`) | ⚪ OPTYMALNY |
| `L3_KB-01_COST_PLUS1` | KB-01 (Rozkaz Dworu): cost 1 → 2 | 9.4 → 🔴 **  9.0** (`-0.4`) | 3.3 | 10.5 | 14.4 → 13.1 (`-1.3`) | ⚪ OPTYMALNY |
| `L3_KB-08_HERESY_PLUS1` | KB-08 (Przekupstwo Sędziego): heresy 0 → 1 | 9.4 → 🔴 **  9.0** (`-0.4`) | 3.3 → 3.2 (`-0.1`) | 10.5 → 9.5 (`-1.0`) | 14.4 | ⚪ OPTYMALNY |
| `L3_SO-04_COST_MINUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 0 | 9.4 → 🔴 **  9.0** (`-0.4`) | 3.3 | 10.5 → 9.9 (`-0.6`) | 14.4 → 13.7 (`-0.7`) | ⚪ OPTYMALNY |
| `L3_KT-03_HERESY_PLUS1` | KT-03 (Zakazana Wiedza): heresy 1 → 2 | 9.4 → 🔴 **  8.9** (`-0.5`) | 3.3 → 2.9 (`-0.4`) | 10.5 → 9.9 (`-0.6`) | 14.4 → 13.9 (`-0.5`) | ⚪ OPTYMALNY |
| `L3_SO-10_COST_MINUS1` | SO-10 (Oczyść Miasto): cost 5 → 4 | 9.4 → 🔴 **  8.9** (`-0.5`) | 3.3 | 10.5 → 10.3 (`-0.2`) | 14.4 → 13.1 (`-1.3`) | ⚪ OPTYMALNY |
| `L3_GC-02_COST_PLUS1` | GC-02 (Czarny Rynek): cost 1 → 2 | 9.4 → 🔴 **  8.8** (`-0.6`) | 3.3 | 10.5 → 9.4 (`-1.1`) | 14.4 → 13.6 (`-0.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_COST_PLUS1` | KB-10 (Pieczęć Korony): cost 2 → 3 | 9.4 → 🔴 **  8.8** (`-0.6`) | 3.3 → 2.5 (`-0.8`) | 10.5 → 9.5 (`-1.0`) | 14.4 → 14.3 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_COST_PLUS1` | KB-08 (Przekupstwo Sędziego): cost 2 → 3 | 9.4 → 🔴 **  8.7** (`-0.7`) | 3.3 | 10.5 → 9.0 (`-1.5`) | 14.4 → 13.7 (`-0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_HERESY_MINUS1` | CAA-10 (Echo Alhambry): heresy 1 → 0 | 9.4 → 🔴 **  8.6** (`-0.8`) | 3.3 | 10.5 → 9.9 (`-0.6`) | 14.4 → 12.6 (`-1.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_HERESY_MINUS1` | GC-02 (Czarny Rynek): heresy 1 → 0 | 9.4 → 🔴 **  8.6** (`-0.8`) | 3.3 → 3.2 (`-0.1`) | 10.5 → 9.1 (`-1.4`) | 14.4 → 13.6 (`-0.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_HERESY_MINUS1` | GC-10 (Upadek Domu): heresy 2 → 1 | 9.4 → 🔴 **  8.6** (`-0.8`) | 3.3 → 3.2 (`-0.1`) | 10.5 → 9.3 (`-1.2`) | 14.4 → 13.2 (`-1.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_COST_MINUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 1 | 9.4 → 🔴 **  8.6** (`-0.8`) | 3.3 → 2.8 (`-0.5`) | 10.5 → 9.7 (`-0.8`) | 14.4 → 13.3 (`-1.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_COST_MINUS1` | KT-10 (Pieczęć Salomona): cost 2 → 1 | 9.4 → 🔴 **  8.6** (`-0.8`) | 3.3 → 2.8 (`-0.5`) | 10.5 → 9.7 (`-0.8`) | 14.4 → 13.3 (`-1.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_COST_PLUS1` | KT-03 (Zakazana Wiedza): cost 0 → 1 | 9.4 → 🔴 **  8.4** (`-1.0`) | 3.3 → 2.8 (`-0.5`) | 10.5 → 9.2 (`-1.3`) | 14.4 → 13.3 (`-1.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_HERESY_MINUS1` | GC-04 (Informator): heresy 1 → 0 | 9.4 → 🔴 **  8.3** (`-1.1`) | 3.3 → 3.2 (`-0.1`) | 10.5 → 9.1 (`-1.4`) | 14.4 → 12.7 (`-1.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_COST_MINUS1` | KB-04 (Faworyt Dworu): cost 2 → 1 | 9.4 → 🔴 **  8.3** (`-1.1`) | 3.3 → 2.7 (`-0.6`) | 10.5 → 10.1 (`-0.4`) | 14.4 → 12.2 (`-2.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_HERESY_PLUS1` | KB-12 (Szantaż Salonowy): heresy 0 → 1 | 9.4 → 🔴 **  8.1** (`-1.3`) | 3.3 → 2.8 (`-0.5`) | 10.5 → 8.7 (`-1.8`) | 14.4 → 12.7 (`-1.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_COST_PLUS1` | KB-12 (Szantaż Salonowy): cost 1 → 2 | 9.4 → 🔴 **  8.0** (`-1.4`) | 3.3 | 10.5 → 9.9 (`-0.6`) | 14.4 → 10.8 (`-3.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_HERESY_MINUS1` | KT-10 (Pieczęć Salomona): heresy 1 → 0 | 9.4 → 🔴 **  8.0** (`-1.4`) | 3.3 → 2.7 (`-0.6`) | 10.5 → 8.9 (`-1.6`) | 14.4 → 12.4 (`-2.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_COST_PLUS1` | CAA-06 (Ucieczka z Lochów): cost 2 → 3 | 9.4 → 🔴 **  7.8** (`-1.6`) | 3.3 → 3.2 (`-0.1`) | 10.5 → 8.7 (`-1.8`) | 14.4 → 11.5 (`-2.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_HERESY_PLUS1` | CAA-06 (Ucieczka z Lochów): heresy 1 → 2 | 9.4 → 🔴 **  7.8** (`-1.6`) | 3.3 → 3.2 (`-0.1`) | 10.5 → 8.8 (`-1.7`) | 14.4 → 11.5 (`-2.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-12_COST_PLUS1` | CAA-12 (Skrytka w Murach): cost 0 → 1 | 9.4 → 🔴 **  7.8** (`-1.6`) | 3.3 → 3.2 (`-0.1`) | 10.5 → 9.2 (`-1.3`) | 14.4 → 11.1 (`-3.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_HERESY_PLUS1` | KB-10 (Pieczęć Korony): heresy 2 → 3 | 9.4 → 🔴 **  6.5** (`-2.9`) | 3.3 → 1.1 (`-2.2`) | 10.5 → 4.3 (`-6.2`) | 14.4 → 14.1 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_COST_PLUS1` | KB-09 (Dekret Królewski): cost 3 → 4 | 9.4 → 🔴 **  6.1** (`-3.3`) | 3.3 → 1.2 (`-2.1`) | 10.5 → 5.6 (`-4.9`) | 14.4 → 11.4 (`-3.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_HERESY_PLUS1` | KB-09 (Dekret Królewski): heresy 1 → 2 | 9.4 → 🔴 **  4.4** (`-5.0`) | 3.3 → 1.1 (`-2.2`) | 10.5 → 3.3 (`-7.2`) | 14.4 → 8.8 (`-5.6`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (67)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-09_HERESY_MINUS1` | 6.56 Er (2–12) | 14.1% | 0.8% | 2.03 (0–5) | 5.55 (0–26) | 18.07zł (1.3–44.3) | 6.29 (1.3–10.0) | 🟢 W NORMIE |
| `L3_KT-09_COST_MINUS1` | 6.67 Er (2–12) | 13.8% | 0.8% | 2.07 (0–5) | 5.86 (0–27) | 18.57zł (1.7–44.3) | 6.40 (1.4–10.0) | 🟢 W NORMIE |
| `L3_KT-10_COST_PLUS1` | 7.01 Er (2–12) | 16.8% | 0.8% | 2.18 (0–5) | 6.24 (0–26) | 19.89zł (1.3–44.3) | 6.52 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-05_COST_MINUS1` | 7.07 Er (2–12) | 17.0% | 0.7% | 2.19 (0–5) | 6.34 (0–26) | 20.30zł (1.7–44.3) | 6.54 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-10_HERESY_PLUS1` | 7.04 Er (2–12) | 15.6% | 0.7% | 2.18 (0–5) | 6.56 (0–27) | 20.07zł (1.7–44.3) | 6.61 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-02_COST_MINUS1` | 7.10 Er (2–12) | 16.9% | 0.7% | 2.20 (0–5) | 6.43 (0–26) | 20.29zł (1.7–44.3) | 6.57 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-03_HERESY_MINUS1` | 7.17 Er (2–12) | 18.2% | 0.7% | 2.22 (0–5) | 6.36 (0–26) | 20.50zł (1.7–44.3) | 6.53 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-02_COST_MINUS1` | 7.18 Er (2–12) | 17.2% | 0.7% | 2.21 (0–5) | 6.57 (0–26) | 20.54zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-09_HERESY_PLUS1` | 7.21 Er (2–12) | 17.5% | 0.7% | 2.23 (0–5) | 6.77 (0–26) | 20.61zł (1.7–44.3) | 6.70 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-02_HERESY_PLUS1` | 7.20 Er (2–12) | 17.3% | 0.7% | 2.23 (0–5) | 6.75 (0–26) | 20.58zł (1.7–44.3) | 6.69 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-04_HERESY_PLUS1` | 7.21 Er (2–12) | 17.4% | 0.7% | 2.23 (0–5) | 6.74 (0–26) | 20.60zł (1.7–44.3) | 6.68 (1.6–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-06_HERESY_MINUS1` | 7.16 Er (2–12) | 16.5% | 0.7% | 2.24 (0–5) | 6.44 (0–26) | 20.17zł (1.7–44.3) | 6.59 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-06_HERESY_PLUS1` | 7.21 Er (2–12) | 17.5% | 0.7% | 2.23 (0–5) | 6.74 (0–26) | 20.64zł (1.7–44.3) | 6.69 (1.6–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-05_HERESY_PLUS1` | 7.19 Er (2–12) | 17.2% | 0.7% | 2.22 (0–5) | 6.67 (0–26) | 20.60zł (1.3–44.3) | 6.65 (1.6–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-06_COST_PLUS1` | 7.21 Er (2–12) | 17.7% | 0.8% | 2.23 (0–5) | 6.55 (0–27) | 20.52zł (1.0–44.3) | 6.60 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-04_COST_MINUS1` | 7.23 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.65 (0–27) | 20.63zł (1.7–44.3) | 6.64 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-10_COST_MINUS1` | 7.07 Er (2–12) | 17.0% | 0.8% | 2.19 (0–5) | 6.67 (0–26) | 19.65zł (0.7–44.0) | 6.72 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-11_COST_MINUS1` | 7.24 Er (2–12) | 17.2% | 0.7% | 2.27 (0–5) | 6.78 (0–27) | 20.70zł (1.7–44.3) | 6.67 (1.6–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-03_HERESY_PLUS1` | 7.23 Er (2–12) | 17.5% | 0.7% | 2.24 (0–5) | 6.74 (0–27) | 20.72zł (1.7–44.3) | 6.67 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-04_HERESY_MINUS1` | 7.26 Er (2–12) | 18.1% | 0.8% | 2.25 (0–5) | 6.52 (0–27) | 20.61zł (1.3–44.3) | 6.61 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-03_COST_MINUS1` | 7.24 Er (2–12) | 17.7% | 0.4% | 2.24 (0–5) | 6.67 (0–26) | 20.71zł (1.7–44.3) | 6.64 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-05_COST_PLUS1` | 7.21 Er (2–12) | 17.5% | 0.8% | 2.23 (0–5) | 6.56 (0–26) | 20.55zł (1.3–44.3) | 6.61 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-09_COST_MINUS1` | 7.22 Er (2–12) | 17.5% | 0.7% | 2.24 (0–5) | 6.60 (0–27) | 20.65zł (1.7–43.7) | 6.63 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-05_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.62zł (1.3–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-08_COST_MINUS1` | 7.24 Er (2–12) | 17.7% | 0.7% | 2.27 (0–5) | 6.66 (0–26) | 20.53zł (1.7–44.0) | 6.65 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-06_COST_MINUS1` | 7.23 Er (2–12) | 17.7% | 0.4% | 2.24 (0–5) | 6.60 (0–26) | 20.69zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-01_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.8% | 2.24 (0–5) | 6.61 (0–26) | 20.72zł (0.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-06_COST_PLUS1` | 7.26 Er (2–12) | 17.9% | 0.8% | 2.25 (0–5) | 6.62 (0–26) | 20.65zł (1.3–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-01_COST_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.4% | 2.24 (0–5) | 6.61 (0–26) | 20.70zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-02_COST_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.62 (0–26) | 20.82zł (1.7–44.7) | 6.63 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-03_COST_PLUS1` | 7.25 Er (2–12) | 17.9% | 0.8% | 2.24 (0–5) | 6.63 (0–26) | 20.75zł (1.7–44.3) | 6.63 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-05_HERESY_PLUS1` | 7.23 Er (2–12) | 17.1% | 0.7% | 2.23 (0–5) | 6.72 (0–27) | 20.67zł (1.7–44.3) | 6.65 (1.6–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-12_HERESY_PLUS1` | 7.22 Er (2–12) | 17.6% | 0.7% | 2.23 (0–5) | 6.70 (0–27) | 20.68zł (1.3–44.3) | 6.65 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-08_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.72zł (1.7–44.3) | 6.63 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-04_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-11_COST_PLUS1` | 7.24 Er (2–12) | 17.9% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.72zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-01_COST_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.70zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-09_COST_MINUS1` | 7.24 Er (2–12) | 17.9% | 0.8% | 2.24 (0–5) | 6.62 (0–26) | 20.84zł (1.0–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-10_HERESY_MINUS1` | 7.25 Er (2–12) | 18.3% | 0.7% | 2.26 (0–5) | 6.57 (0–26) | 20.71zł (1.7–44.3) | 6.52 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-10_HERESY_PLUS1` | 7.26 Er (2–12) | 18.5% | 0.7% | 1.94 (0–4) | 6.55 (0–26) | 21.30zł (1.7–44.3) | 6.42 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-07_COST_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.70zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-09_COST_PLUS1` | 7.27 Er (2–12) | 18.0% | 1.2% | 2.25 (0–5) | 6.63 (0–26) | 20.68zł (0.3–44.3) | 6.61 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-10_COST_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.83zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-12_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.8% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-10_COST_PLUS1` | 7.27 Er (2–12) | 18.7% | 0.7% | 1.94 (0–4) | 6.57 (0–26) | 21.33zł (1.7–44.3) | 6.43 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-11_COST_MINUS1` | 7.09 Er (2–12) | 16.8% | 0.6% | 2.19 (0–5) | 6.46 (0–27) | 20.10zł (0.7–44.3) | 6.58 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-10_HERESY_PLUS1` | 7.23 Er (2–12) | 17.6% | 0.7% | 2.22 (0–5) | 7.00 (0–28) | 20.72zł (1.3–44.3) | 6.72 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-03_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.8% | 2.24 (0–5) | 6.60 (0–26) | 20.72zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-06_HERESY_PLUS1` | 7.21 Er (2–12) | 17.0% | 0.7% | 2.23 (0–5) | 6.73 (0–26) | 20.61zł (1.7–44.3) | 6.65 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-05_HERESY_PLUS1` | 7.31 Er (2–12) | 17.8% | 0.7% | 2.26 (0–5) | 6.80 (0–27) | 20.96zł (1.7–44.3) | 6.68 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-10_COST_PLUS1` | 7.24 Er (2–12) | 17.7% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-07_HERESY_PLUS1` | 7.29 Er (2–12) | 18.5% | 0.7% | 2.26 (0–5) | 6.60 (0–26) | 21.20zł (1.7–44.3) | 6.59 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-04_HERESY_PLUS1` | 7.13 Er (2–12) | 17.4% | 0.6% | 2.21 (0–5) | 6.44 (0–27) | 20.51zł (0.7–44.3) | 6.55 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-07_COST_PLUS1` | 7.29 Er (2–12) | 18.5% | 0.7% | 2.27 (0–5) | 6.60 (0–26) | 21.21zł (1.7–44.3) | 6.59 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-05_COST_MINUS1` | 7.13 Er (2–12) | 17.1% | 0.6% | 2.20 (0–5) | 6.48 (0–27) | 20.49zł (0.3–44.3) | 6.55 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-02_HERESY_PLUS1` | 7.24 Er (2–12) | 17.5% | 0.7% | 2.21 (0–5) | 6.62 (0–26) | 20.80zł (1.7–44.3) | 6.75 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-05_COST_PLUS1` | 7.32 Er (2–12) | 18.1% | 0.7% | 2.27 (0–5) | 6.68 (0–27) | 20.89zł (1.7–44.3) | 6.66 (1.6–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-12_COST_MINUS1` | 7.15 Er (2–12) | 17.4% | 0.6% | 2.21 (0–5) | 6.52 (0–27) | 20.53zł (1.2–44.3) | 6.58 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-02_COST_MINUS1` | 7.08 Er (2–12) | 17.3% | 0.5% | 2.18 (0–5) | 6.43 (0–26) | 20.32zł (0.7–44.3) | 6.53 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-02_COST_PLUS1` | 7.41 Er (2–12) | 19.0% | 0.8% | 2.31 (0–5) | 6.70 (0–26) | 21.31zł (0.7–44.3) | 6.63 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-10_COST_MINUS1` | 6.73 Er (1–12) | 16.2% | 0.6% | 2.06 (0–5) | 6.09 (0–26) | 19.36zł (0.0–44.3) | 6.33 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-02_HERESY_PLUS1` | 7.41 Er (2–12) | 18.1% | 0.7% | 2.30 (0–5) | 6.96 (0–27) | 21.28zł (1.3–44.3) | 6.73 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-09_COST_MINUS1` | 6.88 Er (1–12) | 17.0% | 0.9% | 2.10 (0–5) | 6.26 (0–26) | 19.82zł (0.0–44.3) | 6.35 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-04_COST_PLUS1` | 7.12 Er (2–12) | 17.5% | 0.6% | 2.21 (0–5) | 6.29 (0–27) | 20.62zł (0.7–44.3) | 6.51 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-10_HERESY_MINUS1` | 6.55 Er (2–12) | 14.9% | 0.9% | 2.02 (0–5) | 5.29 (0–27) | 18.44zł (0.7–44.3) | 6.12 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-09_HERESY_MINUS1` | 6.32 Er (2–12) | 14.2% | 1.0% | 1.95 (0–5) | 4.89 (0–26) | 17.73zł (0.7–44.3) | 5.95 (1.0–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 127 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_CAA-01_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-01_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-02_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-03_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.58zł (1.3–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-04_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-06_COST_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.73zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-07_COST_PLUS1` | 7.24 Er (2–12) | 17.9% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-07_COST_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-07_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-08_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-08_COST_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-08_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-08_HERESY_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-11_COST_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-11_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-01_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-01_HERESY_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-03_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-05_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.62zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-05_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-07_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-08_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-10_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-11_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-12_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-12_HERESY_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-01_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-01_HERESY_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-03_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-03_HERESY_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-06_COST_PLUS1` | 7.25 Er (2–12) | 17.8% | 0.8% | 2.24 (0–5) | 6.62 (0–26) | 20.73zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-06_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-11_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-01_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-01_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-02_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-04_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-07_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-07_HERESY_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-08_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-09_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-11_COST_PLUS1` | 7.24 Er (2–12) | 17.9% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-11_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-12_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-12_HERESY_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-01_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-01_COST_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-01_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-02_COST_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.81zł (1.7–44.7) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-03_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-03_COST_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-03_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-04_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-04_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-05_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.62zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-05_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-06_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-06_COST_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-06_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-07_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-07_COST_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-07_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-08_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-08_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-09_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-09_COST_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-09_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-11_HERESY_PLUS1` | 7.24 Er (2–12) | 17.7% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.70zł (1.7–44.3) | 6.65 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-12_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-12_HERESY_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-02_COST_PLUS1` | 7.24 Er (2–12) | 17.9% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.72zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-03_HERESY_MINUS1` | 7.28 Er (2–12) | 18.3% | 0.7% | 2.26 (0–5) | 6.52 (0–26) | 20.83zł (1.7–44.3) | 6.57 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-09_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.8% | 2.24 (0–5) | 6.61 (0–26) | 20.62zł (1.3–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-09_HERESY_PLUS1` | 7.21 Er (2–12) | 17.6% | 0.7% | 2.22 (0–5) | 6.82 (0–27) | 20.72zł (1.7–44.3) | 6.69 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-06_COST_MINUS1` | 7.25 Er (2–12) | 17.8% | 0.8% | 2.24 (0–5) | 6.63 (0–26) | 20.85zł (1.0–44.3) | 6.63 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-01_COST_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-02_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-04_COST_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.70zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-07_COST_PLUS1` | 7.24 Er (2–12) | 17.9% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.72zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-08_COST_PLUS1` | 7.24 Er (2–12) | 17.9% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.72zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-08_COST_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-09_COST_PLUS1` | 7.24 Er (2–12) | 17.7% | 0.7% | 2.24 (0–5) | 6.59 (0–27) | 20.70zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-11_COST_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-12_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.8% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-02_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.61zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-12_COST_MINUS1` | 7.23 Er (2–12) | 17.4% | 0.7% | 2.27 (0–5) | 6.66 (0–26) | 20.61zł (1.7–44.3) | 6.67 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-05_COST_MINUS1` | 7.25 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.62 (0–26) | 20.84zł (1.7–44.3) | 6.63 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-04_COST_PLUS1` | 7.24 Er (2–12) | 17.9% | 0.7% | 2.24 (0–5) | 6.59 (0–26) | 20.59zł (0.3–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-07_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-08_COST_MINUS1` | 7.23 Er (2–12) | 17.7% | 0.7% | 2.24 (0–5) | 6.64 (0–26) | 20.62zł (1.7–44.3) | 6.64 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-11_COST_MINUS1` | 7.23 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.62 (0–26) | 20.62zł (1.7–44.3) | 6.64 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-04_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-07_COST_MINUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-11_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.58 (0–26) | 20.76zł (1.7–44.3) | 6.61 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-10_COST_PLUS1` | 7.26 Er (2–12) | 18.0% | 0.8% | 2.25 (0–5) | 6.64 (0–26) | 20.68zł (1.3–44.3) | 6.63 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-03_COST_MINUS1` | 7.23 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.62 (0–26) | 20.62zł (1.7–44.3) | 6.64 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-11_COST_PLUS1` | 7.24 Er (2–12) | 17.8% | 0.8% | 2.24 (0–5) | 6.60 (0–26) | 20.71zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-07_COST_MINUS1` | 7.27 Er (2–12) | 17.6% | 0.9% | 2.25 (0–5) | 6.74 (0–27) | 20.92zł (1.0–44.3) | 6.73 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-08_COST_MINUS1` | 7.28 Er (2–12) | 17.6% | 0.9% | 2.26 (0–5) | 6.77 (0–27) | 20.95zł (0.7–44.3) | 6.74 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-11_COST_PLUS1` | 7.25 Er (2–12) | 17.9% | 0.8% | 2.24 (0–5) | 6.63 (0–26) | 20.73zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-12_HERESY_MINUS1` | 7.27 Er (2–12) | 18.2% | 0.7% | 2.25 (0–5) | 6.55 (0–26) | 20.80zł (1.7–44.3) | 6.58 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-04_COST_MINUS1` | 7.23 Er (2–12) | 17.8% | 0.7% | 2.24 (0–5) | 6.62 (0–26) | 20.80zł (1.7–44.3) | 6.63 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-01_COST_PLUS1` | 7.24 Er (2–12) | 17.9% | 0.8% | 2.24 (0–5) | 6.64 (0–26) | 20.72zł (0.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-08_HERESY_PLUS1` | 7.28 Er (2–12) | 18.4% | 0.7% | 2.26 (0–5) | 6.60 (0–26) | 21.16zł (1.7–44.3) | 6.59 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-04_COST_MINUS1` | 7.24 Er (2–12) | 17.4% | 0.7% | 2.27 (0–5) | 6.67 (0–26) | 20.54zł (1.7–44.3) | 6.66 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-03_HERESY_PLUS1` | 7.28 Er (2–12) | 17.4% | 0.7% | 2.25 (0–5) | 6.80 (0–26) | 20.83zł (1.7–44.3) | 6.67 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-10_COST_MINUS1` | 7.24 Er (2–12) | 17.9% | 0.7% | 2.24 (0–5) | 6.61 (0–26) | 20.80zł (1.7–44.3) | 6.62 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-02_COST_PLUS1` | 7.29 Er (2–12) | 18.5% | 0.7% | 2.26 (0–5) | 6.53 (0–26) | 20.89zł (1.3–44.3) | 6.55 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-10_COST_PLUS1` | 7.42 Er (2–12) | 19.3% | 0.7% | 2.29 (0–5) | 6.78 (0–26) | 21.20zł (1.2–44.3) | 6.70 (1.6–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-08_COST_PLUS1` | 7.27 Er (2–12) | 18.3% | 0.7% | 2.26 (0–5) | 6.59 (0–26) | 21.14zł (1.7–44.3) | 6.59 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-10_HERESY_MINUS1` | 7.31 Er (2–12) | 18.7% | 0.7% | 2.27 (0–5) | 6.45 (0–26) | 20.88zł (1.7–44.3) | 6.52 (1.0–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-02_HERESY_MINUS1` | 7.26 Er (2–12) | 18.1% | 0.7% | 2.25 (0–5) | 6.50 (0–26) | 20.80zł (1.7–44.3) | 6.56 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-10_HERESY_MINUS1` | 7.12 Er (2–12) | 17.3% | 0.8% | 2.21 (0–5) | 6.52 (0–26) | 19.84zł (0.7–44.0) | 6.64 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-06_COST_MINUS1` | 7.31 Er (2–12) | 18.1% | 0.7% | 2.26 (0–5) | 6.72 (0–26) | 21.03zł (1.7–44.3) | 6.65 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-10_COST_MINUS1` | 7.31 Er (2–12) | 18.1% | 0.7% | 2.26 (0–5) | 6.72 (0–26) | 21.03zł (1.7–44.3) | 6.65 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-03_COST_PLUS1` | 7.32 Er (2–12) | 18.2% | 0.8% | 2.27 (0–5) | 6.74 (0–26) | 20.88zł (1.3–44.3) | 6.66 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-04_HERESY_MINUS1` | 7.27 Er (2–12) | 18.2% | 0.7% | 2.25 (0–5) | 6.51 (0–26) | 20.80zł (1.7–44.3) | 6.56 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-04_COST_MINUS1` | 7.32 Er (2–12) | 17.8% | 0.8% | 2.27 (0–5) | 6.78 (0–27) | 20.93zł (1.7–44.3) | 6.67 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-12_HERESY_PLUS1` | 7.32 Er (2–12) | 17.8% | 0.6% | 2.27 (0–5) | 6.85 (0–26) | 21.08zł (1.3–44.3) | 6.66 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-12_COST_PLUS1` | 7.26 Er (2–12) | 18.1% | 0.5% | 2.25 (0–5) | 6.51 (0–26) | 20.67zł (1.3–44.3) | 6.51 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KT-10_HERESY_MINUS1` | 7.38 Er (2–12) | 20.0% | 0.7% | 2.29 (0–5) | 6.56 (0–26) | 21.21zł (0.7–44.3) | 6.59 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-06_COST_PLUS1` | 7.26 Er (2–12) | 18.3% | 0.7% | 2.25 (0–5) | 6.60 (0–26) | 20.89zł (1.7–44.3) | 6.61 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-06_HERESY_PLUS1` | 7.26 Er (2–12) | 18.3% | 0.7% | 2.25 (0–5) | 6.60 (0–26) | 20.89zł (1.7–44.3) | 6.61 (1.4–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-12_COST_PLUS1` | 7.32 Er (2–12) | 18.4% | 0.7% | 2.28 (0–5) | 6.56 (0–26) | 20.94zł (1.3–44.3) | 6.58 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-10_HERESY_PLUS1` | 7.82 Er (2–12) | 20.0% | 0.6% | 2.41 (0–5) | 8.03 (0–28) | 22.55zł (2.0–44.3) | 7.05 (1.7–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-09_COST_PLUS1` | 7.90 Er (2–12) | 20.3% | 0.9% | 2.45 (0–5) | 7.57 (0–27) | 22.78zł (0.3–44.3) | 6.99 (1.6–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-09_HERESY_PLUS1` | 8.04 Er (2–12) | 19.7% | 0.6% | 2.50 (0–5) | 7.95 (0–27) | 23.28zł (2.0–44.3) | 7.12 (1.7–10.0) | 🔴 PRZEKROCZONE NORMY |

</details>