# Raport 20: Wielka Próba Uczenia Botów i Analizy Głłębokiej (80,000 Partii)

**Wielkość Próby:** 5000 gier na setup (16 setupów) | **Łącznie:** 80,000 gier | **Czas Symulacji:** 11.33s
**Global Game Balance Index:** `49.0 / 100.0 pkt`

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

- **Rozgrywki 3-osobowe (3p Avg):** `58.9 / 100.0 pkt` (10 setupów)
- **Rozgrywki 4-osobowe (4p Avg):** `39.2 / 100.0 pkt` (5 setupów)
- **Rozgrywki 5-osobowe (5p Avg):** `0.0 / 100.0 pkt` (1 setup)

## 3. Pełny Raport Zwiastunowy 16 Setupów (Uśrednienie 5000 gier)

| Setup | Gr. | Score | Śr. Er | Remisy (8Er) % | Pas Biedy % | Złoto End | Herezja End | Autodafé | Oskarżenia | Alerty |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | ** 56.0** | 6.24 | 12.3% | 25.8% | 0.71zł | 6.83 | 0.81 | 3.33 | WARNING: Podwyższony limit Er: 12.3%; WARNING: Nietypowa aktywność Autodafé: 0.81; WARNING: Ostrzeżenie Ubóstwa: 25.8% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-cienie-korona-gildia` | 3 | ** 66.3** | 5.96 | 21.3% | 28.7% | 0.44zł | 7.15 | 0.79 | 3.99 | CRITICAL: CRITICAL DEADLOCK: 21.3% gier kończy remis (limit >15%); WARNING: Nietypowa aktywność Autodafé: 0.79; WARNING: Ostrzeżenie Ubóstwa: 28.7% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-cienie-korona-kabala` | 3 | ** 92.1** | 6.20 | 8.7% | 24.7% | 0.62zł | 6.49 | 0.80 | 3.04 | WARNING: Podwyższony limit Er: 8.7%; WARNING: Nietypowa aktywność Autodafé: 0.80; WARNING: Ostrzeżenie Ubóstwa: 24.7% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-korona-kabala-gildia` | 3 | ** 43.0** | 6.31 | 11.2% | 27.6% | 0.81zł | 6.97 | 0.80 | 4.05 | WARNING: Podwyższony limit Er: 11.2%; WARNING: Nietypowa aktywność Autodafé: 0.80; WARNING: Odbiegi aktywności Oskarżeń: 4.05; WARNING: Ostrzeżenie Ubóstwa: 27.6% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-oficjum-alandalus-gildia` | 3 | ** 70.0** | 5.71 | 19.5% | 32.8% | 0.36zł | 6.37 | 1.25 | 2.50 | CRITICAL: CRITICAL DEADLOCK: 19.5% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 32.8% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `3p-oficjum-alandalus-kabala` | 3 | **  0.0** | 6.17 | 9.1% | 29.6% | 0.54zł | 5.86 | 1.29 | 1.82 | WARNING: Podwyższony limit Er: 9.1%; WARNING: Ostrzeżenie Ubóstwa: 29.6% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-oficjum-alandalus-korona` | 3 | ** 76.5** | 5.89 | 16.0% | 32.7% | 0.34zł | 6.24 | 1.27 | 2.35 | CRITICAL: CRITICAL DEADLOCK: 16.0% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 32.7% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-oficjum-kabala-gildia` | 3 | ** 51.7** | 6.10 | 12.9% | 31.9% | 0.73zł | 6.41 | 1.29 | 2.61 | WARNING: Podwyższony limit Er: 12.9%; WARNING: Ostrzeżenie Ubóstwa: 31.9% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `3p-oficjum-korona-gildia` | 3 | ** 41.2** | 5.84 | 23.4% | 35.0% | 0.45zł | 6.71 | 1.28 | 2.92 | CRITICAL: CRITICAL DEADLOCK: 23.4% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 35.0% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `3p-oficjum-korona-kabala` | 3 | ** 92.4** | 6.27 | 8.7% | 31.5% | 0.70zł | 6.29 | 1.29 | 2.61 | WARNING: Podwyższony limit Er: 8.7%; WARNING: Ostrzeżenie Ubóstwa: 31.5% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `4p-core` | 4 | ** 32.3** | 4.99 | 1.1% | 26.1% | 0.55zł | 5.41 | 1.19 | 2.51 | WARNING: Porażenie tempa: 4.99 Er (zalecane 5.0–7.0); WARNING: Ostrzeżenie Ubóstwa: 26.1% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `4p-no-cienie` | 4 | **  0.0** | 4.87 | 1.9% | 27.5% | 0.62zł | 5.71 | 1.14 | 2.92 | WARNING: Porażenie tempa: 4.87 Er (zalecane 5.0–7.0); WARNING: Ostrzeżenie Ubóstwa: 27.5% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `4p-no-kabala` | 4 | **  0.0** | 4.80 | 5.3% | 29.0% | 0.36zł | 5.74 | 1.16 | 2.78 | WARNING: Porażenie tempa: 4.80 Er (zalecane 5.0–7.0); WARNING: Podwyższony limit Er: 5.3%; WARNING: Ostrzeżenie Ubóstwa: 29.0% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `4p-no-korona` | 4 | ** 83.1** | 4.88 | 3.0% | 25.9% | 0.56zł | 5.41 | 1.15 | 2.54 | WARNING: Porażenie tempa: 4.88 Er (zalecane 5.0–7.0); WARNING: Ostrzeżenie Ubóstwa: 25.9% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `4p-no-oficjum` | 4 | ** 80.8** | 5.26 | 3.0% | 23.6% | 0.56zł | 6.06 | 0.72 | 4.39 | WARNING: Nietypowa aktywność Autodafé: 0.72; WARNING: Odbiegi aktywności Oskarżeń: 4.39; WARNING: Ostrzeżenie Ubóstwa: 23.6% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `5p-full` | 5 | **  0.0** | 4.87 | 0.8% | 26.0% | 0.51zł | 5.63 | 1.19 | 4.01 | WARNING: Porażenie tempa: 4.87 Er (zalecane 5.0–7.0); WARNING: Odbiegi aktywności Oskarżeń: 4.01; WARNING: Ostrzeżenie Ubóstwa: 26.0% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
