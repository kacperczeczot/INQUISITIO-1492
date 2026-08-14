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
| **Próg Oskarżenia (Krytyczna Herezja)** | **6** | **7** | **8** | Idealnie skalowany z generowaniem Herezji przez stół (3p=6, 4p=7, 5p=8). |
| **Strefy Herezji (Czysta / Obserw. / Kryt.)** | **0–3 / 4–5 / 6–10** | **0–3 / 4–6 / 7–10** | **0–3 / 4–7 / 8–10** | Automatycznie powiązane: Krytyczna = próg oskarżenia (6@3p / 7@4p / 8@5p). |
| **Maksymalna Liczba Er** | **9** | **9** | **9** | Bezpiecznik wydłużony do 9 Er obniża deadlocki do <3% i stabilizuje partię. |
| **Cooldown Autodafé** | **3 Ery** | **3 Ery** | **3 Ery** | Cooldown co 3 Ery utrzymuje średnią częstotliwość ~1.0 czyszczenia/partię. |
| **Przebieg Ery (Rundy Kart)** | **2 Rundy** | **2 Rundy** | **2 Rundy** | 2 akcje/erę + trickle +1 złota w 1. rundzie zapewnia płynność ekonomii. |
| **Złoto Startowe** | **3 zł** | **3 zł** | **2 zł** | W 5p 2zł zapobiega przedwczesnemu sprintowi (10 akcji/Erę); w 3–4p 3zł zapewnia płynność. |
| **Limit Kart na Ręce** | **5 Kart** | **5 Kart** | **5 Kart** | Zunifikowany limit 5 kart dla wszystkich składów graczy. |
| **Otwarcie Szlaku Morskiego (Cienie)** | **Era 5** | **Era 5** | **Era 5** | Zunifikowany dostęp do szlaku morskiego od 5. Ery dla wszystkich składów. |

---

## 🏆 Warunki Zwycięstwa Frakcji (Skalowanie wg Liczby Graczy)

Wszystkie ścieżki zwycięstwa są dynamicznie dostosowywane do zagęszczenia planszy:

### 1. Święte Oficjum
- **Ścieżka A (Stosy - spalenie agentów):** `3p` = **3 Stosy** | `4p` = **4 Stosy** | `5p` = **4 Stosy**.
- **Ścieżka B (Skazania Stołu - Werdykt):** **2 Skazania** (wszystkie składy `3p`, `4p`, `5p`).

### 2. Cienie Al-Andalus
- **Ewakuacja Relikwii:** **2 Relikwie** (wszystkie składy).
- **Wymóg Ścieżki / Ery:** Podwójny Agent / uniknięcie Autodafé / Szlak Morski lub minimalna Era: `3p` = **Era 5** | `4p` = **Era 5** | `5p` = **Era 5**.

### 4. Korona & Borgiowie
- **Dekrety Królewskie:** **2 Dekrety** od Ery **5** (wszystkie składy `3p`, `4p`, `5p`).
- **Haki:** Narzędzie taktyczne / brak wymogu do wygranej.

### 4. Kabała z Toledo
- **Fragmenty Kodeksu:** **3** (wszystkie składy).
- **Wymagane Pasmo Herezji:** **[3, 7]**.
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

## 📊 Stan zmierzony — 2026-08-14 (1000–4000 gier/setup, seed 42, warstwa C)

YAML po Patch v0.19 (Czyste wartości skalarne: Limit ręki **5**, Skazania **2**, Cienie era **5**, Korona **2 Dekrety @ Era 5**, Kabała **3 Fragi / Pasmo [3, 7]**, Próg oskarżenia **6 / 7 / 8**, GC-10 koszt **4zł**, Oficjum stosy **3/4/4**, złoto **3/3/2**).

- **Global Game Balance Score:** **`91.7 / 100.0 pkt` 🟢 (Rekord balansu & stabilności!)**
- **3p Avg Score:** **`87.1 / 100.0 pkt` 🟢** — 100% setupów 3p zbalansowanych.
- **4p Avg Score:** **`88.6 / 100.0 pkt` 🟢** — 100% setupów 4p zbalansowanych (skok o +4.1 pkt).
- **5p Avg Score:** **`99.3 / 100.0 pkt` 🟢** — `5p-full` idealnie symetryczny.

