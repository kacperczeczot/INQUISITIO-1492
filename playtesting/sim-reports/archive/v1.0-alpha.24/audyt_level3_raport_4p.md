# Raport Precyzyjnego Audytu Poziomu 3 (Parametry Pojedynczych Kart) — Wersja Balansu: v1.0-alpha.24

**Wersja Balansu:** `v1.0-alpha.24` | **Data:** 2026-08-22 18:28 | **Przeanalizowano Wariantów Kart:** 270 | **Próba:** 3000 gier/setup | **Czas:** 1290.19s
**Filtry:** Parametry: `cost,heresy` | Frakcja: `all` | Karta: `Wszystkie`
**Wynik Bazy Poziomu 3 (Global):** `🟡 84.3 pkt` | 3p: `0.0 pkt` | 4p: `84.3 pkt` | 5p: `0.0 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (31)

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | Baza (Bieżące parametry wszystkich kart) | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KB-05_HERESY_PLUS1` | KB-05 (List Żelazny): heresy 0 → 1 | 84.3 → 🟡 ** 86.7** (`⬆️ +2.4`) | 0.0 | 84.3 → 86.7 (`⬆️ +2.4`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-05_HERESY_SET1` | KB-05 (List Żelazny): dodaj heresy = 1 | 84.3 → 🟡 ** 86.7** (`⬆️ +2.4`) | 0.0 | 84.3 → 86.7 (`⬆️ +2.4`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-04_HERESY_PLUS1` | KB-04 (Faworyt Dworu): heresy 1 → 2 | 84.3 → 🟡 ** 86.6** (`⬆️ +2.3`) | 0.0 | 84.3 → 86.6 (`⬆️ +2.3`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-09_HERESY_PLUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 2 | 84.3 → 🟡 ** 86.6** (`⬆️ +2.3`) | 0.0 | 84.3 → 86.6 (`⬆️ +2.3`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 2 → 3 | 84.3 → 🟡 ** 86.1** (`⬆️ +1.8`) | 0.0 | 84.3 → 86.1 (`⬆️ +1.8`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-09_COST_MINUS1` | KT-09 (Fragment Kodeksu): cost 2 → 1 | 84.3 → 🟡 ** 85.6** (`⬆️ +1.3`) | 0.0 | 84.3 → 85.6 (`⬆️ +1.3`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-07_HERESY_SET2` | SO-07 (Przesłuchanie Oficjum): dodaj heresy = 2 | 84.3 → 🟡 ** 85.5** (`⬆️ +1.2`) | 0.0 | 84.3 → 85.5 (`⬆️ +1.2`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-12_COST_PLUS1` | CAA-12 (Skrytka w Murach): cost 0 → 1 | 84.3 → 🟡 ** 85.0** (`⬆️ +0.7`) | 0.0 | 84.3 → 85.0 (`⬆️ +0.7`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-01_COST_PLUS1` | GC-01 (Przekupiony Strażnik): cost 2 → 3 | 84.3 → 🟡 ** 84.9** (`⬆️ +0.6`) | 0.0 | 84.3 → 84.9 (`⬆️ +0.6`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-07_HERESY_PLUS1` | SO-07 (Przesłuchanie Oficjum): heresy 0 → 1 | 84.3 → 🟡 ** 84.9** (`⬆️ +0.6`) | 0.0 | 84.3 → 84.9 (`⬆️ +0.6`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-07_HERESY_SET1` | SO-07 (Przesłuchanie Oficjum): dodaj heresy = 1 | 84.3 → 🟡 ** 84.9** (`⬆️ +0.6`) | 0.0 | 84.3 → 84.9 (`⬆️ +0.6`) | 0.0 | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-07_COST_PLUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 3 | 84.3 → 🟡 ** 84.8** (`⬆️ +0.5`) | 0.0 | 84.3 → 84.8 (`⬆️ +0.5`) | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-01_COST_PLUS2` | GC-01 (Przekupiony Strażnik): cost 2 → 4 (+2) | 84.3 → 🟡 ** 84.8** (`⬆️ +0.5`) | 0.0 | 84.3 → 84.8 (`⬆️ +0.5`) | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-02_COST_PLUS1` | GC-02 (Czarny Rynek): cost 1 → 2 | 84.3 → 🟡 ** 84.7** (`⬆️ +0.4`) | 0.0 | 84.3 → 84.7 (`⬆️ +0.4`) | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-10_COST_MINUS1` | GC-10 (Upadek Domu): cost 4 → 3 | 84.3 → 🟡 ** 84.7** (`⬆️ +0.4`) | 0.0 | 84.3 → 84.7 (`⬆️ +0.4`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-03_HERESY_PLUS1` | KT-03 (Zakazana Wiedza): heresy 0 → 1 | 84.3 → 🟡 ** 84.7** (`⬆️ +0.4`) | 0.0 | 84.3 → 84.7 (`⬆️ +0.4`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-03_HERESY_SET1` | KT-03 (Zakazana Wiedza): dodaj heresy = 1 | 84.3 → 🟡 ** 84.7** (`⬆️ +0.4`) | 0.0 | 84.3 → 84.7 (`⬆️ +0.4`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KB-07_HERESY_PLUS1` | KB-07 (Szantaż Pieczęcią): heresy 0 → 1 | 84.3 → 🟡 ** 84.6** (`⬆️ +0.3`) | 0.0 | 84.3 → 84.6 (`⬆️ +0.3`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KB-07_HERESY_SET1` | KB-07 (Szantaż Pieczęcią): dodaj heresy = 1 | 84.3 → 🟡 ** 84.6** (`⬆️ +0.3`) | 0.0 | 84.3 → 84.6 (`⬆️ +0.3`) | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-10_COST_MINUS1` | SO-10 (Oczyść Miasto): cost 5 → 4 | 84.3 → 🟡 ** 84.6** (`⬆️ +0.3`) | 0.0 | 84.3 → 84.6 (`⬆️ +0.3`) | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-03_COST_PLUS1` | CAA-03 (Cień na Rynku): cost 0 → 1 | 84.3 → 🟡 ** 84.5** (`⬆️ +0.2`) | 0.0 | 84.3 → 84.5 (`⬆️ +0.2`) | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-11_COST_PLUS1` | GC-11 (Fałszywe Świadectwo Cechu): cost 0 → 1 | 84.3 → 🟡 ** 84.5** (`⬆️ +0.2`) | 0.0 | 84.3 → 84.5 (`⬆️ +0.2`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-04_COST_MINUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 0 | 84.3 → 🟡 ** 84.5** (`⬆️ +0.2`) | 0.0 | 84.3 → 84.5 (`⬆️ +0.2`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-08_HERESY_SET2` | KT-08 (Areszt Wiedzy): dodaj heresy = 2 | 84.3 → 🟡 ** 84.5** (`⬆️ +0.2`) | 0.0 | 84.3 → 84.5 (`⬆️ +0.2`) | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-09_COST_PLUS1` | SO-09 (Świadek Koronny): cost 1 → 2 | 84.3 → 🟡 ** 84.5** (`⬆️ +0.2`) | 0.0 | 84.3 → 84.5 (`⬆️ +0.2`) | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-06_COST_PLUS1` | CAA-06 (Ucieczka z Lochów): cost 0 → 1 | 84.3 → 🟡 ** 84.4** (`⬆️ +0.1`) | 0.0 | 84.3 → 84.4 (`⬆️ +0.1`) | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-09_COST_PLUS1` | CAA-09 (Kurier Relikwii): cost 0 → 1 | 84.3 → 🟡 ** 84.4** (`⬆️ +0.1`) | 0.0 | 84.3 → 84.4 (`⬆️ +0.1`) | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-01_COST_MINUS1` | GC-01 (Przekupiony Strażnik): cost 2 → 1 | 84.3 → 🟡 ** 84.4** (`⬆️ +0.1`) | 0.0 | 84.3 → 84.4 (`⬆️ +0.1`) | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-08_HERESY_PLUS1` | SO-08 (Nasłanie Inkwizytora): heresy 0 → 1 | 84.3 → 🟡 ** 84.4** (`⬆️ +0.1`) | 0.0 | 84.3 → 84.4 (`⬆️ +0.1`) | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-08_HERESY_SET1` | SO-08 (Nasłanie Inkwizytora): dodaj heresy = 1 | 84.3 → 🟡 ** 84.4** (`⬆️ +0.1`) | 0.0 | 84.3 → 84.4 (`⬆️ +0.1`) | 0.0 | ⚪ OPTYMALNY |

<details>
<summary><b>🔻 Pokaż pozostałe 239 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 0 → 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-01_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-01_HERESY_SET1` | CAA-01 (Przejście Podziemiami): dodaj heresy = 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-01_HERESY_SET2` | CAA-01 (Przejście Podziemiami): dodaj heresy = 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-04_COST_PLUS1` | CAA-04 (Fałszywy Trop): cost 0 → 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-04_HERESY_PLUS1` | CAA-04 (Fałszywy Trop): heresy 0 → 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-04_HERESY_SET1` | CAA-04 (Fałszywy Trop): dodaj heresy = 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-04_HERESY_SET2` | CAA-04 (Fałszywy Trop): dodaj heresy = 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-08_COST_PLUS1` | CAA-08 (Kaptur Nocy): cost 1 → 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-08_COST_MINUS1` | CAA-08 (Kaptur Nocy): cost 1 → 0 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-08_HERESY_PLUS1` | CAA-08 (Kaptur Nocy): heresy 0 → 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-08_HERESY_SET1` | CAA-08 (Kaptur Nocy): dodaj heresy = 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-08_HERESY_SET2` | CAA-08 (Kaptur Nocy): dodaj heresy = 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-11_COST_PLUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-11_COST_MINUS1` | CAA-11 (Nocna Zmiana Warty): cost 1 → 0 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-11_HERESY_PLUS1` | CAA-11 (Nocna Zmiana Warty): heresy 0 → 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-11_HERESY_SET1` | CAA-11 (Nocna Zmiana Warty): dodaj heresy = 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-11_HERESY_SET2` | CAA-11 (Nocna Zmiana Warty): dodaj heresy = 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-01_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): heresy 1 → 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-01_HERESY_MINUS1` | GC-01 (Przekupiony Strażnik): heresy 1 → 0 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-03_HERESY_PLUS1` | GC-03 (Podrzucenie Księgi): heresy 0 → 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-03_HERESY_SET1` | GC-03 (Podrzucenie Księgi): dodaj heresy = 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-03_HERESY_SET2` | GC-03 (Podrzucenie Księgi): dodaj heresy = 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-05_COST_PLUS1` | GC-05 (Fałszywy Świadek): cost 0 → 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-05_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): heresy 0 → 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-05_HERESY_SET1` | GC-05 (Fałszywy Świadek): dodaj heresy = 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-05_HERESY_SET2` | GC-05 (Fałszywy Świadek): dodaj heresy = 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 1 → 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-08_HERESY_MINUS1` | GC-08 (Zatrute Złoto): heresy 1 → 0 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-11_HERESY_PLUS1` | GC-11 (Fałszywe Świadectwo Cechu): heresy 2 → 3 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-11_HERESY_MINUS1` | GC-11 (Fałszywe Świadectwo Cechu): heresy 2 → 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-12_COST_PLUS1` | GC-12 (Złodziejski Zwiad): cost 0 → 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-12_HERESY_PLUS1` | GC-12 (Złodziejski Zwiad): heresy 2 → 3 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-12_HERESY_MINUS1` | GC-12 (Złodziejski Zwiad): heresy 2 → 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KB-01_HERESY_PLUS1` | KB-01 (Rozkaz Dworu): heresy 1 → 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KB-01_HERESY_MINUS1` | KB-01 (Rozkaz Dworu): heresy 1 → 0 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KB-03_HERESY_PLUS1` | KB-03 (Plotka Dworska): heresy 1 → 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KB-03_HERESY_MINUS1` | KB-03 (Plotka Dworska): heresy 1 → 0 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KB-11_HERESY_PLUS1` | KB-11 (Tajny Emisariusz): heresy 0 → 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KB-11_HERESY_SET1` | KB-11 (Tajny Emisariusz): dodaj heresy = 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KB-11_HERESY_SET2` | KB-11 (Tajny Emisariusz): dodaj heresy = 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-01_COST_MINUS1` | KT-01 (Rytuał Przejścia): cost 1 → 0 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-01_HERESY_PLUS1` | KT-01 (Rytuał Przejścia): heresy 0 → 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-01_HERESY_SET1` | KT-01 (Rytuał Przejścia): dodaj heresy = 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-01_HERESY_SET2` | KT-01 (Rytuał Przejścia): dodaj heresy = 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-02_HERESY_PLUS1` | KT-02 (Transmutacja Złota): heresy 0 → 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-02_HERESY_SET1` | KT-02 (Transmutacja Złota): dodaj heresy = 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-02_HERESY_SET2` | KT-02 (Transmutacja Złota): dodaj heresy = 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-04_HERESY_PLUS1` | KT-04 (Zwierciadło Herezji): heresy 0 → 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-04_HERESY_SET1` | KT-04 (Zwierciadło Herezji): dodaj heresy = 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-04_HERESY_SET2` | KT-04 (Zwierciadło Herezji): dodaj heresy = 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-10_HERESY_PLUS1` | KT-10 (Pieczęć Salomona): heresy 2 → 3 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-11_HERESY_PLUS1` | KT-11 (Medytacja Sefirot): heresy 0 → 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-11_HERESY_SET1` | KT-11 (Medytacja Sefirot): dodaj heresy = 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-11_HERESY_SET2` | KT-11 (Medytacja Sefirot): dodaj heresy = 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-12_HERESY_PLUS1` | KT-12 (Strażnik Archiwum): heresy 1 → 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-12_HERESY_MINUS1` | KT-12 (Strażnik Archiwum): heresy 1 → 0 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-01_COST_PLUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-01_COST_MINUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 0 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-01_HERESY_PLUS1` | SO-01 (Patrol Familiariuszy): heresy 0 → 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-01_HERESY_SET1` | SO-01 (Patrol Familiariuszy): dodaj heresy = 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-01_HERESY_SET2` | SO-01 (Patrol Familiariuszy): dodaj heresy = 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-02_COST_MINUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 0 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-03_COST_PLUS1` | SO-03 (Podejrzenie): cost 2 → 3 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-03_COST_MINUS1` | SO-03 (Podejrzenie): cost 2 → 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-03_HERESY_PLUS1` | SO-03 (Podejrzenie): heresy 2 → 3 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-03_HERESY_MINUS1` | SO-03 (Podejrzenie): heresy 2 → 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-04_HERESY_SET2` | SO-04 (Publiczne Ostrzeżenie): dodaj heresy = 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-05_HERESY_PLUS1` | SO-05 (Wezwanie do Trybunału): heresy 0 → 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-05_HERESY_SET1` | SO-05 (Wezwanie do Trybunału): dodaj heresy = 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-05_HERESY_SET2` | SO-05 (Wezwanie do Trybunału): dodaj heresy = 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-10_HERESY_PLUS1` | SO-10 (Oczyść Miasto): heresy 1 → 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-10_HERESY_MINUS1` | SO-10 (Oczyść Miasto): heresy 1 → 0 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-11_COST_PLUS1` | SO-11 (Dekret Czystości Wiary): cost 1 → 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-11_COST_MINUS1` | SO-11 (Dekret Czystości Wiary): cost 1 → 0 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-11_HERESY_PLUS1` | SO-11 (Dekret Czystości Wiary): heresy 1 → 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-11_HERESY_MINUS1` | SO-11 (Dekret Czystości Wiary): heresy 1 → 0 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-12_COST_PLUS1` | SO-12 (Straż Trybunalska): cost 1 → 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-12_HERESY_PLUS1` | SO-12 (Straż Trybunalska): heresy 0 → 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-12_HERESY_SET1` | SO-12 (Straż Trybunalska): dodaj heresy = 1 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-12_HERESY_SET2` | SO-12 (Straż Trybunalska): dodaj heresy = 2 | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-01_COST_PLUS2` | CAA-01 (Przejście Podziemiami): cost 0 → 2 (+2) | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-01_HERESY_PLUS2` | CAA-01 (Przejście Podziemiami): heresy 0 → 2 (+2) | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-01_HERESY_PLUS2` | GC-01 (Przekupiony Strażnik): heresy 1 → 3 (+2) | 🟡 ** 84.3** | 0.0 | 84.3 | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-10_COST_MINUS1` | CAA-10 (Echo Alhambry): cost 1 → 0 | 84.3 → 🟡 ** 84.2** (`-0.1`) | 0.0 | 84.3 → 84.2 (`-0.1`) | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-03_COST_PLUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 2 | 84.3 → 🟡 ** 84.2** (`-0.1`) | 0.0 | 84.3 → 84.2 (`-0.1`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KB-08_HERESY_PLUS1` | KB-08 (Przekupstwo Sędziego): heresy 0 → 1 | 84.3 → 🟡 ** 84.2** (`-0.1`) | 0.0 | 84.3 → 84.2 (`-0.1`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KB-08_HERESY_SET1` | KB-08 (Przekupstwo Sędziego): dodaj heresy = 1 | 84.3 → 🟡 ** 84.2** (`-0.1`) | 0.0 | 84.3 → 84.2 (`-0.1`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 84.3 → 🟡 ** 84.2** (`-0.1`) | 0.0 | 84.3 → 84.2 (`-0.1`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-06_COST_PLUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 3 | 84.3 → 🟡 ** 84.2** (`-0.1`) | 0.0 | 84.3 → 84.2 (`-0.1`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-08_HERESY_PLUS1` | KT-08 (Areszt Wiedzy): heresy 0 → 1 | 84.3 → 🟡 ** 84.2** (`-0.1`) | 0.0 | 84.3 → 84.2 (`-0.1`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-08_HERESY_SET1` | KT-08 (Areszt Wiedzy): dodaj heresy = 1 | 84.3 → 🟡 ** 84.2** (`-0.1`) | 0.0 | 84.3 → 84.2 (`-0.1`) | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-04_COST_MINUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 0 | 84.3 → 🟡 ** 84.2** (`-0.1`) | 0.0 | 84.3 → 84.2 (`-0.1`) | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-05_COST_PLUS1` | SO-05 (Wezwanie do Trybunału): cost 0 → 1 | 84.3 → 🟡 ** 84.2** (`-0.1`) | 0.0 | 84.3 → 84.2 (`-0.1`) | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-07_COST_MINUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 1 | 84.3 → 🟡 ** 84.2** (`-0.1`) | 0.0 | 84.3 → 84.2 (`-0.1`) | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-07_COST_PLUS1` | GC-07 (Skrytobójstwo): cost 0 → 1 | 84.3 → 🟡 ** 84.1** (`-0.2`) | 0.0 | 84.3 → 84.1 (`-0.2`) | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 1 → 2 | 84.3 → 🟡 ** 84.1** (`-0.2`) | 0.0 | 84.3 → 84.1 (`-0.2`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-03_COST_PLUS1` | KT-03 (Zakazana Wiedza): cost 0 → 1 | 84.3 → 🟡 ** 84.1** (`-0.2`) | 0.0 | 84.3 → 84.1 (`-0.2`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-04_COST_PLUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 2 | 84.3 → 🟡 ** 84.1** (`-0.2`) | 0.0 | 84.3 → 84.1 (`-0.2`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-11_COST_MINUS1` | KT-11 (Medytacja Sefirot): cost 2 → 1 | 84.3 → 🟡 ** 84.1** (`-0.2`) | 0.0 | 84.3 → 84.1 (`-0.2`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-12_COST_PLUS1` | KT-12 (Strażnik Archiwum): cost 0 → 1 | 84.3 → 🟡 ** 84.1** (`-0.2`) | 0.0 | 84.3 → 84.1 (`-0.2`) | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-04_HERESY_PLUS1` | SO-04 (Publiczne Ostrzeżenie): heresy 0 → 1 | 84.3 → 🟡 ** 84.1** (`-0.2`) | 0.0 | 84.3 → 84.1 (`-0.2`) | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-04_HERESY_SET1` | SO-04 (Publiczne Ostrzeżenie): dodaj heresy = 1 | 84.3 → 🟡 ** 84.1** (`-0.2`) | 0.0 | 84.3 → 84.1 (`-0.2`) | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-06_HERESY_SET2` | SO-06 (Areszt Trybunalski): dodaj heresy = 2 | 84.3 → 🟡 ** 84.1** (`-0.2`) | 0.0 | 84.3 → 84.1 (`-0.2`) | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-04_COST_MINUS1` | GC-04 (Informator): cost 1 → 0 | 84.3 → 🟡 ** 84.0** (`-0.3`) | 0.0 | 84.3 → 84.0 (`-0.3`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 84.3 → 🟡 ** 84.0** (`-0.3`) | 0.0 | 84.3 → 84.0 (`-0.3`) | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-08_COST_PLUS1` | SO-08 (Nasłanie Inkwizytora): cost 0 → 1 | 84.3 → 🟡 ** 84.0** (`-0.3`) | 0.0 | 84.3 → 84.0 (`-0.3`) | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-05_COST_PLUS2` | GC-05 (Fałszywy Świadek): cost 0 → 2 (+2) | 84.3 → 🟡 ** 84.0** (`-0.3`) | 0.0 | 84.3 → 84.0 (`-0.3`) | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 0 → 1 | 84.3 → 🟡 ** 83.9** (`-0.4`) | 0.0 | 84.3 → 83.9 (`-0.4`) | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-05_COST_PLUS1` | CAA-05 (Ukryty Kurier): cost 0 → 1 | 84.3 → 🟡 ** 83.9** (`-0.4`) | 0.0 | 84.3 → 83.9 (`-0.4`) | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-03_COST_MINUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 0 | 84.3 → 🟡 ** 83.9** (`-0.4`) | 0.0 | 84.3 → 83.9 (`-0.4`) | 0.0 | ⚪ OPTYMALNY |
| `L3_GC-09_COST_PLUS1` | GC-09 (Lista Dłużników): cost 3 → 4 | 84.3 → 🟡 ** 83.9** (`-0.4`) | 0.0 | 84.3 → 83.9 (`-0.4`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KB-01_COST_MINUS1` | KB-01 (Rozkaz Dworu): cost 1 → 0 | 84.3 → 🟡 ** 83.9** (`-0.4`) | 0.0 | 84.3 → 83.9 (`-0.4`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KB-03_COST_MINUS1` | KB-03 (Plotka Dworska): cost 1 → 0 | 84.3 → 🟡 ** 83.9** (`-0.4`) | 0.0 | 84.3 → 83.9 (`-0.4`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KB-11_COST_PLUS1` | KB-11 (Tajny Emisariusz): cost 1 → 2 | 84.3 → 🟡 ** 83.9** (`-0.4`) | 0.0 | 84.3 → 83.9 (`-0.4`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-07_HERESY_PLUS1` | KT-07 (Archiwum Ukryte): heresy 1 → 2 | 84.3 → 🟡 ** 83.9** (`-0.4`) | 0.0 | 84.3 → 83.9 (`-0.4`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KT-08_COST_MINUS1` | KT-08 (Areszt Wiedzy): cost 1 → 0 | 84.3 → 🟡 ** 83.9** (`-0.4`) | 0.0 | 84.3 → 83.9 (`-0.4`) | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-06_COST_PLUS1` | SO-06 (Areszt Trybunalski): cost 2 → 3 | 84.3 → 🟡 ** 83.9** (`-0.4`) | 0.0 | 84.3 → 83.9 (`-0.4`) | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-09_HERESY_PLUS1` | SO-09 (Świadek Koronny): heresy 0 → 1 | 84.3 → 🟡 ** 83.9** (`-0.4`) | 0.0 | 84.3 → 83.9 (`-0.4`) | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-09_HERESY_SET1` | SO-09 (Świadek Koronny): dodaj heresy = 1 | 84.3 → 🟡 ** 83.9** (`-0.4`) | 0.0 | 84.3 → 83.9 (`-0.4`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KB-07_COST_PLUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 3 | 84.3 → 🟡 ** 83.8** (`-0.5`) | 0.0 | 84.3 → 83.8 (`-0.5`) | 0.0 | ⚪ OPTYMALNY |
| `L3_SO-10_COST_PLUS1` | SO-10 (Oczyść Miasto): cost 5 → 6 | 84.3 → 🟡 ** 83.8** (`-0.5`) | 0.0 | 84.3 → 83.8 (`-0.5`) | 0.0 | ⚪ OPTYMALNY |
| `L3_CAA-05_COST_PLUS2` | CAA-05 (Ukryty Kurier): cost 0 → 2 (+2) | 84.3 → 🟡 ** 83.8** (`-0.5`) | 0.0 | 84.3 → 83.8 (`-0.5`) | 0.0 | ⚪ OPTYMALNY |
| `L3_KB-01_COST_PLUS1` | KB-01 (Rozkaz Dworu): cost 1 → 2 | 84.3 → 🟡 ** 83.7** (`-0.6`) | 0.0 | 84.3 → 83.7 (`-0.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_COST_PLUS1` | KT-08 (Areszt Wiedzy): cost 1 → 2 | 84.3 → 🟡 ** 83.7** (`-0.6`) | 0.0 | 84.3 → 83.7 (`-0.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_COST_PLUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 2 | 84.3 → 🟡 ** 83.7** (`-0.6`) | 0.0 | 84.3 → 83.7 (`-0.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): heresy 0 → 1 | 84.3 → 🟡 ** 83.7** (`-0.6`) | 0.0 | 84.3 → 83.7 (`-0.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_HERESY_SET1` | SO-06 (Areszt Trybunalski): dodaj heresy = 1 | 84.3 → 🟡 ** 83.7** (`-0.6`) | 0.0 | 84.3 → 83.7 (`-0.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_COST_MINUS1` | SO-09 (Świadek Koronny): cost 1 → 0 | 84.3 → 🟡 ** 83.7** (`-0.6`) | 0.0 | 84.3 → 83.7 (`-0.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_COST_PLUS1` | KB-08 (Przekupstwo Sędziego): cost 2 → 3 | 84.3 → 🟡 ** 83.6** (`-0.7`) | 0.0 | 84.3 → 83.6 (`-0.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_COST_MINUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 1 | 84.3 → 🟡 ** 83.6** (`-0.7`) | 0.0 | 84.3 → 83.6 (`-0.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_COST_PLUS1` | KT-07 (Archiwum Ukryte): cost 1 → 2 | 84.3 → 🟡 ** 83.6** (`-0.7`) | 0.0 | 84.3 → 83.6 (`-0.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-11_COST_PLUS1` | KT-11 (Medytacja Sefirot): cost 2 → 3 | 84.3 → 🟡 ** 83.6** (`-0.7`) | 0.0 | 84.3 → 83.6 (`-0.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_HERESY_PLUS1` | GC-02 (Czarny Rynek): heresy 1 → 2 | 84.3 → 🟡 ** 83.5** (`-0.8`) | 0.0 | 84.3 → 83.5 (`-0.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_HERESY_SET2` | SO-08 (Nasłanie Inkwizytora): dodaj heresy = 2 | 84.3 → 🟡 ** 83.5** (`-0.8`) | 0.0 | 84.3 → 83.5 (`-0.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_COST_PLUS1` | CAA-10 (Echo Alhambry): cost 1 → 2 | 84.3 → 🟡 ** 83.4** (`-0.9`) | 0.0 | 84.3 → 83.4 (`-0.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_HERESY_SET2` | SO-09 (Świadek Koronny): dodaj heresy = 2 | 84.3 → 🟡 ** 83.4** (`-0.9`) | 0.0 | 84.3 → 83.4 (`-0.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_COST_MINUS1` | GC-02 (Czarny Rynek): cost 1 → 0 | 84.3 → 🟡 ** 83.3** (`-1.0`) | 0.0 | 84.3 → 83.3 (`-1.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_COST_MINUS1` | GC-06 (Szantaż): cost 2 → 1 | 84.3 → 🟡 ** 83.3** (`-1.0`) | 0.0 | 84.3 → 83.3 (`-1.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_COST_PLUS1` | KB-03 (Plotka Dworska): cost 1 → 2 | 84.3 → 🟡 ** 83.3** (`-1.0`) | 0.0 | 84.3 → 83.3 (`-1.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_HERESY_PLUS1` | KT-06 (Przesłuchanie Imienia): heresy 0 → 1 | 84.3 → 🟡 ** 83.3** (`-1.0`) | 0.0 | 84.3 → 83.3 (`-1.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_HERESY_SET1` | KT-06 (Przesłuchanie Imienia): dodaj heresy = 1 | 84.3 → 🟡 ** 83.3** (`-1.0`) | 0.0 | 84.3 → 83.3 (`-1.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_COST_MINUS1` | SO-06 (Areszt Trybunalski): cost 2 → 1 | 84.3 → 🟡 ** 83.3** (`-1.0`) | 0.0 | 84.3 → 83.3 (`-1.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_COST_MINUS1` | GC-08 (Zatrute Złoto): cost 1 → 0 | 84.3 → 🟡 ** 83.2** (`-1.1`) | 0.0 | 84.3 → 83.2 (`-1.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_COST_MINUS1` | KT-10 (Pieczęć Salomona): cost 2 → 1 | 84.3 → 🟡 ** 83.2** (`-1.1`) | 0.0 | 84.3 → 83.2 (`-1.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_HERESY_PLUS1` | CAA-05 (Ukryty Kurier): heresy 0 → 1 | 84.3 → 🟡 ** 83.1** (`-1.2`) | 0.0 | 84.3 → 83.1 (`-1.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_HERESY_SET1` | CAA-05 (Ukryty Kurier): dodaj heresy = 1 | 84.3 → 🟡 ** 83.1** (`-1.2`) | 0.0 | 84.3 → 83.1 (`-1.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_COST_MINUS1` | GC-09 (Lista Dłużników): cost 3 → 2 | 84.3 → 🟡 ** 83.1** (`-1.2`) | 0.0 | 84.3 → 83.1 (`-1.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_HERESY_PLUS1` | KB-12 (Szantaż Salonowy): heresy 0 → 1 | 84.3 → 🟡 ** 83.1** (`-1.2`) | 0.0 | 84.3 → 83.1 (`-1.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_HERESY_SET1` | KB-12 (Szantaż Salonowy): dodaj heresy = 1 | 84.3 → 🟡 ** 83.1** (`-1.2`) | 0.0 | 84.3 → 83.1 (`-1.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_COST_PLUS1` | GC-04 (Informator): cost 1 → 2 | 84.3 → 🟡 ** 83.0** (`-1.3`) | 0.0 | 84.3 → 83.0 (`-1.3`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_COST_PLUS1` | GC-10 (Upadek Domu): cost 4 → 5 | 84.3 → 🟡 ** 83.0** (`-1.3`) | 0.0 | 84.3 → 83.0 (`-1.3`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_COST_PLUS1` | KB-12 (Szantaż Salonowy): cost 1 → 2 | 84.3 → 🟡 ** 83.0** (`-1.3`) | 0.0 | 84.3 → 83.0 (`-1.3`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_HERESY_PLUS1` | CAA-03 (Cień na Rynku): heresy 1 → 2 | 84.3 → 🟡 ** 82.9** (`-1.4`) | 0.0 | 84.3 → 82.9 (`-1.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-12_COST_MINUS1` | SO-12 (Straż Trybunalska): cost 1 → 0 | 84.3 → 🟡 ** 82.9** (`-1.4`) | 0.0 | 84.3 → 82.9 (`-1.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_COST_PLUS1` | GC-06 (Szantaż): cost 2 → 3 | 84.3 → 🟡 ** 82.8** (`-1.5`) | 0.0 | 84.3 → 82.8 (`-1.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 84.3 → 🟡 ** 82.4** (`-1.9`) | 0.0 | 84.3 → 82.4 (`-1.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_HERESY_MINUS1` | GC-10 (Upadek Domu): heresy 2 → 1 | 84.3 → 🟡 ** 82.4** (`-1.9`) | 0.0 | 84.3 → 82.4 (`-1.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_COST_MINUS1` | KT-07 (Archiwum Ukryte): cost 1 → 0 | 84.3 → 🟡 ** 82.3** (`-2.0`) | 0.0 | 84.3 → 82.3 (`-2.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-12_HERESY_PLUS1` | CAA-12 (Skrytka w Murach): heresy 0 → 1 | 84.3 → 🟡 ** 81.8** (`-2.5`) | 0.0 | 84.3 → 81.8 (`-2.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-12_HERESY_SET1` | CAA-12 (Skrytka w Murach): dodaj heresy = 1 | 84.3 → 🟡 ** 81.8** (`-2.5`) | 0.0 | 84.3 → 81.8 (`-2.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_HERESY_PLUS1` | GC-10 (Upadek Domu): heresy 2 → 3 | 84.3 → 🟡 ** 81.8** (`-2.5`) | 0.0 | 84.3 → 81.8 (`-2.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_COST_PLUS1` | KB-02 (Pobór Podatków): cost 1 → 2 | 84.3 → 🟡 ** 81.7** (`-2.6`) | 0.0 | 84.3 → 81.7 (`-2.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_HERESY_PLUS1` | KB-02 (Pobór Podatków): heresy 0 → 1 | 84.3 → 🟡 ** 81.7** (`-2.6`) | 0.0 | 84.3 → 81.7 (`-2.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_HERESY_SET1` | KB-02 (Pobór Podatków): dodaj heresy = 1 | 84.3 → 🟡 ** 81.7** (`-2.6`) | 0.0 | 84.3 → 81.7 (`-2.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_COST_PLUS1` | KB-05 (List Żelazny): cost 2 → 3 | 84.3 → 🟡 ** 81.7** (`-2.6`) | 0.0 | 84.3 → 81.7 (`-2.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_HERESY_PLUS1` | CAA-06 (Ucieczka z Lochów): heresy 0 → 1 | 84.3 → 🟡 ** 81.6** (`-2.7`) | 0.0 | 84.3 → 81.6 (`-2.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_HERESY_SET1` | CAA-06 (Ucieczka z Lochów): dodaj heresy = 1 | 84.3 → 🟡 ** 81.6** (`-2.7`) | 0.0 | 84.3 → 81.6 (`-2.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-11_COST_MINUS1` | KB-11 (Tajny Emisariusz): cost 1 → 0 | 84.3 → 🟡 ** 81.5** (`-2.8`) | 0.0 | 84.3 → 81.5 (`-2.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_COST_PLUS2` | CAA-10 (Echo Alhambry): cost 1 → 3 (+2) | 84.3 → 🟡 ** 81.5** (`-2.8`) | 0.0 | 84.3 → 81.5 (`-2.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_HERESY_PLUS1` | CAA-02 (Złoto z Kryjówki): heresy 0 → 1 | 84.3 → 🟡 ** 81.2** (`-3.1`) | 0.0 | 84.3 → 81.2 (`-3.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_HERESY_SET1` | CAA-02 (Złoto z Kryjówki): dodaj heresy = 1 | 84.3 → 🟡 ** 81.2** (`-3.1`) | 0.0 | 84.3 → 81.2 (`-3.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_COST_MINUS1` | KB-06 (Areszt Królewski): cost 2 → 1 | 84.3 → 🟡 ** 81.0** (`-3.3`) | 0.0 | 84.3 → 81.0 (`-3.3`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_COST_PLUS1` | KB-10 (Pieczęć Korony): cost 3 → 4 | 84.3 → 🟡 ** 81.0** (`-3.3`) | 0.0 | 84.3 → 81.0 (`-3.3`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_HERESY_PLUS1` | GC-06 (Szantaż): heresy 1 → 2 | 84.3 → 🟡 ** 80.7** (`-3.6`) | 0.0 | 84.3 → 80.7 (`-3.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_HERESY_SET2` | KB-05 (List Żelazny): dodaj heresy = 2 | 84.3 → 🟡 ** 80.6** (`-3.7`) | 0.0 | 84.3 → 80.6 (`-3.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_HERESY_MINUS1` | KT-07 (Archiwum Ukryte): heresy 1 → 0 | 84.3 → 🟡 ** 80.6** (`-3.7`) | 0.0 | 84.3 → 80.6 (`-3.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): heresy 0 → 1 | 84.3 → 🟡 ** 80.5** (`-3.8`) | 0.0 | 84.3 → 80.5 (`-3.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_HERESY_SET1` | SO-02 (Skarbiec Trybunału): dodaj heresy = 1 | 84.3 → 🟡 ** 80.5** (`-3.8`) | 0.0 | 84.3 → 80.5 (`-3.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_HERESY_SET2` | KB-06 (Areszt Królewski): dodaj heresy = 2 | 84.3 → 🟡 ** 80.3** (`-4.0`) | 0.0 | 84.3 → 80.3 (`-4.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_HERESY_PLUS1` | GC-04 (Informator): heresy 1 → 2 | 84.3 → 🟡 ** 80.2** (`-4.1`) | 0.0 | 84.3 → 80.2 (`-4.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_COST_PLUS1` | KB-06 (Areszt Królewski): cost 2 → 3 | 84.3 → 🟡 ** 80.1** (`-4.2`) | 0.0 | 84.3 → 80.1 (`-4.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_HERESY_SET2` | KT-06 (Przesłuchanie Imienia): dodaj heresy = 2 | 84.3 → 🟡 ** 79.9** (`-4.4`) | 0.0 | 84.3 → 79.9 (`-4.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_HERESY_SET2` | KB-02 (Pobór Podatków): dodaj heresy = 2 | 84.3 → 🟡 ** 79.8** (`-4.5`) | 0.0 | 84.3 → 79.8 (`-4.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_HERESY_PLUS1` | KB-06 (Areszt Królewski): heresy 0 → 1 | 84.3 → 🟡 ** 79.8** (`-4.5`) | 0.0 | 84.3 → 79.8 (`-4.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_HERESY_SET1` | KB-06 (Areszt Królewski): dodaj heresy = 1 | 84.3 → 🟡 ** 79.8** (`-4.5`) | 0.0 | 84.3 → 79.8 (`-4.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_HERESY_PLUS1` | GC-07 (Skrytobójstwo): heresy 0 → 1 | 84.3 → 🟡 ** 79.7** (`-4.6`) | 0.0 | 84.3 → 79.7 (`-4.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_HERESY_SET1` | GC-07 (Skrytobójstwo): dodaj heresy = 1 | 84.3 → 🟡 ** 79.7** (`-4.6`) | 0.0 | 84.3 → 79.7 (`-4.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 84.3 → 🟡 ** 79.6** (`-4.7`) | 0.0 | 84.3 → 79.6 (`-4.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_HERESY_PLUS1` | GC-09 (Lista Dłużników): heresy 1 → 2 | 84.3 → 🟡 ** 79.4** (`-4.9`) | 0.0 | 84.3 → 79.4 (`-4.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_COST_PLUS1` | KB-04 (Faworyt Dworu): cost 2 → 3 | 84.3 → 🟡 ** 78.8** (`-5.5`) | 0.0 | 84.3 → 78.8 (`-5.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_HERESY_MINUS1` | GC-02 (Czarny Rynek): heresy 1 → 0 | 84.3 → 🟡 ** 78.6** (`-5.7`) | 0.0 | 84.3 → 78.6 (`-5.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_HERESY_SET2` | SO-02 (Skarbiec Trybunału): dodaj heresy = 2 | 84.3 → 🟡 ** 78.5** (`-5.8`) | 0.0 | 84.3 → 78.5 (`-5.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_COST_MINUS1` | KB-04 (Faworyt Dworu): cost 2 → 1 | 84.3 → 🟡 ** 78.4** (`-5.9`) | 0.0 | 84.3 → 78.4 (`-5.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_COST_PLUS1` | KB-09 (Dekret Królewski): cost 4 → 5 | 84.3 → 🟡 ** 78.1** (`-6.2`) | 0.0 | 84.3 → 78.1 (`-6.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_HERESY_MINUS1` | GC-04 (Informator): heresy 1 → 0 | 84.3 → 🟡 ** 78.0** (`-6.3`) | 0.0 | 84.3 → 78.0 (`-6.3`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_COST_MINUS1` | KB-05 (List Żelazny): cost 2 → 1 | 84.3 → 🟡 ** 78.0** (`-6.3`) | 0.0 | 84.3 → 78.0 (`-6.3`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_HERESY_SET2` | KT-03 (Zakazana Wiedza): dodaj heresy = 2 | 84.3 → 🟡 ** 77.9** (`-6.4`) | 0.0 | 84.3 → 77.9 (`-6.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_COST_MINUS1` | KB-08 (Przekupstwo Sędziego): cost 2 → 1 | 84.3 → 🟡 ** 77.8** (`-6.5`) | 0.0 | 84.3 → 77.8 (`-6.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_HERESY_MINUS1` | GC-09 (Lista Dłużników): heresy 1 → 0 | 84.3 → 🟡 ** 77.6** (`-6.7`) | 0.0 | 84.3 → 77.6 (`-6.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_HERESY_MINUS1` | GC-06 (Szantaż): heresy 1 → 0 | 84.3 → 🟡 ** 77.4** (`-6.9`) | 0.0 | 84.3 → 77.4 (`-6.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_COST_MINUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 1 | 84.3 → 🟡 ** 76.9** (`-7.4`) | 0.0 | 84.3 → 76.9 (`-7.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_HERESY_SET2` | KB-07 (Szantaż Pieczęcią): dodaj heresy = 2 | 84.3 → 🟡 ** 76.9** (`-7.4`) | 0.0 | 84.3 → 76.9 (`-7.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_COST_MINUS1` | KB-12 (Szantaż Salonowy): cost 1 → 0 | 84.3 → 🟡 ** 76.7** (`-7.6`) | 0.0 | 84.3 → 76.7 (`-7.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_HERESY_SET2` | KB-08 (Przekupstwo Sędziego): dodaj heresy = 2 | 84.3 → 🟡 ** 76.5** (`-7.8`) | 0.0 | 84.3 → 76.5 (`-7.8`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_COST_MINUS1` | KT-02 (Transmutacja Złota): cost 1 → 0 | 84.3 → 🟡 ** 76.4** (`-7.9`) | 0.0 | 84.3 → 76.4 (`-7.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_HERESY_PLUS1` | CAA-10 (Echo Alhambry): heresy 0 → 1 | 84.3 → 🟡 ** 76.3** (`-8.0`) | 0.0 | 84.3 → 76.3 (`-8.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_HERESY_SET1` | CAA-10 (Echo Alhambry): dodaj heresy = 1 | 84.3 → 🟡 ** 76.3** (`-8.0`) | 0.0 | 84.3 → 76.3 (`-8.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_HERESY_PLUS1` | CAA-09 (Kurier Relikwii): heresy 0 → 1 | 84.3 → 🟡 ** 76.2** (`-8.1`) | 0.0 | 84.3 → 76.2 (`-8.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_HERESY_SET1` | CAA-09 (Kurier Relikwii): dodaj heresy = 1 | 84.3 → 🟡 ** 76.2** (`-8.1`) | 0.0 | 84.3 → 76.2 (`-8.1`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_HERESY_SET2` | CAA-05 (Ukryty Kurier): dodaj heresy = 2 | 84.3 → 🟡 ** 76.1** (`-8.2`) | 0.0 | 84.3 → 76.1 (`-8.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_COST_MINUS1` | KB-10 (Pieczęć Korony): cost 3 → 2 | 84.3 → 🟡 ** 76.1** (`-8.2`) | 0.0 | 84.3 → 76.1 (`-8.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_HERESY_PLUS2` | CAA-05 (Ukryty Kurier): heresy 0 → 2 (+2) | 84.3 → 🟡 ** 76.1** (`-8.2`) | 0.0 | 84.3 → 76.1 (`-8.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_HERESY_PLUS1` | CAA-07 (Szantaż Bractwa): heresy 0 → 1 | 84.3 → 🟡 ** 75.8** (`-8.5`) | 0.0 | 84.3 → 75.8 (`-8.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_HERESY_SET1` | CAA-07 (Szantaż Bractwa): dodaj heresy = 1 | 84.3 → 🟡 ** 75.8** (`-8.5`) | 0.0 | 84.3 → 75.8 (`-8.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_HERESY_SET2` | GC-07 (Skrytobójstwo): dodaj heresy = 2 | 84.3 → 🟠 ** 74.9** (`-9.4`) | 0.0 | 84.3 → 74.9 (`-9.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_HERESY_SET2` | CAA-02 (Złoto z Kryjówki): dodaj heresy = 2 | 84.3 → 🟠 ** 74.7** (`-9.6`) | 0.0 | 84.3 → 74.7 (`-9.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-12_HERESY_SET2` | CAA-12 (Skrytka w Murach): dodaj heresy = 2 | 84.3 → 🟠 ** 74.3** (`-10.0`) | 0.0 | 84.3 → 74.3 (`-10.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_COST_MINUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 0 | 84.3 → 🟠 ** 73.6** (`-10.7`) | 0.0 | 84.3 → 73.6 (`-10.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-12_HERESY_SET2` | KB-12 (Szantaż Salonowy): dodaj heresy = 2 | 84.3 → 🟠 ** 73.3** (`-11.0`) | 0.0 | 84.3 → 73.3 (`-11.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_HERESY_SET2` | CAA-06 (Ucieczka z Lochów): dodaj heresy = 2 | 84.3 → 🟠 ** 72.7** (`-11.6`) | 0.0 | 84.3 → 72.7 (`-11.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_COST_PLUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 2 | 84.3 → 🟠 ** 71.7** (`-12.6`) | 0.0 | 84.3 → 71.7 (`-12.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_COST_MINUS1` | KB-02 (Pobór Podatków): cost 1 → 0 | 84.3 → 🟠 ** 71.1** (`-13.2`) | 0.0 | 84.3 → 71.1 (`-13.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_HERESY_MINUS1` | KB-04 (Faworyt Dworu): heresy 1 → 0 | 84.3 → 🟠 ** 70.7** (`-13.6`) | 0.0 | 84.3 → 70.7 (`-13.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_HERESY_MINUS1` | KB-10 (Pieczęć Korony): heresy 2 → 1 | 84.3 → 🟠 ** 70.6** (`-13.7`) | 0.0 | 84.3 → 70.6 (`-13.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_HERESY_PLUS1` | KT-05 (Wskazówka Cyklu): heresy 1 → 2 | 84.3 → 🟠 ** 69.8** (`-14.5`) | 0.0 | 84.3 → 69.8 (`-14.5`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 0 → 1 | 84.3 → 🟠 ** 67.7** (`-16.6`) | 0.0 | 84.3 → 67.7 (`-16.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_HERESY_PLUS1` | KB-09 (Dekret Królewski): heresy 1 → 2 | 84.3 → 🟠 ** 67.3** (`-17.0`) | 0.0 | 84.3 → 67.3 (`-17.0`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_COST_PLUS1` | KT-10 (Pieczęć Salomona): cost 2 → 3 | 84.3 → 🟠 ** 66.4** (`-17.9`) | 0.0 | 84.3 → 66.4 (`-17.9`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_HERESY_SET2` | CAA-07 (Szantaż Bractwa): dodaj heresy = 2 | 84.3 → 🟠 ** 65.9** (`-18.4`) | 0.0 | 84.3 → 65.9 (`-18.4`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_COST_MINUS1` | KB-09 (Dekret Królewski): cost 4 → 3 | 84.3 → 🟠 ** 65.6** (`-18.7`) | 0.0 | 84.3 → 65.6 (`-18.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_HERESY_MINUS1` | KT-10 (Pieczęć Salomona): heresy 2 → 1 | 84.3 → 🟠 ** 65.1** (`-19.2`) | 0.0 | 84.3 → 65.1 (`-19.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_HERESY_SET2` | CAA-10 (Echo Alhambry): dodaj heresy = 2 | 84.3 → 🟠 ** 64.6** (`-19.7`) | 0.0 | 84.3 → 64.6 (`-19.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_HERESY_PLUS2` | CAA-10 (Echo Alhambry): heresy 0 → 2 (+2) | 84.3 → 🟠 ** 64.6** (`-19.7`) | 0.0 | 84.3 → 64.6 (`-19.7`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_HERESY_SET2` | CAA-09 (Kurier Relikwii): dodaj heresy = 2 | 84.3 → 🟠 ** 64.1** (`-20.2`) | 0.0 | 84.3 → 64.1 (`-20.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_HERESY_MINUS1` | KT-05 (Wskazówka Cyklu): heresy 1 → 0 | 84.3 → 🟠 ** 63.0** (`-21.3`) | 0.0 | 84.3 → 63.0 (`-21.3`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_HERESY_MINUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 0 | 84.3 → 🟠 ** 60.1** (`-24.2`) | 0.0 | 84.3 → 60.1 (`-24.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_HERESY_MINUS1` | KB-09 (Dekret Królewski): heresy 1 → 0 | 84.3 → 🔴 ** 55.1** (`-29.2`) | 0.0 | 84.3 → 55.1 (`-29.2`) | 0.0 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_HERESY_PLUS1` | KB-10 (Pieczęć Korony): heresy 2 → 3 | 84.3 → 🔴 ** 45.7** (`-38.6`) | 0.0 | 84.3 → 45.7 (`-38.6`) | 0.0 | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (31)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-05_HERESY_PLUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.94 (0–22) | 15.88zł (2.2–47.0) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-05_HERESY_SET1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.94 (0–22) | 15.88zł (2.2–47.0) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-04_HERESY_PLUS1` | 5.94 Er (1–14) | 0.1% | 0.9% | 1.69 (0–4) | 3.93 (0–25) | 15.87zł (2.5–46.2) | 6.71 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-09_HERESY_PLUS1` | 5.99 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.95 (0–22) | 15.89zł (2.2–46.2) | 6.73 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-09_COST_PLUS1` | 5.99 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.93 (0–22) | 15.88zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-09_COST_MINUS1` | 5.98 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 3.97 (0–22) | 15.76zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-07_HERESY_SET2` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.92 (0–22) | 15.93zł (2.2–46.2) | 6.77 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-12_COST_PLUS1` | 5.96 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.90 (0–22) | 15.60zł (2.2–46.2) | 6.71 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-01_COST_PLUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.71 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-07_HERESY_PLUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.92 (0–23) | 15.87zł (2.2–46.2) | 6.75 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-07_HERESY_SET1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.92 (0–23) | 15.87zł (2.2–46.2) | 6.75 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-07_COST_PLUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.89 (0–22) | 15.85zł (2.2–46.2) | 6.71 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-01_COST_PLUS2` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.92 (0–22) | 15.81zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-02_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.71 (0–4) | 3.89 (0–22) | 15.75zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-10_COST_MINUS1` | 5.92 Er (1–14) | 0.1% | 1.0% | 1.68 (0–4) | 3.94 (0–22) | 15.56zł (2.2–46.2) | 6.73 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-03_HERESY_PLUS1` | 6.00 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 4.02 (0–22) | 15.98zł (2.2–46.2) | 6.71 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-03_HERESY_SET1` | 6.00 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 4.02 (0–22) | 15.98zł (2.2–46.2) | 6.71 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-07_HERESY_PLUS1` | 5.99 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 3.99 (0–21) | 16.09zł (2.2–46.2) | 6.73 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-07_HERESY_SET1` | 5.99 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 3.99 (0–21) | 16.09zł (2.2–46.2) | 6.73 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-10_COST_MINUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.92 (0–22) | 15.82zł (2.2–46.2) | 6.71 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_COST_PLUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.62zł (2.0–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-11_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-04_COST_MINUS1` | 5.97 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-08_HERESY_SET2` | 6.02 Er (1–14) | 0.1% | 0.9% | 1.71 (0–4) | 3.93 (0–21) | 16.19zł (2.2–46.8) | 6.68 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-09_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.90 (0–25) | 15.73zł (2.2–46.2) | 6.71 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_COST_PLUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.67zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.92 (0–22) | 15.67zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-01_COST_MINUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.83zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-08_HERESY_PLUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.92 (0–25) | 15.83zł (2.2–46.2) | 6.79 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-08_HERESY_SET1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.92 (0–25) | 15.83zł (2.2–46.2) | 6.79 (0.2–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 239 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_CAA-01_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_HERESY_SET1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_HERESY_SET2` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_HERESY_SET1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_HERESY_SET2` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_COST_MINUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_HERESY_SET1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_HERESY_SET2` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-11_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-11_COST_MINUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-11_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-11_HERESY_SET1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-11_HERESY_SET2` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-01_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-01_HERESY_MINUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-03_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-03_HERESY_SET1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-03_HERESY_SET2` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-05_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.74zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-05_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-05_HERESY_SET1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-05_HERESY_SET2` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-08_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-08_HERESY_MINUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-11_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-11_HERESY_MINUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-12_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.83zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-12_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-12_HERESY_MINUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-01_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-01_HERESY_MINUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-03_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-03_HERESY_MINUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-11_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-11_HERESY_SET1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-11_HERESY_SET2` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_MINUS1` | 5.98 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-01_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-01_HERESY_SET1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-01_HERESY_SET2` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-02_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-02_HERESY_SET1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-02_HERESY_SET2` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-04_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-04_HERESY_SET1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-04_HERESY_SET2` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-10_HERESY_PLUS1` | 6.00 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 4.17 (0–22) | 15.93zł (2.2–46.2) | 6.74 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-11_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-11_HERESY_SET1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-11_HERESY_SET2` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-12_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-12_HERESY_MINUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-01_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-01_COST_MINUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-01_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-01_HERESY_SET1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-01_HERESY_SET2` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-02_COST_MINUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.92 (0–22) | 15.96zł (2.2–46.5) | 6.71 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-03_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-03_COST_MINUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-03_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-03_HERESY_MINUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-04_HERESY_SET2` | 5.96 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.93 (0–25) | 15.87zł (2.2–46.2) | 6.83 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-05_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-05_HERESY_SET1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-05_HERESY_SET2` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-10_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-10_HERESY_MINUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-11_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-11_COST_MINUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-11_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-11_HERESY_MINUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-12_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-12_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-12_HERESY_SET1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-12_HERESY_SET2` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_COST_PLUS2` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_HERESY_PLUS2` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-01_HERESY_PLUS2` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_COST_MINUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 16.02zł (2.5–46.5) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-03_COST_PLUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-08_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 3.99 (0–22) | 16.08zł (2.2–46.2) | 6.73 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-08_HERESY_SET1` | 5.98 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 3.99 (0–22) | 16.08zł (2.2–46.2) | 6.73 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.83zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-06_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.72zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-08_HERESY_PLUS1` | 6.00 Er (1–14) | 0.1% | 0.9% | 1.71 (0–4) | 3.94 (0–21) | 16.09zł (2.2–46.8) | 6.69 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-08_HERESY_SET1` | 6.00 Er (1–14) | 0.1% | 0.9% | 1.71 (0–4) | 3.94 (0–21) | 16.09zł (2.2–46.8) | 6.69 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-04_COST_MINUS1` | 5.96 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.93 (0–26) | 15.87zł (2.2–49.0) | 6.71 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-05_COST_PLUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.70zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-07_COST_MINUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.92 (0–22) | 15.96zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-07_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.71zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-03_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.92 (0–22) | 15.72zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-04_COST_PLUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-11_COST_MINUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-12_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.83zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-04_HERESY_PLUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.92 (0–25) | 15.83zł (2.2–46.2) | 6.80 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-04_HERESY_SET1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.92 (0–25) | 15.83zł (2.2–46.2) | 6.80 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-06_HERESY_SET2` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.87 (0–25) | 15.94zł (2.2–46.2) | 6.83 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-04_COST_MINUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.93 (0–22) | 15.94zł (2.2–46.5) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-02_COST_PLUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.71 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-08_COST_PLUS1` | 5.96 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.91zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-05_COST_PLUS2` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.92 (0–22) | 15.65zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_COST_PLUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.65zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.71 (0–4) | 3.92 (0–22) | 15.69zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-03_COST_MINUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-09_COST_PLUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.70zł (2.2–46.2) | 6.71 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-01_COST_MINUS1` | 5.97 Er (1–14) | 0.1% | 0.4% | 1.70 (0–4) | 3.92 (0–30) | 15.81zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-03_COST_MINUS1` | 5.98 Er (1–14) | 0.1% | 0.3% | 1.70 (0–4) | 3.92 (0–30) | 15.83zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-11_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.92 (0–22) | 15.83zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-07_HERESY_PLUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.82zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-08_COST_MINUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.92 (0–22) | 15.93zł (2.2–46.5) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-06_COST_PLUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.86 (0–25) | 15.84zł (2.2–46.2) | 6.71 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-09_HERESY_PLUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–30) | 15.83zł (2.2–46.2) | 6.83 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-09_HERESY_SET1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–30) | 15.83zł (2.2–46.2) | 6.83 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-07_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.1% | 1.70 (0–4) | 3.91 (0–22) | 15.75zł (2.0–46.2) | 6.71 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-10_COST_PLUS1` | 5.96 Er (1–14) | 0.1% | 1.0% | 1.69 (0–4) | 3.88 (0–22) | 15.77zł (2.2–48.2) | 6.70 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_COST_PLUS2` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.71 (0–4) | 3.92 (0–22) | 15.51zł (2.0–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-01_COST_PLUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.90 (0–22) | 15.80zł (2.2–46.2) | 6.71 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-08_COST_PLUS1` | 6.00 Er (1–14) | 0.1% | 1.0% | 1.71 (0–4) | 3.88 (0–22) | 15.85zł (2.2–46.8) | 6.68 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-04_COST_PLUS1` | 5.96 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 16.02zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-06_HERESY_PLUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.89 (0–25) | 15.88zł (2.2–46.2) | 6.79 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-06_HERESY_SET1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.89 (0–25) | 15.88zł (2.2–46.2) | 6.79 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-09_COST_MINUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.92 (0–22) | 15.94zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-08_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.1% | 1.70 (0–4) | 3.89 (0–19) | 15.75zł (2.2–46.2) | 6.70 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-06_COST_MINUS1` | 5.97 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 3.91 (0–22) | 15.94zł (2.5–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-07_COST_PLUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.90 (0–22) | 15.81zł (2.2–46.2) | 6.71 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-11_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.83zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-02_HERESY_PLUS1` | 5.95 Er (1–14) | 0.1% | 1.0% | 1.69 (0–4) | 3.96 (0–22) | 15.81zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-08_HERESY_SET2` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.93 (0–25) | 15.88zł (2.2–46.2) | 6.83 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_COST_PLUS1` | 5.99 Er (1–14) | 0.1% | 1.0% | 1.71 (0–4) | 3.92 (0–22) | 15.65zł (2.0–46.2) | 6.74 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-09_HERESY_SET2` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.92 (0–23) | 15.85zł (2.2–46.2) | 6.93 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-02_COST_MINUS1` | 5.96 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.93zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-06_COST_MINUS1` | 5.96 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.92 (0–22) | 15.88zł (2.5–46.2) | 6.73 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-03_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.92 (0–23) | 15.83zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-06_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 4.00 (0–22) | 15.89zł (2.2–46.2) | 6.69 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-06_HERESY_SET1` | 5.98 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 4.00 (0–22) | 15.89zł (2.2–46.2) | 6.69 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-06_COST_MINUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.93 (0–23) | 15.94zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_MINUS1` | 5.95 Er (1–14) | 0.1% | 1.0% | 1.69 (0–4) | 4.00 (0–22) | 15.73zł (2.2–46.2) | 6.76 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-10_COST_MINUS1` | 5.97 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 3.91 (0–22) | 15.92zł (2.5–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_HERESY_PLUS1` | 5.91 Er (1–14) | 0.1% | 1.0% | 1.68 (0–4) | 3.90 (0–22) | 15.60zł (2.2–46.8) | 6.82 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_HERESY_SET1` | 5.91 Er (1–14) | 0.1% | 1.0% | 1.68 (0–4) | 3.90 (0–22) | 15.60zł (2.2–46.8) | 6.82 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-09_COST_MINUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.94zł (2.5–46.5) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-12_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 4.00 (0–22) | 16.05zł (2.2–46.2) | 6.70 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-12_HERESY_SET1` | 5.98 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 4.00 (0–22) | 16.05zł (2.2–46.2) | 6.70 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-04_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.91 (0–22) | 15.73zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-10_COST_PLUS1` | 6.04 Er (1–14) | 0.1% | 1.0% | 1.72 (0–4) | 3.84 (0–22) | 16.40zł (2.2–49.8) | 6.68 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-12_COST_PLUS1` | 5.99 Er (1–14) | 0.1% | 1.3% | 1.71 (0–4) | 3.91 (0–20) | 15.81zł (2.2–46.2) | 6.66 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_HERESY_PLUS1` | 5.91 Er (1–14) | 0.1% | 1.0% | 1.68 (0–4) | 3.89 (0–22) | 15.62zł (2.2–46.8) | 6.82 (0.5–10.0) | 🟢 W NORMIE |
| `L3_SO-12_COST_MINUS1` | 5.95 Er (1–14) | 0.1% | 1.0% | 1.69 (0–4) | 3.93 (0–22) | 15.57zł (2.2–46.2) | 6.73 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-06_COST_PLUS1` | 5.97 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.89 (0–22) | 15.72zł (2.2–46.2) | 6.71 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_HERESY_MINUS1` | 6.02 Er (1–14) | 0.1% | 1.0% | 1.71 (0–4) | 3.90 (0–22) | 15.97zł (2.2–46.2) | 6.58 (0.0–10.0) | 🟢 W NORMIE |
| `L3_GC-10_HERESY_MINUS1` | 5.94 Er (1–14) | 0.1% | 1.0% | 1.69 (0–4) | 3.86 (0–22) | 15.48zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-07_COST_MINUS1` | 5.95 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 3.90 (0–21) | 15.71zł (2.2–46.2) | 6.74 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-12_HERESY_PLUS1` | 5.90 Er (1–14) | 0.1% | 1.0% | 1.68 (0–4) | 3.92 (0–22) | 15.58zł (2.2–46.8) | 6.81 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-12_HERESY_SET1` | 5.90 Er (1–14) | 0.1% | 1.0% | 1.68 (0–4) | 3.92 (0–22) | 15.58zł (2.2–46.8) | 6.81 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-10_HERESY_PLUS1` | 6.04 Er (1–14) | 0.1% | 1.0% | 1.72 (0–4) | 3.84 (0–22) | 16.41zł (2.2–46.2) | 6.68 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-02_COST_PLUS1` | 5.99 Er (1–14) | 0.1% | 1.0% | 1.71 (0–4) | 3.84 (0–23) | 16.05zł (2.2–46.2) | 6.67 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-02_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 3.91 (0–22) | 15.92zł (2.2–46.2) | 6.70 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-02_HERESY_SET1` | 5.98 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 3.91 (0–22) | 15.92zł (2.2–46.2) | 6.70 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-05_COST_PLUS1` | 6.01 Er (1–14) | 0.1% | 1.3% | 1.72 (0–4) | 3.95 (0–26) | 15.85zł (2.2–46.0) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_HERESY_PLUS1` | 5.95 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.97 (0–26) | 15.75zł (2.2–47.0) | 6.82 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_HERESY_SET1` | 5.95 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.97 (0–26) | 15.75zł (2.2–47.0) | 6.82 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-11_COST_MINUS1` | 5.97 Er (1–14) | 0.1% | 0.5% | 1.70 (0–4) | 3.98 (0–21) | 15.66zł (2.2–46.2) | 6.75 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_COST_PLUS2` | 6.01 Er (1–14) | 0.1% | 1.0% | 1.72 (0–4) | 3.94 (0–22) | 15.55zł (2.0–46.2) | 6.76 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_HERESY_PLUS1` | 5.93 Er (1–14) | 0.1% | 1.0% | 1.69 (0–4) | 3.91 (0–22) | 15.61zł (2.2–46.8) | 6.81 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_HERESY_SET1` | 5.93 Er (1–14) | 0.1% | 1.0% | 1.69 (0–4) | 3.91 (0–22) | 15.61zł (2.2–46.8) | 6.81 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-06_COST_MINUS1` | 5.98 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.93 (0–19) | 15.80zł (2.2–46.5) | 6.74 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-10_COST_PLUS1` | 6.04 Er (1–14) | 0.1% | 1.0% | 1.73 (0–4) | 3.98 (0–22) | 15.96zł (2.2–46.2) | 6.73 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-06_HERESY_PLUS1` | 5.95 Er (1–14) | 0.1% | 1.0% | 1.69 (0–4) | 3.96 (0–22) | 15.88zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-05_HERESY_SET2` | 5.96 Er (1–14) | 0.1% | 0.9% | 1.69 (0–4) | 4.02 (0–25) | 16.07zł (2.2–47.5) | 6.71 (0.5–10.0) | 🟢 W NORMIE |
| `L3_KT-07_HERESY_MINUS1` | 5.96 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.88 (0–22) | 15.64zł (2.2–46.2) | 6.71 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-02_HERESY_PLUS1` | 6.00 Er (1–14) | 0.1% | 1.0% | 1.71 (0–4) | 3.93 (0–27) | 15.88zł (2.2–46.2) | 6.93 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-02_HERESY_SET1` | 6.00 Er (1–14) | 0.1% | 1.0% | 1.71 (0–4) | 3.93 (0–27) | 15.88zł (2.2–46.2) | 6.93 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-06_HERESY_SET2` | 5.98 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 3.93 (0–22) | 16.21zł (2.2–47.8) | 6.70 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-04_HERESY_PLUS1` | 5.94 Er (1–14) | 0.1% | 1.0% | 1.69 (0–4) | 3.94 (0–22) | 15.83zł (2.2–46.2) | 6.71 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-06_COST_PLUS1` | 5.98 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 3.91 (0–23) | 16.11zł (2.2–47.8) | 6.68 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-06_HERESY_SET2` | 6.02 Er (1–14) | 0.1% | 0.9% | 1.71 (0–4) | 4.10 (0–22) | 16.16zł (2.5–46.5) | 6.70 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-02_HERESY_SET2` | 5.99 Er (1–14) | 0.1% | 0.9% | 1.71 (0–4) | 3.92 (0–19) | 16.01zł (2.2–46.2) | 6.70 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-06_HERESY_PLUS1` | 5.98 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 3.92 (0–22) | 16.17zł (2.2–47.8) | 6.70 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-06_HERESY_SET1` | 5.98 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 3.92 (0–22) | 16.17zł (2.2–47.8) | 6.70 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-07_HERESY_PLUS1` | 5.93 Er (1–14) | 0.1% | 1.0% | 1.69 (0–4) | 3.96 (0–22) | 15.76zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-07_HERESY_SET1` | 5.93 Er (1–14) | 0.1% | 1.0% | 1.69 (0–4) | 3.96 (0–22) | 15.76zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-02_COST_PLUS1` | 6.05 Er (1–14) | 0.1% | 1.0% | 1.73 (0–4) | 3.88 (0–27) | 16.08zł (2.2–46.2) | 6.73 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-09_HERESY_PLUS1` | 5.94 Er (1–14) | 0.1% | 1.0% | 1.69 (0–4) | 4.00 (0–22) | 15.80zł (2.2–46.8) | 6.73 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-04_COST_PLUS1` | 5.88 Er (1–14) | 0.1% | 1.0% | 1.67 (0–4) | 3.81 (0–22) | 15.52zł (2.2–46.2) | 6.73 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-02_HERESY_MINUS1` | 5.99 Er (1–14) | 0.2% | 1.0% | 1.70 (0–4) | 3.81 (0–22) | 15.82zł (2.2–46.5) | 6.70 (0.2–10.0) | 🟢 W NORMIE |
| `L3_SO-02_HERESY_SET2` | 6.00 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.98 (0–27) | 15.84zł (2.2–46.2) | 7.06 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-04_COST_MINUS1` | 5.91 Er (1–14) | 0.1% | 0.9% | 1.67 (0–4) | 3.86 (0–17) | 15.67zł (2.5–46.2) | 6.69 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-09_COST_PLUS1` | 6.06 Er (1–14) | 0.2% | 0.8% | 1.73 (0–4) | 4.02 (0–25) | 16.13zł (2.2–46.2) | 6.78 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-04_HERESY_MINUS1` | 6.00 Er (1–14) | 0.1% | 1.0% | 1.71 (0–4) | 3.84 (0–22) | 15.87zł (2.2–46.2) | 6.69 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-05_COST_MINUS1` | 5.91 Er (1–14) | 0.1% | 0.8% | 1.67 (0–4) | 3.85 (0–20) | 15.71zł (2.2–46.5) | 6.71 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-03_HERESY_SET2` | 6.05 Er (1–14) | 0.1% | 0.9% | 1.71 (0–4) | 4.14 (0–22) | 16.19zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-08_COST_MINUS1` | 5.90 Er (1–14) | 0.1% | 0.9% | 1.67 (0–4) | 3.85 (0–29) | 15.67zł (2.2–46.2) | 6.75 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-09_HERESY_MINUS1` | 5.99 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.82 (0–22) | 15.83zł (2.2–46.8) | 6.69 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-06_HERESY_MINUS1` | 5.99 Er (1–14) | 0.1% | 1.0% | 1.70 (0–4) | 3.82 (0–22) | 15.80zł (2.2–46.2) | 6.70 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-07_COST_MINUS1` | 5.91 Er (1–14) | 0.1% | 0.9% | 1.68 (0–4) | 3.86 (0–26) | 15.69zł (2.5–46.5) | 6.75 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-07_HERESY_SET2` | 6.01 Er (1–14) | 0.1% | 0.8% | 1.72 (0–4) | 4.06 (0–29) | 16.34zł (2.2–47.0) | 6.74 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-12_COST_MINUS1` | 5.90 Er (1–14) | 0.1% | 1.0% | 1.67 (0–4) | 3.82 (0–24) | 15.66zł (2.2–46.5) | 6.68 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-08_HERESY_SET2` | 6.01 Er (1–14) | 0.1% | 0.8% | 1.71 (0–4) | 4.05 (0–20) | 16.33zł (2.2–46.2) | 6.74 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-02_COST_MINUS1` | 5.92 Er (1–14) | 0.1% | 1.0% | 1.68 (0–4) | 3.85 (0–21) | 15.68zł (2.2–46.5) | 6.73 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_PLUS1` | 5.85 Er (1–14) | 0.1% | 0.9% | 1.66 (0–4) | 3.93 (0–24) | 15.40zł (2.2–46.8) | 6.94 (0.8–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_SET1` | 5.85 Er (1–14) | 0.1% | 0.9% | 1.66 (0–4) | 3.93 (0–24) | 15.40zł (2.2–46.8) | 6.94 (0.8–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_HERESY_PLUS1` | 5.85 Er (1–14) | 0.1% | 1.0% | 1.67 (0–4) | 3.95 (0–18) | 15.43zł (2.2–46.2) | 6.90 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_HERESY_SET1` | 5.85 Er (1–14) | 0.1% | 1.0% | 1.67 (0–4) | 3.95 (0–18) | 15.43zł (2.2–46.2) | 6.90 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_HERESY_SET2` | 5.86 Er (1–14) | 0.1% | 1.0% | 1.67 (0–4) | 3.91 (0–22) | 15.46zł (2.2–46.2) | 6.90 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-10_COST_MINUS1` | 5.90 Er (1–14) | 0.1% | 0.9% | 1.67 (0–4) | 3.84 (0–22) | 15.64zł (2.2–46.2) | 6.70 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_HERESY_PLUS2` | 5.86 Er (1–14) | 0.1% | 1.0% | 1.67 (0–4) | 3.91 (0–22) | 15.46zł (2.2–46.2) | 6.90 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_HERESY_PLUS1` | 5.99 Er (1–14) | 0.1% | 0.9% | 1.71 (0–4) | 3.94 (0–22) | 15.93zł (2.2–46.2) | 6.76 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_HERESY_SET1` | 5.99 Er (1–14) | 0.1% | 0.9% | 1.71 (0–4) | 3.94 (0–22) | 15.93zł (2.2–46.2) | 6.76 (0.2–10.0) | 🟢 W NORMIE |
| `L3_GC-07_HERESY_SET2` | 5.91 Er (1–14) | 0.1% | 1.0% | 1.68 (0–4) | 4.00 (0–22) | 15.76zł (2.2–46.2) | 6.71 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_HERESY_SET2` | 5.90 Er (1–14) | 0.1% | 1.0% | 1.68 (0–4) | 3.92 (0–24) | 15.48zł (2.2–46.2) | 6.86 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-12_HERESY_SET2` | 5.87 Er (1–14) | 0.1% | 1.0% | 1.67 (0–4) | 3.92 (0–24) | 15.33zł (2.2–46.2) | 6.85 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-05_COST_MINUS1` | 5.91 Er (1–14) | 0.1% | 1.0% | 1.68 (0–4) | 3.85 (0–22) | 15.65zł (2.2–46.2) | 6.69 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-12_HERESY_SET2` | 5.98 Er (1–14) | 0.1% | 0.9% | 1.70 (0–4) | 4.06 (0–23) | 16.21zł (2.2–46.5) | 6.70 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_HERESY_SET2` | 5.98 Er (1–14) | 0.1% | 0.9% | 1.71 (0–4) | 3.95 (0–26) | 15.89zł (2.2–46.2) | 6.85 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-05_COST_PLUS1` | 6.10 Er (1–14) | 0.2% | 0.9% | 1.73 (0–4) | 4.06 (0–22) | 16.45zł (2.2–46.2) | 6.76 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-02_COST_MINUS1` | 5.85 Er (1–14) | 0.1% | 0.8% | 1.65 (0–4) | 3.83 (0–29) | 15.32zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-04_HERESY_MINUS1` | 5.96 Er (1–14) | 0.1% | 1.0% | 1.69 (0–4) | 3.84 (0–22) | 15.55zł (2.2–46.2) | 6.72 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-10_HERESY_MINUS1` | 5.92 Er (1–14) | 0.0% | 1.0% | 1.68 (0–4) | 3.81 (0–21) | 15.49zł (2.2–46.2) | 6.67 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-05_HERESY_PLUS1` | 6.10 Er (1–14) | 0.2% | 0.9% | 1.73 (0–4) | 4.07 (0–22) | 16.50zł (2.2–46.2) | 6.76 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_COST_PLUS1` | 6.04 Er (1–14) | 0.1% | 0.9% | 1.73 (0–4) | 3.99 (0–22) | 15.98zł (2.2–46.2) | 6.71 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-09_HERESY_PLUS1` | 6.05 Er (1–14) | 0.2% | 0.9% | 1.73 (0–4) | 4.14 (0–23) | 16.29zł (2.2–46.2) | 6.78 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-10_COST_PLUS1` | 5.88 Er (1–14) | 0.1% | 1.0% | 1.68 (0–4) | 3.76 (0–22) | 15.38zł (2.2–46.2) | 6.70 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_HERESY_SET2` | 6.03 Er (1–14) | 0.1% | 0.9% | 1.73 (0–4) | 4.00 (0–22) | 16.10zł (2.2–46.2) | 6.76 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-09_COST_MINUS1` | 5.83 Er (1–14) | 0.1% | 1.5% | 1.64 (0–4) | 3.77 (0–20) | 15.32zł (2.2–46.2) | 6.66 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-10_HERESY_MINUS1` | 5.90 Er (1–14) | 0.1% | 1.0% | 1.68 (0–4) | 3.61 (0–22) | 15.42zł (2.2–46.2) | 6.66 (0.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_SET2` | 5.76 Er (1–14) | 0.1% | 0.9% | 1.64 (0–4) | 4.05 (0–23) | 15.10zł (2.2–46.8) | 7.10 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_PLUS2` | 5.76 Er (1–14) | 0.1% | 0.9% | 1.64 (0–4) | 4.05 (0–23) | 15.10zł (2.2–46.8) | 7.10 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_HERESY_SET2` | 5.77 Er (1–14) | 0.1% | 0.9% | 1.64 (0–4) | 4.06 (0–22) | 15.22zł (2.2–47.8) | 7.01 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-05_HERESY_MINUS1` | 5.87 Er (1–14) | 0.1% | 1.0% | 1.68 (0–4) | 3.71 (0–22) | 15.34zł (2.2–46.2) | 6.69 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KT-09_HERESY_MINUS1` | 5.87 Er (1–14) | 0.1% | 1.0% | 1.68 (0–4) | 3.72 (0–22) | 15.35zł (2.2–46.2) | 6.67 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-09_HERESY_MINUS1` | 5.89 Er (1–14) | 0.1% | 1.1% | 1.67 (0–4) | 3.66 (0–17) | 15.23zł (2.5–46.2) | 6.60 (0.2–10.0) | 🟢 W NORMIE |
| `L3_KB-10_HERESY_PLUS1` | 6.18 Er (1–14) | 0.2% | 0.8% | 1.78 (0–4) | 4.26 (0–22) | 16.57zł (2.2–46.2) | 6.77 (0.2–10.0) | 🟢 W NORMIE |

</details>