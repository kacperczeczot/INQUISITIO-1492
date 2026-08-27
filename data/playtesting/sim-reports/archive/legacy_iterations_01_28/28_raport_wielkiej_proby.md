[Strona główna](../../../../../README.md) > [legacy_iterations_01_28](README.md) > [28_raport_wielkiej_proby](28_raport_wielkiej_proby.md)

---

# Raport 28: Wielka Próba Uczenia Botów i Analizy Głębokie (80,000 Partii)

**Wielkość Próby:** 5000 gier na setup (16 setupów) | **Łącznie:** 80,000 gier | **Czas Symulacji:** 11.18s
**Global Game Balance Index:** `43.4 / 100.0 pkt`

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

- **Rozgrywki 3-osobowe (3p Avg):** `47.5 / 100.0 pkt` (10 setupów)
- **Rozgrywki 4-osobowe (4p Avg):** `39.2 / 100.0 pkt` (5 setupów)
- **Rozgrywki 5-osobowe (5p Avg):** `0.0 / 100.0 pkt` (1 setup)

## 3. Pełny Raport Zwiastunowy 16 Setupów (Uśrednienie 5000 gier)

| Setup | Gr. | Score | Śr. Er | Remisy (8Er) % | Pas Biedy % | Złoto End | Herezja End | Autodafé | Oskarżenia | Alerty |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | ** 56.3** | 6.21 | 8.9% | 25.7% | 0.70zł | 6.81 | 0.81 | 3.27 | WARNING: Podwyższony limit Er: 8.9%; WARNING: Nietypowa aktywność Autodafé: 0.81; WARNING: Ostrzeżenie Ubóstwa: 25.7% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-cienie-korona-gildia` | 3 | ** 64.4** | 5.82 | 17.0% | 28.1% | 0.40zł | 7.07 | 0.76 | 3.74 | CRITICAL: CRITICAL DEADLOCK: 17.0% gier kończy remis (limit >15%); WARNING: Nietypowa aktywność Autodafé: 0.76; WARNING: Ostrzeżenie Ubóstwa: 28.1% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-cienie-korona-kabala` | 3 | ** 87.0** | 6.12 | 5.8% | 24.3% | 0.59zł | 6.42 | 0.79 | 2.89 | WARNING: Podwyższony limit Er: 5.8%; WARNING: Nietypowa aktywność Autodafé: 0.79; WARNING: Ostrzeżenie Ubóstwa: 24.3% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-korona-kabala-gildia` | 3 | ** 94.5** | 6.14 | 7.4% | 26.9% | 0.75zł | 6.90 | 0.77 | 3.77 | WARNING: Podwyższony limit Er: 7.4%; WARNING: Nietypowa aktywność Autodafé: 0.77; WARNING: Ostrzeżenie Ubóstwa: 26.9% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-oficjum-alandalus-gildia` | 3 | **  0.0** | 5.47 | 15.0% | 32.0% | 0.34zł | 6.22 | 1.21 | 2.21 | WARNING: Podwyższony limit Er: 15.0%; WARNING: Ostrzeżenie Ubóstwa: 32.0% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `3p-oficjum-alandalus-kabala` | 3 | ** 99.6** | 5.92 | 4.1% | 28.8% | 0.53zł | 5.70 | 1.26 | 1.57 | WARNING: Ostrzeżenie Ubóstwa: 28.8% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `3p-oficjum-alandalus-korona` | 3 | ** 73.3** | 5.52 | 11.9% | 31.8% | 0.32zł | 6.02 | 1.22 | 2.01 | WARNING: Podwyższony limit Er: 11.9%; WARNING: Ostrzeżenie Ubóstwa: 31.8% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-oficjum-kabala-gildia` | 3 | **  0.0** | 5.79 | 7.5% | 30.9% | 0.70zł | 6.24 | 1.24 | 2.27 | WARNING: Podwyższony limit Er: 7.5%; WARNING: Ostrzeżenie Ubóstwa: 30.9% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `3p-oficjum-korona-gildia` | 3 | **  0.0** | 5.36 | 14.2% | 33.6% | 0.41zł | 6.48 | 1.21 | 2.44 | WARNING: Podwyższony limit Er: 14.2%; WARNING: Ostrzeżenie Ubóstwa: 33.6% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `3p-oficjum-korona-kabala` | 3 | **  0.0** | 5.81 | 4.7% | 30.2% | 0.67zł | 6.08 | 1.23 | 2.20 | WARNING: Ostrzeżenie Ubóstwa: 30.2% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `4p-core` | 4 | ** 32.3** | 4.99 | 1.1% | 26.1% | 0.55zł | 5.41 | 1.19 | 2.51 | WARNING: Porażenie tempa: 4.99 Er (zalecane 5.0–7.0); WARNING: Ostrzeżenie Ubóstwa: 26.1% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `4p-no-cienie` | 4 | **  0.0** | 4.87 | 1.9% | 27.5% | 0.62zł | 5.71 | 1.14 | 2.92 | WARNING: Porażenie tempa: 4.87 Er (zalecane 5.0–7.0); WARNING: Ostrzeżenie Ubóstwa: 27.5% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `4p-no-kabala` | 4 | **  0.0** | 4.77 | 5.3% | 29.0% | 0.36zł | 5.74 | 1.15 | 2.78 | WARNING: Porażenie tempa: 4.77 Er (zalecane 5.0–7.0); WARNING: Podwyższony limit Er: 5.3%; WARNING: Ostrzeżenie Ubóstwa: 29.0% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `4p-no-korona` | 4 | ** 83.1** | 4.88 | 3.0% | 25.9% | 0.56zł | 5.41 | 1.15 | 2.54 | WARNING: Porażenie tempa: 4.88 Er (zalecane 5.0–7.0); WARNING: Ostrzeżenie Ubóstwa: 25.9% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `4p-no-oficjum` | 4 | ** 80.8** | 5.26 | 3.0% | 23.6% | 0.56zł | 6.06 | 0.72 | 4.39 | WARNING: Nietypowa aktywność Autodafé: 0.72; WARNING: Odbiegi aktywności Oskarżeń: 4.39; WARNING: Ostrzeżenie Ubóstwa: 23.6% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `5p-full` | 5 | **  0.0** | 4.55 | 0.6% | 25.0% | 0.52zł | 5.41 | 1.14 | 3.59 | WARNING: Porażenie tempa: 4.55 Er (zalecane 5.0–7.0); WARNING: Ostrzeżenie Ubóstwa: 25.0% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
