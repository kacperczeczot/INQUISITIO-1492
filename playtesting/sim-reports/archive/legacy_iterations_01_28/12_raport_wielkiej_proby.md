# Raport Wielkiej Próby Uczenia Botów i Analizy Głłębokiej (80,000 Partii)

**Wielkość Próby:** 5000 gier na setup (16 setupów) | **Łącznie:** 80,000 gier | **Czas Symulacji:** 9.76s
**Global Game Balance Index:** `35.6 / 100.0 pkt`

## 1. Wyuczone Wnioski Strategiczne w Języku Naturalnym (XAI)

### Wniosek 01: Frakcja CIENIE-AL-ANDALUS (Skuteczność: +17.8%)
💡 Taktyczne spasowanie w Erze 1–3 w celu zaoszczędzenia 2zł na kartę Signature zwiększa szansę na wygraną Cieni o +17.8%.

### Wniosek 02: Frakcja KABALA-TOLEDO (Skuteczność: +13.4%)
💡 Oszczędzanie złota na Pieczęć Salomona we wczesnej fazie gry (Erze 2) podnosi skuteczność Kabały o +13.4%.

### Wniosek 03: Frakcja KORONA-BORGIOWIE (Skuteczność: +11.2%)
💡 Wczesne zagranie Dekretu Miejskiego (przed Erą 4) zwiększa tempo zwycięstwa Korony o +11.2%.

### Wniosek 04: Frakcja SWIETE-OFICJUM (Skuteczność: +16.5%)
💡 Użycie karty Signature Oficjum przy progu 4 Stosów podnosi wygraną o +16.5%.

### Wniosek 05: Frakcja SWIETE-OFICJUM (Skuteczność: +14.5%)
💡 Zdarzenie 'autodafe_on_relic_site' zwiększa skuteczność frakcji swiete-oficjum o +14.5%.

## 2. Podsumowanie Wskaźników Balansu Kategorii Graczy

- **Rozgrywki 3-osobowe (3p Avg):** `46.5 / 100.0 pkt` (10 setupów)
- **Rozgrywki 4-osobowe (4p Avg):** `33.4 / 100.0 pkt` (5 setupów)
- **Rozgrywki 5-osobowe (5p Avg):** `27.0 / 100.0 pkt` (1 setup)

## 3. Pełny Raport Zwiastunowy 16 Setupów (Uśrednienie 5000 gier)

| Setup | Gr. | Score | Śr. Er | Remisy (8Er) % | Pas Biedy % | Złoto End | Herezja End | Autodafé | Oskarżenia | Alerty |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | ** 62.6** | 6.31 | 19.3% | 26.0% | 0.73zł | 6.87 | 0.83 | 3.50 | CRITICAL: CRITICAL DEADLOCK: 19.3% gier kończy remis (limit >15%); WARNING: Nietypowa aktywność Autodafé: 0.83; WARNING: Ostrzeżenie Ubóstwa: 26.0% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-cienie-korona-gildia` | 3 | ** 39.4** | 6.07 | 21.3% | 29.2% | 0.49zł | 7.22 | 0.80 | 4.16 | CRITICAL: CRITICAL DEADLOCK: 21.3% gier kończy remis (limit >15%); WARNING: Nietypowa aktywność Autodafé: 0.80; WARNING: Odbiegi aktywności Oskarżeń: 4.16; WARNING: Ostrzeżenie Ubóstwa: 29.2% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-cienie-korona-kabala` | 3 | ** 61.9** | 6.55 | 14.7% | 26.0% | 0.70zł | 6.75 | 0.85 | 3.51 | WARNING: Podwyższony limit Er: 14.7%; WARNING: Nietypowa aktywność Autodafé: 0.85; WARNING: Ostrzeżenie Ubóstwa: 26.0% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-korona-kabala-gildia` | 3 | **  0.0** | 6.50 | 19.1% | 28.3% | 0.88zł | 7.07 | 0.83 | 4.42 | CRITICAL: CRITICAL DEADLOCK: 19.1% gier kończy remis (limit >15%); WARNING: Nietypowa aktywność Autodafé: 0.83; WARNING: Odbiegi aktywności Oskarżeń: 4.42; WARNING: Ostrzeżenie Ubóstwa: 28.3% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-oficjum-alandalus-gildia` | 3 | ** 70.0** | 5.71 | 19.5% | 32.8% | 0.36zł | 6.37 | 1.25 | 2.50 | CRITICAL: CRITICAL DEADLOCK: 19.5% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 32.8% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `3p-oficjum-alandalus-kabala` | 3 | ** 42.2** | 6.25 | 16.9% | 29.9% | 0.58zł | 5.92 | 1.31 | 1.94 | CRITICAL: CRITICAL DEADLOCK: 16.9% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 29.9% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-oficjum-alandalus-korona` | 3 | ** 45.1** | 6.08 | 16.0% | 33.2% | 0.35zł | 6.40 | 1.30 | 2.51 | CRITICAL: CRITICAL DEADLOCK: 16.0% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 33.2% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-oficjum-kabala-gildia` | 3 | ** 57.6** | 6.19 | 22.0% | 32.1% | 0.76zł | 6.48 | 1.31 | 2.77 | CRITICAL: CRITICAL DEADLOCK: 22.0% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 32.1% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `3p-oficjum-korona-gildia` | 3 | ** 20.3** | 5.93 | 23.4% | 35.2% | 0.47zł | 6.75 | 1.29 | 3.01 | CRITICAL: CRITICAL DEADLOCK: 23.4% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 35.2% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `3p-oficjum-korona-kabala` | 3 | ** 65.6** | 6.57 | 15.8% | 32.3% | 0.72zł | 6.48 | 1.33 | 2.89 | CRITICAL: CRITICAL DEADLOCK: 15.8% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 32.3% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `4p-core` | 4 | ** 49.1** | 5.39 | 2.9% | 27.6% | 0.59zł | 5.66 | 1.25 | 2.99 | WARNING: Ostrzeżenie Ubóstwa: 27.6% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `4p-no-cienie` | 4 | **  0.0** | 5.19 | 4.9% | 28.7% | 0.64zł | 5.88 | 1.19 | 3.32 | WARNING: Ostrzeżenie Ubóstwa: 28.7% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `4p-no-kabala` | 4 | ** 51.3** | 5.01 | 7.2% | 30.0% | 0.37zł | 5.89 | 1.19 | 3.10 | WARNING: Podwyższony limit Er: 7.2%; WARNING: Ostrzeżenie Ubóstwa: 30.0% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `4p-no-korona` | 4 | ** 66.6** | 5.11 | 7.1% | 26.9% | 0.58zł | 5.56 | 1.19 | 2.87 | WARNING: Podwyższony limit Er: 7.1%; WARNING: Ostrzeżenie Ubóstwa: 26.9% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `4p-no-oficjum` | 4 | **  0.0** | 5.39 | 4.8% | 24.0% | 0.56zł | 6.15 | 0.75 | 4.69 | WARNING: Nietypowa aktywność Autodafé: 0.75; WARNING: Odbiegi aktywności Oskarżeń: 4.69; WARNING: Ostrzeżenie Ubóstwa: 24.0% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `5p-full` | 5 | ** 27.0** | 5.08 | 1.8% | 26.9% | 0.51zł | 5.77 | 1.23 | 4.38 | WARNING: Odbiegi aktywności Oskarżeń: 4.38; WARNING: Ostrzeżenie Ubóstwa: 26.9% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |