[Strona główna](../../../../../README.md) > [legacy_iterations_01_28](README.md) > [09_raport_wielkiej_proby](09_raport_wielkiej_proby.md)

---

# Raport Wielkiej Próby Uczenia Botów i Analizy Głłębokiej (80,000 Partii)

**Wielkość Próby:** 5000 gier na setup (16 setupów) | **Łącznie:** 80,000 gier | **Czas Symulacji:** 9.63s
**Global Game Balance Index:** `44.5 / 100.0 pkt`

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

- **Rozgrywki 3-osobowe (3p Avg):** `47.8 / 100.0 pkt` (10 setupów)
- **Rozgrywki 4-osobowe (4p Avg):** `49.0 / 100.0 pkt` (5 setupów)
- **Rozgrywki 5-osobowe (5p Avg):** `36.7 / 100.0 pkt` (1 setup)

## 3. Pełny Raport Zwiastunowy 16 Setupów (Uśrednienie 5000 gier)

| Setup | Gr. | Score | Śr. Er | Remisy (8Er) % | Pas Biedy % | Złoto End | Herezja End | Autodafé | Oskarżenia | Alerty |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | ** 66.8** | 6.33 | 20.9% | 26.4% | 0.57zł | 6.88 | 0.83 | 3.52 | CRITICAL: CRITICAL DEADLOCK: 20.9% gier kończy remis (limit >15%); WARNING: Nietypowa aktywność Autodafé: 0.83; WARNING: Ostrzeżenie Ubóstwa: 26.4% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-cienie-korona-gildia` | 3 | ** 39.4** | 6.07 | 21.3% | 29.2% | 0.49zł | 7.22 | 0.80 | 4.16 | CRITICAL: CRITICAL DEADLOCK: 21.3% gier kończy remis (limit >15%); WARNING: Nietypowa aktywność Autodafé: 0.80; WARNING: Odbiegi aktywności Oskarżeń: 4.16; WARNING: Ostrzeżenie Ubóstwa: 29.2% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-cienie-korona-kabala` | 3 | ** 54.3** | 6.57 | 16.2% | 26.6% | 0.60zł | 6.73 | 0.87 | 3.50 | CRITICAL: CRITICAL DEADLOCK: 16.2% gier kończy remis (limit >15%); WARNING: Nietypowa aktywność Autodafé: 0.87; WARNING: Ostrzeżenie Ubóstwa: 26.6% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-korona-kabala-gildia` | 3 | ** 19.2** | 6.55 | 21.8% | 28.7% | 0.73zł | 7.09 | 0.84 | 4.45 | CRITICAL: CRITICAL DEADLOCK: 21.8% gier kończy remis (limit >15%); WARNING: Nietypowa aktywność Autodafé: 0.84; WARNING: Odbiegi aktywności Oskarżeń: 4.45; WARNING: Ostrzeżenie Ubóstwa: 28.7% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-oficjum-alandalus-gildia` | 3 | ** 70.0** | 5.71 | 19.5% | 32.8% | 0.36zł | 6.37 | 1.25 | 2.50 | CRITICAL: CRITICAL DEADLOCK: 19.5% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 32.8% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `3p-oficjum-alandalus-kabala` | 3 | ** 39.5** | 6.27 | 18.8% | 30.3% | 0.43zł | 5.89 | 1.32 | 1.96 | CRITICAL: CRITICAL DEADLOCK: 18.8% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 30.3% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-oficjum-alandalus-korona` | 3 | ** 45.1** | 6.08 | 16.0% | 33.2% | 0.35zł | 6.40 | 1.30 | 2.51 | CRITICAL: CRITICAL DEADLOCK: 16.0% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 33.2% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-oficjum-kabala-gildia` | 3 | ** 60.0** | 6.24 | 24.4% | 32.6% | 0.59zł | 6.49 | 1.32 | 2.79 | CRITICAL: CRITICAL DEADLOCK: 24.4% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 32.6% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `3p-oficjum-korona-gildia` | 3 | ** 20.3** | 5.93 | 23.4% | 35.2% | 0.47zł | 6.75 | 1.29 | 3.01 | CRITICAL: CRITICAL DEADLOCK: 23.4% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 35.2% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `3p-oficjum-korona-kabala` | 3 | ** 63.2** | 6.60 | 17.4% | 32.8% | 0.56zł | 6.45 | 1.34 | 2.88 | CRITICAL: CRITICAL DEADLOCK: 17.4% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 32.8% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `4p-core` | 4 | ** 51.3** | 5.40 | 3.2% | 27.8% | 0.42zł | 5.65 | 1.25 | 3.01 | WARNING: Ostrzeżenie Ubóstwa: 27.8% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `4p-no-cienie` | 4 | **  0.0** | 5.21 | 6.0% | 29.0% | 0.48zł | 5.88 | 1.20 | 3.32 | WARNING: Podwyższony limit Er: 6.0%; WARNING: Ostrzeżenie Ubóstwa: 29.0% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `4p-no-kabala` | 4 | ** 51.3** | 5.01 | 7.2% | 30.0% | 0.37zł | 5.89 | 1.19 | 3.10 | WARNING: Podwyższony limit Er: 7.2%; WARNING: Ostrzeżenie Ubóstwa: 30.0% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `4p-no-korona` | 4 | ** 74.8** | 5.12 | 7.8% | 27.1% | 0.44zł | 5.56 | 1.20 | 2.88 | WARNING: Podwyższony limit Er: 7.8%; WARNING: Ostrzeżenie Ubóstwa: 27.1% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |
| `4p-no-oficjum` | 4 | ** 67.7** | 5.41 | 5.5% | 24.2% | 0.41zł | 6.15 | 0.75 | 4.67 | WARNING: Podwyższony limit Er: 5.5%; WARNING: Nietypowa aktywność Autodafé: 0.75; WARNING: Odbiegi aktywności Oskarżeń: 4.67; WARNING: Ostrzeżenie Ubóstwa: 24.2% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `5p-full` | 5 | ** 36.7** | 5.11 | 2.4% | 27.1% | 0.40zł | 5.78 | 1.23 | 4.38 | WARNING: Odbiegi aktywności Oskarżeń: 4.38; WARNING: Ostrzeżenie Ubóstwa: 27.1% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |