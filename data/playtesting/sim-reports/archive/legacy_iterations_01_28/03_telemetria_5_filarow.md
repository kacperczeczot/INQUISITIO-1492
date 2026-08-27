[Strona główna](../../../../../README.md) > [legacy_iterations_01_28](README.md) > [03_telemetria_5_filarow](03_telemetria_5_filarow.md)

---

# Raport Telemetrii i Punktacji Balansu Symulacji (Zakresy 2-Poziomowe i 1-Poziomowe)

**Global Game Balance Score:** `63.8 / 100.0 pkt`

## 1. Zakresy Dopuszczalne i Progi Alertów

### A. Mechaniki Krytyczne (Dwupoziomowe: Cel Ścisły vs Czerwona Linia)
| Metryka | 🎯 Cel Ścisły | 🚨 Czerwona Linia (Blocker) |
| :--- | :---: | :---: |
| **Średnia Liczba Er (`eras_avg`)** | 5.0 – 7.0 Er | < 4.0 LUB > 7.5 Er |
| **Remisy na Limicie 8 Er (`eras_limit_pct`)** | 0.0% – 5.0% | > 15.0% |
| **Autodafé na partię (`autodafe_avg`)** | 1.0 – 2.5 | < 0.5 LUB > 4.0 |
| **Oskarżenia / Werdykty (`accusations_avg`)** | 1.5 – 4.0 | < 0.8 LUB > 6.0 |

### B. Mechaniki Pomocnicze (Jednopoziomowe: Zakres Ostrzegawczy)
| Metryka | ⚠️ Zakres Ostrzegawczy | Co oznacza przekroczenie |
| :--- | :---: | :--- |
| **Złoto End (`avg_gold_end`)** | 0.20 zł – 1.50 zł | <0.2zł: ubóstwo; >1.5zł: inflacja/brak kart |
| **Herezja End (`avg_heresy_end`)** | 4.5 – 7.5 | <4.5: zbyt bezpiecznie w 0-3; >7.5: tłok w 7-10 |
| **Pas Przymusowy (`passes_forced_pct`)** | < 3.0% | >3%: pętla ubóstwa u danej frakcji |
| **Min Liczba Er (`eras_min`)** | ≥ 3 Er | <3 Er: anomalia zrzuconej wygranej w 1-2 Erze |

## 2. Podsumowanie Ocen Kategorii Graczy
- **3-osobowe (3p Avg):** `83.9 / 100.0 pkt` (10 setupów)
- **4-osobowe (4p Avg):** `60.1 / 100.0 pkt` (5 setupów)
- **5-osobowe (5p Avg):** `47.5 / 100.0 pkt` (1 setup)

## 3. Szczegółowy Raport Telemetryczny i Alertów per Setup

| Setup | Gr. | Score | Śr. Er | Remis % | Złoto End | Herezja End | Autodafé | Oskarżenia | Alerty i Ostrzeżenia |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `3p-cienie-kabala-gildia` | 3 | ** 99.8** | 6.22 | 20.4% | 0.46zł | 6.66 | 0.83 | 3.37 | CRITICAL: CRITICAL DEADLOCK: 20.4% gier kończy remis (limit >15%); WARNING: Nietypowa aktywność Autodafé: 0.83; WARNING: Ostrzeżenie Ubóstwa: 31.4% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-cienie-korona-gildia` | 3 | ** 94.9** | 5.98 | 18.8% | 0.49zł | 7.16 | 0.78 | 4.09 | CRITICAL: CRITICAL DEADLOCK: 18.8% gier kończy remis (limit >15%); WARNING: Nietypowa aktywność Autodafé: 0.78; WARNING: Odbiegi aktywności Oskarżeń: 4.09; WARNING: Ostrzeżenie Ubóstwa: 34.4% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-cienie-korona-kabala` | 3 | ** 94.6** | 6.52 | 16.2% | 0.49zł | 6.55 | 0.89 | 3.37 | CRITICAL: CRITICAL DEADLOCK: 16.2% gier kończy remis (limit >15%); WARNING: Nietypowa aktywność Autodafé: 0.89; WARNING: Ostrzeżenie Ubóstwa: 31.0% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-korona-kabala-gildia` | 3 | ** 33.2** | 6.63 | 24.8% | 0.63zł | 6.95 | 0.84 | 4.24 | CRITICAL: CRITICAL DEADLOCK: 24.8% gier kończy remis (limit >15%); WARNING: Nietypowa aktywność Autodafé: 0.84; WARNING: Odbiegi aktywności Oskarżeń: 4.24; WARNING: Ostrzeżenie Ubóstwa: 32.9% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-oficjum-alandalus-gildia` | 3 | ** 99.8** | 5.82 | 21.2% | 0.36zł | 6.44 | 1.23 | 2.59 | CRITICAL: CRITICAL DEADLOCK: 21.2% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 39.0% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-oficjum-alandalus-kabala` | 3 | ** 91.5** | 6.21 | 19.2% | 0.31zł | 5.72 | 1.30 | 1.84 | CRITICAL: CRITICAL DEADLOCK: 19.2% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 36.0% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-oficjum-alandalus-korona` | 3 | ** 94.3** | 6.18 | 16.2% | 0.35zł | 6.43 | 1.28 | 2.58 | CRITICAL: CRITICAL DEADLOCK: 16.2% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 38.9% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-oficjum-kabala-gildia` | 3 | ** 93.6** | 6.43 | 29.8% | 0.44zł | 6.40 | 1.34 | 2.82 | CRITICAL: CRITICAL DEADLOCK: 29.8% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 38.0% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-oficjum-korona-gildia` | 3 | ** 37.9** | 5.92 | 21.8% | 0.47zł | 6.71 | 1.27 | 2.94 | CRITICAL: CRITICAL DEADLOCK: 21.8% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 40.7% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `3p-oficjum-korona-kabala` | 3 | ** 99.9** | 6.64 | 18.6% | 0.46zł | 6.27 | 1.35 | 2.86 | CRITICAL: CRITICAL DEADLOCK: 18.6% gier kończy remis (limit >15%); WARNING: Ostrzeżenie Ubóstwa: 37.6% tur w pasie z braku złota |
| `4p-core` | 4 | **  8.3** | 5.27 | 3.8% | 0.36zł | 5.41 | 1.24 | 2.60 | WARNING: Ostrzeżenie Ubóstwa: 34.8% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `4p-no-cienie` | 4 | ** 49.4** | 5.20 | 7.2% | 0.45zł | 5.74 | 1.14 | 3.22 | WARNING: Podwyższony limit Er: 7.2%; WARNING: Ostrzeżenie Ubóstwa: 36.1% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `4p-no-kabala` | 4 | ** 98.2** | 5.04 | 8.2% | 0.38zł | 5.82 | 1.17 | 2.82 | WARNING: Podwyższony limit Er: 8.2%; WARNING: Ostrzeżenie Ubóstwa: 36.9% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `4p-no-korona` | 4 | ** 94.5** | 5.11 | 7.8% | 0.34zł | 5.50 | 1.21 | 2.70 | WARNING: Podwyższony limit Er: 7.8%; WARNING: Ostrzeżenie Ubóstwa: 34.5% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `4p-no-oficjum` | 4 | ** 49.9** | 5.27 | 5.2% | 0.39zł | 6.01 | 0.72 | 4.37 | WARNING: Podwyższony limit Er: 5.2%; WARNING: Nietypowa aktywność Autodafé: 0.72; WARNING: Odbiegi aktywności Oskarżeń: 4.37; WARNING: Ostrzeżenie Ubóstwa: 31.4% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 2 |
| `5p-full` | 5 | ** 47.5** | 4.51 | 1.8% | 0.34zł | 5.27 | 1.16 | 3.45 | WARNING: Porażenie tempa: 4.51 Er (zalecane 5.0–7.0); WARNING: Ostrzeżenie Ubóstwa: 33.9% tur w pasie z braku złota; WARNING: Ostrzeżenie Anomali Wygranej: partia wygrana w Erze 1 |