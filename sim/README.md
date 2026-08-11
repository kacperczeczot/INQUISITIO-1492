# INQUISITIO 1492 — silnik symulacji

Silnik Python z przebiegiem 4 faz Ery, handlerami 58 kart (Markdown → YAML), agentami **politycznymi** (belief / groźby / bluff / sojusze) oraz batch-raportami A/B progu Herezji.

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
# lista setupów
python -m inquisitio setups

# batch
python -m inquisitio run --games 200 --setup 3p-oficjum-alandalus-korona --threshold 7 --seed 42

# porównanie progu 7 vs 8
python -m inquisitio compare --games 200 --setup 3p-oficjum-alandalus-korona --seed 42
```

Raporty JSON + MD → [`../playtesting/sim-reports/`](../playtesting/sim-reports/).

## Design: Skill > Luck

Losowość **nie może** przeważać wyniku. Implementacja:

| Mechanika | Zasada |
| :--- | :--- |
| Talia Czasu | Odkryj 2 → wybór gracza z najniższym postępem; reszta na spód |
| Szlak Morski | Otwarcie za **3 złota** (Agent na Rynku/Gildii) LUB Flota |
| Mulligan | Do 2 kart na start |
| 1. gracz | Ustalany, nie losowany (kostka tylko przy remisie decyzji) |
| Sim agents | Exploration kart 5%; wybór wydarzenia wg EV frakcji |

Szczegóły reguł: [`../docs/rules/README.md`](../docs/rules/README.md).

## Agenci intrygi

Nie są to boty „losowy legal move”. Każda frakcja ma osobowość:

| Frakcja | Intent |
| :--- | :--- |
| Święte Oficjum | Polowanie na strefę Krytyczną / Stosy |
| Cienie Al-Andalus | Feint transportu Relikwii, ewakuacja |
| Korona | Kontrola Pałac+Rynek, kupowanie procesów |
| Kabała | Sweet spot Herezji 4–6, farm Wskazówek |
| Gildia | Wrabianie (`target_heresy`), Upadek |

Pipeline: observe → belief → threat map → alliance → intent → **bluff/feint lokacji** → act → oskarżenie po EV (nie always-on).

Log decyzji: `intent`, `feint`, `blame`, `accuse_reason` w `GameMetrics.intrigue_log`.

## LLM (opcjonalnie)

Domyślnie **wyłączone** (setki partii lokalnie). Włączenie:

```bash
export INQ_LLM=1
export OPENAI_API_KEY=...          # lub INQ_LLM_KEY
export INQ_LLM_BASE=https://api.openai.com/v1
export INQ_LLM_MODEL=gpt-4o-mini
```

LLM przejmuje tylko forki: wybór lokacji (bluff) i decyzja oskarżenia.

## Karty / wierność

Źródło: [`../game/cards/`](../game/cards/). Parser frontmatter YAML. Każde `id` ma handler w `inquisitio/engine/effects/handlers_*.py`. Semantyka priorytetowa: Herezja, Relikwie, Proces, Kontrola, Wskazówki, Upadek. Pełne odwzorowanie każdego zdania efektu PL nie jest gwarantowane (oznaczenia w kodzie / rozwój).

## Testy

```bash
pytest -q
```

## Układ pakietu

```
inquisitio/
  cards/loader.py
  model/
  engine/          # state, setup, turn, process, effects
  agents/          # intrigue + factions
  llm/adapter.py
  runner/          # batch, report
  cli.py
```
