[Strona główna](../README.md) > [Playtesting](README.md)

---

# Playtesting — balans (stan aktualny)

Sim filtruje: deadlocki, oskarżenia, Autodafé, Haki, Podwójni.  
**Werdykt fun = sesja ludzka** ([`sessions/_TEMPLATE.md`](sessions/_TEMPLATE.md)).  
**Spłaszczanie:** unikamy skalowania 3p/4p/5p; jedna liczba, jeśli wynik jest lepszy, podobny albo tani ([hierarchia §0](../docs/rules/hierarchia_balansowania.md)).

Setupy: [`setups.md`](setups.md) · Hierarchia Balansowania: [`../docs/rules/hierarchia_balansowania.md`](../docs/rules/hierarchia_balansowania.md) · Silnik: [`../sim/README.md`](../sim/README.md) · Config: [`../game_config.yaml`](../game_config.yaml).

---

## ⚙️ Kluczowe Parametry Systemowe (Single Source of Truth: `game_config.yaml`)

Wszystkie wartości balansu są zsynchronizowane centralnie z pliku [`game_config.yaml`](../game_config.yaml):

| Parametr Systemowy | 3 Graczy (3p) | 4 Graczy (4p) | 5 Graczy (5p Full) | Uzasadnienie Analityczne |
| :--- | :---: | :---: | :---: | :--- |
| **Próg Oskarżenia (Krytyczna Herezja)** | **6** | **7** | **7** | Schodek 1: 3p=6 (zera Oficjum), 4p/5p=7 jak 5p. 4p przy 7 ma SO za mocne w `no-cienie`/`no-kabala` — to błąd 4p, nie powód trzymać 8. |
| **Strefy Herezji (Czysta / Obserw. / Kryt.)** | **0–3 / 4–5 / 6–10** | **0–3 / 4–6 / 7–10** | **0–3 / 4–6 / 7–10** | Krytyczna = próg oskarżenia (6@3p / 7@4–5p). |
| **Maksymalna Liczba Er** | **9** | **9** | **9** | Bezpiecznik wydłużony do 9 Er obniża deadlocki o połowę (z 7.1% do 3.5%) i podnosi Global Score do 67.3 pkt. |
| **Cooldown Autodafé** | **3 Ery** | **3 Ery** | **3 Ery** | L1 ±1 (3000 gier): cooldown 3 daje +4.0 global i +12.5 w 4p przy 5p −0.5; średnie Autodafé zostaje ~1.0/partię. |
| **Przebieg Ery (Rundy Kart)** | **2 Rundy** | **2 Rundy** | **2 Rundy** | 2 akcje/erę + trickle +1 złota w 1. rundzie poprawiają płynność ekonomii. |
| **Złoto Startowe** | **3 zł** | **3 zł** | **2 zł** | W 5p 2zł zwalnia wczesny rozmach Korony/Gildii i daje czas Oficjum/Kabale (skok wyniku 5p do 65.5 pkt); w 3–4p 3zł zapewnia płynność. |
| **Limit Kart na Ręce** | **5 Kart** | **5 Kart** | **6 Kart** | W 5p limit 6 kart daje szeroki wybór akcji w tłoku (skok wyniku 5p do 69.1 pkt); w 3–4p limit 5 kart trzyma tempo. |
| **Otwarcie Szlaku Morskiego (Cienie)** | **Era 6** | **Era 5** | **Era 5** | Automatyczny dostęp do ewakuacji morskiej w 5. Erze dla wyższych składów. |

---

## 🏆 Warunki Zwycięstwa Frakcji (Skalowanie wg Liczby Graczy)

Wszystkie ścieżki zwycięstwa są dynamicznie dostosowywane do zagęszczenia planszy:

### 1. Święte Oficjum
- **Ścieżka A (Stosy - spalenie agentów):** `3p` = **3 Stosy** | `4p` = **3 Stosy** | `5p` = **4 Stosy**.
- **Ścieżka B (Skazania Stołu - Werdykt):** `3p` = **2 Skazania** | `4p` = **3 Skazania** | `5p` = **4 Skazania**.

### 2. Cienie Al-Andalus
- **Ewakuacja Relikwii:** **2 Relikwie** (wszystkie składy).
- **Wymóg Ścieżki / Ery:** Podwójny Agent / uniknięcie Autodafé / Szlak Morski lub minimalna Era: `3p` = **Era 6** | `4p` = **Era 5** | `5p` = **Era 5**.

