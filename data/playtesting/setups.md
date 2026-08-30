[Strona główna](../README.md) > [Playtesting](README.md)

---

## Parametry wspólne (zsynchronizowane z `game_config.yaml`)

| Parametr | 3p | 4p (Kanon) / 5p |
| :--- | :--- | :--- |
| Próg Krytycznej (Oskarżenie) | **7** | **7** / **7** |
| Strefa Obserwowana | **5–6** | **5–6** / **5–6** |
| Strefa Krytyczna | **≥7** | **≥7** / **≥7** |
| Karty w Fazie II (Plan) | **2** rundy zagrań / Erę | **2** rundy zagrań / Erę |
| Limit Er | **15** | **15** |
| Relikwie | 1 w Lochach + **2** odkryte | 1 w Lochach + **2** odkryte |
| Fragmenty Kodeksu (pula) | **4** | **6** |
| Złoto startowe | **4** | **4** |
| Agenci | **3** | **3** |
| Limit na ręce | **5** | **5** |
| Inkwizytor | Start: Trybunał, Patrol | Start: Trybunał, Patrol |

### Karty wg warstwy PnP

| Warstwa | W talii gracza |
| :--- | :--- |
| **A** | Tylko `layer: A` (5 kart) — Inkwizytor + Werdykt |
| **B** | A + B (bez karty specjalnej) |
| **C** | Pełne 10 + Kronika Dziejów |

---

### Presety silnika (`sim` — 16 kombinacji)

| Kod | Skład Frakcji |
| :--- | :--- |
| **3p (10 kombinacji):** | |
| `3p-oficjum-alandalus-korona` | Oficjum + Cienie + Korona |
| `3p-oficjum-kabala-gildia` | Oficjum + Kabała + Gildia |
| `3p-cienie-korona-gildia` | Cienie + Korona + Gildia |
| `3p-oficjum-alandalus-gildia` | Oficjum + Cienie + Gildia |
| `3p-oficjum-alandalus-kabala` | Oficjum + Cienie + Kabała |
| `3p-oficjum-korona-gildia` | Oficjum + Korona + Gildia |
| `3p-oficjum-korona-kabala` | Oficjum + Korona + Kabała |
| `3p-cienie-korona-kabala` | Cienie + Korona + Kabała |
| `3p-cienie-kabala-gildia` | Cienie + Kabała + Gildia |
| `3p-korona-kabala-gildia` | Korona + Kabała + Gildia |
| **4p (5 kombinacji):** | |
| `4p-core` | Oficjum + Cienie + Korona + Kabała |
| `4p-no-kabala` | Oficjum + Cienie + Korona + Gildia |
| `4p-no-korona` | Oficjum + Cienie + Kabała + Gildia |
| `4p-no-cienie` | Oficjum + Korona + Kabała + Gildia |
| `4p-no-oficjum` | Cienie + Korona + Kabała + Gildia |
| **5p (1 kombinacja):** | |
| `5p-full` | Wszystkie 5 frakcji (Oficjum + Cienie + Korona + Kabała + Gildia) |

```bash
cd sim && source .venv/bin/activate
python -m inquisitio setups
python -m inquisitio matrix --games 80 --layers B,C   # cała matryca balansu
pytest tests/test_balance.py -v
```

---

## 3 graczy (Format 3P)

Cel: czytelny stół (~60–90 min), dramat Werdyktu / Inkwizytora bez pełnego szumu 5 frakcji.

### 🌟 Oficjalnie Rekomendowane Składy dla 3P (Score ≥ 85.0)

W formacie 3-osobowym rekomendujemy wyłącznie zestawienia osiągające certyfikowany, wysoki wynik balansu (**Score ≥ 85.0**):

| Setup / Kod | Skład Frakcji | Balans Win-Share (Score) | Styl rozgrywki i Dynamika Stołu |
| :--- | :--- | :---: | :--- |
| **`3p-cienie-korona-gildia`** | **Cienie + Korona + Gildia** | 🟡 **89.3**<br>(32.0% / 31.4% / 36.6%) | **👑 Pakt Kupiecki & Intryga:** Inkwizytor działa jako neutralny NPC na planszy. Najwyżej zbalansowany i najbardziej płynny format dla 3 graczy — brak bezpośredniego terroru gracza Inkwizycji, gra oparta na szantażu, handlu i wpływach. |
| **`3p-oficjum-korona-kabala`** | **Oficjum + Korona + Kabała** | 🟡 **86.2**<br>(29.4% / 34.6% / 36.0%) | **⚔️ Władza, Trybunał i Tajemnica:** Pełna równowaga trójkąta z graczem Inkwizycji. Władza świecka (Korona) szachuje Trybunał (Oficjum), a Kabała manipuluje Sefirotami w Złotym Paśmie Herezji [4, 6]. |