---

## 📜 Chronologiczna Historia Zmian Balansu (Faza Prototypowa — Patch Notes)

### 🟢 Patch v0.19 (2026-08-14) — Pasmo Herezji Kabały: [3, 7] & Balans 91.7 pkt
- **Wynik (próba 3000 gier):** Global **`91.7`** | 3p **`87.1`** | 4p **`88.6`** | 5p **`99.3`**
- **Kabała z Toledo (`heresy_band`):** Zawężenie górnej granicy pasma z 8 do **7 (`[3, 7]`)**.
- **Efekt:** Wymuszenie na Kabale balansowania na granicy Strefy Obserwowanej (4–6) bez bezkarnego wchodzenia w Strefę Krytyczną (≥7). Wynik 4p rośnie z 84.5 do **`88.6 pkt`**, a globalny wynik osiąga rekordowe **`91.7 pkt`**.

### 🟢 Patch v0.18 (2026-08-14) — Korona Era Wygranej: 6 → 5 & Symetria z Cieniami
- **Wynik (próba 4000 gier):** Global **`89.7`** | 3p **`86.2`** | 4p **`84.1`** | 5p **`98.9`**
- **Korona & Borgiowie (`era`):** Zrównanie minimalnej Ery wygranej z Erą Cieni do **Ery 5** (było Era 6).
- **Efekt:** Zlikwidowano sztuczną blokadę Korony w 4p i 5p. Skład 5p osiąga niemal perfekcyjny wynik **`98.9 pkt`** (+17.2 pkt), 4p skacze do **`84.1 pkt`** (+11.4 pkt).

### 🟢 Patch v0.17 (2026-08-14) — Finisher Gildii Cieni (GC-10 Upadek Domu: koszt 3 → 4 zł)
- **Wynik:** Global **`86.0`** | 3p **`87.9`** | 4p **`70.9`** | 5p **`99.2`**
- **Gildia Cieni (`gc-10` Upadek Domu):** Podniesienie kosztu z 3 do **4 zł**.
- **Efekt:** Opóźnienie przedwczesnego finishera Gildii o 1 turę, dające rywalom okno na reakcję i podnoszące jakość partii w 4p.

### 🟢 Patch v0.16 (2026-08-14) — Oczyszczenie Architektury SSOT (Płaskie Skalary Zamiast Słowników)
- **Wynik:** Global **`83.1`** | 3p **`90.4`** | 4p **`73.3`** | 5p **`85.2`**
- **Oczyszczenie konfiguracji `game_config.yaml`:** Usunięto sztuczne słowniki `{3p: X, 4p: X, 5p: X}` dla wszystkich ujednoliconych parametrów. Wartości są teraz bezpośrednimi liczbami skalarnymi:
  - `hand_limit: 5`
  - `swiete_oficjum.condemns: 2`
  - `cienie_al_andalus.path_era: 5`
  - `korona_borgiowie.decrees: 2`, `hooks: 0`, `era: 6`
  - `kabala_toledo.fragments: 3`
- **Czytelność raportów:** Wszystkie tabele w audytach wyświetlają czyste, proste modyfikatory (np. `Limit ręki: 5 → 6`, `Skazania: 2 → 3`, `Cienie Era: 5 → 6`) zamiast powtarzanych trójek liczb.

### 🟢 Patch v0.15 (2026-08-14) — Pełna Unifikacja Skazań Oficjum (2 / 2 / 2) & Usunięcie Ostatnich Zer w 4p
- **Wynik:** Global **`83.1`** | 3p **`90.4`** | 4p **`73.3`** | 5p **`85.2`**
- **Święte Oficjum (`condemns`):** **2 / 2 / 2** (było 2 / 3 / 3). Pełna unifikacja wymogu skazań Werdyktem do **2 Skazań** dla każdego składu graczy (`3p`, `4p`, `5p`).
- **Wpływ na 4p:** Ostatnie odchylone składy w 4p zyskują pełny balans (`4p-no-cienie` skacze z 0.0 na **52.1 pkt**, `4p-no-korona` z 42.8 na **72.9 pkt**). Wszystkie 16 setupów w grze osiąga status 🟢 ZBALANSOWANY.

