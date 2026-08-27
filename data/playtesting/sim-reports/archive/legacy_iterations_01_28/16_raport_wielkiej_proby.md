# Raport 16: Wielka Próba Uczenia Botów i Analizy Głębokie (80,000 Partii)

**Wielkość Próby:** 5000 gier na setup (16 setupów) | **Łącznie:** 80,000 gier | **Czas Symulacji:** 11.94s
**Global Game Balance Index:** `48.4 / 100.0 pkt`

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

- **Rozgrywki 3-osobowe (3p Avg):** `26.2 / 100.0 pkt` (10 setupów)
- **Rozgrywki 4-osobowe (4p Avg):** `57.5 / 100.0 pkt` (5 setupów)
- **Rozgrywki 5-osobowe (5p Avg):** `61.5 / 100.0 pkt` (1 setup)

## 3. Pełny Raport Zwiastunowy 16 Setupów (Uśrednienie 5000 gier)

| Setup | Gr. | Score | Śr. Er | Remisy (8Er) % | Pas Biedy % | Złoto End | Herezja End | Autodafé | Oskarżenia | Alerty |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | **  0.0** | 6.79 | 18.7% | 27.2% | 0.74zł | 7.26 | 0.89 | 3.91 | CRITICAL: CRITICAL DEADLOCK: 18.7% gier kończy remis (limit >15%); WARNING: Nietypowa aktywność Autodafé: 0.89; WARNING: Ostrzeżenie Ubóstwa: 27.2% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-cienie-korona-gildia` | 3 | **  0.0** | 6.70 | 35.4% | 30.5% | 0.53zł | 7.67 | 0.90 | 5.00 | CRITICAL: CRITICAL DEADLOCK: 35.4% gier kończy remis (limit >15%); WARNING: Nietypowa aktywność Autodafé: 0.90; WARNING: Odbiegi aktywności Oskarżeń: 5.00; WARNING: Ostrzeżenie Poziomu Herezji: 7.67; WARNING: Ostrzeżenie Ubóstwa: 30.5% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-cienie-korona-kabala` | 3 | **  0.0** | 7.10 | 13.2% | 27.1% | 0.71zł | 7.16 | 0.93 | 3.94 | WARNING: Porażenie tempa: 7.10 Er (zalecane 5.0–7.0); WARNING: Podwyższony limit Er: 13.2%; WARNING: Nietypowa aktywność Autodafé: 0.93; WARNING: Ostrzeżenie Ubóstwa: 27.1% tur w pasie z braku złota |
| `3p-korona-kabala-gildia` | 3 | **  0.0** | 6.42 | 11.2% | 28.2% | 0.86zł | 7.02 | 0.81 | 4.24 | WARNING: Podwyższony limit Er: 11.2%; WARNING: Nietypowa aktywność Autodafé: 0.81; WARNING: Odbiegi aktywności Oskarżeń: 4.24; WARNING: Ostrzeżenie Ubóstwa: 28.2% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-oficjum-alandalus-gildia` | 3 | ** 70.0** | 5.71 | 19.5% | 32.8% | 0.36zł | 6.37 | 1.25 | 2.50 | CRITICAL: CRITICAL DEADLOCK: 19.5% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 32.8% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `3p-oficjum-alandalus-kabala` | 3 | **  0.0** | 6.17 | 9.1% | 29.6% | 0.54zł | 5.86 | 1.29 | 1.82 | WARNING: Podwyższony limit Er: 9.1%; WARNING: Ostrzeżenie Ubóstwa: 29.6% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-oficjum-alandalus-korona` | 3 | ** 45.1** | 6.08 | 16.0% | 33.2% | 0.35zł | 6.40 | 1.30 | 2.51 | CRITICAL: CRITICAL DEADLOCK: 16.0% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 33.2% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-oficjum-kabala-gildia` | 3 | ** 51.7** | 6.10 | 12.9% | 31.9% | 0.73zł | 6.41 | 1.29 | 2.61 | WARNING: Podwyższony limit Er: 12.9%; WARNING: Ostrzeżenie Ubóstwa: 31.9% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `3p-oficjum-korona-gildia` | 3 | ** 20.3** | 5.93 | 23.4% | 35.2% | 0.47zł | 6.75 | 1.29 | 3.01 | CRITICAL: CRITICAL DEADLOCK: 23.4% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 35.2% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `3p-oficjum-korona-kabala` | 3 | ** 75.3** | 6.50 | 8.7% | 32.1% | 0.71zł | 6.42 | 1.32 | 2.80 | WARNING: Podwyższony limit Er: 8.7%; WARNING: Ostrzeżenie Ubóstwa: 32.1% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `4p-core` | 4 | ** 77.3** | 5.35 | 1.6% | 27.5% | 0.59zł | 5.62 | 1.25 | 2.92 | WARNING: Ostrzeżenie Ubóstwa: 27.5% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `4p-no-cienie` | 4 | ** 44.4** | 5.13 | 2.8% | 28.5% | 0.63zł | 5.84 | 1.18 | 3.23 | WARNING: Ostrzeżenie Ubóstwa: 28.5% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `4p-no-kabala` | 4 | ** 51.3** | 5.01 | 7.2% | 30.0% | 0.37zł | 5.89 | 1.19 | 3.10 | WARNING: Podwyższony limit Er: 7.2%; WARNING: Ostrzeżenie Ubóstwa: 30.0% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `4p-no-korona` | 4 | ** 57.3** | 5.03 | 4.3% | 26.5% | 0.56zł | 5.50 | 1.18 | 2.74 | WARNING: Ostrzeżenie Ubóstwa: 26.5% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `4p-no-oficjum` | 4 | ** 57.4** | 5.33 | 3.0% | 23.7% | 0.55zł | 6.10 | 0.73 | 4.53 | WARNING: Nietypowa aktywność Autodafé: 0.73; WARNING: Odbiegi aktywności Oskarżeń: 4.53; WARNING: Ostrzeżenie Ubóstwa: 23.7% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `5p-full` | 5 | ** 61.5** | 5.03 | 0.8% | 26.7% | 0.52zł | 5.73 | 1.22 | 4.28 | WARNING: Odbiegi aktywności Oskarżeń: 4.28; WARNING: Ostrzeżenie Ubóstwa: 26.7% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
