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

## 3 graczy

Cel: czytelny stół (~60–90 min), dramat Werdyktu / Inkwizytora bez pełnego szumu 5 frakcji.

### Rekomendowane składy

| Kod / skład | Co testuje |
| :--- | :--- |
| Oficjum + Cienie + Korona | Terror / Relikwie / Dekrety+Haki |
| Oficjum + Kabała + Gildia | Sweet spot Herezji vs Upadek vs Stosy |
| Cienie + Korona + Gildia | Polityka i szantaż (Inkwizytor jako neutralny NPC) |
| Oficjum + Cienie + Gildia | Stosy vs Relikwie vs Upadek |

### Notatki 3p

- Gildia i Kabała mają mniej celów — metryki Haków / wrabiania mogą być ostrzejsze.
- Pierwsza sesja: preferuj **Oficjum + Cienie + Korona**.

---

## 4 graczy

Cel: asymetria + sojusze, bez pełnej piątki.

### Którą frakcję wyłączyć

| Wyłącz | Styl rozgrywki przy stole |
| :--- | :--- |
| **Gildia Cieni** | Czystszy stół; fokus Relikwie / Stosy / Dekrety |
| **Kabała z Toledo** | Mniej manewru Herezją; ostrzejszy Werdykt |
| **Korona** | Mniej Haków/Dekretów; ostrzejsze Relikwie i Stosy |
| **Cienie Al-Andalus** | Brak ewakuacji — fokus Herezja / Upadek / Stosy |
| **Święte Oficjum** | Inkwizytor jako neutralny NPC na planszy |

Domyślnie pierwsza sesja 4p: **wyłącz Gildię**.

---

## 5 graczy

Wszystkie frakcje. Pełny chaos Haków, Marionetek i Werdyktów (~90+ min).

---

## Checklista przed sesją

1. Wydruk / szkic: [`../game/board/locations.md`](../game/board/locations.md), [`../game/board/player-board.md`](../game/board/player-board.md)
2. Komponenty: [`../game/components/inventory.md`](../game/components/inventory.md), [`../game/components/print-3d.md`](../game/components/print-3d.md)
3. Talie wg warstwy + (C) Kronika Dziejów (10 kart edyktów)
4. Żetony: Herezja, złoto, Relikwie, Fragmenty, Haki, Marionetki, Stosy, Upadek, Dekret, Inkwizytor
5. Sprawdź próg oskarżenia (**7** — Krytyczna Herezja) oraz warstwę A/B/C — zapisz w notatce sesji
6. Wybierz skład z tej strony
7. Po grze: [`sessions/_TEMPLATE.md`](sessions/_TEMPLATE.md) (UX: downtime, AP, emocja Werdyktu)
