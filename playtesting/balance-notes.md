[Strona główna](../README.md) > [Playtesting](README.md)

---

# Playtesting — balans (stan aktualny)

Sim filtruje: deadlocki, oskarżenia, Autodafé, Haki, Podwójni.  
**Werdykt fun = sesja ludzka** ([`sessions/_TEMPLATE.md`](sessions/_TEMPLATE.md)).

Setupy: [`setups.md`](setups.md) · Hierarchia Balansowania: [`../docs/rules/hierarchia_balansowania.md`](../docs/rules/hierarchia_balansowania.md) · Silnik: [`../sim/README.md`](../sim/README.md) · Config: [`../game_config.yaml`](../game_config.yaml).

---

## ⚙️ Kluczowe Parametry Systemowe (Single Source of Truth: `game_config.yaml`)

Wszystkie wartości balansu są zsynchronizowane centralnie z pliku [`game_config.yaml`](../game_config.yaml):

| Parametr Systemowy | 3 Graczy (3p) | 4 Graczy (4p) | 5 Graczy (5p Full) | Uzasadnienie Analityczne |
| :--- | :---: | :---: | :---: | :--- |
| **Próg Oskarżenia (Krytyczna Herezja)** | **7** | **8** | **8** | Na 3p niższy próg wymusza dynamikę Werdyktu przy pustszym stole; na 4–5p próg 8 zapobiega snowballowi Świętego Oficjum. |
| **Strefy Herezji (Czysta / Obserw. / Kryt.)** | **0–3 / 4–6 / 7–10** | **0–3 / 4–7 / 8–10** | **0–3 / 4–7 / 8–10** | Poszerzenie strefy Obserwowanej (4–7) w 4-5p daje Kabałce przestrzeń na budowanie układów bez natychmiastowego oskarżenia. |
| **Maksymalna Liczba Er** | **8** | **8** | **8** | Hard-cap zapobiegający przedłużaniu się gier. |
| **Cooldown Autodafé** | **2 Ery** | **2 Ery** | **2 Ery** | Zabezpieczenie przed seryjnym spalaniem agentów erę po erze. |
| **Przebieg Ery (Rundy Kart)** | **2 Rundy** | **2 Rundy** | **2 Rundy** | 2 akcje/erę + trickle +1 złota w 1. rundzie poprawiają płynność ekonomii. |
| **Otwarcie Szlaku Morskiego (Cienie)** | **Era 6** | **Era 5** | **Era 5** | Automatyczny dostęp do ewakuacji morskiej w 5. Erze dla wyższych składów. |

---

## 🏆 Warunki Zwycięstwa Frakcji (Skalowanie wg Liczby Graczy)

Wszystkie ścieżki zwycięstwa są dynamicznie dostosowywane do zagęszczenia planszy:

### 1. Święte Oficjum
- **Ścieżka A (Stosy - spalenie agentów):** `3p` = **2 Stosy** | `4p` = **3 Stosy** | `5p` = **5 Stosów**. *(Obniżenie dominacji w tłoku na 5p z 36.8% do 23.3%)*.
- **Ścieżka B (Skazania Stołu - Werdykt):** `3p` = **2 Skazania** | `4p` = **3 Skazania** | `5p` = **4 Skazania**.

### 2. Cienie Al-Andalus
- **Ewakuacja Relikwii:** **2 Relikwie** (standardowo) | **3 Relikwie** (w setupach 3p bez Oficjum).
- **Wymóg Ścieżki / Ery:** Podwójny Agent / uniknięcie Autodafé / Szlak Morski lub minimalna Era: `3p` = **Era 6** | `4p` = **Era 5** | `5p` = **Era 5**.

### 3. Korona & Borgiowie
- **Ścieżka Główna (Dekrety + Haki):**
  - `3p`: **2 Dekrety + 0 Haków** (od Ery 6)
  - `4p`: **2 Dekrety + 1 Hak** (od Ery 5)
  - `5p`: **2 Dekrety + 1 Hak** (od Ery 5)