### 3. Korona & Borgiowie
- **Ścieżka Główna (Dekrety + Haki):**
  - `3p`: **2 Dekrety + 0 Haków** (od Ery 5)
  - `4p`: **2 Dekrety + 1 Hak** (od Ery 5)
  - `5p`: **2 Dekrety + 1 Hak** (od Ery 5)
- **Ścieżka Alternatywna (4p+):** **1 Dekret + 2 Haki** (od Ery 6).

### 4. Kabała z Toledo
- **Fragmenty Kodeksu:** **3** (wszystkie składy).
- **Wymagane Pasmo Herezji:** **[3, 8]** (musi znajdować się w strefie Obserwowanej lub na progu Krytycznej).
- **Minimalna Era Wygranej:** `3p` = **Era 7** | `4p` = **Era 6** | `5p` = **Era 6**.


### 5. Gildia Cieni
- **Upadki Rywali (Falls):** **2 Upadki** ze Świętym Oficjum | **3 Upadki** gdy Oficjum nie gra.

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

## 📊 Stan zmierzony — 2026-08-13 (3000 gier/setup, seed 42, warstwa C)

`autodafe_cooldown` **3** + `stacks.3p` **3** + `accusation_threshold` **6 / 7 / 7**.

- **Global Game Balance Score:** **`77.1 / 100.0 pkt`**
- **3p Avg Score:** **`89.6 / 100.0 pkt`** — bez zer
- **4p Avg Score:** **`44.7 / 100.0 pkt`** — zera `4p-no-cienie`, `4p-no-kabala` (SO ~37–39%)
- **5p Avg Score:** **`96.9 / 100.0 pkt`**

`python tools/sim/measure_baseline.py --games 3000 --seed 42`

---

## 📜 Chronologiczna Historia Zmian Balansu (Patch Notes)

### ⚪ Patch v1.9 (2026-08-13) — Korona Era 5 / 5 / 5
- `victory.korona_borgiowie.era` = **5 / 5 / 5** (było 6 / 5 / 5). Spłaszczenie do liczby 4p/5p. L2 `KB_ERA_PLUS1` ~0; `MINUS1` psuje 4p tylko przez zejście do 4. Alt-path nadal Era 6.

### ⚪ Patch v1.8 (2026-08-13) — Kabała Fragmenty 3 / 3 / 3
- `victory.kabala_toledo.fragments` = **3 / 3 / 3** (było 2 / 3 / 2). Spłaszczenie V-kształtu; 4p bez zmiany. L2 `FRAGS_PLUS1` (3/4/3) ~0 na score — pomiar 3000 jeszcze nie zrobiony.

### 🟢 Patch v1.7 (2026-08-13) — próg oskarżenia 6 / 7 / 7
- `accusation_threshold` = **6 / 7 / 7** (było 6 / 8 / 8). Pomiar 3000: Global **77.1** (3p 89.6 / 4p 44.7 / 5p 96.9). 4p: zera `no-cienie` i `no-kabala`.

### 🟢 Patch v1.6 (2026-08-13) — 3p próg oskarżenia 7 → 6
- `accusation_threshold` = **6 / 8 / 8**. Pomiar 3000: Global **84.3** (3p 89.6 / 4p 66.1 / 5p 97.3). Oba zera 3p zniknęły.

### 🟢 Patch v1.5 (2026-08-13) — 3p Oficjum Stosy 2 → 3
- `victory.swiete_oficjum.stacks.3p` = **3**. Pomiar 3000 gier: Global **77.4** (3p 68.7 / 4p 66.1 / 5p 97.3). Trzy zera Oficjum zniknęły; zostały dwa składy, gdzie SO jest za słabe vs Kabała/Cienie.

### 🟢 Patch v1.4 (2026-08-13) — Cooldown Autodafé 2 → 3
- Jedyna zmiana z audytu L1–L4. Pomiar 3000 gier/setup, seed 42: Global **71.3** (3p 50.6 / 4p 66.1 / 5p 97.3). `4p-no-cienie` 0.0 → 56.1.

