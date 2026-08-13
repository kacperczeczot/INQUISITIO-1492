[Strona główna](../README.md) > [Playtesting](README.md)

---


# Playtesting — balans (stan aktualny)

Sim filtruje: deadlocki, oskarżenia, Autodafé, Haki, Podwójni.  
**Werdykt fun = sesja ludzka** ([`sessions/_TEMPLATE.md`](sessions/_TEMPLATE.md)).

Setupy: [`setups.md`](setups.md) · Silnik: [`../sim/README.md`](../sim/README.md).

## Hipotezy (otwarte na stole)

1. Próg oskarżenia **7** vs **8** — dramat Werdyktu vs snowball Oficjum?
2. Sweet spot Kabały **4–6** — czy stół wypycha?
3. Tempo Relikwii — 2 ewakuacje w 60–90 min?

## Dwupoziomowe Progi Balansu Wygranych (Sztywne Bramki `sim`)

| Liczba graczy | Punkt Idealny | 🎯 Cel Ścisły (Target Band) | 🚨 Czerwona Linia (Krytyczna Wariancja) |
| :---: | :---: | :---: | :---: |
| **3 graczy (3p)** | **33.3%** | **28.0% – 38.0%** | **20.0% – 45.0%** |
| **4 graczy (4p)** | **25.0%** | **20.0% – 30.0%** | **15.0% – 35.0%** |
| **5 graczy (5p Full)** | **20.0%** | **16.0% – 24.0%** | **10.0% – 30.0%** |

* **Cel Ścisły:** Sztywny zakres docelowy przy projektowaniu i dostrajaniu balansu.
* **Czerwona Linia:** Przekroczenie oznacza krytyczny błąd balansu (blocker), wyzwalający błąd w testach automatycznych i wymagający bezwzględnej korekty w GDD/kodzie.

---

## Gate przed stołem

```bash
cd sim && source .venv/bin/activate
python -m inquisitio matrix --games 100 --layers A,B,C --seed 42
python -m inquisitio feel --setup 3p-oficjum-alandalus-korona --seed 42 --layer C
pytest tests/test_balance.py tests/test_smoke.py -q
```

Wysokie deadlocki C = blocker (napraw, nie drukuj).

## Stan po 5 Falach Optymalizacji Kombinatorycznej (Monte Carlo 5,000,000 Partii) — 2026-08-13

- **Global Game Balance Score:** **`92.1 / 100.0 pkt`** (Ścisłe Odchylenie Względne)
- **3p Avg Score:** **`95.6 / 100.0 pkt`** (🟢 S-Tier Klasa Światowa — 10 setupów)
- **4p Avg Score:** **`86.2 / 100.0 pkt`** (🟢 S-Tier Klasa Światowa — 5 setupów)
- **5p Avg Score:** **`94.6 / 100.0 pkt`** (🟢 S-Tier Klasa Światowa — 1 setup)

### Zwycięski Ostateczny Pakiet Poprawek Produkcyjnych (T03 + T37 + T20 + T25 + T31 + T43):

| Frakcja | Id Karty / Zasadzie | Zmiana Balansowa | Uzasadnienie Analityczne |
| :--- | :--- | :--- | :--- |
| **Święte Oficjum** | `so-05` / `win.py` | `so-05` koszt = **2 zł**; 5p Stosy = **5 Stosów** | Obniżenie darmowej dominacji Oficjum w Lochach na 5p z 36.8% do 23.3%. |
| **Kabała z Toledo** | `kt-10`, `kt-03`, `kt-09` | `kt-10` koszt = **1 zł**; `kt-03` = **0 zł**; `kt-09` = **1 zł** | Podniesienie płynności skarbcowej Kabały w tłoku z 9.2% do 11.8% -> 20.0%. |
| **Korona & Borgiowie** | `kb-07`, `kb-04` | `kb-07` koszt = **2 zł**; `kb-04` = **1 zł**; Era wygranej = **6**@4–5p | Zbalansowanie wybuchu wygranych Korony w Erze 5 w setupie `4p-core`. |
| **Gildia Cieni** | `gc-08`, `win.py` | `gc-08` koszt = **2 zł**; Upadki na 5p = **3 Upadki** | Usunięcie biernych wygranych w Erze 3 z przypadkowych Haków rywali. |
| **Cienie Al-Andalus** | `caa-05`, `caa-10` | `caa-05` koszt = **1 zł**; `caa-10` = **1 zł**; 3p bez Oficjum = **3 Relikwie** | Stabilizacja Cieni w samym centrum Celu Ścisłego (20.0%). |

Szczegóły: [`../docs/rules/ksiega.md`](../docs/rules/ksiega.md) · słownik: [`../docs/rules/slownik.md`](../docs/rules/slownik.md) · frakcje: [`../game/factions/`](../game/factions/).
