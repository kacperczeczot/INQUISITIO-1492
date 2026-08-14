# Raport Precyzyjnego Audytu Poziomu 3 (Parametry Pojedynczych Kart) — Wersja Balansu: v0.13

**Wersja Balansu:** `v0.13` | **Data:** 2026-08-14 11:46 | **Przeanalizowano Wariantów Kart:** 161 | **Próba:** 300 gier/setup | **Czas:** 86.85s
**Filtry:** Parametry: `cost,heresy` | Frakcja: `all` | Karta: `Wszystkie`
**Wynik Bazy Poziomu 3 (Global):** `🟢 77.0 pkt` | 3p: `87.9 pkt` | 4p: `63.6 pkt` | 5p: `79.5 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | Baza (Bieżące parametry wszystkich kart) | 🟢 ** 77.0** | 87.9 | 63.6 | 79.5 | ⚪ OPTYMALNY |
| `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 1 → 2 | 77.0 → 🟢 ** 75.9** (`-1.1`) | 87.9 → 83.9 (`-4.0`) | 63.6 → 59.2 (`-4.4`) | 79.5 → 84.7 (`⬆️ +5.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-01_COST_MINUS1` | CAA-01 (Przejście Podziemiami): cost 1 → 0 | 77.0 → 🟢 ** 77.9** (`⬆️ +0.9`) | 87.9 → 79.5 (`-8.4`) | 63.6 → 70.4 (`⬆️ +6.8`) | 79.5 → 83.7 (`⬆️ +4.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-01_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 77.0 → 🟢 ** 73.0** (`-4.0`) | 87.9 → 84.8 (`-3.1`) | 63.6 → 59.5 (`-4.1`) | 79.5 → 74.6 (`-4.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 1 → 2 | 77.0 → 🟢 ** 80.2** (`⬆️ +3.2`) | 87.9 → 83.2 (`-4.7`) | 63.6 → 60.4 (`-3.2`) | 79.5 → 97.0 (`⬆️ +17.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-02_COST_MINUS1` | CAA-02 (Złoto z Kryjówki): cost 1 → 0 | 77.0 → 🟢 ** 75.3** (`-1.7`) | 87.9 → 86.6 (`-1.3`) | 63.6 → 71.3 (`⬆️ +7.7`) | 79.5 → 68.1 (`-11.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_HERESY_PLUS1` | CAA-02 (Złoto z Kryjówki): heresy 0 → 1 | 77.0 → 🟢 ** 83.8** (`⬆️ +6.8`) | 87.9 → 84.6 (`-3.3`) | 63.6 → 68.7 (`⬆️ +5.1`) | 79.5 → 98.2 (`⬆️ +18.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-03_COST_PLUS1` | CAA-03 (Cień na Rynku): cost 1 → 2 | 77.0 → 🟢 ** 72.3** (`-4.7`) | 87.9 → 81.0 (`-6.9`) | 63.6 → 62.9 (`-0.7`) | 79.5 → 73.1 (`-6.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_COST_MINUS1` | CAA-03 (Cień na Rynku): cost 1 → 0 | 77.0 → 🟢 ** 72.7** (`-4.3`) | 87.9 → 78.5 (`-9.4`) | 63.6 → 65.8 (`⬆️ +2.2`) | 79.5 → 73.9 (`-5.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-03_HERESY_PLUS1` | CAA-03 (Cień na Rynku): heresy 1 → 2 | 77.0 → 🟢 ** 85.1** (`⬆️ +8.1`) | 87.9 → 90.3 (`⬆️ +2.4`) | 63.6 → 67.3 (`⬆️ +3.7`) | 79.5 → 97.8 (`⬆️ +18.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 77.0 → 🟢 ** 74.7** (`-2.3`) | 87.9 → 84.0 (`-3.9`) | 63.6 → 54.2 (`-9.4`) | 79.5 → 85.8 (`⬆️ +6.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-04_COST_PLUS1` | CAA-04 (Fałszywy Trop): cost 1 → 2 | 77.0 → 🟢 ** 80.1** (`⬆️ +3.1`) | 87.9 → 87.8 (`-0.1`) | 63.6 → 55.4 (`-8.2`) | 79.5 → 97.2 (`⬆️ +17.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-04_COST_MINUS1` | CAA-04 (Fałszywy Trop): cost 1 → 0 | 77.0 → 🟢 ** 80.2** (`⬆️ +3.2`) | 87.9 → 79.6 (`-8.3`) | 63.6 → 63.4 (`-0.2`) | 79.5 → 97.6 (`⬆️ +18.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-04_HERESY_PLUS1` | CAA-04 (Fałszywy Trop): heresy 0 → 1 | 77.0 → 🟢 ** 73.1** (`-3.9`) | 87.9 → 85.6 (`-2.3`) | 63.6 → 65.4 (`⬆️ +1.8`) | 79.5 → 68.3 (`-11.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_COST_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 2 | 77.0 → 🟢 ** 64.5** (`-12.5`) | 87.9 → 82.7 (`-5.2`) | 63.6 → 43.7 (`-19.9`) | 79.5 → 67.0 (`-12.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_COST_MINUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 | 77.0 → 🟢 ** 80.2** (`⬆️ +3.2`) | 87.9 → 79.4 (`-8.5`) | 63.6 → 63.1 (`-0.5`) | 79.5 → 98.1 (`⬆️ +18.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-05_HERESY_PLUS1` | CAA-05 (Ukryty Kurier): heresy 0 → 1 | 77.0 → 🟢 ** 73.8** (`-3.2`) | 87.9 → 87.2 (`-0.7`) | 63.6 → 52.4 (`-11.2`) | 79.5 → 81.9 (`⬆️ +2.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_COST_PLUS1` | CAA-06 (Ucieczka z Lochów): cost 2 → 3 | 77.0 → 🟢 ** 59.1** (`-17.9`) | 87.9 → 86.2 (`-1.7`) | 63.6 → 42.7 (`-20.9`) | 79.5 → 48.4 (`-31.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_COST_MINUS1` | CAA-06 (Ucieczka z Lochów): cost 2 → 1 | 77.0 → 🟢 ** 76.7** (`-0.3`) | 87.9 → 81.9 (`-6.0`) | 63.6 → 63.0 (`-0.6`) | 79.5 → 85.2 (`⬆️ +5.7`) | ⚪ OPTYMALNY |
| `L3_CAA-06_HERESY_PLUS1` | CAA-06 (Ucieczka z Lochów): heresy 0 → 1 | 77.0 → 🟢 ** 73.3** (`-3.7`) | 87.9 → 87.2 (`-0.7`) | 63.6 → 61.8 (`-1.8`) | 79.5 → 70.9 (`-8.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 2 → 3 | 77.0 → 🟢 ** 75.7** (`-1.3`) | 87.9 → 87.4 (`-0.5`) | 63.6 → 55.9 (`-7.7`) | 79.5 → 83.9 (`⬆️ +4.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_COST_MINUS1` | CAA-07 (Szantaż Bractwa): cost 2 → 1 | 77.0 → 🟢 ** 77.5** (`⬆️ +0.5`) | 87.9 → 75.2 (`-12.7`) | 63.6 → 71.5 (`⬆️ +7.9`) | 79.5 → 85.7 (`⬆️ +6.2`) | ⚪ OPTYMALNY |
| `L3_CAA-07_HERESY_PLUS1` | CAA-07 (Szantaż Bractwa): heresy 0 → 1 | 77.0 → 🟢 ** 82.8** (`⬆️ +5.8`) | 87.9 → 86.7 (`-1.2`) | 63.6 → 62.9 (`-0.7`) | 79.5 → 98.7 (`⬆️ +19.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-08_COST_PLUS1` | CAA-08 (Kaptur Nocy): cost 1 → 2 | 77.0 → 🟢 ** 79.7** (`⬆️ +2.7`) | 87.9 → 85.2 (`-2.7`) | 63.6 → 55.7 (`-7.9`) | 79.5 → 98.3 (`⬆️ +18.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-08_COST_MINUS1` | CAA-08 (Kaptur Nocy): cost 1 → 0 | 77.0 → 🟢 ** 76.5** (`-0.5`) | 87.9 → 86.6 (`-1.3`) | 63.6 → 58.2 (`-5.4`) | 79.5 → 84.6 (`⬆️ +5.1`) | ⚪ OPTYMALNY |
| `L3_CAA-08_HERESY_PLUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 2 | 77.0 → 🟢 ** 76.3** (`-0.7`) | 87.9 → 87.5 (`-0.4`) | 63.6 → 58.5 (`-5.1`) | 79.5 → 82.8 (`⬆️ +3.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-08_HERESY_MINUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 0 | 77.0 → 🟢 ** 75.8** (`-1.2`) | 87.9 → 85.8 (`-2.1`) | 63.6 → 58.3 (`-5.3`) | 79.5 → 83.4 (`⬆️ +3.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_COST_PLUS1` | CAA-09 (Kurier Relikwii): cost 2 → 3 | 77.0 → 🟢 ** 69.6** (`-7.4`) | 87.9 → 83.3 (`-4.6`) | 63.6 → 54.6 (`-9.0`) | 79.5 → 70.8 (`-8.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_COST_MINUS1` | CAA-09 (Kurier Relikwii): cost 2 → 1 | 77.0 → 🟢 ** 73.3** (`-3.7`) | 87.9 → 76.7 (`-11.2`) | 63.6 → 73.7 (`⬆️ +10.1`) | 79.5 → 69.4 (`-10.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_HERESY_PLUS1` | CAA-09 (Kurier Relikwii): heresy 0 → 1 | 77.0 → 🟢 ** 71.7** (`-5.3`) | 87.9 → 73.4 (`-14.5`) | 63.6 → 58.1 (`-5.5`) | 79.5 → 83.5 (`⬆️ +4.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_COST_PLUS1` | CAA-10 (Echo Alhambry): cost 1 → 2 | 77.0 → 🟢 ** 51.6** (`-25.4`) | 87.9 → 58.2 (`-29.7`) | 63.6 → 42.8 (`-20.8`) | 79.5 → 53.9 (`-25.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_COST_MINUS1` | CAA-10 (Echo Alhambry): cost 1 → 0 | 77.0 → 🟢 ** 76.9** (`-0.1`) | 87.9 → 80.0 (`-7.9`) | 63.6 → 68.3 (`⬆️ +4.7`) | 79.5 → 82.3 (`⬆️ +2.8`) | ⚪ OPTYMALNY |
| `L3_CAA-10_HERESY_PLUS1` | CAA-10 (Echo Alhambry): heresy 1 → 2 | 77.0 → 🟢 ** 64.1** (`-12.9`) | 87.9 → 76.0 (`-11.9`) | 63.6 → 48.9 (`-14.7`) | 79.5 → 67.5 (`-12.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_HERESY_MINUS1` | CAA-10 (Echo Alhambry): heresy 1 → 0 | 77.0 → 🟢 ** 74.8** (`-2.2`) | 87.9 → 83.4 (`-4.5`) | 63.6 → 55.5 (`-8.1`) | 79.5 → 85.5 (`⬆️ +6.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_COST_PLUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 2 | 77.0 → 🟢 ** 70.5** (`-6.5`) | 87.9 → 85.7 (`-2.2`) | 63.6 → 67.1 (`⬆️ +3.5`) | 79.5 → 58.7 (`-20.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_COST_MINUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 0 | 77.0 → 🟢 ** 51.8** (`-25.2`) | 87.9 → 75.7 (`-12.2`) | 63.6 → 19.6 (`-44.0`) | 79.5 → 60.2 (`-19.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): heresy 0 → 1 | 77.0 → 🟢 ** 74.6** (`-2.4`) | 87.9 → 85.7 (`-2.2`) | 63.6 → 54.3 (`-9.3`) | 79.5 → 83.7 (`⬆️ +4.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_COST_PLUS1` | GC-02 (Czarny Rynek): cost 1 → 2 | 77.0 → 🟢 ** 84.9** (`⬆️ +7.9`) | 87.9 → 83.9 (`-4.0`) | 63.6 → 71.7 (`⬆️ +8.1`) | 79.5 → 99.2 (`⬆️ +19.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-02_COST_MINUS1` | GC-02 (Czarny Rynek): cost 1 → 0 | 77.0 → 🟢 ** 56.7** (`-20.3`) | 87.9 → 84.0 (`-3.9`) | 63.6 → 30.2 (`-33.4`) | 79.5 → 55.8 (`-23.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_HERESY_PLUS1` | GC-02 (Czarny Rynek): heresy 0 → 1 | 77.0 → 🟢 ** 63.5** (`-13.5`) | 87.9 → 84.7 (`-3.2`) | 63.6 → 39.9 (`-23.7`) | 79.5 → 65.9 (`-13.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-03_COST_PLUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 2 | 77.0 → 🟢 ** 84.4** (`⬆️ +7.4`) | 87.9 → 87.4 (`-0.5`) | 63.6 → 66.6 (`⬆️ +3.0`) | 79.5 → 99.2 (`⬆️ +19.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-03_COST_MINUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 0 | 77.0 → 🟢 ** 53.3** (`-23.7`) | 87.9 → 83.4 (`-4.5`) | 63.6 → 28.8 (`-34.8`) | 79.5 → 47.6 (`-31.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-03_HERESY_PLUS1` | GC-03 (Podrzucenie Księgi): heresy 0 → 1 | 77.0 → 🟢 ** 74.1** (`-2.9`) | 87.9 → 85.7 (`-2.2`) | 63.6 → 61.1 (`-2.5`) | 79.5 → 75.5 (`-4.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_COST_PLUS1` | GC-04 (Informator): cost 1 → 2 | 77.0 → 🟢 ** 83.6** (`⬆️ +6.6`) | 87.9 → 86.7 (`-1.2`) | 63.6 → 66.3 (`⬆️ +2.7`) | 79.5 → 97.9 (`⬆️ +18.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-04_COST_MINUS1` | GC-04 (Informator): cost 1 → 0 | 77.0 → 🟢 ** 68.5** (`-8.5`) | 87.9 → 74.4 (`-13.5`) | 63.6 → 34.9 (`-28.7`) | 79.5 → 96.3 (`⬆️ +16.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_HERESY_PLUS1` | GC-04 (Informator): heresy 1 → 2 | 77.0 → 🟢 ** 78.8** (`⬆️ +1.8`) | 87.9 → 84.5 (`-3.4`) | 63.6 → 53.9 (`-9.7`) | 79.5 → 98.0 (`⬆️ +18.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-04_HERESY_MINUS1` | GC-04 (Informator): heresy 1 → 0 | 🟢 ** 77.0** | 87.9 → 83.0 (`-4.9`) | 63.6 → 52.0 (`-11.6`) | 79.5 → 96.1 (`⬆️ +16.6`) | ⚪ OPTYMALNY |
| `L3_GC-05_COST_PLUS1` | GC-05 (Fałszywy Świadek): cost 0 → 1 | 🟢 ** 77.0** | 87.9 | 63.6 | 79.5 | ⚪ OPTYMALNY |
| `L3_GC-05_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): heresy 0 → 1 | 🟢 ** 77.0** | 87.9 | 63.6 | 79.5 | ⚪ OPTYMALNY |
| `L3_GC-06_COST_PLUS1` | GC-06 (Szantaż): cost 2 → 3 | 77.0 → 🟢 ** 82.1** (`⬆️ +5.1`) | 87.9 → 82.4 (`-5.5`) | 63.6 → 68.4 (`⬆️ +4.8`) | 79.5 → 95.4 (`⬆️ +15.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-06_COST_MINUS1` | GC-06 (Szantaż): cost 2 → 1 | 77.0 → 🟡 ** 48.2** (`-28.8`) | 87.9 → 81.1 (`-6.8`) | 63.6 → 33.2 (`-30.4`) | 79.5 → 30.4 (`-49.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_HERESY_PLUS1` | GC-06 (Szantaż): heresy 0 → 1 | 77.0 → 🟢 ** 71.5** (`-5.5`) | 87.9 → 84.7 (`-3.2`) | 63.6 → 54.3 (`-9.3`) | 79.5 → 75.6 (`-3.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_COST_PLUS1` | GC-07 (Skrytobójstwo): cost 2 → 3 | 77.0 → 🟢 ** 73.1** (`-3.9`) | 87.9 → 89.5 (`⬆️ +1.6`) | 63.6 → 50.5 (`-13.1`) | 79.5 → 79.4 (`-0.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_COST_MINUS1` | GC-07 (Skrytobójstwo): cost 2 → 1 | 77.0 → 🟢 ** 62.6** (`-14.4`) | 87.9 → 72.7 (`-15.2`) | 63.6 → 31.1 (`-32.5`) | 79.5 → 84.1 (`⬆️ +4.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_HERESY_PLUS1` | GC-07 (Skrytobójstwo): heresy 1 → 2 | 77.0 → 🟢 ** 74.0** (`-3.0`) | 87.9 → 87.7 (`-0.2`) | 63.6 → 51.3 (`-12.3`) | 79.5 → 83.1 (`⬆️ +3.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_HERESY_MINUS1` | GC-07 (Skrytobójstwo): heresy 1 → 0 | 77.0 → 🟢 ** 75.7** (`-1.3`) | 87.9 → 86.3 (`-1.6`) | 63.6 → 61.4 (`-2.2`) | 79.5 | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 1 → 2 | 77.0 → 🟢 ** 79.7** (`⬆️ +2.7`) | 87.9 → 86.0 (`-1.9`) | 63.6 → 55.0 (`-8.6`) | 79.5 → 98.0 (`⬆️ +18.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-08_COST_MINUS1` | GC-08 (Zatrute Złoto): cost 1 → 0 | 77.0 → 🟢 ** 56.5** (`-20.5`) | 87.9 → 86.3 (`-1.6`) | 63.6 → 32.7 (`-30.9`) | 79.5 → 50.4 (`-29.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 0 → 1 | 77.0 → 🟢 ** 76.9** (`-0.1`) | 87.9 → 85.5 (`-2.4`) | 63.6 → 58.8 (`-4.8`) | 79.5 → 86.5 (`⬆️ +7.0`) | ⚪ OPTYMALNY |
| `L3_GC-09_COST_PLUS1` | GC-09 (Lista Dłużników): cost 2 → 3 | 77.0 → 🟢 ** 73.5** (`-3.5`) | 87.9 → 86.6 (`-1.3`) | 63.6 → 64.1 (`⬆️ +0.5`) | 79.5 → 69.7 (`-9.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_COST_MINUS1` | GC-09 (Lista Dłużników): cost 2 → 1 | 77.0 → 🟢 ** 56.3** (`-20.7`) | 87.9 → 88.5 (`⬆️ +0.6`) | 63.6 → 32.6 (`-31.0`) | 79.5 → 47.9 (`-31.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_HERESY_PLUS1` | GC-09 (Lista Dłużników): heresy 0 → 1 | 77.0 → 🟢 ** 69.4** (`-7.6`) | 87.9 → 85.4 (`-2.5`) | 63.6 → 63.2 (`-0.4`) | 79.5 → 59.7 (`-19.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_COST_PLUS1` | GC-10 (Upadek Domu): cost 3 → 4 | 77.0 → 🟢 ** 70.0** (`-7.0`) | 87.9 → 87.0 (`-0.9`) | 63.6 → 72.4 (`⬆️ +8.8`) | 79.5 → 50.6 (`-28.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_COST_MINUS1` | GC-10 (Upadek Domu): cost 3 → 2 | 77.0 → 🟢 ** 62.6** (`-14.4`) | 87.9 → 86.8 (`-1.1`) | 63.6 → 30.8 (`-32.8`) | 79.5 → 70.2 (`-9.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-10_HERESY_PLUS1` | GC-10 (Upadek Domu): heresy 2 → 3 | 77.0 → 🟢 ** 76.6** (`-0.4`) | 87.9 → 70.3 (`-17.6`) | 63.6 → 77.3 (`⬆️ +13.7`) | 79.5 → 82.2 (`⬆️ +2.7`) | ⚪ OPTYMALNY |
| `L3_GC-10_HERESY_MINUS1` | GC-10 (Upadek Domu): heresy 2 → 1 | 77.0 → 🟢 ** 63.8** (`-13.2`) | 87.9 → 76.0 (`-11.9`) | 63.6 → 34.7 (`-28.9`) | 79.5 → 80.8 (`⬆️ +1.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_COST_PLUS1` | KB-01 (Rozkaz Dworu): cost 1 → 2 | 77.0 → 🟢 ** 83.9** (`⬆️ +6.9`) | 87.9 → 83.3 (`-4.6`) | 63.6 → 70.6 (`⬆️ +7.0`) | 79.5 → 97.8 (`⬆️ +18.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-01_COST_MINUS1` | KB-01 (Rozkaz Dworu): cost 1 → 0 | 77.0 → 🟢 ** 83.2** (`⬆️ +6.2`) | 87.9 → 85.0 (`-2.9`) | 63.6 → 66.3 (`⬆️ +2.7`) | 79.5 → 98.2 (`⬆️ +18.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-01_HERESY_PLUS1` | KB-01 (Rozkaz Dworu): heresy 0 → 1 | 77.0 → 🟢 ** 70.1** (`-6.9`) | 87.9 → 77.8 (`-10.1`) | 63.6 → 60.2 (`-3.4`) | 79.5 → 72.4 (`-7.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_COST_PLUS1` | KB-02 (Pobór Podatków): cost 1 → 2 | 77.0 → 🟡 ** 48.2** (`-28.8`) | 87.9 → 76.7 (`-11.2`) | 63.6 → 19.8 (`-43.8`) | 79.5 → 0.0 (`-79.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_COST_MINUS1` | KB-02 (Pobór Podatków): cost 1 → 0 | 77.0 → 🟢 ** 63.7** (`-13.3`) | 87.9 → 82.4 (`-5.5`) | 63.6 → 64.4 (`⬆️ +0.8`) | 79.5 → 44.3 (`-35.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_HERESY_PLUS1` | KB-02 (Pobór Podatków): heresy 0 → 1 | 77.0 → 🟢 ** 56.2** (`-20.8`) | 87.9 → 74.2 (`-13.7`) | 63.6 → 34.3 (`-29.3`) | 79.5 → 60.2 (`-19.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_COST_PLUS1` | KB-03 (Plotka Dworska): cost 1 → 2 | 77.0 → 🟢 ** 76.0** (`-1.0`) | 87.9 → 79.2 (`-8.7`) | 63.6 → 50.5 (`-13.1`) | 79.5 → 98.4 (`⬆️ +18.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-03_COST_MINUS1` | KB-03 (Plotka Dworska): cost 1 → 0 | 🟢 ** 77.0** | 87.9 → 77.2 (`-10.7`) | 63.6 → 54.8 (`-8.8`) | 79.5 → 99.1 (`⬆️ +19.6`) | ⚪ OPTYMALNY |
| `L3_KB-03_HERESY_PLUS1` | KB-03 (Plotka Dworska): heresy 0 → 1 | 77.0 → 🟢 ** 56.1** (`-20.9`) | 87.9 → 72.8 (`-15.1`) | 63.6 → 35.4 (`-28.2`) | 79.5 → 60.0 (`-19.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_COST_PLUS1` | KB-04 (Faworyt Dworu): cost 1 → 2 | 77.0 → 🟢 ** 78.7** (`⬆️ +1.7`) | 87.9 → 90.9 (`⬆️ +3.0`) | 63.6 → 71.7 (`⬆️ +8.1`) | 79.5 → 73.4 (`-6.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-04_COST_MINUS1` | KB-04 (Faworyt Dworu): cost 1 → 0 | 77.0 → 🟢 ** 63.5** (`-13.5`) | 87.9 → 83.5 (`-4.4`) | 63.6 → 39.1 (`-24.5`) | 79.5 → 67.9 (`-11.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_HERESY_PLUS1` | KB-04 (Faworyt Dworu): heresy 1 → 2 | 77.0 → 🟡 ** 43.9** (`-33.1`) | 87.9 → 69.9 (`-18.0`) | 63.6 → 59.6 (`-4.0`) | 79.5 → 2.3 (`-77.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_HERESY_MINUS1` | KB-04 (Faworyt Dworu): heresy 1 → 0 | 77.0 → 🟢 ** 84.4** (`⬆️ +7.4`) | 87.9 → 91.5 (`⬆️ +3.6`) | 63.6 → 65.0 (`⬆️ +1.4`) | 79.5 → 96.8 (`⬆️ +17.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-05_COST_PLUS1` | KB-05 (List Żelazny): cost 2 → 3 | 77.0 → 🟢 ** 66.7** (`-10.3`) | 87.9 → 86.5 (`-1.4`) | 63.6 → 52.9 (`-10.7`) | 79.5 → 60.7 (`-18.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_COST_MINUS1` | KB-05 (List Żelazny): cost 2 → 1 | 77.0 → 🟢 ** 65.4** (`-11.6`) | 87.9 → 72.8 (`-15.1`) | 63.6 → 36.1 (`-27.5`) | 79.5 → 87.2 (`⬆️ +7.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_HERESY_PLUS1` | KB-05 (List Żelazny): heresy 0 → 1 | 77.0 → 🟢 ** 70.1** (`-6.9`) | 87.9 → 83.0 (`-4.9`) | 63.6 → 50.5 (`-13.1`) | 79.5 → 76.8 (`-2.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_COST_PLUS1` | KB-06 (Areszt Królewski): cost 2 → 3 | 77.0 → 🟢 ** 79.5** (`⬆️ +2.5`) | 87.9 → 88.9 (`⬆️ +1.0`) | 63.6 → 66.1 (`⬆️ +2.5`) | 79.5 → 83.4 (`⬆️ +3.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-06_COST_MINUS1` | KB-06 (Areszt Królewski): cost 2 → 1 | 77.0 → 🟢 ** 60.9** (`-16.1`) | 87.9 → 89.4 (`⬆️ +1.5`) | 63.6 → 45.4 (`-18.2`) | 79.5 → 48.0 (`-31.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_HERESY_PLUS1` | KB-06 (Areszt Królewski): heresy 0 → 1 | 77.0 → 🟢 ** 70.6** (`-6.4`) | 87.9 → 87.1 (`-0.8`) | 63.6 → 44.9 (`-18.7`) | 79.5 → 79.7 (`⬆️ +0.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_COST_PLUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 3 | 77.0 → 🟢 ** 77.2** (`⬆️ +0.2`) | 87.9 → 91.4 (`⬆️ +3.5`) | 63.6 → 54.0 (`-9.6`) | 79.5 → 86.1 (`⬆️ +6.6`) | ⚪ OPTYMALNY |
| `L3_KB-07_COST_MINUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 1 | 77.0 → 🟢 ** 76.7** (`-0.3`) | 87.9 → 85.5 (`-2.4`) | 63.6 → 66.4 (`⬆️ +2.8`) | 79.5 → 78.3 (`-1.2`) | ⚪ OPTYMALNY |
| `L3_KB-07_HERESY_PLUS1` | KB-07 (Szantaż Pieczęcią): heresy 0 → 1 | 77.0 → 🟢 ** 66.9** (`-10.1`) | 87.9 → 77.9 (`-10.0`) | 63.6 → 46.2 (`-17.4`) | 79.5 → 76.6 (`-2.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_COST_PLUS1` | KB-08 (Przekupstwo Sędziego): cost 3 → 4 | 77.0 → 🟢 ** 67.1** (`-9.9`) | 87.9 → 90.9 (`⬆️ +3.0`) | 63.6 → 70.0 (`⬆️ +6.4`) | 79.5 → 40.3 (`-39.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_COST_MINUS1` | KB-08 (Przekupstwo Sędziego): cost 3 → 2 | 77.0 → 🟢 ** 78.9** (`⬆️ +1.9`) | 87.9 → 88.5 (`⬆️ +0.6`) | 63.6 → 63.5 (`-0.1`) | 79.5 → 84.8 (`⬆️ +5.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-08_HERESY_PLUS1` | KB-08 (Przekupstwo Sędziego): heresy 0 → 1 | 77.0 → 🟢 ** 75.2** (`-1.8`) | 87.9 → 88.2 (`⬆️ +0.3`) | 63.6 → 59.6 (`-4.0`) | 79.5 → 77.7 (`-1.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_COST_PLUS1` | KB-09 (Dekret Królewski): cost 3 → 4 | 77.0 → 🔴 ** 20.1** (`-56.9`) | 87.9 → 37.2 (`-50.7`) | 63.6 → 2.9 (`-60.7`) | 79.5 → 0.0 (`-79.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_COST_MINUS1` | KB-09 (Dekret Królewski): cost 3 → 2 | 77.0 → 🟢 ** 76.7** (`-0.3`) | 87.9 → 81.6 (`-6.3`) | 63.6 → 51.4 (`-12.2`) | 79.5 → 97.2 (`⬆️ +17.7`) | ⚪ OPTYMALNY |
| `L3_KB-09_HERESY_PLUS1` | KB-09 (Dekret Królewski): heresy 1 → 2 | 77.0 → 🟢 ** 62.3** (`-14.7`) | 87.9 → 78.2 (`-9.7`) | 63.6 → 32.5 (`-31.1`) | 79.5 → 76.1 (`-3.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_HERESY_MINUS1` | KB-09 (Dekret Królewski): heresy 1 → 0 | 77.0 → 🟢 ** 84.9** (`⬆️ +7.9`) | 87.9 → 88.7 (`⬆️ +0.8`) | 63.6 → 67.3 (`⬆️ +3.7`) | 79.5 → 98.6 (`⬆️ +19.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-10_COST_PLUS1` | KB-10 (Pieczęć Korony): cost 2 → 3 | 77.0 → 🔴 ** 19.8** (`-57.2`) | 87.9 → 36.8 (`-51.1`) | 63.6 → 2.9 (`-60.7`) | 79.5 → 0.0 (`-79.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_COST_MINUS1` | KB-10 (Pieczęć Korony): cost 2 → 1 | 77.0 → 🟢 ** 56.7** (`-20.3`) | 87.9 → 63.2 (`-24.7`) | 63.6 → 35.4 (`-28.2`) | 79.5 → 71.6 (`-7.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_HERESY_PLUS1` | KB-10 (Pieczęć Korony): heresy 2 → 3 | 77.0 → 🟡 ** 29.8** (`-47.2`) | 87.9 → 44.0 (`-43.9`) | 63.6 → 15.4 (`-48.2`) | 79.5 → 29.9 (`-49.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_HERESY_MINUS1` | KB-10 (Pieczęć Korony): heresy 2 → 1 | 77.0 → 🟢 ** 82.2** (`⬆️ +5.2`) | 87.9 → 88.4 (`⬆️ +0.5`) | 63.6 → 61.1 (`-2.5`) | 79.5 → 97.2 (`⬆️ +17.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 77.0 → 🟢 ** 82.4** (`⬆️ +5.4`) | 87.9 → 89.2 (`⬆️ +1.3`) | 63.6 → 60.4 (`-3.2`) | 79.5 → 97.6 (`⬆️ +18.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-01_COST_MINUS1` | KT-01 (Rytuał Przejścia): cost 1 → 0 | 77.0 → 🟢 ** 72.0** (`-5.0`) | 87.9 → 86.2 (`-1.7`) | 63.6 → 48.6 (`-15.0`) | 79.5 → 81.2 (`⬆️ +1.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_HERESY_PLUS1` | KT-01 (Rytuał Przejścia): heresy 0 → 1 | 77.0 → 🟢 ** 74.7** (`-2.3`) | 87.9 → 89.1 (`⬆️ +1.2`) | 63.6 → 64.7 (`⬆️ +1.1`) | 79.5 → 70.3 (`-9.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 77.0 → 🟢 ** 78.7** (`⬆️ +1.7`) | 87.9 → 90.1 (`⬆️ +2.2`) | 63.6 → 70.9 (`⬆️ +7.3`) | 79.5 → 75.0 (`-4.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-02_COST_MINUS1` | KT-02 (Transmutacja Złota): cost 1 → 0 | 77.0 → 🟢 ** 78.4** (`⬆️ +1.4`) | 87.9 → 87.8 (`-0.1`) | 63.6 → 63.2 (`-0.4`) | 79.5 → 84.3 (`⬆️ +4.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-02_HERESY_PLUS1` | KT-02 (Transmutacja Złota): heresy 0 → 1 | 77.0 → 🟢 ** 74.2** (`-2.8`) | 87.9 → 89.4 (`⬆️ +1.5`) | 63.6 → 63.5 (`-0.1`) | 79.5 → 69.8 (`-9.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_COST_PLUS1` | KT-03 (Zakazana Wiedza): cost 0 → 1 | 77.0 → 🟢 ** 78.6** (`⬆️ +1.6`) | 87.9 → 90.7 (`⬆️ +2.8`) | 63.6 → 60.5 (`-3.1`) | 79.5 → 84.7 (`⬆️ +5.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-03_HERESY_PLUS1` | KT-03 (Zakazana Wiedza): heresy 1 → 2 | 77.0 → 🟢 ** 75.3** (`-1.7`) | 87.9 → 88.2 (`⬆️ +0.3`) | 63.6 → 68.9 (`⬆️ +5.3`) | 79.5 → 68.8 (`-10.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-03_HERESY_MINUS1` | KT-03 (Zakazana Wiedza): heresy 1 → 0 | 77.0 → 🟢 ** 79.9** (`⬆️ +2.9`) | 87.9 → 86.2 (`-1.7`) | 63.6 → 69.9 (`⬆️ +6.3`) | 79.5 → 83.6 (`⬆️ +4.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-04_COST_PLUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 2 | 77.0 → 🟢 ** 70.3** (`-6.7`) | 87.9 → 89.3 (`⬆️ +1.4`) | 63.6 → 44.6 (`-19.0`) | 79.5 → 77.1 (`-2.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-04_COST_MINUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 0 | 77.0 → 🟢 ** 64.9** (`-12.1`) | 87.9 → 89.5 (`⬆️ +1.6`) | 63.6 → 49.5 (`-14.1`) | 79.5 → 55.6 (`-23.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-04_HERESY_PLUS1` | KT-04 (Zwierciadło Herezji): heresy 0 → 1 | 77.0 → 🟢 ** 71.1** (`-5.9`) | 87.9 → 88.6 (`⬆️ +0.7`) | 63.6 → 57.6 (`-6.0`) | 79.5 → 67.1 (`-12.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-05_COST_PLUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 2 | 77.0 → 🟢 ** 79.2** (`⬆️ +2.2`) | 87.9 → 90.7 (`⬆️ +2.8`) | 63.6 → 48.9 (`-14.7`) | 79.5 → 98.1 (`⬆️ +18.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-05_COST_MINUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 0 | 77.0 → 🟢 ** 79.1** (`⬆️ +2.1`) | 87.9 → 86.9 (`-1.0`) | 63.6 → 66.5 (`⬆️ +2.9`) | 79.5 → 83.8 (`⬆️ +4.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-05_HERESY_PLUS1` | KT-05 (Wskazówka Cyklu): heresy 0 → 1 | 77.0 → 🟢 ** 72.7** (`-4.3`) | 87.9 → 87.8 (`-0.1`) | 63.6 → 61.6 (`-2.0`) | 79.5 → 68.6 (`-10.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_COST_PLUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 3 | 77.0 → 🟢 ** 73.4** (`-3.6`) | 87.9 → 89.5 (`⬆️ +1.6`) | 63.6 → 32.4 (`-31.2`) | 79.5 → 98.3 (`⬆️ +18.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-06_COST_MINUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 1 | 77.0 → 🟢 ** 77.9** (`⬆️ +0.9`) | 87.9 → 86.1 (`-1.8`) | 63.6 → 62.0 (`-1.6`) | 79.5 → 85.6 (`⬆️ +6.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-06_HERESY_PLUS1` | KT-06 (Przesłuchanie Imienia): heresy 0 → 1 | 77.0 → 🟢 ** 72.6** (`-4.4`) | 87.9 → 86.7 (`-1.2`) | 63.6 → 68.5 (`⬆️ +4.9`) | 79.5 → 62.7 (`-16.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_COST_PLUS1` | KT-07 (Archiwum Ukryte): cost 1 → 2 | 77.0 → 🟢 ** 69.9** (`-7.1`) | 87.9 → 90.5 (`⬆️ +2.6`) | 63.6 → 32.4 (`-31.2`) | 79.5 → 86.8 (`⬆️ +7.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-07_COST_MINUS1` | KT-07 (Archiwum Ukryte): cost 1 → 0 | 77.0 → 🟢 ** 79.6** (`⬆️ +2.6`) | 87.9 → 87.4 (`-0.5`) | 63.6 → 64.8 (`⬆️ +1.2`) | 79.5 → 86.6 (`⬆️ +7.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-07_HERESY_PLUS1` | KT-07 (Archiwum Ukryte): heresy 0 → 1 | 77.0 → 🟢 ** 68.6** (`-8.4`) | 87.9 → 89.9 (`⬆️ +2.0`) | 63.6 → 46.9 (`-16.7`) | 79.5 → 68.9 (`-10.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-08_COST_PLUS1` | KT-08 (Areszt Wiedzy): cost 2 → 3 | 77.0 → 🟢 ** 78.1** (`⬆️ +1.1`) | 87.9 → 87.0 (`-0.9`) | 63.6 → 49.3 (`-14.3`) | 79.5 → 98.1 (`⬆️ +18.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-08_COST_MINUS1` | KT-08 (Areszt Wiedzy): cost 2 → 1 | 77.0 → 🟢 ** 82.7** (`⬆️ +5.7`) | 87.9 → 86.6 (`-1.3`) | 63.6 → 64.2 (`⬆️ +0.6`) | 79.5 → 97.2 (`⬆️ +17.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-08_HERESY_PLUS1` | KT-08 (Areszt Wiedzy): heresy 0 → 1 | 77.0 → 🟢 ** 70.4** (`-6.6`) | 87.9 | 63.6 → 55.5 (`-8.1`) | 79.5 → 67.9 (`-11.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 1 → 2 | 77.0 → 🟢 ** 82.8** (`⬆️ +5.8`) | 87.9 → 86.2 (`-1.7`) | 63.6 → 62.7 (`-0.9`) | 79.5 → 99.5 (`⬆️ +20.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-09_COST_MINUS1` | KT-09 (Fragment Kodeksu): cost 1 → 0 | 77.0 → 🟢 ** 70.7** (`-6.3`) | 87.9 → 86.3 (`-1.6`) | 63.6 → 63.3 (`-0.3`) | 79.5 → 62.4 (`-17.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_HERESY_PLUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 2 | 77.0 → 🟢 ** 76.1** (`-0.9`) | 87.9 → 89.1 (`⬆️ +1.2`) | 63.6 → 56.5 (`-7.1`) | 79.5 → 82.7 (`⬆️ +3.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_HERESY_MINUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 0 | 77.0 → 🟢 ** 75.5** (`-1.5`) | 87.9 → 85.1 (`-2.8`) | 63.6 → 60.0 (`-3.6`) | 79.5 → 81.4 (`⬆️ +1.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_COST_PLUS1` | KT-10 (Pieczęć Salomona): cost 1 → 2 | 77.0 → 🟢 ** 84.6** (`⬆️ +7.6`) | 87.9 → 93.4 (`⬆️ +5.5`) | 63.6 → 62.4 (`-1.2`) | 79.5 → 98.0 (`⬆️ +18.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-10_COST_MINUS1` | KT-10 (Pieczęć Salomona): cost 1 → 0 | 77.0 → 🟢 ** 73.2** (`-3.8`) | 87.9 → 87.4 (`-0.5`) | 63.6 → 58.5 (`-5.1`) | 79.5 → 73.8 (`-5.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_HERESY_PLUS1` | KT-10 (Pieczęć Salomona): heresy 0 → 1 | 77.0 → 🟢 ** 78.9** (`⬆️ +1.9`) | 87.9 → 82.6 (`-5.3`) | 63.6 → 58.1 (`-5.5`) | 79.5 → 95.9 (`⬆️ +16.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-01_COST_PLUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 2 | 77.0 → 🟢 ** 79.2** (`⬆️ +2.2`) | 87.9 → 94.1 (`⬆️ +6.2`) | 63.6 → 63.1 (`-0.5`) | 79.5 → 80.4 (`⬆️ +0.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-01_COST_MINUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 0 | 77.0 → 🟢 ** 77.8** (`⬆️ +0.8`) | 87.9 → 87.8 (`-0.1`) | 63.6 → 62.5 (`-1.1`) | 79.5 → 83.1 (`⬆️ +3.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-01_HERESY_PLUS1` | SO-01 (Patrol Familiariuszy): heresy 0 → 1 | 77.0 → 🟢 ** 68.2** (`-8.8`) | 87.9 → 82.0 (`-5.9`) | 63.6 → 55.5 (`-8.1`) | 79.5 → 67.1 (`-12.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 77.0 → 🟢 ** 78.7** (`⬆️ +1.7`) | 87.9 → 88.0 (`⬆️ +0.1`) | 63.6 → 50.6 (`-13.0`) | 79.5 → 97.4 (`⬆️ +17.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-02_COST_MINUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 0 | 77.0 → 🟢 ** 68.4** (`-8.6`) | 87.9 → 87.3 (`-0.6`) | 63.6 → 57.3 (`-6.3`) | 79.5 → 60.5 (`-19.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): heresy 0 → 1 | 77.0 → 🟢 ** 61.8** (`-15.2`) | 87.9 → 77.1 (`-10.8`) | 63.6 → 54.9 (`-8.7`) | 79.5 → 53.3 (`-26.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_COST_PLUS1` | SO-03 (Podejrzenie): cost 1 → 2 | 🟢 ** 77.0** | 87.9 → 89.7 (`⬆️ +1.8`) | 63.6 → 61.5 (`-2.1`) | 79.5 → 79.7 (`⬆️ +0.2`) | ⚪ OPTYMALNY |
| `L3_SO-03_COST_MINUS1` | SO-03 (Podejrzenie): cost 1 → 0 | 77.0 → 🟢 ** 74.9** (`-2.1`) | 87.9 → 92.2 (`⬆️ +4.3`) | 63.6 → 59.2 (`-4.4`) | 79.5 → 73.3 (`-6.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_HERESY_PLUS1` | SO-03 (Podejrzenie): heresy 0 → 1 | 77.0 → 🟢 ** 60.3** (`-16.7`) | 87.9 → 79.5 (`-8.4`) | 63.6 → 45.9 (`-17.7`) | 79.5 → 55.6 (`-23.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_COST_PLUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 2 | 77.0 → 🟢 ** 70.6** (`-6.4`) | 87.9 → 87.7 (`-0.2`) | 63.6 → 67.8 (`⬆️ +4.2`) | 79.5 → 56.3 (`-23.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_COST_MINUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 0 | 77.0 → 🟢 ** 66.1** (`-10.9`) | 87.9 → 92.9 (`⬆️ +5.0`) | 63.6 → 61.0 (`-2.6`) | 79.5 → 44.4 (`-35.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-04_HERESY_PLUS1` | SO-04 (Publiczne Ostrzeżenie): heresy 0 → 1 | 77.0 → 🟢 ** 62.9** (`-14.1`) | 87.9 → 79.2 (`-8.7`) | 63.6 → 46.0 (`-17.6`) | 79.5 → 63.4 (`-16.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-05_COST_PLUS1` | SO-05 (Wezwanie do Trybunału): cost 0 → 1 | 🟢 ** 77.0** | 87.9 | 63.6 | 79.5 | ⚪ OPTYMALNY |
| `L3_SO-05_HERESY_PLUS1` | SO-05 (Wezwanie do Trybunału): heresy 0 → 1 | 🟢 ** 77.0** | 87.9 | 63.6 | 79.5 | ⚪ OPTYMALNY |
| `L3_SO-06_COST_PLUS1` | SO-06 (Areszt Trybunalski): cost 2 → 3 | 77.0 → 🟢 ** 63.8** (`-13.2`) | 87.9 → 87.4 (`-0.5`) | 63.6 → 57.9 (`-5.7`) | 79.5 → 46.2 (`-33.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_COST_MINUS1` | SO-06 (Areszt Trybunalski): cost 2 → 1 | 77.0 → 🟢 ** 70.0** (`-7.0`) | 87.9 → 87.3 (`-0.6`) | 63.6 → 71.8 (`⬆️ +8.2`) | 79.5 → 50.8 (`-28.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-06_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): heresy 0 → 1 | 77.0 → 🟢 ** 72.8** (`-4.2`) | 87.9 → 89.0 (`⬆️ +1.1`) | 63.6 → 64.1 (`⬆️ +0.5`) | 79.5 → 65.3 (`-14.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-07_COST_PLUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 3 | 77.0 → 🟢 ** 58.8** (`-18.2`) | 87.9 → 90.2 (`⬆️ +2.3`) | 63.6 → 47.3 (`-16.3`) | 79.5 → 38.8 (`-40.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-07_COST_MINUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 1 | 77.0 → 🟢 ** 70.1** (`-6.9`) | 87.9 → 89.7 (`⬆️ +1.8`) | 63.6 → 50.4 (`-13.2`) | 79.5 → 70.2 (`-9.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-07_HERESY_PLUS1` | SO-07 (Przesłuchanie Oficjum): heresy 0 → 1 | 77.0 → 🟢 ** 67.8** (`-9.2`) | 87.9 → 82.6 (`-5.3`) | 63.6 → 66.6 (`⬆️ +3.0`) | 79.5 → 54.3 (`-25.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_COST_PLUS1` | SO-08 (Nasłanie Inkwizytora): cost 2 → 3 | 77.0 → 🟢 ** 69.9** (`-7.1`) | 87.9 → 83.3 (`-4.6`) | 63.6 → 49.9 (`-13.7`) | 79.5 → 76.4 (`-3.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_COST_MINUS1` | SO-08 (Nasłanie Inkwizytora): cost 2 → 1 | 77.0 → 🟢 ** 61.9** (`-15.1`) | 87.9 → 85.5 (`-2.4`) | 63.6 → 36.0 (`-27.6`) | 79.5 → 64.1 (`-15.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_HERESY_PLUS1` | SO-08 (Nasłanie Inkwizytora): heresy 1 → 2 | 77.0 → 🟢 ** 64.2** (`-12.8`) | 87.9 → 77.4 (`-10.5`) | 63.6 → 58.7 (`-4.9`) | 79.5 → 56.5 (`-23.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_HERESY_MINUS1` | SO-08 (Nasłanie Inkwizytora): heresy 1 → 0 | 77.0 → 🟢 ** 73.6** (`-3.4`) | 87.9 → 81.3 (`-6.6`) | 63.6 → 58.0 (`-5.6`) | 79.5 → 81.6 (`⬆️ +2.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_COST_PLUS1` | SO-09 (Świadek Koronny): cost 2 → 3 | 77.0 → 🟢 ** 68.5** (`-8.5`) | 87.9 → 89.2 (`⬆️ +1.3`) | 63.6 → 53.2 (`-10.4`) | 79.5 → 63.2 (`-16.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_COST_MINUS1` | SO-09 (Świadek Koronny): cost 2 → 1 | 77.0 → 🟢 ** 65.4** (`-11.6`) | 87.9 → 89.2 (`⬆️ +1.3`) | 63.6 → 42.2 (`-21.4`) | 79.5 → 64.9 (`-14.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_HERESY_PLUS1` | SO-09 (Świadek Koronny): heresy 0 → 1 | 77.0 → 🟢 ** 68.7** (`-8.3`) | 87.9 → 83.5 (`-4.4`) | 63.6 → 47.9 (`-15.7`) | 79.5 → 74.8 (`-4.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_COST_PLUS1` | SO-10 (Oczyść Miasto): cost 4 → 5 | 77.0 → 🟢 ** 60.5** (`-16.5`) | 87.9 → 71.5 (`-16.4`) | 63.6 → 29.8 (`-33.8`) | 79.5 → 80.2 (`⬆️ +0.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_COST_MINUS1` | SO-10 (Oczyść Miasto): cost 4 → 3 | 77.0 → 🟢 ** 74.3** (`-2.7`) | 87.9 → 89.2 (`⬆️ +1.3`) | 63.6 → 62.7 (`-0.9`) | 79.5 → 71.1 (`-8.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_HERESY_PLUS1` | SO-10 (Oczyść Miasto): heresy 2 → 3 | 77.0 → 🟢 ** 62.7** (`-14.3`) | 87.9 → 77.5 (`-10.4`) | 63.6 → 44.5 (`-19.1`) | 79.5 → 66.2 (`-13.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_HERESY_MINUS1` | SO-10 (Oczyść Miasto): heresy 2 → 1 | 77.0 → 🟢 ** 69.4** (`-7.6`) | 87.9 → 81.4 (`-6.5`) | 63.6 → 43.7 (`-19.9`) | 79.5 → 83.2 (`⬆️ +3.7`) | 🔴 POGARSZA GLOBALNIE |

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | 5.62 Er (1–9) | 3.1% | 28.7% | 1.02 (0–3) | 3.69 (0–15) | 0.53zł (0.0–2.3) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_COST_PLUS1` | 5.67 Er (1–9) | 3.7% | 30.2% | 1.02 (0–3) | 3.80 (0–17) | 0.57zł (0.0–2.3) | 6.27 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-01_COST_MINUS1` | 5.59 Er (1–9) | 2.9% | 28.5% | 1.02 (0–3) | 3.68 (0–17) | 0.57zł (0.0–2.3) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_HERESY_PLUS1` | 5.59 Er (1–9) | 3.0% | 28.6% | 1.01 (0–3) | 3.75 (0–15) | 0.53zł (0.0–2.3) | 6.33 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_COST_PLUS1` | 5.67 Er (1–9) | 3.9% | 31.2% | 1.02 (0–3) | 3.77 (0–17) | 0.56zł (0.0–2.3) | 6.27 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-02_COST_MINUS1` | 5.59 Er (1–9) | 3.0% | 28.4% | 1.02 (0–3) | 3.66 (0–17) | 0.58zł (0.0–2.7) | 6.22 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_HERESY_PLUS1` | 5.59 Er (1–9) | 3.0% | 28.6% | 1.02 (0–3) | 3.79 (0–15) | 0.53zł (0.0–2.3) | 6.36 (1.3–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_COST_PLUS1` | 5.68 Er (1–9) | 3.8% | 30.1% | 1.03 (0–3) | 3.74 (0–15) | 0.54zł (0.0–2.3) | 6.22 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-03_COST_MINUS1` | 5.59 Er (1–9) | 2.8% | 28.5% | 1.01 (0–3) | 3.70 (0–17) | 0.57zł (0.0–2.7) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_HERESY_PLUS1` | 5.60 Er (1–9) | 3.0% | 28.6% | 1.01 (0–3) | 3.81 (0–15) | 0.53zł (0.0–2.3) | 6.37 (1.4–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_HERESY_MINUS1` | 5.64 Er (1–9) | 3.2% | 28.7% | 1.02 (0–3) | 3.61 (0–17) | 0.53zł (0.0–2.3) | 6.07 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_COST_PLUS1` | 5.66 Er (1–9) | 3.3% | 30.1% | 1.03 (0–3) | 3.70 (0–14) | 0.55zł (0.0–2.3) | 6.24 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-04_COST_MINUS1` | 5.59 Er (1–9) | 2.9% | 28.5% | 1.02 (0–3) | 3.68 (0–17) | 0.57zł (0.0–2.3) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_HERESY_PLUS1` | 5.59 Er (1–9) | 2.9% | 28.6% | 1.01 (0–3) | 3.79 (0–14) | 0.53zł (0.0–2.3) | 6.35 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_COST_PLUS1` | 5.68 Er (1–9) | 3.9% | 30.0% | 1.03 (0–3) | 3.72 (0–15) | 0.53zł (0.0–2.3) | 6.24 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-05_COST_MINUS1` | 5.59 Er (1–9) | 2.9% | 28.4% | 1.01 (0–3) | 3.68 (0–17) | 0.56zł (0.0–2.7) | 6.22 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_HERESY_PLUS1` | 5.59 Er (1–9) | 3.0% | 28.6% | 1.01 (0–3) | 3.80 (0–15) | 0.53zł (0.0–2.3) | 6.36 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_COST_PLUS1` | 5.64 Er (1–9) | 3.6% | 29.1% | 1.02 (0–3) | 3.74 (0–15) | 0.54zł (0.0–2.7) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_COST_MINUS1` | 5.59 Er (1–9) | 3.0% | 28.6% | 1.01 (0–3) | 3.66 (0–17) | 0.54zł (0.0–2.7) | 6.17 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_HERESY_PLUS1` | 5.61 Er (1–9) | 3.2% | 28.7% | 1.02 (0–3) | 3.73 (0–15) | 0.53zł (0.0–2.3) | 6.29 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_COST_PLUS1` | 5.62 Er (1–9) | 3.1% | 29.3% | 1.02 (0–3) | 3.69 (0–18) | 0.53zł (0.0–2.3) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_COST_MINUS1` | 5.57 Er (1–9) | 2.7% | 28.5% | 1.01 (0–3) | 3.65 (0–15) | 0.55zł (0.0–2.3) | 6.18 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_HERESY_PLUS1` | 5.60 Er (1–9) | 3.0% | 28.6% | 1.02 (0–3) | 3.78 (0–15) | 0.53zł (0.0–2.3) | 6.35 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_COST_PLUS1` | 5.63 Er (1–9) | 3.0% | 30.3% | 1.02 (0–3) | 3.66 (0–16) | 0.59zł (0.0–2.3) | 6.16 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-08_COST_MINUS1` | 5.60 Er (1–9) | 3.0% | 28.5% | 1.03 (0–3) | 3.75 (0–17) | 0.58zł (0.0–2.3) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_HERESY_PLUS1` | 5.59 Er (1–9) | 2.9% | 28.6% | 1.01 (0–3) | 3.71 (0–15) | 0.53zł (0.0–2.3) | 6.30 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_HERESY_MINUS1` | 5.62 Er (1–9) | 3.2% | 28.7% | 1.02 (0–3) | 3.64 (0–16) | 0.53zł (0.0–2.3) | 6.15 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_COST_PLUS1` | 5.70 Er (1–9) | 3.7% | 29.1% | 1.03 (0–3) | 3.71 (0–15) | 0.55zł (0.0–2.3) | 6.24 (1.3–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_COST_MINUS1` | 5.60 Er (1–9) | 3.1% | 28.1% | 1.02 (0–3) | 3.68 (0–15) | 0.56zł (0.0–2.7) | 6.19 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_HERESY_PLUS1` | 5.58 Er (1–9) | 2.9% | 28.6% | 1.01 (0–3) | 3.89 (0–15) | 0.52zł (0.0–2.3) | 6.43 (1.8–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_COST_PLUS1` | 5.73 Er (1–9) | 4.0% | 30.1% | 1.04 (0–3) | 3.80 (0–14) | 0.53zł (0.0–2.3) | 6.24 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-10_COST_MINUS1` | 5.60 Er (1–9) | 3.1% | 28.2% | 1.02 (0–3) | 3.70 (0–17) | 0.57zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_PLUS1` | 5.53 Er (1–9) | 2.7% | 28.4% | 1.00 (0–3) | 3.95 (0–17) | 0.52zł (0.0–2.3) | 6.45 (1.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_MINUS1` | 5.64 Er (1–9) | 3.3% | 28.8% | 1.02 (0–3) | 3.52 (0–15) | 0.53zł (0.0–2.5) | 5.83 (0.7–9.7) | 🟢 W NORMIE |
| `L3_GC-01_COST_PLUS1` | 5.63 Er (1–9) | 3.2% | 29.2% | 1.02 (0–3) | 3.70 (0–16) | 0.55zł (0.0–2.3) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-01_COST_MINUS1` | 5.59 Er (1–9) | 3.0% | 27.9% | 1.01 (0–3) | 3.68 (0–16) | 0.55zł (0.0–2.3) | 6.30 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-01_HERESY_PLUS1` | 5.61 Er (1–9) | 3.1% | 28.6% | 1.02 (0–3) | 3.73 (0–15) | 0.53zł (0.0–2.3) | 6.34 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-02_COST_PLUS1` | 5.68 Er (1–9) | 3.7% | 30.5% | 1.04 (0–3) | 3.75 (0–15) | 0.52zł (0.0–2.3) | 6.22 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-02_COST_MINUS1` | 5.59 Er (1–9) | 3.0% | 28.0% | 1.02 (0–3) | 3.72 (0–15) | 0.56zł (0.0–2.7) | 6.32 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-02_HERESY_PLUS1` | 5.59 Er (1–9) | 3.2% | 28.5% | 1.01 (0–3) | 3.77 (0–15) | 0.53zł (0.0–3.0) | 6.35 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-03_COST_PLUS1` | 5.66 Er (1–9) | 3.3% | 29.3% | 1.03 (0–3) | 3.67 (0–16) | 0.55zł (0.0–2.7) | 6.22 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-03_COST_MINUS1` | 5.60 Er (1–9) | 3.2% | 27.9% | 1.01 (0–3) | 3.75 (0–15) | 0.56zł (0.0–2.7) | 6.32 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-03_HERESY_PLUS1` | 5.61 Er (1–9) | 3.1% | 28.6% | 1.02 (0–3) | 3.77 (0–15) | 0.53zł (0.0–2.3) | 6.36 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-04_COST_PLUS1` | 5.65 Er (1–9) | 3.5% | 29.3% | 1.03 (0–3) | 3.65 (0–14) | 0.54zł (0.0–2.7) | 6.19 (1.3–10.0) | 🟢 W NORMIE |
| `L3_GC-04_COST_MINUS1` | 5.60 Er (1–9) | 2.8% | 28.1% | 1.01 (0–3) | 3.77 (0–15) | 0.55zł (0.0–2.3) | 6.32 (1.4–10.0) | 🟢 W NORMIE |
| `L3_GC-04_HERESY_PLUS1` | 5.60 Er (1–9) | 3.0% | 28.5% | 1.02 (0–3) | 3.81 (0–15) | 0.53zł (0.0–2.3) | 6.37 (1.4–10.0) | 🟢 W NORMIE |
| `L3_GC-04_HERESY_MINUS1` | 5.62 Er (1–9) | 3.1% | 28.7% | 1.02 (0–3) | 3.57 (0–15) | 0.53zł (0.0–2.3) | 6.09 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-05_COST_PLUS1` | 5.62 Er (1–9) | 3.1% | 28.7% | 1.02 (0–3) | 3.69 (0–15) | 0.53zł (0.0–2.3) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-05_HERESY_PLUS1` | 5.62 Er (1–9) | 3.1% | 28.7% | 1.02 (0–3) | 3.69 (0–15) | 0.53zł (0.0–2.3) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-06_COST_PLUS1` | 5.68 Er (1–9) | 3.8% | 29.2% | 1.03 (0–3) | 3.79 (0–16) | 0.53zł (0.0–2.3) | 6.33 (1.3–10.0) | 🟢 W NORMIE |
| `L3_GC-06_COST_MINUS1` | 5.59 Er (1–9) | 3.0% | 28.1% | 1.01 (0–4) | 3.70 (0–15) | 0.55zł (0.0–2.7) | 6.31 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-06_HERESY_PLUS1` | 5.61 Er (1–9) | 3.2% | 28.6% | 1.02 (0–3) | 3.75 (0–15) | 0.53zł (0.0–2.3) | 6.36 (1.4–10.0) | 🟢 W NORMIE |
| `L3_GC-07_COST_PLUS1` | 5.62 Er (1–9) | 3.5% | 28.9% | 1.03 (0–3) | 3.71 (0–16) | 0.53zł (0.0–2.3) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-07_COST_MINUS1` | 5.59 Er (1–9) | 3.0% | 28.2% | 1.02 (0–3) | 3.72 (0–15) | 0.52zł (0.0–2.3) | 6.33 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-07_HERESY_PLUS1` | 5.61 Er (1–9) | 3.1% | 28.6% | 1.02 (0–3) | 3.72 (0–15) | 0.53zł (0.0–2.3) | 6.29 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-07_HERESY_MINUS1` | 5.62 Er (1–9) | 3.2% | 28.7% | 1.02 (0–3) | 3.67 (0–15) | 0.53zł (0.0–2.3) | 6.18 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_PLUS1` | 5.69 Er (1–9) | 3.7% | 29.8% | 1.03 (0–3) | 3.67 (0–15) | 0.53zł (0.0–2.3) | 6.20 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_MINUS1` | 5.58 Er (1–9) | 2.9% | 28.0% | 1.01 (0–3) | 3.72 (0–15) | 0.56zł (0.0–2.3) | 6.32 (1.3–10.0) | 🟢 W NORMIE |
| `L3_GC-08_HERESY_PLUS1` | 5.59 Er (1–9) | 2.9% | 28.5% | 1.01 (0–3) | 3.78 (0–14) | 0.53zł (0.0–2.3) | 6.36 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-09_COST_PLUS1` | 5.68 Er (1–9) | 3.7% | 29.2% | 1.04 (0–3) | 3.72 (0–14) | 0.51zł (0.0–2.3) | 6.24 (1.3–10.0) | 🟢 W NORMIE |
| `L3_GC-09_COST_MINUS1` | 5.62 Er (1–9) | 2.8% | 28.4% | 1.02 (0–4) | 3.78 (0–15) | 0.56zł (0.0–2.3) | 6.35 (1.5–10.0) | 🟢 W NORMIE |
| `L3_GC-09_HERESY_PLUS1` | 5.61 Er (1–9) | 3.1% | 28.6% | 1.02 (0–3) | 3.77 (0–14) | 0.53zł (0.0–3.0) | 6.37 (1.5–10.0) | 🟢 W NORMIE |
| `L3_GC-10_COST_PLUS1` | 5.69 Er (1–9) | 3.6% | 28.2% | 1.03 (0–3) | 3.62 (0–16) | 0.58zł (0.0–2.3) | 6.07 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-10_COST_MINUS1` | 5.57 Er (1–9) | 3.2% | 27.8% | 1.02 (0–3) | 3.76 (0–15) | 0.54zł (0.0–2.7) | 6.30 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-10_HERESY_PLUS1` | 5.54 Er (1–9) | 3.0% | 28.3% | 1.01 (0–3) | 4.03 (0–15) | 0.53zł (0.0–2.3) | 6.39 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-10_HERESY_MINUS1` | 5.65 Er (1–9) | 3.6% | 28.8% | 1.04 (0–3) | 3.40 (0–15) | 0.53zł (0.0–2.3) | 6.02 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-01_COST_PLUS1` | 5.62 Er (1–9) | 2.7% | 29.7% | 1.02 (0–3) | 3.74 (0–16) | 0.55zł (0.0–2.3) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-01_COST_MINUS1` | 5.59 Er (1–9) | 2.5% | 28.1% | 1.01 (0–3) | 3.70 (0–15) | 0.54zł (0.0–2.3) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-01_HERESY_PLUS1` | 5.59 Er (1–9) | 2.9% | 28.6% | 1.01 (0–3) | 3.72 (0–14) | 0.53zł (0.0–2.3) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-02_COST_PLUS1` | 5.67 Er (1–9) | 3.8% | 31.0% | 1.02 (0–3) | 3.79 (0–17) | 0.54zł (0.0–2.3) | 6.24 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-02_COST_MINUS1` | 5.59 Er (1–9) | 2.6% | 28.5% | 1.01 (0–3) | 3.69 (0–15) | 0.55zł (0.0–2.5) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-02_HERESY_PLUS1` | 5.57 Er (1–9) | 3.0% | 28.5% | 1.01 (0–3) | 3.75 (0–19) | 0.53zł (0.0–2.3) | 6.29 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-03_COST_PLUS1` | 5.63 Er (1–9) | 2.8% | 29.9% | 1.02 (0–3) | 3.65 (0–17) | 0.54zł (0.0–2.3) | 6.19 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-03_COST_MINUS1` | 5.59 Er (1–9) | 2.6% | 28.1% | 1.02 (0–4) | 3.74 (0–16) | 0.54zł (0.0–2.3) | 6.30 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-03_HERESY_PLUS1` | 5.58 Er (1–9) | 3.1% | 28.6% | 1.01 (0–3) | 3.77 (0–19) | 0.54zł (0.0–2.7) | 6.30 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-04_COST_PLUS1` | 5.67 Er (1–9) | 3.1% | 29.8% | 1.02 (0–3) | 3.71 (0–15) | 0.55zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-04_COST_MINUS1` | 5.56 Er (1–9) | 2.8% | 28.1% | 1.01 (0–3) | 3.70 (0–16) | 0.54zł (0.0–2.3) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-04_HERESY_PLUS1` | 5.56 Er (1–9) | 3.0% | 28.5% | 1.01 (0–3) | 3.81 (0–19) | 0.53zł (0.0–2.7) | 6.30 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-04_HERESY_MINUS1` | 5.67 Er (1–9) | 3.2% | 28.8% | 1.03 (0–3) | 3.61 (0–16) | 0.53zł (0.0–2.3) | 6.17 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-05_COST_PLUS1` | 5.62 Er (1–9) | 2.8% | 28.9% | 1.03 (0–3) | 3.64 (0–14) | 0.53zł (0.0–2.3) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-05_COST_MINUS1` | 5.57 Er (1–9) | 2.4% | 28.1% | 1.01 (0–3) | 3.64 (0–14) | 0.52zł (0.0–2.3) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-05_HERESY_PLUS1` | 5.60 Er (1–9) | 3.0% | 28.6% | 1.02 (0–3) | 3.74 (0–15) | 0.53zł (0.0–2.3) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-06_COST_PLUS1` | 5.61 Er (1–9) | 3.0% | 28.8% | 1.01 (0–3) | 3.70 (0–15) | 0.54zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-06_COST_MINUS1` | 5.66 Er (1–9) | 3.8% | 28.3% | 1.02 (0–3) | 3.80 (0–16) | 0.52zł (0.0–2.3) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-06_HERESY_PLUS1` | 5.60 Er (1–9) | 3.1% | 28.6% | 1.02 (0–3) | 3.70 (0–19) | 0.53zł (0.0–2.3) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-07_COST_PLUS1` | 5.59 Er (1–9) | 2.7% | 28.8% | 1.01 (0–3) | 3.65 (0–17) | 0.52zł (0.0–3.0) | 6.22 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-07_COST_MINUS1` | 5.60 Er (1–9) | 3.0% | 28.3% | 1.02 (0–3) | 3.69 (0–14) | 0.52zł (0.0–2.3) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-07_HERESY_PLUS1` | 5.58 Er (1–9) | 2.9% | 28.6% | 1.01 (0–3) | 3.72 (0–19) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-08_COST_PLUS1` | 5.62 Er (1–9) | 3.0% | 28.7% | 1.02 (0–3) | 3.70 (0–14) | 0.53zł (0.0–2.3) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-08_COST_MINUS1` | 5.64 Er (1–9) | 3.2% | 28.6% | 1.02 (0–3) | 3.76 (0–17) | 0.53zł (0.0–2.3) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-08_HERESY_PLUS1` | 5.61 Er (1–9) | 3.0% | 28.6% | 1.02 (0–3) | 3.70 (0–15) | 0.53zł (0.0–2.3) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-09_COST_PLUS1` | 5.79 Er (1–9) | 4.6% | 28.8% | 1.05 (0–3) | 3.90 (0–16) | 0.57zł (0.0–2.3) | 6.30 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-09_COST_MINUS1` | 5.56 Er (1–9) | 2.8% | 28.4% | 1.01 (0–3) | 3.67 (0–14) | 0.53zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-09_HERESY_PLUS1` | 5.57 Er (1–9) | 3.3% | 28.5% | 1.02 (0–3) | 3.79 (0–15) | 0.53zł (0.0–2.3) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-09_HERESY_MINUS1` | 5.66 Er (1–9) | 3.2% | 28.8% | 1.03 (0–3) | 3.61 (0–15) | 0.53zł (0.0–2.3) | 6.14 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-10_COST_PLUS1` | 5.75 Er (1–9) | 4.5% | 29.0% | 1.05 (0–3) | 3.76 (0–17) | 0.55zł (0.0–2.3) | 6.19 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-10_COST_MINUS1` | 5.54 Er (1–9) | 2.4% | 27.9% | 1.01 (0–3) | 3.72 (0–14) | 0.52zł (0.0–2.3) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-10_HERESY_PLUS1` | 5.45 Er (1–9) | 2.4% | 28.2% | 0.99 (0–3) | 3.98 (0–18) | 0.53zł (0.0–2.3) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-10_HERESY_MINUS1` | 5.72 Er (1–9) | 3.4% | 28.9% | 1.04 (0–3) | 3.46 (0–14) | 0.53zł (0.0–2.7) | 6.10 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_PLUS1` | 5.64 Er (1–9) | 3.5% | 29.1% | 1.03 (0–3) | 3.72 (0–18) | 0.44zł (0.0–2.3) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_MINUS1` | 5.62 Er (1–9) | 3.2% | 28.6% | 1.02 (0–3) | 3.69 (0–15) | 0.70zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-01_HERESY_PLUS1` | 5.63 Er (1–9) | 4.0% | 28.7% | 1.02 (0–3) | 3.77 (0–18) | 0.53zł (0.0–2.7) | 6.37 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-02_COST_PLUS1` | 5.64 Er (1–9) | 3.6% | 29.5% | 1.02 (0–3) | 3.73 (0–18) | 0.43zł (0.0–2.0) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-02_COST_MINUS1` | 5.62 Er (1–9) | 3.3% | 28.6% | 1.02 (0–3) | 3.68 (0–15) | 0.71zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-02_HERESY_PLUS1` | 5.62 Er (1–9) | 4.0% | 28.7% | 1.02 (0–3) | 3.78 (0–18) | 0.54zł (0.0–2.7) | 6.38 (1.5–10.0) | 🟢 W NORMIE |
| `L3_KT-03_COST_PLUS1` | 5.64 Er (1–9) | 3.5% | 29.1% | 1.02 (0–3) | 3.73 (0–19) | 0.40zł (0.0–2.0) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-03_HERESY_PLUS1` | 5.63 Er (1–9) | 4.5% | 28.7% | 1.02 (0–3) | 3.80 (0–18) | 0.54zł (0.0–3.0) | 6.38 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-03_HERESY_MINUS1` | 5.63 Er (1–9) | 2.8% | 28.7% | 1.02 (0–3) | 3.66 (0–15) | 0.53zł (0.0–2.3) | 6.10 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-04_COST_PLUS1` | 5.65 Er (1–9) | 3.7% | 29.1% | 1.02 (0–3) | 3.69 (0–18) | 0.43zł (0.0–2.3) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-04_COST_MINUS1` | 5.62 Er (1–9) | 3.2% | 28.5% | 1.02 (0–3) | 3.68 (0–15) | 0.70zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-04_HERESY_PLUS1` | 5.62 Er (1–9) | 3.9% | 28.7% | 1.02 (0–3) | 3.77 (0–18) | 0.53zł (0.0–2.7) | 6.37 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-05_COST_PLUS1` | 5.65 Er (1–9) | 3.6% | 29.2% | 1.02 (0–3) | 3.72 (0–18) | 0.43zł (0.0–2.3) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-05_COST_MINUS1` | 5.62 Er (1–9) | 3.3% | 28.6% | 1.02 (0–3) | 3.69 (0–15) | 0.71zł (0.0–2.8) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-05_HERESY_PLUS1` | 5.62 Er (1–9) | 3.9% | 28.7% | 1.02 (0–3) | 3.79 (0–18) | 0.53zł (0.0–2.3) | 6.38 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-06_COST_PLUS1` | 5.65 Er (1–9) | 3.7% | 29.4% | 1.03 (0–3) | 3.70 (0–18) | 0.45zł (0.0–2.3) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-06_COST_MINUS1` | 5.63 Er (1–9) | 3.2% | 28.6% | 1.02 (0–4) | 3.70 (0–15) | 0.74zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-06_HERESY_PLUS1` | 5.65 Er (1–9) | 5.0% | 28.7% | 1.02 (0–3) | 3.83 (0–18) | 0.54zł (0.0–2.7) | 6.41 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-07_COST_PLUS1` | 5.65 Er (1–9) | 3.6% | 29.1% | 1.02 (0–3) | 3.73 (0–18) | 0.43zł (0.0–2.3) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-07_COST_MINUS1` | 5.63 Er (1–9) | 3.3% | 28.6% | 1.02 (0–3) | 3.70 (0–15) | 0.71zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-07_HERESY_PLUS1` | 5.62 Er (1–9) | 3.9% | 28.7% | 1.02 (0–3) | 3.79 (0–18) | 0.53zł (0.0–2.7) | 6.38 (1.3–10.0) | 🟢 W NORMIE |
| `L3_KT-08_COST_PLUS1` | 5.64 Er (1–9) | 3.7% | 29.1% | 1.02 (0–3) | 3.71 (0–18) | 0.45zł (0.0–2.3) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-08_COST_MINUS1` | 5.63 Er (1–9) | 3.3% | 28.6% | 1.02 (0–4) | 3.69 (0–15) | 0.70zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-08_HERESY_PLUS1` | 5.61 Er (1–9) | 3.9% | 28.6% | 1.02 (0–3) | 3.78 (0–18) | 0.53zł (0.0–2.7) | 6.37 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-09_COST_PLUS1` | 5.66 Er (1–9) | 3.8% | 29.3% | 1.02 (0–3) | 3.70 (0–18) | 0.44zł (0.0–2.3) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-09_COST_MINUS1` | 5.63 Er (1–9) | 3.4% | 28.6% | 1.02 (0–3) | 3.69 (0–15) | 0.72zł (0.0–2.8) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-09_HERESY_PLUS1` | 5.63 Er (1–9) | 4.2% | 28.7% | 1.02 (0–3) | 3.81 (0–18) | 0.54zł (0.0–2.3) | 6.38 (1.3–10.0) | 🟢 W NORMIE |
| `L3_KT-09_HERESY_MINUS1` | 5.62 Er (1–9) | 3.1% | 28.7% | 1.02 (0–3) | 3.66 (0–15) | 0.53zł (0.0–2.7) | 6.09 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-10_COST_PLUS1` | 5.64 Er (1–9) | 3.7% | 29.1% | 1.03 (0–3) | 3.72 (0–18) | 0.43zł (0.0–2.3) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-10_COST_MINUS1` | 5.63 Er (1–9) | 3.3% | 28.6% | 1.02 (0–3) | 3.70 (0–15) | 0.71zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-10_HERESY_PLUS1` | 5.62 Er (1–9) | 4.3% | 28.6% | 1.02 (0–3) | 3.92 (0–17) | 0.54zł (0.0–2.3) | 6.50 (1.4–10.0) | 🟢 W NORMIE |
| `L3_SO-01_COST_PLUS1` | 5.62 Er (1–9) | 3.1% | 29.3% | 1.02 (0–3) | 3.72 (0–15) | 0.53zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-01_COST_MINUS1` | 5.61 Er (2–9) | 3.3% | 27.6% | 1.03 (0–4) | 3.71 (0–15) | 0.54zł (0.0–2.3) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-01_HERESY_PLUS1` | 5.54 Er (1–9) | 2.5% | 28.4% | 1.01 (0–3) | 3.73 (0–15) | 0.53zł (0.0–2.3) | 6.32 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-02_COST_PLUS1` | 5.66 Er (1–9) | 3.5% | 30.8% | 1.01 (0–3) | 3.67 (0–15) | 0.54zł (0.0–2.7) | 6.22 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-02_COST_MINUS1` | 5.59 Er (1–9) | 3.4% | 27.5% | 1.07 (0–3) | 3.72 (0–15) | 0.58zł (0.0–2.7) | 6.29 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-02_HERESY_PLUS1` | 5.51 Er (1–9) | 2.6% | 28.3% | 1.01 (0–3) | 3.74 (0–15) | 0.53zł (0.0–2.3) | 6.31 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-03_COST_PLUS1` | 5.65 Er (1–9) | 3.4% | 29.4% | 1.02 (0–4) | 3.66 (0–15) | 0.53zł (0.0–2.3) | 6.20 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-03_COST_MINUS1` | 5.60 Er (1–9) | 3.0% | 27.5% | 1.04 (0–3) | 3.73 (0–15) | 0.54zł (0.0–2.3) | 6.26 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-03_HERESY_PLUS1` | 5.49 Er (1–9) | 2.4% | 28.3% | 1.01 (0–3) | 3.72 (0–15) | 0.52zł (0.0–2.3) | 6.32 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-04_COST_PLUS1` | 5.61 Er (1–9) | 3.3% | 29.3% | 1.00 (0–3) | 3.69 (0–15) | 0.53zł (0.0–2.3) | 6.22 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-04_COST_MINUS1` | 5.61 Er (1–9) | 3.1% | 27.5% | 1.06 (0–3) | 3.74 (0–15) | 0.55zł (0.0–2.7) | 6.28 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-04_HERESY_PLUS1` | 5.49 Er (1–9) | 2.5% | 28.3% | 1.01 (0–3) | 3.76 (0–15) | 0.52zł (0.0–2.3) | 6.34 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-05_COST_PLUS1` | 5.62 Er (1–9) | 3.1% | 28.7% | 1.02 (0–3) | 3.69 (0–15) | 0.53zł (0.0–2.3) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-05_HERESY_PLUS1` | 5.62 Er (1–9) | 3.1% | 28.7% | 1.02 (0–3) | 3.69 (0–15) | 0.53zł (0.0–2.3) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-06_COST_PLUS1` | 5.59 Er (1–9) | 2.8% | 28.5% | 1.04 (0–3) | 3.69 (0–15) | 0.54zł (0.0–2.7) | 6.26 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-06_COST_MINUS1` | 5.61 Er (1–9) | 3.4% | 27.7% | 1.02 (0–3) | 3.69 (0–15) | 0.51zł (0.0–3.0) | 6.22 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-06_HERESY_PLUS1` | 5.60 Er (1–9) | 2.9% | 28.6% | 1.02 (0–3) | 3.70 (0–15) | 0.53zł (0.0–2.3) | 6.27 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-07_COST_PLUS1` | 5.60 Er (1–9) | 3.0% | 28.6% | 1.03 (0–3) | 3.72 (0–15) | 0.55zł (0.0–2.3) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-07_COST_MINUS1` | 5.59 Er (1–9) | 3.2% | 27.6% | 1.04 (0–3) | 3.69 (0–15) | 0.52zł (0.0–2.3) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-07_HERESY_PLUS1` | 5.56 Er (1–9) | 2.7% | 28.5% | 1.01 (0–3) | 3.72 (0–15) | 0.53zł (0.0–2.3) | 6.31 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-08_COST_PLUS1` | 5.64 Er (1–9) | 3.6% | 28.9% | 1.02 (0–3) | 3.65 (0–15) | 0.54zł (0.0–3.0) | 6.18 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-08_COST_MINUS1` | 5.55 Er (1–9) | 2.9% | 27.3% | 1.03 (0–4) | 3.69 (0–15) | 0.50zł (0.0–3.0) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-08_HERESY_PLUS1` | 5.51 Er (1–9) | 2.4% | 28.3% | 1.00 (0–3) | 3.74 (0–15) | 0.53zł (0.0–2.3) | 6.30 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-08_HERESY_MINUS1` | 5.67 Er (1–9) | 3.7% | 28.8% | 1.03 (0–3) | 3.63 (0–15) | 0.54zł (0.0–2.3) | 6.10 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-09_COST_PLUS1` | 5.60 Er (1–9) | 3.0% | 28.7% | 1.04 (0–3) | 3.67 (0–15) | 0.54zł (0.0–2.5) | 6.23 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-09_COST_MINUS1` | 5.63 Er (1–9) | 3.2% | 27.8% | 1.05 (0–3) | 3.70 (0–15) | 0.52zł (0.0–3.0) | 6.27 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-09_HERESY_PLUS1` | 5.54 Er (1–9) | 2.4% | 28.4% | 1.01 (0–3) | 3.71 (0–15) | 0.53zł (0.0–2.3) | 6.31 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-10_COST_PLUS1` | 5.81 Er (1–9) | 4.0% | 28.0% | 0.76 (0–3) | 3.56 (0–15) | 0.54zł (0.0–2.3) | 6.15 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-10_COST_MINUS1` | 5.60 Er (1–9) | 3.2% | 28.1% | 1.03 (0–3) | 3.72 (0–15) | 0.53zł (0.0–2.3) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-10_HERESY_PLUS1` | 5.51 Er (1–9) | 2.9% | 28.3% | 1.01 (0–3) | 3.75 (0–15) | 0.52zł (0.0–2.3) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-10_HERESY_MINUS1` | 5.71 Er (1–9) | 3.5% | 28.9% | 1.03 (0–4) | 3.63 (0–15) | 0.53zł (0.0–2.3) | 6.20 (1.2–10.0) | 🟢 W NORMIE |