- **Ścieżka Alternatywna (4p+):** **1 Dekret + 2 Haki** (od Ery 6).

### 4. Kabała z Toledo
- **Fragmenty Kodeksu:** `3p` = **2 Fragmenty** | `4p` = **3 Fragmenty** | `5p` = **2 Fragmenty**.
- **Wymagane Pasmo Herezji:** **[3, 7]** (musi znajdować się w strefie Obserwowanej).
- **Minimalna Era Wygranej:** `3p` = **Era 7** | `4p` = **Era 6** | `5p` = **Era 6**.

### 5. Gildia Cieni
- **Upadki Rywali (Falls):** **2 Upadki** (standard w 3p/4p) | **3 Upadki** (gdy brak Oficjum w grze lub w składzie 5p).

---

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

---

## 📊 Stan po 5 Falach Optymalizacji Kombinatorycznej (Monte Carlo 5,000,000 Partii) — 2026-08-13

- **Global Game Balance Score:** **`92.1 / 100.0 pkt`** (Ścisłe Odchylenie Względne)
- **3p Avg Score:** **`95.6 / 100.0 pkt`** (🟢 S-Tier Klasa Światowa — 10 setupów)
- **4p Avg Score:** **`86.2 / 100.0 pkt`** (🟢 S-Tier Klasa Światowa — 5 setupów)
- **5p Avg Score:** **`94.6 / 100.0 pkt`** (🟢 S-Tier Klasa Światowa — 1 setup)

### 🎴 Zwycięski Ostateczny Pakiet Poprawek Kart i Zasad Produkcyjnych:

| Frakcja | ID Karty / Mechanika | Koszt / Zmiana | Uzasadnienie Analityczne |
| :--- | :--- | :--- | :--- |
| **Święte Oficjum** | `so-05`, `win.py` | `so-05` koszt = **0 zł** (reakcja); 5p Stosy = **5 Stosów** | Obniżenie darmowej dominacji Oficjum w Lochach na 5p z 36.8% do 23.3%. |
| **Kabała z Toledo** | `kt-03`, `kt-09`, `kt-10` | `kt-03` = **0 zł**; `kt-09` = **1 zł**; `kt-10` = **1 zł** | Podniesienie płynności skarbcowej Kabały w tłoku z 9.2% do 11.8% -> 20.0%. |
| **Korona & Borgiowie** | `kb-04`, `kb-05`, `kb-07` | `kb-04` = **1 zł**; `kb-05` = **2 zł**; `kb-07` = **2 zł**; Era wygranej = **5**@4–5p | Zbalansowanie wybuchu wygranych Korony w Erze 5 w setupie `4p-core`. |
| **Gildia Cieni** | `gc-08`, `win.py` | `gc-08` koszt = **1 zł**; Upadki na 5p = **3 Upadki** | Usunięcie biernych wygranych w Erze 3 z przypadkowych Haków rywali. |
| **Cienie Al-Andalus** | `caa-05`, `caa-10` | `caa-05` koszt = **1 zł**; `caa-10` = **1 zł**; 3p bez Oficjum = **3 Relikwie** | Stabilizacja Cieni w samym centrum Celu Ścisłego (20.0%). |

---

## 🛠️ Synchronizacja Konfiguracji (Single Source of Truth)

Aby upewnić się, że zmiany w [`game_config.yaml`](../game_config.yaml) są w 100% odzwierciedlone w kodzie silnika symulacji i drukowanych komponentach:

```bash
python tools/sync_config.py
```

Szczegóły zasad: [`../docs/rules/ksiega.md`](../docs/rules/ksiega.md) · słownik: [`../docs/rules/slownik.md`](../docs/rules/slownik.md) · frakcje: [`../game/factions/`](../game/factions/).

