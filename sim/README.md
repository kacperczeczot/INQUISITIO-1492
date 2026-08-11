# INQUISITIO 1492 — silnik symulacji

Silnik Python pod prototyp polityczny (warstwy **A → B → C**): Herezja, Inkwizytor, Werdykt, Lochy/Podwójni, Haki, Signature, Talia Czasu.  
Karty: Markdown → YAML z [`../game/cards/`](../game/cards/).  
Batch-raporty: dramat + zdrowie reguł → [`../playtesting/sim-reports/`](../playtesting/sim-reports/).

## Instalacja

```bash
cd sim
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -U pip setuptools wheel
pip install -e ".[dev]"
```

Wymaga Python **≥ 3.9** (zalecane 3.11+).

## CLI

```bash
# lista setupów (tylko 3–5p)
python -m inquisitio setups

# batch
python -m inquisitio run --games 50 --setup 3p-oficjum-alandalus-korona --layer C --threshold 7 --seed 42

# porównanie progu Herezji 7 vs 8 (eksperyment dramatu)
python -m inquisitio compare --games 50 --setup 3p-oficjum-alandalus-korona --seed 42
```

## Metryki raportu

| Metryka | Po co |
| :--- | :--- |
| Autodafé / oskarżenia / skazania | Terror publiczny |
| Haki utworzone / wymuszone | Władza prywatna |
| Podwójni | Lochy |
| Deadlocki / legal moves | Zdrowie reguł |
| Długość (Ery) | Tempo |
| Wins | Informacyjnie — sukces produktu mierzy stół |

## Moduły

| Moduł | Warstwa |
| :--- | :--- |
| `state`, `heresy`, `inquisitor`, `verdict`, `turn`, `win` | A |
| `dungeon`, `hooks` | B |
| effects / signature / time edicts | C |
| `agents/politics` | B–C |

## Agenci (heurystyki)

Nie są pełnym blfem ludzkim. Orientacyjne intenty:

| Frakcja | Intent |
| :--- | :--- |
| Święte Oficjum | Nasłanie, Autodafé, Stosy, oskarżenia |
| Cienie Al-Andalus | Relikwie, unik Autodafé, Podwójni |
| Korona | Haki, Dekrety, złoto |
| Kabała | Sweet spot Herezji 4–6, Fragmenty |
| Gildia | Wrabianie, Haki, Upadek |

## Testy

```bash
pytest tests/test_smoke.py -v
```

## Roadmap stołu

Solo Dev-Play / PnP / UX: [`../docs/roadmap.md`](../docs/roadmap.md).  
Zasady: [`../docs/rules/README.md`](../docs/rules/README.md).
