[Strona główna](../../../../../README.md) > [legacy_iterations_01_28](README.md) > [24_raport_wielkiej_proby](24_raport_wielkiej_proby.md)

---

# Raport 24: Wielka Próba Uczenia Botów i Analizy Głłębokiej (80,000 Partii)

**Wielkość Próby:** 5000 gier na setup (16 setupów) | **Łącznie:** 80,000 gier | **Czas Symulacji:** 11.02s
**Global Game Balance Index:** `50.5 / 100.0 pkt`

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

- **Rozgrywki 3-osobowe (3p Avg):** `61.9 / 100.0 pkt` (10 setupów)
- **Rozgrywki 4-osobowe (4p Avg):** `39.2 / 100.0 pkt` (5 setupów)
- **Rozgrywki 5-osobowe (5p Avg):** `0.0 / 100.0 pkt` (1 setup)

## 3. Pełny Raport Zwiastunowy 16 Setupów (Uśrednienie 5000 gier)

| Setup | Gr. | Score | Śr. Er | Remisy (8Er) % | Pas Biedy % | Złoto End | Herezja End | Autodafé | Oskarżenia | Alerty |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | ** 56.0** | 6.24 | 12.3% | 25.8% | 0.71zł | 6.83 | 0.81 | 3.33 | WARNING: Podwyższony limit Er: 12.3%; WARNING: Nietypowa aktywność Autodafé: 0.81; WARNING: Ostrzeżenie Ubóstwa: 25.8% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-cienie-korona-gildia` | 3 | ** 64.4** | 5.82 | 17.0% | 28.1% | 0.40zł | 7.07 | 0.76 | 3.74 | CRITICAL: CRITICAL DEADLOCK: 17.0% gier kończy remis (limit >15%); WARNING: Nietypowa aktywność Autodafé: 0.76; WARNING: Ostrzeżenie Ubóstwa: 28.1% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-cienie-korona-kabala` | 3 | ** 72.5** | 6.15 | 8.4% | 24.4% | 0.60zł | 6.44 | 0.79 | 2.94 | WARNING: Podwyższony limit Er: 8.4%; WARNING: Nietypowa aktywność Autodafé: 0.79; WARNING: Ostrzeżenie Ubóstwa: 24.4% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-korona-kabala-gildia` | 3 | ** 89.8** | 6.17 | 9.7% | 26.9% | 0.75zł | 6.92 | 0.78 | 3.82 | WARNING: Podwyższony limit Er: 9.7%; WARNING: Nietypowa aktywność Autodafé: 0.78; WARNING: Odbiegi aktywności Oskarżeń: 4.82; WARNING: Ostrzeżenie Ubóstwa: 26.9% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-oficjum-alandalus-gildia` | 3 | ** 70.0** | 5.71 | 19.5% | 32.8% | 0.36zł | 6.37 | 1.25 | 2.50 | CRITICAL: CRITICAL DEADLOCK: 19.5% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 32.8% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `3p-oficjum-alandalus-kabala` | 3 | **  0.0** | 6.17 | 9.1% | 29.6% | 0.54zł | 5.86 | 1.29 | 1.82 | WARNING: Podwyższony limit Er: 9.1%; WARNING: Ostrzeżenie Ubóstwa: 29.6% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-oficjum-alandalus-korona` | 3 | ** 58.2** | 5.85 | 15.5% | 32.6% | 0.34zł | 6.21 | 1.26 | 2.29 | CRITICAL: CRITICAL DEADLOCK: 15.5% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 32.6% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-oficjum-kabala-gildia` | 3 | ** 51.7** | 6.10 | 12.9% | 31.9% | 0.73zł | 6.41 | 1.29 | 2.61 | WARNING: Podwyższony limit Er: 12.9%; WARNING: Ostrzeżenie Ubóstwa: 31.9% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `3p-oficjum-korona-gildia` | 3 | ** 71.2** | 5.73 | 18.9% | 34.6% | 0.44zł | 6.66 | 1.26 | 2.80 | CRITICAL: CRITICAL DEADLOCK: 18.9% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 34.6% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `3p-oficjum-korona-kabala` | 3 | ** 85.6** | 6.23 | 8.3% | 31.3% | 0.69zł | 6.26 | 1.28 | 2.55 | WARNING: Podwyższony limit Er: 8.3%; WARNING: Ostrzeżenie Ubóstwa: 31.3% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `4p-core` | 4 | ** 32.3** | 4.99 | 1.1% | 26.1% | 0.55zł | 5.41 | 1.19 | 2.51 | WARNING: Porażenie tempa: 4.99 Er (zalecane 5.0–7.0); WARNING: Ostrzeżenie Ubóstwa: 26.1% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `4p-no-cienie` | 4 | **  0.0** | 4.87 | 1.9% | 27.5% | 0.62zł | 5.71 | 1.14 | 2.92 | WARNING: Porażenie tempa: 4.87 Er (zalecane 5.0–7.0); WARNING: Ostrzeżenie Ubóstwa: 27.5% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `4p-no-kabala` | 4 | **  0.0** | 4.77 | 5.3% | 29.0% | 0.36zł | 5.74 | 1.15 | 2.78 | WARNING: Porażenie tempa: 4.77 Er (zalecane 5.0–7.0); WARNING: Podwyższony limit Er: 5.3%; WARNING: Ostrzeżenie Ubóstwa: 29.0% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `4p-no-korona` | 4 | ** 83.1** | 4.88 | 3.0% | 25.9% | 0.56zł | 5.41 | 1.15 | 2.54 | WARNING: Porażenie tempa: 4.88 Er (zalecane 5.0–7.0); WARNING: Ostrzeżenie Ubóstwa: 25.9% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `4p-no-oficjum` | 4 | ** 80.8** | 5.26 | 3.0% | 23.6% | 0.56zł | 6.06 | 0.72 | 4.39 | WARNING: Nietypowa aktywność Autodafé: 0.72; WARNING: Odbiegi aktywności Oskarżeń: 4.39; WARNING: Ostrzeżenie Ubóstwa: 23.6% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `5p-full` | 5 | **  0.0** | 4.55 | 0.6% | 25.0% | 0.52zł | 5.41 | 1.14 | 3.59 | WARNING: Porażenie tempa: 4.55 Er (zalecane 5.0–7.0); WARNING: Ostrzeżenie Ubóstwa: 25.0% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
