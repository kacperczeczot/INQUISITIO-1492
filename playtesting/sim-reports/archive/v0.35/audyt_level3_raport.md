# Raport Precyzyjnego Audytu Poziomu 3 (Parametry Pojedynczych Kart) — Wersja Balansu: v0.35

**Wersja Balansu:** `v0.35` | **Data:** 2026-08-15 21:24 | **Przeanalizowano Wariantów Kart:** 158 | **Próba:** 3000 gier/setup | **Czas:** 3517.64s
**Filtry:** Parametry: `cost,heresy` | Frakcja: `all` | Karta: `Wszystkie`
**Wynik Bazy Poziomu 3 (Global):** `🟢 97.5 pkt` | 3p: `94.2 pkt` | 4p: `99.1 pkt` | 5p: `99.3 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

### 🌟 Warianty z Zyskiem (Dowolna kategoria > 0) — Posortowane wg Global Delta (40)

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | Baza (Bieżące parametry wszystkich kart) | 🟢 ** 97.5** | 94.2 | 99.1 | 99.3 | ⚪ OPTYMALNY |
| `L3_CAA-09_COST_MINUS1` | CAA-09 (Kurier Relikwii): cost 2 → 1 | 97.5 → 🟢 ** 97.6** (`⬆️ +0.1`) | 94.2 → 94.3 (`⬆️ +0.1`) | 99.1 → 99.2 (`⬆️ +0.1`) | 99.3 | ⚪ OPTYMALNY |
| `L3_KT-01_COST_MINUS1` | KT-01 (Rytuał Przejścia): cost 1 → 0 | 🟢 ** 97.5** | 94.2 → 93.7 (`-0.5`) | 99.1 → 99.2 (`⬆️ +0.1`) | 99.3 → 99.5 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L3_CAA-07_COST_MINUS1` | CAA-07 (Szantaż Bractwa): cost 2 → 1 | 🟢 ** 97.5** | 94.2 → 94.3 (`⬆️ +0.1`) | 99.1 → 99.2 (`⬆️ +0.1`) | 99.3 → 98.9 (`-0.4`) | ⚪ OPTYMALNY |
| `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 🟢 ** 97.5** | 94.2 → 94.0 (`-0.2`) | 99.1 → 99.2 (`⬆️ +0.1`) | 99.3 → 99.4 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 🟢 ** 97.5** | 94.2 → 94.0 (`-0.2`) | 99.1 → 99.2 (`⬆️ +0.1`) | 99.3 | ⚪ OPTYMALNY |
| `L3_GC-01_HERESY_MINUS1` | GC-01 (Przekupiony Strażnik): heresy 1 → 0 | 97.5 → 🟢 ** 97.4** (`-0.1`) | 94.2 → 94.8 (`⬆️ +0.6`) | 99.1 → 98.7 (`-0.4`) | 99.3 → 98.6 (`-0.7`) | ⚪ OPTYMALNY |
| `L3_KT-02_HERESY_PLUS1` | KT-02 (Transmutacja Złota): heresy 0 → 1 | 97.5 → 🟢 ** 97.4** (`-0.1`) | 94.2 → 93.7 (`-0.5`) | 99.1 → 99.3 (`⬆️ +0.2`) | 99.3 → 99.1 (`-0.2`) | ⚪ OPTYMALNY |
| `L3_SO-04_COST_MINUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 0 | 97.5 → 🟢 ** 97.4** (`-0.1`) | 94.2 → 94.4 (`⬆️ +0.2`) | 99.1 → 98.9 (`-0.2`) | 99.3 → 98.9 (`-0.4`) | ⚪ OPTYMALNY |
| `L3_KT-02_COST_MINUS1` | KT-02 (Transmutacja Złota): cost 1 → 0 | 97.5 → 🟢 ** 97.4** (`-0.1`) | 94.2 → 93.7 (`-0.5`) | 99.1 | 99.3 → 99.4 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_KB-07_HERESY_PLUS1` | KB-07 (Szantaż Pieczęcią): heresy 0 → 1 | 97.5 → 🟢 ** 97.3** (`-0.2`) | 94.2 → 93.3 (`-0.9`) | 99.1 → 98.8 (`-0.3`) | 99.3 → 99.7 (`⬆️ +0.4`) | ⚪ OPTYMALNY |
| `L3_KT-04_HERESY_PLUS1` | KT-04 (Zwierciadło Herezji): heresy 0 → 1 | 97.5 → 🟢 ** 97.3** (`-0.2`) | 94.2 → 93.3 (`-0.9`) | 99.1 → 99.2 (`⬆️ +0.1`) | 99.3 → 99.5 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L3_CAA-05_COST_MINUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 | 97.5 → 🟢 ** 97.3** (`-0.2`) | 94.2 → 93.9 (`-0.3`) | 99.1 → 99.2 (`⬆️ +0.1`) | 99.3 → 98.8 (`-0.5`) | ⚪ OPTYMALNY |
| `L3_CAA-06_COST_MINUS1` | CAA-06 (Ucieczka z Lochów): cost 2 → 1 | 97.5 → 🟢 ** 97.3** (`-0.2`) | 94.2 → 93.5 (`-0.7`) | 99.1 → 99.2 (`⬆️ +0.1`) | 99.3 | ⚪ OPTYMALNY |
| `L3_KT-05_COST_MINUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 0 | 97.5 → 🟢 ** 97.3** (`-0.2`) | 94.2 → 93.5 (`-0.7`) | 99.1 | 99.3 → 99.4 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_SO-01_COST_PLUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 2 | 97.5 → 🟢 ** 97.2** (`-0.3`) | 94.2 → 95.5 (`⬆️ +1.3`) | 99.1 → 97.4 (`-1.7`) | 99.3 → 98.8 (`-0.5`) | ⚪ OPTYMALNY |
| `L3_KT-10_COST_MINUS1` | KT-10 (Pieczęć Salomona): cost 1 → 0 | 97.5 → 🟢 ** 97.2** (`-0.3`) | 94.2 → 92.9 (`-1.3`) | 99.1 | 99.3 → 99.5 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L3_KT-01_HERESY_PLUS1` | KT-01 (Rytuał Przejścia): heresy 0 → 1 | 97.5 → 🟢 ** 97.2** (`-0.3`) | 94.2 → 93.2 (`-1.0`) | 99.1 → 99.2 (`⬆️ +0.1`) | 99.3 → 99.1 (`-0.2`) | ⚪ OPTYMALNY |
| `L3_KT-05_HERESY_PLUS1` | KT-05 (Wskazówka Cyklu): heresy 0 → 1 | 97.5 → 🟢 ** 97.2** (`-0.3`) | 94.2 → 93.5 (`-0.7`) | 99.1 → 99.2 (`⬆️ +0.1`) | 99.3 → 98.8 (`-0.5`) | ⚪ OPTYMALNY |
| `L3_KB-04_HERESY_PLUS1` | KB-04 (Faworyt Dworu): heresy 1 → 2 | 97.5 → 🟢 ** 97.1** (`-0.4`) | 94.2 → 92.8 (`-1.4`) | 99.1 → 99.2 (`⬆️ +0.1`) | 99.3 → 99.2 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_KT-05_COST_PLUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 2 | 97.5 → 🟢 ** 97.1** (`-0.4`) | 94.2 → 92.9 (`-1.3`) | 99.1 → 99.2 (`⬆️ +0.1`) | 99.3 → 99.1 (`-0.2`) | ⚪ OPTYMALNY |
| `L3_KT-08_COST_MINUS1` | KT-08 (Areszt Wiedzy): cost 2 → 1 | 97.5 → 🟢 ** 97.1** (`-0.4`) | 94.2 → 92.9 (`-1.3`) | 99.1 → 99.0 (`-0.1`) | 99.3 → 99.4 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_KT-07_HERESY_PLUS1` | KT-07 (Archiwum Ukryte): heresy 0 → 1 | 97.5 → 🟢 ** 97.0** (`-0.5`) | 94.2 → 92.7 (`-1.5`) | 99.1 → 99.4 (`⬆️ +0.3`) | 99.3 → 99.0 (`-0.3`) | ⚪ OPTYMALNY |
| `L3_SO-06_COST_PLUS1` | SO-06 (Areszt Trybunalski): cost 2 → 3 | 97.5 → 🟢 ** 97.0** (`-0.5`) | 94.2 → 92.6 (`-1.6`) | 99.1 → 99.4 (`⬆️ +0.3`) | 99.3 → 98.9 (`-0.4`) | ⚪ OPTYMALNY |
| `L3_KT-08_HERESY_PLUS1` | KT-08 (Areszt Wiedzy): heresy 0 → 1 | 97.5 → 🟢 ** 97.0** (`-0.5`) | 94.2 → 92.8 (`-1.4`) | 99.1 → 99.2 (`⬆️ +0.1`) | 99.3 → 99.1 (`-0.2`) | ⚪ OPTYMALNY |
| `L3_KT-09_HERESY_PLUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 2 | 97.5 → 🟢 ** 96.8** (`-0.7`) | 94.2 → 92.0 (`-2.2`) | 99.1 → 99.3 (`⬆️ +0.2`) | 99.3 → 99.1 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 0 → 1 | 97.5 → 🟢 ** 96.8** (`-0.7`) | 94.2 → 93.4 (`-0.8`) | 99.1 → 97.5 (`-1.6`) | 99.3 → 99.4 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_COST_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 2 | 97.5 → 🟢 ** 96.8** (`-0.7`) | 94.2 → 93.5 (`-0.7`) | 99.1 → 97.5 (`-1.6`) | 99.3 → 99.4 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_COST_PLUS1` | CAA-04 (Fałszywy Trop): cost 1 → 2 | 97.5 → 🟢 ** 96.3** (`-1.2`) | 94.2 → 93.3 (`-0.9`) | 99.1 → 96.0 (`-3.1`) | 99.3 → 99.5 (`⬆️ +0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_HERESY_PLUS1` | GC-07 (Skrytobójstwo): heresy 1 → 2 | 97.5 → 🟢 ** 96.3** (`-1.2`) | 94.2 → 90.5 (`-3.7`) | 99.1 → 99.2 (`⬆️ +0.1`) | 99.3 → 99.1 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_HERESY_PLUS1` | KT-03 (Zakazana Wiedza): heresy 1 → 2 | 97.5 → 🟢 ** 96.2** (`-1.3`) | 94.2 → 90.7 (`-3.5`) | 99.1 → 99.2 (`⬆️ +0.1`) | 99.3 → 98.8 (`-0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_HERESY_PLUS1` | GC-09 (Lista Dłużników): heresy 0 → 1 | 97.5 → 🟢 ** 96.0** (`-1.5`) | 94.2 → 89.7 (`-4.5`) | 99.1 → 99.2 (`⬆️ +0.1`) | 99.3 → 99.0 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_HERESY_PLUS1` | SO-08 (Nasłanie Inkwizytora): heresy 0 → 1 | 97.5 → 🟢 ** 95.9** (`-1.6`) | 94.2 → 89.8 (`-4.4`) | 99.1 → 98.6 (`-0.5`) | 99.3 → 99.4 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_HERESY_PLUS1` | KT-06 (Przesłuchanie Imienia): heresy 0 → 1 | 97.5 → 🟢 ** 95.8** (`-1.7`) | 94.2 → 89.3 (`-4.9`) | 99.1 → 99.3 (`⬆️ +0.2`) | 99.3 → 98.8 (`-0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_HERESY_MINUS1` | GC-04 (Informator): heresy 1 → 0 | 97.5 → 🟢 ** 95.7** (`-1.8`) | 94.2 → 94.8 (`⬆️ +0.6`) | 99.1 → 93.7 (`-5.4`) | 99.3 → 98.6 (`-0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_COST_PLUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 2 | 97.5 → 🟢 ** 95.6** (`-1.9`) | 94.2 → 91.4 (`-2.8`) | 99.1 → 95.9 (`-3.2`) | 99.3 → 99.6 (`⬆️ +0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_HERESY_PLUS1` | SO-04 (Publiczne Ostrzeżenie): heresy 0 → 1 | 97.5 → 🟢 ** 94.3** (`-3.2`) | 94.2 → 84.8 (`-9.4`) | 99.1 → 98.6 (`-0.5`) | 99.3 → 99.4 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_COST_PLUS1` | KB-04 (Faworyt Dworu): cost 2 → 3 | 97.5 → 🟢 ** 90.3** (`-7.2`) | 94.2 → 88.1 (`-6.1`) | 99.1 → 83.3 (`-15.8`) | 99.3 → 99.5 (`⬆️ +0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_COST_PLUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 3 | 97.5 → 🟡 ** 89.2** (`-8.3`) | 94.2 → 87.1 (`-7.1`) | 99.1 → 80.9 (`-18.2`) | 99.3 → 99.5 (`⬆️ +0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_COST_MINUS1` | KB-06 (Areszt Królewski): cost 1 → 0 | 97.5 → 🟡 ** 87.4** (`-10.1`) | 94.2 → 87.9 (`-6.3`) | 99.1 → 75.0 (`-24.1`) | 99.3 → 99.4 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |

<details>
<summary><b>🔻 Pokaż pozostałe 118 wariantów bez zysku (wszystkie delty ≤ 0)...</b></summary>

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_GC-05_COST_PLUS1` | GC-05 (Fałszywy Świadek): cost 0 → 1 | 🟢 ** 97.5** | 94.2 | 99.1 | 99.3 | ⚪ OPTYMALNY |
| `L3_GC-05_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): heresy 0 → 1 | 🟢 ** 97.5** | 94.2 | 99.1 | 99.3 | ⚪ OPTYMALNY |
| `L3_KB-08_HERESY_PLUS1` | KB-08 (Przekupstwo Sędziego): heresy 0 → 1 | 🟢 ** 97.5** | 94.2 → 94.0 (`-0.2`) | 99.1 | 99.3 | ⚪ OPTYMALNY |
| `L3_SO-05_COST_PLUS1` | SO-05 (Wezwanie do Trybunału): cost 0 → 1 | 🟢 ** 97.5** | 94.2 | 99.1 | 99.3 | ⚪ OPTYMALNY |
| `L3_SO-05_HERESY_PLUS1` | SO-05 (Wezwanie do Trybunału): heresy 0 → 1 | 🟢 ** 97.5** | 94.2 | 99.1 | 99.3 | ⚪ OPTYMALNY |
| `L3_SO-06_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): heresy 0 → 1 | 🟢 ** 97.5** | 94.2 → 94.0 (`-0.2`) | 99.1 | 99.3 | ⚪ OPTYMALNY |
| `L3_KT-03_COST_PLUS1` | KT-03 (Zakazana Wiedza): cost 0 → 1 | 97.5 → 🟢 ** 97.4** (`-0.1`) | 94.2 | 99.1 | 99.3 → 98.9 (`-0.4`) | ⚪ OPTYMALNY |
| `L3_CAA-02_COST_MINUS1` | CAA-02 (Złoto z Kryjówki): cost 1 → 0 | 97.5 → 🟢 ** 97.3** (`-0.2`) | 94.2 → 93.8 (`-0.4`) | 99.1 → 99.0 (`-0.1`) | 99.3 → 99.2 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_CAA-04_COST_MINUS1` | CAA-04 (Fałszywy Trop): cost 1 → 0 | 97.5 → 🟢 ** 97.3** (`-0.2`) | 94.2 → 94.0 (`-0.2`) | 99.1 → 99.0 (`-0.1`) | 99.3 → 99.0 (`-0.3`) | ⚪ OPTYMALNY |
| `L3_CAA-10_COST_PLUS1` | CAA-10 (Echo Alhambry): cost 0 → 1 | 97.5 → 🟢 ** 97.3** (`-0.2`) | 94.2 → 93.5 (`-0.7`) | 99.1 | 99.3 | ⚪ OPTYMALNY |
| `L3_KT-04_COST_PLUS1` | KT-04 (Zwierciadło Herezji): cost 0 → 1 | 97.5 → 🟢 ** 97.3** (`-0.2`) | 94.2 → 93.7 (`-0.5`) | 99.1 | 99.3 → 99.2 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_KT-09_COST_MINUS1` | KT-09 (Fragment Kodeksu): cost 1 → 0 | 97.5 → 🟢 ** 97.3** (`-0.2`) | 94.2 → 93.4 (`-0.8`) | 99.1 | 99.3 | ⚪ OPTYMALNY |
| `L3_SO-01_COST_MINUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 0 | 97.5 → 🟢 ** 97.3** (`-0.2`) | 94.2 → 93.4 (`-0.8`) | 99.1 | 99.3 | ⚪ OPTYMALNY |
| `L3_CAA-08_COST_MINUS1` | CAA-08 (Kaptur Nocy): cost 2 → 1 | 97.5 → 🟢 ** 97.2** (`-0.3`) | 94.2 → 93.2 (`-1.0`) | 99.1 | 99.3 → 99.2 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_GC-07_HERESY_MINUS1` | GC-07 (Skrytobójstwo): heresy 1 → 0 | 97.5 → 🟢 ** 97.2** (`-0.3`) | 94.2 → 93.9 (`-0.3`) | 99.1 → 99.0 (`-0.1`) | 99.3 → 98.8 (`-0.5`) | ⚪ OPTYMALNY |
| `L3_SO-07_HERESY_PLUS1` | SO-07 (Przesłuchanie Oficjum): heresy 0 → 1 | 97.5 → 🟢 ** 97.2** (`-0.3`) | 94.2 → 93.4 (`-0.8`) | 99.1 | 99.3 → 99.0 (`-0.3`) | ⚪ OPTYMALNY |
| `L3_CAA-08_COST_PLUS1` | CAA-08 (Kaptur Nocy): cost 2 → 3 | 97.5 → 🟢 ** 97.1** (`-0.4`) | 94.2 → 93.3 (`-0.9`) | 99.1 | 99.3 → 98.9 (`-0.4`) | ⚪ OPTYMALNY |
| `L3_GC-01_COST_PLUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 2 | 97.5 → 🟢 ** 97.1** (`-0.4`) | 94.2 → 93.1 (`-1.1`) | 99.1 → 98.8 (`-0.3`) | 99.3 | ⚪ OPTYMALNY |
| `L3_KB-03_HERESY_PLUS1` | KB-03 (Plotka Dworska): heresy 0 → 1 | 97.5 → 🟢 ** 97.1** (`-0.4`) | 94.2 → 93.0 (`-1.2`) | 99.1 → 99.0 (`-0.1`) | 99.3 → 99.2 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_KT-07_COST_MINUS1` | KT-07 (Archiwum Ukryte): cost 1 → 0 | 97.5 → 🟢 ** 97.1** (`-0.4`) | 94.2 → 93.3 (`-0.9`) | 99.1 → 99.0 (`-0.1`) | 99.3 → 99.0 (`-0.3`) | ⚪ OPTYMALNY |
| `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 1 → 2 | 97.5 → 🟢 ** 97.1** (`-0.4`) | 94.2 → 93.1 (`-1.1`) | 99.1 → 99.0 (`-0.1`) | 99.3 → 99.1 (`-0.2`) | ⚪ OPTYMALNY |
| `L3_SO-07_COST_MINUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 1 | 97.5 → 🟢 ** 97.1** (`-0.4`) | 94.2 → 93.4 (`-0.8`) | 99.1 → 98.9 (`-0.2`) | 99.3 → 99.1 (`-0.2`) | ⚪ OPTYMALNY |
| `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 1 → 2 | 97.5 → 🟢 ** 97.0** (`-0.5`) | 94.2 → 93.2 (`-1.0`) | 99.1 → 99.0 (`-0.1`) | 99.3 → 98.9 (`-0.4`) | ⚪ OPTYMALNY |
| `L3_GC-07_COST_PLUS1` | GC-07 (Skrytobójstwo): cost 2 → 3 | 97.5 → 🟢 ** 97.0** (`-0.5`) | 94.2 → 92.7 (`-1.5`) | 99.1 → 99.0 (`-0.1`) | 99.3 → 99.2 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_GC-07_COST_MINUS1` | GC-07 (Skrytobójstwo): cost 2 → 1 | 97.5 → 🟢 ** 97.0** (`-0.5`) | 94.2 → 92.9 (`-1.3`) | 99.1 → 98.9 (`-0.2`) | 99.3 | ⚪ OPTYMALNY |
| `L3_KB-05_HERESY_PLUS1` | KB-05 (List Żelazny): heresy 0 → 1 | 97.5 → 🟢 ** 97.0** (`-0.5`) | 94.2 → 92.9 (`-1.3`) | 99.1 → 99.0 (`-0.1`) | 99.3 → 99.2 (`-0.1`) | ⚪ OPTYMALNY |
| `L3_KB-08_COST_PLUS1` | KB-08 (Przekupstwo Sędziego): cost 3 → 4 | 97.5 → 🟢 ** 97.0** (`-0.5`) | 94.2 | 99.1 → 97.6 (`-1.5`) | 99.3 | ⚪ OPTYMALNY |
| `L3_KB-08_COST_MINUS1` | KB-08 (Przekupstwo Sędziego): cost 3 → 2 | 97.5 → 🟢 ** 97.0** (`-0.5`) | 94.2 → 93.5 (`-0.7`) | 99.1 → 98.9 (`-0.2`) | 99.3 → 98.7 (`-0.6`) | ⚪ OPTYMALNY |
| `L3_KT-07_COST_PLUS1` | KT-07 (Archiwum Ukryte): cost 1 → 2 | 97.5 → 🟢 ** 97.0** (`-0.5`) | 94.2 → 92.7 (`-1.5`) | 99.1 | 99.3 → 99.1 (`-0.2`) | ⚪ OPTYMALNY |
| `L3_GC-03_COST_MINUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 0 | 97.5 → 🟢 ** 96.9** (`-0.6`) | 94.2 → 92.9 (`-1.3`) | 99.1 → 98.7 (`-0.4`) | 99.3 → 99.0 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_HERESY_PLUS1` | KB-01 (Rozkaz Dworu): heresy 0 → 1 | 97.5 → 🟢 ** 96.9** (`-0.6`) | 94.2 → 92.5 (`-1.7`) | 99.1 → 99.0 (`-0.1`) | 99.3 | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_HERESY_PLUS1` | SO-03 (Podejrzenie): heresy 0 → 1 | 97.5 → 🟢 ** 96.9** (`-0.6`) | 94.2 → 92.7 (`-1.5`) | 99.1 | 99.3 → 99.0 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_COST_MINUS1` | SO-08 (Nasłanie Inkwizytora): cost 1 → 0 | 97.5 → 🟢 ** 96.9** (`-0.6`) | 94.2 → 92.9 (`-1.3`) | 99.1 → 98.8 (`-0.3`) | 99.3 → 99.0 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_COST_PLUS1` | KT-08 (Areszt Wiedzy): cost 2 → 3 | 97.5 → 🟢 ** 96.8** (`-0.7`) | 94.2 → 93.7 (`-0.5`) | 99.1 → 97.4 (`-1.7`) | 99.3 → 99.2 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_COST_PLUS1` | KT-10 (Pieczęć Salomona): cost 1 → 2 | 97.5 → 🟢 ** 96.8** (`-0.7`) | 94.2 → 94.0 (`-0.2`) | 99.1 → 97.5 (`-1.6`) | 99.3 → 98.9 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_COST_MINUS1` | SO-03 (Podejrzenie): cost 2 → 1 | 97.5 → 🟢 ** 96.8** (`-0.7`) | 94.2 → 92.7 (`-1.5`) | 99.1 → 98.9 (`-0.2`) | 99.3 → 98.8 (`-0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_COST_MINUS1` | SO-09 (Świadek Koronny): cost 2 → 1 | 97.5 → 🟢 ** 96.7** (`-0.8`) | 94.2 → 92.3 (`-1.9`) | 99.1 → 99.0 (`-0.1`) | 99.3 → 98.9 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_HERESY_PLUS1` | SO-09 (Świadek Koronny): heresy 0 → 1 | 97.5 → 🟢 ** 96.7** (`-0.8`) | 94.2 → 92.0 (`-2.2`) | 99.1 → 99.0 (`-0.1`) | 99.3 → 99.1 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_COST_PLUS1` | CAA-03 (Cień na Rynku): cost 0 → 1 | 97.5 → 🟢 ** 96.6** (`-0.9`) | 94.2 → 91.8 (`-2.4`) | 99.1 → 99.0 (`-0.1`) | 99.3 → 99.1 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_COST_MINUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 0 | 97.5 → 🟢 ** 96.6** (`-0.9`) | 94.2 → 93.9 (`-0.3`) | 99.1 → 96.8 (`-2.3`) | 99.3 → 99.2 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_COST_MINUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 1 | 97.5 → 🟢 ** 96.6** (`-0.9`) | 94.2 → 92.9 (`-1.3`) | 99.1 → 97.7 (`-1.4`) | 99.3 → 99.1 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_COST_MINUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 0 | 97.5 → 🟢 ** 96.6** (`-0.9`) | 94.2 → 92.6 (`-1.6`) | 99.1 → 99.0 (`-0.1`) | 99.3 → 98.3 (`-1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_COST_PLUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 3 | 97.5 → 🟢 ** 96.5** (`-1.0`) | 94.2 → 93.4 (`-0.8`) | 99.1 → 97.4 (`-1.7`) | 99.3 → 98.8 (`-0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_HERESY_PLUS1` | SO-01 (Patrol Familiariuszy): heresy 0 → 1 | 97.5 → 🟢 ** 96.5** (`-1.0`) | 94.2 → 91.2 (`-3.0`) | 99.1 → 98.9 (`-0.2`) | 99.3 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 2 → 3 | 97.5 → 🟢 ** 96.4** (`-1.1`) | 94.2 → 92.7 (`-1.5`) | 99.1 → 97.4 (`-1.7`) | 99.3 → 99.2 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): heresy 1 → 2 | 97.5 → 🟢 ** 96.4** (`-1.1`) | 94.2 → 90.9 (`-3.3`) | 99.1 | 99.3 → 99.2 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_HERESY_MINUS1` | KT-03 (Zakazana Wiedza): heresy 1 → 0 | 97.5 → 🟢 ** 96.4** (`-1.1`) | 94.2 → 92.7 (`-1.5`) | 99.1 → 97.6 (`-1.5`) | 99.3 → 99.0 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_HERESY_PLUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 2 | 97.5 → 🟢 ** 96.3** (`-1.2`) | 94.2 → 92.6 (`-1.6`) | 99.1 → 97.4 (`-1.7`) | 99.3 → 98.9 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_HERESY_MINUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 0 | 97.5 → 🟢 ** 96.3** (`-1.2`) | 94.2 → 92.1 (`-2.1`) | 99.1 → 97.7 (`-1.4`) | 99.3 → 99.0 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_HERESY_PLUS1` | GC-06 (Szantaż): heresy 0 → 1 | 97.5 → 🟢 ** 96.2** (`-1.3`) | 94.2 → 90.8 (`-3.4`) | 99.1 | 99.3 → 98.7 (`-0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 1 → 2 | 97.5 → 🟢 ** 96.2** (`-1.3`) | 94.2 → 91.3 (`-2.9`) | 99.1 → 98.7 (`-0.4`) | 99.3 → 98.5 (`-0.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_COST_MINUS1` | GC-09 (Lista Dłużników): cost 2 → 1 | 97.5 → 🟢 ** 96.2** (`-1.3`) | 94.2 → 92.1 (`-2.1`) | 99.1 → 97.5 (`-1.6`) | 99.3 → 98.9 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_COST_MINUS1` | SO-06 (Areszt Trybunalski): cost 2 → 1 | 97.5 → 🟢 ** 96.2** (`-1.3`) | 94.2 → 92.6 (`-1.6`) | 99.1 → 97.3 (`-1.8`) | 99.3 → 98.7 (`-0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_HERESY_PLUS1` | KB-06 (Areszt Królewski): heresy 0 → 1 | 97.5 → 🟢 ** 96.1** (`-1.4`) | 94.2 → 92.3 (`-1.9`) | 99.1 → 97.1 (`-2.0`) | 99.3 → 98.9 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_COST_PLUS1` | CAA-06 (Ucieczka z Lochów): cost 2 → 3 | 97.5 → 🟢 ** 96.0** (`-1.5`) | 94.2 → 93.1 (`-1.1`) | 99.1 → 95.8 (`-3.3`) | 99.3 → 99.2 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-03_COST_PLUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 2 | 97.5 → 🟢 ** 96.0** (`-1.5`) | 94.2 → 91.0 (`-3.2`) | 99.1 → 99.0 (`-0.1`) | 99.3 → 98.1 (`-1.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-03_HERESY_PLUS1` | GC-03 (Podrzucenie Księgi): heresy 0 → 1 | 97.5 → 🟢 ** 95.9** (`-1.6`) | 94.2 → 89.6 (`-4.6`) | 99.1 → 99.0 (`-0.1`) | 99.3 → 99.2 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): heresy 0 → 1 | 97.5 → 🟢 ** 95.9** (`-1.6`) | 94.2 → 90.2 (`-4.0`) | 99.1 → 98.8 (`-0.3`) | 99.3 → 98.8 (`-0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-07_COST_PLUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 3 | 97.5 → 🟢 ** 95.9** (`-1.6`) | 94.2 → 92.1 (`-2.1`) | 99.1 → 97.3 (`-1.8`) | 99.3 → 98.4 (`-0.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_COST_PLUS1` | SO-09 (Świadek Koronny): cost 2 → 3 | 97.5 → 🟢 ** 95.9** (`-1.6`) | 94.2 → 91.4 (`-2.8`) | 99.1 → 97.5 (`-1.6`) | 99.3 → 98.9 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_COST_PLUS1` | GC-10 (Upadek Domu): cost 4 → 5 | 97.5 → 🟢 ** 95.8** (`-1.7`) | 94.2 → 93.9 (`-0.3`) | 99.1 → 94.6 (`-4.5`) | 99.3 → 99.0 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_COST_PLUS1` | CAA-09 (Kurier Relikwii): cost 2 → 3 | 97.5 → 🟢 ** 95.6** (`-1.9`) | 94.2 → 92.2 (`-2.0`) | 99.1 → 95.8 (`-3.3`) | 99.3 → 98.7 (`-0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 0 → 1 | 97.5 → 🟢 ** 95.6** (`-1.9`) | 94.2 → 89.4 (`-4.8`) | 99.1 | 99.3 → 98.2 (`-1.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_HERESY_PLUS1` | GC-02 (Czarny Rynek): heresy 1 → 2 | 97.5 → 🟢 ** 95.5** (`-2.0`) | 94.2 → 89.2 (`-5.0`) | 99.1 → 98.9 (`-0.2`) | 99.3 → 98.5 (`-0.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_COST_MINUS1` | SO-10 (Oczyść Miasto): cost 4 → 3 | 97.5 → 🟢 ** 95.4** (`-2.1`) | 94.2 → 89.4 (`-4.8`) | 99.1 → 99.0 (`-0.1`) | 99.3 → 97.7 (`-1.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_COST_PLUS1` | GC-04 (Informator): cost 0 → 1 | 97.5 → 🟢 ** 95.3** (`-2.2`) | 94.2 → 89.5 (`-4.7`) | 99.1 → 97.4 (`-1.7`) | 99.3 → 98.9 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_HERESY_PLUS1` | CAA-06 (Ucieczka z Lochów): heresy 1 → 2 | 97.5 → 🟢 ** 95.2** (`-2.3`) | 94.2 → 91.0 (`-3.2`) | 99.1 → 95.2 (`-3.9`) | 99.3 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_COST_PLUS1` | GC-02 (Czarny Rynek): cost 1 → 2 | 97.5 → 🟢 ** 95.2** (`-2.3`) | 94.2 → 90.6 (`-3.6`) | 99.1 → 97.2 (`-1.9`) | 99.3 → 97.7 (`-1.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_HERESY_PLUS1` | CAA-07 (Szantaż Bractwa): heresy 0 → 1 | 97.5 → 🟢 ** 95.0** (`-2.5`) | 94.2 → 89.7 (`-4.5`) | 99.1 → 96.5 (`-2.6`) | 99.3 → 98.8 (`-0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_HERESY_PLUS1` | KT-10 (Pieczęć Salomona): heresy 0 → 1 | 97.5 → 🟢 ** 94.9** (`-2.6`) | 94.2 → 87.4 (`-6.8`) | 99.1 → 98.7 (`-0.4`) | 99.3 → 98.7 (`-0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_COST_PLUS1` | GC-09 (Lista Dłużników): cost 2 → 3 | 97.5 → 🟢 ** 94.8** (`-2.7`) | 94.2 → 88.4 (`-5.8`) | 99.1 → 97.3 (`-1.8`) | 99.3 → 98.7 (`-0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 97.5 → 🟢 ** 94.8** (`-2.7`) | 94.2 → 91.3 (`-2.9`) | 99.1 → 94.4 (`-4.7`) | 99.3 → 98.7 (`-0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_COST_PLUS1` | SO-08 (Nasłanie Inkwizytora): cost 1 → 2 | 97.5 → 🟢 ** 94.8** (`-2.7`) | 94.2 → 89.7 (`-4.5`) | 99.1 → 95.6 (`-3.5`) | 99.3 → 99.1 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_COST_PLUS1` | GC-06 (Szantaż): cost 2 → 3 | 97.5 → 🟢 ** 94.7** (`-2.8`) | 94.2 → 87.4 (`-6.8`) | 99.1 → 98.9 (`-0.2`) | 99.3 → 97.9 (`-1.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_COST_PLUS1` | SO-03 (Podejrzenie): cost 2 → 3 | 97.5 → 🟢 ** 94.7** (`-2.8`) | 94.2 → 88.9 (`-5.3`) | 99.1 → 97.0 (`-2.1`) | 99.3 → 98.3 (`-1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_COST_MINUS1` | GC-08 (Zatrute Złoto): cost 1 → 0 | 97.5 → 🟢 ** 94.6** (`-2.9`) | 94.2 → 93.4 (`-0.8`) | 99.1 → 91.5 (`-7.6`) | 99.3 → 99.0 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_HERESY_MINUS1` | GC-02 (Czarny Rynek): heresy 1 → 0 | 97.5 → 🟢 ** 94.5** (`-3.0`) | 94.2 → 93.9 (`-0.3`) | 99.1 → 98.3 (`-0.8`) | 99.3 → 91.2 (`-8.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_COST_MINUS1` | GC-02 (Czarny Rynek): cost 1 → 0 | 97.5 → 🟢 ** 94.2** (`-3.3`) | 94.2 → 93.2 (`-1.0`) | 99.1 → 96.8 (`-2.3`) | 99.3 → 92.5 (`-6.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_HERESY_PLUS1` | CAA-05 (Ukryty Kurier): heresy 0 → 1 | 97.5 → 🟢 ** 94.1** (`-3.4`) | 94.2 → 91.0 (`-3.2`) | 99.1 → 92.9 (`-6.2`) | 99.3 → 98.5 (`-0.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_COST_PLUS1` | KB-06 (Areszt Królewski): cost 1 → 2 | 97.5 → 🟢 ** 94.1** (`-3.4`) | 94.2 → 91.1 (`-3.1`) | 99.1 → 91.9 (`-7.2`) | 99.3 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_HERESY_PLUS1` | CAA-03 (Cień na Rynku): heresy 1 → 2 | 97.5 → 🟢 ** 93.7** (`-3.8`) | 94.2 → 89.6 (`-4.6`) | 99.1 → 92.6 (`-6.5`) | 99.3 → 98.9 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_HERESY_MINUS1` | KB-09 (Dekret Królewski): heresy 1 → 0 | 97.5 → 🟢 ** 93.6** (`-3.9`) | 94.2 → 89.3 (`-4.9`) | 99.1 → 92.2 (`-6.9`) | 99.3 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_HERESY_MINUS1` | GC-10 (Upadek Domu): heresy 2 → 1 | 97.5 → 🟢 ** 93.2** (`-4.3`) | 94.2 → 93.5 (`-0.7`) | 99.1 → 88.0 (`-11.1`) | 99.3 → 98.2 (`-1.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_HERESY_PLUS1` | CAA-04 (Fałszywy Trop): heresy 0 → 1 | 97.5 → 🟢 ** 93.0** (`-4.5`) | 94.2 → 91.5 (`-2.7`) | 99.1 → 95.1 (`-4.0`) | 99.3 → 92.3 (`-7.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_COST_PLUS1` | KB-01 (Rozkaz Dworu): cost 1 → 2 | 97.5 → 🟢 ** 93.0** (`-4.5`) | 94.2 → 90.8 (`-3.4`) | 99.1 → 89.0 (`-10.1`) | 99.3 → 99.2 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_HERESY_PLUS1` | SO-10 (Oczyść Miasto): heresy 2 → 3 | 97.5 → 🟢 ** 93.0** (`-4.5`) | 94.2 → 85.3 (`-8.9`) | 99.1 → 94.7 (`-4.4`) | 99.3 → 99.1 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-01_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 97.5 → 🟢 ** 92.8** (`-4.7`) | 94.2 → 90.3 (`-3.9`) | 99.1 → 96.4 (`-2.7`) | 99.3 → 91.6 (`-7.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_HERESY_PLUS1` | GC-04 (Informator): heresy 1 → 2 | 97.5 → 🟢 ** 92.7** (`-4.8`) | 94.2 → 88.3 (`-5.9`) | 99.1 → 98.8 (`-0.3`) | 99.3 → 90.9 (`-8.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_COST_MINUS1` | GC-06 (Szantaż): cost 2 → 1 | 97.5 → 🟢 ** 92.5** (`-5.0`) | 94.2 → 94.0 (`-0.2`) | 99.1 → 91.3 (`-7.8`) | 99.3 → 92.3 (`-7.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_COST_MINUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 1 | 97.5 → 🟢 ** 92.2** (`-5.3`) | 94.2 → 94.1 (`-0.1`) | 99.1 → 95.2 (`-3.9`) | 99.3 → 87.3 (`-12.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_HERESY_PLUS1` | CAA-02 (Złoto z Kryjówki): heresy 0 → 1 | 97.5 → 🟢 ** 91.0** (`-6.5`) | 94.2 → 90.8 (`-3.4`) | 99.1 → 94.8 (`-4.3`) | 99.3 → 87.5 (`-11.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_HERESY_MINUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 0 | 97.5 → 🟡 ** 89.4** (`-8.1`) | 94.2 → 82.2 (`-12.0`) | 99.1 → 94.9 (`-4.2`) | 99.3 → 91.0 (`-8.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_HERESY_PLUS1` | KB-02 (Pobór Podatków): heresy 0 → 1 | 97.5 → 🟡 ** 89.3** (`-8.2`) | 94.2 → 90.6 (`-3.6`) | 99.1 → 95.5 (`-3.6`) | 99.3 → 81.9 (`-17.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_HERESY_MINUS1` | CAA-06 (Ucieczka z Lochów): heresy 1 → 0 | 97.5 → 🟡 ** 89.0** (`-8.5`) | 94.2 → 80.6 (`-13.6`) | 99.1 → 95.0 (`-4.1`) | 99.3 → 91.5 (`-7.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_COST_MINUS1` | KB-04 (Faworyt Dworu): cost 2 → 1 | 97.5 → 🟡 ** 89.0** (`-8.5`) | 94.2 → 92.9 (`-1.3`) | 99.1 → 97.5 (`-1.6`) | 99.3 → 76.6 (`-22.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_COST_MINUS1` | KB-01 (Rozkaz Dworu): cost 1 → 0 | 97.5 → 🟡 ** 88.9** (`-8.6`) | 94.2 → 87.8 (`-6.4`) | 99.1 → 79.8 (`-19.3`) | 99.3 → 99.2 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_COST_MINUS1` | KB-03 (Plotka Dworska): cost 1 → 0 | 97.5 → 🟡 ** 88.4** (`-9.1`) | 94.2 → 89.4 (`-4.8`) | 99.1 → 76.9 (`-22.2`) | 99.3 → 99.0 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_COST_MINUS1` | GC-10 (Upadek Domu): cost 4 → 3 | 97.5 → 🟡 ** 87.8** (`-9.7`) | 94.2 → 93.4 (`-0.8`) | 99.1 → 96.8 (`-2.3`) | 99.3 → 73.1 (`-26.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_HERESY_MINUS1` | SO-10 (Oczyść Miasto): heresy 2 → 1 | 97.5 → 🟡 ** 87.7** (`-9.8`) | 94.2 → 85.2 (`-9.0`) | 99.1 → 79.0 (`-20.1`) | 99.3 → 98.9 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_COST_PLUS1` | KB-03 (Plotka Dworska): cost 1 → 2 | 97.5 → 🟡 ** 87.6** (`-9.9`) | 94.2 → 89.5 (`-4.7`) | 99.1 → 89.0 (`-10.1`) | 99.3 → 84.4 (`-14.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 97.5 → 🟡 ** 85.8** (`-11.7`) | 94.2 → 80.1 (`-14.1`) | 99.1 → 94.5 (`-4.6`) | 99.3 → 82.8 (`-16.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_COST_MINUS1` | KB-05 (List Żelazny): cost 2 → 1 | 97.5 → 🟡 ** 81.9** (`-15.6`) | 94.2 → 83.4 (`-10.8`) | 99.1 → 63.1 (`-36.0`) | 99.3 → 99.1 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_HERESY_MINUS1` | KB-04 (Faworyt Dworu): heresy 1 → 0 | 97.5 → 🟡 ** 81.5** (`-16.0`) | 94.2 → 89.2 (`-5.0`) | 99.1 → 93.1 (`-6.0`) | 99.3 → 62.1 (`-37.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_COST_PLUS1` | SO-10 (Oczyść Miasto): cost 4 → 5 | 97.5 → 🟡 ** 80.8** (`-16.7`) | 94.2 → 67.0 (`-27.2`) | 99.1 → 76.9 (`-22.2`) | 99.3 → 98.4 (`-0.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_HERESY_MINUS1` | KB-10 (Pieczęć Korony): heresy 2 → 1 | 97.5 → 🟡 ** 78.6** (`-18.9`) | 94.2 → 72.2 (`-22.0`) | 99.1 → 65.6 (`-33.5`) | 99.3 → 98.1 (`-1.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_HERESY_PLUS1` | GC-10 (Upadek Domu): heresy 2 → 3 | 97.5 → 🟡 ** 77.0** (`-20.5`) | 94.2 → 80.1 (`-14.1`) | 99.1 → 77.6 (`-21.5`) | 99.3 → 73.4 (`-25.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_HERESY_MINUS1` | CAA-10 (Echo Alhambry): heresy 1 → 0 | 97.5 → 🟠 ** 72.2** (`-25.3`) | 94.2 → 62.1 (`-32.1`) | 99.1 → 81.0 (`-18.1`) | 99.3 → 73.4 (`-25.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_HERESY_PLUS1` | CAA-09 (Kurier Relikwii): heresy 0 → 1 | 97.5 → 🟠 ** 69.5** (`-28.0`) | 94.2 → 74.3 (`-19.9`) | 99.1 → 65.0 (`-34.1`) | 99.3 → 69.3 (`-30.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_COST_MINUS1` | KB-02 (Pobór Podatków): cost 1 → 0 | 97.5 → 🟠 ** 66.5** (`-31.0`) | 94.2 → 78.0 (`-16.2`) | 99.1 → 55.1 (`-44.0`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_HERESY_PLUS1` | KB-10 (Pieczęć Korony): heresy 2 → 3 | 97.5 → 🟠 ** 65.1** (`-32.4`) | 94.2 → 73.2 (`-21.0`) | 99.1 → 72.2 (`-26.9`) | 99.3 → 50.0 (`-49.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_COST_PLUS1` | KB-05 (List Żelazny): cost 2 → 3 | 97.5 → 🟠 ** 60.6** (`-36.9`) | 94.2 → 87.8 (`-6.4`) | 99.1 → 92.7 (`-6.4`) | 99.3 → 1.4 (`-97.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_HERESY_PLUS1` | KB-09 (Dekret Królewski): heresy 1 → 2 | 97.5 → 🔴 ** 59.5** (`-38.0`) | 94.2 → 76.8 (`-17.4`) | 99.1 → 42.1 (`-57.0`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_HERESY_PLUS1` | CAA-10 (Echo Alhambry): heresy 1 → 2 | 97.5 → 🔴 ** 59.3** (`-38.2`) | 94.2 → 68.7 (`-25.5`) | 99.1 → 60.2 (`-38.9`) | 99.3 → 49.0 (`-50.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_COST_PLUS1` | KB-02 (Pobór Podatków): cost 1 → 2 | 97.5 → 🔴 ** 56.7** (`-40.8`) | 94.2 → 70.6 (`-23.6`) | 99.1 → 42.8 (`-56.3`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_COST_MINUS1` | KB-10 (Pieczęć Korony): cost 2 → 1 | 97.5 → 🔴 ** 46.0** (`-51.5`) | 94.2 → 62.3 (`-31.9`) | 99.1 → 24.1 (`-75.0`) | 99.3 → 51.7 (`-47.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_COST_PLUS1` | KB-10 (Pieczęć Korony): cost 2 → 3 | 97.5 → 🔴 ** 44.7** (`-52.8`) | 94.2 → 59.5 (`-34.7`) | 99.1 → 29.9 (`-69.2`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_COST_MINUS1` | KB-09 (Dekret Królewski): cost 3 → 2 | 97.5 → 🔴 ** 41.2** (`-56.3`) | 94.2 → 59.1 (`-35.1`) | 99.1 → 23.3 (`-75.8`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_COST_PLUS1` | KB-09 (Dekret Królewski): cost 3 → 4 | 97.5 → 🔴 ** 28.8** (`-68.7`) | 94.2 → 37.7 (`-56.5`) | 99.1 → 19.8 (`-79.3`) | 99.3 → 0.0 (`-99.3`) | 🔴 POGARSZA GLOBALNIE |

</details>

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

### 🌟 Telemetria Wariantów z Zyskiem (40)

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | 5.55 Er (1–10) | 1.3% | 26.2% | 1.04 (0–4) | 3.62 (0–18) | 1.21zł (0.0–5.0) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_COST_MINUS1` | 5.54 Er (1–10) | 1.2% | 26.0% | 1.04 (0–4) | 3.63 (0–19) | 1.37zł (0.0–5.3) | 6.36 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_MINUS1` | 5.55 Er (1–10) | 1.3% | 26.2% | 1.04 (0–4) | 3.62 (0–18) | 1.38zł (0.0–5.3) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_COST_MINUS1` | 5.54 Er (1–10) | 1.2% | 26.0% | 1.04 (0–4) | 3.63 (0–19) | 1.37zł (0.0–5.7) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_PLUS1` | 5.55 Er (1–10) | 1.3% | 26.3% | 1.04 (0–4) | 3.62 (0–18) | 1.06zł (0.0–4.7) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-02_COST_PLUS1` | 5.55 Er (1–10) | 1.3% | 26.4% | 1.04 (0–4) | 3.62 (0–18) | 1.05zł (0.0–4.7) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-01_HERESY_MINUS1` | 5.57 Er (1–10) | 1.3% | 26.3% | 1.05 (0–4) | 3.59 (0–18) | 1.22zł (0.0–5.0) | 6.25 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-02_HERESY_PLUS1` | 5.55 Er (1–10) | 1.5% | 26.2% | 1.04 (0–4) | 3.68 (0–20) | 1.21zł (0.0–5.0) | 6.48 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-04_COST_MINUS1` | 5.53 Er (1–10) | 1.2% | 25.1% | 1.07 (0–4) | 3.64 (0–18) | 1.22zł (0.0–5.0) | 6.38 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-02_COST_MINUS1` | 5.55 Er (1–10) | 1.3% | 26.2% | 1.04 (0–4) | 3.62 (0–18) | 1.39zł (0.0–5.3) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-07_HERESY_PLUS1` | 5.51 Er (1–10) | 1.1% | 26.1% | 1.03 (0–4) | 3.63 (0–22) | 1.21zł (0.0–5.0) | 6.38 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-04_HERESY_PLUS1` | 5.55 Er (1–10) | 1.5% | 26.2% | 1.04 (0–4) | 3.70 (0–20) | 1.22zł (0.0–5.0) | 6.49 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_COST_MINUS1` | 5.54 Er (1–10) | 1.3% | 26.1% | 1.04 (0–4) | 3.62 (0–18) | 1.38zł (0.0–5.3) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_COST_MINUS1` | 5.54 Er (1–10) | 1.3% | 26.0% | 1.04 (0–4) | 3.62 (0–18) | 1.36zł (0.0–5.3) | 6.36 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-05_COST_MINUS1` | 5.55 Er (1–10) | 1.3% | 26.2% | 1.04 (0–4) | 3.62 (0–18) | 1.40zł (0.0–5.7) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-01_COST_PLUS1` | 5.54 Er (1–10) | 1.2% | 26.8% | 1.04 (0–4) | 3.61 (0–18) | 1.21zł (0.0–5.0) | 6.36 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-10_COST_MINUS1` | 5.55 Er (1–10) | 1.3% | 26.2% | 1.04 (0–4) | 3.62 (0–18) | 1.40zł (0.0–5.7) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-01_HERESY_PLUS1` | 5.55 Er (1–10) | 1.5% | 26.2% | 1.04 (0–4) | 3.68 (0–20) | 1.21zł (0.0–5.3) | 6.48 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-05_HERESY_PLUS1` | 5.55 Er (1–10) | 1.4% | 26.2% | 1.04 (0–4) | 3.69 (0–18) | 1.22zł (0.0–5.0) | 6.48 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-04_HERESY_PLUS1` | 5.52 Er (1–10) | 1.1% | 26.1% | 1.04 (0–4) | 3.68 (0–18) | 1.21zł (0.0–5.0) | 6.39 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-05_COST_PLUS1` | 5.55 Er (1–10) | 1.3% | 26.3% | 1.04 (0–4) | 3.63 (0–18) | 1.04zł (0.0–4.3) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-08_COST_MINUS1` | 5.55 Er (1–10) | 1.3% | 26.2% | 1.04 (0–4) | 3.62 (0–18) | 1.39zł (0.0–5.3) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-07_HERESY_PLUS1` | 5.55 Er (1–10) | 1.5% | 26.2% | 1.04 (0–4) | 3.69 (0–20) | 1.21zł (0.0–5.3) | 6.49 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-06_COST_PLUS1` | 5.54 Er (1–10) | 1.2% | 26.2% | 1.06 (0–4) | 3.61 (0–18) | 1.22zł (0.0–5.0) | 6.37 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-08_HERESY_PLUS1` | 5.56 Er (1–10) | 1.5% | 26.2% | 1.04 (0–4) | 3.69 (0–21) | 1.21zł (0.0–5.3) | 6.49 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-09_HERESY_PLUS1` | 5.56 Er (1–10) | 1.6% | 26.3% | 1.04 (0–4) | 3.72 (0–20) | 1.22zł (0.0–5.0) | 6.49 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_COST_PLUS1` | 5.56 Er (1–10) | 1.2% | 26.5% | 1.04 (0–4) | 3.61 (0–18) | 1.08zł (0.0–4.3) | 6.34 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_COST_PLUS1` | 5.57 Er (1–10) | 1.3% | 26.6% | 1.04 (0–4) | 3.61 (0–20) | 1.09zł (0.0–4.7) | 6.34 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_COST_PLUS1` | 5.56 Er (1–10) | 1.2% | 26.5% | 1.04 (0–4) | 3.61 (0–18) | 1.09zł (0.0–4.7) | 6.34 (0.3–10.0) | 🟢 W NORMIE |
| `L3_GC-07_HERESY_PLUS1` | 5.55 Er (1–10) | 1.3% | 26.2% | 1.04 (0–4) | 3.66 (0–18) | 1.22zł (0.0–5.0) | 6.41 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-03_HERESY_PLUS1` | 5.57 Er (1–10) | 1.6% | 26.3% | 1.04 (0–4) | 3.73 (0–20) | 1.22zł (0.0–5.3) | 6.50 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-09_HERESY_PLUS1` | 5.54 Er (1–10) | 1.2% | 26.2% | 1.04 (0–4) | 3.70 (0–18) | 1.21zł (0.0–5.0) | 6.45 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-08_HERESY_PLUS1` | 5.45 Er (1–10) | 1.0% | 25.9% | 1.02 (0–4) | 3.67 (0–18) | 1.20zł (0.0–5.0) | 6.47 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-06_HERESY_PLUS1` | 5.57 Er (1–10) | 1.7% | 26.3% | 1.04 (0–4) | 3.72 (0–19) | 1.22zł (0.0–5.3) | 6.51 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-04_HERESY_MINUS1` | 5.57 Er (1–10) | 1.4% | 26.3% | 1.05 (0–4) | 3.52 (0–18) | 1.21zł (0.0–5.0) | 6.22 (0.6–10.0) | 🟢 W NORMIE |
| `L3_SO-04_COST_PLUS1` | 5.56 Er (1–10) | 1.3% | 27.0% | 1.02 (0–4) | 3.60 (0–18) | 1.21zł (0.0–5.0) | 6.34 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-04_HERESY_PLUS1` | 5.45 Er (1–10) | 0.9% | 25.9% | 1.03 (0–4) | 3.68 (0–18) | 1.20zł (0.0–5.0) | 6.47 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-04_COST_PLUS1` | 5.52 Er (1–10) | 1.1% | 26.5% | 1.04 (0–4) | 3.53 (0–18) | 1.21zł (0.0–5.0) | 6.33 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-07_COST_PLUS1` | 5.50 Er (1–10) | 1.0% | 26.4% | 1.03 (0–4) | 3.55 (0–18) | 1.21zł (0.0–5.0) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-06_COST_MINUS1` | 5.50 Er (1–10) | 0.9% | 25.6% | 1.03 (0–4) | 3.57 (0–19) | 1.22zł (0.0–5.0) | 6.37 (0.7–10.0) | 🟢 W NORMIE |

<details>
<summary><b>🔻 Pokaż telemetrię pozostałych 118 wariantów bez zysku...</b></summary>

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_GC-05_COST_PLUS1` | 5.55 Er (1–10) | 1.3% | 26.2% | 1.04 (0–4) | 3.62 (0–18) | 1.21zł (0.0–5.0) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-05_HERESY_PLUS1` | 5.55 Er (1–10) | 1.3% | 26.2% | 1.04 (0–4) | 3.62 (0–18) | 1.21zł (0.0–5.0) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-08_HERESY_PLUS1` | 5.55 Er (1–10) | 1.3% | 26.2% | 1.04 (0–4) | 3.62 (0–18) | 1.21zł (0.0–5.0) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-05_COST_PLUS1` | 5.55 Er (1–10) | 1.3% | 26.2% | 1.04 (0–4) | 3.62 (0–18) | 1.21zł (0.0–5.0) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-05_HERESY_PLUS1` | 5.55 Er (1–10) | 1.3% | 26.2% | 1.04 (0–4) | 3.62 (0–18) | 1.21zł (0.0–5.0) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-06_HERESY_PLUS1` | 5.54 Er (1–10) | 1.1% | 26.2% | 1.03 (0–4) | 3.63 (0–18) | 1.21zł (0.0–5.0) | 6.41 (0.8–10.0) | 🟢 W NORMIE |
| `L3_KT-03_COST_PLUS1` | 5.55 Er (1–10) | 1.3% | 26.2% | 1.04 (0–4) | 3.62 (0–18) | 1.01zł (0.0–4.3) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_COST_MINUS1` | 5.55 Er (1–10) | 1.3% | 26.1% | 1.04 (0–4) | 3.62 (0–18) | 1.38zł (0.0–5.7) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_COST_MINUS1` | 5.54 Er (1–10) | 1.3% | 26.1% | 1.04 (0–4) | 3.63 (0–18) | 1.37zł (0.0–5.3) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_COST_PLUS1` | 5.56 Er (1–10) | 1.3% | 26.5% | 1.04 (0–4) | 3.60 (0–19) | 1.04zł (0.0–4.7) | 6.34 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-04_COST_PLUS1` | 5.56 Er (1–10) | 1.3% | 26.3% | 1.04 (0–4) | 3.62 (0–18) | 1.04zł (0.0–4.7) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-09_COST_MINUS1` | 5.55 Er (1–10) | 1.3% | 26.2% | 1.04 (0–4) | 3.62 (0–18) | 1.41zł (0.0–5.7) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-01_COST_MINUS1` | 5.55 Er (1–10) | 1.2% | 25.2% | 1.06 (0–4) | 3.62 (0–18) | 1.21zł (0.0–5.0) | 6.37 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_COST_MINUS1` | 5.54 Er (1–10) | 1.2% | 26.0% | 1.04 (0–4) | 3.62 (0–18) | 1.35zł (0.0–5.3) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-07_HERESY_MINUS1` | 5.55 Er (1–10) | 1.2% | 26.3% | 1.04 (0–4) | 3.60 (0–18) | 1.21zł (0.0–5.0) | 6.28 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-07_HERESY_PLUS1` | 5.52 Er (1–10) | 1.1% | 26.1% | 1.04 (0–4) | 3.66 (0–18) | 1.21zł (0.0–5.0) | 6.44 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_COST_PLUS1` | 5.55 Er (1–10) | 1.3% | 26.4% | 1.04 (0–4) | 3.61 (0–18) | 1.12zł (0.0–4.7) | 6.34 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-01_COST_PLUS1` | 5.56 Er (1–10) | 1.2% | 26.9% | 1.04 (0–4) | 3.61 (0–19) | 1.17zł (0.0–4.7) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-03_HERESY_PLUS1` | 5.52 Er (1–10) | 1.2% | 26.1% | 1.04 (0–4) | 3.70 (0–20) | 1.21zł (0.0–5.0) | 6.42 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-07_COST_MINUS1` | 5.55 Er (1–10) | 1.3% | 26.2% | 1.04 (0–4) | 3.62 (0–18) | 1.40zł (0.0–5.3) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-09_COST_PLUS1` | 5.55 Er (1–10) | 1.3% | 26.3% | 1.04 (0–4) | 3.63 (0–18) | 1.03zł (0.0–4.3) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-07_COST_MINUS1` | 5.53 Er (1–10) | 1.2% | 25.2% | 1.06 (0–4) | 3.62 (0–18) | 1.18zł (0.0–5.0) | 6.37 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_COST_PLUS1` | 5.56 Er (1–10) | 1.2% | 26.6% | 1.04 (0–4) | 3.61 (0–18) | 1.09zł (0.0–4.3) | 6.33 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-07_COST_PLUS1` | 5.55 Er (1–10) | 1.3% | 26.4% | 1.04 (0–4) | 3.61 (0–19) | 1.18zł (0.0–4.7) | 6.34 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-07_COST_MINUS1` | 5.53 Er (1–10) | 1.1% | 25.8% | 1.03 (0–4) | 3.62 (0–19) | 1.20zł (0.0–4.7) | 6.39 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-05_HERESY_PLUS1` | 5.53 Er (1–10) | 1.2% | 26.2% | 1.04 (0–4) | 3.65 (0–19) | 1.21zł (0.0–5.0) | 6.40 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-08_COST_PLUS1` | 5.55 Er (1–10) | 1.2% | 26.2% | 1.04 (0–4) | 3.62 (0–19) | 1.21zł (0.0–5.0) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-08_COST_MINUS1` | 5.56 Er (1–10) | 1.4% | 26.2% | 1.04 (0–3) | 3.63 (0–19) | 1.21zł (0.0–5.0) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-07_COST_PLUS1` | 5.55 Er (1–10) | 1.3% | 26.3% | 1.04 (0–4) | 3.62 (0–18) | 1.04zł (0.0–4.7) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-03_COST_MINUS1` | 5.50 Er (1–10) | 1.0% | 25.6% | 1.03 (0–4) | 3.61 (0–18) | 1.22zł (0.0–5.0) | 6.39 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-01_HERESY_PLUS1` | 5.52 Er (1–10) | 1.1% | 26.1% | 1.04 (0–4) | 3.64 (0–21) | 1.21zł (0.0–5.0) | 6.40 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-03_HERESY_PLUS1` | 5.52 Er (1–10) | 1.1% | 26.1% | 1.03 (0–4) | 3.65 (0–18) | 1.21zł (0.0–5.0) | 6.43 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-08_COST_MINUS1` | 5.52 Er (1–10) | 1.1% | 25.1% | 1.07 (0–4) | 3.63 (0–18) | 1.22zł (0.0–5.0) | 6.38 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-08_COST_PLUS1` | 5.55 Er (1–10) | 1.3% | 26.3% | 1.04 (0–4) | 3.63 (0–18) | 1.05zł (0.0–4.7) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-10_COST_PLUS1` | 5.55 Er (1–10) | 1.3% | 26.2% | 1.04 (0–4) | 3.63 (0–18) | 1.04zł (0.0–4.3) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-03_COST_MINUS1` | 5.52 Er (1–10) | 1.2% | 25.2% | 1.04 (0–4) | 3.63 (0–18) | 1.18zł (0.0–5.0) | 6.39 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-09_COST_MINUS1` | 5.53 Er (1–10) | 1.2% | 25.2% | 1.06 (0–4) | 3.63 (0–18) | 1.18zł (0.0–5.0) | 6.38 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-09_HERESY_PLUS1` | 5.51 Er (1–10) | 1.0% | 26.1% | 1.04 (0–4) | 3.66 (0–18) | 1.21zł (0.0–5.0) | 6.45 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_COST_PLUS1` | 5.56 Er (1–10) | 1.3% | 26.5% | 1.04 (0–4) | 3.61 (0–18) | 1.06zł (0.0–4.3) | 6.34 (0.3–10.0) | 🟢 W NORMIE |
| `L3_GC-01_COST_MINUS1` | 5.52 Er (1–10) | 1.1% | 25.7% | 1.04 (0–4) | 3.63 (0–21) | 1.23zł (0.0–4.7) | 6.39 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-06_COST_MINUS1` | 5.55 Er (1–10) | 1.3% | 26.2% | 1.04 (0–4) | 3.62 (0–18) | 1.43zł (0.0–5.3) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-02_COST_MINUS1` | 5.53 Er (1–10) | 1.1% | 25.1% | 1.10 (0–4) | 3.62 (0–18) | 1.24zł (0.0–5.0) | 6.40 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-06_COST_PLUS1` | 5.55 Er (1–10) | 1.3% | 26.4% | 1.04 (0–4) | 3.63 (0–18) | 1.01zł (0.0–4.7) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-01_HERESY_PLUS1` | 5.49 Er (1–10) | 1.1% | 26.0% | 1.03 (0–4) | 3.65 (0–18) | 1.21zł (0.0–5.0) | 6.45 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_COST_PLUS1` | 5.56 Er (1–10) | 1.3% | 26.5% | 1.04 (0–4) | 3.61 (0–18) | 1.09zł (0.0–4.3) | 6.34 (0.3–10.0) | 🟢 W NORMIE |
| `L3_GC-01_HERESY_PLUS1` | 5.53 Er (1–10) | 1.2% | 26.1% | 1.04 (0–4) | 3.66 (0–18) | 1.21zł (0.0–5.0) | 6.43 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-03_HERESY_MINUS1` | 5.56 Er (1–10) | 1.1% | 26.3% | 1.04 (0–4) | 3.60 (0–19) | 1.22zł (0.0–5.7) | 6.20 (0.6–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_HERESY_PLUS1` | 5.53 Er (1–10) | 1.1% | 26.1% | 1.04 (0–4) | 3.63 (0–18) | 1.21zł (0.0–5.0) | 6.42 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KT-09_HERESY_MINUS1` | 5.56 Er (1–10) | 1.2% | 26.3% | 1.04 (0–4) | 3.61 (0–18) | 1.22zł (0.0–5.7) | 6.22 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-06_HERESY_PLUS1` | 5.53 Er (1–10) | 1.2% | 26.2% | 1.04 (0–4) | 3.67 (0–18) | 1.21zł (0.0–5.0) | 6.44 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_PLUS1` | 5.60 Er (1–10) | 1.3% | 27.3% | 1.05 (0–4) | 3.61 (0–21) | 1.16zł (0.0–5.0) | 6.29 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-09_COST_MINUS1` | 5.52 Er (1–10) | 1.1% | 26.0% | 1.04 (0–4) | 3.66 (0–20) | 1.20zł (0.0–5.0) | 6.43 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-06_COST_MINUS1` | 5.55 Er (1–10) | 1.2% | 25.3% | 1.05 (0–4) | 3.61 (0–18) | 1.18zł (0.0–5.0) | 6.36 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-06_HERESY_PLUS1` | 5.52 Er (1–10) | 1.2% | 26.1% | 1.04 (0–3) | 3.68 (0–18) | 1.21zł (0.0–5.0) | 6.42 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_COST_PLUS1` | 5.57 Er (1–10) | 1.3% | 26.5% | 1.04 (0–4) | 3.62 (0–19) | 1.10zł (0.0–4.7) | 6.34 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-03_COST_PLUS1` | 5.59 Er (1–10) | 1.3% | 26.9% | 1.05 (0–4) | 3.63 (0–18) | 1.16zł (0.0–5.0) | 6.32 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-03_HERESY_PLUS1` | 5.52 Er (1–10) | 1.2% | 26.1% | 1.04 (0–4) | 3.68 (0–18) | 1.21zł (0.0–5.0) | 6.44 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-02_HERESY_PLUS1` | 5.46 Er (1–10) | 1.0% | 25.9% | 1.04 (0–4) | 3.67 (0–18) | 1.21zł (0.0–5.0) | 6.46 (0.8–10.0) | 🟢 W NORMIE |
| `L3_SO-07_COST_PLUS1` | 5.55 Er (1–10) | 1.2% | 26.3% | 1.05 (0–4) | 3.61 (0–18) | 1.21zł (0.0–5.0) | 6.36 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-09_COST_PLUS1` | 5.55 Er (1–10) | 1.2% | 26.4% | 1.05 (0–4) | 3.60 (0–18) | 1.21zł (0.0–5.0) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-10_COST_PLUS1` | 5.61 Er (1–10) | 1.4% | 26.0% | 1.05 (0–4) | 3.49 (0–18) | 1.27zł (0.0–5.0) | 6.25 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_COST_PLUS1` | 5.56 Er (1–10) | 1.2% | 26.5% | 1.04 (0–4) | 3.61 (0–18) | 1.10zł (0.0–4.7) | 6.33 (0.3–10.0) | 🟢 W NORMIE |
| `L3_GC-08_HERESY_PLUS1` | 5.53 Er (1–10) | 1.2% | 26.2% | 1.04 (0–4) | 3.70 (0–19) | 1.21zł (0.0–5.0) | 6.44 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-02_HERESY_PLUS1` | 5.53 Er (1–10) | 1.2% | 26.2% | 1.04 (0–4) | 3.70 (0–19) | 1.21zł (0.0–5.0) | 6.44 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-10_COST_MINUS1` | 5.50 Er (1–10) | 1.0% | 25.1% | 1.15 (0–4) | 3.64 (0–18) | 1.23zł (0.0–5.0) | 6.43 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-04_COST_PLUS1` | 5.60 Er (1–10) | 1.3% | 27.2% | 1.05 (0–4) | 3.59 (0–18) | 1.14zł (0.0–5.3) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_HERESY_PLUS1` | 5.52 Er (1–10) | 1.1% | 26.1% | 1.04 (0–4) | 3.67 (0–18) | 1.21zł (0.0–5.0) | 6.44 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-02_COST_PLUS1` | 5.61 Er (1–10) | 1.4% | 27.8% | 1.05 (0–4) | 3.61 (0–18) | 1.16zł (0.0–4.7) | 6.26 (0.3–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_HERESY_PLUS1` | 5.51 Er (1–10) | 1.1% | 26.1% | 1.03 (0–4) | 3.69 (0–18) | 1.21zł (0.0–5.0) | 6.44 (0.8–10.0) | 🟢 W NORMIE |
| `L3_KT-10_HERESY_PLUS1` | 5.56 Er (1–10) | 1.7% | 26.2% | 1.04 (0–4) | 3.81 (0–19) | 1.22zł (0.0–5.0) | 6.60 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-09_COST_PLUS1` | 5.60 Er (1–10) | 1.5% | 27.0% | 1.05 (0–4) | 3.63 (0–21) | 1.19zł (0.0–5.0) | 6.31 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-02_COST_PLUS1` | 5.58 Er (1–10) | 1.3% | 28.2% | 1.02 (0–4) | 3.59 (0–18) | 1.21zł (0.0–5.0) | 6.32 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-08_COST_PLUS1` | 5.57 Er (1–10) | 1.4% | 27.0% | 1.03 (0–4) | 3.61 (0–18) | 1.21zł (0.0–5.0) | 6.34 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-06_COST_PLUS1` | 5.58 Er (1–10) | 1.5% | 26.7% | 1.04 (0–4) | 3.66 (0–18) | 1.17zł (0.0–4.7) | 6.36 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-03_COST_PLUS1` | 5.56 Er (1–10) | 1.2% | 26.2% | 1.06 (0–4) | 3.59 (0–18) | 1.22zł (0.0–5.0) | 6.33 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_MINUS1` | 5.49 Er (1–10) | 1.1% | 25.8% | 1.03 (0–4) | 3.60 (0–18) | 1.20zł (0.0–4.7) | 6.40 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-02_HERESY_MINUS1` | 5.58 Er (1–10) | 1.3% | 26.3% | 1.05 (0–4) | 3.53 (0–18) | 1.21zł (0.0–5.0) | 6.23 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-02_COST_MINUS1` | 5.49 Er (1–10) | 1.1% | 25.6% | 1.03 (0–4) | 3.62 (0–18) | 1.21zł (0.0–4.7) | 6.41 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_HERESY_PLUS1` | 5.50 Er (1–10) | 1.0% | 26.0% | 1.03 (0–4) | 3.68 (0–18) | 1.21zł (0.0–5.0) | 6.44 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-06_COST_PLUS1` | 5.53 Er (1–10) | 1.1% | 27.2% | 1.04 (0–3) | 3.61 (0–18) | 1.23zł (0.0–5.0) | 6.37 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_HERESY_PLUS1` | 5.51 Er (1–10) | 1.1% | 26.1% | 1.03 (0–4) | 3.70 (0–18) | 1.21zł (0.0–4.7) | 6.44 (0.8–10.0) | 🟢 W NORMIE |
| `L3_KB-09_HERESY_MINUS1` | 5.57 Er (1–10) | 1.2% | 26.3% | 1.05 (0–4) | 3.51 (0–18) | 1.21zł (0.0–5.0) | 6.22 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-10_HERESY_MINUS1` | 5.59 Er (1–10) | 1.3% | 26.4% | 1.05 (0–4) | 3.43 (0–18) | 1.21zł (0.0–5.3) | 6.21 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_HERESY_PLUS1` | 5.51 Er (1–10) | 1.1% | 26.1% | 1.03 (0–4) | 3.69 (0–18) | 1.21zł (0.0–5.0) | 6.44 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-01_COST_PLUS1` | 5.52 Er (1–10) | 1.1% | 27.3% | 1.04 (0–4) | 3.59 (0–19) | 1.23zł (0.0–5.0) | 6.38 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-10_HERESY_PLUS1` | 5.45 Er (1–10) | 1.1% | 25.9% | 1.03 (0–4) | 3.67 (0–18) | 1.20zł (0.0–5.0) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_HERESY_PLUS1` | 5.51 Er (1–10) | 1.1% | 26.1% | 1.03 (0–4) | 3.67 (0–19) | 1.21zł (0.0–4.7) | 6.43 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-04_HERESY_PLUS1` | 5.52 Er (1–10) | 1.2% | 26.1% | 1.03 (0–4) | 3.76 (0–20) | 1.21zł (0.0–5.0) | 6.45 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-06_COST_MINUS1` | 5.50 Er (1–10) | 1.1% | 25.8% | 1.03 (0–4) | 3.56 (0–20) | 1.20zł (0.0–5.0) | 6.38 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-07_COST_MINUS1` | 5.53 Er (1–10) | 1.3% | 25.8% | 1.04 (0–4) | 3.61 (0–19) | 1.20zł (0.0–5.0) | 6.39 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_HERESY_PLUS1` | 5.51 Er (1–10) | 1.1% | 26.1% | 1.03 (0–3) | 3.69 (0–18) | 1.21zł (0.0–4.7) | 6.44 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_HERESY_MINUS1` | 5.58 Er (1–10) | 1.5% | 26.3% | 1.05 (0–4) | 3.59 (0–22) | 1.22zł (0.0–5.0) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-02_HERESY_PLUS1` | 5.52 Er (1–10) | 1.2% | 26.3% | 1.04 (0–4) | 3.72 (0–18) | 1.21zł (0.0–5.0) | 6.41 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_HERESY_MINUS1` | 5.58 Er (1–10) | 1.4% | 26.3% | 1.05 (0–4) | 3.55 (0–22) | 1.22zł (0.0–5.0) | 6.23 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-04_COST_MINUS1` | 5.51 Er (1–10) | 1.3% | 25.7% | 1.04 (0–4) | 3.63 (0–19) | 1.20zł (0.0–5.0) | 6.39 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-01_COST_MINUS1` | 5.50 Er (1–10) | 0.9% | 25.7% | 1.04 (0–4) | 3.56 (0–20) | 1.22zł (0.0–5.0) | 6.36 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-03_COST_MINUS1` | 5.49 Er (1–10) | 1.0% | 25.6% | 1.03 (0–3) | 3.60 (0–20) | 1.22zł (0.0–5.0) | 6.38 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-10_COST_MINUS1` | 5.50 Er (1–10) | 1.0% | 25.8% | 1.03 (0–4) | 3.68 (0–18) | 1.15zł (0.0–4.7) | 6.44 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-10_HERESY_MINUS1` | 5.66 Er (1–10) | 1.5% | 26.6% | 1.06 (0–4) | 3.54 (0–18) | 1.22zł (0.0–5.0) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-03_COST_PLUS1` | 5.56 Er (1–10) | 1.1% | 27.4% | 1.04 (0–4) | 3.52 (0–18) | 1.23zł (0.0–5.0) | 6.28 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_HERESY_MINUS1` | 5.58 Er (1–10) | 1.5% | 26.4% | 1.04 (0–4) | 3.54 (0–22) | 1.22zł (0.0–5.0) | 6.21 (0.3–10.0) | 🟢 W NORMIE |
| `L3_KB-05_COST_MINUS1` | 5.47 Er (1–10) | 0.8% | 26.3% | 1.03 (0–4) | 3.56 (0–19) | 1.18zł (0.0–5.0) | 6.35 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-04_HERESY_MINUS1` | 5.61 Er (1–10) | 1.4% | 26.3% | 1.05 (0–4) | 3.60 (0–18) | 1.23zł (0.0–5.0) | 6.30 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-10_COST_PLUS1` | 5.67 Er (1–10) | 1.4% | 25.5% | 0.89 (0–4) | 3.49 (0–18) | 1.22zł (0.0–5.0) | 6.26 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-10_HERESY_MINUS1` | 5.62 Er (1–10) | 1.4% | 26.4% | 1.05 (0–4) | 3.34 (0–20) | 1.21zł (0.0–5.0) | 6.15 (0.7–10.0) | 🟢 W NORMIE |
| `L3_GC-10_HERESY_PLUS1` | 5.50 Er (1–10) | 1.1% | 26.0% | 1.03 (0–4) | 3.82 (0–21) | 1.21zł (0.0–5.0) | 6.41 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_MINUS1` | 5.60 Er (1–10) | 1.6% | 26.4% | 1.05 (0–4) | 3.45 (0–21) | 1.22zł (0.0–5.7) | 6.00 (0.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_HERESY_PLUS1` | 5.47 Er (1–10) | 1.0% | 25.9% | 1.02 (0–4) | 3.77 (0–20) | 1.20zł (0.0–5.0) | 6.50 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-02_COST_MINUS1` | 5.46 Er (1–10) | 0.8% | 25.8% | 1.03 (0–3) | 3.55 (0–18) | 1.21zł (0.0–5.0) | 6.36 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-10_HERESY_PLUS1` | 5.42 Er (1–10) | 1.2% | 25.8% | 1.02 (0–4) | 3.89 (0–19) | 1.21zł (0.0–5.0) | 6.42 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-05_COST_PLUS1` | 5.61 Er (1–10) | 1.7% | 27.2% | 1.05 (0–4) | 3.63 (0–18) | 1.22zł (0.0–5.3) | 6.36 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-09_HERESY_PLUS1` | 5.57 Er (1–10) | 1.4% | 26.2% | 1.04 (0–4) | 3.77 (0–18) | 1.22zł (0.0–5.0) | 6.43 (0.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_PLUS1` | 5.44 Er (1–10) | 0.9% | 25.8% | 1.02 (0–4) | 3.79 (0–20) | 1.20zł (0.0–5.0) | 6.49 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-02_COST_PLUS1` | 5.65 Er (1–10) | 1.6% | 28.8% | 1.06 (0–4) | 3.68 (0–18) | 1.24zł (0.0–5.0) | 6.33 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-10_COST_MINUS1` | 5.38 Er (1–10) | 0.5% | 26.0% | 1.01 (0–4) | 3.60 (0–18) | 1.16zł (0.0–5.0) | 6.42 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-10_COST_PLUS1` | 5.69 Er (1–10) | 1.8% | 27.7% | 1.06 (0–3) | 3.67 (0–18) | 1.25zł (0.0–5.3) | 6.32 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-09_COST_MINUS1` | 5.40 Er (1–10) | 0.5% | 25.7% | 1.02 (0–4) | 3.53 (0–18) | 1.15zł (0.0–5.0) | 6.36 (0.7–10.0) | 🟢 W NORMIE |
| `L3_KB-09_COST_PLUS1` | 5.72 Er (1–10) | 1.6% | 27.9% | 1.07 (0–4) | 3.84 (0–23) | 1.21zł (0.0–5.0) | 6.41 (0.7–10.0) | 🟢 W NORMIE |

</details>