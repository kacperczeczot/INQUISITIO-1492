[Strona główna](../../../../../README.md) > [v0.12](README.md) > [audyt_level3_raport](audyt_level3_raport.md)

---

# Raport Precyzyjnego Audytu Poziomu 3 (Parametry Pojedynczych Kart) — Wersja Balansu: v0.12

**Wersja Balansu:** `v0.12` | **Data:** 2026-08-14 11:33 | **Przeanalizowano Wariantów Kart:** 161 | **Próba:** 500 gier/setup | **Czas:** 144.86s
**Filtry:** Parametry: `cost,heresy` | Frakcja: `all` | Karta: `Wszystkie`
**Wynik Bazy Poziomu 3 (Global):** `🟢 50.4 pkt` | 3p: `78.5 pkt` | 4p: `41.3 pkt` | 5p: `31.3 pkt`

## 1. Tabela Wyników Balansu i Delty (Zmiany) dla Każdego Składu Graczy

| ID | Testowany Parametr Karty | Global (baza → test) | 3p (baza → test) | 4p (baza → test) | 5p (baza → test) | Status Balansu |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | Baza (Bieżące parametry wszystkich kart) | 🟢 ** 50.4** | 78.5 | 41.3 | 31.3 | ⚪ OPTYMALNY |
| `L3_CAA-01_COST_PLUS1` | CAA-01 (Przejście Podziemiami): cost 1 → 2 | 50.4 → 🟡 ** 49.6** (`-0.8`) | 78.5 → 73.6 (`-4.9`) | 41.3 → 51.9 (`⬆️ +10.6`) | 31.3 → 23.3 (`-8.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-01_COST_MINUS1` | CAA-01 (Przejście Podziemiami): cost 1 → 0 | 50.4 → 🟢 ** 65.2** (`⬆️ +14.8`) | 78.5 → 79.9 (`⬆️ +1.4`) | 41.3 → 57.6 (`⬆️ +16.3`) | 31.3 → 58.1 (`⬆️ +26.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-01_HERESY_PLUS1` | CAA-01 (Przejście Podziemiami): heresy 0 → 1 | 50.4 → 🟡 ** 44.6** (`-5.8`) | 78.5 → 76.0 (`-2.5`) | 41.3 → 37.1 (`-4.2`) | 31.3 → 20.7 (`-10.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-02_COST_PLUS1` | CAA-02 (Złoto z Kryjówki): cost 1 → 2 | 50.4 → 🟢 ** 65.3** (`⬆️ +14.9`) | 78.5 → 75.1 (`-3.4`) | 41.3 → 50.5 (`⬆️ +9.2`) | 31.3 → 70.3 (`⬆️ +39.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-02_COST_MINUS1` | CAA-02 (Złoto z Kryjówki): cost 1 → 0 | 50.4 → 🟢 ** 65.1** (`⬆️ +14.7`) | 78.5 → 79.2 (`⬆️ +0.7`) | 41.3 → 52.4 (`⬆️ +11.1`) | 31.3 → 63.8 (`⬆️ +32.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-02_HERESY_PLUS1` | CAA-02 (Złoto z Kryjówki): heresy 0 → 1 | 50.4 → 🟢 ** 54.2** (`⬆️ +3.8`) | 78.5 → 77.0 (`-1.5`) | 41.3 → 41.0 (`-0.3`) | 31.3 → 44.7 (`⬆️ +13.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-03_COST_PLUS1` | CAA-03 (Cień na Rynku): cost 1 → 2 | 50.4 → 🟢 ** 50.6** (`⬆️ +0.2`) | 78.5 → 73.8 (`-4.7`) | 41.3 → 27.5 (`-13.8`) | 31.3 → 0.0 (`-31.3`) | ⚪ OPTYMALNY |
| `L3_CAA-03_COST_MINUS1` | CAA-03 (Cień na Rynku): cost 1 → 0 | 50.4 → 🟢 ** 63.0** (`⬆️ +12.6`) | 78.5 → 75.2 (`-3.3`) | 41.3 → 50.9 (`⬆️ +9.6`) | 31.3 → 0.0 (`-31.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-03_HERESY_PLUS1` | CAA-03 (Cień na Rynku): heresy 1 → 2 | 50.4 → 🟢 ** 52.9** (`⬆️ +2.5`) | 78.5 → 78.2 (`-0.3`) | 41.3 → 42.2 (`⬆️ +0.9`) | 31.3 → 38.4 (`⬆️ +7.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-03_HERESY_MINUS1` | CAA-03 (Cień na Rynku): heresy 1 → 0 | 50.4 → 🟢 ** 54.6** (`⬆️ +4.2`) | 78.5 → 74.1 (`-4.4`) | 41.3 → 46.2 (`⬆️ +4.9`) | 31.3 → 43.6 (`⬆️ +12.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-04_COST_PLUS1` | CAA-04 (Fałszywy Trop): cost 1 → 2 | 50.4 → 🟢 ** 55.1** (`⬆️ +4.7`) | 78.5 → 79.7 (`⬆️ +1.2`) | 41.3 → 49.7 (`⬆️ +8.4`) | 31.3 → 36.0 (`⬆️ +4.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-04_COST_MINUS1` | CAA-04 (Fałszywy Trop): cost 1 → 0 | 50.4 → 🟢 ** 55.5** (`⬆️ +5.1`) | 78.5 → 72.3 (`-6.2`) | 41.3 → 54.7 (`⬆️ +13.4`) | 31.3 → 39.4 (`⬆️ +8.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-04_HERESY_PLUS1` | CAA-04 (Fałszywy Trop): heresy 0 → 1 | 50.4 → 🟢 ** 51.0** (`⬆️ +0.6`) | 78.5 → 76.7 (`-1.8`) | 41.3 → 47.0 (`⬆️ +5.7`) | 31.3 → 29.3 (`-2.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-05_COST_PLUS1` | CAA-05 (Ukryty Kurier): cost 1 → 2 | 50.4 → 🟡 ** 46.1** (`-4.3`) | 78.5 → 71.1 (`-7.4`) | 41.3 → 36.0 (`-5.3`) | 31.3 | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-05_COST_MINUS1` | CAA-05 (Ukryty Kurier): cost 1 → 0 | 50.4 → 🟢 ** 56.0** (`⬆️ +5.6`) | 78.5 → 78.8 (`⬆️ +0.3`) | 41.3 → 44.3 (`⬆️ +3.0`) | 31.3 → 44.8 (`⬆️ +13.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-05_HERESY_PLUS1` | CAA-05 (Ukryty Kurier): heresy 0 → 1 | 50.4 → 🟡 ** 47.0** (`-3.4`) | 78.5 → 77.7 (`-0.8`) | 41.3 → 37.8 (`-3.5`) | 31.3 → 25.5 (`-5.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_COST_PLUS1` | CAA-06 (Ucieczka z Lochów): cost 2 → 3 | 50.4 → 🟡 ** 46.1** (`-4.3`) | 78.5 → 78.1 (`-0.4`) | 41.3 → 36.9 (`-4.4`) | 31.3 → 23.4 (`-7.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-06_COST_MINUS1` | CAA-06 (Ucieczka z Lochów): cost 2 → 1 | 50.4 → 🟢 ** 52.5** (`⬆️ +2.1`) | 78.5 → 71.7 (`-6.8`) | 41.3 → 42.6 (`⬆️ +1.3`) | 31.3 → 43.3 (`⬆️ +12.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-06_HERESY_PLUS1` | CAA-06 (Ucieczka z Lochów): heresy 0 → 1 | 50.4 → 🟡 ** 49.8** (`-0.6`) | 78.5 → 78.3 (`-0.2`) | 41.3 → 42.9 (`⬆️ +1.6`) | 31.3 → 28.2 (`-3.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-07_COST_PLUS1` | CAA-07 (Szantaż Bractwa): cost 2 → 3 | 50.4 → 🟢 ** 55.0** (`⬆️ +4.6`) | 78.5 → 78.2 (`-0.3`) | 41.3 → 47.0 (`⬆️ +5.7`) | 31.3 → 39.8 (`⬆️ +8.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-07_COST_MINUS1` | CAA-07 (Szantaż Bractwa): cost 2 → 1 | 50.4 → 🟢 ** 62.7** (`⬆️ +12.3`) | 78.5 → 69.1 (`-9.4`) | 41.3 → 56.3 (`⬆️ +15.0`) | 31.3 → 0.0 (`-31.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-07_HERESY_PLUS1` | CAA-07 (Szantaż Bractwa): heresy 0 → 1 | 50.4 → 🟢 ** 55.7** (`⬆️ +5.3`) | 78.5 → 79.3 (`⬆️ +0.8`) | 41.3 → 42.4 (`⬆️ +1.1`) | 31.3 → 45.3 (`⬆️ +14.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-08_COST_PLUS1` | CAA-08 (Kaptur Nocy): cost 1 → 2 | 50.4 → 🟢 ** 60.3** (`⬆️ +9.9`) | 78.5 → 78.1 (`-0.4`) | 41.3 → 52.9 (`⬆️ +11.6`) | 31.3 → 50.0 (`⬆️ +18.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-08_COST_MINUS1` | CAA-08 (Kaptur Nocy): cost 1 → 0 | 50.4 → 🟢 ** 52.8** (`⬆️ +2.4`) | 78.5 → 78.8 (`⬆️ +0.3`) | 41.3 → 44.4 (`⬆️ +3.1`) | 31.3 → 35.1 (`⬆️ +3.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-08_HERESY_PLUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 2 | 50.4 → 🟢 ** 52.3** (`⬆️ +1.9`) | 78.5 → 78.8 (`⬆️ +0.3`) | 41.3 → 41.6 (`⬆️ +0.3`) | 31.3 → 36.4 (`⬆️ +5.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-08_HERESY_MINUS1` | CAA-08 (Kaptur Nocy): heresy 1 → 0 | 50.4 → 🟡 ** 49.8** (`-0.6`) | 78.5 → 76.4 (`-2.1`) | 41.3 → 41.0 (`-0.3`) | 31.3 → 31.9 (`⬆️ +0.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_COST_PLUS1` | CAA-09 (Kurier Relikwii): cost 2 → 3 | 50.4 → 🟡 ** 45.4** (`-5.0`) | 78.5 → 76.9 (`-1.6`) | 41.3 → 34.5 (`-6.8`) | 31.3 → 24.8 (`-6.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-09_COST_MINUS1` | CAA-09 (Kurier Relikwii): cost 2 → 1 | 50.4 → 🟢 ** 54.2** (`⬆️ +3.8`) | 78.5 → 70.2 (`-8.3`) | 41.3 → 43.2 (`⬆️ +1.9`) | 31.3 → 49.3 (`⬆️ +18.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-09_HERESY_PLUS1` | CAA-09 (Kurier Relikwii): heresy 0 → 1 | 50.4 → 🟡 ** 42.6** (`-7.8`) | 78.5 → 64.9 (`-13.6`) | 41.3 → 27.8 (`-13.5`) | 31.3 → 35.1 (`⬆️ +3.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_COST_PLUS1` | CAA-10 (Echo Alhambry): cost 1 → 2 | 50.4 → 🟡 ** 33.9** (`-16.5`) | 78.5 → 47.9 (`-30.6`) | 41.3 → 19.8 (`-21.5`) | 31.3 → 0.0 (`-31.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_COST_MINUS1` | CAA-10 (Echo Alhambry): cost 1 → 0 | 50.4 → 🟢 ** 51.2** (`⬆️ +0.8`) | 78.5 → 71.4 (`-7.1`) | 41.3 → 38.5 (`-2.8`) | 31.3 → 43.8 (`⬆️ +12.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_CAA-10_HERESY_PLUS1` | CAA-10 (Echo Alhambry): heresy 1 → 2 | 50.4 → 🟡 ** 31.8** (`-18.6`) | 78.5 → 60.4 (`-18.1`) | 41.3 → 20.6 (`-20.7`) | 31.3 → 14.4 (`-16.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_CAA-10_HERESY_MINUS1` | CAA-10 (Echo Alhambry): heresy 1 → 0 | 50.4 → 🟡 ** 49.8** (`-0.6`) | 78.5 → 66.9 (`-11.6`) | 41.3 → 46.0 (`⬆️ +4.7`) | 31.3 → 36.4 (`⬆️ +5.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_COST_PLUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 2 | 50.4 → 🟡 ** 49.2** (`-1.2`) | 78.5 → 74.2 (`-4.3`) | 41.3 → 46.9 (`⬆️ +5.6`) | 31.3 → 26.6 (`-4.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_COST_MINUS1` | GC-01 (Przekupiony Strażnik): cost 1 → 0 | 50.4 → 🟡 ** 42.5** (`-7.9`) | 78.5 → 69.8 (`-8.7`) | 41.3 → 15.2 (`-26.1`) | 31.3 → 0.0 (`-31.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-01_HERESY_PLUS1` | GC-01 (Przekupiony Strażnik): heresy 0 → 1 | 50.4 → 🟢 ** 58.5** (`⬆️ +8.1`) | 78.5 → 78.0 (`-0.5`) | 41.3 → 46.2 (`⬆️ +4.9`) | 31.3 → 51.4 (`⬆️ +20.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-02_COST_PLUS1` | GC-02 (Czarny Rynek): cost 1 → 2 | 50.4 → 🟢 ** 66.2** (`⬆️ +15.8`) | 78.5 → 79.0 (`⬆️ +0.5`) | 41.3 → 53.3 (`⬆️ +12.0`) | 31.3 → 0.0 (`-31.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-02_COST_MINUS1` | GC-02 (Czarny Rynek): cost 1 → 0 | 50.4 → 🟡 ** 43.3** (`-7.1`) | 78.5 → 72.1 (`-6.4`) | 41.3 → 14.6 (`-26.7`) | 31.3 → 43.1 (`⬆️ +11.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-02_HERESY_PLUS1` | GC-02 (Czarny Rynek): heresy 0 → 1 | 50.4 → 🟢 ** 58.8** (`⬆️ +8.4`) | 78.5 → 76.4 (`-2.1`) | 41.3 → 42.8 (`⬆️ +1.5`) | 31.3 → 57.1 (`⬆️ +25.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-03_COST_PLUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 2 | 50.4 → 🟢 ** 53.9** (`⬆️ +3.5`) | 78.5 → 79.8 (`⬆️ +1.3`) | 41.3 → 41.9 (`⬆️ +0.6`) | 31.3 → 40.1 (`⬆️ +8.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-03_COST_MINUS1` | GC-03 (Podrzucenie Księgi): cost 1 → 0 | 50.4 → 🟡 ** 43.7** (`-6.7`) | 78.5 → 76.4 (`-2.1`) | 41.3 → 17.7 (`-23.6`) | 31.3 → 36.9 (`⬆️ +5.6`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-03_HERESY_PLUS1` | GC-03 (Podrzucenie Księgi): heresy 0 → 1 | 50.4 → 🟢 ** 61.8** (`⬆️ +11.4`) | 78.5 → 81.7 (`⬆️ +3.2`) | 41.3 → 48.2 (`⬆️ +6.9`) | 31.3 → 55.5 (`⬆️ +24.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-04_COST_PLUS1` | GC-04 (Informator): cost 1 → 2 | 50.4 → 🟢 ** 55.2** (`⬆️ +4.8`) | 78.5 → 74.7 (`-3.8`) | 41.3 → 35.7 (`-5.6`) | 31.3 → 0.0 (`-31.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-04_COST_MINUS1` | GC-04 (Informator): cost 1 → 0 | 50.4 → 🟡 ** 48.6** (`-1.8`) | 78.5 → 68.1 (`-10.4`) | 41.3 → 39.0 (`-2.3`) | 31.3 → 38.7 (`⬆️ +7.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-04_HERESY_PLUS1` | GC-04 (Informator): heresy 1 → 2 | 50.4 → 🟢 ** 61.3** (`⬆️ +10.9`) | 78.5 → 76.0 (`-2.5`) | 41.3 → 54.8 (`⬆️ +13.5`) | 31.3 → 53.1 (`⬆️ +21.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-04_HERESY_MINUS1` | GC-04 (Informator): heresy 1 → 0 | 50.4 → 🟡 ** 43.1** (`-7.3`) | 78.5 → 74.1 (`-4.4`) | 41.3 → 12.1 (`-29.2`) | 31.3 → 0.0 (`-31.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-05_COST_PLUS1` | GC-05 (Fałszywy Świadek): cost 0 → 1 | 🟢 ** 50.4** | 78.5 | 41.3 | 31.3 | ⚪ OPTYMALNY |
| `L3_GC-05_HERESY_PLUS1` | GC-05 (Fałszywy Świadek): heresy 0 → 1 | 🟢 ** 50.4** | 78.5 | 41.3 | 31.3 | ⚪ OPTYMALNY |
| `L3_GC-06_COST_PLUS1` | GC-06 (Szantaż): cost 2 → 3 | 50.4 → 🟢 ** 52.3** (`⬆️ +1.9`) | 78.5 → 74.2 (`-4.3`) | 41.3 → 47.9 (`⬆️ +6.6`) | 31.3 → 34.9 (`⬆️ +3.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-06_COST_MINUS1` | GC-06 (Szantaż): cost 2 → 1 | 50.4 → 🟡 ** 44.3** (`-6.1`) | 78.5 → 73.5 (`-5.0`) | 41.3 → 15.1 (`-26.2`) | 31.3 → 0.0 (`-31.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-06_HERESY_PLUS1` | GC-06 (Szantaż): heresy 0 → 1 | 50.4 → 🟢 ** 53.8** (`⬆️ +3.4`) | 78.5 → 77.8 (`-0.7`) | 41.3 → 42.2 (`⬆️ +0.9`) | 31.3 → 41.4 (`⬆️ +10.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-07_COST_PLUS1` | GC-07 (Skrytobójstwo): cost 2 → 3 | 50.4 → 🟡 ** 48.2** (`-2.2`) | 78.5 → 78.0 (`-0.5`) | 41.3 → 28.2 (`-13.1`) | 31.3 → 38.3 (`⬆️ +7.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_COST_MINUS1` | GC-07 (Skrytobójstwo): cost 2 → 1 | 50.4 → 🟡 ** 48.4** (`-2.0`) | 78.5 → 74.9 (`-3.6`) | 41.3 → 20.8 (`-20.5`) | 31.3 → 49.5 (`⬆️ +18.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-07_HERESY_PLUS1` | GC-07 (Skrytobójstwo): heresy 1 → 2 | 50.4 → 🟢 ** 52.9** (`⬆️ +2.5`) | 78.5 → 78.1 (`-0.4`) | 41.3 → 46.2 (`⬆️ +4.9`) | 31.3 → 34.5 (`⬆️ +3.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-07_HERESY_MINUS1` | GC-07 (Skrytobójstwo): heresy 1 → 0 | 50.4 → 🟡 ** 45.8** (`-4.6`) | 78.5 → 76.9 (`-1.6`) | 41.3 → 38.9 (`-2.4`) | 31.3 → 21.6 (`-9.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_COST_PLUS1` | GC-08 (Zatrute Złoto): cost 1 → 2 | 🟢 ** 50.4** | 78.5 → 74.0 (`-4.5`) | 41.3 → 29.8 (`-11.5`) | 31.3 → 47.4 (`⬆️ +16.1`) | ⚪ OPTYMALNY |
| `L3_GC-08_COST_MINUS1` | GC-08 (Zatrute Złoto): cost 1 → 0 | 50.4 → 🟡 ** 47.5** (`-2.9`) | 78.5 → 75.1 (`-3.4`) | 41.3 → 19.9 (`-21.4`) | 31.3 → 0.0 (`-31.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-08_HERESY_PLUS1` | GC-08 (Zatrute Złoto): heresy 0 → 1 | 50.4 → 🟢 ** 57.4** (`⬆️ +7.0`) | 78.5 → 78.2 (`-0.3`) | 41.3 → 46.6 (`⬆️ +5.3`) | 31.3 → 47.3 (`⬆️ +16.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-09_COST_PLUS1` | GC-09 (Lista Dłużników): cost 2 → 3 | 50.4 → 🟢 ** 51.6** (`⬆️ +1.2`) | 78.5 → 75.1 (`-3.4`) | 41.3 → 38.0 (`-3.3`) | 31.3 → 41.8 (`⬆️ +10.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-09_COST_MINUS1` | GC-09 (Lista Dłużników): cost 2 → 1 | 50.4 → 🟡 ** 41.1** (`-9.3`) | 78.5 → 85.6 (`⬆️ +7.1`) | 41.3 → 19.7 (`-21.6`) | 31.3 → 17.9 (`-13.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_GC-09_HERESY_PLUS1` | GC-09 (Lista Dłużników): heresy 0 → 1 | 50.4 → 🟢 ** 62.3** (`⬆️ +11.9`) | 78.5 → 80.9 (`⬆️ +2.4`) | 41.3 → 58.0 (`⬆️ +16.7`) | 31.3 → 47.9 (`⬆️ +16.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-10_COST_PLUS1` | GC-10 (Upadek Domu): cost 3 → 4 | 50.4 → 🟢 ** 55.0** (`⬆️ +4.6`) | 78.5 → 70.4 (`-8.1`) | 41.3 → 39.5 (`-1.8`) | 31.3 → 0.0 (`-31.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-10_COST_MINUS1` | GC-10 (Upadek Domu): cost 3 → 2 | 50.4 → 🟢 ** 53.1** (`⬆️ +2.7`) | 78.5 → 77.4 (`-1.1`) | 41.3 → 28.7 (`-12.6`) | 31.3 → 0.0 (`-31.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-10_HERESY_PLUS1` | GC-10 (Upadek Domu): heresy 2 → 3 | 50.4 → 🟢 ** 69.4** (`⬆️ +19.0`) | 78.5 → 69.3 (`-9.2`) | 41.3 → 72.8 (`⬆️ +31.5`) | 31.3 → 66.0 (`⬆️ +34.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_GC-10_HERESY_MINUS1` | GC-10 (Upadek Domu): heresy 2 → 1 | 50.4 → 🟡 ** 40.0** (`-10.4`) | 78.5 → 70.8 (`-7.7`) | 41.3 → 9.3 (`-32.0`) | 31.3 → 0.0 (`-31.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-01_COST_PLUS1` | KB-01 (Rozkaz Dworu): cost 1 → 2 | 50.4 → 🟢 ** 71.8** (`⬆️ +21.4`) | 78.5 → 89.4 (`⬆️ +10.9`) | 41.3 → 52.4 (`⬆️ +11.1`) | 31.3 → 73.7 (`⬆️ +42.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-01_COST_MINUS1` | KB-01 (Rozkaz Dworu): cost 1 → 0 | 50.4 → 🟢 ** 68.3** (`⬆️ +17.9`) | 78.5 → 88.7 (`⬆️ +10.2`) | 41.3 → 49.3 (`⬆️ +8.0`) | 31.3 → 66.9 (`⬆️ +35.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-01_HERESY_PLUS1` | KB-01 (Rozkaz Dworu): heresy 0 → 1 | 50.4 → 🟡 ** 48.3** (`-2.1`) | 78.5 → 72.1 (`-6.4`) | 41.3 → 24.6 (`-16.7`) | 31.3 → 0.0 (`-31.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_COST_PLUS1` | KB-02 (Pobór Podatków): cost 1 → 2 | 50.4 → 🟡 ** 35.3** (`-15.1`) | 78.5 → 50.0 (`-28.5`) | 41.3 → 20.6 (`-20.7`) | 31.3 → 0.0 (`-31.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-02_COST_MINUS1` | KB-02 (Pobór Podatków): cost 1 → 0 | 50.4 → 🟢 ** 62.2** (`⬆️ +11.8`) | 78.5 | 41.3 → 36.1 (`-5.2`) | 31.3 → 72.0 (`⬆️ +40.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-02_HERESY_PLUS1` | KB-02 (Pobór Podatków): heresy 0 → 1 | 50.4 → 🟢 ** 54.5** (`⬆️ +4.1`) | 78.5 → 70.8 (`-7.7`) | 41.3 → 38.1 (`-3.2`) | 31.3 → 0.0 (`-31.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-03_COST_PLUS1` | KB-03 (Plotka Dworska): cost 1 → 2 | 50.4 → 🟢 ** 69.2** (`⬆️ +18.8`) | 78.5 → 88.2 (`⬆️ +9.7`) | 41.3 → 44.4 (`⬆️ +3.1`) | 31.3 → 75.1 (`⬆️ +43.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-03_COST_MINUS1` | KB-03 (Plotka Dworska): cost 1 → 0 | 50.4 → 🟢 ** 59.0** (`⬆️ +8.6`) | 78.5 → 79.2 (`⬆️ +0.7`) | 41.3 → 39.9 (`-1.4`) | 31.3 → 57.8 (`⬆️ +26.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-03_HERESY_PLUS1` | KB-03 (Plotka Dworska): heresy 0 → 1 | 50.4 → 🟡 ** 37.1** (`-13.3`) | 78.5 → 69.8 (`-8.7`) | 41.3 → 12.8 (`-28.5`) | 31.3 → 28.8 (`-2.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-04_COST_PLUS1` | KB-04 (Faworyt Dworu): cost 1 → 2 | 50.4 → 🟢 ** 65.1** (`⬆️ +14.7`) | 78.5 → 85.3 (`⬆️ +6.8`) | 41.3 → 56.3 (`⬆️ +15.0`) | 31.3 → 53.7 (`⬆️ +22.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-04_COST_MINUS1` | KB-04 (Faworyt Dworu): cost 1 → 0 | 50.4 → 🟢 ** 61.3** (`⬆️ +10.9`) | 78.5 → 78.0 (`-0.5`) | 41.3 → 43.7 (`⬆️ +2.4`) | 31.3 → 62.1 (`⬆️ +30.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-04_HERESY_PLUS1` | KB-04 (Faworyt Dworu): heresy 1 → 2 | 50.4 → 🟢 ** 59.3** (`⬆️ +8.9`) | 78.5 → 68.4 (`-10.1`) | 41.3 → 50.2 (`⬆️ +8.9`) | 31.3 → 0.0 (`-31.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-04_HERESY_MINUS1` | KB-04 (Faworyt Dworu): heresy 1 → 0 | 50.4 → 🟢 ** 58.0** (`⬆️ +7.6`) | 78.5 → 85.4 (`⬆️ +6.9`) | 41.3 → 58.1 (`⬆️ +16.8`) | 31.3 → 30.5 (`-0.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-05_COST_PLUS1` | KB-05 (List Żelazny): cost 2 → 3 | 50.4 → 🟢 ** 64.9** (`⬆️ +14.5`) | 78.5 → 85.4 (`⬆️ +6.9`) | 41.3 → 57.2 (`⬆️ +15.9`) | 31.3 → 52.2 (`⬆️ +20.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-05_COST_MINUS1` | KB-05 (List Żelazny): cost 2 → 1 | 50.4 → 🟡 ** 49.5** (`-0.9`) | 78.5 → 65.4 (`-13.1`) | 41.3 → 28.4 (`-12.9`) | 31.3 → 54.8 (`⬆️ +23.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-05_HERESY_PLUS1` | KB-05 (List Żelazny): heresy 0 → 1 | 50.4 → 🟡 ** 47.0** (`-3.4`) | 78.5 → 72.3 (`-6.2`) | 41.3 → 38.8 (`-2.5`) | 31.3 → 29.8 (`-1.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-06_COST_PLUS1` | KB-06 (Areszt Królewski): cost 2 → 3 | 50.4 → 🟢 ** 64.7** (`⬆️ +14.3`) | 78.5 → 85.9 (`⬆️ +7.4`) | 41.3 → 49.6 (`⬆️ +8.3`) | 31.3 → 58.7 (`⬆️ +27.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-06_COST_MINUS1` | KB-06 (Areszt Królewski): cost 2 → 1 | 50.4 → 🟢 ** 57.6** (`⬆️ +7.2`) | 78.5 → 73.9 (`-4.6`) | 41.3 → 41.2 (`-0.1`) | 31.3 → 0.0 (`-31.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-06_HERESY_PLUS1` | KB-06 (Areszt Królewski): heresy 0 → 1 | 50.4 → 🟢 ** 51.1** (`⬆️ +0.7`) | 78.5 → 78.2 (`-0.3`) | 41.3 → 40.9 (`-0.4`) | 31.3 → 34.2 (`⬆️ +2.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-07_COST_PLUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 3 | 50.4 → 🟡 ** 44.1** (`-6.3`) | 78.5 → 68.6 (`-9.9`) | 41.3 → 19.6 (`-21.7`) | 31.3 → 0.0 (`-31.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-07_COST_MINUS1` | KB-07 (Szantaż Pieczęcią): cost 2 → 1 | 50.4 → 🟢 ** 54.4** (`⬆️ +4.0`) | 78.5 → 61.1 (`-17.4`) | 41.3 → 3.6 (`-37.7`) | 31.3 → 98.6 (`⬆️ +67.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-07_HERESY_PLUS1` | KB-07 (Szantaż Pieczęcią): heresy 0 → 1 | 50.4 → 🟡 ** 44.4** (`-6.0`) | 78.5 → 73.0 (`-5.5`) | 41.3 → 38.8 (`-2.5`) | 31.3 → 21.4 (`-9.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_COST_PLUS1` | KB-08 (Przekupstwo Sędziego): cost 3 → 4 | 50.4 → 🟡 ** 49.8** (`-0.6`) | 78.5 → 77.1 (`-1.4`) | 41.3 → 47.9 (`⬆️ +6.6`) | 31.3 → 24.5 (`-6.8`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-08_COST_MINUS1` | KB-08 (Przekupstwo Sędziego): cost 3 → 2 | 50.4 → 🟢 ** 67.6** (`⬆️ +17.2`) | 78.5 → 79.2 (`⬆️ +0.7`) | 41.3 → 51.4 (`⬆️ +10.1`) | 31.3 → 72.1 (`⬆️ +40.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-08_HERESY_PLUS1` | KB-08 (Przekupstwo Sędziego): heresy 0 → 1 | 50.4 → 🟡 ** 49.9** (`-0.5`) | 78.5 → 77.7 (`-0.8`) | 41.3 → 40.7 (`-0.6`) | 31.3 → 31.4 (`⬆️ +0.1`) | ⚪ OPTYMALNY |
| `L3_KB-09_COST_PLUS1` | KB-09 (Dekret Królewski): cost 3 → 4 | 50.4 → 🟡 ** 32.0** (`-18.4`) | 78.5 → 35.7 (`-42.8`) | 41.3 → 28.3 (`-13.0`) | 31.3 → 0.0 (`-31.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_COST_MINUS1` | KB-09 (Dekret Królewski): cost 3 → 2 | 50.4 → 🟢 ** 72.9** (`⬆️ +22.5`) | 78.5 → 84.4 (`⬆️ +5.9`) | 41.3 → 38.7 (`-2.6`) | 31.3 → 95.6 (`⬆️ +64.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-09_HERESY_PLUS1` | KB-09 (Dekret Królewski): heresy 1 → 2 | 50.4 → 🟡 ** 45.8** (`-4.6`) | 78.5 → 70.9 (`-7.6`) | 41.3 → 29.0 (`-12.3`) | 31.3 → 37.4 (`⬆️ +6.1`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-09_HERESY_MINUS1` | KB-09 (Dekret Królewski): heresy 1 → 0 | 50.4 → 🟢 ** 66.8** (`⬆️ +16.4`) | 78.5 → 89.8 (`⬆️ +11.3`) | 41.3 → 51.7 (`⬆️ +10.4`) | 31.3 → 58.9 (`⬆️ +27.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KB-10_COST_PLUS1` | KB-10 (Pieczęć Korony): cost 2 → 3 | 50.4 → 🟡 ** 27.8** (`-22.6`) | 78.5 → 35.7 (`-42.8`) | 41.3 → 19.9 (`-21.4`) | 31.3 → 0.0 (`-31.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_COST_MINUS1` | KB-10 (Pieczęć Korony): cost 2 → 1 | 50.4 → 🟢 ** 50.2** (`-0.2`) | 78.5 → 51.7 (`-26.8`) | 41.3 → 16.1 (`-25.2`) | 31.3 → 82.8 (`⬆️ +51.5`) | ⚪ OPTYMALNY |
| `L3_KB-10_HERESY_PLUS1` | KB-10 (Pieczęć Korony): heresy 2 → 3 | 50.4 → 🟡 ** 38.0** (`-12.4`) | 78.5 → 58.7 (`-19.8`) | 41.3 → 17.3 (`-24.0`) | 31.3 → 0.0 (`-31.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KB-10_HERESY_MINUS1` | KB-10 (Pieczęć Korony): heresy 2 → 1 | 50.4 → 🟢 ** 59.5** (`⬆️ +9.1`) | 78.5 → 78.9 (`⬆️ +0.4`) | 41.3 → 48.9 (`⬆️ +7.6`) | 31.3 → 50.7 (`⬆️ +19.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-01_COST_PLUS1` | KT-01 (Rytuał Przejścia): cost 1 → 2 | 50.4 → 🟢 ** 58.6** (`⬆️ +8.2`) | 78.5 → 77.8 (`-0.7`) | 41.3 → 27.3 (`-14.0`) | 31.3 → 70.7 (`⬆️ +39.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-01_COST_MINUS1` | KT-01 (Rytuał Przejścia): cost 1 → 0 | 50.4 → 🟡 ** 49.6** (`-0.8`) | 78.5 → 77.5 (`-1.0`) | 41.3 → 38.3 (`-3.0`) | 31.3 → 33.0 (`⬆️ +1.7`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-01_HERESY_PLUS1` | KT-01 (Rytuał Przejścia): heresy 0 → 1 | 50.4 → 🟢 ** 52.4** (`⬆️ +2.0`) | 78.5 → 80.3 (`⬆️ +1.8`) | 41.3 → 45.1 (`⬆️ +3.8`) | 31.3 → 31.9 (`⬆️ +0.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-02_COST_PLUS1` | KT-02 (Transmutacja Złota): cost 1 → 2 | 50.4 → 🟢 ** 57.4** (`⬆️ +7.0`) | 78.5 → 78.9 (`⬆️ +0.4`) | 41.3 → 48.9 (`⬆️ +7.6`) | 31.3 → 44.5 (`⬆️ +13.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-02_COST_MINUS1` | KT-02 (Transmutacja Złota): cost 1 → 0 | 50.4 → 🟢 ** 54.4** (`⬆️ +4.0`) | 78.5 → 77.8 (`-0.7`) | 41.3 | 31.3 → 44.0 (`⬆️ +12.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-02_HERESY_PLUS1` | KT-02 (Transmutacja Złota): heresy 0 → 1 | 50.4 → 🟢 ** 59.2** (`⬆️ +8.8`) | 78.5 → 81.4 (`⬆️ +2.9`) | 41.3 → 47.9 (`⬆️ +6.6`) | 31.3 → 48.4 (`⬆️ +17.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-03_COST_PLUS1` | KT-03 (Zakazana Wiedza): cost 0 → 1 | 50.4 → 🟢 ** 61.1** (`⬆️ +10.7`) | 78.5 → 85.2 (`⬆️ +6.7`) | 41.3 → 39.4 (`-1.9`) | 31.3 → 58.8 (`⬆️ +27.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-03_HERESY_PLUS1` | KT-03 (Zakazana Wiedza): heresy 1 → 2 | 50.4 → 🟢 ** 66.4** (`⬆️ +16.0`) | 78.5 → 85.4 (`⬆️ +6.9`) | 41.3 → 65.3 (`⬆️ +24.0`) | 31.3 → 48.4 (`⬆️ +17.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-03_HERESY_MINUS1` | KT-03 (Zakazana Wiedza): heresy 1 → 0 | 50.4 → 🟢 ** 59.6** (`⬆️ +9.2`) | 78.5 → 77.0 (`-1.5`) | 41.3 → 50.2 (`⬆️ +8.9`) | 31.3 → 51.5 (`⬆️ +20.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-04_COST_PLUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 2 | 50.4 → 🟢 ** 55.2** (`⬆️ +4.8`) | 78.5 → 82.9 (`⬆️ +4.4`) | 41.3 → 38.7 (`-2.6`) | 31.3 → 43.9 (`⬆️ +12.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-04_COST_MINUS1` | KT-04 (Zwierciadło Herezji): cost 1 → 0 | 50.4 → 🟡 ** 47.9** (`-2.5`) | 78.5 | 41.3 → 42.4 (`⬆️ +1.1`) | 31.3 → 22.8 (`-8.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-04_HERESY_PLUS1` | KT-04 (Zwierciadło Herezji): heresy 0 → 1 | 50.4 → 🟢 ** 52.8** (`⬆️ +2.4`) | 78.5 → 81.0 (`⬆️ +2.5`) | 41.3 → 43.3 (`⬆️ +2.0`) | 31.3 → 34.0 (`⬆️ +2.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-05_COST_PLUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 2 | 50.4 → 🟢 ** 60.1** (`⬆️ +9.7`) | 78.5 → 78.8 (`⬆️ +0.3`) | 41.3 → 42.8 (`⬆️ +1.5`) | 31.3 → 58.6 (`⬆️ +27.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-05_COST_MINUS1` | KT-05 (Wskazówka Cyklu): cost 1 → 0 | 50.4 → 🟢 ** 55.6** (`⬆️ +5.2`) | 78.5 → 77.7 (`-0.8`) | 41.3 → 46.3 (`⬆️ +5.0`) | 31.3 → 42.7 (`⬆️ +11.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-05_HERESY_PLUS1` | KT-05 (Wskazówka Cyklu): heresy 0 → 1 | 50.4 → 🟢 ** 57.5** (`⬆️ +7.1`) | 78.5 → 80.5 (`⬆️ +2.0`) | 41.3 → 52.4 (`⬆️ +11.1`) | 31.3 → 39.5 (`⬆️ +8.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-06_COST_PLUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 3 | 50.4 → 🟢 ** 53.4** (`⬆️ +3.0`) | 78.5 → 83.7 (`⬆️ +5.2`) | 41.3 → 34.5 (`-6.8`) | 31.3 → 42.1 (`⬆️ +10.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-06_COST_MINUS1` | KT-06 (Przesłuchanie Imienia): cost 2 → 1 | 50.4 → 🟢 ** 52.2** (`⬆️ +1.8`) | 78.5 → 77.6 (`-0.9`) | 41.3 → 39.0 (`-2.3`) | 31.3 → 40.0 (`⬆️ +8.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-06_HERESY_PLUS1` | KT-06 (Przesłuchanie Imienia): heresy 0 → 1 | 50.4 → 🟢 ** 53.2** (`⬆️ +2.8`) | 78.5 → 78.3 (`-0.2`) | 41.3 → 49.4 (`⬆️ +8.1`) | 31.3 → 31.8 (`⬆️ +0.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-07_COST_PLUS1` | KT-07 (Archiwum Ukryte): cost 1 → 2 | 50.4 → 🟢 ** 62.0** (`⬆️ +11.6`) | 78.5 → 79.4 (`⬆️ +0.9`) | 41.3 → 37.7 (`-3.6`) | 31.3 → 68.8 (`⬆️ +37.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-07_COST_MINUS1` | KT-07 (Archiwum Ukryte): cost 1 → 0 | 50.4 → 🟢 ** 57.3** (`⬆️ +6.9`) | 78.5 → 77.7 (`-0.8`) | 41.3 → 41.0 (`-0.3`) | 31.3 → 53.2 (`⬆️ +21.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-07_HERESY_PLUS1` | KT-07 (Archiwum Ukryte): heresy 0 → 1 | 50.4 → 🟢 ** 54.1** (`⬆️ +3.7`) | 78.5 → 81.1 (`⬆️ +2.6`) | 41.3 → 46.0 (`⬆️ +4.7`) | 31.3 → 35.1 (`⬆️ +3.8`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-08_COST_PLUS1` | KT-08 (Areszt Wiedzy): cost 2 → 3 | 50.4 → 🟢 ** 58.6** (`⬆️ +8.2`) | 78.5 → 83.7 (`⬆️ +5.2`) | 41.3 → 40.2 (`-1.1`) | 31.3 → 51.9 (`⬆️ +20.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-08_COST_MINUS1` | KT-08 (Areszt Wiedzy): cost 2 → 1 | 50.4 → 🟢 ** 57.3** (`⬆️ +6.9`) | 78.5 → 77.0 (`-1.5`) | 41.3 → 46.2 (`⬆️ +4.9`) | 31.3 → 48.8 (`⬆️ +17.5`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-08_HERESY_PLUS1` | KT-08 (Areszt Wiedzy): heresy 0 → 1 | 50.4 → 🟢 ** 57.0** (`⬆️ +6.6`) | 78.5 → 80.3 (`⬆️ +1.8`) | 41.3 → 45.1 (`⬆️ +3.8`) | 31.3 → 45.5 (`⬆️ +14.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-09_COST_PLUS1` | KT-09 (Fragment Kodeksu): cost 1 → 2 | 50.4 → 🟢 ** 66.6** (`⬆️ +16.2`) | 78.5 → 81.6 (`⬆️ +3.1`) | 41.3 → 53.9 (`⬆️ +12.6`) | 31.3 → 64.4 (`⬆️ +33.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-09_COST_MINUS1` | KT-09 (Fragment Kodeksu): cost 1 → 0 | 50.4 → 🟡 ** 48.5** (`-1.9`) | 78.5 → 77.3 (`-1.2`) | 41.3 → 38.9 (`-2.4`) | 31.3 → 29.3 (`-2.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-09_HERESY_PLUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 2 | 50.4 → 🟢 ** 65.6** (`⬆️ +15.2`) | 78.5 → 79.8 (`⬆️ +1.3`) | 41.3 → 50.9 (`⬆️ +9.6`) | 31.3 → 66.2 (`⬆️ +34.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-09_HERESY_MINUS1` | KT-09 (Fragment Kodeksu): heresy 1 → 0 | 50.4 → 🟢 ** 54.7** (`⬆️ +4.3`) | 78.5 → 75.7 (`-2.8`) | 41.3 → 48.7 (`⬆️ +7.4`) | 31.3 → 39.7 (`⬆️ +8.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-10_COST_PLUS1` | KT-10 (Pieczęć Salomona): cost 1 → 2 | 50.4 → 🟢 ** 65.8** (`⬆️ +15.4`) | 78.5 → 78.8 (`⬆️ +0.3`) | 41.3 → 58.1 (`⬆️ +16.8`) | 31.3 → 60.6 (`⬆️ +29.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_KT-10_COST_MINUS1` | KT-10 (Pieczęć Salomona): cost 1 → 0 | 50.4 → 🟡 ** 48.5** (`-1.9`) | 78.5 → 77.4 (`-1.1`) | 41.3 → 37.4 (`-3.9`) | 31.3 → 30.8 (`-0.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_KT-10_HERESY_PLUS1` | KT-10 (Pieczęć Salomona): heresy 0 → 1 | 50.4 → 🟢 ** 66.4** (`⬆️ +16.0`) | 78.5 → 77.2 (`-1.3`) | 41.3 → 49.6 (`⬆️ +8.3`) | 31.3 → 72.5 (`⬆️ +41.2`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-01_COST_PLUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 2 | 50.4 → 🟢 ** 54.7** (`⬆️ +4.3`) | 78.5 → 79.3 (`⬆️ +0.8`) | 41.3 → 48.3 (`⬆️ +7.0`) | 31.3 → 36.4 (`⬆️ +5.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-01_COST_MINUS1` | SO-01 (Patrol Familiariuszy): cost 1 → 0 | 50.4 → 🟢 ** 56.9** (`⬆️ +6.5`) | 78.5 → 77.8 (`-0.7`) | 41.3 → 51.1 (`⬆️ +9.8`) | 31.3 → 41.7 (`⬆️ +10.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-01_HERESY_PLUS1` | SO-01 (Patrol Familiariuszy): heresy 0 → 1 | 50.4 → 🟢 ** 51.8** (`⬆️ +1.4`) | 78.5 → 76.6 (`-1.9`) | 41.3 → 44.3 (`⬆️ +3.0`) | 31.3 → 34.6 (`⬆️ +3.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-02_COST_PLUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 2 | 50.4 → 🟡 ** 44.4** (`-6.0`) | 78.5 → 75.0 (`-3.5`) | 41.3 → 25.6 (`-15.7`) | 31.3 → 32.6 (`⬆️ +1.3`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-02_COST_MINUS1` | SO-02 (Skarbiec Trybunału): cost 1 → 0 | 50.4 → 🟢 ** 63.4** (`⬆️ +13.0`) | 78.5 → 73.7 (`-4.8`) | 41.3 → 53.1 (`⬆️ +11.8`) | 31.3 → 0.0 (`-31.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-02_HERESY_PLUS1` | SO-02 (Skarbiec Trybunału): heresy 0 → 1 | 50.4 → 🟢 ** 55.8** (`⬆️ +5.4`) | 78.5 → 72.6 (`-5.9`) | 41.3 → 55.9 (`⬆️ +14.6`) | 31.3 → 39.0 (`⬆️ +7.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-03_COST_PLUS1` | SO-03 (Podejrzenie): cost 1 → 2 | 50.4 → 🟢 ** 59.8** (`⬆️ +9.4`) | 78.5 → 75.3 (`-3.2`) | 41.3 → 52.8 (`⬆️ +11.5`) | 31.3 → 51.4 (`⬆️ +20.1`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-03_COST_MINUS1` | SO-03 (Podejrzenie): cost 1 → 0 | 50.4 → 🟡 ** 47.5** (`-2.9`) | 78.5 → 79.9 (`⬆️ +1.4`) | 41.3 → 38.9 (`-2.4`) | 31.3 → 23.8 (`-7.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-03_HERESY_PLUS1` | SO-03 (Podejrzenie): heresy 0 → 1 | 50.4 → 🟢 ** 51.7** (`⬆️ +1.3`) | 78.5 → 69.4 (`-9.1`) | 41.3 → 57.0 (`⬆️ +15.7`) | 31.3 → 28.6 (`-2.7`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-04_COST_PLUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 2 | 50.4 → 🟢 ** 67.5** (`⬆️ +17.1`) | 78.5 → 78.3 (`-0.2`) | 41.3 → 56.6 (`⬆️ +15.3`) | 31.3 → 0.0 (`-31.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-04_COST_MINUS1` | SO-04 (Publiczne Ostrzeżenie): cost 1 → 0 | 50.4 → 🟢 ** 54.1** (`⬆️ +3.7`) | 78.5 → 78.8 (`⬆️ +0.3`) | 41.3 → 41.7 (`⬆️ +0.4`) | 31.3 → 41.7 (`⬆️ +10.4`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-04_HERESY_PLUS1` | SO-04 (Publiczne Ostrzeżenie): heresy 0 → 1 | 50.4 → 🟢 ** 58.8** (`⬆️ +8.4`) | 78.5 → 68.8 (`-9.7`) | 41.3 → 48.9 (`⬆️ +7.6`) | 31.3 → 0.0 (`-31.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-05_COST_PLUS1` | SO-05 (Wezwanie do Trybunału): cost 0 → 1 | 🟢 ** 50.4** | 78.5 | 41.3 | 31.3 | ⚪ OPTYMALNY |
| `L3_SO-05_HERESY_PLUS1` | SO-05 (Wezwanie do Trybunału): heresy 0 → 1 | 🟢 ** 50.4** | 78.5 | 41.3 | 31.3 | ⚪ OPTYMALNY |
| `L3_SO-06_COST_PLUS1` | SO-06 (Areszt Trybunalski): cost 2 → 3 | 50.4 → 🟢 ** 50.5** (`⬆️ +0.1`) | 78.5 → 77.7 (`-0.8`) | 41.3 → 40.1 (`-1.2`) | 31.3 → 33.6 (`⬆️ +2.3`) | ⚪ OPTYMALNY |
| `L3_SO-06_COST_MINUS1` | SO-06 (Areszt Trybunalski): cost 2 → 1 | 50.4 → 🟢 ** 62.0** (`⬆️ +11.6`) | 78.5 → 76.1 (`-2.4`) | 41.3 → 58.5 (`⬆️ +17.2`) | 31.3 → 51.3 (`⬆️ +20.0`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-06_HERESY_PLUS1` | SO-06 (Areszt Trybunalski): heresy 0 → 1 | 50.4 → 🟢 ** 50.1** (`-0.3`) | 78.5 → 79.0 (`⬆️ +0.5`) | 41.3 → 43.2 (`⬆️ +1.9`) | 31.3 → 28.1 (`-3.2`) | ⚪ OPTYMALNY |
| `L3_SO-07_COST_PLUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 3 | 50.4 → 🟡 ** 46.1** (`-4.3`) | 78.5 → 78.9 (`⬆️ +0.4`) | 41.3 → 47.1 (`⬆️ +5.8`) | 31.3 → 12.4 (`-18.9`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-07_COST_MINUS1` | SO-07 (Przesłuchanie Oficjum): cost 2 → 1 | 50.4 → 🟢 ** 58.0** (`⬆️ +7.6`) | 78.5 → 74.3 (`-4.2`) | 41.3 → 32.9 (`-8.4`) | 31.3 → 66.9 (`⬆️ +35.6`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-07_HERESY_PLUS1` | SO-07 (Przesłuchanie Oficjum): heresy 0 → 1 | 50.4 → 🟡 ** 48.7** (`-1.7`) | 78.5 → 73.7 (`-4.8`) | 41.3 → 44.3 (`⬆️ +3.0`) | 31.3 → 28.1 (`-3.2`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_COST_PLUS1` | SO-08 (Nasłanie Inkwizytora): cost 2 → 3 | 50.4 → 🟢 ** 55.5** (`⬆️ +5.1`) | 78.5 → 76.0 (`-2.5`) | 41.3 → 35.1 (`-6.2`) | 31.3 → 0.0 (`-31.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-08_COST_MINUS1` | SO-08 (Nasłanie Inkwizytora): cost 2 → 1 | 50.4 → 🟢 ** 53.9** (`⬆️ +3.5`) | 78.5 → 75.6 (`-2.9`) | 41.3 → 32.2 (`-9.1`) | 31.3 → 0.0 (`-31.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-08_HERESY_PLUS1` | SO-08 (Nasłanie Inkwizytora): heresy 1 → 2 | 50.4 → 🟡 ** 46.3** (`-4.1`) | 78.5 → 69.8 (`-8.7`) | 41.3 → 36.7 (`-4.6`) | 31.3 → 32.3 (`⬆️ +1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-08_HERESY_MINUS1` | SO-08 (Nasłanie Inkwizytora): heresy 1 → 0 | 50.4 → 🟡 ** 45.7** (`-4.7`) | 78.5 → 76.5 (`-2.0`) | 41.3 → 34.8 (`-6.5`) | 31.3 → 25.8 (`-5.5`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-09_COST_PLUS1` | SO-09 (Świadek Koronny): cost 2 → 3 | 50.4 → 🟢 ** 67.2** (`⬆️ +16.8`) | 78.5 → 77.5 (`-1.0`) | 41.3 → 56.9 (`⬆️ +15.6`) | 31.3 → 0.0 (`-31.3`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-09_COST_MINUS1` | SO-09 (Świadek Koronny): cost 2 → 1 | 50.4 → 🟢 ** 59.5** (`⬆️ +9.1`) | 78.5 → 77.2 (`-1.3`) | 41.3 → 36.0 (`-5.3`) | 31.3 → 65.2 (`⬆️ +33.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-09_HERESY_PLUS1` | SO-09 (Świadek Koronny): heresy 0 → 1 | 50.4 → 🟢 ** 52.1** (`⬆️ +1.7`) | 78.5 → 78.9 (`⬆️ +0.4`) | 41.3 → 42.1 (`⬆️ +0.8`) | 31.3 → 35.2 (`⬆️ +3.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-10_COST_PLUS1` | SO-10 (Oczyść Miasto): cost 4 → 5 | 50.4 → 🟡 ** 38.5** (`-11.9`) | 78.5 → 56.1 (`-22.4`) | 41.3 → 27.1 (`-14.2`) | 31.3 → 32.3 (`⬆️ +1.0`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_COST_MINUS1` | SO-10 (Oczyść Miasto): cost 4 → 3 | 50.4 → 🟡 ** 48.7** (`-1.7`) | 78.5 → 78.4 (`-0.1`) | 41.3 → 31.0 (`-10.3`) | 31.3 → 36.7 (`⬆️ +5.4`) | 🔴 POGARSZA GLOBALNIE |
| `L3_SO-10_HERESY_PLUS1` | SO-10 (Oczyść Miasto): heresy 2 → 3 | 50.4 → 🟢 ** 61.4** (`⬆️ +11.0`) | 78.5 → 76.0 (`-2.5`) | 41.3 → 64.1 (`⬆️ +22.8`) | 31.3 → 44.2 (`⬆️ +12.9`) | 🟢 POPRAWIA GLOBALNIE |
| `L3_SO-10_HERESY_MINUS1` | SO-10 (Oczyść Miasto): heresy 2 → 1 | 50.4 → 🟡 ** 42.3** (`-8.1`) | 78.5 → 71.5 (`-7.0`) | 41.3 → 28.5 (`-12.8`) | 31.3 → 26.8 (`-4.5`) | 🔴 POGARSZA GLOBALNIE |

## 2. Pełna Tabela Telemetrii 5 Filarów z Zakresami (Min / Średnia / Max) i Zgodnością Norm

| ID | Długość Gry (Ery) [Min–Max] | Deadlocks % (<15%) | Pas Biedy % (<30%) | Autodafé / Partię [Min–Max] | Oskarżenia / Partię [Min–Max] | Złoto End [Min–Max] | Herezja End [Min–Max] | Weryfikacja Norm Telemetrii |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `L3_BAZA` | 5.59 Er (1–9) | 3.4% | 28.6% | 1.03 (0–3) | 3.70 (0–15) | 0.54zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_COST_PLUS1` | 5.62 Er (1–9) | 3.5% | 30.1% | 1.03 (0–4) | 3.77 (0–17) | 0.57zł (0.0–2.7) | 6.27 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-01_COST_MINUS1` | 5.56 Er (1–9) | 3.1% | 28.3% | 1.03 (0–3) | 3.67 (0–17) | 0.57zł (0.0–2.7) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-01_HERESY_PLUS1` | 5.57 Er (1–9) | 3.3% | 28.6% | 1.02 (0–3) | 3.77 (0–16) | 0.53zł (0.0–2.7) | 6.34 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_COST_PLUS1` | 5.63 Er (1–9) | 4.0% | 31.1% | 1.03 (0–3) | 3.78 (0–17) | 0.56zł (0.0–2.3) | 6.28 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-02_COST_MINUS1` | 5.56 Er (1–9) | 3.3% | 28.3% | 1.03 (0–4) | 3.68 (0–17) | 0.59zł (0.0–3.0) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-02_HERESY_PLUS1` | 5.58 Er (1–9) | 3.2% | 28.6% | 1.03 (0–3) | 3.79 (0–15) | 0.53zł (0.0–2.7) | 6.37 (1.3–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_COST_PLUS1` | 5.65 Er (1–9) | 3.9% | 30.0% | 1.04 (0–4) | 3.74 (0–15) | 0.54zł (0.0–2.7) | 6.23 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-03_COST_MINUS1` | 5.57 Er (1–9) | 3.0% | 28.4% | 1.02 (0–4) | 3.71 (0–17) | 0.57zł (0.0–2.7) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_HERESY_PLUS1` | 5.57 Er (1–9) | 3.1% | 28.6% | 1.02 (0–3) | 3.82 (0–15) | 0.53zł (0.0–2.7) | 6.38 (1.4–10.0) | 🟢 W NORMIE |
| `L3_CAA-03_HERESY_MINUS1` | 5.62 Er (1–9) | 3.4% | 28.8% | 1.03 (0–3) | 3.62 (0–17) | 0.53zł (0.0–2.7) | 6.08 (1.0–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_COST_PLUS1` | 5.64 Er (1–9) | 3.6% | 30.1% | 1.04 (0–3) | 3.70 (0–17) | 0.56zł (0.0–2.7) | 6.24 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-04_COST_MINUS1` | 5.55 Er (1–9) | 3.1% | 28.4% | 1.03 (0–3) | 3.68 (0–17) | 0.57zł (0.0–2.7) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-04_HERESY_PLUS1` | 5.57 Er (1–9) | 3.3% | 28.6% | 1.02 (0–3) | 3.79 (0–16) | 0.53zł (0.0–2.7) | 6.36 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_COST_PLUS1` | 5.65 Er (1–9) | 4.0% | 30.0% | 1.04 (0–3) | 3.72 (0–15) | 0.54zł (0.0–2.7) | 6.25 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-05_COST_MINUS1` | 5.55 Er (1–9) | 2.9% | 28.3% | 1.02 (0–3) | 3.67 (0–17) | 0.57zł (0.0–2.7) | 6.22 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-05_HERESY_PLUS1` | 5.57 Er (1–9) | 3.2% | 28.6% | 1.02 (0–3) | 3.81 (0–15) | 0.53zł (0.0–2.7) | 6.37 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_COST_PLUS1` | 5.62 Er (1–9) | 3.7% | 29.0% | 1.03 (0–4) | 3.76 (0–16) | 0.54zł (0.0–2.7) | 6.29 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_COST_MINUS1` | 5.56 Er (1–9) | 3.1% | 28.5% | 1.02 (0–3) | 3.67 (0–17) | 0.54zł (0.0–2.7) | 6.18 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-06_HERESY_PLUS1` | 5.58 Er (1–9) | 3.4% | 28.6% | 1.03 (0–3) | 3.73 (0–15) | 0.53zł (0.0–2.7) | 6.30 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_COST_PLUS1` | 5.59 Er (1–9) | 3.2% | 29.3% | 1.03 (0–3) | 3.68 (0–16) | 0.54zł (0.0–2.7) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_COST_MINUS1` | 5.55 Er (1–9) | 2.9% | 28.5% | 1.02 (0–3) | 3.67 (0–15) | 0.55zł (0.0–2.3) | 6.19 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-07_HERESY_PLUS1` | 5.57 Er (1–9) | 3.1% | 28.6% | 1.03 (0–3) | 3.79 (0–15) | 0.53zł (0.0–2.7) | 6.35 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_COST_PLUS1` | 5.60 Er (1–9) | 3.4% | 30.2% | 1.03 (0–4) | 3.66 (0–16) | 0.59zł (0.0–2.7) | 6.17 (1.3–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-08_COST_MINUS1` | 5.58 Er (1–9) | 3.2% | 28.4% | 1.03 (0–3) | 3.75 (0–17) | 0.59zł (0.0–2.7) | 6.29 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_HERESY_PLUS1` | 5.57 Er (1–9) | 3.1% | 28.6% | 1.02 (0–3) | 3.72 (0–15) | 0.54zł (0.0–2.7) | 6.31 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-08_HERESY_MINUS1` | 5.60 Er (1–9) | 3.5% | 28.7% | 1.03 (0–3) | 3.66 (0–15) | 0.53zł (0.0–2.7) | 6.16 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_COST_PLUS1` | 5.67 Er (1–9) | 3.7% | 29.1% | 1.04 (0–3) | 3.73 (0–15) | 0.55zł (0.0–2.7) | 6.24 (1.3–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_COST_MINUS1` | 5.56 Er (1–9) | 3.1% | 28.0% | 1.03 (0–3) | 3.67 (0–15) | 0.56zł (0.0–2.7) | 6.20 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-09_HERESY_PLUS1` | 5.55 Er (1–9) | 3.0% | 28.5% | 1.02 (0–3) | 3.88 (0–15) | 0.53zł (0.0–2.7) | 6.43 (1.5–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_COST_PLUS1` | 5.70 Er (1–9) | 4.3% | 30.1% | 1.05 (0–3) | 3.80 (0–15) | 0.54zł (0.0–2.3) | 6.23 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_CAA-10_COST_MINUS1` | 5.56 Er (1–9) | 3.1% | 28.1% | 1.03 (0–3) | 3.70 (0–17) | 0.57zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_PLUS1` | 5.50 Er (1–9) | 2.9% | 28.4% | 1.01 (0–3) | 3.95 (0–18) | 0.53zł (0.0–2.7) | 6.45 (1.7–10.0) | 🟢 W NORMIE |
| `L3_CAA-10_HERESY_MINUS1` | 5.61 Er (1–9) | 3.6% | 28.7% | 1.03 (0–3) | 3.54 (0–17) | 0.54zł (0.0–3.0) | 5.83 (0.7–9.7) | 🟢 W NORMIE |
| `L3_GC-01_COST_PLUS1` | 5.59 Er (1–9) | 3.2% | 29.1% | 1.03 (0–3) | 3.70 (0–15) | 0.54zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-01_COST_MINUS1` | 5.56 Er (1–9) | 2.9% | 27.8% | 1.02 (0–3) | 3.68 (0–14) | 0.55zł (0.0–2.7) | 6.31 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-01_HERESY_PLUS1` | 5.57 Er (1–9) | 3.2% | 28.6% | 1.03 (0–3) | 3.73 (0–15) | 0.53zł (0.0–2.7) | 6.35 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-02_COST_PLUS1` | 5.65 Er (1–9) | 4.0% | 30.4% | 1.04 (0–3) | 3.75 (0–16) | 0.52zł (0.0–2.7) | 6.21 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_GC-02_COST_MINUS1` | 5.54 Er (1–9) | 3.0% | 27.8% | 1.02 (0–3) | 3.71 (0–16) | 0.56zł (0.0–2.7) | 6.31 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-02_HERESY_PLUS1` | 5.56 Er (1–9) | 3.3% | 28.5% | 1.02 (0–3) | 3.77 (0–15) | 0.54zł (0.0–3.0) | 6.36 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-03_COST_PLUS1` | 5.64 Er (1–9) | 3.5% | 29.3% | 1.03 (0–3) | 3.66 (0–15) | 0.53zł (0.0–2.7) | 6.22 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-03_COST_MINUS1` | 5.55 Er (1–9) | 3.2% | 27.8% | 1.02 (0–3) | 3.72 (0–14) | 0.55zł (0.0–2.7) | 6.32 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-03_HERESY_PLUS1` | 5.58 Er (1–9) | 3.4% | 28.6% | 1.03 (0–3) | 3.77 (0–15) | 0.53zł (0.0–2.7) | 6.36 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-04_COST_PLUS1` | 5.63 Er (1–9) | 3.7% | 29.3% | 1.04 (0–3) | 3.69 (0–16) | 0.54zł (0.0–2.7) | 6.19 (1.3–10.0) | 🟢 W NORMIE |
| `L3_GC-04_COST_MINUS1` | 5.55 Er (1–9) | 2.8% | 27.9% | 1.02 (0–3) | 3.77 (0–15) | 0.55zł (0.0–2.7) | 6.32 (1.4–10.0) | 🟢 W NORMIE |
| `L3_GC-04_HERESY_PLUS1` | 5.58 Er (1–9) | 3.3% | 28.5% | 1.03 (0–3) | 3.84 (0–18) | 0.54zł (0.0–2.7) | 6.38 (1.4–10.0) | 🟢 W NORMIE |
| `L3_GC-04_HERESY_MINUS1` | 5.61 Er (1–9) | 3.4% | 28.7% | 1.03 (0–3) | 3.60 (0–14) | 0.53zł (0.0–2.7) | 6.11 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-05_COST_PLUS1` | 5.59 Er (1–9) | 3.4% | 28.6% | 1.03 (0–3) | 3.70 (0–15) | 0.54zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-05_HERESY_PLUS1` | 5.59 Er (1–9) | 3.4% | 28.6% | 1.03 (0–3) | 3.70 (0–15) | 0.54zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-06_COST_PLUS1` | 5.63 Er (1–9) | 3.7% | 29.2% | 1.04 (0–4) | 3.80 (0–16) | 0.53zł (0.0–3.0) | 6.32 (1.3–10.0) | 🟢 W NORMIE |
| `L3_GC-06_COST_MINUS1` | 5.54 Er (1–9) | 2.9% | 28.0% | 1.02 (0–4) | 3.68 (0–15) | 0.54zł (0.0–2.7) | 6.31 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-06_HERESY_PLUS1` | 5.58 Er (1–9) | 3.3% | 28.6% | 1.03 (0–4) | 3.75 (0–15) | 0.53zł (0.0–2.7) | 6.37 (1.4–10.0) | 🟢 W NORMIE |
| `L3_GC-07_COST_PLUS1` | 5.58 Er (1–9) | 3.4% | 28.9% | 1.04 (0–4) | 3.69 (0–16) | 0.53zł (0.0–2.7) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_GC-07_COST_MINUS1` | 5.56 Er (1–9) | 2.9% | 28.1% | 1.02 (0–3) | 3.72 (0–15) | 0.51zł (0.0–2.7) | 6.33 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-07_HERESY_PLUS1` | 5.59 Er (1–9) | 3.4% | 28.6% | 1.03 (0–3) | 3.72 (0–15) | 0.54zł (0.0–2.7) | 6.30 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-07_HERESY_MINUS1` | 5.60 Er (1–9) | 3.5% | 28.7% | 1.03 (0–4) | 3.69 (0–15) | 0.53zł (0.0–2.7) | 6.19 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_PLUS1` | 5.65 Er (1–9) | 3.5% | 29.7% | 1.03 (0–3) | 3.65 (0–15) | 0.53zł (0.0–2.7) | 6.19 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-08_COST_MINUS1` | 5.53 Er (1–9) | 2.9% | 27.8% | 1.01 (0–3) | 3.71 (0–15) | 0.55zł (0.0–2.7) | 6.31 (1.3–10.0) | 🟢 W NORMIE |
| `L3_GC-08_HERESY_PLUS1` | 5.56 Er (1–9) | 3.1% | 28.5% | 1.02 (0–3) | 3.78 (0–15) | 0.53zł (0.0–2.7) | 6.36 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-09_COST_PLUS1` | 5.64 Er (1–9) | 3.8% | 29.2% | 1.04 (0–3) | 3.72 (0–16) | 0.52zł (0.0–3.0) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-09_COST_MINUS1` | 5.57 Er (1–9) | 2.6% | 28.3% | 1.02 (0–4) | 3.77 (0–16) | 0.56zł (0.0–2.7) | 6.35 (1.5–10.0) | 🟢 W NORMIE |
| `L3_GC-09_HERESY_PLUS1` | 5.57 Er (1–9) | 3.1% | 28.5% | 1.03 (0–4) | 3.77 (0–14) | 0.54zł (0.0–3.0) | 6.38 (1.5–10.0) | 🟢 W NORMIE |
| `L3_GC-10_COST_PLUS1` | 5.66 Er (1–9) | 3.9% | 28.1% | 1.04 (0–3) | 3.65 (0–16) | 0.59zł (0.0–2.7) | 6.07 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-10_COST_MINUS1` | 5.54 Er (1–9) | 3.3% | 27.7% | 1.02 (0–3) | 3.76 (0–15) | 0.54zł (0.0–2.7) | 6.30 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-10_HERESY_PLUS1` | 5.49 Er (1–9) | 3.1% | 28.2% | 1.01 (0–3) | 4.02 (0–17) | 0.53zł (0.0–2.7) | 6.39 (1.2–10.0) | 🟢 W NORMIE |
| `L3_GC-10_HERESY_MINUS1` | 5.64 Er (1–9) | 3.9% | 28.8% | 1.04 (0–3) | 3.43 (0–15) | 0.54zł (0.0–2.7) | 6.02 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-01_COST_PLUS1` | 5.56 Er (1–9) | 3.0% | 29.4% | 1.02 (0–3) | 3.68 (0–16) | 0.54zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-01_COST_MINUS1` | 5.52 Er (1–9) | 2.6% | 27.7% | 1.01 (0–3) | 3.66 (0–16) | 0.53zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-01_HERESY_PLUS1` | 5.56 Er (1–9) | 3.1% | 28.6% | 1.03 (0–3) | 3.72 (0–15) | 0.53zł (0.0–2.7) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-02_COST_PLUS1` | 5.68 Er (1–9) | 4.0% | 30.9% | 1.04 (0–3) | 3.83 (0–17) | 0.54zł (0.0–2.7) | 6.27 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_KB-02_COST_MINUS1` | 5.48 Er (1–9) | 2.5% | 28.0% | 1.01 (0–3) | 3.60 (0–15) | 0.54zł (0.0–2.7) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-02_HERESY_PLUS1` | 5.55 Er (1–9) | 3.3% | 28.5% | 1.02 (0–3) | 3.75 (0–19) | 0.54zł (0.0–2.7) | 6.29 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-03_COST_PLUS1` | 5.57 Er (1–9) | 3.0% | 29.5% | 1.03 (0–3) | 3.60 (0–17) | 0.53zł (0.0–2.7) | 6.18 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-03_COST_MINUS1` | 5.50 Er (1–9) | 2.7% | 27.7% | 1.02 (0–4) | 3.68 (0–19) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-03_HERESY_PLUS1` | 5.55 Er (1–9) | 3.2% | 28.5% | 1.02 (0–3) | 3.76 (0–19) | 0.54zł (0.0–2.7) | 6.30 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-04_COST_PLUS1` | 5.61 Er (1–9) | 3.2% | 29.5% | 1.03 (0–3) | 3.69 (0–17) | 0.54zł (0.0–2.7) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-04_COST_MINUS1` | 5.48 Er (1–9) | 2.7% | 27.8% | 1.01 (0–3) | 3.63 (0–16) | 0.53zł (0.0–2.7) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-04_HERESY_PLUS1` | 5.53 Er (1–9) | 3.1% | 28.5% | 1.02 (0–3) | 3.82 (0–19) | 0.54zł (0.0–2.7) | 6.30 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-04_HERESY_MINUS1` | 5.64 Er (1–9) | 3.5% | 28.8% | 1.04 (0–3) | 3.60 (0–16) | 0.54zł (0.0–2.7) | 6.17 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-05_COST_PLUS1` | 5.57 Er (1–9) | 3.1% | 28.7% | 1.03 (0–4) | 3.60 (0–16) | 0.52zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-05_COST_MINUS1` | 5.47 Er (1–9) | 2.6% | 27.8% | 1.01 (0–3) | 3.55 (0–15) | 0.52zł (0.0–2.7) | 6.21 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-05_HERESY_PLUS1` | 5.57 Er (1–9) | 3.3% | 28.6% | 1.03 (0–3) | 3.73 (0–15) | 0.54zł (0.0–2.7) | 6.29 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-06_COST_PLUS1` | 5.57 Er (1–9) | 3.2% | 28.8% | 1.02 (0–4) | 3.69 (0–15) | 0.54zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-06_COST_MINUS1` | 5.62 Er (1–9) | 4.1% | 28.1% | 1.03 (0–3) | 3.76 (0–16) | 0.52zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-06_HERESY_PLUS1` | 5.58 Er (1–9) | 3.3% | 28.6% | 1.03 (0–3) | 3.71 (0–19) | 0.54zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-07_COST_PLUS1` | 5.61 Er (1–9) | 3.6% | 29.0% | 1.03 (0–4) | 3.74 (0–17) | 0.54zł (0.0–3.0) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-07_COST_MINUS1` | 5.47 Er (1–9) | 2.8% | 27.8% | 1.01 (0–3) | 3.54 (0–17) | 0.51zł (0.0–2.7) | 6.21 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-07_HERESY_PLUS1` | 5.56 Er (1–9) | 3.3% | 28.6% | 1.02 (0–3) | 3.73 (0–19) | 0.54zł (0.0–2.7) | 6.28 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-08_COST_PLUS1` | 5.60 Er (1–9) | 3.4% | 28.7% | 1.03 (0–3) | 3.72 (0–17) | 0.54zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-08_COST_MINUS1` | 5.60 Er (1–9) | 3.3% | 28.6% | 1.03 (0–3) | 3.72 (0–17) | 0.53zł (0.0–2.7) | 6.25 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KB-08_HERESY_PLUS1` | 5.59 Er (1–9) | 3.3% | 28.6% | 1.03 (0–3) | 3.71 (0–15) | 0.53zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-09_COST_PLUS1` | 5.77 Er (1–9) | 4.6% | 28.7% | 1.06 (0–3) | 3.91 (0–16) | 0.57zł (0.0–2.7) | 6.29 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-09_COST_MINUS1` | 5.48 Er (1–9) | 2.8% | 28.1% | 1.01 (0–3) | 3.60 (0–15) | 0.52zł (0.0–2.7) | 6.22 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-09_HERESY_PLUS1` | 5.54 Er (1–9) | 3.4% | 28.5% | 1.02 (0–3) | 3.79 (0–15) | 0.53zł (0.0–2.7) | 6.29 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-09_HERESY_MINUS1` | 5.62 Er (1–9) | 3.4% | 28.7% | 1.04 (0–3) | 3.61 (0–15) | 0.53zł (0.0–2.7) | 6.13 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-10_COST_PLUS1` | 5.77 Er (1–9) | 4.7% | 28.9% | 1.06 (0–3) | 3.80 (0–17) | 0.55zł (0.0–2.7) | 6.21 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-10_COST_MINUS1` | 5.41 Er (1–9) | 2.3% | 27.4% | 1.00 (0–3) | 3.57 (0–15) | 0.52zł (0.0–2.7) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-10_HERESY_PLUS1` | 5.43 Er (1–9) | 2.8% | 28.2% | 1.00 (0–3) | 3.97 (0–18) | 0.53zł (0.0–2.7) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KB-10_HERESY_MINUS1` | 5.67 Er (1–9) | 3.9% | 28.8% | 1.05 (0–3) | 3.46 (0–15) | 0.54zł (0.0–2.7) | 6.08 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_PLUS1` | 5.62 Er (1–9) | 3.7% | 29.1% | 1.03 (0–3) | 3.75 (0–16) | 0.45zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-01_COST_MINUS1` | 5.60 Er (1–9) | 3.5% | 28.5% | 1.03 (0–3) | 3.71 (0–18) | 0.69zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-01_HERESY_PLUS1` | 5.60 Er (1–9) | 4.2% | 28.7% | 1.03 (0–4) | 3.77 (0–18) | 0.54zł (0.0–2.7) | 6.38 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-02_COST_PLUS1` | 5.61 Er (1–9) | 3.7% | 29.5% | 1.03 (0–3) | 3.73 (0–15) | 0.44zł (0.0–2.3) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-02_COST_MINUS1` | 5.59 Er (1–9) | 3.5% | 28.5% | 1.03 (0–3) | 3.70 (0–15) | 0.71zł (0.0–3.0) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-02_HERESY_PLUS1` | 5.60 Er (1–9) | 4.2% | 28.7% | 1.03 (0–3) | 3.78 (0–18) | 0.54zł (0.0–2.7) | 6.38 (1.5–10.0) | 🟢 W NORMIE |
| `L3_KT-03_COST_PLUS1` | 5.61 Er (1–9) | 3.6% | 29.1% | 1.03 (0–3) | 3.73 (0–15) | 0.41zł (0.0–2.3) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-03_HERESY_PLUS1` | 5.60 Er (1–9) | 4.6% | 28.7% | 1.03 (0–3) | 3.80 (0–18) | 0.54zł (0.0–3.0) | 6.39 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-03_HERESY_MINUS1` | 5.60 Er (1–9) | 3.2% | 28.7% | 1.03 (0–4) | 3.67 (0–15) | 0.53zł (0.0–2.7) | 6.10 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-04_COST_PLUS1` | 5.62 Er (1–9) | 3.9% | 29.0% | 1.03 (0–3) | 3.73 (0–16) | 0.45zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-04_COST_MINUS1` | 5.59 Er (1–9) | 3.5% | 28.5% | 1.03 (0–3) | 3.70 (0–18) | 0.70zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-04_HERESY_PLUS1` | 5.59 Er (1–9) | 4.1% | 28.6% | 1.03 (0–3) | 3.76 (0–18) | 0.54zł (0.0–2.7) | 6.37 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-05_COST_PLUS1` | 5.62 Er (1–9) | 3.7% | 29.2% | 1.03 (0–3) | 3.74 (0–15) | 0.44zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-05_COST_MINUS1` | 5.60 Er (1–9) | 3.6% | 28.6% | 1.03 (0–3) | 3.72 (0–18) | 0.71zł (0.0–3.0) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-05_HERESY_PLUS1` | 5.59 Er (1–9) | 4.2% | 28.6% | 1.03 (0–3) | 3.78 (0–18) | 0.54zł (0.0–2.7) | 6.38 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-06_COST_PLUS1` | 5.62 Er (1–9) | 3.8% | 29.3% | 1.03 (0–3) | 3.71 (0–15) | 0.46zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-06_COST_MINUS1` | 5.60 Er (1–9) | 3.6% | 28.5% | 1.03 (0–4) | 3.72 (0–18) | 0.74zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-06_HERESY_PLUS1` | 5.61 Er (1–9) | 5.1% | 28.7% | 1.03 (0–3) | 3.81 (0–18) | 0.54zł (0.0–2.7) | 6.41 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-07_COST_PLUS1` | 5.61 Er (1–9) | 3.7% | 29.0% | 1.03 (0–3) | 3.74 (0–15) | 0.44zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-07_COST_MINUS1` | 5.60 Er (1–9) | 3.6% | 28.6% | 1.03 (0–3) | 3.72 (0–18) | 0.71zł (0.0–3.0) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-07_HERESY_PLUS1` | 5.59 Er (1–9) | 4.0% | 28.6% | 1.03 (0–3) | 3.78 (0–18) | 0.54zł (0.0–2.7) | 6.38 (1.3–10.0) | 🟢 W NORMIE |
| `L3_KT-08_COST_PLUS1` | 5.62 Er (1–9) | 3.9% | 29.1% | 1.03 (0–4) | 3.73 (0–15) | 0.46zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-08_COST_MINUS1` | 5.61 Er (1–9) | 3.6% | 28.6% | 1.03 (0–4) | 3.71 (0–18) | 0.70zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-08_HERESY_PLUS1` | 5.59 Er (1–9) | 4.1% | 28.6% | 1.03 (0–3) | 3.77 (0–18) | 0.54zł (0.0–2.7) | 6.38 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-09_COST_PLUS1` | 5.62 Er (1–9) | 3.9% | 29.2% | 1.03 (0–3) | 3.72 (0–15) | 0.45zł (0.0–2.7) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-09_COST_MINUS1` | 5.60 Er (1–9) | 3.6% | 28.5% | 1.03 (0–3) | 3.71 (0–16) | 0.72zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-09_HERESY_PLUS1` | 5.60 Er (1–9) | 4.6% | 28.7% | 1.03 (0–3) | 3.81 (0–18) | 0.54zł (0.0–2.7) | 6.39 (1.3–10.0) | 🟢 W NORMIE |
| `L3_KT-09_HERESY_MINUS1` | 5.60 Er (1–9) | 3.3% | 28.7% | 1.03 (0–4) | 3.67 (0–15) | 0.54zł (0.0–2.7) | 6.10 (1.0–10.0) | 🟢 W NORMIE |
| `L3_KT-10_COST_PLUS1` | 5.61 Er (1–9) | 3.8% | 29.1% | 1.03 (0–3) | 3.73 (0–15) | 0.44zł (0.0–2.3) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-10_COST_MINUS1` | 5.60 Er (1–9) | 3.6% | 28.6% | 1.03 (0–4) | 3.72 (0–18) | 0.71zł (0.0–3.0) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_KT-10_HERESY_PLUS1` | 5.59 Er (1–9) | 4.6% | 28.6% | 1.03 (0–4) | 3.91 (0–17) | 0.55zł (0.0–2.7) | 6.50 (1.4–10.0) | 🟢 W NORMIE |
| `L3_SO-01_COST_PLUS1` | 5.59 Er (1–9) | 3.4% | 29.4% | 1.03 (0–4) | 3.70 (0–15) | 0.55zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-01_COST_MINUS1` | 5.56 Er (1–9) | 3.4% | 27.7% | 1.03 (0–4) | 3.70 (0–15) | 0.56zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-01_HERESY_PLUS1` | 5.52 Er (1–9) | 2.8% | 28.4% | 1.02 (0–3) | 3.74 (0–15) | 0.53zł (0.0–2.7) | 6.33 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-02_COST_PLUS1` | 5.63 Er (1–9) | 3.7% | 30.8% | 1.02 (0–4) | 3.68 (0–15) | 0.55zł (0.0–2.7) | 6.23 (1.2–10.0) | 🔴 PRZEKROCZONE NORMY |
| `L3_SO-02_COST_MINUS1` | 5.56 Er (1–9) | 3.4% | 27.6% | 1.08 (0–4) | 3.72 (0–15) | 0.60zł (0.0–3.0) | 6.29 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-02_HERESY_PLUS1` | 5.48 Er (1–9) | 2.8% | 28.3% | 1.02 (0–3) | 3.75 (0–15) | 0.53zł (0.0–2.7) | 6.33 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-03_COST_PLUS1` | 5.61 Er (1–9) | 3.6% | 29.4% | 1.03 (0–4) | 3.64 (0–15) | 0.55zł (0.0–2.3) | 6.19 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-03_COST_MINUS1` | 5.56 Er (1–9) | 3.3% | 27.6% | 1.05 (0–3) | 3.74 (0–15) | 0.55zł (0.0–3.0) | 6.26 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-03_HERESY_PLUS1` | 5.47 Er (1–9) | 2.8% | 28.3% | 1.01 (0–3) | 3.74 (0–15) | 0.53zł (0.0–2.7) | 6.33 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-04_COST_PLUS1` | 5.58 Er (1–9) | 3.5% | 29.4% | 1.01 (0–3) | 3.71 (0–15) | 0.55zł (0.0–2.7) | 6.23 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-04_COST_MINUS1` | 5.56 Er (1–9) | 3.3% | 27.5% | 1.06 (0–3) | 3.75 (0–15) | 0.57zł (0.0–2.7) | 6.28 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-04_HERESY_PLUS1` | 5.46 Er (1–9) | 2.7% | 28.2% | 1.01 (0–3) | 3.77 (0–15) | 0.53zł (0.0–2.7) | 6.34 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-05_COST_PLUS1` | 5.59 Er (1–9) | 3.4% | 28.6% | 1.03 (0–3) | 3.70 (0–15) | 0.54zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-05_HERESY_PLUS1` | 5.59 Er (1–9) | 3.4% | 28.6% | 1.03 (0–3) | 3.70 (0–15) | 0.54zł (0.0–2.7) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-06_COST_PLUS1` | 5.57 Er (1–9) | 3.2% | 28.6% | 1.05 (0–3) | 3.71 (0–15) | 0.55zł (0.0–2.7) | 6.26 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-06_COST_MINUS1` | 5.58 Er (1–9) | 3.5% | 27.8% | 1.03 (0–3) | 3.69 (0–15) | 0.52zł (0.0–3.0) | 6.23 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-06_HERESY_PLUS1` | 5.58 Er (1–9) | 3.3% | 28.6% | 1.03 (0–3) | 3.71 (0–15) | 0.53zł (0.0–2.7) | 6.28 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-07_COST_PLUS1` | 5.59 Er (1–9) | 3.3% | 28.7% | 1.05 (0–3) | 3.74 (0–15) | 0.55zł (0.0–2.3) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-07_COST_MINUS1` | 5.57 Er (1–9) | 3.4% | 27.8% | 1.05 (0–3) | 3.70 (0–15) | 0.53zł (0.0–3.0) | 6.25 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-07_HERESY_PLUS1` | 5.54 Er (1–9) | 3.1% | 28.5% | 1.02 (0–3) | 3.73 (0–15) | 0.53zł (0.0–2.7) | 6.31 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-08_COST_PLUS1` | 5.63 Er (1–9) | 3.9% | 29.0% | 1.04 (0–3) | 3.68 (0–15) | 0.55zł (0.0–3.0) | 6.20 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-08_COST_MINUS1` | 5.53 Er (1–9) | 3.2% | 27.4% | 1.04 (0–3) | 3.71 (0–15) | 0.52zł (0.0–3.0) | 6.27 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-08_HERESY_PLUS1` | 5.49 Er (1–9) | 2.7% | 28.3% | 1.02 (0–3) | 3.76 (0–15) | 0.53zł (0.0–2.7) | 6.32 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-08_HERESY_MINUS1` | 5.65 Er (1–9) | 4.0% | 28.8% | 1.04 (0–3) | 3.64 (0–15) | 0.54zł (0.0–2.7) | 6.12 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-09_COST_PLUS1` | 5.58 Er (1–9) | 3.1% | 28.7% | 1.04 (0–3) | 3.69 (0–15) | 0.55zł (0.0–2.7) | 6.25 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-09_COST_MINUS1` | 5.59 Er (1–9) | 3.2% | 27.8% | 1.05 (0–3) | 3.71 (0–15) | 0.53zł (0.0–3.0) | 6.27 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-09_HERESY_PLUS1` | 5.53 Er (1–9) | 2.9% | 28.4% | 1.02 (0–3) | 3.73 (0–15) | 0.53zł (0.0–2.7) | 6.33 (1.3–10.0) | 🟢 W NORMIE |
| `L3_SO-10_COST_PLUS1` | 5.76 Er (1–9) | 4.2% | 27.9% | 0.76 (0–3) | 3.53 (0–15) | 0.54zł (0.0–2.7) | 6.13 (0.7–10.0) | 🟢 W NORMIE |
| `L3_SO-10_COST_MINUS1` | 5.56 Er (1–9) | 3.3% | 28.1% | 1.04 (0–3) | 3.73 (0–15) | 0.55zł (0.0–2.7) | 6.26 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-10_HERESY_PLUS1` | 5.48 Er (1–9) | 3.0% | 28.3% | 1.02 (0–3) | 3.74 (0–15) | 0.53zł (0.0–2.7) | 6.24 (1.2–10.0) | 🟢 W NORMIE |
| `L3_SO-10_HERESY_MINUS1` | 5.70 Er (1–9) | 3.9% | 28.9% | 1.05 (0–4) | 3.64 (0–15) | 0.54zł (0.0–2.7) | 6.21 (1.2–10.0) | 🟢 W NORMIE |