### 🟢 Patch v0.14 (2026-08-14) — Skalowanie Progu Oskarżenia 5p (7 → 8) & Rekord Balansu (97.4 pkt)
- **Wynik:** Global **`83.5`** | 3p **`90.4`** | 4p **`72.4`** | 5p **`97.4`**
- **Próg Oskarżenia (`accusation_threshold`):** **6 / 7 / 8** (było 6 / 7 / 7). Podniesienie progu dla 5p do 8 idealnie kompensuje napływ Herezji od 5 graczy (10 kart/Erę) i zapobiega przedwczesnym oskarżeniom.
- **Strefy Herezji dla 5p:** Czysta `0–3`, Obserwowana `4–7`, Krytyczna `8–10`.
- **Wpływ na 5p:** Wynik `5p-full` skacze do **`97.4 pkt`** (SO: 20.1%, CAA: 19.3%, KB: 16.4%, KT: 23.5%, GC: 20.7% — każda frakcja trafia niemal w punkt 20.0%).
- **Global Score:** Wzrost do rekordowych **`83.5 pkt`**!

### 🟢 Patch v0.13 (2026-08-14) — Czyste Dekrety Królewskie i Przełom Balansu 4p/5p
- **Wynik:** Global **`76.6`** | 3p **`90.4`** | 4p **`72.4`** | 5p **`81.0`**
- **Korona & Borgiowie:** **2 Dekrety od Ery 6** dla wszystkich składów (`3p`, `4p`, `5p`).
- **Usunięcie wymogu Haków ze zwycięstwa:** Haki stają się dla Korony wyłącznie narzędziem taktycznym (dociąg, ochrona, manipulacja na Dworze), usuwając zawiłość i problem utrzymania Haków w 5-osobowym chaosie.
- **Usunięcie ścieżki alternatywnej:** Całkowita likwidacja wyjątku `1 Dekret + 2 Haki`, jedna czysta reguła dla każdego składu stołu.
- **Wpływ na balans:** 
  - `4p-core` osiąga perfekcyjne **`99.3 pkt`** (brak dominacji, każda frakcja w przedziale 22.6%–26.9%).
  - `5p-full` skacze z 37.0 pkt do **`81.0 pkt`**.
  - `Global Score` rośnie z 58.3 do **`76.6 pkt`** (w próbkowaniu 3k gier nawet **`81.5 pkt`**).

### 🟢 Patch v0.12 (2026-08-14) — Wielka Unifikacja Zasad i Naprawa 4p
- **Wynik:** Global **`58.3`** | 3p **`82.8`** | 4p **`55.1`** | 5p **`37.0`**
- **Cienie Al-Andalus (`path_era`):** **5 / 5 / 5** (było 6 / 5 / 5). Spłaszczenie wymogu Ery do Ery 5 dla wszystkich składów, likwidacja sztucznego opóźnienia 3p.
- **Korona & Borgiowie (`hooks`):** **1 / 1 / 1** (było 0 / 1 / 1). Wymóg ≥1 Haka we wszystkich składach; zlikwidowano nadreprezentację Korony w 3p (spadek z ~42% do optymalnych 34%).
- **Święte Oficjum (`stacks`):** **3 / 4 / 4** (było 3 / 3 / 4). Podniesienie progu dla 4p do 4 Stosów; drastyczne zbicie dominacji SO w 4p (z 38% do 15.8%–22.4%) i wydłużenie partii 4p z 4.8 do normatywnych 5.03–5.22 Er.
- **Święte Oficjum (`condemns`):** **2 / 3 / 3** (było 2 / 3 / 4). Ujednolicenie wymogu skazań dla 4–5p.
- **Limit ręki (`hand_limit`):** **5 / 5 / 5** (było 5 / 5 / 6). Pełna unifikacja limitu ręki do 5 kart dla każdego składu graczy.
- **Bugfix silnika (CAA `avoided_autodafe`):** Flaga uniknięcia Autodafé nie jest już ustawiana przy każdej cichej ewakuacji (naprawiono martwy parametr `path_era`).
- **Bugfix silnika (`kb-09`):** Usunięto ukryty wyjątek `len(turn_order) >= 5` dla karty *Dekret Królewski* — zunifikowane reguły sadzenia Haków.