> [!WARNING]
> **Pozostałe Składy 3P (Warianty Asymetryczne / Dla Doświadczonych Graczy):**
> Składy poniżej progu 85.0 (np. `3p-oficjum-alandalus-gildia` 82.4, `3p-oficjum-korona-gildia` 80.5, `3p-cienie-kabala-gildia` 78.6, `3p-korona-kabala-gildia` 72.0, `3p-cienie-korona-kabala` 70.2) oraz układy spolaryzowane (`3p-oficjum-kabala-gildia` 59.6, `3p-oficjum-alandalus-korona` 51.9, `3p-oficjum-alandalus-kabala` 49.3) cechują się ostrzejszą asymetrią i wymagają od graczy aktywnej gry przeciwko uciekającemu liderowi (*Anti-Leader / Kingmaker Resistance*).

---

## 4 graczy (Kanon 4P — Główny Format Gry)

Podstawowy kanon turniejowy i pudełkowy gry INQUISITIO-1492 ([ADR-0002](../docs/adr/0002-kanon-4p-jako-bezwzgledna-kotwica-balansu.md)). 

### 🌟 2 Główne Rekomendowane Składy dla 4P (Elita Balansu Score > 93.0)

W formacie 4-osobowym rekomendujemy przede wszystkim dwa flagowe zestawienia oferujące najwyższy możliwy poziom matematycznej symetrii szans:

| Setup / Kod | Skład Frakcji | Balans Win-Share (Score) | Rekomendacja i Zastosowanie |
| :--- | :--- | :---: | :--- |
| **`4p-no-korona`**<br>*(bez Korony)* | **Oficjum + Cienie + Kabała + Gildia** | 🟢 **97.2**<br>(24.2% / 25.1% / 24.9% / 25.8%) | **🏆 Kanon Turniejowy z Graczem Inkwizycji:** Niemal idealna symetria szans (~25% per frakcja). Pełna, ostra interakcja: polowanie na Herezję, procesy Trybunału, ucieczka Szlakiem Morskim i Upadki Gildii. |
| **`4p-no-oficjum`**<br>*(bez Oficjum)* | **Cienie + Korona + Kabała + Gildia** | 🟢 **93.2**<br>(23.0% / 26.0% / 25.3% / 25.7%) | **👑 Król Czystej Gry Politycznej:** Inkwizytor działa jako bezstronny, neutralny NPC na planszy — gra opiera się na czystej intrydze, handlu, Dekretach i wpływach dworskich bez presji procesowej gracza Inkwizycji. |

### Pozostałe Składy 4P (Warianty Alternatywne i Wprowadzające)

* **`4p-no-kabala`** (Score: **90.7** 🟢) — Oficjum + Cienie + Korona + Gildia. Klasyczny format wpływów i terroru bez manipulacji mistycyzmem Kabały.
* **`4p-no-cienie`** (Score: **83.7** 🟡) — Oficjum + Korona + Kabała + Gildia. Brak ewakuacji Relikwii — bezwzględna presja lochów, Dekretów i sądów.
* **`4p-core`** / `4p-no-gildia` (Score: **82.4** 🟡) — Oficjum + Cienie + Korona + Kabała. **Kanon Narracyjny na Pierwszą Grę:** 4 pierwotne frakcje historyczne Hiszpanii 1492 roku bez skomplikowanych łańcuchów Upadków Gildii. Idealne do nauki zasad.

---

## 5 graczy (Format 5P Full)

| Setup / Kod | Skład Frakcji | Balans Win-Share (Score) | Rekomendacja i Styl |
| :--- | :--- | :---: | :--- |
| **`5p-full`** | **Wszystkie 5 frakcji** | 🟢 **92.2**<br>(19.6% / 21.2% / 20.0% / 21.0% / 18.2%) | **👑 Pełny Majestat Asymetrii:** Wszystkie frakcje przy stole (~20% na frakcję). Pełna sieć Haków, Marionetek, Procesów, Dekretów i Ucieczki (~90+ min). |

---

## Checklista przed sesją

1. Wydruk / szkic: [`../game/board/locations.md`](../game/board/locations.md), [`../game/board/player-board.md`](../game/board/player-board.md)
2. Komponenty: [`../game/components/inventory.md`](../game/components/inventory.md), [`../game/components/print-3d.md`](../game/components/print-3d.md)
3. Talie wg warstwy + (C) Kronika Dziejów (10 kart edyktów)
4. Żetony: Herezja, złoto, Relikwie, Fragmenty, Haki, Marionetki, Stosy, Upadek, Dekret, Inkwizytor
5. Sprawdź próg oskarżenia (**7** — Krytyczna Herezja) oraz warstwę A/B/C — zapisz w notatce sesji
6. Wybierz skład z tej strony
7. Po grze: [`sessions/_TEMPLATE.md`](sessions/_TEMPLATE.md) (UX: downtime, AP, emocja Werdyktu)