### 🟡 Patch v1.3.1 (2026-08-13) — Pełny rollback kart v1.3
- Wszystkie 10 zmian parametrów z audytu L3 cofnięte (w tym czteropak i `gc-07`).
- **Wynik:** Global **70.8** (3p 50.2 / 4p 64.1 / 5p 98.0) — zgodny z `L3_BAZA`.
- Audyt L1: z powrotem offsety względne (to nie jest zmiana kart).

### ⚪ Patch v1.3 (2026-08-13) — odrzucona wiązka 10 kart z audytu L3
Dziesięć „zielonych” delt L3 wgrane naraz → Global 44.6. Suma niezależnych delt ≠ wynik pakietu. Cofnięte w v1.3.1.

### 🟢 Patch v1.2 (2026-08-13) — Rekalibracja 5p, Pasma Kabały & Parametrów Asymetrycznych
- **Święte Oficjum (`5p Stosy`):** Obniżenie wymogu z 5 do **4 Stosy** w składzie 5-osobowym. 
  - *Efekt:* Wzrost wygranych Oficjum w 5p z 10.5% do **20.4%** (trafienie w idealny punkt 20.0%) i skok wyniku balansu 5p z **`🔴 0.0 pkt`** do **`🟢 52.9 pkt`**.
- **Złoto Startowe (`start_gold`):** Wprowadzenie asymetrycznego budżetu startowego wg liczby graczy (`3p: 3zł` | `4p: 3zł` | `5p: 2zł`).
  - *Efekt:* Zmniejszenie startowej dominacji Korony/Gildii w tłoku 5p bez wywoływania pasa biedy w 3–4p.
- **Limit Kart na Ręce (`hand_limit`):** Wprowadzenie asymetrycznego limitu kart na ręce (`3p: 5` | `4p: 5` | `5p: 6`).
  - *Efekt:* W 5p limit 6 kart dostarcza szeroki wybór opcji taktycznych w tłoku 15 agentów na mapie.
- **Kabała z Toledo (`heresy_band`):** Poszerzenie górnej granicy pasma z 7 do **8 (`[3, 8]`)**.
  - *Efekt:* Podniesienie wyniku `Global Score` z 59.8 do **`🟢 64.5 pkt`** (`+4.7 pkt`) oraz `5p Score` do **`🟢 79.4 pkt`** (`+10.3 pkt`).
- **Limit Er (`max_eras`):** Podniesienie bezpiecznika z 8 do **9 Er**.
  - *Efekt:* Redukcja patów o 50% (z 7.1% do 3.5%) i skok `Global Score` do **`🟢 67.3 pkt`** (`+0.8 pkt`).




### 🟡 Patch v1.1 (2026-08-13) — Pakiet 5 Fal Optymalizacji Monte Carlo (5,000,000 Partii)
- **Święte Oficjum:** `so-05` koszt reakcji = 0 zł.
- **Kabała z Toledo:** `kt-03` = 0 zł, `kt-09` = 1 zł, `kt-10` = 1 zł (poprawa skarbu z 9.2% do 20.0%).
- **Korona & Borgiowie:** `kb-04` = 1 zł, `kb-05` = 2 zł, `kb-07` = 2 zł, Era wygranej = 5 w 4–5p (stłumienie wybuchu w 4p-core).
- **Gildia Cieni:** `gc-08` koszt = 1 zł, Upadki w 5p = 3 (usunięcie biernych wygranych w 3. Erze).
- **Cienie Al-Andalus:** `caa-05` = 1 zł, `caa-10` = 1 zł, 3p bez Oficjum = 3 Relikwie.

### ⚪ Patch v1.0 (Inicjalny) — Zrębowa Kalibracja Progowo-Ścieżkowa
- Ustalenie progów oskarżenia (7 dla 3p, 8 dla 4–5p).
- Definicja bazowych celów frakcyjnych i progu bezpiecznika 8 Er.

---


## 🛠️ Synchronizacja Konfiguracji (Single Source of Truth)

Aby upewnić się, że zmiany w [`game_config.yaml`](../game_config.yaml) są w 100% odzwierciedlone w kodzie silnika symulacji i drukowanych komponentach:

```bash
python tools/sync_config.py
```

Szczegóły zasad: [`../docs/rules/ksiega.md`](../docs/rules/ksiega.md) · słownik: [`../docs/rules/slownik.md`](../docs/rules/slownik.md) · frakcje: [`../game/factions/`](../game/factions/).

