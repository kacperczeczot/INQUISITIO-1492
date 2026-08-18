[Strona główna](../README.md) > [Playtesting](README.md)

---

## Parametry wspólne (zsynchronizowane z `game_config.yaml`)

| Parametr | 3p | 4p (Kanon) / 5p |
| :--- | :--- | :--- |
| Próg Krytycznej (Oskarżenie) | **6** | **7** / **8** |
| Strefa Obserwowana | **5–5** | **5–6** / **5–7** |
| Strefa Krytyczna | **≥6** | **≥7** / **≥8** |
| Karty w Fazie II (Plan) | **2** rundy zagrań / Erę | **2** rundy zagrań / Erę |
| Limit Er | **12** | **12** |
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

| Kod | Skład |
| :--- | :--- |
| **3p (10 kombinacji):** | |
| `3p-oficjum-alandalus-korona` | Oficjum + Cienie + Korona |
| `3p-oficjum-kabala-gildia` | Oficjum + Kabała + Gildia |
| `3p-cienie-korona-gildia` | Cienie + Korona + Gildia *(bez Oficjum)* |
| `3p-oficjum-alandalus-gildia` | Oficjum + Cienie + Gildia |
| `3p-oficjum-alandalus-kabala` | Oficjum + Cienie + Kabała |
| `3p-oficjum-korona-gildia` | Oficjum + Korona + Gildia |
| `3p-oficjum-korona-kabala` | Oficjum + Korona + Kabała |
| `3p-cienie-korona-kabala` | Cienie + Korona + Kabała *(bez Oficjum)* |
| `3p-cienie-kabala-gildia` | Cienie + Kabała + Gildia *(bez Oficjum)* |
| `3p-korona-kabala-gildia` | Korona + Kabała + Gildia *(bez Oficjum)* |
| **4p (5 kombinacji):** | |
| `4p-core` | bez Gildii |
| `4p-no-kabala` | bez Kabały |
| `4p-no-korona` | bez Korony |
| `4p-no-cienie` | bez Cieni |
| `4p-no-oficjum` | bez Oficjum |
| **5p (1 kombinacja):** | |
| `5p-full` | wszystkie 5 frakcji |

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
| Cienie + Korona + Gildia | Polityka bez Oficjum — czy Autodafé/Werdykt wciąż żyją? |
| Oficjum + Cienie + Gildia | Stosy vs Relikwie vs Upadek |

### Notatki 3p

- Gildia i Kabała mają mniej celów — metryki Haków / wrabiania mogą być ostrzejsze.
- Pierwsza sesja: preferuj **Oficjum + Cienie + Korona**.

---

## 4 graczy

Cel: asymetria + sojusze, bez pełnej piątki.

### Którą frakcję wyłączyć

| Wyłącz | Gdy chcesz przetestować |
| :--- | :--- |
| **Gildia Cieni** | Czystszy stół; fokus Relikwie / Stosy / Dekrety |
| **Kabała z Toledo** | Mniej miejsca na manewr Herezją; ostrzejszy Werdykt |
| **Korona** | Mniej Haków/Dekretów; ostrzejsze Relikwie i Stosy |
| **Cienie Al-Andalus** | Brak ewakuacji — fokus Herezja / Upadek / Stosy |
| **Święte Oficjum** | Osobna hipoteza: czy Inkwizytor NPC wystarcza bez gracza-Oficjum |

Domyślnie pierwsza sesja 4p: **wyłącz Gildię**.

---

## 5 graczy

Wszystkie frakcje. Pełny chaos Haków, Marionetek i Werdyktów (~90+ min).

---

## Checklista przed sesją

1. Wydruk / szkic: [`../game/board/locations.md`](../game/board/locations.md), [`../game/board/player-board.md`](../game/board/player-board.md)
2. Komponenty: [`../game/components/inventory.md`](../game/components/inventory.md), [`../game/components/print-3d.md`](../game/components/print-3d.md)
3. Talie wg warstwy + (C) Kronika Dziejów 8
4. Żetony: Herezja, złoto, Relikwie, Fragmenty, Haki, Marionetki, Stosy, Upadek, Dekret, Inkwizytor
5. Sprawdź próg oskarżenia (**6** w 3p, **7** w 4p, **8** w 5p) oraz warstwę A/B/C — zapisz w notatce sesji
6. Wybierz skład z tej strony
7. Po grze: [`sessions/_TEMPLATE.md`](sessions/_TEMPLATE.md) (UX: downtime, AP, emocja Werdyktu)