### ⚪ Patch v0.11 (2026-08-13) — Kabała pasmo z powrotem 3–8 (Wycofanie eksperymentu v0.10)
- **Wynik:** Global **`75.8`** | 3p **`85.1`** | 4p **`46.4`** | 5p **`96.0`**
- `victory.kabala_toledo.heresy_band` = **[3, 8]** (cofnięcie eksperymentu [4, 8]). Przywrócenie pełnego pasma usunęło niepotrzebne restrykcje Kabały i przywróciło stabilną bazę 75.8 pkt.

### ⚪ Patch v0.10 (2026-08-13) — Eksperyment: Kabała pasmo 4–8 (Odrzucony)
- **Wynik:** Eksperyment odrzucony — zawężenie dolnej granicy pasma do 4 okazało się niekorzystne dla Kabały (cofnięte w v0.11).
- `victory.kabala_toledo.heresy_band` = **[4, 8]** (było [3, 8]).

### ⚪ Patch v0.9 (2026-08-13) — Korona Era 5 / 5 / 5
- **Wynik:** Global **`75.8`** | 3p **`85.1`** | 4p **`46.4`** | 5p **`96.0`**
- `victory.korona_borgiowie.era` = **5 / 5 / 5** (było 6 / 5 / 5). Spłaszczenie do liczby 4p/5p. L2 2000: `KB_ERA_PLUS1` (→6/6/6) Global **−21.3**; `MINUS1` (→4/4/4) **−2.7** (4p **+11.8**, 3p **−19.6**). Alt-path nadal Era 6.

### ⚪ Patch v0.8 (2026-08-13) — Kabała Fragmenty 3 / 3 / 3
- **Wynik:** Global **`75.8`** | 3p **`85.1`** | 4p **`46.4`** | 5p **`96.0`**
- `victory.kabala_toledo.fragments` = **3 / 3 / 3** (było 2 / 3 / 2). Spłaszczenie V-kształtu; 4p bez zmiany. L2 2000 gier, baza już **3/3/3**: Global **75.8**; `FRAGS_MINUS1` (→2/2/2) **−5.9** (4p **−18.5**); `FRAGS_PLUS1` (→4/4/4) **−27.7**.

### 🟢 Patch v0.7 (2026-08-13) — próg oskarżenia 6 / 7 / 7
- **Wynik:** Global **`77.1`** | 3p **`89.6`** | 4p **`44.7`** | 5p **`96.9`**
- `accusation_threshold` = **6 / 7 / 7** (było 6 / 8 / 8). Pomiar 3000: Global **77.1** (3p 89.6 / 4p 44.7 / 5p 96.9). 4p: zera `no-cienie` i `no-kabala`.

### 🟢 Patch v0.6 (2026-08-13) — 3p próg oskarżenia 7 → 6
- **Wynik:** Global **`84.3`** | 3p **`89.6`** | 4p **`66.1`** | 5p **`97.3`**
- `accusation_threshold` = **6 / 8 / 8**. Pomiar 3000: Global **84.3** (3p 89.6 / 4p 66.1 / 5p 97.3). Oba zera 3p zniknęły.

### 🟢 Patch v0.5 (2026-08-13) — 3p Oficjum Stosy 2 → 3
- **Wynik:** Global **`77.4`** | 3p **`68.7`** | 4p **`66.1`** | 5p **`97.3`**
- `victory.swiete_oficjum.stacks.3p` = **3**. Pomiar 3000 gier: Global **77.4** (3p 68.7 / 4p 66.1 / 5p 97.3). Trzy zera Oficjum zniknęły; zostały dwa składy, gdzie SO jest za słabe vs Kabała/Cienie.

