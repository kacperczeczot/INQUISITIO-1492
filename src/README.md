[Strona główna](../README.md) > [Symulacja](README.md)

---


# INQUISITIO 1492 — silnik symulacji

Silnik Python pod prototyp (**warstwa C** na stół; A/B = filtry talii w sim).  
Pętla ery: Faza I = zakryta karta **lub** Akcja Gospodarcza (`system.intrigue_gold`); Faza II = Inkwizytor → odkrycie 1→5 → Lochy → Werdykt.  
Karty: Markdown → YAML z [`../game/cards/`](../game/cards/).  

## Instalacja

```bash
cd sim
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -U pip setuptools wheel
pip install -e ".[dev]"
```

Wymaga Python **≥ 3.9** (zalecane 3.11+).

## CLI & Narzędzia Balansujące

```bash
# lista setupów (tylko 3–5p)
python -m inquisitio setups

# Solo Dev-Play — narracyjny log 1 partii
python -m inquisitio feel --setup 3p-oficjum-alandalus-korona --seed 42 --layer C

# heavy sim / matryca
python -m inquisitio run --games 200 --setup 3p-oficjum-alandalus-korona --layer C --threshold 7 --seed 42
python -m inquisitio matrix --games 100 --layers C --seed 42

# porównanie progu Herezji 7 vs 8
python -m inquisitio compare --games 100 --setup 3p-oficjum-alandalus-korona --seed 42 --layer C
```

### 🤖 Autonomiczne Audytory i Optymalizatory Balansu

```bash
# 1. Audytor Kanonu 4P (Główna kotwica: pełna optymalizacja talii 50 kart i parametrów 4P)
python tools/sim/audytor_kanonu.py --workers 10

# 2. Audytor 4P Makro (L1/L2/L4 ±1, Lookahead +1D; bez kart)
python tools/sim/audytor_4p.py --workers 10

# 3. Audytor 3P (Dedykowany optymalizator 10 setupów 3-osobowych z algorytmem Adaptive Lookahead +1D)
python tools/sim/audytor_3p.py --workers 10

# 4. Audytor 5P (Dedykowany optymalizator formatu 5-osobowego z algorytmem Adaptive Lookahead +1D)
python tools/sim/audytor_5p.py --workers 10

# 5. Grand Audit (Pełny audyt poziomów L1–L4, telemetrii 5 filarów i testów stresu ekonomicznego)
python tools/sim/run_grand_audit.py
```

Makro (`audytor_4p.py` / 3p / 5p) wdraża żywe `±1` i lookahead 2D/3D. Nie wdraża: ablacji `off` (w tym Gospodarcza 1→0), agentów (SKU), Werdyktu Tajnego, tempa Kroniki, splitu upadków. Jeździec Δ≈0 (np. Er +1 bez zmiany 4P) odpada przy held. **3p/5p nie zapisują gałek całego stołu** (Gospodarcza, Obserwowana, karty/erę, limit Er, CD Autodafé, szlak) — to kanon 4P. `--dry-run` bez zapisu YAML. Szczegóły: [`docs/rules/hierarchia_balansowania.md`](../docs/rules/hierarchia_balansowania.md) §0 pkt 4.

```bash
# pomiar bez zapisu
python tools/sim/audytor_4p.py --workers 10 --dry-run
```

## Testy

```bash
pytest tests/test_smoke.py tests/test_balance.py -v
# test_balance: 10 setupów × B/C + multi-seed na core compositions
```

## Metryki raportu

| Metryka | Po co |
| :--- | :--- |
| Autodafé / oskarżenia / skazania | Terror publiczny |
| Haki utworzone / wymuszone | Władza prywatna |
| Marionetki | Lochy |
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
| Cienie Al-Andalus | Relikwie, unik Autodafé, Marionetki |
| Korona | Haki, Dekrety, złoto |
| Kabała | Sweet spot Herezji 4–6, Fragmenty |
| Gildia | Wrabianie, Haki, Upadek |

## Roadmap stołu

Kolejność: **heavy sim → feel C → PnP C → sesja pełnych mechanik**.  
Szczegóły: [`../docs/roadmap.md`](../docs/roadmap.md).  
Zasady: hub [`../docs/rules/README.md`](../docs/rules/README.md) · księga [`../docs/rules/ksiega.md`](../docs/rules/ksiega.md) · słownik [`../docs/rules/slownik.md`](../docs/rules/slownik.md).
