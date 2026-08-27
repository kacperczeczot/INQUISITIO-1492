# Raport Precyzyjnego Audytu Poziomu 3 (Parametry Pojedynczych Kart) — Wersja Balansu: v0.28

**Wersja Balansu:** `v0.28` | **Data:** 2026-08-14 18:48 | **Przeanalizowano Wariantów Kart:** 158 | **Próba:** 3000 gier/setup | **Czas:** 1110.88s
**Filtry:** Parametry: `cost,heresy` | Frakcja: `all` | Karta: `Wszystkie`
**Wynik Bazy Poziomu 3 (Global):** `🟢 95.8 pkt` | 3p: `90.0 pkt` | 4p: `98.4 pkt` | 5p: `99.1 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (97)

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | Baza (Bieżące parametry wszystkich kart) | 🟢 ** 95.8** | 90.0 | 98.4 | 99.1 | ⚪ OPTYMALNY |
| `L3_CAA-06_HERESY_PLUS1` | CAA-06 (Ucieczka z Lochów): heresy 0 → 1 | 95.8 → 🟢 ** 96.7** (`⬆️ +0.9`) | 90.0 → 92.9 (`⬆️ +2.9`) | 98.4 → 98.0 (`-0.4`) | 99.1 → 99.3 (`⬆️ +0.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-01_COST_MINUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 0 | 95.8 → 🟢 ** 96.2** (`⬆️ +0.4`) | 90.0 → 91.3 (`⬆️ +1.3`) | 98.4 | 99.1 → 99.0 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_CAA-08_COST_MINUS1` | CAA-08 (Kaptur Nocy): cost 1 → 0 | 95.8 → 🟢 ** 96.2** (`⬆️ +0.4`) | 90.0 → 90.6 (`⬆️ +0.6`) | 98.4 | 99.1 → 99.6 (`⬆️ +0.5`) | ⚪ OPTYMALNY |
| `L3_CAA-02_HERESY_PLUS1` | CAA-02 (Złoto z Kryjówki): heresy 0 → 1 | 95.8 → 🟢 ** 96.1** (`⬆️ +0.3`) | 90.0 → 91.3 (`⬆️ +1.3`) | 98.4 → 97.9 (`-0.5`) | 99.1 → 99.2 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_SO-09_COST_MINUS1` | SO-09 (Świadek Koronny): cost 2 → 1 | 95.8 → 🟢 ** 96.1** (`⬆️ +0.3`) | 90.0 → 91.3 (`⬆️ +1.3`) | 98.4 → 98.2 (`-0.2`) | 99.1 → 98.8 (`-0.3`) | ⚪ OPTYMALNY |
| `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 95.8 → 🟢 ** 96.1** (`⬆️ +0.3`) | 90.0 → 90.6 (`⬆️ +0.6`) | 98.4 → 98.2 (`-0.2`) | 99.1 → 99.5 (`⬆️ +0.4`) | ⚪ OPTYMALNY |
| `L3_GC-01_HERESY_MINUS1` | GC-01 (Przekupiony Strażnik): heresy 1 → 0 | 95.8 → 🟢 ** 96.0** (`⬆️ +0.2`) | 90.0 → 91.2 (`⬆️ +1.2`) | 98.4 → 98.0 (`-0.4`) | 99.1 → 98.8 (`-0.3`) | ⚪ OPTYMALNY |
| `L3_GC-07_HERESY_MINUS1` | GC-07 (Skrytobójstwo): heresy 1 → 0 | 95.8 → 🟢 ** 96.0** (`⬆️ +0.2`) | 90.0 → 90.9 (`⬆️ +0.9`) | 98.4 → 98.2 (`-0.2`) | 99.1 → 98.9 (`-0.2`) | ⚪ OPTYMALNY |
| `L3_CAA-01_COST_MINUS1` | CAA-01 (Przejście Podziemiami): cost 1 → 0 | 95.8 → 🟢 ** 96.0** (`⬆️ +0.2`) | 90.0 → 90.2 (`⬆️ +0.2`) | 98.4 → 98.6 (`⬆️ +0.2`) | 99.1 → 99.2 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_CAA-08_HERESY_PLUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 2 | 95.8 → 🟢 ** 95.9** (`⬆️ +0.1`) | 90.0 → 90.9 (`⬆️ +0.9`) | 98.4 → 97.9 (`-0.5`) | 99.1 → 99.0 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_CAA-02_COST_MINUS1` | CAA-02 (Złoto z Kryjówki): cost 1 → 0 | 95.8 → 🟢 ** 95.9** (`⬆️ +0.1`) | 90.0 → 89.8 (`-0.2`) | 98.4 → 98.6 (`⬆️ +0.2`) | 99.1 → 99.4 (`⬆️ +0.3`) | ⚪ OPTYMALNY |
| `L3_KT-01_COST_MINUS1` | KT-01 (Rytuał Przejścia): cost 1 → 0 | 95.8 → 🟢 ** 95.9** (`⬆️ +0.1`) | 90.0 → 89.9 (`-0.1`) | 98.4 | 99.1 → 99.4 (`⬆️ +0.3`) | ⚪ OPTYMALNY |
| `L3_KT-09_COST_MINUS1` | KT-09 (Fragment Kodeksu): cost 1 → 0 | 95.8 → 🟢 ** 95.9** (`⬆️ +0.1`) | 90.0 → 89.8 (`-0.2`) | 98.4 | 99.1 → 99.4 (`⬆️ +0.3`) | ⚪ OPTYMALNY |
| `L3_CAA-05_COST_MINUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 | 95.8 → 🟢 ** 95.9** (`⬆️ +0.1`) | 90.0 → 90.3 (`⬆️ +0.3`) | 98.4 → 98.3 (`-0.1`) | 99.1 → 99.2 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_CAA-06_COST_MINUS1` | CAA-06 (Ucieczka z Lochów): cost 2 → 1 | 95.8 → 🟢 ** 95.9** (`⬆️ +0.1`) | 90.0 → 89.9 (`-0.1`) | 98.4 → 98.6 (`⬆️ +0.2`) | 99.1 → 99.2 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_KT-09_HERESY_MINUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 0 | 🟢 ** 95.8** | 90.0 → 89.7 (`-0.3`) | 98.4 → 98.1 (`-0.3`) | 99.1 → 99.7 (`⬆️ +0.6`) | ⚪ OPTYMALNY |
| `L3_GC-07_HERESY_PLUS1` | GC-07 (Skrytobójstwo): heresy 1 → 2 | 🟢 ** 95.8** | 90.0 → 89.3 (`-0.7`) | 98.4 → 98.7 (`⬆️ +0.3`) | 99.1 → 99.5 (`⬆️ +0.4`) | ⚪ OPTYMALNY |
| `L3_KT-07_COST_MINUS1` | KT-07 (Archiwum Ukryte): cost 1 → 0 | 🟢 ** 95.8** | 90.0 → 89.7 (`-0.3`) | 98.4 → 98.3 (`-0.1`) | 99.1 → 99.5 (`⬆️ +0.4`) | ⚪ OPTYMALNY |
| `L3_CAA-04_COST_MINUS1` | CAA-04 (Fałszywy Trop): cost 1 → 0 | 🟢 ** 95.8** | 90.0 → 89.6 (`-0.4`) | 98.4 | 99.1 → 99.3 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L3_KB-08_HERESY_PLUS1` | KB-08 (Przekupstwo Sędziego): heresy 0 → 1 | 🟢 ** 95.8** | 90.0 → 89.9 (`-0.1`) | 98.4 | 99.1 → 99.2 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_KT-02_COST_MINUS1` | KT-02 (Transmutacja Złota): cost 1 → 0 | 🟢 ** 95.8** | 90.0 → 89.9 (`-0.1`) | 98.4 | 99.1 → 99.2 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_CAA-09_COST_MINUS1` | CAA-09 (Kurier Relikwii): cost 2 → 1 | 🟢 ** 95.8** | 90.0 → 90.1 (`⬆️ +0.1`) | 98.4 → 98.5 (`⬆️ +0.1`) | 99.1 → 98.7 (`-0.4`) | ⚪ OPTYMALNY |
| `L3_CAA-04_HERESY_PLUS1` | CAA-04 (Fałszywy Trop): heresy 0 → 1 | 95.8 → 🟢 ** 95.7** (`-0.1`) | 90.0 → 92.2 (`⬆️ +2.2`) | 98.4 → 96.1 (`-2.3`) | 99.1 → 98.7 (`-0.4`) | ⚪ OPTYMALNY |
| `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 95.8 → 🟢 ** 95.7** (`-0.1`) | 90.0 → 89.0 (`-1.0`) | 98.4 → 98.2 (`-0.2`) | 99.1 → 99.8 (`⬆️ +0.7`) | ⚪ OPTYMALNY |
| `L3_KT-07_COST_PLUS1` | KT-07 (Archiwum Ukryte): cost 1 → 2 | 95.8 → 🟢 ** 95.7** (`-0.1`) | 90.0 → 89.5 (`-0.5`) | 98.4 → 98.2 (`-0.2`) | 99.1 → 99.4 (`⬆️ +0.3`) | ⚪ OPTYMALNY |
| `L3_CAA-01_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 95.8 → 🟢 ** 95.7** (`-0.1`) | 90.0 → 90.2 (`⬆️ +0.2`) | 98.4 → 98.2 (`-0.2`) | 99.1 → 98.6 (`-0.5`) | ⚪ OPTYMALNY |
| `L3_CAA-07_COST_MINUS1` | CAA-07 (Szantaż Bractwa): cost 2 → 1 | 95.8 → 🟢 ** 95.7** (`-0.1`) | 90.0 → 89.4 (`-0.6`) | 98.4 → 98.5 (`⬆️ +0.1`) | 99.1 → 99.3 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L3_KT-08_COST_MINUS1` | KT-08 (Areszt Wiedzy): cost 2 → 1 | 95.8 → 🟢 ** 95.7** (`-0.1`) | 90.0 → 89.6 (`-0.4`) | 98.4 → 98.2 (`-0.2`) | 99.1 → 99.3 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L3_GC-07_COST_PLUS1` | GC-07 (Skrytobójstwo): cost 2 → 3 | 95.8 → 🟢 ** 95.7** (`-0.1`) | 90.0 | 98.4 → 98.0 (`-0.4`) | 99.1 → 99.2 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 1 → 2 | 95.8 → 🟢 ** 95.7** (`-0.1`) | 90.0 → 89.5 (`-0.5`) | 98.4 → 98.3 (`-0.1`) | 99.1 → 99.2 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_SO-06_COST_MINUS1` | SO-06 (Areszt Trybunalski): cost 2 → 1 | 95.8 → 🟢 ** 95.6** (`-0.2`) | 90.0 → 92.1 (`⬆️ +2.1`) | 98.4 → 96.0 (`-2.4`) | 99.1 → 98.6 (`-0.5`) | ⚪ OPTYMALNY |
| `L3_KT-04_COST_PLUS1` | KT-04 (Zwierciadło Herezji): cost 0 → 1 | 95.8 → 🟢 ** 95.6** (`-0.2`) | 90.0 → 89.2 (`-0.8`) | 98.4 → 98.2 (`-0.2`) | 99.1 → 99.5 (`⬆️ +0.4`) | ⚪ OPTYMALNY |
| `L3_GC-09_COST_MINUS1` | GC-09 (Lista Dłużników): cost 2 → 1 | 95.8 → 🟢 ** 95.6** (`-0.2`) | 90.0 → 89.4 (`-0.6`) | 98.4 → 98.0 (`-0.4`) | 99.1 → 99.4 (`⬆️ +0.3`) | ⚪ OPTYMALNY |
| `L3_KT-10_COST_PLUS1` | KT-10 (Pieczęć Salomona): cost 1 → 2 | 95.8 → 🟢 ** 95.6** (`-0.2`) | 90.0 → 89.5 (`-0.5`) | 98.4 → 98.2 (`-0.2`) | 99.1 → 99.2 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_KT-05_COST_PLUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 2 | 95.8 → 🟢 ** 95.5** (`-0.3`) | 90.0 → 88.6 (`-1.4`) | 98.4 → 98.2 (`-0.2`) | 99.1 → 99.6 (`⬆️ +0.5`) | ⚪ OPTYMALNY |
| `L3_GC-01_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): heresy 1 → 2 | 95.8 → 🟢 ** 95.4** (`-0.4`) | 90.0 → 88.2 (`-1.8`) | 98.4 → 98.6 (`⬆️ +0.2`) | 99.1 → 99.4 (`⬆️ +0.3`) | ⚪ OPTYMALNY |
| `L3_KT-08_COST_PLUS1` | KT-08 (Areszt Wiedzy): cost 2 → 3 | 95.8 → 🟢 ** 95.4** (`-0.4`) | 90.0 → 88.9 (`-1.1`) | 98.4 → 98.0 (`-0.4`) | 99.1 → 99.3 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L3_GC-06_HERESY_PLUS1` | GC-06 (Szantaż): heresy 0 → 1 | 95.8 → 🟢 ** 95.4** (`-0.4`) | 90.0 → 88.6 (`-1.4`) | 98.4 → 98.6 (`⬆️ +0.2`) | 99.1 | ⚪ OPTYMALNY |
| `L3_GC-09_HERESY_PLUS1` | GC-09 (Lista Dłużników): heresy 0 → 1 | 95.8 → 🟢 ** 95.3** (`-0.5`) | 90.0 → 87.2 (`-2.8`) | 98.4 → 98.9 (`⬆️ +0.5`) | 99.1 → 99.7 (`⬆️ +0.6`) | ⚪ OPTYMALNY |
| `L3_KT-06_COST_PLUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 3 | 95.8 → 🟢 ** 95.3** (`-0.5`) | 90.0 → 88.6 (`-1.4`) | 98.4 → 98.1 (`-0.3`) | 99.1 → 99.3 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L3_SO-06_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): heresy 0 → 1 | 95.8 → 🟢 ** 95.3** (`-0.5`) | 90.0 → 88.3 (`-1.7`) | 98.4 | 99.1 → 99.3 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L3_KT-03_HERESY_MINUS1` | KT-03 (Zakazana Wiedza): heresy 1 → 0 | 95.8 → 🟢 ** 95.2** (`-0.6`) | 90.0 → 89.8 (`-0.2`) | 98.4 → 96.1 (`-2.3`) | 99.1 → 99.7 (`⬆️ +0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-03_HERESY_PLUS1` | GC-03 (Podrzucenie Księgi): heresy 0 → 1 | 95.8 → 🟢 ** 95.2** (`-0.6`) | 90.0 → 87.4 (`-2.6`) | 98.4 → 98.8 (`⬆️ +0.4`) | 99.1 → 99.5 (`⬆️ +0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_HERESY_PLUS1` | KT-05 (Wskazówka Cyklu): heresy 0 → 1 | 95.8 → 🟢 ** 95.2** (`-0.6`) | 90.0 → 87.9 (`-2.1`) | 98.4 → 98.5 (`⬆️ +0.1`) | 99.1 → 99.3 (`⬆️ +0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_COST_MINUS1` | GC-07 (Skrytobójstwo): cost 2 → 1 | 95.8 → 🟢 ** 95.1** (`-0.7`) | 90.0 → 89.7 (`-0.3`) | 98.4 → 95.6 (`-2.8`) | 99.1 → 99.9 (`⬆️ +0.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 0 → 1 | 95.8 → 🟢 ** 95.1** (`-0.7`) | 90.0 → 87.2 (`-2.8`) | 98.4 → 98.7 (`⬆️ +0.3`) | 99.1 → 99.5 (`⬆️ +0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_COST_MINUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 0 | 95.8 → 🟢 ** 95.1** (`-0.7`) | 90.0 → 89.4 (`-0.6`) | 98.4 → 96.3 (`-2.1`) | 99.1 → 99.5 (`⬆️ +0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_HERESY_PLUS1` | KT-07 (Archiwum Ukryte): heresy 0 → 1 | 95.8 → 🟢 ** 95.1** (`-0.7`) | 90.0 → 87.5 (`-2.5`) | 98.4 → 98.5 (`⬆️ +0.1`) | 99.1 → 99.4 (`⬆️ +0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_HERESY_PLUS1` | KB-05 (List Żelazny): heresy 0 → 1 | 95.8 → 🟢 ** 95.1** (`-0.7`) | 90.0 → 87.9 (`-2.1`) | 98.4 → 98.2 (`-0.2`) | 99.1 → 99.2 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_HERESY_PLUS1` | KB-06 (Areszt Królewski): heresy 0 → 1 | 95.8 → 🟢 ** 95.1** (`-0.7`) | 90.0 | 98.4 → 96.1 (`-2.3`) | 99.1 → 99.2 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 1 → 2 | 95.8 → 🟢 ** 95.0** (`-0.8`) | 90.0 → 91.9 (`⬆️ +1.9`) | 98.4 → 95.4 (`-3.0`) | 99.1 → 97.7 (`-1.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_HERESY_PLUS1` | KT-02 (Transmutacja Złota): heresy 0 → 1 | 95.8 → 🟢 ** 95.0** (`-0.8`) | 90.0 → 87.3 (`-2.7`) | 98.4 → 98.3 (`-0.1`) | 99.1 → 99.4 (`⬆️ +0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_HERESY_PLUS1` | KT-01 (Rytuał Przejścia): heresy 0 → 1 | 95.8 → 🟢 ** 95.0** (`-0.8`) | 90.0 → 87.2 (`-2.8`) | 98.4 → 98.6 (`⬆️ +0.2`) | 99.1 → 99.3 (`⬆️ +0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_HERESY_PLUS1` | GC-02 (Czarny Rynek): heresy 0 → 1 | 95.8 → 🟢 ** 94.9** (`-0.9`) | 90.0 → 87.1 (`-2.9`) | 98.4 | 99.1 → 99.2 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_HERESY_PLUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 2 | 95.8 → 🟢 ** 94.8** (`-1.0`) | 90.0 → 86.6 (`-3.4`) | 98.4 → 98.5 (`⬆️ +0.1`) | 99.1 → 99.4 (`⬆️ +0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_HERESY_PLUS1` | CAA-03 (Cień na Rynku): heresy 1 → 2 | 95.8 → 🟢 ** 94.8** (`-1.0`) | 90.0 → 90.2 (`⬆️ +0.2`) | 98.4 → 95.7 (`-2.7`) | 99.1 → 98.6 (`-0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_COST_MINUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 0 | 95.8 → 🟢 ** 94.8** (`-1.0`) | 90.0 → 89.5 (`-0.5`) | 98.4 → 95.7 (`-2.7`) | 99.1 → 99.2 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_COST_PLUS1` | SO-09 (Świadek Koronny): cost 2 → 3 | 95.8 → 🟢 ** 94.8** (`-1.0`) | 90.0 → 88.6 (`-1.4`) | 98.4 → 96.5 (`-1.9`) | 99.1 → 99.2 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-07_HERESY_PLUS1` | SO-07 (Przesłuchanie Oficjum): heresy 0 → 1 | 95.8 → 🟢 ** 94.7** (`-1.1`) | 90.0 → 86.4 (`-3.6`) | 98.4 | 99.1 → 99.3 (`⬆️ +0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_HERESY_PLUS1` | CAA-07 (Szantaż Bractwa): heresy 0 → 1 | 95.8 → 🟢 ** 94.7** (`-1.1`) | 90.0 → 89.3 (`-0.7`) | 98.4 → 95.7 (`-2.7`) | 99.1 → 99.2 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_HERESY_MINUS1` | GC-04 (Informator): heresy 1 → 0 | 95.8 → 🟢 ** 94.6** (`-1.2`) | 90.0 → 90.4 (`⬆️ +0.4`) | 98.4 → 94.9 (`-3.5`) | 99.1 → 98.4 (`-0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_COST_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 2 | 95.8 → 🟢 ** 94.5** (`-1.3`) | 90.0 → 91.6 (`⬆️ +1.6`) | 98.4 → 93.3 (`-5.1`) | 99.1 → 98.6 (`-0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_COST_PLUS1` | KB-04 (Faworyt Dworu): cost 1 → 2 | 95.8 → 🟢 ** 94.5** (`-1.3`) | 90.0 → 91.1 (`⬆️ +1.1`) | 98.4 → 93.7 (`-4.7`) | 99.1 → 98.7 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_HERESY_PLUS1` | SO-09 (Świadek Koronny): heresy 0 → 1 | 95.8 → 🟢 ** 94.5** (`-1.3`) | 90.0 → 85.7 (`-4.3`) | 98.4 → 98.3 (`-0.1`) | 99.1 → 99.5 (`⬆️ +0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_COST_PLUS1` | SO-08 (Nasłanie Inkwizytora): cost 2 → 3 | 95.8 → 🟢 ** 94.5** (`-1.3`) | 90.0 → 90.2 (`⬆️ +0.2`) | 98.4 → 94.0 (`-4.4`) | 99.1 → 99.2 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_COST_PLUS1` | CAA-03 (Cień na Rynku): cost 0 → 1 | 95.8 → 🟢 ** 94.3** (`-1.5`) | 90.0 → 90.7 (`⬆️ +0.7`) | 98.4 → 93.5 (`-4.9`) | 99.1 → 98.6 (`-0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_HERESY_PLUS1` | KT-08 (Areszt Wiedzy): heresy 0 → 1 | 95.8 → 🟢 ** 94.3** (`-1.5`) | 90.0 → 87.0 (`-3.0`) | 98.4 → 96.5 (`-1.9`) | 99.1 → 99.4 (`⬆️ +0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-07_COST_MINUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 1 | 95.8 → 🟢 ** 94.3** (`-1.5`) | 90.0 → 89.9 (`-0.1`) | 98.4 → 93.7 (`-4.7`) | 99.1 → 99.3 (`⬆️ +0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_COST_PLUS1` | CAA-06 (Ucieczka z Lochów): cost 2 → 3 | 95.8 → 🟢 ** 94.2** (`-1.6`) | 90.0 → 91.3 (`⬆️ +1.3`) | 98.4 → 93.0 (`-5.4`) | 99.1 → 98.3 (`-0.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 2 → 3 | 95.8 → 🟢 ** 94.2** (`-1.6`) | 90.0 → 90.4 (`⬆️ +0.4`) | 98.4 → 93.0 (`-5.4`) | 99.1 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_COST_PLUS1` | CAA-04 (Fałszywy Trop): cost 1 → 2 | 95.8 → 🟢 ** 94.0** (`-1.8`) | 90.0 → 91.1 (`⬆️ +1.1`) | 98.4 → 92.9 (`-5.5`) | 99.1 → 98.1 (`-1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_HERESY_PLUS1` | CAA-05 (Ukryty Kurier): heresy 0 → 1 | 95.8 → 🟢 ** 93.9** (`-1.9`) | 90.0 → 91.5 (`⬆️ +1.5`) | 98.4 → 91.6 (`-6.8`) | 99.1 → 98.7 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 1 → 2 | 95.8 → 🟢 ** 93.7** (`-2.1`) | 90.0 → 91.0 (`⬆️ +1.0`) | 98.4 → 92.8 (`-5.6`) | 99.1 → 97.2 (`-1.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_HERESY_PLUS1` | KT-03 (Zakazana Wiedza): heresy 1 → 2 | 95.8 → 🟢 ** 93.7** (`-2.1`) | 90.0 → 83.0 (`-7.0`) | 98.4 → 98.5 (`⬆️ +0.1`) | 99.1 → 99.5 (`⬆️ +0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_COST_PLUS1` | CAA-09 (Kurier Relikwii): cost 2 → 3 | 95.8 → 🟢 ** 93.2** (`-2.6`) | 90.0 → 90.6 (`⬆️ +0.6`) | 98.4 → 90.6 (`-7.8`) | 99.1 → 98.3 (`-0.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_HERESY_PLUS1` | KB-07 (Szantaż Pieczęcią): heresy 0 → 1 | 95.8 → 🟢 ** 93.1** (`-2.7`) | 90.0 → 86.5 (`-3.5`) | 98.4 → 93.0 (`-5.4`) | 99.1 → 99.9 (`⬆️ +0.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_COST_MINUS1` | SO-08 (Nasłanie Inkwizytora): cost 2 → 1 | 95.8 → 🟢 ** 93.1** (`-2.7`) | 90.0 → 86.3 (`-3.7`) | 98.4 → 93.4 (`-5.0`) | 99.1 → 99.6 (`⬆️ +0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_HERESY_PLUS1` | SO-01 (Patrol Familiariuszy): heresy 0 → 1 | 95.8 → 🟢 ** 93.0** (`-2.8`) | 90.0 → 83.7 (`-6.3`) | 98.4 → 95.9 (`-2.5`) | 99.1 → 99.4 (`⬆️ +0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_HERESY_PLUS1` | KT-06 (Przesłuchanie Imienia): heresy 0 → 1 | 95.8 → 🟢 ** 92.9** (`-2.9`) | 90.0 → 80.9 (`-9.1`) | 98.4 | 99.1 → 99.4 (`⬆️ +0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_COST_PLUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 2 | 95.8 → 🟢 ** 92.9** (`-2.9`) | 90.0 → 83.5 (`-6.5`) | 98.4 → 95.9 (`-2.5`) | 99.1 → 99.2 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 95.8 → 🟢 ** 92.8** (`-3.0`) | 90.0 → 83.7 (`-6.3`) | 98.4 → 95.6 (`-2.8`) | 99.1 → 99.2 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_COST_PLUS1` | GC-06 (Szantaż): cost 2 → 3 | 95.8 → 🟢 ** 92.8** (`-3.0`) | 90.0 → 81.1 (`-8.9`) | 98.4 → 98.5 (`⬆️ +0.1`) | 99.1 → 98.8 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_COST_PLUS1` | KB-06 (Areszt Królewski): cost 2 → 3 | 95.8 → 🟢 ** 92.7** (`-3.1`) | 90.0 → 86.7 (`-3.3`) | 98.4 → 91.7 (`-6.7`) | 99.1 → 99.8 (`⬆️ +0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_HERESY_PLUS1` | GC-04 (Informator): heresy 1 → 2 | 95.8 → 🟢 ** 92.7** (`-3.1`) | 90.0 → 80.3 (`-9.7`) | 98.4 → 98.6 (`⬆️ +0.2`) | 99.1 → 99.3 (`⬆️ +0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_HERESY_PLUS1` | KT-10 (Pieczęć Salomona): heresy 0 → 1 | 95.8 → 🟢 ** 91.6** (`-4.2`) | 90.0 → 79.9 (`-10.1`) | 98.4 → 95.7 (`-2.7`) | 99.1 → 99.2 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 95.8 → 🟢 ** 91.3** (`-4.5`) | 90.0 → 77.4 (`-12.6`) | 98.4 → 98.5 (`⬆️ +0.1`) | 99.1 → 97.9 (`-1.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_HERESY_PLUS1` | SO-08 (Nasłanie Inkwizytora): heresy 1 → 2 | 95.8 → 🟢 ** 91.2** (`-4.6`) | 90.0 → 78.4 (`-11.6`) | 98.4 → 95.6 (`-2.8`) | 99.1 → 99.6 (`⬆️ +0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_COST_MINUS1` | KB-06 (Areszt Królewski): cost 2 → 1 | 95.8 → 🟢 ** 91.1** (`-4.7`) | 90.0 → 92.7 (`⬆️ +2.7`) | 98.4 → 96.1 (`-2.3`) | 99.1 → 84.5 (`-14.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_HERESY_MINUS1` | KB-04 (Faworyt Dworu): heresy 1 → 0 | 95.8 → 🟢 ** 90.9** (`-4.9`) | 90.0 → 91.0 (`⬆️ +1.0`) | 98.4 → 96.0 (`-2.4`) | 99.1 → 85.8 (`-13.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_COST_PLUS1` | KB-01 (Rozkaz Dworu): cost 1 → 2 | 95.8 → 🟢 ** 89.5** (`-6.3`) | 90.0 → 84.7 (`-5.3`) | 98.4 → 84.1 (`-14.3`) | 99.1 → 99.6 (`⬆️ +0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_HERESY_PLUS1` | SO-10 (Oczyść Miasto): heresy 2 → 3 | 95.8 → 🟢 ** 89.1** (`-6.7`) | 90.0 → 78.8 (`-11.2`) | 98.4 → 89.1 (`-9.3`) | 99.1 → 99.3 (`⬆️ +0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_COST_PLUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 3 | 95.8 → 🟢 ** 88.5** (`-7.3`) | 90.0 → 85.7 (`-4.3`) | 98.4 → 79.9 (`-18.5`) | 99.1 → 99.8 (`⬆️ +0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_COST_MINUS1` | KB-04 (Faworyt Dworu): cost 1 → 0 | 95.8 → 🟢 ** 87.2** (`-8.6`) | 90.0 → 82.9 (`-7.1`) | 98.4 → 79.5 (`-18.9`) | 99.1 → 99.2 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_HERESY_PLUS1` | SO-03 (Podejrzenie): heresy 0 → 1 | 95.8 → 🟢 ** 86.8** (`-9.0`) | 90.0 → 71.4 (`-18.6`) | 98.4 → 89.5 (`-8.9`) | 99.1 → 99.4 (`⬆️ +0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): heresy 0 → 1 | 95.8 → 🟢 ** 86.5** (`-9.3`) | 90.0 → 71.8 (`-18.2`) | 98.4 → 88.4 (`-10.0`) | 99.1 → 99.2 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_COST_MINUS1` | KB-05 (List Żelazny): cost 2 → 1 | 95.8 → 🟢 ** 76.2** (`-19.6`) | 90.0 → 76.6 (`-13.4`) | 98.4 → 52.9 (`-45.5`) | 99.1 → 99.2 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 61 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_GC-05_COST_PLUS1` | GC-05 (Fałszywy Świadek): cost 0 → 1 | 🟢 ** 95.8** | 90.0 | 98.4 | 99.1 | ⚪ OPTYMALNY |
| `L3_GC-05_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): heresy 0 → 1 | 🟢 ** 95.8** | 90.0 | 98.4 | 99.1 | ⚪ OPTYMALNY |
| `L3_KT-03_COST_PLUS1` | KT-03 (Zakazana Wiedza): cost 0 → 1 | 🟢 ** 95.8** | 90.0 | 98.4 | 99.1 | ⚪ OPTYMALNY |
| `L3_SO-05_COST_PLUS1` | SO-05 (Wezwanie do Trybunału): cost 0 → 1 | 🟢 ** 95.8** | 90.0 | 98.4 | 99.1 | ⚪ OPTYMALNY |
| `L3_SO-05_HERESY_PLUS1` | SO-05 (Wezwanie do Trybunału): heresy 0 → 1 | 🟢 ** 95.8** | 90.0 | 98.4 | 99.1 | ⚪ OPTYMALNY |
| `L3_KB-08_COST_MINUS1` | KB-08 (Przekupstwo Sędziego): cost 3 → 2 | 95.8 → 🟢 ** 95.6** (`-0.2`) | 90.0 | 98.4 → 98.3 (`-0.1`) | 99.1 → 98.6 (`-0.5`) | ⚪ OPTYMALNY |
| `L3_KT-06_COST_MINUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 1 | 95.8 → 🟢 ** 95.5** (`-0.3`) | 90.0 → 89.4 (`-0.6`) | 98.4 → 98.2 (`-0.2`) | 99.1 → 99.0 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_SO-01_COST_PLUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 2 | 95.8 → 🟢 ** 95.4** (`-0.4`) | 90.0 → 89.8 (`-0.2`) | 98.4 | 99.1 → 98.0 (`-1.1`) | ⚪ OPTYMALNY |
| `L3_GC-04_COST_PLUS1` | GC-04 (Informator): cost 0 → 1 | 95.8 → 🟢 ** 95.2** (`-0.6`) | 90.0 → 88.4 (`-1.6`) | 98.4 → 98.3 (`-0.1`) | 99.1 → 98.9 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_COST_MINUS1` | KT-10 (Pieczęć Salomona): cost 1 → 0 | 95.8 → 🟢 ** 95.1** (`-0.7`) | 90.0 → 89.7 (`-0.3`) | 98.4 → 96.4 (`-2.0`) | 99.1 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_COST_PLUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 2 | 95.8 → 🟢 ** 95.0** (`-0.8`) | 90.0 → 89.9 (`-0.1`) | 98.4 → 96.0 (`-2.4`) | 99.1 → 99.0 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_COST_PLUS1` | KB-08 (Przekupstwo Sędziego): cost 3 → 4 | 95.8 → 🟢 ** 95.0** (`-0.8`) | 90.0 → 89.8 (`-0.2`) | 98.4 → 96.2 (`-2.2`) | 99.1 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-04_HERESY_PLUS1` | KT-04 (Zwierciadło Herezji): heresy 0 → 1 | 95.8 → 🟢 ** 95.0** (`-0.8`) | 90.0 → 87.5 (`-2.5`) | 98.4 → 98.3 (`-0.1`) | 99.1 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-03_COST_PLUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 2 | 95.8 → 🟢 ** 94.9** (`-0.9`) | 90.0 → 89.3 (`-0.7`) | 98.4 → 96.3 (`-2.1`) | 99.1 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_COST_PLUS1` | GC-09 (Lista Dłużników): cost 2 → 3 | 95.8 → 🟢 ** 94.9** (`-0.9`) | 90.0 → 88.2 (`-1.8`) | 98.4 | 99.1 → 98.1 (`-1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_COST_PLUS1` | CAA-10 (Echo Alhambry): cost 0 → 1 | 95.8 → 🟢 ** 94.8** (`-1.0`) | 90.0 → 89.7 (`-0.3`) | 98.4 → 95.8 (`-2.6`) | 99.1 → 99.0 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_COST_PLUS1` | CAA-08 (Kaptur Nocy): cost 1 → 2 | 95.8 → 🟢 ** 94.7** (`-1.1`) | 90.0 → 88.6 (`-1.4`) | 98.4 → 96.5 (`-1.9`) | 99.1 → 98.9 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-07_COST_PLUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 3 | 95.8 → 🟢 ** 94.7** (`-1.1`) | 90.0 → 88.7 (`-1.3`) | 98.4 → 96.3 (`-2.1`) | 99.1 | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_COST_MINUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 0 | 95.8 → 🟢 ** 94.5** (`-1.3`) | 90.0 → 88.4 (`-1.6`) | 98.4 → 96.0 (`-2.4`) | 99.1 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_COST_MINUS1` | GC-10 (Upadek Domu): cost 4 → 3 | 95.8 → 🟢 ** 94.3** (`-1.5`) | 90.0 → 88.9 (`-1.1`) | 98.4 → 95.4 (`-3.0`) | 99.1 → 98.5 (`-0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_COST_MINUS1` | SO-03 (Podejrzenie): cost 1 → 0 | 95.8 → 🟢 ** 94.2** (`-1.6`) | 90.0 → 89.8 (`-0.2`) | 98.4 → 93.7 (`-4.7`) | 99.1 → 99.0 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_HERESY_PLUS1` | KB-01 (Rozkaz Dworu): heresy 0 → 1 | 95.8 → 🟢 ** 94.0** (`-1.8`) | 90.0 → 87.2 (`-2.8`) | 98.4 → 96.2 (`-2.2`) | 99.1 → 98.7 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_HERESY_PLUS1` | KB-03 (Plotka Dworska): heresy 0 → 1 | 95.8 → 🟢 ** 93.9** (`-1.9`) | 90.0 → 86.8 (`-3.2`) | 98.4 → 96.0 (`-2.4`) | 99.1 → 99.0 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_COST_MINUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 0 | 95.8 → 🟢 ** 93.8** (`-2.0`) | 90.0 → 87.1 (`-2.9`) | 98.4 → 96.0 (`-2.4`) | 99.1 → 98.4 (`-0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_COST_PLUS1` | GC-10 (Upadek Domu): cost 4 → 5 | 95.8 → 🟢 ** 93.1** (`-2.7`) | 90.0 → 88.3 (`-1.7`) | 98.4 → 93.7 (`-4.7`) | 99.1 → 97.3 (`-1.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_COST_PLUS1` | SO-03 (Podejrzenie): cost 1 → 2 | 95.8 → 🟢 ** 93.1** (`-2.7`) | 90.0 → 84.4 (`-5.6`) | 98.4 → 95.9 (`-2.5`) | 99.1 → 99.0 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_COST_MINUS1` | GC-08 (Zatrute Złoto): cost 1 → 0 | 95.8 → 🟢 ** 92.9** (`-2.9`) | 90.0 → 89.9 (`-0.1`) | 98.4 → 91.2 (`-7.2`) | 99.1 → 97.7 (`-1.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_HERESY_PLUS1` | KB-04 (Faworyt Dworu): heresy 1 → 2 | 95.8 → 🟢 ** 92.9** (`-2.9`) | 90.0 → 85.6 (`-4.4`) | 98.4 → 95.1 (`-3.3`) | 99.1 → 98.1 (`-1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_COST_PLUS1` | SO-06 (Areszt Trybunalski): cost 2 → 3 | 95.8 → 🟢 ** 92.8** (`-3.0`) | 90.0 → 81.1 (`-8.9`) | 98.4 → 98.2 (`-0.2`) | 99.1 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 1 → 2 | 95.8 → 🟢 ** 92.7** (`-3.1`) | 90.0 → 86.8 (`-3.2`) | 98.4 → 93.1 (`-5.3`) | 99.1 → 98.3 (`-0.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-03_COST_MINUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 0 | 95.8 → 🟢 ** 92.5** (`-3.3`) | 90.0 → 89.7 (`-0.3`) | 98.4 → 89.2 (`-9.2`) | 99.1 → 98.5 (`-0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_HERESY_MINUS1` | KB-09 (Dekret Królewski): heresy 1 → 0 | 95.8 → 🟢 ** 92.5** (`-3.3`) | 90.0 → 89.3 (`-0.7`) | 98.4 → 89.2 (`-9.2`) | 99.1 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_COST_MINUS1` | GC-02 (Czarny Rynek): cost 1 → 0 | 95.8 → 🟢 ** 92.0** (`-3.8`) | 90.0 → 88.5 (`-1.5`) | 98.4 → 90.0 (`-8.4`) | 99.1 → 97.6 (`-1.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_COST_PLUS1` | GC-02 (Czarny Rynek): cost 1 → 2 | 95.8 → 🟢 ** 91.8** (`-4.0`) | 90.0 → 80.4 (`-9.6`) | 98.4 → 96.5 (`-1.9`) | 99.1 → 98.5 (`-0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_COST_MINUS1` | GC-06 (Szantaż): cost 2 → 1 | 95.8 → 🟢 ** 91.5** (`-4.3`) | 90.0 → 88.6 (`-1.4`) | 98.4 → 88.0 (`-10.4`) | 99.1 → 97.9 (`-1.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_COST_MINUS1` | SO-10 (Oczyść Miasto): cost 4 → 3 | 95.8 → 🟢 ** 91.5** (`-4.3`) | 90.0 → 79.2 (`-10.8`) | 98.4 → 98.2 (`-0.2`) | 99.1 → 97.0 (`-2.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_HERESY_MINUS1` | SO-08 (Nasłanie Inkwizytora): heresy 1 → 0 | 95.8 → 🟢 ** 91.4** (`-4.4`) | 90.0 → 84.4 (`-5.6`) | 98.4 → 91.2 (`-7.2`) | 99.1 → 98.7 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_HERESY_MINUS1` | GC-10 (Upadek Domu): heresy 2 → 1 | 95.8 → 🟢 ** 91.2** (`-4.6`) | 90.0 → 89.6 (`-0.4`) | 98.4 → 86.2 (`-12.2`) | 99.1 → 97.8 (`-1.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_HERESY_MINUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 0 | 95.8 → 🟢 ** 90.8** (`-5.0`) | 90.0 → 79.2 (`-10.8`) | 98.4 → 94.6 (`-3.8`) | 99.1 → 98.5 (`-0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_HERESY_PLUS1` | SO-04 (Publiczne Ostrzeżenie): heresy 0 → 1 | 95.8 → 🟢 ** 89.1** (`-6.7`) | 90.0 → 75.5 (`-14.5`) | 98.4 → 92.7 (`-5.7`) | 99.1 → 99.0 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_HERESY_MINUS1` | CAA-10 (Echo Alhambry): heresy 1 → 0 | 95.8 → 🟢 ** 88.7** (`-7.1`) | 90.0 → 71.3 (`-18.7`) | 98.4 → 96.4 (`-2.0`) | 99.1 → 98.4 (`-0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_COST_PLUS1` | KB-03 (Plotka Dworska): cost 1 → 2 | 95.8 → 🟢 ** 88.1** (`-7.7`) | 90.0 → 89.7 (`-0.3`) | 98.4 → 87.2 (`-11.2`) | 99.1 → 87.5 (`-11.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_HERESY_MINUS1` | SO-10 (Oczyść Miasto): heresy 2 → 1 | 95.8 → 🟢 ** 88.0** (`-7.8`) | 90.0 → 81.8 (`-8.2`) | 98.4 → 83.5 (`-14.9`) | 99.1 → 98.6 (`-0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_COST_MINUS1` | KB-01 (Rozkaz Dworu): cost 1 → 0 | 95.8 → 🟢 ** 87.8** (`-8.0`) | 90.0 → 82.7 (`-7.3`) | 98.4 → 81.9 (`-16.5`) | 99.1 → 98.9 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_HERESY_PLUS1` | GC-10 (Upadek Domu): heresy 2 → 3 | 95.8 → 🟢 ** 87.3** (`-8.5`) | 90.0 → 78.2 (`-11.8`) | 98.4 → 86.4 (`-12.0`) | 99.1 → 97.3 (`-1.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_COST_PLUS1` | SO-10 (Oczyść Miasto): cost 4 → 5 | 95.8 → 🟢 ** 86.7** (`-9.1`) | 90.0 → 80.0 (`-10.0`) | 98.4 → 82.8 (`-15.6`) | 99.1 → 97.3 (`-1.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_HERESY_PLUS1` | KB-02 (Pobór Podatków): heresy 0 → 1 | 95.8 → 🟢 ** 86.2** (`-9.6`) | 90.0 → 87.2 (`-2.8`) | 98.4 → 93.6 (`-4.8`) | 99.1 → 77.7 (`-21.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_COST_MINUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 1 | 95.8 → 🟢 ** 84.4** (`-11.4`) | 90.0 → 86.2 (`-3.8`) | 98.4 → 83.2 (`-15.2`) | 99.1 → 83.8 (`-15.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_HERESY_PLUS1` | CAA-09 (Kurier Relikwii): heresy 0 → 1 | 95.8 → 🟢 ** 83.8** (`-12.0`) | 90.0 → 82.3 (`-7.7`) | 98.4 → 85.1 (`-13.3`) | 99.1 → 83.9 (`-15.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_COST_MINUS1` | KB-03 (Plotka Dworska): cost 1 → 0 | 95.8 → 🟢 ** 83.6** (`-12.2`) | 90.0 → 82.9 (`-7.1`) | 98.4 → 69.7 (`-28.7`) | 99.1 → 98.1 (`-1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_HERESY_MINUS1` | KB-10 (Pieczęć Korony): heresy 2 → 1 | 95.8 → 🟢 ** 81.0** (`-14.8`) | 90.0 → 84.2 (`-5.8`) | 98.4 → 73.7 (`-24.7`) | 99.1 → 85.0 (`-14.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_COST_PLUS1` | KB-02 (Pobór Podatków): cost 1 → 2 | 95.8 → 🟢 ** 80.9** (`-14.9`) | 90.0 → 77.4 (`-12.6`) | 98.4 → 84.4 (`-14.0`) | 99.1 → 0.0 (`-99.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_HERESY_PLUS1` | CAA-10 (Echo Alhambry): heresy 1 → 2 | 95.8 → 🟢 ** 78.3** (`-17.5`) | 90.0 → 77.9 (`-12.1`) | 98.4 → 83.1 (`-15.3`) | 99.1 → 74.0 (`-25.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_COST_PLUS1` | KB-10 (Pieczęć Korony): cost 2 → 3 | 95.8 → 🟢 ** 73.2** (`-22.6`) | 90.0 → 72.8 (`-17.2`) | 98.4 → 73.6 (`-24.8`) | 99.1 → 0.0 (`-99.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_HERESY_PLUS1` | KB-09 (Dekret Królewski): heresy 1 → 2 | 95.8 → 🟢 ** 69.5** (`-26.3`) | 90.0 → 75.9 (`-14.1`) | 98.4 → 63.0 (`-35.4`) | 99.1 → 0.0 (`-99.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_COST_PLUS1` | KB-05 (List Żelazny): cost 2 → 3 | 95.8 → 🟢 ** 67.1** (`-28.7`) | 90.0 → 83.9 (`-6.1`) | 98.4 → 96.2 (`-2.2`) | 99.1 → 21.1 (`-78.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_COST_MINUS1` | KB-02 (Pobór Podatków): cost 1 → 0 | 95.8 → 🟢 ** 66.9** (`-28.9`) | 90.0 → 70.1 (`-19.9`) | 98.4 → 52.3 (`-46.1`) | 99.1 → 78.4 (`-20.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_HERESY_PLUS1` | KB-10 (Pieczęć Korony): heresy 2 → 3 | 95.8 → 🟢 ** 61.1** (`-34.7`) | 90.0 → 57.8 (`-32.2`) | 98.4 → 75.1 (`-23.3`) | 99.1 → 50.5 (`-48.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_COST_MINUS1` | KB-10 (Pieczęć Korony): cost 2 → 1 | 95.8 → 🟢 ** 50.1** (`-45.7`) | 90.0 → 63.3 (`-26.7`) | 98.4 → 31.5 (`-66.9`) | 99.1 → 55.4 (`-43.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_COST_MINUS1` | KB-09 (Dekret Królewski): cost 3 → 2 | 95.8 → 🟡 ** 47.1** (`-48.7`) | 90.0 → 63.6 (`-26.4`) | 98.4 → 30.6 (`-67.8`) | 99.1 → 0.0 (`-99.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_COST_PLUS1` | KB-09 (Dekret Królewski): cost 3 → 4 | 95.8 → 🟡 ** 30.9** (`-64.9`) | 90.0 → 42.3 (`-47.7`) | 98.4 → 19.5 (`-78.9`) | 99.1 → 0.0 (`-99.1`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (97)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | 5.51 Er (1–10) | 1.2% | 26.4% | 1.02 (0–4) | 3.59 (0–19) | 1.04zł (0.0–4.3) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_HERESY_PLUS1` | 5.49 Er (1–10) | 1.0% | 26.3% | 1.02 (0–4) | 3.64 (0–21) | 1.03zł (0.0–4.3) | 6.41 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-01_COST_MINUS1` | 5.51 Er (1–10) | 1.1% | 25.4% | 1.04 (0–4) | 3.59 (0–19) | 1.05zł (0.0–4.3) | 6.32 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_COST_MINUS1` | 5.50 Er (1–10) | 1.1% | 26.2% | 1.02 (0–4) | 3.60 (0–17) | 1.17zł (0.0–4.7) | 6.32 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_HERESY_PLUS1` | 5.48 Er (1–10) | 1.0% | 26.3% | 1.02 (0–4) | 3.67 (0–19) | 1.03zł (0.0–4.3) | 6.42 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-09_COST_MINUS1` | 5.50 Er (1–10) | 1.1% | 25.4% | 1.05 (0–4) | 3.60 (0–19) | 1.02zł (0.0–4.3) | 6.33 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-02_COST_PLUS1` | 5.50 Er (1–10) | 1.1% | 26.5% | 1.02 (0–4) | 3.60 (0–19) | 0.87zł (0.0–3.7) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-01_HERESY_MINUS1` | 5.52 Er (1–10) | 1.1% | 26.4% | 1.03 (0–4) | 3.55 (0–19) | 1.04zł (0.0–4.7) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-07_HERESY_MINUS1` | 5.50 Er (1–10) | 1.1% | 26.4% | 1.02 (0–4) | 3.57 (0–19) | 1.03zł (0.0–4.3) | 6.23 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_COST_MINUS1` | 5.50 Er (1–10) | 1.1% | 26.1% | 1.02 (0–4) | 3.58 (0–17) | 1.17zł (0.0–4.7) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_HERESY_PLUS1` | 5.49 Er (1–10) | 1.1% | 26.3% | 1.02 (0–4) | 3.65 (0–19) | 1.04zł (0.0–4.3) | 6.42 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_COST_MINUS1` | 5.50 Er (1–10) | 1.1% | 26.1% | 1.02 (0–4) | 3.58 (0–19) | 1.19zł (0.0–5.0) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_MINUS1` | 5.50 Er (1–10) | 1.2% | 26.4% | 1.02 (0–4) | 3.59 (0–19) | 1.21zł (0.0–4.7) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-09_COST_MINUS1` | 5.51 Er (1–10) | 1.1% | 26.4% | 1.02 (0–4) | 3.59 (0–19) | 1.23zł (0.0–4.7) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_COST_MINUS1` | 5.50 Er (1–10) | 1.1% | 26.1% | 1.02 (0–4) | 3.59 (0–19) | 1.19zł (0.0–4.7) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_COST_MINUS1` | 5.50 Er (1–10) | 1.1% | 26.2% | 1.02 (0–4) | 3.58 (0–17) | 1.17zł (0.0–4.7) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-09_HERESY_MINUS1` | 5.51 Er (1–10) | 1.0% | 26.4% | 1.02 (0–4) | 3.56 (0–19) | 1.04zł (0.0–4.7) | 6.18 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-07_HERESY_PLUS1` | 5.50 Er (1–10) | 1.1% | 26.3% | 1.02 (0–4) | 3.63 (0–19) | 1.04zł (0.0–4.3) | 6.38 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-07_COST_MINUS1` | 5.50 Er (1–10) | 1.2% | 26.4% | 1.02 (0–4) | 3.59 (0–19) | 1.22zł (0.0–5.0) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_COST_MINUS1` | 5.50 Er (1–10) | 1.1% | 26.1% | 1.02 (0–4) | 3.59 (0–19) | 1.17zł (0.0–5.0) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-08_HERESY_PLUS1` | 5.50 Er (1–10) | 1.1% | 26.4% | 1.02 (0–4) | 3.59 (0–19) | 1.04zł (0.0–4.3) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-02_COST_MINUS1` | 5.51 Er (1–10) | 1.1% | 26.4% | 1.02 (0–4) | 3.59 (0–19) | 1.22zł (0.0–5.0) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_COST_MINUS1` | 5.49 Er (1–10) | 1.1% | 26.1% | 1.02 (0–4) | 3.58 (0–17) | 1.18zł (0.0–5.0) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_HERESY_PLUS1` | 5.48 Er (1–10) | 1.0% | 26.3% | 1.02 (0–4) | 3.68 (0–19) | 1.03zł (0.0–4.3) | 6.43 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_PLUS1` | 5.50 Er (1–10) | 1.2% | 26.5% | 1.02 (0–4) | 3.58 (0–19) | 0.88zł (0.0–4.0) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-07_COST_PLUS1` | 5.51 Er (1–10) | 1.2% | 26.5% | 1.02 (0–4) | 3.59 (0–19) | 0.87zł (0.0–4.0) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_HERESY_PLUS1` | 5.48 Er (1–10) | 1.0% | 26.3% | 1.02 (0–4) | 3.66 (0–21) | 1.03zł (0.0–4.3) | 6.43 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_COST_MINUS1` | 5.49 Er (1–10) | 1.1% | 26.1% | 1.02 (0–4) | 3.58 (0–17) | 1.17zł (0.0–4.7) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-08_COST_MINUS1` | 5.51 Er (1–10) | 1.1% | 26.4% | 1.02 (0–4) | 3.59 (0–19) | 1.21zł (0.0–4.7) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-07_COST_PLUS1` | 5.50 Er (1–10) | 1.1% | 26.6% | 1.02 (0–4) | 3.57 (0–19) | 1.00zł (0.0–4.3) | 6.29 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-09_COST_PLUS1` | 5.51 Er (1–10) | 1.2% | 26.5% | 1.02 (0–4) | 3.59 (0–19) | 0.86zł (0.0–4.0) | 6.31 (0.6–10.0) | 🟢 W NORMIE |
| `L3_SO-06_COST_MINUS1` | 5.51 Er (1–10) | 1.1% | 25.5% | 1.03 (0–4) | 3.58 (0–19) | 1.02zł (0.0–4.3) | 6.30 (0.6–10.0) | 🟢 W NORMIE |
| `L3_KT-04_COST_PLUS1` | 5.51 Er (1–10) | 1.2% | 26.5% | 1.02 (0–4) | 3.58 (0–19) | 0.87zł (0.0–4.0) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-09_COST_MINUS1` | 5.48 Er (1–10) | 1.0% | 26.1% | 1.02 (0–4) | 3.65 (0–20) | 1.03zł (0.0–4.3) | 6.40 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-10_COST_PLUS1` | 5.51 Er (1–10) | 1.2% | 26.4% | 1.03 (0–4) | 3.60 (0–19) | 0.86zł (0.0–4.0) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-05_COST_PLUS1` | 5.50 Er (1–10) | 1.2% | 26.4% | 1.02 (0–4) | 3.59 (0–19) | 0.86zł (0.0–4.0) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-01_HERESY_PLUS1` | 5.49 Er (1–10) | 1.1% | 26.3% | 1.02 (0–4) | 3.62 (0–19) | 1.04zł (0.0–4.0) | 6.40 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-08_COST_PLUS1` | 5.51 Er (1–10) | 1.2% | 26.5% | 1.02 (0–4) | 3.59 (0–19) | 0.87zł (0.0–4.0) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-06_HERESY_PLUS1` | 5.49 Er (1–10) | 1.0% | 26.3% | 1.02 (0–4) | 3.63 (0–19) | 1.03zł (0.0–4.0) | 6.42 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-09_HERESY_PLUS1` | 5.49 Er (1–10) | 1.1% | 26.3% | 1.02 (0–4) | 3.66 (0–19) | 1.04zł (0.0–4.3) | 6.43 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-06_COST_PLUS1` | 5.51 Er (1–10) | 1.2% | 26.6% | 1.02 (0–4) | 3.59 (0–19) | 0.84zł (0.0–4.0) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-06_HERESY_PLUS1` | 5.49 Er (1–10) | 1.0% | 26.3% | 1.01 (0–4) | 3.61 (0–19) | 1.03zł (0.0–4.3) | 6.35 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-03_HERESY_MINUS1` | 5.51 Er (1–10) | 1.0% | 26.4% | 1.03 (0–4) | 3.56 (0–19) | 1.04zł (0.0–4.3) | 6.16 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-03_HERESY_PLUS1` | 5.49 Er (1–10) | 1.1% | 26.3% | 1.02 (0–3) | 3.66 (0–21) | 1.03zł (0.0–4.7) | 6.41 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-05_HERESY_PLUS1` | 5.50 Er (1–10) | 1.2% | 26.4% | 1.02 (0–4) | 3.67 (0–19) | 1.04zł (0.0–4.7) | 6.44 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-07_COST_MINUS1` | 5.48 Er (1–10) | 1.0% | 25.9% | 1.02 (0–3) | 3.60 (0–19) | 1.02zł (0.0–4.7) | 6.37 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-08_HERESY_PLUS1` | 5.49 Er (1–10) | 1.1% | 26.3% | 1.02 (0–3) | 3.66 (0–21) | 1.03zł (0.0–4.7) | 6.42 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-05_COST_MINUS1` | 5.51 Er (1–10) | 1.1% | 26.4% | 1.02 (0–4) | 3.59 (0–19) | 1.22zł (0.0–5.0) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-07_HERESY_PLUS1` | 5.51 Er (1–10) | 1.3% | 26.4% | 1.02 (0–4) | 3.67 (0–20) | 1.04zł (0.0–4.7) | 6.44 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-05_HERESY_PLUS1` | 5.49 Er (1–10) | 1.1% | 26.3% | 1.02 (0–4) | 3.61 (0–19) | 1.04zł (0.0–4.3) | 6.34 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-06_HERESY_PLUS1` | 5.50 Er (1–10) | 1.1% | 26.3% | 1.02 (0–4) | 3.59 (0–19) | 1.04zł (0.0–4.3) | 6.32 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_COST_PLUS1` | 5.53 Er (1–10) | 1.2% | 27.2% | 1.02 (0–4) | 3.62 (0–18) | 1.03zł (0.0–4.3) | 6.32 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-02_HERESY_PLUS1` | 5.51 Er (1–10) | 1.3% | 26.4% | 1.02 (0–4) | 3.66 (0–19) | 1.04zł (0.0–4.7) | 6.44 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-01_HERESY_PLUS1` | 5.51 Er (1–10) | 1.4% | 26.4% | 1.02 (0–4) | 3.66 (0–19) | 1.04zł (0.0–4.7) | 6.44 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-02_HERESY_PLUS1` | 5.48 Er (1–10) | 1.1% | 26.3% | 1.02 (0–4) | 3.67 (0–19) | 1.03zł (0.0–4.3) | 6.42 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-09_HERESY_PLUS1` | 5.52 Er (1–10) | 1.4% | 26.4% | 1.02 (0–4) | 3.69 (0–22) | 1.04zł (0.0–4.7) | 6.45 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_HERESY_PLUS1` | 5.48 Er (1–10) | 1.0% | 26.3% | 1.02 (0–4) | 3.69 (0–21) | 1.03zł (0.0–4.7) | 6.43 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-01_COST_MINUS1` | 5.47 Er (1–10) | 1.0% | 25.8% | 1.02 (0–3) | 3.62 (0–18) | 1.05zł (0.0–4.0) | 6.36 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-09_COST_PLUS1` | 5.51 Er (1–10) | 1.1% | 26.5% | 1.04 (0–4) | 3.57 (0–19) | 1.05zł (0.0–4.3) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-07_HERESY_PLUS1` | 5.46 Er (1–10) | 1.0% | 26.2% | 1.02 (0–4) | 3.63 (0–19) | 1.04zł (0.0–4.3) | 6.37 (0.8–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_HERESY_PLUS1` | 5.48 Er (1–10) | 1.0% | 26.3% | 1.02 (0–4) | 3.67 (0–21) | 1.03zł (0.0–4.3) | 6.43 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-04_HERESY_MINUS1` | 5.53 Er (1–10) | 1.2% | 26.5% | 1.03 (0–4) | 3.49 (0–18) | 1.04zł (0.0–4.7) | 6.15 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_COST_PLUS1` | 5.54 Er (1–10) | 1.2% | 27.0% | 1.03 (0–4) | 3.60 (0–18) | 1.02zł (0.0–4.3) | 6.31 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-04_COST_PLUS1` | 5.52 Er (1–10) | 1.0% | 27.4% | 1.03 (0–3) | 3.55 (0–19) | 1.05zł (0.0–4.3) | 6.28 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-09_HERESY_PLUS1` | 5.46 Er (1–10) | 1.0% | 26.2% | 1.02 (0–3) | 3.63 (0–19) | 1.04zł (0.0–4.3) | 6.37 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-08_COST_PLUS1` | 5.55 Er (1–10) | 1.3% | 26.7% | 1.04 (0–4) | 3.56 (0–19) | 1.05zł (0.0–4.3) | 6.26 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_COST_PLUS1` | 5.54 Er (1–10) | 1.1% | 27.4% | 1.03 (0–4) | 3.59 (0–18) | 1.00zł (0.0–4.3) | 6.28 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-08_HERESY_PLUS1` | 5.51 Er (1–10) | 1.4% | 26.4% | 1.02 (0–4) | 3.66 (0–19) | 1.03zł (0.0–4.3) | 6.44 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-07_COST_MINUS1` | 5.51 Er (1–10) | 1.2% | 25.5% | 1.04 (0–3) | 3.59 (0–19) | 1.02zł (0.0–4.3) | 6.32 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_COST_PLUS1` | 5.54 Er (1–10) | 1.1% | 27.2% | 1.03 (0–4) | 3.62 (0–18) | 1.09zł (0.0–4.3) | 6.32 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_COST_PLUS1` | 5.54 Er (1–10) | 1.1% | 27.2% | 1.03 (0–4) | 3.59 (0–18) | 1.05zł (0.0–4.3) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_COST_PLUS1` | 5.54 Er (1–10) | 1.2% | 27.2% | 1.03 (0–4) | 3.58 (0–18) | 1.03zł (0.0–4.3) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_HERESY_PLUS1` | 5.48 Er (1–10) | 1.0% | 26.3% | 1.02 (0–4) | 3.67 (0–19) | 1.03zł (0.0–4.7) | 6.43 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_COST_PLUS1` | 5.54 Er (1–10) | 1.2% | 27.8% | 1.03 (0–4) | 3.62 (0–20) | 1.03zł (0.0–4.3) | 6.32 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-03_HERESY_PLUS1` | 5.52 Er (1–10) | 1.5% | 26.4% | 1.02 (0–4) | 3.70 (0–19) | 1.04zł (0.0–5.0) | 6.45 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_COST_PLUS1` | 5.55 Er (1–10) | 1.1% | 27.3% | 1.03 (0–4) | 3.60 (0–18) | 1.04zł (0.0–4.3) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-07_HERESY_PLUS1` | 5.46 Er (1–10) | 1.0% | 26.2% | 1.02 (0–4) | 3.60 (0–21) | 1.03zł (0.0–4.3) | 6.34 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-08_COST_MINUS1` | 5.45 Er (1–10) | 1.0% | 25.2% | 1.03 (0–4) | 3.61 (0–19) | 1.01zł (0.0–4.3) | 6.33 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-01_HERESY_PLUS1` | 5.43 Er (1–10) | 1.0% | 26.1% | 1.01 (0–3) | 3.62 (0–19) | 1.03zł (0.0–4.3) | 6.39 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-06_HERESY_PLUS1` | 5.52 Er (1–10) | 1.6% | 26.5% | 1.02 (0–4) | 3.70 (0–22) | 1.04zł (0.0–4.7) | 6.46 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-04_COST_PLUS1` | 5.50 Er (1–10) | 1.1% | 27.1% | 1.01 (0–4) | 3.58 (0–19) | 1.05zł (0.0–4.3) | 6.29 (0.6–10.0) | 🟢 W NORMIE |
| `L3_SO-02_COST_PLUS1` | 5.54 Er (1–10) | 1.2% | 28.6% | 1.02 (0–4) | 3.56 (0–19) | 1.05zł (0.0–4.3) | 6.28 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-06_COST_PLUS1` | 5.53 Er (1–10) | 1.2% | 26.8% | 1.03 (0–4) | 3.62 (0–19) | 0.99zł (0.0–4.7) | 6.33 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-06_COST_PLUS1` | 5.47 Er (1–10) | 0.9% | 26.5% | 1.02 (0–4) | 3.55 (0–19) | 1.04zł (0.0–4.3) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-04_HERESY_PLUS1` | 5.48 Er (1–10) | 1.0% | 26.3% | 1.02 (0–3) | 3.73 (0–21) | 1.04zł (0.0–4.0) | 6.43 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-10_HERESY_PLUS1` | 5.51 Er (1–10) | 1.5% | 26.4% | 1.02 (0–4) | 3.80 (0–20) | 1.04zł (0.0–4.3) | 6.56 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_HERESY_MINUS1` | 5.53 Er (1–10) | 1.2% | 26.5% | 1.03 (0–4) | 3.50 (0–18) | 1.04zł (0.0–4.3) | 6.15 (0.3–10.0) | 🟢 W NORMIE |
| `L3_SO-08_HERESY_PLUS1` | 5.42 Er (1–10) | 0.9% | 26.1% | 1.01 (0–4) | 3.64 (0–19) | 1.03zł (0.0–4.3) | 6.38 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-06_COST_MINUS1` | 5.51 Er (1–10) | 1.2% | 25.9% | 1.02 (0–3) | 3.58 (0–18) | 1.03zł (0.0–4.3) | 6.29 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-04_HERESY_MINUS1` | 5.56 Er (1–10) | 1.2% | 26.5% | 1.03 (0–4) | 3.49 (0–19) | 1.04zł (0.0–4.3) | 6.22 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-01_COST_PLUS1` | 5.47 Er (1–10) | 0.9% | 27.3% | 1.02 (0–4) | 3.55 (0–18) | 1.05zł (0.0–4.3) | 6.32 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-10_HERESY_PLUS1` | 5.41 Er (1–10) | 1.0% | 26.1% | 1.01 (0–3) | 3.65 (0–19) | 1.03zł (0.0–4.3) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-07_COST_PLUS1` | 5.47 Er (1–10) | 1.0% | 26.5% | 1.02 (0–4) | 3.51 (0–19) | 1.03zł (0.0–4.3) | 6.29 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-04_COST_MINUS1` | 5.44 Er (1–10) | 0.8% | 25.7% | 1.01 (0–4) | 3.55 (0–17) | 1.04zł (0.0–4.3) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-03_HERESY_PLUS1` | 5.40 Er (1–10) | 0.8% | 26.0% | 1.01 (0–3) | 3.66 (0–19) | 1.03zł (0.0–4.3) | 6.39 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-02_HERESY_PLUS1` | 5.40 Er (1–10) | 0.9% | 26.0% | 1.02 (0–3) | 3.66 (0–19) | 1.03zł (0.0–4.3) | 6.39 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-05_COST_MINUS1` | 5.43 Er (1–10) | 0.7% | 26.3% | 1.01 (0–3) | 3.50 (0–17) | 1.00zł (0.0–4.3) | 6.29 (0.7–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 61 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_GC-05_COST_PLUS1` | 5.51 Er (1–10) | 1.2% | 26.4% | 1.02 (0–4) | 3.59 (0–19) | 1.04zł (0.0–4.3) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-05_HERESY_PLUS1` | 5.51 Er (1–10) | 1.2% | 26.4% | 1.02 (0–4) | 3.59 (0–19) | 1.04zł (0.0–4.3) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-03_COST_PLUS1` | 5.51 Er (1–10) | 1.2% | 26.4% | 1.02 (0–4) | 3.59 (0–19) | 0.83zł (0.0–3.7) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-05_COST_PLUS1` | 5.51 Er (1–10) | 1.2% | 26.4% | 1.02 (0–4) | 3.59 (0–19) | 1.04zł (0.0–4.3) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-05_HERESY_PLUS1` | 5.51 Er (1–10) | 1.2% | 26.4% | 1.02 (0–4) | 3.59 (0–19) | 1.04zł (0.0–4.3) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-08_COST_MINUS1` | 5.51 Er (1–10) | 1.0% | 26.3% | 1.02 (0–4) | 3.61 (0–19) | 1.04zł (0.0–5.0) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-06_COST_MINUS1` | 5.51 Er (1–10) | 1.1% | 26.4% | 1.02 (0–4) | 3.59 (0–19) | 1.25zł (0.0–5.0) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-01_COST_PLUS1` | 5.51 Er (1–10) | 1.1% | 27.1% | 1.03 (0–3) | 3.60 (0–19) | 1.05zł (0.0–4.3) | 6.32 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-04_COST_PLUS1` | 5.55 Er (1–10) | 1.2% | 27.3% | 1.03 (0–4) | 3.56 (0–18) | 0.96zł (0.0–5.0) | 6.24 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-10_COST_MINUS1` | 5.51 Er (1–10) | 1.2% | 26.4% | 1.02 (0–4) | 3.59 (0–19) | 1.22zł (0.0–4.7) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-01_COST_PLUS1` | 5.51 Er (1–10) | 1.2% | 27.0% | 1.03 (0–4) | 3.58 (0–17) | 0.99zł (0.0–4.0) | 6.25 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-08_COST_PLUS1` | 5.50 Er (1–10) | 1.1% | 26.4% | 1.02 (0–4) | 3.58 (0–18) | 1.04zł (0.0–4.3) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-04_HERESY_PLUS1` | 5.50 Er (1–10) | 1.3% | 26.4% | 1.02 (0–4) | 3.69 (0–20) | 1.04zł (0.0–4.3) | 6.44 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-03_COST_PLUS1` | 5.54 Er (1–10) | 1.1% | 27.1% | 1.03 (0–4) | 3.57 (0–18) | 0.98zł (0.0–4.7) | 6.28 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-09_COST_PLUS1` | 5.54 Er (1–10) | 1.3% | 27.1% | 1.03 (0–4) | 3.60 (0–18) | 1.01zł (0.0–4.0) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_COST_PLUS1` | 5.53 Er (1–10) | 1.1% | 27.6% | 1.02 (0–4) | 3.58 (0–18) | 1.01zł (0.0–4.3) | 6.28 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_COST_PLUS1` | 5.52 Er (1–10) | 1.1% | 27.3% | 1.03 (0–4) | 3.57 (0–18) | 1.05zł (0.0–4.3) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-07_COST_PLUS1` | 5.51 Er (1–10) | 1.1% | 26.4% | 1.05 (0–4) | 3.59 (0–19) | 1.05zł (0.0–4.3) | 6.32 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-04_COST_MINUS1` | 5.48 Er (1–10) | 1.1% | 25.2% | 1.05 (0–4) | 3.60 (0–19) | 1.05zł (0.0–4.3) | 6.33 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-10_COST_MINUS1` | 5.45 Er (1–10) | 1.0% | 26.0% | 1.01 (0–4) | 3.67 (0–18) | 0.98zł (0.0–4.0) | 6.42 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-03_COST_MINUS1` | 5.49 Er (1–10) | 1.1% | 25.3% | 1.04 (0–4) | 3.63 (0–19) | 1.05zł (0.0–4.3) | 6.33 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-01_HERESY_PLUS1` | 5.48 Er (1–10) | 1.1% | 26.3% | 1.02 (0–3) | 3.60 (0–19) | 1.03zł (0.0–4.3) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-03_HERESY_PLUS1` | 5.47 Er (1–10) | 1.0% | 26.2% | 1.02 (0–4) | 3.64 (0–19) | 1.03zł (0.0–4.3) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-02_COST_MINUS1` | 5.47 Er (1–10) | 1.1% | 25.2% | 1.08 (0–4) | 3.60 (0–19) | 1.08zł (0.0–4.7) | 6.34 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-10_COST_PLUS1` | 5.56 Er (1–10) | 1.3% | 26.1% | 1.03 (0–4) | 3.48 (0–20) | 1.10zł (0.0–4.7) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-03_COST_PLUS1` | 5.54 Er (1–10) | 1.2% | 27.2% | 1.03 (0–4) | 3.56 (0–19) | 1.05zł (0.0–4.3) | 6.27 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_MINUS1` | 5.44 Er (1–10) | 1.0% | 25.9% | 1.01 (0–3) | 3.57 (0–18) | 1.03zł (0.0–4.3) | 6.37 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-04_HERESY_PLUS1` | 5.45 Er (1–10) | 1.0% | 26.2% | 1.01 (0–4) | 3.68 (0–18) | 1.03zł (0.0–4.3) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-06_COST_PLUS1` | 5.50 Er (1–10) | 1.1% | 26.3% | 1.05 (0–4) | 3.59 (0–19) | 1.05zł (0.0–4.3) | 6.33 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_PLUS1` | 5.56 Er (1–10) | 1.3% | 27.5% | 1.03 (0–4) | 3.56 (0–19) | 0.98zł (0.0–4.0) | 6.24 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-03_COST_MINUS1` | 5.45 Er (1–10) | 0.9% | 25.8% | 1.02 (0–3) | 3.57 (0–20) | 1.04zł (0.0–4.3) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-09_HERESY_MINUS1` | 5.53 Er (1–10) | 1.1% | 26.5% | 1.03 (0–4) | 3.49 (0–19) | 1.04zł (0.0–4.3) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-02_COST_MINUS1` | 5.45 Er (1–10) | 0.9% | 25.8% | 1.01 (0–3) | 3.58 (0–18) | 1.03zł (0.0–4.3) | 6.38 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-02_COST_PLUS1` | 5.55 Er (1–10) | 1.2% | 28.1% | 1.03 (0–4) | 3.63 (0–18) | 0.98zł (0.0–4.0) | 6.27 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-06_COST_MINUS1` | 5.45 Er (1–10) | 1.0% | 25.9% | 1.02 (0–3) | 3.53 (0–18) | 1.03zł (0.0–4.3) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-10_COST_MINUS1` | 5.45 Er (1–10) | 0.9% | 25.2% | 1.12 (0–4) | 3.63 (0–19) | 1.06zł (0.0–4.3) | 6.36 (1.0–10.0) | 🟢 W NORMIE |
| `L3_SO-08_HERESY_MINUS1` | 5.56 Er (1–10) | 1.4% | 26.6% | 1.03 (0–4) | 3.53 (0–19) | 1.04zł (0.0–4.3) | 6.19 (0.5–10.0) | 🟢 W NORMIE |
| `L3_GC-10_HERESY_MINUS1` | 5.54 Er (1–10) | 1.2% | 26.5% | 1.03 (0–3) | 3.39 (0–17) | 1.03zł (0.0–4.3) | 6.14 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_HERESY_MINUS1` | 5.52 Er (1–10) | 1.2% | 26.5% | 1.03 (0–4) | 3.54 (0–17) | 1.04zł (0.0–4.3) | 6.19 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-04_HERESY_PLUS1` | 5.39 Er (1–10) | 0.8% | 26.0% | 1.01 (0–3) | 3.66 (0–19) | 1.02zł (0.0–4.3) | 6.39 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_MINUS1` | 5.53 Er (1–10) | 1.3% | 26.5% | 1.03 (0–4) | 3.43 (0–19) | 1.04zł (0.0–4.3) | 5.91 (0.3–10.0) | 🟢 W NORMIE |
| `L3_KB-03_COST_PLUS1` | 5.51 Er (1–10) | 1.0% | 27.4% | 1.02 (0–4) | 3.49 (0–18) | 1.05zł (0.0–4.7) | 6.24 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-10_HERESY_MINUS1` | 5.61 Er (1–10) | 1.3% | 26.7% | 1.04 (0–4) | 3.51 (0–19) | 1.05zł (0.0–4.3) | 6.27 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-01_COST_MINUS1` | 5.46 Er (1–10) | 0.9% | 25.8% | 1.02 (0–3) | 3.55 (0–17) | 1.05zł (0.0–4.3) | 6.32 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-10_HERESY_PLUS1` | 5.44 Er (1–10) | 1.1% | 26.1% | 1.01 (0–3) | 3.84 (0–20) | 1.04zł (0.0–5.0) | 6.39 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-10_COST_PLUS1` | 5.64 Er (1–10) | 1.3% | 25.6% | 0.88 (0–4) | 3.45 (0–19) | 1.04zł (0.0–4.3) | 6.25 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-02_HERESY_PLUS1` | 5.48 Er (1–10) | 1.1% | 26.5% | 1.02 (0–4) | 3.66 (0–19) | 1.04zł (0.0–4.3) | 6.36 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-07_COST_MINUS1` | 5.49 Er (1–10) | 1.0% | 26.0% | 1.02 (0–4) | 3.56 (0–19) | 1.02zł (0.0–4.3) | 6.33 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_HERESY_PLUS1` | 5.44 Er (1–10) | 0.9% | 26.1% | 1.01 (0–4) | 3.76 (0–19) | 1.03zł (0.0–4.3) | 6.51 (1.3–10.0) | 🟢 W NORMIE |
| `L3_KB-03_COST_MINUS1` | 5.45 Er (1–10) | 0.8% | 25.7% | 1.01 (0–3) | 3.56 (0–17) | 1.04zł (0.0–4.3) | 6.33 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-10_HERESY_MINUS1` | 5.59 Er (1–10) | 1.2% | 26.7% | 1.04 (0–3) | 3.28 (0–19) | 1.04zł (0.0–4.3) | 6.14 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-02_COST_PLUS1` | 5.58 Er (1–10) | 1.4% | 28.8% | 1.04 (0–4) | 3.67 (0–19) | 1.06zł (0.0–4.3) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_PLUS1` | 5.42 Er (1–10) | 0.9% | 26.0% | 1.01 (0–4) | 3.83 (0–19) | 1.03zł (0.0–4.3) | 6.51 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-10_COST_PLUS1` | 5.63 Er (1–10) | 1.4% | 27.6% | 1.04 (0–4) | 3.65 (0–18) | 1.07zł (0.0–4.3) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-09_HERESY_PLUS1` | 5.52 Er (1–10) | 1.2% | 26.4% | 1.02 (0–4) | 3.77 (0–19) | 1.05zł (0.0–4.3) | 6.37 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-05_COST_PLUS1` | 5.56 Er (1–10) | 1.4% | 27.1% | 1.03 (0–4) | 3.59 (0–19) | 1.04zł (0.0–4.7) | 6.32 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-02_COST_MINUS1` | 5.41 Er (1–10) | 0.7% | 25.9% | 1.01 (0–4) | 3.52 (0–19) | 1.04zł (0.0–4.3) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-10_HERESY_PLUS1` | 5.37 Er (1–10) | 1.0% | 25.9% | 1.00 (0–4) | 3.82 (0–19) | 1.03zł (0.0–4.3) | 6.33 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-10_COST_MINUS1` | 5.33 Er (1–10) | 0.5% | 26.0% | 1.00 (0–4) | 3.54 (0–18) | 0.99zł (0.0–4.3) | 6.34 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-09_COST_MINUS1` | 5.36 Er (1–10) | 0.5% | 26.0% | 1.00 (0–4) | 3.50 (0–17) | 0.98zł (0.0–4.3) | 6.29 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-09_COST_PLUS1` | 5.68 Er (1–10) | 1.5% | 28.2% | 1.05 (0–4) | 3.81 (0–20) | 1.03zł (0.0–4.3) | 6.37 (0.7–10.0) | 🟢 W NORMIE |

</details>