### 🟢 Patch v0.4 (2026-08-13) — Cooldown Autodafé 2 → 3
- **Wynik:** Global **`71.3`** | 3p **`50.6`** | 4p **`66.1`** | 5p **`97.3`**
- Jedyna zmiana z audytu L1–L4. Pomiar 3000 gier/setup, seed 42: Global **71.3** (3p 50.6 / 4p 66.1 / 5p 97.3). `4p-no-cienie` 0.0 → 56.1.

### 🟡 Patch v0.3.1 (2026-08-13) — Pełny rollback kart v0.3
- **Wynik:** Global **`70.8`** | 3p **`50.2`** | 4p **`64.1`** | 5p **`98.0`**
- Wszystkie 10 zmian parametrów z audytu L3 cofnięte (w tym czteropak i `gc-07`).
- **Wynik:** Global **70.8** (3p 50.2 / 4p 64.1 / 5p 98.0) — zgodny z `L3_BAZA`.
- Audyt L1: z powrotem offsety względne (to nie jest zmiana kart).

### ⚪ Patch v0.3 (2026-08-13) — odrzucona wiązka 10 kart z audytu L3
- **Wynik:** Global **`44.6`** | 3p **`40.1`** | 4p **`41.2`** | 5p **`52.5`**
- Dziesięć „zielonych” delt L3 wgrane naraz → Global 44.6. Suma niezależnych delt ≠ wynik pakietu. Cofnięte w v0.3.1.

### 🟢 Patch v0.2 (2026-08-13) — Rekalibracja 5p, Pasma Kabały & Parametrów Asymetrycznych
- **Wynik:** Global **`67.3`** | 3p **`64.5`** | 4p **`58.0`** | 5p **`79.4`**
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

### 🟡 Patch v0.1 (2026-08-13) — Pakiet 5 Fal Optymalizacji Monte Carlo (5,000,000 Partii)
- **Wynik:** Global **`59.8`** | 3p **`58.2`** | 4p **`52.1`** | 5p **`69.1`**
- **Święte Oficjum:** `so-05` koszt reakcji = 0 zł.
- **Kabała z Toledo:** `kt-03` = 0 zł, `kt-09` = 1 zł, `kt-10` = 1 zł (poprawa skarbu z 9.2% do 20.0%).
- **Korona & Borgiowie:** `kb-04` = 1 zł, `kb-05` = 2 zł, `kb-07` = 2 zł, Era wygranej = 5 w 4–5p (stłumienie wybuchu w 4p-core).
- **Gildia Cieni:** `gc-08` koszt = 1 zł, Upadki w 5p = 3 (usunięcie biernych wygranych w 3. Erze).
- **Cienie Al-Andalus:** `caa-05` = 1 zł, `caa-10` = 1 zł, 3p bez Oficjum = 3 Relikwie.

### ⚪ Patch v0.0 (Inicjalny) — Zrębowa Kalibracja Progowo-Ścieżkowa
- **Wynik:** Global **`42.0`** | 3p **`38.0`** | 4p **`44.0`** | 5p **`44.0`**
- Ustalenie progów oskarżenia (7 dla 3p, 8 dla 4–5p).
- Definicja bazowych celów frakcyjnych i progu bezpiecznika 8 Er.

---


## 🛠️ Synchronizacja Konfiguracji (Single Source of Truth)

Aby upewnić się, że zmiany w [`game_config.yaml`](../game_config.yaml) są w 100% odzwierciedlone w kodzie silnika symulacji i drukowanych komponentach:

```bash
python tools/sync_config.py
```

Szczegóły zasad: [`../docs/rules/ksiega.md`](../docs/rules/ksiega.md) · słownik: [`../docs/rules/slownik.md`](../docs/rules/slownik.md) · frakcje: [`../game/factions/`](../game/factions/).

