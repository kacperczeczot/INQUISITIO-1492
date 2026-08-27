[Strona główna](../../../../../README.md) > [v0.15](README.md) > [audyt_level3_raport](audyt_level3_raport.md)

---

# Raport Precyzyjnego Audytu Poziomu 3 (Parametry Pojedynczych Kart) — Wersja Balansu: v0.15

**Wersja Balansu:** `v0.15` | **Data:** 2026-08-14 12:07 | **Przeanalizowano Wariantów Kart:** 161 | **Próba:** 500 gier/setup | **Czas:** 141.22s
**Filtry:** Parametry: `cost,heresy` | Frakcja: `all` | Karta: `Wszystkie`
**Wynik Bazy Poziomu 3 (Global):** `🟢 87.1 pkt` | 3p: `91.5 pkt` | 4p: `70.7 pkt` | 5p: `99.1 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | Baza (Bieżące parametry wszystkich kart) | 🟢 ** 87.1** | 91.5 | 70.7 | 99.1 | ⚪ OPTYMALNY |
| `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 1 → 2 | 87.1 → 🟢 ** 69.7** (`-17.4`) | 91.5 → 85.3 (`-6.2`) | 70.7 → 64.3 (`-6.4`) | 99.1 → 59.6 (`-39.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-01_COST_MINUS1` | CAA-01 (Przejście Podziemiami): cost 1 → 0 | 87.1 → 🟢 ** 82.3** (`-4.8`) | 91.5 → 91.2 (`-0.3`) | 70.7 → 79.0 (`⬆️ +8.3`) | 99.1 → 76.6 (`-22.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-01_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 87.1 → 🟢 ** 86.4** (`-0.7`) | 91.5 → 88.3 (`-3.2`) | 70.7 → 72.2 (`⬆️ +1.5`) | 99.1 → 98.8 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 1 → 2 | 87.1 → 🟢 ** 81.4** (`-5.7`) | 91.5 → 87.3 (`-4.2`) | 70.7 → 71.9 (`⬆️ +1.2`) | 99.1 → 85.1 (`-14.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_COST_MINUS1` | CAA-02 (Złoto z Kryjówki): cost 1 → 0 | 87.1 → 🟢 ** 85.5** (`-1.6`) | 91.5 → 90.4 (`-1.1`) | 70.7 → 78.9 (`⬆️ +8.2`) | 99.1 → 87.2 (`-11.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_HERESY_PLUS1` | CAA-02 (Złoto z Kryjówki): heresy 0 → 1 | 87.1 → 🟢 ** 86.4** (`-0.7`) | 91.5 → 88.2 (`-3.3`) | 70.7 → 72.4 (`⬆️ +1.7`) | 99.1 → 98.7 (`-0.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_COST_PLUS1` | CAA-03 (Cień na Rynku): cost 1 → 2 | 87.1 → 🟢 ** 82.8** (`-4.3`) | 91.5 → 86.1 (`-5.4`) | 70.7 → 64.8 (`-5.9`) | 99.1 → 97.4 (`-1.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_COST_MINUS1` | CAA-03 (Cień na Rynku): cost 1 → 0 | 87.1 → 🟢 ** 78.7** (`-8.4`) | 91.5 → 87.9 (`-3.6`) | 70.7 → 77.7 (`⬆️ +7.0`) | 99.1 → 70.5 (`-28.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_HERESY_PLUS1` | CAA-03 (Cień na Rynku): heresy 1 → 2 | 87.1 → 🟢 ** 87.9** (`⬆️ +0.8`) | 91.5 → 90.4 (`-1.1`) | 70.7 → 74.7 (`⬆️ +4.0`) | 99.1 → 98.5 (`-0.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 87.1 → 🟢 ** 85.6** (`-1.5`) | 91.5 → 85.8 (`-5.7`) | 70.7 → 72.3 (`⬆️ +1.6`) | 99.1 → 98.8 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_COST_PLUS1` | CAA-04 (Fałszywy Trop): cost 1 → 2 | 87.1 → 🟢 ** 87.3** (`⬆️ +0.2`) | 91.5 → 91.4 (`-0.1`) | 70.7 → 72.4 (`⬆️ +1.7`) | 99.1 → 98.2 (`-0.9`) | ⚪ OPTYMALNY |
| `L3_CAA-04_COST_MINUS1` | CAA-04 (Fałszywy Trop): cost 1 → 0 | 87.1 → 🟢 ** 78.7** (`-8.4`) | 91.5 → 83.1 (`-8.4`) | 70.7 → 70.1 (`-0.6`) | 99.1 → 83.0 (`-16.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_HERESY_PLUS1` | CAA-04 (Fałszywy Trop): heresy 0 → 1 | 87.1 → 🟢 ** 86.6** (`-0.5`) | 91.5 → 87.8 (`-3.7`) | 70.7 → 74.9 (`⬆️ +4.2`) | 99.1 → 97.1 (`-2.0`) | ⚪ OPTYMALNY |
| `L3_CAA-05_COST_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 2 | 87.1 → 🟢 ** 80.2** (`-6.9`) | 91.5 → 84.8 (`-6.7`) | 70.7 → 72.1 (`⬆️ +1.4`) | 99.1 → 83.6 (`-15.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_COST_MINUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 | 87.1 → 🟢 ** 87.4** (`⬆️ +0.3`) | 91.5 → 89.2 (`-2.3`) | 70.7 → 75.2 (`⬆️ +4.5`) | 99.1 → 97.7 (`-1.4`) | ⚪ OPTYMALNY |
| `L3_CAA-05_HERESY_PLUS1` | CAA-05 (Ukryty Kurier): heresy 0 → 1 | 87.1 → 🟢 ** 86.9** (`-0.2`) | 91.5 → 89.5 (`-2.0`) | 70.7 → 72.6 (`⬆️ +1.9`) | 99.1 → 98.7 (`-0.4`) | ⚪ OPTYMALNY |
| `L3_CAA-06_COST_PLUS1` | CAA-06 (Ucieczka z Lochów): cost 2 → 3 | 87.1 → 🟢 ** 65.9** (`-21.2`) | 91.5 → 90.2 (`-1.3`) | 70.7 → 51.0 (`-19.7`) | 99.1 → 56.5 (`-42.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_COST_MINUS1` | CAA-06 (Ucieczka z Lochów): cost 2 → 1 | 87.1 → 🟢 ** 76.4** (`-10.7`) | 91.5 → 83.8 (`-7.7`) | 70.7 → 73.8 (`⬆️ +3.1`) | 99.1 → 71.6 (`-27.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_HERESY_PLUS1` | CAA-06 (Ucieczka z Lochów): heresy 0 → 1 | 87.1 → 🟢 ** 86.6** (`-0.5`) | 91.5 → 90.5 (`-1.0`) | 70.7 → 70.3 (`-0.4`) | 99.1 | ⚪ OPTYMALNY |
| `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 2 → 3 | 🟢 ** 87.1** | 91.5 → 91.0 (`-0.5`) | 70.7 → 72.6 (`⬆️ +1.9`) | 99.1 → 97.6 (`-1.5`) | ⚪ OPTYMALNY |
| `L3_CAA-07_COST_MINUS1` | CAA-07 (Szantaż Bractwa): cost 2 → 1 | 87.1 → 🟢 ** 83.0** (`-4.1`) | 91.5 → 81.8 (`-9.7`) | 70.7 → 79.4 (`⬆️ +8.7`) | 99.1 → 87.7 (`-11.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_HERESY_PLUS1` | CAA-07 (Szantaż Bractwa): heresy 0 → 1 | 🟢 ** 87.1** | 91.5 → 90.5 (`-1.0`) | 70.7 → 71.8 (`⬆️ +1.1`) | 99.1 | ⚪ OPTYMALNY |
| `L3_CAA-08_COST_PLUS1` | CAA-08 (Kaptur Nocy): cost 1 → 2 | 87.1 → 🟢 ** 90.5** (`⬆️ +3.4`) | 91.5 → 90.4 (`-1.1`) | 70.7 → 84.2 (`⬆️ +13.5`) | 99.1 → 97.0 (`-2.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-08_COST_MINUS1` | CAA-08 (Kaptur Nocy): cost 1 → 0 | 87.1 → 🟢 ** 81.6** (`-5.5`) | 91.5 → 91.6 (`⬆️ +0.1`) | 70.7 → 66.5 (`-4.2`) | 99.1 → 86.8 (`-12.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_HERESY_PLUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 2 | 87.1 → 🟢 ** 88.2** (`⬆️ +1.1`) | 91.5 → 91.2 (`-0.3`) | 70.7 → 73.9 (`⬆️ +3.2`) | 99.1 → 99.4 (`⬆️ +0.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-08_HERESY_MINUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 0 | 87.1 → 🟢 ** 86.9** (`-0.2`) | 91.5 → 90.0 (`-1.5`) | 70.7 → 71.5 (`⬆️ +0.8`) | 99.1 → 99.2 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_CAA-09_COST_PLUS1` | CAA-09 (Kurier Relikwii): cost 2 → 3 | 87.1 → 🟢 ** 78.2** (`-8.9`) | 91.5 → 87.2 (`-4.3`) | 70.7 → 65.2 (`-5.5`) | 99.1 → 82.1 (`-17.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_COST_MINUS1` | CAA-09 (Kurier Relikwii): cost 2 → 1 | 87.1 → 🟢 ** 77.9** (`-9.2`) | 91.5 → 81.9 (`-9.6`) | 70.7 → 78.6 (`⬆️ +7.9`) | 99.1 → 73.2 (`-25.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_HERESY_PLUS1` | CAA-09 (Kurier Relikwii): heresy 0 → 1 | 87.1 → 🟢 ** 73.9** (`-13.2`) | 91.5 → 81.7 (`-9.8`) | 70.7 → 57.1 (`-13.6`) | 99.1 → 82.9 (`-16.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_COST_PLUS1` | CAA-10 (Echo Alhambry): cost 1 → 2 | 87.1 → 🟢 ** 55.8** (`-31.3`) | 91.5 → 61.2 (`-30.3`) | 70.7 → 47.5 (`-23.2`) | 99.1 → 58.8 (`-40.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_COST_MINUS1` | CAA-10 (Echo Alhambry): cost 1 → 0 | 87.1 → 🟢 ** 78.5** (`-8.6`) | 91.5 → 83.3 (`-8.2`) | 70.7 → 76.5 (`⬆️ +5.8`) | 99.1 → 75.8 (`-23.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_HERESY_PLUS1` | CAA-10 (Echo Alhambry): heresy 1 → 2 | 87.1 → 🟢 ** 58.0** (`-29.1`) | 91.5 → 72.3 (`-19.2`) | 70.7 → 48.6 (`-22.1`) | 99.1 → 53.0 (`-46.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_HERESY_MINUS1` | CAA-10 (Echo Alhambry): heresy 1 → 0 | 87.1 → 🟢 ** 72.9** (`-14.2`) | 91.5 → 79.4 (`-12.1`) | 70.7 → 71.7 (`⬆️ +1.0`) | 99.1 → 67.6 (`-31.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_COST_PLUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 2 | 87.1 → 🟢 ** 86.2** (`-0.9`) | 91.5 → 89.3 (`-2.2`) | 70.7 → 72.4 (`⬆️ +1.7`) | 99.1 → 97.0 (`-2.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_COST_MINUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 0 | 87.1 → 🟢 ** 80.9** (`-6.2`) | 91.5 → 85.9 (`-5.6`) | 70.7 → 60.3 (`-10.4`) | 99.1 → 96.4 (`-2.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): heresy 0 → 1 | 87.1 → 🟢 ** 86.9** (`-0.2`) | 91.5 → 90.2 (`-1.3`) | 70.7 → 73.1 (`⬆️ +2.4`) | 99.1 → 97.4 (`-1.7`) | ⚪ OPTYMALNY |
| `L3_GC-02_COST_PLUS1` | GC-02 (Czarny Rynek): cost 1 → 2 | 87.1 → 🟢 ** 89.8** (`⬆️ +2.7`) | 91.5 → 85.8 (`-5.7`) | 70.7 → 85.9 (`⬆️ +15.2`) | 99.1 → 97.8 (`-1.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-02_COST_MINUS1` | GC-02 (Czarny Rynek): cost 1 → 0 | 87.1 → 🟢 ** 75.5** (`-11.6`) | 91.5 → 88.3 (`-3.2`) | 70.7 → 40.6 (`-30.1`) | 99.1 → 97.6 (`-1.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_HERESY_PLUS1` | GC-02 (Czarny Rynek): heresy 0 → 1 | 87.1 → 🟢 ** 80.4** (`-6.7`) | 91.5 → 89.1 (`-2.4`) | 70.7 → 65.8 (`-4.9`) | 99.1 → 86.4 (`-12.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-03_COST_PLUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 2 | 87.1 → 🟢 ** 88.4** (`⬆️ +1.3`) | 91.5 → 88.8 (`-2.7`) | 70.7 → 78.5 (`⬆️ +7.8`) | 99.1 → 97.9 (`-1.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-03_COST_MINUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 0 | 87.1 → 🟢 ** 84.0** (`-3.1`) | 91.5 → 89.3 (`-2.2`) | 70.7 → 65.2 (`-5.5`) | 99.1 → 97.4 (`-1.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-03_HERESY_PLUS1` | GC-03 (Podrzucenie Księgi): heresy 0 → 1 | 87.1 → 🟢 ** 86.6** (`-0.5`) | 91.5 → 88.8 (`-2.7`) | 70.7 → 74.2 (`⬆️ +3.5`) | 99.1 → 96.8 (`-2.3`) | ⚪ OPTYMALNY |
| `L3_GC-04_COST_PLUS1` | GC-04 (Informator): cost 1 → 2 | 87.1 → 🟢 ** 89.1** (`⬆️ +2.0`) | 91.5 → 89.9 (`-1.6`) | 70.7 → 80.4 (`⬆️ +9.7`) | 99.1 → 97.0 (`-2.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-04_COST_MINUS1` | GC-04 (Informator): cost 1 → 0 | 87.1 → 🟢 ** 81.4** (`-5.7`) | 91.5 → 86.7 (`-4.8`) | 70.7 → 60.3 (`-10.4`) | 99.1 → 97.2 (`-1.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_HERESY_PLUS1` | GC-04 (Informator): heresy 1 → 2 | 87.1 → 🟢 ** 78.8** (`-8.3`) | 91.5 → 87.7 (`-3.8`) | 70.7 → 69.2 (`-1.5`) | 99.1 → 79.5 (`-19.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_HERESY_MINUS1` | GC-04 (Informator): heresy 1 → 0 | 87.1 → 🟢 ** 85.5** (`-1.6`) | 91.5 → 90.5 (`-1.0`) | 70.7 → 67.4 (`-3.3`) | 99.1 → 98.5 (`-0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-05_COST_PLUS1` | GC-05 (Fałszywy Świadek): cost 0 → 1 | 🟢 ** 87.1** | 91.5 | 70.7 | 99.1 | ⚪ OPTYMALNY |
| `L3_GC-05_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): heresy 0 → 1 | 🟢 ** 87.1** | 91.5 | 70.7 | 99.1 | ⚪ OPTYMALNY |
| `L3_GC-06_COST_PLUS1` | GC-06 (Szantaż): cost 2 → 3 | 87.1 → 🟢 ** 84.6** (`-2.5`) | 91.5 → 85.8 (`-5.7`) | 70.7 → 82.4 (`⬆️ +11.7`) | 99.1 → 85.7 (`-13.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_COST_MINUS1` | GC-06 (Szantaż): cost 2 → 1 | 87.1 → 🟢 ** 62.4** (`-24.7`) | 91.5 → 87.4 (`-4.1`) | 70.7 → 46.4 (`-24.3`) | 99.1 → 53.3 (`-45.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_HERESY_PLUS1` | GC-06 (Szantaż): heresy 0 → 1 | 87.1 → 🟢 ** 85.5** (`-1.6`) | 91.5 → 90.0 (`-1.5`) | 70.7 → 67.2 (`-3.5`) | 99.1 → 99.2 (`⬆️ +0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_COST_PLUS1` | GC-07 (Skrytobójstwo): cost 2 → 3 | 87.1 → 🟢 ** 80.1** (`-7.0`) | 91.5 → 91.4 (`-0.1`) | 70.7 → 51.9 (`-18.8`) | 99.1 → 97.0 (`-2.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_COST_MINUS1` | GC-07 (Skrytobójstwo): cost 2 → 1 | 87.1 → 🟢 ** 78.4** (`-8.7`) | 91.5 → 88.4 (`-3.1`) | 70.7 → 50.4 (`-20.3`) | 99.1 → 96.3 (`-2.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_HERESY_PLUS1` | GC-07 (Skrytobójstwo): heresy 1 → 2 | 87.1 → 🟢 ** 87.3** (`⬆️ +0.2`) | 91.5 → 90.5 (`-1.0`) | 70.7 → 72.6 (`⬆️ +1.9`) | 99.1 → 98.9 (`-0.2`) | ⚪ OPTYMALNY |
| `L3_GC-07_HERESY_MINUS1` | GC-07 (Skrytobójstwo): heresy 1 → 0 | 87.1 → 🟢 ** 87.5** (`⬆️ +0.4`) | 91.5 | 70.7 → 72.3 (`⬆️ +1.6`) | 99.1 → 98.7 (`-0.4`) | ⚪ OPTYMALNY |
| `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 1 → 2 | 87.1 → 🟢 ** 83.0** (`-4.1`) | 91.5 → 89.0 (`-2.5`) | 70.7 → 63.0 (`-7.7`) | 99.1 → 97.1 (`-2.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_COST_MINUS1` | GC-08 (Zatrute Złoto): cost 1 → 0 | 87.1 → 🟢 ** 64.8** (`-22.3`) | 91.5 → 90.2 (`-1.3`) | 70.7 → 48.2 (`-22.5`) | 99.1 → 56.1 (`-43.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 0 → 1 | 87.1 → 🟢 ** 82.2** (`-4.9`) | 91.5 → 88.8 (`-2.7`) | 70.7 → 70.5 (`-0.2`) | 99.1 → 87.4 (`-11.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_COST_PLUS1` | GC-09 (Lista Dłużników): cost 2 → 3 | 87.1 → 🟢 ** 87.3** (`⬆️ +0.2`) | 91.5 → 88.2 (`-3.3`) | 70.7 → 75.6 (`⬆️ +4.9`) | 99.1 → 98.0 (`-1.1`) | ⚪ OPTYMALNY |
| `L3_GC-09_COST_MINUS1` | GC-09 (Lista Dłużników): cost 2 → 1 | 87.1 → 🟢 ** 68.3** (`-18.8`) | 91.5 → 92.1 (`⬆️ +0.6`) | 70.7 → 49.9 (`-20.8`) | 99.1 → 63.0 (`-36.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_HERESY_PLUS1` | GC-09 (Lista Dłużników): heresy 0 → 1 | 87.1 → 🟢 ** 87.3** (`⬆️ +0.2`) | 91.5 → 87.8 (`-3.7`) | 70.7 → 76.7 (`⬆️ +6.0`) | 99.1 → 97.5 (`-1.6`) | ⚪ OPTYMALNY |
| `L3_GC-10_COST_PLUS1` | GC-10 (Upadek Domu): cost 3 → 4 | 87.1 → 🟢 ** 90.3** (`⬆️ +3.2`) | 91.5 → 88.2 (`-3.3`) | 70.7 → 86.4 (`⬆️ +15.7`) | 99.1 → 96.2 (`-2.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-10_COST_MINUS1` | GC-10 (Upadek Domu): cost 3 → 2 | 87.1 → 🟢 ** 80.3** (`-6.8`) | 91.5 → 89.8 (`-1.7`) | 70.7 → 65.0 (`-5.7`) | 99.1 → 86.1 (`-13.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_HERESY_PLUS1` | GC-10 (Upadek Domu): heresy 2 → 3 | 87.1 → 🟢 ** 62.5** (`-24.6`) | 91.5 → 72.7 (`-18.8`) | 70.7 → 52.2 (`-18.5`) | 99.1 → 0.0 (`-99.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_HERESY_MINUS1` | GC-10 (Upadek Domu): heresy 2 → 1 | 87.1 → 🟢 ** 77.1** (`-10.0`) | 91.5 → 85.7 (`-5.8`) | 70.7 → 48.5 (`-22.2`) | 99.1 → 97.1 (`-2.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_COST_PLUS1` | KB-01 (Rozkaz Dworu): cost 1 → 2 | 87.1 → 🟢 ** 85.9** (`-1.2`) | 91.5 → 81.1 (`-10.4`) | 70.7 → 78.6 (`⬆️ +7.9`) | 99.1 → 97.9 (`-1.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_COST_MINUS1` | KB-01 (Rozkaz Dworu): cost 1 → 0 | 87.1 → 🟢 ** 83.7** (`-3.4`) | 91.5 → 79.8 (`-11.7`) | 70.7 → 72.4 (`⬆️ +1.7`) | 99.1 → 98.8 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_HERESY_PLUS1` | KB-01 (Rozkaz Dworu): heresy 0 → 1 | 87.1 → 🟢 ** 83.2** (`-3.9`) | 91.5 → 88.9 (`-2.6`) | 70.7 → 62.4 (`-8.3`) | 99.1 → 98.2 (`-0.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_COST_PLUS1` | KB-02 (Pobór Podatków): cost 1 → 2 | 87.1 → 🟢 ** 51.5** (`-35.6`) | 91.5 → 74.5 (`-17.0`) | 70.7 → 28.6 (`-42.1`) | 99.1 → 0.0 (`-99.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_COST_MINUS1` | KB-02 (Pobór Podatków): cost 1 → 0 | 87.1 → 🟢 ** 82.7** (`-4.4`) | 91.5 → 76.5 (`-15.0`) | 70.7 → 74.7 (`⬆️ +4.0`) | 99.1 → 96.9 (`-2.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_HERESY_PLUS1` | KB-02 (Pobór Podatków): heresy 0 → 1 | 87.1 → 🟢 ** 73.2** (`-13.9`) | 91.5 → 84.3 (`-7.2`) | 70.7 → 52.6 (`-18.1`) | 99.1 → 82.7 (`-16.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_COST_PLUS1` | KB-03 (Plotka Dworska): cost 1 → 2 | 87.1 → 🟢 ** 84.9** (`-2.2`) | 91.5 → 82.2 (`-9.3`) | 70.7 → 74.4 (`⬆️ +3.7`) | 99.1 → 98.0 (`-1.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_COST_MINUS1` | KB-03 (Plotka Dworska): cost 1 → 0 | 87.1 → 🟢 ** 75.0** (`-12.1`) | 91.5 → 76.4 (`-15.1`) | 70.7 → 66.1 (`-4.6`) | 99.1 → 82.4 (`-16.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_HERESY_PLUS1` | KB-03 (Plotka Dworska): heresy 0 → 1 | 87.1 → 🟢 ** 72.9** (`-14.2`) | 91.5 → 85.5 (`-6.0`) | 70.7 → 58.4 (`-12.3`) | 99.1 → 74.9 (`-24.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_COST_PLUS1` | KB-04 (Faworyt Dworu): cost 1 → 2 | 87.1 → 🟢 ** 89.0** (`⬆️ +1.9`) | 91.5 → 90.2 (`-1.3`) | 70.7 → 78.9 (`⬆️ +8.2`) | 99.1 → 98.0 (`-1.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-04_COST_MINUS1` | KB-04 (Faworyt Dworu): cost 1 → 0 | 87.1 → 🟢 ** 83.1** (`-4.0`) | 91.5 → 77.8 (`-13.7`) | 70.7 → 73.2 (`⬆️ +2.5`) | 99.1 → 98.4 (`-0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_HERESY_PLUS1` | KB-04 (Faworyt Dworu): heresy 1 → 2 | 87.1 → 🟢 ** 68.0** (`-19.1`) | 91.5 → 82.2 (`-9.3`) | 70.7 → 66.9 (`-3.8`) | 99.1 → 55.0 (`-44.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_HERESY_MINUS1` | KB-04 (Faworyt Dworu): heresy 1 → 0 | 87.1 → 🟢 ** 90.4** (`⬆️ +3.3`) | 91.5 → 90.8 (`-0.7`) | 70.7 → 82.3 (`⬆️ +11.6`) | 99.1 → 98.2 (`-0.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-05_COST_PLUS1` | KB-05 (List Żelazny): cost 2 → 3 | 87.1 → 🟢 ** 70.1** (`-17.0`) | 91.5 → 87.5 (`-4.0`) | 70.7 → 68.5 (`-2.2`) | 99.1 → 54.4 (`-44.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_COST_MINUS1` | KB-05 (List Żelazny): cost 2 → 1 | 87.1 → 🟢 ** 82.0** (`-5.1`) | 91.5 → 74.6 (`-16.9`) | 70.7 → 73.3 (`⬆️ +2.6`) | 99.1 → 98.0 (`-1.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_HERESY_PLUS1` | KB-05 (List Żelazny): heresy 0 → 1 | 87.1 → 🟢 ** 85.2** (`-1.9`) | 91.5 → 89.7 (`-1.8`) | 70.7 → 67.7 (`-3.0`) | 99.1 → 98.1 (`-1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_COST_PLUS1` | KB-06 (Areszt Królewski): cost 2 → 3 | 87.1 → 🟢 ** 88.5** (`⬆️ +1.4`) | 91.5 → 91.0 (`-0.5`) | 70.7 → 75.3 (`⬆️ +4.6`) | 99.1 → 99.3 (`⬆️ +0.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-06_COST_MINUS1` | KB-06 (Areszt Królewski): cost 2 → 1 | 87.1 → 🟢 ** 74.6** (`-12.5`) | 91.5 → 90.2 (`-1.3`) | 70.7 → 69.4 (`-1.3`) | 99.1 → 64.2 (`-34.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_HERESY_PLUS1` | KB-06 (Areszt Królewski): heresy 0 → 1 | 87.1 → 🟢 ** 86.2** (`-0.9`) | 91.5 → 91.2 (`-0.3`) | 70.7 → 68.2 (`-2.5`) | 99.1 | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_COST_PLUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 3 | 87.1 → 🟢 ** 87.2** (`⬆️ +0.1`) | 91.5 → 90.3 (`-1.2`) | 70.7 → 72.1 (`⬆️ +1.4`) | 99.1 → 99.3 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L3_KB-07_COST_MINUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 1 | 87.1 → 🟢 ** 78.3** (`-8.8`) | 91.5 → 84.3 (`-7.2`) | 70.7 → 84.7 (`⬆️ +14.0`) | 99.1 → 66.0 (`-33.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_HERESY_PLUS1` | KB-07 (Szantaż Pieczęcią): heresy 0 → 1 | 87.1 → 🟢 ** 78.8** (`-8.3`) | 91.5 → 87.4 (`-4.1`) | 70.7 → 50.7 (`-20.0`) | 99.1 → 98.4 (`-0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_COST_PLUS1` | KB-08 (Przekupstwo Sędziego): cost 3 → 4 | 87.1 → 🟢 ** 88.1** (`⬆️ +1.0`) | 91.5 → 91.0 (`-0.5`) | 70.7 → 75.3 (`⬆️ +4.6`) | 99.1 → 98.0 (`-1.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-08_COST_MINUS1` | KB-08 (Przekupstwo Sędziego): cost 3 → 2 | 87.1 → 🟢 ** 86.0** (`-1.1`) | 91.5 → 91.2 (`-0.3`) | 70.7 → 68.6 (`-2.1`) | 99.1 → 98.1 (`-1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_HERESY_PLUS1` | KB-08 (Przekupstwo Sędziego): heresy 0 → 1 | 87.1 → 🟢 ** 86.8** (`-0.3`) | 91.5 → 91.6 (`⬆️ +0.1`) | 70.7 → 69.8 (`-0.9`) | 99.1 | ⚪ OPTYMALNY |
| `L3_KB-09_COST_PLUS1` | KB-09 (Dekret Królewski): cost 3 → 4 | 87.1 → 🔴 ** 23.9** (`-63.2`) | 91.5 → 38.5 (`-53.0`) | 70.7 → 9.2 (`-61.5`) | 99.1 → 0.0 (`-99.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_COST_MINUS1` | KB-09 (Dekret Królewski): cost 3 → 2 | 87.1 → 🟢 ** 71.2** (`-15.9`) | 91.5 → 77.8 (`-13.7`) | 70.7 → 66.7 (`-4.0`) | 99.1 → 69.1 (`-30.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_HERESY_PLUS1` | KB-09 (Dekret Królewski): heresy 1 → 2 | 87.1 → 🟢 ** 62.8** (`-24.3`) | 91.5 → 83.6 (`-7.9`) | 70.7 → 28.7 (`-42.0`) | 99.1 → 76.0 (`-23.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_HERESY_MINUS1` | KB-09 (Dekret Królewski): heresy 1 → 0 | 87.1 → 🟢 ** 90.3** (`⬆️ +3.2`) | 91.5 → 89.9 (`-1.6`) | 70.7 → 82.4 (`⬆️ +11.7`) | 99.1 → 98.5 (`-0.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-10_COST_PLUS1` | KB-10 (Pieczęć Korony): cost 2 → 3 | 87.1 → 🔴 ** 24.4** (`-62.7`) | 91.5 → 39.5 (`-52.0`) | 70.7 → 9.2 (`-61.5`) | 99.1 → 0.0 (`-99.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_COST_MINUS1` | KB-10 (Pieczęć Korony): cost 2 → 1 | 87.1 → 🟢 ** 67.4** (`-19.7`) | 91.5 → 61.2 (`-30.3`) | 70.7 → 41.1 (`-29.6`) | 99.1 → 99.8 (`⬆️ +0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_HERESY_PLUS1` | KB-10 (Pieczęć Korony): heresy 2 → 3 | 87.1 → 🟡 ** 38.5** (`-48.6`) | 91.5 → 58.5 (`-33.0`) | 70.7 → 9.2 (`-61.5`) | 99.1 → 47.8 (`-51.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_HERESY_MINUS1` | KB-10 (Pieczęć Korony): heresy 2 → 1 | 87.1 → 🟢 ** 80.2** (`-6.9`) | 91.5 → 85.0 (`-6.5`) | 70.7 → 84.8 (`⬆️ +14.1`) | 99.1 → 70.9 (`-28.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 87.1 → 🟢 ** 83.6** (`-3.5`) | 91.5 → 89.0 (`-2.5`) | 70.7 → 62.8 (`-7.9`) | 99.1 → 98.9 (`-0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_COST_MINUS1` | KT-01 (Rytuał Przejścia): cost 1 → 0 | 87.1 → 🟢 ** 81.7** (`-5.4`) | 91.5 → 90.4 (`-1.1`) | 70.7 → 69.6 (`-1.1`) | 99.1 → 85.0 (`-14.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_HERESY_PLUS1` | KT-01 (Rytuał Przejścia): heresy 0 → 1 | 87.1 → 🟢 ** 87.2** (`⬆️ +0.1`) | 91.5 → 89.7 (`-1.8`) | 70.7 → 72.8 (`⬆️ +2.1`) | 99.1 | ⚪ OPTYMALNY |
| `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 87.1 → 🟢 ** 87.3** (`⬆️ +0.2`) | 91.5 → 90.3 (`-1.2`) | 70.7 → 74.5 (`⬆️ +3.8`) | 99.1 → 97.0 (`-2.1`) | ⚪ OPTYMALNY |
| `L3_KT-02_COST_MINUS1` | KT-02 (Transmutacja Złota): cost 1 → 0 | 87.1 → 🟢 ** 87.9** (`⬆️ +0.8`) | 91.5 → 90.8 (`-0.7`) | 70.7 → 75.0 (`⬆️ +4.3`) | 99.1 → 97.9 (`-1.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-02_HERESY_PLUS1` | KT-02 (Transmutacja Złota): heresy 0 → 1 | 87.1 → 🟢 ** 87.5** (`⬆️ +0.4`) | 91.5 → 90.4 (`-1.1`) | 70.7 → 72.7 (`⬆️ +2.0`) | 99.1 → 99.3 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L3_KT-03_COST_PLUS1` | KT-03 (Zakazana Wiedza): cost 0 → 1 | 87.1 → 🟢 ** 86.0** (`-1.1`) | 91.5 → 90.9 (`-0.6`) | 70.7 → 69.0 (`-1.7`) | 99.1 → 98.0 (`-1.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_HERESY_PLUS1` | KT-03 (Zakazana Wiedza): heresy 1 → 2 | 87.1 → 🟢 ** 88.0** (`⬆️ +0.9`) | 91.5 → 88.8 (`-2.7`) | 70.7 → 76.4 (`⬆️ +5.7`) | 99.1 → 98.9 (`-0.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-03_HERESY_MINUS1` | KT-03 (Zakazana Wiedza): heresy 1 → 0 | 87.1 → 🟢 ** 87.0** (`-0.1`) | 91.5 → 89.9 (`-1.6`) | 70.7 → 72.5 (`⬆️ +1.8`) | 99.1 → 98.5 (`-0.6`) | ⚪ OPTYMALNY |
| `L3_KT-04_COST_PLUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 2 | 87.1 → 🟢 ** 83.5** (`-3.6`) | 91.5 → 87.8 (`-3.7`) | 70.7 → 64.0 (`-6.7`) | 99.1 → 98.8 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-04_COST_MINUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 0 | 87.1 → 🟢 ** 82.9** (`-4.2`) | 91.5 → 90.8 (`-0.7`) | 70.7 → 72.8 (`⬆️ +2.1`) | 99.1 → 85.0 (`-14.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-04_HERESY_PLUS1` | KT-04 (Zwierciadło Herezji): heresy 0 → 1 | 87.1 → 🟢 ** 87.4** (`⬆️ +0.3`) | 91.5 → 92.0 (`⬆️ +0.5`) | 70.7 → 71.1 (`⬆️ +0.4`) | 99.1 | ⚪ OPTYMALNY |
| `L3_KT-05_COST_PLUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 2 | 87.1 → 🟢 ** 88.0** (`⬆️ +0.9`) | 91.5 → 89.5 (`-2.0`) | 70.7 → 76.4 (`⬆️ +5.7`) | 99.1 → 98.2 (`-0.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-05_COST_MINUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 0 | 87.1 → 🟢 ** 81.1** (`-6.0`) | 91.5 → 89.8 (`-1.7`) | 70.7 → 74.3 (`⬆️ +3.6`) | 99.1 → 79.1 (`-20.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_HERESY_PLUS1` | KT-05 (Wskazówka Cyklu): heresy 0 → 1 | 87.1 → 🟢 ** 87.5** (`⬆️ +0.4`) | 91.5 → 89.3 (`-2.2`) | 70.7 → 74.2 (`⬆️ +3.5`) | 99.1 → 98.9 (`-0.2`) | ⚪ OPTYMALNY |
| `L3_KT-06_COST_PLUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 3 | 87.1 → 🟢 ** 81.9** (`-5.2`) | 91.5 → 89.5 (`-2.0`) | 70.7 → 70.9 (`⬆️ +0.2`) | 99.1 → 85.2 (`-13.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_COST_MINUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 1 | 87.1 → 🟢 ** 85.2** (`-1.9`) | 91.5 → 89.9 (`-1.6`) | 70.7 → 68.7 (`-2.0`) | 99.1 → 96.9 (`-2.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_HERESY_PLUS1` | KT-06 (Przesłuchanie Imienia): heresy 0 → 1 | 87.1 → 🟢 ** 86.8** (`-0.3`) | 91.5 → 86.6 (`-4.9`) | 70.7 → 75.6 (`⬆️ +4.9`) | 99.1 → 98.1 (`-1.0`) | ⚪ OPTYMALNY |
| `L3_KT-07_COST_PLUS1` | KT-07 (Archiwum Ukryte): cost 1 → 2 | 87.1 → 🟢 ** 81.1** (`-6.0`) | 91.5 → 91.3 (`-0.2`) | 70.7 → 65.2 (`-5.5`) | 99.1 → 86.7 (`-12.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_COST_MINUS1` | KT-07 (Archiwum Ukryte): cost 1 → 0 | 87.1 → 🟢 ** 86.4** (`-0.7`) | 91.5 → 90.6 (`-0.9`) | 70.7 → 71.8 (`⬆️ +1.1`) | 99.1 → 96.8 (`-2.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_HERESY_PLUS1` | KT-07 (Archiwum Ukryte): heresy 0 → 1 | 87.1 → 🟢 ** 87.4** (`⬆️ +0.3`) | 91.5 → 91.3 (`-0.2`) | 70.7 → 71.8 (`⬆️ +1.1`) | 99.1 → 99.2 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_KT-08_COST_PLUS1` | KT-08 (Areszt Wiedzy): cost 2 → 3 | 87.1 → 🟢 ** 86.0** (`-1.1`) | 91.5 → 89.6 (`-1.9`) | 70.7 → 69.3 (`-1.4`) | 99.1 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_COST_MINUS1` | KT-08 (Areszt Wiedzy): cost 2 → 1 | 87.1 → 🟢 ** 87.0** (`-0.1`) | 91.5 → 89.9 (`-1.6`) | 70.7 → 74.2 (`⬆️ +3.5`) | 99.1 → 96.9 (`-2.2`) | ⚪ OPTYMALNY |
| `L3_KT-08_HERESY_PLUS1` | KT-08 (Areszt Wiedzy): heresy 0 → 1 | 87.1 → 🟢 ** 87.0** (`-0.1`) | 91.5 → 89.4 (`-2.1`) | 70.7 → 72.3 (`⬆️ +1.6`) | 99.1 → 99.2 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 1 → 2 | 87.1 → 🟢 ** 86.3** (`-0.8`) | 91.5 → 87.9 (`-3.6`) | 70.7 → 72.3 (`⬆️ +1.6`) | 99.1 → 98.8 (`-0.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_COST_MINUS1` | KT-09 (Fragment Kodeksu): cost 1 → 0 | 87.1 → 🟢 ** 82.0** (`-5.1`) | 91.5 → 89.4 (`-2.1`) | 70.7 → 71.5 (`⬆️ +0.8`) | 99.1 → 85.2 (`-13.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_HERESY_PLUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 2 | 87.1 → 🟢 ** 87.7** (`⬆️ +0.6`) | 91.5 → 87.8 (`-3.7`) | 70.7 → 76.3 (`⬆️ +5.6`) | 99.1 → 98.9 (`-0.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-09_HERESY_MINUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 0 | 87.1 → 🟢 ** 86.1** (`-1.0`) | 91.5 → 87.9 (`-3.6`) | 70.7 → 71.4 (`⬆️ +0.7`) | 99.1 | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_COST_PLUS1` | KT-10 (Pieczęć Salomona): cost 1 → 2 | 87.1 → 🟢 ** 89.3** (`⬆️ +2.2`) | 91.5 → 90.6 (`-0.9`) | 70.7 → 78.0 (`⬆️ +7.3`) | 99.1 → 99.2 (`⬆️ +0.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-10_COST_MINUS1` | KT-10 (Pieczęć Salomona): cost 1 → 0 | 87.1 → 🟢 ** 85.6** (`-1.5`) | 91.5 → 89.6 (`-1.9`) | 70.7 → 70.1 (`-0.6`) | 99.1 → 97.2 (`-1.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_HERESY_PLUS1` | KT-10 (Pieczęć Salomona): heresy 0 → 1 | 87.1 → 🟢 ** 82.1** (`-5.0`) | 91.5 → 86.5 (`-5.0`) | 70.7 → 62.9 (`-7.8`) | 99.1 → 96.9 (`-2.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_COST_PLUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 2 | 87.1 → 🟢 ** 68.9** (`-18.2`) | 91.5 → 93.0 (`⬆️ +1.5`) | 70.7 → 64.2 (`-6.5`) | 99.1 → 49.4 (`-49.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_COST_MINUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 0 | 87.1 → 🟢 ** 74.8** (`-12.3`) | 91.5 | 70.7 → 62.5 (`-8.2`) | 99.1 → 70.5 (`-28.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-01_HERESY_PLUS1` | SO-01 (Patrol Familiariuszy): heresy 0 → 1 | 87.1 → 🟢 ** 83.9** (`-3.2`) | 91.5 → 87.5 (`-4.0`) | 70.7 → 65.2 (`-5.5`) | 99.1 → 99.0 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 87.1 → 🟢 ** 81.9** (`-5.2`) | 91.5 → 88.6 (`-2.9`) | 70.7 → 70.6 (`-0.1`) | 99.1 → 86.5 (`-12.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_COST_MINUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 0 | 87.1 → 🟢 ** 65.5** (`-21.6`) | 91.5 → 87.2 (`-4.3`) | 70.7 → 54.3 (`-16.4`) | 99.1 → 55.1 (`-44.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): heresy 0 → 1 | 87.1 → 🟢 ** 82.2** (`-4.9`) | 91.5 → 83.9 (`-7.6`) | 70.7 → 64.7 (`-6.0`) | 99.1 → 97.9 (`-1.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_COST_PLUS1` | SO-03 (Podejrzenie): cost 1 → 2 | 87.1 → 🟢 ** 85.7** (`-1.4`) | 91.5 → 90.3 (`-1.2`) | 70.7 → 68.4 (`-2.3`) | 99.1 → 98.5 (`-0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_COST_MINUS1` | SO-03 (Podejrzenie): cost 1 → 0 | 87.1 → 🟢 ** 78.5** (`-8.6`) | 91.5 → 93.9 (`⬆️ +2.4`) | 70.7 → 69.3 (`-1.4`) | 99.1 → 72.4 (`-26.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_HERESY_PLUS1` | SO-03 (Podejrzenie): heresy 0 → 1 | 87.1 → 🟢 ** 82.5** (`-4.6`) | 91.5 → 85.5 (`-6.0`) | 70.7 → 63.5 (`-7.2`) | 99.1 → 98.4 (`-0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_COST_PLUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 2 | 87.1 → 🟢 ** 85.0** (`-2.1`) | 91.5 → 92.0 (`⬆️ +0.5`) | 70.7 → 77.5 (`⬆️ +6.8`) | 99.1 → 85.4 (`-13.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_COST_MINUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 0 | 87.1 → 🟢 ** 86.5** (`-0.6`) | 91.5 → 91.7 (`⬆️ +0.2`) | 70.7 → 71.9 (`⬆️ +1.2`) | 99.1 → 96.0 (`-3.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_HERESY_PLUS1` | SO-04 (Publiczne Ostrzeżenie): heresy 0 → 1 | 87.1 → 🟢 ** 77.6** (`-9.5`) | 91.5 → 84.3 (`-7.2`) | 70.7 → 50.6 (`-20.1`) | 99.1 → 97.8 (`-1.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-05_COST_PLUS1` | SO-05 (Wezwanie do Trybunału): cost 0 → 1 | 🟢 ** 87.1** | 91.5 | 70.7 | 99.1 | ⚪ OPTYMALNY |
| `L3_SO-05_HERESY_PLUS1` | SO-05 (Wezwanie do Trybunału): heresy 0 → 1 | 🟢 ** 87.1** | 91.5 | 70.7 | 99.1 | ⚪ OPTYMALNY |
| `L3_SO-06_COST_PLUS1` | SO-06 (Areszt Trybunalski): cost 2 → 3 | 87.1 → 🟢 ** 85.6** (`-1.5`) | 91.5 → 87.9 (`-3.6`) | 70.7 → 71.5 (`⬆️ +0.8`) | 99.1 → 97.5 (`-1.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_COST_MINUS1` | SO-06 (Areszt Trybunalski): cost 2 → 1 | 87.1 → 🟢 ** 89.3** (`⬆️ +2.2`) | 91.5 → 88.4 (`-3.1`) | 70.7 → 82.2 (`⬆️ +11.5`) | 99.1 → 97.2 (`-1.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-06_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): heresy 0 → 1 | 🟢 ** 87.1** | 91.5 → 92.0 (`⬆️ +0.5`) | 70.7 → 70.4 (`-0.3`) | 99.1 → 98.9 (`-0.2`) | ⚪ OPTYMALNY |
| `L3_SO-07_COST_PLUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 3 | 87.1 → 🟢 ** 86.6** (`-0.5`) | 91.5 → 92.0 (`⬆️ +0.5`) | 70.7 → 69.8 (`-0.9`) | 99.1 → 98.1 (`-1.0`) | ⚪ OPTYMALNY |
| `L3_SO-07_COST_MINUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 1 | 87.1 → 🟢 ** 81.6** (`-5.5`) | 91.5 → 89.9 (`-1.6`) | 70.7 → 68.1 (`-2.6`) | 99.1 → 86.9 (`-12.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-07_HERESY_PLUS1` | SO-07 (Przesłuchanie Oficjum): heresy 0 → 1 | 87.1 → 🟢 ** 87.0** (`-0.1`) | 91.5 → 90.1 (`-1.4`) | 70.7 → 72.9 (`⬆️ +2.2`) | 99.1 → 98.1 (`-1.0`) | ⚪ OPTYMALNY |
| `L3_SO-08_COST_PLUS1` | SO-08 (Nasłanie Inkwizytora): cost 2 → 3 | 87.1 → 🟢 ** 79.7** (`-7.4`) | 91.5 → 89.8 (`-1.7`) | 70.7 → 74.2 (`⬆️ +3.5`) | 99.1 → 75.2 (`-23.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_COST_MINUS1` | SO-08 (Nasłanie Inkwizytora): cost 2 → 1 | 87.1 → 🟢 ** 77.9** (`-9.2`) | 91.5 → 86.8 (`-4.7`) | 70.7 → 49.1 (`-21.6`) | 99.1 → 97.7 (`-1.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_HERESY_PLUS1` | SO-08 (Nasłanie Inkwizytora): heresy 1 → 2 | 87.1 → 🟢 ** 82.2** (`-4.9`) | 91.5 → 83.9 (`-7.6`) | 70.7 → 64.9 (`-5.8`) | 99.1 → 97.9 (`-1.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_HERESY_MINUS1` | SO-08 (Nasłanie Inkwizytora): heresy 1 → 0 | 87.1 → 🟢 ** 88.6** (`⬆️ +1.5`) | 91.5 → 90.5 (`-1.0`) | 70.7 → 75.8 (`⬆️ +5.1`) | 99.1 → 99.6 (`⬆️ +0.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-09_COST_PLUS1` | SO-09 (Świadek Koronny): cost 2 → 3 | 87.1 → 🟢 ** 84.5** (`-2.6`) | 91.5 → 90.3 (`-1.2`) | 70.7 → 77.2 (`⬆️ +6.5`) | 99.1 → 86.1 (`-13.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_COST_MINUS1` | SO-09 (Świadek Koronny): cost 2 → 1 | 87.1 → 🟢 ** 75.2** (`-11.9`) | 91.5 → 90.8 (`-0.7`) | 70.7 → 66.9 (`-3.8`) | 99.1 → 67.8 (`-31.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_HERESY_PLUS1` | SO-09 (Świadek Koronny): heresy 0 → 1 | 87.1 → 🟢 ** 86.5** (`-0.6`) | 91.5 → 90.0 (`-1.5`) | 70.7 → 71.8 (`⬆️ +1.1`) | 99.1 → 97.7 (`-1.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_COST_PLUS1` | SO-10 (Oczyść Miasto): cost 4 → 5 | 87.1 → 🟢 ** 71.3** (`-15.8`) | 91.5 → 71.3 (`-20.2`) | 70.7 → 61.0 (`-9.7`) | 99.1 → 81.7 (`-17.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_COST_MINUS1` | SO-10 (Oczyść Miasto): cost 4 → 3 | 87.1 → 🟢 ** 70.5** (`-16.6`) | 91.5 → 92.6 (`⬆️ +1.1`) | 70.7 → 60.1 (`-10.6`) | 99.1 → 58.9 (`-40.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_HERESY_PLUS1` | SO-10 (Oczyść Miasto): heresy 2 → 3 | 87.1 → 🟢 ** 80.6** (`-6.5`) | 91.5 → 85.9 (`-5.6`) | 70.7 → 58.0 (`-12.7`) | 99.1 → 98.0 (`-1.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_HERESY_MINUS1` | SO-10 (Oczyść Miasto): heresy 2 → 1 | 87.1 → 🟢 ** 87.3** (`⬆️ +0.2`) | 91.5 → 87.3 (`-4.2`) | 70.7 → 76.1 (`⬆️ +5.4`) | 99.1 → 98.5 (`-0.6`) | ⚪ OPTYMALNY |

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | 5.62 Er (1–9) | 3.1% | 28.7% | 1.03 (0–3) | 3.64 (0–15) | 0.53zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_COST_PLUS1` | 5.65 Er (1–9) | 3.4% | 30.2% | 1.03 (0–4) | 3.72 (0–17) | 0.57zł (0.0–2.7) | 6.28 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-01_COST_MINUS1` | 5.59 Er (1–9) | 2.8% | 28.4% | 1.03 (0–3) | 3.62 (0–17) | 0.57zł (0.0–2.7) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_HERESY_PLUS1` | 5.59 Er (1–9) | 2.9% | 28.6% | 1.02 (0–3) | 3.70 (0–16) | 0.53zł (0.0–2.7) | 6.34 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_COST_PLUS1` | 5.66 Er (1–9) | 3.5% | 31.2% | 1.03 (0–3) | 3.71 (0–17) | 0.56zł (0.0–2.3) | 6.28 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-02_COST_MINUS1` | 5.60 Er (1–9) | 3.0% | 28.4% | 1.03 (0–4) | 3.62 (0–17) | 0.58zł (0.0–3.0) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_HERESY_PLUS1` | 5.60 Er (1–9) | 2.8% | 28.6% | 1.03 (0–3) | 3.72 (0–15) | 0.52zł (0.0–2.7) | 6.38 (1.3–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_COST_PLUS1` | 5.67 Er (1–9) | 3.5% | 30.1% | 1.04 (0–4) | 3.68 (0–15) | 0.54zł (0.0–2.7) | 6.23 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-03_COST_MINUS1` | 5.59 Er (1–9) | 2.7% | 28.5% | 1.02 (0–3) | 3.64 (0–17) | 0.57zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_HERESY_PLUS1` | 5.60 Er (1–9) | 2.7% | 28.6% | 1.02 (0–3) | 3.75 (0–15) | 0.53zł (0.0–2.7) | 6.38 (1.4–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_HERESY_MINUS1` | 5.65 Er (1–9) | 3.1% | 28.8% | 1.03 (0–3) | 3.56 (0–17) | 0.53zł (0.0–2.7) | 6.09 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_COST_PLUS1` | 5.67 Er (1–9) | 3.2% | 30.1% | 1.04 (0–3) | 3.65 (0–17) | 0.56zł (0.0–2.7) | 6.24 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-04_COST_MINUS1` | 5.59 Er (1–9) | 2.9% | 28.4% | 1.03 (0–3) | 3.61 (0–17) | 0.57zł (0.0–2.7) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_HERESY_PLUS1` | 5.60 Er (1–9) | 2.9% | 28.6% | 1.03 (0–3) | 3.73 (0–16) | 0.53zł (0.0–2.7) | 6.37 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_COST_PLUS1` | 5.68 Er (1–9) | 3.7% | 30.0% | 1.04 (0–4) | 3.65 (0–15) | 0.54zł (0.0–2.7) | 6.25 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-05_COST_MINUS1` | 5.58 Er (1–9) | 2.7% | 28.4% | 1.02 (0–3) | 3.62 (0–17) | 0.56zł (0.0–2.7) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_HERESY_PLUS1` | 5.60 Er (1–9) | 2.8% | 28.6% | 1.03 (0–3) | 3.74 (0–15) | 0.53zł (0.0–2.7) | 6.38 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_COST_PLUS1` | 5.64 Er (1–9) | 3.5% | 29.1% | 1.04 (0–3) | 3.69 (0–16) | 0.54zł (0.0–2.7) | 6.30 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_COST_MINUS1` | 5.59 Er (1–9) | 2.9% | 28.6% | 1.02 (0–3) | 3.61 (0–17) | 0.54zł (0.0–2.7) | 6.19 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_HERESY_PLUS1` | 5.61 Er (1–9) | 3.0% | 28.7% | 1.03 (0–3) | 3.67 (0–15) | 0.53zł (0.0–2.7) | 6.31 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_COST_PLUS1` | 5.63 Er (1–9) | 3.0% | 29.3% | 1.04 (0–3) | 3.63 (0–18) | 0.53zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_COST_MINUS1` | 5.58 Er (1–9) | 2.7% | 28.6% | 1.03 (0–3) | 3.61 (0–15) | 0.54zł (0.0–2.3) | 6.20 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_HERESY_PLUS1` | 5.60 Er (1–9) | 2.8% | 28.6% | 1.03 (0–3) | 3.72 (0–15) | 0.52zł (0.0–2.7) | 6.36 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_COST_PLUS1` | 5.64 Er (1–9) | 3.1% | 30.3% | 1.03 (0–4) | 3.60 (0–16) | 0.59zł (0.0–2.7) | 6.17 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-08_COST_MINUS1` | 5.61 Er (1–9) | 2.9% | 28.5% | 1.03 (0–3) | 3.68 (0–17) | 0.58zł (0.0–2.7) | 6.29 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_HERESY_PLUS1` | 5.60 Er (1–9) | 2.8% | 28.6% | 1.03 (0–3) | 3.65 (0–15) | 0.53zł (0.0–2.7) | 6.32 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_HERESY_MINUS1` | 5.63 Er (1–9) | 3.1% | 28.7% | 1.03 (0–3) | 3.59 (0–15) | 0.53zł (0.0–2.7) | 6.17 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_COST_PLUS1` | 5.70 Er (1–9) | 3.4% | 29.1% | 1.04 (0–3) | 3.66 (0–15) | 0.54zł (0.0–2.7) | 6.25 (1.3–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_COST_MINUS1` | 5.60 Er (1–9) | 2.9% | 28.1% | 1.03 (0–3) | 3.62 (0–15) | 0.56zł (0.0–2.7) | 6.21 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_HERESY_PLUS1` | 5.57 Er (1–9) | 2.6% | 28.5% | 1.02 (0–3) | 3.81 (0–15) | 0.52zł (0.0–2.7) | 6.44 (1.5–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_COST_PLUS1` | 5.73 Er (1–9) | 3.9% | 30.2% | 1.05 (0–3) | 3.73 (0–15) | 0.53zł (0.0–2.3) | 6.24 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-10_COST_MINUS1` | 5.60 Er (1–9) | 2.9% | 28.2% | 1.03 (0–3) | 3.64 (0–17) | 0.56zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_PLUS1` | 5.52 Er (1–9) | 2.6% | 28.4% | 1.01 (0–3) | 3.89 (0–18) | 0.52zł (0.0–2.7) | 6.46 (1.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_MINUS1` | 5.65 Er (1–9) | 3.2% | 28.8% | 1.03 (0–3) | 3.49 (0–17) | 0.53zł (0.0–3.0) | 5.85 (0.7–9.7) | 🟢 W NORMIE |
| `L3_GC-01_COST_PLUS1` | 5.62 Er (1–9) | 3.0% | 29.2% | 1.03 (0–3) | 3.63 (0–15) | 0.55zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-01_COST_MINUS1` | 5.59 Er (1–9) | 2.8% | 27.9% | 1.02 (0–3) | 3.63 (0–15) | 0.55zł (0.0–2.7) | 6.32 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-01_HERESY_PLUS1` | 5.61 Er (1–9) | 2.9% | 28.6% | 1.03 (0–3) | 3.67 (0–15) | 0.53zł (0.0–2.7) | 6.36 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-02_COST_PLUS1` | 5.67 Er (1–9) | 3.6% | 30.5% | 1.04 (0–3) | 3.68 (0–16) | 0.52zł (0.0–2.7) | 6.21 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-02_COST_MINUS1` | 5.57 Er (1–9) | 2.9% | 27.9% | 1.02 (0–3) | 3.64 (0–16) | 0.56zł (0.0–2.7) | 6.32 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-02_HERESY_PLUS1` | 5.60 Er (1–9) | 3.0% | 28.5% | 1.03 (0–3) | 3.71 (0–15) | 0.53zł (0.0–3.0) | 6.37 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-03_COST_PLUS1` | 5.67 Er (1–9) | 3.3% | 29.3% | 1.03 (0–3) | 3.59 (0–15) | 0.54zł (0.0–2.7) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-03_COST_MINUS1` | 5.59 Er (1–9) | 3.0% | 27.9% | 1.02 (0–3) | 3.65 (0–15) | 0.55zł (0.0–2.7) | 6.33 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-03_HERESY_PLUS1` | 5.61 Er (1–9) | 3.1% | 28.6% | 1.03 (0–3) | 3.71 (0–15) | 0.52zł (0.0–2.7) | 6.38 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-04_COST_PLUS1` | 5.65 Er (1–9) | 3.4% | 29.3% | 1.04 (0–3) | 3.61 (0–16) | 0.54zł (0.0–2.7) | 6.20 (1.3–10.0) | 🟢 W NORMIE |
| `L3_GC-04_COST_MINUS1` | 5.58 Er (1–9) | 2.8% | 28.0% | 1.02 (0–3) | 3.71 (0–15) | 0.55zł (0.0–2.7) | 6.33 (1.4–10.0) | 🟢 W NORMIE |
| `L3_GC-04_HERESY_PLUS1` | 5.60 Er (1–9) | 3.0% | 28.6% | 1.03 (0–3) | 3.77 (0–18) | 0.53zł (0.0–2.7) | 6.38 (1.4–10.0) | 🟢 W NORMIE |
| `L3_GC-04_HERESY_MINUS1` | 5.63 Er (1–9) | 3.1% | 28.7% | 1.03 (0–3) | 3.53 (0–15) | 0.52zł (0.0–2.7) | 6.11 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-05_COST_PLUS1` | 5.62 Er (1–9) | 3.1% | 28.7% | 1.03 (0–3) | 3.64 (0–15) | 0.53zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-05_HERESY_PLUS1` | 5.62 Er (1–9) | 3.1% | 28.7% | 1.03 (0–3) | 3.64 (0–15) | 0.53zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-06_COST_PLUS1` | 5.66 Er (1–9) | 3.4% | 29.2% | 1.04 (0–4) | 3.72 (0–16) | 0.52zł (0.0–3.0) | 6.33 (1.3–10.0) | 🟢 W NORMIE |
| `L3_GC-06_COST_MINUS1` | 5.57 Er (1–9) | 2.9% | 28.1% | 1.02 (0–3) | 3.64 (0–15) | 0.54zł (0.0–2.7) | 6.32 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-06_HERESY_PLUS1` | 5.61 Er (1–9) | 3.1% | 28.6% | 1.03 (0–4) | 3.69 (0–15) | 0.53zł (0.0–2.7) | 6.38 (1.4–10.0) | 🟢 W NORMIE |
| `L3_GC-07_COST_PLUS1` | 5.61 Er (1–9) | 3.2% | 28.9% | 1.04 (0–3) | 3.62 (0–16) | 0.53zł (0.0–2.7) | 6.26 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-07_COST_MINUS1` | 5.60 Er (1–9) | 2.8% | 28.2% | 1.03 (0–3) | 3.67 (0–15) | 0.51zł (0.0–2.7) | 6.35 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-07_HERESY_PLUS1` | 5.62 Er (1–9) | 3.0% | 28.6% | 1.03 (0–3) | 3.66 (0–15) | 0.53zł (0.0–2.7) | 6.31 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-07_HERESY_MINUS1` | 5.62 Er (1–9) | 3.1% | 28.7% | 1.03 (0–4) | 3.62 (0–15) | 0.52zł (0.0–2.7) | 6.20 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_PLUS1` | 5.68 Er (1–9) | 3.2% | 29.7% | 1.04 (0–3) | 3.58 (0–15) | 0.52zł (0.0–2.7) | 6.20 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_MINUS1` | 5.56 Er (1–9) | 2.8% | 27.9% | 1.02 (0–3) | 3.65 (0–15) | 0.55zł (0.0–2.7) | 6.32 (1.3–10.0) | 🟢 W NORMIE |
| `L3_GC-08_HERESY_PLUS1` | 5.59 Er (1–9) | 2.7% | 28.5% | 1.02 (0–3) | 3.72 (0–15) | 0.52zł (0.0–2.7) | 6.37 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-09_COST_PLUS1` | 5.66 Er (1–9) | 3.5% | 29.2% | 1.04 (0–3) | 3.65 (0–14) | 0.51zł (0.0–3.0) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-09_COST_MINUS1` | 5.61 Er (1–9) | 2.5% | 28.4% | 1.03 (0–3) | 3.71 (0–15) | 0.56zł (0.0–2.7) | 6.36 (1.5–10.0) | 🟢 W NORMIE |
| `L3_GC-09_HERESY_PLUS1` | 5.61 Er (1–9) | 2.9% | 28.6% | 1.03 (0–4) | 3.71 (0–14) | 0.53zł (0.0–3.0) | 6.39 (1.5–10.0) | 🟢 W NORMIE |
| `L3_GC-10_COST_PLUS1` | 5.69 Er (1–9) | 3.5% | 28.2% | 1.04 (0–3) | 3.58 (0–16) | 0.58zł (0.0–2.7) | 6.08 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-10_COST_MINUS1` | 5.58 Er (1–9) | 3.1% | 27.8% | 1.02 (0–3) | 3.69 (0–15) | 0.54zł (0.0–2.7) | 6.31 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-10_HERESY_PLUS1` | 5.53 Er (1–9) | 3.0% | 28.3% | 1.01 (0–3) | 3.97 (0–17) | 0.52zł (0.0–2.7) | 6.40 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-10_HERESY_MINUS1` | 5.66 Er (1–9) | 3.5% | 28.8% | 1.04 (0–3) | 3.36 (0–15) | 0.53zł (0.0–2.7) | 6.03 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-01_COST_PLUS1` | 5.61 Er (1–9) | 2.8% | 29.7% | 1.03 (0–3) | 3.64 (0–16) | 0.55zł (0.0–2.7) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-01_COST_MINUS1` | 5.58 Er (1–9) | 2.4% | 28.0% | 1.02 (0–3) | 3.63 (0–15) | 0.54zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-01_HERESY_PLUS1` | 5.59 Er (1–9) | 2.8% | 28.6% | 1.03 (0–3) | 3.66 (0–15) | 0.52zł (0.0–2.7) | 6.29 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-02_COST_PLUS1` | 5.68 Er (1–9) | 3.6% | 31.0% | 1.04 (0–3) | 3.71 (0–15) | 0.54zł (0.0–2.7) | 6.26 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-02_COST_MINUS1` | 5.56 Er (1–9) | 2.5% | 28.4% | 1.02 (0–3) | 3.63 (0–15) | 0.54zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-02_HERESY_PLUS1` | 5.58 Er (1–9) | 3.0% | 28.5% | 1.02 (0–3) | 3.69 (0–19) | 0.53zł (0.0–2.7) | 6.30 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-03_COST_PLUS1` | 5.62 Er (1–9) | 2.8% | 29.8% | 1.03 (0–3) | 3.57 (0–17) | 0.54zł (0.0–2.7) | 6.19 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-03_COST_MINUS1` | 5.56 Er (1–9) | 2.6% | 28.0% | 1.02 (0–4) | 3.66 (0–19) | 0.53zł (0.0–2.7) | 6.30 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-03_HERESY_PLUS1` | 5.58 Er (1–9) | 3.0% | 28.6% | 1.03 (0–3) | 3.70 (0–19) | 0.53zł (0.0–2.7) | 6.31 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-04_COST_PLUS1` | 5.65 Er (1–9) | 2.9% | 29.7% | 1.04 (0–3) | 3.64 (0–17) | 0.55zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-04_COST_MINUS1` | 5.55 Er (1–9) | 2.6% | 28.1% | 1.02 (0–3) | 3.64 (0–16) | 0.54zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-04_HERESY_PLUS1` | 5.56 Er (1–9) | 2.9% | 28.5% | 1.02 (0–3) | 3.75 (0–19) | 0.53zł (0.0–2.7) | 6.30 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-04_HERESY_MINUS1` | 5.67 Er (1–9) | 3.1% | 28.8% | 1.04 (0–3) | 3.54 (0–16) | 0.53zł (0.0–2.7) | 6.18 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-05_COST_PLUS1` | 5.62 Er (1–9) | 2.9% | 28.8% | 1.04 (0–3) | 3.58 (0–16) | 0.53zł (0.0–2.7) | 6.29 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-05_COST_MINUS1` | 5.56 Er (1–9) | 2.5% | 28.1% | 1.02 (0–3) | 3.59 (0–15) | 0.52zł (0.0–2.7) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-05_HERESY_PLUS1` | 5.60 Er (1–9) | 3.0% | 28.6% | 1.03 (0–3) | 3.67 (0–15) | 0.53zł (0.0–2.7) | 6.29 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-06_COST_PLUS1` | 5.60 Er (1–9) | 2.9% | 28.8% | 1.03 (0–4) | 3.63 (0–15) | 0.53zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-06_COST_MINUS1` | 5.65 Er (1–9) | 3.6% | 28.2% | 1.03 (0–3) | 3.68 (0–16) | 0.52zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-06_HERESY_PLUS1` | 5.61 Er (1–9) | 3.0% | 28.6% | 1.03 (0–3) | 3.64 (0–19) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-07_COST_PLUS1` | 5.58 Er (1–9) | 2.7% | 28.8% | 1.02 (0–4) | 3.58 (0–17) | 0.52zł (0.0–3.0) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-07_COST_MINUS1` | 5.59 Er (1–9) | 3.0% | 28.3% | 1.03 (0–3) | 3.63 (0–17) | 0.51zł (0.0–2.7) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-07_HERESY_PLUS1` | 5.58 Er (1–9) | 2.9% | 28.6% | 1.02 (0–3) | 3.65 (0–19) | 0.53zł (0.0–2.7) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-08_COST_PLUS1` | 5.63 Er (1–9) | 3.0% | 28.7% | 1.03 (0–3) | 3.66 (0–19) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-08_COST_MINUS1` | 5.63 Er (1–9) | 3.2% | 28.6% | 1.03 (0–3) | 3.68 (0–17) | 0.53zł (0.0–2.7) | 6.26 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-08_HERESY_PLUS1` | 5.61 Er (1–9) | 3.0% | 28.7% | 1.03 (0–3) | 3.64 (0–15) | 0.53zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-09_COST_PLUS1` | 5.78 Er (1–9) | 4.6% | 28.8% | 1.06 (0–3) | 3.84 (0–16) | 0.57zł (0.0–2.7) | 6.29 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-09_COST_MINUS1` | 5.54 Er (1–9) | 2.6% | 28.3% | 1.02 (0–3) | 3.61 (0–15) | 0.53zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-09_HERESY_PLUS1` | 5.57 Er (1–9) | 3.1% | 28.5% | 1.03 (0–3) | 3.74 (0–15) | 0.53zł (0.0–2.7) | 6.29 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-09_HERESY_MINUS1` | 5.66 Er (1–9) | 3.0% | 28.8% | 1.04 (0–3) | 3.54 (0–15) | 0.53zł (0.0–2.7) | 6.15 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-10_COST_PLUS1` | 5.77 Er (1–9) | 4.6% | 29.0% | 1.06 (0–3) | 3.70 (0–17) | 0.56zł (0.0–2.7) | 6.20 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-10_COST_MINUS1` | 5.51 Er (1–9) | 2.2% | 27.8% | 1.01 (0–3) | 3.62 (0–15) | 0.51zł (0.0–2.7) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-10_HERESY_PLUS1` | 5.45 Er (1–9) | 2.6% | 28.2% | 1.00 (0–3) | 3.90 (0–18) | 0.52zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-10_HERESY_MINUS1` | 5.73 Er (1–9) | 3.5% | 28.9% | 1.06 (0–3) | 3.40 (0–15) | 0.53zł (0.0–2.7) | 6.11 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_PLUS1` | 5.65 Er (1–9) | 3.4% | 29.1% | 1.04 (0–3) | 3.68 (0–16) | 0.44zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_MINUS1` | 5.63 Er (1–9) | 3.1% | 28.6% | 1.03 (0–3) | 3.65 (0–18) | 0.69zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-01_HERESY_PLUS1` | 5.63 Er (1–9) | 3.8% | 28.7% | 1.03 (0–4) | 3.70 (0–18) | 0.53zł (0.0–2.7) | 6.39 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-02_COST_PLUS1` | 5.64 Er (1–9) | 3.4% | 29.5% | 1.03 (0–3) | 3.67 (0–15) | 0.43zł (0.0–2.3) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-02_COST_MINUS1` | 5.63 Er (1–9) | 3.1% | 28.6% | 1.03 (0–3) | 3.63 (0–15) | 0.71zł (0.0–3.0) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-02_HERESY_PLUS1` | 5.62 Er (1–9) | 3.8% | 28.7% | 1.03 (0–3) | 3.71 (0–18) | 0.53zł (0.0–2.7) | 6.39 (1.5–10.0) | 🟢 W NORMIE |
| `L3_KT-03_COST_PLUS1` | 5.64 Er (1–9) | 3.3% | 29.1% | 1.04 (0–3) | 3.67 (0–15) | 0.40zł (0.0–2.3) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-03_HERESY_PLUS1` | 5.62 Er (1–9) | 4.1% | 28.7% | 1.03 (0–3) | 3.73 (0–18) | 0.53zł (0.0–3.0) | 6.40 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-03_HERESY_MINUS1` | 5.63 Er (1–9) | 2.8% | 28.7% | 1.04 (0–4) | 3.61 (0–15) | 0.53zł (0.0–2.7) | 6.11 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-04_COST_PLUS1` | 5.66 Er (1–9) | 3.5% | 29.1% | 1.04 (0–3) | 3.65 (0–16) | 0.43zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-04_COST_MINUS1` | 5.62 Er (1–9) | 3.1% | 28.6% | 1.03 (0–3) | 3.64 (0–18) | 0.70zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-04_HERESY_PLUS1` | 5.61 Er (1–9) | 3.6% | 28.6% | 1.03 (0–3) | 3.69 (0–18) | 0.53zł (0.0–2.7) | 6.39 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-05_COST_PLUS1` | 5.65 Er (1–9) | 3.4% | 29.2% | 1.04 (0–3) | 3.66 (0–15) | 0.43zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-05_COST_MINUS1` | 5.63 Er (1–9) | 3.2% | 28.6% | 1.03 (0–3) | 3.66 (0–18) | 0.71zł (0.0–3.0) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-05_HERESY_PLUS1` | 5.62 Er (1–9) | 3.7% | 28.7% | 1.03 (0–3) | 3.72 (0–18) | 0.53zł (0.0–2.7) | 6.39 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-06_COST_PLUS1` | 5.65 Er (1–9) | 3.4% | 29.4% | 1.03 (0–3) | 3.64 (0–16) | 0.44zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-06_COST_MINUS1` | 5.63 Er (1–9) | 3.2% | 28.6% | 1.03 (0–4) | 3.66 (0–18) | 0.74zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-06_HERESY_PLUS1` | 5.64 Er (1–9) | 4.6% | 28.7% | 1.03 (0–3) | 3.74 (0–18) | 0.53zł (0.0–2.7) | 6.42 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-07_COST_PLUS1` | 5.65 Er (1–9) | 3.4% | 29.1% | 1.03 (0–3) | 3.67 (0–15) | 0.43zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-07_COST_MINUS1` | 5.64 Er (1–9) | 3.3% | 28.6% | 1.03 (0–3) | 3.65 (0–18) | 0.71zł (0.0–3.0) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-07_HERESY_PLUS1` | 5.61 Er (1–9) | 3.6% | 28.7% | 1.03 (0–3) | 3.71 (0–18) | 0.53zł (0.0–2.7) | 6.40 (1.3–10.0) | 🟢 W NORMIE |
| `L3_KT-08_COST_PLUS1` | 5.65 Er (1–9) | 3.5% | 29.1% | 1.03 (0–4) | 3.65 (0–15) | 0.44zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-08_COST_MINUS1` | 5.64 Er (1–9) | 3.2% | 28.7% | 1.03 (0–4) | 3.65 (0–18) | 0.70zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-08_HERESY_PLUS1` | 5.61 Er (1–9) | 3.6% | 28.6% | 1.03 (0–3) | 3.70 (0–18) | 0.53zł (0.0–2.7) | 6.39 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-09_COST_PLUS1` | 5.64 Er (1–9) | 3.5% | 29.2% | 1.03 (0–3) | 3.64 (0–15) | 0.43zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-09_COST_MINUS1` | 5.63 Er (1–9) | 3.3% | 28.6% | 1.03 (0–3) | 3.65 (0–16) | 0.71zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-09_HERESY_PLUS1` | 5.63 Er (1–9) | 4.1% | 28.7% | 1.03 (0–3) | 3.74 (0–18) | 0.53zł (0.0–2.7) | 6.40 (1.3–10.0) | 🟢 W NORMIE |
| `L3_KT-09_HERESY_MINUS1` | 5.63 Er (1–9) | 2.9% | 28.7% | 1.04 (0–4) | 3.61 (0–15) | 0.53zł (0.0–2.7) | 6.11 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-10_COST_PLUS1` | 5.64 Er (1–9) | 3.5% | 29.1% | 1.03 (0–3) | 3.65 (0–15) | 0.43zł (0.0–2.3) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-10_COST_MINUS1` | 5.63 Er (1–9) | 3.3% | 28.6% | 1.03 (0–3) | 3.66 (0–18) | 0.71zł (0.0–3.0) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-10_HERESY_PLUS1` | 5.61 Er (1–9) | 4.2% | 28.6% | 1.03 (0–4) | 3.84 (0–17) | 0.54zł (0.0–2.7) | 6.51 (1.4–10.0) | 🟢 W NORMIE |
| `L3_SO-01_COST_PLUS1` | 5.61 Er (1–9) | 3.0% | 29.3% | 1.03 (0–3) | 3.63 (0–15) | 0.53zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-01_COST_MINUS1` | 5.59 Er (1–9) | 3.0% | 27.6% | 1.04 (0–4) | 3.64 (0–15) | 0.54zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-01_HERESY_PLUS1` | 5.55 Er (1–9) | 2.5% | 28.4% | 1.02 (0–3) | 3.68 (0–15) | 0.52zł (0.0–2.7) | 6.34 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-02_COST_PLUS1` | 5.66 Er (1–9) | 3.5% | 30.8% | 1.02 (0–3) | 3.61 (0–15) | 0.53zł (0.0–2.7) | 6.24 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-02_COST_MINUS1` | 5.59 Er (1–9) | 3.1% | 27.5% | 1.09 (0–4) | 3.67 (0–15) | 0.58zł (0.0–3.0) | 6.30 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-02_HERESY_PLUS1` | 5.51 Er (1–9) | 2.5% | 28.3% | 1.02 (0–3) | 3.69 (0–15) | 0.52zł (0.0–2.7) | 6.34 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-03_COST_PLUS1` | 5.64 Er (1–9) | 3.4% | 29.4% | 1.03 (0–4) | 3.58 (0–15) | 0.53zł (0.0–2.3) | 6.20 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-03_COST_MINUS1` | 5.59 Er (1–9) | 2.9% | 27.5% | 1.05 (0–3) | 3.67 (0–15) | 0.53zł (0.0–3.0) | 6.27 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-03_HERESY_PLUS1` | 5.50 Er (1–9) | 2.5% | 28.3% | 1.02 (0–3) | 3.68 (0–15) | 0.52zł (0.0–2.7) | 6.35 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-04_COST_PLUS1` | 5.61 Er (1–9) | 3.2% | 29.4% | 1.02 (0–3) | 3.65 (0–15) | 0.53zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-04_COST_MINUS1` | 5.60 Er (1–9) | 3.1% | 27.5% | 1.06 (0–3) | 3.68 (0–15) | 0.55zł (0.0–2.7) | 6.29 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-04_HERESY_PLUS1` | 5.50 Er (1–9) | 2.4% | 28.3% | 1.02 (0–3) | 3.71 (0–15) | 0.52zł (0.0–2.7) | 6.35 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-05_COST_PLUS1` | 5.62 Er (1–9) | 3.1% | 28.7% | 1.03 (0–3) | 3.64 (0–15) | 0.53zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-05_HERESY_PLUS1` | 5.62 Er (1–9) | 3.1% | 28.7% | 1.03 (0–3) | 3.64 (0–15) | 0.53zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-06_COST_PLUS1` | 5.61 Er (1–9) | 2.9% | 28.6% | 1.05 (0–3) | 3.64 (0–15) | 0.54zł (0.0–2.7) | 6.27 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-06_COST_MINUS1` | 5.61 Er (1–9) | 3.2% | 27.8% | 1.04 (0–3) | 3.63 (0–15) | 0.51zł (0.0–3.0) | 6.24 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-06_HERESY_PLUS1` | 5.61 Er (1–9) | 2.9% | 28.6% | 1.03 (0–3) | 3.65 (0–15) | 0.53zł (0.0–2.7) | 6.29 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-07_COST_PLUS1` | 5.61 Er (1–9) | 3.0% | 28.7% | 1.05 (0–3) | 3.66 (0–15) | 0.54zł (0.0–2.3) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-07_COST_MINUS1` | 5.59 Er (1–9) | 3.1% | 27.7% | 1.05 (0–3) | 3.63 (0–15) | 0.51zł (0.0–3.0) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-07_HERESY_PLUS1` | 5.57 Er (1–9) | 2.7% | 28.5% | 1.03 (0–3) | 3.66 (0–15) | 0.52zł (0.0–2.7) | 6.32 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-08_COST_PLUS1` | 5.66 Er (1–9) | 3.5% | 29.0% | 1.04 (0–3) | 3.62 (0–15) | 0.53zł (0.0–3.0) | 6.21 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-08_COST_MINUS1` | 5.55 Er (1–9) | 2.9% | 27.4% | 1.04 (0–4) | 3.64 (0–15) | 0.50zł (0.0–3.0) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-08_HERESY_PLUS1` | 5.53 Er (1–9) | 2.5% | 28.4% | 1.02 (0–3) | 3.70 (0–15) | 0.52zł (0.0–2.7) | 6.33 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-08_HERESY_MINUS1` | 5.67 Er (1–9) | 3.6% | 28.8% | 1.04 (0–3) | 3.58 (0–15) | 0.53zł (0.0–2.7) | 6.13 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-09_COST_PLUS1` | 5.62 Er (1–9) | 2.9% | 28.7% | 1.05 (0–3) | 3.64 (0–15) | 0.53zł (0.0–2.7) | 6.26 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-09_COST_MINUS1` | 5.61 Er (1–9) | 3.0% | 27.7% | 1.05 (0–3) | 3.64 (0–15) | 0.51zł (0.0–3.0) | 6.27 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-09_HERESY_PLUS1` | 5.56 Er (1–9) | 2.5% | 28.5% | 1.03 (0–3) | 3.67 (0–15) | 0.52zł (0.0–2.7) | 6.34 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-10_COST_PLUS1` | 5.79 Er (1–9) | 3.8% | 28.0% | 0.76 (0–3) | 3.46 (0–15) | 0.53zł (0.0–2.7) | 6.14 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-10_COST_MINUS1` | 5.59 Er (1–9) | 3.0% | 28.1% | 1.04 (0–3) | 3.66 (0–15) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-10_HERESY_PLUS1` | 5.51 Er (1–9) | 2.7% | 28.4% | 1.02 (0–3) | 3.68 (0–15) | 0.52zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-10_HERESY_MINUS1` | 5.73 Er (1–9) | 3.5% | 29.0% | 1.05 (0–4) | 3.57 (0–15) | 0.53zł (0.0–2.7) | 6.22 (1.2–10.0) | 🟢 W NORMIE |